---
finding_id: finding-2026-07-16-0003
created_at: 2026-07-16T16:22:00-04:00
graded_by: grader
grading_run_id: flash-2026-07-16-1600
grading_mode: flash_fast_path

# Core grading (from admiralty-grading skill output)
digraph: A2
source_reliability:
  grade: A
  source_name: "CERT-UA (Ukraine national CERT) — originating advisory 2026-07-16; relayed via The Record (Recorded Future News)"
  source_yaml_id: the-record          # relay-of-record in source-grades.yaml (grade B); originator CERT-UA not yet a dedicated id
  grade_rationale: >
    Letter anchored on the ORIGINATING evidence basis: CERT-UA, Ukraine's national
    CERT. National-CERT advisories are technically verified before publication and are
    the authoritative primary on Sandworm/GRU operations in the Ukraine theater —
    CISA-analog / national-cyber-authority class, which the corpus grades A (per the
    CISA / NSA-CNSA precedent and the foreign national-cyber-authority precedents
    CCB / ABW / CCCS). This sweep reached Archimedes via The Record (source-grades.yaml
    the-record, ratified B) only; the CERT-UA advisory primary was NOT directly
    retrieved. Conservative floor would be B (first-surface foreign CERT, per the
    provisional-B starting point used for CCB/ABW/CCCS). Anchored at A on the
    national-CERT authority; either A2 or B2 clears the FLASH grade threshold, so the
    letter does not change the disposition below.
  provisional: true
  provisional_reason: >
    No dedicated source-grades.yaml id yet exists for CERT-UA. Provisional A proposed
    per the national-cyber-authority / government-CERT precedent (CISA-analog class).
    Relay-conveyed via The Record (ratified B); CERT-UA advisory primary awaiting
    direct retrieval (needed for atomic IOCs — domains/hashes/PowerShell command
    detail absent from the relay). Flagged to librarian to add a dedicated cert-ua
    source id with ratification clock; see source_grade_notes.
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # Sandworm (GRU 74455) operations against Ukrainian targets are the actor's baseline theater; adopting ClickFix (fake-CAPTCHA -> user-pasted PowerShell), a widely-observed 2025-2026 delivery technique, is consistent with the broader threat landscape and with the actor's ongoing tooling churn
    - probably_true_no_contradicting_ab      # no A/B-grade source contradicts CERT-UA's characterization
    - probably_true_claims_coherent          # ClickFix fake-CAPTCHA -> PowerShell is a well-documented real delivery chain; the named tooling roles (GhettoVibe initial, ScoutCurl recon, FluidLeech AV-removal-disguised loader, LoadLoop loader) form an internally coherent kill chain
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld. Only ONE effective evidence basis is present — the
    CERT-UA advisory. The Record is a relay OF that advisory, not an independent second
    telemetry/IR source, so the corroboration independence test fails (a relay of a
    single upstream is not corroboration). Grade 1 also requires cross-matching
    technical artifacts across independent sources; NONE are published in the retrieved
    relay (zero atomic IOCs — tooling named at family level only). Err low -> 2.
  rationale: >
    Per CERT-UA (relayed by The Record), Sandworm has shifted this spring/summer toward
    a ClickFix social-engineering delivery: victims encounter a fake CAPTCHA on a
    compromised site and are instructed to paste a PowerShell command into Windows,
    deploying a new named malware set (GhettoVibe / ScoutCurl / FluidLeech / LoadLoop)
    for persistent access and reconnaissance. CERT-UA frames this as an evolved
    delivery TACTIC, not an entirely new capability class, against primarily Ukrainian
    targets. The delivery-method shift and the specific tooling names are new to the
    Archimedes corpus; the Sandworm attribution itself is long-established (GRU Unit
    74455) and is preserved verbatim, not originated.
corroboration:
  independent_sources:
    - certua-advisory-2026-07-16     # originating
  independent: false
  test_passed: >
    FAILS. Single effective evidence basis (CERT-UA). The Record is a relay of the
    CERT-UA advisory, not an independent evidence source — remove CERT-UA and The
    Record's report does not stand on its own telemetry. One upstream, one effective
    source.
first_party_precedence:
  applied: false
  splunk_evidence: null
  rationale: >
    No atomic IOCs present in the relay to query against defenseclaw_local / archimedes
    telemetry (zero domains/IPs/hashes; tooling named at family level only). No
    first-party check performable this sweep. Absence of queryable indicators is NOT
    disconfirming. Re-run first-party precedence when the CERT-UA primary is retrieved
    and atomic IOCs are available.
single_source_veto_applied: true
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "Sandworm ClickFix (fake-CAPTCHA -> PowerShell) delivery shift + new tooling set vs Ukrainian targets"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-16-flash-1600-001
  attribution_claims:
    - claimed_actor: Sandworm
      roster_id: "007"
      claimed_by_sources: [certua-advisory-2026-07-16]
      novelty: not_new           # long-established GRU Unit 74455 attribution; NEW element is tooling/delivery, not actor
      requires_analyst_review: true

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_action        # A2 clears B2 minimum
    - weekly_synthesis
    - actor_profile_update      # new tooling + delivery TTP for Sandworm dossier #007
  flash_grade_threshold_met: true    # A2 (or B2 floor) clears the B2 FLASH minimum on GRADE
  flash_posted: false                # HELD from FLASH on anti-noise / relevance grounds (see flash_disposition)

# FLASH disposition (grader routing decision)
flash_disposition:
  trigger_claimed: trigger-4-tracked-actor-ttp-change
  trigger_met: true                  # marginal — new tooling + delivery shift, tracked actor, A/B source
  posted_as_flash: false
  routing: next_scheduled_brief_russia_watch
  hold_reasons:
    - no_ad_dib_gov_ci_nexus         # targeting is "primarily Ukrainian"; zero aerospace/defense/DIB/ITAR/gov/CI target named
    - commodity_technique            # ClickFix is a widely-used commodity delivery method; Sandworm ADOPTING a common technique in its baseline theater, not a novel capability class
    - attribution_not_new            # Sandworm=GRU 74455 is long-standing; no new attribution (would-be Trigger 2 not met)
    - no_atomic_iocs                 # zero actionable indicators in the relay; no defensive action a target could take from this item today
    - anti_noise_doctrine            # FLASH-POLICY anti-noise: a Ukraine-theater commodity-technique adoption with no A&D nexus is a weak FLASH and risks FLASH fatigue
  anti_noise_check:
    b2_minimum_met: true
    distinct_from_prior_flash_topics: true   # NOT a repeat of 2026-07-13 DynoWiper/EU-UK-sanctions topic nor the FSB Center16 advisory — different vector (delivery/tooling vs OT-destructive wiper + sanctions)
    red_team_mandatory: false                # WEP "likely" (< very likely); Anti-Noise Rule 3 not triggered

# Downstream handoff flags
analyst_review_required: true       # attribution claim present (per grader doctrine: true if WEP >= likely OR attribution claim present)
red_team_review_required: false     # WEP "likely" < very likely
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Source-grade proposal for librarian
source_grade_notes:
  proposal: add_new_source
  proposed_source_id: cert-ua
  proposed_name: "CERT-UA (Computer Emergency Response Team of Ukraine)"
  proposed_category: government
  proposed_grade: A
  proposed_provisional: true
  rationale: >
    National cyber authority / government-CERT class, authoritative primary on
    Sandworm/GRU Ukraine-theater operations (CISA-analog). Follows the CCB/ABW/CCCS
    foreign-national-cyber-authority precedent. Conservative alternative floor B if
    operator prefers the first-surface provisional-B starting point. First corpus
    citation via this finding (relay-conveyed by The Record); CERT-UA primary awaiting
    direct retrieval. Recommend ratification clock + direct-retrieval todo.
  action: "Add provisional cert-ua id to source-grades.yaml + source-grade-log.md; set ratification clock; log direct-retrieval collection todo for atomic IOCs."

# Lifecycle
tlp: CLEAR
published_in_briefs: []
retracted: false
retraction_brief_id: null
---

# CERT-UA: Sandworm shifts to ClickFix (fake-CAPTCHA to pasted PowerShell) delivering a new malware set against Ukrainian targets

## Summary

CERT-UA reports that Sandworm (roster #007; APT44 / Seashell Blizzard, RU GRU Unit 74455) has shifted this spring and summer to a ClickFix delivery chain — a fake CAPTCHA on a compromised site prompts victims to paste a PowerShell command into Windows, which deploys a newly named malware set for persistent access and reconnaissance. The targeting is described as primarily Ukrainian, with no aerospace, defense, DIB, government, or critical-infrastructure nexus to the target profile. The Sandworm attribution is long-established; the new elements are the ClickFix delivery method and the tooling (GhettoVibe, ScoutCurl, FluidLeech, LoadLoop). Graded A2 (single-source veto applied — one effective upstream, no independent corroboration), WEP likely.

## Grading rationale

- **Source (A):** Originating source is CERT-UA, Ukraine's national CERT — CISA-analog government-CERT class, graded A on originator authority (provisional; conservative floor B). Reached Archimedes via The Record (ratified B relay); CERT-UA advisory primary not directly retrieved this sweep.
- **Credibility (2):** Consistent with Sandworm's baseline Ukraine-theater operations; ClickFix is a well-documented delivery technique; named tooling forms a coherent kill chain. Grade 1 withheld — a relay of a single upstream is not independent corroboration, and no atomic artifacts are published for cross-matching.
- **Single-source veto:** Applied. One effective evidence basis (CERT-UA). WEP capped at **likely**.

## FLASH determination

- **Grade threshold:** MET. A2 clears the B2 FLASH minimum (the conservative B2 floor would also clear it). The hold is NOT on grade.
- **Trigger:** Trigger 4 (tracked-actor TTP change) marginally met — new tooling + delivery shift, tracked actor, A/B source. Trigger 2 (new attribution) NOT met — Sandworm=GRU 74455 is long-established.
- **Held from FLASH.** Routed to the next scheduled brief (Russia-watch / afternoon). Rationale, per FLASH-POLICY anti-noise doctrine:
  - No A&D / DIB / gov / CI nexus — targeting is primarily Ukrainian; the target profile (ad-prime-v1) is not implicated.
  - ClickFix is a commodity technique; Sandworm is adopting a common delivery method in its home theater, not fielding a novel capability class.
  - No atomic IOCs in the relay — a target could take no specific defensive action from this item today.
  - Distinct from prior Sandworm FLASH/brief topics (2026-07-13 DynoWiper/EU-UK sanctions; FSB Center16 advisory), so not a 24h-repeat suppression — but a weak FLASH that would contribute to FLASH fatigue.
- This is a legitimate scheduled-brief Russia-watch item and an actor-profile input (new Sandworm tooling/TTP for dossier #007), not a wake-someone alert.

## Technical detail

- **Delivery:** ClickFix — a fake CAPTCHA on a compromised web page instructs the victim to copy and paste a PowerShell command into Windows (Run dialog / terminal), executing attacker code. Maps to user-executed script delivery (ATT&CK T1204.004 / T1059.001). No PowerShell command body reproduced (Hard Rule 3).
- **Tooling (CERT-UA codenames):** GhettoVibe (initial malware), ScoutCurl (reconnaissance — system details, software inventory, browser data), FluidLeech (loader disguised as antivirus-removal software), LoadLoop (loader).
- **Attribution:** CERT-UA describes the actor as "Kremlin-backed" and linked to "Russia's military intelligence agency, the GRU," active "since at least 2013." Preserved verbatim per Hard Rule 2; not originated or upgraded by Archimedes.

## IOCs surfaced

None. Zero atomic indicators (no domains, IPs, or hashes) in the retrieved relay; tooling named at family level only. CERT-UA advisory primary pending direct retrieval for atomic IOCs — logged as a collection todo. First-party Splunk precedence not performable this sweep (no queryable indicators).

## Relationship to existing findings

- **finding-2026-07-13-0001** (EU/UK first joint cyber-sanctions; Sandworm DynoWiper / Poland grid; FSB Center16 / Turla). Same actor, different vector — that finding covered OT-destructive wiper activity + sanctions designations; this covers an espionage-oriented ClickFix delivery shift and new tooling. Complementary, not duplicative. Together they show Sandworm active across both destructive and access-oriented tracks in mid-2026.
- Actor dossier: threats/threat-actors/Sandworm/ (#007, HIGH). This finding is an actor-profile input (new delivery TTP + four new named tools).

## Open questions for analyst

- **Attribution (verbatim, not new):** CERT-UA attributes to Sandworm/GRU 74455 — long-established. Confirm no inference beyond CERT-UA's stated confidence before any propagation to the dossier.
- **Direct retrieval:** Pull the CERT-UA primary advisory for atomic IOCs (domains/hashes) and the PowerShell chain detail (for detection engineering, not reproduction). Re-run first-party Splunk precedence once indicators exist.
- **Tooling novelty:** Assess whether GhettoVibe/ScoutCurl/FluidLeech/LoadLoop are genuinely new families or renamed/rebuilt prior Sandworm tooling — bears on the actor-profile capability delta.
- **Commodity-technique framing:** For the scheduled brief, frame ClickFix adoption as landscape-consistent commodity tradecraft, not a Sandworm-specific escalation — avoid overstating A&D relevance.
