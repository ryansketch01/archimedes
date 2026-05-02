"""Configuration loader for the Shodan MCP.

Same pattern as splunk-query and virustotal: find_dotenv walk-up,
pydantic-settings, named missing-key errors.

Two base URLs because Shodan's free InternetDB endpoint lives on a
separate subdomain from the paid v1 API.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, HttpUrl, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class ShodanConfig(BaseSettings):
    """Runtime configuration for the Shodan MCP."""

    model_config = SettingsConfigDict(
        env_file=None,
        case_sensitive=True,
        frozen=True,
        extra="ignore",
    )

    shodan_api_key: Annotated[SecretStr, Field(alias="SHODAN_API_KEY")]
    shodan_api_base_url: Annotated[HttpUrl, Field(alias="SHODAN_API_BASE_URL")] = HttpUrl(
        "https://api.shodan.io/"
    )
    shodan_internetdb_base_url: Annotated[HttpUrl, Field(alias="SHODAN_INTERNETDB_BASE_URL")] = HttpUrl(
        "https://internetdb.shodan.io/"
    )


def load_config() -> ShodanConfig:
    """Load and validate Shodan MCP config from the workspace .env."""
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        raise RuntimeError(
            "Could not find .env file. Expected at the Archimedes workspace root "
            f"(searching upward from {Path(__file__).resolve()})."
        )

    load_dotenv(env_path, override=False)

    try:
        return ShodanConfig()  # type: ignore[call-arg]
    except ValidationError as e:
        missing = [err["loc"][0] for err in e.errors() if err["type"] == "missing"]
        if missing:
            raise RuntimeError(
                f"Missing required environment variable(s) in {env_path}: "
                f"{', '.join(str(m) for m in missing)}"
            ) from e
        raise RuntimeError(f"Invalid Shodan MCP config in {env_path}: {e}") from e
