---
brief_id: 2026-06-12-afternoon
brief_type: afternoon
published_at: 2026-06-12T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_required
human_override: null
word_count: 880
findings_referenced:
  - finding-2026-06-12-0001
  - finding-2026-06-12-0002
  - finding-2026-06-12-0003
  - finding-2026-06-12-0004
  - finding-2026-06-12-0005
  - finding-2026-06-12-0006
  - finding-2026-06-12-0007
  - finding-2026-06-12-0008
tlp: GREEN
status: published
discord_delivery:
  channel: intel-briefs
  channel_id: "1499952717173358672"
  message_ids:
    - "1515102414036795404"
  parts: 1
  delivered_at: 2026-06-12T16:05:00-04:00
  late: false
  via: librarian
  layer_2_char_count: 1737
---

# Afternoon Brief — 2026-06-12

**CISA added Oracle PeopleSoft CVE-2026-35273 to KEV with a 3-day FCEB deadline (2026-06-15) and a `knownRansomwareCampaignUse: Known` tag — the same day Ivanti clarified that the CVE-2026-10520 "mass" framing traces to honeypot hits, not production systems.** Two federal-procedural-attestation moves, opposite vectors, same KEV catalog.

**Why it matters:** A&D-prime PeopleSoft deployments now face federal attestation of ransomware-operations use — without a GA patch. DIB legal teams should also note the unsealed IBM/AT&T whistleblower complaint naming DFARS 252.204-7012, CMMC L2/L3, and False Claims Act exposure on federal-contractor breach disclosure.

---

## 🚨 Active Threats

**UPDATE: CVE-2026-35273 (Oracle PeopleSoft) added to CISA KEV with 3-day FCEB clock and ransomware-use tag**
- What: CISA added 2026-06-12, dueDate 2026-06-15, `knownRansomwareCampaignUse: Known`. Oracle's out-of-band mitigations only — no GA patch.
- Framing: KEV inclusion is the federal determination of in-the-wild exploitation. The ransomware-use tag is procedural-taxonomic — CISA tags vulnerabilities used in ransomware operations, NOT actors. ShinyHunters' 100-org self-claim remains separately sourced; *Archimedes does not collapse the two layers.* Scale: limited per Mandiant + ZDI; observed framings likely lag current operational reality.
- A&D action: inventory PeopleTools internet exposure; apply Oracle's mitigations; treat the FCEB cadence as aspirational for DIB primes (BOD 26-04 binds FCEB only).
- Source: [CISA KEV catalog](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) · Digraph: A1 · WEP very likely on federal-attestation · finding-2026-06-12-0001
- 🔗 **Update on:** 2026-06-11 flash-1200 (Mandiant ITW); 2026-06-11 afternoon (ZDI "limited" + HIBP 455k).

**UPDATE: Ivanti clarifies CVE-2026-10520 KEV-triggering exploitation hit honeypots, not production**
- What: Ivanti's advisory update (via SecurityWeek) characterizes the observed exploitation as honeypot-targeted; vulnerable APIs are mTLS-protected on EPMM-managed appliances; unmanaged Sentry cannot run in production.
- What does NOT change: CVSS 10.0 pre-auth RCE; CISA KEV listing; BOD 26-04 3-day FCEB clock (2026-06-14); CVE-2026-10523 companion auth bypass (CVSS 9.9) is not addressed.
- This validates the morning red-team hedge on "mass" framing. Internet-facing Sentry without mTLS remains exposed-class.
- Source: [SecurityWeek](https://www.securityweek.com/ivanti-sentry-exploitation-attempts-hitting-honeypots/) · Digraph: A2 · finding-2026-06-12-0002
- 🔗 **Update on:** 2026-06-11 morning + 2026-06-11 afternoon (CISA KEV + BOD 26-04).

**400+ Arch User Repository packages hijacked — "Atomic Arch" Rust credential stealer + eBPF rootkit**
- What: Sonatype documents new maintainer accounts adopting abandoned AUR packages, modifying PKGBUILD/.install scripts, and delivering a Rust stealer that — with root — loads an eBPF rootkit. Two waves; ~408 packages. Official Arch repos NOT affected.
- Targeted credentials (8 categories): GitHub / npm / Vault tokens, OpenAI creds, SSH keys, Docker, VPN profiles, browser cookies, shell histories, Electron session data.
- A&D action: audit AUR use on developer workstations; rotate developer-tier credentials if exposure suspected; hunt eBPF maps `hidden_pids`, `hidden_names`, `hidden_inodes`. IOCs: SHA-256 `6144d433...43c98b`; `atomic-lockfile@1.4.2`; `js-digest`; C2 `temp.sh` + Tor onion.
- First Arch ecosystem mass compromise in corpus; extends the supply-chain-of-developer-tooling cluster (Mini Shai-Hulud → Shai-Hulud → node-ipc → Anthropic TanStack → GitHub 3,800-repo).
- Sources: [BleepingComputer](https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/) · [The Hacker News](https://thehackernews.com/2026/06/400-arch-linux-aur-packages-hijacked.html) · Digraph: B2 · finding-2026-06-12-0005

**Tenet Security "Agentjacking" — Sentry DSN abuse against Claude Code and Cursor**
- What: Tenet research-attests an 85% success rate injecting malicious instructions into fabricated Sentry error events; AI coding agents interpret the content as legitimate guidance. 2,388 orgs have exploitable DSNs in Tenet's enumeration. Sentry declined to patch the behavior — content filter only. Defense-bypass: the malicious content is the trusted Sentry feed itself, so EDR / WAF / VPN provide no obstacle.
- A&D scope: any A&D-prime engineering team running Claude Code or Cursor against a public-app Sentry is in scope; population not enumerated. *Inventory Sentry DSN exposure; constrain agent-tool feeds to vetted sources.*
- Source: [The Hacker News](https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html) · Digraph: B2 · finding-2026-06-12-0007 (Part A)

## 🔓 Vulnerabilities

**LangGraph 3-CVE chain — SQL injection + msgpack deserialization + RediSearch query injection, all patched**
- CVE-2025-67644 (CVSS 7.3) `langgraph-checkpoint-sqlite <3.0.1` SQL injection; CVE-2026-28277 (CVSS 6.8) `langgraph <1.0.10` unsafe msgpack deserialization; CVE-2026-27022 (CVSS 6.5) `@langchain/langgraph-checkpoint-redis <1.0.1` RediSearch query injection.
- Chain-to-RCE: CVE-2025-67644 + CVE-2026-28277 chainable on self-hosted with SQLite or Redis checkpointers + user-controlled filter inputs. No ITW. Managed LangSmith Deployment NOT affected. *A&D-prime teams running internal agent platforms should pin to patched versions today.*
- Source: [The Hacker News](https://thehackernews.com/2026/06/critical-langgraph-flaws.html) · Digraph: B2 · finding-2026-06-12-0007 (Part B)

## ✈️ Sector Focus: Aerospace & Defense

**Unsealed whistleblower complaint alleges IBM and AT&T concealed federal-contractor breaches**
- What: Bloomberg broke 2026-06-04 (via [SecurityWeek's In Other News](https://www.securityweek.com/in-other-news-google-security-layoffs-audia6-takedown-400-million-coupang-fine/)). William Barlow (former IBM VP, Threat Intelligence) filed qui tam under seal in 2020; DOJ declined to intervene; pending in federal court in New York. The complaint alleges IBM and AT&T concealed "foreign and unidentified hackers" repeatedly infiltrating their networks while providing false security-posture assurances to maintain federal contracts. *Archimedes does not extend the complaint language to any named actor.*
- IBM (paraphrased per Hard Rule 6): the complaint was filed six years ago, DOJ declined to intervene, the company's actions followed the letter of the law. AT&T did not comment.
- A&D-adjacent: DFARS 252.204-7012 + CMMC L2/L3 + False Claims Act exposure. Spillover depends on the case proceeding past motion-to-dismiss; not source-attested.
- Digraph: B3 · finding-2026-06-12-0008

## 🕵️ Actor Activity

**[Sygnia documents Velvet Ant — China-nexus PAM + OpenSSH backdoor on East Asia victim, ~10-year dwell](https://thehackernews.com/2026/06/sygnia-velvet-ant-pam-openssh.html)**
- What: Sygnia (via THN) attests nine PAM-module backdoor variants plus modified OpenSSH logging credentials and typed commands, with an operator-side disable switch. Earliest traces 2016. Air-gapped victim. No A&D-prime sector named.
- Velvet Ant is NOT in Archimedes' roster — `/new-actor` DEFER pending direct Sygnia primary retrieval. Hedge: primitives are portable in principle; A&D-prime applicability bounded by access-vector and configuration overlap not enumerated in the relay.
- Detection-engineering: PAM module FIM; OpenSSH binary attestation; syscall-tracing for the disable switch. Threat Detection Weekly candidate.
- Digraph: B2 · finding-2026-06-12-0004

## 🇮🇷 Iran Cyber Watch

**Handala Hack (#014, Iran/MOIS per prior US-government attribution) claims California Water Service breach**
- What: SecurityWeek relays Handala's self-publication — 5 GB leak naming Cal Water's Chico District; customer PII, RTKBase admin credentials, NTRIP source passwords across seven district mountpoints. Dataminr identifies RTKBase as the likely initial access vector with lateral move to billing.
- Attribution: SW restates prior US-government public attribution of Handala to Iran's MOIS — restatement, NOT new. Handala is roster #014. New aliases (Banished Kitten, Dune, Red Sandstorm) flagged for actor-profiler fold-in. Hard Rule 7: PII / credential categories counted at article level only.
- Cal Water has not publicly acknowledged. Water utility — NOT A&D. Iranian retaliation is NOT extrapolated to A&D-prime targeting from a single water-utility cycle (Hard Rule 2).
- Source: [SecurityWeek](https://www.securityweek.com/iranian-cyber-group-handala-claims-cal-water-hack/) · Digraph: B3 · finding-2026-06-12-0003

## 📰 Other Signal

**[Google sues China-based "Outsider" smishing PhaaS over Gemini AI abuse.](https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html)** SDNY civil complaint: five-group structure ($88/week via `@OutsiderCodeBot`), 290+ impersonation templates, operators prompting Gemini for "gift redemption page" HTML pasted into Outsider. Alleged scope: 9,000 fake sites + 1.59M URLs + 2.5M Android smishing messages May-June 2026 + 100,000+ victims. Civil pleadings, NOT criminal. *Complaint names "China-based criminal actors," NOT Chinese intelligence services.* Third AI-tooling weaponization data point this window: AI-as-target (Langflow ITW + LangGraph + Agentjacking) vs AI-as-tool (Outsider/Gemini + Unit 42 Trust-No-Skill). Flagged for Wednesday's Threat Detection Weekly. **Digraph: B2 · finding-2026-06-12-0006.**

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:GREEN.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-12.

🚨 **Active Threats**

• **[Oracle PeopleSoft CVE-2026-35273 added to CISA KEV — ransomware-use tag, June 15 FCEB clock](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)** — No GA patch; Oracle mitigations only. *KEV tag is procedural-taxonomic, NOT actor attribution.* ShinyHunters' self-claim stays separate.

• **[400+ AUR packages hijacked — "Atomic Arch" Rust stealer + eBPF rootkit](https://www.bleepingcomputer.com/news/security/over-400-arch-linux-packages-compromised-to-push-rootkit-infostealer/)** — Targets GitHub/npm/Vault tokens, SSH, Docker, VPN. Official Arch repos unaffected. *Audit AUR; rotate dev creds.*

✈️ **Sector Focus: A&D**

• **[Whistleblower suit alleges IBM + AT&T concealed federal-contractor breaches](https://www.securityweek.com/in-other-news-google-security-layoffs-audia6-takedown-400-million-coupang-fine/)** — Bloomberg, June 4; ex-IBM VP Barlow's 2020 qui tam unsealed; DOJ declined. Cites "foreign and unidentified hackers" — no named actor. DFARS, CMMC L2/L3, FCA exposure.

🇮🇷 **Iran Cyber Watch**

• **[Handala (#014) claims California Water Service breach](https://www.securityweek.com/iranian-cyber-group-handala-claims-cal-water-hack/)** — 5 GB leak: PII, RTKBase admin creds, NTRIP passwords. Dataminr flags RTKBase as likely initial access. SW restates prior US-gov Iran/MOIS attribution — restatement, NOT new. Water utility, not A&D.

Layer 1 also covers the Ivanti CVE-2026-10520 honeypot clarification, Tenet Agentjacking vs Claude Code/Cursor, LangGraph 3-CVE chain, Velvet Ant (`/new-actor` DEFER), and Google v. Outsider/Gemini.
