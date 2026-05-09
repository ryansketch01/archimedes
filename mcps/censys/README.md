# censys MCP

[Censys](https://search.censys.io/) MCP server for Archimedes. Three
read-only tools:

- `search_hosts(query, per_page, cursor)` — Censys host search v2
  (services running on internet-exposed IPs)
- `lookup_host(ip)` — full host record by IP
- `search_certificates(query, per_page, cursor)` — certificate
  transparency + scan-derived cert search

Read-heavy by design. No DNS scan submission, no admin endpoints,
no domain takeover signals.

## Configuration

| Var | Required | Purpose |
|---|---|---|
| `CENSYS_API_ID` | yes | API ID from https://search.censys.io/account/api |
| `CENSYS_API_SECRET` | yes | API Secret (paired with the API ID) |
| `CENSYS_API_BASE_URL` | no | Override base URL (default `https://search.censys.io/api/`) |

Authentication uses HTTP Basic with API_ID as username and API_SECRET
as password. Empirically verified 2026-05-09: Censys's v2 API rejects
Personal Access Token (Bearer) auth with *"You must authenticate with
a valid API ID and secret."* — PATs may be for v3/GraphQL endpoints
but won't work against /api/v2/. Use the legacy ID + Secret pair.

The Censys account API page (https://search.censys.io/account/api)
typically shows both PAT and API ID/Secret sections — the API ID
section may be visually below or in a separate tab from the PAT
section.

## Free-tier quota (as of 2026-05)

- ~100 search queries/month — `search_hosts`, `search_certificates`
- ~250 view requests/month — `lookup_host`

Censys returns 429 on both rate-limit and quota-exhaustion. The
client distinguishes them via the response body and surfaces
`CensysQuotaExhaustedError` separately so the operator can tell
"too fast right now" from "no more this month."

## Tools

### `search_hosts(query, per_page=10, cursor=None)`

Censys query syntax (Lucene-flavored, v2):

```
services.service_name: HTTP and location.country: "United States"
autonomous_system.asn: 13335
services.tls.certificates.leaf_data.subject.common_name: example.com
services.banner: "OpenSSH" and location.country_code: RU
```

Returns trimmed host hits with services list (port, transport,
software, banner excerpt, JA3S/JA4S, leaf cert SHA-256), location,
ASN, DNS names. Pagination via `next_cursor`.

### `lookup_host(ip)`

Returns same shape as a search hit but for a specific IP. Returns
`found: false` if Censys has no record.

### `search_certificates(query, per_page=10, cursor=None)`

Censys cert search syntax:

```
parsed.subject.common_name: example.com
parsed.issuer.organization: "Let's Encrypt"
parsed.validity.start: [2026-01-01 to 2026-05-01]
names: defense-careers-portal.com
```

Returns trimmed cert hits — fingerprints (SHA-256 + SHA-1), subject
CN, issuer DN/CN/organization, SAN list, validity window, key /
signature algorithms. Drops the parsed cert blob (huge).

Useful for IOC enrichment: find every cert ever issued for a domain,
identify cert reuse across infrastructure, hunt for Let's Encrypt
certs in attacker patterns (e.g., 7-day cycling on UNC1549's staging
domains).

## Run locally

```bash
uv sync --all-packages
uv run --directory mcps/censys censys
```

## Tests

```bash
# unit tests (fast, no network, no quota consumed)
uv run --directory mcps/censys pytest tests/test_config.py tests/test_client.py -v

# live tests (3 quota units consumed: 2 search + 1 view)
CENSYS_LIVE_TEST=1 uv run --directory mcps/censys pytest tests/test_integration.py -v
```

## Naming

Package name `censys`, entry point `censys`. Claude Code-side tool
calls are `mcp__censys__search_hosts`, `mcp__censys__lookup_host`,
`mcp__censys__search_certificates`.
