---
brief_id: 2026-06-13-afternoon
brief_type: afternoon
published_at: 2026-06-13T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: archimedes-red-team
human_override: null
word_count: 762
findings_referenced:
  - finding-2026-06-13-0004
  - finding-2026-06-13-0005
  - finding-2026-06-13-0006
tlp: GREEN
status: published
discord_delivery:
  channel: intel-briefs
  channel_id: "1499952717173358672"
  message_ids:
    - "1515454417980100808"
  parts: 1
  delivered_at: 2026-06-13T16:00:47-04:00
  late: false
  via: librarian
---

# Afternoon Brief — 2026-06-13

**Mandiant primary direct retrieval on UNC6240 (ShinyHunters) Oracle PeopleSoft unlocks 11 net-new IOCs — 5 staging IPs in 142.11.200.0/24, 4 SHA-256 hashes converting filename-only meshagent IOCs to hash-grade (rename-resistant), and a NEW Linux meshagent indicator class — plus verbatim zstd exfil command and exact `.xml` persistence path.**

**Why it matters:** A&D primes inheriting the Sunday 2026-06-15 FCEB clock via DFARS flow-down now have hash-grade detection content on the meshagent payload, not filename strings. Same campaign, far stronger defender posture than this morning. Splunk also patched a CVSS 9.8 PostgreSQL-sidecar RCE on its own SIEM tier today — affected product is the detection substrate.

---

## 🚨 Active Threats

**UPDATE: Mandiant + GTIG primary direct retrieval on UNC6240 (ShinyHunters) PeopleSoft campaign — 11 net-new IOCs + TTP-chain enrichment**
- What: WebFetch landing-page resolution unlocked the Mandiant primary post directly this sweep (RSS still stale-persistent at failure_count 25). Source-fidelity upgrade from this morning's SecurityAffairs relay to Mandiant primary direct. Mandiant's attribution language is identical to the SA relay — *"active compromise and extortion campaign attributed to UNC6240 (ShinyHunters)"* (9 words) — confirming relay fidelity for finding-2026-06-13-0002.
- Net-new IOCs (11): 5 staging IPs in `142.11.200.186` through `142.11.200.190` (Python SimpleHTTPServer on port 8888, 2026-05-27 to 2026-06-09); 4 SHA-256 hashes converting filename-only Windows meshagent IOCs to hash IOCs (`meshagent64-azure-ops.exe`, `meshagent64-v2.exe`, `meshagent32-azure-ops.exe`, attacker `.bash_history`); 1 SHA-256 for an **unconfigured Linux meshagent binary** — a NEW indicator class with no morning-finding equivalent.
- TTP-chain enrichment: verbatim exfil pipe `pv -s … | zstd -3 -T0 -o exfil.tar.zst`; exact persistence path under `<docroot>/envmetadata/data/environment/` for XMLDecoder exploitation; defacement marker file (`README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT`) placed in WebLogic and Process Scheduler directories.
- Scale-corroboration: 100-org figure now Mandiant-primary-direct (source-fidelity upgrade); 455k HIBP figure remains SA-relay-sourced in this sweep's excerpt. **Red-team HEDGE on scale-quantification (100+ orgs / ~455k records / 68% higher-ed) carries forward — Mandiant still single-vendor; no second IR-firm (Unit 42 / CrowdStrike / Microsoft / ZDI / Volexity / Trend Micro) surfaced 12:00 → 15:30 EDT.** ZDI Childs limited-exploitation framing remains side-by-side, not collapsed.
- A&D action: backfill the 11 net-new IOCs into PeopleSoft 8.61/8.62 hunt scope today; hash-grade matching on the 4 Windows meshagent SHA-256s replaces brittle filename matching. FCEB BOD 26-04 3-day clock closes Sunday 2026-06-15 16:00 EDT — A&D primes inherit via DFARS 252.204-7012, not BOD bindingness.
- Sources: [Mandiant + GTIG primary direct](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit) · Digraph: A2 · WEP very likely on attribution + IOC enrichment; likely on scale · finding-2026-06-13-0006
- 🔗 **Update on:** 2026-06-13 morning (SA relay of same Mandiant material); 2026-06-12 afternoon (CISA KEV + 3-day FCEB clock); 2026-06-11 flash-1200 (Mandiant Carmakal LinkedIn ITW).

## 🔓 Vulnerabilities

**CVE-2026-20253 (Splunk Enterprise, CVSS 9.8 unauth PostgreSQL-sidecar RCE) — patched 2026-06-10; coordinated vendor + discoverer disclosure**
- What: Splunk published SVD-2026-0603 and watchTowr Labs (Bazydlo + Ganchev) published the discoverer writeup the same day. Mechanic: the PostgreSQL sidecar's `/v1/postgres/recovery/{backup,restore}` endpoints lack authentication; the localhost-bound sidecar is reachable through the Splunk main web interface on port 8000. Unauthenticated file-create/truncate primitive escalates to RCE per the discoverer writeup. Splunk Cloud and the 10.4 line are NOT affected.
- Exploitation status: The Hacker News reports *"no evidence of the flaw being exploited in the wild"* (13 words) as of 2026-06-13 09:23 EDT; CISA KEV catalogVersion 2026.06.12 does not list it. **Red-team caveat binding:** the negative-inference window is ~48 hours and the affected product IS the SIEM tier used to generate detection reports — adverse selection on detection. Exploitation-status WEP downgraded from *likely* to *roughly even chance*; treat as UNKNOWN, not confirmed-negative.
- A&D relevance: Splunk Enterprise is widely deployed at A&D primes for DFARS / CMMC L2+ audit-event logging; affected 10.0.x and 10.2.x are the deployed cohort, not a niche. Patch to 10.0.7 / 10.2.4 / 10.4.0. Hunt for `/v1/postgres/recovery/*` access attempts in available SIEM telemetry — detection content had ~0 days to mature before disclosure.
- Archimedes-self-substrate operational implication: Frank runs Splunk Free 10.2.2 per CLAUDE.md Operational Notes — likely inherits the affected PostgreSQL sidecar (Splunk Free is documented as the Enterprise build behind a license gate; *not vendor-attested for the Free SKU specifically*; structural inference per the Session 3 auth-control divergence note). Self-substrate WEP downgraded from *very likely* to *likely* pending vendor confirmation. **Patching action stands regardless** — operator should upgrade Frank 10.2.2 → 10.2.4 and verify port 8000 external-reachability posture.
- Sources: [Splunk SVD-2026-0603](https://advisory.splunk.com/advisories/SVD-2026-0603) (provisional A) · [watchTowr Labs](https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/) (provisional B) · [The Hacker News](https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html) · Digraph: A2 · WEP very likely on tech-vuln layer; roughly even chance on exploitation status; likely on self-substrate · finding-2026-06-13-0004

**CVE-2026-35273 (Oracle PeopleSoft, CVSS 9.8 unauth RCE):** FCEB dueDate Sunday 2026-06-15 16:00 EDT under BOD 26-04. Oracle out-of-band mitigations only — no GA patch. Hunt the expanded 19-IOC set above today. DIB primes inherit via DFARS flow-down, not BOD bindingness.

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in the reporting window. Two structural-inference items intersect A&D — Mandiant PeopleSoft (no A&D-prime victim publicly confirmed) and Splunk Enterprise SIEM-tier RCE (deployed cohort, no A&D-prime victim observed). Neither is a direct A&D hit. Tracked actors with historical A&D targeting: APT28, [UNC1549](../threat-actors/UNC1549/profile.md), Lazarus, APT41, Salt Typhoon.

## 🕵️ Actor Activity

**GitHub announces NPM 12 default script-execution change (expected July 2026) — defensive roadmap citing TeamPCP (roster #001 HIGH) and Shai-Hulud**
- What: Per SecurityWeek's relay of GitHub's announcement (direct GitHub blog retrieval pending next sweep), NPM 12 will block `preinstall`, `install`, `postinstall`, and `prepare` scripts from dependencies by default; native `node-gyp` builds with `binding.gyp` also affected; git dependencies will not resolve unless explicitly allowed; remote-URL tarball dependencies require an `--allow-remote` flag. Opt-in allowlist via `npm approve-scripts` written to `package.json`. Brings npm in line with pnpm's and bun's pre-existing security-aware default.
- Motivating campaigns (preserved verbatim per Hard Rule 2): TeamPCP (roster #001, HIGH) — per SecurityWeek's restatement of earlier industry reporting — *"exploited automatic script execution during npm install"* (7 words). Shai-Hulud — described by SecurityWeek as a self-replicating worm weaponizing the `binding.gyp` build descriptor. Both campaigns described by SecurityWeek as having affected developers at scale; *Archimedes does not lift the aggregate figure as load-bearing.*
- Caveats: Shai-Hulud is NOT on Archimedes roster — second roster-gap candidate this week after Velvet Ant. Operator-deferred `/new-actor` decision; *Archimedes does not pre-empt the cross-walk*. Per corpus baseline (finding-2026-05-12-FLASH-0001), TeamPCP is treated as actor and Shai-Hulud as campaign family — parallel framing preserved, no collapse, no distinction beyond what SecurityWeek says.
- A&D relevance: structural — A&D primes commonly use NPM-driven JS/TS for internal web apps, CI/CD, IaC, and AI-agent harnesses (LangChain / LangGraph / Claude Code / Cursor). Developer-endpoint infection via install-time scripts is an initial-access path. Operator action: inventory NPM-consuming build pipelines; plan for the NPM 12 default-block migration and the `npm 11.16.0+` preparation upgrade path.
- Source: [SecurityWeek](https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/) · Digraph: B2 · WEP likely on announcement layer; very likely on TeamPCP TTP restatement · finding-2026-06-13-0005

## 🇮🇷 Iran Cyber Watch

**UPDATE: Handala (#014) Cal Water independence-check NEGATIVE — third-source attempt collapses; red-team HEDGE reinforced**
- What: Attempted third-publisher independence check on yesterday's Handala / California Water Service self-claim returned BreachNews (provisional C, aggregator with self-disclaimer pattern) and Wanaen (provisional D, Iranian state-adjacent) — both read directly off Handala's own leak post. NOT independent corroboration. SecurityWeek (yesterday) and SecurityAffairs (this morning) share the Dataminr analytic substrate. Underlying claim layer remains single-substrate.
- Implication: Red-team HEDGE on Handala / Cal Water from this morning is reinforced, not lifted. Cal Water still silent at the publisher layer. OT/ICS disruption explicitly NOT confirmed by Dataminr (RTKBase is GPS-correction infrastructure, not SCADA).
- Hard Rule 2 binding (carry-forward): Iranian retaliation is NOT extrapolated to A&D-prime targeting from a single water-utility cycle; Stryker is NOT cross-walked beyond Handala #014; Banished Kitten / Dune / Red Sandstorm aliases remain PENDING actor-profiler fold-in.
- Source: independence-check audit only — no new substantive publisher · Digraph: B3 (carry-forward) · WEP likely on attribution restatement · finding-2026-06-13-0003 (carry-forward)
- 🔗 **Update on:** 2026-06-13 morning (SA second relay); 2026-06-12 afternoon (SW primary; Dataminr first relay).

## 📰 Other Signal

- **Splunk first-party sentinel (Hard Rule 8):** Expanded 19-IOC sweep (8 from morning + 11 net-new) returned 0 events over -24h on both `defenseclaw_local` and `archimedes` indexes. Silent Splunk does NOT disconfirm — Frank is not a higher-ed environment consistent with the 68% UNC6240 victim profile. Visibility-limited absence.
- **AI-tooling supply-chain cluster:** NPM 12 defensive roadmap is the sixth data point — LangFlow ITW → LangGraph 3-CVE → Agentjacking → Outsider/Gemini → Anthropic export-control → NPM 12 default-block. Synthesis candidate for Wednesday's Threat Detection Weekly.
- **Provisional source-grades (72h clock at 2026-06-15T16:00:00-04:00 unchanged):** Sonatype, Sygnia, Tenet Security, Dataminr at provisional B. Bloomberg PENDING operator B/B+/A tier decision. New this run: `splunk-advisory` provisional A (vendor self-disclosure; may fold into existing `splunk-advisory-portal`), `watchtowr-labs` provisional B, `breachnews` provisional C, `wanaen` provisional D.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:GREEN.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-13.

🚨 **Active Threats**

• **[Mandiant primary unlocks 11 net-new UNC6240 / PeopleSoft IOCs](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit)** — Direct fetch today: 5 staging IPs `142.11.200.186-190`, 4 SHA-256s converting filename-only meshagent IOCs to hash-grade, plus a NEW Linux meshagent class. Verbatim zstd exfil + exact `.xml` persistence path. Mandiant still single-vendor on scale — *HEDGE carries.* **PeopleSoft 8.61/8.62: backfill the 11 IOCs today; FCEB closes Sunday June 15.**

🔓 **Vulnerabilities**

• **[Splunk patches CVSS 9.8 PostgreSQL-sidecar pre-auth RCE (CVE-2026-20253)](https://advisory.splunk.com/advisories/SVD-2026-0603)** — Splunk + watchTowr coordinated disclosure June 10: unauth `/v1/postgres/recovery/{backup,restore}` via port-8000 relay. Cloud + 10.4 NOT affected; fixes 10.0.7 / 10.2.4 / 10.4.0. THN reports no public exploitation — but the affected product IS the SIEM generating those reports; treat status UNKNOWN. **A&D 10.0.x / 10.2.x: *patch this week*.**

🕵️ **Actor Activity**

• **[GitHub will block npm dependency scripts by default in NPM 12 (July 2026)](https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/)** — Per SecurityWeek's relay of GitHub: preinstall / install / postinstall / prepare blocked by default; opt-in via `npm approve-scripts`; git + remote-URL gated. Motivated by TeamPCP (#001) and Shai-Hulud — *not collapsed beyond SW's parallel framing*. *Inventory builds; plan 11.16.0+ prep upgrade.*

🇮🇷 **Iran Cyber Watch**

• **Handala (#014) Cal Water — independence-check NEGATIVE; HEDGE reinforced.** BreachNews + Wanaen both read off Handala's leak post. SW + SA still share Dataminr. *Iranian retaliation not extrapolated to A&D from one water cycle.*
