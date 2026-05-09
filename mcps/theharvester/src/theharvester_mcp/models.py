"""Pydantic models for theHarvester MCP tool inputs and outputs.

Output shape is a flat enumeration result — hosts (subdomains with
optional resolved IPs), distinct ips, virtual hosts, ASNs. Email
enumeration is intentionally NOT exposed by this MCP per LEGAL-POLICY
PII handling rules; the operator can run `theHarvester -d <d> -b
hunter` directly outside the MCP if email enumeration is genuinely
needed for an authorized investigation.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


# ---------- shared ----------


class HostEntry(BaseModel):
    """One host (subdomain) result, optionally with its resolved IPs."""

    hostname: str
    ips: list[str] = Field(
        default_factory=list,
        description="Resolved IP addresses, when theHarvester observed any. "
        "Empty list when only the hostname was discovered (no resolution).",
    )


class AsnEntry(BaseModel):
    """One ASN result."""

    asn: str
    name: str | None = None


# ---------- enumerate ----------


# Passive-only source allowlist. Reviewed against theHarvester 4.10.1
# (verified live 2026-05-09). Case is PRESERVED as theHarvester
# expects — most sources are lowercase but `securityTrails` is
# camelCase, and the argparse choices are case-sensitive.
#
# Inclusion criteria:
#   - Passive (queries third-party OSINT, not direct probes against target)
#   - Returns infrastructure data (hosts, ips, vhosts, asns), NOT primarily PII
#
# PII-heavy sources EXCLUDED from this allowlist per LEGAL-POLICY:
#   dehashed, haveibeenpwned, hunter, leakix, leaklookup, rocketreach, tomba
# These return primarily breach data / email enumeration. Operator
# may invoke them outside this MCP for authorized investigations.
PASSIVE_SOURCE_ALLOWLIST: tuple[str, ...] = (
    "baidu",
    "bevigil",
    "bitbucket",
    "brave",
    "bufferoverun",
    "builtwith",
    "censys",
    "certspotter",
    "chaos",
    "commoncrawl",
    "criminalip",
    "crtsh",
    "dnsdumpster",
    "duckduckgo",
    "fofa",
    "fullhunt",
    "github-code",
    "gitlab",
    "hackertarget",
    "hudsonrock",
    "hunterhow",
    "intelx",
    "mojeek",
    "netlas",
    "onyphe",
    "otx",
    "pentesttools",
    "projectdiscovery",
    "rapiddns",
    "robtex",
    "securityscorecard",
    "securityTrails",  # case-sensitive — matches theHarvester's argparse choice
    "shodan",
    "subdomaincenter",
    "subdomainfinderc99",
    "thc",
    "threatcrowd",
    "urlscan",
    "venacus",
    "virustotal",
    "waybackarchive",
    "whoisxml",
    "windvane",
    "yahoo",
    "zoomeye",
)

# Lowercase -> canonical-case map for case-insensitive caller input
# normalization. Callers can pass "securitytrails" or "SecurityTrails"
# and we translate to the canonical "securityTrails" that theHarvester
# expects.
_ALLOWLIST_LOWERCASE_MAP: dict[str, str] = {
    s.lower(): s for s in PASSIVE_SOURCE_ALLOWLIST
}

# Default source set when caller passes none. Sticks to keyless
# sources so the MCP works on a fresh theHarvester install without
# api-keys.yaml configured. All verified to exist in 4.10.1.
DEFAULT_SOURCES: tuple[str, ...] = (
    "crtsh",
    "otx",
    "hackertarget",
    "rapiddns",
    "certspotter",
    "duckduckgo",
)


class EnumerateInput(BaseModel):
    """Input for `enumerate`."""

    domain: str = Field(
        ...,
        description="Target domain (e.g., 'example.com'). theHarvester "
        "queries third-party OSINT sources for this domain; it does NOT "
        "directly probe the target.",
        min_length=3,
    )
    sources: list[str] = Field(
        default_factory=lambda: list(DEFAULT_SOURCES),
        description="List of theHarvester source plugin names. Each must be "
        "in the passive-only allowlist enforced by this MCP. Defaults to a "
        "keyless set (crtsh, otx, hackertarget, rapiddns, sitedossier, "
        "duckduckgo).",
    )
    limit: int | None = Field(
        default=None,
        ge=1,
        le=10000,
        description="Max results per source. theHarvester's own default is 500; "
        "this MCP defaults to THEHARVESTER_DEFAULT_LIMIT (100) for snappier "
        "responses. Override per call if needed.",
    )


class EnumerateOutput(BaseModel):
    """Result of `enumerate`."""

    domain: str
    sources_queried: list[str] = Field(
        default_factory=list,
        description="Final source list passed to theHarvester (after allowlist filter).",
    )
    duration_seconds: float | None = Field(
        default=None,
        description="Wall-clock seconds the theHarvester subprocess ran.",
    )
    hosts: list[HostEntry] = Field(default_factory=list)
    distinct_ips: list[str] = Field(default_factory=list)
    vhosts: list[str] = Field(
        default_factory=list,
        description="Virtual hosts (HTTP Host header values) discovered.",
    )
    asns: list[AsnEntry] = Field(default_factory=list)
    raw_output_path: str | None = Field(
        default=None,
        description="Path to the JSON output file theHarvester wrote (under a temp "
        "dir). Caller can read it if more detail than this trimmed view is needed; "
        "the MCP cleans it up after the response unless THEHARVESTER_KEEP_OUTPUT=1.",
    )


# ---------- list_sources ----------


class ListSourcesOutput(BaseModel):
    """Result of `list_sources`."""

    passive_allowlist: list[str] = Field(
        default_factory=list,
        description="Sources this MCP will accept in `enumerate`.",
    )
    default_sources: list[str] = Field(
        default_factory=list,
        description="Sources used when caller passes no `sources` arg.",
    )
