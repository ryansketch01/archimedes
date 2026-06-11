---
id: finding-2026-06-11-0009
finding_id: finding-2026-06-11-0009-thn-prodaft-microsoft-storm-2697-gentlemen-ransomware-yapaev-larva368-material-extension-on-0017
title: "The Gentlemen Ransomware material extension — PRODAFT (Phantom Mantis tracking) + Microsoft (Storm-2697 tracking) independent attribution corroboration of Krebs OSINT-de-anonymization Alexander Yapaev / Izhevsk identification; PRODAFT names LARVA-368 alias + 478 victim count claim + prior LockBit/Qilin/Medusa RaaS affiliate history (LockBit roster #015 dossier touchpoint); MATERIAL-EXTENSION on finding-2026-06-10-0017"
date: 2026-06-11
created_at: 2026-06-11T17:05:00-04:00
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
  # ---- ATTRIBUTION CORROBORATION LAYER (material extension on 0017) ----
  prodaft_independently_tracks_the_gentlemen_as_phantom_mantis: B2  # The Hacker News (provisional B) relay of PRODAFT (provisional B vendor research) — second-vendor independent tracking of the same operator beyond Krebs Check Point Intel 471 Flashpoint cluster from 0017
  microsoft_independently_tracks_the_gentlemen_as_storm_2697: B2  # The Hacker News relay of Microsoft-tier tracking ID — MSTIC Storm-NNNN designations are MSTIC-canonical at originator layer (A); relay-tier B-grade
  prodaft_plus_microsoft_corroborate_krebs_check_point_yapaev_identification: B2  # MATERIAL INDEPENDENT corroboration of finding-2026-06-10-0017's OSINT-de-anonymization chain
  prodaft_names_larva_368_designation_for_yapaev_operator: B2  # The Hacker News relay of PRODAFT operator-designation
  yapaev_real_identity_alexander_andreevich_yapaev_36_izhevsk_russia_consistent_with_0017_krebs: A2  # Carry-forward from finding-2026-06-10-0017 (Krebs primary OSINT identification); PM-cycle PRODAFT confirms identity at B2
  # ---- OPERATOR-HISTORY LAYER (material new content) ----
  yapaev_previous_alias_armcorp_per_prodaft: B3  # Single-vendor PRODAFT-originated alias; new to corpus
  yapaev_transitioned_from_raas_affiliate_to_independent_operator_july_2025: B2  # PRODAFT vendor research; single-vendor on the transition-date specifics; consistent with 0017's Krebs OSINT timeline
  yapaev_prior_lockbit_affiliate_tenacious_mantis: B2  # PRODAFT vendor tracking; LockBit is in roster (#015, HIGH); material touchpoint to roster maintenance
  yapaev_prior_qilin_affiliate_pestilent_mantis: B2  # PRODAFT vendor tracking; Qilin NOT in roster
  yapaev_prior_medusa_affiliate_venomous_mantis: B2  # PRODAFT vendor tracking; Medusa NOT in roster
  # ---- VICTIM SCALE LAYER (PRODAFT/Microsoft tracking) ----
  the_gentlemen_478_victim_count_claimed: B2  # PRODAFT-attested number through THN relay; lifts above 0017's "240+ in 2026" framing per Check Point; PRODAFT methodology not directly retrieved this sweep
  # ---- TECHNICAL LAYER (PRODAFT vendor research) ----
  go_binary_with_garble_obfuscation: B2  # PRODAFT-attested
  x25519_key_exchange_plus_xchacha20_encryption_scheme: B2  # PRODAFT-attested
  multi_platform_targeting_windows_linux_esxi_lvm: B2  # PRODAFT-attested
  spread_argument_flag_converts_single_host_to_worm: B2  # PRODAFT-attested; OPERATIONAL DEFENDER PIVOT — worm-like propagation flag is defensible at endpoint command-line audit layer
  dwell_time_2_to_6_weeks: B3  # PRODAFT operational characterization
  # ---- GEOGRAPHIC LAYER ----
  victim_distribution_only_13_percent_us_based: B2  # PRODAFT scanning/tracking attestation
  victim_distribution_majority_thailand_uk_brazil_germany_india: B2  # PRODAFT scanning/tracking
  # ---- ROSTER CROSSWALK LAYER (Hard Rule 2 binding) ----
  lockbit_in_roster_id_015_high_threat_level: A1  # Verifiable per direct roster file retrieval; LockBit per roster check Session 1+ migration entry #015
  yapaev_as_former_lockbit_affiliate_now_independent_operator: B2  # PRODAFT attribution corroborated by Krebs (finding-2026-06-10-0017)
  hard_rule_2_does_NOT_extend_lockbit_dossier_to_cover_the_gentlemen_independent_operations: A1  # Yapaev is FORMER affiliate; current Gentlemen operations are independent per PRODAFT framing; Hard Rule 2 binding
  qilin_not_in_archimedes_roster: A1  # Verifiable absence
  medusa_not_in_archimedes_roster: A1  # Verifiable absence
  # ---- A&D / DIB RELEVANCE LAYER ----
  no_ad_prime_named_as_victim: A1  # Verifiable absence
  no_defense_sector_targeting_per_source: A1  # Verifiable absence
  ad_relevance_watchlist_signal_only: A1  # Verifiable absence at substantive layer
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / Usually Reliable B-grade
  source). The Hacker News (provisional B per source-grades.yaml)
  is the sole in-window publisher relaying PRODAFT (provisional B
  vendor research; NOT directly retrieved) and Microsoft (Storm-
  2697 tracking ID at MSTIC ratified A originator layer; relay-tier
  B-grade through THN).

  KEY GRADING REASONING — MATERIAL EXTENSION on
  finding-2026-06-10-0017:

    (1) INDEPENDENT ATTRIBUTION CORROBORATION on Yapaev identity:
        finding-2026-06-10-0017 anchored on Krebs (B) OSINT-de-
        anonymization chain (Hastalamuerte / Zeta88 →
        Alexander Yapaev, Izhevsk, Udmurt Republic, B3 identity
        layer) via Check Point + Intel 471 + Flashpoint cluster
        coverage. PM-cycle PRODAFT (independent vendor) names
        SAME real identity (Alexander Andreevich Yapaev, 36,
        Izhevsk, Russia) PLUS distinct operator-designation
        (LARVA-368) AND distinct group-tracking (Phantom Mantis).
        PM-cycle Microsoft (MSTIC, ratified A at originator layer)
        independently tracks SAME operator as Storm-2697.
        THREE independent vendor-tier attributions converging on
        SAME real identity = MATERIAL EXTENSION of 0017's
        identification confidence. Conservative B2 anchor because
        PRODAFT primary NOT directly retrieved; THN relay tier
        B-grade.

    (2) IDENTIFICATION-CONFIDENCE LIFT EVENT: 0017 was anchored
        on Krebs B (B3 at identity layer due to OSINT-via-
        breadcrumb-chain class). PM-cycle PRODAFT + Microsoft
        independent corroboration through THN relay LIFTS identity
        layer to B2 (Krebs + PRODAFT independent attribution; THN
        relay of Microsoft Storm-2697 as MSTIC-tier confirmation).
        At the strict skill Step 4 reading, the three sources are
        publisher-independent at relay layer; PRODAFT and Check
        Point are evidence-independent (different vendor research
        teams, different evidence bases); Microsoft is canonical-
        on-own-tracking-ID. The aggregate cluster across 0017 +
        this finding genuinely satisfies the independence test
        on the Yapaev identity layer.

    (3) NEW MATERIAL CONTENT (beyond 0017 corpus state):
        - LARVA-368 operator designation (PRODAFT-originated)
        - Phantom Mantis group tracking (PRODAFT)
        - Storm-2697 group tracking (Microsoft)
        - ArmCorp prior alias (PRODAFT)
        - Transition timeline: RaaS affiliate → independent
          operator July 2025 (PRODAFT-specific date)
        - Prior LockBit affiliate (Tenacious Mantis) (PRODAFT)
        - Prior Qilin affiliate (Pestilent Mantis) (PRODAFT)
        - Prior Medusa affiliate (Venomous Mantis) (PRODAFT)
        - 478 victim count (PRODAFT-attested through THN relay;
          lifts above 0017's Check Point "240+ in 2026" framing)
        - Technical detail: Go binary + Garble obfuscation +
          X25519/XChaCha20 + Windows/Linux/ESXi/LVM + `--spread`
          worm-flag + 2-6 week dwell
        - Geographic: only ~13% U.S.-based; majority
          Thailand/UK/Brazil/Germany/India

    (4) ROSTER CROSSWALK (Hard Rule 2 binding):
        - LockBit IS in roster (#015, HIGH per migration from
          C3PO intel-repository per _roster.yaml comment Session
          1). Yapaev's prior LockBit affiliation is material to
          LockBit dossier maintenance (next-review-due 2026-07-10
          per finding-2026-06-10-0017 record).
        - Hard Rule 2 binding: do NOT extend LockBit dossier to
          cover Yapaev's current INDEPENDENT Gentlemen operations.
          Per PRODAFT framing, Yapaev transitioned away from
          LockBit (and Qilin and Medusa) to operate independently
          July 2025. Current Gentlemen operations are NOT LockBit
          operations.
        - Qilin and Medusa NOT in roster. Material is /new-actor
          candidacy awareness; same operator-decision-pending
          status as 0017.

    (5) WHY THIS IS NOT ANTI-NOISE RESTATEMENT (vs.
        finding-2026-06-10-0017):
        - 0017 was Krebs (B) primary on OSINT-de-anonymization
          chain to Yapaev identity, with Check Point + Intel 471
          + Flashpoint cluster-coverage corroborators.
        - This finding adds PRODAFT (independent vendor) AND
          Microsoft (Storm-2697 MSTIC tracking) as DISTINCT
          vendor-tier attribution sources NOT cited in 0017.
        - 478 victim count materially extends 0017's "240+ in
          2026" framing.
        - LARVA-368 / Phantom Mantis / Storm-2697 / ArmCorp
          designations are NEW to corpus.
        - Technical detail (Go/Garble, X25519/XChaCha20, spread-
          flag worm capability) is NEW to corpus.
        - Geographic distribution (~13% U.S.-based; majority
          Thailand/UK/Brazil/Germany/India) is NEW to corpus.
        - Conclusion: MATERIAL EXTENSION, not anti-noise
          restatement. Promote.

  SINGLE-SOURCE VETO APPLICATIONS:
    - APPLIES on specific PRODAFT-originated operator designations
      (LARVA-368 / Phantom Mantis / ArmCorp prior alias) and
      transition timeline (RaaS affiliate → independent July 2025)
      and technical detail (Go/Garble, X25519/XChaCha20, spread-
      flag worm, 2-6 week dwell). PRODAFT primary not directly
      retrieved.
    - APPLIES on Microsoft Storm-2697 designation (Microsoft-
      canonical at originator layer; relay-tier B through THN; no
      second-vendor corroboration of Storm-2697 designation
      itself).
    - NOT APPLIED on Yapaev identity layer (independence test
      passes via Krebs + PRODAFT + Microsoft three-vendor
      convergence through publisher-independent and evidence-
      independent paths).
    - NOT APPLIED on verifiable-absence claims (no A&D-prime
      victim named; no defense-sector targeting per source).

  Hard Rule 2 binding constraint: PRESERVED — Archimedes does NOT
  extend LockBit dossier to cover Yapaev's independent Gentlemen
  operations; LockBit prior-affiliate status preserved as
  PRODAFT-attested historical lineage with citation, NOT as
  current Gentlemen attribution. Qilin and Medusa NOT in roster;
  operator decision required on /new-actor candidacy. The Gentlemen
  /new-actor candidacy carries forward unchanged from 0017.

  Hard Rule 6 binding constraint: PRESERVED — at most one short
  paraphrase per source under 15 words. No verbatim quotes at
  finding-layer beyond PRODAFT designation labels (LARVA-368 /
  Phantom Mantis / Tenacious Mantis / Pestilent Mantis /
  Venomous Mantis) which are operator-designation tokens, not
  prose quotes.

  Hard Rule 7 binding constraint: PRESERVED — Yapaev is publicly
  named in PRODAFT vendor research + Krebs OSINT-de-anonymization
  per finding-2026-06-10-0017; LEGAL-POLICY data-handling table
  permits named threat actors (pseudonyms, aliases, group names)
  and corporate officers publicly named in incidents with source
  citation.

  Hard Rule 8 binding constraint: -7d@d first-party Splunk query
  on Yapaev + Gentlemen + LARVA-368 + Phantom Mantis + Storm-2697:
  10 events returned, all Archimedes self-instrumentation. Zero
  substantive first-party matches. Per Hard Rule 8: silence is
  not disconfirming. defenseclaw_local does not observably run
  systems matching the Gentlemen victim profile (~13% U.S.-based,
  majority Thailand/UK/Brazil/Germany/India). First-party
  precedence does NOT apply.

source_reliability:
  grade: B
  source_name: "The Hacker News (provisional B per source-grades.yaml) — sole in-window publisher relaying PRODAFT (provisional B vendor research; primary not directly retrieved) + Microsoft (Storm-2697 MSTIC tracking ID; ratified A at originator layer; relay-tier B through THN)"
  source_yaml_id: thehackernews
  grade_rationale: >
    The Hacker News is provisional B per source-grades.yaml (2026-
    05-14 first-citation; multi-cross-corroboration-cycle). PRODAFT
    is established threat-intelligence research provider with
    track record on operator-de-anonymization research (peer class
    to Mandiant / CrowdStrike / Intel 471 / Flashpoint /
    Check Point); provisional B starting grade pending direct
    primary retrieval. Microsoft MSTIC is ratified A at originator
    layer per source-grades.yaml; Storm-NNNN designations are
    MSTIC-canonical on own tracking.
  provisional: false
  cluster_secondary_sources:
    - source_yaml_id: prodaft-research
      grade: B
      provisional: true
      provisional_since: 2026-06-11
      provisional_72h_clock_expires: 2026-06-14T17:05:00-04:00
      grade_rationale: "PRODAFT is established threat-intelligence research provider with sustained operator-de-anonymization track record (peer class to Mandiant / CrowdStrike / Intel 471 / Flashpoint / Check Point). First Archimedes-corpus dedicated source ID via this finding. Conservative provisional B starting grade pending direct primary retrieval. Librarian handoff for source-grades.yaml addition. 72h ratification clock to 2026-06-14T17:05:00-04:00."
      role: originating_vendor_research_on_phantom_mantis_larva_368_yapaev_attribution_not_directly_retrieved
    - source_yaml_id: mstic
      grade: A
      provisional: false
      grade_rationale: "Pre-assigned A per source-grades.yaml; Microsoft MSTIC ratified at originator layer. Storm-2697 designation is MSTIC-canonical on own tracking ID. Relay-tier B through THN."
      role: independent_vendor_tracking_id_corroborator_at_originator_layer_a_relay_tier_b
    - source_yaml_id: krebs
      grade: B
      provisional: false
      grade_rationale: "Pre-assigned B per source-grades.yaml; carry-forward from finding-2026-06-10-0017 as canonical originating-publisher on Yapaev OSINT-de-anonymization chain."
      role: prior_finding_carry_forward_canonical_on_yapaev_identification_chain

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_finding_2026_06_10_0017_yapaev_identification_chain
    - probably_true_consistent_with_check_point_intel_471_flashpoint_cluster_coverage_from_0017
    - probably_true_no_contradicting_a_b_grade_source_at_sweep
    - probably_true_technical_claims_internally_coherent_go_garble_x25519_xchacha20_mechanism_class_plausible_for_modern_ransomware_family
    - probably_true_prior_affiliate_history_lockbit_qilin_medusa_consistent_with_raas_ecosystem_pattern
  checklist_NOT_passed_at_grade_1:
    - confirmed_independent_corroboration_at_substantive_evidence_basis_layer  # PASSES at Yapaev identity layer (three-vendor convergence via Krebs + PRODAFT + Microsoft through publisher-independent and evidence-independent paths); FAILS at PRODAFT-specific operator designations + transition timeline + technical detail layers (single-vendor PRODAFT-originated, primary not directly retrieved)
  rationale: >
    Cluster anchor B2 with MATERIAL EXTENSION on finding-2026-06-
    10-0017. PM-cycle PRODAFT + Microsoft independent attribution
    corroboration of Krebs Yapaev identification lifts identity
    layer to B2 across publisher-independent and evidence-
    independent paths. NEW material (PRODAFT operator
    designations, transition timeline, technical detail,
    geographic distribution, prior RaaS affiliate history) carries
    B2 anchor with single-source veto on PRODAFT-specific layers.
    Consistent with Krebs OSINT-de-anonymization chain + Check
    Point + Intel 471 + Flashpoint cluster coverage from 0017.
    Grade 1 (Confirmed) FAILS at PRODAFT-specific layers — single-
    vendor through single-publisher relay; primary not directly
    retrieved.

corroboration:
  independent_sources:
    - thehackernews  # publisher relay
    - prodaft-research  # primary not directly retrieved
    - mstic  # Storm-2697 MSTIC tracking ID at originator A; relay-tier B through THN
    - krebs  # carry-forward from finding-2026-06-10-0017 (Yapaev OSINT identification primary)
    - check-point  # carry-forward from 0017 (Gentlemen cluster coverage)
    - intel-471  # carry-forward from 0017 (forum-registration trace)
    - flashpoint  # carry-forward from 0017 (cluster coverage)
  independent: partial
  independent_at_substantive_evidence_basis_layer:
    yapaev_identity_layer: true   # Krebs + PRODAFT + Microsoft three-vendor convergence via publisher-independent + evidence-independent paths
    prodaft_specific_operator_designations_larva_368_phantom_mantis_armcorp: false  # Single-vendor PRODAFT-originated
    microsoft_storm_2697_designation: false  # Microsoft-canonical at originator layer; no second-vendor corroboration of Storm-2697 designation itself
    transition_timeline_raas_affiliate_to_independent_july_2025: false  # PRODAFT-specific date
    technical_detail_go_garble_x25519_xchacha20_spread_worm: false  # PRODAFT vendor research
    478_victim_count: false  # PRODAFT-attested through THN relay
    geographic_distribution_13_pct_us_majority_thailand_uk_brazil_germany_india: false  # PRODAFT scanning
  test_passed: >
    Yapaev identity layer is independently corroborated across
    Krebs + PRODAFT + Microsoft three-vendor convergence via
    publisher-independent and evidence-independent paths. This
    materially extends finding-2026-06-10-0017's identification
    confidence.
  test_failed: >
    PRODAFT-specific operator designations + transition timeline
    + technical detail + 478 victim count + geographic
    distribution all rest on single-vendor PRODAFT through
    single-publisher THN relay; PRODAFT primary not directly
    retrieved. Single-source veto applies on those layers.
    Microsoft Storm-2697 designation is Microsoft-canonical at
    originator layer but no second-vendor corroboration of the
    Storm-2697 designation itself; single-source veto applies
    on the designation as such (though the underlying actor it
    designates IS corroborated at identity layer).

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    Grader-side first-party Splunk query (-7d@d window across
    index=archimedes OR index=defenseclaw_local) on Yapaev +
    Gentlemen + LARVA-368 + Phantom Mantis + Storm-2697 +
    ransomware-related TTPs: 10 events returned, all Archimedes
    self-instrumentation (sourcetype archimedes:operation). Zero
    substantive first-party matches. Per Hard Rule 8: silence is
    not disconfirming. defenseclaw_local does not observably
    run systems matching the Gentlemen victim profile (~13%
    U.S.-based; majority Thailand/UK/Brazil/Germany/India).
    First-party precedence does NOT apply.

single_source_veto_applied: true
single_source_veto_detail: >
  APPLIES on PRODAFT-specific operator designations + transition
  timeline + technical detail + 478 victim count + geographic
  distribution — all rest on single-vendor PRODAFT through
  single-publisher THN relay; PRODAFT primary not directly
  retrieved.

  APPLIES on Microsoft Storm-2697 designation as such — Microsoft-
  canonical at originator layer but no second-vendor corroboration
  of the Storm-2697 designation itself (though underlying actor
  IS corroborated at identity layer).

  NOT APPLIED on Yapaev identity layer (Krebs + PRODAFT +
  Microsoft three-vendor convergence via publisher-independent
  and evidence-independent paths).

  NOT APPLIED on verifiable-absence claims (no A&D-prime victim
  named; no defense-sector targeting; LockBit roster #015,
  Qilin not in roster, Medusa not in roster).

wep_ceiling: likely
wep_layered:
  yapaev_real_identity_alexander_andreevich_yapaev_36_izhevsk_russia: very_likely  # Three-vendor convergence via Krebs + PRODAFT + Microsoft through publisher-independent + evidence-independent paths
  yapaev_as_the_gentlemen_operator: very_likely  # Same independence test passes
  yapaev_prior_lockbit_affiliate_status: likely  # PRODAFT-specific historical attribution; consistent with Krebs OSINT timeline from 0017
  yapaev_prior_qilin_affiliate_status: likely  # PRODAFT-specific; single-source veto
  yapaev_prior_medusa_affiliate_status: likely  # PRODAFT-specific; single-source veto
  yapaev_transition_from_raas_affiliate_to_independent_operator_july_2025: likely  # PRODAFT-specific timeline; single-source veto
  prodaft_phantom_mantis_designation: likely  # PRODAFT-canonical on own tracking ID; relay-tier through THN
  microsoft_storm_2697_designation: likely  # MSTIC-canonical on own tracking ID; relay-tier B; no second-vendor corroboration of designation as such
  prodaft_larva_368_operator_designation: likely  # PRODAFT-canonical on own tracking ID
  yapaev_armcorp_prior_alias: roughly_even_chance  # PRODAFT-specific; single-source veto
  the_gentlemen_478_victim_count: likely  # PRODAFT-attested through THN relay; lifts above 0017's "240+ in 2026" Check Point framing
  go_binary_garble_obfuscation: likely  # PRODAFT vendor research; technically plausible for modern ransomware family
  x25519_xchacha20_encryption_scheme: likely  # PRODAFT; technically plausible
  multi_platform_windows_linux_esxi_lvm_targeting: likely  # PRODAFT; consistent with modern ransomware ecosystem
  spread_argument_flag_converts_single_host_to_worm: likely  # PRODAFT; OPERATIONAL DEFENDER PIVOT
  dwell_time_2_to_6_weeks: roughly_even_chance  # PRODAFT operational characterization
  victim_distribution_only_13_pct_us_based: likely  # PRODAFT scanning
  victim_distribution_majority_thailand_uk_brazil_germany_india: likely  # PRODAFT scanning
  lockbit_roster_dossier_extension_to_cover_gentlemen_operations: very_likely_NOT  # Hard Rule 2 binding; Yapaev FORMER affiliate now independent operator
  no_ad_prime_named_as_victim: very_likely  # A1 verifiable absence
  no_defense_sector_targeting_per_source: very_likely  # A1 verifiable absence
  ad_relevance_watchlist_signal_only: very_likely  # A1

inclusion:
  eligible_for:
    - daily_brief_monitoring   # B2 clears B2 minimum; substantial material extension on 0017
    - weekly_synthesis
    - actor_profile_awareness  # LockBit roster #015 touchpoint; The Gentlemen /new-actor carry-forward awareness
inclusion_eligibility: yes
inclusion_rationale: >
  B2 cluster anchor + WEP "likely" on substantive operational
  claims. NOT eligible for daily_brief_action — no A&D-prime
  victim named; victim profile ~13% U.S.-based with majority
  Thailand/UK/Brazil/Germany/India; no DIB-direct exposure
  signal. Monitoring-tier + weekly synthesis + actor-profile
  awareness appropriate. LockBit roster dossier #015 touchpoint
  flagged for actor-profiler awareness without dossier extension
  (Hard Rule 2 binding).

# ============================================================================
# Hard Rule 2 — Attribution preserved
# ============================================================================
attribution: null
attribution_claims:
  - claimed_actor: The Gentlemen (PRODAFT: Phantom Mantis; Microsoft: Storm-2697)
    claim_type: vendor_attribution_chain_to_real_identity
    claim: "Operator real identity: Alexander Andreevich Yapaev, 36, Izhevsk, Russia"
    claimed_by_sources:
      - prodaft-research  # primary, not directly retrieved
      - mstic            # Storm-2697 tracking ID at originator A
      - thehackernews    # relay tier
      - krebs           # finding-2026-06-10-0017 carry-forward
      - check-point      # finding-2026-06-10-0017 carry-forward
      - intel-471        # finding-2026-06-10-0017 carry-forward
      - flashpoint       # finding-2026-06-10-0017 carry-forward
    independent_corroboration: true  # MATERIAL EXTENSION on 0017 via three-vendor convergence
    archimedes_attribution_origination_check: pass_per_hard_rule_2_vendor_attribution_preserved_with_citation_not_originated_by_archimedes
    roster_status: not_in_archimedes_roster_v2_as_of_2026_05_10_new_actor_candidate
  - claimed_actor: The Gentlemen / LARVA-368 / Phantom Mantis / Storm-2697 / ArmCorp prior alias
    claim_type: operator_alias_chain
    claim: "Multi-alias operator with prior RaaS affiliate history (LockBit Tenacious Mantis / Qilin Pestilent Mantis / Medusa Venomous Mantis), transitioned to independent operator July 2025"
    claimed_by_sources:
      - prodaft-research
      - thehackernews
    independent_corroboration: false  # PRODAFT-originated alias chain + transition timeline; single-vendor through single-publisher relay
    archimedes_attribution_origination_check: pass_per_hard_rule_2_vendor_attribution_preserved_with_citation
    lockbit_roster_dossier_extension_prohibited: true   # Hard Rule 2 binding; Yapaev FORMER LockBit affiliate now INDEPENDENT operator; current Gentlemen operations are NOT LockBit operations
attribution_rationale: >
  Hard Rule 2 binding: Archimedes does NOT originate attribution.
  Yapaev identity is independently corroborated across Krebs +
  PRODAFT + Microsoft three-vendor convergence; preserved as
  vendor-attested with citation. PRODAFT-specific operator
  designations (LARVA-368, Phantom Mantis, ArmCorp prior alias)
  and Microsoft Storm-2697 designation preserved as source-
  attested. Hard Rule 2 binding on LockBit dossier maintenance:
  Yapaev is FORMER affiliate (per PRODAFT framing); current
  Gentlemen operations are INDEPENDENT (post-July-2025
  transition); LockBit dossier #015 is NOT extended to cover
  Gentlemen operations. Qilin and Medusa NOT in roster; operator
  decision required on /new-actor candidacy for any of those
  groups separately. The Gentlemen /new-actor candidacy carries
  forward unchanged from finding-2026-06-10-0017.

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
  actors:
    - actor_name: The Gentlemen
      operator_real_identity: Alexander_Andreevich_Yapaev_36_Izhevsk_Russia
      aliases_per_prodaft: [LARVA-368, Phantom Mantis, ArmCorp]
      aliases_per_microsoft: [Storm-2697]
      aliases_carry_forward_from_finding_2026_06_10_0017: [Hastalamuerte, Zeta88]
      prior_raas_affiliate_history_per_prodaft:
        lockbit: Tenacious_Mantis
        qilin: Pestilent_Mantis
        medusa: Venomous_Mantis
      transition_to_independent_operator: 2025_07_per_prodaft
      victim_count_per_prodaft_through_thn_relay: 478
      geographic_distribution_per_prodaft:
        us_percent: ~13
        majority_geography: [Thailand, UK, Brazil, Germany, India]
      operator_designation_independence_corroboration_test:
        krebs_plus_prodaft_plus_microsoft_converge_on_yapaev_identity: true
        single_source_veto_on_designations_as_such: true
      roster_status: not_in_archimedes_roster_v2_as_of_2026_05_10_new_actor_candidacy_carry_forward
      lockbit_roster_dossier_extension_prohibited_per_hard_rule_2: true
  technical_iocs:
    - binary_class: Go_with_Garble_obfuscation
      source: prodaft_research_via_thn_relay
      single_source_veto_applies: true
    - encryption_scheme: X25519_key_exchange_plus_XChaCha20_encryption
      source: prodaft_research_via_thn_relay
      single_source_veto_applies: true
    - multi_platform_targeting: [Windows, Linux, ESXi, LVM]
      source: prodaft_research_via_thn_relay
      single_source_veto_applies: true
    - worm_capability_argument_flag: --spread
      source: prodaft_research_via_thn_relay
      defender_pivot: endpoint_command_line_audit_for_argv_pattern_dash_dash_spread_on_ransomware_class_binaries
      single_source_veto_applies: true
ioc_count: 4  # Actor + 3 technical IOCs (binary class, encryption scheme, worm flag)
iocs_summary: >
  Actor-attribution chain with three-vendor convergence on Yapaev
  identity layer. Four technical IOCs in PRODAFT vendor research
  layer (single-source veto applies). No hash, domain, or IP
  IOCs surfaced in B-grade relay tier. PRODAFT primary likely
  carries hash + infrastructure IOCs but was NOT directly
  retrieved this sweep.

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "The Gentlemen Ransomware MATERIAL EXTENSION — PRODAFT (Phantom Mantis / LARVA-368) + Microsoft (Storm-2697) independent corroboration of Krebs OSINT identification of Alexander Yapaev (Izhevsk, Russia); prior LockBit/Qilin/Medusa RaaS affiliate history; LockBit roster #015 dossier touchpoint per Hard Rule 2 binding"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-11-pm-005   # subset (1 of 4 cybercrime cluster components)
  raw_signal_decomposition_note: >
    Raw-signal pm-005 carries 4 cybercrime cluster components
    (OnyxC2 MaaS / The Gentlemen Ransomware / AudiA6 takedown /
    Nightmare Eclipse GreatXML). Per admiralty-grading skill
    Step 2 multi-claim halt + decomposition rule, each component
    is graded separately. This finding covers the Gentlemen /
    Yapaev / PRODAFT-Microsoft attribution-corroboration component.
    OnyxC2 (finding-2026-06-11-0010), AudiA6 (finding-2026-06-11-
    0011), Nightmare Eclipse GreatXML (finding-2026-06-11-0012)
    are graded separately.
  attribution_claims_summary: see_attribution_claims_field_above
  related_findings:
    - finding-2026-06-10-0017   # Krebs primary on Yapaev OSINT identification; THIS finding materially extends with PRODAFT + Microsoft independent attribution corroboration + new operator designations + technical detail + 478 victim count + geographic distribution + prior RaaS affiliate history
  relationship_to_existing_findings: >
    MATERIAL EXTENSION on finding-2026-06-10-0017. 0017 anchored on
    Krebs OSINT-de-anonymization chain (Hastalamuerte / Zeta88 →
    Alexander Yapaev) with Check Point + Intel 471 + Flashpoint
    cluster-coverage corroborators. This finding adds PRODAFT
    (independent vendor) AND Microsoft (Storm-2697 MSTIC tracking)
    as DISTINCT vendor-tier attribution sources NOT cited in 0017
    PLUS new operator designations (LARVA-368, Phantom Mantis,
    ArmCorp) + transition timeline (July 2025) + prior RaaS
    affiliate history (LockBit Tenacious Mantis + Qilin Pestilent
    Mantis + Medusa Venomous Mantis) + technical detail (Go/Garble,
    X25519/XChaCha20, multi-platform, --spread worm flag, 2-6 week
    dwell) + 478 victim count + geographic distribution (~13%
    U.S.-based; majority Thailand/UK/Brazil/Germany/India).

# ============================================================================
# Inclusion + handoffs
# ============================================================================
analyst_review_required: true
analyst_review_rationale: >
  Attribution corroboration on Yapaev identity + LockBit roster
  dossier touchpoint per Hard Rule 2 binding warrant SAT-class
  consideration on:
  (a) /NEW-ACTOR DECISION CARRY-FORWARD for The Gentlemen —
      operator decision continues to defer per
      finding-2026-06-10-0017. PM-cycle adds PRODAFT + Microsoft
      independent corroboration which materially strengthens the
      identification confidence (lifts identity layer to
      "very_likely"). Recommend actor-profiler scaffolding
      research if operator approves /new-actor.
  (b) LOCKBIT ROSTER #015 DOSSIER MAINTENANCE — next-review-due
      2026-07-10 per finding-2026-06-10-0017. PM-cycle PRODAFT
      identifies Yapaev as FORMER LockBit affiliate (Tenacious
      Mantis) who transitioned to independent operator July 2025.
      Hard Rule 2 binding: do NOT extend LockBit dossier to
      cover Yapaev's current Gentlemen operations. The historical
      affiliate-lineage is material for LockBit dossier
      maintenance context but NOT for Gentlemen attribution.
      Verify actor-profiler discipline at next-review.
  (c) DEFENDER PIVOT — `--spread` argument flag is operational
      defender pivot at endpoint command-line audit layer.
      Conservative B2 single-source veto on the specific flag;
      monitoring-tier inclusion warranted.

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling "likely" on substantive operational claims (single-
  source veto holds on PRODAFT-specific layers). Does NOT meet
  red-team invocation floor of "very_likely+" on operational
  impact claims. WEP "very_likely" on Yapaev identity layer
  (three-vendor convergence) does not warrant red-team invocation
  per established convention (identity-corroboration class is
  attribution-chain not operational-impact class).

red_team_review: null

analysis_sections:
  # /new-actor decision carry-forward for The Gentlemen
  new_actor_decision_support:
    candidate_actor_name: "The Gentlemen"
    candidate_actor_aliases_per_in_window_source:
      - LARVA-368   # PRODAFT operator designation
      - Phantom Mantis   # PRODAFT group tracking
      - Storm-2697   # Microsoft MSTIC group tracking
      - ArmCorp   # PRODAFT prior operator alias
    candidate_actor_aliases_carry_forward_from_0017:
      - Hastalamuerte
      - Zeta88
    candidate_actor_operator_real_identity_per_three_vendor_convergence:
      name: Alexander Andreevich Yapaev
      age: 36
      location: Izhevsk, Russia
    archimedes_roster_status: not_in_roster_v2_as_of_2026_05_10
    evidence_basis_enumeration:
      a_grade_originator_layer:
        - microsoft_mstic_storm_2697_designation_at_originator_a_relay_b_through_thn
      a_grade_in_window: []
      b_grade_in_window:
        - thn_relay_of_prodaft_phantom_mantis_larva_368_yapaev_attribution_b2
        - thn_relay_of_microsoft_storm_2697_designation_b2
        - thn_relay_of_prodaft_478_victim_count_b2
        - thn_relay_of_prodaft_technical_detail_go_garble_x25519_xchacha20_spread_worm_2_6_week_dwell_b2
        - thn_relay_of_prodaft_geographic_distribution_13_pct_us_majority_thailand_uk_brazil_germany_india_b2
        - thn_relay_of_prodaft_prior_raas_affiliate_history_lockbit_qilin_medusa_b2
      b_grade_carry_forward_from_0017:
        - krebs_osint_de_anonymization_chain_b2
        - check_point_intel_471_flashpoint_cluster_coverage_b2
      verifiable_absence_a1:
        - no_ad_prime_named_as_victim
        - no_defense_sector_targeting_per_source
        - prodaft_primary_not_directly_retrieved
        - microsoft_msrc_or_security_blog_publication_naming_storm_2697_not_in_window_attested
    ach_assessment_against_actor_profile_standard_minimums:
      attribution_clarity:
        verdict: strong
        rationale: >
          Three-vendor convergence (Krebs + PRODAFT + Microsoft) on Yapaev identity
          via publisher-independent and evidence-independent paths satisfies
          ACTOR-PROFILE-STANDARD attribution requirements at strong tier. The
          operator-real-identity layer is supported by a level of corroboration
          rare for unaligned cybercriminal actors. Nation/service framing
          (Russia / no state service; independent operator) is sourced and
          coherent.
      us_prime_exposure:
        verdict: weak
        rationale: >
          ~13% U.S.-based victim distribution per PRODAFT scanning; no A&D-prime
          named as victim; no defense-sector targeting per source. ACTOR-PROFILE-
          STANDARD section 2 'Primary Targets' would have to acknowledge a
          predominantly non-U.S. focus (Thailand / UK / Brazil / Germany / India)
          with U.S. as minority exposure. Defender utility for the A&D-prime
          target profile is moderate at best — the actor exists, is well-
          characterized, but does not currently appear to prioritize A&D primes.
      tooling_tradecraft_documentation_availability:
        verdict: strong_at_relay_tier_pending_prodaft_primary_retrieval
        rationale: >
          ACTOR-PROFILE-STANDARD sections 4 'TTPs' (Initial Access not
          characterized in-window; Execution/Persistence/Lateral Movement via
          `--spread` worm flag), 5 'Malware Arsenal' (Go binary with Garble
          obfuscation; X25519+XChaCha20 encryption), 6 'Infrastructure Patterns'
          (not characterized in-window), 7 'Known IOCs' (no hashes / domains /
          IPs at B-grade relay tier) would be partially populatable from in-
          window material. PRODAFT primary retrieval would likely fill hash and
          infrastructure IOC gaps; without it, the dossier sections 6 and 7
          would be sparse. Sections 4 and 5 are minimally populatable now.
      raas_lineage_documentation_availability:
        verdict: material_for_lockbit_dossier_maintenance_not_for_gentlemen_dossier
        rationale: >
          PRODAFT's lineage tracking (Yapaev as Tenacious Mantis / Pestilent
          Mantis / Venomous Mantis across LockBit / Qilin / Medusa) is rich
          historical context but per Hard Rule 2 binding does NOT extend the
          LockBit dossier (roster #015) to cover Yapaev's INDEPENDENT current
          Gentlemen operations. The lineage layer is material for LockBit
          dossier 'Connection Web' section context at next-review (due
          2026-07-10) but NOT for current attribution.
    analyst_recommendation:
      recommendation: approve_candidacy_pending_operator_decision
      rationale: >
        The Gentlemen meets a stronger evidence threshold than Void Blizzard
        for /new-actor candidacy:
          (a) Attribution clarity is strong — three-vendor convergence on
              operator real identity is rare and well-corroborated;
          (b) Tooling/tradecraft is partially documented at B-tier relay with
              defender-actionable elements (`--spread` worm flag, Go/Garble
              binary, multi-platform targeting);
          (c) Microsoft MSTIC tracking ID (Storm-2697) signals MSTIC has been
              monitoring this operator — additional MSTIC publication retrieval
              would lift the dossier substantially.
        BUT the A&D-prime relevance is weak (~13% U.S.-based, no DIB direct
        exposure, no defense-sector targeting). The dossier would document a
        well-characterized actor that does not currently prioritize the
        Archimedes target profile.
        Recommend: SURFACE candidacy to operator with the structured tradeoff
        narrative — strong attribution + tradecraft documentation, but weak
        A&D-prime relevance. Operator-decision factors: (i) does Archimedes
        track well-characterized actors regardless of A&D-prime exposure?
        (ii) is the prior-LockBit-affiliate lineage sufficient to warrant
        tracking via #015 connection-web rather than independent dossier?
        (iii) does the `--spread` worm flag's defender-pivot relevance to
        broader DIB infrastructure (RaaS lineage, multi-platform targeting)
        justify dedicated tracking?
        Analyst's secondary recommendation: if operator declines /new-actor,
        document the Yapaev / Gentlemen / LARVA-368 / Phantom Mantis /
        Storm-2697 cluster in LockBit #015's 'Connection Web' section
        narrative AT NEXT REVIEW with explicit "FORMER affiliate, INDEPENDENT
        post-July-2025" framing per Hard Rule 2.
      hard_rule_2_compliance: pass
      hard_rule_2_compliance_detail: >
        Analyst recommendation is APPROVE-CANDIDACY-PENDING-OPERATOR-DECISION,
        framed as recommendation only. Analyst does NOT originate attribution.
        Three-vendor convergence (Krebs + PRODAFT + Microsoft) on Yapaev
        identity is preserved as vendor-attested with citation. PRODAFT-
        specific operator designations + transition timeline + technical
        detail preserved as source-attested. LockBit roster #015 dossier
        extension to cover Yapaev's INDEPENDENT current Gentlemen operations
        is PROHIBITED per Hard Rule 2. Historical affiliate-lineage is
        material for LockBit dossier 'Connection Web' context only.

  sat_ach:
    ach_analysis:
      question: "Does the PRODAFT + Microsoft (Storm-2697) PM-cycle corroboration of Krebs' OSINT-de-anonymization chain meet the threshold for /new-actor dossier creation per ACTOR-PROFILE-STANDARD?"
      analyzed_at: 2026-06-11T17:55:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: "Sufficient evidence to scaffold an actor profile that materially serves the Archimedes A&D-prime target profile — three-vendor identity convergence + defender-actionable TTP detail (`--spread` worm flag) + RaaS lineage + ongoing operational tempo (478 victims) warrants dossier creation."
        - id: H2
          statement: "Sufficient evidence for an actor profile but A&D-prime relevance is too weak to warrant dedicated tracking — the dossier would be well-characterized but operationally low-priority. Better fit as connection-web context in LockBit #015's dossier, not as standalone."
        - id: H3
          statement: "Insufficient evidence — PRODAFT primary not directly retrieved; many key claims rest on single-vendor through single-publisher relay; the profile would be skeletal in critical sections (Infrastructure Patterns, Known IOCs) until primary retrieval. Defer pending primary."
        - id: H4
          statement: "Hard Rule 2 binding precludes the /new-actor decision being made on current evidence alone — the underlying identity claim rests on OSINT-via-breadcrumb-chain (0017's Krebs) plus PRODAFT relay; without direct PRODAFT publication retrieval or Microsoft MSRC/security blog publication attesting Storm-2697 at A, the dossier creation would imply higher-confidence attribution than evidence supports."
      evidence:
        - id: E1
          description: "Three-vendor convergence on Yapaev identity (Krebs + PRODAFT + Microsoft Storm-2697) via publisher-independent and evidence-independent paths"
          source: three_vendor_corroboration_per_aggregate_finding_0017_plus_0009_cluster
          digraph: B2
          weight: 2
        - id: E2
          description: "478 victim count per PRODAFT through THN relay (lifts above 0017's Check Point '240+ in 2026' framing)"
          source: prodaft_via_thn
          digraph: B2
          weight: 2
        - id: E3
          description: "Defender-actionable technical detail: `--spread` argument flag converts single-host encryptor into self-propagating worm; Go binary with Garble obfuscation; X25519+XChaCha20 encryption; Windows/Linux/ESXi/LVM multi-platform targeting; 2-6 week dwell time"
          source: prodaft_via_thn
          digraph: B2
          weight: 2
        - id: E4
          description: "Geographic distribution — ~13% U.S.-based; majority Thailand / UK / Brazil / Germany / India"
          source: prodaft_via_thn
          digraph: B2
          weight: 2
        - id: E5
          description: "Verifiable absence — no A&D-prime named as victim; no defense-sector targeting per source"
          source: verifiable_absence_at_sweep
          digraph: A1
          weight: 3
        - id: E6
          description: "Verifiable absence — PRODAFT primary not directly retrieved; THN relay only"
          source: verifiable_absence_at_sweep
          digraph: A1
          weight: 3
        - id: E7
          description: "Microsoft MSTIC Storm-2697 designation — MSTIC-canonical at originator layer (A); relay-tier B through THN; no second-vendor corroboration of Storm-2697 designation as such"
          source: microsoft_via_thn
          digraph: B2
          weight: 2
        - id: E8
          description: "Prior RaaS affiliate history per PRODAFT: LockBit (as Tenacious Mantis), Qilin (Pestilent Mantis), Medusa (Venomous Mantis); transition to independent operator July 2025. LockBit is in roster #015"
          source: prodaft_via_thn
          digraph: B2
          weight: 2
      matrix:
        E1: {H1: C, H2: C, H3: I, H4: I}   # Strong identity convergence cuts against insufficient-evidence H3 and against high-confidence-attribution-not-supported H4
        E2: {H1: C, H2: N, H3: N, H4: N}   # 478 victim count supports tracking but doesn't speak to A&D-prime relevance
        E3: {H1: C, H2: C, H3: N, H4: N}   # Defender-actionable detail supports H1 (warrants tracking) and H2 (well-characterized) equally
        E4: {H1: I, H2: C, H3: N, H4: N}   # ~13% U.S.-based directly cuts against H1 (A&D-prime-target-profile-serving) and supports H2
        E5: {H1: I, H2: C, H3: N, H4: C}   # Absence of A&D-prime victim cuts against H1; supports H2 (operationally low-priority for AD target) and H4 (attribution caveat)
        E6: {H1: N, H2: N, H3: C, H4: C}   # Primary not retrieved supports H3 (skeletal) and H4 (caveat)
        E7: {H1: C, H2: N, H3: N, H4: C}   # Microsoft MSTIC tracking supports H1 (warrants tracking) but designation not corroborated at originator — partial H4 caveat
        E8: {H1: C, H2: C, H3: N, H4: N}   # RaaS lineage supports H1 and H2 (rich context); doesn't address H3 or H4
      inconsistency_counts:
        H1: 2   # E4 ~13% U.S., E5 no A&D victim
        H2: 0
        H3: 1   # E1 strong identity convergence
        H4: 1   # E1 strong identity convergence
      diagnostic_evidence:
        - E1: "Three-vendor identity convergence is diagnostic for H1/H2 vs. H3/H4 — distinguishes sufficient-evidence from insufficient-evidence framings"
        - E4: "~13% U.S.-based is diagnostic for H1 vs. H2 — distinguishes 'serves A&D-prime profile' from 'well-characterized but low-priority'"
        - E5: "Absence of A&D-prime victim reinforces E4 diagnosticity"
      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: "Zero inconsistencies. The evidence supports actor profile creation in concept but the A&D-prime relevance is too weak to warrant dedicated tracking. Better operational fit as connection-web context in LockBit #015's dossier rather than standalone."
          wep: likely
        - rank: 2
          hypothesis_id: H1
          rationale: "Two inconsistencies (E4 geographic distribution, E5 verifiable absence of A&D victim). H1 cannot be ruled out — Archimedes may track well-characterized actors regardless of A&D-prime exposure — but the evidence does not affirmatively support 'materially serves the A&D-prime target profile.'"
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H3
          rationale: "One inconsistency (E1 strong identity convergence). Identity layer is well-corroborated despite PRODAFT primary not retrieved; H3 over-corrects against the available evidence. But H3 is right that specific dossier sections (Infrastructure Patterns, Known IOCs) would be sparse."
          wep: unlikely
        - rank: 4
          hypothesis_id: H4
          rationale: "One inconsistency (E1). Hard Rule 2 binding concern is real but the three-vendor convergence on identity is itself the kind of vendor-attestation Archimedes is permitted to track. H4 over-corrects."
          wep: unlikely
      sensitivity_analysis:
        brittleness: low_to_medium
        load_bearing_evidence: [E1, E4, E5]
        if_E4_geographic_data_proves_wrong_or_skewed: "If U.S. exposure is materially higher than 13%, H1 lifts and could overtake H2"
        if_A_and_D_prime_named_victim_surfaces_in_next_30d: "H1 lifts substantially; H2 weakens; recommend immediate /new-actor approval"
        if_prodaft_primary_retrieved_with_richer_a_and_d_context: "Re-rank possible; H1/H2 distinction sharpens"
        if_microsoft_publishes_msrc_or_security_blog_on_storm_2697: "Lifts E7 to A; H1 strengthens via MSTIC-attributed defender content"
      tripwires:
        - observation: "A&D-prime or DIB-supplier-class organization named as Gentlemen / Phantom Mantis / Storm-2697 victim"
          effect: "H1 lifts to likely; recommend immediate /new-actor approval"
        - observation: "PRODAFT publishes their primary research directly accessible to Archimedes collector"
          effect: "Lift PRODAFT-specific layers from B2 to A2; rerun decision support"
        - observation: "Microsoft publishes MSRC or Security Response blog naming Storm-2697 at A"
          effect: "Lift E7 to A; strengthens H1; consider /new-actor approval"
        - observation: "Yapaev arrested, sanctioned, or operationally disrupted"
          effect: "H1 may weaken (dormant actor); /new-actor decision can be deferred indefinitely"
        - observation: "Geographic distribution updates show U.S. exposure climbing above 25%"
          effect: "E4 weakens; H1 strengthens; lift to roughly_even_chance or likely"
      conclusion:
        summary: |
          The leading hypothesis is H2 (sufficient evidence to scaffold a profile,
          but A&D-prime relevance too weak to warrant dedicated tracking; better fit
          as LockBit #015 connection-web context) at "likely." H1 (warrants dedicated
          tracking for A&D defender utility) is "roughly even chance" — two
          inconsistencies via geographic distribution and absence of A&D-prime
          victim. H3 (insufficient evidence) and H4 (Hard Rule 2 caveat) are both
          "unlikely" — the three-vendor identity convergence is genuinely strong.
          Practical recommendation: SURFACE the candidacy to operator with the
          structured tradeoff narrative. The decision rests on Archimedes policy
          (does it track well-characterized actors regardless of A&D-prime
          relevance?), not on evidence sufficiency.
        wep: likely
        confidence_caveats: |
          Assessment is low-to-medium brittle. The single biggest pivot is E5 — if
          an A&D-prime named victim surfaces in next 30d, H1 lifts substantially
          and recommendation changes to immediate approval. Until then, the
          conservative read holds. Identity layer (three-vendor convergence)
          remains very_likely regardless of this analysis.

  # LockBit roster #015 dossier-maintenance discipline verification (per grader-specified scope)
  lockbit_roster_015_dossier_maintenance_discipline_check:
    hard_rule_2_binding_check: pass
    detail: >
      Finding explicitly preserves the Hard Rule 2 binding: LockBit roster #015
      dossier is NOT extended to cover Yapaev's current INDEPENDENT Gentlemen
      operations. Yapaev is FORMER affiliate (per PRODAFT framing — Tenacious
      Mantis lineage); transitioned to independent operator July 2025. Current
      Gentlemen operations are NOT LockBit operations and are NOT propagated
      to LockBit #015 dossier. Finding correctly flags the lineage as material
      for LockBit dossier 'Connection Web' context at next-review (due
      2026-07-10) only — NOT as current LockBit attribution.
    actor_profiler_handoff_guidance: >
      At LockBit #015 next-review (2026-07-10), actor-profiler should:
      (a) Add a 'Connection Web' section note: "Per PRODAFT 2026-06-11 vendor
          research relayed via The Hacker News, Alexander Yapaev (Izhevsk,
          Russia) operated within the LockBit affiliate program as 'Tenacious
          Mantis' prior to transitioning to independent operations (now
          tracked by PRODAFT as Phantom Mantis / LARVA-368 and by Microsoft
          MSTIC as Storm-2697) in July 2025. The Gentlemen ransomware
          operations post-July-2025 are NOT LockBit operations."
      (b) Do NOT extend LockBit TTPs, Malware Arsenal, Infrastructure Patterns,
          or IOC sections to include Phantom Mantis / Storm-2697 specific
          content per Hard Rule 2;
      (c) Cross-reference the Gentlemen /new-actor decision outcome (whether
          standalone dossier or LockBit-connection-web-context-only) into
          this note.

  # Defender pivot — --spread worm flag
  defender_pivot_spread_worm_flag:
    finding_classification: defender_actionable_endpoint_command_line_audit
    detail: >
      PRODAFT vendor research (via THN relay) documents that The Gentlemen
      ransomware binary accepts a `--spread` argument flag that converts a
      single-host encryptor into self-propagating worm-like behavior across
      Windows / Linux / ESXi / LVM multi-platform targets. This is an
      operationally significant defender pivot for any network defender
      monitoring endpoint command-line telemetry.
    defender_implications:
      - "Hosts observed executing a Go binary with `--spread` argument flag should be treated as LATERAL-MOVEMENT AMPLIFIERS — they are not just compromised endpoints; they are actively spreading the encryptor to additional reachable hosts."
      - "EDR / endpoint command-line audit (Sysmon Event ID 1, Defender for Endpoint process telemetry, CrowdStrike Falcon process data) should add a detection on argv pattern matching `--spread` on Go binary execution where parent process or binary path looks suspicious."
      - "Network segmentation discipline is the controlling mitigation — if `--spread` activated host can reach 100 additional hosts via SMB / SSH / hypervisor APIs / LVM, the blast radius is 100; if segmentation contains reach to 5, blast radius is 5."
      - "Hypervisor / ESXi management plane should be specifically audited — Gentlemen's ESXi/LVM targeting indicates operator capability to encrypt at hypervisor layer, which has multiplicative impact (one ESXi compromise = many VM compromises)."
      - "2-6 week dwell time per PRODAFT operational characterization means `--spread` may be activated late in the dwell window after extensive lateral movement preparation; early-detection of pre-encryption-stage indicators is the high-leverage window."
    confidence_caveats:
      - "PRODAFT primary not directly retrieved; specific argv pattern and binary fingerprint should be re-verified against PRODAFT primary publication if available."
      - "Single-source veto applies on the specific flag designation; detection rules should be tuned conservatively (high specificity, accept lower recall) to avoid false-positive noise on legitimate `--spread` flag usage in benign tooling."
      - "PRODAFT publication likely contains hash + infrastructure IOCs not surfaced at THN relay tier; collector handoff for PRODAFT primary retrieval would substantially strengthen defender deployment."

  sat_kac: null  # KAC not invoked for this finding — WEP caps at "likely" on substantive operational claims; identity layer at "very_likely" via three-vendor convergence is well-characterized and doesn't rest on hidden assumptions per SAT-KAC invocation criteria. SAT-ACH on /new-actor decision support + LockBit dossier-maintenance discipline + defender pivot satisfy grader-specified scope.

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
  - source_yaml_id: prodaft-research
    proposed_action: add_new_provisional_source_entry
    proposed_grade: B
    proposed_provisional_until: 2026-06-14T17:05:00-04:00
    rationale: "PRODAFT is established threat-intelligence research provider with sustained operator-de-anonymization track record (peer class to Mandiant / CrowdStrike / Intel 471 / Flashpoint / Check Point). First Archimedes-corpus dedicated source ID via this finding. Conservative provisional B starting grade pending direct primary retrieval. Librarian handoff for source-grades.yaml addition + source-grade-log entry. 72h ratification clock."
---

# The Gentlemen Ransomware — PRODAFT + Microsoft independent attribution corroboration of Krebs Yapaev identification (material extension on finding-2026-06-10-0017)

## Summary

PRODAFT (tracks as Phantom Mantis; operator-designates LARVA-368) and Microsoft (tracks as Storm-2697) independently corroborate the finding-2026-06-10-0017 Krebs OSINT-de-anonymization chain identifying The Gentlemen ransomware operator as Alexander Andreevich Yapaev, 36, Izhevsk, Russia. The PM-cycle three-vendor convergence (Krebs + PRODAFT + Microsoft) lifts the identity layer from 0017's B3 OSINT-via-breadcrumb anchor to B2 / "very_likely" via publisher-independent and evidence-independent paths. PRODAFT adds material new content: prior alias ArmCorp; transition from RaaS affiliate to independent operator July 2025; prior RaaS affiliate history with LockBit (as Tenacious Mantis), Qilin (Pestilent Mantis), Medusa (Venomous Mantis); technical detail (Go binary + Garble obfuscation; X25519 key exchange + XChaCha20 encryption; Windows/Linux/ESXi/LVM targeting; `--spread` argument-flag worm capability; 2-6 week dwell time); 478 victim count claim lifting above 0017's Check Point "240+ in 2026" framing; geographic distribution (~13% U.S.-based; majority Thailand/UK/Brazil/Germany/India). No A&D-prime named victim. LockBit roster #015 dossier touchpoint per Hard Rule 2 binding: Yapaev is FORMER LockBit affiliate now INDEPENDENT operator; current Gentlemen operations are NOT LockBit operations.

## Sources

### The Hacker News (thehackernews, B provisional) — sole in-window publisher

- URL: https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html
- Published: 2026-06-11 16:50 EDT
- Key claim: Relays PRODAFT (Phantom Mantis / LARVA-368) + Microsoft (Storm-2697) on Gentlemen ransomware operator Alexander Yapaev (Izhevsk, Russia); 478 victim count; prior LockBit/Qilin/Medusa RaaS affiliate history; transition to independent operator July 2025; Go binary + Garble + X25519/XChaCha20; multi-platform targeting; `--spread` worm flag; geographic distribution.

### PRODAFT (prodaft-research, B provisional) — originating vendor, NOT directly retrieved

- Status: primary not directly retrieved this sweep; substantive content relayed via THN
- Role: originating vendor research on Phantom Mantis / LARVA-368 / Yapaev attribution + operator-history reconstruction + technical detail + 478 victim count + geographic distribution
- Librarian handoff: add to source-grades.yaml as provisional B; 72h ratification clock to 2026-06-14T17:05:00-04:00

### Microsoft (mstic, A) — Storm-2697 tracking ID corroborator

- Status: Storm-2697 tracking ID at MSTIC ratified A originator layer; relay-tier B through THN
- Role: independent vendor tracking ID corroboration of Yapaev identity layer

### Krebs (krebs, B) — carry-forward from finding-2026-06-10-0017

- Role: canonical originating-publisher on Yapaev OSINT-de-anonymization chain (Hastalamuerte / Zeta88 breadcrumb → Yapaev identification)
- Status: finding-2026-06-10-0017 source-of-truth

## Technical detail — material extension on 0017

This finding is a MATERIAL EXTENSION on `finding-2026-06-10-0017`. NEW corpus material:

1. **Independent attribution corroboration on Yapaev identity:** PRODAFT (independent vendor) + Microsoft (Storm-2697 MSTIC tracking ID at originator layer A) corroborate 0017's Krebs OSINT-de-anonymization chain. Three-vendor convergence lifts identity layer to B2 / "very_likely" via publisher-independent and evidence-independent paths.

2. **Operator designations (NEW to corpus):**
   - **PRODAFT:** Phantom Mantis (group tracking ID), LARVA-368 (operator designation), ArmCorp (prior alias)
   - **Microsoft:** Storm-2697 (group tracking ID)
   - Prior aliases carry-forward from 0017: Hastalamuerte, Zeta88

3. **Operator transition timeline (NEW):** Per PRODAFT, Yapaev transitioned from RaaS affiliate to independent operator July 2025.

4. **Prior RaaS affiliate history (NEW):**
   - LockBit as **Tenacious Mantis** (LockBit IS in roster #015, HIGH; per Hard Rule 2 do NOT extend LockBit dossier to cover Gentlemen)
   - Qilin as **Pestilent Mantis** (Qilin NOT in roster)
   - Medusa as **Venomous Mantis** (Medusa NOT in roster)

5. **Technical detail (NEW):**
   - Go binary with Garble obfuscation
   - X25519 key exchange + XChaCha20 encryption
   - Windows / Linux / ESXi / LVM multi-platform targeting
   - **`--spread` argument flag** converts single-host encryptor into self-propagating worm — operational defender pivot at endpoint command-line audit layer
   - 2-6 week dwell time

6. **Victim count (NEW):** 478 victims claimed per PRODAFT through THN relay; lifts above 0017's Check Point "240+ in 2026" framing.

7. **Geographic distribution (NEW):** ~13% U.S.-based; majority Thailand / UK / Brazil / Germany / India.

## Roster crosswalk — Hard Rule 2 binding

- **LockBit IS in roster** (`_roster.yaml` id #015, threat_level HIGH; tracked from Session 1 C3PO migration).
- **Yapaev's prior LockBit affiliation** (per PRODAFT: Tenacious Mantis) is material for LockBit dossier maintenance context but does NOT extend the LockBit dossier to cover Gentlemen operations. Yapaev is a FORMER affiliate who transitioned to independent operator July 2025; current Gentlemen operations are NOT LockBit operations.
- **Qilin and Medusa NOT in roster.** Operator decision required on /new-actor candidacy for either group separately. Material is `/new-actor` candidacy awareness; same operator-decision-pending status as 0017.
- **The Gentlemen /new-actor candidacy** carries forward unchanged from 0017. PM-cycle three-vendor convergence on identity layer materially strengthens identification confidence.

## A&D / DIB relevance

- **No A&D-prime named as victim:** verifiable absence.
- **No defense-sector targeting per source:** verifiable absence.
- **A&D relevance watchlist-signal only:** geographic distribution (~13% U.S.-based with majority Thailand / UK / Brazil / Germany / India) reduces DIB-direct exposure narrative further than 0017's broader-victim-base framing.

## Why this is NOT anti-noise restatement vs. finding-2026-06-10-0017

- 0017 was Krebs primary OSINT-de-anonymization chain with Check Point + Intel 471 + Flashpoint cluster-coverage corroborators.
- This finding adds PRODAFT AND Microsoft as DISTINCT vendor-tier attribution sources NOT cited in 0017.
- LARVA-368 / Phantom Mantis / Storm-2697 / ArmCorp designations are NEW to corpus.
- Technical detail (Go/Garble, X25519/XChaCha20, `--spread` worm flag) is NEW to corpus.
- Geographic distribution and 478 victim count are NEW to corpus.
- Prior RaaS affiliate history (LockBit Tenacious Mantis / Qilin Pestilent Mantis / Medusa Venomous Mantis) is NEW to corpus.

Conclusion: MATERIAL EXTENSION, not anti-noise restatement. Promote.

## IOCs surfaced

- **Actor:** The Gentlemen (PRODAFT: Phantom Mantis / LARVA-368; Microsoft: Storm-2697; ArmCorp prior alias; Hastalamuerte / Zeta88 prior aliases per 0017)
- **Operator real identity:** Alexander Andreevich Yapaev, 36, Izhevsk, Russia (three-vendor convergence)
- **Technical:** Go binary + Garble obfuscation; X25519 key exchange + XChaCha20 encryption; Windows/Linux/ESXi/LVM multi-platform targeting; `--spread` argument flag (worm capability — defender pivot at endpoint command-line audit layer); 2-6 week dwell time
- **No hash, domain, or IP IOCs** in B-grade relay tier. PRODAFT primary likely carries hash + infrastructure IOCs but was NOT directly retrieved this sweep.

## Relationship to existing findings

- **finding-2026-06-10-0017** — Krebs primary OSINT-de-anonymization chain on Yapaev identification. This finding MATERIALLY EXTENDS with PRODAFT + Microsoft independent attribution corroboration + new operator designations + technical detail + 478 victim count + geographic distribution + prior RaaS affiliate history. 0017 remains canonical source-of-truth for the Krebs OSINT-de-anonymization chain itself.

## Open questions for analyst

1. **`/new-actor` decision carry-forward for The Gentlemen:** PM-cycle three-vendor convergence strengthens identification confidence to "very_likely" on identity layer. Operator decision continues to defer per 0017; recommend actor-profiler scaffolding research if operator approves.
2. **LockBit roster #015 dossier maintenance discipline (SAT-class):** Verify Hard Rule 2 binding at next-review (due 2026-07-10) — do NOT extend LockBit dossier to cover Yapaev's current INDEPENDENT Gentlemen operations. Historical affiliate-lineage is material for LockBit dossier context only.
3. **Defender pivot watch:** `--spread` argument flag in PRODAFT vendor research is operational defender pivot at endpoint command-line audit layer. Conservative B2 single-source veto on the specific flag; monitoring-tier inclusion warranted.

## Analytic notes (from analyst review)

SAT-ACH on /new-actor decision support ranks H2 (sufficient evidence to scaffold a profile, but A&D-prime relevance too weak to warrant dedicated tracking; better fit as LockBit #015 connection-web context) at "likely" with zero inconsistencies. H1 (warrants dedicated tracking for A&D defender utility) is "roughly even chance" — two inconsistencies via geographic distribution (~13% U.S.-based) and absence of A&D-prime victim. The three-vendor identity convergence (Krebs + PRODAFT + Microsoft Storm-2697) is genuinely strong evidence and cuts against H3 (insufficient) and H4 (Hard Rule 2 caveat). Recommendation: SURFACE candidacy to operator with structured tradeoff narrative. The decision rests on Archimedes policy (does it track well-characterized actors regardless of A&D-prime relevance?), not on evidence sufficiency.

LockBit #015 dossier-maintenance discipline is preserved: Yapaev's prior-LockBit affiliation (as Tenacious Mantis) is material for LockBit dossier 'Connection Web' context at next-review (2026-07-10) ONLY, NOT for current LockBit attribution. Finding correctly flags this. Hard Rule 2 binding is intact — no Gentlemen TTPs / malware / IOCs propagated to LockBit dossier sections.

Defender pivot — the `--spread` argument flag is operationally significant: hosts executing a Go binary with this flag should be treated as lateral-movement amplifiers, not just compromised endpoints. Network defenders should add endpoint command-line audit detections on argv pattern matching `--spread` on Go-binary execution; segmentation discipline is the controlling mitigation; ESXi/LVM management plane warrants specific audit given Gentlemen's hypervisor-layer targeting. 2-6 week dwell time means early-detection of pre-encryption-stage indicators is the high-leverage window.
