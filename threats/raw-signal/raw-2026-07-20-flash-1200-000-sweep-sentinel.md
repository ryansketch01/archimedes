---
raw_id: raw-2026-07-20-flash-1200-000
collected_at: 2026-07-20T12:15:00-04:00
run_id: flash-sweep-20260720-120000
collection_mode: flash_sweep
source:
  source_yaml_id: multiple
  source_name: "FLASH alert sweep coverage sentinel (12:00 EDT)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_sweep, coverage_record, non_flash, one_non_flash_raw_signal]
iocs_extracted: false
iocs_count: 0
text_word_count: 620
promoted: false
ttl_expires_at: 2026-10-18T12:15:00-04:00
---

# FLASH sweep coverage record — 2026-07-20 12:00 EDT

**Outcome: 0 FLASH candidates, 0 triggers matched.** One net-new non-FLASH
grader/vuln-tracker queue item written (raw-2026-07-20-flash-1200-001 —
SonicWall SMA1000 zero-days). 12:00 is INSIDE active hours (09:00–21:00 EDT),
so a FLASH would have posted immediately — none generated, nothing posted or queued.

Window: ~2026-07-20T06:00 → 12:00 EDT (6h primary). Prior sweep of record:
2026-07-20 06:00 FLASH (2 candidates promoted, 0 posts — ServiceNow CVE-2026-6875
+ wp2shell absorbed to 08:00 morning brief per the commit log). Monday midday.

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- **bleepingcomputer** — 4 items in window (15 in feed; last_modified 2026-07-20T15:57 GMT).
  All evaluated, none matched watchlist/roster/vuln-index:
  (1) "An AI SOC Evaluation Guide" — sponsored (Prophet Security), filtered.
  (2) "Hugging Face warns an autonomous AI agent hacked its network" — internal
  datasets + credentials accessed via autonomous AI-agent system. Notable AI-security
  story but NO A&D entity, NO roster actor, NO tracked CVE. Discarded per Mode 2
  (no watchlist/roster/vuln-index hit). Flagged here for orchestrator awareness only.
  (3) "Microsoft confirms WSUS sync delays" — operational/reliability, not a threat. Discard.
  (4) "Windows KB5121767 OOB update fixes Dell shutdowns" — patch-quality, not a threat. Discard.
- **securityweek** — 7 items in window (10 in feed; last_modified 2026-07-20T15:12 GMT).
  Evaluated: Neo $100M funding (filtered); OpenSSL "HollowByte" DoS silently fixed
  (DoS-only, no RCE, no ITW — discard); "New Index Tracks Material Breaches"
  (resource/journalism — discard); Ernst & Young data breach (not A&D/roster — discard);
  Cloud & Data Security Summit (event — discard); Capital One "VulnHunter" open-source
  tool (tool release — discard). ONE item retained → SonicWall SMA1000 zero-days
  (CVE-2026-15409/-15410, UTA0533/Volexity) → raw-2026-07-20-flash-1200-001 as
  **non-FLASH** grader/vuln-tracker queue item (see trigger disposition below).
- **the-record** — 3 items in window (5 in feed): South Korea diplomatic-academy
  training-system breach (9-month intrusion, unidentified hackers, no roster
  attribution, not A&D — discard); Romania land-registry cyberattack (not A&D, no
  actor — discard); Craneware US-hospital software-provider breach (not A&D, no
  roster — discard). None matched.

Authoritative CVE surface:
- **cisa-kev** (JSON, direct WebFetch) — NO entries dated 2026-07-18, 07-19, or 07-20.
  Most recent adds remain 2026-07-16 (SharePoint CVE-2026-58644 VT-041; FortiSandbox
  CVE-2026-25089 + CVE-2026-39808) and 2026-07-15 (Oracle EBS CVE-2026-46817 VT-043;
  KNX). No new KEV additions this window. Confirmed SonicWall CVE-2026-15409/-15410
  are already KEV-listed since 2026-07-14 (n-day, not net-new to KEV).

First-party (Splunk, Frank; reachable):
- **Trigger-3 sweep** (index=archimedes OR index=defenseclaw_local, excluding
  Archimedes' own operation/scheduler self-telemetry, -24h): **0 events** — no
  tracked-IOC hits. Visibility-bounded null, no bonus.

Not queried this sweep (FLASH-fast scope / prior stale): mandiant (stale since
2026-06-13, RSS 404), msrc (stale since 2026-05-30, feed parse error), ars-security
(stale since 2026-05-09). No stale-source retry attempted this FLASH window.

## FLASH trigger evaluation

All 6 triggers evaluated against in-window items — none matched:
- **T1 critical-CVE-exploited:** no net-new CVSS≥9.0 + active-exploitation + A-grade.
  SonicWall SMA1000 pair is actively exploited but n-day (patched + KEV-listed 07-14,
  6 days old; CVSS not established ≥9.0 this sweep) — not a fresh disclosure; non-FLASH.
- **T2 tracked-actor-attribution:** UTA0533 (Volexity) NOT in `_roster.yaml`; no new
  attribution to any tracked actor.
- **T3 first-party-IOC-hit:** no Splunk telemetry hits (null, see above).
- **T4 tracked-actor-TTP-change:** none net-new (UTA0533 not tracked).
- **T5 A&D-sector-campaign:** no named A&D victim / no multi-victim A&D campaign net-new.
- **T6 zero-day-no-patch:** none net-new (SonicWall patched 07-14).

## Standing watch items — no A-grade escalation this window

- **ServiceNow CVE-2026-6875** (06:00 06:00 sweep, B2/likely, absorbed to morning brief):
  no new A-grade exploitation leg this window. Quiet.
- **wp2shell / WordPress core CVE-2026-63030** (VW-001, ITW, absorbed to morning brief):
  no new escalation (no named A&D victim, no new mass-exploitation telemetry). Quiet.
- **VT-041 SharePoint CVE-2026-58644 / FortiSandbox CVE-2026-25089+39808** (KEV deadlines
  past-due 07-19): no new signal. A passing KEV deadline is not a trigger. Quiet.
- **Oracle EBS CVE-2026-46817** (VT-043, KEV past-due 07-18): no new attribution, no
  named A&D victim, no exploitation-state flip. Quiet.

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no new
failures, no recoveries. mandiant/msrc/ars-security carry prior stale state (not
retried this FLASH-fast sweep). No runtime-field changes warranted; no edit to
source-health.yaml this sweep.
