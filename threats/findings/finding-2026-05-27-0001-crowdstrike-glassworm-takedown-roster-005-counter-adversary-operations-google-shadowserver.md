---
finding_id: finding-2026-05-27-0001-crowdstrike-glassworm-takedown-roster-005-counter-adversary-operations-google-shadowserver
created_at: 2026-05-27T08:14:00-04:00
graded_by: grader
grading_run_id: morning-20260527-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: A2
digraph_layered:
  crowdstrike_counter_adversary_takedown_disclosure: A2
  four_channel_c2_architecture_solana_dht_calendar_vps: A2
  multi_partner_coordination_google_shadowserver: A2
  sinkhole_ip_164_92_88_210_crowdstrike_operated: A1
  yara_rule_crowdstrike_glasswormrat_01: A1
  yara_rule_crowdstrike_glasswormdownloader_01: A1
  glasswormrat_nodejs_rat_classification: A2
  campaign_duration_since_at_least_early_2025: A2
  developer_population_targeting_general: A2
  vscode_openvsx_npm_pypi_github_300_repos_attack_vectors: A2
  russia_origin_likely_attribution_pattern_based: A3   # Hard Rule 2; "likely based in Russia" preserved per CrowdStrike verbatim
  cis_locale_geofencing_indicator: A2
  russian_language_comments_in_code: A3                # Per CrowdStrike's own caveat: comments may reflect AI tooling
  securityweek_relay_not_independent_corroboration: A1
  no_ad_prime_victim_named: A1
  no_cve_assigned: A1
  cluster_anchor: A2

digraph_anchor: >
  Cluster digraph A2 anchored on CrowdStrike Counter Adversary
  Operations primary publication (2026-05-26 ~14:00 UTC) disclosing a
  coordinated multi-partner takedown of GlassWorm botnet (Archimedes
  tracked actor roster #005, HIGH threat level). CrowdStrike is A-grade
  per source-grades.yaml. SecurityWeek (Ionut Arghire 2026-05-27 06:10
  EDT) is a B-grade media relay of the CrowdStrike primary - same shape
  as BleepingComputer summarizing Mandiant per INTEL-GRADING.md
  independence test - NOT independent corroboration. The cluster has
  ONE effective source on the takedown disclosure layer; single-source
  veto applies on forward-looking WEP claims about GlassWorm
  operational dormancy. Procedural facts (YARA rules, sinkhole IP,
  campaign vectors, four-channel C2 architecture description) reach A1
  procedurally as CrowdStrike-published artifacts but the cluster
  digraph follows the weakest-link operational claim per INTEL-GRADING.
  Russia-origin attribution is A3 (single-source pattern-based
  assessment with CrowdStrike's own caveat "no single indicator is
  proof on its own"); Archimedes preserves "likely based in Russia"
  verbatim per Hard Rule 2 and does NOT upgrade _roster.yaml #005 to
  confirmed RU attribution.

source_reliability:
  grade: A
  source_name: "CrowdStrike Counter Adversary Operations"
  source_yaml_id: crowdstrike
  grade_rationale: >
    Pre-assigned A per source-grades.yaml. CrowdStrike Counter
    Adversary Operations team byline (no individual analyst named) is
    the consistent CrowdStrike publication convention for
    coordinated-takedown post-mortems and is operationally equivalent
    in source-grade to bylined CrowdStrike Intelligence research. The
    Counter Adversary Operations blog post anchors the in-window event
    (takedown coordinated 2026-05-26 14:00 UTC).
  provisional: false
  pre_window_relay:
    source_yaml_id: securityweek
    source_grade: B
    publication: "GlassWorm Botnet Disrupted"
    publication_date: 2026-05-27T10:10:00Z
    contribution: >
      B-grade media relay of the CrowdStrike primary publication.
      Confirms takedown date and partner set, four-channel C2
      architecture description, and "likely Russia" framing. Does NOT
      add independent telemetry or original IOCs.

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_ttps_or_known_campaign_timing_targeting
    - probably_true_no_contradicting_evidence_from_ab_grade_sources
    - probably_true_technical_claims_internally_coherent
  grade_1_test:
    - independent_corroboration_present_no: "SecurityWeek is a pure relay of CrowdStrike; not independent. No second A/B-grade IR firm has published parallel telemetry."
    - grade_1_blocked_by: "Single-source A-grade vendor on the takedown-disclosure claim. Procedural artifacts (YARA, sinkhole IP) are individually A1 but cluster anchor follows the weakest-link operational claim."
  rationale: >
    GlassWorm is corpus-anchored as roster #005 HIGH since 2026-04-02;
    CrowdStrike's takedown disclosure is consistent with the established
    actor profile (developer-population targeting, supply-chain
    propagation via VSCode/OpenVSX/npm/PyPI/GitHub). The novel
    four-channel C2 architecture (Solana blockchain dead-drop +
    BitTorrent DHT + Google Calendar event titles + commercial VPS) is
    internally coherent with the supply-chain-attack tradecraft layer
    GlassWorm has demonstrated. CrowdStrike's "likely based in Russia"
    attribution language is preserved verbatim per Hard Rule 2; CIS
    locale geofencing + Russian-language code comments are
    pattern-consistent but CrowdStrike's own caveat ("no single
    indicator is proof on its own"; code comments may reflect AI
    tooling) is preserved.

corroboration:
  independent_sources:
    - crowdstrike
  independent: false
  test_passed_no: >
    SecurityWeek is a media relay of the CrowdStrike primary - NOT
    independent corroboration per INTEL-GRADING.md independence test
    (a relay of source X is not corroboration of X). The Shadowserver
    Foundation and Google were operational partners in the takedown,
    not independent research sources publishing parallel telemetry.
    Cluster has ONE effective source for the takedown disclosure.
  pm_27_corroboration_field_amendment:
    amended_at: 2026-05-27T16:25:00-04:00
    amended_by: grader
    amended_in_run: afternoon-20260527-160000
    triggering_raw_signal: raw-2026-05-27-pm-005
    triggering_rejection_id: reject-2026-05-27-0003
    amendment_type: attribution_enrichment_within_existing_finding
    additional_relay_layers_now_on_file:
      - bleepingcomputer (Ilascu 2026-05-27 09:28 EDT)        # also relay of CrowdStrike primary; not independent
      - thehackernews (2026-05-27 11:48 EDT)                  # also relay of CrowdStrike primary; not independent
      - the-register (2026-05-27 13:56 EDT)                   # fourth relay; PM-005 triggering surface; not independent
    independence_test_amended_status: >
      Four media relays now on file (SW + BC + THN + Register) all
      derived from the same CrowdStrike Counter Adversary Operations
      primary. Independence test STILL FAILS — four relays of the same
      primary do NOT constitute independent corroboration per INTEL-
      GRADING.md. Cluster anchor remains A2 with single-source veto on
      forward-looking WEP claims. Hultquist GTIG named-byline social-
      media confirmation is operational-partnership confirmation, not
      parallel-telemetry research evidence basis.
    new_indicators_surfaced_via_register_relay:
      - indicator: "CIS-locale termination check"
        description: "Malware terminates execution on Commonwealth of Independent States systems (RU, BY, KZ, etc.). Well-documented Russian-cybercrime operational artifact (Conti, TrickBot, IcedID, Babuk, Sandworm-toolkit precedent)."
        confidence: A (vendor-research-attested via CrowdStrike per The Register relay)
        novel_to_corpus_surface_for_glassworm: true
        attribution_strengthening_layer: "Russian-origin attribution prong"
      - indicator: "Russian-language code comments in malware source"
        description: "Higher-confidence Russian-language operational artifact than CIS-skip logic (CIS-skip is widely emulated by non-Russian actors)."
        confidence: A
        novel_to_corpus_surface_for_glassworm: true
        crowdstrike_own_caveat_preserved: "Code comments may reflect AI-tooling output rather than human authorship; no single indicator is proof on its own"
      - indicator: "John Hultquist (Google Threat Intelligence Group chief analyst) confirms GTIG role via social media"
        description: "First byline-credit surface for GTIG partnership in this event. Operational confirmation of partnership, NOT independent parallel-telemetry research evidence."
        confidence: A
      - indicator: "300+ GitHub repositories confirmed compromised"
        description: "CrowdStrike takedown-surface count. Distinct from prior Koi 400+ figure (Oct 2025 discovery). The Register relay does not disambiguate — may be subset (300 actively poisoned via takedown evidence; 400 historically touched) or separate tracking."
        confidence: A
        novelty: "specific victim count from CrowdStrike takedown surface vs prior Koi 400+ historical reach figure"
      - indicator: "GlasswormRAT (Node.js remote access tool) named"
        description: "Tool-attribution detail matching CrowdStrike YARA rule CrowdStrike_GlasswormRat_01 published with this finding's IOC set."
        confidence: A
      - indicator: "Koi (October 2025 originating discovery) named as endpoint-security shop"
        description: "Source-grades.yaml first-citation candidate flagged for librarian. Provisional F per cheatsheet for unknown research vendor with no prior corpus citation. Hold at F pending Koi-independent-research surface that is not derived from CrowdStrike chain."
        confidence: A
    mini_shai_hulud_parallel_editorial_mention_disposition: >
      The Register editorial framing notes "another self-replicating
      worm, Mini Shai-Hulud, rips through open source code" in parallel
      to GlassWorm. This is EDITORIAL FRAMING by The Register, NOT a
      Gambit / Mandiant / CrowdStrike attribution claim. Per Hard Rule
      2, NO cross-walk from GlassWorm (#005) to TeamPCP / Mini Shai-
      Hulud (VT-006) despite the parallel-mention framing. The two
      cluster surfaces remain distinct corpus-tracked threads.
    glassworm_005_roster_attribution_operator_decision_flagged: >
      Operator decision flagged for /update-tracking workflow:
      GlassWorm (#005) roster attribution field update from
      `nation: unknown / service: null` to `nation: RU (likely, per
      CrowdStrike 2026-05-26 Counter Adversary Operations)` with
      CrowdStrike's own caveat preserved verbatim per Hard Rule 2.
      This is NOT a collector-side or grader-side action — flow through
      formal /update-tracking workflow or human ratification per
      CLAUDE.md Rule 5 + Hard Rule 2.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    Splunk query against defenseclaw_local + archimedes over -24h
    covering "GlassWorm", "GlasswormRAT", "164.92.88.210" (sinkhole
    IP). Zero events. Hard Rule 8: silence is not disconfirming.
    Sinkhole IP is benign post-takedown - any defenseclaw_local hit
    would be a SOC false-positive concern, not malicious traffic.

single_source_veto_applied: true
single_source_veto_rationale: >
  Per INTEL-GRADING.md, A-grade single-source claims cap at WEP
  "likely" until independent corroboration arrives. SecurityWeek
  relays CrowdStrike; relays are not corroboration. The takedown is
  factually disclosed by CrowdStrike but forward-looking claims
  ("GlassWorm operationally neutralized", "Russia-origin confirmed")
  carry single-source-veto.

wep_ceiling: likely
wep_layered:
  takedown_event_occurred_2026_05_26: very_likely        # CrowdStrike claims, partners (Google + Shadowserver) implicit confirmation
  four_channel_c2_architecture_existed: likely           # A2 description
  glassworm_operationally_dormant_post_takedown: likely  # A2 + single-source veto; attackers commonly rebuild infrastructure
  russia_origin_likely_pattern_based: likely             # CrowdStrike's own qualifier; Hard Rule 2 preserves verbatim
  cis_locale_geofencing_present: very_likely             # technical artifact, CrowdStrike-observed
  developer_population_targeting_continued: very_likely  # corpus-anchored tradecraft
  supply_chain_propagation_via_openvsx_npm_pypi_github_300_repos: very_likely  # corpus-anchored

inclusion:
  eligible_for:
    - daily_brief_action
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update                # roster #005 attribution + TTP update
    - ioc_master_index_propagation        # YARA rules + sinkhole IP
  not_eligible_for:
    - flash             # tracked-actor STATE CHANGE class, not Trigger 2 (TTP change) or Trigger 1 (CVE); not FLASH-shaped per FLASH-POLICY
  inclusion_rationale: >
    A2 cluster on tracked actor #005 GlassWorm (HIGH threat level)
    operational disruption by A-grade vendor. Per INTEL-GRADING
    thresholds, A2 is brief-action-eligible AND actor-profile-update-
    eligible. The takedown is intelligence-significant for two reasons
    distinct from FLASH-shape: (1) actor-profile update on #005
    (attribution toward Russia, four-channel C2 architecture details,
    300+ poisoned GitHub repo scope), and (2) defender-awareness on
    YARA rule availability + sinkhole IP for SOC noise-filtering.

# Cluster metadata
cluster:
  topic: "CrowdStrike Counter Adversary Operations + Google + Shadowserver coordinated takedown of GlassWorm (roster #005 HIGH) - four-channel C2 architecture (Solana blockchain dead-drop, BitTorrent DHT, Google Calendar event titles, commercial VPS) simultaneously disrupted 2026-05-26 14:00 UTC - infected machines redirected to CrowdStrike-operated benign sinkhole 164.92.88.210 - 300+ poisoned GitHub repositories via stolen credentials - VSCode/OpenVSX/npm/PyPI as supply-chain propagation vectors - GlasswormRAT (Node.js RAT) + GlasswormDownloader (<10KB) families with CrowdStrike-published YARA rules - 'likely based in Russia' per CrowdStrike pattern-based attribution (CIS locale geofencing + Russian-language code comments; CrowdStrike's own caveat preserved) - Hard Rule 2 preserves verbatim attribution language and does NOT upgrade roster #005 to confirmed RU"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-27-am-001
  related_actors:
    - actor_id: "005"
      actor_name: "GlassWorm"
      threat_level_at_finding: HIGH
      attribution_change_proposed:
        current_roster_state: "nation: unknown, service: null"
        proposed_state: "nation: RU (likely, per CrowdStrike 2026-05-26)"
        confidence_language_preserved: "the criminals are likely based in Russia"
        hard_rule_2_compliance: "Archimedes records CrowdStrike's pattern-based assessment verbatim and does NOT upgrade to confirmed RU; actor-profiler decides whether to update roster nation field to 'RU (likely, per CrowdStrike 2026-05-26 Counter Adversary Operations)' or hold at 'unknown' pending second A/B-grade IR-firm corroboration"
      ttp_update_proposed:
        novel_to_roster_005_profile:
          - "Four-channel C2 architecture: Solana blockchain dead-drop (memo fields), BitTorrent DHT (public-key keyed config retrieval), Google Calendar event titles (Base64 dead-drop), commercial VPS direct C2"
          - "Scope clarification: 300+ poisoned GitHub repositories via stolen credentials; VSCode/Cursor/Positron/Windsurf/VSCodium platform spread"
          - "Operational neutralization 2026-05-26 14:00 UTC via multi-partner CrowdStrike + Google + Shadowserver takedown"
  related_vulnerabilities: []
  attribution_claims:
    - claim: "GlassWorm operators likely based in Russia"
      claimed_by: CrowdStrike Counter Adversary Operations
      claim_confidence_language: "likely based in Russia" (pattern-based, with vendor's own caveat that no single indicator is proof on its own)
      claim_evidence_basis:
        - "Runtime locale + timezone checks; malware exits if victim is in CIS country"
        - "Russian-language comments throughout source code (with CrowdStrike caveat: comments may reflect AI tooling rather than human authorship)"
      novelty_to_corpus: true   # roster #005 attribution is currently "nation: unknown"; this is first A-grade attribution toward RU origin
      requires_analyst_review: true
      hard_rule_2_status: "preserved verbatim; not upgraded"

# IOCs surfaced
iocs_surfaced:
  - type: ipv4
    value: 164.92.88.210
    context: "CrowdStrike-operated benign sinkhole - infected machines redirected here post-takedown - defender SOC should treat this IP as benign-known-traffic if observed in egress"
    confidence: high
    source_attribution: "CrowdStrike Counter Adversary Operations 2026-05-26"
    defanged: false
    librarian_action_required: "Add to _master-index.yaml IOC index with 'benign-sinkhole' classification"
  - type: yara_rule
    value: CrowdStrike_GlasswormRat_01
    context: "Detects GlasswormRAT - patterns include DownloadManager, start_socks, nodejs.org, bootstrap strings"
    confidence: high
    source_attribution: "CrowdStrike Counter Adversary Operations 2026-05-26"
    defanged: false
  - type: yara_rule
    value: CrowdStrike_GlasswormDownloader_01
    context: "Detects GlasswormDownloader (<10KB downloader component) - patterns include zlib, decompress, lambda, exec"
    confidence: high
    source_attribution: "CrowdStrike Counter Adversary Operations 2026-05-26"
    defanged: false
  - type: c2_channel_pattern
    value: "Solana blockchain memo-field dead-drop / BitTorrent DHT public-key keyed config / Google Calendar event-title Base64 dead-drop / commercial VPS"
    context: "Four-channel parallel C2 architecture - decentralized resilience pattern reusable by other actors even after GlassWorm disruption"
    confidence: high
    source_attribution: "CrowdStrike Counter Adversary Operations 2026-05-26"
    defanged: false

ttp_keywords:
  - name: Supply-chain compromise via trojanized VSCode extensions (OpenVSX marketplace)
    framework_mapping: MITRE T1195.002 Supply Chain Compromise - Compromise Software Supply Chain
    context: "GlassWorm distributed via OpenVSX (open VSCode marketplace); platforms targeted include VSCode, Cursor, Positron, Windsurf, VSCodium"
  - name: Supply-chain compromise via npm + PyPI package compromise
    framework_mapping: MITRE T1195.002 Supply Chain Compromise
    context: "Compromised npm and Python packages as parallel distribution vector"
  - name: Supply-chain compromise via GitHub repository poisoning with stolen credentials
    framework_mapping: MITRE T1195.002 Supply Chain Compromise
    context: "300+ poisoned GitHub repositories using stolen developer credentials"
  - name: Blockchain-based dead-drop C2 (Solana memo fields)
    framework_mapping: MITRE T1102 Web Service (Dead Drop Resolver class)
    context: "C2 addresses encoded in memo fields of Solana blockchain transactions - immutable publicly-accessible dead-drop"
  - name: Decentralized peer-to-peer DHT-based C2 (BitTorrent DHT)
    framework_mapping: MITRE T1090.003 Proxy - Multi-hop Proxy / T1102 Web Service
    context: "GlasswormRAT queries BitTorrent DHT for configuration data stored against hardcoded public keys"
  - name: Cloud-service abuse for C2 (Google Calendar event titles as Base64 dead-drop)
    framework_mapping: MITRE T1102.002 Web Service - Bidirectional Communication
    context: "Google Calendar event titles used as dead-drop locations for Base64-encoded C2 paths"

# Downstream handoff flags
analyst_review_required: true
analyst_review_topics:
  - "Roster #005 attribution change proposal: actor-profiler decides whether to update _roster.yaml nation field from 'unknown' to 'RU (likely, per CrowdStrike 2026-05-26)' or hold pending second A/B-grade IR-firm corroboration. Hard Rule 2 requires the qualifier be preserved verbatim."
  - "TTP update on #005 dossier: four-channel C2 architecture is novel-to-corpus for this actor and represents a reusable architectural pattern beyond just GlassWorm. Actor-profiler should evaluate whether to add ATT&CK technique mappings (T1102, T1195.002, T1090.003) to #005's profile."
  - "SAT-ACH candidate: competing hypotheses on GlassWorm operational disposition post-takedown. (H1) GlassWorm operators reconstitute infrastructure within weeks using same architectural patterns. (H2) Operators pivot to a different actor/branding to evade detection. (H3) The takedown materially degrades GlassWorm operations through end of Q2 2026. Load-bearing assumption: CrowdStrike + Google + Shadowserver coordination is sufficient to disrupt all four C2 channels durably."

analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Is CrowdStrike's 'likely based in Russia' attribution for GlassWorm operators (roster #005) supported by the cited evidence against alternative explanations?"
      analyzed_at: 2026-05-27T08:42:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: "GlassWorm operators are Russian-based criminals (the sourced hypothesis - CrowdStrike's framing)."
        - id: H2
          statement: "GlassWorm operators are CIS-region (non-Russian) Russian-speaking criminals - e.g., Belarus, Ukraine pre-war diaspora, Kazakhstan. CIS-locale geofencing fits this superset; CrowdStrike's 'Russia' label may be over-precise."
        - id: H3
          statement: "Null hypothesis: GlassWorm is a multi-nationality criminal collective; geofencing + Russian comments reflect tooling and OPSEC choices rather than operator nationality."
        - id: H4
          statement: "Surprise hypothesis: GlassWorm operators are non-Russian criminals using Russian-language comments + CIS geofencing as deliberate misdirection (false-flag posture). Code comments per CrowdStrike's own caveat may reflect AI-tooling output rather than human authorship."
        - id: H5
          statement: "Composite hypothesis: A core Russian-speaking developer team + non-Russian operators / affiliates (typical of mature commodity-actor ecosystems). Code-base nationality and operational-tempo nationality differ."
      evidence:
        - id: E1
          description: "CIS-locale runtime geofencing - malware exits if victim is in CIS country"
          source: crowdstrike-counter-adversary-operations-2026-05-26
          digraph: A2
          weight: 3
        - id: E2
          description: "Russian-language comments throughout source code (CrowdStrike's own caveat: may reflect AI-tooling output)"
          source: crowdstrike-counter-adversary-operations-2026-05-26
          digraph: A3
          weight: 1
        - id: E3
          description: "CrowdStrike's own framing 'no single indicator is proof on its own'"
          source: crowdstrike-counter-adversary-operations-2026-05-26
          digraph: A1
          weight: 3
        - id: E4
          description: "Four-channel C2 architecture (Solana / BitTorrent DHT / Google Calendar / commercial VPS) suggests resource-rich, technically sophisticated developer team"
          source: crowdstrike-counter-adversary-operations-2026-05-26
          digraph: A2
          weight: 3
        - id: E5
          description: "Developer-population targeting (npm/PyPI/VSCode/OpenVSX) is supply-chain-criminal pattern - not geopolitically aligned with any specific nation's targeting priorities"
          source: crowdstrike-counter-adversary-operations-2026-05-26
          digraph: A2
          weight: 3
        - id: E6
          description: "No second A/B-grade IR firm has corroborated the Russia attribution (Mandiant / MSTIC / Unit 42 / Recorded Future / Volexity / Cisco Talos silent on this attribution)"
          source: corpus-silence-2026-05-27
          digraph: A1
          weight: 3
        - id: E7
          description: "No A&D-prime victim named; no government / espionage targeting pattern visible"
          source: crowdstrike-counter-adversary-operations-2026-05-26
          digraph: A1
          weight: 3
      matrix:
        E1: {H1: C, H2: C, H3: N, H4: C, H5: C}
        E2: {H1: C, H2: C, H3: N, H4: C, H5: C}
        E3: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E4: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E5: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E6: {H1: I, H2: N, H3: N, H4: N, H5: N}
        E7: {H1: C, H2: C, H3: C, H4: C, H5: C}
      inconsistency_counts:
        H1: 1
        H2: 0
        H3: 0
        H4: 0
        H5: 0
      diagnostic_evidence:
        - none: "The matrix is largely non-diagnostic. E1 (CIS geofencing) and E2 (Russian comments) are equally consistent with H1, H2, H4, and H5 - they cannot distinguish 'Russian operator' from 'CIS-speaking operator' from 'false-flag actor mimicking either' from 'Russian-developer-team-with-non-Russian-affiliates'."
        - E6: "Mildly diagnostic against H1 in the sense that single-source attribution claims for a tracked actor without parallel A/B-grade corroboration are normally suspect; but does not actively support any alternative."
      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: "Strictly the most defensible: CIS Russian-speaking criminal superset fits all observed evidence and is over-specified by the 'Russia' label. Zero inconsistencies. Note: NOT a license to originate this attribution per Hard Rule 2 - this ranking pressure-tests H1, it does not replace it."
          wep: roughly_even_chance
        - rank: 2
          hypothesis_id: H1
          rationale: "CrowdStrike's sourced hypothesis. Consistent with all positive evidence; the single inconsistency is non-corroboration. Cannot be elevated above 'likely' per single-source veto already applied in grading."
          wep: likely
        - rank: 3
          hypothesis_id: H5
          rationale: "Composite (Russian devs + multinational affiliates) is plausible for a mature commodity-actor ecosystem but adds unverified entities. Zero inconsistencies but requires unsupported sub-assumptions."
          wep: roughly_even_chance
        - rank: 4
          hypothesis_id: H4
          rationale: "False-flag is technically uncontradicted but requires unverified motive and capability; CrowdStrike's AI-tooling caveat keeps it live but unsupported."
          wep: unlikely
        - rank: 5
          hypothesis_id: H3
          rationale: "Null hypothesis - sustainable as a framing but not affirmatively supported by anything."
          wep: unlikely
      sensitivity_analysis:
        brittleness: high
        load_bearing_evidence: [E1, E2]
        if_E2_reinterpreted_as_AI_tooling: "Removes the language-attribution leg entirely; H1 collapses to H2/H3 superset; Russia-specific claim becomes unsupported"
        if_crowdstrike_attribution_methodology_downgraded: "All four hypotheses collapse toward H3 (null); roster #005 should remain nation: unknown"
        single_point_of_failure: "E2 (Russian-language comments). CrowdStrike's own caveat that this may be AI-tooling output is itself a published-by-the-source brittleness flag."
      tripwires:
        - observation: "Second A/B-grade IR firm publishes parallel GlassWorm Russia attribution with independent telemetry"
          effect: "Elevate E6 from inconsistent to neutral; H1 strengthens; clears single-source veto"
        - observation: "Reconstituted GlassWorm infrastructure observed in non-CIS region (e.g., LatAm, SEA hosting)"
          effect: "Supports H2/H5 (CIS-superset or multi-nationality affiliates)"
        - observation: "Law-enforcement arrests or indictment naming specific nationality"
          effect: "Definitive resolution; rerun ACH"
        - observation: "Russian-language artifact analysis by independent linguist confirms native-speaker idiom (vs AI-generated translation)"
          effect: "Strengthens E2; supports H1"
      conclusion:
        summary: |
          The matrix is largely non-diagnostic - E1 (CIS geofencing) and E2
          (Russian-language code comments) are consistent with all attribution
          hypotheses including the H2 CIS-Russian-speaking-criminal superset.
          H1 (CrowdStrike's 'likely Russia' framing) cannot be elevated above
          'likely' per single-source veto and is strictly over-specified relative
          to the evidence presented. The assessment is high-brittleness to
          re-interpretation of E2 (which CrowdStrike's own caveat already flags
          as potentially AI-tooling-derived).
        wep: likely
        confidence_caveats: |
          Per Hard Rule 2, analyst does NOT originate the H2 CIS-superset
          attribution. The ACH pressure-tests CrowdStrike's sourced H1 framing
          and confirms it should be preserved verbatim with the qualifier
          'likely' rather than upgraded. Actor-profiler should hold roster #005
          attribution at 'unknown' OR update to 'RU (likely, per CrowdStrike
          2026-05-26)' with the full verbatim qualifier including CrowdStrike's
          own caveat. The non-diagnostic matrix supports the grader's
          single-source veto and supports holding the WEP at 'likely' rather
          than elevating.

red_team_review_required: false
red_team_review_topics_skip_rationale: >
  WEP ceiling is "likely" (single-source veto applied). Red-team-
  analyst doctrine triggers on WEP "very likely" or higher. The
  procedural facts (YARA rules, sinkhole IP, takedown event) reach
  very_likely individually but the load-bearing forward claims
  ("GlassWorm operationally neutralized through Q2") sit at likely.

# Analyst review tracking
analyst_review_complete: true
analyst_review_run_id: analyst-20260527-084200
wep_ceiling_adjusted: false
wep_ceiling_adjustment_reason: >
  ACH confirms grader's WEP ceiling "likely" is appropriate. The matrix
  is non-diagnostic across attribution hypotheses, which independently
  supports the single-source veto already applied. No downward
  adjustment needed; WEP is correctly capped. No upward adjustment
  available without independent A/B-grade IR-firm corroboration.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-27-morning, 2026-05-27-afternoon]
retracted: false
retraction_brief_id: null
---

# CrowdStrike Counter Adversary Operations takes down GlassWorm botnet in coordinated multi-partner operation

## Summary

CrowdStrike's Counter Adversary Operations team disclosed a coordinated 2026-05-26 takedown of GlassWorm (Archimedes tracked actor #005, HIGH threat level), executed jointly with Google and the Shadowserver Foundation. All four of GlassWorm's parallel command-and-control channels — Solana blockchain memo-field dead-drops, BitTorrent DHT-based configuration retrieval, Google Calendar event titles as Base64 dead-drops, and commercial VPS direct C2 — were disrupted simultaneously, with infected machines redirected to CrowdStrike's benign sinkhole at 164.92.88.210. CrowdStrike attributes the operation to actors "likely based in Russia" based on CIS-locale runtime geofencing and Russian-language code comments, with the vendor's own caveat that no single indicator is proof. No A&D-prime victim is named; the campaign targeted the broader software-developer population via VSCode extensions, npm/PyPI packages, and 300+ poisoned GitHub repositories.

## Sources

### CrowdStrike Counter Adversary Operations (crowdstrike, A-grade)

- URL: https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/
- Published: 2026-05-26 ~14:00 UTC (RSS feed lists `published: null` per CrowdStrike's persistent dateless-marketing pattern; body content + cross-relay corroboration anchors the date)
- Key claim: Multi-partner coordinated takedown of GlassWorm; four-channel C2 architecture description; YARA rules published; Russia-origin pattern-based attribution.

### SecurityWeek (securityweek, B-grade) — relay only

- URL: https://www.securityweek.com/glassworm-botnet-disrupted/
- Published: 2026-05-27 10:10 UTC (06:10 EDT today, in-window)
- Byline: Ionut Arghire
- Key claim: Same as CrowdStrike. Pure relay; not independent corroboration per INTEL-GRADING.md independence test.

## Technical detail

GlassWorm has been corpus-tracked as roster #005 (HIGH) since 2026-04-02. CrowdStrike's takedown disclosure represents the first A-grade vendor takedown report on the actor in the Archimedes corpus and the first A-grade attribution toward Russian origin (current roster state: `nation: unknown, service: null`).

The four-channel C2 architecture is the intelligence-significant tradecraft layer:

1. **Solana blockchain dead-drop**: C2 addresses encoded in Solana transaction memo fields — immutable and publicly accessible.
2. **BitTorrent DHT**: GlasswormRAT queries the peer-to-peer DHT for configuration data stored against hardcoded public keys — decentralized resilience.
3. **Google Calendar**: Event titles used as dead-drop locations for Base64-encoded C2 paths — disrupted via Google partnership.
4. **Commercial VPS**: Traditional direct C2 for final-stage payload delivery.

Two malware families are named with published YARA rules:
- **GlasswormRAT** — Node.js remote access tool; detection patterns include `DownloadManager`, `start_socks`, `nodejs.org`, bootstrap strings (YARA rule `CrowdStrike_GlasswormRat_01`)
- **GlasswormDownloader** — sub-10KB downloader component; detection patterns include `zlib`, `decompress`, `lambda`, `exec` (YARA rule `CrowdStrike_GlasswormDownloader_01`)

Attack vectors per CrowdStrike: trojanized VSCode extensions distributed via OpenVSX marketplace, compromised npm and PyPI packages, and over 300 poisoned GitHub repositories accessed using stolen developer credentials. Platforms with confirmed extension spread: VSCode, Cursor, Positron, Windsurf, VSCodium.

CrowdStrike's attribution language is preserved verbatim per Hard Rule 2: **"The criminals are likely based in Russia."** No APT alias or UNC designation. Pattern-based indicators are CIS-locale runtime geofencing and Russian-language code comments. CrowdStrike's own caveat is preserved: *"No single indicator is proof on its own"* (with the vendor's further note that code comments may reflect AI tooling rather than human authorship).

## IOCs surfaced

See `iocs_surfaced` frontmatter block. Summary:
- Benign sinkhole: `164.92.88.210` (CrowdStrike-operated; SOC-aware classification only)
- YARA rules: `CrowdStrike_GlasswormRat_01`, `CrowdStrike_GlasswormDownloader_01`
- C2 architectural pattern: four-channel (Solana / BitTorrent DHT / Google Calendar / VPS)

CrowdStrike's post references Solana addresses, BitTorrent hashes, and Google Calendar event titles as part of the C2 architecture but does NOT publish specific identifiers in the body. Direct CrowdStrike intel-platform access would be required for that IOC layer.

## Relationship to existing findings

This is the first A-grade vendor takedown report on roster #005 GlassWorm in the corpus. Prior GlassWorm signal in the corpus has been at the supply-chain-tradecraft-pattern level via finding-2026-05-19-0001 (Mini Shai-Hulud) and finding-2026-05-25-0001 (Megalodon — unattributed but ecosystem-adjacent). This finding establishes #005's specific C2 architecture and Russia-origin candidate attribution.

## Open questions for analyst

1. **Roster #005 attribution change**: actor-profiler decides whether to update `_roster.yaml` from `nation: unknown` to `nation: RU (likely, per CrowdStrike 2026-05-26)` with the qualifier verbatim, or hold pending second A/B-grade IR-firm corroboration. Per Hard Rule 2 and the single-source veto, the qualifier "likely" must be preserved if updated.
2. **Forward-looking dormancy assessment**: SAT-ACH candidate on competing hypotheses about GlassWorm's post-takedown operational disposition (reconstitution within weeks vs. pivot-to-new-branding vs. material degradation through Q2). Load-bearing assumption is whether multi-partner coordination materially disrupts all four C2 channels durably.
3. **Architectural pattern reusability**: the four-channel C2 design (blockchain + DHT + cloud-service + VPS) is reusable by other actors. Worth surfacing in weekly synthesis or weekly threat-detection brief as a structural tradecraft warning beyond just GlassWorm.

## Analytic notes (from analyst review)

SAT-ACH pressure-tested CrowdStrike's "likely based in Russia" attribution against four alternatives: a CIS-Russian-speaking-criminal superset (H2), a multi-nationality collective null (H3), a false-flag posture (H4), and a Russian-developer-plus-non-Russian-affiliate composite (H5). The matrix is largely non-diagnostic. CIS-locale geofencing and Russian-language code comments are equally consistent with H1 and the H2 superset; CrowdStrike's own caveat that the comments may be AI-tooling output is a published-by-source brittleness flag against H1 specifically. The H2 CIS-superset is strictly the most defensible reading but Hard Rule 2 prevents originating that attribution. The actionable analyst output is to confirm the grader's single-source veto and ceiling at "likely" — these are correct.

The forward-looking dormancy question (post-takedown disposition) was not subjected to ACH at this pass; it is suitable for revisit in the next #005 actor-profiler review when reconstitution-or-pivot evidence is observable. Roster update guidance: actor-profiler may safely update #005 to nation "RU (likely, per CrowdStrike 2026-05-26)" with the full verbatim qualifier including the AI-tooling caveat, or hold at "unknown" — either is defensible. WEP unchanged.

## Hard Rule compliance

- **Hard Rule 2**: CrowdStrike attribution language preserved verbatim ("the criminals are likely based in Russia"); not upgraded to confirmed RU; actor-profiler review proposed. ACH did NOT originate alternative attribution; H2 surfaced as a more-defensible reading but the analyst output preserves H1 per source.
- **Hard Rule 3**: No PoC, no exploit primitive, no working attack chain reproduced.
- **Hard Rule 6**: CrowdStrike attribution quote at 7 words, under 15-word ceiling. One quote per source.
- **Hard Rule 8**: Splunk first-party check executed; zero events; silence not disconfirming.
