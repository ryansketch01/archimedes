#!/usr/bin/env python3
"""
splunk-log.py — Send a single event to the Archimedes Splunk HEC.

Used by Claude Code hooks (the librarian subagent) to ship pipeline
telemetry to the archimedes index. Mirrors:
  - scripts/regenerate-ioc-index.py — CLI shape, REPO_ROOT pattern, stderr errors
  - mcps/splunk-query — .env loading via python-dotenv

Stays narrow on purpose. The splunk-query MCP is the read path (REST API,
port 8089). This is the write path (HEC, port 8088). Different ports,
different auth, different audiences (LLM analysis vs. orchestration plumbing).

Usage:
    python scripts/splunk-log.py --event '{"phase":"morning-brief"}'
    python scripts/splunk-log.py --event-file path/to/event.json
    cat event.json | python scripts/splunk-log.py --event-stdin

    # Override the default sourcetype for this event
    python scripts/splunk-log.py --event '{...}' --sourcetype archimedes:brief

Environment (loaded from <repo>/.env via find_dotenv walk-up):
    SPLUNK_HEC_URL          Full URL incl. /services/collector/event
    SPLUNK_HEC_TOKEN        HEC token (UUID)
    SPLUNK_HEC_INDEX        Default index (e.g. archimedes)
    SPLUNK_HEC_SOURCETYPE   Default sourcetype (e.g. archimedes:operation)

Exit codes:
    0  Success — HEC returned 200 with code:0
    2  Configuration error (missing env, bad CLI args)
    3  Transport error (could not reach HEC)
    4  HEC rejected the event (non-200 or non-zero code in body)
    5  Bad JSON input
"""

from __future__ import annotations

import argparse
import json
import socket
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

REQUIRED_ENV = (
    "SPLUNK_HEC_URL",
    "SPLUNK_HEC_TOKEN",
    "SPLUNK_HEC_INDEX",
    "SPLUNK_HEC_SOURCETYPE",
)


def load_hec_env() -> dict[str, str]:
    """Load HEC config from .env. Raises RuntimeError on missing keys."""
    import os

    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        raise RuntimeError(
            f"Could not find .env file (searched upward from {Path(__file__).resolve()})."
        )
    load_dotenv(env_path, override=False)

    missing = [k for k in REQUIRED_ENV if not os.environ.get(k)]
    if missing:
        raise RuntimeError(
            f"Missing required env var(s) in {env_path}: {', '.join(missing)}"
        )
    return {k: os.environ[k] for k in REQUIRED_ENV}


def parse_event_input(args: argparse.Namespace) -> dict[str, Any]:
    """Resolve --event / --event-file / --event-stdin into a parsed dict."""
    if args.event is not None:
        raw = args.event
        source = "--event"
    elif args.event_file is not None:
        raw = Path(args.event_file).read_text(encoding="utf-8")
        source = f"--event-file {args.event_file}"
    elif args.event_stdin:
        raw = sys.stdin.read()
        source = "--event-stdin"
    else:
        raise ValueError("Must supply one of --event, --event-file, or --event-stdin")

    raw = raw.strip()
    if not raw:
        raise ValueError(f"Event input from {source} is empty")

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Event input from {source} is not valid JSON: {e}") from e

    if not isinstance(parsed, dict):
        raise ValueError(
            f"Event input from {source} must be a JSON object, got {type(parsed).__name__}"
        )
    return parsed


def build_payload(
    event: dict[str, Any],
    *,
    index: str,
    sourcetype: str,
    host: str,
    source: str,
) -> dict[str, Any]:
    """Construct the HEC payload envelope around the event body."""
    return {
        "event": event,
        "sourcetype": sourcetype,
        "index": index,
        "host": host,
        "source": source,
    }


def post_to_hec(
    *,
    url: str,
    token: str,
    payload: dict[str, Any],
    timeout: float = 10.0,
    session: requests.Session | None = None,
) -> tuple[int, dict[str, Any]]:
    """POST the payload to HEC. Returns (status_code, parsed_body).

    Raises requests.RequestException for transport errors (caller decides
    how to surface). Body parse failures fall back to {"raw": <text>}.
    """
    sess = session or requests
    resp = sess.post(
        url,
        headers={"Authorization": f"Splunk {token}"},
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
    src.add_argument("--event", help="JSON object as a string")
    src.add_argument("--event-file", help="Path to a file containing a JSON object")
    src.add_argument("--event-stdin", action="store_true", help="Read JSON object from stdin")

    parser.add_argument("--sourcetype", help="Override SPLUNK_HEC_SOURCETYPE for this event")
    parser.add_argument("--index", help="Override SPLUNK_HEC_INDEX for this event")
    parser.add_argument("--host", default=None, help="Host field (default: socket.gethostname())")
    parser.add_argument(
        "--source",
        default="archimedes/scripts/splunk-log.py",
        help="Source field (default: this script)",
    )
    parser.add_argument("--timeout", type=float, default=10.0, help="HEC timeout in seconds")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="On success, suppress HEC response body (still exit 0)",
    )

    args = parser.parse_args(argv)

    try:
        env = load_hec_env()
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    try:
        event = parse_event_input(args)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 5

    payload = build_payload(
        event,
        index=args.index or env["SPLUNK_HEC_INDEX"],
        sourcetype=args.sourcetype or env["SPLUNK_HEC_SOURCETYPE"],
        host=args.host or socket.gethostname(),
        source=args.source,
    )

    try:
        status, body = post_to_hec(
            url=env["SPLUNK_HEC_URL"],
            token=env["SPLUNK_HEC_TOKEN"],
            payload=payload,
            timeout=args.timeout,
        )
    except requests.RequestException as e:
        print(f"ERROR: HEC unreachable at {env['SPLUNK_HEC_URL']}: {e}", file=sys.stderr)
        return 3

    if status != 200 or body.get("code") not in (0, None):
        print(f"ERROR: HEC rejected event — status={status} body={body}", file=sys.stderr)
        return 4

    if not args.quiet:
        print(json.dumps({"status": status, "body": body}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
