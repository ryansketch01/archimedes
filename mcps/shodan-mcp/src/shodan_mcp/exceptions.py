"""Domain exceptions for the Shodan MCP."""

from __future__ import annotations


class ShodanClientError(Exception):
    """Base exception for all Shodan client errors."""


class ShodanConnectionError(ShodanClientError):
    """Raised when the Shodan endpoint is unreachable or returns 5xx."""


class ShodanAuthError(ShodanClientError):
    """Raised when Shodan rejects the API key (401/403)."""


class ShodanRateLimitError(ShodanClientError):
    """Raised when Shodan returns 429 (1 req/sec on most plans)."""


class ShodanCreditError(ShodanClientError):
    """Raised when Shodan returns a credit-exhaustion error.

    Shodan signals this via 401 with a specific body (not just bad-key) or
    402, depending on endpoint. Surfaces separately so callers can fall
    back to InternetDB or count_hosts.
    """


class ShodanRequestError(ShodanClientError):
    """Raised when Shodan accepts the request but rejects it (other 4xx)."""
