"""MCP server for VirusTotal v3.

Exposes four read-only lookup tools:
  - lookup_file   — by MD5/SHA1/SHA256
  - lookup_url    — by URL string
  - lookup_domain — by domain
  - lookup_ip     — by IPv4/IPv6

Transport: stdio. Pattern follows mcps/splunk-query/server.py:
  - FastMCP instance is created at module load with no side effects.
  - VTClient is constructed lazily on first tool call (so `mcp dev` can
    introspect without a working .env).
  - main() validates config eagerly so missing env produces a clean
    stderr error before stdio handshake.

Read-only on purpose. No file uploads, no comments, no votes — those
broaden the trust boundary in ways the analyst-side use case doesn't need.
"""

from __future__ import annotations

import sys
from typing import Any

from mcp.server.fastmcp import FastMCP

from virustotal.config import load_config
from virustotal.exceptions import (
    VTAuthError,
    VTConnectionError,
    VTRateLimitError,
    VTRequestError,
)
from virustotal.models import (
    DomainLookupInput,
    FileLookupInput,
    IpLookupInput,
    UrlLookupInput,
)
from virustotal.vt_client import VTClient

SERVER_NAME = "virustotal"

mcp = FastMCP(SERVER_NAME)

_client: VTClient | None = None


def _get_client() -> VTClient:
    """Return the shared VTClient, constructing it on first use."""
    global _client
    if _client is None:
        config = load_config()
        _client = VTClient(config)
    return _client


def _surface(e: Exception) -> RuntimeError:
    """Translate domain exceptions into the RuntimeErrors MCP returns."""
    if isinstance(e, VTAuthError):
        return RuntimeError(f"VirusTotal authentication failed: {e}")
    if isinstance(e, VTRateLimitError):
        return RuntimeError(f"VirusTotal rate limit hit: {e}")
    if isinstance(e, VTConnectionError):
        return RuntimeError(f"Could not reach VirusTotal: {e}")
    if isinstance(e, VTRequestError):
        return RuntimeError(f"VirusTotal rejected request: {e}")
    return RuntimeError(f"Unexpected VirusTotal error: {e}")


@mcp.tool()
def lookup_file(file_hash: str) -> dict[str, Any]:
    """Look up a file by hash on VirusTotal.

    Returns analysis stats (malicious/suspicious/harmless/undetected counts),
    reputation, file type, known names, and the engines that flagged it as
    malicious. If VT has no record, returns {"found": false}.

    Use for hash IOCs from threat reports. Free-tier rate limit applies
    (4 req/min, 500/day) — batch with care.

    Args:
        file_hash: MD5 (32 hex), SHA1 (40 hex), or SHA256 (64 hex).
    """
    params = FileLookupInput(file_hash=file_hash)
    try:
        return _get_client().lookup_file(params.file_hash).model_dump()
    except (VTAuthError, VTConnectionError, VTRateLimitError, VTRequestError) as e:
        raise _surface(e) from e


@mcp.tool()
def lookup_url(url: str) -> dict[str, Any]:
    """Look up a URL on VirusTotal.

    Returns analysis stats, vendor categorizations (e.g. phishing, malware),
    page title, and the engines that flagged it as malicious. If VT has no
    record, returns {"found": false}.

    Use for suspicious links in phishing reports, C2 indicators, etc.

    Args:
        url: Full URL including scheme (http:// or https://).
    """
    params = UrlLookupInput(url=url)
    try:
        return _get_client().lookup_url(params.url).model_dump()
    except (VTAuthError, VTConnectionError, VTRateLimitError, VTRequestError) as e:
        raise _surface(e) from e


@mcp.tool()
def lookup_domain(domain: str) -> dict[str, Any]:
    """Look up a domain on VirusTotal.

    Returns analysis stats, registrar, creation/update timestamps, vendor
    categorizations, and popularity ranks (Cisco Umbrella, Majestic, etc.
    when available). If VT has no record, returns {"found": false}.

    Use for domain IOCs from actor campaigns, suspect lookalikes, etc.

    Args:
        domain: Bare domain (no scheme, no path). Example: "example.com".
    """
    params = DomainLookupInput(domain=domain)
    try:
        return _get_client().lookup_domain(params.domain).model_dump()
    except (VTAuthError, VTConnectionError, VTRateLimitError, VTRequestError) as e:
        raise _surface(e) from e


@mcp.tool()
def lookup_ip(ip: str) -> dict[str, Any]:
    """Look up an IP address on VirusTotal.

    Returns analysis stats, country, ASN/AS owner, network CIDR, and the
    engines that flagged the IP as malicious. If VT has no record, returns
    {"found": false}.

    Use for C2 IPs, scanner sources, infrastructure mapping.

    Args:
        ip: IPv4 (e.g. "8.8.8.8") or IPv6 address.
    """
    params = IpLookupInput(ip=ip)
    try:
        return _get_client().lookup_ip(params.ip).model_dump()
    except (VTAuthError, VTConnectionError, VTRateLimitError, VTRequestError) as e:
        raise _surface(e) from e


def main() -> None:
    """Runtime entry point: validate config eagerly, then run on stdio."""
    try:
        _get_client()
    except RuntimeError as e:
        print(f"[virustotal] startup failed: {e}", file=sys.stderr)
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
