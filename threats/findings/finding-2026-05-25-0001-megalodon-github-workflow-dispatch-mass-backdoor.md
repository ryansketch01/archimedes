---
finding_id: finding-2026-05-25-0001-megalodon-github-workflow-dispatch-mass-backdoor
created_at: 2026-05-25T08:00:00-04:00
graded_by: grader
grading_run_id: morning-20260525-080000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: C2
digraph_layered:
  safedep_megalodon_5561_repos_mass_backdoor_disclosure: C2
  workflow_dispatch_anti_recursion_bypass_mechanism: C2
  sysdiag_and_optimize_build_payload_variants: C2
  base64_encoded_bash_one_liner_execution_pattern: C2
  permissions_requested_id_token_write_actions_read: C2
  tiledesk_downstream_npm_2_18_6_through_2_18_12_poisoning: C2
  legitimate_maintainer_eljohnny_unknowing_publication: C2
  c2_infrastructure_216_126_225_129_tcp_8443: C2
  throwaway_github_accounts_8char_random_username_pattern: C2
  author_identity_spoofing_build_bot_auto_ci_ci_bot_pipeline_bot: C2
  7_commit_message_template_variants: C2
  tiledesk_forensic_commit_acac5a9854650c4ae2883c4740bf87d34120c038: C2
  9_tiledesk_repos_affected_named_list: C2
  black_iron_project_8_repos_secondary_victim: C2
  6h17m_injection_window_2026_05_18_11_36_to_17_48_utc: C2
  no_actor_attribution_per_safedep_explicit_decline: A1
  no_cve_assigned_workflow_dispatch_intended_by_design_per_safedep: A1
  no_ad_prime_named_victim: A1
  splunk_first_party_zero_hits_on_megalodon_iocs: A1
  securityweek_relay_not_independent_corroboration: A1
  cluster_anchor: C2

digraph_anchor: >
  Cluster digraph C2 anchored on the load-bearing operational claim:
  SafeDep (graded C provisional per source-grades.yaml since 2026-05-12)
  discloses a mass GitHub-repo backdooring campaign dubbed "Megalodon"
  in which 5,718 malicious commits were pushed across 5,561 distinct
  repositories during a tight 6h17m window on 2026-05-18 (11:36 UTC to
  17:48 UTC). The attack abuses GitHub Actions `workflow_dispatch`
  anti-recursion behavior — by design GitHub does not retrigger a
  workflow file that itself committed a workflow file — allowing a
  committer who pushes a `.github/workflows/*.yml` file via a fake
  automated-commit identity to deploy CI-time payloads without firing
  a recursive-trigger detection. Two payload variants observed:
  SysDiag (triggers on push + pull_request_target for maximum
  execution surface) and Optimize-Build (replaces existing workflows,
  dormant until triggered via stolen tokens through GitHub API). Both
  request `id-token: write` + `actions: read` permissions and execute
  base64-decoded bash one-liners targeting CI environment variables,
  cloud credentials, SSH keys, and CI/CD tokens. Downstream impact:
  the legitimate Tiledesk npm maintainer `eljohnny` unknowingly
  published 7 poisoned versions (`@tiledesk/tiledesk-server@2.18.6`
  through `2.18.12`) between 2026-05-19 and 2026-05-21 from the
  compromised source-of-truth repository. Clean version: 2.18.5.
  C2 infrastructure: `216.126.225.129:8443`. Throwaway GitHub accounts
  use 8-character random-alphanumeric usernames (examples `rkb8el9r`,
  `bhlru9nr`, `lo6wt4t6`) with forged Git author identities including
  `build-bot`, `auto-ci`, `ci-bot`, `pipeline-bot`. Seven commit-message
  template variants observed. **Attribution: UNATTRIBUTED** per
  SafeDep's explicit decline-to-attribute; SafeDep credits discovery
  to its internal "Malysis engine." No A&D-prime victim is named.

  C2 (not B2, not A2) holds because:
    - SafeDep is graded C provisional per `source-grades.yaml`
      (since 2026-05-12, first cited via finding-2026-05-12-FLASH-0001
      Mini Shai-Hulud cluster-corroboration layer; awaiting
      ratification). SafeDep blog primary was directly retrieved this
      sweep at `safedep.io/megalodon-mass-github-repo-backdooring-ci-
      workflows` — the directly-retrieved primary is the cluster anchor.
    - SecurityWeek (Ionut Arghire, 2026-05-25 03:40 EDT in-window) is
      graded B provisional but is a PURE RELAY of the SafeDep primary
      research. Per INTEL-GRADING.md independence test, SecurityWeek
      summarizing SafeDep is the same shape as BleepingComputer
      summarizing Mandiant — not corroboration. The cluster has ONE
      effective source.
    - Credibility = 2 (Probably True) because: (a) consistent with the
      established 2026-Q2 SDLC-targeting wave of supply-chain
      mass-compromise events in corpus (Mini Shai-Hulud, TrapDoor,
      node-ipc, Laravel-Lang, Packagist 8-pkg, durabletask, art-template);
      (b) no contradicting A/B-grade source within sweep window
      (Snyk / Wiz / Aikido / StepSecurity / Socket / Unit 42 / MSTIC
      all silent in 14h window on this specific Megalodon cluster);
      (c) technical claims internally coherent — the workflow_dispatch
      anti-recursion behavior is a real (documented-by-GitHub) feature,
      the named throwaway accounts and forensic commit hash are
      enumerable against the GitHub API, the 7 named poisoned npm
      versions are verifiable against npm registry, the C2 IP is
      publicly observable (no privileged telemetry required to
      validate).
    - Cannot rise to C1 / Confirmed without independent A/B-grade
      research on this specific Megalodon cluster.
    - Single-source veto applies (see below) — even at C2, all
      forward-looking and scope-projection claim layers cap at
      "likely" WEP.

  Hard Rule 2 binding: SafeDep declines actor attribution and does
  not link Megalodon to any tracked roster actor. SecurityWeek
  uses generic "the attacker" / "attackers" language. Author-identity
  spoofing patterns (`build-bot` / `auto-ci` / `ci-bot` / `pipeline-bot`)
  thematically overlap with TeamPCP's `claude@users.noreply.github.com`
  spoofing from the 2026-05-12 Mini Shai-Hulud cluster, but the
  technique is portable and shared across multiple unattributed
  cybercriminal operators in the current SDLC-targeting wave.
  Archimedes does NOT collapse Megalodon, TrapDoor, TeamPCP, and
  node-ipc into a single actor without A/B-grade attribution.

  Hard Rule 8 first-party precedence: Grader-inheriting collector-
  executed targeted 17-IOC Splunk sweep across `defenseclaw_local`
  over -24h@h window (covering Megalodon C2 IP 216.126.225.129,
  RemotePE C2 aes-secure[.]net, DPAPILoader Iassvc.dll, TrapDoor
  exfil ddjidd564.github.io, @tiledesk/tiledesk-server,
  flipboxstudio, and 11 tracked actor / tracked CVE tokens) returned
  ZERO events. 56th consecutive dormant non-self sweep posture on
  `defenseclaw_local`. Per Hard Rule 8: first-party silence is
  neither confirming nor disconfirming.

source_reliability:
  primary:
    grade: C
    source_name: "SafeDep (SafeDep Team byline; npm/supply-chain security vendor; 'Malysis engine' discovery attribution)"
    source_yaml_id: safedep
    grade_rationale: >
      Pre-assigned C provisional per source-grades.yaml (since
      2026-05-12, awaiting ratification — first cited via
      finding-2026-05-12-FLASH-0001 Mini Shai-Hulud cluster-
      corroboration layer). SafeDep primary blog post directly
      retrieved this sweep at
      https://safedep.io/megalodon-mass-github-repo-backdooring-ci-
      workflows. Note: SafeDep published primary research on
      2026-05-21; SecurityWeek relay on 2026-05-25 03:40 EDT
      surfaced it into Archimedes's collection scope (4-day post-
      primary detection gap acknowledged — see collection-gap
      flag in raw-2026-05-25-am-001 disposition).
    provisional: true
    direct_retrieval_status: retrieved_this_sweep_via_securityweek_pickup
  originating_research:
    - grade: C
      source_name: "SafeDep Team (no individual byline; 'Malysis engine' attribution)"
      source_yaml_id: safedep
      grade_rationale: >
        SafeDep is both the directly-retrieved primary and the
        originating research firm. No relay layer between originating
        research and grader-retrieved primary on this cluster.
      provisional: true
  enrichment:
    - grade: B
      source_name: "SecurityWeek (Ionut Arghire byline)"
      source_yaml_id: securityweek
      role: >
        Pure relay of SafeDep primary research. Published 2026-05-25
        03:40 EDT (in-window). SecurityWeek does not contribute
        independent telemetry, independent IOC discovery, or
        independent analysis — the article summarizes SafeDep's
        findings and cites SafeDep as the source. Per INTEL-GRADING.md
        independence test, SecurityWeek summarizing SafeDep is
        NOT independent corroboration of SafeDep (analogous to
        BleepingComputer summarizing Mandiant). Cluster effectively
        stands on the SafeDep evidence basis alone.
      url: https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/

credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent           # Mass GitHub-repo backdooring via abuse of CI/CD feature behavior is consistent with the 2026 SDLC-targeting wave (Mini Shai-Hulud npm-worming via maintainer credential theft; node-ipc via npm publish; Laravel-Lang via Packagist tag-resolution abuse; Packagist 8-pkg via postinstall + GitHub-hosted binary; TrapDoor via three-ecosystem simultaneous publication). The workflow_dispatch anti-recursion behavior is a documented GitHub Actions design pattern; the abuse layer (push fake automated commits to add workflow files that deploy CI-time payloads without triggering recursive-trigger detection) is mechanically consistent with established CI/CD supply-chain abuse tradecraft (TanStack/OpenAI GitHub Actions finding-2026-05-14-0008; nx-console formal confirmation finding-2026-05-21-0003).
    - probably_true_no_contradicting_ab      # No contradicting A/B-grade source within sweep window. Snyk, Wiz Research, Aikido, StepSecurity, Socket, Unit 42 npm threat landscape, Ox Security, Upwind, Checkmarx all silent in 14h window on this specific Megalodon cluster. GitHub-side official statement not yet observed (GitHub may consider workflow_dispatch anti-recursion behavior intended-by-design per SafeDep's framing — and therefore not a vulnerability they would patch or advise on).
    - probably_true_claims_coherent          # Technical claims internally coherent: the workflow_dispatch anti-recursion behavior is a real GitHub Actions feature (documented); the named throwaway accounts (rkb8el9r, bhlru9nr, lo6wt4t6) and forensic commit hash (acac5a9854650c4ae2883c4740bf87d34120c038) are enumerable against the GitHub API; the 7 poisoned npm versions (@tiledesk/tiledesk-server@2.18.6 through 2.18.12) are verifiable against the npm registry; the C2 IP 216.126.225.129:8443 is publicly observable (no privileged telemetry required to validate); the SysDiag and Optimize-Build payload variant names and their permission requests (id-token:write + actions:read) and execution patterns (base64-decoded bash one-liners) are consistent with established CI/CD abuse mechanics.
  fails_grade_1:
    - confirmed_independent_corroboration_no_second_a_b_primary  # Cluster stands on SafeDep-directly-retrieved primary; SecurityWeek is pure relay; no second A/B-grade vendor has independently analyzed this Megalodon cluster as of this sweep
  rationale: >
    Grade 2 (Probably True). Cluster anchor is SafeDep's directly-
    retrieved blog primary, augmented by a SecurityWeek relay (not
    independent). The technical claims are internally coherent and
    independently verifiable in principle (npm registry, GitHub API,
    public IP observability), even though no second A/B-grade primary
    research vendor has corroborated within the sweep window. Cannot
    rise to Confirmed (1) without independent A/B-grade primary
    research on this specific Megalodon cluster. Grade 2 holds on all
    three checklist conditions.

corroboration:
  independent_sources:
    - safedep    # SOLE originating-research independent source
  independent: false
  test_passed: >
    Independence test FAILS at the second-source layer. SafeDep is the
    sole originating-research primary. SecurityWeek (Ionut Arghire)
    summarizes the SafeDep disclosure and cites SafeDep as the source.
    Per INTEL-GRADING.md ("Different publishing organization, neither
    cites the other, different evidence basis"), SecurityWeek
    summarizing SafeDep is NOT independent corroboration (same shape
    as BleepingComputer summarizing Mandiant — explicit anti-pattern
    in the doctrine). The cluster effectively stands on one evidence
    basis (SafeDep originating research, blog primary directly
    retrieved). No second A/B-grade vendor research (Snyk, Wiz,
    Aikido, StepSecurity, Socket, Unit 42, Ox Security, Upwind,
    Checkmarx, MSTIC, ESET, Sophos, Bitdefender) has surfaced
    corroborating analysis on this specific Megalodon cluster within
    the 14h sweep window.
  corroboration_uplift_anticipated:
    - "A second A/B-grade vendor publishing independent analysis (Snyk, Wiz, Aikido, StepSecurity, Socket, Unit 42, Ox Security, Upwind, Checkmarx) within 24-72h regrades the cluster toward C1, or — if the second-vendor source is B-grade or better — toward B2."
    - "GitHub-side official statement on the workflow_dispatch anti-recursion behavior (whether intended-by-design or patched as a vulnerability) adds GitHub-self-disclosure evidence basis."
    - "npm registry-side official statement on the @tiledesk/tiledesk-server poisoned-versions remediation status adds ecosystem-self-disclosure evidence basis."
    - "VirusTotal enrichment on 216.126.225.129 (vendor detection scores, AS/netblock context, passive DNS history) adds independent enrichment-class corroboration."
    - "Tiledesk maintainer eljohnny's own statement on the breach scope and remediation timeline adds victim-self-disclosure evidence basis."

first_party_precedence:
  applied: true
  splunk_query: >
    search index=defenseclaw_local earliest=-24h@h latest=now
    (216.126.225.129 OR megalodon OR tiledesk OR
     "@tiledesk/tiledesk-server" OR "build-bot" OR "auto-ci" OR
     "ci-bot" OR "pipeline-bot" OR rkb8el9r OR bhlru9nr OR lo6wt4t6)
    | head 50
  splunk_result: zero_hits_genuine
  splunk_evidence: >
    Collector-executed first-party Splunk hand-built sweep this sweep
    (component of the consolidated 17-IOC keyword query documented in
    raw-2026-05-25-am-000 sentinel) returned ZERO events on the
    Megalodon IOC layer (C2 IP 216.126.225.129; npm package
    @tiledesk/tiledesk-server; throwaway-account username patterns
    rkb8el9r / bhlru9nr / lo6wt4t6; forged-identity patterns build-bot
    / auto-ci / ci-bot / pipeline-bot). 56th consecutive dormant
    non-self sweep posture on `defenseclaw_local`. Per Hard Rule 8:
    first-party silence is neither confirming nor disconfirming.
    `defenseclaw_local` is a local Splunk instance not connected to a
    production network — IOC-class payload observation is structurally
    bounded by the instance's narrow ingest scope; absence of hits
    does not disconfirm the external SafeDep disclosure.

single_source_veto_applied: true
single_source_veto_scope: >
  Single-source veto applies on ALL claim layers — the cluster stands
  on SafeDep's evidence basis alone. WEP ceiling caps at "likely" on:
    - 5,561-distinct-repositories scope count (SafeDep-originating;
      independently auditable against GitHub API but not yet audited
      by a second vendor).
    - 5,718-malicious-commits scope count (same as above).
    - 6h17m injection window (same as above).
    - Two-payload-variants framing (SysDiag and Optimize-Build —
      SafeDep-internal classification labels).
    - Downstream-Tiledesk-npm-publication attribution (the causal
      link between the GitHub source-of-truth poisoning and the
      `eljohnny`-published npm versions is SafeDep's analytic
      reconstruction; verifiable in principle but no second-vendor
      confirmation in window).
    - Author-identity-spoofing technique-class attribution to
      "this specific operator" (vs. portable-technique-class shared
      across multiple unattributed operators).
    - Forward-looking claims about campaign-continuity, additional-
      victim-disclosure, or attribution-by-second-vendor.
    - A&D-prime supply-chain exposure pathway (no A&D victim named;
      structural-indirect via developer-ecosystem ubiquity only).
    - Actor-attribution to any tracked roster actor (SafeDep
      declines; Hard Rule 2 binding).

wep_split:
  five_thousand_five_hundred_sixty_one_repositories_backdoored: likely  # SafeDep-originating scope claim; independently auditable but not yet audited
  six_hour_seventeen_minute_injection_window_2026_05_18: likely         # SafeDep-originating timeline anchor
  workflow_dispatch_anti_recursion_bypass_mechanism: likely             # SafeDep-originating technical framing; the GitHub Actions feature itself is documented but the abuse classification is SafeDep-internal
  sysdiag_and_optimize_build_payload_variants: likely                   # SafeDep-internal classification labels for the two payload-variant patterns
  base64_decoded_bash_one_liner_execution: likely                       # Standard payload-execution mechanic; SafeDep-reported
  c2_216_126_225_129_tcp_8443: likely                                   # SafeDep-originating IOC; publicly observable
  tiledesk_downstream_npm_2_18_6_through_2_18_12_poisoning: likely      # SafeDep-originating causal link claim; npm versions verifiable
  legitimate_maintainer_eljohnny_unknowing: likely                      # SafeDep-originating attribution-of-state; eljohnny has not publicly confirmed
  throwaway_github_accounts_8char_random_pattern: likely                # SafeDep-originating IOC pattern; three named examples enumerable
  author_identity_spoofing_build_bot_auto_ci_ci_bot_pipeline_bot: likely # SafeDep-originating IOC pattern; forged-author-name strings enumerable against any GitHub-audit-log surface
  seven_commit_message_templates: likely                                # SafeDep-originating IOC pattern; template strings enumerable
  tiledesk_forensic_commit_hash: likely                                 # SafeDep-originating IOC; hash verifiable against GitHub
  nine_tiledesk_repos_affected_named_list: likely                       # SafeDep-originating victim-scope claim; repository names enumerable
  black_iron_project_8_repos_secondary_victim: likely                   # SafeDep-originating victim-scope claim; secondary org named
  wise_community_secondary_victim: likely                               # SafeDep-originating victim-scope claim; count not specified by SafeDep
  five_thousand_smaller_repositories_long_tail: likely                  # SafeDep-originating victim-scope claim; long-tail count
  actor_attribution: do_not_predict                                     # SafeDep explicitly declines; Hard Rule 2 binding
  campaign_continuity_or_actor_pivot: likely                            # Forward prediction; single-source veto holds at "likely"
  cross_corpus_collapse_with_teampcp_or_trapdoor_or_node_ipc: do_not_predict  # Author-identity-spoofing is a portable technique-class shared across multiple unattributed operators; collapsing without A/B-grade attribution would violate Hard Rule 2
  ad_prime_supply_chain_exposure: roughly_even_chance                   # STRUCTURAL-INDIRECT only; Tiledesk is live-chat/chatbot infrastructure with no A&D-specific deployment context surfaced; A&D-prime SDLCs operating GitHub Actions are PROCEDURALLY exposed to the same attack class if a poisoned committer-identity can modify workflow files
  github_workflow_dispatch_class_attack_recurrence: likely              # Forward prediction on the class of attack (vs. this specific campaign continuing); the abuse pattern is now publicly disclosed and other operators can adopt it

wep_ceiling: likely    # single-source veto applies on all claim layers; cluster stands on SafeDep evidence basis alone

# Cluster metadata
cluster:
  topic: >
    Megalodon mass GitHub-repo backdooring campaign (5,561 repositories
    backdoored 2026-05-18 via GitHub Actions workflow_dispatch
    anti-recursion bypass; SysDiag + Optimize-Build payload variants;
    downstream npm @tiledesk/tiledesk-server@2.18.6 through 2.18.12
    poisoning via legitimate maintainer eljohnny; C2 216.126.225.129:8443;
    UNATTRIBUTED per SafeDep explicit decline)
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-25-am-001-securityweek-megalodon-5561-github-repos-workflow-dispatch-tiledesk
  attribution_claims: []           # SafeDep declines attribution; SecurityWeek uses generic "attackers" language; Hard Rule 2 preserved
  cross_corpus_pattern_observed:
    - finding-2026-05-24-0001            # TrapDoor multi-ecosystem supply-chain (UNATTRIBUTED per Socket; same SDLC-targeting wave; mechanically distinct — no GitHub Actions abuse layer)
    - finding-2026-05-23-0005            # Packagist 8-pkg PHP/Composer (UNATTRIBUTED per Socket)
    - finding-2026-05-23-0001            # Laravel-Lang Composer (UNATTRIBUTED)
    - finding-2026-05-21-0003            # nx-console formal confirmation (GitHub Actions abuse-class adjacent)
    - finding-2026-05-20-0001            # SecurityWeek Mini Shai-Hulud @antv continuation (TeamPCP-attributed per Wiz + StepSecurity)
    - finding-2026-05-20-FLASH-0001      # GitHub-corp internal repos via VS Code extension (TeamPCP-claimed)
    - finding-2026-05-14-0009            # node-ipc npm supply-chain (UNATTRIBUTED four-firm consensus)
    - finding-2026-05-14-0008            # TanStack / OpenAI GitHub Actions abuse (mechanically adjacent: CI/CD-token-theft via workflow abuse)
    - finding-2026-05-12-FLASH-0001      # Mini Shai-Hulud npm+PyPI worm (TeamPCP-attributed per Wiz + StepSecurity)
  cross_corpus_pattern_significance: >
    EIGHTH distinct 2026 supply-chain mass-compromise campaign in the
    Archimedes corpus within the 14-day window 2026-05-12 to 2026-05-25.
    Megalodon introduces the FIRST CORPUS INSTANCE of mass GitHub-repo
    backdooring via abuse of GitHub Actions workflow_dispatch
    anti-recursion behavior. Mechanically distinct from prior corpus
    supply-chain events:
      - Mini Shai-Hulud (TeamPCP-attributed): npm + PyPI maintainer-
        credential-theft worming.
      - node-ipc: npm publish-from-compromised-maintainer-account.
      - Laravel-Lang: Composer/Packagist GitHub-to-Packagist
        tag-resolution abuse + autoload.files + helpers.php
        per-request execution.
      - Packagist 8-pkg: Composer/Packagist postinstall in package.json
        + GitHub-hosted Linux binary.
      - TrapDoor: npm + PyPI + Crates.io simultaneous publication;
        one attacker identity across all three; GitHub-Pages dead-drop;
        .cursorrules + CLAUDE.md AI-agent-config persistence.
      - TanStack/OpenAI: GitHub Actions token theft via workflow
        injection (mechanically closest prior corpus precedent for
        Megalodon).
      - nx-console: 18-minute compromise window publication.
      - Megalodon: mass GitHub-repo backdooring at scale (5,561
        distinct repos in 6h17m) via workflow_dispatch anti-recursion
        bypass; novel attack-class within the corpus.

    Cross-corpus author-identity-spoofing pattern observation
    (technique-class catalog entry, NOT actor-attribution):
      - Megalodon: build-bot / auto-ci / ci-bot / pipeline-bot
      - Mini Shai-Hulud (TeamPCP): claude@users.noreply.github.com
      - node-ipc: atiertant (no-history account)
      - TrapDoor: (not specified in Socket/THN coverage)
    Author-identity spoofing + throwaway-account creation has appeared
    in 4+ unattributed supply-chain mass-compromise events in the past
    14 days. The technique is portable post-access and does NOT
    distinguish actor identity. Hard Rule 2 binding: do NOT collapse
    Megalodon / TrapDoor / TeamPCP / node-ipc into a single actor
    without A/B-grade attribution.

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_monitoring         # C2 meets monitoring threshold per INTEL-GRADING.md inclusion table (C3 minimum for monitoring)
    - weekly_synthesis               # C2 meets weekly synthesis threshold (C3 minimum)
    - supply_chain_watch_section     # candidate for the Supply Chain Watch standing section (pair with finding-2026-05-24-0001 TrapDoor)
  not_eligible_for:
    - flash                          # C2 below FLASH B2 minimum threshold; also collector evaluated FLASH triggers — Trigger 5 NEAR-MISS but failed on no-A&D-prime-named-victim condition
    - daily_brief_action             # C2 below B2 minimum for action-item inclusion; monitoring-tier-only
    - actor_profile_update           # UNATTRIBUTED; no actor dossier to update

# Downstream handoff flags
analyst_review_required: true       # WEP "likely" on all forward claim layers AND novel attack-class (workflow_dispatch anti-recursion bypass is first corpus instance) AND cross-corpus pattern (eighth 2026 supply-chain mass-compromise campaign in 14 days) AND single-source veto applies — warrant analyst SAT-KAC review of load-bearing assumptions (SafeDep-faithful-relay; workflow_dispatch-as-genuine-abuse-class vs. operator-defined-classification; downstream-tiledesk-causal-link; cross-corpus author-identity-spoofing as technique-class vs. actor-collapse-signal). Analyst should also assess whether to invoke SAT-ACH on the cluster of unattributed supply-chain mass-compromise events (now eight in 14 days) to stress-test the multi-actor-convergence H2 framing inherited from finding-2026-05-23-0001 ACH and finding-2026-05-23-0005 KAC.
analyst_review_complete: true       # SAT-KAC + SAT-ACH applied 2026-05-25T08:54:00-04:00
analyst_review_run_id: analyst-20260525-084200
red_team_review_required: false     # WEP ceiling is "likely" (single-source veto applied), below "very likely" threshold for red-team review per grader doctrine
wep_ceiling_adjusted: false         # grader's "likely" stands; SAT-KAC + SAT-ACH did NOT recommend WEP adjustment — A3 (test classification) does not block monitoring-tier inclusion, and ACH H2 retains rank-1 with no leader-flip
assessment_blocked_pending_test: false  # A3 test (eljohnny + npm tarball diff + Socket corroboration) recommended but does NOT block monitoring-tier framing; would block action-item or FLASH (which were already declined by grader on independent grounds)
red_team_review: null
analysis_sections:
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "SafeDep (graded C provisional) has accurately characterized a
        coherent campaign — dubbed Megalodon — in which 5,718 malicious
        commits were pushed across 5,561 distinct GitHub repositories
        on 2026-05-18 via GitHub Actions workflow_dispatch anti-recursion
        bypass, with downstream poisoning of @tiledesk/tiledesk-server
        npm versions 2.18.6 through 2.18.12; cross-corpus author-identity
        spoofing patterns are a portable technique-class, NOT signal of
        actor identity; the finding is fit for monitoring-tier inclusion
        in the morning brief at WEP ceiling 'likely' under single-source
        veto."
      analyzed_at: 2026-05-25T08:42:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Grader flagged analyst_review_required:true on three stacked
        reasons (novel attack-class — first corpus instance of mass
        GitHub-repo backdooring via workflow_dispatch anti-recursion
        bypass; eighth supply-chain mass-compromise in 14 days; single-
        source veto active). Pre-publication review for the morning brief
        2026-05-25.

      assumptions:
        - id: A1
          statement: >
            SafeDep is a faithful relay of what its Malysis engine
            observed — the 5,561-repository scope count, the 6h17m
            injection window, and the two-payload-variants classification
            are not exaggerations or methodology artifacts.
          category: source_reliability
          stated: false
          why_must_be_true: >
            The entire cluster's quantitative shape (scope, timeline,
            variant taxonomy) rests on SafeDep's internal detection
            pipeline. If SafeDep's tooling double-counts forks, treats
            normal-but-unusual commits as malicious, or inflates the
            variant count by labeling minor template differences as
            distinct campaigns, downstream framing distorts.
          when_could_be_false: >
            (a) SafeDep's Malysis engine has not been independently
            audited and the 5,561 figure could include forks of the same
            template-commit, archived repos, or test repos that materially
            inflate the headline number. (b) SafeDep is a young/emerging
            vendor (C-provisional in source-grades.yaml since 2026-05-12,
            awaiting ratification) and has not previously published a
            disclosure of this magnitude in the Archimedes corpus —
            track record on scope-claim accuracy is thin. (c) Vendor
            naming-and-shaming a campaign ("Megalodon") creates a mild
            marketing incentive to round up rather than down.
          evidence_for:
            - safedep_megalodon_blog_2026_05_21_via_finding_2026_05_25_0001  # SafeDep primary directly retrieved
            - securityweek_ionut_arghire_in_window_relay_2026_05_25_03_40_edt  # repeats SafeDep figures uncritically
          evidence_against:
            - no_second_independent_vendor_audit_in_14h_sweep_window  # Snyk/Wiz/Aikido/StepSecurity/Socket/Unit42/Ox/Upwind/Checkmarx all silent
            - safedep_safedep_io_megalodon_post_is_self_published_blog_not_peer_review  # vendor blog, not joint research
          confidence: medium
          centrality: critical
          classification: qualify

        - id: A2
          statement: >
            The workflow_dispatch trigger usage on these 5,561 repos
            constitutes genuine abuse, not legitimate-but-unusual CI/CD
            patterns the researcher misread. The 7 commit-message
            templates, throwaway-account pattern, base64+bash payload
            structure, and id-token:write permission request collectively
            distinguish malicious from legitimate activity.
          category: technology_interpretation
          stated: false
          why_must_be_true: >
            If the activity is genuine but unusual CI/CD bot behavior
            (large-scale template propagation by a legitimate automation
            vendor, mass-CI-migration tool, dependabot-class auto-PR
            engine, GitHub Marketplace app rollout), the headline collapses
            from "supply-chain attack" to "noisy benign automation."
          when_could_be_false: >
            (a) Concrete: a vendor sells a CI-migration tool that creates
            8-char-pseudonym GitHub accounts and pushes templated
            workflow files. (b) SafeDep classified abuse by surface
            pattern (8-char account + forged identity + base64 payload)
            but the base64 payloads on the 5,500 long-tail repos may
            differ from the named Tiledesk + Black-Iron + WISE samples
            and have not been individually triaged.
          evidence_for:
            - base64_bash_payload_targeting_aws_gcp_azure_credentials_per_safedep_observation  # exfiltration target list is malicious-pattern-consistent
            - c2_216_126_225_129_8443_dedicated_high_port_per_safedep_observation  # 8443 tcp is malicious-pattern-consistent
            - id_token_write_actions_read_permission_request_per_safedep_observation  # privileged-permission request is malicious-pattern-consistent
            - throwaway_8char_pseudonym_accounts_no_prior_commit_history_per_safedep_observation  # account-pattern matches malicious tradecraft, not legitimate vendor automation
            - 7_commit_message_template_variants_low_entropy_per_safedep_observation  # template uniformity matches campaign tradecraft, not organic automation
          evidence_against:
            - safedep_did_not_publish_per_repo_payload_triage_for_long_tail_5500_smaller_repos  # the 5,500 long-tail count is the WEAKEST layer; only Tiledesk + Black-Iron + WISE have named verifiable trail
          confidence: medium
          centrality: material
          classification: qualify

        - id: A3
          statement: >
            The claimed Tiledesk downstream-causal-link is real: the
            GitHub source-of-truth poisoning during the 2026-05-18
            window directly caused the @tiledesk/tiledesk-server@2.18.6-
            2.18.12 poisoned-npm publications by maintainer eljohnny
            between 2026-05-19 and 2026-05-21. This is not a coincidental
            adjacent Tiledesk compromise via a separate vector.
          category: causal_chain
          stated: true
          why_must_be_true: >
            The downstream-impact framing is the load-bearing operational
            justification for treating Megalodon as more than a noisy
            GitHub commit-spam event. Without the causal link, the
            5,561-repo scope is dramatically less interesting (mostly
            small personal blogs and OSS projects) and the named-victim
            blast radius shrinks.
          when_could_be_false: >
            (a) Tiledesk was compromised via maintainer-credential theft
            (Mini Shai-Hulud-class) independently in the same window and
            SafeDep retro-fitted the causal chain. (b) eljohnny's npm
            publishing pipeline pulled from a non-poisoned branch or
            commit; the poisoned commit landed but never reached the
            published artifacts. (c) The poisoned versions contain the
            poisoned workflow files but the runtime malware payload was
            never published (workflow files don't ship inside npm
            tarballs by default).
          evidence_for:
            - tiledesk_forensic_commit_acac5a9854650c4ae2883c4740bf87d34120c038_named_by_safedep  # specific verifiable commit anchor
            - 7_named_poisoned_versions_2_18_6_through_2_18_12_verifiable_against_npm_registry  # poisoned versions are enumerable
            - injection_window_2026_05_18_precedes_publication_window_2026_05_19_to_05_21  # temporal ordering consistent
            - eljohnny_named_as_unknowing_publisher_per_safedep_observation  # SafeDep names the maintainer-state
          evidence_against:
            - eljohnny_has_not_publicly_confirmed_compromise_scope_or_remediation_timeline  # victim-self-disclosure absent
            - safedep_did_not_publish_npm_tarball_diff_showing_workflow_file_in_published_artifact  # the workflow-to-tarball causal step is asserted not demonstrated
            - no_independent_npm_registry_or_socket_corroboration_of_the_causal_chain_at_finding_write_time
          confidence: medium
          centrality: critical
          classification: test

        - id: A4
          statement: >
            The cross-corpus author-identity-spoofing pattern (build-bot
            / auto-ci / ci-bot / pipeline-bot in Megalodon; claude@
            users.noreply.github.com in TeamPCP/Mini Shai-Hulud and Mini
            Shai-Hulud VT-006 continuation; atiertant in node-ipc;
            unspecified in TrapDoor) is a TECHNIQUE-CLASS catalog entry
            — multiple unattributed operators are independently adopting
            CI-bot-impersonation tradecraft because it is portable and
            effective. It is NOT actor-collapse signal pointing to a
            single underlying actor.
          category: ttp_patterns
          stated: true
          why_must_be_true: >
            Hard Rule 2 binding. If author-identity spoofing IS
            actor-collapse signal, Archimedes would be silently
            originating a TeamPCP-or-related attribution across multiple
            campaigns that vendors have explicitly NOT attributed
            (Socket on TrapDoor explicitly rules out TeamPCP / Shai-Hulud
            / Mini Shai-Hulud; Socket+Aikido on Laravel-Lang decline;
            four-firm consensus on node-ipc declines; SafeDep on
            Megalodon declines). Treating the pattern as actor-class
            signal would violate Rule 2 by collapsing four UNATTRIBUTED
            campaigns into one implicit cluster.
          when_could_be_false: >
            (a) A subsequent A/B-grade vendor (Wiz, Mandiant, MSTIC)
            publishes a tradecraft-cluster analysis that attributes 2+
            of these campaigns to a common operator on the basis of
            additional evidence (shared infrastructure, shared payload
            internals, shared monetization channel). (b) An attacker
            self-claim on Breached / RAMP / similar surfaces 2+ of the
            campaigns to one persona. (c) Reverse-engineering of the
            CI-bot-impersonation toolkit shows shared kit (same
            generator, same template engine) across campaigns.
          evidence_for:
            - finding_2026_05_23_0001_ach_h2_multi_actor_convergence_rank_1_zero_inconsistencies  # corpus-internal ACH already weighed this
            - finding_2026_05_23_0005_kac_inherited_h2_framing_continuing_no_attribution_at_scale_e15  # cross-corpus reinforcement
            - finding_2026_05_24_0001_socket_explicit_decline_to_attribute_trapdoor_specifically_ruling_out_teampcp_shai_hulud_mini_shai_hulud  # Socket actively denies the actor-collapse reading
            - safedep_explicit_decline_to_attribute_megalodon_per_finding_2026_05_25_0001_no_actor_attribution_per_safedep  # SafeDep actively declines
            - distinct_c2_infrastructure_across_campaigns_216_126_225_129_megalodon_vs_flipboxstudio_info_laravel_lang_vs_6_distinct_teampcp_domains_vs_ddjidd564_github_io_trapdoor  # E6 from morning-23 ACH — strongly diagnostic
            - distinct_ecosystem_vectors_per_campaign_workflow_dispatch_vs_npm_publish_vs_composer_tag_resolution_vs_three_ecosystem_simultaneous  # E7 from morning-23 ACH — diagnostic
          evidence_against:
            - cross_corpus_temporal_density_8_in_14_days_remains_high_e1_morning_23_ach  # temporal cluster could in principle mean one operator
          confidence: medium
          centrality: critical
          classification: qualify

        - id: A5
          statement: >
            GitHub's workflow_dispatch anti-recursion behavior is
            intended-by-design (per SafeDep's characterization); GitHub
            will treat this as documentation/hardening guidance rather
            than a CVE-class vulnerability, and no NVD/CVE coordination
            will activate.
          category: technology
          stated: true
          why_must_be_true: >
            Drives the defender-response framing — if intended-by-design,
            mitigation is procedural (branch-protection rules + required-
            reviews on .github/workflows/*.yml). If GitHub reclassifies
            it as a vulnerability, a CVE is plausible and vuln-tracker
            activates.
          when_could_be_false: >
            (a) GitHub Security publishes an advisory and assigns a CVE.
            (b) GitHub silently changes the anti-recursion behavior in
            a future release without acknowledging it as a security fix
            (the soft-deprecation path; quiet-but-effective).
          evidence_for:
            - safedep_explicit_framing_anti_recursion_is_intended_by_design  # SafeDep's read
            - no_github_security_advisory_on_workflow_dispatch_anti_recursion_in_14h_sweep_window  # silence as of finding-write time
          evidence_against:
            - no_explicit_github_statement_observed_in_14h_window_either_way  # silence is bidirectional
          confidence: low
          centrality: peripheral
          classification: qualify

        - id: A6
          statement: >
            Splunk first-party silence on the Megalodon IOC layer
            (216.126.225.129; @tiledesk/tiledesk-server; throwaway
            usernames; forged identities) reflects genuine non-exposure
            of the Archimedes/defenseclaw_local environment, not
            visibility-gap. Per Hard Rule 8, first-party silence is
            neither confirming nor disconfirming.
          category: visibility
          stated: true
          why_must_be_true: >
            Drives the cluster's framing of A&D-prime exposure as
            structural-indirect-only. If Splunk silence is actually a
            visibility gap rather than genuine absence, an A&D-prime
            could be exposed through Tiledesk-deployed help-desk /
            customer-support / chatbot stacks without Archimedes seeing
            it.
          when_could_be_false: >
            (a) defenseclaw_local is a local Splunk instance with narrow
            ingest scope and does not represent any production A&D-prime
            network; the absence of hits is structurally bounded by the
            instance's ingest. (b) 56th consecutive dormant non-self
            sweep posture means the instance is reliably reporting
            nothing because it sees almost nothing — not because there
            is nothing to see.
          evidence_for:
            - splunk_query_per_finding_first_party_precedence_section_zero_hits_on_17_ioc_sweep
            - 56th_consecutive_dormant_non_self_sweep_per_finding_hard_rule_8_compliance
          evidence_against:
            - defenseclaw_local_is_narrow_ingest_local_instance_per_operational_notes_session_3_security_boundary_is_os_level
          confidence: high
          centrality: peripheral
          classification: sound

        - id: A7
          statement: >
            SecurityWeek (Ionut Arghire, 2026-05-25 03:40 EDT) is a
            faithful relay of SafeDep's research and adds no independent
            evidence basis — therefore the cluster correctly stands on
            SafeDep's evidence basis alone and the single-source veto
            applies.
          category: source_reliability
          stated: true
          why_must_be_true: >
            If SecurityWeek were independently corroborating (separate
            telemetry, separate IOC discovery), the cluster could escape
            single-source veto and rise toward C1 / B2. The grader's
            independence-test conclusion is load-bearing for the WEP
            ceiling.
          when_could_be_false: >
            SecurityWeek silently incorporated separate vendor briefings
            (e.g., quiet B-grade vendor contributions not credited in
            the article). Low likelihood given Arghire's standard
            single-source relay pattern.
          evidence_for:
            - securityweek_article_text_summarizes_safedep_and_cites_safedep_per_finding_corroboration_section
            - intel_grading_md_independence_test_explicit_anti_pattern_bleepingcomputer_summarizing_mandiant
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound

        - id: A8
          statement: >
            The novel-attack-class framing ("first corpus instance of
            mass GitHub-repo backdooring via workflow_dispatch anti-
            recursion bypass") is genuinely novel WITHIN the Archimedes
            corpus, not an observability artifact of the corpus's
            14-day-window and its source-mix.
          category: visibility
          stated: true
          why_must_be_true: >
            Drives the cross-corpus pattern observation that this is the
            eighth supply-chain mass-compromise in 14 days. If the
            workflow_dispatch anti-recursion bypass is actually NOT
            novel — prior coverage exists in vendors not in the
            corpus's source-mix, or in older non-cluster events — the
            "novel" framing overstates.
          when_could_be_false: >
            (a) StepSecurity / GitGuardian / Endor Labs / Apiiro / other
            non-currently-tracked supply-chain security vendors have
            published on this technique pre-2026 and the corpus simply
            doesn't ingest them. (b) GitHub's own security blog has
            historical coverage that hasn't been catalogued.
          evidence_for:
            - cross_corpus_pattern_observed_list_per_finding_cluster_section_9_named_distinct_campaigns_no_workflow_dispatch_anti_recursion_layer_in_any
            - finding_2026_05_14_0008_tanstack_openai_github_actions_is_closest_prior_corpus_precedent_and_is_token_theft_via_workflow_injection_NOT_anti_recursion_bypass
          evidence_against:
            - source_mix_finite_other_vendors_may_have_covered_pre_2026  # known-unknown
          confidence: medium
          centrality: peripheral
          classification: qualify

      classifications_summary:
        sound: 2     # A6, A7
        qualify: 5   # A1, A2, A4, A5, A8
        test: 1      # A3
        reject: 0
        total: 8

      remediation:
        status: proceed_with_caveats
        blocking_assumption: null    # A3 classified test but DOES NOT block monitoring-tier inclusion
        rationale: >
          A3 (downstream-Tiledesk-causal-link) is classified Test because
          a critical-centrality assumption has medium confidence and a
          specific test would resolve it (eljohnny public statement +
          npm tarball diff + Socket / Snyk corroboration of the causal
          chain). HOWEVER, the finding is classified for MONITORING-TIER
          inclusion only — not action-item, not FLASH. Monitoring-tier
          framing already implies caveat-heavy presentation. The Test
          status on A3 is therefore satisfied by explicit caveat in the
          brief language rather than by blocking publication.

          If the finding were proposed for action-item or FLASH
          inclusion, A3 WOULD block pending the test. The grader has
          already declined action-item / FLASH inclusion due to single-
          source veto and no-A&D-prime-named-victim; A3 corroborates
          that disposition independently.

        qualifying_caveats:
          - >
            "Per SafeDep" attribution must appear in every claim layer
            quoting Megalodon scope, timeline, or causal chain. A1
            (SafeDep faithful relay) is medium-confidence critical;
            scope figures (5,561 repos / 5,718 commits / 6h17m window)
            may compress on second-vendor independent audit.
          - >
            Long-tail "~5,500 smaller repositories" claim is the weakest
            evidence layer (A2 qualify) — only Tiledesk + Black-Iron-
            Project + WISE-Community have named per-victim trails.
            Brief should foreground the named-victim layer and treat
            the long-tail as scope-context only.
          - >
            Downstream Tiledesk causal chain (A3 test) is asserted by
            SafeDep but not yet corroborated by npm registry, Socket,
            or eljohnny himself. Brief language should be CONDITIONAL:
            "SafeDep reports the @tiledesk/tiledesk-server@2.18.6-2.18.12
            poisoning resulted from the workflow_dispatch poisoning;
            maintainer eljohnny has not publicly confirmed."
          - >
            Cross-corpus author-identity-spoofing pattern (A4 qualify)
            is a TECHNIQUE-CLASS observation. Brief MUST NOT imply
            single-actor cluster across Megalodon / TrapDoor / TeamPCP
            / node-ipc. Hard Rule 2 binding. The morning-23 ACH already
            ranked multi-actor-convergence H2 as leading; this finding
            inherits that framing.
          - >
            workflow_dispatch anti-recursion as intended-by-design (A5
            qualify, low confidence) — brief should NOT assume GitHub
            position is final. Note "no GitHub-side official statement
            observed at finding-write time" so the briefer can reflect
            a CVE-coordination-pending caveat if GitHub publishes during
            the brief window.

      recommended_wep_after_test:
        if_A3_corroborated_by_eljohnny_statement_or_socket_independent_analysis: >
          WEP ceiling could rise on the Tiledesk downstream layer to
          "very likely" pending second-vendor independence on the broader
          campaign. Cluster digraph remains capped by SafeDep grade until
          source-grades.yaml ratification or second A/B-grade independent
          vendor.
        if_A3_contradicted_eljohnny_publishes_alternative_compromise_vector: >
          Tiledesk-downstream-causal-link claim layer reclassifies from
          "likely" to "unlikely"; revise finding; remove from supply-
          chain-watch monitoring tier.
        if_A3_remains_unresolved_after_72h: >
          Hold at current "likely" with explicit "per SafeDep, not
          independently corroborated" caveat in all brief language;
          escalate to weekly-synthesis-2026-06-01 revisit.

  sat_ach:
    ach_analysis:
      question: >
        Given the eighth distinct 2026 supply-chain mass-compromise
        campaign in 14 days (now including Megalodon), does the multi-
        actor-convergence (H2) leading-hypothesis ranking from
        finding-2026-05-23-0001's morning ACH (later reinforced in
        finding-2026-05-23-0005's KAC-ACH-reweight) still hold, or
        does the Megalodon evidence shift the ranking?
      analyzed_at: 2026-05-25T08:54:00-04:00
      analyzed_by: analyst
      red_team_review: null    # red-team-analyst not invoked: cluster WEP ceiling is "likely" (single-source veto), below "very likely" red-team threshold per grader doctrine

      inherited_baseline: >
        finding-2026-05-23-0001 morning ACH: H2 (multi-actor convergence)
        rank-1, zero inconsistencies. H1 (single-cluster TeamPCP-aligned)
        rank-5, five inconsistencies weighted 13. H4 (copycat clustering)
        rank-2, zero inconsistencies but operationally indistinguishable
        from H2 without temporal-causation evidence.
        finding-2026-05-23-0005 KAC-ACH-reweight: H2 retains rank-1.
        Added H_new (multi-actor convergence WITH ecosystem-specific
        affinity refinement) tracking as H2 sub-hypothesis rather than
        replacement. H1 weighted disfavor accumulates to 24.

      hypotheses:
        - id: H1
          statement: >
            Single underlying actor or affiliate-group cluster is
            operating multiple personas across the 8-in-14-days wave
            (including Megalodon). Cross-corpus author-identity-spoofing
            pattern + temporal density supports the single-cluster reading.
          inherited_from: finding_2026_05_23_0001_morning_ach_H1
        - id: H2
          statement: >
            Multiple independent unattributed cybercriminal operators
            are converging on high-leverage supply-chain technique
            classes independently. Megalodon (workflow_dispatch
            anti-recursion bypass) is a new technique-class addition
            to the convergence rather than a single-actor extension.
          inherited_from: finding_2026_05_23_0001_morning_ach_H2_rank_1
        - id: H3
          statement: >
            The wave is a research-methodology / visibility artifact —
            supply-chain security vendors (SafeDep, Socket, Aikido,
            StepSecurity, Wiz) are getting better at detecting and
            disclosing this class of activity, not the threat landscape
            actually getting more active. The eight-in-14-days density
            reflects observer-side capability ramp.
          inherited_from: finding_2026_05_23_0001_morning_ach_H3_subset_observer_bias
        - id: H4
          statement: >
            An ecosystem-wide platform vulnerability or systemic gap
            (across GitHub Actions / npm / PyPI / Composer / Crates /
            Packagist) is being independently rediscovered by multiple
            campaigns. Megalodon's workflow_dispatch anti-recursion
            bypass is one instance; Laravel-Lang's GitHub-to-Packagist
            tag-resolution is another; the underlying pattern is
            platform-side, not adversary-coordination.
          inherited_from: NEW_for_this_ach_extends_finding_2026_05_23_0001_morning_ach_H4_copycat_with_platform_focus

      evidence:
        # E1-E17 inherited from morning-23 + 23-0005 reweight; new evidence E18-E24 for Megalodon-specific
        - id: E18
          description: >
            Megalodon C2 infrastructure (216.126.225.129:8443) shows
            no overlap with prior corpus campaigns: distinct from
            Mini Shai-Hulud 6 C2 domains, TrapDoor's ddjidd564.github.io
            GitHub-Pages dead-drop, Laravel-Lang's flipboxstudio[.]info,
            GitHub-corp's check-git-service[.]com / t-m-kosche[.]com,
            node-ipc's package-publish path
          source: cross_finding_corpus_analysis_c2_infrastructure_layer
          digraph: A1
          weight: 3
        - id: E19
          description: >
            Megalodon attack-class (workflow_dispatch anti-recursion
            bypass) is mechanically DISTINCT from all 7 prior corpus
            campaigns: not maintainer-credential theft (Mini Shai-Hulud,
            node-ipc), not Composer tag-resolution (Laravel-Lang), not
            postinstall + GitHub-hosted binary (Packagist 8-pkg), not
            multi-ecosystem simultaneous publication (TrapDoor), not
            GitHub Actions token theft via workflow injection
            (TanStack/OpenAI). Mechanical distinctness extends across
            ALL 8 campaigns
          source: cross_finding_corpus_analysis_attack_mechanism_layer
          digraph: A2
          weight: 3
        - id: E20
          description: >
            Megalodon UNATTRIBUTED per SafeDep explicit decline; vendor
            (SafeDep) is consistent with the 23-0001/23-0005 observation
            that supply-chain security vendors are independently
            declining attribution at scale (Socket on TrapDoor explicitly
            rules out TeamPCP/Shai-Hulud/Mini Shai-Hulud; Socket+Aikido
            decline on Laravel-Lang; four-firm consensus declines on
            node-ipc)
          source: safedep_explicit_decline_plus_cross_finding_corpus_attribution_layer
          digraph: A1
          weight: 3
        - id: E21
          description: >
            Megalodon author-identity-spoofing pattern (build-bot /
            auto-ci / ci-bot / pipeline-bot) extends the cross-corpus
            CI-bot-impersonation tradecraft observed in TeamPCP
            (claude@users.noreply.github.com) and node-ipc (atiertant).
            Pattern is portable post-access and now appears in 4+
            unattributed campaigns
          source: cross_finding_corpus_pattern_observation_finding_2026_05_25_0001
          digraph: B2
          weight: 2
        - id: E22
          description: >
            Megalodon scope-density unique: 5,561 distinct repositories
            in 6h17m via single attack mechanism is the largest single-
            event scope in the 14-day wave by an order of magnitude
            (Mini Shai-Hulud npm worm scope was hundreds of packages
            over days; node-ipc scope was single package; Laravel-Lang
            scope was hundreds of tags on one package; Packagist 8-pkg
            scope was 8 packages)
          source: cross_finding_corpus_scope_layer_finding_2026_05_25_0001
          digraph: B2
          weight: 2
        - id: E23
          description: >
            Megalodon exploits a documented-by-GitHub design behavior
            (workflow_dispatch anti-recursion) — the abuse is creative
            but the underlying mechanism is a platform-feature gap, not
            a credential-theft vector. Mechanism uniqueness suggests
            specific platform-knowledge rather than commodity stealer
            kit
          source: safedep_megalodon_blog_2026_05_21_mechanism_description
          digraph: B2
          weight: 2
        - id: E24
          description: >
            No Splunk first-party hits on Megalodon IOC layer; consistent
            with all prior 7 wave campaigns having zero first-party
            hits in defenseclaw_local — the local instance is narrow-
            ingest and structurally bounded
          source: finding_first_party_precedence_section_plus_56_consecutive_dormant_non_self_sweeps
          digraph: A1
          weight: 3

      matrix:
        E18: {H1: I, H2: C, H3: N, H4: C}    # NO infrastructure overlap with prior campaigns strongly inconsistent with single-cluster (H1); consistent with multi-actor or independent rediscovery; non-diagnostic on observer-bias
        E19: {H1: I, H2: C, H3: N, H4: C}    # mechanical distinctness across all 8 campaigns inconsistent with one cluster iterating; consistent with multi-actor convergence and platform-rediscovery
        E20: {H1: I, H2: C, H3: N, H4: C}    # continued no-attribution at scale extends morning-23 E10 / 23-0005 E15 diagnostic against H1
        E21: {H1: C, H2: C, H3: N, H4: N}    # CI-bot-impersonation pattern is portable; consistent with H1 (one cluster reusing tradecraft) AND H2 (multiple operators independently adopting); not actor-collapse signal alone per A4
        E22: {H1: N, H2: N, H3: I, H4: C}    # order-of-magnitude scope-density spike argues against H3 (observer-bias would distribute more evenly); consistent with H4 (a platform-mechanism-discovery moment can produce one-shot large scope)
        E23: {H1: N, H2: C, H3: N, H4: C}    # platform-feature-gap exploitation reinforces H4; consistent with H2 (a multi-actor convergence layer can include platform-rediscovery as one technique-class)
        E24: {H1: N, H2: N, H3: N, H4: N}    # narrow-ingest first-party silence is non-diagnostic across all hypotheses per Hard Rule 8

      inconsistency_counts_megalodon_new_only:
        H1: 3    # E18, E19, E20 — accumulated weight 9 (3+3+3)
        H2: 0
        H3: 1    # E22 — weight 2
        H4: 0

      inconsistency_counts_cumulative_with_inherited:
        H1_morning_23: 5            # E4, E6, E7, E8, E10 weighted 13
        H1_23_0005_reweight: 4      # E12, E13, E15, E17 weighted 11
        H1_25_0001_megalodon: 3     # E18, E19, E20 weighted 9
        H1_cumulative_total: 12     # weighted 33 across three ACH passes
        H2_cumulative_total: 0
        H3_cumulative_total: 1      # E22 only — weight 2
        H4_cumulative_total: 0

      diagnostic_evidence:
        - E18: >
            Megalodon C2 infrastructure non-overlap with all prior
            campaigns extends the morning-23 E6 diagnostic into the
            8th campaign with zero exceptions. Strongly distinguishes
            H2/H4 from H1.
        - E19: >
            Mechanical distinctness across 8 campaigns extends morning-
            23 E7 diagnostic into the 8th campaign with zero exceptions.
            Strongly distinguishes H2/H4 from H1.
        - E20: >
            Continued no-attribution-at-scale (4-firm consensus + 2
            explicit vendor rule-outs of TeamPCP) extends morning-23
            E10 and 23-0005 E15 diagnostic. Strongly distinguishes H2
            from H1.
        - E22: >
            Order-of-magnitude scope-density spike on Megalodon (5,561
            repos in 6h17m) distinguishes H3 (observer-bias) from H4
            (platform-mechanism-discovery moment). Argues against H3
            specifically.
        - E23: >
            Platform-feature-gap exploitation (workflow_dispatch
            anti-recursion as documented design) reinforces H4 as a
            distinct hypothesis from H2 — platform-side rediscovery is
            a different causal model from independent multi-actor TTP
            convergence, even though they share the "not coordinated"
            character.

      ranking:
        - rank: 1
          hypothesis_id: H2
          rationale: >
            Multi-actor convergence on supply-chain technique classes.
            ZERO cumulative inconsistencies across three ACH passes
            (morning-23, 23-0005 reweight, 25-0001 megalodon). H2 has
            now been load-tested against eight distinct campaigns and
            retains rank-1.
          wep: >
            Forward prediction on cross-corpus pattern: likely (single-
            source-veto holds at "likely" on any synthesis-layer
            cross-corpus claim — see WEP discipline below).
          delta_from_inherited_baseline: rank_1_retained_with_cumulative_strengthening
        - rank: 2
          hypothesis_id: H4
          rationale: >
            Platform-vulnerability independent-rediscovery hypothesis is
            NEW for this ACH (extends morning-23 H4 copycat with platform-
            focus). Zero inconsistencies on Megalodon-specific evidence.
            E22 + E23 mildly favor H4 for Megalodon specifically
            (platform-mechanism-discovery shape). However, H4 cannot be
            promoted above H2 because (a) Megalodon's platform-mechanism
            is specific to GitHub Actions, while other wave campaigns
            (Composer tag-resolution, npm credential-worming, Crates/
            PyPI simultaneous publication) are not all platform-feature-
            gap exploitations, so H4 doesn't account for the broader
            wave as cleanly as H2 does. H4 likely accounts for the
            SUBSET of the wave that is platform-feature-gap (Megalodon
            + possibly TanStack/OpenAI + possibly Laravel-Lang); H2
            accounts for the broader convergence.
          wep: roughly_even_chance    # against the H2-rank-1 framing; H4 is a coherent alternative for the platform-focus subset
          delta_from_inherited_baseline: NEW_rank_2_promoted_above_morning_23_H4_copycat
        - rank: 3
          hypothesis_id: H1
          rationale: >
            Single-cluster reading. THREE additional inconsistencies
            from Megalodon evidence (E18, E19, E20) bring cumulative
            weighted disfavor to 33 across three ACH passes. Continues
            to be strongly disfavored. H1 retained in the matrix for
            falsifiability discipline — a future vendor disclosure
            attributing 2+ wave campaigns to one operator would
            promote H1 — but at current evidence level remains rank-3.
          wep: unlikely
          delta_from_inherited_baseline: continued_strong_disfavor_rank_unchanged_at_3
        - rank: 4
          hypothesis_id: H3
          rationale: >
            Research-methodology / visibility artifact hypothesis. E22
            (Megalodon order-of-magnitude scope-density spike) is one
            inconsistency: observer-bias would produce more even
            distribution rather than a single 5,561-repo 6h17m
            super-event. H3 hasn't been a leading hypothesis in any
            inherited ACH but is retained for falsifiability. Mild
            additional disfavor from Megalodon.
          wep: unlikely
          delta_from_inherited_baseline: continued_disfavor

      sensitivity_analysis:
        brittleness: medium
        load_bearing_evidence:
          - E18  # C2 infrastructure non-overlap diagnostic — if Megalodon C2 were later linked to any prior wave campaign's infrastructure, H1 would suddenly become plausible
          - E19  # mechanical distinctness — if Megalodon's payload internals turn out to share kit (same XOR keys, same exfil-encryption, same C2 protocol) with prior wave campaigns, H1 would rise
          - E20  # continued no-attribution-at-scale — if a single A-grade vendor (Wiz, Mandiant, MSTIC) publishes tradecraft-cluster analysis attributing 2+ wave campaigns to one operator, H1 would dominate

        if_E18_inverted_megalodon_c2_overlap_emerges: >
          H1 promotes from rank-3 to rank-1 contender. Cumulative
          inconsistency count on H1 drops from 12 to 11. Rerun full
          ACH with infrastructure-overlap-as-newly-diagnostic evidence.
        if_E19_inverted_kit_sharing_revealed_in_reverse_engineering: >
          H1 promotes significantly. Mechanical distinctness was the
          backbone of the H2 case across three ACH passes.
        if_E20_inverted_vendor_publishes_cross_campaign_attribution: >
          H1 promotes to leader. H2 becomes the alternative-explanation
          rather than the leading hypothesis. Rerun ACH from scratch
          with new attribution evidence.
        if_safedep_grade_drops_or_megalodon_disclosure_is_partially_retracted: >
          E18, E19, E22, E23 all weight lower. H4 (platform-rediscovery)
          may lose support specifically because Megalodon was its
          strongest example. H2 (multi-actor convergence) loses one of
          eight supporting campaigns but retains rank-1 on the other
          seven.

      tripwires:
        - observation: >
            Second A/B-grade vendor (Snyk, Wiz, Aikido, StepSecurity,
            Socket, Unit 42, Ox Security, Upwind, Checkmarx, MSTIC,
            ESET, Sophos, Bitdefender) publishes independent analysis
            on Megalodon within 24-72h
          effect: >
            Cluster digraph reclassifies toward C1 / B2; single-source
            veto on Megalodon-specific layers lifts; ACH evidence
            weights recalibrate.
        - observation: >
            GitHub publishes official statement on workflow_dispatch
            anti-recursion behavior (advisory, hardening guidance, or
            CVE assignment)
          effect: >
            E23 (platform-feature-gap framing) weight changes. If CVE
            assigned, H4 (platform-rediscovery) strengthens marginally.
            If "intended-by-design" confirmed, defender-response framing
            crystallizes.
        - observation: >
            Tiledesk maintainer eljohnny publicly confirms (or refutes)
            the workflow-poisoning-to-npm-publication causal chain
          effect: >
            A3 KAC test resolved. Cluster status on Tiledesk downstream
            layer either confirms toward C1 or retracts.
        - observation: >
            Vendor publishes tradecraft-cluster analysis attributing
            2+ wave campaigns to one operator (most likely Wiz, given
            their TeamPCP attribution discipline)
          effect: >
            H1 promotes to leader. Rerun full ACH from scratch. Update
            actor-profiler TTP catalog with cross-campaign linkage.
        - observation: >
            A 9th supply-chain mass-compromise surfaces within 7 days,
            extending the wave beyond Megalodon
          effect: >
            Either reinforces H2 (continued multi-actor convergence) or,
            if mechanically similar to Megalodon (workflow_dispatch or
            CI/CD platform-feature-gap class), strengthens H4 platform-
            rediscovery reading.
        - observation: >
            Megalodon attack-class recurs post-disclosure (copycat
            workflow_dispatch anti-recursion abuse by other operators)
          effect: >
            Reinforces H2 (technique now portable and adopted broadly)
            AND H4 (platform-feature-gap incentivizes rediscovery).
            Does NOT differentiate H2 vs H4 — both predict recurrence.

      conclusion:
        summary: >
          Multi-actor convergence (H2) RETAINS rank-1 across all three
          ACH passes (morning-23, 23-0005 reweight, 25-0001 megalodon).
          Cumulative weighted disfavor of H1 (single-cluster) reaches 33
          across the wave's first eight campaigns. Megalodon adds a NEW
          rank-2 hypothesis (H4: ecosystem-platform-vulnerability
          independent-rediscovery) that accounts for the subset of the
          wave that is platform-feature-gap exploitation; H4 cannot
          dominate H2 because the broader wave includes credential-
          theft, tag-resolution-abuse, and multi-ecosystem-simultaneous-
          publication patterns that are not all platform-feature-gap.
          H1, H3 strongly disfavored but retained for falsifiability.
          ACH on this cluster is NOT producing novel attribution — it
          is pressure-testing the sourced non-attributions (SafeDep,
          Socket, Socket+Aikido, four-firm-consensus) and finding them
          analytically defensible against the alternative single-cluster
          reading that the temporal density tempts.
        wep: >
          On the cross-corpus synthesis question (which hypothesis best
          accounts for the 8-in-14-days wave): likely H2 (multi-actor
          convergence) with H4 (platform-rediscovery for the platform-
          gap subset) as a plausible refinement. Cluster Megalodon-
          specific WEP ceiling remains "likely" per grader (single-
          source veto holds on Megalodon-internal claims).
        confidence_caveats: >
          (1) ACH RANKS hypotheses; it does NOT CREATE attribution.
          Hard Rule 2 binding. (2) H2 is consistent with all four cited
          vendor sources DECLINING attribution; treating ACH ranking as
          permission to attribute would be the textbook violation
          ACH was designed to prevent. (3) Sensitivity is medium: a
          single A-grade vendor cross-campaign attribution would flip
          the ranking. (4) Single-source veto on Megalodon caps the
          cluster's contribution to the cross-corpus synthesis at
          "likely" weight — ACH cumulative-evidence-strengthening on
          H2 does NOT override admiralty rules.
        h2_vs_h4_distinction_for_briefer: >
          For brief framing: H2 says "multiple operators chose
          supply-chain TTPs independently." H4 says "the platforms
          have systemic gaps that multiple parties are independently
          finding." Both are 'not-coordinated' framings; the difference
          is whether the focus is on adversary-side convergence (H2) or
          platform-side gap (H4). Briefer should foreground the
          DEFENDER-POSTURE implication (which is the same under H2 and
          H4): supply-chain attack-class is the operational concern;
          actor-identity-cluster is NOT a useful defender frame.

# Lifecycle
tlp: CLEAR
published_in_briefs:                 # briefer appends brief_ids
  - 2026-05-25-morning
retracted: false
retraction_brief_id: null

# Open questions for analyst (grader-flagged)
open_questions_for_analyst:
  - question: >
      Does any second A/B-grade vendor (Snyk, Wiz, Aikido, StepSecurity,
      Socket, Unit 42 npm threat landscape, Ox Security, Upwind,
      Checkmarx, MSTIC, ESET, Sophos, Bitdefender) surface independent
      analysis on the Megalodon 5,561-repository cluster within 24-72h
      post-SafeDep disclosure? If yes, regrade toward C1 / B2; if no,
      single-source posture continues at C2.
    flagged_by: grader
    priority: high
    target_completion: afternoon_brief_2026_05_25_or_morning_brief_2026_05_26
  - question: >
      What is the GitHub-side official position on the workflow_dispatch
      anti-recursion behavior? SafeDep frames it as intended-by-design;
      if GitHub agrees, no CVE coordination is expected and defender
      response is procedural (workflow-file branch-protection rules,
      required-reviews on .github/workflows/*.yml changes). If GitHub
      reclassifies it as a vulnerability, a CVE could be assigned
      retroactively and the vuln-tracker hook activates.
    flagged_by: grader
    priority: high
    target_completion: next_24_72h
  - question: >
      What is the npm registry-side remediation status of the 7
      poisoned @tiledesk/tiledesk-server versions (2.18.6 through
      2.18.12)? Are they removed, deprecated, or still installable?
      Removal status is load-bearing for the defender-action-item
      layer (operators need to know whether removing already-installed
      poisoned versions is sufficient or whether fresh installs are
      still possible).
    flagged_by: grader
    priority: high
    target_completion: afternoon_brief_2026_05_25
  - question: >
      Has Tiledesk maintainer `eljohnny` publicly confirmed the
      compromise scope and remediation timeline? SafeDep characterizes
      eljohnny as the unknowing publisher; a direct maintainer
      statement would add victim-self-disclosure evidence basis and
      potentially regrade the downstream-tiledesk-causal-link claim
      layer.
    flagged_by: grader
    priority: medium
    target_completion: afternoon_brief_2026_05_25_or_morning_brief_2026_05_26
  - question: >
      Is the cross-corpus author-identity-spoofing pattern (build-bot
      / auto-ci / ci-bot / pipeline-bot in Megalodon; claude@users.
      noreply.github.com in TeamPCP/Mini Shai-Hulud; atiertant in
      node-ipc) genuinely a portable technique-class shared across
      multiple unattributed operators, OR does it support a multi-
      actor-convergence H2 reading that warrants attribution-by-
      tradecraft-cluster analysis? Hard Rule 2 prohibits Archimedes-
      originated attribution, but actor-profiler can catalog this as
      a TTP-class observation for the SDLC-targeting wave dossier.
    flagged_by: grader
    priority: medium
    target_completion: next_update_tracking_cycle
  - question: >
      Does the Megalodon attack pattern (mass GitHub-repo backdooring
      via workflow_dispatch anti-recursion bypass) recur post-
      disclosure? The public disclosure of the abuse mechanism makes
      the technique available to other operators; defender-side
      hardening (branch-protection rules on .github/workflows/*.yml,
      required-reviews, signed commits) may not propagate quickly
      enough to prevent copycat operations.
    flagged_by: grader
    priority: medium
    target_completion: weekly_synthesis_2026_06_01
  - question: >
      What is the A&D-prime SDLC procedural exposure assessment? No
      A&D-prime victim is named in SafeDep's coverage. Tiledesk is
      live-chat / chatbot infrastructure that may appear in A&D-prime
      customer-support stacks, partner-portal layers, or internal IT
      help-desk deployments rather than mission-system SDLCs. The
      higher-impact takeaway is the workflow_dispatch anti-recursion
      bypass mechanism itself — any A&D-prime SDLC operating GitHub
      Actions is procedurally exposed to the same attack class if a
      repo's workflow files can be modified by a poisoned committer
      identity. Operator should consider whether to issue an internal
      advisory to A&D-prime SDLC stakeholders on branch-protection
      rules + required-reviews on workflow-file changes.
    flagged_by: grader
    priority: medium
    target_completion: weekly_synthesis_2026_06_01_or_internal_advisory_drafting

# Hard Rules compliance
hard_rules_compliance:
  rule_2_no_attribution_origination: |
    UNATTRIBUTED preserved per SafeDep + SecurityWeek primary sources.
    SafeDep explicitly declines to attribute to any tracked actor or
    nation-state; credits discovery to internal "Malysis engine."
    SecurityWeek uses generic "the attacker" / "attackers" language.
    Cross-corpus author-identity-spoofing pattern (build-bot / auto-ci
    / ci-bot / pipeline-bot vs. TeamPCP's claude@users.noreply.github.com
    vs. node-ipc's atiertant vs. TrapDoor unspecified) is flagged as
    technique-class observation for actor-profiler TTP catalog, NOT
    as actor-attribution. Archimedes does NOT collapse Megalodon /
    TrapDoor / TeamPCP / node-ipc into a single actor without
    A/B-grade attribution.
  rule_3_no_exploitation: |
    No PoC code reproduced. Attack mechanism (workflow_dispatch
    anti-recursion bypass) described at conceptual level for
    defender-detection-engineering purposes. Operator-side detection
    guidance and Splunk SPL examples are defensive.
  rule_4_passive_only: |
    No active scans. SafeDep direct-retrieval is passive; Splunk
    first-party query is on Archimedes's own instance. SpiderFoot not
    invoked. authorized-targets.yaml empty.
  rule_6_quote_limit: |
    Single 4-word quoted phrase from SafeDep ("base64-encoded bash")
    for technical-mechanism preservation in the raw-signal — within
    15-word limit, single instance per source. No additional quotes
    in this finding's prose.
  rule_7_credentials_radioactive: |
    No credential exposure surfaced in the SafeDep or SecurityWeek
    coverage. Forged email addresses on the SafeDep primary surface
    are Cloudflare-protected and were not extracted in cleartext.
  rule_8_splunk_first_party_priority: |
    Collector-executed targeted 17-IOC hand-built Splunk sweep on
    `defenseclaw_local` (component of the consolidated query
    documented in raw-2026-05-25-am-000 sentinel) returned ZERO events
    on the Megalodon IOC layer. 56th consecutive dormant non-self
    sweep posture on `defenseclaw_local`. Per Hard Rule 8: first-party
    silence is neither confirming nor disconfirming. `defenseclaw_local`
    is a local Splunk instance not connected to a production network;
    IOC-class payload observation is structurally bounded by the
    instance's narrow ingest scope.
---

# Megalodon: 5,561 GitHub repositories backdoored via GitHub Actions workflow_dispatch anti-recursion bypass; downstream @tiledesk/tiledesk-server npm poisoning; UNATTRIBUTED per SafeDep

## Summary

SafeDep (graded C provisional) disclosed on 2026-05-21 a mass GitHub-repo backdooring campaign dubbed Megalodon in which 5,718 malicious commits were pushed across 5,561 distinct repositories during a 6h17m window on 2026-05-18 (11:36 UTC to 17:48 UTC). The attack abuses GitHub Actions workflow_dispatch anti-recursion behavior — GitHub does not retrigger workflow files that themselves committed workflow files — allowing a committer with a fake automated-commit identity to deploy CI-time payloads without firing a recursive-trigger detection. Downstream, the legitimate Tiledesk npm maintainer `eljohnny` unknowingly published 7 poisoned versions of `@tiledesk/tiledesk-server` (2.18.6 through 2.18.12) between 2026-05-19 and 2026-05-21 from the compromised source-of-truth repository. C2 infrastructure is `216.126.225.129:8443`. Attribution is UNATTRIBUTED — SafeDep credits discovery to its internal Malysis engine and explicitly declines to link Megalodon to any tracked actor; SecurityWeek (Ionut Arghire, 2026-05-25 03:40 EDT in-window relay) uses generic "attackers" language. No A&D-prime victim is named. The cluster is graded C2 (single-source SafeDep evidence basis; SecurityWeek is pure relay and does not provide independent corroboration) with single-source veto applied — WEP ceiling is "likely" on all claim layers. The finding is monitoring-tier-only (below B2 action-item threshold) pending second A/B-grade vendor independent analysis.

## Sources

### SafeDep (safedep, digraph: C)

- URL: https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows
- Published: 2026-05-21 (4 days prior to SecurityWeek pickup; collection-gap acknowledged)
- Byline: SafeDep Team (no individual researcher named)
- Key claim: 5,718 malicious commits across 5,561 distinct GitHub repositories injected 2026-05-18 11:36-17:48 UTC via GitHub Actions workflow_dispatch anti-recursion bypass; two payload variants (SysDiag and Optimize-Build); downstream `@tiledesk/tiledesk-server` poisoning; UNATTRIBUTED.

### SecurityWeek (securityweek, digraph: B — but RELAY of SafeDep, not independent)

- URL: https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/
- Published: 2026-05-25 03:40 EDT (in-window)
- Byline: Ionut Arghire
- Key claim: Relays SafeDep's disclosure with the 5,500+ repository scope count and the workflow_dispatch abuse mechanism; uses generic "the attacker" / "attackers" language; does NOT contribute independent telemetry or independent IOC discovery. Per INTEL-GRADING.md independence test, SecurityWeek summarizing SafeDep is NOT corroboration.

## Technical detail

### Attack mechanism — workflow_dispatch anti-recursion bypass

GitHub Actions does not retrigger workflow runs that were themselves triggered by a workflow committing a file. This anti-recursion behavior — characterized by SafeDep as intended-by-design — means a committer who pushes a `.github/workflows/*.yml` file via a fake automated-commit identity can deploy CI-time payloads without firing a recursive-trigger detection.

The campaign deployed two payload variants using this mechanism:

| Variant | Trigger surface | Effect |
|---|---|---|
| SysDiag | `push` (all branches) + `pull_request_target` | Maximum automated execution; runs on every push + every PR-merge candidate |
| Optimize-Build | `workflow_dispatch` (replaces existing) | Dormant backdoor executable via GitHub API when operator chooses (using stolen tokens) |

Both variants:

- Request permissions `id-token: write` and `actions: read`
- Execute via `set +e; echo "<BASE64>" | base64 -d | bash` one-liners (base64-decoded bash, per SafeDep — 4-word quoted phrase under Hard Rule 6 limit)
- Target CI environment variables; AWS / GCP / Azure credentials; SSH private keys; Docker / Kubernetes configs; API keys; database connection strings; GitHub Actions tokens; GitLab CI/CD tokens

### Timeline

| Time (UTC) | Event |
|---|---|
| 2026-05-18 11:36-17:48 | Mass-injection window: 5,718 commits across 5,561 repositories |
| 2026-05-19 | `@tiledesk/tiledesk-server@2.18.6` published to npm by `eljohnny` from now-poisoned source-of-truth |
| 2026-05-19 -> 2026-05-21 | Sequential npm publication of versions 2.18.7 through 2.18.12 |
| 2026-05-21 | SafeDep primary research published |
| 2026-05-25 03:40 EDT | SecurityWeek (Ionut Arghire) in-window relay |

### CVE coordination status

NO CVE assigned. SafeDep characterizes the workflow_dispatch anti-recursion behavior as intended-by-design GitHub Actions behavior; GitHub-side official position not yet observed. If GitHub agrees with intended-by-design framing, no CVE coordination is expected and defender response is procedural (branch-protection rules and required-reviews on `.github/workflows/*.yml` changes). If GitHub reclassifies it as a vulnerability, a CVE could be assigned retroactively and a vuln-tracker entry would activate.

## IOCs surfaced

### C2 infrastructure

- `216.126.225.129:8443` (single C2 IP, single port observed)

### Compromised npm package versions

- `@tiledesk/tiledesk-server@2.18.6`
- `@tiledesk/tiledesk-server@2.18.7`
- `@tiledesk/tiledesk-server@2.18.8`
- `@tiledesk/tiledesk-server@2.18.9`
- `@tiledesk/tiledesk-server@2.18.10`
- `@tiledesk/tiledesk-server@2.18.11`
- `@tiledesk/tiledesk-server@2.18.12`

Clean version: `@tiledesk/tiledesk-server@2.18.5` and earlier.

### Forensic commit hash (Tiledesk)

- `acac5a9854650c4ae2883c4740bf87d34120c038`

### Throwaway GitHub accounts (3 named examples; pattern: 8-char random alphanumeric, no prior commit history, created shortly before 2026-05-18)

- `rkb8el9r`
- `bhlru9nr`
- `lo6wt4t6`

### Author-identity spoofing (forged Git author names)

- `build-bot`
- `auto-ci`
- `ci-bot`
- `pipeline-bot`

Associated forged email addresses are Cloudflare-protected on the SafeDep primary surface and were not extracted in cleartext.

### Forged commit-message templates (7 variants)

- `ci: add build optimization step`
- `build: improve ci performance`
- `chore: optimize pipeline runtime`
- `chore: sync ci configuration`
- `chore: update ci/cd pipeline`
- `ci: update build config`
- `fix: correct build workflow`

### Workflow filenames

- `.github/workflows/ci.yml` (SysDiag variant — push + pull_request_target)
- Existing workflows REPLACED in the Optimize-Build variant (filename varies per victim)

### npm maintainer

- `eljohnny` (legitimate Tiledesk maintainer; UNKNOWING publisher of poisoned versions 2.18.6-2.18.12 per SafeDep)

### Victim scope

- Primary: Tiledesk (9 repositories — `tiledesk-server`, `tiledesk-dashboard`, `tiledesk-telegram-connector`, `tiledesk-llm`, `tiledesk-docker-proxy`, `tiledesk-community-app`, `tiledesk-campaign-dahboard` [sic per SafeDep], `tiledesk-helpcenter-template`, `tiledesk-ai`)
- Secondary: Black-Iron-Project (8 repositories); WISE-Community (count not specified by SafeDep)
- Long tail: ~5,500 smaller repositories (individual personal blogs, small OSS projects, miscellaneous)
- A&D / defense / aerospace victims: NONE NAMED in either source

## Relationship to existing findings

**Eighth distinct 2026 supply-chain mass-compromise campaign in the corpus within the 14-day window 2026-05-12 to 2026-05-25.** Mechanically distinct from prior corpus events:

- finding-2026-05-24-0001 (TrapDoor): npm + PyPI + Crates.io simultaneous publication; one attacker identity across three ecosystems; GitHub Pages dead-drop; `.cursorrules` + `CLAUDE.md` AI-agent-config persistence. UNATTRIBUTED per Socket explicit decline (specifically NOT TeamPCP / Shai-Hulud / Mini Shai-Hulud).
- finding-2026-05-23-0005 (Packagist 8-pkg): Composer/Packagist `postinstall` in `package.json` + GitHub-hosted Linux binary. UNATTRIBUTED.
- finding-2026-05-23-0001 (Laravel-Lang): Composer/Packagist GitHub-to-Packagist tag-resolution abuse + `autoload.files` + `helpers.php` per-request execution. UNATTRIBUTED.
- finding-2026-05-21-0003 (nx-console): formal confirmation of 18-minute compromise window publication.
- finding-2026-05-20-0001 (SecurityWeek Mini Shai-Hulud @antv continuation): TeamPCP-attributed per Wiz + StepSecurity.
- finding-2026-05-20-FLASH-0001 (GitHub-corp internal repos via VS Code extension): TeamPCP-claimed.
- finding-2026-05-14-0009 (node-ipc npm supply-chain): UNATTRIBUTED four-firm consensus.
- finding-2026-05-14-0008 (TanStack / OpenAI GitHub Actions): mechanically closest prior corpus precedent — CI/CD token theft via workflow injection.
- finding-2026-05-12-FLASH-0001 (Mini Shai-Hulud npm + PyPI worm): TeamPCP-attributed per Wiz + StepSecurity.

Megalodon introduces the **first corpus instance of mass GitHub-repo backdooring at scale (5,561 distinct repos in 6h17m) via workflow_dispatch anti-recursion bypass** — novel attack-class within the corpus. The mechanism is distinct from CI/CD-token theft (TanStack/OpenAI), maintainer-credential worming (Mini Shai-Hulud), and ecosystem-side abuse (Laravel-Lang, Packagist 8-pkg, TrapDoor).

Pattern observation inherits the multi-actor-convergence H2 framing from finding-2026-05-23-0001 ACH and finding-2026-05-23-0005 KAC. This finding does NOT re-run ACH — analyst should consider whether the eighth 2026 supply-chain mass-compromise campaign in 14 days warrants ACH-reweight at next analyst pass.

## Open questions for analyst

See `open_questions_for_analyst` in frontmatter. Highest-priority items:

1. Does any second A/B-grade vendor surface independent analysis on the Megalodon cluster within 24-72h?
2. What is the GitHub-side official position on the workflow_dispatch anti-recursion behavior?
3. What is the npm registry-side remediation status of the 7 poisoned `@tiledesk/tiledesk-server` versions?
4. Has Tiledesk maintainer `eljohnny` publicly confirmed compromise scope and remediation timeline?
5. Does the cross-corpus author-identity-spoofing pattern warrant a TTP-class catalog entry in the actor-profiler SDLC-targeting wave dossier?

## Analytic notes

- **SafeDep grade is C, not B.** The collector raw-signal speculated tentative-A/B based on Socket/Snyk-tier comparison; source-grades.yaml has SafeDep at C-provisional (since 2026-05-12). The grader cannot uplift the grade unilaterally — operator-side ratification via source-grade-log is required to move SafeDep to B. The C2 grade reflects authoritative source-grades.yaml.
- **SecurityWeek is a relay, not an independent corroborator.** Despite SecurityWeek's B-provisional grade, summarizing SafeDep's research does not satisfy the INTEL-GRADING.md independence test (different evidence basis required). The cluster effectively stands on SafeDep's evidence basis alone.
- **Inclusion is monitoring-tier only.** C2 meets the C3 minimum for monitoring inclusion in the morning brief but does NOT meet the B2 minimum for action-item inclusion or FLASH. The briefer should frame this as a Supply Chain Watch monitoring item, not as an action-item carrying confident assessment.
- **A&D relevance is structural-indirect.** No A&D-prime victim named. Tiledesk is live-chat / chatbot infrastructure that may appear in A&D-prime customer-support stacks or internal IT help-desk deployments — lower-criticality blast radius than a mission-system SDLC. The higher-impact takeaway is the workflow_dispatch anti-recursion bypass mechanism itself, which any A&D-prime SDLC operating GitHub Actions is procedurally exposed to if a repo's workflow files can be modified by a poisoned committer identity.

## Analytic notes (from analyst review)

SAT-KAC surfaced 8 assumptions across the finding; 2 sound (A6 Splunk-silence-as-genuine-non-exposure, A7 SecurityWeek-as-faithful-relay), 5 qualify (A1 SafeDep-faithful-relay; A2 workflow_dispatch-as-genuine-abuse; A4 author-identity-spoofing-as-technique-class-not-actor-collapse; A5 anti-recursion-as-intended-by-design; A8 novel-attack-class-as-genuinely-novel-in-corpus), 1 test (A3 Tiledesk-downstream-causal-link), 0 reject. The Test classification on A3 does NOT block monitoring-tier inclusion (which is the only inclusion tier the grader proposed) — it WOULD block action-item or FLASH, which the grader already declined on independent grounds. Brief language on the Tiledesk causal chain must be explicitly conditional ("SafeDep reports … maintainer eljohnny has not publicly confirmed"). The long-tail ~5,500 smaller-repositories scope claim is the weakest layer per A2 qualify and should be foregrounded by the named-victim trio (Tiledesk + Black-Iron-Project + WISE-Community) rather than headlined.

SAT-ACH extended the multi-actor-convergence (H2) ranking inherited from finding-2026-05-23-0001 morning ACH and finding-2026-05-23-0005 KAC-ACH-reweight into an eighth campaign. H2 RETAINS rank-1 with zero cumulative inconsistencies across three ACH passes; H1 (single-cluster) accumulates weighted disfavor to 33. Megalodon introduced a NEW rank-2 hypothesis H4 (ecosystem-platform-vulnerability independent-rediscovery) for the subset of the wave that is platform-feature-gap exploitation; H4 cannot dominate H2 because the broader wave includes credential-theft, tag-resolution-abuse, and multi-ecosystem-simultaneous-publication patterns that are not platform-feature-gap. The H2-vs-H4 distinction is operationally moot for defender posture — both are "not coordinated" framings — and the brief should foreground the supply-chain-attack-class concern rather than the actor-identity-cluster question.

**Briefer caveats inherited from SAT outputs:** (1) every Megalodon scope/timeline/causal-chain claim attributed "per SafeDep" with explicit independence-pending note; (2) Tiledesk downstream framed conditionally; (3) cross-corpus author-identity-spoofing labeled technique-class observation, NOT actor-collapse signal; (4) GitHub-side workflow_dispatch position framed as not-yet-observed; (5) for the cross-corpus 8-in-14-days framing, multi-actor convergence is the leading analytic line — Hard Rule 2 binding, no single-actor cluster collapse. WEP ceiling stands at grader's "likely"; no adjustment recommended.
