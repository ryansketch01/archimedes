---
raw_id: raw-2026-07-15-pm-000
collected_at: 2026-07-15T15:36:00-04:00
run_id: pre-brief-20260715-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: multiple
  source_name: Afternoon pre-brief sweep sentinel (2026-07-15 15:30 EDT)
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
ttl_expires_at: 2026-10-13T15:36:00-04:00
---

# Afternoon pre-brief collection sweep — 2026-07-15 15:30 EDT (window ~07:30→15:30 EDT, ~8h)

Sweep record for the 16:00 EDT afternoon brief. Post-Patch-Tuesday quiet-ish window; one substantive raw-signal (pm-001, tracked-vuln escalation). Bookkeeping sentinel, not a promotable finding.

## Sources queried (healthy per source-health.yaml)

- **bleepingcomputer** — RSS 200, 15 items in feed, 3 in 8h window. All 3 filtered (Gemini CLI abuse, AsyncAPI npm stealer, sponsored) — see Filtered below.
- **securityweek** — RSS 200, 10 items in feed, 5 in window. PRODUCTIVE — pm-001 (CISA/SharePoint exploited cluster). Remaining 4 filtered.
- **the-record** — RSS 200, 5 items in feed, 5 in window. All filtered (Patch-Tuesday recap = anti-noise; rest non-A&D/policy/consumer).
- **sans-isc** — RSS 200, 10 items in feed, 0 in 8h window.
- **krebs** — RSS 200, 10 items in feed, 0 in window (normal cadence).
- **unit42** — feedburner 200, 15 items in feed, 0 in window (normal cadence).
- **mstic** — RSS 200 (parent feed microsoft.com/en-us/security/blog/feed/), 1 in-window item = "Turning threat intelligence into decisive action with Defender Experts" (product-service marketing, Defender Experts MDR/TI launch). No threat-intel content, no roster actor, no A&D, no CVE — filtered.
- **cisa-advisories** — all.xml 200, 30 items, 2 in-window: (1) CISA/NSA joint CVD-program guidance (policy guidance, no match); (2) "CISA Adds Two KEV" — CVE-2023-4346 (KNX Association KNX Protocol account-lockout) + CVE-2026-46817 (Oracle E-Business Suite improper privilege mgmt). Neither is A&D-named, roster, or tracked-vuln — discarded per Mode 1 (documented below). BOD 26-04 referenced (KEV remediation regime).
- **splunk (archimedes + defenseclaw_local)** — targeted IOC sweep for SharePoint + named CVE IDs over last 24h: 0 non-archimedes-internal hits. First-party clean; visibility-bounded null. (No health ping issues; both indices reachable per prior sweeps.)

Not re-queried this sweep (scope + known state; no in-window lead required them): nvd (no fresh non-tracked CVE lead requiring lastModified pivot; SharePoint cluster CVEs already have IDs/context), crowdstrike (persistently barren marketing feed), rapid7, wired-security, recorded-future (dateless index), shodan/virustotal/abuseipdb (no enrichment trigger — pm-001 carries no atomic IP/domain/hash IOCs to enrich).

## Stale / skipped per health rules

- **mandiant** — feedburner RSS 404 long-entrenched; direct-HTML path is the operator-pending workaround. Not exercised this light afternoon window (stale >24h → try-once eligible, but no in-window lead warranted the direct-HTML pull; quiet publication cadence).
- **msrc** — feed parse error (stale since 2026-05-30); MSRC content reaches corpus via relays (today's Microsoft SharePoint material arrived via SecurityWeek + The Record).
- **ars-security** — security-path retired; root-feed workaround (not needed this sweep).
- **github-advisories** — 406 on global advisories.atom; per-repo GHSA fallback (not triggered — SharePoint CVEs are Microsoft-CNA, not GHSA).
- **x-cisagov / x-gossithedog** — nitter-bridge stale (bridge fragility). Not retried.
- **censys / urlscan / hibp / threatfox / malwarebazaar** — no-MCP / auth-injection limited; not invoked (no enrichment trigger).

No stale flips this sweep. No recovery attempts warranted (all under known-workaround states). No runtime source-health field changes made.

## Raw-signal written this sweep (1 substantive + this sentinel)

- **pm-001** — CISA urges immediate patching of actively exploited on-prem SharePoint cluster. Escalation surface for tracked **VT-037 / CVE-2026-56164** (July PT exploited zero-day, already finding-2026-07-14-0004). Broader named cluster: CVE-2026-32201 (Apr zero-day), CVE-2026-45659 (May OOB zero-day, KEV early July), plus critical CVE-2026-55040 + CVE-2026-58644. Post-exploitation = RCE + IIS machine-key theft. On-prem SE/2019/2016; no actor, no atomic IOCs. A&D relevance structural/high.

## Filtered / discarded (documented, not raw-signaled)

- "Google Gemini CLI abused as a hacking agent, malware botnet operator" (BC, Bill Toulas) — Russian-speaking actor "bandcampro" (not a roster actor), AI-tool-abuse + small botnet. No A&D / roster / tracked-vuln hit. AI-abuse trend noted for awareness.
- "AsyncAPI npm packages infected with credential-stealing malware" (BC, Bill Toulas) — 5 malicious AsyncAPI npm versions delivering info-stealer RAT. Supply-chain compromise but no tracked CVE (distinct from VT-006 TanStack / Mini Shai-Hulud), no roster actor, no named A&D prime. Structural SDLC relevance only — does not clear Mode 1 filter. Flagged for awareness (npm supply-chain pattern continues).
- "We built a vulnerability vending machine: AI tokens in, zero-days out" (BC) — sponsored by Intruder. Filtered (sponsored).
- "Unpatched Cursor Vulnerability Exposes Users to Code Execution" (SecurityWeek) — Cursor AI IDE auto-executes git.exe from a malicious repo root. Dev-tooling RCE, unpatched; no CVE assigned in source, no roster actor, no named prime. Structural SDLC relevance only — no Mode 1 filter hit. Awareness.
- "Windows Bind Link Attacks Can Hide Malware From EDR Tools" (SecurityWeek, Bitdefender research) — EDR-evasion technique via Windows bind links / conflicting filesystem views. No CVE, no actor, no A&D. Defensive-interest TTP noted for awareness; no filter hit.
- "Virtual Event Today: Cloud & Data Security Summit" (SecurityWeek) — event promo. Filtered.
- "US Charges Russian Individuals and Firms for Running Cybercrime Services" (SecurityWeek, Eduard Kovacs) — DOJ charges vs previously-sanctioned Russian bulletproof-hosting operators/firms. Cybercrime-infrastructure LE action; no roster actor named, no A&D, no tracked vuln. Likely continuation of prior sanctioned-BPH takedown coverage (cf. 07-14 Media Land indictment). Awareness only — no filter hit.
- "Microsoft smashes Patch Tuesday record for second successive month" (The Record) — 622-bug July PT recap. ANTI-NOISE vs already-covered Patch Tuesday (raw-2026-07-14-pm-001 / finding-2026-07-14-0004); SharePoint content folded into pm-001. Not separately raw-signaled.
- "Trump's DNI pick grilled about election security, voter fraud" (The Record) — policy/politics. No hit.
- "23andMe reaches $18 million settlement with states for massive breach" (The Record) — consumer-breach settlement. No A&D / roster / vuln hit.
- "Dutch police dismantle global crypto investment scam, arrest alleged mastermind" (The Record) — fraud/LE. No hit.
- "LAPD sidelines relationship with license-plate reader company Flock Safety" (The Record) — privacy/policy. No hit.
- "Turning threat intelligence into decisive action with Defender Experts" (MSTIC blog) — product-service launch marketing. No threat-intel content. Filtered.
- CISA KEV in-window adds CVE-2023-4346 (KNX Protocol) + CVE-2026-46817 (Oracle E-Business Suite) — actively-exploited per CISA but neither A&D-named, roster, nor tracked-vuln. Discarded per Mode 1; flagged for vuln-tracker awareness (Oracle EBS is enterprise-ERP-pervasive; not currently on watchlist).
- CISA/NSA joint CVD-program guidance (cisa-advisories) — best-practice policy guidance, not threat intel. No hit.

## Notes for downstream

- Grader 16:00 queue: **pm-001** (tracked VT-037 escalation — CISA patch-now advisory + broader exploited SharePoint cluster; single in-window relay = SecurityWeek B, underlying authority CISA A). Suggest grader/vuln-tracker weigh a VT-037 state update (KEV 3-day; cluster expansion to CVE-2026-32201 / -45659; machine-key-theft persistence angle) and direct-retrieve the CISA KEV entries for -32201 / -45659 (relay-only this sweep).
- vuln-tracker candidates: VT-037 SharePoint cluster escalation (pm-001). Awareness-only (no dossier action from collector): Oracle E-Business Suite CVE-2026-46817 KEV add; AsyncAPI npm supply-chain compromise; Cursor IDE unpatched RCE.
- No policy violations, no credential exposure, no controlled-information triggers this sweep. No SpiderFoot / active-recon requests. No authorized-targets scans.
