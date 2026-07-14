---
raw_id: raw-2026-07-14-pm-007
collected_at: 2026-07-14T15:40:55-04:00
run_id: pre-brief-20260714-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: the-record
  source_name: The Record (Recorded Future News)
  source_url: https://therecord.media/russian-intelligence-compromising-cameras-nato-ukraine-netherlands
  published_at: 2026-07-14T09:55:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [AIVD, MIVD, Russian intelligence, IP cameras, NATO logistics, Ukraine, military espionage]
triage_tags: [nation_state, defense_sector_espionage, government_advisory, generic_attribution_preserve_verbatim, flash_1200_handoff]
iocs_extracted: true
iocs_count: 0
text_word_count: 200
promoted: true
promoted_to_finding: finding-2026-07-14-0010
promoted_at: 2026-07-14T16:04:00-04:00
ttl_expires_at: 2026-10-12T15:40:55-04:00
---

# Dutch AIVD/MIVD advisory: at least one Russian intelligence service compromising internet-connected cameras to spy on NATO military logistics and Ukraine-bound shipments

The Netherlands' General Intelligence and Security Service (**AIVD**) and Military Intelligence and Security Service (**MIVD**) jointly issued an advisory (dated 2026-07-10) that a Russian intelligence service is compromising internet-connected cameras across Europe to surveil military logistics. (Carried forward from the 12:00 FLASH sweep non-FLASH grader queue; formalized to raw-signal this pre-brief.)

**Attribution (preserve verbatim, Hard Rule 2):** the advisory names no specific service — it states only "at least one Russian intelligence service." No APT designation (no APT28, no Sandworm) is asserted by the source. Archimedes originates none.

**Targets:** NATO military logistics routes; weapons shipments destined for Ukraine; Ukrainian military personnel positions; military transport activity in NATO/EU member states.

**Method:** scan the internet for exposed devices; identify IP cameras by manufacturer; exploit weak security — default passwords, outdated firmware, default configurations. Video feeds are then analyzed with image-recognition software to detect military vehicles and cargo.

No CVEs, no atomic IOCs (IPs/domains/hashes), and no named victims were provided in the source.

---

## Extraction notes

- Language: en
- Publisher byline: n/a (The Record staff)
- Article type: news relaying a government (AIVD/MIVD) joint advisory
- Raw IOC extraction invoked: yes — no atomic IOCs present
- A&D relevance: sector / defense-logistics — targets NATO military logistics and Ukraine-bound weapons shipments; relevant to the defense-transport and supplier ecosystem, though no A&D-prime entity is named. Method is opportunistic edge-device compromise (default creds / outdated firmware), not a named-CVE exploit chain.
- Attribution discipline: generic "Russian intelligence service" retained verbatim; do NOT map to a roster actor (APT28 #006 / Sandworm #007) absent an A/B-grade source making that link. Grader/analyst domain if a later vendor attributes.
- No exploit detail (Hard Rule 3); no credentials (Hard Rule 7).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-14-pm-007
  source_url: https://therecord.media/russian-intelligence-compromising-cameras-nato-ukraine-netherlands
  extracted_at: 2026-07-14T15:40:55-04:00
  extracted_by: collector
  target_actor_id: null
  text_word_count: 200

indicators: []

attribution_claims:
  - claimed_actor: "at least one Russian intelligence service (unspecified — no APT designation)"
    ioc_ids: []
    claimed_by_source: aivd-mivd-joint-advisory-2026-07-10 (via the-record)
    attribution_confidence_in_source: "government advisory; service unspecified"
    requires_grading: true

benign_filtered: []

extraction_warnings:
  - type: generic_attribution
    ioc_id: null
    detail: "Source attributes to unspecified Russian intelligence service; no roster-actor mapping asserted. Hard Rule 2 — preserve verbatim, do not upgrade."
```
