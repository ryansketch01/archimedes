---
raw_id: raw-2026-06-02-am-003-securityweek-supply-chain-red-hat-npm-32-packages-miasma-mini-shai-hulud-vt006-family-extension
collected_at: 2026-06-02T07:36:00-04:00
run_id: pre-brief-20260602-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (Ionut Arghire byline) - consolidates ReversingLabs + Aikido + Ox Security + Socket independent vendor research on Red Hat npm supply-chain attack
  source_url: https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/
  published_at: 2026-06-02T05:51:19-04:00
source_grade: B (SecurityWeek relay; consolidates four independent vendor research surfaces — ReversingLabs C, Aikido C, Ox Security B, Socket B per source-grades.yaml)
date: 2026-06-02
topic: red-hat-npm-32-package-supply-chain-attack-miasma-mini-shai-hulud-variant-vt006-family-extension
match_reason:
  watchlist: []
  actors: ["001"]  # TeamPCP (per VT-006 family attribution, carried forward; SecurityWeek
                   # confirms TeamPCP attribution as restatement, not new origination)
  vulnerabilities: [VT-006]  # Mini Shai-Hulud npm + PyPI self-propagating worm family,
                             # CVE-2026-45321
  keywords: [Mini Shai-Hulud, Miasma, Shai-Hulud, Red Hat, npm, supply chain, TeamPCP, ReversingLabs, Aikido, Ox Security, Socket, GitHub Actions OIDC, CI/CD compromise]
triage_tags: [vt006_family_extension, supply_chain_attack, npm_ecosystem, multi_vendor_corroboration, anti_noise_partial, non_flash]
candidate_triggers:
  - trigger_id: 2
    name: tracked-actor-attribution
    evaluation: FAIL (attribution_is_not_new — restatement of existing VT-006 / finding-2026-05-12-FLASH-0001 TeamPCP attribution)
    rationale: >
      VT-006 Mini Shai-Hulud family is already corpus-resident with
      TeamPCP attribution at "likely" WEP per `finding-2026-05-12-FLASH-0001`
      (Wiz + Snyk + StepSecurity origination). SecurityWeek's 2026-06-02
      restatement of TeamPCP attribution on the Red Hat npm extension
      does NOT constitute a "new attribution to a tracked actor" under
      FLASH Trigger 2's `attribution_is_new_not_restatement` condition.
      Restated attribution on a new victim cohort (Red Hat
      @redhat-cloud-services scope) is a campaign-progression
      observation, not a new attribution event. Trigger 2 FAILS.
  - trigger_id: 5
    name: ad-sector-campaign
    evaluation: FAIL (no_ad_prime_named)
    rationale: >
      Red Hat is the named victim — Red Hat is NOT an A&D-prime watchlist
      entity. Red Hat is a commercial open-source vendor (IBM-owned)
      providing enterprise Linux distribution and developer tooling. The
      32 @redhat-cloud-services npm packages compromised are part of Red
      Hat's Hybrid Cloud Console JavaScript ecosystem, with broad
      enterprise consumer footprint (~10 million collective downloads).
      A&D-prime downstream-dependency exposure via the @redhat-cloud-
      services scope is possible (any A&D prime running Red Hat Hybrid
      Cloud Console or pulling those packages transitively into their
      SDLC), but no A&D-prime is NAMED as a downstream victim in
      SecurityWeek's coverage. Trigger 5 requires named-A&D-target;
      restated transitive-dependency exposure does not satisfy.
iocs_extracted: true
iocs_count: 4
text_word_count: 1480
promoted: true
promoted_to_finding: finding-2026-06-02-0003-securityweek-reversinglabs-aikido-ox-socket-miasma-red-hat-npm-32-package-vt006-extension-multi-firm-corroboration-oidc-cicd-vector
promoted_at: 2026-06-02T08:22:00-04:00
promotion_run_id: morning-20260602-080000
ttl_expires_at: 2026-08-31T07:36:00-04:00
test: false
---

# Supply Chain Attack Hits 32 Red Hat NPM Packages

## Source

SecurityWeek (Ionut Arghire byline), 2026-06-02T09:51:19 GMT =
05:51 EDT (in 14h pre-brief window). URL:
https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/

SecurityWeek consolidates four independent vendor research surfaces:

| Vendor | Grade | Coverage |
|---|---|---|
| ReversingLabs | C (first surface in Archimedes corpus — would be provisional-C on first-citation per LayerX / Seqrite / Trendyol precedent) | 72-second publication window + CI/CD compromise analysis |
| Aikido | C (provisional, source-grades.yaml line 274) | GitHub Actions OIDC exploitation assessment |
| Ox Security | B (provisional, source-grades.yaml line 466) | 210 infected repositories with stolen credentials enumeration |
| Socket | B (provisional, source-grades.yaml line 442) | Malware capability detailed analysis |

This is **four independent vendor research surfaces consolidated through
a B-grade relay** — a stronger evidentiary position than VT-006's
original 2026-05-12 FLASH disclosure which carried fewer corroborating
vendor sources.

## Body

A supply-chain attack hit **32 Red Hat npm packages** in the
**@redhat-cloud-services scope**, with **96 malicious package versions
published** before Red Hat detected and unpublished. The compromise
covers **"the entire Red Hat Hybrid Cloud Console JavaScript
ecosystem"** with ~10 million collective downloads. SecurityWeek
notes that downstream consumers should "check transitive dependencies,
as the packages are widely used as indirect libraries" — broad
ecosystem-reach.

## Attribution

**TeamPCP is identified as the threat group behind this campaign**
(SecurityWeek, restating attribution from the four vendor research
sources). The malware payload carried the string **"Miasma: The
Spreading Blight"** — researcher-coined working name for this
specific variant of the Mini Shai-Hulud worm.

This **restates** TeamPCP attribution previously established on
VT-006 / `finding-2026-05-12-FLASH-0001` (Wiz + Snyk + StepSecurity
origination at "high confidence" / "likely" WEP). Per Hard Rule 2,
Archimedes does not originate attribution; the restatement of TeamPCP
here is sourced via ReversingLabs / Aikido / Ox Security / Socket
through SecurityWeek's relay, not originated by Archimedes.

## Mechanism (technical class)

- **Publication window**: 72 seconds between earliest and latest
  malicious-version publication (ReversingLabs analysis) — indicative
  of automated push via compromised CI/CD pipeline rather than
  interactive attacker session.
- **CI/CD compromise vector**: GitHub Actions OIDC exploitation
  (Aikido assessment) — the GitHub Actions OIDC token-issuance flow
  was leveraged to obtain npm publish credentials from federated
  identity rather than from static maintainer-account compromise.
- **Downstream blast radius**: ~210 infected repositories with stolen
  credentials (Ox Security enumeration) — the worm propagated from
  the initial @redhat-cloud-services maintainer compromise into 210
  downstream consumer-repos that pulled and ran the malicious
  versions.
- **Mini Shai-Hulud variant capabilities** (Socket analysis,
  consolidated by SecurityWeek):
  - Credential-stealing worm class
  - Exfiltration to attacker-controlled server (specific endpoint
    NOT published in SecurityWeek coverage)
  - GitHub-based fallback C2 mechanism (specific endpoint NOT
    published in SecurityWeek coverage)
  - "Miasma: The Spreading Blight" payload-embedded researcher-coined
    name string

Hard Rule 3 compliance: SecurityWeek's coverage does not include PoC
code, exploit walkthroughs, or attack-step detail beyond the mechanism
class described above. Nothing exploit-enabling is preserved here.

## VT-006 family lineage (corpus-resident context)

This is the **second cross-vendor multi-firm corroboration** of the
Mini Shai-Hulud family within 21 days:

- 2026-05-12 FLASH: original Mini Shai-Hulud disclosure (TanStack +
  @uipath + @mistralai + @opensearch-project + @squawk aviation + ~172
  packages total compromised; `finding-2026-05-12-FLASH-0001`; VT-006)
- 2026-05-27: CISA KEV listing of CVE-2026-45321 (catalog version
  2026.05.27; `finding-2026-05-27-0007`; VT-006 state transition to
  KEV-listed; federal deadline 2026-06-10)
- 2026-06-01: Red Hat @redhat-cloud-services npm 32-package
  compromise originally surfaced (`finding-2026-06-01-0004` —
  Socket + The Hacker News primary)
- 2026-06-02 (this raw-signal): SecurityWeek consolidates
  ReversingLabs + Aikido + Ox Security + Socket research, naming
  the Red Hat-scope compromise as a Mini Shai-Hulud / "Miasma" variant
  with TeamPCP attribution

The 2026-06-02 SecurityWeek surface ADDS to `finding-2026-06-01-0004`
the following new material:

1. **"Miasma: The Spreading Blight" payload-string name** (researcher-
   coined working name for this specific variant, distinct from "Mini
   Shai-Hulud" parent family name)
2. **72-second automated publication-window observation** (ReversingLabs)
3. **GitHub Actions OIDC exploitation as the CI/CD compromise vector**
   (Aikido)
4. **210 downstream infected repositories** (Ox Security)
5. **Four-firm independent consolidated coverage** (vs. finding 0004's
   Socket + THN single-vendor + relay)

This material is **substantively new** and warrants grader's promotion-
or-supersede decision on `finding-2026-06-01-0004`. The grader may
elect to:

- **Supersede** finding 0004 with a richer 2026-06-02 finding folding
  in the new material; OR
- **Update** finding 0004 in-place with the new vendor research and
  the "Miasma" variant name; OR
- **Defer** if AM-1 brief space is constrained (the campaign-progression
  signal alone is not FLASH-trigger-class).

## A&D-relevance assessment (grader-input)

**No A&D-prime named as downstream victim**.

**Indirect transitive-dependency exposure vector**: any A&D prime
running Red Hat Hybrid Cloud Console (cloud management UI) or pulling
the @redhat-cloud-services npm scope transitively into SDLC pipelines
inherits potential exposure. Red Hat Hybrid Cloud Console is the
SaaS-control-plane for Red Hat OpenShift / RHEL subscription
management — A&D primes running OpenShift in cleared / classified
environments may or may not be exposed depending on tenancy posture
(air-gapped vs. SaaS-connected).

VT-006 carry-forward `ad_relevance: medium_indirect_via_squawk_aviation_
ecosystem` from `_index.yaml` line 192 also applies: the Mini Shai-
Hulud worm's mechanism is maintainer-enumeration-driven, not sector-
targeted. @squawk aviation-namespace and @redhat-cloud-services Red
Hat-namespace compromises are both products of the same propagation
mechanism, not products of A&D-sector targeting.

## Anti-noise check

**Partial anti-noise**: VT-006 family covered by `finding-2026-06-01-0004`
(yesterday's PM brief); but this 06-02 SecurityWeek surface adds
substantively new material (Miasma variant name, 72-second publication
window, GitHub Actions OIDC vector, 210 downstream repos, four-firm
corroboration) not in finding 0004. Anti-noise applies to the campaign
identity but NOT to the new material. Grader call on supersede vs.
update.

UNC1549 / Screening Serpens 2026-tradecraft anti-noise lock: not
applicable to this item.

## IOCs (from ioc-extraction skill)

```yaml
indicators:
  - type: cve
    value: CVE-2026-45321
    confidence: high
    context: >
      VT-006 family parent CVE. Mini Shai-Hulud npm + PyPI self-
      propagating worm. KEV-listed 2026-05-27 with 2026-06-10 federal
      deadline. The 2026-06-02 Red Hat @redhat-cloud-services 32-package
      compromise is a downstream extension of this CVE's mechanism
      class.
    sources:
      - https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/

  - type: malware_family
    value: "Mini Shai-Hulud"
    variant_name: "Miasma" / "Miasma: The Spreading Blight"
    confidence: high
    context: >
      "Miasma: The Spreading Blight" is the researcher-coined name for
      this specific variant of the Mini Shai-Hulud worm, identified
      via payload-embedded string. Distinct from parent family name
      "Mini Shai-Hulud" used in VT-006 dossier. Variant compromised
      the @redhat-cloud-services npm scope at 32 packages / 96 versions
      / ~10 million collective downloads.
    sources:
      - https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/

  - type: package_scope
    value: "@redhat-cloud-services (npm)"
    affected_count: "32 packages, 96 malicious versions"
    confidence: high
    context: >
      Red Hat Hybrid Cloud Console JavaScript ecosystem entire scope.
      ~10 million collective downloads. Red Hat detected and
      unpublished. Downstream transitive-dependency exposure for any
      consumer pulling the scope.
    sources:
      - https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/

  - type: ttp_observation
    value: "72-second automated publication window across 96 malicious versions"
    confidence: high
    context: >
      ReversingLabs analysis indicates automated publication via
      compromised CI/CD pipeline (not interactive attacker session).
    sources:
      - https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/

attribution_claims:
  - claim: >
      TeamPCP is the threat group behind the Red Hat npm
      @redhat-cloud-services 32-package supply-chain compromise; the
      Mini Shai-Hulud variant carrying the "Miasma: The Spreading
      Blight" payload string.
    asserted_by: >
      SecurityWeek (Ionut Arghire byline) consolidating ReversingLabs +
      Aikido + Ox Security + Socket independent vendor research
    asserted_via: trade-press consolidation of four vendor surfaces
    confidence_language: descriptive (TeamPCP "identified ... behind
      this campaign")
    actor_named: TeamPCP (corpus actor id 001)
    family_lineage: Mini Shai-Hulud (VT-006), via Shai-Hulud family
    novelty_layer: "Miasma" variant name first surface in corpus on
      2026-06-02
    archimedes_compliance_note: >
      This is a RESTATEMENT of pre-existing TeamPCP attribution on the
      VT-006 family (Wiz + Snyk + StepSecurity origination 2026-05-12).
      Archimedes does not originate attribution; this raw-signal
      records the restatement and the family-extension event, not a
      new attribution. Hard Rule 2 compliant.
```

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire (SecurityWeek)
- Article type: vendor-research-consolidation relay (B-grade relay over
  four vendor primaries: ReversingLabs C / Aikido C / Ox Security B /
  Socket B)
- Raw IOC extraction invoked: yes (4 indicators: CVE-2026-45321
  family carry-forward, "Miasma" variant name, @redhat-cloud-services
  package scope, 72-second TTP observation)
- Hard Rule 2 compliance: TeamPCP attribution is RESTATEMENT not
  origination; preserved as "Miasma variant of Mini Shai-Hulud
  attributed to TeamPCP" rather than "Archimedes attributes Red Hat
  npm compromise to TeamPCP"
- Hard Rule 3 compliance: no exploit code, no PoC, no GitHub-Actions-
  OIDC walkthrough preserved — mechanism class described, attack-
  enabling detail intentionally omitted
- Hard Rule 6 compliance: zero verbatim source quotes used (paraphrased
  throughout)
- Hard Rule 8 compliance: Splunk first-party check ran during sentinel
  sweep (`splunk-archimedes` + `splunk-defenseclaw` 24h, zero non-self-
  telemetry events, no IOC hits)
- Grader handoff: this item is a **VT-006 family extension** and a
  **promotion-or-supersede decision** on `finding-2026-06-01-0004`.
  Recommended grader options:
  1. SUPERSEDE finding 0004 with a richer 2026-06-02 finding folding
     in the new material (Miasma variant, 72s window, OIDC vector,
     210 downstream repos, four-firm corroboration), OR
  2. UPDATE finding 0004 in-place with the new material via a
     "campaign-progression amendment" pattern, OR
  3. CREATE a stand-alone 2026-06-02 finding cross-referencing 0004
     as the original surface.
  The four-firm independent corroboration STRENGTHENS the WEP layer
  on Mini Shai-Hulud attribution from "likely" to potentially "very
  likely" on the procedural facts; the attribution-to-TeamPCP layer
  remains at "likely" (StepSecurity originating attribution +
  ReversingLabs/Aikido/Ox/Socket restating without independent
  attribution origination on Red Hat-scope specifically).
