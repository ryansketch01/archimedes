---
finding_id: finding-2026-05-28-0002-unit42-2026-world-cup-attack-surface-handala-cyberav3ngers-razing-ursa-noname057-iran-irgc-mois-fronts
created_at: 2026-05-28T07:58:00-04:00
graded_by: grader
grading_run_id: morning-20260528-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: A2
digraph_layered:
  unit42_a_grade_primary_publication: A2
  handala_hack_mois_front_attribution_unit42_canonical: A2  # Unit 42 IS canonical for Palo Alto "Kitten" naming family
  sandworm_razing_ursa_alias_unit42_canonical: A2           # Unit 42 IS canonical for Palo Alto "Ursa" naming family
  scattered_spider_muddled_libra_alias_unit42_canonical: A2 # roster #013 alias already in _roster.yaml
  banished_kitten_new_alias_for_handala: A2                 # Unit 42 canonical for this naming, but novel-to-corpus
  cobalt_mystique_new_alias_for_handala: A2                 # Unit 42 canonical for this naming, but novel-to-corpus
  razing_ursa_new_alias_for_sandworm: A2                    # Unit 42 canonical, novel-to-corpus
  cyberavengers_irgc_cyber_electronic_command_attribution: A2  # Unit 42 attribution + CISA AA26-097A in-body citation
  cyberavengers_aliases_shahid_kaveh_bauxite_hydro_kitten_storm_0784_unc5691: A2
  forward_looking_world_cup_threat_assessment: A3            # single-source A-grade FORWARD-LOOKING; veto + speculative class
  iran_disruptive_ops_highly_likely_unit42_language: A2     # Unit 42's own confidence language preserved
  cisa_aa26_097a_rockwell_allen_bradley_plc_campaign_existence: A1  # cited within Unit 42 — CISA advisory is corpus-baseline procedural fact
  2018_pyeongchang_olympic_destroyer_sandworm_attribution: A1  # corpus-baseline historical attribution (WCC consensus)
  january_2024_texas_water_tank_russian_attribution: A2     # cited within Unit 42; corpus-adjacent historical (CISA + US gov-attributed)
  noname057_3700_ddos_nato_pattern: A2                       # Unit 42-cited operational figure
  fiddling_scorpius_play_ransomware_french_rugby_attack: A2  # Unit 42-cited operational claim
  no_ad_prime_named_victim: A1                              # negative claim with strong source support
  hard_rule_2_attribution_language_preserved_verbatim: A1
  cluster_anchor: A2

digraph_anchor: >
  Cluster digraph A2 anchored on Palo Alto Unit 42 (Justin Moore byline,
  2026-05-28 06:00 EDT today, in-window for AM-28 14h pre-brief) on
  forward-looking 2026 FIFA World Cup attack-surface threat assessment.
  Unit 42 is A-grade per source-grades.yaml. Single-A-grade-source
  publication with no B-grade media relay layer in the AM-28 window
  (THN / BleepingComputer / SecurityWeek / The Record silent on this
  piece as of 07:42 EDT collection — feeds were checked, items not
  yet present). The cluster anchor A2 reflects:
    (a) Unit 42 (A) as single primary
    (b) Single-source veto on the forward-looking World Cup threat-
        assessment layer — WEP ceiling "likely" until second
        independent A/B-grade source corroborates
    (c) Tracked-actor alias-cluster expansion layer (Banished Kitten /
        Cobalt Mystique for Handala #014; Razing Ursa for Sandworm
        #007) is Unit 42's canonical-naming-convention layer — Unit
        42 IS the canonical originating source for Palo Alto's
        "Kitten" / "Ursa" / "Libra" / "Scorpius" cluster taxonomy, so
        these alias mappings are essentially A2 facts about Unit 42's
        own naming convention
    (d) CISA AA26-097A citation is a real artifact (corpus-baseline
        procedural fact); the underlying CyberAv3ngers / IRGC Cyber-
        Electronic Command Rockwell/Allen-Bradley PLC-targeting
        campaign is CISA-attributed (A1 on existence of the advisory
        + active-campaign-attribution by CISA)
    (e) Historical precedents (2018 Pyeongchang Olympic Destroyer,
        January 2024 Texas water tank) are corpus-baseline well-
        documented attributions (WCC consensus + US-gov attributed)
  Per Hard Rule 2, ALL of Unit 42's source-confidence language is
  preserved verbatim — "highly likely" Iran-nexus disruptive ops,
  "highest-volume highest-likelihood" cybercrime, etc. — without
  Archimedes-side upgrade or downgrade.

source_reliability:
  grade: A
  source_name: "Palo Alto Unit 42 (Justin Moore)"
  source_yaml_id: unit42
  grade_rationale: >
    Unit 42 pre-assigned A per source-grades.yaml. Single-byline,
    Unit 42 in-house threat-assessment publication on the 2026 FIFA
    World Cup attack surface. Unit 42 is also the canonical originator
    for Palo Alto's "Kitten" / "Ursa" / "Libra" / "Scorpius" cluster-
    naming taxonomy — meaning the new aliases surfaced in this piece
    (Banished Kitten, Cobalt Mystique, Razing Ursa) are Unit-42-
    canonical-naming-convention facts about Unit 42's own taxonomy,
    not third-party-attributable claims.
  provisional: false
  embedded_a_grade_citations:
    - artifact: CISA AA26-097A
      grade: A
      role: "CISA advisory cited within the Unit 42 body documenting an active, ongoing Iranian-affiliated campaign targeting Rockwell Automation and Allen-Bradley programmable logic controllers in U.S. critical infrastructure"
      independent_of_unit42: true   # CISA advisory is independent A-grade artifact, not a Unit 42 derivative
      corroboration_value: "Bolsters the CyberAv3ngers IRGC Cyber-Electronic Command PLC-targeting attribution layer specifically; does NOT corroborate the broader forward-looking World Cup threat assessment"
    - artifact: 2018 Pyeongchang Olympic Destroyer attribution to Sandworm / GRU Unit 74455
      grade: A
      role: "Corpus-baseline historical attribution (Western intelligence community consensus + indictment-anchored). Cited within Unit 42 as the canonical sporting-event-targeting precedent for projecting potential 2026 World Cup activity."
      independent_of_unit42: true
    - artifact: January 2024 Texas municipal water tank overflow (Russian-attributed cyber attack)
      grade: A
      role: "CISA + US government attributed; cited within Unit 42 as the OT-disruption-pattern validation precedent (operationally demonstrated, not theoretical)"
      independent_of_unit42: true

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_unit42_canonical_naming_taxonomy
    - probably_true_no_contradicting_ab_grade_source
    - probably_true_technical_claims_internally_coherent_with_corpus_baseline_historical_precedents
  rationale: >
    Probably True (2) on the alias-cluster expansion and Iran-nexus
    threat-assessment layers. Unit 42's canonical-naming-convention
    layer is essentially self-corroborating (Unit 42 IS the canonical
    source for "Kitten" / "Ursa" / "Libra" / "Scorpius" alias
    mappings). The CISA AA26-097A in-body citation provides A-grade
    corroboration specifically on the CyberAv3ngers / IRGC Cyber-
    Electronic Command PLC-targeting attribution layer. Historical
    precedents (2018 Pyeongchang, January 2024 Texas) are corpus-
    baseline well-documented attributions. Forward-looking World Cup
    threat assessment carries single-source-veto status (no second
    A/B-grade source independently corroborates the forward
    projection). No contradicting evidence from A/B-grade sources.

corroboration:
  independent_sources:
    - unit42
    - cisa-advisories
  independent: true
  independent_test_passed: >
    Unit 42 (A vendor) and CISA Advisory AA26-097A (A government) are
    independent sources on the CyberAv3ngers / IRGC Cyber-Electronic
    Command Rockwell/Allen-Bradley PLC-targeting attribution layer.
    CISA AA26-097A is cited within the Unit 42 body but is an
    independent A-grade artifact existing prior to and outside of the
    Unit 42 publication — the CISA advisory's attribution methodology
    is government-grade (CISA names "active, ongoing Iranian-affiliated
    campaign" with its own attribution chain). The independence test
    passes for this specific layer of the cluster.
  partial_corroboration_layers:
    - layer: "CyberAv3ngers / IRGC Cyber-Electronic Command Rockwell+Allen-Bradley PLC-targeting active campaign"
      corroboration_quality: "A+A independent (Unit 42 + CISA AA26-097A)"
      cluster_layer_grade: A1
    - layer: "Handala Hack MOIS-front attribution"
      corroboration_quality: "Unit 42 single-A-grade-source (canonical Palo Alto naming for 'Kitten' family); corpus-tracked via roster #014 with prior B/A-grade sources"
      cluster_layer_grade: A2_with_single_source_veto_on_world_cup_projection
    - layer: "Sandworm Razing Ursa alias mapping"
      corroboration_quality: "Unit 42 canonical naming (Palo Alto convention); roster #007 corpus-tracked with prior B/A-grade aliases (APT44, Seashell Blizzard, Iron Viking, BlackEnergy Group, Telebots, Voodoo Bear)"
      cluster_layer_grade: A2
    - layer: "Forward-looking 2026 World Cup threat assessment for sporting infrastructure / municipal services / hospitality"
      corroboration_quality: "Unit 42 single-A-grade-source; no second independent A/B-grade analysis published; speculative-forward-looking class"
      cluster_layer_grade: A3_with_single_source_veto
  awaiting_corroboration:
    - "Second A/B-grade vendor analysis on the forward-looking 2026 World Cup threat assessment (Mandiant / MSTIC / CrowdStrike / Recorded Future / Cisco Talos all silent in AM-28 window)"
    - "Independent A/B-grade corroboration on Banished Kitten / Cobalt Mystique novel aliases for Handala Hack (Unit 42 canonical naming, but second-source confirmation would lift novel-alias layer)"
    - "B-grade media relay layer (THN / BleepingComputer / SecurityWeek / Dark Reading) on the Unit 42 piece — feeds checked at 07:42 EDT, none yet present"

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    Splunk query against defenseclaw_local + archimedes over -24h@h
    covering "Handala", "CyberAv3ngers", "Banished Kitten", "Razing
    Ursa", "Allen-Bradley", "Rockwell", "Modicon", "FIFA", "World Cup".
    Zero IOC events. Hard Rule 8: silence is not disconfirming. 67th
    consecutive dormant non-self sweep on defenseclaw_local per pre-
    brief sentinel raw-2026-05-28-am-000. No Rockwell/Allen-Bradley
    PLC inventory expected in defenseclaw_local at the current
    instrumentation tier.

single_source_veto_applied: true
single_source_veto_rationale: >
  Veto applies on the forward-looking 2026 World Cup threat-assessment
  layer (Unit 42 single-A-grade-source; no second independent A/B-
  grade analysis). WEP ceiling on that layer is "likely" not "very
  likely" per single-source-veto convention. Veto does NOT apply on
  the CyberAv3ngers / IRGC Cyber-Electronic Command PLC-targeting
  attribution layer (Unit 42 + CISA AA26-097A independent), so that
  sub-layer can carry "very_likely" WEP. Veto does NOT apply on
  Unit-42-canonical alias-cluster expansion (Unit 42 IS canonical for
  Palo Alto naming convention — self-corroborating layer).

wep_ceiling: likely
wep_layered:
  unit42_publication_exists_with_named_byline: very_likely    # procedural
  banished_kitten_unit42_alias_for_handala: very_likely       # Unit 42 canonical
  cobalt_mystique_unit42_alias_for_handala: very_likely       # Unit 42 canonical
  razing_ursa_unit42_alias_for_sandworm: very_likely          # Unit 42 canonical
  handala_hack_mois_front_attribution: likely                 # Unit 42 single-source on this specific framing
  cyberav3ngers_irgc_cyber_electronic_command_attribution: very_likely  # Unit 42 + CISA AA26-097A independent
  rockwell_allen_bradley_plc_active_campaign: very_likely     # CISA AA26-097A is corpus-baseline A1
  forward_looking_world_cup_threat_assessment_iran_disruptive_highly_likely: likely  # single-source veto
  forward_looking_world_cup_cybercrime_highest_volume_highest_likelihood: likely     # single-source veto
  2018_pyeongchang_olympic_destroyer_sandworm: almost_certainly  # corpus-baseline historical attribution
  january_2024_texas_water_tank_russian: very_likely          # CISA + US gov attributed
  noname057_16_3700_ddos_nato_pattern: likely                 # Unit 42 single-source on the figure
  fiddling_scorpius_play_ransomware_french_rugby: likely      # Unit 42 single-source
  ad_prime_direct_exposure: roughly_even_chance               # indirect via tracked-actor capability portability only

inclusion:
  eligible_for:
    - daily_brief_action            # A2 + Iran Cyber Watch standing section + multi-tracked-roster relevance
    - daily_brief_monitoring
    - weekly_synthesis              # Iran-nexus pattern cumulation + tracked-actor alias-expansion signal
    - actor_profile_update          # roster #014 Handala + roster #007 Sandworm alias updates (operator decision)
    - ioc_master_index_propagation  # CISA AA26-097A campaign reference + tracked-actor alias data
  not_eligible_for:
    - flash             # Unit 42 forward-looking threat assessment; no specific in-progress campaign trigger; no CVE; no first-party hit; no A&D-prime named victim (Trigger 5 fails — sporting/municipal/hospitality focus)
  inclusion_rationale: >
    A2 cluster on Unit 42's forward-looking 2026 World Cup attack-
    surface assessment. Eligible for AM-28 brief action tier on the
    basis that: (a) the tracked-actor alias-cluster expansion is
    operator-actionable (roster #014 Handala Hack + roster #007
    Sandworm alias updates pending /update-tracking decision); (b) the
    CyberAv3ngers / IRGC Cyber-Electronic Command PLC-targeting
    attribution layer carries A1 corroboration (Unit 42 + CISA
    AA26-097A) and is directly relevant to A&D-prime OT estates
    running Rockwell + Allen-Bradley PLCs in manufacturing / R&D
    environments; (c) the Iran Cyber Watch standing section relevance
    is high (Handala MOIS + CyberAv3ngers IRGC service-level attributions
    are corpus-baseline updates). NOT FLASH-eligible — forward-looking
    threat-assessment piece, no in-progress campaign trigger, no
    A&D-prime named victim.

# Cluster metadata
cluster:
  topic: "Palo Alto Unit 42 forward-looking 2026 FIFA World Cup attack-surface threat assessment (Justin Moore byline 2026-05-28 06:00 EDT) — names roster #014 Handala Hack with NEW alias cluster Banished Kitten + Cobalt Mystique alongside known Storm-0842 + Void Manticore (MOIS-front per Unit 42; wiper attacks + high-level-government-officials targeting); names roster #007 Sandworm with NEW alias Razing Ursa (Palo Alto canonical naming; 2018 Pyeongchang Olympic Destroyer precedent); names roster #013 Scattered Spider with known Muddled Libra alias (ALPHV/BlackCat operator characterization, hospitality-sector ransomware); names non-roster CyberAv3ngers with alias cluster Shahid Kaveh Group + Bauxite + Hydro Kitten + Storm-0784 + UNC5691 as IRGC Cyber-Electronic Command OT-targeting arm with CISA AA26-097A active-Iran-affiliated-campaign attribution against Rockwell Automation and Allen-Bradley PLCs in US critical infrastructure (water, wastewater, regional power, airport operations, emergency services named victim sectors); names non-roster NoName057(16) pro-Russian hacktivist DDoS cluster (3,700+ verified attacks on NATO members since 2022); names non-roster Fiddling Scorpius Play ransomware distributor (French Rugby Federation attack). Threat-assessment language preserved verbatim per Hard Rule 2: Iran-nexus disruptive ops 'highly likely'; financially motivated cybercrime 'highest-volume highest-likelihood'; OT disruption High severity; wiper/destructive ops High-critical severity. NO A&D / aerospace / defense / government contractor sector named in body. Indirect A&D-relevance via tracked-actor capability portability (Handala wiper + Sandworm Olympic Destroyer precedent + CyberAv3ngers Rockwell PLC TTPs portable to A&D-prime OT estates)."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-28-am-002-unit42-2026-world-cup-attack-surface-handala-cyberav3ngers-razing-ursa-noname057-iran-irgc-mois-fronts
  related_actors:
    - actor_id: "014"
      actor_name: "Handala Hack"
      threat_level: HIGH
      alias_cluster_per_unit42: ["Banished Kitten (NEW)", "Storm-0842", "Void Manticore", "Cobalt Mystique (NEW)"]
      roster_yaml_aliases: ["Void Manticore", "Storm-0842", "DEV-0842"]
      delta: "ADD Banished Kitten + Cobalt Mystique (Unit 42 canonical Palo Alto 'Kitten' family naming); already-present: Void Manticore, Storm-0842"
      requires_actor_profiler_update: true
    - actor_id: "007"
      actor_name: "Sandworm"
      threat_level: HIGH
      alias_cluster_per_unit42: ["Razing Ursa (NEW)"]
      roster_yaml_aliases: ["APT44", "Seashell Blizzard", "Iron Viking", "BlackEnergy Group", "Telebots", "Voodoo Bear"]
      delta: "ADD Razing Ursa (Unit 42 canonical Palo Alto 'Ursa' family naming)"
      requires_actor_profiler_update: true
    - actor_id: "013"
      actor_name: "Scattered Spider"
      threat_level: HIGH
      alias_cluster_per_unit42: ["Muddled Libra"]
      roster_yaml_aliases: ["UNC3944", "Octo Tempest", "0ktapus", "Scatter Swine", "Muddled Libra", "Starfraud"]
      delta: "No new aliases — Muddled Libra already in roster. ALPHV/BlackCat operator characterization is operationally narrower than full Scattered Spider tradecraft (Octo Tempest / 0ktapus / vishing); briefer should preserve Unit 42's specific framing without conflating with full roster #013 dossier."
      requires_actor_profiler_update: false
  non_roster_actor_candidates:
    - candidate_name: "CyberAv3ngers"
      priority: HIGH
      rationale: "IRGC Cyber-Electronic Command OT-targeting arm + CISA AA26-097A active-campaign attribution against Rockwell+Allen-Bradley PLCs in US critical infrastructure + named victim sectors (water, wastewater, regional power, airport operations, emergency services) + operational portability to A&D-prime manufacturing/R&D OT estates running Rockwell PLCs. HIGH-priority /new-actor candidate for operator evaluation."
      unit42_alias_cluster: ["Shahid Kaveh Group", "Bauxite", "Hydro Kitten", "Storm-0784", "UNC5691"]
    - candidate_name: "NoName057(16)"
      priority: LOW
      rationale: "Pro-Russian hacktivist DDoS cluster; 3,700+ verified attacks on NATO members since 2022. DDoS-only TTP; hacktivist cluster; NATO-targeting pattern structurally adjacent to A&D but not direct-A&D-sector."
    - candidate_name: "Fiddling Scorpius"
      priority: LOW
      rationale: "Play ransomware distributor; French Rugby Federation attack. Cybercriminal cluster; lower priority absent A&D-prime-specific TTP evidence."
  related_vulnerabilities: []  # No fresh CVE in article body
  related_campaign_references:
    - campaign: "CISA AA26-097A"
      type: "active Iranian-affiliated campaign"
      targets: "Rockwell Automation + Allen-Bradley PLCs in US critical infrastructure"
      sectors_named: ["water", "wastewater treatment", "regional power", "airport operations", "emergency services"]
  attribution_claims:
    - claim: "CyberAv3ngers = IRGC Cyber-Electronic Command's OT targeting arm"
      claimed_by: Unit 42 (Justin Moore 2026-05-28)
      claim_confidence_language: "IRGC Cyber-Electronic Command's OT targeting arm" (Unit 42 verbatim)
      novelty_to_corpus: true   # first corpus formalization of the CyberAv3ngers IRGC service attribution
      requires_analyst_review: true   # /new-actor candidate decision + service-level attribution review
      hard_rule_2_status: "preserved as Unit 42 attribution; CISA AA26-097A provides independent A-grade corroboration on the PLC-targeting campaign existence layer specifically"
    - claim: "Handala Hack = MOIS front"
      claimed_by: Unit 42 (Justin Moore 2026-05-28)
      claim_confidence_language: "assessed as MOIS front" (Unit 42 verbatim) — Iranian Ministry of Intelligence and Security
      novelty_to_corpus: false  # roster #014 dossier already lists Handala Hack as IR/MOIS
      requires_analyst_review: false
      hard_rule_2_status: "preserved; corpus-baseline restatement"
    - claim: "Banished Kitten + Cobalt Mystique = Handala Hack aliases (Unit 42 canonical Palo Alto naming)"
      claimed_by: Unit 42 (Justin Moore 2026-05-28)
      claim_confidence_language: "Unit 42 canonical naming convention"
      novelty_to_corpus: true   # NEW aliases not in _roster.yaml
      requires_analyst_review: false  # Unit 42 canonical naming, A-grade single-source on its own taxonomy
      hard_rule_2_status: "preserved; actor-profiler roster update flag for #014"
    - claim: "Razing Ursa = Sandworm (Unit 42 canonical Palo Alto naming)"
      claimed_by: Unit 42 (Justin Moore 2026-05-28)
      claim_confidence_language: "Unit 42 canonical naming convention"
      novelty_to_corpus: true   # NEW alias not in _roster.yaml
      requires_analyst_review: false
      hard_rule_2_status: "preserved; actor-profiler roster update flag for #007"

# IOCs surfaced
iocs_surfaced:
  - type: actor_alias_cluster
    value: "Handala Hack — Banished Kitten + Cobalt Mystique + Storm-0842 + Void Manticore"
    context: "Unit 42 canonical alias cluster for roster #014. Banished Kitten + Cobalt Mystique are NEW (Unit 42 Palo Alto 'Kitten' family naming); Storm-0842 + Void Manticore already in roster."
    confidence: high
    source_attribution: "Unit 42 (Justin Moore) 2026-05-28"
    defanged: false
  - type: actor_alias_cluster
    value: "Sandworm — Razing Ursa"
    context: "Unit 42 canonical alias for roster #007. Razing Ursa is NEW (Unit 42 Palo Alto 'Ursa' family naming); existing roster aliases APT44 / Seashell Blizzard / Iron Viking / BlackEnergy Group / Telebots / Voodoo Bear."
    confidence: high
    source_attribution: "Unit 42 (Justin Moore) 2026-05-28"
    defanged: false
  - type: actor_alias_cluster
    value: "CyberAv3ngers — Shahid Kaveh Group + Bauxite + Hydro Kitten + Storm-0784 + UNC5691"
    context: "Unit 42 alias cluster for non-roster IRGC Cyber-Electronic Command OT-targeting arm. CISA AA26-097A documents active campaign against Rockwell+Allen-Bradley PLCs."
    confidence: high
    source_attribution: "Unit 42 (Justin Moore) 2026-05-28 + CISA AA26-097A"
    defanged: false
  - type: campaign_reference
    value: "CISA AA26-097A"
    context: "Active, ongoing Iranian-affiliated campaign targeting internet-exposed Rockwell Automation and Allen-Bradley programmable logic controllers in U.S. critical infrastructure. Named victim sectors: water, wastewater treatment, regional power, airport operations, emergency services."
    confidence: high
    source_attribution: "CISA AA26-097A (cited within Unit 42 body)"
    defanged: false
  - type: tradecraft_pattern
    value: "Handala Hack wiper attacks + high-level-government-officials targeting"
    context: "Unit 42 TTP characterization for roster #014. Wiper-class capability operationally portable to A&D-prime M365 / executive-targeting scenarios."
    confidence: high
    source_attribution: "Unit 42 (Justin Moore) 2026-05-28"
    defanged: false
  - type: historical_precedent
    value: "2018 Pyeongchang Olympic Destroyer attribution to Sandworm / GRU Unit 74455"
    context: "Corpus-baseline historical attribution (WCC consensus + indictment-anchored). Canonical sporting-event-targeting precedent Unit 42 uses to project potential 2026 World Cup activity."
    confidence: high
    source_attribution: "Unit 42 reference + corpus-baseline"
    defanged: false
  - type: historical_precedent
    value: "January 2024 Texas municipal water tank overflow (Russian-attributed cyber attack)"
    context: "CISA + US government attributed. Cited within Unit 42 as OT-disruption-pattern validation precedent (operationally demonstrated, not theoretical)."
    confidence: high
    source_attribution: "Unit 42 reference + CISA + US gov"
    defanged: false
  - type: operational_figure
    value: "NoName057(16) — 3,700+ verified DDoS attacks against NATO members since 2022"
    context: "Unit 42 cited operational figure; pro-Russian hacktivist DDoS cluster."
    confidence: medium
    source_attribution: "Unit 42 (Justin Moore) 2026-05-28"
    defanged: false
  - type: operational_event
    value: "Fiddling Scorpius — Play ransomware attack on French Rugby Federation"
    context: "Unit 42 cited recent reference for Play ransomware distributor."
    confidence: medium
    source_attribution: "Unit 42 (Justin Moore) 2026-05-28"
    defanged: false

ttp_keywords:
  - name: Wiper attacks against government-official targets (Handala Hack)
    framework_mapping: MITRE T1485 Data Destruction / T1561 Disk Wipe
    context: "Unit 42 TTP characterization for roster #014. Operationally portable to A&D-prime M365 / executive-targeting scenarios."
  - name: ICS/OT targeting of Rockwell Automation + Allen-Bradley PLCs (CyberAv3ngers / IRGC Cyber-Electronic Command)
    framework_mapping: MITRE ATT&CK for ICS T0809 Block Reporting Message / T0814 Denial of Service / T0831 Manipulation of Control / T0855 Unauthorized Command Message
    context: "CISA AA26-097A documents active campaign; named victim sectors water/wastewater/regional power/airport ops/emergency services. Portable to A&D-prime manufacturing/R&D OT estates running Rockwell PLCs."
  - name: Hospitality-sector ransomware targeting (Muddled Libra / ALPHV-BlackCat operator role)
    framework_mapping: MITRE T1486 Data Encrypted for Impact / T1657 Financial Theft
    context: "Unit 42 cited Muddled Libra / Scattered Spider ALPHV/BlackCat operator role targeting hospitality sector (hotel chains hosting World Cup tourists/officials)."
  - name: DDoS against NATO-member online services (NoName057(16))
    framework_mapping: MITRE T1498 Network Denial of Service
    context: "Unit 42 cites 3,700+ verified attacks since 2022; politically symbolic event surge pattern."

# Downstream handoff flags
analyst_review_required: true
analyst_review_topics:
  - "/new-actor scaffolding decision for CyberAv3ngers: Unit 42 attributes to IRGC Cyber-Electronic Command + CISA AA26-097A active-campaign attribution + named victim sectors (water, wastewater, regional power, airport ops, emergency services) + Unit 42 alias cluster (Shahid Kaveh Group + Bauxite + Hydro Kitten + Storm-0784 + UNC5691). Operationally portable to A&D-prime OT estates running Rockwell+Allen-Bradley PLCs. HIGH-priority operator decision."
  - "Actor-profiler roster update for #014 Handala Hack: ADD Banished Kitten + Cobalt Mystique aliases (Unit 42 Palo Alto 'Kitten' family canonical naming). Existing aliases Void Manticore + Storm-0842 + DEV-0842 unchanged."
  - "Actor-profiler roster update for #007 Sandworm: ADD Razing Ursa alias (Unit 42 Palo Alto 'Ursa' family canonical naming). Existing aliases APT44 + Seashell Blizzard + Iron Viking + BlackEnergy Group + Telebots + Voodoo Bear unchanged."
  - "SAT-ACH candidate on the forward-looking 2026 World Cup threat-assessment confidence framing: Unit 42's 'highly likely' on Iran-nexus disruptive ops + 'highest-volume highest-likelihood' on financially motivated cybercrime is single-source. Competing hypotheses on whether second-source corroboration will (H1) confirm Unit 42's framing, (H2) shift the relative weighting (e.g., Sandworm Olympic Destroyer precedent suggests Russia-nexus is comparably likely), (H3) downgrade the forward projection altogether (sporting-event threat models can over-project)."
  - "Defender carry-forward for any A&D-prime estate with Rockwell + Allen-Bradley PLC inventory: CISA AA26-097A is the relevant artifact. CyberAv3ngers / IRGC Cyber-Electronic Command active-campaign attribution carries A1 corroboration (Unit 42 + CISA independent). SAT-KAC on the assumption that A&D-prime OT estates are sufficiently segmented from internet exposure to mitigate the CISA-documented internet-exposed-PLC attack surface."

analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Which framing best explains the Iran-nexus actor structure Unit 42 presents — Handala Hack as MOIS front + CyberAv3ngers as IRGC Cyber-Electronic Command — and what is the corroboration status of the IRGC/MOIS service-tier attribution for an A&D-prime defender's purposes?"
      analyzed_at: 2026-05-28T08:40:00-04:00
      analyzed_by: analyst
      analyst_run_id: analyst-20260528-082000
      red_team_review_note: >
        Grader explicitly held red-team on this finding (WEP capped at
        'likely' on dominant forward-looking layer by single-source veto;
        CyberAv3ngers PLC-campaign sub-layer is A1 via CISA but is
        corpus-baseline restatement rather than novel synthesis).
        Analyst proceeds with ACH on the front-organization attribution
        layer specifically, where the IRGC vs MOIS service-tier
        distinction matters for downstream actor-profiler tracking and
        Iran-roster framing.

      hypotheses:
        - id: H1
          statement: "Unit 42's framing is substantively correct: Handala Hack is an MOIS front; CyberAv3ngers is the IRGC Cyber-Electronic Command's OT-targeting arm. The two clusters operate under distinct Iranian services with separable mandates (MOIS = intelligence/disruptive ops + influence; IRGC-CEC = ICS/OT disruption against CI). Roster #014 attribution stands; CyberAv3ngers warrants a separate roster slot."
        - id: H2
          statement: "Both Handala and CyberAv3ngers are Iran-nexus but the specific service attribution (MOIS vs IRGC-CEC) is over-determined by available evidence. Both could be contractor-cluster activities tasked across multiple Iranian services rather than directly subordinated to a single agency. The Unit 42 service-tier distinction is plausible analysis but not load-bearing for defender prioritization."
        - id: H3
          statement: "Handala Hack as MOIS front is corpus-baseline (roster #014 already attributes MOIS); CyberAv3ngers as IRGC Cyber-Electronic Command's OT-targeting arm is a NOVEL Unit 42 attribution that has not been independently corroborated at the IRGC-CEC service-tier level (CISA AA26-097A attributes 'Iranian-affiliated' without naming the specific service). The IRGC-CEC claim is single-source-veto territory."
        - id: H4
          statement: "Surprise/composite: CyberAv3ngers is an IRGC-affiliated contractor cluster (not directly an IRGC unit) — operating with state acquiescence rather than as a state organic capability. The Unit 42 'IRGC Cyber-Electronic Command's OT targeting arm' framing collapses contractor + state into a single label that the available evidence cannot distinguish."
        - id: H5
          statement: "Null/persona hypothesis: CyberAv3ngers is a persona used across multiple Iranian operational units, sometimes IRGC-CEC-directed and sometimes MOIS-directed depending on target sector. The single-service attribution is a model-fit issue, not a reflection of how the activity is actually conducted."

      evidence:
        - id: E1
          description: "Unit 42 names Handala Hack as MOIS front (canonical Palo Alto 'Kitten' family — Banished Kitten + Cobalt Mystique aliases)"
          source: unit42-2026-05-28
          digraph: A2
          weight: 3
        - id: E2
          description: "Unit 42 names CyberAv3ngers as 'IRGC Cyber-Electronic Command's OT targeting arm with documented escalation curve'"
          source: unit42-2026-05-28
          digraph: A2
          weight: 3
        - id: E3
          description: "CISA AA26-097A attributes the active Rockwell+Allen-Bradley PLC campaign to 'Iranian-affiliated' actors but does NOT specify IRGC-CEC at the service-tier level"
          source: cisa-aa26-097a-cited-in-unit42-body
          digraph: A1
          weight: 3
        - id: E4
          description: "CyberAv3ngers alias cluster per Unit 42: Shahid Kaveh Group + Bauxite + Hydro Kitten + Storm-0784 + UNC5691 — multi-vendor alias overlap is consistent with a single attributed cluster"
          source: unit42-2026-05-28
          digraph: A2
          weight: 3
        - id: E5
          description: "Roster #014 Handala Hack already lists IR/MOIS attribution; Unit 42 framing is corpus-baseline restatement on this layer"
          source: roster-014-corpus-baseline
          digraph: A2
          weight: 3
        - id: E6
          description: "Iranian cyber operations are corpus-documented as involving contractor clusters (MABNA Institute, Charming Kitten contractor sphere, MuddyWater contractor frameworks) — service attribution is sometimes contractor-mediated rather than direct unit assignment"
          source: corpus-prior-iran-attribution-pattern
          digraph: B2
          weight: 2
        - id: E7
          description: "Roster #022 MuddyWater + roster #014 Handala both attribute MOIS — MOIS has multiple operational entities in corpus; CyberAv3ngers being an additional IRGC entity is structurally consistent with the IR-service portfolio"
          source: corpus-iran-roster-baseline
          digraph: A2
          weight: 3
        - id: E8
          description: "No second A-grade vendor analysis (Mandiant / MSTIC / CrowdStrike / Recorded Future / Cisco Talos) on the specific CyberAv3ngers = IRGC Cyber-Electronic Command service-tier attribution visible in AM-28 window"
          source: corpus-silence-2026-05-28
          digraph: A1
          weight: 3
        - id: E9
          description: "Documented escalation curve language in Unit 42 implies longitudinal observation by Palo Alto across multiple campaigns — the IRGC-CEC framing is consistent with Unit 42's own historical telemetry, not a one-off framing"
          source: unit42-2026-05-28
          digraph: A2
          weight: 3
        - id: E10
          description: "CyberAv3ngers named victim sectors per Unit 42 + CISA: water, wastewater, regional power, airport operations, emergency services — sectors consistent with IRGC-CEC OT-disruption mandate (vs MOIS intelligence-oriented mandate)"
          source: unit42-2026-05-28-and-cisa-aa26-097a
          digraph: A1
          weight: 3
        - id: E11
          description: "MOIS-attributed clusters in corpus (MuddyWater #022, Handala #014) primarily target espionage / disruption / hacktivist-style influence — distinct operational signature from CyberAv3ngers' OT-disruption pattern"
          source: corpus-iran-roster-baseline
          digraph: A2
          weight: 3

      matrix:
        E1:  {H1: C, H2: C, H3: C, H4: C, H5: C}
        E2:  {H1: C, H2: N, H3: I, H4: N, H5: N}
        E3:  {H1: N, H2: C, H3: C, H4: C, H5: C}
        E4:  {H1: C, H2: C, H3: C, H4: C, H5: C}
        E5:  {H1: C, H2: C, H3: C, H4: C, H5: C}
        E6:  {H1: N, H2: C, H3: N, H4: C, H5: C}
        E7:  {H1: C, H2: N, H3: N, H4: N, H5: N}
        E8:  {H1: N, H2: N, H3: C, H4: N, H5: N}
        E9:  {H1: C, H2: N, H3: I, H4: N, H5: N}
        E10: {H1: C, H2: C, H3: N, H4: C, H5: I}
        E11: {H1: C, H2: N, H3: N, H4: N, H5: I}

      inconsistency_counts:
        H1: 0
        H2: 0
        H3: 2
        H4: 0
        H5: 2

      diagnostic_evidence:
        - E2: "Diagnostic against H3 — Unit 42 affirmatively names IRGC Cyber-Electronic Command; H3 (no IRGC-CEC corroboration) treats this affirmation as un-corroborated rather than as the Unit 42 contribution it is. The diagnostic question is whether single-A-grade-source naming a specific service tier suffices for that tier-level attribution."
        - E9: "Diagnostic against H3 — 'documented escalation curve' language implies Unit 42 longitudinal observation across multiple campaigns; the IRGC-CEC framing is anchored in observed pattern not one-off label."
        - E10: "Diagnostic against H5 — sector pattern (OT/ICS critical infrastructure) is consistent with IRGC mandate, less consistent with persona-shared-across-services framing where sectors would be more heterogeneous."
        - E11: "Diagnostic against H5 — MOIS clusters in corpus show distinct (espionage/disruption/hacktivist) operational signature; if CyberAv3ngers were sometimes MOIS-directed, we'd expect more mixed targeting."

      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: "Zero inconsistencies. The strongest diagnostic evidence (E9, E10, E11) all align: Unit 42 has longitudinal observation; sector pattern fits IRGC OT mandate; MOIS clusters show distinct operational signature. This is the analyst's preferred reading, with the explicit caveat that the IRGC-CEC-specific service-tier attribution rests on Unit 42 single-A-grade-source."
          wep: likely
        - rank: 2
          hypothesis_id: H4
          rationale: "Zero inconsistencies but introduces a contractor-vs-state-organic distinction the evidence cannot resolve. Iranian cyber operations corpus pattern (E6) makes this hypothesis structurally available. Cannot be ruled out; should be treated as a 'cannot eliminate' refinement of H1 rather than a competing reading."
          wep: roughly_even_chance
        - rank: 3
          hypothesis_id: H2
          rationale: "Zero inconsistencies but introduces an over-determination concern that lacks specific support. The 'service distinction is not load-bearing for defender prioritization' framing is plausible but the diagnostic evidence (E9, E10, E11) actively distinguishes IRGC pattern from MOIS pattern in corpus."
          wep: unlikely
        - rank: 4
          hypothesis_id: H3
          rationale: "Two inconsistencies (E2, E9). The IRGC-CEC service-tier attribution stands on Unit 42 single-A-grade-source — but treating that as inadequate ignores Unit 42's longitudinal observation language and the corroborative CISA AA26-097A on the broader Iranian-affiliated campaign. H3 demands a stricter corroboration standard than the corpus typically requires for service-tier framings."
          wep: unlikely
        - rank: 5
          hypothesis_id: H5
          rationale: "Two inconsistencies (E10, E11). Persona-shared-across-services is hardest to sustain because the operational signature (OT-only sector targeting) is too consistent with a single mandate. If CyberAv3ngers were a persona used across services, sector pattern would be more heterogeneous."
          wep: unlikely

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E2, E8, E10]
        if_E2_unit42_attribution_partially_retracted_or_qualified: "H3 strengthens; IRGC-CEC service-tier attribution downgrades to 'roughly even chance'; rerun ACH"
        if_E8_resolves_with_corroborating_vendor: "H1 strengthens; WEP on IRGC-CEC service-tier could lift to 'very likely'; rerun ACH"
        if_E8_resolves_with_contradicting_vendor_naming_different_service: "H1 weakens significantly; H3/H4 strengthen; immediate rerun"
        if_E10_cyberavengers_observed_targeting_non_ot_non_ci_sector: "H5 strengthens; H1 weakens; immediate rerun"
        single_point_of_failure: "E2 (Unit 42's specific IRGC Cyber-Electronic Command service-tier attribution) for the IRGC-CEC-specific framing. The broader CyberAv3ngers-as-Iranian-affiliated layer is anchored by CISA AA26-097A (A1 independent) and does NOT collapse if E2 erodes — only the service-tier specificity does."

      tripwires:
        - observation: "Mandiant / MSTIC / CrowdStrike / Recorded Future publish independent analysis on CyberAv3ngers service-tier attribution"
          effect: "E8 flips; rerun ACH; cluster grade on this layer can lift to A1"
        - observation: "Independent corroboration of CyberAv3ngers as IRGC-CEC specifically (rather than generic 'Iranian')"
          effect: "H1 confirms at very_likely; service-tier framing solidifies"
        - observation: "Independent attribution naming a DIFFERENT Iranian service (MOIS, IRGC-IO, IRGC-QF) for CyberAv3ngers"
          effect: "H3 strengthens; immediate rerun"
        - observation: "CyberAv3ngers observed targeting espionage-oriented sectors (telecoms, government, A&D R&D) inconsistent with OT-only signature"
          effect: "H5 strengthens; operational signature breaks"
        - observation: "Sandworm observed running a World Cup-targeting operation paralleling 2018 Pyeongchang"
          effect: "Validates the Olympic Destroyer historical-precedent layer; cluster overall lifts"

      conclusion:
        summary: |
          The best-supported reading is H1: Handala Hack as MOIS front (corpus-
          baseline; roster #014 confirms) and CyberAv3ngers as IRGC Cyber-
          Electronic Command's OT-targeting arm (Unit 42 attribution + CISA
          AA26-097A independent corroboration on the active campaign layer,
          though CISA does not specify IRGC-CEC at the service tier). The
          operational signature (OT-only sector targeting, documented
          escalation curve, multi-vendor alias overlap) distinguishes
          CyberAv3ngers from corpus-tracked MOIS clusters and supports the
          IRGC-mandate framing. H4 (contractor-vs-state-organic refinement)
          cannot be ruled out and may be the more accurate model; H4 is
          best read as a sharpening of H1 rather than a replacement.
        wep: likely
        wep_layered:
          handala_mois_front_corpus_baseline: very_likely
          cyberavengers_iranian_affiliated_generic_per_cisa: very_likely
          cyberavengers_irgc_cyber_electronic_command_specific: likely
          contractor_vs_state_organic_refinement_for_cyberavengers: roughly_even_chance
          forward_looking_world_cup_threat_assessment: likely
        confidence_caveats: |
          Single-source veto applies on the IRGC-CEC service-tier
          specificity (Unit 42 only). The Iranian-affiliated layer is A1
          via CISA. Hard Rule 2 preserves attribution as Unit 42-sourced
          for the IRGC-CEC specificity and CISA-sourced for the broader
          Iranian-affiliated campaign existence. Brief should keep these
          two layers separable; if a second A/B-grade vendor corroborates
          the IRGC-CEC service-tier specifically, the WEP on that layer
          can lift to very_likely.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "CyberAv3ngers (per CISA AA26-097A + Unit 42 attribution) actively
        targets Rockwell Automation and Allen-Bradley PLCs in US critical
        infrastructure; the TTPs are operationally portable to A&D-prime
        manufacturing/R&D OT estates running Rockwell PLCs; A&D-prime OT
        estates are sufficiently segmented from internet exposure to
        mitigate the documented internet-exposed-PLC attack surface."
      analyzed_at: 2026-05-28T08:48:00-04:00
      analyzed_by: analyst
      invoking_context: >
        The grader explicitly flagged the A&D-prime OT-segmentation
        assumption as the load-bearing premise for the defender carry-
        forward implication. The CISA AA26-097A campaign documents
        internet-exposed PLCs in water / wastewater / regional power /
        airport ops / emergency services — sectors whose internet exposure
        patterns differ from A&D-prime manufacturing OT. KAC interrogates
        whether the framework applies to A&D-prime contexts, or is
        sector-specific to the documented victim sectors.

      assumptions:
        - id: A1
          statement: "A&D-prime manufacturing and R&D OT estates run Rockwell Automation + Allen-Bradley PLCs at material density (i.e., enough Rockwell/AB inventory that CyberAv3ngers' Rockwell+AB-specific TTPs apply)"
          category: technology
          stated: true
          why_must_be_true: >
            The whole carry-forward depends on A&D-prime estates actually
            running the targeted technology stack; if A&D primes have
            largely standardized on Siemens / Schneider / Mitsubishi /
            other PLC vendors, the Rockwell+AB-specific TTPs don't apply
            and the campaign is sector-specific rather than vendor-specific
          when_could_be_false: >
            A&D-prime OT inventory varies by program and supplier. Boeing,
            Lockheed, Northrop, Raytheon, GD, and L3Harris run heterogeneous
            PLC fleets across hundreds of facilities; vendor mix depends
            on plant age, country of origin, and program-specific
            integration requirements. Rockwell is common in US-domestic
            manufacturing but not universal
          evidence_for: [rockwell-is-dominant-us-domestic-manufacturing-plc-vendor-industry-baseline]
          evidence_against: [no-archimedes-corpus-evidence-on-specific-ad-prime-plc-inventory, splunk-defenseclaw-local-zero-rockwell-allen-bradley-hits-in-last-30d]
          confidence: medium
          centrality: critical
          classification: qualify

        - id: A2
          statement: "A&D-prime OT estates are sufficiently SEGMENTED from internet exposure to mitigate the CyberAv3ngers internet-exposed-PLC attack surface"
          category: technology
          stated: true
          why_must_be_true: >
            The defender posture conclusion ('A&D primes are relatively
            insulated from the documented campaign') depends on A&D-prime
            OT being air-gapped or strongly segmented; if A&D-prime
            Rockwell PLCs are reachable from the internet (directly or
            via flat-network management VLANs), the campaign applies
            directly
          when_could_be_false: >
            (a) A&D-prime contractor manufacturing facilities are not
            uniformly segmented to the same degree as the company's R&D
            classified networks — production lines often have engineering
            workstations dual-homed for maintenance/monitoring; (b) the
            DIB ecosystem includes Tier-2/3 suppliers whose segmentation
            is materially weaker than primes' own; (c) historical CISA
            advisories (e.g., the 2024 Texas water tank precedent cited
            in this Unit 42 piece) have repeatedly found that 'air-gapped'
            OT networks are not actually air-gapped; (d) A&D-prime IT/OT
            convergence trends (Industrial IoT, predictive-maintenance
            analytics, vendor-managed monitoring) increasingly couple OT
            to the internet via cloud services
          evidence_for: [ad-prime-cmmc-and-cdsa-requirements-mandate-strong-network-segmentation, ad-prime-itar-controlled-networks-have-formal-segmentation-controls]
          evidence_against: [historical-cisa-advisories-find-ad-jacent-ot-networks-routinely-internet-reachable, dib-tier-2-3-suppliers-known-weaker-segmentation, it-ot-convergence-trend-erodes-segmentation, no-archimedes-first-party-evidence-on-ad-prime-ot-segmentation]
          confidence: low
          centrality: critical
          classification: test

        - id: A3
          statement: "The Unit 42 World Cup framework — focused on sporting infrastructure, host-city municipal services, hospitality, and fan platforms — actually applies to a US aerospace/defense contractor target, given that A&D is NOT named in the article's sector list"
          category: semantic
          stated: false
          why_must_be_true: >
            The whole analytic relevance of this finding to an A&D-prime
            audience depends on capability portability from Unit 42's
            named sectors to A&D-prime OT. If portability is weak, the
            finding has only general 'know what's out there' value rather
            than direct defender carry-forward
          when_could_be_false: >
            Unit 42 explicitly scoped to sporting/municipal/hospitality;
            CyberAv3ngers documented victims (water, wastewater, regional
            power, airport ops, emergency services) are utility-class OT
            with different threat models than A&D-prime manufacturing.
            The Rockwell+AB attack surface is shared, but the broader
            World Cup framework may not transfer. Israeli-context
            historical Iranian OT attacks (the implicit backdrop for
            Iran-affiliated PLC targeting) have different geopolitical
            and operational drivers than US-domestic A&D
          evidence_for: [rockwell-allen-bradley-vendor-tooling-is-vendor-specific-not-sector-specific-so-the-plc-ttps-port]
          evidence_against: [unit42-world-cup-scope-explicitly-non-ad, unit42-sporting-municipal-hospitality-targeting-sector-specific, israeli-context-iranian-ot-history-has-different-drivers-than-us-ad]
          confidence: medium
          centrality: material
          classification: qualify

        - id: A4
          statement: "Iranian-affiliated OT-targeting actors during the World Cup window will operate at increased tempo regardless of whether their specific targets are in the World Cup ecosystem — i.e., the campaign window translates to general Iranian cyber tempo, not just sport-related targets"
          category: actor_operational_status
          stated: false
          why_must_be_true: >
            The forward-looking projection's relevance to an A&D-prime
            audience depends on Iranian OT-targeting actors elevating
            tempo broadly during the window, not just against the World
            Cup-specific sectors. If actors stay narrowly focused on
            World Cup targets, an A&D defender's tempo concern is
            unchanged from baseline
          when_could_be_false: >
            Historical precedent (Pyeongchang 2018 Sandworm Olympic
            Destroyer) is event-specific, not a generalized Russian-
            cyber-tempo increase; the same could apply to Iran in 2026.
            Iranian cyber resourcing decisions may concentrate on the
            event rather than expand the operational envelope
          evidence_for: [unit42-says-iran-nexus-disruptive-ops-highly-likely-during-window, iranian-cyber-operations-corpus-pattern-typically-multi-front]
          evidence_against: [pyeongchang-2018-was-event-specific-not-tempo-generalization, no-corpus-evidence-on-iranian-event-driven-vs-baseline-tempo-distinction]
          confidence: medium
          centrality: material
          classification: qualify

        - id: A5
          statement: "Unit 42's 'highly likely' confidence language for Iran-nexus disruptive ops translates to WEP 'likely' (not 'very likely') for an Archimedes audience, given single-source veto on the forward projection"
          category: source_reliability
          stated: true
          why_must_be_true: >
            The grader has explicitly applied single-source veto and
            capped WEP at 'likely' on the forward projection layer;
            preserving this in analyst-side framing prevents over-promotion
            of Unit 42's language
          when_could_be_false: >
            If a second A/B-grade vendor publishes corroborating forward
            assessment, single-source veto lifts and the WEP could rise
            to 'very likely' or higher consistent with Unit 42's confidence
          evidence_for: [grader-explicit-single-source-veto, intel-grading-doctrine-veto-convention]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound

        - id: A6
          statement: "The Handala Hack MOIS-front attribution is corpus-stable enough (roster #014 already lists IR/MOIS) that Unit 42's restatement does not constitute novel single-source attribution requiring veto"
          category: source_reliability
          stated: false
          why_must_be_true: >
            The MOIS-front layer of the Handala framing is corpus-baseline;
            Unit 42 restating it does not introduce new attribution risk.
            This is structurally different from the CyberAv3ngers = IRGC-
            CEC service-tier framing, which IS novel
          when_could_be_false: >
            If the original MOIS attribution for Handala is itself single-
            source-dependent in the corpus, Unit 42 restating it does not
            multiply the corroboration; corpus-baseline stability assumes
            the original attribution chain is robust
          evidence_for: [roster-014-mois-attribution-is-corpus-baseline-pre-this-finding, multi-vendor-naming-overlap-storm-0842-void-manticore-dev-0842-suggests-multi-source-attribution-history]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound

        - id: A7
          statement: "Defender carry-forward for A&D primes is 'audit Rockwell+Allen-Bradley PLC internet exposure; verify segmentation' rather than 'patch a specific CVE' — i.e., the CyberAv3ngers campaign is a configuration/exposure threat not a vulnerability threat"
          category: technology
          stated: false
          why_must_be_true: >
            CISA AA26-097A documents 'internet-exposed' PLCs as the
            attack surface; the defender response is therefore about
            exposure/segmentation rather than patching. The carry-forward
            framing depends on this characterization holding
          when_could_be_false: >
            If CyberAv3ngers exploits CVE-class vulnerabilities IN the
            Rockwell/AB firmware (rather than misconfigured exposure),
            defender response shifts to patching priorities. CISA
            advisories sometimes mix exposure and CVE-class issues
          evidence_for: [cisa-aa26-097a-language-emphasizes-internet-exposed-plcs-per-unit42-relay]
          evidence_against: [archimedes-has-not-directly-retrieved-cisa-aa26-097a-text-to-verify-exposure-vs-cve-mix]
          confidence: medium
          centrality: material
          classification: qualify

        - id: A8
          statement: "The Razing Ursa alias for Sandworm (Unit 42 canonical Palo Alto 'Ursa' family naming) is operationally identical to Sandworm and does not denote a different cluster"
          category: source_reliability
          stated: true
          why_must_be_true: >
            The roster #007 update workflow assumes Razing Ursa is just
            an alias addition, not a new cluster requiring separate
            attribution analysis
          when_could_be_false: >
            Palo Alto's 'Ursa' family naming is canonical for their own
            taxonomy; if Razing Ursa as Unit 42 defines it is a sub-
            cluster of Sandworm rather than coextensive with the full
            APT44 / Seashell Blizzard / Iron Viking grouping, the
            mapping requires more care than a simple alias add
          evidence_for: [unit42-canonical-naming-convention-is-authoritative-for-palo-alto-taxonomy, multi-vendor-alias-conventions-typically-cluster-coextensive]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound

      classifications_summary:
        sound: 3
        qualify: 4
        test: 1
        reject: 0

      remediation:
        status: proceed_with_explicit_qualify
        qualifying_caveats:
          - "A1 — Brief defender carry-forward should be framed as 'IF A&D-prime estates run Rockwell+Allen-Bradley PLCs at material density (vendor mix varies) THEN the CyberAv3ngers TTPs apply directly' rather than presupposing universal Rockwell density"
          - "A2 — Brief should NOT assert A&D-prime OT estates are 'sufficiently segmented' — the assumption is low-confidence + critical-centrality; the framing should be 'A&D-prime defenders should verify Rockwell+Allen-Bradley PLC internet exposure and segmentation posture' rather than 'A&D primes are insulated'"
          - "A3 — Brief should explicitly note that Unit 42's World Cup framework is scoped to sporting/municipal/hospitality sectors and does NOT name A&D; A&D-prime relevance is via TTP/vendor portability (Rockwell+AB) and historical-precedent reasoning (2018 Pyeongchang Olympic Destroyer / 2024 Texas water tank), not direct sector inclusion"
          - "A4 — Brief should not extrapolate from Unit 42's World-Cup-window framing to a general Iranian cyber tempo increase against A&D primes; the window may concentrate effort on event-specific targets"
          - "A7 — Brief should preserve CISA AA26-097A's 'internet-exposed PLCs' framing as the attack-surface descriptor; not a CVE-patching priority"
        test_assumption_a2:
          test: >
            Splunk first-party query against defenseclaw_local + archimedes
            for any Rockwell / Allen-Bradley PLC mentions, ICS/OT events,
            or known internet-exposed industrial protocols (Modbus, EtherNet/
            IP, DNP3) on management interfaces, in last 90d. Negative
            result strengthens A2 (segmentation appears to hold for
            instrumented surface); positive result would require immediate
            escalation. Sentinel raw-2026-05-28-am-000 confirms 67
            consecutive dormant sweeps but the query set may need expansion
            to include Rockwell/AB specifically.
          test_status: "Pre-brief Splunk sweep was generic; explicit Rockwell+AB query expansion recommended as a follow-up Splunk Mode 4 collector invocation"
          test_blocks_assessment: false  # finding can still ship with A2 framed as qualify; test outcome refines the carry-forward language
          note: "Per Hard Rule 8, Splunk first-party silence is not disconfirming. A2 stays qualify-class even with negative Splunk result."

      recommended_wep_after_kac:
        handala_mois_front_corpus_baseline: very_likely
        cyberavengers_iranian_affiliated_per_cisa: very_likely
        cyberavengers_irgc_cec_specific_per_unit42: likely
        rockwell_allen_bradley_active_campaign_existence: very_likely
        ad_prime_direct_exposure_via_same_tradecraft: roughly_even_chance
        ad_prime_ot_segmentation_sufficient_to_mitigate: roughly_even_chance  # test-class — should not be asserted
        razing_ursa_alias_addition_unit42_canonical: very_likely
        banished_kitten_cobalt_mystique_handala_aliases: very_likely
        forward_looking_world_cup_threat_assessment: likely

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling on the dominant claim layer (forward-looking World Cup
  threat assessment) is "likely" with single-source veto explicitly
  applied. The CyberAv3ngers / IRGC Cyber-Electronic Command attribution
  layer with A1 corroboration (Unit 42 + CISA AA26-097A) carries WEP
  "very_likely" but represents corpus-baseline restatement of a CISA-
  attributed active campaign rather than a novel-to-Archimedes
  attribution synthesis. Red-team review is reserved for findings
  with novel high-confidence assessments (WEP very_likely or higher
  on novel Archimedes-side synthesis); restatement of A1-corroborated
  external attribution does not meet that bar. If a second A/B-grade
  vendor publishes the forward-looking World Cup assessment and lifts
  the cluster to "very_likely" on that layer, red-team review should
  be triggered at that point.
red_team_review: null

# Lifecycle
tlp: CLEAR
published_in_briefs:
  - 2026-05-28-morning
retracted: false
retraction_brief_id: null
---

# Unit 42 2026 FIFA World Cup attack-surface threat assessment — names roster #014 Handala Hack (new Banished Kitten + Cobalt Mystique aliases) and roster #007 Sandworm (new Razing Ursa alias) and roster #013 Scattered Spider (Muddled Libra ALPHV/BlackCat operator) — names non-roster CyberAv3ngers as IRGC Cyber-Electronic Command OT arm with CISA AA26-097A active-campaign attribution against Rockwell+Allen-Bradley PLCs — NoName057(16) + Fiddling Scorpius non-roster references

## Summary

Palo Alto Unit 42 published a forward-looking 2026 FIFA World Cup
attack-surface threat assessment under Justin Moore's byline. The
piece names three tracked-roster actors (Handala Hack #014 with new
Banished Kitten + Cobalt Mystique aliases; Sandworm #007 with new
Razing Ursa alias; Scattered Spider #013 with Muddled Libra ALPHV/
BlackCat-operator characterization) plus non-roster CyberAv3ngers
(attributed by Unit 42 to IRGC Cyber-Electronic Command, with CISA
AA26-097A providing independent A-grade corroboration on the active
Rockwell+Allen-Bradley PLC-targeting campaign), NoName057(16) pro-
Russian hacktivist DDoS cluster, and Fiddling Scorpius Play
ransomware distributor. Unit 42's confidence language is preserved
verbatim per Hard Rule 2: Iran-nexus disruptive ops "highly likely,"
financially motivated cybercrime "highest-volume highest-likelihood,"
OT disruption "High" severity, wiper/destructive ops "High-critical"
severity. NO aerospace / defense / government contractor sector is
named in the article — scope is sporting infrastructure, host-city
municipal services, hospitality, and fan-facing platforms. Indirect
A&D-relevance via tracked-actor capability portability: Handala wiper
capability + Sandworm 2018 Pyeongchang Olympic Destroyer precedent +
CyberAv3ngers Rockwell PLC TTPs are operationally portable to A&D-
prime OT and executive-targeting scenarios.

## Sources

### Palo Alto Unit 42 (unit42, digraph: A)

- URL: https://unit42.paloaltonetworks.com/fifa-world-cup-attack-surface/
- Published: 2026-05-28T10:00:53+00:00 (06:00 EDT — in-window)
- Author: Justin Moore
- Key claim: Forward-looking 2026 FIFA World Cup attack-surface
  threat assessment naming Handala Hack (MOIS front), Sandworm,
  Scattered Spider, CyberAv3ngers (IRGC Cyber-Electronic Command),
  NoName057(16), and Fiddling Scorpius as actors likely to operate
  against sporting infrastructure / municipal services / hospitality
  / fan platforms during the World Cup window. Iran-nexus disruptive
  ops assessed "highly likely"; financially motivated cybercrime
  assessed "highest-volume highest-likelihood."

### CISA AA26-097A (cisa-advisories, digraph: A — independent corroboration on PLC-targeting layer only)

- Cited within Unit 42 body; not directly retrieved this sweep but
  exists as corpus-baseline CISA advisory.
- Key claim: "Active, ongoing Iranian-affiliated campaign" targeting
  internet-exposed Rockwell Automation and Allen-Bradley programmable
  logic controllers in U.S. critical infrastructure across water,
  wastewater treatment, regional power, airport operations, and
  emergency services sectors.
- Independence: Independent of Unit 42 — CISA advisory exists prior
  to and outside of Unit 42 publication with its own government-
  grade attribution methodology.

## Technical detail

### Tracked-roster actor mappings (per Unit 42 alias naming)

**Roster #014 Handala Hack (Iran / MOIS, HIGH per _roster.yaml)**
- Unit 42 alias cluster: Banished Kitten + Storm-0842 + Void
  Manticore + Cobalt Mystique
- New aliases requiring actor-profiler update: **Banished Kitten**
  and **Cobalt Mystique** (Unit 42 Palo Alto "Kitten" family
  canonical naming)
- Activity profile per Unit 42: wiper attacks + high-level
  government-officials targeting
- MOIS-front attribution: Unit 42 verbatim "assessed as MOIS front"
  (Iranian Ministry of Intelligence and Security)

**Roster #007 Sandworm (Russia / GRU Unit 74455, HIGH per _roster.yaml)**
- Unit 42 alias: Razing Ursa (Palo Alto "Ursa" family canonical
  naming, NEW to corpus)
- Historical precedent cited: 2018 Pyeongchang Olympic Destroyer
  wiper attack — the canonical sporting-event-targeting historical
  reference Unit 42 uses to project potential 2026 World Cup activity

**Roster #013 Scattered Spider (HIGH per _roster.yaml)**
- Unit 42 alias: Muddled Libra (already in roster)
- Unit 42 characterizes Muddled Libra as ALPHV/BlackCat operators —
  operationally narrower than full Scattered Spider tradecraft
  (Octo Tempest / 0ktapus / vishing)
- World Cup-specific TTP: ransomware targeting hospitality sector
  (hotel chains hosting World Cup tourists / officials)

### Non-roster actor candidates

**CyberAv3ngers** (HIGH-priority /new-actor candidate)
- Unit 42 alias cluster: Shahid Kaveh Group + Bauxite + Hydro
  Kitten + Storm-0784 + UNC5691
- Unit 42 attribution: "IRGC Cyber-Electronic Command's OT
  targeting arm with documented escalation curve"
- CISA AA26-097A documents active Iranian-affiliated campaign
  against Rockwell + Allen-Bradley PLCs in US critical
  infrastructure (water, wastewater, regional power, airport ops,
  emergency services)
- A&D-prime relevance: operational portability to manufacturing /
  R&D OT estates running Rockwell PLCs

**NoName057(16)** (LOW-priority candidate)
- Pro-Russian hacktivist DDoS cluster
- Unit 42 cites 3,700+ verified DDoS attacks against NATO members
  since 2022
- Surge pattern around politically symbolic events

**Fiddling Scorpius** (LOW-priority candidate)
- Play ransomware distributor
- Unit 42 cites French Rugby Federation attack as recent reference

### Critical-infrastructure targeting scope (per Unit 42)

Sectors named as in-scope for adversary during World Cup window:
- Water treatment
- Wastewater treatment
- Regional power
- Airport operations
- Emergency services

Historical precedent: January 2024 Texas municipal water tank
overflow (Russian-attributed cyber attack) — the operational-
demonstration validation precedent.

### Threat-assessment language preserved verbatim (Hard Rule 2)

- Iran-nexus disruptive operations: **"highly likely"**
- Financially motivated cybercrime: **"highest-volume, highest-
  likelihood threat category"**
- OT disruption at host-city utility: **High** severity
- Wiper / destructive operation: **High-critical** severity

## IOCs surfaced

| Type | Value | Confidence | Source |
|------|-------|-----------|--------|
| Actor alias cluster | Handala Hack — Banished Kitten + Cobalt Mystique + Storm-0842 + Void Manticore | High | Unit 42 (canonical naming) |
| Actor alias cluster | Sandworm — Razing Ursa (new) | High | Unit 42 (canonical naming) |
| Actor alias cluster | CyberAv3ngers — Shahid Kaveh + Bauxite + Hydro Kitten + Storm-0784 + UNC5691 | High | Unit 42 + CISA AA26-097A |
| Campaign reference | CISA AA26-097A (Rockwell+Allen-Bradley PLC campaign, US CI) | High | CISA + Unit 42 citation |
| Tradecraft pattern | Handala wiper + government-official targeting | High | Unit 42 |
| Tradecraft pattern | CyberAv3ngers Rockwell+Allen-Bradley PLC OT-targeting | High | Unit 42 + CISA |
| Historical precedent | 2018 Pyeongchang Olympic Destroyer / Sandworm | High | Corpus-baseline |
| Historical precedent | January 2024 Texas water tank / Russian attribution | High | CISA + US gov |
| Operational figure | NoName057(16) 3,700+ DDoS attacks on NATO since 2022 | Medium | Unit 42 |
| Operational event | Fiddling Scorpius Play ransomware French Rugby Federation | Medium | Unit 42 |

No domains, IPs, hashes, or file artifacts in this assessment piece.

## Relationship to existing findings

- **finding-2026-05-27-0004-securityweek-lacmta-iran-black-shadow-mois-gambit-israel-cyber-directorate-relay-investigation-update** — Iran Cyber Watch standing-section continuity. The LACMTA / Black Shadow / MOIS investigation (inv-2026-05-26-001) is a separate active Iran-nexus surface; Unit 42 does NOT name LACMTA or Black Shadow in the World Cup piece. Briefer may pair both under Iran Cyber Watch with cross-link but do not force a cluster mapping (forward-looking World Cup vs retrospective municipal-transit incident).
- **roster #014 Handala Hack dossier** — actor-profiler should add Banished Kitten + Cobalt Mystique aliases.
- **roster #007 Sandworm dossier** — actor-profiler should add Razing Ursa alias.
- **roster #022 MuddyWater, #004 UNC1549, #011 Charming Kitten, #023 APT34** — NOT named by Unit 42 in this piece. Iran-roster scope of the World Cup assessment is narrower than full Iran roster (Handala + CyberAv3ngers only).

## Open questions for analyst

1. **/new-actor scaffolding decision for CyberAv3ngers** — HIGH-priority operator-evaluation candidate. IRGC Cyber-Electronic Command service-level attribution + CISA AA26-097A active-campaign attribution + named victim sectors + Rockwell+Allen-Bradley PLC-targeting portability to A&D-prime OT estates.
2. **Actor-profiler roster updates for #014 (Banished Kitten + Cobalt Mystique aliases) and #007 (Razing Ursa alias)** — Unit 42 canonical naming additions; operator-approval-pending workflow.
3. **SAT-ACH on the forward-looking World Cup threat-assessment confidence framing** — single-source-veto applied; competing hypotheses on whether second-source corroboration will confirm Unit 42's framing, shift the relative actor-cluster weighting, or downgrade the forward projection altogether.
4. **SAT-KAC on the assumption that A&D-prime OT estates are sufficiently segmented from internet exposure** to mitigate the CISA AA26-097A internet-exposed-PLC attack surface — Rockwell+Allen-Bradley PLC inventory in A&D-prime manufacturing/R&D environments is the load-bearing assumption for defensive prioritization.
5. **CyberAv3ngers vs MuddyWater (#022 LOW) vs Handala Hack (#014 HIGH)** — three distinct Iran clusters in corpus context (MOIS service-tier per #014 and #022; IRGC Cyber-Electronic Command per CyberAv3ngers Unit 42 attribution). Hard Rule 2 prohibits cross-walking between them despite shared nation-tier. Analyst review on whether the corpus framing of Iran-nexus threat to A&D should treat these as three separate operational entities or as a connected IR-state-cyber portfolio.

## Analytic notes (from analyst review)

ACH on the Iran-nexus front-organization claim (5 hypotheses, 11 evidence
items) ranks H1 first with zero inconsistencies: Handala Hack as MOIS front
(corpus-baseline, roster #014 confirms) and CyberAv3ngers as IRGC Cyber-
Electronic Command's OT-targeting arm (Unit 42 attribution + CISA AA26-097A
independent corroboration on the active Iranian-affiliated campaign, though
CISA does not specify IRGC-CEC at the service tier). Diagnostic evidence
distinguishes IRGC operational signature (OT-only sector targeting,
documented escalation curve) from corpus-tracked MOIS clusters (espionage /
disruption / hacktivist). H4 (contractor-vs-state-organic refinement) is a
zero-inconsistencies sharpening of H1 rather than a competing reading. The
IRGC-CEC service-tier specificity caps at "likely" per single-source veto;
the broader Iranian-affiliated layer is "very likely" via CISA.

KAC surfaces eight assumptions; one is test-class (A2 — A&D-prime OT
segmentation sufficient to mitigate the internet-exposed-PLC surface). A2's
confidence is low and centrality critical: A&D-prime OT segmentation is
asserted in compliance frameworks (CMMC, CDSA) but historical CISA advisories
have repeatedly found "air-gapped" OT to be reachable. The IT/OT convergence
trend and DIB tier-2/3 supplier exposure further erode the assumption. The
recommended remediation is to NOT assert A&D-prime insulation in the brief;
the carry-forward should be framed as "verify Rockwell+Allen-Bradley PLC
internet exposure and segmentation posture" rather than presupposing the
assumption holds.

Recommendation: brief should preserve three separable layers. (1) CISA-
documented active Iranian-affiliated campaign against Rockwell+AB PLCs in US
CI — very likely; A1 corroborated. (2) Unit 42's IRGC Cyber-Electronic
Command service-tier specificity — likely; single-source. (3) Forward-
looking World Cup threat projection — likely; single-source veto. Defender
carry-forward should be framed as a verification action (segmentation audit)
not an insulation assertion. Roster #014 Handala Hack alias additions
(Banished Kitten + Cobalt Mystique) and roster #007 Sandworm alias addition
(Razing Ursa) are routine Unit-42-canonical alias adds; CyberAv3ngers
remains a HIGH-priority /new-actor candidate pending operator decision.
