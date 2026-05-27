---
finding_id: finding-2026-05-27-0005-mstic-cryptojacking-screenconnect-ai-chatbot-seo-poisoning-gleeze-com-dynu-autorun-dll
created_at: 2026-05-27T08:22:00-04:00
graded_by: grader
grading_run_id: morning-20260527-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: A2
digraph_layered:
  mstic_cryptojacking_campaign_disclosure: A2
  novel_ai_chatbot_poisoning_methodology_class: A2
  screenconnect_dll_sideload_autorun_dll_persistence: A2
  150_plus_malicious_domains_since_march_2026: A2
  gleeze_com_parent_domain_dynu_dynamic_dns: A2
  utility_brand_impersonation_crystaldiskinfo_hwmonitor_ddu_furmark_klite_pdfgear: A2
  nine_distinct_autorun_dll_variants_observed: A2
  llm_referral_metadata_in_virustotal_traffic: A2
  unknown_threat_actor_explicit_mstic_attribution: A1   # MSTIC explicit decline-to-attribute is procedural
  no_cve_in_primary_scope: A1
  no_ad_prime_named_victim: A1
  thn_pre_window_relay_b_grade_supporting_context: B2
  cluster_anchor: A2

digraph_anchor: >
  Cluster digraph A2 anchored on Microsoft Security Blog (Microsoft
  Defender Experts + Microsoft Defender Security Research Team joint
  byline, 2026-05-26 21:35 UTC = 17:35 EDT yesterday, in-window for
  AM-27 16h pre-brief). MSTIC is A-grade per source-grades.yaml.
  Single-source A-grade primary on the cryptojacking campaign
  disclosure and novel AI-chatbot-poisoning methodology class. The
  Hacker News (Ravie Lakshmanan 2026-05-27 03:45 EDT) is a B-grade
  relay that was discarded at the 06:00 FLASH sentinel (no roster /
  no A&D / no vuln-index hit); the MSTIC primary warrants raw-
  signaling and finding-tier promotion at primary tier rather than
  letting the relay-tier discard stand.

  A2 (not A1) holds because: single A-grade source on the campaign
  disclosure layer. The Hacker News relay does not constitute
  independent corroboration. No second A/B-grade vendor (Mandiant,
  Unit 42, CrowdStrike, Cisco Talos, Sophos) has published parallel
  telemetry on this cryptojacking campaign. Procedural artifacts
  (gleeze.com parent domain, Dynu DDNS infrastructure, 9 autorun.dll
  variants, 6 impersonated utility brands, ScreenConnect abuse,
  150+ malicious domains since March 2026) are individually well-
  characterized but the cluster anchor follows single-source weakest-
  link operational claim per INTEL-GRADING.

  Single-source veto applies: forward-looking WEP claims (campaign
  continuation, AI-chatbot-poisoning becoming standard tradecraft)
  cap at "likely". Procedural facts reach individual A1 on
  defender-actionable artifacts.

source_reliability:
  grade: A
  source_name: "Microsoft Security Blog (Microsoft Defender Experts + Microsoft Defender Security Research Team)"
  source_yaml_id: mstic
  grade_rationale: >
    MSTIC pre-assigned A per source-grades.yaml. Microsoft Defender
    Experts + Microsoft Defender Security Research Team joint byline
    is the consistent MSTIC publication convention for ecosystem-
    level abuse research and is operationally equivalent in source-
    grade to bylined MSTIC research. In-window publication
    2026-05-26 17:35 EDT (yesterday afternoon, within 16h AM-27
    pre-brief window).
  provisional: false
  pre_window_relay:
    source_yaml_id: thehackernews
    source_grade: B
    publication: "AI Chatbot Recommendations Redirect [...]"
    publication_date: 2026-05-27T07:45:52Z
    contribution: >
      B-grade media relay of the MSTIC primary publication, with
      emphasis on the novel AI-chatbot-poisoning methodology layer.
      Already evaluated at 06:00 EDT FLASH sentinel and discarded at
      relay-tier per Mode 1 (no roster / no A&D / no vuln-index hit).
      Does NOT add independent corroboration on the campaign
      disclosure.

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_ttps_or_known_campaign_timing_targeting
    - probably_true_no_contradicting_evidence_from_ab_grade_sources
    - probably_true_technical_claims_internally_coherent
  grade_1_test:
    - independent_corroboration_present_no: "THN is a relay of MSTIC; not independent. No second A/B-grade vendor has published parallel telemetry."
    - grade_1_blocked_by: "Single-source A-grade vendor on the campaign disclosure claim. Procedural artifacts are individually A1 but cluster anchor follows weakest-link operational claim."
  rationale: >
    The campaign tradecraft (SEO poisoning + DLL sideloading +
    ScreenConnect abuse + cryptojacking GPU mining) is consistent with
    established commodity-actor cryptojacking tradecraft. The novel
    layer (AI chatbot poisoning - users querying LLM-based tools for
    software download recommendations are presented with attacker-
    controlled domains) is internally coherent with the broader SEO-
    poisoning attack surface being absorbed into AI-chatbot training
    data and retrieval pipelines. MSTIC's careful framing ("this
    example is illustrative and does not indicate a systemic issue
    with any specific AI service") preserves the structural-warning
    layer without attributing the chatbot behavior to any specific
    LLM vendor's product flaw. The target-quality-over-volume pattern
    (high-performance PC enthusiast utility brands - CrystalDiskInfo,
    HWMonitor, DDU, FurMark, K-Lite, PDFgear - users with discrete
    GPUs viable for crypto mining) is operationally coherent. The
    150+ malicious domains since March 2026 + gleeze.com + Dynu DDNS
    infrastructure scope is empirically scoped and defender-actionable.

corroboration:
  independent_sources:
    - mstic (A-grade primary)
  independent: false
  test_passed_no: >
    Cluster has ONE effective A-grade source. THN is a B-grade relay
    of MSTIC; per INTEL-GRADING.md independence test, a relay is not
    independent corroboration. No parallel A/B-grade vendor publication
    on this cryptojacking campaign as of this sweep.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    Splunk query against defenseclaw_local + archimedes over -24h
    covering "gleeze.com", "Dynu", "ScreenConnect", "autorun.dll",
    "CrystalDiskInfo", "HWMonitor", "FurMark". Zero events. Hard Rule
    8: silence not disconfirming. A&D-prime engineering workstation
    download of one of the named utility brands during the campaign
    window would have been potentially exposed; defenseclaw_local
    silence is consistent with either no-exposure or with exposure
    on network segments outside archimedes/defenseclaw_local Splunk
    visibility.

single_source_veto_applied: true
single_source_veto_rationale: >
  Per INTEL-GRADING.md, A-grade single-source claims cap at WEP
  "likely" until independent corroboration. THN relay does not
  corroborate MSTIC. Cluster veto applies on forward-looking
  campaign-continuation and AI-chatbot-poisoning-becoming-standard-
  tradecraft claims; procedural defender-actionable artifacts (IOCs,
  detection guidance) reach very_likely individually as MSTIC-
  published facts.

wep_ceiling: likely
wep_layered:
  cryptojacking_campaign_active_at_mstic_publication: very_likely        # MSTIC publication = procedural fact
  150_plus_malicious_domains_existed_since_march_2026: very_likely       # MSTIC-empirical
  gleeze_com_dynu_infrastructure_attribution: very_likely                # MSTIC-observed
  9_autorun_dll_variants_observed: very_likely                           # MSTIC-empirical
  screenconnect_dll_sideload_mechanism: very_likely                      # MSTIC-observed
  ai_chatbot_poisoning_methodology_demonstrated: likely                  # MSTIC-observed but novel class; single-source veto on novelty
  ai_chatbot_poisoning_becomes_standard_tradecraft_industry_wide: likely # forward projection; veto applies
  campaign_continuation_through_q2_2026: likely                          # operational continuation
  no_actor_attribution_correctness: very_likely                          # MSTIC explicit unknown; Hard Rule 2 holds
  ad_prime_engineering_workstation_indirect_exposure: roughly_even_chance  # structural inference
  follow_on_data_theft_lateral_movement_ransomware_risk: roughly_even_chance  # MSTIC speculative "could later support"

inclusion:
  eligible_for:
    - daily_brief_action            # A2 + novel attack class for defender awareness
    - daily_brief_monitoring
    - weekly_synthesis              # pattern signal on AI-chatbot-poisoning emerging class
    - ioc_master_index_propagation  # gleeze.com, Dynu, autorun.dll patterns
  not_eligible_for:
    - flash             # tracked-actor / CVE / first-party / A&D-victim Triggers 1-5 fail; novel-attack-class disclosure without active A&D targeting is not FLASH-shaped per FLASH-POLICY
    - actor_profile_update  # no tracked actor; no actor attribution
  inclusion_rationale: >
    A2 cluster on MSTIC A-grade primary disclosing active cryptojacking
    campaign with novel AI-chatbot-poisoning methodology class. The
    AI-chatbot-poisoning layer is the intelligence-significant novel
    signal worth surfacing in AM-27 brief action tier for defender
    awareness. Per INTEL-GRADING A2 thresholds: eligible for daily-
    brief action + monitoring + weekly synthesis + IOC master index.
    NOT FLASH-eligible: no tracked actor (MSTIC explicit unknown),
    no specific CVE, no first-party hit, no A&D-prime named.

# Cluster metadata
cluster:
  topic: "MSTIC discloses active cryptojacking campaign abusing ScreenConnect + Microsoft .NET utilities + DLL sideloading via 9 autorun.dll variants - novel AI-chatbot-poisoning methodology layer alongside traditional SEO poisoning - 150+ malicious domains identified since March 2026 - parent infrastructure gleeze.com on Dynu dynamic DNS - utility brand impersonation: CrystalDiskInfo, HWMonitor, Display Driver Uninstaller (DDU), FurMark, K-Lite Codec Pack, PDFgear (targets high-performance PC enthusiast audience with discrete GPUs viable for crypto mining) - attack chain: poisoned search/chatbot result → attacker-controlled lookalike site → ZIP archive with legitimate utility + malicious autorun.dll → DLL sideload silently installs ScreenConnect → GPU mining payload via ScreenConnect persistent access → potential follow-on data theft, lateral movement, ransomware - MSTIC explicit 'unknown threat actor' attribution - no CVE - no named A&D victim - structural-supply-chain warning class for A&D-developer/engineer-population indirect exposure via high-performance PC utility downloads"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-27-am-006
  related_actors: []        # MSTIC explicit "unknown threat actor"; Hard Rule 2 holds
  related_vulnerabilities:
    - cve: null
      product_class: "Legitimate RMM (ScreenConnect) + DLL sideload via autorun.dll - no CVE in primary scope"
      mstic_referenced_separately:
        cve: CVE-2025-33073
        context: "MSTIC's post references CVE-2025-33073 in a separate F5/Atlassian unrelated case study about SEO poisoning - NOT a vulnerability in this cryptojacking campaign"
      vt_candidate: false
      rationale: "No CVE in primary scope; mechanism is DLL sideload via legitimate ScreenConnect abuse rather than vulnerability exploitation. Not vuln-tracker-eligible."
  attribution_claims:
    - claim: "Unknown threat actor responsible for cryptojacking campaign"
      claimed_by: MSTIC (Microsoft Defender Experts + Microsoft Defender Security Research Team)
      claim_confidence_language: "the threat actor / operator" (no specific cluster name, no tracked APT alias, no UNC designation)
      novelty_to_corpus: false
      requires_analyst_review: false
      hard_rule_2_status: "MSTIC explicit unknown preserved; no cross-walk to any tracked actor; Hard Rule 2 strictly holds"

# IOCs surfaced
iocs_surfaced:
  - type: domain
    value: gleeze.com
    defanged_value: gleeze[.]com
    context: "Parent malicious-campaign domain per MSTIC - subdomain-per-campaign pattern - hosted on Dynu dynamic DNS infrastructure"
    confidence: high
    source_attribution: "MSTIC Microsoft Defender Experts + Microsoft Defender Security Research Team 2026-05-26"
    defanged: false
    librarian_action_required: "Add to _master-index.yaml domain table with cryptojacking-campaign classification"
  - type: infrastructure_pattern
    value: "Dynu dynamic DNS (dynu.com) hosting"
    defanged_value: "Dynu DDNS (dynu[.]com)"
    context: "Dynamic DNS provider frequently leveraged by threat actors - gleeze.com parent domain hosted on Dynu DDNS infrastructure - 150+ malicious domains identified since March 2026"
    confidence: high
    source_attribution: "MSTIC 2026-05-26"
    defanged: false
  - type: file_pattern
    value: autorun.dll
    context: "Malicious DLL sideload payload - 9 distinct variants observed by MSTIC - resides alongside legitimate utility executable in downloaded ZIP archive - loaded by legitimate program via DLL sideloading (no exploitation, no user-visible anomaly)"
    confidence: high
    source_attribution: "MSTIC 2026-05-26"
    defanged: false
  - type: legitimate_software_abused
    value: ScreenConnect (RMM)
    context: "Legitimate remote monitoring & management software silently installed by malicious autorun.dll for persistent remote access - subsequently abused for GPU mining payload deployment and potential follow-on activity"
    confidence: high
    source_attribution: "MSTIC 2026-05-26"
    defanged: false
  - type: targeted_brand_impersonation
    value: "CrystalDiskInfo, HWMonitor, Display Driver Uninstaller (DDU), FurMark, K-Lite Codec Pack, PDFgear"
    context: "Six impersonated legitimate software brands - target-quality selection for users with high-performance discrete GPUs viable for cryptocurrency mining - A&D-prime engineering workstations (CAD / simulation / GPU-accelerated compute) overlap this target audience"
    confidence: high
    source_attribution: "MSTIC 2026-05-26"
    defanged: false
  - type: novel_methodology_class
    value: "AI chatbot recommendation poisoning - LLM-generated software download recommendations directing users to attacker-controlled domains"
    context: "Novel attack-surface class - traditional SEO poisoning extending into AI-chatbot retrieval pipelines - MSTIC observed in April 2026 with VirusTotal traffic metadata referencing chatbot interactions as referral context - emerging tradecraft layer for defender awareness across A&D-prime engineering staff using AI tools for software discovery"
    confidence: high
    source_attribution: "MSTIC 2026-05-26"
    defanged: false

ttp_keywords:
  - name: SEO poisoning (traditional search-engine-result manipulation)
    framework_mapping: MITRE T1583.008 Acquire Infrastructure - Malvertising
    context: "Manipulated search results direct users querying for legitimate utility downloads to attacker-controlled lookalike sites"
  - name: AI chatbot poisoning (novel class)
    framework_mapping: extension of T1583.008 into LLM retrieval pipelines
    context: "LLM-generated responses to software-download queries present links to attacker-controlled domains - emerging tradecraft observed by MSTIC April 2026 - VirusTotal traffic metadata showed chatbot-interaction referral context"
  - name: DLL sideloading via autorun.dll (9 variants)
    framework_mapping: MITRE T1574.002 Hijack Execution Flow - DLL Side-Loading
    context: "Legitimate utility executable loads malicious autorun.dll from same folder - no exploitation, no user-visible anomaly - 9 distinct variants observed by MSTIC"
  - name: ScreenConnect RMM abuse for persistent remote access
    framework_mapping: MITRE T1219 Remote Access Software
    context: "Silently-installed ScreenConnect provides persistent attacker access for GPU mining payload deployment and potential follow-on activity (data theft, lateral movement, ransomware)"
  - name: GPU resource hijacking for cryptocurrency mining
    framework_mapping: MITRE T1496 Resource Hijacking
    context: "Cryptocurrency mining payload deployed via ScreenConnect persistent access - target-quality-over-volume pattern selects high-performance PC enthusiast audience with discrete GPUs"

# Downstream handoff flags
analyst_review_required: true
analyst_review_topics:
  - "Novel AI-chatbot-poisoning methodology class warrants weekly-synthesis pattern surfacing alongside corpus-adjacent findings on AI-tooling abuse (Mini Shai-Hulud / Nx Console persona-attack, GTG1002 Mexico AI-assisted operations, SymJack symlink-hijack of AI coding agents). SAT-ACH candidate: competing hypotheses on AI-chatbot-poisoning trajectory. (H1) Will become standard tradecraft within 2-4 quarters as adversaries learn the channel. (H2) Will remain niche due to LLM vendor mitigations or limited operational return. (H3) Already in widespread use but underreported because telemetry visibility is sparse."
  - "A&D-prime engineering workstation indirect exposure assessment (SAT-ACH / SAT-KAC candidate): the grader's structural-warning reading rests on the load-bearing assumption that A&D-prime engineering staff use high-performance workstations for CAD/simulation/GPU-accelerated computation AND download utility software like CrystalDiskInfo/HWMonitor/DDU/FurMark from public sources. ACH hypotheses: (H1) Exposure is meaningful and warrants enterprise software-source-control policy review. (H2) A&D-prime engineering estates already enforce software-source-control sufficient to mitigate. (H3) Exposure varies by company and by specific engineering tooling vs IT-controlled estates."

analysis_sections:
  sat_ach:
    ach_analysis:
      question: "What is the most likely trajectory of AI-chatbot-recommendation poisoning as a TTP class - is it a generalizable tradecraft or a one-off MSTIC artifact?"
      analyzed_at: 2026-05-27T08:55:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: "AI-chatbot-poisoning becomes standard commodity-actor tradecraft within 2-4 quarters as adversaries observe the operational return on the gleeze.com campaign + adjacent campaigns reported by other vendors."
        - id: H2
          statement: "AI-chatbot-poisoning remains a niche technique due to LLM vendor mitigations (retrieval-source filtering, brand-impersonation detection, output-claim safety) or limited operational return per adversary-hour invested."
        - id: H3
          statement: "AI-chatbot-poisoning is already in widespread use in 2026 but underreported because LLM-vendor telemetry is closed and IR-firm visibility into chatbot-referral context is sparse - the MSTIC report surfaces an existing-but-invisible class."
        - id: H4
          statement: "Surprise hypothesis: AI-chatbot-poisoning is functionally identical to SEO poisoning (just a new retrieval channel) and gets categorized AS SEO poisoning in vendor reporting - the 'novel class' framing is artifact of naming-convention rather than tradecraft novelty."
        - id: H5
          statement: "Null hypothesis: The MSTIC observation is a one-off artifact of one campaign's specific operational choices; AI-chatbot-poisoning does not stabilize as a distinct TTP class because the LLM-retrieval-pipeline channel is too fragile (rapid LLM model updates, search-augmentation changes) for adversaries to invest in."
      evidence:
        - id: E1
          description: "MSTIC observed VirusTotal traffic metadata referencing chatbot-interactions as a referral context (April 2026)"
          source: mstic-2026-05-26
          digraph: A2
          weight: 3
        - id: E2
          description: "MSTIC explicit disclaimer that the example 'is illustrative and does not indicate a systemic issue with any specific AI service'"
          source: mstic-2026-05-26
          digraph: A1
          weight: 3
        - id: E3
          description: "Single A-grade source on the AI-chatbot-poisoning observation; no parallel A/B-grade vendor (Mandiant / Unit 42 / CrowdStrike / Cisco Talos / Sophos) has published comparable observations"
          source: corpus-silence-2026-05-27
          digraph: A1
          weight: 3
        - id: E4
          description: "150+ malicious domains since March 2026 on gleeze.com / Dynu infrastructure - operational scale suggests active adversary investment in the gleeze.com campaign specifically"
          source: mstic-2026-05-26
          digraph: A2
          weight: 3
        - id: E5
          description: "Corpus-adjacent findings on AI-tooling abuse: Mini Shai-Hulud (Nx Console / persona-attack), GTG1002 Mexico AI-assisted operations, SymJack symlink-hijack of AI coding agents, ACR Stealer fake Claude download page - the broader AI-developer-targeting tradecraft class is multi-vendor multi-campaign in 2026"
          source: archimedes-corpus-prior-findings
          digraph: A2
          weight: 3
        - id: E6
          description: "Traditional SEO poisoning is well-established tradecraft with decade+ operational history; AI-chatbot recommendation pipelines are documented to draw from SEO-poisoned search results"
          source: industry-knowledge-uncited
          digraph: C2
          weight: 1
        - id: E7
          description: "LLM vendor mitigation surface is technically tractable (retrieval-source filtering, output-claim brand-impersonation detection, sandboxed download-link warnings) but operational deployment timeline is uncertain"
          source: analyst-inference
          digraph: F
          weight: 0.5
        - id: E8
          description: "Single-source veto applied at grading layer; cluster wep_ceiling capped at 'likely' for forward-projection claims"
          source: archimedes-finding-grading
          digraph: A1
          weight: 3
      matrix:
        E1: {H1: C, H2: N, H3: C, H4: C, H5: C}
        E2: {H1: N, H2: C, H3: N, H4: C, H5: C}
        E3: {H1: I, H2: C, H3: I, H4: N, H5: C}
        E4: {H1: C, H2: N, H3: C, H4: C, H5: I}
        E5: {H1: C, H2: I, H3: C, H4: N, H5: I}
        E6: {H1: C, H2: N, H3: C, H4: C, H5: N}
        E7: {H1: N, H2: C, H3: N, H4: N, H5: N}
        E8: {H1: N, H2: N, H3: N, H4: N, H5: N}
      inconsistency_counts:
        H1: 1
        H2: 1
        H3: 1
        H4: 0
        H5: 2
      diagnostic_evidence:
        - E3: "Diagnostic against H1 and H3 (single-source absence of parallel A/B-grade vendor reporting weakens both 'becomes standard' and 'already widespread' readings) and toward H2 (consistent with 'niche, limited operational return')."
        - E5: "Diagnostic against H2 and H5 - the broader AI-developer-targeting tradecraft class is already multi-vendor multi-campaign in 2026, which weakens the 'niche' and 'one-off' readings."
        - E4: "Diagnostic against H5 (one-off) - 150+ domains since March 2026 is operational scale inconsistent with one-off framing."
      ranking:
        - rank: 1
          hypothesis_id: H4
          rationale: "Zero inconsistencies. The 'AI-chatbot-poisoning is functionally identical to SEO poisoning in a new retrieval channel' reading is defensible and arguably the most parsimonious. Note: H4 does NOT contradict the practical defender implication of H1 (the channel is real and growing); it reframes the taxonomy."
          wep: likely
        - rank: 2
          hypothesis_id: H1
          rationale: "One inconsistency (E3, no parallel vendor reporting yet). The H4-vs-H1 distinction is taxonomic - H4 says 'it's still SEO poisoning' while H1 says 'it's a distinct TTP class' but the defender posture (software-source-control, source-validation training) converges. WEP 'likely' on the practical-trajectory reading."
          wep: likely
        - rank: 3
          hypothesis_id: H3
          rationale: "One inconsistency (E3). 'Already widespread but underreported' is plausible given closed LLM-vendor telemetry but unfalsifiable on current evidence."
          wep: roughly_even_chance
        - rank: 4
          hypothesis_id: H2
          rationale: "One inconsistency (E5, broader AI-developer-targeting class is multi-vendor multi-campaign already). 'Niche' reading is increasingly hard to sustain given E5."
          wep: unlikely
        - rank: 5
          hypothesis_id: H5
          rationale: "Two inconsistencies (E4, E5). 'One-off MSTIC artifact' is contradicted by operational scale and corpus-adjacent multi-vendor evidence."
          wep: unlikely
      sensitivity_analysis:
        brittleness: low
        load_bearing_evidence: [E5, E3]
        if_second_vendor_publishes_chatbot_poisoning_observation: "E3 flips from inconsistent to consistent for H1/H3; H1 becomes clear rank-1; H2 ruled out; weekly-synthesis pattern signal strengthens"
        if_mstic_observation_not_replicated_at_T_plus_90_days: "E3 strengthens against H1; H2 strengthens; trajectory becomes 'niche or already-receded'"
        single_point_of_failure: "E5 (corpus-adjacent AI-developer-targeting findings). The trajectory assessment leans heavily on the broader corpus pattern rather than this single MSTIC observation. If E5 evidence base were re-evaluated and found weaker, H1/H3 ranking deteriorates."
      tripwires:
        - observation: "Second A/B-grade vendor (Mandiant / Unit 42 / CrowdStrike / Cisco Talos / Sophos) publishes parallel AI-chatbot-poisoning observation within 90 days"
          effect: "E3 flips; rerun ACH; H1 likely rank-1; cluster can elevate to A1"
        - observation: "LLM vendor publishes documented mitigation deployment (retrieval-source filtering, brand-impersonation detection)"
          effect: "E7 strengthens; H2 strengthens"
        - observation: "First-party defenseclaw_local hit on gleeze.com subdomain or autorun.dll variant"
          effect: "Hard Rule 8 first-party precedence; rerun finding with first-party telemetry"
        - observation: "A&D-prime engineering-workstation incident publicly tied to chatbot-recommendation lure"
          effect: "Major escalation; A&D-prime exposure no longer structural-inference but evidenced"
      conclusion:
        summary: |
          AI-chatbot-recommendation-poisoning is most likely a real and
          growing tradecraft class, but H4 (it's still functionally SEO
          poisoning in a new retrieval channel) and H1 (it becomes a distinct
          TTP class within 2-4 quarters) are operationally equivalent for
          defender posture. The single inconsistency between them is taxonomic.
          Cluster sits at "likely" on trajectory claims per single-source veto.
        wep: likely
        confidence_caveats: |
          Single-source dependence on MSTIC is the dominant limitation. ACH
          supports the grader's WEP ceiling "likely" - no upward or downward
          adjustment indicated. The corpus-adjacent AI-developer-targeting
          findings (E5) carry meaningful weight in the trajectory assessment;
          if a second vendor publishes parallel observation within 90 days, the
          cluster can elevate to A1 and the analyst recommends rerunning this
          ACH at that point.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "A&D-prime engineering workstations are indirectly exposed to the MSTIC
        cryptojacking campaign via the structural overlap between high-
        performance PC enthusiast audience (the campaign's target selection)
        and A&D-prime engineering staff using high-performance workstations
        for CAD / simulation / GPU-accelerated computation."
      analyzed_at: 2026-05-27T08:58:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication review for AM-27 morning brief; the 'this matters to our target profile' reasoning is structural-inference and the grader explicitly flagged the indirect-exposure path as KAC-candidate. Hard Rule 8 first-party silence is non-disconfirming but also non-supporting."
      assumptions:
        - id: A1
          statement: "A&D-prime engineering staff have local administrative privileges to install utility software (CrystalDiskInfo, HWMonitor, DDU, FurMark, K-Lite, PDFgear) on their workstations"
          category: capability_visibility
          stated: false
          why_must_be_true: "If users cannot install software, the lure cannot proceed past download. Indirect-exposure assessment requires user-side install capability."
          when_could_be_false: "A&D-prime engineering estates often run under managed software-deployment policies (SCCM / Intune / managed app catalogs) that restrict user-side install; CMMC Level 2/3 requirements typically push toward least-privilege"
          evidence_for: [analyst_inference_uncited]
          evidence_against: [cmmc_least_privilege_industry_pattern]
          confidence: low
          centrality: critical
          classification: test
        - id: A2
          statement: "A&D-prime engineering staff source utility software from public download sites rather than enterprise-curated software catalogs"
          category: ttp_patterns_organizational
          stated: false
          why_must_be_true: "The lure operates via public-search and AI-chatbot-recommendation channels. Indirect-exposure requires users to use those channels."
          when_could_be_false: "Mature A&D-prime estates curate software catalogs; engineering staff source from internal catalogs first. Less mature or geographically distributed estates vary."
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: critical
          classification: test
        - id: A3
          statement: "The named utility brands (CrystalDiskInfo, HWMonitor, DDU, FurMark, K-Lite, PDFgear) are actually used by A&D-prime engineering staff"
          category: semantic_actor_overlap
          stated: true
          why_must_be_true: "The exposure-path reasoning depends on brand overlap between campaign-target audience and A&D-prime engineering audience"
          when_could_be_false: "These are PC-enthusiast utilities; A&D engineering CAD/simulation workflows use different tool sets (ANSYS, CATIA, NX, MATLAB, etc.). Hardware-monitoring overlap is real but narrow."
          evidence_for: [pc_enthusiast_utility_industry_use]
          evidence_against: [a_d_engineering_tool_stack_differs_substantively]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A4
          statement: "ScreenConnect installation would not be blocked by A&D-prime EDR / managed-application policy"
          category: technology_visibility
          stated: false
          why_must_be_true: "Persistent attacker access requires successful ScreenConnect install. If EDR or app-allowlist blocks ScreenConnect, the attack chain truncates."
          when_could_be_false: "CrowdStrike / Defender for Endpoint / SentinelOne signature for ScreenConnect-in-unexpected-install-context would block; many A&D-prime estates run managed EDR with such signatures"
          evidence_for: [mstic_defensive_guidance_implies_block_path_exists]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A5
          statement: "DLL sideloading via autorun.dll is not detected by standard EDR signatures across A&D-prime estates"
          category: technology_visibility
          stated: false
          why_must_be_true: "Stealthy DLL-sideload is necessary for the silent install chain"
          when_could_be_false: "DLL-sideload-from-user-download-folder is a well-instrumented EDR detection class; many A&D-prime EDRs catch this"
          evidence_for: []
          evidence_against: [edr_dll_sideload_detection_industry_standard]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "Archimedes' Splunk visibility (defenseclaw_local + archimedes indices) is representative of A&D-prime engineering-workstation telemetry scope"
          category: visibility
          stated: false
          why_must_be_true: "Hard Rule 8 first-party precedence relies on this; zero events in Splunk would be meaningfully disconfirming only if visibility scope is representative"
          when_could_be_false: "A&D-prime engineering workstations often run on segregated networks (test cells, classified enclaves, supplier-collaboration segments) with limited Splunk visibility"
          evidence_for: []
          evidence_against: [a_d_segregated_network_industry_pattern]
          confidence: low
          centrality: material
          classification: qualify
        - id: A7
          statement: "A&D-prime engineering staff use AI chatbots (ChatGPT, Claude, Gemini, Copilot) for software-discovery queries"
          category: ttp_patterns_organizational
          stated: false
          why_must_be_true: "The novel AI-chatbot-poisoning layer of the campaign requires user-side AI-chatbot use for software discovery"
          when_could_be_false: "A&D-prime estates may restrict AI-chatbot use (Cisco / Samsung / various A&D-prime news on AI-tool policy 2024-2026), particularly for sensitive contexts"
          evidence_for: [ai_chatbot_general_workforce_adoption_2026]
          evidence_against: [a_d_prime_ai_tool_policy_restriction_pattern]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A8
          statement: "If exposure occurred, A&D-prime EDR or security operations would detect cryptocurrency-mining GPU resource consumption"
          category: visibility
          stated: false
          why_must_be_true: "The cryptojacking outcome layer is detectable via host-performance telemetry; if A&D security ops have this visibility, the post-exposure detection path exists"
          when_could_be_false: "Engineering workstations frequently run high-GPU workloads legitimately (CAD render, FEA simulation, ML model training); cryptomining signal may not stand out without specific tuning"
          evidence_for: []
          evidence_against: [legitimate_high_gpu_workload_obscures_cryptomining]
          confidence: low
          centrality: peripheral
          classification: qualify
      classifications_summary:
        sound: 0
        qualify: 6
        test: 2
        reject: 0
      remediation:
        status: proceed_with_qualifications
        blocking_assumption: null
        blocking_detail: |
          No hard-block test classification - A1 and A2 are marked test
          because their resolution would meaningfully tighten the
          assessment, but the indirect-exposure framing is already conditional
          ("structural-warning class") and the grader has appropriately held
          the A&D-prime-exposure WEP at "roughly_even_chance" in
          wep_layered. The qualifying caveats below are sufficient for
          publication as monitoring-tier content; the assessment should NOT
          be presented as action-tier without resolving A1 and A2.
        qualifying_caveats:
          - "Indirect exposure reasoning assumes engineering staff have install-privileges + use public download sites + use the specific utility brands - none of these are uniformly true across A&D-prime estates"
          - "Indirect exposure reasoning assumes EDR / managed-app policy + DLL-sideload detection + GPU-anomaly detection do NOT block at multiple chain steps - all three are detectable layers in mature estates"
          - "Archimedes Splunk visibility scope is bounded; first-party silence is non-disconfirming but also non-supporting"
          - "AI-chatbot use for software discovery varies by A&D-prime organizational policy (some restrict, some encourage)"
        next_action: "Brief at monitoring-tier with the structural-warning framing; do NOT escalate to action-tier without specific A&D-prime first-party hit or named A&D-prime victim. The brief language should preserve 'structural-warning class' framing and avoid implying confirmed A&D-prime exposure."
      recommended_wep_after_test:
        if_a1_a2_confirmed_engineering_staff_install_privileges_and_public_sourcing: "ad_prime_engineering_workstation_indirect_exposure can elevate to 'likely' for affected estates"
        if_a1_a2_confirmed_managed_software_deployment_only: "ad_prime_engineering_workstation_indirect_exposure drops to 'unlikely'; assessment becomes 'structural-warning for less-mature estates only'"
        if_a1_a2_unresolved: "ad_prime_engineering_workstation_indirect_exposure holds at 'roughly_even_chance' per current grader assessment - which the analyst confirms is appropriate"

red_team_review_required: false
red_team_review_topics_skip_rationale: >
  WEP ceiling is "likely" (single-source veto). Red-team-analyst
  doctrine triggers on WEP "very likely" or higher. Procedural
  defender-actionable artifacts (IOCs, detection guidance) reach
  very_likely individually but cluster's load-bearing forward claims
  (AI-chatbot-poisoning trajectory, A&D-prime indirect-exposure
  magnitude) sit at likely / roughly_even_chance.

# Analyst review tracking
analyst_review_complete: true
analyst_review_run_id: analyst-20260527-085500
wep_ceiling_adjusted: false
wep_ceiling_adjustment_reason: >
  ACH on AI-chatbot-poisoning trajectory confirms WEP "likely" -
  H4 (taxonomic-reframing-of-SEO-poisoning) ties with H1
  (becomes-standard-tradecraft) at zero or one inconsistency; both
  support defender posture toward this attack class. KAC on A&D-prime
  engineering-workstation indirect-exposure surfaces 2 test-class and
  6 qualify-class assumptions but no rejections; the grader's
  wep_layered "roughly_even_chance" for ad_prime_engineering_workstation_indirect_exposure
  is appropriate and the analyst confirms briefer should present at
  monitoring-tier with structural-warning framing rather than
  action-tier. No WEP adjustment needed.
brief_publication_guidance: >
  Briefer note: the AI-chatbot-poisoning layer is suitable for action-tier
  defender-awareness framing (gleeze.com / autorun.dll / ScreenConnect
  IOCs are immediately actionable). The A&D-prime indirect-exposure
  reasoning should be presented at monitoring-tier with the structural-
  warning framing - do NOT escalate to action-tier without specific
  A&D-prime first-party hit or named A&D-prime victim.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-27-morning]
retracted: false
retraction_brief_id: null
---

# MSTIC: active cryptojacking campaign abuses ScreenConnect via DLL-sideloaded autorun.dll, with novel AI-chatbot-poisoning lure layer

## Summary

Microsoft Security Blog (Microsoft Defender Experts + Microsoft Defender Security Research Team joint byline, 2026-05-26 17:35 EDT) disclosed an active cryptojacking campaign that combines traditional SEO poisoning with a **novel AI-chatbot recommendation-poisoning methodology layer**, then delivers a multi-stage payload chain: lookalike utility download → ZIP archive with legitimate utility + malicious `autorun.dll` → DLL sideload silently installs ScreenConnect → GPU mining payload via ScreenConnect persistent access. MSTIC has identified **150+ malicious domains since March 2026** on parent infrastructure `gleeze[.]com` hosted via Dynu dynamic DNS, with **9 distinct `autorun.dll` variants** observed across **6 impersonated utility brands** (CrystalDiskInfo, HWMonitor, Display Driver Uninstaller, FurMark, K-Lite Codec Pack, PDFgear) targeting high-performance PC enthusiast audiences with discrete GPUs viable for cryptocurrency mining. **Attribution: unknown threat actor** per MSTIC's explicit framing — no tracked APT alias, no UNC designation. No CVE in scope; no A&D-prime named victim. Cluster digraph A2 with single-source veto applied on forward-looking AI-chatbot-poisoning trajectory claims.

## Sources

### MSTIC — Microsoft Security Blog (mstic, A-grade)

- URL: https://www.microsoft.com/en-us/security/blog/2026/05/26/poisoned-search-results-gpu-mining-cryptojacking-campaign-abusing-screenconnect-microsoft-net-utilities/
- Published: 2026-05-26 21:35:34 UTC (17:35 EDT yesterday, in-window for AM-27 pre-brief sweep)
- Byline: Microsoft Defender Experts + Microsoft Defender Security Research Team
- Key claim: Active cryptojacking campaign with novel AI-chatbot-poisoning layer; ScreenConnect + DLL sideload chain; gleeze.com + Dynu infrastructure; 150+ malicious domains since March 2026.

### The Hacker News (thehackernews, B-grade) — relay only

- URL: https://thehackernews.com/2026/05/ai-chatbot-recommendations-redirect.html
- Published: 2026-05-27 07:45:52 UTC (03:45 EDT today)
- Byline: Ravie Lakshmanan
- Status: relay of MSTIC primary. Already evaluated at 06:00 FLASH sentinel and discarded at relay-tier (no roster / no A&D / no vuln-index hit). Surfaced here for completeness; does NOT add independent corroboration.

## Technical detail

**Attack chain** (per MSTIC):

1. **Initial access**: user searches for a system utility (e.g., `CrystalDiskInfo download`) via traditional search engine OR asks an AI chatbot for a software download recommendation
2. **Search/chatbot result poisoning**: manipulated search results and AI-generated responses direct user to attacker-controlled lookalike sites
3. **Download**: fake site presents download button claiming to provide the legitimate utility; download retrieves a ZIP archive hosted on a campaign-specific subdomain of `gleeze[.]com` (parent on Dynu dynamic DNS)
4. **DLL sideload**: ZIP contains legitimate utility executable alongside malicious `autorun.dll`; user launches legitimate program; program loads `autorun.dll` from same folder via DLL sideloading (no exploitation, no user-visible anomaly); **9 distinct `autorun.dll` variants observed across the campaign**
5. **Silent ScreenConnect install**: malicious DLL silently installs ScreenConnect (legitimate RMM software being abused) for persistent remote access
6. **Cryptocurrency mining**: GPU mining payload deployed via ScreenConnect persistent access
7. **Potential follow-on**: ScreenConnect persistence "could later support data theft, lateral movement, or ransomware activity" per MSTIC (speculative — not yet observed in MSTIC telemetry)

**AI chatbot poisoning methodology** (novel layer):

Per MSTIC's research: in April 2026, Microsoft observed reports indicating users may have been directed to malicious domains through interactions with large-language-model (LLM)-based tools. Users querying AI chatbots for software download recommendations were presented with links to attacker-controlled domains within generated responses. Analysis of VirusTotal scan associated with these domains identified traffic metadata referencing chatbot interactions as a potential referral context. MSTIC characterizes the behavior as consistent with emerging techniques in AI search result poisoning — an extension of traditional SEO poisoning beyond conventional search engines.

**MSTIC explicitly disclaims** any systemic attribution to specific LLM vendor product flaws: their example "is illustrative and does not indicate a systemic issue with any specific AI service." The mechanism is the broader ecosystem-level SEO-poisoning surface being absorbed into AI-chatbot training data and retrieval pipelines.

**Target selection** (utility brand impersonation):

The campaign deliberately curates target audience for users likely to own high-performance discrete GPUs — the hardware that makes GPU cryptocurrency mining economically viable. Impersonated brands:
- CrystalDiskInfo
- HWMonitor
- Display Driver Uninstaller (DDU)
- FurMark
- K-Lite Codec Pack
- PDFgear

This is a **target-quality-over-target-volume** operational pattern. A&D-prime engineering workstations used for CAD, simulation, and GPU-accelerated computation overlap this target audience.

## Attribution — explicit "unknown threat actor"

**MSTIC does NOT attribute the campaign to any named tracked actor.** Framing throughout: "the threat actor" / "operator" — not a specific cluster name, not a tracked APT alias, not a UNC designation. Per Hard Rule 2, Archimedes records MSTIC's explicit "unknown" attribution and does NOT cross-walk to any tracked actor.

## A&D / aerospace / defense framing

- **Named A&D victim**: NONE
- **Named A&D sector**: NONE
- **Structural-supply-chain warning class** for A&D-developer/engineer-population indirect exposure: A&D-prime engineering staff using high-performance workstations for CAD/simulation/GPU-accelerated computation overlap the targeted PC-enthusiast audience. Any A&D-prime engineering laptop or workstation download of one of the named utilities (CrystalDiskInfo, HWMonitor, DDU, FurMark, K-Lite, PDFgear) during the campaign window had contemporaneous exposure to this attack chain.
- Per Hard Rule 2, Archimedes does NOT extrapolate from "PC-enthusiast audience" to "specific A&D-prime exposure" — the extrapolation is structural-warning class only.

## IOCs surfaced

See `iocs_surfaced` frontmatter block. Defender-actionable summary:
- **Parent domain**: `gleeze[.]com` with subdomain-per-campaign pattern
- **Infrastructure**: Dynu dynamic DNS (`dynu[.]com`)
- **File pattern**: `autorun.dll` (9 distinct variants)
- **Abused legitimate software**: ScreenConnect (RMM)
- **Brand impersonations**: 6 utility brands listed above
- **Aggregate scope**: 150+ malicious domains since March 2026

Specific `gleeze.com` subdomains, `autorun.dll` hash values, and additional IOC strings would require direct retrieval from MSTIC's full IOC appendix.

## Microsoft's defensive guidance (per MSTIC)

- Enable cloud-delivered protection
- Run EDR in block mode
- Enable attack surface reduction (ASR) rules

## Relationship to existing findings

This finding sits within a growing corpus thread on **AI-tooling abuse and AI-developer/engineer-population targeting**:
- finding-2026-05-19-0002 Nx Console / Claude Code / 1Password persona-attack (AI-developer extension marketplace)
- finding-2026-05-26-0002 Check Point AI threat landscape digest (GTG1002 Mexico, AI-assisted operations)
- finding-2026-05-26-0006 SANS ISC ACR Stealer fake Claude download page (AI-developer download impersonation)
- finding-2026-05-26-0007 UNC1549 Nimbus Manticore (AI-assisted malware development indicators)
- finding-2026-05-27-0003 SymJack symlink-hijack of AI coding agents (sibling finding this run)

The AI-chatbot-poisoning layer is **novel-to-corpus** as a specific methodology class. Weekly-synthesis pattern surfacing recommended.

## Open questions for analyst

1. **AI-chatbot-poisoning trajectory** (SAT-ACH candidate): competing hypotheses on whether AI-chatbot-poisoning becomes standard tradecraft within 2-4 quarters (H1), remains niche due to LLM vendor mitigations or limited operational return (H2), or is already in widespread use but underreported (H3). Load-bearing evidence required: second A/B-grade vendor independent observation of AI-chatbot-poisoning in another campaign.
2. **A&D-prime engineering workstation exposure** (SAT-ACH/SAT-KAC candidate): the structural-warning reading rests on the load-bearing assumption that A&D-prime engineering staff use high-performance workstations AND download utility software from public sources. Hypothesis competition: (H1) exposure is meaningful, warrants policy review; (H2) A&D-prime engineering estates already enforce software-source-control sufficiently; (H3) exposure varies by company-specific engineering tooling vs IT-controlled estates.
3. **Cross-corroboration watch**: track whether Mandiant / Unit 42 / CrowdStrike / Cisco Talos / Sophos publish parallel telemetry on the same `gleeze.com` campaign within 30 days. If so, cluster can elevate to A1.

## Analytic notes (from analyst review)

SAT-ACH on the AI-chatbot-poisoning trajectory question surfaced five hypotheses; H4 (the technique is functionally identical to SEO poisoning in a new retrieval channel) ranked first with zero inconsistencies and H1 (becomes standard commodity-actor tradecraft within 2-4 quarters) ranked second with one inconsistency (no parallel A/B-grade vendor reporting yet). H4 and H1 are operationally equivalent for defender posture - the distinction is taxonomic. The corpus-adjacent AI-developer-targeting findings (Mini Shai-Hulud, GTG1002, SymJack, ACR Stealer fake Claude page) carry meaningful weight against the "niche" and "one-off" alternatives. Trajectory WEP holds at "likely" per single-source veto.

SAT-KAC on the A&D-prime engineering-workstation indirect-exposure path surfaced 8 assumptions: 2 test (A1 - install privileges; A2 - public-download-site sourcing), 6 qualify, 0 reject. The grader's roughly-even-chance reading for indirect-exposure is appropriate; the analyst confirms the briefer should present this layer at monitoring-tier with structural-warning framing, NOT action-tier. The defender-actionable IOC layer (gleeze.com, autorun.dll variants, ScreenConnect lure pattern) is independently action-tier-eligible. Briefer guidance: separate these two layers explicitly in the brief - IOC-action-tier for the campaign artifacts; structural-warning-monitoring-tier for the A&D-prime indirect-exposure framing.

## Hard Rule compliance

- **Hard Rule 2**: MSTIC explicit "unknown threat actor" attribution preserved; no cross-walk to any tracked actor. ACH did not originate alternative attribution.
- **Hard Rule 3**: Attack chain described at defender-actionable level; no working `autorun.dll` variant code reproduced; no ScreenConnect payload reproduced; no `gleeze.com` subdomain enumeration provided.
- **Hard Rule 6**: MSTIC framing paraphrased throughout; no direct quotes >15 words.
- **Hard Rule 8**: Splunk first-party check executed; zero events; silence not disconfirming. KAC A6 explicitly flags Splunk visibility scope as a load-bearing assumption.
