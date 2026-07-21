---
raw_id: raw-2026-07-21-flash-0000-000
collected_at: 2026-07-21T00:06:00-04:00
run_id: flash-sweep-20260721-000000
collection_mode: flash_sweep
source:
  source_yaml_id: multiple
  source_name: "FLASH alert sweep coverage sentinel (00:00 EDT)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_sweep, coverage_record, non_flash, clean_sweep]
iocs_extracted: false
iocs_count: 0
text_word_count: 540
promoted: false
ttl_expires_at: 2026-10-19T00:06:00-04:00
---

# FLASH sweep coverage record — 2026-07-21 00:00 EDT

CLEAN sweep for FLASH purposes. **0 FLASH candidates, 0 triggers matched.** Two
in-window items touch already-tracked open threads and are raw-signaled as
non-FLASH grader-queue / morning-brief-UPDATE material (raw-...-001 Cl0p/Oracle
EBS new victim; raw-...-002 SonicWall SMA1000 corroboration + net-new tooling).
Neither cleared a FLASH trigger. Quiet hours apply (00:00 is inside 21:00–09:00
EDT) — any candidate would have QUEUED to `infrastructure/flash-queue.yaml` for
the 09:00 catchup; none generated.

Window: ~2026-07-20T18:00 → 2026-07-21T00:00 EDT (6h primary). Prior sweep of
record: 2026-07-20 18:00 FLASH (raw-2026-07-20-flash-0000-000-sweep-sentinel,
clean). Monday-night / early-Tuesday cadence.

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- bleepingcomputer — 3 items in window (15 in feed; last_modified
  2026-07-21T03:59 GMT). (1) Estée Lauder / Oracle EBS breach [Cl0p, tracked
  #018 — raw-...-001]; (2) SonicWall SMA1000 zero-days push custom malware
  [UTA0533, already tracked — raw-...-002]; (3) Ostium $23.7M crypto theft
  [commodity, no A&D / no roster actor / no tracked CVE — DISCARDED per Mode 1].
- securityweek — 0 items in window (10 in feed; last_modified 2026-07-20T17:00
  GMT).
- the-record — 0 items in window (5 in feed).

Authoritative CVE surface:
- cisa-kev (JSON, direct WebFetch) — NO entries dated 2026-07-19, 2026-07-20, or
  2026-07-21. Most recent adds remain 2026-07-16: CVE-2026-58644 SharePoint
  (VT-041), CVE-2026-25089 + CVE-2026-39808 FortiSandbox (VT-043) — all already
  tracked; all three dueDate 2026-07-19 now past. A passing KEV deadline is not a
  FLASH trigger. No new KEV additions this window.

First-party (Splunk, Frank; reachable, v10.2.2, license OK):
- Trigger-3 sweep (index=archimedes OR index=defenseclaw_local, -24h): in-window
  events are exclusively Archimedes' own operational/scheduler telemetry
  (archimedes:operation 10, archimedes:scheduler 17 = 27 self-audit events).
  defenseclaw_local returned ZERO events in-window. No tracked-IOC hits.
  Visibility-bounded null, no bonus.

Not queried this sweep (FLASH-fast scope): mandiant (stale since 2026-06-13, RSS
404), msrc (stale since 2026-05-30, feed parse error), ars-security (stale since
2026-05-09). No stale-source retry attempted this FLASH window.

## FLASH trigger evaluation

All 6 triggers evaluated against in-window items — none matched:
- T1 critical-CVE-exploited: SonicWall SMA1000 CVE-2026-15409 (critical SSRF) +
  active exploitation is real BUT already FLASH-evaluated 2026-07-20 12:00 (→
  non_flash, absorbed to afternoon brief); anti-noise one-per-topic-per-24h bars
  a re-flash. No OTHER net-new CVSS≥9.0 + active-exploitation + A-grade item.
- T2 tracked-actor-attribution: Cl0p (#018) named on Estée Lauder, but the
  Cl0p↔Oracle-EBS attribution is the established 2025 campaign (CVE-2025-61882) —
  a new victim is NOT new attribution. No new attribution to any roster actor.
- T3 first-party-IOC-hit: no Splunk telemetry hits (null, see above).
- T4 tracked-actor-TTP-change: none net-new (UTA0533 not roster).
- T5 A&D-sector-campaign: no active multi-victim A&D campaign net-new. Estée
  Lauder = cosmetics; SonicWall victim sectors unspecified, no A&D named.
- T6 zero-day-no-patch: SonicWall patched since 2026-07-14 (not no-patch). None
  net-new.

## Standing watch items — no state change this window

- SonicWall SMA1000 CVE-2026-15409/15410 (UTA0533): fresh BleepingComputer relay
  (Lawrence Abrams) corroborates the already-briefed story + adds ROOTRUN tooling
  + affected models + patch versions. UPDATE material, raw-...-002. Not a flip.
- Oracle EBS: NOTE the Estée Lauder breach is via the 2025 Cl0p campaign
  (CVE-2025-61882), DISTINCT from tracked VT-043 CVE-2026-46817. No new signal on
  VT-043 itself this window; it remains quiet / KEV past-due.
- SharePoint CVE-2026-58644 (VT-041): no escalation net-new. Quiet.
- FortiSandbox CVE-2026-25089 / CVE-2026-39808 (VT-043): no escalation. Quiet.
- ServiceNow CVE-2026-6875; WordPress Core CVE-2026-63030 (wp2shell); HollowGraph
  M365-Graph C2 (net-new 07-20 PM brief): all quiet this window.

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no
new failures, no recoveries. mandiant/msrc/ars-security carry prior stale state
(not retried this FLASH-fast sweep). No runtime-field changes warranted; no edit
to source-health.yaml this sweep.
