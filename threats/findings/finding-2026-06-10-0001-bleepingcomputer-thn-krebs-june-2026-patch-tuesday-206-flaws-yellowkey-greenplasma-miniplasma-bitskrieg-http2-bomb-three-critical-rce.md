---
finding_id: finding-2026-06-10-0001-bleepingcomputer-thn-krebs-june-2026-patch-tuesday-206-flaws-yellowkey-greenplasma-miniplasma-bitskrieg-http2-bomb-three-critical-rce
created_at: 2026-06-10T08:14:00-04:00
graded_by: grader
grading_run_id: morning-20260610-080000
grading_mode: scheduled_brief
test: false
status: graded

relates_to:
  - finding-2026-06-03-0002-bleepingcomputer-vs-code-github-oauth-token-theft-zero-day-askar-poc-full-disclosure-microsoft-disclosure-policy-current
  - finding-2026-06-03-0003-securityweek-thn-http2-bomb-cve-2026-49975-nginx-apache-iis-envoy-pingora-dos-mixed-patch-calif-codex-disclosure
relation_type: continuing_coverage_nightmare_eclipse_researcher_series_plus_http2_bomb_cluster_extension

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  june_2026_patch_tuesday_206_flaws_patched: B1                      # BleepingComputer + THN + Krebs three-source independent agreement on top-line patch volume (THN 206, Krebs "nearly 200" — within rounding tolerance). Three B-grade publisher-independent primaries.
  three_publicly_disclosed_zero_days_yellowkey_greenplasma_miniplasma_patched: B1  # Same three-source consensus on the trio identification and patched-at-disclosure framing.
  yellowkey_cve_2026_45585_bitlocker_winre_bypass_cvss_6_8: B1       # CVE assignment + CVSS + class consistent across BC + THN; verifiable in NVD per established CVE-procedural-class
  greenplasma_cve_2026_45586_ctfmon_lpe_cvss_7_8: B1                 # CVE assignment + CVSS + class consistent across BC + THN
  miniplasma_cve_2020_17103_cloud_files_mini_filter_driver_lpe_incomplete_prior_fix_re_patched: B1  # BC + THN consistent on framing
  greenplasma_actively_exploited_in_attacks_itw_claim: B3            # BleepingComputer single-source on ITW framing; THN frames as "publicly disclosed"; Krebs does NOT label as ITW. Single-source veto applies on the ITW claim specifically.
  miniplasma_actively_exploited_itw_claim: B3                        # Same single-source veto posture as GreenPlasma — BC sole-originator on ITW
  bitskrieg_cve_2026_50507_bitlocker_eop_patched: B2                 # Krebs + THN cross-corroborate on patch + class; THN adds bitskrieg lineage explicit; BC less explicit on this specific CVE in retrieved text
  http2_bomb_cve_2026_49160_iis_dos_patched: B2                      # Krebs + THN cross-corroborate; carry-context to finding-2026-06-03-0003 HTTP/2 Bomb multi-server cluster
  three_critical_non_zero_day_rce_chain_cve_2026_45657_47291_44815_cvss_9_8: B2  # THN single-originating with explicit CVSS list; not contradicted; no ITW reported
  nightmare_eclipse_chaotic_eclipse_researcher_pseudonym_attribution: B1  # All three sources attribute to researcher pseudonym; this is researcher-pseudonym NOT threat-actor attribution — Hard Rule 2 PRESERVED
  nightmare_eclipse_former_microsoft_employee_self_claim: B3         # Krebs single-source on this self-claim; Microsoft has not confirmed per Krebs; not load-bearing
  nightmare_eclipse_pledges_more_zero_days_july_14_2026_predictive_claim: C3  # Predictive claim attributed to researcher pseudonym; Krebs single-source; defender-prudent monitoring framing only
  rapid7_barnett_360_browser_vulns_patched_10x_normal_observation: B2  # Krebs sole-originator quoting Rapid7 Adam Barnett; observation by reputable IR firm but single-source-citation
  zd_001_bluehammer_state_transition_resolution_pending_vuln_tracker_verification: C3   # Internal corpus state; pending vuln-tracker direct MSRC retrieval; cannot grade resolution at this hour
  zd_002_redsun_state_transition_resolution_pending: C3              # Same posture as ZD-001
  zd_003_undefend_state_transition_resolution_pending: C3            # Same posture; RoguePlanet is SEPARATE Defender issue and does NOT close UnDefend
  no_a_grade_a_d_prime_named_victim: B1                              # Verifiable absence in primaries; structural Windows-deployment exposure only
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored on three independent B-grade publisher-independent
  primary sources covering June 2026 Microsoft Patch Tuesday:
  BleepingComputer (Sergiu Gatlan, 2026-06-10T09:57:33 UTC),
  The Hacker News (Ravie Lakshmanan, 2026-06-10T09:38:13 UTC),
  and Krebs on Security (Brian Krebs, 2026-06-09T22:07:28 UTC).
  All three are pre-assigned B per source-grades.yaml. THN is
  provisional B; Krebs and BleepingComputer are ratified B.

  B2 (not B1, not B3) anchored because:

    - SOURCE LETTER GRADE: All three sources are B (no A-grade
      primary retrieved this sweep — no MSRC blog post, no
      Mandiant / Volexity / Unit 42 dedicated writeup on the
      Nightmare-Eclipse zero-day cluster in the 14h window). The
      cluster-anchor letter grade holds at B under conservative
      lowest-common-grade aggregation. A future MSRC technical
      writeup or first-party IR firm telemetry would lift to B1
      with A-grade corroboration.

    - INDEPENDENCE TEST: Three independent publishers (BC, THN,
      Krebs are three different organizations). None cites
      another as origin in the retrieved text. Different evidence
      bases: BC has direct MSRC advisory retrieval; THN has
      direct MSRC advisory retrieval + ZDI cross-reference;
      Krebs has direct MSRC advisory retrieval + quoted Rapid7
      analyst (Adam Barnett) commentary. Independence test
      PASSES on procedural facts (patch volume, CVE identifiers,
      CVSS scores, patched-at-disclosure framing, researcher-
      pseudonym attribution).

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed) — would require A-grade independent
        corroboration. No A-grade primary in window. Falls back.
      * Grade 2 (Probably True) — PASSES: consistent with
        established Microsoft Patch Tuesday cadence + the prior
        Nightmare-Eclipse researcher-series chain (Bitskrieg /
        BlueHammer / UnDefend / RedSun / RoguePlanet — eight
        disclosures deep across prior corpus surfaces);
        no contradicting A/B source; technical claims
        internally coherent (CVE IDs structurally valid; CVSS
        values reasonable; CTFMON / WinRE / Cloud Files Mini
        Filter Driver are documented Windows subsystems).

    - SUBSTANTIVE CLAIM LAYERS that warrant separate grading:
      * Procedural facts (patch volume, CVE IDs, CVSS scores,
        patched-at-disclosure, researcher-pseudonym credit):
        B2 cluster anchor with multi-source corroboration.
      * GreenPlasma + MiniPlasma "actively exploited in attacks"
        ITW claim: BleepingComputer SINGLE-SOURCE on this
        specific framing. THN frames as "publicly disclosed"
        (PoC-public, no explicit ITW). Krebs does not label
        as ITW. Per skill Step 4 independence test, ITW claim
        collapses to ONE effective source (BC). SINGLE-SOURCE
        VETO applies on the ITW layer. WEP capped at "likely"
        on the ITW claim. This is the load-bearing distinction
        — defender response is patch-urgency (vendor patches
        available) regardless of ITW status, but Archimedes
        does not assert as confirmed without independent
        corroboration.
      * Three critical-class non-zero-day RCEs (CVE-2026-45657
        kernel UAF, CVE-2026-47291 HTTP.sys integer overflow,
        CVE-2026-44815 DHCP Client stack buffer overflow at
        CVSS 9.8 each): THN originating with explicit CVSS
        list; Krebs covers patch volume framing; BC less
        explicit on these three. Two-source partial
        corroboration. No ITW reported by any source.
      * bitskrieg / HTTP/2 Bomb IIS lineage: Krebs + THN
        corroborate; carry-context to finding-2026-06-03-0003
        (HTTP/2 Bomb multi-server cluster) preserved.

  Single-source veto APPLIED on:
    - GreenPlasma + MiniPlasma "actively exploited" ITW claim
      (BC single-source; THN reframes as "publicly disclosed";
      Krebs not explicit). WEP ceiling "likely" on ITW layer.
    - Nightmare-Eclipse "former Microsoft employee" self-claim
      (Krebs single-source; Microsoft has not confirmed).
    - Nightmare-Eclipse "more zero-days July 14" predictive
      claim (Krebs single-source quoting researcher pseudonym).
    - Rapid7 Adam Barnett "360 browser vulns 10x normal" claim
      (Krebs single-source quoting Rapid7 analyst).

  Single-source veto NOT applied on:
    - Patched-at-disclosure procedural facts (CVE IDs, CVSS,
      patch volume, researcher-pseudonym credit) at three-
      source B-grade convergence. WEP ceiling "very likely"
      on procedural facts.

  Hard Rule 2 binding constraint: PRESERVED — Nightmare-Eclipse
  / Chaotic Eclipse is researcher pseudonym, NOT a tracked
  threat actor. Archimedes does NOT roster-tier this researcher.
  Coverage is vuln-tracker / researcher-series tracking only.
  All three sources preserve researcher-pseudonym credit
  language; Archimedes does not originate or transform that
  language into threat-actor attribution.

  Hard Rule 3 binding constraint: PRESERVED — no PoC content,
  no exploit chain detail, no technical walkthrough captured.
  Mechanism descriptions ("BitLocker bypass via WinRE",
  "LPE in CTFMON", "LPE in Cloud Files Mini Filter Driver")
  are architectural-class descriptions, not exploitation
  guidance.

  Hard Rule 6: PRESERVED — all source quotes ≤15 words; one
  quote per source maximum in finding text.

  Hard Rule 8 binding constraint: Splunk first-party check ran
  (-30d sweep against CVE IDs + Nightmare-Eclipse keywords on
  index=archimedes OR index=defenseclaw_local). 0 substantive
  events (25 events all sourcetype `archimedes:operation`
  self-instrumentation). Silence preserved as data point per
  the persistent dormant-non-self-telemetry pattern; not
  disconfirming external claims.

source_reliability:
  grade: B
  source_name: "BleepingComputer (Sergiu Gatlan) — 'Microsoft patches YellowKey, GreenPlasma, MiniPlasma zero-days' (2026-06-10), paired with The Hacker News (Ravie Lakshmanan) 'Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs' (2026-06-10) and Krebs on Security (Brian Krebs) 'A Record-Breaking Patch Tuesday for June 2026' (2026-06-09) — three independent B-grade publisher-independent primaries"
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    Pre-assigned B per source-grades.yaml — ratified B for
    BleepingComputer and Krebs; provisional B for The Hacker
    News (since 2026-05-14). Three publisher-independent
    B-grade media outlets with different bylines and different
    publishers covering the same Microsoft Patch Tuesday
    primary source. No A-grade primary (MSRC blog, Mandiant,
    Unit 42) retrieved this sweep on the Nightmare-Eclipse
    cluster specifically.
  provisional: false
  cluster_secondary_sources:
    - source_yaml_id: thehackernews
      grade: B
      provisional: true
      grade_rationale: "Pre-assigned B per source-grades.yaml; provisional since 2026-05-14"
      role: independent_publisher_primary
    - source_yaml_id: krebs
      grade: B
      provisional: false
      grade_rationale: "Pre-assigned B per source-grades.yaml; ratified"
      role: independent_publisher_primary

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_microsoft_patch_tuesday_cadence_and_nightmare_eclipse_researcher_series_chain
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_technical_claims_internally_coherent_cve_ids_structurally_valid_cvss_reasonable_windows_subsystems_documented
    - probably_true_three_independent_b_grade_publishers_corroborate_procedural_facts
  rationale: >
    Three independent B-grade publishers converge on procedural
    facts (Microsoft June 2026 Patch Tuesday patched 206 flaws
    including three publicly-disclosed zero-days attributed to
    Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym;
    patched-at-disclosure framing on the trio plus bitskrieg
    BitLocker EoP + HTTP/2 Bomb IIS variant + three critical
    9.8 RCEs). Single-source veto applies on the
    GreenPlasma + MiniPlasma "actively exploited" ITW
    framing (BC single-source); WEP capped at "likely" on the
    ITW claim layer. No contradicting A/B source. Technical
    claims internally coherent. Grade 1 (Confirmed) would
    require A-grade independent corroboration, which is not
    present in window — MSRC blog and Tier-1 IR firm telemetry
    on the Nightmare-Eclipse cluster were not retrieved this
    sweep.

corroboration:
  independent_sources:
    - bleepingcomputer
    - thehackernews
    - krebs
  independent: true
  test_passed: >
    Three independent publishers, different bylines, different
    organizations, none cites another as origin in retrieved
    text. Different evidence bases (each independently retrieved
    MSRC advisories; Krebs additionally quotes Rapid7 analyst
    Adam Barnett commentary). Removing any one of the three
    leaves the other two standing on their own retrieval.
    Independence test PASSES on procedural facts. FAILS on
    GreenPlasma + MiniPlasma "actively exploited" ITW claim
    layer (BC single-source; THN reframes; Krebs not explicit).
  test_failed: >
    Independence FAILS on GreenPlasma + MiniPlasma "actively
    exploited" ITW claim layer (BC single-source on this
    specific framing). Independence FAILS on Nightmare-Eclipse
    "former Microsoft employee" self-claim (Krebs single-source).
    Independence FAILS on Nightmare-Eclipse "July 14 more
    zero-days" predictive claim (Krebs single-source quoting
    researcher pseudonym). Independence FAILS on Rapid7
    Barnett "360 browser vulns" commentary (Krebs single-source
    quoting Rapid7 analyst).

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    -30d sweep across index=archimedes OR index=defenseclaw_local
    on CVE-2026-45585 / 45586 / 50507 / 49160 / 45657 / 47291 /
    44815 / 2020-17103 + Nightmare-Eclipse + Chaotic Eclipse +
    YellowKey + GreenPlasma + MiniPlasma + bitskrieg + RoguePlanet
    superset (combined with the broader morning-brief query).
    25 events returned, all sourcetype `archimedes:operation`
    self-instrumentation. 0 substantive first-party network /
    auth / EDR telemetry hits. Per Hard Rule 8: silence is not
    disconfirming.

single_source_veto_applied: true
single_source_veto_detail: >
  Applied on the GreenPlasma + MiniPlasma "actively exploited
  in attacks" ITW claim layer (BleepingComputer single-source
  on this specific framing; THN reframes as "publicly disclosed";
  Krebs not explicit on ITW for these specific CVEs). Applied
  on the Nightmare-Eclipse "former Microsoft employee" self-
  claim (Krebs single-source; Microsoft has not confirmed).
  Applied on the Nightmare-Eclipse "July 14 more zero-days"
  predictive claim (Krebs single-source quoting researcher
  pseudonym). Applied on Rapid7 Barnett "360 browser vulns
  10x normal" observation (Krebs single-source quoting Rapid7
  analyst). NOT applied on procedural facts (CVE IDs, CVSS,
  patch volume, patched-at-disclosure, researcher-pseudonym
  attribution) at three-source B-grade convergence.

wep_ceiling: likely
wep_layered:
  june_2026_patch_tuesday_patched_206_flaws_with_three_publicly_disclosed_zero_days: very_likely  # Three-source procedural facts convergence
  yellowkey_cve_2026_45585_bitlocker_winre_bypass_patched_cvss_6_8: very_likely
  greenplasma_cve_2026_45586_ctfmon_lpe_patched_cvss_7_8: very_likely
  miniplasma_cve_2020_17103_cloud_files_mini_filter_driver_lpe_re_patched_for_incomplete_prior_fix: very_likely
  bitskrieg_cve_2026_50507_bitlocker_eop_patched_cvss_6_8: very_likely
  http2_bomb_cve_2026_49160_iis_variant_patched_cvss_7_5_carry_lineage: very_likely
  three_critical_non_zero_day_rces_cve_2026_45657_47291_44815_cvss_9_8_patched_no_itw_at_disclosure: likely  # Two-source partial corroboration with no ITW; single-source-veto-adjacent on critical-class chain
  greenplasma_actively_exploited_in_attacks_itw: likely  # SINGLE-SOURCE VETOED — BC single-source on ITW framing
  miniplasma_actively_exploited_itw: likely  # SINGLE-SOURCE VETOED — same posture as GreenPlasma
  nightmare_eclipse_chaotic_eclipse_researcher_pseudonym_attribution_to_the_trio_plus_bitskrieg: very_likely  # Three-source procedural facts on credit
  nightmare_eclipse_former_microsoft_employee_self_claim: roughly_even_chance  # Krebs single-source; Microsoft has not confirmed
  nightmare_eclipse_july_14_more_zero_days_predictive: roughly_even_chance  # Krebs single-source quoting researcher pseudonym; predictive
  zd_001_bluehammer_state_transition_resolved_by_june_patch_tuesday: roughly_even_chance  # Pending vuln-tracker direct MSRC retrieval; cannot grade at this hour
  zd_002_redsun_state_transition_resolved_by_june_patch_tuesday: roughly_even_chance  # Same posture
  zd_003_undefend_state_transition_resolved_by_june_patch_tuesday: roughly_even_chance  # Same posture; RoguePlanet does NOT close UnDefend

inclusion:
  eligible_for:
    - daily_brief_action       # B2 meets action floor; patched-at-disclosure with three-source procedural facts convergence; defender-priority patch-urgency framing
    - daily_brief_monitoring
    - weekly_synthesis
  not_eligible_for:
    - flash                    # Not FLASH — CVSS sub-9 on the trio; single-source-vetoed on ITW; no tracked actor; no A&D-prime victim; outside FLASH evidence floor
    - actor_profile_update     # No tracked-actor attribution; Nightmare-Eclipse is researcher pseudonym not in roster

# Cluster metadata
cluster:
  topic: >
    Microsoft June 2026 Patch Tuesday — 206 flaws patched
    including three publicly-disclosed zero-days attributed to
    Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym:
    YellowKey (CVE-2026-45585, BitLocker bypass via WinRE,
    CVSS 6.8), GreenPlasma (CVE-2026-45586, LPE in CTFMON,
    CVSS 7.8), and MiniPlasma (CVE-2020-17103, LPE in Cloud
    Files Mini Filter Driver, re-patched for incomplete prior
    fix). Plus bitskrieg-family BitLocker EoP (CVE-2026-50507,
    CVSS 6.8) and HTTP/2 Bomb IIS variant (CVE-2026-49160,
    CVSS 7.5, OpenAI Codex reporter per Krebs — carries lineage
    to finding-2026-06-03-0003 multi-server HTTP/2 Bomb cluster).
    Three critical-class non-zero-day RCEs in same Patch
    Tuesday (CVE-2026-45657 kernel UAF, CVE-2026-47291 HTTP.sys
    integer overflow, CVE-2026-44815 DHCP Client stack buffer
    overflow, CVSS 9.8 each, no ITW reported). All patched at
    disclosure. BleepingComputer single-source on GreenPlasma +
    MiniPlasma "actively exploited" ITW framing — single-source
    veto applies on the ITW layer. Tracked vuln-index state
    transitions for ZD-001 BlueHammer / ZD-002 RedSun / ZD-003
    UnDefend pending vuln-tracker direct MSRC advisory
    retrieval and CVE-to-family mapping.
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-10-am-001-bleepingcomputer-thn-krebs-june-patch-tuesday-yellowkey-greenplasma-miniplasma-zero-days-itw
  attribution_claims:
    - claimed_actor: null
      claim_text: >
        Nightmare-Eclipse / Chaotic Eclipse is a security
        researcher pseudonym (NOT a tracked threat actor).
        All three sources (BleepingComputer, The Hacker News,
        Krebs) credit the researcher pseudonym for the
        publicly-disclosed YellowKey + GreenPlasma + MiniPlasma
        trio. Researcher self-claims former Microsoft employee
        status per Krebs (Microsoft has not confirmed).
        Researcher signals "more zero-days July 14, 2026" per
        Krebs.
      claimed_by_sources:
        - bleepingcomputer
        - thehackernews
        - krebs
      requires_analyst_review: false
      hard_rule_2_status: PRESERVED — researcher pseudonym is NOT threat-actor attribution; Archimedes does not roster-tier the researcher; coverage stays in vuln-tracker / researcher-series tracking layer

related_vulnerabilities:
  - CVE-2026-45585   # YellowKey BitLocker WinRE bypass
  - CVE-2026-45586   # GreenPlasma CTFMON LPE
  - CVE-2020-17103   # MiniPlasma Cloud Files Mini Filter Driver LPE re-patch
  - CVE-2026-50507   # bitskrieg-family BitLocker EoP
  - CVE-2026-49160   # HTTP/2 Bomb IIS variant
  - CVE-2026-45657   # Windows Kernel UAF RCE CVSS 9.8
  - CVE-2026-47291   # Windows HTTP.sys integer overflow RCE CVSS 9.8
  - CVE-2026-44815   # Windows DHCP Client stack buffer overflow RCE CVSS 9.8
  - CVE-2026-49975   # HTTP/2 Bomb multi-server cluster (carry-context from finding-2026-06-03-0003)
related_actors: []
related_campaigns:
  - nightmare_eclipse_researcher_series_continuing_coverage

update_on: null

# Downstream handoff flags
analyst_review_required: false
analyst_review_rationale: >
  WEP ceiling at "likely" overall; "very_likely" on procedural
  facts but those are multi-source convergence on patched-at-
  disclosure framing. No actor attribution. No A&D-prime named
  victim. No SAT-ACH / SAT-KAC trigger conditions met.
  Vuln-tracker handoff is the load-bearing downstream queue
  for this cluster (CVE scaffolding + ZD-001/002/003 state
  transition verification).

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling "likely" does not meet red-team invocation floor
  ("very likely" or higher) on substantive predictive or
  attributive claims. Procedural facts at "very_likely" are
  vendor-on-own-product canonical class (Microsoft Patch
  Tuesday CVE assignments + patch availability) which is not
  red-team invocation class. Researcher-pseudonym credit
  preserved without challenge per Hard Rule 2.

red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-10-morning]
retracted: false
retraction_brief_id: null

# Defensive / IOC handoff flags
ioc_handoff:
  defender_relevant_iocs:
    - "CVE-2026-45585 YellowKey — BitLocker bypass via Windows Recovery Environment (Windows 11, Server 2022/2025) CVSS 6.8"
    - "CVE-2026-45586 GreenPlasma — LPE in Collaborative Translation Framework (CTFMON) CVSS 7.8 — ITW per BC single-source"
    - "CVE-2020-17103 MiniPlasma — LPE in Cloud Files Mini Filter Driver re-patched for incomplete prior fix — ITW per BC single-source"
    - "CVE-2026-50507 bitskrieg-family BitLocker EoP CVSS 6.8 — public PoC"
    - "CVE-2026-49160 HTTP/2 Bomb IIS variant CVSS 7.5 — public PoC on GitHub per THN; OpenAI Codex reporter per Krebs"
    - "CVE-2026-45657 / 47291 / 44815 — three critical-class RCEs at CVSS 9.8 each (kernel UAF; HTTP.sys integer overflow; DHCP Client stack buffer overflow) — patched at disclosure, no ITW reported"
  iocs_indirect_action: >
    Defender action framing for A&D-DIB Windows estates:
    (a) Apply June 2026 Patch Tuesday rollup immediately —
    patch coverage spans 206 CVEs including all eight CVEs
    surfaced above;
    (b) BitLocker estate (YellowKey + bitskrieg): physical-
    access threat model; consider WinRE access controls and
    BitLocker policy hardening review for high-value-asset
    laptop fleets;
    (c) CTFMON LPE (GreenPlasma) + Cloud Files Mini Filter
    Driver LPE (MiniPlasma): LPE class — EDR detection
    posture for SYSTEM-shell elevation patterns from non-
    SYSTEM contexts on fully-patched-pre-June hosts;
    (d) HTTP/2 Bomb IIS variant: re-confirm patch baseline
    on internet-facing IIS instances; cross-reference
    finding-2026-06-03-0003 for the multi-server HTTP/2
    Bomb cluster (NGINX + Apache + Envoy + Cloudflare
    Pingora);
    (e) Three critical-class 9.8 RCEs (kernel UAF + HTTP.sys
    integer overflow + DHCP Client stack buffer overflow):
    patch immediately on internet-facing or otherwise-exposed
    Windows hosts; no ITW reported at disclosure but high-
    severity CVSS scoring justifies action-tier urgency.
    (f) Monitor for July 14 2026 Patch Tuesday — Nightmare-
    Eclipse researcher series signaled "more zero-days" per
    Krebs; defender-prudent to anticipate next cycle.

monitor_for_next_cycle:
  - MSRC blog post or Tier-1 IR firm telemetry (Mandiant / Unit 42 / Volexity / MSTIC) on the Nightmare-Eclipse trio — would lift cluster to B1 or A2 layered
  - Independent corroboration of GreenPlasma + MiniPlasma ITW exploitation (currently BC single-source) — would lift ITW layer from "likely" to "very_likely"
  - KEV listing on any of the eight CVEs surfaced
  - July 14 2026 Patch Tuesday — Nightmare-Eclipse signaled "more zero-days"
  - Microsoft public statement on Nightmare-Eclipse former-employee self-claim (Krebs reports Microsoft has not responded)
  - Vuln-tracker CVE-to-family mapping for ZD-001 BlueHammer / ZD-002 RedSun / ZD-003 UnDefend state transition resolution

vuln_tracker_handoff:
  scaffold_candidate: true
  scaffold_note: >
    Eight CVEs warrant vuln-tracker action:
    (1) Scaffold new vuln-dossiers (or extend existing) for:
        CVE-2026-45585 YellowKey, CVE-2026-45586 GreenPlasma,
        CVE-2020-17103 MiniPlasma (re-patch entry), CVE-2026-
        50507 bitskrieg BitLocker EoP, CVE-2026-49160 HTTP/2
        Bomb IIS variant, CVE-2026-45657 kernel UAF, CVE-2026-
        47291 HTTP.sys integer overflow, CVE-2026-44815 DHCP
        Client stack buffer overflow.
    (2) State-transition verification REQUIRED for ZD-001
        BlueHammer / ZD-002 RedSun / ZD-003 UnDefend against
        June Patch Tuesday MSRC advisory map. Vuln-tracker
        must directly retrieve MSRC and cross-reference CVE
        assignments to family identifiers.
    (3) Consider scaffolding ZD-005 series for the Nightmare-
        Eclipse researcher cluster (RoguePlanet + the trio +
        prior bitskrieg / BlueHammer / RedSun / UnDefend
        chain).
    (4) HTTP/2 Bomb cluster (CVE-2026-49160) cross-references
        finding-2026-06-03-0003 HTTP/2 Bomb multi-server
        (NGINX + Apache + IIS + Envoy + Cloudflare Pingora
        CVE-2026-49975); confirm whether 49160 is a sibling
        or extension of the cluster.

librarian_handoff:
  source_grade_revision_proposed: null

briefer_handoff:
  brief_inclusion_recommendation: action_tier
  brief_substance: >
    Morning brief CVE Watch / Action Items section. Headline
    framing: "Microsoft June 2026 Patch Tuesday — 206 flaws
    patched including three publicly-disclosed Nightmare-
    Eclipse zero-days (YellowKey BitLocker, GreenPlasma CTFMON
    LPE, MiniPlasma Cloud Files Mini Filter Driver LPE);
    bitskrieg BitLocker EoP companion patched; HTTP/2 Bomb
    IIS variant patched; three critical 9.8 RCEs patched
    no-ITW." Single-source veto framing on GreenPlasma +
    MiniPlasma "actively exploited" claim — defender response
    is patch immediately regardless of ITW status. Continuing
    coverage note: Nightmare-Eclipse researcher series now
    eight disclosures deep; researcher signals July 14 next
    Patch Tuesday "more zero-days." Vuln-tracker state-
    transition verification queued for ZD-001/002/003.
    Cross-reference HTTP/2 Bomb cluster (finding-2026-06-03-
    0003) and Microsoft disclosure-policy context (finding-
    2026-06-03-0002).
---

# Microsoft June 2026 Patch Tuesday — 206 Flaws Patched Including Three Publicly-Disclosed Nightmare-Eclipse Zero-Days (YellowKey BitLocker, GreenPlasma CTFMON LPE, MiniPlasma Cloud Files Mini Filter Driver LPE) Plus bitskrieg BitLocker EoP and Three Critical 9.8 RCEs

## Summary

Microsoft's June 2026 Patch Tuesday (2026-06-10) patched **206 vulnerabilities**, the largest single-month volume in the corpus to date, per The Hacker News (Krebs reports "nearly 200"). Three of the patched flaws were publicly disclosed prior to release as part of the ongoing Nightmare-Eclipse / Chaotic Eclipse researcher series: **YellowKey** (CVE-2026-45585, BitLocker bypass via Windows Recovery Environment, CVSS 6.8), **GreenPlasma** (CVE-2026-45586, local privilege escalation in Collaborative Translation Framework, CVSS 7.8), and **MiniPlasma** (CVE-2020-17103, local privilege escalation in Cloud Files Mini Filter Driver, re-patched for an incomplete prior fix). All three were patched at disclosure.

BleepingComputer is the only one of the three primary sources that frames GreenPlasma and MiniPlasma as "actively exploited in attacks" — The Hacker News reframes as "publicly disclosed" without ITW labeling, and Krebs does not label them as ITW. Per the single-source veto, the ITW claim layer is capped at WEP "likely"; the patched-at-disclosure procedural-facts layer is at "very likely" with three-source B-grade convergence.

The same Patch Tuesday also patched **CVE-2026-50507** (bitskrieg-family BitLocker EoP, CVSS 6.8 — Krebs notes Microsoft did not credit a specific researcher in the acknowledgement section), **CVE-2026-49160** (HTTP/2 Bomb IIS variant, CVSS 7.5, OpenAI Codex reporter per Krebs — carries lineage to the finding-2026-06-03-0003 multi-server HTTP/2 Bomb cluster), and three critical-class non-zero-day RCEs at CVSS 9.8 each: **CVE-2026-45657** (Windows Kernel use-after-free), **CVE-2026-47291** (Windows HTTP.sys integer overflow), and **CVE-2026-44815** (Windows DHCP Client stack buffer overflow). No ITW reported on the three critical RCEs.

The Nightmare-Eclipse researcher cluster is now eight disclosures deep across the broader corpus chain (Bitskrieg / BlueHammer / RedSun / UnDefend / RoguePlanet / YellowKey / GreenPlasma / MiniPlasma). Per Hard Rule 2, Nightmare-Eclipse is a researcher pseudonym, not a tracked threat actor; Archimedes does not roster-tier the researcher. Researcher signaled "more zero-days July 14, 2026" per Krebs — defender-prudent to anticipate next Patch Tuesday cycle.

Vuln-tracker state-transition verification is queued for **ZD-001 BlueHammer**, **ZD-002 RedSun**, and **ZD-003 UnDefend**: vuln-tracker must directly retrieve MSRC advisories and map CVE assignments to family identifiers to determine resolution status. RoguePlanet (disclosed 2026-06-10 post-Patch-Tuesday) is a separate Defender issue and does NOT close UnDefend.

A&D defensive priority: apply the June 2026 Patch Tuesday rollup immediately across Windows estates. Patch coverage spans 206 CVEs including all eight surfaced above. BitLocker physical-access threat model applies for YellowKey + bitskrieg; LPE class for GreenPlasma + MiniPlasma; HTTP/2 Bomb IIS variant aligns with the prior multi-server cluster. No A&D-prime named as victim; structural Windows-deployment exposure only.

## Sources

### BleepingComputer (bleepingcomputer, digraph: B2 publisher-independent primary)

- URL: https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/
- Published: 2026-06-10T09:57:33 UTC
- Source grade: B (ratified)
- Key claim: BleepingComputer is the sole-originating source on the "actively exploited in attacks" framing for GreenPlasma and MiniPlasma. The trio (YellowKey + GreenPlasma + MiniPlasma) plus bitskrieg lineage attribution to Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym is consistent with THN and Krebs.
- Verbatim quote (≤15 words, one per source, Hard Rule 6): *"actively exploited in attacks"* (4 words, applied to GreenPlasma and MiniPlasma framing).

### The Hacker News (thehackernews, digraph: B2 publisher-independent primary)

- URL: https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html
- Published: 2026-06-10T09:38:13 UTC
- Source grade: B (provisional, since 2026-05-14)
- Key claim: THN frames the patch volume as 206 flaws (39 Critical, 167 Important; 63 EoP, 56 RCE, 30 info disclosure, 27 spoofing, 20 security feature bypass). THN frames the Nightmare-Eclipse trio as "publicly disclosed" — NOT as "actively exploited." THN explicitly lists CVE-2026-45657 / 47291 / 44815 as the three critical 9.8 RCE chain and CVE-2026-50507 with bitskrieg lineage.
- Verbatim quote (≤15 words, one per source): *"Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs"* (12 words, headline-class).

### Krebs on Security (krebs, digraph: B2 publisher-independent primary)

- URL: https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/
- Published: 2026-06-09T22:07:28 UTC
- Source grade: B (ratified)
- Key claim: Krebs reports "nearly 200" CVEs patched. Single-source quotes Rapid7's Adam Barnett observing an additional 360 browser vulnerabilities patched this month (10x normal). Single-source on Nightmare-Eclipse's self-claim of former Microsoft employee status (Microsoft has not confirmed per Krebs). Single-source on researcher signal of "more zero-days July 14" planned drop. Krebs places the bitskrieg lineage explicitly on CVE-2026-50507 and notes Microsoft did not credit a specific researcher in the acknowledgement section.
- Verbatim quote (≤15 words, one per source): *"elevation of privilege bug in BitLocker"* (7 words, on bitskrieg CVE-2026-50507).

Independence test: three publisher-independent organizations, different bylines, none cites another as origin in the retrieved text. Different evidence bases on retrieval (each independently retrieved MSRC advisories; Krebs additionally quotes Rapid7 analyst commentary). PASSES on procedural facts (patch volume, CVE identifiers, CVSS scores, patched-at-disclosure framing, researcher-pseudonym credit). FAILS on the GreenPlasma + MiniPlasma "actively exploited" ITW claim layer (BC single-source).

## Technical detail

### Three publicly-disclosed zero-days (patched at disclosure)

| CVE | Name | Class | CVSS | ITW status |
|---|---|---|---|---|
| CVE-2026-45585 | YellowKey | BitLocker bypass via Windows Recovery Environment (WinRE) | 6.8 | PoC public; no ITW per BC/THN/Krebs |
| CVE-2026-45586 | GreenPlasma | LPE in Collaborative Translation Framework (CTFMON) | 7.8 | "Actively exploited" per BC (single-source); reframed by THN as "publicly disclosed" |
| CVE-2020-17103 | MiniPlasma | LPE in Cloud Files Mini Filter Driver — re-patched for incomplete prior fix | (pending NVD CVSS recomputation for re-patch) | "Actively exploited" per BC (single-source); THN frames as PoC public + incomplete prior fix |

All three attributed to **Nightmare-Eclipse / Chaotic Eclipse** researcher pseudonym across the three sources.

### Companion zero-day class — bitskrieg BitLocker EoP

**CVE-2026-50507** — BitLocker elevation of privilege, CVSS 6.8. Krebs places this as a sub-component of the BitLocker family at this Patch Tuesday; THN explicitly notes "linked to the 'bitskrieg' exploit enabling full access to encrypted data." Microsoft per Krebs did not credit a specific researcher in the acknowledgement section. Carry-context to prior corpus surfaces (finding-2026-06-02 PM-006, finding-2026-06-03 PM-005).

### HTTP/2 Bomb IIS variant

**CVE-2026-49160** — HTTP.sys denial of service, CVSS 7.5. Public PoC on GitHub per THN. Krebs notes the bug was reported by OpenAI's Codex (automated discovery, not actor attribution). Cross-references finding-2026-06-03-0003 (HTTP/2 Bomb multi-server cluster covering NGINX + Apache + Envoy + Cloudflare Pingora CVE-2026-49975); CVE-2026-49160 is the Microsoft-specific IIS fix in the same architectural class.

### Three critical non-zero-day RCEs (CVSS 9.8 each)

- **CVE-2026-45657** — Windows Kernel use-after-free RCE
- **CVE-2026-47291** — Windows HTTP.sys integer overflow RCE
- **CVE-2026-44815** — Windows DHCP Client stack buffer overflow RCE

No ITW reported at disclosure for any of the three. All patched at release. THN is the originating source for this explicit list; Krebs covers via patch-volume framing.

### Nightmare-Eclipse researcher series — continuing coverage

The researcher cluster is now eight disclosures deep: Bitskrieg / BlueHammer / RedSun / UnDefend / RoguePlanet / YellowKey / GreenPlasma / MiniPlasma. Per Krebs: the researcher claims former Microsoft employee status; Microsoft has not responded to questions about this self-claim per Krebs. The researcher signaled "more zero-days July 14, 2026" — defender-prudent to anticipate the next Patch Tuesday cycle. Recent Krebs noted Microsoft initially threatened legal action against the researcher; Microsoft later clarified it would only report to authorities if researchers break the law.

**Hard Rule 2 status:** PRESERVED. Nightmare-Eclipse / Chaotic Eclipse is a researcher pseudonym, NOT a tracked threat actor. Archimedes does not roster-tier the researcher. Coverage stays in vuln-tracker / researcher-series tracking layer.

## IOCs

```yaml
iocs:
  cves:
    - id: CVE-2026-45585
      name: YellowKey
      class: BitLocker bypass via Windows Recovery Environment (WinRE)
      cvss: 6.8
      severity: Important
      exploitation_status: poc_publicly_disclosed_no_itw_per_three_source_consensus
      patch_status: patched_2026_06_10_patch_tuesday
      attribution: Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym
      platform: Windows 11, Windows Server 2022, Windows Server 2025
    - id: CVE-2026-45586
      name: GreenPlasma
      class: Local privilege escalation in Collaborative Translation Framework (CTFMON)
      cvss: 7.8
      severity: Important
      exploitation_status: poc_public; bleepingcomputer_single_source_on_itw_claim_single_source_vetoed
      patch_status: patched_2026_06_10_patch_tuesday
      attribution: Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym
      platform: Windows
    - id: CVE-2020-17103
      name: MiniPlasma
      class: LPE in Cloud Files Mini Filter Driver — re-patched for incomplete prior fix
      cvss: pending
      severity: pending
      exploitation_status: poc_public; bleepingcomputer_single_source_on_itw_claim_single_source_vetoed
      patch_status: patched_2026_06_10_patch_tuesday_incomplete_prior_fix_re_patched
      attribution: Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym
    - id: CVE-2026-50507
      name: bitskrieg-family BitLocker EoP
      class: BitLocker elevation of privilege
      cvss: 6.8
      severity: Important
      exploitation_status: poc_public
      patch_status: patched_2026_06_10_patch_tuesday
      attribution: per THN "linked to the bitskrieg exploit"; per Krebs no researcher credit in advisory
    - id: CVE-2026-49160
      name: HTTP/2 Bomb (Microsoft IIS variant)
      class: HTTP.sys denial of service
      cvss: 7.5
      severity: Important
      exploitation_status: poc_public_github
      patch_status: patched_2026_06_10_patch_tuesday
      attribution: OpenAI Codex reporter per Krebs (automated discovery)
      cross_corpus_lineage: HTTP/2 Bomb multi-server cluster (CVE-2026-49975 NGINX/Apache/Envoy/Pingora per finding-2026-06-03-0003)
    - id: CVE-2026-45657
      class: Windows Kernel use-after-free RCE
      cvss: 9.8
      severity: Critical
      exploitation_status: no_itw_at_disclosure
      patch_status: patched_2026_06_10_patch_tuesday
    - id: CVE-2026-47291
      class: Windows HTTP.sys integer overflow RCE
      cvss: 9.8
      severity: Critical
      exploitation_status: no_itw_at_disclosure
      patch_status: patched_2026_06_10_patch_tuesday
    - id: CVE-2026-44815
      class: Windows DHCP Client stack buffer overflow RCE
      cvss: 9.8
      severity: Critical
      exploitation_status: no_itw_at_disclosure
      patch_status: patched_2026_06_10_patch_tuesday
  hashes: []
  domains: []
  ipv4: []
  urls: []
  attribution_claims:
    - claim_text: "Nightmare-Eclipse / Chaotic Eclipse — security researcher pseudonym; claims former Microsoft employee status per Krebs; Microsoft has not confirmed"
      target: CVE-2026-45585, CVE-2026-45586, CVE-2020-17103
      source: bleepingcomputer, thehackernews, krebs
      attribution_type: researcher_pseudonym_NOT_tracked_actor
      hard_rule_2_compliant: true
```

## Relationship to existing findings

- **finding-2026-06-03-0002** (BleepingComputer / VS Code / GitHub OAuth token theft / Askar PoC full disclosure / Microsoft disclosure policy current) — same Microsoft disclosure-policy thread (Nightmare-Eclipse legal-action initial-posture mention; relationship to researcher-disclosure framing).
- **finding-2026-06-03-0003** (SecurityWeek / THN / HTTP/2 Bomb CVE-2026-49975 NGINX/Apache/IIS/Envoy/Pingora multi-server) — CVE-2026-49160 is the Microsoft-specific IIS fix in the same HTTP/2 Bomb architectural class. Vuln-tracker should confirm whether 49160 is a sibling CVE under the same cluster or a distinct sub-vulnerability.
- **flash-2026-06-10-0600 RoguePlanet (raw-2026-06-10-flash-0600-000)** — RoguePlanet is the Defender zero-day Nightmare-Eclipse published immediately after this Patch Tuesday; PoC-only, no ITW per BC/THN. NOT graded as a separate finding in this morning brief (deferred to UPDATE block per the 06:00 FLASH-rejection disposition).
- **Prior Nightmare-Eclipse corpus chain:** finding-2026-06-02 PM-006 (Bitskrieg first surface), finding-2026-06-03 PM-005 (TheRegister Microsoft disclosure-policy on Askar VS Code + Nightmare-Eclipse Bitskrieg explicit linkage).

## Open questions for analyst

- Is the BleepingComputer single-source ITW framing on GreenPlasma + MiniPlasma corroborated by any A-grade IR firm telemetry post-disclosure? Monitor MSTIC, Mandiant, Volexity, Unit 42 for 24-48 hour confirmation; if confirmed, ITW layer lifts from "likely" to "very_likely."
- Does the Nightmare-Eclipse former-Microsoft-employee self-claim materially change the operator's threat model for the researcher series? (Krebs notes Microsoft has not confirmed. Analyst SAT-ACH not invoked at this hour given research-pseudonym-not-threat-actor disposition; revisit if Microsoft confirms or denies in the next cycle.)
- Vuln-tracker state-transition verification for ZD-001 BlueHammer / ZD-002 RedSun / ZD-003 UnDefend: cannot grade resolution at this hour without direct MSRC retrieval and CVE-to-family mapping. Vuln-tracker queue priority.
