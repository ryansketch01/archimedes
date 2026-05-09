"""Domain exceptions for the urlscan MCP."""

from __future__ import annotations


class UrlscanClientError(Exception):
    """Base exception for all urlscan client errors."""


class UrlscanConnectionError(UrlscanClientError):
    """Raised when urlscan.io is unreachable or returns 5xx."""


class UrlscanAuthError(UrlscanClientError):
    """Raised when urlscan.io rejects the API key (401/403)."""


class UrlscanRateLimitError(UrlscanClientError):
    """Raised when urlscan.io returns 429.

    Free tier limits as of 2026-05: 5,000 public scans/month, search
    unlimited but rate-limited at ~1 req/sec. Caller should back off
    on this exception (do not mark the source stale on the first hit).
    """


class UrlscanRequestError(UrlscanClientError):
    """Raised when urlscan.io accepts the request but rejects it
    (other 4xx — bad query syntax, scan submission denied, etc.)."""


class UrlscanScanDeniedError(UrlscanClientError):
    """Raised on submit_scan when urlscan.io denies the scan request.

    Examples:
      - Domain blocked (some hostnames are on urlscan's denylist)
      - Visibility=public denied for scan-private-only accounts
      - Daily/monthly submit quota exhausted

    Surfaces as a distinct exception so callers can fall back to
    `search` (which doesn't consume submission quota).
    """
