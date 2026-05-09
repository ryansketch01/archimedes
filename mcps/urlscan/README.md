# urlscan MCP

[urlscan.io](https://urlscan.io/) MCP server for Archimedes. Three
read-or-write tools:

- `search(query, size)` — search past public scans (Lucene-style query
  syntax). Free, no submit quota consumed.
- `lookup_scan(uuid)` — fetch a single scan's full record. Free.
- `submit_scan(url, visibility, ...)` — submit a new URL for scanning.
  Consumes the 5,000/month free-tier quota.

## Configuration

| Var | Required | Purpose |
|---|---|---|
| `URLSCAN_API_KEY` | yes | API key from https://urlscan.io/user/profile/ |
| `URLSCAN_API_BASE_URL` | no | Override base URL (default `https://urlscan.io/api/v1/`) |

## Tools

### `search(query, size=10)`

Search urlscan's public scan history. Lucene-style query language:

```
domain:example.com
ip:1.2.3.4
page.country:RU AND task.source:api
hash:<sha256>
task.url:"https://example.com/login*"
```

Free text without a field qualifier matches any URL field.

Returns `total`, `returned`, `has_more`, and a list of trimmed result
entries. Each entry includes the scan UUID (pass to `lookup_scan` for
the full record), task metadata, page (domain/IP/country/server),
stats, slim verdicts, and pointers to the full result API URL plus
the screenshot URL.

### `lookup_scan(uuid)`

Fetch a single scan's full record by UUID. Returns:

- `task` — submission metadata (URL, time, source, visibility, tags)
- `page` — post-redirect URL, IP, country, server, ASN, TLS age
- `stats` — uniqIPs / uniqCountries / uniqASNs / requests / etc.
- `verdicts` — overall + urlscan classifier + community + engines
- `lists` — IPs / domains / ASNs / countries / servers / hashes
  (URLs intentionally dropped — too noisy)
- `screenshot_url`, `result_url`, `web_url`

If urlscan has no record for the UUID, returns `found: false` rather
than raising. Useful when you have a UUID from somewhere uncertain.

### `submit_scan(url, visibility="public", tags, referer, user_agent)`

Submit a new URL to urlscan.io for scanning. urlscan visits the URL
from THEIR infrastructure (not yours), so this is acceptable under
Hard Rule 4 (no scanning third parties from your own infrastructure).

**Visibility caveat:** `public` scans are searchable by other urlscan
users. Use `unlisted` or `private` if the URL contains sensitive
context (internal hostnames, credentials in query strings, customer
context, etc.). Free-tier quota: 5,000/month public + 1,000 unlisted
+ 1,000 private.

**Async:** scans typically take 15-30 sec. `submit_scan` returns the
UUID immediately; poll `lookup_scan(uuid)` after a wait to fetch the
result.

**Operator note:** prefer `search` first. Most CTI questions ("has
anyone seen this URL before?", "what does this domain look like?")
are answered by historical scans without consuming submit quota.
Only submit when you genuinely need a fresh observation.

## Run locally

```bash
# from repo root
uv sync --all-packages
uv run --directory mcps/urlscan urlscan
```

## Tests

```bash
# unit tests (fast, no network)
uv run --directory mcps/urlscan pytest tests/test_config.py tests/test_client.py -v

# live read-only tests against urlscan.io (requires URLSCAN_API_KEY in .env)
URLSCAN_LIVE_TEST=1 uv run --directory mcps/urlscan pytest tests/test_integration.py -v

# live submit test (consumes 1 from your 5,000/mo quota; uses unlisted visibility)
URLSCAN_LIVE_TEST=1 URLSCAN_LIVE_SUBMIT=1 \
    uv run --directory mcps/urlscan pytest tests/test_integration.py -v
```

## Naming note

Package name `urlscan` (no `-mcp` suffix) and entry point `urlscan`
to match `mcps/virustotal` and `mcps/shodan-mcp` conventions for
unique-on-PyPI names. Claude Code-side tool calls are
`mcp__urlscan__search`, `mcp__urlscan__lookup_scan`,
`mcp__urlscan__submit_scan`.
