---
finding_id: finding-2026-05-26-0007-checkpoint-research-unc1549-nimbus-manticore-fast-and-furious-operation-epic-fury-primary-26-ioc
created_at: 2026-05-26T16:00:00-04:00
graded_by: grader
grading_run_id: afternoon-20260526-160000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: A2
digraph_layered:
  ckr_primary_originating_publication_in_corpus_first_time: A2
  minifast_16_opcode_capability_matrix_full_drop: A2     # CKR primary + Unit 42 concurrent corroborate tradecraft family
  appdomain_hijacking_trojanized_xml_config_specifics: A2
  zoom_scheduled_task_hijack_zoomupdatetaskuser_persistence: A2
  windows_security_update_scheduled_task_name: A2
  sslsign_certificate_abuse_gray_matter_kirubel_subjects: A2  # CKR-only on specific subjects
  operation_epic_fury_us_military_feb_28_2026_anchor: A3  # CKR analytical campaign-naming, single-source
  unc1549_subgroup_of_charming_kitten_apt35_relation_novel_framing: A3  # CKR-only, novel-to-corpus relation
  bohrium_ta455_alias_set_expansion: A3  # CKR-only on these aliases vs corpus roster
  us_aviation_explicit_targeting_ckr_primary_quote: A2  # CKR primary text supports; named airline impersonation lures (no prime named)
  ai_assisted_malware_development_indicators_ckr_inference: B3  # single-vendor analytical inference, corpus-baseline carry-forward from finding-0001
  iran_irgc_attribution_corpus_baseline_restated: A1
  industrial_cyber_relay_aerospace_editorialization_drift_flagged: B3  # relay-introduced framing not in CKR primary
  securityweek_relay_aviation_software_framing_consistent_with_primary: B2
  splunk_first_party_zero_hits_8h_window_targeted_iocs: A1
  cluster_anchor: A2

digraph_anchor: >
  Cluster digraph A2 anchored on Check Point Research primary publication
  "Fast and Furious - Nimbus Manticore Operations During the Iranian
  Conflict" (2026-05-22, https://research.checkpoint.com/2026/fast-and-
  furious-nimbus-manticore-operations-during-the-iranian-conflict/) which
  surfaces in the Archimedes corpus directly for the first time today via
  SecurityWeek (Ionut Arghire) and Industrial Cyber (Anna Ribeiro) PM-
  window relays. CKR carries provisional A per source-grades cheatsheet
  category "vendor research blog with multi-cycle cross-corroboration
  established" (recommend librarian formalize via source-grade-log
  entry). The independent-corroboration test passes at the vendor-
  research-pair layer: CKR primary + Palo Alto Networks Unit 42's
  2026-05-22 concurrent publication on the same UNC1549 cluster
  (different parent orgs, different telemetry, different naming
  taxonomies - CKR's "Nimbus Manticore" vs Unit 42's "Screening
  Serpens / Smoke Sandstorm") are genuinely independent A-grade vendor
  research on overlapping but taxonomically distinct cluster mappings.
  Credibility 2 (Probably True) holds across the corroborated tradecraft
  layer. Single-source veto applies LAYERED on three CKR-only analytical
  claims: Operation Epic Fury campaign-naming + US military Feb 28
  anchor (A3); UNC1549 subgroup-of-Charming-Kitten relation (A3, novel
  framing to corpus roster); Bohrium + TA455 alias additions to the
  UNC1549 set (A3). These three CKR-only claims cap WEP at "likely".
  The corroborated tradecraft layer (MiniFast capability matrix,
  AppDomain hijacking specifics, Zoom scheduled-task hijack) reaches
  WEP "very likely" via the CKR+Unit42 corroboration. Iran/IRGC
  attribution is corpus-baseline (actor #004) - restated, not
  originated. This finding is a SIBLING to finding-2026-05-26-0001
  (THN-relay anchor): both findings cover the UNC1549 2026 tradecraft-
  evolution surface, with 0001 anchored on THN editorial relay and
  0007 anchored on CKR originating primary. The CKR primary URL plus
  the full 26 SHA256 + 26 domain IOC drop are net-new to corpus.

source_reliability:
  grade: A
  source_name: "Check Point Research (primary publication)"
  source_yaml_id: checkpoint-research
  grade_rationale: >
    Provisional A per source-grades-cheatsheet.md category "vendor
    research blog" - multi-cycle cross-corroboration cycle established
    in corpus (2026-04-02 UNC1549 corpus seed, 2026-05-09 carry-forward,
    2026-05-22 Fast-and-Furious primary, 2026-05-26 AM-26 finding-0002
    AI Threat Landscape Digest, 2026-05-26 PM-26 this finding). CKR is
    the originating vendor for the Nimbus Manticore cluster designation.
    Surfaces in this finding via direct primary URL (vs the AM-26
    finding-0001 THN-relay anchor). Recommend librarian formalize
    checkpoint-research entry in source-grades.yaml at grade A on next
    librarian pass given the now-multiple-cycle corpus track record.
  provisional: true
  source_grade_revision_proposed:
    source_yaml_id: checkpoint-research
    current_grade: provisional_A_via_cheatsheet
    proposed_grade: A_formalized
    reason: "Multiple-cycle cross-corroboration established; provisional A held across 2026-04-02, 2026-05-22, 2026-05-26 corpus surfaces; recommend formalization in source-grades.yaml"
    severity: formalization_not_downgrade
    action: "Librarian add to source-grades.yaml on next pass per source-grade-log convention"
  in_window_relays:
    - vendor_name: "SecurityWeek (Ionut Arghire relay)"
      vendor_yaml_id: securityweek
      vendor_grade: B
      publication: "Iranian APT Targets Aviation, Software Companies With Updated Tools"
      publication_at: 2026-05-26T13:26:17+00:00
      sector_framing: "aviation + software (consistent with CKR primary 'aviation' framing)"
    - vendor_name: "Industrial Cyber (Anna Ribeiro relay)"
      vendor_yaml_id: industrialcyber-co
      vendor_grade: B
      publication: "IRGC-linked Nimbus Manticore group attacks defense, aerospace, telecom sectors using Minifast malware toolkit"
      publication_at: 2026-05-26T00:00:00+00:00
      sector_framing: "defense, aerospace, telecom (RELAY-INTRODUCED 'aerospace' not in CKR primary text; CKR uses 'aviation')"
      relay_drift_flag: true
  underlying_corroborating_primary:
    vendor_name: "Palo Alto Networks Unit 42"
    vendor_yaml_id: unit42
    vendor_grade: A
    publication: "MiniUpdate / MiniJunk V2 / AppDomainManager tradecraft (concurrent)"
    publication_date: 2026-05-22
    relation_to_ckr: "Independent vendor research concurrent on overlapping campaign; different telemetry; different cluster-naming taxonomies (Screening Serpens / Smoke Sandstorm vs Nimbus Manticore)"

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_ttps_or_known_campaign_timing_targeting
    - probably_true_no_contradicting_evidence_from_ab_grade_sources
    - probably_true_technical_claims_internally_coherent
  grade_1_test:
    - independent_corroboration_present_yes: "CKR + Unit 42 2026-05-22 concurrent are genuinely independent vendor research"
    - neither_cites_other_origin_yes: "CKR does not cite Unit 42; Unit 42 does not cite CKR (concurrent publication pattern)"
    - technical_artifacts_match_across_sources_partial: "Tradecraft overlap (AppDomain hijacking, MiniFast/MiniUpdate family, Zoom installer trojanization, SEO poisoning) is consistent; specific IOC hashes are CKR-side only at this surface; Unit 42 IOC list not directly fetched this sweep"
    - no_contradicting_higher_grade_source_yes: "Mandiant + Microsoft MSTIC corpus history all consistent with Iran/IRGC attribution and aviation/defense/telecom sectoral pattern"
    - grade_1_blocked_by: "Technical artifact match is PARTIAL (tradecraft yes, specific IOC hashes not directly cross-walked Unit 42 vs CKR this sweep). Grade 1 requires full match. Held at 2."
  rationale: >
    Consistent with established UNC1549 / Nimbus Manticore TTPs in
    corpus baseline. Three-campaign breakdown (Rising Tension February
    2026, Operation Epic Fury post-February 28 2026, SQL Developer
    April 2026) is consistent with the actor's known post-geopolitical-
    escalation operational tempo. AppDomain hijacking via trojanized
    .config files pointing to AppDomainManager classes is a documented
    .NET DLL-loading abuse pattern (MITRE T1574 family). Zoom
    ZoomUpdateTaskUser-SID scheduled-task hijacking is a documented
    living-off-the-land persistence pattern. MiniFast 16-opcode
    capability matrix is internally coherent and consistent with the
    abstract-MiniFast-description carried forward from finding-0001.
    SSL.com certificate abuse with two distinct subjects (Gray Matter
    Software S.R.L., Kirubel Kerie Negeya) is a documented code-signing-
    abuse class for Iran-nexus actors. AI-assisted malware development
    indicators (excessive error handling, repetitive function naming,
    embedded debug messages, modular code organization) carry the same
    single-vendor analytical-inference caveat flagged in finding-0001.
    No contradicting evidence from A/B-grade sources.

corroboration:
  independent_sources:
    - checkpoint-research      # originating primary (2026-05-22)
    - unit42                   # concurrent corroborating primary (2026-05-22)
    - securityweek             # in-window B-grade relay (2026-05-26 09:26 EDT)
    - industrialcyber-co       # in-window B-grade relay (2026-05-26 byline today)
  independent: true
  test_passed: >
    CKR and Unit 42 are genuinely independent vendor research
    organizations (Check Point Software Technologies vs Palo Alto
    Networks; different telemetry sources; different cluster-naming
    taxonomies - CKR's Nimbus Manticore vs Unit 42's Screening Serpens
    / Smoke Sandstorm). Their 2026-05-22 concurrent publications cover
    overlapping but taxonomically distinct mappings of the same UNC1549
    campaign cluster. SecurityWeek and Industrial Cyber relays do NOT
    add independent corroboration - they aggregate CKR. The vendor-
    research-pair (CKR + Unit 42) carries the corroboration weight.
  relay_drift_flag: >
    Industrial Cyber's relay editorializes CKR's "aviation" sector
    framing to "aerospace, aviation, telecom". CKR primary text uses
    "defense, aviation and telecommunication" - no "aerospace" in the
    primary. For an A&D-prime target audience, the distinction between
    commercial aviation (airlines, with which CKR's US-domestic-airline
    impersonation lures are consistent) and aerospace (manufacturers
    including Boeing/Airbus/Lockheed) is material. Industrial Cyber's
    editorialization may overstate the A&D-prime targeting signal.
    The grader propagates CKR's "aviation" framing in this finding;
    the relay's "aerospace" framing is flagged for analyst SAT review.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    PM pre-brief sweep included a -8h@h query against defenseclaw_local
    and archimedes covering MiniFast, MiniJunk, Nimbus Manticore,
    UNC1549, AppDomain, Smoke Sandstorm, Bohrium, TA455, 157.20.182.49,
    fmapp.exe/dll, sentinelmemoryscanner/agentcore, ChromElevator,
    FileFiend, Charming Kitten, APT35, plus the four PM in-window CVE
    strings (48172, 45659, 9082, 42897). Zero events returned. 61st+
    consecutive dormant non-self sweep on defenseclaw_local. Hard
    Rule 8: silence is not disconfirming.

single_source_veto_applied: true
single_source_veto_rationale: >
  Veto applies LAYERED on three CKR-only analytical claims:
  (1) "Operation Epic Fury" campaign-naming with "US military campaign
  against Iran launched on February 28, 2026" anchor - CKR-only
  analytical framing. WEP capped at "likely".
  (2) "Nimbus Manticore is believed to be a subgroup of Charming Kitten
  (APT35)" relation - CKR-only, novel framing relative to corpus
  _roster.yaml which has #004 (UNC1549) and #011 (Charming Kitten)
  as separate entries with no subgroup relation documented. WEP capped
  at "likely". Flagged for actor-profiler review.
  (3) Bohrium + TA455 aliases as members of the UNC1549 alias set -
  CKR-only on these specific aliases vs corpus roster which currently
  lists UNC1549 aliases as Tortoiseshell, Smoke Sandstorm, Imperial
  Kitten, Crimson Sandstorm. WEP capped at "likely". Flagged for
  actor-profiler review on alias-set expansion.
  Corroborated tradecraft layer (MiniFast 16-opcode matrix, AppDomain
  hijacking via .config files, Zoom ZoomUpdateTaskUser-SID scheduled-
  task hijack, SEO poisoning + getsqldeveloper.com, trojanized Zoom
  installer initial access) reaches WEP "very likely" via CKR + Unit 42
  corroboration. WEP not capped at this layer.

wep_ceiling: very_likely
wep_layered:
  unc1549_iran_irgc_attribution_corpus_baseline: not_a_new_claim   # already-established
  ckr_primary_publication_now_in_corpus_directly: very_likely      # procedural
  minifast_16_opcode_capability_matrix: very_likely                # corroborated by Unit 42 tradecraft family
  appdomain_hijacking_via_trojanized_xml_config_specifics: very_likely
  zoom_scheduled_task_hijack_zoomupdatetaskuser_persistence: very_likely
  ssl_com_certificate_abuse_gray_matter_kirubel_subjects: likely  # CKR-only on specific subjects (no contradicting source but no independent corroboration on subjects)
  operation_epic_fury_us_military_feb_28_2026_campaign_anchor: likely    # single-source CKR analytical framing
  unc1549_subgroup_of_charming_kitten_apt35_relation: likely        # single-source CKR novel framing
  bohrium_ta455_aliases_addition_to_unc1549_set: likely              # single-source CKR novel framing
  us_aviation_explicit_targeting_per_ckr_quote: very_likely           # CKR primary supports; US-domestic airline impersonation lures concrete
  industrial_cyber_relay_aerospace_editorialization: roughly_even_chance  # relay-introduced framing not in primary
  ai_assisted_malware_development_indicators: roughly_even_chance    # single-vendor analytical inference (carry-forward from finding-0001)
  twenty_six_sha256_plus_twenty_six_domain_ioc_set: very_likely     # vendor-published IOCs

inclusion:
  eligible_for:
    - daily_brief_action
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update
    - vuln_tracker_consideration_no_cve_class
    - ioc_master_index_propagation
  not_eligible_for:
    - flash               # FLASH-POLICY anti-noise lock active through 2026-05-27 08:00 EDT (24h from AM-26 morning brief publication); CKR primary URL surfacing is corpus-extension on the locked surface, not new attribution; brief-tier coverage is the correct disposition
  inclusion_rationale: >
    A2 cluster anchor on the CKR primary publication directly surfacing
    in corpus for the first time, with net-new material (26+26 IOC drop,
    Operation Epic Fury campaign framing, full MiniFast 16-opcode
    matrix, AppDomain hijacking specifics, SSL.com certificate abuse
    subjects, three CKR-only analytical claims). Eligible for PM-26
    afternoon brief action item per INTEL-GRADING.md thresholds. UNC1549
    actor #004 dossier last-reviewed 2026-05-09 (threat level MEDIUM
    weighted 5.4; Espionage category HIGH composite 10) - the CKR
    primary's alias-set expansion (Bohrium, TA455) and the subgroup-of-
    Charming-Kitten relation framing warrant actor-profiler dossier
    update review. NOT FLASH-eligible per anti-noise lock active on the
    UNC1549 surface through 2026-05-27 08:00.

# Cluster metadata
cluster:
  topic: "UNC1549 / Nimbus Manticore Check Point Research primary publication 'Fast and Furious - Nimbus Manticore Operations During the Iranian Conflict' (2026-05-22) surfaces in corpus directly via PM-26 in-window B-grade relays (SecurityWeek + Industrial Cyber); net-new corpus material includes 26 SHA256 + 26 domains IOC drop, Operation Epic Fury campaign framing tied to US military operation Feb 28 2026, full MiniFast 16-opcode capability matrix, AppDomain hijacking via trojanized XML .config files specifics, Zoom ZoomUpdateTaskUser-SID scheduled-task hijack persistence, WindowsSecurityUpdate scheduled-task name, SSL.com certificate abuse (Gray Matter Software S.R.L. + Kirubel Kerie Negeya subjects), AI-assisted malware development indicators (corpus carry-forward), Bohrium + TA455 alias-set expansion, Nimbus Manticore as subgroup of Charming Kitten (APT35) relation framing. US aviation explicit targeting per CKR primary quote with US-domestic-airline impersonation lures (specific airline unnamed). Sector framing fidelity: CKR primary 'aviation' vs Industrial Cyber relay 'aerospace' - relay drift flagged."
  cluster_size: 1                    # single PM raw-signal item, but it carries the CKR primary URL into corpus directly with the full IOC drop
  raw_signal_members:
    - raw-2026-05-26-pm-001-checkpoint-research-unc1549-nimbus-manticore-fast-and-furious-operation-epic-fury-aviation-aerospace-26-ioc-primary-surface
  related_actors:
    - "004"                          # UNC1549 (primary)
    - "011"                          # Charming Kitten (related via CKR-claimed subgroup relation; flagged for actor-profiler review)
  related_vulnerabilities: []         # No CVE in this cluster; UNC1549 ops are post-exploit / supply-chain phishing class
  related_campaigns:
    - unc1549-nimbus-manticore-2026-active-campaign
    - operation-epic-fury-2026                          # net-new CKR-named campaign anchor
    - campaign-1-rising-tension-2026                    # CKR Campaign 1 breakdown
    - campaign-3-sql-developer-april-2026               # CKR Campaign 3 breakdown
  sibling_finding:
    finding_id: finding-2026-05-26-0001-unc1549-nimbus-manticore-minifast-minijunk-v2-seo-poisoning-getsqldeveloper
    relation: |
      Finding 0007 is a SIBLING (not an update or replacement) of
      finding-0001. Both findings cover the UNC1549 2026 tradecraft-
      evolution surface. 0001 is anchored on The Hacker News editorial
      relay (B2 cluster anchor; THN published 2026-05-26 03:13 EDT).
      0007 is anchored on the Check Point Research originating primary
      (A2 cluster anchor; CKR published 2026-05-22 surfaced in PM-26
      window via SecurityWeek + Industrial Cyber B-grade relays). The
      direct retrieval of the CKR primary URL upgrades the corpus
      treatment from B2 (relay) to A2 (originating primary) on the same
      tradecraft surface. 0001's open analyst question "naming taxonomy
      reconciliation - does CKR's MiniFast == Unit 42's MiniUpdate" is
      partially answered by 0007: CKR's MiniFast capability matrix is
      now in corpus directly; Unit 42 primary direct fetch in a
      subsequent sweep would close the question. 0001's anti-noise lock
      "unc1549-screening-serpens-tradecraft-evolution-2026" continues
      to govern this surface through 2026-05-27 08:00 EDT.
  attribution_claims:
    - claimed_actor: "UNC1549 / Nimbus Manticore"
      claimed_actor_roster_id: "004"
      claimed_by_sources: [checkpoint-research, unit42, securityweek, industrialcyber-co]
      attribution_specificity: >
        Iran-nexus, IRGC-affiliated per CKR primary verbatim language
        "Iranian, IRGC affiliated, threat actor Nimbus Manticore" (no
        formal "high confidence" qualifier). Corpus-baseline per
        _roster.yaml actor #004.
      hard_rule_2_treatment: >
        Corpus-baseline attribution preserved. CKR primary is the
        originating source for the Nimbus Manticore designation;
        Archimedes does not originate attribution - propagates CKR's
        framing without elevation.
      requires_analyst_review: false
    - claimed_actor: "UNC1549 alias-set expansion"
      claimed_actor_roster_id: "004"
      claimed_by_sources: [checkpoint-research]
      attribution_specificity: >
        CKR primary lists Nimbus Manticore aliases as: UNC1549 (Mandiant
        originating cluster naming), Bohrium (CKR-side novel addition to
        corpus), Smoke Sandstorm (corpus-baseline), TA455 (CKR-side
        novel addition to corpus). Current _roster.yaml #004 alias set:
        Tortoiseshell, Smoke Sandstorm, Imperial Kitten, Crimson
        Sandstorm. CKR adds Bohrium + TA455 + Nimbus Manticore (where
        Imperial Kitten + Crimson Sandstorm + Tortoiseshell are NOT
        named in CKR primary).
      hard_rule_2_treatment: >
        Alias-set expansion is reportage of a single A-grade vendor's
        framing - not Archimedes attribution origination. Flagged for
        actor-profiler review to harmonize the corpus roster alias set
        with CKR's published set.
      requires_analyst_review: true
      requires_actor_profiler_review: true
    - claimed_actor: "UNC1549 as subgroup of Charming Kitten (APT35)"
      claimed_actor_roster_id: "004 + 011 relation"
      claimed_by_sources: [checkpoint-research]
      attribution_specificity: >
        CKR primary verbatim: "believed to be a subgroup of Charming
        Kitten (APT35)". This is a NOVEL framing to corpus - _roster.yaml
        has #004 (UNC1549) and #011 (Charming Kitten) as separate
        entries with no subgroup relation documented. Other vendor
        research (Mandiant, Unit 42, Microsoft MSTIC) has historically
        treated UNC1549 and Charming Kitten as separate Iran-nexus
        clusters with non-overlapping operational signatures.
      hard_rule_2_treatment: >
        Subgroup-relation claim is reportage of single CKR analytical
        framing - Archimedes does not originate the relation. Single-
        source veto applies on the relation claim - WEP "likely" not
        "very likely". Flagged for actor-profiler review on whether
        to (a) add CKR-claimed relation to _roster.yaml as analyst-
        flagged-pending-corroboration, (b) hold roster at status quo
        until second A/B-grade source publishes corroborating relation
        framing, or (c) update both #004 and #011 dossiers with
        cross-references and CKR-claimed relation note.
      requires_analyst_review: true
      requires_actor_profiler_review: true

# IOCs surfaced (full CKR primary IOC drop now in corpus)
iocs_surfaced:
  - type: domain
    value: business-startup[.]org
    context: "Nimbus Manticore C2 / phishing infrastructure - Operation Epic Fury Campaign 2 apex domain"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    related_campaign: operation-epic-fury-2026
    defanged: true
  - type: domain
    value: getsqldeveloper[.]com
    context: "SEO-poisoning fake Oracle SQL Developer download site - Campaign 3 SQL Developer April 2026; CKR primary direct (vs finding-0001 THN relay)"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    related_campaign: campaign-3-sql-developer-april-2026
    defanged: true
  - type: domain
    value: buisness-centeral-transportation[.]com
    context: "Apex domain for transportation-themed lure - Operation Epic Fury"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    related_campaign: operation-epic-fury-2026
    defanged: true
  - type: domain
    value: PremierHealthAdvisory[.]com
    context: "Healthcare-themed phishing lure apex"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    related_campaign: operation-epic-fury-2026
    defanged: true
  - type: domain
    value: ramiltonsfinance[.]com
    context: "Finance-themed phishing lure apex"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    related_campaign: operation-epic-fury-2026
    defanged: true
  # Azure-hosted variants (21 azurewebsites.net domains) - full enumeration in raw-signal pm-001 IOC block; condensed reference here
  - type: domain_family
    value: "azurewebsites[.]net hosted Nimbus Manticore staging (21 domains)"
    context: "Twenty-one azurewebsites.net subdomains hosting Nimbus Manticore staging infrastructure - business-startup, businessstartup, buisness-centeral, buisness-centeral-transportation, licencemanagers, licencesupporting, peerdistsvcmanagers, nanomatrix, PremierHealthAdvisory, Premier-HealthAdvisory, ramiltonsfinance, ramiltons-finance, globalitconsultants, globalit-consultants, global-it-consultants, global-it-checkers, global-it-checkbusiness, global-check-itbusiness, global-check-business-it, globalbusiness-checkers-it - see raw-2026-05-26-pm-001 IOC block for full enumeration"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    related_campaign: operation-epic-fury-2026
    defanged: true
    librarian_action_required: "Propagate all 21 azurewebsites.net variants to _master-index.yaml IOC index"
  - type: hash_sha256_family
    value: "26 SHA256 hashes published by CKR primary"
    context: "Full SHA256 IOC drop from CKR primary 'Fast and Furious' Indicators of Compromise section - see raw-2026-05-26-pm-001 for the complete 26-hash enumeration including 10fd541674adadfbba99b54280f7e59732746faf2b10ce68521866f737f1e46d (top of list)"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    related_campaign: unc1549-nimbus-manticore-2026-active-campaign
    defanged: false
    librarian_action_required: "Propagate all 26 SHA256 hashes to _master-index.yaml IOC index"
  - type: file_path
    value: "C:\\Users\\<USER>\\AppData\\Local\\Zoom\\bin\\update"
    context: "MiniFast staging directory; uses Zoom bin/update path for blending with legitimate Zoom client artifacts"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    defanged: false
  - type: scheduled_task
    value: "ZoomUpdateTaskUser-<SID>"
    context: "Hijacks Zoom legitimate update task for MiniFast persistence (corpus-novel persistence specific)"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    defanged: false
  - type: scheduled_task
    value: "WindowsSecurityUpdate"
    context: "Persistence task name impersonating Windows security update routine (corpus-novel)"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    defanged: false
  - type: user_agent
    value: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    context: "MiniFast HTTPS user-agent impersonating Chrome 146 (corpus-novel detection string)"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    defanged: false
  - type: ssl_cert_subject
    value: "Gray Matter Software S.R.L."
    context: "SSL.com-issued code-signing certificate abused (corpus-novel)"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    defanged: false
  - type: ssl_cert_subject
    value: "Kirubel Kerie Negeya"
    context: "SSL.com-issued code-signing certificate abused (corpus-novel; PII restraint noted - subject name appears in CKR primary as code-signing-cert subject only)"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    defanged: false
  - type: c2_api_endpoint_family
    value: "MiniFast C2 REST API: /rg (POST handshake), /agent/init (POST register), /agent/poll?token= (GET task), /agent/result (POST), /upload/ (PUT exfil), /files/ (GET download)"
    context: "MiniFast 6-endpoint REST API surface (corpus-novel detection layer)"
    confidence: high
    source_attribution: "Check Point Research primary (2026-05-22)"
    actor_id: "004"
    defanged: false

ttp_keywords:
  - name: AppDomain hijacking via trojanized XML .config files
    framework_mapping: MITRE T1574.014 / Hijack Execution Flow - AppDomainManager
    context: "Malicious .config files pointing to AppDomainManager classes - corpus-novel level of specific TTP detail vs finding-0001 abstract AppDomain hijacking note"
  - name: Zoom scheduled-task hijack (ZoomUpdateTaskUser-SID)
    framework_mapping: MITRE T1053.005 / Scheduled Task/Job - Scheduled Task
    context: "Hijacks legitimate Zoom client's per-user update scheduled task for MiniFast persistence"
  - name: SSL.com code-signing certificate abuse
    framework_mapping: MITRE T1588.003 / Obtain Capabilities - Code Signing Certificates
    context: "Two CKR-named SSL.com subject identities (Gray Matter Software S.R.L., Kirubel Kerie Negeya) used to sign Nimbus Manticore payloads"
  - name: MiniFast 16-opcode command matrix
    framework_mapping: Multi-mapping family (T1083 file/directory discovery, T1059.003 cmd.exe, T1057 process discovery, T1490 inhibit recovery via process termination, T1547.001 persistence via scheduled task, T1548.002 runas UAC bypass, T1571 dynamic poll/jitter)
    context: "Comprehensive backdoor capability surface - directory enumeration (0x02), file move/rename (0x03), cmd execution (0x04), process enum (0x05), file/directory deletion (0x06), download (0x07), upload (0x08), drive enum (0x09), process termination (0x0A), DLL loading (0x0B), directory creation (0x0C), ZIP archive creation (0x0D), UAC elevation via runas (0xB0), persistence via scheduled task (0xB1), dynamic poll interval (0xF0), jitter configuration (0xF2)"
  - name: AI-assisted malware development indicators
    framework_mapping: Analytical assessment - no formal MITRE mapping
    context: "CKR analytical inference: excessive error handling on simple API calls, verbose/repetitive function naming, embedded debug/status messages, modular code organization despite functional simplicity. Single-vendor confidence layer (corpus carry-forward caveat from finding-0001)."

# Downstream handoff flags
analyst_review_required: true
analyst_review_topics:
  - "Sector-framing fidelity: Industrial Cyber relay introduces 'aerospace' framing not in CKR primary text - load-bearing assumption for A&D-prime audience"
  - "AI-assisted malware development indicators (CKR-only analytical inference; carry-forward from finding-0001 open question; ACH might surface alternative explanations like developer-team-restructure or framework-template-imprint)"
  - "Operation Epic Fury campaign-naming + Feb 28 2026 US military operation anchor - CKR-only analytical framing; KAC review on geopolitical-attribution-by-timing assumption"
  - "UNC1549 as subgroup of Charming Kitten (APT35) - novel-to-corpus relation framing requiring actor-profiler dossier review on whether to integrate CKR-claimed relation into _roster.yaml"
  - "Bohrium + TA455 alias-set expansion - novel-to-corpus aliases requiring actor-profiler alias-set harmonization"

red_team_review_required: true
red_team_review_topics:
  - "WEP very_likely on procedural tradecraft layer (MiniFast 16-opcode, AppDomain hijacking specifics, Zoom scheduled-task hijack) - argue alternative explanations or weaker confidence reading"
  - "26+26 IOC drop authority: vendor-published; argue for or against treating CKR's IOC enumeration as authoritative vs vendor-internal-naming-convention noise"
  - "Sector framing 'aviation' authoritative reading: US-domestic-airline impersonation lures are concrete but no A&D-prime is named compromised; red-team the very-likely WEP on US-aviation-explicit-targeting given lack of named victim"
red_team_review:
  reviewed_at: 2026-05-26T17:05:00-04:00
  reviewed_by: red-team-analyst
  run_id: red-team-20260526-170500
  mode: post_analyst

  strongest_counter_hypothesis:
    hypothesis: >
      H2 (UNC1549 conducted the campaigns AND the subgroup-of-Charming-Kitten
      relation is operationally meaningful) is more competitive than the
      analyst's three-inconsistency ranking implies. The analyst's H1
      zero-inconsistency rests heavily on E9 (absence of corroborating
      vendor research on subgroup framing). CKR's primary was published
      only 2026-05-22 - four calendar days before this sweep. Treating
      a four-day silence from Mandiant, Unit 42, and MSTIC as informative
      absence is structurally weak: vendor research cycles routinely take
      weeks to months to publish on a specific relation claim, especially
      one as novel as a subgroup-of-APT35 framing.
    evidence_for_counter:
      - "CKR primary publication date 2026-05-22; sweep date 2026-05-26 - only 4 calendar days of corpus-observable silence on subgroup framing"
      - "Vendor research on novel cluster-relation claims routinely lags originating publication by weeks (e.g., Charming Kitten / APT42 / TA453 relation took months for cross-vendor convergence in 2022-2023 corpus history)"
      - "CKR uses 'believed to be a subgroup' hedge language - this is CONSISTENT with CKR having visibility evidence not yet exposed publicly rather than INCONSISTENT with operational subgroup status (the hedge is normal vendor caution on novel framing, not absence of evidence)"
      - "Both UNC1549 (#004) and Charming Kitten (#011) are IRGC-affiliated per corpus baseline; shared parent (IRGC) makes subgroup organizational relation structurally plausible regardless of operational tradecraft differences"
    evidence_against_counter:
      - "Multi-year corpus baseline (Mandiant, Unit 42, MSTIC 2024-2026) treats UNC1549 and Charming Kitten as separate clusters with non-overlapping operational signatures - this is not 4 days of silence; it is years of differential treatment"
      - "CKR's 'believed to be' is a confidence-marker; the hedge cuts both ways but more typically signals analytical inference than withheld operational evidence"
      - "Unit 42's concurrent 2026-05-22 publication on the same UNC1549 cluster does NOT adopt the subgroup-of-APT35 framing - this is meaningful contemporaneous non-adoption, not just temporal silence"

  weaknesses_in_primary_assessment:
    - "E9 (absence of corroborating subgroup research) is counted as INCONSISTENT with H2 in the ACH matrix, but absence-of-evidence at 4-day observation window is weak diagnostic evidence. Analyst's framing of E9 as informative absence is brittle. The diagnostic count separating H1 (0) and H2 (3) is overstated; a more honest read is H1 (0) vs H2 (1-2)."
    - "E2 (Unit 42 concurrent as independent A-grade corroboration) is load-bearing on the 'very_likely' WEP for corroborated tradecraft. Unit 42 primary has NOT been directly fetched in this sweep per finding's own naming-taxonomy-reconciliation open question carried forward from finding-0001. Treating concurrent publication as proven-independent without primary read is a sensitivity that analyst's own tripwire (if_E2_unit42_downgraded) acknowledges but does not resolve at this surface. The independence claim is currently structural-inference, not verified."
    - "The 'very_likely' WEP entry on us_aviation_explicit_targeting_per_ckr_quote conflates two layers: (a) 'CKR said US aviation is targeted' (CKR primary verbatim - very_likely on the speech act); and (b) 'US-domestic-airline impersonation lures prove US aviation targeting' (chain of inference qualified by KAC A2 'qualify' classification). The WEP value rests on (a) but downstream consumers will read it as endorsing (b). Analyst's KAC explicitly qualified A2 (lures may target across sectors, not just sector matching the lure subject) but the WEP table does not reflect that qualification."
    - "Cluster topic prose ('US aviation explicit targeting') is downstream-readable as direct A&D-prime targeting evidence for the brief audience. The KAC A4 (A&D-prime employee populations within UNC1549 targeting set via airline lures) is test-classified 'not achievable from corpus' and critical-centrality. Same pattern as the 0008 finding's prose-vs-WEP-table inconsistency the analyst flagged: prose categorically asserts what the WEP table correctly qualifies."

  strongest_counter_wep: likely  # if subgroup-of-APT35 framing turns out operationally meaningful, H2's WEP becomes "likely" not "remote"

  recommendation: qualify

  qualifying_language_suggested: >
    Briefer should split the WEP-level framing on aviation targeting into
    two reads for downstream consumers: (1) "CKR primary explicitly
    names aviation as a targeted sector with US-domestic-airline lures
    as concrete evidence" - this is very_likely (CKR-said-it, verbatim
    quoted under 15 words); (2) "A&D-prime defensive priority via airline-
    themed lures translates to material employee exposure" - this is
    roughly_even_chance and conditional on specific airline-adjacent
    employee segmentation per the analyst's KAC A4 test deferral.
    Additionally, the absence-of-corroborating-research on the subgroup-
    of-APT35 framing should be characterized as "no corroboration yet
    at 4-day post-publication window" rather than as informative absence;
    re-evaluate when the corpus-observation window reaches 30+ days
    without corroboration.

  specific_tests_that_would_resolve:
    - "Direct Unit 42 primary fetch (2026-05-22 publication) - verifies E2 independence and resolves whether Unit 42 adopts or rejects CKR's subgroup-of-APT35 framing in their own primary text"
    - "30-day corpus observation window on subgroup framing - if no second A/B-grade vendor publishes corroborating subgroup-of-APT35 framing by 2026-06-22, the absence-of-evidence becomes meaningfully diagnostic (E9 weight rises)"
    - "Mandiant or MSTIC explicit response (adoption, rejection, or qualification) on CKR's three CKR-only analytical claims - the 4-day silence is non-informative; a 30+ day silence with no public response from cluster-naming-authority vendors would be more diagnostic"
    - "Splunk first-party telemetry hits on MiniFast IOCs or UNC1549 infrastructure - would anchor first-party-precedence and recalibrate the entire WEP layering"

  wep_adjustment_recommended: very_likely  # ceiling unchanged on corroborated tradecraft; recommend prose-level qualification on aviation-targeting layer
  wep_adjustment_rationale: >
    Top-level wep_ceiling: very_likely stands on the corroborated
    tradecraft layer (CKR + Unit 42, even with E2 independence-as-
    structural-inference caveat). No ceiling reduction recommended.
    The qualification applies at the wep_layered entry for
    us_aviation_explicit_targeting_per_ckr_quote: recommend briefer
    treat as "very_likely on CKR speech act; roughly_even_chance on
    A&D-prime employee exposure inference" - i.e., split the layer
    rather than reduce it. The three CKR-only analytical claims
    (Operation Epic Fury naming, subgroup-of-APT35 relation, Bohrium +
    TA455 alias-set) correctly held at "likely" by single-source veto;
    no change. This is a prose-level qualify recommendation, not a
    WEP-ceiling downgrade.

  notes: >
    Not blocking - the underlying UNC1549 cluster-identity claim is
    robust against contrarian challenge. H1 ranks first in the contrarian
    re-run too. The weaknesses are: (1) the absence-evidence weighting
    on E9 is brittle at 4-day post-publication window; (2) Unit 42
    independence is structural-inference until primary direct-fetch;
    (3) the aviation-explicit-targeting WEP layer conflates CKR's
    speech act with the inference-chain-to-A&D-prime that KAC properly
    qualified. The brief should preserve the analyst's qualifying
    framing rather than collapse to the categorical "US aviation
    explicit targeting" prose. The subgroup-of-Charming-Kitten relation
    deserves explicit "single-vendor analytical framing pending
    corroboration" rather than implicit single-source-veto handling -
    downstream consumers including actor-profiler will read the
    finding more accurately with the explicit caveat.
    Hard Rule 2 compliance verified - contrarian counter-hypotheses
    do not originate new attribution; H2 is CKR's own framing being
    pressure-tested upward, H3/H4 are within the Iran-nexus actor
    set already in corpus roster (no novel actor claim raised).

red_team_review_complete: true
red_team_outcome: qualify
wep_ceiling_adjusted_by_red_team: very_likely  # unchanged at top level
wep_ceiling_adjustment_reason_red_team: >
  Top-level wep_ceiling stands; red-team recommends prose-level
  qualifying language on the us_aviation_explicit_targeting layer
  to preserve the analyst's KAC A4 test-deferral framing rather
  than collapse to categorical "aviation explicit targeting" prose.
  Briefer to split the WEP read into CKR-speech-act (very_likely)
  vs A&D-prime-employee-exposure-inference (roughly_even_chance).
publication_blocked: false

analyst_review_complete: true
analyst_review_run_id: analyst-20260526-164200
analyst_wep_adjusted: false
analyst_wep_adjustment_reason: >
  No WEP adjustment recommended. ACH ranks H1 (UNC1549 as cohesive cluster per CKR + Unit 42) first with zero inconsistencies; grader's existing WEP layering (very_likely on corroborated tradecraft; likely on three CKR-only analytical claims via single-source veto) is correctly calibrated. KAC qualifies the aviation->A&D-prime inference chain with explicit caveats but does not invalidate the underlying targeting claim.
assessment_blocked_pending_test: false
analyst_test_deferred: A4_ad_prime_employee_lure_exposure_not_achievable_from_publicly_available_corpus

analysis_sections:
  sat_ach:
    ach_analysis:
      question: >
        Given the CKR-reported tradecraft cluster (MiniFast 16-opcode backdoor,
        AppDomain hijacking via XML .config files, Zoom scheduled-task hijack,
        SSL.com cert abuse on Gray Matter / Kirubel subjects, getsqldeveloper
        SEO poisoning, US-domestic-airline impersonation lures, Azure-hosted
        staging, Iran/IRGC nexus framing): is CKR's attribution to UNC1549 /
        Nimbus Manticore the strongest explanation, or do alternative Iran-
        nexus or Iran-adjacent actors fit the corroborated tradecraft surface
        better than the single-vendor CKR analytical framing implies (alias-
        set expansion Bohrium + TA455; subgroup-of-Charming-Kitten relation)?
      analyzed_at: 2026-05-26T16:42:00-04:00
      analyzed_by: analyst
      red_team_review: null

      hypotheses:
        - id: H1
          statement: >
            UNC1549 / Nimbus Manticore (corpus actor #004, Iran/IRGC) conducted
            all three CKR-documented 2026 campaigns; CKR's alias-set expansion
            (Bohrium, TA455) is a single-vendor naming-taxonomy contribution
            that does not change actor identity; the subgroup-of-Charming-
            Kitten framing is CKR analytical shorthand for shared Iran-nexus
            genealogy not an operational subgroup relation.
        - id: H2
          statement: >
            UNC1549 conducted the campaigns, AND the subgroup-of-Charming-
            Kitten (APT35, corpus #011) relation framed by CKR is an
            operationally meaningful claim - shared infrastructure, shared
            operators, or shared tasking justifies treating UNC1549 as a
            Charming-Kitten subordinate cluster rather than a peer Iran-
            nexus actor.
        - id: H3
          statement: >
            The campaigns were conducted by a distinct Iran-nexus actor
            (Bohrium and/or TA455 as separate clusters, NOT UNC1549 aliases
            despite CKR's alias-set framing); CKR has merged operationally-
            distinct Iran-nexus clusters into one Nimbus Manticore designation
            on the basis of shared tradecraft families that other vendors
            (Mandiant, Unit 42, MSTIC) keep separate.
        - id: H4
          statement: >
            The campaigns were conducted by a different tracked Iran-nexus
            actor (Charming Kitten #011, APT34 #023, MuddyWater #022, or
            Handala Hack #014) whose 2026 tradecraft has drifted into
            UNC1549-resembling territory; CKR's attribution is correct on
            Iran-nexus framing but misassigns the specific cluster.
        - id: H5
          statement: >
            Null hypothesis - the campaigns are not the work of a single
            cohesive actor; the CKR-reported tradecraft cluster is an
            ecosystem-of-Iran-nexus-tradecraft surface (shared tooling,
            shared hosting, shared lure themes) being exercised by multiple
            Iran-nexus operators without coherent single-cluster attribution.
        - id: H6
          statement: >
            False-flag / non-Iran-nexus actor (Russia-nexus or China-nexus
            sophisticated APT, or capable cybercriminal-adjacent group)
            deliberately running operations to look like UNC1549 /
            Nimbus Manticore for plausible-deniability or strategic-
            confusion purposes.

      evidence:
        - id: E1
          description: >
            CKR primary verbatim "Iranian, IRGC affiliated, threat actor
            Nimbus Manticore" - direct vendor attribution language
          source: checkpoint-research-2026-05-22
          digraph: A2
          weight: 3
        - id: E2
          description: >
            Unit 42 concurrent publication on same UNC1549 cluster with
            different taxonomy (Screening Serpens / Smoke Sandstorm) -
            independent vendor research corroborating tradecraft family
          source: unit42-2026-05-22
          digraph: A2
          weight: 3
        - id: E3
          description: >
            MiniFast 16-opcode backdoor capability matrix - corpus-novel
            specific TTP detail; tightly internally consistent
          source: checkpoint-research-2026-05-22
          digraph: A2
          weight: 3
        - id: E4
          description: >
            AppDomain hijacking via trojanized XML .config files pointing
            to AppDomainManager classes - MITRE T1574.014 corpus-novel
            specific detail; corroborated via Unit 42 AppDomainManager
            tradecraft (per finding-0001 THN-relay aggregation)
          source: checkpoint-research-2026-05-22 + unit42-2026-05-22
          digraph: A2
          weight: 3
        - id: E5
          description: >
            Zoom ZoomUpdateTaskUser-SID scheduled-task hijack persistence
            + WindowsSecurityUpdate task name - corpus-novel persistence
            mechanism documented by CKR only at this surface
          source: checkpoint-research-2026-05-22
          digraph: A2
          weight: 3
        - id: E6
          description: >
            SSL.com code-signing certificate abuse with two named subjects
            (Gray Matter Software S.R.L., Kirubel Kerie Negeya) - CKR-
            only on specific subjects; no contradicting source
          source: checkpoint-research-2026-05-22
          digraph: A2
          weight: 3
        - id: E7
          description: >
            getsqldeveloper.com SEO poisoning + US-domestic-airline
            impersonation lures (Campaign 3 fake hiring portals) -
            consistent with CKR primary aviation-sector targeting framing
          source: checkpoint-research-2026-05-22
          digraph: A2
          weight: 3
        - id: E8
          description: >
            Corpus baseline - UNC1549 actor #004 has Mandiant 2026-05-04
            originating attribution + Unit 42 2026-05-22 concurrent +
            CKR 2026-05-22 originating-for-Nimbus-Manticore-designation;
            multi-vendor Iran/IRGC consensus is pre-established
          source: corpus-roster-actor-004
          digraph: A1
          weight: 3
        - id: E9
          description: >
            Other vendor research (Mandiant, Unit 42, MSTIC) has historically
            treated UNC1549 and Charming Kitten (APT35) as separate Iran-
            nexus clusters with non-overlapping operational signatures;
            no second A/B-grade source corroborates CKR's subgroup-of-APT35
            framing
          source: corpus-baseline-multi-vendor-2025-2026
          digraph: A2
          weight: 3
        - id: E10
          description: >
            Bohrium (Microsoft taxonomy) and TA455 (Proofpoint taxonomy)
            have historically been used by other vendors with overlapping-
            but-not-identical activity attribution to Iran-nexus operations;
            CKR's inclusion of these aliases in the UNC1549 alias set is
            a single-vendor framing
          source: vendor-taxonomy-historical-baseline
          digraph: B3
          weight: 1
        - id: E11
          description: >
            Splunk first-party 8h sweep on UNC1549 / Nimbus Manticore /
            MiniFast / Bohrium / TA455 / Charming Kitten / APT35 plus
            campaign IOC strings - zero events
          source: splunk-defenseclaw_local + archimedes -8h@h
          digraph: A1
          weight: 3
        - id: E12
          description: >
            CKR primary uses "believed to be a subgroup" hedge language -
            not "is a subgroup"; vendor's own confidence-marker indicates
            analytical framing rather than operational evidence
          source: checkpoint-research-2026-05-22-verbatim
          digraph: A2
          weight: 3
        - id: E13
          description: >
            Operation Epic Fury campaign-naming anchored to "US military
            campaign against Iran launched on February 28, 2026" - CKR-
            only geopolitical-timing analytical anchor; no second source
            corroborates the operational link between Iran-nexus activity
            spike and the Feb 28 US military event
          source: checkpoint-research-2026-05-22
          digraph: A3
          weight: 1
        - id: E14
          description: >
            Tradecraft family is documented Iran-nexus pattern across
            multiple actors (Iran/IRGC code-signing-cert abuse - actor
            APT34/OilRig pattern; .NET DLL-loading abuse - cross-cluster
            Iran-nexus pattern; SEO poisoning - Iran-nexus broad pattern)
          source: corpus-baseline-iran-nexus-ttp-family
          digraph: B2
          weight: 2

      matrix:
        E1:  {H1: C, H2: C, H3: I, H4: I, H5: I, H6: I}     # direct CKR attribution to UNC1549/Nimbus Manticore - inconsistent with non-UNC1549 hypotheses
        E2:  {H1: C, H2: C, H3: I, H4: I, H5: I, H6: I}     # Unit 42 corroboration on same UNC1549 cluster (with different taxonomy) - inconsistent with non-UNC1549
        E3:  {H1: C, H2: C, H3: C, H4: C, H5: N, H6: C}     # MiniFast capability matrix is tradecraft-detail; non-diagnostic for cluster-identity question
        E4:  {H1: C, H2: C, H3: C, H4: C, H5: N, H6: C}     # AppDomain hijacking corroborated tradecraft - non-diagnostic for cluster identity
        E5:  {H1: C, H2: C, H3: C, H4: C, H5: N, H6: C}     # Zoom scheduled-task hijack - non-diagnostic for cluster identity
        E6:  {H1: C, H2: C, H3: C, H4: C, H5: C, H6: C}     # SSL.com cert subjects - CKR-only; non-diagnostic for hypothesis distinction
        E7:  {H1: C, H2: C, H3: N, H4: C, H5: N, H6: N}     # US-aviation impersonation lures consistent with UNC1549 known targeting + with H4 Iran-nexus drift
        E8:  {H1: C, H2: C, H3: I, H4: I, H5: I, H6: I}     # corpus baseline multi-vendor UNC1549 consensus - inconsistent with non-UNC1549 hypotheses
        E9:  {H1: C, H2: I, H3: C, H4: C, H5: C, H6: N}     # ABSENCE of corroborating vendor research on subgroup-of-APT35 framing - INCONSISTENT with H2 specifically
        E10: {H1: C, H2: N, H3: C, H4: N, H5: C, H6: N}     # historical taxonomy keeps Bohrium/TA455 as separate-but-overlapping clusters - mildly consistent with H3 cluster-merger reading
        E11: {H1: N, H2: N, H3: N, H4: N, H5: N, H6: N}     # Splunk silence - non-diagnostic per Hard Rule 8 ("silence is not disconfirming")
        E12: {H1: C, H2: I, H3: N, H4: N, H5: N, H6: N}     # CKR's "believed to be" hedge language - INCONSISTENT with H2 (which requires operational subgroup evidence)
        E13: {H1: N, H2: N, H3: N, H4: N, H5: C, H6: C}     # geopolitical-timing campaign-naming - non-diagnostic for cluster identity; mildly consistent with H5 ecosystem reading
        E14: {H1: C, H2: C, H3: C, H4: C, H5: C, H6: I}     # Iran-nexus TTP-family consistency - inconsistent with H6 non-Iran-nexus false flag

      inconsistency_counts:
        H1: 0     # zero inconsistencies; consistent across all diagnostic evidence
        H2: 3     # E9 (absence of corroborating subgroup-of-APT35 vendor research), E12 (CKR's own hedge language), E1/E2 mildly weighted positive but the subgroup-specific evidence is contradicted
        H3: 4     # E1, E2, E8 each inconsistent with rejecting UNC1549-as-coherent-cluster
        H4: 4     # E1, E2, E8 each inconsistent with non-UNC1549 Iran-nexus assignment despite tradecraft drift
        H5: 4     # E1, E2, E8 each inconsistent with null-hypothesis non-coherent-cluster reading
        H6: 5     # E1, E2, E8, E14 inconsistent with non-Iran-nexus false flag (Iran-nexus TTP-family + multi-vendor IRGC attribution is hard to false-flag)

      diagnostic_evidence:
        - E1: "Direct CKR attribution language distinguishes H1/H2 (UNC1549/Nimbus Manticore) from H3/H4/H5/H6 (alternative actor or null)"
        - E2: "Unit 42 concurrent publication on same UNC1549 cluster distinguishes H1/H2 (UNC1549) from H3/H4/H5 (alternative cluster)"
        - E8: "Corpus baseline multi-vendor consensus on UNC1549 as cohesive cluster distinguishes H1/H2 from H3/H4/H5/H6"
        - E9: "ABSENCE of corroborating vendor research on subgroup-of-APT35 framing specifically distinguishes H1 from H2 - this is the diagnostic evidence on the subgroup-relation sub-question"
        - E12: "CKR's own 'believed to be' hedge language distinguishes H1 (CKR's framing as analytical shorthand) from H2 (operational subgroup relation)"

      ranking:
        - rank: 1
          hypothesis_id: H1
          rationale: >
            Zero inconsistencies. All five diagnostic evidence items (E1, E2,
            E8, E9, E12) are consistent with H1. CKR's primary attribution
            language + Unit 42 corroborating concurrent publication +
            corpus-baseline multi-vendor consensus + CKR's own hedge
            language on the subgroup framing + absence of corroborating
            subgroup research all align on H1's reading: CKR's attribution
            to UNC1549 is sound; the alias-set expansion and subgroup-
            of-Charming-Kitten framing are single-vendor analytical
            contributions that warrant actor-profiler review but do not
            change the underlying cluster identity. Per the grader's WEP
            layered table this maps to "very likely" on the actor-identity
            claim and "likely" on the subgroup-relation and alias-set claims
            (single-source veto already capped these correctly).
          wep_implication: >
            Procedural tradecraft cluster very_likely; subgroup-of-APT35
            relation likely (single-source); alias-set expansion likely
            (single-source); supports grader's existing WEP layering -
            no adjustment recommended.
        - rank: 2
          hypothesis_id: H2
          rationale: >
            Three inconsistencies. E9 specifically (absence of any second
            A/B-grade source corroborating the subgroup-of-Charming-Kitten
            framing across Mandiant, Unit 42, MSTIC, CrowdStrike) is the
            structurally important inconsistency. E12 (CKR's own "believed
            to be" hedge language) is a vendor-internal confidence marker
            inconsistent with operational subgroup status. H2 is plausible
            but not currently supported - escalating to operational
            subgroup status requires either second-vendor corroboration
            or direct CKR primary read for the evidence basis.
          wep_implication: >
            Subgroup-relation operational reading: unlikely at present
            evidence. Maps to grader's "likely" on the relation-claim layer
            via single-source-veto correctly.
        - rank: 3
          hypothesis_id: H3
          rationale: >
            Four inconsistencies via E1, E2, E8. The cluster-merger reading
            (CKR has improperly merged distinct Iran-nexus clusters into
            Nimbus Manticore) is contradicted by Unit 42's independent
            corroboration on the same UNC1549 cluster identity. The
            historical taxonomy ambiguity on Bohrium/TA455 (E10) gives
            this hypothesis a small foothold for actor-profiler dossier
            review but does not make it the stronger explanation.
          wep_implication: very_unlikely
        - rank: 4
          hypothesis_id: H4
          rationale: >
            Four inconsistencies via E1, E2, E8. Tradecraft-drift toward
            UNC1549-resembling activity by Charming Kitten, APT34,
            MuddyWater, or Handala is theoretically possible but no
            evidence in the cluster surfaces it; CKR + Unit 42 + corpus-
            baseline all converge on UNC1549.
          wep_implication: very_unlikely
        - rank: 5
          hypothesis_id: H5
          rationale: >
            Four inconsistencies. The ecosystem-of-Iran-nexus-tradecraft
            null hypothesis is contradicted by the multi-vendor
            convergence on UNC1549 as a coherent cluster. The historical
            taxonomy ambiguity (E10) gives this minimal support but
            E1/E2/E8 are heavyweight contradictions.
          wep_implication: remote
        - rank: 6
          hypothesis_id: H6
          rationale: >
            Five inconsistencies including the Iran-nexus TTP-family
            evidence (E14). False-flagging Iran/IRGC attribution against
            both Mandiant + Unit 42 + Microsoft historical baseline +
            CKR + the Iran-nexus TTP-family signature would require an
            improbably capable and sustained masquerade operation. Ruled
            out at this surface.
          wep_implication: remote

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence: [E1, E2, E8, E9, E12]
        if_E2_unit42_downgraded: >
          If Unit 42's 2026-05-22 concurrent publication were later
          determined to derive from CKR rather than independent telemetry
          (currently graded A2 as independent vendor research), H1's
          inconsistency count would still be zero but the assessment
          becomes effectively single-A-grade-source - the WEP ceiling on
          the corroborated tradecraft layer would drop from "very likely"
          to "likely" per single-source veto. Mitigation: direct Unit 42
          primary read in a subsequent sweep is the correct test.
        if_E9_corpus_baseline_revised: >
          If a second A/B-grade source (Mandiant, MSTIC, CrowdStrike, or
          a future vendor publication) publishes corroborating subgroup-
          of-Charming-Kitten framing, H2's inconsistency count drops to
          ~1; H2 becomes operationally meaningful and actor-profiler
          should integrate the relation into _roster.yaml. Tripwire
          flagged below.
        if_E1_e8_attribution_drift: >
          If a future vendor publication explicitly disputes UNC1549
          attribution on the 2026 campaigns (e.g., assigns to a different
          cluster), H1's inconsistencies rise and H3/H4 gain support.
          Tripwire flagged.
        single_point_of_failure: >
          The H1 v H2 ranking on the subgroup-relation sub-question is
          load-bearing on E9 (absence of corroborating vendor research)
          + E12 (CKR's own hedge language). If both were to be
          superseded by future reporting, H2 becomes competitive. The
          subgroup-relation layer is the brittle sub-element; the
          underlying UNC1549 cluster-identity is robust.

      tripwires:
        - observation: >
            Second A/B-grade vendor publishes corroborating subgroup-of-
            Charming-Kitten (APT35) relation for UNC1549 / Nimbus Manticore
          effect: >
            H2 inconsistency drops; actor-profiler must integrate the
            relation into _roster.yaml. Rerun ACH.
        - observation: >
            Unit 42 primary directly fetched and determined to derive
            attribution from CKR (rather than independent telemetry)
          effect: >
            E2 weight reduces; corroborated tradecraft layer WEP drops
            from very_likely to likely; rerun ACH on tradecraft-cluster
            sub-question.
        - observation: >
            Future vendor publication disputes UNC1549 attribution or
            assigns 2026 campaigns to a different Iran-nexus cluster
          effect: >
            H1 inconsistency rises; H3/H4 gain support; rerun ACH on
            cluster-identity question.
        - observation: >
            Splunk first-party telemetry surfaces hits on MiniFast IOCs,
            UNC1549 infrastructure, or Bohrium/TA455 strings in
            defenseclaw_local
          effect: >
            E11 inverts from neutral to high-weight positive; cluster-
            identity question gets first-party-precedence anchor;
            rerun ACH with +1 confidence weighting per Hard Rule 8.
        - observation: >
            Bohrium-attributed activity (per Microsoft) or TA455-attributed
            activity (per Proofpoint) is published with operational
            signatures distinct from UNC1549 campaigns
          effect: >
            E10 weight rises; H3 (cluster-merger reading) gains support
            on the alias-set sub-question; actor-profiler review on
            alias-set harmonization escalates.

      conclusion:
        summary: >
          UNC1549 / Nimbus Manticore attribution to the three CKR-documented
          2026 campaigns is the strongest explanation by structural ACH
          analysis (H1 rank 1, zero inconsistencies). The subgroup-of-
          Charming-Kitten relation (H2) is the structurally weaker reading
          - inconsistent with the absence of corroborating vendor research
          and inconsistent with CKR's own "believed to be" hedge language.
          The alias-set expansion (Bohrium + TA455 as UNC1549 aliases)
          carries moderate ambiguity per historical multi-vendor taxonomy
          (E10) but is not contested by the structural evidence; it warrants
          actor-profiler dossier review rather than ACH-level rejection.
          The Iran/IRGC attribution itself is corpus-baseline and is not
          a novel attribution per Hard Rule 2 - CKR is the originating
          source for Nimbus Manticore designation, not for Iran-nexus
          framing. The grader's existing WEP layering (very_likely on
          tradecraft cluster; likely on the three CKR-only analytical
          claims) is appropriately calibrated by single-source veto and
          does not require adjustment based on this ACH.
        wep_implication: >
          No WEP adjustment recommended. Grader's wep_ceiling: very_likely
          on the corroborated tradecraft layer stands; the three CKR-only
          analytical claims (Operation Epic Fury campaign-naming;
          subgroup-of-Charming-Kitten relation; Bohrium + TA455 alias-set
          expansion) remain at "likely" per single-source veto. Assessment
          is medium-brittleness to Unit 42 corroboration weight (E2) and
          to the absence-evidence on subgroup framing (E9).
        confidence_caveats: >
          Single-vendor dependence on CKR for the three analytical claims
          is the material limitation; the corroborated tradecraft layer
          (CKR + Unit 42) is more robust than the analytical-framing
          layer. Hard Rule 2 holds: Archimedes propagates CKR's
          framings as CKR's framings, not as Archimedes-originated
          attributions or relations.

  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "CKR primary reports explicit US aviation targeting by UNC1549 /
        Nimbus Manticore (US-domestic-airline impersonation lures
        Campaign 2 + Campaign 3 fake airline hiring portals); for an A&D-
        prime target audience this constitutes a material targeting
        signal warranting defensive priority - i.e., 'aviation' framing
        extends meaningfully to US A&D primes."
      analyzed_at: 2026-05-26T16:50:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Pre-publication review for PM-26 afternoon brief. The grader has
        flagged the sector-framing fidelity question (CKR primary
        "aviation" vs Industrial Cyber relay "aerospace") as the load-
        bearing question for the A&D-prime audience. KAC interrogates
        the chain of inference from "CKR says aviation targeted" to
        "A&D primes should treat this as material defensive signal."

      assumptions:
        - id: A1
          statement: >
            CKR's "aviation" sector framing accurately represents what
            UNC1549 / Nimbus Manticore is targeting in 2026
          category: source_reliability
          stated: true
          why_must_be_true: >
            Assessment uses CKR primary as authoritative on sector framing
          when_could_be_false: >
            CKR's telemetry visibility is biased toward CKR customer base
            (which includes both airlines and broader enterprise verticals
            but may not represent UNC1549's full victim distribution);
            CKR may report on what they see rather than UNC1549's full
            operational scope
          evidence_for: [checkpoint-research-2026-05-22, unit42-2026-05-22-corroborating-tradecraft]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A2
          statement: >
            US-domestic-airline impersonation lures (Campaign 2 + Campaign 3
            fake hiring portals) demonstrate that UNC1549 is targeting US
            aviation rather than impersonating US aviation to phish other
            sectors
          category: TTP_patterns
          stated: false
          why_must_be_true: >
            The lure-content -> targeting-vector chain of inference depends
            on assuming attackers craft lures matching their intended
            victim sector rather than using sector-specific lures to phish
            broadly across sectors
          when_could_be_false: >
            Iran-nexus actors have documented patterns of using sector-
            specific lures (hiring portals, conference invites) to phish
            ACROSS sectors - the lure subject does not always match the
            victim sector; alternatively, "US-domestic-airline impersonation"
            could be the cover identity used to phish defense, telecom,
            or other sectors
          evidence_for: [checkpoint-research-2026-05-22-campaign-3-fake-hiring-portals]
          evidence_against: [iran-nexus-historical-lure-cross-sector-pattern]
          confidence: medium
          centrality: material
          classification: qualify
        - id: A3
          statement: >
            "Aviation" in CKR's framing maps to commercial passenger
            airlines (United, Delta, American, Southwest) rather than to
            aerospace manufacturers (Boeing, Airbus, Lockheed Martin) or
            defense contractors (Northrop Grumman, Raytheon, General
            Atomics)
          category: semantic
          stated: true
          why_must_be_true: >
            CKR primary uses "aviation" not "aerospace"; Industrial Cyber
            relay's "aerospace" addition is editorial drift per grader's
            relay-drift flag; the distinction is material for the A&D-
            prime audience
          when_could_be_false: >
            CKR's "aviation" framing may encompass airline AND aerospace-
            manufacturer overlap that the grader is parsing too strictly;
            the lure US-domestic-airline portals may be a beachhead
            into airline IT staff who maintain shared infrastructure
            with aerospace primes (Boeing IT for example services multiple
            commercial airline customer accounts)
          evidence_for: [grader-relay-drift-flag-analysis]
          evidence_against: [aviation-aerospace-airline-supplier-ecosystem-overlap]
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A4
          statement: >
            US A&D primes are not directly exposed to UNC1549 via the
            airline-lure surface because A&D prime employees do not
            routinely receive airline-hiring-portal phishing as part of
            their threat surface
          category: visibility
          stated: false
          why_must_be_true: >
            For the "aviation = airline = NOT A&D prime" reading to
            translate into "low A&D prime priority", A&D prime employees
            must not actually be in the targeting set for airline-themed
            lures
          when_could_be_false: >
            Many A&D primes have aviation-customer-facing employees
            (Boeing Commercial Aircraft division, Lockheed's Sikorsky
            unit servicing airline operators, Raytheon Pratt-Whitney
            servicing engine programs) who DO receive aviation-themed
            communication routinely; airline-themed phishing is a
            plausible attack surface for those employee segments
          evidence_for: []
          evidence_against: [boeing-commercial-aircraft-employee-segment, sikorsky-airline-rotor-servicing]
          confidence: low
          centrality: critical
          classification: test
        - id: A5
          statement: >
            UNC1549's 2026 operational tempo is high enough that "consider
            this material" is a defensively meaningful posture for A&D
            primes - i.e., the actor is genuinely active on US aviation
            surface and not concluded-after-Operation-Epic-Fury
          category: actor_operational_status
          stated: false
          why_must_be_true: >
            For the targeting signal to be defensively actionable, UNC1549
            must remain operationally active on the documented surface
            through the assessment window
          when_could_be_false: >
            Operation Epic Fury per CKR is anchored to a specific
            geopolitical event (Feb 28 2026 US military operation against
            Iran); if the operational tempo was geopolitically-driven
            and the geopolitical context has shifted, current activity
            may not match the CKR-documented tempo; alternatively,
            Iran-nexus disruption from law-enforcement / counterintelligence
            response could change operational status
          evidence_for: [unc1549-2025-2026-multi-vendor-active-campaign-baseline]
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A6
          statement: >
            CKR's "explicit aviation targeting" framing represents intent
            to compromise aviation, not merely opportunistic compromise
            in the aviation space
          category: intent
          stated: false
          why_must_be_true: >
            Assessment treats CKR's "aviation targeted" language as
            evidence of strategic intent; A&D-prime defensive prioritization
            depends on the actor having sector-specific intent rather than
            random victim distribution
          when_could_be_false: >
            UNC1549 could be a broad-spectrum Iran-nexus operator with
            aviation appearing as one of many vertical targets
            opportunistically; the "aviation explicit targeting" reading
            could reflect CKR's customer-base bias rather than actor
            intent
          evidence_for: [checkpoint-research-2026-05-22-three-campaign-aviation-thread, unc1549-historical-aviation-pattern-mandiant-2024-2025]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A7
          statement: >
            CKR's Iran/IRGC attribution remains accurate through the
            assessment window; the actor has not been re-attributed by
            other vendors to a non-Iran-nexus identity
          category: source_reliability
          stated: false
          why_must_be_true: >
            The defensive-priority chain depends on UNC1549 remaining
            an Iran-nexus actor with sustained intent against US targets;
            re-attribution would change the threat model entirely
          when_could_be_false: >
            Multi-vendor consensus shifts (e.g., Mandiant retracts or
            qualifies); future vendor research disputes the Iran-nexus
            framing
          evidence_for: [mandiant-2026-05-04, unit42-2026-05-22, checkpoint-research-2026-05-22, microsoft-historical-iran-nexus-baseline]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A8
          statement: >
            Archimedes' first-party Splunk silence on UNC1549 / MiniFast /
            Nimbus Manticore IOCs reflects actual non-presence in
            defenseclaw_local infrastructure rather than a visibility gap
          category: visibility
          stated: false
          why_must_be_true: >
            The grader's Hard Rule 8 note ("silence is not disconfirming")
            already covers this; KAC surfaces the assumption that
            defenseclaw_local has visibility into the right surfaces to
            detect UNC1549 activity if it were present
          when_could_be_false: >
            defenseclaw_local is a non-self lab estate; visibility into
            real-world aerospace prime networks is by design absent;
            silence here cannot inform aviation/aerospace defensive
            posture in any direction
          evidence_for: [hard-rule-8-doctrine, defenseclaw_local-61-consecutive-dormant-sweep]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
        - id: A9
          statement: >
            The "aviation" framing in CKR primary text is meaningful
            verbatim and the relay drift to "aerospace" by Industrial
            Cyber reflects relay editorialization not investigative
            evidence
          category: source_reliability
          stated: true
          why_must_be_true: >
            Grader's relay-drift flag depends on CKR primary being the
            authoritative sector-framing source; Industrial Cyber as a
            relay does not add primary investigative evidence on sector
          when_could_be_false: >
            Industrial Cyber's editorial may reflect access to a CKR
            extended-version or briefing that the public CKR primary
            does not contain; this is unlikely but possible
          evidence_for: [grader-direct-ckr-primary-read]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A10
          statement: >
            "Defensive priority for A&D primes" is the appropriate audience
            framing for this finding rather than "primary A&D-prime alert"
          category: semantic
          stated: false
          why_must_be_true: >
            The finding's intended downstream audience is A&D primes; the
            framing balance between alerting and informational is calibrated
            by the actual sector-targeting evidence
          when_could_be_false: >
            If aviation actually does encompass aerospace-prime surface
            via shared employee segments + shared supplier ecosystem
            (A4 + A3 combined), the appropriate framing escalates from
            informational to alerting
          evidence_for: [grader-A&D-prime-direct-relevance-medium-via-airline-impersonation]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify

      classifications_summary:
        sound: 4       # A1, A7, A8, A9
        qualify: 5     # A2, A3, A5, A6, A10
        test: 1        # A4
        reject: 0

      remediation:
        status: qualify_with_explicit_caveats
        qualifying_caveats:
          - >
            CKR primary's "aviation" sector framing is the authoritative
            verbatim read; Industrial Cyber relay's "aerospace"
            editorialization is not evidence-supported - flag preserved
            from grader (A9 sound)
          - >
            US-domestic-airline-impersonation lures are concrete evidence
            of US aviation in UNC1549's lure-content set; whether the
            intended victim sector is airline-employee, airline-IT,
            aerospace-prime-employees-receiving-airline-themed-comms, or
            cross-sector phishing using airline lure as cover is NOT
            disambiguated by current evidence (A2 + A6 qualify)
          - >
            For A&D-prime defensive prioritization: aviation framing
            should be treated as "material if your prime has airline-
            adjacent employee segments or services airline customers"
            rather than "material across all prime employee populations"
            (A3 + A4 + A10 qualify)
          - >
            UNC1549 operational continuity through the assessment window
            is a load-bearing assumption that the grader's first-party
            Splunk dormancy and the corpus-baseline 2025-2026 active-
            campaign pattern do support but do not confirm; treat
            "material defensive signal" as conditional on actor remaining
            operationally active (A5 qualify)
        test_required:
          assumption_id: A4
          test_description: >
            Determine whether A&D-prime employee populations (specifically
            commercial-aviation-adjacent segments at Boeing Commercial
            Aircraft, Sikorsky / Lockheed Aerospace Services, Pratt-Whitney
            / Raytheon engine programs, Embraer Defense, GE Aerospace, etc.)
            are within UNC1549's targeting set via airline-themed lures.
            This is fundamentally unanswerable from publicly available
            corpus material - it requires either (a) victim-population
            disclosure by named A&D primes (unlikely to be public), (b)
            second-vendor publication of A&D-prime-specific UNC1549
            targeting evidence, or (c) first-party Splunk telemetry from
            an A&D-prime estate. None of these are achievable via current
            collection.
          test_disposition: >
            Test is NOT achievable at this sweep. Assessment proceeds
            with A4 qualified as low-confidence-critical: the chain of
            inference from "airline-themed lures" to "A&D-prime employee
            exposure" cannot be confirmed or refuted from current evidence.
            Recommend briefer surface as "potentially material via
            airline-adjacent employee segments; evidence does not
            disambiguate" rather than as either "material" or "not
            material" categorically.
        next_action: >
          Briefer should include the sector-framing qualifying caveats
          explicitly in the afternoon brief. Vuln-tracker / actor-profiler
          may also benefit from the qualified framing during dossier
          updates. A4-test status: deferred indefinitely pending
          collection-side break.

      recommended_wep_after_kac:
        us_aviation_explicit_targeting_per_ckr_quote: >
          No change from grader's "very_likely" - CKR primary verbatim
          + US-domestic-airline impersonation lures concrete; the
          targeting CLAIM is very_likely. The INFERENCE from that claim
          to "material defensive signal for all A&D primes" is what's
          qualified, not the underlying targeting claim itself.
        ad_prime_indirect_relevance_via_airline_adjacent_employee_segments: >
          No grader WEP entry exists for this specific layer; analyst
          recommends briefer include as qualifying caveat at "roughly
          even chance" - A&D-prime exposure varies by company-specific
          aviation-adjacent employee segmentation and cannot be
          generically asserted.
        sector_framing_aviation_per_ckr_vs_aerospace_per_relay: >
          No change from grader's roughly_even_chance on the relay-
          editorialization claim - the "aerospace" framing is relay
          editorial drift, not evidence-supported; "aviation" remains
          the authoritative read.

      sensitivity_analysis:
        most_load_bearing_assumptions: [A3, A4, A5, A7]
        if_A3_wrong_aviation_actually_encompasses_aerospace_overlap: >
          Assessment escalates A&D-prime indirect relevance from
          "varies by company" to "material across primes with commercial-
          aviation-adjacent units" - reframes audience guidance
        if_A4_wrong_A&D_primes_actually_exposed_via_airline_lures: >
          Assessment escalates from informational to alerting framing;
          briefer would surface this as "verify airline-adjacent employee
          segments are aware of UNC1549 lure patterns" rather than
          generic sector-monitoring
        if_A5_wrong_unc1549_disrupted_or_dormant: >
          Assessment de-escalates to historical-tracking framing;
          would mean current finding is post-campaign reportage rather
          than active-threat-signal
        if_A7_wrong_unc1549_re-attributed_to_non-iran-nexus: >
          Entire threat model recasts; finding becomes attribution-
          uncertainty rather than Iran-nexus-active-targeting; would
          require full rerun of analysis pipeline

      tripwires:
        - observation: >
            Second A/B-grade vendor publishes UNC1549 victim list including
            a named A&D prime (e.g., Lockheed, Boeing, Northrop, Raytheon)
          effect: >
            A4 confidence rises sharply; reframes A&D-prime relevance
            from indirect to direct; rerun KAC
        - observation: >
            Second A/B-grade vendor publishes UNC1549 victim list confined
            to commercial airlines without A&D-prime overlap
          effect: >
            A3 + A4 confidence sharpens toward narrow "aviation = airline
            only" reading; de-emphasizes A&D-prime defensive priority
        - observation: >
            UNC1549 operational disruption announced (law enforcement
            action, infrastructure takedown, or vendor reports campaign
            cessation)
          effect: >
            A5 inverts; assessment shifts to historical-tracking framing
        - observation: >
            Mandiant or other primary vendor disputes CKR's Iran/IRGC
            attribution or proposes alternative cluster framing
          effect: >
            A7 inverts; full reassessment required
        - observation: >
            Splunk first-party hits in defenseclaw_local on UNC1549 /
            MiniFast / Nimbus Manticore IOCs
          effect: >
            A8 visibility assumption updates; first-party precedence
            takes effect; entire defensive posture shifts

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-26-afternoon]
retracted: false
retraction_brief_id: null
---

# Check Point Research Primary Surfaces in Corpus: UNC1549 / Nimbus Manticore "Fast and Furious" Three-Campaign Breakdown with 26 SHA256 + 26 Domain IOC Drop, Operation Epic Fury Anchored to US Military Operation Against Iran (Feb 28 2026), and CKR-Only Framing of Nimbus Manticore as Charming Kitten (APT35) Subgroup

## Summary

Check Point Research's 2026-05-22 primary publication "Fast and Furious - Nimbus Manticore Operations During the Iranian Conflict" surfaces in the Archimedes corpus directly for the first time today via SecurityWeek (Ionut Arghire, 09:26 EDT) and Industrial Cyber (Anna Ribeiro, today) PM-window B-grade relays. CKR documents three sequenced 2026 campaigns by UNC1549 / Nimbus Manticore: Campaign 1 "Rising Tension" (February 2026, AppDomain hijacking introduction + MiniJunk deployment), Campaign 2 "Operation Epic Fury" (post-February 28 2026, anchored to the US military campaign against Iran launched that date - trojanized Zoom installer + MiniFast backdoor introduction + AI-assisted development indicators), and Campaign 3 "SQL Developer" (April 2026, SEO poisoning + fake US-domestic-airline hiring portals). CKR carries provisional A grade in corpus; corroboration is by Palo Alto Networks Unit 42's 2026-05-22 concurrent publication on the same UNC1549 cluster (different parent org, different telemetry, different cluster-naming taxonomy). Iran/IRGC attribution to UNC1549 (actor #004) is corpus-baseline. Three CKR-only analytical claims carry single-source-veto caps to WEP "likely": Operation Epic Fury campaign-naming + US-military-timing anchor; UNC1549 as "believed to be a subgroup of Charming Kitten (APT35)" - novel relation framing relative to corpus _roster.yaml; Bohrium + TA455 alias-set expansion. Net-new corpus material includes the full 26 SHA256 + 26 domain IOC drop, full MiniFast 16-opcode capability matrix, AppDomain hijacking via trojanized XML .config files pointing to AppDomainManager classes, Zoom ZoomUpdateTaskUser-SID scheduled-task hijack persistence, WindowsSecurityUpdate scheduled-task name, and SSL.com code-signing certificate abuse with two distinct subject identities. CKR primary says US aviation is explicitly targeted with US-domestic-airline impersonation lures - no specific airline or A&D-prime is named as compromised. Sector framing fidelity flagged: Industrial Cyber's relay editorializes CKR's "aviation" to "aerospace, aviation, telecom" - the "aerospace" framing is not in CKR primary text and may overstate the A&D-prime targeting signal for an A&D-prime audience. This finding is a SIBLING to finding-2026-05-26-0001 (THN-relay anchor; B2 cluster digraph); the direct CKR primary surfacing upgrades the corpus treatment to A2 on the same tradecraft surface. Anti-noise lock on the UNC1549 surface remains active through 2026-05-27 08:00 EDT.

## Sources

### Check Point Research primary (checkpoint-research, digraph: provisional A)

- URL: https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/
- Published: 2026-05-22
- Byline: Check Point Research team
- Key claim: Three-campaign breakdown of UNC1549 / Nimbus Manticore 2026 operations - Campaign 1 Rising Tension (February 2026), Campaign 2 Operation Epic Fury (post Feb 28 2026), Campaign 3 SQL Developer (April 2026). Full MiniFast 16-opcode backdoor capability documentation. AppDomain hijacking via trojanized XML .config files. SSL.com code-signing certificate abuse (Gray Matter Software S.R.L., Kirubel Kerie Negeya). 26 SHA256 + 26 domain IOC drop. CKR-only analytical claims: Operation Epic Fury named + tied to US Feb 28 2026 military operation; Nimbus Manticore as "believed to be a subgroup of Charming Kitten (APT35)"; Bohrium + TA455 added to alias set. Iran/IRGC attribution corpus-baseline.

### SecurityWeek in-window relay (securityweek, digraph: B)

- URL: https://www.securityweek.com/iranian-apt-targets-aviation-software-companies-with-updated-tools/
- Published: 2026-05-26 09:26 EDT (in-window)
- Byline: Ionut Arghire
- Key claim: B-grade relay of CKR primary; sector framing "aviation and software companies" consistent with CKR primary "aviation" framing. No novel investigative content vs CKR.

### Industrial Cyber in-window relay (industrialcyber-co, digraph: B with relay-drift flag)

- URL: https://industrialcyber.co/ransomware/irgc-linked-nimbus-manticore-group-attacks-defense-aerospace-telecom-sectors-using-minifast-malware-toolkit/
- Published: 2026-05-26 (today)
- Byline: Anna Ribeiro (News Editor)
- Key claim: B-grade relay of CKR primary. Sector framing editorialized to "defense, aerospace, telecom" - the "aerospace" framing is RELAY-INTRODUCED and does not appear in CKR primary text (CKR uses "aviation"). Relay-drift flag set; for A&D-prime audience the distinction between commercial aviation (airlines, with which CKR's US-domestic-airline impersonation lures are consistent) and aerospace (manufacturers including Boeing/Airbus/Lockheed) is material.

### Palo Alto Networks Unit 42 (unit42, digraph: A) - corroborating corpus-tracked primary

- Publication: MiniUpdate / MiniJunk V2 / AppDomainManager tradecraft (concurrent with CKR)
- Publication date: 2026-05-22
- Relation: Independent vendor research concurrent on the same UNC1549 campaign cluster - different parent org (Palo Alto Networks vs Check Point Software Technologies), different telemetry, different cluster-naming taxonomy (Screening Serpens / Smoke Sandstorm vs Nimbus Manticore). Cited via finding-0001's THN-relay aggregation; direct primary fetch in a subsequent sweep would close the open analyst question on whether CKR's MiniFast == Unit 42's MiniUpdate (same family) or adjacent-but-distinct.

## Technical detail

### MiniFast 16-opcode capability matrix (full corpus-novel drop per CKR primary)

64-bit Windows PE DLL impersonating Chrome browser. Entry point `CheckForUpdates` exported function. Communication via JSON-formatted REST-style API with Base64-encoded task structures. Six C2 endpoints: `/rg` (POST handshake), `/agent/init` (POST register), `/agent/poll?token=` (GET task), `/agent/result` (POST), `/upload/` (PUT exfil), `/files/` (GET download).

Sixteen opcodes documented by CKR:

| Opcode | Capability | MITRE mapping (analytical) |
|---|---|---|
| 0x02 | Directory enumeration | T1083 |
| 0x03 | File move / rename | T1070 |
| 0x04 | Shell command execution via `cmd.exe /c` | T1059.003 |
| 0x05 | Process enumeration | T1057 |
| 0x06 | File / directory deletion | T1070.004 |
| 0x07 | File download from C2 | T1105 |
| 0x08 | File upload to C2 | T1041 |
| 0x09 | Drive enumeration | T1083 |
| 0x0A | Process termination | T1489 family |
| 0x0B | DLL loading with exported function invocation | T1129 |
| 0x0C | Directory creation | T1564 family |
| 0x0D | ZIP archive creation | T1560.002 |
| 0xB0 | UAC elevation via `runas` | T1548.002 |
| 0xB1 | Persistence installation via scheduled tasks | T1053.005 |
| 0xF0 | Dynamic poll interval adjustment | T1571 |
| 0xF2 | Jitter configuration | T1571 |

### AppDomain hijacking via trojanized XML .config files (corpus-novel specifics)

CKR documents specific abuse pattern: malicious `.config` files pointing to `AppDomainManager` classes, exploiting the .NET runtime's CLR loader to execute attacker-controlled assemblies when legitimate .NET executables launch. MITRE T1574.014 (Hijack Execution Flow - AppDomainManager). This is more specific than finding-0001's abstract "AppDomain hijacking" note - the .config-file-with-AppDomainManager-pointer pattern is the corpus-novel technical anchor.

### Zoom scheduled-task hijack and WindowsSecurityUpdate persistence (corpus-novel)

CKR documents two persistence-task names:
- `ZoomUpdateTaskUser-<SID>` - hijacks Zoom client's legitimate per-user update scheduled task to launch MiniFast at user logon while blending with normal Zoom update telemetry
- `WindowsSecurityUpdate` - persistence task name impersonating Windows security update routine

MiniFast staging path: `C:\Users\<USER>\AppData\Local\Zoom\bin\update` - uses Zoom's legitimate `bin/update` path for filesystem blending.

### SSL.com code-signing certificate abuse (two CKR-named subjects)

CKR primary names two SSL.com-issued code-signing certificate subjects abused for Nimbus Manticore payload signing:
- Gray Matter Software S.R.L. (organization subject)
- Kirubel Kerie Negeya (individual-name subject)

These are corpus-novel detection-and-revocation anchors. PII handling: the individual-name subject appears in CKR primary as code-signing-certificate subject only (not as a victim or private-individual identifier); inclusion follows LEGAL-POLICY GDPR data minimization (named public-identifier-acting-in-cert-issuance-context retained for defensive use).

### Three-campaign timeline (per CKR primary)

| Date | Campaign | CKR-documented events |
|---|---|---|
| At least 2022 | (Active since) | Initial UNC1549 / Nimbus Manticore activity |
| November 2024 | Dream Job campaign | Lazarus-style tactics adoption |
| February 2026 | Campaign 1: Rising Tension | AppDomain Hijacking introduction; MiniJunk deployment |
| **February 28, 2026** | **Operation Epic Fury** | **CKR-claimed anchor**: US military campaign against Iran launched; Nimbus Manticore resurfaces |
| During Operation Epic Fury | Campaign 2 | Trojanized Zoom installer; MiniFast introduced; AI-assist indicators |
| April 2026 | Campaign 3 | SEO poisoning; getsqldeveloper.com; US-airline-themed hiring portals |
| 2026-05-22 | CKR primary published | Three-wave consolidation |
| 2026-05-26 | SecurityWeek + Industrial Cyber relays | Corpus surface today (PM window) |

### CKR-only analytical claims requiring single-source-veto handling

Three claims are CKR-only at this surface and carry single-source-veto caps to WEP "likely":

1. **Operation Epic Fury campaign-naming + Feb 28 2026 US military operation anchor.** CKR-only analytical framing tying Campaign 2 to a specific geopolitical date. WEP capped at "likely" pending second A/B-grade source corroboration.

2. **Nimbus Manticore as "believed to be a subgroup of Charming Kitten (APT35)".** Verbatim CKR primary language. Novel framing relative to corpus _roster.yaml which has UNC1549 (#004) and Charming Kitten (#011) as separate Iran-nexus entries with no subgroup relation documented. Other vendor research (Mandiant, Unit 42, Microsoft MSTIC) has historically treated these as separate clusters. Flagged for actor-profiler review.

3. **Bohrium + TA455 added to UNC1549 alias set.** CKR primary names these aliases. Current corpus _roster.yaml #004 alias set: Tortoiseshell, Smoke Sandstorm, Imperial Kitten, Crimson Sandstorm. CKR's published aliases: Nimbus Manticore, UNC1549, Bohrium, Smoke Sandstorm, TA455. Bohrium and TA455 are net-new to corpus. Flagged for actor-profiler review on alias-set harmonization.

### Sector and geography framing - originating vs relay drift

| Source | Sectors named | Direct framing |
|---|---|---|
| Check Point Research (primary) | "defense, aviation and telecommunication" | "primarily targets the defense, aviation and telecommunication sectors" |
| SecurityWeek (Arghire relay) | aviation, software | "aviation and software companies" |
| Industrial Cyber (Ribeiro relay) | "defense, aerospace, telecom" | RELAY-INTRODUCED "aerospace" framing not in CKR primary |

For A&D-prime audience: CKR primary supports "aviation" (commercial airlines, consistent with US-domestic-airline impersonation lures) and "defense" (generic, no specifics) but NOT "aerospace" in the manufacturer/prime sense. Industrial Cyber's editorialization is the relay-drift case worth analyst attention.

### Named victims and impersonation targets

- **Named confirmed victims: ZERO** - CKR primary names no specific company as a confirmed victim
- **Named impersonated organizations** (phishing lures): Accenture, US-based airline (Campaign 2; specific airline unnamed), US-domestic airlines (Campaign 3 fake hiring portals; specific airlines unnamed), Zoom (legitimate software trojanized via installer), Oracle SQL Developer (Campaign 3 fake download), Chrome / Google (user-agent spoofing)
- **Hosting / abuse infrastructure**: Azure Web Sites, OnlyOffice (document hosting / malware staging), SSL.com (certificate authority abused - two specific subjects above)

### AI-assisted malware development indicators (corpus carry-forward)

CKR's analytical inference - same caveat as finding-0001 - that MiniFast's code structure exhibits:
- Excessive error handling on simple API calls
- Verbose, repetitive function naming patterns
- Embedded debug / status messages
- Modular code organization despite functional simplicity

Single-vendor analytical inference. Corpus-baseline AI-assisted-development concern from CKR's separate AI Threat Landscape Digest (finding-2026-05-26-0002) is the broader context but does not corroborate this specific MiniFast inference.

## IOCs surfaced (full CKR primary IOC drop now in corpus)

Net-new IOC additions to corpus this finding:

- **26 SHA256 hashes** (full CKR primary IOC list - see raw-2026-05-26-pm-001 frontmatter for complete enumeration; librarian to propagate to `_master-index.yaml`)
- **26 malicious domains** including 21 azurewebsites[.]net staging subdomains + 5 apex/non-Azure domains (`business-startup[.]org`, `buisness-centeral-transportation[.]com`, `PremierHealthAdvisory[.]com`, `ramiltonsfinance[.]com`, `getsqldeveloper[.]com` - see raw-signal pm-001 for full enumeration; librarian to propagate)
- **MiniFast staging path**: `C:\Users\<USER>\AppData\Local\Zoom\bin\update`
- **Scheduled-task names**: `ZoomUpdateTaskUser-<SID>`, `WindowsSecurityUpdate`
- **MiniFast HTTPS user-agent**: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36`
- **SSL.com code-signing certificate subjects**: `Gray Matter Software S.R.L.`, `Kirubel Kerie Negeya`
- **MiniFast C2 REST API surface**: `/rg`, `/agent/init`, `/agent/poll?token=`, `/agent/result`, `/upload/`, `/files/`

## Relationship to existing findings

- **finding-2026-05-26-0001** (sibling, B2 cluster anchor) - The Hacker News editorial-relay anchor on the same UNC1549 tradecraft surface. Finding 0007 is the originating-primary direct-surface sibling. 0001's open analyst question on "naming taxonomy reconciliation - does CKR's MiniFast == Unit 42's MiniUpdate" is partially advanced by 0007: CKR's MiniFast capability matrix is now in corpus directly; Unit 42 primary direct fetch in a subsequent sweep would close the question.
- **finding-2026-05-26-0002** (sibling A1, CKR primary on AI Threat Landscape Digest) - Same publisher, different surface. Finding 0002 covers AI-use-in-offensive-operations at the landscape level; the AI-assisted-malware-development-indicators inference in finding 0007 is a corpus-internal cross-reference but NOT corroboration of MiniFast-specific AI inference (the 0002 surface is GTG-1002 Mexico and BISSA/EvilTokens, not UNC1549).
- **UNC1549 actor #004 dossier** (last-reviewed 2026-05-09, threat level MEDIUM weighted 5.4) - This finding warrants an actor-profiler dossier update review covering: (a) Operation Epic Fury campaign anchor; (b) Bohrium + TA455 alias-set expansion; (c) Charming Kitten subgroup-relation framing (corpus-novel relation); (d) MiniFast 16-opcode capability matrix; (e) SSL.com code-signing certificate abuse pattern; (f) Zoom scheduled-task hijack persistence.
- **Charming Kitten actor #011 dossier** (last-reviewed 2026-05-09, threat level LOW weighted 4.45) - Indirectly affected by the CKR-claimed subgroup relation; actor-profiler review should consider cross-referencing the two dossiers if the relation framing carries forward in corroborating publications.

## Open questions for analyst

- **Sector-framing fidelity (SAT-ACH candidate):** Industrial Cyber's relay-introduced "aerospace" framing vs CKR primary "aviation" framing. For an A&D-prime audience, the distinction is material. Hypotheses to compete: (H1) CKR primary text accurately captures targeting scope - "aviation" = commercial airlines + "defense" generic; (H2) Industrial Cyber's editorial sees evidence in CKR primary that supports "aerospace" extension that grader missed; (H3) Industrial Cyber relay drift is editorial-amplification not evidence-supported.

- **Operation Epic Fury campaign-naming geopolitical-timing inference (SAT-KAC candidate):** CKR ties Campaign 2 to "US military campaign against Iran launched on February 28, 2026". Load-bearing assumption: that the campaign-naming-by-geopolitical-trigger framing is analytically sound vs the alternative that February-March 2026 activity by Iran-nexus actors is a routine operational tempo not specifically anchored to one geopolitical event. KAC review on the chain of inference from observed activity to claimed campaign-trigger.

- **UNC1549 subgroup-of-Charming-Kitten relation (actor-profiler SAT-ACH candidate):** CKR's novel framing relative to corpus roster. Hypotheses: (H1) CKR has visibility into operational overlap (shared infrastructure, shared operators, shared tradecraft) that supports a subgroup relation; (H2) CKR's "subgroup of" is analytical shorthand for "Iran-nexus IRGC-affiliated cluster that may share some operational genealogy with Charming Kitten" without operational evidence of subgroup status; (H3) Other vendor research (Mandiant, Unit 42, MSTIC) treats them as separate clusters because the operational signatures do NOT support a subgroup relation. Resolution requires either second A/B-grade source corroboration of the relation OR direct CKR primary read for the evidence basis of the framing.

- **Alias-set harmonization (actor-profiler task):** Bohrium + TA455 are net-new to corpus _roster.yaml #004 alias set. CKR primary does not include Imperial Kitten + Crimson Sandstorm + Tortoiseshell (which are in current corpus roster). Actor-profiler should decide: (a) merge CKR aliases additively into corpus set; (b) flag corpus aliases not in CKR set for review; (c) annotate corpus roster with source-attribution per alias.

- **AI-assisted malware development indicators (carry-forward from finding-0001):** Single-vendor analytical inference. Red-team alternatives: developer-team-restructure-or-rotation, framework-template-imprint, intentional-defensive-obfuscation-mimicry. Resolution requires Unit 42 / Mandiant / MSTIC corroboration on the MiniFast-specific inference.

- **US aviation explicit targeting (red-team-analyst candidate):** CKR primary says US aviation is explicitly targeted; concrete-evidence layer is US-domestic-airline impersonation lures (Campaign 2 + Campaign 3 fake hiring portals) without specific airline named. Red-team the very-likely WEP on "US aviation explicit targeting" given the lack of named victim - is the targeting claim authoritative, or is it inference from lure-content?

## Hard Rules compliance

- **Rule 2 - no novel attribution origination:** Iran/IRGC attribution to UNC1549 is corpus-baseline (Mandiant 2026-05-04 originating, Unit 42 2026-05-22 concurrent, CKR 2026-05-22 originating-for-Nimbus-Manticore-designation, AM-26 morning brief absorption). CKR-only claims (Operation Epic Fury campaign-naming, subgroup-of-Charming-Kitten relation, Bohrium + TA455 aliases) are reported as CKR framings - not Archimedes-originated.
- **Rule 6 - quote discipline:** Verbatim quotations preserved with attribution: "Iranian, IRGC affiliated, threat actor Nimbus Manticore" (6 words, CKR); "believed to be a subgroup of Charming Kitten (APT35)" (9 words, CKR); "US military campaign against Iran launched on February 28, 2026" (10 words, CKR); "the actor's recent operations demonstrate an expansion toward aviation-sector targets in the United States" (15 words exactly, CKR). All under 15-word limit; one-quote-per-source observed across multiple paraphrase-context sections.
- **Rule 7 - credentials:** No credential exposure surfaced; SSL.com cert subjects are code-signing-cert subjects (not credentials).
- **Rule 8 - first-party precedence:** PM pre-brief 8h Splunk sweep zero hits on MiniFast / Nimbus Manticore / UNC1549 / AppDomain / Bohrium / TA455 / Charming Kitten / APT35 plus campaign-specific IOC strings. Silence is not disconfirming.

## Analytic notes (from analyst review)

ACH ranks H1 (UNC1549 / Nimbus Manticore as cohesive cluster per CKR + Unit 42) first with zero inconsistencies; H2 (operationally meaningful subgroup-of-Charming-Kitten relation) ranks second with three inconsistencies, the most diagnostic being the absence of any second A/B-grade vendor corroborating the subgroup framing and CKR's own "believed to be" hedge language. The grader's WEP layering — very_likely on the CKR+Unit42 corroborated tradecraft, likely (single-source-veto-capped) on the three CKR-only analytical claims (Operation Epic Fury naming, subgroup-of-APT35 relation, Bohrium + TA455 alias-set expansion) — is correctly calibrated. No WEP adjustment recommended.

KAC on the load-bearing assumption that CKR's "aviation" framing extends meaningfully to US A&D primes surfaces ten assumptions, four sound, five qualify, one test. The critical-centrality test classification (A4 — whether A&D-prime employee populations are within UNC1549's airline-themed-lure targeting set) is not achievable from publicly available corpus material; it requires victim disclosure, second-vendor publication, or first-party A&D-prime telemetry. Assessment proceeds with explicit qualifying caveats: aviation framing should be treated as "material if your prime has airline-adjacent employee segments or services airline customers" rather than uniformly material across all primes. Brittleness is medium — the assessment is robust on Iran/IRGC attribution and on the tradecraft cluster but conditional on UNC1549 operational continuity and on the airline-lure-to-A&D-employee inference chain.

Hard Rule 2 holds throughout: CKR's framings (Nimbus Manticore designation, alias-set expansion, subgroup-of-APT35 relation) are propagated as CKR's framings, not as Archimedes-originated claims. Tripwires set for second-vendor corroboration on subgroup framing, named-A&D-prime victim disclosure, and any Splunk first-party hits.
