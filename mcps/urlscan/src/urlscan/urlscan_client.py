"""urlscan.io v1 REST client.

Synchronous httpx wrapper. Three operations:

  - search(query, size)        — search past public scans
  - lookup_scan(uuid)          — fetch a single scan's full record
  - submit_scan(url, ...)      — submit a new scan (async; poll later
                                  via lookup_scan)

API auth: per-request `API-Key: <key>` header. Same pattern as VT.

Endpoint shape (urlscan v1):

  GET  /api/v1/search/?q=<query>&size=<n>
  GET  /api/v1/result/<uuid>/
  POST /api/v1/scan/                           {"url": "...", "visibility": "..."}

On 404 lookup_scan returns a not-found record rather than raising —
"urlscan has no data for this UUID" is a valid analytic answer.
"""

from __future__ import annotations

from typing import Any
from urllib.parse import urljoin

import httpx

from urlscan.config import UrlscanConfig
from urlscan.exceptions import (
    UrlscanAuthError,
    UrlscanConnectionError,
    UrlscanRateLimitError,
    UrlscanRequestError,
    UrlscanScanDeniedError,
)
from urlscan.models import (
    LookupScanOutput,
    ScanLists,
    ScanPage,
    ScanStats,
    ScanTask,
    ScanVerdict,
    ScanVerdicts,
    SearchOutput,
    SearchResultEntry,
    SubmitScanOutput,
)

DEFAULT_TIMEOUT_SECONDS = 20.0
WEB_BASE = "https://urlscan.io/result/"


# ---------- helpers ----------


def _verdict_from(raw: dict[str, Any] | None) -> ScanVerdict | None:
    if not isinstance(raw, dict):
        return None
    return ScanVerdict(
        score=raw.get("score"),
        malicious=raw.get("malicious"),
        categories=list(raw.get("categories") or []),
        tags=list(raw.get("tags") or []),
        brands=list(raw.get("brands") or []),
    )


def _verdicts_from(raw: dict[str, Any] | None) -> ScanVerdicts | None:
    if not isinstance(raw, dict):
        return None
    return ScanVerdicts(
        overall=_verdict_from(raw.get("overall")),
        urlscan=_verdict_from(raw.get("urlscan")),
        community=_verdict_from(raw.get("community")),
        engines=_verdict_from(raw.get("engines")),
    )


def _task_from(raw: dict[str, Any] | None) -> ScanTask:
    if not isinstance(raw, dict):
        return ScanTask()
    return ScanTask(
        uuid=raw.get("uuid"),
        url=raw.get("url"),
        time=raw.get("time"),
        source=raw.get("source"),
        visibility=raw.get("visibility"),
        tags=list(raw.get("tags") or []),
    )


def _page_from(raw: dict[str, Any] | None) -> ScanPage:
    if not isinstance(raw, dict):
        return ScanPage()
    return ScanPage.model_validate(raw)


def _stats_from(raw: dict[str, Any] | None) -> ScanStats | None:
    if not isinstance(raw, dict):
        return None
    return ScanStats.model_validate(raw)


def _lists_from(raw: dict[str, Any] | None) -> ScanLists:
    """Build ScanLists from urlscan's `lists` block. URLs intentionally
    dropped (too noisy)."""
    if not isinstance(raw, dict):
        return ScanLists()
    return ScanLists(
        ips=list(raw.get("ips") or []),
        domains=list(raw.get("domains") or []),
        asns=[str(a) for a in (raw.get("asns") or [])],
        countries=list(raw.get("countries") or []),
        servers=list(raw.get("servers") or []),
        hashes=list(raw.get("hashes") or []),
    )


# ---------- client ----------


class UrlscanClient:
    """Synchronous urlscan.io v1 client.

    Closes its httpx.Client on .close() / __exit__.
    """

    def __init__(self, config: UrlscanConfig, timeout: float = DEFAULT_TIMEOUT_SECONDS) -> None:
        self._config = config
        self._base_url = str(config.urlscan_api_base_url).rstrip("/") + "/"
        api_key = config.urlscan_api_key.get_secret_value()
        self._client = httpx.Client(
            timeout=timeout,
            headers={
                "API-Key": api_key,
                "Accept": "application/json",
                "User-Agent": "ArchimedesUrlscan/0.1",
            },
        )

    def __enter__(self) -> UrlscanClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    # ---------- transport ----------

    def _get(self, path: str, params: dict[str, Any] | None = None) -> tuple[int, dict[str, Any] | None]:
        """GET against urlscan. Returns (status, body). 404 => (404, None).

        Raises Urlscan*Error for transport, auth, rate limit, and other
        4xx/5xx outcomes.
        """
        url = urljoin(self._base_url, path)
        try:
            resp = self._client.get(url, params=params)
        except httpx.ConnectError as e:
            raise UrlscanConnectionError(f"Could not connect to {self._base_url}: {e}") from e
        except httpx.TimeoutException as e:
            raise UrlscanConnectionError(f"urlscan request timed out: {e}") from e
        except httpx.RequestError as e:
            raise UrlscanConnectionError(f"urlscan request failed: {e}") from e

        return self._handle_response(resp)

    def _post(self, path: str, payload: dict[str, Any]) -> tuple[int, dict[str, Any] | None]:
        url = urljoin(self._base_url, path)
        try:
            resp = self._client.post(url, json=payload)
        except httpx.ConnectError as e:
            raise UrlscanConnectionError(f"Could not connect to {self._base_url}: {e}") from e
        except httpx.TimeoutException as e:
            raise UrlscanConnectionError(f"urlscan request timed out: {e}") from e
        except httpx.RequestError as e:
            raise UrlscanConnectionError(f"urlscan request failed: {e}") from e

        return self._handle_response(resp)

    def _handle_response(self, resp: httpx.Response) -> tuple[int, dict[str, Any] | None]:
        """Map HTTP status to either parsed body, None (404), or raised error."""
        if resp.status_code == 404:
            return (404, None)
        if resp.status_code == 429:
            retry_after = resp.headers.get("Retry-After")
            raise UrlscanRateLimitError(
                f"urlscan rate-limited (Retry-After: {retry_after}); free-tier "
                "search allows ~1 req/sec, scans 5,000/month"
            )
        if resp.status_code in (401, 403):
            raise UrlscanAuthError(
                f"urlscan rejected the API key ({resp.status_code}): {resp.text[:200]}"
            )
        if resp.status_code >= 500:
            raise UrlscanConnectionError(
                f"urlscan server error {resp.status_code}: {resp.text[:200]}"
            )
        if resp.status_code >= 400:
            # Submit-scan denials surface as 400 with specific message
            text = resp.text[:300]
            if "denied" in text.lower() or "denylist" in text.lower():
                raise UrlscanScanDeniedError(
                    f"urlscan denied the scan ({resp.status_code}): {text}"
                )
            raise UrlscanRequestError(
                f"urlscan rejected request ({resp.status_code}): {text}"
            )

        if not resp.content:
            return (resp.status_code, None)
        try:
            return (resp.status_code, resp.json())
        except ValueError:
            raise UrlscanRequestError(
                f"urlscan returned non-JSON (status {resp.status_code}): {resp.text[:200]}"
            )

    # ---------- search ----------

    def search(self, query: str, size: int = 10) -> SearchOutput:
        params = {"q": query, "size": str(size)}
        status, body = self._get("search/", params=params)
        if body is None:
            return SearchOutput(total=0, returned=0, has_more=False)

        results_raw = body.get("results") or []
        entries: list[SearchResultEntry] = []
        for r in results_raw:
            if not isinstance(r, dict):
                continue
            uuid = r.get("_id") or (r.get("task") or {}).get("uuid")
            if not uuid:
                continue
            entries.append(
                SearchResultEntry(
                    uuid=uuid,
                    task=_task_from(r.get("task")),
                    page=_page_from(r.get("page")),
                    stats=_stats_from(r.get("stats")),
                    verdicts=_verdicts_from(r.get("verdicts")),
                    result_url=r.get("result"),
                    screenshot_url=r.get("screenshot"),
                )
            )

        return SearchOutput(
            total=int(body.get("total", 0) or 0),
            returned=len(entries),
            has_more=bool(body.get("has_more", False)),
            took_ms=body.get("took"),
            results=entries,
        )

    # ---------- lookup_scan ----------

    def lookup_scan(self, uuid: str) -> LookupScanOutput:
        clean = uuid.strip()
        status, body = self._get(f"result/{clean}/")
        if body is None:
            return LookupScanOutput(found=False, uuid=clean)

        return LookupScanOutput(
            found=True,
            uuid=clean,
            task=_task_from(body.get("task")),
            page=_page_from(body.get("page")),
            stats=_stats_from(body.get("stats")),
            verdicts=_verdicts_from(body.get("verdicts")),
            lists=_lists_from(body.get("lists")),
            screenshot_url=body.get("task", {}).get("screenshotURL")
            if isinstance(body.get("task"), dict)
            else None,
            result_url=urljoin(self._base_url, f"result/{clean}/"),
            web_url=f"{WEB_BASE}{clean}/",
        )

    # ---------- submit_scan ----------

    def submit_scan(
        self,
        url: str,
        visibility: str = "public",
        tags: list[str] | None = None,
        referer: str | None = None,
        user_agent: str | None = None,
    ) -> SubmitScanOutput:
        payload: dict[str, Any] = {
            "url": url.strip(),
            "visibility": visibility,
        }
        if tags:
            payload["tags"] = list(tags)
        if referer:
            payload["referer"] = referer
        if user_agent:
            payload["customagent"] = user_agent

        status, body = self._post("scan/", payload)
        if body is None:
            raise UrlscanRequestError(
                f"urlscan submit returned no body (status {status})"
            )

        uuid = body.get("uuid")
        if not uuid:
            raise UrlscanRequestError(
                f"urlscan submit response missing uuid: {body}"
            )

        return SubmitScanOutput(
            uuid=uuid,
            api_url=body.get("api") or urljoin(self._base_url, f"result/{uuid}/"),
            web_url=body.get("result") or f"{WEB_BASE}{uuid}/",
            visibility=body.get("visibility", visibility),
            message=body.get("message"),
        )
