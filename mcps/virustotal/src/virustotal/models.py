"""Pydantic models for VirusTotal MCP tool inputs and outputs.

Output shape philosophy: trim VT's verbose response to the fields a CTI
analyst actually needs. Skip the per-engine breakdown (70+ entries) by
default; surface a list of just the engines that flagged the artifact.

All four lookup tools (file/url/domain/ip) share an `AnalysisStats`
sub-model so downstream consumers can write generic display logic.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------- shared ----------


class AnalysisStats(BaseModel):
    """VT's last_analysis_stats block."""

    malicious: int = 0
    suspicious: int = 0
    harmless: int = 0
    undetected: int = 0
    timeout: int = 0


# ---------- file lookup ----------


class FileLookupInput(BaseModel):
    """Input for the lookup_file tool."""

    file_hash: str = Field(
        ...,
        description="MD5 (32 hex), SHA1 (40 hex), or SHA256 (64 hex) of the file.",
        min_length=32,
        max_length=64,
    )


class FileLookupOutput(BaseModel):
    """Trimmed file report from VT."""

    found: bool = Field(..., description="True if VT had data for this hash.")
    sha256: str | None = None
    sha1: str | None = None
    md5: str | None = None
    meaningful_name: str | None = Field(
        default=None, description="VT's canonical filename (often the most-submitted name)."
    )
    type_description: str | None = Field(
        default=None, description="File type, e.g. 'Win32 EXE', 'PowerShell'."
    )
    size: int | None = Field(default=None, description="File size in bytes.")
    last_analysis_stats: AnalysisStats | None = None
    reputation: int | None = Field(
        default=None, description="VT community reputation score (-100 to +100)."
    )
    first_submission_date: str | None = Field(
        default=None, description="ISO-8601 UTC, derived from VT's unix timestamp."
    )
    last_analysis_date: str | None = Field(
        default=None, description="ISO-8601 UTC, derived from VT's unix timestamp."
    )
    names: list[str] = Field(default_factory=list, description="Known filenames.")
    tags: list[str] = Field(default_factory=list, description="VT tags.")
    malicious_engines: list[str] = Field(
        default_factory=list,
        description="Engine names that flagged this file as malicious.",
    )
    vt_link: str | None = Field(
        default=None, description="Public VT GUI link for this artifact."
    )


# ---------- url lookup ----------


class UrlLookupInput(BaseModel):
    """Input for the lookup_url tool."""

    url: str = Field(..., description="Full URL including scheme.", min_length=4)


class UrlLookupOutput(BaseModel):
    """Trimmed URL report from VT."""

    found: bool
    url: str | None = None
    last_final_url: str | None = Field(
        default=None, description="URL after redirects, if VT followed any."
    )
    last_analysis_stats: AnalysisStats | None = None
    reputation: int | None = None
    first_submission_date: str | None = None
    last_analysis_date: str | None = None
    categories: dict[str, str] = Field(
        default_factory=dict,
        description="Vendor → category mapping (e.g. 'Forcepoint ThreatSeeker' → 'phishing').",
    )
    title: str | None = None
    malicious_engines: list[str] = Field(default_factory=list)
    vt_link: str | None = None


# ---------- domain lookup ----------


class DomainLookupInput(BaseModel):
    """Input for the lookup_domain tool."""

    domain: str = Field(..., description="Domain name (no scheme, no path).", min_length=3)


class DomainLookupOutput(BaseModel):
    """Trimmed domain report from VT."""

    found: bool
    domain: str | None = None
    last_analysis_stats: AnalysisStats | None = None
    reputation: int | None = None
    creation_date: str | None = None
    last_update_date: str | None = None
    last_analysis_date: str | None = None
    registrar: str | None = None
    categories: dict[str, str] = Field(default_factory=dict)
    popularity_ranks: dict[str, dict[str, Any]] = Field(
        default_factory=dict,
        description="Provider → {rank, timestamp} for sources like Cisco Umbrella, Majestic.",
    )
    malicious_engines: list[str] = Field(default_factory=list)
    vt_link: str | None = None


# ---------- ip lookup ----------


class IpLookupInput(BaseModel):
    """Input for the lookup_ip tool."""

    ip: str = Field(..., description="IPv4 (e.g. 8.8.8.8) or IPv6 address.", min_length=3)


class IpLookupOutput(BaseModel):
    """Trimmed IP report from VT."""

    found: bool
    ip: str | None = None
    last_analysis_stats: AnalysisStats | None = None
    reputation: int | None = None
    country: str | None = None
    asn: int | None = None
    as_owner: str | None = None
    network: str | None = None
    last_analysis_date: str | None = None
    malicious_engines: list[str] = Field(default_factory=list)
    vt_link: str | None = None
