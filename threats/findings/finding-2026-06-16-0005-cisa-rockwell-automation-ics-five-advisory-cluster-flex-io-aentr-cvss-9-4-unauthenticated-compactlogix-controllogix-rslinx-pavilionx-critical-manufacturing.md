---
id: finding-2026-06-16-0005
finding_id: finding-2026-06-16-0005-cisa-rockwell-automation-ics-five-advisory-cluster-flex-io-aentr-cvss-9-4-unauthenticated-compactlogix-controllogix-rslinx-pavilionx-critical-manufacturing
title: "CISA ICS-CERT issues five-advisory Rockwell Automation cluster (ICSA-26-167-01 through -05) covering FactoryTalk Analytics PavilionX (CVE-2025-14272 missing-auth CVSS 7.0), RSLinx Classic (CVE-2020-13573 stack-overflow CVSS 7.5 vintage), Logix 5370/5570 controllers (CVE-2026-11317 CIP DoS CVSS 7.5), CompactLogix 5370 L1/L2/L3 (CVE-2025-11694 CIP DoS + sequence-validation CVSS 7.5), and FLEX I/O EtherNet/IP adapters 1794-AENTR/1794-AENTRXT (CVE-2026-0646 memory-handling + CVE-2026-0647 missing-authentication CVSS 9.4 unauthenticated as the headline entry); no active exploitation cited; no actor attribution; no CISA KEV listing for any of the six CVEs at sweep time; vendor-PSIRT-cross-walked-via-CISA-ICS-channel cluster anchor; Critical Manufacturing sector deployment baseline worldwide with high operational-template inheritance into DIB Tier-1/2 supplier manufacturing-floor and supplier-network industrial bases; A&D-prime direct relevance NONE (no named victim), A&D operational-template relevance HIGH on FLEX I/O 9.4 unauthenticated entry"
date: 2026-06-16
created_at: 2026-06-16T16:00:00-04:00
graded_by: grader
grading_run_id: afternoon-20260616-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: A2
admiralty_grade: A2
digraph_layered:
  cisa_ics_cert_a_grade_government_primary_per_source_grades_yaml: A1
  five_advisory_cluster_icsa_26_167_01_through_05_dated_2026_06_16: A1
  vendor_rockwell_automation_psirt_cross_walked_into_cisa_ics_channel_standard_pattern: A1
  flex_io_aentr_aentrxt_cve_2026_0646_cvss_9_4_missing_release_memory_after_effective_lifetime: A2
  flex_io_aentr_aentrxt_cve_2026_0647_cvss_9_4_missing_authentication_critical_function: A2
  flex_io_9_4_unauthenticated_cluster_headline_entry: A2
  factorytalk_analytics_pavilionx_cve_2025_14272_cvss_7_0_missing_authorization_api_endpoints: A2
  rslinx_classic_cve_2020_13573_cvss_7_5_third_party_vintage_oob_read_stack_buffer_overflow: A2
  logix_5370_5570_cve_2026_11317_cvss_7_5_improper_resource_shutdown_release_mnrf: A2
  compactlogix_5370_l1_l2_l3_cve_2025_11694_cvss_7_5_cip_sequence_validation_connection_id_exposure: A2
  critical_manufacturing_sector_deployment_baseline_worldwide: A1
  rslinx_classic_additionally_critical_infrastructure_energy_food_agriculture_water_wastewater: A1
  no_active_exploitation_cited_in_any_of_the_five_advisories: A1
  no_actor_attribution_claims_to_preserve_hard_rule_2_not_triggered: A1
  no_cisa_kev_listing_for_any_of_the_six_cves_at_sweep_time: A1
  patches_available_per_vendor_advisories_cross_walked_through_cisa_ics_channel: A2
  ad_direct_relevance_none_no_ad_prime_named_victim: A1
  ad_operational_template_inheritance_high_compactlogix_controllogix_guardlogix_widely_deployed_dib_tier_1_2_manufacturing_floors: A2
  ad_operational_template_inheritance_high_flex_io_distributed_io_ethernet_ip_fieldbus_common_dib_tier_1_2_supplier_manufacturing: A2
  ad_operational_template_inheritance_moderate_rslinx_classic_legacy_communications_driver_persistent_in_industrial_estates: A2
  ad_operational_template_inheritance_moderate_factorytalk_analytics_pavilionx_inherited_in_ot_it_converged_estates: A2
  splunk_first_party_check_invoked_30d_lookback: A1
  splunk_first_party_zero_hits_on_rockwell_product_indicators_or_cve_indicators: A1
  frank_not_critical_manufacturing_rockwell_ics_deployment_visibility_bounded_absence: A1
  not_under_existing_anti_noise_hold: A1
  cluster_anchor: A2

digraph_anchor: >
  Cluster anchored at A2 (Probably True / action-tier inclusion eligible).
  CISA Advisories is A-grade per source-grades.yaml id `cisa-advisories`
  (Official U.S. gov, technically verified before publication). Five
  advisories in cluster, all dated 2026-06-16, all A1 government primary
  on the procedural-fact layer (CVE assignments, CVSS scores, affected
  product versions, CWE classifications, critical-infrastructure-sector
  deployment baseline).

  WHY A2 NOT A1:
    1. NO INDEPENDENT IR-VENDOR CORROBORATION on active-exploitation
       layer (because there is no active-exploitation claim to
       corroborate — these are vendor-discovered vulnerabilities cross-
       walked through CISA ICS, not active campaign reports).
    2. CISA ICS advisories are vendor-PSIRT-derived — Rockwell
       Automation PSIRT advisories cross-walked into the CISA ICS-CERT
       channel per standard CISA ICS pattern. The CVE-record layer is
       A1; the broader contextual analysis (operational-template
       inheritance, A&D Tier-1/2 supplier exposure pattern) is A2
       analyst-grade synthesis grounded in CISA advisory text.
    3. CVE-2020-13573 (RSLinx Classic) is a 2020 third-party
       vulnerability newly cross-walked into the CISA ICS channel via
       Rockwell advisory — vintage CVE with broader sector applicability
       (Critical Manufacturing + Energy + Food and Agriculture + Water
       and Wastewater) noted by CISA.

  Single-source-veto consideration: CISA is the SOLE source on this
  cluster anchor (vendor-PSIRT-derived through the CISA ICS channel).
  Single-source veto applies on WEP claims, but the WEP layer here is
  thin — these are vulnerability advisories with patches, not campaign
  claims requiring forward predictive assessment. WEP capped at "likely"
  on operational-template-inheritance-applicability assessment; the
  A1 procedural-fact layer (CVE-assignment, CVSS, vendor-PSIRT-
  confirmed-on-own-product) does NOT require WEP at all.

  WHY NOT FLASH:
    - T1 (CVSS-10-active-exploitation): FAIL. CVSS top at 9.4; no
      active exploitation cited; no CISA KEV listing at sweep time.
    - T2 (tracked-actor-attribution): FAIL. No actor attribution.
    - T3 (first-party-splunk-hit): FAIL. Splunk zero hits; Frank is
      NOT a Critical Manufacturing Rockwell ICS deployment.
    - T4 (tracked-actor-ttp-change): FAIL. No actor.
    - T5 (multi-victim-campaign): FAIL. No campaign — vulnerability
      cluster only.
    - T6 (vendor-zero-day-without-patch): FAIL. Patches available
      per vendor advisories.
    - Critical-override 0-of-4 conditions met.

  HARD RULE 2: NOT TRIGGERED — no actor attribution claims to preserve.

  HARD RULE 5: NOT TRIGGERED — no actor scoring proposal; no roster
  mutation; no threat-box score in flight. Vuln-tracker handoff
  operator-deferred per standard pathway (six distinct CVE dossier
  scaffolds OR cluster-dossier decision recommended).

  HARD RULE 6: PRESERVED. CISA advisory text quotes preserved verbatim
  under 15-word cap (one quote per advisory used where needed).

  HARD RULE 8: PRESERVED. Splunk first-party check 30-day lookback;
  ZERO hits across defenseclaw_local + archimedes on Rockwell /
  RSLinx / FactoryTalk / CompactLogix / ControlLogix / GuardLogix /
  FLEX / 1794-AENTR / PavilionX / CVE-2026-11317 / CVE-2026-0646 /
  CVE-2026-0647 / CVE-2025-14272 / CVE-2025-11694 / CVE-2020-13573.
  Frank is NOT a Critical Manufacturing Rockwell ICS deployment —
  visibility-bounded absence flagged; silent-Splunk-does-NOT-disconfirm.

source_reliability:
  grade: A
  source_name: "CISA Cybersecurity & Infrastructure Security Agency (ICS Advisories) — five-advisory Rockwell Automation cluster"
  source_yaml_id: cisa-advisories
  grade_rationale: >
    CISA Advisories is A-grade per source-grades.yaml id `cisa-advisories`
    (Official U.S. gov, technically verified before publication). ICS-CERT
    channel cross-walks vendor-PSIRT advisories with CISA's technical
    review layer. Cluster published 2026-06-16T12:00:00+00:00 (08:00 EDT)
    inside the 07:30→15:30 EDT pre-brief window. All five advisories share
    publication date and Rockwell Automation vendor; CISA cross-walk
    pattern is standard.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - consistent_with_established_ics_vulnerability_disclosure_pattern
    - no_contradicting_evidence_from_a_or_b_grade_sources
    - technical_claims_internally_coherent_cve_records_cvss_scores_cwe_classifications_affected_product_versions
  rationale: >
    Technical claims internally coherent: six distinct CVEs with
    explicit CVSS v3 scores, CWE classifications, affected product
    versions (down to specific firmware revisions), and critical-
    infrastructure-sector deployment baselines. CISA ICS-CERT
    methodology consistent with prior Rockwell PSIRT cross-walks
    (long-running pattern). No contradicting A/B-grade source. Patches
    available per vendor advisories — vendor confirmation on own product
    is A2 baseline at minimum; A1 with independent customer-deployment
    confirmation, but customer-deployment data not in CISA advisory.
    Single-vendor (Rockwell on own product) attestation routed through
    A-grade government channel — single-source veto applies on the WEP
    layer (operational-template-inheritance assessment) but does NOT
    bind on the procedural-fact layer (CVE record, CVSS, CWE, affected
    versions, patches) which is A1.

corroboration:
  independent_sources:
    - cisa-advisories
  independent: false
  test_passed: >
    Single source (CISA ICS-CERT channel) sourced from vendor PSIRT
    (Rockwell Automation). No second IR-vendor or independent customer
    deployment data corroborates the vulnerabilities at this sweep —
    this is the standard pattern for newly-disclosed vendor-PSIRT-cross-
    walked ICS advisories pre-CISA-KEV-listing. Procedural-fact layer
    (CVE assignment, CVSS, CWE, affected versions) is A1 government
    primary not requiring corroboration. Operational-template-inheritance
    assessment layer (A&D Tier-1/2 supplier exposure pattern) is
    analyst synthesis grounded in CISA's critical-infrastructure-sector
    deployment baseline — single-source veto applies there at "likely"
    WEP ceiling.
  independent_layered:
    cisa_government_primary: true
    rockwell_psirt_vendor_on_own_product: true_via_cisa_cross_walk
    independent_ir_vendor_corroboration: false
    independent_customer_deployment_data: false

first_party_precedence:
  applied: true
  splunk_evidence:
    query_executed: "search index=archimedes OR index=defenseclaw_local (Rockwell OR RSLinx OR FactoryTalk OR CompactLogix OR ControlLogix OR GuardLogix OR FLEX OR \"1794-AENTR\" OR PavilionX OR \"CVE-2026-11317\" OR \"CVE-2026-0646\" OR \"CVE-2026-0647\" OR \"CVE-2025-14272\" OR \"CVE-2025-11694\" OR \"CVE-2020-13573\") NOT sourcetype IN (archimedes:operation, archimedes:scheduler) earliest=-30d"
    hits_on_external_indicators: 0
    note: >
      30-day lookback. ZERO hits on Rockwell / RSLinx / FactoryTalk /
      CompactLogix / ControlLogix / GuardLogix / FLEX / 1794-AENTR /
      PavilionX product names or any of the six CVE identifiers across
      defenseclaw_local + archimedes. Frank is NOT a Critical
      Manufacturing Rockwell ICS deployment (no programmable automation
      controllers, no industrial fieldbus infrastructure, no factory-
      automation MES integration visible to Archimedes sentinel).
      Visibility-bounded absence flagged per Hard Rule 8 binding —
      silent-Splunk-does-NOT-disconfirm. CISA primary attestation stands.

single_source_veto_applied: true
single_source_veto_layers:
  - cisa_sole_publisher_on_cluster_anchor_no_independent_ir_vendor_corroboration_no_independent_customer_deployment_data
  - operational_template_inheritance_assessment_layer_analyst_synthesis_grounded_in_cisa_advisory_text_no_independent_dib_tier_1_2_supplier_telemetry_corroboration
wep_ceiling: likely
wep_layer_breakdown:
  cve_assignment_cvss_cwe_affected_versions_procedural_fact_layer: very_likely_to_almost_certainly  # A1 government primary; vendor on own product
  patches_available_layer: very_likely  # vendor-confirmed-on-own-product
  ad_operational_template_inheritance_layer: likely  # single-source veto applies — analyst synthesis from CISA critical-infrastructure-sector baseline
  active_exploitation_layer: not_asserted_no_wep_required  # no active exploitation cited

cluster:
  topic: "CISA ICS-CERT 2026-06-16 five-advisory Rockwell Automation cluster (ICSA-26-167-01 through -05) — six CVEs across FactoryTalk Analytics PavilionX, RSLinx Classic, Logix 5370/5570 controllers, CompactLogix 5370 L1/L2/L3, FLEX I/O EtherNet/IP adapters; FLEX I/O 9.4 unauthenticated is cluster headline; no active exploitation; no actor; no CISA KEV listing at sweep time; Critical Manufacturing deployment baseline worldwide"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-16-pm-002-cisa-rockwell-ics-five-advisory-cluster-critical-manufacturing
  attribution_claims: []  # no actor attribution — vulnerability cluster only
  cve_inventory:
    - cve: CVE-2026-0646
      cvss_v3: 9.4
      cwe: "CWE-401 Missing Release of Memory after Effective Lifetime"
      product: "Rockwell FLEX I/O EtherNet/IP Adapters 1794-AENTR V2.012 / 1794-AENTRXT V2.012"
      advisory: ICSA-26-167-05
      kev_listed: false
      impact_summary: "Improper memory handling of CIP protocol requests; adapter fault and loss of connection to associated I/O. PAIRED with CVE-2026-0647 missing-authentication on the same product cluster. Headline 9.4-unauthenticated entry."
    - cve: CVE-2026-0647
      cvss_v3: 9.4
      cwe: "CWE-306 Missing Authentication for Critical Function"
      product: "Rockwell FLEX I/O EtherNet/IP Adapters 1794-AENTR V2.012 / 1794-AENTRXT V2.012"
      advisory: ICSA-26-167-05
      kev_listed: false
      impact_summary: "Missing authentication on critical function — unauthorized access, account takeover, loss of availability."
    - cve: CVE-2026-11317
      cvss_v3: 7.5
      cwe: "CWE-404 Improper Resource Shutdown or Release"
      product: "Rockwell CompactLogix 5370 ≤ 34.016, Compact GuardLogix 5370 ≤ 35.015, ControlLogix 5570 ≤ 35.015, GuardLogix 5570 36.012"
      advisory: ICSA-26-167-03
      kev_listed: false
      impact_summary: "DoS condition that may result in major nonrecoverable fault (MNRF) on the affected controllers."
    - cve: CVE-2025-11694
      cvss_v3: 7.5
      cwe: "CWE-354 Improper Validation of Integrity Check Value + CWE-497 Exposure of Sensitive System Information"
      product: "Rockwell CompactLogix 5370 L1, L2, L3"
      advisory: ICSA-26-167-04
      kev_listed: false
      impact_summary: "DoS via missing validation of sequence numbers and source IP addresses in the CIP protocol; abuse of exposed Connection IDs visible on web interface."
    - cve: CVE-2025-14272
      cvss_v3: 7.0
      cwe: "CWE-862 Missing Authorization"
      product: "Rockwell FactoryTalk Analytics PavilionX < 7.01"
      advisory: ICSA-26-167-01
      kev_listed: false
      impact_summary: "Improper authorization enforcement in API endpoints; unauthorized actor can execute privileged operations including user/role management and other administrative actions."
    - cve: CVE-2020-13573
      cvss_v3: 7.5
      cwe: "CWE-125 Out-of-bounds Read (stack-based buffer overflow per CISA summary)"
      product: "Rockwell RSLinx Classic ≤ 4.50.00"
      advisory: ICSA-26-167-02
      kev_listed: false
      vintage: true
      impact_summary: "Stack-based buffer overflow allowing remote arbitrary code execution; denial-of-service unresponsive state without self-recovery. THIRD-PARTY VINTAGE CVE (2020) newly cross-walked into CISA ICS channel via Rockwell advisory. Broader critical-infrastructure-sector applicability: Critical Manufacturing + Energy + Food and Agriculture + Water and Wastewater."

inclusion:
  eligible_for:
    - daily_brief_other_signal       # A&D ICS one-liner with FLEX I/O 9.4 unauthenticated headline
    - weekly_synthesis
  not_eligible_for:
    - flash                          # no T1-T6 triggers fire; critical-override 0-of-4
    - actor_profile_update           # no actor
    - daily_brief_action             # action-tier inclusion eligible per A2 grade, but operational-template only — briefer may surface as Other Signal one-liner or as standalone A&D ICS surface notification at briefer discretion

analyst_review_required: false       # no attribution claim; no WEP claim requiring ACH/KAC; vulnerability cluster only
analyst_review_status: not_required
red_team_review_required: false      # WEP ceiling "likely" — below "very likely" red-team threshold

operator_deferred_handoffs:
  vuln_tracker_handoff:
    pathway: "vuln-tracker scaffolds six CVE dossiers OR one cluster dossier"
    cves_in_scope:
      - CVE-2026-0646
      - CVE-2026-0647
      - CVE-2026-11317
      - CVE-2025-11694
      - CVE-2025-14272
      - CVE-2020-13573
    decision_required: "operator decides individual CVE dossier vs cluster dossier path"
    substrate_ready: true
    hard_rule_5_binding: not_triggered_no_actor_scoring  # vuln-tracker handoff does not gate on Hard Rule 5
    priority_cve_within_cluster: "CVE-2026-0646 + CVE-2026-0647 paired FLEX I/O 9.4 unauthenticated — highest CVSS, highest A&D Tier-1/2 supplier operational-template-inheritance relevance"
    cisa_kev_pathway: "none of the six CVEs are KEV-listed at sweep time; vendor-PSIRT-derived advisory cluster; KEV listing pathway possible if active exploitation surfaces but not predicted at this sweep"
  new_actor_candidacy: null            # no actor
  new_vulnerability_dossier: same_as_vuln_tracker_handoff_above

ad_relevance_assessment:
  direct_named_victim: none
  structural_operational_template_inheritance: high
  affected_products_widely_deployed_in_dib_tier_1_2_supplier_manufacturing:
    - CompactLogix / ControlLogix / GuardLogix programmable automation controllers — widely deployed in A&D-prime manufacturing floors, factory automation, supplier networks (Tier-1/2 industrial subcontractors), build-line MES integration
    - RSLinx Classic — communications driver historically bundled with Rockwell PAC deployments; legacy installations persist in industrial estates
    - FactoryTalk Analytics PavilionX — analytics platform commonly inherited in A&D manufacturing OT/IT-converged estates
    - FLEX I/O EtherNet/IP Adapters (1794-AENTR / 1794-AENTRXT) — distributed I/O on EtherNet/IP fieldbus, common in DIB Tier-1/2 supplier manufacturing
  headline_entry: "CVE-2026-0646 + CVE-2026-0647 paired FLEX I/O 9.4 unauthenticated — most operationally-relevant for DIB Tier-1/2 supplier defenders to track now"

tlp: CLEAR
published_in_briefs:
  - 2026-06-16-afternoon
retracted: false
retraction_brief_id: null
---

# CISA ICS-CERT five-advisory Rockwell Automation cluster — FLEX I/O 9.4 unauthenticated headline, no active exploitation, no actor

## Summary

CISA ICS-CERT issued a five-advisory cluster on Rockwell Automation industrial control products on 2026-06-16 (ICSA-26-167-01 through -05), covering six CVEs across five product families. The headline entry is CVE-2026-0646 + CVE-2026-0647, a paired vulnerability on FLEX I/O EtherNet/IP adapters (1794-AENTR, 1794-AENTRXT) at CVSS 9.4 — missing-memory-release plus missing-authentication on the same product cluster. The remaining four advisories cover FactoryTalk Analytics PavilionX (missing-authorization API endpoints, CVE-2025-14272), RSLinx Classic (third-party vintage stack-overflow CVE-2020-13573), Logix 5370/5570 controllers (CIP DoS CVE-2026-11317), and CompactLogix 5370 L1/L2/L3 (CIP sequence-validation + Connection-ID exposure CVE-2025-11694).

No active exploitation is cited in any advisory. No actor attribution. No CISA KEV listing for any of the six CVEs at sweep time. Patches available per Rockwell advisories cross-walked through the CISA ICS-CERT channel.

A&D-prime direct relevance is none — no named victim. A&D operational-template inheritance is high, particularly on the FLEX I/O 9.4 unauthenticated entry. Rockwell programmable automation controllers, RSLinx, FactoryTalk PavilionX, and FLEX I/O fieldbus adapters are widely deployed across DIB Tier-1/2 supplier manufacturing-floor and supplier-network industrial bases.

## Sources

### CISA Cybersecurity & Infrastructure Security Agency (cisa-advisories, digraph: A)

- URL: https://www.cisa.gov/cybersecurity-advisories/all.xml
- Published: 2026-06-16T12:00:00+00:00 (08:00 EDT, inside pre-brief window)
- Five advisories: ICSA-26-167-01 / 02 / 03 / 04 / 05
- Key claim: Six CVEs disclosed across five Rockwell Automation product families; FLEX I/O EtherNet/IP adapter pair at CVSS 9.4 is the cluster headline; no active exploitation cited; patches available

## Technical detail

### Advisory 1 — FactoryTalk Analytics PavilionX (ICSA-26-167-01)

- CVE: CVE-2025-14272 / CVSS v3: 7.0 / CWE-862 Missing Authorization
- Affected: FactoryTalk Analytics PavilionX < 7.01
- Critical infrastructure sector: Critical Manufacturing; Worldwide deployment
- Impact: "improper authorization enforcement in API endpoints" — unauthorized actor can execute privileged operations including user/role management and other administrative actions [13-word at-limit quote preserved verbatim per Hard Rule 6]

### Advisory 2 — RSLinx Classic (ICSA-26-167-02)

- CVE: CVE-2020-13573 (third-party vintage) / CVSS v3: 7.5 / CWE-125 Out-of-bounds Read (stack-based buffer overflow per CISA summary)
- Affected: RSLinx Classic ≤ 4.50.00
- Critical infrastructure sectors: Critical Manufacturing, Energy, Food and Agriculture, Water and Wastewater
- Impact: Stack-based buffer overflow allowing remote arbitrary code execution; denial-of-service unresponsive state without self-recovery

### Advisory 3 — Logix 5370 & 5570 Controllers (ICSA-26-167-03)

- CVE: CVE-2026-11317 / CVSS v3: 7.5 / CWE-404 Improper Resource Shutdown or Release
- Affected: CompactLogix 5370 ≤ 34.016, Compact GuardLogix 5370 ≤ 35.015, ControlLogix 5570 ≤ 35.015, GuardLogix 5570 36.012
- Critical infrastructure sector: Critical Manufacturing
- Impact: Denial-of-service that may result in a major nonrecoverable fault (MNRF)

### Advisory 4 — CompactLogix 5370 L1/L2/L3 (ICSA-26-167-04)

- CVE: CVE-2025-11694 / CVSS v3: 7.5 / CWE-354 Improper Validation of Integrity Check Value + CWE-497 Exposure of Sensitive System Information
- Affected: CompactLogix 5370 L1, L2, L3
- Critical infrastructure sector: Critical Manufacturing
- Impact: DoS via missing validation of sequence numbers and source IP addresses in the CIP protocol; abuse of exposed Connection IDs visible on web interface

### Advisory 5 — FLEX I/O EtherNet/IP Adapters (ICSA-26-167-05) — HIGHEST CVSS IN CLUSTER

- CVEs: CVE-2026-0646 + CVE-2026-0647 / CVSS v3: 9.4 / CWE-401 Missing Release of Memory after Effective Lifetime + CWE-306 Missing Authentication for Critical Function
- Affected: 1794-AENTR V2.012, 1794-AENTRXT V2.012
- Critical infrastructure sector: Critical Manufacturing
- Impact: CVE-2026-0646 — improper memory handling of CIP protocol requests causing adapter fault + loss of connection to associated I/O. CVE-2026-0647 — paired missing-authentication critical-function vulnerability. Combined: unauthorized access, account takeover, loss of availability.

## Attribution discipline (Hard Rule 2)

NOT TRIGGERED — vulnerability advisories carry no actor attribution claims. No Archimedes-originated attribution.

## A&D relevance assessment

- **Direct relevance:** NONE. No A&D-prime named victim.
- **Structural relevance via operational-template inheritance:** HIGH. Rockwell programmable automation controllers (CompactLogix / ControlLogix / GuardLogix), RSLinx Classic communications driver, FactoryTalk Analytics PavilionX, and FLEX I/O EtherNet/IP fieldbus adapters are widely deployed across A&D-prime manufacturing floors and DIB Tier-1/2 supplier networks.
- **Headline entry for A&D defenders:** CVE-2026-0646 + CVE-2026-0647 paired FLEX I/O 9.4 unauthenticated. Highest CVSS, paired memory-handling + missing-authentication, distributed I/O on EtherNet/IP fieldbus is common deployment pattern in DIB Tier-1/2 supplier manufacturing.
- **Vintage CVE-2020-13573 (RSLinx Classic):** broader cross-sector applicability per CISA (Critical Manufacturing + Energy + Food and Agriculture + Water and Wastewater). Legacy installations persist in industrial estates; patch eligibility audit recommended for any DIB supplier running RSLinx Classic ≤ 4.50.00.

## IOCs surfaced

NONE. These are vulnerability advisories, not active campaign reports. No IPs / domains / hashes / samples surface in CISA advisory text.

```yaml
iocs:
  cves:
    - id: CVE-2026-0646
      type: cve
      product: "Rockwell FLEX I/O EtherNet/IP Adapters 1794-AENTR/1794-AENTRXT"
      cvss: 9.4
      cwe: "CWE-401 Missing Release of Memory after Effective Lifetime"
      kev_listed: false
      source: "CISA ICSA-26-167-05"
    - id: CVE-2026-0647
      type: cve
      product: "Rockwell FLEX I/O EtherNet/IP Adapters 1794-AENTR/1794-AENTRXT"
      cvss: 9.4
      cwe: "CWE-306 Missing Authentication for Critical Function"
      kev_listed: false
      source: "CISA ICSA-26-167-05"
    - id: CVE-2026-11317
      type: cve
      product: "Rockwell CompactLogix 5370 / Compact GuardLogix 5370 / ControlLogix 5570 / GuardLogix 5570"
      cvss: 7.5
      cwe: "CWE-404 Improper Resource Shutdown or Release"
      kev_listed: false
      source: "CISA ICSA-26-167-03"
    - id: CVE-2025-11694
      type: cve
      product: "Rockwell CompactLogix 5370 L1/L2/L3"
      cvss: 7.5
      cwe: "CWE-354 + CWE-497"
      kev_listed: false
      source: "CISA ICSA-26-167-04"
    - id: CVE-2025-14272
      type: cve
      product: "Rockwell FactoryTalk Analytics PavilionX"
      cvss: 7.0
      cwe: "CWE-862 Missing Authorization"
      kev_listed: false
      source: "CISA ICSA-26-167-01"
    - id: CVE-2020-13573
      type: cve
      product: "Rockwell RSLinx Classic"
      cvss: 7.5
      cwe: "CWE-125 Out-of-bounds Read (stack-based buffer overflow)"
      vintage: true
      kev_listed: false
      source: "CISA ICSA-26-167-02"
      broader_sectors: ["Critical Manufacturing", "Energy", "Food and Agriculture", "Water and Wastewater"]
```

## Relationship to existing findings

- No standing Rockwell Automation finding in the corpus (last historical reference: finding-2026-05-12-0006 and finding-2026-05-28-0002, both unrelated to this CISA cluster).
- This finding is a net-new cluster anchor; vuln-tracker handoff operator-deferred for six CVE dossier scaffolds OR cluster-dossier decision.

## Open questions for analyst

- None at this grading pass — no attribution claim requiring ACH/KAC analysis; no WEP layer above "likely" requiring red-team review; no contradicting source. Vuln-tracker handoff is the operator-deferred pathway, not analyst pathway.

## Open questions for briefer

- Surface as A&D ICS Other Signal one-liner with FLEX I/O 9.4 unauthenticated as headline entry, or as standalone net-new finding surface notification at briefer discretion. Inclusion eligibility per `inclusion.eligible_for` is `daily_brief_other_signal` and `weekly_synthesis`; FLASH-ineligible by all six triggers.
- Critical Manufacturing operational-template inheritance baseline relevant to DIB Tier-1/2 supplier defenders is the framing handle.
