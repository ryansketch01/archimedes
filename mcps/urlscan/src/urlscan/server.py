"""MCP server for urlscan.io.

Exposes three tools:

  - search(query, size)       — search past public scans
  - lookup_scan(uuid)         — fetch a single scan's full record
  - submit_scan(url, ...)     — submit a new URL for scanning

Read-heavy by design: search and lookup_scan use no submit quota.
submit_scan is included because operationally-driven CTI work
("scan this suspicious URL right now") is the obvious complement to
lookup, but consumes the 5,000/month free-tier scan quota — prefer
search first when the question is "has anyone seen this before?".

Pattern follows mcps/shodan-mcp/server.py and mcps/virustotal/server.py.
"""

from __future__ import annotations

import sys
from typing import Any

from mcp.server.fastmcp import FastMCP

from urlscan.config import load_config
from urlscan.exceptions import (
    UrlscanAuthError,
    UrlscanConnectionError,
    UrlscanRateLimitError,
    UrlscanRequestError,
    UrlscanScanDeniedError,
)
from urlscan.models import (
    LookupScanInput,
    SearchInput,
    SubmitScanInput,
)
from urlscan.urlscan_client import UrlscanClient

# Claude Code-side MCP name is "urlscan". Tool calls are
# mcp__urlscan__search, mcp__urlscan__lookup_scan, mcp__urlscan__submit_scan.
SERVER_NAME = "urlscan"

mcp = FastMCP(SERVER_NAME)

_client: UrlscanClient | None = None


def _get_client() -> UrlscanClient:
    global _client
    if _client is None:
        config = load_config()
        _client = UrlscanClient(config)
    return _client


def _surface(e: Exception) -> RuntimeError:
    if isinstance(e, UrlscanAuthError):
        return RuntimeError(f"urlscan authentication failed: {e}")
    if isinstance(e, UrlscanRateLimitError):
        return RuntimeError(f"urlscan rate limit hit: {e}")
    if isinstance(e, UrlscanScanDeniedError):
        return RuntimeError(f"urlscan denied scan submission: {e}")
    if isinstance(e, UrlscanConnectionError):
        return RuntimeError(f"Could not reach urlscan: {e}")
    if isinstance(e, UrlscanRequestError):
        return RuntimeError(f"urlscan rejected request: {e}")
    return RuntimeError(f"Unexpected urlscan error: {e}")


@mcp.tool()
def search(query: str, size: int = 10) -> dict[str, Any]:
    """Search past public urlscan.io scans.

    Field-qualified examples:
        domain:example.com
        ip:1.2.3.4
        page.country:RU AND page.tlsAgeDays:<30
        hash:<sha256>
        task.url:"https://example.com/login*"

    Free text without a field qualifier matches any URL field.

    Returns metadata for matching scans. Each result has a `uuid` you
    can pass to lookup_scan for the full record. Search is unmetered
    on the free tier (no submit quota consumed).

    Args:
        query: urlscan search query (Lucene-style; see urlscan.io docs).
        size: Max results to return (1-10000; default 10).
    """
    params = SearchInput(query=query, size=size)
    try:
        return _get_client().search(query=params.query, size=params.size).model_dump()
    except (
        UrlscanAuthError, UrlscanRateLimitError, UrlscanConnectionError, UrlscanRequestError,
    ) as e:
        raise _surface(e) from e


@mcp.tool()
def lookup_scan(uuid: str) -> dict[str, Any]:
    """Fetch a urlscan.io scan result by UUID.

    Returns the trimmed scan record: task, page (post-redirect URL +
    IP/country/server), stats, verdicts (overall + urlscan +
    community + engines), indicator lists (ips/domains/asns/countries
    /servers/hashes — URLs intentionally dropped due to volume), and
    pointers to the full result API URL plus the urlscan.io web GUI.

    If urlscan has no record for this UUID (typo, scan not yet
    finished, or scan was deleted), returns `found: false` rather
    than raising.

    Args:
        uuid: Scan UUID. Get from search() results or submit_scan() output.
    """
    params = LookupScanInput(uuid=uuid)
    try:
        return _get_client().lookup_scan(params.uuid).model_dump()
    except (
        UrlscanAuthError, UrlscanRateLimitError, UrlscanConnectionError, UrlscanRequestError,
    ) as e:
        raise _surface(e) from e


@mcp.tool()
def submit_scan(
    url: str,
    visibility: str = "public",
    tags: list[str] | None = None,
    referer: str | None = None,
    user_agent: str | None = None,
) -> dict[str, Any]:
    """Submit a new URL to urlscan.io for scanning.

    urlscan.io visits the URL from THEIR infrastructure (not yours),
    so this is acceptable under Hard Rule 4 (no scanning third
    parties from your own infrastructure). However:

      - The scan is logged on urlscan.io with your account context
      - Public scans are searchable by other urlscan users — prefer
        `unlisted` or `private` visibility if the URL contains
        sensitive context, internal hostnames, or query-string secrets
      - Free-tier limit: 5,000 public scans/month + 1,000 unlisted +
        1,000 private. Search() doesn't consume this; prefer search
        first when the question is "has anyone scanned this before?"

    The scan is async — typically takes 15-30 seconds to complete.
    Output returns the UUID immediately; poll with lookup_scan(uuid)
    after a wait.

    Args:
        url: URL to scan. Must include scheme (http:// or https://).
        visibility: public / unlisted / private (default 'public').
        tags: Optional tags to apply (e.g., ['archimedes', 'ioc-hunt']).
        referer: Optional Referer header for the scan.
        user_agent: Optional User-Agent override (default: urlscan UA).
    """
    params = SubmitScanInput(
        url=url, visibility=visibility, tags=tags or [], referer=referer, user_agent=user_agent
    )
    try:
        return _get_client().submit_scan(
            url=params.url,
            visibility=params.visibility,
            tags=params.tags,
            referer=params.referer,
            user_agent=params.user_agent,
        ).model_dump()
    except (
        UrlscanAuthError,
        UrlscanRateLimitError,
        UrlscanScanDeniedError,
        UrlscanConnectionError,
        UrlscanRequestError,
    ) as e:
        raise _surface(e) from e


def main() -> None:
    """Runtime entry point: validate config eagerly, then run on stdio."""
    try:
        _get_client()
    except RuntimeError as e:
        print(f"[urlscan] startup failed: {e}", file=sys.stderr)
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
