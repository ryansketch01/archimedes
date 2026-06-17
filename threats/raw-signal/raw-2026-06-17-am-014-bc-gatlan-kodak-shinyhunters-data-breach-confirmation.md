---
raw_id: raw-2026-06-17-am-014-bc-gatlan-kodak-shinyhunters-data-breach-confirmation
collected_at: 2026-06-17T07:57:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/kodak-confirms-data-breach-claimed-by-shinyhunters-extortion-gang/
  published_at: 2026-06-17T07:07:56+00:00
match_reason:
  watchlist: []
  actors: [ShinyHunters]
  vulnerabilities: []
  keywords: [Kodak, ShinyHunters, data breach, extortion]
triage_tags: [out_of_ad_scope, possible_substrate_strengthening_shinyhunters_carry_forward, anti_noise_dedup_06_00_sweep]
iocs_extracted: false
iocs_count: 0
text_word_count: 135
promoted: false
rejected_at: 2026-06-17T08:26:00-04:00
rejection_id: reject-2026-06-17-0007
ttl_expires_at: 2026-09-15T07:57:00-04:00
---

# Kodak confirms data breach claimed by ShinyHunters extortion gang

**Source:** BleepingComputer (https://www.bleepingcomputer.com/news/security/kodak-confirms-data-breach-claimed-by-shinyhunters-extortion-gang/)
**Author byline:** Sergiu Gatlan
**Published:** 2026-06-17T07:07:56+00:00 (03:07:56 EDT)

## RSS-summary captured

> Kodak has confirmed that it's working with external cybersecurity experts to investigate a security breach after hackers gained access to some of the company's data.

## Extraction notes

- **Language:** en
- **Publisher byline:** Sergiu Gatlan (BleepingComputer)
- **Article type:** trade-press victim-confirmation reporting
- **Upstream primary:** Kodak (victim) statement
- **Cross-walk:** Same Kodak/ShinyHunters trigger-topic carry-forward from 2026-06-17 06:00 sweep (BC initial publication noted in 06:00 sweep notes; this is now victim-confirmation). ShinyHunters NOT on 24-actor `_roster.yaml`. Kodak imaging/printing NOT A&D/DIB/CMMC/ITAR — out-of-A&D-scope.
- **Anti-noise:** Same trigger-topic already discarded out-of-A&D-scope in 06:00 sweep — anti-noise rule 1 in effect.
- **Hard Rule 6 preservation:** 15-word quote discipline preserved.
- **Hard Rule 2 preservation:** ShinyHunters attribution recorded per BC + Kodak source. NOT cross-walked.
- **Raw IOC extraction invoked:** no

## Substrate observation for grader

T2 FAIL ShinyHunters NOT roster. T5 FAIL Kodak NOT A&D. T1/T3/T4/T6 FAIL no CVE. Critical-override 0-of-4. Non-FLASH-eligible.

Discarded as out-of-A&D-scope (anti-noise dedup from 06:00 sweep). Cross-reference with Mandiant direct page #3 "ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit" — ShinyHunters cluster expanding across imaging/printing (Kodak) + education sector (Salesforce/Infinite Campus + Glendale CC / Moody Bible / Illinois CC / Houston City CC per Security Affairs raw-NEW-edtech below).
