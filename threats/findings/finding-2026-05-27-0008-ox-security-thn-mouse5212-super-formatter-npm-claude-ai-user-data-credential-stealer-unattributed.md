---
finding_id: finding-2026-05-27-0008-ox-security-thn-mouse5212-super-formatter-npm-claude-ai-user-data-credential-stealer-unattributed
created_at: 2026-05-27T16:12:00-04:00
graded_by: grader
grading_run_id: afternoon-20260527-160000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: B3
digraph_layered:
  thn_relay_layer_disclosure: B3                          # B-grade media relay, single-source
  ox_security_originating_research_attestation: B3        # B-provisional primary, awaiting_direct_retrieval still set
  malicious_npm_package_existence_factual: B2             # vendor-attested artifact existence
  github_account_unplowed3584_attacker_controlled: B2     # vendor-attested artifact existence
  postinstall_credential_stealer_mechanism_description: B2  # mechanism description coherent
  claude_ai_user_data_directory_targeting_mnt_user_data: B3  # described per vendor, but no independent corroboration on Claude AI environment specifics
  download_count_676_at_disclosure: B3                     # npm registry figure inherently includes CI/CD scanners, automated crawlers
  hardcoded_github_token_leaked_in_malware_opsec_failure: B2  # vendor-attested observation
  campaign_name_malware_slop_researcher_coined: B2         # researcher working name (not actor designation)
  no_attribution_to_tracked_actor_explicit_decline: A1     # OX Security explicitly declines attribution
  ad_relevance_low_indirect: A1                            # Anthropic Claude AI not A&D-prime SDLC; AM-27 thematic arc connection structural-only
  cluster_anchor: B3

digraph_anchor: >
  Cluster digraph B3 anchored on The Hacker News (Wednesday 2026-05-27
  11:44 EDT) B-grade media relay of OX Security primary research by
  Moshe Siman Tov Bustan and Nir Zadok. The OX Security primary post URL
  was NOT directly retrieved this sweep — the THN relay is the only
  in-corpus evidence layer for this cluster. OX Security carries
  provisional B per source-grades.yaml since 2026-05-15 first-citation
  with `awaiting_direct_retrieval: true` flag still set as of this
  sweep. Per INTEL-GRADING.md credibility checklist: grade 1 fails
  (single source, no independent corroboration); grade 2 fails (the
  claim cluster has internally coherent technical claims and is
  consistent with established npm-supply-chain TTPs, BUT the
  awaiting_direct_retrieval flag means even the primary research has
  not been independently verified by direct fetch); grade 3 applies
  (single-source uncorroborated B-grade primary via B-grade relay,
  partially consistent with known TTPs with novel elements specific to
  Claude AI `/mnt/user-data` targeting). Single-source veto applies on
  any forward-looking WEP claims; cluster anchor B3.

source_reliability:
  grade: B
  source_name: "The Hacker News (relay) / OX Security (primary research)"
  source_yaml_id: thehackernews
  grade_rationale: >
    THN pre-assigned B per source-grades.yaml. OX Security provisional
    B per source-grades.yaml 2026-05-15 first-citation; awaiting human
    ratification AND awaiting direct-retrieval verification (the
    `awaiting_direct_retrieval: true` flag has been set since OX
    Security's first appearance and was NOT cleared this sweep — only
    the THN relay layer was directly retrieved). The cluster grade is
    held at B (not upgraded to A despite OX Security's apparent
    technical depth) because the primary research has not been
    directly verified by Archimedes and the relay layer is the only
    evidence basis available to the grader.
  provisional: false  # thehackernews itself is not provisional; ox-security primary is provisional but is not the proximate source
  primary_source_provisional:
    source_yaml_id: ox-security
    grade: B
    provisional: true
    provisional_since: 2026-05-15
    awaiting_direct_retrieval: true
    awaiting_direct_retrieval_flag_still_set_after_this_sweep: true
    librarian_action_recommended: >
      OX Security direct-retrieval verification has been pending since
      2026-05-15. This is the second corpus surface (Megalodon
      finding-2026-05-26 was the first; this mouse5212 surface is the
      second) where OX Security primary research is relayed without
      direct corpus retrieval. Recommend operator decision: either
      (a) clear the awaiting_direct_retrieval flag via direct WebFetch
      of ox.security/blog/ on next scheduled cycle, or (b) downgrade
      ox-security provisional grade from B to C if direct-retrieval
      gap persists past 2026-06-01.

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_but_source_b_grade_or_better
    - possibly_true_partially_consistent_with_known_ttps_but_some_elements_novel
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable
  grade_2_test:
    - probably_true_consistent_with_established_ttps_partial: "npm postinstall credential stealer is well-documented TTP class (TeamPCP Shai-Hulud, Mini Shai-Hulud, Megalodon, GlassWorm chains); attacker-controlled GitHub account as exfil destination is plausible primitive"
    - probably_true_no_contradicting_evidence_from_ab_grade_sources: "No contradicting source"
    - probably_true_technical_claims_internally_coherent: "Claims are coherent at architectural level (postinstall + GitHub-API exfil + Anthropic /mnt/user-data target)"
    - grade_2_blocked_by: "OX Security primary not directly retrieved by Archimedes; THN relay is only in-corpus evidence layer; no second A/B-grade vendor researcher has published parallel analysis of this specific package; OX Security awaiting_direct_retrieval flag still set after this sweep. The hardcoded-token OPSEC failure characteristic suggests lower-tier operator skill which differentiates from TeamPCP-tier tradecraft (consistent with researchers' positioning of broader 'low-bar entrants' trend) — this novel-element-vs-known-actor pattern keeps cluster at credibility 3."
  rationale: >
    The claim cluster (malicious npm package targeting Claude AI
    /mnt/user-data via postinstall credential-stealer exfiltrating to
    attacker-controlled GitHub) is plausible per established TTPs but
    cannot reach grade 2 because: (a) only the THN relay layer has been
    directly retrieved (OX Security primary post awaiting_direct_retrieval),
    (b) no second A/B-grade vendor researcher has published parallel
    analysis, (c) some novel-element-vs-known-actor signals (hardcoded
    token OPSEC failure, lower scale, lower technical sophistication)
    differentiate from established TeamPCP / GlassWorm tradecraft and
    suggest the researchers' own framing — "more threat actors getting
    into the game" — is the operative read. Cluster held at credibility
    3 (Possibly True).

corroboration:
  independent_sources:
    - thehackernews
    - ox-security                                          # primary research source; awaiting_direct_retrieval still set
  independent: false
  test_passed_no: >
    THN is a media relay of the OX Security primary. Per INTEL-GRADING
    independence test, a relay of source X is NOT corroboration of X.
    Cluster has ONE effective source (OX Security via THN). No second
    A/B-grade vendor researcher (Mandiant, Microsoft MSTIC, CrowdStrike,
    Unit 42, SentinelOne, Recorded Future, Volexity, Snyk, Socket, Wiz,
    Aikido, SafeDep, Onapsis, Upwind, Semgrep, StepSecurity, Phylum,
    JFrog Security, ReversingLabs) has published parallel analysis of
    the mouse5212-super-formatter package as of this sweep.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    Per pre-brief sentinel raw-2026-05-27-pm-000 targeted -9h@h sweep
    on archimedes + defenseclaw_local covering 'mouse5212-super-formatter',
    'unplowed3584', '/mnt/user-data', 'Malware-Slop'. ZERO non-archimedes-
    internal events. 67th consecutive dormant non-self sweep. Hard
    Rule 8: silence is not disconfirming. The package itself is npm-
    registry-hosted; first-party visibility would require active
    Anthropic-Claude-AI-developer-population telemetry which is not
    in the defenseclaw_local A&D-prime scope.

single_source_veto_applied: true
single_source_veto_rationale: >
  Per INTEL-GRADING single-source veto, single-source B-grade claims
  cap at WEP "likely" — and in this case, the source's own awaiting-
  direct-retrieval status (OX Security primary not directly retrieved)
  + the THN relay layer being the only directly-retrieved evidence
  basis lower the effective ceiling further. Cluster WEP ceiling held
  at "roughly_even_chance" for forward-looking claims (e.g., "this
  actor will continue operating" or "this campaign will expand") and
  "likely" for backward-looking factual claims (e.g., "the package
  existed and was published").

wep_ceiling: likely                                       # backward-looking factual; roughly_even_chance forward-looking
wep_layered:
  malicious_npm_package_mouse5212_super_formatter_existed: likely    # vendor-attested artifact
  github_account_unplowed3584_attacker_controlled: likely             # vendor-attested observation
  postinstall_credential_stealer_payload_architecture: likely         # mechanism description coherent
  claude_ai_mnt_user_data_targeting: roughly_even_chance              # vendor-described, no independent verification of Claude AI environment specifics
  hardcoded_github_token_opsec_failure: likely                        # vendor-attested observation
  lower_tier_operator_skill_relative_to_teampcp_tradecraft: roughly_even_chance  # interpretive framing
  campaign_expansion_beyond_single_package: roughly_even_chance       # forward-looking, no evidence basis
  thematic_continuation_of_ai_developer_tooling_supply_chain_pressure: likely  # corpus-anchored pattern across 5 in-class events since 2026-05-12

inclusion:
  eligible_for:
    - daily_brief_monitoring                              # C3+ monitoring tier; cumulative-thematic-bullet treatment recommended
    - weekly_synthesis                                    # pattern signal: 5th-in-class for AI-developer-tooling supply-chain pressure
    - ioc_master_index_propagation                        # mouse5212-super-formatter + github.com/unplowed3584 + Malware-Slop campaign-name
  not_eligible_for:
    - flash                                               # below B2; no FLASH trigger fires (no CVE / no tracked actor / no A&D-prime victim / no zero-day)
    - daily_brief_action                                  # below B2 minimum for action-item tier
    - actor_profile_update                                # explicit decline of attribution by OX Security; no roster candidate
    - vuln_tracker_index_update                           # no CVE assigned
  inclusion_rationale: >
    B3 cluster on B-grade THN relay of B-provisional OX Security primary.
    Per pre-brief sentinel recommendation, treatment is cumulative-
    thematic-bullet within the structural-supply-chain-warning section
    alongside AM-27 findings 0003 (SymJack symlink hijack against AI
    coding agents) + 0005 (MSTIC cryptojacking ScreenConnect AI-chatbot
    SEO poisoning) + carry-forwards from finding-2026-05-14-0008 (OpenAI
    TanStack supply-chain breach) and finding-2026-05-20-FLASH-0001
    (GitHub Nx Console 3,800-repo breach). Fifth-in-class for the
    AI-developer-tooling-ecosystem-under-sustained-supply-chain-pressure
    thematic arc since 2026-05-12. NOT a standalone PM-27 finding
    promotion candidate at headline tier; included as monitoring-tier
    finding for the cumulative thematic treatment.

# Cluster metadata
cluster:
  topic: "OX Security researchers Moshe Siman Tov Bustan + Nir Zadok via The Hacker News relay (Wednesday 2026-05-27 11:44 EDT) disclose malicious npm package `mouse5212-super-formatter` (676 downloads at disclosure; account creation 2026-05-26) disguised as 'archive deployment sync' utility — triggers in npm postinstall stage — authenticates to GitHub using victim's environment token OR hardcoded fallback token (so even environments without pre-existing GitHub credentials get exfiltrated) — recursively uploads local workspace files to attacker-controlled github.com/unplowed3584 (now suspended) — target directory Anthropic Claude AI's /mnt/user-data directory — hardcoded private GitHub token leaked in malware (OPSEC failure) — researcher-coined campaign working name 'Malware-Slop' — OX Security EXPLICITLY declines attribution to TeamPCP / Shai-Hulud / Mini Shai-Hulud / GlassWorm / Megalodon lineage despite tradecraft adjacency (lower-tier operator skill signals) — researchers characterize as part of broader trend of lower-bar entrants — Hard Rule 2: no cross-walk to tracked roster despite shared technical primitive of GitHub-token-exfil-via-postinstall-stage — A&D relevance LOW-INDIRECT (Anthropic Claude AI is target application, not A&D-prime SDLC software per se) — joins AI-developer-tooling-ecosystem-supply-chain-pressure thematic arc as fifth-in-class since 2026-05-12 alongside AM-27 findings 0003 + 0005 + finding-2026-05-14-0008 + finding-2026-05-20-FLASH-0001"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-27-pm-002
  related_actors: []                                       # OX Security explicit decline; Hard Rule 2 no cross-walk
  related_vulnerabilities: []                              # no CVE assigned
  attribution_claims:
    - claim: "Campaign 'Malware-Slop' is unattributed; researchers explicitly decline attribution to tracked actor"
      claimed_by: OX Security (Moshe Siman Tov Bustan + Nir Zadok) via The Hacker News
      claim_confidence_language: "explicit decline; researchers characterize as part of broader trend of lower-bar entrants"
      novelty_to_corpus: true                              # mouse5212-super-formatter + Malware-Slop working name + github.com/unplowed3584 all novel
      requires_analyst_review: false                       # explicit decline means no attribution to analyze
      hard_rule_2_status: "no attribution originated; OX Security decline preserved verbatim; no cross-walk to TeamPCP / Shai-Hulud / Mini Shai-Hulud / GlassWorm / Megalodon despite tradecraft adjacency"

# IOCs surfaced
iocs_surfaced:
  - type: npm_package
    value: "mouse5212-super-formatter"
    context: "Malicious npm package with postinstall credential-stealer payload targeting Claude AI /mnt/user-data directory. 676 downloads at OX Security disclosure (npm registry figure inherently includes CI/CD scanners + automated crawlers — actual installation count unclear). Package status at THN relay publication: STILL AVAILABLE on npm registry."
    confidence: medium-high
    source_attribution: "OX Security via The Hacker News 2026-05-27"
    defanged: false
    librarian_action_required: "Add to _master-index.yaml IOC index with category 'malicious_npm_package' and unattributed disposition. Cross-reference 'AI-developer-tooling-supply-chain-pressure' thematic tag for weekly-synthesis aggregation."
    attribution: UNATTRIBUTED (OX Security explicit decline)
  - type: github_account
    value: "github.com/unplowed3584"
    context: "Attacker-controlled GitHub account receiving exfiltrated files via API. Account creation 2026-05-26 (day before malicious-package surface). Status at OX Security disclosure: no longer available (suspended or taken down by GitHub Trust & Safety)."
    confidence: high
    source_attribution: "OX Security via The Hacker News 2026-05-27"
    defanged: false
    librarian_action_required: "Add to _master-index.yaml IOC index. Track for retroactive lookup if cluster develops attribution."
    attribution: UNATTRIBUTED
  - type: working_name
    value: "Malware-Slop"
    context: "OX Security researcher-coined working name for the campaign. NOT an attributed actor designation. Adopted in this finding as the bin-naming convention for the cluster pending any future attribution that would warrant /new-actor scaffolding."
    confidence: high
    source_attribution: "OX Security via The Hacker News 2026-05-27"
    defanged: false
    librarian_action_required: "Track as cluster name; not a roster candidate at this surface."
  - type: target_directory_path
    value: "/mnt/user-data"
    context: "Anthropic Claude AI's dedicated upload/output handling directory per OX Security description. Target of recursive workspace-file exfiltration."
    confidence: medium                                     # described per vendor but Archimedes has not independently verified Claude AI's user-data directory structure
    source_attribution: "OX Security via The Hacker News 2026-05-27"
    defanged: false
    librarian_action_required: "Track for cross-correlation with future AI-developer-tooling supply-chain findings."

ttp_keywords:
  - name: Supply-chain compromise via npm postinstall stage credential stealer
    framework_mapping: MITRE T1195.002 Supply Chain Compromise - Compromise Software Supply Chain
    context: "Well-documented npm supply-chain attack class — postinstall script triggers on package install and exfiltrates credentials. Shared technical primitive with TeamPCP Shai-Hulud / Mini Shai-Hulud / Megalodon / GlassWorm chains but lower-tier operator-skill signals (hardcoded fallback token + leaked private token in malware) differentiate."
  - name: GitHub-API-based exfiltration to attacker-controlled account
    framework_mapping: MITRE T1567.002 Exfiltration Over Web Service - Exfiltration to Cloud Storage
    context: "Recursive workspace-file upload via GitHub API to attacker-controlled github.com/unplowed3584. Distinct from C2-channel-mediated exfil; relies on GitHub as commodity exfil platform."
  - name: AI-developer-tooling-ecosystem targeting (Claude AI /mnt/user-data)
    framework_mapping: MITRE T1530 Data from Cloud Storage Object (adapted) + T1213 Data from Information Repositories
    context: "Anthropic Claude AI's dedicated user-data directory as exfil target — novel-to-corpus targeting class. Joins AI-developer-tooling-supply-chain-pressure thematic arc."

# Downstream handoff flags
analyst_review_required: false
analyst_review_topics: []
analyst_review_rationale: >
  No analyst SAT review required for this finding individually. OX
  Security's explicit decline of attribution means there is no
  attribution-validity ACH question to evaluate; no load-bearing
  assumption that would benefit from KAC review on a single B-grade
  uncorroborated source. The cumulative-thematic treatment in the
  PM-27 brief (and ongoing weekly-synthesis tracking of the AI-
  developer-tooling-supply-chain-pressure thematic arc) is briefer-
  and weekly-synthesis-tier work, not finding-individual analyst SAT
  work.

red_team_review_required: false
red_team_review_rationale: >
  WEP ceiling held at "likely" (backward-looking) / "roughly_even_chance"
  (forward-looking) per single-source veto + OX Security awaiting-
  direct-retrieval status. No load-bearing forward-looking assessment
  rising to "very likely" or higher that would warrant red-team
  challenge per CLAUDE.md pipeline definition.
red_team_review: null

analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-27-afternoon]
retracted: false
retraction_brief_id: null
---

# OX Security via THN — Malicious npm `mouse5212-super-formatter` exfils Anthropic Claude AI user data via attacker-controlled GitHub; researchers decline attribution

## Summary

OX Security researchers Moshe Siman Tov Bustan and Nir Zadok disclosed
a malicious npm package `mouse5212-super-formatter` (676 downloads at
disclosure; attacker GitHub account created 2026-05-26) that triggers
a credential-stealer in the npm postinstall stage and recursively
uploads files from Anthropic Claude AI's `/mnt/user-data` directory
to attacker-controlled `github.com/unplowed3584` via GitHub API. OX
Security explicitly declines attribution to TeamPCP / Shai-Hulud /
Mini Shai-Hulud / GlassWorm / Megalodon lineage despite shared
GitHub-token-exfil tradecraft, characterizing this as part of a
broader lower-bar-entrants trend. The cluster is fifth-in-class for
the AI-developer-tooling-ecosystem-supply-chain-pressure thematic
arc since 2026-05-12.

## Sources

### The Hacker News (thehackernews, digraph: B3 cluster anchor)

- URL: https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html
- Published: 2026-05-27 11:44 EDT
- Key claim: Relay of OX Security primary research disclosing the
  `mouse5212-super-formatter` malicious npm package.

### OX Security (ox-security, primary research; provisional B; awaiting_direct_retrieval still set)

- URL: https://www.ox.security/ (specific blog post URL not surfaced
  in THN relay text; awaiting_direct_retrieval flag still set after
  this sweep — flagged for librarian/collector follow-up)
- Key claim: Originating research; technical mechanism description;
  attacker-controlled GitHub account identification; OPSEC failure
  observation (hardcoded private GitHub token leaked in malware);
  campaign working name "Malware-Slop".

## Technical detail

The package disguises itself as an "archive deployment sync" utility.
Mechanism per OX Security via THN relay:

- **Trigger:** npm `postinstall` stage (well-documented supply-chain
  attack class).
- **Authentication primitive:** GitHub API via either the victim's
  environment token OR a hardcoded fallback token. This dual-mode
  authentication ensures environments without pre-existing GitHub
  credentials still get exfiltrated.
- **Exfil action:** Recursively uploads local workspace files to the
  attacker-controlled GitHub account.
- **Target directory:** `/mnt/user-data` — described as Anthropic
  Claude AI's dedicated upload/output handling directory.

Researchers noted the malware "leaked details of the GitHub account,
including its private token" (paraphrased to under 15 words per Hard
Rule 6). This OPSEC failure (token value not recorded per Hard Rule
7) signals lower-tier operator skill — distinct from TeamPCP-tier
tradecraft where the GitHub-author-spoofing and C2 PBKDF2-salt + locale-
check tradecraft is well-instrumented.

## Attribution disposition (Hard Rule 2 preserved)

OX Security **explicitly declines** attribution to any tracked actor.
The researchers characterize the campaign as part of a broader trend
(under-15-word paraphrase from THN relay): "the bar to create
malicious code [was] reduced significantly... more threat actors
getting into the game."

The cluster is **lineage-adjacent** to corpus VT-006 Mini Shai-Hulud
/ TeamPCP on a shared technical primitive (GitHub-token-based exfil
via postinstall stage of an npm package targeting AI-developer-
adjacent ecosystem) but differs on every other dimension (worm
class, attestation breaking, C2 layer, locale check, GitHub spoof
sophistication, OPSEC, scale, maintainer-network propagation). Per
Hard Rule 2, no cross-walk from `mouse5212-super-formatter` to
TeamPCP / Mini Shai-Hulud / Shai-Hulud / GlassWorm / Megalodon. OX
Security's explicit-decline is preserved verbatim per relay layer.

## A&D relevance

**LOW-INDIRECT.** Anthropic Claude AI is the targeted application; not
A&D-prime SDLC software per se. However, the corpus has previously
flagged AI-coding-agent SDLC compromises as **structural supply-chain
warning class** for A&D-developer-population indirect exposure. This
finding joins that thematic arc as **fifth-in-class** since 2026-05-12:

1. Mini Shai-Hulud (TanStack @squawk implicating aviation namespace)
2. Nx Console (Claude Code configurations exfil)
3. OpenAI TanStack-breach self-disclosure
4. SymJack (Claude Code symlink hijack)
5. MSTIC AI-chatbot-SEO-cryptojack (ScreenConnect)
6. **mouse5212-super-formatter** (Claude AI user-data directory exfil)

The cumulative pattern: "AI-developer-tooling-ecosystem is under
sustained supply-chain pressure" — increasingly relevant for any A&D-
prime program using Claude Code or Anthropic API directly within
ITAR-regulated SDLC boundaries.

## IOCs surfaced

See `iocs_surfaced` frontmatter block:
- `mouse5212-super-formatter` (npm package)
- `github.com/unplowed3584` (attacker GitHub account, suspended)
- "Malware-Slop" (researcher-coined working name)
- `/mnt/user-data` (target directory path)

## Relationship to existing findings

- **finding-2026-05-12-FLASH-0001 / VT-006** (Mini Shai-Hulud TeamPCP)
  — lineage-adjacent on technical-primitive layer ONLY; no attribution
  cross-walk per Hard Rule 2.
- **finding-2026-05-14-0008** (OpenAI TanStack supply-chain breach
  self-disclosure) — thematic arc.
- **finding-2026-05-20-FLASH-0001** (GitHub Nx Console 3,800-repo
  breach) — thematic arc.
- **finding-2026-05-27-0003** (SymJack symlink hijack against AI
  coding agents — AM-27) — thematic arc same brief day.
- **finding-2026-05-27-0005** (MSTIC cryptojacking ScreenConnect
  AI-chatbot SEO poisoning — AM-27) — thematic arc same brief day.

## Open questions for analyst / vuln-tracker / librarian

**Librarian handoff:**
1. Add IOCs to `_master-index.yaml` per `iocs_surfaced` block.
2. OX Security direct-retrieval verification has been pending since
   2026-05-15. This is the second corpus surface (Megalodon
   finding-2026-05-26 was the first) where OX Security primary
   research is relayed without direct corpus retrieval. Recommend
   operator decision: either (a) clear the awaiting_direct_retrieval
   flag via direct WebFetch of ox.security/blog/ on next scheduled
   cycle, or (b) downgrade ox-security provisional grade from B to C
   if direct-retrieval gap persists past 2026-06-01.

**No vuln-tracker handoff** (no CVE).
**No actor-profiler handoff** (OX Security explicit attribution
decline; no roster candidate).
**No analyst SAT-ACH / SAT-KAC** (single uncorroborated B source;
WEP ceiling held at "likely" for backward-looking factual claims).

## Hard Rules compliance

- **Rule 2 (no attribution origination):** OX Security explicit
  decline preserved; no cross-walk despite tradecraft adjacency.
- **Rule 3 (no exploitation):** Mechanism described at architectural
  level only — no working payload reproduced, no PoC content.
- **Rule 6 (15-word quote limit):** Researchers' characterization
  paraphrased to under 15 words.
- **Rule 7 (credentials):** Researchers reported "leaked GitHub
  private token" surfaced in the malware. Token value NOT recorded
  per Hard Rule 7. Only the existence-of-token-leak is documented.
- **Rule 8 (Splunk first-party):** Targeted -9h@h sweep on
  mouse5212-super-formatter / unplowed3584 / /mnt/user-data /
  Malware-Slop returned ZERO non-archimedes-internal events. 67th
  consecutive dormant non-self sweep on defenseclaw_local.
