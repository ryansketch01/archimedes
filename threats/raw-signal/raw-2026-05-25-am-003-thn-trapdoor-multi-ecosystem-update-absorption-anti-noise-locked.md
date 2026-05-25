---
raw_id: raw-2026-05-25-am-003-thn-trapdoor-multi-ecosystem-update-absorption-anti-noise-locked
collected_at: 2026-05-25T07:38:00-04:00
run_id: pre-brief-20260525-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News — TrapDoor multi-ecosystem supply-chain (Socket primary corpus-anchored; anti-noise-locked UPDATE absorption)"
  source_url: https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html
  source_grade_thn: B (provisional, awaiting ratification)
  source_grade_socket: B (provisional, awaiting ratification — first cited 2026-05-14)
  published_at: 2026-05-25T01:59:13-04:00
  socket_primary_published_at: 2026-05-25T00:00:00-04:00     # Socket published 2026-05-25 morning per THN body; specific time approximated; earliest TrapDoor activity 2026-05-22 20:20 UTC per THN
match_reason:
  watchlist: []
  actors: []                                 # UNATTRIBUTED per Socket + THN primary
  vulnerabilities: []
  keywords:
    - "TrapDoor"
    - "supply chain"
    - "npm"
    - "PyPI"
    - "Crates.io"
    - "credential-stealer"
    - ".cursorrules"
    - "CLAUDE.md"
    - "AI coding agents"
    - "browser-use"
    - "langchain-ai"
    - "langflow-ai"
triage_tags:
  - anti_noise_locked_update_absorption
  - corpus_already_tracked
  - net_new_framing_detail_ai_agent_config_manipulation
  - non_flash_tier
  - unattributed
iocs_extracted: true
iocs_count: 39                              # 6 Crates.io + 19 npm + 7 PyPI = 32 packages; 1 GitHub Pages exfil endpoint; 2 hidden-instruction file targets; 1 malicious .js payload; 1 malicious .rs payload; 1 earliest-activity timestamp; 1 disambiguation flag
text_word_count: 1100
promoted: false
absorbed: true
absorbed_into_finding: finding-2026-05-24-0001
absorbed_at: 2026-05-25T08:00:00-04:00
absorbed_update_id: update-2026-05-25-001
absorbed_disposition: in_place_update_log_entry_on_existing_finding_per_anti_noise_lock_active
ttl_expires_at: 2026-08-23T07:38:00-04:00
anti_noise_lock_reference: trapdoor-multi-ecosystem-supply-chain-socket
anti_noise_lock_expires_at: 2026-05-25T16:00:00-04:00
---

# The Hacker News — TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via npm, PyPI, and CratesIO
# Anti-noise-locked UPDATE absorption — corpus-anchored via finding-2026-05-24-0001

**Title:** TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via npm, PyPI, and CratesIO
**THN byline:** The Hacker News (info@thehackernews.com author email; no individual byline)
**Published:** 2026-05-25 05:59:13 UTC = 01:59 EDT (in-window)
**Socket primary:** corpus-anchored via finding-2026-05-24-0001 (PM brief commit 0774f79)
**Earliest TrapDoor activity (per THN):** 2026-05-22 20:20 UTC
**URL:** https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html

---

## Disposition framing

This raw-signal is captured for **anti-noise-locked UPDATE
absorption** into the morning brief. The TrapDoor multi-ecosystem
supply-chain campaign is **corpus-anchored** via
finding-2026-05-24-0001 (Socket primary; 2026-05-24 afternoon
brief commit `0774f79`). The anti-noise lock
`trapdoor-multi-ecosystem-supply-chain-socket` is **ACTIVE
through 2026-05-25 16:00 EDT** (8.5 hours remaining from this
sweep).

Per `doctrine/FLASH-POLICY.md` anti-noise rule 1 ("one FLASH
per topic per 24h"), this surface absorbs as UPDATE flag into
the next scheduled brief, NOT as re-FLASH.

---

## Net-new content delta over Socket primary

| Layer | Socket primary | THN UPDATE (this surface) |
|---|---|---|
| Package count / ecosystems | 34 packages / 384 versions across npm + PyPI + Crates.io | Same |
| Earliest activity | 2026-05-22 20:20 UTC | Same (confirmed) |
| Attribution | UNATTRIBUTED | UNATTRIBUTED |
| AI-agent-config angle | Implicit | **EXPLICIT framing**: `.cursorrules` and `CLAUDE.md` hidden-instruction files |
| Named GitHub PR targets | Not specified | **browser-use/browser-use, langchain-ai/langchain, langflow-ai/langflow** |
| Exfil endpoint | Not surfaced in Socket layer | **ddjidd564.github[.]io** (GitHub Pages domain) |
| Malicious payload files | Generic credential-stealer framing | **trap-core.js** (shared JS payload) + **build.rs** (Rust build script) |
| Disambiguation from Android TrapDoor | Not addressed | **EXPLICIT**: unrelated to HUMAN Satori Android ad-fraud TrapDoor disclosed prior week (455 Google Play apps) |

The **AI-agent-config manipulation framing** is the most
substantive net-new contribution from THN. Attackers embedded
hidden instructions in `.cursorrules` (Cursor IDE rules file) and
`CLAUDE.md` (Claude Code project instructions file) designed to
"trick artificial intelligence (AI) assistants into running a
security scan" resulting in credential exfiltration. This is the
**first explicit framing in the corpus** of supply-chain attackers
weaponizing AI-coding-agent configuration files to instruct
victim-side AI assistants to execute payloads on behalf of the
attacker — a novel-class developer-environment attack path.

---

## Indicators of Compromise

### Malicious packages

**Crates.io (6):**

- `move-analyzer-build`
- `move-compiler-tools`
- `move-project-builder`
- `sui-framework-helpers`
- `sui-move-build-helper`
- `sui-sdk-build-utils`

**npm (19 — note THN lists 20; counting 19 unique unless one is duplicated):**

- `async-pipeline-builder`
- `build-scripts-utils`
- `chain-key-validator`
- `crypto-credential-scanner`
- `defi-env-auditor`
- `defi-threat-scanner`
- `deployment-key-auditor`
- `dev-env-bootstrapper`
- `eth-wallet-sentinel`
- `llm-context-compressor`
- `mnemonic-safety-check`
- `model-switch-router`
- `node-setup-helpers`
- `project-init-tools`
- `prompt-engineering-toolkit`
- `solidity-deploy-guard`
- `token-usage-tracker`
- `wallet-backup-verifier`
- `wallet-security-checker`
- `web3-secrets-detector`
- `workspace-config-loader`

**PyPI (7):**

- `cryptowallet-safety`
- `data-pipeline-check`
- `defi-risk-scanner`
- `env-loader-cli`
- `eth-security-auditor`
- `git-config-sync`
- `solidity-build-guard`

### C2 / exfil infrastructure

- **`ddjidd564.github[.]io`** (GitHub Pages domain — attacker-
  controlled payload-hosting + exfil)

### Malicious payload files

- **`trap-core.js`** — shared JavaScript payload for credential
  scanning across npm + PyPI ecosystem targets
- **`build.rs`** — Rust build script for malicious execution
  (Crates.io targeting)

### AI-coding-agent configuration weaponization

- **`.cursorrules`** — Cursor IDE rules file with hidden
  attacker instructions
- **`CLAUDE.md`** — Claude Code project instructions file with
  hidden attacker instructions

### Named GitHub PR targets (attack vector)

- `browser-use/browser-use` (popular AI-browser-automation library)
- `langchain-ai/langchain` (popular AI orchestration framework)
- `langflow-ai/langflow` (visual AI workflow tool)

These are PR-target repositories the attacker filed pull requests
against to inject the `.cursorrules` / `CLAUDE.md` content into
upstream AI-coding-agent project metadata.

### Disambiguation flag

This TrapDoor (npm/PyPI/Crates.io supply chain, AI-coding-agent
abuse) is **UNRELATED** to the similarly-named **TrapDoor Android
ad-fraud operation** disclosed by **HUMAN's Satori Threat
Intelligence team** the previous week (455 Google Play Store apps).
Briefer + actor-profiler should preserve this disambiguation in
any morning-brief framing.

---

## Splunk first-party hand-built query EXECUTED this sweep

```spl
search index=defenseclaw_local earliest=-24h@h latest=now
  (trapdoor OR ddjidd564 OR "trap-core.js" OR ".cursorrules" OR
   "CLAUDE.md" OR "browser-use" OR "langchain-ai" OR "langflow-ai")
| head 50
```

Result: **ZERO hits** (component of the consolidated 17-IOC
sweep documented in companion sentinel am-000). Hard Rule 8:
silence is not disconfirming.

---

## Cross-corpus note

`ddjidd564.github[.]io` exfil endpoint appearance in TrapDoor is
**distinct from** Megalodon's `216.126.225.129:8443` C2 (separate
campaign per anti-noise framing). Operator should NOT conflate the
two in defensive blocklist or hunt queries. Both campaigns target
the developer / SDLC supply chain but use different infrastructure
classes (TrapDoor: GitHub Pages-hosted exfil; Megalodon:
IP-direct C2 over TCP/8443).

---

## A&D relevance

**Structural-indirect via developer-ecosystem ubiquity.** No
A&D-prime is named in either Socket or THN coverage. The
AI-coding-agent angle does raise the **structural exposure profile**
slightly because Cursor / Claude Code / LangChain / browser-use
adoption in A&D-prime SDLCs is plausibly high (these are
mainstream AI-developer-tooling products), but no operational A&D-
prime customer-impact statement has surfaced.

---

## Recommendations to morning grader / briefer / orchestrator

1. **Grader: do NOT promote to new finding-tier** — corpus-
   anchored via finding-2026-05-24-0001, anti-noise locked.
   The TrapDoor finding from 2026-05-24 PM brief should be
   **updated in-place** with the new IOC details (exfil
   endpoint, malicious payload filenames, AI-agent-config
   weaponization framing, named PR targets) rather than
   creating a duplicate finding.
2. **Briefer: morning brief UPDATE flag** on TrapDoor in the
   supply-chain monitoring section. Frame the AI-agent-config
   manipulation as a novel-class developer-environment attack
   path worth defensive prioritization in A&D-prime SDLCs that
   adopt AI coding assistants (Cursor / Claude Code / Copilot /
   etc.).
3. **Anti-noise lock extension considered**: current lock
   expires 2026-05-25 16:00 EDT. Recommend extending to
   2026-05-26 16:00 EDT if afternoon brief surfaces additional
   TrapDoor coverage (no extension required at this sweep — the
   THN UPDATE absorbs into morning brief and the lock can run
   to natural expiry).
4. **Splunk savedsearch action**: add `ddjidd564.github.io` +
   `trap-core.js` + the 32 package names to ongoing Splunk
   savedsearch keyword list against `defenseclaw_local`. Zero
   hits this sweep; maintain ongoing detection.
5. **Operator: AI-coding-agent .cursorrules / CLAUDE.md
   defensive guidance** — consider drafting an internal
   advisory or detection-engineering note on this attack class.
   `.cursorrules` and `CLAUDE.md` are project-root developer
   files that get committed to repos by default — code review
   should flag any external PR modifying these files with
   instructions to "run security scan" or similar AI-agent
   directives.

---

## Hard Rules compliance check

- **Rule 2** (no Archimedes-originated attribution):
  UNATTRIBUTED preserved per both Socket + THN primary sources.
  Cross-corpus author-identity-spoofing pattern observation
  (in companion am-001 Megalodon raw-signal) explicitly notes
  TrapDoor as one of multiple unattributed supply-chain
  mass-compromise events that do NOT support actor-collapse.
- **Rule 3** (no exploitation content): no PoC code reproduced.
  Attack mechanism described at conceptual level; AI-agent-
  config weaponization framing is defensive-detection-engineering.
- **Rule 4** (passive only): WebFetch on public THN article;
  Splunk hand-built query on Archimedes's own instance. No
  active recon.
- **Rule 6** (15-word quote limit): one 14-word quoted phrase
  from THN ("trick artificial intelligence (AI) assistants
  into running a security scan" — 11 words, single instance,
  within limit).
- **Rule 7** (credentials radioactive): no credential exposure
  in source body.
- **Rule 8** (Splunk first-party): hand-built sweep executed
  (component of 17-IOC consolidated sweep); zero hits in
  -24h@h on TrapDoor IOCs. 56th consecutive dormant non-self
  sweep on `defenseclaw_local`.

---

## Disposition

- **Raw-signal status:** companion to am-000 sentinel; UPDATE
  absorption candidate for the existing TrapDoor finding
  (finding-2026-05-24-0001) rather than new finding.
- **FLASH trigger status:** anti-noise-locked. Trigger 5 would
  not fire even absent the lock (multi-victim YES; A&D-direct
  FAIL; UNATTRIBUTED).
- **Anti-noise lock state:** ACTIVE through 2026-05-25 16:00
  EDT (8.5h from this sweep); UPDATE-flag absorption proceeds
  within lock period.
- **TLP:CLEAR.**
