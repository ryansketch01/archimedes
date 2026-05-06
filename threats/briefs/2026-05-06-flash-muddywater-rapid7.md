---
brief_id: flash-2026-05-06-1200
brief_type: flash
published_at: 2026-05-06T12:55:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: archimedes-red-team
red_team_outcome: PUBLISH-WITH-CHANGES
human_override: null
digraph: A2
wep: likely
single_source_veto_applied: true
double_constraint_note: |
  WEP "likely" is doing double-duty: single-source veto (Rapid7 sole originating;
  SecurityWeek and BleepingComputer are pure relays) AND Rapid7's own self-rated
  "moderate confidence" — vendor-IR convention treats "moderate" as one band
  below their ceiling. Both pressures argue for the same cap; surfaced separately
  to the reader rather than absorbed silently.
flash_trigger: trigger-2-new-attribution
flash_trigger_secondary: trigger-4-tracked-actor-ttp-change
flash_trigger_note: |
  Triggers 2 (new attribution to a tracked roster actor) and 4 (tracked-actor
  TTP / tooling / infrastructure change from A/B-grade source) fire concurrently
  on the same topic. Per FLASH-POLICY anti-noise rule "one FLASH per trigger
  topic per 24h," both resolve to a single FLASH led on the new-attribution
  angle, with the TTP-change detail in the body.
quiet_hours_at_compose: false
critical_override_evaluated: true
critical_override_applied: false
critical_override_rationale: |
  4 conditions required, 2 met. CVSS 10.0 fails (no CVE component — TTP /
  actor / tooling report). Active exploitation passes (active IR engagement
  per Rapid7). Tracked actor passes (MuddyWater is roster #022). A&D
  watchlist sector targeted fails (Rapid7 names construction, manufacturing,
  business services — NOT aerospace, defense, or any A&D watchlist entity;
  inferential A&D relevance does not satisfy the condition). Override does
  not apply. Compose time 12:55 EDT is inside active hours (09:00-21:00
  EDT) — FLASH posts directly per standard rules; no quiet-hours queueing.
disposition: posted-immediately
findings_referenced:
  - finding-2026-05-06-FLASH-0002
related_actors:
  - "022"
related_actor_profile_status: pending
actor_profiler_handoff:
  required: true
  actor_id: "022"
  primary_name: MuddyWater
  first_pass_profile_deadline: 2026-05-13
  threat_box_scoring_deadline: 2026-05-20
  high_composite_requires_human_signoff: true
  high_composite_signoff_command: /approve-scoring
sources_referenced:
  - source_id: rapid7-blog
    grade: A
    provisional: true
    role: originating
    url: https://www.rapid7.com/blog/
  - source_id: bleepingcomputer
    grade: B
    role: relay
    url: https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/
  - source_id: securityweek
    grade: B
    provisional: true
    role: relay
    url: https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/
auto_downgrade_clock:
  trigger_at: 2026-05-09T12:18:00-04:00
  conditions_for_downgrade_all_of:
    - no_second_ab_grade_independent_confirmation
    - no_first_party_splunk_hit_post_ioc_ingest
    - no_cisa_or_fbi_advisory_pickup
  consequence: re-grade to C3 'possibly true' in next sweep
tripwires_for_regrade_up:
  - second_ab_grade_independent_confirmation
  - first_party_splunk_hit_post_ioc_ingest
  - cisa_or_fbi_advisory_pickup
  - rapid7_followon_high_confidence_upgrade
ioc_handoff:
  required: true
  count: 19
  breakdown:
    sha256: 9
    domain: 3
    ipv4: 4
    onion: 1
    code_signing_certificate: 1
  retroactive_sweep_requested: true
  forward_detection_requested: true
explicit_non_linkage:
  - related_brief: flash-2026-05-06-0600
    related_finding: finding-2026-05-06-FLASH-0001
    topic: PAN-OS CVE-2026-0300
    relationship: structural_parallel_only
    do_not_mutual_validate: true
    rationale: |
      Different topic, no shared evidence, no shared actor. Both findings
      are single-source-veto load-bearing FLASHes — that is an operational
      pattern, not corroborating signal. Holding any pattern observation
      for weekly synthesis (2026-05-10).
  - related_brief: 2026-05-05-morning
    related_finding: finding-2026-05-05-0001
    topic: UNC1549 CMMC-adjacent campaign
    relationship: different_iranian_actor_no_shared_evidence
    do_not_mutual_validate: true
    rationale: |
      UNC1549 is IRGC; MuddyWater is MOIS. No shared evidence, no shared
      infrastructure. Stacking "multiple Iranian campaigns this week"
      across separate findings is a presentation choice that risks
      implying corroboration where none exists.
word_count: 297
tlp: CLEAR
---

# FLASH: Rapid7 attributes US intrusion to MuddyWater at moderate confidence — ransomware as cover for espionage

*2026-05-06 12:55 EDT · A2 · WEP likely · TLP:CLEAR · Active-hours post*

**Rapid7's IR report attributes a 2026-05 intrusion at an unnamed US organization to MuddyWater (#022, Iran/MOIS per Rapid7's citation chain) at "Moderate confidence in attributing the incident to MuddyWater."** Two sub-claims ship; their defensibility differs.

**Defensible read — espionage shape, observable from forensics:** Chaos ransomware without actual encryption, fake DLS onion as extortion theater, a 12-command custom RAT (Game.exe / Darkcomp posing as Microsoft WebView2), interactive Microsoft Teams screen-share for live credential harvest, MFA device-add manipulation. Espionage wrapped in ransomware theater — the shape holds whoever the actor is.

**Moderate-confidence read — actor cluster:** Rapid7 attributes specifically to MuddyWater on continuity surfaces (pythonw.exe injection, Teams persona masquerading as internal IT support, Donald Gay code-signing lineage, Operation Olalampo overlap). The framing leaves alternative Iranian-cluster and mixed-composition readings open. Hard Rule 2: Archimedes does not originate or strengthen.

**A&D relevance — tradecraft portability, not sector targeting:** Rapid7 names US construction, manufacturing, business services. **No aerospace, defense, or A&D watchlist entity is named.** The defensible move is platform-generic: audit M365 / Teams for external-account screen-share initiation, MFA device-add operations, and Quick Assist initiation from external accounts.

**Two confidence constraints stack** — single-source veto (SecurityWeek and BleepingComputer are pure Rapid7 relays) AND Rapid7's own moderate self-rating. WEP capped at likely.

**MuddyWater profile is pending** (#022) — no independent Archimedes baseline. Actor-profiler first-pass in 7 days; threat-box in 14; HIGH composite needs `/approve-scoring`.

**Auto-downgrade clock — +72h (2026-05-09 12:18 EDT):** re-grade to C3 absent (a) second A/B-grade confirmation, (b) first-party Splunk hit post-ingest, or (c) CISA / FBI pickup. Any one fires re-grade-up.

**First-party Splunk:** -30d silent on 4 IPs and 3 domains across `archimedes` and `defenseclaw_local`. Absence of evidence, not evidence of absence (Hard Rule 8). 19 IOCs handed to librarian for `_master-index.yaml` ingestion.

**Sources:**
- Rapid7 IR report — [rapid7.com/blog](https://www.rapid7.com/blog/) · A (provisional)
- BleepingComputer (relay) — [bleepingcomputer.com](https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/) · B
- SecurityWeek (relay) — [securityweek.com](https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/) · B (provisional)

**Related:** Actor #022 MuddyWater (profile pending) · finding-2026-05-06-FLASH-0002 · 19 IOCs.
