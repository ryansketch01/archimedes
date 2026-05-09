"""Tests for the SpiderFoot MCP config loader."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import SecretStr

from spiderfoot_mcp.config import SpiderFootConfig, load_config


@pytest.fixture
def valid_env(tmp_path: Path) -> Path:
    env = tmp_path / ".env"
    env.write_text("SPIDERFOOT_URL=http://localhost:5001\n", encoding="utf-8")
    return env


@pytest.fixture
def clean_env() -> None:
    """Strip SPIDERFOOT_* env vars at setup AND teardown.

    Teardown is critical because individual tests run load_dotenv()
    which side-effects new SPIDERFOOT_* keys into os.environ that
    weren't saved at setup. Without the explicit teardown strip those
    leak into subsequent test modules.
    """
    keys = [k for k in os.environ if k.startswith("SPIDERFOOT_")]
    saved = {k: os.environ.pop(k) for k in keys}
    yield
    for k in [k for k in os.environ if k.startswith("SPIDERFOOT_")]:
        del os.environ[k]
    os.environ.update(saved)


def test_loads_valid_config(valid_env: Path, clean_env: None) -> None:
    with patch("spiderfoot_mcp.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()
    assert isinstance(cfg, SpiderFootConfig)
    assert str(cfg.spiderfoot_url).rstrip("/") == "http://localhost:5001"
    assert cfg.spiderfoot_username is None
    assert cfg.spiderfoot_password is None
    assert cfg.spiderfoot_scan_timeout_seconds == 600.0
    assert cfg.spiderfoot_poll_interval_seconds == 5.0
    assert cfg.spiderfoot_http_timeout_seconds == 30.0
    assert cfg.spiderfoot_verify_ssl is True


def test_missing_url_fails_with_clear_message(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("# no SPIDERFOOT_URL here\n", encoding="utf-8")
    with patch("spiderfoot_mcp.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="SPIDERFOOT_URL"):
            load_config()


def test_optional_auth_loads_when_set(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "SPIDERFOOT_URL=http://sf.local:5001\n"
        "SPIDERFOOT_USERNAME=archimedes\n"
        "SPIDERFOOT_PASSWORD=swordfish\n",
        encoding="utf-8",
    )
    with patch("spiderfoot_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.spiderfoot_username == "archimedes"
    assert isinstance(cfg.spiderfoot_password, SecretStr)
    assert cfg.spiderfoot_password.get_secret_value() == "swordfish"


def test_password_redacted_in_repr(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "SPIDERFOOT_URL=http://sf.local:5001\n"
        "SPIDERFOOT_USERNAME=archimedes\n"
        "SPIDERFOOT_PASSWORD=swordfish-not-leaked\n",
        encoding="utf-8",
    )
    with patch("spiderfoot_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert "swordfish-not-leaked" not in repr(cfg)
    assert "swordfish-not-leaked" not in str(cfg)


def test_timeout_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "SPIDERFOOT_URL=http://localhost:5001\n"
        "SPIDERFOOT_SCAN_TIMEOUT_SECONDS=120\n"
        "SPIDERFOOT_POLL_INTERVAL_SECONDS=2\n",
        encoding="utf-8",
    )
    with patch("spiderfoot_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.spiderfoot_scan_timeout_seconds == 120.0
    assert cfg.spiderfoot_poll_interval_seconds == 2.0


def test_invalid_timeout_rejected(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "SPIDERFOOT_URL=http://localhost:5001\n"
        "SPIDERFOOT_SCAN_TIMEOUT_SECONDS=0\n",
        encoding="utf-8",
    )
    with patch("spiderfoot_mcp.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="Invalid SpiderFoot MCP config"):
            load_config()


def test_verify_ssl_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "SPIDERFOOT_URL=https://sf.local:5001\n"
        "SPIDERFOOT_VERIFY_SSL=false\n",
        encoding="utf-8",
    )
    with patch("spiderfoot_mcp.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.spiderfoot_verify_ssl is False


def test_missing_dotenv_raises(clean_env: None) -> None:
    with patch("spiderfoot_mcp.config.find_dotenv", return_value=""):
        with pytest.raises(RuntimeError, match="Could not find .env"):
            load_config()
