"""Subprocess runner for theHarvester.

Different from the REST clients in this workspace — this MCP wraps a
local CLI tool. Runner responsibilities:

  - Validate the source allowlist (refuse non-passive sources)
  - Resolve the theHarvester executable (PATH or THEHARVESTER_BIN)
  - Run theHarvester with -f <basename> -d <domain> -b <comma-sources>
    -l <limit> in a temp dir
  - Parse theHarvester's JSON output (basename.json)
  - Map to our flat EnumerateOutput
  - Clean up temp dir unless THEHARVESTER_KEEP_OUTPUT=1

theHarvester writes BOTH .json and .xml output. We only parse JSON.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

from theharvester_mcp.config import TheHarvesterConfig
from theharvester_mcp.exceptions import (
    TheHarvesterNotInstalledError,
    TheHarvesterParseError,
    TheHarvesterPolicyError,
    TheHarvesterRunError,
    TheHarvesterTimeoutError,
)
from theharvester_mcp.models import (
    PASSIVE_SOURCE_ALLOWLIST,
    AsnEntry,
    EnumerateOutput,
    HostEntry,
)


def _validate_sources(sources: list[str]) -> list[str]:
    """Filter sources against the passive-only allowlist.

    Refuses ANY source not in the allowlist with a TheHarvesterPolicyError.
    Returns the filtered list (preserves order; deduplicates while
    preserving first occurrence).
    """
    seen: set[str] = set()
    cleaned: list[str] = []
    rejected: list[str] = []
    for s in sources:
        s_lower = s.strip().lower()
        if not s_lower:
            continue
        if s_lower in seen:
            continue
        if s_lower not in PASSIVE_SOURCE_ALLOWLIST:
            rejected.append(s_lower)
            continue
        seen.add(s_lower)
        cleaned.append(s_lower)

    if rejected:
        raise TheHarvesterPolicyError(
            f"Source(s) not on the passive-only allowlist: {', '.join(rejected)}. "
            f"Allowed: {', '.join(PASSIVE_SOURCE_ALLOWLIST)}. "
            "Sources outside the allowlist are refused per Hard Rule 4 — they may "
            "perform active recon against unauthorized targets. Operator must "
            "invoke them outside this MCP if needed."
        )

    if not cleaned:
        raise TheHarvesterPolicyError(
            "No valid sources after allowlist filter; specify at least one "
            "passive source from PASSIVE_SOURCE_ALLOWLIST."
        )
    return cleaned


def _resolve_executable(config: TheHarvesterConfig) -> str:
    """Locate the theHarvester executable. Prefers explicit
    THEHARVESTER_BIN; falls back to PATH lookup."""
    candidate = config.theharvester_bin
    # If candidate looks like a path, validate it exists
    if os.sep in candidate or "/" in candidate:
        if not Path(candidate).is_file():
            raise TheHarvesterNotInstalledError(
                f"THEHARVESTER_BIN points at non-existent file: {candidate}. "
                "Install via `uv tool install theHarvester` or `pipx install "
                "theHarvester`, then either ensure it's on PATH or update the "
                "env var."
            )
        return candidate

    # Bare command — search PATH
    found = shutil.which(candidate)
    if not found:
        raise TheHarvesterNotInstalledError(
            f"`{candidate}` not found on PATH. Install via "
            "`uv tool install theHarvester` (preferred) or `pipx install "
            "theHarvester`. If installed but not on PATH, set THEHARVESTER_BIN "
            "to the full executable path."
        )
    return found


def _parse_json_output(json_path: Path) -> dict[str, Any]:
    """Parse theHarvester's JSON output. Schema varies by version; we
    accept both top-level dict and nested-by-domain shapes."""
    if not json_path.is_file():
        raise TheHarvesterParseError(
            f"Expected JSON output at {json_path} but file does not exist."
        )
    try:
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        raise TheHarvesterParseError(
            f"Failed to parse theHarvester JSON output at {json_path}: {e}"
        ) from e
    if not isinstance(data, dict):
        raise TheHarvesterParseError(
            f"theHarvester JSON output is not a dict (got {type(data).__name__}). "
            f"Path: {json_path}"
        )
    return data


def _normalize_hosts(raw: Any) -> list[HostEntry]:
    """theHarvester's `hosts` field is sometimes a list of strings
    ('host:ip,ip'), sometimes list of dicts, sometimes mixed."""
    out: list[HostEntry] = []
    if not isinstance(raw, list):
        return out
    for entry in raw:
        if isinstance(entry, str):
            # Format: "subdomain.example.com:1.2.3.4,5.6.7.8" or just "subdomain"
            if ":" in entry:
                host, _, ips_str = entry.partition(":")
                ips = [ip.strip() for ip in ips_str.split(",") if ip.strip()]
                hostname = host.strip()
                if not hostname:
                    continue
                out.append(HostEntry(hostname=hostname, ips=ips))
            else:
                hostname = entry.strip()
                if not hostname:
                    continue
                out.append(HostEntry(hostname=hostname))
        elif isinstance(entry, dict):
            host = entry.get("host") or entry.get("hostname") or entry.get("name")
            if not host:
                continue
            hostname = str(host).strip()
            if not hostname:
                continue
            ip_list_raw = entry.get("ip") or entry.get("ips") or []
            if isinstance(ip_list_raw, str):
                ips = [ip.strip() for ip in ip_list_raw.split(",") if ip.strip()]
            elif isinstance(ip_list_raw, list):
                ips = [str(ip).strip() for ip in ip_list_raw if ip]
            else:
                ips = []
            out.append(HostEntry(hostname=hostname, ips=ips))
    return out


def _normalize_strings(raw: Any) -> list[str]:
    """Generic list-of-strings normalizer for ips/vhosts."""
    if not isinstance(raw, list):
        return []
    return [str(v).strip() for v in raw if v]


def _normalize_asns(raw: Any) -> list[AsnEntry]:
    """ASN entries can be strings ('AS13335 CLOUDFLARENET') or dicts."""
    out: list[AsnEntry] = []
    if not isinstance(raw, list):
        return out
    for entry in raw:
        if isinstance(entry, str):
            parts = entry.split(maxsplit=1)
            asn = parts[0].strip()
            name = parts[1].strip() if len(parts) > 1 else None
            if asn:
                out.append(AsnEntry(asn=asn, name=name))
        elif isinstance(entry, dict):
            asn = entry.get("asn") or entry.get("number")
            if not asn:
                continue
            out.append(AsnEntry(asn=str(asn).strip(), name=entry.get("name") or entry.get("organization")))
    return out


def run_theharvester(
    config: TheHarvesterConfig,
    domain: str,
    sources: list[str],
    limit: int | None = None,
) -> EnumerateOutput:
    """Run theHarvester end-to-end and return a parsed EnumerateOutput.

    Raises:
        TheHarvesterPolicyError: source not on allowlist
        TheHarvesterNotInstalledError: executable not found
        TheHarvesterTimeoutError: subprocess exceeded timeout
        TheHarvesterRunError: subprocess returned non-zero
        TheHarvesterParseError: output JSON missing or malformed
    """
    cleaned_sources = _validate_sources(sources)
    bin_path = _resolve_executable(config)

    effective_limit = limit if limit is not None else config.theharvester_default_limit
    sources_arg = ",".join(cleaned_sources)

    keep_output = os.environ.get("THEHARVESTER_KEEP_OUTPUT") == "1"
    tmpdir_str = tempfile.mkdtemp(prefix="archimedes-harvester-")
    tmpdir = Path(tmpdir_str)
    output_basename = tmpdir / "harvest"

    cmd = [
        bin_path,
        "-d", domain.strip(),
        "-b", sources_arg,
        "-l", str(effective_limit),
        "-f", str(output_basename),
    ]

    start = time.monotonic()
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=config.theharvester_timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as e:
        if not keep_output:
            shutil.rmtree(tmpdir, ignore_errors=True)
        raise TheHarvesterTimeoutError(
            f"theHarvester exceeded {config.theharvester_timeout_seconds}s timeout. "
            f"Sources: {sources_arg}. Reduce sources or limit, or raise "
            "THEHARVESTER_TIMEOUT_SECONDS."
        ) from e
    except FileNotFoundError as e:
        # Race: PATH lookup said it was there but exec failed
        shutil.rmtree(tmpdir, ignore_errors=True)
        raise TheHarvesterNotInstalledError(
            f"Failed to exec {bin_path}: {e}"
        ) from e

    duration = time.monotonic() - start

    if proc.returncode != 0:
        if not keep_output:
            shutil.rmtree(tmpdir, ignore_errors=True)
        raise TheHarvesterRunError(
            f"theHarvester exited rc={proc.returncode}. stderr (last 500 chars): "
            f"{proc.stderr[-500:].strip()}"
        )

    json_path = Path(str(output_basename) + ".json")
    try:
        data = _parse_json_output(json_path)
    except TheHarvesterParseError:
        if not keep_output:
            shutil.rmtree(tmpdir, ignore_errors=True)
        raise

    # theHarvester JSON shape varies. Try common locations:
    hosts_raw = data.get("hosts") or data.get("host") or []
    ips_raw = data.get("ips") or data.get("ip") or []
    vhosts_raw = data.get("vhost") or data.get("vhosts") or []
    asns_raw = data.get("asns") or data.get("asn") or []

    output = EnumerateOutput(
        domain=domain.strip(),
        sources_queried=cleaned_sources,
        duration_seconds=round(duration, 2),
        hosts=_normalize_hosts(hosts_raw),
        distinct_ips=_normalize_strings(ips_raw),
        vhosts=_normalize_strings(vhosts_raw),
        asns=_normalize_asns(asns_raw),
        raw_output_path=str(json_path) if keep_output else None,
    )

    if not keep_output:
        shutil.rmtree(tmpdir, ignore_errors=True)

    return output
