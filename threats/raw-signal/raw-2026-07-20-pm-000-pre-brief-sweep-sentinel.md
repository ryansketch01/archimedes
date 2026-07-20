---
raw_id: raw-2026-07-20-pm-000
collected_at: 2026-07-20T15:32:00-04:00
run_id: pre-brief-20260720-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: "Pre-brief collection coverage sentinel (15:30 EDT, afternoon brief)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [pre_brief, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: false
ttl_expires_at: 2026-10-18T15:32:00-04:00
---

# Pre-brief collection coverage record — 2026-07-20 15:30 EDT (afternoon brief)

ONE net-new substantive raw-signal written this sweep: raw-2026-07-20-pm-001
(Group-IB HollowGraph / Microsoft Graph C2 linked to the Cavern C2 framework —
Iran-nexus, Israel-targeted; roster-adjacent to Cavern Manticore #026 via tooling).
This sentinel is the coverage record for the 2026-07-20 afternoon brief pre-brief
collection.

Window: ~2026-07-20T07:30 → 15:30 EDT (afternoon, ~8h primary). The 06:00→12:00
slice was swept by the 2026-07-20 12:00 FLASH (clean, 0 candidates — commit fca78c0,
which raw-signaled the SonicWall SMA1000 deep-dive as a non-FLASH grader/vuln-tracker
item at raw-2026-07-20-flash-1200-001). Net-new uncovered slice this pre-brief was
~12:00 → 15:30 EDT plus a broad re-sweep of all healthy surfaces. Monday afternoon
cadence.

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- bleepingcomputer — 3 items in window (15 in feed; last_modified 2026-07-20T19:23 GMT).
  Evaluated below. PRODUCTIVE: HollowGraph item raw-signaled (pm-001).
- securityweek — 4 items in window (10 in feed; last_modified 2026-07-20T17:00 GMT).
  Evaluated below.
- the-record — 4 items in window (5 in feed). Evaluated below.

Authoritative CVE surface:
- cisa-kev (JSON, direct WebFetch) — catalog version 2026.07.16 (released
  2026-07-16T17:00Z). NO entries dated 2026-07-17, 07-18, 07-19, or 07-20. No new KEV
  additions this window (unchanged from morning pre-brief). Standing items
  CVE-2026-46817 (Oracle EBS), CVE-2026-58644 (SharePoint), CVE-2026-25089 /
  CVE-2026-39808 (FortiSandbox), CVE-2026-15409 / CVE-2026-15410 (SonicWall SMA1000)
  all still present with past-due deadlines — no state change. ServiceNow CVE-2026-6875
  and wp2shell CVE-2026-63030 confirmed still NOT KEV-listed (KEV-add remains an open
  watch signal on both).

First-party (Splunk, Frank; reachable, v10.2.2, license OK):
- Coverage sweep (index=archimedes OR index=defenseclaw_local, -9h): in-window events
  are exclusively Archimedes' own telemetry (archimedes:operation 4, archimedes:scheduler
  7 = 11 self-audit events). defenseclaw_local ZERO events in-window. No tracked-IOC hits.
- Targeted IOC sweep (-90d) on the pm-001 Cavern-cluster indicators (cloudlanecdn[.]com,
  hospitalinstallation[.]com [Cavern Manticore #026 C2], HollowGraph, logAzure): 0 hits.
  Visibility-bounded null, no bonus. Trigger 3 cannot fire.

Not queried this pre-brief (stale, carry prior state; entrenched failure patterns
pending operator action): mandiant (stale since 2026-06-13, feedburner RSS 404 —
direct-HTML workaround known, canonical-swap still pending), msrc (stale since
2026-05-30, feed parse error — content reaches corpus via relays), ars-security
(stale since 2026-05-09, security-only path retired — root-feed workaround). No
stale-source retry attempted this sweep (all under the routine-skip posture; none is
>24h-since-stale-eligible-and-untried in a way that changes the sweep).

## In-window item evaluation

RAW-SIGNALED (net-new match):
- HollowGraph / Microsoft Graph M365-calendar C2 (BleepingComputer / Bill Toulas,
  13:43 EDT; Group-IB primary) — Group-IB high-confidence links the malware to the
  **Cavern C2 framework** (tracked tooling of Cavern Manticore #026, Iran-MOIS), plus a
  low-confidence Lyceum similarity. Iran-nexus, Israel-targeted espionage, 12 systems,
  IOC cloudlanecdn[.]com. → raw-2026-07-20-pm-001 (grader/actor-profiler queue). See
  that file for full FLASH-trigger disposition (NON-flash; T2/T4 fail because the linkage
  is tooling-level, no hardened roster-actor attribution).

Anti-noise dedup (already captured earlier today — NOT re-raw-signaled):
- SonicWall SMA1000 CVE-2026-15409 / CVE-2026-15410 "Zero-Days Exploited to Deliver
  Custom Malware for Weeks Before Patch" (SecurityWeek / Eduard Kovacs, 10:11 EDT) — SAME
  Volexity/UTA0533 item already captured at raw-2026-07-20-flash-1200-001 (12:00 FLASH).
  No net-new content. Standing vuln-tracker VT-NNN-dossier recommendation carries.
- Hugging Face autonomous-AI-agent breach (BleepingComputer / Sergiu Gatlan, 07:56 EDT;
  also SecurityWeek AM) — SAME breach already evaluated + discarded at the 2026-07-20
  morning pre-brief (raw-2026-07-20-am-000). No A&D / roster / tracked-CVE match. Anti-noise.

Filtered — no watchlist (aerospace-defense) / _roster.yaml actor / _index.yaml vuln
match (Mode 1 discard, logged for orchestrator awareness):
- "OpenSSL Silently Fixes 'HollowByte' DoS Vulnerability" (SecurityWeek / Ionut Arghire,
  08:32 EDT) — memory-exhaustion DoS in OpenSSL, silently fixed. DoS-only, no CVE cited in
  relay, NO ITW, NOT KEV, not in _index.yaml. Widely-deployed library but DoS-class +
  no-exploitation → does not clear tracking floor. Discarded per Mode 1; noted for
  vuln-tracker awareness (OpenSSL is infrastructure-ubiquitous; if a CVE + exploitation
  surface later, re-evaluate).
- "India says allegedly leaked nuclear plant files pose no safety risk" (The Record,
  14:20 EDT) — World Leaks cybercrime group claimed Kudankulam Nuclear Power Plant leak;
  Indian officials say no safety/security data. World Leaks NOT in roster; Indian civil
  nuclear utility NOT an A&D-prime watchlist entity; no tracked CVE. Discarded per Mode 1.
- "Hackers were inside South Korea's diplomat training system for 9 months" (The Record,
  11:15 EDT) — SK Foreign Ministry diplomatic-academy compromise, PII theft, "unidentified
  hackers" (NO attribution named). Espionage-flavored but no roster actor, no A&D-prime,
  no CVE. Discarded per Mode 1; noted (DPRK/China-APT-plausible region but UNATTRIBUTED —
  no basis to originate attribution, Hard Rule 2).
- "Romania races to restore land registry after cyberattack" (The Record, 10:45 EDT) —
  govt land-registry disruption; no roster actor, no A&D, no CVE. Discarded.
- "More than 1,000 domains illegally streaming World Cup seized, DOJ" (The Record) —
  LE/anti-piracy; no match. Discarded.
- SecurityWeek: "Neo Emerges From Stealth With $100M" (AI-security funding) and "New Index
  Tracks Material Breaches" (resource/journalism) — non-threat-intel, filtered.
- BleepingComputer: "An AI SOC Evaluation Guide" (sponsored by Prophet Security) — sponsored,
  filtered.

## Standing watch items — no state change this window

- SonicWall SMA1000 CVE-2026-15409 / -15410 (UTA0533/Volexity, KEV-listed 07-14, past-due):
  today's SecurityWeek deep-dive already captured at 12:00 FLASH; vuln-tracker VT-NNN-dossier
  recommendation stands (net-new to _index.yaml, actively-exploited edge-appliance pair). No
  further net-new since 12:00.
- ServiceNow CVE-2026-6875 (B2/likely, promoted 06:00, absorbed to morning brief): no KEV add,
  no actor, no named A&D victim net-new. Quiet.
- wp2shell CVE-2026-63030 (VW-001, ITW): no KEV add net-new. Quiet.
- Oracle EBS CVE-2026-46817 (VT-043, KEV past-due): no new attribution / A&D victim /
  ransomware flip. Quiet.
- SharePoint CVE-2026-58644 (VT-041) / FortiSandbox CVE-2026-25089 / -39808 (VT-045/046):
  KEV deadlines lapsed, all past-due; no escalation net-new. Quiet.
- Nightmare Eclipse / LegacyHive (VT-042, no CVE, MSRC silent): no CVE assignment, no MSRC
  advisory, no independent ITW confirmation this window. Quiet.
- Cavern Manticore #026 (Iran-MOIS, Cavern C2 framework): NEW roster-adjacent development
  this window — Group-IB HollowGraph report (pm-001). Tooling-level linkage only; actor
  attribution NOT hardened. Flagged for actor-profiler review.

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no new
failures, no recoveries. mandiant / msrc / ars-security carry prior stale state (not
retried this sweep). No runtime-field changes warranted; no edit to source-health.yaml
this sweep (operator-set `notes` and unrecognized keys preserved verbatim, per field-
ownership rule).
