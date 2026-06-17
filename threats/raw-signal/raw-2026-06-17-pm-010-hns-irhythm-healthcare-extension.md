---
raw_id: raw-2026-06-17-pm-010
collected_at: 2026-06-17T15:50:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: helpnetsecurity
  source_name: Help Net Security (Sinisa Markovic)
  source_url: https://www.helpnetsecurity.com/2026/06/17/irhythm-data-breach-patient-health-information-stolen/
  published_at: 2026-06-17T10:51:03-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [iRhythm, healthcare, Novo Nordisk, breach, PHI, patient data, extortion]
triage_tags: [non_flash, out_of_a&d_scope, healthcare, anti_noise_dedup_candidate]
iocs_extracted: true
iocs_count: 0
text_word_count: 250
promoted: false
rejection_id: reject-2026-06-17-0013
rejected_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:50:00-04:00
---

# Another healthcare firm attacked days after Novo Nordisk breach

Help Net Security, Sinisa Markovic, 2026-06-17 14:51 UTC.

Medical technology company iRhythm Holdings disclosed a cyberattack involving certain third-party-hosted business applications that resulted in the theft of patient protected health information, proprietary data, and other personal data. The company discovered unauthorized activity on June 8, 2026, and launched an investigation with the assistance of external cybersecurity experts. A day later, a threat actor claimed to have obtained "sensitive information, including proprietary data, patient protected health information and other personal information" and demanded payment... (article continues).

---

## Extraction notes

- Language: en
- Publisher byline: Sinisa Markovic (HNS), B-grade
- Article type: HNS breach disclosure extension
- Anti-noise context: SAME trigger-topic as reject-2026-06-16-0003 (iRhythm 12M healthcare patient breach). Already rejected as out-of-A&D-scope healthcare. This is HNS-Markovic extension piece, non-substrate-shifting.
- Discarded out-of-A&D-scope healthcare
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
extracted_iocs:
  ipv4: []
  ipv6: []
  domains: []
  urls: []
  hashes: []
  email_addresses: []
  attribution_claims:
    - actor: "threat actor (uncategorized)"
      source: iRhythm disclosure via HNS
```
