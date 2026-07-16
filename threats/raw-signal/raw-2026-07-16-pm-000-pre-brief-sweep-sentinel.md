---
raw_id: raw-2026-07-16-pm-000
collected_at: 2026-07-16T15:35:00-04:00
run_id: pre-brief-20260716-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: Afternoon pre-brief sweep sentinel (2026-07-16 15:30 EDT)
  source_url: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sweep-record]
triage_tags: [sweep_sentinel, non_promotable_record]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-14T15:35:00-04:00
---

# Afternoon pre-brief collection sweep — 2026-07-16 15:30 EDT (window ~01:30→15:30 EDT, ~14h per orchestrator)

Sweep record for the 16:00 EDT afternoon brief. Two substantive raw-signals written (pm-001 tracked-actor LE sentencing; pm-002 CISA KEV 2026-07-16 batch incl. VT-041 state change). Bookkeeping sentinel, not a promotable finding.

## Sources queried (healthy per source-health.yaml)

- **bleepingcomputer** — RSS 200, 15 items in feed, 9 in ~14h window. PRODUCTIVE — pm-001 (Scattered Spider TfL sentencing). Anti-noise dedup: Oracle EBS CISA-Saturday (= am-004/VT-043). Remainder filtered (see Filtered).
- **securityweek** — RSS 200, 10 items in feed, 10 in window. Corroborates pm-001 (Scattered Spider UK sentencing). Anti-noise dedup: F5 NGINX/BIG-IP (= am-002/VT-044), Nightmare Eclipse LegacyHive (= am-005/VT-042). Remainder filtered.
- **the-record** — RSS 200, 5 items in feed, 4 in window. Corroborates pm-001. Anti-noise dedup: Sandworm CAPTCHA/PowerShell (= flash-1600-001 / finding-2026-07-16-0003). Remainder filtered (policy/geopolitics).
- **sans-isc** — RSS 200, 10 items in feed, 0 in window.
- **krebs** — RSS 200, 10 items in feed, 0 in window (normal cadence).
- **cisa-kev** — JSON feed directly retrieved. PRODUCTIVE — pm-002: three adds dated 2026-07-16 (CVE-2026-58644 SharePoint = VT-041 state change; CVE-2026-25089 + CVE-2026-39808 FortiSandbox OS command injection). The 2026-07-15 adds (Oracle EBS CVE-2026-46817 / KNX CVE-2023-4346) are anti-noise (already am-004 + absorbed at 06:00 sweep per commit 5299279).
- **splunk (archimedes + defenseclaw_local)** — health ping OK (Frank, Splunk 10.2.2, reachable). No targeted IOC sweep executed: both net-new items are IOC-empty at the atomic-network level (LE sentencing has no IOCs; KEV adds are CVE IDs only). No enrichment trigger; no first-party query warranted this sweep.

Not re-queried this sweep (scope + known state; no in-window lead required them): nvd (KEV adds already carry CVE IDs/context; no fresh non-tracked CVE lead needed a lastModified pivot), crowdstrike (persistently barren marketing feed), unit42 / mstic (morning sweep already pulled am-001 MSTIC AsyncAPI + am-003 Unit42 npm; no fresh afternoon lead), cisco-talos (the UAT-11795 Starland item reached corpus via BC relay — dispositioned below), rapid7, wired-security, recorded-future, sentinelone/bitdefender/symantec/proofpoint/wiz/socket (no in-window relay lead pointed to a fresh primary), shodan/virustotal/abuseipdb/threatfox/malwarebazaar (no enrichment trigger — no atomic IOCs to enrich), x-swiftonsecurity/x-vxunderground/x-falconfeedsio + iran-monitor/cyberwarrior76 (primary aggregators already swept; no standing-section Iran lead surfaced beyond corpus).

## Stale / skipped per health rules

- **mandiant** — feedburner RSS 404 long-entrenched; direct-HTML workaround operator-pending. Not exercised (no in-window lead warranted the direct-HTML pull; quiet cadence).
- **msrc** — feed parse error (stale since 2026-05-30); Microsoft content reaches corpus via relays this sweep (SharePoint via CISA KEV direct; no MSRC-primary lead needed).
- **ars-security** — security-path retired; root-feed workaround (not needed).
- **github-advisories** — 406 on global advisories.atom; per-repo GHSA fallback (not triggered — today's CVEs are Microsoft-CNA / Fortinet-PSIRT, not GHSA).
- **censys / urlscan / hibp** — stale (no-MCP / auth-injection limited); not invoked (no enrichment trigger).
- **x-cisagov / x-gossithedog** — nitter-bridge stale; not retried.
- **industrialcyber-co / sophos / volexity** — stale; not retried (no in-window lead required them).

No stale flips this sweep. All queried sources returned 200 / valid. No runtime source-health field changes required (all healthy sources succeeded; no failures to record; operator-set `notes` fields untouched).

## Raw-signal written this sweep (2 substantive + this sentinel)

- **pm-001** — Scattered Spider (roster **#013** / UNC3944) members Thalha Jubair + Owen Flowers sentenced to 5.5 years in UK for the Aug-2024 Transport for London hack; DOJ parallel charges (~120 US breaches). Tracked-actor LE / attribution-of-record development; retrospective, no new TTP or IOC. Three publisher-independent relays (BleepingComputer + SecurityWeek + The Record). Not A&D-named; not FLASH-shaped.
- **pm-002** — CISA KEV catalog adds dated 2026-07-16: **CVE-2026-58644** (Microsoft SharePoint unauth deserialization RCE, CVSS 9.8) = Archimedes **VT-041** flipping NOT-exploited/NOT-KEV → actively-exploited/KEV-listed (Trigger-1-shaped tracked-vuln state change; due 2026-07-19). Plus **CVE-2026-25089** + **CVE-2026-39808** (Fortinet FortiSandbox OS command injection, net-new to corpus, KEV-listed / due 2026-07-19).

## Filtered / discarded (documented, not raw-signaled)

- "Claude Chrome extension flaw lets malicious extensions trigger AI actions" (BC, Lawrence Abrams) — new Anthropic Claude-for-Chrome disclosure (malicious extension simulates clicks to trigger AI actions abusing Gmail/Docs/Calendar/Salesforce access). Adjacent to the ClaudeBleed thread already raw-signaled 07-14 (pm-008), but a distinct mechanism; no roster actor, no A&D, no tracked CVE. Awareness only (Anthropic-product / AI-agent-security thread continues) — no Mode 1 filter hit.
- "New OkoBot framework deploys 20 payloads to steal data, crypto" (BC, Toulas) — commodity crypto/credential stealer framework. No roster/A&D/vuln hit.
- "Russian hackers trojanize WebEx, Zoom apps to push Starland malware" (BC, Toulas) — financially-motivated Russian actor UAT-11795 (Cisco Talos designation; NOT a roster actor) + new Starland RAT. Russian-nexus but financially motivated, no A&D, no tracked vuln. No filter hit. Flagged for awareness as a potential /new-actor candidate for operator review.
- "New Spirals ransomware encrypts victim network in under 24 hours" (BC, Toulas) — new ransomware actor "Spirals," fast-encryption. Not roster/A&D/vuln. Awareness.
- "23andMe to pay $18 million in new genetics data breach settlement" (BC / The Record) — consumer-breach settlement. No hit.
- "AI Agents Broke the Security Playbook..." (BC) — sponsored (Token Security). Filtered.
- "Windows 11 24H2 Home and Pro reach end of support in 90 days" (BC) — lifecycle news, not threat intel. No hit.
- "Legacy Systems, Real-World Impacts: The Reality of OT Security" (SecurityWeek, Tod Beardsley) — opinion/analysis. No hit.
- "AI Data Centers Are Being Built Faster Than They Can Be Secured" (SecurityWeek) — analysis. No hit.
- "'ClickLock Stealer' Bypasses macOS Security..." (SecurityWeek) — commodity macOS infostealer (ClickFix-adjacent social engineering). No roster/A&D/vuln hit. Awareness (ClickFix-technique proliferation).
- "Oak Emerges From Stealth Mode With $60 Million..." (SecurityWeek) — funding/business. Filtered.
- "Splunk, Zoom Patch Critical Vulnerabilities" (SecurityWeek) — Splunk + Zoom critical patches. No active exploitation, no CVE match to a tracked vuln, no A&D. NOTE: Splunk is Archimedes' own SIEM stack (Frank) — flagged for operator/infra awareness (patch-posture interest), but no Mode 1 filter hit → discarded.
- "China's Top Cybersecurity Firms Hit by Mounting Military Procurement Bans" (SecurityWeek) — China geopolitics/policy; no specific roster actor / A&D victim / tracked vuln. No hit.
- "Old UEFI Shims Expose Systems to Secure Boot Bypass" (SecurityWeek) — Microsoft-signed vulnerable UEFI shim bootloaders / Secure Boot bypass. Vuln-class awareness; no tracked CVE, no active exploitation named, no A&D-direct nexus. No filter hit.
- "UK investigates TikTok for alleged age-verification lapses" (The Record) — regulatory/policy. No hit.
- "Ukrainians rally against dismissal of tech-minded defense minister Fedorov" (The Record) — geopolitics. No hit.

## Notes for downstream

- **Grader 16:00 queue:**
  - **pm-002** is the priority afternoon-brief item — VT-041 / CVE-2026-58644 tracked-vuln state change to KEV-listed / actively-exploited (on-prem SharePoint, DIB-pervasive; A&D relevance HIGH-structural). Suggest vuln-tracker VT-041 STATE UPDATE (kev_pending → kev_listed; exploitation not_observed → in_the_wild; due 2026-07-19). CISA KEV entry directly retrieved this sweep (A1 procedural). No actor, no atomic IOC. Note ongoing SharePoint-cluster context (VT-037/-038/-039/-040/-041 lineage).
  - **pm-002 (Fortinet):** CVE-2026-25089 + CVE-2026-39808 FortiSandbox command-injection = new KEV-listed vuln-tracker scaffolding candidates (edge/security appliance; A&D-relevant perimeter tier).
  - **pm-001** is a tracked-actor (#013 Scattered Spider) LE/attribution-of-record item — low-heat, retrospective; suitable as an actor-watch / ransomware-watch brief note, not a FLASH.
- **vuln-tracker candidates:** VT-041 state update (headline); FortiSandbox CVE-2026-25089 / CVE-2026-39808 net-new dossiers. Awareness-only (no dossier action from collector): Splunk/Zoom critical patches; UEFI shim Secure Boot bypass; UAT-11795 (Starland RAT) and Spirals ransomware as potential future roster candidates.
- **FLASH note:** pm-002's VT-041 KEV flip is Trigger-1-shaped (critical CVE + active exploitation + A-grade). Since the 16:00 scheduled brief is imminent, a separate FLASH is anti-noise — routed to the afternoon brief per FLASH-POLICY absorb-into-next-scheduled precedent.
- No policy violations, no credential exposure, no controlled-information triggers this sweep. No SpiderFoot / active-recon requests. No authorized-targets scans. Splunk first-party reachable (health ping OK); no IOC-bearing item required a first-party query.
