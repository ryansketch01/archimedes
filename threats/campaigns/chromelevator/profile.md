---
campaign_id: chromelevator
aliases: [ChromeLevator, Symantec MuddyWater multi-victim 2026-05]
status: active
first_observed: 2026 (campaign window; specific start per Symantec)
last_observed: 2026-05-13
attributed_actors:
  - actor_id: "022"
    actor_name: MuddyWater
    threat_level: LOW            # roster level; per-category Espionage is composite 7 MEDIUM
    confidence: per-Symantec-single-source
    attribution_source: "Symantec Threat Hunter Team (single-source veto on attribution leg per INTEL-GRADING)"
attribution_caveats: |
  Single-source attribution from Symantec. WEP cap at "likely" per single-source
  veto rule. Independent A/B-grade corroboration not yet observed.
sectors_targeted: [MENA-government, telecom, oil-and-gas]
geographies: [MENA primarily — per MuddyWater historical pattern]
named_victims: []                # multi-victim per Symantec framing; specific names not in corpus excerpt
ad_relevance: sector-adjacency-not-target-specific
ad_relevance_rationale: |
  MuddyWater historical targeting is MENA government / telecom / oil-and-gas —
  not US A&D primes. ChromeLevator continues that pattern. Per /update-tracking
  2026-05-09, MuddyWater Intent=3 (Sector Association) bound by red-team qualify
  directive — Rapid7 names no A&D primes; historical MENA pattern is sector-shaped,
  not target-specific.
related_briefs:
  - threats/briefs/2026-05-13-flash-1800-symantec-muddywater-chromelevator-multi-victim.md
related_actors_referenced: [MuddyWater]
related_vulnerabilities: []
tracked_since: 2026-05-13
last_reviewed: 2026-05-13
next_review_due: 2026-08-13
dossier_version: 1
tlp: CLEAR
---

# Campaign — ChromeLevator (MuddyWater multi-victim)

## Status

**Active.** First Archimedes-corpus surface 2026-05-13 via Symantec disclosure (FLASH 18:00 EDT). Symantec framed as "multi-victim" — specific named-victim count pending source detail.

## Attribution

**MuddyWater** (roster #022, LOW). Attribution is **per Symantec single-source**, with INTEL-GRADING single-source-veto cap at "likely" pending independent A/B-grade corroboration. Per Hard Rule 2, Archimedes restates Symantec's attribution; it does not originate.

72h auto-downgrade clock applies per standing RETRACTION-POLICY pattern: if no second A/B-grade vendor publishes corroborating attribution within 72 hours of FLASH disclosure, attribution leg drops from A2 to C3 ("possibly true"); campaign forensics hold at the source-reported level.

## Mechanism

Reported by Symantec Threat Hunter Team — see FLASH brief for technical detail. Surface-level: chrome-themed lure / loader pattern (campaign name "ChromeLevator" appears to reference the lure mechanism). Specifics in the FLASH brief.

## A&D relevance

**Sector adjacency, not target-specific.** MuddyWater's documented victim profile is MENA government, telecom, and oil-and-gas — not US A&D primes. Per the threat-box scoring run 2026-05-09, the actor was held to Intent=3 (Sector Association) because Rapid7 (the prior corpus source) named no A&D primes, and historical MENA pattern is sector-shaped rather than prime-direct.

ChromeLevator continues the historical pattern.

## Source citations

- FLASH brief 2026-05-13 18:00 (Symantec / MuddyWater / ChromeLevator)
- Symantec Threat Hunter Team disclosure (primary source)
- /update-tracking 2026-05-09 (MuddyWater scoring run — context for Intent binding)

## Related Archimedes records

- **Actor:** [MuddyWater dossier](../../threat-actors/MuddyWater/profile.md) — actor #022, LOW
- **Briefs:** see frontmatter `related_briefs:`
- **Prior MuddyWater finding:** finding-2026-05-06-FLASH-0002 (Rapid7 — auto-downgraded 2026-05-09 to C3 after 72h corroboration window closed unbroken)

## Operator notes

Independent A/B-grade corroboration (Mandiant / Unit 42 / MSTIC / Volexity) on attribution leg is the canonical re-grade-up trigger. Splunk hunt opportunity opens once Symantec publishes hashes / C2 / domain IOCs — currently absent from FLASH brief excerpt.
