"""Tests for the Shodan MCP config loader."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import SecretStr

from shodan_mcp.config import ShodanConfig, load_config


@pytest.fixture
def valid_env(tmp_path: Path) -> Path:
    env = tmp_path / ".env"
    env.write_text("SHODAN_API_KEY=fake-test-key-32-chars-aaaaaaaaa\n", encoding="utf-8")
    return env


@pytest.fixture
def clean_env() -> None:
    keys = [k for k in os.environ if k.startswith("SHODAN_")]
    saved = {k: os.environ.pop(k) for k in keys}
    yield
    os.environ.update(saved)


def test_loads_valid_config(valid_env: Path, clean_env: None) -> None:
    with patch("shodan_mcp.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()
    assert isinstance(cfg.shodan_api_key, SecretStr)
    assert cfg.shodan_api_key.get_secret_value() == "fake-test-key-32-chars-aaaaaaaaa"
    assert str(cfg.shodan_api_base_url).startswith("https://api.shodan.io/")
    assert str(cfg.shodan_internetdb_base_url).startswith("https://internetdb.shodan.io/")


def test_api_key_redacted_in_repr(valid_env: Path, clean_env: None) -> None:
    with patch("shodan_mcp.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()
    assert "fake-test-key-32-chars-aaaaaaaaa" not in repr(cfg)
    assert "fake-test-key-32-chars-aaaaaaaaa" not in str(cfg)


def test_missing_key_fails_with_clear_message(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("# no SHODAN_API_KEY here\n", encoding="utf-8")
    with patch("shodan_mcp.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="SHODAN_API_KEY"):
            load_config()


def test_base_urls_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "SHODAN_API_KEY=k\n"
        "SHODAN_API_BASE_URL=http://mock.local/api/\n"
        "SHODAN_INTERNETDB_BASE_URL=http://mock.local/idb/\n",
        encoding="utf-8",
    )
    with patch("shodan_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert str(cfg.shodan_api_base_url) == "http://mock.local/api/"
    assert str(cfg.shodan_internetdb_base_url) == "http://mock.local/idb/"
