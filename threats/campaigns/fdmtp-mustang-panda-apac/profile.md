---
campaign_id: fdmtp-mustang-panda-apac
aliases: [FDMTP RAT campaign, Twill Typhoon APAC, Mustang Panda APAC 2025-2026, TA416 APAC]
status: active
first_observed: 2025-09
last_observed: 2026-04 (per Darktrace reporting window; surface published 2026-05-14)
attributed_actors:
  - actor_id: null            # NOT in roster — /new-actor flagged in 2026-05-14 brief
    actor_name: Twill Typhoon / Mustang Panda / TA416
    threat_level: not-tracked
    confidence: per-Darktrace-single-source
    attribution_source: "Darktrace single-source. WEP cap at 'likely' per single-source veto."
attribution_caveats: |
  Single-source attribution from Darktrace. WEP cap at "likely" per
  INTEL-GRADING single-source veto. Mustang Panda / TA416 is a well-established
  Chinese-attributed actor in prior corpus reporting (Mandiant, Microsoft,
  Cisco Talos); the FDMTP-modular-.NET-RAT introduction is the novel element
  in this campaign. Financial-sector targeting is an outlier vs. Mustang
  Panda's historical NGO / journalist profile.
sectors_targeted:
  - financial
  - unspecified (per Darktrace framing)
geographies: [APAC, Japan]
named_victims: []
ad_relevance: low
ad_relevance_rationale: |
  No A&D-prime named victim. Sector profile (financial + unspecified APAC) is
  outside the US A&D target profile. Tradecraft (FDMTP modular .NET RAT) is
  notable for defensive detection-engineering teams as a new variant, but the
  campaign itself does not implicate DIB partner exposure.
related_briefs:
  - threats/briefs/2026-05-14-morning.md
  - threats/briefs/2026-05-14-afternoon.md
related_actors_referenced:
  - Twill Typhoon
  - Mustang Panda
  - TA416
related_vulnerabilities: []
tracked_since: 2026-05-14
last_reviewed: 2026-05-14
next_review_due: 2026-08-14
dossier_version: 1
tlp: CLEAR
---

# Campaign — FDMTP / Mustang Panda APAC

## Status

**Active.** Per Darktrace single-source reporting, campaign window is **2025-09 → 2026-04**. Published 2026-05-14 via SecurityWeek aggregation of Chinese-APT expansion coverage.

## Attribution

**Twill Typhoon / Mustang Panda / TA416** per Darktrace single-source. Multi-name convention reflects vendor disagreement on canonical naming — Twill Typhoon is Microsoft's designation, Mustang Panda is CrowdStrike's, TA416 is Proofpoint's.

NOT currently a roster entry. `/new-actor` flagged in the 2026-05-14 morning brief. The actor itself is well-established in pre-Archimedes-corpus reporting (Mandiant, Microsoft, Cisco Talos historical coverage 2020-2025); the **FDMTP modular .NET RAT** is the novel element this campaign introduces.

Per Hard Rule 2, the attribution to Twill Typhoon / Mustang Panda is Darktrace-originated and Archimedes restates it. Per single-source veto, WEP on the attribution leg is capped at "likely."

## Mechanism

- **FDMTP modular .NET RAT** — new malware family attributed to Twill Typhoon's tooling
- Modular architecture; specific module taxonomy in the Darktrace source
- APAC + Japan targeting per source framing

**Financial-sector targeting is an outlier** vs. Mustang Panda's historical profile (NGO / journalist / regional government). Source framing suggests either an opportunistic pivot or a sub-cluster within the actor.

## A&D relevance

**Low.** No A&D-prime named victim. Financial-sector APAC focus is outside the US A&D target profile. Tradecraft note (the new FDMTP RAT) is relevant for **defensive detection-engineering teams** maintaining EDR coverage against Chinese-attributed tooling — push FDMTP YARA / behavioral indicators to detection inventory when published.

## Source citations

- Darktrace (primary source for FDMTP RAT analysis)
- SecurityWeek aggregation: https://www.securityweek.com/chinese-apts-expand-targets-update-backdoors-in-recent-campaigns/
- 2026-05-14 morning brief (Archimedes capture)

## Related Archimedes records

- **Actor:** Twill Typhoon / Mustang Panda / TA416 — **NOT in roster**; `/new-actor` flagged
- **Briefs:** see frontmatter `related_briefs:`
- **Linked campaign:** [Salt Typhoon Azerbaijan Energy](../salt-typhoon-azerbaijan-energy/profile.md) — separate Chinese-APT campaign, co-mentioned in 2026-05-14 brief's "Chinese APTs expand targets" theme
- **Related finding (referenced in brief, not yet verified on disk):** finding-2026-05-14-0007

## Operator notes

`/new-actor "Twill Typhoon"` (or Mustang Panda / TA416 — operator chooses canonical name) is the next operator action if scaffolding desired. Multi-name convention should be captured in the dossier `aliases:` list.
