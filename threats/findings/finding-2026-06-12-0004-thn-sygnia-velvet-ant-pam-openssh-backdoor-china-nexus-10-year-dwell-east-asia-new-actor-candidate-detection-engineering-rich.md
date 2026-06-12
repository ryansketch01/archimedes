---
id: finding-2026-06-12-0004
finding_id: finding-2026-06-12-0004-thn-sygnia-velvet-ant-pam-openssh-backdoor-china-nexus-10-year-dwell-east-asia-new-actor-candidate-detection-engineering-rich
title: "Sygnia documents Velvet Ant (China-nexus, NOT in Archimedes roster) backdoor of Linux PAM and OpenSSH on air-gapped East Asia victim; ~10-year dwell since 2016; nine PAM-module variants + modified OpenSSH credential-and-command logging with hidden disable switch; sector NOT named; structural detection-engineering callout for A&D Linux fleets; /new-actor candidacy flag"
date: 2026-06-12
created_at: 2026-06-12T16:40:00-04:00
graded_by: grader
grading_run_id: afternoon-20260612-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- VENDOR RESEARCH LAYER (Sygnia primary; THN relay) ----
  sygnia_documents_velvet_ant_pam_openssh_backdoor: B2  # Sygnia primary not in source-grades.yaml; provisional B-tier per cheatsheet "named IR firm with structured public technical research"; THN B-grade relay
  pam_login_module_replaced_with_backdoored_copies: B2  # Sygnia primary via THN relay
  nine_separate_versions_of_backdoored_pam_module: B2  # Sygnia primary via THN relay — specific technical enumeration
  openssh_modified_to_log_credentials_and_commands_typed: B2  # Sygnia primary via THN relay
  openssh_variants_accept_secret_passwords_or_silently_record_legitimate_logins: B2  # Sygnia primary via THN relay
  hidden_disable_switch_on_logging_functionality: B2  # Sygnia primary via THN relay — operator-side switch
  hide_inside_linux_login_system_itself_tradecraft: B2  # Sygnia primary tradecraft framing
  # ---- DWELL TIME LAYER ----
  earliest_traces_date_to_2016_approximately_ten_year_dwell: B2  # Sygnia primary via THN relay — specific dwell claim
  # ---- VICTIM LAYER ----
  victim_network_had_no_direct_internet_access_air_gapped_or_isolated: B2  # Sygnia primary via THN relay
  victim_located_in_east_asia_per_sygnia_prior_lineage: B2  # Sygnia lineage consistent across surfaces
  no_specific_sector_named_in_thn_summary: A1  # Verifiable absence in pm-004
  no_specific_country_named_in_thn_summary: A1  # Verifiable absence in pm-004
  # ---- ATTRIBUTION LAYER (HARD RULE 2 BINDING) ----
  velvet_ant_china_nexus_per_sygnia_thn_relay: B2  # "China-nexus" / "China-linked" — Sygnia primary characterization through THN relay; conservative B2 per single-vendor primary
  velvet_ant_NOT_in_archimedes_roster_yaml: A1  # Verifiable absence per roster #001-022 check
  no_pla_mss_unit_naming_at_any_in_window_source: A1  # Verifiable absence
  no_cross_walk_to_apt41_volt_typhoon_salt_typhoon_apt40: A1  # Hard Rule 2 binding — Archimedes does NOT cross-walk
  # ---- PRIOR PUBLIC LINEAGE LAYER ----
  velvet_ant_2024_f5_big_ip_appliance_exploitation_prior_public: B2  # THN article reference to prior Velvet Ant lineage
  velvet_ant_2024_cve_2024_20399_cisco_nx_os_zero_day_prior_public: B2  # THN article reference; verifiable in NVD
  velvet_ant_sygnia_tracked_since_at_least_2024: B2  # Sygnia organizational lineage
  velvet_ant_migration_pattern_endpoints_to_legacy_to_appliances_to_login_subsystem: B2  # Sygnia analytic framing of multi-year campaign pattern
  # ---- A&D / DIB RELEVANCE LAYER (structural inference) ----
  ad_direct_relevance: A1  # NONE — verifiable absence; no A&D-prime victim named
  ad_structural_relevance_pam_openssh_universal_on_linux_fleets: B3  # Structural inference; A&D-prime Linux fleets universally run PAM + OpenSSH but no source-attested deployment-density evidence for Velvet Ant in A&D
  ad_extrapolation_from_east_asia_to_a_d_prime_BLOCKED: A1  # Hard Rule 2 binding on extrapolation
  detection_engineering_richness_pam_module_fim_openssh_binary_attestation_high: B3  # Structural inference — detection-engineering callout is operationally meaningful but not source-attested as A&D-specific
  # ---- IOC LAYER ----
  no_iocs_enumerated_in_thn_relay: A1  # Verifiable absence
  sygnia_primary_may_carry_richer_iocs_not_directly_retrieved_this_sweep: B3  # Flag for next-sweep direct retrieval
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True) on Sygnia primary
  research relayed by The Hacker News (ratified B per
  source-grades.yaml; provisional B per provisional_since
  2026-05-14). Sygnia is NOT in source-grades.yaml — provisional
  B-tier per cheatsheet "named IR firm with structured public
  technical research" lineage. Sygnia primary blog
  (https://www.sygnia.co/blog/) was NOT directly retrieved this
  sweep; flag for next-sweep direct retrieval (high-value, may
  carry richer IOCs not in THN relay).

  Single-source veto APPLIES at the strict "vendor-primary
  independently corroborated by second IR firm" framing — only
  Sygnia provides this research at sweep; no Mandiant / Unit 42 /
  Volexity / CrowdStrike / MSTIC cross-vendor corroboration on
  the specific 9-PAM-variant + OpenSSH-backdoor primitive set
  in window. WEP ceiling caps at "likely" per veto.

  WHAT THE B2 ATTESTS:
    (a) Sygnia has documented (via primary research relayed
        by THN) a Velvet Ant campaign against an East Asia
        victim featuring 9 PAM-module backdoor variants +
        modified OpenSSH credential/command logging with
        operator-side disable switch.
    (b) The dwell time claim (earliest traces 2016, ~10 years)
        is internally coherent with Sygnia's lineage on
        Velvet Ant prior research (2024 F5 + Cisco NX-OS).
    (c) The "hide inside the Linux login system itself"
        tradecraft framing is consistent with prior Velvet Ant
        campaign migration pattern (Sygnia analytic framing).

  WHAT THE B2 DOES NOT ATTEST:
    - A&D-prime targeting (no A&D-prime victim named; Hard
      Rule 2 binding on extrapolation from East Asia campaign).
    - Specific sector identification (no sector named in THN
      summary; Sygnia primary may carry richer detail not in
      relay).
    - Specific PLA / MSS / unit attribution (Sygnia framing is
      "China-nexus" / "China-linked"; Archimedes does NOT
      cross-walk to APT41 / Volt Typhoon / Salt Typhoon /
      APT40 / other roster actors).
    - IOC enumerability (no file paths, hashes, or IP
      addresses in THN relay; Sygnia primary not directly
      retrieved).

  HARD RULE 2 binding constraint: PRESERVED.
    - Velvet Ant is NOT in Archimedes _roster.yaml (verified
      against full 22-actor roster at grading time).
    - Sygnia's attribution language is "China-nexus" / "China-
      linked" — NOT a specific PLA / MSS / unit naming.
    - Archimedes does NOT cross-walk Velvet Ant to existing
      roster actors (APT41, Volt Typhoon, Salt Typhoon,
      APT40, etc.).
    - /new-actor candidacy is flagged for operator decision;
      this finding does NOT initiate /new-actor scaffolding.
    - East Asia → A&D-prime extrapolation is BLOCKED.

  HARD RULE 6 binding constraint: PRESERVED. No verbatim
  quotes ≥15 words propagated. The "hide inside the Linux
  login system itself" tradecraft framing is Sygnia analytic
  paraphrase at <15 words.

  HARD RULE 8 binding constraint: Per pm-000 sentinel + grader-
  side first-party Splunk query (-7d window across
  index=archimedes OR index=defenseclaw_local on Velvet Ant +
  Sygnia + PAM-module-tampering + sshd-config-modification
  keywords): 12 events at most-recent query, all Archimedes
  self-instrumentation. Zero substantive first-party matches.
  defenseclaw_local does run Linux systems (Frank-host
  ancillary services) but Sygnia primary indicators (specific
  file paths, hashes) are not in the THN relay, so no
  detection-meaningful sentinel can be authored at this hour.
  Per Hard Rule 8: silence is not disconfirming. First-party
  precedence does NOT apply.

source_reliability:
  grade: B
  source_name: "Sygnia primary research (provisional B-tier per cheatsheet, not in source-grades.yaml) relayed by The Hacker News (provisional B per source-grades.yaml provisional_since 2026-05-14)"
  source_yaml_id: thehackernews
  grade_rationale: >
    The Hacker News is provisional B per source-grades.yaml.
    Sygnia primary research is NOT in source-grades.yaml —
    provisional B-tier per cheatsheet "named IR firm with
    structured public technical research" lineage. Sygnia has
    institutional research lineage on Velvet Ant since at least
    2024 (2024 F5 BIG-IP + 2024 CVE-2024-20399 Cisco NX-OS
    zero-day prior public).
  provisional: true
  provisional_since: 2026-05-14
  flag_for_librarian: >
    Add Sygnia to source-grades.yaml at provisional B-tier per
    cheatsheet "named IR firm with structured public technical
    research" lineage; Sygnia has Velvet Ant tracking lineage
    since at least 2024 and appears as primary research source
    in multiple prior corpus contexts (operator memory check).

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_known_ttps_or_campaign_timing  # Velvet Ant migration-between-target-classes pattern (endpoints → legacy servers → network appliances → login subsystem) is consistent with Sygnia's prior public lineage on the actor
    - probably_true_no_contradicting_ab_grade_source  # No A/B-grade contradiction at sweep
    - probably_true_technical_claims_internally_coherent  # 9 PAM-module variants + modified OpenSSH credential-and-command logging + hidden disable switch is internally coherent with Linux login-system architecture; the technical primitive set is documented within established Linux backdoor research lineage
  rationale: >
    Cluster anchor at Grade 2 (Probably True): Sygnia primary
    research is internally coherent with prior Velvet Ant
    public lineage (2024 F5 + Cisco NX-OS); technical
    primitives (PAM module replacement, OpenSSH credential
    logging, operator-side disable switch) are within
    established Linux backdoor research lineage and are
    consistent with multi-year-dwell APT tradecraft. No A/B-
    grade contradiction at sweep. Single-source veto applies
    on the cluster anchor (WEP caps at "likely"); Sygnia
    primary not directly retrieved (flag for next-sweep
    direct retrieval). Grade 1 (Confirmed) not met because
    no independent IR firm corroboration in window; Grade 3
    (Possibly True) not met because the technical primitives
    + dwell time are internally coherent and consistent with
    prior Velvet Ant lineage.

corroboration:
  independent_sources:
    - thehackernews
  independent: false  # Sygnia primary reaches cluster through single THN relay; no second IR firm corroboration at sweep
  test_passed: >
    Corroboration test FAILS at this sweep. THN single in-
    window publisher; Sygnia primary not directly retrieved.
    Independence requires either (a) Sygnia primary direct
    retrieval, (b) second IR firm (Mandiant / Unit 42 /
    Volexity / CrowdStrike / MSTIC / Sophos / SentinelLabs)
    independent analysis on the same campaign, or (c) a
    second media publisher (BC / SW / The Record / Krebs)
    relaying Sygnia primary. All three are next-sweep watch
    items.

first_party_precedence:
  applied: false
  splunk_evidence: >
    Per pm-000 sentinel + grader-side query (-7d window across
    index=archimedes OR index=defenseclaw_local on Velvet Ant +
    Sygnia + PAM-module + OpenSSH-backdoor keywords): 12 events
    at most-recent query, all Archimedes self-instrumentation.
    Zero substantive first-party matches. defenseclaw_local
    runs Linux systems but the THN relay does not enumerate
    specific file paths, hashes, or IPs that could be used to
    author a detection sentinel. Sygnia primary not directly
    retrieved; flag for next-sweep retrieval. Per Hard Rule 8:
    silence is not disconfirming. First-party precedence does
    NOT apply.

single_source_veto_applied: true  # Sygnia primary through single THN relay
wep_ceiling: likely  # Per veto + B2 anchor
wep_layered:
  sygnia_documents_velvet_ant_campaign_layer: likely  # Per veto + B2
  9_pam_variants_modified_openssh_technical_primitives_layer: likely  # Per veto + B2
  10_year_dwell_2016_to_2026_layer: likely  # Per veto + B2
  east_asia_air_gapped_victim_layer: likely  # Per veto + B2
  velvet_ant_china_nexus_per_sygnia_layer: likely  # Per veto + B2; conservative on "China-nexus" not a specific unit-attribution
  ad_direct_relevance: very_unlikely  # Verifiable absence
  ad_structural_relevance_via_universal_pam_openssh_class: roughly_even_chance  # Structural; not source-attested
  ad_extrapolation_from_east_asia_to_ad_prime_BLOCKED: not_assessed_per_hard_rule_2
  detection_engineering_callout_pam_fim_openssh_attestation_value: roughly_even_chance  # Operationally meaningful but not source-attested

inclusion:
  eligible_for:
    - daily_brief_action  # B2 meets action threshold; Other Signal section item
    - weekly_synthesis  # Detection-engineering surfaces are Threat Detection Weekly content
    - actor_profile_update  # /new-actor candidacy flag (operator decision pending)
  flash_eligible: false  # No A&D-prime targeting + no CVE + no active US-prime exploitation = below FLASH triggers
  flash_threshold_met: true  # B2 meets B2 threshold; held for afternoon brief per scope (not FLASH-shaped)

graded_at: 2026-06-12T16:40:00-04:00

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "Velvet Ant (China-nexus, NOT in Archimedes roster) PAM and OpenSSH backdoor campaign on air-gapped East Asia victim; ~10-year dwell since 2016; Sygnia primary via THN relay; detection-engineering callout for Linux fleets"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-12-pm-004
  attribution_claims:
    - claimed_actor: Velvet Ant
      claimed_attribution: China-nexus (Sygnia primary characterization)
      claimed_by_sources: [sygnia_primary_via_thehackernews_relay]
      requires_analyst_review: true
      note: "Velvet Ant NOT in roster. Sygnia framing is 'China-nexus' / 'China-linked' — NOT specific PLA/MSS unit. Archimedes does NOT cross-walk to roster actors. /new-actor candidacy operator-flagged."

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: true  # Velvet Ant /new-actor candidacy + detection-engineering surfaces for A&D-prime Linux fleets warrant SAT-KAC assumption check on structural-extrapolation framing
analyst_review_complete: true  # SAT-KAC applied 2026-06-12T17:25; 2 Test classifications (A2 supply-chain overlap; A7 Sygnia primary retrieval) + 3 Qualify; structural-relevance framing must hedge per analytic notes; /new-actor candidacy DEFER pending Sygnia primary retrieval at next sweep
analyst_review_run_id: analyst-20260612-172500
red_team_review_required: false  # WEP "likely" per veto; not very_likely+ trigger for red-team per doctrine
red_team_review: null

actor_profile_handoff:
  new_actor_candidacy_flagged: true
  candidate_name: Velvet Ant
  candidate_attribution: China-nexus
  candidate_research_lineage: Sygnia (2024 F5 BIG-IP + 2024 CVE-2024-20399 Cisco NX-OS + 2026 PAM/OpenSSH login-system campaign)
  operator_decision_pending: true
  prior_candidacy_flags_in_corpus:
    - OceanLotus / APT32 (raw-2026-06-11-am-001)
    - UNC1069 (source-health notes from 2026-05-09)
    - UNC6692 (source-health notes from 2026-05-09)
    - ShinyHunters (finding-2026-06-10-0012 / finding-2026-06-11-flash1200-0001 / finding-2026-06-11-0006 / finding-2026-06-12-0001)

vuln_tracker_handoff:
  prior_velvet_ant_cve_lineage:
    - CVE-2024-20399 (Cisco NX-OS zero-day, 2024)
    - 2024 F5 BIG-IP exploitation (CVE reference pending dossier check)
  no_new_cve_in_this_finding: true

analysis_sections:
  sat_ach: null  # ACH not invoked — only one in-window primary (Sygnia via THN); attribution layer is at "China-nexus" framing per single primary, no competing actor hypothesis in cited sources (Hard Rule 2 prevents originating one). KAC is the appropriate SAT here.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        Velvet Ant's PAM and OpenSSH backdoor tradecraft (9 PAM-module
        variants + modified OpenSSH credential-and-command logging with
        hidden disable switch) is structurally relevant to A&D-prime Linux
        fleets — the 9-variant backdoored PAM + modified OpenSSH primitives
        are detection-engineering-rich material defenders should be aware
        of even though A&D-prime targeting is not source-attested.
      analyzed_at: 2026-06-12T17:25:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Pre-publication review for afternoon brief inclusion. Velvet Ant is
        NOT in roster; Sygnia primary not directly retrieved; THN is single
        in-window publisher. Structural-relevance framing carries implicit
        assumptions that need surfacing before brief propagates the framing.

      assumptions:
        - id: A1
          statement: >
            A&D-prime Linux fleets run PAM and OpenSSH at sufficient density
            and configuration overlap with the East Asia victim that the
            same 9-variant PAM tampering + OpenSSH credential-logging
            primitives would be operationally meaningful for A&D-prime SOCs.
          category: capability
          stated: true
          why_must_be_true: >
            The structural-relevance claim depends on the tradecraft being
            executable against A&D-prime Linux fleets the same way it
            executed against the East Asia victim. PAM and OpenSSH are
            near-universal on Linux but A&D-prime Linux fleets may run
            RHEL/RHEL-derivative + STIG hardening + endpoint EDR coverage
            patterns very different from the unnamed East Asia victim's
            configuration. The actor's specific primitives may not port
            cleanly.
          when_could_be_false: >
            If A&D-prime Linux fleets run substantially hardened PAM
            stacks (STIG-compliant; PAM module integrity monitoring;
            SELinux MAC), the specific 9-variant PAM-module-replacement
            primitive may not be portable without significant rework.
            Equally, A&D-prime fleets running heavy EDR coverage on
            Linux servers may catch the OpenSSH binary modification at
            file-integrity layer regardless of the actor's specific
            tradecraft.
          evidence_for:
            - "Structural inference — PAM is the universal Linux authentication primitive; OpenSSH is near-universal for remote admin"
          evidence_against:
            - "No source-attested deployment-density evidence for Velvet Ant in A&D"
            - "East Asia victim configuration not enumerated in THN relay"
          confidence: low
          centrality: critical
          classification: qualify

        - id: A2
          statement: >
            A&D-prime Linux supply chains overlap with the East Asia
            victim's supply chain enough that initial access vectors
            (which Sygnia/THN does NOT enumerate in the relayed summary)
            would be approximately portable.
          category: capability
          stated: false
          why_must_be_true: >
            For the East Asia campaign to be even loosely indicative of
            future A&D-prime targeting, the initial-access surface must
            be approximately shared. If the East Asia victim was reached
            via a regional supply-chain vector (e.g., compromise of a
            China-based MSP serving that region), the A&D-prime fleet
            sits behind entirely different supply-chain surfaces.
          when_could_be_false: >
            If the East Asia victim was reached via regional/local
            supply-chain (e.g., a specific MSP, software vendor, or
            third-party support agreement constrained to East Asia),
            the campaign tradecraft demonstrates capability but not
            access-vector portability to A&D-prime.
          evidence_for: []
          evidence_against:
            - "Initial-access vector NOT enumerated in THN relay"
            - "Sygnia primary not directly retrieved — initial access may be in primary but not relayed"
            - "Velvet Ant 2024 lineage (F5 BIG-IP, Cisco NX-OS) targets specific appliance classes; 2026 PAM/OpenSSH campaign on air-gapped victim is novel access pattern"
          confidence: unknown
          centrality: critical
          classification: test

        - id: A3
          statement: >
            Velvet Ant has the intent or operational selection criteria
            that would lead them to target a US A&D-prime — i.e., the East
            Asia campaign is indicative of broader China-nexus targeting
            patterns rather than a region-specific operation.
          category: intent
          stated: false
          why_must_be_true: >
            Capability without intent doesn't predict A&D-prime targeting.
            The structural-relevance framing implicitly assumes Velvet
            Ant's victim selection extends beyond East Asia.
          when_could_be_false: >
            If Velvet Ant's operational mandate is region-specific (East
            Asia intelligence; specific country/sector mandate), the
            tradecraft is portable in principle but the actor itself
            won't reach A&D-prime targets in window.
          evidence_for:
            - "China-nexus attribution carries general adversary-priority signal"
            - "Velvet Ant 2024 F5 + Cisco NX-OS lineage suggests willingness to operate against globally-distributed appliance victims, not just East Asia"
          evidence_against:
            - "Sygnia framing names only East Asia in this campaign"
            - "Hard Rule 2 BLOCKS extrapolation from East Asia to A&D-prime"
          confidence: low
          centrality: material
          classification: qualify

        - id: A4
          statement: >
            Sygnia's "China-nexus" attribution language is reliable as a
            tradecraft-stability anchor — i.e., the 9-PAM-variant + OpenSSH
            tradecraft genuinely belongs to a single coherent actor named
            Velvet Ant, not a fuzzy cluster of activity Sygnia has tagged
            under the Velvet Ant label.
          category: actor_continuity
          stated: false
          why_must_be_true: >
            The "structurally relevant" framing collapses if Velvet Ant
            is actually a fuzzy cluster — different sub-clusters may use
            different primitives, and the 9-PAM-variant set may not be
            representative of Velvet Ant's broader tradecraft.
          when_could_be_false: >
            If "Velvet Ant" is a Sygnia-internal tag covering related-
            but-distinct campaigns (a not-uncommon pattern with single-
            vendor APT tracking), the East Asia tradecraft characterizes
            a specific operation rather than the actor as a whole.
          evidence_for:
            - "Sygnia has institutional research lineage on Velvet Ant since at least 2024"
          evidence_against:
            - "No second IR firm corroboration of Velvet Ant as a coherent actor"
          confidence: medium
          centrality: material
          classification: qualify

        - id: A5
          statement: >
            The detection-engineering primitives (PAM-module file-integrity
            monitoring; OpenSSH binary attestation; secret-password-
            acceptance behavioral anomaly) are deployable on A&D-prime
            Linux fleets without significant additional engineering work.
          category: visibility
          stated: true
          why_must_be_true: >
            The "detection-engineering-rich" framing assumes the
            primitives translate into deployable SOC controls.
          when_could_be_false: >
            File-integrity monitoring on PAM modules is uncommon at scale
            because PAM modules are routinely updated via package
            management (high false-positive surface). OpenSSH binary
            attestation requires baseline integrity infrastructure many
            A&D-prime fleets don't yet operate at the depth needed.
          evidence_for:
            - "PAM modules and OpenSSH binaries are well-known FIM/attestation targets in mature Linux SOC programs"
          evidence_against:
            - "Mature Linux endpoint security at A&D-prime scale is uneven (Windows EDR is more advanced)"
          confidence: medium
          centrality: peripheral
          classification: sound

        - id: A6
          statement: >
            The dwell-time claim (earliest traces 2016, ~10 years) is a
            transferable indicator of Velvet Ant's operational discipline
            — i.e., A&D-prime SOCs should expect long-dwell adversary
            behavior from this actor class even if Velvet Ant itself
            never reaches them.
          category: ttp_patterns
          stated: false
          why_must_be_true: >
            Reading dwell-time as a class-level signal (rather than a
            campaign-specific outlier) generalizes the lesson beyond the
            specific actor.
          when_could_be_false: >
            10-year dwell is exceptional even for nation-state APTs;
            generalizing it as a class signal may overweight an outlier.
          evidence_for:
            - "Multi-year dwell is consistent with prior Velvet Ant lineage (2024 F5 + Cisco NX-OS multi-year campaigns)"
            - "Long-dwell tradecraft is generally consistent with China-nexus APT pattern (per separate corpus on APT41, Volt Typhoon)"
          evidence_against:
            - "10-year dwell is exceptional; treating as class signal risks overfitting"
          confidence: medium
          centrality: peripheral
          classification: sound

        - id: A7
          statement: >
            Sygnia primary research (not directly retrieved this sweep)
            does NOT contain materially contradicting context (e.g.,
            constraint to East Asia regional mandate; named-victim
            sector limited to financial services; tradecraft only
            effective against specific Linux distribution).
          category: source_reliability
          stated: false
          why_must_be_true: >
            Acting on the THN relay assumes the THN summary captures
            the operationally meaningful elements of Sygnia primary.
          when_could_be_false: >
            Sygnia primary may carry sector-specific constraints,
            distribution-specific tradecraft, or other context that
            THN's summary stripped.
          evidence_for: []
          evidence_against:
            - "Sygnia primary not directly retrieved at sweep"
            - "Single THN relay is documented to occasionally elide constraints from primary research"
          confidence: low
          centrality: material
          classification: test

      classifications_summary:
        sound: 2
        qualify: 3
        test: 2
        reject: 0

      remediation:
        status: proceed_with_qualifying_caveats
        qualifying_caveats:
          - >
            Structural-relevance framing must be hedged with "primitives are
            portable in principle; A&D-prime applicability depends on
            initial-access vector portability (not enumerated in THN relay)
            and on fleet-configuration overlap with East Asia victim (also
            not enumerated)."
          - >
            "China-nexus" attribution language must be carried verbatim;
            Archimedes does NOT cross-walk to APT41 / Volt Typhoon / Salt
            Typhoon / APT40 even when the tradecraft has surface similarity.
          - >
            Detection-engineering callout (PAM FIM; OpenSSH attestation;
            secret-password-acceptance anomaly) is operationally meaningful
            and brief-includable, but Sygnia primary direct retrieval at
            next sweep is a hard prerequisite for any actor-profile-
            scaffolding work.
        test_required: >
          A2 (supply-chain overlap) and A7 (Sygnia primary not retrieved)
          are both Test classifications. A2 cannot be cheaply tested at
          this sweep without primary retrieval; A7 is testable via
          Sygnia primary direct retrieval at next sweep. Recommend the
          librarian flag Sygnia primary retrieval as a Mode 2 collector
          task for tomorrow's 07:30 pre-brief sweep. Brief inclusion can
          proceed with qualifying caveats; actor-profile scaffolding
          (the /new-actor candidacy decision) should wait for primary
          retrieval per A7.
        next_action: >
          Brief inclusion approved with caveats. /new-actor candidacy
          decision deferred pending Sygnia primary retrieval. Sygnia
          primary blog (https://www.sygnia.co/blog/) flagged for
          next-sweep collector work.

      recommended_wep_after_test:
        if_A2_confirmed_supply_chain_overlap: >
          Lift structural-relevance framing from "roughly even chance" to
          "likely"
        if_A2_disconfirmed_supply_chain_specific_to_east_asia: >
          Drop A&D-prime structural-relevance framing entirely; keep only
          generic Linux-fleet detection-engineering callout
        if_A7_confirmed_sygnia_primary_consistent_with_thn_relay: >
          Proceed to /new-actor candidacy evaluation with qualifying
          caveats per A4
        if_A7_disconfirmed_sygnia_primary_carries_material_constraints: >
          Revise finding with primary-source-attested constraints;
          rerun KAC

      new_actor_candidacy_recommendation:
        recommended_action: defer_pending_sygnia_primary_retrieval
        rationale: >
          Velvet Ant warrants /new-actor candidacy escalation in principle
          (Sygnia institutional research lineage; multi-year multi-target-
          class campaign pattern; "China-nexus" attribution with
          distinctive tradecraft). However, the THN relay does not
          enumerate enough constraint context to support a quality first-
          pass profile, and single-vendor APT tracking has a documented
          history of fuzzy cluster naming (A4). Sygnia primary direct
          retrieval is a hard prerequisite. Recommend defer for one
          sweep cycle; if primary retrieved tomorrow and consistent with
          relay, candidacy escalation to operator decision is justified.
          Note Velvet Ant joins existing pending candidates (OceanLotus,
          UNC1069, UNC6692, ShinyHunters); queue length warrants
          consolidated operator escalation.

tlp: CLEAR
published_in_briefs: [2026-06-12-afternoon]
retracted: false
retraction_brief_id: null
---

# Sygnia documents Velvet Ant (China-nexus, NOT in Archimedes roster) backdoor of Linux PAM and OpenSSH on air-gapped East Asia victim — ~10-year dwell; 9 PAM-module variants; modified OpenSSH credential-and-command logging with hidden disable switch; /new-actor candidate

## Summary

Sygnia has documented (via The Hacker News relay on 2026-06-12) a China-nexus group tracked as Velvet Ant that backdoored the Pluggable Authentication Modules (PAM) and OpenSSH components of a victim's Linux login system. Sygnia identifies nine distinct backdoored PAM module variants and OpenSSH modifications that log credentials and every command typed, with an operator-side disable switch. The victim network had no direct Internet access (air-gapped or isolated); earliest traces date to 2016, indicating approximately a decade of unbroken access. The victim is located in East Asia per Sygnia's prior public lineage; no specific sector is named in the THN summary. Velvet Ant is NOT in the Archimedes roster and Sygnia's characterization is "China-nexus" — not a specific PLA/MSS unit — so Hard Rule 2 binds Archimedes against cross-walking to roster actors. The tradecraft (hiding inside the Linux login system itself) is detection-engineering-rich for A&D-prime Linux fleets even though A&D-prime extrapolation from this East Asia campaign is blocked.

## Sources

### The Hacker News (thehackernews, digraph: B provisional) relaying Sygnia primary

- URL: `https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html`
- Published: 2026-06-12T14:17 EDT (18:17 UTC)
- Key claim: Velvet Ant backdoored PAM (9 variants) and OpenSSH (credential-and-command logging) on air-gapped East Asia victim; ~10-year dwell since 2016; "China-nexus" / "China-linked" attribution per Sygnia primary. Sygnia primary not directly retrieved this sweep (flag for next pass).

## Technical detail

- **PAM (Pluggable Authentication Modules):** main PAM login module replaced with backdoored copies. Sygnia documents nine separate variants of the backdoored module.
- **OpenSSH:** programs modified to log credentials and every command typed; some variants accept secret passwords; others quietly record real usernames and passwords during legitimate logins.
- **Hidden disable switch:** the credential/command logging functionality includes an operator-side switch to disable it on demand (operational discipline against forensic surface).
- **Persistence philosophy:** the actor "hid inside the Linux login system itself" rather than on endpoints/servers defenders watch most closely — Sygnia analytic framing.
- **Dwell time:** earliest traces date to 2016; ~10 years of unbroken access on the victim network.
- **Victim profile:** air-gapped or isolated network; located in East Asia per Sygnia prior lineage; no specific country or sector named in THN summary.
- **Prior Velvet Ant public lineage (per article reference):** 2024 F5 BIG-IP appliance exploitation; 2024 CVE-2024-20399 Cisco NX-OS zero-day. Sygnia has tracked Velvet Ant since at least 2024. Migration pattern between target classes (endpoints → legacy servers → network appliances → login subsystem) within the same victim environment over multi-year campaigns.

## Hard Rule 2 — attribution discipline (BINDING)

- Velvet Ant is NOT in Archimedes _roster.yaml (verified against full 22-actor roster at grading time).
- Sygnia's verbatim attribution per THN is "China-nexus group" / "China-linked." NOT a specific PLA / MSS / unit naming. NOT mapped to APT41 / Volt Typhoon / Salt Typhoon / APT40.
- Archimedes does NOT cross-walk Velvet Ant to existing roster actors.
- /new-actor candidacy is flagged for operator decision. This finding does NOT initiate /new-actor scaffolding.
- A&D-prime extrapolation from East Asia campaign is BLOCKED. Archimedes notes structural Linux-fleet defensive relevance without asserting A&D-prime targeting.

## A&D / DIB relevance

- **Direct:** none. No A&D-prime victim named.
- **Structural:** Velvet Ant's "hide in the login system itself" tradecraft is exactly the kind of long-dwell capability A&D-prime SOCs need to defend against. The 9-variant backdoored PAM + modified OpenSSH primitives are detection-engineering-rich material:
  - File-integrity monitoring on PAM modules.
  - OpenSSH binary attestation (e.g., package-fingerprint baselining; behavioral anomaly on command-logging patterns).
  - Behavioral anomaly detection for secret-password-acceptance patterns.
- **A&D-prime exposure inference:** structurally meaningful (any A&D-prime Linux fleet runs PAM + OpenSSH; the supply chain is the same supply chain Velvet Ant targeted) but Hard Rule 2 binds against extrapolating A&D-prime targeting from this East Asia campaign.

## IOCs surfaced

None enumerated in THN relay (no file paths, hashes, or IPs). Sygnia primary blog (https://www.sygnia.co/blog/) flagged for next-sweep direct retrieval — Sygnia primary likely carries richer IOC content (file paths, file hashes, behavioral signatures) not propagated through THN summary.

## Relationship to existing findings

- **First Velvet Ant appearance in Archimedes corpus** — no prior corpus reference at grading time (per operator check against finding-2026-06-11-0003 OceanLotus/APT32 + UNC1069/UNC6692 flagged candidates).
- **/new-actor candidacy queue:** Velvet Ant joins prior pending candidates (OceanLotus, UNC1069, UNC6692, ShinyHunters). Operator decision pending across all four.
- **Detection-engineering surfaces for Threat Detection Weekly synthesis:** PAM module file-integrity monitoring, OpenSSH binary attestation, secret-password-acceptance behavioral pattern.

## Open questions for analyst

- /new-actor decision on Velvet Ant (operator).
- SAT-KAC assumption check: the "structurally relevant to A&D-prime Linux fleets" framing carries an implicit assumption that A&D-prime Linux supply chains overlap with the East Asia victim's supply chain. Worth surfacing.
- Watch: Sygnia primary direct retrieval at next sweep (high-value; likely carries IOCs not in THN relay).
- Watch: second IR-firm corroboration of Velvet Ant attribution or technical primitives.
- Watch: any A&D-prime SOC reporting of PAM-module integrity anomalies in the next 60 days.

## Analytic notes (from analyst review)

KAC on the structural-relevance framing surfaced seven assumptions, two of which classified as Test (A2: A&D-prime Linux supply chains overlap with the East Asia victim's; A7: Sygnia primary not directly retrieved this sweep is consistent with the THN relay) and three as Qualify (A1: fleet-configuration overlap; A3: actor intent beyond East Asia mandate; A4: Velvet Ant is a coherent actor not a fuzzy Sygnia-internal cluster). The structural-relevance claim is portable in principle but the East Asia victim's initial-access vector and fleet configuration are not enumerated in the THN relay — A&D-prime applicability cannot be source-attested from this sweep alone. Hard Rule 2 binding on East Asia → A&D-prime extrapolation is preserved; the brief should carry "primitives are portable in principle; A&D-prime applicability bounded by access-vector and configuration overlap, neither of which is enumerated" framing.

Detection-engineering callout (PAM module FIM; OpenSSH binary attestation; secret-password-acceptance behavioral anomaly) is operationally meaningful and brief-includable as defender-awareness content — A5 classifies as Sound. Briefer should NOT escalate the structural-relevance framing beyond "operationally significant primitive set; A&D-prime applicability depends on access-vector and configuration overlap not enumerated in the THN relay."

/new-actor candidacy: recommend defer pending Sygnia primary direct retrieval at next sweep (A7 Test classification). The candidate queue is already at five (OceanLotus, UNC1069, UNC6692, ShinyHunters, now Velvet Ant); consolidated operator escalation warranted. WEP unchanged from grader's "likely" ceiling.
