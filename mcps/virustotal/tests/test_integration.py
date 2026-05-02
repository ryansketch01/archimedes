"""Integration tests for the VirusTotal client.

Hits the real public VirusTotal v3 API. Skipped by default — set
ARCHIMEDES_RUN_INTEGRATION=1 to enable.

Free-tier rate limit is 4 req/min. This file makes 3 real API calls,
keeping a margin. Don't add more without considering throttling.

Requires VT_API_KEY in .env at the workspace root.
"""

from __future__ import annotations

import os

import pytest

from virustotal.config import load_config
from virustotal.vt_client import VTClient

pytestmark = pytest.mark.skipif(
    os.environ.get("ARCHIMEDES_RUN_INTEGRATION") != "1",
    reason="Set ARCHIMEDES_RUN_INTEGRATION=1 to run integration tests against real VirusTotal",
)


# Universal anti-malware test signature — guaranteed to be in VT and to be
# flagged as malicious by virtually every engine. Safe to query.
EICAR_MD5 = "44d88612fea8a8f36de82e1278abb02f"


@pytest.fixture
def client():
    cfg = load_config()
    with VTClient(cfg) as c:
        yield c


def test_lookup_file_eicar(client: VTClient) -> None:
    """EICAR is the canonical AV test signature; should be found and heavily flagged."""
    out = client.lookup_file(EICAR_MD5)

    assert out.found is True, "EICAR should always be in VT"
    assert out.md5 == EICAR_MD5
    assert out.last_analysis_stats is not None
    assert out.last_analysis_stats.malicious >= 30, (
        f"EICAR should be flagged by 30+ engines, got "
        f"{out.last_analysis_stats.malicious}"
    )
    assert len(out.malicious_engines) >= 30
    assert out.vt_link and out.vt_link.startswith("https://www.virustotal.com/gui/file/")


def test_lookup_domain_google(client: VTClient) -> None:
    """google.com is benign and well-known; expect found=True with malicious≈0."""
    out = client.lookup_domain("google.com")

    assert out.found is True
    assert out.domain == "google.com"
    assert out.last_analysis_stats is not None
    # Allow up to 2 false positives — VT engines occasionally disagree
    assert out.last_analysis_stats.malicious <= 2, (
        f"google.com should not be flagged as malicious, got "
        f"{out.last_analysis_stats.malicious}"
    )


def test_lookup_ip_google_dns(client: VTClient) -> None:
    """8.8.8.8 should resolve to GOOGLE / AS15169 / US."""
    out = client.lookup_ip("8.8.8.8")

    assert out.found is True
    assert out.ip == "8.8.8.8"
    assert out.country == "US"
    assert out.asn == 15169
    assert out.as_owner and "GOOGLE" in out.as_owner.upper()
