"""MCP server for theHarvester.

Exposes two tools:

  - enumerate(domain, sources, limit) — passive subdomain / host /
    IP / vhost / ASN enumeration via theHarvester
  - list_sources()                    — return the passive-only
    allowlist this MCP enforces, plus the default source set

Email enumeration is intentionally NOT exposed per LEGAL-POLICY PII
handling. Active recon sources (DNS brute-force, takeover) are NOT on
the allowlist and are refused per Hard Rule 4.

Pattern follows mcps/shodan-mcp / mcps/urlscan / mcps/censys but
wraps a CLI subprocess instead of a REST API.
"""

from __future__ import annotations

import sys
from typing import Any

from mcp.server.fastmcp import FastMCP

from theharvester_mcp.config import load_config
from theharvester_mcp.exceptions import (
    TheHarvesterError,
    TheHarvesterNotInstalledError,
    TheHarvesterParseError,
    TheHarvesterPolicyError,
    TheHarvesterRunError,
    TheHarvesterTimeoutError,
)
from theharvester_mcp.harvester_runner import run_theharvester
from theharvester_mcp.models import (
    DEFAULT_SOURCES,
    PASSIVE_SOURCE_ALLOWLIST,
    EnumerateInput,
    ListSourcesOutput,
)

SERVER_NAME = "theharvester"

mcp = FastMCP(SERVER_NAME)

# Cached config — loaded once at startup, reused across calls.
_config = None


def _get_config():
    global _config
    if _config is None:
        _config = load_config()
    return _config


def _surface(e: Exception) -> RuntimeError:
    if isinstance(e, TheHarvesterPolicyError):
        return RuntimeError(f"theHarvester source policy violation: {e}")
    if isinstance(e, TheHarvesterNotInstalledError):
        return RuntimeError(f"theHarvester not installed: {e}")
    if isinstance(e, TheHarvesterTimeoutError):
        return RuntimeError(f"theHarvester timeout: {e}")
    if isinstance(e, TheHarvesterRunError):
        return RuntimeError(f"theHarvester subprocess failed: {e}")
    if isinstance(e, TheHarvesterParseError):
        return RuntimeError(f"theHarvester output parse failed: {e}")
    if isinstance(e, TheHarvesterError):
        return RuntimeError(f"theHarvester error: {e}")
    return RuntimeError(f"Unexpected theHarvester error: {e}")


@mcp.tool()
def enumerate(
    domain: str,
    sources: list[str] | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    """Run passive subdomain / host / IP / vhost / ASN enumeration.

    theHarvester queries third-party OSINT indexes for the target domain
    (cert transparency, search engines, threat-intel feeds). It does NOT
    directly probe the target — Hard Rule 4 (no scanning third parties
    from operator's infrastructure) is satisfied because the queries
    hit the OSINT services, not the target.

    Sources are filtered against a passive-only allowlist (see
    list_sources). Active-recon sources (DNS brute-force, takeover
    detection) are refused.

    Email enumeration is intentionally NOT exposed by this MCP per
    LEGAL-POLICY PII handling. Operator can run `theHarvester -d
    <domain> -b hunter` directly outside the MCP if email enumeration
    is genuinely needed for an authorized investigation.

    Sources that need API keys (Shodan, Censys, SecurityTrails, etc.)
    work if the operator has configured ~/.theHarvester/api-keys.yaml.
    Otherwise theHarvester silently skips them. The default source set
    sticks to keyless sources so it works on a fresh install.

    Args:
        domain: Target domain (e.g., 'example.com').
        sources: Optional list of theHarvester source plugin names.
            Defaults to ['crtsh', 'otx', 'hackertarget', 'rapiddns',
            'sitedossier', 'duckduckgo'] when not specified.
        limit: Optional max results per source (1-10000). Defaults to
            THEHARVESTER_DEFAULT_LIMIT (100) for snappier responses.
    """
    params = EnumerateInput(
        domain=domain,
        sources=sources if sources else list(DEFAULT_SOURCES),
        limit=limit,
    )
    try:
        result = run_theharvester(
            _get_config(),
            domain=params.domain,
            sources=params.sources,
            limit=params.limit,
        )
        return result.model_dump()
    except TheHarvesterError as e:
        raise _surface(e) from e


@mcp.tool()
def list_sources() -> dict[str, Any]:
    """Return the passive-only source allowlist enforced by this MCP,
    plus the default source set used when `enumerate` is called without
    an explicit `sources` arg.

    Useful for operator triage when a desired source isn't accepted —
    inspect the allowlist before guessing.
    """
    return ListSourcesOutput(
        passive_allowlist=list(PASSIVE_SOURCE_ALLOWLIST),
        default_sources=list(DEFAULT_SOURCES),
    ).model_dump()


def main() -> None:
    """Runtime entry point. Validates config eagerly; defers theHarvester
    binary check to first invocation so the server still starts even if
    theHarvester isn't installed yet (the operator gets a clear error
    only when they actually try to use it)."""
    try:
        _get_config()
    except RuntimeError as e:
        print(f"[theharvester-mcp] startup failed: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        mcp.run()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
