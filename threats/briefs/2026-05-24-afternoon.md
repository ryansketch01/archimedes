---
brief_id: 2026-05-24-afternoon
brief_type: afternoon
published_at: 2026-05-24T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_required_wep_ceiling_likely_below_very_likely_threshold
human_override: null
status: published
run_id: afternoon-20260524-160000
word_count: 728
findings_referenced:
  - finding-2026-05-24-0001
carry_forwards_referenced:
  - cve-2026-9082-drupal-kev-due-date-t-3
  - cve-2026-42897-exchange-kev-due-date-t-5
related_vulns:
  - CVE-2026-9082
  - CVE-2026-42897
related_actors: []
related_zero_days: []
related_campaigns:
  - trapdoor-multi-ecosystem-supply-chain-2026
tlp: CLEAR
---

# Afternoon Brief — 2026-05-24

**Cursor and Claude Code users: a new supply-chain campaign writes malicious instructions into `.cursorrules` and `CLAUDE.md` for persistence.** Socket disclosed TrapDoor today — 34 typo-squat packages across npm + PyPI + Crates.io (384 versions, one attacker identity) carrying an XOR-obfuscated stealer that targets crypto/DeFi/AI/security developers. UNATTRIBUTED per Socket.

**Why it matters:** No A&D prime is named as victim. Sub-tier exposure runs through any A&D developer workstation running Cursor or Claude Code on a package whose dependency tree intersects the 34 named packages. The defender action — audit `.cursorrules` and `CLAUDE.md` for instructions the developer didn't write — is attribution-independent.

---

## 🚨 Active Threats

**TrapDoor multi-ecosystem supply-chain campaign — first Crates.io surface in the Archimedes corpus this year; novel AI-agent-config persistence vector**
- What: Socket Research Team disclosed a coordinated campaign of 34 malicious packages and 384 versions published over ~50 hours starting 2026-05-22 across npm (21), PyPI (7), and Crates.io (6). One attacker identity links all three ecosystems: GitHub `ddjidd564` (also hosts the GitHub Pages dead-drop `ddjidd564.github.io/defi-security-best-practices/`) and npm `asdxzxc`. Payload is `trap-core.js` (48,485 bytes, XOR key `cargo-build-helper-2026`, internal campaign marker `P-2024-001`). Persistence mixes `.cursorrules` and `CLAUDE.md` AI-agent-config-file injection with Git hooks, shell hooks, systemd units, cron, and SSH. Credential-exfil scope spans SSH keys, Sui/Solana/Aptos wallets, AWS, GitHub tokens, browser data, environment variables, API keys, and local dev configs.
- Why it matters for A&D: Structural-indirect only. No A&D-prime named as victim; target sectors are crypto/DeFi/Move-language/AI/security developers. Sub-tier exposure pathway runs through A&D developers using Cursor or Claude Code on workstations whose dependency trees touch any of the 34 named packages. The `.cursorrules` + `CLAUDE.md` persistence vector is the first such observation in the Archimedes corpus this year and is actionable regardless of attribution.
- Defender action: Audit `.cursorrules` and `CLAUDE.md` across developer workstations for instructions the developer did not author; inventory dependency trees against Socket's 34-package list; block traffic to `ddjidd564.github.io`; hunt for `trap-core.js` and the campaign marker `P-2024-001` in egress proxies and EDR.
- Source: [Socket](https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates) · Digraph: B2 · WEP: likely (single-source veto applies — see analyst caveats)
- Hard Rule 2: **Socket explicitly declines attribution and specifically rules out TeamPCP / Shai-Hulud / Mini Shai-Hulud. Archimedes does not originate any cross-walk to tracked roster actors. The attacker-self-described "Universal AI Agent Extraction Framework" framing is the attacker's own payload-embedded text, preserved verbatim per Hard Rule 2 — not a Socket attribution and not an Archimedes attribution.**
- Analyst caveats: Three load-bearing assumptions qualified — (1) Socket-source-faithful-relay (no second A/B-grade vendor independently analyzed the 34-package cluster within sweep); (2) Socket's not-TeamPCP framing methodology (negative attribution asserted, specific evidence basis not published); (3) `.cursorrules` + `CLAUDE.md` novelty is **first-in-the-Archimedes-corpus-this-year**, NOT first-in-the-wild (Socket has not framed it as wild-novel). Related: finding-2026-05-24-0001.

## 🔓 Vulnerabilities

**KEV deadline countdowns — no change to substance, status reinforcement only**
- **CVE-2026-9082 (Drupal Core SQLi, PostgreSQL path) — federal due Wednesday 2026-05-27 (T-3, ~63h).** Status unchanged from this morning's brief; patch-coverage confirmation on DIB-adjacent marketing microsites, contractor portals, and third-party vendor pages remains the action.
- **CVE-2026-42897 (Exchange OWA XSS) — federal due Friday 2026-05-29 (T-5, ~111h).** No MSRC GA patch in this sweep; MSRC blog surface continues template-only / 403. ESU + EEMS / EOMT mitigation path unchanged. Active-exploitation single-source veto on MSRC originating tag still holds — Mandiant, Volexity, Unit 42, MSTIC TI blog, and CrowdStrike silent on corroborating telemetry through this sweep.
- Source: [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A1 (KEV listings) · WEP: very likely (deadline-as-stated)

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific cyber threats against watchlist companies in the 8h reporting window. This morning's [Russian Kosmos 2610–2613 orbital-proximity event vs. ICEYE-X36](2026-05-23-morning.md) (carried from 2026-05-23) stands without development. Tracked A&D-targeting actors ([APT28](../threat-actors/APT28/profile.md), [UNC1549](../threat-actors/UNC1549/profile.md), Lazarus, APT41, Salt Typhoon) silent.

## 🕵️ Actor Activity

No new attributed actor activity in the 8h window. TrapDoor (above) is UNATTRIBUTED per Socket's explicit decline; not propagated to any tracked roster actor. This morning's [UNC1151 / Ghostwriter UPDATE](2026-05-24-morning.md) (third multi-A-grade surface in 14 days) stands without development; `/new-actor` candidacy remains at operator discretion.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors ([UNC1549](../threat-actors/UNC1549/profile.md), [Charming Kitten](../threat-actors/Charming-Kitten/profile.md), Handala Hack, [MuddyWater](../threat-actors/MuddyWater/profile.md)) in the last 48h.

## 📰 Other Signal

**Supply-chain campaign density — five distinct campaigns across 14 days.** TrapDoor is the fifth distinct supply-chain campaign in 14 days (Mini Shai-Hulud → node-ipc → Laravel-Lang → Packagist 8-pkg → TrapDoor), and the third Socket-anchored disclosure in 8 days. Researcher-attention-effect caveat (inherited from yesterday's afternoon ACH): independent A/B-grade vendor entry on TrapDoor within 48h is the natural test of whether the density reflects underlying threat-landscape tempo or Socket's analytic concentration. Watch Snyk, Wiz, Aikido, StepSecurity, SafeDep, Unit 42, Ox Security, Upwind, and Checkmarx for next-sweep corroboration. Sunday Weekly Synthesis (10:00 EDT, T+18h from this brief, already published) consolidated the first four campaigns; TrapDoor enters as the fifth data point for next week's synthesis.

**Post-window claim layer flagged for next-sweep verification (not in this brief):** Socket's @SocketSecurity follow-up post at 17:29 EDT (post-window) referenced attempted-injection of `.cursorrules` / `CLAUDE.md` into upstream `modelcontextprotocol` and `gemini-cli` repos. Not retrievable in this 8h sweep; held for 2026-05-25 morning collection to substantiate via commit URLs, PR/issue links, or upstream-repo disclosure.

**First-party Splunk (Hard Rule 8):** Grader-executed query across `archimedes` and `defenseclaw_local` over -30d for the full 9-IOC TrapDoor set (ddjidd564, asdxzxc, trap-core.js, cargo-build-helper-2026, P-2024-001, ddjidd564.github.io, defi-security-best-practices, "Universal AI Agent Extraction Framework", TrapDoor) returned zero genuine hits. Both indexes remain in dormant non-self sweep posture (53rd consecutive dormant sweep per the PM sentinel). Silence is not disconfirming.

---

*Sources hyperlinked inline. Digraph per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-05-24.

🚨 **Active Threats**

• **[TrapDoor — supply-chain stealer drops malicious `.cursorrules` and `CLAUDE.md` for persistence](https://socket.dev/blog/trapdoor-crypto-stealer-npm-pypi-crates)** — Socket disclosed today: 34 typo-squat packages across npm + PyPI + Crates.io, 384 versions, one attacker identity (GitHub `ddjidd564`, npm `asdxzxc`) shipping an XOR-obfuscated `trap-core.js` stealer since May 22. Targets crypto/DeFi/AI/security developers — no A&D prime named. *Cursor and Claude Code users: audit `.cursorrules` and `CLAUDE.md` for instructions you didn't write, right now.* **Socket explicitly declines attribution and rules out TeamPCP / Shai-Hulud / Mini Shai-Hulud; Archimedes does not originate.** First Crates.io surface in the corpus this year — bounded by corpus coverage, not framed as first-in-the-wild.

🔓 **Vulnerabilities**

• **CVE-2026-9082 (Drupal Core SQLi):** federal patch due **Wednesday May 27** (~63h). Status unchanged. *Confirm Drupal/PostgreSQL coverage on contractor portals and third-party vendor pages.*
• **CVE-2026-42897 (Exchange OWA XSS):** federal patch due **Friday May 29** (~111h). No MSRC GA patch yet; ESU + EEMS / EOMT mitigation path holds. *Mandiant, Volexity, Unit 42, MSTIC, CrowdStrike all silent on active-exploitation corroboration — single-source veto on MSRC continues.*

📰 **Other Signal**

• **Supply-chain density: 5 distinct campaigns in 14 days, 3 Socket-anchored in 8.** Independent A/B-grade vendor entry on TrapDoor within 48h is the test of whether the density reflects landscape tempo or Socket's analytic concentration.
