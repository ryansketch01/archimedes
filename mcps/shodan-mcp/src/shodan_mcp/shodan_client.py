"""Shodan v1 + InternetDB client.

Synchronous httpx wrapper. Read-only: host lookup, search, count, and the
free InternetDB endpoint. No scan submission, no DNS, no alerts.

Two base URLs:
  - api.shodan.io (paid, query-string auth via ?key=)
  - internetdb.shodan.io (free, no auth)

Auth gotcha: Shodan uses ?key=<key> query string, not headers. Different
from VirusTotal (header) and Splunk (basic). The client merges the key
into every paid-API request's params.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any
from urllib.parse import urljoin

import httpx

from shodan_mcp.config import ShodanConfig
from shodan_mcp.exceptions import (
    ShodanAuthError,
    ShodanConnectionError,
    ShodanCreditError,
    ShodanRateLimitError,
    ShodanRequestError,
)
from shodan_mcp.models import (
    CountHostsOutput,
    HostLookupOutput,
    InternetDbLookupOutput,
    SearchHostsOutput,
    ServiceEntry,
)

DEFAULT_TIMEOUT_SECONDS = 30.0
GUI_BASE = "https://www.shodan.io/host/"
BANNER_EXCERPT_LEN = 200


def _normalize_last_update(value: str | None) -> str | None:
    """Shodan returns 'YYYY-MM-DDTHH:MM:SS.ffffff' without TZ. Treat as UTC."""
    if not value:
        return None
    try:
        # Shodan uses naive ISO; we treat as UTC and normalize.
        return datetime.fromisoformat(value).isoformat() + "+00:00"
    except ValueError:
        return value  # Pass through if parsing fails


def _trim_banner(data: str | None) -> str | None:
    if not data:
        return None
    s = data.strip()
    if not s:
        return None
    if len(s) <= BANNER_EXCERPT_LEN:
        return s
    return s[:BANNER_EXCERPT_LEN] + "..."


def _service_from_data(entry: dict[str, Any]) -> ServiceEntry:
    return ServiceEntry(
        port=entry.get("port"),
        transport=entry.get("transport"),
        product=entry.get("product"),
        version=entry.get("version"),
        banner_excerpt=_trim_banner(entry.get("data")),
    )


def _host_from_payload(payload: dict[str, Any]) -> HostLookupOutput:
    """Map Shodan's host JSON into our flat HostLookupOutput."""
    ip = payload.get("ip_str") or payload.get("ip")
    asn_raw = payload.get("asn")
    asn = str(asn_raw) if asn_raw is not None else None
    return HostLookupOutput(
        found=True,
        ip=ip,
        hostnames=payload.get("hostnames") or [],
        country=payload.get("country_name"),
        country_code=payload.get("country_code"),
        city=payload.get("city"),
        org=payload.get("org"),
        isp=payload.get("isp"),
        asn=asn,
        last_update=_normalize_last_update(payload.get("last_update")),
        ports=payload.get("ports") or [],
        vulns=list(payload.get("vulns") or []),
        tags=payload.get("tags") or [],
        services=[_service_from_data(d) for d in (payload.get("data") or []) if isinstance(d, dict)],
        shodan_link=f"{GUI_BASE}{ip}" if ip else None,
    )


class ShodanClient:
    """Synchronous Shodan client.

    Uses two httpx clients under the hood — one for the authenticated
    api.shodan.io endpoints and one for the unauthenticated internetdb
    subdomain. Both close on .close() / __exit__.
    """

    def __init__(self, config: ShodanConfig, timeout: float = DEFAULT_TIMEOUT_SECONDS) -> None:
        self._config = config
        self._api_base = str(config.shodan_api_base_url).rstrip("/") + "/"
        self._internetdb_base = str(config.shodan_internetdb_base_url).rstrip("/") + "/"
        self._api_key = config.shodan_api_key.get_secret_value()
        self._api_client = httpx.Client(timeout=timeout)
        self._internetdb_client = httpx.Client(timeout=timeout)

    def __enter__(self) -> ShodanClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._api_client.close()
        self._internetdb_client.close()

    # ---------- transport ----------

    def _api_get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """GET against api.shodan.io with auth. Returns None on 404."""
        url = urljoin(self._api_base, path)
        merged = {"key": self._api_key, **(params or {})}
        try:
            resp = self._api_client.get(url, params=merged)
        except httpx.ConnectError as e:
            raise ShodanConnectionError(f"Could not connect to {self._api_base}: {e}") from e
        except httpx.TimeoutException as e:
            raise ShodanConnectionError(f"Shodan request timed out: {e}") from e

        return self._handle_response(resp)

    def _internetdb_get(self, ip: str) -> dict[str, Any] | None:
        """GET against internetdb.shodan.io. No auth. Returns None on 404."""
        url = urljoin(self._internetdb_base, ip)
        try:
            resp = self._internetdb_client.get(url)
        except httpx.ConnectError as e:
            raise ShodanConnectionError(f"Could not connect to InternetDB: {e}") from e
        except httpx.TimeoutException as e:
            raise ShodanConnectionError(f"InternetDB request timed out: {e}") from e

        return self._handle_response(resp)

    def _handle_response(self, resp: httpx.Response) -> dict[str, Any] | None:
        """Translate HTTP status into either parsed JSON, None (404), or raise."""
        if resp.status_code == 404:
            return None
        if resp.status_code == 429:
            raise ShodanRateLimitError("Shodan rate limit exceeded (1 req/sec on most plans)")
        if resp.status_code in (401, 403):
            body = resp.text.lower()
            # Shodan signals "not enough credits" via a 401 with an error body
            # like {"error":"You don't have enough query credits..."}. Disambiguate.
            if "credit" in body or "upgrade" in body:
                raise ShodanCreditError(f"Shodan: out of credits ({resp.status_code}): {resp.text[:200]}")
            raise ShodanAuthError(f"Shodan rejected the API key ({resp.status_code})")
        if resp.status_code == 402:
            raise ShodanCreditError(f"Shodan: payment required (402): {resp.text[:200]}")
        if resp.status_code >= 500:
            raise ShodanConnectionError(f"Shodan server error {resp.status_code}: {resp.text[:200]}")
        if resp.status_code >= 400:
            raise ShodanRequestError(f"Shodan rejected request ({resp.status_code}): {resp.text[:200]}")

        if not resp.content:
            return None
        return resp.json()

    # ---------- lookup_host (1 query credit) ----------

    def lookup_host(self, ip: str) -> HostLookupOutput:
        clean = ip.strip()
        data = self._api_get(f"shodan/host/{clean}")
        if data is None:
            return HostLookupOutput(found=False, ip=clean)
        return _host_from_payload(data)

    # ---------- search_hosts (1 credit per page) ----------

    def search_hosts(self, query: str, page: int = 1, facets: str | None = None) -> SearchHostsOutput:
        params: dict[str, Any] = {"query": query, "page": page}
        if facets:
            params["facets"] = facets
        data = self._api_get("shodan/host/search", params=params)
        if data is None:
            return SearchHostsOutput(total=0, page=page)
        matches = [_host_from_payload(m) for m in (data.get("matches") or []) if isinstance(m, dict)]
        return SearchHostsOutput(
            total=data.get("total", 0),
            page=page,
            matches=matches,
            facets=data.get("facets") or {},
        )

    # ---------- count_hosts (FREE) ----------

    def count_hosts(self, query: str, facets: str | None = None) -> CountHostsOutput:
        params: dict[str, Any] = {"query": query}
        if facets:
            params["facets"] = facets
        data = self._api_get("shodan/host/count", params=params)
        if data is None:
            return CountHostsOutput(total=0)
        return CountHostsOutput(total=data.get("total", 0), facets=data.get("facets") or {})

    # ---------- lookup_internetdb (FREE, no key) ----------

    def lookup_internetdb(self, ip: str) -> InternetDbLookupOutput:
        clean = ip.strip()
        data = self._internetdb_get(clean)
        if data is None:
            return InternetDbLookupOutput(found=False, ip=clean)
        return InternetDbLookupOutput(
            found=True,
            ip=data.get("ip"),
            hostnames=data.get("hostnames") or [],
            ports=data.get("ports") or [],
            cpes=data.get("cpes") or [],
            vulns=data.get("vulns") or [],
            tags=data.get("tags") or [],
        )
