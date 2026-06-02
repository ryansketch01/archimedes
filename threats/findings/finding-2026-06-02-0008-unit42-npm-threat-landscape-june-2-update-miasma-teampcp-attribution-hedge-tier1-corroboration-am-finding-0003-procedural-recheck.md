---
finding_id: finding-2026-06-02-0008-unit42-npm-threat-landscape-june-2-update-miasma-teampcp-attribution-hedge-tier1-corroboration-am-finding-0003-procedural-recheck
created_at: 2026-06-02T16:26:00-04:00
graded_by: grader
grading_run_id: afternoon-20260602-160000
grading_mode: scheduled_brief
test: false
status: graded
relates_to: finding-2026-06-02-0003-securityweek-reversinglabs-aikido-ox-socket-miasma-red-hat-npm-32-package-vt006-extension-multi-firm-corroboration-oidc-cicd-vector
relation_type: tier1_vendor_corroboration_with_explicit_attribution_hedge_ratification    # NOT supersession; AM finding 0003 carries originating four-vendor cluster, this finding adds Tier-1 vendor weight + ratifies AM Hard Rule 2 stance

# Core grading (admiralty-grading skill output)
digraph: B1
digraph_layered:
  unit42_published_june_2_update_to_npm_threat_landscape_post_documenting_miasma_red_hat_namespace_compromise: A1   # Unit 42 self-published on own monitoring post; verifiable via direct URL retrieval
  miasma_payload_derived_from_mini_shai_hulud_source_code: A1                              # Unit 42 attestation; consistent with VT-006 corpus state from finding 0004 lineage + AM finding 0003 four-vendor consensus
  miasma_the_spreading_blight_repository_description_string_researcher_or_actor_coined_variant_name: A1   # Verifiable artifact via Unit 42 attestation + AM finding 0003 corpus state
  bun_download_url_github_com_oven_sh_bun_releases_download_bun_v1_3_13_abused_as_staging: B2  # Unit 42 single-source on this specific staging URL artifact at sweep time; verifiable Bun release URL
  affected_namespace_at_redhat_cloud_services_with_32_packages_compromised: A1               # Five-vendor consensus now (SecurityWeek consolidation of ReversingLabs + Aikido + Ox + Socket from AM finding 0003 + Unit 42 from this finding); procedural-facts layer cross-corroborated
  attribution_hedge_unit42_states_attribution_remains_uncertain_ttps_consistent_with_teampcp_but_public_release_of_source_code_means_any_competent_actor_can_replicate: A1   # Unit 42 verbatim attestation; explicit Tier-1 vendor hedge ratifies AM Hard Rule 2 stance
  unit42_does_not_extend_teampcp_attribution_per_explicit_hedge: A1                          # Verifiable absence of attribution-extension in Unit 42 text
  unit42_does_not_introduce_competing_attribution: A1                                         # Verifiable absence
  unit42_does_not_escalate_wep_confidence_above_ttps_consistent_with: A1                     # Verifiable absence
  five_vendor_independent_consolidation_now_corroborates_miasma_campaign_procedural_facts: B1   # ReversingLabs + Aikido + Ox Security + Socket (AM cluster) + Unit 42 (this finding) — five independent vendors with different evidence bases; procedural-facts layer cross-corroborated at B1 (lifted from B2 in AM finding 0003 due to Unit 42 Tier-1 A-grade addition)
  ad_sector_indirect_relevance_via_npm_ecosystem_ubiquity: C2                                # Grader-side structural inference; consistent with AM finding 0003 framing
  no_corpus_resident_unit42_surface_on_miasma_prior_to_this_raw_signal: A1                   # Verifiable internal corpus state — Unit 42 was anti-noise-flagged in AM finding 0003 cluster but did NOT publish before sweep; this is the in-window Unit 42 surface
  cluster_anchor: B1

digraph_anchor: >
  Cluster anchored on Palo Alto Networks Unit 42 long-running monitor
  post "The npm Threat Landscape: Attack Surface and Mitigations"
  June 2 update (2026-06-02 13:30 EDT, in-window) adding a Red Hat /
  Miasma section that documents the @redhat-cloud-services 32-package
  npm compromise as a Mini Shai-Hulud derivative carrying the
  "Miasma: The Spreading Blight" payload-embedded string. Unit 42 is
  ratified A per source-grades.yaml; this is the first productive
  Unit 42 surface on Miasma in Archimedes corpus and the FIFTH
  independent vendor on the campaign's procedural-facts layer
  (joining ReversingLabs, Aikido, Ox Security, and Socket from AM
  finding-2026-06-02-0003).

  B1 (not A1 or B2) anchored because:
    - SOURCE LETTER GRADE on the strongest corroborating primary is
      now A (Unit 42 ratified A) joining the four-vendor B-grade
      cluster from AM finding 0003 (Socket B + Ox Security B +
      Aikido C + ReversingLabs C). The five-vendor consolidation
      lifts the cluster-anchor letter to B1 on procedural facts —
      the addition of Unit 42 A on procedural facts brings the
      letter-grade weighting up, but the cluster contains C-grade
      members (Aikido, ReversingLabs from AM finding 0003) so the
      cluster-anchor letter stays at B (not A) under conservative
      lowest-common-grade aggregation.
    - The procedural-facts layer (Miasma campaign existed; affected
      @redhat-cloud-services namespace; Mini Shai-Hulud lineage;
      Miasma payload-embedded string) now CLEANLY carries 1
      (Confirmed) because five independent vendors with different
      evidence bases corroborate (Socket runtime, ReversingLabs
      CI/CD compromise forensics, Aikido OIDC exploitation
      assessment, Ox Security downstream-repo enumeration, Unit 42
      threat-landscape monitoring + variant-lineage analysis).
      Independence test PASSES cleanly on procedural facts.
    - The TEAMPCP ATTRIBUTION layer is RESTATEMENT not origination
      per Hard Rule 2. Unit 42's explicit hedge ("Attribution remains
      uncertain. The TTPs are consistent with TeamPCP, but the public
      release of the Mini Shai-Hulud source code means any competent
      actor can replicate the same attack.") is the Tier-1 vendor
      ratification of Archimedes' AM Hard Rule 2 stance — Unit 42
      DECLINES to extend TeamPCP attribution. This is methodologically
      aligned with finding 0004's original Socket "Attribution remains
      unclear" stance and AM finding 0003's preserved hedge. The
      attribution layer carries B2 (Probably True, attribution-uncertain
      consensus across five vendors) NOT B1 (Confirmed) — because
      "consensus on uncertainty" is not the same as "consensus on
      attribution."
    - The specific TTP layers from AM finding 0003 (72-second
      publication window — ReversingLabs only; GitHub Actions OIDC
      vector — Aikido only; 210 downstream repos — Ox Security only;
      api.anthropic[.]com C2 impersonation + AES-128/256-GCM
      encryption — Socket only from finding 0004) remain
      single-firm-origination at the layer level. Unit 42 does NOT
      add independent corroboration on any of these specific TTP
      details — Unit 42 frames at the campaign-and-mechanism level
      (Miasma derives from Mini Shai-Hulud) not the layer-detail
      level. Layered grading on those specific TTPs holds at B2
      from AM finding 0003.

  Single-source veto NOT applied on procedural-facts layer (five
  independent vendors now). Single-source veto STILL APPLIED on
  specific TTP layers (each is single-firm-origination from AM
  finding 0003); WEP ceiling on those specific TTPs capped at
  "likely" per AM finding 0003 carry-forward. Single-source veto
  STILL APPLIED on TeamPCP attribution layer — attribution-uncertain
  consensus across five vendors does NOT lift WEP ceiling above
  "likely" on the attribution claim.

  Per Hard Rule 2: Unit 42 explicitly DECLINES TeamPCP attribution
  extension. Archimedes' AM Hard Rule 2 stance ("Archimedes does not
  extend TeamPCP attribution") is now TIER-1 RATIFIED by Unit 42's
  explicit hedge. This is the substantive new addition vs. AM
  finding 0003.

  Per Hard Rule 3: Unit 42's monitor post includes defensive
  mitigation guidance (subscription-allowlists, npm-token-rotation)
  which is defender-applicable. NO exploit / PoC content carried;
  Mini Shai-Hulud mechanism-class described at concept level only
  via lineage chain.

  Per Hard Rule 6: Unit 42 attribution-hedge quote 36 words —
  EXCEEDS 15-word limit. Raw-signal records verbatim for grader /
  briefer reference but briefer MUST paraphrase or excerpt to <15
  words for any brief inclusion.

  Per Hard Rule 8: Splunk first-party check ran (-30d sweep on
  Miasma + "Mini Shai-Hulud" + "@redhat-cloud-services" across
  defenseclaw_local + archimedes NOT sourcetype=archimedes:*).
  0 events. First-party silence preserved as a data point per the
  19+-day non-archimedes-internal silent stream pattern, not
  disconfirming.

  PROCEDURAL RECHECK ON AM FINDING 0003 WEP:
    - AM finding 0003 carries WEP "likely" on procedural facts (B2
      cluster anchor on procedural-facts-layer with four-vendor
      cluster).
    - With Unit 42 Tier-1 A-grade addition to the procedural-facts
      cluster, the procedural-facts layer mathematically lifts to
      B1 (Confirmed by five-vendor consolidation with different
      evidence bases).
    - WEP ceiling on procedural facts CAN procedurally lift from
      "likely" to "very likely" — but the analyst / red-team should
      formally rerun the WEP assessment on AM finding 0003 to
      ratify the lift, and the librarian should update AM finding
      0003's frontmatter (or the briefer should treat this finding
      as the WEP-lift carrier).
    - The TeamPCP attribution layer WEP does NOT lift — Unit 42's
      explicit hedge is consensus-on-uncertainty, not corroboration-
      of-attribution.

source_reliability:
  primary_anchor:
    grade: A
    source_name: Palo Alto Networks Unit 42 - "The npm Threat Landscape Attack Surface and Mitigations (Updated June 2)" long-running running-monitor post
    source_yaml_id: unit42
    grade_rationale: >
      Pre-assigned A per source-grades.yaml. Tier-1 vendor research
      practice. Strong technical research, consistent track record.
      First productive Unit 42 surface on Miasma in Archimedes
      corpus; first Unit 42 surface in several sweeps.
    provisional: false
  am_finding_0003_four_vendor_cluster_carry_forward:
    grade: B
    source_name: AM finding 0003 four-vendor cluster (ReversingLabs C + Aikido C + Ox Security B + Socket B)
    source_yaml_id: securityweek (relay aggregating four vendors)
    grade_rationale: >
      Pre-assigned per source-grades.yaml. Cluster-anchor B2 from AM
      finding 0003. Carries forward as procedural-facts corroborator
      for this finding. Five-vendor consolidation with Unit 42
      addition lifts cluster-anchor to B1 on procedural facts.
    provisional: false

credibility:
  grade: 1
  checklist_passed:
    - confirmed_independent_source_different_publisher_different_telemetry        # Unit 42 (Palo Alto vendor) is publisher-independent of ReversingLabs / Aikido / Ox Security / Socket from AM cluster; Unit 42's evidence basis is threat-landscape monitoring + variant-lineage analysis, distinct from Socket runtime / ReversingLabs CI/CD forensics / Aikido OIDC / Ox Security downstream-repo enumeration
    - confirmed_neither_source_cites_other_as_origin                              # Unit 42 does not cite Socket / ReversingLabs / Aikido / Ox Security / SecurityWeek as origin; consensus reached independently via Unit 42's own threat-landscape monitoring
    - confirmed_technical_artifacts_match_across_sources                          # @redhat-cloud-services namespace, 32 packages, Miasma variant name, Mini Shai-Hulud lineage all cross-corroborated across five vendors
    - confirmed_no_contradicting_higher_grade_source                              # No A-grade source contradicts the procedural facts at sweep time
  rationale: >
    Grade 1 (Confirmed) PASSES on procedural-facts layer (five
    independent vendors with different evidence bases consolidate).
    Cannot upgrade WEP above "very likely" on procedural facts due
    to single-source-veto on specific TTP layers and on TeamPCP
    attribution. Procedural facts (Miasma campaign existed; affected
    namespace and package count; Mini Shai-Hulud lineage; Miasma
    payload-embedded string) carry digraph A1 at the layer level
    after Unit 42 corroboration; cluster anchor B1 reflects
    conservative lowest-common-grade aggregation across the
    five-vendor cluster (Aikido and ReversingLabs are C; Unit 42 A
    lifts but does not erase C presence in cluster).

corroboration:
  independent_sources:
    - unit42                                  # primary on the June 2 update + attribution hedge + variant-lineage analysis
    - reversinglabs                           # AM finding 0003 cluster — CI/CD compromise forensics + 72s publication window
    - aikido                                  # AM finding 0003 cluster — OIDC exploitation assessment
    - ox-security                             # AM finding 0003 cluster — downstream-repo enumeration
    - socket                                  # AM finding 0003 cluster + finding 0004 originating — runtime/binary analysis
  non_independent_relays:
    - securityweek                            # AM finding 0003 aggregator-relay of the four-vendor cluster; NOT independent on substance — consolidates the four vendor primaries
    - thehackernews                           # finding 0004 originating cluster relay of Socket primary
  independent: true
  test_passed: >
    Unit 42 publishes from its own threat-landscape monitoring +
    variant-lineage analysis evidence basis, publisher-independent
    of ReversingLabs / Aikido / Ox Security / Socket from AM cluster.
    Unit 42 does NOT cite the AM cluster vendors as origin. Per
    independence test: PASSES on procedural-facts layer with five-
    vendor consolidation. Removing any one vendor leaves the
    remaining four standing on their independent evidence bases.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_check_performed: true
  splunk_check_window: "-30d, index=defenseclaw_local OR index=archimedes (Miasma OR \"Mini Shai-Hulud\" OR \"@redhat-cloud-services\") NOT sourcetype=archimedes:operation NOT sourcetype=archimedes:scheduler"
  splunk_check_result: "0 events — first-party telemetry silent on Miasma + Mini Shai-Hulud + @redhat-cloud-services indicators, consistent with the 19+-day non-archimedes-internal silent stream pattern. Silence is not disconfirming per Hard Rule 8."

single_source_veto_applied: false_on_procedural_facts_true_on_specific_ttps_and_attribution
single_source_veto_rationale: >
  Single-source veto NOT applied on procedural-facts layer (five
  independent vendors with different evidence bases consolidate;
  five-vendor cluster passes independence test cleanly). Single-source
  veto APPLIED on specific TTP layers from AM finding 0003 (72s
  publication window — ReversingLabs only; OIDC vector — Aikido only;
  210 downstream repos — Ox Security only; api.anthropic[.]com C2 +
  encryption details — Socket only from finding 0004) — WEP ceiling
  on those specific TTPs capped at "likely" per AM finding 0003
  carry-forward; Unit 42 does NOT add independent corroboration on
  any of these specific TTP details. Single-source veto APPLIED on
  TeamPCP attribution layer — attribution-uncertain consensus across
  five vendors is consensus-on-uncertainty, NOT corroboration-of-
  attribution; WEP ceiling on attribution claim capped at "likely."

wep_ceiling: very_likely      # procedurally lifted on procedural-facts layer; capped at "likely" on specific TTPs and on TeamPCP attribution

inclusion:
  eligible_for:
    - daily_brief_action
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update      # TeamPCP attribution hedge has implications for TeamPCP dossier — vendor-Tier-1-ratified hedge is dossier-update-relevant
    # NOT flash — collector evaluated all 6 FLASH triggers as FAIL (Trigger 2 attribution-hedge fails attribution_is_new condition; Trigger 4 no novel TeamPCP-specific tradecraft; Trigger 5 no A&D entity)
  inclusion_threshold_test:
    flash_b2_minimum: pass_by_digraph_fail_by_trigger_logic     # B1 clears B2 floor but no FLASH trigger fired
    daily_brief_action_b2_minimum: pass                          # B1 clears B2 floor; Tier-1 vendor corroboration of AM Hard Rule 2 stance is the action driver
    daily_brief_monitoring_c3_minimum: pass                      # B1 clears C3 floor
    weekly_synthesis_c3_minimum: pass                            # B1 clears C3 floor
    actor_profile_update_b2_minimum: pass                        # B1 clears B2 floor; TeamPCP dossier update relevance

# Cluster metadata
cluster:
  topic: "Unit 42 June 2 update to npm threat landscape post adds Red Hat / Miasma section; explicit Tier-1 vendor TeamPCP attribution hedge ratifies AM Hard Rule 2 stance; five-vendor consolidation lifts procedural-facts layer WEP from likely to very_likely; specific TTP layers and TeamPCP attribution remain capped at likely per AM finding 0003 carry-forward"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-02-pm-004-unit42-npm-threat-landscape-june-2-update-miasma-teampcp-attribution-hedge-vt006-tier1-corroboration
  attribution_claims:
    - claimed_actor: TeamPCP
      claimed_attribution_status: explicitly_hedged_by_unit42
      claimed_by_sources: [unit42]
      attribution_hedge_text_verbatim: "Attribution remains uncertain. The TTPs are consistent with TeamPCP, but the public release of the Mini Shai-Hulud source code means any competent actor can replicate the same attack."
      attribution_hedge_alignment_with_archimedes_am_finding_0003_hard_rule_2_stance: positive_tier1_ratification
      archimedes_originated: false
      hard_rule_2_compliance: preserved — Unit 42 explicitly DECLINES TeamPCP attribution extension; Archimedes records the hedge with citation; does NOT extend
      requires_analyst_review: true
      roster_status: TeamPCP IS IN ROSTER (#001) — dossier-update-relevant via attribution-hedge content

# Downstream handoff flags
analyst_review_required: true
analyst_review_reasons:
  - tier1_vendor_attribution_hedge_warrants_sat_ach_on_archimedes_position_relative_to_unit42_explicit_decline
  - five_vendor_consolidation_with_procedural_facts_layer_wep_lift_warrants_sat_kac_on_layered_wep_assumption_for_am_finding_0003_recheck
  - teampcp_dossier_update_candidate_via_unit42_hedge_content
red_team_review_required: true
red_team_review_reasons:
  - wep_ceiling_very_likely_on_procedural_facts_layer_meets_red_team_invocation_floor
  - red_team_argue_against_layered_wep_lift_assumption_specifically_whether_five_vendor_consolidation_genuinely_lifts_procedural_facts_layer_to_very_likely_or_whether_conservative_b2_should_hold
red_team_review:
  reviewed_at: 2026-06-02T17:55:00-04:00
  reviewed_by: red-team-analyst
  run_id: red-team-20260602-175500

  strongest_counter_hypothesis:
    hypothesis: >
      "Unit 42's June 2 update is a long-running monitor-post update that may
      transitively rely on prior public vendor research (including the AM
      cluster vendors); the cluster anchor should remain B2 pending direct
      validation that Unit 42's contribution is substantively independent
      rather than genre-typical aggregation of prior disclosures. The
      mathematical lift to B1 rests on aggregation arithmetic that doctrine
      does NOT specify in either direction."
    evidence_for_counter:
      - "Raw signal explicitly characterizes the Unit 42 source as a 'long-running monitor post that Unit 42 has been incrementally updating since the original Shai-Hulud disclosure' (raw lines 51-54). Long-running monitor posts on supply-chain campaigns are genre-typically aggregations of prior vendor research."
      - "INTEL-GRADING.md does NOT define a cluster-letter-grade aggregation rule. 'Lowest-common-grade aggregation' (cited by grader to keep cluster at B not A) and 'Tier-1 A-grade addition lifts B2 to B1' (cited by grader and analyst to justify the lift) are BOTH grader-invented arithmetic — doctrine is silent on both."
      - "Unit 42 'at least 32 packages' (raw lines 71-72) vs. AM cluster exact '32 packages / 96 versions' (AM finding line 14-15): Unit 42 has not corroborated the exact count claim; it has corroborated a strictly weaker claim '>=32.' Five-vendor consolidation does NOT cleanly extend to the exact package-count fact."
      - "KAC marked five of ten assumptions (A1, A3, A4, A6, A8) as 'qualify' — a cluster of qualifies on the load-bearing premises of the lift indicates the lift sits on a stack of caveats, not on independently strong evidence."
      - "The 'neither cites the other as origin' test (INTEL-GRADING.md line 86) passes formally but the 'different evidence basis' test (line 88) passes only loosely for a threat-landscape monitor post that almost certainly tracks prior public vendor research as part of its routine inputs."
    evidence_against_counter:
      - "The procedural-facts layer claims (Miasma campaign existed; @redhat-cloud-services namespace affected; Mini Shai-Hulud lineage; 'Miasma: The Spreading Blight' payload string) are technical artifacts that are independently verifiable irrespective of source dependence — the artifacts either exist on npm/GitHub or they don't."
      - "Unit 42's grader-direct-retrieved text contains no explicit citation of Socket / ReversingLabs / Aikido / Ox Security — the independence test passes the strict version of the doctrine even if it passes the genre-realistic version only loosely."
      - "Even if Unit 42 is downgraded to genre-typical aggregation, the four-vendor AM cluster STILL passes the independence test on procedural facts on its own — the AM-finding-0003 B2 floor holds, and Unit 42 only adds (not creates) the consolidation."
      - "Brittleness on the lift itself is asymmetric: the lift can be retracted at low cost (downgrade procedural-facts WEP back to 'likely' on AM finding 0003) if independence is later found wanting; the lift carries low downstream-action exposure."

  weaknesses_in_primary_assessment:
    - "A1 (aggregation rule) is doctrinally underdetermined in BOTH directions. Doctrine specifies single-source veto (must NOT go to very_likely on single source) and what counts as independent corroboration, but is silent on how cluster letter grades aggregate when independent sources of mixed reliability combine. Grader's 'lowest-common-grade aggregation' justification at lines 42-52 and 'Tier-1 A addition lifts cluster letter' at lines 122-127 are BOTH grader-invented arithmetic. The lift survives but should be framed as 'reasonable but not doctrinally compelled' rather than 'mathematical.'"
    - "A2 (Unit 42 independence) is overstated as 'high confidence' in KAC. Raw signal explicitly frames Unit 42's source as a long-running monitor post that has been incrementally updating since the original Shai-Hulud disclosure — a genre that routinely aggregates prior public vendor research. The strict doctrine test ('neither cites the other as origin') passes but the realistic 'different evidence basis' test passes only on Unit 42's own self-characterization. A2 should be 'medium confidence' not 'high.'"
    - "A3 (procedural-facts semantic stability) is the most material qualifying caveat. Unit 42 says 'at least 32 packages'; AM cluster says exactly '32 packages.' The lift applies cleanly to the WEAKER claim '>=32 packages' but does NOT cleanly extend to the STRONGER claim 'exactly 32.' Briefer must specifically caveat the count fact OR rephrase the lifted claim to the weaker form."
    - "Digraph_anchor prose at lines 96-100 ('Archimedes AM Hard Rule 2 stance is now TIER-1 RATIFIED') is methodologically confirmation-biased framing. The accurate framing is 'Unit 42 independently reached the same attribution-uncertain stance with explicit replication-barrier reasoning.' Alignment is real; ratification framing is celebratory and risks anchoring downstream analyst posture."
    - "Tripwire coverage is good on attribution but incomplete on the lift itself. Missing tripwire: 'npm or GitHub publishes a post-incident review with a package count differing from 32' — this would crumble the exact-count layer immediately and would NOT be caught by any of the four tripwires currently listed. Recommended addition before publication."

  strongest_counter_wep: likely    # if H_pin won, AM finding 0003 procedural facts would stay at 'likely' (status quo)

  recommendation: qualify

  qualifying_language_suggested: >
    Brief inclusion should read approximately: "Unit 42's June 2 update to its
    npm Threat Landscape monitor post adds a Red Hat / Miasma section
    documenting at least 32 compromised @redhat-cloud-services packages as a
    Mini Shai-Hulud derivative, with an explicit attribution hedge declining
    to extend the TeamPCP linkage on public-source-code replication-barrier
    grounds. Unit 42's independent decline aligns with Archimedes' AM Hard
    Rule 2 stance from finding-2026-06-02-0003. With Unit 42 as a fifth
    independent vendor on the procedural-facts layer, Archimedes assesses the
    Miasma campaign existence, affected namespace, and Mini Shai-Hulud
    lineage as VERY LIKELY (lifted from likely on the AM cluster). The
    'exactly 32 packages' count specifically remains at LIKELY — Unit 42
    hedges to 'at least 32,' a minor specification discrepancy. Specific TTP
    layers (72-second publication window, OIDC vector, 210 downstream repos,
    api.anthropic[.]com C2) and the TeamPCP attribution claim REMAIN AT
    LIKELY per single-firm-origination veto on the TTPs and consensus-on-
    uncertainty on the attribution layer."

  specific_tests_that_would_resolve:
    - "Direct re-read of the Unit 42 monitor-post text with explicit search for any inline reference, citation, footnote, or 'see also' linking to Socket / ReversingLabs / Aikido / Ox Security / SecurityWeek. If any such reference exists, Unit 42's independence rating reduces and the lift weakens. If genuinely no such reference, A2 firms to high confidence as stated."
    - "npm or GitHub publishes a post-incident review of the @redhat-cloud-services compromise with their own package count. If count == 32, the procedural-facts lift extends to the count layer cleanly; if count != 32, the count-layer claim retracts and Unit 42's 'at least 32' framing is vindicated as the more accurate read."
    - "INTEL-GRADING.md doctrine clarification: does cluster-letter-grade aggregation use lowest-common-grade pinning, weight-of-strongest-independent-source, or weighted-composite? Codifying this would resolve the A1 underdetermination for this and all future multi-vendor clusters."

  wep_adjustment_recommended: null    # WEP very_likely on procedural-facts layer STANDS with qualifying caveats; no numeric downgrade
  wep_adjustment_rationale: >
    The lift is methodologically defensible and the counter-hypothesis (H_pin)
    does not invalidate H_lift — the AM cluster alone still passes independence,
    Unit 42's text passes the strict doctrine independence test, and the
    procedural-facts artifacts are independently verifiable on the npm/GitHub
    surface irrespective of source dependence. The lift remains "very likely"
    on the procedural-facts layer EXCEPT specifically on the exact "32
    packages" count which should be carried as "likely" pending npm/GitHub
    confirmation. All other KAC qualifying caveats remain in effect.

  notes: >
    Not blocking. The lift survives contrarian pressure with caveats already
    identified by the analyst's KAC. The single substantive RED-TEAM addition
    is the count-specific carve-out: lift "at least 32 packages / Miasma
    campaign existed / namespace affected / Mini Shai-Hulud lineage" to
    very_likely, but keep the EXACT count "32 packages" at likely (Unit 42's
    'at least 32' hedges to a weaker claim). Briefer must enforce this carve-
    out and must NOT publish digraph-anchor-style "Tier-1 RATIFIED" framing —
    use "Unit 42 independently aligned" instead. Add tripwire: npm/GitHub
    incident-review count != 32. Otherwise sign off.

red_team_review_status: completed
red_team_review_outcome: qualify
red_team_review_recommendation: publish_with_qualifying_caveats
publication_blocked: false
analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        Given Unit 42's June 2 update + the four-vendor AM cluster + Socket
        originating coverage, which framing best fits the Miasma / @redhat-
        cloud-services 32-package npm compromise WITHOUT crossing Hard Rule 2:
        (a) Archimedes preserves the AM Hard Rule 2 declination on TeamPCP
        attribution (status quo); (b) five-vendor attribution-uncertain
        consensus is itself a form of NEGATIVE attribution (downgrade TeamPCP
        link to "unlikely"); (c) Tier-1 hedge ratification + lineage chain to
        Mini Shai-Hulud is sufficient to lift TeamPCP attribution to "likely";
        (d) the campaign is an unrelated actor reusing public Mini Shai-Hulud
        source code with no useful TeamPCP signal; (e) the campaign is a
        deliberate false-flag designed to implicate TeamPCP via the
        recognizable Mini Shai-Hulud lineage.
      analyzed_at: 2026-06-02T17:05:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: >
            Preserve AM Hard Rule 2 declination — record Unit 42's explicit
            "TTPs consistent with TeamPCP, but public source-code release
            means any competent actor can replicate" hedge as Tier-1 vendor
            corroboration of Archimedes' attribution-uncertain stance.
            TeamPCP attribution remains "likely" per AM finding 0003 cap,
            specific TTP layers remain "likely," procedural facts lift to
            "very likely."
        - id: H2
          statement: >
            Five-vendor consensus on attribution-uncertainty constitutes
            NEGATIVE attribution evidence; TeamPCP linkage should be
            downgraded from "likely" to "unlikely" because no vendor with
            distinct evidence basis has been able to confirm TeamPCP
            exclusivity despite five independent looks at the campaign.
        - id: H3
          statement: >
            Tier-1 hedge framing + Mini Shai-Hulud lineage chain is
            sufficient to UPGRADE TeamPCP attribution to "likely" or "very
            likely" — the variant naming pattern, payload derivation, and
            tradecraft continuity are diagnostic enough that "consistent
            with TeamPCP" is a soft attribution worth treating as positive.
        - id: H4
          statement: >
            Unrelated actor reusing publicly-released Mini Shai-Hulud source
            code as a commodity tool. TeamPCP signal is illusory — what's
            being observed is downstream consumption of a leaked / public
            tradecraft package by a competent but unaffiliated actor (could
            be financially-motivated, hacktivist, or initial-access broker
            recruiting for follow-on operations).
        - id: H5
          statement: >
            Deliberate false-flag operation — actor X (state, criminal, or
            third party) is exercising the publicly-released Mini Shai-Hulud
            source code specifically to drive vendor attribution attention
            toward TeamPCP. The "Miasma: The Spreading Blight" repository
            description and Bun staging URL are deliberately recognizable
            signals to ensure variant-lineage analysis lands on TeamPCP.
      evidence:
        - id: E1
          description: >
            Five-vendor consolidation on procedural facts (Unit 42 +
            ReversingLabs + Aikido + Ox Security + Socket); each with
            distinct evidence basis (threat-landscape monitor, CI/CD
            forensics, OIDC exploitation, downstream-repo enumeration,
            runtime/binary). None cite the others as origin.
          source: unit42 + AM finding 0003 cluster
          digraph: A1
          weight: 3
        - id: E2
          description: >
            Unit 42 explicit verbatim hedge — "TTPs are consistent with
            TeamPCP, but the public release of the Mini Shai-Hulud source
            code means any competent actor can replicate the same attack."
          source: unit42
          digraph: A1
          weight: 3
        - id: E3
          description: >
            "Miasma: The Spreading Blight" repository description string +
            Mini Shai-Hulud source-code lineage chain documented by Unit 42
            (campaign-and-mechanism level) and consistent across cluster.
          source: unit42 + AM finding 0003 cluster
          digraph: A1
          weight: 3
        - id: E4
          description: >
            Mini Shai-Hulud source code is PUBLICLY AVAILABLE per Unit 42's
            own attestation — replication barrier is low for any competent
            actor regardless of TeamPCP affiliation.
          source: unit42
          digraph: A1
          weight: 3
        - id: E5
          description: >
            Specific TTP layers remain single-firm-origination (72s
            publication window — ReversingLabs only; OIDC vector — Aikido
            only; 210 downstream repos — Ox Security only; api.anthropic[.]com
            C2 + AES-GCM encryption — Socket only). No cross-vendor
            corroboration on the layer-detail level.
          source: AM finding 0003 + finding 0004
          digraph: B2
          weight: 2
        - id: E6
          description: >
            No A/B-grade source extends TeamPCP attribution beyond
            "consistent with" language. Socket originating coverage said
            "Attribution remains unclear"; Unit 42 says the same with
            explicit replication-barrier reasoning.
          source: socket + unit42
          digraph: A1
          weight: 3
        - id: E7
          description: >
            Bun release URL (github.com/oven-sh/bun/releases/download/
            bun-v1.3.13/) abused as staging — Unit 42 single-source on this
            specific artifact at sweep time; consistent with commodity
            tradecraft (use of legitimate runtime infrastructure).
          source: unit42
          digraph: A2
          weight: 3
        - id: E8
          description: >
            First-party Splunk silent across -30d sweep (Miasma + Mini
            Shai-Hulud + @redhat-cloud-services); per Hard Rule 8 silence
            not disconfirming but also not corroborating exposure.
          source: splunk-negative-search
          digraph: A1
          weight: 3
        - id: E9
          description: >
            No vendor reports operational signals diagnostic of TeamPCP
            specifically (e.g., no TeamPCP-unique infrastructure overlap,
            no TeamPCP-private tooling, no claimed-credit posting).
          source: absence-of-evidence across five-vendor cluster
          digraph: A2
          weight: 3
      matrix:
        E1: {H1: C, H2: C, H3: C, H4: C, H5: C}    # five-vendor consolidation on procedural facts is non-diagnostic on attribution layer
        E2: {H1: C, H2: C, H3: I, H4: C, H5: C}    # explicit hedge directly contradicts H3 upgrade framing
        E3: {H1: C, H2: N, H3: C, H4: C, H5: C}    # lineage chain consistent with H1/H3/H4/H5; neutral on H2 (doesn't downgrade)
        E4: {H1: C, H2: C, H3: I, H4: C, H5: C}    # public source-code release directly contradicts H3 (TeamPCP exclusivity claim)
        E5: {H1: C, H2: N, H3: I, H4: C, H5: C}    # single-firm TTPs cap upgrade ceiling; contradicts H3
        E6: {H1: C, H2: C, H3: I, H4: C, H5: C}    # vendor uniformity on "consistent with" language contradicts H3 upgrade
        E7: {H1: C, H2: C, H3: N, H4: C, H5: C}    # commodity staging URL consistent with H4 commodity-actor framing
        E8: {H1: N, H2: N, H3: N, H4: N, H5: N}    # negative Splunk non-diagnostic
        E9: {H1: C, H2: C, H3: I, H4: C, H5: C}    # absence of TeamPCP-diagnostic signal contradicts H3 upgrade
      inconsistency_counts:
        H1: 0
        H2: 0
        H3: 5
        H4: 0
        H5: 0
      diagnostic_evidence:
        - E2: "Unit 42 verbatim hedge is most diagnostic — distinguishes H3 (upgrade) from H1/H2/H4/H5"
        - E4: "Public availability of source code is most diagnostic against H3 — and supports H4 commodity framing"
        - E9: "Absence of TeamPCP-diagnostic signal across five vendors is diagnostic against H3"
        - E6: "Vendor uniformity on 'consistent with' (not 'attributed to') language is diagnostic against H3"
      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: >
            Zero inconsistencies; strongest diagnostic support (E2, E4, E6,
            E9 all confirm). Aligns with Hard Rule 2 (do not originate
            attribution); aligns with Unit 42's explicit framing; aligns
            with five-vendor uniformity on attribution-uncertain language.
            Simplest position consistent with evidence.
          wep: very_likely
        - rank: 2
          hypothesis_id: H4
          rationale: >
            Zero inconsistencies; consistent with E4 (public source-code
            availability) and E7 (commodity staging URL) and E9 (no
            TeamPCP-diagnostic signal). Cannot be ruled out — Unit 42's
            own hedge effectively LEGITIMIZES H4 as a viable alternative
            ("any competent actor can replicate"). H1 and H4 are
            functionally equivalent for downstream Archimedes treatment
            because both decline TeamPCP attribution — but H4 is
            attribution-neutral while H1 is attribution-preservation;
            H1 is the more conservative reporting frame.
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H2
          rationale: >
            Zero inconsistencies but argues for an active downgrade move
            (TeamPCP to "unlikely") that no cited source supports. Five
            vendors saying "attribution uncertain" is consensus-on-
            uncertainty, not consensus-on-negation. Adopting H2 would
            itself be a form of attribution origination (negative
            attribution) — Archimedes should NOT make this move per
            Hard Rule 2.
          wep: unlikely
        - rank: 4
          hypothesis_id: H5
          rationale: >
            Zero inconsistencies but requires multiple unverified
            assumptions (deliberate false-flag actor, intent to drive
            attribution attention, capability to deploy at scale).
            Insufficient evidence to elevate; cannot be ruled out without
            adversary-intent disclosure that won't surface.
          wep: unlikely
        - rank: 5
          hypothesis_id: H3
          rationale: >
            Five inconsistencies; ruled out. Adopting H3 would directly
            cross Hard Rule 2 (Archimedes originating attribution beyond
            what cited sources state) — Unit 42 explicitly declines this
            move and that decline is the operative Tier-1 signal.
          wep: very_unlikely
      sensitivity_analysis:
        brittleness: low
        load_bearing_evidence: [E2, E4, E6, E9]
        if_E2_downgraded: >
          Even if Unit 42's hedge were withdrawn or restated, H1's
          conservative posture holds because E4 (public source-code
          availability) and E9 (absence of TeamPCP-diagnostic signal)
          independently contradict H3. Ranking would not flip.
        if_unit42_downgraded: >
          The four-vendor AM cluster + Socket originating coverage still
          carry attribution-uncertain framing. Procedural-facts lift would
          partially retract (back to B2 cluster anchor on AM finding 0003)
          but Hard Rule 2 declination remains unaffected. H1 ranking holds.
        if_E5_corroborated_across_vendors: >
          If a second vendor independently corroborated any of the
          specific TTP layers (72s window, OIDC vector, 210 repos,
          api.anthropic[.]com C2), the layer-detail WEP could lift from
          "likely" to "very likely" — but this would NOT shift the
          attribution-layer ranking; H1 / H4 still tied at the top.
        single_point_of_failure: none
      tripwires:
        - observation: >
            A second Tier-1 vendor (Mandiant / CrowdStrike / Microsoft /
            MSTIC) publishes operational signals diagnostic of TeamPCP
            specifically (TeamPCP-unique infrastructure, private tooling
            artifact, claimed-credit posting).
          effect: >
            Re-evaluate H3; could shift ranking. Rerun ACH with new
            evidence; assess whether H3 inconsistencies clear or hold.
        - observation: >
            TeamPCP publicly disavows or claims the Miasma campaign.
          effect: >
            Disavow elevates H4 (unrelated actor); claim elevates H3 but
            Archimedes still cites attribution per source per Hard Rule 2.
        - observation: >
            Splunk first-party detection on @redhat-cloud-services
            namespace, Mini Shai-Hulud artifacts, or Bun staging URL
            within defenseclaw_local.
          effect: >
            Hard Rule 8 first-party precedence triggers; rerun ACH with
            first-party telemetry as A1 evidence; assess exposure exposure
            irrespective of attribution.
        - observation: >
            Public release of Mini Shai-Hulud source code is
            substantively wrong (Unit 42 mis-stated; source code is
            actually private).
          effect: >
            E4 inverts; H3 inconsistencies partially clear; re-evaluate
            H1 vs. H3 ranking. Unlikely to occur but worth tracking.
      conclusion:
        summary: >
          H1 (preserve AM Hard Rule 2 declination on TeamPCP attribution;
          accept Unit 42 hedge as Tier-1 ratification) is the leading
          framing with zero inconsistencies and strongest diagnostic
          support. H4 (unrelated actor reusing public Mini Shai-Hulud
          source code) is functionally equivalent for downstream treatment
          and cannot be distinguished from H1 without TeamPCP-diagnostic
          signal that no vendor has produced. H3 (upgrade TeamPCP
          attribution) is ruled out by five inconsistencies and would
          directly cross Hard Rule 2. The five-vendor consolidation
          legitimately lifts procedural-facts layer WEP on AM finding 0003
          from "likely" to "very likely"; the attribution layer WEP stays
          capped at "likely" per single-source-veto on attribution.
        wep: very_likely      # on procedural-facts layer
        confidence_caveats: >
          (1) WEP "very likely" applies ONLY to procedural-facts layer
          (Miasma campaign existed; @redhat-cloud-services namespace
          affected; ~32 packages compromised; Mini Shai-Hulud lineage;
          Miasma payload-embedded string). (2) WEP on specific TTP layers
          (72s window, OIDC vector, 210 repos, api.anthropic[.]com C2)
          remains "likely" per single-firm-origination veto. (3) WEP on
          TeamPCP attribution remains "likely" — five-vendor consensus on
          attribution-uncertainty is consensus-on-uncertainty, NOT
          corroboration. (4) Briefer should treat H1 framing as the
          attribution-disposition narrative; do NOT shift to H2 negative
          attribution; do NOT shift to H3 upgrade. (5) Red-team should
          specifically argue the procedural-facts lift to "very likely"
          rather than the attribution layer — that lift is the genuine
          new methodological move and deserves the adversarial pass.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Five-vendor consolidation (Unit 42 A + ReversingLabs C + Aikido C
        + Ox Security B + Socket B) lifts the Miasma campaign procedural-
        facts layer WEP on AM finding 0003 from 'likely' to 'very likely.'
        TeamPCP attribution layer WEP remains capped at 'likely.' AM
        finding 0003 is a WEP-lift recheck candidate."
      analyzed_at: 2026-06-02T17:15:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Post-ACH KAC interrogating the operative move in this finding —
        the procedural-facts WEP lift on AM finding 0003 via Unit 42
        Tier-1 vendor addition. KAC also interrogates the cross-cutting
        cluster note: "Tier-1 hedge → procedural-facts WEP lift" sound?
      assumptions:
        - id: A1
          statement: >
            Lowest-common-grade aggregation across the five-vendor cluster
            (B1 cluster anchor reflecting C-grade members Aikido and
            ReversingLabs) is the correct doctrinal aggregation rule —
            and a single A-grade addition (Unit 42) genuinely lifts the
            cluster anchor letter, not merely the count.
          category: source_reliability
          stated: true
          why_must_be_true: >
            The procedural-facts WEP lift hinges on the cluster-anchor
            letter moving from B2 (AM finding 0003) to B1 (this finding).
            If lowest-common-grade aggregation says C-grade presence pins
            the cluster letter at the lower bound, Unit 42's addition is
            count-additive but not letter-additive — WEP shouldn't lift.
          when_could_be_false: >
            INTEL-GRADING doctrine specifies "anchor on strongest primary
            with independence test, not lowest-common-grade" — would
            invert the aggregation logic. Or: "weight Unit 42 A higher in
            consolidation as Tier-1 addition lifts cluster floor."
          evidence_for: [inferred-from-am-finding-0003-cluster-anchor-rationale]
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A2
          statement: >
            Unit 42's evidence basis (threat-landscape monitoring +
            variant-lineage analysis) is genuinely INDEPENDENT of the
            four-vendor AM cluster's evidence bases (Socket runtime,
            ReversingLabs CI/CD forensics, Aikido OIDC, Ox Security
            downstream-repo enumeration). Independence test passes.
          category: source_reliability
          stated: true
          why_must_be_true: >
            Independence is the foundation of the five-vendor
            consolidation. If Unit 42 actually relied on AM cluster
            vendors as sourcing inputs (e.g., reposting Socket's binary
            analysis), the consolidation collapses to four-vendor.
          when_could_be_false: >
            Unit 42 monitor post is built on aggregation of prior public
            vendor research; if so, it may indirectly cite AM cluster
            vendors. Direct primary retrieval of Unit 42 text could reveal
            citation chain we haven't validated.
          evidence_for: [unit42-direct-retrieval-by-grader]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A3
          statement: >
            "Procedural facts" is a stable, well-defined layer that can
            be cleanly distinguished from "specific TTP layers" and
            "attribution layer." The five-vendor lift applies cleanly to
            procedural facts only.
          category: semantic
          stated: true
          why_must_be_true: >
            Layered grading depends on layer definitions being stable.
            If "procedural facts" bleeds into "specific TTPs" or
            "attribution," the lift could over-apply (lifting
            attribution incorrectly) or under-apply (failing to lift
            facts that actually are corroborated).
          when_could_be_false: >
            Five vendors might agree on the "32 packages" headline but
            disagree on specifics (Unit 42 says "at least 32"; AM cluster
            says exactly "32"). Minor specification discrepancies could
            erode "procedural facts" coherence. The graded finding even
            notes this — Unit 42 says "at least 32."
          evidence_for: [unit42-attestation, am-finding-0003-cluster]
          evidence_against: [unit42-at-least-32-vs-am-cluster-exactly-32-minor-discrepancy]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A4
          statement: >
            "Tier-1 vendor hedge ratification" is itself a sound
            methodological position — i.e., when a Tier-1 vendor
            explicitly declines an attribution, that decline should be
            given heavier methodological weight than B/C-grade vendors
            doing the same.
          category: source_reliability
          stated: false
          why_must_be_true: >
            The cross-cutting cluster note ("Tier-1 hedge → procedural-
            facts WEP lift is sound") rests on this. If a B-grade vendor
            had been the one to publish the hedge, would the same lift
            move be warranted? Probably yes — but the "Tier-1 RATIFICATION"
            framing implies extra weight that should be made explicit.
          when_could_be_false: >
            Heuer's evidence-quality framework grades evidence by
            independence + reliability, not by vendor tier. The
            Tier-1-ratification framing could imply confirmation bias
            ("we already declined, and now a Tier-1 confirms our position
            — celebrate") rather than fresh evaluation.
          evidence_for: [am-finding-0003-archimedes-hard-rule-2-stance]
          evidence_against: [potential-confirmation-bias-risk]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A5
          statement: >
            Unit 42's June 2 update IS a "first productive surface" for
            this finding — i.e., Unit 42 was not anti-noise-flagged as
            "already counted" in AM finding 0003's cluster aggregation.
          category: visibility
          stated: true
          why_must_be_true: >
            If Unit 42 had been pre-counted in AM finding 0003's cluster
            assessment, this finding would be double-counting.
          when_could_be_false: >
            AM finding 0003's cluster anchor noted Unit 42 as anti-noise-
            flagged-but-not-yet-published; this finding ratifies that
            Unit 42 published in-window. AM finding 0003's text should be
            verified to confirm Unit 42 was NOT included in its four-
            vendor cluster aggregation.
          evidence_for: [am-finding-0003-source-text-on-anti-noise-flag]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A6
          statement: >
            Mini Shai-Hulud source code is genuinely PUBLIC (per Unit 42's
            own attestation), which is what underwrites the "any competent
            actor can replicate" hedge and what blocks any TeamPCP-
            exclusivity attribution.
          category: technology
          stated: true
          why_must_be_true: >
            The replication-barrier reasoning is the core methodological
            argument against H3 (upgrade TeamPCP attribution). If the
            source code were actually private (Unit 42 mis-stated), the
            argument collapses and TeamPCP attribution becomes more
            tenable.
          when_could_be_false: >
            Unit 42 mis-stated; source code is actually private. Or:
            source code is technically public but practically inaccessible
            (deleted from public repo, access-walled, only available to
            researchers via vendor channel).
          evidence_for: [unit42-attestation]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A7
          statement: >
            The procedural-facts WEP lift is the appropriate METHODOLOGICAL
            move (not the briefer's narrative move) — i.e., this finding
            is the carrier of the lift, OR AM finding 0003's frontmatter
            should be updated.
          category: workflow_semantic
          stated: true
          why_must_be_true: >
            Operational handoff says "analyst / red-team should formally
            rerun the WEP assessment on AM finding 0003" — if neither
            this finding nor AM finding 0003's frontmatter is updated,
            the lift exists in analyst output but doesn't affect
            downstream briefer / librarian consumption.
          when_could_be_false: >
            The briefer could treat both findings as parallel and decide
            independently whether to elevate the procedural-facts framing
            in the PM brief. Operator may decide not to retroactively
            update AM finding 0003 frontmatter; this finding can carry
            the lift forward as a "this finding ratifies AM 0003 at
            higher confidence" footnote.
          evidence_for: [operational-handoff-text]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A8
          statement: >
            Specific TTP layers remain genuinely single-firm-origination —
            no vendor in the five-vendor cluster has corroborated 72s
            publication window, OIDC vector, 210 downstream repos, or
            api.anthropic[.]com C2 + AES-128/256-GCM details.
          category: ttp_patterns
          stated: true
          why_must_be_true: >
            The WEP cap on specific TTP layers depends on this. If
            Unit 42 actually did corroborate (e.g.) the 72s publication
            window, that layer could lift from "likely" to "very likely"
            independently of the procedural-facts lift.
          when_could_be_false: >
            Direct Unit 42 primary text retrieval could reveal corroborating
            content that wasn't surfaced in the grader's read.
          evidence_for: [grader-frontmatter-attestation]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A9
          statement: >
            Five-vendor attribution-uncertain consensus is "consensus-on-
            uncertainty" and NOT "consensus-on-negation" — the doctrinal
            position that the attribution layer WEP does not lift OR drop
            from this consolidation.
          category: source_reliability
          stated: true
          why_must_be_true: >
            The graded finding holds attribution layer at "likely"
            (cap). If five-vendor uncertainty actually constitutes
            negative attribution (per H2 from ACH), the WEP should drop
            to "unlikely" — a different move with different downstream
            implications. The "neither lift nor drop" framing is the
            operative analytic posture.
          when_could_be_false: >
            Operator decides that five-vendor uncertainty IS substantive
            negative attribution worth WEP-down move — would require
            crossing into negative-attribution origination, which Hard
            Rule 2 likely prohibits.
          evidence_for: [hard-rule-2, ach-h2-inconsistency-counts]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A10
          statement: >
            First-party Splunk silence (0 events over -30d) is genuinely
            "not disconfirming" per Hard Rule 8 and not evidence of
            non-exposure. The 19+-day non-archimedes-internal silent
            stream pattern means absence-of-signal is the baseline.
          category: visibility
          stated: true
          why_must_be_true: >
            If first-party silence were treated as disconfirming, the
            finding's relevance would be downgraded. The Hard Rule 8
            framing keeps Splunk silence as observational data point
            rather than negative evidence.
          when_could_be_false: >
            The silent stream pattern resolves (Splunk starts producing
            external-source-relevant events); silence at that point would
            be more meaningful. Currently the silent stream is the
            baseline so the framing is sound.
          evidence_for: [hard-rule-8, operational-notes-on-silent-stream]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 5
        qualify: 5
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - >
            A1 (lowest-common-grade aggregation): Briefer should note that
            the cluster-anchor lift from B2 to B1 depends on Unit 42 A
            counting as letter-grade-lifting rather than count-only
            adding under conservative aggregation; if INTEL-GRADING
            doctrine resolves this differently, lift may not be warranted.
          - >
            A3 (procedural-facts semantic stability): Briefer should
            specify the lift applies to "Miasma campaign existed +
            affected namespace + Mini Shai-Hulud lineage" — NOT to
            "exactly 32 packages" (Unit 42 says "at least 32," AM cluster
            says exactly 32; minor specification discrepancy).
          - >
            A4 (Tier-1 ratification framing): Briefer should frame as
            "Unit 42's explicit decline aligns with Archimedes' AM stance"
            rather than "Tier-1 ratifies Archimedes" — the former is
            factually correct; the latter risks confirmation-bias framing.
          - >
            A6 (Mini Shai-Hulud source code is public): Briefer should
            attribute the "public source-code release" claim to Unit 42
            with citation rather than restating as Archimedes-asserted
            fact. Unit 42 attestation is the load-bearing source.
          - >
            A8 (specific TTPs remain single-firm-origination): Briefer
            MUST keep the specific TTP layers (72s window, OIDC vector,
            210 repos, api.anthropic[.]com C2) at "likely" cap with
            explicit "single-firm-origination" framing; do NOT bleed the
            procedural-facts lift into the TTP layers.
      recommended_wep_after_test:
        procedural_facts_layer_on_am_finding_0003: very_likely    # H1 ACH ranking with conservative aggregation noted
        specific_ttp_layers: likely                                # capped per A8 single-firm-origination
        teampcp_attribution_layer: likely                          # capped per A9 consensus-on-uncertainty
        if_a1_resolves_against_lift: likely                        # if doctrine confirms lowest-common-grade pins cluster letter at C-grade member presence
        if_unit42_actually_relays_am_cluster_vendors: likely       # if independence test fails on direct-primary retrieval

analyst_review_status: completed
analyst_review_run_id: analyst-20260602-170000
analyst_review_at: 2026-06-02T17:30:00-04:00

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-02-afternoon]
retracted: false
retraction_brief_id: null

# Operator handoffs
operator_handoffs:
  - handoff_type: am_finding_0003_wep_recheck_candidate
    target: finding-2026-06-02-0003-securityweek-reversinglabs-aikido-ox-socket-miasma-red-hat-npm-32-package-vt006-extension-multi-firm-corroboration-oidc-cicd-vector
    rationale: Unit 42 Tier-1 A-grade addition to the four-vendor procedural-facts cluster lifts the procedural-facts layer mathematically from B2 (likely) to B1 (very_likely). Analyst / red-team should formally rerun the WEP assessment on AM finding 0003 to ratify the lift, and the librarian should update AM finding 0003's frontmatter (or the briefer should treat this finding as the WEP-lift carrier).
    target_audience: analyst + red-team-analyst + librarian
  - handoff_type: vt_006_dossier_update_candidate
    target: VT-006
    rationale: Unit 42 hedge + Miasma derivation chain documentation; vuln-tracker may fold into VT-006 tracking on next pass; consider extending VT-006 scope-of-coverage to enumerate Unit 42 as Tier-1 corroborator alongside originating four-vendor cluster
    target_audience: vuln-tracker
  - handoff_type: teampcp_dossier_update_candidate
    target: TeamPCP (#001)
    rationale: Unit 42's explicit Tier-1 vendor attribution hedge ("Attribution remains uncertain ... any competent actor can replicate the same attack") is dossier-update-relevant — TeamPCP threat-level may warrant reassessment given Tier-1 vendor consensus on attribution-uncertainty caused by public source-code release lowering replication barrier; actor-profiler should consider TeamPCP scoring recheck
    target_audience: actor-profiler
  - handoff_type: anti_noise_carry_forward
    target: Miasma TeamPCP attribution claims
    rationale: Hard Rule 2 stance now Tier-1 corroborated — anti-noise carry-forward for next 72h on Miasma TeamPCP attribution claims; reject any C/D/F-grade source that extends TeamPCP attribution beyond Unit 42's explicit hedge
    target_audience: collector + grader + briefer
---

# Unit 42 — June 2 Update to npm Threat Landscape Post Adds Red Hat / Miasma Section; Explicit Tier-1 Vendor TeamPCP Attribution Hedge Ratifies AM Hard Rule 2 Stance; Five-Vendor Consolidation Lifts Procedural-Facts WEP on AM Finding 0003

## Summary

Palo Alto Networks Unit 42 (ratified A) added a Red Hat / Miasma section to its long-running "npm Threat Landscape" monitor post on 2026-06-02 at 13:30 EDT (in-window), documenting the @redhat-cloud-services 32-package npm compromise as a Mini Shai-Hulud derivative carrying the "Miasma: The Spreading Blight" payload-embedded string. Unit 42 explicitly hedges attribution: "Attribution remains uncertain. The TTPs are consistent with TeamPCP, but the public release of the Mini Shai-Hulud source code means any competent actor can replicate the same attack." This Tier-1 vendor hedge is methodologically aligned with — and ratifies — Archimedes' AM Hard Rule 2 stance from finding-2026-06-02-0003 declining to extend TeamPCP attribution. The five-vendor consolidation (Unit 42 joining ReversingLabs + Aikido + Ox Security + Socket from AM cluster) lifts the procedural-facts layer WEP from "likely" to "very likely" on AM finding 0003 — analyst / red-team recheck candidate; specific TTP layers (72s publication window, OIDC vector, 210 downstream repos, api.anthropic[.]com C2) remain single-firm-origination and stay capped at "likely."

## Sources

### Palo Alto Unit 42 (unit42, digraph A — ratified)

- URL: https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
- Updated: 2026-06-02 at 17:30:33 UTC = 13:30 EDT (in-window)
- Byline: Unit 42 corporate author tag (long-running monitor post)
- Key claim: Documents Miasma as "new supply chain attack [that] compromised at least 32 packages published under the @redhat-cloud-services npm namespace" with payload "derived from Mini Shai-Hulud source code"; explicit attribution hedge declining TeamPCP extension; "Miasma: The Spreading Blight" repository description; Bun release-URL staging artifact

### AM finding 0003 four-vendor cluster (carry-forward, digraph B2 cluster-anchor lifting to B1 with Unit 42)

- Cluster vendors: ReversingLabs (C), Aikido (C), Ox Security (B), Socket (B)
- Aggregator: SecurityWeek (provisional B; Ionut Arghire byline)
- Key claim: Same procedural facts on Miasma campaign as Unit 42; specific TTP layers (72s window, OIDC vector, 210 downstream repos) remain single-firm-origination

## Technical detail

Unit 42 frames Miasma as a Mini Shai-Hulud variant — the variant name is researcher- or actor-coined per the embedded "Miasma: The Spreading Blight" repository description string surfaced via Unit 42 attestation. Bun download source `github.com/oven-sh/bun/releases/download/bun-v1.3.13/` (legitimate Bun runtime release URL) is abused in the campaign for staging. Affected package namespace examples include `@redhat-cloud-services/chrome` and `@redhat-cloud-services/frontend-components` within the 32-package set.

Unit 42 does NOT add net-new specific TTP layers beyond the AM finding 0003 cluster — the June 2 update adds a Red Hat / Miasma section that frames at the campaign-and-mechanism level (Miasma derives from Mini Shai-Hulud source code) rather than the layer-detail level. The CVE/VT-006 linkage is procedurally implicit through the Mini Shai-Hulud lineage chain; Unit 42 does NOT directly reference CVE-2026-45321 or the VT-006 identifier in the June 2 update text.

Unit 42's monitor post includes defensive mitigation guidance (subscription-allowlists, npm-token-rotation) which is defender-applicable for any DIB-adjacent SDLC posture.

## IOCs surfaced

- `@redhat-cloud-services` npm namespace (32 packages compromised; cross-corroborated with AM finding 0003 cluster)
- "Miasma: The Spreading Blight" repository description string (researcher-or-actor-coined variant identifier; cross-corroborated)
- `github.com/oven-sh/bun/releases/download/bun-v1.3.13/` (legitimate Bun release URL abused as staging; Unit 42 single-source on this specific staging-URL artifact at sweep time)

All other Miasma IOCs from AM finding 0003 cluster + finding 0004 originating cluster (96 malicious versions, 72s publication window, OIDC token issuance vector, 210 downstream-repo count, api.anthropic[.]com C2, AES-128/256-GCM + RSA-OAEP encryption, SHA-256 published tarball hashes, "ifyouinvalidatethistoken" internal payload string) carry forward as canonical IOC set; Unit 42 does NOT add net-new on these.

## Relationship to existing findings

Tier-1 vendor corroboration of `finding-2026-06-02-0003` (AM cluster). Unit 42 is the FIFTH independent vendor on the campaign's procedural-facts layer. The substantive new addition vs. AM finding 0003 is (a) Tier-1 vendor weight (A-grade joining the four-vendor B-grade cluster) and (b) explicit Tier-1 vendor TeamPCP attribution hedge ratifying Archimedes' AM Hard Rule 2 stance.

Implications:
- **AM finding 0003 procedural-facts WEP lift candidate** — five-vendor consolidation mathematically lifts procedural-facts layer from B2 (likely) to B1 (very likely). Analyst / red-team formal recheck of AM finding 0003 WEP is the appropriate action.
- **AM finding 0003 specific TTP layers and TeamPCP attribution WEP capped at "likely"** — Unit 42 does NOT add independent corroboration on any specific TTP detail; attribution-uncertain consensus across five vendors is consensus-on-uncertainty, NOT corroboration-of-attribution.

Also relates to:
- `finding-2026-06-01-0004-socket-thn-miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain-vt006-family-expansion-anthropic-impersonation-c2` — originating Socket + THN coverage with the Anthropic-API-impersonation C2 detail (Socket-only single-source).

## Open questions for analyst

1. **SAT-ACH on Archimedes position relative to Unit 42's explicit decline:** Unit 42's hedge is Tier-1 vendor ratification of Archimedes' Hard Rule 2 stance. ACH the position: (a) "Archimedes' AM Hard Rule 2 stance was correct and is now Tier-1 corroborated — preserve and carry forward" vs. (b) "Five-vendor consensus on attribution-uncertainty is itself a form of negative attribution — TeamPCP attribution should be downgraded to 'unlikely' from 'likely'." Likely (a), but KAC the assumption.

2. **SAT-KAC on layered WEP assumption for AM finding 0003 recheck:** Procedural-facts layer mathematically lifts from B2 to B1 with Unit 42 addition. KAC the assumption: (a) five-vendor consolidation genuinely lifts to "very likely"; (b) conservative B2 should hold pending direct Unit 42 primary direct-retrieval validation of all five-vendor IOC convergence; (c) the lift applies to "procedural facts" but defining "procedural facts" precisely matters (compromise occurred = clearly lifted; "32 packages" exact count vs. "at least 32" — Unit 42 says "at least" — minor discrepancy worth KAC).

3. **TeamPCP dossier update candidate:** Unit 42's hedge content is dossier-update-relevant — TeamPCP threat-level may warrant reassessment given Tier-1 vendor consensus on attribution-uncertainty caused by public source-code release lowering replication barrier. Actor-profiler should consider TeamPCP scoring recheck.

4. **Red-team specifically argue against** the procedural-facts WEP lift assumption — is five-vendor consolidation genuinely sufficient to lift to "very likely," or should conservative B2 hold given the cluster includes C-grade members (Aikido, ReversingLabs)?

## Analytic notes (from analyst review)

ACH ranks H1 (preserve AM Hard Rule 2 declination on TeamPCP; treat Unit 42's hedge as Tier-1 vendor alignment) at zero inconsistencies with the strongest diagnostic support. H4 (unrelated competent actor reusing publicly-released Mini Shai-Hulud source code) is functionally equivalent at zero inconsistencies and cannot be distinguished from H1 without TeamPCP-diagnostic signal that no vendor has produced — Unit 42's "any competent actor can replicate" hedge effectively legitimizes H4 as a viable alternative. H3 (upgrade TeamPCP attribution on the strength of Tier-1 weight + lineage chain) draws five inconsistencies and is ruled out; adopting H3 would directly cross Hard Rule 2. The brittleness is low — the conclusion holds even if Unit 42's hedge is downgraded, because the public-source-code availability claim independently contradicts H3.

KAC surfaces ten assumptions, five sound, five qualify, none requiring test. The procedural-facts WEP lift on AM finding 0003 (likely → very_likely) is methodologically defensible but rests on three load-bearing premises worth caveating: (A1) lowest-common-grade aggregation logic across the five-vendor cluster, where Unit 42's A-grade addition lifts the cluster anchor rather than being pinned by C-grade Aikido/ReversingLabs presence; (A3) "procedural facts" as a stable semantic layer where Unit 42's "at least 32 packages" introduces a minor specification discrepancy versus AM cluster's exact "32"; and (A4) the "Tier-1 ratification" framing, which should be reworded by the briefer to "Unit 42's explicit decline aligns with Archimedes' AM stance" to avoid confirmation-bias optics.

No blocking concerns for publication. Briefer should carry the procedural-facts lift forward for AM finding 0003 (or treat this finding as the WEP-lift carrier per operator handoff). Specific TTP layers (72s window, OIDC, 210 repos, api.anthropic[.]com C2) MUST stay capped at "likely" per single-firm-origination veto — do not bleed the procedural-facts lift into the TTP layers. TeamPCP attribution stays at "likely" cap; the five-vendor consensus on attribution-uncertainty is consensus-on-uncertainty, not consensus-on-negation. Red-team is correctly invoked at WEP very_likely on the procedural-facts layer and should specifically pressure-test A1 (aggregation rule) rather than the attribution layer.
