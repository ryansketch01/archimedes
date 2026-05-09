"""Tests for the Censys MCP config loader."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import SecretStr

from censys.config import CensysConfig, load_config


@pytest.fixture
def valid_env(tmp_path: Path) -> Path:
    env = tmp_path / ".env"
    env.write_text(
        "CENSYS_API_ID=fake-id-aaaa-bbbb\n"
        "CENSYS_API_SECRET=fake-secret-cccc-dddd\n",
        encoding="utf-8",
    )
    return env


@pytest.fixture
def clean_env() -> None:
    """Strip CENSYS_* env vars at setup AND teardown.

    Pattern from urlscan: load_dotenv side-effects need to be cleaned
    explicitly so a per-test .env doesn't leak across modules.
    """
    keys = [k for k in os.environ if k.startswith("CENSYS_")]
    saved = {k: os.environ.pop(k) for k in keys}
    yield
    for k in [k for k in os.environ if k.startswith("CENSYS_")]:
        del os.environ[k]
    os.environ.update(saved)


def test_loads_valid_config(valid_env: Path, clean_env: None) -> None:
    with patch("censys.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()
    assert isinstance(cfg.censys_api_id, SecretStr)
    assert isinstance(cfg.censys_api_secret, SecretStr)
    assert cfg.censys_api_id.get_secret_value() == "fake-id-aaaa-bbbb"
    assert cfg.censys_api_secret.get_secret_value() == "fake-secret-cccc-dddd"
    assert str(cfg.censys_api_base_url).startswith("https://search.censys.io/api/")


def test_secrets_redacted_in_repr(valid_env: Path, clean_env: None) -> None:
    with patch("censys.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()
    assert "fake-id-aaaa-bbbb" not in repr(cfg)
    assert "fake-secret-cccc-dddd" not in repr(cfg)
    assert "fake-id-aaaa-bbbb" not in str(cfg)
    assert "fake-secret-cccc-dddd" not in str(cfg)


def test_missing_id_fails_with_clear_message(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("CENSYS_API_SECRET=k\n", encoding="utf-8")
    with patch("censys.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="CENSYS_API_ID"):
            load_config()


def test_missing_secret_fails_with_clear_message(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("CENSYS_API_ID=k\n", encoding="utf-8")
    with patch("censys.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="CENSYS_API_SECRET"):
            load_config()


def test_base_url_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "CENSYS_API_ID=k\n"
        "CENSYS_API_SECRET=s\n"
        "CENSYS_API_BASE_URL=http://mock.local/api/\n",
        encoding="utf-8",
    )
    with patch("censys.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert str(cfg.censys_api_base_url) == "http://mock.local/api/"
