"""Tests for the RSS Bridge MCP config loader."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest

from rss_bridge.config import DEFAULT_USER_AGENT, RssBridgeConfig, load_config


@pytest.fixture
def clean_env() -> None:
    keys = [k for k in os.environ if k.startswith("RSS_BRIDGE_")]
    saved = {k: os.environ.pop(k) for k in keys}
    yield
    os.environ.update(saved)


def test_loads_with_defaults_when_no_env_vars(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("# nothing relevant\n", encoding="utf-8")
    with patch("rss_bridge.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.rss_bridge_user_agent == DEFAULT_USER_AGENT
    assert cfg.rss_bridge_timeout_seconds == 30.0
    assert cfg.rss_bridge_max_items_default == 50


def test_user_agent_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("RSS_BRIDGE_USER_AGENT=CustomBot/1.0\n", encoding="utf-8")
    with patch("rss_bridge.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.rss_bridge_user_agent == "CustomBot/1.0"


def test_timeout_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("RSS_BRIDGE_TIMEOUT_SECONDS=15.5\n", encoding="utf-8")
    with patch("rss_bridge.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.rss_bridge_timeout_seconds == 15.5


def test_max_items_overridable(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("RSS_BRIDGE_MAX_ITEMS_DEFAULT=200\n", encoding="utf-8")
    with patch("rss_bridge.config.find_dotenv", return_value=str(env)):
        cfg = load_config()
    assert cfg.rss_bridge_max_items_default == 200


def test_invalid_timeout_rejected(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("RSS_BRIDGE_TIMEOUT_SECONDS=-5\n", encoding="utf-8")
    with patch("rss_bridge.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="Invalid"):
            load_config()


def test_invalid_max_items_rejected(tmp_path: Path, clean_env: None) -> None:
    env = tmp_path / ".env"
    env.write_text("RSS_BRIDGE_MAX_ITEMS_DEFAULT=0\n", encoding="utf-8")
    with patch("rss_bridge.config.find_dotenv", return_value=str(env)):
        with pytest.raises(RuntimeError, match="Invalid"):
            load_config()


def test_missing_dotenv_falls_back_to_defaults(clean_env: None) -> None:
    """RSS doesn't need keys, so a missing .env should not be fatal."""
    with patch("rss_bridge.config.find_dotenv", return_value=""):
        cfg = load_config()
    assert isinstance(cfg, RssBridgeConfig)
    assert cfg.rss_bridge_user_agent == DEFAULT_USER_AGENT
