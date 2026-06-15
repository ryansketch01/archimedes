---
id: finding-2026-06-15-0012
finding_id: finding-2026-06-15-0012-thn-obsidian-security-litellm-3-vuln-chain-low-priv-to-admin-to-rce-ai-gateway-substrate-pending-primary-direct-retrieval
title: "The Hacker News single-publisher relay (snippet substrate ~220 words) of Obsidian Security (provisional B first-surface) research on LiteLLM AI gateway three-vulnerability chain — default low-privilege account can climb to full admin and execute arbitrary code on the LiteLLM proxy server; server takeover exposes every model-provider API key the gateway holds (downstream secondary-victim cascade pattern similar to OnyxC2 MaaS / API-key-aggregator class); LiteLLM is widely deployed OSS AI gateway brokering calls to >100 model providers behind one OpenAI-compatible interface; CVE IDs NOT enumerated in THN snippet (pending Obsidian primary direct retrieval); CVSS scores NOT disclosed; affected/fixed LiteLLM version range NOT disclosed; active exploitation attestation NOT visible in retrievable substrate (pre-disclosure research class likely); LiteLLM maintainer coordination + patch availability NOT disclosed; NO threat actor attribution (Hard Rule 2 preserved); A&D relevance MEDIUM (LiteLLM widely deployed in OSS / enterprise / DIB SDLC pipelines as commercial-LLM-air-gap proxy in CMMC-flow tenants; standard-config-defaults position is the binding gate); related to prior LiteLLM finding-2026-06-10-flash-cve-2026-42271 (command-injection RCE chain — DISTINCT 3-vuln chain this surface vs that finding's chain); NOT FLASH-eligible (T1 PENDING / T6 PENDING — substrate insufficient for trigger evaluation); substrate is monitoring-tier C3 pending Obsidian primary direct retrieval enriching with CVE IDs + CVSS + version range + patch status"
date: 2026-06-15
created_at: 2026-06-15T16:46:00-04:00
graded_by: grader
grading_run_id: afternoon-20260615-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: C3
admiralty_grade: C3
digraph_layered:
  # ---- OBSIDIAN SECURITY PRIMARY RESEARCH LAYER (FIRST-SURFACE PROVISIONAL B) ----
  obsidian_security_litellm_3_vuln_chain_primary_research_first_archimedes_corpus_citation: B3  # Obsidian Security is identity/SaaS security vendor with prior threat research output; first Archimedes-corpus citation; provisional B per cheatsheet — but cluster anchored at C3 due to substrate-fidelity issues below
  # ---- THE HACKER NEWS RELAY LAYER (SINGLE-PUBLISHER, SNIPPET ONLY) ----
  the_hacker_news_single_publisher_b_grade_snippet_substrate: B3  # THN ratified B per source-grades.yaml BUT substrate is ~220-word snippet only, not full article
  no_second_publisher_relay_in_window: A1  # Verifiable absence — BC / SW / SA / TR / DR / Krebs all silent on this item
  obsidian_primary_research_url_NOT_directly_retrieved_this_sweep: A1  # Verifiable per pre-flash sentinel sweep
  # ---- TECHNICAL CHAIN LAYER (CONSTRAINED BY SNIPPET FIDELITY) ----
  three_vulnerability_chain_low_priv_default_account_to_full_admin_to_rce: B3  # Obsidian primary via THN snippet; technical claim
  default_low_privilege_account_starting_position: B3  # Obsidian primary via THN snippet
  server_takeover_exposes_every_provider_key_held_by_gateway: B3  # Obsidian primary via THN snippet; blast-radius framing
  litellm_widely_deployed_oss_ai_gateway_brokering_calls_to_more_than_100_model_providers: A1  # Verifiable per LiteLLM project public documentation; not Obsidian-attribution-dependent
  litellm_openai_compatible_interface_pattern: A1  # Verifiable per LiteLLM project public documentation
  # ---- CVE IDENTIFICATION LAYER ----
  cve_ids_not_enumerated_in_thn_snippet_pending_obsidian_primary_retrieval: A1  # Verifiable absence
  cvss_scores_not_disclosed_in_thn_snippet: A1  # Verifiable absence
  affected_litellm_version_range_not_disclosed_in_thn_snippet: A1  # Verifiable absence
  fixed_litellm_version_not_disclosed_in_thn_snippet: A1  # Verifiable absence
  # ---- ITW EXPLOITATION ATTESTATION LAYER ----
  active_exploitation_attestation_not_visible_in_thn_snippet: A1  # Verifiable absence — pre-disclosure research class likely
  pre_disclosure_research_class_likely_based_on_snippet_substrate: B3  # Inferential; pending Obsidian primary direct retrieval
  # ---- PATCH / VENDOR COORDINATION LAYER ----
  litellm_maintainer_coordination_status_not_disclosed_in_thn_snippet: A1  # Verifiable absence
  patch_availability_not_disclosed_in_thn_snippet: A1  # Verifiable absence
  # ---- ATTRIBUTION-DISCIPLINE LAYER (HARD RULE 2 BINDING) ----
  no_threat_actor_attribution_in_thn_snippet_or_obsidian_research_class: A1  # Verifiable absence; Hard Rule 2 preserved
  pre_disclosure_research_class_no_actor_extrapolation: A1  # Hard Rule 2 binding
  # ---- A&D / DIB RELEVANCE LAYER ----
  ad_direct_relevance: A1  # NONE — no A&D-prime victim named (pre-disclosure research class)
  ad_structural_relevance_litellm_deployed_in_dib_sdlc_pipelines_oss_ai_gateway_class: B3  # Structural inference — no source-attested DIB deployment-density data
  ad_structural_relevance_cmmc_flow_tenants_air_gapping_commercial_llm_access_behind_internal_proxy: B3  # Structural inference — pattern is plausible but density not source-attested
  ad_structural_relevance_standard_config_defaults_position_is_binding_gate: B3  # Structural inference — default-low-priv-account-existing is the key exposure-gating question; pending Obsidian primary retrieval for specifics
  # ---- IOC LAYER ----
  no_iocs_in_thn_snippet_no_hashes_ips_domains_urls: A1  # Verifiable absence — research-class disclosure
  # ---- FIRST-PARTY SPLUNK LAYER (HARD RULE 8 BINDING) ----
  splunk_first_party_check_invoked_30d_lookback_litellm_keyword: A1  # Procedural — search executed
  splunk_first_party_zero_hits_on_external_indicators: A1  # Verifiable per query result — only hits were Archimedes' own operational meta-logging on prior LiteLLM CVE-2026-42271 FLASH brief
  frank_does_not_run_litellm_gateway_at_relevant_scale_visibility_bounded_absence: A1  # Frank-environment-specific; Hard Rule 8 binding
  no_first_party_telemetry_contradiction_or_confirmation_available: A1  # Verifiable per Hard Rule 8 binding
  # ---- RELATED PRIOR CORPUS SUBSTRATE LAYER ----
  prior_corpus_finding_2026_06_10_flash_cve_2026_42271_litellm_command_injection_rce_chain: A2  # Carry-forward reference; DISTINCT 3-vuln chain (this surface is auth-bypass-to-admin-to-RCE; prior was command-injection)
  litellm_substrate_now_multi_chain_class_in_corpus: B2  # Inferential — corpus now has two distinct LiteLLM attack-chain classes
  # ---- ANTI-NOISE DISPOSITION LAYER ----
  net_new_disclosure_distinct_from_finding_2026_06_10_flash_litellm_substrate: A1  # Verifiable — different vuln chain mechanism
  not_under_existing_anti_noise_hold: A1  # Verifiable per pre-flash sentinel sweep audit
  cluster_anchor: C3

digraph_anchor: >
  Cluster anchored at C3 (Possibly True / monitoring-tier inclusion).
  The Hacker News (ratified B per source-grades.yaml) single-publisher
  ~220-word snippet substrate of Obsidian Security primary research
  on LiteLLM AI gateway three-vulnerability chain. Obsidian Security
  is provisional B first-surface per cheatsheet "named vendor with
  structured public technical research" precedent — but the cluster
  anchors at C3 due to substrate-fidelity issues that constrain
  inclusion to monitoring-tier.

  WHY C3 NOT B2:
    1. THN SNIPPET SUBSTRATE ONLY. Article surface is ~220 words
       visible to collector this sweep — not a full publisher
       relay. Detail beyond the chain-outline + LiteLLM-deployment
       scale is NOT in retrievable substrate.
    2. OBSIDIAN PRIMARY NOT DIRECTLY RETRIEVED. Substrate reaches
       the cluster through THN snippet relay only — primary
       research URL not directly retrieved this sweep.
    3. NO SECOND PUBLISHER RELAY. BleepingComputer / SecurityWeek /
       SecurityAffairs / The Record / Dark Reading / Krebs all
       silent on this item in window. Single-publisher single-
       snippet substrate.
    4. NO CVE IDS / NO CVSS / NO VERSION RANGE / NO PATCH STATUS.
       The four canonical inclusion-gates for action-tier
       substrate are all missing from THN snippet.
    5. NO ACTIVE EXPLOITATION ATTESTATION. Pre-disclosure research
       class likely (inferential) — no ITW substrate visible.

  WHY MONITORING-TIER INCLUSION NOT REJECT:
    1. LiteLLM is widely deployed OSS AI gateway brokering calls
       to >100 model providers behind one OpenAI-compatible
       interface — structurally significant attack surface.
    2. Blast-radius framing (server takeover exposes every
       provider API key held by gateway) is operationally
       meaningful given downstream secondary-victim cascade
       pattern.
    3. Substrate is corpus-coherent with prior LiteLLM substrate
       (finding-2026-06-10-flash-cve-2026-42271 command-injection
       RCE chain — DISTINCT 3-vuln chain this surface).
    4. Recommend Obsidian primary direct retrieval next sweep —
       if CVE IDs + CVSS + active exploitation surface, this can
       be elevated to action-tier or FLASH candidate.

  WHY MONITORING-TIER INCLUSION NOT ACTION-TIER:
    1. Substrate insufficient for action-tier inclusion gates
       (no CVE IDs / no CVSS / no version range / no patch
       status / no ITW attestation).
    2. Action-tier inclusion threshold per INTEL-GRADING.md is
       B2; this finding fails the substrate-fidelity test for
       B2 due to single-publisher single-snippet retrieval state.
    3. Monitoring-tier inclusion (C3) is the appropriate
       threshold per INTEL-GRADING.md while awaiting Obsidian
       primary direct retrieval.

  WHAT THE C3 ATTESTS:
    (a) Obsidian Security has disclosed (via THN snippet) a
        three-vulnerability chain in LiteLLM AI gateway allowing
        a default low-privilege account to climb to full admin
        and execute arbitrary code on the server.
    (b) Server takeover exposes every model-provider API key
        held by the LiteLLM gateway (blast-radius framing).
    (c) LiteLLM is widely deployed OSS AI gateway brokering
        calls to >100 model providers behind one OpenAI-
        compatible interface (verifiable public fact, not
        Obsidian-attribution-dependent).

  WHAT THE C3 DOES NOT ATTEST:
    - Specific CVE IDs (not enumerated in THN snippet).
    - CVSS scores (not disclosed).
    - Affected / fixed LiteLLM version range (not disclosed).
    - Patch availability + LiteLLM maintainer coordination
      status (not disclosed).
    - Active in-the-wild exploitation (not attested).
    - Specific threat actor attribution (Hard Rule 2 preserved).
    - Specific A&D / DIB deployment-density data for LiteLLM
      (structural inference only).
    - First-party Frank-environment telemetry confirmation or
      contradiction (Frank does not run LiteLLM at relevant
      scale; visibility-bounded absence per Hard Rule 8 binding).

  HARD RULE 2 binding constraint: PRESERVED.
    - No actor attribution originated by Archimedes.
    - Pre-disclosure research class — no exploitation pattern
      claimed for any specific actor.

  HARD RULE 6 binding constraint: NOT APPLICABLE.
    - No source quotes in retrievable THN snippet; substrate is
      paraphrase-only.

  HARD RULE 8 binding constraint: PRESERVED.
    - Splunk first-party check invoked with 30-day lookback;
      ZERO hits on LiteLLM keyword across defenseclaw_local +
      archimedes (the 2 hits returned were Archimedes' own
      operational meta-logging on prior LiteLLM CVE-2026-42271
      FLASH brief — NOT first-party LiteLLM telemetry).
    - Frank does not run LiteLLM gateway at relevant scale;
      silent-Splunk-does-NOT-disconfirm per Hard Rule 8 binding.

source_reliability:
  grade: B
  source_name: "Obsidian Security primary research via The Hacker News single-publisher snippet substrate"
  source_yaml_id: obsidian-security (PROVISIONAL — proposed source-grades.yaml addition) + thehackernews
  grade_rationale: >
    Obsidian Security is provisional B per cheatsheet "named vendor
    with structured public technical research" — identity/SaaS
    security vendor with prior threat research output. First
    Archimedes-corpus citation this sweep via raw-2026-06-15-pm-007.
    Recommend librarian source-grades.yaml addition for operator
    ratification. THN ratified B per source-grades.yaml — but
    substrate is ~220-word snippet only, constraining cluster anchor
    despite acceptable source grade.
  provisional: true
  provisional_note: "Obsidian Security first Archimedes-corpus citation; provisional B per cheatsheet; flag for librarian source-grades.yaml addition + operator ratification"

credibility:
  grade: 3
  checklist_passed:
    - single_source_uncorroborated_but_source_is_b_grade_or_better
    - technical_claims_plausible_but_not_independently_verifiable
  rationale: >
    Single-source (THN snippet of Obsidian primary), uncorroborated
    in window. Source is B-grade (THN ratified; Obsidian provisional
    B). Technical claims (3-vuln chain default-low-priv → admin →
    RCE) plausible given LiteLLM's known auth-model complexity and
    corpus carry-forward (finding-2026-06-10-flash-cve-2026-42271
    LiteLLM substrate establishes precedent for the vendor's vuln
    pattern) but NOT independently verifiable through retrievable
    substrate this sweep. CVE IDs / CVSS / version range / patch
    status all missing — material substrate gaps.

corroboration:
  independent_sources:
    - obsidian-security  # primary research (provisional B first-surface)
    - thehackernews      # single-publisher snippet relay
  independent: false
  test_passed: >
    Single-publisher single-snippet substrate. No second publisher
    relay in window (BC / SW / SA / TR / DR / Krebs all silent).
    Obsidian primary research URL not directly retrieved this sweep.
    Per INTEL-GRADING.md rule of thumb, the chain has single-vendor
    primary-research evidence basis with single-publisher relay —
    independence test FAILS.
  independent_layered:
    obsidian_security_primary_research: true   # Vendor-canonical primary evidence basis
    thehackernews_relay: false                 # Publisher relay of Obsidian primary; only retrievable substrate this sweep

first_party_precedence:
  applied: true
  splunk_evidence:
    query_executed: "search index=archimedes OR index=defenseclaw_local (LiteLLM) earliest=-30d"
    hits_on_external_indicators: 0
    note: >
      Splunk first-party check invoked with 30-day lookback. Zero
      first-party hits on defenseclaw_local + archimedes for LiteLLM
      keyword. The 2 hits returned were Archimedes' own operational
      meta-logging on prior LiteLLM CVE-2026-42271 FLASH brief —
      NOT first-party LiteLLM telemetry. Frank does not run LiteLLM
      gateway at relevant scale; silent-Splunk-does-NOT-disconfirm
      per Hard Rule 8 binding. Visibility-bounded absence flagged,
      NOT treated as negative evidence.

single_source_veto_applied: true
single_source_veto_layers:
  - obsidian_security_primary_only_via_thn_single_publisher_snippet_substrate
  - no_second_publisher_relay_in_window
  - obsidian_primary_research_url_not_directly_retrieved
wep_ceiling: likely  # Capped by single-source veto; substrate-fidelity issues further constrain to monitoring-tier

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "LiteLLM AI gateway 3-vuln chain (default low-priv → admin → RCE) — Obsidian Security primary research via The Hacker News snippet substrate — pending direct retrieval enrichment"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-15-pm-007-thn-litellm-vuln-chain-obsidian-security-primary
  attribution_claims: []
  attribution_claims_note: "No threat actor attribution by Obsidian Security or The Hacker News. Hard Rule 2 preserved. Pre-disclosure research class likely (inferential)."

# ============================================================================
# Inclusion eligibility
# ============================================================================
inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - ai_attack_class_tracking
  not_eligible_for:
    - flash  # T1 PENDING (no CVE IDs, no CVSS, no ITW attestation); T6 PENDING (no patch status disclosed)
    - actor_profile_update  # No actor attribution
    - vuln_tracker_update  # No CVE IDs disclosed — substrate insufficient

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: true   # Monitoring-tier substrate gaps + AI attack-class novelty + DIB AI-gateway-class exposure
analyst_review_complete: true
analyst_review_run_id: analyst-20260615-160800
red_team_review_required: false # WEP ceiling capped at "likely" per single-source veto; monitoring-tier
red_team_review: null
analysis_sections:
  sat_ach: null  # NOT APPLICABLE — no attribution claim, pre-disclosure research-class substrate, no competing hypotheses
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Obsidian Security primary research (via THN snippet only) discloses LiteLLM
        3-vuln chain enabling default-low-priv → full-admin → RCE; substrate-fidelity
        issues constrain to monitoring-tier C3 pending Obsidian primary direct retrieval."
      analyzed_at: 2026-06-15T16:46:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication; substrate-fidelity check; AI attack-class novelty; corpus-coherence with prior LiteLLM substrate"
      assumptions:
        - id: A1
          statement: "THN snippet accurately reflects Obsidian Security primary research substance"
          category: source_reliability
          stated: false
          why_must_be_true: "Substrate is THN-snippet-only — all claims pass through one publisher's interpretation"
          when_could_be_false: "Snippet may have summarized incorrectly; snippet may have foregrounded marketing framing; ~220-word substrate is materially constrained"
          evidence_for: [thn_ratified_b_per_source_grades_yaml]
          evidence_against: [single_publisher_snippet_only_no_independent_verification]
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A2
          statement: "Default low-privilege account exists in standard LiteLLM deployments without operator-side hardening"
          category: technology
          stated: false
          why_must_be_true: "Exposure-gating depends on default-account-presence in real deployments"
          when_could_be_false: "Default account may have been removed in recent LiteLLM versions; operator-side hardening may be standard practice in DIB / enterprise deployments; vendor-default-config may be more restrictive than implied"
          evidence_for: [thn_snippet_framing_implies_default_low_priv_starting_position]
          evidence_against: [no_specific_litellm_version_range_disclosed]
          confidence: low
          centrality: critical
          classification: test
        - id: A3
          statement: "LiteLLM is widely deployed in DIB / CMMC partner-flow tenants as commercial-LLM-air-gap proxy"
          category: ad_relevance
          stated: true
          why_must_be_true: "A&D relevance MEDIUM framing depends on actual DIB LiteLLM deployment density"
          when_could_be_false: "LiteLLM is one of several AI-gateway-class options (LangChain, LlamaIndex, etc.); DIB tenants may have selected alternatives; air-gap-proxy pattern may be less common than implied"
          evidence_for: [litellm_widely_deployed_oss_ai_gateway_brokering_calls_to_100_plus_model_providers]
          evidence_against: [no_source_attested_dib_litellm_deployment_density_data]
          confidence: low
          centrality: material
          classification: qualify
        - id: A4
          statement: "No CVE IDs / no CVSS / no version range / no patch status is correctly inferred to mean substrate is insufficient for action-tier"
          category: source_reliability
          stated: true
          why_must_be_true: "C3 monitoring-tier inclusion gate rests on substrate-fidelity assessment"
          when_could_be_false: "Substrate gaps may be THN snippet artifacts rather than Obsidian primary gaps; Obsidian primary may carry all four canonical inclusion-gates and direct retrieval would lift to B2/B1"
          evidence_for: [thn_snippet_220_word_substrate_constraint]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A5
          statement: "Pre-disclosure research class likely (inferred from snippet substrate not mentioning patch/ITW)"
          category: ttp_patterns
          stated: false
          why_must_be_true: "WEP framing depends on substrate-class characterization"
          when_could_be_false: "Obsidian may have published post-coordinated-disclosure with patch already available; THN snippet may have omitted coordination detail"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 2
        qualify: 2
        test: 1
        reject: 0
      remediation:
        status: proceed
        blocking_assumption: A2
        blocking_detail: |
          A2 (default low-privilege account exists in standard LiteLLM deployments
          without operator-side hardening) is low-confidence + critical-centrality.
          Test: retrieve Obsidian Security primary research URL OR check LiteLLM
          project documentation for default-account-configuration patterns OR check
          for prior LiteLLM CVE patterns. WITHOUT this test, exposure-gating
          framing cannot be confirmed; monitoring-tier C3 inclusion is appropriate
          and proceeds without action-tier elevation pending substrate enrichment.
        qualifying_caveats:
          - "THN snippet substrate is single-publisher single-snippet (~220 words); all claims pass through one interpretation (A1 qualify)"
          - "DIB LiteLLM deployment density is structural inference, not source-attested (A3 qualify)"
        next_action: "Proceed to publication at C3 monitoring-tier as graded; PRIORITY: Obsidian Security primary direct retrieval next sweep (substrate-elevation pathway from C3 → B2 or FLASH candidate). Flag Obsidian Security source-grade addition to librarian."
      recommended_wep_after_test:
        if_obsidian_primary_carries_cve_cvss_version_patch: "C3 → B2 action-tier; rerun KAC"
        if_active_exploitation_attestation_surfaces: "FLASH candidate; rerun KAC with urgency"
        if_default_account_not_present_in_recent_litellm_versions: "A2 satisfied; exposure-gating narrows"
        current_state: "C3 monitoring-tier is appropriate; substrate insufficient for higher tier"

direct_retrieval_handoff:
  proposed_action: obsidian_security_primary_direct_retrieval_high_priority
  rationale: |
    Substrate-elevation pathway from C3 monitoring-tier to potential B2
    action-tier requires Obsidian primary research URL direct retrieval
    enriching with:
      - CVE IDs (if assigned)
      - CVSS scores
      - LiteLLM affected version range
      - Fixed version (if available)
      - Active exploitation attestation (if any)
      - LiteLLM maintainer coordination + patch availability status
    Direct retrieval recommended for next sweep. If CVE IDs + CVSS ≥9.0
    + active exploitation surface, this becomes FLASH candidate.

source_grade_revision_proposed:
  - source_id: obsidian-security
    proposed_grade: B
    rationale: |
      First Archimedes-corpus citation via raw-2026-06-15-pm-007 (LiteLLM
      3-vuln chain disclosure via The Hacker News). Obsidian Security is
      an identity/SaaS security vendor with prior threat research output.
      Conservative provisional B starting grade per same precedent class
      as the existing vendor-research Tier-2 provisional grades
      (StepSecurity / Socket / Sysdig / Zellic / Push Security / Varonis
      Threat Labs first-surface this same brief cycle).

# ============================================================================
# Lifecycle
# ============================================================================
tlp: CLEAR
published_in_briefs:
  - 2026-06-15-afternoon
retracted: false
retraction_brief_id: null
---

# Obsidian Security (provisional B first-surface) discloses LiteLLM 3-vuln chain via The Hacker News snippet substrate — default low-priv → full admin → RCE; server takeover exposes all model-provider API keys; LiteLLM widely deployed OSS AI gateway; CVE IDs / CVSS / patch status NOT in retrievable substrate (pending Obsidian primary direct retrieval); monitoring-tier C3 pending substrate enrichment

## Summary

The Hacker News single-publisher snippet substrate (~220 words visible to
collector) covers Obsidian Security primary research disclosing a
three-vulnerability chain in LiteLLM — a widely deployed open-source AI
gateway that brokers calls to more than 100 model providers behind one
OpenAI-compatible interface. A default low-privilege account on a LiteLLM
proxy can climb to full admin and execute arbitrary code on the server by
chaining the three vulnerabilities. **Blast radius**: a server takeover
exposes every model-provider API key held by the gateway — downstream
secondary-victim cascade pattern similar to the OnyxC2 MaaS class in
finding-2026-06-11-0010 or general API-key-aggregator attack classes.
**Substrate gaps**: CVE IDs NOT enumerated in THN snippet; CVSS scores NOT
disclosed; affected and fixed LiteLLM version range NOT disclosed; active
exploitation attestation NOT visible (pre-disclosure research class likely);
LiteLLM maintainer coordination + patch availability NOT disclosed. **NO
threat actor attribution** (Hard Rule 2 preserved). A&D relevance MEDIUM:
LiteLLM is widely deployed in OSS / enterprise / DIB SDLC pipelines as a
commercial-LLM-air-gap proxy in CMMC-flow tenants; standard-config-defaults
position is the binding gate. **Related to prior LiteLLM substrate** —
finding-2026-06-10-flash-cve-2026-42271 (command-injection RCE chain — this
surface is a DISTINCT 3-vuln chain). Cluster anchored at C3 monitoring-tier
pending Obsidian primary direct retrieval enriching substrate with CVE IDs
+ CVSS + version range + patch status. NOT FLASH-eligible (substrate
insufficient for trigger evaluation).

## Sources

### The Hacker News (source_yaml_id: thehackernews, digraph: B)

- URL: https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html
- Published: 2026-06-15 16:39 UTC
- Byline: not visible
- Substrate: ~220-word snippet visible to collector
- Key claim: Single-publisher snippet relay of Obsidian Security primary research; chain outline + blast-radius framing + LiteLLM deployment scale

### Obsidian Security (primary research, provisional B first-surface)

- URL: not directly retrieved this sweep (HIGH PRIORITY flag for next-sweep retrieval)
- Source-layer: vendor primary research
- Provisional grade: B per cheatsheet "named vendor with structured public technical research"
- Key claim: LiteLLM 3-vuln chain enabling default-low-priv → full-admin → RCE escalation

## Technical detail

### Vulnerability overview (constrained by THN snippet fidelity)

- **Product**: LiteLLM (widely deployed open-source AI gateway brokering
  calls to more than 100 model providers behind one OpenAI-compatible
  interface)
- **Chain**: Three vulnerabilities (specific CVE IDs NOT enumerated in
  THN snippet)
- **Privilege progression**: Low-privilege default account → full admin
  → arbitrary code execution on server
- **Blast radius**: A server takeover exposes every model-provider API
  key held by the gateway — the secrets that govern access to LLM-provider
  API endpoints downstream

### Substrate gaps (pending Obsidian primary direct retrieval)

The following are NOT visible in the THN snippet substrate retrievable
this sweep:

- Specific CVE IDs (if assigned)
- CVSS scores
- Affected LiteLLM version range
- Fixed version (if available)
- Active in-the-wild exploitation attestation
- LiteLLM maintainer coordination timeline
- Patch availability status

Direct retrieval of Obsidian Security primary research URL is HIGH PRIORITY
for next-sweep substrate-elevation pathway from C3 monitoring-tier to
potential B2 action-tier.

### A&D / DIB structural relevance

LiteLLM is widely deployed as an OSS AI gateway in OSS / enterprise / DIB
SDLC pipelines that mediate calls to commercial LLM providers (OpenAI /
Anthropic / Google / etc). Notable pattern in CMMC-flow tenants that
air-gap commercial LLM access behind an internal proxy. Server takeover =
exfil of all provider API keys held by the gateway = downstream
secondary-victim cascade pattern.

Standard config-defaults position is the binding gate — if the "default
low-privilege account" is widely present in default LiteLLM deployments
without operator-side hardening, exposure is meaningful. Obsidian primary
likely carries this detail.

## IOCs surfaced

```yaml
iocs:
  cves: []   # CVE IDs NOT enumerated in THN snippet — pending Obsidian primary retrieval
  hashes: []
  ips: []
  domains: []
  urls: []

attribution_claims: []
attribution_claims_note: "No threat actor attribution by Obsidian Security or The Hacker News. Hard Rule 2 preserved. Pre-disclosure research class likely (inferential)."
```

## Relationship to existing findings

- **Lateral linkage to prior LiteLLM substrate**:
  - finding-2026-06-10-flash-cve-2026-42271 (LiteLLM CVE-2026-42271
    command-injection RCE chain — this surface is a DISTINCT 3-vuln chain
    with different mechanism)
  - LiteLLM corpus substrate now has multi-chain-class pattern
- **Lateral linkage to broader AI-gateway / AI-attack-class substrate
  cluster**:
  - finding-2026-06-15-0011 (SearchLeak CVE-2026-42824 M365 Copilot
    Enterprise — distinct AI-attack-class chain in this same brief cycle)
  - finding-2026-06-12-0007 (Agentjacking + Langgraph 3-CVE chain)
  - finding-2026-06-11-0008 (Langflow CVE-2026-5027 ITW)
  - finding-2026-06-11-0010 (OnyxC2 MaaS API-key-aggregator class)

## Open questions for analyst / direct-retrieval-handoff

1. **Obsidian primary direct retrieval** (HIGH PRIORITY, direct-retrieval
   handoff): Retrieve Obsidian Security primary research URL for substrate
   enrichment. Specifically: CVE IDs, CVSS scores, LiteLLM affected/fixed
   version range, active exploitation attestation, LiteLLM maintainer
   coordination timeline, patch availability. Substrate-elevation pathway
   from C3 monitoring-tier to potential B2 action-tier OR FLASH candidate
   contingent on retrieval results.
2. **Source-grade ratification for Obsidian Security** (librarian handoff):
   First Archimedes-corpus citation; provisional B per cheatsheet.
   Recommend librarian source-grades.yaml addition with operator
   ratification per source-grade-log.md pattern.
3. **LiteLLM maintainer coordination watch** (analyst): Whether LiteLLM
   maintainers have published patch or whether Obsidian's disclosure is
   coordinated-with-maintainer or independent-disclosure shapes immediacy
   of operator action. Direct retrieval should clarify.
4. **Second-publisher relay watch** (analyst): No BC / SW / SA / TR / DR /
   Krebs in-window coverage this sweep. Watch for second-publisher
   convergence next sweep; would lift substrate-fidelity weakness.
5. **A&D / DIB AI-gateway deployment-state check** (operator surface):
   A&D-prime defenders running internal LiteLLM gateways for AI tooling
   adoption (notably in CMMC-flow tenants that air-gap commercial LLM
   access behind an internal proxy) should evaluate exposure. Default-
   config-defaults audit gates this; pending Obsidian primary disclosure
   for specific exposure-gating details.
6. **AI attack-class pattern tracking** (analyst): Adds to AI-attack-class
   corpus substrate alongside SearchLeak (finding-2026-06-15-0011) this
   same brief cycle. Multi-chain-class LiteLLM substrate now present in
   corpus (command-injection from finding-2026-06-10-flash + this 3-vuln
   chain). Patterns emerging across AI-gateway-class substrate worth
   weekly-synthesis treatment.

## Analytic notes (from analyst review)

KAC ran on five assumptions; two sound, two qualify, one Test. ACH was not applied — no attribution claim, pre-disclosure research class, no competing-hypothesis question. The grader's substrate-fidelity assessment (C3 monitoring-tier, four canonical inclusion gates missing) is methodologically sound and KAC supports it.

A2 (default low-privilege account exists in standard LiteLLM deployments without operator-side hardening) is the load-bearing Test classification — low-confidence at critical-centrality. The blast-radius framing collapses if default accounts don't actually exist in current LiteLLM versions; the entire exposure-gating story rests on this assumption. Obsidian primary direct retrieval is the test pathway.

C3 monitoring-tier inclusion is appropriate. No red-team escalation. Single highest-priority handoff: Obsidian Security primary direct retrieval next sweep — if CVE IDs + CVSS + version range + patch + ITW status surface, substrate elevates to action-tier or FLASH candidate; rerun KAC then. Librarian source-grade addition for Obsidian Security recommended.
