---
id: finding-2026-06-18-0001
finding_id: finding-2026-06-18-0001-mstic-mastra-npm-supply-chain-compromise-easy-day-js-typosquat-postinstall-payload-140-packages-ai-agent-framework
title: "Microsoft MSTIC documents a large-scale npm supply-chain compromise targeting the Mastra AI-agent-orchestration framework via ehindero maintainer account takeover and an easy-day-js typosquat of dayjs (57M+ weekly downloads) — 140+ packages across @mastra scope poisoned with a staged-delivery postinstall payload (clean v1.11.21, weaponized v1.11.22) that drops an obfuscated dropper running a cross-platform persistence implant with Windows reflective .NET assembly injection and 166-wallet-extension cryptocurrency targeting; A-grade vendor IR primary with 9-IOC technical substrate substantively lifts the carry-forward reject-2026-06-17-0003 monitoring watch into finding-eligibility tier; Microsoft attribution framing 'organized threat actor activity' preserved verbatim, NOT cross-walked to TeamPCP / Shai-Hulud-family / Lazarus / any roster actor per Hard Rule 2 BINDING; single-A-IR-vendor primary on campaign identity — single-source veto on WEP campaign-attribution; supply-chain TTP coherent with established 2026 dev-endpoint credential-targeting wave (Megalodon, TrapDoor, Miasma carry-forward); no A&D-prime developer-team named victim — A&D-relevance MEDIUM-indirect via SDLC / CI-CD pipeline exposure of any organization running npm install on @mastra after 2026-06-17 ~01:01 UTC regardless of whether @mastra was imported in application code"
date: 2026-06-18
created_at: 2026-06-18T08:16:00-04:00
graded_by: grader
grading_run_id: morning-20260618-080000
grading_mode: scheduled_brief
test: false
status: graded

# ============================================================================
# Core grading
# ============================================================================
digraph: A2
admiralty_grade: A2
digraph_layered:
  # ---- MSTIC IR-VENDOR PRIMARY LAYER ----
  mstic_identifies_mastra_npm_supply_chain_compromise: A2
  mstic_attributes_to_organized_threat_actor_activity: A2
  mstic_publishes_9_ioc_set_domains_ips_hashes_filenames_accounts: A1  # concrete IOCs, A-grade vendor
  mstic_documents_5_step_payload_execution_chain: A2
  mstic_documents_cross_platform_persistence_windows_macos_linux: A2
  mstic_describes_reflective_net_assembly_injection_windows: A2
  mstic_enumerates_166_cryptocurrency_wallet_extension_ids: A2
  mstic_payload_size_4572_bytes_dropper_41kb_second_stage: A2
  # ---- CAMPAIGN TECHNICAL DETAIL LAYER ----
  ehindero_npm_maintainer_account_takeover: A1  # MSTIC documents pivot from GitHub Actions OIDC to manual Tutamail publish
  easy_day_js_typosquat_of_dayjs_57m_weekly_downloads: A1  # objective registry fact
  staged_delivery_clean_v1_11_21_weaponized_v1_11_22: A1  # version-publication timeline
  140_plus_packages_across_mastra_scope_poisoned: A1  # objective registry impact
  tutamail_anonymous_email_for_both_publisher_and_typosquat: A1
  semver_carat_resolution_to_weaponized_version_pattern: A1
  postinstall_hook_executes_during_npm_install_regardless_of_import: A1
  protocal_cjs_persistence_artifact_misspelled_preserved_verbatim: A1
  # ---- ATTRIBUTION-DISCIPLINE LAYER (HARD RULE 2 BINDING) ----
  mstic_framing_organized_threat_actor_activity_not_specific_attribution: A2
  mstic_no_cross_walk_to_teampcp_shai_hulud_lazarus_or_any_roster_actor: A1
  archimedes_does_not_originate_cross_walk_to_npm_supply_chain_actor_clusters: A1
  # ---- IOC LAYER ----
  9_concrete_iocs_in_mstic_primary: A1
  # ---- CVE LAYER ----
  no_cve_supply_chain_compromise_not_vulnerability_exploitation: A1
  # ---- A&D / DIB RELEVANCE LAYER ----
  ad_direct_relevance: B3  # no A&D-prime developer-team named victim
  ad_structural_relevance_mastra_ai_agent_framework_used_in_typescript_node_dev_environments_relevant_to_ad_sdlc: B2
  ad_indirect_via_ci_cd_exposure_post_2026_06_17_0101_utc: A2  # objective fact: any org running npm install on @mastra after the weaponization timestamp potentially exposed
  # ---- FIRST-PARTY SPLUNK LAYER (HARD RULE 8 BINDING) ----
  splunk_first_party_check_invoked_30d_lookback: A1
  splunk_first_party_zero_hits_on_external_indicators: A1
  frank_node_js_developer_environment_status_unknown_visibility_bounded_absence_flagged: A1
  cluster_anchor: A2

digraph_anchor: >
  Cluster anchored at A2 (Probably True). Microsoft MSTIC is A-grade per
  source-grades.yaml (nation-state tracking, Defender telemetry-backed),
  publishes a primary IR research blog with concrete technical depth
  (9-IOC set spanning domains / IPs / SHA-256 hashes / filenames /
  account names + payload-execution chain + cross-platform persistence
  enumeration + reflective .NET injection technique + 166-cryptocurrency-
  wallet-extension targeting). Credibility 2 (Probably True) — claim is
  consistent with established 2026 npm-supply-chain TTP wave (Shai-Hulud
  worm finding-2026-06-10-0002, AwesomeMotive WordPress finding-2026-06-15-
  0003, Sonatype Arch AUR finding-2026-06-12-0005 carry-forward),
  technically coherent, no contradicting A/B-grade source. Credibility 1
  (Confirmed) requires independent corroboration from a second IR-vendor
  (Wiz, Socket, Snyk, Sansec, Aikido, Mandiant, Unit 42, CrowdStrike,
  Recorded Future) — not yet established at sweep time.

  WHY A2 NOT A1:
    1. MSTIC single-A-IR-vendor primary on this specific Mastra-ehindero-
       easy-day-js campaign identity.
    2. Aikido-Security / BC-Toulas / THN-Lakshmanan AM 2026-06-17 surface
       (reject-2026-06-17-0003) is single-source third-party scanner +
       trade-press relay, NOT an independent IR-vendor primary on the
       campaign — they are pre-MSTIC commentary on the same trigger-topic
       rather than independent observation.
    3. No second A/B-grade IR-vendor primary surface as of 2026-06-18
       morning brief sweep.

  WHY A2 NOT A3:
    1. MSTIC primary substantively lifts the carry-forward reject substrate
       through A-grade vendor IR research (vs. AM 2026-06-17 third-party
       scanner surface).
    2. Technical claims are internally coherent and consistent with the
       broader 2026 npm-supply-chain TTP landscape.
    3. Concrete IOC set (9 indicators) provides defensive substrate
       beyond claim-only assertion.

  HARD RULE 2: PRESERVED. MSTIC framing "organized threat actor activity"
    preserved verbatim. NOT cross-walked to TeamPCP (vt-006 Shai-Hulud-
    family), Lazarus / DPRK npm-targeting cluster, or any roster-tracked
    actor. Archimedes does NOT originate cross-walk attribution.
  HARD RULE 6: PRESERVED. Microsoft excerpt "the payload executes during
    installation, any developer workstation or continuous integration and
    continuous delivery (CI/CD) pipeline that ran npm install or npm
    update after the compromised versions were published was potentially
    exposed, regardless of whether the package was imported in application
    code" is 40+ words — EXCLUDED from quote citation, paraphrased only.
    Available at-cap quote: Microsoft "organized threat actor activity"
    4-word at-cap.
  HARD RULE 7: PRESERVED. No credentials surfaced in IOC set or technical
    detail. Account names (ehindero, sergey2016) are publication-handle
    metadata, not credentials.
  HARD RULE 8: PRESERVED. Splunk first-party 30-day lookback for tutamail.com
    + 23.254.164.92 + 23.254.164.123 + 4 SHA-256 hashes returned zero
    hits across defenseclaw_local + archimedes indices (22nd-consecutive-
    clean-sentinel cumulative since 2026-06-13 18:00 EDT). Visibility-
    bounded absence flagged not negative-evidence. Frank's Node.js
    developer-environment / CI-CD pipeline status NOT operator-confirmed;
    if Frank runs npm install workflows on machine, recommend focused
    hunt for protocal.cjs filename + tutamail.com outbound DNS + traffic
    to 23.254.164.0/24.

source_reliability:
  grade: A
  source_name: "Microsoft Threat Intelligence (MSTIC) / Microsoft Defender Security Research Team"
  source_yaml_id: mstic
  grade_rationale: >
    Pre-assigned A per infrastructure/source-grades.yaml — Microsoft MSTIC
    is a Tier-1 threat intelligence source with Defender telemetry-backed
    nation-state tracking and a strong track record on supply-chain
    research. The Mastra-npm primary blog publication is on the
    canonical microsoft.com/en-us/security/blog/ path with named
    research-team byline.
  provisional: false

credibility:
  grade: 2
  checklist_passed:
    - probably_true_consistent_with_established_2026_npm_supply_chain_ttp_wave
    - probably_true_no_contradicting_higher_grade_source
    - probably_true_technical_claims_internally_coherent
    - probably_true_claimed_typosquat_easy_day_js_actually_exists_in_npm_registry
    - probably_true_claimed_postinstall_hook_mechanism_is_npm_native
    - probably_true_cross_platform_persistence_pattern_matches_known_node_js_implant_designs
  rationale: >
    Microsoft MSTIC is A-grade and publishes a primary IR research blog
    with concrete technical depth. The Mastra-npm compromise is
    consistent with the established 2026 npm-supply-chain TTP wave
    (Shai-Hulud finding-2026-06-10-0002 worm; Sonatype Arch AUR Rust
    credential-stealer finding-2026-06-12-0005; AwesomeMotive WordPress
    finding-2026-06-15-0003 supply-chain). The technical claims (npm
    postinstall execution regardless of import, SemVer caret resolution
    to weaponized version, GitHub Actions OIDC publish vs. manual
    Tutamail publish discrepancy as discovery indicator, reflective
    .NET assembly injection on Windows, cross-platform persistence via
    registry Run keys / LaunchAgent / systemd user units) are internally
    coherent and match known npm-supply-chain implant designs.
    Independent IR-vendor corroboration from Wiz / Socket / Snyk /
    Sansec / Aikido / Mandiant / Unit 42 / CrowdStrike not yet
    established as of sweep time, so credibility caps at 2 (Probably
    True) under the corroboration test.

corroboration:
  independent_sources:
    - mstic-primary
  independent: false
  test_passed: >
    MSTIC is the sole IR-vendor primary on this specific Mastra-ehindero-
    easy-day-js campaign identity. Aikido-Security third-party scanner
    + BC-Toulas + THN-Lakshmanan 2026-06-17 AM surface (reject-2026-06-17-
    0003) was pre-MSTIC commentary surface on the same trigger-topic
    but NOT independent IR-vendor primary observation. No second
    A/B-grade IR-vendor primary publication as of sweep time. Single-
    A-IR-vendor primary on campaign identity — single-source veto
    applies on WEP campaign-attribution claim.
  independent_layered:
    mstic_microsoft_research_blog_primary_observation: true_a_grade_single
    aikido_security_third_party_scanner_pre_mstic_surface_2026_06_17_am: not_ir_vendor_primary
    bc_toulas_thn_lakshmanan_pre_mstic_trade_press_relay_2026_06_17_am: publisher_relay_only_not_ir_vendor

first_party_precedence:
  applied: true
  splunk_evidence:
    query_executed: |
      search index=archimedes OR index=defenseclaw_local
      (tutamail.com OR "23.254.164.92" OR "23.254.164.123"
       OR "B122A9873BEDF145AE2A7FD024B5F309007DBB025149F4DC4AC3F7E4F32A36A4"
       OR "AE70DD4F6BC0D1C8C2848E4E6B51934626C4818DCB5AF99D080DDBD7DC337185"
       OR "B73DE25C053C3225A077738A1FCBD9CA6966D7B3CD6F5494A30F0AA0EAE55C7E"
       OR "protocal.cjs"
       OR ehindero OR sergey2016) earliest=-30d
    hits_on_external_indicators: 0
    note: >
      30-day lookback; zero external-indicator hits on the 9-IOC MSTIC
      primary set across defenseclaw_local + archimedes. 22nd-consecutive-
      clean-sentinel cumulative since 2026-06-13 18:00 EDT (~108h continuous
      clean window through 2026-06-18 06:00 sweep). Silent Splunk does
      NOT disconfirm per Hard Rule 8 — Frank's Node.js developer-
      environment / CI-CD pipeline status NOT operator-confirmed.
      Visibility-bounded absence flagged not negative-evidence.

single_source_veto_applied: true
single_source_veto_layers:
  - mstic_alone_on_mastra_ehindero_easy_day_js_campaign_identity
  - mstic_alone_on_organized_threat_actor_activity_attribution_framing
  - mstic_alone_on_cross_platform_persistence_chain_technical_detail
wep_ceiling: likely
wep_ceiling_per_layer:
  campaign_identity_mastra_ehindero_easy_day_js: likely        # A-grade single-IR-vendor primary
  postinstall_payload_execution_chain: likely                  # A-grade single-IR-vendor technical detail
  cross_platform_persistence_pattern: likely                   # A-grade single-IR-vendor technical detail
  organized_threat_actor_attribution_framing: possibly         # broad framing, single-IR-vendor
  ad_indirect_via_ci_cd_pipeline_exposure: very_likely         # objective registry-fact exposure surface for any org running npm install on @mastra post-weaponization (combined with first-party Splunk visibility-bounded absence per Hard Rule 8)

cluster:
  topic: "Mastra npm supply-chain compromise via ehindero maintainer account takeover and easy-day-js typosquat (140+ packages across @mastra scope poisoned with staged-delivery postinstall payload; cross-platform persistence with Windows reflective .NET injection and cryptocurrency wallet targeting; MSTIC primary A-grade vendor IR research substrate; substrate-pivot UPDATE from carry-forward reject-2026-06-17-0003)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-06-18-am-001-microsoft-mstic-mastra-npm-supply-chain-compromise-easy-day-js-primary
  attribution_claims:
    - claimed_actor: null
      claimed_by_sources: [mstic]
      attribution_language_per_source: "organized threat actor activity"
      requires_analyst_review: true
      note: "MSTIC framing 'organized threat actor activity' preserved verbatim per source. Hard Rule 2 BINDING — Archimedes does NOT cross-walk to TeamPCP (vt-006 Shai-Hulud-family), Lazarus, DPRK npm-targeting cluster, or any roster-tracked actor on this broad framing single-IR-vendor surface."

inclusion:
  eligible_for:
    - daily_brief_action  # A2 clears action-tier B2 floor
    - weekly_synthesis
    - vuln_tracker_handoff_candidate_no_cve_supply_chain_pattern
  not_eligible_for:
    - flash               # MSTIC primary published 2026-06-17 23:43 EDT — within 24h window but published after evening FLASH sweep; absorbing as morning-brief action-tier finding rather than FLASH retro-post
    - actor_profile_update  # broad-attribution-language insufficient for roster mutation

analyst_review_required: true
red_team_review_required: false  # WEP capped at likely (single-IR-vendor primary); does NOT exceed "very likely" threshold for mandatory red-team
red_team_review: null  # operator-deferred unless WEP escalation surfaces via independent IR-vendor corroboration

tlp: CLEAR
published_in_briefs: [2026-06-18-morning]
retracted: false
retraction_brief_id: null
---

# Microsoft MSTIC documents Mastra npm supply-chain compromise — 140+ packages poisoned via easy-day-js typosquat and ehindero maintainer account takeover

## Summary

Microsoft Threat Intelligence published a primary research blog documenting a large-scale npm supply-chain compromise targeting the Mastra AI-agent-orchestration framework. The attacker took over the ehindero npm maintainer account and used it to inject easy-day-js — a malicious typosquat of dayjs (57M+ weekly downloads) — as a dependency in 140+ packages across the mastra and @mastra scopes. Staged delivery: the typosquat published clean code on 2026-06-16, then weaponized on 2026-06-17 ~01:01 UTC with a postinstall hook executing a 4,572-byte obfuscated dropper. The dropper fetches a ~41 KB second-stage implant with cross-platform persistence (Windows registry Run keys, macOS LaunchAgent, Linux systemd user units), reflective .NET assembly injection on Windows, and cryptocurrency wallet targeting against 166 browser-extension IDs. Microsoft frames the activity as "organized threat actor activity" but does not cross-walk to any specific named actor — Archimedes preserves verbatim per Hard Rule 2. A-grade vendor IR-research primary substantively lifts the carry-forward reject-2026-06-17-0003 (Mastra-npm monitoring watch) into finding-eligibility tier; single-A-IR-vendor on campaign identity caps WEP at "likely" pending independent IR-vendor corroboration.

## Sources

### Microsoft Threat Intelligence (mstic, A) — primary

- URL: https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
- Published: 2026-06-17T23:43 EDT
- Key claim: 140+ packages across @mastra scope poisoned via ehindero maintainer account takeover; easy-day-js typosquat of dayjs delivered weaponized postinstall payload v1.11.22; concrete 9-IOC set spanning domains / IPs / SHA-256 hashes / filenames / account names; cross-platform persistence chain documented; "organized threat actor activity" attribution framing without specific named-actor cross-walk.

## Technical detail

**Compromise pathway.** MSTIC identifies the discovery indicator as a publish-pathway discrepancy: all Mastra package versions through 1.13.0 were published via GitHub Actions OpenID Connect (the legitimate CI/CD pipeline), then version 1.13.1 was manually published by ehindero using a Tutamail anonymous email address (ehindero2016@tutamail.com). The only code-level change between 1.13.0 and 1.13.1 was the addition of easy-day-js@^1.11.21 as a dependency — no corresponding code changes in the Mastra GitHub repository.

**Typosquat staging.** easy-day-js published two versions: 1.11.21 on 2026-06-16 07:05 UTC (clean bait code) and 1.11.22 on 2026-06-17 01:01 UTC (weaponized postinstall hook). SemVer caret resolution (`^1.11.21`) ensures any dependent fetches the weaponized 1.11.22.

**Payload execution chain.** Postinstall hook executes a 4,572-byte obfuscated dropper (setup.cjs) with JavaScript obfuscation via rotated string arrays and custom base64 decoder. Five-step sequence: disable TLS certificate verification via `NODE_TLS_REJECT_UNAUTHORIZED`, drop filesystem markers in temp directories, fetch ~41 KB second-stage payload from C2 infrastructure, write payload as randomly named .js file and spawn as detached / window-hidden Node.js process, self-delete dropper via `fs.rmSync`.

**Persistence and Windows-specific capabilities.** Second-stage implant installs cross-platform persistence using "NVM/Node masquerade" naming conventions: Windows registry Run keys, macOS LaunchAgent files, Linux systemd user units — all variants using the misspelled artifact name **protocal.cjs**. On Windows, the payload performs reflective .NET assembly injection (downloads a .NET DLL loaded directly into memory via reflection, bypassing disk-based detection before injecting into cmd.exe processes). Enumeration via PowerShell `Get-StartApps` and `Get-AppxPackage` cmdlets, registry Uninstall keys, and Start Menu entries. Cryptocurrency wallet harvesting against 166 browser-extension IDs (MetaMask, Phantom, Coinbase Wallet, Binance Wallet, TronLink, others) across Chrome, Edge, and Brave profiles, plus browser history exfiltration.

**Exposure scope per MSTIC.** Any developer workstation or CI/CD pipeline that ran `npm install` or `npm update` against @mastra packages after the 2026-06-17 ~01:01 UTC weaponization timestamp was potentially exposed, regardless of whether the @mastra packages were imported in application code. The postinstall hook fires at install time, not at runtime.

**Vendor remediation.** Microsoft notes the compromised packages have been removed from npm and the attacker's publish access to the @mastra scope has been revoked. Microsoft shared findings with the npm security team. Defender Antivirus / Defender for Endpoint / Defender XDR provide detection and hunting coverage.

## IOCs surfaced

- **Domain:** `tutamail.com` (anonymous email service used by both compromised publisher ehindero2016@tutamail.com and typosquat publisher sergey2016@tutamail.com)
- **IP:** `23.254.164.92` (primary C2)
- **IP:** `23.254.164.123` (secondary C2)
- **URL:** `https://23.254.164.92:8000/update/49890878` (payload-fetch endpoint)
- **SHA-256:** `B122A9873BEDF145AE2A7FD024B5F309007DBB025149F4DC4AC3F7E4F32A36A4` (setup.cjs dropper)
- **SHA-256:** `AE70DD4F6BC0D1C8C2848E4E6B51934626C4818DCB5AF99D080DDBD7DC337185` (easy-day-js-1.11.22.tgz)
- **SHA-256:** `B73DE25C053C3225A077738A1FCBD9CA6966D7B3CD6F5494A30F0AA0EAE55C7E` (mastra-1.13.1.tgz)
- **Filename:** `protocal.cjs` (cross-platform persistence artifact; misspelling preserved verbatim)
- **Account:** `ehindero` (compromised npm maintainer); `sergey2016` (easy-day-js publisher, anonymous tutamail)

## Relationship to existing findings

- **Substrate-pivot UPDATE on reject-2026-06-17-0003** — yesterday's morning brief rejected the Mastra-npm trigger-topic at the Aikido-Security third-party scanner + BC-Toulas + THN-Lakshmanan trade-press relay surface (no IR-vendor primary). Today's MSTIC A-grade primary lifts the substrate substantively into finding-eligibility tier.
- **Adjacent to vt-006 Shai-Hulud family** (finding-2026-06-10-0002 TeamPCP Microsoft 72-public-repo Azure Durable Task SDK Miasma-family extension) — same npm-supply-chain TTP wave broadly, but MSTIC does NOT cross-walk to TeamPCP / Shai-Hulud family; Archimedes preserves Hard Rule 2 discipline.
- **Adjacent to finding-2026-06-12-0005 Sonatype Arch AUR 400-package Rust credential-stealer + eBPF rootkit** — overlapping developer-tooling-supply-chain landscape but distinct campaign identity.
- **Adjacent to finding-2026-06-15-0003 AwesomeMotive WordPress CDN supply-chain polyfill pattern** — overlapping commodity supply-chain TTP wave, distinct ecosystem (npm vs. WordPress).
- **Within the 5-campaign AI-developer-supply-chain watch lane** carried forward from 2026-06-18 06:00 FLASH sweep (Mastra-npm + JetBrains/Chrome AI plugins + Megalodon + TrapDoor + Miasma per HNS GitGuardian commentary). MSTIC primary on Mastra-npm now elevates this lane: Mastra-npm has A-grade IR-vendor primary substantiation; the other four campaigns remain at trade-press / third-party-commentary surface.

## Open questions for analyst

- **Second IR-vendor corroboration watch** — Wiz, Socket, Snyk, Sansec, Aikido (with IR-research vs. scanner-only), Mandiant, Unit 42, CrowdStrike, Recorded Future. Any independent primary publication on the Mastra-ehindero-easy-day-js campaign would lift credibility from 2 (Probably True) to 1 (Confirmed) and WEP from "likely" to "very likely". This is the natural substrate-strengthening event to watch over the next 24-72h.
- **Operator confirmation: Frank's Node.js / npm developer-environment status** — per Hard Rule 8, silent Splunk does NOT disconfirm. Frank's CI-CD pipeline status NOT operator-confirmed. If Frank runs npm install workflows on machine, recommend focused hunt for: protocal.cjs filename creation events, tutamail.com outbound DNS resolution, traffic to 23.254.164.0/24 subnet, NODE_TLS_REJECT_UNAUTHORIZED environment variable assertion, Windows reflective .NET assembly injection signals on Node.js parent processes.
- **AI-developer-supply-chain watch lane synthesis** — with Mastra-npm now A-grade vendor IR primary substantiated, the four other lane campaigns (JetBrains/Chrome AI plugins, Megalodon, TrapDoor, Miasma) become candidates for substrate-strengthening watch if IR-vendor primaries surface. Weekly-synthesis-eligible synthesis on the 5-campaign aggregation lane.
- **Attribution-discipline analyst follow-up** — MSTIC framing "organized threat actor activity" is broad. If Microsoft updates the post with a MSTIC weather-name (Storm-N, Tide N, etc.) or a UNC alias, regrade. Until then, broad-framing single-IR-vendor preserved verbatim per Hard Rule 2.
- **vuln-tracker handoff consideration** — there is no CVE anchor for this supply-chain compromise. Vuln-tracker scaffold-eligibility is operator-deferred; supply-chain pattern dossier (separate from CVE-anchored vulnerability dossier) is the alternative substrate.
