---
raw_id: raw-2026-07-21-am-000
collected_at: 2026-07-21T07:37:00-04:00
run_id: pre-brief-20260721-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: "Pre-brief collection coverage sentinel (07:30 EDT, morning brief)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-0257, CVE-2026-6875, VT-042, CVE-2025-61882, CVE-2026-15409]
  keywords: []
triage_tags: [pre_brief, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: false
ttl_expires_at: 2026-10-19T07:37:00-04:00
---

# Pre-brief collection coverage record — 2026-07-21 07:30 EDT (morning brief)

**3 net-new substantive raw-signal files written** (am-001 PAN-OS/Qilin, am-002
ServiceNow exploitation clarification, am-003 LegacyHive 0Patch), plus 2 in-window
items carried as anti-noise dedup against the overnight FLASH sweeps (Estée Lauder /
Oracle EBS, SonicWall SMA1000). This sentinel is the coverage record for the
2026-07-21 morning brief pre-brief collection.

Window: ~2026-07-20T15:30 → 2026-07-21T07:30 EDT (14h primary). Overnight slices
already swept: 2026-07-20 18:00 FLASH (clean, commit 85f5384), 2026-07-21 00:00
FLASH (2 items raw-signaled, commit c7fa9e0), 2026-07-21 06:00 FLASH (clean,
commit a1b449a). Net-new uncovered slice this pre-brief was ~06:00 → 07:30 EDT plus
a broad re-sweep of all healthy surfaces — which surfaced the net-new PAN-OS/Qilin
and ServiceNow-exploitation stories (both published this morning after the 06:00
sweep). Tuesday morning cadence.

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- bleepingcomputer — 9 items in window (15 in feed; last_modified 2026-07-21T11:25
  GMT). Evaluated below.
- securityweek — 6 items in window (10 in feed; last_modified 2026-07-21T11:30 GMT).
  Evaluated below.
- the-record — 1 item in window (5 in feed): Flock Safety acoustic-detection
  shutdown (privacy/tech) — no A&D / no roster actor / no tracked CVE, DISCARDED.

Authoritative CVE surface:
- cisa-kev: per the 2026-07-21 00:00 + 06:00 FLASH checks, NO entries dated
  2026-07-19, 07-20, or 07-21; most recent adds remain 2026-07-16 (SharePoint
  CVE-2026-58644 / FortiSandbox CVE-2026-25089 + CVE-2026-39808, all past-due). No
  new KEV additions this window. NOTE: CVE-2026-0257 (PAN-OS GlobalProtect, am-001)
  is an EXISTING KEV entry (added 2026-05-29) — the net-new element is the Qilin
  ransomware attribution, not a KEV state change.

First-party (Splunk, Frank; reachable, v10.2.2, license OK):
- Trigger-3 / first-party-IOC sweep (index=archimedes OR index=defenseclaw_local,
  -14h): in-window events are exclusively Archimedes' own telemetry
  (archimedes:operation 4, archimedes:scheduler 7 = 11 self-audit events).
  defenseclaw_local ZERO events in-window. No tracked-IOC hits. Visibility-bounded
  null, no bonus. Trigger 3 cannot fire.

Not queried this pre-brief (stale, carry prior state; entrenched failure patterns
pending operator action): mandiant (stale since 2026-06-13, feedburner RSS 404 —
direct-HTML workaround known, canonical-swap still pending), msrc (stale since
2026-05-30, feed parse error — content reaches corpus via relays), ars-security
(stale since 2026-05-09, security-only path retired — root-feed workaround). No
stale-source retry attempted this sweep.

## In-window item evaluation

NET-NEW substantive (raw-signaled for grader):
- **PAN-OS GlobalProtect CVE-2026-0257 exploited by Qilin ransomware** (BleepingComputer /
  Sergiu Gatlan, relaying Arctic Wolf Labs) — raw-2026-07-21-am-001. Critical
  edge/VPN auth-bypass, KEV-listed since 2026-05-29, patched 2026-05-13; Arctic Wolf
  ties June 2026 Qilin-ransomware intrusions to it. A&D-relevant edge infra; no named
  A&D victim. COVERAGE-GAP flag: CVE-2026-0257 not in _index.yaml as its own row
  (only a "distinct from" note under VT-019).
- **ServiceNow CVE-2026-6875 exploitation clarification** (SecurityWeek / Eduard
  Kovacs) — raw-2026-07-21-am-002. Net-new refinement of the 06:00 "retraction":
  Defused ITW observation = replay of Searchlight Cyber's public PoC, ServiceNow-hosted
  instances unaffected per vendor; ITW-attempt observation itself stands. UPDATE material.
- **Windows LegacyHive VT-042 gets 0Patch/ACROS unofficial micropatch** (BleepingComputer /
  Sergiu Gatlan) — raw-2026-07-21-am-003. Patch-status state change (was unpatched /
  MSRC-silent); still no CVE, no official patch, no ITW. UPDATE material for vuln-tracker.

In-window, ALREADY captured overnight (anti-noise dedup — NOT re-written):
- Estée Lauder / Oracle EBS breach (BleepingComputer + SecurityWeek, both in-window) —
  same story captured at raw-2026-07-21-flash-0000-001. Cl0p 2025 campaign
  (CVE-2025-61882), DISTINCT from tracked VT-043 CVE-2026-46817. SecurityWeek version
  adds detail (breach dated August 2025; personal/financial/health data). Grader-queue /
  morning-brief-UPDATE material via the existing 00:00 raw-signal.
- SonicWall SMA1000 zero-days push custom malware (BleepingComputer / Lawrence Abrams) —
  captured at raw-2026-07-21-flash-0000-002 (UTA0533, ROOTRUN tooling). Anti-noise dedup.

Filtered — no watchlist / roster / vuln-index match (Mode 1 discard, logged for
orchestrator awareness):
- US/DOJ FIFA World Cup piracy site seizures (1,000+ domains) — LE action, no nexus.
- Microsoft WSUS sync-delay MANUAL FIX (BleepingComputer) — operational only, NOT the
  security advisory; no exploitation / no tracked vuln. (Open-thread "Microsoft WSUS
  advisory" = no security state change this window.)
- Meta $78k bug-bounty broken-access-control disclosure — patched, no A&D/actor/CVE.
- Clover Health Investments data breach (social engineering / healthcare) — no nexus.
- Zimbra update patches critical vulns (cmd injection / XSS / bypass / SSRF) — patched,
  NO ITW, NO actor, A&D-relevance low. (Open-thread "Zimbra critical patches" = patched,
  no exploitation; discard consistent with 06:00 FLASH.)
- Ostium $23.7M crypto theft; Cursor/Codex/Gemini CLI/Antigravity AI sandbox escapes
  (patched CVEs, Google downgraded two); JadePuffer/EncForge agentic-AI ransomware —
  all commodity / no tracked actor / no A&D nexus (consistent with 18:00 07-20 + 00:00
  07-21 discards). NOTE for orchestrator: agentic-AI-attack theme recurring (JadePuffer,
  Hugging Face 07-20) — potential emerging-TTP watch candidate, not in current scope.

## Standing watch / open threads — state this window

- **Cl0p / Oracle EBS (CVE-2025-61882):** new named victim Estée Lauder (Aug-2025 breach
  disclosed now). Attribution re-stated, not new. Already captured (flash-0000-001).
- **SonicWall SMA1000 UTA0533 (CVE-2026-15409/15410):** corroboration + ROOTRUN tooling.
  Already captured (flash-0000-002). Not a flip.
- **VT-043 Oracle EBS CVE-2026-46817:** quiet — no new attribution, no A&D victim, no
  ransomware-use flip, KEV past-due. (Do not conflate with the Cl0p CVE-2025-61882 above.)
- **ServiceNow CVE-2026-6875:** exploitation-picture UPDATE this window (am-002).
- **VT-042 LegacyHive:** unofficial-micropatch state change this window (am-003).
- **wp2shell CVE-2026-63030 (VW-001); VT-041 SharePoint; VT-045/046 FortiSandbox;
  HollowGraph M365-Graph C2 (net-new 07-20 PM brief):** all quiet this window.

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no new
failures, no recoveries. mandiant / msrc / ars-security carry prior stale state (not
retried this sweep). No runtime-field changes warranted; no edit to source-health.yaml
this sweep (operator-set `notes` fields preserved verbatim).
