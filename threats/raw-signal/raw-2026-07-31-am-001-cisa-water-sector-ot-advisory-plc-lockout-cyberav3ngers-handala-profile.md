---
raw_id: raw-2026-07-31-am-001
collected_at: 2026-07-31T07:34:00-04:00
run_id: pre-brief-20260731-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/cisa-urges-water-sector-to-protect-ot-after-coordinated-attacks-on-plcs/
  published_at: 2026-07-30T18:18:36-04:00
  originating_authority: "CISA (A-grade gov) — SecurityWeek (Mike Lennon) is the relay; CISA alert 2026-07-30 references advisory AA26-097A for IOCs"
match_reason:
  watchlist: []              # water/wastewater = critical infrastructure, NOT aerospace & defense; no watchlist entity named
  actors: []                 # NO formal attribution — CyberAv3ngers (#028) + Handala (#014) named only as PROFILE-FIT, not attributed (Hard Rule 2)
  vulnerabilities: []        # no CVE named in the advisory relay
  keywords: [OT, ICS, PLC, water utility, wastewater, critical infrastructure, CISA, AA26-097A, coordinated attack, disruption]
triage_tags: [non_flash, ot_ics, critical_infra, cisa_advisory, update, roster_profile_fit, grader_queue, next_scheduled_brief]
iocs_extracted: true
iocs_count: 0
text_word_count: 0
promoted: true
promoted_as: update                                # authoritative-advisory UPDATE to an existing finding, not a net-new finding
promoted_to_finding: finding-2026-07-29-0001
promoted_update_id: upd-2026-07-31-0001
promoted_at: 2026-07-31T08:16:00-04:00
ttl_expires_at: 2026-10-29T07:34:00-04:00
related_raw_signals: [raw-2026-07-29-flash-0600-001]   # Minnesota water OT campaign originating raw-signal (promoted to finding-2026-07-29-0001)
---

# CISA Urges Water Sector to Protect OT After Coordinated Attacks on PLCs

**Below-FLASH-bar, raw-signaled for the 2026-07-31 morning-brief grader queue as an UPDATE
to the tracked Minnesota water-utility OT campaign (raw-2026-07-29-flash-0600-001 →
finding-2026-07-29-0001).** This is the CISA advisory follow-on the 06:00 EDT FLASH sweep
held below-bar for the morning grader. A-grade government authority + roster-actor
profile-fit mentions + PLC-targeting detail make it grader-relevant despite water sector
being outside the A&D watchlist.

Window: 2026-07-30T17:30 → 2026-07-31T07:30 EDT. Source: SecurityWeek (Mike Lennon,
published 2026-07-30 18:18 EDT, in-window), relaying a CISA alert dated 2026-07-30.

## What the source reports

- **CISA guidance (3 immediate actions):** (1) disconnect PLCs from the internet — route
  remote access through VPN/gateway instead; (2) enable password protection and change
  default credentials; (3) allowlist IP addresses to known devices only. CISA also
  recommends maintaining clean PLC backups and reviewing **advisory AA26-097A** for
  indicators of compromise.
- **The intrusions (context):** a coordinated attack struck **more than 30 community water
  systems** on **2026-07-26 to 2026-07-27**. Named municipalities: Maple Plain, Braham,
  South St. Paul, Plymouth (Minnesota). Some automated control functions were disrupted;
  contingency procedures maintained operations; drinking water remained safe.
- **Attack technique:** attackers **modified passwords to lock out operators** and
  **disconnected PLCs by changing IP addresses**. Targeting spanned organizations of all
  sizes. **Vulnerable cellular modems** installed by operators/vendors were specifically
  called out as often-undocumented entry points.
- **Targeted equipment (named PLC families):** Rockwell **CompactLogix** and **Micro850**,
  Schneider Electric **Modicon M340**, Siemens **S7-1200** series.
- **Sector:** water / wastewater (critical infrastructure) — **NOT aerospace & defense**;
  no A&D/DIB entity named.
- **CVEs:** none named. **Atomic IOCs:** none in the relay; CISA points to **AA26-097A** for
  the IOC set.

## Attribution — Hard Rule 2 discipline

The source states **no formal attribution has been made**. It notes only that Iranian
threat groups **CyberAv3ngers** and **Handala** "fit the attack profile," and that
CyberAv3ngers "has targeted small water utilities historically." This is profile-fit
framing, **not** an attribution. **Archimedes originates no attribution.** Roster overlap
recorded for grader/analyst awareness only:

- **CyberAv3ngers (#028)** — IRGC-CEC OT/ICS actor; documented US water-utility targeting
  (Unitronics 2023–24, CISA-confirmed). Note: **CISA's own cross-reference to AA26-097A**
  (the CyberAv3ngers six-agency advisory, per roster #028 sourcing) is a procedural
  IOC-reference, not an attribution of this Minnesota campaign — preserve that distinction.
- **Handala Hack (#014)** — Iran-MOIS destructive/hacktivist actor, named in the same
  profile-fit framing.

No source attributes this campaign to a tracked actor. First-party Splunk: 0 hits both
indices this sweep (dormant external-telemetry stream; visibility-bounded null).

## Why grader-relevant (below FLASH bar)

- **State change / UPDATE:** advances the tracked Minnesota OT campaign
  (finding-2026-07-29-0001) from initial incident reporting to an **authoritative CISA
  mitigation advisory** with named PLC targets and a named IOC-reference advisory (AA26-097A).
- **Trigger 5 (A&D-sector campaign):** FAIL — water/wastewater, no A&D/DIB victim.
- **Trigger 2 (new attribution to tracked actor):** FAIL — no attribution; actor mentions
  explicitly profile-fit only.
- Held for the scheduled morning brief per FLASH anti-noise (same topic already surfaced
  06:00 sweep; the Minnesota incident is already an in-corpus finding).

---

## Extraction notes

- Language: en
- Publisher byline: Mike Lennon (SecurityWeek), relaying a CISA alert
- Article type: advisory relay (security media)
- Raw IOC extraction invoked: yes (result below)
- Copyright: paraphrased; no quoted span exceeds 15 words

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: securityweek-2026-07-30-cisa-water-ot
  source_url: https://www.securityweek.com/cisa-urges-water-sector-to-protect-ot-after-coordinated-attacks-on-plcs/
  extracted_at: 2026-07-31T07:34:00-04:00
  extracted_by: collector
  target_actor_id: null
  text_word_count: 0   # relay summary; full body not stored (no atomic IOCs to preserve)

indicators: []          # no atomic IOCs (IPs/domains/hashes) in the relay; CISA references AA26-097A for IOC set

attribution_claims: []  # NONE — source explicitly states no attribution made; CyberAv3ngers/Handala are profile-fit mentions, not claims

benign_filtered: []

extraction_warnings:
  - type: attribution_profile_fit_not_claim
    ioc_id: null
    detail: "CyberAv3ngers (#028) and Handala (#014) named as profile-fit only; no source attributes this campaign. Do not upgrade to attribution downstream (Hard Rule 2)."
  - type: named_products_not_iocs
    ioc_id: null
    detail: "Rockwell CompactLogix/Micro850, Schneider Modicon M340, Siemens S7-1200 are targeted PLC families (affected-product context), not atomic indicators. AA26-097A holds the IOC set (not retrieved this sweep — direct-retrieval todo for vuln-tracker/actor-profiler)."
```
