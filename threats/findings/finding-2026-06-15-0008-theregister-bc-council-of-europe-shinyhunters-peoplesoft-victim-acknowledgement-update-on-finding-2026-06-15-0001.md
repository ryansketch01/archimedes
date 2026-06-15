---
id: finding-2026-06-15-0008
finding_id: finding-2026-06-15-0008-theregister-bc-council-of-europe-shinyhunters-peoplesoft-victim-acknowledgement-update-on-finding-2026-06-15-0001
title: "UPDATE on finding-2026-06-15-0001 — The Register (cyber-crime desk) + BleepingComputer (Sergiu Gatlan) dual-publisher relays obtain Council of Europe direct victim acknowledgement ('currently investigating the matter and assessing the situation') resolving the morning brief's no-CoE-ACK weakness; ShinyHunters self-claim now linked to Oracle PeopleSoft CVE-2026-35273 vector explicitly per The Register (ShinyHunters spokesperson statement); CoE-ACK procedural-fact layer lifts C3 → B2; underlying 297 GB / 429K files quantified-volume claim remains C3 (Council of Europe has NOT confirmed scope numbers — only confirmed an investigation is ongoing); GTIG carry-forward cross-corroboration on CVE-2026-35273 mass-exploitation (May 27 - June 9, >100 orgs notified, 68% higher-ed sector) re-stated but no NET-NEW substrate vs finding-2026-06-13-0006; UNC6240/ShinyHunters identity chain remains Mandiant-attributed (Hard Rule 2 binding preserved — Archimedes does NOT originate the UNC6240↔ShinyHunters mapping; neither actor on _roster.yaml); NO US A&D-prime / DIB intersection (CoE is 46-state intergovernmental human-rights body); ed-tech cluster context (Canvas/Infinite Campus/Nottingham) all carry-forward anti-noise from prior surfaces; FCEB BOD 26-04 KEV deadline EOD TONIGHT 2026-06-15 for CVE-2026-35273 — this finding lands T-7h before deadline closure; 11th-consecutive Splunk first-party sentinel CLEAN on the 19-IOC PeopleSoft/UNC6240 set per Hard Rule 8 binding"
date: 2026-06-15
created_at: 2026-06-15T16:22:00-04:00
graded_by: grader
grading_run_id: afternoon-20260615-160000
grading_mode: scheduled_brief
test: false
status: graded
update_type: layered_update
updates_finding: finding-2026-06-15-0001-securityweek-shinyhunters-council-of-europe-leak-site-claim-297gb-dual-campaign-actor-visibility

# ============================================================================
# Core grading (admiralty-grading skill output) — UPDATE LAYER
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- COUNCIL OF EUROPE DIRECT ACK LAYER (NET-NEW vs finding-0001) ----
  council_of_europe_spokesperson_direct_statement_to_the_register_currently_investigating: A1  # Verifiable verbatim — 11-word quote ("currently investigating the matter and assessing the situation") + "declined to comment further" framing
  coe_ack_resolves_morning_brief_finding_0001_no_coe_ack_weakness: A1  # Procedural — verifiable per finding-0001 C3-anchor weakness enumeration
  procedural_fact_of_coe_investigation_now_corroborated_by_victim_organization_itself: B2  # Victim-organization ACK at the procedural-fact layer (investigation occurring); does NOT corroborate substantive scope claims
  # ---- CVE-2026-35273 VECTOR LINKAGE LAYER (NET-NEW vs finding-0001) ----
  shinyhunters_spokesperson_to_the_register_explicitly_links_coe_to_peoplesoft_zero_day: B2  # The Register direct attribution to ShinyHunters spokesperson — actor-self-claim layer linking CoE to CVE-2026-35273; previously finding-0001 noted SW explicitly framed campaigns as SEPARATE
  cve_2026_35273_oracle_peoplesoft_vector_now_self_claimed_by_shinyhunters_for_coe: B2  # Actor-self-claim — methodologically C3 for substantive volume claims but procedural-fact of self-claim is B2
  # ---- DUAL-PUBLISHER LAYER (NET-NEW vs finding-0001's single SecurityWeek substrate) ----
  the_register_cyber_crime_desk_iain_thomson_byline_customary_for_class: B2  # The Register ratified B per source-grades.yaml; byline named in raw-signal extraction (customary attribution for this story class)
  bleepingcomputer_sergiu_gatlan_independent_publisher_relay_same_day: B2  # BleepingComputer ratified B per source-grades.yaml; same-day independent relay
  dual_publisher_independence_test_passes_at_publisher_layer: A2  # Two B-grade publishers with different bylines on same day — publisher-side independence achieved; both directly retrieved ShinyHunters claim + CoE response
  # ---- SCOPE / VOLUME CLAIM LAYER (CARRY-FORWARD FROM finding-0001 — UNCHANGED) ----
  claimed_volume_297gb_429k_files_remains_C3_actor_self_claim_layer: C3  # CoE confirmed investigation but did NOT confirm scope numbers; single-source actor-self-claim through B-publisher relay
  data_scope_payroll_hr_medical_records_cvs_remains_C3_actor_self_claim_layer: C3  # Same — actor self-claim layer unchanged
  threatened_release_deadline_2026_06_16_carry_forward_from_finding_0001: B2  # SW + The Register + BC all attest leak-site posting; verifiable
  # ---- GTIG CROSS-CORROBORATION LAYER (CARRY-FORWARD — re-stated, not net-new) ----
  gtig_mandiant_late_week_report_cited_by_the_register_re_states_finding_2026_06_13_0006_substrate: A2  # GTIG report is carry-forward primary from finding-2026-06-13-0006 — The Register re-relays without new evidence basis
  malicious_activity_consistent_with_cve_2026_35273_exploitation_may_27_to_june_9_carry_forward: A2  # Restatement of GTIG primary observation at lower source-fidelity (via The Register relay vs direct Mandiant retrieval)
  100_global_orgs_notified_carry_forward_from_gtig_via_the_register_relay: A2  # Restatement
  68_percent_higher_ed_sector_carry_forward_from_gtig_via_the_register_relay: A2  # Restatement — most US-based, 68% higher-ed
  no_new_gtig_substrate_via_the_register_relay_this_sweep: A1  # Verifiable absence — The Register re-cites without new GTIG content
  # ---- UNC6240 ↔ SHINYHUNTERS IDENTITY CHAIN LAYER (HARD RULE 2 BINDING — CARRY-FORWARD) ----
  unc6240_mandiant_attribution_carry_forward_from_finding_0006: A2  # Mandiant primary canonical
  shinyhunters_extortion_brand_self_claim_layer_carry_forward: A2  # ShinyHunters leak-site self-claim is canonical for the brand-self-attribution layer
  unc6240_shinyhunters_dual_naming_chain_per_mandiant_primary_substrate_NOT_originated_by_archimedes: A1  # Hard Rule 2 binding preserved
  unc6240_NOT_on_archimedes_roster_carry_forward: A1  # Verifiable per roster check
  shinyhunters_NOT_on_archimedes_roster_carry_forward: A1  # Verifiable per roster check
  no_archimedes_originated_mapping_of_unc6240_to_shinyhunters: A1  # Hard Rule 2 binding preserved
  # ---- DUAL-CAMPAIGN ACTOR VISIBILITY LAYER (UPDATED FROM finding-0001) ----
  finding_0001_initial_framing_separate_campaigns_SUPERSEDED_by_shinyhunters_self_claim_of_cve_2026_35273_for_coe: A1  # Verifiable — finding-0001 noted SW framed CoE and PeopleSoft as separate; The Register surfaces ShinyHunters explicitly claiming CVE-2026-35273 for CoE
  dual_campaign_visibility_partially_collapses_to_single_campaign_visibility_at_ShinyHunters_brand_layer: B2  # The Register attribution to ShinyHunters spokesperson; methodologically actor-self-claim layer; does NOT independently verify the CVE-2026-35273 vector for CoE
  # ---- ED-TECH CLUSTER CONTEXT LAYER (ALL CARRY-FORWARD ANTI-NOISE) ----
  instructure_canvas_275m_records_mid_may_2026_paid_carry_forward: B2  # The Register restatement; prior surface
  infinite_campus_137k_records_march_2026_did_not_pay_carry_forward: B2  # The Register restatement; same item as today's BC 12:38 piece per pre-flash sentinel
  university_of_nottingham_454600_records_last_week_carry_forward: B2  # The Register restatement
  ed_tech_cluster_pattern_recognition_not_net_new_substrate_this_sweep: A1  # Verifiable — all ed-tech items carry-forward
  # ---- FCEB BOD 26-04 KEV DEADLINE LAYER (CARRY-FORWARD — CRITICAL TIMING) ----
  cve_2026_35273_fceb_bod_26_04_deadline_eod_tonight_2026_06_15_T_minus_approximately_7_hours: A1  # Verifiable per CISA KEV catalog + finding-2026-06-12-0001 / 0006 carry-forward
  oracle_out_of_band_mitigations_only_no_ga_patch_carry_forward: A1  # Verifiable per finding-2026-06-13-0006 substrate
  this_finding_lands_T_minus_7h_before_deadline_closure: A1  # Verifiable timing — 16:00 EDT publication, deadline EOD same day
  # ---- A&D / DIB RELEVANCE LAYER (UNCHANGED FROM finding-0001) ----
  ad_direct_relevance: A1  # NONE — verifiable; CoE is 46-state intergovernmental human-rights body
  no_ad_dib_aerospace_defense_intersection_carry_forward: A1  # Verifiable structural absence
  edqm_pharma_regulatory_adjacent_NOT_ad_carry_forward: B2  # Carry-forward from finding-0001
  # ---- FIRST-PARTY SPLUNK LAYER (HARD RULE 8 BINDING — CARRY-FORWARD) ----
  splunk_first_party_check_19_ioc_peoplesoft_unc6240_sentinel_set_clean_for_11_consecutive_sweeps: A1  # Carry-forward per FLASH 12:00 commit c48f6fc substrate; this finding rides on standing 19-IOC sentinel-set check
  frank_not_higher_ed_environment_visibility_bounded_absence_carry_forward: A1  # Hard Rule 8 binding — silent Splunk does NOT disconfirm; Frank is not 68% UNC6240 victim profile
  # ---- IOC LAYER ----
  no_new_iocs_disclosed_in_the_register_or_bc_relays_this_sweep: A1  # Verifiable absence
  carry_forward_19_ioc_set_standing_unchanged_finding_0006: A2  # Carry-forward
  # ---- ANTI-NOISE DISPOSITION LAYER ----
  net_new_substrate_coe_ack_layer_only: A1  # Verifiable per pre-flash sentinel sweep audit
  cve_2026_35273_mechanism_anti_noise_preserved_carry_forward_finding_0006: A1  # Verifiable — substrate update on CoE-ACK layer only; CVE substrate locked
  gtig_scale_claims_anti_noise_preserved_carry_forward_finding_0006: A1  # Verifiable — re-citation only
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / action-tier inclusion) on
  layered UPDATE pathway over finding-2026-06-15-0001. The Register
  (cyber-crime desk, customary Iain Thomson byline) + BleepingComputer
  (Sergiu Gatlan byline) dual-publisher relays — both ratified B per
  source-grades.yaml — converge on Council of Europe direct victim
  acknowledgement at 2026-06-15. CoE spokesperson statement to The
  Register is 11-word verbatim quote ("currently investigating the
  matter and assessing the situation") plus "declined to comment
  further" framing.

  The CoE-ACK substrate is the binding net-new layer this update,
  resolving the no-CoE-ACK weakness that anchored finding-0001 at C3.
  Victim-organization direct acknowledgement of an active investigation
  is procedurally A1 at the fact-of-investigation layer, but does
  NOT corroborate substantive scope claims (297 GB / 429K files /
  payroll-HR-medical scope) — CoE explicitly "declined to comment
  further."

  CVE-2026-35273 VECTOR LINKAGE NET-NEW: finding-0001 noted SecurityWeek
  framed the CoE breach and Oracle PeopleSoft campaign as SEPARATE.
  The Register UPDATE surfaces a ShinyHunters spokesperson explicitly
  claiming the CoE compromise was via the same Oracle PeopleSoft
  zero-day. This is actor-self-claim layer — methodologically C3 for
  the substantive vector claim, but procedurally B2 on the fact of
  ShinyHunters claiming the vector. Note this is NOT independently
  verified — CoE has NOT confirmed the vector, only confirmed an
  investigation is ongoing.

  WHY B2 NOT B1:
    1. CoE ACK is at INVESTIGATION-LAYER ONLY. Victim ack confirms
       an investigation is ongoing; does NOT corroborate the
       quantified-volume scope claim or the CVE-2026-35273 vector
       claim.
    2. Scope claims (297 GB / 429K files / payroll-HR-medical)
       remain ACTOR SELF-CLAIM through B-publisher relay — C3
       layer carry-forward from finding-0001.
    3. GTIG substrate is RE-CITED via The Register, not new
       evidence basis — primary GTIG content was anchored in
       finding-2026-06-13-0006.

  WHY ACTION-TIER INCLUSION:
    1. Substrate update from C3 → B2 on the procedural-fact layer
       (CoE ACK obtained, ShinyHunters explicitly self-claims
       CVE-2026-35273 vector) is operationally meaningful — these
       are NET-NEW substrate vs morning brief finding-0001.
    2. Dual-publisher independent relay convergence (The Register +
       BleepingComputer) lifts publisher-side independence vs
       finding-0001's single SecurityWeek substrate.
    3. CVE-2026-35273 FCEB BOD 26-04 deadline EOD TONIGHT
       2026-06-15 (T-minus ~7h from this finding publication);
       afternoon brief is the FINAL pre-deadline coverage window.
    4. Hard Rule 5 binding preserved: UNC6240/ShinyHunters
       operator-deferred /new-actor candidacy substrate continues
       strengthening (third campaign in visible ShinyHunters
       portfolio this week — CoE / Oracle PeopleSoft / Tchap-
       adjacent / DentaQuest).

  WHAT THE B2 ATTESTS:
    (a) Council of Europe spokesperson directly told The Register
        the CoE is "currently investigating the matter and
        assessing the situation" (verbatim 11-word quote;
        Hard Rule 6 preserved).
    (b) CoE "declined to comment further" — victim ACK at the
        investigation-layer only, no substantive scope or vector
        confirmation.
    (c) ShinyHunters spokesperson explicitly claimed to The
        Register that the CoE compromise was via the Oracle
        PeopleSoft zero-day (CVE-2026-35273) — actor self-claim
        layer linking CoE to the same campaign vector as
        finding-2026-06-13-0006 substrate.
    (d) Two B-grade publishers (The Register + BleepingComputer)
        independently surfaced both the CoE ACK and ShinyHunters
        attribution claims at publisher-relay layer.
    (e) GTIG late-week report substrate (May 27 - June 9 mass
        exploitation, >100 orgs notified, 68% higher-ed sector)
        is re-cited via The Register without new GTIG evidence
        basis — carry-forward from finding-2026-06-13-0006.

  WHAT THE B2 DOES NOT ATTEST:
    - CoE scope confirmation (297 GB / 429K files / payroll-HR-
      medical / EDQM departments) — CoE "declined to comment
      further"; scope claims remain ShinyHunters self-claim C3
      layer.
    - CoE confirmation of CVE-2026-35273 vector — only ShinyHunters
      has claimed this; CoE has NOT confirmed the vector.
    - Any nation-state attribution (no PLA / MSS / Iranian / North
      Korean / Russian intelligence-services language at any source).
    - Net-new IOCs (no hashes / IPs / domains beyond carry-forward
      19-IOC standing sentinel set).
    - First-party Frank-environment telemetry confirmation (Frank
      is not higher-ed sector consistent with 68% UNC6240 victim
      profile; standing 11-consecutive-sweep clean sentinel
      continues per Hard Rule 8 binding visibility-bounded
      absence).
    - Whether the dual-campaign-actor-visibility framing from
      finding-0001 fully collapses to single-campaign visibility
      — only ShinyHunters has claimed the linkage; vector
      independently unverified.

  HARD RULE 2 binding constraint: PRESERVED.
    - UNC6240↔ShinyHunters dual-naming chain remains
      Mandiant-primary-attributed (carry-forward from finding-
      2026-06-13-0006); Archimedes does NOT originate this
      mapping.
    - Neither UNC6240 nor ShinyHunters on Archimedes 24-actor
      `_roster.yaml` (operator-deferred /new-actor candidacy
      substrate-strengthening per Hard Rule 5).
    - No nation-state attribution originated by Archimedes.

  HARD RULE 6 binding constraint: PRESERVED.
    - CoE spokesperson quote: "currently investigating the matter
      and assessing the situation" (11 words — under 15-word cap;
      one quote per source).

  HARD RULE 8 binding constraint: PRESERVED.
    - Standing 19-IOC PeopleSoft/UNC6240 sentinel-set continues
      11th consecutive clean sweep across defenseclaw_local +
      archimedes per FLASH 12:00 commit substrate.
    - Frank NOT higher-ed environment (68% UNC6240 victim profile);
      silent-Splunk-does-NOT-disconfirm — visibility-bounded
      absence flagged, NOT treated as negative evidence.

source_reliability:
  grade: B
  source_name: "The Register (cyber-crime desk) + BleepingComputer (Sergiu Gatlan) dual-publisher relays of ShinyHunters self-claim + Council of Europe direct ACK"
  source_yaml_id: theregister + bleepingcomputer
  grade_rationale: >
    Two ratified B-grade publishers (per source-grades.yaml).
    Publisher-side independence achieved with same-day dual relay.
    Underlying substrate is actor self-claim (ShinyHunters) +
    direct victim ACK (Council of Europe spokesperson) — different
    evidence-basis layers within the same surface.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - consistent_with_established_shinyhunters_tradecraft_pattern_per_corpus_substrate_finding_0001_finding_0006
    - no_contradicting_evidence_from_a_or_b_grade_sources
    - technical_claims_internally_coherent_with_carry_forward_substrate
  rationale: >
    The Register + BleepingComputer dual-publisher relays converge
    on CoE ACK + ShinyHunters self-claim. Consistent with
    established ShinyHunters / UNC6240 PeopleSoft campaign
    substrate from finding-2026-06-13-0006 (Mandiant primary).
    No contradicting evidence in window. Technical claims (CVE
    vector self-claim) are internally coherent but NOT
    independently verified — CoE confirmed investigation only,
    did NOT confirm vector or scope.

corroboration:
  independent_sources:
    - theregister
    - bleepingcomputer
    - council-of-europe-spokesperson-direct  # victim-organization direct ACK
    - mandiant-gtig  # carry-forward primary via finding-2026-06-13-0006
  independent: true
  test_passed: >
    Publisher-side independence: The Register + BleepingComputer
    are two different B-grade publishers with different bylines
    surfacing the CoE ACK + ShinyHunters self-claim same day.
    Evidence-basis independence: CoE spokesperson direct ACK is
    independent evidence basis vs ShinyHunters Tor leak-site
    self-claim (victim-side vs actor-side); GTIG carry-forward
    primary (finding-0006) is third independent evidence basis on
    the broader CVE-2026-35273 campaign substrate. Multi-layered
    corroboration achieved across publisher + victim + actor +
    third-party-IR substrates.
  independent_layered:
    coe_spokesperson_direct_ack: true   # Victim-organization direct evidence basis
    shinyhunters_self_claim_via_publishers: false   # Actor self-claim layer (single evidence basis)
    gtig_mandiant_carry_forward: true   # Third-party IR-firm primary (carry-forward from finding-0006)
    publisher_side_independence_thereg_plus_bc: true   # Two-publisher publisher-side independence

first_party_precedence:
  applied: true
  splunk_evidence:
    query_executed: "standing 19-IOC PeopleSoft/UNC6240 sentinel-set check per FLASH 12:00 commit c48f6fc substrate (carry-forward)"
    hits_on_external_indicators: 0
    consecutive_clean_sweeps: 11
    cumulative_clean_window_hours: 42
    note: >
      Standing 19-IOC PeopleSoft/UNC6240 sentinel-set continues
      11th consecutive clean sweep across defenseclaw_local +
      archimedes (cumulative 42+h clean window since 2026-06-13 PM
      per FLASH 12:00 commit substrate). Frank is NOT higher-ed
      environment (68% UNC6240 victim profile per finding-0006);
      silent-Splunk-does-NOT-disconfirm per Hard Rule 8 binding.
      Visibility-bounded absence flagged, NOT treated as negative
      evidence on external Mandiant primary substrate.

single_source_veto_applied: false
single_source_veto_layers: []
single_source_veto_note: >
  Cluster has multi-layered independence: publisher-side (The
  Register + BC), victim-side (CoE direct ACK), actor-side
  (ShinyHunters self-claim), and third-party IR-firm (GTIG
  carry-forward primary from finding-0006). The substantive
  scope claims (297 GB / 429K files) remain single-source
  ShinyHunters self-claim — that specific layer is single-evidence-
  basis, but the procedural-fact layer (CoE investigation ongoing,
  ShinyHunters claiming the vector) is multi-layered. WEP ceiling
  on procedural-fact layer is NOT capped; WEP ceiling on
  substantive scope claims remains "likely" per the underlying
  single-source veto from finding-0001.
wep_ceiling: very_likely  # on procedural-fact layer (CoE investigation + ShinyHunters self-claim); scope claims cap at "likely" per inherited single-source veto

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "Council of Europe ShinyHunters PeopleSoft CVE-2026-35273 — Council of Europe direct ACK + ShinyHunters explicit vector self-claim — layered UPDATE on finding-2026-06-15-0001"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-15-pm-003-theregister-bc-council-of-europe-shinyhunters-peoplesoft-ack-substrate-update
  attribution_claims:
    - claimed_actor: "ShinyHunters"
      claimed_by_sources: [theregister, bleepingcomputer]
      claimed_by_source_layer: extortion_brand_self_claim_via_tor_leak_site + spokesperson_statement_to_the_register
      requires_analyst_review: true
      note: |
        Hard Rule 2 preserved — Mandiant primary attribution language
        is UNC6240; ShinyHunters is the extortion-brand self-claim
        layer. Archimedes does NOT originate the UNC6240 ↔ ShinyHunters
        identity mapping; Mandiant carry-forward primary substrate
        asserts the dual-naming chain. Neither actor on _roster.yaml.
    - claimed_actor: "UNC6240 (per corpus carry-forward)"
      claimed_by_sources: [mandiant-gtig]
      claimed_by_source_layer: mandiant_primary_per_finding_2026_06_13_0006
      requires_analyst_review: true
      note: "Carry-forward from finding-2026-06-13-0006 Mandiant primary"

# ============================================================================
# Inclusion eligibility
# ============================================================================
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - vuln_tracker_kev_compliance_retrospective_cohort
  not_eligible_for:
    - flash  # CVE-2026-35273 anti-noise locked through FLASH 12:00 + morning brief substrate; finding is UPDATE on already-shipped finding-0001
    - actor_profile_update  # ShinyHunters/UNC6240 operator-deferred /new-actor candidacy; Archimedes does NOT originate roster addition

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: true   # WEP "very likely" on procedural layer + attribution claims + KEV deadline closure tonight
analyst_review_complete: true
analyst_review_run_id: analyst-20260615-160800
red_team_review_required: true  # WEP ceiling >= very_likely on procedural-fact layer triggers red-team review
red_team_review_complete: true
red_team_outcome: sign_off
red_team_review:
  reviewed_at: 2026-06-15T17:08:00-04:00
  reviewed_by: red-team-analyst
  run_id: red-team-20260615-170000
  mode: post_analyst
  scope: >
    Procedural-fact layer ONLY (WEP very_likely). Substantive-vector layer
    already capped at "roughly even" by analyst ACH; scope-claims layer
    already capped at "likely" by inherited single-source veto. Red-team
    does NOT re-litigate those — they survived analyst pressure and the
    three-layer separation is the very thing under defense here.
  strongest_counter_hypothesis:
    hypothesis: >
      The procedural-fact layer ("CoE is investigating; ShinyHunters has
      claimed the CVE vector") collapses if CoE's "currently investigating"
      statement is interpreted as boilerplate PR acknowledgement of
      ShinyHunters' public claim rather than as confirmation of an actual
      incident under internal investigation. Under that reading the
      procedural fact reduces to "ShinyHunters claimed a thing + CoE put
      out a non-denial" — which is materially weaker than "victim
      organization confirmed an incident is being investigated."
    evidence_for_counter:
      - "CoE 'declined to comment further' — consistent with both 'real incident under wraps' and 'no incident, declining to dignify the claim with a denial'"
      - "Generic corporate-PR framing (KAC A2 already qualified) does not distinguish actual breach from investigation-of-claims"
      - "ShinyHunters self-claim is single-source actor evidence with documented brand-aggrandizement history (Canvas 275M, Nottingham 454K, Infinite Campus 137K corpus substrate)"
    evidence_against_counter:
      - "The Register quotes a CoE spokesperson directly with 11-word verbatim and named-byline cyber-crime desk attribution — this is sourced ACK, not a media inference"
      - "BleepingComputer same-day independent relay (Sergiu Gatlan byline, different publisher) corroborates the publisher-side fact of CoE response — two B-grade publishers converged on the same victim-spokesperson contact"
      - "Procedural fact under defense is not 'CoE confirmed a breach' — it is 'CoE acknowledged an investigation is ongoing.' That weaker fact IS what the spokesperson said per The Register, and CoE issuing a 'no comment beyond investigation' is itself a procedural fact even if the underlying incident is later disputed"
      - "Analyst's three-layer separation already isolates this — the substantive scope and vector claims are capped at likely/roughly-even respectively, so the very_likely is doing narrow work on the narrowest fact"
  strongest_counter_wep: likely
  weaknesses_in_primary_assessment:
    - "Three-layer WEP separation is the load-bearing scaffold. If the briefer collapses procedural and substantive into a single confidence statement, the very_likely floods downstream and misrepresents the substantive-vector claim that ACH placed at roughly-even."
    - "ShinyHunters 'spokesperson' channel is opaque — The Register attribution is to 'a ShinyHunters spokesperson' which could be a Tor leak-site account operator, a forum handle, or a DM thread. The actor self-claim layer has weaker provenance than the CoE-side ACK."
  recommendation: sign_off
  sign_off_rationale: >
    The procedural-fact layer survives contrarian challenge. The strongest
    counter argues that CoE's statement is boilerplate non-denial rather
    than meaningful ACK, but even under that reading the procedural fact
    ("CoE issued a public statement acknowledging an investigation, on
    record to two B-grade publishers via named spokesperson") still holds
    at very_likely. The counter-hypothesis would knock down a STRONGER
    claim that Archimedes is NOT making — Archimedes is not asserting
    "CoE confirmed a breach." The analyst's three-layer WEP separation
    correctly isolates what very_likely covers and what it does not.
  qualifying_language_required:
    procedural_fact_layer: "very likely (CoE has acknowledged an investigation per its spokesperson to The Register; ShinyHunters has publicly claimed CVE-2026-35273 as the vector via the same publisher channel)"
    substantive_vector_layer: "roughly even chance (per analyst ACH — four alternative hypotheses tie on inconsistency count with H1; CoE has not confirmed vector)"
    scope_claims_layer: "likely (per inherited single-source veto from finding-0001; 297 GB / 429K files remains ShinyHunters self-claim through B-publisher relay)"
    briefer_directive: >
      Brief language MUST NOT collapse these three layers into a single
      confidence statement. Default-safe phrasing: "ShinyHunters has
      publicly claimed the CoE breach was via Oracle PeopleSoft
      CVE-2026-35273; CoE has acknowledged it is investigating (per The
      Register + BleepingComputer). CoE has not confirmed the vector;
      the substantive vector linkage is not independently corroborated."
  specific_tests_that_would_resolve:
    - "CoE issues a second statement confirming or denying the CVE-2026-35273 vector specifically"
    - "Independent IR firm (Mandiant / Unit 42 / CrowdStrike / Volexity) publishes confirming the vector for CoE specifically"
    - "ShinyHunters publishes data sample inconsistent with CoE's actual systems (would elevate fabrication H4)"
    - "First-party Splunk hit on the standing 19-IOC PeopleSoft/UNC6240 sentinel-set against any partner-shared environment"
  wep_adjustment_recommended: null
  wep_adjustment_rationale: "No adjustment — three-layer separation is correct; very_likely is appropriate on the narrow procedural-fact layer."
  attribution_discipline_check:
    hard_rule_2_red_team_compliance: passed
    note: >
      Red-team did NOT originate any new actor attribution. The counter-
      hypothesis tests CoE-side language interpretation and ShinyHunters
      spokesperson-channel provenance — both arguments AGAINST sourced
      claims rather than novel attributions. UNC6240 ↔ ShinyHunters
      mapping remains Mandiant-primary-sourced; neither actor proposed
      for roster addition.
  notes: >
    Sign-off conditional on the briefer preserving the three-layer
    separation. If the briefer drafts language that collapses procedural
    + substantive into one WEP statement, this red-team sign-off does
    NOT extend to that language — escalate back. The three-layer
    separation is the substance of the sign-off, not just a side note.
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Is ShinyHunters' explicit self-claim that the Council of Europe compromise was via Oracle PeopleSoft CVE-2026-35273 supported against alternative explanations?"
      analyzed_at: 2026-06-15T16:22:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: "ShinyHunters' self-claim is accurate: CoE compromise was via CVE-2026-35273 PeopleSoft exploitation, consistent with the broader UNC6240/ShinyHunters campaign documented by GTIG (May 27 - June 9, >100 orgs, 68% higher-ed)."
        - id: H2
          statement: "ShinyHunters compromised CoE via a different vector (phishing, Salesforce intrusion wave per Infinite Campus precedent, vendor compromise) and is opportunistically claiming the high-profile PeopleSoft vector for brand-aggrandizement."
        - id: H3
          statement: "A different actor compromised CoE; ShinyHunters is reposting victim data acquired second-hand from a broker/affiliate market, claiming it as their own."
        - id: H4
          statement: "The CoE data exposure ShinyHunters is claiming is a fabrication (data composition is synthetic or recycled from prior leaks); CoE is investigating ShinyHunters' claims rather than a confirmed breach."
        - id: H5
          statement: "ShinyHunters compromised CoE via PeopleSoft but the broader UNC6240 campaign cluster is methodologically distinct from this specific CoE incident — i.e., correct vector + correct actor + wrong cluster-attribution."
      evidence:
        - id: E1
          description: "ShinyHunters spokesperson explicit statement to The Register linking CoE to PeopleSoft CVE-2026-35273 zero-day"
          source: theregister-bleepingcomputer-dual-publisher
          digraph: B2
          weight: 2
        - id: E2
          description: "Council of Europe spokesperson direct ACK: 'currently investigating the matter and assessing the situation' + 'declined to comment further'"
          source: coe-direct-spokesperson-via-theregister
          digraph: A1
          weight: 3
        - id: E3
          description: "GTIG primary substrate (finding-0006 carry-forward): malicious activity May 27 - June 9 consistent with CVE-2026-35273; >100 global orgs notified; 68% higher-ed sector; most US-based"
          source: gtig-mandiant-primary-carry-forward
          digraph: A2
          weight: 3
        - id: E4
          description: "CoE is 46-state intergovernmental human-rights body (NOT higher-ed, NOT US-based) — sector/geography inconsistent with GTIG-documented 68%-higher-ed/most-US victim pattern"
          source: structural-fact-verifiable
          digraph: A1
          weight: 3
        - id: E5
          description: "ShinyHunters established pattern of scope-inflation and brand-aggrandizement claims (Canvas 275M paid + Nottingham 454K + Infinite Campus 137K + DentaQuest carry-forward)"
          source: corpus-substrate-multi-finding
          digraph: B2
          weight: 2
        - id: E6
          description: "Standing 19-IOC PeopleSoft/UNC6240 sentinel — 11 consecutive clean sweeps on Frank's defenseclaw_local + archimedes (visibility-bounded — Frank not higher-ed)"
          source: splunk-first-party-carry-forward
          digraph: A1
          weight: 3
        - id: E7
          description: "Oracle out-of-band mitigations only, NO GA patch — vector remains exploitable; CoE timing plausible within May 27 - June 9 window"
          source: finding-0006-carry-forward-mandiant-primary
          digraph: A2
          weight: 3
      matrix:
        E1: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E2: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E3: {H1: C, H2: N, H3: N, H4: N, H5: N}
        E4: {H1: I, H2: C, H3: C, H4: N, H5: C}
        E5: {H1: N, H2: C, H3: C, H4: C, H5: N}
        E6: {H1: N, H2: N, H3: N, H4: N, H5: N}
        E7: {H1: C, H2: N, H3: N, H4: N, H5: C}
      inconsistency_counts:
        H1: 1
        H2: 0
        H3: 0
        H4: 0
        H5: 0
      diagnostic_evidence:
        - E4: "Distinguishes vector-fits-GTIG-pattern (H1) from vector-doesn't-fit-pattern (H2/H3/H5) — CoE sector/geography is the diagnostic gap"
        - E5: "Distinguishes ShinyHunters-actually-did-it (H1/H5) from ShinyHunters-opportunistic-claim (H2/H3/H4)"
      ranking:
        - rank: 1-tied
          hypothesis_id: H2
          rationale: "Zero inconsistencies; CoE sector/geography mismatch with GTIG higher-ed pattern is well-explained by ShinyHunters using a different vector (Salesforce intrusion per Infinite Campus precedent, phishing, vendor compromise) and opportunistically claiming the headline CVE."
          wep: roughly_even
        - rank: 1-tied
          hypothesis_id: H3
          rationale: "Zero inconsistencies; ShinyHunters' established pattern of reposting/aggregating victim data is consistent with brand-aggrandizement."
          wep: roughly_even
        - rank: 1-tied
          hypothesis_id: H4
          rationale: "Zero inconsistencies on available evidence; CoE's investigation-only stance does NOT confirm any actual data exposure occurred. Fabrication remains live until CoE confirms scope."
          wep: roughly_even
        - rank: 1-tied
          hypothesis_id: H5
          rationale: "Zero inconsistencies; PeopleSoft + ShinyHunters but different cluster than UNC6240 GTIG campaign."
          wep: roughly_even
        - rank: 5
          hypothesis_id: H1
          rationale: "One inconsistency (E4 — CoE sector/geography doesn't fit GTIG 68%-higher-ed/most-US pattern); requires ShinyHunters to have opportunistically expanded targeting outside the documented campaign profile."
          wep: possibly
      sensitivity_analysis:
        brittleness: high
        load_bearing_evidence: [E4, E5]
        if_E4_reframed: "If CoE's status as intergovernmental body (rather than higher-ed) is considered 'adjacent enough' to higher-ed PeopleSoft deployments, H1 inconsistency disappears and H1 rises to leader"
        if_CoE_confirms_PeopleSoft_vector: "H1 rises to leader; H2/H3/H4 fall; assessment shifts to 'likely' or 'very likely' on substantive vector claim"
        if_independent_IR_firm_corroborates_vector_for_CoE: "H1 rises to leader; veto lifts; substrate consolidates"
        if_CoE_confirms_DIFFERENT_vector: "H1 falls to remote; H2 rises to leader; substrate fragments"
      tripwires:
        - observation: "Council of Europe confirms or denies the PeopleSoft vector specifically"
          effect: "Either confirms H1 or elevates H2/H3/H4; rerun ACH"
        - observation: "Independent IR-firm (Mandiant/Unit42/CrowdStrike/Volexity) publishes confirming the vector for CoE specifically"
          effect: "Confirms H1; rerun ACH; potential WEP elevation"
        - observation: "ShinyHunters publishes data sample inconsistent with CoE's actual systems"
          effect: "Elevates H4 (fabrication); revise assessment"
        - observation: "Splunk sentinel-set catches an indicator on Frank or any partner-shared environment"
          effect: "First-party telemetry; rerun ACH with Hard Rule 8 priority"
      conclusion:
        summary: |
          ACH reveals the SUBSTANTIVE vector claim (CoE was compromised via
          CVE-2026-35273) is far weaker than the procedural-fact framing
          ("ShinyHunters has claimed the vector to The Register"). Four hypotheses
          (H2/H3/H4/H5) tie at zero inconsistencies as plausible alternatives to
          H1 (Sygnia's framing). E4 (CoE sector/geography mismatch with GTIG
          higher-ed pattern) is the diagnostic gap that pushes H1 to rank-5 on
          the substantive vector layer. The procedural-fact (ShinyHunters
          claimed it; CoE is investigating) holds at WEP very_likely; the
          SUBSTANTIVE-vector merit caps at "roughly even chance" between H1 and
          the four opportunistic-claim alternatives. Hard Rule 2 preserved —
          this ACH pressure-tests ShinyHunters' sourced self-claim against
          alternatives that other sources have NOT made; it does NOT originate.
        wep: very_likely
        confidence_caveats: |
          Procedural-fact layer is solid; substantive-vector-truth is brittle.
          Recommend explicit caveat in brief language separating "ShinyHunters
          claimed X" (high confidence) from "ShinyHunters did X" (roughly even
          across H1-H5). The original grader's split between procedural
          (very_likely) and scope-claims (likely per inherited single-source veto)
          is appropriate; ACH supports adding a third layer — substantive vector
          claim caps at "roughly even chance" until CoE confirms or independent
          IR firm corroborates.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "WEP 'very likely' on the procedural-fact layer (CoE investigation ongoing,
        ShinyHunters has claimed CVE-2026-35273 vector for CoE)."
      analyzed_at: 2026-06-15T16:22:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication procedural-layer assumption check; supplements ACH on substantive merit"
      assumptions:
        - id: A1
          statement: "The Register correctly transcribed CoE spokesperson statement and ShinyHunters spokesperson statement"
          category: source_reliability
          stated: false
          why_must_be_true: "Direct quote attribution is the procedural-fact basis"
          when_could_be_false: "Transcription errors, mistranslation (CoE typically operates in French/English), spokesperson misidentification"
          evidence_for: [bleepingcomputer_same_day_independent_confirmation_of_quote_substance]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A2
          statement: "CoE's 'currently investigating' statement constitutes meaningful corroboration of an actual incident"
          category: semantic
          stated: false
          why_must_be_true: "Procedural-fact layer rests on victim-acknowledgement-of-investigation as meaningful evidence basis"
          when_could_be_false: "CoE is investigating ShinyHunters' CLAIMS, not a confirmed incident; the 'investigating' framing is procedurally identical whether actual breach occurred or not"
          evidence_for: [coe_decline_to_comment_further_consistent_with_active_incident_investigation_pattern]
          evidence_against: [generic_corporate_PR_framing_does_not_distinguish_real_vs_claimed_incidents]
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A3
          statement: "ShinyHunters' spokesperson statement constitutes meaningful evidence of vector"
          category: source_reliability
          stated: false
          why_must_be_true: "Actor self-claim is the binding evidence for the vector linkage"
          when_could_be_false: "ShinyHunters has established pattern of scope-inflation and opportunistic claiming; spokesperson statements are not under oath"
          evidence_for: [actor_self_claim_via_publisher_relay_via_b_grade_publisher]
          evidence_against: [shinyhunters_pattern_of_brand_aggrandizement_per_corpus_substrate_canvas_nottingham_infinite_campus]
          confidence: low
          centrality: critical
          classification: test
        - id: A4
          statement: "ShinyHunters and UNC6240 are the same actor cluster per Mandiant primary"
          category: actor_continuity
          stated: false
          why_must_be_true: "Cross-corroboration via GTIG primary depends on UNC6240↔ShinyHunters identity mapping"
          when_could_be_false: "Mandiant primary mapping is wrong; brand and actor cluster diverge"
          evidence_for: [mandiant_primary_attribution_per_finding_0006_carry_forward]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A5
          statement: "Splunk first-party silence is non-disconfirming because Frank is not higher-ed environment consistent with 68% UNC6240 victim profile"
          category: visibility
          stated: true
          why_must_be_true: "Hard Rule 8 binding on silent-Splunk-does-NOT-disconfirm requires the visibility-bounded-absence framing"
          when_could_be_false: "Frank's environment changes or sentinel-set is misconfigured"
          evidence_for: [11_consecutive_clean_sweeps_42h_cumulative_clean_window, frank_environment_profile_audit]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 2
        qualify: 2
        test: 1
        reject: 0
      remediation:
        status: proceed
        blocking_assumption: A3
        blocking_detail: |
          A3 (ShinyHunters' spokesperson statement constitutes meaningful evidence
          of vector) is low-confidence + critical-centrality — the interesting
          KAC box. Test would be CoE confirmation of vector OR independent IR-firm
          corroboration. ABSENT that test passing, the substantive-vector claim
          remains capped at "roughly even chance" per ACH; procedural-fact layer
          can proceed at "very likely" with explicit caveat.
        qualifying_caveats:
          - "CoE 'investigating' statement does not distinguish actual breach from investigation-of-claims (A2 qualify)"
          - "ShinyHunters self-claim is single-source actor evidence basis; substrate is procedurally B2 but substantively C3 (A3 test pending CoE/IR-firm corroboration)"
          - "UNC6240↔ShinyHunters identity mapping relies on Mandiant primary; cross-walk is sourced, not originated (A4 qualify)"
        next_action: "Proceed to publication with explicit three-layer WEP separation: procedural-fact 'very likely' / substantive-vector 'roughly even' / scope-claims 'likely' per inherited veto. Red-team escalation REQUIRED per procedural-fact 'very likely' trigger."
      recommended_wep_after_test:
        if_coe_confirms_vector: "Substantive-vector lifts to 'likely' or 'very likely'"
        if_independent_ir_firm_corroborates: "Substantive-vector lifts to 'likely'"
        if_coe_confirms_different_vector: "Substantive-vector falls to 'remote'; H2 takes leader; assessment fragments"
        current_state: "Procedural-fact 'very likely' appropriate with three-layer caveat; substantive-vector caps at 'roughly even chance'"

vuln_tracker_handoff:
  cve_id: CVE-2026-35273
  related_vt_id: VT-PEOPLESOFT-EXISTING  # Carry-forward — vuln-tracker entry should already exist per finding-2026-06-13-0006
  proposed_action: kev_compliance_retrospective_phase_starts_2026_06_16
  fceb_bod_26_04_deadline: 2026-06-15 EOD
  current_finding_publication: 2026-06-15 ~16:00 EDT (T-minus ~7h before deadline closure)
  carry_forward_substrate: finding-2026-06-13-0006 (Mandiant primary direct retrieval)
  new_victim_acknowledgements_this_update:
    - "Council of Europe (direct spokesperson ACK 2026-06-15)"

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs:
  - 2026-06-15-afternoon
retracted: false
retraction_brief_id: null
---

# UPDATE on finding-2026-06-15-0001: Council of Europe direct victim ACK obtained via The Register + BleepingComputer dual-publisher relays; ShinyHunters spokesperson explicitly claims CoE compromise was via Oracle PeopleSoft CVE-2026-35273; CoE confirms investigation but declines further comment; T-minus ~7h before FCEB BOD 26-04 KEV deadline closure

## Summary

The Register (cyber-crime desk) and BleepingComputer (Sergiu Gatlan byline)
dual-publisher relays on 2026-06-15 surface two net-new substrate layers vs
the morning brief's finding-2026-06-15-0001: (1) **Council of Europe direct
victim acknowledgement** — CoE spokesperson directly told The Register the
organization is "currently investigating the matter and assessing the
situation" (11-word verbatim quote) and "declined to comment further";
(2) **ShinyHunters spokesperson explicit vector self-claim** — the actor
explicitly claimed to The Register that the CoE compromise was via the same
Oracle PeopleSoft zero-day (CVE-2026-35273) substrate that anchors
finding-2026-06-13-0006. CoE confirmed investigation only — did NOT confirm
the 297 GB / 429K files / payroll-HR-medical scope claims (those remain
ShinyHunters self-claim C3 layer carry-forward from finding-0001), and did
NOT confirm the CVE-2026-35273 vector. GTIG late-week report substrate
(May 27 - June 9 mass exploitation, >100 orgs notified, 68% higher-ed sector)
is re-cited via The Register without new GTIG evidence basis — carry-forward
from finding-2026-06-13-0006. This finding lands T-minus approximately 7
hours before the FCEB BOD 26-04 KEV deadline closure for CVE-2026-35273
(EOD tonight 2026-06-15). The 19-IOC PeopleSoft/UNC6240 standing sentinel
set continues its 11th-consecutive clean sweep on Frank's defenseclaw_local
+ archimedes indexes per Hard Rule 8 binding (Frank is not higher-ed
environment consistent with 68% UNC6240 victim profile; visibility-bounded
absence flagged).

## Sources

### The Register (source_yaml_id: theregister, digraph: B)

- URL: https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/
- Published: 2026-06-15 17:44 UTC
- Byline: cyber-crime desk (Iain Thomson byline customary for this story class)
- Key claim: Direct retrieval of CoE spokesperson statement + ShinyHunters spokesperson explicit CVE-2026-35273 vector self-claim for CoE compromise

### BleepingComputer (source_yaml_id: bleepingcomputer, digraph: B)

- URL: https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/
- Published: 2026-06-15 16:37 UTC
- Byline: Sergiu Gatlan
- Key claim: Independent same-day publisher relay of CoE ACK + ShinyHunters claim convergence

### Council of Europe (direct spokesperson statement, via The Register)

- Statement verbatim: "currently investigating the matter and assessing the situation" (11 words)
- Additional: "declined to comment further"
- Source-layer: direct victim-organization ACK at procedural-fact layer

### Mandiant / GTIG (carry-forward primary via finding-2026-06-13-0006)

- Carry-forward substrate: late-week report; activity consistent with CVE-2026-35273 exploitation May 27 - June 9; >100 global orgs notified; 68% higher-ed sector
- Re-cited by The Register without new GTIG content this sweep

## Technical detail

### Council of Europe direct ACK (NET-NEW vs finding-0001)

CoE spokesperson statement to The Register verbatim (Hard Rule 6 preserved —
11 words, under 15-word cap, one quote per source):

> "currently investigating the matter and assessing the situation"

CoE additionally "declined to comment further" — victim ACK is at the
**investigation-layer only**. No confirmation of:
- Scope numbers (297 GB / 429K files)
- Data categories (payroll / HR / medical)
- CVE vector (Oracle PeopleSoft CVE-2026-35273)
- Threat actor (ShinyHunters / UNC6240)

This NET-NEW substrate resolves the `no-CoE-ACK` weakness anchoring
finding-2026-06-15-0001 at C3. Lifts the procedural-fact layer from C3 → B2.

### ShinyHunters explicit vector self-claim (NET-NEW vs finding-0001)

Per The Register, a ShinyHunters spokesperson told the publication that the
Council of Europe is "yet another victim of the Oracle PeopleSoft heist" —
explicitly linking the CoE compromise to the CVE-2026-35273 substrate that
anchors finding-2026-06-13-0006.

This SUPERSEDES finding-0001's framing of the CoE breach and Oracle PeopleSoft
campaign as SEPARATE (which was based on SecurityWeek not making the linkage).
The vector self-claim is actor-attestation only — CoE has NOT confirmed the
vector, and no third-party IR firm has corroborated. Methodologically:
- Procedural-fact of ShinyHunters claiming the vector: **B2** (publisher-
  relay-verifiable per direct quote)
- Substantive truth of the vector for CoE specifically: **C3** (single-source
  actor self-claim through B-publisher relay; CoE has not confirmed)

### Carry-forward GTIG substrate (re-cited, NOT new evidence basis)

Per The Register relay of Mandiant / Google Threat Intelligence Group
late-week report (carry-forward primary from finding-2026-06-13-0006):

- Activity "consistent with the exploitation of CVE-2026-35273"
  between **May 27 and June 9, 2026**
- GTIG IR responders notified **>100 global orgs** "whose IP addresses
  correlated with potentially vulnerable endpoints"
- **Most US-based**; **68% higher-education sector**

The Register re-states without new GTIG content this sweep — substrate is
locked under anti-noise from finding-2026-06-13-0006.

### Carry-forward ed-tech cluster context

Per The Register restatement of prior-surface substrate (all carry-forward
anti-noise — restated for cluster context only):

- **Instructure Canvas**: mid-May 2026; 275M records exposed; "reached an
  agreement" with ShinyHunters (per The Register framing — corporate-speak
  for paid the ransom demand)
- **Infinite Campus** (K-12 software): March 2026; ShinyHunters Salesforce
  intrusion wave; did NOT pay; ~137K individuals' data published. Today's
  BleepingComputer 12:38 piece is same item — filtered as anti-noise per
  pre-flash sentinel sweep.
- **University of Nottingham**: last week; 454,600 current and former
  students' records dumped on ShinyHunters leak site

### FCEB BOD 26-04 KEV deadline closure (CRITICAL TIMING)

CVE-2026-35273 (Oracle PeopleSoft, zero-day exploited per UNC6240/
ShinyHunters per Mandiant primary):

- CISA KEV listing: per finding-2026-06-12-0001 + 2026-06-13-0006 carry-forward
- FCEB BOD 26-04 deadline: **EOD TONIGHT 2026-06-15** (3-day clock)
- Oracle patch state: out-of-band mitigations only, NO GA patch
- This finding publication: 2026-06-15 ~16:00 EDT
- **T-minus approximately 7 hours before deadline closure**

The 16:00 afternoon brief is the **FINAL pre-deadline coverage window** for
FCEB compliance. Tomorrow's morning brief (2026-06-16 08:00) lands in the
KEV-compliance retrospective phase.

## IOCs surfaced

```yaml
iocs:
  cves:
    - id: CVE-2026-35273
      product: Oracle PeopleSoft (FSCM / HCM / Campus Solutions modules)
      status: zero_day_exploited
      kev_listed: true (per VT corpus tracking per finding-2026-06-13-0006 carry-forward)
      kev_due_date: 2026-06-15 EOD (FCEB BOD 26-04)
      patch_availability: "Oracle out-of-band mitigations only — NO GA patch (carry-forward from finding-2026-06-13-0006)"

  hashes: []  # Standing 19-IOC set unchanged — carry-forward from finding-2026-06-13-0006
  ips: []
  domains: []
  urls: []

  victims_named_this_finding:
    - "Council of Europe (ACK-OBTAINED 2026-06-15 spokesperson statement; investigation-layer only — no scope/vector confirmation)"

  carry_forward_victims_anti_noise:
    - "Instructure Canvas (mid-May 2026, 275M records, paid)"
    - "Infinite Campus (March 2026, 137K records via Salesforce intrusion wave, did NOT pay)"
    - "University of Nottingham (last week, 454,600 records)"

attribution_claims:
  - source: ShinyHunters (self-claim, Tor leak site + spokesperson to The Register)
    actor_claimed_self: ShinyHunters
    actor_claimed_vector_for_coe: CVE-2026-35273 Oracle PeopleSoft zero-day
    confidence: SELF_CLAIM_VIA_PUBLISHER_RELAY
    note: "Methodologically procedural-fact-B2 + substantive-vector-C3 single-source layered"

  - source: Council of Europe (direct spokesperson, via The Register)
    statement: "currently investigating the matter and assessing the situation"
    statement_word_count: 11
    additional: "declined to comment further"
    confidence: VICTIM_ACK_AT_INVESTIGATION_LAYER_ONLY
    note: "Procedurally A1 on fact-of-investigation; does NOT corroborate scope or vector"

  - source: Mandiant / GTIG (carry-forward primary via finding-2026-06-13-0006)
    timeline: "malicious activity consistent with exploitation of CVE-2026-35273 between May 27 and June 9"
    notification_scope: ">100 global orgs whose IP addresses correlated with potentially vulnerable endpoints"
    sector_breakdown: "Most US-based; 68% higher education"
    note: "Re-cited via The Register without new GTIG content — carry-forward anti-noise from finding-2026-06-13-0006"
```

## Relationship to existing findings

- **UPDATE on finding-2026-06-15-0001** (SecurityWeek single-publisher relay of
  ShinyHunters Tor leak-site self-claim against Council of Europe at morning
  brief). This finding adds:
  (1) Council of Europe direct victim ACK at investigation-layer (NET-NEW);
  (2) ShinyHunters spokesperson explicit CVE-2026-35273 vector self-claim
      for CoE (NET-NEW vs finding-0001's "SEPARATE campaigns" framing);
  (3) Dual-publisher independent relay (The Register + BleepingComputer)
      vs finding-0001's single SecurityWeek substrate.

- **Lateral linkage to finding-2026-06-13-0006** (Mandiant + GTIG primary
  direct retrieval on UNC6240 / ShinyHunters Oracle PeopleSoft CVE-2026-35273
  campaign): GTIG late-week report is re-cited via The Register but no new
  GTIG content this sweep — substrate locked under anti-noise.

- **Lateral linkage to finding-2026-06-12-0001 + finding-2026-06-11-0006
  + finding-2026-06-10-0012** (PeopleSoft CVE-2026-35273 substrate lineage):
  Carry-forward anti-noise on CVE substrate; this UPDATE concerns the CoE
  victim-layer + dual-publisher convergence only.

## Open questions for analyst / red-team

1. **Red-team review required** (WEP "very likely" on procedural layer):
   Argue against the procedural-fact layer (CoE ACK + ShinyHunters
   vector self-claim). Specifically: (a) does CoE's "investigating"
   statement constitute meaningful corroboration given they declined
   to confirm scope or vector? (b) does ShinyHunters' vector self-claim
   constitute meaningful evidence given the actor's pattern of
   scope-inflation and brand-aggrandizement? (c) is the vector linkage
   to CVE-2026-35273 plausible given GTIG's 68% higher-ed framing vs
   CoE being an intergovernmental org?
2. **Vector independent verification watch** (analyst): CoE has NOT
   confirmed CVE-2026-35273 as the breach vector. Watch for
   third-party IR-firm publication (Mandiant / Unit 42 / CrowdStrike /
   Volexity) explicitly confirming the vector for CoE specifically.
   Absent independent confirmation, vector remains ShinyHunters
   self-claim C3 layer.
3. **/new-actor candidacy decision** (operator-deferred, Hard Rule 5):
   ShinyHunters / UNC6240 substrate continues strengthening — third
   campaign in visible portfolio this week (CoE / Oracle PeopleSoft
   mass-exploitation / DentaQuest / Tchap-adjacent + ed-tech cluster
   Canvas / Infinite Campus / Nottingham). Hard Rule 5 binding —
   only operator can invoke /new-actor.
4. **KEV-compliance retrospective phase** (vuln-tracker handoff):
   FCEB BOD 26-04 deadline EOD tonight 2026-06-15. Tomorrow's morning
   brief lands in retrospective-compliance-metrics phase per
   standard pattern. Recommend coverage-log decision on whether
   KEV-compliance-cohort becomes a standing brief section per
   morning brief analyst_handoff_notes from 02b713e.
5. **First-party Frank-environment watch** (Hard Rule 8): Standing
   19-IOC PeopleSoft/UNC6240 sentinel-set continues 11th consecutive
   clean sweep. Frank NOT higher-ed environment; visibility-bounded
   absence per Hard Rule 8 binding. Continue sentinel monitoring
   post-deadline closure.
6. **A&D / DIB intersection** (analyst): NONE — CoE is 46-state
   intergovernmental human-rights body. No A&D-prime / DIB / aerospace
   / defense intersection. Substrate continues to inform UNC6240/
   ShinyHunters operational-template understanding for A&D defender
   pattern recognition but no direct A&D campaign association in this
   surface.

## Analytic notes (from analyst review)

ACH surfaced a meaningful gap between procedural-fact and substantive-vector layers. The procedural-fact (ShinyHunters claimed CVE-2026-35273 for CoE; CoE is investigating) holds at "very likely" — the source chain is rigorous (two B-grade publishers + direct CoE spokesperson + actor self-claim). The SUBSTANTIVE vector claim is materially weaker: four alternative hypotheses (different vector + opportunistic claim, second-hand data resale, fabrication, correct-vector-wrong-cluster) all score zero inconsistencies and tie at "roughly even" while the leading hypothesis (H1 — vector claim is accurate) carries one inconsistency from E4 (CoE sector/geography mismatch with GTIG 68%-higher-ed/most-US pattern).

KAC reinforces this with A3 (ShinyHunters' spokesperson statement as meaningful vector evidence) classified as Test — low-confidence + critical-centrality. ABSENT CoE vector confirmation or independent IR-firm corroboration specifically for CoE, the substantive-vector claim cannot rise above "roughly even chance" regardless of the procedural-fact strength.

Recommend brief language use three-layer WEP separation: procedural-fact "very likely" / substantive-vector "roughly even" / scope-claims "likely" per inherited single-source veto from finding-0001. Red-team escalation REQUIRED (already flagged by grader). The brittleness is HIGH: CoE statement confirming or denying the vector flips ranking entirely. Watch tripwires aggressively.
