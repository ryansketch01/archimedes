---
raw_id: raw-2026-05-28-flash-1800-000-sentinel-clean-sweep
collected_at: 2026-05-28T18:02:00-04:00
run_id: flash-sweep-20260528-180000
collection_mode: flash_sweep
source:
  source_yaml_id: sentinel
  source_name: FLASH 1800 sentinel clean sweep
  source_url: null
  published_at: 2026-05-28T18:02:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, clean-sweep, flash-1800]
triage_tags: [sentinel, clean_sweep, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 320
promoted: false
ttl_expires_at: 2026-08-26T18:02:00-04:00
---

# FLASH 1800 Sentinel — Clean Sweep, 2026-05-28

Window: 2026-05-28T16:00:00-04:00 → 2026-05-28T18:02:00-04:00 (afternoon brief commit ed16a5f → now).

## Sources swept

- BleepingComputer RSS — 1 in-window item (BTMOB Android MaaS, 21:10 UTC). DISCARDED — commodity LatAm crimeware, no A&D / no tracked actor / no CVE / no IOC. No trigger match.
- The Record RSS — 0 in-window items.
- CISA Advisories all.xml — 0 in-window items.
- SecurityWeek RSS — 0 in-window items.
- Unit 42 (feedburner) — 0 in-window items.
- MSTIC parent feed — 0 in-window items.
- The Hacker News — 0 in-window items (top items dated 2026-05-28 earlier in day already covered: FortiClient EMS CVE-2026-35616 = FLASH-1200-001, Gogs zero-day = FLASH-1200-002, MSRC Chaotic Eclipse = FLASH-1200-003).
- Krebs on Security — 0 in-window items (most recent 2026-05-25).
- SANS ISC — 0 in-window items.
- Cisco Talos — 0 in-window items.
- Security Affairs — 0 in-window items.
- Proofpoint — read timeout (one-off, not a stale flip).

## CISA KEV check

KEV JSON: zero entries dated 2026-05-28. Most recent dateAdded values: 2026-05-27 (3 entries — Nx Console CVE-2026-48027, TanStack CVE-2026-45321, Daemon Tools Lite CVE-2026-8398, all in afternoon brief carry-forwards), 2026-05-26 (LiteSpeed CVE-2026-48172), 2026-05-22 (Drupal CVE-2026-9082).

## Splunk first-party

`index=defenseclaw_local OR index=archimedes earliest=-24h@h` — only archimedes operational events (14 archimedes:operation, 17 archimedes:scheduler). Zero defenseclaw_local events. Zero IOC hits.

## Anti-noise

Already-covered today (NOT re-triggered):
- FortiClient EMS CVE-2026-35616 (FLASH-1200-001, Arctic Wolf ITW)
- Gogs zero-day RCE (FLASH-1200-002, Rapid7 no-patch)
- MSRC Chaotic Eclipse pushback (FLASH-1200-003)
- All 7 PM brief findings (CENTCOM/Wyden, The Gentlemen MSTIC, Nx Console CISA federal escalation, FBI/Group-IB Ghost Stadium, GCHQ/Russia subsea, GreyVibe WithSecure, CISA ICS batch)

## Trigger evaluation

- Trigger 1 (critical CVE + ITW): No new entries.
- Trigger 2 (tracked actor attribution): No new attribution.
- Trigger 3 (first-party IOC hit): Splunk clean.
- Trigger 4 (tracked actor TTP change): None.
- Trigger 5 (A&D sector campaign): None.
- Trigger 6 (zero-day no patch): No new entries.

**Disposition:** NO TRIGGERS. Sentinel-only.

## Source-health changes

None proposed this sweep. Proofpoint timeout was a single read failure; held healthy pending next-sweep retry per source-health policy.
