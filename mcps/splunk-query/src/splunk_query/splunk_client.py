"""Splunk REST API client.

Thin synchronous wrapper around httpx targeting Splunk Free's REST endpoint
on port 8089. Exposes only the operations the MCP needs: search and health.

Designed for localhost use against a single Splunk instance. The verify_ssl
flag defaults to whatever .env says (typically False for self-signed local
certs); flip it to True only when targeting a Splunk with a CA-signed cert.
"""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import urljoin

import httpx

from splunk_query.config import SplunkConfig
from splunk_query.exceptions import (
    SplunkAuthError,
    SplunkConnectionError,
    SplunkQueryError,
)

DEFAULT_EARLIEST = "-24h@h"
DEFAULT_LATEST = "now"
MAX_RESULT_LIMIT = 10_000
SEARCH_TIMEOUT_SECONDS = 60.0
HEALTH_TIMEOUT_SECONDS = 5.0


class SplunkClient:
    """Synchronous Splunk REST client.

    Use as a context manager to ensure the underlying connection pool closes:
        with SplunkClient(config) as client:
            results = client.search("index=archimedes")
    """

    def __init__(self, config: SplunkConfig) -> None:
        self._config = config
        self._base_url = str(config.splunk_rest_url).rstrip("/") + "/"
        self._client = httpx.Client(
            auth=(
                config.splunk_rest_user,
                config.splunk_rest_password.get_secret_value(),
            ),
            verify=config.splunk_rest_verify_ssl,
            timeout=SEARCH_TIMEOUT_SECONDS,
        )

    def __enter__(self) -> SplunkClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def health(self) -> dict[str, Any]:
        """Return server info: version, build, license state, server name.

        Cheap call against /services/server/info. Used as a liveness probe.

        WARNING: This endpoint is unauthenticated by design in Splunk. A
        successful health() call confirms Splunk is reachable, but does NOT
        confirm the configured credentials are valid. Use search() for that.
        """
        url = urljoin(self._base_url, "services/server/info")
        try:
            resp = self._client.get(
                url,
                params={"output_mode": "json"},
                timeout=HEALTH_TIMEOUT_SECONDS,
            )
        except httpx.ConnectError as e:
            raise SplunkConnectionError(
                f"Could not connect to Splunk at {self._base_url}: {e}"
            ) from e
        except httpx.TimeoutException as e:
            raise SplunkConnectionError(
                f"Splunk health check timed out after {HEALTH_TIMEOUT_SECONDS}s"
            ) from e

        if resp.status_code == 401:
            raise SplunkAuthError("Splunk rejected credentials (401 Unauthorized)")
        if resp.status_code >= 400:
            raise SplunkQueryError(
                f"Splunk health check failed: {resp.status_code} {resp.text[:200]}"
            )

        data = resp.json()
        entry = data.get("entry", [{}])[0].get("content", {})
        return {
            "version": entry.get("version"),
            "build": entry.get("build"),
            "server_name": entry.get("serverName"),
            "license_state": entry.get("licenseState"),
            "os_name": entry.get("os_name"),
            "startup_time": entry.get("startup_time"),
        }

    def search(
        self,
        spl: str,
        earliest: str = DEFAULT_EARLIEST,
        latest: str = DEFAULT_LATEST,
        max_results: int = 100,
    ) -> list[dict[str, Any]]:
        """Run a blocking SPL search and return events as a list of dicts.

        Args:
            spl: SPL query. May omit the leading 'search '; we add it if absent.
            earliest: Earliest time bound (Splunk time modifier, e.g. '-24h@h').
            latest: Latest time bound.
            max_results: Cap on returned events. Hard upper bound: 10000.

        Returns:
            List of event dicts. Empty list if no events match.

        Raises:
            SplunkConnectionError: Network or timeout failure.
            SplunkAuthError: Credentials rejected.
            SplunkQueryError: SPL syntax error or other Splunk-reported failure.
        """
        if max_results < 1:
            raise ValueError("max_results must be >= 1")
        if max_results > MAX_RESULT_LIMIT:
            raise ValueError(
                f"max_results must be <= {MAX_RESULT_LIMIT} (Splunk Free safety cap)"
            )

        spl_normalized = spl.strip()
        if not spl_normalized.lower().startswith(("search ", "|")):
            spl_normalized = f"search {spl_normalized}"

        url = urljoin(self._base_url, "services/search/jobs/export")
        try:
            resp = self._client.post(
                url,
                data={
                    "search": spl_normalized,
                    "earliest_time": earliest,
                    "latest_time": latest,
                    "output_mode": "json",
                    "count": str(max_results),
                    "exec_mode": "oneshot",
                },
            )
        except httpx.ConnectError as e:
            raise SplunkConnectionError(
                f"Could not connect to Splunk at {self._base_url}: {e}"
            ) from e
        except httpx.TimeoutException as e:
            raise SplunkConnectionError(
                f"Splunk search timed out after {SEARCH_TIMEOUT_SECONDS}s"
            ) from e

        if resp.status_code == 401:
            raise SplunkAuthError("Splunk rejected credentials (401 Unauthorized)")
        if resp.status_code >= 400:
            raise SplunkQueryError(
                f"Splunk search failed ({resp.status_code}): {resp.text[:500]}"
            )

        # Export endpoint returns one JSON object per line (newline-delimited JSON).
        events: list[dict[str, Any]] = []
        for line in resp.text.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if "result" in obj:
                events.append(obj["result"])

        return events