---
raw_id: raw-2026-05-07-flash-0000-001
collected_at: 2026-05-07T00:02:30-04:00
run_id: flash-sweep-20260507-000000
collection_mode: flash_sweep
test: false
sources:
  - source_yaml_id: unit42
    source_name: Palo Alto Unit 42
    source_url: https://unit42.paloaltonetworks.com/captive-portal-zero-day/
    source_grade_estimated: A
    role: originating
    published_at: 2026-05-06T00:00:00-04:00
    note: |
      Unit 42 threat brief on CVE-2026-0300 exploitation. Introduces material
      escalation beyond morning PSIRT advisory + 18:00 CISA KEV addition:
      (1) actor cluster CL-STA-1132 ("likely state-sponsored"), (2) four new
      C2/staging IPs, (3) one tooling hash (EarthWorm), (4) ReverseSocks5
      GitHub release URL used as second-stage delivery, (5) detailed
      post-exploitation TTPs (SAML flood failover, log sanitization, AD
      enumeration). None of these IOCs or TTPs were in the morning PSIRT
      advisory or in the 18:00 KEV/Record reporting evaluated in
      raw-2026-05-06-flash-1800-001.
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-0300]
  keywords: [pan-os, cve-2026-0300, captive-portal, cl-sta-1132, earthworm, reversesocks5, saml-flood, post-exploitation, state-sponsored]
candidate_triggers:
  - id: trigger-1-critical-cve-exploited
    fires: true
    detail: |
      CVE-2026-0300 (CVSS 9.3) + Unit 42 confirms exploitation in 2-device
      compromise at single org + A-grade source. Trigger-1 conditions
      independently re-met by Unit 42's originating disclosure. Already
      satisfied by 18:00 sweep but Unit 42 supplies a second A-grade
      independent confirmation with first-hand IR observations.
  - id: trigger-2-tracked-actor-attribution
    fires: false
    reason: |
      Unit 42 names cluster CL-STA-1132 and characterizes as "likely
      state-sponsored" but does NOT map to any actor in _roster.yaml.
      Hard Rule 2 holds — Archimedes does not originate the cross-walk.
      Grader/actor-profiler may flag CL-STA-1132 as candidate-for-tracking.
  - id: trigger-3-first-party-ioc-hit
    fires: false
    reason: |
      Splunk archimedes index queried for all 82 master-index IOCs
      (last 24h, both src_ip/dest_ip + domain fields). Zero hits.
      Result: splunk_clean. Note: the 4 new Unit 42 IPs (67.206.213.86,
      136.0.8.48, 146.70.100.69, 149.104.66.84) are not yet in
      master-index — librarian to add post-promotion. Re-query after
      ingestion is recommended.
  - id: trigger-4-tracked-actor-ttp-change
    fires: false
    reason: "CL-STA-1132 not tracked. No tracked-actor TTP delta."
  - id: trigger-5-ad-sector-campaign
    fires: false
    reason: |
      Unit 42 explicitly states "only limited exploitation" with the
      observed compromise scoped to two firewall devices at a single
      organization. No A&D sector named. No multi-victim claim with
      sector identification.
  - id: trigger-6-zero-day-no-patch
    fires: false
    reason: |
      Patch ETAs published 2026-05-06 by vendor (2026-05-13 / 2026-05-28).
      Trigger-6 condition (patch_available: false) does not hold. State
      already documented in raw-2026-05-06-flash-1800-001.
topic_overlap:
  active_24h_topics:
    - covered_in: raw-2026-05-06-flash-1800-001-pan-os-kev-resurface.md
      topic: cve-2026-0300-pan-os
      relationship: |
        SAME topic but materially escalating per orchestrator instruction.
        18:00 sweep covered KEV addition + patch ETAs. This 00:00 candidate
        adds (a) Unit 42 originating IR-grade analysis, (b) actor cluster
        designation, (c) novel IOC set, (d) novel post-exploitation TTPs.
        Anti-noise rule passes: at least three documented resurface
        conditions fire (new IOCs published, second A-grade independent
        confirmation, novel TTPs published).
    - covered_in: finding-2026-05-06-FLASH-0001
      topic: cve-2026-0300-initial-disclosure
      relationship: parent finding from morning brief
    - covered_in: finding-2026-05-06-FLASH-0003
      topic: cve-2026-0300-kev-resurface
      relationship: parent finding from afternoon resurface
    - covered_in: raw-2026-05-06-flash-1200-001-muddywater-chaos.md
      topic: muddywater-chaos-lure
      relationship: unrelated; no overlap with this signal
  decision: |
    Write fresh raw-signal. Tagged with explicit covered_in lineage
    so grader can decide whether to (a) extend finding-2026-05-06-FLASH-0003,
    (b) promote a new finding-2026-05-07-FLASH-0001 capturing the Unit 42
    layer, or (c) consolidate into morning brief UPDATE block. All three
    paths supported by the data.
splunk_first_party_check:
  query_run: true
  query_window: -24h
  indices_queried: [archimedes]
  iocs_queried: 82
  ioc_categories: [ipv4, domain]
  hits_returned: 0
  result: splunk_clean
  notes: |
    Query covered all current master-index IPv4 + domain indicators
    across both src_ip / dest_ip + domain fields. Zero matches. The
    four Unit 42-published IPs (67.206.213.86, 136.0.8.48, 146.70.100.69,
    149.104.66.84) and the GitHub ReverseSocks5 URL are NEW IOCs not yet
    in master-index — recommend re-query after librarian ingestion.
triage_tags: [flash_candidate, trigger-1-critical-cve-exploited, escalation-vs-prior-flash, second-a-grade-confirmation, novel-iocs, novel-post-exploitation-ttps, vendor-pan-os, possible-state-sponsored-cluster]
iocs_extracted: true
iocs_count: 7
text_word_count: 720
promoted: true
promoted_to_finding: finding-2026-05-07-FLASH-0001
promoted_at: 2026-05-07T00:18:00-04:00
promoted_by: grader
promoted_grading_run_id: flash-grade-20260507-001500
ttl_expires_at: 2026-08-05T00:02:30-04:00
---

# Unit 42 publishes IR-grade analysis of CVE-2026-0300 exploitation; introduces CL-STA-1132 cluster and novel IOCs

## Source summary

Unit 42 ("Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution," 2026-05-06, https://unit42.paloaltonetworks.com/captive-portal-zero-day/) publishes an IR-grade analysis that escalates the public-knowledge state of CVE-2026-0300 beyond the morning PSIRT advisory and the 18:00 CISA KEV addition.

Unit 42 quote (under 15-word limit): "only limited exploitation."

## What the source adds (delta vs. prior 24h coverage)

1. **Activity cluster designation.** Unit 42 tracks the activity as **CL-STA-1132**, characterized as "likely state-sponsored." No nation-state attribution is offered. The cluster is a Unit-42-internal designation, not in `_roster.yaml`, and Archimedes does not originate the cross-walk to any tracked actor (Hard Rule 2).

2. **IR observations.** Two firewall devices compromised at one organization. No sector named. No multi-victim claim. This is consistent with The Record's "several companies" relay but tighter ("limited exploitation," single-org IR observation).

3. **Novel IOCs.** Four IPs not in master-index: 67.206.213.86, 136.0.8.48, 146.70.100.69 (C2 staging), 149.104.66.84. One staging URL: hxxp[:]//146.70.100[.]69:8000/php_sess. One second-stage tool URL: hxxps[:]//github[.]com/Acebond/ReverseSocks5/releases/download/v2.2.0/ReverseSocks5-v2.2.0-linux-amd64.tar[.]gz. One file hash: e11f69b49b6f2e829454371c31ebf86893f82a042dae3f2faf63dcd84f97a584 (Unit 42 labels as EarthWorm).

4. **Novel post-exploitation TTPs.**
   - "SAML flood" technique that triggers HA failover to a secondary firewall device
   - Systematic log sanitization, including crash kernel messages and core dumps
   - Active Directory enumeration targeting domain root and DomainDnsZones objects

These TTPs were not present in any of the four sources processed in raw-2026-05-06-flash-1800-001. Together with the new IOC set, this represents the second A-grade independent confirmation of active exploitation and the first IR-side disclosure.

## What the source does NOT add

- No nation-state name. No tracked-actor link. No A&D sector targeting. No additional victim count or named victim. No new patch ETA changes (the 2026-05-13 / 2026-05-28 schedule from the morning PSIRT advisory remains current).

## Trigger evaluation summary

Of the six FLASH triggers, only Trigger-1 (Critical CVE Exploited) fires, on the basis of a second A-grade independent confirmation of active exploitation accompanied by novel defender-actionable IOCs and TTPs. All other triggers explicitly fail. See `candidate_triggers` block above for line-item rationale.

The 18:00 sweep already shipped a FLASH on the KEV resurface for the same CVE topic. Anti-noise rule (one FLASH per topic per 24h) is bypassed under the same documented resurface-conditions logic the 18:00 sweep used (at least two of: new IOCs published, second A-grade confirmation, novel TTPs published — here all three fire). Grader holds the final call on whether to promote into a fresh FLASH finding, extend FLASH-0003, or roll the Unit 42 layer into a morning UPDATE block.

---

## Extraction notes

- Language: en
- Article type: vendor IR-grade threat brief
- Publisher: Palo Alto Unit 42
- Raw IOC extraction invoked: yes
- Quote-discipline: one quote, 4 words, under 15-word limit honored

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: cve
    value: CVE-2026-0300
    confidence: high
    role: vulnerability
    cvss: 9.3
    kev: true
    kev_added: 2026-05-06
    affected_component: User-ID Authentication Portal (Captive Portal)
    exploitation: confirmed_active_limited
    source_attribution: ["Palo Alto Unit 42", "Palo Alto PSIRT", "CISA KEV"]
    actor_attribution: "CL-STA-1132 (Unit 42 internal cluster, likely state-sponsored, no nation named)"
    notes: "Already tracked. Unit 42 layer adds IR-grade context."

  - type: ipv4
    value: 67.206.213.86
    confidence: high
    role: c2_or_staging
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132
    first_seen: 2026-05
    notes: "New IOC; not in master-index. Defanged in source."

  - type: ipv4
    value: 136.0.8.48
    confidence: high
    role: c2_or_staging
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132
    first_seen: 2026-05
    notes: "New IOC; not in master-index."

  - type: ipv4
    value: 146.70.100.69
    confidence: high
    role: c2_staging
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132
    first_seen: 2026-05
    notes: |
      New IOC. Unit 42 specifically labels as C2 staging.
      Hosts staging endpoint at port 8000/php_sess.

  - type: ipv4
    value: 149.104.66.84
    confidence: high
    role: c2_or_staging
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132
    first_seen: 2026-05
    notes: "New IOC; not in master-index."

  - type: url
    value: "http://146.70.100.69:8000/php_sess"
    confidence: high
    role: c2_staging_endpoint
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132
    notes: "Defanged in source as hxxp[:]//146.70.100[.]69:8000/php_sess."

  - type: url
    value: "https://github.com/Acebond/ReverseSocks5/releases/download/v2.2.0/ReverseSocks5-v2.2.0-linux-amd64.tar.gz"
    confidence: high
    role: second_stage_tooling_delivery
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132
    tool: ReverseSocks5
    notes: |
      Open-source tunneling tool repurposed by attacker. Detection by
      URL-fetch alone produces false positives (legitimate research
      use exists). Recommend correlating with PAN-OS-host process context.

  - type: sha256
    value: e11f69b49b6f2e829454371c31ebf86893f82a042dae3f2faf63dcd84f97a584
    confidence: high
    role: post_exploitation_tooling
    malware: EarthWorm
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132
    notes: |
      EarthWorm is a known publicly available Chinese-developed tunneling
      tool. Use of EarthWorm itself does not constitute nation-state
      attribution. Hard Rule 2 holds.

  - type: detection_pattern
    value: "SAML authentication flood inducing PAN-OS HA failover"
    confidence: high
    role: post_exploitation_ttp
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132

  - type: detection_pattern
    value: "Crash kernel message + core dump scrubbing on PAN-OS host"
    confidence: high
    role: post_exploitation_ttp_anti_forensics
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132

  - type: detection_pattern
    value: "Active Directory enumeration of domain root and DomainDnsZones objects"
    confidence: high
    role: post_exploitation_ttp_recon
    source_attribution: ["Palo Alto Unit 42"]
    cluster: CL-STA-1132

attribution_claims:
  - actor_named: CL-STA-1132
    actor_class: "Unit 42 internal cluster designation"
    nation_state_named: false
    confidence_language: "likely state-sponsored"
    cross_walk_to_roster: null
    archimedes_action: |
      Hard Rule 2 — do not originate cross-walk. Grader / actor-profiler
      may evaluate whether CL-STA-1132 warrants tracking-candidate flag
      for /new-actor consideration. No automated promotion.
```
