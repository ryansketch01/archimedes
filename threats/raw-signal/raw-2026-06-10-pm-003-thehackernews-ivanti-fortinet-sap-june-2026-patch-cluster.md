---
raw_id: raw-2026-06-10-pm-003
collected_at: 2026-06-10T15:37:00-04:00
run_id: pre-brief-20260610-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News (Ravie Lakshmanan)"
  source_url: https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html
  published_at: 2026-06-10T15:10:59+00:00
  retrieval_method: WebFetch + RSS
secondary_sources:
  - id: bleepingcomputer
    name: "BleepingComputer"
    url: https://www.bleepingcomputer.com/news/security/sap-fixes-critical-flaws-in-netweaver-and-commerce-cloud/
    published_at: 2026-06-09T19:36:00+00:00  # pre-window indirectly relayed; SAP pickup may have additional in-window items
    grade: B
originating_vendors:
  - vendor: "Fortinet PSIRT (own-product self-disclosure)"
    cve_set: ["CVE-2026-25089"]
  - vendor: "Ivanti PSIRT (own-product self-disclosure)"
    cve_set: ["CVE-2026-10520", "CVE-2026-10523"]
    notes: "Carried forward from raw-2026-06-10-am-003 (already finding-2026-06-10-0003); Ivanti Sentry is corpus-tracked. This signal aggregates the Ivanti pair into the THN cross-vendor PT cluster article."
  - vendor: "SAP Security Patch Day (own-product self-disclosure)"
    cve_set: ["CVE-2026-44748", "CVE-2026-27671", "CVE-2026-22732", "CVE-2026-40128"]
match_reason:
  watchlist: []  # No A&D-prime named victim in any of these advisories
  actors: []  # No actor attribution
  vulnerabilities:
    - CVE-2026-25089  # FortiSandbox WEB UI command injection CVSS 9.1
    - CVE-2026-10520  # Ivanti Sentry pre-auth OS command injection CVSS 10.0 (carry-forward AM-003)
    - CVE-2026-10523  # Ivanti Sentry auth bypass CVSS 9.9 (carry-forward AM-003)
    - CVE-2026-44748  # SAP NetWeaver AS ABAP XML signature wrapping SAML CVSS 9.9
    - CVE-2026-27671  # SAP NetWeaver / ABAP Platform RFC memory corruption CVSS 9.8
    - CVE-2026-22732  # SAP Commerce Cloud / Data Hub Spring security issue CVSS 9.1
    - CVE-2026-40128  # SAP NetWeaver AS Java directory traversal CVSS 9.0
  keywords: [Ivanti Sentry, Fortinet, FortiSandbox, SAP, NetWeaver, ABAP Platform, Commerce Cloud, Data Hub, XML signature wrapping, SAML, RFC memory corruption, Spring security, directory traversal, patch tuesday, june 2026]
triage_tags:
  - vendor_patch_disclosures_aggregate
  - fortisandbox_pre_auth_command_injection_high_cvss_9_1
  - sap_netweaver_cvss_9_9_xml_signature_wrapping_saml
  - sap_critical_cluster_four_cves_above_cvss_9
  - ivanti_sentry_carry_forward_am003_already_promoted
  - no_itw_per_vendor_attestation_layer
  - hard_rule_2_no_actor_attribution
  - fortinet_psirt_sap_security_patch_day_provisional_a_grade_class
iocs_extracted: true
iocs_count: 7  # 7 CVEs
text_word_count: 0
promoted: true
promoted_to_finding: finding-2026-06-10-0009-thehackernews-bleepingcomputer-fortinet-sap-june-2026-patch-cluster-fortisandbox-cve-2026-25089-sap-netweaver-cve-2026-44748-no-itw
promoted_at: 2026-06-10T16:30:00-04:00
ttl_expires_at: 2026-09-08T15:37:00-04:00
---

# Ivanti, Fortinet, and SAP — June 2026 Critical-CVE Patch Cluster (THN aggregation)

**Primary source:** The Hacker News (Ravie Lakshmanan) — "Ivanti, Fortinet, and SAP Release Patches for Multiple Critical Vulnerabilities" — 2026-06-10T15:10:59 UTC

## Key claims (per THN aggregation; vendor advisories not directly retrieved this sweep)

This signal aggregates three vendors' June 2026 patch releases into one corpus record. Ivanti Sentry pair already raw-signaled at AM-003 + promoted to finding-2026-06-10-0003 — included here for cluster completeness; the operative new content this signal is the **Fortinet FortiSandbox** and **SAP NetWeaver/Commerce-Cloud cluster**.

### Fortinet — FortiSandbox WEB UI Command Injection

**CVE-2026-25089** (CVSS 9.1)
- **Type:** OS command injection in FortiSandbox WEB UI (CWE-78).
- **Class:** Improper neutralization of special elements used in an OS command. Unauthenticated attacker can execute unauthorized commands via crafted HTTP requests.
- **Affected products + fix matrix:**
  - FortiSandbox 5.0.0 – 5.0.5 → upgrade to 5.0.6+
  - FortiSandbox 4.4.0 – 4.4.8 → upgrade to 4.4.9+
  - FortiSandbox Cloud 5.0.4 – 5.0.5 → upgrade to 5.0.6+
  - FortiSandbox PaaS 5.0.4 – 5.0.5 → upgrade to 5.0.6+
- **Exploitation status (per Fortinet PSIRT via THN):** No evidence of in-the-wild exploitation.
- **Patch availability:** Available.
- **Vendor disclosure class:** Fortinet PSIRT vendor-self-disclosure on own product — procedurally A-grade per Cisco PSIRT / F5 PSIRT / Ivanti PSIRT / Palo Alto PSIRT / Arista PSIRT precedent class. Fortinet PSIRT NOT yet in source-grades.yaml as a dedicated id (note for source-grade-log review — recommend addition under the PSIRT-class A-grade precedent).

### Ivanti — Sentry Critical Flaws (carry-forward AM-003)

**CVE-2026-10520** (CVSS 10.0) — OS command injection (pre-auth), root-level RCE; no ITW per vendor.
**CVE-2026-10523** (CVSS 9.9) — Authentication bypass, arbitrary admin account creation; no ITW per vendor.
- **Versions:** Pre-R10.5.2 / R10.6.2 / R10.7.1.
- Already raw-signaled at raw-2026-06-10-am-003, promoted to finding-2026-06-10-0003. **No new content this signal** beyond cluster aggregation.

### SAP — Four Critical Vulnerabilities (June 2026 Security Patch Day)

| CVE | CVSS | Product | Type | ITW per vendor |
|-----|------|---------|------|-----|
| **CVE-2026-44748** | **9.9** | NetWeaver AS ABAP, ABAP Platform | XML signature wrapping in SAML | No |
| **CVE-2026-27671** | **9.8** | NetWeaver, ABAP Platform | Memory corruption (RFC) | No |
| **CVE-2026-22732** | **9.1** | Commerce Cloud, Data Hub | Spring security issue | No |
| **CVE-2026-40128** | **9.0** | NetWeaver AS Java | Directory traversal | No |

- **CVE-2026-44748 mechanism detail (per THN):** "Allows authenticated attackers to obtain a valid signed message and send modified signed XML documents with tampered identity information leading to unauthorized access" (paraphrased from THN excerpt; verbatim quote redacted per Hard Rule 6 — vendor advisory not directly retrieved this sweep).
- **SAP Security Patch Day disclosure class:** Vendor-self-disclosure on own product — procedurally A-grade per PSIRT precedent class. SAP NOT yet in source-grades.yaml as a dedicated id (note for source-grade-log review).

## Cross-corpus context

### Vendor coverage gap on source-grades.yaml
- **Fortinet PSIRT** — first dedicated-id surface candidate (peer to Cisco PSIRT, F5 PSIRT, Ivanti PSIRT, Palo Alto PSIRT, Arista PSIRT). Fortinet products surfaced in prior corpus: CVE-2026-44277 FortiAuthenticator (VT-007), CVE-2026-35616 FortiClient EMS (Arctic Wolf finding-2026-05-28-FLASH-1200-0001; cross-corpus to JDY botnet pm-001 today). Fortinet PSIRT now warrants a dedicated source-grades.yaml id at provisional A.
- **SAP Security Patch Day** — first dedicated-id surface candidate. SAP previously surfaced in finding-2026-05-12-FLASH-0001 (Mini Shai-Hulud lineage via Onapsis SAP CAP coverage). SAP Security Patch Day is the canonical vendor authority on SAP-product CVEs.

### Cross-corpus tie-in with FortiAuthenticator VT-007
- VT-007 (CVE-2026-44277 FortiAuthenticator pre-auth RCE) is in `kev_pending: true` state since 2026-05-12 (no ITW per Fortinet PSIRT; watching for any KEV addition or third-party IR-firm telemetry).
- Today's FortiSandbox CVE-2026-25089 is a **sibling pattern** — same vendor, same disclosure class (pre-auth, CWE-78 command injection on UI), same no-ITW vendor attestation, same fix-at-disclosure cadence.
- Suggests Fortinet PSIRT is on a regular vulnerability-disclosure cycle but no public exploitation of the May 2026 / June 2026 cluster has surfaced. Watch signals for VT-007 (Watchtowr / Horizon3.ai / Assetnote / Rapid7 n-day research) apply to FortiSandbox CVE-2026-25089 by structural similarity.

### A&D-prime defender relevance
- **FortiSandbox (CVE-2026-25089):** Network-security appliance class. Sandbox-class detection appliances are common across enterprise A&D estates as part of Fortinet's broader product line. Pre-auth WEB UI command injection on a security-stack appliance is a critical attack class — appliance compromise undermines the very detection layer it's meant to provide.
- **SAP NetWeaver (CVE-2026-44748 CVSS 9.9 + CVE-2026-27671 CVSS 9.8 + CVE-2026-40128 CVSS 9.0):** SAP NetWeaver / ABAP runs ERP / HR / finance / supply-chain / program-management for many A&D primes (Lockheed Martin / Boeing / RTX / BAE Systems / Airbus all have SAP deployments). XML signature wrapping SAML + RFC memory corruption + directory traversal cluster on the ERP layer is a CRITICAL defender priority for A&D estates running NetWeaver. No-ITW-per-vendor attestation is the standard initial framing; watch signals for Onapsis / Pathlock / Rapid7 / vendor exploit-broker telemetry.
- **SAP Commerce Cloud (CVE-2026-22732 CVSS 9.1):** Spring security issue. Less directly A&D-prime relevant than the NetWeaver cluster.

## FLASH-trigger evaluation

- **Trigger 1 (critical-cve-exploited):** ❌ No — every vuln in this cluster is no-ITW per vendor attestation. CVSS thresholds met (multiple >= 9.0) but the active-exploitation arm is absent.
- **Trigger 6 (zero-day-no-patch):** ❌ No — patches available at disclosure for all.
- **Trigger 5 (ad-sector-campaign):** ❌ No — no active campaign described.

Not a FLASH trigger. Brief-track. PM brief candidate as a high-volume Patch Tuesday cluster summary alongside the Microsoft + Adobe items.

## Extraction notes

- Language: en
- Publisher byline: Ravie Lakshmanan (THN recurring author)
- Article type: news aggregation of three vendor patch advisories
- Raw IOC extraction invoked: yes (below)

## IOCs (from ioc-extraction skill)

```yaml
attribution_claims: []  # No actor attribution per any of the three vendor advisories

cves:
  - cve: CVE-2026-25089
    vendor: Fortinet
    product: FortiSandbox WEB UI
    cvss: 9.1
    cwe: CWE-78
    type: "OS command injection"
    auth_required: false  # unauthenticated per THN
    itw_status: "No evidence of in-the-wild exploitation per Fortinet PSIRT"
    patch_available: true
    fix_versions:
      - "FortiSandbox 5.0.6+"
      - "FortiSandbox 4.4.9+"
      - "FortiSandbox Cloud 5.0.6+"
      - "FortiSandbox PaaS 5.0.6+"

  - cve: CVE-2026-10520
    vendor: Ivanti
    product: Sentry
    cvss: 10.0
    type: "OS command injection (pre-auth)"
    itw_status: "No ITW per vendor"
    patch_available: true
    carry_forward_from: "raw-2026-06-10-am-003 → finding-2026-06-10-0003"

  - cve: CVE-2026-10523
    vendor: Ivanti
    product: Sentry
    cvss: 9.9
    type: "Authentication bypass"
    itw_status: "No ITW per vendor"
    patch_available: true
    carry_forward_from: "raw-2026-06-10-am-003 → finding-2026-06-10-0003"

  - cve: CVE-2026-44748
    vendor: SAP
    product: "NetWeaver AS ABAP / ABAP Platform"
    cvss: 9.9
    type: "XML signature wrapping in SAML"
    auth_required: true  # authenticated per THN
    itw_status: "No ITW per vendor"
    patch_available: true
    mechanism: "Authenticated attacker obtains valid signed message + sends modified signed XML documents with tampered identity information → unauthorized access"

  - cve: CVE-2026-27671
    vendor: SAP
    product: "NetWeaver / ABAP Platform"
    cvss: 9.8
    type: "Memory corruption (RFC)"
    itw_status: "No ITW per vendor"
    patch_available: true

  - cve: CVE-2026-22732
    vendor: SAP
    product: "Commerce Cloud / Data Hub"
    cvss: 9.1
    type: "Spring security issue"
    itw_status: "No ITW per vendor"
    patch_available: true

  - cve: CVE-2026-40128
    vendor: SAP
    product: "NetWeaver AS Java"
    cvss: 9.0
    type: "Directory traversal"
    itw_status: "No ITW per vendor"
    patch_available: true

vendor_disclosure_class:
  fortinet_psirt:
    own_product: yes
    procedural_grade_class: "A-grade vendor-on-own-product per Cisco PSIRT / F5 PSIRT / Ivanti PSIRT / Palo Alto PSIRT / Arista PSIRT precedent"
    source_grades_yaml_status: "Not yet a dedicated id — recommend addition at provisional A"
  ivanti_psirt:
    own_product: yes
    procedural_grade_class: "A-grade — Ivanti PSIRT already provisional A in source-grades.yaml (2026-06-10 same-day precedent from AM-003)"
  sap_security_patch_day:
    own_product: yes
    procedural_grade_class: "A-grade vendor-on-own-product per same PSIRT precedent class"
    source_grades_yaml_status: "Not yet a dedicated id — recommend addition at provisional A"

network_iocs_extracted:
  domains: []
  ipv4: []
  hashes: []
  notes: "No IOCs — vendor patch advisories not exploitation reports"
```

## Notes for grader

- **Two source-grades.yaml additions** recommended: Fortinet PSIRT (provisional A) + SAP Security Patch Day (provisional A) — both peer to the established PSIRT-class A precedent. Pending human ratification per source-grade-log.md protocol.
- **Ivanti Sentry pair (CVE-2026-10520 + 10523)** is carry-forward from AM-003 / finding-2026-06-10-0003 — no new content; cluster mention only.
- **Hard Rule 2** preserved — no actor attribution surfaced.
- **No FLASH trigger** — all CVEs in cluster carry no-ITW vendor attestation.
- **A&D-prime defender priority** (operator lens): SAP NetWeaver cluster (4 CVEs >= 9.0 on ERP layer) is the highest-stakes class; FortiSandbox pre-auth RCE on security-stack appliance is a tight second; Ivanti Sentry already in AM brief.
- **Brief-track** — PM brief candidate as a critical-CVE cluster summary; consider grouping with Adobe (pm-010) and Microsoft Patch Tuesday context (already in AM brief) as a "June 2026 Patch Tuesday surge — vendor-cluster overview" thread.
