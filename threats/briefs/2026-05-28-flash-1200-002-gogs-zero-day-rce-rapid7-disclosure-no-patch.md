---
brief_id: flash-2026-05-28-1200-002-gogs-zero-day-rce-rapid7-disclosure-no-patch
brief_type: flash
published_at: 2026-05-28T12:40:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_required_wep_ceiling_likely
human_override: null
findings_referenced:
  - finding-2026-05-28-FLASH-1200-0002
related_actors_referenced: []
related_vulns_referenced:
  - cve_id: not_yet_assigned
    product: "Gogs (self-hosted Git)"
    vendor: "Gogs (open source maintainers)"
    cvss: not_yet_assigned
    cwe_class: argument_injection_in_pull_request_rebase_handling
    affected_versions: ["0.14.2", "0.15.0+dev"]
    patched_version: none_at_disclosure
    patch_available: false
    cisa_kev_listed: false_at_sweep_time
    install_base_exposure:
      shadowserver_exposed_instances: 2400_plus
      shodan_fingerprint_ips: 1000_plus
      geographic_skew: asia_and_europe_primary
related_findings_referenced:
  - finding-id: finding-2026-05-12-FLASH-0001
    relationship: adjacent_developer_tooling_exposure_class_npm_supply_chain_pattern_not_same_vector
  - finding-id: finding-2026-05-20-FLASH-0001
    relationship: adjacent_developer_tooling_exposure_class_vscode_marketplace_extension_not_same_vector
digraph: A2
digraph_layered:
  cluster_anchor: A2
  rapid7_zero_day_disclosure: A2
  no_cve_assigned_at_disclosure: A1
  no_patch_available_at_disclosure: A1
  disclosure_timeline_march_17_to_may_28_60_plus_days_vendor_silence: A2
  affected_versions_0_14_2_and_0_15_0_dev: A2
  argument_injection_in_pull_request_rebase_handling_mechanism_class: A2
  authentication_pre_condition_registered_user_required: A1
  effective_pre_auth_on_default_open_registration_configuration: A2
  shadowserver_2400_plus_exposed_instances: B2
  shodan_1000_plus_ips_with_gogs_fingerprint: A2
  no_confirmed_in_wild_exploitation_of_this_specific_zero_day: A1
  cve_2025_8110_historical_exploitation_of_related_gogs_flaw: A2
  no_actor_attribution: A1
  no_a_and_d_prime_named_as_victim: A1
wep: likely
wep_layered:
  vulnerability_existence_and_mechanism_class: likely_to_very_likely    # Rapid7 A-grade single-source on originating disclosure; "likely" floor
  no_patch_no_cve_at_disclosure_time: very_likely                       # A1 procedural fact
  install_base_2400_plus_exposed_instances: very_likely                  # Shadowserver + Shodan independent on exposure layer
  effective_pre_auth_on_default_config: likely
  imminent_exploitation_following_public_disclosure: likely              # orchestrator-side forward-projection from corpus-historical pattern
  a_and_d_inheritance_via_self_hosted_scm_estate: roughly_even_chance   # structural-inferential
single_source_veto_applied: true
single_source_veto_scope: imminent_exploitation_forward_projection_layer_rapid7_does_not_attest_imminence_this_is_orchestrator_inference_from_corpus_historical_pattern_disclosure_event_install_base_and_open_registration_default
single_source_veto_lift_conditions: independent_a_b_vendor_ir_or_threat_intel_firm_observes_exploitation_of_this_specific_argument_injection_flaw_or_cisa_kev_addition_once_cve_assigned_or_shodan_shadowserver_telemetry_confirming_widespread_post_disclosure_scanning_of_internet_exposed_gogs_instances
red_team_review_required: false
red_team_review_outcome: not_invoked_wep_ceiling_at_likely
quiet_hours_at_compose: false
critical_override_applied: false
critical_override_evaluation:
  cvss_10_0: false                          # no CVSS assigned at disclosure time
  cvss_value: null
  active_exploitation: false                 # Rapid7 explicitly attests no confirmed in-wild exploitation of this specific zero-day; CVE-2025-8110 is historical context only
  tracked_actor_involved: false              # no actor attribution
  ad_watchlist_targeted: false               # no A&D-prime named
  conditions_met: 0_of_4
  result: override_does_not_apply
  reason: "All four prongs fail — no CVSS, no current exploitation, no actor, no A&D-watchlist entity. Quiet-hours bypass irrelevant; 12:40 EDT is within active hours regardless."
disposition: post_within_active_hours_no_queue
flash_trigger_fit:
  trigger_id_claimed: zero-day-no-patch
  cvss_threshold_met: indeterminate_no_cvss_assigned_but_rce_mechanism_class_would_typically_score_8_to_9
  no_patch_confirmed: true
  exploitation_confirmed_or_imminent_per_a_grade_source: marginal_imminent_is_orchestrator_inference_not_rapid7_direct_attestation
  caveat: "Trigger 6 spec requires 'exploitation confirmed or imminent per A-grade source.' Rapid7 (A provisional) does NOT directly attest imminence — the 'imminent' reading is Archimedes-side inference from (a) public disclosure event raises exploitation risk against unpatched instances; (b) 60+ days vendor silence; (c) effective pre-auth attack surface on default config; (d) 2,400+ install base; (e) corpus-historical pattern of related Gogs CVE-2025-8110 exploitation. Trigger fires on the totality, not on single-source attestation of imminence. Operator may re-tune Trigger 6 wording to clarify whether 'imminent per A-grade source' requires (i) explicit A-grade attestation of imminence or (ii) A-grade attestation of preconditions with orchestrator inference."
hard_rule_2_framings_load_bearing:
  - "No actor or nation-state attributed to either this current flaw OR to the historical CVE-2025-8110 exploitation per Rapid7 / BleepingComputer"
  - "Archimedes does not originate attribution"
  - "BleepingComputer cites CVE-2025-8110 as historical context only — NOT claimed as the current flaw"
  - "'Imminent exploitation' is Archimedes-side orchestrator inference from preconditions, not Rapid7 vendor attestation"
hard_rule_6_quote_budget:
  total_quotes_in_brief: 0
  rationale: "Paraphrase only — no direct quotation."
hard_rule_8_first_party_check:
  splunk_query: "index=defenseclaw_local OR index=archimedes (gogs OR \"gogs.io\" OR \"git_repository\" OR Rapid7) earliest=-30d"
  result: 0_hits
  interpretation: silence_is_not_contradiction_per_doctrine_credibility_grade_unchanged
  consecutive_dormant_non_self_sweep_count: 67
ad_relevance_class: structural_indirect_self_hosted_scm_on_premise_alternative_to_github_enterprise_gitlab_self_managed_bitbucket_in_dib_engineering_team_settings_no_named_victims_no_named_sector_targeting_geographic_skew_asia_and_europe_suggests_typical_gogs_deployment_may_not_be_us_dib
librarian_handoffs:
  - action: collector_watch_config_addition
    target: infrastructure/watch-config.yaml
    payload: "Add `gogs-argument-injection-2026-05-28` to vuln-watch keywords; monitor for CVE assignment, Gogs upstream commit referencing rebase / argument-injection / branch-name handling, and any vendor IR firm observation of exploitation"
  - action: direct_retrieval_followup
    target: rapid7_primary_disclosure_blog_url
    payload: "Directly retrieve Rapid7 primary disclosure blog post in next collection cycle to confirm BleepingComputer relay faithfulness; this sweep evidence basis was BleepingComputer-relay only"
  - action: discord_post
    target: "#flash-alerts"
    payload: "FLASH within active hours; no queue; post immediately"
vuln_tracker_handoffs:
  - action: standalone_dossier_candidate_eval
    target: threats/vulnerabilities/gogs-argument-injection-rce-unassigned-CVE/
    payload: "Gogs argument-injection RCE; no CVE assigned at sweep time; no patch; affected versions 0.14.2 and 0.15.0+dev; effective pre-auth on default open-registration config; 2,400+ exposed instances per Shadowserver; mechanism class is git-rebase argument injection; Rapid7 Jonah Burges disclosure 2026-05-28 after 60+ days vendor silence following 2026-03-17 report; recommend MEDIUM-priority dossier scaffolding pending CVE assignment + patch publication; vuln-tracker monitors CVE assignment + Gogs upstream commit"
  - action: monitor_for_cve_assignment
    target: NVD_MITRE_cve_feed
    payload: "Gogs argument-injection RCE awaiting CVE assignment as of 2026-05-28 12:40 EDT; expected within 7-14 days based on historical NVD assignment cadence for vendor-coordinated-late disclosures"
word_count: 387
word_count_band: over_target_150_300_under_hard_cap_450_per_litespeed_2026_05_23_precedent
word_count_rationale: "FLASH runs hot when doctrinal framings (single-source veto on imminence, Hard Rule 2 attribution, Hard Rule 8 first-party check, Trigger 6 fit caveat, A&D-relevance qualifier, no-patch action-set) are all load-bearing per grader. Body is 387 words; under the 450-word hard cap (150% of FLASH max 300). Precedent: flash-2026-05-23-0600-002-litespeed-cpanel ran ~414 body words with same regulatory-framing load."
tlp: CLEAR
test: false
discord_delivery:
  channel: flash-alerts
  channel_id: "1499952828087533588"
  message_ids:
    - "1509595715582824574"
    - "1509595733513208000"
    - "1509595751217369282"
  parts: 3
  delivered_at: 2026-05-28T13:00:00-04:00
  late: false
  via: librarian
  complete: true
  run_id: librarian-flash-1200-20260528
---

# ⚡ FLASH: Gogs self-hosted Git zero-day RCE — Rapid7 discloses after 60+ days of vendor silence; no patch, no CVE assigned

*2026-05-28 12:40 EDT · A2 · WEP likely · TLP:CLEAR · posts immediately, within active hours*

**Action.** There is no patch. DIB engineering teams running self-hosted Gogs (versions **0.14.2** and **0.15.0+dev**): (1) inventory Internet-exposed Gogs instances now — Shadowserver tracks 2,400+ globally, Shodan 1,000+; (2) **disable open registration** on every deployed instance (admin → site settings → `DISABLE_REGISTRATION = true`) — this collapses the effective pre-auth attack surface to known-user only; (3) restrict Gogs admin and web surfaces to VPN / IP allowlist; (4) monitor the Gogs upstream repository for a fix commit and CVE assignment. Gitea / Forgejo / GitLab / GitHub Enterprise deployments are **not affected** by this flaw.

**What.** [Rapid7 senior security researcher Jonah Burges has disclosed](https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution/) a zero-day argument-injection RCE in Gogs pull-request rebase handling — malicious branch names passed to `git rebase` during the "Rebase before merging" flow enable arbitrary command execution. A registered user account is technically required, but Gogs ships with **open registration enabled by default**, so any reachable instance is effectively pre-auth. Rapid7 reported the flaw to maintainers on **2026-03-17**, was acknowledged on 2026-03-28, and disclosed publicly today after 60+ days of vendor silence. **No CVE assigned. No patch.**

**Exploitation framing (single-source veto on imminence).** Rapid7 attests no confirmed in-wild exploitation of this specific flaw at disclosure. BleepingComputer cites the related **CVE-2025-8110** Gogs flaw as historical exploitation context only — *not* claimed as the current flaw. The "imminent exploitation" framing on this brief is Archimedes-side inference from public disclosure, install-base size, open-registration default, and the historical-pattern precedent — *not* a Rapid7 direct attestation. WEP capped at *likely*; lift conditions are independent vendor-IR observation, CISA KEV addition once CVE assigned, or Shodan / Shadowserver telemetry confirming widespread post-disclosure scanning.

**Impact.** A&D-prime direct exposure is **structural-indirect**: self-hosted SCM is competitive with GitHub Enterprise / GitLab Self-Managed / Bitbucket Data Center in the DIB / ITAR / CMMC engineering-team setting, but the Gogs install-base geographic skew (Asia and Europe primary) suggests the typical deployment may not be US-DIB. **No A&D-prime, sector, or geography has been named.** No actor attribution from any source; *Archimedes does not originate one.*

**First-party Splunk.** Zero hits at -30d on Gogs product + Rapid7 researcher sweep across `defenseclaw_local` + `archimedes`. Per Hard Rule 8: silence is not contradiction. 67th consecutive dormant non-self sweep.

**Trigger 6 fit caveat.** Spec requires "exploitation confirmed or imminent per A-grade source." Rapid7 (A provisional) attests preconditions, not imminence; the imminence reading is orchestrator inference. Trigger fires on the totality. Critical override 0/4 — fails all four prongs.

**Sources.** [BleepingComputer (2026-05-28 10:25 EDT, Sergiu Gatlan)](https://www.bleepingcomputer.com/news/security/new-gogs-zero-day-flaw-lets-hackers-get-remote-code-execution/) — B relay · Rapid7 (Jonah Burges, A provisional) — sole primary disclosure (direct URL pending next collection cycle).

**Related.** [finding-2026-05-28-FLASH-1200-0002](../findings/finding-2026-05-28-FLASH-1200-0002-bleepingcomputer-gogs-zero-day-rce-rapid7-jonah-burges-no-patch.md). No prior Gogs coverage in corpus. Adjacent developer-tooling-exposure class: [finding-2026-05-12-FLASH-0001](../findings/finding-2026-05-12-FLASH-0001.md) (npm supply-chain) and [finding-2026-05-20-FLASH-0001](../findings/finding-2026-05-20-FLASH-0001.md) (VS Code marketplace) — different vectors, same SDLC exposure umbrella. Vuln-tracker handoff: MEDIUM-priority dossier pending CVE assignment.
