"""Configuration loader for the Censys MCP.

Same pattern as splunk-query, virustotal, shodan-mcp, rss-bridge,
urlscan: find_dotenv walk-up, pydantic-settings, named missing-key
errors.

Authentication: HTTP Basic auth with API_ID as username and
API_SECRET as password. Empirically verified 2026-05-09: Censys's
v2 API rejects Personal Access Token (Bearer) auth with
"You must authenticate with a valid API ID and secret." even when
the PAT is otherwise valid. PATs may be for v3/GraphQL endpoints;
v2 host/cert search requires the legacy ID+SECRET pair. Both are
issued from https://search.censys.io/account/api — the API ID
section may be visually separate from the PAT section.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, HttpUrl, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class CensysConfig(BaseSettings):
    """Runtime configuration for the Censys MCP."""

    model_config = SettingsConfigDict(
        env_file=None,
        case_sensitive=True,
        frozen=True,
        extra="ignore",
    )

    censys_api_id: Annotated[SecretStr, Field(alias="CENSYS_API_ID")]
    censys_api_secret: Annotated[SecretStr, Field(alias="CENSYS_API_SECRET")]
    censys_api_base_url: Annotated[HttpUrl, Field(alias="CENSYS_API_BASE_URL")] = HttpUrl(
        "https://search.censys.io/api/"
    )


def load_config() -> CensysConfig:
    """Load and validate Censys MCP config from the workspace .env."""
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        raise RuntimeError(
            "Could not find .env file. Expected at the Archimedes workspace root "
            f"(searching upward from {Path(__file__).resolve()})."
        )

    load_dotenv(env_path, override=False)

    try:
        return CensysConfig()  # type: ignore[call-arg]
    except ValidationError as e:
        missing = [err["loc"][0] for err in e.errors() if err["type"] == "missing"]
        if missing:
            raise RuntimeError(
                f"Missing required environment variable(s) in {env_path}: "
                f"{', '.join(str(m) for m in missing)}"
            ) from e
        raise RuntimeError(f"Invalid Censys MCP config in {env_path}: {e}") from e
