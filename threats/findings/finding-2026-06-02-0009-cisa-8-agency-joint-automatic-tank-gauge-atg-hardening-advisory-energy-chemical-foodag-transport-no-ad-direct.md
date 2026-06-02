---
finding_id: finding-2026-06-02-0009-cisa-8-agency-joint-automatic-tank-gauge-atg-hardening-advisory-energy-chemical-foodag-transport-no-ad-direct
created_at: 2026-06-02T16:32:00-04:00
graded_by: grader
grading_run_id: afternoon-20260602-160000
grading_mode: scheduled_brief
test: false
status: graded

# Core grading (admiralty-grading skill output)
digraph: A3
digraph_layered:
  cisa_plus_7_agency_joint_advisory_published_2026_06_02_on_atg_systems_hardening: A1                  # CISA self-canonical on its own publication; verifiable URL + timestamp
  eight_authoring_organizations_cisa_fbi_nsa_doe_epa_tsa_dot_usda: A1                                   # Verifiable in advisory text
  advisory_observes_malicious_cyber_activity_targeting_us_based_automatic_tank_gauge_systems: A3       # CISA self-canonical attestation but actor-class observation without specific attribution, no specific CVE referenced, no specific campaign named, no specific multi-victim attribution; underlying evidence basis not procedurally disclosed
  atg_systems_widely_deployed_across_energy_chemical_foodag_transportation_sectors: A1                  # Verifiable industry baseline; CISA-attested sector enumeration
  hardening_guidance_strong_passwords_remove_default_weak_credentials_network_segment: A1               # Verifiable in advisory text
  no_specific_cve_referenced: A1                                                                         # Verifiable absence
  no_threat_actor_named: A1                                                                              # Verifiable absence
  no_multi_victim_campaign_attribution: A1                                                               # Verifiable absence
  no_ad_dib_sector_mentioned_no_aerospace_defense_yaml_watchlist_entity_named: A1                       # Verifiable absence
  no_specific_atg_vendor_named: A1                                                                       # Verifiable absence (Veeder-Root / OPW / Franklin Fueling / Gilbarco common vendors NOT singled out)
  no_cisa_kev_addition_concurrent_for_any_atg_vendor_product_cve: A1                                    # Verifiable internal corpus state
  eight_agency_joint_authoring_count_unusually_heavy: B3                                                # Grader-side qualitative observation; benchmark against CISA's historical joint-authoring counts not formally retrieved this sweep
  historical_precedent_similar_joint_advisories_preceded_campaign_attribution_disclosures_30_90_days: C2  # Grader-side structural inference (e.g., Iran-OT-targeting joint advisories 2023-2025 preceding CyberAv3ngers attribution); pattern not formally validated against base-rate analysis
  ad_relevance_indirect_via_military_dod_fuel_storage_estates_jet_fuel_motor_pool_strategic_reserve: C2  # Grader-side structural inference; TSA + DOT + DOE joint authoring suggests national-fuel-infrastructure scope with possible DIB fuel-vendor partner-flow inheritance
  cluster_anchor: A3

digraph_anchor: >
  Cluster anchored on CISA-led 8-agency joint advisory (CISA + FBI +
  NSA + DOE + EPA + TSA + DOT + USDA) published 2026-06-02 at 12:00
  UTC = 08:00 EDT (in-window, exact start of pre-brief window) on
  hardening Automatic Tank Gauge (ATG) systems against observed
  malicious cyber activity targeting US-based ATG deployments.

  A3 (not A2 or A1) anchored because:
    - CISA grade A is ratified canonical authority on government
      advisory publication; the 8-agency joint authoring is
      procedurally A1 (publication exists, sectors enumerated,
      hardening guidance attested).
    - The OPERATIONAL CLAIM ("malicious cyber activity targeting
      U.S.-based automatic tank gauge systems") is sub-graded A3
      (Possibly True) rather than A2 (Probably True) because:
        (a) CISA's attestation is single-source on the operational
            observation;
        (b) Underlying evidence basis (telemetry, IR findings, case
            file) is NOT procedurally disclosed with the advisory
            (consistent with CISA's typical sector-hardening-advisory
            publication pattern, but differs from CISA's
            campaign-attribution publications which include more
            substantive case-file content);
        (c) Actor-class observation without specific attribution,
            no specific CVE referenced, no specific campaign named,
            no specific multi-victim attribution — the "malicious
            cyber activity" framing is the lowest-specificity-class
            CISA publication tier;
        (d) Single-source veto applies — no third-party A/B-grade IR
            firm corroboration of THIS specific ATG-targeting
            observation at sweep time (Dragos / Claroty / Nozomi /
            Industrial Cyber / SCADAfence have not published
            independent ATG-targeting telemetry at sweep);
        (e) Without specific CVE / actor / victim / vendor identification,
            the operational claim cannot internally cohere beyond
            "Possibly True" — coherence requires at least some
            specific attestation that allows independent verification.
    - The PROCEDURAL FACTS layer (publication exists, 8-agency
      authoring, sector enumeration, hardening guidance text) is
      cleanly A1 — verifiable against the CISA resource page.
    - The 8-AGENCY JOINT AUTHORING COUNT layer is qualitatively
      graded B3 — one of the heavier joint-authoring counts CISA
      publishes for sector-specific guidance, but benchmark against
      CISA's full historical joint-authoring counts not formally
      retrieved this sweep.
    - The A&D RELEVANCE layer is grader-side structural inference
      C2 — military / DoD fuel-storage estates deploy ATG systems
      for jet-fuel / motor-pool / strategic-reserve tank monitoring;
      TSA + DOT + DOE joint authoring suggests national-fuel-
      infrastructure operational concern with possible DIB
      fuel-vendor partner-flow inheritance, but the advisory's
      named sectors (Energy, Chemical, Food&Ag, Transportation)
      do NOT include A&D / DIB, and no A&D-prime watchlist entity
      is named.

  Single-source veto applied on operational claim layer: WEP ceiling
  on the active ATG-targeting trajectory and any predictive claims
  about ATG-targeting actors capped at "likely" pending independent
  A/B-grade IR firm corroboration or follow-on CISA campaign-
  attribution publication.

  Per Hard Rule 2: CISA observes "malicious cyber activity"
  generically without naming any specific actor. Archimedes preserves
  zero attribution. The Linux container-escape class has been
  historically exercised by Kinsing / TeamTNT cryptojacking and the
  ATG-targeting class has been historically exercised by CyberAv3ngers
  per pre-Archimedes vendor reporting, but CISA does NOT name those
  actors on THIS advisory; Archimedes does NOT extend the historical
  actor association into a new attribution. Pattern-match commentary
  on the CyberAv3ngers historical precedent is preserved at
  pattern-class only, NOT as Archimedes attribution.

  Per Hard Rule 3: NO exploit / PoC content. Advisory is defensive
  hardening guidance only (strong passwords, default-credential
  removal, network segmentation).

  Per Hard Rule 8: Splunk first-party check ran (-30d sweep on
  "ATG" + "automatic tank gauge" across defenseclaw_local +
  archimedes NOT sourcetype=archimedes:*). 0 events. First-party
  silence preserved as a data point per the 19+-day non-archimedes-
  internal silent stream pattern, not disconfirming. ATG systems
  not in defenseclaw_local target environment, so silence is
  consistent with environmental baseline.

source_reliability:
  primary_anchor:
    grade: A
    source_name: CISA joint advisory with FBI, NSA, DOE, EPA, TSA, DOT, USDA - Hardening Automatic Tank Gauge (ATG) Systems
    source_yaml_id: cisa-advisories
    grade_rationale: >
      Pre-assigned A per source-grades.yaml. CISA-led 8-agency joint
      advisory; government-body authority on critical-infrastructure
      protection guidance. CISA is the publishing organization;
      co-authoring agencies (FBI, NSA, DOE, EPA, TSA, DOT, USDA)
      add multi-agency-consensus weight without changing the
      publication-source authority.
    provisional: false

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_but_source_is_b_grade_or_better   # CISA A-grade sole primary on operational ATG-targeting observation; no independent A/B IR firm corroboration at sweep
    - possibly_true_partially_consistent_with_known_ttps_but_some_elements_novel   # Historical CyberAv3ngers OT-targeting pattern provides class-context but THIS specific observation lacks actor / CVE / vendor / victim specificity
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable    # ATG-targeting class is plausible (well-documented OT attack surface; default-credential prevalence in ICS); but without specific actor / CVE / vendor, independent verification is not possible at sweep
  rationale: >
    Grade 1 (Confirmed) FAILS — single-source on operational claim;
    no independent A/B IR firm corroboration. Grade 2 (Probably True)
    FAILS — checklist condition "technical claims internally coherent"
    fails when no specific CVE / actor / vendor / victim is identified;
    the operational claim is too generic to internally cohere beyond
    "Possibly True." Grade 3 (Possibly True) PASSES: ALL of single-
    source-B-or-better-uncorroborated + partially-consistent-with-
    known-TTPs + technical-claims-plausible-but-not-independently-
    verifiable conditions met.

corroboration:
  independent_sources:
    - cisa-advisories                        # primary; co-authoring agencies FBI, NSA, DOE, EPA, TSA, DOT, USDA are multi-agency-consensus weight not independent corroboration
  non_independent_relays: []
  independent: false
  test_failed: >
    CISA is the sole primary; co-authoring 7-agency consensus is
    multi-agency-consensus weight on the publication-source side
    but does NOT constitute independent corroboration on the
    operational substance (the 7 co-authoring agencies do not
    publish independent advisories with separate evidence bases on
    THIS specific ATG-targeting observation). No third-party A/B-grade
    IR firm corroboration (Dragos / Claroty / Nozomi / Industrial
    Cyber / SCADAfence have not published independent ATG-targeting
    telemetry at sweep time). Per independence test on the
    operational claim: fails.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_check_performed: true
  splunk_check_window: "-30d, index=defenseclaw_local OR index=archimedes (ATG OR \"automatic tank gauge\") NOT sourcetype=archimedes:operation NOT sourcetype=archimedes:scheduler"
  splunk_check_result: "0 events — first-party telemetry silent on ATG indicators. ATG systems not in defenseclaw_local target environment (A&D-prime IT/OT estate does not typically include ATG fuel-storage tank monitoring as primary infrastructure), so silence is consistent with environmental baseline. Silence is not disconfirming per Hard Rule 8."

single_source_veto_applied: true
single_source_veto_rationale: >
  CISA is the sole primary on the operational claim. Co-authoring
  agencies are multi-agency-consensus weight on publication source
  but not independent corroboration on operational substance. No
  third-party A/B-grade IR firm corroboration of THIS specific
  ATG-targeting observation at sweep. WEP ceiling on operational
  ATG-targeting trajectory and any predictive claims capped at
  "likely" per single-source-veto rule. (Note: A3 digraph already
  caps WEP below "very likely" per WEP-ceiling table; veto is
  procedurally documented for consistency.)

wep_ceiling: likely

inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    # NOT daily_brief_action — A3 falls below B2 floor for action items; A&D direct relevance absent (named sectors are Energy, Chemical, Food&Ag, Transportation, not A&D / DIB)
    # NOT flash — collector evaluated all 6 FLASH triggers as FAIL (Trigger 5 fails on A&D-not-named); A3 falls below B2 floor anyway
    # NOT actor_profile_update — no actor named
  inclusion_threshold_test:
    flash_b2_minimum: fail_a3_below_b2_floor                              # A3 fails B2 minimum on credibility-number axis
    daily_brief_action_b2_minimum: fail_a3_below_b2_floor                  # A3 fails B2 minimum
    daily_brief_monitoring_c3_minimum: pass                                # A3 clears C3 floor (A>C and 3=3 monitoring threshold)
    weekly_synthesis_c3_minimum: pass                                      # A3 clears C3 floor
    actor_profile_update_b2_minimum: fail_a3_below_b2_floor_and_no_actor_named

# Cluster metadata
cluster:
  topic: "CISA-led 8-agency joint advisory on hardening Automatic Tank Gauge (ATG) systems against malicious cyber activity targeting US-based ATG deployments in Energy, Chemical, Food&Ag, and Transportation sectors; no specific actor / CVE / vendor / victim named; A&D not in named sectors; sector-intelligence carry-context"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-02-pm-005-cisa-7-agency-joint-automatic-tank-gauge-atg-hardening-energy-transportation-critical-infra
  attribution_claims: []   # CISA observes "malicious cyber activity" generically without naming any specific actor

# Downstream handoff flags
analyst_review_required: false
analyst_review_reasons:
  - wep_ceiling_likely_with_no_actor_attributed_no_cve_no_vendor_no_victim_does_not_warrant_sat_ach_or_sat_kac_at_this_specificity_class
red_team_review_required: false
red_team_review_reasons:
  - wep_ceiling_likely_below_very_likely_threshold_per_hard_rule_red_team_invocation_floor
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-02-afternoon]
retracted: false
retraction_brief_id: null

# Operator handoffs
operator_handoffs:
  - handoff_type: actor_profiler_awareness
    target: future_atg_targeting_actor_attribution_disclosures
    rationale: Historical precedent — similar joint advisories have preceded campaign-attribution disclosures by 30-90 days (e.g., Iran-OT-targeting joint advisories 2023-2025 preceded CyberAv3ngers attribution); actor-profiler should monitor for follow-on attribution publications from CISA / FBI / DOE within the next 30-90 day forward window
    target_audience: actor-profiler
  - handoff_type: vuln_tracker_awareness
    target: future_atg_vendor_cve_kev_additions
    rationale: Vuln-tracker should monitor for ATG-vendor (Veeder-Root / OPW / Franklin Fueling / Gilbarco) CVE additions to KEV in the 30-90 day forward window; 8-agency joint authoring is the elevated-signal indicator
    target_audience: vuln-tracker
  - handoff_type: briefer_sector_intel_note
    target: pm_brief_other_signal_or_sector_focus_section
    rationale: 8-agency joint authoring is the newsworthy signal even absent specific A&D-prime relevance; brief inclusion at monitoring tier (one-paragraph treatment) for sector-intelligence carry-context; not action-item tier given A3 credibility-number ceiling and A&D-direct absence
    target_audience: briefer
---

# CISA 8-Agency Joint Advisory — Hardening Automatic Tank Gauge (ATG) Systems Against Observed Malicious Cyber Activity; Energy / Chemical / Food&Ag / Transportation Sectors Named; A&D Not Named

## Summary

CISA, FBI, NSA, DOE, EPA, TSA, DOT, and USDA jointly published a hardening advisory on 2026-06-02 at 08:00 EDT (in-window at the absolute start of the pre-brief window) for Automatic Tank Gauge (ATG) systems, observing "malicious cyber activity targeting U.S.-based automatic tank gauge systems" across Energy, Chemical, Food and Agriculture, and Transportation sectors. Eight-agency joint authoring is one of the heavier joint-authoring counts CISA publishes for sector-specific guidance. CISA names no specific actor, CVE, ATG vendor, or victim, and the advisory carries no concurrent CISA KEV addition for any ATG-vendor-product CVE. A&D / DIB is NOT in the named sector set, and no aerospace-defense.yaml watchlist entity is named. A&D-prime relevance is indirect via military / DoD fuel-storage estates deploying ATG for jet-fuel / motor-pool / strategic-reserve tank monitoring, but the advisory text does not reference these. Sector-intelligence carry-context only; monitoring-tier brief inclusion appropriate.

## Sources

### CISA + 7-agency joint advisory (cisa-advisories, digraph A)

- URL: https://www.cisa.gov/resources-tools/resources/cisa-and-partners-urge-hardening-automatic-tank-gauge-systems
- Published: 2026-06-02 at 12:00 UTC = 08:00 EDT (in-window)
- Co-authoring agencies: CISA, FBI, NSA, DOE, EPA, TSA, DOT, USDA
- Key claim: Observes malicious cyber activity targeting US-based ATG systems; recommends strong-password / default-credential-removal / network-segmentation hardening; sector enumeration covers Energy, Chemical, Food&Ag, Transportation

## Technical detail

Automatic Tank Gauge (ATG) systems automate remote monitoring of storage tank parameters including fuel levels, liquid levels, temperature, and leak detection. Widely deployed across:

- Energy Sector (fuel storage tank monitoring)
- Chemical Sector (storage tank parameters, leak detection)
- Food and Agriculture Sector (agricultural / industrial liquid storage)
- Transportation Systems Sector (transport-fuel infrastructure)

Hardening guidance per advisory:
- Secure ATG systems with strong passwords
- Remove default / weak / vendor-default credentials
- (Implicit) Network-segment ATG management interfaces away from internet-accessible exposure

What's NOT in the advisory:
- No specific CVE referenced
- No threat actor named
- No multi-victim campaign attribution
- No A&D / DIB sector mentioned
- No specific ATG vendor named (Veeder-Root / OPW / Franklin Fueling / Gilbarco common ATG vendors NOT singled out)
- No CISA KEV addition concurrent for any ATG-vendor-product CVE

## IOCs surfaced

None applicable. Operational-hardening guidance is mechanism-class, not infrastructure.

## Relationship to existing findings

No prior Archimedes-corpus ATG-targeting coverage; net-new sector-intel topic. Historical pattern precedent (grader-side structural inference, C2): similar joint advisories have preceded campaign-attribution disclosures by 30-90 days (e.g., Iran-OT-targeting joint advisories 2023-2025 preceded CyberAv3ngers attribution). Monitor for follow-on campaign-attribution publications from CISA / FBI / DOE within the 30-90 day forward window.

## Open questions for analyst

None at this finding's specificity class. WEP "likely" with no actor attributed, no CVE referenced, no vendor named, and no victim identified does not warrant SAT-ACH or SAT-KAC at this surface. Re-evaluate on follow-on CISA campaign-attribution publication or independent A/B IR firm corroboration.
