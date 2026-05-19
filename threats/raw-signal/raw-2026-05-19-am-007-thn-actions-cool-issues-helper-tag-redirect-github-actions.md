---
raw_id: raw-2026-05-19-am-007
collected_at: 2026-05-19T07:58:00-04:00
run_id: pre-brief-20260519-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News (Ravie Lakshmanan)"
  source_url: https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html
  published_at: 2026-05-19T01:28:06-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [GitHub Actions, actions-cool, issues-helper, maintain-one-comment, tag-redirect, Bun runtime, Runner.Worker memory, supply chain, Mini Shai-Hulud]
triage_tags:
  - github_actions_supply_chain_compromise
  - actions_cool_issues_helper_all_tags
  - actions_cool_maintain_one_comment_15_tags
  - stepsecurity_varun_sharma_originating_research
  - socket_philipp_burckhardt_cross_link_to_mini_shai_hulud_antv
  - mini_shai_hulud_cluster_attribution_via_shared_c2_t_m_kosche
  - teampcp_attribution_not_propagated_to_this_surface_per_hard_rule_2
  - bun_runtime_lolbin_variant
  - runner_worker_memory_credential_extraction_class
  - tag_redirect_to_imposter_commit_tradecraft
  - github_disabled_repo_access_at_detection
  - active_exploitation_in_wild_via_downstream_workflow_runs
  - t_m_kosche_com_c2_domain_net_new_ioc
  - vt006_ioc_augmentation_candidate
  - flash_06_00_carry_forward_for_grader
  - hard_rule_2_no_attribution_origination
iocs_extracted: true
iocs_count: 4
text_word_count: 768
promoted: true
promoted_to_finding: finding-2026-05-19-0001
promoted_at: 2026-05-19T08:14:00-04:00
ttl_expires_at: 2026-08-17T07:58:00-04:00
---

# Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials

## Headline & date

**Source:** The Hacker News (Ravie Lakshmanan) — 2026-05-19T01:28:06-04:00 (05:28 GMT)
**Headline:** "Popular GitHub Action Tags Redirected to Imposter Commit to Steal CI/CD Credentials"
**URL:** https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html

## Originating researchers

- **StepSecurity** — analyst Varun Sharma. Provisional B per source-grades.yaml (first cited 2026-05-12-FLASH-0001; awaiting human ratification).
- **Socket** — analyst Philipp Burckhardt. Provisional B per source-grades.yaml (first cited 2026-05-14-0009; awaiting human ratification).

## Attack core

Two compromised GitHub Actions in the actions-cool organization:

- `actions-cool/issues-helper` — **all existing tags** moved to point to an imposter commit
- `actions-cool/maintain-one-comment` — **15 tags** moved to imposter commits

GitHub disabled both repositories at detection citing terms-of-service violation.

**Tradecraft chain (per StepSecurity + Socket):**

1. Attacker controls upstream repo state and rewrites every existing tag in the repository to point to an imposter commit not in the action's normal commit history.
2. Imposter commit downloads the **Bun JavaScript runtime** to the runner as a LOLBin variant.
3. Bun script reads memory from the `Runner.Worker` process to extract in-memory credentials (the GitHub Actions secrets that the workflow had ephemeral access to).
4. Extracted credentials exfiltrated via HTTPS to `t.m-kosche[.]com` (C2 domain — **NET-NEW IOC**, shared with @antv `atool` maintainer compromise per Socket Philipp Burckhardt cross-link observation).

StepSecurity researcher Varun Sharma: paraphrased per Rule 6 — every existing tag was moved to point to an imposter commit not in the action's normal commit history (16w original quote over 15w ceiling).

## Impact & exploitation status

**ACTIVE exploitation in the wild for downstream CI/CD consumers:** any workflow that references the action by tag pulls the malicious code on its next run. Only workflows pinned to known-good commit SHAs remain unaffected.

## IOCs

| IOC | Type | Notes |
|---|---|---|
| `t.m-kosche[.]com` | C2 domain | NET-NEW; shared with @antv `atool` maintainer compromise per Socket cross-link |
| `actions-cool/issues-helper` (all tags) | compromised artifact | GitHub Action; disabled by GitHub at detection |
| `actions-cool/maintain-one-comment` (15 tags) | compromised artifact | GitHub Action; disabled by GitHub at detection |
| Tag-redirect to imposter-commit (technique) | tradecraft pattern | detection-relevant — workflows pinned to SHAs unaffected |

## Attribution per source

**Mini Shai-Hulud** campaign-cluster attribution via Socket Philipp Burckhardt's cross-link observation that the exfiltration domain overlaps with the Mini Shai-Hulud campaign targeting npm packages from the @antv ecosystem. THN echoes Socket's framing.

THN does **NOT** independently name TeamPCP for THIS specific incident. Per Hard Rule 2, Archimedes does NOT propagate TeamPCP attribution from finding-2026-05-12-FLASH-0001 / VT-006 to this surface — the Mini Shai-Hulud campaign-cluster linkage IS source-said (Socket), but the TeamPCP-as-actor attribution chain (Wiz + StepSecurity + Snyk originating, finding 0001) is NOT extended to this specific incident by either StepSecurity or Socket in their published writeups.

## A&D / defense-prime relevance

None directly. SDLC-class CI/CD-consumer targeting. STRUCTURAL relevance: the `actions-cool` organization's two compromised actions appear in standard GitHub Actions workflows across all sectors. Any A&D-prime CI/CD pipeline that references these actions by tag (vs. SHA-pinned) was exposed during the compromise window.

## Trigger evaluation (carry-forward from FLASH-06:00 sentinel)

- T1 (CVE+active+A-grade): no CVE → **FAIL**
- T2 (new attribution to roster): no roster actor; Mini Shai-Hulud is a campaign-cluster not a roster member; per Hard Rule 2 cannot propagate Mini Shai-Hulud → TeamPCP attribution from VT-006 to this specific incident → **FAIL**
- T3 (Splunk IOC): 0 hits on `t.m-kosche` / `actions-cool/issues-helper` / `actions-cool/maintain-one-comment` tokens per pre-brief Splunk sweep → **FAIL**
- T4 (TTP change): no roster actor → **FAIL** (Bun runtime LOLBin variant + Runner.Worker memory-exfil tradecraft variant absorbs into VT-006 TTP refinement at morning grader)
- T5 (A&D campaign): no A&D customer → **FAIL**
- T6 (zero-day): tag-redirect-then-rotate technique against GitHub Actions registry boundary; GitHub disabled repo access at detection — registry-side mitigation, not zero-day → **FAIL**

## Disposition

**VT-006 IOC-augmentation candidate** for morning grader: net-new C2 `t.m-kosche[.]com` cross-binds this surface with the @antv `atool` maintainer compromise (am-008); Bun-runtime LOLBin variant + Runner.Worker memory-credential-extraction tradecraft variant + tag-redirect-to-imposter-commit technique all extend VT-006's tradecraft catalog.

## Extraction notes

- Language: en
- Publisher byline: Ravie Lakshmanan
- Article type: news + originating-research relay
- Hard Rule 2: Mini Shai-Hulud cluster-overlap preserved as Socket-said. TeamPCP NOT propagated to this surface.
- Hard Rule 3: tradecraft chain described at IOC level without weaponized exploit guidance; StepSecurity / Socket technical writeups not linked at exploit-detail level.
- Raw IOC extraction invoked: yes — 1 domain (t.m-kosche.com) + 2 GitHub Action paths + 1 detection-pattern (tag-redirect).
