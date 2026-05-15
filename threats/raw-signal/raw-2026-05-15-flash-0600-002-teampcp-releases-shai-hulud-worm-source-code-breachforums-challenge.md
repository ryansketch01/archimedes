---
raw_id: raw-2026-05-15-flash-0600-002
collected_at: 2026-05-15T06:15:00-04:00
run_id: flash-sweep-20260515-060000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-15T06:00:00-04:00
time_window_start: 2026-05-15T00:00:00-04:00
time_window_end: 2026-05-15T06:00:00-04:00
test: false
flash_candidate: true
quiet_hours_active: true                   # 06:00 EDT outside 09:00-21:00 EDT active window — FLASH must queue per FLASH-POLICY
trigger_id:
  - tracked-actor-ttp-change               # Trigger 4 — primary (new tooling/distribution channel for tracked actor #001)
  - tracked-actor-attribution              # Trigger 2 — secondary (new attribution surface naming TeamPCP for source-code release act; not a re-statement of prior worm-deployment attribution)
trigger_detail: >
  TeamPCP (tracked actor #001, threat_level HIGH) has released the
  Shai-Hulud npm/PyPI worm's source code on GitHub repositories
  (subsequently removed by GitHub; multiple forks reported persisting)
  alongside a BreachForums announcement framing a "supply chain
  challenge" — explicit operator solicitation of additional supply-
  chain compromises with monetary rewards tied to proof of intrusion
  and downstream impact maximization. Per SecurityWeek primary (Ionut
  Arghire byline, published 2026-05-15T05:47 EDT). Trigger 4 fits:
  new distribution channel (open-source worm release + cybercriminal-
  forum bounty model) is a meaningful TTP departure from prior
  TeamPCP operational pattern (private deployment of Mini Shai-Hulud
  worm against npm + PyPI per Wiz / Snyk / StepSecurity attribution
  in the 2026-05-12 FLASH). Trigger 2 fires on the new-attribution
  dimension: the source-code-release act itself is a new attribution
  surface — TeamPCP is named as the releasing entity, not just the
  prior worm-deployer.

  Sources for the attribution: SecurityWeek primary; Datadog
  (technical malware framework analysis cited); Ox Security (attack
  variant observations cited); Black Duck (Ben Ronallo commentary
  cited); Pathlock (Jonathan Stross remediation guidance cited). Per
  SecurityWeek attribution language: TeamPCP is "infamous" and has
  "targeted the open source software ecosystem multiple times over
  the past six months" — consistent with prior corpus framing of
  TeamPCP via VT-006 (Mini Shai-Hulud), finding-2026-05-04-0003
  (PyTorch Lightning ShaiWorm family lineage), and 2026-05-14 22:00
  EDT FLASH (TeamPCP Mistral AI 450 repos sale).
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (originating relay; Ionut Arghire byline)
  source_url: https://www.securityweek.com/teampcp-ups-the-game-releases-shai-hulud-worms-source-code/
  published_at: 2026-05-15T05:47:09-04:00
  author: Ionut Arghire
  primary_research_sources:
    - id: securityweek
      url: https://www.securityweek.com/teampcp-ups-the-game-releases-shai-hulud-worms-source-code/
      grade: B
      grade_rationale: |
        SecurityWeek is provisional B per source-grades.yaml (awaiting
        ratification; first cited 2026-05-06). Originating relay on
        this surface — synthesizes Datadog + Ox Security + Black Duck
        + Pathlock vendor commentary into a single article. None of
        the cited downstream-analysis vendors appears to have
        published a standalone primary at sweep time; Datadog and Ox
        Security are likely the originating technical primaries but
        their direct publications were not retrievable this sweep.
      published_at: 2026-05-15
      author: Ionut Arghire
    - id: datadog
      url: not_retrieved_this_sweep
      grade_proposal: provisional_B
      grade_rationale: |
        Datadog Security Labs is a cloud-security vendor research
        practice; first surface in Archimedes corpus. Per SecurityWeek
        citation: "Datadog ... detailed malware framework analysis."
        Provisional B is the conservative starting grade for first-
        surface vendor-research firms per the established precedent
        (StepSecurity 2026-05-12, Sysdig 2026-05-14, Zellic
        2026-05-14, Socket 2026-05-14). Operator may upgrade to A on
        subsequent surfaces showing peer-reviewed APT/supply-chain
        research rigor.
      published_at: 2026-05-15
      author: unknown_per_relay
    - id: ox-security
      url: not_retrieved_this_sweep
      grade_proposal: provisional_C
      grade_rationale: |
        Ox Security is an application-security vendor research
        practice; first surface in Archimedes corpus. Per
        SecurityWeek citation: "Ox Security ... attack variant
        observations." Provisional C is the conservative starting
        grade for first-surface vendor-research firms without prior
        corpus track record (per LayerX / Seqrite / Trendyol-Albayrak
        / Aikido / SafeDep precedent). Operator may upgrade to B on
        subsequent surfaces showing consistent technical rigor.
      published_at: 2026-05-15
      author: unknown_per_relay
  social_sources:
    - id: x-dailydarkweb
      url: not_retrieved_this_sweep
      grade_proposal: provisional_C
      grade_rationale: |
        @DailyDarkWeb is an X/Twitter dark-web-monitoring account;
        first surface in Archimedes corpus. Per SecurityWeek
        citation: "@DailyDarkWeb ... stumbled upon the BreachForums
        announcement." Social-tier account, no Tier-1 vendor research
        affiliation per relay framing. Provisional C is the
        conservative starting grade per the established X-source
        grading convention (x-vxunderground C, x-falconfeedsio C).
      published_at: 2026-05-15
      author: "@DailyDarkWeb"
match_reason:
  watchlist: []                            # No A&D-prime named-victim or named-supply-chain-target in source content this sweep. A&D-relevance is indirect via the worm's @squawk aviation-namespace and @tanstack downstream dependency chains already tracked under VT-006.
  actors:
    - "TeamPCP"                            # Tracked actor #001 in _roster.yaml; primary_name match. Threat_level HIGH.
  vulnerabilities:
    - CVE-2026-45321                       # Mini Shai-Hulud worm CVE; tracked under VT-006 in _index.yaml. Source-code release is operationally adjacent — released code IS the Shai-Hulud worm itself per SecurityWeek framing (not a different worm), making this an evolution of the VT-006 surface rather than a new CVE entry.
  keywords:
    - "TeamPCP"
    - "Shai-Hulud"
    - "supply chain challenge"
    - "BreachForums"
    - "monetary rewards"
    - "source code release"
triage_tags:
  - flash_candidate
  - tracked-actor-ttp-change
  - tracked-actor-attribution
  - supply-chain-attack
  - npm-ecosystem
  - pypi-ecosystem
  - source-code-release
  - cybercriminal-bounty-program
  - operational-expansion
  - vt-006-evolution
  - ad-sector-indirect-via-squawk-tanstack-dependency-graphs
iocs_extracted: true
iocs_count: 0                              # No new technical IOCs (domains/IPs/hashes/repos) published by SecurityWeek primary; GitHub repo URLs were removed by GitHub prior to article publication and were not listed
text_word_count: 850
promoted: true
promoted_to_finding: finding-2026-05-15-FLASH-0002
promoted_at: 2026-05-15T06:35:00-04:00
promoted_grading_run_id: flash-grade-20260515-060000
ttl_expires_at: 2026-08-13T06:15:00-04:00
---

# TeamPCP Releases Shai-Hulud npm/PyPI Worm Source Code on GitHub + BreachForums "Supply Chain Challenge" With Monetary Rewards

## Summary

SecurityWeek (Ionut Arghire byline, published 2026-05-15 05:47 EDT) reports that TeamPCP — the tracked threat actor (#001, HIGH) attributed by Wiz + Snyk + StepSecurity to the 2026-05-12 Mini Shai-Hulud npm + PyPI worm campaign (Archimedes-tracked VT-006, CVE-2026-45321) — has released the worm's source code via GitHub repositories under multiple user accounts. GitHub removed the original repositories; multiple forks have appeared.

TeamPCP simultaneously posted to BreachForums announcing a "supply chain challenge," explicitly soliciting other cybercriminals to deploy Shai-Hulud in attacks, provide proof of intrusion, and maximize downstream impact in exchange for monetary rewards.

Datadog and Ox Security are credited with technical follow-on analysis; Black Duck (Ben Ronallo) and Pathlock (Jonathan Stross) are quoted on commentary and remediation. The discovery of the BreachForums announcement is credited to X/Twitter user @DailyDarkWeb.

No specific GitHub repository URLs, IOC hashes, or new technical indicators are listed in the SecurityWeek primary this sweep.

## Why this is a FLASH candidate

**Primary trigger — Trigger 4 (tracked actor TTP change):** TeamPCP's prior operational pattern (per VT-006 corpus state + 2026-05-12 FLASH attribution) is private deployment of the Mini Shai-Hulud worm against npm + PyPI maintainer accounts via SLSA-attestation-breaking OIDC token hijack. The new behavior — open-source release of the worm's source code on GitHub PLUS a BreachForums-fronted cybercriminal-bounty challenge — is a meaningful TTP departure across three dimensions:

1. **Distribution model:** From private/operator-controlled deployment to commodity-style open-source release. Shifts TeamPCP from a single-operator to a campaign-host role.
2. **Force multiplication:** Bounty mechanism explicitly solicits third-party use of the worm code. Future Shai-Hulud-attributed intrusions may not be TeamPCP itself but copycats motivated by the BreachForums challenge.
3. **Attribution complexity:** Future Shai-Hulud-derivative intrusions become attribution-ambiguous between TeamPCP and the broader BreachForums cybercriminal pool. The 2026-05-12 VT-006 attribution chain (Wiz/Snyk/StepSecurity → TeamPCP) does not automatically extend to derivative campaigns.

**Secondary trigger — Trigger 2 (tracked actor attribution):** The source-code release act itself is a new attribution surface. SecurityWeek + Datadog + Ox Security name TeamPCP as the releasing entity, not as the prior worm-deployer. This is a new TeamPCP-attributed event, not a re-statement of the 2026-05-12 attribution.

## VT-006 / CVE-2026-45321 evolution context

This event is operationally adjacent to the existing VT-006 tracked surface and the 2026-05-12 FLASH brief:

- The released source code IS the Shai-Hulud worm itself per SecurityWeek framing — not a different worm.
- This evolves the VT-006 entry from "active in-the-wild self-propagating worm" (current `exploitation_status`) to "active in-the-wild self-propagating worm + publicly-released source code commoditizing the attack class."
- Recommended vuln-tracker update: extend VT-006 `note` and `watch_signals` to include the source-code-release + BreachForums-bounty pivot. Add `derivative_attacks_expected: true` and a new IOC-class tracking for GitHub fork repositories as they are surfaced and taken down.

## A&D-prime relevance

**Indirect / structural — same disposition as VT-006 baseline.** The worm's @squawk aviation-namespace (19 packages, including @squawk/flightplan, @squawk/weather, @squawk/mcp) and @tanstack ecosystem footprint already establish indirect A&D-prime exposure via SDLC dependency graphs. The commoditization of the worm raises the floor on derivative-attack volume — increasing the probability that a Tier-1 prime's SDLC will be hit by a Shai-Hulud-derivative within the 30-day forward window — but does NOT introduce new A&D-direct targeting. A&D-prime customer-impact statements have not surfaced this sweep.

The OpenAI TanStack-breach self-disclosure (2026-05-14 afternoon brief, finding-2026-05-14-0008) is the corpus's only named-enterprise-victim on VT-006 to date; the source-code release dramatically increases the probability of additional named-victim disclosures in the next 30 days.

## Anti-noise dedup check

- 2026-05-12 FLASH (`flash-2026-05-12-0600`) covered the original Mini Shai-Hulud worm deployment attribution to TeamPCP. **Distinct topic.** Today's surface is the source-code release + bounty model — a TTP evolution event, not a re-statement.
- 2026-05-14 22:00 EDT FLASH covered TeamPCP Mistral AI 450 repos sale (`raw-2026-05-14-flash-2200-001`). **Distinct topic.** That FLASH is a separate TeamPCP commercialization vector (selling repo access on a separate channel); today's is open-source release + bounty.
- Per FLASH-POLICY anti-noise rule "One FLASH per trigger topic per 24 hours": no prior FLASH in last 24h covers the source-code-release-with-bounty topic. **Eligible to fire.**

## Quiet-hours posture

06:00 EDT sweep falls outside the 09:00–21:00 EDT active window per FLASH-POLICY. Critical override does NOT apply — no CVSS 10.0 component, and although TeamPCP is a tracked actor, no A&D watchlist entity is named as a direct target. Default behavior: queue this FLASH to `infrastructure/flash-queue.yaml` for the 09:00 catchup sweep, where it will be evaluated for supersession by the 08:00 morning brief. If the 08:00 brief covers the TeamPCP source-code release, this queued FLASH is marked superseded and archived.

---

## Extraction notes

- Language: en
- Article type: vendor / security-media primary on cybercriminal-actor operational shift, synthesizing multiple downstream-analysis vendor commentary
- Cross-corroboration at sweep time: SecurityWeek primary + Datadog (cited, not directly retrieved) + Ox Security (cited, not directly retrieved) + Black Duck (commentary) + Pathlock (commentary). The grader should attempt direct retrieval of Datadog and Ox Security primaries on next pass before promotion.
- No verbatim BreachForums post content retrieved or stored this sweep (passive OSINT discipline; LEGAL-POLICY data-handling).
- No GitHub repository URLs published by SecurityWeek primary; GitHub had removed the originals prior to article publication.
- @DailyDarkWeb attribution chain: X/Twitter monitor account → SecurityWeek pickup. Not corroborated by independent A/B-grade source at sweep time. Single-source-veto consideration likely at grader stage if no A-grade vendor publishes a direct primary.

## IOCs (from ioc-extraction skill)

```yaml
iocs: []   # No technical IOCs (domains, IPs, hashes, repo URLs, accounts) published by SecurityWeek primary this sweep. Operational details only.

attribution_claims:
  - source: securityweek
    actor_named: TeamPCP
    confidence_language_verbatim: "infamous hacking group that has targeted the open source software ecosystem multiple times over the past six months"
    new_or_restatement: new_attribution_surface_for_source_code_release_act
    notes: |
      The TeamPCP attribution as releasing-entity for the Shai-Hulud
      source code is consistent with prior VT-006 attribution
      (Wiz + Snyk + StepSecurity, 2026-05-12) but represents a
      separate attribution surface — the act of releasing the source
      code on GitHub + BreachForums is distinct from the prior act
      of deploying the worm against npm/PyPI maintainers.
      Single-source veto consideration applies at grader stage:
      SecurityWeek is the originating relay; Datadog and Ox Security
      are cited but their direct publications were not retrieved
      this sweep.

  - source: securityweek_citing_datadog
    actor_named: TeamPCP
    confidence_language_verbatim: not_directly_retrieved_via_securityweek_only
    new_or_restatement: technical_framework_analysis_supports_attribution
    notes: "Per SecurityWeek: Datadog published detailed malware framework analysis. Direct retrieval pending next pass."

  - source: securityweek_citing_ox_security
    actor_named: TeamPCP
    confidence_language_verbatim: not_directly_retrieved_via_securityweek_only
    new_or_restatement: attack_variant_observations
    notes: "Per SecurityWeek: Ox Security observed attack variants. Direct retrieval pending next pass."
```
