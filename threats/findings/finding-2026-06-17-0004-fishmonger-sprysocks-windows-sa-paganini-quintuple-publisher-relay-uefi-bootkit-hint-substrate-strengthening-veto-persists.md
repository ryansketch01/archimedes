---
id: finding-2026-06-17-0004
finding_id: finding-2026-06-17-0004-fishmonger-sprysocks-windows-sa-paganini-quintuple-publisher-relay-uefi-bootkit-hint-substrate-strengthening-veto-persists
title: "Security Affairs (Pierluigi Paganini) editorial relay extends ESET FishMonger SprySOCKS Windows substrate (finding-2026-06-16-0001) from PM-brief BC+THN+DR triple-publisher journalistic relay to BC+THN+DR+SA quadruple-publisher journalistic relay (SA per 06:00 sweep prior cross-reference) + this AM raw-005 SA-Paganini full-body retrieval to quintuple-publisher functional confirmation — substrate-strengthening on publisher-independence layer NOT on IR-vendor-corroboration layer; single-vendor-on-cluster-identity veto persists (Mandiant / CrowdStrike / Unit 42 / MSTIC corroboration of FishMonger==i-Soon-contractor remains substrate-that-would-lift-veto); SA full-body retrieval surfaces UEFI bootkit hint citing potential CVE-2023-24932 (BlackLotus) exploitation as ESET 'limited indications suggesting the possible use' qualifier — novel substrate not in earlier relays; WIN_DRV kernel-driver named RawWNPF + DriverLoader; WIN_PLUS Print Spooler injection via svchost.exe; TCP traffic diversion mechanism; SprySOCKS-Trochilus-RedLeaves codebase lineage with Webworm + SixLittleMonkeys cluster overlap; victim countries Honduras + Taiwan + Thailand + Pakistan 2023-2024 deployment window; WEP unchanged at 'likely' on cluster-identity layer; UEFI-bootkit-hint via CVE-2023-24932 escalates A&D-relevance via persistence-survives-OS-reinstall threat model (novel substrate worth grader attention); ESET hedge language 'limited indications' preserved verbatim per Hard Rule 2"
date: 2026-06-17
created_at: 2026-06-17T08:15:00-04:00
graded_by: grader
grading_run_id: morning-20260617-080000
grading_mode: scheduled_brief
test: false
status: graded

update_pivot_on: finding-2026-06-16-0001
update_type: substrate_strengthening_quintuple_publisher_relay_plus_uefi_bootkit_hint_novel_substrate_layer_veto_persists

# ============================================================================
# Core grading
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- SA-PAGANINI EDITORIAL RELAY LAYER (PUBLISHER-INDEPENDENCE) ----
  sa_paganini_full_body_retrieval_of_eset_primary_substrate: B2
  quintuple_publisher_journalistic_relay_bc_thn_dr_sa: B2  # publisher-independence layer
  publisher_independence_not_ir_vendor_corroboration: A1  # doctrinal distinction
  single_vendor_on_cluster_identity_veto_persists: A1
  # ---- NOVEL SUBSTRATE LAYER (UEFI BOOTKIT HINT VIA CVE-2023-24932) ----
  sa_full_body_surfaces_uefi_bootkit_hint_citing_cve_2023_24932: B2  # SA full-body retrieval; ESET-originated hedge
  eset_hedge_language_limited_indications_suggesting_possible_use_preserved_verbatim: A1
  cve_2023_24932_blacklotus_uefi_bootkit_class_pattern_inheritance: A1
  uefi_bootkit_persistence_survives_os_reinstall_threat_model_escalation: A2
  # ---- NOVEL TECHNICAL DETAIL SUBSTRATE LAYER ----
  win_drv_kernel_driver_named_rawwnpf_driverloader: B2  # SA full-body, ESET-originated
  win_plus_print_spooler_injection_via_svchost: B2
  tcp_traffic_diversion_mechanism: B2
  sprysocks_trochilus_redleaves_codebase_lineage_webworm_sixlittlemonkeys_overlap: B2
  # ---- VICTIM PROFILE LAYER (INHERITED FROM FINDING-0001) ----
  victim_countries_honduras_taiwan_thailand_pakistan_2023_2024: A2  # inherited
  no_ad_prime_named_victim: A1  # inherited
  # ---- ATTRIBUTION-DISCIPLINE LAYER (HARD RULE 2 BINDING) ----
  fishmonger_cluster_identity_preserved_verbatim: A1
  archimedes_does_not_cross_walk_to_apt41_winnti_umbrella: A1
  eset_i_soon_contractor_assertion_preserved_per_eset: A1
  # ---- IOC LAYER (INHERITED FROM FINDING-0001) ----
  no_new_iocs_in_sa_relay_layer_inherited_from_eset_primary_in_finding_0001: A1
  # ---- A&D / DIB RELEVANCE LAYER ----
  ad_direct_relevance: A1  # NONE — inherited
  ad_structural_relevance_initial_access_pivot_inheritance_fortinet_gitlab_exchange_telerik_zimbra: A2  # inherited HIGH
  ad_structural_relevance_uefi_bootkit_threat_model_novel_escalation_via_sa_substrate: A2  # net-new this finding
  # ---- FIRST-PARTY SPLUNK LAYER (HARD RULE 8 BINDING) ----
  splunk_first_party_check_invoked_30d_lookback: A1
  splunk_first_party_zero_hits_on_external_indicators: A1
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True) inheriting from finding-2026-06-16-
  0001 (B2 cluster anchor) — substrate-strengthening on publisher-
  independence layer (BC+THN+DR+SA now quintuple-publisher journalistic
  relay) does NOT lift the cluster anchor because publisher-independence
  is doctrinally distinct from IR-vendor corroboration. Single-vendor-on-
  cluster-identity veto persists — Mandiant / CrowdStrike / Unit 42 /
  MSTIC independent IR-vendor corroboration remains substrate-that-would-
  lift-veto.

  Net-new substrate this UPDATE: UEFI-bootkit-hint via CVE-2023-24932
  (BlackLotus) exploitation surfaced via SA full-body retrieval. ESET's
  hedge language "limited indications suggesting the possible use" is
  preserved verbatim per Hard Rule 2 — Archimedes does NOT originate the
  UEFI-bootkit confirmation, only records ESET's hedged characterization.
  A&D-relevance escalation via persistence-survives-OS-reinstall threat
  model is novel substrate layer that warrants Defender-tenant /
  endpoint-defense / firmware-attestation operational alignment in A&D-
  prime endpoint security posture.

  T1 GATE: SATISFIED for monitoring-tier inclusion. WEP ceiling unchanged
  at "likely" on cluster-identity layer per single-vendor-veto persistence.

  HARD RULE 2: PRESERVED. FishMonger cluster identity verbatim; no cross-
    walk to APT41 / Winnti umbrella originated by Archimedes; ESET-
    asserted i-Soon contractor attribution preserved per ESET. ESET hedge
    on UEFI bootkit preserved verbatim.
  HARD RULE 6: PRESERVED. SA full-body summarization paraphrased; ESET
    hedge quote 7 words at-cap "limited indications suggesting the
    possible use".
  HARD RULE 8: PRESERVED. Splunk first-party 30-day lookback for
    "FishMonger" returned only archimedes:operation self-telemetry;
    silent-Splunk-does-NOT-disconfirm.

source_reliability:
  grade: B
  source_name: "Security Affairs (Pierluigi Paganini) editorial relay full-body retrieval of ESET WeLiveSecurity (Martin Smolar) primary research carried forward from finding-2026-06-16-0001"
  source_yaml_id: securityaffairs
  grade_rationale: >
    Security Affairs is B-grade per source-grades.yaml awaiting_ratification
    list. SA-Paganini editorial relay is fifth publisher journalistic
    relay extension of finding-2026-06-16-0001 substrate (BC+THN+DR base
    + SA prior cross-reference + this raw-005 full-body retrieval).
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - consistent_with_established_ttps_for_eset_originated_cluster
    - no_contradicting_evidence_from_a_or_b_grade_sources
    - technical_claims_internally_coherent_uefi_bootkit_hint_kernel_driver_print_spooler
  rationale: >
    SA editorial relay is internally coherent with ESET primary substrate.
    UEFI bootkit hint citing CVE-2023-24932 BlackLotus is a documented
    technical pathway (BlackLotus emerged 2023). WIN_DRV + WIN_PLUS
    technical details consistent with SprySOCKS codebase lineage
    documented elsewhere. Single-vendor-on-cluster-identity veto persists
    (ESET sole IR-vendor); credibility 2 inherited from finding-0001.

corroboration:
  independent_sources:
    - bleepingcomputer       # BC-Toulas AM finding-0001
    - thehackernews          # THN-Lakshmanan AM finding-0001
    - dark-reading           # DR-Wright PM finding-0001 editorial relay
    - securityaffairs        # SA-Paganini this raw-005 full-body retrieval
    - eset-wls               # ESET WeLiveSecurity Martin Smolar primary
  independent: false
  test_passed: >
    Five publishers but ONE IR-vendor evidence basis (ESET WeLiveSecurity).
    Publisher-independence layer satisfied (different publishing orgs,
    none cite each other as primary) BUT IR-vendor-independence-on-cluster-
    identity NOT satisfied. The corroboration test for credibility 1 on
    cluster-identity requires DIFFERENT IR-VENDOR EVIDENCE BASIS —
    Mandiant / CrowdStrike / Unit 42 / MSTIC independent telemetry would
    satisfy. Single-source-veto on cluster-identity layer persists.
  independent_layered:
    eset_wls_ir_vendor_primary: false  # single IR-vendor on cluster-identity layer
    bleepingcomputer_publisher_relay: true
    thehackernews_publisher_relay: true
    dark_reading_publisher_relay: true
    securityaffairs_publisher_relay: true

first_party_precedence:
  applied: true
  splunk_evidence:
    query_executed: "search index=archimedes OR index=defenseclaw_local FishMonger earliest=-30d"
    hits_on_external_indicators: 0
    note: >
      30-day lookback; ZERO external-indicator hits. Frank not known to
      operate in named victim sectors (Honduras / Taiwan / Thailand /
      Pakistan government foreign-affairs / tech / telco); visibility-
      bounded absence flagged per Hard Rule 8 binding.

single_source_veto_applied: true
single_source_veto_layers:
  - eset_wls_alone_on_cluster_identity_layer_no_independent_ir_vendor_corroboration
  - eset_wls_alone_on_uefi_bootkit_hint_substrate_layer
wep_ceiling: likely
wep_ceiling_per_layer:
  fishmonger_cluster_identity_attribution_per_eset: likely  # unchanged
  win_drv_win_plus_technical_substrate_per_eset: likely     # unchanged
  uefi_bootkit_hint_cve_2023_24932_use_per_eset_hedge: possibly  # ESET explicit hedge
  initial_access_pivot_inheritance_pattern: likely          # operational-template

cluster:
  topic: "FishMonger SprySOCKS Windows — SA-Paganini editorial relay extends to quintuple-publisher journalistic relay; UEFI bootkit hint via CVE-2023-24932 (BlackLotus) surfaces as novel substrate layer per ESET hedge; single-vendor-on-cluster-identity veto persists"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-17-am-005-sa-paganini-fishmonger-sprysocks-windows-fifth-publisher-relay
  attribution_claims:
    - claimed_actor: FishMonger
      claimed_by_sources: [eset-wls]
      requires_analyst_review: true
      note: "ESET-asserted cluster identity preserved verbatim. NOT on 24-actor _roster.yaml. /new-actor-FishMonger candidacy operator-deferred per Hard Rule 5. Cross-walk to Earth Lusca / Aquatic Panda / Charcoal Typhoon / RedHotel / i-Soon contractor preserved per ESET."

inclusion:
  eligible_for:
    - daily_brief_monitoring  # B2 monitoring + UPDATE pivot inclusion
    - weekly_synthesis
  not_eligible_for:
    - flash                # anti-noise (same trigger-topic as finding-0001)
    - daily_brief_action   # WEP ceiling unchanged; UPDATE substrate is publisher-independence not IR-vendor corroboration
    - actor_profile_update # single-vendor-on-cluster-identity veto persists
    - vuln_tracker_update  # CVE-2023-24932 BlackLotus hint is ESET-hedged; not action-tier substrate

analyst_review_required: true
red_team_review_required: false  # WEP ceiling unchanged at "likely"
red_team_review: null

tlp: CLEAR
published_in_briefs: [2026-06-17-morning]
retracted: false
retraction_brief_id: null
---

# FishMonger SprySOCKS Windows UPDATE — quintuple-publisher journalistic relay, UEFI bootkit hint via CVE-2023-24932 (BlackLotus) novel substrate via ESET hedge

## Summary

Security Affairs (Pierluigi Paganini) editorial relay full-body retrieval extends finding-2026-06-16-0001 (ESET FishMonger SprySOCKS Windows) to quintuple-publisher journalistic relay (BC + THN + DR + SA prior cross-reference + this AM SA full-body). Substrate-strengthening on publisher-independence layer only; single-vendor-on-cluster-identity veto persists (Mandiant / CrowdStrike / Unit 42 / MSTIC IR-vendor corroboration remains substrate-that-would-lift-veto). Net-new substrate via SA full-body: UEFI bootkit hint citing potential CVE-2023-24932 (BlackLotus) exploitation, surfaced as ESET hedge "limited indications suggesting the possible use" preserved verbatim. Additional technical detail layer: WIN_DRV kernel driver named RawWNPF + DriverLoader; WIN_PLUS Print Spooler injection via svchost.exe; TCP traffic diversion mechanism; SprySOCKS-Trochilus-RedLeaves codebase lineage with Webworm + SixLittleMonkeys cluster overlap. WEP unchanged at "likely" on cluster-identity layer.

## Sources

### Security Affairs (securityaffairs, B) — Pierluigi Paganini editorial relay

- URL: https://securityaffairs.com/193728/apt/china-linked-fishmonger-ports-sprysocks-to-windows-with-kernel-level-stealth-and-uefi-bootkit-hints.html
- Published: 2026-06-17 08:10 UTC
- Editorial relay of ESET WeLiveSecurity (Martin Smolar) primary; full-body summarization ~700 words; surfaces UEFI bootkit hint + technical kernel-driver detail not in earlier relays.

### Inherited substrate from finding-2026-06-16-0001

- ESET WeLiveSecurity (Martin Smolar) primary; BC (Toulas), THN (Lakshmanan), DR (Wright) publisher relays.

## Technical detail

UEFI bootkit hint substrate is the operationally-significant net-new layer this UPDATE. ESET's hedge language "limited indications suggesting the possible use" of CVE-2023-24932 (BlackLotus class Secure Boot bypass) is preserved verbatim per Hard Rule 2 — Archimedes does NOT confirm UEFI bootkit use, only records ESET's hedged characterization. If substantiated, the threat model escalates to persistence-survives-OS-reinstall, with Defender-tenant + firmware-attestation + Secure Boot policy enforcement as the primary defensive substrate for A&D-prime endpoint security.

WIN_DRV kernel driver components named RawWNPF + DriverLoader; WIN_PLUS uses Print Spooler injection via svchost.exe; TCP traffic diversion mechanism for C2; SprySOCKS codebase lineage traces to Trochilus + RedLeaves with Webworm + SixLittleMonkeys cluster overlap per ESET research. Victim countries (Honduras + Taiwan + Thailand + Pakistan, 2023-2024 deployment window) inherited from finding-2026-06-16-0001 unchanged.

## IOCs surfaced

None new in SA relay. IOCs at ESET primary documented in finding-2026-06-16-0001 stand.

## Relationship to existing findings

- Substrate-strengthening UPDATE on **finding-2026-06-16-0001** — publisher-independence quintupled (BC+THN+DR+SA, with SA primary capture this raw-005); single-vendor-on-cluster-identity veto persists.
- Operationally adjacent to BlackLotus-class UEFI bootkit threat model (CVE-2023-24932) — if ESET hedge substantiates, escalates to persistence-survives-OS-reinstall posture concern.

## Open questions for analyst

- **IR-vendor corroboration watch** — Mandiant / CrowdStrike / Unit 42 / MSTIC independent telemetry on FishMonger==i-Soon-contractor cluster identity remains substrate-that-would-lift-single-vendor-veto. Any of those vendors publishing corroborating substrate within 24-72h would warrant cluster anchor lift from B2 to A2.
- **UEFI bootkit hint follow-up** — ESET hedge "limited indications" warrants direct review of ESET WeLiveSecurity full publication for any technical evidence beyond the hedge. If ESET publishes signature samples or firmware artifacts substantiating CVE-2023-24932 exploitation, escalate threat-model assessment.
- **/new-actor-FishMonger candidacy** — operator-deferred per Hard Rule 5; substrate-strengthening on publisher-independence does not by itself satisfy roster mutation threshold.
