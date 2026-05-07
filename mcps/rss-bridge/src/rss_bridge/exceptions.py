"""Domain exceptions for the RSS Bridge MCP."""

from __future__ import annotations


class RssBridgeClientError(Exception):
    """Base exception for all RSS Bridge client errors."""


class RssBridgeConnectionError(RssBridgeClientError):
    """Raised when the feed host is unreachable or returns 5xx."""


class RssBridgeRateLimitError(RssBridgeClientError):
    """Raised when the feed host returns 429."""


class RssBridgeRequestError(RssBridgeClientError):
    """Raised when the host accepts the request but rejects it (4xx other than 404/429)."""


class RssBridgeParseError(RssBridgeClientError):
    """Raised when the response could not be parsed as RSS/Atom.

    The fetch itself succeeded (2xx, valid HTTP body), but the body is not
    a valid feed — could be HTML, XML in an unsupported schema, garbled
    bytes, or an empty document. Distinct from connection/auth errors so
    callers can mark the source for human review rather than back-off.
    """
