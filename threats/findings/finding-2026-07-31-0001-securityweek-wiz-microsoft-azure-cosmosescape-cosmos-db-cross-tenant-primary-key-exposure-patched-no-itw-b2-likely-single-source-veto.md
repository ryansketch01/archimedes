---
finding_id: finding-2026-07-31-0001
created_at: 2026-07-31T08:16:00-04:00
graded_by: grader
grading_run_id: morning-20260731-080000
grading_mode: scheduled_brief
finding_type: new                         # net-new topic; no prior corpus finding for CosmosEscape / Azure Cosmos DB cross-tenant flaw

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: "SecurityWeek (Ionut Arghire)"
  source_yaml_id: securityweek
  underlying_primary:
    - source_name: "Wiz Research (originating discovery; 'CosmosEscape')"
      source_yaml_id: wiz-research
      grade: A                            # provisional A (awaiting_ratification) per source-grades.yaml
      in_hand_this_cycle: false           # Wiz blog not directly retrieved; reaches corpus via SecurityWeek relay
    - source_name: "Microsoft (MSRC/MSTIC self-disclosure on Azure platform patch status + access-log review)"
      source_yaml_id: mstic
      grade: A                            # platform-owner self-disclosure on own service is authoritative for patch state
      in_hand_this_cycle: false           # Microsoft statement not directly retrieved; reaches corpus via SecurityWeek relay
  grade_rationale: >
    Anchored B on SecurityWeek (provisional B, awaiting_ratification), the relay layer in hand.
    SecurityWeek relays two originating authorities — Wiz Research (provisional A, the discoverer)
    and Microsoft (A, the platform owner confirming patch + no-unauthorized-activity access-log
    review). Neither primary was directly retrieved this cycle, so the effective source in hand is
    a single B-grade publisher.
  provisional: true                       # securityweek anchor is provisional B (awaiting_ratification)
credibility:
  grade: 2
  checklist_passed:
    - probably_true_claims_coherent          # cloud control-plane flaw is internally coherent: Gremlin API graph-query sandbox escape (via .NET reflection) -> arbitrary code on the DB Gateway -> platform signing key ("Cosmos Master Key") -> retrieval of primary keys for any Cosmos DB account cross-tenant/cross-region. A recognized cross-tenant-isolation-failure class for managed cloud DBs.
    - probably_true_no_contradicting_ab       # no A/B-grade source contradicts; Microsoft (platform owner, A) affirmatively CONFIRMS the flaw existed and was remediated, and attests its access-log review found no unauthorized activity outside the researcher's testing
    - probably_true_ttp_consistent            # (vuln-research analogue) consistent with the managed-cloud cross-tenant control-plane flaw class the wider ecosystem has seen before (ChaosDB-class Cosmos DB key-exposure lineage); coherent with how such multi-tenant signing-key exposures are found and disclosed
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld. Although two distinct originating authorities (Wiz discovery +
    Microsoft platform confirmation) describe the same flaw — which is strong in spirit — the
    effective evidence in hand is a SINGLE relay publisher (SecurityWeek); neither the Wiz report
    nor the Microsoft statement was directly retrieved, so there is no independent second
    documentary basis in hand. Per INTEL-GRADING, one effective evidence basis cannot reach
    Confirmed -> capped at grade 2. Direct retrieval of the Wiz blog AND Microsoft's statement
    (two independent documentary bases) is the firming milestone toward grade 1.
  rationale: >
    SecurityWeek (Ionut Arghire, published 2026-07-31 05:04 EDT, in the pre-brief window) reports
    a now-patched Azure Cosmos DB flaw ("CosmosEscape," Wiz-coined) in the Gremlin API graph-query
    processor that permitted a cross-tenant primary-key exposure. Microsoft states it deployed a
    hotfix within ~2 days of the November 2025 report and completed the long-term architectural fix
    in July 2026 across all regions, with no evidence of malicious exploitation and no customer
    action required. Coherent cloud control-plane flaw, platform-owner-confirmed, single relay
    publisher in hand, no active exploitation -> Probably True.
corroboration:
  independent_sources:
    - securityweek
  independent: false
  test_result: >
    FAILS independence for grade 1 on the evidence in hand. One publisher (SecurityWeek) relaying
    Wiz + Microsoft. The two originating authorities (Wiz discovery, Microsoft platform confirmation)
    are distinct organizations with distinct evidence bases (research vs. platform access-logs/patch
    deployment) and would satisfy independence IF directly retrieved — but neither was retrieved this
    cycle, so the effective source in hand is a single relay publisher. Veto binds until an
    independent second documentary basis is in hand.
first_party_precedence:
  applied: false
  queried_indices: [archimedes, defenseclaw_local]
  query_window: "-14d (grader Rule 8 confirmatory) + collector 07:30 pre-brief sentinel sweep"
  splunk_evidence: >
    Rule 8 run by grader this cycle: (index=archimedes OR index=defenseclaw_local) NOT
    sourcetype=archimedes:* over "Cosmos" / "CosmosEscape" -> 0 events. No atomic IOCs published to
    pivot on regardless (no IPs/domains/hashes; no CVE). Visibility-bounded null — neither
    corroboration nor disconfirmation (Hard Rule 8). first_party_precedence not applied.
single_source_veto_applied: true
single_source_veto_note: >
  Applies — single effective evidence basis (one relay publisher, SecurityWeek; neither Wiz nor
  Microsoft primary directly retrieved). WEP capped at "likely." Veto lifts on direct retrieval of
  the Wiz report + Microsoft statement (two independent documentary bases) or any independent second
  publisher with a separate evidence basis. Note: WEP is largely moot here — this is a retrospective
  disclosure of a now-closed, fully-patched flaw with no forward predictive claim to carry.
wep_ceiling: likely

# Attribution — NONE (no actor named anywhere in the source)
attribution:
  attribution_made: false
  attributed_by: null
  archimedes_position: >
    No actor is named. This is a vendor-research disclosure (Wiz) of a cloud-provider-side flaw that
    Microsoft has confirmed and patched, with Microsoft attesting no malicious exploitation. Nothing
    to attribute; Archimedes originates nothing (Hard Rule 2, vacuously satisfied).

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_monitoring              # B2 clears both the B2 action floor and the C3 monitoring floor by grade; SCOPED to monitoring/awareness given low relevance (no A&D victim, no CVE, patched, no ITW, no customer action)
    - weekly_synthesis
  action_flash_exclusion_note: >
    NOT action-item / NOT FLASH — the exclusion is on RELEVANCE, not grade. Trigger 1 (critical CVE +
    active exploitation): FAIL (no CVE; Microsoft attests no exploitation). Trigger 6 (zero-day, no
    patch): FAIL (fully patched — hotfix Nov 2025 + architectural fix Jul 2026). No actor, no A&D
    victim, no first-party hit. Awareness/monitoring datum only; collector flagged inclusion as
    honestly marginal.

# A&D relevance (structural / indirect — low urgency)
ad_relevance: low
ad_relevance_rationale: >
  Azure Cosmos DB is broadly used across enterprises including A&D/DIB Azure tenants; a cross-tenant
  primary-key-exposure class is exactly the kind of multi-tenant cloud control-plane failure that
  would be a serious concern IF unpatched. But it is patched, no ITW, and no customer action is
  required per Microsoft — a retrospective disclosure of a now-closed provider-side flaw, not an
  active exposure. No A&D victim named. Rated LOW / awareness-only. Re-rate ONLY if a CVE is assigned,
  an ITW report emerges, or a residual-exposure caveat surfaces.

# Cluster metadata
cluster:
  topic: "Azure Cosmos DB 'CosmosEscape' (Wiz): a now-patched Gremlin-API sandbox-escape flaw that reached a platform signing key ('Cosmos Master Key'), enabling cross-tenant/cross-region retrieval of any Cosmos DB account's primary keys. Microsoft hotfixed within ~2 days of the Nov 2025 report; architectural fix completed Jul 2026 across all regions; no evidence of malicious exploitation; no customer action required. No CVE, no actor, no A&D victim, 0 atomic IOCs."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-31-am-003
  attribution_claims: []                  # NONE — no actor named (Hard Rule 2: empty, not omitted)

# Downstream handoff flags
analyst_review_required: false            # cleared — light-touch KAC complete 2026-07-31
analyst_review_complete: true
analyst_review_run_id: analyst-20260731-083000
red_team_review_required: false           # WEP ceiling 'likely' (< very_likely). Red-team not mandatory; unchanged by KAC.
red_team_review: null
assessment_blocked_pending_test: false    # no Test-class assumption surfaced; monitoring disposition holds
wep_ceiling_adjusted: null                # KAC did not adjust WEP — remains 'likely' (grader's single-source veto stands)
analysis_sections:
  sat_ach: null                           # not applicable — vendor-research + platform-owner-confirmed fact; no >=2 genuine competing explanations
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "CosmosEscape is a now-patched, provider-side Azure Cosmos DB cross-tenant primary-key-exposure
        flaw with no in-the-wild exploitation and no required customer action; the correct disposition
        for the A&D/DIB target is monitoring/awareness only — nothing to action."
      analyzed_at: 2026-07-31T08:34:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Grader handoff (analyst_review_required: true, WEP == likely). Light-touch KAC appropriate to a
        'likely'-grade retrospective awareness item — surface the load-bearing assumptions behind the
        monitoring disposition, flag any whose failure would change that disposition. Not a HIGH-confidence
        attribution finding; no ACH (no >=2 competing explanations).
      assumptions:
        - id: A1
          statement: "The SecurityWeek relay faithfully renders Wiz Research + Microsoft (no material distortion of scope, patch state, or the no-exploitation attestation)"
          category: source_reliability
          stated: true
          why_must_be_true: "Neither the Wiz blog nor Microsoft's statement was directly retrieved this cycle; the entire finding rests on one B-grade relay publisher accurately conveying two A-grade originating authorities"
          when_could_be_false: "Relay overstates scope, mis-dates the fix, or renders Microsoft's bounded access-log attestation as a stronger absolute claim than the primary made"
          evidence_for: [securityweek]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A2
          statement: "'No evidence of malicious exploitation' is an access-log-bounded, point-in-time attestation (absence of evidence), not proof no exploitation ever occurred"
          category: visibility
          stated: true
          why_must_be_true: "Microsoft's finding is scoped to its own access-log review coverage and retention window; a cross-tenant control-plane exploit within blind spots or beyond retention would not necessarily appear"
          when_could_be_false: "Later forensic work, a Wiz/third-party follow-up, or log gaps surface exploitation Microsoft's review did not capture"
          evidence_for: [mstic, securityweek]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A3
          statement: "The architectural fix (Jul 2026, all regions) is complete and effective, so A&D/DIB Azure Cosmos DB tenants are no longer exposed to this class"
          category: technology
          stated: true
          why_must_be_true: "The monitoring-only disposition depends on the exposure being closed; if the fix were partial or had a residual bypass, this would be an active exposure, not a retrospective"
          when_could_be_false: "Residual-exposure caveat emerges, a bypass of the architectural fix is reported, or 'all regions' proves incomplete for some tenant configurations"
          evidence_for: [mstic, securityweek]
          evidence_against: []
          confidence: medium
          centrality: critical
          classification: qualify
        - id: A4
          statement: "Because the flaw was cloud-provider-side, no customer action is required — including no need for A&D tenants to rotate Cosmos DB primary keys exposed during the Nov 2025 -> Jul 2026 window"
          category: technology
          stated: true
          why_must_be_true: "'No customer action required' (per Microsoft) presupposes no primary keys were actually retrieved by a malicious party during the exposure window; the no-action framing inherits directly from the no-exploitation finding (A2)"
          when_could_be_false: "ITW retrieval of primary keys is later confirmed for the exposure window — customers whose keys were exposed would then face a residual key-rotation obligation despite the platform-side patch"
          evidence_for: [mstic, securityweek]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A5
          statement: "First-party Splunk null (0 'Cosmos' events over the window) does not disconfirm the disposition — Archimedes has no meaningful visibility into cloud control-plane cross-tenant activity and there are no atomic IOCs to pivot on"
          category: visibility
          stated: true
          why_must_be_true: "The finding correctly treats the Splunk null as visibility-bounded (Hard Rule 8), not as corroboration; disposition does not rest on first-party telemetry here"
          when_could_be_false: "n/a for disposition — a non-null would be informative, but the null is expected and non-load-bearing"
          evidence_for: [archimedes, defenseclaw_local]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
        - id: A6
          statement: "The state stays static — no CVE, no actor, no forward predictive claim — so the item carries no attribution or exploitation-forecast burden"
          category: semantic
          stated: true
          why_must_be_true: "The finding is a retrospective disclosure of a closed flaw; there is no forward-looking assessment whose assumptions could drift"
          when_could_be_false: "A CVE is assigned or an actor is later named by a source (which would be a new grading event, not an Archimedes-originated claim)"
          evidence_for: [securityweek]
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 2
        qualify: 4
        test: 0
        reject: 0
      remediation:
        status: proceed
        blocking_assumption: null
        blocking_detail: null
        qualifying_caveats:
          - "Finding rests on a single B-grade relay (SecurityWeek); Wiz + Microsoft primaries not directly retrieved — scope/patch/no-exploitation claims inherit the relay's fidelity (A1)"
          - "'No evidence of malicious exploitation' is Microsoft's access-log-bounded, point-in-time attestation, not proof of no exploitation (A2)"
          - "Monitoring-only disposition is contingent on the Jul 2026 architectural fix being complete and residual-exposure-free (A3)"
          - "'No customer action' inherits from the no-exploitation finding; IF ITW key retrieval is later confirmed, A&D tenants with keys exposed during the Nov 2025 -> Jul 2026 window may face a residual key-rotation obligation (A4)"
        disposition_review_triggers:
          - "A CVE is assigned to CosmosEscape"
          - "Any in-the-wild exploitation report emerges (would activate A4's residual key-rotation caveat)"
          - "A residual-exposure or fix-bypass caveat surfaces (would flip A3 and re-open exposure)"
        next_action: "Proceed with monitoring/awareness disposition; no test blocks publication. Re-run KAC only if a disposition_review_trigger fires."
      recommended_wep_after_test:
        note: "No test required; WEP unchanged at 'likely' (grader's single-source veto is the binding cap, not any KAC assumption). KAC does not move the WEP for a retrospective, patched, no-ITW datum."

# vuln-tracker handoff (no CVE — watch-keyword tier at most)
vuln_tracker_handoff:
  recommended_action: watch_keyword_or_note_only
  anchor_cve: null                        # no CVE assigned; vendor-named 'CosmosEscape' cloud-provider-side flaw
  in_index: false
  patch_available: true                   # hotfix Nov 2025 + architectural fix Jul 2026 (all regions)
  active_exploitation: false              # Microsoft attests none
  note: >
    Not indexable as a tracked CVE (none assigned). Cloud-provider-side, fully remediated, no customer
    action. VW/awareness-tier at most. Direct-retrieval todo: Wiz blog + Microsoft statement would firm
    the documentary basis (candidate to lift credibility toward 1) but change nothing operationally
    (patched, no ITW).

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-31-morning]                   # briefer appends brief_ids
retracted: false
retraction_brief_id: null
---

# Wiz discloses now-patched Azure Cosmos DB cross-tenant primary-key exposure ("CosmosEscape") — Microsoft remediated, no known exploitation (awareness only)

## Summary

SecurityWeek (Ionut Arghire, 2026-07-31) relays Wiz Research and Microsoft on "CosmosEscape," a now-patched Azure Cosmos DB flaw in the Gremlin API graph-query processor. Per the reporting, researchers escaped the Gremlin sandbox to reach a platform-wide signing key that could retrieve primary keys for any Cosmos DB account across tenants and regions. Microsoft deployed a hotfix within roughly two days of the November 2025 report, completed the long-term architectural fix in July 2026 across all regions, found no evidence of malicious exploitation in its access-log review, and states no customer action is required.

Graded B2 / "likely" with the single-source veto applied: a single B-grade relay publisher (SecurityWeek) in hand, carrying two authoritative originating primaries (Wiz discovery + Microsoft platform confirmation) that were not directly retrieved this cycle. This is an awareness/monitoring datum — no CVE, no actor, no A&D victim, fully patched, no in-the-wild exploitation, and no customer action.

## Grade rationale

- **Source B** — SecurityWeek (provisional B) is the relay layer in hand; Wiz (provisional A, discoverer) and Microsoft (A, platform owner) are the originating authorities, neither directly retrieved.
- **Credibility 2** — coherent cloud control-plane flaw, affirmatively confirmed by the platform owner (Microsoft); single documentary basis in hand → cannot reach 1.
- **Single-source veto applied** — one effective evidence basis → WEP held at "likely" (largely moot for a patched, no-ITW retrospective).

## Technical detail

Recorded at class level only (Hard Rule 3 — no reproduction detail). The flaw was in Azure Cosmos DB's Gremlin API graph-query processor. Per the reporting, researchers escaped the Gremlin sandbox via .NET reflection to run code on the DB Gateway and reached a platform signing key (the "Cosmos Master Key"), which could be used to retrieve primary keys for any Cosmos DB account across tenants and regions — full cross-tenant read/write in principle. Microsoft's remediation was a fast hotfix (within ~2 days of the November 2025 disclosure) followed by a long-term architectural fix completed July 2026 across all regions. No credential values observed or stored (Hard Rule 7).

## IOCs surfaced

```yaml
atomic_iocs: []                           # no atomic network/host IOCs; cloud-service-side flaw, no CVE, no hashes/IPs/domains
cve_references: []                        # no CVE assigned (vendor-named 'CosmosEscape')
credential_exposure_detected: false
```

## Relationship to existing findings

Net-new topic; no prior corpus finding for CosmosEscape or an Azure Cosmos DB cross-tenant flaw. Thematically part of the broader cloud-provider-side / multi-tenant-isolation-failure class the corpus notes generally, but stands alone this cycle.

## A&D relevance

Structural, low urgency. Azure Cosmos DB is used broadly, including by A&D/DIB Azure tenants; a cross-tenant primary-key-exposure class would be a serious multi-tenant concern if unpatched. It is patched, with no ITW and no customer action required — awareness only, nothing to action.

## Open questions for analyst

- **Light-touch KAC expected.** The load-bearing assumptions are (a) that the SecurityWeek relay faithfully renders Wiz + Microsoft, and (b) that "no evidence of malicious exploitation" is an access-log-bounded, point-in-time attestation (absence of evidence, not evidence of absence). Neither blocks the awareness framing.
- **Direct-retrieval firming (optional).** The Wiz blog + Microsoft statement would establish two independent documentary bases (candidate to lift credibility toward 1) but would not change the operational disposition (patched, no ITW).
- **Attribution correctly absent (Hard Rule 2).** No actor named.

## Analytic notes (from analyst review)

Light-touch KAC only — no ACH (no competing explanations; this is a platform-owner-confirmed fact, not a contested attribution). Six load-bearing assumptions surfaced, none reaching Test-class. The monitoring/awareness disposition holds, and the WEP stays "likely" (the grader's single-source veto is the binding cap; no assumption moves it).

Four assumptions were Qualified rather than treated as settled. The disposition rests most heavily on A3 — that Microsoft's July 2026 architectural fix is complete and residual-free across all regions — and on A2, that "no evidence of malicious exploitation" is an access-log-bounded, point-in-time attestation, not proof. The one caveat worth carrying forward is A4: "no customer action required" inherits directly from the no-exploitation finding. If in-the-wild key retrieval is ever confirmed for the Nov 2025 to July 2026 exposure window, A&D/DIB tenants whose Cosmos DB primary keys were exposed could face a residual key-rotation obligation that the platform-side patch does not resolve.

None of that changes the current call. Proceed as awareness-only. Re-open the assessment on any of three triggers: a CVE assignment, any ITW report, or a residual-exposure/fix-bypass caveat. No attribution originated (none exists to test).

## Sources

### SecurityWeek (securityweek, digraph letter: B provisional) — 2026-07-31 05:04 EDT

- URL: https://www.securityweek.com/critical-flaw-led-to-azure-cosmos-db-pwnage/
- Author: Ionut Arghire
- Relays: Wiz Research (originating discovery, "CosmosEscape") + Microsoft (patch-status and no-unauthorized-activity attestation)
- Key claim: a now-patched Gremlin-API sandbox-escape flaw in Azure Cosmos DB reached a platform signing key enabling cross-tenant/cross-region primary-key retrieval; Microsoft hotfixed within ~2 days of the Nov 2025 report and completed the architectural fix Jul 2026; no evidence of malicious exploitation; no customer action required.
