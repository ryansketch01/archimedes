#!/usr/bin/env python3
"""
discord_listener.py — Long-running Discord listener that bridges
operator-typed slash-style commands in the Archimedes #commands channel
to `claude -p` invocations on the host.

Bridges the same way scripts/run_phase.ps1 bridges Task Scheduler to
the wrapper: receive a structured request, spawn `claude -p` with an
appropriate prompt, capture stdout, ship the result back. Discord
becomes the input channel; Claude Code stays the execution engine.

This is the INBOUND counterpart to scripts/discord_post.py. They share
the same DISCORD_BOT_TOKEN and authenticate against the same bot
identity, but use different transports (REST POST vs WebSocket gateway).

Architecture:
  - discord.py Client connects to the Discord gateway (WebSocket)
  - on_message hook filters by author + channel + command prefix
  - Matched commands spawn `claude -p` via async subprocess
  - claude's stdout posted back to the same channel as a reply
  - Reactions on the trigger message track state: 👀 (received) →
    ✅ (success) or ❌ (failure)

Auth model (intentionally narrow for v1):
  - Only DISCORD_OPERATOR_USER_ID can trigger commands
  - Only the channel matching DISCORD_CHANNEL_COMMANDS is listened to
  - Bots cannot trigger commands (msg.author.bot guard — prevents echo)
  - Unrecognized commands are silently ignored (no useful error to leak)

Supported commands (v1):
  - /investigate <target>  — deep dive on actor, domain, hash, campaign, CVE
  - /ioc-hunt <indicator>  — check an IOC against repo + Splunk + external
  - /ping                  — liveness check; bot replies "pong" without
                             invoking claude (used to verify the listener
                             is actually running)

More commands (/new-actor, /update-tracking, /approve-scoring, /flash, /brief)
are documented in CLAUDE.md as on-demand slash commands. They CAN be added
here later by extending the COMMAND_HANDLERS dict — the bridge pattern is
identical for each.

Long-running supervision:
  Run as a Task Scheduler entry triggered "at log on" with
  RestartOnFailure on. The listener doesn't self-restart on crash; the
  scheduler re-spawns it. Keeping the listener stateless (each command
  is independent) makes restarts safe.

Environment (loaded from <repo>/.env via find_dotenv walk-up):
    DISCORD_BOT_TOKEN              Bot token (from Discord developer portal)
    DISCORD_CHANNEL_COMMANDS       Channel ID to listen on
    DISCORD_OPERATOR_USER_ID       Operator's Discord user ID (numeric, snowflake)
    SPLUNK_HEC_*                   For listener telemetry (optional; logging
                                   to Splunk best-effort, not blocking)

    DISCORD_LISTENER_LOG_DIR       Optional; default: <repo>/logs/discord-listener/

Discord developer-portal prerequisites (one-time):
  1. The bot must have the "Message Content Intent" privileged intent
     ENABLED. Without it, msg.content is empty in on_message. Set at
     https://discord.com/developers/applications/<app-id>/bot
  2. The bot needs View Channel + Read Message History + Send Messages
     + Add Reactions permission in the commands channel.

Exit codes:
    0  Clean shutdown (KeyboardInterrupt or signal)
    2  Configuration error (missing env vars)
    3  Discord auth failure (bad token, intent not enabled, etc.)

Usage:
    uv run python scripts/discord_listener.py

    # In production, invoked via a Task Scheduler entry that wraps
    # this command with -ExecutionPolicy Bypass logic mirroring
    # run_phase.ps1's setup.
"""

from __future__ import annotations

import asyncio
import logging
import os
import shlex
import signal
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Awaitable, Callable

try:
    import discord
    from dotenv import find_dotenv, load_dotenv
except ImportError as e:
    print(
        f"ERROR: missing dependency ({e}). Run: uv sync --all-packages --extra discord",
        file=sys.stderr,
    )
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
SPLUNK_LOG_SCRIPT = REPO_ROOT / "scripts" / "splunk_log.py"

REQUIRED_ENV = (
    "DISCORD_BOT_TOKEN",
    "DISCORD_CHANNEL_COMMANDS",
    "DISCORD_OPERATOR_USER_ID",
)

CLAUDE_TIMEOUT_SECONDS = 600  # 10 min hard cap per command
DISCORD_MAX_CONTENT_LEN = 2000  # Discord per-message ceiling
DISCORD_RESPONSE_RESERVE = 100  # leave headroom for "..." and prefix
DISCORD_BOT_USER_AGENT = "ArchimedesBot/0.1 (listener)"

REACTION_RECEIVED = "👀"
REACTION_OK = "✅"
REACTION_FAIL = "❌"


# ---------------------------------------------------------------------------
# Configuration loading (mirrors discord_post.py)
# ---------------------------------------------------------------------------


def load_env() -> dict[str, str]:
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if env_path:
        load_dotenv(env_path, override=False)

    missing = [k for k in REQUIRED_ENV if not os.environ.get(k)]
    if missing:
        searched_from = env_path or str(REPO_ROOT)
        raise RuntimeError(
            f"Missing required env var(s): {', '.join(missing)}. "
            f"Searched .env from {searched_from}."
        )
    return {k: os.environ[k] for k in REQUIRED_ENV}


def configure_logging() -> logging.Logger:
    log_dir = Path(
        os.environ.get(
            "DISCORD_LISTENER_LOG_DIR",
            str(REPO_ROOT / "logs" / "discord-listener"),
        )
    )
    today = datetime.now().strftime("%Y-%m-%d")
    daily = log_dir / today
    daily.mkdir(parents=True, exist_ok=True)
    log_file = daily / f"listener-{datetime.now().strftime('%H%M%S')}.log"

    logger = logging.getLogger("discord-listener")
    logger.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    logger.info("listener log file: %s", log_file)
    return logger


# ---------------------------------------------------------------------------
# Splunk telemetry — best-effort, never blocks command handling
# ---------------------------------------------------------------------------


async def emit_splunk_event(event: dict, logger: logging.Logger) -> None:
    """Fire-and-forget Splunk event via splunk_log.py. Failures are logged
    but never raised — telemetry is downstream of the listener's primary job.
    """
    if not SPLUNK_LOG_SCRIPT.is_file():
        return  # splunk_log.py absent on this checkout; skip silently

    import json

    try:
        proc = await asyncio.create_subprocess_exec(
            "uv", "run", "python", str(SPLUNK_LOG_SCRIPT),
            "--event", json.dumps(event),
            "--sourcetype", "archimedes:operation",
            "--quiet",
            cwd=REPO_ROOT,
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            await asyncio.wait_for(proc.wait(), timeout=15)
        except asyncio.TimeoutError:
            proc.kill()
            logger.warning("Splunk emit timed out for event %s", event.get("event_type"))
    except Exception as e:  # noqa: BLE001 — telemetry must never crash the listener
        logger.warning("Splunk emit failed for %s: %s", event.get("event_type"), e)


# ---------------------------------------------------------------------------
# Command handlers — each takes the parsed args + returns the prompt to send
# to claude -p. Pure-function shape so they're easy to test and extend.
# ---------------------------------------------------------------------------


def prompt_for_investigate(args: str) -> str:
    target = args.strip()
    if not target:
        raise ValueError("/investigate requires a target (actor, domain, hash, CVE, etc.)")
    return (
        f"Run /investigate {target} per the on-demand command workflow in CLAUDE.md. "
        "Consult .claude/commands/investigate.md if it exists; otherwise use the "
        "investigation pattern documented in CLAUDE.md and doctrine. Apply legal "
        "policy. Return a Smart Brevity summary suitable for posting to Discord — "
        "lead with impact, cite sources, no hedging filler. Keep the response under "
        "1800 characters so it fits one Discord message; if more detail is warranted, "
        "commit a longer write-up to threats/investigations/ and end with the relative "
        "path to that file."
    )


def prompt_for_ioc_hunt(args: str) -> str:
    indicator = args.strip()
    if not indicator:
        raise ValueError("/ioc-hunt requires an indicator (IP, domain, hash, URL)")
    return (
        f"Run /ioc-hunt {indicator} per the on-demand command workflow in CLAUDE.md. "
        "Check the indicator against threats/iocs/_master-index.yaml (both actor "
        "lookup and unattributed_lookup), Splunk first-party indexes (archimedes + "
        "defenseclaw_local), and external enrichment (Shodan / VT / AbuseIPDB / "
        "ThreatFox / abuse.ch as relevant to the indicator type). Apply Hard Rule 8 "
        "first-party precedence. Return a Smart Brevity summary under 1800 chars — "
        "lead with the most operationally meaningful result, then secondary signals."
    )


def prompt_for_new_actor(args: str) -> str:
    name = args.strip()
    if not name:
        raise ValueError(
            "/new-actor requires an actor name (e.g. 'APT45', 'Sandworm', "
            "'UNC9999'). Optionally include a triggering finding id as a "
            "second token: `/new-actor APT45 finding-2026-05-09-0007`."
        )
    return (
        f"Run /new-actor {name} per the on-demand command workflow in CLAUDE.md. "
        "Spawn the actor-profiler subagent to scaffold a full 5-file dossier per "
        "doctrine/ACTOR-PROFILE-STANDARD.md. If a triggering finding is named, "
        "use it as the source for IOC ingestion; otherwise pull from canonical "
        "OSINT (Mandiant / MITRE ATT&CK / Talos / Volexity / Unit 42) for the "
        "first-pass profile. Add the actor to threats/threat-actors/_roster.yaml "
        "at the next available id with full aliases and mitre_attack_id if known. "
        "Leave threat-box.yaml as TEMPLATE (null scores) per scaffold convention; "
        "scoring follows in a separate /update-tracking pass. Per Hard Rule 2, "
        "do NOT originate attribution — every claim must trace to a cited "
        "source. Return a Smart Brevity summary under 1800 chars: actor id, "
        "dossier path, IOC count, attribution lineage."
    )


def prompt_for_update_tracking(args: str) -> str:
    target = args.strip()
    if not target:
        return (
            "Run /update-tracking per the on-demand command workflow in CLAUDE.md "
            "with no target specified — pick the actor whose `last_reviewed` is "
            "oldest in _roster.yaml (or whose `next_review_due` has passed). "
            "Spawn the actor-profiler to refresh that actor's dossier from the "
            "last 90 days of corpus evidence and re-run threat-box scoring. If "
            "the new score is HIGH, do NOT auto-commit — return the proposed "
            "score summary so the operator can review and approve via "
            "/approve-scoring. Return a Smart Brevity summary under 1800 chars: "
            "actor id, what changed, new threat-box overall, gate status."
        )
    return (
        f"Run /update-tracking against actor {target} per the on-demand command "
        "workflow in CLAUDE.md. Spawn the actor-profiler to refresh the dossier "
        "from the last 90 days of corpus evidence and re-run threat-box scoring "
        "via the threat-box-scoring skill. Apply IOC corroboration bonus from "
        "Splunk first-party hits (both archimedes + defenseclaw_local indexes). "
        "If the new score is HIGH, do NOT auto-commit — return the proposed "
        "score summary so the operator can approve via /approve-scoring. If "
        "MEDIUM/LOW, the librarian auto-commits per Mode 4. Return a Smart "
        "Brevity summary under 1800 chars: actor id, what changed, new "
        "threat-box overall, gate status."
    )


def prompt_for_approve_scoring(args: str) -> str:
    actor_id = args.strip()
    if not actor_id:
        raise ValueError(
            "/approve-scoring requires an actor id (e.g. '011' or 'APT37'). "
            "This is the operator-confirmation half of the Hard Rule 5 gate — "
            "the proposed HIGH threat-box score should already be visible in "
            "#actor-review with the AWAITING /approve-scoring tag."
        )
    return (
        f"Run /approve-scoring {actor_id} per the on-demand command workflow in "
        "CLAUDE.md. The operator has reviewed the pending HIGH threat-box "
        "scoring for this actor (visible in #actor-review per Hard Rule 5) and "
        "is authorizing the librarian to commit the threat-box.yaml change to "
        "main. Spawn the librarian in Mode 4 with pending_approval=false. "
        "Verify the review branch (review/actor-<id>-scoring-<date>) exists and "
        "matches the proposed score before merging. Update _roster.yaml's "
        "scoring_pending_approval flag to false and increment "
        "_meta.scoring_complete. Per Hard Rule 5 enforcement: refuse if no "
        "matching review branch exists or if the proposed score is not HIGH. "
        "Return a Smart Brevity summary under 1800 chars: actor id, commit "
        "hash, new threat_level on main."
    )


def prompt_for_cve(args: str) -> str:
    cve_id = args.strip()
    if not cve_id:
        raise ValueError(
            "/cve requires a CVE ID (e.g. 'CVE-2026-0300' or '2026-0300'). "
            "Routes to vuln-tracker for research; scaffolds a dossier if "
            "A&D-relevant and not already tracked."
        )
    # Normalize "2026-0300" -> "CVE-2026-0300" so prompt always carries the
    # canonical form. Defensive only — claude can also handle the bare form.
    normalized = cve_id if cve_id.upper().startswith("CVE-") else f"CVE-{cve_id}"
    return (
        f"Run /cve {normalized} per the on-demand command workflow. Spawn the "
        "vuln-tracker subagent.\n\n"
        "Step 1 — existing-dossier check. Search threats/vulnerabilities/ "
        "(any subdirectory; dossier IDs vary — VT-NNN, ZD-NNN, etc.) for a "
        "dossier whose frontmatter or body references this CVE. If found:\n"
        "  - Return the existing dossier summary: bottom-line state, CVSS + "
        "    KEV status, patch availability, affected products, A&D "
        "    relevance, actor attribution from finding cross-references.\n"
        "  - Note last-updated timestamp. If stale (>14 days) AND the CVE "
        "    is in an active state (active exploitation, no patch, KEV "
        "    deadline approaching), refresh from NVD + vendor advisory + "
        "    CISA KEV before returning the summary.\n\n"
        "Step 2 — if no dossier exists. Research from canonical sources: "
        "NVD record, vendor advisory, CISA KEV, and any Tier-1 vendor "
        "reporting (Mandiant / Unit 42 / MSTIC / Talos / Volexity / Rapid7 "
        "/ Sophos / ESET / Dragos). Determine A&D relevance via three "
        "questions:\n"
        "  - Does the affected product run in defense-contractor or "
        "    aerospace environments?\n"
        "  - Is it part of the supply chain (build tooling, CI/CD, code "
        "    signing, OT/ICS, satellite/spacecraft components)?\n"
        "  - Is it being exploited or anticipated to be exploited against "
        "    A&D targets?\n\n"
        "If A&D-relevant: scaffold a vulnerability dossier per the "
        "vuln-tracker's standard layout (frontmatter with CVE / CVSS / "
        "state / patch / vendor / products / KEV / A&D-relevance, plus "
        "research notes body). If NOT A&D-relevant: return a brief NVD-"
        "style summary without scaffolding — don't bloat the corpus with "
        "irrelevant CVEs.\n\n"
        "Hard Rule 2: don't originate exploitation attribution. If the CVE "
        "is exploited, cite the originating source (CISA KEV adds it via "
        "CISA, vendor reports cite vendors, etc.).\n\n"
        "Return a Smart Brevity summary under 1800 chars: bottom-line "
        "state, CVSS + KEV, patch availability, A&D relevance verdict, "
        "exploitation attribution if any, dossier path if scaffolded or "
        "refreshed."
    )


# Registry: command name -> prompt builder. Each entry bridges to claude -p.
# Add new commands here; the on_message handler picks them up automatically.
COMMAND_HANDLERS: dict[str, Callable[[str], str]] = {
    "investigate": prompt_for_investigate,
    "ioc-hunt": prompt_for_ioc_hunt,
    "new-actor": prompt_for_new_actor,
    "update-tracking": prompt_for_update_tracking,
    "approve-scoring": prompt_for_approve_scoring,
    "cve": prompt_for_cve,
}

# Inline commands handled in-process without invoking claude. Useful as
# liveness / discoverability primitives without burning API tokens.
PING_COMMAND = "ping"
HELP_COMMAND = "help"

HELP_TEXT = (
    "**Archimedes Discord listener — available commands**\n\n"
    "**Inline (no `claude -p`, instant):**\n"
    "  `/ping` — liveness probe; replies pong\n"
    "  `/help` — this message\n\n"
    "**Bridge to `claude -p` (run `~10s`–`~5min` depending on scope):**\n"
    "  `/ioc-hunt <indicator>` — IP / domain / hash / URL lookup vs corpus + Splunk + external\n"
    "  `/investigate <target>` — deep dive on actor / CVE / campaign / domain / hash\n"
    "  `/cve <cve-id>` — vulnerability research; scaffolds a dossier if A&D-relevant\n"
    "  `/new-actor <name> [<finding-id>]` — scaffold a new actor dossier\n"
    "  `/update-tracking [<actor>]` — refresh dossier + re-score (oldest actor if no arg)\n"
    "  `/approve-scoring <actor-id>` — operator confirmation for HIGH-scoring gate (Hard Rule 5)\n\n"
    "**State tracking via reactions:** 👀 received → ✅ success / ❌ failure\n"
    "**Auth:** only the configured operator user ID, only this channel.\n"
    "**Long output:** truncated at ~1800 chars; full output in `logs/discord-listener/`."
)


# ---------------------------------------------------------------------------
# claude -p invocation
# ---------------------------------------------------------------------------


async def invoke_claude(prompt: str, logger: logging.Logger) -> tuple[int, str, str]:
    """Run `claude -p <prompt>` and return (exit_code, stdout, stderr).

    Same flags as scripts/run_phase.ps1: --output-format text and
    --permission-mode bypassPermissions. cwd is the repo root so
    relative paths in claude's context resolve correctly.

    A 10-minute hard cap protects against runaway invocations.
    """
    logger.info("invoking claude -p (prompt length=%d)", len(prompt))

    proc = await asyncio.create_subprocess_exec(
        "claude", "-p", prompt,
        "--output-format", "text",
        "--permission-mode", "bypassPermissions",
        cwd=REPO_ROOT,
        stdin=asyncio.subprocess.DEVNULL,  # avoid the 3s "no stdin" warning
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    try:
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(), timeout=CLAUDE_TIMEOUT_SECONDS
        )
    except asyncio.TimeoutError:
        proc.kill()
        await proc.wait()
        logger.warning("claude -p exceeded %ds timeout; killed", CLAUDE_TIMEOUT_SECONDS)
        return (-1, "", f"Timed out after {CLAUDE_TIMEOUT_SECONDS}s")

    rc = proc.returncode if proc.returncode is not None else -1
    out = stdout.decode("utf-8", errors="replace") if stdout else ""
    err = stderr.decode("utf-8", errors="replace") if stderr else ""
    logger.info("claude -p exited rc=%d (stdout=%dB, stderr=%dB)", rc, len(out), len(err))
    return rc, out, err


# ---------------------------------------------------------------------------
# Discord posting helpers
# ---------------------------------------------------------------------------


def truncate_for_discord(text: str, limit: int = DISCORD_MAX_CONTENT_LEN - DISCORD_RESPONSE_RESERVE) -> str:
    """Trim text to fit a single Discord message. Adds a truncation marker."""
    text = text.strip()
    if len(text) <= limit:
        return text
    cutoff = limit - len("\n\n... [response truncated; full output in logs/discord-listener/]")
    return text[:cutoff].rstrip() + "\n\n... [response truncated; full output in logs/discord-listener/]"


# ---------------------------------------------------------------------------
# Main bot
# ---------------------------------------------------------------------------


def parse_command(content: str) -> tuple[str | None, str]:
    """Strip a leading slash and split into (command_name, rest).

    Examples:
        "/investigate APT37"  -> ("investigate", "APT37")
        "/ping"               -> ("ping", "")
        "hello"               -> (None, "hello")
        "/ unknown"           -> (None, "unknown")  # space after slash is ambiguous; ignore
    """
    text = content.strip()
    if not text.startswith("/"):
        return None, text
    body = text[1:].lstrip()
    if not body:
        return None, ""
    parts = body.split(maxsplit=1)
    cmd = parts[0].lower()
    rest = parts[1] if len(parts) > 1 else ""
    return cmd, rest


def build_client(
    env: dict[str, str],
    logger: logging.Logger,
) -> discord.Client:
    intents = discord.Intents.default()
    # Privileged intent — must be enabled in Discord Developer Portal too
    intents.message_content = True

    client = discord.Client(intents=intents)

    operator_id = int(env["DISCORD_OPERATOR_USER_ID"])
    commands_channel_id = int(env["DISCORD_CHANNEL_COMMANDS"])

    @client.event
    async def on_ready() -> None:
        logger.info(
            "ready as %s (id=%s); listening on channel %s; operator=%s",
            client.user, client.user.id if client.user else "?",
            commands_channel_id, operator_id,
        )
        await emit_splunk_event(
            {
                "event_type": "discord_listener_started",
                "bot_user_id": str(client.user.id) if client.user else None,
                "channel_id": str(commands_channel_id),
                "operator_id": str(operator_id),
                "started_at": datetime.now(timezone.utc).isoformat(),
            },
            logger,
        )

    @client.event
    async def on_message(message: discord.Message) -> None:
        # Filter: only operator, only commands channel, no bot loopback
        if message.author.bot:
            return
        if message.author.id != operator_id:
            return
        if message.channel.id != commands_channel_id:
            return

        cmd, rest = parse_command(message.content)
        if cmd is None:
            return  # not a command; ignore silently

        # Inline commands — handled in-process, no claude invocation
        if cmd == PING_COMMAND:
            logger.info("/ping from operator")
            try:
                await message.add_reaction(REACTION_OK)
                await message.reply(
                    f"pong — `{client.user}` listening since process start",
                    mention_author=False,
                )
            except discord.HTTPException as e:
                logger.warning("/ping reply failed: %s", e)
            return

        if cmd == HELP_COMMAND:
            logger.info("/help from operator")
            try:
                await message.add_reaction(REACTION_OK)
                await message.reply(HELP_TEXT, mention_author=False)
            except discord.HTTPException as e:
                logger.warning("/help reply failed: %s", e)
            return

        if cmd not in COMMAND_HANDLERS:
            # Not a known command — silent ignore. Could be a question or
            # comment that just happened to start with /. Don't leak useful
            # info to anyone watching the channel.
            logger.info("unrecognized command /%s; ignoring", cmd)
            return

        # Recognized command — acknowledge with reaction, then bridge to claude
        run_id = f"discord-{cmd}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        logger.info("handling /%s [run_id=%s] args=%r", cmd, run_id, rest)

        try:
            await message.add_reaction(REACTION_RECEIVED)
        except discord.HTTPException as e:
            logger.warning("reaction add failed (continuing): %s", e)

        try:
            prompt = COMMAND_HANDLERS[cmd](rest)
        except ValueError as ve:
            await _safe_reply(message, f"❌ {ve}", logger)
            await _safe_react(message, REACTION_FAIL, logger)
            return

        await emit_splunk_event(
            {
                "event_type": "discord_command_received",
                "run_id": run_id,
                "command": cmd,
                "args_length": len(rest),
                "operator_id": str(operator_id),
                "channel_id": str(commands_channel_id),
                "received_at": datetime.now(timezone.utc).isoformat(),
            },
            logger,
        )

        rc, out, err = await invoke_claude(prompt, logger)

        if rc == 0:
            response = truncate_for_discord(out) if out else "(empty response)"
            await _safe_reply(message, response, logger)
            await _safe_react(message, REACTION_OK, logger)
            event_type = "discord_command_completed"
        else:
            err_excerpt = (err.strip()[:300] if err else "(no stderr)")
            await _safe_reply(
                message,
                f"❌ /{cmd} failed (rc={rc})\n\n```{err_excerpt}```\nFull log: `logs/discord-listener/`",
                logger,
            )
            await _safe_react(message, REACTION_FAIL, logger)
            event_type = "discord_command_failed"

        await emit_splunk_event(
            {
                "event_type": event_type,
                "run_id": run_id,
                "command": cmd,
                "exit_code": rc,
                "stdout_bytes": len(out),
                "stderr_bytes": len(err),
                "completed_at": datetime.now(timezone.utc).isoformat(),
            },
            logger,
        )

    return client


async def _safe_reply(message: discord.Message, content: str, logger: logging.Logger) -> None:
    """Reply guarded against Discord API exceptions — never crashes the listener."""
    try:
        await message.reply(content, mention_author=False)
    except discord.HTTPException as e:
        logger.error("reply failed: %s (content length=%d)", e, len(content))


async def _safe_react(message: discord.Message, emoji: str, logger: logging.Logger) -> None:
    try:
        await message.add_reaction(emoji)
    except discord.HTTPException as e:
        logger.warning("reaction failed: %s", e)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> int:
    logger = configure_logging()

    try:
        env = load_env()
    except RuntimeError as e:
        logger.error("config error: %s", e)
        return 2

    client = build_client(env, logger)

    # SIGTERM/Ctrl-C clean shutdown via discord.py's own signal handling +
    # a clean Splunk close-event when we exit normally.
    async def runner() -> int:
        try:
            await client.start(env["DISCORD_BOT_TOKEN"])
        except discord.LoginFailure as e:
            logger.error("Discord auth failed (check DISCORD_BOT_TOKEN): %s", e)
            return 3
        except discord.PrivilegedIntentsRequired as e:
            logger.error(
                "Privileged intent missing. Enable 'Message Content Intent' "
                "in the Discord developer portal for this bot. (%s)", e,
            )
            return 3
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received; shutting down")
        except Exception as e:  # noqa: BLE001
            logger.exception("unexpected listener exit: %s", e)
            return 1
        finally:
            if not client.is_closed():
                await client.close()
            await emit_splunk_event(
                {
                    "event_type": "discord_listener_stopped",
                    "stopped_at": datetime.now(timezone.utc).isoformat(),
                },
                logger,
            )
        return 0

    try:
        return asyncio.run(runner())
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
