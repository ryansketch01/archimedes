---
raw_id: raw-2026-07-23-am-002
collected_at: 2026-07-23T07:35:00-04:00
run_id: pre-brief-20260723-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek"
  source_url: https://www.securityweek.com/us-warns-of-iranian-hackers-targeting-siemens-schneider-and-rockwell-ics-devices/
  published_at: 2026-07-23T01:28:50-04:00   # 05:28:50 GMT
match_reason:
  watchlist: []
  actors: [CyberAv3ngers, Handala Hack]   # roster #028 + #014, as named by the article
  vulnerabilities: []
  keywords: [Iran, ICS, OT, PLC, Siemens, Schneider, Rockwell, "CISA advisory", "hacktivist persona", Stryker, "Cal Water"]
triage_tags: [non_flash, update_state_change, iran_cyber, tracked_actor_named, ot_ics, ad_sector_structural, anti_noise_prior_coverage]
iocs_extracted: true
iocs_count: 0
text_word_count: 300
promoted: true
promoted_to_finding: finding-2026-07-23-0002    # UPDATE / enrichment finding (state change to finding-2026-07-22-0004): PLC-model/port specificity + source-designated #028/#014 persona context; B2 / likely / single-source veto
promoted_at: 2026-07-23T08:16:00-04:00
prior_coverage:
  - raw-2026-07-22-pm-001   # Iran-linked OT CISA/FBI/EPA advisory revision (raw-signaled 2026-07-22 PM)
  - 2026-07-22-afternoon    # afternoon brief covered the advisory revision
ttl_expires_at: 2026-10-21T07:35:00-04:00
---

# US Iran-linked OT advisory (CISA/FBI/EPA revision) — SecurityWeek relay adds PLC-model + port + persona-attribution detail; names CyberAv3ngers (#028) and Handala (#014) (UPDATE to raw-2026-07-22-pm-001)

**State this window (2026-07-22 17:30 → 2026-07-23 07:30 EDT):** SecurityWeek (Eduard
Kovacs) relayed the **updated US federal advisory** (published 2026-07-22, referenced as
`260722.pdf`) warning that **Iranian-government-linked actors using hacktivist personas**
are targeting ICS/PLC devices. This is an **UPDATE / re-report** of the advisory revision
already raw-signaled 2026-07-22 (raw-2026-07-22-pm-001) and covered in the 2026-07-22
afternoon brief — the net-new content is the media relay's **technique + persona detail**.
Grader to apply anti-noise and fold as an UPDATE into the Iran Cyber Watch standing section.

## Net-new detail this window

- **Two roster actors named** by the relay (recorded as the source's designation, NOT an
  Archimedes-originated attribution — Hard Rule 2):
  - **CyberAv3ngers (#028)** — "made many headlines in the past years for its attacks on
    such systems" (IRGC-CEC OT/ICS actor, per roster).
  - **Handala (#014, Handala Hack / Void Manticore)** — "has taken the lead this year,
    starting with attacks on Stryker." (Aligns with the #014 roster note: Stryker Intune
    MDM mass-wipe ~2026-03.)
- **Targeted PLC models / config software (net-new specificity):**
  - Rockwell Automation — CompactLogix, Micro850, Allen-Bradley; Studio 5000 Logix Designer
  - Schneider Electric — Modicon M340 (BMX P34); EcoStruxure Control Expert
  - Siemens — S7-1200 series; TIA Portal
- **Targeted ports (behavioral observables):** 44818 (EtherNet/IP), 2222, 102 (S7comm),
  502 (Modbus), 22 (SSH).
- **Named victims:** California Water Service (Cal Water), Stryker. **No A&D/DIB prime named.**

## Attribution — inherited from the advisory/relay, not originated (Hard Rule 2)

Source attribution language (verbatim, ≤15 words per Hard Rule 6): *"Iranian government has
been using hacktivist personas to carry out many of the attacks."* The relay attaches the
**CyberAv3ngers** and **Handala** persona labels to specific activity; Archimedes records
these as the source's claims. NO merge, NO hardening of the generic "Iran-linked" framing.
Both actors are already on the roster (#028, #014) — grader/actor-profiler may fold this as
corroborating TTP detail into the Iran Cyber Watch section and the respective dossiers.

## A&D relevance — INDIRECT / structural

OT/ICS targeting of the exact PLC classes (Rockwell/Schneider/Siemens) present in
manufacturing, test-range, and facility SCADA environments of large ITAR enterprises. The
TTP is portable to an A&D-prime OT footprint, but the advisory names water-sector and
medical victims, not A&D primes — A&D relevance remains structural (consistent with the
#028 CyberAv3ngers and #014 Handala dossier framing: Intent held at Ideology, not
Target-Specific).

## FLASH evaluation (pre-brief context, not a FLASH sweep)

- T2 tracked-actor-attribution: named actors are roster (#028, #014) but this is a
  **re-report** of the 2026-07-22 advisory revision (already briefed) — NOT a net-new
  attribution → anti-noise, no FLASH.
- T5 A&D-sector-campaign: no named A&D prime; multi-victim but water/medical sectors →
  does not clear the A&D-sector-campaign bar.

## Extraction notes

- Language: en
- Publisher byline: Eduard Kovacs (SecurityWeek)
- Article type: security news relaying a US federal ICS/OT advisory revision
- Raw IOC extraction invoked: yes — no atomic network IOCs (IPs/domains/hashes) in the
  relay; only PLC product models + targeted ports (behavioral observables, recorded below).
  CISA/FBI/EPA advisory PDF (260722.pdf) NOT directly retrieved this sweep — direct-retrieval
  todo for atomic IOCs + formal advisory identifier + any CVE references.
- Hard Rule 3: no exploit content. Port/PLC detail recorded as defensive observables.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: securityweek-2026-07-23-iran-ot-advisory
  source_url: https://www.securityweek.com/us-warns-of-iranian-hackers-targeting-siemens-schneider-and-rockwell-ics-devices/
  extracted_at: 2026-07-23T11:35:00Z
  extracted_by: collector
  target_actor_id: null    # relay names #028 + #014; grader/actor-profiler to resolve
  text_word_count: 300

indicators: []             # no atomic network IOCs in the relay

behavioral_observables:    # non-atomic; recorded for detection context, not iocs.yaml atoms
  targeted_ports: [44818, 2222, 102, 502, 22]
  targeted_products:
    - "Rockwell Automation CompactLogix / Micro850 / Allen-Bradley (Studio 5000 Logix Designer)"
    - "Schneider Electric Modicon M340 BMX P34 (EcoStruxure Control Expert)"
    - "Siemens S7-1200 (TIA Portal)"

cve_references: []         # none referenced in the relay

attribution_claims:
  - claimed_actor: CyberAv3ngers
    ioc_ids: []
    claimed_by_source: securityweek-2026-07-23-iran-ot-advisory
    attribution_confidence_in_source: "named persona / prior-activity framing (relay of US federal advisory)"
    requires_grading: true
    roster_id: "028"
  - claimed_actor: Handala
    ioc_ids: []
    claimed_by_source: securityweek-2026-07-23-iran-ot-advisory
    attribution_confidence_in_source: "named persona; 'taken the lead this year, starting with Stryker'"
    requires_grading: true
    roster_id: "014"
  - claimed_actor: "Iranian government (hacktivist personas)"
    ioc_ids: []
    claimed_by_source: securityweek-2026-07-23-iran-ot-advisory
    attribution_confidence_in_source: "US federal advisory attribution (generic Iran-linked)"
    requires_grading: true

benign_filtered:
  - value: securityweek.com
    reason: publisher_domain

extraction_warnings:
  - type: prior_coverage
    detail: "Re-report of the 2026-07-22 CISA/FBI/EPA advisory revision (raw-2026-07-22-pm-001, afternoon brief). Grader anti-noise: fold as UPDATE, not net-new finding."
```
