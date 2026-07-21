---
raw_id: raw-2026-07-21-pm-000
collected_at: 2026-07-21T15:37:00-04:00
run_id: pre-brief-20260721-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: "Pre-brief collection coverage sentinel (15:30 EDT, afternoon brief)"
  source_url: null
  published_at: null
match_reason:
  watchlist: [aerospace-defense]
  actors: []
  vulnerabilities: [CVE-2026-63030, CVE-2026-60137, CVE-2026-0770, CVE-2026-0257, CVE-2025-61882, CVE-2026-46817, CVE-2026-6875, VT-042]
  keywords: []
triage_tags: [pre_brief, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 620
promoted: false
ttl_expires_at: 2026-10-19T15:37:00-04:00
---

# Pre-brief collection coverage record — 2026-07-21 15:30 EDT (afternoon brief)

**2 net-new substantive raw-signal files written** (pm-001 wp2shell active-exploitation
detail, pm-002 Trump defense-supply-chain EO). This sentinel is the coverage record for
the 2026-07-21 afternoon brief pre-brief collection.

Window: net-new slice ~2026-07-21T12:00 → 15:30 EDT (since the 12:00 FLASH sweep,
commit 8b18de6). Broader 14h pre-brief window (~01:30 → 15:30) already covered by the
06:00 FLASH (clean, a1b449a), the 07:30 morning pre-brief (am sentinel + 3 items,
2ddfccb), and the 12:00 FLASH (3 raw-signal files, 8b18de6). Focus was net-new content
published after the 12:00 sweep. Tuesday afternoon cadence.

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- bleepingcomputer — 2 items in window (15 in feed; last_modified 2026-07-21T19:20 GMT).
  Evaluated below.
- securityweek — 2 items in window (10 in feed; last_modified 2026-07-21T18:27 GMT).
  Evaluated below.
- the-record — 2 items in window (5 in feed): DNI nominee Clayton Senate-panel approval
  (govt/leadership) + Spain fines 23andMe ~$3M (GDPR/consumer breach) — neither has an
  A&D / roster-actor / tracked-CVE nexus. DISCARDED.
- sans-isc — 0 items in window (feed 200, 10 in feed). Krebs — 0 in window (last post
  2026-07-15). rapid7 — 0 in window. unit42 (feedburner) — 0 in window (last 2026-07-20).
  mstic parent feed — 0 in window (last 2026-07-17).

Authoritative CVE surface:
- cisa-kev: JSON re-checked. Most recent dateAdded remains **2026-07-21** — the SAME
  four entries surfaced at the 12:00 sweep (CVE-2026-63030 wp2shell due 07-24;
  CVE-2026-60137 wp2shell-SQLi due 08-04; CVE-2026-0770 Langflow due 07-24; CVE-2021-27137
  DD-WRT due 07-24). **NO net-new KEV additions since the 12:00 sweep.** No entries dated
  2026-07-22.

First-party (Splunk, Frank; reachable):
- Trigger-3 / first-party-IOC sweep (index=archimedes OR index=defenseclaw_local, -24h):
  in-window events are exclusively Archimedes' own telemetry (archimedes:scheduler 17,
  archimedes:operation 10 = 27 self-audit events). **defenseclaw_local ZERO events**
  in-window. No tracked-IOC hits. Visibility-bounded null, no bonus. Trigger 3 cannot fire.

Not queried this pre-brief (stale, carry prior state; entrenched failure patterns pending
operator action): mandiant (stale since 2026-06-13, feedburner RSS 404 — direct-HTML
workaround known, canonical-swap pending), msrc (stale since 2026-05-30, feed parse error —
content reaches corpus via relays), ars-security (stale since 2026-05-09, security-only path
retired — root-feed workaround), github-advisories (406 on global atom — per-repo GHSA
fallback), dragos (blog RSS 404). No stale-source retry attempted this sweep (all under the
carry-prior-state pattern).

## In-window item evaluation

NET-NEW substantive (raw-signaled for grader):
- **wp2shell CVE-2026-63030 / CVE-2026-60137 — active exploitation + webshell deployment**
  (BleepingComputer / Bill Toulas, relaying Wiz) — raw-2026-07-21-pm-001. First post-KEV
  ITW webshell-deployment detail + timeline (first probing 2026-07-17 23:29 UTC) + host
  artifacts. Escalation beyond the 12:00 KEV-add (flash-1200-001). UPDATE material +
  vuln-tracker handoff candidate. No actor. CVSS dispute carries forward.
- **Trump EO: defense contractors to map software + suppliers** (SecurityWeek) —
  raw-2026-07-21-pm-002. A&D watchlist/sector-policy signal: indentured BOM, foreign-
  ownership vetting, Department of War 15-/45-day reporting, CMMC Phase 2 suspension
  reference. No actor/CVE/IOC. Sector context for the afternoon-brief A&D section.

Filtered — no watchlist / roster / vuln-index match (Mode 1 discard, logged for
orchestrator awareness):
- **Anubis ransomware claims Coca-Cola Fairlife attack** (BleepingComputer / Lawrence
  Abrams) — food/dairy subsidiary; Anubis NOT a roster actor; no A&D nexus, no tracked
  CVE. DISCARDED.
- **Cisco launches low-cost AI models for source-code security** (SecurityWeek) —
  product/marketing; no threat, no actor, no CVE. DISCARDED.
- **DNI nominee Clayton Senate-panel approval** + **Spain fines 23andMe ~$3M**
  (The Record) — govt leadership + GDPR/consumer breach; no A&D/actor/CVE nexus.
  DISCARDED.

## Standing watch / open threads — state this window

- **wp2shell CVE-2026-63030 (VW-001):** ESCALATION — first post-KEV ITW webshell-
  deployment detail (pm-001). KEV due 2026-07-24.
- **Langflow CVE-2026-0770 (KEV, ITW):** quiet this window — no net-new since the 12:00
  KEV add; no A&D nexus, no tracked-actor attribution (was routed to afternoon brief per
  12:00 calibration). No new substance.
- **Qilin / PAN-OS GlobalProtect CVE-2026-0257:** quiet — morning-brief lead, no net-new.
- **Cl0p / Oracle EBS CVE-2025-61882 (Estée Lauder):** quiet — attribution re-stated,
  non-A&D, already covered (00:00 flash-0000-001).
- **VT-043 Oracle EBS CVE-2026-46817:** quiet — no new attribution/A&D victim/ransomware
  flip; KEV past-due. (Do NOT conflate with Cl0p CVE-2025-61882.)
- **SonicWall SMA1000 UTA0533 + ROOTRUN:** quiet — no new substance.
- **ServiceNow CVE-2026-6875 (ITW claim retracted):** quiet this window.
- **VT-042 LegacyHive (0patch unofficial micropatch):** quiet this window.
- **VT-041/045/046 SharePoint/FortiSandbox; HollowGraph M365-Graph C2:** all quiet.

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no new
failures, no recoveries. mandiant / msrc / ars-security / github-advisories / dragos carry
prior stale/degraded state (not retried this sweep). **No runtime-field changes warranted;
no edit to source-health.yaml this sweep** (operator-set `notes` fields preserved verbatim).
Proposal to orchestrator: no source-health changes to commit.
