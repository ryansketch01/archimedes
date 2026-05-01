"""Unit tests for scripts/splunk-log.py.

The script file is hyphenated (matches sibling scripts in scripts/), so
we load it as a module via importlib.util rather than a plain import.

These tests do not touch the network. The only test that exercises the
HEC transport uses a fake requests.Session.
"""

from __future__ import annotations

import argparse
import importlib.util
import io
import json
import sys
from pathlib import Path
from typing import Any

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "scripts" / "splunk-log.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("splunk_log", SCRIPT_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def splunk_log():
    return _load_module()


# ---------- parse_event_input ----------

def _make_args(**overrides) -> argparse.Namespace:
    base = {"event": None, "event_file": None, "event_stdin": False}
    base.update(overrides)
    return argparse.Namespace(**base)


def test_parse_event_from_string(splunk_log):
    args = _make_args(event='{"phase":"morning-brief"}')
    assert splunk_log.parse_event_input(args) == {"phase": "morning-brief"}


def test_parse_event_from_file(splunk_log, tmp_path: Path):
    p = tmp_path / "event.json"
    p.write_text('{"x": 1, "y": [2, 3]}', encoding="utf-8")
    args = _make_args(event_file=str(p))
    assert splunk_log.parse_event_input(args) == {"x": 1, "y": [2, 3]}


def test_parse_event_from_stdin(splunk_log, monkeypatch):
    monkeypatch.setattr(sys, "stdin", io.StringIO('{"from":"stdin"}'))
    args = _make_args(event_stdin=True)
    assert splunk_log.parse_event_input(args) == {"from": "stdin"}


def test_parse_event_empty_string_rejected(splunk_log):
    args = _make_args(event="   ")
    with pytest.raises(ValueError, match="empty"):
        splunk_log.parse_event_input(args)


def test_parse_event_invalid_json_rejected(splunk_log):
    args = _make_args(event="{not-json")
    with pytest.raises(ValueError, match="not valid JSON"):
        splunk_log.parse_event_input(args)


def test_parse_event_non_object_rejected(splunk_log):
    args = _make_args(event='["this", "is", "an", "array"]')
    with pytest.raises(ValueError, match="must be a JSON object"):
        splunk_log.parse_event_input(args)


def test_parse_event_no_source_specified(splunk_log):
    args = _make_args()
    with pytest.raises(ValueError, match="Must supply one of"):
        splunk_log.parse_event_input(args)


# ---------- build_payload ----------

def test_build_payload_minimal(splunk_log):
    payload = splunk_log.build_payload(
        {"k": "v"},
        index="archimedes",
        sourcetype="archimedes:operation",
        host="frank",
        source="archimedes/scripts/splunk-log.py",
    )
    assert payload == {
        "event": {"k": "v"},
        "index": "archimedes",
        "sourcetype": "archimedes:operation",
        "host": "frank",
        "source": "archimedes/scripts/splunk-log.py",
    }


# ---------- post_to_hec ----------

class _FakeResponse:
    def __init__(self, status_code: int, body: Any):
        self.status_code = status_code
        self._body = body
        self.text = body if isinstance(body, str) else json.dumps(body)

    def json(self):
        if isinstance(self._body, str):
            raise ValueError("not json")
        return self._body


class _FakeSession:
    def __init__(self, response: _FakeResponse):
        self.response = response
        self.calls: list[dict[str, Any]] = []

    def post(self, url, *, headers, json, timeout):
        self.calls.append(
            {"url": url, "headers": headers, "json": json, "timeout": timeout}
        )
        return self.response


def test_post_to_hec_success(splunk_log):
    session = _FakeSession(_FakeResponse(200, {"text": "Success", "code": 0}))
    status, body = splunk_log.post_to_hec(
        url="http://hec.local/services/collector/event",
        token="UUID-TOKEN",
        payload={"event": {"k": "v"}, "index": "archimedes"},
        timeout=5.0,
        session=session,
    )
    assert status == 200
    assert body == {"text": "Success", "code": 0}
    assert len(session.calls) == 1
    call = session.calls[0]
    assert call["url"] == "http://hec.local/services/collector/event"
    assert call["headers"] == {"Authorization": "Splunk UUID-TOKEN"}
    assert call["json"] == {"event": {"k": "v"}, "index": "archimedes"}
    assert call["timeout"] == 5.0


def test_post_to_hec_non_json_body_falls_back_to_raw(splunk_log):
    session = _FakeSession(_FakeResponse(503, "Service Unavailable"))
    status, body = splunk_log.post_to_hec(
        url="http://hec.local/services/collector/event",
        token="t",
        payload={"event": {}},
        session=session,
    )
    assert status == 503
    assert body == {"raw": "Service Unavailable"}


# ---------- main exit codes ----------

def test_main_bad_event_exits_5(splunk_log, monkeypatch):
    # load_hec_env succeeds first, so stub it
    monkeypatch.setattr(splunk_log, "load_hec_env", lambda: {
        "SPLUNK_HEC_URL": "http://hec.local/services/collector/event",
        "SPLUNK_HEC_TOKEN": "t",
        "SPLUNK_HEC_INDEX": "archimedes",
        "SPLUNK_HEC_SOURCETYPE": "archimedes:operation",
    })
    rc = splunk_log.main(["--event", "{not-json"])
    assert rc == 5


def test_main_missing_env_exits_2(splunk_log, monkeypatch):
    def _raise():
        raise RuntimeError("Missing required env var(s)")
    monkeypatch.setattr(splunk_log, "load_hec_env", _raise)
    rc = splunk_log.main(["--event", '{"x":1}'])
    assert rc == 2
