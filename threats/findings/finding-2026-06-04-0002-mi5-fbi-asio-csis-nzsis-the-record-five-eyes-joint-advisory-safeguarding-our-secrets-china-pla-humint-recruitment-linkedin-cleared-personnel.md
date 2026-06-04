---
finding_id: finding-2026-06-04-0002-mi5-fbi-asio-csis-nzsis-the-record-five-eyes-joint-advisory-safeguarding-our-secrets-china-pla-humint-recruitment-linkedin-cleared-personnel
created_at: 2026-06-04T16:24:00-04:00
graded_by: grader
grading_run_id: afternoon-20260604-160000
grading_mode: scheduled_brief
test: false
status: graded

# Core grading (admiralty-grading skill output)
digraph: A2
digraph_layered:
  five_eyes_joint_counterintelligence_advisory_safeguarding_our_secrets_published_2026_06_04: A1   # Joint government counterintelligence advisory; verifiable via direct URL retrieval at mi5.gov.uk; canonical-by-definition
  advisory_attribution_verbatim_chinas_military_intelligence_services: A1   # Vendor-on-own-attestation by five government counterintelligence services; canonical at the attestation layer
  named_tradecraft_linkedin_front_companies_virtual_interviews_encrypted_messaging_unconventional_payment: A1   # Government counterintelligence service attesting to own observed tradecraft; canonical
  named_target_set_government_military_personnel_cleared_personnel_indo_pacific_stationed_military_academics_journalists_think_tank_staff: A1   # Government counterintelligence service attesting to own observed target set; canonical
  payment_range_100s_to_1000s_per_intelligence_report: A1   # Government counterintelligence service attesting to own observed financial-incentive layer; canonical
  the_record_independent_publisher_relay_with_byline_caveat: B2   # Recorded Future Media relay; publisher-independent of MI5/FBI/ASIO/CSIS/NZSIS; first surface of advisory in trade press at sweep
  dib_cleared_personnel_population_within_implicit_target_scope_per_anyone_with_access_to_classified_or_privileged_information: A2   # Five Eyes scope language "anyone with access to classified or privileged information" implicit includes DIB cleared-personnel; grader-side inference at A-grade on the inclusion claim; capped at A2 because DIB-prime-explicit-naming absent
  indo_pacific_program_teams_direct_relevance_b21_b1b_f22_f35_gmd_thaad_aegis_bmd_submarine_shipbuilding: A2   # Five Eyes explicit Indo-Pacific stationed military call-out direct-relevance to A&D primes with INDOPACOM-customer programs; grader-side inference at A-grade on the relevance claim; capped at A2 because A&D-prime-explicit-naming absent
  specific_a_and_d_prime_targeted_in_active_recruitment_cell: F6   # No named-victim disclosure in advisory; grader cannot assess; F6 cannot-be-judged
  no_specific_tracked_actor_in_roster_named_volt_typhoon_salt_typhoon_apt40_apt41_all_pla_attributed_but_none_named: A1   # Verifiable absence in advisory and The Record relay
  no_cyber_ttp_named_in_advisory_humint_led_counterintelligence: A1   # Mechanism class HUMINT not cyber; verifiable from advisory
  parsimonious_threat_class_pla_strategic_support_force_or_pla_intelligence_bureau_units_via_industry_understanding: C3   # Grader-side structural inference; PLA intelligence apparatus mapping at industry-understanding C3 layered; NOT Archimedes-originated attribution because preserves the advisory's generic attribution
  cluster_anchor: A2

digraph_anchor: >
  Cluster anchored on the Five Eyes joint counterintelligence
  advisory "Safeguarding Our Secrets" (MI5 lead agency,
  FBI/ASIO/CSIS/NZSIS co-authors, PDF published 2026-06-04 on
  mi5.gov.uk) + The Record (Recorded Future Media) trade-press
  relay (2026-06-04 18:04 UTC = 14:04 EDT in-window). New
  source-id `mi5-fbi-asio-csis-nzsis-joint` proposed to librarian
  for source-grades.yaml addition.

  A2 (not A1 or B2) anchored because:

    - SOURCE LETTER GRADE: Five Eyes joint counterintelligence
      advisory at A-grade procedurally per the same precedent
      class as CISA / NSA / FBI Flash / NCSC — five-government-
      intelligence-service joint authorship is the highest-
      credibility public counterintelligence source class
      available. New source-id `mi5-fbi-asio-csis-nzsis-joint`
      proposed at provisional A; pending source-grade-log entry
      + source-grades.yaml addition by librarian (72h ratification
      clock to 2026-06-07T16:24:00-04:00). The Record pre-
      assigned B per source-grades.yaml (ratified).

    - INDEPENDENCE TEST: Two source publishers. Five Eyes joint
      advisory PDF is the primary; The Record is a publisher-
      independent trade-press relay. Publisher-independence
      holds (two different organizations; The Record cites the
      advisory as origin). Evidence-basis-independence: the Five
      Eyes joint advisory IS the canonical evidence basis for
      attestation about own counterintelligence observations.
      The Record cannot add independent telemetry on a
      counterintelligence-service-on-own-observed-activity claim
      by definition.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed): Procedural facts (advisory exists,
        five-service joint authorship, verbatim attribution
        language "China's military intelligence services", named
        tradecraft, named target set) — PASS at the government-
        counterintelligence-service-on-own-observed-activity
        canonical layer. The Record + the advisory together
        satisfy the publisher-independence test. BUT the
        substantive operational claim layer (campaign is active,
        targets DIB cleared-personnel, scale across five-country
        footprint) is single-source-at-the-advisory-layer with
        a publisher-independent relay; this is the same precedent
        as Cisco PSIRT + THN+BleepingComputer triangle.
      * Grade 2 (Probably True): ASSIGNS — Five Eyes attestation
        is consistent with established PLA HUMINT tradecraft per
        prior public DIA / NCSC / CISA / DCSA insider-threat
        bulletins on Chinese intelligence services; no
        contradicting A/B-grade source; technical-tradecraft
        claims (LinkedIn approach + front companies + virtual
        interviews + encrypted-messaging transitions +
        unconventional payments) are internally coherent and
        consistent with the historical PLA / MSS HUMINT pattern
        documented across two decades of US counterintelligence
        cases.

    - SUBSTANTIVE CLAIM CLASS is HUMINT-led counterintelligence,
      NOT cyber-TTP. Distinguishes from cyber-CTI standard
      surface. Per operator judgment, counterintelligence-adjacent
      material IS in-scope for an A&D-target-profile audience
      because DCSA / FSO / insider-threat partnership is a
      legitimate defensive lever even when the mechanism is
      HUMINT not cyber.

    - HARD RULE 2 COMPLIANCE STRESS-TESTED: Five Eyes attributes
      verbatim to "China's military intelligence services" —
      phrasing connotes PLA-linked (military intelligence
      apparatus) rather than civilian intelligence (MSS /
      Ministry of State Security). No specific PLA unit, no
      specific tracked-actor in `_roster.yaml` is named. Volt
      Typhoon (#008), Salt Typhoon (#010), APT40 (#017), APT41
      (#019) are all PLA / China-affiliated and present in the
      roster but none is named in this advisory. Grader
      PRESERVES the verbatim Five Eyes attribution and does
      NOT upgrade to specific tracked-actor mapping. Hard Rule
      2 (no first-time attribution origination) holds.

  Single-source veto APPLIED on operational claim that "a
  specific A&D prime is targeted in any active recruitment cell"
  (no named-victim disclosure in this advisory; grader cannot
  assess; layered F6). NOT applied on government-
  counterintelligence-service-on-own-observed-activity canonical
  layer for procedural facts or the named tradecraft / target
  set claims.

  Hard Rule 2: PRESERVED — verbatim Five Eyes attribution
  language preserved ("China's military intelligence services");
  no upgrade to specific tracked-actor mapping.

  Hard Rule 3: PRESERVED — HUMINT advisory; no PoC content;
  no cyber-attack-tooling described.

  Hard Rule 6: PRESERVED — no direct quotes from Five Eyes
  PDF surfaced in finding body text beyond the verbatim
  attribution phrase ("China's military intelligence services",
  5 words) and the verbatim target-set phrase ("anyone with
  access to classified or privileged information", 8 words).
  Both under 15-word limit. The Record relay paraphrased.

  Hard Rule 8: Splunk first-party check ran (-30d sweep on PLA
  + LinkedIn + Five Eyes + Safeguarding Our Secrets + Chinese
  military intelligence + MI5 superset across defenseclaw_local
  + archimedes-NOT-archimedes-internal). 0 events. Per Hard
  Rule 8 silence is not disconfirming. HUMINT-tradecraft
  signals would not surface in cyber-security telemetry by
  definition.

source_reliability:
  grade: A
  source_name: "Five Eyes joint counterintelligence advisory — 'Safeguarding Our Secrets' (MI5 lead, FBI / ASIO / CSIS / NZSIS co-authors) — government-counterintelligence-service-on-own-observed-activity primary; The Record (Recorded Future Media) publisher-independent trade-press relay"
  source_yaml_id: mi5-fbi-asio-csis-nzsis-joint
  grade_rationale: >
    NEW source-id proposed at provisional A per the same
    precedent class as CISA / NSA / FBI Flash / NCSC — five-
    government-intelligence-service joint authorship is the
    highest-credibility public counterintelligence source class
    available. Source-grade-log entry + source-grades.yaml
    addition required by librarian (handoff field below). 72h
    ratification clock to 2026-06-07T16:24:00-04:00.
  provisional: true
  cluster_secondary_sources:
    - source_yaml_id: the-record
      grade: B
      provisional: false
      grade_rationale: "Pre-assigned B per source-grades.yaml (ratified); publisher-independent trade-press relay of Five Eyes joint advisory primary"
      role: relay

credibility:
  grade: 2
  checklist_passed:
    - probably_true_government_counterintelligence_service_on_own_observed_activity_attestation_consistent_with_established_pla_humint_tradecraft
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_tradecraft_claims_internally_coherent_with_historical_pla_mss_humint_pattern
    - probably_true_consistent_with_prior_public_dia_ncsc_cisa_dcsa_insider_threat_bulletins_on_chinese_intelligence_services
  rationale: >
    Five Eyes joint advisory attestation: advisory exists at
    mi5.gov.uk; five-service joint authorship; verbatim
    attribution "China's military intelligence services" (PLA-
    linked, not MSS); named tradecraft (LinkedIn primary
    platform, front companies posing as consultancies / think
    tanks / HR firms, virtual interviews with role-and-unit
    probing, encrypted-messaging transitions, payment $100s-
    $1000s per intelligence report); named target set
    (government / military personnel, Indo-Pacific stationed
    military explicitly, academics / journalists / think-tank
    staff with "indirect or peripheral access", "anyone with
    access to classified or privileged information"). The
    Record is publisher-independent trade-press relay confirming
    the advisory content but cannot add independent telemetry
    on a counterintelligence-service-on-own-observed-activity
    claim. Substantive tradecraft and target-set claims are
    internally coherent and consistent with historical PLA /
    MSS HUMINT pattern documented across two decades of US
    counterintelligence cases. No contradicting A/B-grade
    source.

corroboration:
  independent_sources:
    - mi5-fbi-asio-csis-nzsis-joint
    - the-record
  independent: partial
  test_passed: >
    Publisher-independence holds: Five Eyes joint advisory
    (mi5.gov.uk PDF) + The Record (Recorded Future Media) are
    two different publishing organizations. The Record cites
    the advisory as origin but contributes the Jun 4 18:04 UTC
    timestamp + trade-press editorial framing. Five-government-
    intelligence-service joint authorship internally satisfies
    the cross-service independence test for the advisory itself.
  test_failed: >
    Evidence-basis-independence at the operational-claim layer
    FAILS in the strict skill-Step-4 sense: The Record relay
    cannot add independent telemetry on a counterintelligence-
    service-on-own-observed-activity claim by definition. For
    substantive operational content (campaign scale, target-set
    detail, tradecraft specifics), the relay adds publisher-
    cross-reference but not telemetry-cross-reference. Single-
    source veto applies on CLAIMS about specific operational
    reach into A&D programs (no named-victim disclosure in
    advisory; grader cannot assess). Does NOT apply on
    PROCEDURAL facts at government-counterintelligence-service-
    on-own-observed-activity canonical layer.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    -30d sweep across defenseclaw_local + (archimedes NOT
    sourcetype=archimedes:*) on PLA + LinkedIn + Five Eyes +
    Safeguarding Our Secrets + Chinese military intelligence +
    MI5 superset. 0 events. Per Hard Rule 8 silence is not
    disconfirming. HUMINT-tradecraft signals would not surface
    in cyber-security telemetry by definition — first-party
    visibility on this campaign would require insider-threat /
    DCSA-partnership channels, not cyber-IOC matches.

single_source_veto_applied: true
single_source_veto_detail: >
  Applied on the operational claim that "a specific A&D prime
  is targeted in any active recruitment cell" (no named-victim
  disclosure in advisory; layered F6 cannot-be-judged). NOT
  applied on government-counterintelligence-service-on-own-
  observed-activity canonical layer for procedural facts
  (advisory exists, verbatim attribution, named tradecraft,
  named target set). WEP ceiling capped at "likely" on the
  specific-A&D-prime-targeted layer; remains "very likely" on
  procedural facts and the implicit-target-scope inclusion of
  DIB cleared-personnel.

wep_ceiling: likely
wep_layered:
  five_eyes_joint_advisory_exists_at_mi5_gov_uk_with_five_service_joint_authorship: very_likely   # Government canonical
  verbatim_attribution_chinas_military_intelligence_services_pla_linked_not_mss: very_likely   # Government counterintelligence service-on-own-attestation canonical
  named_tradecraft_linkedin_front_companies_virtual_interviews_encrypted_messaging_unconventional_payment: very_likely   # Government counterintelligence service-on-own-observed-activity canonical
  named_target_set_government_military_personnel_cleared_personnel_indo_pacific_stationed_military_academics_journalists_think_tank_staff: very_likely   # Government counterintelligence service-on-own-observed-activity canonical
  dib_cleared_personnel_population_within_implicit_target_scope: likely   # A-grade source attesting; implicit scope inclusion via "anyone with access to classified or privileged information" + Indo-Pacific stationed military framing
  indo_pacific_program_teams_direct_relevance_b21_b1b_f22_f35_gmd_thaad_aegis_bmd_submarine_shipbuilding: likely   # Grader-side structural inference per CLAUDE.md target profile; A-grade source attesting to Indo-Pacific framing
  specific_a_and_d_prime_targeted_in_any_active_recruitment_cell: unable_to_assess   # F6 layered; no named-victim disclosure
  no_specific_tracked_actor_named_in_advisory: very_likely   # Verifiable absence
  hard_rule_2_preservation_no_tracked_actor_upgrade: very_likely   # Grader discipline; verifiable

inclusion:
  eligible_for:
    - daily_brief_monitoring   # A2 above C3 monitoring floor; counterintelligence-adjacent material in-scope per operator judgment
    - weekly_synthesis
  not_eligible_for:
    - flash   # No cyber-TTP active campaign; no tracked-actor attribution; per 12:00 FLASH sentinel evaluation no triggers fire
    - daily_brief_action   # No immediate cyber-defensive action triggered; FSO / DCSA channel partnership is the operational pivot, which is monitoring-tier framing
    - actor_profile_update   # Hard Rule 2 preserves verbatim "China's military intelligence services"; no specific roster actor named; no tracked-actor profile update justified

# Cluster metadata
cluster:
  topic: >
    Five Eyes joint counterintelligence advisory "Safeguarding
    Our Secrets" (MI5 lead agency; FBI / ASIO / CSIS / NZSIS
    co-authors; PDF published 2026-06-04 on mi5.gov.uk) plus
    The Record (Recorded Future Media) publisher-independent
    trade-press relay. Advisory attributes verbatim to "China's
    military intelligence services" (PLA-linked, not MSS) for
    HUMINT recruitment operations against personnel in Five
    Eyes nations holding security clearances or access to
    classified or privileged information. Named tradecraft:
    LinkedIn as primary platform; front companies posing as
    consultancies / think tanks / HR firms; virtual interviews
    with role-and-unit probing questions; encrypted-messaging
    transitions; payment $100s-$1000s per intelligence report.
    Named target set: government / military personnel, Indo-
    Pacific stationed military explicitly, academics /
    journalists / think-tank staff with "indirect or peripheral
    access", "anyone with access to classified or privileged
    information". HUMINT-led counterintelligence, NOT cyber-
    TTP. DIB cleared-personnel population within implicit
    target scope; A&D primes with INDOPACOM-customer programs
    direct-relevance via Indo-Pacific framing.
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-04-pm-002-therecord-mi5-fbi-asio-csis-nzsis-five-eyes-safeguarding-our-secrets-china-pla-humint-linkedin-recruitment
  attribution_claims:
    - claimed_actor: "China's military intelligence services (PLA-linked, not MSS; verbatim from Five Eyes joint advisory)"
      claim_text: >
        Five Eyes attribution language verbatim: "China's
        military intelligence services". Phrasing connotes
        PLA-linked (military intelligence apparatus) rather
        than civilian intelligence (MSS / Ministry of State
        Security). No specific PLA unit named. No specific
        tracked-actor in `_roster.yaml` named (Volt Typhoon,
        Salt Typhoon, APT40, APT41 all PLA / China-affiliated
        but none referenced in advisory). The Record explicitly
        notes the absence of named threat-actor.
      claimed_by_sources:
        - mi5-fbi-asio-csis-nzsis-joint
        - the-record
      requires_analyst_review: true
      hard_rule_2_status: >
        PRESERVED — verbatim Five Eyes attribution language
        preserved; no upgrade to specific tracked-actor mapping
        (Volt Typhoon / Salt Typhoon / APT40 / APT41 etc.). Per
        Hard Rule 2 grader does NOT originate attribution; Five
        Eyes generic attribution to PLA military intelligence
        services is preserved verbatim. Analyst review flagged
        for potential FSO / DCSA / insider-threat framing for
        target-profile audience (not for attribution upgrade).

related_vulnerabilities: []
related_actors: []   # No specific tracked actor named per Hard Rule 2; advisory generic-PLA-attribution preserved verbatim
related_campaigns: []   # No specific named campaign; advisory describes ongoing HUMINT recruitment activity at strategic scope
update_on: null

# Downstream handoff flags
analyst_review_required: true
analyst_review_rationale: >
  Hard Rule 2 attribution preservation context (Five Eyes
  generic-PLA-attribution; analyst should examine whether any
  tracked-actor cross-reference is appropriate without
  originating attribution). Operationally significant
  counterintelligence-adjacent material for target-profile
  audience — analyst should consider FSO / DCSA / insider-
  threat partnership framing in monitoring-tier brief surface.
  WEP ceiling at "likely" on operational DIB-cleared-personnel
  implications; analyst SAT-ACH on the question "is the DIB
  cleared-personnel population materially in target scope
  versus general cleared-personnel population" may sharpen
  the brief framing. No SAT-KAC trigger condition (assumption
  layer is at the implicit-target-scope inclusion of DIB,
  which the operator's judgment has already settled).

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling at "likely" on operational layer does not meet
  red-team invocation floor ("very likely" or higher). The
  procedural-facts layer at "very_likely" is vendor-on-own-
  attestation canonical (government counterintelligence service
  attesting to own observed activity), not analyst-predictive
  class.

red_team_review: null

# Analyst SAT run — analyst subagent
analyst_review_complete: true
analyst_review_run_id: analyst-20260604-164500
analyst_review_run_at: 2026-06-04T16:45:00-04:00
wep_ceiling_adjusted: likely   # unchanged from grader's ceiling; operational layer remains "likely" per analyst SAT
wep_ceiling_adjustment_reason: >
  Analyst SAT confirms grader's operational-layer "likely" ceiling is
  calibrated correctly — the implicit-target-scope inference from "anyone
  with access to classified or privileged information" + Indo-Pacific
  stationed military framing to DIB cleared-personnel survives KAC's
  Centrality/Confidence test, but two material caveats (HR4 corporate-
  recruiter/HR-due-diligence pivot AND the framing being implicit not
  explicit on DIB-prime naming) should be carried verbatim in the brief.
  No WEP movement is warranted; qualifying caveats applied.

assessment_blocked_pending_test: false   # KAC produced no Test classifications; one assumption qualifies, none blocks
test_required: null

red_team_review_required: false   # WEP ceiling at "likely" remains below the "very_likely" red-team floor

analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        How should an A&D-target-profile reader (mid-to-large US
        aerospace and defense contractor — ITAR-regulated, cleared-
        personnel population, USG contract vehicles, INDOPACOM-customer
        programs) operationalize the 2026-06-04 Five Eyes joint
        counterintelligence advisory "Safeguarding Our Secrets"?
      analyzed_at: 2026-06-04T16:45:00-04:00
      analyzed_by: analyst
      red_team_review: null
      invoking_context: >
        Grader flagged analyst_review_required:true. Operational-layer
        WEP at "likely" on DIB-cleared-personnel inclusion (grader-side
        inference). Hard Rule 2 attribution-preservation context: Five
        Eyes attributes generically to "China's military intelligence
        services" — no tracked-actor named. ACH question is about
        ACTION FRAMING for the target profile, NOT about attribution
        (Rule 2 prohibits attribution origination; ACH here pressure-
        tests the sourced operationalization claim, not a sourced
        attribution claim).
      hypotheses:
        - id: H1
          statement: >
            The alert is direct-actionable for DIB cleared-personnel —
            FSO / DCSA partnership + LinkedIn-pattern security awareness
            is the right immediate response. Implicit-target-scope from
            "anyone with access to classified or privileged information"
            + Indo-Pacific stationed military framing is materially-
            applicable to A&D primes and Tier-2/3 suppliers.
        - id: H2
          statement: >
            The alert is monitoring-tier only — generic-PLA attribution
            + implicit-not-explicit DIB scope = standard insider-threat
            program awareness, no new defensive action beyond what FSO
            programs already do continuously.
        - id: H3
          statement: >
            The alert is out-of-cyber-domain and should not have been
            promoted into a cyber-CTI corpus — counterintelligence
            material belongs in DCSA / FBI CI channels, not in a
            cyber-CTI brief audience pipeline.
        - id: H4
          statement: >
            The alert is partially actionable but the leverage point is
            corporate-recruiter / HR due diligence + foreign-influence
            vetting on senior-cleared roles, not FSO partnership per se
            (the named tradecraft of front-company-as-recruiter
            specifically targets the recruiter-to-candidate interface,
            which sits with HR/Corp Security, not FSO).
        - id: H5
          statement: >
            Composite / null — alert is operationally relevant only as
            background awareness; no specific defender action ought to
            change because the advisory names no specific tradecraft
            signature that current insider-threat programs don't
            already monitor for. (Closer-to-null variant; functionally
            distinct from H2 because it asserts no action change AT ALL,
            including no awareness-circulation push.)
      evidence:
        - id: E1
          description: >
            Five Eyes joint authorship (MI5 lead + FBI/ASIO/CSIS/NZSIS
            co-authors); five-government-intelligence-service joint
            counterintelligence advisory class — highest-credibility
            public counterintelligence source available
          source: mi5-fbi-asio-csis-nzsis-joint
          digraph: A1
          weight: 3
        - id: E2
          description: >
            Verbatim target-set language explicitly includes "anyone
            with access to classified or privileged information" + the
            "indirect or peripheral access" hedge — broader than just
            government employees
          source: mi5-fbi-asio-csis-nzsis-joint
          digraph: A1
          weight: 3
        - id: E3
          description: >
            Indo-Pacific stationed military explicitly named in target
            set; direct-relevance to INDOPACOM-customer programs that
            cleared A&D primes routinely support (B-21/B-1B sustainment,
            F-22/F-35 modification, GMD/THAAD, Aegis BMD, submarine +
            shipbuilding)
          source: mi5-fbi-asio-csis-nzsis-joint
          digraph: A1
          weight: 3
        - id: E4
          description: >
            DIB prime names ABSENT from the advisory's named-target
            list; the advisory names government/military personnel,
            academics, journalists, think-tank staff explicitly — but
            does not enumerate cleared-defense-contractor populations
            as a distinct named category
          source: mi5-fbi-asio-csis-nzsis-joint
          digraph: A1
          weight: 3
        - id: E5
          description: >
            Mechanism class is HUMINT (LinkedIn / front-company-as-
            recruiter / virtual-interview / encrypted-messaging-
            transition / unconventional-payment) — verifiably NOT
            cyber-TTP; no malware, no CVE, no C2, no infrastructure
            artifacts; advisory is counterintelligence content
          source: mi5-fbi-asio-csis-nzsis-joint
          digraph: A1
          weight: 3
        - id: E6
          description: >
            Generic-PLA attribution ("China's military intelligence
            services"); no specific PLA unit, no specific tracked-actor
            designation (Volt Typhoon / Salt Typhoon / APT40 / APT41
            all PLA / China-affiliated and in roster but none named
            in advisory)
          source: mi5-fbi-asio-csis-nzsis-joint
          digraph: A1
          weight: 3
        - id: E7
          description: >
            Splunk -30d sweep on PLA / LinkedIn / Five Eyes /
            Safeguarding Our Secrets / Chinese military intelligence /
            MI5 superset returned 0 events; per Hard Rule 8 silence
            is not disconfirming because HUMINT-tradecraft signals
            would not surface in cyber-security telemetry by definition
          source: splunk-negative-search
          digraph: A1
          weight: 3
        - id: E8
          description: >
            Target profile (mid-to-large US A&D contractor, ITAR-
            regulated, USG contract vehicles, classified/sensitive R&D)
            structurally aligns with "anyone with access to classified
            or privileged information" — the cleared-personnel
            population at such a contractor is a population the
            advisory's target-set framing covers by class even if not
            by explicit naming
          source: archimedes-target-profile-per-CLAUDE-md
          digraph: A1
          weight: 3
        - id: E9
          description: >
            Front-company-as-recruiter named tradecraft specifically
            targets the recruiter-to-candidate interface (LinkedIn
            unsolicited contact → fake consultancy/think-tank/HR-firm
            framing → virtual interview → encrypted messaging →
            unconventional payment); this leverage point sits at
            HR / Corp Security as much as at FSO
          source: mi5-fbi-asio-csis-nzsis-joint
          digraph: A1
          weight: 3
        - id: E10
          description: >
            The Record (Recorded Future Media) trade-press relay
            confirms the advisory exists and faithfully relays
            content + Indo-Pacific framing + verbatim absence of
            specific tracked-actor naming
          source: the-record
          digraph: B2
          weight: 2
      matrix:
        E1: {H1: C, H2: C, H3: I, H4: C, H5: N}   # Five Eyes authorship class supports any operational read; out-of-domain H3 inconsistent because a five-service counterintelligence advisory IS in-scope for CTI by precedent (CISA/NSA/FBI Flash co-publications)
        E2: {H1: C, H2: N, H3: I, H4: C, H5: I}   # "Anyone with access" language is direct-evidence the scope is broad; inconsistent with both out-of-scope H3 and no-action H5; neutral for monitoring-only H2 because the broad scope could still be argued as routine
        E3: {H1: C, H2: N, H3: I, H4: C, H5: I}   # Indo-Pacific stationed military framing is highly diagnostic — directly relevant to A&D INDOPACOM-customer programs; inconsistent with H3 and H5
        E4: {H1: I, H2: C, H3: N, H4: I, H5: C}   # DIB prime ABSENT from named list is inconsistent with H1's "direct-actionable" strength and H4's HR-pivot-as-primary; consistent with monitoring-tier H2 and the null H5; neutral for out-of-domain H3
        E5: {H1: C, H2: C, H3: C, H4: C, H5: C}   # HUMINT mechanism is consistent with all hypotheses — non-diagnostic
        E6: {H1: N, H2: C, H3: N, H4: N, H5: C}   # Generic-PLA attribution (no tracked-actor) doesn't speak to actionability per se; supports monitoring-tier and null framings because absence of specific actor signature reduces operational specificity
        E7: {H1: N, H2: N, H3: N, H4: N, H5: N}   # Splunk negative on HUMINT-class advisory is per-Rule-8 not disconfirming; non-diagnostic across all hypotheses
        E8: {H1: C, H2: C, H3: I, H4: C, H5: N}   # Target profile alignment confirms in-scope-by-class; inconsistent with out-of-domain H3
        E9: {H1: N, H2: N, H3: I, H4: C, H5: I}   # Front-company-as-recruiter tradecraft is DIAGNOSTIC for H4 — recruiter-interface tradecraft sits at HR/Corp Security; inconsistent with H3 and H5; neutral for H1/H2
        E10: {H1: C, H2: C, H3: I, H4: C, H5: N}   # Independent relay confirms scope but adds no new operational evidence
      inconsistency_counts:
        H1: 1   # only E4 (DIB-absent-from-named-list) materially inconsistent
        H2: 0
        H3: 5   # E1, E2, E3, E8, E10 — all inconsistent with the out-of-cyber-domain framing
        H4: 1   # only E4 (DIB-absent) materially inconsistent; otherwise diagnostically supported by E9
        H5: 3   # E2, E3, E9 — broad scope, Indo-Pacific framing, and HR-pivot tradecraft each cut against the no-action framing
      diagnostic_evidence:
        - E2: >
            "Anyone with access to classified or privileged information"
            language is the load-bearing evidence for in-scope-by-class
            inclusion of DIB cleared-personnel; diagnostic against H3
            (out-of-domain) and H5 (no-action).
        - E3: >
            Indo-Pacific stationed military framing is diagnostic
            against H3 and H5; direct-relevance to A&D INDOPACOM-
            customer programs is structural, not speculative.
        - E4: >
            DIB-prime ABSENCE from named-target list is the load-
            bearing evidence AGAINST a maximally-strong H1 / H4
            framing; it's why operational WEP capped at "likely"
            not "very likely" — implicit-not-explicit scope.
        - E9: >
            Front-company-as-recruiter tradecraft is diagnostic FOR
            H4 — the leverage point genuinely does sit at the
            HR/Corp-Security interface, not exclusively at FSO. This
            is the most actionable insight ACH surfaces; it suggests
            BOTH FSO awareness (H1) AND HR/corp-recruiter due
            diligence (H4) are correct operational levers, not
            substitutes.
      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: >
            Zero inconsistencies. The monitoring-tier framing is the
            best fit to the source text strictly read — the advisory
            does not enumerate DIB primes, does not name a specific
            tracked-actor, and the mechanism class (HUMINT) does not
            demand new cyber-defensive action. H2 wins on raw
            inconsistency count.
          wep: likely
        - rank: 2
          hypothesis_id: H1
          rationale: >
            Single inconsistency (E4 — DIB-prime absent from named
            list). H1 is supported by E2 (broad scope language), E3
            (Indo-Pacific framing), E8 (target-profile alignment).
            The single inconsistency is structural (advisory naming
            convention, not contradicting evidence) and is what caps
            WEP at "likely" rather than "very likely". H1 and H2
            are best understood as COMPLEMENTARY, not competing —
            H1 is the "what should the brief say to do" and H2 is
            the "what tier should the brief land in" answer.
          wep: likely
        - rank: 3
          hypothesis_id: H4
          rationale: >
            Single inconsistency (E4 — same as H1). Diagnostically
            supported by E9 (front-company-as-recruiter tradecraft
            sits at HR/Corp Security). The HR-pivot framing is a
            REAL leverage point that the grader's "FSO / DCSA"
            framing under-weights; brief should explicitly add
            corporate-recruiter due diligence as a second leverage
            point alongside FSO.
          wep: likely
        - rank: 4
          hypothesis_id: H5
          rationale: >
            Three inconsistencies (E2, E3, E9). The "no action change
            at all" framing is too strong — broad-scope target
            language, Indo-Pacific INDOPACOM relevance, and
            recruiter-interface tradecraft each justify SOMETHING
            beyond pure status-quo monitoring.
          wep: unlikely
        - rank: 5
          hypothesis_id: H3
          rationale: >
            Five inconsistencies. Out-of-domain framing fails because
            (a) cyber and counterintelligence are operationally
            adjacent in DIB security programs by long-standing
            precedent; (b) the operator's pre-decision (which is
            itself a load-bearing assumption — see KAC A4) settled
            that CI-adjacent material is in-scope. Rejected.
          wep: very_unlikely
      sensitivity_analysis:
        brittleness: low_to_medium
        load_bearing_evidence: [E2, E3, E4, E9]
        if_E2_reinterpreted: >
          If the "anyone with access" phrasing were narrowly
          construed (government-employee-only), H2 would gain
          relative to H1; brief framing should soften from "direct-
          actionable for DIB" to "monitoring with awareness-
          circulation." Single source = single point of failure;
          no second A-grade source on the scope-interpretation
          question. Brittleness is real but contained because
          Five Eyes joint authorship is the highest-credibility
          counterintelligence source class.
        if_E3_reinterpreted: >
          If Indo-Pacific framing were re-read as limited to
          uniformed military forward-deployed (not contractor
          program teams), H1's INDOPACOM-program-relevance lever
          weakens; H2 strengthens. Same single-source dependence.
        if_E4_reinterpreted: >
          If a follow-on advisory (CISA / NCSC / DCSA) explicitly
          names cleared-defense-contractor populations, E4 inverts
          from inconsistency to consistency, and WEP could rise
          on the implicit-scope inclusion to "very likely."
          Tripwire condition.
        if_E9_reinterpreted: >
          If front-company-as-recruiter tradecraft were re-read
          as primarily an FSO concern (the cleared employee
          surface) rather than an HR concern (the recruitment
          surface), H4 weakens. Both readings are defensible;
          including BOTH levers in the brief is the safer
          framing.
        single_point_of_failure: >
          Five Eyes advisory is the single attestation source;
          The Record is a publisher-independent relay but adds
          no telemetry. If the advisory itself were ever retracted
          or substantively amended (low probability for a five-
          service joint publication), the entire finding collapses.
          Brittleness on the source side is low because the source
          class is canonical; brittleness on the interpretation
          side (E2/E3 reading) is medium.
      tripwires:
        - observation: >
            Any follow-on Five Eyes, NCSC, CISA, DSS, or DCSA advisory
            that explicitly names cleared-defense-contractor populations
            as a recruitment target
          effect: >
            E4 inverts; H1 and H4 strengthen materially; WEP on DIB
            cleared-personnel inclusion could rise from "likely" to
            "very likely"
        - observation: >
            Any Tier-1 IR firm (Mandiant / CrowdStrike / Unit 42 /
            MSTIC / Recorded Future) attributes a specific PLA unit
            or tracked-actor designation (Volt Typhoon / Salt Typhoon
            / APT40 / APT41 etc.) to the activity described
          effect: >
            Hard Rule 2 boundary moves; analyst can pressure-test
            the SOURCED attribution; actor-profiler should consider
            profile updates; FLASH Trigger 2 territory likely
        - observation: >
            First-party Splunk telemetry surfaces an indicator
            consistent with the advisory's tradecraft (e.g., insider-
            threat program reports an unsolicited LinkedIn approach
            matching the front-company pattern)
          effect: >
            Hard Rule 8 first-party precedence activates; finding
            could lift to "very likely" on attribution-to-our-
            environment claim
        - observation: >
            Industry-association advisory (NDIA / AIA / DSCA / DIB
            ISAC) issues a paralleling alert with explicit DIB
            naming
          effect: >
            E4 inverts at industry-association layer; supports H1
            and H4 framing more strongly; brief tier could lift
            from monitoring to action
        - observation: >
            Discord operator decision: should "Chinese PLA HUMINT
            cluster" become a tracked entity in _roster.yaml?
          effect: >
            Out-of-band signal that the operator has decided to
            accept attribution origination explicitly with human
            sign-off; Hard Rule 2 boundary handled by operator,
            not by analyst
      conclusion:
        summary: >
          H1 and H2 are co-leading and complementary, not competing.
          H2 (monitoring-tier framing) wins on raw inconsistency
          count (zero) and is the right answer to "what brief tier?"
          H1 (direct-actionable for DIB cleared-personnel) ties for
          second with H4 (HR/corp-recruiter pivot) at one
          inconsistency each, and together answer "what specific
          action framing?" The grader's existing monitoring-tier
          inclusion + FSO/DCSA framing is correct, but the brief
          should additionally surface H4's HR/corp-recruiter due-
          diligence leverage point — front-company-as-recruiter
          tradecraft sits as much at HR/Corp Security as at FSO.
          H3 (out-of-domain) and H5 (no action at all) are rejected.
        wep: likely
        confidence_caveats: >
          Single attestation source (Five Eyes joint advisory) with
          publisher-independent trade-press relay only; no telemetry
          cross-reference possible by definition. WEP capped at
          "likely" on the operational layer per single-source veto.
          Implicit-not-explicit DIB scope is the load-bearing
          inference; if a follow-on advisory names DIB primes
          explicitly, WEP can rise. ACH does NOT and CANNOT
          propose any tracked-actor attribution — Hard Rule 2
          preserved verbatim.
        hard_rule_2_status: >
          PRESERVED. ACH ranking-1 hypothesis (H2) is an
          operationalization framing, not an attribution claim.
          The single attribution string in the finding ("China's
          military intelligence services") is and remains the
          verbatim Five Eyes phrase. No tracked-actor cross-
          reference proposed; no roster update justified by this
          ACH output.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        The Five Eyes 2026-06-04 "Safeguarding Our Secrets" joint
        counterintelligence advisory is operationally relevant for
        an A&D-target-profile audience because DIB cleared-personnel
        populations fall within the advisory's implicit target scope
        per "anyone with access to classified or privileged
        information" + Indo-Pacific stationed military framing; the
        defensive lever is FSO / DCSA insider-threat partnership +
        cleared-personnel security awareness; the advisory belongs
        in the monitoring tier of a cyber-CTI brief surface.
      analyzed_at: 2026-06-04T16:45:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Operator-requested KAC on four explicitly-named load-bearing
        premises. Operator pre-decision (counterintelligence-adjacent
        material is in-scope for cyber-CTI brief audience) is itself
        flagged as load-bearing and is interrogated here as A4.
      assumptions:
        - id: A1
          statement: >
            The advisory's verbatim target-set scope ("anyone with
            access to classified or privileged information") extends
            from the explicit named targets (government/military,
            Indo-Pacific stationed military, academics, journalists,
            think-tank staff) to DIB cleared-personnel at A&D primes
            and Tier-2/3 suppliers as an implicit-but-materially-
            applicable population
          category: semantic
          stated: false
          why_must_be_true: >
            The finding's operational-DIB-applicability layer
            depends on this implicit-scope inference. Without it,
            the advisory's relevance to A&D cleared-personnel
            collapses to "general counterintelligence awareness"
            with no specific target-profile pivot.
          when_could_be_false: >
            If "classified or privileged information" were read
            narrowly to refer only to government-classified
            information held by direct government employees, not
            by contractor cleared-personnel (i.e., the cleared-
            contractor population accessing classified material
            on behalf of USG would be treated as a separate
            category requiring separate naming). A follow-on
            advisory or DCSA / FBI CI clarifying note could
            settle this either way.
          evidence_for:
            - mi5-fbi-asio-csis-nzsis-joint
            - archimedes-target-profile-per-CLAUDE-md
          evidence_against: []
          confidence: medium_to_high
          centrality: critical
          classification: qualify
          remediation_detail: >
            Verbatim scope language is genuinely broad ("anyone with
            access") and the structural argument for DIB cleared-
            personnel inclusion is sound — cleared-defense-contractor
            personnel demonstrably have access to USG classified
            material as a matter of contract execution. But the
            advisory does NOT enumerate DIB primes by name, so the
            inference is implicit not explicit. Brief framing should
            preserve this distinction verbatim: "implicit but
            materially-applicable target scope" rather than
            "directly named."
        - id: A2
          statement: >
            LinkedIn / front-company-as-recruiter / virtual-interview
            tradecraft observed in the Five Eyes scope is directly
            portable to A&D-cleared-engineer / classified-program-PM
            / USG-contract-vehicle-lead recruitment
          category: TTP_patterns
          stated: false
          why_must_be_true: >
            If the tradecraft does not port to the A&D-cleared
            population, the finding's defensive lever (security-
            awareness reminder + HR due diligence) misfires because
            the recognition artifacts circulated would not match
            what targeted personnel actually encounter.
          when_could_be_false: >
            If PLA HUMINT recruitment specifically tailors tradecraft
            by target class — e.g., government-employee recruitment
            uses LinkedIn front-companies, but cleared-defense-
            contractor recruitment uses different vectors (industry
            conferences, ITAR-cleared-recruiter intermediation,
            classified-contract-lead poaching) — the named
            tradecraft becomes partially or fully inapplicable.
          evidence_for:
            - mi5-fbi-asio-csis-nzsis-joint
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
          remediation_detail: >
            Internally coherent with historical PLA / MSS HUMINT
            patterns documented across two decades of US CI cases
            (Glenn Duffie Shriver, Ji Chaoqun, others used LinkedIn
            / academic-cover / consultancy-cover variants targeting
            cleared US persons including defense-industry-adjacent
            populations). Portability claim is plausible at medium
            confidence. Brief should frame tradecraft as
            "consistent with PLA HUMINT pattern broadly observed
            against cleared US persons" rather than "specifically
            tailored to A&D cleared-personnel." This caveat
            already implicit in the grader's framing; keep it
            verbatim.
        - id: A3
          statement: >
            The operational defensive lever is FSO / DCSA insider-
            threat partnership + cleared-personnel security awareness
            reminder, rather than cyber-controls (EDR / network /
            identity hardening)
          category: capability
          stated: true
          why_must_be_true: >
            HUMINT recruitment via LinkedIn / front-company /
            virtual-interview tradecraft is a human-factor security
            problem; cyber controls (EDR, network egress, identity)
            do not detect or interdict an unsolicited LinkedIn
            message, a fake consultancy invitation, or a virtual
            interview conducted over public video tools.
          when_could_be_false: >
            If the HUMINT recruitment cycle eventually pivots to
            cyber delivery (recruited insider runs malware,
            credentials harvested, etc.), cyber-controls re-engage.
            But that's a successor stage, not the recruitment-
            stage activity the advisory describes.
          evidence_for:
            - mi5-fbi-asio-csis-nzsis-joint
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
          remediation_detail: >
            Genuinely sound. HUMINT-class advisory ⇒ human-factor
            defensive lever. Keep grader framing as-is. One nuance
            ACH surfaced: H4 (HR/corp-recruiter due diligence)
            is a complementary lever the grader's FSO-framing
            under-weights. Brief should add HR/corp-recruiter
            due diligence alongside FSO/DCSA partnership rather
            than treat them as substitutes.
        - id: A4
          statement: >
            HUMINT-led counterintelligence material is in-scope for
            a cyber-CTI brief audience (the operator pre-decided this
            with caveats; the assumption deserves explicit KAC
            interrogation as load-bearing for the inclusion decision
            itself)
          category: semantic
          stated: true
          why_must_be_true: >
            If CI material is out-of-scope for cyber-CTI brief
            audience, the finding should not be promoted at all
            and the analyst SAT is moot. Inclusion decision
            depends on this assumption holding.
          when_could_be_false: >
            If the brief audience is strictly cyber-only (SOC /
            EDR / network / identity teams) with no CI / FSO /
            DCSA-adjacent reader population, CI content would be
            noise that erodes signal-to-noise ratio.
          evidence_for:
            - archimedes-target-profile-per-CLAUDE-md
            - operator-judgment-precedent
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
          remediation_detail: >
            Operator pre-decision is documented and consistent with
            target-profile reality — DIB cleared-personnel
            environments have FSO / Corp Security / Insider Threat
            programs adjacent to (often integrated with) cyber
            security functions. CI-adjacent material is a
            legitimate brief surface for such an audience. The
            assumption holds at high confidence. Caveat: if a
            future operator decision narrows the audience scope,
            this should be re-tested. Tripwire: any operator
            directive to remove CI-adjacent content categories
            from brief surface.
        - id: A5
          statement: >
            Generic-PLA attribution ("China's military intelligence
            services") preserves Hard Rule 2 without requiring any
            tracked-actor cross-reference
          category: source_reliability
          stated: true
          why_must_be_true: >
            If the advisory's generic attribution implicitly
            equates to one of the tracked PLA-affiliated actors
            (Volt Typhoon, Salt Typhoon, APT40, APT41), then
            preserving the advisory verbatim while NOT updating
            the relevant actor profile becomes incoherent.
          when_could_be_false: >
            If a Tier-1 IR firm publishes a follow-on report
            naming a specific PLA unit and explicitly linking
            it to the Five Eyes advisory, the generic attribution
            collapses into a specific one and the actor-profiler
            should re-evaluate.
          evidence_for:
            - mi5-fbi-asio-csis-nzsis-joint
            - the-record
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
          remediation_detail: >
            Five Eyes attribution is genuinely generic — "China's
            military intelligence services" is a class-level
            attribution that does not map cleanly to any single
            tracked-actor in the roster. Volt Typhoon and Salt
            Typhoon are typically attributed in CISA / NSA / FBI
            framing to PRC state actors broadly with infrastructure
            targeting emphasis; APT40 is PLA-attributed by Mandiant
            with a maritime / South China Sea targeting emphasis;
            APT41 is dual-mission (espionage + criminal) and not
            a clean PLA-only entity. None is a one-to-one match
            for "PLA HUMINT recruitment." Grader's Hard Rule 2
            discipline (preserve verbatim, no upgrade) is correct.
            Tripwire is set for any Tier-1 IR firm linkage.
      classifications_summary:
        sound: 3   # A3, A4, A5
        qualify: 2   # A1, A2
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - >
            "Implicit but materially-applicable target scope" —
            DIB cleared-personnel are within scope per the broad
            "anyone with access to classified or privileged
            information" language and the Indo-Pacific stationed
            military framing, but the advisory does NOT enumerate
            DIB primes by name. Brief should preserve this
            distinction verbatim.
          - >
            "Tradecraft portability at medium confidence" — named
            LinkedIn / front-company / virtual-interview tradecraft
            is consistent with the broad historical PLA / MSS
            HUMINT pattern against cleared US persons, but
            specific tailoring to A&D-cleared-engineer /
            classified-program-PM populations is inferred not
            attested. Brief should frame as "consistent with the
            broad PLA HUMINT pattern observed against cleared US
            persons" rather than "specifically calibrated to A&D
            cleared roles."
          - >
            "Complementary HR/corp-recruiter due-diligence lever"
            — ACH H4 surfaces that front-company-as-recruiter
            tradecraft sits at the HR/Corp-Security interface in
            addition to the FSO interface. Brief should add
            corporate-recruiter due diligence (front-company
            vetting on outreach to senior-cleared candidates) as
            a complementary lever to FSO/DCSA partnership, not
            as a substitute.
        next_action: >
          Proceed to brief surface at monitoring tier per grader
          recommendation. Apply the three qualifying caveats
          above to brief framing. No assessment block; no test
          required; WEP ceiling unchanged at "likely" on the
          operational layer.
      recommended_wep_after_test:
        unchanged: likely   # KAC produced no Test classifications; WEP unchanged
        if_DIB_named_explicitly_in_follow_on: very_likely   # tripwire would lift implicit-scope to explicit-scope and clear single-source-veto via independent advisory layer
        if_tracked_actor_linked_by_tier_1: re-evaluate   # actor-profiler involvement triggered; Hard Rule 2 boundary handled by sourced attribution
      hard_rule_2_status: >
        PRESERVED. KAC's A5 sound-classification reinforces the
        grader's verbatim-preservation discipline. No assumption
        in this KAC proposes or requires a tracked-actor mapping.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-04-afternoon]
retracted: false
retraction_brief_id: null

# Defensive / IOC handoff flags
ioc_handoff:
  defender_relevant_iocs: []   # HUMINT advisory; no cyber-IOCs by definition. Tradecraft-recognition is the equivalent.
  tradecraft_recognition_artifacts:
    - "LinkedIn unsolicited contacts from 'private consultancies,' 'think tanks,' or 'human resources firms' offering paid consulting work / 'intelligence reports' / virtual-interview engagement"
    - "Virtual interview probing questions about role, unit, customer programs in early-stage interview"
    - "Payment offers ($100s-$1000s per intelligence report)"
    - "Transition to encrypted-messaging app after initial LinkedIn contact"
    - "Front-company-as-recruiter posing as consultancy / think tank / HR firm"
  iocs_indirect_action: >
    Defender action framing for A&D-DIB cleared-personnel
    population:
    (a) Cleared-personnel security-awareness reminder via FSO / DCSA channels — circulate named tradecraft pattern;
    (b) Indo-Pacific program teams (B-21 / B-1B sustainment, F-22 / F-35 modification, GMD / THAAD, Aegis BMD, submarine + shipbuilding) — direct circulation of MI5 PDF to security-cleared personnel on INDOPACOM-customer programs; FSO brief on Indo-Pacific framing;
    (c) Corporate security CI partnership — confirm working relationship with FBI Counterintelligence / DCSA insider-threat program; report any matching tradecraft observations;
    (d) HR / external-recruiter due diligence — for senior-cleared roles, augment standard background checks with insider-threat / foreign-influence vetting where DCSA permits;
    (e) NO cyber-TTP defensive action change — this is HUMINT-led counterintelligence; standard cyber controls (EDR, network egress, identity hardening) are not the leverage point. The leverage point is human-factor security awareness + CI partnership.

monitor_for_next_cycle:
  - Any cyber-TTP overlap surfaced by a Tier-1 IR firm (e.g., subsequent malware delivery against recruited insider) — would lift this from counterintelligence advisory to cyber-actionable
  - Any APT40 / APT41 / Volt Typhoon / Salt Typhoon attribution layered on by a Tier-1 IR firm — would lift to FLASH Trigger 2 territory and likely re-evaluation
  - Named A&D prime in any follow-on Five Eyes, NCSC, CISA, or industry-association advisory
  - Any DIB / cleared-defense-contractor-specific guidance from CISA / DSS / DCSA / NCSC paralleling the Five Eyes alert (DCSA insider-threat guidance update would be the strongest follow-on signal for the target profile)
  - Operator decision: should "Chinese PLA HUMINT cluster" become a tracked entity in `_roster.yaml`? Currently NO per Hard Rule 2 and absence of specific tracked-actor designation in advisory itself; re-evaluate if a Tier-1 IR firm or follow-on government advisory names a specific PLA unit

actor_profiler_handoff:
  scaffold_candidate: false
  scaffold_note: >
    Hard Rule 2 preserves verbatim Five Eyes generic attribution
    to "China's military intelligence services" (PLA-linked).
    No specific tracked-actor in `_roster.yaml` is named. Volt
    Typhoon (#008), Salt Typhoon (#010), APT40 (#017), APT41
    (#019) are all PLA / China-affiliated and present in the
    roster but none is named in this advisory. Grader does
    NOT scaffold a new "PLA HUMINT cluster" tracked entity;
    advisory does not name a specific PLA unit and Hard Rule
    2 prohibits Archimedes from originating attribution.
    Actor-profiler should NOT take action on this finding
    unless a Tier-1 IR firm or follow-on advisory names a
    specific PLA unit / tracked-actor designation.

librarian_handoff:
  new_source_addition:
    source_yaml_id: mi5-fbi-asio-csis-nzsis-joint
    proposed_grade: A
    provisional: true
    provisional_since: 2026-06-04
    provisional_reason: >
      Five Eyes joint counterintelligence advisory class — five-
      government-intelligence-service joint authorship is the
      highest-credibility public counterintelligence source
      class available. Provisional A per the same precedent
      class as CISA / NSA / FBI Flash / NCSC. First Archimedes-
      corpus citation via MI5 lead-agency PDF publication of
      "Safeguarding Our Secrets" advisory paired with The
      Record (Recorded Future Media) trade-press relay. 72h
      ratification clock to 2026-06-07T16:24:00-04:00.
    action_requested: source-grade-log entry + source-grades.yaml addition by librarian on next pass
  source_grade_revision_proposed: null

briefer_handoff:
  brief_inclusion_recommendation: monitoring_tier
  brief_substance: >
    PM brief Other Signal / Monitoring section.
    Counterintelligence-adjacent material in-scope per operator
    judgment for A&D-target-profile audience. Headline framing:
    "Five Eyes joint advisory — Chinese PLA military
    intelligence HUMINT recruitment via LinkedIn / front
    companies / virtual interviews — cleared-personnel target
    set including Indo-Pacific stationed military." Practical
    defender pivot: FSO / DCSA cleared-personnel security
    awareness; Indo-Pacific program-team circulation of MI5
    PDF; corporate-security CI partnership. NO cyber-TTP action
    triggered — this is human-factor security awareness lever
    not cyber-controls lever. Briefer should preserve Hard
    Rule 2 verbatim attribution ("China's military intelligence
    services") and explicitly note no specific tracked-actor
    named in advisory. Keep concise (4-5 sentences in
    monitoring tier given operator note that this is a
    legitimate defensive lever).

---

# Five Eyes Joint Counterintelligence Advisory "Safeguarding Our Secrets" — Chinese PLA Military Intelligence Services HUMINT Recruitment via LinkedIn, Front Companies, Virtual Interviews Targeting Cleared Personnel Including Indo-Pacific Stationed Military

## Summary

A joint Five Eyes counterintelligence advisory titled **"Safeguarding Our Secrets"** was published on 2026-06-04 as a PDF on mi5.gov.uk. Authored by MI5 (UK, lead agency), FBI (US), ASIO (Australia), CSIS (Canada), and NZSIS (New Zealand). The advisory warns verbatim that *"China's military intelligence services"* are conducting HUMINT recruitment operations against personnel in Five Eyes nations who hold security clearances or have access to *"classified or privileged information"*. The Record (Recorded Future Media) reported the advisory on 2026-06-04 at 18:04 UTC (14:04 EDT, in-window) as the first publisher-independent trade-press relay.

**Hard Rule 2 disposition:** Five Eyes attributes generically to "China's military intelligence services" (PLA-linked, not MSS). No specific PLA unit, no specific tracked-actor designation. Volt Typhoon (#008), Salt Typhoon (#010), APT40 (#017), APT41 (#019) are all PLA / China-affiliated and present in `_roster.yaml` but none is named in the advisory. Archimedes preserves the verbatim Five Eyes attribution and does NOT upgrade to specific tracked-actor mapping.

**Substantive claim class is HUMINT-led counterintelligence, NOT cyber-TTP.** Per operator judgment, counterintelligence-adjacent material is in-scope for an A&D-target-profile audience because DCSA / FSO / insider-threat partnership is a legitimate defensive lever even when the mechanism is HUMINT not cyber.

**Defensive scope:** DIB cleared-personnel population is within the advisory's implicit target scope per the verbatim phrase *"anyone with access to classified or privileged information"*. Indo-Pacific stationed military is explicitly named, which puts A&D primes with INDOPACOM-customer programs (B-21 / B-1B sustainment, F-22 / F-35 modification, GMD / THAAD, Aegis BMD, submarine + shipbuilding) in direct relevance.

## Sources

### Five Eyes joint counterintelligence advisory (mi5-fbi-asio-csis-nzsis-joint, digraph: A2 layered — NEW source-id pending librarian addition)

- URL: https://www.mi5.gov.uk/sites/default/files/2026-06/SAFEGUARDING%20OUR%20SECRETS%20PUBLICATION.pdf
- Published: 2026-06-04
- Lead agency: MI5 (UK)
- Co-authors: FBI (US), ASIO (Australia), CSIS (Canada), NZSIS (New Zealand)
- Source grade: A (provisional, new source-id since 2026-06-04; same precedent class as CISA / NSA / FBI Flash / NCSC; 72h ratification clock to 2026-06-07T16:24:00-04:00; librarian handoff for source-grades.yaml addition)
- Key claim: Five-service joint attestation that "China's military intelligence services" are conducting active HUMINT recruitment operations against cleared and access-privileged personnel in Five Eyes nations via LinkedIn, front companies, virtual interviews, encrypted-messaging transitions, and unconventional payment.
- Verbatim attribution quote (5 words, Hard Rule 6 preserved): *"China's military intelligence services"*.
- Verbatim target-set quote (8 words, Hard Rule 6 preserved): *"anyone with access to classified or privileged information"*.

### The Record (the-record, digraph: B2 relay)

- URL: https://therecord.media/five-eyes-warns-chinese-spies-are-using-job-sites-to-recruit-insiders
- Published: 2026-06-04 18:04 UTC (14:04 EDT)
- Source grade: B (ratified per source-grades.yaml)
- Key claim: Publisher-independent trade-press relay of Five Eyes joint advisory; surfaces Indo-Pacific stationed military verbatim call-out; notes verbatim absence of any specific named threat-actor in the advisory.

Independence test: publisher-independence holds across two sources (Five Eyes PDF + The Record relay). Five-government-intelligence-service joint authorship internally satisfies cross-service independence for the advisory itself. Evidence-basis at the operational-claim layer is government-counterintelligence-service-on-own-observed-activity canonical.

## Named tradecraft

Per the Five Eyes joint advisory:

- **LinkedIn** as primary platform — named explicitly.
- Generic job-advertisement platforms.
- **Front companies** posing as private consultancies, think tanks, or human resources firms.
- Virtual interviews with role-and-unit probing questions.
- Encrypted-messaging-app transitions (off LinkedIn after initial contact).
- Payment via unconventional methods ($100s–$1000s per intelligence report).

This is internally coherent with the historical PLA / MSS HUMINT pattern documented across two decades of US counterintelligence cases. Mechanism class only; no PoC, no cyber-attack tooling described (HUMINT advisory by definition).

## Named target set

Per the Five Eyes joint advisory:

- Government and military personnel.
- **Indo-Pacific stationed military personnel** (named verbatim per The Record relay).
- Academics, journalists, think-tank staff (cited as targets with "indirect or peripheral access" to privileged information).
- Anyone with "direct or indirect access to privileged information" — explicitly hedged to include targets whose information "may not necessarily be 'classified'" but possess valuable "insights and network of contacts."

## A&D / DIB defensive scope

**Not explicit** in the advisory; the advisory names "government and military personnel" and the broader "anyone with access to classified or privileged information." DIB cleared-personnel — and by extension A&D prime / Tier-2/3 supplier security-cleared engineers, program managers, and program-office staff — are within the implicit target scope but NOT in the named-target list.

**Operational read for the target profile:** A mid-to-large US aerospace and defense contractor's cleared-personnel population — ITAR-program engineers, classified-program PMs, USG contract-vehicle leads — falls within "anyone with access to classified or privileged information". Indo-Pacific-deployed military personnel call-out is direct-relevance to A&D primes with INDOPACOM-customer programs.

**Defender action framing:**

1. **Cleared-personnel security-awareness reminder via FSO / DCSA channels.** Circulate the named tradecraft pattern (unsolicited LinkedIn contacts from "private consultancies," "think tanks," or "HR firms"; probing questions in early interviews; payment offers; encrypted-messaging transitions).
2. **Indo-Pacific program teams.** Direct circulation of MI5 PDF to security-cleared personnel on INDOPACOM-customer programs; FSO brief on the Indo-Pacific framing.
3. **Corporate security CI partnership.** Confirm working relationship with FBI Counterintelligence / DCSA insider-threat program; report matching tradecraft observations.
4. **HR / external-recruiter due diligence.** For senior-cleared roles, augment standard background checks with insider-threat / foreign-influence vetting where DCSA permits. Front-company-as-recruiter is a named tradecraft; the recruiting organization itself may be the threat surface.
5. **No cyber-TTP defensive action change.** This is HUMINT-led counterintelligence; standard cyber controls (EDR, network egress, identity hardening) are not the leverage point for this campaign. The leverage point is human-factor security awareness + CI partnership.

## IOCs surfaced

No cyber-IOCs (no C2, no actor infrastructure, no file hashes, no domains). HUMINT advisory by definition. Tradecraft-recognition artifacts are the equivalent and are surfaced in the `ioc_handoff.tradecraft_recognition_artifacts` field.

Attribution claims preserved verbatim: *"China's military intelligence services"* (Five Eyes joint, generic PLA-attributed; PLA-linked rather than MSS / civilian intelligence). Archimedes does NOT upgrade to specific tracked-actor mapping. No first-time attribution origination per Hard Rule 2.

## Relationship to existing findings

No direct relation to existing tracked actors (per Hard Rule 2 preservation discipline), campaigns, or VT-* dossiers. Volt Typhoon (#008), Salt Typhoon (#010), APT40 (#017), APT41 (#019) actor dossiers exist in `_roster.yaml` and are all PLA / China-affiliated but none is named in this advisory; this finding does NOT propose updates to those profiles.

## Open questions for analyst

Analyst review flagged (`analyst_review_required: true`) for:

1. **Hard Rule 2 attribution preservation context.** Analyst should examine whether any tracked-actor cross-reference is appropriate in the brief framing WITHOUT originating attribution. Recommended disposition: brief preserves Five Eyes verbatim attribution and explicitly notes absence of specific tracked-actor.
2. **DCSA / FSO / insider-threat partnership framing.** Analyst SAT-ACH on the question "is the DIB cleared-personnel population materially in target scope versus general cleared-personnel population?" may sharpen the brief framing. Hypotheses to consider:
   - H1: DIB cleared-personnel are materially in scope at parity with government / military personnel (per "anyone with access" framing).
   - H2: DIB cleared-personnel are in scope but lower-priority than government / military / Indo-Pacific stationed military (per the advisory's explicit named-target hierarchy).
   - H3: DIB cleared-personnel are out-of-scope for this specific advisory and the framing is government-employee-focused.
   Evidence available: advisory's verbatim target-set language; absence of A&D-prime explicit naming; Indo-Pacific framing's direct relevance to INDOPACOM-customer programs. Operator judgment leans H1-H2; analyst should formalize.
3. **No SAT-KAC trigger.** Assumption layer is at the implicit-target-scope inclusion of DIB, which the operator's judgment has already settled at H1-H2; no key-assumption SAT-KAC is warranted at this monitoring-tier finding.

Re-evaluate on any of:
- Any cyber-TTP overlap surfaced by a Tier-1 IR firm
- Any APT40 / APT41 / Volt Typhoon / Salt Typhoon attribution layered on by a Tier-1 IR firm
- Named A&D prime in any follow-on Five Eyes, NCSC, CISA, or industry-association advisory
- DIB / cleared-defense-contractor-specific guidance from CISA / DSS / DCSA / NCSC paralleling the Five Eyes alert

## Analytic notes (from analyst review)

Analyst SAT (ACH + KAC) confirms the grader's monitoring-tier inclusion + "likely" operational-layer WEP is correctly calibrated, with three qualifying caveats the briefer should preserve verbatim.

ACH ranking-1 hypothesis (H2 — monitoring-tier framing) won on raw inconsistency count, but H1 (direct-actionable for DIB cleared-personnel) and H4 (HR/corp-recruiter due-diligence pivot) tied for second at one inconsistency each and are complementary not competing. The grader's framing under-weighted H4: front-company-as-recruiter tradecraft sits at the HR/Corp-Security interface as much as at FSO/DCSA. The brief should surface both leverage points. H3 (out-of-domain) and H5 (no-action) were rejected at three and five inconsistencies respectively.

KAC produced no Test or Reject classifications. A1 (DIB implicit-scope inclusion) and A2 (tradecraft portability to A&D-cleared roles) qualified at medium-to-high confidence with critical and material centrality — both require explicit framing caveats but neither blocks publication. A3 (HUMINT human-factor lever), A4 (CI-adjacent material in-scope per operator pre-decision), and A5 (Hard Rule 2 preserved by generic-PLA attribution) classified sound.

Hard Rule 2 preserved verbatim throughout. No tracked-actor cross-reference proposed; tripwires set for any Tier-1 IR firm linkage to Volt Typhoon / Salt Typhoon / APT40 / APT41 or any follow-on advisory explicitly naming DIB primes.

## Hard Rule Compliance

- **Hard Rule 1 (Legal policy):** PRESERVED — counterintelligence advisory at TLP:CLEAR per government public-PDF publication; no PII of private individuals collected; no controlled technical data; legitimate-interest basis for defensive intelligence research.
- **Hard Rule 2 (Never originate attribution):** PRESERVED — verbatim Five Eyes attribution language preserved ("China's military intelligence services"); no upgrade to specific tracked-actor mapping. The advisory itself does NOT name Volt Typhoon, Salt Typhoon, APT40, APT41, or any other specific tracked-actor; Archimedes does not originate the attribution layer.
- **Hard Rule 3 (No exploitation):** PRESERVED — HUMINT advisory; no PoC content; no cyber-attack tooling described.
- **Hard Rule 6 (Quote discipline):** PRESERVED — two verbatim Five Eyes attribution quotes preserved at 5 words ("China's military intelligence services") and 8 words ("anyone with access to classified or privileged information"); both under 15-word limit; one quote-class per source (vendor primary). The Record relay paraphrased.
- **Hard Rule 7 (Credentials):** N/A — no credentials in source content.
- **Hard Rule 8 (Splunk first-party):** Splunk -30d sweep ran on PLA + LinkedIn + Five Eyes + Safeguarding Our Secrets + Chinese military intelligence + MI5 superset; 0 events; silence not disconfirming (HUMINT-tradecraft signals would not surface in cyber-security telemetry by definition).
