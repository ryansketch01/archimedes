"""VirusTotal v3 REST client.

Synchronous httpx wrapper. Read-only — exposes the four GET endpoints
Archimedes needs (file/url/domain/ip) and nothing else.

Trims VT's verbose responses into our flat output shapes (see models.py).
On 404, returns a "not found" record rather than raising — VT having no
data on an artifact is a legitimate analytic answer, not an error.
"""

from __future__ import annotations

import base64
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urljoin

import httpx

from virustotal.config import VTConfig
from virustotal.exceptions import (
    VTAuthError,
    VTConnectionError,
    VTRateLimitError,
    VTRequestError,
)
from virustotal.models import (
    AnalysisStats,
    DomainLookupOutput,
    FileLookupOutput,
    IpLookupOutput,
    UrlLookupOutput,
)

DEFAULT_TIMEOUT_SECONDS = 15.0
GUI_BASE = "https://www.virustotal.com/gui/"


def _unix_to_iso(ts: int | None) -> str | None:
    """Convert a VT unix timestamp (UTC) to ISO-8601 string."""
    if ts is None:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def _stats(raw: dict[str, Any] | None) -> AnalysisStats | None:
    """Build AnalysisStats from VT's last_analysis_stats dict."""
    if not raw:
        return None
    return AnalysisStats(
        malicious=raw.get("malicious", 0),
        suspicious=raw.get("suspicious", 0),
        harmless=raw.get("harmless", 0),
        undetected=raw.get("undetected", 0),
        timeout=raw.get("timeout", 0),
    )


def _malicious_engines(results: dict[str, Any] | None) -> list[str]:
    """Pull engine names that returned category=malicious from last_analysis_results."""
    if not results:
        return []
    return sorted(
        engine
        for engine, verdict in results.items()
        if isinstance(verdict, dict) and verdict.get("category") == "malicious"
    )


def _encode_url(url: str) -> str:
    """VT v3 wants base64-urlsafe-no-padding encoding for URL IDs."""
    return base64.urlsafe_b64encode(url.encode("utf-8")).decode("ascii").rstrip("=")


class VTClient:
    """Synchronous VirusTotal v3 client."""

    def __init__(self, config: VTConfig, timeout: float = DEFAULT_TIMEOUT_SECONDS) -> None:
        self._config = config
        self._base_url = str(config.vt_base_url).rstrip("/") + "/"
        self._client = httpx.Client(
            headers={"x-apikey": config.vt_api_key.get_secret_value()},
            timeout=timeout,
        )

    def __enter__(self) -> VTClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    # ---------- transport ----------

    def _get(self, path: str) -> dict[str, Any] | None:
        """GET <base>/<path>. Returns parsed JSON, or None on 404."""
        url = urljoin(self._base_url, path)
        try:
            resp = self._client.get(url)
        except httpx.ConnectError as e:
            raise VTConnectionError(f"Could not connect to VT at {self._base_url}: {e}") from e
        except httpx.TimeoutException as e:
            raise VTConnectionError(f"VT request timed out: {e}") from e

        if resp.status_code == 404:
            return None
        if resp.status_code in (401, 403):
            raise VTAuthError(f"VT rejected the API key ({resp.status_code})")
        if resp.status_code == 429:
            raise VTRateLimitError(
                "VT rate limit exceeded (free tier: 4/min, 500/day, 15.5K/month)"
            )
        if resp.status_code >= 500:
            raise VTConnectionError(f"VT server error {resp.status_code}: {resp.text[:200]}")
        if resp.status_code >= 400:
            raise VTRequestError(f"VT rejected request ({resp.status_code}): {resp.text[:200]}")

        return resp.json()

    # ---------- file ----------

    def lookup_file(self, file_hash: str) -> FileLookupOutput:
        clean = file_hash.strip().lower()
        data = self._get(f"files/{clean}")
        if data is None:
            return FileLookupOutput(found=False)

        attrs = data.get("data", {}).get("attributes", {})
        sha256 = attrs.get("sha256")
        return FileLookupOutput(
            found=True,
            sha256=sha256,
            sha1=attrs.get("sha1"),
            md5=attrs.get("md5"),
            meaningful_name=attrs.get("meaningful_name"),
            type_description=attrs.get("type_description"),
            size=attrs.get("size"),
            last_analysis_stats=_stats(attrs.get("last_analysis_stats")),
            reputation=attrs.get("reputation"),
            first_submission_date=_unix_to_iso(attrs.get("first_submission_date")),
            last_analysis_date=_unix_to_iso(attrs.get("last_analysis_date")),
            names=attrs.get("names", []) or [],
            tags=attrs.get("tags", []) or [],
            malicious_engines=_malicious_engines(attrs.get("last_analysis_results")),
            vt_link=f"{GUI_BASE}file/{sha256}" if sha256 else None,
        )

    # ---------- url ----------

    def lookup_url(self, url: str) -> UrlLookupOutput:
        encoded = _encode_url(url.strip())
        data = self._get(f"urls/{encoded}")
        if data is None:
            return UrlLookupOutput(found=False, url=url)

        attrs = data.get("data", {}).get("attributes", {})
        return UrlLookupOutput(
            found=True,
            url=attrs.get("url") or url,
            last_final_url=attrs.get("last_final_url"),
            last_analysis_stats=_stats(attrs.get("last_analysis_stats")),
            reputation=attrs.get("reputation"),
            first_submission_date=_unix_to_iso(attrs.get("first_submission_date")),
            last_analysis_date=_unix_to_iso(attrs.get("last_analysis_date")),
            categories=attrs.get("categories") or {},
            title=attrs.get("title"),
            malicious_engines=_malicious_engines(attrs.get("last_analysis_results")),
            vt_link=f"{GUI_BASE}url/{encoded}",
        )

    # ---------- domain ----------

    def lookup_domain(self, domain: str) -> DomainLookupOutput:
        clean = domain.strip().lower()
        data = self._get(f"domains/{clean}")
        if data is None:
            return DomainLookupOutput(found=False, domain=clean)

        attrs = data.get("data", {}).get("attributes", {})
        return DomainLookupOutput(
            found=True,
            domain=clean,
            last_analysis_stats=_stats(attrs.get("last_analysis_stats")),
            reputation=attrs.get("reputation"),
            creation_date=_unix_to_iso(attrs.get("creation_date")),
            last_update_date=_unix_to_iso(attrs.get("last_update_date")),
            last_analysis_date=_unix_to_iso(attrs.get("last_analysis_date")),
            registrar=attrs.get("registrar"),
            categories=attrs.get("categories") or {},
            popularity_ranks=attrs.get("popularity_ranks") or {},
            malicious_engines=_malicious_engines(attrs.get("last_analysis_results")),
            vt_link=f"{GUI_BASE}domain/{clean}",
        )

    # ---------- ip ----------

    def lookup_ip(self, ip: str) -> IpLookupOutput:
        clean = ip.strip()
        data = self._get(f"ip_addresses/{clean}")
        if data is None:
            return IpLookupOutput(found=False, ip=clean)

        attrs = data.get("data", {}).get("attributes", {})
        return IpLookupOutput(
            found=True,
            ip=clean,
            last_analysis_stats=_stats(attrs.get("last_analysis_stats")),
            reputation=attrs.get("reputation"),
            country=attrs.get("country"),
            asn=attrs.get("asn"),
            as_owner=attrs.get("as_owner"),
            network=attrs.get("network"),
            last_analysis_date=_unix_to_iso(attrs.get("last_analysis_date")),
            malicious_engines=_malicious_engines(attrs.get("last_analysis_results")),
            vt_link=f"{GUI_BASE}ip-address/{clean}",
        )
