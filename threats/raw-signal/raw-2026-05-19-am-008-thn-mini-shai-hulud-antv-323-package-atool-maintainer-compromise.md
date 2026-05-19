---
raw_id: raw-2026-05-19-am-008
collected_at: 2026-05-19T08:02:00-04:00
run_id: pre-brief-20260519-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News (Ravie Lakshmanan)"
  source_url: https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html
  published_at: 2026-05-19T00:54:17-04:00
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: [CVE-2026-45321]
  keywords: [Mini Shai-Hulud, npm, atool maintainer, @antv, echarts-for-react, OIDC, Sigstore attestation forgery, SLSA provenance forgery, Docker host socket, BreachForums, supply chain]
triage_tags:
  - mini_shai_hulud_largest_single_day_expansion
  - 639_versions_323_packages_22_min_burst
  - atool_maintainer_compromise_vector
  - teampcp_attribution_source_said_anti_noise_locked_no_new_attribution
  - finding_2026_05_12_FLASH_0001_cluster_anchor_carry_forward
  - vt006_carry_forward_anti_noise_active
  - t_m_kosche_com_c2_shared_with_actions_cool_surface
  - niagA_oG_eW_ereH_duluH_iahS_marker_string
  - 2500_plus_marker_repos_scale_observation
  - docker_host_socket_container_escape_variant
  - oidc_sigstore_slsa_forgery_class
  - 20plus_credential_class_enumeration
  - socket_stepsecurity_safedep_jfrog_endor_datadog_trendmicro_mondoo_oxsecurity_relay_set
  - no_a_and_d_customer_named
  - non_a_and_d_general_dev_tooling_at_antv_visualization
  - hard_rule_2_no_attribution_origination
  - flash_06_00_carry_forward_for_grader
  - vt006_ad_relevance_refinement_candidate
iocs_extracted: true
iocs_count: 14
text_word_count: 1024
promoted: true
promoted_to_finding: finding-2026-05-19-0001
promoted_at: 2026-05-19T08:14:00-04:00
ttl_expires_at: 2026-08-17T08:02:00-04:00
---

# Mini Shai-Hulud Pushes Malicious AntV npm Packages via Compromised Maintainer Account

## Headline & date

**Source:** The Hacker News (Ravie Lakshmanan) — 2026-05-19T00:54:17-04:00 (04:54 GMT)
**Headline:** "Mini Shai-Hulud Pushes Malicious AntV npm Packages via Compromised Maintainer Account"
**URL:** https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html

## Originating researchers (multi-vendor relay-set)

Socket + StepSecurity + SafeDep + JFrog + Endor Labs + Datadog + Trend Micro + Mondoo + Ox Security. Eight distinct security-research firms tracking and publishing on the same surface.

## Attack scope (largest single-day Mini Shai-Hulud expansion to date)

- **639 malicious versions** across **323 unique packages**
- **558 versions** across **279 @antv packages** (@antv/g2, @antv/g6, @antv/x6, @antv/l7, @antv/s2, @antv/f2, @antv/g, @antv/g2plot, @antv/graphin, @antv/data-set, …)
- Non-@antv ecosystem: `echarts-for-react` (~1.1M weekly downloads), `timeago.js`, `size-sensor`, `canvas-nest.js`
- Compromised npm maintainer account: **`atool`**
- Publish burst: **22 minutes** across 317 packages with identical obfuscated payload (rules out gradual operation)

## Tradecraft

- **preinstall hooks** (`bun run index.js`)
- **optionalDependencies injection**: 630/637 versions inject optionalDependencies pointing to imposter commits in legitimate `antvis/G2` GitHub repo
- **Credential stealer**: harvests **20+ credential classes** — AWS, GCP, Azure, GitHub, npm, SSH, Kubernetes, Vault, Stripe, Docker
- **Docker container escape**: via host socket
- **Primary exfil**: `t.m-kosche[.]com:443` — **SHARED WITH actions-cool/issues-helper compromise** (am-007) cross-binding the two surfaces
- **Fallback exfil**: GitHub-token-abuse to create public repos with marker description **`niagA oG eW ereH :duluH-iahS`** (reverses to "Shai-Hulud: Here We Go Again")
- **2,500+ repositories** identified with the marker string (NET-NEW scale observation)
- **OIDC-token abuse + Sigstore attestation pipeline**: forges legitimate release signatures via CI runner identity
- **SLSA provenance forgery**

## Attribution per source

THN explicitly attributes to **"TeamPCP (financially motivated actor)"** per the attribution paragraph. Framing references the antecedent context that TeamPCP released full malware source code to BreachForums (supply chain attack contest partnership) — already covered in finding-2026-05-12-FLASH-0001 + finding-2026-05-15-* + finding-2026-05-18-0003 carry-forward chain.

**Anti-noise rule 1 applies on the attribution layer:** TeamPCP→Mini-Shai-Hulud attribution was already established in finding-2026-05-12-FLASH-0001 (Wiz + StepSecurity originating; Snyk relay) and VT-006 carry-forward. This article is **incremental cluster expansion**, NOT first-time attribution. Per FLASH-POLICY.md Trigger 2 evidence-minimum, the `new_attribution: true` predicate **FAILS**.

## IOCs

| IOC | Type | Notes |
|---|---|---|
| `t.m-kosche[.]com:443` | C2 domain | NET-NEW; cross-binds with actions-cool/issues-helper (am-007) |
| `atool` (npm maintainer account) | identity artifact | compromised account; vector for 639 versions / 323 packages |
| `niagA oG eW ereH :duluH-iahS` | marker string | reversed "Shai-Hulud: Here We Go Again"; 2,500+ marker-repos identified |
| `@antv/g2` … `@antv/data-set` (10 named) | npm packages | 279 packages × 558 malicious versions; preinstall-hook + optionalDependencies injection |
| `echarts-for-react` | npm package | ~1.1M weekly downloads; non-@antv ecosystem |
| `timeago.js` | npm package | non-@antv ecosystem |
| `size-sensor` | npm package | non-@antv ecosystem |
| `canvas-nest.js` | npm package | non-@antv ecosystem |
| `bun run index.js` (preinstall) | tradecraft pattern | Bun-runtime LOLBin |
| optionalDependencies pointing to imposter commits in `antvis/G2` repo | tradecraft pattern | 630/637 versions |
| Docker host-socket container-escape | tradecraft pattern | runtime-class container escape |
| OIDC + Sigstore + Fulcio attestation forgery | tradecraft pattern | CI-runner-identity abuse |
| SLSA provenance forgery | tradecraft pattern | attestation-chain breakage |
| GitHub-token-abuse to create public repos with marker description | tradecraft pattern | fallback exfil + scale measurement |

## A&D / defense-prime relevance

NO A&D customer named. The @antv visualization-library ecosystem is general developer tooling — distinct from VT-006 prior surface where @squawk aviation packages were named. ad_relevance_rationale for THIS surface is LOW-INDIRECT. This AFFIRMS VT-006's existing 'A&D-prime dependency-graph reach unverified' caveat: the cluster has expanded WITHOUT touching aviation packages this surface, suggesting maintainer-enumeration-driven mechanism not sector-targeted.

## Trigger evaluation (carry-forward from FLASH-06:00 sentinel)

- T1 (CVE+active+A-grade): no NEW CVE — parent VT-006 CVE-2026-45321 carry-forward already covers cluster → **FAIL**
- T2 (new attribution): TeamPCP IS roster #001 HIGH AND attribution IS source-said by THN/Socket, BUT this is NOT new attribution per anti-noise rule 1 — already established in finding-2026-05-12-FLASH-0001 + VT-006 carry-forward. `new_attribution: true` predicate FAILS → **FAIL**
- T3 (Splunk IOC): 0 hits across all tokens per pre-brief Splunk sweep → **FAIL**
- T4 (TTP change): tradecraft refinements (atool maintainer-account vector + 22-min publish burst + GitHub-Search-API dead-drop variant + 2,500+ marker-repo scale + Bun-runtime as preinstall LOLBin + Docker-host-socket container-escape variant) are within-cluster TTP refinement NOT class-change vs VT-006 baseline; per anti-noise rule 1 absorbs into VT-006 morning grader IOC-augmentation pass → **FAIL** on anti-noise
- T5 (A&D campaign): no A&D-sector targeting; @antv visualization-library ecosystem is general dev tooling → **FAIL**
- T6 (zero-day): rolling unpublishes per VT-006 patch_status; no zero-day boundary → **FAIL**

## Disposition

**STRONG cluster-anchor-refinement for VT-006 update at 08:00 morning brief** — largest single-day surface-area expansion of the Mini Shai-Hulud cluster to date. Net-new IOCs (atool maintainer account + `niagA oG eW ereH :duluH-iahS` marker string + 2,500+ marker-repo discovery + `t.m-kosche[.]com:443` cross-bound C2 + Docker-host-socket container-escape variant + 20+ credential-class enumeration) extend VT-006's catalog.

**Recommend VT-006 ad_relevance refinement** by morning grader: was 'medium_indirect_via_squawk_aviation_ecosystem' — needs adjustment now that the cluster has expanded WITHOUT touching aviation packages this surface, suggesting maintainer-enumeration-driven mechanism not sector-targeted.

## Extraction notes

- Language: en
- Publisher byline: Ravie Lakshmanan
- Article type: news + multi-vendor relay
- Hard Rule 2: TeamPCP attribution preserved as-source-said per THN + Socket multi-firm consensus; NOT propagated to am-006 Nx Console or am-007 actions-cool surfaces.
- Hard Rule 3: tradecraft described at IOC level; no PoC code, no exploit walkthrough, no Socket / StepSecurity blog URL linked at exploit-detail level.
- Raw IOC extraction invoked: yes — 14 indicators (1 C2 domain + 1 maintainer-account identity + 1 marker string + 5 npm packages + 5 tradecraft patterns + 1 detection-pattern).
