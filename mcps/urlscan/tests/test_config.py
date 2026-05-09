"""Tests for the urlscan MCP config loader."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import SecretStr

from urlscan.config import UrlscanConfig, load_config


@pytest.fixture
def valid_env(tmp_path: Path) -> Path:
    env = tmp_path / ".env"
    env.write_text("URLSCAN_API_KEY=fake-test-key-aaaa-bbbb-cccc-dddd\n", encoding="utf-8")
    return env


@pytest.fixture
def clean_env() -> None:
    """Strip URLSCAN_* env vars at setup AND teardown.

    The teardown step is critical because individual tests use
    load_dotenv() which adds new URLSCAN_* keys to os.environ that
    weren't saved at setup. Without the explicit teardown strip,
    those leak into subsequent tests in other modules (e.g. test_client
    saw URLSCAN_API_BASE_URL=http://mock.local/ from this module's
    test_base_url_overridable test).
    """
    keys = [k for k in os.environ if k.startswith("URLSCAN_")]
    saved = {k: os.environ.pop(k) for k in keys}
    yield
    # Clean any URLSCAN_* set during the test (load_dotenv side-effect)
    for k in [k for k in os.environ if k.startswith("URLSCAN_")]:
        del os.environ[k]
    # Restore originals
    os.environ.update(saved)


def test_loads_valid_config(valid_env: Path, clean_env: None) -> None:
    with patch("urlscan.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()
    assert isinstance(cfg.urlscan_api_key, SecretStr)
    assert cfg.urlscan_api_key.get_secret_value() == "fake-test-key-aaaa-bbbb-cccc-dddd"
    assert str(cfg.urlscan_api_base_url).startswith("https://urlscan.io/api/v1/")


def test_api_key_redacted_in_repr(valid_env: Path, clean_env: None) -> None:
    with patch("urlscan.config.find_dotenv", return_value=str(valid_env)):
        cfg = load_config()
    assert "fake-test-key-aaaa-bbbb-cccc-dddd" not in repr(cfg)
    assert "fake-test-key-aaaa-bbbb-cccc-dddd" not in str(cfg)


def test_missing_key_fails_with_clear_message(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("# no URLSCAN_API_KEY here\n", encoding="utf-8")
    with patch("urlscan.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="URLSCAN_API_KEY"):
            load_config()


def test_base_url_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text(
        "URLSCAN_API_KEY=k\n"
        "URLSCAN_API_BASE_URL=http://mock.local/api/v1/\n",
        encoding="utf-8",
    )
    with patch("urlscan.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert str(cfg.urlscan_api_base_url) == "http://mock.local/api/v1/"
