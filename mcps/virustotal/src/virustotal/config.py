"""Configuration loader for the VirusTotal MCP.

Mirrors the splunk-query pattern: load .env via find_dotenv walk-up,
validate via pydantic-settings, fail loud with a named missing key.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, HttpUrl, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class VTConfig(BaseSettings):
    """Runtime configuration for the VirusTotal MCP.

    Only one secret (VT_API_KEY). Base URL is overridable for testing
    against a mock server but defaults to the public VirusTotal endpoint.
    """

    model_config = SettingsConfigDict(
        env_file=None,
        case_sensitive=True,
        frozen=True,
        extra="ignore",
    )

    vt_api_key: Annotated[SecretStr, Field(alias="VT_API_KEY")]
    vt_base_url: Annotated[HttpUrl, Field(alias="VT_BASE_URL")] = HttpUrl(
        "https://www.virustotal.com/api/v3/"
    )


def load_config() -> VTConfig:
    """Load and validate VT MCP config from the workspace .env."""
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        raise RuntimeError(
            "Could not find .env file. Expected at the Archimedes workspace root "
            f"(searching upward from {Path(__file__).resolve()})."
        )

    load_dotenv(env_path, override=False)

    try:
        return VTConfig()  # type: ignore[call-arg]
    except ValidationError as e:
        missing = [err["loc"][0] for err in e.errors() if err["type"] == "missing"]
        if missing:
            raise RuntimeError(
                f"Missing required environment variable(s) in {env_path}: "
                f"{', '.join(str(m) for m in missing)}"
            ) from e
        raise RuntimeError(f"Invalid VT MCP config in {env_path}: {e}") from e
