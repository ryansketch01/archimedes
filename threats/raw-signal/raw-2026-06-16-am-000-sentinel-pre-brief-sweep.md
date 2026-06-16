---
raw_id: raw-2026-06-16-am-000
collected_at: 2026-06-16T07:35:00-04:00
run_id: pre-brief-20260616-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-internal
  source_name: Archimedes Sentinel
  source_url: null
  published_at: 2026-06-16T07:35:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, pre_brief_sweep, internal_substrate]
triage_tags: [sentinel, internal]
iocs_extracted: false
iocs_count: 0
text_word_count: 220
promoted: false
ttl_expires_at: 2026-09-14T07:35:00-04:00
---

# Sentinel — Pre-brief sweep 2026-06-16 07:30 EDT

Internal sentinel substrate. Records that the pre-brief collection sweep for the 2026-06-16 08:00 EDT morning brief ran. Never promoted; never rejected. Just records the sweep happened.

## Sweep summary

- Time window: 2026-06-15T17:30 EDT → 2026-06-16T07:30 EDT (14h)
- Sources queried (healthy): CISA all.xml, CISA KEV JSON, BleepingComputer, The Hacker News, SecurityWeek, The Record, Security Affairs, The Register, Help Net Security, Dark Reading, SANS ISC, KrebsOnSecurity, Mandiant cloud.google.com direct, ESET WeLiveSecurity direct, Unit 42, Cisco Talos, CrowdStrike, MSTIC, ZDI blog, Fortinet PSIRT direct, Cisco PSIRT direct, Genians Security Center direct, SecurityWeek Atomic Arch follow-up
- Sources skipped under under-24h stale rule: mandiant feedburner RSS (failure_count 27, stale_since 2026-06-13), msrc RSS (stale_since 2026-05-30), proofpoint /us/threat-insight/blog/feed (5x 404), sophos top-level (stale_since 2026-05-17), industrialcyber.co RSS (stale_since 2026-06-11), volexity (stale_since 2026-06-11)
- KrebsOnSecurity feed: 0 items in window (quiet — not a failure)
- Dark Reading RSS feed: 0 items in window (200 OK, transient pattern confirmed not a failure)
- Wired security feed: 0 items in window (200 OK)

## In-window items written as raw-signal

- am-001 ESET WeLiveSecurity FishMonger SprySOCKS Windows expansion A-grade vendor IR primary published 2026-06-16 (BC + THN dual-relay also)
- am-002 BC FortiSandbox three-CVE active exploitation cluster — net-new from 06:00 substrate (THN second-publisher relay) Fortinet PSIRT FG-IR-26-141 advisory directly retrieved confirms vendor side
- am-003 THN APT37/ScarCruft NarwhalRAT — Genians Security Center primary confirmed direct, plus THN relay (publisher-independent corroboration of 06:00 single-publisher substrate)
- am-004 SecurityWeek + Help Net Security + Security Affairs + The Register Cisco SD-WAN Manager CVE-2026-20262 — second-publisher relay cluster, vendor-confirmed in-the-wild, CISA KEV-listed 2026-06-15, finding-2026-06-15-0006 status pivot UPDATE
- am-005 BC + THN + Security Affairs LiteSpeed cPanel CVE-2026-54420 — CISA KEV-listed 2026-06-15, deadline 2026-06-18, A&D-relevance LOW Other Signal substrate
- am-006 Security Affairs UNC6508 — second-publisher relay of GTIG primary, pure relay no independent telemetry per source-of-claim analysis
- am-007 BC DragonForce Backdoor.Turn Microsoft Teams TURN relay abuse — Symantec primary attribution, no A&D-prime named victim
- am-008 BC iRhythm Holdings cardiac monitoring breach — healthcare (12M patient profile), social-engineering vector, no actor attribution, no A&D-prime named victim

## Discarded out-of-window or out-of-scope

- ZDNet zero-day feed (consumer hardware reviews, not security)
- Wired security (0 items in window)
- KrebsOnSecurity (0 items in window)
- The Record UK social media under-16 ban (regulatory/policy, no CVE no actor no IOC no A&D relevance)
- The Record Estonia .ru domain quarantine (regulatory/policy)
- SANS ISC VHDX → Remcos RAT diary 2026-06-16 (BC awareness-only consumer-RAT-delivery template, no CVE no actor no A&D relevance — discarded)
- Help Net Security crypto courier-cash-pickup FBI warning, ENISA SBOM CRA, hospitality travel fraud, GitHub multilingual dataset, AI threat modeling interview, EU Cybersecurity Act 2.0, machine identities, AI data governance, jobs board — all opinion/policy/jobs, no actor no CVE no A&D direct
- SecurityWeek Athena OSS coalition, cybersecurity executives urging Trump to ease Anthropic restrictions (Fable 5/Mythos 5 substrate update — Anthropic position carry-forward, NOT net-new substrate beyond finding-2026-06-15-0010 — discarded under anti-noise rule 1 binding)
- BC DOJ CFAKE/SOCFAKE seizure (already covered 18:00 sweep — anti-noise dedup binding)
- ZDI blog (most recent post 2026-06-09)
- Cisco Talos blog (most recent post 2026-06-11)
- CrowdStrike blog (2026-06-15 post is product marketing, not threat research)
- MSTIC (most recent threat-intel post 2026-06-08, no in-window content)
- Mandiant cloud.google.com index page same top-8 titles as 06:00 sweep (UNC6508 / GTIG AI Threat Tracker / ShinyHunters PeopleSoft / Seeking Counsel US law firms / KnowledgeDeliver / 2 PhaaS / BlackFile / UNC6692 Snow Flurries — all out-of-window or already-substrate)
- ESET WeLiveSecurity OceanLotus Vietnam shift (2026-06-11 out-of-window)

## Source-health observations carried forward, no mutation

- mandiant feedburner RSS not re-attempted under under-24h skip rule (last attempt 2026-06-14 07:31, failure_count 27, stale_since 2026-06-13). Direct cloud.google.com HTML success-pattern entrenched 9+ consecutive successes. Canonical-swap operator-deferred.
- proofpoint /us/threat-insight/blog/feed 5x consecutive 404 not promoted to stale without operator approval. THN relay backstop productive.
- sophos top-level news.sophos.com/en-us/feed/ stale-persistent since 2026-05-17, replacement candidate news.sophos.com/en-us/category/threat-research/feed/ standing pending operator decision.
- Dark Reading rss.xml RECOVERY-PERSISTENCE-EXTENDED 200 OK at 00:00 and 06:00 sweeps and now this 07:30 sweep with 0 items in window (quiet sweep, not a failure). Pattern firmly transient; operator review closed.

## Notes to grader

Net-new substrate worth flagging for the 08:00 brief composition:

1. **ESET FishMonger SprySOCKS Windows expansion (am-001)** — A-grade vendor IR primary direct retrieval. ESET cluster-name "FishMonger" with explicit Winnti-umbrella framing AND named cross-walk to Earth Lusca / Aquatic Panda / Bronze University / Charcoal Typhoon / RedHotel — but Hard Rule 2 BINDING: ESET originates the cluster identity preservation, Archimedes does NOT cross-walk further. FishMonger/Earth Lusca NOT on 24-actor _roster.yaml. PRC-nexus i-Soon contractor attribution per ESET. Per WIN_DRV variant uses kernel driver RawWNPF + DriverLoader fsdiskbit.sys, WIN_PLUS uses Print Spooler. CVE-2023-24932 Secure Boot bypass possible UEFI bootkit involvement (limited evidence). 4 named victim countries (Honduras, Taiwan, Thailand, Pakistan) — government foreign affairs/tech/telecom — NO A&D-prime named victim. Substrate-ready for /new-actor candidacy operator-deferred per Hard Rule 5. Initial access via N-day exploitation of Fortinet, GitLab, Microsoft Exchange, Progress Telerik UI, Zimbra — universally A&D-relevant pivot inheritance.
2. **FortiSandbox three-CVE cluster (am-002)** — independent vendor confirmation: Fortinet PSIRT FG-IR-26-141 direct retrieval confirms CVE-2026-25089 CVSS 9.1 "second-order OS command injection via JSON input on start VNC feature in the web UI" patched 2026-06-09. THN + BC second-publisher independent relay of Defused observation. T1 GATE now SATISFIED — vendor-side independent of news relay. Fortinet PSIRT did NOT itself acknowledge active exploitation at advisory publication ("No known exploits") — exploitation observed via Defused IR vendor only. CISA KEV NOT YET LISTED. CVSS 9.1 satisfies Trigger 1 floor (>= 9.0). A&D-relevance HIGH — FortiSandbox is sandboxing-platform commonly inherited in DIB tenants. Grader candidate for B2/B3 finding.
3. **APT37 NarwhalRAT (am-003)** — Genians Security Center direct retrieval confirms 2026-06-14 publication of "Analysis of APT37 NarwhalRAT Leveraging MS-Themed Phishing and Dead-drop C2." THN second-publisher relay. APT37 on _roster.yaml #024 (MEDIUM, last_reviewed 2026-05-10). NarwhalRAT is net-new tooling not previously in APT37 dossier. T2 partial fire (tracked actor + new tooling), T5 FAIL no A&D-prime named victim. Grader candidate for B2 finding with possible APT37 dossier mutation upon operator approval.
4. **Cisco SD-WAN CVE-2026-20262 (am-004)** — SecurityWeek Eduard Kovacs + Help Net Security Zeljka Zorz + Security Affairs Paganini + The Register all second-publisher independent. CISA KEV-listed 2026-06-15 with deadline 2026-06-29 confirms anticipated KEV pathway from finding-2026-06-15-0006. Status pivot UPDATE eligible: KEV-listing-watch CLOSED → KEV-listed-with-BOD-22-01-deadline-2026-06-29. The Register frames as "eighth Cisco SD-WAN KEV add of 2026." Help Net Security adds Cisco's own statement that vulnerability was "found during internal security testing" — Zorz raises sharp internal-discovery-vs-external-exploitation framing question (productive secondary observation).
5. **LiteSpeed cPanel CVE-2026-54420 (am-005)** — net-new to corpus. BC + THN + Security Affairs three independent second-publisher relays. CISA KEV deadline 2026-06-18 ~T+58h. CVSS 8.5. A&D-relevance LOW (shared hosting / SMB / CloudLinux / CageFS commodity infrastructure). Possible Other Signal one-liner for morning brief, NOT promotable finding.

Anti-noise carry-forward (no net-new substrate this window):

- UNC6508 / INFINITERED PRC-nexus — Security Affairs pure relay of GTIG primary, 72h FLASH dedup through 2026-06-18 12:00 EDT binding. No net-new independent A-grade IR vendor corroboration; SA does NOT clear single-source veto.
- CVE-2026-35273 PeopleSoft FCEB BOD 26-04 — deadline closed EOD 2026-06-15, retrospective-compliance-metrics phase
- CVE-2026-10520 Ivanti Sentry — retrospective phase, deadline 2026-06-14 closed
- CVE-2026-0257 PAN-OS — retrospective phase, deadline 2026-06-01 15d+ past
- CVE-2026-20253 Splunk Enterprise — HOLD vendor confirmation pending
- Fable 5/Mythos 5 Anthropic USG export-control finding-2026-06-15-0010 — SecurityWeek follow-up "Cybersecurity Executives Urge Trump to Ease Restrictions" carries forward existing dispute, NOT net-new substrate
- Velvet Ant Operation Highland Sygnia primary finding-2026-06-15-0007 — carry-forward
- Handala #014 / Cal Water Iran Cyber Watch third-source NEGATIVE binding stands
- Check Point VPN CVE-2026-50751 / Qilin
- CVE-2026-42824 SearchLeak M365 Copilot Enterprise — finding-2026-06-15-0011, vuln-tracker-handoff operator-deferred stands
- SecurityWeek Atomic Arch supply chain 1500 packages — substrate update to Arch AUR cluster from PM brief 580af3f finding-2026-06-15-0013, NOT net-new substrate beyond Sonatype attestations already in record
