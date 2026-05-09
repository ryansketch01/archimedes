"""Tests for the passive-module allowlist enforcement.

This is the load-bearing safety primitive — these tests prove no
active SpiderFoot module can reach the wire regardless of caller.
"""

from __future__ import annotations

import pytest

from spiderfoot_mcp.exceptions import SpiderFootPolicyError
from spiderfoot_mcp.models import (
    DEFAULT_MODULES,
    PASSIVE_MODULE_ALLOWLIST,
    PROHIBITED_MODULES,
)
from spiderfoot_mcp.policy import validate_modules


def test_none_returns_default_modules() -> None:
    assert validate_modules(None) == list(DEFAULT_MODULES)


def test_empty_returns_default_modules() -> None:
    assert validate_modules([]) == list(DEFAULT_MODULES)


def test_blank_strings_only_returns_defaults() -> None:
    assert validate_modules(["", "   ", "\t"]) == list(DEFAULT_MODULES)


def test_accepts_passive_modules() -> None:
    out = validate_modules(["sfp_dnsresolve", "sfp_whois", "sfp_crt"])
    assert out == ["sfp_dnsresolve", "sfp_whois", "sfp_crt"]


def test_strips_module_prefix() -> None:
    """SpiderFoot's wire format is `module_<name>`. Caller can pass either form."""
    out = validate_modules(["module_sfp_crt", "sfp_whois"])
    assert out == ["sfp_crt", "sfp_whois"]


def test_case_insensitive_matching() -> None:
    out = validate_modules(["SFP_CRT", "Sfp_Whois", "sfp_DNSRESOLVE"])
    assert out == ["sfp_crt", "sfp_whois", "sfp_dnsresolve"]


def test_dedupes_preserving_order() -> None:
    out = validate_modules(["sfp_crt", "sfp_whois", "sfp_crt", "sfp_whois"])
    assert out == ["sfp_crt", "sfp_whois"]


def test_rejects_active_recon_modules() -> None:
    """All explicitly-prohibited modules must be refused."""
    for prohibited in PROHIBITED_MODULES:
        with pytest.raises(SpiderFootPolicyError, match="prohibited"):
            validate_modules([prohibited])


def test_rejects_unknown_modules() -> None:
    """Anything not on the allowlist (and not in prohibited) is also rejected.

    The allowlist is the real enforcement boundary; the prohibited
    list is documentation. A new SpiderFoot module nobody's seen
    must still be refused — only the allowlist whitelists.
    """
    with pytest.raises(SpiderFootPolicyError, match="not on the passive allowlist"):
        validate_modules(["sfp_some_future_active_module"])


def test_mixed_passive_and_active_rejects_all() -> None:
    """Even if some entries are passive, an active entry rejects the call."""
    with pytest.raises(SpiderFootPolicyError, match="prohibited"):
        validate_modules(["sfp_crt", "sfp_tool_nmap", "sfp_whois"])


def test_error_message_lists_all_rejected_modules() -> None:
    with pytest.raises(SpiderFootPolicyError) as excinfo:
        validate_modules(["sfp_tool_nmap", "sfp_spider", "sfp_dnsbrute"])
    msg = str(excinfo.value)
    assert "sfp_tool_nmap" in msg
    assert "sfp_spider" in msg
    assert "sfp_dnsbrute" in msg


def test_allowlist_is_canonical_case() -> None:
    """All allowlist entries should be lowercase. Defensive check —
    caught a real `securityTrails` casing issue in theHarvester MCP."""
    for m in PASSIVE_MODULE_ALLOWLIST:
        # SpiderFoot conventions are always lowercase + underscore
        assert m == m.lower(), f"Module {m!r} is not lowercase"
        assert m.startswith("sfp_"), f"Module {m!r} missing sfp_ prefix"


def test_default_modules_are_in_allowlist() -> None:
    """Defaults must be a subset of the allowlist (otherwise fallback path explodes)."""
    for m in DEFAULT_MODULES:
        assert m in PASSIVE_MODULE_ALLOWLIST, f"{m} in DEFAULT_MODULES but not allowlist"


def test_prohibited_modules_not_in_allowlist() -> None:
    """Sanity: nothing on the prohibited list is also allowlisted."""
    for m in PROHIBITED_MODULES:
        assert m not in PASSIVE_MODULE_ALLOWLIST, f"{m} is both prohibited AND allowed"


def test_non_string_input_rejected_gracefully() -> None:
    """Caller passing wrong types must surface as a policy error, not a TypeError."""
    with pytest.raises(SpiderFootPolicyError, match="not on the passive allowlist"):
        validate_modules([123, None, {"oops": "dict"}])  # type: ignore[list-item]
