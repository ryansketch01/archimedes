---
raw_id: raw-2026-05-12-am-002
collected_at: 2026-05-12T07:32:00-04:00
run_id: pre-brief-20260512-073000
collection_mode: pre_brief_collection
sweep_type: pre_brief
test: false
source:
  source_yaml_id: siemens-productcert    # NOT YET IN source-grades.yaml as of 2026-05-12 — first Archimedes-corpus surface; source-grade-log candidate proposed below
  source_name: Siemens ProductCERT (vendor official advisory)
  source_urls:
    - https://cert-portal.siemens.com/productcert/html/ssa-081142.html   # RUGGEDCOM ROX command injection
    - https://cert-portal.siemens.com/productcert/html/ssa-357982.html   # ROS# path traversal
  source_grade_proposed: A (provisional, first surface — see source-grade-log block below)
  primary_disclosure_source: Siemens AG corporate (Siemens ProductCERT)
  primary_disclosure_source_grade_proposed: A (vendor official advisory)
  nvd_cross_corroboration:
    - source: nvd
      cve_records_fresh_today: ["CVE-2025-40949", "CVE-2026-41551", "CVE-2026-22924", "CVE-2026-25786", "CVE-2026-25787"]
      query_endpoint: services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=2026-05-12T06:00:00.000-04:00&lastModEndDate=2026-05-12T07:30:00.000-04:00
  published_at: 2026-05-12     # advisory publication date; specific UTC time not exposed in Siemens advisory HTML
  authors: Siemens ProductCERT (corporate byline per Siemens vendor-advisory convention)
match_reason:
  watchlist: []
  watchlist_match_strength: structural_via_siemens_as_supplier_to_primes_and_ros_aerospace_defense_robotics_context
  watchlist_match_detail: |
    Siemens AG is not directly named in infrastructure/watchlists/
    aerospace-defense.yaml (which tracks Tier-1 A&D primes), but
    Siemens is a Tier-1 A&D supplier with substantial defense-
    electronics, avionics, ground-systems, and military-radar
    business. Siemens products are deployed across defense
    manufacturing facilities, test environments, ground support
    equipment, and weapon-system integration labs — making Siemens
    advisories structurally relevant to A&D prime infrastructure
    even when no specific prime is named as a victim.

    Per the structural-A&D-relevance test established in
    raw-2026-05-09-am-001 (OpenC3 COSMOS five-CVE cluster NVD-direct
    find), and refreshed in raw-2026-05-12-am-001 (SAP May Patch Day,
    same sweep), Siemens May 2026 Patch Tuesday cluster is RAW-
    SIGNALED via the same rationale.

    Specifically relevant products in this cluster:
      - RUGGEDCOM ROX (SSA-081142, CVE-2025-40949): ruggedized
        industrial networking devices for "electrical harsh and
        climatically demanding environments such as electric
        utility substations and traffic control cabinets"
        (per Siemens advisory text) — also deployed in defense
        ground systems and military substation contexts.
      - ROS# (SSA-357982, CVE-2026-41551): Siemens' .NET library
        for the Robot Operating System (ROS), used in robotics
        applications including aerospace/defense robotics R&D
        (military UGV / UAV ground control / collaborative
        robotics in manufacturing). UNAUTHENTICATED CVSS 9.1 is
        a high-concern profile.
      - SIMATIC CN 4100 (CVE-2026-22924): communication node
        used in industrial automation contexts including defense
        manufacturing.
      - SIMATIC PLC/HMI (CVE-2026-25786, CVE-2026-25787): XSS
        via PLC station name and Technology Object name — widely
        deployed industrial control system endpoints.

    Per Hard Rule 2, the collector does NOT assert any specific
    prime has been impacted by these Siemens 2026-05-12 advisories.
    The structural-relevance surfacing is a sector-scope handoff
    to the grader, not an attribution claim.
  actors: []
  actors_attribution_note: |
    Siemens advisories cite NO threat actor attribution. No active
    exploitation claimed in any of the four advisory clusters.
    Hard Rule 2 applies.
  vulnerabilities:
    - cve: CVE-2025-40949
      siemens_advisory_id: SSA-081142
      product: RUGGEDCOM ROX
      product_family: industrial_ruggedized_networking
      version_range: all_below_v2.17.1
      affected_models: ["MX5000", "MX5000RE", "RX1400", "RX1500", "RX1501", "RX1510", "RX1511", "RX1512", "RX1524", "RX1536", "RX5000"]
      severity_class: HIGH_to_CRITICAL
      cvss_v3_1: 9.1
      cvss_v4_0: 8.9
      cwe: CWE-78    # OS Command Injection
      attack_vector: Network
      attack_complexity: Low
      privileges_required: High (authenticated)
      user_interaction: None
      impact: Authenticated_attacker_arbitrary_command_execution_with_root_privileges
      exploitation_status: not_observed_per_vendor_at_patch_time
      patch_status: available_v2.17.1_or_later
      kev_status: NOT_KEV_LISTED
    - cve: CVE-2026-41551
      siemens_advisory_id: SSA-357982
      product: ROS# (.NET library for Robot Operating System)
      product_family: industrial_robotics_library_dotnet
      version_range: all_before_v2.2.2
      severity_class: CRITICAL
      cvss_v3_1: 9.1
      cvss_v4_0: 9.3
      cwe: CWE-23    # Relative Path Traversal
      attack_vector: Network
      attack_complexity: Low
      privileges_required: None_UNAUTHENTICATED
      user_interaction: None
      impact: Remote_attacker_arbitrary_file_read_write_on_device_with_service_user_privileges
      exploitation_status: not_observed_per_vendor_at_patch_time
      patch_status: available_v2.2.2_or_later
      remediation_link: https://github.com/siemens/ros-sharp/releases/tag/2.2.2
      kev_status: NOT_KEV_LISTED
      pre_patch_mitigations:
        - Deploy file_server exclusively on trusted networks
        - Execute with minimal necessary user permissions
        - Operate only for intended URDF file transfers, not continuous background services
        - Use only when manual file transfers are infeasible
    - cve: CVE-2026-22924
      product: SIMATIC CN 4100
      product_family: industrial_communication_node
      severity_class: HIGH
      cvss_v3_1: 8.8
      cwe_class: improper_connection_restriction_resource_exhaustion
      exploitation_status: not_observed_per_vendor_at_patch_time
      kev_status: NOT_KEV_LISTED
      nvd_status: Received_2026-05-12
    - cve: CVE-2026-25786
      product: SIMATIC (PLC/HMI line per NVD)
      severity_class: CRITICAL
      cvss_v3_1: 9.1
      vulnerability_type: stored_xss_via_unsanitized_plc_station_name_on_communication_parameters_page
      exploitation_status: not_observed_per_vendor_at_patch_time
      kev_status: NOT_KEV_LISTED
      nvd_status: Received_2026-05-12
    - cve: CVE-2026-25787
      product: SIMATIC (PLC/HMI line per NVD)
      severity_class: CRITICAL
      cvss_v3_1: 9.1
      vulnerability_type: stored_xss_via_unsanitized_technology_object_name_on_motion_control_diagnostics_page
      exploitation_status: not_observed_per_vendor_at_patch_time
      kev_status: NOT_KEV_LISTED
      nvd_status: Received_2026-05-12
  vulnerabilities_summary: |
    Siemens May 2026 Patch Tuesday cluster — FIVE CVEs published
    on 2026-05-12, all FRESH this sweep (Siemens ProductCERT
    SSA-081142 + SSA-357982 direct, plus three SIMATIC entries
    surfaced via NVD lastModStartDate window-query):

    HEADLINER: CVE-2026-41551 (Siemens SSA-357982) — ROS# path
    traversal, CVSS 9.1 v3.1 / 9.3 v4.0, attack-vector NETWORK,
    UNAUTHENTICATED, no user interaction required. Arbitrary file
    read AND write on device with service-user privileges. Patched
    in ROS# v2.2.2. ROS# is the .NET library Siemens publishes for
    Robot Operating System (ROS) — used in robotics applications
    that span manufacturing, automation, simulation, and (per
    structural relevance) aerospace/defense robotics R&D.

    NEAR-HEADLINER: CVE-2025-40949 (Siemens SSA-081142) — RUGGEDCOM
    ROX command injection in Scheduler Web UI, CVSS 9.1 v3.1 /
    8.9 v4.0, attack-vector NETWORK, AUTHENTICATED (PR:H),
    arbitrary command execution at root. Patched in v2.17.1.
    Affects 11 RUGGEDCOM ROX model variants (MX5000/RX1400/etc).
    Critical-infrastructure deployment — electrical utility
    substations, traffic control cabinets, defense ground systems.

    SIMATIC cluster: CVE-2026-22924 (8.8 HIGH, CN 4100 resource
    exhaustion) + CVE-2026-25786/25787 (both 9.1 CRITICAL, XSS in
    PLC station / Technology Object name fields).

    Siemens advisories cite no in-the-wild exploitation observed.
    KEV catalog (verified 2026-05-12T07:30 EDT) shows ZERO entries
    dateAdded >= 2026-05-11 — none of these five CVEs are KEV-listed.
  keywords:
    - siemens_may_2026_patch_tuesday
    - ruggedcom_rox_ssa_081142
    - ros_sharp_ssa_357982
    - simatic_cluster
    - cve_2026_41551_ros_sharp_unauthenticated_path_traversal_9_1
    - cve_2025_40949_ruggedcom_rox_command_injection_9_1
    - cve_2026_22924_simatic_cn_4100_resource_exhaustion
    - cve_2026_25786_simatic_xss_plc_station_name
    - cve_2026_25787_simatic_xss_technology_object_name
    - structural_ad_relevance_via_siemens_supplier_chain
    - ros_sharp_robotics_aerospace_defense_context
    - critical_infrastructure_industrial_networking_robotics
    - vendor_advisory_first_archimedes_corpus_surface
triage_tags:
  - non_flash
  - flash_trigger_1_fail_no_active_exploitation
  - flash_trigger_5_fail_no_specific_ad_prime_named
  - flash_trigger_6_fail_patched_at_disclosure
  - grader_queue_for_morning_brief
  - structural_ad_relevance_via_siemens_supplier_chain
  - siemens_productcert_vendor_source_grade_log_candidate
  - first_siemens_productcert_archimedes_corpus_surface
  - ros_sharp_unauthenticated_cvss_9_1_headliner
  - ruggedcom_rox_authenticated_cvss_9_1_near_headliner
  - simatic_xss_pair_9_1_cluster_corroboration
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    fail_reason: |
      Siemens advisories cite NO active exploitation for any of
      the four advisory clusters. CVSS scores >= 9.0 satisfied
      on CVE-2025-40949 (9.1), CVE-2026-41551 (9.1), CVE-2026-25786
      (9.1), CVE-2026-25787 (9.1) — but the active-exploitation
      criterion FAILS. Trigger 1 requires the strict conjunction.
  trigger_2_tracked_actor_attribution:
    matched: false
    fail_reason: |
      No threat-actor attribution claimed in Siemens advisories
      or NVD CVE records.
  trigger_3_first_party_ioc_hit:
    matched: false
    fail_reason: |
      Splunk archimedes + defenseclaw_local combined sweep over
      14h returns zero non-archimedes-internal events; over 24h
      zero events. Targeted IOC keyword sweep across Siemens
      CVE tokens (CVE-2025-40949, CVE-2026-41551, CVE-2026-22924,
      CVE-2026-25786, CVE-2026-25787, RUGGEDCOM, SIMATIC, ROS#)
      over 24h matched only pipeline self-references. Trigger 3
      cannot fire on a dormant non-Archimedes stream.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    fail_reason: |
      No tracked-actor activity. Siemens Patch Tuesday cadence is
      regular vendor security cycle, not actor TTP.
  trigger_5_ad_sector_campaign:
    matched: false
    fail_reason: |
      Siemens advisories cite no campaign, no victims, no specific
      sector targeting. STRUCTURAL A&D-relevance is real but does
      NOT meet Trigger 5's explicit "campaign described with multi-
      victim confirmed and A&D-watchlist-entity hit" structural
      test. Consistent with the strict reading applied to prior
      structural-relevance cases (OpenC3 COSMOS, SailPoint,
      HookedWing, SAP this same sweep).
  trigger_6_zero_day_no_patch:
    matched: false
    fail_reason: |
      Patches available at disclosure for all five CVEs in the
      cluster — Siemens published all four SSAs with concurrent
      patch release. Type-mismatch for Trigger 6's unpatched-
      orphan-vuln structural fit.
  critical_override_evaluated:
    applied: false
    conditions_failed: 4_of_4
    notes: |
      Override requires CVSS 10.0 + confirmed exploitation +
      tracked actor + A&D watchlist hit. CVSS 9.1 < 10.0 floor
      (TWO of the cluster's CVEs at exactly 9.1 — Trigger 1 floor
      satisfied but critical-override floor NOT satisfied). Zero
      exploitation. No actor. No specific prime named. N/A.

source_grade_log_candidate_block:
  proposed_persistence:
    - source_yaml_id: siemens-productcert
      proposed_category: government_or_vendor   # vendor official-advisory tier; some operators categorize ICS-vendor advisories alongside CISA ICS-CERT under government — operator decision
      proposed_grade: A
      rationale: |
        Siemens ProductCERT is the official vendor security-advisory
        publishing arm of Siemens AG — Tier-1 industrial-automation
        vendor with substantial A&D-supplier business. ProductCERT
        advisories are technically vetted, peer-reviewed internally
        before publication, and consistently follow vendor-advisory
        rigor matching the precedent of MSRC (A), Palo Alto Networks
        PSIRT (A), Ivanti PSIRT (cited at A across prior corpus),
        SAP corporate (proposed A in companion AM-001 this same
        sweep). Siemens advisories include CVSS v3.1 + v4.0 scores,
        full CWE classifications, affected-version matrices, and
        remediation paths. Provisional A appropriate per same
        precedent applied to other vendor official-advisory tiers.

        Note on RSS feed: Siemens ProductCERT publishes an RSS feed
        at https://cert-portal.siemens.com/productcert/rss/
        advisories.rss — but this sweep observed it stale at
        January 2026 dates. Recent advisories surface via direct
        SSA-URL fetch only. Operator decision: ratify provisional
        A grade AND identify a working RSS endpoint OR rely on
        WebFetch fallback for direct SSA-URL retrieval.

        First Archimedes-corpus surface — pending operator
        ratification.
      first_cite: raw-2026-05-12-am-002
      ad_relevance_strength: structural_medium (supplier-chain across primes; ROS# specific aerospace/defense robotics R&D context)

extraction_notes:
  language: en
  article_type: vendor_official_advisory_direct_plus_nvd_window_query
  primary_source_byline: Siemens ProductCERT (corporate)
  raw_ioc_extraction_invoked: yes
  iocs_summary: 5 CVEs (CVE-2025-40949 + CVE-2026-41551 + CVE-2026-22924 + CVE-2026-25786 + CVE-2026-25787); 2 Siemens advisory IDs (SSA-081142, SSA-357982); 1 GitHub remediation tag (siemens/ros-sharp v2.2.2); no IPs / domains / hashes (vulnerabilities, not infrastructure)

iocs:
  cves:
    - id: CVE-2025-40949
      siemens_advisory: SSA-081142
      product: RUGGEDCOM ROX
      class: os_command_injection_cwe_78
      severity_class: HIGH_to_CRITICAL
      cvss_v3_1: 9.1
      cvss_v4_0: 8.9
      kev_listed: false
      exploitation_status: not_observed
      patch_status: available_v2.17.1_or_later
      affected_models: ["MX5000", "MX5000RE", "RX1400", "RX1500", "RX1501", "RX1510", "RX1511", "RX1512", "RX1524", "RX1536", "RX5000"]
      privileges_required: High_authenticated
    - id: CVE-2026-41551
      siemens_advisory: SSA-357982
      product: ROS_sharp_dotnet_library_for_robot_operating_system
      class: relative_path_traversal_cwe_23
      severity_class: CRITICAL
      cvss_v3_1: 9.1
      cvss_v4_0: 9.3
      kev_listed: false
      exploitation_status: not_observed
      patch_status: available_v2.2.2_or_later
      privileges_required: None_UNAUTHENTICATED
      remediation_url: https://github.com/siemens/ros-sharp/releases/tag/2.2.2
    - id: CVE-2026-22924
      product: SIMATIC_CN_4100
      class: improper_connection_restriction_resource_exhaustion
      severity_class: HIGH
      cvss_v3_1: 8.8
      kev_listed: false
      exploitation_status: not_observed
      nvd_status: Received_2026-05-12
    - id: CVE-2026-25786
      product: SIMATIC
      class: stored_xss_plc_station_name
      severity_class: CRITICAL
      cvss_v3_1: 9.1
      kev_listed: false
      exploitation_status: not_observed
      nvd_status: Received_2026-05-12
    - id: CVE-2026-25787
      product: SIMATIC
      class: stored_xss_technology_object_name
      severity_class: CRITICAL
      cvss_v3_1: 9.1
      kev_listed: false
      exploitation_status: not_observed
      nvd_status: Received_2026-05-12
  vendor_advisory_urls:
    - https://cert-portal.siemens.com/productcert/html/ssa-081142.html
    - https://cert-portal.siemens.com/productcert/html/ssa-357982.html
  remediation_urls:
    - https://github.com/siemens/ros-sharp/releases/tag/2.2.2
  domains: []
  ipv4: []
  ipv6: []
  urls: []
  hashes:
    sha256: []
    sha1: []
    md5: []
  attribution_claims: []   # Hard Rule 2 — no attribution observed in source
  exploitation_status_aggregate: not_observed_per_vendor_at_patch_time_across_all_five_cves
  patch_status_aggregate: available_at_disclosure_across_all_five_cves

promoted: true
promoted_to_finding: finding-2026-05-12-0002
promoted_at: 2026-05-12T08:08:00-04:00
promoted_by_grading_run_id: morning-20260512-080000
ttl_expires_at: 2026-08-10T07:32:00-04:00
---

# Siemens May 2026 Patch Tuesday — RUGGEDCOM ROX SSA-081142 + ROS# SSA-357982 + SIMATIC cluster (Siemens ProductCERT direct + NVD corroboration)

## What the sources say

**Sources:**
- **Siemens ProductCERT (vendor official advisory; first Archimedes-corpus surface)**
  - SSA-081142 — RUGGEDCOM ROX command injection (CVE-2025-40949) — published 2026-05-12
  - SSA-357982 — ROS# path traversal (CVE-2026-41551) — published 2026-05-12
- **NVD (A-grade reference)** — window-query 2026-05-12T06:00 → 07:30 EDT surfaced fresh Siemens 2026-numbered CVEs (CVE-2026-22924, CVE-2026-25786, CVE-2026-25787, CVE-2026-41551), plus the RUGGEDCOM ROX CVE-2025-40949 metadata-refresh corresponding to today's SSA-081142 advisory.

**Key claims (per Siemens advisories + NVD CVE records):**

### Headliner — CVE-2026-41551 (Siemens SSA-357982, ROS#)

- **Product:** ROS# (Siemens' .NET library for the Robot Operating System) — all versions before V2.2.2.
- **Vulnerability:** Path traversal in `file_server` component due to unsanitized user input (CWE-23 Relative Path Traversal).
- **Impact:** Remote attacker can read AND write arbitrary files on the device with the service user's privileges.
- **CVSS:** 9.1 CRITICAL (v3.1) / 9.3 CRITICAL (v4.0).
- **Attack profile:** Network vector, **no authentication required**, no user interaction.
- **Patch:** ROS# v2.2.2 available at https://github.com/siemens/ros-sharp/releases/tag/2.2.2.
- **Pre-patch mitigations** (per Siemens advisory): deploy `file_server` exclusively on trusted networks; execute with minimal necessary user permissions; operate only for intended URDF file transfers, not continuous background services; use only when manual file transfers are infeasible.

**Why this is the headliner:** Unauthenticated network-vector file-read-AND-write on a robotics library is a high structural concern. ROS# is used in robotics applications including aerospace/defense robotics R&D contexts (military UGV / UAV ground control / collaborative robotics in manufacturing). The advisory does not name specific aerospace/defense customers, but ROS is the dominant open-source robotics middleware and ROS# is its primary .NET interop layer.

### Near-headliner — CVE-2025-40949 (Siemens SSA-081142, RUGGEDCOM ROX)

- **Product:** RUGGEDCOM ROX II family — MX5000, MX5000RE, RX1400, RX1500, RX1501, RX1510, RX1511, RX1512, RX1524, RX1536, RX5000 — all versions below V2.17.1.
- **Vulnerability:** Scheduler functionality in the Web UI doesn't properly sanitize user-supplied input (CWE-78 OS Command Injection).
- **Impact:** Authenticated attacker arbitrary command execution with **root** privileges.
- **CVSS:** 9.1 CRITICAL (v3.1) / 8.9 HIGH (v4.0).
- **Attack profile:** Network vector, low complexity, **authentication required (PR:H)**, no user interaction.
- **Patch:** v2.17.1 available.
- **Critical-infrastructure context** (per Siemens advisory): "RUGGEDCOM Ethernet switches are used to operate reliably in electrical harsh and climatically demanding environments such as electric utility substations and traffic control cabinets" — also deployed in defense ground systems and military substation contexts.

### SIMATIC cluster (NVD-surfaced)

- **CVE-2026-22924** — SIMATIC CN 4100 communication node: improper connection restriction enabling resource exhaustion. CVSS 8.8 HIGH. NVD status: Received 2026-05-12.
- **CVE-2026-25786** — SIMATIC stored XSS via unsanitized PLC station name on communication parameters page. CVSS 9.1 CRITICAL. NVD status: Received 2026-05-12.
- **CVE-2026-25787** — SIMATIC stored XSS via unsanitized Technology Object name on Motion Control Diagnostics page. CVSS 9.1 CRITICAL. NVD status: Received 2026-05-12.

### Exploitation and KEV status

- Siemens advisories cite **NO in-the-wild exploitation observed** for any of the four advisory clusters.
- KEV catalog (verified 2026-05-12T07:30 EDT via JSON catalog fetch) shows **ZERO entries with dateAdded >= 2026-05-11** — none of these five CVEs are KEV-listed at this sweep.

## Structural A&D relevance

No specific A&D prime is named as a victim or impacted organization in any of the Siemens advisories. Structural-relevance rationale follows the same precedent as `raw-2026-05-09-am-001` (OpenC3 COSMOS) and `raw-2026-05-12-am-001` (SAP May Patch Day, same sweep):

| Siemens product | A&D structural relevance |
|---|---|
| RUGGEDCOM ROX | Ruggedized industrial networking for "harsh and climatically demanding environments" — substations, traffic control cabinets — also deployed in defense ground systems, military substation contexts, weapons-test environments. |
| ROS# (.NET library for ROS) | Robotics middleware bridge — used in robotics applications including aerospace/defense robotics R&D (military UGV / UAV ground control / collaborative robotics in defense manufacturing). |
| SIMATIC CN 4100 | Industrial communication node — deployed across defense manufacturing facilities. |
| SIMATIC PLC/HMI | Industrial control system endpoints — widely deployed across defense manufacturing, weapons-test ranges, ground support equipment. |

Siemens is a Tier-1 A&D supplier (avionics, aerospace ground systems, defense electronics) — the supplier-chain relevance is the structural argument. Per Hard Rule 2, the collector does **not** assert specific prime impact from these specific 2026-05-12 advisories.

## FLASH trigger evaluation

All six FLASH triggers FAIL for this cluster:

- **Trigger 1 (critical-cve-exploited)** — strict conjunction requires CVSS >= 9.0 AND active exploitation AND A-grade source naming operational layer. CVSS floor satisfied on 4 of 5 cluster CVEs (9.1 each). **Active exploitation NOT observed per vendor** — fails.
- **Trigger 2 (tracked-actor-attribution)** — no actor claimed.
- **Trigger 3 (first-party-ioc-hit)** — Splunk dormant 17th consecutive sweep; targeted Siemens-keyword sweep returned only pipeline self-references.
- **Trigger 4 (tracked-actor-ttp-change)** — no actor activity; vendor Patch Tuesday cadence is regular security cycle, not actor TTP.
- **Trigger 5 (ad-sector-campaign)** — no campaign described; structural A&D-relevance does not meet the explicit "multi-victim-confirmed-and-A&D-watchlist-entity-hit" test (consistent with prior structural cases).
- **Trigger 6 (zero-day-no-patch)** — patches available at disclosure for all five CVEs.

**Critical override:** N/A (4 of 4 conditions failed — CVSS at 9.1 below 10.0 floor; no exploitation; no actor; no specific prime).

**Grader disposition:** Non-FLASH grader-queue item for 08:00 morning brief. CVE-2026-41551 (ROS# UNAUTHENTICATED CVSS 9.1 path traversal) is the headliner — the unauthenticated network-vector profile in a robotics library warrants prominent treatment even without active-exploitation gating.

## Source-grade-log candidate

This is the **first Siemens ProductCERT direct-advisory citation in the Archimedes corpus**. Operator decision candidate: add `siemens-productcert` to `source-grades.yaml` at provisional A grade.

Rationale: Siemens ProductCERT is Tier-1 industrial-automation vendor's official security-advisory publishing arm — technically vetted, peer-reviewed internally before publication, full CVSS v3.1 + v4.0 + CWE + affected-version-matrix + remediation rigor. Aligns with MSRC, Palo Alto PSIRT, Ivanti PSIRT, SAP corporate (proposed A in companion AM-001 this same sweep).

**RSS feed status:** Siemens ProductCERT publishes RSS at https://cert-portal.siemens.com/productcert/rss/advisories.rss but this sweep observed the feed stale at January 2026 dates. Recent advisories surface only via direct SSA-URL fetch. Operator decision needed: ratify provisional A grade AND identify a working RSS endpoint OR rely on WebFetch fallback for direct SSA-URL retrieval going forward.

## Splunk first-party telemetry

Combined `archimedes` + `defenseclaw_local` sweep over 14h returns zero non-archimedes-internal events. Targeted IOC keyword sweep across Siemens-related tokens (`CVE-2025-40949`, `CVE-2026-41551`, `CVE-2026-22924`, `CVE-2026-25786`, `CVE-2026-25787`, `RUGGEDCOM`, `SIMATIC`, `ROS#`) over 24h matched only `archimedes:operation` pipeline self-references. Trigger 3 cannot fire on a dormant stream. Seventeenth consecutive dormant-stream sweep.

## Anti-noise observations

No prior Archimedes-corpus coverage of these specific Siemens advisories or CVEs. Prior corpus coverage of Siemens products: zero direct ProductCERT-source surface to date (per source-grades.yaml review). Anti-noise rule "one signal per topic per 24h" applies per-topic; this is a fresh topic. No anti-noise hit.

## Extraction notes

- Language: en
- Primary source byline: Siemens ProductCERT (corporate vendor-advisory convention)
- Article type: vendor official advisory direct fetch (SSA-081142 + SSA-357982) + NVD CVE-record window-query corroboration
- Raw IOC extraction invoked: yes — 5 CVEs surfaced; 2 Siemens advisory IDs; 1 GitHub remediation tag (siemens/ros-sharp v2.2.2); vulnerabilities only, no infrastructure IOCs (this is a product-vulnerability cluster, not a campaign analysis)

## IOCs

```yaml
cves:
  - id: CVE-2025-40949
    siemens_advisory: SSA-081142
    product: RUGGEDCOM_ROX
    affected_models: ["MX5000", "MX5000RE", "RX1400", "RX1500", "RX1501", "RX1510", "RX1511", "RX1512", "RX1524", "RX1536", "RX5000"]
    class: os_command_injection_cwe_78
    severity_class: HIGH_to_CRITICAL
    cvss_v3_1: 9.1
    cvss_v4_0: 8.9
    privileges_required: High_authenticated
    exploitation_status: not_observed_per_vendor_at_patch_time
    patch_status: available_v2.17.1_or_later
    kev_listed: false
  - id: CVE-2026-41551
    siemens_advisory: SSA-357982
    product: ROS_sharp_dotnet_library_for_ROS
    class: relative_path_traversal_cwe_23
    severity_class: CRITICAL
    cvss_v3_1: 9.1
    cvss_v4_0: 9.3
    privileges_required: None_UNAUTHENTICATED
    exploitation_status: not_observed_per_vendor_at_patch_time
    patch_status: available_v2.2.2_or_later
    kev_listed: false
    remediation_url: https://github.com/siemens/ros-sharp/releases/tag/2.2.2
  - id: CVE-2026-22924
    product: SIMATIC_CN_4100
    class: improper_connection_restriction_resource_exhaustion
    severity_class: HIGH
    cvss_v3_1: 8.8
    kev_listed: false
    nvd_status: Received_2026-05-12
  - id: CVE-2026-25786
    product: SIMATIC
    class: stored_xss_plc_station_name
    severity_class: CRITICAL
    cvss_v3_1: 9.1
    kev_listed: false
    nvd_status: Received_2026-05-12
  - id: CVE-2026-25787
    product: SIMATIC
    class: stored_xss_technology_object_name
    severity_class: CRITICAL
    cvss_v3_1: 9.1
    kev_listed: false
    nvd_status: Received_2026-05-12

vendor_advisory_urls:
  - https://cert-portal.siemens.com/productcert/html/ssa-081142.html
  - https://cert-portal.siemens.com/productcert/html/ssa-357982.html

remediation_urls:
  - https://github.com/siemens/ros-sharp/releases/tag/2.2.2

domains: []
ipv4: []
hashes:
  sha256: []
attribution_claims: []   # Hard Rule 2 — no attribution observed in any of the Siemens advisories or NVD CVE records
exploitation_status_aggregate: not_observed_per_vendor_at_patch_time_across_all_five_cves
patch_status_aggregate: available_at_disclosure_across_all_five_cves
```
