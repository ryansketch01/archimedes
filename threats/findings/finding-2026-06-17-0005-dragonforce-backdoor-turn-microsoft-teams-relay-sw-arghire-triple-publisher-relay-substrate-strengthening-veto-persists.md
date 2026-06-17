---
id: finding-2026-06-17-0005
finding_id: finding-2026-06-17-0005-dragonforce-backdoor-turn-microsoft-teams-relay-sw-arghire-triple-publisher-relay-substrate-strengthening-veto-persists
title: "SecurityWeek (Ionut Arghire) trade-press journalistic relay extends Symantec DragonForce Backdoor.Turn / Microsoft Teams TURN-relay substrate (finding-2026-06-16-0004) from PM-brief BC+HNS dual-publisher to BC+HNS+SW triple-publisher journalistic relay — substrate-strengthening on publisher-independence layer NOT on IR-vendor-corroboration layer; single-vendor-on-novel-TTP-layer veto persists (Symantec sole IR-vendor on Backdoor.Turn novel TURN-relay TTP; Mandiant / CrowdStrike / Unit 42 / MSTIC independent IR-vendor corroboration remains substrate-that-would-lift-veto); Scattered-Spider / DragonForce linkage Hard-Rule-2 BINDING preserved (Scattered-Spider dossier mutation PAUSED pending independent second-IR-vendor corroboration); no net-new technical detail in SW relay beyond Symantec primary substrate already captured in finding-0004; WEP unchanged at 'likely' on novel-TTP layer; A&D-relevance via operational-template inheritance MEDIUM (Microsoft Teams TURN-relay abuse is identical-class novel TTP affecting any A&D-prime Teams tenant)"
date: 2026-06-17
created_at: 2026-06-17T08:18:00-04:00
graded_by: grader
grading_run_id: morning-20260617-080000
grading_mode: scheduled_brief
test: false
status: graded

update_pivot_on: finding-2026-06-16-0004
update_type: substrate_strengthening_triple_publisher_relay_veto_persists

# ============================================================================
# Core grading
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- SW-ARGHIRE TRADE-PRESS RELAY LAYER (PUBLISHER-INDEPENDENCE) ----
  sw_arghire_third_independent_b_grade_publisher_relay: B2
  triple_publisher_journalistic_relay_bc_hns_sw: B2  # publisher-independence layer
  publisher_independence_not_ir_vendor_corroboration: A1  # doctrinal distinction
  single_vendor_on_novel_ttp_veto_persists: A1
  # ---- ATTRIBUTION-DISCIPLINE LAYER (HARD RULE 2 BINDING) ----
  symantec_asserted_dragonforce_scattered_spider_linkage_preserved_verbatim: A1
  scattered_spider_dossier_mutation_paused_per_hard_rule_2: A1
  archimedes_does_not_cross_walk_dragonforce_to_scattered_spider_on_symantec_alone: A1
  # ---- IOC LAYER (INHERITED FROM FINDING-0004) ----
  no_new_iocs_in_sw_relay_layer_inherited_from_symantec_primary_in_finding_0004: A1
  # ---- A&D / DIB RELEVANCE LAYER ----
  ad_direct_relevance: A1  # NONE — inherited
  ad_structural_relevance_microsoft_teams_turn_relay_abuse_universal_tenant_pattern: A2  # inherited
  # ---- FIRST-PARTY SPLUNK LAYER (HARD RULE 8 BINDING) ----
  splunk_first_party_check_invoked_30d_lookback: A1
  splunk_first_party_zero_hits_on_external_indicators: A1
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True) inheriting from finding-2026-06-16-
  0004 — substrate-strengthening on publisher-independence layer
  (triple-publisher journalistic relay BC+HNS+SW) does NOT lift the
  cluster anchor because publisher-independence is doctrinally distinct
  from IR-vendor corroboration. Single-vendor-on-novel-TTP veto persists
  (Symantec sole IR-vendor on Backdoor.Turn / Microsoft Teams TURN-relay
  abuse novel TTP).

  No net-new technical detail in SW relay beyond what Symantec primary
  documents in finding-0004. SW relay is publisher-independence
  substrate-strengthening only.

  HARD RULE 2: PRESERVED. Symantec-asserted DragonForce/Scattered-Spider
    linkage preserved verbatim; Scattered-Spider dossier mutation PAUSED
    pending independent second-IR-vendor corroboration; Archimedes does
    NOT cross-walk DragonForce to Scattered-Spider on Symantec alone.
  HARD RULE 6: PRESERVED. SW RSS-summary 14 words at-cap.
  HARD RULE 8: PRESERVED. Splunk first-party 30-day lookback returned
    only archimedes:operation self-telemetry.

source_reliability:
  grade: B
  source_name: "SecurityWeek (Ionut Arghire) trade-press journalistic relay of Symantec Threat Hunter Team primary research carried forward from finding-2026-06-16-0004"
  source_yaml_id: securityweek
  grade_rationale: >
    SecurityWeek is B-grade per source-grades.yaml awaiting_ratification
    list. SW-Arghire trade-press relay is third independent B-grade
    publisher journalistic relay extension of finding-2026-06-16-0004
    substrate (BC primary capture AM, HNS-Markovic PM brief extension,
    this raw-003 SW extension).
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - consistent_with_established_ttps_for_symantec_originated_cluster
    - no_contradicting_evidence_from_a_or_b_grade_sources
    - technical_claims_internally_coherent
  rationale: >
    SW trade-press relay is internally coherent with Symantec primary
    substrate. Microsoft Teams TURN-relay abuse + Go-based backdoor
    (Backdoor.Turn family) inherits finding-0004 credibility 2.
    Single-vendor-on-novel-TTP veto persists (Symantec sole IR-vendor);
    credibility 2 inherited from finding-0004.

corroboration:
  independent_sources:
    - bleepingcomputer  # BC primary capture AM finding-0004
    - helpnetsecurity   # HNS-Markovic PM finding-0004 extension
    - securityweek      # SW-Arghire this raw-003 extension
    - symantec          # Symantec Threat Hunter Team primary
  independent: false
  test_passed: >
    Three trade-press publishers but ONE IR-vendor evidence basis
    (Symantec). Publisher-independence layer satisfied; IR-vendor-
    independence-on-novel-TTP NOT satisfied. The corroboration test for
    credibility 1 on novel-TTP requires DIFFERENT IR-VENDOR EVIDENCE
    BASIS — Mandiant / CrowdStrike / Unit 42 / MSTIC independent
    telemetry would satisfy.
  independent_layered:
    symantec_ir_vendor_primary: false  # single IR-vendor
    bleepingcomputer_publisher_relay: true
    helpnetsecurity_publisher_relay: true
    securityweek_publisher_relay: true

first_party_precedence:
  applied: true
  splunk_evidence:
    query_executed: "search index=archimedes OR index=defenseclaw_local (\"Backdoor.Turn\" OR DragonForce OR \"Teams TURN\") earliest=-30d"
    hits_on_external_indicators: 0
    note: >
      30-day lookback; ZERO external-indicator hits across
      defenseclaw_local + archimedes. Frank's Microsoft Teams tenant
      deployment status not publicly catalogued; visibility-bounded
      absence flagged per Hard Rule 8 binding.

single_source_veto_applied: true
single_source_veto_layers:
  - symantec_alone_on_novel_ttp_backdoor_turn_microsoft_teams_turn_relay_no_independent_ir_vendor_corroboration
  - symantec_alone_on_dragonforce_scattered_spider_linkage_attribution_layer
wep_ceiling: likely
wep_ceiling_per_layer:
  backdoor_turn_family_existence_per_symantec: likely  # unchanged
  microsoft_teams_turn_relay_abuse_novel_ttp_per_symantec: likely  # unchanged
  dragonforce_scattered_spider_linkage_per_symantec: possibly  # contested-attribution

cluster:
  topic: "DragonForce Backdoor.Turn Microsoft Teams TURN-relay abuse — SW-Arghire trade-press relay extends to triple-publisher journalistic relay (BC+HNS+SW); single-vendor-on-novel-TTP veto persists"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-17-am-003-sw-arghire-microsoft-teams-relay-servers-dragonforce-ransomware
  attribution_claims:
    - claimed_actor: DragonForce
      claimed_by_sources: [symantec, bleepingcomputer, helpnetsecurity, securityweek]
      requires_analyst_review: false
      note: "DragonForce attribution preserved per Symantec primary + publisher relays."
    - claimed_actor: Scattered-Spider
      claimed_by_sources: [symantec]
      requires_analyst_review: true
      note: "Symantec-asserted DragonForce/Scattered-Spider linkage. Hard Rule 2 BINDING — Scattered-Spider dossier mutation PAUSED pending independent second-IR-vendor corroboration. Archimedes does NOT cross-walk on Symantec alone."

inclusion:
  eligible_for:
    - daily_brief_monitoring  # B2 monitoring + UPDATE pivot inclusion
    - weekly_synthesis
  not_eligible_for:
    - flash                # anti-noise (same trigger-topic as finding-0004)
    - daily_brief_action   # WEP ceiling unchanged; UPDATE substrate is publisher-independence not IR-vendor corroboration
    - actor_profile_update # single-vendor-on-novel-TTP veto persists; Scattered-Spider dossier mutation PAUSED

analyst_review_required: true
red_team_review_required: false  # WEP ceiling unchanged at "likely"
red_team_review: null

# ============================================================================
# PM UPDATE — SA-Paganini publisher-relay extends to quadruple-publisher
# ============================================================================
pm_update:
  update_id: pm-update-2026-06-17-0005
  updated_at: 2026-06-17T16:00:00-04:00
  grading_run_id: afternoon-20260617-160000
  update_type: substrate_strengthening_publisher_relay_only_non_substrate_shifting_veto_persists
  raw_signal_members_pm:
    - raw-2026-06-17-pm-005-dragonforce-sa-paganini-fullbody
  substrate_changes:
    publisher_cardinality: "BC+HNS+SW triple-publisher (AM) -> BC+HNS+SW+SA quadruple-publisher journalistic relay (PM)"
    net_new_technical_detail: "NONE beyond Symantec primary already documented in finding-2026-06-16-0004 / finding-2026-06-17-0005"
    veto_layer_status:
      single_vendor_on_novel_ttp_veto: "PERSISTS — Symantec sole IR-vendor on Microsoft Teams TURN-relay novel TTP; Mandiant / CrowdStrike / Unit 42 / MSTIC corroboration remains substrate-that-would-lift-veto"
      scattered_spider_dossier_mutation: "REMAINS-PAUSED per Hard Rule 2 BINDING; Symantec-asserted DragonForce <-> Scattered-Spider linkage preserved verbatim; Archimedes does NOT cross-walk on Symantec alone"
    wep_revision:
      backdoor_turn_family_existence_per_symantec: "UNCHANGED at likely"
      microsoft_teams_turn_relay_abuse_novel_ttp: "UNCHANGED at likely (publisher-independence is NOT IR-vendor-corroboration)"
      dragonforce_scattered_spider_linkage: "UNCHANGED at possibly (single-IR-vendor contested-attribution)"
  hard_rules_audit:
    rule_1: "PRESERVED — no credentials, no PII, no ITAR-questionable content"
    rule_2: "PRESERVED — Symantec-asserted Scattered-Spider linkage preserved verbatim; Scattered-Spider dossier mutation PAUSED"
    rule_6: "Symantec block 11-word excerpt at-cap in raw-signal substrate flagged for briefer paraphrase-only handling"
    rule_8: "Splunk first-party check carried from AM; visibility-bounded absence stands"

tlp: CLEAR
published_in_briefs: [2026-06-17-morning, 2026-06-17-afternoon]
retracted: false
retraction_brief_id: null
---

# DragonForce Backdoor.Turn Microsoft Teams TURN-relay UPDATE — triple-publisher relay, single-vendor veto persists

## Summary

SecurityWeek (Ionut Arghire) trade-press journalistic relay extends Symantec DragonForce Backdoor.Turn / Microsoft Teams TURN-relay substrate (finding-2026-06-16-0004) from BC+HNS dual-publisher to BC+HNS+SW triple-publisher journalistic relay. Substrate-strengthening on publisher-independence layer only; single-vendor-on-novel-TTP veto persists (Symantec sole IR-vendor; Mandiant / CrowdStrike / Unit 42 / MSTIC corroboration remains substrate-that-would-lift-veto). No net-new technical detail in SW relay. Scattered-Spider / DragonForce linkage Hard Rule 2 BINDING preserved — Scattered-Spider dossier mutation PAUSED pending independent second-IR-vendor corroboration. WEP unchanged at "likely" on novel-TTP layer.

## Sources

### SecurityWeek (securityweek, B) — Ionut Arghire trade-press relay

- URL: https://www.securityweek.com/microsoft-teams-relay-servers-abused-in-dragonforce-ransomware-attack/
- Published: 2026-06-17 10:38 UTC
- Third independent B-grade publisher journalistic relay of Symantec primary substrate.

### Inherited substrate from finding-2026-06-16-0004

- Symantec Threat Hunter Team primary (Backdoor.Turn family novel TURN-relay TTP, DragonForce ransomware, Scattered-Spider linkage); BC + HNS publisher relays.

## Technical detail

No net-new technical detail in SW relay beyond what Symantec primary documents in finding-0004. SW relay is publisher-independence substrate-strengthening only.

## IOCs surfaced

None new in SW relay. IOCs at Symantec primary documented in finding-2026-06-16-0004 stand.

## Relationship to existing findings

- Substrate-strengthening UPDATE on **finding-2026-06-16-0004** — publisher-independence triple (BC+HNS+SW); single-vendor-on-novel-TTP veto persists.

## Open questions for analyst

- **IR-vendor corroboration watch** — Mandiant / CrowdStrike / Unit 42 / MSTIC independent telemetry on Symantec Backdoor.Turn / Microsoft Teams TURN-relay abuse novel TTP remains substrate-that-would-lift-veto. Any such corroboration would also unblock Scattered-Spider dossier mutation evaluation (currently PAUSED per Hard Rule 2 BINDING).
- **Scattered-Spider linkage** — Symantec sole-source on the linkage claim; Hard Rule 2 prohibits Archimedes from originating cross-walk. Watch for independent IR-vendor confirmation.

## PM UPDATE 2026-06-17 16:00 — SA-Paganini publisher-relay extends to quadruple-publisher

Security Affairs (Pierluigi Paganini) full-body relay published 2026-06-17 15:55 UTC extends the journalistic-relay chain from BC+HNS+SW triple-publisher (AM) to BC+HNS+SW+SA quadruple-publisher. **No net-new technical detail** beyond what Symantec primary documents in finding-2026-06-16-0004 — Backdoor.Turn (Go-based, injected into legitimate DbgView64.exe; Teams TURN-relay anonymous-visitor-token + QUIC C2; BYOVD against Huawei HWAuidoOs2Ec.sys + Palo Alto-impersonating custom driver; Ghost Calls Black Hat 2025 inspiration). SA-Paganini is editorial relay only; substrate-strengthening on publisher-independence layer.

Single-vendor-on-novel-TTP veto **PERSISTS** — Symantec sole IR-vendor on Microsoft Teams TURN-relay abuse novel TTP. Mandiant / CrowdStrike / Unit 42 / MSTIC independent telemetry remains substrate-that-would-lift-veto. Symantec-asserted DragonForce <-> Scattered-Spider linkage preserved verbatim per Hard Rule 2 BINDING — Scattered-Spider dossier mutation **REMAINS-PAUSED** pending independent second-IR-vendor corroboration. WEP unchanged at "likely" on novel-TTP layer.
