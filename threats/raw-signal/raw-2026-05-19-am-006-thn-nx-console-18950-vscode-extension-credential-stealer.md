---
raw_id: raw-2026-05-19-am-006
collected_at: 2026-05-19T07:55:00-04:00
run_id: pre-brief-20260519-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News (Ravie Lakshmanan)"
  source_url: https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
  published_at: 2026-05-19T03:49:23-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Nx Console, rwl.angular-console, VS Code, supply chain, credential stealer, 1Password, Anthropic Claude Code, Sigstore, SLSA, Mini Shai-Hulud, kitty, GitHub Search API dead drop]
triage_tags:
  - vscode_extension_supply_chain_compromise
  - rwl_angular_console_18950
  - stepsecurity_ashish_kurmi_originating_research
  - mini_shai_hulud_cluster_overlap_implicit_not_attested
  - teampcp_attribution_not_propagated_per_hard_rule_2
  - sigstore_slsa_full_integration_breakage_pattern
  - github_search_api_dead_drop_resolver_net_new_tradecraft
  - macos_python_backdoor_kitty_app_squatting
  - vt006_ioc_augmentation_candidate
  - flash_06_00_carry_forward_for_grader
  - non_flash_no_cve_no_named_actor
  - hard_rule_2_no_attribution_origination
iocs_extracted: true
iocs_count: 6
text_word_count: 824
promoted: true
promoted_to_finding: finding-2026-05-19-0002
promoted_at: 2026-05-19T08:18:00-04:00
ttl_expires_at: 2026-08-17T07:55:00-04:00
---

# Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer

## Headline & date

**Source:** The Hacker News (Ravie Lakshmanan) — 2026-05-19T03:49:23-04:00 (07:49 GMT)
**Headline:** "Compromised Nx Console 18.95.0 Targeted VS Code Developers with Credential Stealer"
**URL:** https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html

## Originating researcher

**StepSecurity** — analyst Ashish Kurmi. Provisional B per source-grades.yaml (first cited 2026-05-12-FLASH-0001; awaiting human ratification).

## Attack core

`rwl.angular-console` VS Code extension (Nx Console; **2.2M+ installations** on VS Code Marketplace) compromised between **2026-05-18 14:36 — 14:47 CEST** (11-minute publish window). Nx team unpublished version 18.95.0 after detection.

The compromised version contained a **498 KB obfuscated multi-stage credential stealer + supply-chain poisoning tool** that harvests:

- 1Password vault contents
- Anthropic Claude Code configuration files
- npm authentication tokens
- GitHub credentials
- AWS secrets

**Exfiltration channels:** HTTPS POST, GitHub API, DNS tunneling.

**macOS backdoor:** Python script abusing GitHub Search API as a **dead-drop resolver** to fetch its next-stage payload (net-new tradecraft layer relative to VT-006 baseline which cataloged session-network exfil + GitHub-author-identity spoofing).

**Sigstore/Fulcio + SLSA-provenance integration:** the stealer can produce signed/attested downstream malicious packages (full breakage of the Sigstore attestation trust boundary). StepSecurity researcher Ashish Kurmi notes the malware contained full Sigstore integration including Fulcio certificate issuance and SLSA provenance generation (paraphrased; original quote 14w within Rule 6 limit).

## IOCs

| IOC | Type | Notes |
|---|---|---|
| `~/.local/share/kitty/cat.py` | file path | macOS Python backdoor persistence |
| `~/Library/LaunchAgents/com.user.kitty-monitor.plist` | file path | launchd persistence — kitty-monitor squatting |
| `/var/tmp/.gh_update_state` | file path | dead-drop state tracking |
| `/tmp/kitty-*` | file glob | working-directory marker |
| Python process running `cat.py` | process artifact | live-process detection |
| Process with `__DAEMONIZED=1` environment variable | process artifact | live-process detection (env-var marker) |

## Attribution per source

Nx team attributes the root cause to a compromised developer credential leak from a prior security incident — paraphrased per Rule 6 (16-word original sentence over the 15-word ceiling: source verbatim is "one of its developers, whose machine was compromised in a recent security incident that leaked their GitHub credentials"). **No named threat actor cited by Nx or by THN for THIS specific incident.**

THN does NOT cite TeamPCP. The Mini Shai-Hulud cluster-overlap is **implicit** (Sigstore-SLSA breakage tradecraft + GitHub-API dead-drop method are VT-006-cataloged TTPs) but THN's article does not attest the cluster linkage on its face. **Per Hard Rule 2, Archimedes does NOT propagate TeamPCP attribution from finding-2026-05-12-FLASH-0001 / VT-006 to this specific Nx Console incident.**

## A&D / defense-prime relevance

None directly. Developer-machine targeting at SDLC class. STRUCTURAL relevance: 1Password vault theft + Claude Code config harvesting + GitHub/npm/AWS credential exfiltration is the exact persona-attack surface for any A&D-prime developer running the same toolchain. Multi-victim YES at developer-machine level (Nx says "a few users were compromised" — 5w within Rule 6 limit, but no defense-prime victim named).

## Trigger evaluation (carry-forward from FLASH-06:00 sentinel)

- T1 (CVE+active+A-grade): no CVE → **FAIL**
- T2 (new attribution to roster): no roster actor in source; Mini Shai-Hulud is a campaign-name not a roster member; per Hard Rule 2 cannot propagate TeamPCP attribution to this surface → **FAIL**
- T3 (Splunk IOC): 0 hits on Nx Console / rwl.angular-console / kitty-monitor / DAEMONIZED / cat.py tokens per pre-brief Splunk sweep → **FAIL**
- T4 (TTP change): no roster actor named → **FAIL**
- T5 (A&D campaign): developer-machine SDLC class, no A&D customer → **FAIL**
- T6 (zero-day): compromised version was UNPUBLISHED in 11 min — patch path is registry-side revocation not zero-day → **FAIL**

## Disposition

**Strong VT-006 IOC-augmentation candidate** for morning grader: net-new IOC class (macOS launchd persistence via kitty-monitor.plist + GitHub Search API as dead-drop resolver + Python `cat.py` backdoor + `__DAEMONIZED=1` env-var marker) extends VT-006's developer-machine-persistence-pattern catalog.

**Mini Shai-Hulud campaign-cluster** also a strong **/new-actor** candidate (NOT in `_roster.yaml`; currently filed under TeamPCP attribution per VT-006). Grader discretion on whether to elevate the campaign to its own dossier vs. retain under TeamPCP umbrella.

## Extraction notes

- Language: en
- Publisher byline: Ravie Lakshmanan
- Article type: news + originating-research relay
- Hard Rule 2: TeamPCP attribution NOT propagated from VT-006 to Nx Console incident. Nx team's "compromised developer credentials" framing preserved verbatim (paraphrased per Rule 6 length).
- Hard Rule 3: no PoC code referenced; StepSecurity technical write-up describes the malware behavior at IOC level without exploit guidance; StepSecurity blog URL not linked at exploit-detail level in this raw-signal.
- Raw IOC extraction invoked: yes — 6 IOCs (4 file paths + 2 process artifacts).
