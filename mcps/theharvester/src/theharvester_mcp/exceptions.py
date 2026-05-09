"""Domain exceptions for the theHarvester MCP."""

from __future__ import annotations


class TheHarvesterError(Exception):
    """Base exception for all theHarvester wrapper errors."""


class TheHarvesterNotInstalledError(TheHarvesterError):
    """Raised when the theHarvester executable can't be found.

    Either THEHARVESTER_BIN points at a non-existent file, or the bare
    `theHarvester` command isn't on PATH. Operator fix: `uv tool install
    theHarvester` or `pipx install theHarvester`.
    """


class TheHarvesterTimeoutError(TheHarvesterError):
    """Raised when a theHarvester invocation exceeds the configured
    THEHARVESTER_TIMEOUT_SECONDS hard cap. Default 600s.

    Common cause: too many sources selected with a high limit. Either
    reduce the source list, lower the limit, or raise the timeout."""


class TheHarvesterRunError(TheHarvesterError):
    """Raised when theHarvester runs but exits with non-zero status.

    Stderr from the run is included on the exception for context. Common
    causes: invalid domain, source plugin error, missing API key for a
    source that needs one (Shodan/Censys/SecurityTrails)."""


class TheHarvesterParseError(TheHarvesterError):
    """Raised when theHarvester completed but its output JSON couldn't
    be parsed. Indicates a theHarvester version mismatch or a partial
    write (disk full, killed mid-write, etc.)."""


class TheHarvesterPolicyError(TheHarvesterError):
    """Raised when a caller asks for a source that's NOT on the passive-
    only allowlist enforced by this MCP.

    Per Hard Rule 4 (no scanning third parties from operator's
    infrastructure), theHarvester sources that perform active recon
    (DNS brute-force, takeover detection) are refused. Operator must
    invoke them outside this MCP if needed and authorized."""
