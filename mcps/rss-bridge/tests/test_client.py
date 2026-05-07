"""Unit tests for the RSS Bridge client.

Uses respx to mock httpx without hitting the network. Covers:
  - Successful RSS parse + item trimming + HTML stripping
  - Atom feed parse
  - 304 Not Modified caching
  - 4xx/5xx/429 error mapping
  - `since` time filter
  - `max_items` cap
  - Validate-feed positive and negative paths
"""

from __future__ import annotations

import httpx
import pytest
import respx

from rss_bridge.config import RssBridgeConfig
from rss_bridge.exceptions import (
    RssBridgeConnectionError,
    RssBridgeRateLimitError,
    RssBridgeRequestError,
)
from rss_bridge.rss_client import RssBridgeClient


@pytest.fixture
def client() -> RssBridgeClient:
    cfg = RssBridgeConfig()  # type: ignore[call-arg]
    c = RssBridgeClient(cfg)
    yield c
    c.close()


SAMPLE_RSS = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Test Feed</title>
    <description>Sample for unit tests</description>
    <link>https://example.test/</link>
    <language>en</language>
    <item>
      <title>First Article</title>
      <link>https://example.test/first</link>
      <description>This is the first &lt;b&gt;article&lt;/b&gt;.</description>
      <pubDate>Tue, 06 May 2026 12:00:00 GMT</pubDate>
      <guid>https://example.test/first</guid>
      <category>cybersecurity</category>
      <category>aerospace</category>
    </item>
    <item>
      <title>Second Article</title>
      <link>https://example.test/second</link>
      <description>Older article.</description>
      <pubDate>Mon, 05 May 2026 08:00:00 GMT</pubDate>
      <guid>https://example.test/second</guid>
    </item>
  </channel>
</rss>
"""

SAMPLE_ATOM = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Atom Test</title>
  <subtitle>Atom sample</subtitle>
  <link href="https://atom.test/"/>
  <id>urn:uuid:atom-test</id>
  <updated>2026-05-07T10:00:00Z</updated>
  <entry>
    <title>Atom Item</title>
    <link href="https://atom.test/item-1"/>
    <id>urn:uuid:item-1</id>
    <updated>2026-05-07T10:00:00Z</updated>
    <published>2026-05-07T10:00:00Z</published>
    <summary>An atom entry.</summary>
    <author><name>Test Author</name></author>
  </entry>
</feed>
"""


# ---------- fetch_feed ----------


@respx.mock
def test_fetch_rss_returns_trimmed_items(client: RssBridgeClient) -> None:
    respx.get("https://example.test/feed").mock(
        return_value=httpx.Response(
            200,
            content=SAMPLE_RSS,
            headers={"ETag": '"abc123"', "Last-Modified": "Wed, 07 May 2026 09:00:00 GMT"},
        )
    )
    out = client.fetch_feed("https://example.test/feed")

    assert out.found is True
    assert out.not_modified is False
    assert out.feed_title == "Test Feed"
    assert out.feed_description == "Sample for unit tests"
    assert out.feed_language == "en"
    assert out.status_code == 200
    assert out.etag == '"abc123"'
    assert out.last_modified == "Wed, 07 May 2026 09:00:00 GMT"
    assert out.items_total_in_feed == 2
    assert len(out.items) == 2

    first = out.items[0]
    assert first.title == "First Article"
    assert first.link == "https://example.test/first"
    # HTML should be stripped from <b>article</b>
    assert first.summary == "This is the first article."
    assert first.published is not None
    assert first.published.startswith("2026-05-06T12:00:00")
    assert "cybersecurity" in first.categories
    assert "aerospace" in first.categories


@respx.mock
def test_fetch_atom_feed(client: RssBridgeClient) -> None:
    respx.get("https://atom.test/").mock(
        return_value=httpx.Response(200, content=SAMPLE_ATOM)
    )
    out = client.fetch_feed("https://atom.test/")
    assert out.found is True
    assert out.feed_title == "Atom Test"
    assert len(out.items) == 1
    assert out.items[0].author == "Test Author"
    assert out.items[0].title == "Atom Item"


@respx.mock
def test_fetch_returns_304_not_modified(client: RssBridgeClient) -> None:
    respx.get("https://example.test/feed").mock(
        return_value=httpx.Response(
            304,
            headers={"ETag": '"abc123"'},
        )
    )
    out = client.fetch_feed("https://example.test/feed", etag='"abc123"')
    assert out.found is True
    assert out.not_modified is True
    assert out.status_code == 304
    assert out.items == []
    assert out.etag == '"abc123"'


@respx.mock
def test_since_filter_drops_older_items(client: RssBridgeClient) -> None:
    respx.get("https://example.test/feed").mock(
        return_value=httpx.Response(200, content=SAMPLE_RSS)
    )
    # Cutoff between the two sample items
    out = client.fetch_feed(
        "https://example.test/feed", since="2026-05-06T00:00:00+00:00"
    )
    # First (May 6) kept; second (May 5) dropped
    assert out.items_total_in_feed == 2
    assert out.items_after_since_filter == 1
    assert len(out.items) == 1
    assert out.items[0].title == "First Article"


@respx.mock
def test_max_items_caps_results(client: RssBridgeClient) -> None:
    respx.get("https://example.test/feed").mock(
        return_value=httpx.Response(200, content=SAMPLE_RSS)
    )
    out = client.fetch_feed("https://example.test/feed", max_items=1)
    assert len(out.items) == 1
    assert out.items_total_in_feed == 2
    assert out.items_after_since_filter == 2


@respx.mock
def test_429_raises_rate_limit_error(client: RssBridgeClient) -> None:
    respx.get("https://rate.test/feed").mock(
        return_value=httpx.Response(429, headers={"Retry-After": "60"})
    )
    with pytest.raises(RssBridgeRateLimitError, match="60"):
        client.fetch_feed("https://rate.test/feed")


@respx.mock
def test_500_raises_connection_error(client: RssBridgeClient) -> None:
    respx.get("https://err.test/feed").mock(return_value=httpx.Response(503))
    with pytest.raises(RssBridgeConnectionError):
        client.fetch_feed("https://err.test/feed")


@respx.mock
def test_403_raises_request_error(client: RssBridgeClient) -> None:
    respx.get("https://forbidden.test/feed").mock(return_value=httpx.Response(403))
    with pytest.raises(RssBridgeRequestError):
        client.fetch_feed("https://forbidden.test/feed")


# ---------- validate_feed ----------


@respx.mock
def test_validate_returns_true_for_valid_rss(client: RssBridgeClient) -> None:
    respx.get("https://example.test/feed").mock(
        return_value=httpx.Response(200, content=SAMPLE_RSS)
    )
    out = client.validate_feed("https://example.test/feed")
    assert out.valid is True
    assert out.feed_title == "Test Feed"
    assert out.feed_type == "rss"
    assert out.items_total == 2
    assert out.error is None


@respx.mock
def test_validate_returns_true_for_valid_atom(client: RssBridgeClient) -> None:
    respx.get("https://atom.test/").mock(
        return_value=httpx.Response(200, content=SAMPLE_ATOM)
    )
    out = client.validate_feed("https://atom.test/")
    assert out.valid is True
    assert out.feed_type == "atom"


@respx.mock
def test_validate_returns_false_for_html(client: RssBridgeClient) -> None:
    respx.get("https://html.test/").mock(
        return_value=httpx.Response(
            200,
            content=b"<!DOCTYPE html><html><body>not a feed</body></html>",
            headers={"Content-Type": "text/html"},
        )
    )
    out = client.validate_feed("https://html.test/")
    assert out.valid is False
    assert "not a valid feed" in (out.error or "")


@respx.mock
def test_validate_returns_false_for_empty_body(client: RssBridgeClient) -> None:
    respx.get("https://empty.test/").mock(return_value=httpx.Response(200, content=b""))
    out = client.validate_feed("https://empty.test/")
    assert out.valid is False
    assert "empty" in (out.error or "").lower()


@respx.mock
def test_validate_returns_false_for_404(client: RssBridgeClient) -> None:
    respx.get("https://gone.test/").mock(return_value=httpx.Response(404))
    out = client.validate_feed("https://gone.test/")
    assert out.valid is False
    assert out.status_code == 0  # request_error path resets status_code
