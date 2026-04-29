"""Tests for the Splunk MCP config loader."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import SecretStr

from splunk_query.config import SplunkConfig, load_config


@pytest.fixture
def valid_env(tmp_path: Path) -> Path:
    """Write a complete, valid .env to a temp dir."""
    env = tmp_path / ".env"
    env.write_text(
        "SPLUNK_REST_URL=https://127.0.0.1:8089\n"
        "SPLUNK_REST_USER=admin\n"
        "SPLUNK_REST_PASSWORD=hunter2\n"
        "SPLUNK_REST_VERIFY_SSL=false\n",
        encoding="utf-8",
    )
    return env


@pytest.fixture
def clean_env() -> None:
    """Strip SPLUNK_REST_* from os.environ for the duration of the test."""
    keys = [k for k in os.environ if k.startswith("SPLUNK_REST_")]
    saved = {k: os.environ.pop(k) for k in keys}
    yield
    os.environ.update(saved)


def test_loads_valid_config(valid_env: Path, clean_env: None) -> None:
    """Happy path: all env vars set, config loads cleanly."""
    with patch("splunk_query.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()

    assert str(cfg.splunk_rest_url).rstrip("/") == "https://127.0.0.1:8089"
    assert cfg.splunk_rest_user == "admin"
    assert isinstance(cfg.splunk_rest_password, SecretStr)
    assert cfg.splunk_rest_password.get_secret_value() == "hunter2"
    assert cfg.splunk_rest_verify_ssl is False


def test_password_is_redacted_in_repr(valid_env: Path, clean_env: None) -> None:
    """SecretStr should never expose the password in repr/str output."""
    with patch("splunk_query.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()

    assert "hunter2" not in repr(cfg)
    assert "hunter2" not in str(cfg)


def test_missing_key_fails_with_clear_message(tmp_path: Path, clean_env: None) -> None:
    """Missing required vars produce an error naming the missing key."""
    env = tmp_path / ".env"
    env.write_text(
        "SPLUNK_REST_URL=https://127.0.0.1:8089\n"
        "SPLUNK_REST_USER=admin\n"
        # SPLUNK_REST_PASSWORD intentionally omitted
        "SPLUNK_REST_VERIFY_SSL=false\n",
        encoding="utf-8",
    )

    with patch("splunk_query.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="SPLUNK_REST_PASSWORD"):
            load_config()


@pytest.mark.parametrize("raw,expected", [("false", False), ("False", False), ("0", False),
                                          ("true", True), ("True", True), ("1", True)])
def test_ssl_flag_parsing(tmp_path: Path, clean_env: None, raw: str, expected: bool) -> None:
    """Boolean parsing handles common spellings."""
    env = tmp_path / ".env"
    env.write_text(
        "SPLUNK_REST_URL=https://127.0.0.1:8089\n"
        "SPLUNK_REST_USER=admin\n"
        "SPLUNK_REST_PASSWORD=x\n"
        f"SPLUNK_REST_VERIFY_SSL={raw}\n",
        encoding="utf-8",
    )

    with patch("splunk_query.config.find_dotenv", return_value=str(env)):
        cfg = load_config()

    assert cfg.splunk_rest_verify_ssl is expected