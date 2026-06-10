---
raw_id: raw-2026-06-10-pm-008
collected_at: 2026-06-10T15:47:00-04:00
run_id: pre-brief-20260610-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek"
  source_url: https://www.securityweek.com/ics-patch-tuesday-vulnerabilities-fixed-by-siemens-schneider-phoenix-contact/
  published_at: 2026-06-10T00:00:00+00:00
  retrieval_method: WebFetch
secondary_sources: []  # Vendor PSIRT pages not directly retrieved this sweep
originating_vendors:
  - vendor: "Siemens ProductCERT (own-product self-disclosure)"
    products_advisory_class: ["Sinec INS", "Siprotec 5", "WinCC Certificate Manager", "Scalance", "Simatic", "Sinamics"]
  - vendor: "Schneider Electric CPCERT (own-product self-disclosure)"
    products_advisory_class: ["PowerLogic P7", "EasyLogic T150", "Saitel DP RTU/Controller", "EcoStruxure IT Data Center Expert"]
  - vendor: "Phoenix Contact PSIRT (own-product self-disclosure)"
    products_advisory_class: ["CHARX SEC-3xxx charging controllers"]
match_reason:
  watchlist: []
  actors: []
  vulnerabilities:
    - CVE-2025-15467  # OpenSSL RCE re-exposed in Siemens Scalance/Simatic/Sinamics/Sinec
  keywords: [ICS Patch Tuesday, Siemens, ProductCERT, Schneider Electric, Phoenix Contact, Sinec INS, Siprotec 5, WinCC Certificate Manager, Scalance, Simatic, Sinamics, PowerLogic P7, Saitel DP, RTU, EcoStruxure, CHARX SEC, EV charging, OpenSSL]
triage_tags:
  - ics_ot_vendor_patch_disclosures
  - siemens_schneider_phoenix_contact_aggregate
  - openssl_re_exposure_via_siemens_product_lineup
  - ev_charging_controller_class_charx
  - rtu_class_saitel_dp
  - ad_prime_industrial_relevance_indirect_via_factory_automation
  - thin_article_recommend_direct_vendor_psirt_retrieval
  - no_actor_attribution
iocs_extracted: true
iocs_count: 1
text_word_count: 0
promoted: true
promoted_to_finding: finding-2026-06-10-0014-securityweek-ics-patch-tuesday-siemens-schneider-phoenix-contact-june-2026-openssl-re-exposure-cve-2025-15467-factory-automation-class
promoted_at: 2026-06-10T16:30:00-04:00
ttl_expires_at: 2026-09-08T15:47:00-04:00
---

# ICS Patch Tuesday June 2026 — Siemens, Schneider Electric, Phoenix Contact (SecurityWeek aggregation)

**Primary source:** SecurityWeek — "ICS Patch Tuesday: Vulnerabilities Fixed by Siemens, Schneider, Phoenix Contact" — 2026-06-10
**Originating vendors:** Siemens ProductCERT, Schneider Electric CPCERT, Phoenix Contact PSIRT — direct advisory URLs not retrieved this sweep.

## Key claims (per SecurityWeek aggregation)

### Article quality caveat
SecurityWeek aggregation lacks CVSS scores and CVE identifiers (except one OpenSSL reference) — direct vendor PSIRT retrieval recommended for technical depth. This raw-signal records the framing and the product-class coverage.

### Siemens patches
- **Sinec INS** — authenticated command execution, information disclosure, privilege escalation, password exposure cluster.
- **Siprotec 5** — DoS and potential code execution.
- **WinCC Certificate Manager** — sensitive information exposure.
- **CVE-2025-15467 (OpenSSL RCE)** re-exposed via Siemens product lineup: **Scalance, Simatic, Sinamics, Sinec** (and others not enumerated in SW article).

### Schneider Electric patches
- **PowerLogic P7** — DoS and command execution.
- **EasyLogic T150** and **Saitel DP RTU/Controller** — credential exposure.
- **EcoStruxure IT Data Center Expert** — information disclosure.

### Phoenix Contact patches
- **CHARX SEC-3xxx charging controllers** — unauthenticated log download.

### Critical gaps in SW article
- No specific CVSS scores published.
- No CVE identifiers (except CVE-2025-15467 OpenSSL inheritance).
- No exploitation status (ITW or PoC).
- No named victims.
- No IOCs.
- No actor attribution.

## Cross-corpus context

### A&D-prime industrial relevance
- **Siemens Simatic / Scalance / Sinamics** are widely deployed in A&D-prime factory automation:
  - Aircraft / spacecraft assembly lines (Boeing, Airbus, Lockheed Martin Skunk Works).
  - Missile / weapons-system production (RTX Raytheon, Northrop Grumman, L3Harris Aerojet Rocketdyne).
  - Electronic-systems assembly (BAE Systems, L3Harris).
- The OpenSSL RCE (CVE-2025-15467) re-exposure across this Siemens product lineup is a defender priority where A&D primes operate Simatic/Scalance/Sinamics in production.
- **Schneider Saitel DP RTU/Controller** — remote terminal unit class with industrial-automation deployments; less A&D-prime-direct but supply-chain-adjacent.
- **EcoStruxure IT Data Center Expert** — datacenter-class adjacent to the SW HVAC/UPS Claroty research item (also surfaced today; discarded as standalone — see sentinel pm-000 notes).
- **Phoenix Contact CHARX SEC-3xxx EV charging controllers** — EV / facility-charging class, indirect A&D-relevance via facility infrastructure.

### Standing watchlist
- VT-005 (OpenC3 COSMOS) sets the corpus precedent for open-source spacecraft C2 ICS-relevant tracking.
- VT-010 (Yamcs CVE-2026-44632) sets a parallel precedent for spacecraft mission control software.
- This signal is mainstream-ICS / factory-automation class; less novel than VT-005/VT-010 but materially-relevant to operationally-deployed A&D factory environments.

### Dragos status check
- Dragos is the canonical ICS / OT vendor research source (id `dragos` ratified A in source-grades.yaml). Dragos source-health 2026-05-13 noted single failure (404 on dragos.com/blog/feed/); operator-side path identification pending. No Dragos primary on June 2026 ICS Patch Tuesday has been surfaced in corpus this hour.

## FLASH-trigger evaluation

- **Trigger 1 (critical-cve-exploited):** ❌ Insufficient CVSS / ITW detail in SW aggregation.
- **Trigger 5 (ad-sector-campaign):** ❌ Vendor patch cycle, not active campaign.
- **Trigger 6 (zero-day-no-patch):** ❌ Vendor patches available.

Not a FLASH trigger. Brief-track candidate via standing-section ICS lane. Light handling acceptable given thin SW article.

## Extraction notes

- Language: en
- Article type: ICS Patch Tuesday aggregation
- Raw IOC extraction invoked: yes (below)
- Recommended next-pass action: Siemens ProductCERT / Schneider CPCERT / Phoenix Contact PSIRT direct retrieval for CVE + CVSS + ITW detail.

## IOCs (from ioc-extraction skill)

```yaml
attribution_claims: []

cves:
  - cve: CVE-2025-15467
    type: "OpenSSL RCE"
    re_exposed_in_siemens_products:
      - Scalance
      - Simatic
      - Sinamics
      - Sinec
    notes: "Re-exposure via Siemens product lineup; CVE underlying OpenSSL flaw; severity not enumerated in SW article"

vendor_disclosure_class:
  siemens_product_cert:
    own_product: yes
    procedural_grade_class: "A-grade vendor-on-own-product per PSIRT precedent"
    source_grades_yaml_status: "Not yet a dedicated id — recommend addition at provisional A"
  schneider_cpcert:
    own_product: yes
    procedural_grade_class: "A-grade vendor-on-own-product"
    source_grades_yaml_status: "Not yet a dedicated id"
  phoenix_contact_psirt:
    own_product: yes
    procedural_grade_class: "A-grade vendor-on-own-product"
    source_grades_yaml_status: "Not yet a dedicated id"

product_classes_patched:
  siemens:
    - "Sinec INS (network management — authenticated cmd exec / info disclosure / privesc / password exposure)"
    - "Siprotec 5 (protective relay — DoS / code exec)"
    - "WinCC Certificate Manager (HMI/SCADA cert mgmt — info disclosure)"
    - "Scalance + Simatic + Sinamics + Sinec (OpenSSL re-exposure CVE-2025-15467)"
  schneider:
    - "PowerLogic P7 (power monitoring — DoS / cmd exec)"
    - "EasyLogic T150 (power monitoring — credential exposure)"
    - "Saitel DP RTU/Controller (industrial automation RTU — credential exposure)"
    - "EcoStruxure IT Data Center Expert (datacenter mgmt — info disclosure)"
  phoenix_contact:
    - "CHARX SEC-3xxx charging controllers (EV charging — unauthenticated log download)"

ad_prime_industrial_relevance:
  siemens_simatic_scalance_sinamics: "Widely deployed in A&D factory automation (aircraft/spacecraft assembly, missile production, electronic systems)"
  schneider_saitel_dp: "RTU class — supply-chain-adjacent industrial automation"
  ecostruxure_dcim: "Datacenter management — facility-OT class"
  phoenix_contact_charx: "EV charging — facility infrastructure"

network_iocs_extracted:
  domains: []
  ipv4: []
  hashes: []
  notes: "Vendor patch advisories — no campaign IOCs"
```

## Notes for grader

- **Thin article** — SecurityWeek aggregation lacks CVE / CVSS / ITW detail. Recommend grader treat this as awareness-level coverage; vuln-tracker or analyst on-demand direct retrieval of vendor PSIRT pages for any specifically-promoted CVE.
- **No FLASH trigger.**
- **Brief-track via standing-section ICS lane** — light handling.
- **A&D-prime defender relevance** present but indirect via factory-automation product class.
- **Source-grades.yaml** — three new vendor PSIRT additions recommended (Siemens ProductCERT, Schneider CPCERT, Phoenix Contact PSIRT) per the established PSIRT-class A-grade precedent.
