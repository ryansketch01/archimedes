---
finding_id: finding-2026-05-30-0001-mstic-33-malicious-npm-dependency-confusion-recon-only-mode-oob-moika-tech-c2-three-aliases-no-roster-attribution-no-ad-nexus
created_at: 2026-05-30T08:05:00-04:00
graded_by: grader
grading_run_id: morning-20260530-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: A2
digraph_layered:
  mstic_primary_research_publication_existence: A1                            # MSTIC byline, Microsoft Defender Security Research Team, vendor-authority on own product detection telemetry + npm coordinated takedown
  33_package_count_in_two_burst_windows_may_28_19_03_may_29_09_02_utc: A2     # MSTIC vendor observation; not independently corroborated in window
  three_maintainer_aliases_mr_4nd3r50n_ce_rwb_t_in_one_yandex_ru: A2          # MSTIC forensic-npm-registry-metadata observation
  operator_level_attribution_three_accounts_same_individual_high_confidence: A2  # MSTIC explicit attribution language, operator-level only, no APT/nation-state claim
  no_apt_or_nation_state_attribution: A1                                       # MSTIC explicit decline — verbatim source statement
  oob_moika_tech_c2_three_platform_payload_delivery: A2                        # MSTIC IOC publication on own-telemetry observation
  x_secret_header_gate_l95hd_unique_strong_signal: A2                          # Hardcoded shared secret published verbatim, defensive-detection-grade IOC
  recon_only_mode_with_server_side_toggle_for_followon_exploit: A2             # MSTIC analytic assessment of payload state; methodologically novel signature
  two_phase_design_recon_now_exploit_later_methodological_signature: A2        # Analytic framing, internally coherent, well-supported by payload analysis
  inflated_version_numbers_100_100_100_99_5_7_99_5_8_dependency_confusion_winning_tactic: A1  # Well-established dependency-confusion primitive since Birsan 2021
  obfuscator_io_style_obfuscation_7kb_postinstall_stager: A1                   # MSTIC technical artifact observation
  bug_bounty_account_to_malware_operator_lifecycle_mr_4nd3r50n: A2             # MSTIC forensic-registry observation; novel operator-lifecycle signal
  npm_coordinated_takedown_all_packages_removed_before_publication: A1         # MSTIC procedural vendor coordination claim
  no_ad_nexus_fintech_ecommerce_russian_speaking_target_set: A2                # MSTIC target-scope observation; explicit absence of DIB / ITAR / aerospace framing
  sberbank_sberpay_wildberries_capibar_target_set: A2                          # MSTIC scope-name analysis
  no_lineage_link_to_shai_hulud_teampcp_mini_shai_hulud_vt006: A2              # MSTIC explicitly does NOT make the link; Archimedes does NOT originate one
  github_cloudplatform_single_spa_io_spoofed_enterprise_metadata: A1           # MSTIC IOC publication; detection-grade for any environment resolving the hostname
  cluster_anchor: A2

digraph_anchor: >
  Cluster digraph A2 anchored on Microsoft MSTIC / Microsoft Security
  Blog primary (Microsoft Defender Security Research Team, 2026-05-29
  20:06 EDT) — vendor-authority publication of an active npm
  supply-chain attack. MSTIC names 33 malicious packages registered
  under nine spoofed organizational scopes employing dependency
  confusion, three new maintainer aliases (`mr.4nd3r50n`, `ce-rwb`,
  `t-in-one`) all using yandex.ru email addresses, and assesses with
  high confidence the three accounts are operated by a single
  individual (forensic npm registry metadata analysis). Two
  publication bursts: May 28 18:47-19:03 UTC and May 29 09:01-09:02
  UTC. All packages ship the same ~7KB obfuscated postinstall stager
  that posts to a single C2 endpoint (`oob.moika.tech`) gated by a
  hardcoded shared secret (`l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1`).
  Payload is platform-specific (Windows / macOS / Linux), runs in
  RECON_ONLY mode currently (a server-side toggle exists for
  follow-on exploitation), and performs environment fingerprinting
  + credential reconnaissance via environment variables passed to a
  detached process. Several scope names target Russian-language
  enterprise software ecosystems (Sberbank SberPay, Wildberries
  shape). MSTIC + npm team coordinated removal of all packages
  before publication.

  A2 (not A1) holds on the cluster anchor because:
    - MSTIC is single-source in window. Corpus grep across `threats/`
      for `moika`, `4nd3r50n`, `ce-rwb`, `t-in-one`, "dependency
      confusion", "33 malicious" → zero prior mentions. Sentinel
      AM-30 confirmed no overnight relay arrived from BleepingComputer,
      The Hacker News, Security Affairs, The Register, Socket, or
      Snyk in the ~12-hour window since MSTIC publication
      (2026-05-29 20:06 EDT → 2026-05-30 07:35 EDT). Single-source
      veto applies on operational claims that exceed "likely" WEP.
    - The procedural facts (campaign exists, 33 IOCs valid, C2 host
      published, X-Secret gate value published, packages removed by
      npm) are at A1 individually but cluster-anchor at A2 pending
      independent corroboration of the campaign envelope.
    - MSTIC's attribution is operator-level only (single individual,
      high confidence). MSTIC explicitly declines APT / nation-state
      attribution. Per Hard Rule 2, Archimedes does NOT extend the
      attribution to any roster actor; the three aliases are not in
      the Archimedes roster.

  Per Hard Rule 3 (no exploitation, ever), defender-facing detail is
  included in the technical-detail section, but NO PoC reproduction
  steps, payload construction, or exploitation guidance.

source_reliability:
  grade: A
  source_name: "Microsoft MSTIC / Microsoft Security Blog (Microsoft Defender Security Research Team)"
  source_yaml_id: mstic
  grade_rationale: >
    MSTIC pre-assigned A per source-grades.yaml. Microsoft Defender
    Security Research Team byline; vendor-authority publication on
    own-product detection telemetry; full IOC enumeration with
    detection-grade artifacts (C2 hostname, X-Secret header value,
    three-platform payload paths, spoofed enterprise metadata domains);
    remediation coordinated with npm team (packages removed before
    publication). Article is a vendor blog primary research piece,
    not a relay.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_established_dependency_confusion_primitive_birsan_2021_lineage
    - probably_true_no_contradicting_ab_grade_source_in_window
    - probably_true_technical_claims_internally_coherent_inflated_versions_postinstall_hook_x_secret_gated_three_platform_c2_all_real_and_plausible_in_combination
  rationale: >
    Probably True (2) on the campaign-envelope claim. MSTIC technical
    detail (33 malicious packages under nine spoofed scopes,
    dependency confusion via inflated version numbers as the
    winning-tactic, ~7KB Obfuscator.io-style postinstall stager,
    platform-specific payload delivery via `/payload/{win,mac,linux}`
    paths gated by `X-Secret` HTTP header, RECON_ONLY mode with
    server-side toggle for follow-on, three yandex.ru maintainer
    aliases, two publication burst windows) is internally coherent
    and consistent with established npm-supply-chain TTPs (T1195.002
    Supply Chain Compromise: Software, T1059.007 JavaScript,
    T1027 Obfuscated Files, T1071.001 HTTP C2, T1574 Hijack
    Execution Flow via npm lifecycle hooks). Cannot be promoted to
    "Confirmed" (1) without at least one independent source
    (BleepingComputer, The Hacker News, Socket, Snyk, StepSecurity,
    or another Tier-1/2 vendor) relaying or expanding on this
    campaign. Sentinel AM-30 documented zero such relay arrived
    overnight. No contradicting A/B-grade source. The RECON_ONLY
    + two-phase methodological framing is MSTIC's analytic
    characterization of the observed payload state, not
    independently corroborated.

corroboration:
  independent_sources:
    - mstic
  independent: false
  independent_test_failed: >
    Single MSTIC primary in window. Corpus grep across `threats/`
    for `moika`, `4nd3r50n`, `ce-rwb`, `t-in-one`, "dependency
    confusion", "33 malicious" returned zero prior mentions (only
    the three 2026-05-30 raw-signal sentinels referencing this very
    item). Sentinel AM-30 (2026-05-30 07:35 EDT) and the prior 00:00
    + 06:00 FLASH sentinels confirmed no BleepingComputer / The
    Hacker News / Security Affairs / The Register / Socket / Snyk /
    StepSecurity / Wiz / Semgrep / Aikido relay arrived in the
    ~12-hour window since MSTIC publication (2026-05-29 20:06 EDT).
    The cluster anchor is single-source MSTIC.
  single_source_veto_applied: true
  single_source_veto_layer: campaign_envelope_and_operator_attribution_claim
  wep_ceiling_with_veto: likely

first_party_precedence:
  applied: false
  splunk_query_executed: true
  splunk_query: 'index=defenseclaw_local OR index=archimedes ("oob.moika.tech" OR "moika.tech" OR "mr.4nd3r50n" OR "ce-rwb" OR "t-in-one" OR "ogvanta" OR "l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1" OR "sberpay-widget" OR "capibar.chat" OR "sber-ecom-core" OR "cloudplatform-single-spa") earliest=-14h@h'
  splunk_event_count: 0
  splunk_silent_not_contradictory: true
  hard_rule_8_notes: >
    Splunk re-queried at grading time -14h@h across full 11-token
    IOC set (C2 domain, three maintainer aliases, third alias's
    registry email `ogvanta`, X-Secret shared secret value,
    Sberbank SberPay widget package name, three scope names) on
    both defenseclaw_local and archimedes indices. Result: 0 events.
    Sentinel pre-check at 00:00 was identical. Absence of evidence
    is not evidence of absence per CLAUDE.md Hard Rule 8 doctrine.
    First-party precedence not applied — no Splunk attestation to
    bump or contradict. defenseclaw_local index continues the
    60-consecutive-day dormant pattern noted by AM-30 sentinel.

wep_ceiling: likely
wep_layered:
  campaign_exists_per_mstic: very_likely                                # MSTIC primary, vendor self-attestation on own telemetry, coordinated takedown executed
  iocs_valid_oob_moika_tech_x_secret_value_yandex_ru_aliases: very_likely  # MSTIC IOC publication, internally coherent, defender-grade artifacts
  packages_removed_by_npm_before_publication: very_likely               # MSTIC vendor coordination claim
  three_accounts_one_individual_high_confidence: likely                 # MSTIC operator-level attribution, single-source veto applies
  recon_only_mode_with_followon_exploit_toggle: likely                  # MSTIC analytic characterization, single-source
  two_phase_methodological_signature_recon_now_exploit_later: likely    # Analytic framing, defensible from MSTIC observation but single-source
  bug_bounty_to_malware_operator_lifecycle_mr_4nd3r50n: likely          # MSTIC forensic-registry observation, single-source
  any_apt_or_nation_state_attribution: NOT_ARCHIMEDES_ORIGINATED        # Hard Rule 2 binding; MSTIC explicitly declines APT attribution
  shai_hulud_teampcp_mini_shai_hulud_vt006_lineage_link: NOT_ARCHIMEDES_ORIGINATED  # MSTIC does NOT link; Archimedes does NOT originate
  ad_dib_itar_aerospace_targeting: not_applicable_explicit_absence      # MSTIC target set is Russian-speaking fintech / e-commerce / generic dev infra, not DIB
  dib_developer_environment_structural_exposure_via_dependency_confusion: roughly_even_chance  # Mechanism is broadly applicable to ANY dev environment, but this specific cluster is not targeting A&D — defensive guidance still relevant
  followon_exploitation_phase_will_activate_against_some_recon_victims: roughly_even_chance  # Server-side toggle exists per MSTIC, but no evidence of activation; outcome contingent on operator decisions

# Cluster metadata
cluster:
  topic: >
    Microsoft MSTIC discloses an active npm dependency-confusion
    supply-chain campaign: 33 malicious packages registered under
    nine spoofed organizational scopes by three new maintainer
    aliases (mr.4nd3r50n, ce-rwb, t-in-one — all yandex.ru),
    assessed with high confidence to be operated by a single
    individual; obfuscated ~7KB postinstall stager delivers
    platform-specific payload from `oob.moika.tech` gated by a
    hardcoded `X-Secret` HTTP header; payload runs in RECON_ONLY
    mode with a server-side toggle for follow-on exploitation;
    target ecosystem is Russian-speaking fintech (Sberbank SberPay)
    + e-commerce (Wildberries-shaped) + generic dev infrastructure,
    NO A&D / DIB / ITAR nexus; npm coordinated removal of all
    packages before publication; MSTIC explicitly declines
    APT / nation-state attribution (operator-level attribution
    only); no lineage link to Shai-Hulud / TeamPCP / Mini Shai-Hulud
    despite operating in adjacent territory.
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-30-flash-0000-001-mstic-33-malicious-npm-dependency-confusion-recon-only-mode-oob-moika-tech-c2-no-roster-attribution-no-ad-nexus-am-handoff
  attribution_claims:
    - claimed_actor: null
      claimed_by_sources: [mstic]
      claim_language: "three accounts operated by the same individual (high confidence)"
      attribution_level: operator_only_no_apt_no_nation_state
      requires_analyst_review: true
      notes: >
        MSTIC names NO tracked threat actor. MSTIC explicitly
        declines APT / nation-state attribution; the attribution
        is operator-level only based on forensic npm registry
        metadata analysis. The three aliases (`mr.4nd3r50n`,
        `ce-rwb`, `t-in-one`) are not in the Archimedes roster.
        Per Hard Rule 2, Archimedes does NOT extend attribution
        beyond MSTIC's stated operator-level claim. MSTIC also
        does NOT link this cluster to Shai-Hulud / TeamPCP / Mini
        Shai-Hulud / vpmdhaj (the May 28 distinct MSTIC-disclosed
        cluster covered in finding-2026-05-29-0001) despite all
        four operating in npm supply-chain adjacent territory.
        Analyst should NOT originate a lineage claim; cross-cluster
        comparison may be appropriate as an analytic observation
        but cannot promote to attribution.

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - ioc_index_update
  ineligible_for:
    - flash    # 0 of 6 FLASH triggers fired (per sentinel disposition); no A&D nexus; AM-collection-class only
    - actor_profile_update    # No tracked roster actor named; three aliases are not in roster; MSTIC declines APT attribution
  rationale: >
    Cluster meets B2-minimum inclusion threshold for action-item
    brief inclusion (A2 anchor with single-source veto capping WEP
    at "likely"). Not FLASH-eligible — zero of six FLASH triggers
    fired per sentinel evaluation; no A&D nexus; AM-collection-class
    only. Not actor-profile-eligible — no tracked roster actor
    named, MSTIC declines APT attribution, three aliases are not
    in roster. IOC index update warranted (23 indicators total: 1
    C2 domain, 3 C2 URL paths, 3 maintainer email addresses, 3 npm
    accounts, 1 shared-secret HTTP-header value, 9 spoofed npm
    scopes, 3 spoofed enterprise metadata domains, 1 detection
    pattern, 1 filename — full enumeration in raw-signal). The
    X-Secret value is an unusually strong defender-grade signal:
    any HTTP request carrying `X-Secret: l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1`
    to any host is high-confidence malicious regardless of
    destination.

# Downstream handoff flags
analyst_review_required: true
analyst_review_reason: >
  Three questions require analyst structured-analysis judgment:
    (1) RECON_ONLY + two-phase methodological signature — does
        the "recon now, exploit later" payload-state framing
        warrant treatment as a distinct TTP-class observation
        worth recording in actor-profiler / vuln-tracker doctrine,
        or is it a routine staged-attack signal? Recommend
        SAT-KAC on the assumption "MSTIC's RECON_ONLY framing
        is methodologically novel."
    (2) Bug-bounty-account → malware-operator lifecycle pattern
        — `mr.4nd3r50n`'s 2024-04 v0.0.0 "Bugbounty" tagged
        packages followed by a ~2-year quiet period and then
        malicious activity in 2026-05-28 is an operator-lifecycle
        signal worth documenting. Does this pattern warrant a
        cross-corpus lookup against historical npm bug-bounty
        accounts as a hunting hypothesis? Recommend SAT-ACH on
        the lifecycle pattern's predictive value.
    (3) Cross-cluster comparison — vpmdhaj (finding-2026-05-29-0001,
        MSTIC 2026-05-28), the 33-package cluster (this finding,
        MSTIC 2026-05-29), and the broader Shai-Hulud / TeamPCP /
        Mini Shai-Hulud (VT-006) campaign tree all operate in
        npm supply-chain credential-stealer adjacent territory
        but MSTIC explicitly declines to link any of them. The
        analyst should explicitly affirm the grader's conservative
        posture: do NOT originate a lineage claim across these
        three clusters. The comparison is an analytic observation,
        not an attribution. Recommend documenting in a brief
        side-note as cross-corpus cluster geometry.

red_team_review_required: false
red_team_review_required_reason: >
  WEP ceiling caps at "likely" (not "very likely" or higher) due
  to single-source veto on campaign envelope and all
  attribution-adjacent claims. Per CLAUDE.md pipeline doctrine,
  red-team review threshold is WEP "very likely" or higher.
  Red-team review not required. Analyst may escalate to red-team
  if BleepingComputer / The Hacker News / Socket / Snyk / Wiz /
  StepSecurity follow-up arrives later today and bumps WEP above
  "likely."

red_team_review: null

# Analyst review status
analyst_review_complete: true
analyst_review_run_id: analyst-20260530-083500
analyst_sats_applied: [sat-kac, sat-ach-bug-bounty-lifecycle, sat-ach-cross-cluster-lineage]
wep_ceiling_adjusted: false
wep_ceiling_adjustment_reason: >
  WEP ceiling remains "likely" per grader's single-source veto
  application. Analyst SATs surfaced caveats on the RECON_ONLY
  intent-vs-staging-convenience assumption (KAC A1 classified as
  test-required) and affirmed grader's conservative posture on
  cross-cluster lineage. None of the analyst findings warrant
  raising the ceiling above "likely"; none warrant lowering it
  below "likely" either (the underlying campaign-envelope and IOC
  facts remain at A2 / probably true). Grade unchanged.
assessment_blocked_pending_test: false
finding_blocking_concerns: []
finding_publication_ready: true
finding_publication_ready_notes: >
  Publication-ready for the 2026-05-30 morning brief with the
  briefer-actionable framing adjustments noted below. NO
  finding-blocking concerns. The KAC A1 test classification
  (RECON_ONLY-as-intent assumption) does NOT block publication —
  it requires the briefer to report MSTIC's RECON_ONLY observation
  as a factual payload-state claim, NOT as an operator-intent
  signal of patience / strategic discipline. The cross-cluster
  ACH AFFIRMS the grader's conservative posture; brief side-note
  on cluster geometry is appropriate as analytic observation, NOT
  attribution.
briefer_actionable_caveats:
  - id: caveat_recon_only_framing
    target_section: technical_detail_recon_only_paragraph
    instruction: >
      Report MSTIC's RECON_ONLY observation as a factual claim
      about the deployed payload's behavior. Do NOT promote the
      "recon now, exploit later" phrasing into a strategic-intent
      claim. Suggested rewording: "MSTIC observes the deployed
      payload currently runs in a reconnaissance-only state with
      a server-side toggle for follow-on exploitation; whether
      this reflects deliberate operator patience or mid-development
      tooling shipped early is not determinable in window."
  - id: caveat_cross_cluster_observation
    target_section: relationship_to_existing_findings
    instruction: >
      Brief side-note on cross-cluster geometry is appropriate.
      Frame as: "MSTIC published two distinct npm supply-chain
      findings 22 hours apart (vpmdhaj 2026-05-28, 33-package
      cluster 2026-05-29) and did NOT link them. The 33-package
      cluster diverges from vpmdhaj on C2 architecture, payload
      posture, Defender family-signature classification, primitive
      choice, and maintainer-profile inflection — analyst ACH
      affirms the clusters are methodologically distinct on
      MSTIC's reported evidence. Per Hard Rule 2, Archimedes does
      NOT originate a lineage claim." See sat_ach cross_cluster_lineage
      block for the full pressure-test record.
  - id: caveat_bug_bounty_lifecycle_observation
    target_section: technical_detail_or_open_questions
    instruction: >
      The bug-bounty-account-to-malware-operator lifecycle is a
      defensible analytic OBSERVATION worth recording but NOT a
      basis for cross-corpus attribution. ACH ranks "deliberate
      account-aging-as-cover" (H2) as most parsimonious; "genuine
      bug-bounty pivot" (H1) cannot be ruled out. Suggested
      briefer framing: "MSTIC notes mr.4nd3r50n's npm history shows
      v0.0.0 'Bugbounty'-tagged packages in 2024, ~2-year dormancy,
      then 2026-05-28 malicious bursts. Analyst ACH suggests this
      is most likely a deliberate account-aging-as-cover pattern;
      cross-corpus hunting for similar dormant-then-burst npm
      accounts is a defensible follow-on but not predictive of
      attribution."
analysis_sections:
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "MSTIC's RECON_ONLY mode + server-side toggle for follow-on
        exploitation is a methodologically meaningful operator-level
        signal of patience and strategic intent (quiet long-tail data
        collection over immediate compromise), warranting treatment as
        a distinct TTP-class observation worth recording in
        vuln-tracker / actor-profiler doctrine."
      analyzed_at: 2026-05-30T08:35:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Pre-publication review for 2026-05-30 morning brief. Grader
        question 1 — interrogate the "recon-now-exploit-later"
        framing before it propagates into doctrine or actor scoring.
      assumptions:
        - id: A1
          statement: >
            The deployed payload's RECON_ONLY behavior reflects a
            deliberate operator decision to stage reconnaissance now
            with follow-on exploitation deferred, rather than a
            development/staging convenience (operator not finished
            building stage-2, server-side toggle is a placeholder).
          category: intent
          stated: true
          why_must_be_true: >
            The "patience / strategic intent" framing rests on this
            being a planned posture, not an incomplete one. If the
            toggle is just a placeholder for unfinished tooling, the
            signal is operator-immaturity, not operator-discipline.
          when_could_be_false: >
            Operator is building stage-2 in parallel and shipped the
            recon harness early; toggle is a deploy-time scaffold.
            Bursty publication pattern (2 windows ~14h apart, then
            silence) is more consistent with iterative deploy than
            patient long-tail.
          evidence_for: [mstic]
          evidence_against: []
          confidence: low
          centrality: critical
          classification: test
        - id: A2
          statement: >
            A server-side toggle architecture is methodologically
            distinct from routine staged-malware operation. Most
            credential-stealer-class supply-chain payloads in this
            corpus deliver stage-2 on first contact; recon-then-pause
            is a meaningful TTP differentiator.
          category: ttp_patterns
          stated: true
          why_must_be_true: >
            If most comparable campaigns also gate stage-2 server-side,
            the framing is descriptive of the class, not a
            distinguishing observation.
          when_could_be_false: >
            Cross-corpus check shows vpmdhaj (two-generation stager),
            TeamPCP tree, mouse5212, and the broader Shai-Hulud family
            all use multi-stage architectures with operator-controlled
            gating. Server-side toggles are common in modern
            supply-chain credential stealers.
          evidence_for: [mstic]
          evidence_against:
            - finding-2026-05-29-0001-mstic-vpmdhaj-npm-typosquat-shaiworm-cloud-cicd-credential-theft-bun-runtime-abuse-distinct-cluster-lineage-suggestion
          confidence: low
          centrality: material
          classification: qualify
        - id: A3
          statement: >
            MSTIC's payload analysis comprehensively maps the toggle
            state — i.e., the C2 truly has not activated stage-2
            against any victim, vs. activating selectively against
            non-MSTIC-monitored victims.
          category: visibility
          stated: false
          why_must_be_true: >
            "Currently RECON_ONLY" claim depends on MSTIC observing
            the C2's behavior across all observed victims, not just
            telemetry MSTIC sees.
          when_could_be_false: >
            C2 server-side logic could return stage-2 only to victims
            whose fingerprint matches a target set MSTIC's Defender
            telemetry under-samples (Russian-speaking dev environments,
            Sberbank-adjacent CI/CD). MSTIC observed RECON_ONLY in
            their visibility cone; stage-2 activation outside that
            cone is unobservable to MSTIC.
          evidence_for: [mstic]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A4
          statement: >
            "Quiet long-tail data collection" requires operator
            persistence to remain valuable. The operator will keep
            the C2 alive and continue collecting through the
            takedown window.
          category: actor_operational_status
          stated: false
          why_must_be_true: >
            "Patient strategic intent" framing presumes the operator
            sustains the operation post-detection. If C2 goes dark
            within 72h of MSTIC publication, the operator's posture
            was opportunistic, not patient.
          when_could_be_false: >
            Operator burns the C2 the moment MSTIC publishes (typical
            cybercriminal hygiene); reconnaissance collected during the
            bursts is then a finite-yield asset, not a long-tail one.
          evidence_for: []
          evidence_against: []
          confidence: unknown
          centrality: material
          classification: qualify
        - id: A5
          statement: >
            Recording RECON_ONLY-as-TTP-class in actor-profiler /
            vuln-tracker doctrine would change how Archimedes scores
            or categorizes future supply-chain findings.
          category: semantic
          stated: true
          why_must_be_true: >
            The grader's question asks whether to elevate this to
            doctrine. If recording it changes nothing operationally,
            the question is moot.
          when_could_be_false: >
            Archimedes's threat-box methodology does not have a
            "deployment-state of operator tooling" axis;
            actor-profiler dossiers do not score recon-vs-exploit
            posture. Recording the observation has no downstream
            operational effect beyond a side-note in this finding.
          evidence_for:
            - doctrine_threat_box_methodology
            - doctrine_actor_profile_standard
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A6
          statement: >
            MSTIC's payload reverse-engineering correctly identifies
            the toggle as a server-side decision point rather than a
            client-side dead branch or development artifact.
          category: technology
          stated: false
          why_must_be_true: >
            The "two-phase design" reading depends on the toggle
            being functional, server-controlled, and intentional.
          when_could_be_false: >
            Toggle could be client-side dead code (developer left a
            conditional branch unwired); could be a server endpoint
            that returns the same recon-only payload regardless of
            state; could be vestigial from a code-template the
            operator copied.
          evidence_for: [mstic]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
      classifications_summary:
        sound: 1
        qualify: 4
        test: 1
        reject: 0
      remediation:
        status: revise_assessment
        blocking_assumption: A1
        blocking_detail: >
          A1 (intent-vs-staging-convenience) is critical-centrality
          with low confidence and no test in-window. The grader's
          framing of "patience / strategic intent" cannot be defended
          on MSTIC's single-source observation alone — the same
          payload state is equally consistent with mid-development
          tooling shipped early.
        qualifying_caveats:
          - >
            RECON_ONLY framing is reported per MSTIC; the inference
            that it reflects deliberate operator patience rather than
            mid-build tooling is NOT independently supported in window.
          - >
            Server-side gating of stage-2 is common across modern
            npm credential-stealer campaigns (vpmdhaj two-generation
            stager, broader Shai-Hulud family) — the architectural
            pattern is not by itself methodologically novel.
          - >
            MSTIC's visibility cone is Defender-telemetry-shaped;
            stage-2 activation against victims outside that cone is
            unobservable from MSTIC's vantage.
        next_action: >
          Brief should report MSTIC's RECON_ONLY observation as a
          factual payload-state claim, NOT as an operator-intent
          signal. Do NOT promote "two-phase methodological
          signature" to vuln-tracker / actor-profiler doctrine on
          this single observation. Tripwire: if MSTIC or another
          A-grade source later documents the toggle flipping
          against any victim, or documents the C2 remaining alive
          14+ days post-publication, the patience-framing becomes
          testable. Re-run KAC then.
      recommended_wep_after_test:
        if_A1_confirmed_deliberate: likely
        if_A1_confirmed_staging_convenience: drop_two_phase_framing_entirely
        if_A1_unclear: report_observation_only_no_intent_inference

  sat_ach:
    bug_bounty_lifecycle:
      ach_analysis:
        question: >
          What best explains the operator trajectory of npm account
          `mr.4nd3r50n`: April 2024 v0.0.0 "Bugbounty"-tagged packages,
          ~2-year quiet period, then bursts of 26 malicious packages
          on 2026-05-28 from the same account?
        analyzed_at: 2026-05-30T08:40:00-04:00
        analyzed_by: analyst
        red_team_review: null
        hypotheses:
          - id: H1
            statement: >
              Same operator pivot — `mr.4nd3r50n` is the same individual
              throughout; the 2024 activity was legitimate bug-bounty
              research (or research-shaped staging) and the operator
              transitioned to malicious activity in 2026, either
              ideologically or financially motivated.
          - id: H2
            statement: >
              Throwaway pre-staging — the 2024 v0.0.0 packages were
              always intended as account-aging cover; the operator
              registered the account, posted innocuous "Bugbounty"-tagged
              dummies to establish baseline reputation, then waited the
              dormancy interval before activation as a deliberate OPSEC
              maneuver.
          - id: H3
            statement: >
              Account purchase / handoff — `mr.4nd3r50n` was registered
              and used by one party in 2024, sold or transferred (via
              underground marketplace, OPSEC handoff, or compromise) to
              a different party who reactivated it in 2026 for malicious
              use. The 2024 and 2026 actors are different individuals.
          - id: H4
            statement: >
              Compromised legitimate account — a legitimate 2024
              bug-bounty researcher's npm account credentials were
              stolen (credential stuffing, phishing, dev-machine
              compromise), and the malicious 2026 activity is the
              attacker using a hijacked, aged account.
          - id: H5
            statement: >
              Null / coincidence — the 2024 and 2026 activities are
              unrelated within npm registry metadata; the name reuse is
              coincidental or the package metadata MSTIC analyzed
              conflates two distinct registry records.
          - id: H6
            statement: >
              Composite — operator used the account for legitimate
              bug-bounty work in 2024, was recruited/coerced/financially
              motivated to weaponize the aged account themselves
              (insider-to-malicious transition with the same hands on
              keyboard but different organizational sponsorship).
        evidence:
          - id: E1
            description: >
              Same npm account `mr.4nd3r50n` is the registry-recorded
              publisher for both the 2024-04 v0.0.0 "Bugbounty" packages
              and the 2026-05-28 malicious bursts (forensic npm
              registry metadata per MSTIC).
            source: mstic
            digraph: A2
            weight: 3
          - id: E2
            description: >
              Same yandex.ru email (`mr.4nd3r50n@yandex.ru`) registered
              on the account across both activity windows.
            source: mstic
            digraph: A2
            weight: 3
          - id: E3
            description: >
              2024 packages tagged "Bugbounty" with v0.0.0 versions —
              the canonical pattern for bug-bounty researchers staking
              an npm namespace claim during a coordinated disclosure
              workflow.
            source: mstic
            digraph: A2
            weight: 3
          - id: E4
            description: >
              ~2-year quiet interval between 2024-04 and 2026-05-28
              activity on this account. No intervening npm publishing
              activity reported.
            source: mstic
            digraph: A2
            weight: 3
          - id: E5
            description: >
              MSTIC assesses with high confidence that `mr.4nd3r50n`,
              `ce-rwb`, and `t-in-one` are operated by the same
              individual based on forensic registry metadata. Two of
              the three (`ce-rwb`, `t-in-one`) are new-2026 accounts
              with no prior history.
            source: mstic
            digraph: A2
            weight: 3
          - id: E6
            description: >
              Third alias's email-to-account mismatch (`ce-rwb` account
              paired with `ogvanta@yandex.ru` email) shows deliberate
              operator OPSEC, suggesting an operationally-aware actor
              consistent with intentional staging rather than naive
              account reuse.
            source: mstic
            digraph: A2
            weight: 3
          - id: E7
            description: >
              No evidence in MSTIC reporting of credential theft,
              account compromise indicators (e.g., publisher session
              hijack, unusual login geography, npm 2FA bypass), or
              hijack-pattern signals on `mr.4nd3r50n`.
            source: mstic
            digraph: A2
            weight: 2
          - id: E8
            description: >
              No public bug-bounty report, HackerOne disclosure, npm
              security advisory, or CVE attribution exists for the
              2024 `mr.4nd3r50n` v0.0.0 packages — the "Bugbounty" tag
              is self-applied without an external bug-bounty trail.
            source: corpus_negative
            digraph: B3
            weight: 1
          - id: E9
            description: >
              Splunk first-party silent on the operator aliases and
              C2 over -14h@h; defenseclaw_local index continues 60-day
              dormant pattern — does not distinguish hypotheses but
              constrains H5 (coincidence is consistent with silence,
              but silence does not require coincidence).
            source: splunk_negative
            digraph: A1
            weight: 1
        matrix:
          E1: {H1: C, H2: C, H3: C, H4: C, H5: I, H6: C}
          E2: {H1: C, H2: C, H3: C, H4: C, H5: I, H6: C}
          E3: {H1: C, H2: C, H3: N, H4: C, H5: N, H6: C}
          E4: {H1: C, H2: C, H3: C, H4: C, H5: N, H6: C}
          E5: {H1: C, H2: C, H3: I, H4: I, H5: N, H6: C}
          E6: {H1: C, H2: C, H3: N, H4: I, H5: N, H6: C}
          E7: {H1: C, H2: C, H3: N, H4: I, H5: N, H6: C}
          E8: {H1: I, H2: C, H3: N, H4: I, H5: N, H6: I}
          E9: {H1: N, H2: N, H3: N, H4: N, H5: C, H6: N}
        inconsistency_counts:
          H1: 1
          H2: 0
          H3: 1
          H4: 4
          H5: 2
          H6: 1
        diagnostic_evidence:
          - E5: >
              "Same individual operates all three accounts (high
              confidence)" — strongly inconsistent with H3 (account
              handoff to a different party) and H4 (compromise of one
              account by an attacker who then operates two other new
              accounts). Same individual + new-2026 accounts strongly
              imply operator-controlled tooling, not stolen creds.
          - E6: >
              Deliberate OPSEC mismatch on the third alias suggests
              operationally-aware actor — inconsistent with the
              "victim of compromise" framing of H4.
          - E7: >
              No reported compromise indicators on `mr.4nd3r50n` —
              materially inconsistent with H4.
          - E8: >
              No external bug-bounty trail for the 2024 packages —
              inconsistent with H1 (genuine bug-bounty researcher
              would typically have at least one disclosed report or
              HackerOne handle) and weakens H6 (genuine-then-pivoted
              insider). Most consistent with H2 (staged cover).
        ranking:
          - rank: 1
            hypothesis_id: H2
            rationale: >
              Zero inconsistencies. The dormancy interval, "Bugbounty"
              tag without external bug-bounty trail, deliberate OPSEC
              mismatch on the third alias (E6), and MSTIC's
              same-individual assessment across three accounts (E5)
              all align with deliberate account-aging as cover. Most
              parsimonious explanation given E8 negative.
            wep: likely
          - rank: 2
            hypothesis_id: H1
            rationale: >
              One inconsistency (E8). Pivot from genuine bug-bounty to
              malicious is plausible (operator-trajectory pattern
              documented across other ecosystems), but the absence of
              an external bug-bounty trail is awkward — a genuine
              researcher would typically have at least one HackerOne
              or coordinated-disclosure record. Cannot be ruled out.
            wep: roughly_even_chance
          - rank: 3
            hypothesis_id: H6
            rationale: >
              One inconsistency (E8). Composite scenario (genuine
              insider weaponized) shares H1's bug-bounty-trail problem
              and adds complexity without resolving it. Less
              parsimonious than H2.
            wep: unlikely
          - rank: 4
            hypothesis_id: H3
            rationale: >
              One inconsistency (E5). Account handoff is inconsistent
              with MSTIC's same-individual assessment across all three
              accounts — would require the handoff recipient to also
              operate two unrelated new accounts.
            wep: unlikely
          - rank: 5
            hypothesis_id: H5
            rationale: >
              Two inconsistencies (E1, E2). Same account name AND
              same email across both windows make coincidence
              extremely strained.
            wep: very_unlikely
          - rank: 6
            hypothesis_id: H4
            rationale: >
              Four inconsistencies (E5, E6, E7, E8). Compromised
              account framing is inconsistent with MSTIC's
              same-individual assessment, OPSEC discipline observed,
              and absence of compromise indicators.
            wep: very_unlikely
        sensitivity_analysis:
          brittleness: medium
          load_bearing_evidence: [E5, E8]
          if_E5_downgraded: >
            If MSTIC's same-individual high-confidence assessment is
            later qualified (e.g., second source disputes the
            three-account linkage), H3 (handoff) becomes competitive
            with H2. Ranking gap H2 → H3 collapses.
          if_E8_reinterpreted: >
            If a 2024 bug-bounty disclosure trail for `mr.4nd3r50n`
            surfaces (HackerOne handle, CVE credit, npm advisory),
            H1 becomes competitive with H2. Ranking gap H2 → H1
            collapses; assessment moves to "roughly even chance"
            between the two.
          single_point_of_failure: >
            E5 is the strongest single-point-of-failure. MSTIC's
            attribution at the three-account level is single-source;
            the entire H3/H4 rejection rests on it.
        tripwires:
          - observation: >
              A 2024 bug-bounty disclosure trail (HackerOne handle,
              CVE credit, coordinated-disclosure record) tied to
              `mr.4nd3r50n`@yandex.ru surfaces.
            effect: >
              H1 (genuine pivot) becomes ranking-competitive with H2.
              Re-run ACH.
          - observation: >
              A second A/B-grade source disputes MSTIC's
              same-individual three-account linkage.
            effect: >
              E5 weight drops; H3 (handoff) rises. Re-run ACH.
          - observation: >
              Another aged-then-burst npm account is documented with
              the same v0.0.0 "Bugbounty" tag pattern.
            effect: >
              Strengthens H2 by establishing a cross-corpus
              account-aging-as-cover pattern. Recommend cross-corpus
              hunt across historical npm accounts with v0.0.0
              "Bugbounty"-tagged staging packages followed by
              dormancy then malicious bursts.
        conclusion:
          summary: >
            The bug-bounty-account-to-malware-operator trajectory is
            most parsimoniously explained as deliberate
            account-aging-as-cover (H2): an operator registered the
            account in 2024, posted innocuous "Bugbounty"-tagged
            v0.0.0 staging packages to establish baseline registry
            reputation, then waited ~2 years before activating the
            account for the dependency-confusion campaign. The
            absence of an external bug-bounty trail for the 2024
            packages and the deliberate OPSEC discipline observed in
            the third alias (account-email mismatch) align with H2.
            Genuine bug-bounty pivot (H1) cannot be ruled out and
            sits second. Account handoff (H3) and account compromise
            (H4) are materially inconsistent with MSTIC's
            same-individual assessment across all three accounts.
            The analytic value of this finding is the hypothesis
            itself, not the attribution — Archimedes does NOT name
            the operator beyond MSTIC's alias-level reporting.
          wep: likely
          confidence_caveats: >
            Single-source dependence on MSTIC for E5 caps WEP at
            "likely" per single-source veto. The H2 ranking depends
            on MSTIC's three-account same-individual assessment
            holding; if that's qualified later, H3 rises. Cross-corpus
            hunting hypothesis (search historical npm accounts for
            v0.0.0 "Bugbounty"-tag + dormancy + malicious-burst
            pattern) is a defensible follow-on but should NOT be
            framed as predictive of attribution.

    cross_cluster_lineage:
      ach_analysis:
        question: >
          Does MSTIC's reported evidence on the 33-package cluster
          (oob.moika.tech, X-Secret-gated C2, three yandex.ru aliases,
          inflated-version dependency confusion) support, refute, or
          remain neutral on lineage to any Archimedes-roster-tracked
          supply-chain actor (TeamPCP / Shai-Hulud lineage)? Per
          Hard Rule 2, Archimedes does NOT originate attribution; this
          ACH evaluates ONLY whether MSTIC's reported evidence supports
          or refutes lineage MSTIC did NOT make.
        analyzed_at: 2026-05-30T08:45:00-04:00
        analyzed_by: analyst
        red_team_review: null
        hypotheses:
          - id: H1
            statement: >
              The 33-package cluster is methodologically distinct from
              the TeamPCP / Shai-Hulud / vpmdhaj credential-stealer
              family — a separate operator running a separate
              campaign with no MSTIC-stated lineage link.
          - id: H2
            statement: >
              The 33-package cluster shares operational lineage with
              the broader Shai-Hulud family (including TeamPCP and
              vpmdhaj) — same actor or same toolkit family, but MSTIC
              has chosen not to state the linkage publicly.
          - id: H3
            statement: >
              The 33-package cluster is TTP-adjacent only — same
              broad TTP class (npm supply chain, postinstall hooks,
              obfuscated stagers) but distinct toolkit, infrastructure,
              and operator. The adjacency reflects shared TTP-class
              ecosystem, not shared lineage.
          - id: H4
            statement: >
              The 33-package cluster is a copycat / TTP-clone — a new
              operator reusing publicly-documented Shai-Hulud-family
              TTPs (inflated versions, postinstall hooks, obfuscated
              stagers) without operational connection.
          - id: H5
            statement: >
              MSTIC's silence on lineage is operationally significant
              — vendor-internal classification deliberately declines
              to link, suggesting MSTIC has positive evidence the
              clusters are separate but is not publishing the
              underlying analysis.
        evidence:
          - id: E1
            description: >
              33-package cluster's C2 architecture is HTTP GET with
              hardcoded `X-Secret` header gate (single-secret
              shared-key authentication) returning platform-specific
              payload.
            source: mstic
            digraph: A2
            weight: 3
          - id: E2
            description: >
              vpmdhaj's (finding-2026-05-29-0001) C2 architecture is
              two-generation HTTP beacon (Gen-1 `aab.sportsontheweb.net`
              plain HTTP; Gen-2 Bun-runtime loader from `oven.sh/bun/releases`)
              — distinct two-stage architecture, no shared-secret
              header gate.
            source: mstic_finding_2026_05_29_0001
            digraph: A2
            weight: 3
          - id: E3
            description: >
              33-package cluster's payload runs in RECON_ONLY mode
              (environment fingerprinting + credential reconnaissance
              via environment variables passed to detached process),
              with server-side toggle for follow-on.
            source: mstic
            digraph: A2
            weight: 3
          - id: E4
            description: >
              vpmdhaj's payload is full credential stealer — AWS
              IMDSv2 + ECS task creds, HashiCorp Vault tokens,
              GitHub Actions secrets, AWS Secrets Manager across
              16+ regions, npm publish tokens. Active exfiltration
              on first contact, not RECON_ONLY.
            source: mstic_finding_2026_05_29_0001
            digraph: A2
            weight: 3
          - id: E5
            description: >
              33-package cluster carries NO Defender `Trojan:JS/ShaiWorm`
              family signature per MSTIC's IOC publication — only
              generic obfuscated-stager and postinstall-hook signatures
              are referenced.
            source: mstic
            digraph: A1
            weight: 3
          - id: E6
            description: >
              vpmdhaj carries `Trojan:JS/ShaiWorm` family signature
              — MSTIC's internal classification signal places it in
              the Shai-Hulud lineage view, even though MSTIC's article
              body declines to state the TeamPCP attribution.
            source: mstic_finding_2026_05_29_0001
            digraph: A1
            weight: 3
          - id: E7
            description: >
              33-package cluster uses inflated-version-number
              dependency confusion (100.100.100, 99.5.7, 99.5.8) —
              Birsan-2021-lineage primitive, broadly applicable across
              the npm supply-chain ecosystem.
            source: mstic
            digraph: A1
            weight: 2
          - id: E8
            description: >
              vpmdhaj uses typosquat (not dependency confusion) —
              different primitive within the same broad TTP class.
            source: mstic_finding_2026_05_29_0001
            digraph: A2
            weight: 3
          - id: E9
            description: >
              33-package cluster maintainers (mr.4nd3r50n, ce-rwb,
              t-in-one) all use yandex.ru email addresses; target
              scope includes Sberbank SberPay and Wildberries shapes
              (Russian-speaking ecosystem inflection).
            source: mstic
            digraph: A2
            weight: 2
          - id: E10
            description: >
              vpmdhaj maintainer uses gmail.com email
              (a39155771@gmail.com); target ecosystem is OpenSearch /
              ElasticSearch / DevOps configuration (no Russian-speaking
              inflection).
            source: mstic_finding_2026_05_29_0001
            digraph: A2
            weight: 2
          - id: E11
            description: >
              MSTIC publishes both findings (vpmdhaj 2026-05-28,
              33-package 2026-05-29) and explicitly does NOT link them
              despite publishing within 22 hours of each other and
              both being npm supply-chain attacks. MSTIC's article on
              the 33-package cluster does not reference vpmdhaj,
              TeamPCP, or Shai-Hulud.
            source: mstic
            digraph: A1
            weight: 3
          - id: E12
            description: >
              No independent source (BleepingComputer, The Hacker News,
              Socket, Snyk, Wiz, StepSecurity, Semgrep, Aikido) has
              published lineage analysis on the 33-package cluster in
              the ~12-hour window since MSTIC publication.
            source: corpus_negative
            digraph: A2
            weight: 2
        matrix:
          E1: {H1: C, H2: N, H3: C, H4: C, H5: C}
          E2: {H1: C, H2: I, H3: C, H4: C, H5: C}
          E3: {H1: C, H2: N, H3: C, H4: C, H5: C}
          E4: {H1: C, H2: I, H3: C, H4: C, H5: C}
          E5: {H1: C, H2: I, H3: C, H4: C, H5: C}
          E6: {H1: N, H2: N, H3: N, H4: N, H5: N}
          E7: {H1: N, H2: C, H3: C, H4: C, H5: N}
          E8: {H1: C, H2: I, H3: C, H4: C, H5: C}
          E9: {H1: C, H2: N, H3: C, H4: C, H5: C}
          E10: {H1: C, H2: I, H3: C, H4: C, H5: C}
          E11: {H1: C, H2: N, H3: C, H4: C, H5: C}
          E12: {H1: N, H2: N, H3: N, H4: N, H5: N}
        inconsistency_counts:
          H1: 0
          H2: 6
          H3: 0
          H4: 0
          H5: 0
        diagnostic_evidence:
          - E2_vs_E1: >
              C2 architecture diverges (two-generation HTTP beacon vs.
              X-Secret-gated single-stage). Distinguishes H2 (shared
              lineage) from H1/H3/H4.
          - E4_vs_E3: >
              Payload posture diverges (active full credential stealer
              vs. RECON_ONLY with toggle). Inconsistent with shared
              tooling.
          - E5_vs_E6: >
              Defender family-signature classification diverges —
              `Trojan:JS/ShaiWorm` present on vpmdhaj, absent on
              33-package cluster. MSTIC's internal classifier is
              materially inconsistent with shared-lineage framing.
          - E8_vs_E7: >
              Primitive diverges within the same TTP class (typosquat
              vs. dependency confusion). Consistent with H3 (TTP-class
              adjacency without shared toolkit).
          - E11: >
              MSTIC declines to link despite publishing within 22h.
              Strong negative signal for H2 (shared lineage with
              undisclosed MSTIC-internal classification).
        ranking:
          - rank: 1
            hypothesis_id: H1
            rationale: >
              Zero inconsistencies. C2 architecture, payload posture,
              Defender family-signature classification, primitive
              choice, maintainer-email inflection, and target ecosystem
              all diverge from vpmdhaj / Shai-Hulud / TeamPCP. MSTIC's
              explicit non-linkage is consistent.
            wep: likely
          - rank: 2
            hypothesis_id: H3
            rationale: >
              Zero inconsistencies. TTP-class adjacency (npm supply
              chain, postinstall hooks, obfuscated stagers) is real
              and observed but does not require shared lineage —
              shared TTP-class is consistent with separate operators
              in the same ecosystem. Essentially co-equal with H1;
              H1 is preferred only because it makes the
              non-linkage more parsimonious.
            wep: likely
          - rank: 3
            hypothesis_id: H4
            rationale: >
              Zero inconsistencies. Copycat / TTP-clone is possible
              but adds the assumption of public-TTP-replay. The
              dependency-confusion primitive is well-publicized
              (Birsan 2021), so the copycat framing is plausible but
              speculative without a clear motive signal.
            wep: unlikely
          - rank: 4
            hypothesis_id: H5
            rationale: >
              Zero inconsistencies but unfalsifiable — MSTIC's silence
              is consistent with both "positive evidence of separateness"
              and "no analysis performed." Cannot be promoted without
              evidence of MSTIC's internal analytic posture.
            wep: unlikely
          - rank: 5
            hypothesis_id: H2
            rationale: >
              Six inconsistencies — C2 architecture, payload posture,
              Defender family-signature classification, primitive
              choice, maintainer-email inflection, and MSTIC's
              explicit non-linkage all point against shared lineage.
              Ruled out on MSTIC's reported evidence.
            wep: very_unlikely
        sensitivity_analysis:
          brittleness: low
          load_bearing_evidence: [E2, E4, E5, E11]
          if_E5_reinterpreted: >
            If MSTIC later publishes a `Trojan:JS/ShaiWorm` signature
            or related family-name signature for the 33-package
            cluster, E5 flips and H2 (shared lineage) becomes
            ranking-competitive with H1. Re-run ACH.
          if_E11_reinterpreted: >
            If MSTIC publishes a follow-on article explicitly linking
            the 33-package cluster to vpmdhaj or Shai-Hulud, H2 rises.
            Re-run ACH.
          robustness_note: >
            Six independent diagnostic divergences (C2, payload,
            classifier, primitive, maintainer profile, MSTIC silence)
            make H2 (shared lineage) materially inconsistent. Even
            full downgrade of any single diagnostic still leaves
            five others pointing the same direction. Assessment is
            robust.
        tripwires:
          - observation: >
              MSTIC publishes a Defender `ShaiWorm` family signature
              for the 33-package cluster.
            effect: >
              E5 flips; H2 becomes competitive with H1. Re-run ACH.
          - observation: >
              Wiz / Snyk / StepSecurity / Semgrep / Aikido cohort
              publishes lineage analysis linking the 33-package
              cluster to TeamPCP or to vpmdhaj.
            effect: >
              External-source lineage claim arrives; H2 rises. Re-run
              ACH. NOTE: per Hard Rule 2, Archimedes still does NOT
              originate; the trigger is a sourced claim Archimedes
              can pressure-test, not generate.
          - observation: >
              `oob.moika.tech` infrastructure overlap with vpmdhaj's
              `aab.sportsontheweb.net` is documented (shared registrar,
              shared NS, common SSL fingerprint).
            effect: >
              Infrastructure-overlap signal would be the strongest
              single piece of pro-lineage evidence; if surfaced, H2
              rises dramatically. Re-run ACH.
        conclusion:
          summary: >
            MSTIC's reported evidence on the 33-package cluster
            REFUTES shared lineage with vpmdhaj / Shai-Hulud / TeamPCP.
            C2 architecture (X-Secret-gated single-stage vs.
            two-generation Bun-runtime), payload posture (RECON_ONLY
            with toggle vs. active full credential stealer), MSTIC's
            internal classifier (no `Trojan:JS/ShaiWorm` family
            signature), primitive choice (dependency confusion vs.
            typosquat), maintainer profile (yandex.ru / Russian-speaking
            inflection vs. gmail / DevOps-config target ecosystem),
            and MSTIC's explicit non-linkage across two findings
            published 22 hours apart all point the same direction.
            The most defensible analytic posture is: the
            33-package cluster is methodologically distinct, with
            TTP-class adjacency at most. The grader's conservative
            posture (do NOT originate a lineage claim) is AFFIRMED.
            Cross-cluster geometry is documentable as analytic
            observation only — six diagnostic divergences in MSTIC's
            own evidence base argue against shared lineage; one
            external-source claim or one MSTIC follow-on could flip
            this, but neither has arrived.
          wep: likely
          confidence_caveats: >
            Hard Rule 2 applies — Archimedes is testing MSTIC's
            reported evidence against MSTIC's own non-linkage claim,
            NOT generating an attribution. The "distinct cluster"
            conclusion is the AFFIRMATION of MSTIC's posture, not a
            novel Archimedes-side attribution. Single-source
            dependence on MSTIC for both findings caps WEP at
            "likely" per single-source veto. If Wiz / Snyk /
            StepSecurity / Semgrep / Aikido cohort relays a lineage
            link, re-run ACH with their evidence weighted.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-30-morning]    # back-written by librarian post-publication
retracted: false
retraction_brief_id: null

# Grader-only handoff notes
grader_handoff_notes: >
  Single MSTIC primary; A-grade vendor source; strong technical
  content; full 23-IOC set already extracted in raw-signal (do
  NOT re-enumerate here — point to raw-signal for full list);
  three named maintainer aliases (NOT in Archimedes roster); MSTIC
  explicit decline of APT / nation-state attribution; explicit
  absence of A&D / DIB / ITAR nexus; X-Secret value
  `l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1` is the strongest single
  defender-grade detection artifact (universal HTTP header signal
  regardless of destination). Briefer guidance: action-item brief
  inclusion with explicit "no A&D nexus, defensive guidance
  warranted because mechanism is broadly applicable" framing.
  Vuln-tracker handoff: consider standalone VT scaffold (no
  CVE class, supply-chain campaign tracker). Actor-profiler
  handoff: NONE — no roster actor named, do NOT scaffold a new
  actor on three unknown yandex.ru aliases per Hard Rule 2 and
  per ACTOR-PROFILE-STANDARD threshold practice. Cross-cluster
  observation re vpmdhaj / Shai-Hulud / TeamPCP / Mini Shai-Hulud
  for analyst SAT consideration but Archimedes does NOT originate
  lineage. Splunk first-party silent over -14h@h on 11-token
  IOC subset; full IOC sweep recommended at IOC-index update
  step.

source_health_concerns: []    # No source-health issues surfaced
deviation_from_sentinel_recommendation: none    # Sentinel suggested WEP "likely"; grader confirms WEP "likely" via single-source veto application
---

# MSTIC discloses 33-package npm dependency-confusion cluster — three yandex.ru aliases, RECON_ONLY mode with follow-on toggle, `oob.moika.tech` C2 with `X-Secret` gate, no APT attribution, no A&D nexus

## Summary

Microsoft MSTIC published a primary-research disclosure on 2026-05-29 20:06 EDT covering an active npm dependency-confusion campaign: 33 malicious packages registered under nine spoofed organizational scopes by three new maintainer aliases (`mr.4nd3r50n`, `ce-rwb`, `t-in-one` — all yandex.ru email addresses), assessed with high confidence to be operated by a single individual based on forensic npm registry metadata analysis. All packages ship the same ~7KB obfuscated postinstall stager that posts to a single C2 endpoint (`oob.moika.tech`) gated by a hardcoded shared secret (`l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1`), with platform-specific payload delivery (Windows / macOS / Linux) currently running in RECON_ONLY mode but with a server-side toggle for follow-on exploitation. Target ecosystem is Russian-speaking fintech (Sberbank SberPay impersonation), e-commerce (Wildberries shape), and generic dev infrastructure — explicit absence of A&D / DIB / ITAR / aerospace targeting. MSTIC + npm team coordinated removal of all packages before publication. MSTIC explicitly declines APT / nation-state attribution; the attribution is operator-level only. Per Hard Rule 2, Archimedes does not extend the attribution to any roster actor; the three aliases are not in the Archimedes roster.

## Sources

### Microsoft MSTIC / Microsoft Security Blog (mstic, digraph A — grade A per source-grades.yaml)

- URL: https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/
- Published: 2026-05-29T20:06:20-04:00
- Byline: Microsoft Defender Security Research Team
- Key claim: 33 malicious npm packages were registered under nine spoofed organizational scopes by three new maintainer aliases (all yandex.ru) employing dependency confusion via inflated version numbers; all packages ship the same obfuscated postinstall stager that fetches a platform-specific payload from `oob.moika.tech` gated by an `X-Secret` HTTP header; payload runs in RECON_ONLY mode with a server-side toggle for follow-on exploitation; npm coordinated removal of all packages; MSTIC attributes only at the operator level (single individual, high confidence) and does NOT make any APT / nation-state claim.
- Direct quote (≤15 words, Hard Rule 6): "three accounts operated by the same individual"

## Technical detail

**Campaign envelope.** Thirty-three malicious npm packages registered under nine spoofed organizational scopes (`@cloudplatform-single-spa`, `@wb-track`, `@data-science`, `@ce-rwb`, `@payments-widget`, `@travel-autotests`, `@t-in-one`, `@capibar.chat`, `@sber-ecom-core`) by three maintainer accounts (`mr.4nd3r50n`, `ce-rwb`, `t-in-one`) — all using yandex.ru email addresses (`mr.4nd3r50n@yandex.ru`, `ogvanta@yandex.ru` (note: maintainer account name `ce-rwb` paired with registry email `ogvanta` — likely deliberate operator OPSEC), `t-in-one@yandex.ru`). Publication occurred in two bursts: 2026-05-28 18:47-19:03 UTC (~16-minute window) and 2026-05-29 09:01-09:02 UTC (~1-minute window). The `mr.4nd3r50n` account's first npm activity dates to April 2024 (v0.0.0 packages tagged "Bugbounty"), followed by a ~2-year quiet period, then malicious activity beginning 2026-05-28. The other two accounts are new-2026.

**Dependency confusion mechanism.** All packages use **inflated version numbers** (`100.100.100`, `99.5.7`, `99.5.8`) — the canonical winning-tactic for the dependency-confusion primitive since Birsan 2021. When a victim's `package.json` references a private internal package name that collides with one of these public-registry impostors, npm's resolver prefers the public package on first install if the configured registry / version constraints allow it.

**Execution chain.** Every malicious package includes `scripts/postinstall.js` — an ~7KB Obfuscator.io-style obfuscated stager invoked automatically by `npm install`. The stager:

1. Collects host context (platform, arch, environment variables).
2. Sends an HTTPS GET to `oob.moika.tech/payload/{win,mac,linux}` corresponding to the host platform.
3. Includes the hardcoded HTTP header `X-Secret: l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1` on the request — the C2 returns the payload only if the header is present and matches.
4. Spawns the platform-specific payload as a detached process; environment-variable context is passed via process environment.

**RECON_ONLY mode with server-side toggle.** MSTIC's payload analysis assesses the current operator state as RECON_ONLY: the deployed payload performs environment fingerprinting and credential-reconnaissance (environment variables, host metadata) but does not execute follow-on exploitation. A server-side toggle exists for activation of a follow-on phase; MSTIC does not document the post-toggle payload state because the C2 has not (as of publication) activated it. This **two-phase design — recon now, exploit later** — is the methodological signature worth flagging for analyst review; it differentiates a supply-chain campaign that intends quiet long-tail data collection from one that intends immediate compromise.

**Spoofed enterprise metadata.** Each package's `package.json` references fake enterprise repository URLs: `github.cloudplatform-single-spa.io`, `docs.cloudplatform-single-spa.io`, `jira.cloudplatform-single-spa.io`. These are not actual GitHub Enterprise instances — defenders can alert on any environment that resolves or attempts to fetch from these hostnames.

**Target ecosystem (no A&D nexus).** The impersonated organizational scopes target:
- `@sber-ecom-core` — Sberbank SberPay payment widget (Russian retail bank).
- `@capibar.chat` — likely consumer messaging clone.
- `@wb-track` — likely Wildberries (Russian e-commerce).
- `@data-science`, `@cloudplatform-single-spa`, `@payments-widget`, `@travel-autotests`, `@ce-rwb`, `@t-in-one` — generic dev-infrastructure shapes.

The MSTIC report makes **zero defense-contractor / DIB / ITAR / aerospace references**. The lure surface is consumer fintech + e-commerce + generic enterprise dev infrastructure with a Russian-speaking inflection. Structural relevance to an A&D prime is indirect at most: a defense prime's developer environment IS exposed to dependency-confusion-class attacks broadly, and the X-Secret detection pattern is universally applicable, but this specific cluster is not targeting the DIB surface.

**MITRE ATT&CK mapping.** T1195.002 (Supply Chain Compromise: Software Dependencies), T1059.007 (Command and Scripting Interpreter: JavaScript), T1027 (Obfuscated Files or Information), T1071.001 (Application Layer Protocol: Web Protocols), T1574 (Hijack Execution Flow via npm lifecycle hook), T1041 (Exfiltration Over C2 Channel).

**Defensive detection opportunities (universally applicable regardless of target ecosystem).**

- **Universal HTTP-header signal.** Any outbound HTTP request carrying the header `X-Secret: l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1` to any destination is high-confidence malicious — the value is unique and hardcoded.
- **DNS / proxy block.** `oob.moika.tech` and the spoofed enterprise metadata hostnames (`github.cloudplatform-single-spa.io`, `docs.cloudplatform-single-spa.io`, `jira.cloudplatform-single-spa.io`) are trivial DNS / proxy block candidates.
- **npm policy.** Scope / maintainer allowlisting on internal package registries prevents dependency-confusion attacks of this class as a category; inflated-version-number detection (any public package version higher than a private-registry version) is a strong second-line signal.
- **Postinstall hook restriction.** `npm install --ignore-scripts` or organization-wide policy disabling lifecycle scripts blocks the postinstall stager regardless of which packages are installed.

## IOCs surfaced

**Full IOC set (23 indicators) is enumerated in the raw-signal source file**: `threats/raw-signal/raw-2026-05-30-flash-0000-001-mstic-33-malicious-npm-dependency-confusion-recon-only-mode-oob-moika-tech-c2-no-roster-attribution-no-ad-nexus-am-handoff.md` — see the `## IOCs` section. Per grader doctrine, IOCs are referenced rather than re-enumerated to avoid duplication; the librarian's IOC-index regeneration will pick up the full set.

Summary breakdown:
- **1 C2 domain** (`oob.moika.tech`)
- **3 C2 URL paths** (`/payload/win`, `/payload/mac`, `/payload/linux`)
- **3 maintainer email addresses** (all yandex.ru)
- **3 npm publisher accounts** (`mr.4nd3r50n`, `ce-rwb`, `t-in-one`)
- **1 shared-secret HTTP header value** (`X-Secret: l95HdDaz3kQx1Zsg3WxH6HvKANf51RY1` — strongest universal detection artifact)
- **9 spoofed npm organizational scopes**
- **3 spoofed enterprise metadata domains** (`*.cloudplatform-single-spa.io`)
- **1 behavior detection pattern** (postinstall hook + HTTPS GET to `oob.moika.tech/payload/{win,mac,linux}` with `X-Secret` header)
- **1 filename** (`scripts/postinstall.js`, Obfuscator.io-style ~7KB)

## Relationship to existing findings

This finding is a **distinct cluster** with no MSTIC-stated lineage link to any prior corpus item. Three related-but-distinct prior findings are worth noting for analyst cross-cluster geometry consideration only (NOT as a lineage claim):

- **finding-2026-05-29-0001 (MSTIC vpmdhaj npm typosquat, 2026-05-28)** — distinct MSTIC-disclosed npm supply-chain campaign by a different single actor (`vpmdhaj` maintainer alias, `a39155771@gmail.com` registry email), targeting OpenSearch / ElasticSearch / DevOps configuration libraries (NOT dependency confusion; typosquat instead), with a Defender `Trojan:JS/ShaiWorm` family-name signal (suggesting MSTIC internal classification in the Shai-Hulud lineage but MSTIC does NOT state actor attribution). The 33-package cluster (THIS finding) carries NO `ShaiWorm` family-name signal — MSTIC does NOT classify it in the Shai-Hulud lineage.
- **finding-2026-05-25-0002 (TeamPCP supply-chain activity consolidation)** — broader npm supply-chain credential-stealer campaign tree previously attributed by Wiz / Snyk / StepSecurity to TeamPCP (roster id 001). MSTIC makes no link from the 33-package cluster to TeamPCP.
- **finding-2026-05-27-0008 (mouse5212 super-formatter npm Claude AI user-data credential stealer)** — distinct npm supply-chain credential-stealer campaign, unattributed.

The four npm supply-chain clusters (this finding, vpmdhaj, TeamPCP tree, mouse5212) all operate in adjacent territory but no source has stated any cross-cluster lineage link. Per Hard Rule 2, Archimedes does NOT originate one. The analyst may document the **cluster geometry** as an analytic observation but cannot promote it to attribution.

## Open questions for analyst

1. **RECON_ONLY + two-phase methodological signature.** MSTIC's "recon now, exploit later" framing of the payload state is a methodologically novel observation. Does it warrant treatment as a distinct TTP-class worth recording in vuln-tracker / actor-profiler doctrine? Recommend **SAT-KAC** on the assumption "MSTIC's RECON_ONLY framing is methodologically novel."

2. **Bug-bounty-account → malware-operator lifecycle.** `mr.4nd3r50n`'s 2024-04 v0.0.0 "Bugbounty" tagged packages → ~2-year quiet period → 2026-05-28 malicious activity is an operator-lifecycle signal. Does this pattern warrant a cross-corpus hunting hypothesis against historical npm bug-bounty accounts? Recommend **SAT-ACH** on the lifecycle pattern's predictive value.

3. **Cross-cluster geometry.** Affirm or revise the grader's conservative posture: vpmdhaj (MSTIC 2026-05-28), the 33-package cluster (MSTIC 2026-05-29), the TeamPCP / Mini Shai-Hulud (VT-006) campaign tree, and the mouse5212 campaign all operate in adjacent npm-supply-chain credential-stealer territory but MSTIC declines to link any of them. Archimedes does NOT originate a lineage claim. The analyst should explicitly document the cross-cluster geometry as an analytic observation (NOT attribution) in a brief side-note.

4. **A&D defensive applicability vs. target-ecosystem mismatch.** The mechanism (dependency confusion + obfuscated postinstall stager + X-Secret-gated platform-specific payload) is broadly applicable to ANY dev environment, but the specific cluster's target set is Russian-speaking fintech / e-commerce. The defensive guidance (X-Secret header detection, oob.moika.tech block, postinstall-hook restriction, scope/maintainer allowlisting) is universally relevant. Should the brief lead with "no A&D nexus but defensive guidance still applies" framing, or treat as a monitoring-only item? Grader recommends action-item inclusion with the explicit framing because the X-Secret HTTP-header value is an unusually strong universal detection artifact.

## Analytic notes (from analyst review)

Three SATs applied — one KAC, two ACH. Bottom lines for the briefer:

**RECON_ONLY framing — KAC says report-but-don't-promote.** The "recon now, exploit later" phrasing is grader-supplied analytic language, not MSTIC's. The critical-centrality assumption inside it is that the payload's recon-only state reflects deliberate operator patience rather than mid-development tooling shipped early; that assumption is low-confidence on a single source and cannot be tested in window. Server-side gating is also common across modern npm credential-stealer campaigns (vpmdhaj's two-generation stager, the broader Shai-Hulud family), so the architectural pattern is not by itself methodologically novel. Brief should report MSTIC's observation as a factual payload-state claim, NOT promote it to an operator-intent signal or to vuln-tracker / actor-profiler doctrine.

**Bug-bounty-to-malware lifecycle — ACH ranks "deliberate account-aging-as-cover" first.** Six hypotheses tested: same-operator pivot, throwaway pre-staging, account handoff, compromised legitimate account, null/coincidence, composite insider-weaponized. H2 (account-aging-as-cover) has zero inconsistencies; H1 (genuine pivot) has one (absence of any external bug-bounty trail for the 2024 packages). H3/H4 (handoff/compromise) are materially inconsistent with MSTIC's same-individual three-account assessment. Cross-corpus hunting for v0.0.0 "Bugbounty"-tag + dormancy + malicious-burst pattern is a defensible follow-on; it is NOT predictive of attribution. Sensitivity is medium — H1 rises if a 2024 bug-bounty trail later surfaces.

**Cross-cluster geometry — ACH AFFIRMS grader's conservative posture.** Six independent diagnostic divergences between this cluster and vpmdhaj — C2 architecture, payload posture, Defender family-signature classification, primitive choice, maintainer-profile inflection, and MSTIC's explicit non-linkage across two findings published 22 hours apart — all argue against shared lineage. H1 (methodologically distinct) and H3 (TTP-class adjacency only) tie at zero inconsistencies; H2 (shared lineage MSTIC has chosen not to publish) has six. Per Hard Rule 2, Archimedes is NOT originating a non-linkage claim — it is testing MSTIC's reported evidence against MSTIC's own posture and finding the posture supported. The cross-cluster observation belongs in the brief as analytic geometry, not as attribution.

**Finding is publication-ready** for the 08:00 brief at WEP "likely" — no blocking concerns; three caveats for the briefer captured in the `briefer_actionable_caveats` field of the frontmatter.
