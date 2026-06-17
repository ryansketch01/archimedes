---
raw_id: raw-2026-06-17-am-005-sa-paganini-fishmonger-sprysocks-windows-fifth-publisher-relay
collected_at: 2026-06-17T07:42:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityaffairs
  source_name: Security Affairs
  source_url: https://securityaffairs.com/193728/apt/china-linked-fishmonger-ports-sprysocks-to-windows-with-kernel-level-stealth-and-uefi-bootkit-hints.html
  published_at: 2026-06-17T08:10:45+00:00
match_reason:
  watchlist: []
  actors: [FishMonger]
  vulnerabilities: [CVE-2023-24932]
  keywords: [FishMonger, SprySOCKS, ESET, Earth Lusca, Aquatic Panda, Charcoal Typhoon, RedHotel, Winnti, i-Soon, BlackLotus, UEFI bootkit, kernel driver, Print Spooler, Honduras, Taiwan, Thailand, Pakistan]
triage_tags: [substrate_strengthening_finding_2026_06_16_0001, fifth_publisher_relay, vendor_ir_single_source_veto_persists, uefi_bootkit_hint_substrate]
iocs_extracted: false
iocs_count: 0
text_word_count: 305
promoted: true
promoted_to_finding: finding-2026-06-17-0004
promoted_at: 2026-06-17T08:15:00-04:00
ttl_expires_at: 2026-09-15T07:42:00-04:00
---

# China-Linked FishMonger Ports SprySOCKS to Windows With Kernel-Level Stealth and UEFI Bootkit Hints

**Source:** Security Affairs (https://securityaffairs.com/193728/apt/china-linked-fishmonger-ports-sprysocks-to-windows-with-kernel-level-stealth-and-uefi-bootkit-hints.html)
**Author byline:** Pierluigi Paganini
**Published:** 2026-06-17T08:10:45+00:00 (04:10:45 EDT)

## RSS-summary captured

> China-linked FishMonger used two SprySOCKS Windows variants that leveraged kernel drivers and the Print Spooler to target governments in four countries.

## Extraction notes

- **Language:** en
- **Publisher byline:** Pierluigi Paganini (Security Affairs)
- **Article type:** trade-press editorial relay of ESET WeLiveSecurity primary research with significant body summarization (~700 word article body retrieved via fetch_feed RSS content full body)
- **Upstream primary:** ESET (Martin Smolar) — captured AM 2026-06-16 as raw-2026-06-16-am-001 → finding-2026-06-16-0001
- **Cross-walk:** Same trigger-topic carry-forward from AM brief 2bde07c finding-2026-06-16-0001 + PM brief 8fc1987 UPDATE pivot (BC+THN+DR triple-publisher) + 2026-06-17 06:00 sweep SA-Paganini quadruple-publisher journalistic relay flag. Per 06:00 sweep notes, SA-Paganini extends to quadruple-publisher (BC + THN + DR + SA). This raw-signal captures the SA piece directly. **This is the same SA article noted in the 06:00 sweep**, but published 2026-06-17 08:10 UTC = 04:10 EDT — slightly post-06:00 sweep close, so this is a re-confirmation rather than net-new substrate.
- **Net-new substrate via SA full-body retrieval:** SA piece adds depth not in RSS summary — UEFI bootkit hint citing potential CVE-2023-24932 (BlackLotus) exploitation; WIN_DRV kernel driver named RawWNPF + DriverLoader; WIN_PLUS Print Spooler injection via svchost.exe; TCP traffic diversion mechanism; SprySOCKS-Trochilus-RedLeaves codebase lineage with Webworm + SixLittleMonkeys cluster overlap; victim countries Honduras + Taiwan + Thailand + Pakistan 2023-2024 deployment window.
- **Hard Rule 6 preservation:** 15-word quote discipline preserved — RSS-summary quote at-cap; longer body quotes paraphrased.
- **Hard Rule 2 preservation:** ESET-originated cluster identity "FishMonger" preserved verbatim. ESET-asserted cross-walk to Earth Lusca / Aquatic Panda / Charcoal Typhoon / RedHotel + i-Soon contractor attribution preserved per ESET statement. Archimedes does NOT originate any further cross-walk to APT41 (Winnti umbrella).
- **Raw IOC extraction invoked:** no (relay-layer article; IOCs already at ESET upstream primary in raw-2026-06-16-am-001)

## Substrate observation for grader

**Quadruple-publisher journalistic relay confirmed (BC + THN + DR + SA).** Substrate-strengthening for finding-2026-06-16-0001 on publisher-independence layer. Single-vendor-IR-firm-on-cluster-identity-layer veto still applies — Mandiant / CrowdStrike / Unit 42 / MSTIC independent IR-vendor corroboration of FishMonger==i-Soon-contractor cluster identity remains substrate-that-would-lift-veto.

UEFI-bootkit-hint via CVE-2023-24932 is potentially novel substrate not in earlier relays — escalates A&D-relevance via persistence-survives-OS-reinstall threat model. Possible morning brief substrate-strengthening one-liner. ESET hedge language "limited indications suggesting the possible use" preserved verbatim per Hard Rule 2.
