---
raw_id: raw-2026-07-14-pm-002
collected_at: 2026-07-14T15:34:40-04:00
run_id: pre-brief-20260714-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/
  published_at: 2026-07-14T12:08:47-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Progress ShareFile, Storage Zone Controller, zero-day, path traversal, emergency shutdown]
triage_tags: [vuln_disclosure, tracked_topic_continuation, patch_released, cve_reserved_unpublished, ad_structural]
iocs_extracted: true
iocs_count: 0
text_word_count: 210
promoted: true
promoted_to_finding: finding-2026-07-14-0005
promoted_at: 2026-07-14T15:59:00-04:00
ttl_expires_at: 2026-10-12T15:34:40-04:00
---

# Progress confirms ShareFile zero-day behind last week's emergency Storage Zone Controller shutdown — patched

Progress Software confirmed that a **high-severity path-traversal zero-day** was behind the emergency shutdown directive it issued last week for ShareFile Storage Zone Controllers (SZC). This is the resolution of a topic already tracked in the Archimedes corpus (raw-2026-07-10-pm-001, raw-2026-07-13-flash-0600-002 — the "credible external security threat" / emergency SZC shutdown).

- **Vulnerability:** Path traversal, classified high-severity. An authenticated administrator could read arbitrary files accessible to the application's service account, write attacker-controlled content to arbitrary directories, or enumerate the server filesystem layout.
- **Affected:** ShareFile Storage Zone Controller versions 5.x and 6.x (all versions).
- **Fixed:** 5.12.5 and 6.0.2 (security updates now released).
- **CVE:** Reserved but not yet published — Progress states publication is scheduled in roughly two weeks.
- **Exploitation:** No confirmed active exploitation. Progress: "we have no indication of unauthorized access to any ShareFile customer account or data" (11 words, Hard Rule 6). Progress received warning "from a credible source"; no actor attributed.

---

## Extraction notes

- Language: en
- Publisher byline: Lawrence Abrams
- Article type: news
- Raw IOC extraction invoked: yes — no atomic IOCs present (no IPs/domains/hashes; CVE reserved-unpublished)
- A&D relevance: structural — ShareFile is a managed file-transfer / secure content-collaboration platform used across regulated enterprises including DIB/supplier environments for CUI-adjacent document exchange; authenticated-admin path traversal on the storage tier is a data-exposure primitive. Corpus continuation of the tracked emergency-shutdown event.
- No actor attribution present; none originated (Hard Rule 2). Vuln-tracker may wish to open a watch entry pending CVE publication (~2 weeks), mirroring the gogs / ServiceNow CVE-pending pattern in watch-config.yaml.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-14-pm-002
  source_url: https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/
  extracted_at: 2026-07-14T15:34:40-04:00
  extracted_by: collector
  target_actor_id: null
  text_word_count: 210

indicators: []

attribution_claims: []

benign_filtered: []

extraction_warnings:
  - type: cve_reserved_unpublished
    ioc_id: null
    detail: "CVE reserved but not yet published (Progress: ~2 weeks). No CVE IOC extractable this sweep. Watch signal for vuln-tracker: CVE publication + potential KEV addition."
```
