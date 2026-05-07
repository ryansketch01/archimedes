"""Live integration tests for the RSS Bridge MCP.

Hits real public RSS feeds. Skipped by default unless RSS_BRIDGE_LIVE_TEST=1
in the environment, so CI runs don't depend on third-party uptime.

Run with:
    RSS_BRIDGE_LIVE_TEST=1 uv run --directory mcps/rss-bridge pytest tests/test_integration.py -v
"""

from __future__ import annotations

import os

import pytest

from rss_bridge.config import RssBridgeConfig
from rss_bridge.rss_client import RssBridgeClient


pytestmark = pytest.mark.skipif(
    os.environ.get("RSS_BRIDGE_LIVE_TEST") != "1",
    reason="set RSS_BRIDGE_LIVE_TEST=1 to enable live network tests",
)


@pytest.fixture
def client() -> RssBridgeClient:
    cfg = RssBridgeConfig()  # type: ignore[call-arg]
    c = RssBridgeClient(cfg)
    yield c
    c.close()


# Use feeds that are stable, lightweight, and don't gate by UA aggressively.
# CISA KEV is excluded because it's JSON, not RSS.

LIVE_FEEDS = [
    ("krebs", "https://krebsonsecurity.com/feed/"),
    ("the-record", "https://therecord.media/feed/"),
    ("bleeping", "https://www.bleepingcomputer.com/feed/"),
]


@pytest.mark.parametrize("name,url", LIVE_FEEDS)
def test_live_fetch_returns_items(client: RssBridgeClient, name: str, url: str) -> None:
    out = client.fetch_feed(url, max_items=3)
    assert out.found, f"{name}: feed at {url} did not parse"
    assert out.feed_title, f"{name}: missing feed_title"
    assert len(out.items) > 0, f"{name}: zero items returned"
    # First item should at minimum have a title and a link
    first = out.items[0]
    assert first.title, f"{name}: first item missing title"
    assert first.link, f"{name}: first item missing link"


@pytest.mark.parametrize("name,url", LIVE_FEEDS)
def test_live_validate_passes(client: RssBridgeClient, name: str, url: str) -> None:
    out = client.validate_feed(url)
    assert out.valid, f"{name}: validate_feed returned valid=false: {out.error}"
    assert out.feed_type in ("rss", "atom"), f"{name}: unexpected feed_type {out.feed_type}"


def test_live_etag_caching_round_trip(client: RssBridgeClient) -> None:
    """Two consecutive fetches with the returned ETag should yield 304."""
    url = "https://krebsonsecurity.com/feed/"
    first = client.fetch_feed(url, max_items=1)
    if not first.etag and not first.last_modified:
        pytest.skip("Krebs did not return ETag or Last-Modified; cannot test caching")

    second = client.fetch_feed(
        url,
        etag=first.etag,
        last_modified=first.last_modified,
        max_items=1,
    )
    # We can't strictly assert 304 (host may have updated between calls), but
    # if the host returned anything other than 200 or 304, that's a regression.
    assert second.status_code in (200, 304), f"unexpected status {second.status_code}"
