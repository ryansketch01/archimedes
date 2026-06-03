---
finding_id: finding-2026-06-03-0002-bleepingcomputer-vs-code-github-oauth-token-theft-zero-day-askar-poc-full-disclosure-microsoft-disclosure-policy-current
created_at: 2026-06-03T08:24:00-04:00
graded_by: grader
grading_run_id: morning-20260603-080000
grading_mode: scheduled_brief
test: false
status: graded

relates_to:
  - finding-2026-06-02-0010-theregister-microsoft-nightmare-eclipse-0day-researcher-dispute-bitskrieg-secure-boot-bitlocker-forthcoming-claim
relation_type: microsoft_disclosure_policy_current_third_data_point_independent_disclosure

# Core grading (admiralty-grading skill output)
digraph: B3
digraph_layered:
  bleepingcomputer_published_vs_code_zero_day_disclosure_with_public_poc_reference: A1   # Verifiable via direct URL retrieval; BleepingComputer is publishing organization
  askar_released_public_poc_exploit_code_on_github_with_1_hour_pre_notification_to_github: B2   # BleepingComputer single-source on disclosure timeline; verifiable procedural fact
  vulnerability_class_vs_code_webview_message_passing_to_rogue_extension_install_to_github_dev_oauth_token_theft: B3   # BleepingComputer single-source on technical mechanism; no Tier-1 vendor corroboration of mechanism at this hour
  stolen_token_has_full_access_to_every_other_repo_user_has_access_to_per_askar_quote: B2   # Researcher self-statement via BleepingComputer; verifiable via researcher's public PoC
  no_cve_assigned: A1                                                                       # Verifiable absence
  no_official_patch_at_publication: A1                                                     # Verifiable absence at sweep time
  mitigation_clear_cookies_and_local_site_data_for_github_dev: B2                          # BleepingComputer single-source on mitigation guidance
  microsoft_github_no_immediate_comment_at_publication: A1                                 # Verifiable absence at sweep time
  no_in_the_wild_exploitation_reported_at_publication: A1                                  # Verifiable absence — no A-grade source claims ITW
  researcher_cited_prior_msrc_experience_as_reason_for_full_disclosure_with_minimal_vendor_notification: B2   # Researcher self-statement via BleepingComputer
  ad_defensive_implication_for_vs_code_estates_with_github_dev_integration_indirect: C2    # Grader-side structural inference; VS Code + github.dev are widely deployed at A&D primes per CLAUDE.md target profile but no A&D-prime named as victim or in-scope target
  third_data_point_in_microsoft_disclosure_policy_current_after_finding_2026_06_02_0010_nightmare_eclipse_bitskrieg_arc: A1   # Verifiable internal corpus state
  cluster_anchor: B3

digraph_anchor: >
  Cluster anchored on BleepingComputer (Sergiu Gatlan byline,
  2026-06-03 02:50 EDT in-window) covering researcher Ammar Askar's
  disclosure of a VS Code zero-day that allows GitHub OAuth token
  theft via webview-message-passing → rogue extension install →
  github.dev OAuth token extraction. PoC is public on GitHub; no
  CVE assigned; no official patch; Microsoft / GitHub provided no
  immediate comment at publication time.

  B3 (not B2 or A2) anchored because:

    - SOURCE LETTER GRADE: BleepingComputer is B (ratified per
      source-grades.yaml — fast and accurate on CVEs/ransomware).
      Sole primary at this hour. No Tier-1 A-grade vendor (Mandiant
      / Unit 42 / MSTIC / CrowdStrike / Cisco Talos / SentinelLabs /
      Volexity / Microsoft / GitHub) has published independent
      corroboration of the technical mechanism, exploitation, or
      remediation status at this hour. Per single-source veto, WEP
      ceiling capped at "likely" regardless of source grade.

    - CREDIBILITY: Walk the checklist.
      * Grade 1 (Confirmed): FAILS — single-source, no independent
        corroboration. Other potential corroborators (Microsoft
        MSRC, GitHub Security, A-grade IR firm telemetry) are
        SILENT at this hour. Silence is not corroboration.
      * Grade 2 (Probably True): FAILS — no contradicting A/B-
        grade source exists, technical claims are internally
        coherent (webview message-passing → rogue extension is a
        known VS Code attack-class), and the vulnerability class
        is TTP-consistent with known dev-tool token-theft patterns.
        However, "consistent with established TTPs for the named
        actor" condition does NOT apply because there is NO actor
        — this is a researcher disclosure, not actor activity.
        Grade 2 conditions are designed around actor-attributed
        claims; the closest analog is the technical-mechanism
        coherence layer which DOES satisfy at procedural-fact
        level.
      * Grade 3 (Possibly True): ASSIGNS — single-source,
        uncorroborated, but source is B-grade or better. Partially
        consistent with known TTPs (VS Code webview attack class
        is documented) but specific mechanism (github.dev OAuth
        token via webview-driven rogue extension install) is
        researcher-claimed and not Tier-1-verified at this hour.
        Technical claims plausible but not independently verifiable
        at sweep time.

    - Procedural facts about the DISCLOSURE EVENT itself (PoC
      released; 1-hour pre-notification to GitHub; researcher
      named as Ammar Askar; no CVE; no patch; no ITW reported)
      are at A1 layered — verifiable via the BleepingComputer
      article and the public PoC repository. The TECHNICAL
      MECHANISM CLAIM (specifically that VS Code's sandboxed
      webview message-passing system can be exploited to install
      a rogue extension that extracts github.dev OAuth tokens) is
      single-source B-grade and carries the B3 cluster-anchor
      grade per single-source veto on the substantive technical
      claim.

  Single-source veto APPLIED at cluster-anchor level on the
  technical mechanism claim. Procedural-disclosure-fact layer
  is at A1 layered. Researcher-self-statement layer at B2
  (verifiable via researcher's PoC + BleepingComputer attribution).

  Hard Rule 2: PRESERVED — no actor attribution. Researcher
  disclosure with PoC; no threat-actor activity. Askar is an
  independent security researcher.

  Hard Rule 3: BleepingComputer references the GitHub PoC URL but
  does NOT walk through exploit construction. Raw-signal records
  vulnerability mechanism CLASS at category level only. No PoC
  content is copied into the corpus.

  Hard Rule 6: PRESERVED. Direct researcher quote preserved
  verbatim at 12 words ("I really don't want to deal with MSRC
  on VSCode bugs") in raw-signal IOC field; not surfaced in finding
  body text at all.

  Hard Rule 8: Splunk first-party check ran (-30d sweep on
  github.dev + VS Code OAuth + webview + extension-install
  superset across defenseclaw_local + archimedes-NOT-archimedes-
  internal). 0 events. Per Rule 8 silence is not disconfirming.

  RELATION TO finding-2026-06-02-0010 (Microsoft disclosure-policy
  current / Nightmare-Eclipse / Bitskrieg arc): Askar's explicit
  choice to bypass MSRC's standard coordinated-disclosure window
  and release publicly with 1-hour pre-notification is the SAME
  disclosure-policy current that finding 0010 catalogued. Askar
  cited prior negative MSRC experience as his reason. This is the
  THIRD data point in the current within ~30h (Nightmare-Eclipse
  Bitskrieg-forthcoming claim + Microsoft "olive branch" Monday
  walkback statement on 2026-06-02; THIS finding on 2026-06-03;
  and finding-2026-06-03-0004 Huntress disclosure of unpatched
  Windows Search URI after Microsoft declined remediation, also
  on 2026-06-03). Briefer should consider single-cluster narrative
  framing in AM brief; grader holds three findings separate
  because they are DIFFERENT vulnerability classes with DIFFERENT
  researchers and different disclosure-trigger conditions.

source_reliability:
  grade: B
  source_name: BleepingComputer (Sergiu Gatlan byline) — Ammar Askar VS Code zero-day disclosure with public PoC, 1-hour pre-notification window to GitHub
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    Pre-assigned B per source-grades.yaml — BleepingComputer is fast
    and accurate on CVEs/ransomware; B-grade media. Sole primary at
    this hour. Microsoft / GitHub had not provided immediate comment
    at publication; no Tier-1 vendor independent corroboration of
    the technical mechanism or remediation status.
  provisional: false

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_b_grade_source
    - possibly_true_partially_consistent_with_known_vs_code_webview_attack_ttps
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable_at_sweep
  rationale: >
    Single-source B-grade with no corroboration at this hour; technical
    mechanism is plausible (VS Code webview attack-class is documented)
    but the specific github.dev OAuth token theft via webview-driven
    rogue extension install is researcher-claimed and not Tier-1-verified
    at sweep. Procedural-disclosure-fact layer (PoC released; no CVE;
    no patch; no ITW) is at A1 layered via verifiable public artifacts.

corroboration:
  independent_sources:
    - bleepingcomputer
  independent: false
  test_passed: null
  test_failed: >
    Single-source at this hour. No Tier-1 vendor (Mandiant / Unit 42 /
    MSTIC / CrowdStrike / Cisco Talos / SentinelLabs / Volexity /
    Microsoft / GitHub) independent corroboration of technical
    mechanism, exploitation, or remediation status at sweep time.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_run: >
    -30d sweep across defenseclaw_local + (archimedes NOT
    sourcetype=archimedes:*) on github.dev + VS Code + OAuth +
    webview keywords. 0 events. Per Hard Rule 8 silence is not
    disconfirming.

single_source_veto_applied: true
single_source_veto_detail: >
  Applied at cluster-anchor level on technical mechanism claim.
  BleepingComputer is sole primary at this hour; no Tier-1 vendor
  independent corroboration. WEP ceiling capped at "likely" on
  the technical mechanism + exploitation-class claim per single-
  source veto.

wep_ceiling: likely
wep_layered:
  disclosure_event_procedural_facts_poc_released_no_cve_no_patch_no_itw_no_msft_comment: very_likely   # Verifiable via direct URL + public PoC repo
  technical_mechanism_class_vs_code_webview_to_rogue_extension_to_github_dev_oauth_token: likely        # Single-source B; capped per veto
  stolen_token_full_access_to_every_other_repo_user_has_access_to: likely                              # Researcher self-statement; consistent with GitHub OAuth scope model; not Tier-1-verified for this specific PoC
  no_in_the_wild_exploitation_reported_at_publication: very_likely                                     # Verifiable absence at sweep
  third_data_point_in_microsoft_disclosure_policy_current: very_likely                                 # Verifiable internal corpus state across finding 0010 + this finding + finding 0004
  ad_defensive_implication_for_vs_code_estates_with_github_dev_integration: roughly_even_chance        # Grader-side structural inference; no A&D-prime named victim or in-scope target; defensive-action framing depends on prime-by-prime VS Code + github.dev policy

inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
  not_eligible_for:
    - flash               # B3 below B2 FLASH floor; no ITW; PoC-only
    - daily_brief_action  # B3 below B2 action floor
    - actor_profile_update # No actor attribution

# Cluster metadata
cluster:
  topic: >
    BleepingComputer reports researcher Ammar Askar disclosed a VS
    Code zero-day allowing GitHub OAuth token theft via webview-
    driven rogue extension install on github.dev. Public PoC,
    no CVE, no patch, 1-hour pre-notification to GitHub. No ITW.
    Third data point in the Microsoft disclosure-policy current
    arc (per relation to finding-2026-06-02-0010 + finding-2026-
    06-03-0004).
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-03-am-002-bleepingcomputer-vs-code-github-oauth-token-theft-zero-day-no-cve-no-patch-askar-poc-full-disclosure
  attribution_claims:
    - claimed_actor: null
      claim_text: >
        Researcher Ammar Askar disclosed the flaw with 1-hour pre-
        notification to GitHub and released a public PoC. No threat-
        actor activity reported.
      claimed_by_sources:
        - bleepingcomputer
      requires_analyst_review: false
      hard_rule_2_status: PRESERVED — researcher disclosure, no actor attribution
    - claimed_actor: null
      claim_text: >
        Askar cited prior negative MSRC experience as the reason for
        full disclosure with minimal vendor notification — pattern
        is part of the broader MSRC disclosure-policy current.
      claimed_by_sources:
        - bleepingcomputer
      requires_analyst_review: false
      hard_rule_2_status: PRESERVED — researcher self-statement; preserved as data point in disclosure-policy arc, not as actor attribution

# Downstream handoff flags
analyst_review_required: false
analyst_review_rationale: >
  WEP ceiling at "likely" on technical mechanism (single-source veto
  capped); no actor attribution; no ITW; no A&D-prime named victim.
  No SAT-ACH / SAT-KAC trigger conditions met. Re-evaluate on
  Microsoft / GitHub official response, A-grade IR firm telemetry,
  CVE assignment, or vendor patch.

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling at "likely" does not meet red-team invocation floor
  ("very likely" or higher).

red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-06-03-morning]
retracted: false
retraction_brief_id: null

# Defensive / IOC handoff flags
ioc_handoff:
  defender_relevant_iocs:
    - "Vulnerability mechanism class: VS Code webview message-passing → rogue extension install → github.dev OAuth token theft"
    - "Affected product: Visual Studio Code (with github.dev integration)"
  iocs_indirect_action: >
    Defender action framing for A&D-prime VS Code estates with
    github.dev integration (per raw-signal handoff notes, refined
    by grader):
    (a) Audit organization OAuth-app policies and approved scopes
        in GitHub Enterprise / Cloud admin panels;
    (b) Consider disabling github.dev integration in enterprise
        SSO policies pending patch;
    (c) Rotate GitHub OAuth tokens for users who have accessed
        github.dev in the prior 24h as precaution;
    (d) Monitor GitHub audit logs for unusual repo-enumeration
        API queries from user OAuth tokens;
    (e) Watch for Microsoft / GitHub official response and
        CVE assignment for definitive remediation guidance.

monitor_for_next_cycle:
  - Microsoft / GitHub official response statement
  - A-grade IR firm telemetry on attempted exploitation (Mandiant / Unit 42 / MSTIC / CrowdStrike / Cisco Talos / Volexity)
  - CVE assignment
  - Vendor patch
  - Token-theft observation in any A-grade vendor blog or first-party telemetry

vuln_tracker_handoff:
  scaffold_pending_cve_assignment: true
  scaffold_note: >
    No CVE assigned at this hour. Vuln-tracker may scaffold a
    researcher-coined-name dossier (Askar-VSCode-github.dev-OAuth)
    pending CVE assignment, or hold until CVE assignment per
    vuln-tracker discretion. If CVE assigned, scaffold as VT-* with
    Microsoft / VS Code as affected product set.

briefer_handoff:
  brief_inclusion_recommendation: monitoring_tier
  brief_substance: >
    AM brief Other Signal / Monitoring section. Briefer should
    consider clustering with finding-2026-06-03-0004 (Huntress
    Windows Search URI NTLM leak) under a "Microsoft disclosure-
    policy current" narrative framing alongside the existing
    finding-2026-06-02-0010 (Nightmare-Eclipse / Bitskrieg arc)
    if monitoring-section narrative coherence is preferred. Default
    framing: standalone monitoring item with one-line cross-reference
    to the disclosure-policy current arc.

source_grade_revision_proposed: null
---

# BleepingComputer reports VS Code GitHub OAuth Token Theft Zero-Day (Ammar Askar Public PoC, 1-Hour MSRC Notification, No CVE, No Patch)

## Summary

BleepingComputer (Sergiu Gatlan byline, 2026-06-03 02:50 EDT in-window) reports independent security researcher Ammar Askar disclosed a VS Code zero-day that allows GitHub OAuth token theft via webview-driven rogue extension install on github.dev. The vulnerability mechanism class is VS Code's sandboxed webview message-passing system being exploited to simulate keypresses and install a rogue extension; the rogue extension extracts GitHub OAuth tokens posted to github.dev and queries the GitHub API to enumerate accessible private repositories.

Public PoC exploit code is published on GitHub. No CVE assigned. No official patch. Mitigation per BleepingComputer: clear cookies and local site data for github.dev through browser settings. Microsoft / GitHub had not provided immediate comment at publication time. No in-the-wild exploitation reported.

Askar chose full disclosure with minimal vendor notification (1-hour pre-notification to GitHub before public release), citing prior negative MSRC experience. This places the disclosure as the THIRD data point in the Microsoft vulnerability-disclosure-policy current arc previously catalogued in finding-2026-06-02-0010 (Nightmare-Eclipse / Bitskrieg-forthcoming claim + Microsoft "olive branch" walkback), alongside finding-2026-06-03-0004 (Huntress Windows Search URI NTLM hash leak after Microsoft declined remediation).

Single-source veto applied on technical mechanism at cluster-anchor level (BleepingComputer sole primary); WEP ceiling "likely" on mechanism; "very_likely" on procedural disclosure facts.

## Sources

### BleepingComputer (bleepingcomputer, digraph: B3 cluster-anchor)

- URL: https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/
- Published: 2026-06-03 02:50 EDT
- Byline: Sergiu Gatlan
- Source grade: B (ratified per source-grades.yaml — BleepingComputer is fast and accurate on CVEs/ransomware)
- Key claim: Researcher Ammar Askar released exploit code for a VS Code zero-day allowing one-click GitHub OAuth token theft via webview-driven rogue extension install on github.dev; 1-hour MSRC pre-notification; no CVE; no patch; no ITW.

No corroborating sources at this hour.

## Technical detail

**Vulnerability mechanism class (per BleepingComputer + Askar PoC reference):** VS Code's sandboxed webview message-passing system can be exploited when users interact with github.dev (the browser-based code editor). Malicious JavaScript in a webview simulates keypresses to install a rogue VS Code extension. The rogue extension extracts GitHub OAuth tokens posted to github.dev and queries the GitHub API to enumerate accessible private repositories. Token scope is the user's full GitHub OAuth scope.

Hard Rule 3 discipline: vulnerability mechanism CLASS only described above. No PoC content copied; no exploit construction walkthrough. Defensive content (clear cookies + local site data for github.dev) preserved as it is publicly published mitigation guidance.

**Patch / CVE status (verifiable at sweep time):**
- No CVE assigned.
- No official patch.
- Microsoft / GitHub had not provided immediate comment at publication.
- Mitigation: clear cookies and local site data for github.dev.

**In-the-wild status:** No in-the-wild exploitation reported. PoC-only.

**Disclosure timeline:** Askar notified GitHub one hour before public disclosure. Vulnerability publicly disclosed 2026-06-03 with working PoC on GitHub.

## IOCs surfaced

No traditional IOCs (no IPs / domains / hashes / CVEs) at this hour. Class-level descriptors only:

- **Vulnerability mechanism class:** VS Code webview message-passing → rogue extension install → github.dev OAuth token theft
- **Affected product surface:** Visual Studio Code (with github.dev integration enabled)

## Relationship to existing findings

- **finding-2026-06-02-0010** — Microsoft disclosure-policy current / Nightmare-Eclipse / Bitskrieg arc. RELATION: This finding is the SECOND in-corpus data point in the Microsoft disclosure-policy current arc (after Nightmare-Eclipse forthcoming claim + Microsoft Monday walkback statement). Askar's framing of prior negative MSRC experience is consistent with the disclosure-policy current that finding 0010 catalogued.
- **finding-2026-06-03-0004** — Huntress Windows Search URI NTLM leak (filed concurrently this run). RELATION: THIRD data point in the same Microsoft disclosure-policy current arc. Briefer may consider clustering all three under a single narrative arc in the AM brief monitoring section; grader holds them separate because they are DIFFERENT vulnerability classes with DIFFERENT researchers and different disclosure-trigger conditions.

No relation to existing VT-* tracked vulnerabilities (no CVE; no tracked product / actor).

## Open questions for analyst

None at WEP "likely" — this finding does not trigger analyst SAT-ACH / SAT-KAC handoff. Monitor-only.

Re-evaluate on any of:
- Microsoft / GitHub official response statement
- A-grade IR firm telemetry on attempted exploitation
- CVE assignment
- Vendor patch
- Token-theft observation in any A-grade vendor blog or first-party telemetry

## Hard Rule Compliance

- **Hard Rule 2:** PRESERVED — no actor attribution; researcher disclosure with PoC.
- **Hard Rule 3:** PRESERVED — vulnerability mechanism described at category level only; no PoC content extracted into corpus; defender mitigation (cookies + site data clear) is publicly published defensive content.
- **Hard Rule 6:** PRESERVED — zero direct quotes used in finding body text; researcher's 12-word verbatim quote preserved in raw-signal IOC field only, not surfaced here.
- **Hard Rule 8:** Splunk -30d sweep ran on github.dev + VS Code + OAuth + webview superset; 0 events; silence not disconfirming.
