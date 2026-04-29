"""Integration tests for the Splunk REST client.

These tests hit a real, running Splunk instance. They're skipped by default
unless ARCHIMEDES_RUN_INTEGRATION=1 is set in the environment.

To run:
    $env:ARCHIMEDES_RUN_INTEGRATION = "1"
    uv run pytest tests\test_integration.py -v

Requires a live Splunk on the URL/port in .env, with credentials that work
and an 'archimedes' index containing at least one event.
"""

from __future__ import annotations

import os

import pytest

from splunk_query.config import load_config
from splunk_query.exceptions import SplunkQueryError
from splunk_query.splunk_client import SplunkClient

pytestmark = pytest.mark.skipif(
    os.environ.get("ARCHIMEDES_RUN_INTEGRATION") != "1",
    reason="Set ARCHIMEDES_RUN_INTEGRATION=1 to run integration tests against real Splunk",
)


@pytest.fixture
def client():
    """Real client against the Splunk in .env. Closes on test exit."""
    cfg = load_config()
    with SplunkClient(cfg) as c:
        yield c


def test_health_returns_server_info(client: SplunkClient) -> None:
    """Health check returns the expected fields from a live Splunk."""
    info = client.health()

    assert info["version"], "version should be populated"
    assert info["server_name"], "server_name should be populated"
    assert info["license_state"] in ("OK", "EXPIRED", "VIOLATION", "TRIAL"), (
        f"unexpected license_state: {info['license_state']}"
    )


def test_search_archimedes_index_returns_events(client: SplunkClient) -> None:
    """Searching the archimedes index returns at least the HEC smoke-test event."""
    events = client.search("index=archimedes", earliest="-90d", max_results=10)

    assert len(events) >= 1, "Expected at least the Session 2B smoke-test event"
    first = events[0]
    assert first.get("index") == "archimedes"
    assert first.get("sourcetype") == "archimedes:operation"


def test_search_with_no_matches_returns_empty_list(client: SplunkClient) -> None:
    """A search that matches nothing returns [] cleanly, not None or an error."""
    events = client.search(
        "index=archimedes nonexistent_field_xyz_12345",
        earliest="-1h",
        max_results=10,
    )

    assert events == []


def test_pipe_prefixed_search_passes_through(client: SplunkClient) -> None:
    """Generating commands (|-prefixed) work without auto-prefixing 'search'."""
    events = client.search("| metadata type=sourcetypes index=archimedes", max_results=5)

    # metadata returns one row per sourcetype; archimedes:operation should be there
    assert any(e.get("sourcetype") == "archimedes:operation" for e in events), (
        f"expected archimedes:operation in metadata, got: {events}"
    )


def test_invalid_spl_raises_query_error(client: SplunkClient) -> None:
    """Malformed SPL produces a SplunkQueryError, not a generic exception."""
    with pytest.raises(SplunkQueryError):
        client.search("| this_is_not_a_real_command foo bar baz", max_results=1)


def test_max_results_cap_enforced() -> None:
    """Client refuses max_results above the Splunk Free safety cap."""
    cfg = load_config()
    with SplunkClient(cfg) as c:
        with pytest.raises(ValueError, match="must be <= 10000"):
            c.search("index=archimedes", max_results=20_000)


