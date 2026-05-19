---
campaign_id: salt-typhoon-azerbaijan-energy
aliases: [Salt Typhoon Azerbaijan O&G, FamousSparrow Azerbaijan energy]
status: active
first_observed: 2026 (per source-reported window)
last_observed: 2026-05-13
attributed_actors:
  - actor_id: null            # Salt Typhoon entry exists on roster but not numbered in available extract
    actor_name: Salt Typhoon
    threat_level: HIGH
    confidence: per-FLASH-source
    attribution_source: "Original source per FLASH 2026-05-13 14:30 — see brief"
  - actor_id: null
    actor_name: FamousSparrow
    threat_level: not-tracked
    confidence: per-FLASH-source
    attribution_source: "Co-mentioned in FLASH 2026-05-13 14:30. Relationship to Salt Typhoon: per source framing; not Archimedes-originated."
attribution_caveats: |
  Two actor names in the FLASH brief title (FamousSparrow + Salt Typhoon).
  Per Hard Rule 2, the FamousSparrow-as-Salt-Typhoon framing is source-attributed,
  not Archimedes-originated. Per-source attribution relationship pending the
  briefer's verbatim capture.
sectors_targeted: [energy, oil-and-gas]
geographies: [Azerbaijan]
named_victims: []                # specific names per source; not in available extract
ad_relevance: structural-not-prime-direct
ad_relevance_rationale: |
  Azerbaijan O&G is not a US A&D prime sector. Structural relevance is via
  Salt Typhoon's broader Chinese-APT energy-sector targeting pattern, which
  brushes US energy infrastructure adjacent to DIB supply chains in other
  campaigns. No direct A&D-prime victim named in this surface.
related_briefs:
  - threats/briefs/2026-05-13-flash-1430-famoussparrow-salt-typhoon-azerbaijan-energy.md
related_actors_referenced: [Salt Typhoon]
related_vulnerabilities: []
tracked_since: 2026-05-13
last_reviewed: 2026-05-13
next_review_due: 2026-08-13
dossier_version: 1
tlp: CLEAR
---

# Campaign — Salt Typhoon Azerbaijan Energy

## Status

**Active.** First Archimedes-corpus surface 2026-05-13 via FLASH 14:30 EDT. Subsequent 2026-05-14 morning brief noted continuation through SecurityWeek aggregation: *"Salt Typhoon Azerbaijan O&G in same SecurityWeek aggregation — no new content past yesterday's FLASH."*

## Attribution

**Salt Typhoon** (roster — HIGH) and **FamousSparrow** are both named in the FLASH brief title. The relationship between the two names is per the original source's framing; Archimedes does not originate the "FamousSparrow = Salt Typhoon" identification per Hard Rule 2.

Salt Typhoon is roster-tracked at HIGH. FamousSparrow is not currently a separate roster entry; whether to scaffold via `/new-actor` is a future operator decision (see Connects callout in 2026-05-14 morning brief).

## Mechanism

Per FLASH brief — specific tradecraft / IOCs / campaign timeline in the source document. Surface-level: Chinese-APT energy-sector targeting in the Caucasus.

## A&D relevance

**Structural, not prime-direct.** Azerbaijan O&G is outside the US A&D-prime profile. Structural concern is Salt Typhoon's broader pattern of energy-sector targeting, which has touched US energy infrastructure adjacent to DIB supply chains in other (unrelated) campaigns.

## Source citations

- FLASH brief 2026-05-13 14:30 (FamousSparrow / Salt Typhoon / Azerbaijan energy)
- SecurityWeek aggregation reference per 2026-05-14 morning brief

## Related Archimedes records

- **Actor:** Salt Typhoon on roster — see `threats/threat-actors/_roster.yaml`
- **Briefs:** see frontmatter `related_briefs:`
- **Linked campaign:** FDMTP / Mustang Panda APAC ops — co-mentioned in 2026-05-14 morning brief's Chinese-APT expansion theme (different actor, related theme)

## Operator notes

If a separate FamousSparrow roster entry is desired, `/new-actor FamousSparrow` will scaffold one — with the source-attestation framing preserved. Today the actor is folded under Salt Typhoon's roster entry by source convention.
