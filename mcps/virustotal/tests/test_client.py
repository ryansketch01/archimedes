"""Tests for the VirusTotal client.

Covers:
  - Pure helpers: _unix_to_iso, _stats, _malicious_engines, _encode_url
  - Transport error translation (404 → not-found, 401 → VTAuthError, etc.)
    via httpx.MockTransport so we don't burn the free-tier rate limit.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

import httpx
import pytest
from pydantic import HttpUrl, SecretStr

from virustotal.config import VTConfig
from virustotal.exceptions import (
    VTAuthError,
    VTConnectionError,
    VTRateLimitError,
    VTRequestError,
)
from virustotal.vt_client import (
    VTClient,
    _encode_url,
    _malicious_engines,
    _stats,
    _unix_to_iso,
)


# ---------- pure helpers ----------


def test_unix_to_iso_handles_none():
    assert _unix_to_iso(None) is None


def test_unix_to_iso_returns_utc_iso():
    # 2025-01-01T00:00:00Z = 1735689600
    out = _unix_to_iso(1735689600)
    assert out == "2025-01-01T00:00:00+00:00"
    # Round-trip parseable
    assert datetime.fromisoformat(out).tzinfo == timezone.utc


def test_stats_handles_none():
    assert _stats(None) is None


def test_stats_fills_missing_fields_with_zero():
    s = _stats({"malicious": 5, "harmless": 2})
    assert s.malicious == 5
    assert s.harmless == 2
    assert s.suspicious == 0
    assert s.undetected == 0
    assert s.timeout == 0


def test_malicious_engines_empty_for_none():
    assert _malicious_engines(None) == []


def test_malicious_engines_filters_and_sorts():
    results = {
        "Kaspersky":   {"category": "malicious", "result": "EICAR-Test-File"},
        "Microsoft":   {"category": "malicious", "result": "Virus:DOS/EICAR_Test_File"},
        "ClamAV":      {"category": "harmless", "result": None},
        "BadEntry":    "not-a-dict",  # malformed; must be ignored
        "AVG":         {"category": "malicious", "result": "EICAR_Test"},
    }
    assert _malicious_engines(results) == ["AVG", "Kaspersky", "Microsoft"]


def test_encode_url_matches_vt_format():
    # VT example: http://www.virustotal.com → encoded ID
    encoded = _encode_url("http://www.virustotal.com")
    # base64-urlsafe of the input, no padding
    assert "=" not in encoded
    # round-trip decode by adding padding back
    import base64
    pad = encoded + "=" * (-len(encoded) % 4)
    assert base64.urlsafe_b64decode(pad).decode() == "http://www.virustotal.com"


# ---------- transport error translation ----------


def _make_client_with_handler(handler) -> VTClient:
    """Build a VTClient whose internal httpx.Client uses MockTransport."""
    cfg = VTConfig(
        VT_API_KEY=SecretStr("k"),
        VT_BASE_URL=HttpUrl("https://mock.local/api/v3/"),
    )
    client = VTClient(cfg)
    # Swap the live client for one with a mock transport
    client._client.close()
    client._client = httpx.Client(
        headers={"x-apikey": "k"},
        transport=httpx.MockTransport(handler),
    )
    return client


def test_lookup_file_404_returns_not_found():
    def handler(request):
        return httpx.Response(404, json={"error": {"code": "NotFoundError"}})

    client = _make_client_with_handler(handler)
    out = client.lookup_file("0" * 64)
    assert out.found is False
    assert out.sha256 is None


def test_lookup_file_401_raises_auth_error():
    def handler(request):
        return httpx.Response(401, json={"error": {"code": "WrongCredentialsError"}})

    client = _make_client_with_handler(handler)
    with pytest.raises(VTAuthError):
        client.lookup_file("0" * 64)


def test_lookup_file_429_raises_rate_limit_error():
    def handler(request):
        return httpx.Response(429, json={"error": {"code": "QuotaExceededError"}})

    client = _make_client_with_handler(handler)
    with pytest.raises(VTRateLimitError):
        client.lookup_file("0" * 64)


def test_lookup_file_5xx_raises_connection_error():
    def handler(request):
        return httpx.Response(503, text="Service Unavailable")

    client = _make_client_with_handler(handler)
    with pytest.raises(VTConnectionError):
        client.lookup_file("0" * 64)


def test_lookup_file_400_raises_request_error():
    def handler(request):
        return httpx.Response(400, json={"error": {"code": "BadRequest"}})

    client = _make_client_with_handler(handler)
    with pytest.raises(VTRequestError):
        client.lookup_file("0" * 64)


def test_lookup_file_200_parses_full_record():
    """Exercises the file-attribute → FileLookupOutput mapping path."""
    def handler(request):
        # Verify the path was constructed correctly
        assert request.url.path.endswith("/files/abc123")
        # Verify the API key header was sent
        assert request.headers.get("x-apikey") == "k"
        return httpx.Response(
            200,
            json={
                "data": {
                    "id": "deadbeef" * 8,
                    "type": "file",
                    "attributes": {
                        "sha256": "deadbeef" * 8,
                        "sha1": "ab" * 20,
                        "md5": "00" * 16,
                        "meaningful_name": "test.exe",
                        "type_description": "Win32 EXE",
                        "size": 12345,
                        "reputation": -50,
                        "first_submission_date": 1735689600,
                        "last_analysis_date": 1735776000,
                        "names": ["test.exe", "evil.exe"],
                        "tags": ["pe32", "signed"],
                        "last_analysis_stats": {
                            "malicious": 42, "suspicious": 1, "harmless": 0,
                            "undetected": 5, "timeout": 0,
                        },
                        "last_analysis_results": {
                            "Kaspersky": {"category": "malicious"},
                            "ClamAV": {"category": "harmless"},
                        },
                    },
                }
            },
        )

    client = _make_client_with_handler(handler)
    out = client.lookup_file("ABC123")  # uppercase to test normalization
    assert out.found is True
    assert out.sha256 == "deadbeef" * 8
    assert out.meaningful_name == "test.exe"
    assert out.size == 12345
    assert out.last_analysis_stats.malicious == 42
    assert out.malicious_engines == ["Kaspersky"]
    assert out.first_submission_date == "2025-01-01T00:00:00+00:00"
    assert out.vt_link == f"https://www.virustotal.com/gui/file/{'deadbeef' * 8}"


def test_lookup_url_404_returns_not_found_with_input_url():
    def handler(request):
        return httpx.Response(404)

    client = _make_client_with_handler(handler)
    out = client.lookup_url("http://example.com/x")
    assert out.found is False
    assert out.url == "http://example.com/x"


def test_lookup_url_constructs_base64_id_path():
    seen_paths = []

    def handler(request):
        seen_paths.append(request.url.path)
        return httpx.Response(200, json={"data": {"attributes": {}}})

    client = _make_client_with_handler(handler)
    client.lookup_url("http://example.com")
    expected_id = _encode_url("http://example.com")
    assert seen_paths[0].endswith(f"/urls/{expected_id}")


def test_lookup_domain_404_includes_normalized_domain():
    def handler(request):
        return httpx.Response(404)

    client = _make_client_with_handler(handler)
    out = client.lookup_domain("Example.COM")
    assert out.found is False
    assert out.domain == "example.com"


def test_lookup_ip_200_pulls_geo_and_asn():
    def handler(request):
        assert request.url.path.endswith("/ip_addresses/8.8.8.8")
        return httpx.Response(
            200,
            json={
                "data": {
                    "attributes": {
                        "country": "US",
                        "asn": 15169,
                        "as_owner": "GOOGLE",
                        "network": "8.8.8.0/24",
                        "last_analysis_stats": {"malicious": 0, "harmless": 80},
                    }
                }
            },
        )

    client = _make_client_with_handler(handler)
    out = client.lookup_ip("8.8.8.8")
    assert out.found is True
    assert out.country == "US"
    assert out.asn == 15169
    assert out.as_owner == "GOOGLE"
    assert out.network == "8.8.8.0/24"


def test_connect_error_raises_vt_connection_error():
    def handler(request):
        raise httpx.ConnectError("socket refused")

    client = _make_client_with_handler(handler)
    with pytest.raises(VTConnectionError):
        client.lookup_file("0" * 64)


def test_timeout_raises_vt_connection_error():
    def handler(request):
        raise httpx.ReadTimeout("slow VT")

    client = _make_client_with_handler(handler)
    with pytest.raises(VTConnectionError):
        client.lookup_file("0" * 64)
