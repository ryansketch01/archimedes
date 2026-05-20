---
brief_id: flash-2026-05-20-0608-teampcp-github-internal-repos
brief_type: flash
published_at: 2026-05-20T06:08:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
analyst_review: pending (analyst_review_required: true — framing-gap SAT-ACH on GitHub-vs-TeamPCP language; cross-corpus C2 SAT-KAC on t.m-kosche.com)
red_team_review: complete (red-team-20260520-064500 — qualify, language-discipline W1-W5; no WEP adjustment)
human_override: null
findings_referenced:
  - finding-2026-05-20-FLASH-0001
related_actors_referenced:
  - actor_id: "001"
    actor_name: TeamPCP
    treatment: self_claimed_on_breached_relayed_via_three_b_grade_media_single_source_veto_on_attribution_layer_no_archimedes_origination
related_vulns_referenced:
  - vt_id: VT-006
    cve: CVE-2026-45321
    role: parent_campaign_chain_2026_sdlc_supply_chain
related_findings_referenced:
  - finding-id: finding-2026-05-12-FLASH-0001
    relationship: vt_006_corpus_anchor_mini_shai_hulud_worm_deployment_a1_attribution_chain
  - finding-id: finding-2026-05-14-0008
    relationship: openai_tanstack_first_named_enterprise_victim_vendor_self_disclosure_precedent_class
  - finding-id: finding-2026-05-15-FLASH-0002
    relationship: teampcp_source_code_release_distinct_topic_teampcp_as_releaser_not_intruder
  - finding-id: finding-2026-05-19-0001
    relationship: mini_shai_hulud_expansion_cross_corpus_c2_t_m_kosche_via_socket_burckhardt_named_analyst_higher_rigor_chain
  - finding-id: finding-2026-05-19-0002
    relationship: nx_console_vs_code_extension_class_sibling_distinct_mechanism_hard_rule_2_no_teampcp_propagation
digraph: B2
digraph_layered:
  cluster_anchor: B2
  github_breach_procedural_facts: A2
  teampcp_attribution: B2
  c2_malicious_status: A1
  c2_attribution_to_teampcp: F6
wep: likely
wep_split:
  github_breach_factually_occurred: very_likely
  approximately_3800_repos_scope: very_likely
  vs_code_extension_initial_access_vector: very_likely
  customer_data_no_evidence_of_impact: likely
  teampcp_attributed_compromiser: likely
  campaign_chain_extension_to_github_corp: likely
  c2_check_git_service_com_malicious: very_likely
  c2_t_m_kosche_com_malicious: very_likely
  c2_attribution_to_teampcp: roughly_even_chance
  ad_prime_supply_chain_exposure_increase: likely
single_source_veto_applied: true
single_source_veto_layer: teampcp_attribution_to_github_corp_compromise
quiet_hours_at_compose: true
critical_override_applied: false
critical_override_evaluation:
  cvss_10_0: false
  cvss_value: null
  active_exploitation: true
  tracked_actor_involved: true
  ad_watchlist_targeted: false
  conditions_met: 2_of_4
  result: override_does_not_apply
triggers_fired:
  - trigger_2_new_attribution_for_tracked_actor
  - trigger_4_tracked_actor_ttp_change
triggers_failed:
  - trigger_1_critical_cve_exploited
  - trigger_3_first_party_ioc_hit
  - trigger_5_explicit_ad_sector_targeting
  - trigger_6_zero_day_no_patch
posting_path: queue_for_catchup
quiet_hours_queued: true
expected_post_window: "09:00 EDT catchup sweep — librarian must check for supersession by 08:00 morning brief before posting"
absorbs_flash: null
anti_noise_lock: teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20
anti_noise_lock_expires: 2026-05-21T06:08:00-04:00
anti_noise_distinction:
  flash_2026_05_12_0600_mini_shai_hulud_worm_deployment: distinct_topic_different_victim_class
  flash_2026_05_15_0600_teampcp_source_code_release: distinct_topic_teampcp_as_releaser_not_intruder
  flash_2026_05_14_2200_mistral_450_repos_sale_raw: distinct_topic_parallel_commercialization_channel
  finding_2026_05_19_0002_nx_console_vs_code_extension: distinct_topic_different_mechanism_no_teampcp_propagation
hard_rule_2_framings_load_bearing:
  - "TeamPCP attribution: self-claim on Breached relayed by three B-grade media; NOT Archimedes-originated"
  - "GitHub's 'directionally consistent with our investigation' framing preserved verbatim; Archimedes does NOT upgrade to confirmed TeamPCP attribution"
  - "Campaign-chain placement sourced to SecurityWeek-relayed researcher commentary"
  - "Cross-corpus C2 t.m-kosche.com surfaces with asymmetric source rigor across finding-2026-05-19-0001 (Socket/Burckhardt named-analyst) and this finding (media-relay VT-lookup); clusters NOT collapsed"
  - "VS Code extension identifier withheld by GitHub across all four primaries; Hard Rule 3 — no speculation"
hard_rule_6_quote_budget:
  github: '"directionally consistent with our investigation" (6 words / 15)'
  teampcp_self_claim: '"this is not a ransom" (4 words / 15)'
  researcher_commentary: 'paraphrased; no direct quote used'
splunk_first_party:
  status: clean_at_compose
  query_window: -72h
  indexes_queried: [archimedes, defenseclaw_local]
  hits_external_iocs: 0
  hits_self_telemetry: 3
  hard_rule_8_framing: silence_not_disconfirming_not_confirming
  consecutive_dormant_sweep_count: 47
red_team_qualifying_recommendations_honored:
  W1_pending_direct_retrieval_qualifier: yes
  W2_approximately_3800_preserved_verbatim: yes
  W3_asymmetric_evidence_rigor_on_t_m_kosche_preserved: yes
  W4_lead_with_actionable_layer_not_structural_framing: yes
  W5_explicit_pending_direct_retrieval_qualifier_on_procedural_facts: yes
word_count: 300
tlp: CLEAR
test: false
---

# FLASH: TeamPCP self-claims compromise of GitHub-corp via poisoned VS Code marketplace extension — approximately ~3,800 internal repos exfiltrated

*2026-05-20 06:08 EDT · B2 · TLP:CLEAR · QUEUED — quiet hours, awaits 09:00 catchup sweep*

**Action.** A&D defenders: inventory VS Code marketplace extensions on developer workstations against a known-good baseline. Hunt unfamiliar publishers, recent installs, elevated-permission extensions. GitHub withheld the extension identifier — posture is inventory-and-baseline, not chase-a-named-extension (Hard Rule 3). Detection-add: `check.git-service.com` (VT 10/93; parent created 2016-02-09 — re-purposed long-dormant) and `t.m-kosche.com` (VT 15/91; parent created 2026-05-15 NameSilo — 5 days pre-incident).

**What.** [GitHub disclosed](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) — per three B-grade media relays; primary blog URL not directly retrieved this sweep — an employee device compromised via a poisoned VS Code extension, exfiltrating approximately ~3,800 internal repos. GitHub assesses no evidence of impact to customer data outside internal repos. [TeamPCP (#001, HIGH)](../threat-actors/_roster.yaml) self-claimed on Breached, listing ~4,000 repos at $50,000 minimum, framing as "this is not a ransom." GitHub calls the claim "directionally consistent with our investigation" — softer than confirmation. Procedural facts A2 / very likely (vendor-authority, pending retrieval); attribution B2 / likely (single-source veto on three relays of one self-claim); C2 malicious A1 / very likely; C2-to-TeamPCP roughly-even.

**Impact.** A&D-relevance structural-indirect — no A&D prime named. The exposure is developer workstations: VS Code reaches every Tier-1 / Tier-2 SDLC. Per SecurityWeek-relayed researcher commentary, this extends the TeamPCP 2026 SDLC chain (Trivy → Checkmarx → Bitwarden CLI → TanStack → OpenAI → Mistral → Grafana → GitHub-corp); Archimedes does not independently affirm. `t.m-kosche.com` also surfaces in [finding-2026-05-19-0001](../findings/finding-2026-05-19-0001.md) via Socket / Philipp Burckhardt named-analyst cross-binding — higher-rigor than this finding's media-relay VT-lookup; clusters NOT collapsed per Hard Rule 2.

**Sources.** [BleepingComputer](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) (Gatlan, 04:14 EDT, B) · The Hacker News (00:01 EDT, B provisional) · [SecurityWeek](https://www.securityweek.com/github-confirms-hack-impacting-3800-internal-repositories/) (Arghire, 05:28 EDT, B provisional; sole chain-placement). GitHub blog primary URL queued for next-pass retrieval.

**Related.** [TeamPCP #001](../threat-actors/_roster.yaml) · [VT-006](../vulnerabilities/_index.yaml) · [05-12 parent A1](../findings/finding-2026-05-12-FLASH-0001.md) · [05-14 OpenAI precedent](../findings/finding-2026-05-14-0008.md) · [05-15 releaser-distinct](../findings/finding-2026-05-15-FLASH-0002.md) · [05-19 cross-corpus C2](../findings/finding-2026-05-19-0001.md) · [05-19 Nx Console — NOT propagated](../findings/finding-2026-05-19-0002.md). Override 2/4.
