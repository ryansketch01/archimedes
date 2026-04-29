"""Pydantic models for Splunk-query MCP tool inputs and outputs.

These define the contract between MCP clients (Claude Code, the inspector,
subagents) and our tools. Inputs are validated by the SDK before the tool
runs; outputs are serialized as JSON.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

# ---------- search tool ----------


class SearchInput(BaseModel):
    """Input for the search tool."""

    spl: str = Field(
        ...,
        description=(
            "SPL query. The 'search ' prefix is added automatically if absent. "
            "Generating commands starting with '|' (e.g. '| metadata', '| tstats') "
            "are passed through unchanged."
        ),
        min_length=1,
    )
    earliest: str = Field(
        default="-24h@h",
        description=(
            "Earliest time bound as a Splunk time modifier. Examples: "
            "'-24h@h' (last 24h, snapped to hour), '-7d', '-30d@d', '0' (epoch). "
            "Defaults to last 24h."
        ),
    )
    latest: str = Field(
        default="now",
        description="Latest time bound. Examples: 'now', '-1h', '@d' (start of today).",
    )
    max_results: int = Field(
        default=100,
        ge=1,
        le=10_000,
        description=(
            "Maximum number of events to return. Hard cap of 10,000 to protect "
            "Splunk Free's 500MB/day license."
        ),
    )


class SearchOutput(BaseModel):
    """Output for the search tool."""

    event_count: int = Field(..., description="Number of events returned.")
    events: list[dict[str, Any]] = Field(
        ..., description="Splunk events as dicts. Includes _time, _raw, host, sourcetype, etc."
    )
    spl_executed: str = Field(..., description="The SPL actually sent to Splunk after normalization.")
    earliest: str = Field(..., description="Earliest time bound used.")
    latest: str = Field(..., description="Latest time bound used.")


# ---------- health tool ----------


class HealthInput(BaseModel):
    """Input for the health tool. Takes no arguments."""


class HealthOutput(BaseModel):
    """Output for the health tool."""

    reachable: bool = Field(..., description="Whether Splunk responded successfully.")
    version: str | None = Field(default=None, description="Splunk version string, e.g. '10.2.2'.")
    build: str | None = Field(default=None, description="Splunk build hash.")
    server_name: str | None = Field(default=None, description="Splunk's configured server name.")
    license_state: str | None = Field(
        default=None,
        description="License state: OK, EXPIRED, VIOLATION, TRIAL, etc.",
    )
    os_name: str | None = Field(default=None, description="Host OS name.")
    note: str | None = Field(
        default=None,
        description=(
            "Operational note. WARNING: On Splunk Free, /services/server/info "
            "is unauthenticated by design — a successful health check confirms "
            "Splunk is reachable but does NOT validate credentials."
        ),
    )