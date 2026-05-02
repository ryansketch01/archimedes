#!/usr/bin/env python3
"""
discord_post.py — Post a single message to an Archimedes Discord channel.

Used by Claude Code hooks (the librarian subagent) to publish briefs,
FLASH alerts, actor-review notices, and command-channel control
messages. Mirrors scripts/splunk_log.py — same shape, same error
discipline, same .env loading pattern.

Authentication uses the Discord Bot API (not webhooks). Posting goes
through POST /channels/{channel_id}/messages with `Authorization: Bot
<token>`. Bot must have View Channel + Send Messages perms in the
target channel.

Usage:
    python scripts/discord_post.py --channel commands --message "hello"
    python scripts/discord_post.py --channel intel-briefs --message-file brief.md
    cat brief.md | python scripts/discord_post.py --channel intel-briefs --message-stdin

    # Override the symbolic channel resolution with a raw ID
    python scripts/discord_post.py --channel-id 123456789 --message "..."

Environment (loaded from <repo>/.env via find_dotenv walk-up):
    DISCORD_BOT_TOKEN              Bot token (from Discord developer portal)
    DISCORD_CHANNEL_INTEL_BRIEFS   Channel ID for --channel intel-briefs
    DISCORD_CHANNEL_FLASH_ALERTS   Channel ID for --channel flash-alerts
    DISCORD_CHANNEL_ACTOR_REVIEW   Channel ID for --channel actor-review
    DISCORD_CHANNEL_COMMANDS       Channel ID for --channel commands

Exit codes:
    0  Success — Discord returned 200 with a message object
    2  Configuration error (missing env, bad CLI args, unknown --channel)
    3  Transport error (could not reach discord.com)
    4  Discord rejected the request (4xx or 5xx)
    5  Bad input (message file missing, empty message, exceeds 2000 chars)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import requests
    from dotenv import find_dotenv, load_dotenv
except ImportError as e:
    print(f"ERROR: missing dependency ({e}). Run: uv sync --all-packages", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent

DISCORD_API_BASE = "https://discord.com/api/v10"
DISCORD_MAX_CONTENT_LEN = 2000

CHANNEL_ENV_MAP = {
    "intel-briefs": "DISCORD_CHANNEL_INTEL_BRIEFS",
    "flash-alerts": "DISCORD_CHANNEL_FLASH_ALERTS",
    "actor-review": "DISCORD_CHANNEL_ACTOR_REVIEW",
    "commands": "DISCORD_CHANNEL_COMMANDS",
}


def load_discord_env(channel_env_var: str | None) -> dict[str, str]:
    """Load Discord config from .env. Raises RuntimeError on missing keys.

    Always requires DISCORD_BOT_TOKEN. If channel_env_var is supplied,
    that var must also be set; otherwise --channel-id was used and
    channel resolution is the caller's job.
    """
    import os

    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        raise RuntimeError(
            f"Could not find .env file (searched upward from {Path(__file__).resolve()})."
        )
    load_dotenv(env_path, override=False)

    required = ["DISCORD_BOT_TOKEN"]
    if channel_env_var is not None:
        required.append(channel_env_var)

    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        raise RuntimeError(
            f"Missing required env var(s) in {env_path}: {', '.join(missing)}"
        )
    return {k: os.environ[k] for k in required}


def parse_message_input(args: argparse.Namespace) -> str:
    """Resolve --message / --message-file / --message-stdin into a string.

    Strips trailing whitespace but preserves intentional internal newlines.
    """
    if args.message is not None:
        text = args.message
        source = "--message"
    elif args.message_file is not None:
        text = Path(args.message_file).read_text(encoding="utf-8")
        source = f"--message-file {args.message_file}"
    elif args.message_stdin:
        text = sys.stdin.read()
        source = "--message-stdin"
    else:
        raise ValueError("Must supply one of --message, --message-file, or --message-stdin")

    text = text.rstrip()
    if not text:
        raise ValueError(f"Message input from {source} is empty")

    if len(text) > DISCORD_MAX_CONTENT_LEN:
        raise ValueError(
            f"Message length {len(text)} exceeds Discord limit "
            f"({DISCORD_MAX_CONTENT_LEN}). Split or truncate before posting."
        )
    return text


def resolve_channel_id(args: argparse.Namespace, env: dict[str, str]) -> str:
    """Pick channel_id from --channel-id (raw) or --channel (symbolic)."""
    if args.channel_id is not None:
        return args.channel_id
    env_var = CHANNEL_ENV_MAP[args.channel]
    return env[env_var]


def build_payload(content: str) -> dict[str, Any]:
    """Construct the Discord message payload."""
    return {"content": content}


def post_to_discord(
    *,
    channel_id: str,
    token: str,
    payload: dict[str, Any],
    timeout: float = 10.0,
    session: requests.Session | None = None,
) -> tuple[int, dict[str, Any]]:
    """POST the payload to Discord. Returns (status_code, parsed_body).

    Raises requests.RequestException for transport errors. Body parse
    failures fall back to {"raw": <text>}.
    """
    sess = session or requests
    url = f"{DISCORD_API_BASE}/channels/{channel_id}/messages"
    resp = sess.post(
        url,
        headers={
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json",
            "User-Agent": "ArchimedesBot (https://github.com/archimedes, 0.1)",
        },
        json=payload,
        timeout=timeout,
    )
    try:
        body = resp.json()
    except ValueError:
        body = {"raw": resp.text}
    return resp.status_code, body


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--message", help="Message text as a string")
    src.add_argument("--message-file", help="Path to a file containing the message text")
    src.add_argument("--message-stdin", action="store_true", help="Read message from stdin")

    chan = parser.add_mutually_exclusive_group(required=True)
    chan.add_argument(
        "--channel",
        choices=sorted(CHANNEL_ENV_MAP.keys()),
        help="Symbolic channel name (resolved via env var)",
    )
    chan.add_argument("--channel-id", help="Raw Discord channel ID (bypasses env lookup)")

    parser.add_argument("--timeout", type=float, default=10.0, help="Discord API timeout in seconds")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="On success, suppress Discord response body (still exit 0)",
    )

    args = parser.parse_args(argv)

    channel_env_var = CHANNEL_ENV_MAP[args.channel] if args.channel is not None else None
    try:
        env = load_discord_env(channel_env_var)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    try:
        content = parse_message_input(args)
    except (ValueError, FileNotFoundError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 5

    channel_id = resolve_channel_id(args, env)
    payload = build_payload(content)

    try:
        status, body = post_to_discord(
            channel_id=channel_id,
            token=env["DISCORD_BOT_TOKEN"],
            payload=payload,
            timeout=args.timeout,
        )
    except requests.RequestException as e:
        print(f"ERROR: Discord API unreachable: {e}", file=sys.stderr)
        return 3

    if status >= 400:
        print(f"ERROR: Discord rejected post — status={status} body={body}", file=sys.stderr)
        return 4

    if not args.quiet:
        print(json.dumps({"status": status, "message_id": body.get("id"), "channel_id": channel_id}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
