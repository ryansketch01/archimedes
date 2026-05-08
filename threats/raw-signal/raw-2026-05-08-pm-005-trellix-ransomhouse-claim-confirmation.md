---
raw_id: raw-2026-05-08-pm-005
collected_at: 2026-05-08T15:39:00-04:00
run_id: pre-brief-20260508-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: bleepingcomputer
    source_name: "BleepingComputer (Bill Toulas)"
    source_url: https://www.bleepingcomputer.com/news/security/trellix-source-code-breach-claimed-by-ransomhouse-hackers/
    source_grade_estimated: B
    role: corroborating_extension
    published_at: 2026-05-08T13:23:23+00:00
    note: |
      Material extension of morning AM-007 (raw-2026-05-08-am-007). The
      morning piece (also BleepingComputer) was the initial Trellix
      source-code-breach disclosure relay. This afternoon's piece adds
      the ATTRIBUTION: RansomHouse has now publicly claimed the breach
      and posted screenshots on their darkweb extortion portal. This
      transforms the morning unattributed-breach signal into an
      attributed-extortion-claim event.
publish_window: { start: 2026-05-08T07:30:00-04:00, end: 2026-05-08T15:30:00-04:00 }
match_reason:
  watchlist: []
  actors:
    - RansomHouse  # NOT in current _roster.yaml
  vulnerabilities: []
  keywords:
    - trellix
    - ransomhouse
    - source-code-breach
    - extortion-claim
    - data-encryption
    - mario-encryptor
    - mragent
    - april-17-intrusion
    - mcafee-fireeye-history
triage_tags:
  - new_actor_claim_against_security_vendor
  - source_code_compromise_supply_chain_risk
  - actor_not_in_roster_candidate_intake
  - vendor_followup_corroboration
  - same_topic_as_morning_am_007
  - attribution_emerging
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    decision: not_triggered
    rationale: "No CVE involved."
  trigger_2_tracked_actor_attribution:
    evaluation: |
      Conditions:
      - article_attributes_activity_to_actor: TRUE — RansomHouse
        publicly claimed.
      - attributed_actor in _roster.yaml: FALSE — RansomHouse is NOT
        in the current Archimedes _roster.yaml. Per Hard Rule:
        FLASH-2 specifically requires a tracked actor.
      Trigger does not fire — but this is a candidate actor for
      /new-actor intake (not auto-promoted by collector).
    decision: not_triggered_actor_not_in_roster
    rationale: |
      RansomHouse not currently in roster. BleepingComputer notes
      RansomHouse "launched in 2022 as a data-extortion operation,"
      previous high-profile victim Askul Corporation (740,000 records
      stolen). Group has its own encryption tools 'Mario' and 'MrAgent'.
      A&D-target-profile relevance is moderate (security-vendor
      compromise has supply-chain implications) but not Tier-1 prime.
      Recommend operator consider /new-actor RansomHouse in next
      session — but the FLASH-2 trigger as defined requires roster
      membership and does not fire here.
  trigger_3_first_party_ioc_hit:
    decision: not_triggered
    rationale: "No IOCs published; Splunk archimedes/defenseclaw_local clean."
  trigger_4_tracked_actor_ttp_change:
    decision: not_triggered
  trigger_5_ad_sector_campaign:
    decision: not_triggered
    rationale: "Trellix is a cybersecurity vendor (McAfee Enterprise + FireEye merger), not directly A&D. Indirect supply-chain relevance only."
  trigger_6_zero_day_no_patch:
    decision: not_triggered
iocs_extracted: true
iocs_count: 3
text_word_count: 580
publication_window_match: in_window
promoted: true
promoted_to_finding: finding-2026-05-08-0008
promoted_at: 2026-05-08T16:26:00-04:00
ttl_expires_at: 2026-08-06T15:39:00-04:00
---

# Trellix source code breach — RansomHouse publicly claims; April 17 intrusion date now disclosed

## Source summary

BleepingComputer published "Trellix source code breach claimed by RansomHouse hackers" at 2026-05-08T13:23 UTC. The piece materially extends morning AM-007 (raw-2026-05-08-am-007), which was the initial unattributed-breach disclosure relay. Today's piece confirms attribution and adds technical/timeline details.

## Material new content versus morning AM-007

| Element | Morning AM-007 (2026-05-01 disclosure) | This afternoon (PM-005) |
|---|---|---|
| Attribution | None — Trellix said "investigating" | **RansomHouse publicly claimed** |
| Intrusion date | Not disclosed | **April 17, 2026** (per RansomHouse claim) |
| Encryption status | Trellix said "no evidence source code release/distribution affected" | **RansomHouse says "resulted in data encryption"** |
| Public proof | None | **RansomHouse posted screenshots of "appliance management system" access on darkweb portal** |
| Trellix follow-up statement | Initial advisory only | **"aware of claims of responsibility for the attack and are looking into it"** |

## RansomHouse profile (per BleepingComputer)

- **Origin:** Launched 2022 as data-extortion operation (no encryption)
- **Evolution:** Expanded to include encryption tools 'Mario' and 'MrAgent'
- **Notable prior victim:** Askul Corporation — stole 740,000 customer records
- **TTPs:** Standard pattern — public extortion portal listing, screenshots as proof, escalation toward data leak if no payment

## Why this matters for A&D target profile

**Supply chain pivot risk:**
- Trellix is the post-merger entity from McAfee Enterprise + FireEye (NDR/EDR + endpoint legacy). Trellix products are widely deployed in **federal, DoD, and A&D environments** as endpoint defense and threat intelligence.
- Source code compromise of a security vendor creates two potential supply-chain risks:
  1. **Update / patch poisoning** if attacker can move from source repo to build/release pipeline. Trellix says no evidence of this.
  2. **Detection-bypass discovery:** With source code, an attacker can identify which behaviors Trellix detects and engineer evasion.
- The April 17 intrusion date plus May 8 public claim = ~3 weeks between intrusion and extortion claim. Standard data-extortion operating tempo.

**Authenticity caveat:** BleepingComputer notes "could not confirm the authenticity of the data" in RansomHouse's screenshots. Trellix has not confirmed the encryption claim.

## Actor-roster candidate

RansomHouse is **not in the current _roster.yaml**. Recommend operator consider /new-actor intake. Profile-creation triggers per CLAUDE.md:
- Active extortion campaign with public claim
- Tier-2 cybercriminal RaaS with encryption tooling
- Prior 740K-record victim establishes track record
- Now claimed against a major security vendor (Trellix) with potential A&D supply-chain implications

Collector does not promote — flagging for operator decision.

## Anti-noise observation

Same topic as morning AM-007. Today's piece adds attribution + intrusion date — material new content justifies fresh raw-signal. Grader clusters with AM-007 at promotion. Briefer should treat as Trellix update block in 16:00 afternoon brief, NOT a fresh standalone item.

## Extraction notes

- Language: en
- Article type: media (BleepingComputer)
- Publisher byline: Bill Toulas
- Raw IOC extraction invoked: yes

## IOCs

```yaml
iocs:
  - type: actor_alias_candidate
    value: "RansomHouse"
    role: extortion_group
    associated_tooling: ["Mario (encryptor)", "MrAgent"]
    notable_prior_victim: "Askul Corporation (740,000 records, data extortion)"
    notes: "Not in current _roster.yaml. Candidate for /new-actor intake."
    sources: [bleepingcomputer]

  - type: incident_timeline
    value: "Trellix intrusion 2026-04-17; public extortion claim 2026-05-08"
    role: incident_metadata
    sources: [bleepingcomputer, ransomhouse-darkweb-portal-claim]
    notes: "21 days from intrusion to public claim."

  - type: extortion_evidence_claim
    value: "Screenshots of Trellix appliance management system on RansomHouse darkweb portal"
    role: evidence
    notes: "Authenticity not independently confirmed by BleepingComputer."
    sources: [bleepingcomputer]

attribution_claims:
  - claim_text: "RansomHouse claimed responsibility for the Trellix source code breach"
    claim_source: bleepingcomputer
    claim_confidence: actor_self_claim_unverified
    claim_date: 2026-05-08
    notes: |
      RansomHouse self-claim via darkweb portal. Trellix has not
      confirmed. BleepingComputer cannot confirm authenticity of
      screenshots. Grader treats as B-grade attribution at best
      (actor self-claim alone is not strong attribution); analyst
      may discount further pending Trellix confirmation or independent
      validation.
```
