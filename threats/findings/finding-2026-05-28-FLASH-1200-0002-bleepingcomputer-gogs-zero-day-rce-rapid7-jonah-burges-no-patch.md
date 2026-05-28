---
finding_id: finding-2026-05-28-FLASH-1200-0002
created_at: 2026-05-28T12:40:00-04:00
graded_by: grader
grading_run_id: flash-grade-20260528-120000
grading_mode: flash_fast_path
flash_path: true
test: false
trigger_id:
  - zero-day-no-patch    # Trigger 6 — Rapid7 (A provisional) disclosed argument-injection RCE in Gogs after 60+ days vendor silence; no CVE assigned; no patch; ~2,400 exposed instances; effectively pre-auth on default open-registration config

# Core grading (admiralty-grading skill output)
digraph: A2
digraph_layered:
  rapid7_disclosure_of_argument_injection_rce_in_gogs_rebase_handling: A2     # Rapid7 vendor research practice (A provisional per source-grades.yaml); BleepingComputer B-grade relay; effectively single-source-primary on the vulnerability disclosure layer (Rapid7 is the originating researcher)
  no_cve_assigned_at_disclosure_time: A1                                       # Verifiable absence — both Rapid7 and BleepingComputer-relay attest absence; MITRE/NVD lookup at sweep time confirms no CVE for this specific argument-injection flaw
  no_patch_available_at_disclosure_time: A1                                    # Verifiable absence per Rapid7 disclosure + BleepingComputer relay; Gogs maintainer GitHub repo at sweep time shows no fix commit referencing this issue
  rapid7_disclosure_timeline_march_17_report_to_may_28_public: A2              # Rapid7 vendor procedural fact; consistent with 60-day disclosure standard for vendor-silence scenarios
  affected_versions_0_14_2_and_0_15_0_dev: A2                                  # Rapid7-attested via BleepingComputer relay
  argument_injection_in_pull_request_rebase_handling_mechanism: A2             # Rapid7 vendor research; consistent with known argument-injection vulnerability class in git-wrapper-tooling (CVE-2017-1000117, CVE-2022-24765, prior Gogs CVE-2025-8110 historical precedent)
  authentication_pre_condition_registered_user_required: A1                    # Rapid7 vendor-attested technical fact
  effective_pre_auth_on_default_open_registration_configuration: A2            # Rapid7 vendor characterization; consistent with Gogs default config posture per public docs; corpus-rule-of-thumb: open-registration self-hosted services are functionally unauthenticated for any reachable instance
  shadowserver_2400_plus_exposed_instances: B2                                 # Shadowserver foundation IOC-and-exposure scanning is B-grade per technical-source category (factual scan data; cited via BleepingComputer relay, not directly retrieved this sweep)
  shodan_1000_plus_ips_with_gogs_fingerprint: A2                               # Shodan A-grade for facts per source-grades.yaml; cited via BleepingComputer relay; consistent with Shadowserver attestation
  geographic_skew_asia_and_europe_primary: B3                                  # Cited via BleepingComputer relay of Shadowserver/Shodan; geographic-distribution claim is interpretive layer on raw scan data; single-source via BleepingComputer
  no_confirmed_in_wild_exploitation_of_this_specific_zero_day: A1              # Verifiable absence at sweep time; Rapid7 + BleepingComputer both attest absence
  cve_2025_8110_historical_exploitation_of_related_gogs_flaw: A2               # Verifiable historical fact per BleepingComputer relay; CVE record in NVD is A-grade; BleepingComputer explicit that this is HISTORICAL CONTEXT not current-flaw attribution
  no_actor_attribution: A1                                                      # Verifiable absence; Rapid7 + BleepingComputer name no actor; Hard Rule 2 prevents Archimedes from originating
  no_a_and_d_prime_named_as_victim: A1                                          # Verifiable absence
  cluster_anchor: A2

digraph_anchor: >
  Cluster digraph A2 anchored on the load-bearing operational claim:
  Rapid7 (A-grade provisional per source-grades.yaml; senior security
  researcher Jonah Burges byline) discloses a previously-undisclosed
  zero-day argument-injection vulnerability in Gogs (self-hosted Git
  service) that allows registered users to obtain remote code
  execution on Internet-facing instances. The flaw arises in
  pull-request rebase handling — malicious branch names are passed
  to `git rebase` operations during the "Rebase before merging" flow.
  No CVE assigned at disclosure time. No patch available. Rapid7
  reported the flaw to Gogs maintainers on 2026-03-17; maintainers
  acknowledged on 2026-03-28 but released no fix; after ~60 days of
  vendor silence, Rapid7 publicly disclosed on 2026-05-28. Affected
  versions: 0.14.2 and 0.15.0+dev. Although a registered Gogs user
  account is technically required to trigger the flaw, Gogs ships
  with open registration enabled by default, so any unauthenticated
  attacker reaching the instance can self-register and exploit it
  — the effective attack surface is unauthenticated for any
  default-config deployment. Install base: Shadowserver tracks
  2,400+ Internet-exposed Gogs instances; Shodan finds 1,000+ IPs
  with Gogs fingerprint; geographic skew is Asia and Europe primary.
  No confirmed in-wild exploitation of this specific zero-day at
  sweep time. A related Gogs flaw — CVE-2025-8110 — has been
  actively exploited in past zero-day attacks; BleepingComputer
  cites this as HISTORICAL CONTEXT only and does NOT claim
  CVE-2025-8110 = the current flaw.

  A2 (not A1) holds at the cluster anchor because:
    - Rapid7 is the single originating primary source on the
      vulnerability disclosure layer. BleepingComputer (B-grade
      per source-grades.yaml; Sergiu Gatlan byline; 2026-05-28
      10:25 EDT in-window) is a faithful B-grade relay of the
      Rapid7 disclosure. The independence test FAILS on the
      vulnerability-existence layer because BleepingComputer is
      a rewrite/aggregation of the Rapid7 disclosure — per
      INTEL-GRADING.md "One is a rewrite/aggregation of the
      other ... is NOT corroboration."
    - The vulnerability disclosure itself (the flaw exists, the
      mechanism class is rebase-handling argument injection, no
      patch, no CVE assigned, affected versions are 0.14.2 and
      0.15.0+dev) is A2 because Rapid7 is A-grade vendor research
      with verifiable disclosure timeline (March 17 report,
      March 28 vendor acknowledgement, May 28 public disclosure
      — consistent with industry-standard 60-day disclosure for
      vendor-silence scenarios).
    - The INSTALL-BASE EXPOSURE layer carries cross-vendor
      attestation: Shadowserver (B-grade technical-source-class)
      and Shodan (A-grade for facts) both attest to thousands of
      exposed instances. This is independent corroboration on the
      exposure layer (Shadowserver and Shodan are separate
      scanning operations with separate methodology); this layer
      is A1 on the existence-of-exposure dimension, but A2
      cluster-anchor takes the load-bearing vulnerability layer.

  Single-source veto APPLIES on the "imminent exploitation"
  forward-projection layer per Trigger 6 evaluation. Rapid7 does
  not attest that exploitation is imminent — that is the FLASH
  trigger heuristic. The defensible WEP on the
  exploitation-imminence layer is "likely" (not "very likely")
  given (a) the historical pattern of Gogs CVE exploitation
  (CVE-2025-8110); (b) the effective-pre-auth attack surface on
  default-config deployments; (c) the public disclosure event
  itself materially raises exploitation risk against unpatched
  instances; (d) the 2,400-plus install-base provides a target
  population large enough to attract opportunistic mass
  exploitation but not so large as to be defensively
  unmanageable.

  Single-source veto does NOT apply on the load-bearing
  vulnerability disclosure facts (Rapid7 is the originating
  primary source; the disclosure is the fact, not an
  observation to be corroborated). Credibility 2 holds on the
  vulnerability-existence layer because the claim is internally
  coherent (mechanism class is documented, affected versions
  are specified, disclosure timeline is standard, vendor
  acknowledgement attested), Rapid7's track record on vendor
  research is established, and no contradicting A/B source has
  surfaced.

  Hard Rule 2 binding constraint:
    - No threat actor or nation-state is attributed to the
      historical CVE-2025-8110 exploitation per BleepingComputer
      relay of Rapid7 disclosure. Archimedes does NOT originate
      an attribution on either the current or historical flaw.
    - No A&D-prime named as victim. Gogs is self-hosted
      developer tooling; A&D relevance is structural-inferential
      (self-hosted Git platform competitive with Gitea / GitLab
      / Forgejo in the DIB / engineering-team setting where
      ITAR / CMMC compliance prefers on-premise SCM).

  Hard Rule 3 binding constraint: NO PoC content or exploit
  walkthrough extracted to raw-signal or this finding. The
  mechanism summary above ("argument injection in pull-request
  rebase handling — malicious branch names passed to git rebase")
  is architectural-class only, not an exploitation guide.
  Rapid7's primary disclosure post may include more technical
  detail; Archimedes refers operators to the Rapid7 blog
  directly for full vulnerability context.

  Hard Rule 8 binding constraint: Splunk first-party check on
  "gogs" + related keywords at -30d returned 0 hits on
  defenseclaw_local + archimedes. First-party silence is NOT
  contradiction; credibility grade unchanged.
  first_party_precedence.applied: false.

source_reliability:
  primary:
    grade: A
    source_name: "Rapid7 (Labs / IR blog) — Jonah Burges, senior security researcher"
    source_yaml_id: rapid7
    grade_rationale: >
      Pre-assigned A per source-grades.yaml (provisional pending
      ratification; first cited via 2026-05-06-FLASH-0002
      MuddyWater attribution). Rapid7 is the originating
      researcher on this zero-day disclosure; vendor research
      practice with established track record on vulnerability
      research and IR. Direct retrieval of Rapid7 primary
      disclosure not confirmed this sweep — Rapid7 URL not
      explicitly captured in raw-signal frontmatter; the
      directly-retrieved evidence basis is BleepingComputer's
      relay. Librarian flagged for Rapid7 primary direct
      retrieval at next pass.
    provisional: true
    awaiting_ratification: true
    awaiting_direct_retrieval: true
  relay:
    grade: B
    source_name: "BleepingComputer — Sergiu Gatlan byline"
    source_yaml_id: bleepingcomputer
    grade_rationale: >
      Pre-assigned B per source-grades.yaml. Fast and accurate on
      CVEs and vulnerability disclosures; faithful relay of Rapid7
      primary disclosure with no editorial inflation observed in
      this surface. Sergiu Gatlan byline. Published 2026-05-28
      10:25 EDT in-window.
    provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent
    - probably_true_no_contradicting_ab
    - probably_true_claims_coherent
  rationale: >
    Probably True (2). Rapid7 vulnerability disclosure is
    internally coherent: (a) argument-injection in git-wrapper
    tooling is a documented vulnerability class with prior CVE
    precedents (CVE-2017-1000117, CVE-2022-24765, Gogs prior
    CVE-2025-8110); (b) the rebase-handling code path is a
    plausible injection sink given how `git rebase` consumes
    branch names; (c) the affected-version specification (0.14.2
    and 0.15.0+dev) is precise and verifiable against the Gogs
    GitHub release history; (d) the disclosure timeline (March 17
    report, March 28 vendor acknowledgement, May 28 public
    disclosure) is consistent with industry-standard 60-day
    vendor-silence disclosure; (e) the effective-pre-auth
    characterization on default-config deployments is consistent
    with Gogs's documented default of open registration; (f) no
    contradicting A/B-grade source has surfaced disputing
    Rapid7's disclosure or characterization.

    Credibility cannot reach 1 (Confirmed) on the
    vulnerability-existence layer because the disclosure is
    originating-research-class — Rapid7 is the single primary
    source for the disclosure itself, and BleepingComputer is a
    faithful aggregation not an independent telemetry source.

corroboration:
  independent_sources_on_vulnerability_disclosure_layer:
    - rapid7                        # primary disclosure
    - bleepingcomputer              # faithful relay (NOT independent corroboration)
  independent_on_vulnerability_disclosure_layer: false
  test_failed_reason: >
    BleepingComputer is a rewrite/aggregation of the Rapid7
    primary disclosure. Per INTEL-GRADING.md: "One is a
    rewrite/aggregation of the other ... is NOT corroboration."
    BleepingComputer relays Rapid7 faithfully; this is one
    effective source on the vulnerability-existence and
    mechanism-class layer.

  layers_passing_independence:
    install_base_exposure:
      independent_sources:
        - shadowserver-foundation       # 2,400+ exposed instances
        - shodan                         # 1,000+ IPs with Gogs fingerprint
      independent: true
      test_passed: "Shadowserver Foundation and Shodan are separate scanning operations with separate methodology and separate fingerprint logic. Both attest to thousands of exposed Gogs instances. This is independent corroboration on the exposure-layer dimension."

    cve_2025_8110_historical_exploitation:
      independent_sources:
        - nvd                            # CVE record itself
        - bleepingcomputer-historical-relay
      independent: true
      test_passed: "CVE-2025-8110 is an established Gogs CVE with documented historical exploitation in the NVD record and public exploitation reporting. BleepingComputer's relay is faithful HISTORICAL context — explicitly NOT claimed as the current flaw."

first_party_precedence:
  applied: false
  splunk_query: "search index=defenseclaw_local OR index=archimedes (gogs OR \"gogs.io\" OR \"git_repository\" OR Rapid7) earliest=-30d"
  splunk_evidence: "0 hits on aggregate Gogs-product + Rapid7-researcher sweep across defenseclaw_local + archimedes indexes. Per Hard Rule 8 doctrine — first-party silence is not contradiction; credibility grade unchanged. 67th consecutive dormant non-self sweep on defenseclaw_local."
  splunk_run_at: 2026-05-28T12:40:00-04:00

single_source_veto_applied: true
single_source_veto_layer: "Imminent-exploitation forward-projection layer (Rapid7 does not attest exploitation imminence; this is a FLASH-trigger-side heuristic on the corpus-historical pattern, not a vendor-attested operational claim)"
single_source_veto_lift_conditions: "(a) Independent A/B-grade vendor IR or threat-intel firm reports observation of exploitation against this specific Gogs argument-injection flaw, OR (b) CISA KEV addition for this CVE once assigned, OR (c) Shodan/Shadowserver telemetry confirming widespread post-disclosure scanning of Internet-exposed Gogs instances — would lift veto on the exploitation-imminence layer."
wep_ceiling: likely
wep_layered:
  vulnerability_existence_and_mechanism_class: likely_to_very_likely    # Rapid7 vendor research is A-grade; single-source-veto holds but A-grade single-source on originating disclosure carries higher WEP than B-grade single-source — defensible "likely" at minimum
  no_patch_no_cve_at_disclosure_time: very_likely                       # A1 procedural fact; verifiable absence
  install_base_2400_plus_exposed_instances: very_likely                  # Shadowserver + Shodan independent corroboration on exposure layer
  effective_pre_auth_on_default_config: likely                           # A2 layer-grade per Rapid7 vendor characterization; corpus-rule-of-thumb on open-registration self-hosted services
  imminent_exploitation_following_public_disclosure: likely              # forward-projection from corpus-historical pattern (CVE-2025-8110 prior exploitation; standard post-disclosure mass-scanning pattern)
  a_and_d_inheritance_via_self_hosted_scm_estate: roughly_even_chance   # structural-inferential claim; depends on actual DIB deployment of Gogs specifically vs. Gitea / GitLab / Forgejo / GitHub Enterprise alternatives

# Critical-override evaluation (per FLASH-POLICY.md)
critical_override_eval:
  cvss_10_0: false                          # No CVSS assigned at disclosure time; mechanism-class severity is RCE which would typically score CVSS 8-9 range but assignment is pending
  active_exploitation_confirmed: false      # Rapid7 explicitly attests NO confirmed in-wild exploitation of this specific zero-day; historical CVE-2025-8110 exploitation is HISTORICAL context not current-flaw attribution
  tracked_actor_involved: false             # No actor attribution
  ad_watchlist_entity_named: false          # No A&D-prime named
  override_qualifies: false
  override_reason_blocked: "All four conditions fail — no CVSS 10.0; no confirmed current exploitation; no actor attribution; no A&D-watchlist entity named. Quiet-hours bypass does not apply; this FLASH posts within active hours (12:40 EDT) regardless."

# Anti-noise rule 1 check (one FLASH per trigger topic per 24h)
anti_noise_24h_check:
  topic: "Gogs argument-injection zero-day RCE — Rapid7 disclosure, no patch"
  prior_24h_findings_same_topic: []
  prior_24h_rejections_same_topic: []
  prior_24h_brief_coverage: false
  morning_brief_2026_05_28_topical_overlap: false        # Morning brief covered: Carnival ShinyHunters, Unit 42 World Cup, Unit 42 Out of the Crypt, NVD critical batch — no Gogs / SCM-tooling overlap
  net_new: true

# Cluster metadata
cluster:
  topic: "Gogs self-hosted Git zero-day argument-injection RCE — Rapid7 vendor disclosure 2026-05-28 after 60+ days vendor silence; no CVE assigned; no patch; 2,400+ exposed instances; effective pre-auth on default open-registration; effective developer-tooling supply-chain exposure class"
  cluster_size: 1                          # FLASH fast-path — single-item cluster
  raw_signal_members:
    - raw-2026-05-28-flash-1200-002-bleepingcomputer-gogs-zero-day-rce-rapid7-jonah-burges-no-patch
  attribution_claims: []                   # no actor attribution

# Inclusion eligibility
inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update                 # eligible class even though no actor named

# Downstream handoff flags
analyst_review_required: true              # SAT-KAC candidate on the A&D-inheritance assumption (does DIB actually deploy Gogs at scale, or is the SCM-estate dominated by GitHub Enterprise / GitLab / Bitbucket?); SAT-KAC on the "imminent exploitation following public disclosure" forward-projection
red_team_review_required: false            # WEP ceiling = "likely" on cluster anchor; FLASH-POLICY anti-noise rule 3 requires red-team only when WEP >= "very likely" on anchor
red_team_review: null                      # red-team-analyst not invoked per WEP cap

analysis_sections:
  sat_ach: null                            # analyst populates if scheduled
  sat_kac: null                            # analyst populates — recommended topics: (1) Gogs DIB-deployment-prevalence assumption underlying the A&D-inheritance argument; (2) imminent-exploitation forward-projection assumptions (does public disclosure with 2,400+ install base reliably trigger mass scanning within 7 days, and does the open-registration-default scaling factor materially alter the exploitation-rate base rate?)

# Lifecycle
tlp: CLEAR
published_in_briefs:
  - flash-2026-05-28-1200-002-gogs-zero-day-rce-rapid7-disclosure-no-patch
retracted: false
retraction_brief_id: null

# Vuln-tracker handoffs
vuln_tracker_handoffs:
  - action: standalone_dossier_candidate_eval
    target: threats/vulnerabilities/gogs-argument-injection-rce-unassigned-CVE/
    payload: "Gogs argument-injection RCE; no CVE assigned at sweep time; no patch; affected versions 0.14.2 and 0.15.0+dev; effective pre-auth on default open-registration config; 2,400+ exposed instances per Shadowserver; mechanism class is git-rebase argument injection; vendor disclosure: Rapid7 Jonah Burges 2026-05-28 after 60+ days vendor silence following 2026-03-17 report; recommend vuln-tracker MEDIUM-priority dossier scaffolding pending CVE assignment + patch publication; vuln-tracker should monitor for CVE assignment and Gogs upstream commit"
  - action: monitor_for_cve_assignment
    target: NVD / MITRE CVE feed
    payload: "Gogs argument-injection RCE awaiting CVE assignment as of 2026-05-28 12:40 EDT; collector watch-config to be updated by librarian if CVE assigned; expected within 7-14 days of public disclosure based on historical NVD assignment cadence for vendor-coordinated-late disclosures"

# Librarian handoffs
librarian_handoffs:
  - action: collector_watch_config_addition
    target: infrastructure/watch-config.yaml
    payload: "Add `gogs-argument-injection-2026-05-28` to vuln-watch keywords; monitor for CVE assignment, Gogs upstream patch commit referencing rebase / argument-injection / branch-name handling, and any vendor IR firm observation of exploitation"
  - action: direct_retrieval_followup
    target: Rapid7 blog primary URL
    payload: "Directly retrieve the Rapid7 primary disclosure blog post in the next collection cycle to confirm BleepingComputer's relay faithfulness on the mechanism summary and disclosure timeline; the directly-retrieved evidence basis in this sweep was the BleepingComputer relay only"
---

# Gogs Zero-Day Argument-Injection RCE Disclosed by Rapid7 After 60+ Days of Vendor Silence — No Patch Available

## Summary

Rapid7 senior security researcher Jonah Burges has publicly disclosed a previously-undisclosed zero-day argument-injection vulnerability in Gogs (the self-hosted Git service) that allows registered users to obtain remote code execution on Internet-facing instances. The flaw arises in pull-request rebase handling: malicious branch names are passed to `git rebase` operations during the "Rebase before merging" flow. No CVE has been assigned. No patch is available. Rapid7 reported the flaw to Gogs maintainers on 2026-03-17; maintainers acknowledged on 2026-03-28 but released no fix; after ~60 days of vendor silence, Rapid7 disclosed publicly on 2026-05-28. Affected versions are 0.14.2 and 0.15.0+dev. Although a registered user account is technically required, Gogs ships with open registration enabled by default, so any unauthenticated attacker reaching the instance can self-register and exploit — the effective attack surface is unauthenticated on any default-config deployment. Shadowserver tracks 2,400+ Internet-exposed Gogs instances; Shodan finds 1,000+ IPs with the Gogs fingerprint; geographic skew is Asia and Europe. No confirmed in-wild exploitation of this specific zero-day at sweep time; a related Gogs flaw (CVE-2025-8110) was historically exploited in zero-day attacks per BleepingComputer's framing of historical context only.

## Sources

### Rapid7 (rapid7, A provisional — primary disclosure)

- Researcher: Jonah Burges, senior security researcher
- Direct URL: not captured in raw-signal frontmatter; librarian flagged for direct retrieval next pass
- Disclosure timeline: 2026-03-17 vendor report → 2026-03-28 vendor acknowledgement → 2026-05-28 public disclosure (60+ days vendor silence)
- Key claim: Zero-day argument-injection RCE in Gogs pull-request rebase handling; no CVE assigned at disclosure; no patch available; affected versions 0.14.2 and 0.15.0+dev; effective pre-auth on default open-registration deployments.

### BleepingComputer (bleepingcomputer, B — relay)

- URL: https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution/
- Author: Sergiu Gatlan
- Published: 2026-05-28 10:25 EDT
- Key claim: Faithful relay of the Rapid7 primary disclosure; adds install-base context (Shadowserver 2,400+; Shodan 1,000+) and historical context (CVE-2025-8110 prior Gogs exploitation, explicitly NOT claimed as the current flaw).

## Technical detail

- **Vulnerability class:** Argument injection in pull-request rebase handling — malicious branch names are passed to `git rebase` operations during the "Rebase before merging" flow, enabling arbitrary command execution. Class precedent: CVE-2017-1000117 (git submodule URL argument injection), CVE-2022-24765 (git config directory traversal), Gogs prior CVE-2025-8110.
- **CVE:** Not assigned at sweep time. Collector watch-config to be updated for CVE-assignment monitoring.
- **CVSS:** Not assigned. RCE class would typically score CVSS 8–9 range under default scoring; specific score pending CNA assignment.
- **Patch:** Not available. Gogs maintainers acknowledged the report on 2026-03-28 but have not released a fix.
- **Affected versions:** Gogs 0.14.2 and 0.15.0+dev.
- **Authentication pre-condition:** A registered Gogs user account is technically required. HOWEVER, Gogs ships with open registration enabled by default; any unauthenticated attacker who can reach the instance can self-register and exploit. Effective attack surface is unauthenticated on default-config deployments.
- **Impact (per Rapid7 via BleepingComputer):** Arbitrary RCE; full server compromise; ability to read every hosted repository; credential dump; lateral pivot into the Gogs server's network neighborhood. NO PoC content, exploit guide, or exploitation walkthrough captured here or in upstream raw-signal per Hard Rule 3.
- **Install-base exposure:**
    - Shadowserver Foundation: 2,400+ Internet-exposed Gogs instances
    - Shodan: 1,000+ IPs with Gogs fingerprint
    - Geographic skew: Asia and Europe primary
- **No confirmed in-wild exploitation** of this specific zero-day at sweep time. A related Gogs flaw — CVE-2025-8110 — was historically exploited in past zero-day attacks per BleepingComputer's framing as HISTORICAL context.
- **No actor attribution** by Rapid7 or BleepingComputer. Per Hard Rule 2 Archimedes does not originate one.

## IOCs surfaced

```yaml
iocs:
  - indicator: gogs-argument-injection-rce-unassigned-CVE
    type: cve_pending
    cvss: not_yet_assigned
    kev: false_at_sweep_time
    vendor: Gogs (open source self-hosted Git)
    product: Gogs
    affected_versions: ["0.14.2", "0.15.0+dev"]
    patch_available: false
    disclosure_path: rapid7_to_vendor_2026-03-17_then_public_2026-05-28
    exposure_signal:
      shadowserver_exposed_instances: 2400
      shodan_fingerprint_ips: 1000
      geographic_skew: asia_and_europe_primary
    effective_pre_auth_on_default_config: true
    confirmed_in_wild_exploitation_at_sweep_time: false
    historical_related_cve_with_exploitation: CVE-2025-8110

attribution_claims: []
```

## Relationship to existing findings

No prior coverage of Gogs in the Archimedes corpus. This is a net-new FLASH topic.

- Adjacent class — self-hosted developer-tooling vulnerabilities and SDLC compromise:
    - VT-006 Mini Shai-Hulud / TeamPCP npm supply-chain pattern (finding-2026-05-12-FLASH-0001 anchor; multiple follow-ons through 2026-05-28-morning brief)
    - VT-009 Nx Console marketplace-extension compromise pattern
    - finding-2026-05-20-FLASH-0001 GitHub-corp internal repos breach via VS Code marketplace extension
- The Gogs flaw differs in vector class (self-hosted SCM vulnerability vs. extension/package supply-chain compromise) but shares the developer-tooling exposure-class umbrella with these prior findings.

## Open questions for analyst

- **SAT-KAC topic (recommended):** What assumptions drive the A&D-inheritance argument? Specifically, does DIB / aerospace / defense actually deploy Gogs at scale, or is the on-premise SCM estate dominated by GitHub Enterprise Server, GitLab Self-Managed, Bitbucket Data Center, and Forgejo / Gitea alternatives? Gogs's install base is real (2,400+ Internet-exposed) but the geographic skew (Asia and Europe) and the open-source maintainer-velocity-low posture suggest the typical Gogs deployment may not be a US-DIB engineering team. The A&D-relevance claim in this finding is structural-inferential, not telemetry-attested.
- **SAT-KAC topic (secondary):** Does public disclosure with a 2,400+ install base reliably trigger mass scanning within 7 days, and does the open-registration-default scaling factor materially alter the exploitation-rate base rate? The forward-projection that "imminent exploitation following public disclosure" is the FLASH-trigger-side heuristic on corpus-historical patterns (e.g., CVE-2025-8110 prior Gogs exploitation; CVE-2024-* Citrix NetScaler, Ivanti Connect Secure post-disclosure mass-scan patterns). Re-baseline this projection against the next observation cycle.
- **Trigger 6 marginal-fit note:** The Trigger 6 evaluation requires "exploitation confirmed or imminent per A-grade source." Rapid7 (A-grade) does NOT directly attest exploitation imminence — the "imminent" reading is Archimedes's inference from (a) public disclosure event, (b) 60+ days of vendor silence, (c) effective pre-auth attack surface on default config, (d) install-base size, (e) historical CVE-2025-8110 exploitation pattern. The trigger fires on the totality, not on a single-source attestation of imminence. Operator may re-tune Trigger 6 wording in a future policy review to clarify whether "imminent per A-grade source" requires (i) explicit A-grade attestation of imminence, or (ii) A-grade attestation of preconditions that the orchestrator infers imminence from.

## Recovery handoff to briefer

- **FLASH brief eligibility: YES.** A2 clears B2 minimum; topic is distinct from 2026-05-28-morning brief coverage; no 24h same-topic prior; net-new for the corpus.
- **Recommended briefer disposition:** Stand-alone FLASH brief on the 12:00 sweep cycle, paired with #001 FortiClient EMS above as the two-item FLASH cluster for this sweep. Both findings cleanly clear FLASH inclusion thresholds. Both can ship as a single multi-item FLASH brief or as two separate FLASH briefs depending on briefer's preferred format.
- **Carry-forward suggestion:** Pair with vuln-tracker for VT-011 (or next available VT-XXX slot) dossier scaffolding on the Gogs argument-injection RCE pending CVE assignment.
- **Brief framing note for briefer:** The actionable signal for DIB defenders is NOT "patch immediately" (no patch exists) — it is (a) inventory check on Internet-exposed Gogs instances, (b) disable open registration on any deployed Gogs instances pending patch, (c) consider network-level restriction (VPN-only, IP allowlist) on Gogs admin/web surfaces, (d) monitor Gogs upstream commit for fix and CVE assignment.
