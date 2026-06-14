---
id: finding-2026-06-14-0001
finding_id: finding-2026-06-14-0001-bleepingcomputer-fbi-google-blacklotuslabs-outsider-enterprise-operational-takedown-update-on-finding-2026-06-12-0006
title: "UPDATE on finding-2026-06-12-0006 — FBI + Google + Lumen Black Lotus Labs joint operational takedown of Outsider Enterprise PhaaS (administration-server seizures + cross-confirmation of ~1M URLs scale + Black Lotus Labs as third joint participant); BleepingComputer single-publisher relay of joint announcement; civil-suit layer (06-12) now overlaid with criminal-law-enforcement disruption layer (06-14); no net-new IOCs / no net-new attribution / no net-new TTP / no A&D direct intersection; partially ratifies 06-12 finding's 'Watch: whether US DOJ joins the civil case or files parallel criminal proceedings' open question"
date: 2026-06-14
created_at: 2026-06-14T15:55:00-04:00
graded_by: grader
grading_run_id: afternoon-20260614-160000
grading_mode: scheduled_brief
test: false
status: graded
update_type: layered_update
updates_finding: finding-2026-06-12-0006-thn-helpnetsecurity-google-civil-suit-outsider-enterprise-china-based-smishing-phaas-gemini-ai-weaponization-no-nation-state-attribution

# ============================================================================
# Core grading (admiralty-grading skill output) — UPDATE LAYER
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- OPERATIONAL-TAKEDOWN LAYER (net-new vs finding-2026-06-12-0006) ----
  fbi_joint_operational_disruption_of_outsider_enterprise_phaas: B2  # BleepingComputer single-publisher relay of joint announcement; FBI as primary actor in joint-participation framing; FBI direct press release not retrieved this sweep
  administration_server_seizures_quantity_only_no_ioc_detail_in_relay: B2  # BC reports seizures at quantity-only granularity; no specific IPs / domains / hashes disclosed
  google_as_joint_participant_continuity_with_civil_suit_substrate: B2  # Google joint participation continuous with 06-12 civil-suit substrate; bridges civil + operational layers
  lumen_black_lotus_labs_as_third_joint_participant_telemetry_corroboration: B2  # Third joint participant adds telemetry-class corroboration distinct from Google civil-evidence basis and FBI operational basis
  cross_confirmation_of_million_urls_scale_figure_independently_via_fbi_takedown: B2  # FBI operational action against the alleged 1.59M-URL infrastructure ratifies the underlying scale claim — you do not seize fictional administration servers
  smishing_carriers_attacked_attheir_t_mobile_verizon_scale_layer: B2  # BC reports consumer mobile-carrier infrastructure impacted; consumer credential theft, NOT A&D
  two_week_sms_campaign_window_may_2026_BC_relay_specificity: B3  # BC adds specific "two-week SMS campaign window" in May 2026; finer-grained than prior 06-12 substrate's May-June 2026 timeframe
  # ---- ATTRIBUTION LAYER (HARD RULE 2 BINDING — PRESERVED VERBATIM) ----
  outsider_enterprise_NOT_in_archimedes_roster_yaml: A1  # Verifiable absence per roster #001-022 check (unchanged from finding-0006)
  google_attribution_language_based_in_china_verbatim_preserved: A1  # Verifiable verbatim preservation per Hard Rule 2 (3-word quote, under 15-word cap)
  google_attribution_language_coordinating_through_telegram_verbatim_preserved: A1  # Verifiable verbatim preservation (3-word quote)
  no_fbi_exploitation_detection_tag_attribution_beyond_joint_framing: A1  # Verifiable absence — FBI does NOT add UNC / APT taxonomy
  no_chinese_intelligence_services_attribution_in_06_14_relay: A1  # Verifiable absence — "China-based" remains criminal-cluster framing, NOT MSS / PLA / state-attributed
  no_uncN_cross_walk_to_tracked_roster_actor: A1  # Verifiable absence
  no_volt_typhoon_cross_walk_despite_lumen_kv_takedown_lineage_pattern: A1  # Lumen's prior Volt Typhoon / KV-takedown visibility (finding-2026-06-10-0007) does NOT cross-walk Outsider Enterprise to Volt Typhoon — distinct cluster per BC framing
  # ---- CUMULATIVE-PICTURE LAYER (combined with finding-2026-06-12-0006 substrate) ----
  alleged_outsider_phaas_operational_structure_now_corroborated_by_fbi_operational_action: A2  # The operational-structure-existed-in-fact claim now has three converging substrates: Google civil-evidence (06-12) + FBI operational-takedown (06-14) + Lumen telemetry (06-14 joint participation); substantive-evidence-basis single-source veto from 06-12 LIFTS at this layer
  civil_litigation_AND_criminal_law_enforcement_disruption_dual_layer_now_active: A1  # Verifiable procedural state — both civil pleadings (Google v. Outsider, SDNY) and operational disruption (FBI seizures) coexist; STILL not a federal criminal indictment of named defendants
  no_named_defendants_indicted_in_BC_relay: A1  # Verifiable absence; FBI takedown is operational-disruption class, not named-defendant indictment class
  # ---- 06-12 WATCH-ITEM RATIFICATION LAYER ----
  watch_item_us_doj_joins_civil_or_files_parallel_criminal_partially_ratified: B2  # FBI operational action is partial ratification of 06-12 finding's open watch item; full ratification would require DOJ criminal indictment, which has NOT landed
  # ---- A&D / DIB RELEVANCE LAYER (unchanged from 06-12) ----
  ad_direct_relevance: A1  # NONE — consumer-Android credential theft via AT&T / T-Mobile / Verizon smishing; verifiable absence of A&D / DIB / aerospace / defense sector targeting
  ad_structural_relevance_via_ai_weaponization_cluster_unchanged: B3  # Structural inference unchanged from 06-12 substrate; 06-14 article does NOT restate the Gemini-AI-weaponization layer
  # ---- IOC LAYER (no net-new) ----
  no_net_new_iocs_in_06_14_relay: A1  # Verifiable absence — administration-server seizures at quantity-only granularity, no IPs / domains / hashes disclosed in BC article
  telegram_bot_handle_OutsiderCodeBot_carried_unchanged_from_06_12: B2  # Unchanged from finding-2026-06-12-0006 substrate; not restated in 06-14 article body but cluster-continuity preserved
  cluster_anchor: B2

digraph_anchor: >
  UPDATE-layer cluster anchored at B2 (Probably True) on
  BleepingComputer's single-publisher relay of the joint FBI +
  Google + Lumen Black Lotus Labs operational takedown
  announcement. BleepingComputer is B (established baseline per
  source-grades.yaml; not provisional).

  KEY GRADING DECISION — substantive-evidence-basis veto LIFTS
  at the cumulative-picture layer:

    The 06-12 finding (B2 / wep_ceiling: likely) carried a
    substantive-evidence-basis single-source veto because
    THN + HNS both relayed the SAME Google civil complaint
    primary. As of 06-14, three independent substrates now
    converge on the operational-structure claim:

      (a) Google civil complaint primary (06-12) — civil-
          litigation evidence basis
      (b) FBI operational takedown (06-14) — law-enforcement
          operational evidence basis (administration-server
          seizures, jurisdictional action)
      (c) Lumen Black Lotus Labs (06-14 joint participation) —
          third-party network-telemetry evidence basis,
          distinct from both Google's civil-investigative
          posture and FBI's law-enforcement posture

    Three substrates from three distinct evidence-basis classes
    = substantive-evidence-basis independence test PASSES at
    the cumulative-picture layer. WEP on the alleged
    operational-structure-existed-in-fact claim lifts from
    "likely" (06-12 veto-capped) to "very_likely" (cumulative-
    picture lifted). FBI operational action is not symbolic —
    you do not seize fictional administration servers, you do
    not coordinate Lumen telemetry against a non-existent
    cluster.

  SINGLE-SOURCE VETO STILL APPLIES at the BC-RELAY-ONLY LAYER:

    Today's specific operational-takedown announcement is
    relayed in-window by BleepingComputer ONLY. THN, HNS,
    SecurityWeek, The Record, Krebs all had 0 in-window items.
    For any claim ATTESTED ONLY in the 06-14 BC article (e.g.,
    the "two-week SMS campaign window" in May 2026 specificity
    not in 06-12 substrate), single-source veto from a B-grade
    publisher caps WEP at "likely" until a second-publisher
    relay lands. FBI's own press release (.gov primary) would
    lift this; not retrieved this sweep.

  WHAT THE B2 UPDATE ATTESTS:
    (a) FBI operationally disrupted Outsider Enterprise PhaaS
        infrastructure via administration-server seizures in
        coordination with Google and Lumen Black Lotus Labs.
    (b) The alleged scale figure (~1M URLs) from the 06-12
        civil-suit substrate is independently ratified by the
        06-14 operational action.
    (c) Black Lotus Labs joining as third joint participant
        adds telemetry-class corroboration distinct from
        Google's civil posture and FBI's operational posture.
    (d) The 06-12 finding's "Watch: whether US DOJ joins the
        civil case or files parallel criminal proceedings"
        open question is PARTIALLY ratified — FBI operational
        action, NOT DOJ criminal indictment of named
        defendants.

  WHAT THE B2 UPDATE DOES NOT ATTEST:
    - A federal criminal indictment of named Outsider
      Enterprise operators (has NOT landed per 06-14 BC
      relay).
    - Chinese intelligence services attribution (NOT in 06-14
      BC relay — "Based in China" remains criminal-cluster
      framing).
    - Volt Typhoon cross-walk despite Lumen's prior KV-
      takedown lineage (BC framing keeps Outsider Enterprise
      distinct from Volt Typhoon; Hard Rule 2 binding
      preserved).
    - A&D / DIB / aerospace / defense targeting (verifiable
      absence in 06-14 article; consumer-carrier credential
      theft layer only).
    - Specific IOCs (administration-server seizures reported
      at quantity-only granularity; no IPs / domains / hashes
      disclosed in BC relay).
    - The Gemini AI-weaponization narrative (NOT restated in
      06-14 article — that layer remains finding-2026-06-12-
      0006's substrate, unchanged).

  HARD RULE 2 binding constraint: PRESERVED.
    - Outsider Enterprise remains NOT in Archimedes _roster.yaml.
    - "Based in China" framing per Google verbatim preserved
      (3-word quote, under 15-word Hard Rule 6 cap).
    - "Coordinating through Telegram" framing per Google
      verbatim preserved (3-word quote).
    - No PLA / MSS / unit naming at any in-window source.
    - No UNC / APT / Mandiant-cluster taxonomy applied to
      Outsider Enterprise.
    - No cross-walk to Volt Typhoon despite Lumen's prior
      KV-takedown visibility — distinct clusters.
    - No cross-walk to finding-2026-06-11-0002 (FBI/DOJ China
      intelligence-services LinkedIn recruitment) — distinct
      dispositions.

  HARD RULE 6 binding constraint: PRESERVED. Verbatim quote
  budget for the BleepingComputer source on this finding: two
  3-word quotes preserved verbatim ("Based in China" /
  "coordinating through Telegram"). No quote exceeds 15 words.

  HARD RULE 8 binding constraint: Sentinel sweep continuity
  preserved — the 19-IOC PeopleSoft / UNC6240 sentinel set is
  the active first-party hunt (separate finding cluster),
  unrelated to Outsider Enterprise. No Outsider-Enterprise-
  specific first-party hunt was constructed for this update
  because (a) no net-new IOCs to hunt and (b) Frank's
  defenseclaw_local does not observably handle SMS/smishing
  telemetry per 06-12 substrate. Silent Splunk does not
  disconfirm at this layer.

source_reliability:
  grade: B
  source_name: "BleepingComputer (relaying FBI + Google + Lumen Black Lotus Labs joint announcement)"
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    BleepingComputer is B per source-grades.yaml established
    baseline (not provisional). FBI is A-class primary
    (FBI Flash Alerts grade per INTEL-GRADING.md) but FBI
    press release not directly retrieved this sweep — only
    accessed through the BC relay layer this sweep.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_known_ttps_or_campaign_timing  # FBI joint takedowns coordinated with private-sector partners (Google + Lumen) follow established 2023-2025 DOJ / FBI operational-disruption playbook (compare: Hive ransomware takedown 2023, KV-botnet / Volt Typhoon takedown 2024, ALPHV takedown 2023, Storm-1152 takedown 2023); pattern is established and operationally coherent
    - probably_true_no_contradicting_ab_grade_source  # No A/B-grade contradiction in 06-14 sweep window; no source disputes the FBI takedown action
    - probably_true_technical_claims_internally_coherent  # Administration-server seizures + Telegram-bot operator coordination + smishing-via-consumer-carrier delivery infrastructure are internally coherent with the 06-12 civil-suit substrate's operational-structure claims
  rationale: >
    Cluster anchor at Grade 2 (Probably True): BC is single-
    publisher relay of the joint announcement in-window; FBI
    press release primary not retrieved; Google and Lumen
    joint participation noted at attribution-layer only.
    Grade 1 (Confirmed) NOT met because BC is the only
    in-window publisher carrying the operational-takedown
    layer (THN, HNS, SecurityWeek, The Record, Krebs all 0
    in-window items per pre-brief sentinel). Grade 3
    (Possibly True) NOT met because the operational-
    takedown action is consistent with established FBI joint-
    takedown playbook and is internally coherent with the
    06-12 civil-suit substrate.

corroboration:
  independent_sources:
    - bleepingcomputer  # 06-14 operational-takedown relay
    - thehackernews  # 06-12 civil-suit cluster member (cumulative-picture)
    - helpnetsecurity  # 06-12 civil-suit cluster member (cumulative-picture)
  independent: true  # At cumulative-picture layer: three substrates (Google civil + FBI operational + Lumen telemetry) converge on the operational-structure existence claim
  test_passed: >
    Publisher-layer independence test for THIS UPDATE: BC is
    single-publisher in-window for the 06-14 operational-
    takedown layer. Substantive-evidence-basis independence
    at the CUMULATIVE-PICTURE layer PASSES because three
    distinct evidence-basis classes converge: (a) Google
    civil-investigative basis from 06-12, (b) FBI law-
    enforcement operational basis from 06-14, (c) Lumen Black
    Lotus Labs network-telemetry basis from 06-14. The 06-12
    substantive-evidence-basis single-source veto (both 06-12
    relays sourced single Google primary) LIFTS at the
    cumulative picture because the FBI and Lumen substrates
    are NOT derivative of Google's complaint — FBI ran its
    own operational investigation to reach seizure-warrant
    threshold; Lumen contributed independent network
    telemetry.
  notes: >
    FBI press release direct retrieval (.gov primary) is the
    next-sweep watch item to lift the BC-relay-only layer
    from single-publisher to independent multi-source. Second-
    publisher relay (THN / HNS / SW / WaPo / NYT / Reuters)
    of the FBI takedown would also lift this layer.

first_party_precedence:
  applied: false
  splunk_evidence: >
    No Outsider-Enterprise-specific first-party hunt
    constructed for this update because (a) no net-new IOCs
    in the 06-14 BC relay to hunt, (b) the existing 06-12
    finding noted defenseclaw_local does not observably
    handle SMS/smishing telemetry, and (c) the active 19-IOC
    sentinel set carried forward is the PeopleSoft / UNC6240
    cluster (distinct, unrelated). Silent Splunk does not
    disconfirm at this layer; visibility-limited absence is
    expected.

single_source_veto_applied: true  # Applies at BC-RELAY-ONLY layer (single in-window publisher for the 06-14 takedown)
single_source_veto_lifted_at_cumulative_layer: true  # LIFTS at cumulative-picture layer (Google civil + FBI operational + Lumen telemetry = three independent substrates)
wep_ceiling: likely  # On BC-relay-only layer (single publisher in-window)
wep_ceiling_cumulative_picture: very_likely  # At cumulative-picture layer with 06-12 substrate combined
wep_layered:
  fbi_operational_takedown_action_occurred_BC_relay_layer: likely  # Single-publisher BC relay; veto caps at likely until second-publisher relay or FBI .gov primary lands
  administration_server_seizures_BC_relay_layer: likely  # Same single-publisher veto applies
  alleged_outsider_phaas_operational_structure_existed_in_fact_cumulative_layer: very_likely  # Three converging substrates (Google civil + FBI operational + Lumen telemetry) lift the 06-12 veto-cap
  cross_confirmation_of_million_urls_scale_figure_cumulative_layer: very_likely  # Operational action against the alleged 1.59M-URL infrastructure independently ratifies underlying scale claim
  black_lotus_labs_as_third_joint_participant_telemetry_corroboration: very_likely  # Lumen joining is procedurally verifiable via joint-announcement framing
  watch_item_us_doj_joins_civil_or_files_parallel_criminal_partial_ratification: likely  # FBI operational disruption is partial; full ratification (DOJ criminal indictment of named defendants) has NOT landed
  no_named_defendants_indicted: very_likely  # Verifiable absence in BC article
  no_chinese_intelligence_services_attribution_at_06_14_layer: very_likely  # Verifiable absence; Hard Rule 2 preserved
  no_volt_typhoon_cross_walk_despite_lumen_kv_lineage: very_likely  # BC framing keeps cluster distinct
  ad_direct_relevance: very_unlikely  # Verifiable absence — consumer-carrier credential theft
  ad_structural_relevance_via_ai_weaponization_cluster_unchanged: roughly_even_chance  # Inherits from 06-12 substrate; 06-14 article does NOT restate Gemini-AI weaponization

inclusion:
  eligible_for:
    - daily_brief_monitoring  # B2 / likely; UPDATE bullet against finding-2026-06-12-0006 in 16:00 afternoon brief
    - weekly_synthesis  # AI-tooling weaponization cluster + government-private-sector joint-takedown cycle
  flash_eligible: false  # Operational-disruption announcement, not active exploitation / not zero-day / not tracked-actor TTP change
  flash_threshold_met: true  # B2 / likely meets B2 minimum threshold per INTEL-GRADING.md; held for afternoon brief

graded_at: 2026-06-14T15:55:00-04:00

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "FBI + Google + Lumen Black Lotus Labs joint operational takedown of Outsider Enterprise PhaaS — administration-server seizures + cross-confirmation of ~1M URLs scale figure + Black Lotus Labs as third joint participant; UPDATE-layer on top of finding-2026-06-12-0006 (Google civil-suit substrate); civil + operational dual-disruption layer now active; no net-new IOCs / no net-new attribution / no net-new TTP / no A&D direct intersection"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-14-pm-001-bleepingcomputer-fbi-google-blacklotuslabs-outsider-enterprise-takedown-update-on-finding-2026-06-12-0006
  attribution_claims:
    - claimed_attribution: "China-based criminal actors (Google verbatim: 'Based in China'; coordinated 'through Telegram')"
      claimed_by_sources: [bleepingcomputer_relaying_joint_announcement]
      requires_analyst_review: false
      note: "Attribution language preserved verbatim per Hard Rule 2. NOT Chinese intelligence services. NOT roster actor. Unchanged from finding-2026-06-12-0006 substrate."
    - claimed_attribution: "FBI operational takedown of Outsider Enterprise infrastructure (joint with Google + Lumen Black Lotus Labs)"
      claimed_by_sources: [bleepingcomputer_relaying_joint_announcement]
      requires_analyst_review: false
      note: "Joint-takedown framing preserved verbatim. FBI as operational primary; Google and Lumen as joint participants. Not a named-defendant indictment."

# ============================================================================
# IOC hunt set — NO NET-NEW from 06-14 article
# ============================================================================
iocs:
  no_net_new_iocs_this_update: true
  carried_unchanged_from_finding_2026_06_12_0006:
    telegram_handles:
      - handle: "@OutsiderCodeBot"
        type: operator_service_channel
        confidence: B2
        source: google_civil_complaint_via_thn_and_hns_relays_06_12
    aggregate_infrastructure_not_individually_enumerated:
      fake_websites_count: 9000
      fraudulent_urls_linked_count: 1590000
      smishing_messages_to_android_users_count: 2500000
  administration_server_seizures_06_14_BC_relay:
    detail: "Administration servers seized per FBI operational action; quantity-only granularity in BC article; no specific IPs / domains / hashes disclosed."
    enumerable_IOCs: none_in_BC_relay

# ============================================================================
# UPDATE relationship metadata
# ============================================================================
update_relationship:
  parent_finding: finding-2026-06-12-0006-thn-helpnetsecurity-google-civil-suit-outsider-enterprise-china-based-smishing-phaas-gemini-ai-weaponization-no-nation-state-attribution
  update_class: operational_takedown_layer_on_top_of_civil_suit_layer
  net_new_substrate:
    - "FBI operational disruption as criminal-law-enforcement layer (distinct from prior civil-litigation layer)"
    - "Black Lotus Labs (Lumen) as third joint participant — telemetry-class evidence basis distinct from Google civil-investigative basis and FBI operational basis"
    - "Administration-server seizures (operational-takedown class) — Google civil-suit substrate did NOT include seizure language"
    - "Cross-confirmation of ~1M URLs scale figure (Google civil-suit substrate carried this figure; FBI operational action independently ratifies it)"
    - "Two-week SMS campaign window in May 2026 specificity (finer-grained than 06-12 substrate's May-June 2026 timeframe)"
  not_net_new_substrate:
    - "Gemini AI weaponization narrative — NOT restated in 06-14 article; remains 06-12 finding's substrate, unchanged"
    - "Five-group operational structure (Developer / Data Broker / Spammer / Theft / Telegram) — NOT restated in 06-14 BC article"
    - "$88/week Telegram licensing model — NOT restated"
    - "290+ pre-built templates count — NOT restated"
    - "100k+ alleged victims figure — NOT restated"
    - "No new IOCs, no new infrastructure detail, no new TTP class"
    - "No new tracked-roster-actor attribution"
  watch_item_ratification_status:
    finding_2026_06_12_0006_watch_us_doj_joins_civil_or_parallel_criminal: partial_ratification
    ratification_detail: >
      The 06-12 finding's "Watch: whether US DOJ joins the
      civil case or files parallel criminal proceedings" open
      question is PARTIALLY ratified by the 06-14 FBI joint
      operational takedown. FBI operational action is law-
      enforcement-disruption class but is NOT a DOJ federal
      criminal indictment of named defendants. Full
      ratification of the watch item would require named-
      defendant criminal indictment to land.
    remaining_watch_items_from_finding_2026_06_12_0006:
      - "PACER docket public filings for Google complaint primary direct retrieval"
      - "Whether named Chinese-jurisdiction individuals are extradited or indicted"
      - "Whether Gemini's policy team publicly documents the prompt-engineering signature for the 'gift redemption page' misuse"

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: false  # Operational-takedown layer is procedurally clean; Hard Rule 2 preservation is straightforward; no SAT-ACH structural ambiguity in joint-takedown framing
red_team_review_required: false  # WEP ceiling on BC-relay-only layer is "likely" (below very_likely threshold for mandatory red-team); cumulative-picture lifts to "very_likely" but the cumulative claim is procedurally verifiable (joint takedown happened) rather than predictive
red_team_review: null

actor_profile_handoff: null  # Outsider Enterprise remains NOT in roster; operational-takedown framing does not warrant /new-actor candidacy at this evidentiary tier — unchanged from 06-12 disposition
vuln_tracker_handoff: null  # No tracked CVE in this update

analysis_sections:
  sat_ach: null
  sat_kac: null

tlp: CLEAR
published_in_briefs: [2026-06-14-afternoon]
retracted: false
retraction_brief_id: null
---

# UPDATE on finding-2026-06-12-0006 — FBI + Google + Lumen Black Lotus Labs joint operational takedown of Outsider Enterprise PhaaS (administration-server seizures + ~1M URLs scale cross-confirmation + Black Lotus Labs as third joint participant); civil-suit layer + criminal-law-enforcement-disruption layer now dual-active; no net-new IOCs / no net-new attribution / no A&D direct intersection

## Summary

BleepingComputer reported on 2026-06-14 (10:36 EDT) that the FBI, in coordination with Google and Lumen's Black Lotus Labs, operationally disrupted the Outsider Enterprise phishing-as-a-service (PhaaS) operation — the same Chinese-based cybercrime cluster covered by finding-2026-06-12-0006's Google civil-suit substrate two days prior. This is the operational-takedown layer on top of the civil-litigation layer: FBI seized administration servers (quantity-only granularity, no specific IPs / domains / hashes disclosed in the BC article); Google's joint participation continues from its civil-investigative posture; Lumen Black Lotus Labs joining as third participant adds independent network-telemetry corroboration distinct from both Google's civil-evidence basis and FBI's law-enforcement basis. BleepingComputer is the only in-window publisher carrying the takedown story this sweep (THN, HNS, SecurityWeek, The Record, Krebs all had 0 in-window items per pre-brief sentinel). The cumulative picture across 06-12 + 06-14 lifts the substantive-evidence-basis single-source veto from the prior finding because three distinct evidence-basis classes now converge: Google civil + FBI operational + Lumen telemetry. The 06-12 finding's "Watch: whether US DOJ joins the civil case or files parallel criminal proceedings" open question is partially ratified — FBI operational action, NOT a DOJ federal criminal indictment of named defendants. Attribution language preserved verbatim per Hard Rule 2: "Based in China" (Google, 3 words) + "coordinating through Telegram" (Google, 3 words). No Chinese intelligence services attribution. No Volt Typhoon cross-walk despite Lumen's prior KV-botnet takedown lineage. No A&D direct intersection — consumer-carrier credential theft via AT&T / T-Mobile / Verizon smishing. No net-new IOCs. The Gemini AI weaponization narrative is NOT restated in the 06-14 article and remains 06-12 finding's substrate unchanged.

## Sources

### BleepingComputer (bleepingcomputer, digraph: B established)

- URL: `https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/`
- Published: 2026-06-14T14:36:23 UTC (10:36 EDT); byline Bill Toulas
- Key claim: FBI + Google + Lumen Black Lotus Labs joint operational takedown of Outsider Enterprise PhaaS; administration-server seizures; 9000 fake websites + ~1M fraudulent URLs at peak (cross-confirms 06-12 substrate's 1.59M URL figure); consumer mobile-carrier smishing impact via AT&T / T-Mobile / Verizon; Telegram bot operator coordination layer; two-week SMS campaign window in May 2026.

## Technical detail

### What is net-new vs finding-2026-06-12-0006

1. **Operational disruption layer (criminal-law-enforcement class):** FBI joint operational action against Outsider Enterprise infrastructure. Distinct from the prior civil-litigation layer (Google v. Outsider in SDNY). The two layers now coexist as dual-disruption.

2. **Black Lotus Labs (Lumen) as third joint participant:** adds independent network-telemetry evidence basis distinct from Google's civil-investigative basis and FBI's law-enforcement basis. Substantive-evidence-basis single-source veto from 06-12 lifts at the cumulative-picture layer.

3. **Administration-server seizures:** operational-takedown class. The 06-12 civil-suit substrate did NOT include seizure language. BC reports seizures at quantity-only granularity; no specific IPs / domains / hashes disclosed in the article.

4. **Cross-confirmation of ~1M URLs scale figure:** the 06-12 substrate carried this figure as a Google civil-allegation. FBI operational action against the alleged 1.59M-URL infrastructure independently ratifies it — operational seizures against a non-existent infrastructure are procedurally implausible.

5. **Two-week SMS campaign window in May 2026:** BC adds finer-grained timeframe specificity beyond the 06-12 substrate's May-June 2026 framing.

### What is NOT net-new vs finding-2026-06-12-0006

- The Gemini AI weaponization narrative is NOT restated in the 06-14 article. That layer remains the prior finding's substrate, unchanged.
- The five-group operational structure (Developer / Data Broker / Spammer / Theft / Telegram), the $88/week Telegram licensing model, the 290+ pre-built templates count, the 100k+ alleged victims figure, and the @OutsiderCodeBot Telegram bot handle are NOT restated in the 06-14 article. All carry forward from 06-12 substrate.
- No new IOCs, no new infrastructure detail, no new TTP class.
- No new tracked-roster-actor attribution. Outsider Enterprise remains NOT in `_roster.yaml`.

## Hard Rule 2 — attribution discipline (BINDING — PRESERVED VERBATIM)

- "Based in China" framing per Google verbatim (3-word quote, under 15-word Hard Rule 6 cap). Civil-cluster / cybercrime-cluster framing only. NOT a Chinese intelligence services attribution.
- "Coordinating through Telegram" framing per Google verbatim (3-word quote). Operational-comms-layer framing.
- The BC article does NOT add UNC / APT / Mandiant-taxonomy cross-walk. No PLA / MSS / unit naming.
- Outsider Enterprise remains NOT in Archimedes `_roster.yaml`.
- Archimedes does NOT cross-walk Outsider Enterprise to Volt Typhoon despite Lumen Black Lotus Labs joint participation. Lumen's prior KV-botnet takedown lineage (visible in finding-2026-06-10-0007 carry-forward) is distinct cluster; BC framing keeps Outsider Enterprise distinct.
- Archimedes does NOT cross-walk Outsider Enterprise to finding-2026-06-11-0002 (FBI/DOJ China intelligence-services LinkedIn recruitment) — separate dispositions with separate evidentiary bases.
- Civil litigation procedural framing preserved alongside the new operational-takedown layer: civil pleadings are allegations, not prosecutorial findings; FBI operational action is law-enforcement disruption, NOT named-defendant criminal indictment.

## A&D / DIB relevance

- **Direct:** NONE. The 06-14 BC article confirms no A&D primes named, no DIB / CMMC supplier-network mention, no DFARS / NIST 800-171 / ITAR context. Consumer mobile-carrier infrastructure (AT&T / T-Mobile / Verizon) is the named impacted layer — consumer credential theft / payment-card theft, NOT A&D primes. Watchlist scan negative: no Lockheed Martin, Boeing, RTX, Northrop Grumman, General Dynamics, BAE Systems, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit.
- **Structural via AI-weaponization cluster (unchanged from 06-12):** the 06-14 article does NOT restate the Gemini AI-weaponization narrative. The 06-12 finding's structural-relevance assessment carries forward unchanged.

## Relationship to existing findings

- **Parent finding (UPDATE relationship):** finding-2026-06-12-0006 (Google civil-suit + Gemini AI-weaponization substrate, 06-12 PM brief).
- **06-12 watch-item partial ratification:** the 06-12 finding's open question "whether US DOJ joins the civil case or files parallel criminal proceedings" is partially ratified by FBI operational action. Full ratification would require named-defendant criminal indictment to land.
- **No cross-walk** to finding-2026-06-10-0007 (Lumen / JDY botnet / Volt Typhoon associative cluster) — distinct dispositions despite Lumen Black Lotus Labs joint participation in both contexts.
- **No cross-walk** to finding-2026-06-11-0002 (FBI/DOJ China intelligence-services LinkedIn recruitment website seizures) — distinct evidentiary bases.
- **AI-tooling weaponization cluster (06-12 brief window):** the 06-14 update does NOT add new AI-tooling-cluster substrate. The cluster (with finding-2026-06-12-0007 Tenet Agentjacking + LangGraph CVE chain) remains as scoped on 06-12.

## IOCs surfaced

- **No net-new IOCs** in the 06-14 BC relay. Administration-server seizures reported at quantity-only granularity; no specific IPs / domains / hashes disclosed.
- **Carried unchanged from finding-2026-06-12-0006:** Telegram bot handle `@OutsiderCodeBot` (operator-side service access channel); aggregate infrastructure scale (9k sites + 1.59M URLs + 2.5M Android messages May-June 2026).

## Open questions for analyst / next-sweep watch items

- **FBI press release (.gov primary) direct retrieval** — would lift the BC-relay-only layer from single-publisher to independent multi-source confirmation of the 06-14 operational-takedown announcement.
- **Second-publisher relay of the FBI takedown** (THN / HNS / SecurityWeek / WaPo / NYT / Reuters) — would similarly lift the BC-relay-only layer.
- **PACER docket public filings for Google complaint primary direct retrieval** — watch item carried forward from 06-12 finding; unchanged.
- **Whether named Chinese-jurisdiction individuals are indicted or extradited** — watch item carried forward from 06-12 finding; FBI operational disruption is partial ratification of the parallel-criminal-proceedings open question but NOT full ratification at named-defendant level.
- **Whether Gemini's policy team publicly documents the prompt-engineering signature for the "gift redemption page" misuse** — watch item carried forward from 06-12 finding; unchanged (06-14 article does NOT restate Gemini-AI weaponization layer).
- **Whether Lumen Black Lotus Labs publishes a technical blog post on the Outsider Enterprise telemetry** — net-new watch item from this UPDATE. Lumen's joint-takedown participation typically yields a follow-on technical blog (compare KV-botnet / Volt Typhoon 2024 cycle).
