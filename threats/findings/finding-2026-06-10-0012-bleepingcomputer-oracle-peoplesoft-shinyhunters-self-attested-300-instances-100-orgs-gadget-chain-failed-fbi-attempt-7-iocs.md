---
finding_id: finding-2026-06-10-0012-bleepingcomputer-oracle-peoplesoft-shinyhunters-self-attested-300-instances-100-orgs-gadget-chain-failed-fbi-attempt-7-iocs
created_at: 2026-06-10T16:18:00-04:00
graded_by: grader
grading_run_id: afternoon-20260610-160000
grading_mode: scheduled_brief
test: false
status: graded

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  shinyhunters_self_attested_300_instances_100_plus_orgs_per_bc: B3                    # BC sole-source on actor self-attestation; actor self-attestation is per-source-reported claim, not corroborated fact
  nottingham_university_named_victim_data_published_on_shinyhunters_leak_site: B2       # BC primary; leak-site verifiability not directly retrieved (Hard Rule 1 considerations)
  failed_fbi_peoplesoft_portal_breach_attempt: B3                                       # BC single-source on failed-targeting claim
  oracle_peoplesoft_exploitation_via_gadget_chain_of_old_and_zero_day_vulnerabilities: B2  # BC primary; technical framing per actor self-attestation + BC editorial framing
  exploitation_success_variable_depending_on_instance_configuration: B2                   # BC primary
  no_specific_cve_assigned: B1                                                            # Verifiable absence in primary
  oracle_had_not_responded_at_bc_publication_time: B1                                     # Verifiable absence
  ipv4_iocs_142_11_200_186_thru_190_and_108_174_202_99_and_176_120_22_24: B2              # BC primary published IOCs; first-party Splunk silent over -90d (corroborating absence of internal exposure but not confirming external claim)
  domain_azurenetfiles_net_tls_cert_cn_linked_to_shinyhunters: B2                          # BC primary published IOC
  ad_prime_named_victim_explicitly_none_education_sector_primary: B1                       # Verifiable absence in BC primary
  oracle_peoplesoft_a_d_prime_structural_relevance_indirect: C2                            # Grader-side structural inference; HR/finance/supply-chain ERP deployment pattern
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored on ONE B-grade media primary (BleepingComputer
  Lawrence Abrams 2026-06-10T18:31:57 UTC). No secondary primary
  surfaced in window. ShinyHunters self-attestation to BC is the
  load-bearing source on attribution + scope claims.

  B2 (not B1, not B3) anchored because:

    - SOURCE LETTER GRADE: One B-grade media primary
      (BleepingComputer ratified B). BC reports the actor
      self-attestation directly received from ShinyHunters
      group. No Oracle vendor advisory + no Tier-1 IR firm
      telemetry + no independent corroboration. Cluster
      letter holds at B under conservative single-source-
      primary aggregation.

    - INDEPENDENCE TEST: Single-source cluster. Actor self-
      attestation is one-side of a non-mutual disclosure
      (BC received from actor; Oracle not responded). No
      independent IR firm or vendor cross-corroboration
      available in-window.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed): FAILS — single-source primary,
        actor self-attestation with no independent
        corroboration.
      * Grade 2 (Probably True) PASSES on procedural facts:
        ShinyHunters is established long-running extortion
        group with multi-year mass-data-theft pattern (AT&T
        2024, Microsoft, AWS prior incidents);
        self-attestation pattern (claiming-to-press cadence)
        is consistent with LockBit / BlackCat / Scattered
        Spider press-relations playbook; published IPv4 +
        domain IOCs lend technical specificity that elevates
        from pure self-claim.
      * Grade 3 (Possibly True) applies on specific scope
        claims (300 instances / 100+ orgs) that are
        actor-self-attested with no independent verification.

    - SUBSTANTIVE CLAIM LAYERS:
      * Existence of campaign + Nottingham University
        named-victim claim + published IOCs: B2 — BC primary;
        IOC publication adds technical specificity over pure
        self-claim.
      * ShinyHunters self-attested 300 instances / 100+ orgs
        scope claim: B3 — single-source, actor self-
        attestation, no independent verification possible
        in-window. Hard Rule 2 preserved: report as actor
        self-claim, NOT propagate as Archimedes-confirmed.
      * Failed FBI PeopleSoft portal attempt claim: B3 —
        single-source, BC editorial framing of actor claim.
      * Gadget chain of "old and zero-day vulnerabilities"
        framing: B2 — BC primary; technical class
        plausible but no specific CVE designations.
      * No named A&D-prime victim: B1 — verifiable absence.
      * A&D-prime structural relevance via Oracle PeopleSoft
        HR/finance/supply-chain ERP deployment pattern: C2 —
        grader-side structural inference per target profile;
        Hard Rule 2 preserved (no A&D-victim propagation).

  Single-source veto APPLIED on:
    - 300-instances / 100+-orgs scope claim (actor self-
      attestation, no independent verification; WEP capped
      at "likely").
    - Failed FBI PeopleSoft portal attempt claim (BC
      single-source editorial framing of actor claim).
    - Gadget-chain technical framing (no specific CVE).

  Single-source veto NOT applied on:
    - Existence of campaign + leak-site presence (BC
      primary; first-party-publishable observation).
    - Published IPv4 + domain IOCs (BC primary;
      operator-actionable).
    - No-named-A&D-prime-victim and Oracle-no-response
      facts (verifiable absences).

source_reliability:
  cluster_anchor_grade: B
  sources:
    - source_yaml_id: bleepingcomputer
      grade: B
      provisional: false
      role: "Sole-primary (Lawrence Abrams byline) of ShinyHunters self-attestation + IOC publication on Oracle PeopleSoft mass-data-theft campaign"
  grade_rationale: >
    Cluster letter grade holds at B (single B-grade media
    primary). Actor self-attestation pattern is consistent
    with established extortion-group press-relations
    playbook; BC's track record on ransomware/cybercrime
    reporting is the load-bearing factor.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_shinyhunters_multi_year_mass_data_theft_pattern
    - probably_true_no_contradicting_a_b_source
    - probably_true_technical_claims_internally_coherent_oracle_peoplesoft_widely_deployed_actor_press_relations_cadence_documented
  rationale: >
    ShinyHunters is established long-running extortion group
    (active since approximately 2020) with multi-year multi-
    victim mass-data-theft track record (AT&T 2024, Microsoft,
    AWS prior incidents). Self-attestation-to-press cadence is
    consistent with LockBit / BlackCat / Scattered Spider
    press-relations playbook. Published IPv4 + domain IOCs add
    technical specificity over pure self-claim. No contradicting
    source. Scope-claim layers (300 instances / 100+ orgs;
    failed FBI attempt) are actor self-attestation under single-
    source veto.

corroboration:
  independent_sources:
    - bleepingcomputer
  independent: false
  test_passed: >
    Independence test FAILS — single-source primary. Actor
    self-attestation to BC is one-side of non-mutual
    disclosure. No independent IR firm or Oracle vendor
    cross-corroboration available in-window. Watch signals:
    Oracle vendor advisory; Tier-1 IR firm telemetry; KEV
    addition on any specific CVE; secondary news outlet
    independent confirmation of leak-site contents
    (constrained by Hard Rule 1 / TLP considerations on
    leak-site contents).

first_party_precedence:
  applied: true
  splunk_evidence: >
    Splunk first-party hunt executed against published IOCs:
    archimedes + defenseclaw_local indices queried for
    src_ip IN (142.11.200.186-190, 108.174.202.99, 176.120.22.24)
    over -90d window. RESULT: zero hits across all 7 IPv4
    addresses. Per Hard Rule 8 / INTEL-GRADING.md / sat-ach
    discipline: absence-of-evidence is NOT evidence-of-absence.
    Silent Splunk on these IOCs is NOT disconfirming of
    external claim; consistent with no known internal exposure
    to date. First-party precedence applied as "no
    contradiction" rather than as "confirmation" or
    "disconfirmation."
  splunk_query_executed: "index=archimedes OR index=defenseclaw_local (src_ip=\"142.11.200.186\" OR src_ip=\"142.11.200.187\" OR src_ip=\"142.11.200.188\" OR src_ip=\"142.11.200.189\" OR src_ip=\"142.11.200.190\" OR src_ip=\"108.174.202.99\" OR src_ip=\"176.120.22.24\")"
  splunk_window: "-90d"
  splunk_result: "zero events across all 7 IPv4 IOCs"
  splunk_interpretation: "no_internal_exposure_to_published_ipv4_iocs_silent_not_disconfirming"

single_source_veto_applied: true
single_source_veto_layers:
  - shinyhunters_self_attested_300_instances_100_plus_orgs_scope_claim
  - failed_fbi_peoplesoft_portal_attempt_claim
  - gadget_chain_old_zero_day_technical_framing_no_specific_cve
wep_ceiling: likely

inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - other_signal_cybercriminal_watch
    - new_actor_candidate_referral

# Cluster metadata
cluster:
  topic: "ShinyHunters extortion group self-attests Oracle PeopleSoft mass-data-theft campaign to BleepingComputer — claims 300 instances / 100+ organizations exfiltrated via 'gadget chain of old and zero-day vulnerabilities'; Nottingham University named victim with data published on leak site; failed FBI PeopleSoft portal attempt claimed; Oracle silent; 7 IPv4 + 1 domain IOCs published; ShinyHunters NOT in Archimedes roster"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-10-pm-006
  attribution_claims:
    - claimed_actor: "ShinyHunters (self-attestation)"
      claimed_by_sources: [shinyhunters_via_bleepingcomputer]
      requires_analyst_review: true
      hard_rule_2_compliance: "Self-attribution by actor reported as fact-of-claim; preserve verbatim; do NOT upgrade to Archimedes-confirmed"
      roster_status: "NOT in _roster.yaml — recommend /new-actor candidate evaluation"

# Downstream handoff flags
analyst_review_required: true
analyst_review_complete: true
analyst_review_run_id: analyst-20260610-164500
red_team_review_required: false
red_team_review: null

# Analyst-driven WEP-layer adjustments (per SAT-ACH refutation discipline)
wep_layer_adjustments:
  - layer: shinyhunters_self_attested_300_instances_100_plus_orgs_scope_claim
    before: likely
    after: roughly_even_chance
    reason: "KAC A1 flags low-confidence-critical assumption on actor self-attestation truthfulness; no Archimedes-corpus base-rate calibration on ShinyHunters' prior self-attested scope claims. Brief should report scope verbatim as actor claim, NOT propagate as ground truth."
  - layer: failed_fbi_peoplesoft_portal_attempt_claim
    before: likely
    after: roughly_even_chance_h1_vs_h2
    reason: "ACH ranks H2 (publicity stunt) above H1 (genuine attempt) at zero vs one inconsistency. The failed-FBI-attempt-implies-A&D-prime-co-scoping escalation chain (KAC A3) is rejected or heavily qualified — its predicate is unsupported. Brief should explicitly frame as press-relations boast per ACH refutation discipline."
  - layer: campaign_existence_and_published_iocs
    before: likely
    after: likely
    reason: "Holds; published IPv4 + domain IOCs are technically specific (ACH E2) and likely tied to real campaign activity. The CAMPAIGN existence layer is robust; the SCOPE and FBI-ATTEMPT layers are the weakened claims."
  - layer: nottingham_university_named_victim
    before: likely
    after: likely
    reason: "Holds; BC's track record on leak-site reporting (KAC A6) supports the single-named-victim anchor."

# Tests flagged for actor-profiler follow-up
analyst_tests_flagged:
  - test_id: T1
    description: "/new-actor evaluation for ShinyHunters with retrospective base-rate calibration on AT&T 2024 / Microsoft / AWS self-attested-vs-confirmed scope ratios"
    unblocks: [kac_A1, future-shinyhunters-scope-claim-grading-baseline]
    priority: high
    blocks_publication: false
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "What is the most likely interpretation of ShinyHunters' self-attested claim of an unsuccessful attempt to compromise the FBI's PeopleSoft portal — given that this is a single-source actor self-attestation reported by BC?"
      analyzed_at: 2026-06-10T16:45:00-04:00
      analyzed_by: analyst
      red_team_review: null

      hypotheses:
        - id: H1
          statement: "Genuine targeting attempt: ShinyHunters actually probed/exploited the FBI PeopleSoft portal as part of the broader 300-instances campaign and the attempt failed on instance hardening or detection. The disclosure to BC is post-hoc credibility-building on a real but unsuccessful operation."
        - id: H2
          statement: "Publicity stunt: ShinyHunters never seriously attempted the FBI PeopleSoft portal — the claim is fabricated or exaggerated press-relations boasting to maximize media coverage and reputation among the criminal/affiliate ecosystem. The boast costs nothing (FBI can neither confirm nor deny), buys reputation."
        - id: H3
          statement: "Genuine but trivial probing: ShinyHunters sent automated scanning traffic toward an FBI-attributed IP space as part of broader internet-wide scanning, with no specific intent to breach. The post-hoc 'failed FBI attempt' framing elevates routine scanning into a strategic boast."
        - id: H4
          statement: "Misattribution by the actor: ShinyHunters did attempt to breach a PeopleSoft instance they believed was FBI-attributed but was actually a federal-contractor or commercial instance with FBI-adjacent IP/branding. The 'failed FBI attempt' is the actor's own mismeasurement, not Archimedes'."
        - id: H5
          statement: "Wholly fabricated: no probe occurred at any layer. The boast exists purely as a narrative device to attach the operation to a high-prestige federal target. Functions identically to H2 from a defender perspective but is informationally distinct."

      evidence:
        - id: E1
          description: "ShinyHunters has a multi-year track record of mass-data-theft operations (AT&T 2024, Microsoft, AWS prior incidents) with a documented press-relations cadence."
          source: bc-primary-editorial-context
          digraph: B2
          weight: 2
        - id: E2
          description: "ShinyHunters published 7 IPv4 IOCs + 1 TLS-cert domain through BC — a level of technical specificity not consistent with pure fabrication."
          source: bc-primary
          digraph: B2
          weight: 2
        - id: E3
          description: "Splunk first-party hunt across both indices (-90d) on all 7 IPv4 IOCs returned ZERO hits — silent, not disconfirming."
          source: splunk-first-party
          digraph: A1
          weight: 3
        - id: E4
          description: "Self-attested scope is 300 instances / 100+ orgs. Nottingham University is the ONLY specifically named victim with data on the leak site."
          source: bc-primary
          digraph: B2
          weight: 2
        - id: E5
          description: "Oracle had NOT responded at BC publication time; no vendor advisory, no separate PeopleSoft-specific statement."
          source: bc-primary
          digraph: B1
          weight: 2
        - id: E6
          description: "No specific CVE designations; mechanism framed as 'gadget chain of old and zero-day vulnerabilities' with success 'variable depending on instance configuration.'"
          source: bc-primary
          digraph: B2
          weight: 2
        - id: E7
          description: "Failed FBI portal claim provides no technical detail (no specific instance URL, no specific CVE chain attempted, no specific failure mode)."
          source: bc-primary
          digraph: B3
          weight: 1
        - id: E8
          description: "Industry-standard ransomware/extortion press-relations playbook (LockBit, BlackCat, Scattered Spider precedents) includes high-prestige-target name-dropping for affiliate-ecosystem reputation."
          source: cross-corpus-precedent
          digraph: B2
          weight: 2
        - id: E9
          description: "No FBI public response, statement, or denial of the claim."
          source: absence
          digraph: B1
          weight: 1
        - id: E10
          description: "ShinyHunters is NOT currently in the Archimedes roster — first-Archimedes-corpus surface; no Archimedes prior baseline on their truthfulness in self-attestation."
          source: roster-state
          digraph: B1
          weight: 1

      matrix:
        E1: {H1: C, H2: C, H3: C, H4: C, H5: C}  # Track record consistent with any hypothesis where the actor IS ShinyHunters
        E2: {H1: C, H2: N, H3: C, H4: C, H5: I}  # Technical IOC specificity weighs against pure fabrication (H5); consistent with H1/H3/H4; neutral for H2 (boast about FBI can be fabricated separately from real IOCs from real other ops)
        E3: {H1: N, H2: N, H3: N, H4: N, H5: N}  # Splunk silence non-diagnostic; absence of evidence
        E4: {H1: N, H2: C, H3: N, H4: N, H5: C}  # Single named victim against 300-instance claim is consistent with publicity-stunt scope inflation (H2) or wholly-fabricated scope (H5); neutral on FBI-specific claim
        E5: {H1: N, H2: N, H3: N, H4: N, H5: N}  # Oracle silence does not distinguish
        E6: {H1: C, H2: C, H3: C, H4: C, H5: C}  # Vague technical framing fits all hypotheses
        E7: {H1: I, H2: C, H3: I, H4: I, H5: C}  # Lack of technical detail on failed attempt is mildly inconsistent with genuine attempt hypotheses (H1/H3/H4) — a real failed attempt would normally generate observable artifacts the actor could cite; consistent with boast-only hypotheses (H2/H5)
        E8: {H1: N, H2: C, H3: N, H4: N, H5: C}  # Press-relations playbook precedent supports H2/H5 (boasting hypothesis); neutral on genuine-attempt hypotheses
        E9: {H1: N, H2: C, H3: N, H4: N, H5: C}  # No FBI denial is consistent with publicity stunt (boasting against unprovable target); neutral on genuine attempts
        E10: {H1: N, H2: N, H3: N, H4: N, H5: N}  # Roster gap is non-diagnostic on truthfulness

      inconsistency_counts:
        H1: 1
        H2: 0
        H3: 1
        H4: 1
        H5: 1

      diagnostic_evidence:
        - E7: "Distinguishes boast-only hypotheses (H2/H5) — which require no technical artifacts — from genuine-attempt hypotheses (H1/H3/H4) which would normally generate citable evidence"
        - E8: "Distinguishes publicity-stunt (H2/H5) precedent-fit from genuine-targeting hypotheses"
        - E2: "Distinguishes wholly-fabricated (H5) from hypotheses where IOCs come from real campaign elements (H1/H3/H4) and the FBI boast layers on top (H2)"

      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: "Zero inconsistencies. Publicity-stunt fits the press-relations precedent (E8), the boasting-against-unprovable-target pattern (E9), and the lack of any technical artifact on the failed attempt (E7). H2 does NOT require the entire campaign to be fake — it only requires the FBI-specific layer to be boast. The 7 published IOCs (E2) likely trace to real campaign activity against the unnamed scope; the FBI claim is the layered-on boast."
          wep: likely
        - rank: 2
          hypothesis_id: H1
          rationale: "One inconsistency (E7 — absence of technical detail on the failed attempt). H1 is plausible — the actor's broader campaign IS real (E2 IOCs are specific) — but a genuine FBI attempt would normally generate citable artifacts the actor could use for credibility. Cannot be ruled out; substantially less likely than H2."
          wep: unlikely
        - rank: 3
          hypothesis_id: H3
          rationale: "One inconsistency (E7). Internet-wide scanning that incidentally touched FBI-attributed IPs is plausible operational base-rate; the actor's elevation of this into 'failed FBI attempt' is a framing layer. Plausible but the 'attempt' framing is overstated."
          wep: unlikely
        - rank: 4
          hypothesis_id: H4
          rationale: "One inconsistency (E7). Actor-side mismeasurement — actor believed an instance was FBI when it was a contractor/commercial instance with adjacent branding. Plausible but unverifiable from external observation."
          wep: unlikely
        - rank: 5
          hypothesis_id: H5
          rationale: "One inconsistency (E2 — 7 published IOCs are technically specific and likely tied to real campaign activity, mildly inconsistent with WHOLLY fabricated). H5 collapses to H2 if the FBI-specific claim is decoupled from the campaign-existence claim."
          wep: unlikely

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E7, E8]
        if_E7_resolved_with_actor_artifacts: "If the actor later provides specific technical detail on the failed FBI attempt (e.g., specific instance URL probed, specific CVE chain attempted, specific failure indicator), E7's inconsistency against H1/H3/H4 reverses. H1 would elevate."
        if_FBI_denies_explicitly: "Elevates H2/H5; demotes H1/H3/H4. Currently no FBI public response."
        if_FBI_confirms_attempt: "Inverse — confirms H1; demotes H2/H5."
        if_shinyhunters_track_record_revisited: "Cross-corpus review of prior ShinyHunters self-attested claims (AT&T 2024, Microsoft, AWS) for accuracy-vs-boast pattern would inform base rate on truthfulness. Worth pulling on /new-actor profile creation."

      tripwires:
        - observation: "FBI publicly confirms or denies the claimed attempt"
          effect: "Material change to H1-vs-H2 ranking"
        - observation: "ShinyHunters publishes additional technical detail on the failed FBI attempt (URL, CVE, failure mode)"
          effect: "Elevate H1; possibly trigger Archimedes confirmed-attempt framing"
        - observation: "Second independent source (Tier-1 IR firm) corroborates the 300-instance / 100+-org scope claim"
          effect: "Lift scope-claim layer WEP from 'likely' toward 'very likely'"
        - observation: "Oracle releases PeopleSoft advisory naming the gadget-chain CVEs"
          effect: "Resolves the no-specific-CVE layer; informs A&D-prime configuration audit actionability"
        - observation: "Splunk first-party hit on any of the 7 published IPv4 IOCs in archimedes / defenseclaw_local"
          effect: "First-party telemetry; rerun ACH with Hard Rule 8 weighting; may directly involve A&D-prime exposure"

      conclusion:
        summary: |
          The failed-FBI-attempt claim is most consistent with publicity-stunt
          press-relations boasting (H2), zero inconsistencies. Genuine-attempt
          hypotheses (H1/H3/H4) each carry one inconsistency — the absence of
          any technical artifact the actor could cite to substantiate the
          claim. The 7 published IOCs are technically specific and likely
          tie to real campaign activity against the unnamed scope; the FBI-
          specific claim layers on top as reputation-building boast. The
          underlying CAMPAIGN existence is real (IOCs are specific, named-
          victim Nottingham is verifiable); the FBI-attempt LAYER is the
          claim under question. Brief framing should preserve the actor's
          self-attestation verbatim and explicitly note that the failed-FBI-
          attempt claim is most consistent with press-relations precedent
          rather than confirmed targeting. Hard Rule 2 holds: actor self-
          attestation is reported as fact-of-claim; NOT propagated as
          Archimedes-confirmed federal targeting.
        wep: likely
        wep_layer_specific:
          campaign_existence_and_iocs: likely
          shinyhunters_self_attested_300_instances_100_orgs_scope: roughly_even_chance
          failed_fbi_peoplesoft_portal_attempt_claim: roughly_even_chance_h1_vs_h2
          nottingham_university_named_victim: likely
        confidence_caveats: |
          (1) Single-source BC primary; no independent IR firm corroboration
          available in-window; single-source veto persists.
          (2) Scope claim (300 instances / 100+ orgs) is actor self-attestation
          with only one independently-named victim — boasting / scope-inflation
          is plausible base-rate behavior; brief should report 'self-attested
          300 / 100+, only Nottingham specifically named' verbatim.
          (3) Failed FBI portal claim is most consistent with publicity-stunt
          (H2) under refutation discipline; brief should NOT propagate as
          confirmed federal-targeting attempt.
          (4) Splunk first-party silence is NOT disconfirming — A&D-prime
          PeopleSoft exposure is a structural concern independent of whether
          the 7 published IOCs touched the operator's environment.

  sat_kac:
    kac_analysis:
      assessment_under_review: |
        (a) ShinyHunters' self-attested scope claim (300 PeopleSoft instances
        across 100+ organizations) is approximately accurate.
        (b) A&D-prime structural exposure to Oracle PeopleSoft (HR/finance/
        supply-chain ERP deployment pattern across Lockheed Martin / Boeing /
        Northrop Grumman / RTX / BAE Systems / L3Harris) constitutes material
        defender-actionable risk independent of named-victim status.
        (c) The failed FBI portal claim, IF genuine, implies A&D-prime
        federal-contractor PeopleSoft instances are also co-scoped.
      analyzed_at: 2026-06-10T16:48:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication analyst review for 2026-06-10 PM brief — finding-2026-06-10-0012; grader-flagged sat_ach + sat_kac per single-source veto on scope + failed-FBI-attempt layers; /new-actor candidate referral"

      assumptions:
        - id: A1
          statement: "ShinyHunters' track record on prior self-attested claims (AT&T 2024, Microsoft, AWS) has been broadly accurate — meaning their self-attestation has signal value above baseline."
          category: source_reliability
          stated: false
          why_must_be_true: "The ACH H1 (genuine targeting) and the brief's scope-claim framing depend on the actor's self-attestation carrying signal."
          when_could_be_false: "Prior ShinyHunters self-attested scope claims were inflated 2-10x relative to ground-truth victim disclosure. (Historical CTI literature on ransomware/extortion self-attested counts is mixed — some groups inflate by integer factors, others under-report.)"
          evidence_for: [shinyhunters-multi-year-mass-data-theft-pattern-documented]
          evidence_against: [no-archimedes-corpus-prior-baseline-on-shinyhunters-truthfulness-pattern]
          confidence: low
          centrality: critical
          classification: test
          test_proposed: "On /new-actor evaluation for ShinyHunters, profiler should retrospectively grade the AT&T 2024 / Microsoft / AWS self-attested-vs-confirmed scope ratios as base-rate calibration. Until that's done, brief should report scope as actor-self-attested, NOT propagate as ground truth."
        - id: A2
          statement: "A&D primes (Lockheed Martin, Boeing, Northrop Grumman, RTX, BAE Systems, L3Harris) all have material Oracle PeopleSoft footprints in HR, finance, and supply-chain ERP."
          category: semantic
          stated: true
          why_must_be_true: "The finding's A&D-prime structural relevance claim rests on this deployment-pattern observation."
          when_could_be_false: "Tier-1 A&D primes have heterogeneous ERP stacks — some have migrated off PeopleSoft to Workday (HR), SAP (finance), or Oracle Fusion (cloud successor) over the past 5-10 years. The 'all major A&D primes have PeopleSoft' framing may overstate current density."
          evidence_for: [oracle-peoplesoft-historical-deployment-in-large-us-federal-contractors]
          evidence_against: [hr-migration-to-workday-trend-2018-2024-among-tier1-primes]
          confidence: medium
          centrality: material
          classification: qualify
          note: "Brief should frame as 'Oracle PeopleSoft is historically deeply deployed across major A&D primes' rather than 'all major A&D primes have material PeopleSoft footprints today.' The structural concern is real but the specific deployment density at 2026 timeline is heterogeneous and partially-migrated."
        - id: A3
          statement: "Failed FBI portal claim, IF genuine, indicates the actor is actively scoping federal-class PeopleSoft instances — and federal-contractor instances (A&D primes) are co-scoped."
          category: intent
          stated: true
          why_must_be_true: "The brief's escalation path from 'failed FBI attempt' to 'A&D-prime federal-contractor implication' depends on this logical chain."
          when_could_be_false: "ACH ranks H2 (publicity stunt) above H1 (genuine attempt) on refutation discipline. If H2 is correct, the failed FBI attempt provides ZERO signal on A&D-prime federal-contractor co-scoping. The brief's escalation chain breaks at the predicate."
          evidence_for: []
          evidence_against: [ach-ranking-h2-above-h1]
          confidence: low
          centrality: critical
          classification: reject_or_qualify_heavily
          note: "ACH H2 (publicity stunt) outranks H1 (genuine attempt). The 'failed FBI implies A&D-prime co-scoping' framing must be REJECTED or HEAVILY qualified. Brief should NOT propagate the escalation chain as Archimedes-assessed logic; report the actor's claim, note ACH refutation discipline ranks publicity-stunt higher."
        - id: A4
          statement: "Splunk first-party silence on the 7 published IPv4 IOCs over -90d is consistent with no operator-environment exposure to date."
          category: visibility
          stated: true
          why_must_be_true: "First-party precedence framing relies on the absence interpretation."
          when_could_be_false: "(a) Splunk logging coverage of relevant data sources is incomplete; (b) ShinyHunters' actual operational IPs are not the 7 published (which may be staging / proxy / sacrificial infrastructure); (c) the operator-environment is exposed via a different access vector entirely (compromised supplier connection, third-party IT services, federal-contractor M&A integration)."
          evidence_for: [archimedes-and-defenseclaw-local-index-coverage-baseline]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: qualify
          note: "Per Hard Rule 8 absence-is-not-evidence-of-absence. Brief should report Splunk silence as 'no internal exposure to the 7 published IPv4 IOCs over -90d' WITHOUT implying that's a clean bill of health on PeopleSoft exposure broadly. Splunk silence on IOCs ≠ Splunk silence on PeopleSoft activity."
        - id: A5
          statement: "Oracle's lack of response at BC publication time is operational silence, not denial."
          category: source_reliability
          stated: false
          why_must_be_true: "If Oracle's silence were read as denial, the campaign-existence claim would weaken; the grading already treats it as silence-pending-response."
          when_could_be_false: "Oracle publishes a denial-class statement in the next 7 days reframing the campaign as low-impact or misattributed."
          evidence_for: []
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
          note: "Standard vendor-response-cycle pattern; brief should track Oracle response window as a 7-day tripwire."
        - id: A6
          statement: "ShinyHunters' leak site is functioning and accessible; Nottingham University data is genuinely posted there as BC reports."
          category: source_reliability
          stated: false
          why_must_be_true: "The single named-victim anchor depends on the leak-site claim being verifiable."
          when_could_be_false: "BC asserts leak-site posting without direct verification; per Hard Rule 1 considerations Archimedes does not directly access criminal leak sites."
          evidence_for: [bc-editorial-track-record-on-ransomware-leak-site-reporting]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: sound
          note: "BC has a strong track record on ransomware/extortion leak-site reporting; Archimedes' procedural-blocking on direct leak-site access is correct policy and does not impair confidence in the BC framing."
        - id: A7
          statement: "ShinyHunters' 'gadget chain of old and zero-day vulnerabilities' technical framing, despite the lack of specific CVE designations, describes a real exploit chain rather than a marketing abstraction."
          category: capability
          stated: false
          why_must_be_true: "Brief's actionability framing depends on a real exploit chain being the access vector; if the chain is marketing abstraction, defender response shifts toward generic posture rather than specific CVE-driven action."
          when_could_be_false: "Actor description is post-hoc marketing of unrelated initial-access (e.g., credentials, supplier compromise); the 'gadget chain' framing is reverse-engineered for press effect."
          evidence_for: [shinyhunters-prior-incidents-have-typically-involved-credentials-and-misconfigurations-rather-than-cve-chains]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
          note: "Brief should report 'actor describes gadget chain of old and zero-day vulnerabilities — no specific CVEs published' without endorsing the technical framing as confirmed."
        - id: A8
          statement: "The 300-instance / 100+-org scope, if approximately accurate, includes A&D-prime victims who have not yet been individually notified or disclosed."
          category: visibility
          stated: false
          why_must_be_true: "The brief's defender-actionability framing rests on the possibility that some A&D primes are exposed but not yet aware."
          when_could_be_false: "Actor's scope is inflated and the real victim count is much smaller (15-30 instances) — concentrated in education, healthcare, and small-government sectors per Nottingham University precedent — and A&D primes are not in the realized victim set."
          evidence_for: []
          evidence_against: [ach-ranking-h2-above-h1-suggests-scope-inflation-plausible]
          confidence: low
          centrality: material
          classification: qualify
          note: "Brief framing should be 'A&D-prime PeopleSoft instances are structurally in-scope for this attack pattern — defender-side configuration audit and IOC monitoring are appropriate even if no A&D prime is named in the BC primary' — explicitly NOT 'A&D primes are likely among the 100+ undisclosed victims.'"

      classifications_summary:
        sound: 2
        qualify: 4
        test: 1
        reject_or_qualify_heavily: 1

      remediation:
        status: proceed_with_qualifications_and_one_reject
        qualifying_caveats:
          - "Actor self-attested scope (300 instances / 100+ orgs) is reported verbatim as actor claim, NOT propagated as Archimedes-confirmed ground truth. ShinyHunters base-rate truthfulness on prior self-attested scope claims is currently uncalibrated in the Archimedes corpus — pending /new-actor profiling (A1)."
          - "A&D-prime structural relevance is via the HISTORICAL Oracle PeopleSoft deployment pattern; current 2026 density is heterogeneous and partially-migrated (Workday/HR, SAP/finance, Oracle Fusion/cloud). Brief should frame as 'historically deeply deployed' rather than 'all major primes have material footprint today' (A2)."
          - "REJECT or HEAVILY QUALIFY the escalation chain 'failed FBI attempt → A&D-prime federal-contractor co-scoping.' ACH refutation discipline ranks publicity-stunt (H2) above genuine attempt (H1). The escalation chain's predicate is unsupported (A3)."
          - "Splunk first-party silence on the 7 published IPv4 IOCs is reported as 'no internal exposure to those IOCs over -90d' — NOT propagated as a clean bill of health on broader PeopleSoft exposure. Operator-environment may be exposed via different vectors not captured in the published IOC set (A4)."
          - "Actor's 'gadget chain of old and zero-day vulnerabilities' technical framing is reported as actor claim; without specific CVE designations defender remediation is constrained to IOC monitoring + configuration hardening, NOT CVE-specific patching (A7)."
          - "300-instance scope, IF approximately accurate, has uncertain A&D-prime victim composition. Brief should frame A&D-prime exposure as 'structurally in-scope for the attack pattern' rather than 'likely victim of the campaign' (A8)."
        tests_required:
          - test_id: T1
            test: "/new-actor evaluation for ShinyHunters with retrospective base-rate calibration on AT&T 2024 / Microsoft / AWS self-attested-vs-confirmed scope ratios"
            unblocks: "A1 (actor self-attestation signal value); informs scope-claim WEP on all future ShinyHunters findings"
            priority: high
            blocks_publication: false
        next_action: "Publish in PM brief WITH the qualifying caveats above. Flag T1 for actor-profiler /new-actor follow-up. Do NOT block on T1 — brief is publishable as 'ShinyHunters self-attests Oracle PeopleSoft mass-data-theft campaign at unverified scope; 7 IPv4 + 1 domain IOCs operator-actionable; Splunk silent; A&D-prime structurally in-scope per ERP deployment pattern.' The failed-FBI-attempt claim should be explicitly framed as press-relations boast per ACH refutation discipline."

      recommended_wep_after_test:
        if_T1_confirms_shinyhunters_self_attestation_historically_accurate: "Hold scope-claim WEP at 'likely'; lift failed-FBI-attempt-layer to 'likely' if other supporting evidence emerges"
        if_T1_reveals_historical_2_5x_scope_inflation: "Reduce scope-claim WEP to 'unlikely' (actor self-attestation discounted); preserve campaign-existence and IOC-publication layers at 'likely'"
        if_T1_inconclusive: "Hold all current WEP layers as-is with qualify-language preserved"

# New-actor candidate referral
new_actor_candidate:
  actor_name: ShinyHunters
  candidacy_rationale: >
    Long-running extortion group active since approximately
    2020; prior major incidents (AT&T 2024, Microsoft, AWS);
    today's surface is mass-victim Oracle PeopleSoft campaign
    with 300-instance / 100+-org self-attested scope; published
    IOCs (7 IPv4 + 1 domain) operator-actionable for first-
    party hunt; Oracle PeopleSoft is widely deployed across
    A&D primes for HR / finance / supply chain — structural
    A&D-prime defender relevance even without named A&D victim;
    failed FBI PeopleSoft portal attempt indicates actor is
    actively scoping federal-class instances which implies
    A&D-prime federal-contractor PeopleSoft instances are
    also in scope.
  referral_action: "Operator /new-actor evaluation recommended"

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-10-afternoon]
retracted: false
retraction_brief_id: null
---

# Oracle PeopleSoft Mass-Data-Theft Campaign — ShinyHunters Self-Attests 300 Instances / 100+ Orgs; Nottingham University Named; 7 IPv4 + 1 Domain IOCs Published; Failed FBI Attempt Claimed; Splunk Silent

## Summary

ShinyHunters self-attested to BleepingComputer responsibility for an Oracle PeopleSoft mass-data-theft campaign claiming stolen data from 300 instances across more than 100 organizations, via a "gadget chain of old and zero-day vulnerabilities." Nottingham University is the only specifically named victim, with data published on the ShinyHunters leak site (education sector). The group also claimed an unsuccessful attempt to breach the FBI PeopleSoft portal — a notable failed-targeting data point. Oracle had not responded at BC publication time. Published IOCs include 7 IPv4 addresses and 1 TLS-certificate CN domain (`azurenetfiles[.]net`). Archimedes Splunk first-party hunt across both indices over -90d returned zero hits on all 7 IPv4 IOCs (silent, not disconfirming). ShinyHunters is NOT currently in the Archimedes roster — strong /new-actor candidate.

## Sources

### BleepingComputer (bleepingcomputer, B)

- URL: https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/
- Published: 2026-06-10T18:31:57 UTC
- Author: Lawrence Abrams
- Key claim: ShinyHunters self-attestation + scope + named victim + IOC publication + failed FBI attempt + Oracle silence.

## Technical detail

### Attribution

- **Actor:** ShinyHunters (long-running extortion group, active since approximately 2020; prior incidents AT&T 2024, Microsoft, AWS)
- **Attribution basis:** Actor self-attestation directly to BleepingComputer
- **Hard Rule 2 framing:** Self-attribution reported as fact-of-claim; preserved verbatim; not propagated as Archimedes-confirmed

### Scope (per actor self-attestation, single-source veto applied)

- "Stolen data from 300 instances across more than 100 organizations" (per BC, ShinyHunters self-attested)
- Named victim: **Nottingham University** (education sector); data published on leak site
- **No A&D / aerospace / defense / cleared contractor named in BC primary**

### Failed FBI targeting

- Per BC, ShinyHunters claimed an unsuccessful attempt to compromise the FBI's PeopleSoft portal — actor actively scoping federal-class PeopleSoft instances

### Technical mechanism

- "Gadget chain of old and zero-day vulnerabilities" (verbatim per BC) — **no specific CVE designations published**
- Attack success "variable depending on instance configuration"

### Oracle response

- Oracle had **not responded** at BC publication time
- No separate PeopleSoft-specific vendor statement

## IOCs surfaced

### IPv4 addresses (BC-published)

- 142.11.200.186
- 142.11.200.187
- 142.11.200.188
- 142.11.200.189
- 142.11.200.190
- 108.174.202.99
- 176.120.22.24

### Domain / TLS certificate (BC-published)

- `azurenetfiles[.]net` — TLS certificate CN linked to ShinyHunters infrastructure

### Splunk first-party hunt result

Per Hard Rule 8 first-party precedence: Splunk queried across `archimedes` and `defenseclaw_local` indices for all 7 published IPv4 IOCs over -90d window. **Result: zero hits.**

Interpretation per sat-ach discipline: absence-of-evidence is NOT evidence-of-absence. Silent Splunk on these IOCs is NOT disconfirming of external claim; consistent with no known internal exposure to date. First-party precedence applied as "no contradiction" rather than as "confirmation" or "disconfirmation."

## Relationship to existing findings

- **No direct prior finding tie-in** — first ShinyHunters surface in Archimedes corpus
- **Cross-corpus structural context:** Veeam CVE-2026-44963 (finding-2026-06-10-0010) backup-server-RCE primitive is structurally aligned with ransomware-staging methodology (though no actor attribution exists between Veeam advisory and any specific actor)

## Analytic notes (from analyst review)

The CAMPAIGN existence layer is robust — 7 published IPv4 + 1 TLS-cert domain IOC are technically specific and consistent with real campaign activity, and Nottingham University is a verifiable single named victim. The SCOPE layer (300 instances / 100+ orgs) and the FAILED-FBI-ATTEMPT layer are the weakened claims under refutation discipline. ACH ranks "publicity stunt — boast layered on a real campaign" above "genuine FBI targeting attempt" at zero versus one inconsistency. The diagnostic evidence is the absence of any technical artifact the actor could cite to substantiate a failed FBI attempt — a real failed probe would normally generate observable failure modes (specific instance URL, specific CVE chain attempted, specific detection or block signature) that the actor could deploy for credibility. The boast pattern fits the LockBit / BlackCat / Scattered Spider press-relations playbook precedent and costs the actor nothing because FBI can neither confirm nor deny.

The brief should preserve the actor's self-attestation verbatim and explicitly frame the failed-FBI-attempt claim as press-relations precedent rather than confirmed federal targeting. The escalation chain "failed FBI attempt → A&D-prime federal-contractor co-scoping" is REJECTED at its predicate — ACH refutation discipline does not support the genuine-attempt reading, so the downstream inference is unsupported. A&D-prime structural relevance is real but is via the historical Oracle PeopleSoft deployment pattern (heterogeneous and partially-migrated to Workday / SAP / Oracle Fusion since 2018), NOT via the failed-FBI-attempt logic. Splunk first-party silence on the 7 IOCs is reported as no internal exposure to those specific IOCs over -90d — explicitly NOT a clean bill of health on broader PeopleSoft exposure. The /new-actor evaluation should retrospectively calibrate ShinyHunters' base-rate truthfulness on AT&T 2024 / Microsoft / AWS prior self-attested scope claims to inform future scope-claim grading.

## Open questions for analyst

- **/new-actor evaluation:** ShinyHunters warrants /new-actor candidate review given (a) sustained multi-year mass-victim track record, (b) Oracle PeopleSoft structural A&D-prime ERP exposure, (c) federal-class targeting attempt against FBI, (d) leak-site monetization pattern, (e) operator-actionable published IOCs.
- **A&D-prime structural relevance:** Oracle PeopleSoft is deeply deployed across all major A&D primes for HR (clearance tracking, payroll), finance (program costing), and supply chain (vendor management, contract admin). Lockheed Martin, Boeing, Northrop Grumman, RTX, BAE Systems, L3Harris all have material PeopleSoft footprints. The 300-instance / 100-organization self-attested scope implies victims beyond Nottingham University; some may not yet be aware they are compromised. SAT-ACH: under hypotheses (a) actor scope claim is accurate ≥ 50, (b) actor scope claim is exaggerated ≥ 30% but real, (c) actor scope claim is largely fabricated.
- **Failed FBI attempt significance:** SAT-KAC consideration on assumption that failed-targeting reporting carries signal. What does the attempt tell defenders about ShinyHunters' federal-targeting calculus and whether A&D-prime federal-contractor PeopleSoft instances are co-scoped.
- **Configuration audit actionability:** "Attack success variable depending on instance configuration" — without specific CVE, defender remediation is constrained to (a) monitoring for the 7 IPv4 + 1 domain IOCs over -90d window, (b) reviewing PeopleSoft instance configuration hardening per Oracle baseline guidance (when published), (c) audit unusual data-egress patterns from PeopleSoft tier.
- **Hard Rule 2 preservation:** Nottingham University education-sector victim does NOT propagate to any A&D-prime victim framing. Structural deployment-pattern observation is operator-defender-actionable but not victim-attribution-equivalent.
