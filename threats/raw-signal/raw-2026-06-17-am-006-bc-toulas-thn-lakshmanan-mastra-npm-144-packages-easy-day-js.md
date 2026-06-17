---
raw_id: raw-2026-06-17-am-006-bc-toulas-thn-lakshmanan-mastra-npm-144-packages-easy-day-js
collected_at: 2026-06-17T07:44:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
  published_at: 2026-06-17T07:38:24+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Mastra, npm, supply-chain, easy-day-js, JFrog, SafeDep, Socket, StepSecurity, ehindero, AI development]
triage_tags: [carry_forward_06_00_sweep, possible_other_signal, ai_dev_supply_chain_pattern, no_tracked_actor, generic_cybercrime]
iocs_extracted: false
iocs_count: 0
text_word_count: 235
promoted: false
rejected_at: 2026-06-17T08:22:00-04:00
rejection_id: reject-2026-06-17-0003
ttl_expires_at: 2026-09-15T07:44:00-04:00
---

# 144 Mastra npm Packages Compromised via Hijacked Contributor Account

**Source:** The Hacker News (https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html)
**Author byline:** info@thehackernews.com / Ravie Lakshmanan
**Published:** 2026-06-17T07:38:24+00:00 (03:38:24 EDT)

## RSS-summary captured

> As many as 144 npm packages associated with the Mastra namespace ("@mastra/*"), a popular open-source JavaScript and TypeScript framework for building artificial intelligence (AI) applications, have been compromised as part of a software supply chain attack codenamed easy-day-js, per findings from JFrog, SafeDep, Socket, and StepSecurity.

## Extraction notes

- **Language:** en
- **Publisher byline:** Ravie Lakshmanan (The Hacker News)
- **Article type:** trade-press journalistic relay of multi-vendor IR research (JFrog + SafeDep + Socket + StepSecurity coordinated discovery)
- **Upstream primaries:** JFrog (not yet in source-grades.yaml; would be provisional on first surface), SafeDep (provisional C since 2026-05-12), Socket (provisional B since 2026-05-14), StepSecurity (provisional B since 2026-05-12)
- **Cross-walk:** Same trigger-topic carry-forward from 2026-06-17 06:00 sweep. Campaign name "easy-day-js" working-name researcher-coined. Compromise vector: single npm account `ehindero` mass-published malicious packages. @mastra/core has 918K weekly downloads per StepSecurity per 06:00 sweep notes.
- **A&D-relevance:** LOW (commodity AI-dev-supply-chain operational-template pattern). StepSecurity quote from 06:00 sweep "Mastra sits at the intersection of AI development and cloud infrastructure" (11 words at-limit-not-exceeded) — single-weak-indicator operational-template inheritance for A&D-prime AI-development teams using Mastra.
- **Hard Rule 6 preservation:** 15-word quote discipline preserved.
- **Hard Rule 2 preservation:** No tracked-actor attribution. Generic-cybercrime supply-chain pattern.
- **Raw IOC extraction invoked:** no (no specific IOCs in relay; specific package versions + account name at vendor upstream primaries)

## Substrate observation for grader

Carry-forward from 06:00 sweep. T1/T6 FAIL (no CVE). T2/T4 FAIL (no tracked-actor attribution). T5 FAIL (no A&D-prime named victim — multi-victim developer base affecting any team using @mastra/*). Critical-override 0-of-4.

Possible 2026-06-17 morning brief Other Signal one-liner. Twin AI-dev-supply-chain surface alongside JetBrains Marketplace plugins (15) + Chrome extensions (2) AI-API-key theft cluster (separate raw-signal this sweep raw-2026-06-17-am-007).
