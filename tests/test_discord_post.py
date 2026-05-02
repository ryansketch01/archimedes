"""Unit tests for scripts/discord_post.py.

These tests do not touch the network. The only test that exercises the
Discord transport uses a fake requests.Session.
"""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path
from typing import Any

import pytest

from scripts import discord_post as discord_post_module


@pytest.fixture(scope="module")
def discord_post():
    return discord_post_module


# ---------- parse_message_input ----------

def _make_args(**overrides) -> argparse.Namespace:
    base = {"message": None, "message_file": None, "message_stdin": False}
    base.update(overrides)
    return argparse.Namespace(**base)


def test_parse_message_from_string(discord_post):
    args = _make_args(message="hello world")
    assert discord_post.parse_message_input(args) == "hello world"


def test_parse_message_from_file(discord_post, tmp_path: Path):
    p = tmp_path / "msg.txt"
    p.write_text("multi\nline\nbody", encoding="utf-8")
    args = _make_args(message_file=str(p))
    assert discord_post.parse_message_input(args) == "multi\nline\nbody"


def test_parse_message_from_stdin(discord_post, monkeypatch):
    monkeypatch.setattr(sys, "stdin", io.StringIO("from stdin\n"))
    args = _make_args(message_stdin=True)
    assert discord_post.parse_message_input(args) == "from stdin"


def test_parse_message_strips_trailing_whitespace(discord_post):
    args = _make_args(message="hello   \n\n  ")
    assert discord_post.parse_message_input(args) == "hello"


def test_parse_message_preserves_internal_newlines(discord_post):
    args = _make_args(message="line1\n\nline2")
    assert discord_post.parse_message_input(args) == "line1\n\nline2"


def test_parse_message_empty_rejected(discord_post):
    args = _make_args(message="   \n\n")
    with pytest.raises(ValueError, match="empty"):
        discord_post.parse_message_input(args)


def test_parse_message_too_long_rejected(discord_post):
    args = _make_args(message="x" * 2001)
    with pytest.raises(ValueError, match="exceeds Discord limit"):
        discord_post.parse_message_input(args)


def test_parse_message_at_limit_accepted(discord_post):
    args = _make_args(message="x" * 2000)
    assert len(discord_post.parse_message_input(args)) == 2000


def test_parse_message_no_source_specified(discord_post):
    args = _make_args()
    with pytest.raises(ValueError, match="Must supply one of"):
        discord_post.parse_message_input(args)


# ---------- resolve_channel_id ----------

def test_resolve_channel_id_from_raw(discord_post):
    args = argparse.Namespace(channel=None, channel_id="999")
    assert discord_post.resolve_channel_id(args, env={}) == "999"


def test_resolve_channel_id_from_symbolic(discord_post):
    args = argparse.Namespace(channel="commands", channel_id=None)
    env = {"DISCORD_CHANNEL_COMMANDS": "12345"}
    assert discord_post.resolve_channel_id(args, env) == "12345"


def test_resolve_channel_id_raw_overrides_symbolic(discord_post):
    # If both somehow set (shouldn't happen via argparse but sanity-check
    # the precedence), --channel-id wins.
    args = argparse.Namespace(channel="commands", channel_id="raw-123")
    assert discord_post.resolve_channel_id(args, env={"DISCORD_CHANNEL_COMMANDS": "ignored"}) == "raw-123"


# ---------- build_payload ----------

def test_build_payload_minimal(discord_post):
    assert discord_post.build_payload("hello") == {"content": "hello"}


# ---------- post_to_discord ----------

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


def test_post_to_discord_success(discord_post):
    session = _FakeSession(_FakeResponse(200, {"id": "msg-1", "channel_id": "111"}))
    status, body = discord_post.post_to_discord(
        channel_id="111",
        token="BOT-TOKEN",
        payload={"content": "hi"},
        timeout=5.0,
        session=session,
    )
    assert status == 200
    assert body == {"id": "msg-1", "channel_id": "111"}
    assert len(session.calls) == 1
    call = session.calls[0]
    assert call["url"] == "https://discord.com/api/v10/channels/111/messages"
    assert call["headers"]["Authorization"] == "Bot BOT-TOKEN"
    assert call["headers"]["Content-Type"] == "application/json"
    assert "User-Agent" in call["headers"]
    assert call["json"] == {"content": "hi"}
    assert call["timeout"] == 5.0


def test_post_to_discord_non_json_body_falls_back_to_raw(discord_post):
    session = _FakeSession(_FakeResponse(503, "Service Unavailable"))
    status, body = discord_post.post_to_discord(
        channel_id="111",
        token="t",
        payload={"content": "x"},
        session=session,
    )
    assert status == 503
    assert body == {"raw": "Service Unavailable"}


# ---------- main exit codes ----------

def test_main_missing_env_exits_2(discord_post, monkeypatch):
    def _raise(_):
        raise RuntimeError("Missing required env var(s)")
    monkeypatch.setattr(discord_post, "load_discord_env", _raise)
    rc = discord_post.main(["--message", "hi", "--channel", "commands"])
    assert rc == 2


def test_main_message_too_long_exits_5(discord_post, monkeypatch):
    monkeypatch.setattr(discord_post, "load_discord_env", lambda _: {
        "DISCORD_BOT_TOKEN": "t",
        "DISCORD_CHANNEL_COMMANDS": "111",
    })
    rc = discord_post.main(["--message", "x" * 2001, "--channel", "commands"])
    assert rc == 5


def test_main_unknown_channel_rejected_by_argparse(discord_post):
    # argparse rejects unknown choices with SystemExit(2). We don't reach
    # main()'s error handling for this — just verify it doesn't slip
    # through.
    with pytest.raises(SystemExit):
        discord_post.main(["--message", "hi", "--channel", "nonexistent"])
