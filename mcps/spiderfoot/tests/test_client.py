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
def test_health_reachable_no_auth_modern_4_0(client: SpiderFootClient) -> None:
    """SpiderFoot 4.0.0 /ping returns JSON list ['SUCCESS', '<version>']."""
    respx.get(f"{BASE}/ping").mock(
        return_value=httpx.Response(200, json=["SUCCESS", "4.0.0"])
    )
    h = client.health()
    assert h.reachable is True
    assert h.authenticated is None  # no auth configured
    assert h.spiderfoot_version == "4.0.0"
    assert h.message == "OK"


@respx.mock
def test_health_reachable_legacy_pong(client: SpiderFootClient) -> None:
    """Older builds / forks may return plain text 'pong' on /ping."""
    respx.get(f"{BASE}/ping").mock(return_value=httpx.Response(200, text="pong"))
    h = client.health()
    assert h.reachable is True
    assert h.message == "OK"


@respx.mock
def test_health_reachable_with_auth_accepted(auth_client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/ping").mock(
        return_value=httpx.Response(200, json=["SUCCESS", "4.0.0"])
    )
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
def test_get_scan_status_modern_7_element_list(client: SpiderFootClient) -> None:
    """SpiderFoot 4.0.0 /scanstatus returns 7 elements:
    [name, target, created, started, ended, status, riskmatrix]
    Verified live against SpiderFoot 4.0.0 (Session 13)."""
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(
            200,
            json=[
                "scan-name",
                "example.com",
                "2026-05-09 12:00:00",  # created
                "2026-05-09 12:00:01",  # started
                "2026-05-09 12:00:33",  # ended
                "FINISHED",             # status
                {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0},  # riskmatrix
            ],
        )
    )
    body = client.get_scan_status("X1")
    assert body["status"] == "FINISHED"
    assert body["target"] == "example.com"
    assert body["created"] == "2026-05-09 12:00:00"
    assert body["riskmatrix"]["HIGH"] == 0


@respx.mock
def test_get_scan_status_legacy_6_element_list(client: SpiderFootClient) -> None:
    """Older / forked SpiderFoot returns 6 elements (no `created` field)."""
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
def test_get_scan_status_unknown_scan_id_raises(client: SpiderFootClient) -> None:
    """SpiderFoot returns [] for unknown scan_id — surface as a clear error."""
    respx.get(f"{BASE}/scanstatus").mock(return_value=httpx.Response(200, json=[]))
    with pytest.raises(SpiderFootRequestError, match="no record"):
        client.get_scan_status("UNKNOWN")


@respx.mock
def test_get_scan_status_unexpected_raises(client: SpiderFootClient) -> None:
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(200, text="something garbled")
    )
    with pytest.raises(SpiderFootRequestError, match="Unexpected /scanstatus"):
        client.get_scan_status("X1")


# ---------- export_results ----------


@respx.mock
def test_export_results_modern_positional_list(client: SpiderFootClient) -> None:
    """SpiderFoot 4.0.0 /scaneventresults returns list-of-lists.
    Each row: [last_seen, data, source_data, module, conf, vis, risk,
              hash, fp, reserved, event_type]
    Verified live against SpiderFoot 4.0.0 (Session 13)."""
    respx.get(f"{BASE}/scaneventresults").mock(
        return_value=httpx.Response(
            200,
            json=[
                # last_seen, data, src_data, module, conf, vis, risk, hash, fp, _, type
                ["2026-05-09 12:00:01", "sub.example.com", "example.com",
                 "sfp_crt", 100, 100, 0, "h1", 0, 0, "DOMAIN_NAME"],
                ["2026-05-09 12:00:05", "203.0.113.5", "example.com",
                 "sfp_dnsresolve", 100, 100, 0, "h2", 0, 0, "IP_ADDRESS"],
                # ROOT pseudo-event must be filtered out
                ["2026-05-09 12:00:00", "example.com", "example.com",
                 "", 100, 100, 0, "ROOT", 0, 0, "ROOT"],
            ],
        )
    )
    out = client.export_results("X1")
    assert len(out) == 2  # ROOT skipped
    assert out[0]["type"] == "DOMAIN_NAME"
    assert out[0]["data"] == "sub.example.com"
    assert out[0]["module"] == "sfp_crt"
    assert out[1]["type"] == "IP_ADDRESS"


@respx.mock
def test_export_results_uses_scaneventresults_not_export_endpoint(client: SpiderFootClient) -> None:
    """Critical: the JSON-friendly endpoint is /scaneventresults, NOT
    /scaneventresultexport. The latter returns CSV/Excel and 200s with
    HTML 'Error' when asked for JSON. Live-verified Session 13."""
    route = respx.get(f"{BASE}/scaneventresults").mock(
        return_value=httpx.Response(200, json=[])
    )
    client.export_results("X1")
    assert route.called
    sent_params = dict(route.calls.last.request.url.params)
    assert sent_params["id"] == "X1"
    assert sent_params["eventType"] == "ALL"


@respx.mock
def test_export_results_dict_wrapped(client: SpiderFootClient) -> None:
    """Forks that return {'events': [...]} are accepted."""
    respx.get(f"{BASE}/scaneventresults").mock(
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
    respx.get(f"{BASE}/scaneventresults").mock(
        return_value=httpx.Response(200, json=[])
    )
    assert client.export_results("X1") == []


# ---------- run_passive_scan ----------


@respx.mock
def test_run_passive_scan_happy_path(client: SpiderFootClient) -> None:
    respx.post(f"{BASE}/startscan").mock(
        return_value=httpx.Response(200, json=["SUCCESS", "SCAN-1"])
    )
    # Status polling — 7-element SpiderFoot 4.0.0 shape:
    # [name, target, created, started, ended, status, riskmatrix]
    respx.get(f"{BASE}/scanstatus").mock(
        side_effect=[
            httpx.Response(
                200,
                json=["happy", "example.com", "12:00:00", "12:00:01", "",
                      "RUNNING", {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}],
            ),
            httpx.Response(
                200,
                json=["happy", "example.com", "12:00:00", "12:00:01", "",
                      "RUNNING", {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}],
            ),
            httpx.Response(
                200,
                json=["happy", "example.com", "12:00:00", "12:00:01", "12:00:33",
                      "FINISHED", {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}],
            ),
        ]
    )
    # /scaneventresults positional list shape (verified live SF 4.0.0):
    respx.get(f"{BASE}/scaneventresults").mock(
        return_value=httpx.Response(
            200,
            json=[
                ["12:00:02", "a.example.com", "example.com",
                 "sfp_crt", 100, 100, 0, "h1", 0, 0, "DOMAIN_NAME"],
                ["12:00:03", "b.example.com", "example.com",
                 "sfp_crt", 100, 100, 0, "h2", 0, 0, "DOMAIN_NAME"],
                ["12:00:04", "a.example.com", "example.com",  # duplicate
                 "sfp_crt", 100, 100, 0, "h3", 0, 0, "DOMAIN_NAME"],
                ["12:00:05", "203.0.113.5", "example.com",
                 "sfp_dnsresolve", 100, 100, 0, "h4", 0, 0, "IP_ADDRESS"],
                ["12:00:06", "abuse@example.com", "example.com",
                 "sfp_whois", 100, 100, 0, "h5", 0, 0, "EMAILADDR"],
                # ROOT must be filtered out
                ["12:00:00", "example.com", "example.com",
                 "", 100, 100, 0, "ROOT", 0, 0, "ROOT"],
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
    # Always RUNNING, never finishes (modern 7-element shape)
    respx.get(f"{BASE}/scanstatus").mock(
        return_value=httpx.Response(
            200,
            json=["timeout", "example.com", "12:00:00", "12:00:01", "",
                  "RUNNING", {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}],
        )
    )
    respx.get(f"{BASE}/scaneventresults").mock(
        return_value=httpx.Response(
            200,
            json=[
                ["12:00:02", "partial.example.com", "example.com",
                 "sfp_crt", 100, 100, 0, "h1", 0, 0, "DOMAIN_NAME"],
            ],
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
