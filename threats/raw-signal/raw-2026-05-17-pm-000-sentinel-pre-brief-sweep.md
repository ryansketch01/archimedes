---
raw_id: raw-2026-05-17-pm-000
collected_at: 2026-05-17T15:32:00-04:00
run_id: pre-brief-20260517-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-self
  source_name: "Archimedes collector — pre-brief sweep sentinel"
  source_url: null
  published_at: 2026-05-17T15:32:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, pre_brief, dedup_audit, sunday_quiet]
triage_tags:
  - sentinel
  - non_flash
  - dedup_audit
  - splunk_self_telemetry_only
  - dormant_splunk_sweep_37
  - sunday_pattern
  - cve_2026_20182_kev_t_0_today_pm
  - cve_2026_42897_kev_t_12d
  - symantec_provisional_a_clock_fired_21h_ago
iocs_extracted: false
iocs_count: 0
text_word_count: 1480
promoted: false
promoted_note: "Sentinel tombstone — non-promotable per established precedent. Tycoon2FA referenced in sentinel body was promoted to finding-2026-05-17-0002 via primary raw-signal raw-2026-05-17-pm-001. This sentinel file is a coverage-decision-deferred tombstone, NOT a rejection-log candidate."
graded_at: 2026-05-17T16:08:00-04:00
graded_by_run: afternoon-20260517-160000
ttl_expires_at: 2026-08-15T15:32:00-04:00
---

# Pre-brief sweep sentinel — 2026-05-17 15:30 EDT (Sunday)

**Window:** 2026-05-17 07:30 EDT → 2026-05-17 15:32 EDT (~8h)
**Prior sweeps inside or overlapping this window:**
- 2026-05-17 07:30 EDT pre-brief (clean sweep, 0 items survived filter, 35th consecutive dormant Splunk sweep, Tycoon2FA / Grafana / Dark Reading deferred; raw-2026-05-17-am-000; commit c8a140d)
- 2026-05-17 12:00 EDT scheduled FLASH (clean sweep, 0 triggers, 36th consecutive dormant Splunk sweep, THN NGINX framing + Tycoon2FA both flagged for 16:00 grader, did NOT FLASH-fire; raw-2026-05-17-flash-1200-000; commit 8a4d2de)

**Quiet hours:** INACTIVE. 15:30 EDT well inside the 09:00–21:00 active window.

**Catchup-window load this pre-brief:** the 12:00 FLASH sweep already cleared the bulk of the 07:30 → 12:00 segment; this pre-brief covers the gap 12:00 → 15:32 (~3.5h fresh window) plus a full re-pass of the priority sources to catch items that drifted in.

---

## Sources queried (this pre-brief sweep)

| Source | Status | Items in 8h window | Notes |
|---|---|---|---|
| CISA Advisories (`cisa-advisories`, RSS all.xml) | OK 200 | 0 | 30 items in feed total, all pre-window |
| CISA KEV (`cisa-kev`, JSON via WebFetch) | OK | 0 new entries | catalogVersion 2026.05.15, dateReleased 2026-05-15T16:55:06Z (UNCHANGED from 07:30 + 12:00 sweeps). Top entries: CVE-2026-42897 (Exchange OWA XSS, dateAdded 2026-05-15, due 2026-05-29 / **T-12d**), CVE-2026-20182 (Cisco Catalyst SD-WAN auth bypass, dateAdded 2026-05-14, due 2026-05-17 / **T-0 TODAY**). KEV has NOT yet emitted a T-0-day catalog refresh on CVE-2026-20182 — the deadline arrives on a Sunday and the typical KEV cadence is weekday business hours. |
| The Hacker News (`thehackernews`, RSS) | OK 200 | 0 | last_modified 2026-05-17T16:03:06 GMT = 12:03 EDT, server-fresh; 50 items in feed, all dated <= 2026-05-17 morning (12:00 FLASH already evaluated the morning THN items including the 07:57 EDT NGINX Rift "exploited in the wild" framing item which was flagged as B-grade-VulnCheck-scoped-claim deferred to 16:00 grader, NOT FLASH-fired). No fresh post-12:00 EDT THN items in the 3.5h gap window. |
| BleepingComputer (`bleepingcomputer`, RSS) | OK 200 | **1** | last_modified 2026-05-17T19:20:36 GMT = 15:20 EDT server-fresh. One in-window item: Tycoon2FA / device-code phishing / Microsoft 365 (Bill Toulas byline, 2026-05-17T14:43:10 UTC = 10:43 EDT). This is the same item the 12:00 FLASH sweep already flagged for the 16:00 grader as a possible defensive-TTP note candidate. Discrete raw-signal written this pre-brief: raw-2026-05-17-pm-001-bleepingcomputer-tycoon2fa-device-code-phishing.md. Item disposition is grader's decision, not collector's. |
| SecurityWeek (`securityweek`, RSS) | OK 200 | 0 | last_modified 2026-05-16T12:45:50 GMT = 08:45 EDT, pre-window. 10 items in feed, all pre-window. |
| Krebs on Security (`krebs`, RSS) | OK 200 | 0 | last_modified 2026-05-13, multi-day Krebs cadence (normal for Sunday weekend). |
| The Record (`the-record`, RSS) | OK 200 | 0 | 5 items in feed, all pre-window. |
| Unit 42 (`unit42`, RSS feedburner) | OK 200 | 0 | last_modified 2026-05-15T18:38:01 GMT, pre-window. |
| Recorded Future (`recorded-future`, RSS) | OK 200 | 0 | last_modified 2026-05-15T14:00:45 GMT, pre-window. |
| ESET WeLiveSecurity (`eset`, RSS) | OK 200 | 0 | 100 items in feed, all pre-window. |
| SANS ISC (`sans-isc`, RSS rssfeed.xml) | OK 200 | 0 | last_modified 2026-05-17T19:29:04 GMT = 15:29 EDT, server-fresh; 10 items in feed, all pre-window (no fresh weekend storm-center diary entries). |
| Volexity (`volexity`, RSS) | OK 200 | 0 | last_modified 2026-05-13T20:25:24 GMT, pre-window. Multi-day cadence; no CVE-2026-42897 Exchange second-corpus citation surfaced this sweep. |
| Cisco Talos blog index (`cisco-talos`, WebFetch fallback after persistent RSS 404) | OK | 0 | RSS endpoint blog.talosintelligence.com/rss/ returned `last_modified: null` and 0 items in-window from fetch_feed (same as prior 17:30 / 00:00 / 06:00 / 07:30 / 12:00 sweeps — FIFTH consecutive feed failure). Blog index WebFetch reachable; three most recent posts confirmed dated 2026-05-14 12:02 (CVE-2026-20182 SD-WAN ongoing exploitation), 2026-05-14 14:00 (Martin Lee newsletter — AI & vulnerability discovery), 2026-05-13 06:00 (Philippe Laulheret profile). **No 2026-05-16 or 2026-05-17 Talos posts.** No T-0-day UAT-8616 update on CVE-2026-20182. |
| CrowdStrike (`crowdstrike`, RSS) | OK 200 | 0 effective (10 items returned dateless; same 15+-consecutive-sweep marketing-content pattern) | last_modified 2026-05-17T06:08:55 GMT = 02:08 EDT server-fresh. Content unchanged from prior sweeps — top items remain MQ-marketing / financial-services-report / patch-Tuesday-rollup / CORDIAL SPIDER + SNARKY SPIDER Falcon Shield product post (both adversaries off-roster). No CVE-2026-42897 second-corpus citation. No CVE-2026-20182 attribution material. Dateless feed prevents since-filter; treated as pre-window via content review. |
| Microsoft Security Blog (`mstic`) | RSS parse error (recurrent) | n/a | msrc.microsoft.com/blog/feed XML parse failure recurs (known intermittent issue; 4th observed across sweeps). Blog index out-of-window via WebFetch surface check; no fresh MSTIC post on CVE-2026-42897 Exchange exploitation. No second-corpus corroboration of Symantec/SentinelLABS Fast16 surfaced from MSTIC. |
| Mandiant (`mandiant`) | feedburner 404 (~21st consecutive) | n/a | Carried in expected-broken state per source-health.yaml. No Mandiant Cloud blog WebFetch surface check this sweep. |
| Cloud.google.com threat intelligence (`mandiant`, alt) | RSS parse error | n/a | cloud.google.com/blog/topics/threat-intelligence/rss returned XML parse error — same path-fragility as prior surfaces. |
| Dragos (`dragos`) | known broken | n/a | /blog/feed/ 404 in source-health; carried in expected-broken state. |
| Bitdefender Labs (`bitdefender`) | path-discovery 404 | n/a | businessinsights.bitdefender.com/rss 404; second failure_count increment. No fresh Bitdefender Labs research observed via alt surfaces. |
| Symantec security.com (`symantec`) | symantec-enterprise-blogs feed 404 | n/a | Same path-discovery issue as 2026-05-16 + 07:30 sweep; no surfacing of second-corpus citation of Symantec/SentinelLABS Fast16 from Symantec's own current surface. |
| Wiz Research (`wiz-research`) | feed.xml 404 | n/a | Same path-discovery issue as prior sweeps. |
| Socket (`socket`) | blog/rss.xml 404 | n/a | Same path-discovery issue as prior sweeps. |
| Sophos (`sophos`) | 404 (stale_since 2026-05-17) | n/a — stale | Skipped per under-24h-stale rule (stale_since=2026-05-17; eligible-to-retry rule fires 2026-05-18+). |
| Mandiant Google Cloud (`mandiant`) | 404 / parse error | n/a | Both feedburner and cloud.google.com paths failed this sweep. No second-corpus citation of CVE-2026-20182 / CVE-2026-42897 / Symantec Fast16 surfaced via Mandiant. |
| Industrial Cyber (`industrialcyber-co`) | **403 Akamai WAF/bot-block** | n/a | Recurrent pattern; no change in posture from prior sweeps. `industrialcyber.co/feed/` consistently 403s. |
| Sentinel Labs (`sentinelone`, RSS) | not re-tested this sweep | n/a (sentinel cadence multi-day; 07:30 + 12:00 already covered) | Carry-context: last_modified 2026-05-15T19:30 UTC, pre-window across SEVEN+ consecutive sweeps. SentinelLABS publication cadence is multi-day; Fast16 second-corpus citation would surface via Symantec primary surface first. |
| Dark Reading (`darkreading`, RSS via fetch_feed) | OK 200 | 1 (same future-dated 2026-05-18 "Boring Stuff" opinion piece evaluated and discarded at 07:30 sweep — anti-noise applies, not re-evaluated) | last_modified 2026-05-17T19:31:50 GMT. The 2026-05-18T13:00 UTC future-scheduled article remains the only in-window item; failed A&D / roster / vuln-index filter at 07:30 sweep and re-application yields same disposition. |
| ZDI Pwn2Own blog (`zdi-blog`, RSS) | OK 200 | 0 | 20 items in feed, all pre-window. WebFetch confirms three most recent posts are 2026-05-16 Day Three / 2026-05-15 Day Two / 2026-05-14 Day One — all already in corpus (raw-2026-05-15-pm-002 + raw-2026-05-16-am-001). No new ZDI blog posts since 2026-05-16 morning. Pwn2Own Berlin Day 2 Exchange RCE-to-SYSTEM chain remains under standard 90-day vendor-coordinated-disclosure embargo through ~2026-08-13. |
| Splunk first-party (`splunk-archimedes`, `splunk-defenseclaw`) | OK | 0 non-self-telemetry events | **37th consecutive dormant non-self-telemetry sweep** — see Splunk section below. |
| x-cisagov | stale (nitter bridge fragility) | skipped per source-health | <24h since stale_since=2026-05-10; bridge-pool decision still pending operator. |
| x-gossithedog | stale (nitter delisted) | skipped per source-health | |
| ars-security | stale (feed retired) | skipped per source-health | Workaround: arstechnica.com/feed root works but security-only is retired. |

---

## Splunk self-telemetry sweep

`index=archimedes OR index=defenseclaw_local NOT sourcetype=archimedes:* earliest=-8h` returned 0 events. mcp__splunk-query__health returned reachable=true, version 10.2.2 / Frank / license OK.

**Zero non-self-telemetry events. 37th consecutive dormant non-self-telemetry Splunk sweep.** Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`. Trigger 3 (first-party-ioc-hit) cannot fire on a dormant non-archimedes-event stream.

---

## Single in-window BleepingComputer item raw-signaled (NOT graded)

**BleepingComputer (2026-05-17T14:43:10 UTC = 10:43 EDT): "Tycoon2FA hijacks Microsoft 365 accounts via device-code phishing"**

- Author: Bill Toulas. Primary originating research: **eSentire** (BleepingComputer relays vendor findings).
- Discrete raw-signal file: `raw-2026-05-17-pm-001-bleepingcomputer-tycoon2fa-device-code-phishing.md`.
- Carry-forward from 12:00 FLASH evaluation: flagged as possible defensive-TTP note candidate for the 16:00 afternoon brief; FLASH-fire failed all 6 triggers (commodity criminal PhaaS, no tracked roster actor, no A&D entity, no CVE).
- Grader/briefer decision territory, not collector's. Collector raw-signals the item per Mode 1 procedure (BleepingComputer is a healthy active source; the item is fresh and unambiguous) and lets the downstream grader apply the defensive-TTP-note disposition or rejection.

---

## Carry-forwards preserved (NOT re-collected)

Per orchestrator scope this pre-brief — watch for new developments but do NOT re-collect existing topics:

1. **CVE-2026-20182 Cisco Catalyst SD-WAN auth bypass (CVSS 10.0, CISA KEV).** Federal patch deadline **TODAY 2026-05-17** (T-0). Watched this sweep for late-disclosure exploitation, attribution updates, or KEV catalog refresh: **zero new items.** KEV catalogVersion 2026.05.15 still unchanged across 07:30 + 12:00 + 15:32 sweeps. Cisco Talos blog no new post since 2026-05-14 12:02. SecurityWeek + BleepingComputer + The Hacker News + The Record + Krebs + Recorded Future + Unit 42 all 0 in-window items on this topic.

2. **CVE-2026-42897 Microsoft Exchange OWA XSS (CISA KEV, due 2026-05-29).** T-12d to federal patch deadline. >48h single-source veto active on exploitation-claim layer per orchestrator scope. Watched for Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike second-corpus corroboration: **zero new items.** Volexity feed reachable but pre-window. MSTIC parse error. Mandiant 404. Unit 42 pre-window. CrowdStrike dateless marketing content.

3. **CVE-2026-42945 NGINX Rift PoC carry-forward** (depthfirst GitHub repo per finding-2026-05-16-0001). Hard Rule 3 prevents repo URL linking. The Hacker News 07:57 EDT "exploited in the wild" framing item already flagged at 12:00 FLASH as VulnCheck-honeypot-scanner-class B-grade scoped claim, deferred to 16:00 grader as CVE-2026-42945 carry-forward refinement. Watched this 3.5h gap window for A-grade attestation of confirmed production exploitation: **zero new items.** No vendor advisory updates from F5 or NGINX maintainers.

4. **Symantec/SentinelLABS Fast16 (2005-era pre-Stuxnet simulation-sabotage research targeting LS-DYNA + AUTODYN).** Provisional-A ratification clock fired 2026-05-16T18:25 EDT — currently **T+21h07m** past elapsed deadline. Watched this sweep for second-corpus citations: **zero new corpus citations** of the Fast16 research from any A/B-grade source. Single-source veto at finding-2026-05-16-0003 remains in effect (capped at "likely" WEP). Awaiting operator pass on ratification — outside collector scope per orchestrator informational-only flag.

5. **Pwn2Own Berlin closure carry-forward** (raw-2026-05-16-am-001; $943,250 total / 42 zero-days; Day 2 Orange Tsai DEVCORE Exchange RCE-to-SYSTEM chain under standard 90-day embargo through ~2026-08-13). No new ZDI blog posts in 8h window.

6. **Turla/Kazuar D+2 relay layer duplicate-lock** (finding-2026-05-14-0006 / reject-2026-05-16-0001). No new Turla / Kazuar surfacing this sweep. Anti-noise rule 1 remains active. **Not re-collected.**

7. **Tycoon2FA device-code phishing** (BleepingComputer 10:43 EDT). Raw-signaled this sweep as discrete raw-signal per BleepingComputer being a healthy active source and the item being fresh; disposition (defensive-TTP note vs. discard) is grader/briefer territory.

---

## Source health observations (this sweep)

Runtime state changes proposed for `infrastructure/source-health.yaml` (operator-set `notes:` preserved verbatim):

- **`bleepingcomputer`**: healthy. Fetch successful; 1 in-window item (Tycoon2FA) raw-signaled discretely. `last_successful_fetch` updates to 2026-05-17T15:32:00-04:00. `failure_count` remains 0.

- **`thehackernews`**: healthy. Fetch successful; 0 in-window items in 3.5h gap (since 12:00 FLASH). `last_successful_fetch` updates to 2026-05-17T15:32:00-04:00.

- **`securityweek`**: healthy. Fetch successful; 0 in-window items. `last_successful_fetch` updates to 2026-05-17T15:32:00-04:00.

- **`the-record`**, **`krebs`**, **`cisa-advisories`**, **`cisa-kev`**, **`unit42`**, **`recorded-future`**, **`eset`**, **`sans-isc`**, **`volexity`**, **`darkreading`**, **`zdi-blog`**: all reachable, 0 in-window items. `last_successful_fetch` updates to 2026-05-17T15:32:00-04:00 (where applicable; existing operator-set `notes` preserved).

- **`cisco-talos`**: continued RSS-endpoint failure (FIFTH consecutive sweep observation). Fetched via fetch_feed: 200 OK but `last_modified: null` and 0 items in-window. Blog index WebFetch alt-path verifies working and confirms latest post date 2026-05-14 12:02. Same operator-decision-pending posture as 07:30 sweep — recommend operator confirm formal stale flip or path-replacement decision. `failure_count` should increment to 5 to reflect cumulative same-class observations; `last_error` updated to reflect the fifth-consecutive feed-empty observation.

- **`splunk-archimedes`**, **`splunk-defenseclaw`**: both healthy; 37th consecutive dormant non-self-telemetry sweep. `last_successful_fetch` updates to 2026-05-17T15:32:00-04:00.

- **`industrialcyber-co`**: 403 Akamai WAF/bot-block recurs. Already at failure_count=1 from 2026-05-16 07:30. Increment to 2 brings it to ≥2 stale-flip threshold. Hold healthy this sweep ONLY pending operator-side feed-path resolution; recommend operator review.

- **`bitdefender`**, **`symantec`**, **`wiz-research`**, **`socket`**, **`mandiant`**, **`mstic`** (msrc), **`dragos`**: same path-discovery / feedburner / parse-error issues observed across prior sweeps. No new operator-actionable signal this sweep; flag for systematic feed-path remediation pass.

- All other queried sources: reachable or in known expected-broken/stale state per source-health.yaml; no changes proposed.

---

## Disposition

**Single in-window item raw-signaled (BleepingComputer Tycoon2FA / device-code phishing).** Item is FLASH-trigger-negative (already evaluated at 12:00 FLASH sweep; all 6 triggers fail), defensive-TTP note candidate for 16:00 briefer per orchestrator scope. Disposition (note vs. discard) is grader/briefer territory, not collector's.

**Zero new items survive A&D / roster / vuln-index filter this sweep on standing carry-forward topics** — CVE-2026-20182 SD-WAN T-0 calendar event arrives TODAY with no fresh exploitation reporting, vendor patch updates, federal compliance commentary, or KEV catalog refresh in the 8h window; CVE-2026-42897 Exchange OWA XSS T-12d with no second-corpus exploitation corroboration; NGINX Rift PoC carry-forward with no A-grade confirmed-production-exploitation attestation; Symantec/SentinelLABS Fast16 with no second-corpus citation 21h past elapsed ratification clock; Pwn2Own Berlin closure with no new ZDI surfacing; Turla/Kazuar duplicate-locked.

**37th consecutive dormant non-self-telemetry Splunk sweep.** Quiet-hours INACTIVE (15:30 inside 09:00–21:00 active window). 16:00 afternoon brief publication is in ~28 minutes.

**Source-health runtime updates queued for `infrastructure/source-health.yaml`:** bleepingcomputer / thehackernews / securityweek / the-record / krebs / cisa-advisories / cisa-kev / unit42 / recorded-future / eset / sans-isc / volexity / darkreading / zdi-blog last_successful_fetch refresh to 2026-05-17T15:32:00-04:00; cisco-talos failure_count++ to 5 with last_error updated to reflect FIFTH consecutive feed-empty observation; splunk-archimedes + splunk-defenseclaw last_successful_fetch refresh + 37th-dormant-sweep notation append. Operator-set `notes:` fields preserved verbatim per Hard Rule field-ownership doctrine.
