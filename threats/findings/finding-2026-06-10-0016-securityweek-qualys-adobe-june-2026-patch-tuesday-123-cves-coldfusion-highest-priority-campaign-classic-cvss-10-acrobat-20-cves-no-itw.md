---
finding_id: finding-2026-06-10-0016-securityweek-qualys-adobe-june-2026-patch-tuesday-123-cves-coldfusion-highest-priority-campaign-classic-cvss-10-acrobat-20-cves-no-itw
created_at: 2026-06-10T16:26:00-04:00
graded_by: grader
grading_run_id: afternoon-20260610-160000
grading_mode: scheduled_brief
test: false
status: graded

relates_to:
  - finding-2026-06-10-0001-bleepingcomputer-thn-krebs-june-2026-patch-tuesday-206-flaws-yellowkey-greenplasma-miniplasma-bitskrieg-http2-bomb-three-critical-rce
relation_type: june_2026_patch_tuesday_combined_cycle_adobe_complement_to_microsoft_206_cve_cluster

# Core grading (admiralty-grading skill output)
digraph: B2
digraph_layered:
  adobe_june_2026_patch_tuesday_123_cves_across_10_products: B2                          # SW primary; Qualys secondary aggregation
  apsb26_66_adobe_campaign_classic_two_cvss_10_cves: B2                                   # SW primary
  apsb26_64_adobe_coldfusion_seven_cves_adobe_highest_priority_label: B2                  # SW primary; Adobe-self-prioritization framing
  apsb26_63_acrobat_reader_20_cves: B2                                                    # SW primary
  apsb26_58_indesign_12_cves: B2                                                          # SW primary
  apsb26_57_experience_manager_forms_3_cves: B2                                           # SW primary
  patches_concurrent_with_advisory_no_zero_day_no_patch_gap: B1                            # Verifiable across vendor cycles class
  no_itw_attestation_visible_in_sw_aggregation: B1                                         # Verifiable absence
  no_actor_attribution_hard_rule_2_preserved: B1                                            # Verifiable absence
  no_iocs_published_vendor_patch_advisory_class: B1                                         # Verifiable absence
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored on ONE B-provisional media primary
  (SecurityWeek 2026-06-09) of Adobe PSIRT June 2026 cycle
  with ONE B-grade vendor-research secondary aggregation
  (Qualys). Adobe PSIRT primary not directly retrieved this
  sweep — vendor-on-own-product PSIRT-class procedurally
  A-equivalent but not yet in source-grades.yaml as
  dedicated id.

  B2 (not B1, not A2) anchored because:

    - SOURCE LETTER GRADE: One B-provisional primary + one
      B-grade vendor-research secondary. Adobe PSIRT
      primary not directly retrieved. Cluster letter holds
      at B under conservative aggregation. Future direct
      Adobe PSIRT retrieval would lift to B1 or A2.

    - INDEPENDENCE TEST: SW + Qualys are independent
      publishers but Qualys's coverage primarily aggregates
      vendor PSIRT outputs (similar to Tenable / Rapid7
      vulnerability research aggregation class). The
      Qualys analysis on the combined Microsoft + Adobe
      Patch Tuesday cycle is itself independent vendor-
      research commentary. Independence holds weakly at
      the editorial-aggregation tier.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed): partially supports —
        procedural facts (APSB IDs, product names, CVE
        counts, two CVSS 10s in Campaign Classic) are
        canonical from Adobe PSIRT vendor-on-own-product.
        But primary not directly retrieved + SW + Qualys
        editorial framing both trace to Adobe primary —
        falls to Grade 2.
      * Grade 2 (Probably True) PASSES: consistent with
        Adobe PSIRT established monthly cadence;
        consistent with established Adobe Patch Tuesday
        volume historical patterns (June cycle is often
        higher-volume due to ColdFusion-class disclosures
        + Acrobat Reader endpoint depth); no contradicting
        source; technical claims internally coherent
        (APSB IDs structurally valid; product names valid;
        CVSS 10 in Campaign Classic plausible for
        enterprise marketing platform with deep
        permissions model).

    - SUBSTANTIVE CLAIM LAYERS:
      * Patch volume + APSB IDs + product enumeration:
        B2 — SW primary + Qualys aggregation.
      * Adobe-self-prioritization of ColdFusion as
        highest-priority: B2 — SW primary; Adobe-self-
        attested editorial framing.
      * Two CVSS 10 CVEs in Campaign Classic: B2 — SW
        primary; specific CVE IDs pending direct Adobe
        PSIRT retrieval.
      * No-ITW: B1 — verifiable absence across SW + Qualys.

  Single-source veto NOT applied at cluster level.
  Watch signals: Tier-1 IR firm telemetry; direct Adobe
  PSIRT retrieval for specific CVE IDs + CVSS detail; CISA
  KEV addition on any ColdFusion CVE (historical attractor
  pattern).

source_reliability:
  cluster_anchor_grade: B
  sources:
    - source_yaml_id: securityweek
      grade: B
      provisional: true
      role: "Primary aggregation of Adobe PSIRT June 2026 cycle"
    - source_yaml_id: qualys
      grade: B
      provisional: true
      provisional_proposed_addition: true
      role: "Secondary vendor-research aggregation (combined Microsoft + Adobe Patch Tuesday cycle context); first Archimedes-corpus dedicated-id surface"
    - source_yaml_id: adobe-psirt
      grade: A
      provisional: true
      provisional_proposed_addition: true
      role: "Vendor self-disclosure on own product (APSB-series bulletins); A-provisional under PSIRT-class precedent; first Archimedes-corpus dedicated-id surface; primary not directly retrieved this sweep"
  grade_rationale: >
    Cluster letter grade holds at B under lowest-common-grade
    aggregation when Adobe PSIRT primary is not directly
    retrieved this sweep. Recommend source-grades.yaml
    additions for Adobe PSIRT (A provisional) and Qualys
    (B provisional).
  provisional: true

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_adobe_patch_tuesday_established_monthly_cadence
    - probably_true_no_contradicting_a_b_source
    - probably_true_technical_claims_coherent_apsb_ids_product_names_cvss_values_valid
  rationale: >
    APSB IDs structurally valid; product names valid; CVSS
    10 in Campaign Classic plausible for enterprise marketing
    platform class with deep permissions model. Consistent
    with Adobe PSIRT established monthly cadence and
    historical June-cycle volume patterns (ColdFusion-class
    disclosures + Acrobat Reader endpoint depth). No
    contradicting source.

corroboration:
  independent_sources:
    - securityweek
    - qualys
  independent: true
  test_passed: >
    SW + Qualys are independent publishers with different
    editorial focuses (SW is security-news media; Qualys is
    vendor-research aggregation). Both trace to Adobe PSIRT
    primary but with independent editorial commentary
    (Qualys adds combined-cycle context with Microsoft
    Patch Tuesday). Independence holds weakly at the
    editorial-aggregation tier.

first_party_precedence:
  applied: false
  splunk_evidence: >
    No published network IOCs in vendor patch advisory class.
    No first-party hunt actionable at this sweep.

single_source_veto_applied: false
single_source_veto_layers: []
wep_ceiling: likely

inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis

# Cluster metadata
cluster:
  topic: "Adobe June 2026 Patch Tuesday — 123 CVEs across 10 products (Reader, ColdFusion, Experience Manager Forms, InDesign, InCopy, Substance 3D Sampler, Content Credentials SDK, Dreamweaver, Format Plugins, Campaign Classic). Critical highlights: APSB26-66 Campaign Classic two CVSS 10 CVEs; APSB26-64 ColdFusion seven CVEs (Adobe-self-prioritized as highest priority of cycle); APSB26-63 Acrobat Reader 20 CVEs (ubiquitous endpoint deployment); APSB26-58 InDesign 12 CVEs; APSB26-57 Experience Manager Forms 3 CVEs. No ITW attestation in SW aggregation. Pairs with Microsoft Patch Tuesday 206 CVEs (finding-2026-06-10-0001) as largest combined monthly release since 2017 per Qualys analysis."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-10-pm-010
  attribution_claims: []

# Downstream handoff flags
analyst_review_required: false
red_team_review_required: false
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Source-grade revision proposals
source_grade_revision_proposed:
  - source_yaml_id: adobe-psirt
    current_grade: null
    proposed_grade: A_provisional
    reason: >
      First Archimedes-corpus dedicated-id surface for Adobe
      PSIRT. Vendor-on-own-product PSIRT-class precedent.
      Adobe products surface across A&D-prime endpoint
      (Acrobat Reader) + ColdFusion enterprise-web platform
      contexts; dedicated source id warranted.
    severity: addition_requires_ratification
    action: "Post to #actor-review for operator ratification"
  - source_yaml_id: qualys
    current_grade: null
    proposed_grade: B_provisional
    reason: >
      First Archimedes-corpus dedicated-id surface for Qualys
      vendor-research blog. Vendor vulnerability-research
      aggregation class peer to Tenable / Rapid7. Provisional
      B per Tier-2 vendor-research precedent.
    severity: addition_requires_ratification
    action: "Post to #actor-review for operator ratification"

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-10-afternoon]
retracted: false
retraction_brief_id: null
---

# Adobe June 2026 Patch Tuesday — 123 CVEs Across 10 Products; ColdFusion Adobe-Self-Prioritized as Highest Priority; Two CVSS 10 in Campaign Classic; Acrobat Reader 20 CVEs (No ITW Visible in SW Aggregation)

## Summary

Adobe's June 2026 Patch Tuesday addressed 123 vulnerabilities across 10 products per SecurityWeek and Qualys aggregation. Critical highlights: APSB26-66 Adobe Campaign Classic contains two CVSS 10.0 CVEs; APSB26-64 ColdFusion contains seven mostly Critical/High-rated CVEs and is Adobe-self-prioritized as highest priority of the cycle; APSB26-63 Acrobat Reader contains 20 CVEs (ubiquitous endpoint deployment burden). InDesign (APSB26-58) and Experience Manager Forms (APSB26-57) round out the named critical advisories. No in-the-wild exploitation attestation visible in SW aggregation. The Adobe cycle pairs with Microsoft's 206-CVE June Patch Tuesday (finding-2026-06-10-0001) as the largest combined monthly release since 2017 per Qualys analysis.

## Sources

### SecurityWeek (securityweek, B provisional)

- URL: https://www.securityweek.com/adobe-patches-123-vulnerabilities/
- Published: 2026-06-09
- Key claim: Aggregation framing on Adobe PSIRT June 2026 cycle; APSB ID enumeration; ColdFusion priority highlight.

### Qualys (qualys, B provisional — first Archimedes-corpus surface)

- URL: https://blog.qualys.com/vulnerabilities-threat-research/2026/06/09/microsoft-and-adobe-patch-tuesday-june-2026-security-update-review
- Key claim: Combined Microsoft + Adobe Patch Tuesday cycle context; "largest monthly release since 2017."

### Adobe PSIRT (adobe-psirt, A provisional — NOT directly retrieved this sweep)

## Technical detail

### Patch volume

- **123 vulnerabilities** across **10 products**: Reader, ColdFusion, Experience Manager Forms, InDesign, InCopy, Substance 3D Sampler, Content Credentials SDK, Dreamweaver, Format Plugins, Adobe Campaign Classic

### Critical advisories

| APSB ID | Product | CVE Count | Notes |
|---------|---------|-----------|-------|
| APSB26-66 | Campaign Classic | 2 CVSS 10 (cluster contents TBD) | Two CVSS 10 in enterprise marketing platform |
| APSB26-64 | ColdFusion | 7 mostly Critical/High | **Adobe-self-prioritized as highest priority of cycle** |
| APSB26-63 | Acrobat Reader | 20 | Ubiquitous endpoint deployment burden |
| APSB26-58 | InDesign | 12 | |
| APSB26-57 | Experience Manager Forms | 3 | |

### Patch and exploitation status

- All patches concurrent with advisory (no zero-day no-patch gap)
- No in-the-wild exploitation attestation surfaced in SW aggregation

## IOCs surfaced

None — vendor patch advisories.

## Relationship to existing findings

- **finding-2026-06-10-0001** — Microsoft June Patch Tuesday 206 CVEs; this finding (Adobe 123 CVEs) is the structural complement under combined-cycle framing.
- **Patch Tuesday combined-cycle context (per Qualys):** Microsoft 206 + Adobe 123 = largest combined monthly release since 2017.

## Open questions for analyst

- **A&D-prime defender priority:**
  - **ColdFusion (APSB26-64)** — HIGHEST priority. Adobe-self-confirmed + historical KEV-attractor pattern for ColdFusion CVEs frequently exploited in opportunistic and targeted operations against enterprise web platforms.
  - **Acrobat Reader (APSB26-63)** — HIGH priority. Ubiquitous deployment across A&D primes; 20 CVEs is high-volume patch deployment burden on endpoint security teams.
  - **Campaign Classic (APSB26-66)** — MEDIUM-HIGH. Two CVSS 10 CVEs but narrower deployment than Reader / ColdFusion.
  - **Experience Manager Forms (APSB26-57)** — MEDIUM. Some A&D-prime customer/supplier portal deployments.
- **Vuln-tracker dossier consideration:** ColdFusion APSB26-64 cluster warrants tracked-vulnerability dossier candidacy given Adobe-self-prioritization + historical exploitation patterns. Specific CVE IDs pending direct Adobe PSIRT retrieval.
- **Brief composition guidance:** PM brief could thread Microsoft (finding-2026-06-10-0001) + Adobe (this finding) + Ivanti/Fortinet/SAP (finding-2026-06-10-0009) + Veeam (finding-2026-06-10-0010) under combined "vendor patch surge" section rather than line-item per vendor.
- **Watch signals:** Tier-1 IR firm telemetry on any ColdFusion / Acrobat Reader / Campaign Classic exploitation; CISA KEV addition pattern (ColdFusion historical attractor); direct Adobe PSIRT retrieval for specific CVE IDs + CVSS detail.
