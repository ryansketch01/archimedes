---
id: finding-2026-06-16-0001
finding_id: finding-2026-06-16-0001-eset-fishmonger-sprysocks-windows-win-drv-rootkit-win-plus-print-spooler-prc-nexus-isoon-contractor-not-on-roster-operator-deferred-new-actor
title: "ESET WeLiveSecurity (Martin Smolar byline) primary discloses two previously undocumented Windows variants of SprySOCKS (WIN_DRV kernel-driver rootkit using RawWNPF + DriverLoader; WIN_PLUS Print Spooler-leveraged barebones backdoor) attributed to FishMonger cluster operating under Winnti umbrella per ESET (cross-references Earth Lusca / Aquatic Panda / Bronze University / Charcoal Typhoon / RedHotel — ESET originates cluster identity preservation, Archimedes does NOT cross-walk further per Hard Rule 2); FishMonger assessed by ESET as conducted by Chinese contractor i-Soon active since 2021; victim countries Honduras / Taiwan / Thailand / Pakistan in government foreign-affairs / technology / telecommunications sectors (no A&D-prime named victim); initial access via N-day exploitation of Fortinet / GitLab / Microsoft Exchange / Progress Telerik UI / Zimbra edge appliances (universally A&D-relevant pivot inheritance); possible CVE-2023-24932 Secure Boot bypass / BlackLotus UEFI bootkit involvement per ESET ('limited evidence' qualifier); BleepingComputer (Bill Toulas) + The Hacker News (Ravie Lakshmanan) publisher-independent same-day relays both cite ESET primary; FishMonger / Earth Lusca / Aquatic Panda NOT on 24-actor Archimedes _roster.yaml — operator-deferred /new-actor candidacy stands; single-vendor IR firm on actor-attribution layer (single-source-veto applies on attribution layer); WEP ceiling likely; A&D-relevance via initial-access-pivot-inheritance pattern HIGH (Fortinet/GitLab/Exchange/Telerik/Zimbra universally deployed) plus kernel-driver-detection-pattern + UEFI bootkit detection broadly applicable to A&D Windows endpoint defense"
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
  eset_welivesecurity_primary_direct_url_404_first_attempt_substrate_reconstructed_from_thn_bc_relays: B2
  win_drv_variant_kernel_driver_rootkit_previously_undocumented_windows_variant_of_sprysocks: A2
  win_plus_variant_print_spooler_leveraged_barebones_backdoor_previously_undocumented_windows_variant: A2
  rawwnpf_kernel_driver_file_name_kw1b5206bdc1743fp_dat: A2
  driverloader_separate_loader_binary_kx1b5206bdc1743dd_dat: A2
  tcp_traffic_diversion_via_random_tcp_ports_kernel_layer_evasion: A2
  conceals_network_connections_processes_files_registry_keys_at_kernel_layer: A2
  print_spooler_service_spoolsv_exe_leverage_with_print_processor_vspmsg: A2
  svchost_exe_injection_of_sprysocks_loader: A2
  both_variants_support_30_plus_command_types_tcp_udp_websocket_c2: A2
  dll_based_architecture_loader_main_payload_model: A2
  sprysocks_internally_versioned_v1_8_based_on_windows_rat_trochilus_shares_traits_redleaves: A2
  eset_attributes_fishmonger_cluster_operating_under_winnti_umbrella: A2
  eset_cross_references_earth_lusca_aquatic_panda_bronze_university_charcoal_typhoon_redhotel: A2
  eset_attributes_operations_to_chinese_contractor_isoon_active_since_2021: A2
  hard_rule_2_no_cross_walk_originated_by_archimedes: A1
  fishmonger_earth_lusca_aquatic_panda_bronze_university_charcoal_typhoon_redhotel_isoon_not_on_24_actor_roster: A1
  victim_countries_honduras_taiwan_thailand_pakistan: A2
  victim_sectors_government_foreign_affairs_technology_telecommunications: A2
  no_named_victim_organizations_in_eset_report: A1
  no_ad_prime_named_victim: A1
  operation_fishmedley_2022_predecessor_seven_organizations_taiwan_hungary_turkey_thailand_france_us: A2
  initial_access_n_day_exploitation_fortinet_gitlab_microsoft_exchange_progress_telerik_ui_zimbra: A2
  possible_cve_2023_24932_secure_boot_bypass_blacklotus_uefi_bootkit_involvement: B3
  persistence_scheduled_tasks: A2
  persistence_ifeo_hijacking_targeting_vds_exe: A2
  persistence_windows_print_processor_registration_vspmsg: A2
  sha256_68aec5085599e8a272767f50da66c83a6582e4e16ed97c209f65f81538b0c028_win_drv_main_sample: A2
  no_ip_addresses_in_retrievable_substrate: A1
  no_domains_in_retrievable_substrate: A1
  full_ioc_table_pending_direct_eset_retrieval: A1
  ad_direct_relevance: A1
  ad_relevance_via_initial_access_pivot_inheritance_fortinet_gitlab_exchange_telerik_zimbra: A2
  ad_relevance_kernel_driver_detection_pattern_byovd_rawwnpf_driverloader: A2
  ad_relevance_uefi_bootkit_detection_pattern_cve_2023_24932_blacklotus_secure_boot_bypass: B3
  splunk_first_party_check_invoked_30d_lookback: A1
  splunk_first_party_zero_hits_on_external_indicators: A1
  frank_not_korean_language_environment_not_isoon_attributed_target_country_visibility_bounded_absence: A1
  no_first_party_telemetry_contradiction_or_confirmation_available: A1
  net_new_substrate_win_drv_win_plus_windows_variants_previously_undocumented: A1
  not_under_existing_anti_noise_hold: A1
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / action-tier inclusion).
  ESET WeLiveSecurity is A-grade vendor IR primary per source-grades.yaml
  id `eset`. Primary URL returned 404 on first attempt; substance
  reconstructed from BleepingComputer (Bill Toulas, B) and The Hacker
  News (Ravie Lakshmanan, B) — both publishers independently relay the
  same ESET primary within a 45-minute window and both quote Martin
  Smolar directly.

  WHY B2 NOT A2:
    1. ESET PRIMARY NOT DIRECTLY RETRIEVED — canonical URL 404 first
       attempt; substrate reached through B-grade publisher relays only.
    2. SINGLE-IR-VENDOR ON ATTRIBUTION LAYER — no Mandiant / CrowdStrike
       / Unit 42 / MSTIC corroboration of FishMonger == this campaign.
    3. UEFI bootkit involvement ESET-qualified as "limited evidence" —
       that layer cannot anchor stronger than B3.

  Single-source-veto consideration: ESET stands alone on attribution
  (FishMonger cluster identity preservation; i-Soon contractor
  attribution). THN + BC are publisher-relays, NOT independent evidence
  basis. WEP ceiling caps at "likely" per single-source veto.

  WHY NOT FLASH:
    - T5 (ad-sector-campaign): FAIL — no A&D-prime named victim.
    - T2 (tracked-actor-attribution): FAIL — FishMonger not on roster.
    - T4 (tracked-actor-ttp-change): FAIL — no dossier to mutate.
    - T1 (critical-cve-exploited): MARGINAL — CVE-2023-24932 UEFI
      involvement is "limited evidence."

  HARD RULE 2: PRESERVED. ESET cluster identity stands; NO Archimedes
  cross-walk to APT41 or other roster actors; operator-deferred
  /new-actor candidacy for FishMonger / Earth-Lusca surfaced.

  HARD RULE 6: PRESERVED. One quote per source under 15 words.

  HARD RULE 8: PRESERVED. Splunk first-party check 30-day lookback;
  ZERO external-IOC hits across defenseclaw_local + archimedes. Frank
  not in ESET-named victim country set; silent-Splunk-does-NOT-disconfirm.

source_reliability:
  grade: A
  source_name: "ESET WeLiveSecurity (Martin Smolar byline) via BleepingComputer (Bill Toulas) + The Hacker News (Ravie Lakshmanan) publisher-independent relay"
  source_yaml_id: eset
  grade_rationale: >
    ESET is A-grade per source-grades.yaml id `eset` (vendor IR primary,
    active true). Reached this sweep through THN + BC publisher-relay
    because ESET canonical URL returned 404 first attempt; both
    publishers credit ESET directly and quote Martin Smolar. B2 cluster
    anchor reflects substrate reached via publisher relay rather than
    direct retrieval.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - consistent_with_established_ttps_for_prc_nexus_cyberespionage_clusters
    - no_contradicting_evidence_from_a_or_b_grade_sources
    - technical_claims_internally_coherent
  rationale: >
    Technical claims internally coherent: WIN_DRV/WIN_PLUS architecture
    described with specific file names, kernel driver mechanics, Print
    Spooler service abuse pattern, persistence mechanisms, C2 protocol
    detail. Consistent with established PRC-nexus cyberespionage
    tradecraft. No contradicting A/B-grade source. Two publisher-
    independent relays (BC + THN) within 45-minute window both quote
    Martin Smolar with consistent technical detail. ESET originates
    actor cluster identity — single-IR-vendor on attribution layer;
    would lift to credibility 1 with independent vendor IR firm
    corroboration (Mandiant / CrowdStrike / Unit 42 / MSTIC).

corroboration:
  independent_sources:
    - eset
    - bleepingcomputer
    - thehackernews
  independent: false
  test_passed: >
    BC and THN are publisher-independent of each other but both
    explicitly credit ESET as report origin and quote Martin Smolar.
    Publisher-independent relay of a single A-grade vendor IR primary,
    NOT independent evidence basis. The corroboration test for
    credibility 1 requires DIFFERENT EVIDENCE BASIS — independent
    IR-vendor corroboration (Mandiant / CrowdStrike / Unit 42) would
    constitute different evidence basis on the actor-attribution layer.
  independent_layered:
    eset_vendor_ir_primary: true
    bleepingcomputer_publisher_relay: false
    thehackernews_publisher_relay: false

first_party_precedence:
  applied: true
  splunk_evidence:
    query_executed: "search index=archimedes OR index=defenseclaw_local (FishMonger OR SprySOCKS OR RawWNPF OR KW1B5206BDC1743FP OR KX1B5206BDC1743DD OR i-Soon OR \"Earth Lusca\") earliest=-30d"
    hits_on_external_indicators: 0
    note: >
      30-day lookback. ZERO hits on external indicators across
      defenseclaw_local + archimedes. The 16 hits returned are
      Archimedes' own operational meta-logging events. Frank is NOT a
      Korean-language environment, not in ESET-named victim country set
      (Honduras / Taiwan / Thailand / Pakistan), and not running
      publicly-exposed Fortinet / GitLab / Exchange / Telerik / Zimbra
      edge appliances at A&D-prime scale visible to Archimedes sentinel.
      Visibility-bounded absence flagged per Hard Rule 8 binding —
      silent-Splunk-does-NOT-disconfirm. ESET vendor IR primary
      attestation stands.

single_source_veto_applied: true
single_source_veto_layers:
  - eset_only_on_fishmonger_cluster_attribution_and_isoon_contractor_attribution_no_independent_ir_vendor_corroboration
  - eset_only_on_win_drv_win_plus_windows_variant_existence_no_independent_ir_vendor_telemetry
wep_ceiling: likely

cluster:
  topic: "ESET FishMonger SprySOCKS Windows variants (WIN_DRV + WIN_PLUS) — PRC-nexus i-Soon contractor attribution, government foreign-affairs / tech / telecom victims across Honduras / Taiwan / Thailand / Pakistan, N-day edge-appliance initial access"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-16-am-001-eset-fishmonger-sprysocks-windows-prc-nexus-government-foreign-affairs-net-new-tooling
  attribution_claims:
    - claimed_actor: "FishMonger (Winnti umbrella; cross-references Earth Lusca / Aquatic Panda / Bronze University / Charcoal Typhoon / RedHotel; i-Soon Chinese contractor)"
      claimed_by_sources: [eset]
      requires_analyst_review: true
      note: "ESET originates cluster identity preservation; Hard Rule 2 binding — NO Archimedes cross-walk. Operator-deferred /new-actor candidacy stands. Analyst review flagged for SAT-ACH."

inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
  not_eligible_for:
    - flash
    - actor_profile_update

analyst_review_required: true
analyst_review_status: complete
analyst_review_completed_at: 2026-06-16T08:30:00-04:00
analyst_review_run_id: analyst-20260616-083000
red_team_review_required: false
red_team_review: null
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Does ESET's attribution of the WIN_DRV + WIN_PLUS SprySOCKS Windows variants to the FishMonger cluster (i-Soon contractor under Winnti umbrella) hold against alternative explanations that the toolkit is shared across multiple PRC-nexus clusters operating under common contractor / quartermaster infrastructure?"
      analyzed_at: 2026-06-16T08:30:00-04:00
      analyzed_by: analyst
      red_team_review: null

      hypotheses:
        - id: H1
          statement: "ESET's attribution holds: FishMonger (i-Soon contractor cluster) developed and operated WIN_DRV + WIN_PLUS as proprietary tooling for this 2023-2024 campaign."
        - id: H2
          statement: "WIN_DRV + WIN_PLUS are shared PRC-quartermaster toolkit deployed by FishMonger AND other Winnti-umbrella clusters (Earth Lusca / Aquatic Panda / Bronze University / Charcoal Typhoon / RedHotel); ESET observed a FishMonger deployment but the toolkit is not exclusive."
        - id: H3
          statement: "ESET's cluster boundary is too narrow: the 'FishMonger' label conflates multiple distinct activity sets sharing initial-access tradecraft (N-day edge appliance pivots) but operationally separate beyond initial access — the SprySOCKS variants belong to a sub-cluster, not the full FishMonger identity."
        - id: H4
          statement: "Null / surprise hypothesis: the toolkit is not exclusively PRC-nexus — it's a commodity rootkit framework (SprySOCKS lineage from Windows RAT Trochilus per ESET's own framing) being adopted by multiple actors and ESET's FishMonger attribution rests on initial-access TTP overlap with prior FishMonger activity rather than on toolkit exclusivity."
        - id: H5
          statement: "Misattribution: a different PRC actor deliberately reused FishMonger-class initial-access tradecraft to misdirect attribution; ESET is reading the surface tradecraft correctly but the operator is not the historical FishMonger."

      evidence:
        - id: E1
          description: "ESET attributes campaign to FishMonger under Winnti umbrella with cross-references to Earth Lusca / Aquatic Panda / Bronze University / Charcoal Typhoon / RedHotel; ESET assesses operations conducted by Chinese contractor i-Soon active since 2021"
          source: eset_via_thn_bc
          digraph: A2
          weight: 3
        - id: E2
          description: "Two previously-undocumented Windows variants (WIN_DRV kernel-driver rootkit using RawWNPF + DriverLoader; WIN_PLUS Print Spooler-leveraged barebones backdoor) with internally-coherent technical architecture (DLL-based loader/main payload model, 30+ command types, TCP/UDP/WebSocket C2)"
          source: eset_via_thn_bc
          digraph: A2
          weight: 3
        - id: E3
          description: "SprySOCKS internally versioned v1.8; based on Windows RAT Trochilus; shares traits with RedLeaves — i.e., the malware lineage is publicly-documented PRC-ecosystem code with multi-actor precedent"
          source: eset_via_thn_bc
          digraph: A2
          weight: 3
        - id: E4
          description: "Initial access via N-day exploitation of Fortinet / GitLab / Microsoft Exchange / Progress Telerik UI / Zimbra edge appliances — broadly-shared PRC-nexus initial-access pattern across multiple Winnti-umbrella clusters"
          source: eset_via_thn_bc
          digraph: A2
          weight: 3
        - id: E5
          description: "Victim countries Honduras / Taiwan / Thailand / Pakistan in government foreign-affairs / technology / telecommunications sectors; no A&D-prime named victim. Targeting pattern consistent with FishMonger's documented Operation FishMedley 2022 predecessor (Taiwan/Hungary/Turkey/Thailand/France/US, seven orgs)"
          source: eset_via_thn_bc
          digraph: A2
          weight: 3
        - id: E6
          description: "No independent IR vendor corroboration (Mandiant / CrowdStrike / Unit 42 / MSTIC) of the FishMonger == i-Soon contractor == WIN_DRV/WIN_PLUS operator chain"
          source: corroboration_gap
          digraph: A1
          weight: 3
        - id: E7
          description: "Possible CVE-2023-24932 / BlackLotus UEFI bootkit involvement — ESET explicitly qualifies as 'limited evidence'; not asserted as confirmed deployment"
          source: eset_via_thn_bc
          digraph: B3
          weight: 1
        - id: E8
          description: "First-party Splunk telemetry: 30-day lookback, zero hits across defenseclaw_local + archimedes on FishMonger / SprySOCKS / RawWNPF / KW1B5206BDC1743FP / KX1B5206BDC1743DD / i-Soon / Earth Lusca. Frank not in ESET-named victim country set; visibility-bounded absence"
          source: splunk_negative_search
          digraph: A1
          weight: 3

      matrix:
        E1: {H1: C, H2: C, H3: N, H4: I, H5: I}
        E2: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E3: {H1: N, H2: C, H3: C, H4: C, H5: C}
        E4: {H1: C, H2: C, H3: C, H4: N, H5: C}
        E5: {H1: C, H2: C, H3: N, H4: N, H5: N}
        E6: {H1: I, H2: N, H3: N, H4: N, H5: N}
        E7: {H1: N, H2: N, H3: N, H4: N, H5: N}
        E8: {H1: N, H2: N, H3: N, H4: N, H5: N}

      inconsistency_counts:
        H1: 1
        H2: 0
        H3: 0
        H4: 1
        H5: 1

      diagnostic_evidence:
        - E1: "ESET's attribution methodology is diagnostic against H4 (null/commodity) and H5 (misattribution) — both require ESET to be making a methodological error. E1 is the load-bearing evidence."
        - E3: "Trochilus/RedLeaves lineage is diagnostic against H1 (exclusive FishMonger ownership) — the lineage of the codebase points toward shared-ecosystem origin, weakly favoring H2/H3."
        - E6: "Absence of corroboration is diagnostic against H1 (which would predict that multiple A-grade vendors converge on the same attribution) and weakly favors H2/H3 (consistent with single-vendor cluster-boundary observation)."

      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: "Zero inconsistencies. SprySOCKS lineage (Trochilus/RedLeaves) and ESET's own umbrella framing (Winnti, with five cross-referenced cluster aliases) are positively consistent with toolkit sharing across Winnti-umbrella clusters. Does NOT contradict ESET's FishMonger attribution — it accepts that FishMonger deployed the variants but does not assert FishMonger-exclusive ownership."
          wep: likely
        - rank: 2
          hypothesis_id: H3
          rationale: "Zero inconsistencies. Cluster-boundary critique is consistent with the standard PRC-actor methodology problem (Mandiant / CrowdStrike / Microsoft all maintain different cluster taxonomies that overlap inconsistently with ESET's). Cannot be distinguished from H2 on current evidence."
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H1
          rationale: "One inconsistency (E6). H1 is what ESET asserts and what the substrate would most naturally be read as if no corroboration question existed. ESET's track record on PRC-nexus attribution is strong. Held back by single-vendor evidence basis — the assessment is brittle to ESET being wrong on cluster boundaries."
          wep: likely
        - rank: 4
          hypothesis_id: H4
          rationale: "One inconsistency (E1). Commodity-rootkit framing is undermined by ESET's specific FishMonger attribution and consistent prior FishMonger reporting pattern. Possible but requires assuming ESET methodology error."
          wep: unlikely
        - rank: 5
          hypothesis_id: H5
          rationale: "One inconsistency (E1). False-flag/misdirection hypotheses against vendor-IR-firm attribution typically require additional positive evidence (the misdirector's fingerprints) which is absent."
          wep: very_unlikely

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E1, E6]
        if_E1_methodology_questioned: "H2/H3 rise; H1 falls below H2 in ranking. Cluster identity becomes openly contested."
        if_independent_ir_vendor_corroborates_e6_closes: "H1 inconsistency closes; H1 rises to tie with H2 or surpass it depending on the corroborating vendor's cluster boundaries."
        if_eset_primary_directly_retrieved_with_full_ioc_table: "Granular IOCs would either reinforce H1 (specific FishMonger infrastructure overlap) or weaken it (overlap with non-FishMonger Winnti-umbrella infrastructure)."
        single_point_of_failure: "ESET's cluster-boundary methodology. If FishMonger as a cluster is internally inconsistent across ESET's own prior reporting, the whole attribution layer weakens."

      tripwires:
        - observation: "Independent IR vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC) publishes corroborating attribution of WIN_DRV/WIN_PLUS to the same cluster"
          effect: "H1 inconsistency E6 closes; promote H1 to lead. WEP ceiling lifts toward very_likely on attribution layer."
        - observation: "Independent IR vendor attributes WIN_DRV/WIN_PLUS to a DIFFERENT cluster (e.g., APT41-as-Mandiant-defines-it or a Microsoft Typhoon designation)"
          effect: "H3 rises; cluster-boundary disagreement becomes the lede. ESET's FishMonger framing must be reported as one of two competing vendor cluster identities."
        - observation: "WIN_DRV / WIN_PLUS samples surface in a victim outside ESET's named cluster pattern (e.g., a clearly RedHotel-attributed victim or APT41-attributed victim per separate vendor)"
          effect: "H2 confirmed via positive evidence. WEP lifts on toolkit-sharing claim."
        - observation: "ESET primary URL becomes directly retrievable; full IOC table available"
          effect: "Re-run ACH with granular infrastructure evidence; sensitivity drops."
        - observation: "First-party Splunk hit on RawWNPF / DriverLoader file-name pattern or SHA256 68aec5085599e8a272767f50da66c83a6582e4e16ed97c209f65f81538b0c028"
          effect: "Hard Rule 8 binding — first-party precedence; rerun ACH with first-party telemetry weighting."

      conclusion:
        summary: |
          ESET's attribution holds AS ESET STATES IT — i.e., FishMonger deployed
          the WIN_DRV + WIN_PLUS variants. The ACH does NOT support a stronger
          claim that FishMonger exclusively owns the toolkit. H2 (Winnti-umbrella
          shared quartermaster) has zero inconsistencies and is positively
          consistent with the SprySOCKS lineage (Trochilus / RedLeaves shared
          ecosystem) and ESET's own umbrella framing. Reporting the attribution
          as "FishMonger per ESET" is correct; reporting it as "FishMonger
          exclusively" overreaches. Cluster-boundary discipline matters here —
          Archimedes does NOT cross-walk to APT41 / Volt Typhoon / Salt Typhoon
          per Hard Rule 2, but the analyst notes that the toolkit-sharing
          hypothesis (H2) is co-equal with the ESET-attribution hypothesis (H1)
          on current evidence.
        wep: likely
        confidence_caveats: |
          Single-vendor evidence basis on attribution layer (E6) is the binding
          constraint. WEP at "likely" matches the grader's single-source veto
          assessment. Brief should present FishMonger attribution as ESET's
          claim, not as Archimedes-confirmed. Operator-deferred /new-actor
          candidacy substrate-ready but should carry "ESET cluster boundary
          subject to independent vendor corroboration" qualifier in any
          actor-profiler scaffold per Hard Rule 5 pathway.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "ESET's FishMonger cluster identity is stable across the N-day-edge-
        appliance access pattern shared with multiple PRC-nexus clusters; the
        WIN_DRV + WIN_PLUS Windows variants are FishMonger-deployed tooling
        attributable to the i-Soon contractor active since 2021."
      analyzed_at: 2026-06-16T08:30:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-brief analyst review on grader-deferred attribution-cluster-identity-preservation-vs-cross-walk plus UEFI-bootkit-limited-evidence layers"

      assumptions:
        - id: A1
          statement: "ESET's cluster boundary for FishMonger is internally consistent across ESET's own reporting (i.e., FishMonger in 2026 is the same activity set ESET called FishMonger in 2022 Operation FishMedley)"
          category: source_reliability
          stated: false
          why_must_be_true: "Assessment treats 'FishMonger' as a coherent referent; if ESET's own cluster boundary has drifted, the attribution loses meaning"
          when_could_be_false: "ESET's cluster taxonomy has evolved (industry-standard problem — Mandiant, CrowdStrike, Microsoft all revise cluster boundaries); FishMonger 2026 may be operationally distinct from FishMonger 2022"
          evidence_for: [eset_operation_fishmedley_2022_predecessor_substrate]
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A2
          statement: "The i-Soon contractor attribution is reliable (i.e., the activity is operated by i-Soon personnel/infrastructure, not just consistent with i-Soon tradecraft)"
          category: actor_continuity
          stated: true
          why_must_be_true: "ESET's framing distinguishes 'FishMonger conducted by i-Soon contractor' from a more cautious 'FishMonger displays i-Soon-consistent tradecraft'"
          when_could_be_false: "i-Soon as a contractor entity could be servicing multiple PRC IS/MSS handlers under different cluster identities; FishMonger could be one of several i-Soon brand identities; or i-Soon's leaked materials (2024 i-Soon leak) could be informing ESET's attribution methodology in ways that don't strictly correspond to direct infrastructure ownership"
          evidence_for: [eset_high_confidence_framing_substrate]
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A3
          statement: "The Winnti-umbrella framing is a meaningful organizing concept, not just a label for 'PRC-nexus clusters that share some tradecraft elements'"
          category: semantic
          stated: true
          why_must_be_true: "ESET's cross-references to Earth Lusca / Aquatic Panda / Bronze University / Charcoal Typhoon / RedHotel under Winnti umbrella implicitly assume umbrella coherence"
          when_could_be_false: "Winnti is a well-known fuzzy umbrella in vendor taxonomy — Kaspersky, ESET, Mandiant, CrowdStrike all use 'Winnti' with somewhat different boundaries; umbrella may not correspond to a single PRC handling structure"
          evidence_for: []
          evidence_against: [vendor_taxonomy_divergence_widely_documented]
          confidence: low
          centrality: peripheral
          classification: qualify
        - id: A4
          statement: "N-day exploitation of Fortinet / GitLab / Exchange / Telerik / Zimbra edge appliances is distinctive enough to indicate FishMonger operatorship (vs being a broadly-shared PRC initial-access pattern)"
          category: ttp_patterns
          stated: false
          why_must_be_true: "ESET's framing uses this initial-access pattern as part of the FishMonger identity"
          when_could_be_false: "This initial-access pattern is documented across multiple PRC-nexus clusters per Mandiant / CISA / Volexity reporting since 2022 — N-day edge-appliance pivots are common practice across APT41 / Volt Typhoon-class / Salt Typhoon-class actors"
          evidence_for: [eset_initial_access_chain_documented]
          evidence_against: [n_day_edge_appliance_pattern_shared_across_prc_nexus_clusters_industry_consensus]
          confidence: low
          centrality: critical
          classification: test
        - id: A5
          statement: "SprySOCKS / WIN_DRV / WIN_PLUS code lineage from Trochilus and RedLeaves does NOT undermine FishMonger ownership — i.e., the actor took commodity-RAT code and made it their own"
          category: technology
          stated: false
          why_must_be_true: "If commodity-code adoption is the dominant explanation, attribution to FishMonger requires non-code evidence (infrastructure overlap, victim selection, operational tempo)"
          when_could_be_false: "Trochilus and RedLeaves have been available in PRC-nexus ecosystem for multiple years; any actor with access to that lineage could produce a similar variant"
          evidence_for: []
          evidence_against: [trochilus_redleaves_shared_lineage_eset_acknowledges]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "CVE-2023-24932 / BlackLotus UEFI bootkit involvement is real, not a methodology artifact"
          category: technology
          stated: true
          why_must_be_true: "ESET's 'limited evidence' qualifier preserves the possibility but does not assert; finding's WIN_DRV layer attribution does NOT depend on UEFI involvement"
          when_could_be_false: "ESET's 'limited evidence' could downgrade further if additional samples surface without UEFI artifacts; or upgrade if direct bootkit deployment is confirmed"
          evidence_for: [eset_limited_evidence_qualifier_substrate]
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: qualify
        - id: A7
          statement: "First-party Splunk silence (zero hits on -30d lookback) is not negative evidence against FishMonger activity in Frank's environment — Frank's profile does not match the ESET-named victim countries"
          category: visibility
          stated: true
          why_must_be_true: "Hard Rule 8 binding — silent-Splunk-does-NOT-disconfirm when first-party visibility doesn't intersect with the named campaign pattern"
          when_could_be_false: "If a future campaign extension to US A&D primes occurred and Splunk still showed no hits, visibility-bounded-absence interpretation would weaken"
          evidence_for: [hard_rule_8_doctrine, frank_profile_not_korean_language_environment_not_isoon_named_victim_country]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound

      classifications_summary:
        sound: 1
        qualify: 5
        test: 1
        reject: 0

      remediation:
        status: proceed
        qualifying_caveats:
          - "FishMonger cluster identity is preserved as ESET's framing; Archimedes does NOT collapse or extend it (Hard Rule 2 binding)"
          - "i-Soon contractor attribution is reported as ESET's claim; the assumption that this represents direct operational ownership (vs tradecraft-consistency-based inference) is single-vendor and weakly supported"
          - "Winnti-umbrella framing carries vendor-taxonomy divergence risk; brief should report umbrella as ESET's organizing concept, not as established cross-vendor consensus"
          - "WIN_DRV/WIN_PLUS code lineage (Trochilus/RedLeaves) suggests shared-ecosystem origin compatible with toolkit sharing across Winnti-umbrella clusters per ACH H2"
          - "UEFI bootkit involvement preserves ESET's 'limited evidence' qualifier; not asserted as confirmed"
        test_required: "A4 (N-day edge-appliance pattern distinctiveness) cannot be resolved within Archimedes substrate. Test would require: (a) cross-vendor survey of which PRC-nexus clusters have been documented using the same five-product N-day chain since 2023, OR (b) independent IR vendor publishing a corroborating WIN_DRV/WIN_PLUS attribution that names the same initial-access products. NOT BLOCKING for this morning's brief (WEP already capped at 'likely' which matches the assumption set); NOTED for /new-actor scaffolding work if operator invokes the pathway."
        next_action: "Proceed to brief at WEP 'likely' with the five qualifying caveats explicit. Defer the A4 test to /new-actor pathway."

      recommended_wep_after_test:
        if_independent_corroboration_arrives: "WEP holds at likely or rises to very_likely depending on corroborating vendor's framing"
        if_a4_test_fails_widely_shared_pattern: "WEP drops to roughly_even_chance on FishMonger-as-operator layer; attribution restated as 'ESET attributes to FishMonger; pattern not exclusive to cluster'"
        if_eset_primary_retrievable: "Marginal upward pressure on WEP; sensitivity analysis re-run with granular IOCs"

new_actor_candidacy_handoff:
  proposed_actor: "FishMonger"
  alternative_names: ["Earth Lusca", "Aquatic Panda", "Bronze University", "Charcoal Typhoon", "RedHotel"]
  attributed_to: "Chinese contractor i-Soon per ESET"
  primary_substrate: "ESET WeLiveSecurity 2026-06-16 (Martin Smolar byline)"
  not_on_roster: true
  operator_action_required: "/new-actor FishMonger (or /new-actor Earth-Lusca) to scaffold dossier; actor-profiler subagent handles per Hard Rule 5"

tlp: CLEAR
published_in_briefs:
  - 2026-06-16-morning
retracted: false
retraction_brief_id: null
---

# ESET WeLiveSecurity: FishMonger cluster Windows-variant SprySOCKS arsenal (WIN_DRV kernel-driver rootkit + WIN_PLUS Print Spooler backdoor) — i-Soon contractor attribution, government foreign-affairs/tech/telecom victims, N-day edge-appliance initial access

## Summary

ESET researchers (Martin Smolar byline) disclosed two previously undocumented Windows variants of the SprySOCKS backdoor — internally tagged **WIN_DRV** (kernel-driver rootkit using RawWNPF + a separate DriverLoader binary) and **WIN_PLUS** (a barebones backdoor that leverages the Windows Print Spooler service via print processor VSPMsg). ESET attributes the campaign to the **FishMonger** cluster operating under the broader **Winnti umbrella**, with cross-references to Earth Lusca / Aquatic Panda / Bronze University / Charcoal Typhoon / RedHotel; ESET assesses operations are conducted by Chinese contractor **i-Soon**, active since at least 2021. Confirmed Windows-variant deployments 2023-2024 hit government foreign-affairs, technology, and telecommunications targets in Honduras, Taiwan, Thailand, and Pakistan — **no A&D-prime named victim**. Initial access is via N-day exploitation of Fortinet, GitLab, Microsoft Exchange, Progress Telerik UI, and Zimbra edge appliances (universally A&D-relevant pivot inheritance pattern). ESET notes possible CVE-2023-24932 / BlackLotus-pattern UEFI bootkit involvement with a "limited evidence" qualifier — not asserted as confirmed deployment. The cluster is single-IR-vendor on the attribution layer; WEP ceiling caps at "likely" per single-source veto; independent vendor IR corroboration (Mandiant / Unit 42 / CrowdStrike / MSTIC) would lift the veto. FishMonger / Earth Lusca / Aquatic Panda is NOT on the 24-actor Archimedes roster — operator-deferred /new-actor candidacy stands per Hard Rule 5.

## Sources

### ESET WeLiveSecurity (source_yaml_id: eset, digraph: A) — PRIMARY

- URL: https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/
- Published: 2026-06-16
- Byline: Martin Smolar
- Direct retrieval this sweep: 404 first attempt; substance reconstructed from THN + BC relays
- Key claim: Two previously undocumented Windows variants of SprySOCKS; FishMonger cluster attribution under Winnti umbrella with i-Soon contractor framing

### BleepingComputer (source_yaml_id: bleepingcomputer, digraph: B)

- URL: https://www.bleepingcomputer.com (Bill Toulas byline)
- Published: 2026-06-16T09:00:00Z
- Key claim: Publisher-independent relay of ESET primary; adds granular C2 protocol detail and Operation FishMedley historical context

### The Hacker News (source_yaml_id: thehackernews, digraph: B)

- URL: https://thehackernews.com (Ravie Lakshmanan byline)
- Published: 2026-06-16T09:44:34Z
- Key claim: Publisher-independent relay of ESET primary; adds explicit i-Soon attribution and CVE-2023-24932 framing

## Technical detail

### WIN_DRV variant (rootkit-class)

- Kernel driver **RawWNPF** (file name `KW1B5206BDC1743FP.dat`)
- Loaded via separate loader binary **DriverLoader** (`KX1B5206BDC1743DD.dat`)
- TCP traffic diversion — operators send commands through random TCP ports
- Conceals network connections, processes, files, and registry keys at kernel layer

### WIN_PLUS variant (barebones backdoor)

- Leverages Windows **Print Spooler service** (`spoolsv.exe`)
- Uses print processor as initial execution point (`VSPMsg`)
- Injects SprySOCKS loader into `svchost.exe`
- First detected July 2024 in a Pakistan victim

### Common architecture

- 30+ command types covering system enumeration, process management, service operations, file system access
- C2 via TCP, UDP, WebSocket protocols
- DLL-based architecture; loader → main payload model
- SprySOCKS internally versioned v1.8; based on Windows RAT Trochilus; shares traits with RedLeaves

### Persistence

- Scheduled tasks
- IFEO hijacking targeting `vds.exe`
- Windows Print Processor registration (`VSPMsg`)

### Initial access vector (per ESET)

- N-day exploitation of **Fortinet, GitLab, Microsoft Exchange, Progress Telerik UI, Zimbra** edge appliances

### Possible UEFI bootkit involvement (limited-evidence qualifier per ESET)

- Possible exploitation of **CVE-2023-24932** (Windows Boot Manager Security Feature Bypass; BlackLotus association)
- ESET does NOT assert confirmed UEFI bootkit deployment — "limited evidence" qualifier preserved

## Attribution discipline (Hard Rule 2 binding)

ESET originates cluster identity preservation:

- **Cluster name:** FishMonger
- **Umbrella framing:** Winnti
- **Cross-references:** Earth Lusca, Aquatic Panda, Bronze University, Charcoal Typhoon, RedHotel
- **Contractor attribution:** Chinese contractor i-Soon, active since at least 2021

**Archimedes does NOT cross-walk further.** Per Hard Rule 2, ESET cluster identity stands. NO Archimedes assertion that FishMonger == APT41 == Winnti Group at any rigorous level. APT41 (#019 on roster) carries Winnti as a listed alias but APT41 is a distinct cluster identity per Mandiant lineage; ESET's FishMonger framing does NOT collapse the two. The 24-actor `_roster.yaml` cohort does NOT include FishMonger, Earth Lusca, Aquatic Panda, Bronze University, Charcoal Typhoon, RedHotel, or i-Soon.

Operator-deferred /new-actor candidacy: if operator invokes `/new-actor FishMonger` (or `/new-actor Earth-Lusca`), actor-profiler scaffolds dossier with this ESET primary as foundation.

## A&D relevance assessment

- **Direct relevance: NONE.** No A&D-prime named victim.
- **Structural relevance via initial-access-pivot-inheritance: HIGH.** Fortinet / GitLab / Exchange / Telerik / Zimbra universally deployed in A&D-prime tenants and DIB supply-chain estates.
- **Kernel-driver-detection-pattern relevance: HIGH.** RawWNPF + DriverLoader BYOVD/rootkit detection signatures universally relevant.
- **UEFI bootkit detection-pattern relevance: HIGH (tied to limited-evidence qualifier).** CVE-2023-24932 / BlackLotus-pattern detection universally relevant on A&D Windows fleets running Secure Boot.

## IOCs surfaced

```yaml
iocs:
  hashes:
    - id: sprysocks_win_drv_main_sample
      type: sha256
      value: "68aec5085599e8a272767f50da66c83a6582e4e16ed97c209f65f81538b0c028"
      description: "WIN_DRV main sample (per THN VirusTotal link via ESET primary)"
      source: "ESET via THN"

  file_names:
    - id: rawwnpf_kernel_driver
      type: file_name
      value: "KW1B5206BDC1743FP.dat"
      description: "RawWNPF kernel driver"
    - id: driverloader_loader_binary
      type: file_name
      value: "KX1B5206BDC1743DD.dat"
      description: "DriverLoader"

  persistence_artifacts:
    - id: vds_exe_ifeo_hijack
      type: registry_key_pattern
      description: "IFEO hijacking targeting vds.exe"
    - id: vspmsg_print_processor_registration
      type: print_processor
      value: "VSPMsg"
    - id: scheduled_task_persistence
      type: scheduled_task_pattern

  cves:
    - id: CVE-2023-24932
      type: cve
      product: "Windows Boot Manager"
      cvss: 6.7
      description: "Windows Boot Manager Security Feature Bypass; BlackLotus UEFI bootkit association; ESET notes POSSIBLE involvement with limited-evidence qualifier"
      source: "ESET (limited-evidence qualifier)"

  initial_access_appliance_families:
    - "Fortinet (N-day)"
    - "GitLab (N-day)"
    - "Microsoft Exchange (N-day)"
    - "Progress Telerik UI (N-day)"
    - "Zimbra (N-day)"

  ips: []
  domains: []
  urls: []

  note: "Full IOC table pending direct ESET retrieval — THN/BC relays do not enumerate."
```

## Relationship to existing findings

- **No prior FishMonger / Earth Lusca / Aquatic Panda / i-Soon Archimedes finding** — net-new cluster identity to corpus.
- **Adjacent precedent class (NOT cross-walk per Hard Rule 2):** Velvet Ant / Operation Highland (Sygnia primary) finding-2026-06-15-0007 — same broad class (PRC patient long-dwell), different cluster.
- **Adjacent precedent class (NOT cross-walk):** UNC6508 / INFINITERED (GTIG primary) finding-2026-06-15-flash1200-0006 — same broad class (PRC-nexus espionage against research targets), different victim set and tradecraft chain.

## Analytic notes (from analyst review)

ACH pressure-tests ESET's FishMonger attribution against four alternatives: shared Winnti-umbrella quartermaster toolkit (H2), narrower sub-cluster boundary (H3), commodity-rootkit adoption (H4), and false-flag misdirection (H5). H2 and H1 (ESET's claim) both land at zero meaningful inconsistencies, with H2 actually scoring better given E6 (single-vendor evidence basis). The SprySOCKS lineage from Trochilus and RedLeaves is internally consistent with shared-ecosystem origin and weakly favors H2 over a FishMonger-exclusive read. The brief should present FishMonger as ESET's framing, not as Archimedes-confirmed exclusive ownership — toolkit sharing across Winnti-umbrella clusters is the equally-plausible alternative on current evidence.

KAC surfaces seven assumptions; five qualify, one tests, one sound. The load-bearing concerns are A2 (i-Soon as direct operator vs tradecraft-consistent inference) and A4 (N-day edge-appliance pattern distinctiveness — well-documented as shared across PRC-nexus clusters since 2023). A4 is flagged as TEST but is not blocking for morning-brief WEP 'likely' which already accommodates the assumption set. Single-vendor evidence basis is the binding constraint; the grader's WEP capping at 'likely' matches the analyst's read. No WEP adjustment recommended. No new red-team escalation — finding remains at WEP 'likely' below the very_likely red-team threshold. The five qualifying caveats from KAC should be visible in any /new-actor FishMonger scaffolding work.

## Open questions for analyst / red-team / vuln-tracker / actor-profiler

1. **ESET primary direct retrieval** (collector watch): URL 404 first attempt. Re-attempt next sweep.
2. **Independent IR-vendor corroboration watch** (analyst): No Mandiant / CrowdStrike / Unit 42 / MSTIC corroboration. Independent vendor IR firm corroboration would lift single-source veto.
3. **/new-actor FishMonger candidacy** (operator action): Substrate ready for actor-profiler scaffold per Hard Rule 5.
4. **SAT-ACH on attribution layer** (analyst defer): Competing-hypothesis analysis on cluster identity preservation vs cross-walk candidacy.
5. **SAT-KAC on UEFI bootkit involvement layer** (analyst defer): Key-assumptions checklist on "limited evidence" qualifier.
6. **N-day edge-appliance defensive posture audit** (operator surface): A&D-prime tenants should audit Fortinet / GitLab / Exchange / Telerik / Zimbra patch state.
