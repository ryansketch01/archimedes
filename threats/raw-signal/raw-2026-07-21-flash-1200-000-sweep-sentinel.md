---
raw_id: raw-2026-07-21-flash-1200-000
collected_at: 2026-07-21T12:08:00-04:00
run_id: flash-sweep-20260721-120000
collection_mode: flash_sweep
source:
  source_yaml_id: multiple
  source_name: "FLASH alert sweep coverage sentinel (12:00 EDT)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-63030, CVE-2026-60137, CVE-2026-0770, CVE-2021-27137]
  keywords: [wp2shell, CISA-KEV, Langflow]
triage_tags: [flash_sweep, coverage_record, non_flash, clean_sweep]
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: false
ttl_expires_at: 2026-10-19T12:08:00-04:00
---

# FLASH sweep coverage record — 2026-07-21 12:00 EDT

**CLEAN sweep for FLASH-posting purposes. 0 posted-FLASH candidates, 0 triggers
warranting a Discord post.** Active hours apply (12:00 is inside 09:00–21:00 EDT),
so a genuine FLASH would post immediately — none generated.

Window: ~2026-07-21T06:00 → 12:00 EDT (6h primary). Prior sweep of record:
2026-07-21 06:00 FLASH (clean, 0 candidates). Morning brief published 08:00
(Qilin/PAN-OS GlobalProtect CVE-2026-0257 lead + ServiceNow/LegacyHive/SonicWall
UPDATEs).

**One genuine state change this window:** CISA KEV added four CVEs dated
2026-07-21 (none existed as of the 00:00 or 06:00 sweeps). Two are UPDATE-worthy
and raw-signaled as non-FLASH grader-queue / afternoon-brief material
(raw-...-001 wp2shell chain — already-tracked open thread; raw-...-002 Langflow
CVE-2026-0770 — net-new critical). Disposition = absorb into the 16:00 afternoon
brief per the established Oracle-EBS / SharePoint precedent (KEV criticals with no
A&D nexus and no tracked-actor attribution route to scheduled briefs, not posted
FLASHes). Neither warrants a Discord FLASH.

## Sources swept (healthy)

RSS/media via rss-bridge fetch_feed (all HTTP 200):
- **bleepingcomputer** — 3 items in window (15 in feed; last_modified
  2026-07-21T15:56 GMT). (1) Qilin exploiting PAN-OS GlobalProtect CVE-2026-0257
  [= this morning's brief LEAD, already covered — anti-noise; Qilin NOT roster;
  attribution already briefed]; (2) US/DOJ FIFA World Cup piracy domain seizures
  [no A&D/roster/CVE — DISCARDED]; (3) sponsored Specops identity post [filtered].
- **securityweek** — 6 items in window (10 in feed; last_modified 2026-07-21T14:37
  GMT). HollowGraph M365-Calendar C&C [already net-new in 07-20 PM brief, no
  tracked-actor attribution — anti-noise UPDATE]; Estée Lauder / Oracle EBS
  zero-day (Cl0p) [already raw-signaled 00:00 sweep raw-...-001; cosmetics, no
  A&D; new victim ≠ new attribution — anti-noise]; Meta $78k bug bounty, Empirical
  $25M funding, ICS awards, CISO Conversations [all non-qualifying — DISCARDED].
- **the-record** — 2 items in window (5 in feed). Taiwan 5G throttling during
  Han Kuang drills; Kenya president website defacement + bitcoin ransom [no
  A&D/roster/tracked-CVE — DISCARDED].

Authoritative CVE surface:
- **cisa-kev** (JSON, WebFetch, verified against known-good 07-16 SharePoint /
  07-15 Oracle-EBS dates): FOUR net-new adds dated 2026-07-21 —
  - CVE-2026-63030 WordPress Core (wp2shell RCE), due 2026-07-24 (accelerated).
  - CVE-2026-60137 WordPress Core SQLi (wp2shell chain), due 2026-08-04.
  - CVE-2026-0770 Langflow RCE (CVSS 9.8), due 2026-07-24 (accelerated).
  - CVE-2021-27137 DD-WRT stack buffer overflow, due 2026-07-24.
  NO adds dated 2026-07-20. SharePoint CVE-2026-58644 (07-16) + Oracle EBS
  CVE-2026-46817 (07-15) confirmed prior adds (a first WebFetch pass mis-bucketed
  both under 07-21; the targeted re-fetch corrected this).

First-party (Splunk, Frank; reachable):
- **Trigger-3 sweep** (index=archimedes OR index=defenseclaw_local, -24h): in-window
  events are exclusively Archimedes' own telemetry (archimedes:operation 10,
  archimedes:scheduler 17 = 27 self-audit events). defenseclaw_local ZERO events
  in-window. No tracked-IOC hits. Visibility-bounded null, no bonus.

Not queried (FLASH-fast scope): mandiant (stale since 2026-06-13, RSS 404), msrc
(stale since 2026-05-30, parse error), ars-security (stale since 2026-05-09). No
stale-source retry this FLASH window.

## FLASH trigger evaluation

All 6 triggers evaluated — none warrant a posted FLASH:
- **T1 critical-CVE-exploited:** Langflow CVE-2026-0770 (9.8 + active exploitation
  + CISA-KEV A-grade) mechanically satisfies T1, and wp2shell CVE-2026-63030 does
  too IF the WPScan-CNA 9.8 is taken over CISA's 7.5 enrichment. BUT both lack any
  A&D nexus / tracked-actor / watchlist hit; wp2shell is an already-tracked open
  thread; both are n-day (patched). Per corpus calibration (Oracle EBS
  CVE-2026-46817 9.8 held/absorbed; SharePoint routed to scheduled), disposition
  = absorb into 16:00 afternoon brief as UPDATE, NOT posted FLASH. Next scheduled
  window (~4h out) precedes both 07-24 KEV deadlines with slack.
- **T2 tracked-actor-attribution:** none. Qilin (PAN-OS), Cl0p (Estée Lauder),
  UTA0533 (SonicWall) are all re-statements of established attributions; Qilin +
  UTA0533 are not roster actors; Cl0p new victim ≠ new attribution.
- **T3 first-party-IOC-hit:** null (no Splunk telemetry hits).
- **T4 tracked-actor-TTP-change:** none net-new attributable to a roster actor.
  HollowGraph (unattributed toolkit) already covered 07-20 PM.
- **T5 A&D-sector-campaign:** no active multi-victim A&D campaign net-new this
  window. WebSearch surfaced only stale March-2026 Lockheed/APT-Iran claims.
- **T6 zero-day-no-patch:** none net-new. wp2shell/Langflow/SonicWall all patched.

## Open threads — status this window

- **Qilin / PAN-OS GlobalProtect CVE-2026-0257:** = morning brief LEAD; today's
  BleepingComputer relay is the same Arctic Wolf attribution already briefed. No
  net-new movement. Anti-noise.
- **wp2shell CVE-2026-63030 / CVE-2026-60137:** STATE CHANGE — added to CISA KEV
  07-21 (RCE due 07-24 accelerated). Already-tracked open thread → UPDATE
  (raw-...-001). Not a flip to FLASH.
- **Cl0p / Oracle EBS CVE-2025-61882:** new victim (Estée Lauder) via SecurityWeek;
  re-stated attribution, non-A&D. Already covered 00:00 sweep. Anti-noise.
- **SonicWall SMA1000 UTA0533 (CVE-2026-15409 / -15410):** no net-new escalation
  beyond prior relays; already briefed 07-20 PM + 00:00 sweep. Quiet.
- **ServiceNow CVE-2026-6875:** exploitation nuance already captured (am-002,
  07-21 morning); Defused ITW-claim retraction noted in 06:00 commit. Quiet.
- **VT-041 SharePoint CVE-2026-58644 / VT-042 LegacyHive / VT-043 Oracle-EBS
  CVE-2026-46817 + FortiSandbox:** no escalation net-new. Quiet.
- **HollowGraph M365-Graph C2:** fresh SecurityWeek coverage, no tracked-actor
  attribution; already net-new in 07-20 PM brief. Anti-noise UPDATE.

## Source health

All queried sources returned HTTP 200 and remain `healthy`; no status flips, no
new failures, no recoveries. mandiant/msrc/ars-security carry prior stale state
(not retried this FLASH-fast sweep). No runtime-field changes; no edit to
source-health.yaml this sweep.
