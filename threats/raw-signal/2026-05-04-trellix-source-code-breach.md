---
raw_id: raw-2026-05-04-0004
collected_at: 2026-05-04T07:55:00-04:00
run_id: pre-brief-20260504-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer"
  source_url: https://www.bleepingcomputer.com/news/security/trellix-discloses-data-breach-after-source-code-repository-hack/
  published_at: 2026-05-04T12:25:07-04:00
  corroborating_sources: []
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [security-vendor-breach, source-code, supply-chain, edr]
triage_tags: [non_flash, security-vendor-breach, supply-chain-risk, ongoing-investigation]
iocs_extracted: false
iocs_count: 0
text_word_count: 215
promoted: true
promoted_to_finding: finding-2026-05-04-0004
promoted_at: 2026-05-04T15:14:00-04:00
ttl_expires_at: 2026-08-02T07:55:00-04:00
test: false
---

# Trellix discloses breach of "a portion" of source code repository

**Victim:** Trellix (cybersecurity vendor; ~50,000 business and government customers; ~200M endpoints)
**Data accessed:** Portion of source code repository
**Customer/corporate data:** No evidence of compromise per Trellix
**Source code release/distribution process:** No evidence of compromise per Trellix
**Detection date:** Not disclosed
**Statement updated:** 2026-05-04
**Vector:** Not disclosed
**Attribution:** None
**IOCs:** None

## What sources say

Per BleepingComputer (2026-05-04): Trellix confirmed attackers accessed "a portion" of its source code repository. The company says it has found no evidence that "corporate or customer data" was stolen and no evidence its source code release or distribution process was affected. Investigation ongoing with outside forensic experts; law enforcement notified.

## A&D relevance

Indirect but worth tracking:
- Trellix EDR/XDR is deployed in defense-industrial-base environments. Source code exposure for security tooling enables future detection-evasion engineering.
- Pattern memory: prior security-vendor source code breaches (e.g., 2024 EDR vendor incidents) preceded targeted detection-bypass campaigns within 6–12 months.
- No claim yet of which products' source code was touched. Watch for follow-on disclosure naming specific product lines.

## FLASH evaluation

No triggers match. Non-FLASH; ongoing-investigation raw-signal. Re-evaluate if attribution emerges or if A&D customer disclosures follow.

## Extraction notes

- Language: en
- Article type: news (BleepingComputer)
- Source grade per source-grades.yaml: B (BleepingComputer)
- Raw IOC extraction invoked: no — no IOCs in article
- Quote count from BleepingComputer: 2 short paraphrased fragments (4 and 5 words; within Hard Rule 6 limit)
