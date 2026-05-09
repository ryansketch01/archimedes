# theharvester MCP

[theHarvester](https://github.com/laramies/theHarvester) MCP server for
Archimedes. Wraps the theHarvester CLI tool for **passive** subdomain /
host / IP / virtual-host / ASN enumeration.

Two tools:

- `enumerate(domain, sources, limit)` — run theHarvester against a domain
- `list_sources()` — return the passive-only allowlist this MCP enforces

**Email enumeration is intentionally NOT exposed** by this MCP per
LEGAL-POLICY PII handling. Operator can run `theHarvester -d <d> -b
hunter` outside the MCP if email enumeration is needed for an
authorized investigation.

## Installation

theHarvester is NOT installed automatically with this MCP — operator
installs it once on the host:

```bash
# Preferred (uv tool):
uv tool install theHarvester

# Alternative (pipx):
pipx install theHarvester

# Verify:
theHarvester --help
```

If installed but not on PATH, set `THEHARVESTER_BIN=/full/path/to/theHarvester`
in `.env`.

## Configuration

| Var | Default | Purpose |
|---|---|---|
| `THEHARVESTER_BIN` | `theHarvester` | Path or PATH-resolvable name of the executable |
| `THEHARVESTER_TIMEOUT_SECONDS` | `600` | Hard timeout per call (seconds; max 1800) |
| `THEHARVESTER_DEFAULT_LIMIT` | `100` | Default per-source result cap when caller doesn't specify |
| `THEHARVESTER_KEEP_OUTPUT` | _unset_ | Set to `1` to retain temp dirs after each run (debugging) |

API keys for sources that need them (Shodan, Censys, SecurityTrails,
etc.) are managed by **theHarvester itself** in
`~/.theHarvester/api-keys.yaml` — this MCP doesn't forward keys.
Sources that need keys but don't have them are silently skipped by
theHarvester.

## Tools

### `enumerate(domain, sources=None, limit=None)`

Run theHarvester against a domain. Returns:

```python
{
  "domain": "example.com",
  "sources_queried": ["crtsh", "otx", ...],
  "duration_seconds": 23.5,
  "hosts": [
    {"hostname": "sub.example.com", "ips": ["1.2.3.4"]},
    ...
  ],
  "distinct_ips": ["1.2.3.4", "9.9.9.9"],
  "vhosts": ["api.example.com"],
  "asns": [{"asn": "AS13335", "name": "CLOUDFLARENET"}],
  "raw_output_path": null   // unless THEHARVESTER_KEEP_OUTPUT=1
}
```

**Default sources** when caller passes none:
`crtsh`, `otx`, `hackertarget`, `rapiddns`, `sitedossier`, `duckduckgo`
(all keyless; works on a fresh theHarvester install).

**Allowlist enforcement:** every source must be in
`PASSIVE_SOURCE_ALLOWLIST`. Active-recon sources (DNS brute-force,
takeover detection) are refused with `TheHarvesterPolicyError`. Hard
Rule 4 (no scanning third parties from operator's infrastructure) is
satisfied because theHarvester queries third-party OSINT services, not
the target directly.

### `list_sources()`

Returns the allowlist + default set so callers can inspect what's
accepted before composing an `enumerate` call.

```python
{
  "passive_allowlist": ["anubis", "baidu", ..., "zoomeye"],
  "default_sources": ["crtsh", "otx", "hackertarget", ...]
}
```

## Run locally

```bash
uv sync --all-packages
uv run --directory mcps/theharvester theharvester-mcp
```

The MCP starts even if theHarvester isn't installed — the missing-
binary error surfaces only when `enumerate` is called.

## Tests

```bash
# unit tests (subprocess mocked; no theHarvester needed)
uv run --directory mcps/theharvester pytest tests/test_config.py tests/test_runner.py -v
```

A live integration test isn't included by default — running
theHarvester end-to-end takes 30s-5min depending on sources/limit
and adds churn against the third-party OSINT services. The unit
tests with mocked subprocess cover the wrapper's logic
exhaustively; smoke-test live by running the MCP and invoking
`enumerate` against a low-impact domain (e.g., your own).

## Naming

Package directory `mcps/theharvester/`, Python package
`theharvester_mcp` (avoids colliding with the upstream `theHarvester`
package name on PyPI). Entry point `theharvester-mcp`. Claude Code-
side tool calls are `mcp__theharvester__enumerate`,
`mcp__theharvester__list_sources`.
