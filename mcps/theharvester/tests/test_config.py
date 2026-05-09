"""Tests for the theHarvester MCP config loader."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest

from theharvester_mcp.config import TheHarvesterConfig, load_config


@pytest.fixture
def clean_env() -> None:
    """Strip THEHARVESTER_* env vars at setup AND teardown."""
    keys = [k for k in os.environ if k.startswith("THEHARVESTER_")]
    saved = {k: os.environ.pop(k) for k in keys}
    yield
    for k in [k for k in os.environ if k.startswith("THEHARVESTER_")]:
        del os.environ[k]
    os.environ.update(saved)


def test_loads_with_defaults_when_no_env_vars(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("# nothing relevant\n", encoding="utf-8")
    with patch("theharvester_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.theharvester_bin == "theHarvester"
    assert cfg.theharvester_timeout_seconds == 600.0
    assert cfg.theharvester_default_limit == 100


def test_bin_path_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("THEHARVESTER_BIN=/custom/path/theHarvester\n", encoding="utf-8")
    with patch("theharvester_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.theharvester_bin == "/custom/path/theHarvester"


def test_timeout_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("THEHARVESTER_TIMEOUT_SECONDS=120.5\n", encoding="utf-8")
    with patch("theharvester_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.theharvester_timeout_seconds == 120.5


def test_limit_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("THEHARVESTER_DEFAULT_LIMIT=500\n", encoding="utf-8")
    with patch("theharvester_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.theharvester_default_limit == 500


def test_invalid_timeout_rejected(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("THEHARVESTER_TIMEOUT_SECONDS=-5\n", encoding="utf-8")
    with patch("theharvester_mcp.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="Invalid"):
            load_config()


def test_invalid_limit_rejected(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("THEHARVESTER_DEFAULT_LIMIT=0\n", encoding="utf-8")
    with patch("theharvester_mcp.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="Invalid"):
            load_config()


def test_missing_dotenv_falls_back_to_defaults(clean_env: None) -> None:
    """theHarvester needs no secrets at the MCP level; missing .env is fine."""
    with patch("theharvester_mcp.config.find_dotenv", return_value=""):
        cfg = load_config()
    assert isinstance(cfg, TheHarvesterConfig)
    assert cfg.theharvester_bin == "theHarvester"
