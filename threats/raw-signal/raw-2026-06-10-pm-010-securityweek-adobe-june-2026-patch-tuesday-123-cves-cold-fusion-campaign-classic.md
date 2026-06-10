---
raw_id: raw-2026-06-10-pm-010
collected_at: 2026-06-10T15:51:00-04:00
run_id: pre-brief-20260610-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek"
  source_url: https://www.securityweek.com/adobe-patches-123-vulnerabilities/  # canonical URL pattern; SW homepage shows "Adobe Patches 123 Vulnerabilities" 2026-06-09
  published_at: 2026-06-09T00:00:00+00:00
  retrieval_method: WebSearch + SW homepage rotation
secondary_sources:
  - id: thehackernews
    name: "Qualys / external aggregation"
    url: https://blog.qualys.com/vulnerabilities-threat-research/2026/06/09/microsoft-and-adobe-patch-tuesday-june-2026-security-update-review
    grade: B  # Tier-2 vendor-research aggregation
originating_vendor:
  vendor: "Adobe PSIRT (own-product self-disclosure via APSB-series bulletins)"
  vendor_disclosure_class: "Vendor-self-disclosure on own product — procedurally A-grade per PSIRT precedent class"
  source_grades_yaml_status: "Adobe PSIRT not yet a dedicated id — recommend addition at provisional A on next pass"
match_reason:
  watchlist: []
  actors: []
  vulnerabilities:
    - APSB26-66  # Adobe Campaign Classic CVSS 10 cluster
    - APSB26-64  # ColdFusion (highest-priority per Adobe)
    - APSB26-63  # Acrobat Reader (20 CVEs)
    - APSB26-58  # InDesign (12 CVEs)
    - APSB26-57  # Experience Manager Forms
  keywords: [Adobe, Patch Tuesday, June 2026, ColdFusion, Campaign Classic, Acrobat Reader, InDesign, Experience Manager, APSB26, 123 CVEs, CVSS 10.0, enterprise marketing platform]
triage_tags:
  - adobe_patch_tuesday_june_2026
  - 123_cves_record_breaking_month
  - two_cvss_10_in_campaign_classic
  - coldfusion_highest_priority_per_adobe
  - acrobat_reader_widely_deployed_a_d_relevance
  - vendor_self_disclosure_adobe_psirt_first_corpus_addition_pending
  - no_itw_attestation_visible_in_sw_aggregation
  - hard_rule_2_no_actor_attribution
iocs_extracted: true
iocs_count: 5  # 5 APSB IDs surfaced
text_word_count: 0
promoted: true
promoted_to_finding: finding-2026-06-10-0016-securityweek-qualys-adobe-june-2026-patch-tuesday-123-cves-coldfusion-highest-priority-campaign-classic-cvss-10-acrobat-20-cves-no-itw
promoted_at: 2026-06-10T16:30:00-04:00
ttl_expires_at: 2026-09-08T15:51:00-04:00
---

# Adobe June 2026 Patch Tuesday — 123 CVEs Across 10 Products (Two CVSS 10 in Campaign Classic)

**Primary source:** SecurityWeek — "Adobe Patches 123 Vulnerabilities" — 2026-06-09 (SecurityWeek homepage rotation; also paraphrased as "Adobe Patches 80 Vulnerabilities Across Eight Products" in alternate framing — total counts vary by vendor counting methodology).
**Secondary aggregation:** Qualys + WebSearch reconstruction

## Key claims

### Patch volume
- Adobe June 2026 release addresses **123 vulnerabilities** across **10 products**: Reader, ColdFusion, Experience Manager Forms, InDesign, InCopy, Substance 3D Sampler, Content Credentials SDK, Dreamweaver, Format Plugins, Adobe Campaign Classic.
- Coincides with Microsoft's record-breaking 200+ CVE Patch Tuesday cycle — combined cycle is largest monthly release since 2017 per Qualys analysis.

### Critical vulnerabilities highlighted
- **APSB26-66 (Adobe Campaign Classic):** Two **CVSS 10.0** rated CVEs in the enterprise marketing platform.
- **APSB26-64 (ColdFusion):** Seven mostly Critical/High rated CVEs. **Adobe prioritizes ColdFusion as highest priority** of the cycle.
- **APSB26-63 (Acrobat Reader):** 20 CVEs total.
- **APSB26-58 (InDesign):** 12 CVEs.
- **APSB26-57 (Experience Manager Forms):** 3 CVEs.

### Attribution / IOCs / exploitation
- No threat actor attribution.
- No IOCs published.
- No in-the-wild exploitation attestation surfaced in SW aggregation.
- Adobe vendor disclosure pattern is standard PSIRT cycle (advisory + patch released concurrently).

## Cross-corpus context

### A&D-prime defender relevance
- **ColdFusion (APSB26-64) is the highest-priority Adobe product class for A&D-prime defenders.** Historical pattern: ColdFusion CVEs frequently exploited in opportunistic and targeted operations against enterprise web platforms; Adobe's own "highest priority" framing reinforces operational urgency.
- **Acrobat Reader (APSB26-63) ubiquitous deployment** across A&D primes; 20 CVEs is a high-volume patch deployment burden on endpoint security teams.
- **Adobe Campaign Classic (APSB26-66 CVSS 10.0 cluster)** — enterprise marketing platform; less A&D-prime-direct than ColdFusion / Reader, but two CVSS 10 CVEs warrant flagging for any prime running Campaign Classic.
- **Experience Manager Forms (APSB26-57)** — used in some A&D-prime customer/supplier portal deployments; lower-priority but auditable.

### Patch Tuesday combined cycle context
- Microsoft AM-001 (206 CVEs incl. YellowKey / GreenPlasma / MiniPlasma) + Adobe pm-010 (123 CVEs) + Ivanti/Fortinet/SAP pm-003 (7 CVEs CVSS 9.0+) + Veeam pm-004 (CVE-2026-44963 CVSS 9.4) + Cisco SD-WAN Manager KEV add (CVE-2026-20245) + Chrome KEV add (CVE-2026-11645) + Arista no-patch KEV (CVE-2026-7473) = the broadest June Patch Tuesday cycle in Archimedes corpus history.
- Brief composition consideration: PM brief could thread the Patch Tuesday combined-cycle as a single "vendor patch surge" section rather than line-item per vendor.

## FLASH-trigger evaluation

- **Trigger 1 (critical-cve-exploited):** ❌ Two CVSS 10.0 in Campaign Classic meet CVSS threshold but no ITW attestation visible in SW aggregation. Doesn't meet Trigger 1's "active exploitation" requirement.
- **Trigger 6 (zero-day-no-patch):** ❌ Patches available concurrent with advisory.

Not a FLASH trigger. Brief-track. PM brief candidate as part of Patch Tuesday combined-cycle thread.

## Extraction notes

- Language: en
- Article type: vendor Patch Tuesday aggregation
- Raw IOC extraction invoked: yes (below)

## IOCs (from ioc-extraction skill)

```yaml
attribution_claims: []

vendor_advisories:
  - apsb_id: APSB26-66
    product: "Adobe Campaign Classic"
    cve_count: 2
    cvss_max: 10.0
    class: "Enterprise marketing platform"
    notes: "Two CVSS 10.0 CVEs (specific CVE IDs pending direct Adobe PSIRT retrieval)"

  - apsb_id: APSB26-64
    product: "Adobe ColdFusion"
    cve_count: 7
    severity_mix: "Mostly Critical/High"
    vendor_prioritization: "Highest priority of cycle per Adobe"
    a_d_prime_relevance: high

  - apsb_id: APSB26-63
    product: "Acrobat Reader"
    cve_count: 20
    a_d_prime_relevance: high  # Ubiquitous endpoint deployment

  - apsb_id: APSB26-58
    product: "InDesign"
    cve_count: 12

  - apsb_id: APSB26-57
    product: "Experience Manager Forms"
    cve_count: 3

vendor_disclosure_class:
  adobe_psirt:
    own_product: yes
    procedural_grade_class: "A-grade vendor-on-own-product per PSIRT precedent class (Cisco PSIRT / F5 PSIRT / Ivanti PSIRT / Palo Alto PSIRT / Arista PSIRT / Fortinet PSIRT recommended / SAP Security Patch Day recommended / Veeam recommended)"
    source_grades_yaml_status: "Not yet a dedicated id — recommend addition at provisional A on next pass"

network_iocs_extracted:
  domains: []
  ipv4: []
  hashes: []
  notes: "Vendor patch advisories — no campaign IOCs"

ad_prime_defender_priority:
  coldfusion: "HIGHEST — Adobe-confirmed priority + historical exploitation pattern"
  acrobat_reader: "HIGH — ubiquitous endpoint deployment, 20 CVEs deployment burden"
  campaign_classic: "MEDIUM-HIGH — two CVSS 10.0 CVEs, but narrower deployment than Reader/ColdFusion"
  experience_manager_forms: "MEDIUM — auditable customer/supplier portal class"
  indesign_dreamweaver_substance3d_format_plugins_inccopy_content_credentials_sdk: "LOW-MEDIUM"
```

## Notes for grader

- **Adobe PSIRT** recommended for source-grades.yaml addition at provisional A.
- **No FLASH trigger.** Brief-track.
- **ColdFusion priority signal** is the operative defender-actionable framing.
- **PM brief composition guidance** — consider threading with Microsoft Patch Tuesday (AM-001), Ivanti/Fortinet/SAP (pm-003), Veeam (pm-004), Cisco SD-WAN Manager KEV add as a combined "vendor patch surge" section rather than line-item.
- **Hard Rule 2** preserved — no actor attribution.
