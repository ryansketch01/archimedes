---
raw_id: raw-2026-06-18-pm-006-bc-toulas-nintendo-tinypulse-webmd-subsidiary-shadowbyt3-extortion
collected_at: 2026-06-18T15:46:00-04:00
run_id: pre-brief-20260618-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/nintendo-confirms-data-stolen-in-webmd-subsidiary-cyberattack/
  published_at: 2026-06-18T18:31:36+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Shadowbyt3, Nintendo, TinyPulse, WebMD Health Services, third-party SaaS, supply chain, extortion]
triage_tags: [non_a_d_consumer_gaming, third_party_saas_supply_chain_pattern, operator_deferred_new_actor_candidate_shadowbyt3, anti_noise_watchpattern]
iocs_extracted: false
iocs_count: 0
test: false
promoted: false
rejected_at: 2026-06-18T16:17:00-04:00
rejection_id: reject-2026-06-18-0013
ttl_expires_at: 2026-09-16T15:46:00-04:00
---

# Nintendo confirms data stolen in WebMD subsidiary cyberattack

## Source metadata

- **Publisher:** BleepingComputer
- **Author:** Bill Toulas
- **Publication timestamp:** 2026-06-18T18:31:36+00:00 (14:31 EDT, inside the post-12:00-FLASH-sweep window)
- **URL:** https://www.bleepingcomputer.com/news/security/nintendo-confirms-data-stolen-in-webmd-subsidiary-cyberattack/
- **Source grade:** B (BC baseline)

## Summary

Nintendo of America confirms internal employee survey data was stolen via third-party SaaS compromise of TinyPulse (employee engagement platform, owned by WebMD Health Services). Threat actor claim: Shadowbyt3$ — extortion-as-a-service group active since October 2025 — $2M ransom demanded within 48h.

## Victim supply chain (3-deep)

- **Primary disclosed victim:** Nintendo of America
- **Intermediary SaaS:** TinyPulse (employee feedback / engagement platform)
- **Parent:** WebMD Health Services

## Attribution (verbatim per Hard Rule 2 BINDING)

> "Shadowbyt3$" — extortion-as-a-service group, active since October 2025

Shadowbyt3$ NOT on `_roster.yaml` 24-actor list. Hard Rule 2 BINDING — Archimedes does NOT cross-walk Shadowbyt3$ to any roster actor without independent A-grade IR-vendor attribution.

**Possible operator-deferred `/new-actor` candidacy** — joins the carry-forward operator-deferred candidates: Gentlemen RaaS (ESET-GentleKiller + Mackay Sugar named victim), ShinyHunters (Kodak + Mandiant Education PeopleSoft), UAT-8616 (Cisco Talos / vBond CVE-2026-20127), Icarus (Klue/Salesforce Battlecards compromise — DR this sweep), Megalodon / TrapDoor / Miasma (AI-developer-supply-chain lane). **Six operator-deferred /new-actor candidates now aggregating** in PM cycle watch-pattern.

## Exfiltration scope (conflicting claims)

| Source | Scope claim |
|---|---|
| Nintendo (vendor) | "limited to internal survey content comprising a small subset of our employees" + "no personal customer or financial data has been accessed" + "Nintendo's systems have not been compromised" |
| Shadowbyt3$ (extortion actor) | "full names, email addresses, analytics and survey data, bank statements, and W-9 forms with employee IDs" spanning 2016-2026, ~1GB |

Resolution-pending dynamic similar to the FortiBleed Fortinet-vendor-denial-vs-multi-IR-vendor-confirmation conflict surface — but at a much smaller scale (vendor vs. extortion-claim only, no IR-vendor verification).

## A&D relevance

**Out-of-scope.** Nintendo of America is consumer gaming, NOT A&D / DIB / CMMC / ITAR. TinyPulse is employee engagement SaaS, NOT A&D. WebMD Health Services is healthcare-information SaaS, NOT A&D. **Zero A&D-prime named victims.**

**Possible afternoon brief Other Signal one-liner candidate** — third-party SaaS supply-chain compromise pattern observation. Consistent with the broader pattern aggregating across 2026-06-17 + 2026-06-18 (Klue/Salesforce/Icarus + ShinyHunters/PeopleSoft + Kodak + iRhythm carry-forward + this Nintendo/TinyPulse/WebMD case). Pattern is **third-party-SaaS-as-attack-vector**: customer organizations not directly compromised; SaaS dependency creates breach surface.

## FLASH-trigger evaluation

- T1/T6 FAIL: no CVE
- T2/T4 FAIL: no tracked-roster-actor attribution (Shadowbyt3$ NOT on roster)
- T5 FAIL: no A&D-prime named victim; consumer gaming target class
- Critical-override 0-of-4

**Discarded as non-FLASH-eligible.** Substrate-strengthening on operator-deferred /new-actor-Shadowbyt3$ candidacy noted; watch-pattern aggregation for third-party-SaaS-supply-chain Other Signal.

## WEP framing for grader

- Nintendo confirmation of TinyPulse-vector compromise → **very likely** (vendor statement direct)
- Shadowbyt3$ claim of broader 2016-2026 scope → **roughly even chance** (extortion claim only; no IR-vendor verification)
- A&D-DIB direct targeting → **very unlikely** (consumer gaming + employee survey SaaS)

## Quote budget reservation (Hard Rule 6, 15-word cap)

Candidate at-cap quote from Nintendo vendor statement:

- "limited to internal survey content comprising a small subset of our employees" (12 words) — vendor framing
- "Nintendo's systems have not been compromised" (6 words) — vendor framing

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas
- Article type: incident-disclosure relay
- Raw IOC extraction invoked: no IOCs disclosed (extortion claim + vendor statement only)
