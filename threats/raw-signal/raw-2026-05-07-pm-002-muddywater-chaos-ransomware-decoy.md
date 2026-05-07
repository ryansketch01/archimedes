---
raw_id: raw-2026-05-07-pm-002
collected_at: 2026-05-07T15:36:00-04:00
run_id: pre-brief-20260507-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: bleepingcomputer
    source_name: "BleepingComputer"
    source_url: https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/
    source_grade_estimated: B
    role: originating
    published_at: 2026-05-06T09:02:00-04:00
    note: |
      Tracked-actor activity (MuddyWater, roster id 022, Iran/MOIS,
      tracked since 2026-05-06 via Rapid7 single-source attribution).
      BleepingComputer relays a campaign in which MuddyWater allegedly
      uses Chaos ransomware as a decoy while leveraging Microsoft Teams
      social engineering for network access. Surface area to the existing
      72h MuddyWater attribution-veto window (clock ~2026-05-09 12:00 EDT
      per _roster.yaml note) — grader/red-team should evaluate whether
      this is a second corroborating B-grade source for the 2026-campaign
      MuddyWater attribution or relay-only of Rapid7's prior reporting.
match_reason:
  watchlist: []
  actors: ["022"]    # MuddyWater
  vulnerabilities: []
  keywords: [muddywater, chaos-ransomware, ransomware-decoy, microsoft-teams, social-engineering, iran, mois, irgc-io, false-flag-ransomware]
triage_tags: [tracked_actor_activity, iran-cyber, mois, possible_attribution_corroboration, ransomware_decoy_ttp, attribution_caveat_pending_72h_clock]
iocs_extracted: true
iocs_count: 0
text_word_count: 220
promoted: false
rejected_at: 2026-05-07T16:21:00-04:00
rejection_id: reject-2026-05-07-0001
rejection_summary: >
  Cluster rejected: source chain unverified (article body not fetched —
  cannot determine if BleepingComputer is relaying Rapid7 or citing a
  different originating source); active 72h attribution-veto clock on
  MuddyWater 2026-campaign attribution (resolves ~2026-05-09 12:00 EDT);
  zero IOCs in available source text. Procedural rejection — claim may
  well be true but cannot be graded cleanly without source-chain detail.
  See _rejection-log.yaml entry reject-2026-05-07-0001 for full rationale
  and re-grading path.
ttl_expires_at: 2026-08-05T15:36:00-04:00
---

# MuddyWater (Iran/MOIS) reportedly uses Chaos ransomware as decoy in Teams-based social engineering campaign

## Source summary

BleepingComputer (2026-05-06 09:02 EDT, "MuddyWater hackers use Chaos ransomware as a decoy in attacks") reports that the Iranian state-aligned group MuddyWater is disguising operations as ransomware incidents while leveraging Microsoft Teams social engineering for network access. The article was identified in feed listing only; full body was not fetched in this sweep due to time-window constraints.

## What this signal represents

1. **Tracked actor.** MuddyWater is roster id 022 (Iran, MOIS, tracked since 2026-05-06). Profile is first-pass; threat-box is TEMPLATE; an attribution-veto / 72h auto-downgrade clock is running on the 2026-campaign MuddyWater attribution per Rapid7 single-source veto (clock resolves ~2026-05-09 12:00 EDT per `_roster.yaml` note).

2. **Possible corroboration vector.** This is BleepingComputer (B-grade media). If BleepingComputer is relaying Rapid7's prior reporting (likely), it does NOT count as an independent second source — it is re-reporting the same source per INTEL-GRADING.md. If BleepingComputer is citing a different originating source (e.g., another vendor, CrowdStrike, Mandiant), it MAY count as a second B/A-grade attribution and would resolve the 72h veto in MuddyWater's favor. Grader must verify the source chain.

3. **TTP claim — ransomware-as-decoy.** "MuddyWater" + "Chaos ransomware as decoy" + "Teams social engineering for network access" represents a TTP profile consistent with prior MuddyWater reporting (Microsoft Teams as initial-access pretext is in MuddyWater's published playbook per Rapid7 finding). Ransomware-as-decoy is a notable false-flag pattern that, if confirmed, raises the bar on Iranian disruption-vs-espionage ambiguity.

## What this source does NOT add (without full-body fetch)

- No IOCs extracted (article body not fetched in this sweep).
- No specific victim sector. No A&D-targeting claim.
- No specific CVE referenced.
- No date range for the campaign.
- No primary attribution language captured beyond the headline.

## Recommendation for grader

This raw-signal is a placeholder for source identification. Grader should fetch the full BleepingComputer article body before promoting, to verify:
- Whether the originating source is Rapid7 (relay → no attribution corroboration) or a different vendor (independent → potential corroboration)
- Whether IOCs are present and overlap with the existing MuddyWater 2026-campaign IOC set
- Whether any A&D sector or watchlist entity is named
- Whether the Chaos ransomware decoy pattern shows up in any first-party telemetry

Until the article body is verified, this signal does NOT promote an MuddyWater attribution beyond the existing Rapid7-veto state. Hard Rule 2 holds.

---

## Extraction notes

- Language: en
- Article type: secondary news reporting (B-grade)
- Publisher: BleepingComputer
- Raw IOC extraction invoked: yes (zero IOCs from feed-listing only; full-body fetch deferred)
- Quote-discipline: zero quotes captured; no source language quoted

## IOCs (from ioc-extraction skill)

```yaml
iocs: []

attribution_claims:
  - actor_named: MuddyWater
    actor_class: "Iran-nexus state-aligned APT (MOIS)"
    nation_state_named: true
    confidence_language: "[unknown — full body not fetched; headline asserts MuddyWater without hedging]"
    cross_walk_to_roster: "022 — already tracked"
    corroboration_status: "pending_grader_verification (relay-vs-independent of Rapid7 must be confirmed before crediting as second source)"
    archimedes_action: |
      Hard Rule 2 / single-source-attribution rule: do not promote a
      MuddyWater attribution beyond what existing tracked-source state
      supports. Existing 72h auto-downgrade clock on 2026-campaign
      MuddyWater attribution remains in effect until grader verifies
      whether this article materially independent.
```

- Authorized-targets check: not applicable (passive WebFetch fallback only)
- LEGAL-POLICY check: passed — passive read of public news index page; no exploitation assistance; no credentials surfaced; no PII collected
- Note to grader: full article body fetch recommended at grading stage to populate IOCs and verify originating source chain
