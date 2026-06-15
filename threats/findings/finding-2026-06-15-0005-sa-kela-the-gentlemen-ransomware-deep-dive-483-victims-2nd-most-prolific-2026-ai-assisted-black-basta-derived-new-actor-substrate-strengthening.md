---
id: finding-2026-06-15-0005
finding_id: finding-2026-06-15-0005-sa-kela-the-gentlemen-ransomware-deep-dive-483-victims-2nd-most-prolific-2026-ai-assisted-black-basta-derived-new-actor-substrate-strengthening
title: "Security Affairs (Paganini) relays KELA RansomNews 2026-06-13 deep-dive on 'The Gentlemen' ransomware operation — surfaced 2025-09 with 483 victims on Tor leak site by 2026-06-13 (380 in 2026 alone; 2nd-most-prolific 2026 brand by leak-site count behind only Qilin); atypically 15% US victims (vs typical 40-50%); top countries Thailand / Brazil / UK / France / India / Germany / Italy / Japan / Taiwan / Spain; top sectors Manufacturing then Technology / Business Services / Healthcare (44 victims); 9 core members + 90/10 affiliate revenue split; named admin handle `zeta88`; multi-vector initial-access (FortiOS CVE-2024-55591 + ZeroLogon + PetitPotam + valid OWA credentials + infostealer commodity markets as primary vector); alerts.bar IOC cross-validation example (2GO Philippine logistics: 6 employee + 7 customer logins + 38 active session tokens pre-victim); AI-assisted ops with stripped-down 'uncensored' Qwen variant for coding + stolen-data analysis; February 2025 Black Basta chat-leak studied as training manual (DERIVATIVE tradecraft pattern, NOT actor-cluster overlap); Microsoft separately attributes Go-based self-propagating encryptor; NOT on 24-actor roster — operator-deferred /new-actor candidate substrate strengthening; NO US A&D-prime direct victim named (Manufacturing top-sector + Tier 1-3 country targeting may include defense-supplier-ecosystem entities but unnamed)"
date: 2026-06-15
created_at: 2026-06-15T08:32:00-04:00
graded_by: grader
grading_run_id: morning-20260615-080000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading
# ============================================================================
digraph: B2
digraph_layered:
  kela_ransomnews_primary_research_2026_06_13_deep_dive_on_the_gentlemen: A2  # KELA is established CTI research firm with leak-site monitoring track record; primary-research-grade
  the_gentlemen_surfaced_2025_09_with_483_victims_by_2026_06_13_380_in_2026_alone: B2  # KELA primary + SA relay; victim count is leak-site observation, externally verifiable in principle
  2nd_most_prolific_2026_ransomware_brand_by_leak_site_count_behind_qilin_only: B2  # KELA primary; ranking-claim is leak-site-count rollup
  atypically_15_percent_us_victims_vs_typical_40_50_percent: B2  # KELA observation; consistent with non-US-targeting framing
  top_countries_and_sectors_thailand_brazil_uk_france_india_etc_manufacturing_top: B2  # KELA primary observation
  9_core_members_plus_90_10_affiliate_revenue_split: B2  # KELA primary from chat-log leak May 2026
  named_admin_handle_zeta88_operational_handle_only_no_real_identity: B2  # KELA primary from chat leak; operational-handle attribution only
  multi_vector_initial_access_fortios_cve_2024_55591_zerologon_petitpotam_owa_creds_infostealer_primary: B2  # KELA primary; technically coherent with established 2025-2026 ransomware tradecraft
  alerts_bar_ioc_cross_validation_2go_philippine_logistics_pre_exposure_observation: B2  # KELA primary observation; methodologically defensible
  ai_assisted_ops_stripped_down_qwen_variant_for_coding_and_stolen_data_analysis: B2  # KELA primary from chat-log leak
  vibe_coded_negotiation_panel_in_three_days: C3  # KELA primary attribution to operator self-claim from leaked chats; not independently verified
  february_2025_black_basta_chat_leak_studied_as_training_manual: B2  # KELA primary observation; DERIVATIVE tradecraft pattern, NOT actor-cluster overlap with Black Basta
  microsoft_separately_documents_go_based_self_propagating_encryptor_attributed_to_the_gentlemen: B2  # KELA references Microsoft binding; Microsoft is A-tier primary but accessed here via KELA's reference, not directly retrieved
  willing_to_get_personal_extortion_pressure_via_sensitive_medical_content: C3  # KELA single observation
  the_gentlemen_NOT_on_24_actor_roster_yaml_operator_deferred_new_actor_decision: A1  # Verifiable absence per roster check
  no_us_ad_prime_direct_victim_named: A1  # Verifiable absence in source
  no_nation_state_attribution_kela_does_not_attribute_to_ru_cn_ir_kp_cluster: A1  # Verifiable absence — Hard Rule 2 binding preserved
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True / monitoring-tier).
  KELA RansomNews is established CTI research-firm primary
  with leak-site monitoring track record (A2 at primary
  layer); Security Affairs B-grade publisher relay provides
  in-window publication surface. Multi-publisher independence
  achieved at primary + publisher layer (KELA + SA).
  Microsoft attribution to Go-based encryptor is referenced
  in KELA primary but not directly retrieved this sweep —
  reduces Microsoft-binding to B2 reference-quality layer
  rather than A1 direct-retrieval.

  WHY B2 NOT B1: Cluster requires independent IR-firm or
  vendor parallel publication to lift to B1. KELA + SA + the
  KELA-referenced Microsoft attribution are not three
  independent evidence bases (Microsoft binding reaches
  Archimedes only through KELA's text). THN /
  BleepingComputer / Krebs / Sophos parallel coverage of
  the same KELA primary would lift to B1.

  WHY MONITORING-TIER INCLUSION NOT ACTION-TIER:
    1. NOT ON 24-ACTOR ROSTER. The Gentlemen has been
       substrate-active across multiple recent surfaces
       (2026-06-15 06:00 FLASH sentinel + this 07:30
       pre-brief deep-dive) but operator-deferred /new-actor
       decision has NOT been made. Hard Rule 5 binding:
       Archimedes does NOT auto-scaffold a /new-actor entry;
       only operator can invoke `/new-actor The Gentlemen`.
       This finding SURFACES the substrate, does NOT propose
       roster addition.
    2. NO US A&D-PRIME DIRECT VICTIM NAMED. Manufacturing
       top-sector + Tier 1-3 country prioritization MAY
       include defense-supplier-ecosystem entities at
       Tier-2/3 levels (smaller machining shops, electronics
       manufacturers servicing A&D primes) but unnamed in
       KELA / SA coverage. No specific A&D-prime victim
       enumerated.
    3. CVE-2024-55591 FORTIOS IS RE-USED 2024 VULN. KEV-
       listed but deadline well-past; not net-new FCEB-class
       urgency. Worth A&D-prime FortiOS deployment-state
       check but not action-tier substrate.
    4. AI-ASSISTED OPS SUBSTRATE IS REPORTABLE BUT NOT
       OPERATIONALLY ACTIONABLE for A&D-prime defenders this
       sweep — pattern-of-method awareness for sector-context
       framing.

  ADDITIONAL ACTOR-PROFILER SURFACING VALUE: The Gentlemen
  /new-actor candidacy substrate is now research-firm-grade
  (KELA RansomNews primary), multi-vector confirmed (FortiOS
  + ZeroLogon + PetitPotam + valid OWA creds + infostealer),
  distinctively named, with quantified victim scale (483
  victims, 2nd-most-prolific 2026), AI-assisted-ops detail,
  and Black Basta tradecraft-inheritance lineage. Recommend
  actor-profiler review window post-PeopleSoft-deadline-cycle
  (EOD Sunday 2026-06-15 + Monday morning brief 2026-06-16)
  for operator /new-actor scaffolding evaluation.

  WHAT THE B2 ATTESTS:
    (a) The Gentlemen surfaced as ransomware operation 2025-09
        with 483 victims on Tor leak site by 2026-06-13 (KELA
        observation).
    (b) 380 of 483 victims are 2026 — accelerating trajectory.
    (c) 2nd-most-prolific 2026 brand by leak-site count
        behind only Qilin (KELA ranking).
    (d) Atypically 15% US victims (vs typical 40-50% across
        other ransomware brands) — non-US-targeting framing.
    (e) Top countries: Thailand, Brazil, UK, France, India,
        Germany, Italy, Japan, Taiwan, Spain.
    (f) Sectoral: Manufacturing (top), Technology, Business
        Services, Healthcare (44 victims).
    (g) Structure: 9 core members + 90/10 affiliate split
        (per chat-log leak May 2026 spanning 2025-11 to
        2026-04).
    (h) Named admin handle `zeta88` (operational only; no
        real-identity surface).
    (i) Multi-vector initial access including FortiOS
        CVE-2024-55591 + ZeroLogon + PetitPotam + valid OWA
        credentials + infostealer commodity markets (primary
        vector).
    (j) alerts.bar IOC cross-validation methodology — KELA
        cross-references named Gentlemen victims against
        infostealer index (2GO Philippine logistics example:
        6 employee + 7 customer logins + 38 active session
        tokens exposed BEFORE 2GO appeared on Gentlemen leak
        site).
    (k) AI-assisted operations: stripped-down Qwen variant
        for coding + stolen-data analysis; "vibe-coded"
        negotiation panel in three days (KELA-attributed to
        zeta88 from leaked chats).
    (l) Feb 2025 Black Basta chat-leak studied as training
        manual — DERIVATIVE tradecraft pattern, NOT actor-
        cluster overlap.
    (m) Microsoft separately attributes Go-based self-
        propagating encryptor to The Gentlemen (KELA-
        referenced, not directly retrieved this sweep).

  WHAT THE B2 DOES NOT ATTEST:
    - That The Gentlemen and Black Basta are operator-overlap
      clusters (KELA framing: training-manual relationship,
      derivative tradecraft pattern, NOT cluster overlap).
    - Any nation-state attribution (KELA does NOT attribute
      to RU / CN / IR / KP).
    - That A&D-prime entities have been victimized by The
      Gentlemen (no A&D-prime enumeration in source).
    - That `zeta88` is a real-identity attribution surface
      (operational handle only).
    - That AI-assisted operations confer step-function
      capability uplift (KELA describes operational use of
      open-weight models; speed-of-development-and-data-
      analysis improvement, not categorical capability
      leap).

  HARD RULE 2 binding constraint: PRESERVED.
    - The Gentlemen + Black Basta framed as DERIVATIVE-
      tradecraft pattern, NOT operator-cluster overlap.
    - KELA does NOT attribute to nation-state cluster.
    - Microsoft attribution to Go-based encryptor preserved
      verbatim as Microsoft binding, NOT Archimedes-
      originated.
    - `zeta88` handle preserved as operational chat handle,
      NOT real-identity surface.

  HARD RULE 5 binding constraint: PRESERVED. This finding
  SURFACES The Gentlemen as /new-actor candidacy substrate;
  it does NOT propose roster addition. Operator /new-actor
  decision is reserved for `/new-actor` command invocation.

  HARD RULE 6 binding constraint: PRESERVED. Zero verbatim
  quotes over 15 words; "vibe-coded ... in three days"
  paraphrased to stay under limit.

  HARD RULE 8 binding constraint: First-party Splunk check
  N/A on most The Gentlemen IOCs disclosed this sweep —
  named victim is 2GO Philippine logistics (NOT A&D-prime,
  NOT in Frank's defenseclaw_local visibility scope by
  geography + sector); CVE-2024-55591 FortiOS deployment
  state on Frank's environment not known; 2GO infostealer
  session-token exposure pattern is methodology not
  Archimedes-actionable IOC. NOT extending the standing
  19-IOC PeopleSoft / UNC6240 sentinel set.

source_reliability:
  grade: B
  source_name: "Security Affairs (Paganini) + KELA RansomNews primary"
  source_yaml_id: securityaffairs
  grade_rationale: >
    Cluster anchor source for grading purposes is SA (B-grade,
    provisional, awaiting_ratification per source-grades.yaml
    provisional_since 2026-05-29). KELA RansomNews primary is
    A-tier CTI research firm with leak-site monitoring track
    record; treated as A-tier primary at substrate layer with
    SA B-grade publisher relay providing in-window publication
    surface.
  provisional: true
  provisional_since: 2026-05-29

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_ttps_for_named_actor_or_campaign
    - probably_true_no_contradicting_evidence_from_a_or_b_grade_sources
    - probably_true_technical_claims_internally_coherent_multi_vector_initial_access_pattern_consistent_with_2025_2026_ransomware_tradecraft
  rationale: >
    Grade 2 (Probably True): KELA RansomNews primary deep-dive
    + SA publisher relay; KELA methodology (leak-site
    monitoring + chat-log analysis + infostealer IOC cross-
    validation via alerts.bar) is technically coherent and
    consistent with established CTI research-firm practice.
    Microsoft's separate Go-based encryptor attribution
    (KELA-referenced) is corroborating reference but not
    directly retrieved. Multi-vector initial-access pattern
    is consistent with established 2025-2026 ransomware
    tradecraft. Black Basta training-manual lineage framing
    is novel substrate (Feb 2025 leak as TTP-pattern source)
    but methodologically defensible.

corroboration:
  independent_sources:
    - kela_ransomnews_primary
    - securityaffairs_publisher_relay
    - microsoft_referenced_via_kela_for_go_based_encryptor_attribution
  independent: false  # KELA + SA + Microsoft (via KELA reference) do not constitute three INDEPENDENT evidence bases — Microsoft binding reaches Archimedes only through KELA text
  test_passed: >
    Publisher independence PARTIAL — KELA research firm
    primary + SA B-grade publisher relay constitute two
    surfaces. Microsoft attribution to Go-based encryptor
    is referenced via KELA text rather than retrieved from
    Microsoft directly. Independent THN / BleepingComputer
    / Krebs / Sophos parallel coverage of the same KELA
    primary would lift to multi-publisher-independence-PASS
    and B1 anchor. Evidence-basis: PARTIAL — KELA primary
    is the load-bearing investigation; Microsoft binding is
    referenced not retrieved.
  notes: >
    Direct retrieval of Microsoft's Go-based encryptor
    attribution OR independent THN / BleepingComputer / Krebs
    / Sophos parallel coverage of the same KELA primary
    would lift cluster from B2 to B1.

first_party_precedence:
  applied: false
  splunk_evidence: >
    No A&D-prime-class IOCs disclosed in source this sweep;
    named victim 2GO Philippine logistics is NOT A&D-prime
    and NOT in Frank's defenseclaw_local visibility scope by
    geography + sector. CVE-2024-55591 FortiOS deployment
    state on Frank's environment not known but FortiOS
    appliance class is a known sentinel-class for general
    enterprise hunting if substrate strengthens. NOT
    extending the standing 19-IOC PeopleSoft / UNC6240
    sentinel set this sweep.

single_source_veto_applied: false  # KELA primary + SA relay + Microsoft reference; not strictly single-source despite Microsoft-referenced-not-retrieved
wep_ceiling: likely  # KELA primary + SA relay; absent independent IR-firm or vendor parallel coverage cluster does not reach very_likely
wep_layered:
  kela_ransomnews_primary_research_substrate: very_likely  # A-tier research firm + established methodology
  the_gentlemen_surfaced_2025_09_with_483_victims_by_2026_06_13: likely  # B2 cluster-anchor; leak-site observation
  380_of_483_victims_in_2026_alone_accelerating_trajectory: likely  # KELA observation
  2nd_most_prolific_2026_ransomware_brand_behind_qilin: likely  # KELA ranking claim
  atypically_15_percent_us_victims: likely  # KELA observation
  top_countries_sectors_distribution: likely  # KELA observation
  9_core_members_plus_90_10_affiliate_split: likely  # KELA from chat-log leak
  named_admin_handle_zeta88_operational_only: likely  # KELA from chat-log leak
  multi_vector_initial_access_fortios_zerologon_petitpotam_owa_infostealer: likely  # KELA primary technical claim
  alerts_bar_ioc_cross_validation_methodology_2go_example: likely  # KELA primary methodology demonstration
  ai_assisted_ops_qwen_variant_for_coding_and_data_analysis: likely  # KELA from chat-log leak
  vibe_coded_negotiation_panel_in_three_days: roughly_even_chance  # C3 layer; operator self-claim from chat leak
  black_basta_chat_leak_studied_as_training_manual_DERIVATIVE_NOT_CLUSTER_OVERLAP: likely  # KELA framing; methodologically defensible
  microsoft_go_based_self_propagating_encryptor_attribution_kela_referenced: likely  # B2 reference-quality
  willing_to_get_personal_extortion_pressure_pattern: roughly_even_chance  # C3 single KELA observation
  the_gentlemen_not_on_roster_operator_deferred_new_actor_substrate_strengthening: very_likely  # Verifiable per roster check
  no_us_ad_prime_direct_victim_named: very_likely  # Verifiable absence
  no_nation_state_attribution: very_likely  # Verifiable absence

inclusion:
  eligible_for:
    - daily_brief_monitoring  # B2 → monitoring tier; /new-actor candidacy substrate value + AI-assisted-ops pattern context for A&D-prime sector framing
    - weekly_synthesis  # Ransomware-as-a-business + AI-assisted-ops + Black Basta tradecraft-inheritance pattern strong candidate for Sunday synthesis substrate
  not_eligible_for:
    - flash  # All 6 FLASH triggers NEGATIVE per collector evaluation
    - daily_brief_action  # No US A&D-prime direct victim; no FCEB-class urgency; substrate is contextual not actionable
    - actor_profile_update  # The Gentlemen NOT on roster; Hard Rule 5 prevents Archimedes self-scaffolding new actor; operator /new-actor decision required
  flash_eligible: false
  flash_threshold_met: false

graded_at: 2026-06-15T08:32:00-04:00

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "KELA RansomNews deep-dive on The Gentlemen ransomware operation — 483 victims (2nd-most-prolific 2026 behind Qilin), atypically 15% US victims, Manufacturing top-sector, 9 core members + 90/10 affiliate split, named admin handle `zeta88`, multi-vector initial access (FortiOS CVE-2024-55591 + ZeroLogon + PetitPotam + valid OWA + infostealer primary), AI-assisted ops with Qwen variant, Black Basta chat-leak studied as training manual (DERIVATIVE pattern NOT cluster overlap), Microsoft attributes Go-based encryptor; NOT on 24-actor roster — /new-actor candidacy substrate strengthening for actor-profiler post-PeopleSoft-deadline review"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-15-am-006-sa-kela-the-gentlemen-ransomware-deep-dive-new-actor-candidate-strengthening
  attribution_claims:
    - claimed_attribution: "The Gentlemen ransomware brand (KELA primary research observation + Microsoft Go-based encryptor attribution via KELA reference)"
      claimed_by_sources: [kela_ransomnews_primary, securityaffairs_publisher_relay, microsoft_via_kela_reference]
      requires_analyst_review: false
      note: "Hard Rule 5 binding: Archimedes does NOT propose /new-actor roster addition. This finding SURFACES The Gentlemen substrate as actor-profiler /new-actor candidacy material; operator /new-actor decision is reserved for `/new-actor` command invocation. Microsoft attribution to Go-based encryptor preserved as Microsoft binding via KELA reference (not directly retrieved this sweep)."
    - claimed_attribution: "Black Basta tradecraft-inheritance via Feb 2025 chat-leak studied as training manual"
      claimed_by_sources: [kela_ransomnews_primary]
      requires_analyst_review: false
      note: "Hard Rule 2 binding: The Gentlemen + Black Basta framed by KELA as DERIVATIVE tradecraft pattern, NOT operator-cluster overlap. Archimedes does NOT collapse the two identities."

# ============================================================================
# IOC hunt set
# ============================================================================
iocs:
  cve_references:
    - value: CVE-2024-55591
      type: initial_access_vector_recurring_legacy
      product: FortiOS
      class: authentication_bypass
      note: "Re-used 2024-disclosed vuln; KEV-listed but deadline well-past; widely deployed legacy exposure"
      sources: [kela_ransomnews_primary, microsoft_via_kela_reference]
  initial_access_techniques:
    - ZeroLogon
    - PetitPotam
    - "Valid credentials from compromised Outlook Web Access mailboxes"
    - "Infostealer commodity markets (primary vector)"
  named_victim_with_session_token_pre_exposure_observation:
    - value: "2GO Philippine logistics"
      type: named_ransomware_victim
      pre_exposure_observation:
        employee_logins: 6
        customer_logins: 7
        active_session_tokens: 38
        infostealer_index_source: "alerts.bar"
      ad_prime_relevance: NO
      sources: [kela_ransomnews_primary]
  ai_tooling_pattern:
    - value: "Qwen variant (stripped-down / 'uncensored' / 'abliterated' open-weight model)"
      type: open_weight_model_pattern
      use_case: "coding + analysis of hundreds of GB stolen data"
      sources: [kela_ransomnews_primary]
  operational_handles:
    - value: "zeta88"
      type: leak_chat_handle
      role: administrator
      sources: [kela_ransomnews_primary]
      note: "Operational handle from leaked chats only; NOT real-identity surface"
  tradecraft_lineage:
    - value: "February 2025 Black Basta chat-leak studied as training manual"
      type: tradecraft_inheritance_DERIVATIVE_PATTERN_NOT_CLUSTER_OVERLAP
      sources: [kela_ransomnews_primary]
  encryptor_attribution_via_microsoft_kela_reference:
    - value: "Go-based self-propagating encryptor"
      attribution: "Microsoft (referenced via KELA, not directly retrieved this sweep)"
      sources: [microsoft_via_kela_reference]
  splunk_hunt_state:
    no_hunt_executed_this_sweep: true
    rationale: "Named victim 2GO Philippine logistics NOT A&D-prime and NOT in Frank's defenseclaw_local visibility scope. CVE-2024-55591 FortiOS deployment state on Frank not known. NOT extending standing 19-IOC PeopleSoft / UNC6240 sentinel set."

# ============================================================================
# Relationship to existing findings
# ============================================================================
relationships:
  related_findings:
    - finding_id: finding-2026-06-12-0006
      relationship: "Cluster-adjacent AI-cybercrime substrate — Google civil suit against China-based smishing PhaaS Outsider Enterprise involving Gemini AI weaponization. DIFFERENT actor, DIFFERENT use-case (smishing PhaaS vs ransomware), but SAME meta-category (AI-assisted cybercrime operational substrate). The Gentlemen's Qwen variant for coding + data analysis is a parallel-but-distinct AI-assisted-ops pattern."
    - finding_id_class: "RaaS / extortion-ecosystem substrate"
      relationship: "The Gentlemen substrate joins corpus alongside other RaaS brand tracking (Qilin / ShinyHunters / UNC6240 / Handala) — Hard Rule 5 binding: each retains separate identity in actor-profiler review pending operator /new-actor decisions."

# ============================================================================
# Open questions for analyst / actor-profiler
# ============================================================================
open_questions_for_analyst:
  - "Independent IR-firm / vendor parallel coverage of the KELA primary (THN / BleepingComputer / Krebs / Sophos / Recorded Future / Microsoft direct retrieval) would lift cluster B2 → B1."
  - "Operator /new-actor decision on The Gentlemen — substrate is now research-firm-grade with multi-surface attestation. Recommend actor-profiler review window post-PeopleSoft-deadline-cycle (EOD Sunday 2026-06-15 + Monday morning brief 2026-06-16). Hard Rule 5 binding: Archimedes does NOT self-scaffold; operator `/new-actor` command required."
  - "Manufacturing top-sector + Tier 1-3 country prioritization MAY include A&D-supplier-ecosystem entities at Tier-2/3 levels (smaller machining shops, electronics manufacturers servicing A&D primes). Worth A&D-prime sector-context briefing as substrate-watch but no specific A&D-prime victim named in KELA / SA coverage."
  - "AI-assisted-ops Qwen-variant tooling pattern: weekly synthesis candidate as parallel-but-distinct AI-assisted-cybercrime substrate alongside Google's Outsider Enterprise smishing PhaaS finding-2026-06-12-0006. Both are operational-use-of-AI patterns, not categorical-capability-leap; framing matters for A&D-prime sector context."
  - "Black Basta tradecraft-inheritance via Feb 2025 chat-leak as training-manual lineage — Hard Rule 2 binding requires NO operator-cluster overlap claim; KELA's framing is methodologically defensible (derivative-pattern, not cluster-overlap). Watch for downstream publisher drift to false 'Black Basta lineage' actor-cluster framing."

analyst_review_required: false  # B2 monitoring tier; substrate-watch + actor-profiler surfacing only; no SAT-ACH / SAT-KAC trigger conditions
red_team_review_required: false  # WEP ceiling likely — does not meet very_likely red-team invocation floor

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs:
  - 2026-06-15-morning
retracted: false
retraction_brief_id: null
---

# The Gentlemen Ransomware — KELA Deep-Dive, 483 Victims (2nd Behind Qilin), AI-Assisted Ops, Black Basta Tradecraft-Inheritance, /new-actor Substrate Strengthening

## Summary

Security Affairs (Paganini, 2026-06-15 02:58 EDT) relays
KELA RansomNews 2026-06-13 deep-dive on The Gentlemen
ransomware operation. The Gentlemen surfaced 2025-09 and
has accumulated 483 victims on its Tor leak site by
2026-06-13 — 380 of those in 2026 alone — making it the
second-most-prolific 2026 ransomware brand by leak-site
count behind only Qilin. Distribution is atypical: only
~15% US victims (vs typical 40-50% across other brands),
with top countries Thailand, Brazil, UK, France, India,
Germany, Italy, Japan, Taiwan, and Spain. Top sectors are
Manufacturing (leading), Technology, Business Services,
and Healthcare (44 victims).

Structure per leaked chat logs (May 2026, spanning 2025-11
to 2026-04): 9 core members; affiliate-based with 90/10
revenue split favoring external operators; one named
administrator handle `zeta88` (operational only, no real-
identity surface). Initial-access vector set: FortiOS
CVE-2024-55591 + ZeroLogon + PetitPotam + valid OWA-
mailbox credentials + infostealer commodity markets as
the primary vector. KELA cross-validates the infostealer-
primary pattern with the alerts.bar index — example named
victim 2GO Philippine logistics had 6 employee logins +
7 customer logins + 38 active session tokens exposed
BEFORE 2GO appeared on the Gentlemen leak site.

AI-assisted operations are research-firm-documented: a
stripped-down ("uncensored" / "abliterated") Qwen variant
for coding and analysis of stolen-data sets ("hundreds of
gigabytes"); `zeta88` is reported as having vibe-coded the
negotiation panel in three days. The Feb 2025 Black Basta
chat-leak is described by KELA as having been studied as a
training manual — DERIVATIVE tradecraft inheritance pattern,
NOT operator-cluster overlap (Hard Rule 2 binding).
Microsoft separately documents a Go-based self-propagating
encryptor attributed to The Gentlemen (KELA-referenced;
not directly retrieved this sweep).

The Gentlemen is NOT on Archimedes' 24-actor `_roster.yaml`.
Operator-deferred /new-actor decision substrate continues
strengthening; this finding SURFACES the candidacy material
but does NOT propose roster addition (Hard Rule 5 binding —
operator `/new-actor` command required). No US A&D-prime
direct victim is named; Manufacturing top-sector + Tier 1-3
country prioritization MAY include defense-supplier-ecosystem
entities at Tier-2/3 levels but unnamed in source. Cluster
anchors B2 / WEP likely — KELA primary + SA publisher relay,
multi-tier source convergence with Microsoft binding
referenced via KELA.

## Sources

### KELA RansomNews (research-firm primary, A-tier)

- Primary deep-dive published 2026-06-13.
- Established CTI research firm with leak-site monitoring
  + chat-log analysis + infostealer IOC cross-validation
  methodology.

### Security Affairs (securityaffairs, digraph B)

- URL: https://securityaffairs.com/193622/uncategorized/infostealers-ai-and-a-90-affiliate-cut-fuel-the-gentlemen-groups-rise.html
- Published: 2026-06-15T06:58:21Z (02:58 EDT)
- Byline: Pierluigi Paganini

### Microsoft (via KELA reference, A-tier primary)

- Microsoft separately attributes Go-based self-propagating
  encryptor to The Gentlemen — referenced in KELA text,
  not directly retrieved this sweep.

## Technical detail

- **Scale**: 483 victims on Tor leak site by 2026-06-13;
  380 of those in 2026; 2nd-most-prolific 2026 brand
  behind Qilin only.
- **Geographic**: atypically 15% US (vs 40-50% typical).
  Top countries: Thailand, Brazil, UK, France, India,
  Germany, Italy, Japan, Taiwan, Spain.
- **Sectoral**: Manufacturing (top), Technology, Business
  Services, Healthcare (44 victims).
- **Structure**: 9 core members + 90/10 affiliate revenue
  split (per chat-log leak May 2026 spanning 2025-11 to
  2026-04). One named admin handle `zeta88` (operational
  only).
- **Targeting doctrine** (per leaked chats): Tier 1-3
  countries + Latin America priority; "operational pain
  over raw revenue" rationale.
- **Initial-access vectors**: FortiOS CVE-2024-55591 +
  ZeroLogon + PetitPotam + valid OWA-mailbox credentials +
  infostealer commodity markets (primary vector).
- **Methodology**: KELA cross-references named Gentlemen
  victims against alerts.bar infostealer index — 2GO
  Philippine logistics example (6 employee + 7 customer
  logins + 38 active session tokens exposed BEFORE 2GO
  appeared on Gentlemen leak site).
- **AI-assisted ops**: stripped-down Qwen variant for
  coding + stolen-data analysis ("hundreds of gigabytes");
  vibe-coded negotiation panel in three days
  (KELA-attributed to zeta88 from leaked chats).
- **Tradecraft lineage**: Feb 2025 Black Basta chat-leak
  studied as training manual — DERIVATIVE pattern, NOT
  operator-cluster overlap.
- **Encryptor**: Go-based self-propagating; Microsoft
  attribution (via KELA reference).
- **Extortion approach**: KELA documents one observation
  of operator pressure via sensitive medical content sent
  from compromised personal mailbox (single observation,
  C3 layer).

## Attribution language (preserved per Hard Rule 2)

- KELA does NOT attribute to RU / CN / IR / KP cluster.
- Microsoft attribution to Go-based encryptor preserved
  verbatim as Microsoft binding (KELA-referenced).
- The Gentlemen + Black Basta framed as DERIVATIVE
  tradecraft pattern, NOT operator-cluster overlap.
- `zeta88` preserved as operational chat handle, NOT
  real-identity surface.

## A&D-prime / watchlist match

- **NONE direct.** No US A&D-prime victim named.
- **Indirect / supplier-ecosystem concern**: Manufacturing
  top-sector + Tier 1-3 country prioritization MAY include
  defense-supplier-ecosystem entities at Tier-2/3 levels
  (smaller machining shops, electronics manufacturers
  servicing A&D primes). Not specifically named per KELA
  / SA coverage.

## /new-actor candidacy — Hard Rule 5 binding

The Gentlemen /new-actor candidacy substrate has been
strengthening across recent surfaces (2026-06-15 06:00
FLASH sentinel + this 07:30 pre-brief deep-dive). This
finding SURFACES the substrate for actor-profiler
visibility but does NOT propose roster addition. Operator
`/new-actor The Gentlemen` command invocation is the
authoritative scaffold trigger per Hard Rule 5.

Recommended actor-profiler review window: post-PeopleSoft-
deadline-cycle (EOD Sunday 2026-06-15 + Monday morning
brief 2026-06-16).

## IOCs surfaced

See `iocs` frontmatter block. No Splunk hunt executed this
sweep (named victim NOT A&D-prime + NOT in Frank's
visibility scope by geography + sector). Standing 19-IOC
PeopleSoft / UNC6240 sentinel set NOT extended.

## Relationship to existing findings

- **finding-2026-06-12-0006** (Google civil suit Outsider
  Enterprise China-based smishing PhaaS w/ Gemini AI
  weaponization): cluster-adjacent in meta-category (AI-
  assisted cybercrime operational substrate); different
  actor, different use-case (smishing PhaaS vs ransomware).

## Open questions for analyst / actor-profiler

1. Independent IR-firm / vendor parallel coverage would
   lift B2 → B1.
2. Operator /new-actor decision post-PeopleSoft-deadline
   cycle (Hard Rule 5 binding).
3. A&D-supplier-ecosystem Tier-2/3 manufacturer victim
   exposure — substrate-watch only, no enumeration in
   source.
4. AI-assisted-ops Qwen-variant pattern as weekly-
   synthesis substrate alongside finding-2026-06-12-0006
   AI-cybercrime cluster.
5. Black Basta tradecraft-inheritance framing — Hard
   Rule 2 binding requires NO cluster-overlap claim.
