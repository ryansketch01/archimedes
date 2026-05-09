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


# Registry: command name -> prompt builder. Add entries here as new commands
# are wired up (e.g. /new-actor, /update-tracking, /flash, /brief).
COMMAND_HANDLERS: dict[str, Callable[[str], str]] = {
    "investigate": prompt_for_investigate,
    "ioc-hunt": prompt_for_ioc_hunt,
}

# /ping is special: handled in-process without invoking claude. Useful as
# a liveness probe without burning API tokens.
PING_COMMAND = "ping"


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

        # Liveness probe — handle inline, no claude
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
