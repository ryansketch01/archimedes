# SpiderFoot MCP

MCP wrapper around a self-hosted SpiderFoot daemon. Restricted to **passive modules only** per `doctrine/LEGAL-POLICY.md` — active modules (port scanning, web spidering, DNS brute force, screenshots, vulnerability probing) are rejected at the input boundary regardless of caller.

## Tools

- `passive_scan(target, name?, modules?, target_type?)` — run a passive scan, block until terminal status or timeout, return aggregated events + folded distinct domains/IPs/emails.
- `list_modules()` — return the passive allowlist, default module set, and a sample of explicitly-prohibited modules.
- `health()` — reachability + auth probe.

## Configuration

| Variable | Required | Default | Notes |
|---|---|---|---|
| `SPIDERFOOT_URL` | yes | — | Base URL of the SpiderFoot daemon (e.g., `http://localhost:5001`). |
| `SPIDERFOOT_USERNAME` | no | — | Set with `SPIDERFOOT_PASSWORD` if SpiderFoot is started with `--passwd <user>:<pass>`. |
| `SPIDERFOOT_PASSWORD` | no | — | See above. |
| `SPIDERFOOT_SCAN_TIMEOUT_SECONDS` | no | `600` | Wall-clock seconds to wait for a scan before returning partial results. Scan continues in SpiderFoot. |
| `SPIDERFOOT_POLL_INTERVAL_SECONDS` | no | `5` | How often to poll `/scanstatus`. |
| `SPIDERFOOT_HTTP_TIMEOUT_SECONDS` | no | `30` | Per-request timeout. |
| `SPIDERFOOT_VERIFY_SSL` | no | `true` | Set `false` only on trusted networks with self-signed certs (loopback, LAN). |

## Installing SpiderFoot

This MCP does NOT bundle SpiderFoot — it expects a daemon already running. Recommended:

```bash
# OSS SpiderFoot via uv tool install
uv tool install --from git+https://github.com/smicallef/spiderfoot.git spiderfoot

# Loopback-only, no auth (default safe for single-host dev):
sf.py -l 127.0.0.1:5001
```

Then set `SPIDERFOOT_URL=http://127.0.0.1:5001` in `.env`.

## Passive allowlist

See `src/spiderfoot_mcp/models.py` for the canonical list. Reconciled against `doctrine/LEGAL-POLICY.md` and `.claude/agents/collector.md`. Includes:

- DNS lookups (resolve, common-SRV, neighbor, AXFR-attempt)
- WHOIS / DNSDB
- Certificate Transparency (crt.sh, Cert Spotter)
- Search engines (Bing, DuckDuckGo, Google, Yandex)
- Threat-intel feeds (VirusTotal, ThreatFox, OTX, ThreatCrowd, Shodan, Censys, GreyNoise, AbuseIPDB, urlscan.io)
- Breach membership (HIBP, HIBP pastes)
- Reputation lists (SpamCop, Spamhaus, PhishTank, MalwarePatrol, Tor exit list)
- Public archives (Wayback, Common Crawl)
- Pastebin search
- GitHub code search

## What's NOT exposed

The MCP intentionally refuses any module that performs active recon (sending traffic to or fingerprinting the target itself):

- `sfp_tool_nmap`, `sfp_tool_nuclei`, `sfp_tool_nbtscan`, `sfp_tool_dnstwist`, `sfp_tool_wafw00f`, `sfp_tool_whatweb`
- `sfp_spider`, `sfp_dnsbrute`, `sfp_screenshot`
- `sfp_portscan_tcp`, `sfp_bingsharedip`

If an authorized engagement genuinely needs an active module against a target in `infrastructure/authorized-targets.yaml`, drive SpiderFoot directly via its web UI / CLI — the MCP is a CTI collection wrapper, not a pentest harness.
