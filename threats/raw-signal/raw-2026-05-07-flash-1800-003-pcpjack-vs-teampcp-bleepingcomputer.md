---
raw_id: raw-2026-05-07-flash-1800-003
collected_at: 2026-05-07T18:11:00-04:00
run_id: flash-sweep-20260507-180000
collection_mode: flash_sweep
test: false
sources:
  - source_yaml_id: bleepingcomputer
    source_name: "BleepingComputer (Bill Toulas)"
    source_url: https://www.bleepingcomputer.com/news/security/new-pcpjack-worm-steals-credentials-cleans-teampcp-infections/
    source_grade_estimated: B
    role: relay
    published_at: 2026-05-07T14:35:00-04:00
    note: |
      BleepingComputer relay of SentinelLabs research describing
      PCPJack — a new credential-stealing worm targeting cloud
      infrastructure (Docker, Kubernetes, Redis, MongoDB, RayML).
      PCPJack actively cleans/displaces TeamPCP tooling on
      compromised hosts, "claiming the compromise for themselves."
      Originating research: SentinelLabs (A-grade equivalent).
match_reason:
  watchlist: []
  actors: ["001"]    # TeamPCP
  vulnerabilities: [CVE-2025-29927, CVE-2025-55182, CVE-2026-1357, CVE-2025-9501, CVE-2025-48703]
  keywords: [pcpjack, teampcp, cloud-credential-theft, worm, displacement, sentinellabs, docker, kubernetes]
triage_tags:
  - non_flash
  - tracked_actor_001_context
  - actor_displacement_event
  - actor_profiler_input
flash_evaluation:
  result: not_a_flash_candidate
  triggers_evaluated:
    trigger_2_tracked_actor_attribution:
      tracked_actor: true
      actor_id: "001"
      new_attribution: false
      verdict: FAIL_NOT_AN_ATTRIBUTION_EVENT
    trigger_4_tracked_actor_ttp_change:
      a_or_b_grade: true
      attributable_to_tracked_actor: false
      new_ttp_attributed_to_tracked_actor: false
      verdict: FAIL_NO_NEW_TTP_ATTRIBUTABLE_TO_TEAMPCP
  rationale: |
    Article describes a new actor (PCPJack) attacking TeamPCP's
    cloud-infrastructure footholds — i.e., TeamPCP appears as a
    victim/displaced party, not as the operator of new tooling or
    infrastructure. There is no new attribution TO TeamPCP and no
    new TTP attributable to TeamPCP. Trigger 2 requires new
    attribution to a tracked actor; trigger 4 requires new
    tooling/targeting/infra attributable to a tracked actor.
    Neither is present. The article does mention TeamPCP by name
    (tracked actor 001) but as a target, not as the operator.

    Operationally interesting for the actor-profiler: a competing
    threat group is actively displacing TeamPCP from cloud
    footholds. This may compress the operational window TeamPCP can
    sustain on any single victim and may surface in TeamPCP's next
    /update-tracking pass as a "competitive landscape" data point.
    But it is NOT a FLASH-grade event.
disposition: |
  Hold; no brief action required. Surface to actor-profiler at next
  TeamPCP review (next_review_due: 2026-06-16 per _roster.yaml) as
  context on the cloud-credential-theft threat-actor competitive
  landscape. May warrant earlier review if a second source confirms
  PCPJack is meaningfully reducing TeamPCP's victim base.
---

# PCPJack worm vs TeamPCP cloud infrastructure — collector observation

## Summary

BleepingComputer (2026-05-07 14:35 EDT) relays SentinelLabs research
on PCPJack, described as a new credential-stealing malware framework
targeting cloud-exposed Docker, Kubernetes, Redis, MongoDB, and RayML
deployments. Notable behavior per quoted research: "During this
initial stage, PCPJack explicitly checks for TeamPCP tooling and
attempts to delete everything, thus claiming the compromise for
themselves."

Targets named for credential exfiltration: SSH keys, Slack tokens,
OpenAI/Anthropic API keys, Discord, DigitalOcean credentials.
Distribution via compromised cloud workloads exploiting CVEs above.

No A&D sector targeting named. No nation-state attribution. PCPJack is
not (yet) a tracked actor in _roster.yaml.

## FLASH evaluation summary

Does not fire any FLASH trigger. TeamPCP appears as the displaced
party, not as the actor performing new TTPs. Operationally relevant
for actor-profiler but not for FLASH.
