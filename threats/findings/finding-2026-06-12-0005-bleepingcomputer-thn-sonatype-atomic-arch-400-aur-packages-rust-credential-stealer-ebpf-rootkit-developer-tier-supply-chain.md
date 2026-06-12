---
id: finding-2026-06-12-0005
finding_id: finding-2026-06-12-0005-bleepingcomputer-thn-sonatype-atomic-arch-400-aur-packages-rust-credential-stealer-ebpf-rootkit-developer-tier-supply-chain
title: "400+ Arch User Repository (AUR) packages hijacked — Sonatype 'Atomic Arch' campaign; new maintainer accounts adopted abandoned packages and modified PKGBUILD/.install scripts; Rust credential stealer with optional eBPF rootkit; 8 developer-secret categories targeted (GitHub/npm/Vault tokens, OpenAI creds, SSH keys, Docker, VPN); two waves; official Arch repos NOT affected; BC + THN independent publisher convergence; no actor attribution"
date: 2026-06-12
created_at: 2026-06-12T16:45:00-04:00
graded_by: grader
grading_run_id: afternoon-20260612-160000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading (admiralty-grading skill output) — LAYERED
# ============================================================================
digraph: B2
admiralty_grade: B2
digraph_layered:
  # ---- VENDOR RESEARCH LAYER (Sonatype primary; two B-grade independent publisher relays + independent researcher) ----
  sonatype_atomic_arch_campaign_designation: B2  # Sonatype primary not in source-grades.yaml; provisional B-tier per cheatsheet "named vendor with structured public technical research"; two independent B-grade publisher relays (BC + THN)
  campaign_compromise_method_orphaned_aur_package_adoption: A2  # BC + THN publisher-independent corroboration on the mechanism; vendor-canonical at Sonatype layer
  pkgbuild_install_script_modification_to_execute_npm_bun_install: A2  # BC + THN publisher-independent corroboration
  weaponized_atomic_lockfile_package_delivered_during_build: A2  # BC + THN publisher-independent corroboration
  spoofed_git_commit_metadata_for_maintainer_change_disguise: B2  # Sonatype primary via BC + THN; technical claim
  initial_wave_20_plus_packages_expanded_to_408_in_two_waves: A2  # BC + THN publisher-independent corroboration on scope
  official_arch_repositories_NOT_affected_aur_only: A1  # BC + THN publisher-independent + technically-coherent scope statement; AUR vs official repo distinction is verifiable at the Arch Linux project level
  in_the_wild_actively_exploited_two_waves_identified: A2  # BC + THN publisher-independent
  whanos_independent_researcher_reverse_engineering: B3  # Independent researcher tracked as "Whanos"; not in source-grades.yaml; provisional B-tier per cheatsheet "researcher with named handle, public technical attestation"; supplementary corroboration
  # ---- PAYLOAD LAYER ----
  rust_binary_payload_built_to_harvest_developer_secrets: A2  # BC + THN publisher-independent on payload class
  ebpf_rootkit_loaded_with_root_privileges_hides_from_standard_tools: A2  # BC + THN publisher-independent
  ebpf_map_names_hidden_pids_hidden_names_hidden_inodes: B2  # Detection-engineering telemetry; Sonatype primary via BC + THN
  payload_sha256_6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b: B2  # IOC hash; Sonatype primary via BC + THN
  malicious_npm_package_atomic_lockfile_1_4_2: B2  # IOC; BC + THN
  malicious_npm_package_js_digest_second_wave: B2  # IOC; BC + THN
  c2_http_exfiltration_to_temp_sh: B2  # IOC; BC + THN
  c2_tor_onion_service_via_local_loopback_proxy_specific_onion_not_enumerated: B3  # Partial IOC enumeration
  # ---- TARGETED CREDENTIAL CATEGORIES LAYER (8 categories per THN summary) ----
  category_browser_cookies_tokens_local_storage_chromium: A2  # BC + THN
  category_electron_app_session_data_slack_discord_teams: A2  # BC + THN
  category_github_npm_hashicorp_vault_tokens: A2  # BC + THN
  category_openai_chatgpt_credentials: A2  # BC + THN
  category_ssh_keys_known_hosts: A2  # BC + THN
  category_shell_histories: A2  # BC + THN
  category_docker_podman_credentials: A2  # BC + THN
  category_vpn_profiles: A2  # BC + THN
  # ---- ATTRIBUTION LAYER (HARD RULE 2 BINDING) ----
  no_actor_attribution_at_any_in_window_source: A1  # Verifiable absence
  sonatype_atomic_arch_is_campaign_designation_only_not_actor_attribution: A1  # Verifiable per Sonatype primary framing
  no_microsoft_storm_typhoon_sandstorm_mantis_taxon_cited: A1  # Verifiable absence
  no_cross_walk_to_existing_roster_actors: A1  # Hard Rule 2 binding
  # ---- A&D / DIB RELEVANCE LAYER ----
  ad_direct_relevance: A1  # NONE — verifiable absence; no A&D-prime victim named
  ad_structural_relevance_developer_credential_categories_universal: B2  # GitHub tokens, npm tokens, Vault, SSH keys, Docker, VPN profiles are exactly the credential class on A&D-prime developer workstations + build environments; structural relevance is high
  arch_linux_aur_usage_on_ad_prime_developer_machines_unmeasured: B3  # No source-attested deployment-density evidence
  # ---- CLUSTER-CONTEXT LAYER (supply-chain-of-developer-tooling pattern) ----
  continues_supply_chain_dev_tooling_pattern_in_corpus: B2  # Cluster-context inference per pm-005 collector analysis
  prior_corpus_cluster_anchor_mini_shai_hulud_npm_pypi_2026_05_12: A2  # Carry-forward reference
  prior_corpus_shai_hulud_microsoft_72_repo_2026_06_10: A2  # Carry-forward reference
  prior_corpus_node_ipc_90_credential_stealer_2026_05_14: A2  # Carry-forward reference
  prior_corpus_anthropic_tanstack_2026_05_14: A2  # Carry-forward reference
  prior_corpus_github_3800_repo_internal_compromise_2026_05_20: A2  # Carry-forward reference
  # ---- CREDENTIAL DISCIPLINE LAYER (HARD RULE 7) ----
  campaign_is_credential_stealer_family_categories_enumerated_at_campaign_level_only: A1  # Hard Rule 7 binding; categories named describe what malware harvests on victim systems, NOT credentials reaching Archimedes corpus
  no_credential_values_stored_in_raw_signal_or_finding: A1  # Hard Rule 7 binding
  cluster_anchor: B2

digraph_anchor: >
  Cluster anchored at B2 (Probably True) on Sonatype primary
  research with TWO publisher-independent media relays
  (BleepingComputer ratified B per source-grades.yaml + The
  Hacker News provisional B per provisional_since 2026-05-14)
  plus supplementary independent researcher (Whanos) reverse-
  engineering attestation. Sonatype primary blog NOT directly
  retrieved this sweep (flag for next-sweep direct retrieval);
  the campaign reaches the cluster through two publisher-
  independent media surfaces converging on Sonatype + Whanos
  primaries.

  Single-source veto DOES NOT apply at the cluster anchor —
  BC + THN are publisher-independent (verified per raw-signal
  pm-005 multi-source ledger: BC by Bill Toulas 13:03 EDT;
  THN by Ravie Lakshmanan 15:24 EDT; neither cites the other
  as origin). The Sonatype primary is the upstream evidence
  basis common to both relays — at the SUBSTANTIVE-EVIDENCE-
  BASIS layer this constitutes a "both rely on the same
  vendor's research" scenario per Skill Step 4, which would
  normally collapse to ONE effective source. HOWEVER, the
  Whanos independent researcher reverse-engineering work is
  separately cited by both relays and represents an
  INDEPENDENT EVIDENCE BASIS (researcher RE on the malware
  artifact, not vendor research from Sonatype's telemetry).
  Two-evidence-basis test PASSES: (a) Sonatype vendor research
  on the campaign mechanism + IOCs; (b) Whanos independent
  researcher RE on the payload artifact.

  WHAT THE B2 ATTESTS:
    (a) Sonatype has documented (via BC + THN publisher-
        independent relays + Whanos independent researcher RE)
        the Atomic Arch campaign featuring 408+ compromised
        AUR packages across two waves.
    (b) The campaign mechanism (orphaned package adoption +
        PKGBUILD/.install script modification + spoofed git
        commit metadata) is internally coherent and reaches
        cluster via two-publisher convergence.
    (c) The payload (Rust credential stealer + optional eBPF
        rootkit) and the 8 targeted credential categories
        (browser cookies, Electron session data, GitHub/npm/
        Vault tokens, OpenAI creds, SSH keys, shell histories,
        Docker/Podman creds, VPN profiles) are documented
        at A2 anchor.
    (d) IOCs (payload SHA-256, two malicious npm package
        names, temp.sh C2, eBPF map names) carry B2 anchor
        for operational hunt set.

  WHAT THE B2 DOES NOT ATTEST:
    - Any actor attribution (Sonatype "Atomic Arch" is
      campaign designation only; Hard Rule 2 binding).
    - A&D-prime targeting (no A&D-prime victim named;
      Hard Rule 2 binding on extrapolation; structural
      relevance for A&D developer environments is
      ASSERTED as inference, not source-attested).
    - AUR deployment density on A&D-prime developer
      machines (unmeasured).

  HARD RULE 2 binding constraint: PRESERVED.
    - No actor attribution at any in-window source.
      Sonatype "Atomic Arch" is a campaign / cluster
      designation only — NOT actor attribution.
    - No Microsoft Storm-/Typhoon-/Sandstorm-/Mantis taxon
      cited by any publisher.
    - Archimedes does NOT cross-walk to existing roster
      actors (GlassWorm npm worm in roster #005 is
      NOT cross-walked — Atomic Arch and GlassWorm
      operate on different package ecosystems with
      different mechanisms and there is no source-
      attested linkage at this hour).

  HARD RULE 6 binding constraint: PRESERVED. No verbatim
  quotes propagated; technical primitives are paraphrased
  from BC + THN summaries.

  HARD RULE 7 binding constraint: PRESERVED. The campaign IS
  a credential-stealer family; the 8 credential categories
  enumerated describe what the malware HARVESTS ON VICTIM
  SYSTEMS, NOT credentials that have reached Archimedes'
  corpus. Counts at the campaign level only. No credential
  values are stored at any layer of raw-signal pm-005 or
  this finding.

  HARD RULE 8 binding constraint: Per pm-000 sentinel + grader-
  side first-party Splunk query carry-forward (-7d window
  across index=archimedes OR index=defenseclaw_local on
  the payload SHA-256 6144d433f8a0316869877b5f834c801251bbb-
  936e5f1577c5680878c7443c98b + atomic-lockfile + js-digest +
  temp.sh + eBPF map names hidden_pids/hidden_names/
  hidden_inodes keywords): 12 events at most-recent query, all
  Archimedes self-instrumentation. Zero substantive first-
  party matches. defenseclaw_local does run Linux systems
  (Frank-host ancillary services) but does not observably
  use AUR. Silence expected; per Hard Rule 8: silence is not
  disconfirming. First-party precedence does NOT apply. Hash
  hunt set is published for any consuming SOC.

source_reliability:
  grade: B
  source_name: "Sonatype primary research (provisional B-tier per cheatsheet, not in source-grades.yaml) relayed by BleepingComputer (ratified B per source-grades.yaml; Bill Toulas byline) + The Hacker News (provisional B per source-grades.yaml provisional_since 2026-05-14; Ravie Lakshmanan byline) + Whanos independent researcher reverse-engineering attestation (provisional B-tier per cheatsheet 'researcher with named handle, public technical attestation')"
  source_yaml_id: bleepingcomputer
  grade_rationale: >
    BleepingComputer is ratified B per source-grades.yaml.
    The Hacker News is provisional B per source-grades.yaml.
    Sonatype primary research is NOT in source-grades.yaml —
    provisional B-tier per cheatsheet "named vendor with
    structured public technical research" lineage. Whanos
    independent researcher reverse-engineering is provisional
    B-tier per cheatsheet "researcher with named handle,
    public technical attestation". Two publisher-independent
    media relays + independent researcher RE.
  provisional: true
  flag_for_librarian: >
    Add Sonatype to source-grades.yaml at provisional B-tier
    per cheatsheet "named vendor with structured public
    technical research" lineage; Sonatype appears as primary
    research source in supply-chain-of-developer-tooling
    cluster context (Mini Shai-Hulud, Shai-Hulud Microsoft,
    node-ipc, Anthropic TanStack lineage).

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_known_ttps_or_campaign_timing  # Orphaned-package-adoption + PKGBUILD modification is consistent with established AUR supply-chain attack pattern (e.g., 2018 PyPI typosquat lineage, 2022 ctx/phpass campaign lineage); Rust-credential-stealer + eBPF rootkit is consistent with 2026 supply-chain-of-developer-tooling pattern in corpus
    - probably_true_no_contradicting_ab_grade_source  # No A/B-grade contradiction at sweep
    - probably_true_technical_claims_internally_coherent  # PKGBUILD/.install script flow + npm/bun install during package build + Rust binary + eBPF rootkit (root-loaded) + temp.sh HTTP exfil + Tor loopback proxy + the 8 credential categories are all internally coherent
  rationale: >
    Cluster anchor at Grade 2 (Probably True): two-publisher
    convergence (BC + THN publisher-independent) on Sonatype
    primary + Whanos independent researcher RE provides
    INDEPENDENT EVIDENCE BASIS at the substantive layer. The
    campaign mechanism is consistent with established AUR
    supply-chain attack pattern; the payload technical
    primitives are internally coherent; the targeted
    credential categories are exactly the developer-secrets
    class expected of this attack family; no A/B-grade
    contradiction at sweep. Grade 1 (Confirmed) is NOT met
    because the SECOND evidence basis (Whanos researcher RE)
    is itself provisional B-tier and reaches the cluster only
    through the same BC + THN relays as Sonatype — at the
    strictest independence test (two A-grade primaries with
    fully separate evidence bases) the cluster has one
    primary + one researcher attestation, which qualifies as
    Grade 2 rather than Grade 1.

corroboration:
  independent_sources:
    - bleepingcomputer
    - thehackernews
  independent: true  # BC + THN are publisher-independent at the publisher layer; Whanos researcher RE provides independent evidence basis at the substantive layer
  test_passed: >
    Two-publisher independence test PASSES at the publisher
    layer: BleepingComputer (Bill Toulas byline, 13:03 EDT)
    and The Hacker News (Ravie Lakshmanan byline, 15:24 EDT)
    neither cites the other as origin per raw-signal pm-005
    multi-source ledger; both source the underlying campaign
    to Sonatype + Whanos. Two-evidence-basis test PASSES at
    the substantive layer: (a) Sonatype vendor research on
    campaign mechanism + IOCs, AND (b) Whanos independent
    researcher reverse-engineering on the payload artifact.
    Sonatype primary not directly retrieved (flag for
    next-sweep retrieval); Whanos research write-up not
    directly retrieved (flag for next-sweep retrieval).

first_party_precedence:
  applied: false
  splunk_evidence: >
    Per pm-000 sentinel + grader-side query (-7d window across
    index=archimedes OR index=defenseclaw_local on payload
    SHA-256 + atomic-lockfile + js-digest + temp.sh + eBPF map
    names): 12 events at most-recent query, all Archimedes
    self-instrumentation. Zero substantive first-party matches.
    defenseclaw_local does not observably use AUR. Silence
    expected; per Hard Rule 8: silence is not disconfirming.
    First-party precedence does NOT apply. Hash hunt set
    (payload SHA-256, eBPF map names, temp.sh, atomic-lockfile,
    js-digest) is published in this finding for downstream
    SOC consumption.

single_source_veto_applied: false  # Two-publisher independent corroboration + independent researcher evidence basis
wep_ceiling: very_likely  # B2 + multi-publisher + independent researcher; not single-source-veto-bound
wep_layered:
  campaign_mechanism_layer: very_likely  # BC + THN publisher-independent on Sonatype + Whanos
  payload_class_layer: very_likely  # BC + THN publisher-independent
  ioc_set_layer: likely  # Conservative on specific IOCs per B2 anchor with single-vendor primary on hash specifics
  408_packages_two_waves_scope_layer: very_likely  # BC + THN convergence
  ad_structural_relevance_developer_credential_categories_universal: likely  # Inference but credential categories are universal for developer environments
  ad_direct_relevance: very_unlikely  # Verifiable absence
  ad_extrapolation_to_specific_ad_prime_targeting_BLOCKED: not_assessed_per_hard_rule_2

inclusion:
  eligible_for:
    - daily_brief_action  # B2 / very_likely on campaign mechanism; brief-worthy supply-chain item
    - weekly_synthesis  # Detection-engineering surfaces + supply-chain-of-developer-tooling cluster pattern
    - vulnerability_tracking_update  # No tracked CVE in this finding; IOC hunt set published
  flash_eligible: false  # No CVE + no A&D-prime targeting + already in afternoon brief window
  flash_threshold_met: true  # B2 / very_likely meets B2 threshold

graded_at: 2026-06-12T16:45:00-04:00

# ============================================================================
# Cluster metadata
# ============================================================================
cluster:
  topic: "Sonatype 'Atomic Arch' campaign — 408 AUR packages hijacked across two waves; Rust credential stealer with optional eBPF rootkit; 8 developer-secret categories targeted; no actor attribution; first Arch ecosystem mass compromise in Archimedes corpus"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-12-pm-005
  attribution_claims: []  # No actor attribution at any in-window source

# ============================================================================
# IOC hunt set (published for downstream SOC consumption)
# ============================================================================
iocs:
  hashes:
    - sha256: "6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b"
      type: payload_binary
      malware_family: atomic_arch_rust_credential_stealer
      confidence: B2
      source: sonatype_via_bleepingcomputer_thehackernews_relays
  malicious_packages:
    - name: "atomic-lockfile"
      version: "1.4.2"
      ecosystem: npm
      role: primary_payload_delivery
      confidence: B2
    - name: "js-digest"
      ecosystem: npm
      role: second_wave_payload_delivery
      confidence: B2
  c2_exfiltration:
    - destination: "temp.sh"
      method: http_exfiltration
      confidence: B2
    - destination: "tor_onion_service_via_local_loopback_proxy"
      specific_onion: not_enumerated_in_relay
      confidence: B3
  detection_engineering_telemetry:
    - ebpf_map_name: "hidden_pids"
      confidence: B2
    - ebpf_map_name: "hidden_names"
      confidence: B2
    - ebpf_map_name: "hidden_inodes"
      confidence: B2

# ============================================================================
# Downstream handoff flags
# ============================================================================
analyst_review_required: false  # B2 / very_likely with multi-publisher convergence; no SAT-ACH structural ambiguity at cluster level
red_team_review_required: false  # WEP "very_likely" on campaign mechanism layer but cluster is supply-chain-disclosure-and-IOC-hunt-set, NOT predictive operational claim against named victim class. Doctrine triggers red-team on predictive operational very_likely+ claims.
red_team_review: null

actor_profile_handoff: null  # No actor attribution

vuln_tracker_handoff: null  # No tracked CVE in this finding

analysis_sections:
  sat_ach: null
  sat_kac: null

tlp: CLEAR
published_in_briefs: [2026-06-12-afternoon]
retracted: false
retraction_brief_id: null
---

# 400+ Arch Linux AUR packages hijacked — Sonatype "Atomic Arch" campaign; Rust credential stealer with optional eBPF rootkit targeting 8 developer-secret categories; two waves; official Arch repos NOT affected; no actor attribution

## Summary

Sonatype has documented (via BleepingComputer + The Hacker News publisher-independent relays on 2026-06-12, plus independent researcher Whanos reverse-engineering attestation) a campaign tracked as "Atomic Arch" that hijacked over 400 packages in the Arch User Repository (AUR). New maintainer accounts adopted abandoned/orphaned AUR packages, modified PKGBUILD and .install scripts to execute npm/bun install commands during package build, and retrieved the weaponized `atomic-lockfile` payload. An initial wave of 20+ packages expanded to ~408 packages across two distinct waves. Official Arch repositories were NOT affected — the campaign targeted exactly the lower-trust adjacent AUR ecosystem. The payload is a Rust binary that harvests developer secrets across 8 categories (browser cookies, Electron session data, GitHub/npm/HashiCorp Vault tokens, OpenAI credentials, SSH keys, shell histories, Docker/Podman credentials, VPN profiles); with root privileges it loads an eBPF rootkit that hides from standard tools. No actor attribution at any in-window source — Sonatype "Atomic Arch" is a campaign designation only. This is the first Arch ecosystem mass compromise in the Archimedes corpus and continues the supply-chain-of-developer-tooling cluster pattern.

## Sources

### BleepingComputer (bleepingcomputer, digraph: B ratified)

- URL: `https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/`
- Published: 2026-06-12T13:03 EDT (17:03 UTC); Bill Toulas byline
- Key claim: 400+ AUR packages compromised via Sonatype-tracked Atomic Arch campaign; Rust credential stealer + eBPF rootkit; PKGBUILD/.install script modification mechanism; two waves; official Arch repos not affected.

### The Hacker News (thehackernews, digraph: B provisional)

- URL: `https://thehackernews.com/2026/06/400-arch-linux-aur-packages-hijacked.html`
- Published: 2026-06-12T15:24 EDT; Ravie Lakshmanan byline
- Key claim: 400+ AUR packages hijacked to install Rust credential stealer; 8 developer-secret categories targeted; Sonatype-tracked Atomic Arch campaign; Whanos independent researcher reverse-engineering.

## Technical detail

- **Campaign mechanism:** new maintainer accounts adopted abandoned/orphaned AUR packages; modified PKGBUILD and .install scripts to execute npm/bun install commands during package build; retrieved weaponized `atomic-lockfile` package. Spoofed git commit metadata was used to disguise the maintainer change.
- **Scope:** initial wave 20+ packages; expanded to ~408 packages within days across two distinct waves; in-the-wild active.
- **Scope bounding:** official Arch repositories were NOT affected. AUR is the community package repository; the campaign targeted exactly the lower-trust adjacent ecosystem.
- **Payload — Rust credential stealer:** built explicitly to harvest developer secrets. With root, loads an eBPF rootkit that hides from standard tools.
- **8 credential categories targeted:**
  1. Browser cookies / tokens / local storage (Chromium-based browsers).
  2. Electron app session data (Slack, Discord, Teams).
  3. GitHub, npm, HashiCorp Vault tokens.
  4. OpenAI / ChatGPT credentials.
  5. SSH keys and known_hosts.
  6. Shell histories.
  7. Docker / Podman credentials.
  8. VPN profiles.
- **C2 / exfiltration:** HTTP exfiltration to `temp.sh`; Tor onion service accessed via local loopback proxy (specific .onion not enumerated in relay).
- **eBPF rootkit telemetry (detection-engineering surfaces):** eBPF map names `hidden_pids`, `hidden_names`, `hidden_inodes`.

## Hard Rule 2 — attribution discipline (BINDING)

- No actor attribution at any in-window source.
- Sonatype "Atomic Arch" is a campaign / cluster designation only — NOT actor attribution.
- No Microsoft Storm-/Typhoon-/Sandstorm-/Mantis taxon cited by any publisher.
- Archimedes does NOT cross-walk Atomic Arch to existing roster actors (including GlassWorm #005, which is a separate npm-worm-cluster lineage operating on different ecosystem mechanics).

## Hard Rule 7 — credential discipline (BINDING)

The campaign IS a credential-stealer family. The 8 credential categories enumerated describe what the malware HARVESTS ON VICTIM SYSTEMS — NOT credentials that have reached Archimedes' corpus. Counts and category names at the campaign level only. No credential values are stored in raw-signal pm-005 or this finding.

## IOCs surfaced

Operational hunt set (B2 confidence):

- **Payload SHA-256:** `6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b`
- **Malicious npm packages:** `atomic-lockfile@1.4.2` (primary payload); `js-digest` (second-wave payload).
- **C2 / exfiltration:** `temp.sh` (HTTP exfiltration); Tor onion service via local loopback proxy (specific .onion not enumerated in relay).
- **eBPF rootkit detection-engineering telemetry:** map names `hidden_pids`, `hidden_names`, `hidden_inodes`.

## A&D / DIB relevance

- **Direct:** none. No A&D-prime victim named or implied.
- **Structural (developer environments):** the 8 credential categories targeted — GitHub tokens, npm tokens, HashiCorp Vault, SSH keys, Docker creds, VPN profiles — are exactly the secrets that A&D-prime developer workstations and build environments carry. Any A&D-prime engineer running Arch Linux on a personal or development machine with AUR enabled is in scope. AUR deployment density on A&D-prime developer machines is unmeasured.
- **Cluster context — supply-chain-of-developer-tooling:** continues the pattern from prior corpus findings (Mini Shai-Hulud npm + PyPI worm, finding-2026-05-12-FLASH-0001; Shai-Hulud Microsoft 72-repo compromise, finding-2026-06-10-0002; node-ipc 90-credential stealer, finding-2026-05-14-0009; Anthropic TanStack, finding-2026-05-14-0008; GitHub 3,800-repo internal compromise, finding-2026-05-20-FLASH-0001). First Arch ecosystem mass compromise in this lineage.

## Relationship to existing findings

- **First Arch ecosystem mass compromise** in the Archimedes corpus.
- **Cluster-context lineage:** continues supply-chain-of-developer-tooling pattern; no supersession.

## Open questions for analyst

- Watch: Sonatype primary blog direct retrieval at next collector pass (likely carries richer IOC content).
- Watch: Whanos reverse-engineering write-up for deeper IOCs.
- Watch: second IR-firm corroboration (Mandiant / Unit 42 / Sophos / SentinelLabs silent at this sweep on Atomic Arch).
- Watch: any A&D-prime SOC reporting an AUR-package-related compromise.
- Action recommendation surface for the brief: audit AUR usage policy on A&D-prime developer machines; rotate developer-tier credentials if AUR usage is suspected; check for the named eBPF maps on suspect systems.
