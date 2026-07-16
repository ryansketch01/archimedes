---
raw_id: raw-2026-07-16-flash-1600-000
collected_at: 2026-07-16T16:05:00-04:00
run_id: flash-2026-07-16-1600
collection_mode: flash_sweep
sweep_window_start: 2026-07-16T06:00:00-04:00
sweep_window_end: 2026-07-16T16:00:00-04:00
source:
  source_yaml_id: multi
  source_name: "FLASH sweep — CISA KEV + productive RSS feeds + Splunk first-party"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: [Sandworm, Scattered Spider]
  vulnerabilities: [CVE-2026-46817]
  keywords: []
triage_tags: [flash_sweep, sweep_sentinel, one_candidate]
iocs_extracted: false
iocs_count: 0
promoted: false
ttl_expires_at: 2026-10-14T16:05:00-04:00
---

# FLASH sweep sentinel — 16:00 EDT 2026-07-16 (1 marginal candidate: Sandworm Trigger 4)

Async, out-of-cadence FLASH sweep. Window 2026-07-16T06:00 -> 16:00 EDT (~10h since the
06:00 clean sweep; overlaps the 07:30 pre-brief + 08:00 morning brief, so morning-absorbed
items are excluded per anti-noise rule 1). Narrow question: anything matching a FLASH trigger
since 06:00? **One marginal Trigger 4 candidate (Sandworm), surfaced for grader adjudication.**

## Sources queried

- **CISA KEV** — catalog version **2026.07.15** (dateReleased 2026-07-15T16:42Z), **UNCHANGED**
  from the 06:00 baseline. Zero new adds; no 2026-07-16 entries. Only 2026-07-15 adds remain
  CVE-2026-46817 (Oracle EBS — VT-043, tracked) and CVE-2023-4346 (KNX — swept, no A&D nexus).
- **BleepingComputer** RSS — reachable (200), 7 items in window (evaluated below).
- **SecurityWeek** RSS — reachable (200), 6 items in window (evaluated below).
- **The Record** RSS — reachable (200), 2 items in window (Sandworm ClickFix = candidate;
  Scattered Spider TfL sentencing = non-FLASH).
- **Splunk first-party** — Frank reachable (10.2.2). defenseclaw_local **0 events / -24h**;
  archimedes only own operational logs (8 operation + 17 scheduler events). **No tracked-IOC
  hit.** Trigger 3 not met (visibility-bounded null).

## FLASH trigger evaluation

- Trigger 1 (critical-CVE + active exploitation, A-grade): **none new** (KEV unchanged).
- Trigger 2 (new tracked-actor attribution): **none** (Sandworm attribution is long-standing,
  not new; Scattered Spider item is a sentencing, not attribution).
- Trigger 3 (first-party IOC hit): **none** (Splunk null).
- Trigger 4 (tracked-actor TTP change): **1 MARGINAL** — Sandworm (#007) ClickFix shift + new
  tooling (GhettoVibe/ScoutCurl/FluidLeech/LoadLoop) per CERT-UA. See
  raw-2026-07-16-flash-1600-001. Ukraine-focused, no A&D nexus, commodity ClickFix base, no
  atomic IOCs in relay -> likely a scheduled-brief Russia-watch item, but surfaced as a
  candidate (collector surfaces, grader decides post/hold).
- Trigger 5 (active multi-victim A&D nation-state campaign): **none**.
- Trigger 6 (zero-day, no patch, exploitation confirmed/imminent): **none new** (LegacyHive/
  VT-042 already tracked; no state change this window).

## Non-FLASH / discarded in-window items (audit trail)

- **Scattered Spider (#013) — TfL hackers sentenced 5.5yr** (BleepingComputer + SecurityWeek +
  The Record). Law-enforcement OUTCOME for a 2024 hack; not new attribution, not TTP change,
  not new campaign. Fails all triggers. Cybercrime/LE — candidate for next scheduled brief
  mention, NOT a FLASH.
- **UAT-11795 — Russian actor trojanizes WebEx/Zoom -> Starland RAT** (BleepingComputer,
  Toulas). Financially-motivated; **UAT-11795 not in _roster.yaml**; no A&D nexus. Non-FLASH.
- **Spirals ransomware — full intrusion-to-encryption <24h** (BleepingComputer, Toulas). New
  non-roster ransomware actor; no A&D nexus. Non-FLASH.
- **Splunk + Zoom patch critical vulnerabilities** (SecurityWeek, Arghire). Vendor patches, no
  ITW claim. Non-FLASH — vuln-tracker interest; NOTE Splunk is Archimedes' own SIEM (Frank runs
  Splunk 10.2.2) -> flag for operator patch-posture awareness.
- **ClickLock Stealer bypasses macOS** (SecurityWeek). Commodity infostealer, ~100 users, no
  A&D / no tracked actor. Discarded.
- **CISA orders feds to patch Oracle EBS by Saturday** (BleepingComputer, Gatlan) — **VT-043
  / CVE-2026-46817**, already absorbed into the 2026-07-16 morning brief as an UPDATE
  (raw-2026-07-16-am-004). Anti-noise rule 1: absorbed, not re-triggered.
- 23andMe $18M settlement, Windows 11 24H2 EOL, AI-datacenter/AI-agent opinion pieces, Oak
  funding, OT-disclosure op-ed — no threat/actor/vuln content. Discarded.

## Absorbed (already tracked — anti-noise rule 1)

- **VT-043 Oracle EBS CVE-2026-46817** — morning-brief UPDATE; KEV deadline 2026-07-18 still
  pending; no new state change this window (no attribution, no new atomic IOCs, ransomware-use
  still Unknown, KEV catalog unchanged).
- **VT-042 LegacyHive** (Nightmare Eclipse profsvc LPE) — morning-brief monitoring item; no new
  state change (still no CVE, unpatched, KEV-ineligible, no ITW).
- **VT-044 F5 NGINX/BIG-IP CVE-2026-42533** — morning-brief new finding; patched, no ITW.

## Source-health observations

- All queried sources reachable/healthy this sweep (BleepingComputer, SecurityWeek, The Record,
  CISA KEV JSON, Splunk/Frank). No new stale flips, no auth errors, no rate-limits. No
  runtime-field changes required beyond timestamp refresh (handled by librarian/orchestrator).
- SANS ISC not queried this narrow async sweep (carried its documented transient-parse pattern
  from the 06:00 sweep; not a blocker).

## Extraction notes

- ioc-extraction skill: invoked on the Sandworm candidate (raw-...-001) -> 0 atomic IOCs
  (tooling names only). Not invoked on discarded items (no promotion).
- No credentials observed. No PoC/exploit content copied (Hard Rule 3).
- No attribution originated or upgraded (Hard Rule 2).
