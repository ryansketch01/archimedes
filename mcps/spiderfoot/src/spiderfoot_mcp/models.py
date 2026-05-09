"""Pydantic models and the passive-module allowlist for the SpiderFoot MCP.

The allowlist is the load-bearing contract here. Any module not on it
is refused — the MCP cannot be used to drive active recon (port
scanning, web spidering, DNS brute force, screenshot capture,
vulnerability probing) regardless of caller. This is enforced at
input validation, before any HTTP call to SpiderFoot.

Active modules outside this allowlist may be perfectly legitimate
when SpiderFoot is run against a target in
`infrastructure/authorized-targets.yaml`, but that workflow goes
direct to SpiderFoot's web UI / CLI and bypasses this MCP. The MCP's
role is to be safe-by-default for analyst-driven CTI collection.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


# ---------- passive module allowlist ----------

# Sources of truth this list is reconciled against:
#   - doctrine/LEGAL-POLICY.md "SpiderFoot — Passive-Only Policy"
#   - .claude/agents/collector.md "SpiderFoot — passive-only enforcement"
#
# Each entry is a SpiderFoot module name (the value passed in
# `modulelist` to /startscan, with the leading `module_` prefix
# replaced by `sfp_` per SpiderFoot's convention). Modules below are
# all passive — they query third-party APIs / databases / public DNS
# infrastructure, not the target itself.
PASSIVE_MODULE_ALLOWLIST: tuple[str, ...] = (
    # --- DNS (passive — public resolver lookups, not target probing) ---
    "sfp_dnsresolve",        # Resolve hostnames to IPs (public DNS)
    "sfp_dnscommonsrv",      # Common SRV record lookups
    "sfp_dnsneighbor",       # Adjacent IPs (passive PTR sweep limited to /24)
    "sfp_dnszonexfr",        # AXFR attempt (passive — fails on locked-down zones)

    # --- WHOIS / registration ---
    "sfp_whois",             # WHOIS queries
    "sfp_dnsdb",             # Passive DNS via DNSDB (paid feed)

    # --- Certificate Transparency ---
    "sfp_crt",               # crt.sh CT log lookups
    "sfp_certspotter",       # Cert Spotter CT logs

    # --- Search engines (passive — search third-party indexes, not the target) ---
    "sfp_bingsearch",
    "sfp_duckduckgo",
    "sfp_googlesearch",
    "sfp_yandexsearch",

    # --- Threat intelligence feed lookups ---
    "sfp_virustotal",
    "sfp_threatfox",
    "sfp_alienvault",        # AlienVault OTX
    "sfp_threatcrowd",
    "sfp_shodan",            # Shodan index lookup (passive — Shodan scanned, not us)
    "sfp_censys",            # Censys index lookup
    "sfp_greynoise",
    "sfp_abuseipdb",
    "sfp_urlscanio",         # urlscan.io history lookup

    # --- Breach membership (membership only, not extraction) ---
    "sfp_hibp_pastes",       # HIBP paste membership
    "sfp_hibp",              # HIBP breach membership

    # --- Reputation / blocklist databases ---
    "sfp_spamcop",
    "sfp_spamhaus",
    "sfp_phishtank",
    "sfp_malwarepatrol",
    "sfp_torch",             # Tor exit node check (passive list lookup)

    # --- Public archives ---
    "sfp_archiveorg",        # Wayback Machine
    "sfp_commoncrawl",

    # --- Pastebin / paste-site monitoring (passive search of third-party indexes) ---
    "sfp_pastebin",

    # --- Code search (passive — searches third-party repos, not target) ---
    "sfp_github",            # GitHub code search for target mentions
)

# Lowercase set for case-insensitive caller input matching.
_ALLOWLIST_LOWERCASE: frozenset[str] = frozenset(m.lower() for m in PASSIVE_MODULE_ALLOWLIST)

# Modules explicitly prohibited — listed for documentation. Caller
# supplying any of these triggers SpiderFootPolicyError with a clear
# pointer to LEGAL-POLICY. Not exhaustive; the allowlist is the real
# enforcement boundary.
PROHIBITED_MODULES: tuple[str, ...] = (
    "sfp_tool_nmap",         # Port scanning
    "sfp_tool_nuclei",       # Vulnerability probing
    "sfp_tool_nbtscan",      # NetBIOS scanning
    "sfp_tool_dnstwist",     # DNS twist (active enumeration)
    "sfp_tool_wafw00f",      # WAF fingerprinting (active probe)
    "sfp_tool_whatweb",      # Web tech fingerprinting (active probe)
    "sfp_spider",            # Web crawling target sites
    "sfp_dnsbrute",          # DNS brute force
    "sfp_screenshot",        # Target screenshots
    "sfp_portscan_tcp",      # Direct TCP port scan
    "sfp_bingsharedip",      # Active reverse-IP probing via Bing
)


# Default module set when caller passes none. A small, fast subset of
# the allowlist that returns useful infrastructure intel without
# requiring API keys for the threat-feed modules.
DEFAULT_MODULES: tuple[str, ...] = (
    "sfp_dnsresolve",
    "sfp_whois",
    "sfp_crt",
    "sfp_certspotter",
    "sfp_archiveorg",
)


# ---------- target-type inference ----------

# SpiderFoot infers target type from the value, but its inference is
# imperfect. The MCP can pre-tag the type to be explicit; falls back
# to SpiderFoot's auto-detection when not specified. Common types:
#   - INTERNET_NAME (domains, hostnames)
#   - IP_ADDRESS (single IPv4/IPv6)
#   - NETBLOCK_OWNER (CIDR)
#   - EMAILADDR (email)
TARGET_TYPES: tuple[str, ...] = (
    "INTERNET_NAME",
    "IP_ADDRESS",
    "NETBLOCK_OWNER",
    "EMAILADDR",
    "PHONE_NUMBER",
    "USERNAME",
    "BITCOIN_ADDRESS",
    "HUMAN_NAME",
)


# ---------- inputs ----------


class PassiveScanInput(BaseModel):
    """Input for the `passive_scan` tool."""

    target: str = Field(
        ...,
        min_length=1,
        description="Target to scan. Domain (example.com), IP, CIDR, email, "
        "username, etc. SpiderFoot infers the type unless `target_type` "
        "is specified.",
    )
    name: str | None = Field(
        default=None,
        description="Human-readable scan name. Defaults to "
        "'archimedes-passive-<target>' if not specified. Used to find the "
        "scan in SpiderFoot's web UI.",
    )
    modules: list[str] | None = Field(
        default=None,
        description="SpiderFoot module names to enable. ALL modules MUST be "
        "on the passive allowlist enforced by this MCP. Defaults to "
        "DEFAULT_MODULES (DNS + WHOIS + CT + Wayback). Caller can pass a "
        "wider passive set if richer output is needed.",
    )
    target_type: str | None = Field(
        default=None,
        description="Explicit target type (INTERNET_NAME / IP_ADDRESS / "
        "NETBLOCK_OWNER / EMAILADDR / etc.). Default: SpiderFoot infers "
        "from the value.",
    )


# ---------- outputs ----------


class ScanEvent(BaseModel):
    """One event SpiderFoot emitted during the scan."""

    event_type: str = Field(
        ...,
        description="SpiderFoot event type (e.g., DOMAIN_NAME, IP_ADDRESS, "
        "AFFILIATE_DOMAIN, EMAILADDR, RAW_DNS_RECORDS, MALICIOUS_AFFILIATE). "
        "See SpiderFoot's docs for the full taxonomy.",
    )
    data: str = Field(..., description="The actual indicator / data value.")
    source_module: str = Field(
        ..., description="Module that produced this event (e.g., sfp_crt)."
    )
    source_event_type: str | None = Field(
        default=None,
        description="Upstream event type that triggered this module's run.",
    )
    timestamp: str | None = Field(
        default=None, description="When SpiderFoot recorded this event (ISO 8601)."
    )
    confidence: int | None = Field(
        default=None, description="SpiderFoot confidence score (0-100)."
    )


class PassiveScanOutput(BaseModel):
    """Result of a `passive_scan` invocation."""

    scan_id: str = Field(..., description="SpiderFoot scan ID — usable in the web UI.")
    name: str = Field(..., description="Scan name as recorded in SpiderFoot.")
    target: str
    target_type: str | None = None
    status: str = Field(
        ...,
        description="Final scan status (FINISHED / ABORTED / ERROR-FAILED / "
        "RUNNING-but-timed-out). RUNNING means the MCP gave up waiting; the "
        "scan continues in SpiderFoot.",
    )
    modules_used: list[str] = Field(
        default_factory=list,
        description="Final module list passed to SpiderFoot (after allowlist filter).",
    )
    duration_seconds: float | None = Field(
        default=None,
        description="Wall-clock seconds the MCP waited before returning.",
    )
    events: list[ScanEvent] = Field(
        default_factory=list,
        description="All scan events SpiderFoot emitted, normalized.",
    )
    distinct_domains: list[str] = Field(
        default_factory=list,
        description="Distinct hostnames/domains observed (DOMAIN_NAME + INTERNET_NAME).",
    )
    distinct_ips: list[str] = Field(
        default_factory=list,
        description="Distinct IPs observed (IP_ADDRESS + IPV6_ADDRESS).",
    )
    distinct_emails: list[str] = Field(default_factory=list)
    web_url: str | None = Field(
        default=None,
        description="URL to the scan's results in SpiderFoot's web UI.",
    )


class ListModulesOutput(BaseModel):
    """Result of the `list_modules` tool."""

    passive_allowlist: list[str] = Field(default_factory=list)
    default_modules: list[str] = Field(default_factory=list)
    prohibited_examples: list[str] = Field(
        default_factory=list,
        description="Sample of explicitly-prohibited modules. Not exhaustive.",
    )


class HealthOutput(BaseModel):
    """Result of the `health` tool — quick reachability + auth check."""

    reachable: bool
    authenticated: bool | None = Field(
        default=None,
        description="True if auth was configured and accepted; False if "
        "configured and rejected; None if no auth configured.",
    )
    spiderfoot_version: str | None = Field(
        default=None,
        description="SpiderFoot version reported by /ping or /scanlist. None "
        "when the daemon doesn't expose a version field on those endpoints.",
    )
    url: str
    message: str | None = None
