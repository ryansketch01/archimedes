"""Domain exceptions for the Splunk-query MCP."""

from __future__ import annotations


class SplunkClientError(Exception):
    """Base exception for all Splunk client errors."""


class SplunkConnectionError(SplunkClientError):
    """Raised when the Splunk REST endpoint is unreachable."""


class SplunkAuthError(SplunkClientError):
    """Raised when Splunk rejects credentials (401)."""


class SplunkQueryError(SplunkClientError):
    """Raised when Splunk accepts the request but rejects the SPL or returns an error."""