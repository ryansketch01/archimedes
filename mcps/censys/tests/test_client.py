"""Unit tests for the Censys client.

Uses respx to mock httpx without hitting the network. Covers:
  - search_hosts maps hits + pagination cursor
  - lookup_host maps the host record + 404 -> found=false
  - search_certificates maps hits with SAN list
  - 401/403/429/quota/5xx error mapping
  - Basic auth header is sent (httpx fills this from auth=)
"""

from __future__ import annotations

import httpx
import pytest
import respx

from censys.config import CensysConfig
from censys.exceptions import (
    CensysAuthError,
    CensysConnectionError,
    CensysQuotaExhaustedError,
    CensysRateLimitError,
    CensysRequestError,
)
from censys.censys_client import CensysClient


@pytest.fixture
def client() -> CensysClient:
    cfg = CensysConfig(
        CENSYS_API_ID="test-id",
        CENSYS_API_SECRET="test-secret",
        CENSYS_API_BASE_URL="https://search.censys.io/api/",
    )  # type: ignore[call-arg]
    c = CensysClient(cfg)
    yield c
    c.close()


SAMPLE_HOSTS_SEARCH = {
    "result": {
        "total": 2,
        "hits": [
            {
                "ip": "1.2.3.4",
                "services": [
                    {
                        "port": 443,
                        "transport_protocol": "TCP",
                        "service_name": "HTTP",
                        "extended_service_name": "HTTPS",
                        "software": [
                            {"product": "nginx", "vendor": "F5", "version": "1.27.0"}
                        ],
                        "banner": "HTTP/1.1 200 OK\r\nServer: nginx/1.27.0",
                        "tls": {
                            "ja3s": "abc123",
                            "ja4s": "def456",
                            "certificates": {
                                "leaf_data": {
                                    "fingerprint": "feedface" * 4,
                                }
                            },
                        },
                    }
                ],
                "location": {
                    "country": "United States",
                    "country_code": "US",
                    "city": "San Francisco",
                    "coordinates": {"latitude": 37.77, "longitude": -122.42},
                },
                "autonomous_system": {
                    "asn": 13335,
                    "name": "CLOUDFLARENET",
                    "country_code": "US",
                },
                "last_updated_at": "2026-05-09T12:00:00Z",
                "dns": {"names": [{"name": "host.example.com"}]},
                "operating_system": {"product": "Linux", "vendor": "Unknown"},
            },
            {
                "ip": "5.6.7.8",
                "services": [{"port": 22, "service_name": "SSH"}],
            },
        ],
        "links": {"next": "cursor-page-2"},
    }
}

SAMPLE_HOST_VIEW = {
    "result": {
        "ip": "9.9.9.9",
        "services": [
            {"port": 53, "service_name": "DNS"},
            {"port": 853, "service_name": "DNS_OVER_TLS"},
        ],
        "location": {"country": "Switzerland", "country_code": "CH"},
        "autonomous_system": {"asn": 19281, "name": "QUAD9-AS-1"},
        "last_updated_at": "2026-05-09T11:30:00Z",
        "dns": {"reverse_dns": {"names": ["dns.quad9.net"]}},
    }
}

SAMPLE_CERT_SEARCH = {
    "result": {
        "total": 1,
        "hits": [
            {
                "fingerprint_sha256": "0011" * 16,
                "parsed": {
                    "fingerprints": {"sha_1": "aaaa" * 10, "sha_256": "0011" * 16},
                    "subject": {"common_name": ["example.com"]},
                    "issuer": {
                        "common_name": ["R3"],
                        "organization": ["Let's Encrypt"],
                    },
                    "subject_dn": "CN=example.com",
                    "issuer_dn": "CN=R3, O=Let's Encrypt, C=US",
                    "validity_period": {
                        "not_before": "2026-04-01T00:00:00Z",
                        "not_after": "2026-07-01T00:00:00Z",
                    },
                    "extensions": {
                        "subject_alt_name": {
                            "dns_names": ["example.com", "www.example.com"],
                        }
                    },
                    "signature": {
                        "self_signed": False,
                        "signature_algorithm": {"name": "SHA256WithRSAEncryption"},
                    },
                    "subject_key_info": {
                        "key_algorithm": {"name": "RSA"},
                    },
                },
            }
        ],
    }
}


# ---------- search_hosts ----------


@respx.mock
def test_search_hosts_returns_trimmed_hits(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/search").mock(
        return_value=httpx.Response(200, json=SAMPLE_HOSTS_SEARCH)
    )
    out = client.search_hosts("services.service_name: HTTP", per_page=10)
    assert out.total == 2
    assert out.returned == 2
    assert out.next_cursor == "cursor-page-2"

    h1 = out.hits[0]
    assert h1.ip == "1.2.3.4"
    assert len(h1.services) == 1
    s = h1.services[0]
    assert s.port == 443
    assert s.service_name == "HTTP"
    assert s.extended_service_name == "HTTPS"
    assert s.software == ["nginx"]  # mapped from product
    assert s.banner_excerpt and "Server: nginx/1.27.0" in s.banner_excerpt
    assert s.tls_ja3s == "abc123"
    assert s.tls_ja4s == "def456"
    assert s.cert_fingerprint_sha256 == "feedface" * 4

    assert h1.location.country == "United States"
    assert h1.location.coordinates["latitude"] == 37.77
    assert h1.autonomous_system.asn == 13335
    assert h1.dns_names == ["host.example.com"]
    assert h1.operating_system == "Linux"

    h2 = out.hits[1]
    assert h2.ip == "5.6.7.8"
    assert len(h2.services) == 1


# ---------- lookup_host ----------


@respx.mock
def test_lookup_host_maps_record(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/9.9.9.9").mock(
        return_value=httpx.Response(200, json=SAMPLE_HOST_VIEW)
    )
    out = client.lookup_host("9.9.9.9")
    assert out.found is True
    assert out.ip == "9.9.9.9"
    assert len(out.services) == 2
    assert out.services[1].service_name == "DNS_OVER_TLS"
    assert out.location.country_code == "CH"
    assert out.autonomous_system.asn == 19281
    assert "dns.quad9.net" in out.dns_names
    assert out.censys_url == "https://search.censys.io/hosts/9.9.9.9"


@respx.mock
def test_lookup_host_404_returns_not_found(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/192.0.2.99").mock(
        return_value=httpx.Response(404)
    )
    out = client.lookup_host("192.0.2.99")
    assert out.found is False
    assert out.ip == "192.0.2.99"
    assert out.services == []


# ---------- search_certificates ----------


@respx.mock
def test_search_certificates_maps_hits(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/certificates/search").mock(
        return_value=httpx.Response(200, json=SAMPLE_CERT_SEARCH)
    )
    out = client.search_certificates("parsed.subject.common_name: example.com")
    assert out.total == 1
    assert out.returned == 1
    c = out.hits[0]
    assert c.fingerprint_sha256 == "0011" * 16
    assert c.subject_cn == "example.com"
    assert c.issuer_cn == "R3"
    assert c.issuer_organization == "Let's Encrypt"
    assert "example.com" in c.sans
    assert "www.example.com" in c.sans
    assert c.validity_start == "2026-04-01T00:00:00Z"
    assert c.validity_end == "2026-07-01T00:00:00Z"
    assert c.self_signed is False
    assert c.key_algorithm == "RSA"
    assert c.signature_algorithm == "SHA256WithRSAEncryption"


@respx.mock
def test_search_certificates_skips_hits_without_fingerprint(client: CensysClient) -> None:
    bad = {"result": {"total": 1, "hits": [{"parsed": {}}]}}  # no fingerprint
    respx.get("https://search.censys.io/api/v2/certificates/search").mock(
        return_value=httpx.Response(200, json=bad)
    )
    out = client.search_certificates("anything")
    assert out.returned == 0
    assert out.hits == []


# ---------- error mapping ----------


@respx.mock
def test_401_raises_auth_error(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/search").mock(return_value=httpx.Response(401))
    with pytest.raises(CensysAuthError):
        client.search_hosts("anything")


@respx.mock
def test_403_raises_auth_error(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/search").mock(return_value=httpx.Response(403))
    with pytest.raises(CensysAuthError):
        client.search_hosts("anything")


@respx.mock
def test_429_with_quota_message_raises_quota_exhausted(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/search").mock(
        return_value=httpx.Response(429, text="Monthly quota exhausted")
    )
    with pytest.raises(CensysQuotaExhaustedError):
        client.search_hosts("anything")


@respx.mock
def test_429_without_quota_message_raises_rate_limit(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/search").mock(
        return_value=httpx.Response(429, text="too fast", headers={"Retry-After": "30"})
    )
    with pytest.raises(CensysRateLimitError, match="30"):
        client.search_hosts("anything")


@respx.mock
def test_500_raises_connection_error(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/search").mock(return_value=httpx.Response(503))
    with pytest.raises(CensysConnectionError):
        client.search_hosts("anything")


@respx.mock
def test_400_raises_request_error(client: CensysClient) -> None:
    respx.get("https://search.censys.io/api/v2/hosts/search").mock(
        return_value=httpx.Response(400, text="Invalid query")
    )
    with pytest.raises(CensysRequestError, match="Invalid query"):
        client.search_hosts("malformed")


@respx.mock
def test_basic_auth_header_sent(client: CensysClient) -> None:
    """Verify httpx sends the Basic auth header. Hits the route and
    inspects the captured request after the call."""
    route = respx.get("https://search.censys.io/api/v2/hosts/search").mock(
        return_value=httpx.Response(200, json={"result": {"total": 0, "hits": []}})
    )
    client.search_hosts("anything")
    assert route.calls.call_count == 1
    auth_header = route.calls.last.request.headers.get("authorization") or ""
    assert auth_header.lower().startswith("basic ")
