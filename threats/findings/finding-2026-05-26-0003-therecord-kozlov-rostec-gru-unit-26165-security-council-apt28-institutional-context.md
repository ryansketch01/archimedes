---
finding_id: finding-2026-05-26-0003-therecord-kozlov-rostec-gru-unit-26165-security-council-apt28-institutional-context
created_at: 2026-05-26T08:00:00-04:00
graded_by: grader
grading_run_id: morning-20260526-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  kozlov_appointment_to_security_council_aide_to_shoigu: B2
  kozlov_former_rostec_cybersecurity_center_head: B2
  kozlov_reportedly_held_classified_clearance_under_military_unit_26165: B3  # "reportedly" qualifier
  predecessor_konovalchik_also_reportedly_linked_to_unit_26165: B3  # "reportedly" qualifier
  unit_26165_85th_gtsss_institutional_home_of_apt28_fancy_bear_blue_delta_forest_blizzard: A1  # corpus baseline, established attribution
  unit_26165_historical_targeting_governments_defense_contractors_logistics_policy_orgs_europe_us: A1  # corpus baseline
  rostec_state_owned_defense_conglomerate_kozlov_prior_employer: A1  # publicly known fact
  no_new_operational_compromise_no_new_ttp_no_new_victimology: A1
  no_ad_prime_named_compromised: A1
  splunk_first_party_zero_hits_on_kozlov_rostec_unit_26165: A1
  cluster_anchor: B2

digraph_anchor: >
  Cluster digraph B2 anchored on The Record (Daryna Antoniuk byline,
  2026-05-25 19:00 EDT in-window) reporting Russia's Security Council
  appointment of Andrei Kozlov, former head of a cybersecurity center
  within state-owned defense conglomerate Rostec, as aide to Security
  Council Secretary Sergei Shoigu. The Record reports Kozlov
  "reportedly held a classified security clearance under Military
  Unit 26165" (85th Main Special Service Center / 85th GTsSS — the
  GRU institutional home of APT28 / Fancy Bear / Forest Blizzard /
  BlueDelta), and that his predecessor Pavel Konovalchik was "also
  reportedly linked to the same GRU unit." This is institutional /
  personnel context — not an operational compromise event, no new
  TTP, no new victimology, no IOCs. The Record is graded B per
  source-grades.yaml. Single-source. Corpus baseline on Unit 26165
  / 85th GTsSS / APT28 institutional attribution is established
  via Western intelligence community consensus (FBI/CISA/NCSC joint
  advisories from 2018 onward, Mandiant + CrowdStrike + Unit 42 +
  MSTIC documentation since at least 2014); The Record's framing
  aligns with corpus baseline. Single-source veto applies — WEP
  ceiling capped at "likely" on the Kozlov-personnel-linkage claim;
  the underlying Unit 26165 institutional attribution is corpus-
  baseline and is restated, not originated. Defender-relevant intel
  signal — personnel movement at senior Russian state-cyber chain of
  command may correlate with medium-term tradecraft or targeting
  shifts in actor #006 (APT28) operations but Archimedes does NOT
  extrapolate to specific predictions per Hard Rule 2.

source_reliability:
  grade: B
  source_name: "The Record (Recorded Future News)"
  source_yaml_id: the-record
  grade_rationale: >
    Pre-assigned B per source-grades.yaml ("Quality journalism,
    usually well-sourced"). Daryna Antoniuk is a Recorded Future
    staff journalist with a multi-year Russia/Ukraine cyber-policy
    reporting beat. Single-source piece without independent
    corroboration of the Kozlov-Unit-26165 linkage at the time of
    this grading.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_ttps_or_known_campaign_timing_targeting
    - probably_true_no_contradicting_evidence_from_ab_grade_sources
    - probably_true_technical_claims_internally_coherent
  rationale: >
    Consistent with established APT28 / Unit 26165 institutional
    attribution baseline (corpus-anchored via Mandiant, CrowdStrike,
    Unit 42, MSTIC, FBI/CISA/NCSC joint advisories). The
    Rostec-cybersecurity-center → Russia Security Council → Shoigu-
    aide career trajectory is plausible within Russian state-cyber
    institutional architecture. No contradicting evidence from A/B-
    grade sources. The "reportedly held a classified security
    clearance" qualifier flags the Kozlov-Unit-26165 personnel
    linkage as a single-source-attestation point — credibility 2
    rather than 1 because the predecessor-Konovalchik linkage and
    the Kozlov linkage are both qualified "reportedly," consistent
    with a journalist-investigation source-protection pattern.
    Predecessor-pattern (Konovalchik → Kozlov, both reportedly
    linked to same GRU unit) is consistent with a deliberate
    institutional-staffing pattern at the Security Council aide
    role.

corroboration:
  independent_sources:
    - the-record
  independent: false
  test_passed: >
    Single-source. The corpus-baseline Unit 26165 / 85th GTsSS /
    APT28 institutional attribution is established via Western
    intelligence community consensus (FBI/CISA/NCSC joint advisories,
    Mandiant/CrowdStrike/Unit 42/MSTIC documentation) but that
    baseline does NOT independently corroborate The Record's
    specific Kozlov-personnel-linkage claim. The Kozlov-personnel
    layer is single-source-effective. Corroboration test fails on
    independence for the personnel-linkage layer. Underlying
    institutional attribution is corpus-baseline (multi-source
    established baseline; not the same as cluster-internal
    corroboration).

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    14h pre-brief sentinel sweep included Kremlin, Kozlov, Rostec,
    Unit 26165, APT28, Sandworm, APT29 keywords across
    defenseclaw_local and archimedes indices. Zero events returned.
    Per Hard Rule 8, silence is not disconfirming. This is personnel/
    institutional intelligence — first-party-IOC class is not
    applicable.

single_source_veto_applied: true
single_source_veto_rationale: >
  Single-source The Record piece on the Kozlov-personnel-linkage
  claim. WEP ceiling capped at "likely" on the institutional-
  context-shift signal. The underlying Unit 26165 / APT28
  attribution is corpus-baseline (multi-source) but the specific
  Kozlov-Unit-26165 linkage and Kozlov-Security-Council appointment
  significance is single-source pending independent corroboration
  (potential corroboration paths: Reuters / FT / NYT / WSJ Russia
  desk coverage; Atlantic Council DFRLab open-source biographical
  analysis; OFAC / EU sanctions-designation paperwork if Kozlov is
  ever designated).

wep_ceiling: likely
wep_layered:
  kozlov_appointed_to_security_council_aide_to_shoigu: very_likely  # procedural-government-appointment fact, citing TASS as wire source
  kozlov_former_rostec_cybersecurity_center_head: very_likely  # publicly verifiable employment record class
  kozlov_held_classified_clearance_under_unit_26165: likely  # "reportedly" qualifier; single-source attestation
  konovalchik_predecessor_also_linked_unit_26165: likely  # "reportedly" qualifier; single-source attestation
  unit_26165_85th_gtsss_apt28_attribution: not_a_new_claim  # corpus baseline restated
  defender_relevance_medium_term_tradecraft_or_targeting_correlation_unknown: not_claimed  # Hard Rule 2: Archimedes does not extrapolate
  no_new_ad_prime_targeting: not_claimed

inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update      # APT28 (#006) institutional-context dossier note
  not_eligible_for:
    - flash                     # No FLASH trigger fires; institutional-context only
    - daily_brief_action        # No actionable defender signal (no IOC, no CVE, no active campaign)
  inclusion_rationale: >
    B2 cluster anchor → eligible for daily brief monitoring section
    per INTEL-GRADING.md thresholds. Actor profile update eligible
    for APT28 (#006) dossier institutional-context note (next-review
    due 2026-07-02). NOT eligible for action-item placement because
    the finding is institutional-context only — no IOCs, no CVE, no
    active campaign attribution, no A&D-prime victim. Brief-tier
    Russia-state-cyber chain-of-command intel signal.

# Cluster metadata
cluster:
  topic: "Kremlin appoints Andrei Kozlov (former Rostec cybersecurity center head, reportedly held classified clearance under Military Unit 26165 / 85th GTsSS — institutional home of APT28 / Fancy Bear / Forest Blizzard / BlueDelta) as Security Council aide to Sergei Shoigu; predecessor Pavel Konovalchik also reportedly linked to same GRU unit per The Record"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-26-am-003-therecord-kremlin-andrei-kozlov-gru-unit-26165-rostec-security-council-apt28
  related_actors: ["006"]   # APT28 institutional-context dossier note
  related_vulnerabilities: []
  related_campaigns: []
  attribution_claims:
    - claimed_actor: "APT28 / Fancy Bear / Forest Blizzard / BlueDelta / Sofacy / Sednit / Pawn Storm / STRONTIUM / FROZENLAKE / Fighting Ursa / Iron Twilight / GruesomeLarch / UAC-0001 / TG-4127 / Tsar Team / Group 74"
      claimed_actor_roster_id: "006"
      claimed_by_sources: [the-record]
      attribution_specificity: >
        The Record names Unit 26165 / 85th Main Special Service
        Center / 85th GTsSS as the institutional home of "Fancy Bear,
        APT28, BlueDelta, Forest Blizzard." Western intelligence
        community baseline. Corpus-anchored per _roster.yaml actor
        #006 attribution (nation=RU, service=GRU, unit="Unit 26165
        (85th GTsSS)"). MITRE ATT&CK ID G0007.
      hard_rule_2_treatment: >
        Corpus-baseline attribution restated. The Record's framing
        aligns with established attribution. Archimedes does NOT
        originate attribution. The Kozlov-personnel-linkage to Unit
        26165 is the new institutional-context layer; the underlying
        APT28-Unit-26165 attribution is corpus-baseline.
      requires_analyst_review: false

# IOCs surfaced
iocs_surfaced: []   # No technical IOCs; institutional/personnel intelligence only

ttp_keywords: []    # No TTPs documented; Unit 26165 historical TTP categories ("cyber espionage, credential theft, influence operations") restated at category level only, not specific new tradecraft

# Downstream handoff flags
analyst_review_required: false      # Corpus-baseline restatement; institutional-context only; no novel attribution; no operational claim
red_team_review_required: false     # WEP ceiling "likely" not "very likely"; no red-team challenge required per CLAUDE.md threshold
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null
actor_profiler_handoff:
  actor_id: "006"
  dossier_path: threats/threat-actors/APT28/
  next_review_due: 2026-07-02
  handoff_notes: >
    Add Kozlov-appointment + institutional-context observation to the
    APT28 dossier "Institutional Background & Chain of Command"
    section at the next /update-tracking cycle. Note: this is
    personnel-context, not operational tradecraft change. Do NOT
    extrapolate to specific predictions; preserve The Record's
    framing verbatim.

# Lifecycle
tlp: CLEAR
published_in_briefs: []
retracted: false
retraction_brief_id: null
---

# The Record: Kremlin Appoints Andrei Kozlov, Former Rostec Cybersecurity Center Head Reportedly Linked to GRU Unit 26165 (APT28 Institutional Home), as Aide to Security Council Secretary Shoigu

## Summary

The Record (Daryna Antoniuk byline, 2026-05-25 19:00 EDT) reports that Andrei Kozlov — the former head of a cybersecurity center within Russia's state-owned defense conglomerate Rostec — has been named an aide to Security Council Secretary Sergei Shoigu. The Record states Kozlov "reportedly held a classified security clearance under Military Unit 26165," the GRU's 85th Main Special Service Center (85th GTsSS), which Western intelligence community consensus identifies as the institutional home of APT28 / Fancy Bear / Forest Blizzard / BlueDelta. The Record notes that Kozlov's predecessor in the role, Pavel Konovalchik, was "also reportedly linked to the same GRU unit," suggesting an institutional staffing pattern. The Record additionally enumerates Unit 26165's historical targeting of "governments, defense contractors, logistics companies and policy organizations across Europe and the United States" — corpus-baseline restated, not new attribution. No new operational compromise, no new TTP, no new victimology, no IOCs. Defender-relevant intel signal at the Russian state-cyber chain-of-command level. Archimedes does NOT extrapolate the personnel movement to specific operational predictions per Hard Rule 2.

## Sources

### The Record (the-record, digraph: B)

- URL: https://therecord.media/andrei-kozlov-appointed-russia-security-council
- Published: 2026-05-25 19:00 EDT
- Byline: Daryna Antoniuk
- Key claim: Kozlov, former Rostec cybersecurity center head reportedly holding classified clearance under Military Unit 26165 (85th GTsSS / APT28 institutional home), appointed aide to Russia Security Council Secretary Sergei Shoigu; predecessor Konovalchik also reportedly linked to the same GRU unit.

## Technical detail

### Named persons

- **Andrei Kozlov** — appointee. Former head of a cybersecurity center within Rostec. Reportedly held a classified security clearance under Military Unit 26165.
- **Sergei Shoigu** — Security Council Secretary (Kozlov's new reporting line).
- **Pavel Konovalchik** — predecessor in the same Security Council aide role; "also reportedly linked to the same GRU unit" per The Record.
- **Vladimir Putin** — Russian President; appointment context.

### Named organizations

- **Russia's Security Council** — Kozlov's new affiliation.
- **Rostec** — Russian state-owned defense conglomerate; Kozlov's prior employer (head of cybersecurity center within).
- **GRU Military Unit 26165 / 85th Main Special Service Center (85th GTsSS)** — Kozlov's reported prior classified security clearance affiliation; also linked to predecessor Konovalchik.
- **RT-Information Security (RT-IB)** — Rostec subsidiary referenced in article context.
- **TASS** — Russian state news agency (article source).

### Unit 26165 historical targeting (per The Record, corpus baseline)

The Record enumerates Unit 26165's historical activity as "cyber espionage, credential theft and influence operations targeting governments, defense contractors, logistics companies and policy organizations across Europe and the United States." This is corpus-baseline restated — actor #006 (APT28) per `_roster.yaml`.

### Aliases per The Record + corpus baseline

Per The Record: Fancy Bear, APT28, BlueDelta, Forest Blizzard. Per `_roster.yaml` actor #006, additional aliases: Sofacy, Sednit, Pawn Storm, STRONTIUM, FROZENLAKE, Fighting Ursa, Iron Twilight, GruesomeLarch, UAC-0001, TG-4127, Tsar Team, Group 74. MITRE ATT&CK ID: G0007.

## IOCs surfaced

None. Institutional and personnel intelligence only; no network IOCs, no file hashes, no domains, no IPs.

## Relationship to existing findings

- **Actor dossier #006 (APT28 / Fancy Bear / Forest Blizzard / BlueDelta)** — next-review due 2026-07-02 per `_roster.yaml`. This finding is an institutional-context note for the dossier "Institutional Background & Chain of Command" section.
- No direct overlap with active operational findings. Cross-references existing corpus surfaces on Russia-aligned cyber infrastructure (`finding-2026-05-25-0003` Netherlands FIOD / MIRhosting / WorkTitans takedown of Stark Industries Solutions successor stack) only at the ecosystem level — no operational linkage between the Stark/MIRhosting ecosystem disruption and the Kozlov appointment in this reporting.

## Open questions for analyst

- Independent corroboration request: Reuters / FT / NYT / WSJ Russia-desk coverage of the appointment; Atlantic Council DFRLab open-source biographical analysis of Kozlov; OFAC / EU sanctions-designation paperwork if Kozlov is ever designated. If independent corroboration arrives, regrade the Kozlov-Unit-26165 linkage from likely toward very_likely.
- Actor-profiler /update-tracking 2026-07-02: add Kozlov + Konovalchik institutional-context observation to the APT28 dossier "Institutional Background & Chain of Command" section. Note: this is personnel context, not operational tradecraft change. Do NOT extrapolate.
- Open question for medium-term intel signal monitoring (not promoted as a prediction): does the Kozlov-to-Security-Council appointment correlate over the next 90-180 days with observable tradecraft or targeting changes in APT28 operations against European or U.S. defense-contractor / logistics / policy-organization victims? This is a watch-item framing, not a forecast.
