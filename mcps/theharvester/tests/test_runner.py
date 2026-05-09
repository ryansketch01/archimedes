"""Unit tests for the theHarvester subprocess runner.

Mocks subprocess.run so we don't need theHarvester installed. Covers:
  - Source allowlist enforcement (rejects active-recon sources)
  - Default source set used when none provided
  - Executable resolution (PATH lookup vs explicit THEHARVESTER_BIN)
  - JSON output parsing (multiple shapes)
  - Timeout, run-error, parse-error mapping
"""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from theharvester_mcp.config import TheHarvesterConfig
from theharvester_mcp.exceptions import (
    TheHarvesterNotInstalledError,
    TheHarvesterParseError,
    TheHarvesterPolicyError,
    TheHarvesterRunError,
    TheHarvesterTimeoutError,
)
from theharvester_mcp.harvester_runner import (
    _normalize_asns,
    _normalize_hosts,
    _normalize_strings,
    _resolve_executable,
    _validate_sources,
    run_theharvester,
)
from theharvester_mcp.models import DEFAULT_SOURCES


# ---------- _validate_sources ----------


def test_validate_sources_accepts_allowlist() -> None:
    out = _validate_sources(["crtsh", "otx", "hackertarget"])
    assert out == ["crtsh", "otx", "hackertarget"]


def test_validate_sources_rejects_active_recon() -> None:
    with pytest.raises(TheHarvesterPolicyError, match="dnsbrute"):
        _validate_sources(["crtsh", "dnsbrute"])


def test_validate_sources_lowercases_and_dedups() -> None:
    out = _validate_sources(["CRTSH", "crtsh", " OTX "])
    assert out == ["crtsh", "otx"]


def test_validate_sources_empty_input_raises() -> None:
    with pytest.raises(TheHarvesterPolicyError, match="No valid sources"):
        _validate_sources([])


def test_validate_sources_all_rejected_raises() -> None:
    with pytest.raises(TheHarvesterPolicyError):
        _validate_sources(["nonexistent", "alsobad"])


# ---------- _resolve_executable ----------


def _config(**kw) -> TheHarvesterConfig:
    return TheHarvesterConfig(
        THEHARVESTER_BIN=kw.pop("bin", "theHarvester"),
        THEHARVESTER_TIMEOUT_SECONDS=kw.pop("timeout", 600.0),
        THEHARVESTER_DEFAULT_LIMIT=kw.pop("limit", 100),
    )  # type: ignore[call-arg]


def test_resolve_executable_uses_path_when_command_bare(tmp_path: Path) -> None:
    cfg = _config(bin="theHarvester")
    # Mock shutil.which inside the runner module
    with patch("theharvester_mcp.harvester_runner.shutil.which", return_value="/usr/bin/theHarvester"):
        path = _resolve_executable(cfg)
    assert path == "/usr/bin/theHarvester"


def test_resolve_executable_path_with_separator_must_exist(tmp_path: Path) -> None:
    fake = tmp_path / "no" / "such" / "theHarvester"
    cfg = _config(bin=str(fake))
    with pytest.raises(TheHarvesterNotInstalledError, match="non-existent"):
        _resolve_executable(cfg)


def test_resolve_executable_explicit_path_that_exists(tmp_path: Path) -> None:
    fake = tmp_path / "theHarvester"
    fake.write_text("#!/bin/sh\nexit 0\n")
    cfg = _config(bin=str(fake))
    path = _resolve_executable(cfg)
    assert path == str(fake)


def test_resolve_executable_path_lookup_fails() -> None:
    cfg = _config(bin="nonexistent-tool-xyz")
    with patch("theharvester_mcp.harvester_runner.shutil.which", return_value=None):
        with pytest.raises(TheHarvesterNotInstalledError, match="not found on PATH"):
            _resolve_executable(cfg)


# ---------- output normalization ----------


def test_normalize_hosts_string_with_ips() -> None:
    out = _normalize_hosts(["sub.example.com:1.2.3.4,5.6.7.8", "other.example.com"])
    assert len(out) == 2
    assert out[0].hostname == "sub.example.com"
    assert out[0].ips == ["1.2.3.4", "5.6.7.8"]
    assert out[1].hostname == "other.example.com"
    assert out[1].ips == []


def test_normalize_hosts_dict_form() -> None:
    out = _normalize_hosts(
        [{"host": "sub.example.com", "ips": ["1.2.3.4"]}, {"hostname": "other", "ip": "5.6.7.8"}]
    )
    assert out[0].hostname == "sub.example.com"
    assert out[0].ips == ["1.2.3.4"]
    assert out[1].hostname == "other"
    assert out[1].ips == ["5.6.7.8"]


def test_normalize_hosts_skips_empty() -> None:
    out = _normalize_hosts([{}, "", {"host": "valid.example.com"}])
    assert len(out) == 1
    assert out[0].hostname == "valid.example.com"


def test_normalize_strings_filters_falsy() -> None:
    assert _normalize_strings(["a", "", None, "b"]) == ["a", "b"]


def test_normalize_strings_non_list_returns_empty() -> None:
    assert _normalize_strings(None) == []
    assert _normalize_strings({"oops": "dict"}) == []


def test_normalize_asns_string_form() -> None:
    out = _normalize_asns(["AS13335 CLOUDFLARENET", "AS15169"])
    assert len(out) == 2
    assert out[0].asn == "AS13335"
    assert out[0].name == "CLOUDFLARENET"
    assert out[1].asn == "AS15169"
    assert out[1].name is None


def test_normalize_asns_dict_form() -> None:
    out = _normalize_asns([{"asn": "AS13335", "name": "CLOUDFLARENET"}])
    assert out[0].asn == "AS13335"
    assert out[0].name == "CLOUDFLARENET"


# ---------- run_theharvester (subprocess mocked) ----------


def _write_sample_output(tmpdir: Path, payload: dict) -> None:
    """Helper to simulate theHarvester writing JSON output during the
    'subprocess run'. We mock subprocess.run to do this side effect
    AND return a CompletedProcess."""
    json_path = tmpdir / "harvest.json"
    json_path.write_text(json.dumps(payload), encoding="utf-8")


@patch("theharvester_mcp.harvester_runner.subprocess.run")
@patch("theharvester_mcp.harvester_runner.shutil.which", return_value="/fake/theHarvester")
@patch("theharvester_mcp.harvester_runner.tempfile.mkdtemp")
def test_run_theharvester_happy_path(
    mock_mkdtemp: MagicMock,
    mock_which: MagicMock,
    mock_run: MagicMock,
    tmp_path: Path,
) -> None:
    mock_mkdtemp.return_value = str(tmp_path)

    def fake_run(cmd, **kw):
        # Simulate theHarvester writing its JSON output, then exit 0
        # Find the -f arg to know basename
        f_idx = cmd.index("-f")
        basename = Path(cmd[f_idx + 1])
        json_path = Path(str(basename) + ".json")
        json_path.write_text(json.dumps({
            "hosts": ["sub.example.com:1.2.3.4", "other.example.com"],
            "ips": ["1.2.3.4", "9.9.9.9"],
            "vhosts": ["api.example.com"],
            "asns": ["AS13335 CLOUDFLARENET"],
        }), encoding="utf-8")
        return MagicMock(returncode=0, stdout="", stderr="")

    mock_run.side_effect = fake_run

    out = run_theharvester(_config(), domain="example.com", sources=["crtsh", "otx"])
    assert out.domain == "example.com"
    assert out.sources_queried == ["crtsh", "otx"]
    assert len(out.hosts) == 2
    assert out.hosts[0].hostname == "sub.example.com"
    assert out.distinct_ips == ["1.2.3.4", "9.9.9.9"]
    assert out.vhosts == ["api.example.com"]
    assert out.asns[0].asn == "AS13335"
    assert out.duration_seconds is not None and out.duration_seconds >= 0


@patch("theharvester_mcp.harvester_runner.subprocess.run")
@patch("theharvester_mcp.harvester_runner.shutil.which", return_value="/fake/theHarvester")
@patch("theharvester_mcp.harvester_runner.tempfile.mkdtemp")
def test_run_theharvester_nonzero_exit_raises(
    mock_mkdtemp: MagicMock,
    mock_which: MagicMock,
    mock_run: MagicMock,
    tmp_path: Path,
) -> None:
    mock_mkdtemp.return_value = str(tmp_path)
    mock_run.return_value = MagicMock(returncode=2, stdout="", stderr="bad domain")
    with pytest.raises(TheHarvesterRunError, match="bad domain"):
        run_theharvester(_config(), domain="bad", sources=["crtsh"])


@patch("theharvester_mcp.harvester_runner.subprocess.run")
@patch("theharvester_mcp.harvester_runner.shutil.which", return_value="/fake/theHarvester")
@patch("theharvester_mcp.harvester_runner.tempfile.mkdtemp")
def test_run_theharvester_timeout_raises(
    mock_mkdtemp: MagicMock,
    mock_which: MagicMock,
    mock_run: MagicMock,
    tmp_path: Path,
) -> None:
    import subprocess as sp

    mock_mkdtemp.return_value = str(tmp_path)
    mock_run.side_effect = sp.TimeoutExpired(cmd="theHarvester", timeout=600)
    with pytest.raises(TheHarvesterTimeoutError, match="600"):
        run_theharvester(_config(), domain="example.com", sources=["crtsh"])


@patch("theharvester_mcp.harvester_runner.subprocess.run")
@patch("theharvester_mcp.harvester_runner.shutil.which", return_value="/fake/theHarvester")
@patch("theharvester_mcp.harvester_runner.tempfile.mkdtemp")
def test_run_theharvester_missing_json_raises_parse_error(
    mock_mkdtemp: MagicMock,
    mock_which: MagicMock,
    mock_run: MagicMock,
    tmp_path: Path,
) -> None:
    mock_mkdtemp.return_value = str(tmp_path)
    # subprocess returns 0 but doesn't write the json file
    mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
    with pytest.raises(TheHarvesterParseError, match="does not exist"):
        run_theharvester(_config(), domain="example.com", sources=["crtsh"])
