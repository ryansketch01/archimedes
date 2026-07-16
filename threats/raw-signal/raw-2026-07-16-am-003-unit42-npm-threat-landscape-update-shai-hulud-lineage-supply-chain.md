---
raw_id: raw-2026-07-16-am-003
collected_at: 2026-07-16T07:35:00-04:00
run_id: pre-brief-20260716-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: unit42
  source_name: Palo Alto Networks Unit 42
  source_url: https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
  published_at: 2026-07-15T23:00:33+00:00
match_reason:
  watchlist: []
  actors: ["001"]
  vulnerabilities: [VT-006]
  keywords: [npm, supply-chain, Shai-Hulud, worm propagation, CI/CD persistence]
  thematic_link: "Living Unit 42 npm-supply-chain landscape doc, 'Updated July 15'. Ties to tracked VT-006 (Mini Shai-Hulud / CVE-2026-45321, actor #001 TeamPCP) Shai-Hulud family lineage and VT-009 (Nx Console). Co-occurs this window with MSTIC @asyncapi compromise (raw-2026-07-16-am-001)."
triage_tags: [supply_chain, npm, shai_hulud_lineage, a_grade_vendor, landscape_update, non_flash, low_priority]
iocs_extracted: true
iocs_count: 0
text_word_count: 90
promoted: false
rejected_at: 2026-07-16T08:24:00-04:00
rejection_id: reject-2026-07-16-0001
rejection_summary: "Anti-noise / no-net-new: Unit 42 (A) living-doc refresh, no atomic IOC/CVE/new campaign/new actor; redundant with tracked VT-006 Shai-Hulud lineage. Referenced as environmental context in finding-2026-07-16-0001 (AsyncAPI/Miasma). Reject on redundancy, not grade (would-be A3)."
ttl_expires_at: 2026-10-14T07:35:00-04:00
---

# The npm Threat Landscape: Attack Surface and Mitigations (Updated July 15)

**Source:** Palo Alto Networks Unit 42 (grade A), living document "Updated July 15" (2026),
published/refreshed 2026-07-15T23:00 UTC.

Unit 42 analyzes npm supply-chain evolution post-Shai-Hulud, covering wormable malware,
CI/CD persistence, multi-stage attacks, credential harvesting, obfuscation, GitHub-hosted
payloads, and worm propagation. Categorized by Unit 42 under "High Profile Threats" and
"Malware" (tags: Credential Harvesting, GitHub, npm packages, obfuscation, payload, supply
chain, worm propagation).

Full body not retrieved this pass (RSS summary only). This is a maintained/updated landscape
reference rather than a single net-new campaign disclosure.

---

## Extraction notes

- Language: en
- Publisher byline: Unit 42 (id: unit42, grade A)
- Article type: vendor threat-landscape reference (living document; "Updated July 15")
- Raw IOC extraction invoked: yes — no atomic IOCs in the RSS summary (full body not retrieved).
- Grader note: captured as context/pairing for the npm-supply-chain cluster this window
  (alongside MSTIC @asyncapi, raw-2026-07-16-am-001). Relevance is to the tracked Shai-Hulud
  family lineage (VT-006 Mini Shai-Hulud / TeamPCP #001) — NOT a new campaign attribution.
  Anti-noise: this is an update to an existing Unit 42 living doc; the briefer/grader should
  weigh whether it adds anything beyond the already-tracked VT-006 lineage. No IOCs, no CVE,
  no named A&D victim, no new actor. Low priority; likely context-only.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-16-am-003
  source_url: https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
  extracted_at: 2026-07-16T11:35:00Z
  extracted_by: collector
  target_actor_id: null
  text_word_count: 90

indicators: []

attribution_claims: []

benign_filtered:
  - value: unit42.paloaltonetworks.com
    reason: reference_site_publisher
  - value: github.com
    reason: reference_site

extraction_warnings:
  - type: source_text_too_short
    detail: "RSS summary only (~90 words); no atomic indicators present. Full landscape-doc body not retrieved. If grader wants IOCs, re-fetch the Unit 42 primary."
```
