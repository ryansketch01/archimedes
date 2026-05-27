---
finding_id: finding-2026-05-27-0004-securityweek-lacmta-iran-black-shadow-mois-gambit-israel-cyber-directorate-relay-investigation-update
created_at: 2026-05-27T08:20:00-04:00
graded_by: grader
grading_run_id: morning-20260527-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: C3
digraph_layered:
  securityweek_b_grade_relay_layer: B2
  gambit_security_black_shadow_cluster_naming: C3
  israel_national_cyber_directorate_mois_service_attribution: C3
  lacmta_victim_named: A1                              # publicly disclosed, uncontested
  multi_victim_regional_campaign_us_israel_saudi_turkey: C3
  no_ad_prime_named_victim: A1
  no_specific_iocs_published_in_relay: A1
  no_cve_referenced: A1
  no_cross_walk_to_tracked_iranian_actors: A1          # Hard Rule 2 compliance
  cluster_anchor: C3

digraph_anchor: >
  Cluster digraph C3 anchored on SecurityWeek (Eduard Kovacs,
  2026-05-27 05:33 EDT) media relay of the open Archimedes
  investigation `inv-2026-05-26-001`. The investigation's WEP ceiling
  is currently C3 single-source-veto (Gambit Security as originating
  IR firm, not yet cross-corroborated by A/B-grade IR firm). This
  finding's role is to record the in-window relay surface and update
  the investigation status; it does NOT elevate the underlying
  attribution because:
    (a) SecurityWeek is B-grade relay - relays do not corroborate
        their underlying source per INTEL-GRADING.md independence test
    (b) Gambit Security remains the originating IR firm; no second
        A/B-grade IR firm (Mandiant, Microsoft MSTIC, CrowdStrike,
        Recorded Future, Volexity, Unit 42, Cisco Talos) has published
        parallel attribution
    (c) Israel National Cyber Directorate is a government-tier
        attribution source but its MOIS service-level claim does NOT
        identify a specific actor cluster within MOIS that would
        permit roster cross-walk
    (d) Hard Rule 2 strictly prohibits cross-walking Black Shadow to
        tracked MOIS actors (MuddyWater #022, Handala Hack #014)
        despite the service-level match
  Investigation lock `inv-2026-05-26-001` carries forward through
  2026-06-09 T+14. This finding does not close the investigation.

source_reliability:
  grade: B
  source_name: "SecurityWeek (Eduard Kovacs) relay layer on inv-2026-05-26-001"
  source_yaml_id: securityweek
  grade_rationale: >
    SecurityWeek pre-assigned B per source-grades.yaml. In-window
    relay at 2026-05-27 05:33 EDT. Cluster grade follows SecurityWeek
    as proximate in-corpus source; underlying attribution chain
    (Gambit Security → Israel National Cyber Directorate) is corpus-
    tracked via investigation inv-2026-05-26-001.
  provisional: false
  attribution_chain:
    - tier_1_originating_ir_firm: Gambit Security
      gambit_security_yaml_id: not_in_source_grades_yaml
      gambit_provisional_grade: F   # cheatsheet: unknown research vendor with no prior corpus citation
      contribution: "Black Shadow cluster naming + configuration-fingerprint-based infrastructure linkage to previously-identified Iranian campaign infrastructure"
      cross_corroboration_status: "no second A/B-grade IR firm publishing parallel attribution as of this sweep"
    - tier_2_government_attribution: Israel National Cyber Directorate
      grade: B
      contribution: "MOIS (Iran Ministry of Intelligence and Security) service-level framing - service attribution, not specific actor cluster attribution"
    - tier_3_relay: SecurityWeek (Eduard Kovacs)
      grade: B
      contribution: "media relay; no new evidence layer; surfaces Black Shadow cluster naming + MOIS framing for English-language A&D-relevant audience"

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_partially_consistent_with_known_ttps_but_some_elements_novel
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable
  grade_2_test:
    - probably_true_consistent_with_established_ttps_partial: "MOIS Iranian state-sponsored operations against US/Israel/Saudi/Turkey civilian targets is the established 2026 Iranian operational pattern - consistent with Iran Cyber Watch standing observation. Hacktivist-front + state-infrastructure pattern is the FDD-noted current wave."
    - probably_true_no_contradicting_evidence_from_ab_grade_sources: "No contradicting source observed; FBI / CISA / DHS / Mandiant / Microsoft / CrowdStrike / Unit 42 silent on Black Shadow attribution as of this sweep - silence is not corroboration but is not contradiction either"
    - probably_true_technical_claims_internally_coherent_partial: "Black Shadow as MOIS cluster is plausible; infrastructure-linkage methodology is standard IR-firm tradecraft. No specific IOCs published in the relay layer to independently evaluate."
    - grade_2_blocked_by: "Single originating IR firm (Gambit Security) without graded track record in Archimedes corpus AND without cross-corroboration from A/B-grade peer IR firm. Per INTEL-GRADING single-source veto + provisional-F-or-unknown originating-source caveat. Cluster anchor holds at credibility 3 (Possibly True) pending: (a) Mandiant or Microsoft MSTIC or CrowdStrike or Recorded Future independent publication of Black Shadow attribution, OR (b) CISA or FBI public attribution of LACMTA incident to Iranian state-sponsored actor."
  rationale: >
    The attribution chain (LACMTA breach → Iranian campaign infrastructure
    → Black Shadow cluster → MOIS service) is plausibly constructed
    given Iran Cyber Watch corpus pattern. The Israel National Cyber
    Directorate's MOIS framing adds government-tier corroboration to
    Gambit Security's IR-firm-tier claim. However, the cluster is
    held at credibility 3 because: (a) Gambit Security has no
    Archimedes-corpus track record (provisional-F per cheatsheet),
    (b) no second A/B-grade IR firm has published parallel
    attribution, (c) no specific IOCs are published in the relay
    layer for independent verification. Per Hard Rule 2, Archimedes
    does NOT cross-walk Black Shadow to MuddyWater (#022) or Handala
    Hack (#014) despite the MOIS service-level match.

corroboration:
  independent_sources:
    - gambit_security (provisional F - first Archimedes-corpus citation; no track record)
    - israel_national_cyber_directorate (B-grade government attribution source - service-level claim, not specific cluster claim)
  independent: partial
  test_status: >
    Gambit Security and Israel National Cyber Directorate are nominally
    independent organizations (private IR firm vs national cyber agency)
    but per public reporting the Israel National Cyber Directorate
    publication cites Gambit Security as its attribution source - making
    the chain effectively single-evidence-basis. SecurityWeek is a relay
    of both - not independent corroboration. Cluster has ONE effective
    evidence basis on the Black Shadow / MOIS / LACMTA attribution.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    Splunk query against defenseclaw_local + archimedes over -24h
    covering "LA Metro", "LACMTA", "Black Shadow", "Iran", "MOIS",
    "Ababil of Minab", "Charter" (related actor cluster check),
    "Iranian state-sponsored". Zero events. Hard Rule 8: silence not
    disconfirming. LACMTA is municipal transit, not A&D-prime - no
    expected defenseclaw_local visibility on LACMTA-specific
    infrastructure. The Black Shadow cluster naming has no published
    IOCs in this relay layer to query for.

single_source_veto_applied: true
single_source_veto_rationale: >
  Per INTEL-GRADING.md single-source veto, the attribution chain
  effectively rests on Gambit Security's research with Israel National
  Cyber Directorate as a government endorsement of Gambit's
  attribution. The chain is single-evidence-basis on the Black Shadow
  cluster identification specifically. Cluster WEP ceiling held at
  "possibly true / roughly even chance" pending A/B-grade IR-firm
  independent attribution.

wep_ceiling: roughly_even_chance
wep_layered:
  lacmta_breach_occurred_partial_access_per_lacmta_disclosure: very_likely  # LACMTA's own confirmation
  iranian_state_sponsored_actor_responsible_per_gambit_iran_cyber_dir: roughly_even_chance  # single-evidence-basis attribution
  black_shadow_is_the_specific_cluster: roughly_even_chance               # single-evidence-basis cluster naming
  mois_is_the_service_per_israel_national_cyber_directorate: roughly_even_chance  # government-tier endorsement but ultimately single chain
  multi_victim_regional_campaign_us_israel_saudi_turkey: roughly_even_chance
  no_ad_prime_named_victim_in_multi_victim_list: very_likely               # explicit absence
  splunk_first_party_silence_implies_no_ad_prime_lateral_movement_yet: roughly_even_chance  # caveat: archimedes/defenseclaw_local Splunk visibility scope is bounded

inclusion:
  eligible_for:
    - daily_brief_monitoring                # Iran Cyber Watch standing section update
    - iran_cyber_watch_standing_section
    - weekly_synthesis                       # pattern signal
    - investigation_update_inv_2026_05_26_001
  not_eligible_for:
    - flash                                  # already absorbed under investigation lock; Trigger 2 marginal-fail (Black Shadow not in _roster)
    - daily_brief_action                     # below B2 minimum; no defender-actionable IOCs
    - actor_profile_update                   # Black Shadow not in _roster; /new-actor scaffolding bar not yet met
  inclusion_rationale: >
    C3 cluster on SecurityWeek B-grade relay layer of open investigation
    inv-2026-05-26-001. Iran Cyber Watch standing section update tier.
    Update content: Black Shadow cluster naming + MOIS service framing
    added to the prior "previously identified Iranian campaign" framing.
    Per Hard Rule 2, no cross-walk to tracked Iranian actors despite
    MOIS match with MuddyWater (#022) and Handala Hack (#014).
    Investigation lock carry-forward through 2026-06-09 T+14 unchanged.

# Cluster metadata
cluster:
  topic: "LACMTA cyberattack attribution update - SecurityWeek (Eduard Kovacs 2026-05-27 05:33 EDT) B-grade relay of Gambit Security (originating IR firm; first Archimedes-corpus citation; provisional F) + Israel National Cyber Directorate (B-grade government attribution) chain - attribution: Black Shadow cluster + MOIS (Iran Ministry of Intelligence and Security) service - prior framing 'previously identified Iranian campaign infrastructure' (from Reuters etc.) now specified to Black Shadow cluster - multi-victim regional campaign touching US, Israel, Saudi Arabia, Turkey across media/education/insurance/restaurant/culture/digital-services/news sectors - NO A&D / aerospace / defense / DIB / CMMC / ITAR sector named - NO watchlist A&D prime named - per Hard Rule 2 NO cross-walk to tracked Iranian actors UNC1549 (#004) / Charming Kitten (#011) / Handala Hack (#014) / MuddyWater (#022) / APT34 (#023) despite MOIS service match - Black Shadow NOT in _roster.yaml - investigation inv-2026-05-26-001 carry-forward through 2026-06-09 T+14"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-27-am-005
  related_actors: []        # Hard Rule 2: no roster cross-walk despite MOIS match
  related_actors_hard_rule_2_caveat:
    - actor_id: "014"
      actor_name: "Handala Hack"
      service: MOIS
      cross_walk_status: "PROHIBITED per Hard Rule 2 - service-level match insufficient for cross-walk; no source makes the Black Shadow → Handala Hack connection"
    - actor_id: "022"
      actor_name: "MuddyWater"
      service: MOIS
      cross_walk_status: "PROHIBITED per Hard Rule 2 - service-level match insufficient for cross-walk; no source makes the Black Shadow → MuddyWater connection"
  related_vulnerabilities: []
  attribution_claims:
    - claim: "LACMTA breach attributed to Black Shadow cluster"
      claimed_by: Gambit Security
      claim_confidence_language: "configuration-fingerprint-based infrastructure linkage"
      novelty_to_corpus: true   # Black Shadow not previously named in Archimedes corpus
      requires_analyst_review: true
      hard_rule_2_status: "preserved; not upgraded; Black Shadow not added to _roster.yaml pending A/B-grade IR-firm corroboration"
    - claim: "Black Shadow cluster owned by MOIS"
      claimed_by: Israel National Cyber Directorate (via Gambit Security publication)
      claim_confidence_language: "MOIS attribution"
      novelty_to_corpus: true
      requires_analyst_review: true
      hard_rule_2_status: "preserved; not upgraded; service-level claim does NOT support cross-walk to tracked MOIS actors per Hard Rule 2"
  related_investigation:
    investigation_id: inv-2026-05-26-001
    investigation_file: threats/investigations/2026-05-26-lacmta-iran-attribution.md
    investigation_status: OPEN since 2026-05-26
    current_wep_ceiling: C3 single-source-veto
    carry_forward_through: 2026-06-09 T+14
    finding_role: "update / surface in Iran Cyber Watch standing section; do NOT close investigation"

# IOCs surfaced
iocs_surfaced: []   # No specific IOCs published in the SecurityWeek relay - infrastructure described at framework-level only

ttp_keywords:
  - name: Hacktivist-front + state-infrastructure pattern (FDD-noted current Iranian wave)
    framework_mapping: ATT&CK Enterprise - operational pattern rather than single technique
    context: "Iranian state-sponsored cyber operations frequently use hacktivist personas (Ababil of Minab, CyberAveng3rs, etc.) as front for state-tier infrastructure - per FDD 2026-05-20 policy brief framing of current Iranian US-civilian-infra wave"
  - name: Configuration-fingerprint-based infrastructure linkage (IR-firm tradecraft)
    framework_mapping: not_attck_specific
    context: "Gambit Security's methodology per public reporting - fingerprinting C2 / staging server configurations against known Iranian campaign infrastructure - standard IR-firm tradecraft but methodology not externally validated for Archimedes corpus purposes"

# Downstream handoff flags
analyst_review_required: true
analyst_review_topics:
  - "Investigation inv-2026-05-26-001 carry-forward decision: analyst evaluates whether Black Shadow naming + MOIS attribution from Israel National Cyber Directorate sufficiently corroborates Gambit Security's attribution to elevate the investigation's WEP ceiling above C3. Per INTEL-GRADING the elevation bar is at least one A/B-grade IR firm independent publication; Israel National Cyber Directorate is B-grade government attribution source which may count toward elevation IF the analyst judges its publication is built on Israel-side telemetry independent of Gambit Security rather than endorsement of Gambit's published research. This is a doctrine-edge call worthy of analyst review."
  - "/new-actor scaffolding decision for Black Shadow: bar is at least one A-grade IR-firm source making the Black Shadow attribution. Bar NOT yet met (Gambit Security is provisional-F first-citation; Israel National Cyber Directorate is B-grade government). Hold pending A/B-grade IR-firm corroboration. If Mandiant / Microsoft MSTIC / CrowdStrike / Recorded Future publishes parallel Black Shadow attribution within 14d window, re-evaluate."
  - "SAT-ACH candidate on the attribution chain: competing hypotheses on Black Shadow / MOIS attribution validity. (H1) Gambit Security's configuration-fingerprint methodology is sound and Black Shadow is a genuine MOIS cluster. (H2) Gambit Security mis-attributed; the LACMTA breach is non-state cyber-criminal opportunism. (H3) Black Shadow is a real cluster but its MOIS attribution by Israel National Cyber Directorate is downstream-endorsement of Gambit rather than independent telemetry. Load-bearing evidence: actual IOC publication by an A/B-grade IR firm with independent telemetry."

analysis_sections:
  sat_ach:
    ach_analysis:
      question: "Is the Gambit Security + Israel National Cyber Directorate attribution chain (LACMTA → Black Shadow → MOIS) supported by the cited evidence against alternative explanations?"
      analyzed_at: 2026-05-27T08:48:00-04:00
      analyzed_by: analyst
      red_team_review: null
      hypotheses:
        - id: H1
          statement: "Sourced hypothesis: Gambit Security's configuration-fingerprint-based attribution is sound; Black Shadow is a genuine MOIS cluster responsible for LACMTA and the broader multi-victim regional campaign; Israel National Cyber Directorate independently corroborates via Israel-side telemetry."
        - id: H2
          statement: "Sourced hypothesis variant: Black Shadow is a real Iranian-aligned cluster but Israel National Cyber Directorate's MOIS framing is downstream endorsement of Gambit Security rather than independent telemetry - the attribution chain is effectively single-evidence-basis dressed up as multi-source."
        - id: H3
          statement: "Null hypothesis: LACMTA breach is non-state cyber-criminal opportunism; Iran-themed branding (Ababil of Minab hacktivist Telegram) is criminal-larp / extortion theatrics; Gambit Security mis-attributed by latching onto Iranian-themed surface signals."
        - id: H4
          statement: "Surprise/false-flag hypothesis: A different state actor (e.g., FSB, GRU, or even an Iranian competitor to MOIS) is staging Iranian-themed operations to muddy attribution. Russian FSB historically uses pro-Iran hacktivist personas; the Black Shadow naming itself could be reused branding."
        - id: H5
          statement: "Composite hacktivist-as-cover hypothesis: Genuinely independent pro-Iran hacktivists (Ababil of Minab) conducted LACMTA opportunistically; Gambit Security retrofitted MOIS infrastructure linkage from earlier unrelated Iranian campaigns, creating false coherence."
      evidence:
        - id: E1
          description: "Gambit Security configuration-fingerprint-based infrastructure linkage to previously-identified Iranian campaign infrastructure"
          source: gambit-security-via-securityweek-2026-05-27
          digraph: C3
          weight: 1
        - id: E2
          description: "Israel National Cyber Directorate publication framing Black Shadow as MOIS cluster"
          source: israel-national-cyber-directorate-via-securityweek
          digraph: B3
          weight: 1
        - id: E3
          description: "Israel National Cyber Directorate publication cites Gambit Security as attribution source (per public reporting) - making the chain effectively single-evidence-basis"
          source: corpus-derived-from-investigation-inv-2026-05-26-001
          digraph: B2
          weight: 2
        - id: E4
          description: "Multi-victim regional campaign scope matches Iranian operational pattern (US/Israel/Saudi/Turkey civilian targets, media/education/insurance sectors) - consistent with FDD-noted 2026 wave"
          source: securityweek-relay-2026-05-27
          digraph: B2
          weight: 2
        - id: E5
          description: "Ababil of Minab pro-Iran hacktivist Telegram claim 2026-04-09 for LACMTA"
          source: ababilofminab-telegram-via-prior-investigation
          digraph: C3
          weight: 1
        - id: E6
          description: "LACMTA itself declined to validate volumetric claims or comment on Gambit findings (vendor silence)"
          source: lacmta-disclosure
          digraph: A2
          weight: 3
        - id: E7
          description: "No A/B-grade IR firm (Mandiant / MSTIC / CrowdStrike / Recorded Future / Volexity / Unit 42 / Cisco Talos) has published parallel Black Shadow attribution as of this sweep"
          source: corpus-silence-2026-05-27
          digraph: A1
          weight: 3
        - id: E8
          description: "No specific IOCs published in the SecurityWeek relay; infrastructure described at framework-level only"
          source: securityweek-relay-2026-05-27
          digraph: A1
          weight: 3
        - id: E9
          description: "Black Shadow is NOT a known alias for any tracked MOIS actor (MuddyWater #022, Handala Hack #014, APT34 #023); roster cross-walk explicitly prohibited"
          source: archimedes-roster-yaml
          digraph: A1
          weight: 3
        - id: E10
          description: "Gambit Security has no prior Archimedes-corpus citation; provisional-F per cheatsheet"
          source: archimedes-source-grades-yaml
          digraph: A1
          weight: 3
      matrix:
        E1: {H1: C, H2: C, H3: I, H4: C, H5: C}
        E2: {H1: C, H2: C, H3: I, H4: C, H5: N}
        E3: {H1: I, H2: C, H3: N, H4: N, H5: N}
        E4: {H1: C, H2: C, H3: N, H4: C, H5: C}
        E5: {H1: C, H2: C, H3: C, H4: C, H5: C}
        E6: {H1: N, H2: N, H3: N, H4: N, H5: N}
        E7: {H1: I, H2: I, H3: N, H4: N, H5: N}
        E8: {H1: I, H2: N, H3: N, H4: N, H5: N}
        E9: {H1: N, H2: N, H3: N, H4: C, H5: N}
        E10: {H1: I, H2: N, H3: N, H4: N, H5: N}
      inconsistency_counts:
        H1: 4
        H2: 1
        H3: 2
        H4: 0
        H5: 0
      diagnostic_evidence:
        - E3: "Diagnostic against H1 (independent corroboration) and toward H2 (downstream endorsement). The 'Israel NCD cites Gambit' chain detail is the most-load-bearing single observation in distinguishing genuine multi-source attribution from dressed-up single-source."
        - E7: "Diagnostic against H1 and H2 in the sense that absence of A/B-grade IR-firm parallel attribution at T+30 days from initial LACMTA disclosure is meaningful weak-evidence for H3/H4/H5 (alternative readings)."
        - E10: "Diagnostic against H1 - provisional-F originating IR firm without track record substantially weakens any single-source-based attribution claim."
      ranking:
        - rank: 1
          hypothesis_id: H4
          rationale: "Zero inconsistencies but requires unverified false-flag motive and capability - rank-1 by inconsistency count alone is misleading. Treated as a live hypothesis to monitor rather than supported."
          wep: unlikely
        - rank: 1
          hypothesis_id: H5
          rationale: "Zero inconsistencies, but composite hypothesis requires the retrofit-of-Iranian-infrastructure-from-earlier-campaigns sub-assumption that is itself unverified."
          wep: unlikely
        - rank: 3
          hypothesis_id: H2
          rationale: "One inconsistency (E7). The 'downstream endorsement of Gambit, not independent telemetry' reading IS most consistent with the evidence as presented and is the analyst's preferred reading for the investigation file. It does NOT contradict H1's directional claim (Black Shadow could still be MOIS) but reframes the corroboration layer."
          wep: roughly_even_chance
        - rank: 4
          hypothesis_id: H3
          rationale: "Two inconsistencies via E1, E2. Iranian-themed surface signals are present (Ababil of Minab Telegram, regional victim pattern) so non-state-opportunism reading is partially contradicted."
          wep: unlikely
        - rank: 5
          hypothesis_id: H1
          rationale: "Four inconsistencies via E3, E7, E8, E10. The sourced hypothesis is the LEAST consistent reading because the corroboration chain (Israel NCD citing Gambit) is effectively single-evidence-basis, no IOCs are published, no peer IR-firm corroborates, and Gambit is provisional-F. Critically: this does NOT mean H1 is false - it means H1 is under-evidenced. The directional attribution may be correct; the evidentiary basis is insufficient for elevation."
          wep: roughly_even_chance
      sensitivity_analysis:
        brittleness: high
        load_bearing_evidence: [E3, E7, E10]
        if_israel_ncd_publishes_independent_telemetry: "E3 flips from I (against H1) to C (for H1); H1 ranking improves dramatically; investigation can elevate above C3"
        if_mandiant_or_mstic_publishes_parallel_black_shadow_attribution: "E7 flips from I to C for H1; investigation elevates to B-tier"
        if_gambit_security_publishes_specific_iocs_that_a_b_grade_firm_validates: "E8, E10 weaken; H1 strengthens substantially"
        single_point_of_failure: "E3 is the single most-load-bearing piece - the 'Israel NCD cites Gambit' detail. If the Israel NCD publication is actually built on independent Israel-side telemetry, the entire H2 ranking collapses into H1."
      tripwires:
        - observation: "Mandiant / MSTIC / CrowdStrike / Recorded Future publishes parallel Black Shadow attribution within 14d investigation window"
          effect: "E7 flips; rerun ACH; H1 likely becomes ranked 1; consider /new-actor scaffolding"
        - observation: "Israel National Cyber Directorate publishes specific IOCs or telemetry independent of Gambit"
          effect: "E3 flips; H1 strengthens"
        - observation: "FBI / CISA public attribution of LACMTA to Iranian state-sponsored actor"
          effect: "Government-tier independent confirmation; H1 strengthens; H3 ruled out"
        - observation: "Gambit Security publishes follow-on research with specific IOCs that another A/B-grade firm validates"
          effect: "E8, E10 weaken; H1 strengthens"
        - observation: "LACMTA breach later attributed to specific tracked Iranian actor by an A/B-grade firm with Black Shadow → tracked-actor cross-walk"
          effect: "Rerun ACH; potential roster update"
      conclusion:
        summary: |
          The attribution chain (Gambit Security → Israel National Cyber
          Directorate → SecurityWeek) is effectively single-evidence-basis
          rather than genuine multi-source corroboration. H2 (downstream
          endorsement reading) is one inconsistency better than the sourced
          H1 framing; both are roughly-even-chance in WEP terms. ACH supports
          the grader's C3 single-source-veto. The investigation should NOT
          elevate above C3 on the basis of this finding's evidence. Black
          Shadow does NOT meet /new-actor scaffolding bar.
        wep: roughly_even_chance
        confidence_caveats: |
          The analyst's preferred reading (H2 - Israel NCD downstream
          endorsement) does NOT contradict the directional claim that Black
          Shadow may be a genuine MOIS cluster. It says the evidentiary basis
          is insufficient for elevation - not that the attribution is wrong.
          Per Hard Rule 2, analyst does NOT originate any alternative
          attribution. The investigation should carry forward through
          2026-06-09 T+14 awaiting A/B-grade IR-firm parallel attribution
          before elevation.

red_team_review_required: false
red_team_review_topics_skip_rationale: >
  WEP ceiling roughly_even_chance; below red-team WEP very_likely
  threshold. Investigation lock manages forward-looking elevation.

# Analyst review tracking
analyst_review_complete: true
analyst_review_run_id: analyst-20260527-084800
wep_ceiling_adjusted: false
wep_ceiling_adjustment_reason: >
  ACH confirms grader's C3 single-source-veto and WEP ceiling
  "roughly_even_chance" is appropriate. The matrix surfaces H2
  (downstream-endorsement reading) as one inconsistency better than the
  sourced H1 framing, supporting the grader's reading that the
  attribution chain is effectively single-evidence-basis. Investigation
  inv-2026-05-26-001 should carry forward through 2026-06-09 T+14
  awaiting A/B-grade IR-firm parallel attribution. No WEP adjustment
  needed.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-27-morning]
retracted: false
retraction_brief_id: null
---

# LACMTA cyberattack now attributed to Black Shadow / MOIS cluster (SecurityWeek relay of Gambit Security + Israel National Cyber Directorate)

## Summary

SecurityWeek (Eduard Kovacs, 2026-05-27 05:33 EDT) relayed an attribution update on the LA Metro (LACMTA) cyberattack: Gambit Security has named **Black Shadow** as the responsible cluster via configuration-fingerprint-based infrastructure linkage to previously-identified Iranian campaign infrastructure, and the Israel National Cyber Directorate frames Black Shadow as a **MOIS (Iran Ministry of Intelligence and Security)** cluster. This finding updates open Archimedes investigation **inv-2026-05-26-001**; it does NOT close the investigation. Per Hard Rule 2, Black Shadow is NOT cross-walked to any tracked Iranian actor in `_roster.yaml` despite the MOIS service-level match with MuddyWater (#022) and Handala Hack (#014) — no source makes that cross-walk explicitly. No A&D / aerospace / defense / DIB / CMMC / ITAR sector is named in the multi-victim regional campaign (US, Israel, Saudi Arabia, Turkey). Cluster digraph held at C3 single-source-veto: Gambit Security is a first-Archimedes-citation provisional-F source, and no parallel A/B-grade IR-firm attribution (Mandiant / Microsoft MSTIC / CrowdStrike / Recorded Future / Volexity / Unit 42 / Cisco Talos / CISA / FBI) is published as of this sweep.

## Sources

### SecurityWeek (securityweek, B-grade) — in-corpus proximate source

- URL: https://www.securityweek.com/la-metro-cyberattack-linked-to-iranian-state-sponsored-hackers/
- Published: 2026-05-27 09:33:45 UTC (05:33 EDT today, in-window)
- Byline: Eduard Kovacs
- Key claim: Relays Gambit Security + Israel National Cyber Directorate attribution of LACMTA breach to Black Shadow / MOIS cluster.

### Gambit Security (originating IR firm, provisional F — first Archimedes-corpus citation, no track record)

- Originating attribution research
- Configuration-fingerprint-based infrastructure linkage to previously-identified Iranian campaign infrastructure
- Status: not in `source-grades.yaml`; provisional F per cheatsheet for unknown research vendor with no prior corpus citation

### Israel National Cyber Directorate (B-grade government attribution)

- Government-tier endorsement of Gambit Security's attribution
- MOIS service-level framing
- Note: chain effectively single-evidence-basis if Israel National Cyber Directorate's publication is downstream of Gambit Security rather than built on independent Israel-side telemetry

## Technical detail

The attribution update layers on the prior open investigation:

**Prior state (as of inv-2026-05-26-001 opening 2026-05-26):**
- LACMTA breach disclosed with partial access confirmation
- Reuters and multiple wire affiliates carried Gambit Security's attribution to "previously identified Iranian campaign" infrastructure
- ~700 GB exfiltrated emails/backups/files via configuration-fingerprint-traced server
- Pro-Iran hacktivist group **Ababil of Minab** claimed via Telegram + `ababilofminab[.]io` 2026-04-09
- LACMTA confirmed partial access, declined to validate volumetric claims, declined comment on Gambit findings
- WEP ceiling: C3 single-source-veto

**Update via this finding (2026-05-27 relay):**
- Cluster name **Black Shadow** added (not previously named in the corpus)
- Service-level attribution **MOIS** added (per Israel National Cyber Directorate)
- Multi-victim regional campaign framing: US, Israel, Saudi Arabia, Turkey across media, education, insurance brokerage, restaurant, culture, digital services, news sectors
- **A&D sector explicitly ABSENT from the multi-victim list**

**What the relay does NOT add:**
- New A-grade IR-firm corroboration (Gambit Security remains the single originating IR firm)
- New victim disclosures beyond LA Metro
- New IOCs (no specific domain / IP / hash published in the SecurityWeek piece — infrastructure described at framework-level only)
- New TTP detail (no malware names, no C2 mechanism described)

## Hard Rule 2 compliance — critical framing

**Black Shadow is NOT in `threats/threat-actors/_roster.yaml`.** The five tracked Iranian actors are:
- UNC1549 (#004) — IRGC
- Charming Kitten (#011) — IRGC-IO
- Handala Hack (#014) — MOIS
- MuddyWater (#022) — MOIS
- APT34 (#023) — MOIS

**Black Shadow is a distinct cluster.** Per Hard Rule 2, Archimedes does NOT cross-walk Black Shadow to any tracked Iranian actor even though MOIS is the named service matching MuddyWater (#022) and Handala Hack (#014). Gambit Security itself made no such cross-walk; the Israel National Cyber Directorate's MOIS attribution is a service-level claim that does NOT identify a specific actor cluster within MOIS.

## A&D / aerospace / defense framing

- **Named A&D victim**: NONE
- **Named A&D sector**: NONE  
- **Multi-victim regional campaign scope**: US, Israel, Saudi Arabia, Turkey — A&D-sector explicitly absent
- **Iran Cyber Watch standing section relevance**: HIGH — this update is the canonical Iran Cyber Watch surface for the AM-27 brief
- **Tradecraft portability concern (per investigation file)**: Iranian state-sponsored hacktivist-front + MOIS-tier infrastructure pattern is a structural concern for A&D-prime defender awareness even absent direct A&D targeting; specifically, VMware vCenter + OT/ICS reach (from prior investigation context) describes capabilities that, if applied to an A&D prime, would matter for fab-floor / test-cell / HIL-rig / supplier-OT estates

## IOCs surfaced

None published in the SecurityWeek relay. Infrastructure described at framework-level only. For specific IOCs, Gambit Security primary publication or Israel National Cyber Directorate primary publication would need direct retrieval — neither was attempted this sweep.

## Relationship to existing findings

- **inv-2026-05-26-001** (LACMTA Iran attribution investigation, OPEN since 2026-05-26): this finding is the AM-27 update layer. Investigation remains open through 2026-06-09 T+14.
- **Iran Cyber Watch standing section corpus** (FDD 2026-05-20 frame; Ababil of Minab Telegram claim; Reuters/wire-affiliate Gambit Security attribution relay 2026-05-26): this finding sits within the same Iran Cyber Watch corpus thread.
- **No Iranian-actor finding closure**: per Hard Rule 2, no tracked Iranian actor profile is updated by this finding.

## Open questions for analyst

1. **Investigation carry-forward decision** (inv-2026-05-26-001): analyst evaluates whether Black Shadow naming + Israel National Cyber Directorate MOIS endorsement sufficiently corroborates Gambit Security to elevate the investigation's WEP ceiling above C3. The doctrine-edge question is whether Israel National Cyber Directorate's MOIS framing constitutes independent corroboration (if built on Israel-side telemetry) or downstream-endorsement of Gambit Security (if simply cites Gambit). Worth analyst review.
2. **/new-actor scaffolding decision for Black Shadow**: bar is at least one A-grade IR-firm source. Bar NOT yet met. Hold pending A/B-grade IR-firm corroboration. Re-evaluate if Mandiant / Microsoft MSTIC / CrowdStrike / Recorded Future publishes parallel Black Shadow attribution within the 14d window.
3. **SAT-ACH candidate**: competing hypotheses on the Black Shadow / MOIS attribution validity. (H1) Gambit Security's configuration-fingerprint methodology is sound and Black Shadow is a genuine MOIS cluster. (H2) Gambit Security mis-attributed; LACMTA breach is non-state cyber-criminal opportunism. (H3) Black Shadow is a real cluster but its MOIS attribution by Israel National Cyber Directorate is downstream-endorsement of Gambit rather than independent telemetry. Load-bearing evidence required: actual IOC publication by an A/B-grade IR firm with independent telemetry.

## Analytic notes (from analyst review)

SAT-ACH pressure-tested the Gambit Security → Israel National Cyber Directorate → SecurityWeek attribution chain against five hypotheses: sourced H1 (genuine multi-source MOIS attribution), H2 (Israel NCD endorsement is downstream of Gambit, not independent telemetry), H3 (criminal larp with Iranian theatrics), H4 (false-flag by competing state actor), and H5 (composite hacktivist-as-cover with Gambit retrofitting unrelated infrastructure linkage). H1 carries four inconsistencies — the highest count — driven by no IOC publication (E8), no peer A/B-grade IR-firm parallel attribution (E7), the corroboration chain being effectively single-evidence-basis (E3), and Gambit's provisional-F first-citation status (E10). H2 is one inconsistency better but is functionally a re-framing of H1 rather than a contradiction; the directional MOIS claim may still be correct.

The analyst output is to confirm the grader's C3 single-source-veto and hold the investigation at roughly-even-chance. Black Shadow does NOT meet /new-actor scaffolding bar. The investigation should carry forward through 2026-06-09 T+14 awaiting A/B-grade IR-firm parallel attribution. Critical tripwire: if Mandiant / MSTIC / CrowdStrike / Recorded Future publishes parallel Black Shadow attribution within window, rerun this ACH — H1 likely becomes rank 1. Briefer note: present this as Iran Cyber Watch monitoring tier, NOT action tier, and explicitly preserve the C3 confidence framing.

## Hard Rule compliance

- **Hard Rule 2**: Attribution language preserved verbatim per SecurityWeek + Gambit + Israel National Cyber Directorate framing. NO cross-walk to tracked Iranian actors despite MOIS service match. Black Shadow NOT added to `_roster.yaml`. ACH did NOT originate alternative attribution; the H2/H4/H5 hypotheses are listed to pressure-test H1, not to assert as Archimedes claims.
- **Hard Rule 3**: No PoC, no exploit primitive, no working attack chain reproduced.
- **Hard Rule 6**: No direct quotes >15 words; attribution language paraphrased.
- **Hard Rule 8**: Splunk first-party check executed; zero events; silence not disconfirming.
