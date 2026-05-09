"""Pydantic models for urlscan MCP tool inputs and outputs.

Output shape philosophy: trim urlscan's verbose responses to fields a
CTI analyst actually uses. Drop the kitchen sink (DOM, console, full
request/response bodies, screenshots base64'd in JSON) — they're huge
and the result API URL points at them when needed.

Each scan result is reduced to:
  - task: who/when/why
  - page: where the URL landed (post-redirects, IP, country, server)
  - stats: aggregate request/host counts
  - verdicts: urlscan's own + community verdicts
  - lists: ips/domains/asns/countries/servers (drops urls — too noisy)
  - screenshot_url: pointer; do not embed image data

Search responses surface a per-result subset of the above plus the
result API URL for follow-up via lookup_scan.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------- shared ----------


class ScanTask(BaseModel):
    """Submission/task metadata for a single scan."""

    uuid: str | None = None
    url: str | None = Field(default=None, description="The URL the scan was submitted for.")
    time: str | None = Field(
        default=None, description="ISO 8601 timestamp of when the scan was submitted."
    )
    source: str | None = Field(
        default=None,
        description="urlscan submission source (api / extension / web / etc.).",
    )
    visibility: str | None = Field(
        default=None,
        description="public / unlisted / private. Public scans are searchable; "
        "unlisted/private return only to the submitter.",
    )
    tags: list[str] = Field(default_factory=list)


class ScanPage(BaseModel):
    """Where the URL landed (post-redirects), as urlscan observed it."""

    url: str | None = Field(
        default=None,
        description="Final URL after following redirects (may differ from task.url).",
    )
    domain: str | None = None
    ip: str | None = Field(default=None, description="Server IP at scan time.")
    country: str | None = Field(default=None, description="ISO country code (e.g., 'US').")
    server: str | None = Field(default=None, description="Server header value.")
    title: str | None = Field(default=None, description="HTML <title> at scan time.")
    asn: str | None = None
    asnname: str | None = None
    tls_valid_days: int | None = Field(default=None, alias="tlsValidDays")
    tls_age_days: int | None = Field(default=None, alias="tlsAgeDays")

    model_config = {"populate_by_name": True}


class ScanStats(BaseModel):
    """Aggregate scan stats."""

    uniq_ips: int | None = Field(default=None, alias="uniqIPs")
    uniq_countries: int | None = Field(default=None, alias="uniqCountries")
    uniq_asns: int | None = Field(default=None, alias="uniqASNs")
    uniq_domains: int | None = Field(default=None, alias="uniqDomains")
    requests: int | None = None
    secure_requests: int | None = Field(default=None, alias="secureRequests")
    data_length: int | None = Field(default=None, alias="dataLength")

    model_config = {"populate_by_name": True}


class ScanVerdict(BaseModel):
    """A single verdict (overall or per-engine)."""

    score: int | None = None
    malicious: bool | None = None
    categories: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    brands: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Phish-brand identification from urlscan's classifier.",
    )


class ScanVerdicts(BaseModel):
    """Both the aggregate 'overall' verdict and urlscan's own classifier."""

    overall: ScanVerdict | None = None
    urlscan: ScanVerdict | None = None
    community: ScanVerdict | None = None
    engines: ScanVerdict | None = None


class ScanLists(BaseModel):
    """Indicator lists from the scan. URLs intentionally dropped —
    urlscan returns hundreds per scan and they bloat the response
    without much CTI value over the page.url + redirect chain."""

    ips: list[str] = Field(default_factory=list)
    domains: list[str] = Field(default_factory=list)
    asns: list[str] = Field(default_factory=list)
    countries: list[str] = Field(default_factory=list)
    servers: list[str] = Field(default_factory=list)
    hashes: list[str] = Field(
        default_factory=list,
        description="SHA-256 hashes of resources fetched during the scan.",
    )


# ---------- search ----------


class SearchInput(BaseModel):
    """Input for `search`."""

    query: str = Field(
        ...,
        description="urlscan search query. Examples: 'example.com', "
        "'domain:example.com', 'ip:1.2.3.4', 'page.country:RU AND task.source:api', "
        "'hash:<sha256>'. Free text without a field qualifier matches any URL.",
        min_length=1,
    )
    size: int = Field(
        default=10,
        ge=1,
        le=10000,
        description="Number of results to return (1-10000; default 10). "
        "urlscan paginates above ~10000 — use the `search_after` field "
        "from a result for deeper pagination if needed.",
    )


class SearchResultEntry(BaseModel):
    """One scan result from a search response."""

    uuid: str = Field(..., description="Scan UUID; pass to lookup_scan for full record.")
    task: ScanTask
    page: ScanPage
    stats: ScanStats | None = None
    verdicts: ScanVerdicts | None = Field(
        default=None,
        description="Search results carry a slimmed verdict set; "
        "lookup_scan returns the full verdicts object.",
    )
    result_url: str | None = Field(
        default=None,
        description="API URL to fetch the full scan result. Maps to lookup_scan(uuid).",
    )
    screenshot_url: str | None = Field(
        default=None,
        description="Direct screenshot URL (PNG). Do not embed; reference only.",
    )


class SearchOutput(BaseModel):
    """Result of `search`."""

    total: int = Field(..., description="Total scans matching the query (across all pages).")
    returned: int = Field(..., description="Count returned in this response.")
    has_more: bool = Field(default=False, description="True if more results available beyond `size`.")
    took_ms: int | None = Field(default=None, description="Server-reported query time in ms.")
    results: list[SearchResultEntry] = Field(default_factory=list)


# ---------- lookup_scan ----------


class LookupScanInput(BaseModel):
    """Input for `lookup_scan`."""

    uuid: str = Field(..., description="Scan UUID (from a search result or submit_scan).", min_length=8)


class LookupScanOutput(BaseModel):
    """Trimmed urlscan result record. Use the result_url for full detail."""

    found: bool = Field(..., description="True if urlscan has data for this UUID.")
    uuid: str | None = None
    task: ScanTask | None = None
    page: ScanPage | None = None
    stats: ScanStats | None = None
    verdicts: ScanVerdicts | None = None
    lists: ScanLists | None = None
    screenshot_url: str | None = None
    result_url: str | None = Field(
        default=None,
        description="Full result API URL on urlscan.io.",
    )
    web_url: str | None = Field(
        default=None,
        description="Human-friendly urlscan.io GUI URL for this scan.",
    )


# ---------- submit_scan ----------


class SubmitScanInput(BaseModel):
    """Input for `submit_scan`.

    Submitting a URL causes urlscan.io to visit it from their
    infrastructure. Per LEGAL-POLICY, this is acceptable for any URL —
    the operator is not the visitor. Hard Rule 4 (no scanning third
    parties) applies to active scanning the operator's infrastructure
    performs, not third-party scan services. The operator should
    still avoid submitting URLs that contain credentials or
    sensitive query params (urlscan archives them).
    """

    url: str = Field(..., description="URL to scan. Must include scheme (http:// or https://).", min_length=8)
    visibility: str = Field(
        default="public",
        description="public / unlisted / private. Default 'public' makes the scan "
        "searchable by other urlscan users — usually appropriate for CTI work. "
        "Use 'unlisted' or 'private' if the URL contains sensitive context.",
    )
    tags: list[str] = Field(
        default_factory=list,
        description="Optional tags applied to the scan (e.g., 'archimedes', 'ioc-hunt').",
    )
    referer: str | None = Field(
        default=None,
        description="Optional Referer header for the scan. Useful when the target "
        "expects a specific referer to render correctly.",
    )
    user_agent: str | None = Field(
        default=None,
        description="Optional User-Agent for the scan. Default urlscan UA otherwise.",
    )


class SubmitScanOutput(BaseModel):
    """Submission acknowledgement. Scan is async; poll lookup_scan(uuid)
    after ~15-30 seconds for the result."""

    uuid: str = Field(..., description="Scan UUID; use to poll lookup_scan or render the GUI URL.")
    api_url: str = Field(..., description="Result API URL (alias for lookup_scan input).")
    web_url: str = Field(..., description="Human-friendly urlscan.io GUI URL.")
    visibility: str
    message: str | None = Field(
        default=None,
        description="urlscan-side context message about the submission "
        "(rate limit warnings, etc.).",
    )
