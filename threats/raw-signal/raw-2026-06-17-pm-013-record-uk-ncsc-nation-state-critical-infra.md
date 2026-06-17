---
raw_id: raw-2026-06-17-pm-013
collected_at: 2026-06-17T15:52:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: the-record
  source_name: The Record from Recorded Future News
  source_url: https://therecord.media/britain-nation-state-cyberattacks-richard-horne-rusi
  published_at: 2026-06-17T13:55:00-04:00
match_reason:
  watchlist: [aerospace-defense]
  actors: []
  vulnerabilities: []
  keywords: [NCSC, Richard Horne, Britain, critical infrastructure, nation-state, prepositioning, kinetic targeting, RUSI]
triage_tags: [policy_announcement, critical_infrastructure_watch, nation_state_prepositioning, strategic_signaling, ad_sector_strategic_relevance]
iocs_extracted: true
iocs_count: 0
text_word_count: 300
promoted: false
rejection_id: reject-2026-06-17-0016
rejected_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:52:00-04:00
---

# Hostile states behind three-quarters of attacks on Britain's critical infrastructure, cyber chief warns

The Record from Recorded Future News, 2026-06-17 17:55 UTC.

NCSC CEO Richard Horne warned that "kinetic targeting in any conflict tomorrow will be based on intelligence gathered today" and that nation-state adversaries were "prepositioning" throughout British critical infrastructure.

(Article body not fully retrieved — RSS summary captures core framing.)

---

## Extraction notes

- Language: en
- Publisher byline: The Record (uncredited)
- Article type: News report on NCSC CEO Richard Horne RUSI speech
- T-gate evaluation:
  - T1 FAIL no specific CVE
  - T2 FAIL no specific roster-tracked actor named in the summary
  - T3 FAIL no first-party IOC hit
  - T4 FAIL not a tracked-actor TTP change
  - T5 PASS-MARGINAL — critical infrastructure adjacent to A&D-prime (A&D primes are part of CI-defined sectors but NOT specifically named UK A&D-prime victims)
  - T6 FAIL no CVE
- Critical override 0-of-4 → non-FLASH-eligible
- Strategic-signaling content: NCSC chief's "prepositioning" + "kinetic targeting" framing — restates the Volt-Typhoon-shaped strategic threat hypothesis. This is policy signaling, not new incident substrate.
- Possible PM brief Other Signal one-liner: UK NCSC chief flags ¾ of CI attacks as state-linked, warns of prepositioning ahead of "kinetic targeting." 
- A&D-relevance: HIGH strategic relevance — A&D primes are CI-adjacent and UK is Five Eyes ally; NCSC framing reinforces the threat picture for US A&D defenders considering parallel exposure (Volt Typhoon, Salt Typhoon prepositioning patterns).
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
    - actor: "hostile states / nation-state adversaries"
      source: Richard Horne (NCSC CEO) via The Record
      preservation_note: "NCSC framing recorded verbatim. Archimedes does NOT cross-walk to APT28 / Volt Typhoon / Salt Typhoon / Lazarus / APT41 without independent A-grade IR-vendor attribution per Hard Rule 2."
  strategic_observations:
    - "75% of attacks on British CI from nation-state adversaries (per Horne)"
    - "Prepositioning observed across CI (per Horne)"
    - "Kinetic-conflict-readiness intelligence-collection framing"
```
