---
brief_id: 2026-05-05-afternoon
brief_type: afternoon
published_at: 2026-05-05T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: null
human_override: null
word_count: 694
findings_referenced:
  - finding-2026-05-05-0007
  - finding-2026-05-05-0008
  - finding-2026-05-05-0009
tlp: CLEAR
test: false
---

# Afternoon Brief — 2026-05-05

**MSTIC discloses an unattributed AitM "code of conduct" phishing campaign that hit 35,000 recipients across 13,000 organizations (92% US) in three days last month — same Entra session-token-theft mechanism class as this morning's Charming Kitten finding, distinct operator and pretext.**

**Why it matters:** Two separate clusters in 24 hours exploit the same gap — non-phishing-resistant MFA against a "Sign in with Microsoft" prompt. The compliance pretext routes naturally to ITAR-burdened legal, HR, and ethics-office staff at primes.

---

## Active Threats

**Microsoft MSTIC: multi-stage AitM phishing campaign hit 35K recipients / 13K orgs / 92% US in a three-day burst (April 14–16, 2026).** Per [Microsoft MSTIC and Defender Security Research](https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/), conduct-policy-themed PDFs route through Cloudflare-CAPTCHA staging into a "Sign in with Microsoft" reverse-proxy that exfiltrates the session token, bypassing non-phishing-resistant MFA. Microsoft names no actor or Storm-NNNN. Sectors named: healthcare (19%), financial services (18%), professional services (11%), tech (11%) — **defense, aerospace, and government are not on Microsoft's named-sectors list**. SecurityWeek's same-day relay adds no independent observation; single-source veto caps WEP at **likely**. Thirteen IOCs published — five attacker domains (`compliance-protectionoutlook.de`, `acceptable-use-policy-calendly.de`, `cocinternal.com`, `gadellinet.com`, `harteprn.com`), five sender addresses, three PDF SHA-256 hashes. First-party Splunk silent on all 13 over -30d. **A&D action:** push the 13 IOCs through SIEM/EDR for a -30d hunt; brief legal, HR, and ethics-office mailboxes — that is where the conduct-policy pretext lands. Digraph: A2 · WEP: likely · finding-2026-05-05-0007.

🔗 **Connects to:** [this morning's Charming Kitten / Mint Sandstorm OAuth campaign (finding-2026-05-05-0002)](2026-05-05-morning.md). Same Entra session-token-theft class — different operator, pretext, sectors, IOC sets. **Do not merge:** Charming Kitten is bounded to think tanks / Iran-nuclear researchers / MENA journalists at A1; this AitM cluster is unattributed at A2 against US healthcare / finance / professional / tech.

**DAEMON Tools trojanized in supply-chain attack — backdoor delivered via the official site since 2026-04-08; thousands of first-stage infections, selective second stage to ~12 victims.** Per [BleepingComputer](https://www.bleepingcomputer.com/news/security/daemon-tools-trojanized-in-supply-chain-attack-to-deploy-backdoor/), versions 12.5.0.2421 through 12.5.0.2434 carried trojanized `DTHelper.exe`, `DiscSoftBusServiceLite.exe`, `DTShellHlp.exe`. Operators filtered second-stage deployment to retail, scientific, government, and manufacturing victims in Russia, Belarus, and Thailand; QUIC RAT landed at one Russian educational institute. **No US victims and no aerospace or defense vertical named.** BleepingComputer reports unnamed researchers "believe the attacker is Chinese speaking" — recorded as the source's reported claim only; no roster actor invoked (Hard Rule 2). Single B-grade source; WEP capped at **likely**. No hashes / C2 / IPs published — hunt surface is filename and version-string only. **A&D action:** SCCM/Intune software-inventory query for DAEMON Tools 12.5.0.2421–12.5.0.2434 across the engineering / R&D bench-tool footprint; signed binaries from the legitimate vendor very likely flowed past EDR during the four-week active window. Digraph: B2 · WEP: likely · finding-2026-05-05-0008.

## Vulnerabilities

**Ollama CVE-2026-7482 "Bleeding Llama" — heap OOB read in GGUF loader, ~300K exposed instances, patched in 0.17.1; no exploitation observed.** Per [SecurityWeek](https://www.securityweek.com/critical-bug-could-expose-300000-ollama-deployments-to-information-theft/) relaying Cyera, an unauthenticated remote attacker triggers the read with a malicious GGUF file (declared tensor offset or size exceeds file length), then abuses Ollama's model-push to exfiltrate the resulting heap content — prompts, environment variables (API keys, tokens), recent user interactions, code under analysis. CVSS 9.3. Root cause is Ollama's default-bind-all-interfaces, no-auth-by-default posture; ~300K internet-reachable instances per Cyera (methodology not independently verified). SecurityWeek is single-effective relay (Cyera provisional C, not in source-grades.yaml); WEP caps at **likely**. **A&D action:** treat as a precautionary patch on a 14-day window, not an active-exploitation event. Inventory any Ollama listener (default port 11434) on RFC-1918 internal interfaces or externally reachable across self-hosted prime AI / R&D inference programs; patch to 0.17.1 or restrict to localhost behind an auth proxy. Digraph: B2 · WEP: likely · finding-2026-05-05-0009.

## Sector Focus: Aerospace & Defense

**Two new prime-relevant inventory hunts open this afternoon on top of the morning's three concurrent perimeter / management-plane patches.** DAEMON Tools 12.5.0.2421–12.5.0.2434 across the engineering / R&D bench-tool estate; Ollama listeners (port 11434) across self-hosted inference programs. MSTIC AitM IOCs queue as a SIEM/EDR hunt. None of the three new findings names a US prime as a victim; all three are mechanism-based exposure patterns.

## Iran Cyber Watch

No new Iranian-actor activity in the afternoon window. UNC1549 and Charming Kitten / Mint Sandstorm carried in this morning's brief; no resurface conditions met for either between 08:00 and 16:00.

## Other Signal

**First-party Splunk:** zero hits across `defenseclaw_local` and `archimedes` for the 13 MSTIC AitM IOCs and the three DAEMON Tools binary names over -30d (Hard Rule 8 silent telemetry). No IOC surface yet for Bleeding Llama (CVE-only).

---

*Sources hyperlinked inline. Admiralty digraph and WEP noted per item. TLP:CLEAR.*
