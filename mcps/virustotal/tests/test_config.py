"""Tests for the VirusTotal MCP config loader."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import SecretStr

from virustotal.config import VTConfig, load_config


@pytest.fixture
def valid_env(tmp_path: Path) -> Path:
    env = tmp_path / ".env"
    env.write_text(
        "VT_API_KEY=fake-test-key-1234567890abcdef\n",
        encoding="utf-8",
    )
    return env


@pytest.fixture
def clean_env() -> None:
    keys = [k for k in os.environ if k.startswith("VT_")]
    saved = {k: os.environ.pop(k) for k in keys}
    yield
    os.environ.update(saved)


def test_loads_valid_config(valid_env: Path, clean_env: None) -> None:
    """Happy path: VT_API_KEY set, config loads with public default base URL."""
    with patch("virustotal.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()

    assert isinstance(cfg.vt_api_key, SecretStr)
    assert cfg.vt_api_key.get_secret_value() == "fake-test-key-1234567890abcdef"
    assert str(cfg.vt_base_url).startswith("https://www.virustotal.com/")


def test_api_key_redacted_in_repr(valid_env: Path, clean_env: None) -> None:
    """SecretStr should never expose the API key in repr/str output."""
    with patch("virustotal.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()

    assert "fake-test-key-1234567890abcdef" not in repr(cfg)
    assert "fake-test-key-1234567890abcdef" not in str(cfg)


def test_missing_key_fails_with_clear_message(tmp_path: Path, clean_env: None) -> None:
    """Missing VT_API_KEY produces an error naming the key."""
    env = tmp_path / ".env"
    env.write_text("# no VT_API_KEY here\n", encoding="utf-8")

    with patch("virustotal.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="VT_API_KEY"):
            load_config()


def test_base_url_overridable(tmp_path: Path, clean_env: None) -> None:
    """VT_BASE_URL can be set to point at a mock server."""
    env = tmp_path / ".env"
    env.write_text(
        "VT_API_KEY=k\nVT_BASE_URL=http://mock.local/api/v3/\n",
        encoding="utf-8",
    )

    with patch("virustotal.config.find_dotenv", return_value=str(env)):
        cfg = load_config()

    assert str(cfg.vt_base_url) == "http://mock.local/api/v3/"
