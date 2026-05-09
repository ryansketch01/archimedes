"""Configuration loader for the theHarvester MCP.

Different from the REST-API MCPs in this workspace: theHarvester is a
CLI tool invoked via subprocess, not an HTTP service we authenticate
against. Configuration is operational:

  - THEHARVESTER_BIN — explicit path to the theHarvester executable.
    Optional; default is to trust PATH and use bare 'theHarvester'.
  - THEHARVESTER_TIMEOUT_SECONDS — per-invocation timeout. theHarvester
    can take 30-300+ seconds depending on selected sources and limit;
    default 600 (10 min) hard cap.
  - THEHARVESTER_DEFAULT_LIMIT — default per-source limit when caller
    doesn't supply one. theHarvester's own default is 500; we set 100
    so MCP defaults stay snappy.

Some theHarvester sources DO consume API keys (Shodan, VirusTotal,
Censys, SecurityTrails, etc.). theHarvester reads those from its own
~/.theHarvester/api-keys.yaml file at runtime; this MCP doesn't
forward them. If the operator wants those sources, they configure
api-keys.yaml separately. The default allowlist used by this MCP
sticks to no-key passive sources so it works on a fresh install.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class TheHarvesterConfig(BaseSettings):
    """Runtime configuration for the theHarvester MCP."""

    model_config = SettingsConfigDict(
        env_file=None,
        case_sensitive=True,
        frozen=True,
        extra="ignore",
    )

    theharvester_bin: Annotated[str, Field(alias="THEHARVESTER_BIN")] = "theHarvester"
    theharvester_timeout_seconds: Annotated[
        float, Field(alias="THEHARVESTER_TIMEOUT_SECONDS", gt=0, le=1800)
    ] = 600.0
    theharvester_default_limit: Annotated[
        int, Field(alias="THEHARVESTER_DEFAULT_LIMIT", gt=0, le=10000)
    ] = 100


def load_config() -> TheHarvesterConfig:
    """Load and validate the theHarvester MCP config from the workspace .env.

    Falls back to defaults if .env is absent — theHarvester needs no
    secrets at this MCP level (sources that need API keys are managed
    by theHarvester's own ~/.theHarvester/api-keys.yaml).
    """
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if env_path:
        load_dotenv(env_path, override=False)

    try:
        return TheHarvesterConfig()  # type: ignore[call-arg]
    except ValidationError as e:
        raise RuntimeError(
            f"Invalid theHarvester MCP config in {env_path or 'environment'}: {e}"
        ) from e
