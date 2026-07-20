---
raw_id: raw-2026-07-20-am-000
collected_at: 2026-07-20T07:33:00-04:00
run_id: pre-brief-20260720-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: "Pre-brief collection coverage sentinel (07:30 EDT, morning brief)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-6875, CVE-2026-63030]   # both in-window but anti-noise dedup vs 06:00 FLASH (already promoted)
  keywords: []
triage_tags: [pre_brief, coverage_record, non_flash, anti_noise_dedup]
iocs_extracted: false
iocs_count: 0
text_word_count: 640
promoted: false
ttl_expires_at: 2026-10-18T07:33:00-04:00
---

# Pre-brief collection coverage record — 2026-07-20 07:30 EDT (morning brief)

NO net-new substantive raw-signal written. The only two in-window watchlist/vuln
matches (ServiceNow CVE-2026-6875, wp2shell CVE-2026-63030) are the EXACT same
BleepingComputer / SecurityWeek articles already captured and promoted by the
2026-07-20 06:00 FLASH sweep — anti-noise dedup, not net-new. This sentinel is
the coverage record for the 2026-07-20 morning brief pre-brief collection.

Window: ~2026-07-19T17:30 → 2026-07-20T07:30 EDT (14h primary). The overnight
slice (18:00 → 06:00) was already swept by the 2026-07-20 00:00 FLASH (clean, 0
candidates — commit d5b9314) and 06:00 FLASH (2 candidates promoted, both
absorbed to this morning brief — commit 3198601). Net-new uncovered slice this
pre-brief was ~06:00 → 07:30 EDT plus a broad re-sweep of all healthy surfaces.
Monday morning cadence.

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- bleepingcomputer — 4 items in window (15 in feed; last_modified 2026-07-20T11:57
  GMT). Evaluated below.
- securityweek — 7 items in window (10 in feed; last_modified 2026-07-20T11:46
  GMT). Evaluated below.
- the-record — 0 items in window (5 in feed).

Authoritative CVE surface:
- cisa-kev (JSON, direct WebFetch) — catalog version 2026.07.16 (released
  2026-07-16T17:00Z). NO entries dated 2026-07-17, 07-18, 07-19, or 07-20. No
  new KEV additions this window. Standing items CVE-2026-46817 (Oracle EBS),
  CVE-2026-58644 (SharePoint), CVE-2026-25089 / CVE-2026-39808 (FortiSandbox) all
  still present with past-due deadlines — no state change. CVE-2026-6875
  (ServiceNow) and CVE-2026-63030 (wp2shell) confirmed NOT KEV-listed (KEV-add
  remains an open watch signal on both).

First-party (Splunk, Frank; reachable, v10.2.2, license OK):
- Trigger-3 / first-party-IOC sweep (index=archimedes OR index=defenseclaw_local,
  -14h): in-window events are exclusively Archimedes' own telemetry
  (archimedes:operation 6, archimedes:scheduler 8 = 14 self-audit events).
  defenseclaw_local ZERO events in-window. No tracked-IOC hits. Visibility-bounded
  null, no bonus. Trigger 3 cannot fire.

Not queried this pre-brief (stale, carry prior state; entrenched failure patterns
pending operator action): mandiant (stale since 2026-06-13, feedburner RSS 404 —
direct-HTML workaround known, canonical-swap still pending), msrc (stale since
2026-05-30, feed parse error — content reaches corpus via relays), ars-security
(stale since 2026-05-09, security-only path retired — root-feed workaround). No
stale-source retry attempted this sweep.

## In-window item evaluation

Watchlist/vuln matches — BOTH anti-noise dedup (already promoted at 06:00):
- ServiceNow CVE-2026-6875 "Critical ServiceNow code execution flaw now exploited"
  (BleepingComputer / Sergiu Gatlan, 05:29 EDT) — SAME article already captured at
  raw-2026-07-20-flash-0600-001 and promoted to finding-2026-07-20-flash-0600-0001
  (B2/likely, absorbed to this morning brief). No net-new content.
- wp2shell CVE-2026-63030 + CVE-2026-60137 "WP2Shell WordPress Vulnerabilities
  Exploited in the Wild" (SecurityWeek / Eduard Kovacs, 01:21 EDT) — SAME article
  already captured at raw-2026-07-20-flash-0600-002 and folded as STATE CHANGE #2
  into finding-2026-07-18-0001 (VW-001, B2/likely). No net-new content.

Filtered — no watchlist (aerospace-defense) / _roster.yaml actor / _index.yaml
vuln match (Mode 1 discard, logged for orchestrator awareness):
- "Hugging Face discloses breach linked to autonomous AI agent" (BleepingComputer,
  05:56 EDT) + "Hugging Face Hacked in Autonomous AI Attack" (SecurityWeek, 05:36
  EDT) — two publisher-independent reports of a production-infrastructure breach of
  the HF AI repository via an autonomous-AI-agent system; internal datasets + service
  credentials compromised. NO A&D entity, NO tracked roster actor, NO tracked CVE →
  discarded per Mode 1. CREDENTIAL DISCIPLINE (Hard Rule 7 / LEGAL-POLICY): articles
  reference credential compromise but publish no credential values; none stored. NOTE
  for orchestrator: second AI-agent-driven-attack theme of the month; potential
  emerging-TTP watch candidate but not currently in Archimedes tracking scope.
- Ernst & Young data breach (SecurityWeek, PII/financial via third-party platform) —
  no match, discarded.
- Chrome 150 memory-safety patch (6 critical/high UAF, patched, no ITW) — routine
  patch, no tracked-vuln / no exploitation, discarded.
- Capital One open-sources "VulnHunter" AI tool; WSUS sync delays; Windows/Dell OOB
  shutdown fix — tooling/operational, discarded.

## FLASH / match evaluation

No NET-NEW item in-window matched any watchlist, roster alias, or tracked vuln that
was not already handled at 06:00. Grader queue for the 2026-07-20 morning brief
carries the two 06:00-promoted absorbed items (ServiceNow, wp2shell) plus standing
sections (A&D Sector Focus, Iran Cyber Watch) on silent-day templates. No new FLASH
candidate.

## Standing watch items — no state change this window

- ServiceNow CVE-2026-6875 (watch: servicenow-api-exploitation-2026-06-09): CVE now
  assigned + ITW — captured/promoted 06:00, absorbed to morning brief. No further
  change (no KEV add, no actor, no named A&D victim) since 06:00.
- wp2shell CVE-2026-63030 (VW-001): ITW multi-firm confirmation — captured/promoted
  06:00 as UPDATE. No further change (no KEV add) since 06:00.
- Oracle EBS CVE-2026-46817 (VT-043, KEV due 07-18, past-due; ransomware Unknown): no
  new attribution, no named A&D/DIB victim, no A-grade direct exploitation confirmation
  net-new, no ransomware-campaign-use flip. Quiet.
- SharePoint CVE-2026-58644 (VT-041) / FortiSandbox CVE-2026-25089 / CVE-2026-39808
  (VT-045/046) — KEV deadlines lapsed 07-19, all past-due; no escalation net-new. Quiet.
- Nightmare Eclipse / LegacyHive (VT-042, no CVE, MSRC silent): no CVE assignment, no
  MSRC advisory, no independent ITW confirmation this window. Quiet.

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no new
failures, no recoveries. mandiant / msrc / ars-security carry prior stale state (not
retried this sweep). No runtime-field changes warranted; no edit to source-health.yaml
this sweep (consistent with recent pre-brief/FLASH practice; operator notes preserved).
