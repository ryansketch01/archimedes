---
id: finding-2026-06-15-0007
finding_id: finding-2026-06-15-0007-helpnetsecurity-sygnia-velvet-ant-operation-highland-direct-retrieval-9-pam-variants-ssspl-socks5-gs-netcat-update-on-finding-2026-06-12-0004
title: "UPDATE on finding-2026-06-12-0004 — HelpNet Security (Zeljka Zorz B-grade publisher relay) covers Sygnia 'Operation Highland' primary post (2026-06-08, 21-minute deep dive, directly retrievable this sweep) on Velvet Ant nearly-decade-long China-nexus authentication-stack backdoor campaign; net-new substrate vs THN-2026-06-12 prior relay: (1) 9 distinct _pam_unix.so_ variants each compiled in separate environment (specific count enumerated this surface vs prior 'nine PAM module variants' framing); (2) custom 'ssspl' SOCKS5 proxy tunneling implementation (NET-NEW tool-name); (3) modified GS-Netcat utility for reverse shell (NET-NEW tool-name); (4) modified Nginx configurations + custom SSH-triggering binary (NET-NEW infrastructure detail); (5) Sygnia primary now directly retrievable resolves prior `awaiting_direct_retrieval` flag on sygnia-research source ID; HelpNet adds independent B-grade publisher relay (vs THN-2026-06-12 single-publisher); Hard Rule 2 preserved (Sygnia attribution remains 'China-nexus' / 'China-linked'; NO cross-walk to APT41 / Volt Typhoon / Salt Typhoon / APT40 / UNC6508); Velvet Ant NOT on 24-actor _roster.yaml (operator-deferred /new-actor candidacy substrate-strengthening); NO US A&D-prime direct victim named (Sygnia primary did NOT disclose victim sector/country in HelpNet relay; structural detection-engineering relevance only)"
date: 2026-06-15
created_at: 2026-06-15T16:14:00-04:00
graded_by: grader
grading_run_id: afternoon-20260615-160000
grading_mode: scheduled_brief
test: false
status: graded
update_type: layered_update
updates_finding: finding-2026-06-12-0004-thn-sygnia-velvet-ant-pam-openssh-backdoor-china-nexus-10-year-dwell-east-asia-new-actor-candidate-detection-engineering-rich

# ============================================================================
# Core grading (admiralty-grading skill output) — UPDATE LAYER
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- VENDOR RESEARCH LAYER (Sygnia primary now directly retrievable) ----
  sygnia_primary_blog_directly_retrievable_this_sweep_operation_highland_2026_06_08: A2  # Procedural success per pre-flash sentinel — Sygnia primary post-level retrieval confirmed
  sygnia_provisional_b_per_source_grades_yaml_since_2026_06_12_via_finding_0004: B2  # Carry-forward provisional grade
  helpnet_security_zeljka_zorz_independent_publisher_relay: B2  # HelpNet ratified B; second publisher independent from THN (06-12)
  publisher_independence_helpnet_vs_thn_06_12_satisfied: A2  # Two B-grade independent publishers + vendor primary directly retrievable = three-source convergence vs single-publisher 06-12 surface
  # ---- NET-NEW TTP DETAIL LAYER ----
  nine_distinct_pam_unix_so_variants_each_compiled_in_separate_environment: B2  # Sygnia primary via HelpNet relay; specific count + per-environment-compilation detail
  custom_ssspl_socks5_proxy_implementation_NET_NEW_TOOL_NAME: B2  # Sygnia primary via HelpNet — net-new tool-name not in 06-12 substrate
  modified_gs_netcat_utility_for_reverse_shell_to_c2_NET_NEW_TOOL_NAME: B2  # Sygnia primary via HelpNet — net-new tool-name
  modified_nginx_configurations_NET_NEW_INFRASTRUCTURE_DETAIL: B2  # Sygnia primary via HelpNet
  custom_ssh_triggering_binary_NET_NEW_INFRASTRUCTURE_DETAIL: B2  # Sygnia primary via HelpNet
  hardcoded_password_bypass_plus_silent_credential_logging_pam_function_layer: B2  # Sygnia primary via HelpNet
  modified_ssh_binaries_capture_incoming_and_outgoing_credentials: B2  # Sygnia primary via HelpNet
  encrypted_storage_with_filesystem_obfuscation: B2  # Sygnia primary via HelpNet
  authorized_keys_append_for_persistence: B2  # Sygnia primary via HelpNet
  # ---- DWELL TIME LAYER (CARRY-FORWARD FROM 06-12) ----
  nearly_a_decade_undetected_dwell_carry_forward_from_finding_0004: A1  # Restatement of 06-12 substrate at higher source-fidelity (Sygnia primary directly retrievable)
  # ---- ATTRIBUTION LAYER (HARD RULE 2 BINDING — PRESERVED VERBATIM) ----
  sygnia_attribution_china_nexus_actor_per_post_title_verbatim: A1  # Verbatim per Sygnia primary post title; verifiable
  sygnia_attribution_china_linked_cyber_espionage_group_per_helpnet_relay_verbatim: A1  # Verbatim quote preservation per Hard Rule 6
  velvet_ant_attribution_remains_china_nexus_NO_cross_walk_to_apt41_volt_typhoon_salt_typhoon_apt40_unc6508: A1  # Hard Rule 2 binding preserved; verifiable per source text — no PLA / MSS / unit naming
  velvet_ant_NOT_on_archimedes_roster_yaml_carry_forward_operator_deferred_new_actor: A1  # Verifiable per roster check unchanged from 06-12
  # ---- VICTIM PROFILE LAYER ----
  victim_organization_UNNAMED_in_sygnia_post_title_and_helpnet_relay: A1  # Verifiable absence per source text
  victim_sector_NOT_disclosed_in_helpnet_relay: A1  # Verifiable absence
  victim_country_NOT_disclosed_in_helpnet_relay: A1  # Verifiable absence
  prior_06_12_east_asia_lineage_NOT_repeated_in_helpnet_relay_this_sweep: B3  # Carry-forward from 06-12; 06-15 HelpNet relay does not restate East Asia framing — Sygnia primary post may carry richer victim detail
  # ---- IOC LAYER ----
  no_hashes_published_in_helpnet_relay: A1  # Verifiable absence
  no_ips_published_in_helpnet_relay: A1  # Verifiable absence
  no_domains_published_in_helpnet_relay: A1  # Verifiable absence
  no_file_paths_published_in_helpnet_relay: A1  # Verifiable absence
  no_cves_referenced_in_helpnet_relay_or_sygnia_primary_in_retrievable_substrate: A1  # Verifiable absence — this is configuration-pattern campaign, not CVE-tracked
  sygnia_primary_post_level_url_likely_carries_richer_iocs_not_extracted_in_helpnet_relay: B3  # Flag for actor-profiler if operator invokes /new-actor scaffolding
  # ---- REMEDIATION COMPLEXITY LAYER (NET-NEW VS 06-12) ----
  remediation_complexity_testing_across_multiple_linux_distributions_required: B2  # Sygnia primary via HelpNet — net-new operational substrate
  rollback_contingencies_required: B2  # Sygnia primary via HelpNet — net-new
  # ---- A&D / DIB RELEVANCE LAYER (unchanged from 06-12) ----
  ad_direct_relevance: A1  # NONE — verifiable absence; no A&D-prime victim named
  ad_structural_relevance_pam_openssh_universal_on_linux_fleets_carry_forward: B3  # Structural inference carry-forward from 06-12
  ad_extrapolation_from_unknown_victim_to_a_d_prime_BLOCKED: A1  # Hard Rule 2 binding on extrapolation
  detection_engineering_richness_pam_module_fim_openssh_binary_attestation_high_carry_forward: B3  # Carry-forward
  # ---- ANTI-NOISE DISPOSITION LAYER ----
  carry_forward_anti_noise_hold_velvet_ant_operation_highland_sygnia_primary_pending_NOW_LIFTED: A1  # Verifiable — hold was for Sygnia primary direct retrieval; achieved this sweep
  net_new_substrate_layered_update_pathway_on_finding_0004: A1  # Procedural — UPDATE-finding scaffold not net-new cluster
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / monitoring-tier) on
  layered UPDATE pathway over finding-2026-06-12-0004. Sygnia
  primary "Operation Highland" post (2026-06-08, 21-minute deep
  dive) is directly retrievable this sweep — resolves the
  `awaiting_direct_retrieval` flag on the sygnia-research source ID
  carried since 2026-06-12. HelpNet Security (Zeljka Zorz byline,
  ratified B per source-grades.yaml) provides independent B-grade
  publisher-side relay distinct from the THN-2026-06-12 surface
  that anchored finding-0004.

  Two publisher-independent relays (THN-06-12 + HelpNet-06-15) +
  vendor primary directly retrievable = three converging substrates
  for the Velvet Ant Operation Highland campaign. This is
  source-fidelity upgrade vs finding-0004's single-publisher
  substrate.

  WHY B2 NOT B1: Cluster still has single primary-research evidence
  basis (Sygnia). Independent IR-firm corroboration (Mandiant /
  Unit 42 / Volexity / CrowdStrike / MSTIC) on the specific
  9-PAM-variant + OpenSSH-backdoor + ssspl-SOCKS5 + GS-Netcat
  primitive set is still NOT in window. Two publisher relays on
  the same Sygnia primary do not constitute independent evidence
  bases per INTEL-GRADING.md rule of thumb. WEP ceiling caps at
  "likely" per single-source-veto on the underlying technical
  attestation.

  WHY MONITORING-TIER INCLUSION NOT ACTION-TIER:
    1. NOT ON 24-ACTOR ROSTER. Velvet Ant has substrate-strengthened
       across two surfaces (THN-06-12 + HelpNet-06-15 + Sygnia
       primary directly retrievable 06-15) but operator-deferred
       /new-actor decision has NOT been made. Hard Rule 5 binding:
       Archimedes does NOT auto-scaffold /new-actor entry; only
       operator can invoke `/new-actor Velvet Ant`. This update
       SURFACES the substrate, does NOT propose roster addition.
    2. NO US A&D-PRIME DIRECT VICTIM NAMED. Sygnia primary did not
       disclose victim sector/country in the HelpNet relay (Sygnia
       primary post may carry richer detail). Hard Rule 2 binding
       on extrapolation from undisclosed victim to A&D-prime
       targeting.
    3. CONFIGURATION-PATTERN CAMPAIGN, NOT CVE-TRACKED. No CVE
       references in either Sygnia primary or HelpNet relay; this
       is initial-access-method + persistence-tradecraft campaign,
       not a vendor-patch-trackable vulnerability. Not vuln-tracker
       eligible.
    4. NET-NEW TTP DETAIL IS REPORTABLE BUT NOT OPERATIONALLY
       ACTIONABLE without IOC enumeration. Detection engineering
       on PAM module integrity monitoring + OpenSSH binary
       attestation is high-value for A&D-prime defenders but
       requires IOCs (hashes / file paths) that Sygnia primary
       likely carries but HelpNet relay did not extract.

  ADDITIONAL ACTOR-PROFILER / DETECTION-ENGINEERING SURFACING
  VALUE: Velvet Ant /new-actor candidacy substrate now has
  vendor-primary-directly-retrievable status (Sygnia post-level
  URL), two-publisher independent relay convergence (THN + HelpNet),
  named tool-set (9 PAM variants + ssspl SOCKS5 + GS-Netcat +
  modified Nginx + custom SSH-triggering binary + OpenSSH credential
  capture + authorized_keys persistence), prior-public lineage
  (2024 F5 BIG-IP + 2024 CVE-2024-20399 Cisco NX-OS), and Sygnia
  organizational lineage tracking since at least 2024. Recommend
  actor-profiler review window for operator /new-actor scaffolding
  evaluation; substrate is now multi-publisher + vendor-primary-
  retrievable across two surfaces.

  WHAT THE B2 ATTESTS:
    (a) Sygnia has documented (via primary research directly
        retrievable + dual-publisher relay convergence) a Velvet
        Ant campaign featuring 9 distinct _pam_unix.so_ variants
        each compiled in separate environments, custom `ssspl`
        SOCKS5 proxy implementation, modified GS-Netcat reverse
        shell, modified Nginx configurations, custom
        SSH-triggering binary, and OpenSSH credential
        capture/command logging with encrypted storage and
        filesystem obfuscation.
    (b) Dwell time is nearly a decade (~9-10 years) undetected
        (carry-forward from 06-12 substrate).
    (c) Attribution remains Sygnia's "China-Nexus Actor" /
        "China-linked cyber espionage group" framing verbatim;
        NO cross-walk to APT41 / Volt Typhoon / Salt Typhoon /
        APT40 / UNC6508 originated by Archimedes (Hard Rule 2
        binding preserved).
    (d) Velvet Ant remains NOT on Archimedes 24-actor roster
        (operator-deferred /new-actor candidacy substrate
        strengthening).
    (e) Sygnia primary post-level URL is directly retrievable
        this sweep — resolves the `awaiting_direct_retrieval`
        flag carried since 2026-06-12.

  WHAT THE B2 DOES NOT ATTEST:
    - A&D-prime targeting (no A&D-prime victim named; Hard Rule
      2 binding on extrapolation).
    - Specific victim sector / country (Sygnia primary did NOT
      disclose in HelpNet relay; primary post may carry).
    - Specific PLA / MSS / unit attribution (Sygnia framing is
      "China-nexus" / "China-linked"; Archimedes does NOT
      cross-walk to roster actors).
    - IOC enumerability at hash / IP / domain / file-path
      granularity (HelpNet relay extracted ZERO IOCs; Sygnia
      primary post likely carries detail not in relay).
    - Initial access method (NOT disclosed in HelpNet relay).
    - C2 infrastructure detail beyond GS-Netcat + ssspl SOCKS5
      tooling naming.

  HARD RULE 2 binding constraint: PRESERVED.
    - Velvet Ant remains NOT in Archimedes _roster.yaml.
    - Sygnia attribution framing preserved verbatim ("China-
      nexus" / "China-linked").
    - NO cross-walk to APT41 / Volt Typhoon / Salt Typhoon /
      APT40 / UNC6508 / other roster actors originated by
      Archimedes.

  HARD RULE 6 binding constraint: PRESERVED. Sygnia attribution
  quotes ("China-Nexus Actor" 3 words, "China-linked cyber
  espionage group" 5 words) preserved verbatim — well under
  15-word cap.

  HARD RULE 8 binding constraint: NOT APPLICABLE.
    - Configuration-pattern campaign, not CVE-tracked, no IOCs
      at hash/IP/domain granularity in retrievable substrate;
      Splunk first-party check structurally limited to PAM
      module integrity monitoring + OpenSSH binary attestation
      which is not currently sentinel-configured for Frank
      environment.

source_reliability:
  grade: B
  source_name: "Sygnia (Operation Highland 2026-06-08) primary via HelpNet Security Zeljka Zorz relay"
  source_yaml_id: helpnetsecurity (publisher) / sygnia-research (primary, provisional)
  grade_rationale: >
    Sygnia is provisional B per source-grades.yaml since 2026-06-12
    via finding-2026-06-12-0004; provisional A candidacy on
    second-surface direct retrieval (Sygnia primary post-level URL
    now directly retrievable this sweep). HelpNet Security
    (Zeljka Zorz byline) is ratified B per source-grades.yaml.
    Two publisher relays (THN-06-12 + HelpNet-06-15) on the same
    Sygnia primary — publisher-side independence achieved.
  provisional: true
  provisional_note: "Sygnia awaiting_direct_retrieval flag now resolved; recommend operator ratification action via /update-tracking or source-grades.yaml direct edit"

credibility:
  grade: 2
  checklist_passed:
    - consistent_with_established_velvet_ant_tradecraft_pattern_per_sygnia_organizational_lineage
    - no_contradicting_evidence_from_a_or_b_grade_sources
    - technical_claims_internally_coherent_pam_openssh_ssspl_socks5_gs_netcat_modular_toolset
  rationale: >
    Sygnia primary research framing is internally coherent with
    multi-year Velvet Ant lineage (2024 F5 BIG-IP / Cisco NX-OS).
    Net-new TTP detail (9 PAM variants compiled per environment,
    ssspl SOCKS5, GS-Netcat reverse shell, custom SSH-triggering
    binary) extends the prior 06-12 substrate without contradicting
    it. Single-vendor evidence basis on the Velvet Ant attribution
    layer — independent IR-firm campaign corroboration would lift
    to credibility 1.

corroboration:
  independent_sources:
    - thehackernews   # via finding-2026-06-12-0004 substrate carry-forward
    - helpnetsecurity  # this sweep
    - sygnia-research  # primary
  independent: false
  test_passed: >
    HelpNet and THN are TWO independent B-grade publishers — they
    are independent publisher-relay layers. BUT both relay the
    SAME Sygnia primary (THN relayed 06-12 substrate; HelpNet
    relays 06-15 substrate of the same Sygnia 2026-06-08 primary
    research). Per INTEL-GRADING.md, these are NOT independent
    evidence bases — both trace to the same Sygnia primary research.
    Publisher-independence satisfied; evidence-basis-independence
    NOT satisfied.
  independent_layered:
    sygnia_primary_research: true   # Vendor-canonical evidence basis
    thehackernews_relay: false      # Publisher relay of Sygnia
    helpnetsecurity_relay: false    # Publisher relay of Sygnia (different sweep)

first_party_precedence:
  applied: false
  splunk_evidence: null
  note: "Configuration-pattern campaign, not CVE-tracked; no IOCs at hash/IP/domain granularity in retrievable substrate to query. PAM module integrity monitoring + OpenSSH binary attestation not currently sentinel-configured for Frank environment."

single_source_veto_applied: true
single_source_veto_layers:
  - sygnia_primary_only_no_independent_ir_firm_corroboration_on_underlying_technical_attestation
wep_ceiling: likely

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "Velvet Ant Operation Highland — China-nexus 9-PAM-variant + OpenSSH + ssspl SOCKS5 + GS-Netcat authentication-stack backdoor; nearly-decade dwell; layered UPDATE on finding-2026-06-12-0004"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-15-pm-002-helpnet-sygnia-velvet-ant-operation-highland-direct-retrieval-substrate-update
  attribution_claims:
    - claimed_actor: "Velvet Ant"
      claimed_actor_attribution_text: "China-Nexus Actor (Sygnia post title verbatim) / China-linked cyber espionage group (HelpNet relay verbatim)"
      claimed_by_sources: [sygnia-research, helpnetsecurity, thehackernews]
      requires_analyst_review: true
      note: |
        Hard Rule 2 preserved — Sygnia attribution string is "China-Nexus" /
        "China-linked"; Archimedes does NOT originate cross-walk to APT41 /
        Volt Typhoon / Salt Typhoon / APT40 / UNC6508 or any roster-tracked
        actor. Velvet Ant is NOT on Archimedes 24-actor _roster.yaml
        (operator-deferred /new-actor candidacy substrate-strengthening per
        Hard Rule 5 — Archimedes does NOT originate roster addition).

# ============================================================================
# Inclusion eligibility
# ============================================================================
inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_substrate_strengthening_pending_operator_new_actor_decision
  not_eligible_for:
    - flash  # FLASH triggers 2/4/5 all FAIL (Velvet Ant not on roster; no A&D-prime victim named)
    - vuln_tracker_update  # Configuration-pattern campaign, not CVE-tracked

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: true   # WEP "likely" + attribution-claim layer requires analyst attention
analyst_review_complete: true
analyst_review_run_id: analyst-20260615-160800
red_team_review_required: false # WEP ceiling capped at "likely" per single-source veto
red_team_review: null
analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Is Sygnia's 'China-Nexus Actor' / 'China-linked cyber espionage group' framing of Velvet Ant supported against alternative explanations of the Operation Highland tradecraft pattern?"
      analyzed_at: 2026-06-15T16:14:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: "Sygnia's framing is correct: Velvet Ant is a China-nexus espionage actor responsible for the 9-PAM-variant + OpenSSH + ssspl + GS-Netcat tradecraft against the unnamed victim."
        - id: H2
          statement: "Velvet Ant is a methodologically distinct cluster from prior Sygnia 'Velvet Ant' reporting (2024 F5 BIG-IP / Cisco NX-OS), and Sygnia has aggregated multiple unrelated China-nexus or unattributed campaigns under a single label."
        - id: H3
          statement: "The Operation Highland tradecraft is the work of a non-China-nexus actor (Russia/Iran/North Korea/criminal) using Linux-fleet tradecraft superficially similar to prior China-nexus PAM-backdoor patterns."
        - id: H4
          statement: "The campaign is the work of a previously-untracked actor reusing publicly-known PAM-backdoor research (multiple public reference implementations exist)."
        - id: H5
          statement: "The campaign is a deliberate false flag: a non-Chinese actor designed to leave artifacts consistent with prior Chinese PAM-tradecraft reporting."
      evidence:
        - id: E1
          description: "Sygnia organizational lineage of Velvet Ant tracking since at least 2024 (F5 BIG-IP / CVE-2024-20399 Cisco NX-OS prior surfaces)"
          source: sygnia-research
          digraph: B2
          weight: 2
        - id: E2
          description: "9 distinct _pam_unix.so_ variants compiled per environment + custom ssspl SOCKS5 + GS-Netcat + custom SSH-triggering binary — bespoke not commodity tooling"
          source: sygnia-research-helpnet-relay
          digraph: B2
          weight: 2
        - id: E3
          description: "Nearly-decade undetected dwell — operational tradecraft consistent with state-sponsored espionage patience profile"
          source: sygnia-research
          digraph: B2
          weight: 2
        - id: E4
          description: "Sygnia attribution language is qualified ('China-Nexus' / 'China-linked'), NOT specific PLA/MSS unit designation"
          source: sygnia-research-helpnet-relay
          digraph: A1
          weight: 3
        - id: E5
          description: "No US A&D-prime victim named; victim sector/country NOT disclosed in HelpNet relay (Sygnia primary post may carry)"
          source: helpnet-relay
          digraph: A1
          weight: 3
        - id: E6
          description: "No independent IR-firm (Mandiant/Unit42/Volexity/CrowdStrike/MSTIC) corroboration on the specific 9-PAM-variant + ssspl + GS-Netcat primitive set in window"
          source: corpus-audit
          digraph: A1
          weight: 3
        - id: E7
          description: "Two B-grade publishers (THN-06-12 + HelpNet-06-15) on same Sygnia primary — publisher independence achieved, evidence-basis independence NOT achieved"
          source: corpus-audit
          digraph: A1
          weight: 3
      matrix:
        E1: {H1: C, H2: I, H3: I, H4: I, H5: N}
        E2: {H1: C, H2: C, H3: N, H4: I, H5: C}
        E3: {H1: C, H2: C, H3: C, H4: I, H5: C}
        E4: {H1: C, H2: C, H3: N, H4: N, H5: N}
        E5: {H1: N, H2: N, H3: N, H4: N, H5: N}
        E6: {H1: N, H2: N, H3: N, H4: N, H5: N}
        E7: {H1: N, H2: N, H3: N, H4: N, H5: N}
      inconsistency_counts:
        H1: 0
        H2: 1
        H3: 2
        H4: 3
        H5: 0
      diagnostic_evidence:
        - E1: "Distinguishes Sygnia's claim of organizational continuity (H1/H5) from cluster-aggregation (H2) and non-China-nexus (H3) hypotheses"
        - E2: "Distinguishes bespoke-tooling hypotheses (H1/H2/H5) from public-research-reuse (H4)"
      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: "Zero inconsistencies; consistent with all diagnostic evidence; simplest explanation given Sygnia's prior tracking continuity. PRIMARY HYPOTHESIS is the one Sygnia originated — Archimedes does NOT originate."
          wep: likely
        - rank: 1-tied
          hypothesis_id: H5
          rationale: "Zero inconsistencies but requires multiple unverified assumptions (sophisticated false-flag actor with PAM-backdoor expertise + intent to implicate China-nexus). Lower a priori probability per parsimony."
          wep: unlikely
        - rank: 3
          hypothesis_id: H2
          rationale: "One inconsistency (E1 — Sygnia's lineage tracking would have to be wrong); plausible but no evidence basis."
          wep: unlikely
        - rank: 4
          hypothesis_id: H3
          rationale: "Two inconsistencies; non-China-nexus actor would have to coincidentally produce China-nexus-pattern tradecraft."
          wep: very_unlikely
        - rank: 5
          hypothesis_id: H4
          rationale: "Three inconsistencies; bespoke per-environment-compiled PAM variants + custom ssspl SOCKS5 + GS-Netcat is unusually high engineering investment for a public-research-reuse actor."
          wep: remote
      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E1, E2]
        if_E1_wrong: "If Sygnia's prior Velvet Ant tracking lineage proves to be aggregated rather than single-actor, H2 rises to equal with H1; assessment shifts from 'this is the same Velvet Ant Sygnia has been tracking' to 'this is Sygnia's umbrella label for China-nexus PAM tradecraft generally'"
        if_E2_wrong: "If the tooling shows signs of public reference-implementation reuse rather than bespoke development, H4 rises materially"
        if_sygnia_downgraded: "Sygnia is provisional B; if substantive errors surface in the primary research post directly retrievable now, H1's weight drops and assessment widens to roughly-even between H1/H2"
      tripwires:
        - observation: "Independent IR-firm (Mandiant/Unit42/Volexity/CrowdStrike/MSTIC) publishes on the same 9-PAM-variant + ssspl + GS-Netcat primitive set"
          effect: "Elevates H1 confidence (independent evidence basis); lifts single-source veto; rerun ACH"
        - observation: "Subsequent publication explicitly maps Velvet Ant to an existing roster actor (APT41 / Volt Typhoon / Salt Typhoon / APT40 / UNC6508)"
          effect: "Triggers Hard Rule 2 cross-walk evaluation; Archimedes does NOT originate cross-walk but may consume sourced mapping"
        - observation: "Victim sector/country surfaces and is A&D-prime"
          effect: "Lifts A&D-direct relevance from NONE; triggers operator surface + actor-profiler escalation"
        - observation: "Sygnia or third party documents prior 'Velvet Ant' incidents as methodologically distinct clusters"
          effect: "Elevates H2 (label-aggregation hypothesis); revises Sygnia source-grade"
      conclusion:
        summary: |
          Sygnia's China-nexus framing is the strongest-supported hypothesis given
          available evidence — zero inconsistencies and consistent with the bespoke
          tooling pattern. Per Hard Rule 2, Archimedes does NOT originate or revise
          attribution; ACH here pressure-tests Sygnia's sourced claim, which survives.
          Critical caveat: H1 and H5 (false-flag) both score zero inconsistencies;
          H5 is ranked lower only by parsimony. The single-source-veto cap at 'likely'
          is appropriate and ACH supports — not challenges — that ceiling. Velvet Ant
          remains operator-deferred /new-actor candidacy per Hard Rule 5; this ACH
          surfaces substrate-strengthening, NOT roster-addition recommendation.
        wep: likely
        confidence_caveats: |
          Single-source dependence on Sygnia. Both publisher relays (THN + HelpNet)
          relay the same Sygnia primary — publisher independence does NOT equal
          evidence-basis independence per INTEL-GRADING. Assessment is brittle to
          (a) Sygnia primary substantive errors and (b) prior Velvet Ant lineage
          turning out to be cluster-aggregation. Watch for independent IR-firm
          publication on the specific primitive set.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Velvet Ant Operation Highland tradecraft (9 PAM variants + ssspl + GS-Netcat)
        is consistent with prior Sygnia-tracked Velvet Ant lineage and remains
        operator-deferred /new-actor candidacy at WEP 'likely'."
      analyzed_at: 2026-06-15T16:14:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication ACH stress-test of the surviving H1; substrate-strengthening for operator-deferred /new-actor candidacy"
      assumptions:
        - id: A1
          statement: "Sygnia's 2024 'Velvet Ant' (F5 BIG-IP / Cisco NX-OS) and 2026 'Velvet Ant Operation Highland' (PAM/OpenSSH) refer to the same actor cluster, not separate campaigns aggregated under one label"
          category: actor_continuity
          stated: false
          why_must_be_true: "Lineage continuity is load-bearing for H1's strength in the ACH ranking"
          when_could_be_false: "Sygnia uses 'Velvet Ant' as an umbrella label for China-nexus long-dwell tradecraft; underlying actors differ across campaigns"
          evidence_for: [sygnia_organizational_tracking_continuity_since_at_least_2024]
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A2
          statement: "China-nexus espionage actors are the dominant population producing 9-PAM-variant + per-environment-compilation tradecraft on Linux fleets"
          category: ttp_patterns
          stated: false
          why_must_be_true: "Attribution to China-nexus depends on base-rate of this tradecraft pattern across nation-state actor populations"
          when_could_be_false: "Other state-sponsored actors (notably Iran's IRGC, North Korean Lazarus subordinates, Russian SVR-aligned operators) have demonstrated PAM-modification capability in research literature"
          evidence_for: [mandiant_apt5_apt15_apt41_pam_tradecraft_historical_corpus]
          evidence_against: [iran_irgc_known_linux_tradecraft_research_pattern, north_korean_pam_implementation_examples_in_kaspersky_corpus]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A3
          statement: "Sygnia's primary research methodology is rigorous enough to support the 'China-Nexus' label assignment"
          category: source_reliability
          stated: true
          why_must_be_true: "Sygnia is provisional B; the framing-quality is load-bearing"
          when_could_be_false: "Direct retrieval of Sygnia primary reveals methodological weaknesses (e.g., attribution based on language/timezone artifacts only, not infrastructure or TTP-uniqueness)"
          evidence_for: [sygnia_primary_now_directly_retrievable_this_sweep]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A4
          statement: "Velvet Ant remains operationally active in 2026 (vs disrupted / dormant / absorbed)"
          category: actor_operational_status
          stated: false
          why_must_be_true: "Current-tense 'Velvet Ant' attribution implies ongoing actor continuity into 2026"
          when_could_be_false: "Original Velvet Ant operators dispersed; current activity is residual access from prior compromises being re-discovered"
          evidence_for: [sygnia_primary_2026_06_08_publication_date_implies_recent_activity]
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: sound
        - id: A5
          statement: "The unnamed victim's sector/country is consistent with prior Velvet Ant targeting patterns (East Asia per finding-0004 substrate)"
          category: semantic
          stated: false
          why_must_be_true: "Cluster-coherence with prior Velvet Ant reporting depends on consistent victim profile"
          when_could_be_false: "Victim turns out to be US/Western/A&D-prime — would change the cluster characterization but support continued China-nexus framing"
          evidence_for: []
          evidence_against: []
          confidence: unknown
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 2
        qualify: 3
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "Velvet Ant lineage continuity (2024 → 2026) is assumed but not independently verified outside Sygnia's own corpus (A1 qualify)"
          - "China-nexus attribution rests on base-rate inference about PAM-tradecraft population; alternative nation-state actor populations have demonstrated similar capability (A2 qualify)"
          - "Sygnia primary methodology rigor not independently audited; direct retrieval recommended for operator review (A3 qualify)"
        next_action: "Proceed to publication at WEP 'likely' as graded; flag operator-deferred /new-actor candidacy with substrate-strengthening; if independent IR-firm corroboration lands OR Sygnia primary methodology reveals weakness, rerun KAC"
      recommended_wep_after_test:
        if_independent_ir_firm_corroborates: "WEP 'very likely' available — would trigger red-team escalation"
        if_sygnia_methodology_questioned: "WEP downgrade to 'possibly'; assessment widens to roughly-even between H1 and H2"
        current_state: "WEP 'likely' is appropriately conservative"

actor_profiler_handoff:
  proposed_action: substrate_strengthen_velvet_ant_candidacy
  rationale: |
    Operator-deferred /new-actor candidacy substrate now has:
    (1) Vendor primary directly retrievable (Sygnia post-level URL);
    (2) Two-publisher independent relay convergence (THN-06-12 + HelpNet-06-15);
    (3) Named tool-set (9 PAM variants + ssspl SOCKS5 + GS-Netcat + modified Nginx + custom SSH-triggering binary + OpenSSH credential capture + authorized_keys persistence);
    (4) Prior-public lineage (2024 F5 BIG-IP + 2024 CVE-2024-20399 Cisco NX-OS);
    (5) Sygnia organizational lineage tracking since at least 2024.
    Hard Rule 5 binding: actor-profiler does NOT auto-scaffold; only operator can invoke /new-actor Velvet Ant.
  attribution_language_to_preserve_verbatim: "China-Nexus Actor / China-linked cyber espionage group"
  hard_rule_2_binding: "NO cross-walk to APT41 / Volt Typhoon / Salt Typhoon / APT40 / UNC6508 or other roster actors"

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs:
  - 2026-06-15-afternoon
retracted: false
retraction_brief_id: null
---

# UPDATE on finding-2026-06-12-0004: HelpNet Security covers Sygnia Operation Highland primary (directly retrievable this sweep) — Velvet Ant nearly-decade China-nexus authentication-stack backdoor; net-new TTP detail (9 PAM variants per-environment-compiled, ssspl SOCKS5, GS-Netcat); two-publisher independent relay convergence; Hard Rule 2 preserved

## Summary

HelpNet Security (Zeljka Zorz byline) published B-grade publisher relay of
Sygnia's "Operation Highland" primary post (2026-06-08, 21-minute deep dive),
which is **directly retrievable this sweep** — resolving the
`awaiting_direct_retrieval` flag carried since 2026-06-12 on the
sygnia-research source ID. Net-new TTP detail vs the THN-2026-06-12 prior
relay surface: 9 distinct `_pam_unix.so_` variants each compiled in a separate
environment, custom `ssspl` SOCKS5 proxy implementation, modified GS-Netcat
reverse shell, modified Nginx configurations, and a custom SSH-triggering
binary. Sygnia attribution remains "China-Nexus Actor" / "China-linked cyber
espionage group" verbatim; **NO cross-walk** to APT41 / Volt Typhoon / Salt
Typhoon / APT40 / UNC6508 originated by Archimedes (Hard Rule 2 binding
preserved). Velvet Ant remains NOT on the 24-actor roster (operator-deferred
/new-actor candidacy substrate-strengthening). No US A&D-prime direct victim
named; Sygnia primary did not disclose victim sector or country in the
HelpNet relay.

## Sources

### Sygnia primary (source_yaml_id: sygnia-research, digraph: B provisional)

- URL: https://www.sygnia.co/blog/ (post-level permalink in 2026-06-08 entry)
- Published: 2026-06-08
- Post title: "Velvet Ant's Operation Highland: How a China-Nexus Actor Infiltrated an Internal Network Undetected"
- Reading time: 21 minutes
- Direct retrieval this sweep: **YES** (resolves prior `awaiting_direct_retrieval` flag)
- Key claim: Vendor-canonical primary research on Velvet Ant nearly-decade-long authentication-stack backdoor campaign with 9 PAM-variant + OpenSSH + ssspl SOCKS5 + GS-Netcat tradecraft

### HelpNet Security (source_yaml_id: helpnetsecurity, digraph: B)

- URL: https://www.helpnetsecurity.com/2026/06/15/velvet-ant-backdoored-authentication-persistence/
- Published: 2026-06-15 15:27 UTC
- Byline: Zeljka Zorz
- Key claim: Independent B-grade publisher-side relay of Sygnia primary; second publisher distinct from THN-2026-06-12 surface

### The Hacker News (source_yaml_id: thehackernews, digraph: B) — CARRY-FORWARD from finding-2026-06-12-0004

- Published: 2026-06-12
- Key claim: First publisher relay of Sygnia primary; substrate anchored in finding-2026-06-12-0004

## Technical detail

### Net-new TTP detail vs finding-2026-06-12-0004

Per Sygnia primary via HelpNet relay (Zorz byline):

1. **Nine distinct `_pam_unix.so_` variants** — each variant built in a
   **separate compile environment**. Functions: hardcoded password bypass +
   silent credential logging. (Specific count + per-environment-compilation
   detail; 06-12 substrate had general "nine PAM module variants" framing.)
2. **Custom `ssspl` SOCKS5 proxy implementation** for tunneling. **NET-NEW
   tool-name** vs 06-12 substrate.
3. **Modified GS-Netcat utility** for reverse shell to C2. **NET-NEW
   tool-name** vs 06-12 substrate.
4. **Modified Nginx configurations** + **custom SSH-triggering binary** for
   pivot infrastructure. **NET-NEW infrastructure detail** vs 06-12 substrate.
5. **Modified SSH server binaries** capture both incoming and outgoing
   credentials, log commands, with encrypted storage and filesystem
   obfuscation.
6. **Authorized_keys append** for persistence (consistent with 06-12 substrate).

### TTP chain (full reconstruction per HelpNet relay of Sygnia primary)

1. Initial access method **NOT disclosed** in the HelpNet relay
2. Deployed modified **GS-Netcat** utility for reverse shell to C2
3. Leveraged modified **Nginx** configurations and custom SSH-triggering binary
4. Established SOCKS5 proxy tunneling using **custom `ssspl` implementation**
5. Compromised authentication layer through **PAM and OpenSSH modifications**

### Dwell time (carry-forward)

Nearly a decade (~9-10 years) undetected — carry-forward from
finding-2026-06-12-0004 substrate at higher source-fidelity (Sygnia primary
now directly retrievable).

### Remediation complexity (net-new)

Per Sygnia primary via HelpNet: testing across multiple Linux distributions
required before production deployment, with rollback contingencies. Operational
substrate not present in 06-12 surface.

### Victim profile

- **Organization**: UNNAMED in both Sygnia primary post title and HelpNet relay
- **Sector**: NOT disclosed in HelpNet relay
- **Country**: NOT disclosed in HelpNet relay (06-12 substrate carried "East
  Asia" lineage from prior Sygnia tracking; not restated in 06-15 HelpNet relay)

### Attribution language (verbatim per Hard Rule 6)

- Sygnia post title verbatim: **"China-Nexus Actor"** (3 words)
- HelpNet relay verbatim: **"China-linked cyber espionage group"** (5 words)

Hard Rule 2 binding: Archimedes does **NOT cross-walk** to APT41 / Volt Typhoon
/ Salt Typhoon / APT40 / UNC6508 or any roster-tracked actor. Velvet Ant is
**NOT on Archimedes 24-actor `_roster.yaml`** (operator-deferred /new-actor
candidacy substrate-strengthening per Hard Rule 5 — Archimedes does NOT
originate roster addition).

## IOCs surfaced

```yaml
iocs:
  hashes: []
  ips: []
  domains: []
  urls: []
  file_paths:
    - "_pam_unix.so_ variants (9 distinct per-environment-compiled — specific paths NOT enumerated in HelpNet relay; Sygnia primary post may carry)"
  cves: []
  tool_names:
    - GS-Netcat (modified — reverse shell to C2)
    - ssspl (custom SOCKS5 proxy implementation)
    - Nginx (modified configurations)
    - "custom SSH-triggering binary (name NOT enumerated)"
  malware_family:
    - "9-variant PAM module backdoor + OpenSSH credential capture (no common malware family designation in retrievable substrate)"

attribution_claims:
  - source: Sygnia (Operation Highland primary, 2026-06-08, directly retrievable)
    actor: "Velvet Ant"
    actor_attribution_verbatim: "China-Nexus Actor (post title) / China-linked cyber espionage group (HelpNet relay)"
    confidence: VENDOR_PRIMARY_ATTESTATION
    hard_rule_2_binding: "Sygnia attribution preserved verbatim; NO cross-walk originated by Archimedes"
```

## Relationship to existing findings

- **UPDATE on finding-2026-06-12-0004** (THN single-publisher relay of Sygnia
  primary; East Asia victim, ~10-year dwell, nine PAM variants, OpenSSH
  credential/command logging with hidden disable switch). This finding adds:
  (1) Sygnia primary now directly retrievable;
  (2) Independent B-grade publisher relay (HelpNet/Zorz);
  (3) Net-new TTP detail (per-environment PAM compilation, ssspl SOCKS5,
      GS-Netcat, modified Nginx, custom SSH-triggering binary);
  (4) Net-new remediation complexity substrate.

- **Anti-noise hold carried since 2026-06-12 ("Velvet Ant Operation Highland
  Sygnia primary pending") is NOW LIFTED.** Sygnia primary direct retrieval
  achieved this sweep.

## Open questions for analyst / actor-profiler

1. **/new-actor candidacy decision** (operator-deferred, Hard Rule 5):
   Substrate has strengthened materially across two surfaces (THN-06-12 +
   HelpNet-06-15 + Sygnia primary directly retrievable). Hard Rule 5
   binding — Archimedes does NOT auto-scaffold; only operator can invoke
   `/new-actor Velvet Ant`. Substrate is now multi-publisher +
   vendor-primary-retrievable across two surfaces — operationally
   meaningful candidacy gate.
2. **Sygnia primary post-level direct retrieval** (actor-profiler if
   operator invokes /new-actor): Retrieve sygnia.co/blog/ Operation
   Highland permalink for full IOC enumeration (hashes, IPs, domains,
   file paths), victim sector/country if disclosed, initial access vector,
   detection/eviction timeline detail, C2 infrastructure beyond GS-Netcat
   + ssspl naming.
3. **Independent IR-firm corroboration watch** (analyst): No Mandiant /
   Unit 42 / Volexity / CrowdStrike / MSTIC publication on the specific
   9-PAM-variant + OpenSSH + ssspl-SOCKS5 primitive set in window.
   Independent corroboration would lift single-source veto on the
   underlying technical attestation.
4. **Hard Rule 2 binding watch** (analyst): Sygnia attribution remains
   "China-nexus" / "China-linked" framing. Archimedes does NOT cross-walk
   to APT41 / Volt Typhoon / Salt Typhoon / APT40 / UNC6508 or other
   roster actors. If a subsequent A-grade publication explicitly maps
   Velvet Ant to an existing roster actor, finding is updated; absent
   that explicit mapping, the "China-nexus" framing is preserved
   verbatim.
5. **A&D detection-engineering operational value** (operator surface):
   PAM module file-integrity monitoring + OpenSSH binary attestation +
   `authorized_keys` change monitoring are universally relevant to
   A&D-prime Linux fleets; detection engineering callout is high-value
   even without specific A&D-prime victim attribution. Recommend operator
   surface for DIB / A&D-prime defender awareness.

## Analytic notes (from analyst review)

ACH ran on five hypotheses (Sygnia's framing, label-aggregation, non-China-nexus actor, untracked-actor reusing public research, false-flag); KAC then stress-tested H1's assumptions. H1 (Sygnia's China-nexus framing) ranked first with zero inconsistencies — but H5 (false-flag) also scored zero, ranked lower only by parsimony. Sygnia's claim survives pressure-testing without being elevated; per Hard Rule 2, Archimedes pressure-tests sourced attribution, does not originate or revise.

The brittleness is medium. KAC surfaced three qualifying assumptions: Sygnia's 2024 → 2026 Velvet Ant lineage continuity is unverified outside Sygnia's own corpus (A1 critical-centrality); China-nexus attribution rests on PAM-tradecraft base-rate reasoning (A2 material); Sygnia's primary methodology rigor not independently audited (A3 material). None blocks publication. The grader's "likely" cap via single-source veto holds — ACH and KAC both support, not challenge, that ceiling.

Operator-deferred /new-actor candidacy substrate strengthens this cycle (Sygnia primary now directly retrievable + two-publisher convergence). Recommend operator review of Sygnia primary methodology before any /new-actor invocation. No red-team escalation needed (WEP capped at "likely").
