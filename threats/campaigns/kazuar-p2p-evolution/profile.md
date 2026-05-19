---
campaign_id: kazuar-p2p-evolution
aliases: [Kazuar P2P botnet, Secret Blizzard architectural evolution, Turla Kazuar evolved]
status: active                                # tracking status; see caveat below
status_caveat: |
  "Active" here means under-current-Archimedes-corpus-tracking. The MSTIC
  publication is an ARCHITECTURAL deep-dive, not a 2026 fresh-incident
  attribution. Per the 2026-05-14 morning brief: "architectural analysis,
  not fresh-incident attribution — no 2026 victim named. Per analyst ACH,
  the historical/baseline reading dominates."
first_observed: pre-2026 (architectural evolution; historical Kazuar prior)
last_observed: 2026-05-14 (publication date of MSTIC deep-dive)
attributed_actors:
  - actor_id: null            # NOT in roster — /new-actor strong-flagged
    actor_name: Secret Blizzard / Turla / FSB Center 16
    threat_level: not-tracked
    confidence: per-MSTIC + CISA citation
    attribution_source: "Microsoft MSTIC publication 2026-05-14; FSB Center 16 attribution per CISA citation (relayed via MSTIC)."
attribution_caveats: |
  MSTIC attribution is A-grade. FSB Center 16 specifically is sourced via
  CISA per MSTIC's citation chain. Per Hard Rule 2, Archimedes restates the
  MSTIC+CISA attribution; it does not originate.
  PER 2026-05-14 brief: "A&D-campaign signal unlikely" — this is a baseline
  framing, not a fresh-incident escalation.
sectors_targeted:
  # Verbatim per MSTIC framing (preserved per quote discipline)
  - ministries of foreign affairs
  - embassies
  - government offices
  - defense departments
  - defense-related companies worldwide
geographies: [worldwide per MSTIC]
named_victims: []               # NO 2026 victim named per MSTIC publication
ad_relevance: historical-baseline-A&D-signal-unlikely
ad_relevance_rationale: |
  MSTIC targeting language includes "defense departments" and "defense-related
  companies worldwide" — verbatim. However, no 2026 victim is named, and the
  publication frames as architectural evolution of long-established tooling
  (Kazuar). Per analyst ACH, the historical/baseline reading dominates the
  fresh-incident reading. Worth tracking for EDR-hash deployment;
  not worth FLASH-tier prioritization.
related_briefs:
  - threats/briefs/2026-05-14-morning.md
related_actors_referenced: [Secret Blizzard, Turla, FSB Center 16]
related_vulnerabilities: []
tracked_since: 2026-05-14
last_reviewed: 2026-05-14
next_review_due: 2026-08-14
dossier_version: 1
tlp: CLEAR
---

# Campaign — Kazuar P2P Botnet Evolution

## Status

**Tracked — architectural evolution, not fresh-incident.** First Archimedes-corpus surface 2026-05-14 via MSTIC publication. Per the morning brief's analyst note: *"architectural analysis, not fresh-incident attribution — no 2026 victim named. Per analyst ACH, the historical/baseline reading dominates."*

This dossier exists primarily to **track the four published SHA256 hashes for EDR deployment** and to anchor the actor (Secret Blizzard / Turla) when a future fresh-incident reporting surfaces.

## Attribution

**Secret Blizzard / Turla / FSB Center 16** per MSTIC publication 2026-05-14. NOT currently a roster entry; **/new-actor strong-flagged** in the 2026-05-14 morning brief.

- **Microsoft MSTIC** is the A-grade publication source.
- **FSB Center 16** specifically is attributed via **CISA citation** as relayed by MSTIC.

Per Hard Rule 2, the FSB Center 16 attribution is source-chained (MSTIC → CISA); Archimedes does not originate it.

## Mechanism (architectural)

MSTIC describes Kazuar's evolution into a **modular peer-to-peer botnet** with three modules:

- **Kernel** — coordination layer
- **Bridge** — communication layer
- **Worker** — payload execution layer

Plus:

- **Leader election** — among Worker nodes, suggesting a resilient, decentralized control plane
- **Pelmeni dropper** — first-stage delivery mechanism

This is an **evolution** of a long-established Kazuar tooling lineage; not novel-introduction reporting.

## Victim sectors (per MSTIC, verbatim)

> *"ministries of foreign affairs, embassies, government offices, defense departments, and defense-related companies worldwide"*

Verbatim per MSTIC. **No specific 2026 victim is named** in the publication.

## A&D relevance

**Historical baseline; fresh-incident signal unlikely.** MSTIC's targeting language explicitly includes *"defense departments and defense-related companies worldwide"* — which is A&D-adjacent. However:

- No 2026 victim is named
- Publication frames as **architectural evolution** of pre-existing tooling
- Per analyst ACH, the historical/baseline reading dominates

Action item: **push the 4 SHA256 hashes to A&D EDR** (per 2026-05-14 morning brief action). Not FLASH-tier; routine detection-engineering work.

## Source citations

- Microsoft MSTIC (2026-05-14): https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/
- CISA citation chain (per MSTIC) — FSB Center 16 attribution
- 2026-05-14 morning brief (Archimedes capture)

## Related Archimedes records

- **Actor:** Secret Blizzard / Turla / FSB Center 16 — **NOT in roster**; `/new-actor` strong-flagged
- **Briefs:** see frontmatter `related_briefs:`
- **Related finding (referenced in brief, not yet verified on disk):** finding-2026-05-14-0006
- **IOCs to push to A&D EDR:**
  - 4 published SHA256 hashes from MSTIC publication (specific values in source)

## Operator notes

`/new-actor "Secret Blizzard"` (or Turla — operator chooses canonical) is the strong-flagged action. Multi-A-grade pre-Archimedes coverage of Turla exists (Mandiant, Microsoft, CrowdStrike); the actor has a long track record despite no Archimedes-corpus prior. Conservative MEDIUM-band on scoring run, pending evidence-minimum-table check against the A&D target profile.
