---
raw_id: raw-2026-06-14-am-000
collected_at: 2026-06-14T07:31:30-04:00
run_id: pre-brief-20260614-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: sentinel-internal
  source_name: "Pre-brief sweep sentinel (internal)"
  source_url: null
  published_at: 2026-06-14T07:31:30-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [pre_brief_sweep_documented, source_health_state, anti_noise_state]
triage_tags: [non_flash, sentinel, sweep_documented, pre_brief_audit_trail]
iocs_extracted: false
iocs_count: 0
text_word_count: 1180
promoted: false
ttl_expires_at: 2026-09-12T07:31:30-04:00
---

# Pre-brief sweep 2026-06-14 07:30 EDT — sentinel + audit trail

## Sweep parameters

- Mode: `pre_brief_collection`
- Time window: 2026-06-13T17:30:00-04:00 → 2026-06-14T07:31:30-04:00 (14h)
- Carry-forward context: 06:00 FLASH sweep (raw-2026-06-14-flash-0600-000) was clean; 0 candidates, 0 triggers. PM brief commit dc85aae published 2026-06-13 16:00 EDT.
- Sources queried this sweep:
  - **Tier-1 vendor research:** Mandiant cloud.google.com direct-HTML index (RSS feedburner stale), Unit 42 feedburner, MSTIC parent feed, SentinelLabs, Rapid7, Cisco Talos (recovered today via /rss/ endpoint — was 404 at 06:00), Check Point Research, Wiz Research (404), Bitdefender (404), Cybereason, DFIR Report, Sygnia, ZDI, Tenable, Snyk, ESET WeLiveSecurity, Proofpoint (404 4th consecutive)
  - **Security media:** BleepingComputer, The Hacker News, SecurityWeek, SecurityAffairs, Krebs, The Record, SANS-ISC, DarkReading, The Register security, Help Net Security, CyberScoop
  - **Government / advisory:** CISA all.xml Atom feed, CISA KEV JSON
  - **Vulnerability databases:** NVD lastModified CRITICAL window query
  - **First-party telemetry:** Splunk archimedes + defenseclaw_local indexes (Hard Rule 8 sentinel sweep, -14h window)
- Sources skipped (stale, <24h since stale_since per under-24h rule): volexity, msrc, lumen, shadowserver, sophos, industrialcyber-co, ars-security, trellix, x-cisagov, x-gossithedog, censys, urlscan, hibp
- Sources skipped (stale, retried per >=24h rule): mandiant feedburner (retried, still 404 — 27th consecutive failure)

## Items in window — summary table

| Source | In-window items | Disposition |
|---|---|---|
| BleepingComputer | 0 | — feed empty, last entry pre-window |
| The Hacker News | 0 | — feed empty, last entry pre-window |
| SecurityWeek | 0 | — feed empty, last entry Sat 13 Jun 15:54 GMT pre-window |
| **SecurityAffairs** | **1** | **SecurityAffairs Conti/Lytvynenko DOJ plea — RAW-SIGNALED to raw-2026-06-14-am-001 below** |
| Krebs | 0 | — feed empty |
| The Record | 0 | — feed empty |
| SANS-ISC | 0 | — feed reachable + parseable (recovery confirmed from 06-13 PM parse error), 0 items in 14h window |
| MSTIC | 0 | — feed last_modified Wed 10 Jun 16:00 GMT pre-window (cadence) |
| Unit 42 | 0 | — feed last_modified Fri 12 Jun 22:27 GMT pre-window |
| CISA all.xml Atom | 0 | — 30 items in feed, all pre-window |
| Help Net Security | 1 in-window | "Week in review" recap of June 8-12 stories already brief-covered; DISCARDED per Mode 1 procedure (anti-noise; pure retrospective recap with NO net-new substrate) |
| DarkReading | 1 dateless | "Name That Toon Contest" event marketing item — DISCARDED |
| The Register | 0 | — feed empty |
| ESET WeLiveSecurity | 0 | — feed empty |
| CyberScoop | 0 | — feed last_modified Sat 13 Jun 18:30 GMT pre-window by 30 min |
| SentinelLabs | 0 | — feed last_modified Sat 13 Jun 00:39 GMT pre-window |
| Rapid7 | 0 | — feed empty |
| **Cisco Talos** | 0 in-window | **/rss/ endpoint RECOVERED this sweep (was 404 at 06:00) — 15 items in feed, all pre-window. Soft-recovery confirmed; matches the 2026-05-24 PM brief recovery pattern when /rss/ replaced the deprecated /feeds/posts/default Atom endpoint.** |
| Check Point Research | 0 | — feed last_modified Thu 11 Jun 13:47 GMT pre-window |
| Cybereason | 0 | — feed last_modified Wed 10 Jun 17:24 GMT pre-window |
| DFIR Report | 0 | — feed last_modified Tue 12 May 13:00 GMT pre-window (multi-day cadence) |
| Sygnia | 0 | — feed last_modified Thu 11 Jun 15:06 GMT pre-window |
| ZDI | 0 | — feed empty |
| Tenable | 0 | — feed empty |
| Snyk | 0 | — feed empty (1637 items in feed total but none in 14h window) |
| **Proofpoint Threat Insight** | n/a | **/us/threat-insight/blog/feed 404 again (4th consecutive observation; soft-pattern entrenched). No top-level entry exists to flip.** |
| **Wiz Research** | n/a | **wiz.io/feed.xml 404 this sweep — first observation against this specific path. Source-grades.yaml lists no canonical Wiz feed URL; soft-pattern. No top-level health update applied this sweep.** |
| **Bitdefender** | n/a | **bitdefender.com/blog/feed/ 404 this sweep — first path-mismatch observation. Bitdefender has multiple publication surfaces per the source-health notes (businessinsights.bitdefender.com and bitdefender.com/blog/labs/); the /blog/feed/ root path may not be the canonical one. Soft-pattern; no health update.** |
| **NVD lastModified CRITICAL window** | 0 | **NVD REST API reachable; CVSS v3 CRITICAL query 2026-06-13T22:00 → 2026-06-14T11:30 UTC returned ZERO results. No fresh critical-severity CVEs in window.** |
| **CISA KEV catalog** | 0 new adds | **Most recent KEV add remains CVE-2026-35273 Oracle PeopleSoft (2026-06-12, dueDate 2026-06-15 ~T-36h to Sunday EOB). 6 most recent: CVE-2026-35273 (PeopleSoft 06-12), CVE-2026-10520 (Ivanti Sentry 06-11, dueDate 2026-06-14 = today EOB ~T-12h), CVE-2026-11645 (Chrome V8 06-09), CVE-2026-7473 (Arista EOS 06-09), CVE-2026-20245 (Cisco Catalyst SD-WAN 06-09), CVE-2026-42271 (BerriAI LiteLLM 06-08). Catalog has NO dateAdded=2026-06-13 OR 2026-06-14 entries.** |
| **Splunk archimedes + defenseclaw_local** | 0 non-archimedes-internal events over -14h; 0 IOC hits on 19-IOC UNC6240 sentinel set + KEV CVE-set over -24h | **Trigger 3 cannot fire; first-party telemetry remains dormant for external observations.** |

## Net-new raw-signal files written this sweep

1. **raw-2026-06-14-am-000** — this file (sentinel + audit trail)
2. **raw-2026-06-14-am-001** — SecurityAffairs Conti/Lytvynenko DOJ plea (A-grade DOJ primary cited; Conti NOT on _roster.yaml; Lytvynenko 2021-2022 attack window retrospective; sentencing 2026-09-10 max 20yr; NO A&D / NO IOC / NO CVE / NO tracked-actor — DOJ-cycle awareness item for grader's brief consideration, A&D-relevance-low)

## FLASH trigger evaluation summary

This is Mode 1 (pre-brief collection), NOT a FLASH sweep — trigger evaluation is informational only:

- **Trigger 1 (critical CVE actively exploited):** NEGATIVE in window. KEV unchanged since 2026-06-12; NVD CRITICAL window query 0 results.
- **Trigger 2 (new attribution for tracked actor):** NEGATIVE in window. SecurityAffairs Conti item is a 2021-2022 retrospective; Conti NOT on roster; no new attribution to roster-tracked actor.
- **Trigger 3 (first-party IOC hit):** NEGATIVE. Splunk sentinel sweep clean on 19-IOC UNC6240 set + KEV CVE-set over -24h.
- **Trigger 4 (tracked actor TTP change):** NEGATIVE.
- **Trigger 5 (active A&D-sector campaign):** NEGATIVE.
- **Trigger 6 (zero-day without patch):** NEGATIVE.

## Anti-noise holds active (carry-forward, per orchestrator binding + Doctrine §134-145)

The following topics from the past 48h's findings + 06:00 FLASH sentinel + 18:00 FLASH sentinel are anti-noise-held; their absence from this sweep's net-new-raw-signal count is intentional, NOT a re-evaluation:

- **PeopleSoft / UNC6240 / CVE-2026-35273** — finding-2026-06-13-0002 AM + finding-2026-06-13-0006 PM; KEV BOD 26-04 deadline 2026-06-15 (~T-36h Sunday EOB)
- **CVE-2026-20253 Splunk Enterprise** — finding-2026-06-13-0004 PM; THN coverage of the same CVE surfaced on homepage but NOT in 14h RSS window
- **NPM 12 default script-execution change** — finding-2026-06-13-0005 PM
- **Fable 5 / Mythos 5 USG export-control on Anthropic** — finding-2026-06-13-0001 AM; SecurityAffairs 4th-publisher relay (raw-2026-06-13-pm-003) already covered
- **Handala / Cal Water single-Dataminr-substrate** — finding-2026-06-13-0003 PM
- **Velvet Ant Operation Highland (Sygnia primary)** — covered 06/12 PM finding-2026-06-12-0004 + 06/13 PM reject-2026-06-13-0003 (BleepingComputer 2nd-publisher + THN 3rd-publisher relays)
- **Ivanti Sentry CVE-2026-10520** — finding-2026-06-11-0001; KEV deadline 2026-06-14 EOB (~T-12h from this sweep — CLOSES TODAY)
- **Check Point VPN CVE-2026-50751 + Qilin** — finding-2026-06-10-flash-0000-002 + 06/11 PM brief

## Splunk first-party sentinel — Hard Rule 8 + Trigger 3

Indexes queried: `archimedes`, `defenseclaw_local`. Time windows: -14h for sourcetype inventory, -24h for IOC search.

Sentinel IOC set (19 indicators): UNC6240 carry-forward — `azurenetfiles.net`, `176.120.22.24`, staging IPs `142.11.200.186-190`, Python SimpleHTTPServer:8888 pattern, Windows meshagent SHA-256 substitutes (meshagent64-azure-ops, meshagent64-v2, meshagent32-azure-ops), Linux meshagent SHA-256, `.bash_history`, `exfil.tar.zst`, `README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT` defacement marker, plus KEV-CVE cohort (CVE-2026-35273, CVE-2026-20253, CVE-2026-10520, CVE-2026-50751, CVE-2026-11645, CVE-2026-7473, CVE-2026-20245, CVE-2026-42271).

**Result over -24h: 6 hits, ALL archimedes:operation pipeline self-references** (1x flash_sweep_completed for 06:00 librarian-flash, 1x flash_sweep_completed for 00:00 sweep, 1x git_committed for dc85aae 06-13 PM brief, 1x brief_published for 06-13 PM, 1x flash_sweep_clean for 06-13 12:00 FLASH, 1x brief_published for 06-13 AM). Zero external observations. Pattern matches the consistent dormancy of non-archimedes-internal events documented across all sweeps since 2026-05-08. Frank is not a higher-ed environment consistent with UNC6240's 68% victim concentration — silent Splunk does NOT disconfirm at this substrate.

**Result over -14h sourcetype inventory (NOT sourcetype=archimedes:*):** 0 events on both indexes.

## Source-health deltas observed this sweep

- **mandiant:** feedburner.com/Mandiant RSS returned 404 again (27th consecutive failure — was on 26 at 06:00 FLASH retry; this 07:30 retry per >=24h-since-stale rule produced same outcome). `failure_count` UNCHANGED at 26 (no double-increment for retries inside the same stale period per source-health field-ownership rule). `last_attempt` advances to this sweep timestamp. Already `stale`; no status flip. Direct-HTML retrieval path on cloud.google.com/blog/topics/threat-intelligence SUCCEEDED this sweep (top-10 posts visible: GTIG AI Threat Tracker, ShinyHunters/PeopleSoft, Seeking Counsel US law firms, KnowledgeDeliver ViewState, 2 PhaaS 2 Furious, BlackFile vishing, Snow Flurries UNC6692, deSouza AI vuln post, German Überfall, vSphere/BRICKSTORM). NONE dated in the 14h window; all out-of-window or already-substrate of prior findings. Direct-HTML path now confirmed working consistently across 4 sweeps (06-13 PM, 06-14 00:00, 06-14 06:00, 06-14 07:30) — operator-note candidate "Direct-HTML path working consistently; RSS path remains stale; canonical-swap decision pending" carries forward.
- **cisco-talos:** blog.talosintelligence.com/rss/ RECOVERED this sweep (was 404 at 06:00 FLASH on the /feeds/posts/default Atom endpoint — that path remains dead). The /rss/ endpoint returned 200 OK with 15 items in feed (all pre-window). `last_successful_fetch` advances. `failure_count` stays at 0 (was already healthy on the canonical /rss/ endpoint per 2026-05-24 PM recovery). This recovery confirms the post-2026-05-24 canonical-endpoint guidance: prefer /rss/ over the deprecated /feeds/posts/default Atom path.
- **sans-isc:** rssfeed.xml reachable AND parseable AND last_modified inside window (Sun 14 Jun 11:29 GMT = 07:29 EDT just inside window from feed-server activity). `last_successful_fetch` advances. Parse-error 1/3 from 06-13 PM remains transient observation; no recurrence today.
- **proofpoint:** /us/threat-insight/blog/feed 404 again (4th consecutive observation across 06-13 PM, 06-14 00:00 + 06:00 + 07:30 sweeps; soft-pattern fully entrenched). No top-level proofpoint entry exists in source-health.yaml at the threat-insight subpath level to flip. The corporate-news /us/rss.xml endpoint is the existing healthy entry per the 2026-05-11 00:00 recovery note. Operator alt-path discovery for the threat-intel-specific surface remains an open item.
- **wiz-research:** wiz.io/feed.xml 404 this sweep (first observation of this specific path). source-grades.yaml + source-health.yaml lists no canonical Wiz feed URL; the existing entry's known-good fetch pattern is direct WebFetch on wiz.io/blog/<slug>. Soft observation only; no health update applied since no prior baseline at this path.
- **bitdefender:** bitdefender.com/blog/feed/ 404 this sweep (first path-mismatch observation). Per the 2026-05-13 source-health notes, Bitdefender has two publication surfaces (businessinsights.bitdefender.com and bitdefender.com/blog/labs/); the /blog/feed/ root path may not be canonical. Soft observation only; no health update.
- **talos legacy Atom endpoint** (blog.talosintelligence.com/feeds/posts/default): NOT retried this sweep because the /rss/ canonical endpoint already proved healthy. The Atom endpoint can be considered deprecated.
- All other healthy sources reachable with 0 in-window items. No new degradations beyond Mandiant counter advance (which stays at 26 per the no-double-increment rule) and the soft path-mismatch observations noted above.

## Carry-forward state for 08:00 morning brief (grader awareness)

- **PeopleSoft KEV BOD 26-04 deadline 2026-06-15 EOB Sunday (~T-36h)** — still in clock, no FCEB-compliance data has surfaced
- **Ivanti Sentry CVE-2026-10520 KEV deadline 2026-06-14 EOB (~T-12h from this sweep) — CLOSES TODAY** — still in clock, no FCEB-compliance data has surfaced
- **Conti DOJ plea** (raw-2026-06-14-am-001) — A-grade DOJ primary cited via SA relay; A&D-relevance-low; grader may surface as criminal-justice cycle bullet
- **HelpNet Week-in-Review recap** — pure retrospective, anti-noise-discarded
- **Cisco Talos /rss/ recovery** — recovery confirmed (was first-flagged 06:00 FLASH); no operational follow-up needed
- **Mandiant direct-HTML canonical-swap decision** — pending operator
- **Proofpoint /us/threat-insight/blog/feed 4th consecutive 404** — operator alt-path discovery pending

## Disposition

Net-new content for grader attention this window: **1 candidate** (SecurityAffairs Conti DOJ plea — raw-2026-06-14-am-001). All other in-window items either failed Mode 1 watchlist/roster/vuln-index filter (HelpNet recap, DarkReading contest) or were anti-noise-held against existing findings.

## Extraction notes

- Language: en
- Article type: sentinel (internal)
- Raw IOC extraction invoked: no (no candidate items in this sentinel file itself)
- Hard Rule binding: Rule 1 (LEGAL-POLICY) — all queries passive RSS/WebFetch/Splunk-self; Rule 8 (Splunk first-party) — sentinel Splunk scan emitted; Rule 2 (no attribution origination) — no novel attributions made this sweep
