"""Domain exceptions for the Censys MCP."""

from __future__ import annotations


class CensysClientError(Exception):
    """Base exception for all Censys client errors."""


class CensysConnectionError(CensysClientError):
    """Raised when Censys is unreachable or returns 5xx."""


class CensysAuthError(CensysClientError):
    """Raised when Censys rejects the API credentials (401/403)."""


class CensysRateLimitError(CensysClientError):
    """Raised when Censys returns 429.

    Free-tier limits as of 2026-05: ~100 search queries/month + ~250
    view (lookup) requests/month. Censys returns 429 on rate-limit
    AND on quota exhaustion; the message body distinguishes them but
    the operational response is the same — back off and surface to
    the operator.
    """


class CensysQuotaExhaustedError(CensysClientError):
    """Raised when Censys explicitly reports the monthly quota is
    exhausted. Distinct from RateLimitError so the operator can tell
    the difference between "too fast right now" and "no more this
    month."""


class CensysRequestError(CensysClientError):
    """Raised when Censys accepts the request but rejects it
    (other 4xx — bad query syntax, malformed IP, etc.)."""
