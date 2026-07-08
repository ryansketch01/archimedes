---
raw_id: raw-2026-07-08-flash-1200-000
collected_at: 2026-07-08T12:08:00-04:00
run_id: flash-sweep-20260708-120000
collection_mode: flash_sweep
sentinel: true
source:
  source_yaml_id: multiple
  source_name: "FLASH sweep — CISA KEV + BleepingComputer + The Hacker News + SecurityWeek + first-party Splunk"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sentinel, clean_sweep, no_flash_trigger]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-06T12:08:00-04:00
---

# FLASH sweep 12:00 EDT 2026-07-08 — CLEAN SWEEP (no FLASH triggers)

Narrow FLASH sweep for the 12:00 EDT window (items new since the 06:00 EDT sweep).
No item matched any of the six FLASH-POLICY trigger conditions. Sentinel written per
FLASH-POLICY anti-noise discipline.

## Sources swept (6h window: 2026-07-08T06:00 → 12:00 EDT)

- **CISA KEV** (JSON catalog) — catalog version **2026.07.07**, released 2026-07-07T18:28Z.
  **No new additions dated 2026-07-08.** The four entries dated 2026-07-07
  (CVE-2026-48282 Adobe ColdFusion, CVE-2026-55255 Langflow, CVE-2026-48908 JoomShaper
  SP Page Builder, CVE-2026-56290 Joomlack Page Builder CK) are all already covered by
  the 06:00 sweep + morning brief (anti-noise). No net-new KEV trigger material.
- **BleepingComputer** — 3 items in window: KDDI telecom breach (12M affected, Japan),
  DuckDuckGo YouTube ad-blocking, and a sponsored Specops post. None A&D / roster-actor /
  tracked-CVE. No FLASH.
- **The Hacker News** — 6 items in window (see below). None matched a FLASH trigger.
- **SecurityWeek** — 5 items in window (see below). None matched a FLASH trigger.
- **First-party Splunk** (`archimedes` + `defenseclaw_local`, last 24h) — 0 hits on tracked
  IOCs. Targeted sweep on newest tracked C2 (Cavern Manticore `hospitalinstallation[.]com`)
  and a broad IOC-tag/threat-match sweep both returned zero events. Trigger 3 clean.

## FLASH trigger evaluation — all six negative

1. **critical-cve-exploited** — no NEW CVSS≥9.0 + confirmed-active-exploitation + A-grade
   item. (The only CVSS-10.0 item in window is Ubiquiti UniFi CVE-2026-50746 — PATCHED,
   no ITW exploitation reported; fails the active-exploitation limb. See non-FLASH notes.)
2. **tracked-actor-attribution** — no new attribution to any of the 26 roster actors.
3. **first-party-ioc-hit** — Splunk clean, 0 hits.
4. **tracked-actor-ttp-change** — LapDogs "Leash" backdoor expansion (SecurityWeek/Cisco)
   involves a China-linked APT **not on the roster**; fails the tracked-actor limb.
5. **ad-sector-campaign** — no active multi-victim campaign vs aerospace/defense/watchlist.
6. **zero-day-no-patch** — no unpatched ≥8.0 zero-day with confirmed/imminent exploitation.

## Non-FLASH items noted for grader / morning awareness (NOT raw-signaled)

- **Ubiquiti UniFi multi-product critical patches — CVE-2026-50746 (CVSS 10.0)** (THN).
  Improper access control in UniFi Connect; privilege escalation / arbitrary command
  execution. **Patched proactively; no in-the-wild exploitation reported.** Not A&D.
  Fails Trigger 1 (no active exploitation) and Trigger 6 (patch available). Grader may
  consider for morning if a consumer/SOHO-network angle emerges; below FLASH floor now.
- **"China-Linked APT Expands Arsenal With New 'Leash' Backdoors" — LapDogs campaign**
  (SecurityWeek, Cisco/Talos as originating). LongLeash / DogLeash / JarLeash SOHO-router
  backdoors. China-linked but **LapDogs is not in `_roster.yaml`** — potential /new-actor
  candidate for operator review, NOT a FLASH (fails Trigger 4 tracked-actor limb; SOHO
  routers, not an A&D-sector multi-victim campaign for Trigger 5).
- **CISA ColdFusion/Langflow/Joomla patching urging** (SecurityWeek, Ionut Arghire) —
  media corroboration of the already-covered 2026-07-07 KEV batch. Anti-noise; absorbed
  into morning brief (AM-001) and 06:00 sweep.

## Extraction notes

- Language: en
- Article type: sweep sentinel (no single source article)
- Raw IOC extraction invoked: no (no qualifying item)
- Anti-noise applied: ColdFusion CVE-2026-48282, Joomla cluster CVE-2026-48908 /
  CVE-2026-56290, Langflow CVE-2026-55255 all pre-covered and excluded from candidacy.
