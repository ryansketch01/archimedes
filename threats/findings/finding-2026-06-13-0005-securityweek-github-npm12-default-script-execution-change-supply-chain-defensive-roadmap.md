---
id: finding-2026-06-13-0005
finding_id: finding-2026-06-13-0005-securityweek-github-npm12-default-script-execution-change-supply-chain-defensive-roadmap
title: "GitHub announces NPM 12 default behavior change (expected July 2026) blocking preinstall/install/postinstall/prepare scripts from dependencies + git/remote-URL dependency resolution; opt-in allowlist via npm approve-scripts; motivated by TeamPCP (roster #001 HIGH) and Shai-Hulud (NOT on roster — operator-deferred /new-actor candidate, second this week after Velvet Ant) supply-chain campaigns; structural ecosystem-level defensive response continuing the supply-chain-of-developer-tooling cluster"
date: 2026-06-13
created_at: 2026-06-13T16:12:00-04:00
graded_by: grader
grading_run_id: afternoon-20260613-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- GITHUB VENDOR PRIMARY (REFERENCED, NOT DIRECTLY RETRIEVED) ----
  github_announced_npm_12_default_script_execution_change: A2       # GitHub canonical on own product roadmap; reach-through via SecurityWeek single-source verbatim relay; A-grade on the underlying claim
  npm_12_expected_release_july_2026_per_securityweek_relay: B2      # Date as relayed; not vendor-direct-retrieved this sweep
  # ---- DEFAULT BEHAVIOR CHANGES ----
  preinstall_scripts_from_dependencies_blocked_by_default: B2       # SecurityWeek as canonical news-tier relay; vendor reach-through pending direct GitHub blog retrieval
  install_scripts_from_dependencies_blocked_by_default: B2
  postinstall_scripts_from_dependencies_blocked_by_default: B2
  prepare_scripts_blocked_for_git_file_link_dependencies: B2
  native_node_gyp_builds_with_binding_gyp_no_explicit_install_affected: B2
  git_dependencies_will_not_resolve_unless_explicitly_allowed: B2
  remote_url_https_tarball_dependencies_require_allow_remote_flag: B2
  # ---- OPT-IN ALLOWLIST MECHANIC ----
  npm_approve_scripts_command_generates_allowlist_in_package_json: B2
  functional_equivalent_to_pnpm_and_bun_already_take_this_approach: A2  # Industry-knowledge confirmable per pnpm + bun published docs; not contested
  npm_11_16_0_or_later_provides_preparation_upgrade_path: B2
  # ---- THREAT-ACTOR / CAMPAIGN REFERENCE LAYER ----
  teampcp_roster_001_HIGH_named_as_motivating_campaign: A1            # TeamPCP verifiable on _roster.yaml at #001 with threat_level HIGH; SecurityWeek paraphrasing earlier industry reporting, not new attribution
  teampcp_exploited_automatic_script_execution_during_npm_install_TTP_already_in_dossier: A2  # TTP already documented in TeamPCP dossier; relayed via SecurityWeek
  shai_hulud_named_as_motivating_campaign_NOT_on_roster: B2          # SecurityWeek paraphrasing earlier industry reporting; Archimedes does NOT originate the Shai-Hulud attribution
  shai_hulud_self_replicating_worm_weaponized_binding_gyp_files: B2  # SecurityWeek paraphrasing; technical claim plausible (binding.gyp is the standard node-gyp build descriptor; weaponization vector is consistent with TeamPCP / supply-chain-of-developer-tooling cluster TTPs)
  both_campaigns_described_as_infected_thousands_of_developers_with_malware: B3  # Aggregate-scale qualitative claim; single-source SecurityWeek paraphrase
  # ---- ATTRIBUTION-DISCIPLINE LAYER (HARD RULE 2 BINDING) ----
  teampcp_attribution_preserved_verbatim_from_existing_roster_entry_NOT_origination: A1  # Hard Rule 2 binding
  shai_hulud_attribution_carry_forward_from_earlier_industry_reporting_via_securityweek_NOT_origination: A1  # Hard Rule 2 binding — SecurityWeek references earlier industry reporting; Archimedes does NOT originate the Shai-Hulud designation; actor-profiler /new-actor candidate flagged for operator review
  no_cross_walk_attempted_between_teampcp_and_shai_hulud: A1          # Hard Rule 2 binding
  # ---- CROSS-CLUSTER CONTEXT LAYER ----
  continues_supply_chain_of_developer_tooling_cluster_from_2026_06_12_pm: A2  # Verifiable per finding-2026-06-12-pm-* corpus (AUR 400+ packages + Atomic Arch Rust stealer + eBPF rootkit; NanoClaw rejected; Tenet Agentjacking 85% success vs Claude Code + Cursor; Sygnia Velvet Ant)
  most_aggressive_ecosystem_level_defensive_response_in_cluster: B3   # Qualitative assessment; structural inference based on default-block being a stricter posture than per-package security guidance
  # ---- A&D / DIB RELEVANCE LAYER ----
  ad_direct_relevance: A1                                              # NONE — NPM is the JavaScript package ecosystem; not aerospace-defense; A&D primes consume NPM via developer tooling for non-flight-software web/internal apps and developer-machine infection risk
  ad_structural_relevance_npm_pervasive_in_developer_tooling_supply_chain: B2  # Structural inference; A&D primes commonly use NPM-driven JS/TS for internal web apps, developer tooling, build pipelines, CI/CD, infrastructure-as-code, AI agent harnesses (LangChain/LangGraph/Claude Code/Cursor) — all of which pull NPM dependencies
  developer_endpoint_infection_via_install_scripts_is_initial_access_to_corp_lateral_movement: B3  # Structural inference following the cluster's pivot narrative
  # ---- VULN-TRACKER / ACTOR-PROFILER HANDOFF LAYER ----
  no_cve_associated_defensive_product_roadmap_not_vulnerability_remediation: A1
  no_vuln_tracker_dossier_warranted: A1
  actor_profiler_teampcp_dossier_ttp_evolution_timeline_update_warranted: A2  # Material for the TeamPCP dossier's TTP-evolution timeline (defensive response motivated by their TTP)
  actor_profiler_shai_hulud_new_actor_scaffold_candidate_operator_deferred: B2  # Second roster-gap candidate this week after Velvet Ant; operator-deferred handoff appropriate per /new-actor command workflow
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Usually Reliable + Probably True) on
  SecurityWeek news-tier first-publisher coverage of GitHub's
  vendor product-roadmap announcement of NPM 12 default behavior
  change blocking preinstall/install/postinstall/prepare scripts
  from dependencies and gating git/remote-URL dependency
  resolution unless explicitly allowed.

  SINGLE-PUBLISHER NEWS-TIER COVERAGE with vendor reach-through:
  SecurityWeek (B-grade ratified) cites GitHub as the source of the
  announcement; direct GitHub blog retrieval was not executed this
  sweep (URL not surfaced). The underlying claim is GitHub-canonical
  on its own product roadmap (A-grade by the vendor-on-own-product
  convention); the SecurityWeek piece is the news-tier vehicle.
  This is the textbook defensive-roadmap pattern from INTEL-
  GRADING.md inclusion-thresholds: defensive product changes are
  highly stable (low information-extraction risk) and
  single-publisher-with-direct-vendor-reference is treated as
  sufficient for B2 inclusion.

  ON THE THREAT-ACTOR / CAMPAIGN REFERENCE LAYER, TeamPCP is on
  _roster.yaml at #001 with threat_level HIGH; the TTP claim
  ("exploited automatic script execution during npm install") is
  consistent with the existing dossier — this is TTP-restatement
  via news relay, NOT new attribution. Shai-Hulud is NOT on
  _roster.yaml; SecurityWeek's reference to Shai-Hulud as a
  "self-replicating worm" weaponizing binding.gyp is preserved
  verbatim per Hard Rule 2 (SecurityWeek paraphrasing earlier
  industry reporting; Archimedes does NOT originate the Shai-Hulud
  designation). Shai-Hulud is the second roster-gap candidate this
  week after Velvet Ant (finding-2026-06-12-0004); operator-deferred
  /new-actor handoff appropriate.

  CRITICAL LAYERED NUANCE — the B2 attests to:
    (a) the announced NPM 12 default behavior changes per
        SecurityWeek's relay of GitHub's roadmap;
    (b) the npm approve-scripts allowlist mechanic and the
        --allow-remote flag for remote URL dependencies;
    (c) the TeamPCP TTP-restatement (NOT new attribution) and the
        Shai-Hulud verbatim-preserved campaign reference;
    (d) the cluster-continuity framing within the supply-chain-
        of-developer-tooling narrative.

  The B2 does NOT attest to:
    - the absolute July 2026 release date for NPM 12 (vendor
      reach-through pending direct GitHub blog retrieval);
    - the "infected thousands of developers" aggregate-scale claim
      (single-source SecurityWeek paraphrase; B3 layer);
    - any net-new Shai-Hulud actor characterization beyond what
      SecurityWeek paraphrases;
    - any cross-walk between TeamPCP and Shai-Hulud (Hard Rule 2
      binding);
    - A&D-prime developer-tooling infection beyond structural
      inference.

  WEP CEILING DERIVATION:
    - Vendor product-roadmap layer: "likely" per B2 + single-
      publisher + vendor reach-through pending direct retrieval.
    - TeamPCP TTP-restatement layer: "very_likely" per A1 +
      verifiable roster entry + TTP already in dossier; this is
      restatement not novel claim.
    - Shai-Hulud campaign-reference layer: "likely" per B2 +
      single-source SecurityWeek paraphrasing earlier industry
      reporting + verbatim preservation.
    - A&D structural-relevance layer: "likely" per structural
      inference; no A&D-prime developer-tooling infection
      observed in this disclosure.

  SINGLE-SOURCE VETO STATUS: Applied on the aggregate-scale claim
  ("infected thousands of developers") and on the GitHub reach-
  through (vendor blog not directly retrieved this sweep). The B2
  cluster anchor reflects the SecurityWeek single-publisher status
  with vendor reference but without independent corroboration of
  the announcement (which is fine for a defensive-roadmap pattern
  — multiple news publishers will likely pick up GitHub's blog
  post within 48 hours; corroboration update can fold in
  post-promotion).

source_reliability:
  primary_sources:
    - id: securityweek
      name: "SecurityWeek (Ionut Arghire)"
      grade: B
      provisional: false
      role: >
        News-tier first publisher of GitHub's NPM 12 roadmap
        announcement, 2026-06-13 11:52 EDT. Article relays GitHub
        announcement verbatim with full default-behavior-change
        list, allowlist mechanic, and threat-actor / campaign
        references (TeamPCP + Shai-Hulud). SecurityWeek is the
        Archimedes-corpus collection vehicle for the GitHub
        announcement.
    - id: github-blog-self-disclosure
      name: "GitHub Blog (referenced via SecurityWeek; not directly retrieved this sweep)"
      grade: A
      provisional: true
      provisional_since: 2026-06-13
      provisional_reason: >
        SecurityWeek attributes "the source of these announcements"
        to GitHub. GitHub blog is canonical on own-product roadmap
        at A-grade by vendor-on-own-product convention. URL was
        not surfaced or directly retrieved this sweep; reach-
        through is via SecurityWeek's verbatim characterization.
        Pending operator ratification at next 72h provisional-
        grade review window. NOTE: The github-blog-self-disclosure
        ID may already exist in source-grades.yaml under a related
        umbrella (github-advisories at B per INTEL-GRADING.md);
        this provisional entry covers the GitHub Blog product-
        roadmap surface specifically.
      role: >
        Vendor canonical primary on own product roadmap. SecurityWeek
        is the vehicle, not the primary; the announcement belongs to
        GitHub. Direct GitHub blog retrieval pending for next sweep.
  cross_corroboration_test: >
    INTEL-GRADING.md Step 4 cross-check: SINGLE-PUBLISHER coverage
    of vendor-roadmap announcement. SecurityWeek + GitHub
    reach-through is one effective source on the announcement
    layer (SecurityWeek is relaying GitHub; not independent of
    GitHub's claim). Single-source veto APPLIES on the announcement
    layer. WEP ceiling on the GitHub-roadmap-as-announced: "likely".
    Multiple publisher pickup expected within 48 hours; corroboration
    update can fold in post-promotion. The TeamPCP TTP-restatement
    is independently anchored in the existing roster entry and
    dossier, not dependent on this single-publisher coverage. The
    Shai-Hulud reference is single-source-SecurityWeek-paraphrasing-
    earlier-industry-reporting; treated as carry-forward not
    novel.

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_ttps_teampcp_and_supply_chain_of_developer_tooling_cluster
    - probably_true_no_contradicting_ab_source
    - probably_true_claims_coherent_default_block_pattern_consistent_with_pnpm_bun_industry_pattern
  rationale: >
    Cluster credibility = 2 (Probably True) on SecurityWeek's
    coverage of GitHub's NPM 12 roadmap. The technical changes are
    internally coherent and consistent with the established pnpm /
    bun security-aware approach (industry-knowledge confirmable).
    TeamPCP TTP reference matches the existing dossier. Shai-Hulud
    reference is single-source paraphrasing earlier industry
    reporting; preserved verbatim per Hard Rule 2. No contradicting
    A/B-grade source. NOT promoted to grade 1 because direct GitHub
    blog retrieval is pending and the Shai-Hulud campaign reference
    is not independently corroborated within the Archimedes corpus.

corroboration:
  independent_sources_announcement_layer:
    - securityweek-2026-06-13-with-github-vendor-reference
  independent_announcement: false
  announcement_single_source_veto: >
    Only SecurityWeek covers GitHub's NPM 12 announcement in this
    sweep window. Single-source veto applies. Multiple publisher
    pickup expected within 48 hours; corroboration update post-
    promotion. The vendor reach-through is structural (GitHub's
    own product roadmap; not subject to independent corroboration
    by definition), so the announcement itself is highly stable.
  independent_sources_teampcp_ttp_layer:
    - existing_archimedes_roster_001_teampcp_dossier
    - securityweek_2026_06_13_restatement
    - prior_industry_reporting_referenced_by_securityweek
  independent_teampcp_ttp: true
  test_passed_teampcp_ttp_layer: >
    TeamPCP TTP is independently anchored in the existing roster
    entry and dossier. The SecurityWeek reference is restatement,
    not novel. The cumulative evidence basis for the TTP claim
    crosses Step 4.

first_party_precedence:
  applied: false
  splunk_evidence: null
  rationale: >
    Defensive product roadmap; no malicious IOCs to query. No
    Splunk sentinel possible. First-party inapplicable.

single_source_veto_applied: true                # On the GitHub announcement layer (single-publisher SecurityWeek + vendor reach-through pending direct retrieval) and on the Shai-Hulud campaign-reference layer
single_source_veto_scope: announcement_layer_and_shai_hulud_reference_layer
wep_ceiling: likely
wep_layered:
  vendor_product_roadmap_layer: likely           # B2 + single-publisher SecurityWeek + GitHub reach-through pending direct retrieval
  teampcp_ttp_restatement_layer: very_likely     # A1 + verifiable roster entry + TTP already in dossier
  shai_hulud_campaign_reference_layer: likely    # B2 + single-source SecurityWeek + Hard Rule 2 verbatim preservation
  cluster_continuity_supply_chain_of_developer_tooling_layer: very_likely  # Verifiable per 2026-06-12 PM corpus
  ad_structural_relevance_layer: likely          # Structural inference

inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update_teampcp_dossier_ttp_evolution_timeline
    - actor_profiler_handoff_shai_hulud_new_actor_evaluation
  not_eligible_for:
    - flash                                       # Defensive product roadmap; no FLASH triggers fired

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "GitHub NPM 12 default script-execution change (expected July 2026); preinstall/install/postinstall/prepare scripts blocked by default + git/remote-URL dependency resolution gated; opt-in allowlist via npm approve-scripts; supply-chain defensive roadmap motivated by TeamPCP (roster #001) and Shai-Hulud (operator-deferred /new-actor candidate)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-13-pm-002-securityweek-github-npm12-default-script-execution-change-supply-chain-defensive-roadmap
  update_relationship:
    update_type: new_finding
    parent_finding: null
    related_findings:
      - finding-2026-06-12-pm-XX  # AUR 400+ packages cluster from 2026-06-12 afternoon brief
      - finding-2026-06-12-pm-XX  # Tenet Agentjacking research
    rationale: >
      First Archimedes-corpus finding on NPM 12 default behavior
      change. Continues the supply-chain-of-developer-tooling cluster
      from the 2026-06-12 afternoon brief but is a structural
      defensive-response framing rather than a continuation of any
      specific compromise event. New finding (not UPDATE).
  attribution_claims:
    - claimed_actor: "TeamPCP"
      cluster_id: "001"   # _roster.yaml
      claimed_by_sources:
        - securityweek-2026-06-13
      attribution_language: "exploited automatic script execution during npm install"
      attribution_confidence_language: securityweek_paraphrasing_earlier_industry_reporting_restatement
      requires_analyst_review: false  # Restatement of existing dossier TTP, not new attribution
      hard_rule_2_compliance: >
        Attribution NOT originated by Archimedes. TeamPCP is on
        _roster.yaml at #001 with HIGH threat_level; the TTP claim
        is already in the dossier. SecurityWeek is restating a
        documented TTP, not making a new attribution claim.
      actor_profiler_handoff_warranted: true
      actor_profiler_handoff_rationale: >
        Material for the TeamPCP dossier's TTP-evolution timeline —
        NPM 12 default-block is a structural ecosystem-level
        defensive response to TeamPCP's documented TTP. Update
        dossier with NPM 12 as a defensive-response milestone.
    - claimed_actor: "Shai-Hulud"
      cluster_id: NOT_ON_ROSTER
      claimed_by_sources:
        - securityweek-2026-06-13
      attribution_language: "self-replicating worm that weaponized binding.gyp files"
      attribution_confidence_language: securityweek_paraphrasing_earlier_industry_reporting
      requires_analyst_review: true
      hard_rule_2_compliance: >
        Attribution NOT originated by Archimedes. SecurityWeek
        references Shai-Hulud as a known industry-reported campaign
        designation. Archimedes preserves verbatim and does NOT
        originate. Shai-Hulud is NOT currently on _roster.yaml; this
        is the second roster-gap candidate this week after Velvet
        Ant (finding-2026-06-12-0004).
      actor_profiler_handoff_warranted: true
      actor_profiler_handoff_rationale: >
        /new-actor scaffold candidate. Operator-deferred handoff
        appropriate (no immediate Hard Rule 5 gate fire — Shai-Hulud
        is described as a self-replicating worm not yet documented
        targeting A&D primes per available reporting). Recommend
        operator review and /new-actor invocation at operator's
        cadence convenience. Roster #001 TeamPCP cluster proximity
        should be noted for potential cross-walk discussion in the
        scaffolding workflow.

  cves_referenced: []   # No CVE — defensive product roadmap

  iocs: []              # No malicious IOCs — defensive product roadmap

  primary_claim: >
    GitHub announced (per SecurityWeek 2026-06-13 11:52 EDT) that
    NPM 12, expected July 2026, will change the default behavior
    of npm install so that preinstall, install, postinstall, and
    prepare scripts from dependencies will no longer execute
    unless explicitly allowed. Native node-gyp builds (packages
    with binding.gyp and no explicit install script) will also be
    affected by default. Git dependencies will not resolve unless
    allowed, and remote URL (HTTPS tarball) dependencies will
    require an explicit --allow-remote flag. Developers run npm
    approve-scripts to generate an allowlist written to
    package.json. This brings npm's default posture in line with
    pnpm's and bun's pre-existing security-aware approach.
    SecurityWeek references two named campaigns motivating the
    change: TeamPCP (Archimedes roster #001 HIGH) "exploited
    automatic script execution during npm install"; and Shai-Hulud
    (NOT on Archimedes roster; operator-deferred /new-actor
    candidate) is described as a "self-replicating worm that
    weaponized binding.gyp files." Both campaigns are described as
    having "infected thousands of developers with malware." This
    continues the supply-chain-of-developer-tooling cluster from
    the 2026-06-12 afternoon brief (AUR + Atomic Arch + NanoClaw
    + Tenet Agentjacking + Sygnia Velvet Ant) as the most
    aggressive ecosystem-level defensive response in the cluster.

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: true   # Shai-Hulud campaign reference is sole-sourced SecurityWeek paraphrase — analyst should validate against the wider public corpus before any actor-profiler /new-actor scaffolding to ensure Hard Rule 2 doctrine compliance
analyst_review_complete_flag: true   # Analyst review complete 2026-06-13T16:30:00-04:00; see analysis_sections below
analyst_review_outcome:
  publishable_as_graded: true
  wep_adjusted: false
  wep_adjustment_reason: >
    KAC + bounded ACH did not surface evidence supporting WEP
    downgrade. Grader's per-layer ceilings are well-calibrated.
    Brittleness on H1 (TeamPCP / Shai-Hulud relationship framing)
    is LOW because the position is corpus-baseline-anchored from
    FLASH-0001 rather than newly originated.
  red_team_review_still_required: false   # WEP ceiling remains "likely"; below very_likely threshold
  briefer_caveats_required:
    - >
      Do NOT lift the SecurityWeek "infected thousands of
      developers with malware" aggregate-scale claim as a
      load-bearing scale figure (KAC A2 qualify). If quoted,
      attribute verbatim to SecurityWeek as paraphrase, not
      as confirmed count.
    - >
      Do NOT collapse or distinguish TeamPCP and Shai-Hulud
      beyond what SecurityWeek says (KAC A3 qualify; ACH H1
      ranking-1). Specifically the brief MUST NOT say or
      imply "Shai-Hulud is a separate actor from TeamPCP"
      or "Shai-Hulud is TeamPCP's worm." Preserve verbatim
      parallel framing.
    - >
      Attribute the announcement as "per SecurityWeek's
      relay of GitHub's announcement," not "GitHub announced"
      (KAC A8 qualify). Direct GitHub blog retrieval pending
      next sweep.
  actor_profiler_action_blocked:
    blocked: true
    blocked_action: shai_hulud_new_actor_scaffolding
    block_reason: >
      KAC A5 test required. Operator must decide BEFORE any
      /new-actor invocation whether Shai-Hulud should be
      tracked as (a) actor roster entry [originates
      attribution MSTIC has declined to make — Hard Rule 2
      risk], (b) campaign-family sidecar under TeamPCP #001
      [consistent with FLASH-0001 corpus position but
      understates if non-TeamPCP actors also produce
      Shai-Hulud campaigns], or (c) family/cluster registry
      distinct from actor roster [methodologically cleanest;
      requires a new tracking category]. Analyst recommends
      option (c).
    not_blocked_action: teampcp_dossier_ttp_evolution_timeline_update
    not_blocked_rationale: >
      TeamPCP dossier update is restatement of existing TTP
      with NPM 12 as defensive-response milestone — not new
      attribution. Actor-profiler can proceed without
      operator decision on A5.
analyst_review_questions:
  - >
    Validate Shai-Hulud campaign-reference verbatim preservation
    per Hard Rule 2: does SecurityWeek's "self-replicating worm
    that weaponized binding.gyp files" framing align with the
    broader industry-reported designation of Shai-Hulud, or has
    SecurityWeek collapsed an industry term? Recommend operator
    /new-actor evaluation at operator cadence convenience.
  - >
    Cross-walk consideration: TeamPCP (roster #001) and Shai-Hulud
    both target the npm install-script execution path. Are they
    distinct actors with parallel TTPs, the same actor under
    different campaign names, or a TTP cluster shared across
    multiple unrelated actors? Hard Rule 2 binding — Archimedes
    does NOT originate the cross-walk; this is an open question
    for the actor-profiler scaffolding workflow.

red_team_review_required: false  # WEP ceiling on the announcement layer is "likely" — below the very_likely threshold that mandates red-team review; defensive-roadmap pattern is doctrinally clean
red_team_review_recommended_optional: false  # No load-bearing very_likely claim requires challenge

vuln_tracker_required: false    # No CVE

actor_profiler_required: true
actor_profiler_handoff_rationale: >
  Two distinct actor-profiler handoffs:
    1. TeamPCP (#001) dossier TTP-evolution timeline update — NPM
       12 default-block is the ecosystem-level defensive milestone
       in response to TeamPCP's documented automatic-script-
       execution TTP. Add to dossier.
    2. Shai-Hulud /new-actor scaffold candidate — operator-deferred.
       Second roster-gap candidate this week after Velvet Ant
       (finding-2026-06-12-0004). Operator should review and decide
       cadence for /new-actor invocation.

briefer_required: true
briefer_handoff_rationale: >
  Include in 2026-06-13 16:00 afternoon brief under the supply-
  chain-of-developer-tooling cluster narrative continuation. Lead
  with the structural defensive-response framing (most aggressive
  ecosystem-level posture in the cluster). Preserve TeamPCP
  (#001) and Shai-Hulud campaign references verbatim per Hard
  Rule 2. Note the npm approve-scripts allowlist mechanic and
  npm 11.16.0+ preparation upgrade path. Surface A&D structural
  relevance via developer-tooling and CI/CD/AI-agent-harness
  dependency-pull pathways. Hard Rule 6: ≤15 words per source per
  quote. Briefer should choose ONE of the two SecurityWeek quotes
  for each actor below — both quotes are within the 15-word cap
  but only ONE per source per finding is allowed.

# ============================================================================
# Source list (consolidated)
# ============================================================================
sources:
  - source_yaml_id: securityweek
    source_name: SecurityWeek (Ionut Arghire)
    source_url: https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
    published_at: 2026-06-13T11:52:58-04:00
    role: news_tier_first_publisher_of_github_npm_12_roadmap_announcement
    grade: B
  - source_yaml_id: github-blog-self-disclosure
    source_name: GitHub Blog (referenced via SecurityWeek; not directly retrieved this sweep)
    source_url: null
    published_at: 2026-06-13      # approximate per SecurityWeek attribution
    role: vendor_canonical_primary_on_own_product_roadmap_referenced
    grade: A
    provisional_grade_pending_ratification: true

# ============================================================================
# Quote audit (Hard Rule 6: ≤15 words per quote, ≤1 quote per source per finding)
# ============================================================================
quote_audit:
  - source: securityweek-2026-06-13
    quote: "exploited automatic script execution during npm install"
    word_count: 7
    within_15_word_cap: true
    purpose: teampcp_ttp_restatement_via_securityweek_paraphrasing_earlier_industry_reporting
  - source: securityweek-2026-06-13   # NOTE: Second SecurityWeek quote exceeds Hard Rule 6 cap (≤1 per source per finding)
    quote: "self-replicating worm that weaponized binding.gyp files"
    word_count: 7
    within_15_word_cap: true
    purpose: shai_hulud_campaign_reference_verbatim_preservation
    rule_6_violation: true
    rule_6_resolution: >
      Briefer MUST choose at most one of the two SecurityWeek
      quotes for the brief. Other can be paraphrased. Recommend
      the TeamPCP TTP quote as load-bearing for the brief because
      it anchors the roster #001 dossier-update framing; the
      Shai-Hulud quote can be paraphrased as "Shai-Hulud is
      reported as a self-replicating worm weaponizing the
      binding.gyp build descriptor."

# ============================================================================
# Analyst review (sat-kac + sat-ach output)
# ============================================================================
analyst_review_complete: true
analyst_review_run_id: analyst-20260613-163000
analyst_review_at: 2026-06-13T16:30:00-04:00
analyst_review_mode: grader_handoff
analyst_review_scope: >
  Grader flagged two questions: (1) verbatim preservation of the
  Shai-Hulud campaign reference per Hard Rule 2; (2) TeamPCP /
  Shai-Hulud cross-walk question (same operation or distinct?).
  Analyst applies sat-kac as primary instrument (cross-walk is an
  assumptions question, not a competing-attribution question) and
  a short bounded sat-ach to pressure-test the cross-walk
  hypotheses against the existing corpus baseline. The 2026-05-12
  FLASH-0001 finding's ACH already established the family-vs-
  actor distinction at MSTIC's family-attribution level; this
  analyst review extends that baseline into the new SecurityWeek
  reach-through.

analysis_sections:

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "GitHub's announced NPM 12 default-block of dependency-
        installed scripts is motivated by TeamPCP and Shai-Hulud
        npm supply-chain campaigns, per SecurityWeek 2026-06-13
        paraphrasing earlier industry reporting. TeamPCP is on
        Archimedes roster #001 HIGH; Shai-Hulud is NOT on roster
        and is an operator-deferred /new-actor scaffold candidate.
        Both are named verbatim per Hard Rule 2; no cross-walk
        is attempted."
      analyzed_at: 2026-06-13T16:30:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Grader handoff. The finding's load-bearing claims rest on
        a single SecurityWeek reach-through to a GitHub blog post
        that was not directly retrieved this sweep. The cross-walk
        question between TeamPCP and Shai-Hulud is an attractive
        analytic trap — both campaigns target the same TTP path
        (install-script execution), and the existing TeamPCP iocs
        sidecar already references the "Mini Shai-Hulud" family
        designation per MSTIC family-attribution. Analyst's job
        is to surface what assumptions a future briefer or
        actor-profiler would need to interrogate, not to originate
        the cross-walk.

      assumptions:
        - id: A1
          statement: >
            SecurityWeek's reference to "Shai-Hulud" denotes the
            same industry-reported campaign family that MSTIC,
            Wiz, and Snyk have used the name for in 2025-2026
            reporting (i.e., the npm supply-chain worm family
            with Russian-locale termination guardrails) — not
            a semantically drifted use of the name by SecurityWeek.
          confidence: high
          centrality: critical
          classification: sound
          rationale: >
            SecurityWeek is a B-grade established outlet with a
            track record of reusing industry-coined campaign
            designations without coining new ones. The article
            describes Shai-Hulud as "self-replicating worm that
            weaponized binding.gyp files" — both attributes
            (self-replicating + binding.gyp / native-build
            weaponization) are documented features of the
            Shai-Hulud family in the Archimedes corpus's prior
            FLASH-0001 finding (Mini Shai-Hulud, 2026-05-12).
            Semantic drift is unlikely. No qualifying caveat
            required.

        - id: A2
          statement: >
            The "infected thousands of developers with malware"
            aggregate-scale claim attributed to BOTH campaigns
            is a SecurityWeek paraphrase of earlier industry
            reporting, not a SecurityWeek-originated scale claim.
          confidence: medium
          centrality: material
          classification: qualify
          rationale: >
            SecurityWeek does not name the prior source for the
            aggregate scale. The figure is plausible (Mini
            Shai-Hulud's 2026-05-12 burst was 169-172 packages
            across multiple namespaces; downstream developer
            infections per package compound rapidly), but
            without source attribution the "thousands" wording
            is an aggregate qualitative claim, not a
            corroborated count. Briefer should NOT lift this
            aggregate-scale claim into the brief as load-bearing
            scale figure; if used, qualify as "SecurityWeek
            characterizes both campaigns as having infected
            'thousands of developers'" with the verbatim attribution.

        - id: A3
          statement: >
            TeamPCP and Shai-Hulud are referenced by SecurityWeek
            as TWO DISTINCT entities (one a named actor cluster,
            one a named campaign / worm family) rather than as
            two names for the same operation.
          confidence: medium
          centrality: critical
          classification: qualify
          rationale: >
            SecurityWeek's article syntax names them in
            parallel ("TeamPCP ... Shai-Hulud ..."), consistent
            with two-entity framing. BUT — the Archimedes
            corpus already documents (via finding-2026-05-12-
            FLASH-0001 SAT-ACH at E13, and via the TeamPCP
            iocs.yaml sidecar header lines 11-15) that the
            relationship is more layered than parallel: Mini
            Shai-Hulud is attributed by Wiz + StepSecurity to
            TeamPCP at the actor level, while MSTIC's
            Shai-Hulud designation is at the family/lineage
            level. The existing corpus position is "TeamPCP is
            ONE actor associated with the Shai-Hulud FAMILY;
            the family may have other actors too." SecurityWeek's
            parallel framing is consistent with this layered
            position but does not affirm it explicitly.
            Qualifying caveat REQUIRED for the brief: do NOT
            describe the two as either "the same campaign" or
            "two unrelated campaigns" — both framings would
            require Archimedes to originate beyond what
            SecurityWeek says.

        - id: A4
          statement: >
            The "Shai-Hulud" designation in SecurityWeek's
            article is consistent with the Archimedes corpus's
            existing use of the name (i.e., refers to the npm
            supply-chain worm family per MSTIC, NOT to some
            other thing called "Shai-Hulud" in adjacent OSINT).
          confidence: high
          centrality: material
          classification: sound
          rationale: >
            The technical descriptors (self-replicating worm,
            binding.gyp weaponization, npm ecosystem) all align
            with the corpus's existing Shai-Hulud family
            designation. No ambiguity surfaces; the name maps
            cleanly. No qualifying caveat required.

        - id: A5
          statement: >
            Treating Shai-Hulud as a /new-actor scaffold candidate
            (vs. as a campaign family under TeamPCP) is the
            correct downstream handoff. The grader's
            operator-deferred /new-actor flag presumes Shai-Hulud
            warrants its own roster entry rather than being
            folded into the TeamPCP dossier as a campaign-family
            sub-entry.
          confidence: unknown
          centrality: critical
          classification: test
          rationale: >
            This is the operationally consequential assumption
            and the one most worth interrogating before any
            roster action. The corpus baseline (FLASH-0001
            SAT-ACH E13 + iocs.yaml header) explicitly states
            that MSTIC's family-attribution is at the
            family/lineage level and does NOT name an actor.
            That means "Shai-Hulud" is the FAMILY/CAMPAIGN
            designation, and the ACTOR(S) attributable to it
            are a separate question. TeamPCP is one such actor
            per Wiz + StepSecurity. Other actors may or may
            not also produce Shai-Hulud-family campaigns.
            Treating Shai-Hulud as a /new-actor candidate (i.e.,
            roster entry as an actor) WOULD ORIGINATE an
            attribution claim — implying a coherent actor identity
            behind the name when MSTIC has explicitly declined
            to attribute the family to a named actor cluster.
            TEST REQUIRED — operator should decide BEFORE
            /new-actor invocation whether Shai-Hulud is to be
            tracked as (a) an actor entry [originates attribution
            beyond what sources say], (b) a campaign-family
            sidecar under TeamPCP #001 [consistent with corpus
            position but understates the case if non-TeamPCP
            actors also produce Shai-Hulud campaigns], or (c) a
            family/cluster registry distinct from the actor
            roster [methodologically cleanest, but requires a
            new tracking category Archimedes does not currently
            maintain]. Recommend option (c) but operator
            decision required.

        - id: A6
          statement: >
            SecurityWeek's verbatim phrasing on Shai-Hulud
            ("self-replicating worm that weaponized binding.gyp
            files") does not collapse a more nuanced industry
            term. SecurityWeek is restating the worm-class
            characterization in language that maps cleanly to
            corpus-documented Shai-Hulud capabilities.
          confidence: high
          centrality: material
          classification: sound
          rationale: >
            Self-replicating worm: documented for Mini Shai-Hulud
            in finding-2026-05-12-FLASH-0001 (worm-class
            self-propagation, E5/E6 evidence). Binding.gyp
            weaponization: consistent with native-build attack
            surface; node-gyp's binding.gyp is the exact file
            NPM 12's default-block is designed to neutralize.
            SecurityWeek's framing is faithful technical
            restatement. No qualifying caveat required.

        - id: A7
          statement: >
            GitHub's NPM 12 product roadmap is genuinely
            motivated by these two campaign references rather
            than retrospectively justified by them. The
            causal direction is: campaigns happened → GitHub
            responded.
          confidence: high
          centrality: material
          classification: sound
          rationale: >
            Standard vendor-roadmap pattern. Defensive product
            changes at ecosystem-package-manager level (npm,
            pnpm, bun) are routinely motivated by named recent
            attack patterns. Causal direction is established
            by the timing (campaigns visible in 2026-Q1/Q2;
            NPM 12 announced 2026-06-13, release July 2026)
            and by SecurityWeek's framing of the campaigns as
            the explicit motivation. No qualifying caveat
            required.

        - id: A8
          statement: >
            GitHub's announcement was actually made by GitHub
            (i.e., SecurityWeek's reach-through to a GitHub
            blog post is faithful, not a SecurityWeek
            invention or paraphrase of a non-blog channel).
          confidence: medium
          centrality: material
          classification: qualify
          rationale: >
            SecurityWeek attributes "the source of these
            announcements" to GitHub but the URL was not
            captured this sweep. Vendor reach-through is the
            standard pattern; SecurityWeek has not been
            observed inventing vendor announcements. BUT
            direct GitHub blog retrieval is pending; this is
            the same gap the grader flagged. Briefer should
            note "expected July 2026 per SecurityWeek's relay
            of GitHub's announcement" — preserves attribution
            chain. Next sweep should attempt direct GitHub
            blog retrieval; if it fails to find the announcement,
            the assessment downgrades sharply.

        - id: A9
          statement: >
            The cross-walk question itself ("TeamPCP and
            Shai-Hulud — same or distinct?") is an analyst-level
            question, not a briefer-level question. The brief
            should NOT take a position on the cross-walk;
            the briefer should report what SecurityWeek says
            and leave the rest to the actor-profiler / operator
            decision queue.
          confidence: high
          centrality: critical
          classification: sound
          rationale: >
            Hard Rule 2 binding. Brief reports sourced claims;
            does not originate analytic positions on actor
            identity. SecurityWeek names both verbatim and
            does not collapse them; brief mirrors that posture.
            No qualifying caveat required — this is the
            analyst's positive recommendation to the briefer.

      classifications_summary:
        sound: 5      # A1, A4, A6, A7, A9
        qualify: 3    # A2, A3, A8
        test: 1       # A5
        unsupported: 0

      remediation:
        status: proceed
        qualifying_caveats:
          - >
            A2 (aggregate-scale claim "thousands of developers"):
            briefer should NOT lift this as a load-bearing scale
            figure; if quoted, attribute verbatim to SecurityWeek
            as a paraphrase rather than as a confirmed count.
          - >
            A3 (TeamPCP / Shai-Hulud parallel framing): brief
            must report the two as SecurityWeek does — in
            parallel, without "same" or "different" claim.
            Specifically, the brief MUST NOT say or imply
            "Shai-Hulud is a separate actor from TeamPCP" or
            "Shai-Hulud is TeamPCP's worm." The corpus position
            is: Mini Shai-Hulud (a campaign family member) was
            attributed by Wiz + StepSecurity to TeamPCP at
            actor level; MSTIC's family-level attribution
            does NOT name an actor for the broader Shai-Hulud
            family. Brief should preserve verbatim and stop.
          - >
            A8 (GitHub blog reach-through): brief should
            phrase as "per SecurityWeek's relay of GitHub's
            announcement" and flag the direct retrieval as
            outstanding for the next sweep. Do NOT cite
            "GitHub announced" as if directly observed.
        test_requirements:
          - assumption_id: A5
            test_description: >
              Operator must decide BEFORE any /new-actor
              invocation whether Shai-Hulud should be tracked
              as (a) actor roster entry [originates attribution
              MSTIC has declined to make], (b) campaign-family
              sidecar under TeamPCP #001 [consistent with
              FLASH-0001 corpus position but understates if
              non-TeamPCP actors also produce Shai-Hulud
              campaigns], or (c) family/cluster registry
              distinct from actor roster [methodologically
              cleanest; requires a new tracking category].
              Analyst recommendation: option (c). Operator
              decision required before actor-profiler
              proceeds with /new-actor.
            blocks_what: shai_hulud_new_actor_scaffolding
            does_not_block: >
              Does NOT block this finding's publication in
              the 2026-06-13 afternoon brief. Brief can ship
              with verbatim Hard Rule 2 preservation and
              defer the roster-action decision to the
              operator queue.

      recommended_wep_after_test:
        vendor_product_roadmap_layer: likely       # unchanged from grader
        teampcp_ttp_restatement_layer: very_likely # unchanged
        shai_hulud_campaign_reference_layer: likely  # unchanged
        cluster_continuity_layer: very_likely      # unchanged
        ad_structural_relevance_layer: likely      # unchanged
      wep_adjustment_summary: >
        KAC does NOT change the grader's WEP ceilings. The
        grader's per-layer ceilings are well-calibrated to
        the source posture. KAC flags ONE test requirement
        (A5: Shai-Hulud roster treatment) and THREE qualifying
        caveats (A2: aggregate-scale paraphrase; A3: parallel
        framing preservation; A8: GitHub reach-through
        attribution). None of these reach the bar for WEP
        downgrade; all are briefer-discipline items.

  sat_ach:
    ach_analysis:
      question: >
        Is Shai-Hulud a distinct campaign from TeamPCP's known
        NPM activity, or is it the same operation under a
        different name?
      analyzed_at: 2026-06-13T16:30:00-04:00
      analyzed_by: analyst
      red_team_review: null
      scope_note: >
        Short bounded ACH. The evidence base is the current
        SecurityWeek reach-through PLUS the existing Archimedes
        corpus position (finding-2026-05-12-FLASH-0001 SAT-ACH
        + TeamPCP iocs.yaml sidecar). ACH is bounded because
        the question is not "who did it" (no novel attribution
        attempted) but "what is the relationship between two
        named-by-sources entities." All four hypotheses below
        EXIST in cited sources or in corpus-already-established
        positions; none would originate attribution.

      hypotheses:
        - id: H1
          statement: >
            TeamPCP and Shai-Hulud are distinct entities at
            different abstraction levels: TeamPCP is an ACTOR
            cluster (Archimedes roster #001), Shai-Hulud is a
            CAMPAIGN FAMILY designation (per MSTIC family-
            attribution). The relationship is "TeamPCP is one
            actor that produces Shai-Hulud-family campaigns;
            other actors may also produce campaigns in this
            family." This is the corpus-established position
            from FLASH-0001 SAT-ACH E13 + iocs.yaml header.
          hypothesis_type: sourced_obvious_corpus_baseline
        - id: H2
          statement: >
            TeamPCP and Shai-Hulud are the same operation under
            different names (one actor cluster, one
            self-designation or external moniker). Cited only
            by inference; no source asserts this.
          hypothesis_type: collapse_alt
        - id: H3
          statement: >
            TeamPCP and Shai-Hulud are two DISTINCT actors with
            parallel TTPs in the same TTP cluster
            (install-script execution), neither one a family
            of the other. SecurityWeek's parallel framing is
            consistent with this reading; the FLASH-0001
            corpus position (TeamPCP attributed to Mini
            Shai-Hulud) would be a partial confound.
          hypothesis_type: parallel_distinct_actors
        - id: H4
          statement: >
            Null / abstain — "Shai-Hulud" is an analytic label
            for clustered activity without coherent actor
            identity behind it; the cross-walk question is
            malformed because Shai-Hulud is not at the same
            ontological level as TeamPCP. (This is the
            corpus-baseline H1 plus an additional skepticism
            layer about whether the family designation itself
            carries actor-level meaning.)
          hypothesis_type: null_abstain
      hypothesis_generation_discipline_check: >
        Four hypotheses generated. H1 = corpus-baseline
        sourced position. H2/H3 = the two operationally
        plausible "collapse" and "parallel" readings the
        grader's open question implicitly raises. H4 = null/
        abstain skepticism layer. NO hypothesis originates a
        novel actor attribution; all four are about the
        RELATIONSHIP between two designations that other
        sources have already made. Hard Rule 2 boundary
        respected.

      evidence:
        - id: E1
          description: >
            SecurityWeek names TeamPCP and Shai-Hulud in
            parallel as two distinct motivating campaigns,
            without collapsing them or asserting they are
            related.
          source: securityweek-2026-06-13
          digraph: B2
          weight: 2
        - id: E2
          description: >
            Existing Archimedes corpus (finding-2026-05-12-
            FLASH-0001 SAT-ACH E13): MSTIC's Shai-Hulud
            family designation is at the FAMILY/LINEAGE
            level, NOT actor level. MSTIC has not attributed
            the Shai-Hulud family to a named actor cluster.
          source: archimedes_corpus_state_finding_0001_e13
          digraph: A1_for_corpus_state
          weight: 3
        - id: E3
          description: >
            Existing Archimedes corpus (finding-2026-05-12-
            FLASH-0001): Wiz Research + StepSecurity
            attributed Mini Shai-Hulud (a member of the
            Shai-Hulud family per MSTIC) to TeamPCP at actor
            level. This is the only known actor-level
            attribution for ANY Shai-Hulud family campaign
            in the corpus.
          source: archimedes_corpus_state_finding_0001_attribution
          digraph: A2_for_attribution_layer
          weight: 3
        - id: E4
          description: >
            TeamPCP iocs.yaml sidecar header explicitly
            characterizes Mini Shai-Hulud as a "member of the
            Shai-Hulud family per MSTIC family attribution
            (MSTIC has not publicly named an actor for the
            family)." This is the analyst-codified corpus
            position on the relationship.
          source: teampcp_iocs_yaml_header_lines_11_18
          digraph: A1_for_corpus_state
          weight: 3
        - id: E5
          description: >
            Shai-Hulud as a designation pre-dates TeamPCP's
            Archimedes roster entry (tracked_since 2026-03-18).
            MSTIC's Shai-Hulud 2.0 guidance was published
            December 2025 per FLASH-0001 evidence. The name
            therefore existed in industry use BEFORE TeamPCP
            was a tracked roster entity.
          source: archimedes_corpus_state_finding_0001
          digraph: A2_for_temporal_state
          weight: 2
        - id: E6
          description: >
            SecurityWeek does not cite which actor the
            Shai-Hulud campaign is attributed to. The article
            names the campaign but not an associated actor
            cluster, consistent with MSTIC's family-level-only
            attribution posture.
          source: securityweek-2026-06-13_negative_observation
          digraph: B2
          weight: 2
        - id: E7
          description: >
            TeamPCP and Shai-Hulud share TTP class
            (install-script execution path; native-build
            weaponization via binding.gyp). TTP-class overlap
            is non-diagnostic because the TTP is publicly
            documented and broadly replicable.
          source: securityweek_2026_06_13_ttp_descriptions_plus_corpus
          digraph: B3
          weight: 1

      matrix:
        E1: {H1: C, H2: I, H3: C, H4: C}    # Parallel framing supports distinct entities; inconsistent with collapse
        E2: {H1: C, H2: I, H3: N, H4: C}    # MSTIC family-not-actor posture supports H1's layered framing; inconsistent with H2 collapse
        E3: {H1: C, H2: C, H3: I, H4: N}    # TeamPCP attribution for Mini Shai-Hulud supports actor-within-family (H1) or collapse (H2); inconsistent with parallel-distinct (H3)
        E4: {H1: C, H2: I, H3: I, H4: C}    # Corpus-codified family-vs-actor distinction directly supports H1; inconsistent with both collapse and parallel-distinct
        E5: {H1: C, H2: I, H3: C, H4: C}    # Shai-Hulud predates TeamPCP roster entry; family designation has independent age, inconsistent with H2 collapse
        E6: {H1: C, H2: N, H3: N, H4: C}    # SecurityWeek's silence on actor for Shai-Hulud consistent with family-not-actor framing
        E7: {H1: C, H2: C, H3: C, H4: C}    # TTP overlap non-diagnostic

      inconsistency_counts:
        H1: 0      # corpus-baseline position survives all evidence
        H2: 4      # E1, E2, E4, E5 contradict the collapse hypothesis
        H3: 2      # E3, E4 contradict parallel-distinct-actors framing
        H4: 0      # abstain survives but doesn't compete with H1 on positive content

      diagnostic_evidence:
        - E2: >
            Diagnostic: MSTIC's family-level-only attribution
            posture is the single most diagnostic piece of
            evidence in the matrix. It directly contradicts
            H2 (collapse to one entity) and is neutral on H3
            (parallel actors). It positively supports H1's
            layered framing.
        - E3: >
            Diagnostic in TWO directions: TeamPCP attribution
            for Mini Shai-Hulud is consistent with H1 (TeamPCP
            is one actor in the family) AND with H2 (collapse
            — Mini Shai-Hulud IS TeamPCP); inconsistent with
            H3 (parallel distinct actors with no overlap).
            E3 alone cannot adjudicate H1 vs H2; E2 + E4 + E5
            together push toward H1.
        - E4: >
            Diagnostic: The analyst-codified corpus position
            (iocs.yaml header) is the established Archimedes
            framing. Treating H1 as ranking-1 is consistent
            with the existing corpus state and does NOT
            originate new attribution.
        - E5: >
            Diagnostic: Temporal precedence of the Shai-Hulud
            designation over TeamPCP's tracked-since date
            argues against H2 (collapse). If they were the
            same operation, naming would track together;
            the family designation having an independent
            history argues for layered framing.

      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: >
            H1 has 0 inconsistencies, is the corpus-baseline
            position established in FLASH-0001 SAT-ACH E13
            and codified in the TeamPCP iocs.yaml header,
            and is consistent with all available evidence.
            H1 is the only hypothesis that simultaneously
            explains (a) MSTIC's family-only attribution
            posture, (b) Wiz/StepSecurity's actor-level
            attribution of Mini Shai-Hulud to TeamPCP, (c)
            SecurityWeek's parallel framing of TeamPCP and
            Shai-Hulud as distinct, and (d) the temporal
            precedence of the Shai-Hulud designation.
          wep: likely
          confidence_caveat: >
            H1 is the ranking-1 hypothesis but is reported AS
            THE CORPUS-BASELINE POSITION, not as a novel
            analyst conclusion. Per Hard Rule 2, H1 does not
            ORIGINATE the framing — it RESTATES the framing
            that MSTIC (via family attribution) and the
            Archimedes corpus (via FLASH-0001) already
            established.
        - rank: 2
          hypothesis_id: H4
          rationale: >
            H4 (null / abstain) has 0 inconsistencies but no
            positive content. H4 is the analytic-skepticism
            layer asking "is Shai-Hulud even at the same
            ontological level as TeamPCP?" Useful as a
            tripwire — if a future source treats Shai-Hulud
            as an actor with coherent identity, H4 falsifies.
          wep: roughly_even_chance_as_skepticism_layer
          confidence_caveat: >
            Useful for analyst discipline; not promotable to
            ranking-1 because H1 has positive evidentiary
            support.
        - rank: 3
          hypothesis_id: H3
          rationale: >
            H3 (parallel distinct actors) has 2 inconsistencies
            (E3, E4 — the corpus has Wiz/StepSecurity actor-
            level attribution of Mini Shai-Hulud to TeamPCP,
            which means at minimum the activities overlap at
            the actor level; not parallel-with-no-overlap).
            H3 is ruled out by the existing corpus state.
          wep: unlikely
          confidence_caveat: >
            H3 would require SecurityWeek's parallel framing
            to be evidence of two ACTOR-level entities, but
            the FLASH-0001 corpus state has Wiz + StepSecurity
            attributing Mini Shai-Hulud to TeamPCP. That
            attribution cannot be reconciled with H3.
        - rank: 4
          hypothesis_id: H2
          rationale: >
            H2 (collapse — same operation, two names) has 4
            inconsistencies — E1 (parallel naming), E2 (MSTIC
            family-not-actor posture, which would not make
            sense if family = actor), E4 (analyst-codified
            distinction), E5 (temporal precedence of family
            designation). H2 also would require Archimedes to
            originate the collapse, violating Hard Rule 2.
          wep: unlikely
          confidence_caveat: >
            H2 is the operationally tempting "Shai-Hulud IS
            TeamPCP's worm" framing that a briefer might
            reach for. ACH explicitly rejects it; brief MUST
            NOT collapse them.

      sensitivity_analysis:
        brittleness: LOW
        load_bearing_evidence: [E2, E4]
        load_bearing_evidence_rationale: >
          The H1-favoring ranking rests primarily on the
          existing Archimedes corpus state (MSTIC family-only
          posture per FLASH-0001 E13 + iocs.yaml header
          codification). If FLASH-0001's framing of MSTIC's
          attribution posture is later revised (e.g., MSTIC
          publishes a follow-up explicitly naming an actor
          cluster behind the Shai-Hulud family), H1 vs H2
          adjudication becomes evidence-driven rather than
          corpus-baseline-driven. Until then, H1 holds with
          low brittleness.
        if_MSTIC_attributes_family_to_actor: >
          If MSTIC publishes actor-level attribution for
          Shai-Hulud family in subsequent reporting and that
          actor IS TeamPCP, H1 strengthens (TeamPCP is THE
          actor for the family, not one of N). If the named
          actor is NOT TeamPCP, H1 still holds (TeamPCP and
          the new actor are both Shai-Hulud-family
          producers) but the FLASH-0001 attribution becomes
          ambiguous.
        if_securityweek_collapses_in_followup: >
          If SecurityWeek or another B-grade outlet publishes
          a follow-up explicitly equating TeamPCP and Shai-
          Hulud, H2 (collapse) rises. Unlikely given current
          posture but worth tracking.

      tripwires:
        - observation: >
            MSTIC, Wiz, or another A-grade source explicitly
            names an actor cluster for the Shai-Hulud family
            broadly (not just Mini Shai-Hulud).
          effect: >
            H1 vs H2 adjudication becomes evidence-driven.
            If named actor IS TeamPCP, H1 strengthens with
            collapse-favoring qualification. If named actor
            is not TeamPCP, H1 holds with explicit
            "multiple actors in family" status.
        - observation: >
            A future A-grade source treats TeamPCP and
            Shai-Hulud as a single entity (collapse).
          effect: >
            H2 rises; ACH rerun with explicit attribution
            chain.
        - observation: >
            A future A-grade source documents non-TeamPCP
            actor producing Shai-Hulud-family campaigns.
          effect: >
            H1 strengthens, with explicit "Shai-Hulud is a
            family with multiple producer actors" framing.
            Argues against H3 collapse to a single parallel-
            actor framing.
        - observation: >
            Operator decides on Shai-Hulud roster treatment
            (assumption A5 test).
          effect: >
            Drives downstream actor-profiler workflow;
            does NOT change ACH outcome but determines
            tracking-system implementation.

      conclusion:
        summary: >
          H1 (TeamPCP and Shai-Hulud are at different
          abstraction levels — actor vs campaign family) is
          ranking-1 with 0 inconsistencies. This is the
          corpus-established position from FLASH-0001 SAT-ACH
          E13 and the TeamPCP iocs.yaml header; ACH does NOT
          originate this framing, it restates it under
          pressure-testing. H2 (collapse to one entity) is
          rejected with 4 inconsistencies. H3 (parallel
          distinct actors) is rejected with 2 inconsistencies.
          H4 (abstain) survives as a skepticism layer.
          Briefer MUST preserve SecurityWeek's parallel
          framing without claiming "same" or "different" at
          the actor level. Actor-profiler MUST resolve
          assumption A5 (KAC) before /new-actor scaffolding.
        wep: likely  # on the H1 framing; corpus-baseline anchored
        confidence_caveats: >
          (1) ACH outcome is corpus-baseline-anchored;
          sensitivity is LOW because the H1 framing is
          already established and the new SecurityWeek
          evidence is consistent with it. (2) H1 is restated,
          not originated — Hard Rule 2 is respected. (3)
          Brittleness rises if MSTIC publishes follow-up
          family-to-actor attribution; tripwire active. (4)
          The KAC test requirement (A5 — Shai-Hulud roster
          treatment) is the operationally consequential
          downstream action; ACH outcome supports but does
          not determine that decision.

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs: [2026-06-13-afternoon]
retracted: false
retraction_brief_id: null
---

# NPM 12 default script-execution change — supply-chain defensive roadmap (continues supply-chain-of-developer-tooling cluster)

## Summary

GitHub announced via SecurityWeek on 2026-06-13 11:52 EDT that NPM 12, expected July 2026, will change the default behavior of `npm install` so that `preinstall`, `install`, `postinstall`, and `prepare` scripts from dependencies will no longer execute unless explicitly allowed. Native `node-gyp` builds with a `binding.gyp` file but no explicit install script will also be affected by default. Git dependencies and HTTPS-tarball remote URL dependencies will require explicit allowlist or `--allow-remote` flagging. Developers will generate an allowlist via `npm approve-scripts`, with `npm 11.16.0+` available now as a preparation upgrade path. SecurityWeek explicitly names TeamPCP (Archimedes roster #001 HIGH) and Shai-Hulud (NOT on roster; operator-deferred /new-actor candidate) as motivating campaigns. This is the most aggressive ecosystem-level defensive response yet in the supply-chain-of-developer-tooling cluster carried into the 2026-06-12 afternoon brief.

## Sources

### SecurityWeek (securityweek, digraph: B) — news-tier first publisher of vendor roadmap

- URL: https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
- Published: 2026-06-13T11:52:58-04:00
- Byline: Ionut Arghire
- Key claim: NPM 12 (July 2026) default-blocks preinstall/install/postinstall/prepare scripts and gates git/remote-URL dependency resolution; opt-in via `npm approve-scripts` allowlist; motivated by TeamPCP and Shai-Hulud supply-chain campaigns.

### GitHub Blog (github-blog-self-disclosure, digraph: A provisional) — vendor primary referenced

- URL: not surfaced this sweep
- Published: 2026-06-13 (approximate per SecurityWeek attribution)
- Key claim: Vendor canonical on own product roadmap. SecurityWeek attributes "the source of these announcements" to GitHub. Reach-through pending direct GitHub blog retrieval next sweep.

## Technical detail

NPM 12's default-block applies to dependency-installed scripts only — not to package.json `scripts` block entries that the developer authors and invokes directly. The opt-in allowlist via `npm approve-scripts` writes trusted package permissions into `package.json`; subsequent installs honor that allowlist. The `--allow-remote` flag is required at install time for remote URL (HTTPS tarball) dependencies. Git dependencies require explicit allowlisting. The `prepare` script gating extends to git/file/link dependencies, which historically resolved and executed `prepare` automatically.

This is functionally equivalent to the security-aware default already taken by `pnpm` and `bun`, brought to npm as default. NPM 11.16.0 or later provides a forward-compatible preparation surface; developers can upgrade now to test their `package.json` against the new posture.

## IOCs surfaced

None. This is a defensive product roadmap, not a vulnerability remediation or attack disclosure. No CVE, no infrastructure, no hashes.

## Threat-actor / campaign references (Hard Rule 2 binding)

Two campaigns are explicitly named by SecurityWeek as motivating the NPM 12 change. Archimedes preserves both verbatim per Hard Rule 2 — SecurityWeek paraphrases earlier industry reporting; Archimedes does NOT originate either designation.

- **TeamPCP** (Archimedes roster #001 HIGH, tracked_since 2026-03-18) — described by SecurityWeek as having "exploited automatic script execution during npm install." This restates a TTP already in the TeamPCP dossier; not a new attribution claim. Material for the dossier's TTP-evolution timeline as the ecosystem-level defensive response milestone.
- **Shai-Hulud** (NOT on Archimedes roster; operator-deferred /new-actor scaffold candidate, second this week after Velvet Ant from 2026-06-12 afternoon brief) — described by SecurityWeek as a "self-replicating worm that weaponized binding.gyp files." Both campaigns are described as having "infected thousands of developers with malware" (aggregate-scale qualitative claim, single-source SecurityWeek paraphrase).

No cross-walk between TeamPCP and Shai-Hulud is attempted by SecurityWeek or by Archimedes. Hard Rule 2 binding.

## A&D / DIB relevance

No direct A&D relevance — NPM is the JavaScript package ecosystem, not aerospace-defense. Structural relevance is real but indirect: A&D primes consume NPM via internal web app development, build pipelines, CI/CD, infrastructure-as-code (e.g., AWS CDK, Pulumi), and AI agent harnesses (LangChain, LangGraph, Claude Code, Cursor — all of which pull NPM dependencies). Developer-endpoint infection via install scripts is an initial-access vector to corporate environments with lateral-movement potential. The NPM 12 default-block reduces the install-script attack surface for any A&D-prime developer pulling third-party JavaScript dependencies.

No A&D-prime victim has been publicly confirmed in either the TeamPCP or Shai-Hulud reporting referenced by SecurityWeek. Structural-inference WEP "likely" for indirect A&D-developer-endpoint exposure pending NPM 12 deployment cycles.

## Cross-cluster context

This finding continues the supply-chain-of-developer-tooling cluster from the 2026-06-12 afternoon brief:

- **AUR 400+ packages hijacked with Atomic Arch Rust credential stealer + eBPF rootkit** (Sonatype, finding-2026-06-12-pm-XX) — first Arch ecosystem mass compromise in the Archimedes corpus.
- **NanoClaw / JFrog AI agent supply-chain** (reject-2026-06-12-0001) — rejected as vendor marketing.
- **Tenet Security Agentjacking research** (finding-2026-06-12-pm-XX) — 85% success rate against Claude Code + Cursor via Sentry DSN abuse.
- **Sygnia Velvet Ant Operation Highland** (finding-2026-06-12-0004) — China-nexus PAM + OpenSSH backdoor on air-gapped East Asia victim; operator-deferred /new-actor candidate.

NPM 12's default-block is the most aggressive ecosystem-level defensive response in this cluster. The other items are either offensive compromise events or research disclosures; NPM 12 is structural infrastructure change at the package manager level.

## Relationship to existing findings

First Archimedes-corpus finding on NPM 12 specifically. Cluster continuation of supply-chain-of-developer-tooling narrative from 2026-06-12 PM brief. TeamPCP (roster #001) dossier should be updated with NPM 12 as a defensive-response TTP-evolution milestone. Shai-Hulud is a new roster-gap candidate for operator-deferred /new-actor scaffolding.

## Open questions for analyst / actor-profiler / red-team

- Analyst should validate Shai-Hulud campaign-reference verbatim preservation per Hard Rule 2: does SecurityWeek's framing align with broader industry-reported designation, or has SecurityWeek collapsed an industry term?
- Cross-walk question (open, not for Archimedes to originate): TeamPCP and Shai-Hulud both target the npm install-script execution path — distinct actors with parallel TTPs, same actor under different campaign names, or shared TTP cluster across unrelated actors? Hard Rule 2 binding.
- Actor-profiler: TeamPCP dossier TTP-evolution timeline update (NPM 12 as defensive-response milestone) + Shai-Hulud /new-actor scaffold operator-deferred decision.
- Briefer must choose ONE SecurityWeek quote per Hard Rule 6 (recommend TeamPCP TTP quote as load-bearing).

## Analytic notes (from analyst review)

KAC interrogated nine assumptions; ACH bounded the cross-walk question. The finding is publishable as-graded with three briefer caveats and one downstream block.

The cross-walk question that worried the grader resolves cleanly when the corpus baseline is brought to bear. Finding-2026-05-12-FLASH-0001's SAT-ACH (evidence E13) and the TeamPCP iocs.yaml sidecar header already establish that MSTIC attributes Shai-Hulud at the family/lineage level and has not named an actor for the broader family; Wiz and StepSecurity separately attributed Mini Shai-Hulud (one family member) to TeamPCP at actor level. SecurityWeek's parallel framing in this finding is consistent with that layered position — TeamPCP is an actor, Shai-Hulud is a campaign family — and ACH ranks that framing first with zero inconsistencies. Collapsing the two ("Shai-Hulud is TeamPCP's worm") gets four inconsistencies and would originate framing beyond what sources say. Brief must preserve parallel framing without claiming "same" or "different" at actor level.

The operationally consequential item is KAC assumption A5: should Shai-Hulud become a roster actor entry, a campaign-family sidecar under TeamPCP, or a new family/cluster tracking category? Treating it as an actor entry would originate attribution that MSTIC has explicitly declined to make. Analyst recommends the third option (family registry distinct from roster), but this requires an operator decision before any /new-actor scaffolding. The TeamPCP dossier TTP-evolution timeline update (NPM 12 as defensive-response milestone) is NOT blocked — that path is pure restatement.
