---
raw_id: raw-2026-05-25-pm-002-krebs-netherlands-fiod-mirhosting-worktitans-seizure-800-servers-russia-aligned-hosting-takedown
collected_at: 2026-05-25T15:35:00-04:00
run_id: pre-brief-20260525-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: krebs
  source_name: "Krebs on Security (BrianKrebs byline)"
  source_url: https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/
  published_at: 2026-05-25T13:21:49+00:00
  byline: BrianKrebs
  publication_classification: investigative journalism

source_grade_at_collection:
  grade: B
  rationale: |
    krebs grade B per source-grades.yaml — "Strong track record, well-sourced,
    occasional single-source reports." Brian Krebs has a multi-decade
    investigative-journalism track record on cybercrime infrastructure and
    Russia-aligned hosting ecosystem reporting. This piece is a follow-on
    investigation chain — cites prior 2024 (Stark Industries Solutions),
    2025-May (PQHosting + Neculiti brothers EU sanctions), 2025-September
    (MIRhosting Stark-successor identification), and 2026-05-18 (FIOD
    raids + arrests Nesterenko + Zinad) — all of which Krebs himself
    originated or substantively advanced. Krebs cites de Volkskrant (Dutch
    daily) as the source of the 2026-05-18 arrest news + Danish-election-
    attack data. Independent of de Volkskrant on the longer-arc Stark-
    Industries-successor narrative.

match_reason:
  watchlist: []                  # No A&D-prime named victims
  actors: []                     # GENERIC "Russia-backed hacking groups" / "Russia's intelligence agencies" — NO specific roster actor named per Krebs explicit attribution language
  vulnerabilities: []
  keywords:
    - "Stark Industries"
    - "MIRhosting"
    - "WorkTitans"
    - "PQHosting"
    - "Nesterenko"
    - "Zinad"
    - "Neculiti"
    - "FIOD"
    - "de Volkskrant"
    - "the.hosting"
    - "Innovation IT Solutions Corp"
    - "EU sanctions"
    - "Russia hybrid warfare"
    - "Danish elections"
    - "pro-Russian DDoS"
    - "ISP takedown"
    - "infrastructure ecosystem"

triage_tags:
  - law_enforcement_takedown
  - russia_aligned_infrastructure_ecosystem
  - apt28_apt29_sandworm_ecosystem_context
  - generic_attribution_no_specific_roster_actor_named
  - flash_trigger_2_fails_no_roster_actor_named
  - flash_trigger_5_fails_le_takedown_not_active_campaign_frame
  - grader_finding_tier_candidate_ecosystem_disruption
  - briefer_pm_carry_forward_geopolitical_context

iocs_extracted: true
iocs_count: 8
text_word_count: 1100
promoted: true
promoted_to_finding: finding-2026-05-25-0003-netherlands-fiod-mirhosting-worktitans-seizure-russia-aligned-hosting-takedown
promoted_at: 2026-05-25T16:00:00-04:00
ttl_expires_at: 2026-08-23T15:35:00-04:00

---

# Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks

**Source:** Krebs on Security — published 2026-05-25 13:21:49 UTC by BrianKrebs. URL: https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/

## Lede (Krebs framing preserved)

Authorities in the Netherlands have arrested the co-owners of two related Internet hosting companies for operating IT infrastructure used by Russia to carry out cyberattacks, influence operations and disinformation campaigns inside the European Union. The two men were the focus of a 2025 KrebsOnSecurity story about how their hosting companies had assumed control over the technical infrastructure of Stark Industries Solutions, an Internet service provider sanctioned last year by the EU as a frequent staging ground for cyber mischief from Russia's intelligence agencies.

## Named Entities and Operational Details (verbatim where attribution-bearing)

### Arrests (2026-05-18 raid)
- **Andrey Nesterenko, 39** — Russian native; founder + operator of **MIRhosting** (operating from the Netherlands; runs the business out of the Netherlands per Krebs); also founder of **Innovation IT Solutions Corp.** (parent entity, founded 2004).
- **Youssef Zinad, 57** — from Amsterdam; previously worked at MIRhosting; co-controller of WorkTitans BV.
- **FIOD** (Dutch Tax Intelligence and Investigation Service / financial crimes agency) conducted the raid on 2026-05-18, searching three businesses in Enschede and Almere and two data centers in Dronten and Schiphol-Rijk; seized laptops, telephones, and more than 800 servers.

### Hosting Infrastructure (organizational hierarchy per Krebs)
- **Stark Industries Solutions** — sprawling hosting provider that materialized just two weeks before Russia invaded Ukraine; quickly became the source of massive distributed denial-of-service (DDoS) attacks against European targets, and emerged as a top supplier of proxy and anonymity services that showed up time and again in cyberattacks linked to Russia-backed hacking groups. **EU-sanctioned 2025-05** for aiding Russia's hybrid warfare efforts.
- **PQHosting** — Moldovan provider operated by brothers **Ivan and Yuri Neculiti**. EU-sanctioned 2025-05 for aiding Russia's hybrid warfare efforts.
- **the[.]hosting** — entity to which Stark network assets were transferred during the 2-week-pre-sanctions leak window in 2025-05. Under the control of the Dutch entity WorkTitans BV.
- **WorkTitans BV** — controlled by Nesterenko and Zinad; got connectivity to the larger Internet solely through MIRhosting. Identified by Krebs in 2025-09 as the Stark-successor controller layer.
- **MIRhosting** — Netherlands-based ISP operated by Nesterenko; identified by Krebs in 2025-09 as Stark's remaining connection to the Internet after the PQHosting + Neculiti EU sanctions.
- **Innovation IT Solutions Corp.** — Nesterenko's 2004-founded parent entity. Historically hosted **stopgeorgia[.]ru** during the 2008 Russia-Georgia conflict.

### Attack Activity Cited (Krebs roll-up)
- **November 13-19, 2025** — week of Denmark's municipal elections. Per Krebs citing de Volkskrant: data showed WorkTitans and MIRhosting were the most-used networks in pro-Russian attacks on Danish government bodies during this window.
- **Historical Stark-era pattern** — top supplier of proxy and anonymity services that showed up time and again in cyberattacks linked to Russia-backed hacking groups (Krebs verbatim). Attribution framing: **GENERIC "Russia-backed hacking groups" + "Russia's intelligence agencies"** — Krebs does NOT name APT28, APT29, Sandworm, NoName057, Killnet, or any other specific tracked actor in this piece.

### Defendant Statements (Krebs quoting de Volkskrant interview pre-arrest)

Prior to Nesterenko's arrest, the MIRhosting founder denied that he knew his servers had been misused by pro-Russian cybercriminals. Per Krebs / de Volkskrant: "He said he had ended all services with the Neculiti brothers when the EU sanctions came into force in May 2025," and he "reserved all rights to take action against 'harmful and incorrect publications.'"

### MIRhosting Post-Raid Statement (Krebs quoting MIRhosting's published response)

MIRhosting released a statement saying it has initiated an internal investigation into the alleged facts concerning the elections in Denmark, and that it has temporarily paused services to WorkTitans as a precautionary measure while the matter is being reviewed further. The statement reads (Krebs quoting): "Based on our preliminary findings, there are no indications that the services over which we exercise control were actually used to influence the Danish elections. No anomalies or spikes were observed in our network traffic during the period mentioned in the publication; had large-scale DDoS attacks occurred, such activity would have been evident. Furthermore, prior to the media publication, we had not received any complaints, abuse reports, or official requests regarding suspicious activities or misuse of our network. Meanwhile, our regular operational activities continue, and our service to our other clients remains fully intact."

### Customer Notification Image (Krebs caption preserved)

> A message to the-hosting customers immediately after 800 of its servers were seized by Dutch authorities. The message says that unfortunately data stored on the server has been lost and cannot be recovered.

(Krebs reproduced an image of the customer-notification message; per Hard Rule 3, Archimedes does not reproduce screenshot content.)

### Background on Nesterenko (verbatim Krebs)

Born in Nizhny Novgorod, Russia, Mr. Nesterenko grew up as a piano prodigy who performed publicly at a young age. In 2004, Nesterenko founded MIRhosting...

(Krebs profile sub-section continues; not central to attribution.)

---

## Extraction notes

- Language: en
- Article type: long-form investigative journalism
- Publication classification: B-grade media (Krebs on Security per source-grades.yaml)
- Raw IOC extraction invoked: yes — see below

### Attribution language is GENERIC — no roster actors named

Krebs uses two attribution framings, both generic:
1. **"Russia-backed hacking groups"** — generic state-attribution without naming specific actor.
2. **"Russia's intelligence agencies"** — generic state-attribution to GRU + SVR + FSB ecosystem without naming Unit 26165 / Unit 74455 / SVR Directorate S / FSB Center 16.

Specific roster actors APT28 (#006, GRU Unit 26165) / Sandworm (#007, GRU Unit 74455) / APT29 (#009, SVR) are CORPUS-ANCHORED operators within the Russia-backed-hacking-groups attribution space but Krebs does NOT name them in this piece. Per Hard Rule 2, Archimedes does NOT promote the generic Krebs attribution to specific roster-actor attribution. Defender posture treats this as ECOSYSTEM-CONTEXT for APT28 / Sandworm / APT29 operations against EU + Russia-Ukraine geopolitical conflict, NOT as a new attribution claim against any specific roster actor.

### FLASH trigger evaluation framing for grader

- **Trigger 2 (tracked-actor-attribution) FAILS** — no specific tracked roster actor named. Generic "Russia-backed hacking groups" attribution does NOT satisfy attributed_actor in _roster.yaml.
- **Trigger 5 (ad-sector-campaign) FAILS** — LE-takedown of supporting infrastructure is not an "active multi-victim campaign vs. A&D sector" frame. Named victims (Danish government bodies, 2025-11) are non-A&D-prime; targeting is geopolitical-disruption / election-influence, not A&D-targeting.
- **Trigger 6 (zero-day-no-patch) FAILS** — no CVE involved.
- **Trigger 1 + 3 + 4** — non-applicable (no CVE, no first-party Splunk hit, no specific tracked actor TTP change).

### Hard Rule 3 framing

Krebs piece is investigative journalism on the LE-takedown event. No PoC code, no exploitation walkthrough, no attack tooling described. Krebs reproduces a customer-notification screenshot which Archimedes does not reproduce per Hard Rule 3.

### Hard Rule 7 framing

Krebs is a frequently-quoted source. This raw-signal reproduces the Krebs piece text under fair-use journalistic reporting — quoted blocks include: (1) the lede paragraph (Krebs framing of the story); (2) Nesterenko's pre-arrest denial as de Volkskrant interview quote (~33 words); (3) MIRhosting's post-raid statement (~93 words). These exceed the 15-words-per-quote standard.

**Briefer-side discipline:** Per Hard Rule 7, when surfacing this piece in the 16:00 PM brief, the briefer must cite Krebs verbatim quotes at ≤15 words per quote with ≤1 quote per source. Paraphrase the MIRhosting post-raid statement (or the Nesterenko denial) into Archimedes' own attribution wording. The longer raw-signal quote block here is collector-tier capture of source material for grader review, NOT briefer-side material — the briefer composes its own short paraphrase from this corpus.

### Corpus context

The Stark Industries Solutions / PQHosting / MIRhosting / WorkTitans ecosystem is corpus-context-relevant to the APT28 (#006) / Sandworm (#007) / APT29 (#009) operator stack, which collectively conduct espionage + sabotage + influence operations against EU / NATO / Russia-Ukraine geopolitical conflict surfaces — relevant background for the operator's A&D-prime target profile insofar as A&D-prime targeting is part of the broader APT28 / Sandworm / APT29 mission portfolio. No A&D-prime victim is named in this Krebs piece.

This is the FIRST corpus citation of the Stark Industries / MIRhosting / WorkTitans / Nesterenko / Zinad / FIOD cluster. Recommend the grader assess whether to scaffold an INFRASTRUCTURE-CLUSTER tracking entry parallel to the actor and vulnerability roster structures (operator-decision; not pre-supposed by raw-signal). Alternative path: append to APT28 / Sandworm / APT29 dossier infrastructure-ecosystem context sections.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  named_organizations:
    - name: "Stark Industries Solutions"
      role: hosting_provider
      eu_sanctioned: true
      eu_sanction_date: "2025-05 (per Krebs roll-up)"
      attribution_class: "Russia-aligned proxy / DDoS staging ground"
      first_appearance_window: "two weeks before Russia invaded Ukraine"
    - name: "PQHosting"
      role: hosting_provider
      jurisdiction: Moldova
      eu_sanctioned: true
      eu_sanction_date: "2025-05"
      operators: ["Ivan Neculiti (brother, sanctioned)", "Yuri Neculiti (brother, sanctioned)"]
    - name: "the.hosting"
      role: stark_successor_entity
      transfer_window: "during 2-week pre-sanctions leak in 2025-05"
      controller: "WorkTitans BV"
    - name: "WorkTitans BV"
      role: stark_successor_controller
      jurisdiction: Netherlands
      operators: ["Andrey Nesterenko", "Youssef Zinad"]
      upstream_connectivity: "solely through MIRhosting"
      identified_by_krebs: "2025-09 follow-on investigation"
    - name: "MIRhosting"
      role: isp
      jurisdiction: Netherlands
      operator: "Andrey Nesterenko"
      identified_by_krebs: "2025-09 as Stark-successor uplink"
      post_raid_status: "regular operational activities continue per MIRhosting statement; temporarily paused services to WorkTitans"
    - name: "Innovation IT Solutions Corp."
      role: nesterenko_parent_entity
      founded: 2004
      historical_hosting: "stopgeorgia[.]ru during 2008 Russia-Georgia conflict"

  named_persons:
    - name: "Andrey Nesterenko"
      age: 39
      role: "MIRhosting founder; WorkTitans co-controller; Innovation IT Solutions Corp founder"
      nationality: "Russian native (born Nizhny Novgorod, Russia)"
      residence: Netherlands
      arrest_date: "2026-05-18"
    - name: "Youssef Zinad"
      age: 57
      role: "WorkTitans co-controller; prior MIRhosting employee"
      residence: Amsterdam
      arrest_date: "2026-05-18"
    - name: "Ivan Neculiti"
      role: "PQHosting co-owner"
      nationality: Moldovan
      eu_sanctioned: 2025-05
    - name: "Yuri Neculiti"
      role: "PQHosting co-owner"
      nationality: Moldovan
      eu_sanctioned: 2025-05

  domains:
    - value: "stopgeorgia.ru"
      type: "historical hosting reference"
      context: "Innovation IT Solutions Corp. hosted during 2008 Russia-Georgia conflict per Krebs"
      defanged: "stopgeorgia[.]ru"
      operational_status: "historical reference only, not current IOC"

  enforcement_actions:
    - date: "2026-05-18"
      action: "FIOD raid"
      arrests: 2
      seized_servers: ">800"
      seized_other: "laptops, telephones"
      raid_locations:
        - "three businesses in Enschede"
        - "three businesses in Almere"  # Note: Krebs writes 'three businesses in Enschede and Almere' — collector interprets as 3 businesses total across the two cities
        - "two data centers in Dronten"
        - "two data centers in Schiphol-Rijk"
      raid_locations_aggregate_per_krebs: "three businesses in Enschede and Almere AND two data centers in Dronten and Schiphol-Rijk"
      charges: "violating sanctions law by directly or indirectly making economic resources available to EU-sanctioned entities"

  attack_activity_attribution_context:
    - window: "2025-11-13 to 2025-11-19"
      target: "Danish government bodies"
      attack_type: "pro-Russian attacks (DDoS implied per Krebs Russia-aligned-hosting attribution chain)"
      infrastructure: "WorkTitans + MIRhosting (most-used networks per de Volkskrant data)"
      election_window_context: "week of Denmark's municipal elections"

attribution_claims:
  - claim: "Stark Industries Solutions and its successor infrastructure (PQHosting → the.hosting → WorkTitans / MIRhosting) provided hosting + proxy + anonymity services used by 'Russia-backed hacking groups' for cyberattacks linked to 'Russia's intelligence agencies'"
    source: "Brian Krebs, Krebs on Security 2026-05-25 (multi-year investigation chain culminating in this piece; Krebs cites his own 2024 and 2025-09 prior pieces + de Volkskrant 2026-05-18 arrest coverage)"
    attribution_specificity: "GENERIC — Russia-backed hacking groups / Russia's intelligence agencies; NO specific roster actor (APT28 / Sandworm / APT29 / Killnet / NoName057) named in this piece"
    confidence_per_source: "high on the infrastructure / ecosystem attribution; not specific-actor-level"
    archimedes_treatment: |
      Hard Rule 2: Krebs's generic attribution language preserved verbatim.
      Archimedes does NOT promote 'Russia-backed hacking groups' to specific
      roster-actor attribution (APT28 / Sandworm / APT29) absent explicit
      Krebs (or other A/B-grade) naming. The infrastructure ecosystem
      provides context relevant to APT28 (#006) / Sandworm (#007) / APT29
      (#009) operations against EU / Russia-Ukraine geopolitical conflict
      but does NOT constitute a new actor-attribution claim.

  - claim: "WorkTitans and MIRhosting were the most-used networks in pro-Russian attacks on Danish government bodies during the week of Denmark's municipal elections (2025-11-13 to 2025-11-19)"
    source: "Brian Krebs 2026-05-25 quoting de Volkskrant data review"
    attribution_specificity: "infrastructure-level; no specific attacker named"
    confidence_per_source: "moderate (relayed de Volkskrant data review)"
    archimedes_treatment: |
      Hard Rule 2: relay-layer claim; cite Krebs cite of de Volkskrant.
      Defender-context observation re: pro-Russian-attacker infrastructure
      ecosystem; not a roster-actor attribution.

  - claim: "FIOD arrested Andrey Nesterenko and Youssef Zinad on 2026-05-18 and seized 800+ servers across multiple Dutch business and data-center locations"
    source: "Brian Krebs 2026-05-25 quoting de Volkskrant + FIOD official statement"
    confidence_per_source: "high (multi-source procedural attestation)"
    archimedes_treatment: |
      Procedural attestation; treat as A-grade-equivalent on the procedural-
      facts layer per the same precedent as Cisco PSIRT / F5 / kernel.org-
      netdev procedural-facts attestation pattern.

flash_trigger_evaluation:
  trigger_2_tracked_actor_attribution:
    fired: false
    reason: |
      No specific tracked roster actor named — generic "Russia-backed
      hacking groups" / "Russia's intelligence agencies" attribution does
      NOT satisfy attributed_actor in _roster.yaml. APT28 / Sandworm /
      APT29 are corpus-anchored operators in the Russia-backed-hacking-
      groups attribution space, but Krebs does NOT name them in this piece.
      Per Hard Rule 2, Archimedes does NOT promote generic attribution to
      specific roster-actor attribution.

  trigger_5_ad_sector_campaign:
    fired: false
    reason: |
      LE-takedown of supporting infrastructure is not an "active multi-
      victim campaign vs. A&D sector" frame. Named victims (Danish
      government bodies, November 2025) are non-A&D-prime; targeting is
      geopolitical-disruption / election-influence, not A&D-targeting.

  trigger_1_critical_cve_exploited: not_applicable_no_cve
  trigger_3_first_party_ioc_hit: not_applicable_no_splunk_match
  trigger_4_tracked_actor_ttp_change: not_applicable_no_specific_actor_named
  trigger_6_zero_day_no_patch: not_applicable_no_cve

grader_recommendations:
  - action: "Consider INFRASTRUCTURE-CLUSTER tracking-entry scaffold for the Stark Industries / MIRhosting / WorkTitans / PQHosting ecosystem"
    rationale: |
      First corpus citation of this ecosystem. Operator-decision whether
      to scaffold a parallel tracking-entry structure for infrastructure
      clusters separate from actor / vulnerability roster, or alternatively
      append to APT28 / Sandworm / APT29 dossier infrastructure-ecosystem
      context sections. The 2024-2026 Krebs investigation chain provides
      substantial corpus background for either path.
  - action: "Briefer-side carry-forward to 16:00 PM brief as Russia-aligned-infrastructure ecosystem LE-takedown context"
    rationale: |
      Worth surfacing in PM brief 'Other Signal' or 'Geopolitical Context'
      section as ecosystem-disruption signal value for defender posture.
      Frame: LE action against APT28 / Sandworm / APT29 operator stack
      supporting infrastructure; not direct A&D-prime targeting. Hard Rule 2
      framing: generic "Russia-backed hacking groups" attribution preserved
      verbatim — no specific roster-actor promotion.

ecosystem_relevance_to_ad_prime_target_profile:
  direct_ad_prime_impact: none
  indirect_ad_prime_relevance: |
    APT28 (#006) / Sandworm (#007) / APT29 (#009) are HIGH-threat-level
    Russia-state actors with documented historical campaigns targeting
    aerospace and defense primes and their suppliers in espionage and
    sabotage campaign portfolios. Infrastructure ecosystem disruption
    (Stark / MIRhosting / WorkTitans takedown) reduces the operational
    capacity of the proxy / anonymity / DDoS-staging layer that supports
    these actors' broader operations — including any A&D-prime-targeting
    sub-campaigns. Defender-posture value is ecosystem-context, not
    direct-impact.
```

## Source-grade & WEP framing for grader

- Source grade at this surface: B (krebs; investigative journalism with multi-decade track record).
- WEP for the procedural-facts layer (arrests, server seizure, FIOD raid date and locations, defendant identities): "very likely" on multi-source procedural attestation (Krebs cites de Volkskrant + FIOD official statement).
- WEP for the infrastructure-ecosystem attribution layer (Stark / PQHosting / WorkTitans / MIRhosting hosting Russia-backed cyberattack infrastructure): "very likely" on Krebs multi-year investigation chain (2024, 2025-05, 2025-09, 2026-05 sequence).
- WEP for the Danish elections attack-windows attribution (WorkTitans + MIRhosting most-used networks): "likely" on de Volkskrant data-review relay (not direct A-grade telemetry attestation).
- WEP for any specific roster-actor attribution (APT28 / Sandworm / APT29): NOT CLAIMED — Krebs explicitly uses generic attribution language; Archimedes does not extrapolate.

---

*Archimedes raw-signal collected at 2026-05-25T15:35:00-04:00 from Krebs on Security 2026-05-25. Sole originating primary on the specific 2026-05-18 raid / arrest narrative culmination (cites de Volkskrant + FIOD official statement). First corpus citation of the Stark Industries / MIRhosting / WorkTitans / Nesterenko / Zinad / FIOD ecosystem. Generic "Russia-backed hacking groups" attribution preserved verbatim per Hard Rule 2 — no roster-actor promotion. Trigger 2 + Trigger 5 explicitly fail. Recommended for grader infrastructure-cluster tracking-entry decision and briefer 16:00 PM brief geopolitical-context carry-forward.*
