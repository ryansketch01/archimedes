# shodan-mcp

MCP server exposing Shodan v1 API to Archimedes. Read-only.

Workspace member is named `shodan-mcp` (and the Python package is
`shodan_mcp`) to avoid colliding with the official `shodan` PyPI SDK.
The Claude Code-side MCP server name is just `shodan`, so tool calls
are `mcp__shodan__<tool>`.

Tools:
- `lookup_host(ip)` — full host detail (1 query credit)
- `search_hosts(query)` — Shodan query-syntax search (1 credit per page)
- `count_hosts(query)` — count only, **free** (no credits consumed)
- `lookup_internetdb(ip)` — free Shodan InternetDB summary (no key required)

Auth via `SHODAN_API_KEY` in workspace `.env`. Requires Shodan Membership
($5 lifetime) for the paid endpoints; InternetDB is unauthenticated.
