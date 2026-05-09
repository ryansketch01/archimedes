"""Live integration tests for the Censys MCP.

Hits real Censys API. Skipped by default unless CENSYS_LIVE_TEST=1
in the environment, so CI runs don't burn the free-tier quota
(~100 searches + ~250 views per month).

Each test consumes 1 quota unit. Be deliberate about running.

Run with:
    CENSYS_LIVE_TEST=1 uv run --directory mcps/censys pytest tests/test_integration.py -v
"""

from __future__ import annotations

import os

import pytest

from censys.config import load_config
from censys.censys_client import CensysClient


pytestmark = pytest.mark.skipif(
    os.environ.get("CENSYS_LIVE_TEST") != "1",
    reason="set CENSYS_LIVE_TEST=1 to enable live network tests "
           "(consumes free-tier quota)",
)


@pytest.fixture
def client() -> CensysClient:
    cfg = load_config()
    c = CensysClient(cfg)
    yield c
    c.close()


def test_live_search_hosts_known_asn_returns_results(client: CensysClient) -> None:
    """Cloudflare's ASN should return a populated host list. Consumes 1
    search-quota unit."""
    out = client.search_hosts("autonomous_system.asn: 13335", per_page=3)
    assert out.total > 0, "Cloudflare ASN search returned 0 — auth or quota issue?"
    assert len(out.hits) > 0
    h = out.hits[0]
    assert h.ip
    # Cloudflare hosts should have at least one service
    assert len(h.services) > 0


def test_live_lookup_host_known_ip_returns_data(client: CensysClient) -> None:
    """1.1.1.1 (Cloudflare DNS) should always be in Censys's index.
    Consumes 1 view-quota unit."""
    out = client.lookup_host("1.1.1.1")
    assert out.found is True
    assert out.ip == "1.1.1.1"
    assert len(out.services) > 0
    # Cloudflare DNS should have an ASN populated
    assert out.autonomous_system is not None
    assert out.censys_url == "https://search.censys.io/hosts/1.1.1.1"


def test_live_search_certificates_known_domain(client: CensysClient) -> None:
    """example.com has thousands of certs in Censys. Consumes 1 search-
    quota unit."""
    out = client.search_certificates(
        "names: example.com", per_page=3
    )
    # Even if the schema mapping drops some hits without fingerprints,
    # we should get at least one valid hit for example.com
    assert out.total > 0
    if out.hits:
        c = out.hits[0]
        assert c.fingerprint_sha256
        assert "example.com" in c.sans or c.subject_cn == "example.com"
