"""Domain exceptions for the VirusTotal MCP."""

from __future__ import annotations


class VTClientError(Exception):
    """Base exception for all VirusTotal client errors."""


class VTConnectionError(VTClientError):
    """Raised when the VirusTotal endpoint is unreachable or returns a 5xx."""


class VTAuthError(VTClientError):
    """Raised when VirusTotal rejects the API key (401/403)."""


class VTRateLimitError(VTClientError):
    """Raised when VirusTotal returns 429 (free-tier: 4/min, 500/day)."""


class VTRequestError(VTClientError):
    """Raised when VirusTotal accepts the request but rejects it (4xx other than 401/403/404/429)."""
