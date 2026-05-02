# virustotal

MCP server exposing VirusTotal v3 file/URL/domain/IP reputation lookups to Archimedes.

Read-only by design. No file uploads. No comment/vote/tag writes. Tools:

- `lookup_file` — by MD5/SHA1/SHA256
- `lookup_url` — by URL string
- `lookup_domain` — by domain
- `lookup_ip` — by IPv4/IPv6

Auth via `VT_API_KEY` in workspace `.env`. Free tier supported (4 req/min, 500/day).
