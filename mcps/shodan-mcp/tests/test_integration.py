"""Integration tests for the Shodan client.

Hits the real Shodan API. Skipped by default — set
ARCHIMEDES_RUN_INTEGRATION=1 to enable.

Credit accounting per run:
  - test_lookup_host_google_dns: 1 query credit
  - test_count_hosts_known_query: 0 (free)
  - test_lookup_internetdb_google_dns: 0 (free)

Total: 1 query credit per integration run. Dev plan has 100/month, so
running the suite ~98 times in a month is safe. Don't add more paid
tests without considering the budget.
"""

from __future__ import annotations

import os

import pytest

from shodan_mcp.config import load_config
from shodan_mcp.shodan_client import ShodanClient

pytestmark = pytest.mark.skipif(
    os.environ.get("ARCHIMEDES_RUN_INTEGRATION") != "1",
    reason="Set ARCHIMEDES_RUN_INTEGRATION=1 to run integration tests against real Shodan",
)


@pytest.fixture
def client():
    cfg = load_config()
    with ShodanClient(cfg) as c:
        yield c


def test_lookup_host_google_dns(client: ShodanClient) -> None:
    """8.8.8.8 should resolve to GOOGLE / AS15169 / US with port 53 visible.

    Costs 1 query credit. Test asserts on stable Shodan-known facts.
    """
    out = client.lookup_host("8.8.8.8")

    assert out.found is True
    assert out.ip == "8.8.8.8"
    assert out.country_code == "US"
    assert out.asn and "15169" in out.asn
    # port 53 (DNS) is the canonical Google DNS port and well-known
    assert 53 in out.ports
    # at least one service entry should exist
    assert len(out.services) >= 1
    assert out.shodan_link == "https://www.shodan.io/host/8.8.8.8"


def test_count_hosts_known_query(client: ShodanClient) -> None:
    """count_hosts is free; nginx hosts on port 443 should number in the millions."""
    out = client.count_hosts("product:nginx port:443")
    assert out.total > 100_000, f"expected >100k nginx:443 hosts, got {out.total}"


def test_lookup_internetdb_google_dns(client: ShodanClient) -> None:
    """InternetDB is free and well-trafficked; 8.8.8.8 always has data."""
    out = client.lookup_internetdb("8.8.8.8")

    assert out.found is True
    assert out.ip == "8.8.8.8"
    assert 53 in out.ports
