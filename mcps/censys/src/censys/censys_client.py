"""Censys v2 REST client.

Synchronous httpx wrapper. Three operations:

  - search_hosts(query, per_page, cursor)        — Censys host search v2
  - lookup_host(ip)                              — Censys host view v2
  - search_certificates(query, per_page, cursor) — Censys certificate search v2

Auth: HTTP Basic (API_ID:API_SECRET). Empirically verified 2026-05-09
that Censys v2 rejects Bearer/PAT auth with an explicit "You must
authenticate with a valid API ID and secret." error. PATs may work
for v3/GraphQL endpoints; v2 host/cert search needs Basic auth.
httpx fills the Basic header automatically via the `auth=` param;
we set it on the client level so every request carries it.

Endpoint shape (Censys v2):

  GET /api/v2/hosts/search?q=...&per_page=...
  GET /api/v2/hosts/<ip>
  GET /api/v2/certificates/search?q=...&per_page=...

The certificates API moved to v2 in 2024. v1 deprecated 2025-Q1.
"""

from __future__ import annotations

from typing import Any
from urllib.parse import urljoin

import httpx

from censys.config import CensysConfig
from censys.exceptions import (
    CensysAuthError,
    CensysConnectionError,
    CensysQuotaExhaustedError,
    CensysRateLimitError,
    CensysRequestError,
)
from censys.models import (
    AutonomousSystem,
    CertificateHit,
    HostHit,
    Location,
    LookupHostOutput,
    SearchCertificatesOutput,
    SearchHostsOutput,
    ServiceEntry,
)

DEFAULT_TIMEOUT_SECONDS = 20.0
WEB_HOST_BASE = "https://search.censys.io/hosts/"
WEB_CERT_BASE = "https://search.censys.io/certificates/"
BANNER_EXCERPT_LEN = 200


# ---------- helpers ----------


def _trim_banner(data: str | None) -> str | None:
    if not data:
        return None
    s = data.strip()
    if not s:
        return None
    if len(s) <= BANNER_EXCERPT_LEN:
        return s
    return s[:BANNER_EXCERPT_LEN] + "..."


def _service_from(raw: dict[str, Any]) -> ServiceEntry:
    """Map a Censys host service entry into our flat ServiceEntry."""
    software_list: list[str] = []
    for sw in raw.get("software") or []:
        if isinstance(sw, dict):
            name = sw.get("product") or sw.get("vendor")
            if name:
                software_list.append(name)

    cert_fp: str | None = None
    tls = raw.get("tls") or {}
    certs = tls.get("certificates") or {}
    leaf = certs.get("leaf_data") or {}
    cert_fp = leaf.get("fingerprint") or leaf.get("fingerprint_sha256")

    ja3s = tls.get("ja3s")
    ja4s = tls.get("ja4s")

    return ServiceEntry(
        port=raw.get("port", 0),
        transport_protocol=raw.get("transport_protocol"),
        service_name=raw.get("service_name"),
        extended_service_name=raw.get("extended_service_name"),
        software=software_list,
        banner_excerpt=_trim_banner(raw.get("banner")),
        tls_ja3s=ja3s,
        tls_ja4s=ja4s,
        cert_fingerprint_sha256=cert_fp,
    )


def _location_from(raw: dict[str, Any] | None) -> Location | None:
    if not isinstance(raw, dict):
        return None
    coords = None
    raw_coords = raw.get("coordinates")
    if isinstance(raw_coords, dict) and "latitude" in raw_coords and "longitude" in raw_coords:
        try:
            coords = {
                "latitude": float(raw_coords["latitude"]),
                "longitude": float(raw_coords["longitude"]),
            }
        except (TypeError, ValueError):
            coords = None
    return Location(
        country=raw.get("country"),
        country_code=raw.get("country_code"),
        province=raw.get("province"),
        city=raw.get("city"),
        postal_code=raw.get("postal_code"),
        timezone=raw.get("timezone"),
        continent=raw.get("continent"),
        coordinates=coords,
    )


def _asn_from(raw: dict[str, Any] | None) -> AutonomousSystem | None:
    if not isinstance(raw, dict):
        return None
    return AutonomousSystem(
        asn=raw.get("asn"),
        name=raw.get("name"),
        description=raw.get("description"),
        country_code=raw.get("country_code"),
        bgp_prefix=raw.get("bgp_prefix"),
    )


def _host_from(raw: dict[str, Any]) -> HostHit:
    services = [
        _service_from(s)
        for s in (raw.get("services") or [])
        if isinstance(s, dict)
    ]
    dns_names: list[str] = []
    dns = raw.get("dns") or {}
    if isinstance(dns, dict):
        # Censys's host doc puts DNS names under various sub-keys
        for entry in dns.get("names") or []:
            if isinstance(entry, str):
                dns_names.append(entry)
            elif isinstance(entry, dict) and entry.get("name"):
                dns_names.append(entry["name"])
        rev = dns.get("reverse_dns")
        if isinstance(rev, dict) and rev.get("names"):
            for n in rev["names"]:
                if n and n not in dns_names:
                    dns_names.append(n)

    os_field = raw.get("operating_system")
    os_str: str | None = None
    if isinstance(os_field, dict):
        os_str = os_field.get("product") or os_field.get("vendor") or os_field.get("uniform_resource_identifier")
    elif isinstance(os_field, str):
        os_str = os_field

    return HostHit(
        ip=raw.get("ip", ""),
        services=services,
        location=_location_from(raw.get("location")),
        autonomous_system=_asn_from(raw.get("autonomous_system")),
        last_updated_at=raw.get("last_updated_at"),
        dns_names=dns_names,
        operating_system=os_str,
    )


def _cert_from(raw: dict[str, Any]) -> CertificateHit | None:
    """Map a Censys certificate hit into our flat CertificateHit.

    Censys's certificate documents have evolved across schema versions;
    this maps the v2 shape with defensive fallbacks for older fields.
    """
    fp = raw.get("fingerprint_sha256")
    if not fp:
        # Try nested location used by some search responses
        parsed = raw.get("parsed") or {}
        fps = parsed.get("fingerprints") or {}
        fp = fps.get("sha_256") or fps.get("sha256")
    if not fp:
        return None  # without a fingerprint we can't track the cert

    parsed = raw.get("parsed") or {}
    subject = parsed.get("subject") or {}
    issuer = parsed.get("issuer") or {}
    validity = parsed.get("validity_period") or parsed.get("validity") or {}
    extensions = parsed.get("extensions") or {}
    san = extensions.get("subject_alt_name") or {}

    sans: list[str] = []
    for k in ("dns_names", "ip_addresses", "uniform_resource_identifiers"):
        for v in san.get(k) or []:
            if isinstance(v, str):
                sans.append(v)

    issuer_org_list = issuer.get("organization") or []
    issuer_org = issuer_org_list[0] if issuer_org_list else None

    sub_cn_list = subject.get("common_name") or []
    sub_cn = sub_cn_list[0] if sub_cn_list else None

    iss_cn_list = issuer.get("common_name") or []
    iss_cn = iss_cn_list[0] if iss_cn_list else None

    return CertificateHit(
        fingerprint_sha256=fp,
        fingerprint_sha1=parsed.get("fingerprints", {}).get("sha_1") if isinstance(parsed.get("fingerprints"), dict) else None,
        subject_dn=parsed.get("subject_dn"),
        subject_cn=sub_cn,
        issuer_dn=parsed.get("issuer_dn"),
        issuer_cn=iss_cn,
        issuer_organization=issuer_org,
        sans=sans,
        validity_start=validity.get("not_before") or validity.get("start"),
        validity_end=validity.get("not_after") or validity.get("end"),
        self_signed=parsed.get("signature", {}).get("self_signed") if isinstance(parsed.get("signature"), dict) else None,
        key_algorithm=(parsed.get("subject_key_info") or {}).get("key_algorithm", {}).get("name")
        if isinstance(parsed.get("subject_key_info"), dict)
        else None,
        signature_algorithm=(parsed.get("signature") or {}).get("signature_algorithm", {}).get("name")
        if isinstance(parsed.get("signature"), dict)
        else None,
        censys_url=f"{WEB_CERT_BASE}{fp}",
    )


# ---------- client ----------


class CensysClient:
    """Synchronous Censys v2 client."""

    def __init__(self, config: CensysConfig, timeout: float = DEFAULT_TIMEOUT_SECONDS) -> None:
        self._config = config
        self._base_url = str(config.censys_api_base_url).rstrip("/") + "/"
        api_id = config.censys_api_id.get_secret_value()
        api_secret = config.censys_api_secret.get_secret_value()
        self._client = httpx.Client(
            timeout=timeout,
            auth=httpx.BasicAuth(api_id, api_secret),
            headers={
                "Accept": "application/json",
                "User-Agent": "ArchimedesCensys/0.1",
            },
        )

    def __enter__(self) -> CensysClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    # ---------- transport ----------

    def _get(
        self, path: str, params: dict[str, Any] | None = None
    ) -> tuple[int, dict[str, Any] | None]:
        """GET against Censys. Returns (status, body). 404 => (404, None)."""
        url = urljoin(self._base_url, path)
        try:
            resp = self._client.get(url, params=params)
        except httpx.ConnectError as e:
            raise CensysConnectionError(f"Could not connect to {self._base_url}: {e}") from e
        except httpx.TimeoutException as e:
            raise CensysConnectionError(f"Censys request timed out: {e}") from e
        except httpx.RequestError as e:
            raise CensysConnectionError(f"Censys request failed: {e}") from e

        return self._handle_response(resp)

    def _handle_response(self, resp: httpx.Response) -> tuple[int, dict[str, Any] | None]:
        if resp.status_code == 404:
            return (404, None)
        if resp.status_code == 429:
            text = resp.text.lower()
            if "quota" in text or "monthly" in text or "exhaust" in text:
                raise CensysQuotaExhaustedError(
                    f"Censys monthly quota exhausted: {resp.text[:200]}"
                )
            retry_after = resp.headers.get("Retry-After")
            raise CensysRateLimitError(
                f"Censys rate-limited (Retry-After: {retry_after}): {resp.text[:200]}"
            )
        if resp.status_code in (401, 403):
            raise CensysAuthError(
                f"Censys rejected the API credentials ({resp.status_code}): {resp.text[:200]}"
            )
        if resp.status_code == 402:
            raise CensysQuotaExhaustedError(
                f"Censys: payment required (402): {resp.text[:200]}"
            )
        if resp.status_code >= 500:
            raise CensysConnectionError(
                f"Censys server error {resp.status_code}: {resp.text[:200]}"
            )
        if resp.status_code >= 400:
            raise CensysRequestError(
                f"Censys rejected request ({resp.status_code}): {resp.text[:200]}"
            )

        if not resp.content:
            return (resp.status_code, None)
        try:
            return (resp.status_code, resp.json())
        except ValueError:
            raise CensysRequestError(
                f"Censys returned non-JSON (status {resp.status_code}): {resp.text[:200]}"
            )

    # ---------- search_hosts ----------

    def search_hosts(
        self, query: str, per_page: int = 10, cursor: str | None = None
    ) -> SearchHostsOutput:
        params: dict[str, Any] = {"q": query, "per_page": per_page}
        if cursor:
            params["cursor"] = cursor
        status, body = self._get("v2/hosts/search", params=params)
        if body is None:
            return SearchHostsOutput(total=0, returned=0)

        result = body.get("result") or {}
        hits_raw = result.get("hits") or []
        hits = [_host_from(h) for h in hits_raw if isinstance(h, dict)]

        # Censys reports 'total' under result.total or links.next presence
        total = result.get("total")
        if total is None:
            total = len(hits)

        next_cursor = (result.get("links") or {}).get("next")

        return SearchHostsOutput(
            total=int(total),
            returned=len(hits),
            next_cursor=next_cursor or None,
            hits=hits,
        )

    # ---------- lookup_host ----------

    def lookup_host(self, ip: str) -> LookupHostOutput:
        clean = ip.strip()
        status, body = self._get(f"v2/hosts/{clean}")
        if body is None:
            return LookupHostOutput(found=False, ip=clean)

        result = body.get("result") or {}
        host = _host_from(result)
        return LookupHostOutput(
            found=True,
            ip=host.ip or clean,
            services=host.services,
            location=host.location,
            autonomous_system=host.autonomous_system,
            last_updated_at=host.last_updated_at,
            dns_names=host.dns_names,
            operating_system=host.operating_system,
            censys_url=f"{WEB_HOST_BASE}{clean}",
        )

    # ---------- search_certificates ----------

    def search_certificates(
        self, query: str, per_page: int = 10, cursor: str | None = None
    ) -> SearchCertificatesOutput:
        params: dict[str, Any] = {"q": query, "per_page": per_page}
        if cursor:
            params["cursor"] = cursor
        status, body = self._get("v2/certificates/search", params=params)
        if body is None:
            return SearchCertificatesOutput(total=0, returned=0)

        result = body.get("result") or {}
        hits_raw = result.get("hits") or []
        hits: list[CertificateHit] = []
        for h in hits_raw:
            if not isinstance(h, dict):
                continue
            mapped = _cert_from(h)
            if mapped is not None:
                hits.append(mapped)

        total = result.get("total")
        if total is None:
            total = len(hits)
        next_cursor = (result.get("links") or {}).get("next")

        return SearchCertificatesOutput(
            total=int(total),
            returned=len(hits),
            next_cursor=next_cursor or None,
            hits=hits,
        )
