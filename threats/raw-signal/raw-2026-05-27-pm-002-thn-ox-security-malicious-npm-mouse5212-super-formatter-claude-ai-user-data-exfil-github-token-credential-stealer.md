---
raw_id: raw-2026-05-27-pm-002
collected_at: 2026-05-27T15:40:00-04:00
run_id: pre-brief-20260527-pm
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html
  source_grade: B (provisional)
  source_grade_basis: thehackernews provisional B per source-grades.yaml awaiting human ratification; relay-tier of OX Security primary research
  primary_source_yaml_id: ox-security
  primary_source_name: OX Security
  primary_source_grade: B (provisional)
  primary_source_grade_basis: ox-security provisional B per source-grades.yaml 2026-05-15 first-citation; awaiting human ratification and direct-retrieval verification
  primary_source_url_referenced: https://www.ox.security/ (full OX Security primary post URL not directly retrieved this sweep — only THN relay layer captured)
  published_at: 2026-05-27T15:44:29+00:00
  fetched_via: rss-bridge fetch_feed feedburner TheHackersNews
match_reason:
  watchlist: []
  actors:
    - "No tracked-actor attribution claimed by OX Security per THN relay. Researchers Moshe Siman Tov Bustan + Nir Zadok make NO attribution to TeamPCP / Shai-Hulud / Mini Shai-Hulud / GlassWorm lineage. Hard Rule 2 preserved: no cross-walk to tracked roster despite Anthropic-Claude AI-tool victim profile + GitHub-token-exfil tradecraft analogous to corpus VT-006 Mini Shai-Hulud."
  vulnerabilities: []
  keywords:
    - npm
    - mouse5212-super-formatter
    - Claude AI
    - Anthropic
    - /mnt/user-data
    - postinstall
    - GitHub token
    - github.com/unplowed3584
    - Malware-Slop
    - OX Security
    - supply-chain-attack-npm
    - credential-stealer-npm
    - AI-coding-agent-supply-chain
triage_tags:
  - pm_pre_brief_scheduled
  - supply_chain_attack_npm
  - ai_coding_agent_supply_chain_class
  - claude_ai_user_data_target
  - unattributed_supply_chain
  - low_severity_install_count_676
  - operational_security_failure_hardcoded_token_exposure
  - npm_postinstall_credential_stealer
  - mini_shai_hulud_lineage_adjacent_unattributed_explicit
iocs_extracted: true
iocs_count: 3
text_word_count: 850
promoted: true
promoted_to_finding: finding-2026-05-27-0008-ox-security-thn-mouse5212-super-formatter-npm-claude-ai-user-data-credential-stealer-unattributed
promoted_at: 2026-05-27T16:12:00-04:00
promoted_in_run: afternoon-20260527-160000
ttl_expires_at: 2026-08-25T15:40:00-04:00
---

# OX Security via THN — Malicious npm Package `mouse5212-super-formatter` Stole Anthropic Claude AI User Files via GitHub Token Exfil; Researchers Decline Attribution

OX Security researchers Moshe Siman Tov Bustan and Nir Zadok disclosed
a malicious npm package `mouse5212-super-formatter` designed to upload
files from Anthropic Claude AI's dedicated user-data directory
(`/mnt/user-data`) to a threat-actor-controlled GitHub account.
Disclosure surfaced today 2026-05-27 11:44 EDT via The Hacker News
relay; OX Security primary post URL not directly retrieved this sweep.

## Technical mechanism

The package disguises itself as "archive deployment sync" utility. The
malicious payload triggers in the **npm postinstall stage** (a
well-documented npm supply-chain attack class, used historically by
TeamPCP Shai-Hulud + Mini Shai-Hulud + corpus VT-006).

- Authenticates to GitHub using either a victim's environment token
  OR a hardcoded fallback token (so even environments without
  pre-existing GitHub credentials get exfiltrated).
- Recursively uploads local workspace files to the attacker-controlled
  GitHub account.
- Target directory: `/mnt/user-data` — Anthropic Claude AI's
  dedicated upload/output handling directory per OX Security's
  description.

## Attack infrastructure (IOCs)

- **Compromised GitHub account (attacker-controlled):**
  `github.com/unplowed3584` (no longer available; suspended or
  taken down).
- **Account creation date:** 2026-05-26 (day before the malicious
  package surface).
- **npm registry status (at OX Security disclosure):** package
  STILL AVAILABLE on npm registry at time of THN relay publication.

## Scale

- **Download count:** 676 (THN relay; actual installation count
  unclear — npm download counts include automated CI/CD scanners
  and crawlers).
- Campaign name: **"Malware-Slop"** (OX Security researcher-coined
  working name).

## Operational security failure (OPSEC)

Researchers noted the malware "leaked details of the GitHub account,
including its private token" (THN relay paraphrase; full OX Security
primary not directly retrieved). This is a notable OPSEC failure
signaling lower-tier operator skill — distinct from corpus VT-006
Mini Shai-Hulud TeamPCP attribution layer where the GitHub-author-
spoofing tradecraft is precise + the C2 PBKDF2-salt + Session-ID +
locale-check tradecraft is well-instrumented.

## Attribution disposition (Hard Rule 2 preserved)

OX Security explicitly **declines** to attribute the campaign to any
tracked actor. The researchers characterize this as part of a broader
trend (quote from THN relay, paraphrased to under 15 words):
"the bar to create malicious code [was] reduced significantly... more
threat actors getting into the game" — under-15-word interpretive
paraphrase of the researchers' positioning.

The campaign is **lineage-adjacent** to corpus VT-006 Mini Shai-Hulud /
TeamPCP based on a shared technical primitive (GitHub-token-based
exfil via postinstall stage of an npm package targeting AI-developer-
adjacent ecosystem) BUT differs on every other dimension:

| Dimension | corpus VT-006 / TeamPCP Mini Shai-Hulud | Today's OX Security `mouse5212-super-formatter` |
|---|---|---|
| Worm class | self-propagating, dual-ecosystem (npm + PyPI) | single-package, single-ecosystem (npm only) |
| Attestation breaking | SLSA attestation breaking | none (no attestation involvement) |
| C2 layer | session-network exfil + PBKDF2 + 6 C2 domains + 1 C2 IP + Session ID | GitHub-API-only exfil; no separate C2 |
| Locale check | Russian-locale guardrail | none |
| GitHub spoof | claude@users.noreply.github.com author spoof | github.com/unplowed3584 (clearly attacker-controlled, no spoofing) |
| OPSEC | high (PBKDF2 salt, locale check, attestation) | low (hardcoded token in code, leaked private token) |
| Scale | ~172 packages compromised | 1 package |
| Maintainer-network propagation | yes (worm-spread to TanStack + UIPath + Mistral + OpenSearch + Squawk maintainers) | no (single-author publication) |

Per Hard Rule 2, **no cross-walk** from `mouse5212-super-formatter` to
TeamPCP / Mini Shai-Hulud / Shai-Hulud / GlassWorm. OX Security's
explicit-decline-attribution is preserved verbatim per relay layer.

## A&D relevance

**LOW-INDIRECT.** Anthropic Claude AI is the targeted application; not
A&D-prime SDLC software per se. However, the corpus has previously
flagged AI-coding-agent SDLC compromises as **structural supply-chain
warning class** for A&D-developer-population indirect exposure (see
AM-27 finding-2026-05-27-0003 SymJack symlink-hijack against Claude
Code + Gemini + Cursor + Grok + Copilot + AM-27 finding-2026-05-27-
0005 MSTIC cryptojacking ScreenConnect AI-chatbot SEO poisoning +
finding-2026-05-14-0008 OpenAI TanStack-supply-chain-breach
self-disclosure layered class). This raw-signal joins that thematic
arc as **fifth-in-class** since 2026-05-12: Mini Shai-Hulud (TanStack
@squawk implicating aviation), Nx Console (Claude Code configurations
exfil), OpenAI TanStack-breach, SymJack (Claude Code symlink), MSTIC
AI-chatbot-SEO-cryptojack, and now `mouse5212-super-formatter`
(Claude AI user-data directory exfil).

The cumulative pattern is grader-side disposition: each individual
event is unattributed-low-severity but the THEMATIC layer is
"AI-developer-tooling-ecosystem is under sustained supply-chain
pressure" — increasingly relevant for any A&D-prime program using
Claude Code or Anthropic API directly within ITAR-regulated SDLC
boundaries.

## FLASH-trigger evaluation note

- **Trigger 1 (critical-cve-exploited):** no CVE assigned. FAIL.
- **Trigger 2 (tracked-actor-attribution):** OX Security declines
  attribution explicitly. FAIL.
- **Trigger 5 (ad-sector-campaign):** no A&D-prime victim named.
  Single-package single-author, not a multi-victim campaign. FAIL.
- **Trigger 6 (zero-day-no-patch):** N/A; this is malicious-package
  surfacing, not a CVE-class vulnerability.

This raw-signal is a **non-FLASH grader-queue item** — appropriate for
afternoon-brief structural-supply-chain-warning treatment, not for
FLASH-tier promotion.

## Source health

- `thehackernews`: fetch_feed succeeded 200 OK; 5 in-window items this
  sweep. `last_successful_fetch: 2026-05-27T15:40:00-04:00`. Healthy.
- `ox-security`: primary URL not directly retrieved this sweep; relay
  layer only. `awaiting_direct_retrieval: true` per source-grades.yaml
  state (since 2026-05-15 first-citation). Flagged for PM-27 brief
  workflow to consider on-demand direct retrieval of OX Security
  primary post URL.

## Hard Rules compliance

- **Rule 2 (no attribution origination):** OX Security's explicit
  decline preserved; no cross-walk despite tradecraft adjacency to
  corpus VT-006 / TeamPCP.
- **Rule 3 (no exploitation):** No PoC content. Mechanism described at
  architectural level only (postinstall + GitHub-API exfil) — no
  working payload reproduced.
- **Rule 4 (passive only):** WebFetch + fetch_feed only.
- **Rule 6 (15-word quote limit):** Researchers' characterization
  quote paraphrased to under 15 words.
- **Rule 7 (credentials):** Researchers reported "leaked GitHub
  private token" surfaced in the malware. **Token value NOT
  recorded** per Hard Rule 7. Only the existence-of-token-leak
  surfaced.
- **Rule 8 (Splunk first-party):** Targeted sweep on
  `mouse5212-super-formatter`, `unplowed3584`, `/mnt/user-data`,
  `Malware-Slop` token returned ZERO non-archimedes-internal events
  on `archimedes` + `defenseclaw_local` over -9h@h.

---

## IOCs (raw extraction)

```yaml
indicators:
  - type: npm_package
    value: "mouse5212-super-formatter"
    description: "Malicious npm package with postinstall credential-stealer payload targeting Claude AI /mnt/user-data directory"
    confidence: A (vendor-research-attested per OX Security primary via THN relay)
    first_seen: 2026-05-26 (account creation) / publication date unclear from THN relay
    source: OX Security via The Hacker News 2026-05-27
    attribution: UNATTRIBUTED (OX Security explicit decline)
  - type: github_account
    value: "github.com/unplowed3584"
    description: "Attacker-controlled GitHub account receiving exfiltrated files via API"
    status: "no longer available (suspended or taken down)"
    creation_date: 2026-05-26
    confidence: A
    source: OX Security via The Hacker News 2026-05-27
  - type: working_name
    value: "Malware-Slop"
    description: "OX Security researcher-coined working name for the campaign (not an attributed actor designation)"
    confidence: A (vendor-attested)
    source: OX Security via The Hacker News 2026-05-27

attribution_claims: []  # OX Security explicitly declines attribution

related_findings:
  - finding-2026-05-12-FLASH-0001  # Mini Shai-Hulud TeamPCP — lineage-adjacent on technical-primitive layer ONLY
  - finding-2026-05-14-0008        # OpenAI TanStack supply-chain breach self-disclosure
  - finding-2026-05-20-FLASH-0001  # GitHub Nx Console 3,800-repo breach
  - finding-2026-05-27-0003        # SymJack symlink hijack against AI coding agents
  - finding-2026-05-27-0005        # MSTIC cryptojacking ScreenConnect AI-chatbot SEO poisoning
```

## Notes

- Single B-grade primary (OX Security) via B-grade relay (THN).
  WEP ceiling at most `likely` per single-source-veto on attribution
  layer. Grader-side disposition.
- Suggested afternoon-brief treatment: include as cumulative-thematic
  bullet within the structural-supply-chain-warning section (alongside
  AM-27 findings 0003 + 0005 + carry-forwards from finding-2026-05-14-
  0008 / finding-2026-05-20-FLASH-0001). NOT a standalone PM-27
  finding promotion candidate at this surface.
- TLP:CLEAR.
