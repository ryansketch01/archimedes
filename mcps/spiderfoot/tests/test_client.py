"""Unit tests for the SpiderFoot HTTP client.

Uses respx to mock httpx without hitting a real SpiderFoot daemon.
Covers:
  - health: reachable, auth-rejected, unreachable
  - start_scan: response-shape variants (list / dict / fallback to /scanlist)
  - get_scan_status: dict and list payload normalization
  - export_results: list and dict-wrapped payloads
  - run_passive_scan: end-to-end with mocked status progression and event export
  - timeout: scan never reaches terminal status, returns RUNNING-TIMEOUT-* with partial events
  - error mapping: 401/403/5xx
"""

from __future__ import annotations

from typing import Iterator

import httpx
import pytest
import respx

from spiderfoot_mcp.config import SpiderFootConfig
from spiderfoot_mcp.exceptions import (
    SpiderFootAuthError,
    SpiderFootConnectionError,
    SpiderFootRequestError,
    SpiderFootScanError,
)
from spiderfoot_mcp.spiderfoot_client import SpiderFootClient


BASE = "http://sf.local:5001"


def _config(**overrides) -> SpiderFootConfig:
    base = {
        "SPIDERFOOT_URL": f"{BASE}/",
        "SPIDERFOOT_SCAN_TIMEOUT_SECONDS": 5.0,
        "SPIDERFOOT_POLL_INTERVAL_SECONDS": 0.01,
        "SPIDERFOOT_HTTP_TIMEOUT_SECONDS": 5.0,
        "SPIDERFOOT_VERIFY_SSL": True,
    }
    base.update(overrides)
    return SpiderFootConfig(**base)  # type: ignore[arg-type]


@pytest.fixture
def client() -> Iterator[SpiderFootClient]:
    c = SpiderFootClient(_config())
    yield c
    c.close()


@pytest.fixture
def auth_client() -> Iterator[SpiderFootClient]:
    cfg = _config(SPIDERFOOT_USERNAME="archimedes", SPIDERFOOT_PASSWORD="swordfish")
    c = SpiderFootClient(cfg)
    yield c
    c.close()


# ---------- health ----------


@respx.mock
def test_health_reachable_no_auth(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/ping").mock(return_value=httpx.Response(200, text="pong"))
    h = client.health()
    assert h.reachable is True
    assert h.authenticated is None  # no auth configured
    assert h.message == "OK"


@respx.mock
def test_health_reachable_with_auth_accepted(auth_client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/ping").mock(return_value=httpx.Response(200, text="pong"))
    respx.get(f"{BASE}/scanlist").mock(return_value=httpx.Response(200, json=[]))
    h = auth_client.health()
    assert h.reachable is True
    assert h.authenticated is True


@respx.mock
def test_health_auth_rejected(auth_client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/ping").mock(return_value=httpx.Response(401, text="auth required"))
    h = auth_client.health()
    assert h.reachable is True
    assert h.authenticated is False
    assert "rejected credentials" in (h.message or "")


@respx.mock
def test_health_unreachable(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/ping").mock(side_effect=httpx.ConnectError("nope"))
    h = client.health()
    assert h.reachable is False
    assert "Could not connect" in (h.message or "")


@respx.mock
def test_health_falls_back_to_scanlist_when_ping_unrecognized(client: SpiderFootClient) -> None:
    """Older / forked SpiderFoot may not have /ping. /scanlist must work as a fallback."""
    respx.get(f"{BASE}/ping").mock(return_value=httpx.Response(404, text=""))
    respx.get(f"{BASE}/scanlist").mock(return_value=httpx.Response(200, json=[]))
    h = client.health()
    assert h.reachable is True
    assert "scanlist" in (h.message or "").lower()


# ---------- start_scan ----------


@respx.mock
def test_start_scan_list_response(client: SpiderFootClient) -> None:
    respx.post(f"{BASE}/startscan").mock(
        return_value=httpx.Response(200, json=["SUCCESS", "ABCD-1234"])
    )
    sid = client.start_scan(
        target="example.com",
        modules=["sfp_crt", "sfp_whois"],
        scan_name="archimedes-test",
    )
    assert sid == "ABCD-1234"


@respx.mock
def test_start_scan_dict_response(client: SpiderFootClient) -> None:
    respx.post(f"{BASE}/startscan").mock(
        return_value=httpx.Response(200, json={"id": "DICT-9999", "status": "STARTED"})
    )
    sid = client.start_scan(
        target="example.com", modules=["sfp_crt"], scan_name="x"
    )
    assert sid == "DICT-9999"


@respx.mock
def test_start_scan_falls_back_to_scanlist(client: SpiderFootClient) -> None:
    """When /startscan response is unparseable, the client probes /scanlist
    for the most recent scan with the matching name."""
    respx.post(f"{BASE}/startscan").mock(
        return_value=httpx.Response(200, html="<html>ok</html>")
    )
    respx.get(f"{BASE}/scanlist").mock(
        return_value=httpx.Response(
            200,
            json=[
                ["FALLBACK-7777", "archimedes-fallback", "example.com",
                 "2026-05-09T12:00", "", "RUNNING", 0]
            ],
        )
    )
    sid = client.start_scan(
        target="example.com", modules=["sfp_crt"], scan_name="archimedes-fallback"
    )
    assert sid == "FALLBACK-7777"


@respx.mock
def test_start_scan_unparseable_raises(client: SpiderFootClient) -> None:
    respx.post(f"{BASE}/startscan").mock(
        return_value=httpx.Response(200, html="<html>nope</html>")
    )
    respx.get(f"{BASE}/scanlist").mock(return_value=httpx.Response(200, json=[]))
    with pytest.raises(SpiderFootScanError, match="Could not extract scan_id"):
        client.start_scan(
            target="example.com", modules=["sfp_crt"], scan_name="will-not-find-it"
        )


@respx.mock
def test_start_scan_prefixes_modules_with_module_(client: SpiderFootClient) -> None:
    """SpiderFoot's modulelist param expects each module prefixed with `module_`."""
    route = respx.post(f"{BASE}/startscan").mock(
        return_value=httpx.Response(200, json=["SUCCESS", "X1"])
    )
    client.start_scan(target="example.com", modules=["sfp_crt", "sfp_whois"], scan_name="n")
    assert route.called
    sent_form = dict(route.calls.last.request.url.params)
    # Form-encoded body, not query string — pull it differently
    body = route.calls.last.request.content.decode()
    assert "modulelist=module_sfp_crt%2Cmodule_sfp_whois" in body
    assert "usecase=Passive" in body


# ---------- get_scan_status ----------


@respx.mock
def test_get_scan_status_dict(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(
            200,
            json={"id": "X1", "name": "n", "status": "RUNNING", "events_count": 5},
        )
    )
    body = client.get_scan_status("X1")
    assert body["status"] == "RUNNING"
    assert body["events_count"] == 5


@respx.mock
def test_get_scan_status_list_normalized(client: SpiderFootClient) -> None:
    """Older SpiderFoot returns a positional list; client normalizes to dict."""
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(
            200,
            json=["scan-name", "example.com", "2026-05-09 12:00", "", "FINISHED", 42],
        )
    )
    body = client.get_scan_status("X1")
    assert body["status"] == "FINISHED"
    assert body["target"] == "example.com"
    assert body["events_count"] == 42


@respx.mock
def test_get_scan_status_unexpected_raises(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(200, text="something garbled")
    )
    with pytest.raises(SpiderFootRequestError, match="Unexpected /scanstatus"):
        client.get_scan_status("X1")


# ---------- export_results ----------


@respx.mock
def test_export_results_list(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scaneventresultexport").mock(
        return_value=httpx.Response(
            200,
            json=[
                {"type": "DOMAIN_NAME", "data": "sub.example.com",
                 "module": "sfp_crt", "source": "INTERNET_NAME",
                 "generated": "2026-05-09 12:00:01"},
                {"type": "IP_ADDRESS", "data": "203.0.113.5",
                 "module": "sfp_dnsresolve", "source": "DOMAIN_NAME",
                 "generated": "2026-05-09 12:00:05"},
            ],
        )
    )
    out = client.export_results("X1")
    assert len(out) == 2
    assert out[0]["type"] == "DOMAIN_NAME"


@respx.mock
def test_export_results_dict_wrapped(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scaneventresultexport").mock(
        return_value=httpx.Response(
            200,
            json={"events": [{"type": "DOMAIN_NAME", "data": "x",
                             "module": "sfp_crt"}]},
        )
    )
    out = client.export_results("X1")
    assert len(out) == 1


@respx.mock
def test_export_results_empty(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scaneventresultexport").mock(
        return_value=httpx.Response(200, json=[])
    )
    assert client.export_results("X1") == []


# ---------- run_passive_scan ----------


@respx.mock
def test_run_passive_scan_happy_path(client: SpiderFootClient) -> None:
    respx.post(f"{BASE}/startscan").mock(
        return_value=httpx.Response(200, json=["SUCCESS", "SCAN-1"])
    )
    # Two RUNNING polls then FINISHED
    respx.get(f"{BASE}/scanstatus").mock(
        side_effect=[
            httpx.Response(200, json={"id": "SCAN-1", "status": "RUNNING"}),
            httpx.Response(200, json={"id": "SCAN-1", "status": "RUNNING"}),
            httpx.Response(200, json={"id": "SCAN-1", "status": "FINISHED"}),
        ]
    )
    respx.get(f"{BASE}/scaneventresultexport").mock(
        return_value=httpx.Response(
            200,
            json=[
                {"type": "DOMAIN_NAME", "data": "a.example.com",
                 "module": "sfp_crt", "source": "INTERNET_NAME"},
                {"type": "DOMAIN_NAME", "data": "b.example.com",
                 "module": "sfp_crt", "source": "INTERNET_NAME"},
                {"type": "DOMAIN_NAME", "data": "a.example.com",  # duplicate
                 "module": "sfp_crt", "source": "INTERNET_NAME"},
                {"type": "IP_ADDRESS", "data": "203.0.113.5",
                 "module": "sfp_dnsresolve", "source": "DOMAIN_NAME"},
                {"type": "EMAILADDR", "data": "abuse@example.com",
                 "module": "sfp_whois", "source": "DOMAIN_NAME"},
            ],
        )
    )

    out = client.run_passive_scan(
        target="example.com",
        modules=["sfp_crt", "sfp_whois", "sfp_dnsresolve"],
        scan_name="happy",
    )
    assert out.scan_id == "SCAN-1"
    assert out.status == "FINISHED"
    assert out.target == "example.com"
    assert len(out.events) == 5
    assert out.distinct_domains == ["a.example.com", "b.example.com"]
    assert out.distinct_ips == ["203.0.113.5"]
    assert out.distinct_emails == ["abuse@example.com"]
    assert out.web_url and "scaninfo?id=SCAN-1" in out.web_url


@respx.mock
def test_run_passive_scan_timeout_returns_partial(client: SpiderFootClient) -> None:
    """When scan never reaches terminal status, return partial events with
    RUNNING-TIMEOUT-* status. Don't raise — partial results are intel."""
    respx.post(f"{BASE}/startscan").mock(
        return_value=httpx.Response(200, json=["SUCCESS", "TIMEOUT-1"])
    )
    # Always RUNNING, never finishes
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(200, json={"id": "TIMEOUT-1", "status": "RUNNING"})
    )
    respx.get(f"{BASE}/scaneventresultexport").mock(
        return_value=httpx.Response(
            200,
            json=[{"type": "DOMAIN_NAME", "data": "partial.example.com",
                   "module": "sfp_crt", "source": "INTERNET_NAME"}],
        )
    )

    # Use a tiny scan timeout so the test runs fast.
    cfg = _config(SPIDERFOOT_SCAN_TIMEOUT_SECONDS=0.05, SPIDERFOOT_POLL_INTERVAL_SECONDS=0.01)
    c = SpiderFootClient(cfg)
    try:
        out = c.run_passive_scan(
            target="example.com", modules=["sfp_crt"], scan_name="timeout"
        )
    finally:
        c.close()

    assert out.scan_id == "TIMEOUT-1"
    assert out.status.startswith("RUNNING-TIMEOUT")
    assert len(out.events) == 1
    assert out.distinct_domains == ["partial.example.com"]


# ---------- error mapping ----------


@respx.mock
def test_5xx_surfaces_as_connection_error(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(500, text="boom")
    )
    with pytest.raises(SpiderFootConnectionError, match="500"):
        client.get_scan_status("X1")


@respx.mock
def test_401_surfaces_as_auth_error(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(401, text="nope")
    )
    with pytest.raises(SpiderFootAuthError):
        client.get_scan_status("X1")


@respx.mock
def test_4xx_surfaces_as_request_error(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(404, text="no such scan")
    )
    with pytest.raises(SpiderFootRequestError, match="404"):
        client.get_scan_status("X1")
