"""MCP server for SpiderFoot.

Exposes three tools:

  - passive_scan(target, name, modules, target_type)
        Run a passive SpiderFoot scan against a target. Modules are
        validated against the passive allowlist before any HTTP call —
        active modules are refused regardless of caller. Blocks until
        the scan finishes or the configured timeout hits.

  - list_modules()
        Return the passive module allowlist + default set + a sample
        of explicitly-prohibited modules. Useful for the analyst /
        collector subagent to know what's available without trial-and-
        error.

  - health()
        Reachability + auth probe. Returns whether SpiderFoot is up,
        whether configured credentials work, and the daemon URL.

Pattern follows mcps/urlscan/server.py and mcps/theharvester/server.py.
"""

from __future__ import annotations

import sys
from typing import Any

from mcp.server.fastmcp import FastMCP

from spiderfoot_mcp.config import load_config
from spiderfoot_mcp.exceptions import (
    SpiderFootAuthError,
    SpiderFootConnectionError,
    SpiderFootPolicyError,
    SpiderFootRequestError,
    SpiderFootScanError,
    SpiderFootTimeoutError,
)
from spiderfoot_mcp.models import (
    DEFAULT_MODULES,
    PASSIVE_MODULE_ALLOWLIST,
    PROHIBITED_MODULES,
    ListModulesOutput,
    PassiveScanInput,
)
from spiderfoot_mcp.policy import validate_modules
from spiderfoot_mcp.spiderfoot_client import SpiderFootClient

# Claude Code-side MCP name is "spiderfoot". Tool calls become
# mcp__spiderfoot__passive_scan / mcp__spiderfoot__list_modules /
# mcp__spiderfoot__health.
SERVER_NAME = "spiderfoot"

mcp = FastMCP(SERVER_NAME)

_client: SpiderFootClient | None = None


def _get_client() -> SpiderFootClient:
    global _client
    if _client is None:
        config = load_config()
        _client = SpiderFootClient(config)
    return _client


def _surface(e: Exception) -> RuntimeError:
    if isinstance(e, SpiderFootPolicyError):
        return RuntimeError(f"SpiderFoot module policy violation: {e}")
    if isinstance(e, SpiderFootAuthError):
        return RuntimeError(f"SpiderFoot authentication failed: {e}")
    if isinstance(e, SpiderFootTimeoutError):
        return RuntimeError(f"SpiderFoot scan timed out: {e}")
    if isinstance(e, SpiderFootConnectionError):
        return RuntimeError(f"Could not reach SpiderFoot: {e}")
    if isinstance(e, SpiderFootScanError):
        return RuntimeError(f"SpiderFoot scan error: {e}")
    if isinstance(e, SpiderFootRequestError):
        return RuntimeError(f"SpiderFoot rejected request: {e}")
    return RuntimeError(f"Unexpected SpiderFoot error: {e}")


@mcp.tool()
def passive_scan(
    target: str,
    name: str | None = None,
    modules: list[str] | None = None,
    target_type: str | None = None,
) -> dict[str, Any]:
    """Run a passive SpiderFoot scan against a target.

    Modules are validated against the passive allowlist BEFORE any
    HTTP call is made to SpiderFoot. Active modules (port scanning,
    web spidering, DNS brute force, screenshots, vulnerability
    probing) are refused with a SpiderFootPolicyError regardless of
    caller — see LEGAL-POLICY.md "SpiderFoot — Passive-Only Policy".

    The MCP blocks until the scan reaches a terminal state (FINISHED /
    ABORTED / ERROR-FAILED) or the configured timeout
    (SPIDERFOOT_SCAN_TIMEOUT_SECONDS, default 600s) elapses. On timeout,
    partial results are returned with status='RUNNING-TIMEOUT-...' —
    SpiderFoot keeps scanning in the background and the operator can
    revisit via the `web_url` field.

    Returns aggregated output:
      - scan_id, name, target, status
      - modules_used: final module list (post-allowlist filter)
      - duration_seconds: wall-clock waited
      - events: every event SpiderFoot emitted (normalized)
      - distinct_domains, distinct_ips, distinct_emails: convenience folds

    Args:
        target: Target value (domain / IP / CIDR / email / username).
        name: Human-readable scan name (default: 'archimedes-passive-<target>').
        modules: List of SpiderFoot module names. ALL must be in the
            passive allowlist. Defaults to DEFAULT_MODULES (DNS + WHOIS +
            CT + Wayback). Module names accepted with or without the
            `module_` prefix; case-insensitive on input.
        target_type: Optional explicit target type (INTERNET_NAME /
            IP_ADDRESS / NETBLOCK_OWNER / EMAILADDR). Default: SpiderFoot
            infers from the value.
    """
    params = PassiveScanInput(
        target=target, name=name, modules=modules, target_type=target_type
    )

    try:
        cleaned_modules = validate_modules(params.modules)
    except SpiderFootPolicyError as e:
        raise _surface(e) from e

    scan_name = params.name or f"archimedes-passive-{params.target}"

    try:
        out = _get_client().run_passive_scan(
            target=params.target,
            modules=cleaned_modules,
            scan_name=scan_name,
            target_type=params.target_type,
        )
    except (
        SpiderFootAuthError,
        SpiderFootConnectionError,
        SpiderFootScanError,
        SpiderFootRequestError,
        SpiderFootTimeoutError,
    ) as e:
        raise _surface(e) from e

    return out.model_dump()


@mcp.tool()
def list_modules() -> dict[str, Any]:
    """List the SpiderFoot modules this MCP will accept.

    Returns:
        passive_allowlist: Every module name accepted by `passive_scan`.
            All are passive — they query third-party APIs / databases /
            public DNS infrastructure, NOT the target itself.
        default_modules: Used when `passive_scan` is called with no
            `modules` arg.
        prohibited_examples: Sample of explicitly-rejected active modules
            (port scan, brute force, web spider, screenshot, vuln probe).
            The list is illustrative — the real enforcement is the
            allowlist; anything not on the allowlist is refused.
    """
    out = ListModulesOutput(
        passive_allowlist=list(PASSIVE_MODULE_ALLOWLIST),
        default_modules=list(DEFAULT_MODULES),
        prohibited_examples=list(PROHIBITED_MODULES),
    )
    return out.model_dump()


@mcp.tool()
def health() -> dict[str, Any]:
    """Quick reachability + auth probe of the SpiderFoot daemon.

    Returns:
        reachable: True if the daemon answered any request (even auth-rejected).
        authenticated: True if creds were configured and accepted; False if
            configured and rejected; None if no creds configured.
        spiderfoot_version: Version string when the endpoint exposes one.
        url: Base URL the MCP is configured to talk to.
        message: Short human-readable status (especially on failure).

    Use this from the collector subagent before kicking off scans to
    fail fast when SpiderFoot isn't running.
    """
    try:
        return _get_client().health().model_dump()
    except (
        SpiderFootAuthError,
        SpiderFootConnectionError,
        SpiderFootRequestError,
    ) as e:
        raise _surface(e) from e


def main() -> None:
    """Runtime entry point: validate config eagerly, then run on stdio."""
    try:
        _get_client()
    except RuntimeError as e:
        print(f"[spiderfoot] startup failed: {e}", file=sys.stderr)
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
