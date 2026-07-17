---
raw_id: raw-2026-07-17-am-000
collected_at: 2026-07-17T07:36:00-04:00
run_id: pre-brief-20260717-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multi
  source_name: "Pre-brief sweep sentinel (coverage record)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sweep-record]
triage_tags: [sweep_sentinel, coverage_record, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-15T07:36:00-04:00
---

# Pre-brief collection sweep — 2026-07-17 morning (07:30 EDT)

Coverage record for the 08:00 morning-brief pre-brief collection. Window:
**2026-07-16T17:30:00-04:00 → 2026-07-17T07:30:00-04:00** (~14h). The 06:00
FLASH sweep (run d238ede — clean, 0 triggers) already covered the 00:00–06:00
sub-window; items dated before ~06:00 EDT that match tracked topics were
absorbed there and are marked ABSORBED below (anti-noise).

## Sources queried (healthy)

| Source | Result |
|---|---|
| bleepingcomputer | 5 in-window items — 1 raw-signaled (LegacyHive, am-004), 2 absorbed by 06:00 FLASH, 2 discarded |
| securityweek | 5 in-window items — 1 raw-signaled (CMMC, am-002), 1 absorbed by 06:00 FLASH, 3 discarded |
| unit42 (feedburner) | 2 in-window items — 1 raw-signaled (Siemens ROX II, am-001), 1 discarded (AI IR-report recap) |
| mstic (MS Security Blog feed) | 1 in-window item — raw-signaled (ACR Stealer, am-003) |
| the-record | 0 items in window |
| krebs | 0 items in window |
| sans-isc | 1 item — Stormcast podcast (awareness only, no body), discarded |
| rapid7 | 0 items in window |
| cisa-advisories (all.xml) | 0 items in window |
| cisa-kev (JSON) | most-recent adds dated 2026-07-16 (VT-041/045/046) — already tracked/absorbed; **0 net-new adds dated 2026-07-17** |

## Raw-signal files written this sweep (4)

- **am-001** — Unit 42 (A) Siemens Ruggedcom ROX II OT-switch zero-day trilogy (CVE-2025-40947/40948/40949; max CVSS 9.1). Net-new A-grade OT/ICS zero-day disclosure; structural/indirect A&D relevance (thematic, not a hard watchlist hit — grader call). vuln-tracker candidate.
- **am-002** — SecurityWeek (B) Pentagon CMMC Phase 2 suspension — Feedback Friday industry-reactions roundup. A&D/DIB standing-section material; follow-on to raw-2026-07-14-flash-0600-001.
- **am-003** — MSTIC (A) ACR Stealer ClickFix intrusion chains (enterprise credential theft; ClickFix TTP proliferation). Borderline (commodity MaaS, no roster actor) but A-grade primary on a corpus-tracked cross-cutting TTP.
- **am-004** — BleepingComputer (B) new LegacyHive Windows zero-day pickup — VT-042 / Nightmare Eclipse `vuln_watch_keywords` corroboration; net-new major-outlet relay (07:05 EDT, post-06:00-FLASH).

## Absorbed by 06:00 FLASH sweep (anti-noise — NOT re-signaled)

- BleepingComputer "CISA urges immediate action on actively exploited Fortinet FortiSandbox flaws" (CVE-2026-25089 / CVE-2026-39808; 03:03 EDT) — VT-045/VT-046, KEV-listed 2026-07-16, due 2026-07-19. Already tracked; FLASH note "VT-045/046 KEV relays absorbed."
- SecurityWeek "Fresh SharePoint Vulnerability Exploited Soon After Disclosure" (03:15 EDT) — on-prem SharePoint exploited-RCE cluster (VT-038 CVE-2026-45659 authenticated / VT-041 CVE-2026-58644 unauth). Already tracked; VT-041 KEV flip captured in v18 index + 2026-07-16 afternoon brief.

## Discarded (no watchlist / roster / vuln-index match)

- BleepingComputer "Windows Server 2022 reach end of mainstream support in 90 days" — lifecycle news, not threat intel.
- BleepingComputer "US charges two over laundering $43 million from investment fraud" — crypto money-laundering LE case; no A&D / roster / vuln nexus.
- BleepingComputer "New ClickLock macOS malware traps users into revealing login password" (Bill Toulas, 17:52 EDT) — commodity macOS infostealer; no roster actor / no A&D / no tracked CVE. (Consistent with prior MacSync/ClickFix-stealer discards.)
- SecurityWeek "Cyberattack Disrupts Operations of Japanese Frozen Food Giant Nichirei" — food-sector disruption; no A&D / roster / vuln nexus.
- SecurityWeek "Risk Ledger Raises $32 Million in Series B Funding" — funding news.
- SecurityWeek "Coca-Cola Suspends US Fairlife Production Due to Ransomware Attack" — consumer-goods ransomware; no A&D / roster / vuln nexus.
- Unit 42 "AI, Automation and Attacks: Unpacking the Unit 42 2026 Global IR Report" — insights/opinion report recap; no specific threat / actor / vuln.
- SANS ISC Stormcast podcast (2026-07-17) — awareness-only, no diary body.

## Source-health note

All queried RSS/JSON sources returned 200 and parsed cleanly; no new stale flips
or recoveries this sweep. mandiant / msrc / ars-security carry prior stale state
(not retried this pass). No credential exposure observed. No prohibited-query
patterns. No active-recon tooling invoked (passive OSINT + first-party feeds only).
