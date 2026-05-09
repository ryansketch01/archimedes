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


# Passive-only source allowlist. Sources here run only OSINT queries
# against third-party indexes (cert transparency, search engines,
# threat-intel feeds), not direct probes against the target. Sources
# OUTSIDE this list are refused by enumerate() with TheHarvesterPolicyError.
#
# Reviewed against theHarvester's source list as of 2026-05. Sources
# that require API keys are included here — theHarvester silently
# skips them if the operator hasn't configured api-keys.yaml, which
# is fine.
PASSIVE_SOURCE_ALLOWLIST: tuple[str, ...] = (
    "anubis",
    "baidu",
    "bing",
    "bingapi",
    "brave",
    "bufferoverun",
    "censys",
    "certspotter",
    "crtsh",
    "dnsdumpster",
    "duckduckgo",
    "github-code",
    "hackertarget",
    "hunterhow",
    "intelx",
    "otx",
    "projectdiscovery",
    "rapiddns",
    "securitytrails",
    "shodan",
    "sitedossier",
    "subdomainfinderc99",
    "threatminer",
    "tomba",
    "urlscan",
    "virustotal",
    "yahoo",
    "zoomeye",
)

# Default source set when caller passes none. Sticks to keyless
# sources so the MCP works on a fresh theHarvester install without
# api-keys.yaml configured.
DEFAULT_SOURCES: tuple[str, ...] = (
    "crtsh",
    "otx",
    "hackertarget",
    "rapiddns",
    "sitedossier",
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
