---
finding_id: finding-2026-06-02-0003-securityweek-reversinglabs-aikido-ox-socket-miasma-red-hat-npm-32-package-vt006-extension-multi-firm-corroboration-oidc-cicd-vector
created_at: 2026-06-02T08:22:00-04:00
graded_by: grader
grading_run_id: morning-20260602-080000
grading_mode: scheduled_brief
test: false
relates_to: finding-2026-06-01-0004-socket-thn-miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain-vt006-family-expansion-anthropic-impersonation-c2
relation_type: campaign_progression_with_multi_firm_corroboration   # NOT supersession; analyst/red-team decide whether to formally supersede 0004

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  red_hat_npm_redhat_cloud_services_scope_32_packages_compromised: B1                # SecurityWeek consolidating four vendor primaries; cross-corroborates finding 0004's Socket+THN origination
  96_malicious_versions_published_before_red_hat_unpublished: B1                     # SecurityWeek; consistent with finding 0004
  ~10_million_collective_downloads_across_compromised_scope: B2                       # SecurityWeek-stated aggregate; not vendor-by-vendor verified
  miasma_the_spreading_blight_payload_string_researcher_coined_variant_name: A1      # Payload-embedded string is verifiable artifact; multi-firm consensus on the variant name
  variant_lineage_mini_shai_hulud_family_vt_006: A1                                  # Internal corpus state verifiable against VT-006 + finding 0004; mechanism-family signature consistent
  72_second_publication_window_across_96_malicious_versions: B2                       # ReversingLabs analysis; single-firm origination on this specific TTP observation; SecurityWeek aggregation does not substitute for independent corroboration
  github_actions_oidc_token_issuance_as_cicd_compromise_vector: B2                    # Aikido assessment; single-firm origination on this specific TTP observation
  210_downstream_infected_repositories_with_stolen_credentials: B2                    # Ox Security enumeration; single-firm origination
  socket_runtime_capability_analysis_credential_stealing_worm_class: B2               # Socket runtime/binary analysis; carry-forward consistent with finding 0004
  teampcp_attributed_via_consolidated_four_vendor_reporting_per_securityweek_aggregation: B2   # Restatement aggregation through SecurityWeek; not Archimedes-originated; carry-forward of finding 0004's "likely" WEP on TeamPCP attribution
  multi_firm_independent_consolidation_strengthens_procedural_facts_layer_to_b1: B1   # The four-vendor independence test on procedural facts (compromise occurred, scope, mechanism class) PASSES — different evidence bases (Socket runtime, ReversingLabs CI/CD compromise, Aikido OIDC, Ox Security downstream-repos enumeration)
  no_ad_prime_named_as_downstream_victim: A1                                          # Verifiable absence; transitive-dependency exposure is grader-inferred not source-named
  cve_2026_45321_family_kev_listed_with_2026_06_10_federal_deadline: A1               # Verifiable CISA KEV catalog state; carry-forward
  red_hat_no_independent_incident_response_statement_at_sweep_time: A1                # Verifiable absence; Red Hat detected and unpublished per SecurityWeek but no independent IR disclosure
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored on SecurityWeek (Ionut Arghire byline, 2026-06-02
  05:51 EDT, in window) consolidating four independent vendor research
  surfaces (ReversingLabs C / Aikido C / Ox Security B / Socket B) on
  the Red Hat @redhat-cloud-services npm 32-package / 96-malicious-
  version supply-chain compromise, identified as a Mini Shai-Hulud
  (VT-006 family) variant carrying the "Miasma: The Spreading Blight"
  payload-embedded string. The four-firm independent corroboration
  layer is the substantively-new addition vs. finding 0004's Socket +
  THN origination.

  B2 (not A2 or B1) anchored because:
    - Source-reliability LETTER grade on the strongest corroborating
      primary is B (Socket and Ox Security at provisional B). Aikido
      and ReversingLabs are C/provisional-C. SecurityWeek is a
      B-grade RELAY consolidating these four primaries; the relay
      itself does not elevate to A.
    - The procedural-facts layer (compromise occurred, scope of 32
      packages / 96 versions, mechanism-class as Mini Shai-Hulud
      variant) cleanly carries B1 because the four vendors are
      independent (different publishing organizations, neither cites
      the others as origin, different evidence bases — Socket runtime
      analysis, ReversingLabs CI/CD compromise + publication-window
      forensics, Aikido OIDC exploitation assessment, Ox Security
      downstream-repo enumeration). Independence test PASSES on
      procedural facts.
    - The specific TTP layers (72-second publication window —
      ReversingLabs only; GitHub Actions OIDC vector — Aikido only;
      210 downstream repos — Ox Security only) each carry single-firm
      origination at B-or-C. SecurityWeek consolidation does not
      substitute for independent corroboration of each specific TTP
      observation. Layered grading: B2 on each.
    - The TeamPCP attribution layer is RESTATEMENT not origination
      per Hard Rule 2. Finding 0004 grades this layer at "likely"
      WEP because Socket originally EXPLICITLY DECLINED attribution
      ("Attribution remains unclear"). SecurityWeek's 2026-06-02
      aggregation says "TeamPCP is identified as the threat group
      behind this campaign" sourced via the four vendors, but the
      directly-retrieved Socket primary (finding 0004) shows Socket
      did NOT originate this attribution. SecurityWeek's "identified"
      framing is reporter-aggregated and does not independently verify
      each vendor's verbatim attribution stance. The attribution layer
      carries B2 (Probably True, single-cluster-source) not B1
      (Confirmed).

  Single-source veto applied on specific TTP layers and attribution:
    - 72-second window (ReversingLabs only) — capped at "likely"
    - GitHub Actions OIDC vector (Aikido only) — capped at "likely"
    - 210 downstream repos (Ox Security only) — capped at "likely"
    - TeamPCP attribution (SecurityWeek aggregation through four
      vendors but not independently directly retrieved) — capped at
      "likely"
  Procedural facts (compromise occurred, scope, mechanism class)
  NOT subject to veto due to four-vendor independence on procedural
  layer.

  Relationship to finding-2026-06-01-0004:
    - This finding is a CAMPAIGN-PROGRESSION extension, NOT a
      supersession. Finding 0004 carries the originating Socket + THN
      coverage with the Anthropic-API-impersonation C2 detail
      (api.anthropic[.]com impersonation; AES-128/256-GCM + RSA-OAEP
      encryption; SHA-256 published tarball hashes; "ifyouinvalidate
      thistoken" internal payload string) — those details are NOT
      in this 2026-06-02 SecurityWeek surface and remain finding
      0004's unique contribution.
    - This 2026-06-02 finding adds: Miasma variant name, 72s window,
      OIDC vector, 210 downstream repos, multi-firm corroboration
      layer.
    - The analyst / red-team / vuln-tracker decide whether to formally
      supersede 0004 with a consolidated finding or carry both with
      explicit cross-reference. Grader recommendation: KEEP BOTH
      with cross-reference; both surfaces contribute unique material.

  Per Hard Rule 2: TeamPCP attribution is RESTATEMENT not origination.
  Archimedes does NOT originate TeamPCP attribution on the Red Hat
  npm Miasma campaign; the attribution layer is preserved as
  "TeamPCP-attributed-by-SecurityWeek-aggregation-of-four-vendor-
  research" rather than as "Archimedes-attributes."

  Per Hard Rule 3: NO exploit code, NO PoC, NO GitHub-Actions-OIDC
  walkthrough preserved. Mechanism class described at analytic level
  only.

  Per Hard Rule 6: zero verbatim source quotes used (paraphrased
  throughout). SecurityWeek's longest direct-quote passages exceed
  15 words; Archimedes paraphrases throughout.

  Per Hard Rule 8: Splunk first-party check ran (-72h sweep on
  redhat-cloud-services + Miasma + CVE-2026-45321 across
  defenseclaw_local + archimedes NOT sourcetype=archimedes:*).
  0 events. Silence not disconfirming.

source_reliability:
  primary_anchor:
    grade: B
    source_name: SecurityWeek (Ionut Arghire byline) - relay consolidating four vendor primaries
    source_yaml_id: securityweek
    grade_rationale: >
      Provisional B per source-grades.yaml (since 2026-05-06, awaiting
      ratification). SecurityWeek is the in-window publication surface
      consolidating four vendor research primaries. The relay itself
      does not elevate above B on the strength of its sources; per
      INTEL-GRADING, a B-grade relay aggregating C/B-grade primaries
      remains a B-grade cluster anchor.
    provisional: true
  corroborators:
    - grade: C
      source_name: ReversingLabs
      source_yaml_id: reversinglabs   # NOT in source-grades.yaml — first surface
      provisional: true
      awaiting_yaml_addition: true
      grade_rationale: >
        First Archimedes-corpus citation. Provisional C per first-
        surface vendor-research-firm precedent (same class as LayerX
        2026-05-08, Seqrite, Trendyol, Albayrak provisional-C starting
        grade). Contributed: 72-second publication window observation
        + CI/CD compromise analysis. Operator may upgrade to B on
        subsequent surfaces showing consistent technical rigor.
        Librarian: add to source-grades.yaml.
    - grade: C
      source_name: Aikido Security
      source_yaml_id: aikido-security
      provisional: true
      grade_rationale: >
        Provisional C per source-grades.yaml (since 2026-05-12). Contributed:
        GitHub Actions OIDC exploitation assessment. Track record on
        Mini Shai-Hulud family adjacent to VT-006 corpus state.
    - grade: B
      source_name: Ox Security
      source_yaml_id: ox-security
      provisional: true
      awaiting_direct_retrieval: true
      grade_rationale: >
        Provisional B per source-grades.yaml (since 2026-05-15).
        Contributed: 210 downstream infected repositories enumeration.
        Cited via SecurityWeek relay; Ox Security primary not directly
        retrieved this sweep — flagged for direct retrieval on next
        collector pass.
    - grade: B
      source_name: Socket
      source_yaml_id: socket
      provisional: true
      grade_rationale: >
        Provisional B per source-grades.yaml (since 2026-05-14;
        direct-retrieval flag lifted on 2026-06-01 via finding 0004
        direct Socket primary surface). Contributed: malware capability
        runtime analysis (credential-stealing worm class, encrypted
        exfiltration, self-propagation).

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent           # Miasma payload signature consistent with VT-006 family mechanism (install-time execution, credential harvest, CI/CD targeting, encrypted exfil, self-propagation); cross-corroborated against finding 0004 + VT-006 corpus state
    - probably_true_no_contradicting_ab      # No A/B source contradicts; Red Hat unpublishing the packages is implicit ground-truth confirmation
    - probably_true_claims_coherent          # CVE-2026-45321 family lineage internally coherent; @redhat-cloud-services scope verifiable; Miasma payload string is researcher-coined consensus
  rationale: >
    Grade 1 (Confirmed) reachable on the procedural-facts layer
    (compromise occurred, scope, mechanism class) — four independent
    vendor primaries with different evidence bases, neither cites the
    others as origin, technical artifacts (CVE, payload string,
    package scope) match. Cluster anchor held at 2 because the
    operator-WEP-relevant layers (specific TTP claims, TeamPCP
    attribution) are single-firm-or-aggregated and pull the
    composite down. Per skill rule: cluster-anchor primary claim
    includes both procedural facts and TTP-specific claims; the
    weakest load-bearing layer (single-firm TTP observations + carry-
    forward attribution) sets the anchor.

corroboration:
  independent_sources:
    - reversinglabs                # CI/CD compromise + 72s window analysis
    - aikido-security              # OIDC exploitation assessment
    - ox-security                  # 210 downstream repos enumeration
    - socket                       # runtime/binary capability analysis
  relay_anchor:
    - securityweek                 # consolidates the four primaries
  independent: true
  test_passed: >
    Four vendor primaries are independent publishing organizations,
    none cite the others as origin, different evidence bases. Remove
    any one and the other three still stand on their own evidence.
    SecurityWeek is the consolidating B-grade relay — the relay
    itself does not corroborate; the independence test applies to
    the four primaries.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_check_performed: true
  splunk_check_window: "-72h, index=defenseclaw_local OR index=archimedes (redhat-cloud-services OR Miasma OR CVE-2026-45321 OR @redhat-cloud-services) NOT sourcetype=archimedes:operation NOT sourcetype=archimedes:scheduler"
  splunk_check_result: "0 events. First-party telemetry silent on Miasma / redhat-cloud-services / CVE-2026-45321. Silence not disconfirming per Hard Rule 8."

single_source_veto_applied: true
single_source_veto_rationale: >
  Specific TTP layers (72s window, OIDC vector, 210 downstream repos)
  each carry single-firm origination. WEP on each capped at "likely"
  pending independent corroboration by a second vendor. TeamPCP
  attribution layer also capped at "likely" per carry-forward from
  finding 0004 (Socket originally declined attribution; SecurityWeek
  aggregation does not lift). Procedural-facts layer (compromise,
  scope, family lineage) NOT subject to veto due to four-vendor
  independence.

wep_ceiling: very_likely    # for procedural facts (compromise occurred, scope, family lineage)
wep_ceiling_attribution_layer: likely   # carry-forward from finding 0004; TeamPCP restatement does not lift
wep_ceiling_specific_ttp_layers: likely   # 72s window, OIDC vector, 210 downstream repos — single-firm origination

inclusion:
  eligible_for:
    - daily_brief_monitoring
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update
    - vuln_tracker_dossier_update   # VT-006 dossier should fold this campaign-progression observation
    # NOT flash — campaign-progression and attribution-restatement do not trigger FLASH per FLASH-POLICY Trigger 2 (attribution_is_new_not_restatement); collector evaluated Trigger 2 as FAIL and Trigger 5 as FAIL (no A&D-prime named victim)
  inclusion_threshold_test:
    daily_brief_action_b2_minimum: pass
    daily_brief_monitoring_c3_minimum: pass
    weekly_synthesis_c3_minimum: pass

# Cluster metadata
cluster:
  topic: "Red Hat @redhat-cloud-services npm 32-package / 96-malicious-version compromise identified as Mini Shai-Hulud (VT-006 family) Miasma variant; multi-firm independent corroboration (ReversingLabs + Aikido + Ox Security + Socket) via SecurityWeek consolidation; GitHub Actions OIDC CI/CD compromise vector; 72-second publication window; 210 downstream infected repositories; TeamPCP attribution restated"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-02-am-003-securityweek-supply-chain-red-hat-npm-32-packages-miasma-mini-shai-hulud-vt006-family-extension
  campaign_progression_relates_to:
    - finding-2026-06-01-0004-socket-thn-miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain-vt006-family-expansion-anthropic-impersonation-c2
    - finding-2026-05-12-FLASH-0001   # original VT-006 family disclosure
    - finding-2026-05-27-0007         # VT-006 CISA KEV listing
  vuln_tracker_index_match:
    - vuln_id: VT-006
      vuln_name: Mini Shai-Hulud npm + PyPI self-propagating worm family
      cve: CVE-2026-45321
      family_extension_event: Miasma variant adds Red Hat @redhat-cloud-services scope to family member list (after TanStack + Nx Console)
  attribution_claims:
    - claimed_actor: TeamPCP
      claimed_actor_roster_id: "001"
      claimed_by_sources: [securityweek aggregation through (reversinglabs + aikido + ox-security + socket)]
      requires_analyst_review: true
      hard_rule_2_compliance_note: >
        TeamPCP attribution is RESTATEMENT not origination per finding
        0004 grading. Socket originally declined attribution. The
        2026-06-02 SecurityWeek "TeamPCP identified ... behind this
        campaign" framing is reporter-aggregated through the four
        vendors and does not independently verify each vendor's
        verbatim attribution stance. Carry-forward at "likely" WEP.

# Downstream handoff flags
analyst_review_required: true
analyst_review_reasons:
  - vt_006_family_extension_event_warrants_sat_kac_on_attribution_carry_forward_assumption
  - github_actions_oidc_cicd_compromise_vector_warrants_sat_ach_on_alternative_initial_access_hypotheses
  - 72_second_publication_window_warrants_sat_kac_on_automated_pipeline_vs_interactive_attacker_assumption
  - supersession_or_keep_both_decision_required_vs_finding_2026_06_01_0004
red_team_review_required: false
red_team_review_reasons:
  - cluster_anchor_wep_ceiling_very_likely_on_procedural_only_with_likely_on_specific_ttp_and_attribution_layers
  - no_ad_prime_named_victim_no_named_a_and_d_targeting
red_team_review: null
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Given Aikido's single-firm attribution of the @redhat-cloud-services npm 32-package / 96-version compromise initial-access vector to GitHub Actions OIDC token-issuance flow exploitation, what is the most consistent initial-access hypothesis when alternatives are weighed against the ReversingLabs 72-second publication window and the @redhat-cloud-services scope completeness pattern?"
      analyzed_at: 2026-06-02T09:02:00-04:00
      analyzed_by: analyst
      red_team_review: null
      analyst_caveat: >
        ACH is on the INITIAL-ACCESS-VECTOR layer, NOT on the TeamPCP
        attribution layer. The TeamPCP attribution is carry-forward
        RESTATEMENT from finding 0004 — Hard Rule 2 prohibits Archimedes
        from independently asserting or revising that attribution. This
        ACH operates BELOW the attribution layer on a separate technical
        question that does not implicate Hard Rule 2.
      hypotheses:
        - id: H1
          statement: "GitHub Actions OIDC federated-identity compromise — attacker abused the OIDC token-issuance flow to obtain npm publish credentials via federated identity rather than static-token theft (Aikido's stated hypothesis)."
        - id: H2
          statement: "Static npm publish-token theft via separate Red Hat maintainer compromise vector (maintainer-account phishing, malicious browser extension, dev-laptop compromise, or credential leak on maintainer side), with attacker-side automation reproducing the 72-second publication window."
        - id: H3
          statement: "Compromised GitHub Actions self-hosted runner with npm credentials in environment variables — runner was the persistence pivot, with publish credentials harvested from runtime environment."
        - id: H4
          statement: "Insider compromise on Red Hat npm publishing infrastructure (rogue maintainer / contractor / supply-chain insider)."
        - id: H5
          statement: "Compromise of the @redhat-cloud-services GitHub organization-level deploy credentials (separate from per-package maintainer tokens), giving scope-wide publish authority."
      evidence:
        - id: E1
          description: "72-second publication window across 96 malicious versions (ReversingLabs single-firm)."
          source: reversinglabs
          digraph: B2
          weight: 2
        - id: E2
          description: "@redhat-cloud-services scope-completeness: 32 packages (the entire scope of Red Hat Hybrid Cloud Console JavaScript ecosystem) compromised, not a selective subset."
          source: securityweek + socket
          digraph: B1
          weight: 2
        - id: E3
          description: "Aikido assessment: GitHub Actions OIDC token-issuance flow as initial-access vector (Aikido single-firm origination, provisional C)."
          source: aikido-security
          digraph: C2
          weight: 1
        - id: E4
          description: "210 downstream infected repositories with stolen credentials propagated from initial Red Hat maintainer compromise (Ox Security single-firm)."
          source: ox-security
          digraph: B2
          weight: 2
        - id: E5
          description: "Miasma payload-embedded researcher-coined string consistent across all 96 malicious versions; mechanism-class match to VT-006 Mini Shai-Hulud family (credential-stealing worm, encrypted exfiltration, GitHub-based fallback C2)."
          source: socket
          digraph: B2
          weight: 2
        - id: E6
          description: "Red Hat detected and unpublished; no independent Red Hat IR statement at sweep time."
          source: securityweek
          digraph: B1
          weight: 2
        - id: E7
          description: "Carry-forward from finding 0004: Anthropic-API-impersonation C2 (api.anthropic[.]com), AES-128/256-GCM + RSA-OAEP encryption, 'ifyouinvalidatethistoken' internal payload string — sophisticated C2 / encryption stack."
          source: finding-0004-socket-primary
          digraph: B2
          weight: 2
        - id: E8
          description: "First-party Splunk silent on Miasma / redhat-cloud-services / CVE-2026-45321 (-72h, 0 events)."
          source: splunk-first-party
          digraph: A1
          weight: 2
      matrix:
        E1: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E2: {H1: C, H2: I, H3: C, H4: C, H5: C}
        E3: {H1: C, H2: I, H3: I, H4: I, H5: I}
        E4: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E5: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E6: {H1: N, H2: N, H3: N, H4: N, H5: N}
        E7: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E8: {H1: N, H2: N, H3: N, H4: N, H5: N}
      inconsistency_counts:
        H1: 0
        H2: 2
        H3: 1
        H4: 1
        H5: 1
      diagnostic_evidence:
        - E2: "Scope-completeness (32 of 32 packages compromised, not selective) is MORE consistent with scope-wide credential compromise (H1/H3/H4/H5) than with per-maintainer-account theft (H2 — multiple separate maintainer compromises would be required to hit the full scope, less plausible)."
        - E3: "Aikido's stated OIDC vector is the only hypothesis with affirmative single-firm support. The other hypotheses are alternative explanations that current evidence does not support but does not rule out."
        - E1: "72-second window is consistent with ALL hypotheses given attacker automation; it does NOT distinguish OIDC-vector from credential-theft-with-automation. Less diagnostic than the grader's framing suggested."
      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: "Zero inconsistencies; affirmative single-firm support (Aikido); scope-completeness fits OIDC-federated-identity model where compromised CI/CD owns the whole scope. Aikido provisional-C source weight is modest, so not promoted to 'likely' alone."
          wep: likely
        - rank: 2
          hypothesis_id: H3
          rationale: "One inconsistency via E3 (Aikido specifically calls OIDC vector, not self-hosted-runner compromise; mild evidence against). Scope-completeness fits. Cannot be ruled out without runner-environment forensics."
          wep: roughly_even_chance
        - rank: 2_tie
          hypothesis_id: H5
          rationale: "One inconsistency via E3. Scope-completeness fits org-level deploy credential compromise. Distinguishable from H1 only by specific token-issuance-flow forensics."
          wep: roughly_even_chance
        - rank: 4
          hypothesis_id: H4
          rationale: "One inconsistency via E3. Insider hypothesis cannot be ruled out without Red Hat IR statement, but is less parsimonious given the worm-propagation pattern (E4) that suggests automated rather than deliberate."
          wep: unlikely
        - rank: 5
          hypothesis_id: H2
          rationale: "Two inconsistencies. Per-maintainer-token theft would require multiple separate compromises to hit the full @redhat-cloud-services scope; less parsimonious than scope-wide credential compromise."
          wep: very_unlikely
      sensitivity_analysis:
        brittleness: medium_to_high
        load_bearing_evidence: [E2, E3]
        if_aikido_oidc_attribution_walked_back: "H1 demoted to tied with H3/H5; current ranking-1 loses its single affirmative source."
        if_red_hat_publishes_ir_statement_naming_vector: "Likely resolves H1 vs H3 vs H5 definitively; rerun ACH."
        if_72_second_window_reframed_as_attacker_automation: "E1 weight to H2 increases; current ranking-5 rises but does not exceed scope-completeness logic."
        single_point_of_failure: "Aikido's OIDC assessment is the SOLE source for the leading hypothesis's specific mechanism. Aikido is provisional-C; a second firm corroborating OIDC-vector specifically would lift this substantially."
      tripwires:
        - observation: "Red Hat publishes incident response statement naming initial-access vector."
          effect: "Resolve H1 vs H3 vs H4 vs H5 definitively; rerun ACH or close it."
        - observation: "Second vendor (ReversingLabs, Socket, Ox Security, GitGuardian, Snyk, Mend) independently confirms OIDC-vector."
          effect: "H1 weight increases substantially; promote to 'very likely' (with single-source veto cleared)."
        - observation: "GitHub publishes incident communication on OIDC-token-issuance abuse pattern."
          effect: "First-party from the OIDC token issuer; resolves the mechanism layer."
        - observation: "Similar OIDC-CI/CD-compromise pattern observed against second npm-scope (non-Red-Hat)."
          effect: "Promotes H1 mechanism as TTP-class, not single-incident."
        - observation: "Red Hat maintainer surfaces with phishing or credential-theft incident report."
          effect: "H2 weight increases; H1 weight decreases."
      conclusion:
        summary: >
          GitHub Actions OIDC federated-identity compromise (H1, Aikido's stated hypothesis)
          is the leading initial-access hypothesis with zero inconsistencies and the only
          affirmative single-firm support. Self-hosted-runner compromise (H3) and
          organization-level deploy credential compromise (H5) are close alternatives that
          cannot be ruled out. Per-maintainer-token theft (H2) is least consistent given
          the scope-completeness pattern. The 72-second window (ReversingLabs) is LESS
          diagnostic than the grader's framing suggested — it fits all hypotheses given
          attacker automation. Brief language should preserve H1 leadership without
          over-confidence relative to H3/H5.
        wep: likely
        confidence_caveats: >
          Aikido provisional-C single-firm origination on OIDC-vector is the load-bearing
          evidence. Sensitivity is MEDIUM-to-HIGH on Aikido reliability. Single-source veto
          already applied at grader level holds. WEP ceiling on initial-access vector
          unchanged at 'likely.' No actor-attribution implications — TeamPCP carry-forward
          remains independent of this initial-access-vector analysis.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Multi-firm restatement of TeamPCP attribution via SecurityWeek's
        four-vendor aggregation does NOT lift the carry-forward 'likely' WEP
        ceiling on TeamPCP attribution from finding 0004, because Socket
        originally explicitly declined attribution and SecurityWeek's
        aggregation does not independently verify each vendor's verbatim
        attribution stance."
      analyzed_at: 2026-06-02T09:08:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Attribution carry-forward conservatism is the grader's epistemic
        position. KAC interrogates whether the conservatism is correctly
        calibrated or over-applied.
      assumptions:
        - id: A1
          statement: "Socket's original explicit declination of attribution on the 2026-05-12 Mini Shai-Hulud disclosure carries forward to the 2026-06-01 / 2026-06-02 Red Hat-scope event UNTIL Socket explicitly attributes."
          category: source_reliability
          stated: true
          why_must_be_true: "If Socket has since attributed (in a later post not captured), the carry-forward conservatism is unwarranted."
          when_could_be_false: "Socket may have published a follow-up blog post attributing the Red Hat-scope event to TeamPCP; collector did not capture it this sweep."
          evidence_for: [finding-0004-socket-directly-retrieved-still-declines]
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify
          remediation_note: "Collector to flag Socket primary for direct retrieval next pre-brief pass to confirm Socket's current attribution stance specifically on the Red Hat-scope event."
        - id: A2
          statement: "SecurityWeek's 'TeamPCP identified as the threat group behind this campaign' framing is REPORTER-AGGREGATED rather than reflecting each of the four vendors' verbatim attribution."
          category: source_reliability
          stated: true
          why_must_be_true: "If each of the four vendors INDEPENDENTLY attributed to TeamPCP in their primaries, the four-vendor corroboration would substantially lift the WEP — but Archimedes hasn't directly retrieved each primary."
          when_could_be_false: "ReversingLabs / Aikido / Ox Security / Socket primaries may each carry TeamPCP attribution explicitly; SecurityWeek's framing may be accurate verbatim restatement."
          evidence_for: [securityweek-aggregation-pattern-historical, socket-finding-0004-explicit-decline]
          evidence_against: []
          confidence: low
          centrality: critical
          classification: test
          proposed_test: >
            Collector to directly retrieve each of the four vendor primaries
            (ReversingLabs, Aikido, Ox Security, Socket) on the Red Hat-scope
            event and document each vendor's verbatim attribution stance.
            If 2+ of 4 vendors INDEPENDENTLY attribute to TeamPCP, WEP can
            promote from 'likely' to 'very likely' per multi-source
            independent attribution rule.
        - id: A3
          statement: "Reporter-aggregated multi-vendor restatement is qualitatively different from independent multi-source attribution for WEP-lifting purposes."
          category: source_reliability
          stated: false
          why_must_be_true: "Implicit premise of the grader's conservatism. If reporter-aggregation counts as independent corroboration, the WEP-lift would already apply."
          when_could_be_false: "INTEL-GRADING doctrine may treat reporter-aggregation of multiple primaries as sufficient for independence-lifting; this depends on whether the reporter has done verification work or simply summarized."
          evidence_for: [doctrine-intel-grading-independence-test-emphasizes-evidence-base-independence]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A4
          statement: "The 'likely' WEP ceiling on attribution layer holds operational value relative to a hypothetical 'very likely' — i.e., the difference matters for downstream brief language and operator action."
          category: semantic
          stated: false
          why_must_be_true: "If 'likely' vs 'very likely' makes no operational difference, the carry-forward conservatism is academic."
          when_could_be_false: "WEP vocabulary differences DO drive brief language ('TeamPCP likely' vs 'TeamPCP very likely') and downstream actor-profiler dossier confidence; the distinction is operationally material per INTEL-GRADING."
          evidence_for: [doctrine-intel-grading-wep-vocabulary-mapping]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A5
          statement: "TeamPCP is a coherent actor cluster, not a label aggregated across loosely-related supply-chain compromise activity."
          category: actor_continuity
          stated: false
          why_must_be_true: "If TeamPCP is a fuzzy cluster label, attribution to 'TeamPCP' is less precise than the WEP language implies."
          when_could_be_false: "Supply-chain attribution clusters notoriously fuzzy across vendors (Lazarus / APT38 / BlueNoroff overlap; TA505 fluidity)."
          evidence_for: [actor-001-teampcp-dossier-state]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "Promotion threshold for restatement-to-attribution-confirmation should be 2+ independent direct primaries (per single-source veto inverse)."
          category: source_reliability
          stated: false
          why_must_be_true: "Implicit threshold logic. If a single-vendor primary suffices, A1 already broken; if 4+ are required, the bar may never be cleared in practice."
          when_could_be_false: "Could be argued at 2 (mirroring single-source veto) or at 3 (stricter for attribution). Doctrine is somewhat under-specified here."
          evidence_for: [doctrine-intel-grading-single-source-veto-implies-2-source-minimum]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
      classifications_summary:
        sound: 2
        qualify: 3
        test: 1
        reject: 0
      remediation:
        status: proceed_with_qualifying_caveats_and_collector_test_flagged
        blocking_assumption: A2
        blocking_detail: >
          The TeamPCP attribution-restatement carry-forward conservatism
          is defensible BUT depends on A2 (reporter-aggregated vs
          independent-vendor-verbatim). The TEST is a collector retrieval
          task, not a halt-the-brief task. The 'likely' ceiling holds for
          this brief cycle; collector to directly retrieve each of the
          four vendor primaries before next AM brief.
        qualifying_caveats:
          - "TeamPCP attribution is restated by SecurityWeek consolidating four vendor primaries; Archimedes has NOT directly retrieved each vendor's verbatim attribution stance, so the 'likely' WEP carry-forward from finding 0004 holds rather than promoting to 'very likely.'"
          - "If 2+ of the four vendor primaries are directly retrieved next pre-brief and independently attribute to TeamPCP, WEP can promote per multi-source independence rule."
          - "TeamPCP actor-cluster coherence is medium-confidence (A5); attribution applies to the cluster as currently defined in roster, not to a strictly atomic operator."
        next_action: >
          Collector to flag direct-retrieval task on ReversingLabs, Aikido,
          Ox Security, Socket primaries for the Red Hat @redhat-cloud-services
          event in next pre-brief pass. Vuln-tracker to fold Miasma variant,
          OIDC vector, 72s window, and 210 downstream repos into VT-006
          dossier scaffold.
      recommended_wep_after_test:
        if_two_or_more_vendor_primaries_independently_attribute_to_teampcp: "Promote attribution WEP to very_likely; remove single-source veto."
        if_zero_or_one_vendor_primary_independently_attributes: "Hold attribution WEP at likely; conservatism vindicated."
        if_a_vendor_primary_diverges_or_disconfirms: "Demote attribution WEP to roughly_even_chance and rerun ACH on attribution."
  sat_kac_2:
    kac_analysis:
      assessment_under_review: >
        "ReversingLabs's 72-second publication window across 96 malicious
        versions is diagnostic of automated CI/CD-pipeline-driven publication
        rather than interactive attacker session, and supports the GitHub
        Actions OIDC initial-access vector hypothesis."
      analyzed_at: 2026-06-02T09:12:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Specific TTP claim flagged for KAC interrogation. The 72-second
        framing is a load-bearing premise for the OIDC-vector hypothesis.
      assumptions:
        - id: B1
          statement: "72 seconds is empirically distinguishable from fast-scripted-interactive (an attacker-with-credentials running their own npm-publish loop)."
          category: technology
          stated: true
          why_must_be_true: "If a credentialed attacker could trivially reproduce the 72s window with their own script, the window does not distinguish 'CI/CD-pipeline-driven' from 'attacker-automation-driven.'"
          when_could_be_false: "Running 'npm publish' in a shell loop for 96 packages CAN complete in 72s on a fast connection. npm publish per-package round-trip is typically 0.5-2s; 96 * 0.75s = 72s. The window is NOT diagnostic of pipeline-vs-attacker-automation."
          evidence_for: []
          evidence_against: [empirical-npm-publish-latency-public-reference]
          confidence: low
          centrality: critical
          classification: reject
          remediation_note: >
            The 72s window is consistent with attacker automation running
            'npm publish' in a loop with credentials. It is therefore NOT
            diagnostic of CI/CD-pipeline compromise specifically. Brief
            language must NOT use the 72s window as evidence for the OIDC
            vector. The OIDC vector evidence is the Aikido single-firm
            assessment, NOT the publication-window forensics.
        - id: B2
          statement: "ReversingLabs's 'automated CI/CD push' inference is grounded in additional forensic detail (e.g., GitHub Actions runner artifacts, OIDC token signatures in publish requests) not captured in the SecurityWeek summary."
          category: source_reliability
          stated: false
          why_must_be_true: "If ReversingLabs has runner artifacts or token-signature forensics, the inference is well-grounded; if not, it is window-size pattern-match only."
          when_could_be_false: "ReversingLabs primary not directly retrieved this sweep; cannot verify forensic basis."
          evidence_for: []
          evidence_against: []
          confidence: unknown
          centrality: material
          classification: test
          proposed_test: >
            Collector to directly retrieve ReversingLabs primary on the
            Red Hat-scope event in next pre-brief; document whether
            inference is supported by additional forensics or by window-
            size pattern-match alone.
        - id: B3
          statement: "Interactive vs automated publication distinction has operational value for defender response."
          category: semantic
          stated: false
          why_must_be_true: "If the distinction doesn't drive defender action, the inference is academic."
          when_could_be_false: "Interactive vs automated DOES drive credential-rotation scope, CI/CD-pipeline-audit prioritization, and incident scoping; operationally material."
          evidence_for: []
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 1
        qualify: 0
        test: 1
        reject: 1
      remediation:
        status: revise_assessment
        blocking_assumption: B1
        blocking_detail: >
          B1 is REJECTED on empirical grounds. The 72s window is consistent
          with attacker-automation-with-credentials AND with CI/CD-pipeline-
          driven publication — it does NOT distinguish between them.
          Therefore the 72s window does NOT support the OIDC-vector
          hypothesis specifically.
        qualifying_caveats:
          - "72-second publication window is consistent with both CI/CD-pipeline-driven push AND attacker-automation-with-stolen-credentials; the window alone does NOT distinguish the two. ReversingLabs's 'automated CI/CD' framing is single-firm inference; brief language should preserve the window observation but NOT use it as evidence for the OIDC vector specifically."
          - "OIDC vector hypothesis rests on Aikido's assessment alone; awaiting direct retrieval of ReversingLabs primary to verify whether additional forensic basis exists."
        next_action: >
          Briefer to revise language on the 72s window framing: report
          the observation factually (72s across 96 versions) but do NOT
          cite it as diagnostic of CI/CD-vector specifically. Collector
          to directly retrieve ReversingLabs primary.
      recommended_wep_after_test:
        if_reversinglabs_primary_carries_additional_forensics: "Restore 72s window as supporting evidence; WEP on OIDC vector holds at 'likely.'"
        if_reversinglabs_primary_is_window_size_pattern_match_only: "Maintain revised brief language; do NOT use 72s as OIDC-vector evidence."

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-02-morning]
retracted: false
retraction_brief_id: null

# Source-grade revision proposals
source_grade_revision_proposed:
  - source_yaml_id: reversinglabs
    current_grade: not_in_yaml
    proposed_grade: C_provisional
    reason: >
      First Archimedes-corpus citation. Vendor-research-firm tier
      (npm/supply-chain forensics). Provisional C per first-surface
      precedent class (LayerX, Seqrite, Trendyol, Albayrak).
      Operator may upgrade to B on subsequent surfaces showing
      consistent technical rigor.
    severity: addition_not_revision
    action: "Add reversinglabs to source-grades.yaml as provisional-C, category=vendor, awaiting_ratification: true"
---

# Red Hat @redhat-cloud-services npm 32-package compromise identified as Mini Shai-Hulud "Miasma" variant; multi-firm corroboration adds GitHub Actions OIDC vector + 210 downstream repos to VT-006 corpus

## Summary

SecurityWeek (Ionut Arghire byline, 2026-06-02 05:51 EDT) consolidates four independent vendor research surfaces — ReversingLabs, Aikido Security, Ox Security, and Socket — on the Red Hat @redhat-cloud-services npm 32-package / 96-malicious-version supply-chain compromise, identifying it as a Mini Shai-Hulud (VT-006 family) variant carrying the researcher-coined "Miasma: The Spreading Blight" payload string. New material vs. the 2026-06-01 Socket + The Hacker News origination (finding-2026-06-01-0004): GitHub Actions OIDC token-issuance flow exploited as the CI/CD compromise vector (Aikido); 72-second automated publication window across the 96 malicious versions (ReversingLabs); 210 downstream infected repositories with stolen credentials (Ox Security); explicit "Miasma" variant name. TeamPCP attribution restated through SecurityWeek's four-vendor aggregation. No A&D-prime named as downstream victim; transitive-dependency exposure for any A&D prime running Red Hat Hybrid Cloud Console or pulling the scope into SDLC pipelines remains a structural concern. CISA KEV federal compliance deadline for CVE-2026-45321 family is 2026-06-10 (T-8 days).

## Sources

### SecurityWeek (Ionut Arghire byline, source_yaml_id: securityweek, digraph: B for relay)

- URL: https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/
- Published: 2026-06-02T09:51 GMT (05:51 EDT, in window)
- Key claim: Consolidates four independent vendor research surfaces on the Red Hat npm scope compromise; identifies as Mini Shai-Hulud "Miasma" variant attributed to TeamPCP (restatement); enumerates the GitHub Actions OIDC vector, 72s publication window, 210 downstream repos.

### ReversingLabs (source_yaml_id: reversinglabs, digraph: C provisional, FIRST CORPUS SURFACE)

- URL: cited via SecurityWeek aggregation; primary not directly retrieved this sweep
- Key claim: 72-second publication window across 96 malicious versions (indicative of automated CI/CD push, not interactive attacker session); CI/CD compromise analysis.
- **Librarian note:** First Archimedes-corpus citation. Add to source-grades.yaml as provisional-C, category=vendor.

### Aikido Security (source_yaml_id: aikido-security, digraph: C provisional)

- URL: cited via SecurityWeek aggregation; primary not directly retrieved this sweep
- Key claim: GitHub Actions OIDC token-issuance flow exploited to obtain npm publish credentials from federated identity (rather than static maintainer-account compromise).

### Ox Security (source_yaml_id: ox-security, digraph: B provisional)

- URL: cited via SecurityWeek aggregation; primary not directly retrieved this sweep (Ox Security awaiting_direct_retrieval flag in source-grades.yaml since 2026-05-15)
- Key claim: 210 downstream infected repositories with stolen credentials (the worm propagated from the initial @redhat-cloud-services maintainer compromise into 210 downstream consumer-repos that pulled and ran the malicious versions).

### Socket (source_yaml_id: socket, digraph: B provisional)

- URL: socket.dev/blog primary (already directly retrieved on 2026-06-01 via finding 0004; this sweep relies on the carry-forward direct-retrieval lifting)
- Key claim: Mini Shai-Hulud variant capabilities — credential-stealing worm class, exfiltration to attacker-controlled server, GitHub-based fallback C2.

## Technical detail

**Vulnerability tracker context:** This finding extends **VT-006** (Mini Shai-Hulud npm + PyPI self-propagating worm family). VT-006 carries CVE-2026-45321 and is CISA KEV-listed (catalog version 2026.05.27) with federal compliance deadline **2026-06-10 (T-8 days from this finding)**.

**Mechanism class:**
- **Publication forensics (ReversingLabs):** 72-second window between earliest and latest malicious-version publication across 96 versions. Indicative of automated push via compromised CI/CD pipeline, not interactive attacker session.
- **CI/CD compromise vector (Aikido):** GitHub Actions OIDC token-issuance flow exploited. Federated identity used to obtain npm publish credentials rather than static-maintainer-account theft. Mechanism class only — no PoC, no walkthrough, no attack-step detail preserved per Hard Rule 3.
- **Downstream blast radius (Ox Security):** 210 infected repositories with stolen credentials. The worm propagated from the @redhat-cloud-services maintainer compromise into 210 downstream consumer-repos that pulled and executed the malicious versions.
- **Runtime capabilities (Socket):** Credential-stealing worm class; exfiltration to attacker-controlled server; GitHub-based fallback C2.

**Miasma variant payload string:** "Miasma: The Spreading Blight" — payload-embedded researcher-coined working name for this specific Mini Shai-Hulud variant. Distinct from parent family name "Mini Shai-Hulud" used in VT-006 dossier.

**Affected scope:** @redhat-cloud-services npm scope. 32 packages. 96 malicious versions. ~10 million collective downloads (SecurityWeek-stated aggregate). Red Hat detected and unpublished. Red Hat has NOT published an independent incident response statement at sweep time.

## IOCs surfaced

```yaml
indicators:
  - type: cve
    value: CVE-2026-45321
    confidence: high
    context: >
      VT-006 family parent CVE. Mini Shai-Hulud npm + PyPI self-
      propagating worm. KEV-listed 2026-05-27 with 2026-06-10 federal
      deadline. The 2026-06-02 Red Hat @redhat-cloud-services 32-package
      compromise is a downstream extension of this CVE's mechanism class.
    sources:
      - https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/

  - type: malware_family
    value: "Mini Shai-Hulud"
    variant_name: "Miasma" / "Miasma: The Spreading Blight"
    confidence: high
    context: >
      Researcher-coined variant name identified via payload-embedded
      string. Distinct from parent family name. Variant compromised
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
    confidence: medium     # single-firm (ReversingLabs) origination; single-source veto applied
    context: >
      ReversingLabs analysis indicates automated publication via
      compromised CI/CD pipeline (not interactive attacker session).
    sources:
      - https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/

  - type: ttp_observation
    value: "GitHub Actions OIDC token-issuance flow as CI/CD compromise vector"
    confidence: medium     # single-firm (Aikido) origination; single-source veto applied
    context: >
      Aikido assessment. Federated identity exploited to obtain npm
      publish credentials.
    sources:
      - https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/

  - type: ttp_observation
    value: "210 downstream infected repositories with stolen credentials"
    confidence: medium     # single-firm (Ox Security) origination; single-source veto applied
    context: >
      Ox Security enumeration. Worm-propagation blast radius from
      initial Red Hat maintainer compromise.
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
    confidence_language: descriptive
    actor_named: TeamPCP (corpus actor id 001)
    family_lineage: Mini Shai-Hulud (VT-006), via Shai-Hulud family
    novelty_layer: "Miasma" variant name first surface in corpus on 2026-06-02
    archimedes_compliance_note: >
      RESTATEMENT not origination. TeamPCP attribution carry-forward
      from finding 0004; the four-vendor SecurityWeek consolidation
      does NOT lift the WEP ceiling on attribution because Socket
      originally explicitly declined attribution and the four
      vendors' verbatim attribution stances were not independently
      directly retrieved. Hard Rule 2 compliant.
```

## Relationship to existing findings

**Campaign-progression extension of finding-2026-06-01-0004** (Socket + THN origination of the Red Hat npm Miasma campaign with Anthropic-API-impersonation C2 detail). This finding is NOT a supersession — finding 0004's Anthropic-API-impersonation C2 detail (`api.anthropic[.]com` impersonation; AES-128/256-GCM + RSA-OAEP encryption; SHA-256 published tarball hashes; "ifyouinvalidatethistoken" internal payload string) remains finding 0004's unique contribution and is NOT in this 2026-06-02 SecurityWeek surface.

**Adds to finding 0004:**
- Miasma variant name (vs. finding 0004's "the Mini Shai-Hulud campaign on Red Hat npm" generic framing)
- Multi-firm corroboration layer (four vendors vs. finding 0004's Socket+THN)
- GitHub Actions OIDC CI/CD compromise vector
- 72-second automated publication window
- 210 downstream infected repositories

**Cross-references VT-006 family lineage:**
- finding-2026-05-12-FLASH-0001 (original Mini Shai-Hulud disclosure; TanStack + @uipath + @mistralai + @opensearch-project + @squawk aviation + ~172 packages)
- finding-2026-05-27-0007 (CISA KEV listing of CVE-2026-45321; federal deadline 2026-06-10)
- finding-2026-06-01-0004 (Red Hat @redhat-cloud-services 32-package origination)

**Analyst/red-team supersession decision:** Recommend keeping both findings with explicit cross-reference. Both contribute unique material; supersession would lose the Anthropic-API-impersonation C2 detail from finding 0004.

## Analytic notes (from analyst review)

ACH on the initial-access vector keeps GitHub Actions OIDC federated-identity compromise (H1, Aikido's stated hypothesis) at rank 1 with zero inconsistencies and the only affirmative single-firm support. Self-hosted-runner compromise (H3) and organization-level deploy credential compromise (H5) are close alternatives that scope-completeness cannot distinguish from H1; per-maintainer-token theft (H2) is least consistent. Aikido is provisional-C single-firm — sensitivity is MEDIUM-to-HIGH on Aikido's reliability. The TeamPCP attribution-restatement is OUT OF SCOPE for this ACH; Hard Rule 2 leaves it as carry-forward from finding 0004.

KAC on the TeamPCP attribution carry-forward conservatism vindicates the grader's 'likely' ceiling: SecurityWeek's framing is reporter-aggregated rather than verified-verbatim across the four vendor primaries, and Socket originally explicitly declined. Collector to directly retrieve each of the four vendor primaries before next AM brief; if 2+ independently attribute to TeamPCP, WEP can promote.

KAC on the 72-second publication window REJECTS the diagnostic claim: 72s is consistent with both CI/CD-pipeline-driven publication AND attacker-automation-with-stolen-credentials (96 * ~0.75s per npm publish round-trip ~ 72s). Brief must report the observation factually but NOT cite it as evidence for the OIDC vector specifically. OIDC-vector hypothesis rests on Aikido's single-firm assessment alone — narrower but defensible framing.

## Open questions for analyst

1. **SAT-KAC candidate — attribution carry-forward assumption.** Key embedded assumption: "Multi-firm restatement of TeamPCP attribution does not lift the carry-forward 'likely' WEP ceiling because the originating Socket primary explicitly declined attribution." KAC evaluation:
   - Does reporter-aggregation through four vendor primaries (SecurityWeek's framing) constitute independent corroboration even if each vendor's verbatim attribution stance is not directly retrieved?
   - At what threshold of independent restatements does carry-forward attribution promote from "likely" to "very likely"?
   - Is the conservative carry-forward defensible if the original Socket primary on the new Red Hat-scope event also DECLINES attribution (vs. Socket's earlier explicit decline applied to the 2026-05-12 origination)?

2. **SAT-ACH candidate — alternative initial-access hypotheses on GitHub Actions OIDC vector.** Aikido attributes the CI/CD compromise to GitHub Actions OIDC token-issuance flow exploitation. ACH framing for alternative explanations:
   - H1: GitHub Actions OIDC federated-identity compromise (Aikido stated hypothesis)
   - H2: Static maintainer npm token theft via separate compromise vector (e.g., maintainer-account phishing, malicious browser extension, dev-laptop compromise)
   - H3: Compromised GitHub Actions self-hosted runner with npm credentials in environment
   - H4: Insider compromise on Red Hat npm publishing infrastructure
   Independence-test each hypothesis against the 72-second publication window (which is more consistent with H1/H3 automated CI/CD vs. H2 interactive theft) and the @redhat-cloud-services scope-completeness pattern.

3. **SAT-KAC candidate — automated-pipeline-vs-interactive-attacker assumption.** Key embedded assumption: "72-second publication window across 96 malicious versions is indicative of automated CI/CD push, not interactive attacker session." KAC evaluation:
   - What window size would distinguish automated-pipeline from fast-but-scripted-interactive (e.g., a maintainer-account holder running an npm-publish loop)?
   - Could the 72s window be reproduced by an attacker with stolen credentials running their own automation, vs. requiring CI/CD pipeline compromise?

4. **Supersession-vs-keep-both decision required.** Grader recommendation is KEEP BOTH (this finding + finding 0004) with cross-reference. Analyst / red-team / vuln-tracker should confirm or override. If supersession is chosen, finding 0004's Anthropic-API-impersonation C2 detail must be folded into the consolidated finding.

5. **Vuln-tracker dossier update.** VT-006 dossier should fold the Miasma variant, the GitHub Actions OIDC vector, the 72s window, and the 210 downstream repos enumeration. VT-006 has not yet been scaffolded as a C3PO-migrated dossier per `_index.yaml` line 496 — recommend vuln-tracker scaffold on next pass.

6. **CISA KEV federal compliance deadline T-8 days.** CVE-2026-45321 KEV-listed 2026-05-27; FCEB deadline 2026-06-10. This finding is operationally adjacent to the deadline; A&D-prime customer organizations with FCEB-adjacent compliance posture (CMMC L3 mappers to NIST 800-171 / 800-172) should treat the deadline as a watch-item for their own RHEL / OpenShift / Red Hat Hybrid Cloud Console SBOM hygiene.
