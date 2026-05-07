"""Configuration loader for the RSS Bridge MCP.

Same pattern as splunk-query, virustotal, shodan-mcp: find_dotenv walk-up,
pydantic-settings, named missing-key errors.

Unlike the other MCPs, RSS doesn't need an API key — RSS/Atom feeds are
public. Configuration is purely operational: user agent, default timeout,
max items per fetch.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


# Default User-Agent. Some RSS hosts (notably CISA) block default httpx UA;
# identifying as a CTI consumer with a contact URL is more polite and less
# likely to trip WAFs than "python-httpx/0.28.1".
DEFAULT_USER_AGENT = (
    "Archimedes-CTI-Collector/0.1 "
    "(+https://github.com/ryansketch01/archimedes)"
)


class RssBridgeConfig(BaseSettings):
    """Runtime configuration for the RSS Bridge MCP."""

    model_config = SettingsConfigDict(
        env_file=None,
        case_sensitive=True,
        frozen=True,
        extra="ignore",
    )

    # All settings are optional with sensible defaults; the MCP works with
    # zero env vars set. Override only when needed.
    rss_bridge_user_agent: Annotated[str, Field(alias="RSS_BRIDGE_USER_AGENT")] = (
        DEFAULT_USER_AGENT
    )
    rss_bridge_timeout_seconds: Annotated[float, Field(alias="RSS_BRIDGE_TIMEOUT_SECONDS", gt=0)] = 30.0
    rss_bridge_max_items_default: Annotated[int, Field(alias="RSS_BRIDGE_MAX_ITEMS_DEFAULT", gt=0, le=500)] = 50


def load_config() -> RssBridgeConfig:
    """Load and validate RSS Bridge MCP config from the workspace .env."""
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        # RSS doesn't strictly need .env, but keep the same loader contract
        # as the other MCPs so behavior is uniform across the workspace.
        # Fall back to a defaulted config if no .env is found rather than
        # erroring — feeds are public.
        try:
            return RssBridgeConfig()  # type: ignore[call-arg]
        except ValidationError as e:
            raise RuntimeError(f"Invalid RSS Bridge MCP defaults: {e}") from e

    load_dotenv(env_path, override=False)

    try:
        return RssBridgeConfig()  # type: ignore[call-arg]
    except ValidationError as e:
        raise RuntimeError(f"Invalid RSS Bridge MCP config in {env_path}: {e}") from e
