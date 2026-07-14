---
raw_id: raw-2026-07-14-pm-003
collected_at: 2026-07-14T15:35:55-04:00
run_id: pre-brief-20260714-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/adobe-patches-critical-coldfusion-vulnerabilities/
  published_at: 2026-07-14T13:06:35-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-48318, CVE-2026-48319, CVE-2026-48321, CVE-2026-48322, CVE-2026-48324, CVE-2026-48325, CVE-2026-48327, CVE-2026-48284]
  keywords: [Adobe ColdFusion, Priority 1, code execution, privilege escalation]
triage_tags: [vuln_disclosure, tracked_product_adjacency, patch_released, no_itw_per_vendor]
iocs_extracted: true
iocs_count: 8
text_word_count: 190
promoted: true
promoted_to_finding: finding-2026-07-14-0006
promoted_at: 2026-07-14T16:00:00-04:00
ttl_expires_at: 2026-10-12T15:35:55-04:00
---

# Adobe patches eight critical ColdFusion vulnerabilities (Priority 1) — no ITW claimed, but follows recent exploited ColdFusion cluster

Adobe's July 2026 update addresses **eight critical ColdFusion vulnerabilities** spanning path traversal, code injection, improper input validation, missing authentication, SQL injection, and incorrect authorization. Adobe rated the advisory **Priority 1** (immediate patching advised). Impact: arbitrary code execution and privilege escalation.

- **CVE IDs:** CVE-2026-48318, CVE-2026-48322, CVE-2026-48284, CVE-2026-48321, CVE-2026-48325, CVE-2026-48319, CVE-2026-48324, CVE-2026-48327.
- **Fixed versions:** ColdFusion 2025 Update 11 and ColdFusion 2023 Update 22 (resolve all eight).
- **CVSS:** not provided in the source.
- **Exploitation:** Adobe "is not aware of any of these vulnerabilities being exploited in the wild." SecurityWeek notes context: ~2 weeks prior, Adobe patched ColdFusion flaws that attackers began exploiting shortly after disclosure.

Corpus adjacency: Archimedes already tracks Adobe ColdFusion via **VT-017 (CVE-2026-48282, max-severity unauth RCE, active-exploitation-observed per KEVIntel + CCCS, finding-2026-07-06-flash-1629-0001)**. This new July cluster is the same product family and warrants vuln-tracker cross-reference — the Priority-1 rating plus Adobe's own note on the recent exploited-shortly-after-disclosure pattern makes rapid exploitation of one or more of these eight a live watch signal.

---

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire
- Article type: news
- Raw IOC extraction invoked: yes — 8 CVE IOCs
- A&D relevance: structural — ColdFusion is an internet-facing application-server platform; unauth/RCE-class flaws on it are perimeter-exposure primitives. Adjacent to tracked VT-017.
- No actor attribution; none originated (Hard Rule 2). No exploit detail copied (Hard Rule 3).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-14-pm-003
  source_url: https://www.securityweek.com/adobe-patches-critical-coldfusion-vulnerabilities/
  extracted_at: 2026-07-14T15:35:55-04:00
  extracted_by: collector
  target_actor_id: null
  text_word_count: 190

indicators:
  - id: raw-cve-2026-48318
    type: cve
    value: CVE-2026-48318
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: null
    related_malware: []
    source_brief: raw-2026-07-14-pm-003
    context_excerpt: "One of 8 critical ColdFusion CVEs (path traversal / code injection / SQLi / auth flaws); Priority 1; no ITW per Adobe"
    attribution_in_text: null
    notes: "Fixed in ColdFusion 2025 u11 / 2023 u22"
  - id: raw-cve-2026-48319
    type: cve
    value: CVE-2026-48319
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: null
    related_malware: []
    source_brief: raw-2026-07-14-pm-003
    context_excerpt: "Critical ColdFusion July 2026 cluster"
    attribution_in_text: null
    notes: null
  - id: raw-cve-2026-48321
    type: cve
    value: CVE-2026-48321
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: null
    related_malware: []
    source_brief: raw-2026-07-14-pm-003
    context_excerpt: "Critical ColdFusion July 2026 cluster"
    attribution_in_text: null
    notes: null
  - id: raw-cve-2026-48322
    type: cve
    value: CVE-2026-48322
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: null
    related_malware: []
    source_brief: raw-2026-07-14-pm-003
    context_excerpt: "Critical ColdFusion July 2026 cluster"
    attribution_in_text: null
    notes: null
  - id: raw-cve-2026-48324
    type: cve
    value: CVE-2026-48324
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: null
    related_malware: []
    source_brief: raw-2026-07-14-pm-003
    context_excerpt: "Critical ColdFusion July 2026 cluster"
    attribution_in_text: null
    notes: null
  - id: raw-cve-2026-48325
    type: cve
    value: CVE-2026-48325
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: null
    related_malware: []
    source_brief: raw-2026-07-14-pm-003
    context_excerpt: "Critical ColdFusion July 2026 cluster"
    attribution_in_text: null
    notes: null
  - id: raw-cve-2026-48327
    type: cve
    value: CVE-2026-48327
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: null
    related_malware: []
    source_brief: raw-2026-07-14-pm-003
    context_excerpt: "Critical ColdFusion July 2026 cluster"
    attribution_in_text: null
    notes: null
  - id: raw-cve-2026-48284
    type: cve
    value: CVE-2026-48284
    defanged_original: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: ambiguous
    campaign: null
    related_malware: []
    source_brief: raw-2026-07-14-pm-003
    context_excerpt: "Critical ColdFusion July 2026 cluster"
    attribution_in_text: null
    notes: null

attribution_claims: []

benign_filtered: []

extraction_warnings:
  - type: cvss_absent
    ioc_id: null
    detail: "No CVSS scores in source; vuln-tracker should retrieve from NVD when records populate. Cross-reference VT-017 (CVE-2026-48282) same product family."
```
