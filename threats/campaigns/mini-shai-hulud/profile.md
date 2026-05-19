---
campaign_id: mini-shai-hulud
aliases: [Mini Shai-Hulud, TanStack supply-chain, Shai-Hulud worm]
status: active
first_observed: 2026-05 (worm wave); precursor activity prior
last_observed: 2026-05-18
attributed_actors:
  - actor_id: "001"
    actor_name: TeamPCP
    threat_level: HIGH
    confidence: high
    attribution_source: "Multi-A-grade vendor convergence (Wiz, Aikido, Snyk supply-chain teams) + operator self-claim activity on BreachForums"
attribution_caveats: null
sectors_targeted: [software-supply-chain, AI-companies, npm-ecosystem, DIB-CI/CD-adjacent]
geographies: [global]
named_victims:
  - OpenAI (2 employee devices confirmed breached)
  - Mistral AI (claimed ~450 repositories, ~5 GB exfil; $25K listing; 2026-05-21 leak deadline)
  - npm registry (worm-propagation victims at scale)
ad_relevance: indirect-supply-chain
ad_relevance_rationale: |
  No A&D-prime named victim. Structural relevance is supply-chain depth — npm
  ecosystem compromise reaches DIB CI/CD pipelines that pull from public registries.
  TeamPCP shift from private operator to campaign-host (worm source public + bounty)
  raises derivative-intrusion volume per analyst KAC.
related_briefs:
  - threats/briefs/2026-05-12-flash-0600-teampcp-mini-shai-hulud.md
  - threats/briefs/2026-05-18-afternoon.md
  - threats/briefs/2026-05-18-morning.md
related_actors_referenced: [TeamPCP]
related_vulnerabilities: []
tracked_since: 2026-05-12
last_reviewed: 2026-05-18
next_review_due: 2026-08-18
dossier_version: 1
tlp: CLEAR
---

# Campaign — Mini Shai-Hulud / TanStack Supply-Chain

## Status

**Active.** Stacked three convergent supply-chain surfaces in 96 hours (per 2026-05-18 morning brief). Worm source code now public on GitHub with a BreachForums bounty for proof-of-intrusion; operator is simultaneously listing a claimed ~450-repository / ~5 GB Mistral AI exfil for $25K with a 2026-05-21 leak deadline.

## Attribution

**TeamPCP** (roster #001, HIGH). Attribution-confidence is **high** based on multi-A-grade vendor convergence (Wiz, Aikido, Snyk on supply-chain compromise indicators) plus operator self-claim activity on BreachForums. Mistral named on VT-006 after OpenAI is the second enterprise victim, confirming actor consistency across both surfaces.

Per Hard Rule 2, Archimedes does **not** originate the attribution — it restates the vendor consensus.

## Mechanism

- **npm package compromise** + **self-replicating worm propagation** across the ecosystem
- **TanStack** is a tracked secondary surface (separate from the worm wave)
- Worm source code release shifts the campaign from a private-operator pattern to a **campaign-host** pattern — TeamPCP now provides infrastructure for derivative actors

## Named victims

- **OpenAI** — 2 employee devices confirmed breached in the Mini Shai-Hulud / TanStack vector
- **Mistral AI** — claimed ~450 repos, ~5 GB exfil; $25K listing on BreachForums; **2026-05-21 leak deadline (T-3 at last review)**
- **npm ecosystem at large** — worm-propagation victims; specific package count tracked via VT-006

## A&D relevance

**Indirect — supply chain.** No A&D-prime named victim to date. Structural concern: TeamPCP-shape worm propagation in npm reaches into DIB CI/CD pipelines that pull from public registries. Per analyst KAC, derivative-intrusion volume is **very likely** to rise over the next 30 days from the worm source-code release.

## Source citations

- FLASH brief 2026-05-12 06:00 (TeamPCP / Mini Shai-Hulud)
- 2026-05-18 morning + afternoon briefs (most recent campaign-state reporting)
- Wiz, Aikido, Snyk supply-chain coverage (vendor advisories, multi-A-grade)
- BreachForums operator-claim activity (operator self-disclosure; not load-bearing for attribution but consistent with vendor consensus)

## Related Archimedes records

- **Actor:** [TeamPCP roster entry](../../threat-actors/_roster.yaml) — actor #001, HIGH
- **Findings:** VT-006 (Mistral / OpenAI exfil tracking — referenced in briefs)
- **Briefs:** see frontmatter `related_briefs:`
- **Linked campaign:** [Shai-Hulud clone wave (npm)](../shai-hulud-clone-wave-202605/profile.md) — distinct, UNATTRIBUTED actor; not TeamPCP

## Operator notes

TeamPCP leak deadline 2026-05-21 (T-3 at last review) is the next actor tripwire. Next /update-tracking pass on TeamPCP should fold in this campaign's escalation pattern.
