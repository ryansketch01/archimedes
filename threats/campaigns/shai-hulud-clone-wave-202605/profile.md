---
campaign_id: shai-hulud-clone-wave-202605
aliases: [Shai-Hulud npm clone wave, Mini Shai-Hulud copy-cat wave 2026-05]
status: active
first_observed: 2026-05-18 (first Archimedes-corpus surface)
last_observed: 2026-05-18
attributed_actors:
  - actor_id: null
    actor_name: UNATTRIBUTED
    threat_level: not-applicable
    confidence: explicit-non-attribution
    attribution_source: "Per Ox Security via BleepingComputer (Bill Toulas, 2026-05-18 13:28 EDT) — clones are EXPLICITLY NOT TeamPCP-attributed."
attribution_caveats: |
  UNATTRIBUTED is the canonical state per source. Per analyst ACH (in
  2026-05-18 afternoon brief), H1 (distinct actor) ties with H3 (copy-cat
  noise riding the Mini Shai-Hulud worm source-code release). C2 on a
  public LocalHost.run anonymizer subdomain is per analyst KAC
  "uninformative for actor-distinction." Hard Rule 2 prevents any
  Archimedes-originated attribution; this dossier preserves UNATTRIBUTED state.
sectors_targeted: [software-supply-chain, npm-ecosystem]
geographies: [global]
named_victims: []               # propagation-stage; specific downstream victims pending
ad_relevance: indirect-supply-chain
ad_relevance_rationale: |
  Materializes the VT-006 derivative-attacks-30d WEP at T+3 days. Same
  structural relevance as Mini Shai-Hulud — npm ecosystem compromise reaches
  DIB CI/CD pipelines that pull from public registries. Distinct from
  Mini Shai-Hulud at the actor layer; same exposure surface for defenders.
related_briefs:
  - threats/briefs/2026-05-18-afternoon.md
related_actors_referenced: []   # explicitly UNATTRIBUTED
related_vulnerabilities: []
tracked_since: 2026-05-18
last_reviewed: 2026-05-18
next_review_due: 2026-06-18      # 30-day review per VT-006 derivative-attacks window
dossier_version: 1
tlp: CLEAR
---

# Campaign — Shai-Hulud npm Clone Wave (2026-05)

## Status

**Active.** First Archimedes-corpus surface 2026-05-18 13:28 EDT via Ox Security reporting (relayed by BleepingComputer / Bill Toulas).

This campaign **materializes the VT-006 derivative-attacks-30d WEP at T+3 days** — i.e., the 2026-05-18 afternoon brief's analyst observation that the public release of Mini Shai-Hulud worm source code on 2026-05-15 was very likely to raise derivative-intrusion volume within ~30 days. The clone wave is the first concrete derivative-actor observation.

## Attribution

**UNATTRIBUTED.** Per Ox Security via BleepingComputer, the clones are **explicitly NOT TeamPCP-attributed**. Per analyst ACH in the 2026-05-18 afternoon brief, two hypotheses tied for leading position:

- **H1: distinct actor** — opportunistic supply-chain operator riding the worm-source-code release
- **H3: copy-cat noise** — generic actor cluster, low-skill, high-volume

The C2 on a public **LocalHost.run anonymizer subdomain** is per analyst KAC "uninformative for actor-distinction" — anonymizer infrastructure is precisely the operator-signal you'd expect from either H1 or H3.

Per Hard Rule 2, this dossier preserves the UNATTRIBUTED state. The clones are **not** to be folded under TeamPCP without an independent corroborating source.

## Mechanism

**Four malicious npm packages** identified at first surface (more very likely follow over the 30-day window):

- `chalk-tempalte` *(typo-squat on `chalk-template`)*
- `@deadcode09284814/axios-util`
- `axois-utils` *(typo-squat on `axios-utils`; adds DDoS payload per source framing)*
- `color-style-utils`

**Defensive action item (from 2026-05-18 afternoon brief):** Add all four package names to dependency-quarantine inventory.

**C2 infrastructure:** `87e0bbc636999[.]lhr[.]life` on a public LocalHost.run anonymizer subdomain. Defanged notation per Archimedes IOC convention.

## A&D relevance

**Indirect — supply chain.** Same structural exposure as the parent Mini Shai-Hulud campaign — npm ecosystem compromise reaches DIB CI/CD pipelines that pull from public registries. The wave **operationalizes** the supply-chain risk the worm source-code release predicted.

## Source citations

- BleepingComputer / Bill Toulas (2026-05-18 13:28 EDT): https://www.bleepingcomputer.com/news/security/leaked-shai-hulud-malware-fuels-new-npm-infostealer-campaign/
- Ox Security (primary source — BleepingComputer relay)
- 2026-05-18 afternoon brief (Archimedes capture + ACH analysis)

## Related Archimedes records

- **Actor:** UNATTRIBUTED — no roster entry
- **Briefs:** see frontmatter `related_briefs:`
- **Linked campaign:** [Mini Shai-Hulud / TanStack](../mini-shai-hulud/profile.md) — parent campaign; clones are **distinct actor**, same exposure surface
- **Related finding (referenced in brief):** VT-006 (Mini Shai-Hulud worm + derivative-30d WEP framing)
- **IOCs to push to defense:**
  - 4 package names (above) → dependency quarantine
  - C2 `87e0bbc636999[.]lhr[.]life` → block / detect

## Operator notes

Next-30-day watch: additional copy-cat clones very likely to surface. Each is **distinct from this dossier** unless corroborating source-evidence links them — preserve actor-distinct tracking per analyst ACH. If a future variant becomes attributable (e.g., second-source ties packages to a named operator), spin out a new campaign dossier per actor.
