---
raw_id: raw-2026-05-18-pm-005
collected_at: 2026-05-18T15:45:00-04:00
run_id: pre-brief-20260518-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/millions-impacted-across-several-us-healthcare-data-breaches/
  published_at: 2026-05-18T08:58:44-04:00
  author: Eduard Kovacs
match_reason:
  watchlist: []  # Healthcare NOT A&D
  actors: []  # Explicit no-attribution preserved
  vulnerabilities: []
  keywords: [healthcare, HHS-OCR, breach-tracker, no-attribution-claimed]
triage_tags: [sector_misaligned_mention_class, explicit_no_attribution_preserved, anti_noise_partial_already_12_00_flash_ac3683d, sector_context_completeness]
iocs_extracted: false
iocs_count: 0
text_word_count: 230
promoted: false
rejected_at: 2026-05-18T16:18:00-04:00
rejection_id: reject-2026-05-18-0002
ttl_expires_at: 2026-08-16T15:45:00-04:00
---

# Millions Impacted Across Several US Healthcare Data Breaches

SecurityWeek (Eduard Kovacs), 2026-05-18 08:58 EDT.

Aggregate of six recently disclosed US healthcare data breaches added to the HHS OCR breach tracker:

- NYC Health and Hospitals Corporation: 1.8M individuals (breach detected 2026-02-02; unauthorized access November 2025–February 2026)
- Erie Family Health Centers (Chicago, IL): 570K individuals (attack detected January 2026; access 2025-12-10 → late January 2026)
- Florida Physician Specialists: 276K individuals (two-day unauthorized access November 2025)
- Coastal Carolina Health Care (NC): ~110K individuals (intrusion detected over one year prior to disclosure)
- Western Orthopaedics (CO): ~110K individuals (timeline not specified)
- Nacogdoches Memorial Hospital (TX): 2.5M individuals (previously reported as 250K — revised upward)

Aggregate impact: ~5.4M records.

Verbatim attribution language preserved per Hard Rule 2: "None of these healthcare data breaches appears to have been claimed by known cybercrime groups."

Regulatory: HHS Office for Civil Rights (OCR) Breach Portal — ocrportal.hhs.gov.

A&D / defense / Tier-1 prime relevance: NONE. Healthcare sector, not A&D watchlist.

---

## Extraction notes

- Language: en
- Publisher byline: Eduard Kovacs
- Article type: aggregate breach roundup
- Raw IOC extraction invoked: not applicable (no IOCs in source body; no actor named)
- Net-new vs. 12:00 FLASH ac3683d: Same item; FLASH evaluated as healthcare-sector-misaligned not-A&D-watchlist; explicit "not claimed by known cybercrime groups" language preserved verbatim per Hard Rule 2.
- Hard Rule 2 preservation: Verbatim "None of these healthcare data breaches appears to have been claimed by known cybercrime groups" (15 words at the policy limit) — preserved exactly.
- Mention-class only for sector-context completeness. NOT a finding-promotion candidate.
- Flagged for grader as sector-context Other Signal mention candidate for 16:00 afternoon brief.

## IOCs

```yaml
iocs: []  # No actor / IP / domain / hash / CVE published.

attribution_claims:
  - claim: "None of these healthcare data breaches appears to have been claimed by known cybercrime groups."
    claimed_by: SecurityWeek (Eduard Kovacs)
    confidence_language: "appears to have been claimed by"  # hedge preserved
    actor_named: null
    archimedes_position: "Preserve verbatim per Hard Rule 2 (no first-time attribution origination). 15 words at quote limit."

sector_relevance:
  a_and_d_watchlist: false
  sector: healthcare
  regulatory_reporting_class: HHS OCR Breach Portal (ocrportal.hhs.gov)
```
