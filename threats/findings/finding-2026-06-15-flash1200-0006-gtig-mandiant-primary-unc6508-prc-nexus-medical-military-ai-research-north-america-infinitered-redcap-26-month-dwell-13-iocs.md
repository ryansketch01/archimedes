---
id: finding-2026-06-15-flash1200-0006
finding_id: finding-2026-06-15-flash1200-0006-gtig-mandiant-primary-unc6508-prc-nexus-medical-military-ai-research-north-america-infinitered-redcap-26-month-dwell-13-iocs
title: "Google Threat Intelligence Group (Mandiant + GTIG + FLARE + Workspace Security) primary direct retrieval discloses UNC6508 — PRC-nexus espionage cluster — conducting 26-month (Sept 2023 → Nov 2025+) campaign against North American medical research institutions, military health institutions, defense intelligence, AI research, uncrewed vehicle systems, Indo-Pacific command operations, and cyber offensive programs via INFINITERED modular backdoor on exposed/legacy REDCap servers; 13 indicators captured (1 IPv4 23.169.65.49 ASUS-router OBF + 1 email BebitaBarefoot774@gmail.com + 1 filename help.php + 7 SHA-256 + 1 GUID b49e334d-9c01-463e-9bc5-00a6920fb66e + 2 host artifacts Patroit + xc32038474a); UNC6508 is NOT on the 24-actor Archimedes roster — operator-deferred /new-actor candidate; GTIG attribution preserved verbatim per Hard Rule 2 (NO cross-walk to APT41/APT40/Salt Typhoon/Volt Typhoon — GTIG did not, Archimedes does not); single-publisher attribution constraint → WEP ceiling LIKELY (not very_likely); SecurityWeek + BleepingComputer are same-day relays crediting GTIG with no independent telemetry; FLASH-eligible per Trigger 5 (active multi-victim campaign vs. A&D sector — A1-primary sector-level A&D-adjacency)"
date: 2026-06-15
created_at: 2026-06-15T12:24:00-04:00
graded_by: grader
grading_run_id: flash-grade-20260615-120000
grading_mode: flash_fast_path
flash_path: true
test: false
status: graded

trigger_id:
  - ad-sector-campaign            # Trigger 5 — active multi-victim PRC-nexus campaign with explicit A&D-sector targeting categories per A1 primary

# ============================================================================
# Core grading (admiralty-grading skill output)
# ============================================================================
digraph: A2
admiralty_grade: A2
digraph_layered:
  # ---- GTIG / MANDIANT PRIMARY DIRECT-RETRIEVAL LAYER ----
  gtig_mandiant_primary_blog_published_2026_06_15_canonical: A1                                 # GTIG canonical on its own research; published today
  primary_direct_retrieval_via_cloud_google_com_succeeded_7th_consecutive: A1                   # Procedural success; source-health audit-trail verifiable
  gtig_attribution_language_unc6508_prc_nexus_threat_actor_high_confidence: A2                  # Mandiant attribution at vendor high-confidence framing; A-grade source, single primary
  # ---- ATTRIBUTION-IDENTITY LAYER (HARD RULE 2 BINDING) ----
  unc6508_distinct_cluster_NOT_cross_walked_to_apt41_apt40_salt_volt_typhoon_per_gtig_explicit: A1   # Verifiable absence — GTIG did not invoke any existing PRC actor name
  unc6508_NOT_on_24_actor_archimedes_roster_operator_deferred_new_actor_candidate: A1            # Verifiable — _roster.yaml _meta total_actors: 24, UNC6508 absent
  archimedes_does_NOT_originate_any_cross_walk_to_existing_roster_actors_hard_rule_2: A1         # Compliance attestation
  # ---- CAMPAIGN ACTIVITY + TIMEFRAME LAYER ----
  earliest_known_compromise_september_2023: A2                                                   # GTIG primary attestation; not independently corroborated this sweep
  observed_activity_duration_sept_2023_through_november_2025_26_months: A2                       # GTIG primary attestation
  more_than_one_year_dwell_undetected_in_primary_victim: A2                                      # GTIG primary attestation; vendor IR observation
  campaign_active_status_attested_through_publication_date: A2                                   # GTIG primary attestation
  # ---- TARGET SECTOR LAYER (A&D-ADJACENT — TRIGGER 5 LOAD-BEARING) ----
  north_american_medical_research_institutions_targeted: A2                                      # GTIG primary; sector-level claim
  north_american_military_health_institutions_targeted: A2                                       # GTIG primary; A&D-adjacent sector category
  defense_intelligence_research_priority_targeted: A2                                            # GTIG verbatim research-priority category
  ai_research_priority_targeted: A2                                                              # GTIG verbatim
  uncrewed_vehicle_systems_research_priority_targeted: A2                                        # GTIG verbatim — counter-UAS / UAS-adjacent A&D category
  cyber_offensive_programs_research_priority_targeted: A2                                        # GTIG verbatim
  indo_pacific_command_operations_research_priority_targeted: A2                                 # GTIG verbatim — SOCOM/INDOPACOM AOR relevant
  military_readiness_research_priority_targeted: A2                                              # GTIG verbatim
  national_defense_intelligence_research_priority_targeted: A2                                   # GTIG verbatim
  named_a_and_d_prime_victim_NONE_identified_in_primary: A1                                      # Verifiable absence — diverse-set framing only, no Lockheed/Boeing/Raytheon/NG named
  diverse_set_of_national_state_private_medical_entities_us_and_canada_multi_victim: A2          # GTIG framing; satisfies Trigger 5 multi-victim element at sector level
  # ---- INITIAL ACCESS + PERSISTENCE LAYER ----
  initial_access_via_vulnerable_legacy_redcap_servers_exposed_web_platform: A2                   # GTIG primary; no specific CVE assigned
  no_specific_cve_assigned_by_primary_configuration_patch_hygiene_pattern: A1                    # Verifiable absence — primary does not name a CVE
  help_php_web_shell_deployed_early_in_compromise_chain: A2                                      # GTIG primary attestation
  infinitered_modular_backdoor_deployed_approximately_3_months_post_initial_compromise: A2       # GTIG primary attestation
  exfiltration_via_google_workspace_compliance_rule_patroit_typo_of_patriot: A2                  # GTIG primary attestation; Workspace Security team co-authored
  bebitabarefoot774_gmail_exfiltration_destination_account_now_disabled: A2                      # GTIG primary attestation
  compromised_asus_router_23_169_65_49_us_obf_administrative_access_source: A2                   # GTIG primary attestation; Shodan internetdb returned found:false consistent with consumer device
  # ---- MALWARE — INFINITERED ARCHITECTURE LAYER ----
  infinitered_three_module_architecture_dropper_credential_harvester_backdoor: A2                # GTIG + FLARE primary attestation
  infinitered_credential_harvester_uses_db_session_id_prefix_xc32038474a_marker: A2              # GTIG primary forensic detail
  infinitered_backdoor_uses_guid_b49e334d_9c01_463e_9bc5_00a6920fb66e_persistence_marker: A2      # GTIG primary forensic detail
  yara_rule_g_backdoor_infinitered_1_published_by_gtig_referenced_by_name_not_reproduced: A1     # Hard Rule 3 compliance — YARA rule referenced, not copied into corpus
  # ---- IOC SET LAYER (13 INDICATORS, ALL A1 ON FACTS — DUAL-GRADE RULE) ----
  ip_23_169_65_49_administrative_login_source_from_compromised_asus_router: A1                   # GTIG IR observation; facts-level
  email_bebitabarefoot774_at_gmail_com_exfiltration_destination: A1                              # GTIG IR observation
  filename_help_php_web_shell: A1                                                                # GTIG IR observation
  sha256_ba6b73b0_help_php_persistence: A1                                                       # GTIG IR observation
  sha256_db65c1b9_infinitered_credential_harvester: A1                                           # GTIG IR observation
  sha256_c1ac43d2_infinitered_credential_harvester: A1                                           # GTIG IR observation
  sha256_8f015885_infinitered_backdoor: A1                                                       # GTIG IR observation
  sha256_51a57bfc_infinitered_backdoor: A1                                                       # GTIG IR observation
  sha256_4efbef69_infinitered_dropper: A1                                                        # GTIG IR observation
  sha256_58bb2577_infinitered_dropper: A1                                                        # GTIG IR observation
  guid_b49e334d_infinitered_backdoor_persistence_marker_host_artifact: A1                        # GTIG IR observation
  host_artifact_xc32038474a_db_session_prefix_forensic_marker: A1                                # GTIG IR observation
  host_artifact_patroit_workspace_compliance_rule_name_exfil_indicator: A1                       # GTIG IR observation
  # ---- RELAY LAYER (NON-INDEPENDENT — INDEPENDENCE TEST FAILS) ----
  securityweek_relay_credits_gtig_no_independent_telemetry_faithful_summary: B3                  # Relay; not independent corroboration per INTEL-GRADING.md
  bleepingcomputer_relay_credits_gtig_partial_ioc_reproduction_no_independent_telemetry: B3      # Relay; not independent corroboration per INTEL-GRADING.md
  # ---- SPLUNK FIRST-PARTY LAYER ----
  splunk_sentinel_9_ioc_unc6508_set_30d_zero_hits_visibility_limited_absence: A1                 # Procedural; query run with documented IOC set + 30d lookback; 0 hits
  silent_splunk_does_NOT_disconfirm_per_hard_rule_8_frank_not_north_american_medical_research: A1 # Doctrine attestation — visibility-limited absence flagged
  # ---- TRIGGER 5 CALIBRATION LAYER ----
  trigger_5_active_yes_sept_2023_through_nov_2025_per_a1_primary: A1                             # Calibration attestation
  trigger_5_multi_victim_yes_diverse_set_of_entities_per_a1_primary: A1                          # Calibration attestation
  trigger_5_ad_sector_yes_at_sector_category_level_per_a1_primary_verbatim: A2                   # Calibration ruling — see digraph_anchor + trigger_5_calibration_note below
  trigger_5_overall_positive: A2                                                                  # Cluster ruling
  # ---- CRITICAL OVERRIDE LAYER ----
  critical_override_does_NOT_apply_zero_of_four_conditions_met: A1                                # No CVE / no roster actor / no named A&D-prime victim / active exploitation conceptually present but CVE-gated condition fails
  cluster_anchor: A2

digraph_anchor: >
  Cluster anchored at A2 (Probably True) on the single A-grade primary source
  (Google Threat Intelligence Group — Mandiant + Mandiant Consulting + FLARE +
  Workspace Security joint publication, direct retrieval from cloud.google.com
  this sweep). The load-bearing operational claim — "a PRC-nexus espionage
  cluster designated UNC6508 conducted a 26-month campaign against North
  American medical research, military health, defense intelligence, AI
  research, uncrewed vehicle systems, Indo-Pacific command, and cyber
  offensive programs via INFINITERED modular backdoor deployed on exposed
  legacy REDCap servers, with 13 high-fidelity indicators documented" — rests
  on GTIG's vendor IR primary observation alone. SecurityWeek (Eduard Kovacs,
  10:07 EDT) and BleepingComputer (Bill Toulas, 10:00 EDT) are same-day relays
  that credit GTIG explicitly and contribute no independent telemetry; per
  INTEL-GRADING.md they collapse to a single effective source on this cluster
  anchor.

  CREDIBILITY CHECKLIST WALK:
    Grade 1 (Confirmed) — FAILS:
      [✗] At least one independent source — NO. SecurityWeek and
          BleepingComputer are relays of GTIG; both explicitly credit GTIG
          and contribute no separate telemetry. Independence test fails on
          the "Different evidence basis" condition.
      [—] Neither source cites the other — NOT APPLICABLE (relays cite GTIG)
      [—] Technical artifacts match across sources — partially (BC reproduces
          2 of 13 IOCs faithfully) but this is relay-fidelity, not
          independent observation.
      [✓] No contradicting higher-grade source — yes, no contradicting A/B.
      Grade 1 fails on the independence requirement.

    Grade 2 (Probably True) — PASSES on all three:
      [✓] Consistent with established TTPs for the named actor OR consistent
          with known campaign timing/targeting — YES. PRC-nexus medical
          research and defense-intelligence espionage is corpus-consistent
          with the broader PRC ecosystem targeting pattern (precedent class:
          health data collection during pandemic-era APT41 activity, biotech
          targeting in CrowdStrike PANDA cluster reports). The Workspace
          compliance-rule abuse for exfiltration is novel-but-coherent TTP
          consistent with PRC tradecraft maturity. 26-month dwell time on a
          research-data-capture platform is operationally plausible.
      [✓] No contradicting evidence from A/B-grade sources — YES, none.
      [✓] Technical claims internally coherent — YES. REDCap is a real and
          widely-deployed academic medical research platform (Vanderbilt
          consortium, used by 5000+ institutions globally). INFINITERED's
          three-module architecture (dropper / credential harvester /
          backdoor) is conventional malware design. The "Patroit" typo
          is human-plausible. The Chikungunya keyword correlating with the
          July 2025 Guangdong outbreak is coherent timing. The 13-IOC set
          is internally consistent (sequential SHA-256 hashes for the
          INFINITERED modules, plausible ASUS-router OBF endpoint per
          Shodan-internetdb non-indexing of consumer hardware).
      → Grade 2 (Probably True) qualifies cleanly.

  SINGLE-SOURCE VETO APPLIES per INTEL-GRADING.md:
    GTIG is the sole originating evidence base for the load-bearing claim
    (UNC6508 attribution, campaign timeline, victim profile, INFINITERED
    architecture, 13-IOC set, Workspace abuse tradecraft). SecurityWeek
    and BleepingComputer relay without independence. Per single-source veto
    doctrine, WEP ceiling caps at "likely" (not "very likely") regardless
    of A2 grade.

  WEP CEILING DERIVATION:
    - Cluster anchor (UNC6508 attribution + campaign existence + IOC set):
      "likely" per A2 + single-source veto.
    - Attribution-identity layer (UNC6508 = PRC-nexus): "likely" per A2 +
      GTIG vendor high-confidence framing, single-publisher.
    - 13-IOC set existence and forensic accuracy: "likely" per A2 + GTIG
      IR primary; first-party Splunk silent (visibility-limited).
    - Trigger 5 A&D-sector calibration: "likely" — A1 primary attests
      sector-level A&D-adjacency (military health, defense intelligence,
      uncrewed vehicle systems, Indo-Pacific command, cyber offensive
      programs) but no named A&D-prime victim; FLASH-POLICY Trigger 5 text
      says "aerospace, defense, or watchlist companies" which the grader
      reads as sector-inclusive — see trigger_5_calibration_note below.
    - Future continuation of campaign post-publication: "likely" per
      historical post-disclosure PRC-cluster behavior (corpus precedent:
      campaigns typically continue with infrastructure rotation rather
      than full cessation following public attribution).

  CRITICAL LAYERED NUANCE — the A2 attests to:
    (a) GTIG canonical authority on its own joint Mandiant + FLARE +
        Workspace Security IR research;
    (b) the procedural success of primary direct retrieval (7th consecutive
        cloud.google.com direct-HTML success);
    (c) the 13-IOC set and INFINITERED architecture as published in the
        primary, treated as A1 on facts per the dual-grade rule;
    (d) the UNC6508 attribution at GTIG's high-confidence framing,
        preserved verbatim per Hard Rule 2;
    (e) Trigger 5 calibration that sector-level A&D-adjacency per A1
        primary satisfies the FLASH-POLICY trigger text.

  The A2 does NOT attest to:
    - any cross-walk between UNC6508 and APT41, APT40, APT10, Volt Typhoon,
      Salt Typhoon, or any other named PRC cluster (GTIG explicitly did
      NOT cross-walk; Archimedes preserves verbatim per Hard Rule 2);
    - any named A&D-prime contractor (Lockheed Martin / Boeing / Raytheon /
      Northrop Grumman / General Dynamics / L3Harris / BAE / etc.) as a
      confirmed victim — no source names one;
    - independent second-vendor corroboration on the UNC6508 designation,
      IOC set, or TTP chain (none surfaced this sweep — no Unit 42 /
      CrowdStrike / MSTIC / Recorded Future / Microsoft DART parallel
      observation);
    - lift of the single-source veto on the campaign-existence claim;
    - any specific CVE assigned to the REDCap initial-access vector (none
      assigned by primary; configuration / patch-hygiene exposure pattern);
    - elevation of WEP above "likely" on any layer.

  TRIGGER 5 CALIBRATION NOTE (load-bearing for FLASH eligibility):
    FLASH-POLICY.md Trigger 5 reads verbatim: "Campaign explicitly
    targeting aerospace, defense, or watchlist companies / AND active
    (not retrospective) / AND multi-victim (not single-incident)."

    Doctrinal question: does sector-level A&D-adjacency per A1 primary
    attestation satisfy the "aerospace, defense, or watchlist companies"
    element, or does the trigger require a named A&D-prime victim
    (Lockheed / Boeing / Raytheon / NG / GD / L3Harris / BAE)?

    Grader ruling: SECTOR-LEVEL A&D-ADJACENCY PER A1 PRIMARY SATISFIES
    THE TRIGGER. Reasoning:

      (1) The policy text says "aerospace, defense, OR watchlist
          companies" — the OR construction makes sector-class
          targeting (defense) sufficient on its own, not contingent
          on watchlist binding. GTIG verbatim names "military health
          institutions" (DoD MHS), "defense intelligence," "uncrewed
          vehicle systems" (counter-UAS / UAS R&D), "Indo-Pacific
          command operations" (INDOPACOM AOR), "cyber offensive
          programs," and "military readiness" as research-priority
          targets. These are within the broader defense sector by
          any reasonable reading.

      (2) The policy does not specify "named-prime-victim binding"
          as a requirement. By contrast, the critical-override
          conditions DO specify "A&D watchlist ENTITY is NAMED as a
          target" — distinct, stricter language. The contrast is
          deliberate: critical-override is once-a-year, requires
          named binding; Trigger 5 is sector-level eligibility,
          does not.

      (3) Erring low on calibration would systematically suppress
          PRC-nexus campaign FLASH eligibility whenever vendor IR
          declined to name an A&D-prime victim — which is the
          near-universal pattern (vendor IR rarely names primes
          due to customer NDA, breach disclosure law, and
          counsel-driven non-attribution). The grader reads this
          as a doctrinal feature, not a bug: Trigger 5 is designed
          to fire on the sector-level pattern, not require the
          rare named-prime victim.

      (4) Active multi-victim: BOTH satisfied unambiguously.
          26-month campaign (Sept 2023 → Nov 2025+) is active.
          "Diverse set of national, state, and private medical
          entities" is multi-victim.

    Trigger 5: POSITIVE — confirmed.

    Operator override available: if the operator subsequently
    determines that Trigger 5 should require named-prime-victim
    binding (tightening the threshold), this finding's eligibility
    re-evaluates and the FLASH brief can be downgraded to a
    monitoring item in the 16:00 PM brief. Recommend operator
    review at next doctrine quarterly.

  HARD RULE BINDINGS RECORDED:
    - Hard Rule 1 (LEGAL-POLICY): all sources public OSINT (GTIG
      blog, SecurityWeek, BleepingComputer); no prohibited query
      patterns; no exploitation assistance; no active recon. PASS.
    - Hard Rule 2 (no novel attribution): UNC6508 attribution
      preserved verbatim from GTIG ("UNC6508, a People's Republic
      of China (PRC)-nexus threat actor"). NO cross-walk to
      APT41/APT40/APT10/Salt Typhoon/Volt Typhoon. GTIG did not,
      Archimedes does not. PASS.
    - Hard Rule 3 (no exploitation content): YARA rule
      G_Backdoor_INFINITERED_1 referenced by name and link to GTIG
      primary; not reproduced verbatim in raw-signal or this
      finding. IOCs at indicator level only. PASS.
    - Hard Rule 6 (15-word quote limit, one quote per source):
      attribution language captured as structured fields and
      paraphrased throughout; verbatim "UNC6508, a People's Republic
      of China (PRC)-nexus threat actor" is 12 words, single
      occurrence, GTIG-only. PASS.
    - Hard Rule 7 (credentials radioactive): no credentials in the
      raw-signal substrate; the BebitaBarefoot774 gmail account is
      a threat-actor-controlled exfiltration destination (now
      disabled per GTIG), recorded as an IOC indicator only — not
      a credential. PASS.
    - Hard Rule 8 (Splunk first-party precedence): 9-IOC sentinel
      run against defenseclaw_local + archimedes at -30d; 0 hits;
      silent Splunk does NOT disconfirm because Frank is not a
      North American medical research / military health
      institution running REDCap. Visibility-limited absence
      flagged; first_party_precedence.applied: false. PASS.

source_reliability:
  primary:
    grade: A
    source_name: "Google Threat Intelligence Group (Mandiant + Mandiant Consulting + FLARE team + Workspace Security)"
    source_yaml_id: mandiant
    source_url: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research
    published: 2026-06-15
    grade_rationale: >
      Pre-assigned A per source-grades.yaml line 156-161 — industry
      gold standard, APT tracking, rigorous attribution. This
      publication is a joint multi-team work-product: Mandiant
      Consulting (IR engagement primary observation), GTIG (cluster
      designation and attribution analysis), FLARE team (INFINITERED
      reverse engineering + YARA rule G_Backdoor_INFINITERED_1), and
      Workspace Security (Google Workspace compliance-rule abuse
      analysis on the "Patroit" exfiltration mechanism — Google's own
      product, first-party telemetry). Direct retrieval from
      cloud.google.com landing page succeeded for the 7th consecutive
      time (Mandiant RSS feedburner remains stale-persistent, 28
      consecutive failures from 15:30 PM 2026-06-14 — under-24h skip
      rule applied, source-health not mutated this sweep).
    provisional: false
  relay_primary:
    grade: B
    source_name: "SecurityWeek (Eduard Kovacs)"
    source_yaml_id: securityweek
    source_url: https://www.securityweek.com/chinese-hackers-target-medical-military-and-ai-research-in-north-america/
    published: 2026-06-15T14:07:45+00:00
    grade_rationale: >
      Pre-assigned B per source-grades.yaml line 871-876
      (provisional pending ratification; first cited 2026-05-06).
      Same-day relay of GTIG primary; credits GTIG explicitly; no
      independent telemetry. Faithful summary at vendor framing.
      Does NOT contribute to independent corroboration on the
      cluster anchor per INTEL-GRADING.md independence test.
    provisional: true
  relay_secondary:
    grade: B
    source_name: "BleepingComputer (Bill Toulas)"
    source_yaml_id: bleepingcomputer
    source_url: https://www.bleepingcomputer.com/news/security/chinese-hackers-breach-redcap-servers-steal-medical-research/
    published: 2026-06-15T14:00:00+00:00
    grade_rationale: >
      Pre-assigned B per source-grades.yaml line 843-848. Same-day
      relay of GTIG primary; credits GTIG explicitly; partial IOC
      reproduction (BebitaBarefoot774@gmail.com + "Patroit"
      compliance rule). No independent telemetry. Does NOT
      contribute to independent corroboration per INTEL-GRADING.md
      independence test.
    provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent                       # PRC-nexus medical / defense-intelligence espionage corpus-consistent
    - probably_true_no_contradicting_ab                  # No contradicting A/B-grade source
    - probably_true_claims_coherent                      # REDCap real platform, INFINITERED architecture conventional, Chikungunya-Guangdong correlation coherent, IOC set internally consistent
  rationale: >
    Probably True (2) qualifies cleanly on all three checklist
    conditions for the cluster anchor.

    Grade 1 (Confirmed) FAILS the independent-source condition:
    SecurityWeek and BleepingComputer are same-day relays that
    explicitly credit GTIG primary with no independent telemetry.
    Per INTEL-GRADING.md, "Two sources are NOT independent if one
    is a rewrite/aggregation of the other" — both relays
    aggregate GTIG; effective source count for the cluster anchor
    is ONE (GTIG primary). Independence test fails.

    On the dual-grade rule for the 13-IOC set: each indicator is
    A1 on FACTS per GTIG IR observation (the credibility-2 cluster
    grade is on the cluster-anchor operational claim level, not
    on each individual fact). Indicator forensic accuracy is
    treated as A1.

    The credibility-2 reading is the strongest defensible reading
    given the single-source originating evidence base; an A1
    reading would require a second independent vendor IR
    confirmation that has not yet surfaced.

corroboration:
  independent_sources:
    - mandiant                                              # GTIG primary direct retrieval — ORIGINATING EVIDENCE BASE
  independent: false
  test_passed: false
  test_failed_reason: >
    Two-source independence test fails on the cluster anchor.
    SecurityWeek (Eduard Kovacs) and BleepingComputer (Bill Toulas)
    are same-day relays that explicitly credit GTIG and contribute
    no independent telemetry or first-party observation. Per
    INTEL-GRADING.md independence test: "If you remove one
    source's reporting, does the other still stand independently?"
    Remove GTIG → SecurityWeek and BleepingComputer collapse to
    aggregation-only (no underlying evidence base). Remove
    SecurityWeek → BleepingComputer + GTIG still stands but
    independence still fails because BC traces to GTIG. Remove
    BleepingComputer → same. The cluster has ONE effective
    originating source on the cluster anchor.

    Single-source veto APPLIES on the entire cluster anchor (UNC6508
    attribution, campaign timeline, victim profile, INFINITERED
    architecture, 13-IOC set, Workspace abuse tradecraft). WEP
    capped at "likely" per INTEL-GRADING.md.

  veto_lift_conditions: >
    Independent A/B-grade vendor IR or government-attestation
    second source on UNC6508 designation, INFINITERED tradecraft,
    or any of the 13 indicators — e.g., Microsoft MSTIC publishing
    a parallel observation under a different cluster name or
    confirming UNC6508 via separate telemetry; CrowdStrike, Unit
    42, Recorded Future, or Microsoft DART publishing parallel
    coverage on independent evidence basis; CISA issuing a CSA
    referencing UNC6508; or first-party Splunk hit on any of the
    9 high-fidelity IOCs in defenseclaw_local or archimedes. Any
    such lift would elevate the cluster anchor to Confirmed (1)
    and WEP to "very likely" or higher pending red-team review.

first_party_precedence:
  applied: false
  splunk_query_summary: >
    9-IOC UNC6508 sentinel set: 23.169.65.49 + BebitaBarefoot774@gmail.com
    + 7 SHA-256 hashes for INFINITERED dropper / credential harvester /
    backdoor + the b49e334d GUID delimiter + the "INFINITERED" string
    keyword. Indexes: defenseclaw_local, archimedes. Lookback: -30d@d.
  splunk_evidence: >
    0 hits across both indexes at -30d. Sentinel run logged in raw-signal
    (raw-2026-06-15-flash-1200-001 substrate-level Splunk check + this
    sweep's sentinel file raw-2026-06-15-flash-1200-000). Silent Splunk
    does NOT disconfirm per Hard Rule 8 — Frank is not a North American
    academic medical research institution, is not a military health
    institution, is not running REDCap, and does not match the UNC6508
    target profile. Visibility-limited absence; expected outcome given
    target-profile mismatch. first_party_precedence.applied: false.
    No credibility adjustment; no source-grade revision.
  splunk_run_at: 2026-06-15T12:08:00-04:00
  recommendation_for_standing_set: >
    Recommend expanding the 19-IOC standing PeopleSoft/UNC6240 Splunk
    sentinel set by 9 high-fidelity UNC6508 IOCs (1 IP + 1 email + 7
    SHA-256) — see librarian_handoffs and ioc_sentinel_expansion below.
    Operator-deferred decision: keep two parallel tracking sets (19 +
    9) or fold into a unified 28-IOC set. Either path is doctrinally
    valid; recommend folded 28-IOC set for operational simplicity.
    Librarian-level handoff at next regeneration cycle.

single_source_veto_applied: true
single_source_veto_layer: >
  Cluster anchor in its entirety (UNC6508 attribution + campaign
  timeline + victim profile + INFINITERED architecture + 13-IOC set
  + Workspace compliance-rule abuse tradecraft). GTIG primary is the
  sole originating evidence base; SecurityWeek and BleepingComputer
  are relays that credit GTIG and contribute no independent telemetry.
single_source_veto_lift_conditions: >
  Independent A/B-grade vendor IR or government-attestation second
  source on UNC6508 designation, INFINITERED tradecraft, or any of
  the 9 high-fidelity IOCs. See veto_lift_conditions above for the
  enumeration.

wep_ceiling: likely
wep_layered:
  unc6508_attribution_to_prc_nexus_per_gtig_high_confidence: likely         # A2 + single-source veto cap
  campaign_existence_sept_2023_through_nov_2025: likely                     # A2 + single-source veto cap
  26_month_dwell_in_primary_victim_undetected: likely                       # A2 + single-source veto cap
  infinitered_modular_backdoor_three_module_architecture: likely            # A2 + single-source veto cap; FLARE primary on RE
  13_ioc_set_accuracy_and_forensic_observation: likely                      # A1 on facts per dual-grade rule, but cluster anchor capped at likely
  workspace_compliance_rule_patroit_exfiltration_mechanism: likely          # A2 + Google Workspace Security team is first-party on own product (Workspace), strengthens but does not lift single-source veto
  ad_sector_adjacency_at_targeting_priority_level_per_gtig_verbatim: likely # A2 + Trigger 5 calibration ruling (sector-level satisfies trigger)
  named_a_and_d_prime_victim_implicated: NOT_ASSERTED                       # No source names any A&D-prime; verifiable absence
  cross_walk_to_apt41_apt40_salt_volt_typhoon: NOT_ASSERTED                 # Hard Rule 2 — GTIG did not, Archimedes does not
  future_campaign_continuation_post_publication: likely                     # Historical PRC post-disclosure pattern: rotation rather than cessation
  detection_efficacy_of_published_yara_rule_g_backdoor_infinitered_1: likely # FLARE primary on its own RE work; defender side; not architecturally challengeable here

# Trigger 5 calibration (load-bearing for FLASH eligibility — see digraph_anchor)
trigger_5_calibration:
  policy_text: "Campaign explicitly targeting aerospace, defense, or watchlist companies AND active (not retrospective) AND multi-victim (not single-incident)"
  active_element: SATISFIED                                                 # Sept 2023 through Nov 2025+ per A1 primary
  multi_victim_element: SATISFIED                                           # "diverse set of national, state, and private medical entities" per A1 primary
  ad_sector_element: SATISFIED_AT_SECTOR_CATEGORY_LEVEL                     # GTIG verbatim "military health institutions" + "defense intelligence" + "uncrewed vehicle systems" + "Indo-Pacific command operations" + "cyber offensive programs" + "military readiness"
  ad_sector_calibration_ruling: >
    Sector-level A&D-adjacency per A1 primary verbatim satisfies the
    FLASH-POLICY Trigger 5 "aerospace, defense, or watchlist
    companies" element. The policy uses OR construction; "defense"
    sector category targeting is sufficient on its own and does NOT
    require named-prime-victim binding. The critical-override
    conditions explicitly use the stricter "A&D watchlist entity is
    NAMED as a target" language, demonstrating that named-binding is
    reserved for the once-a-year override path, not the sector-level
    Trigger 5 path. Erring low on this calibration would suppress
    PRC-nexus FLASH eligibility for the near-universal pattern of
    vendor IR not naming primes (NDA + counsel-driven non-attribution).
    Calibration is CONSERVATIVE because the WEP ceiling caps at
    "likely" via single-source veto regardless — the trigger
    determines FLASH eligibility, not WEP urgency.
  trigger_5_overall: POSITIVE
  operator_review_recommended: >
    Recommend operator review at next doctrine quarterly to decide
    whether Trigger 5 should explicitly affirm sector-level
    sufficiency in policy text (current ruling is grader-inferred
    from policy construction; could be made explicit) OR tighten to
    named-prime-victim binding (would suppress current finding's
    FLASH eligibility). Either way, document the doctrinal stance.

# Critical-override evaluation (per FLASH-POLICY.md)
critical_override_eval:
  cvss_10_0: false                          # No CVE assigned by GTIG — configuration / patch-hygiene REDCap exposure pattern
  active_exploitation_confirmed: true       # Campaign IS active per GTIG; but the override condition is conceptually CVE-gated paired with CVSS 10.0
  tracked_actor_involved: false             # UNC6508 NOT in _roster.yaml (24-actor roster); operator-deferred /new-actor candidate
  ad_watchlist_entity_named: false          # No named A&D-prime — "diverse set" framing only
  override_qualifies: false
  override_reason_blocked: >
    0 of 4 conditions met. No CVE assigned by primary (configuration /
    patch-hygiene REDCap exposure, not zero-day disclosure). UNC6508
    is NOT on the 24-actor Archimedes roster (operator-deferred
    /new-actor candidate per Hard Rule 2 — Archimedes does not
    originate roster additions). No A&D-watchlist entity is named as
    target — GTIG names sector categories (military health, defense
    intelligence, uncrewed vehicle systems, Indo-Pacific command,
    cyber offensive programs) without identifying any specific named
    A&D-prime contractor. Sector-level targeting suffices for Trigger
    5 but NOT for the critical-override (which has strictly tighter
    named-binding language). Standard active-hours posting rules
    apply (12:00 EDT is inside 09:00–21:00 active window — normal
    posting permitted, no quiet-hours queue, no override-bypass).

# Anti-noise rule 1 check (one FLASH per trigger topic per 24h)
anti_noise_24h_check:
  topic: "UNC6508 PRC-nexus 26-month campaign vs North American medical / military health / defense intelligence / AI research / uncrewed vehicle systems / Indo-Pacific command / cyber offensive programs via INFINITERED on exposed REDCap servers"
  prior_24h_findings_same_topic: []
  prior_24h_rejections_same_topic: []
  prior_24h_brief_coverage: false
  net_new: true
  anti_noise: PASS

# Cluster metadata
cluster:
  topic: "UNC6508 (PRC-nexus) 26-month espionage campaign against North American medical research + military health + defense intelligence + AI research + uncrewed vehicle systems + Indo-Pacific command + cyber offensive programs via INFINITERED modular backdoor on exposed legacy REDCap servers; Sept 2023 through Nov 2025+ activity duration; 13 high-fidelity indicators; GTIG primary direct retrieval; no named A&D-prime victim; UNC6508 NOT on Archimedes 24-actor roster (operator-deferred /new-actor candidate)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-15-flash-1200-001-gtig-mandiant-primary-unc6508-prc-nexus-medical-military-ai-research-north-america-infinitered-redcap-flash-candidate-ad-adjacent
  attribution_claims:
    - claimed_actor: "UNC6508"
      claimed_actor_descriptor: "People's Republic of China (PRC)-nexus threat actor"
      actor_in_roster: false
      claimed_by_sources: [mandiant]
      attribution_language_used: "UNC6508, a People's Republic of China (PRC)-nexus threat actor" (12 words, verbatim, GTIG vendor high-confidence framing)
      requires_analyst_review: true
      hard_rule_2_treatment: >
        Recorded as GTIG's vendor IR attribution at GTIG's
        high-confidence language, NOT originated or upgraded by
        Archimedes. Archimedes does NOT cross-walk UNC6508 to
        APT41, APT40, APT10, Salt Typhoon, Volt Typhoon, or any
        other existing PRC cluster — GTIG did not, Archimedes
        does not. Single-source veto applied to the attribution
        layer per INTEL-GRADING.md.
      operator_action_recommended: >
        /new-actor UNC6508 — high-quality candidate for the 24-actor
        roster. A1 primary disclosure with vendor high-confidence
        attribution language, espionage-motivated, PRC-nexus,
        explicit A&D-adjacent targeting categories (military health,
        defense intelligence, uncrewed vehicle systems, Indo-Pacific
        command, cyber offensive programs), custom modular backdoor
        (INFINITERED) with publicly published YARA rule
        G_Backdoor_INFINITERED_1, 26-month documented dwell.
        Grader surfaces; operator scaffolds. Per Hard Rule 5
        sign-off path applies only if threat-box scoring lands
        HIGH after scaffolding.

# Inclusion eligibility
inclusion:
  eligible_for:
    - flash                                # A2 clears B2 minimum + Trigger 5 POSITIVE + net-new topic + anti-noise PASS
    - daily_brief_action                   # A2 clears B2 minimum
    - daily_brief_monitoring               # A2 clears C3 minimum
    - weekly_synthesis                     # A2 clears C3 minimum
    - actor_profile_update                 # A2 clears B2 minimum; UNC6508 NOT on roster — actor-profiler can scaffold from this finding per operator /new-actor invocation
    - ioc_sentinel_expansion               # Standing Splunk sentinel set should grow from 19 to 28 (or two parallel 19 + 9 sets); operator-deferred decision

# Downstream handoff flags
analyst_review_required: true              # Attribution claim present (UNC6508 → PRC-nexus per GTIG); A&D-sector-targeting interpretation; potential ACH topic on PRC cluster taxonomy
red_team_review_required: false            # WEP ceiling = "likely" (single-source veto cap); red-team only mandatory at WEP >= "very likely" per FLASH-POLICY anti-noise rule 3
red_team_review:
  reviewed_at: null
  reviewed_by: null
  notes: >
    Not invoked. FLASH-POLICY anti-noise rule 3 makes red-team
    review mandatory only for FLASHes at WEP >= "very likely."
    This FLASH carries WEP "likely" on all layers per single-
    source veto cap; red-team review is therefore NOT mandatory.
    If a second independent A/B-grade vendor IR source surfaces
    in the next 24-48h (Microsoft MSTIC / Unit 42 / CrowdStrike /
    Recorded Future / Microsoft DART), the single-source veto
    lifts, WEP elevates to "very likely" or above, and red-team
    review becomes mandatory — re-grade required at that point
    via Mode 2 fast-path re-invocation.

red_team_review_complete: false
red_team_outcome: not_applicable
wep_ceiling_adjusted_by_red_team: null
publication_blocked: false

analysis_sections:
  sat_ach: null                            # Recommended ACH topic: UNC6508 cluster taxonomy vs alternative PRC cluster mappings (could this be an APT41 / APT40 / APT10 / Volt-adjacent sub-cluster GTIG has not yet cross-walked — competing-hypotheses against H1 "distinct cluster" as GTIG presents); also alternative-hypothesis: contractor / mercenary actor vs MSS / PLA / MPS direct attribution
  sat_kac: null                            # Recommended KAC topic: assumption that "26-month dwell" represents true campaign duration (could be lower bound if earlier compromise undetected); assumption that REDCap is the only initial-access vector (could be ancillary in a broader access campaign); assumption that Workspace compliance-rule abuse is a new TTP novel to UNC6508 (could be PRC-cluster-wide tradecraft observed independently elsewhere)

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-15-flash-1200]
retracted: false
retraction_brief_id: null

# Librarian handoffs
librarian_handoffs:
  - action: roster_addition_candidate_surface
    target: threats/threat-actors/_roster.yaml
    payload: >
      UNC6508 — operator-deferred /new-actor candidate. GTIG primary
      direct attribution, PRC-nexus, espionage-motivated, A&D-adjacent
      targeting categories per A1 primary verbatim (military health,
      defense intelligence, uncrewed vehicle systems, Indo-Pacific
      command, cyber offensive programs), custom INFINITERED modular
      backdoor with published YARA rule G_Backdoor_INFINITERED_1,
      26-month documented dwell. Surface to operator via finding +
      FLASH brief; do NOT originate scaffolding (operator runs
      /new-actor UNC6508 per Hard Rule 2 and Hard Rule 5 sign-off
      pathway).
  - action: ioc_sentinel_expansion_recommendation
    target: infrastructure/splunk-sentinel-config.yaml (or equivalent IOC tracking artifact)
    payload: >
      Recommend expanding standing Splunk sentinel IOC set from
      19 (current — PeopleSoft/UNC6240) to 28 by adding 9
      high-fidelity UNC6508 indicators: IP 23.169.65.49 +
      BebitaBarefoot774@gmail.com + 7 SHA-256 hashes
      (ba6b73b0..., db65c1b9..., c1ac43d2..., 8f015885...,
      51a57bfc..., 4efbef69..., 58bb2577...). Operator-deferred
      decision: unified 28-IOC set OR two parallel 19 + 9
      tracking sets. Grader-recommended: unified 28-IOC set for
      operational simplicity. Apply at next IOC index
      regeneration cycle (gitignored build artifact —
      regeneration is deterministic from actor / unattributed
      source files).
  - action: brief_handoff_flash
    target: briefer subagent
    payload: >
      FLASH-eligible per Trigger 5 POSITIVE + A2 clears B2 minimum.
      Single-topic FLASH per INTEL-BRIEF-STANDARDS.md FLASH format.
      Active-hours posting to #flash-alerts (12:00 EDT inside
      09:00-21:00 active window). NO red-team review prerequisite
      (WEP "likely" cap). Briefer must preserve Hard Rule 2 binding
      verbatim ("UNC6508, a People's Republic of China (PRC)-nexus
      threat actor" — GTIG language; NO cross-walk to existing PRC
      cluster names). Briefer must surface operator-deferred
      /new-actor UNC6508 candidacy. Briefer must surface
      IOC-sentinel expansion recommendation (19 → 28 unified or
      19 + 9 parallel).

# Vuln-tracker handoffs
vuln_tracker_handoffs:
  - action: not_applicable
    rationale: >
      No CVE assigned by primary. Initial access via "legacy
      vulnerable REDCap servers" is configuration / patch-hygiene
      exposure pattern, not CVE-bound zero-day or n-day disclosure.
      No vuln-tracker dossier scaffolding warranted. If REDCap
      project (Vanderbilt consortium) subsequently assigns a CVE
      retrospectively to the exploited code path, re-evaluate.

# Actor-profiler handoffs
actor_profiler_handoffs:
  - action: roster_addition_recommendation
    target: threats/threat-actors/_roster.yaml + threats/threat-actors/UNC6508/
    payload: >
      Surface UNC6508 to operator as /new-actor candidate. Profile
      scaffolding requires operator invocation (Hard Rule 2 -
      Archimedes does not originate roster additions; Hard Rule 5
      sign-off applies if threat-box scoring lands HIGH after
      scaffolding). Substrate available from GTIG primary direct
      retrieval: PRC-nexus attribution at vendor high-confidence,
      espionage-motivated, A&D-adjacent targeting (military health
      / defense intelligence / uncrewed vehicle systems / Indo-Pacific
      command / cyber offensive programs / military readiness /
      AI research), custom INFINITERED modular backdoor with public
      YARA rule, 26-month documented dwell (Sept 2023 → Nov 2025+),
      13 indicators across IP / email / filename / SHA-256 / GUID /
      host-artifact types, Google Workspace compliance-rule abuse
      tradecraft, ASUS-router OBF endpoint at 23.169.65.49 as
      administrative access source.
---

# UNC6508 — PRC-nexus threat actor — conducted 26-month espionage campaign against North American medical research, military health, defense intelligence, AI research, uncrewed vehicle systems, Indo-Pacific command operations, and cyber offensive programs via INFINITERED modular backdoor on exposed REDCap servers (GTIG primary disclosure 2026-06-15; 13 indicators captured; UNC6508 NOT on Archimedes roster — operator-deferred /new-actor candidate)

## Summary

Google Threat Intelligence Group (Mandiant + Mandiant Consulting + FLARE team + Workspace Security joint publication) published a primary disclosure on 2026-06-15 attributing a 26-month espionage campaign (September 2023 → November 2025+) to UNC6508, characterized by GTIG verbatim as "a People's Republic of China (PRC)-nexus threat actor" at vendor high-confidence framing. The campaign targets, per GTIG verbatim, a diverse set of national, state, and private medical entities across the United States and Canada — academic medical research institutions, world-renowned clinical providers, premier academic centers, military health institutions, professional advocacy groups, and health regulatory bodies — with research-priority collection on molecular discovery and clinical drug trials, state-level public health policy, military readiness, artificial intelligence, uncrewed vehicle systems, cyber offensive programs, Indo-Pacific command operations, and national defense intelligence. No named A&D-prime contractor is identified as a confirmed victim. Initial access was via vulnerable / legacy REDCap (Research Electronic Data Capture) servers running side-by-side with current installations; persistence via a help.php web shell deployed early; the custom INFINITERED modular backdoor (three modules: dropper, credential harvester, backdoor with C2) deployed approximately three months post-initial compromise; and exfiltration via abuse of a Google Workspace content compliance rule named "Patroit" (typo of "Patriot") forwarding emails matching geo-strategic, military, advanced-technology, and pathogen-research keywords (including "Chikungunya" correlating with the July 2025 Guangdong outbreak) to a threat-actor-controlled BebitaBarefoot774@gmail.com address (now disabled per GTIG). GTIG attributes the activity to UNC6508 as a distinct cluster and did NOT cross-walk to APT41, APT40, APT10, Salt Typhoon, Volt Typhoon, or any other named PRC cluster; per Hard Rule 2 Archimedes preserves this verbatim and originates no cross-walk. UNC6508 is NOT on the Archimedes 24-actor roster — operator-deferred /new-actor candidate. SecurityWeek (Eduard Kovacs) and BleepingComputer (Bill Toulas) are same-day relays crediting GTIG with no independent telemetry; per INTEL-GRADING.md they collapse to a single effective source. Single-source veto APPLIES on the cluster anchor; WEP ceiling caps at "likely" (not "very likely"). Splunk sentinel on a 9-IOC UNC6508 set across defenseclaw_local + archimedes at -30d returned 0 hits; silent Splunk does NOT disconfirm per Hard Rule 8 (Frank is not a North American medical / military health institution running REDCap — visibility-limited absence). FLASH-eligible per Trigger 5 (active multi-victim campaign vs A&D sector — sector-level A&D-adjacency per A1 primary satisfies the trigger; named-prime-victim binding is reserved for the stricter critical-override). Critical override does NOT apply (0 of 4 conditions met).

## Sources

### Google Threat Intelligence Group — Mandiant + FLARE + Workspace Security (mandiant, digraph: A2 cluster-anchor; A1 on facts per dual-grade rule)

- URL: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research
- Published: 2026-06-15
- Authors: Google Threat Intelligence Group joint publication — Mandiant (IR engagement primary), GTIG (cluster designation + attribution), FLARE team (INFINITERED reverse engineering + YARA rule G_Backdoor_INFINITERED_1), Workspace Security (Google Workspace compliance-rule abuse analysis on the "Patroit" exfiltration mechanism)
- Retrieval: Direct from cloud.google.com (Mandiant RSS feedburner remains stale-persistent — 28 consecutive failures from 15:30 PM 2026-06-14; under-24h skip rule applied this sweep). 7th consecutive direct-HTML success.
- Key claims:
  - UNC6508 is a People's Republic of China (PRC)-nexus threat actor (vendor high-confidence attribution)
  - 26-month campaign duration (September 2023 → November 2025+)
  - More than one year dwell time undetected in the primary victim
  - Diverse set of national, state, and private medical entities across the United States and Canada targeted
  - North American military health institutions, defense intelligence, AI research, uncrewed vehicle systems, Indo-Pacific command operations, cyber offensive programs, military readiness — explicit research-priority targeting categories
  - Initial access via vulnerable / legacy REDCap (Research Electronic Data Capture) servers exposed and running side-by-side with current installations
  - help.php web shell deployed early in compromise chain
  - INFINITERED three-module backdoor deployed ~3 months post-initial compromise: dropper + credential harvester (uses xc32038474a database session ID prefix as forensic marker) + backdoor with C2 (uses b49e334d-9c01-463e-9bc5-00a6920fb66e GUID as persistence marker)
  - Exfiltration via Google Workspace content compliance rule "Patroit" (typo of "Patriot") forwarding matching emails to BebitaBarefoot774@gmail.com (account now disabled per GTIG)
  - Administrative access source: compromised ASUS router at 23.169.65.49 (US-based OBF / Operational Relay Box endpoint)
  - YARA rule G_Backdoor_INFINITERED_1 published for INFINITERED detection (referenced by name and link to GTIG primary; not reproduced verbatim in this finding per Hard Rule 3)
  - 13 high-fidelity indicators (1 IPv4 + 1 email + 1 filename + 7 SHA-256 + 1 GUID + 2 host artifacts) — full table below
- Hard Rule 2 binding: GTIG explicitly did NOT cross-walk UNC6508 to any existing named PRC cluster (APT41, APT40, APT10, Salt Typhoon, Volt Typhoon). Archimedes preserves verbatim; does NOT originate any cross-walk.

### SecurityWeek — Eduard Kovacs (securityweek, digraph: B3 — relay, not independent corroboration)

- URL: https://www.securityweek.com/chinese-hackers-target-medical-military-and-ai-research-in-north-america/
- Published: 2026-06-15T14:07:45+00:00 (10:07 EDT)
- Key claim: Same-day relay of GTIG primary; credits GTIG explicitly; faithful summary at vendor framing; no independent telemetry.
- Independence test: FAILS — aggregation of GTIG; does NOT contribute to independent corroboration per INTEL-GRADING.md.

### BleepingComputer — Bill Toulas (bleepingcomputer, digraph: B3 — relay, not independent corroboration)

- URL: https://www.bleepingcomputer.com/news/security/chinese-hackers-breach-redcap-servers-steal-medical-research/
- Published: 2026-06-15T14:00:00+00:00 (10:00 EDT)
- Key claim: Same-day relay of GTIG primary; credits GTIG explicitly; partial IOC reproduction (BebitaBarefoot774@gmail.com + "Patroit" compliance rule name); no independent telemetry.
- Independence test: FAILS — aggregation of GTIG; does NOT contribute to independent corroboration per INTEL-GRADING.md.

## Technical detail

- **Attribution (per GTIG verbatim):** "UNC6508, a People's Republic of China (PRC)-nexus threat actor" at vendor high-confidence framing. GTIG attributes based on infrastructure overlaps between campaigns, consistent INFINITERED deployment on REDCap servers, and the specific targeting of medical research and defense sectors. UNC6508 is presented as a distinct cluster — GTIG did NOT cross-walk to any existing PRC cluster. Per Hard Rule 2, Archimedes preserves verbatim and originates no cross-walk.
- **Roster status:** UNC6508 is NOT on the Archimedes 24-actor roster (`_meta.total_actors: 24`, last_updated 2026-05-10). Operator-deferred `/new-actor` candidate.
- **Campaign timeframe:** Earliest known compromise September 2023; observed activity duration through November 2025+; dwell time before detection in primary victim "more than one year"; GTIG publication 2026-06-15 (today).
- **Initial access vector:** Vulnerable / legacy REDCap (Research Electronic Data Capture) servers — exposed web-based medical research database platform widely used by academic medical centers (Vanderbilt consortium, 5000+ institutions globally). Targeting pattern: threat actor probed for legacy/vulnerable REDCap versions running side-by-side with current installations. **No specific CVE assigned by primary** — configuration / patch-hygiene exposure pattern.
- **Persistence (early):** `help.php` web shell deployed early in compromise chain on REDCap servers.
- **Persistence (mature):** INFINITERED modular backdoor deployed approximately three months post-initial-compromise. Three modules:
  1. Dropper / Upgrade Interception — initial installation + ongoing update capability
  2. Credential Harvester — captures REDCap database session credentials; uses database session ID prefix `xc32038474a` as forensic marker
  3. Backdoor with C2 — persistent communication channel; uses GUID `b49e334d-9c01-463e-9bc5-00a6920fb66e` as persistence marker
- **YARA rule:** G_Backdoor_INFINITERED_1 published by FLARE team — covers magic flags, markers, code patterns (plaintext + base64-encoded variants). Referenced by name and link only; NOT reproduced verbatim in this finding per Hard Rule 3 (detection content not exploitation content; defender side; out of scope for in-corpus reproduction).
- **Exfiltration mechanism:** Google Workspace content compliance rule abuse — rule named "Patroit" (typo of "Patriot") configured to capture and forward emails matching geo-strategic policy, military strategy, advanced technology, and pathogen-research keywords (explicitly including "Chikungunya" — correlating with the July 2025 Guangdong province outbreak). Exfiltration destination: BebitaBarefoot774@gmail.com (account now disabled per GTIG).
- **Administrative access source:** Compromised ASUS router at 23.169.65.49 — US-based Operational Relay Box (OBF) endpoint. Shodan internetdb on 23.169.65.49 returned `found: false`, consistent with a residential / SOHO consumer device used as a relay rather than a permanently-internet-facing C2.
- **Splunk first-party check:** 9-IOC UNC6508 sentinel set queried across defenseclaw_local + archimedes at -30d@d; 0 hits. Silent Splunk does NOT disconfirm per Hard Rule 8 — Frank is not a North American medical / military health institution running REDCap. Visibility-limited absence; expected outcome given target-profile mismatch. `first_party_precedence.applied: false`. Recommend expanding standing 19-IOC PeopleSoft/UNC6240 set to unified 28-IOC set (or two parallel 19 + 9 tracking sets) — operator-deferred decision.

## IOCs surfaced

```yaml
iocs:
  - indicator: 23.169.65.49
    type: ipv4
    context: "US-based OBF (Operational Relay Box) — compromised ASUS router used as administrative login source"
    confidence: A1
    fidelity: high
    sentinel_candidate: true
    splunk_first_party_check: 0_hits_at_minus_30d_visibility_limited_absence

  - indicator: BebitaBarefoot774@gmail.com
    type: email
    context: "Exfiltration destination for 'Patroit' Google Workspace content compliance rule; account now disabled per GTIG"
    confidence: A1
    fidelity: high
    sentinel_candidate: true
    splunk_first_party_check: 0_hits_at_minus_30d_visibility_limited_absence

  - indicator: help.php
    type: filename
    context: "Web shell deployed early in compromise chain on REDCap servers"
    confidence: A1
    fidelity: medium                                              # generic filename; hash-pivoting recommended
    sentinel_candidate: false                                     # filename alone is too generic for sentinel

  - indicator: ba6b73b0ca0dc7f86b3b397893ac32d729fd53f9df20643288f141f29d020af7
    type: sha256
    context: "Persistence (help.php web shell binary hash)"
    confidence: A1
    fidelity: high
    sentinel_candidate: true

  - indicator: db65c1b9f9e4cb4d729f45ad4b6fcf3e277caf9eb4c875425dec93fd883f9136
    type: sha256
    context: "INFINITERED credential harvester binary hash"
    confidence: A1
    fidelity: high
    sentinel_candidate: true

  - indicator: c1ac43d23f89d41eb4ff131678ab562ab2cfed9aa334b13767ef141d303b0e5b
    type: sha256
    context: "INFINITERED credential harvester binary hash (second variant)"
    confidence: A1
    fidelity: high
    sentinel_candidate: true

  - indicator: 8f0158855a656b629ca76ebca565f18bc25563ded34b65d6771632c20edb68ec
    type: sha256
    context: "INFINITERED backdoor binary hash"
    confidence: A1
    fidelity: high
    sentinel_candidate: true

  - indicator: 51a57bfc9ed3eb6451c1c289607814d59e1698c666fb97ac5f694c398f23d045
    type: sha256
    context: "INFINITERED backdoor binary hash (second variant)"
    confidence: A1
    fidelity: high
    sentinel_candidate: true

  - indicator: 4efbef69eb3b09bacff892d6a55778d07c418e7f15eba3cf1245e8cdfd8dda0b
    type: sha256
    context: "INFINITERED dropper binary hash"
    confidence: A1
    fidelity: high
    sentinel_candidate: true

  - indicator: 58bb25777e0aa86bcd2125101e0bca4e8732b03d91bd8d2f205b446a2a8d5c86
    type: sha256
    context: "INFINITERED dropper binary hash (second variant)"
    confidence: A1
    fidelity: high
    sentinel_candidate: true

  - indicator: b49e334d-9c01-463e-9bc5-00a6920fb66e
    type: guid
    context: "INFINITERED backdoor persistence marker (host artifact — registry / config marker)"
    confidence: A1
    fidelity: high
    sentinel_candidate: true

  - indicator: xc32038474a
    type: host_artifact
    context: "INFINITERED credential harvester database session ID prefix (forensic marker visible in REDCap session logs)"
    confidence: A1
    fidelity: medium                                              # short string; potential for false positives in non-targeted environments

  - indicator: Patroit
    type: host_artifact
    context: "Google Workspace content compliance rule name used for exfiltration (typo of 'Patriot') — detection in Workspace admin audit logs"
    confidence: A1
    fidelity: high                                                # specific to this campaign; uncommon string

attribution_claims:
  - actor: UNC6508
    actor_descriptor: "People's Republic of China (PRC)-nexus threat actor"
    actor_in_roster: false
    attributed_by: [mandiant]
    attribution_confidence_per_source: high
    attribution_language: "UNC6508, a People's Republic of China (PRC)-nexus threat actor"
    archimedes_treatment: recorded_as_gtig_claim_not_originated
    cross_walk_to_existing_roster_actor: NONE_per_hard_rule_2_gtig_did_not_cross_walk_either
    single_source_veto_applied: true
    wep_cap_for_attribution_layer: likely
    operator_action_recommended: "/new-actor UNC6508"

ioc_sentinel_expansion_recommendation:
  current_standing_set: 19_iocs_peoplesoft_unc6240_shinyhunters
  recommended_expansion: 9_high_fidelity_unc6508_iocs (1_ipv4 + 1_email + 7_sha256)
  recommended_final_set_size_unified_path: 28
  alternative_parallel_path: keep_19_peoplesoft_set_and_9_unc6508_set_separately
  grader_recommendation: unified_28_ioc_set_for_operational_simplicity
  operator_deferred_decision: true
  apply_at: next_ioc_index_regeneration_cycle
```

## Relationship to existing findings

UNC6508 is a **first-time observation** in the Archimedes corpus. No prior FLASH or finding mentions UNC6508, INFINITERED, REDCap, or the Patroit Workspace compliance-rule abuse mechanism. Adjacent precedent class:

- **PRC-cluster taxonomy precedent:** UNC6240 (ShinyHunters partnership; finding-2026-06-12-0001 / 0002 / 0006 / 2026-06-13-0002 / 0006) is a separate UNC-numbered cluster tracked at Mandiant on a different campaign (Oracle PeopleSoft CVE-2026-35273 extortion). The "UNC" prefix is Mandiant's pre-attribution numbering for clusters not yet promoted to named-APT designation. UNC6508 and UNC6240 are distinct clusters; no cross-walk is asserted or implied by GTIG. Archimedes does not cross-walk either.
- **Velvet Ant Operation Highland (Sygnia primary, finding-2026-06-12-0004) — PRC-nexus persistence-focused cluster with 10-year dwell.** UNC6508 and Velvet Ant are BOTH PRC-nexus persistence-focused actors with multi-year dwell times, BUT GTIG does NOT cross-walk between them. Archimedes preserves the distinction per Hard Rule 2 — independent clusters per primary attribution.
- **APT41 medical / biotech targeting precedent (general corpus knowledge):** PRC-nexus targeting of medical research and biotech is a corpus-consistent pattern across multiple PRC clusters historically (APT41 pandemic-era health-data targeting; CrowdStrike PANDA-cluster biotech research targeting). The UNC6508 targeting profile is consistent with this broader pattern WITHOUT requiring cross-walk to any specific named PRC cluster. Pattern-consistency strengthens credibility-2 reading; does not lift single-source veto.
- **Workspace compliance-rule abuse as exfiltration mechanism:** First observation in the Archimedes corpus. Google Workspace Security team is first-party on its own product (Workspace), which strengthens the credibility of the abuse-mechanism observation but does not lift the single-source veto on the cluster anchor.

## Open questions for analyst

- **SAT-ACH topic (recommended):** UNC6508 cluster taxonomy alternatives. GTIG presents UNC6508 as a distinct cluster — competing hypotheses worth weighing: (a) UNC6508 is genuinely a distinct PRC cluster Mandiant has not yet promoted to a named-APT designation (H1 — GTIG's implied reading); (b) UNC6508 is a sub-cluster of APT41, APT40, APT10, or another existing PRC named-APT that Mandiant has not yet cross-walked; (c) UNC6508 is a contractor / mercenary actor working under PRC tasking rather than an MSS / PLA / MPS direct unit (the "nexus" framing leaves attribution-depth ambiguous); (d) UNC6508 is a placeholder cluster designation aggregating activity from multiple distinct actors observed on REDCap victims. ACH would weigh these against H1 using GTIG's evidence basis. Hard Rule 2 prohibits Archimedes from originating a cross-walk regardless of ACH outcome — the ACH output is a confidence-level statement on H1, not a competing attribution claim.
- **SAT-KAC topic (recommended):** Assumption that the 26-month dwell time (Sept 2023 → Nov 2025+) represents the true campaign duration. Plausible lower bound only — earlier compromise may have gone undetected. Assumption that REDCap is the ONLY initial-access vector. Could be the most-observed vector in Mandiant's IR sample without being exhaustive — UNC6508 may have parallel initial-access paths against non-REDCap targets that this sample does not surface. Assumption that the "Patroit" Workspace compliance-rule abuse is a novel TTP unique to UNC6508. Could be PRC-cluster-wide tradecraft observed independently elsewhere — Google Workspace Security would be the natural surface to observe this, but other PRC-tracking vendor research (Microsoft, MSTIC, Recorded Future) may not have parallel visibility into the Workspace audit logs.
- **Hard Rule 2 attribution boundary:** UNC6508 attribution is GTIG's vendor IR claim at high-confidence framing. Archimedes preserves "PRC-nexus" verbatim. NO cross-walk to APT41, APT40, APT10, Salt Typhoon, Volt Typhoon, or any other named PRC cluster — GTIG did not, Archimedes does not. If a second independent A/B-grade vendor IR source (Microsoft MSTIC / Unit 42 / CrowdStrike / Recorded Future / Microsoft DART) publishes parallel observation of UNC6508 — either confirming the distinct-cluster reading or cross-walking to a named PRC actor — single-source veto lifts and re-grade is required.
- **Trigger 5 calibration ruling (operator review recommended):** The grader's Trigger 5 ruling is that sector-level A&D-adjacency per A1 primary verbatim satisfies the trigger; named-prime-victim binding is reserved for the critical-override. Reasoning is documented in `trigger_5_calibration` block above. Operator review recommended at next doctrine quarterly to decide whether to affirm sector-level sufficiency in policy text explicitly or tighten to named-prime-victim binding.
- **Operator action recommended:** `/new-actor UNC6508` — high-quality candidate for the 24-actor roster. Substrate: A1 GTIG primary, PRC-nexus at vendor high-confidence framing, espionage-motivated, A&D-adjacent targeting categories (military health, defense intelligence, uncrewed vehicle systems, Indo-Pacific command, cyber offensive programs), custom modular backdoor (INFINITERED) with public YARA rule G_Backdoor_INFINITERED_1, 26-month documented dwell. Hard Rule 5 threat-box sign-off path applies only if scoring lands HIGH after scaffolding.
- **IOC sentinel expansion recommendation:** Recommend expanding standing Splunk sentinel set from 19 (current — PeopleSoft / UNC6240) to 28 by adding 9 high-fidelity UNC6508 indicators (1 IPv4 + 1 email + 7 SHA-256). Operator-deferred decision: unified 28-IOC set OR parallel 19 + 9 tracking sets. Grader-recommended: unified 28-IOC set for operational simplicity. Apply at next IOC index regeneration cycle (gitignored build artifact; deterministic regeneration from actor / unattributed source files).

## Recovery handoff to briefer

- **FLASH brief eligibility: YES.** A2 clears B2 minimum; net-new topic (no prior 24h same-topic coverage); Trigger 5 POSITIVE per sector-level A&D-adjacency calibration; anti-noise PASS.
- **Recommended briefer disposition:** Single-topic FLASH per INTEL-BRIEF-STANDARDS.md FLASH format. Active-hours posting to `#flash-alerts` (12:00 EDT is inside the 09:00–21:00 active window — normal posting, no quiet-hours queue, no override bypass). NO red-team review prerequisite (WEP "likely" cap via single-source veto — FLASH-POLICY anti-noise rule 3 makes red-team mandatory only at WEP ≥ "very likely").
- **Hard Rule 2 binding (briefer-load-bearing):** Preserve "UNC6508, a People's Republic of China (PRC)-nexus threat actor" verbatim. NO cross-walk to APT41 / APT40 / APT10 / Salt Typhoon / Volt Typhoon — GTIG did not, Archimedes does not. NO assertion of a named A&D-prime victim (none exists in primary).
- **Hard Rule 6 binding (briefer-load-bearing):** Quote limits — under 15 words per quote, one quote per source. The verbatim attribution string is 12 words and GTIG-only. Other content paraphrased.
- **Carry-forward suggestions for the 16:00 PM brief:** Include in Actors section (UNC6508 + operator-deferred /new-actor candidate flag); include in Targeting section (A&D-adjacent sector-category targeting per A1 primary); include 13 IOCs in IOCs section; surface IOC-sentinel expansion recommendation (19 → 28 unified or 19 + 9 parallel) for operator review at PM brief or next morning brief.
- **Splunk sentinel expansion (librarian-handoff at next regeneration cycle):** Recommend 19 → 28 unified set OR 19 + 9 parallel sets; operator-deferred decision; grader-recommended: unified 28-IOC set.

## Compliance attestations

- Hard Rule 1 (LEGAL-POLICY): all sources public OSINT; no prohibited query patterns; no exploitation assistance; no active recon. PASS.
- Hard Rule 2 (no novel attribution): UNC6508 = "PRC-nexus" preserved verbatim from GTIG; NO cross-walk to APT41/APT40/APT10/Salt Typhoon/Volt Typhoon originated. PASS.
- Hard Rule 3 (no exploitation content): YARA rule G_Backdoor_INFINITERED_1 referenced by name + link to GTIG primary; NOT reproduced verbatim. IOCs at indicator level only; no PoC / exploit chain / technical walkthrough. PASS.
- Hard Rule 5 (HIGH threat-box sign-off): N/A at finding stage; applies only if /new-actor UNC6508 scaffolding lands HIGH on subsequent threat-box scoring per `THREAT-BOX-METHODOLOGY.md`.
- Hard Rule 6 (15-word quote limit, one quote per source): verbatim 12-word attribution string used once; all other content paraphrased. PASS.
- Hard Rule 7 (credentials radioactive): BebitaBarefoot774@gmail.com is a threat-actor-controlled exfiltration destination (now disabled per GTIG), recorded as an IOC indicator — not a credential. No credentials in raw-signal or finding. PASS.
- Hard Rule 8 (Splunk first-party precedence): 9-IOC sentinel run, 0 hits at -30d, silent Splunk does NOT disconfirm (target-profile mismatch — Frank not a North American medical / military health institution running REDCap). first_party_precedence.applied: false. PASS.
