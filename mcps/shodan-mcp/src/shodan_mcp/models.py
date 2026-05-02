"""Pydantic models for Shodan MCP tool inputs and outputs.

Output shape philosophy: trim Shodan's verbose responses to the fields a
CTI analyst actually uses. Banner data is huge — we keep an excerpt and
the parsed metadata, not the full thing. Service data is per-port; we
flatten to a list[ServiceEntry] rather than the nested top-level + data[]
structure Shodan returns.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------- shared ----------


class ServiceEntry(BaseModel):
    """One port/service entry from a Shodan host record."""

    port: int
    transport: str | None = Field(default=None, description="tcp/udp.")
    product: str | None = Field(default=None, description="Detected service name (e.g. 'nginx').")
    version: str | None = None
    banner_excerpt: str | None = Field(
        default=None,
        description="First 200 chars of the raw banner data, if any.",
    )


# ---------- lookup_host ----------


class HostLookupInput(BaseModel):
    """Input for lookup_host."""

    ip: str = Field(..., description="IPv4 or IPv6 address.", min_length=3)


class HostLookupOutput(BaseModel):
    """Trimmed Shodan host record. Costs 1 query credit per call."""

    found: bool = Field(..., description="True if Shodan has data for this IP.")
    ip: str | None = None
    hostnames: list[str] = Field(default_factory=list)
    country: str | None = Field(default=None, description="Country name (e.g. 'United States').")
    country_code: str | None = None
    city: str | None = None
    org: str | None = Field(default=None, description="Organization (often the hosting provider).")
    isp: str | None = None
    asn: str | None = Field(default=None, description="AS number as Shodan formats it (e.g. 'AS15169').")
    last_update: str | None = Field(
        default=None,
        description="ISO datetime of Shodan's most recent data for this host.",
    )
    ports: list[int] = Field(default_factory=list)
    vulns: list[str] = Field(
        default_factory=list,
        description="CVE IDs Shodan associates with this host (when present).",
    )
    tags: list[str] = Field(default_factory=list)
    services: list[ServiceEntry] = Field(default_factory=list)
    shodan_link: str | None = Field(default=None, description="Public Shodan GUI link.")


# ---------- search_hosts ----------


class SearchHostsInput(BaseModel):
    """Input for search_hosts."""

    query: str = Field(..., description="Shodan query string (e.g. 'apache port:443 country:US').", min_length=1)
    page: int = Field(default=1, ge=1, le=100, description="Page number; 100 results/page.")
    facets: str | None = Field(
        default=None,
        description="Comma-separated facets to compute, e.g. 'country,org'. Optional.",
    )


class SearchHostsOutput(BaseModel):
    """Trimmed search result. Costs 1 query credit per page."""

    total: int = Field(..., description="Total matching hosts across all pages.")
    page: int
    matches: list[HostLookupOutput] = Field(
        default_factory=list,
        description="Host records on this page. Each is the same shape as lookup_host output.",
    )
    facets: dict[str, list[dict[str, Any]]] = Field(
        default_factory=dict,
        description="Facet counts if requested (Shodan returns a list of {value, count}).",
    )


# ---------- count_hosts ----------


class CountHostsInput(BaseModel):
    """Input for count_hosts. FREE — no query credits consumed."""

    query: str = Field(..., description="Shodan query string.", min_length=1)
    facets: str | None = None


class CountHostsOutput(BaseModel):
    """Count-only result. No host details. Free endpoint."""

    total: int
    facets: dict[str, list[dict[str, Any]]] = Field(default_factory=dict)


# ---------- lookup_internetdb ----------


class InternetDbLookupInput(BaseModel):
    """Input for lookup_internetdb. FREE — no API key, no credits."""

    ip: str = Field(..., description="IPv4 address.", min_length=3)


class InternetDbLookupOutput(BaseModel):
    """Free Shodan InternetDB record. Smaller surface than lookup_host."""

    found: bool
    ip: str | None = None
    hostnames: list[str] = Field(default_factory=list)
    ports: list[int] = Field(default_factory=list)
    cpes: list[str] = Field(
        default_factory=list,
        description="CPE 2.3 strings identifying detected software/services.",
    )
    vulns: list[str] = Field(default_factory=list, description="CVE IDs.")
    tags: list[str] = Field(default_factory=list)
