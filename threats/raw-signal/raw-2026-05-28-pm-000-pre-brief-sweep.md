---
source: archimedes-internal
source_grade: N/A
collected_at: 2026-05-28T15:35:00-04:00
sweep: pre-brief-2026-05-28-pm
url: null
test: false
sentinel: true
sweep_type: pre-brief-collection
status: complete
mode: pre_brief_collection
invocation: scheduled pre-brief PM-28 cycle (15:30 EDT)
sweep_window:
  start: 2026-05-28T08:00:00-04:00
  end: 2026-05-28T15:35:00-04:00
  duration_h: 7.58
prior_anchor:
  prior_sweep_id: flash-2026-05-28-1200
  anchor_at: 2026-05-28T12:35:00-04:00
  raw_ids:
    - raw-2026-05-28-flash-1200-001 (FortiClient EMS CVE-2026-35616 Arctic Wolf fresh exploitation, promoted to finding-2026-05-28-FLASH-1200-0001 B2)
    - raw-2026-05-28-flash-1200-002 (Gogs zero-day RCE Rapid7 no-patch, promoted to finding-2026-05-28-FLASH-1200-0002 A2)
    - raw-2026-05-28-flash-1200-003 (Chaotic Eclipse Defender / BitLocker zero-day publication, MSRC pushback — single-source veto, not promoted)
prior_brief_anchor:
  brief_id: 2026-05-28-morning
  shipped_at: 2026-05-28T08:00:00-04:00
  notes: |
    AM-28 morning brief covered Carnival ShinyHunters 6M confirmation
    (B2; finding 0001), Unit 42 World Cup attack surface — Iran IRGC /
    MOIS / Razing Ursa / Handala / Cyberav3ngers (A2; finding 0002),
    Unit 42 Out of the Crypt extortion economy — TGR-CRI-1135 TeamPCP
    + Bling Libra ShinyHunters + Hazy Scorpius CL0P (A2; finding 0003),
    NVD critical CVE batch — Samba CVE-2026-4408 9.0 + X.Org CVE-2026-
    34000/34002 9.1 + Red Hat Quay CVE-2026-32590 8.8 (A2; finding 0004).
    Standing carry-forwards include LiteSpeed CVE-2026-48172 + Exchange
    OWA CVE-2026-42897 KEV deadlines tomorrow Fri 2026-05-29.

match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sentinel, pre_brief_sweep, pm_pre_brief_28]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-26T15:35:00-04:00
---

# PM-28 Pre-Brief Sentinel Sweep — 2026-05-28 15:30 EDT

## Sweep summary

Standard scheduled afternoon collection ahead of the 16:00 EDT brief. Time window 08:00 → 15:35 EDT (~7.6h since morning brief publication). Sweep returned **seven raw-signal candidates** for grader review at the 16:00 phase. Source set queried per source-grades.yaml v1 (last_updated 2026-05-28T12:35:00-04:00) with status filters per source-health.yaml.

## Raw-signal candidates this sweep

- **raw-2026-05-28-pm-001** — *Pentagon CENTCOM acknowledges adversary exploitation of commercial location data targeting US troops in theater* (Wired investigation + Reuters exclusive; Senator Wyden reports + USCENTCOM statement; multi-source convergence) — **A&D-direct DoD operational tradecraft** — high-priority candidate.
- **raw-2026-05-28-pm-002** — *MSTIC analysis of The Gentlemen ransomware (Storm-2697 RaaS)* — Go-based encryptor, 21-vector lateral movement, BreachForums affiliate partnership; targeted sectors include education, **transportation**, healthcare, financial; geographies multi-continent — A-grade vendor research, transportation sector named as A&D-tier-2/3 adjacency.
- **raw-2026-05-28-pm-003** — *SecurityWeek/WithSecure on GreyVibe Russia-nexus AI-augmented actor* — uses ChatGPT + Google Gemini + Ideogram AI; targets Ukrainian military/government/civilian; PhantomRelay / LegionRelay / Fallspy malware families; possible new roster candidate flagged for orchestrator review.
- **raw-2026-05-28-pm-004** — *CISA alert: Supply Chain Compromises Impact Nx Console and GitHub Repositories* — official government escalation linking Nx Console VSCode extension + Megalodon + GitHub breach into single CISA advisory; federal escalation signal on a corpus-tracked threat surface.
- **raw-2026-05-28-pm-005** — *Group-IB Ghost Stadium China-criminal FIFA 2026 World Cup fraud cluster* (BleepingComputer + The Record convergence; FBI PSA260527 IC3 alert) — 4,300 fraud domains since Aug 2025, premium-ticket and employment-fraud surface; consumer-focused with no A&D direct tie but pairs with morning brief's Unit 42 Iran framing as second sector-corroborating angle.
- **raw-2026-05-28-pm-006** — *GCHQ director Anne Keast-Butler briefing on Russia daily hybrid attacks on UK from seabed to cyberspace* (The Record / Alexander Martin) — subsea cables, energy pipelines, critical infrastructure, supply chains; A&D-indirect via UK defense estate; no UK A&D primes named.
- **raw-2026-05-28-pm-007** — *CISA ICS advisory batch — 10 advisories published 12:00 UTC* including **MacGregor Voyage Data Recorder G4e** (maritime/transport CVSS 8.3 multi-CVE), **XCharge C6 EV charger** (CVSS 9.8 firmware-integrity), **Schneider Electric EcoStruxure Machine Expert HVAC**, **ABB EIBPORT KNX**, **Jinan PUSR USR-W610 hardcoded creds CVSS 9.8**, plus medical (Fourth Frontier) and CCTV (KMW, CP Plus) entries; CISA-A grade procedural facts.

## Sources touched this sweep

**Healthy + productive:**
- bleepingcomputer (6 items in window, 2 raw-signal-worthy: FBI World Cup + FortiClient EMS already covered in 12:00 FLASH)
- securityweek (7 items in window, 2 raw-signal-worthy: GreyVibe + Carnival already in morning brief)
- the-record (4 items in window, 3 raw-signal-worthy: Carnival anti-noise + Ghost Stadium World Cup + GCHQ Russia)
- thehackernews (4 items in window, all already covered in morning brief or 12:00 FLASH — Gogs, FortiClient EMS, Chaotic Eclipse, ThreatsDay Bulletin marketing roundup not raw-signaled)
- mstic (1 item in window: The Gentlemen ransomware — productive A-grade vendor research)
- cisa-advisories (10 ICS advisories in window via all.xml, 1 special alert: Supply Chain Compromises Nx Console + GitHub + Megalodon)
- cisa-kev (KEV catalog refreshed 2026-05-28T16:27Z but ZERO new dateAdded entries today; most recent additions still CVE-2026-48027 + CVE-2026-45321 from 2026-05-27; LiteSpeed CVE-2026-48172 + Exchange OWA CVE-2026-42897 KEV due dates 2026-05-29 unchanged from morning carry-forward)
- nvd (lastModStartDate=2026-05-28T12:00 EDT → 15:30 EDT cvssV3Severity=CRITICAL query returned 9 results; all NON-A&D NON-tracked: 4 historical CVEs metadata-refresh-only — libxslt 2019-11068 / Log4j 2019-17571 / OpenSSH 2023-28531 / VLC 2023-47359; CVE-2026-34000 + 34002 X.Org already in morning brief finding 0004; CVE-2026-35223 Joomla webservice access-control 9.8 — non-A&D CMS; CVE-2026-44723 Vowpal Wabbit CI/CD shell injection 9.9 — niche ML CI/CD with no tracked-actor / A&D direct mapping; CVE-2026-24444 SDMC NE6037 cable modem 9.8 hardcoded password — consumer device. All DISCARDED per Mode 1.)
- wired-security (1 item in window — Pentagon troops phone tracking; raw-signaled despite WebFetch block via Reuters / Army Times / USNews triangulation)
- krebs (0 items in window — normal cadence; most recent post still 2026-05-25 13:21 GMT per last-modified header)
- sans-isc (0 items in window — normal cadence; rssfeed.xml last_modified 2026-05-28T19:29 GMT inside-window from feed-server activity but no fresh entries)
- crowdstrike (10 dateless marketing/MQ items — sixteenth consecutive sweep, pattern fully entrenched; anti-noise applies, anti-promoted)

**Stale / structural:**
- mandiant (feedburner 404 — fortieth-class consecutive failure; failure_count incremented 19 → 20; held healthy pending operator alt-endpoint decision per long-standing policy)
- msrc (msrc.microsoft.com/blog/feed returns parse error — transient or persistent unclear; parent feed Microsoft Security Blog reachable via mstic id which surfaced The Gentlemen successfully this sweep)
- ars-security (still stale per source-health stale_since 2026-05-09; arstechnica.com root feed remains workaround; not invoked this sweep)
- github-advisories (advisories.atom 406 persistent across many sweeps; per-repository GHSA fallback path remains the productive workaround when triggered; not triggered this sweep)
- unit42 (feedburner reachable, 0 items in window since prior sweep; Unit 42 already supplied two findings in morning brief at AM-002 and AM-003 — Out of the Crypt + World Cup attack surface — typical post-publication cadence quiet pattern)

## Source-health state changes this sweep

- **mandiant** — failure_count 19 → 20 (twentieth consecutive feedburner 404). last_error updated to reflect fortieth-class-failure pattern. Held healthy per operator-pending-decision policy.
- All other healthy sources updated last_successful_fetch to 2026-05-28T15:35:00-04:00.
- No flips healthy → stale or stale → healthy this sweep.

## Anti-noise applied

- Carnival ShinyHunters (BleepingComputer + The Record + SecurityWeek all cover) — already in morning brief finding 0001; anti-noise locked, NOT re-raw-signaled.
- FortiClient EMS CVE-2026-35616 (BleepingComputer Bill Toulas 17:25 UTC) — already covered in 12:00 FLASH finding-2026-05-28-FLASH-1200-0001; anti-noise locked.
- Gogs zero-day RCE (BleepingComputer Sergiu Gatlan 14:25 UTC + THN 17:24 UTC) — already covered in 12:00 FLASH finding-2026-05-28-FLASH-1200-0002; anti-noise locked.
- Microsoft pushback / Chaotic Eclipse (THN 13:53 UTC) — already covered in 12:00 FLASH raw-2026-05-28-flash-1200-003 (single-source veto candidate, not promoted); anti-noise locked.
- CrowdStrike marketing/MQ items — sixteenth consecutive entrenched-noise sweep; anti-noise locked.

## Operator-awareness items (NOT raw-signaled — flagged here per sweep discipline)

- **THN ThreatsDay Bulletin** (13:33 UTC) — multi-item editorial roundup mentioning Claude Security Plugin, Azure Priv-Esc, Kali365 MFA Bypass, FIFA Scams "+15 More" — too thin per-item signal-to-noise to raw-signal as a cluster; if any individual sub-item surfaces independently from another A/B-grade source it will be raw-signaled then.
- **SecurityWeek IBM/Red Hat $5B Project Lightwell** (12:41 UTC) — supply-chain-security funding announcement; non-threat-intel business news; not raw-signaled.
- **SecurityWeek Geordie $30M AI security funding** (17:07 UTC) — vendor funding business news; not raw-signaled.
- **SecurityWeek Edamame AI coding agent platform** (12:00 UTC) — vendor product launch; not raw-signaled.
- **SecurityWeek BTMOB Android malware** (13:05 UTC) — generic Android infostealer commodity-malware; consumer device, not A&D direct; not raw-signaled.
- **BleepingComputer Romanian Oregon hacking sentencing** (12:43 UTC) — US LE prosecution outcome; not A&D direct; not raw-signaled.
- **The Record Canadian luring child predator sentencing** (13:42 UTC) — non-cyber-threat content; not raw-signaled.

## Notes for the grader (PM-28 16:00 phase)

The seven raw-signal candidates below cluster into three threat surfaces and one infrastructure batch:

1. **DoD / military tradecraft cluster** — PM-001 (Pentagon troops phone tracking via commercial location data) is the strongest A&D-direct item this sweep. Operationally relevant to ITAR-regulated DIB workforce mobile-device tradecraft for personnel deployed to overseas test ranges, prime defense facilities, classified-area work. CENTCOM-named, Senator Wyden-corroborated, multi-source convergence.

2. **Ransomware / financial-criminal cluster** — PM-002 (The Gentlemen / Storm-2697 RaaS via MSTIC A-grade) names transportation in its sector list which has DIB-tier-2/3 logistics adjacency; the BreachForums RaaS-affiliate partnership signal accelerates affiliate-pool growth which is a recurring theme this corpus (TeamPCP, Bling Libra, ShinyHunters, CL0P).

3. **State / quasi-state actor cluster** — PM-003 (GreyVibe Russia-nexus AI-augmented operator, WithSecure attribution, Ukraine-targeted), PM-006 (GCHQ Russia daily hybrid attacks UK seabed-to-cyberspace), and tangentially PM-005 (Group-IB Ghost Stadium China-criminal World Cup fraud — pairs with morning brief's Iran framing on the World Cup attack-surface theme).

4. **Supply chain / SDLC cluster** — PM-004 (CISA alert escalating Nx Console + Megalodon + GitHub) is a government-source escalation on the standing TeamPCP / Mini Shai-Hulud / Megalodon SDLC threat surface already deeply corpus-tracked. Federal-escalation signal even though the underlying intrusions are corpus-anchored.

5. **ICS / OT batch** — PM-007 (CISA ICS advisory batch of 10) includes MacGregor VDR maritime + XCharge EV charger transportation as the highest-A&D-adjacency items; recommended to index as a single batch entry with per-advisory notes rather than expand each into its own finding unless grader chooses to promote on a specific A&D-direct angle.

GreyVibe (PM-003) is a candidate for /new-actor — WithSecure attribution language has the "Russia-nexus" hedge plus the "cybercriminal, nation-state, or mix" ambiguity which is consistent with the kind of pre-roster surface Archimedes scaffolds via /new-actor. Flagged for orchestrator awareness; not initiating /new-actor from collector.

End sentinel.
