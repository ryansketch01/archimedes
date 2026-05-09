"""Live integration tests for the urlscan MCP.

Hits real urlscan.io API. Skipped by default unless URLSCAN_LIVE_TEST=1
in the environment, so CI runs don't burn submit quota or depend on
third-party uptime.

Run with:
    URLSCAN_LIVE_TEST=1 uv run --directory mcps/urlscan pytest tests/test_integration.py -v

Tests are read-only by default (search + lookup_scan only). The
submit_scan path is gated behind a separate URLSCAN_LIVE_SUBMIT=1
flag because it consumes the 5,000/month free-tier quota.
"""

from __future__ import annotations

import os
import time

import pytest

from urlscan.config import load_config
from urlscan.urlscan_client import UrlscanClient


pytestmark = pytest.mark.skipif(
    os.environ.get("URLSCAN_LIVE_TEST") != "1",
    reason="set URLSCAN_LIVE_TEST=1 to enable live network tests",
)


@pytest.fixture
def client() -> UrlscanClient:
    cfg = load_config()
    c = UrlscanClient(cfg)
    yield c
    c.close()


def test_live_search_known_domain_returns_results(client: UrlscanClient) -> None:
    """example.com has been scanned thousands of times on urlscan; this
    should return >0 results."""
    out = client.search("domain:example.com", size=3)
    assert out.total > 0, "search returned 0 results for example.com — api or auth issue?"
    assert len(out.results) > 0
    e = out.results[0]
    assert e.uuid
    assert e.task.url
    assert e.page.domain  # at least the domain field should be populated


def test_live_lookup_scan_round_trip(client: UrlscanClient) -> None:
    """Search for a known domain, then look up the first result by UUID."""
    search_out = client.search("domain:example.com", size=1)
    if not search_out.results:
        pytest.skip("search returned 0 results; cannot validate lookup_scan round-trip")

    uuid = search_out.results[0].uuid
    detail = client.lookup_scan(uuid)
    assert detail.found is True
    assert detail.uuid == uuid
    assert detail.task is not None
    assert detail.web_url == f"https://urlscan.io/result/{uuid}/"


def test_live_lookup_nonexistent_returns_not_found(client: UrlscanClient) -> None:
    """A made-up UUID should return 404 -> found=false (not raise)."""
    out = client.lookup_scan("00000000-0000-0000-0000-000000000000")
    assert out.found is False


@pytest.mark.skipif(
    os.environ.get("URLSCAN_LIVE_SUBMIT") != "1",
    reason="set URLSCAN_LIVE_SUBMIT=1 to enable live scan submission "
           "(consumes free-tier quota)",
)
def test_live_submit_scan(client: UrlscanClient) -> None:
    """Submit example.com and verify we get a uuid back. Then poll
    lookup_scan once after a delay (don't wait the full 30s)."""
    out = client.submit_scan(
        url="https://example.com/",
        visibility="unlisted",  # don't pollute the public search index
        tags=["archimedes-integration-test"],
    )
    assert out.uuid
    assert out.api_url
    assert out.web_url
    assert out.visibility == "unlisted"

    # Wait a few sec, then poll once. Scan may not be complete yet — the
    # not-yet-ready response may be 404 or partial data. Just confirm we
    # don't get an auth error or 500.
    time.sleep(5)
    detail = client.lookup_scan(out.uuid)
    # Either found=True (rare; scans usually take 15-30s) or found=False
    # (still processing). Both are acceptable for this smoke test.
    assert detail.uuid == out.uuid
