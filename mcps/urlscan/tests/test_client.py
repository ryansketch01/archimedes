"""Unit tests for the urlscan client.

Uses respx to mock httpx without hitting the network. Covers:
  - search returns trimmed results
  - lookup_scan returns trimmed result + lists; URL list intentionally dropped
  - lookup_scan 404 -> found=false (not raised)
  - submit_scan 200 -> SubmitScanOutput
  - 401/403/429/5xx error mapping
  - submit_scan 400 with denylist body -> UrlscanScanDeniedError
"""

from __future__ import annotations

import httpx
import pytest
import respx

from urlscan.config import UrlscanConfig
from urlscan.exceptions import (
    UrlscanAuthError,
    UrlscanConnectionError,
    UrlscanRateLimitError,
    UrlscanRequestError,
    UrlscanScanDeniedError,
)
from urlscan.urlscan_client import UrlscanClient


@pytest.fixture
def client() -> UrlscanClient:
    # Pass base URL explicitly so test_config's test_base_url_overridable
    # doesn't leak into client tests via os.environ. pydantic-settings
    # otherwise reads URLSCAN_API_BASE_URL from env if set, and that test
    # sets it via load_dotenv to http://mock.local without per-test cleanup.
    cfg = UrlscanConfig(
        URLSCAN_API_KEY="test-key",
        URLSCAN_API_BASE_URL="https://urlscan.io/api/v1/",
    )  # type: ignore[call-arg]
    c = UrlscanClient(cfg)
    yield c
    c.close()


SAMPLE_SEARCH = {
    "results": [
        {
            "_id": "uuid-1",
            "task": {
                "uuid": "uuid-1",
                "url": "https://example.test/login",
                "time": "2026-05-09T12:00:00.000Z",
                "source": "api",
                "visibility": "public",
                "tags": ["phish"],
            },
            "page": {
                "url": "https://example.test/login",
                "domain": "example.test",
                "ip": "203.0.113.5",
                "country": "US",
                "server": "nginx",
                "title": "Example Login",
                "asn": "AS65001",
                "asnname": "EXAMPLE-ASN",
            },
            "stats": {
                "uniqIPs": 4,
                "uniqCountries": 2,
                "requests": 17,
                "secureRequests": 17,
            },
            "verdicts": {
                "overall": {"score": 70, "malicious": True, "categories": ["phishing"]},
                "urlscan": {"score": 60, "malicious": True, "tags": ["phish"]},
            },
            "result": "https://urlscan.io/api/v1/result/uuid-1/",
            "screenshot": "https://urlscan.io/screenshots/uuid-1.png",
        }
    ],
    "total": 1,
    "took": 42,
    "has_more": False,
}


SAMPLE_RESULT = {
    "task": {
        "uuid": "uuid-1",
        "url": "https://example.test/login",
        "time": "2026-05-09T12:00:00.000Z",
        "source": "api",
        "visibility": "public",
        "tags": ["phish"],
    },
    "page": {
        "url": "https://example.test/login",
        "domain": "example.test",
        "ip": "203.0.113.5",
        "country": "US",
        "server": "nginx",
        "title": "Example Login",
    },
    "stats": {"uniqIPs": 4, "uniqCountries": 2, "requests": 17},
    "verdicts": {
        "overall": {"score": 70, "malicious": True, "categories": ["phishing"]},
        "urlscan": {"score": 60, "malicious": True},
        "community": {"score": 0, "malicious": False},
        "engines": {"score": 50, "malicious": True, "categories": ["malware"]},
    },
    "lists": {
        "ips": ["203.0.113.5", "203.0.113.10"],
        "domains": ["example.test", "cdn.example.test"],
        "asns": ["AS65001", "AS65002"],
        "countries": ["US", "DE"],
        "servers": ["nginx", "cloudflare"],
        "hashes": ["abc123", "def456"],
        "urls": ["https://example.test/login", "https://example.test/login.css"],  # should be dropped
    },
}


# ---------- search ----------


@respx.mock
def test_search_returns_trimmed_results(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/search/").mock(
        return_value=httpx.Response(200, json=SAMPLE_SEARCH)
    )

    out = client.search("domain:example.test", size=5)
    assert out.total == 1
    assert out.returned == 1
    assert out.has_more is False
    assert out.took_ms == 42

    e = out.results[0]
    assert e.uuid == "uuid-1"
    assert e.task.url == "https://example.test/login"
    assert e.task.tags == ["phish"]
    assert e.page.domain == "example.test"
    assert e.page.country == "US"
    assert e.verdicts.overall.malicious is True
    assert e.verdicts.urlscan.score == 60
    assert e.result_url == "https://urlscan.io/api/v1/result/uuid-1/"
    assert e.screenshot_url == "https://urlscan.io/screenshots/uuid-1.png"


@respx.mock
def test_search_empty_results(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/search/").mock(
        return_value=httpx.Response(200, json={"results": [], "total": 0, "took": 5, "has_more": False})
    )
    out = client.search("nonexistent")
    assert out.total == 0
    assert out.returned == 0
    assert out.results == []


# ---------- lookup_scan ----------


@respx.mock
def test_lookup_scan_returns_trimmed_full_record(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/result/uuid-1/").mock(
        return_value=httpx.Response(200, json=SAMPLE_RESULT)
    )
    out = client.lookup_scan("uuid-1")
    assert out.found is True
    assert out.uuid == "uuid-1"
    assert out.task.uuid == "uuid-1"
    assert out.page.country == "US"
    assert out.stats.uniq_ips == 4
    assert out.verdicts.overall.malicious is True
    assert out.verdicts.community.malicious is False
    assert out.verdicts.engines.score == 50

    # Lists trimmed correctly — ips/domains/etc kept, urls dropped
    assert "203.0.113.5" in out.lists.ips
    assert "example.test" in out.lists.domains
    assert "AS65001" in out.lists.asns
    assert out.lists.hashes == ["abc123", "def456"]
    # ScanLists model has no `urls` field; verify it's not silently set
    assert not hasattr(out.lists, "urls")

    assert out.web_url == "https://urlscan.io/result/uuid-1/"
    assert out.result_url.endswith("/result/uuid-1/")


@respx.mock
def test_lookup_scan_404_returns_not_found(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/result/missing/").mock(
        return_value=httpx.Response(404, json={"message": "Scan not found"})
    )
    out = client.lookup_scan("missing")
    assert out.found is False
    assert out.uuid == "missing"
    assert out.task is None


# ---------- submit_scan ----------


@respx.mock
def test_submit_scan_returns_uuid(client: UrlscanClient) -> None:
    respx.post("https://urlscan.io/api/v1/scan/").mock(
        return_value=httpx.Response(
            200,
            json={
                "uuid": "new-uuid-7",
                "api": "https://urlscan.io/api/v1/result/new-uuid-7/",
                "result": "https://urlscan.io/result/new-uuid-7/",
                "visibility": "public",
                "message": "Submission successful",
            },
        )
    )
    out = client.submit_scan("https://target.test/", visibility="public", tags=["test"])
    assert out.uuid == "new-uuid-7"
    assert out.api_url == "https://urlscan.io/api/v1/result/new-uuid-7/"
    assert out.web_url == "https://urlscan.io/result/new-uuid-7/"
    assert out.visibility == "public"
    assert out.message == "Submission successful"


@respx.mock
def test_submit_scan_denylist_raises(client: UrlscanClient) -> None:
    respx.post("https://urlscan.io/api/v1/scan/").mock(
        return_value=httpx.Response(
            400,
            json={"message": "Submission denied (denylist)"},
            text='{"message": "Submission denied (denylist)"}',
        )
    )
    with pytest.raises(UrlscanScanDeniedError):
        client.submit_scan("https://blocked.test/")


# ---------- error mapping ----------


@respx.mock
def test_401_raises_auth_error(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/search/").mock(return_value=httpx.Response(401))
    with pytest.raises(UrlscanAuthError):
        client.search("anything")


@respx.mock
def test_403_raises_auth_error(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/search/").mock(return_value=httpx.Response(403))
    with pytest.raises(UrlscanAuthError):
        client.search("anything")


@respx.mock
def test_429_raises_rate_limit(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/search/").mock(
        return_value=httpx.Response(429, headers={"Retry-After": "60"})
    )
    with pytest.raises(UrlscanRateLimitError, match="60"):
        client.search("anything")


@respx.mock
def test_500_raises_connection_error(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/search/").mock(return_value=httpx.Response(503))
    with pytest.raises(UrlscanConnectionError):
        client.search("anything")


@respx.mock
def test_400_non_denylist_raises_request_error(client: UrlscanClient) -> None:
    respx.get("https://urlscan.io/api/v1/search/").mock(
        return_value=httpx.Response(400, text="Invalid query syntax")
    )
    with pytest.raises(UrlscanRequestError, match="Invalid query syntax"):
        client.search("malformed")
