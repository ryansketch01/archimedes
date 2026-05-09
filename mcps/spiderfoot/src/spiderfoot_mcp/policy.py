"""Allowlist enforcement for SpiderFoot module selection.

Pulled into its own module because the policy check is the load-bearing
safety primitive — separating it from the HTTP client makes it
trivially testable and gives the test suite a single chokepoint to
prove that no active module ever reaches the wire.
"""

from __future__ import annotations

from spiderfoot_mcp.exceptions import SpiderFootPolicyError
from spiderfoot_mcp.models import (
    _ALLOWLIST_LOWERCASE,
    DEFAULT_MODULES,
    PASSIVE_MODULE_ALLOWLIST,
    PROHIBITED_MODULES,
)


def validate_modules(modules: list[str] | None) -> list[str]:
    """Validate caller-supplied modules against the passive allowlist.

    Behavior:
      - None or empty → DEFAULT_MODULES (same canonical case as the allowlist).
      - Strips `module_` prefix if present (SpiderFoot's wire format).
      - Case-insensitive on input, canonical-case on output.
      - Deduplicates while preserving first-occurrence order.
      - Raises SpiderFootPolicyError with a doctrine pointer if any
        module is not on the allowlist (calling out PROHIBITED_MODULES
        explicitly when matched, since those have specific LEGAL-POLICY
        rationale).

    Returns the cleaned, canonical-case list.
    """
    if not modules:
        return list(DEFAULT_MODULES)

    seen: set[str] = set()
    cleaned: list[str] = []
    rejected: list[str] = []
    prohibited_hits: list[str] = []

    for raw in modules:
        if not isinstance(raw, str):
            rejected.append(repr(raw))
            continue
        stripped = raw.strip()
        if not stripped:
            continue
        # Strip SpiderFoot's wire-format `module_` prefix.
        if stripped.startswith("module_"):
            stripped = stripped[len("module_"):]
        lower = stripped.lower()
        if lower in seen:
            continue
        if lower not in _ALLOWLIST_LOWERCASE:
            if lower in (m.lower() for m in PROHIBITED_MODULES):
                prohibited_hits.append(stripped)
            else:
                rejected.append(stripped)
            continue
        # Recover canonical case from the allowlist.
        canonical = next(
            (m for m in PASSIVE_MODULE_ALLOWLIST if m.lower() == lower), stripped
        )
        seen.add(lower)
        cleaned.append(canonical)

    if prohibited_hits or rejected:
        msg_parts: list[str] = []
        if prohibited_hits:
            msg_parts.append(
                f"Explicitly-prohibited module(s) blocked: "
                f"{', '.join(prohibited_hits)}. These perform active recon "
                "(port scanning, web spidering, brute force, screenshots, "
                "or vulnerability probing) which is forbidden against "
                "non-authorized targets per Hard Rule 4 + LEGAL-POLICY's "
                "SpiderFoot section. Operator must drive SpiderFoot directly "
                "for these against authorized targets."
            )
        if rejected:
            msg_parts.append(
                f"Module(s) not on the passive allowlist: {', '.join(rejected)}. "
                "If a module is genuinely passive but missing here, request a "
                "doctrine update — do not bypass the allowlist."
            )
        raise SpiderFootPolicyError(" ".join(msg_parts))

    if not cleaned:
        # Caller passed only blank/whitespace strings; fall back to defaults
        # so the scan still has *something* to do.
        return list(DEFAULT_MODULES)

    return cleaned
