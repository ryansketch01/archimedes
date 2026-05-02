"""MCP server for Shodan.

Exposes four read-only tools:
  - lookup_host       — full host record (1 query credit)
  - search_hosts      — Shodan query-syntax search (1 credit per page)
  - count_hosts       — query result count, FREE
  - lookup_internetdb — free InternetDB summary (no key, no credits)

Pattern follows mcps/virustotal/server.py.

Read-only by design. No scan submission, no DNS tools, no account
modification. Credit-aware: count_hosts and lookup_internetdb are free
and should be preferred when the question doesn't require host detail.
"""

from __future__ import annotations

import sys
from typing import Any

from mcp.server.fastmcp import FastMCP

from shodan_mcp.config import load_config
from shodan_mcp.exceptions import (
    ShodanAuthError,
    ShodanConnectionError,
    ShodanCreditError,
    ShodanRateLimitError,
    ShodanRequestError,
)
from shodan_mcp.models import (
    CountHostsInput,
    HostLookupInput,
    InternetDbLookupInput,
    SearchHostsInput,
)
from shodan_mcp.shodan_client import ShodanClient

# Claude Code-side MCP name is "shodan" (the package is shodan_mcp to
# avoid colliding with the official PyPI `shodan` SDK). Tool calls are
# mcp__shodan__lookup_host, etc.
SERVER_NAME = "shodan"

mcp = FastMCP(SERVER_NAME)

_client: ShodanClient | None = None


def _get_client() -> ShodanClient:
    global _client
    if _client is None:
        config = load_config()
        _client = ShodanClient(config)
    return _client


def _surface(e: Exception) -> RuntimeError:
    if isinstance(e, ShodanAuthError):
        return RuntimeError(f"Shodan authentication failed: {e}")
    if isinstance(e, ShodanCreditError):
        return RuntimeError(f"Shodan out of credits: {e}")
    if isinstance(e, ShodanRateLimitError):
        return RuntimeError(f"Shodan rate limit hit: {e}")
    if isinstance(e, ShodanConnectionError):
        return RuntimeError(f"Could not reach Shodan: {e}")
    if isinstance(e, ShodanRequestError):
        return RuntimeError(f"Shodan rejected request: {e}")
    return RuntimeError(f"Unexpected Shodan error: {e}")


@mcp.tool()
def lookup_host(ip: str) -> dict[str, Any]:
    """Look up a single IP on Shodan.

    Returns ports, services, banners (excerpted), CVEs, hostnames,
    geo/ASN/org info. Costs 1 query credit per call. If Shodan has no
    record, returns {"found": false, "ip": <input>}.

    Prefer lookup_internetdb first if you only need ports/CPEs/vulns —
    it's free and faster. Use lookup_host when you need the full record.

    Args:
        ip: IPv4 or IPv6 address.
    """
    params = HostLookupInput(ip=ip)
    try:
        return _get_client().lookup_host(params.ip).model_dump()
    except (
        ShodanAuthError, ShodanCreditError, ShodanRateLimitError,
        ShodanConnectionError, ShodanRequestError,
    ) as e:
        raise _surface(e) from e


@mcp.tool()
def search_hosts(query: str, page: int = 1, facets: str | None = None) -> dict[str, Any]:
    """Search Shodan with their query syntax.

    Examples of Shodan query syntax:
        apache port:443
        product:nginx country:CN
        org:"Amazon" port:9200       (open Elasticsearch on AWS)
        vuln:CVE-2021-44228          (hosts with Log4Shell)

    Costs 1 query credit per page (100 results/page). Use count_hosts
    first to see how many results exist before paging through.

    Args:
        query: Shodan query string.
        page: Page number (1-100). Each page is a separate credit.
        facets: Comma-separated facets to compute (e.g. 'country,org').
    """
    params = SearchHostsInput(query=query, page=page, facets=facets)
    try:
        return _get_client().search_hosts(
            query=params.query, page=params.page, facets=params.facets
        ).model_dump()
    except (
        ShodanAuthError, ShodanCreditError, ShodanRateLimitError,
        ShodanConnectionError, ShodanRequestError,
    ) as e:
        raise _surface(e) from e


@mcp.tool()
def count_hosts(query: str, facets: str | None = None) -> dict[str, Any]:
    """Count Shodan results for a query without fetching host details.

    FREE — does not consume query credits. Use this to scope a search
    before paying for results. Returns total count and (optionally)
    facet breakdowns.

    Args:
        query: Shodan query string (same syntax as search_hosts).
        facets: Comma-separated facets, e.g. 'country,port,org'.
    """
    params = CountHostsInput(query=query, facets=facets)
    try:
        return _get_client().count_hosts(
            query=params.query, facets=params.facets
        ).model_dump()
    except (
        ShodanAuthError, ShodanCreditError, ShodanRateLimitError,
        ShodanConnectionError, ShodanRequestError,
    ) as e:
        raise _surface(e) from e


@mcp.tool()
def lookup_internetdb(ip: str) -> dict[str, Any]:
    """Look up an IP on Shodan's free InternetDB.

    Returns ports, hostnames, CPEs, CVEs, tags. No banners, no history,
    no full records — but free, fast, and unauthenticated. Covers most
    "is this IP exposed and what's running" questions.

    Prefer this over lookup_host when you don't need banner content or
    geo/ASN data. Falls back to lookup_host for richer detail.

    Args:
        ip: IPv4 address (InternetDB does not currently support IPv6).
    """
    params = InternetDbLookupInput(ip=ip)
    try:
        return _get_client().lookup_internetdb(params.ip).model_dump()
    except (
        ShodanAuthError, ShodanCreditError, ShodanRateLimitError,
        ShodanConnectionError, ShodanRequestError,
    ) as e:
        raise _surface(e) from e


def main() -> None:
    """Runtime entry point: validate config eagerly, then run on stdio."""
    try:
        _get_client()
    except RuntimeError as e:
        print(f"[shodan-mcp] startup failed: {e}", file=sys.stderr)
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
