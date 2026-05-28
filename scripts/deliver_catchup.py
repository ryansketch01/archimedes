#!/usr/bin/env python3
"""deliver_catchup.py — Deterministic late-delivery of recovered briefs to Discord.

WHY THIS EXISTS
---------------
When a brief phase dies before the librarian runs (the recurring org usage-limit
hit at 08:00 — see CLAUDE.md "A brief phase that dies before the librarian..."),
run_phase.ps1 commits the orphaned corpus with a ``[DEGRADED-RECOVERY]`` marker
but does NOT post to Discord. The brief is fully written and graded; only delivery
failed.

Delivery is deterministic: reading a file, POSTing to Discord, and a git commit
use ZERO model tokens. So this script can run even while the usage limit is still
blocking ``claude -p`` — that is the whole point. Invoked at the end of every
phase by run_phase.ps1, it delivers a recovered brief the same morning (~08:45)
instead of waiting for capacity to return.

WHAT IT DOES
------------
1. Scans recent briefs (``YYYY-MM-DD-{morning,afternoon}.md``) within --lookback-days.
2. Selects ones that are (a) NOT already marked delivered, AND (b) were first
   committed by a ``[DEGRADED-RECOVERY]`` commit (immutable provenance that the
   librarian never posted them). A normally-delivered brief is first-added by a
   "Publish ..." librarian commit and is skipped.
3. Enforces the librarian's TLP gate: only CLEAR / GREEN auto-deliver.
4. Extracts Layer 2 (``## 📣 Discord Summary`` heading to EOF) — same content the
   librarian posts — and chunks it under Discord's 2000-char limit (recovered
   briefs skip the librarian's trim step, so they routinely exceed it).
5. Posts the chunk(s) to #intel-briefs, reusing scripts/discord_post.py's tested
   POST code, with a one-line late-delivery prefix.
6. Writes a ``discord_delivery`` marker into the brief frontmatter (so it never
   re-posts — the on-disk marker is authoritative even if the commit below fails)
   and commits it. The commit is NOT bypassed past gitleaks.

Emits a one-line JSON summary to stdout for the wrapper to parse.

Usage:
    uv run python scripts/deliver_catchup.py [--lookback-days N] [--run-id ID] [--dry-run]

Exit codes:
    0  Ran cleanly (delivered >=0 briefs; see JSON summary)
    2  Configuration error (missing env, etc.)
    3  One or more deliveries failed (see JSON "errors")
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import time
from pathlib import Path

# Reuse the tested Discord POST path. discord_post.py guards main() behind
# __main__, so importing it does not execute anything.
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from discord_post import (  # noqa: E402
        CHANNEL_ENV_MAP,
        DISCORD_MAX_CONTENT_LEN,
        build_payload,
        load_discord_env,
        post_to_discord,
    )
except ImportError as e:
    print(f"ERROR: missing dependency ({e}). Run: uv sync --all-packages", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
BRIEFS_DIR = REPO_ROOT / "threats" / "briefs"

LAYER2_HEADING = "## 📣 Discord Summary"
# Headroom under the hard 2000 limit for the late-delivery prefix and any
# per-part continuation marker.
CHUNK_LIMIT = 1900
TARGET_CHANNEL = "intel-briefs"
DELIVERED_OK_TLP = {"CLEAR", "GREEN"}
# Only morning/afternoon scheduled briefs are in scope; FLASH delivery is the
# librarian's quiet-hours queue, not this path.
BRIEF_NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(morning|afternoon)\.md$")


def run_git(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter_block_without_fences, body). frontmatter is None if absent.

    The frontmatter block excludes the opening/closing '---' fence lines.
    """
    if not text.startswith("---"):
        return None, text
    # Split on the first two '---' fences.
    parts = text.split("\n")
    if parts[0].strip() != "---":
        return None, text
    for i in range(1, len(parts)):
        if parts[i].strip() == "---":
            fm = "\n".join(parts[1:i])
            body = "\n".join(parts[i + 1 :])
            return fm, body
    return None, text


def frontmatter_value(fm: str, key: str) -> str | None:
    """Top-level scalar value for `key` in a simple YAML frontmatter block."""
    if fm is None:
        return None
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", fm)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def has_delivery_marker(fm: str | None) -> bool:
    """True if a discord_delivery block already exists (top-level key)."""
    if fm is None:
        return False
    return re.search(r"(?m)^discord_delivery:\s*$", fm) is not None


def introducing_commit_subject(rel_path: str) -> str | None:
    """Subject of the commit that first added the file (immutable provenance)."""
    cp = run_git(["log", "--diff-filter=A", "--format=%s", "--", rel_path])
    if cp.returncode != 0:
        return None
    lines = [ln for ln in cp.stdout.splitlines() if ln.strip()]
    # --diff-filter=A can in theory list multiple adds (delete+re-add); the
    # last line is the earliest/original add.
    return lines[-1] if lines else None


def extract_layer2(text: str) -> str | None:
    """Return the Layer 2 block (heading through EOF), or None if heading absent."""
    idx = text.find(LAYER2_HEADING)
    if idx == -1:
        return None
    return text[idx:].strip()


def chunk_text(body: str, limit: int, prefix: str = "") -> list[str]:
    """Greedily pack paragraphs into <=limit-char chunks on blank-line boundaries.

    A paragraph longer than the limit is hard-split. The prefix is prepended to
    the first chunk and counted against its budget.
    """
    paragraphs = re.split(r"\n\s*\n", body.strip())
    chunks: list[str] = []
    current = prefix.rstrip("\n")

    def flush():
        nonlocal current
        if current.strip():
            chunks.append(current.strip("\n"))
        current = ""

    for para in paragraphs:
        para = para.strip("\n")
        if not para:
            continue
        # Hard-split an oversized single paragraph.
        while len(para) > limit:
            head, para = para[:limit], para[limit:]
            if current.strip():
                flush()
            chunks.append(head)
        candidate = f"{current}\n\n{para}".strip("\n") if current.strip() else para
        if len(candidate) <= limit:
            current = candidate
        else:
            flush()
            current = para
    flush()
    return chunks


def inject_delivery_marker(path: Path, marker_lines: list[str]) -> bool:
    """Insert a discord_delivery block before the closing frontmatter fence.

    Manual text injection (not a YAML round-trip) to keep the diff minimal.
    Returns False if the file has no frontmatter fence to inject into.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return False
    # Find the closing fence.
    close_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close_idx = i
            break
    if close_idx is None:
        return False
    new_lines = lines[:close_idx] + marker_lines + lines[close_idx:]
    path.write_text("\n".join(new_lines), encoding="utf-8")
    return True


def now_iso() -> str:
    # Local time with offset, matching the rest of the corpus (EDT, -04:00).
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def deliver_one(
    path: Path,
    *,
    token: str,
    channel_id: str,
    run_id: str | None,
    dry_run: bool,
) -> dict:
    """Deliver a single recovered brief. Returns a result dict for the summary."""
    rel = path.relative_to(REPO_ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    fm, _ = split_frontmatter(text)
    brief_id = frontmatter_value(fm, "brief_id") or path.stem
    tlp = (frontmatter_value(fm, "tlp") or "CLEAR").upper()

    layer2 = extract_layer2(text)
    if layer2 is None:
        return {"brief_id": brief_id, "status": "error",
                "reason": f"no '{LAYER2_HEADING}' heading in {rel}"}

    if tlp not in DELIVERED_OK_TLP:
        return {"brief_id": brief_id, "status": "skipped",
                "reason": f"TLP {tlp} requires human approval (only CLEAR/GREEN auto-deliver)"}

    prefix = ("-# :hourglass_flowing_sand: Delivered late by catch-up — "
              "the scheduled pipeline did not post this; content is unchanged.\n\n")
    chunks = chunk_text(layer2, CHUNK_LIMIT, prefix=prefix)
    # Add part markers when multi-part (counted: prefix headroom covers it).
    if len(chunks) > 1:
        chunks = [f"{c}\n\n-# (part {i + 1}/{len(chunks)})" for i, c in enumerate(chunks)]
    # Final safety: never exceed the hard limit.
    for c in chunks:
        if len(c) > DISCORD_MAX_CONTENT_LEN:
            return {"brief_id": brief_id, "status": "error",
                    "reason": f"chunk exceeds {DISCORD_MAX_CONTENT_LEN} after packing"}

    if dry_run:
        return {"brief_id": brief_id, "status": "would_deliver",
                "parts": len(chunks), "layer2_chars": len(layer2), "tlp": tlp}

    message_ids: list[str] = []
    for i, chunk in enumerate(chunks):
        status, body = post_to_discord(
            channel_id=channel_id, token=token, payload=build_payload(chunk)
        )
        if status >= 400:
            # Partial: mark whatever posted so we never re-post the same chunks,
            # but flag for human attention.
            if message_ids:
                _write_marker(path, channel_id, message_ids, len(chunks), run_id, complete=False)
            return {"brief_id": brief_id, "status": "error",
                    "reason": f"discord {status} on part {i + 1}/{len(chunks)}: {body}",
                    "parts_posted": len(message_ids), "parts_total": len(chunks)}
        mid = body.get("id")
        if mid:
            message_ids.append(str(mid))
        time.sleep(0.3)  # preserve ordering, stay clear of channel rate limits

    committed = _write_marker(path, channel_id, message_ids, len(chunks), run_id, complete=True)
    return {"brief_id": brief_id, "status": "delivered",
            "parts": len(chunks), "message_ids": message_ids,
            "marker_committed": committed}


def _write_marker(
    path: Path, channel_id: str, message_ids: list[str], parts: int,
    run_id: str | None, *, complete: bool,
) -> bool:
    """Write the discord_delivery frontmatter marker and commit it. Returns commit ok."""
    ids_inline = "[" + ", ".join(f'"{m}"' for m in message_ids) + "]"
    marker = [
        "discord_delivery:",
        f"  channel: {TARGET_CHANNEL}",
        f"  channel_id: \"{channel_id}\"",
        f"  message_ids: {ids_inline}",
        f"  parts: {parts}",
        f"  delivered_at: {now_iso()}",
        "  late: true",
        "  via: deliver_catchup",
        f"  complete: {str(complete).lower()}",
    ]
    if run_id:
        marker.append(f"  run_id: {run_id}")
    if not inject_delivery_marker(path, marker):
        return False
    rel = path.relative_to(REPO_ROOT).as_posix()
    add = run_git(["add", "--", rel])
    if add.returncode != 0:
        return False
    brief_id = path.stem
    msg = (
        f"deliver: late Discord delivery of {brief_id} (recovered brief, {parts} part(s))\n\n"
        f"{rel} was committed via DEGRADED-RECOVERY without a Discord post. "
        f"deliver_catchup posted Layer 2 to #{TARGET_CHANNEL} (zero model tokens) and "
        f"stamped the discord_delivery marker so it will not re-post.\n\n"
        f"run_id: {run_id or 'n/a'}\n\n"
        "Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
    )
    commit = run_git(["commit", "-m", msg])
    return commit.returncode == 0


def candidate_briefs(lookback_days: int) -> list[Path]:
    """Recent morning/afternoon briefs within the lookback window, newest first."""
    today = dt.date.today()
    floor = today - dt.timedelta(days=lookback_days)
    out: list[tuple[dt.date, Path]] = []
    for p in BRIEFS_DIR.glob("*.md"):
        m = BRIEF_NAME_RE.match(p.name)
        if not m:
            continue
        try:
            d = dt.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if d >= floor:
            out.append((d, p))
    out.sort(key=lambda t: t[0])  # oldest first, so multi-day catch-up posts in order
    return [p for _, p in out]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lookback-days", type=int, default=2,
                    help="Only consider briefs dated within this many days (default 2)")
    ap.add_argument("--run-id", default=None, help="Wrapper run_id for audit trail")
    ap.add_argument("--dry-run", action="store_true",
                    help="Detect and report; do not post or commit")
    args = ap.parse_args(argv)

    summary = {"checked": 0, "delivered": [], "skipped": [], "errors": []}

    token = channel_id = None
    if not args.dry_run:
        try:
            env = load_discord_env(CHANNEL_ENV_MAP[TARGET_CHANNEL])
            token = env["DISCORD_BOT_TOKEN"]
            channel_id = env[CHANNEL_ENV_MAP[TARGET_CHANNEL]]
        except RuntimeError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2

    for path in candidate_briefs(args.lookback_days):
        rel = path.relative_to(REPO_ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)

        # Already delivered (marker present on disk = authoritative).
        if has_delivery_marker(fm):
            continue
        # Provenance gate: only briefs the librarian never posted.
        subj = introducing_commit_subject(rel) or ""
        if not subj.startswith("[DEGRADED-RECOVERY]"):
            continue

        summary["checked"] += 1
        res = deliver_one(path, token=token, channel_id=channel_id,
                          run_id=args.run_id, dry_run=args.dry_run)
        bucket = {"delivered": "delivered", "would_deliver": "delivered",
                  "skipped": "skipped", "error": "errors"}[res["status"]]
        summary[bucket].append(res)

    print(json.dumps(summary))
    return 3 if summary["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
