"""MCP server for Censys.

Exposes three read-only tools:

  - search_hosts(query, per_page, cursor)        — host search v2
  - lookup_host(ip)                              — host view v2
  - search_certificates(query, per_page, cursor) — certificate search v2

Read-only by design. No DNS scan, no admin endpoints, no submission.
Quota-aware: search consumes the monthly search quota (~100/month
free tier); lookup_host consumes the view quota (~250/month free
tier). Certificate search uses the same monthly search quota as
host search.

Pattern follows mcps/shodan-mcp/server.py and mcps/urlscan/server.py.
"""

from __future__ import annotations

import sys
from typing import Any

from mcp.server.fastmcp import FastMCP

from censys.config import load_config
from censys.exceptions import (
    CensysAuthError,
    CensysConnectionError,
    CensysQuotaExhaustedError,
    CensysRateLimitError,
    CensysRequestError,
)
from censys.models import (
    LookupHostInput,
    SearchCertificatesInput,
    SearchHostsInput,
)
from censys.censys_client import CensysClient

SERVER_NAME = "censys"

mcp = FastMCP(SERVER_NAME)

_client: CensysClient | None = None


def _get_client() -> CensysClient:
    global _client
    if _client is None:
        config = load_config()
        _client = CensysClient(config)
    return _client


def _surface(e: Exception) -> RuntimeError:
    if isinstance(e, CensysAuthError):
        return RuntimeError(f"Censys authentication failed: {e}")
    if isinstance(e, CensysQuotaExhaustedError):
        return RuntimeError(f"Censys monthly quota exhausted: {e}")
    if isinstance(e, CensysRateLimitError):
        return RuntimeError(f"Censys rate limit hit: {e}")
    if isinstance(e, CensysConnectionError):
        return RuntimeError(f"Could not reach Censys: {e}")
    if isinstance(e, CensysRequestError):
        return RuntimeError(f"Censys rejected request: {e}")
    return RuntimeError(f"Unexpected Censys error: {e}")


@mcp.tool()
def search_hosts(query: str, per_page: int = 10, cursor: str | None = None) -> dict[str, Any]:
    """Search Censys hosts (services running on internet-exposed IPs).

    Censys query syntax (v2). Examples:

        services.service_name: HTTP and location.country: "United States"
        autonomous_system.asn: 13335
        services.tls.certificates.leaf_data.subject.common_name: example.com
        services.banner: "OpenSSH" and location.country_code: RU

    Returns trimmed host hits — one per IP — with services list,
    location, ASN, DNS names. Each hit's services include port,
    transport, software stack (when detected), banner excerpt
    (first 200 chars), JA3S/JA4S TLS fingerprints, and leaf cert
    SHA-256.

    Quota: consumes 1 search-quota unit per call (monthly cap ~100
    on free tier). Use cursor pagination if you need more than
    per_page hits.

    Args:
        query: Censys search syntax (Lucene-flavored).
        per_page: Hits per response (1-100; default 10).
        cursor: Pagination cursor from a prior call's `next_cursor`.
    """
    params = SearchHostsInput(query=query, per_page=per_page, cursor=cursor)
    try:
        return _get_client().search_hosts(
            query=params.query, per_page=params.per_page, cursor=params.cursor
        ).model_dump()
    except (
        CensysAuthError, CensysQuotaExhaustedError, CensysRateLimitError,
        CensysConnectionError, CensysRequestError,
    ) as e:
        raise _surface(e) from e


@mcp.tool()
def lookup_host(ip: str) -> dict[str, Any]:
    """Look up a single IP on Censys (host view).

    Returns the same shape as a search-hosts hit but for a specific
    IP — services, location, ASN, DNS names, OS, last-updated-at.
    If Censys has no record for the IP, returns `found: false`.

    Quota: consumes 1 view-quota unit per call (monthly cap ~250 on
    free tier).

    Args:
        ip: IPv4 or IPv6 address.
    """
    params = LookupHostInput(ip=ip)
    try:
        return _get_client().lookup_host(params.ip).model_dump()
    except (
        CensysAuthError, CensysQuotaExhaustedError, CensysRateLimitError,
        CensysConnectionError, CensysRequestError,
    ) as e:
        raise _surface(e) from e


@mcp.tool()
def search_certificates(query: str, per_page: int = 10, cursor: str | None = None) -> dict[str, Any]:
    """Search Censys certificates (cert transparency log + scanning).

    Useful for IOC enrichment: find every cert ever issued for a
    domain, identify cert reuse across infrastructure, hunt for
    Let's Encrypt certs in attacker patterns (7-day cycling, etc.).

    Examples:

        parsed.subject.common_name: example.com
        parsed.issuer.organization: "Let\\'s Encrypt"
        parsed.validity.start: [2026-01-01 to 2026-05-01]
        names: defense-careers-portal.com

    Returns trimmed cert hits — fingerprints, subject CN, issuer DN,
    SAN list, validity window. Drops the parsed cert blob (huge).

    Quota: same as search_hosts — 1 search-quota unit per call.

    Args:
        query: Censys cert search syntax.
        per_page: Hits per response (1-100; default 10).
        cursor: Pagination cursor from a prior call.
    """
    params = SearchCertificatesInput(query=query, per_page=per_page, cursor=cursor)
    try:
        return _get_client().search_certificates(
            query=params.query, per_page=params.per_page, cursor=params.cursor
        ).model_dump()
    except (
        CensysAuthError, CensysQuotaExhaustedError, CensysRateLimitError,
        CensysConnectionError, CensysRequestError,
    ) as e:
        raise _surface(e) from e


def main() -> None:
    """Runtime entry point: validate config eagerly, then run on stdio."""
    try:
        _get_client()
    except RuntimeError as e:
        print(f"[censys] startup failed: {e}", file=sys.stderr)
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
