"""MCP server for RSS/Atom feed fetching.

Exposes two read-only tools:
  - fetch_feed     — fetch + parse a feed; supports ETag/Last-Modified caching
                     and a `since` time filter
  - validate_feed  — quick parseability check, no item ingest

Pattern follows mcps/shodan-mcp/server.py.

Direct fetcher — no dependency on the RSS Bridge software project.
For X/Twitter sources, point this MCP at any RSS bridge URL (community
or self-hosted); it just fetches whatever URL you give it.
"""

from __future__ import annotations

import sys
from typing import Any

from mcp.server.fastmcp import FastMCP

from rss_bridge.config import load_config
from rss_bridge.exceptions import (
    RssBridgeConnectionError,
    RssBridgeParseError,
    RssBridgeRateLimitError,
    RssBridgeRequestError,
)
from rss_bridge.models import (
    FetchFeedInput,
    ValidateFeedInput,
)
from rss_bridge.rss_client import RssBridgeClient

# Claude Code-side MCP name is "rss-bridge". Tool calls are
# mcp__rss-bridge__fetch_feed and mcp__rss-bridge__validate_feed.
SERVER_NAME = "rss-bridge"

mcp = FastMCP(SERVER_NAME)

_client: RssBridgeClient | None = None


def _get_client() -> RssBridgeClient:
    global _client
    if _client is None:
        config = load_config()
        _client = RssBridgeClient(config)
    return _client


def _surface(e: Exception) -> RuntimeError:
    if isinstance(e, RssBridgeRateLimitError):
        return RuntimeError(f"RSS feed rate limit hit: {e}")
    if isinstance(e, RssBridgeConnectionError):
        return RuntimeError(f"Could not reach feed: {e}")
    if isinstance(e, RssBridgeRequestError):
        return RuntimeError(f"Feed host rejected request: {e}")
    if isinstance(e, RssBridgeParseError):
        return RuntimeError(f"Feed body could not be parsed as RSS/Atom: {e}")
    return RuntimeError(f"Unexpected RSS Bridge error: {e}")


@mcp.tool()
def fetch_feed(
    url: str,
    since: str | None = None,
    etag: str | None = None,
    last_modified: str | None = None,
    max_items: int | None = None,
) -> dict[str, Any]:
    """Fetch and parse an RSS or Atom feed.

    Returns the feed's metadata plus a list of items, trimmed to the most
    common CTI fields (title, link, published, summary/content, author,
    guid, categories). HTML is stripped from text fields; summary is
    truncated to 1000 chars and content to 5000.

    Caching: pass `etag` and/or `last_modified` from a prior fetch to take
    advantage of conditional GET. If the feed returns 304 Not Modified,
    output `not_modified=true` and an empty items list — caller should
    reuse cached items.

    Time filter: pass `since` (ISO 8601) to drop items strictly older.
    Items without a `published` timestamp are kept regardless. Items
    with unparseable timestamps are kept (defensive — better to surface
    than silently drop).

    Args:
        url: Full URL of the RSS/Atom feed (https:// or http://).
        since: ISO 8601 timestamp; items with `published` strictly older
            than this are dropped. Null = no time filter.
        etag: Prior ETag value, sent as If-None-Match.
        last_modified: Prior Last-Modified header, sent as
            If-Modified-Since.
        max_items: Cap on items returned after `since` filter.
            Defaults to RSS_BRIDGE_MAX_ITEMS_DEFAULT (50).
    """
    params = FetchFeedInput(
        url=url, since=since, etag=etag, last_modified=last_modified, max_items=max_items
    )
    try:
        return _get_client().fetch_feed(
            params.url,
            since=params.since,
            etag=params.etag,
            last_modified=params.last_modified,
            max_items=params.max_items,
        ).model_dump()
    except (
        RssBridgeRateLimitError,
        RssBridgeConnectionError,
        RssBridgeRequestError,
        RssBridgeParseError,
    ) as e:
        raise _surface(e) from e


@mcp.tool()
def validate_feed(url: str) -> dict[str, Any]:
    """Quick parseability check for a feed URL.

    Lighter than fetch_feed — returns whether the URL points at a
    parseable RSS/Atom feed without ingesting any item content. Used by
    source-health checks and operator triage when a feed has been
    failing.

    Returns valid=true only if the host returns 2xx AND the body parses
    as RSS or Atom AND the feed has metadata or entries. Returns
    valid=false (with an `error` string) on any other outcome —
    connection failure, 4xx/5xx, empty body, malformed XML, HTML
    masquerading as a feed, etc.

    Never raises for connection or parse errors; those are reported via
    valid=false and `error`. Only raises on truly unexpected failures.

    Args:
        url: Full URL of the feed.
    """
    params = ValidateFeedInput(url=url)
    try:
        return _get_client().validate_feed(params.url).model_dump()
    except Exception as e:
        # Defensive — validate_feed is supposed to swallow connection/parse
        # errors and return valid=false, so reaching here is a bug.
        raise _surface(e) from e


def main() -> None:
    """Runtime entry point: validate config eagerly, then run on stdio."""
    try:
        _get_client()
    except RuntimeError as e:
        print(f"[rss-bridge] startup failed: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        mcp.run()
    except KeyboardInterrupt:
        pass
    finally:
        global _client
        if _client is not None:
            _client.close()
            _client = None


if __name__ == "__main__":
    main()
