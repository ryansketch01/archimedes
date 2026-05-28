---
finding_id: finding-2026-05-28-0007-cisa-alert-supply-chain-compromises-nx-console-github-megalodon-federal-escalation
created_at: 2026-05-28T16:13:00-04:00
graded_by: grader
grading_run_id: afternoon-20260528-160000
grading_mode: scheduled_brief
test: false

# Core grading
digraph: A1
source_reliability:
  grade: A
  source_name: "CISA — Cybersecurity and Infrastructure Security Agency"
  source_yaml_id: cisa-advisories
  grade_rationale: >
    Pre-assigned A per source-grades.yaml. Official US government,
    technically verified before publication. Government-source
    escalation on threat surfaces with extensive multi-vendor corpus
    corroboration already in place (Wiz / Snyk / StepSecurity / Socket /
    Ox Security / Upwind / Sysdig / SafeDep / Semgrep / Aikido / Onapsis
    on Mini Shai-Hulud lineage; SecurityWeek / Dark Reading / Ox /
    SafeDep on Megalodon).
  provisional: false
credibility:
  grade: 1
  checklist_passed:
    - confirmed_independent_corroboration_via_existing_corpus_depth_multiple_independent_vendor_publications_on_underlying_compromises
    - confirmed_neither_source_cites_the_other_cisa_writes_its_own_alert_text_does_not_relay_a_single_vendor
    - confirmed_technical_artifacts_match_cve_2026_48027_cve_2026_45321_kev_listed_2026_05_27_vs_code_extension_version_18_95_0_all_corpus_anchored
    - confirmed_no_contradicting_a_grade_source
  rationale: >
    CISA alert is the federal-government-escalation surface on threat
    surfaces already deeply corpus-tracked. Nx Console compromise →
    GitHub repo exfil anchored at finding-2026-05-20-FLASH-0001 (TeamPCP
    self-claim, GitHub procedural confirmation, ~3,800 repos exfiltrated).
    Megalodon supply-chain intrusion anchored at finding-2026-05-25-0001
    (5,561 repos in six hours via Tiledesk org-token theft). CVE-2026-
    48027 + CVE-2026-45321 KEV-listed 2026-05-27 per finding-2026-05-27-
    0007. Multiple independent vendor publications (Wiz, Snyk, StepSecurity,
    Socket, Ox Security, Upwind, Sysdig, SafeDep, Semgrep, Aikido, Onapsis
    on Mini Shai-Hulud; SecurityWeek + Dark Reading + Ox + SafeDep on
    Megalodon) provide the independent-corroboration substrate. CISA
    alert is the government formalization. Grade 1 (Confirmed) on the
    facts; the per-actor attribution layer remains corpus-side (TeamPCP)
    rather than CISA-side (CISA does not attribute by actor in alert).
corroboration:
  independent_sources:
    - cisa-advisories
    - corpus-finding-2026-05-20-FLASH-0001-github-nx-console
    - corpus-finding-2026-05-25-0001-megalodon-tiledesk
    - corpus-finding-2026-05-27-0007-cisa-kev-three-add
    - multiple-vendor-research-publications
  independent: true
  test_passed: >
    CISA writes its own alert text independent of any single vendor;
    underlying threat surfaces have multi-vendor research substrate that
    long predates this CISA alert. Independent-corroboration condition
    is fully satisfied at corpus level.
first_party_precedence:
  applied: false
  splunk_evidence: null
  rationale: >
    No new IOCs beyond corpus-tracked CVE-2026-48027 / CVE-2026-45321 /
    VS Code Nx Console version 18.95.0 identifier (all already corpus-
    noted). Splunk hunt for these would have been triggered at original
    promotion findings; not re-invoked here.
single_source_veto_applied: false
wep_ceiling: very_likely

# Cluster metadata
cluster:
  topic: "CISA federal-escalation alert on supply-chain compromises impacting Nx Console + GitHub repositories + Megalodon — formal US-government prioritization on already-corpus-tracked SDLC threat surface"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-28-pm-004
  attribution_claims:
    - claimed_actor: null
      claimed_by_sources: [cisa-advisories]
      requires_analyst_review: false
      notes: >
        CISA does NOT attribute by actor in alert text (standard CISA
        practice). TeamPCP self-claim and corpus attribution on Nx
        Console / GitHub side are separately corpus-anchored, not CISA-
        attributed. Hard Rule 2 preserved.

# Inclusion eligibility
inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update

# Downstream handoff
analyst_review_required: true   # WEP very_likely + federal-compliance trajectory implication
analyst_review_complete: true
analyst_review_run_id: analyst-20260528-1628
red_team_review_required: true  # WEP very_likely
red_team_review:
  reviewed_at: 2026-05-28T16:48:00-04:00
  reviewed_by: red-team-analyst
  run_id: red-team-20260528-164800
  mode: post_analyst

  strongest_counter_hypothesis:
    hypothesis: >
      The "federal-escalation factual layer is solidly A1 / very_likely"
      assessment is structurally weaker than it presents, for two reasons the
      analyst surfaced but did not fully reckon with. (1) CISA's no-attribution
      framing is treated as a STRENGTH (Hard Rule 2 discipline preserved) when
      it is actually a STRUCTURAL WEAKNESS — the CISA alert is a federal-policy
      signal, not a new evidentiary contribution; its credibility-1 (Confirmed)
      grade derives entirely from corpus-anchored vendor research that long
      predated it. (2) The full CISA alert body was NOT retrieved (WAF 403); the
      finding is graded on the alert lede + RSS metadata. Grading something A1
      when its body content is unverified-against-retrieval is a quiet
      single-source-veto question — what's actually being graded is the RSS
      metadata, not the alert.
    evidence_for_counter:
      - "KAC A6: corpus-vendor substrate provides the independent corroboration, not CISA itself — explicit in the analyst's own classification (sound at high confidence)"
      - "KAC A5: full CISA alert body not retrieved due to WAF; alert body may contain attribution language not in the retrievable lede (analyst flagged this as 'qualify')"
      - "CISA alerts that prioritize already-corpus-tracked threat surfaces are policy-cascade signals, not new evidence — the value-add is regulatory trajectory, not factual confirmation. Treating the resulting digraph as A1 conflates policy weight with evidentiary weight."
      - "Multi-vendor 'substrate' (Wiz, Snyk, StepSecurity, Socket, Ox Security, Upwind, Sysdig, SafeDep, Semgrep, Aikido, Onapsis on Mini Shai-Hulud) shares common-origin telemetry (npm + GitHub registry feeds + GitHub procedural disclosure) — analyst's A6 'sound at high confidence' classification under-weights this dependency"
    evidence_against_counter:
      - "CISA process gates technical accuracy before alert publication — the federal-escalation finding is operationally true even if not all attribution language is retrievable"
      - "Vendor substrate sharing npm / GitHub feeds is not the same as sharing INTERPRETATION; each vendor's research conclusions are independently authored"
      - "RSS metadata + lede vs. full body: for a federal-escalation signal, the lede CARRIES the prioritization claim — that is the load-bearing content"
      - "Corpus-anchored attribution to TeamPCP was independently established at FLASH-0001 with TeamPCP self-claim + GitHub procedural confirmation; CISA's no-attribution framing preserves Hard Rule 2 cleanly"

  weaknesses_in_primary_assessment:
    - "Federal-escalation framing is operationally correct but the credibility-1 (Confirmed) grade rests on corpus-anchored prior findings, not on the CISA alert as a standalone source. If the corpus findings (FLASH-0001, 2026-05-25-0001) are reread for independence, several share common-origin substrate (GitHub procedural disclosure, npm registry feeds). The 'fully satisfied at corpus level' independence claim deserves more scrutiny than the grader applied."
    - "The 2026-06-10 KEV-deadline framing (13-day remediation window) is operationally relevant but the analyst's KAC A2 (DIB-prime remediation cadence matches federal-agency cadence) is Test-classified — meaning the forward-projection load-bearing claim has a Test that has not been executed. The remediation will not be observable before brief publication; A2 will remain Test-classified through the 2026-06-10 deadline. The very_likely WEP attaches to the federal-escalation factual layer but the BRIEF NARRATIVE that reaches the reader fuses the federal-escalation factual layer with the DIB-prime remediation forecast — the latter is structurally weaker than the former and the analyst flagged this but did not enforce a brief-narrative split."
    - "VS Code automatic-update silent-distribution claim (A3, 'sound at high confidence') assumes enterprise GPO did NOT gate the update at DIB primes. This is enterprise-IT operational reality that varies WIDELY by prime. The 'silent distribution to all systems' framing is technically accurate for stock VS Code but overstated for managed-developer-environment primes (Boeing's GitHub Enterprise + VS Code policy at managed-developer hosts is notably stricter than the generic 'systems with Nx Console previously installed' framing implies). Analyst classified as 'sound' — should be 'qualify' on the at-DIB-primes-specifically narrative."
    - "TeamPCP operational continuity since 2026-05-20 (A4, qualify, low confidence) is implicit in the federal-escalation framing. If TeamPCP has been disrupted (LE action, BreachForums seizure affecting affiliate funnel) between 2026-05-20 and 2026-05-28, the CISA federal-escalation framing remains operationally correct but the active-threat implication softens. Analyst flagged this; the brief narrative does not enforce the caveat."
    - "Federal-deadline-density framing ('paired with LiteSpeed CVE-2026-48172 + Exchange OWA CVE-2026-42897 KEV deadlines') is a structural argument the analyst did not pressure-test. Federal-deadline density is operationally meaningful at federal agencies (where BOD-22-01 is contractual obligation) but indirectly meaningful at DIB primes (where DFARS 252.204-7012 obligation flows through contracting officers, not directly through KEV-deadline). The brief narrative likely conflates these two cadences."

  strongest_counter_wep: likely

  recommendation: qualify

  qualifying_language_suggested: >
    "CISA's 2026-05-28 alert formally prioritizes federal-agency response to the
    Nx Console / GitHub and Megalodon supply-chain compromises that the corpus
    has tracked since 2026-05-20 (per corpus-anchored vendor research from Wiz,
    Snyk, StepSecurity, Socket, Ox Security, Upwind, Sysdig, SafeDep, Semgrep,
    Aikido, Onapsis on Mini Shai-Hulud and SecurityWeek / Dark Reading / Ox /
    SafeDep on Megalodon). The federal-prioritization signal is the new content;
    the underlying technical picture was already established. DIB-prime
    remediation cadence to the 2026-06-10 KEV deadline (CVE-2026-48027,
    CVE-2026-45321) flows through DFARS 252.204-7012 contractual cascade rather
    than direct BOD-22-01 obligation and is structurally inferred — Splunk
    first-party hunt for Nx Console 18.95.0 in defenseclaw_local recommended
    regardless of brief inclusion."

  specific_tests_that_would_resolve:
    - "Retrieve full CISA alert body (operator manual fetch through non-WAF route) to confirm no attribution language and confirm vector-class scope matches the RSS lede"
    - "Splunk hunt for Nx Console 18.95.0 in defenseclaw_local — the analyst recommended this; outcome is binary (presence = first-party validation of silent-distribution at minimum one monitored environment; absence = no first-party visibility, which is informative but not conclusive)"
    - "Track first DCSA / DFARS-OUSD-A&S guidance update referencing CVE-2026-48027 or Nx Console specifically (cadence test for the regulatory-cascade A1 assumption)"
    - "By 2026-06-10: track federal-agency KEV-deadline compliance signal; if federal agencies miss the deadline, the DIB-prime cadence forecast is over-confident in either direction"

  wep_adjustment_recommended: very_likely  # ceiling preserved on the federal-escalation factual layer; qualifying language applied to forward-projection and 'silent distribution at DIB primes' claims
  wep_adjustment_rationale: >
    The federal-escalation factual layer (CISA published an alert formally
    prioritizing this threat surface; the alert names Nx Console + Megalodon
    + version 18.95.0 + the KEV-deadline pair) is true and stands at very_likely
    even with full body unretrieved — the RSS metadata + lede carry the
    prioritization claim. The structural weakness lives in the FORWARD-PROJECTION
    layer (DIB-prime remediation cadence, DCSA/DFARS/CMMC guidance integration,
    silent-distribution at managed-developer-environment primes). The analyst
    already classified A2 as Test-blocked at the forward-projection layer and
    proposed proceed_with_test_flag. Red-team agrees with that disposition but
    flags that the BRIEF NARRATIVE must enforce the split — the very_likely
    ceiling attaches ONLY to the factual federal-escalation layer, not to the
    DIB-prime-cadence forward-projection that the brief is likely to fuse into
    the same narrative paragraph.

  contrarian_ach_result:
    re_ran_from_contrarian_position: false
    rationale: >
      Analyst did not run ACH (correctly — CISA does not attribute, and the
      TeamPCP corpus-side attribution was ACH'd at finding-2026-05-20-FLASH-0001).
      No attribution-question is in play here. Red-team did not re-run ACH —
      the structural weakness is at the KAC / brief-narrative layer, not the
      hypothesis layer.

  notes: >
    Not blocking. Recommendation is qualify — specifically, briefer must SPLIT
    the federal-escalation factual layer (rides at very_likely) from the DIB-
    prime remediation forecast and silent-distribution-at-primes claims (ride
    at "likely" with explicit caveats). The standing carry-forward across
    PM-28 → AM-29 → weekly synthesis framing the analyst recommended is
    structurally correct; the carry-forward should track the actual 2026-06-10
    KEV-deadline outcome at federal agencies as the first-resolvable test,
    NOT extrapolate to DIB-prime cadence assumptions. The Splunk first-party
    hunt for Nx Console 18.95.0 should run regardless of brief inclusion — if
    that hunt returns hits, the WEP on the threat-surface layer rises and the
    forward-projection layer becomes operationally salient rather than
    structurally inferred.
analysis_sections:
  sat_ach: null  # not warranted — CISA does not attribute; underlying corpus-anchored attribution (TeamPCP) was ACH'd at earlier findings; federal-escalation layer is the new content here and is not an attribution question
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "CISA's 2026-05-28 alert is the federal-government-prioritization
        layer on a supply-chain threat surface the corpus has tracked for ~8
        days; DCSA / DFARS / CMMC implementation guidance is likely to
        incorporate the Nx Console / Megalodon vector class; DIB primes on
        DFARS 252.204-7012 obligations are on accelerated 13-day remediation
        cadence to the 2026-06-10 KEV deadlines for CVE-2026-48027 and
        CVE-2026-45321" (paraphrased CISA + analyst forward-projection).
      analyzed_at: 2026-05-28T16:28:00-04:00
      analyzed_by: analyst
      invoking_context: "Analyst review on A1 / very_likely federal-escalation finding; load-bearing forward-projection on DIB-prime remediation cadence + DCSA/DFARS/CMMC trajectory"
      assumptions:
        - id: A1
          statement: "CISA's federal-prioritization signal will translate into DCSA / DFARS / CMMC implementation guidance updates incorporating this vector class"
          category: capability
          stated: true
          why_must_be_true: "Forward-projection on compliance trajectory rests on this regulatory-cascade mechanism"
          when_could_be_false: "DCSA / DFARS / CMMC updates typically lag CISA alerts by months; specific vector-class integration is not automatic"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A2
          statement: "DIB primes will meet the 2026-06-10 (13-day) KEV deadline for CVE-2026-48027 + CVE-2026-45321 reliably"
          category: capability
          stated: false
          why_must_be_true: "Federal-deadline-density framing assumes prime remediation cadence matches federal-agency cadence"
          when_could_be_false: "BOD-22-01 contractual extension to DIB via DFARS 252.204-7012 is not 1:1; prime remediation backlog and patch-window scheduling vary widely"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: critical
          classification: test
          proposed_test: >
            Query first-party Splunk (defenseclaw_local / archimedes) for
            Nx Console version 18.95.0 presence in any monitored environment;
            also query DCSA / DFARS published guidance for any prime-named
            remediation status update. Test is bounded — outcome is either
            'observed Nx Console 18.95.0 presence (red flag)' or 'no first-
            party visibility' (most likely; informative but not conclusive).
        - id: A3
          statement: "VS Code automatic-update mechanism silently delivered malicious version 18.95.0 to all systems with Nx Console previously installed"
          category: technology
          stated: true
          why_must_be_true: "Severity narrative on silent-distribution depends on this technical claim"
          when_could_be_false: "Auto-update may have been disabled / sandboxed / gated by enterprise GPO at DIB primes; user-confirmation may have been required"
          evidence_for: [cisa-advisories, corpus-finding-2026-05-20-FLASH-0001-github-nx-console]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A4
          statement: "TeamPCP (corpus-anchored attribution on Nx Console / GitHub side) operational continuity since 2026-05-20 has not been disrupted"
          category: actor_operational_status
          stated: false
          why_must_be_true: "Federal-escalation framing implicitly assumes the threat actor remains operational"
          when_could_be_false: "Undisclosed LE disruption, infrastructure takedown, BreachForums seizure affecting affiliate funnel"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A5
          statement: "CISA does not attribute the Nx Console / Megalodon compromises by actor (standard CISA practice)"
          category: source_reliability
          stated: true
          why_must_be_true: "Hard Rule 2 discipline on attribution provenance"
          when_could_be_false: "Full CISA alert body (not retrieved due to WAF) may contain attribution language not in retrievable lede"
          evidence_for: [cisa-advisories]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A6
          statement: "The corpus-anchored multi-vendor research substrate (Wiz / Snyk / StepSecurity / Socket / Ox Security / Upwind / Sysdig / SafeDep / Semgrep / Aikido / Onapsis on Mini Shai-Hulud; SecurityWeek / Dark Reading / Ox / SafeDep on Megalodon) provides the independent corroboration"
          category: source_reliability
          stated: true
          why_must_be_true: "Credibility 1 (Confirmed) rests on the multi-vendor substrate, not CISA alone"
          when_could_be_false: "Substrate vendors may have shared common-origin telemetry (npm / GitHub registry feeds); not all are truly independent"
          evidence_for: [multiple-vendor-research-publications]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A7
          statement: "VS Code extension ecosystem is materially embedded in A&D-prime SDLCs (Boeing / Lockheed / Raytheon / Northrop Grumman / GD / BAE / L3Harris / Leidos)"
          category: target_profile
          stated: true
          why_must_be_true: "A&D-relevance narrative depends on extension-ecosystem footprint at primes"
          when_could_be_false: "Some primes may operate hardened / locked-down developer environments excluding third-party VS Code extensions"
          evidence_for: []
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A8
          statement: "Federal-escalation visibility through CISA alert + KEV listing will be operationally noticed by DIB-prime IT compliance teams within the 13-day window"
          category: visibility
          stated: false
          why_must_be_true: "Compliance-trajectory mechanism assumes downstream awareness"
          when_could_be_false: "DIB-prime IT compliance teams may have already remediated since 2026-05-20 corpus-anchor; new federal-escalation signal may be redundant"
          evidence_for: []
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 3
        qualify: 4
        test: 1
        reject: 0
      remediation:
        status: proceed_with_test_flag
        test_assumption: A2
        test_detail: >
          A2 (DIB-prime remediation cadence matches federal-agency cadence)
          is Test-classified but the Test does NOT block the federal-
          escalation finding itself — only the forward-projection layer
          ('DIB primes will meet 2026-06-10 deadline'). The CISA-alert
          factual layer (A1 + A6) stands at very_likely independently.
          Briefer should treat the DIB-prime remediation forecast as a
          structural inference flagged for monitoring rather than a
          confirmed expectation.
        qualifying_caveats:
          - "DCSA / DFARS / CMMC guidance integration of Nx Console / Megalodon vector class is structural forecast; lag typically months not days"
          - "VS Code auto-update silent-distribution assumes enterprise GPO did NOT gate / sandbox the update — varies by prime"
          - "TeamPCP operational continuity since 2026-05-20 assumed but not directly evidenced this sweep"
          - "Full CISA alert body not retrieved (WAF); retrievable lede may not contain all attribution / scope language"
          - "VS Code extension ecosystem footprint at A&D primes assumed material; some primes operate hardened developer environments"
        next_action: >
          Brief at very_likely on factual federal-escalation layer; flag
          DIB-prime remediation cadence as monitor-only forward-projection.
          Splunk first-party hunt for Nx Console 18.95.0 in defenseclaw_local
          regardless of brief inclusion. Track 2026-06-10 KEV deadline
          paired with adjacent LiteSpeed / Exchange OWA deadlines for
          federal-deadline-density signal in AM-29 brief.
      recommended_wep_after_test:
        if_dib_remediation_cadence_validated: very_likely
        if_dib_remediation_cadence_unsupported: very_likely  # core CISA-escalation factual layer unaffected; forward-projection drops
        if_splunk_hunt_returns_hits: very_likely  # first-party telemetry validation lifts confidence on the threat-surface but doesn't change CISA-escalation grade

# Red-team downstream flags
red_team_review_complete: true
red_team_outcome: qualify
wep_ceiling_adjusted_by_red_team: false  # ceiling preserved on federal-escalation factual layer; qualifying language and brief-narrative split required for forward-projection layer
wep_ceiling_adjustment_reason_red_team: >
  Federal-escalation factual layer (CISA published alert; RSS lede carries the
  prioritization claim) survives at very_likely. Forward-projection layer
  (DIB-prime remediation cadence at 2026-06-10 KEV deadline; DCSA/DFARS/CMMC
  guidance integration; silent-distribution-at-primes) is structurally weaker
  and should ride at "likely" with explicit caveats. Briefer must enforce the
  split rather than fusing into one narrative paragraph.
publication_blocked: false

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-28-afternoon]
retracted: false
retraction_brief_id: null
---

# CISA Federal-Escalation Alert — Nx Console / GitHub + Megalodon Supply-Chain Compromises Formally Prioritized

## Summary

CISA on 2026-05-28 published an alert formally prioritizing federal-agency response to "multiple emerging software supply chain intrusion campaigns targeting developer ecosystems Continuous Integration/Continuous Development (CI/CD) pipelines" — naming both the **Nx Console malicious VS Code extension → GitHub employee device → ~3,800 internal repo exfil** chain (corpus-anchored to TeamPCP per finding-2026-05-20-FLASH-0001) and the **Megalodon supply-chain campaign** (corpus-anchored to finding-2026-05-25-0001, 5,561 repos in six hours via Tiledesk org-token theft). The alert names the malicious extension version (18.95.0) distributed via VS Code's automatic update mechanism, meaning systems with Nx Console previously installed may have received the malicious build silently. CVE-2026-48027 (Nx Console) and CVE-2026-45321 (TanStack Mini Shai-Hulud) carry federal KEV dueDates of 2026-06-10 (13 days from this brief). The alert is the formal US-government escalation on SDLC threat surfaces the corpus has tracked for ~8 days — DIB-prime SDLC implications via DCSA / DFARS 252.204-7012 / CMMC guidance are likely to follow.

## Sources

### CISA Alert (cisa-advisories, digraph: A)

- URL: https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories
- Published: 2026-05-28T12:00:00Z (08:00 EDT)
- Retrieval: Body 403 on direct fetch (standard cisa.gov/news-events WAF pattern); alert metadata + lede via all.xml RSS feed which is the productive endpoint.
- Key claim (lede, verbatim ≤15 words per Hard Rule 6 — paraphrased here): CISA prioritizing response to multiple emerging supply-chain campaigns targeting developer CI/CD pipelines; Nx Console + Megalodon named.

### Corpus-anchored independent corroborators (multi-vendor)

- finding-2026-05-20-FLASH-0001 — GitHub ~3,800 repo exfil via Nx Console; TeamPCP self-claim + GitHub procedural confirmation
- finding-2026-05-25-0001 — Megalodon GitHub workflow_dispatch mass-backdoor; 5,561 repos in six hours via Tiledesk org-token theft (SecurityWeek + Dark Reading + Ox Security + SafeDep)
- finding-2026-05-27-0001 — CrowdStrike GlassWorm takedown (partial adjacency to broader SDLC ecosystem)
- finding-2026-05-27-0007 — CISA KEV three-add (CVE-2026-48027 Nx Console + CVE-2026-45321 TanStack + CVE-2026-8398 Daemon Tools, dueDate 2026-06-10 for first two)
- Vendor research substrate on Mini Shai-Hulud lineage: Wiz, Snyk, StepSecurity, Socket, Ox Security, Upwind, Sysdig, SafeDep, Semgrep, Aikido, Onapsis

## Technical detail

### Vector class
- **Compromise of Nx developer systems** as precursor (prior intrusion)
- **Poisoned third-party VS Code extension** as second-stage delivery
- **GitHub employee device compromise** as exfil pivot
- **VS Code automatic update mechanism** as silent-distribution channel — malicious version 18.95.0 reached systems with Nx Console previously installed without user opt-in

### Federal compliance trajectory
- **CVE-2026-48027 (Nx Console) KEV dueDate: 2026-06-10** (13 days)
- **CVE-2026-45321 (TanStack Mini Shai-Hulud) KEV dueDate: 2026-06-10** (13 days)
- DIB primes operating to BOD-22-01-equivalent contractual obligations under DFARS 252.204-7012 are on accelerated remediation cadence
- DCSA / DFARS 252.204-7012 / CMMC implementation guidance is now likely to incorporate the Nx Console / Megalodon vector class explicitly

### A&D / DIB relevance
CI/CD pipelines, VS Code extensions, and GitHub repos are deeply embedded in A&D-prime SDLCs. Boeing, Lockheed, Raytheon, Northrop Grumman, GD, BAE, L3Harris, Leidos all run extensive enterprise GitHub estates and operate VS Code with extension ecosystems. The federal-prioritization signal raises DCSA / DFARS / CMMC visibility on these surfaces.

## IOCs surfaced

```yaml
cves:
  - CVE-2026-48027    # Nx Console (KEV-listed 2026-05-27, dueDate 2026-06-10)
  - CVE-2026-45321    # TanStack Mini Shai-Hulud (KEV-listed 2026-05-27, dueDate 2026-06-10)
vs_code_extension_versions:
  - "Nx Console 18.95.0 — malicious build"
affected_software_distribution_mechanisms:
  - VS Code automatic update mechanism (silent delivery of 18.95.0)
ip_addresses: []
domains: []
hashes: []
```

No new IOCs beyond corpus-tracked items.

## Relationship to existing findings

This finding is the **federal-escalation layer** on a threat surface the corpus has tracked since 2026-05-20:

- finding-2026-05-20-FLASH-0001 (Nx Console → GitHub ~3,800 repos)
- finding-2026-05-25-0001 (Megalodon → 5,561 repos)
- finding-2026-05-27-0001 (CrowdStrike GlassWorm — partial adjacency)
- finding-2026-05-27-0007 (CISA KEV three-add)
- TeamPCP roster #001 (HIGH threat-level)
- VT-006 Mini Shai-Hulud + VT-009 Nx Console malicious extension

The value of this finding over priors: **government formalization**. The corpus already had the threat picture; CISA now provides the federal-prioritization endorsement that will drive DCSA / DFARS / CMMC compliance trajectories at DIB primes.

## Open questions for analyst

- **Federal compliance trajectory.** Likely DCSA / DFARS 252.204-7012 / CMMC implementation guidance updates incorporating Nx Console / Megalodon vector class. Operator should be ready to surface to DIB-prime IT compliance counterparts.
- **Standing carry-forward.** Pairs with LiteSpeed CVE-2026-48172 + Exchange OWA CVE-2026-42897 KEV deadlines (2026-05-29, tomorrow) for a federal-deadline-density signal across the PM-28 → AM-29 brief windows.
- **Coverage decision.** Brief is at risk of repetition fatigue on Nx Console / Megalodon (multiple corpus surfaces already covered). Briefer should treat this as a **government-escalation UPDATE block** under the standing SDLC threat surface theme, not a fresh story. Anti-repetition consideration is significant here.
- **SAT-KAC candidate.** Assumption "DIB primes are remediating to KEV deadlines reliably" — analyst KAC on whether prime SDLC remediation cadence matches federal-agency cadence at the 2026-06-10 deadline.

## Source notes

- CISA alert body not retrieved due to cisa.gov WAF pattern; metadata + lede via /cybersecurity-advisories/all.xml RSS feed.
- All quotes ≤15 words per Hard Rule 6.
- Hard Rule 2 preserved: CISA does not attribute by actor; the TeamPCP corpus-side attribution is separately corpus-anchored.

## Analytic notes (from analyst review)

KAC surfaces eight assumptions on a finding whose factual layer (CISA federal-escalation alert on already-corpus-tracked SDLC threat surface) is genuinely A1 / very_likely and not the load-bearing analytic risk. The risk surface lives in the forward-projection layer: DIB-prime remediation cadence at the 2026-06-10 KEV deadline (A2, Test-classified) and DCSA / DFARS / CMMC implementation guidance integration of this vector class (A1, qualify). Both are structural inferences about regulatory-cascade behavior, not factual claims about the CISA alert itself. ACH is not warranted — CISA does not attribute, and the TeamPCP corpus-side attribution was already established at finding-2026-05-20-FLASH-0001.

WEP very_likely is defensible on the federal-escalation factual layer. The briefer should preserve the CISA-escalation framing as the new content and treat the DIB-prime remediation forecast as a monitor-only structural inference, not a confirmed expectation. Single point of failure: if the full CISA alert body (not retrieved due to cisa.gov WAF) contains attribution language not in the retrievable lede, that would shift Hard Rule 2 discipline. Splunk first-party hunt for Nx Console 18.95.0 in defenseclaw_local recommended regardless of brief inclusion.
