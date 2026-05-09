"""Domain exceptions for the SpiderFoot MCP."""

from __future__ import annotations


class SpiderFootError(Exception):
    """Base exception for all SpiderFoot MCP errors."""


class SpiderFootConnectionError(SpiderFootError):
    """Raised when the SpiderFoot daemon is unreachable or returns 5xx.

    Most likely causes:
      - SpiderFoot isn't running (check `sf.py` process / docker container)
      - SPIDERFOOT_URL points at the wrong host/port
      - Firewall is blocking the management port
      - Self-signed cert + SPIDERFOOT_VERIFY_SSL=true (set False on LAN)
    """


class SpiderFootAuthError(SpiderFootError):
    """Raised when SpiderFoot rejects the HTTP Basic credentials (401/403).

    SpiderFoot's `--passwd <user>:<pass>` flag enables auth on the
    management interface. If you're seeing this, either:
      - Set SPIDERFOOT_USERNAME / SPIDERFOOT_PASSWORD in .env, or
      - Restart SpiderFoot without `--passwd` (loopback-only deployments).
    """


class SpiderFootRequestError(SpiderFootError):
    """Raised when SpiderFoot accepts the request but rejects it (other 4xx
    or unexpected response shape)."""


class SpiderFootPolicyError(SpiderFootError):
    """Raised when caller specifies a module not on the passive allowlist.

    Hard Rule 4 (no scanning third parties) and LEGAL-POLICY's
    SpiderFoot passive-only section are non-negotiable. The MCP refuses
    active modules at the input boundary regardless of caller. If the
    operator genuinely needs an active module against an authorized
    target (target in `infrastructure/authorized-targets.yaml`), they
    must drive SpiderFoot directly, outside this MCP.
    """


class SpiderFootScanError(SpiderFootError):
    """Raised when a scan starts but errors out, fails to complete, or
    returns no results before the timeout."""


class SpiderFootTimeoutError(SpiderFootError):
    """Raised when a scan exceeds SPIDERFOOT_SCAN_TIMEOUT_SECONDS without
    reaching a terminal state (FINISHED / ABORTED / ERROR-FAILED).

    SpiderFoot keeps scanning in the background even after we stop
    polling — the operator can revisit the scan via SpiderFoot's web
    UI using the scan_id returned in the timeout exception payload.
    """

    def __init__(self, message: str, scan_id: str | None = None) -> None:
        super().__init__(message)
        self.scan_id = scan_id
