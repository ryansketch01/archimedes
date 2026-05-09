"""Pydantic models for Censys MCP tool inputs and outputs.

Output shape philosophy: trim Censys's verbose responses to what a
CTI analyst needs at first read. Censys returns deeply-nested host
records (services x banner x parsed x JARM x JA3 x DNS x ...), most
of which is dead weight for triage. Map to a flat ServiceEntry list
similar to mcps/shodan-mcp's HostLookupOutput, plus the location /
ASN / DNS surface needed for IOC enrichment.

For certificate search, surface SAN list + issuer + validity window
+ fingerprints. Drop the parsed cert blob (huge).
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------- shared ----------


class ServiceEntry(BaseModel):
    """One service/port entry from a Censys host record."""

    port: int
    transport_protocol: str | None = Field(
        default=None,
        description="TCP/UDP/QUIC.",
    )
    service_name: str | None = Field(
        default=None,
        description="Censys's service name (HTTP, SSH, MYSQL, etc.).",
    )
    extended_service_name: str | None = Field(
        default=None,
        description="More specific name when Censys identifies a sub-protocol.",
    )
    software: list[str] = Field(
        default_factory=list,
        description="Detected software products (e.g., 'Apache HTTP Server', "
        "'OpenSSH'). Each entry is the human name; CPEs are dropped.",
    )
    banner_excerpt: str | None = Field(
        default=None,
        description="First 200 chars of the banner if available.",
    )
    tls_ja3s: str | None = None
    tls_ja4s: str | None = None
    cert_fingerprint_sha256: str | None = Field(
        default=None,
        description="SHA-256 of the leaf certificate, if any.",
    )


class Location(BaseModel):
    country: str | None = None
    country_code: str | None = None
    province: str | None = None
    city: str | None = None
    postal_code: str | None = None
    timezone: str | None = None
    continent: str | None = None
    coordinates: dict[str, float] | None = Field(
        default=None,
        description="{'latitude': ..., 'longitude': ...} if available.",
    )


class AutonomousSystem(BaseModel):
    asn: int | None = None
    name: str | None = None
    description: str | None = None
    country_code: str | None = None
    bgp_prefix: str | None = None


# ---------- search_hosts ----------


class SearchHostsInput(BaseModel):
    """Input for `search_hosts`."""

    query: str = Field(
        ...,
        description="Censys search syntax. Examples: "
        "'services.service_name: HTTP and location.country: \"United States\"', "
        "'autonomous_system.asn: 13335', "
        "'services.tls.certificates.leaf_data.subject.common_name: example.com'.",
        min_length=1,
    )
    per_page: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Results per page (1-100). Censys paginates with cursors; "
        "this MCP returns first page only — for deeper pagination, request "
        "a higher per_page or pass a cursor explicitly.",
    )
    cursor: str | None = Field(
        default=None,
        description="Pagination cursor from a prior response's `next_cursor`. "
        "Null for first page.",
    )


class HostHit(BaseModel):
    """One host hit in a search response."""

    ip: str
    services: list[ServiceEntry] = Field(default_factory=list)
    location: Location | None = None
    autonomous_system: AutonomousSystem | None = None
    last_updated_at: str | None = None
    dns_names: list[str] = Field(default_factory=list)
    operating_system: str | None = None


class SearchHostsOutput(BaseModel):
    """Result of `search_hosts`."""

    total: int = Field(..., description="Total hosts matching the query (may be capped at 10k by Censys).")
    returned: int = Field(..., description="Count returned in this page.")
    next_cursor: str | None = Field(
        default=None,
        description="Pass to subsequent calls for pagination. Null if no more pages.",
    )
    hits: list[HostHit] = Field(default_factory=list)


# ---------- lookup_host ----------


class LookupHostInput(BaseModel):
    """Input for `lookup_host`."""

    ip: str = Field(..., description="IPv4 or IPv6 address.", min_length=3)


class LookupHostOutput(BaseModel):
    """Trimmed Censys host record. Costs 1 view request on the free tier."""

    found: bool = Field(..., description="True if Censys has data for this IP.")
    ip: str | None = None
    services: list[ServiceEntry] = Field(default_factory=list)
    location: Location | None = None
    autonomous_system: AutonomousSystem | None = None
    last_updated_at: str | None = None
    dns_names: list[str] = Field(default_factory=list)
    operating_system: str | None = None
    censys_url: str | None = Field(
        default=None,
        description="Direct URL to the Censys host detail page.",
    )


# ---------- search_certificates ----------


class SearchCertificatesInput(BaseModel):
    """Input for `search_certificates`."""

    query: str = Field(
        ...,
        description="Censys cert search syntax. Examples: "
        "'parsed.subject.common_name: example.com', "
        "'parsed.issuer.organization: \"Let\\'s Encrypt\"', "
        "'parsed.validity.start: [2026-01-01 to 2026-05-01]'.",
        min_length=1,
    )
    per_page: int = Field(
        default=10,
        ge=1,
        le=100,
    )
    cursor: str | None = None


class CertificateHit(BaseModel):
    """One certificate hit. Trimmed to identification fields + validity."""

    fingerprint_sha256: str
    fingerprint_sha1: str | None = None
    subject_dn: str | None = None
    subject_cn: str | None = None
    issuer_dn: str | None = None
    issuer_cn: str | None = None
    issuer_organization: str | None = None
    sans: list[str] = Field(
        default_factory=list,
        description="Subject Alternative Names (DNS names + IP-SANs combined).",
    )
    validity_start: str | None = None
    validity_end: str | None = None
    self_signed: bool | None = None
    key_algorithm: str | None = None
    signature_algorithm: str | None = None
    censys_url: str | None = None


class SearchCertificatesOutput(BaseModel):
    """Result of `search_certificates`."""

    total: int
    returned: int
    next_cursor: str | None = None
    hits: list[CertificateHit] = Field(default_factory=list)
