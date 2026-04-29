"""MCP server for Splunk-query.

Exposes two tools:
  - search: run an SPL query against Splunk and return events
  - health: check Splunk reachability and report version/license info

Transport: stdio (standard for local MCP servers spawned by Claude Code).

Design notes:
  - The FastMCP instance is created at module load with no side effects.
  - The SplunkClient is constructed lazily on first tool call. This lets
    `mcp dev` introspect the server without requiring .env to be present.
  - main() is the runtime entry point: validates config eagerly so missing
    env vars produce a clean stderr error before stdio handshake begins.
"""

from __future__ import annotations

import sys
from typing import Any

from mcp.server.fastmcp import FastMCP

from splunk_query.config import load_config
from splunk_query.exceptions import (
    SplunkAuthError,
    SplunkConnectionError,
    SplunkQueryError,
)
from splunk_query.models import HealthOutput, SearchInput, SearchOutput
from splunk_query.splunk_client import SplunkClient

SERVER_NAME = "splunk-query"

# Module-level server instance. No side effects at construction — `mcp dev`
# can import this module without a working .env.
mcp = FastMCP(SERVER_NAME)

# Lazily initialized on first tool call.
_client: SplunkClient | None = None


def _get_client() -> SplunkClient:
    """Return the shared SplunkClient, constructing it on first use.

    Config is loaded here, not at import time. Errors surface to the
    caller (the tool function), which translates them into MCP errors.
    """
    global _client
    if _client is None:
        config = load_config()
        _client = SplunkClient(config)
    return _client


@mcp.tool()
def search(
    spl: str,
    earliest: str = "-24h@h",
    latest: str = "now",
    max_results: int = 100,
) -> dict[str, Any]:
    """Run an SPL query against the Archimedes Splunk index.

    Use this for first-party data lookups (Hard Rule 8): always check
    what Archimedes has already indexed before reaching for external
    OSINT sources. Common patterns:

        index=archimedes sourcetype=archimedes:operation
        index=archimedes earliest=-7d severity=critical
        | metadata type=sourcetypes index=archimedes

    Args:
        spl: SPL query. 'search ' prefix added automatically if absent.
        earliest: Earliest time bound (default: last 24h).
        latest: Latest time bound (default: now).
        max_results: Cap on returned events (1-10000, default 100).
    """
    params = SearchInput(
        spl=spl, earliest=earliest, latest=latest, max_results=max_results
    )

    try:
        client = _get_client()
        events = client.search(
            spl=params.spl,
            earliest=params.earliest,
            latest=params.latest,
            max_results=params.max_results,
        )
    except SplunkAuthError as e:
        raise RuntimeError(f"Splunk authentication failed: {e}") from e
    except SplunkConnectionError as e:
        raise RuntimeError(f"Could not reach Splunk: {e}") from e
    except SplunkQueryError as e:
        raise RuntimeError(f"Splunk query rejected: {e}") from e

    spl_executed = params.spl.strip()
    if not spl_executed.lower().startswith(("search ", "|")):
        spl_executed = f"search {spl_executed}"

    return SearchOutput(
        event_count=len(events),
        events=events,
        spl_executed=spl_executed,
        earliest=params.earliest,
        latest=params.latest,
    ).model_dump()


@mcp.tool()
def health() -> dict[str, Any]:
    """Check Splunk reachability and return server info.

    Returns version, build, server name, license state, and OS info.

    WARNING: On Splunk Free, the underlying /services/server/info
    endpoint is unauthenticated by design. A successful response means
    Splunk is reachable but does NOT confirm credentials are valid.
    Use the search tool to validate authenticated access.
    """
    try:
        client = _get_client()
        info = client.health()
    except SplunkConnectionError as e:
        return HealthOutput(
            reachable=False,
            note=f"Splunk unreachable: {e}",
        ).model_dump()
    except (SplunkAuthError, SplunkQueryError) as e:
        return HealthOutput(
            reachable=False,
            note=f"Splunk responded with error: {e}",
        ).model_dump()

    return HealthOutput(
        reachable=True,
        version=info.get("version"),
        build=info.get("build"),
        server_name=info.get("server_name"),
        license_state=info.get("license_state"),
        os_name=info.get("os_name"),
        note=(
            "WARNING: /services/server/info is unauthenticated on Splunk Free. "
            "Reachability confirmed; credentials NOT validated."
        ),
    ).model_dump()


def main() -> None:
    """Runtime entry point: validate config eagerly, then run on stdio.

    Validates config before stdio handshake so that a missing env var
    produces a clean stderr error rather than a mid-protocol crash.
    """
    try:
        # Eagerly validate config; cache the resulting client.
        _get_client()
    except RuntimeError as e:
        print(f"[splunk-query] startup failed: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        mcp.run()
    finally:
        global _client
        if _client is not None:
            _client.close()
            _client = None


if __name__ == "__main__":
    main()