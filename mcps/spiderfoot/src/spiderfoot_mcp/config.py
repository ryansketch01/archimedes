"""Configuration loader for the SpiderFoot MCP.

Same pattern as urlscan/censys/virustotal: find_dotenv walk-up,
pydantic-settings, named missing-key errors.

Connects to a self-hosted SpiderFoot daemon. Auth is optional —
SpiderFoot's `--passwd` flag enables HTTP Basic on the web/API. If the
operator runs without auth (loopback only, default), leave the
USERNAME/PASSWORD vars unset.

SpiderFoot scans are async and can take minutes. The MCP blocks until
the scan finishes or the timeout hits, then returns aggregated
results. Tune timeout/poll-interval to taste; defaults are
conservative (10 minutes / 5 second poll) for the typical passive
module set.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from dotenv import find_dotenv, load_dotenv
from pydantic import Field, HttpUrl, SecretStr, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class SpiderFootConfig(BaseSettings):
    """Runtime configuration for the SpiderFoot MCP."""

    model_config = SettingsConfigDict(
        env_file=None,
        case_sensitive=True,
        frozen=True,
        extra="ignore",
    )

    # Required: base URL of the SpiderFoot daemon's web/API.
    spiderfoot_url: Annotated[HttpUrl, Field(alias="SPIDERFOOT_URL")]

    # Optional HTTP Basic auth — set both if SpiderFoot is started with
    # `--passwd <user>:<pass>`. Leave unset for unauthenticated loopback.
    spiderfoot_username: Annotated[str | None, Field(alias="SPIDERFOOT_USERNAME")] = None
    spiderfoot_password: Annotated[SecretStr | None, Field(alias="SPIDERFOOT_PASSWORD")] = None

    # Scan timeout — wall-clock seconds the MCP will wait before
    # giving up on a scan. SpiderFoot keeps scanning even if we stop
    # polling, so a timeout returns partial results, not an abort.
    spiderfoot_scan_timeout_seconds: Annotated[
        float, Field(alias="SPIDERFOOT_SCAN_TIMEOUT_SECONDS", gt=0)
    ] = 600.0

    # Poll interval while waiting for scan completion.
    spiderfoot_poll_interval_seconds: Annotated[
        float, Field(alias="SPIDERFOOT_POLL_INTERVAL_SECONDS", gt=0)
    ] = 5.0

    # Connect/read timeout for individual HTTP requests against the
    # SpiderFoot API (separate from scan completion timeout).
    spiderfoot_http_timeout_seconds: Annotated[
        float, Field(alias="SPIDERFOOT_HTTP_TIMEOUT_SECONDS", gt=0)
    ] = 30.0

    # Verify TLS for the SpiderFoot endpoint. Default True; set False
    # only when SpiderFoot is behind a self-signed cert on a trusted
    # network (e.g., localhost or LAN).
    spiderfoot_verify_ssl: Annotated[bool, Field(alias="SPIDERFOOT_VERIFY_SSL")] = True


def load_config() -> SpiderFootConfig:
    """Load and validate SpiderFoot MCP config from the workspace .env."""
    env_path = find_dotenv(usecwd=False, raise_error_if_not_found=False)
    if not env_path:
        raise RuntimeError(
            "Could not find .env file. Expected at the Archimedes workspace root "
            f"(searching upward from {Path(__file__).resolve()})."
        )

    load_dotenv(env_path, override=False)

    try:
        return SpiderFootConfig()  # type: ignore[call-arg]
    except ValidationError as e:
        missing = [err["loc"][0] for err in e.errors() if err["type"] == "missing"]
        if missing:
            raise RuntimeError(
                f"Missing required environment variable(s) in {env_path}: "
                f"{', '.join(str(m) for m in missing)}. "
                "Required: SPIDERFOOT_URL (e.g. http://localhost:5001). "
                "Optional: SPIDERFOOT_USERNAME, SPIDERFOOT_PASSWORD, "
                "SPIDERFOOT_SCAN_TIMEOUT_SECONDS, SPIDERFOOT_POLL_INTERVAL_SECONDS, "
                "SPIDERFOOT_HTTP_TIMEOUT_SECONDS, SPIDERFOOT_VERIFY_SSL."
            ) from e
        raise RuntimeError(f"Invalid SpiderFoot MCP config in {env_path}: {e}") from e
