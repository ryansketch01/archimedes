---
raw_id: raw-2026-05-07-flash-1800-002
collected_at: 2026-05-07T18:08:00-04:00
run_id: flash-sweep-20260507-180000
collection_mode: flash_sweep
test: false
sources:
  - source_yaml_id: the-record
    source_name: "The Record (Recorded Future News)"
    source_url: https://therecord.media/iran-government-hackers-use-chaos-ransomware-as-cover
    source_grade_estimated: B
    role: relay
    published_at: 2026-05-07T17:30:00-04:00
    note: |
      The Record relay of the Rapid7 MuddyWater/Chaos disclosure
      already absorbed via finding-2026-05-06-FLASH-0002. Adds
      historical FBI-warning and prior-incident context (Pay2Key
      healthcare February, Stryker medical device damage) but no
      new IOCs, no new victims, no second-source independent
      attribution. Attribution remains Rapid7-only (B-grade single-
      source veto already applied to MuddyWater dossier; 72h auto-
      downgrade clock running until ~2026-05-09 12:00 EDT per
      _roster.yaml note).
match_reason:
  watchlist: []
  actors: ["022"]    # MuddyWater
  vulnerabilities: []
  keywords: [muddywater, chaos-ransomware, mois, iran, the-record-relay, rapid7-attribution-only]
triage_tags:
  - non_flash
  - relay_no_new_facts
  - already_absorbed
  - single_source_veto_active
  - 72h_auto_downgrade_clock_running
flash_evaluation:
  result: not_a_flash_candidate
  triggers_evaluated:
    trigger_2_tracked_actor_attribution:
      tracked_actor: true
      actor_id: "022"
      new_attribution: false
      verdict: FAIL_NOT_NEW_ATTRIBUTION
    trigger_4_tracked_actor_ttp_change:
      a_or_b_grade: true
      attributable: true
      new_ttp: false
      verdict: FAIL_NO_NEW_TTP
  rationale: |
    The Record article is a relay of Rapid7's 2026-05-06 disclosure
    already absorbed into MuddyWater dossier and the 2026-05-07
    afternoon brief. New material is limited to historical context
    (FBI warnings on Iranian/ransomware-affiliate partnerships,
    Pay2Key-on-US-healthcare February incident, Stryker medical
    device damage) — none of which constitutes new attribution or
    new TTP for the active campaign. No new IOCs. Attribution
    remains Rapid7 single-source; The Record is journalistic
    amplification, not independent corroboration. Single-source veto
    on the MuddyWater attribution remains in force; 72h auto-
    downgrade clock continues to run.
disposition: |
  Hold; no brief action required. If a second A/B-grade source
  (Mandiant, MSTIC, CrowdStrike, Unit 42, ESET, Sophos, etc.)
  publishes independent corroboration of the Rapid7 MuddyWater
  attribution within the 72h window, that would be a candidate to
  lift the single-source veto and adjust WEP. Today's relay does NOT
  qualify.
promoted: false
rejected_at: 2026-05-08T08:30:00-04:00
rejection_id: reject-2026-05-08-0001
---

# The Record relay — MuddyWater/Chaos ransomware (2026-05-07 17:30 EDT)

## Summary (collector observation)

The Record published "Iranian government hackers using Chaos
ransomware as cover, researchers say" at 2026-05-07 17:30 EDT. Article
relays Rapid7's earlier disclosure attributing a Chaos-ransomware-
themed intrusion to MuddyWater (Iranian MOIS, tracked actor 022 in
roster).

Quoted Rapid7 attribution language: "The researchers found troves of
technical evidence pointing to Iran's MOIS. The malware deployed and
certificates used tied back to the toolkit typically used by Iran's
MuddyWater hacking group." This is the same evidence base already
covered in finding-2026-05-06-FLASH-0002 and the MuddyWater dossier.

The Record adds historical reference points: FBI warnings about
Iranian actors partnering with NoEscape, Ransomhouse, AlphV; prior
Pay2Key targeting of US healthcare in February; Stryker medical device
incident. These are framing, not new attribution.

## FLASH evaluation summary

Does not fire trigger 2 (attribution exists but is not new — Rapid7
first published; The Record is a relay) or trigger 4 (no new TTP
described beyond what Rapid7 disclosed). Single-source veto on
MuddyWater attribution remains in force; The Record is not an
independent corroborating source. 72h auto-downgrade clock from the
original FLASH-0002 (~2026-05-09 12:00 EDT) is unchanged.
