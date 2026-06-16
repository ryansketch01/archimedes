---
id: finding-2026-06-16-0004
finding_id: finding-2026-06-16-0004-bc-symantec-dragonforce-backdoor-turn-microsoft-teams-turn-relay-abuse-byovd-palo-alto-masquerade
title: "BleepingComputer (Bill Toulas) relay of Symantec/Broadcom primary IR report discloses DragonForce ransomware operators used custom Go-based RAT 'Backdoor.Turn' to hide command-and-control traffic inside Microsoft Teams TURN (Traversal Using Relays around NAT) relay infrastructure — novel TTP described per Symantec as 'the first known malware to abuse Microsoft Teams TURN relay servers' (15 words, Hard Rule 6 at limit not exceeded); attack against 'a major U.S. services company' in December 2025 (no A&D-prime named victim, victim not identified by name in BC); BYOVD (Bring Your Own Vulnerable Driver) pre-ransomware-deployment defense evasion using Huawei driver + Topaz Antifraud driver + K7 Security driver + custom Palo Alto Networks driver masquerader (impersonates Palo Alto Cortex XDR / Palo Alto driver — distinct from generic vulnerable-driver abuse); BC describes DragonForce as 'linked to Scattered Spider' (Scattered Spider on _roster.yaml #013 HIGH — Hard Rule 2 BINDING: Archimedes does NOT originate the DragonForce/Scattered Spider cross-walk, Symantec asserts the linkage); DragonForce NOT on _roster.yaml as primary or alias; single A-grade vendor IR primary (Symantec/Broadcom) substrate via single B-grade publisher relay (BC) — single-source veto applied on novel-TTP and DragonForce-Scattered-Spider-linkage layers; WEP ceiling likely; A&D-relevance LOW direct (victim sector unspecified, likely commercial services not A&D-prime) but HIGH on TTP-pattern-applicability (TURN-relay abuse broadly applicable across enterprise tenants using Microsoft Teams including A&D-prime tenants; BYOVD with custom Palo Alto masquerader is tradecraft layer that A&D-prime EDR posture defenders should track); no specific IOCs in BC article (BC notes Symantec published complete IOC list — operator-deferred direct Symantec retrieval)"
date: 2026-06-16
created_at: 2026-06-16T08:00:00-04:00
graded_by: grader
grading_run_id: morning-20260616-080000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  symantec_broadcom_vendor_ir_primary_via_bc_relay_only_not_directly_retrieved_this_sweep: B2
  novel_ttp_backdoor_turn_first_known_malware_to_abuse_microsoft_teams_turn_relay_servers: A2  # Symantec primary attribution preserved
  backdoor_turn_go_based_rat_custom_malware_attributed_dragonforce: A2
  turn_relay_abuse_pattern_traversal_using_relays_around_nat_legitimate_webrtc_protocol_abused_for_c2_obfuscation: A2
  ttp_novelty_genuinely_net_new_as_ttp_layer_possible_detection_pattern_substrate: A2
  attack_against_major_us_services_company_december_2025_victim_not_named_in_bc: A2
  no_ad_prime_named_victim: A1
  byovd_bring_your_own_vulnerable_driver_pre_ransomware_deployment_defense_evasion: A2
  byovd_huawei_driver: A2
  byovd_topaz_antifraud_driver: A2
  byovd_k7_security_driver: A2
  byovd_custom_palo_alto_networks_masquerader_driver_impersonates_palo_alto_cortex_xdr_distinct_from_generic_vulnerable_driver_abuse: A2
  final_stage_ransomware_deployment_after_byovd_defense_evasion: A2
  dragonforce_active_since_2023_per_symantec: A2
  symantec_attributes_dragonforce_scattered_spider_linkage: B2  # Symantec asserts linkage; BC relays; substrate single-vendor-on-cross-walk-layer
  dragonforce_not_on_24_actor_roster_as_primary_or_alias: A1
  scattered_spider_on_roster_013_high_threat_level_archimedes_does_not_collapse_clusters_per_hard_rule_2: A1
  hard_rule_2_no_cross_walk_originated_by_archimedes_symantec_asserted_linkage_preserved_as_recorded_not_originated: A1
  sophisticated_cyber_tradecraft_per_symantec_attribution_paraphrased: A2
  no_specific_iocs_in_bc_article: A1
  bc_notes_symantec_published_complete_ioc_list_full_table_pending_direct_symantec_retrieval: A1
  behavioral_detection_pattern_anomalous_tcp_udp_flows_to_teams_turn_relay_servers_anomaly_based_detection: A2
  behavioral_detection_byovd_vulnerable_driver_indicators_huawei_topaz_antifraud_k7: A2
  behavioral_detection_custom_palo_alto_driver_masquerade_signing_certificate_anomaly: A2
  behavioral_detection_go_based_rat_executable_patterns: A2
  ad_direct_relevance: A1
  ad_relevance_ttp_pattern_turn_relay_abuse_broadly_applicable_enterprise_tenants_microsoft_teams_including_ad_prime: A2
  ad_relevance_byovd_with_custom_palo_alto_masquerader_tradecraft_layer_for_ad_prime_edr_posture_defenders: A2
  splunk_first_party_check_invoked_30d_lookback: A1
  splunk_first_party_zero_hits_on_external_indicators: A1
  frank_not_known_to_have_been_target_of_dragonforce_or_scattered_spider_visibility_bounded_absence: A1
  no_first_party_telemetry_contradiction_or_confirmation_available: A1
  net_new_substrate_novel_ttp_layer_turn_relay_abuse_first_known_malware: A1
  not_under_existing_anti_noise_hold: A1
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / action-tier inclusion).
  Symantec/Broadcom is A-grade vendor IR primary per source-grades.
  yaml id `symantec` (provisional A; vendor IR firm). BleepingComputer
  (Bill Toulas) is B-grade per source-grades.yaml id `bleepingcomputer`.
  Symantec primary NOT directly retrieved this sweep — substrate
  reached via BC relay only.

  WHY B2 NOT A2:
    1. SYMANTEC PRIMARY NOT DIRECTLY RETRIEVED — substrate reached
       through BC relay only.
    2. SINGLE-A-VENDOR-PRIMARY SUBSTRATE — Symantec stands alone on
       the Backdoor.Turn discovery, the TURN-relay-abuse-as-first-
       known-malware claim, and the DragonForce/Scattered-Spider
       linkage. No second IR vendor (Mandiant / CrowdStrike / Unit
       42 / Microsoft MSTIC) corroborates.
    3. NO INDEPENDENT PUBLISHER RELAY — BC is sole publisher relay
       at this sweep; THN / SecurityWeek / The Register / Security
       Affairs publisher-independent restatements not yet in
       substrate (would lift publisher-independence layer though
       not the underlying single-IR-vendor evidence basis).

  Single-source-veto consideration: Symantec stands alone on novel-
  TTP claim, BACKDOOR.TURN attribution, and DragonForce/Scattered-
  Spider cross-walk. BC publisher-relay does NOT constitute
  independent evidence basis. WEP ceiling caps at "likely" per
  single-source veto. Independent IR vendor corroboration of TURN-
  relay-abuse-by-Backdoor.Turn or DragonForce-as-Scattered-Spider-
  affiliate would lift veto.

  WHY NOT FLASH:
    - T5 (ad-sector-campaign): FAIL — no A&D-prime named victim;
      victim described as "a major U.S. services company" with
      sector unspecified.
    - T2 (tracked-actor-attribution): PARTIAL FIRE on Scattered
      Spider linkage per Symantec — BUT linkage is Symantec-
      asserted not vendor-confirmed by separate IR firm; HARD RULE
      2 binding — Archimedes does NOT originate or strengthen
      cross-walk beyond Symantec attribution.
    - T4 (tracked-actor-ttp-change): PASSES on TURN-relay abuse
      as novel TTP layer; HOWEVER, the tracked-actor layer requires
      Scattered Spider linkage which is single-vendor-asserted —
      single-source-veto-capped at "likely" WEP keeps it in
      morning-brief lane.
    - Net: morning-brief candidate.

  WHAT THE B2 ATTESTS:
    (a) Symantec/Broadcom has identified novel Go-based RAT
        "Backdoor.Turn" attributed to DragonForce ransomware
        operators.
    (b) Backdoor.Turn abuses Microsoft Teams TURN relay
        infrastructure to hide C2 traffic — Symantec describes
        as "the first known malware to abuse Microsoft Teams
        TURN relay servers."
    (c) Attack against "a major U.S. services company" in
        December 2025; victim not identified by name in BC.
    (d) BYOVD pre-ransomware defense evasion using four
        distinct vulnerable / impersonator drivers: Huawei
        driver, Topaz Antifraud driver, K7 Security driver,
        and custom Palo Alto Networks masquerader driver.
    (e) Final-stage ransomware deployment after BYOVD defense
        evasion.
    (f) BC relays Symantec's framing of DragonForce as
        "linked to Scattered Spider" — Symantec-asserted
        cross-walk recorded but NOT originated by Archimedes.

  WHAT THE B2 DOES NOT ATTEST:
    - Specific A&D-prime victim — none named; sector
      unspecified.
    - DragonForce/Scattered Spider linkage as Archimedes-
      originated — Hard Rule 2 binding; linkage stays at
      Symantec-attribution-language preservation; Archimedes
      does NOT collapse the two clusters even though Symantec
      asserts the linkage.
    - Specific IOCs (IPs, domains, hashes) — BC notes Symantec
      published complete IOC list but BC article does not
      enumerate; operator-deferred direct Symantec retrieval.
    - First-party Frank-environment telemetry — Frank not known
      to have been target of DragonForce or Scattered Spider;
      visibility-bounded absence flagged per Hard Rule 8 binding.

  HARD RULE 2: PRESERVED. Symantec-asserted DragonForce/Scattered
  Spider linkage recorded as Symantec's claim, not originated by
  Archimedes. DragonForce NOT added to roster aliases.

  HARD RULE 6: PRESERVED. Symantec quote captured at 15-word
  limit ("the first known malware to abuse Microsoft Teams TURN
  relay servers") — paraphrase preferred in brief composition to
  give buffer.

  HARD RULE 8: PRESERVED. Splunk first-party check 30-day
  lookback; ZERO external-IOC hits; Frank not known DragonForce
  target; silent-Splunk-does-NOT-disconfirm.

source_reliability:
  grade: A
  source_name: "Symantec/Broadcom (Threat Hunter Team) primary via BleepingComputer (Bill Toulas) publisher-relay"
  source_yaml_id: symantec
  grade_rationale: >
    Symantec is A-grade per source-grades.yaml id `symantec`
    (provisional A; vendor IR firm). BC is B-grade per source-grades.
    yaml id `bleepingcomputer`. Symantec primary NOT directly
    retrieved this sweep — substrate reached through BC relay only.
    B2 cluster anchor reflects substrate reached via single-publisher-
    relay of single-IR-vendor-primary.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - consistent_with_established_ttps_for_ransomware_operators_byovd_defense_evasion
    - no_contradicting_evidence_from_a_or_b_grade_sources
    - technical_claims_internally_coherent
  rationale: >
    Technical claims internally coherent: BYOVD pre-ransomware
    deployment with specific named vulnerable drivers (Huawei,
    Topaz Antifraud, K7) + custom Palo Alto masquerader is a
    plausible and detailed kill chain. TURN-relay abuse is a
    plausible C2-obfuscation pattern — TURN is a legitimate
    WebRTC protocol used by Microsoft Teams for NAT traversal,
    and abuse-of-legitimate-cloud-service-for-C2-obfuscation
    is established tradecraft pattern. Consistent with
    established ransomware-operator tradecraft (BYOVD defense
    evasion + custom RAT + cloud-service abuse for C2). NO
    contradicting A/B-grade source. The novel-TTP-claim
    ("first known malware to abuse Microsoft Teams TURN relay
    servers") and the DragonForce/Scattered-Spider-linkage
    claim are single-IR-vendor (Symantec) — would lift to
    credibility 1 with independent IR vendor (Mandiant /
    CrowdStrike / Unit 42 / MSTIC) confirmation.

corroboration:
  independent_sources:
    - symantec
    - bleepingcomputer
  independent: false
  test_passed: >
    BC explicitly credits Symantec as report origin and relays
    Symantec's framing. Publisher-relay of a single A-grade
    vendor IR primary, NOT independent evidence basis. The
    corroboration test for credibility 1 requires DIFFERENT
    EVIDENCE BASIS — independent IR vendor corroboration
    (Mandiant / CrowdStrike / Unit 42 / MSTIC) would
    constitute different evidence basis on the novel-TTP-layer
    and DragonForce/Scattered-Spider-linkage layer.
  independent_layered:
    symantec_vendor_ir_primary: true
    bleepingcomputer_publisher_relay: false

first_party_precedence:
  applied: true
  splunk_evidence:
    query_executed: "search index=archimedes OR index=defenseclaw_local (\"Backdoor.Turn\" OR \"DragonForce\" OR \"Scattered Spider\" OR \"TURN relay\") earliest=-30d"
    hits_on_external_indicators: 0
    note: >
      30-day lookback. ZERO hits on external indicators across
      defenseclaw_local + archimedes. The 16 hits returned are
      Archimedes' own operational meta-logging events. Frank is
      not known to have been target of DragonForce or Scattered
      Spider; visibility-bounded absence flagged per Hard Rule
      8 binding — silent-Splunk-does-NOT-disconfirm. Symantec
      vendor IR primary attestation stands.

single_source_veto_applied: true
single_source_veto_layers:
  - symantec_only_on_backdoor_turn_novel_ttp_layer_no_independent_ir_vendor_corroboration
  - symantec_only_on_dragonforce_scattered_spider_cross_walk_layer_no_independent_ir_vendor_corroboration
wep_ceiling: likely

cluster:
  topic: "DragonForce ransomware operators novel TTP: Backdoor.Turn Go-based RAT abusing Microsoft Teams TURN relay infrastructure for C2 obfuscation; BYOVD with custom Palo Alto Networks driver masquerader; Symantec-asserted Scattered Spider linkage; attack against unnamed major U.S. services company December 2025"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-16-am-007-bc-dragonforce-backdoor-turn-microsoft-teams-relay-abuse-symantec-primary
  attribution_claims:
    - claimed_actor: "DragonForce (Symantec asserts linkage to Scattered Spider)"
      claimed_by_sources: [symantec]
      requires_analyst_review: true
      note: "Symantec originates DragonForce/Scattered Spider linkage claim — Hard Rule 2 BINDING; Archimedes records the claim, does NOT originate the cross-walk or collapse the clusters. DragonForce NOT on roster as primary or alias. Scattered Spider on roster #013 HIGH — operator-deferred Scattered Spider dossier mutation candidacy if cross-walk operator-approved (separate /update-tracking path)."

related_actors:
  - id: "013"
    primary_name: "Scattered Spider"
    threat_level: HIGH
    note: "Symantec-asserted linkage; Hard Rule 2 binding — Archimedes does NOT collapse clusters; relationship recorded as Symantec claim only"

inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
  not_eligible_for:
    - flash  # T5 fail (no A&D-prime victim); T2 partial (Symantec-asserted Scattered Spider linkage not vendor-confirmed by separate IR firm); single-source-veto-capped WEP keeps in morning-brief lane
    - actor_profile_update  # DragonForce not on roster; Scattered Spider dossier mutation requires operator approval per Hard Rule 2 on cross-walk

analyst_review_required: true   # WEP "likely" + Symantec-asserted Scattered Spider linkage + novel-TTP layer
analyst_review_status: complete
analyst_review_completed_at: 2026-06-16T08:30:00-04:00
analyst_review_run_id: analyst-20260616-083000
red_team_review_required: false # WEP ceiling capped at "likely" per single-source veto
red_team_review: null
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "How should Symantec's asserted DragonForce → Scattered Spider linkage be characterized — affiliate relationship within a Ransomware-as-a-Service program, cluster-overlap via shared toolkit/operators, attribution-misread by Symantec, or distinct clusters with shared third-party tooling?"
      analyzed_at: 2026-06-16T08:30:00-04:00
      analyzed_by: analyst
      red_team_review: null

      hypotheses:
        - id: H1
          statement: "Affiliate-program linkage: DragonForce operates a Ransomware-as-a-Service program; Scattered Spider acts as an affiliate (or one of several affiliates) using DragonForce's payload. The 'linkage' is a business relationship, not cluster collapse."
        - id: H2
          statement: "Cluster overlap via shared operators or shared toolkit: DragonForce and Scattered Spider have personnel overlap or use shared tooling supplied by a common quartermaster; the 'linkage' reflects operational overlap without affiliate-program structure."
        - id: H3
          statement: "Attribution-misread by Symantec: the activity Symantec is attributing to DragonForce-operators-linked-to-Scattered-Spider is actually a different actor entirely, and the linkage is a methodology error from infrastructure/tradecraft pattern matching."
        - id: H4
          statement: "Distinct clusters with shared third-party tools (e.g., shared access broker, shared LLM-tooling supplier, shared BYOVD driver supplier); DragonForce and Scattered Spider operate independently but acquire some inputs from common sources. 'Linkage' is supply-chain coincidence rather than operational relationship."
        - id: H5
          statement: "Null / surprise hypothesis: DragonForce is a Scattered Spider sub-brand or rebrand. Scattered Spider has documented history of rebranding/sub-branding (ALPHV/BlackCat affiliate history, RansomHub, etc.); DragonForce may be a Scattered Spider operational extension rather than a distinct cluster."

      evidence:
        - id: E1
          description: "Symantec/Broadcom asserts DragonForce 'linked to Scattered Spider' framing per BC publisher-relay; Symantec is A-grade vendor IR primary"
          source: symantec_via_bc
          digraph: B2
          weight: 2
        - id: E2
          description: "Custom Go-based RAT 'Backdoor.Turn' described as DragonForce custom tooling; abuses Microsoft Teams TURN relay infrastructure (Symantec frames as 'first known malware' for this pattern)"
          source: symantec_via_bc
          digraph: A2
          weight: 3
        - id: E3
          description: "BYOVD pre-ransomware defense evasion using Huawei driver + Topaz Antifraud driver + K7 Security driver + custom Palo Alto Networks masquerader driver; the custom PAN masquerader is distinctive tradecraft layer"
          source: symantec_via_bc
          digraph: A2
          weight: 3
        - id: E4
          description: "Attack against 'a major U.S. services company' in December 2025; victim sector unspecified, no A&D-prime named victim"
          source: symantec_via_bc
          digraph: A2
          weight: 3
        - id: E5
          description: "DragonForce active since 2023 per Symantec; DragonForce is documented elsewhere in industry reporting as ransomware-as-a-service operator with affiliate program structure (e.g., Marks-and-Spencer / Co-op UK 2025 attribution by independent vendors)"
          source: symantec_via_bc_plus_industry_baseline
          digraph: A2
          weight: 3
        - id: E6
          description: "Scattered Spider on Archimedes roster #013 HIGH; documented affiliate-cycling history (ALPHV/BlackCat → RansomHub → various RaaS operators); does affiliate work for multiple ransomware brands"
          source: roster_baseline
          digraph: A2
          weight: 3
        - id: E7
          description: "No independent IR vendor corroboration (Mandiant / CrowdStrike / Unit 42 / MSTIC) of the Backdoor.Turn novel-TTP attribution or DragonForce/Scattered-Spider linkage"
          source: corroboration_gap
          digraph: A1
          weight: 3
        - id: E8
          description: "DragonForce NOT on Archimedes roster #013 as primary or alias; DragonForce is operationally distinct cluster identity in vendor taxonomy"
          source: roster_baseline
          digraph: A1
          weight: 3
        - id: E9
          description: "First-party Splunk telemetry: 30-day lookback, zero hits on Backdoor.Turn / DragonForce / Scattered Spider / TURN relay. Frank not known DragonForce/Scattered Spider target — visibility-bounded absence per Hard Rule 8"
          source: splunk_negative_search
          digraph: A1
          weight: 3

      matrix:
        E1: {H1: C, H2: C, H3: I, H4: N, H5: C}
        E2: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E3: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E4: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E5: {H1: C, H2: N, H3: N, H4: N, H5: I}
        E6: {H1: C, H2: C, H3: N, H4: N, H5: C}
        E7: {H1: N, H2: N, H3: N, H4: N, H5: N}
        E8: {H1: C, H2: N, H3: N, H4: C, H5: I}
        E9: {H1: N, H2: N, H3: N, H4: N, H5: N}

      inconsistency_counts:
        H1: 0
        H2: 0
        H3: 1
        H4: 0
        H5: 2

      diagnostic_evidence:
        - E1: "Symantec's vendor authority is diagnostic against H3 (misread). A-grade IR vendor attribution methodology error is possible but requires positive evidence; absence of contradicting source means H3 stays in play but doesn't rise."
        - E5: "DragonForce's documented RaaS-affiliate-program structure (industry baseline) is diagnostic in favor of H1 (affiliate linkage) and against H5 (Scattered Spider rebrand). H1 is consistent with the established DragonForce operational pattern."
        - E6: "Scattered Spider's documented affiliate-cycling history is diagnostic in favor of H1 — Scattered Spider routinely affiliates with multiple RaaS brands; DragonForce affiliate engagement fits the documented pattern."
        - E8: "Roster taxonomy distinction (DragonForce not collapsed to Scattered Spider in any vendor's authoritative cluster definition) is diagnostic against H5 (rebrand) — vendor taxonomies have not absorbed DragonForce into Scattered Spider."

      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: "Zero inconsistencies. Best fit: DragonForce-as-RaaS + Scattered-Spider-as-affiliate matches the documented operational pattern for both clusters. Industry baseline supports — DragonForce has affiliate program structure; Scattered Spider has affiliate-cycling history. Cleanest explanation for Symantec's 'linkage' framing."
          wep: likely
        - rank: 2
          hypothesis_id: H2
          rationale: "Zero inconsistencies. Operator-overlap or shared-toolkit hypothesis cannot be distinguished from H1 without granular operational evidence (e.g., shared infrastructure, shared TTPs beyond the campaign artifacts). For defensive purposes equivalent to H1."
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H4
          rationale: "Zero inconsistencies. Shared third-party tools hypothesis is plausible but does not explain Symantec's specific 'linkage' framing as well as H1. Possible alternative."
          wep: unlikely
        - rank: 4
          hypothesis_id: H3
          rationale: "One inconsistency (E1). Misread requires Symantec methodology error against the standing A-grade vendor authority. Possible but requires positive evidence absent in substrate."
          wep: very_unlikely
        - rank: 5
          hypothesis_id: H5
          rationale: "Two inconsistencies (E5, E8). Rebrand hypothesis requires DragonForce to lack independent operational footprint (contradicted by 2023+ activity history and independent vendor reporting). Vendor taxonomies preserving DragonForce as distinct cluster argues against rebrand. Ruled out at low probability."
          wep: remote

      sensitivity_analysis:
        brittleness: low
        load_bearing_evidence: [E1, E5, E6]
        if_symantec_authority_questioned: "H3 rises; cluster relationship becomes contested. Brief framing would shift toward 'Symantec asserts; methodology not independently verified.'"
        if_independent_ir_vendor_corroborates_affiliate_relationship: "H1 confirmed; Scattered Spider dossier mutation candidacy substrate-ready for operator approval."
        if_independent_ir_vendor_attributes_to_different_cluster: "H3 rises; brief framing presents competing vendor cluster identities."
        if_dragonforce_emerges_as_scattered_spider_rebrand: "H5 re-evaluated; this would require positive evidence (e.g., personnel attribution, infrastructure collapse) currently absent."
        single_point_of_failure: "Symantec attribution methodology on the linkage layer specifically. The DragonForce-and-Scattered-Spider-as-distinct-clusters baseline is well-established in industry; the linkage claim is the novel substrate that depends on Symantec alone."

      tripwires:
        - observation: "Independent IR vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC) corroborates DragonForce / Scattered Spider affiliate or operator-overlap relationship"
          effect: "H1 (or H2) confirmation; Scattered Spider dossier mutation candidacy strengthens via /update-tracking pathway; cross-walk operator approval pathway becomes substrate-ready."
        - observation: "Independent IR vendor attributes Backdoor.Turn to a different ransomware operator entirely"
          effect: "H3 rises significantly; brief framing must present competing vendor attributions."
        - observation: "Backdoor.Turn samples surface in non-DragonForce-attributed ransomware operation"
          effect: "H2 (shared toolkit) confirmed via positive evidence; H1 (affiliate-program) weakened."
        - observation: "Symantec primary directly retrieved with full IOC table + named victim or detailed methodology"
          effect: "Re-run ACH with granular operational evidence; sensitivity drops."
        - observation: "First-party Splunk hit on Backdoor.Turn / Microsoft Teams TURN relay anomaly pattern / BYOVD driver indicators"
          effect: "Hard Rule 8 binding — first-party precedence; rerun analysis with first-party telemetry weighting."

      conclusion:
        summary: |
          Symantec's DragonForce → Scattered Spider linkage framing is best
          explained as RaaS-affiliate-program relationship (H1) — DragonForce
          operates the RaaS, Scattered Spider acts as affiliate. This is
          consistent with documented operational patterns for both clusters
          and does NOT require treating DragonForce and Scattered Spider as
          the same cluster identity. Hard Rule 2 binding preserved — even
          with H1 at zero inconsistencies, Archimedes does NOT collapse
          DragonForce into Scattered Spider on roster; the linkage stays at
          Symantec-attribution-language preservation. Operator-approved
          dossier mutation pathway (separate /update-tracking) could record
          DragonForce affiliate relationship in Scattered Spider dossier
          notes WITHOUT collapsing the cluster identity.
        wep: likely
        confidence_caveats: |
          Single-vendor evidence basis on linkage layer (E7) is the binding
          constraint. WEP at 'likely' matches the grader's single-source
          veto assessment. Brief should present DragonForce-Scattered Spider
          linkage as Symantec's claim, not as Archimedes-confirmed cross-
          walk. Scattered Spider dossier mutation candidacy substrate-ready
          but operator approval required per Hard Rule 2 cross-walk
          discipline; mutation should record affiliate relationship
          context, not collapse the clusters.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Symantec's Backdoor.Turn is the first known malware to abuse
        Microsoft Teams TURN relay servers; DragonForce operators (linked to
        Scattered Spider per Symantec) used Backdoor.Turn with BYOVD pre-
        ransomware defense evasion including a custom Palo Alto Networks
        masquerader driver against a major U.S. services company in December
        2025."
      analyzed_at: 2026-06-16T08:30:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-brief analyst review on grader-deferred DragonForce/Scattered-Spider-cluster-relationship and TURN-relay-abuse-novelty-claim layers"

      assumptions:
        - id: A1
          statement: "Microsoft Teams TURN relay abuse for C2 obfuscation has NOT been documented in unrelated tradecraft research (security-research blogs, academic papers, prior incident reports); Symantec's 'first known malware' framing accurately reflects the public record"
          category: source_reliability
          stated: true
          why_must_be_true: "Novelty claim depends on absence of prior public reporting"
          when_could_be_false: "Generic TURN relay abuse for C2 obfuscation may have been documented in security-research literature without operational attribution to malware (e.g., red-team blog posts, academic protocol-abuse research, prior incident reports that did not characterize the C2 mechanism the same way); 'first known malware' is a defensible framing only if Symantec did a comprehensive prior-art search"
          evidence_for: [symantec_first_known_framing]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A2
          statement: "Microsoft Teams TURN relay servers are accessible-enough endpoints that attackers can reliably establish persistent C2 channels — i.e., the abuse pattern works operationally at scale, not just in single-victim demos"
          category: technology
          stated: false
          why_must_be_true: "TTP-pattern-applicability framing depends on the technique being operationally viable"
          when_could_be_false: "Microsoft Teams TURN servers may have rate-limiting / abuse-detection that limits the technique's scalability; the December 2025 single-victim observation may reflect a narrow operational window rather than reliable persistent C2"
          evidence_for: []
          evidence_against: []
          confidence: unknown
          centrality: material
          classification: qualify
        - id: A3
          statement: "The custom Palo Alto Networks masquerader driver is genuinely distinct tradecraft from generic vulnerable-driver abuse, not just a labeling distinction Symantec is drawing"
          category: ttp_patterns
          stated: true
          why_must_be_true: "Tradecraft-novelty framing depends on this being operationally distinct"
          when_could_be_false: "Driver masquerade as legitimate-vendor signing certificate is documented tradecraft pattern (BYOVD-with-Cobalt-Strike-signed-drivers, fake-EDR-driver patterns); the PAN-specific masquerade may be incremental rather than novel"
          evidence_for: []
          evidence_against: [byovd_driver_masquerade_documented_tradecraft_industry_baseline]
          confidence: low
          centrality: peripheral
          classification: qualify
        - id: A4
          statement: "Symantec's IR observation of the December 2025 attack reflects the full scope of the incident — i.e., Symantec had visibility into the complete kill chain from initial access through ransomware deployment"
          category: source_reliability
          stated: false
          why_must_be_true: "Brief framing implies confidence in Symantec's complete observation"
          when_could_be_false: "Symantec IR engagement may have started post-compromise (incident-response window) without visibility into initial access or pre-deployment lateral movement; substantial portions of the kill chain may be inferred rather than observed"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A5
          statement: "DragonForce as an actor identity is operationally coherent — i.e., 'DragonForce' refers to a consistent set of operators across multiple campaigns, not a brand used by varying actors at different times"
          category: actor_continuity
          stated: false
          why_must_be_true: "Attribution depends on DragonForce being a coherent referent"
          when_could_be_false: "Ransomware brands are sometimes used by varying operator clusters as the brand changes hands or affiliates rotate; 'DragonForce' in 2026 may not be the same operator set as 'DragonForce' in 2023"
          evidence_for: [symantec_dragonforce_active_since_2023_framing]
          evidence_against: [ransomware_brand_lifecycle_industry_pattern_brand_handoffs]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "Scattered Spider cluster identity on Archimedes roster #013 is stable across 2024-2026 — i.e., the actor profile baseline against which we evaluate the Symantec-asserted linkage is current"
          category: actor_continuity
          stated: false
          why_must_be_true: "Linkage evaluation depends on Scattered Spider being a stable referent"
          when_could_be_false: "Scattered Spider has documented affiliate cycling and operational changes; roster baseline may need refresh; cluster boundary may have drifted"
          evidence_for: [roster_baseline_scattered_spider]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A7
          statement: "Anomalous TCP/UDP flows to Microsoft Teams TURN relay servers are a detectable behavior with reasonable false-positive rate (i.e., the TTP-pattern-applicability framing translates to a workable detection signature)"
          category: technology
          stated: true
          why_must_be_true: "A&D-relevance HIGH on TTP-pattern-applicability framing depends on defensive utility"
          when_could_be_false: "Legitimate Microsoft Teams traffic uses TURN relays heavily; anomaly-detection in this channel has high false-positive risk; detection may not be operationally viable for A&D EDR teams"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A8
          statement: "First-party Splunk silence on Backdoor.Turn / DragonForce / Scattered Spider / TURN relay queries is not negative evidence because Frank was not the named December 2025 victim"
          category: visibility
          stated: true
          why_must_be_true: "Hard Rule 8 binding — silent-Splunk-does-NOT-disconfirm when first-party visibility doesn't intersect with the named campaign pattern"
          when_could_be_false: "If a future DragonForce or Scattered Spider campaign extension to US A&D primes occurred and Splunk still showed no hits, visibility-bounded-absence interpretation would weaken"
          evidence_for: [hard_rule_8_doctrine, frank_not_named_victim]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound

      classifications_summary:
        sound: 1
        qualify: 7
        test: 0
        reject: 0

      remediation:
        status: proceed
        qualifying_caveats:
          - "TURN-relay-abuse 'first known malware' framing accepts Symantec's prior-art search as comprehensive; security-research prior art outside vendor IR reporting cannot be ruled out"
          - "TURN-relay-abuse operational viability at scale is unknown beyond the single-victim December 2025 observation"
          - "Custom PAN masquerader driver framed as distinct from generic BYOVD; industry baseline includes driver-masquerade tradecraft patterns"
          - "Symantec IR observation completeness assumed; if engagement started post-compromise, initial access framing may be inferred not observed"
          - "DragonForce 2026 operational coherence with 2023 lineage assumed; ransomware brand lifecycle may have introduced operator handoffs"
          - "Scattered Spider roster baseline #013 assumed stable; cluster boundary drift cannot be ruled out without /update-tracking refresh"
          - "Anomalous Teams TURN traffic detection has high false-positive risk; defensive utility framing carries operational-deployment qualifier"
        test_required: null
        next_action: "Proceed to brief at WEP 'likely' with seven qualifying caveats. Scattered Spider dossier mutation candidacy substrate-ready for operator-approved /update-tracking pathway with explicit DragonForce-as-affiliate framing per ACH H1 — does NOT collapse the clusters."

      recommended_wep_after_test:
        if_independent_ir_vendor_corroborates_affiliate_linkage: "WEP rises to very_likely on linkage layer; Scattered Spider dossier mutation pathway becomes operator-ready"
        if_independent_ir_vendor_attributes_to_different_operator: "WEP drops to roughly_even_chance on attribution layer; brief framing must reflect cluster contestation"
        if_security_research_prior_art_documents_turn_relay_abuse: "Novelty claim weakens; WEP on TTP-novelty layer drops to possibly; defensive value of TTP-pattern-applicability framing unchanged"
        if_first_party_splunk_hit: "Hard Rule 8 binding — first-party precedence; rerun analysis"

tlp: CLEAR
published_in_briefs:
  - 2026-06-16-morning
retracted: false
retraction_brief_id: null
---

# Symantec/Broadcom (via BC relay): DragonForce ransomware operators deploy novel Go-based RAT Backdoor.Turn abusing Microsoft Teams TURN relay for C2 obfuscation; BYOVD with custom Palo Alto Networks driver masquerader pre-ransomware-deployment; Symantec-asserted Scattered Spider linkage

## Summary

Symantec/Broadcom (Threat Hunter Team) primary IR report — reached this sweep through BleepingComputer (Bill Toulas) publisher-relay — discloses that **DragonForce** ransomware operators used a custom Go-based RAT named **Backdoor.Turn** to hide command-and-control traffic inside Microsoft Teams **TURN (Traversal Using Relays around NAT)** relay infrastructure. Symantec describes Backdoor.Turn as "the first known malware to abuse Microsoft Teams TURN relay servers" — a genuinely novel TTP layer worth surfacing as detection-pattern substrate. The attack targeted "a major U.S. services company" in December 2025 (no A&D-prime named victim; sector unspecified). Pre-ransomware-deployment defense evasion used **BYOVD (Bring Your Own Vulnerable Driver)** techniques with four distinct vulnerable / impersonator drivers — Huawei driver, Topaz Antifraud driver, K7 Security driver, and a **custom Palo Alto Networks masquerader driver** that impersonates Palo Alto Cortex XDR / Palo Alto driver to evade detection (distinct tradecraft from generic vulnerable-driver abuse). BC relays Symantec's framing of DragonForce as **"linked to Scattered Spider"** — Scattered Spider is on `_roster.yaml` #013 (HIGH threat level), but Hard Rule 2 is BINDING: Archimedes does NOT originate or collapse the cross-walk; the linkage is recorded as Symantec's attribution claim only. DragonForce is NOT on `_roster.yaml` as primary or alias. Single A-grade vendor IR primary substrate via single B-grade publisher relay — single-source veto applied on novel-TTP layer and DragonForce/Scattered-Spider-linkage layer. WEP ceiling caps at "likely." A&D-relevance LOW direct (victim sector unspecified, likely commercial services) but HIGH on TTP-pattern-applicability: TURN-relay abuse is broadly applicable across enterprise tenants using Microsoft Teams including A&D-prime tenants, and BYOVD with custom Palo Alto masquerader is a tradecraft layer A&D-prime EDR posture defenders should track. No specific IOCs in BC article — BC notes Symantec published a complete IOC list; operator-deferred direct Symantec retrieval.

## Sources

### Symantec/Broadcom (source_yaml_id: symantec, digraph: A) — PRIMARY

- Primary report not directly retrieved this sweep; substance reached via BC publisher-relay
- Source: Symantec Threat Hunter Team / Broadcom
- Key claim: Novel Go-based RAT Backdoor.Turn attributed to DragonForce; first known malware to abuse Microsoft Teams TURN relay; BYOVD with custom Palo Alto masquerader; DragonForce-Scattered Spider linkage

### BleepingComputer (source_yaml_id: bleepingcomputer, digraph: B)

- URL: https://www.bleepingcomputer.com/news/security/ransomware-gang-abuses-microsoft-teams-relays-to-hide-malicious-traffic/
- Published: 2026-06-16T10:18:48Z
- Byline: Bill Toulas
- Key claim: Publisher-relay of Symantec primary; DragonForce/Scattered Spider linkage relayed; victim described as "a major U.S. services company" December 2025

## Technical detail

### Novel TTP — Backdoor.Turn abuses Microsoft Teams TURN relay

- **Backdoor.Turn** is a Go-based RAT — custom DragonForce tooling
- Symantec describes as "the first known malware to abuse Microsoft Teams TURN relay servers" (15 words, at Hard Rule 6 limit — paraphrase preferred in brief)
- TURN (Traversal Using Relays around NAT) is a legitimate protocol used by WebRTC services including Microsoft Teams to traverse NAT-restricted networks via relay servers
- By abusing the Teams TURN relays, attackers blend malicious C2 with normal corporate Teams traffic — defenders see flows to legitimate Microsoft infrastructure
- The technique is genuinely novel as a TTP layer — possible detection-pattern substrate worth elevating to operational template tier

### Victim and timeline

- **Named victim:** "A major U.S. services company" (December 2025 attack)
- BC does NOT identify the company by name
- **No A&D-prime named victim**
- Symantec's full report likely names or anonymizes the victim — direct Symantec retrieval would confirm

### Tradecraft — BYOVD pre-ransomware defense evasion

- BYOVD with four distinct vulnerable / impersonator drivers:
  - **Huawei driver** (vulnerable driver)
  - **Topaz Antifraud driver** (vulnerable driver)
  - **K7 Security driver** (vulnerable driver)
  - **Custom Palo Alto Networks masquerader driver** — impersonates Palo Alto Cortex XDR / Palo Alto driver; distinct tradecraft from generic vulnerable-driver abuse
- BYOVD deployed pre-ransomware-deployment for defense evasion against EDR
- Final-stage ransomware deployment after BYOVD defense evasion

### DragonForce / Scattered Spider linkage (Symantec-asserted; Hard Rule 2 BINDING)

- BC describes DragonForce as "linked to Scattered Spider" per Symantec
- Scattered Spider is on `_roster.yaml` #013 (HIGH threat level)
- DragonForce itself is NOT on `_roster.yaml` as primary or alias
- The Scattered Spider linkage is a Symantec/BC observation, not a roster cross-walk
- **Hard Rule 2 BINDING:** Archimedes does NOT originate the DragonForce/Scattered Spider cross-walk. The linkage is preserved as Symantec's attribution claim only; Archimedes does NOT collapse the two clusters.

### Tradecraft sophistication framing

- Symantec attributes "exceptionally sophisticated cyber tradecraft" to the actors (paraphrased per BC)
- DragonForce active since 2023 per Symantec
- This campaign is one of several DragonForce campaigns observed in 2026

## Attribution discipline (Hard Rule 2 binding)

- Symantec originates the Backdoor.Turn / DragonForce attribution
- Symantec originates the DragonForce / Scattered Spider linkage claim
- **Hard Rule 2 BINDING:** Archimedes records what Symantec says; does NOT originate either claim independently
- DragonForce NOT on `_roster.yaml`; Scattered Spider IS on roster as #013 — Hard Rule 2 prohibits Archimedes from collapsing the two clusters even though Symantec asserts the linkage. The grader/analyst/red-team can record the Symantec-asserted linkage but preserves cluster-identity discipline.

## A&D relevance assessment

- **Direct relevance: LOW.** Victim described as "a major U.S. services company" — sector unspecified, likely commercial services not A&D-prime.
- **TTP-pattern relevance: HIGH.** TURN-relay abuse is broadly applicable across enterprise tenants using Microsoft Teams, including A&D-prime tenants. Detection-pattern substrate worth surfacing as operational template.
- **BYOVD tradecraft relevance: HIGH.** Custom Palo Alto masquerader driver is a tradecraft layer A&D-prime EDR posture defenders should track. Driver-signing-certificate-anomaly detection is universally relevant.

## IOCs surfaced

```yaml
iocs:
  hashes: []
  ips: []
  domains: []
  urls: []
  cves: []

  behavioral_detection_patterns:
    - id: anomalous_teams_turn_relay_traffic_flow
      type: network_anomaly_pattern
      description: "Anomalous TCP/UDP traffic flows to Microsoft Teams TURN relay servers (legitimate Teams uses TURN, so detection is by anomaly rather than blocklist — egress flow analysis with timing/volume anomaly detection)"
      source: "Symantec via BC"
    - id: byovd_huawei_driver_indicator
      type: vulnerable_driver
      value: "Huawei driver"
      description: "BYOVD vulnerable-driver indicator (specific driver name/hash not in BC)"
      source: "Symantec via BC"
    - id: byovd_topaz_antifraud_driver_indicator
      type: vulnerable_driver
      value: "Topaz Antifraud driver"
      description: "BYOVD vulnerable-driver indicator (specific driver name/hash not in BC)"
      source: "Symantec via BC"
    - id: byovd_k7_security_driver_indicator
      type: vulnerable_driver
      value: "K7 Security driver"
      description: "BYOVD vulnerable-driver indicator (specific driver name/hash not in BC)"
      source: "Symantec via BC"
    - id: custom_palo_alto_masquerader_driver
      type: driver_masquerade_pattern
      value: "Custom Palo Alto Networks driver masquerader"
      description: "Impersonates Palo Alto Cortex XDR / Palo Alto driver; distinct tradecraft from generic vulnerable-driver abuse; detection via driver-signing-certificate anomaly"
      source: "Symantec via BC"
    - id: go_based_rat_executable_pattern
      type: malware_family_pattern
      value: "Backdoor.Turn (Go-based RAT)"
      description: "Go-based RAT executable patterns — specific hashes pending direct Symantec retrieval"
      source: "Symantec via BC"

  note: "BC states 'Symantec published a complete indicators of compromise list' — Symantec primary retrieval needed for full IOC table (hashes, IPs, domains, specific driver versions)."
```

## Relationship to existing findings

- **No prior DragonForce Archimedes finding** — net-new cluster identity to corpus (DragonForce not on roster).
- **Related to roster #013 Scattered Spider** (Symantec-asserted linkage only, Hard Rule 2 preserved) — operator-deferred Scattered Spider dossier mutation candidacy if cross-walk operator-approved (separate /update-tracking path).
- **Adjacent precedent class:** novel-cloud-service-abuse-for-C2-obfuscation TTP pattern — comparable to APT37 pCloud dead-drop pattern (finding-2026-06-16-0003 same brief cycle), Mythic / Sliver / Cobalt Strike infrastructure-abuse patterns in prior findings. NOT same cluster, NOT same tradecraft chain.

## Analytic notes (from analyst review)

ACH ranks H1 (DragonForce-as-RaaS + Scattered-Spider-as-affiliate) at zero inconsistencies as the cleanest fit for Symantec's linkage framing. This explanation does NOT require collapsing the two clusters — it accepts them as operationally distinct entities in a business relationship. Industry baseline supports: DragonForce has documented RaaS-affiliate-program structure; Scattered Spider has documented affiliate-cycling history. H2 (operator/toolkit overlap) is co-equal at zero inconsistencies but cannot be operationally distinguished from H1 without granular evidence. H5 (Scattered Spider rebrand) is ruled out at two inconsistencies — vendor taxonomies preserve DragonForce as distinct cluster, and DragonForce's 2023+ history independent of Scattered Spider undermines the rebrand read. Hard Rule 2 binding preserved — even at zero inconsistencies, Archimedes does NOT collapse DragonForce into Scattered Spider on roster.

KAC surfaces eight assumptions; seven qualify, one sound. No blocking tests. The highest-centrality concerns: A1 (TURN-relay-abuse novelty claim — Symantec's prior-art search may have missed security-research-tier prior art outside vendor IR reporting) and A7 (anomalous Teams TURN detection signature has high false-positive risk; defensive utility framing carries operational-deployment qualifier). A4 (Symantec IR observation completeness) is worth flagging — if Symantec engagement started post-compromise, initial-access framing may be inferred not observed. No WEP adjustment recommended. No new red-team escalation. Scattered Spider dossier mutation candidacy substrate-ready for operator-approved /update-tracking; mutation should record DragonForce affiliate relationship context WITHOUT collapsing the cluster identities.

## Open questions for analyst / red-team / actor-profiler

1. **Symantec primary direct retrieval** (collector watch): Retrieve Symantec/Broadcom Threat Hunter Team primary blog for full IOC table, named victim or anonymization, and specific driver versions/hashes.
2. **Independent IR-vendor corroboration watch** (analyst): No Mandiant / CrowdStrike / Unit 42 / MSTIC corroboration of TURN-relay-abuse-by-Backdoor.Turn or DragonForce-Scattered Spider linkage. Independent vendor IR firm corroboration would lift single-source veto.
3. **SAT-ACH on DragonForce / Scattered Spider cluster relationship** (analyst defer): Competing-hypothesis analysis on Symantec-asserted linkage — affiliate relationship / shared toolkit / shared-actor-pattern coincidence / Symantec-misclassification. Hard Rule 2 binding — Archimedes does NOT originate cross-walk; SAT-ACH would assess strength of Symantec's attribution methodology.
4. **SAT-KAC on TURN-relay-abuse novelty claim** (analyst defer): Key-assumptions checklist on "first known malware" framing — what would need to be true for the claim to hold (no prior public reporting of similar pattern); what would need to be true for it to fail (prior research that Symantec missed).
5. **A&D-prime detection-pattern publication** (operator surface): TURN-relay-abuse detection pattern + BYOVD with custom Palo Alto masquerader detection signature worth surfacing as operational-template substrate for A&D-prime EDR posture.
6. **Scattered Spider dossier mutation candidacy** (operator action): If operator approves the Symantec-asserted DragonForce/Scattered Spider cross-walk under separate /update-tracking pathway, dossier mutation would add Backdoor.Turn + TURN-relay-abuse + BYOVD-custom-PAN-masquerade to roster #013 substrate. Hard Rule 2 binding — operator approval required.
