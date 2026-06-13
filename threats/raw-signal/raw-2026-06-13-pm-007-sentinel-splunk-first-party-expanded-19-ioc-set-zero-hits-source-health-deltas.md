---
raw_id: raw-2026-06-13-pm-007
collected_at: 2026-06-13T15:38:00-04:00
run_id: pre-brief-20260613-153000
collection_mode: pre_brief_collection
sentinel: true
result: clean
source:
  source_yaml_id: archimedes-self
  source_name: Archimedes collector self-report — Splunk first-party + source-health sentinel
  source_url: null
  published_at: 2026-06-13T15:38:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sentinel, first_party_splunk_zero_hits, source_health_summary]
iocs_extracted: false
iocs_count: 0
text_word_count: 850
promoted: false
ttl_expires_at: 2026-09-11T15:38:00-04:00
---

# Pre-brief 15:30 EDT 2026-06-13 — Splunk first-party sentinel + source-health summary

Companion sentinel raw-signal file for the 15:30 EDT pre-brief sweep. Documents the Splunk first-party IOC sentinel sweep result (expanded 19-IOC set including the 11 net-new IOCs from Mandiant primary retrieval), and source-health deltas observed in this sweep.

## Splunk first-party sentinel — finding-2026-06-13-0002 expanded IOC set (-24h, both indexes)

### Original 8-IOC set from finding-2026-06-13-0002 (already ran at 12:00 FLASH)

- Query: `index=defenseclaw_local OR index=archimedes ("azurenetfiles.net" OR "176.120.22.24" OR "meshagent32-azure-ops" OR "meshagent64-azure-ops" OR "meshagent64-v2" OR "README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED" OR "_fanout.sh" OR "agent.ashx") | stats count by index, sourcetype, host`
- Result: **0 events** over -24h
- Compared to 12:00 FLASH (same query): **0 events** — unchanged baseline.

### Net-new 11-IOC set from Mandiant primary direct retrieval (raw-2026-06-13-pm-005)

- Query: `index=defenseclaw_local OR index=archimedes ("142.11.200.186" OR "142.11.200.187" OR "142.11.200.188" OR "142.11.200.189" OR "142.11.200.190" OR "2ab684d93c1553fad87041b4dea97188a97e78589deee2a7bacff905564f3a35" OR "f02a924c9ff92a8780ce812511341182c6b509d45bc59f3f7b522e37225d24fc" OR "d83fdb9e53c5ff03c4cb0451ea1bebd79b53f29eadc1e2fa394c7af13a86ce2f" OR "c7e9332731b06644fc73e0046a2a89eaa59b09f54250e9bd622467187351711f" OR "68257a6f9ff196179ec03624e849927f26599eb180a7c82e14ef5bc4e93bc309") | stats count by index, sourcetype`
- Result: **0 events** over -24h
- Interpretation: First Splunk sentinel sweep across the full 19-IOC expanded UNC6240 / ShinyHunters IOC set is clean. Frank's telemetry catchment has not touched the campaign infrastructure (consistent with the 100-org / 68%-higher-ed victim profile — Frank is not a higher-ed environment).

### Hard Rule 8 framing

Per Hard Rule 8 + the finding-2026-06-13-0002 telemetry framing: silent Splunk is NOT disconfirming. The 0-hit result on -24h is "absence-of-positive-signal-given-visibility-limited-catchment," NOT "Mandiant's published IOCs are wrong." First-party first-party-vs-external precedence does not apply here because Splunk has nothing to contribute either way.

## archimedes index liveness (-24h baseline)

- Query: `index=defenseclaw_local OR index=archimedes earliest=-24h | stats count by index, sourcetype`
- Result not separately re-executed this sweep; baseline from 12:00 FLASH: 29 events total (archimedes:operation 14, archimedes:scheduler 15). Pattern continues — Archimedes own pipeline healthy, defenseclaw_local in 13th-consecutive sweep of 0-event non-archimedes-internal flow.

## Source-health deltas observed this sweep

Field-ownership rule: only runtime fields updated below; operator-set `notes:` preserved verbatim by librarian when applied.

### Sources reaching corpus this sweep (status held healthy)

| source_yaml_id | observation | last_successful_fetch new value | items in window | raw-signaled |
|---|---|---|---|---|
| bleepingcomputer | 1 in-window item retrieved (Velvet Ant relay) | 2026-06-13T15:31:35-04:00 | 1 | raw-2026-06-13-pm-004 |
| thehackernews | 2 in-window items — Splunk CVE-2026-20253 (09:23 EDT) + Velvet Ant 2026-06-12 surfaced via search | 2026-06-13T15:31:25-04:00 | 2 | raw-2026-06-13-pm-001, raw-2026-06-13-pm-004 |
| securityweek | 1 in-window item (NPM 12) | 2026-06-13T15:31:21-04:00 | 1 | raw-2026-06-13-pm-002 |
| securityaffairs | 1 in-window item (Anthropic 4th-publisher) | 2026-06-13T15:31:27-04:00 | 1 | raw-2026-06-13-pm-003 |
| mandiant | **DIRECT-HTML RETRIEVAL SUCCESS** (RSS endpoint remains stale, but cloud.google.com landing page + direct post URL work via WebFetch). Mandiant primary on UNC6240/ShinyHunters retrieved. | 2026-06-13T15:36:30-04:00 | 1 (1 primary post directly retrieved + listed) | raw-2026-06-13-pm-005 |
| unit42 | 0 in-window items (feed last_modified 2026-06-12T22:00 UTC pre-window) | 2026-06-13T15:32:22-04:00 | 0 | n/a |
| cisco-talos | 0 in-window items (feed last_modified 2026-06-12 pre-window) | 2026-06-13T15:32:04-04:00 | 0 | n/a |
| krebs | 0 in-window items | 2026-06-13T15:31:44-04:00 | 0 | n/a |
| the-record | 0 in-window items | 2026-06-13T15:31:45-04:00 | 0 | n/a |
| helpnetsecurity | 0 in-window items | 2026-06-13T15:31:47-04:00 | 0 | n/a |
| sans-isc | 0 in-window items | 2026-06-13T15:32:03-04:00 | 0 | n/a |
| darkreading | 1 in-window item (Name That Toon Contest — marketing, not signal) | 2026-06-13T15:31:46-04:00 | 0 raw-signaled | n/a |
| mstic | 0 in-window items (last_modified 2026-06-10T16:00 UTC pre-window) | 2026-06-13T15:32:25-04:00 | 0 | n/a |
| theregister | 0 in-window items | 2026-06-13T15:31:28-04:00 | 0 | n/a |
| cisa-advisories | 0 in-window items (all.xml unchanged from 12:00 FLASH) | 2026-06-13T15:31:29-04:00 | 0 | n/a |
| crowdstrike | RSS reachable but feed lacks timestamps; all items appear to be 2026-06 marketing/operational posts | 2026-06-13T15:32:24-04:00 | 0 raw-signaled (no fresh threat-intel content) | n/a |
| volexity | direct-HTML check via volexity.com/blog confirms 5 most recent posts unchanged (last post 2026-06-04 VerdantBamboo); RSS still stale | RSS unchanged stale | 0 | n/a |

### Sources stale-persistent this sweep (no change)

- **mandiant** RSS — failure_count remains 25 (RSS path); but direct-HTML retrieval SUCCESS this sweep on a specific blog post. Note for source-health: keep `status: stale` for the RSS path, but consider adding an operator-set note that direct-HTML retrieval is the working canonical path until the canonical-swap operator decision is made. This is a structural improvement in workflow reliability.
- **volexity** RSS — failure_count remains 6 (RSS); direct-HTML check this sweep showed 0 fresh posts, so no missed coverage.
- **msrc** — pre-existing stale unchanged; not retried.
- **lumen / shadowserver** — pre-existing morning-flipped stale; not retried.
- **sophos / industrialcyber-co / ars-security / trellix / x-cisagov / x-gossithedog / censys / urlscan / hibp** — pre-existing stale; not retried.

### Sources skipped per heavy-priority scope this sweep

x-swiftonsecurity, x-vxunderground, x-falconfeedsio, nsa-cnsa, fbi-flash, nvd, mitre-attack, dod-cmmc, recorded-future, symantec, dragos, zdi-blog, github-blog-self-disclosure, shodan, virustotal, abuseipdb, github-advisories, sentinelone, bitdefender, wired-security, rapid7, proofpoint, sonatype-research, sygnia-research, tenet-security-research, dataminr-research, bloomberg.

### Provisional source-grades ratification clock (unchanged)

2026-06-15T16:00:00-04:00 — Sonatype / Sygnia / Tenet / Dataminr ratification due. Bloomberg PENDING operator B/B+/A tier decision. None of these sources fetched/surfaced new material this sweep.

## Summary table

| Metric | Value |
|---|---|
| Raw-signal files written this sweep | 7 (including this sentinel) |
| Material content files written | 6 (pm-001 through pm-006) |
| Sentinel file | 1 (pm-007 — this) |
| Carry-forward items resolved | 6 of 6 (see resolutions below) |
| Net-new IOCs surfaced | 11 (Mandiant primary direct retrieval — 5 staging IPs + 5 SHA-256 + 1 Linux meshagent indicator class) |
| FLASH triggers fired | 0 (none in window; not a FLASH-mode sweep regardless — Mode 1 pre-brief) |
| Splunk first-party hits across expanded 19-IOC set | 0 |
| Source-health NEW degradations | 0 |
| Source-health recoveries | 1 partial — Mandiant direct-HTML path confirmed working (RSS endpoint still stale; operator-decision on canonical-swap pending) |

## Carry-forward resolution summary (delivered for orchestrator)

| # | Carry-forward item | Resolution | Net-new material |
|---|---|---|---|
| 1 | CVE-2026-20253 Splunk Enterprise CVSS 9.8 | YES | Splunk SVD-2026-0603 vendor primary + watchTowr discoverer writeup + THN news-tier; NOT exploited in wild; NOT KEV-added; patches available |
| 2 | NPM 12 | YES | Full technical mechanic public (default block, npm approve-scripts allowlist, --allow-remote flag, binding.gyp coverage); cites TeamPCP (#001) + Shai-Hulud (operator-deferred /new-actor candidate) |
| 3 | SecurityAffairs Anthropic 4th-publisher relay | PARTIAL | One marginal framing detail (30-day data retention layered-security context); does not warrant finding update |
| 4 | BleepingComputer + (BONUS) The Hacker News on Velvet Ant | PARTIAL | THN also surfaced as 3rd publisher; both relays cite Sygnia; no new IOCs/victims/TTPs/CVEs |
| 5 | UNC6240 / ShinyHunters / CVE-2026-35273 scale corroboration + new IOCs | PARTIAL on scale; YES on IOCs | Mandiant primary direct retrieval unlocks 11 net-new IOCs (5 staging IPs + 5 SHA-256 + 1 new indicator class); no 2nd-vendor on scale figures |
| 6 | Handala / Cal Water genuinely-independent 3rd source | NO | BreachNews + WANA both read off Handala leak-post; no Cal Water statement; no FBI/CISA advisory; no independent vendor DFIR |
