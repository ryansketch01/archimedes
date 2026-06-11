---
raw_id: raw-2026-06-11-pm-003
collected_at: 2026-06-11T15:50:00-04:00
run_id: pre-brief-20260611-153000
collection_mode: pre_brief_collection
sources:
  - source_yaml_id: the-record
    source_name: The Record (Recorded Future News)
    source_url: https://therecord.media/hacker-linked-to-void-blizzard-faces-charges
    grade: B
    published_at: 2026-06-11T15:17:00-04:00
match_reason:
  watchlist: [aerospace-defense]
  actors: ["Void Blizzard (NOT in Archimedes roster — /new-actor candidacy + operator awareness)"]
  vulnerabilities: []
  keywords: [Void Blizzard, Russian, GRU, FSB, defense contractors, cyberespionage, extradition, DOJ, Thailand, Boston]
triage_tags:
  - russian_cyberespionage_attribution
  - defense_contractor_targeting_named_in_source_language
  - new_actor_candidacy_flag
  - DOJ_indictment_continuity_to_cluster_2026-06-04_fbi_doj_seizures
  - ad_sector_direct_per_source_language
  - non_flash_attribution_to_non_roster_actor
iocs_extracted: true
iocs_count: 0
text_word_count: 900
promoted: true
promoted_to_finding: finding-2026-06-11-0007
promoted_at: 2026-06-11T16:45:00-04:00
ttl_expires_at: 2026-09-09T15:50:00-04:00
---

# Denis Obrezko — DOJ charges Russian national in Void Blizzard cyberespionage; defense contractors named in victim profile

## Summary — material A&D-direct attribution surface

A DOJ federal indictment, unsealed via initial Boston court appearance 2026-06-10, charges 36-year-old Russian national Denis Obrezko with infrastructure-provider role in the **Void Blizzard** cyberespionage cluster. The Record (B-grade) describes Void Blizzard victim profile as including **"defense contractors"** alongside government agencies, transportation, media, healthcare, and NGOs — across Europe and North America.

This is the first surface in the Archimedes corpus to name "defense contractors" as a Void Blizzard victim category. Void Blizzard is **NOT in the Archimedes roster** as of the 2026-05-10 v2 — operator awareness flag for `/new-actor` candidacy and Iran/China/Russia tracking expansion.

## Subject

- **Name:** Denis Obrezko
- **Age:** 36
- **Nationality / origin:** Russian (Stavropol)
- **Arrest:** November 2025, Phuket, Thailand (joint FBI–Thai Royal Police operation)
- **Transfer:** Extradited to U.S. custody
- **Initial federal court appearance:** Boston, 2026-06-10
- **Status:** In custody

## Alleged role

Per The Record (relaying DOJ filing):
- Provided infrastructure used to support Void Blizzard cyber operations.
- Used cryptocurrency transactions to purchase virtual private servers and internet domains used as attack infrastructure.
- Facilitated unauthorized computer access targeting U.S. and foreign organizations.

## Victims named in source language

- At least 11 U.S. companies compromised per prosecutors.
- Prosecutors believe actual victim count is significantly higher than 11.
- Void Blizzard victim profile per source: **"government agencies, defense contractors, transportation, media, healthcare, and NGOs"** across Europe and North America.
- Operational pattern: Stolen credentials → email and document theft.

## Attribution per source (Hard Rule 2 — relay only, no origination)

The Record characterizes Void Blizzard as: **"relatively new threat group operating in support of Russian government interests."** No specific GRU / FSB / SVR unit attribution in this source. The "Russian government interests" framing is the Microsoft-tier weather-system naming convention (Microsoft is the originator of the "Blizzard" Russia-attribution naming for actors); Void Blizzard appears in MSTIC reporting from late 2024 onward as a credential-theft-focused Russia-aligned actor.

## A&D / DIB relevance

- **Source-direct A&D language:** "defense contractors" is in The Record's literal victim-profile language for Void Blizzard. This is a B-grade media relay paraphrasing DOJ filing language — not a defense-prime-victim-named surface, but it is the strongest A&D-direct phrasing observed today.
- **Sector-targeting evidence is general-population (multi-sector across two continents):** does not isolate A&D as primary focus.
- **Roster gap:** Void Blizzard is not currently a tracked Archimedes actor. Given (a) A1-tier Microsoft naming origin, (b) DOJ-charged operator now in U.S. custody, and (c) source-named defense-contractor victim category, this warrants **`/new-actor` candidacy review** at operator discretion.

## Continuity to 2026-06-04 + 2026-06-11 morning brief cluster

- 2026-06-04 PM: Five Eyes "Safeguarding Our Secrets" counterintelligence advisory.
- 2026-06-11 AM (`finding-2026-06-11-0002`): FBI/DOJ 13-website seizures tied to Chinese intelligence recruiting US-cleared personnel — operator-graded `very_likely` cluster anchor.
- 2026-06-11 PM (this signal): DOJ Russian Void Blizzard infrastructure-provider indictment.

The three events together suggest a sustained **DOJ/FBI counter-cyberespionage operational tempo** across both China-attribution and Russia-attribution surfaces in a 7-day window. Temporal proximity, not confirmed campaign continuity — collector observation, grader/analyst will decide whether to cluster.

## FLASH trigger evaluation — non-FLASH

- Trigger 2 (tracked-actor-attribution): Void Blizzard is **NOT in roster** — does not satisfy.
- Trigger 5 (ad-sector campaign): Multi-sector cyberespionage with defense-contractor exposure; not a defense-prime-named active-campaign report — does not satisfy.
- Action: Tag as `non_flash`, queue for afternoon brief Iran-Cyber-adjacent / russia-watch reporting line if briefer elects to surface; flag for operator `/new-actor` consideration.

## Why not FLASH despite "defense contractors" in source

The "defense contractors" framing is part of the **Microsoft-MSTIC longitudinal Void Blizzard victim profile** as relayed by The Record — NOT a defense-prime-named victim in this indictment specifically. The 11 U.S. companies are not enumerated. Per FLASH-POLICY Trigger 5 (ad-sector-campaign), "targets include aerospace defense or watchlist entity" + "multi-victim confirmed" both need to be true with named-victim grounding, not relay-tier paraphrased sector taxonomy. Conservative call: collect, do not FLASH, surface to briefer for Russia-watch line.

## Extraction notes

- Language: en
- Article type: media relay of DOJ federal court filing
- Raw IOC extraction invoked: yes — zero IOCs (court filing narrative; no malware / infrastructure / hashes published yet in this relay)

## IOCs (from ioc-extraction skill)

```yaml
iocs: []

attribution_claims:
  - actor: Void Blizzard
    nation: RU (per Microsoft naming convention — Blizzard = Russia)
    framing_in_source: "relatively new threat group operating in support of Russian government interests"
    source: therecord (2026-06-11)
    independent_corroboration: false_in_this_signal_alone_but_Microsoft_origination_attribution_is_a1_at_originator_layer
    archimedes_attribution_origination_check: pass_per_hard_rule_2
    roster_status: not_in_archimedes_roster_v2_as_of_2026-05-10
    new_actor_candidacy_recommended: true_for_operator_decision
  - victim_category: defense contractors
    source_language_verbatim_quote_under_15w: "government agencies, defense contractors, transportation, media, healthcare"
    source: therecord (2026-06-11)
    archimedes_treatment: source_language_preserved_no_first_party_archimedes_amplification

extraction_skill_status: ok
```
