---
raw_id: raw-2026-05-08-pm-004
collected_at: 2026-05-08T15:38:00-04:00
run_id: pre-brief-20260508-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: bleepingcomputer
    source_name: "BleepingComputer (Sergiu Gatlan)"
    source_url: https://www.bleepingcomputer.com/news/security/cisa-gives-feds-four-days-to-patch-ivanti-flaw-exploited-as-zero-day/
    source_grade_estimated: B
    role: corroborating
    published_at: 2026-05-08T12:16:32+00:00
    note: |
      BleepingComputer follow-on coverage of Ivanti EPMM CVE-2026-6973.
      Adds federal-deadline framing ("four days to patch"), Shadowserver
      exposure number (800+ Ivanti EPMM appliances exposed online),
      patch versions, and historical context (third major EPMM
      vulnerability in 2026 — prior CVE-2026-1281, CVE-2026-1340
      both exploited).
publish_window: { start: 2026-05-08T07:30:00-04:00, end: 2026-05-08T15:30:00-04:00 }
match_reason:
  watchlist: []
  actors: []
  vulnerabilities:
    - CVE-2026-6973
    - CVE-2026-1281  # historical reference
    - CVE-2026-1340  # historical reference
  keywords:
    - ivanti-epmm
    - cve-2026-6973
    - cisa-kev
    - 4-day-deadline
    - shadowserver-exposure
    - 800-appliances
    - third-2026-epmm-vuln
triage_tags:
  - kev_listed
  - active_exploitation_corroborated
  - vendor_followup_corroboration
  - exposure_quantification
  - anti_noise_repeat_topic
  - same_topic_as_morning_am_005
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    decision: not_triggered_anti_noise_repeat
    rationale: |
      Same CVE topic as morning AM-005 (raw-2026-05-08-am-005). FLASH
      already fired on 2026-05-07T18:00 for this CVE. Anti-noise rule
      "one FLASH per topic per 24h" applies. BleepingComputer adds
      Shadowserver exposure number and federal-deadline timing — folds
      into 16:00 afternoon brief CVE-2026-6973 update block, not a
      fresh FLASH.
  trigger_2_tracked_actor_attribution:
    decision: not_triggered
    rationale: |
      BleepingComputer: "no attribution provided." Search-derived prior
      reporting (CyberScoop) noted that two earlier Ivanti EPMM CVEs
      (CVE-2026-1281, CVE-2026-1340) "have been exploited by a range
      of threat actors, including China- and Iran-attributed groups"
      but that is HISTORICAL context for the prior CVEs, NOT an
      attribution claim for CVE-2026-6973. No tracked actor named
      for CVE-2026-6973.
  trigger_3_first_party_ioc_hit:
    decision: not_triggered
    rationale: "Splunk archimedes/defenseclaw_local clean for Ivanti EPMM markers in 8h window."
  trigger_4_tracked_actor_ttp_change:
    decision: not_triggered
  trigger_5_ad_sector_campaign:
    decision: not_triggered
  trigger_6_zero_day_no_patch:
    decision: not_triggered
    rationale: "Patch available since 2026-05-06 advisory."
iocs_extracted: true
iocs_count: 5
text_word_count: 580
publication_window_match: in_window
promoted: true
promoted_to_finding: finding-2026-05-08-0007
promoted_at: 2026-05-08T16:20:00-04:00
ttl_expires_at: 2026-08-06T15:38:00-04:00
---

# Ivanti EPMM CVE-2026-6973 — BleepingComputer adds Shadowserver exposure number + federal 4-day deadline framing

## Source summary

BleepingComputer published "CISA gives feds four days to patch Ivanti flaw exploited as zero-day" at 2026-05-08T12:16 UTC. Same CVE as morning brief lead and 2026-05-07T18:00 FLASH (raw-2026-05-07-flash-1800-001) — anti-noise repeat. New material:

1. **Federal patch deadline:** "midnight Sunday, May 10" (i.e., 2026-05-11T00:00 EDT — 4 calendar days from KEV listing)
2. **Shadowserver exposure number:** 800+ Ivanti EPMM appliances exposed online
3. **Historical context:** CVE-2026-6973 is the **third major EPMM vulnerability in 2026** following CVE-2026-1281 (January) and CVE-2026-1340 (April), both also exploited
4. **Ivanti's own statement (per BleepingComputer):** "We are aware of very limited exploitation of CVE-2026-6973, which requires admin authentication for successful exploitation"
5. **Patches:** Versions 12.6.1.1, 12.7.0.1, 12.8.0.1
6. **Ivanti credential rotation guidance:** Recommended for previously exploited systems

## Why this matters

**Recurrence pattern:** Three Ivanti EPMM CVEs exploited in 4 months is a meaningful pattern signal. BleepingComputer cites no attribution for CVE-2026-6973, but background reporting (CyberScoop, search-corroborated 2026-05-07/05-08) notes that the prior two 2026 EPMM CVEs were exploited by "China- and Iran-attributed groups." This is historical context for the prior CVEs, not an attribution to CVE-2026-6973 — but it should inform vuln-tracker's posture on Ivanti EPMM as a serial-target product.

**Exposure signal:** 800+ Ivanti EPMM appliances exposed online per Shadowserver. Federal patch deadline is 2026-05-11T00:00 EDT. Patch coverage by deadline is unknown.

**A&D relevance:** Ivanti EPMM is a mobile device management platform widely deployed in regulated environments (federal civilian, DoD contractors, healthcare). A&D primes commonly use EPMM for managing employee mobile devices including BYOD/CYOD; ITAR-regulated estates may use EPMM in classified-network-adjacent roles. The 800+ exposed-online count is a partial proxy for total install base — internal-only deployments are not surveyable but follow similar patch-discipline curves.

## Anti-noise

Same CVE topic as raw-2026-05-08-am-005 (morning), raw-2026-05-08-flash-0000-000 (00:00 sentinel KEV-listing pickup), and raw-2026-05-07-flash-1800-001 (the original FLASH). Three prior raw-signals; this is the fourth. **All productive net-new info should fold into 16:00 brief CVE-2026-6973 update block, not a fresh FLASH.**

## Extraction notes

- Language: en
- Article type: media (BleepingComputer)
- Publisher byline: Sergiu Gatlan
- Raw IOC extraction invoked: yes

## IOCs

```yaml
iocs:
  - type: cve
    value: "CVE-2026-6973"
    role: vulnerability
    product: "Ivanti Endpoint Manager Mobile (EPMM)"
    affected_versions: "12.6.1.x, 12.7.0.x, 12.8.0.0 and earlier"
    fixed_in: "12.6.1.1, 12.7.0.1, 12.8.0.1"
    cvss: 7.2
    kev_added: "2026-05-07"
    kev_due_date: "2026-05-11"
    type: "Improper input validation; admin-authenticated RCE"
    sources: [bleepingcomputer, ivanti-psirt, cisa-kev]

  - type: shadowserver_exposure_count
    value: "~800+ Ivanti EPMM appliances exposed online"
    role: exposure_telemetry
    sources: [bleepingcomputer-citing-shadowserver]
    notes: "Internet-reachable count only — does not include internal-only or NAT-protected deployments."

  - type: cve_related_reference
    value: "CVE-2026-1281"
    role: prior_exploited_vulnerability
    product: "Ivanti EPMM"
    notes: "January 2026 EPMM CVE; exploited per CyberScoop 'China- and Iran-attributed groups.'"
    sources: [bleepingcomputer, cyberscoop-relay]

  - type: cve_related_reference
    value: "CVE-2026-1340"
    role: prior_exploited_vulnerability
    product: "Ivanti EPMM"
    notes: "April 2026 EPMM CVE; exploited per CyberScoop. Both prior CVEs cited as attribution-context for vuln-tracker posture, NOT current CVE attribution."
    sources: [bleepingcomputer, cyberscoop-relay]

  - type: ivanti_mitigation_guidance
    value: "Rotate credentials on EPMM appliances previously suspected of exploitation"
    role: vendor_mitigation_recommendation
    sources: [ivanti-psirt-via-bleepingcomputer]

attribution_claims:
  - claim_text: "no information identifying threat actors or their origin"
    claim_source: bleepingcomputer
    claim_confidence: explicit_non_attribution
    claim_date: 2026-05-08
    notes: "BleepingComputer makes no attribution claim for CVE-2026-6973."
  - claim_text: "China- and Iran-attributed groups" (referring to PRIOR EPMM CVEs CVE-2026-1281 and CVE-2026-1340)
    claim_source: cyberscoop-historical
    claim_confidence: historical_context_only
    notes: |
      This attribution is for prior 2026 EPMM CVEs, NOT for
      CVE-2026-6973. Recorded for context — vuln-tracker may use
      to inform Ivanti EPMM serial-target posture, but should NOT
      be re-cited as CVE-2026-6973 attribution.
```
