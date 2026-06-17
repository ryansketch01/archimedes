---
raw_id: raw-2026-06-17-pm-006
collected_at: 2026-06-17T15:46:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: security-affairs
  source_name: Security Affairs (Pierluigi Paganini)
  source_url: https://securityaffairs.com/193775/hacking/u-s-cisa-adds-widget-factory-joomla-content-editor-jce-flaw-to-its-known-exploited-vulnerabilities-catalog.html
  published_at: 2026-06-17T11:18:04-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-48907]
  keywords: [CISA, KEV, Joomla, Widget Factory, JCE, Content Editor, CVE-2026-48907, BOD-22-01]
triage_tags: [kev_compliance_cohort, other_signal_candidate, deadline_approaching, anti_noise_dedup_candidate]
iocs_extracted: true
iocs_count: 0
text_word_count: 350
promoted: false
rejection_id: reject-2026-06-17-0009
rejected_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:46:00-04:00
---

# U.S. CISA adds Widget Factory Joomla Content Editor flaw to its Known Exploited Vulnerabilities catalog

Security Affairs, Pierluigi Paganini, 2026-06-17 15:18 UTC.

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added Widget Factory Joomla Content Editor (JCE) flaw, tracked as CVE-2026-48907 (CVSS score of 10.0), to its Known Exploited Vulnerabilities (KEV) catalog.

CISA advisory excerpt:

> "A vulnerability in the JCE editor extension for Joomla allows the creation of new editor profiles for unauthenticated users, ultimately resulting in PHP code upload and execution."

CISA categorization:

> "Widget Factory Joomla Content Editor contains an improper access control vulnerability which could allow for upload and execution of PHP code via the creation of new editor profiles for unauthenticated users."

Affected: JCE versions 1.0.0 through 2.9.99.4. Fixed in version 2.9.99.5 (released 2026-06-03). Details of ongoing attacks not disclosed.

Per BOD 22-01, FCEB agencies must address the vulnerability by 2026-06-19 (end of this week — ~T+2d from collection time).

---

## Extraction notes

- Language: en
- Publisher byline: Pierluigi Paganini (SA), A-grade
- Article type: SA relay of CISA KEV addition (already evaluated in 2026-06-17 06:00 + 12:00 FLASH sweeps as anti-noise dedup)
- Anti-noise context: SAME trigger-topic already covered in standing carry-forward cohort. Joomla JCE is consumer/SMB CMS — A&D-relevance LOW. Other Signal one-liner candidate for PM brief KEV-deadline-approaching cohort (CVE-2026-54420 LiteSpeed cPanel mitigation deadline 2026-06-18 ~T+18h; CVE-2026-48907 dueDate 2026-06-19 ~T+2d; CVE-2026-20262 Cisco SD-WAN Manager BOD-22-01 2026-06-29 T-12d).
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
extracted_iocs:
  ipv4: []
  ipv6: []
  domains: []
  urls: []
  hashes: []
  cves:
    - id: CVE-2026-48907
      cvss_v3: 10.0
      vendor: Widget Factory
      product: Joomla Content Editor (JCE)
      cwe_summary: "improper access control → unauthenticated PHP code upload and execution"
      affected_versions: "1.0.0 through 2.9.99.4"
      patched_version: "2.9.99.5 (2026-06-03)"
      kev_added: 2026-06-16
      kev_due_date: 2026-06-19
  attribution_claims: []
```
