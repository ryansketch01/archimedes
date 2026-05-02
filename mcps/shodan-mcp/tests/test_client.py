"""Tests for the Shodan client.

Covers:
  - Pure helpers: _normalize_last_update, _trim_banner, _service_from_data,
    _host_from_payload
  - Transport: 200/404/401/402/403/429/5xx + credit-vs-auth disambiguation
  - Auth pattern: ?key=<key> query string (not header)

httpx.MockTransport keeps these zero-network so we don't burn the dev
plan's 100 query credits.
"""

from __future__ import annotations

import httpx
import pytest
from pydantic import HttpUrl, SecretStr

from shodan_mcp.config import ShodanConfig
from shodan_mcp.exceptions import (
    ShodanAuthError,
    ShodanConnectionError,
    ShodanCreditError,
    ShodanRateLimitError,
    ShodanRequestError,
)
from shodan_mcp.shodan_client import (
    BANNER_EXCERPT_LEN,
    ShodanClient,
    _host_from_payload,
    _normalize_last_update,
    _service_from_data,
    _trim_banner,
)


# ---------- pure helpers ----------


def test_normalize_last_update_handles_none():
    assert _normalize_last_update(None) is None


def test_normalize_last_update_appends_utc():
    out = _normalize_last_update("2025-01-01T12:34:56.789012")
    assert out.endswith("+00:00")


def test_normalize_last_update_passes_through_unparseable():
    assert _normalize_last_update("not-a-date") == "not-a-date"


def test_trim_banner_handles_none_and_empty():
    assert _trim_banner(None) is None
    assert _trim_banner("") is None
    assert _trim_banner("   ") is None


def test_trim_banner_short_banner_unchanged():
    assert _trim_banner("HTTP/1.1 200 OK") == "HTTP/1.1 200 OK"


def test_trim_banner_long_banner_truncated():
    long = "X" * (BANNER_EXCERPT_LEN + 50)
    out = _trim_banner(long)
    assert out.endswith("...")
    assert len(out) == BANNER_EXCERPT_LEN + 3


def test_service_from_data_full_record():
    s = _service_from_data({
        "port": 443, "transport": "tcp", "product": "nginx",
        "version": "1.18", "data": "HTTP/1.1 200 OK\r\nServer: nginx",
    })
    assert s.port == 443
    assert s.transport == "tcp"
    assert s.product == "nginx"
    assert s.version == "1.18"
    assert s.banner_excerpt.startswith("HTTP/1.1")


def test_host_from_payload_minimal():
    out = _host_from_payload({"ip_str": "8.8.8.8"})
    assert out.found is True
    assert out.ip == "8.8.8.8"
    assert out.shodan_link == "https://www.shodan.io/host/8.8.8.8"
    assert out.ports == []
    assert out.vulns == []


def test_host_from_payload_full():
    out = _host_from_payload({
        "ip_str": "1.2.3.4",
        "hostnames": ["example.com"],
        "country_name": "United States",
        "country_code": "US",
        "city": "Mountain View",
        "org": "Test Org",
        "isp": "Test ISP",
        "asn": "AS15169",
        "last_update": "2025-06-15T10:30:00.000000",
        "ports": [80, 443],
        "vulns": ["CVE-2021-44228"],
        "tags": ["cloud"],
        "data": [
            {"port": 80, "transport": "tcp", "product": "nginx", "data": "HTTP banner..."},
            {"port": 443, "transport": "tcp", "product": "nginx", "data": "HTTPS banner..."},
        ],
    })
    assert out.country == "United States"
    assert out.country_code == "US"
    assert out.asn == "AS15169"
    assert out.last_update.endswith("+00:00")
    assert out.vulns == ["CVE-2021-44228"]
    assert len(out.services) == 2
    assert out.services[0].port == 80


# ---------- transport ----------


def _make_client(api_handler, internetdb_handler=None) -> ShodanClient:
    """Build a ShodanClient with mock transports for both base URLs."""
    cfg = ShodanConfig(
        SHODAN_API_KEY=SecretStr("test-key"),
        SHODAN_API_BASE_URL=HttpUrl("https://mock.api/"),
        SHODAN_INTERNETDB_BASE_URL=HttpUrl("https://mock.idb/"),
    )
    client = ShodanClient(cfg)
    client._api_client.close()
    client._internetdb_client.close()
    client._api_client = httpx.Client(transport=httpx.MockTransport(api_handler))
    if internetdb_handler is not None:
        client._internetdb_client = httpx.Client(transport=httpx.MockTransport(internetdb_handler))
    return client


def test_lookup_host_sends_key_as_query_param():
    seen = []

    def handler(request):
        seen.append(dict(request.url.params))
        return httpx.Response(200, json={"ip_str": "8.8.8.8"})

    client = _make_client(handler)
    client.lookup_host("8.8.8.8")
    assert seen[0]["key"] == "test-key"


def test_lookup_host_404_returns_not_found():
    def handler(request):
        return httpx.Response(404)

    client = _make_client(handler)
    out = client.lookup_host("1.1.1.1")
    assert out.found is False
    assert out.ip == "1.1.1.1"


def test_lookup_host_401_pure_auth():
    """401 without 'credit' or 'upgrade' in body is auth failure."""
    def handler(request):
        return httpx.Response(401, json={"error": "Invalid API key"})

    client = _make_client(handler)
    with pytest.raises(ShodanAuthError):
        client.lookup_host("1.1.1.1")


def test_lookup_host_401_credit_message_raises_credit_error():
    """401 with 'credit' in body should be ShodanCreditError, not auth."""
    def handler(request):
        return httpx.Response(
            401,
            json={"error": "You don't have enough query credits to perform this action"},
        )

    client = _make_client(handler)
    with pytest.raises(ShodanCreditError):
        client.lookup_host("1.1.1.1")


def test_lookup_host_402_raises_credit_error():
    def handler(request):
        return httpx.Response(402, text="Payment Required")

    client = _make_client(handler)
    with pytest.raises(ShodanCreditError):
        client.lookup_host("1.1.1.1")


def test_lookup_host_429_raises_rate_limit():
    def handler(request):
        return httpx.Response(429)

    client = _make_client(handler)
    with pytest.raises(ShodanRateLimitError):
        client.lookup_host("1.1.1.1")


def test_lookup_host_5xx_raises_connection_error():
    def handler(request):
        return httpx.Response(503)

    client = _make_client(handler)
    with pytest.raises(ShodanConnectionError):
        client.lookup_host("1.1.1.1")


def test_lookup_host_400_raises_request_error():
    def handler(request):
        return httpx.Response(400, json={"error": "bad query"})

    client = _make_client(handler)
    with pytest.raises(ShodanRequestError):
        client.lookup_host("1.1.1.1")


def test_search_hosts_sends_query_and_page():
    seen = []

    def handler(request):
        seen.append(dict(request.url.params))
        return httpx.Response(200, json={"total": 0, "matches": []})

    client = _make_client(handler)
    client.search_hosts("apache port:443", page=2, facets="country,org")
    assert seen[0]["query"] == "apache port:443"
    assert seen[0]["page"] == "2"
    assert seen[0]["facets"] == "country,org"
    assert seen[0]["key"] == "test-key"


def test_search_hosts_returns_total_and_matches():
    def handler(request):
        return httpx.Response(200, json={
            "total": 42,
            "matches": [{"ip_str": "1.1.1.1"}, {"ip_str": "2.2.2.2"}],
            "facets": {"country": [{"value": "US", "count": 30}]},
        })

    client = _make_client(handler)
    out = client.search_hosts("nginx")
    assert out.total == 42
    assert len(out.matches) == 2
    assert out.matches[0].ip == "1.1.1.1"
    assert out.facets["country"][0]["value"] == "US"


def test_count_hosts_sends_query_only():
    seen = []

    def handler(request):
        seen.append((str(request.url.path), dict(request.url.params)))
        return httpx.Response(200, json={"total": 12345})

    client = _make_client(handler)
    out = client.count_hosts("vuln:CVE-2021-44228")
    assert seen[0][0].endswith("/shodan/host/count")
    assert seen[0][1]["query"] == "vuln:CVE-2021-44228"
    assert out.total == 12345


def test_lookup_internetdb_no_auth_query():
    """InternetDB endpoint should not get a key= param."""
    seen = []

    def handler(request):
        seen.append(dict(request.url.params))
        assert request.url.path == "/8.8.8.8"
        return httpx.Response(200, json={
            "ip": "8.8.8.8",
            "ports": [53, 443],
            "hostnames": ["dns.google"],
            "cpes": [],
            "vulns": [],
            "tags": [],
        })

    client = _make_client(api_handler=lambda r: httpx.Response(500), internetdb_handler=handler)
    out = client.lookup_internetdb("8.8.8.8")
    assert out.found is True
    assert out.ports == [53, 443]
    assert "key" not in seen[0]  # no auth on InternetDB


def test_lookup_internetdb_404_returns_not_found():
    def handler(request):
        return httpx.Response(404)

    client = _make_client(
        api_handler=lambda r: httpx.Response(500),
        internetdb_handler=handler,
    )
    out = client.lookup_internetdb("9.9.9.9")
    assert out.found is False
    assert out.ip == "9.9.9.9"


def test_connect_error_translates():
    def handler(request):
        raise httpx.ConnectError("refused")

    client = _make_client(handler)
    with pytest.raises(ShodanConnectionError):
        client.lookup_host("1.1.1.1")
