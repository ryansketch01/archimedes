---
raw_id: raw-2026-05-16-am-000
collected_at: 2026-05-16T07:33:00-04:00
run_id: pre-brief-20260516-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-self
  source_name: "Archimedes collector — pre-brief sweep sentinel"
  source_url: null
  published_at: 2026-05-16T07:33:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, pre_brief, dedup_audit, saturday_quiet]
triage_tags: [sentinel, non_flash, dedup_audit, splunk_self_telemetry_only, saturday_pattern]
iocs_extracted: false
iocs_count: 0
text_word_count: 980
promoted: false
ttl_expires_at: 2026-08-14T07:33:00-04:00
---

# Pre-brief sweep sentinel — 2026-05-16 07:30 EDT (Saturday)

Window: 2026-05-15 17:30 EDT → 2026-05-16 07:30 EDT (14h)
Last prior sweep: 2026-05-16 06:00 EDT FLASH (clean sweep, 0 triggers, 29th consecutive dormant non-self-telemetry Splunk sweep per commit d2560d4)
Quiet hours: ending 09:00 EDT — morning brief publishes at 08:00, posts on time

## Sources queried (in 14h pre-brief window)

| Source | Status | Items in window |
|---|---|---|
| CISA Advisories (RSS all.xml) | OK | 0 |
| CISA KEV (JSON, full-catalog dateAdded scan) | OK | 0 new (most recent: CVE-2026-42897 Microsoft Exchange dateAdded 2026-05-15, dueDate 2026-05-29 = T-13 today) |
| BleepingComputer (RSS) | OK | 0 (last_modified 11:21 UTC = 07:21 EDT, server-fresh but no new posts since 2026-05-15 PM) |
| The Record (RSS) | OK | 0 |
| The Hacker News (RSS) | OK | 0 (last_modified 10:23 UTC = 06:23 EDT, server-fresh, no new posts in window) |
| Krebs (RSS) | OK | 0 (last_modified 2026-05-13 — Krebs cadence is multi-day, normal for Saturday) |
| Microsoft Security Blog (RSS) | OK | 0 (last_modified 2026-05-14 21:51 UTC — pre-window) |
| MSRC blog (redirect) | OK via redirect (raw fetch 403 expected) | n/a — covered via parent MS Security Blog feed |
| Mandiant (cloud.google.com) | feedburner 404 persistent | n/a — known stale, index page out-of-window |
| Unit 42 (feedburner) | OK | 0 |
| Cisco Talos (RSS) | OK | 0 |
| Securelist (RSS) | OK | 0 (last_modified 2026-05-15 10:15 UTC — pre-window) |
| Sophos (RSS) | 404 this sweep | n/a — single soft fail, retry next sweep |
| WeLiveSecurity / ESET (RSS) | OK | 0 |
| SentinelOne (RSS) | OK | 0 |
| Volexity (RSS) | XML parse error | n/a — flag for source-health review |
| SANS ISC (RSS) | OK | 0 |
| Rapid7 (RSS) | OK | 0 |
| SecurityWeek (RSS) | OK | 1 (NGINX Rift PoC — already captured in 06:00 FLASH raw-2026-05-16-flash-0600-001) |
| Bitdefender Labs (RSS) | 404 this sweep | n/a — second consecutive failure (also seen in 06:00 FLASH); flag for source-health |
| Industrial Cyber (RSS) | 403 | n/a — bot-block; retry next sweep |
| Symantec security.com (RSS) | 404 | n/a — feed path may have changed; flag for source-health |
| Wiz Research (RSS) | 404 | n/a — feed path may have changed; flag for source-health |
| Snyk (RSS) | OK | 0 |
| Socket (RSS) | 404 | n/a — feed path may have changed |
| Darktrace (RSS) | OK | 0 |
| ZDI Pwn2Own (RSS) | OK | **1 in-window** — Pwn2Own Berlin Day 3 / final results (raw-2026-05-16-am-001) |
| Cybersecurity Dive (RSS) | OK | 0 (last_modified 2026-05-15 15:20 UTC — pre-window) |
| Shodan (NGINX exposure count) | OK | 53,734,017 NGINX hosts globally — contextual for NGINX Rift carry-forward |
| Splunk defenseclaw_local | OK | 0 events last 14h — **30th consecutive dormant non-self-telemetry sweep** |
| Splunk archimedes | OK | 11 self-telemetry events (4 archimedes:operation + 7 archimedes:scheduler) — internal heartbeat only |

Total sources queried: 30
Sources OK with in-window content: 2 (SecurityWeek NGINX Rift PoC dedup'd from FLASH; ZDI Pwn2Own Day 3 new)
Sources with parse / fetch errors: 6 (Sophos, Volexity, Bitdefender, Industrial Cyber, Symantec security.com, Wiz Research, Socket — none load-bearing this sweep)
Source-health changes: see "Source-health changes" section below

## Raw signals written this run

1. **raw-2026-05-16-am-001-pwn2own-berlin-2026-day-3-final-results-master-of-pwn.md**
   - ZDI Day 3 wrap + final Master of Pwn standings
   - Event total $943,250 across 42 unique zero-days
   - Day 2 Exchange chain (Orange Tsai / DEVCORE) embargo continues; no embargo-lift signal in window
   - Routes to morning brief as carry-forward continuation of yesterday afternoon brief Pwn2Own watch item
   - NOT a FLASH trigger

## Carry-forward items from prior cycles — status check

Per orchestrator instructions, these were checked for NEW reporting in the 14h window:

1. **NGINX Rift PoC publication (CVE-2026-42945)** — Carried into 06:00 FLASH as raw-2026-05-16-flash-0600-001 (SecurityWeek primary, depthfirst PoC publication ~36-48h post-disclosure). Routes to morning brief on finding-2026-05-14-0002 lineage. **NEW in 14h window**: Shodan global NGINX exposure count = 53,734,017 hosts (Saturday count) — contextual sizing for briefer if they want to dimension PoC blast radius; not a separate raw-signal-worthy event.

2. **CVE-2026-42897 KEV addition (Microsoft Exchange)** — Verified KEV JSON full-catalog scan this sweep: still most-recent entry (dateAdded 2026-05-15, dueDate 2026-05-29). **T-13 today**. No new KEV updates. No new MSRC reporting in window. No exploitation-status-change signal. Anti-noise: already captured in raw-2026-05-15-flash-0600-001 + raw-2026-05-15-pm-001; do NOT re-write.

3. **Pwn2Own Berlin Day 2 Exchange chain (Orange Tsai / DEVCORE, embargoed)** — **NEW in 14h window**: ZDI Day 3 wrap published this morning. Day 2 Exchange chain NOT mentioned in Day 3 wrap — embargo remains active. raw-2026-05-16-am-001 confirms event conclusion ($943,250 total) and embargo continuation. Operator note: standard 90-day Pwn2Own vendor-coordinated-disclosure window applies; CVE assignments anticipated 2026 Q3.

4. **node-ipc compromise (UNATTRIBUTED, Socket+StepSecurity+Ox+Upwind)** — Anti-noise applies (finding-2026-05-15-0005). No new vendor research in window. Socket / Wiz / Bitdefender Labs feeds all 404 this sweep (transient or path-changed; see source-health section). No re-write.

5. **Cisco SD-WAN T-1** — CVE-2026-20182 federal deadline dueDate 2026-05-17 = **T-1 tomorrow (Sunday)**. KEV catalog unchanged. No new exploitation reporting in window. Briefer should retain this in T-1 watch position. Operator note: Sunday is a federal-holiday-equivalent for non-essential ops; agencies under BOD-22-01 typically front-load Friday remediation, so Monday morning brief may surface compliance-status indicators if CISA publishes Q2 metrics.

6. **MSTIC Turla awareness** — Anti-noise applies (raw-2026-05-15-flash-1800-001 forwarded from yesterday's 18:00 sweep). No new MSTIC reporting in window. MS Security Blog feed last_modified 2026-05-14 21:51 UTC — quiet through weekend.

## Saturday pattern observations

- Cadence on A-grade vendor research and major media sources is genuinely quiet across the Friday-evening → Saturday-morning window. Krebs, MSTIC, Securelist, Cybersecurity Dive, Mandiant index page all show last_modified pre-window timestamps.
- The two productive items (NGINX Rift PoC publication; Pwn2Own Day 3) are exactly the Saturday-shaped surfaces the orchestrator flagged in scope context: an embargoed-disclosure event wrap-up and a researcher PoC publication on a freshly-disclosed vendor CVE.
- No surprise CVE-2026-42897 exploitation report, no NGINX Rift weaponization signal, no supply-chain-follow-up beyond the four-firm node-ipc consensus already in yesterday's brief.

## FLASH-shape candidates the grader should fast-path

**None.** Both 14h-window items routed to morning brief regular flow:

- raw-2026-05-16-flash-0600-001 (NGINX Rift PoC) — already non-FLASH per 06:00 sweep evaluation; carry-forward update on existing finding-2026-05-14-0002
- raw-2026-05-16-am-001 (Pwn2Own Day 3) — non-FLASH (embargoed, no CVE, no exploitation); carry-forward continuation of yesterday afternoon brief Pwn2Own watch

Grader should cluster these with the existing carry-forward lineages, not promote as new findings unless the briefer requests a synthesis-level finding combining NGINX Rift + Pwn2Own + CVE-2026-42897 + Cisco SD-WAN T-1 + node-ipc into a "Saturday weekend posture" summary section.

## Source-health changes proposed

Propose flipping these to runtime-tracked failure_count increments (operator-set `notes` preserved verbatim where present). All are first-tracked failures this sweep — none reach the >=2-failure stale-flip threshold yet:

- **sophos**: First soft fail in source-health (news.sophos.com/en-us/feed/ 404). The sophos source-grades entry uses base news.sophos.com URL without explicit feed path — feed path may have changed. Increment failure_count; retry next sweep; mark stale if 2 more consecutive failures.
- **volexity**: XML parse error (malformed body). Increment failure_count; retry next sweep.
- **bitdefender**: Second consecutive 404 (also seen 06:00 FLASH per FLASH sentinel raw-2026-05-16-flash-0600-000). The provisional-A entry (`bitdefender` in source-grades.yaml) lists both businessinsights.bitdefender.com and bitdefender.com/blog/labs URLs — feed path may have moved. Increment failure_count; recommend operator path re-discovery.
- **industrialcyber-co**: 403 bot-block. Increment failure_count; retry next sweep.
- **symantec** (security.com/threat-intelligence): 404 this sweep on /feed suffix. First soft fail — base URL works for WebFetch, feed path needs verification. Increment failure_count.
- **wiz-research** (wiz.io/blog): 404 on /rss.xml suffix. First soft fail — base blog URL works, feed path needs verification. Increment failure_count.
- **socket** (socket.dev/blog): 404 on /rss.xml suffix. First soft fail — base blog URL works, feed path needs verification. Increment failure_count.

None of these are load-bearing for the morning brief (A-grade primary set CISA / MSRC web / vendor PSIRT / Mandiant / Talos / Unit 42 / Securelist / Sophos via prior sweeps / ESET / Recorded Future / SecurityWeek / SANS ISC / Rapid7 all returned cleanly OR have known workarounds). Operator action recommended on next maintenance pass: feed-path re-discovery for Sophos, Bitdefender, Symantec security.com, Wiz Research, Socket; XML diagnostic for Volexity; bot-bypass strategy for Industrial Cyber.

## Conclusion

**Quiet Saturday morning sweep, 2 raw signals written (1 from 06:00 FLASH + 1 new), 0 FLASH candidates for grader fast-path.** 30th consecutive dormant non-self-telemetry Splunk sweep. All 6 carry-forward items checked; no new exploitation signals; no embargo lifts; no surprise vendor disclosures. Source-health 7 soft fails proposed for failure_count increment, no stale flips yet.
