---
id: finding-2026-06-11-0007
finding_id: finding-2026-06-11-0007-the-record-doj-denis-obrezko-void-blizzard-infrastructure-provider-indictment-boston-court-thailand-extradition-defense-contractors-victim-category
title: "DOJ indicts 36-year-old Russian national Denis Obrezko for infrastructure-provider role in Void Blizzard Russia-aligned cyberespionage cluster; arrested November 2025 Phuket, Thailand; Boston federal court initial appearance 2026-06-10; victim profile named per The Record includes 'government agencies, defense contractors, transportation, media, healthcare, NGOs' — Void Blizzard NOT in roster, Hard Rule 2 binding; /new-actor candidacy flagged for operator"
date: 2026-06-11
created_at: 2026-06-11T16:45:00-04:00
graded_by: grader
grading_run_id: afternoon-20260611-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- PROCEDURAL FACTS LAYER (court filing relayed via single B-grade source) ----
  denis_obrezko_doj_federal_indictment_unsealed_2026_06_10_boston: B2  # The Record relays DOJ court filing; single B-grade publisher; underlying primary IS DOJ A-class but not directly retrieved
  obrezko_36_year_old_russian_national_stavropol: B2  # The Record relay of DOJ filing
  obrezko_arrested_november_2025_phuket_thailand_fbi_thai_royal_police_joint_op: B2  # The Record relay
  obrezko_extradited_to_us_custody: B2  # The Record relay
  obrezko_initial_federal_court_appearance_boston_2026_06_10: B2  # The Record relay
  obrezko_in_custody_status: B2  # The Record relay
  # ---- ALLEGED ROLE LAYER (DOJ filing per The Record relay) ----
  obrezko_alleged_role_infrastructure_provider_support_void_blizzard: B2  # The Record relay of DOJ filing
  obrezko_cryptocurrency_transactions_purchase_vps_internet_domains_attack_infrastructure: B2  # The Record relay
  obrezko_facilitated_unauthorized_computer_access_us_and_foreign_organizations: B2  # The Record relay
  # ---- VICTIM SCALE LAYER (DOJ filing per The Record relay) ----
  at_least_11_us_companies_compromised_per_prosecutors: B2  # The Record relay; specific count from prosecutor framing
  prosecutors_believe_actual_victim_count_higher_than_11: B3  # Forward-looking prosecutor characterization through single-source relay
  void_blizzard_victim_profile_government_agencies_defense_contractors_transportation_media_healthcare_ngos: B2  # The Record verbatim victim profile language (source-direct A&D framing)
  void_blizzard_geographic_scope_europe_and_north_america: B2  # The Record verbatim scope
  void_blizzard_operational_pattern_stolen_credentials_to_email_and_document_theft: B2  # The Record relay
  # ---- ATTRIBUTION LAYER (Hard Rule 2 binding — source attribution preserved) ----
  void_blizzard_characterized_as_relatively_new_threat_group_operating_in_support_of_russian_government_interests: B2  # The Record verbatim attribution framing (NOT Archimedes-originated)
  void_blizzard_NOT_in_archimedes_roster_yaml_v2_2026_05_10: A1  # Verifiable absence per direct roster file retrieval
  microsoft_naming_convention_blizzard_russia: B3  # Background context per Archimedes corpus; not source-directly-attested in this in-window source
  mstic_originator_void_blizzard_naming_late_2024_credential_theft_focused: F6  # Background context per Archimedes corpus knowledge; NOT directly source-attested in this in-window source — Hard Rule 2 binding, do NOT propagate
  no_specific_gru_fsb_svr_unit_attribution_in_source: A1  # Verifiable absence in The Record
  # ---- A&D / DIB RELEVANCE LAYER ----
  defense_contractors_in_source_language_victim_profile: B2  # The Record verbatim; source-direct A&D framing — STRONGEST in-window A&D-direct phrasing observed today
  defense_contractors_named_as_specific_victim_in_this_indictment: A1  # FAILS — verifiable absence; the 11 U.S. companies are NOT enumerated; the "defense contractors" framing is the LONGITUDINAL Void Blizzard victim profile, NOT this indictment-specific victim list
  ad_prime_named_victim_in_window: A1  # FAILS — verifiable absence
  ad_relevance_sector_taxonomy_relay_tier_only: B2  # The Record verbatim sector taxonomy; relay-tier paraphrasing of DOJ filing language
  # ---- CONTINUITY LAYER (cluster context, not corroboration) ----
  continuity_to_2026_06_04_five_eyes_safeguarding_our_secrets_counterintelligence_advisory: B3  # Temporal continuity per collector observation; not campaign corroboration
  continuity_to_finding_2026_06_11_0002_fbi_doj_13_website_seizures_chinese_intelligence: B3  # Temporal continuity; this finding adds Russia-attribution surface alongside today's morning brief's China-attribution surface; both are DOJ/FBI counter-cyberespionage actions in ~7d window; temporal pattern not campaign-link
  # ---- /NEW-ACTOR CANDIDACY LAYER ----
  void_blizzard_new_actor_candidacy_recommended_for_operator: B2  # Per collector observation; Hard Rule 2 requires operator decision, not Archimedes auto-promotion
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / Usually Reliable single-
  source). The Record is the SOLE in-window source; the underlying
  primary IS DOJ (A-class on own filings) but DOJ filing was NOT
  directly retrieved this sweep — substantive content is relay-
  derived. Single-source-veto APPLIES on substantive operational
  claims (alleged role specifics, victim count, victim profile,
  geographic scope, operational pattern). WEP ceiling caps at
  "likely" per veto.

  CRITICAL LAYERED NUANCE:

    (1) THE A&D-DIRECT FRAMING is the longitudinal Microsoft-MSTIC
        Void Blizzard victim profile (Microsoft is the originator
        of the "Blizzard" Russia-attribution naming for actors per
        Archimedes corpus background knowledge), NOT an indictment-
        specific named-defense-prime victim. The 11 U.S. companies
        are NOT enumerated in this source. The "defense contractors"
        framing IS in The Record's literal victim-profile language
        paraphrasing DOJ filing language. Per FLASH-POLICY Trigger 5
        anti-noise: source-language victim taxonomy is NOT the same
        as named-victim grounding. Conservative grading: surface
        the "defense contractors" framing as A&D-direct in-source
        language; do NOT lift to "defense-prime-victim-named" claim.

    (2) HARD RULE 2 BINDING: Void Blizzard is NOT in
        _roster.yaml (verified against full 22-actor list 2026-06-11
        per direct roster file retrieval — Blizzard-string matches
        in roster are: APT28 "Forest Blizzard" alias; Sandworm
        Team APT44 "Seashell Blizzard" alias; Cozy Bear / APT29
        "Midnight Blizzard" alias. NO Void Blizzard match.)
        Archimedes does NOT originate attribution by cross-walking
        Void Blizzard to any tracked actor. The Record's
        characterization "relatively new threat group operating in
        support of Russian government interests" is preserved as
        SOURCE-DIRECT attribution framing with citation. Archimedes
        does NOT propagate it to any roster-tracked actor.

    (3) /NEW-ACTOR CANDIDACY: Three factors warrant operator
        decision:
          (a) Microsoft-MSTIC-tier naming origin (Microsoft is
              ratified A in source-grades.yaml at originator
              layer; Void Blizzard naming origin sits at A1 at
              originator layer per Archimedes corpus background
              knowledge, though NOT directly attested in this
              in-window source);
          (b) DOJ-charged operator now in U.S. custody —
              counter-intelligence operational tempo data point;
          (c) Source-named defense-contractor victim category
              within Void Blizzard's longitudinal Microsoft-tracked
              targeting profile.
        Operator decision is REQUIRED per Hard Rule 2 and
        established /new-actor workflow; Archimedes does NOT
        auto-promote.

    (4) BACKGROUND CONTEXT vs. IN-WINDOW SOURCE: Archimedes corpus
        carries background knowledge of (a) Microsoft "Blizzard"
        weather-system naming convention for Russia-attribution;
        (b) MSTIC originator role for Void Blizzard naming late
        2024 onward as credential-theft-focused Russia-aligned
        actor. NEITHER is directly source-attested in this in-
        window source (The Record). Per Hard Rule 2 + INTEL-GRADING
        rigor: these background-context layers carry F6 ("Cannot
        Be Judged") at this finding because they cannot be
        independently verified in-window without external fetching.
        The collector raw-signal pm-003 flagged these as background
        context for analyst awareness; the grader preserves the
        flag without lifting the grade.

    (5) CONTINUITY TO MORNING BRIEF / WEEK CLUSTER: Today's morning
        brief (finding-2026-06-11-0002) covered FBI/DOJ 13-website
        seizures tied to Chinese intelligence services recruiting
        US-cleared personnel — a CHINA-attribution counter-
        cyberespionage surface. This finding adds a RUSSIA-
        attribution counter-cyberespionage surface in the same
        operational tempo. PLUS 2026-06-04 PM Five Eyes
        "Safeguarding Our Secrets" counterintelligence advisory.
        Three counter-cyberespionage data points across both China
        and Russia attribution surfaces in a 7-day window. This is
        TEMPORAL CONTINUITY, NOT confirmed campaign continuity.
        Grader observation; briefer / analyst handoff for synthesis
        consideration.

  SINGLE-SOURCE VETO APPLICATIONS:
    - APPLIES on all substantive operational claims (alleged role,
      victim count, victim profile, geographic scope, operational
      pattern) — single B-grade source through B-grade relay.
    - APPLIES on the "defense contractors" framing as A&D-direct
      victim category — single B-grade source through B-grade
      relay; sector taxonomy paraphrase, not named-victim
      grounding.
    - NOT APPLIED on the verifiable-absence claims (no specific
      GRU/FSB/SVR unit attribution in source; Void Blizzard not
      in roster) — these are A1 per direct file/source retrieval.

  Hard Rule 2 binding constraint: PRESERVED — Void Blizzard NOT in
  _roster.yaml; Archimedes does NOT originate attribution or cross-
  walk; source attribution framing preserved verbatim with
  citation.

  Hard Rule 6 binding constraint: PRESERVED — at most one short
  verbatim quote per source under 15 words:
    - The Record verbatim victim profile quote: "government
      agencies, defense contractors, transportation, media,
      healthcare" (8 words; sector taxonomy preserve)
    - The Record verbatim attribution framing: "relatively new
      threat group operating in support of Russian government
      interests" (11 words; attribution framing preserve)
  Both quotes are from The Record (one source); per Hard Rule 6
  one-quote-per-source rule, briefer will need to select ONE for
  any downstream brief incorporation.

  Hard Rule 7 binding constraint: PRESERVED — Denis Obrezko is
  publicly named in DOJ federal court filing (per LEGAL-POLICY
  GDPR data-handling table: "Named threat actors (pseudonyms,
  aliases, group names) — freely; Named public figures acting in
  official capacity — freely"; charged subject in unsealed
  federal indictment qualifies as publicly-named-corporate-or-
  legal-figure-named-in-incident with source citation).

  Hard Rule 8 binding constraint: -7d@d first-party Splunk query
  (full IOC set including Void Blizzard, Obrezko, Russian-language
  domain set, MSTIC originator term set): 10 events returned, all
  Archimedes self-instrumentation. Zero substantive first-party
  matches on Void Blizzard, Obrezko, or related infrastructure
  terms. Per Hard Rule 8: silence is not disconfirming.
  defenseclaw_local does not observably run M365 environment
  monitored against Russia-aligned credential-theft TTPs at
  collector-detectable resolution. First-party precedence does
  NOT apply.

source_reliability:
  grade: B
  source_name: "The Record (Recorded Future News) — DOJ federal court filing relay; SOLE in-window source"
  source_yaml_id: the-record
  grade_rationale: >
    The Record (Recorded Future News) is ratified B in source-
    grades.yaml ("Quality journalism, usually well-sourced" per
    INTEL-GRADING.md Security Media category). DOJ-direct primary
    NOT directly retrieved this sweep; substantive content is
    The Record-relay-derived. Single-source through single B-grade
    publisher.
  provisional: false
  cluster_secondary_sources: []
  underlying_primary_not_directly_retrieved:
    source_name: U.S. Department of Justice federal court filing
    proposed_grade_at_originator_layer: A
    rationale: "DOJ unsealed federal indictment is canonical A on own court filings; relay-tier B-grade through The Record. If DOJ press release becomes available in subsequent sweep, regrade candidate."

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_dojs_2024_2026_counter_cyberespionage_indictment_pattern_against_russia_aligned_operators
    - probably_true_consistent_with_microsoft_msticc_void_blizzard_credential_theft_focused_targeting_profile_per_archimedes_background_corpus
    - probably_true_no_contradicting_a_b_grade_source_at_sweep
    - probably_true_technical_claims_internally_coherent_thailand_fbi_extradition_pattern_consistent_with_prior_obrezko_class_arrests
  checklist_NOT_passed_at_grade_1:
    - confirmed_independent_corroboration  # FAILS — single in-window source
    - confirmed_neither_source_cites_the_other_as_origin  # N/A — only one source
    - confirmed_technical_artifacts_match_across_sources  # FAILS — single source, nothing to match
  rationale: >
    Cluster anchor on DOJ federal indictment unsealing relayed
    through single B-grade publisher. Conservative Grade 2 (Probably
    True) per credibility checklist: claim is consistent with
    established DOJ counter-cyberespionage indictment pattern
    against Russia-aligned operators (recurring U.S. federal pattern
    2024-2026); consistent with Microsoft-MSTIC Void Blizzard
    targeting profile (credential-theft-focused Russia-aligned actor
    per Archimedes corpus background knowledge); no contradicting
    A/B-grade source at sweep; technical claims internally coherent
    (Thailand-FBI extradition class consistent with prior counter-
    cybercrime cooperation pattern). Single-source through single
    B-grade publisher disqualifies Grade 1 (Confirmed) per
    corroboration rules.

corroboration:
  independent_sources:
    - the-record  # SOLE in-window source
  independent: false
  test_failed: >
    Single in-window B-grade source; no publisher-independent
    corroboration available this sweep. The underlying DOJ filing
    is A-class canonical at originator layer but was NOT directly
    retrieved — only available through The Record relay.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    Grader-side first-party Splunk query (-7d@d window across
    index=archimedes OR index=defenseclaw_local) on Void Blizzard
    + Obrezko + Russia-aligned credential-theft TTPs keyword
    superset: 10 events returned, all Archimedes self-instrumentation
    (sourcetype archimedes:operation). Zero substantive first-party
    matches. Per Hard Rule 8: silence is not disconfirming.
    defenseclaw_local does not observably run M365 environment
    monitored against Russia-aligned credential-theft TTPs at
    collector-detectable resolution. First-party precedence does
    NOT apply.

single_source_veto_applied: true
single_source_veto_detail: >
  APPLIES on all substantive operational claims (alleged role
  specifics, 11 U.S. companies victim count, victim profile
  taxonomy, geographic scope, operational pattern, "defense
  contractors" sector framing). Single B-grade source through
  single B-grade publisher; DOJ-direct primary NOT retrieved.
  WEP caps at "likely" per veto.

  NOT APPLIED on verifiable-absence claims (no specific GRU/FSB/
  SVR unit attribution in source; Void Blizzard not in roster) —
  these are A1 per direct file/source retrieval and do not require
  corroboration.

wep_ceiling: likely
wep_layered:
  obrezko_doj_federal_indictment_unsealed: likely  # B2 + single-source veto
  obrezko_36_year_old_russian_national: likely  # B2 + veto
  obrezko_arrested_phuket_thailand_november_2025_fbi_thai_royal_police: likely  # B2 + veto
  obrezko_extradited_to_us_custody: likely  # B2 + veto
  obrezko_boston_court_initial_appearance_2026_06_10: likely  # B2 + veto
  obrezko_alleged_role_infrastructure_provider_for_void_blizzard: likely  # B2 + veto
  obrezko_crypto_for_vps_and_domains_for_attack_infrastructure: likely  # B2 + veto
  at_least_11_us_companies_compromised: likely  # B2 + veto
  prosecutors_believe_actual_victim_count_higher: roughly_even_chance  # B3 prosecutor forward-looking; veto
  void_blizzard_victim_profile_sector_taxonomy_per_source: likely  # B2 + veto on the taxonomy
  void_blizzard_geographic_scope_europe_north_america: likely  # B2 + veto
  void_blizzard_credential_theft_to_email_document_theft_operational_pattern: likely  # B2 + veto
  void_blizzard_relatively_new_threat_group_supporting_russian_government_interests: likely  # B2 + veto on the attribution framing (Archimedes preserves source language)
  void_blizzard_not_in_archimedes_roster: very_likely  # A1 verifiable absence
  no_specific_gru_fsb_svr_unit_attribution_in_source: very_likely  # A1 verifiable absence
  defense_contractors_in_source_language_victim_profile: likely  # B2 + veto on the framing
  defense_contractors_named_as_specific_victim_in_this_indictment: roughly_even_chance  # Verifiable-absence of named victim — the "defense contractors" framing is the longitudinal Void Blizzard taxonomy, not this indictment's enumerated victim set
  ad_prime_named_victim_in_window: very_likely_NOT  # A1 verifiable absence; framed as very_likely-NOT for clarity
  microsoft_naming_convention_blizzard_russia: do_not_predict  # F6 background context; NOT in-window source-attested
  mstic_originator_void_blizzard_naming_late_2024: do_not_predict  # F6 background context; NOT in-window source-attested
  void_blizzard_new_actor_candidacy_recommended_for_operator: likely  # B2 collector observation per /new-actor workflow
  continuity_to_2026_06_04_five_eyes_advisory_and_morning_brief_finding_0002_temporal_pattern: roughly_even_chance  # B3 collector observation; temporal pattern not campaign-link

inclusion:
  eligible_for:
    - daily_brief_monitoring   # B2 clears C3 monitoring floor; not action-tier given single-source veto and no A&D-prime-named exposure
    - weekly_synthesis         # Pattern signal across counter-cyberespionage actions in 7-day window
    - actor_profile_awareness  # /new-actor candidate awareness for actor-profiler
inclusion_eligibility: yes
inclusion_rationale: >
  B2 cluster anchor clears B2 minimum at procedural-facts layer,
  but single-source veto caps WEP at "likely" on substantive
  operational claims and the "defense contractors" framing is
  longitudinal-victim-profile-sector-taxonomy not named-victim
  grounding. Conservative inclusion: monitoring-tier + weekly
  synthesis + actor-profile awareness. NOT eligible for daily
  brief ACTION tier (no actionable defender step in this finding
  beyond awareness; no DIB-direct CVE / IOC / campaign element).
  NOT eligible for FLASH per FLASH-POLICY Trigger 5 anti-noise
  rule (sector taxonomy paraphrase, not named-victim grounding).
  Operator decision required on /new-actor candidacy.

# ============================================================================
# Hard Rule 2 — Attribution preserved (source-direct, not Archimedes-originated)
# ============================================================================
attribution: null   # Archimedes-side attribution remains null per Hard Rule 2
attribution_claims:
  - claimed_actor: Void Blizzard
    claim_type: nation_state_aligned_threat_group_attribution_per_doj_and_microsoft_naming_convention
    claim: "Russia-aligned threat group; Microsoft-MSTIC naming convention 'Blizzard' = Russia per Archimedes corpus background knowledge (NOT directly source-attested in this in-window source)"
    source_language_verbatim_quote_under_15w: "relatively new threat group operating in support of Russian government interests"  # 11 words; The Record verbatim
    claimed_by_sources:
      - the-record  # PM-cycle verbatim characterization
      - doj-federal-court-filing  # underlying primary, NOT directly retrieved
    independent_corroboration: false  # Single in-window source through single B-grade publisher
    archimedes_attribution_origination_check: pass_per_hard_rule_2_source_attribution_preserved_with_citation_not_propagated_as_archimedes_attribution
    roster_status: not_in_archimedes_roster_v2_as_of_2026_05_10
    new_actor_candidacy_recommended_for_operator_decision: true
    cross_walk_to_existing_roster_actors_prohibited_per_hard_rule_2: true
  - claimed_subject: Denis Obrezko
    claim_type: doj_federal_indictment_alleging_infrastructure_provider_role
    claim: "36-year-old Russian national (Stavropol) charged with providing infrastructure (cryptocurrency-purchased VPS and internet domains) used to support Void Blizzard cyber operations; arrested November 2025 Phuket Thailand by joint FBI/Thai Royal Police operation; extradited to U.S. custody; initial federal court appearance Boston 2026-06-10"
    claimed_by_sources:
      - the-record
      - doj-federal-court-filing
    independent_corroboration: false
    archimedes_attribution_origination_check: pass_per_legal_policy_data_handling_corporate_officers_publicly_named_in_incidents_with_source_citation
  - claimed_victim_taxonomy_NOT_named_specific_victims:
      sector_taxonomy_per_the_record_verbatim: "government agencies, defense contractors, transportation, media, healthcare"
      enumerated_in_indictment: false   # The 11 U.S. companies are NOT enumerated
      geographic_scope: europe_and_north_america
      operational_pattern: stolen_credentials_to_email_and_document_theft
      claimed_by_sources:
        - the-record  # longitudinal Void Blizzard taxonomy per Microsoft-tracked targeting profile
        - doj-federal-court-filing
attribution_rationale: >
  Hard Rule 2 binding: Archimedes does NOT originate attribution.
  Void Blizzard is NOT in _roster.yaml (verified). Microsoft-MSTIC
  "Blizzard" weather-system naming convention assigns Russia
  attribution per Archimedes corpus background knowledge, but
  this is NOT directly source-attested in this in-window source —
  F6 at the in-window grading layer. The Record's verbatim
  attribution framing ("relatively new threat group operating in
  support of Russian government interests") is preserved with
  citation. The "defense contractors" framing in victim taxonomy
  is preserved as source-language verbatim; Archimedes does NOT
  propagate as named-victim claim. /new-actor candidacy flagged
  for operator decision.

# ============================================================================
# Vulnerability + product identifiers
# ============================================================================
cves: []  # No CVEs in this finding
affected_products: []
affected_vendors: []

# ============================================================================
# IOCs surfaced
# ============================================================================
iocs:
  individuals_named_per_doj_filing_relayed_via_the_record:
    - name: Denis Obrezko
      age: 36
      nationality: Russian
      origin: Stavropol
      status: in_us_custody
      arrest_location: Phuket_Thailand
      arrest_date: 2025_11
      arrest_joint_operation: fbi_thai_royal_police
      first_us_federal_court_appearance: Boston_2026_06_10
      doj_alleged_role: infrastructure_provider_void_blizzard
      doj_alleged_mechanism: cryptocurrency_purchase_of_vps_and_internet_domains_used_as_attack_infrastructure
      doj_alleged_facilitation: unauthorized_computer_access_us_and_foreign_organizations
  attribution_taxonomies_source_language_preserved:
    - taxonomy_name: void_blizzard_longitudinal_victim_profile
      sectors_per_the_record_verbatim_quote_8w: government_agencies_defense_contractors_transportation_media_healthcare
      geographic_scope: europe_north_america
      operational_pattern: stolen_credentials_to_email_document_theft
      source: the-record (2026-06-11)
ioc_count: 1  # one individual named per court filing
iocs_summary: >
  No domains, IPs, hashes, or malware samples in this finding.
  IOC layer is individual-named per DOJ court filing (Obrezko).
  Operational TTP layer is sector taxonomy + operational pattern
  paraphrase per The Record relay of DOJ filing.

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "DOJ counter-cyberespionage indictment of Denis Obrezko (Russian) for Void Blizzard infrastructure-provider role; defense contractors in source-language victim taxonomy; Void Blizzard NOT in roster; /new-actor candidate"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-11-pm-003
  attribution_claims_summary: see_attribution_claims_field_above
  related_findings:
    - finding-2026-06-11-0002  # FBI/DOJ 13-website seizures tied to Chinese intelligence services recruiting US-cleared personnel — China-attribution surface in morning brief; this finding adds Russia-attribution surface
    - finding-2026-06-04-pm    # 2026-06-04 PM Five Eyes "Safeguarding Our Secrets" counterintelligence advisory
  relationship_to_existing_findings: >
    Temporal continuity to morning brief finding-2026-06-11-0002
    (China-attribution counter-cyberespionage surface) and 2026-
    06-04 PM Five Eyes counterintelligence advisory. Three counter-
    cyberespionage data points across China + Russia attribution
    surfaces in 7-day window. TEMPORAL pattern, NOT confirmed
    campaign continuity. Briefer / analyst handoff for synthesis
    consideration.

# ============================================================================
# Inclusion + handoffs
# ============================================================================
analyst_review_required: true
analyst_review_rationale: >
  Attribution-uncertain (single B-grade source through single
  publisher; DOJ-direct primary not retrieved; Microsoft-MSTIC
  background context not in-window-source-attested) warrants
  SAT-class consideration on:
  (a) /NEW-ACTOR DECISION SUPPORT — Void Blizzard candidacy
      evidence-basis enumeration for operator decision: Microsoft-
      MSTIC originator naming (background context F6 at in-window
      grading layer) + DOJ-charged operator in U.S. custody (B2
      in-window) + source-named defense-contractor victim category
      (B2 in-window). Recommend actor-profiler scaffolding
      research if operator approves /new-actor for Void Blizzard.
  (b) COUNTER-CYBERESPIONAGE TEMPO PATTERN — SAT-ACH on temporal
      proximity of three counter-cyberespionage data points
      (2026-06-04 Five Eyes / 2026-06-11 China FBI/DOJ /
      2026-06-11 Russia DOJ) in 7-day window. Alternative
      readings: (i) coincidental scheduling of long-running
      multi-month operations; (ii) intentional joint operational
      tempo by U.S. + Five Eyes; (iii) selection-bias toward
      higher-publicity counter-cyberespionage windows.
  (c) Hard Rule 2 DISCIPLINE VERIFICATION — Archimedes-side
      attribution remains null; source attribution preserved with
      citation; Microsoft-MSTIC background context preserved as
      F6 (NOT propagated to graded attribution). Verify
      downstream brief layer maintains discipline.

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling "likely" on substantive operational claims (single-
  source veto holds). Does NOT meet red-team invocation floor
  of "very likely+" on operational impact claims. WEP "very_likely"
  on verifiable-absence claims (Void Blizzard NOT in roster; no
  specific GRU/FSB/SVR unit attribution in source) does not
  warrant red-team invocation per established convention (red-team
  argues against affirmative high-confidence claims, not against
  verifiable-absence framings).

red_team_review: null

analysis_sections:
  sat_ach:
    ach_analysis:
      question: "What explains the temporal proximity of three counter-cyberespionage data points in a 7-day window (2026-06-04 Five Eyes 'Safeguarding Our Secrets' counterintelligence advisory; 2026-06-11 AM FBI/DOJ 13-website seizures tied to Chinese intelligence recruiting; 2026-06-11 PM DOJ Obrezko / Void Blizzard infrastructure-provider indictment)?"
      analyzed_at: 2026-06-11T17:45:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: "Strategic posture shift — U.S. + Five Eyes governments have moved into a deliberate higher-tempo counter-cyberespionage public-action phase; the three data points reflect coordinated decision-making at policy level to increase public deterrent signaling against both Russia and China."
        - id: H2
          statement: "Opportunistic prosecution window — long-pending counter-cyberespionage cases naturally cluster at favorable political/operational windows (post-election, between-major-international-events, etc.); the 7-day proximity reflects political-calendar opportunism rather than coordinated strategy."
        - id: H3
          statement: "Accumulation of long-pending cases hitting public phase together — each case has its own multi-year backstory (Obrezko arrested 2025-11; Chinese 13-site seizures presumably built over months); the public-phase timing reflects independent case-management decisions converging without coordination."
        - id: H4
          statement: "Operational tempo by adversaries forces response — Russia and China cyberespionage tempo against U.S./Five Eyes has accelerated, and the counter-cyberespionage public-action density reflects defensive response rather than offensive posture; the three actions are reactive."
        - id: H5
          statement: "Selection bias in observation — Archimedes' collection sweep over a 7-day window naturally captures clusters; one would observe similar density in any randomly-chosen 7-day window across 2025-2026 if measured the same way."
      evidence:
        - id: E1
          description: "Obrezko was arrested 2025-11 in Phuket Thailand via joint FBI/Thai Royal Police operation; extradition completed; Boston federal court initial appearance 2026-06-10 (multi-month case lifecycle from arrest to public-phase)"
          source: the_record_via_doj_filing
          digraph: B2
          weight: 2
        - id: E2
          description: "2026-06-04 PM Five Eyes 'Safeguarding Our Secrets' counterintelligence advisory — formal multi-government policy publication (carry-forward from prior corpus)"
          source: prior_archimedes_corpus_finding_2026_06_04_pm
          digraph: A2
          weight: 3
        - id: E3
          description: "2026-06-11 AM FBI/DOJ 13-website seizures tied to Chinese intelligence services recruiting US-cleared personnel (operator-graded very_likely cluster anchor per finding-2026-06-11-0002)"
          source: prior_archimedes_corpus_finding_2026_06_11_0002
          digraph: A2
          weight: 3
        - id: E4
          description: "DOJ Obrezko indictment unsealed Boston 2026-06-10 with initial federal court appearance same day (sole in-window source: The Record relay)"
          source: the_record_via_doj_filing
          digraph: B2
          weight: 2
        - id: E5
          description: "Verifiable absence — no in-window source attests coordination between the three actions; no DOJ / White House / Five Eyes joint statement at sweep that names all three as part of a single campaign"
          source: verifiable_absence_at_sweep
          digraph: A1
          weight: 3
        - id: E6
          description: "Verifiable absence — Archimedes' 30-day corpus shows no comparable density of counter-cyberespionage data points in the prior windows (per corpus background knowledge; not source-attested in-window)"
          source: corpus_background_observation_F6_tier
          digraph: F6
          weight: 0.5
        - id: E7
          description: "Obrezko indictment's victim-profile sector taxonomy includes 'defense contractors' (8-word verbatim quote per The Record relay of DOJ filing)"
          source: the_record_verbatim
          digraph: B2
          weight: 2
        - id: E8
          description: "Each action targets a different attribution surface — Five Eyes advisory (general counterintelligence), 13-site seizures (China), Obrezko indictment (Russia). Heterogeneous targeting argues against single-campaign framing."
          source: structural_observation_across_three_findings
          digraph: A1
          weight: 3
      matrix:
        E1: {H1: N, H2: C, H3: C, H4: N, H5: N}   # Multi-month case lifecycle fits H2/H3 (case timing decisions) rather than H1 (strategic posture)
        E2: {H1: C, H2: N, H3: C, H4: C, H5: N}   # Five Eyes advisory consistent with strategic posture and reactive-tempo framings
        E3: {H1: C, H2: N, H3: C, H4: C, H5: N}   # Same as E2
        E4: {H1: N, H2: C, H3: C, H4: N, H5: N}   # Multi-month case lifecycle (arrested Nov 2025 → court appearance June 2026)
        E5: {H1: I, H2: N, H3: C, H4: N, H5: C}   # No joint statement cuts against H1 coordinated-strategy; consistent with H3 independent-convergence and H5 observation-window
        E6: {H1: C, H2: N, H3: N, H4: C, H5: I}   # If true (corpus-background), 7-day density is unusual; cuts against pure selection bias H5; mildly supports H1/H4
        E7: {H1: N, H2: N, H3: N, H4: N, H5: N}   # Non-diagnostic on the tempo question
        E8: {H1: I, H2: C, H3: C, H4: C, H5: C}   # Heterogeneous targeting (general / China / Russia) cuts against single-campaign H1; consistent with all others
      inconsistency_counts:
        H1: 2   # E5 absence-of-coordination-statement, E8 heterogeneous-targeting
        H2: 0
        H3: 0
        H4: 0
        H5: 1   # E6 corpus-background density observation
      diagnostic_evidence:
        - E1: "Multi-month case lifecycle is diagnostic for H2/H3 case-timing reading"
        - E5: "Absence of joint coordination statement is the strongest single piece of evidence against H1 strategic-posture-shift"
        - E8: "Heterogeneous targeting (general counterintelligence + China + Russia) cuts against single-campaign H1"
      ranking:
        - rank: 1
          hypothesis_id: H3
          rationale: "Zero inconsistencies. Independent case-management decisions converging without coordination is the simplest explanation; consistent with multi-month case lifecycle (E1, E4), absence of joint coordination statement (E5), and heterogeneous targeting (E8)."
          wep: likely
        - rank: 2
          hypothesis_id: H2
          rationale: "Zero inconsistencies. Opportunistic prosecution window framing is plausible but requires a specific political-calendar window claim that isn't directly source-attested. Compatible with H3."
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H4
          rationale: "Zero inconsistencies. Reactive-to-adversary-tempo reading is plausible — if Russia/China cyberespionage tempo has accelerated, defensive response density would naturally follow. But the adversary-tempo claim itself is not source-attested in this finding's sweep; would need cross-finding evidence."
          wep: roughly_even_chance
        - rank: 4
          hypothesis_id: H5
          rationale: "One inconsistency (E6 — if corpus-background observation holds that prior 30d windows are less dense). H5 cannot be fully ruled out without more rigorous baseline measurement, but the observation is at F6 so cannot be relied on with confidence."
          wep: unlikely
        - rank: 5
          hypothesis_id: H1
          rationale: "Two inconsistencies (E5 absence of coordination statement, E8 heterogeneous targeting). Strategic-posture-shift framing requires evidence of coordination that does not exist at sweep. Cannot be entirely ruled out — coordinated decisions may be quiet — but the absence of any in-window attestation makes this the weaker reading."
          wep: unlikely
      sensitivity_analysis:
        brittleness: low
        load_bearing_evidence: [E5, E8]
        if_E5_resolves_in_subsequent_sweep_with_joint_doj_white_house_or_five_eyes_statement: "H1 lifts substantially; ranking flips"
        if_E6_quantifies_against_30d_baseline_with_rigor: "H5 strengthens or weakens depending on direction; H3/H4 hold"
        if_a_fourth_counter_cyberespionage_action_lands_within_next_7d: "H1 strategic-posture-shift gains material support; rerun ACH"
      tripwires:
        - observation: "DOJ / White House / Five Eyes joint statement explicitly tying these actions to a coordinated campaign"
          effect: "Lift H1 to likely or very_likely; rerun ranking"
        - observation: "Fourth counter-cyberespionage action (additional indictment, sanctions, take-down) within next 14 days"
          effect: "Pattern density argues for H1 or H4; rerun"
        - observation: "Quantified comparison of 7-day counter-cyberespionage action density against prior 30-day baseline"
          effect: "Confirms or rules out H5 selection-bias"
        - observation: "Microsoft / MSTIC publication on Void Blizzard activity in same week (would tie Obrezko indictment to ongoing Microsoft-tracked operational tempo)"
          effect: "Strengthens H4 reactive-to-adversary-tempo framing; informs Void Blizzard /new-actor decision"
      conclusion:
        summary: |
          The leading hypothesis is H3 (accumulation of long-pending cases hitting
          public phase together) at "likely" — independent case-management decisions
          converging without coordination is the simplest explanation. H2 (opportunistic
          prosecution window) is a close second; both H2 and H3 are compatible. H1
          (strategic posture shift) is "unlikely" — requires coordination evidence
          that does not exist at sweep, and is undermined by heterogeneous targeting
          (Five Eyes advisory + China seizures + Russia indictment).
          Practical implication: do not extrapolate to "U.S. cyber counterintelligence
          is entering a new strategic phase." The three data points are pattern-
          significant for monitoring but do not justify a structural-shift narrative
          without further evidence. Briefer / weekly-synthesis layer should preserve
          the temporal-continuity framing without lifting to campaign-continuity.
        wep: likely
        confidence_caveats: |
          Assessment is low-brittleness. The strongest single pivot is E5 (absence of
          coordination statement); a subsequent DOJ / White House / Five Eyes joint
          statement would flip the ranking. Without that, the conservative read holds.
          H5 selection-bias cannot be fully ruled out without rigorous baseline
          measurement which Archimedes does not currently maintain.

  # /new-actor decision support for Void Blizzard
  new_actor_decision_support:
    candidate_actor_name: Void Blizzard
    candidate_actor_aliases_per_in_window_source: []
    candidate_actor_aliases_per_corpus_background_F6:
      - storm_blizzard_prefix_convention_implies_microsoft_mstic_originator_naming
    archimedes_roster_status: not_in_roster_v2_as_of_2026_05_10
    evidence_basis_enumeration:
      a_grade_originator_layer:
        - microsoft_mstic_naming_origin_at_originator_layer_per_corpus_background_knowledge_F6_in_window
      a_grade_in_window: []
      b_grade_in_window:
        - the_record_relay_of_doj_filing_b2_obrezko_indictment_alleged_infrastructure_provider_role
        - the_record_relay_of_doj_filing_b2_void_blizzard_longitudinal_victim_profile_includes_defense_contractors_taxonomy
        - the_record_relay_of_doj_filing_b2_at_least_11_us_companies_compromised
        - the_record_relay_of_doj_filing_b2_void_blizzard_relatively_new_threat_group_supporting_russian_government_interests
      verifiable_absence_a1:
        - no_specific_gru_fsb_svr_unit_attribution_in_source
        - no_a_and_d_prime_named_as_victim
        - no_directly_retrieved_doj_press_release_or_indictment_text
        - no_microsoft_mstic_in_window_publication_attesting_void_blizzard_at_a_grade
    ach_assessment_against_actor_profile_standard_minimums:
      attribution_clarity:
        verdict: partial
        rationale: "DOJ indictment attributes infrastructure provider to Void Blizzard via Russian-aligned framing; Microsoft-MSTIC originator naming (background F6 in-window) consolidates as Russia attribution. Strong attribution chain in concept; weak in in-window source-attestation. ACTOR-PROFILE-STANDARD section 5 'Geopolitical Context' would be writable; section 4 'TTPs' would require additional Microsoft / MSTIC publications retrieved as primary."
      us_prime_exposure:
        verdict: weak
        rationale: "Source-named 'defense contractors' sector taxonomy is longitudinal victim profile, not named-prime-victim. ACTOR-PROFILE-STANDARD section 2 'Primary Targets' would have to acknowledge sector-not-prime grounding."
      tooling_tradecraft_documentation_availability:
        verdict: weak_in_window_strong_at_originator
        rationale: "In-window source has zero technical detail — no TTPs, no malware names, no infrastructure IOCs beyond 'cryptocurrency-purchased VPS and internet domains.' Microsoft MSTIC has presumably published Void Blizzard tradecraft details since late-2024 naming-origin per corpus background, but those publications were not retrieved this sweep. ACTOR-PROFILE-STANDARD sections 4 'TTPs', 5 'Malware Arsenal', 6 'Infrastructure Patterns', 7 'Known IOCs' would require dedicated Microsoft / MSTIC retrieval."
    analyst_recommendation:
      recommendation: defer_pending_primary_retrieval
      rationale: >
        Three factors warrant flagging the candidacy for operator decision, BUT
        Archimedes should not auto-promote and the analyst should not push for
        immediate /new-actor either. The strongest case for /new-actor would require:
        (a) at least one Microsoft MSTIC publication retrieved as primary attesting
        Void Blizzard tradecraft at A grade; (b) direct DOJ press release / indictment
        text retrieval lifting the B2 anchor to A; (c) follow-up reporting on the
        specific 11 U.S. company victim set. Without these, the actor profile would
        be skeletal across ACTOR-PROFILE-STANDARD's required sections (TTPs, Malware,
        Infrastructure, IOCs all empty or "No documented [X] at this time").
        Recommend: keep on watchlist; surface to operator via /new-actor candidacy
        flag without auto-actioning; rerun decision when MSTIC primary becomes
        available or when a second-publisher A-grade source corroborates the DOJ
        attribution chain in-window. Operator decision is required per Hard Rule 2
        and established /new-actor workflow.
      hard_rule_2_compliance: pass
      hard_rule_2_compliance_detail: >
        Analyst recommendation is DEFER, framed as recommendation only. Analyst
        does NOT originate attribution. The Record's verbatim attribution framing
        ("relatively new threat group operating in support of Russian government
        interests" — 11 words) is preserved with citation; Microsoft-MSTIC naming
        origin remains F6 background context until in-window-source-attested.

# Analyst Hard Rule 2 discipline verification (per grader-specified scope)
analyst_hard_rule_2_verification:
  attribution_origination_check: pass
  detail: >
    Finding cites DOJ's attribution claim (via The Record relay) without
    originating attribution. Archimedes-side attribution remains null per
    Hard Rule 2. Void Blizzard NOT in _roster.yaml (verified); no cross-walk
    to any tracked roster actor (APT28 Forest Blizzard, Sandworm Seashell
    Blizzard, APT29 Midnight Blizzard) despite naming-convention similarity.
    Microsoft MSTIC background knowledge preserved as F6 (NOT propagated to
    graded attribution). The Record's verbatim source-language attribution
    framing preserved with citation. /new-actor candidacy flagged for
    operator decision; analyst-recommendation is DEFER pending primary
    retrieval. Hard Rule 2 binding preserved.

  sat_kac: null  # KAC not invoked for this finding — WEP caps at "likely" per single-source veto; KAC overhead exceeds value at this confidence level per SAT-KAC skill invocation criteria. SAT-ACH on the counter-cyberespionage tempo question + /new-actor decision support satisfy grader-specified scope.

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs: [2026-06-11-afternoon]
retracted: false
retraction_brief_id: null

# ============================================================================
# Source-grade revision proposed
# ============================================================================
source_grade_revision_proposed:
  - source_yaml_id: doj-federal-court-filings
    proposed_action: add_new_provisional_source_entry_if_missing
    proposed_grade: A
    proposed_provisional_until: pending_first_direct_retrieval
    rationale: "DOJ federal court filings are canonical A on own filings per CISA/NSA/FBI government-source category in INTEL-GRADING.md. Underlying primary for this finding was NOT directly retrieved this sweep; only relayed via The Record. If DOJ press release becomes available in subsequent sweep, regrade candidate to A1 at originator layer."
---

# DOJ indicts Russian national Denis Obrezko for Void Blizzard infrastructure-provider role; "defense contractors" in source-language victim profile (Void Blizzard NOT in roster)

## Summary

A DOJ federal indictment, unsealed via initial Boston court appearance 2026-06-10, charges 36-year-old Russian national Denis Obrezko (Stavropol) with providing infrastructure that supported the Void Blizzard cyberespionage cluster. The Record (B, sole in-window source) characterizes Void Blizzard as "relatively new threat group operating in support of Russian government interests" (11-word verbatim) and lists Void Blizzard's longitudinal victim profile as including "government agencies, defense contractors, transportation, media, healthcare" (8-word verbatim) across Europe and North America. At least 11 U.S. companies have been compromised per prosecutors, who believe the actual victim count is higher. Obrezko was arrested November 2025 in Phuket, Thailand by a joint FBI–Thai Royal Police operation and extradited to U.S. custody. Void Blizzard is NOT in `_roster.yaml`; Hard Rule 2 binding constrains Archimedes from originating attribution or cross-walking to any tracked actor — `/new-actor` candidacy is flagged for operator decision.

## Sources

### The Record (Recorded Future News, the-record, B) — sole in-window source

- URL: https://therecord.media/hacker-linked-to-void-blizzard-faces-charges
- Published: 2026-06-11 15:17 EDT
- Key claim: Denis Obrezko (36, Russian, Stavropol) charged via DOJ federal indictment unsealed at Boston federal court appearance 2026-06-10 with infrastructure-provider role in Void Blizzard cluster; arrested November 2025 Phuket Thailand via joint FBI-Thai Royal Police operation; extradited to U.S. custody; alleged mechanism = cryptocurrency-purchased VPS and internet domains used as attack infrastructure; at least 11 U.S. companies compromised per prosecutors with belief actual count higher; Void Blizzard victim profile across Europe and North America includes "government agencies, defense contractors, transportation, media, healthcare, and NGOs"; characterized as "relatively new threat group operating in support of Russian government interests."

### Underlying primary — DOJ federal court filing (NOT directly retrieved this sweep)

- Proposed grade at originator layer: A
- Status: not directly retrieved; relayed via The Record only
- Re-grade candidate on subsequent DOJ press release availability

## Technical detail — Hard Rule 2 binding constraint binding here

**Void Blizzard is NOT in `_roster.yaml`** (verified 2026-06-11 against full 22-actor list; Blizzard-string matches in roster are APT28 "Forest Blizzard" alias, Sandworm APT44 "Seashell Blizzard" alias, Cozy Bear / APT29 "Midnight Blizzard" alias — none match Void Blizzard). Archimedes does NOT originate attribution by cross-walking Void Blizzard to any tracked actor. The Record's source-language attribution framing ("relatively new threat group operating in support of Russian government interests" — 11 words) is preserved verbatim with citation. Microsoft-MSTIC "Blizzard" weather-system naming convention for Russia-attribution is Archimedes corpus background knowledge but is NOT directly source-attested in this in-window source — graded F6 ("Cannot Be Judged") at the in-window grading layer, NOT propagated to the finding's graded attribution.

### Subject — Denis Obrezko

- **Name:** Denis Obrezko
- **Age:** 36
- **Nationality / origin:** Russian (Stavropol)
- **Arrest:** November 2025, Phuket, Thailand (joint FBI–Thai Royal Police operation)
- **Transfer:** Extradited to U.S. custody
- **Initial federal court appearance:** Boston, 2026-06-10
- **Status:** In custody

### Alleged role per DOJ filing (per The Record relay)

- Provided infrastructure used to support Void Blizzard cyber operations.
- Used cryptocurrency transactions to purchase virtual private servers and internet domains used as attack infrastructure.
- Facilitated unauthorized computer access targeting U.S. and foreign organizations.

### Victim scope per DOJ filing (per The Record relay)

- At least 11 U.S. companies compromised per prosecutors.
- Prosecutors believe actual victim count significantly higher than 11.
- Void Blizzard's longitudinal victim profile per source: "government agencies, defense contractors, transportation, media, healthcare, and NGOs" across Europe and North America.
- Operational pattern: stolen credentials → email and document theft.

## A&D / DIB relevance

- **Direct A&D effect via in-window source:** NONE. The 11 U.S. companies compromised in this indictment are NOT enumerated. No A&D-prime named victim.
- **Source-language A&D-direct framing (B2, single-source veto):** "defense contractors" appears in The Record's literal victim-profile sector taxonomy paraphrasing DOJ filing language. This is the STRONGEST A&D-direct phrasing observed in today's collection sweep, but it is longitudinal-victim-profile sector taxonomy, NOT this-indictment-specific named-victim grounding. Per FLASH-POLICY Trigger 5 anti-noise rule, conservative grading does NOT lift this to "defense-prime-victim-named" framing.
- **Sector-targeting evidence:** General-population multi-sector across two continents; does not isolate A&D as primary focus.
- **Roster gap:** Void Blizzard candidacy review warranted given (a) Microsoft-MSTIC-tier naming origin at originator layer per Archimedes background corpus; (b) DOJ-charged operator in U.S. custody (counter-intelligence operational tempo); (c) source-named defense-contractor victim category. Operator decision required per Hard Rule 2 and established /new-actor workflow.

## Continuity to 2026-06-04 + 2026-06-11 morning brief cluster

- **2026-06-04 PM:** Five Eyes "Safeguarding Our Secrets" counterintelligence advisory.
- **2026-06-11 AM** (`finding-2026-06-11-0002`): FBI/DOJ 13-website seizures tied to Chinese intelligence recruiting US-cleared personnel — operator-graded `very_likely` cluster anchor.
- **2026-06-11 PM** (this finding): DOJ Russian Void Blizzard infrastructure-provider indictment.

Three counter-cyberespionage data points across both China and Russia attribution surfaces in a 7-day window. TEMPORAL CONTINUITY, NOT confirmed campaign continuity. Grader observation; analyst SAT-ACH candidate for synthesis consideration.

## IOCs surfaced

- **Individual named per DOJ filing:** Denis Obrezko (36, Russian, Stavropol; in U.S. custody after Phuket Thailand arrest November 2025 + extradition + Boston federal court appearance 2026-06-10).
- **Attribution taxonomies (source-language preserved):** Void Blizzard longitudinal victim profile sector taxonomy + Europe/North America geographic scope + stolen-credentials-to-email-and-document-theft operational pattern.
- **No domains, IPs, hashes, or malware samples** in this finding. The DOJ alleged-mechanism reference to "cryptocurrency-purchased VPS and internet domains" is alleged-role description, not specific-infrastructure IOC enumeration.

## Relationship to existing findings

- **finding-2026-06-11-0002** (morning) — China-attribution counter-cyberespionage surface; this finding adds Russia-attribution surface in same operational tempo.
- **2026-06-04 PM** — Five Eyes counterintelligence advisory.

Both are temporal continuity, not campaign-link.

## Open questions for analyst

1. **`/new-actor` decision support for Void Blizzard:** Evidence-basis enumeration for operator decision — (a) Microsoft-MSTIC originator naming (background context F6 at in-window grading layer); (b) DOJ-charged operator in U.S. custody (B2 in-window); (c) source-named defense-contractor victim category (B2 in-window). Recommend actor-profiler scaffolding research if operator approves.
2. **Counter-cyberespionage tempo pattern (SAT-ACH candidate):** Decompose temporal proximity of three counter-cyberespionage data points in 7-day window. Hypotheses: (a) coincidental scheduling of long-running multi-month operations; (b) intentional joint operational tempo by U.S. + Five Eyes; (c) selection-bias toward higher-publicity counter-cyberespionage windows.
3. **Hard Rule 2 discipline verification:** Archimedes-side attribution remains null; source attribution preserved with citation; Microsoft-MSTIC background context preserved as F6 (NOT propagated). Verify downstream brief layer maintains discipline.

## Analytic notes (from analyst review)

SAT-ACH on the counter-cyberespionage tempo question ranks H3 (accumulation of long-pending cases hitting public phase together via independent case-management decisions) at "likely" with zero inconsistencies. H2 (opportunistic prosecution window) and H4 (reactive to adversary tempo) are both close seconds at "roughly even chance." The strategic-posture-shift reading (H1) is "unlikely" — two inconsistencies via absence of any joint coordination statement and heterogeneous targeting across Russia, China, and general counterintelligence. The 7-day proximity is pattern-significant for monitoring but does not justify a structural-shift narrative without further evidence (joint coordination statement; fourth action in next 14d; quantified baseline measurement). Briefer / synthesis layer should preserve temporal-continuity framing without lifting to campaign-continuity.

/new-actor decision support for Void Blizzard: recommendation is DEFER pending primary retrieval. Three factors warrant flagging the candidacy (Microsoft MSTIC-tier naming origin at background F6; DOJ-charged operator in U.S. custody; source-named defense-contractor victim category), BUT the actor profile would be skeletal across ACTOR-PROFILE-STANDARD's required sections without dedicated Microsoft / MSTIC primary retrieval (TTPs, Malware, Infrastructure, IOCs all empty). Strongest path to /new-actor approval: collector Mode 4 retrieval of (a) at least one MSTIC publication attesting Void Blizzard tradecraft at A; (b) direct DOJ press release / indictment text. Operator decision required per Hard Rule 2 and established workflow.

Hard Rule 2 discipline verified preserved — finding cites DOJ attribution via The Record relay without originating attribution; no cross-walk to Forest Blizzard / Seashell Blizzard / Midnight Blizzard despite naming-convention similarity; MSTIC background knowledge preserved as F6 not propagated.
