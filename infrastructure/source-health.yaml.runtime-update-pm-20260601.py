#!/usr/bin/env python3
"""
source-health.yaml runtime-field updater — PM-1 afternoon pre-brief sweep
2026-06-01T15:30:00-04:00.

Per LEGAL-POLICY field-ownership rule (operational notes block in CLAUDE.md):
- Touch ONLY runtime fields: status, last_successful_fetch, failure_count,
  stale_since, last_error
- Preserve `notes` and any unrecognized keys verbatim
- Re-emit entries with all original keys intact

Sources successfully fetched this sweep (status 200, RSS feed parseable,
0 or N items in window):
  - cisa-advisories  (1 item in window - KEV-add - raw-signaled at pm-002)
  - cisa-kev        (1 KEV addition in window - raw-signaled at pm-002)
  - mstic           (parent feed reachable, 0 items in window)
  - unit42          (feedburner reachable, 0 items in window)
  - sans-isc        (rssfeed.xml reachable, 0 items in window)
  - krebs           (1 item in window - Meta AI bot - raw-signaled at pm-003)
  - the-record      (2 items in window, both A&D-non-relevant)
  - bleepingcomputer (2 items in window, both A&D-non-relevant)
  - wired-security   (0 items in window via category feed)
  - securityweek    (2 items in window, both A&D-non-relevant)
  - rapid7          (2 items in window, both anti-noise carry-forward from FLASH-12)
  - sentinelone     (0 items in window)
  - sophos          (0 items in window via threat-research feed)
  - welivesecurity / eset (0 items in window)
  - socket          (Mode 3 WebFetch on blog index + primary URL - blog post on
                    Miasma campaign retrieved successfully - raw-signaled at pm-001;
                    RSS endpoint not used this sweep — direct retrieval substitute)
  - cisco-talos     (RSS feed reachable - alt path failed but no degradation)
  - thehackernews   (4 items in window; Miasma + Dragon Weave items raw-signaled or flagged)

Sources that FAILED or returned errors this sweep:
  - mandiant         feedburner 404 (32nd+ consecutive; held healthy per
                    operator alt-endpoint canonical-swap decision still
                    pending; failure_count not incremented this PM sweep
                    because mandiant was NOT re-queried — sweep used
                    fetch_feed against socket / welivesecurity / sentinelone
                    /sophos/talos directly, NOT feedburner.com/Mandiant)
  - bitdefender      news.sophos.com/en-us/category/threat-research/feed
                    succeeded; BleepingComputer's www.bitdefender.com/blog/labs/
                    RSS endpoint returned 404 this sweep — first soft fail
                    pattern noted but failure_count not incremented because
                    Bitdefender source-health entry uses different endpoint;
                    operator action: investigate canonical bitdefender RSS path
  - blog.talosintelligence.com/feeds/posts/default returned 404 (alt path);
                    /rss/ primary path succeeded — no degradation;
                    failure_count not incremented (the alt /feeds/posts/default
                    is not the configured productive path)
  - socket.dev/blog/rss.xml returned 404 — no source-health entry for socket
                    RSS path; entry uses direct-retrieval pattern. No
                    failure_count change.
  - feedburner.com/Mandiant NOT re-queried this PM sweep.
"""

import sys
from pathlib import Path

# Operator-set fields (preserve verbatim): notes, any unknown
RUNTIME_FIELDS = {"status", "last_successful_fetch", "failure_count",
                  "stale_since", "last_error"}

# Per-source runtime updates this sweep.
# None value = clear the field (set to YAML null / blank in source-health
# representation).
PM_UPDATES = {
    "cisa-advisories": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "cisa-kev": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "mstic": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "unit42": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "sans-isc": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "krebs": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "the-record": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "bleepingcomputer": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "securityweek": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
    "rapid7": {
        "status": "healthy",
        "last_successful_fetch": "'2026-06-01T15:30:00-04:00'",
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
    },
}


def apply_updates(filepath: Path) -> str:
    """
    Read source-health.yaml, apply runtime-field updates per PM_UPDATES,
    return modified file text. Preserves notes verbatim and any
    unrecognized keys.

    Strategy: line-by-line scan. When we encounter "  <key>:" matching
    a source we want to update, we enter "in-entry" mode and modify
    only lines whose key matches RUNTIME_FIELDS. We exit "in-entry"
    mode when we encounter the next "  <key>:" 2-space-indent line.
    """
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=False)
    out_lines: list[str] = []

    current_source: str | None = None
    updates_remaining: dict[str, dict] = {k: v.copy() for k, v in PM_UPDATES.items()}

    for line in lines:
        # Detect a top-level source key at 2-space indent: e.g. "  cisa-kev:"
        # Note: keys can contain hyphens.
        stripped = line.lstrip(" ")
        indent = len(line) - len(stripped)
        if indent == 2 and stripped.endswith(":") and not stripped.startswith("#"):
            # We're at a new source entry.
            new_source = stripped[:-1]
            if new_source in updates_remaining:
                current_source = new_source
            else:
                current_source = None
            out_lines.append(line)
            continue

        # If we're inside a target entry, look for runtime-field lines at
        # 4-space indent: "    status: healthy"
        if current_source is not None and indent == 4 and ":" in stripped:
            # Extract the field key (text before first colon)
            key_part = stripped.split(":", 1)[0]
            if key_part in RUNTIME_FIELDS and key_part in updates_remaining[current_source]:
                new_value = updates_remaining[current_source].pop(key_part)
                if new_value is None:
                    # Clear: emit "    field:"
                    out_lines.append(f"    {key_part}:")
                else:
                    out_lines.append(f"    {key_part}: {new_value}")
                continue

        out_lines.append(line)

    # Update top-of-file last_updated timestamp.
    for i, line in enumerate(out_lines):
        if line.startswith("last_updated:"):
            out_lines[i] = "last_updated: 2026-06-01T15:30:00-04:00"
            break

    # Sanity check: emit warnings for any updates not applied (would indicate
    # the source key was not found in the file).
    for src, remaining in updates_remaining.items():
        if remaining:
            print(f"WARN: source '{src}' updates not all applied: {remaining}",
                  file=sys.stderr)

    return "\n".join(out_lines) + ("\n" if text.endswith("\n") else "")


def main() -> None:
    repo_root = Path(__file__).parent.parent  # infrastructure/ -> repo root
    filepath = repo_root / "infrastructure" / "source-health.yaml"
    if not filepath.exists():
        print(f"ERROR: {filepath} not found", file=sys.stderr)
        sys.exit(1)

    new_text = apply_updates(filepath)
    filepath.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"OK: applied PM-1 runtime updates to {filepath}")


if __name__ == "__main__":
    main()
