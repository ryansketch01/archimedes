"""Configuration loader for the urlscan MCP.

Same pattern as splunk-query, virustotal, shodan-mcp, rss-bridge:
find_dotenv walk-up, pydantic-settings, named missing-key errors.

Authentication is per-request `API-Key` header. Free-tier limits at
v1 (verified 2026-05): 5,000 public scans/month + unlimited search.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, HttpUrl, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class UrlscanConfig(BaseSettings):
    """Runtime configuration for the urlscan MCP."""

    model_config = SettingsConfigDict(
        env_file=None,
        case_sensitive=True,
        frozen=True,
        extra="ignore",
    )

    urlscan_api_key: Annotated[SecretStr, Field(alias="URLSCAN_API_KEY")]
    urlscan_api_base_url: Annotated[HttpUrl, Field(alias="URLSCAN_API_BASE_URL")] = HttpUrl(
        "https://urlscan.io/api/v1/"
    )


def load_config() -> UrlscanConfig:
    """Load and validate urlscan MCP config from the workspace .env."""
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        raise RuntimeError(
            "Could not find .env file. Expected at the Archimedes workspace root "
            f"(searching upward from {Path(__file__).resolve()})."
        )

    load_dotenv(env_path, override=False)

    try:
        return UrlscanConfig()  # type: ignore[call-arg]
    except ValidationError as e:
        missing = [err["loc"][0] for err in e.errors() if err["type"] == "missing"]
        if missing:
            raise RuntimeError(
                f"Missing required environment variable(s) in {env_path}: "
                f"{', '.join(str(m) for m in missing)}"
            ) from e
        raise RuntimeError(f"Invalid urlscan MCP config in {env_path}: {e}") from e
