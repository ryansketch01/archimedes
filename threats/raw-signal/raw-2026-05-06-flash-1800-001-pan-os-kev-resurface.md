---
raw_id: raw-2026-05-06-flash-1800-001
collected_at: 2026-05-06T18:08:00-04:00
run_id: flash-sweep-20260506-180000
collection_mode: flash_sweep
sources:
  - source_yaml_id: cisa-kev
    source_name: CISA Known Exploited Vulnerabilities Catalog
    source_url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
    grade: A
    role: originating
    published_at: 2026-05-06T00:00:00-04:00
    note: |
      CVE-2026-0300 added to KEV with dateAdded 2026-05-06. Mandatory federal
      mitigation deadline by Saturday per The Record reporting (specific deadline
      date in JSON; vendor's full patch ETAs run 2026-05-13 / 2026-05-28).
  - source_yaml_id: the-record
    source_name: The Record (Recorded Future)
    source_url: https://therecord.media/palo-alto-warns-of-critical-software-bug-firewalls
    grade: B
    role: relay
    published_at: 2026-05-06T16:33:00-04:00
    note: |
      Article published 2026-05-06 16:33 EDT (within the 2h sweep window).
      Relays CISA KEV addition + adds new claim "Several companies reporting
      exploitation following the release of exploit code" (multi-victim signal
      not present in 06:00 vendor disclosure).
  - source_yaml_id: palo-alto-psirt
    source_name: Palo Alto Networks PSIRT Advisory CVE-2026-0300
    source_url: https://security.paloaltonetworks.com/CVE-2026-0300
    grade: A
    role: originating
    published_at: 2026-05-06T00:00:00-04:00
    note: |
      PSIRT advisory updated 2026-05-06 with: (1) new Threat Prevention ID
      510019 detection signature (PAN-OS 11.1+); (2) clarified workaround
      configuration requirements; (3) confirmed CVSS 9.3; (4) "Limited
      exploitation observed targeting exposed portals." Patch ETAs published:
      PAN-OS 12.1 / 11.2 / 11.1 / 10.2 all on 2026-05-13 and 2026-05-28.
      Note: palo-alto-psirt is not listed in source-grades.yaml; treating as
      A-grade vendor PSIRT (peer of MSRC) per implicit-vendor convention.
      Grader to assign formal grade.
  - source_yaml_id: bleepingcomputer
    source_name: BleepingComputer
    source_url: https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-actively-exploited-firewall-zero-day/
    grade: B
    role: relay
    published_at: 2026-05-06T05:18:16-04:00
    note: |
      Original morning relay; included for completeness — same article surfaced
      again in 18:00 sweep but not the trigger source.
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-0300]
  keywords: [pan-os, palo-alto, kev, cisa-kev, user-id-portal, active-exploitation, zero-day, firewall]
flash_triggers_evaluated:
  trigger-1-critical-cve-exploited:
    fires: true
    detail: |
      CVE-2026-0300, CVSS 9.3, NOW with CISA KEV addition (dateAdded
      2026-05-06) confirming active exploitation per A-grade source. The
      The Record adds "Several companies reporting exploitation" — multi-
      victim signal not previously confirmed. Trigger-1 conditions
      (CVSS >= 9.0 + active exploitation + A-grade source) all met
      independently of the 06:00 vendor-only disclosure.
  trigger-2-tracked-actor-attribution:
    fires: false
    reason: "No actor named in any current source. Hard Rule 2 holds."
  trigger-3-first-party-ioc-hit:
    fires: false
    reason: |
      Splunk -2h sweep across archimedes + defenseclaw_local indices for the
      14 tracked IOCs (3 IPv4 + 4 domains + 3 cloud_service domains + 4
      additional indicators) returned 0 hits. PAN-OS CVE itself produces no
      direct host-side IOC pattern to query against (it is a perimeter
      pre-auth issue).
  trigger-4-tracked-actor-ttp-change:
    fires: false
    reason: "No tracked-actor TTP component."
  trigger-5-ad-sector-campaign:
    fires: false
    reason: |
      No A&D sector targeting confirmed in current reporting. The Record
      describes "several companies" generically, no sector specified, no
      watchlist entity named.
  trigger-6-zero-day-no-patch:
    fires: false
    reason: |
      No longer fires — patch ETAs now published (2026-05-13 / 2026-05-28),
      moving CVE-2026-0300 out of the "no patch" condition. This is itself
      a state change worth surfacing to the grader (downgrades trigger-6
      eligibility but trigger-1 fires harder).
anti_noise_check:
  prior_flash_in_24h:
    - brief_id: flash-2026-05-06-pan-os-cve-2026-0300
      ship_time: 2026-05-06T06:14:00-04:00
      topic: pan-os-cve-2026-0300
  resurface_evaluation:
    documented_resurface_conditions_per_afternoon_brief:
      - second_a_or_b_grade_independent_confirmation
      - new_iocs_published
      - cisa_kev_addition
      - patch_released
    fired_today_at_18:00_sweep:
      - cisa_kev_addition          # confirmed via JSON feed dateAdded 2026-05-06
      - patch_released             # vendor PSIRT now publishes patch ETAs (release dates not yet shipped, but ETAs are new defensive intelligence)
      - new_iocs_published         # arguable: Threat Prevention ID 510019 is a detection-side IOC-equivalent, not a compromise IOC; conservative grader call
    decision: |
      Anti-noise rule 1 ("one FLASH per trigger topic per 24h") does NOT
      bar this raw signal because at least two documented resurface
      conditions fire (KEV addition + patch ETAs published). Per orchestrator
      instruction, the topic remains "covered" but a fresh FLASH evaluation
      is warranted. Briefer/grader to decide whether the 18:00 update ships
      as a standalone FLASH or absorbs into a tomorrow morning UPDATE block.
triage_tags: [flash_candidate, trigger-1-critical-cve-exploited, resurface-event, cisa-kev-addition, vuln-tracking, vendor-psirt-update]
iocs_extracted: true
iocs_count: 4
text_word_count: 1850
promoted: true
promoted_to_finding: finding-2026-05-06-FLASH-0003
promoted_at: 2026-05-06T18:14:00-04:00
ttl_expires_at: 2026-08-04T18:08:00-04:00
---

# CISA KEV adds PAN-OS CVE-2026-0300; Palo Alto PSIRT publishes patch ETAs and new Threat ID

CISA's Known Exploited Vulnerabilities catalog added CVE-2026-0300 (Palo Alto Networks PAN-OS Out-of-bounds Write Vulnerability) on 2026-05-06. The catalog entry confirms active exploitation of the User-ID Authentication Portal service on PA-Series and VM-Series firewalls and triggers the federal mitigation deadline mandate.

In parallel, Palo Alto Networks updated its PSIRT advisory at security.paloaltonetworks.com/CVE-2026-0300 the same day to:

1. Confirm CVSS 9.3 (Critical)
2. Publish patch ETAs for all four affected branches:
   - PAN-OS 12.1 — patches 2026-05-13 and 2026-05-28
   - PAN-OS 11.2 — multiple patches 2026-05-13 and 2026-05-28
   - PAN-OS 11.1 — six patch versions 2026-05-13 and 2026-05-28
   - PAN-OS 10.2 — five patch versions 2026-05-13 and 2026-05-28
3. Add Threat Prevention signature ID 510019 (PAN-OS 11.1+)
4. Clarify the four documented workarounds:
   - Restrict User-ID Authentication Portal access to trusted zones
   - Disable Response Pages in Interface Management Profiles on untrusted/internet-facing interfaces
   - Disable the User-ID Authentication Portal if not required
   - Enable Threat ID 510019

Vendor language quoted (under 15-word limit): "Limited exploitation observed targeting exposed portals; patches incoming for all affected versions."

The Record published a follow-on at 16:33 EDT (https://therecord.media/palo-alto-warns-of-critical-software-bug-firewalls) confirming the KEV addition, the federal Saturday mitigation deadline, and adding the multi-victim claim (under 15-word limit): "Several companies reporting exploitation following the release of exploit code." The Record cites Rapid7 predicting May 13 patch availability for many versions, consistent with the PSIRT ETAs.

The Record additionally notes: "Exploitation was focused on authentication portals that are exposed to untrusted IP addresses or the public internet" — narrows the exposure population from the 06:00 vendor advisory.

No actor attribution in any current source. No A&D sector victims named. No specific IOCs (IPs, hashes, domains) released.

---

## Extraction notes

- Language: en
- Article type: vendor advisory + government KEV catalog + secondary news
- Raw IOC extraction invoked: yes
- Quote-discipline: 15-word limit honored across three sources, one quote per source maximum

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: cve
    value: CVE-2026-0300
    confidence: high
    role: vulnerability
    products: [PAN-OS 10.2, PAN-OS 11.1, PAN-OS 11.2, PAN-OS 12.1, PA-Series firewall, VM-Series firewall]
    cvss: 9.3
    kev: true
    kev_added: 2026-05-06
    patch_status: scheduled
    patch_etas:
      - "2026-05-13"
      - "2026-05-28"
    affected_component: User-ID Authentication Portal
    exploitation: confirmed_active_limited
    source_attribution: ["Palo Alto Networks PSIRT", "CISA KEV", "The Record"]
    actor_attribution: null   # no actor named by any source
    notes: |
      Already tracked in threats/vulnerabilities/_index.yaml as the focus
      of finding-2026-05-06-FLASH-0001. KEV addition is a state change.

  - type: detection_pattern
    value: "PAN Threat ID 510019"
    confidence: high
    role: vendor_detection_signature
    platform: PAN-OS 11.1+
    source_attribution: ["Palo Alto Networks PSIRT"]
    notes: |
      Defensive signature, not a compromise IOC. Useful for detection
      content authoring. Publish to defenders, not to actor profile.

  - type: detection_pattern
    value: "Untrusted-zone access to User-ID Authentication Portal"
    confidence: high
    role: vendor_detection_pattern
    source_attribution: ["Palo Alto Networks PSIRT"]
    notes: |
      Configuration-state pattern. Audit query: enumerate Interface
      Management Profiles where User-ID Auth Portal is reachable from
      non-trusted zones.

  - type: configuration_workaround
    value: "Disable Response Pages in Interface Management Profiles on untrusted/internet-facing interfaces"
    confidence: high
    role: mitigation
    source_attribution: ["Palo Alto Networks PSIRT"]
    notes: "Pre-patch mitigation; defenders should evaluate per environment."

attribution_claims: []
# No actor attribution made in any of the four sources. Hard Rule 2 holds.
# Trigger-2 explicitly does not fire.

splunk_first_party_corroboration:
  query_run: true
  query_window: "-2h to now"
  query_target_iocs: 14    # 3 IPv4 + 4 domains + 3 cloud-service + 4 other (per master-index.yaml IPv4 + domain rows)
  hits_returned: 0
  indices_queried: [archimedes, defenseclaw_local]
  notes: |
    No first-party Splunk hits in the 18:00 sweep window. PAN-OS CVE
    itself does not produce a host-side IOC pattern queryable against
    these indices (perimeter pre-auth vulnerability). Mandiant
    typically publishes follow-on host-side IOCs once they map post-
    exploitation activity; that intel is not yet published.
```
