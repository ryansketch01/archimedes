"""SpiderFoot REST client (open-source SpiderFoot's CherryPy API).

SpiderFoot exposes a CherryPy-backed web UI on a single port (default
5001). The "API" is the same endpoints the UI calls — form-encoded
POSTs and query-string GETs returning JSON.

Endpoints used:

  GET  /ping                                 — liveness probe
  POST /startscan                            — kick off a scan
       form data: scanname, scantarget, modulelist, typelist, usecase
  GET  /scanstatus?id=<scan_id>              — scan status (JSON)
  GET  /scaneventresultexport?id=<id>&type=json&dialect=json
                                             — full results as JSON list
  GET  /scanlist                             — list scans (used as auth probe)

SpiderFoot's `--passwd <user>:<pass>` flag enables HTTP Basic on
every endpoint. Loopback-only deployments typically run without auth.

Scan lifecycle:
  CREATED → RUNNING → FINISHED | ABORTED | ERROR-FAILED

The MCP blocks until terminal state or until SPIDERFOOT_SCAN_TIMEOUT_SECONDS
elapses, then returns whatever SpiderFoot has so far.
"""

from __future__ import annotations

import time
from typing import Any
from urllib.parse import urljoin

import httpx

from spiderfoot_mcp.config import SpiderFootConfig
from spiderfoot_mcp.exceptions import (
    SpiderFootAuthError,
    SpiderFootConnectionError,
    SpiderFootRequestError,
    SpiderFootScanError,
    SpiderFootTimeoutError,
)
from spiderfoot_mcp.models import HealthOutput, PassiveScanOutput, ScanEvent

USER_AGENT = "ArchimedesSpiderFoot/0.1"

# SpiderFoot terminal scan statuses — anything else means the scan is
# still in progress (CREATED / RUNNING / STARTING / etc.).
TERMINAL_STATUSES: frozenset[str] = frozenset(
    {"FINISHED", "ABORTED", "ERROR-FAILED", "ABORT-REQUESTED"}
)

# SpiderFoot event types that carry domain-shaped data.
DOMAIN_EVENT_TYPES: frozenset[str] = frozenset(
    {"DOMAIN_NAME", "INTERNET_NAME", "AFFILIATE_DOMAIN_NAME", "AFFILIATE_INTERNET_NAME"}
)
IP_EVENT_TYPES: frozenset[str] = frozenset(
    {"IP_ADDRESS", "IPV6_ADDRESS", "AFFILIATE_IPADDR"}
)
EMAIL_EVENT_TYPES: frozenset[str] = frozenset(
    {"EMAILADDR", "AFFILIATE_EMAILADDR"}
)


class SpiderFootClient:
    """Synchronous SpiderFoot client.

    Closes its httpx.Client on .close() / __exit__.
    """

    def __init__(self, config: SpiderFootConfig) -> None:
        self._config = config
        self._base_url = str(config.spiderfoot_url).rstrip("/") + "/"

        auth: tuple[str, str] | None = None
        if config.spiderfoot_username and config.spiderfoot_password:
            auth = (
                config.spiderfoot_username,
                config.spiderfoot_password.get_secret_value(),
            )

        self._client = httpx.Client(
            timeout=config.spiderfoot_http_timeout_seconds,
            verify=config.spiderfoot_verify_ssl,
            auth=auth,
            headers={
                "Accept": "application/json",
                "User-Agent": USER_AGENT,
            },
        )

    def __enter__(self) -> SpiderFootClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    @property
    def base_url(self) -> str:
        return self._base_url

    # ---------- transport ----------

    def _get(
        self, path: str, params: dict[str, Any] | None = None
    ) -> tuple[int, str, dict[str, Any] | list[Any] | None]:
        url = urljoin(self._base_url, path)
        try:
            resp = self._client.get(url, params=params)
        except httpx.ConnectError as e:
            raise SpiderFootConnectionError(
                f"Could not connect to SpiderFoot at {self._base_url}: {e}"
            ) from e
        except httpx.TimeoutException as e:
            raise SpiderFootConnectionError(
                f"SpiderFoot request timed out: {e}"
            ) from e
        except httpx.RequestError as e:
            raise SpiderFootConnectionError(
                f"SpiderFoot request failed: {e}"
            ) from e
        return self._handle_response(resp)

    def _post(
        self, path: str, data: dict[str, Any]
    ) -> tuple[int, str, dict[str, Any] | list[Any] | None]:
        url = urljoin(self._base_url, path)
        try:
            resp = self._client.post(url, data=data)
        except httpx.ConnectError as e:
            raise SpiderFootConnectionError(
                f"Could not connect to SpiderFoot at {self._base_url}: {e}"
            ) from e
        except httpx.TimeoutException as e:
            raise SpiderFootConnectionError(
                f"SpiderFoot request timed out: {e}"
            ) from e
        except httpx.RequestError as e:
            raise SpiderFootConnectionError(
                f"SpiderFoot request failed: {e}"
            ) from e
        return self._handle_response(resp)

    def _handle_response(
        self, resp: httpx.Response
    ) -> tuple[int, str, dict[str, Any] | list[Any] | None]:
        """Map status to (status, raw_text, parsed_body_or_None).

        SpiderFoot returns JSON for most endpoints but plain text /
        HTML for a few (e.g., /ping returns the literal string 'pong').
        Caller decides which form is expected.
        """
        if resp.status_code in (401, 403):
            raise SpiderFootAuthError(
                f"SpiderFoot rejected credentials ({resp.status_code}). "
                "Check SPIDERFOOT_USERNAME / SPIDERFOOT_PASSWORD against "
                "SpiderFoot's `--passwd <user>:<pass>` value, or restart "
                "SpiderFoot without --passwd if loopback-only is acceptable."
            )
        if resp.status_code >= 500:
            raise SpiderFootConnectionError(
                f"SpiderFoot server error {resp.status_code}: {resp.text[:200]}"
            )
        if resp.status_code >= 400:
            raise SpiderFootRequestError(
                f"SpiderFoot rejected request ({resp.status_code}): {resp.text[:300]}"
            )

        text = resp.text
        if not text:
            return (resp.status_code, "", None)

        # Try JSON parse; fall through to text-only when the endpoint
        # legitimately returns non-JSON (e.g., /ping → "pong").
        try:
            return (resp.status_code, text, resp.json())
        except ValueError:
            return (resp.status_code, text, None)

    # ---------- health ----------

    def health(self) -> HealthOutput:
        """Reachability + auth probe.

        Strategy:
          1. GET /ping — should return 'pong'. If it 401/403s, that
             tells us the daemon is up but we lack creds.
          2. If /ping is OK and auth is configured, hit /scanlist
             which always requires auth when --passwd is set, to
             confirm the creds work.
          3. If /ping isn't available (older builds), GET /scanlist
             directly and treat 200 as a confirmation.
        """
        ping_body: Any = None
        try:
            status, text, ping_body = self._get("ping")
        except SpiderFootAuthError as e:
            return HealthOutput(
                reachable=True,
                authenticated=False,
                url=self._base_url,
                message=str(e),
            )
        except SpiderFootConnectionError as e:
            return HealthOutput(
                reachable=False,
                authenticated=None,
                url=self._base_url,
                message=str(e),
            )
        except SpiderFootRequestError:
            # 4xx on /ping (typically 404 — endpoint missing on this build).
            # Don't bubble — fall through to the /scanlist fallback below
            # by setting status/text to non-OK values.
            status, text = 404, ""

        # /ping shapes seen in the wild:
        #   - SpiderFoot 4.0.0:    JSON list ["SUCCESS", "<version>"]
        #   - Older / forks:       plain text "pong"
        #   - Some builds:         JSON dict {"version": "..."}
        version: str | None = None
        ping_ok = False
        if status == 200:
            if isinstance(ping_body, list) and len(ping_body) >= 1:
                if str(ping_body[0]).upper() == "SUCCESS":
                    ping_ok = True
                    if len(ping_body) >= 2:
                        version = str(ping_body[1])
            elif isinstance(ping_body, dict):
                # Best-effort version extraction
                version = ping_body.get("version") or ping_body.get("spiderfoot_version")
                if version is not None:
                    ping_ok = True
                    version = str(version)
            elif text.strip().lower() == "pong" or "pong" in text.strip().lower():
                ping_ok = True

        # If /ping wasn't recognized, fall through to /scanlist as the
        # secondary reachability check (and an auth check if creds are
        # configured).
        if not ping_ok:
            try:
                status2, _text2, body2 = self._get("scanlist")
            except SpiderFootAuthError as e:
                return HealthOutput(
                    reachable=True,
                    authenticated=False,
                    url=self._base_url,
                    message=str(e),
                )
            except SpiderFootConnectionError as e:
                return HealthOutput(
                    reachable=False,
                    authenticated=None,
                    url=self._base_url,
                    message=str(e),
                )
            if status2 == 200:
                return HealthOutput(
                    reachable=True,
                    authenticated=self._has_auth() or None,
                    spiderfoot_version=version,
                    url=self._base_url,
                    message="OK (via /scanlist; /ping not available)",
                )
            return HealthOutput(
                reachable=True,
                authenticated=None,
                url=self._base_url,
                message=f"/ping returned status {status} body={text[:80]!r}",
            )

        # Auth probe — only meaningful when creds are configured.
        if self._has_auth():
            try:
                status2, _text2, _body2 = self._get("scanlist")
            except SpiderFootAuthError as e:
                return HealthOutput(
                    reachable=True,
                    authenticated=False,
                    url=self._base_url,
                    message=str(e),
                )
            authenticated: bool | None = status2 == 200
        else:
            authenticated = None

        return HealthOutput(
            reachable=True,
            authenticated=authenticated,
            spiderfoot_version=version,
            url=self._base_url,
            message="OK",
        )

    def _has_auth(self) -> bool:
        return bool(
            self._config.spiderfoot_username and self._config.spiderfoot_password
        )

    # ---------- scan lifecycle ----------

    def start_scan(
        self,
        target: str,
        modules: list[str],
        scan_name: str,
        target_type: str | None = None,
        usecase: str = "Passive",
    ) -> str:
        """Kick off a scan; return the scan_id.

        SpiderFoot's /startscan accepts:
          scanname:   human-readable name
          scantarget: the target string
          modulelist: comma-separated, prefixed with `module_` per
                      SpiderFoot convention (e.g., 'module_sfp_crt,module_sfp_whois')
          typelist:   alternative to modulelist — comma-separated event
                      types (we use modulelist instead, which is more precise)
          usecase:    'Passive' / 'Footprint' / 'Investigate' / 'All'.
                      We default to 'Passive' as a belt-and-suspenders
                      safeguard alongside the module allowlist.

        Response shape varies across SpiderFoot versions. Modern
        builds redirect to a results page with the scan ID in the
        URL. The CherryPy JSON endpoints (when present) return
        ['SUCCESS', '<scan_id>'] or {'id': '<scan_id>', ...}.
        """
        if target_type:
            # SpiderFoot's /startscan doesn't accept an explicit
            # target_type — it infers from the value. We accept the
            # arg for forward-compat / clarity but ignore it on the
            # wire. (Modern SpiderFoot HX has typed targets; the OSS
            # API does not.)
            pass

        modulelist = ",".join(f"module_{m}" if not m.startswith("module_") else m for m in modules)

        form = {
            "scanname": scan_name,
            "scantarget": target,
            "modulelist": modulelist,
            "typelist": "",
            "usecase": usecase,
        }
        status, text, body = self._post("startscan", form)

        # Several response shapes seen across SpiderFoot versions:
        #   1. ['SUCCESS', '<scan_id>']
        #   2. {'id': '<scan_id>'}
        #   3. {'status': 'SUCCESS', 'id': '<scan_id>'}
        #   4. HTML redirect with scan_id in a Location header
        if isinstance(body, list) and len(body) >= 2 and str(body[0]).upper() == "SUCCESS":
            return str(body[1])
        if isinstance(body, dict):
            scan_id = body.get("id") or body.get("scan_id") or body.get("scanId")
            if scan_id:
                return str(scan_id)

        # Last-resort: probe scanlist for the freshest scan with our
        # exact name. Robust across response-shape changes.
        try:
            _status, _text, listing = self._get("scanlist")
        except SpiderFootError:
            listing = None

        if isinstance(listing, list):
            for row in listing:
                # /scanlist rows are typically [id, name, target, started, ended, status, totalevents]
                if isinstance(row, (list, tuple)) and len(row) >= 2 and row[1] == scan_name:
                    return str(row[0])

        raise SpiderFootScanError(
            f"Could not extract scan_id from /startscan response. "
            f"status={status} body_type={type(body).__name__} text={text[:200]!r}"
        )

    def get_scan_status(self, scan_id: str) -> dict[str, Any]:
        """Return the SpiderFoot status payload for a scan.

        SpiderFoot 4.0.0 returns a 7-element positional list:
          [name, target, created, started, ended, status, riskmatrix]
        where `status` is the literal "FINISHED" / "RUNNING" / etc.
        and `riskmatrix` is {"HIGH": int, "MEDIUM": int, "LOW": int, "INFO": int}.

        Some forks / older builds return shorter positional lists or
        dict-shaped payloads; we accept all three.
        """
        status, _text, body = self._get("scanstatus", params={"id": scan_id})

        if isinstance(body, dict):
            return body

        if isinstance(body, list):
            # SpiderFoot 4.0.0 shape: [name, target, created, started, ended, status, riskmatrix]
            if len(body) >= 7:
                return {
                    "id": scan_id,
                    "name": body[0],
                    "target": body[1],
                    "created": body[2],
                    "started": body[3],
                    "ended": body[4],
                    "status": body[5],
                    "riskmatrix": body[6] if len(body) > 6 else None,
                }
            # Older fallback: [name, target, started, ended, status, events_count]
            if len(body) >= 6:
                return {
                    "id": scan_id,
                    "name": body[0],
                    "target": body[1],
                    "started": body[2],
                    "ended": body[3],
                    "status": body[4],
                    "events_count": body[5],
                }
            # /scanstatus returns [] when the scan_id is unknown
            if not body:
                raise SpiderFootRequestError(
                    f"SpiderFoot has no record of scan {scan_id}. "
                    "Most likely the scan_id is wrong or the scan was deleted."
                )

        raise SpiderFootRequestError(
            f"Unexpected /scanstatus response shape: status={status} body={body!r}"
        )

    def export_results(self, scan_id: str) -> list[dict[str, Any]]:
        """Pull all events for a scan as a normalized list of dicts.

        Endpoint: `/scaneventresults?id=<scan_id>&eventType=ALL`. Note
        this is NOT the same as `/scaneventresultexport`, which is the
        CSV/Excel download endpoint and does NOT support JSON output
        in SpiderFoot 4.0.0 (it 200s with HTML "Error" instead).

        SpiderFoot 4.0.0 returns each event as an 11-element list:
          [0] last_seen (formatted timestamp)
          [1] data (the value)
          [2] source data (upstream event's data — usually the target)
          [3] source module (e.g., 'sfp_dnsresolve' or 'SpiderFoot UI'
              for the seed events; '' for ROOT)
          [4] confidence (0-100)
          [5] visibility (0-100)
          [6] risk (0=info, ...)
          [7] hash id
          [8] false_positive (0/1)
          [9] reserved
          [10] event type (e.g., 'IP_ADDRESS', 'DOMAIN_NAME', 'ROOT')

        We normalize each row to the shape `_normalize_events` expects
        (keys: type, data, module, source, generated, fp).
        """
        params = {"id": scan_id, "eventType": "ALL"}
        status, _text, body = self._get("scaneventresults", params=params)

        if body is None:
            return []

        rows: list[Any]
        if isinstance(body, list):
            rows = body
        elif isinstance(body, dict) and isinstance(body.get("events"), list):
            rows = body["events"]
        else:
            raise SpiderFootRequestError(
                f"Unexpected /scaneventresults shape: status={status} "
                f"type={type(body).__name__}"
            )

        normalized: list[dict[str, Any]] = []
        for r in rows:
            if isinstance(r, dict):
                # Fork that already returns dict-shaped rows
                normalized.append(r)
                continue
            if not isinstance(r, list) or len(r) < 11:
                continue
            event_type = str(r[10]) if r[10] is not None else ""
            # Skip ROOT pseudo-events — they're SpiderFoot's record of the
            # target itself and aren't useful intel.
            if event_type == "ROOT":
                continue
            normalized.append({
                "generated": r[0],
                "data": r[1],
                "source": r[2],
                "module": r[3],
                "fp": r[8],
                "type": event_type,
            })
        return normalized

    # ---------- orchestration ----------

    def run_passive_scan(
        self,
        target: str,
        modules: list[str],
        scan_name: str,
        target_type: str | None = None,
    ) -> PassiveScanOutput:
        """Start scan, poll until terminal or timeout, return aggregated output.

        On timeout we return whatever SpiderFoot has emitted so far
        with status='RUNNING-TIMEOUT' and the scan_id so the operator
        can revisit via the web UI. We do NOT raise — partial results
        are useful intel.
        """
        start = time.monotonic()
        scan_id = self.start_scan(
            target=target,
            modules=modules,
            scan_name=scan_name,
            target_type=target_type,
            usecase="Passive",
        )

        deadline = start + self._config.spiderfoot_scan_timeout_seconds
        poll = self._config.spiderfoot_poll_interval_seconds
        last_status = "STARTED"

        while time.monotonic() < deadline:
            status_payload = self.get_scan_status(scan_id)
            last_status = str(status_payload.get("status", "UNKNOWN")).upper()
            if last_status in TERMINAL_STATUSES:
                break
            time.sleep(poll)
        else:
            # Polling loop exited via deadline, not break — partial results
            last_status = f"RUNNING-TIMEOUT-{last_status}"

        duration = time.monotonic() - start
        events_raw = self.export_results(scan_id)
        events = _normalize_events(events_raw)

        domains = _distinct(
            ev.data for ev in events if ev.event_type in DOMAIN_EVENT_TYPES
        )
        ips = _distinct(
            ev.data for ev in events if ev.event_type in IP_EVENT_TYPES
        )
        emails = _distinct(
            ev.data for ev in events if ev.event_type in EMAIL_EVENT_TYPES
        )

        if last_status.startswith("RUNNING-TIMEOUT"):
            # Surface as a soft signal: not raising, but the caller's
            # status field clearly says we timed out.
            pass

        web_url = urljoin(self._base_url, f"scaninfo?id={scan_id}")

        return PassiveScanOutput(
            scan_id=scan_id,
            name=scan_name,
            target=target,
            target_type=target_type,
            status=last_status,
            modules_used=list(modules),
            duration_seconds=round(duration, 2),
            events=events,
            distinct_domains=domains,
            distinct_ips=ips,
            distinct_emails=emails,
            web_url=web_url,
        )

    def run_passive_scan_or_raise(
        self,
        target: str,
        modules: list[str],
        scan_name: str,
        target_type: str | None = None,
    ) -> PassiveScanOutput:
        """Variant that raises SpiderFootTimeoutError on incomplete scans
        instead of returning partial data. Currently unused by the MCP
        tool surface — kept for callers that prefer fail-fast semantics."""
        out = self.run_passive_scan(
            target=target,
            modules=modules,
            scan_name=scan_name,
            target_type=target_type,
        )
        if out.status.startswith("RUNNING-TIMEOUT"):
            raise SpiderFootTimeoutError(
                f"SpiderFoot scan {out.scan_id} did not finish within "
                f"{self._config.spiderfoot_scan_timeout_seconds}s. Partial "
                f"results: {len(out.events)} events. Revisit via {out.web_url}.",
                scan_id=out.scan_id,
            )
        return out


# ---------- helpers ----------


def _normalize_events(raw: list[dict[str, Any]]) -> list[ScanEvent]:
    """Map SpiderFoot's event records to ScanEvent.

    SpiderFoot's export shape varies slightly. Common keys:
      type, data, module, source, generated, source_data, fp.
    Confidence (`fp`) is a 0-100 score in some versions, missing in
    others. We're tolerant.
    """
    out: list[ScanEvent] = []
    for r in raw:
        event_type = r.get("type") or r.get("event_type")
        data = r.get("data")
        module = r.get("module") or r.get("source_module")
        if not event_type or data is None or not module:
            continue
        out.append(
            ScanEvent(
                event_type=str(event_type),
                data=str(data),
                source_module=str(module),
                source_event_type=(
                    str(r["source"]) if r.get("source") is not None else None
                ),
                timestamp=(
                    str(r["generated"]) if r.get("generated") is not None else None
                ),
                confidence=(
                    int(r["fp"]) if isinstance(r.get("fp"), (int, float)) else None
                ),
            )
        )
    return out


def _distinct(items) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for raw in items:
        s = str(raw).strip()
        if not s or s in seen:
            continue
        seen.add(s)
        out.append(s)
    return out
