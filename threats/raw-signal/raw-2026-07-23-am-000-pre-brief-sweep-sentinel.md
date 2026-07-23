---
raw_id: raw-2026-07-23-am-000
collected_at: 2026-07-23T07:33:00-04:00
run_id: pre-brief-20260723-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: "Pre-brief collection coverage sentinel (07:30 EDT)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-16232]
  keywords: [pre_brief, coverage_record]
triage_tags: [pre_brief, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 640
promoted: false
ttl_expires_at: 2026-10-21T07:33:00-04:00
---

# Pre-brief collection coverage record — 2026-07-23 07:30 EDT (feeds 08:00 morning brief)

Window: ~2026-07-22T17:30 → 2026-07-23T07:30 EDT (14h lookback). Prior sweep of
record: 2026-07-23 06:00 FLASH (clean — commit 3688ac2). This pre-brief produced
**2 substantive raw-signal files** (am-001, am-002), both UPDATE / state-change
enrichments of tracked topics already carried in the 2026-07-22 afternoon brief —
grader to apply anti-noise and fold as UPDATE items rather than net-new findings.

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- **bleepingcomputer** — 4 items in window (15 in feed; last_modified
  2026-07-23T11:30 GMT). (1) Check Point SmartConsole zero-day CVE-2026-16232 —
  vendor advisory + patch + 5 IOC IPs [TRACKED CVE; net-new vendor advisory + atomic
  IOCs → **raw-signaled am-001**]; (2) msaRAT / Chaos ransomware gang browser-C2-routing
  backdoor [Chaos NOT a roster actor, no A&D, no tracked CVE — DISCARDED per Mode 1];
  (3) Microsoft Exchange Online mailbox-quarantine operational issue [MS service bug,
  no exploit — DISCARDED]; (4) Upbound/Acima $13M fraudulent-lease breach fallout
  [fintech breach, no A&D / no roster actor / no CVE — DISCARDED].
- **securityweek** — 4 items in window (10 in feed; last_modified 2026-07-23T10:49
  GMT). (1) Upbound Group data breach [same as BleepingComputer #4 — DISCARDED];
  (2) Assaf Keren appointed Meta CISO [personnel — DISCARDED]; (3) Check Point
  CVE-2026-16232 exploited ITW [same TRACKED CVE as BC #1 — corroborating source,
  folded into am-001]; (4) US warns Iranian hackers targeting Siemens/Schneider/Rockwell
  ICS — updated CISA/FBI/EPA advisory naming CyberAv3ngers + Handala [TWO roster actors
  #028 + #014 + Iran-cyber standing section → **raw-signaled am-002**].
- **the-record** — 1 item in window (5 in feed). Stadler Rail refuses Everest $12.3M
  ransom [Swiss train maker; Everest NOT roster; no A&D prime; no tracked CVE —
  DISCARDED per Mode 1].
- **sans-isc** — 1 item in window: ISC Stormcast podcast (Thu Jul 23) [podcast detail,
  no body content, no threat-intel claim — DISCARDED].
- **krebs** — 0 items in window.
- **unit42** (feedburner) — 0 items in window (feed last_modified 2026-07-20).
- **mstic** (parent feed) — 0 items in window (feed last_modified 2026-07-22T16:00).
- **rapid7** — 0 items in window.
- **sentinelone** (blog feed) — 0 items in window (feed last_modified 2026-07-22).
- **cisa-advisories** (all.xml) — 0 items in window (30 in feed; the 2026-07-22 Iran
  OT advisory revision is pre-window on this feed; media relays surfaced it in-window).

Authoritative CVE surface:
- **cisa-kev** (evaluated via the two in-window vendor/media items): no net-new KEV
  adds dated 2026-07-23 surfaced through the media feeds. Most recent KEV adds remain
  the two 2026-07-22 entries (CVE-2026-16232 Check Point SmartConsole, dueDate
  2026-07-25; CVE-2026-50522 SharePoint). No KEV delta this window.

First-party (Splunk, Frank; reachable):
- **Targeted IOC sweep** on the 5 net-new Check Point advisory IPs (151.241.99.207,
  151.241.99.233, 158.62.198.182, 192.142.10.99, 139.28.37.250) across
  index=archimedes OR defenseclaw_local, NOT archimedes:*, over -90d → **0 hits**.
  Visibility-bounded null, no Trigger-3 fire.

Not queried (stale, not retried this pre-brief-fast window): mandiant (stale since
2026-06-13, RSS 404 — direct-HTML path working per prior notes), msrc (stale since
2026-05-30, parse error), ars-security (stale since 2026-05-09, security-path 404).

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no new
failures, no recoveries. mandiant/msrc/ars-security carry prior stale state (not
retried this pre-brief-fast sweep). No runtime-field changes this run; source-health.yaml
last_updated + last_successful_fetch refresh only (no stale/error transitions).
