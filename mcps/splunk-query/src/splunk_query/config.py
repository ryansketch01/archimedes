"""Configuration loader for the Splunk-query MCP.

Loads required environment variables from the workspace .env file at startup,
validates them, and returns a frozen Pydantic model. Fails loud and early if
any required variable is missing or malformed.

Loaded once at process start. No per-request reads.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, HttpUrl, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class SplunkConfig(BaseSettings):
    """Runtime configuration for the Splunk-query MCP.

    All fields are required. Secrets are wrapped in SecretStr so they
    don't leak into logs, repr, or error messages.
    """

    model_config = SettingsConfigDict(
        env_file=None,           # We load .env explicitly via find_dotenv
        case_sensitive=True,
        frozen=True,
        extra="ignore",          # Ignore unrelated env vars (HEC creds, OSINT keys, etc.)
    )

    # Splunk REST API (read path)
    splunk_rest_url: Annotated[HttpUrl, Field(alias="SPLUNK_REST_URL")]
    splunk_rest_user: Annotated[str, Field(alias="SPLUNK_REST_USER", min_length=1)]
    splunk_rest_password: Annotated[SecretStr, Field(alias="SPLUNK_REST_PASSWORD")]
    splunk_rest_verify_ssl: Annotated[bool, Field(alias="SPLUNK_REST_VERIFY_SSL")]


def load_config() -> SplunkConfig:
    """Load and validate Splunk MCP config from the workspace .env.

    Walks up from the current file to find .env. Raises a clear error
    if .env is missing or any required key is absent.
    """
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        raise RuntimeError(
            "Could not find .env file. Expected at the Archimedes workspace root "
            f"(searching upward from {Path(__file__).resolve()})."
        )

    load_dotenv(env_path, override=False)

    try:
        return SplunkConfig()  # type: ignore[call-arg]
    except ValidationError as e:
        missing = [err["loc"][0] for err in e.errors() if err["type"] == "missing"]
        if missing:
            raise RuntimeError(
                f"Missing required environment variable(s) in {env_path}: "
                f"{', '.join(str(m) for m in missing)}"
            ) from e
        raise RuntimeError(f"Invalid Splunk MCP config in {env_path}: {e}") from e