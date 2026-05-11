---
raw_id: raw-2026-05-11-am-000
collected_at: 2026-05-11T07:32:00-04:00
run_id: pre-brief-20260511-073000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-11T07:30:00-04:00
time_window_start: 2026-05-10T17:30:00-04:00
time_window_end: 2026-05-11T07:30:00-04:00
test: false
sources_queried:
  - cisa-kev               # JSON feed via WebFetch — three most recent KEV adds unchanged from 06:00 FLASH sweep (CVE-2026-42208 BerriAI LiteLLM 2026-05-08 dueDate 2026-05-11 today, CVE-2026-6973 Ivanti EPMM 2026-05-07 dueDate 2026-05-10 yesterday-passed, CVE-2026-0300 PAN-OS 2026-05-06 dueDate 2026-05-09 passed). ZERO entries dated 2026-05-09, 2026-05-10, or 2026-05-11. CVE-2026-42208 LiteLLM BOD-22-01 deadline 2026-05-11 today ~T-12h-to-T-16h from 08:00 brief. No KEV-update reflecting compliance status on CVE-2026-6973 or CVE-2026-0300 (standard pattern; KEV does not publish compliance-status changes on catalog itself)
  - cisa-advisories        # all.xml RSS via rss-bridge — status 200, 30 items in feed total, 0 items in 14h window. Direct page fetch on cisa.gov/news-events/cybersecurity-advisories returns 403 (WAF persistent — all.xml remains productive endpoint)
  - bleepingcomputer       # RSS via rss-bridge — status 200, etag 4e590c277fc3bebc9c0006711e4a94c2, last_modified 2026-05-11T11:23:08 GMT = 07:23 EDT (within window from feed-server activity), 1 item in 14h window after since-filter — "TrickMo Android banker adopts TON blockchain for covert comms" (2026-05-11T09:03:02 UTC = 05:03 EDT). WebFetch confirmed: Android banking malware variant, researcher = ThreatFabric (Trickmo.C tracking) + Zimperium (Oct 2024 prior). Geography France/Italy/Austria/Europe broadly. Target users banking + crypto wallet. Novel TON blockchain C2 with .ADNL addresses on infected device. NO threat-actor / APT / nation-state attribution. NO IOCs in article (C2 domains/IPs/hashes not disclosed). NO A&D / aerospace / defense organizations named. DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit)
  - securityweek           # RSS via rss-bridge — status 200, etag W/"7cc01d5aa82dca54baa74a81f2ae5222", last_modified 2026-05-11T11:25:10 GMT = 07:25 EDT (within window from feed-server activity), 7 items in 14h window after since-filter. (1) Cloudflare layoffs 2026-05-11T11:25 UTC — business/management news, NOT threat intel, DISCARDED. (2) SailPoint discloses GitHub repository hack 2026-05-11T10:52 UTC = 06:52 EDT — RAW-SIGNALED as raw-2026-05-11-am-001 (non-FLASH grader-queue item; IGA-vendor compromise, TeamPCP rumored-unconfirmed connection per Hard Rule 2 framing, A&D-capability-level relevance, no IOCs). (3) Checkmarx Jenkins AST plugin compromise 2026-05-11T09:34 UTC = 05:34 EDT — already raw-signaled at raw-2026-05-11-flash-0600-001 (06:00 FLASH), anti-noise applies. (4) Canvas system online after cyberattack 2026-05-11T08:35 UTC = 04:35 EDT — Canvas/ShinyHunters AP wire follow-up, anti-noise vs prior corpus coverage. (5) New Dirty Frag Linux vulnerability possibly exploited 2026-05-11T08:15 UTC = 04:15 EDT — Dirty Frag finding-2026-05-08-0005 follow-up coverage on CVE-2026-43284/43500 framing, anti-noise applies. (6) Crimenetwork marketplace takedown 2026-05-11T07:25 UTC = 03:25 EDT — already covered in 2026-05-10 12:00 FLASH BleepingComputer notes, anti-noise applies. (7) Over 500 Organizations Hit in Years-Long Phishing Campaign 2026-05-11T03:49 UTC = 23:49 EDT prior-evening — already raw-signaled at raw-2026-05-11-flash-0000-001 (00:00 FLASH; HookedWing SOCRadar), anti-noise applies
  - the-record             # RSS via rss-bridge — status 200, 0 items in 14h window (5 items total in feed, most recent 2026-05-08-dated). No fresh in-window content
  - krebs                  # RSS via rss-bridge — status 200, last_modified 2026-05-08T15:10 GMT pre-window, 0 items in 14h window — normal Krebs cadence (multi-day publication interval continues)
  - mstic                  # RSS via rss-bridge (parent feed microsoft.com/en-us/security/blog/feed/) — status 200, etag "031198440f0683102d67b8fe39f97c4b-gzip", last_modified 2026-05-08T23:03:04 GMT pre-window (unchanged across SEVEN consecutive sweeps now), 0 items in 14h window. Most recent MSTIC content remains 2026-05-08T17:12 UTC Dirty Frag active-attack post (~86h aged at this sweep)
  - unit42                 # RSS (feedburner) via rss-bridge — status 200, last_modified 2026-05-08T21:09:40 GMT pre-window (unchanged across SIX consecutive sweeps), 0 items in 14h window. Unit42 feedburner stable but quiet through late-week into Monday-morning window
  - sans-isc               # RSS via rss-bridge — status 200, etag W/"1b5f-651890dcd5e81", last_modified 2026-05-11T11:29:04 GMT = 07:29 EDT (within window from feed-server activity), 2 items in 14h window — (1) ISC Stormcast For Monday May 11 (podcast detail, 2026-05-11T02:15:11Z = 22:15 EDT 2026-05-10, awareness-only no body content) and (2) YARA-X 1.16.0 Release (2026-05-10T22:37:08Z = 18:37 EDT just inside window, tool release announcement, no threat-intel claim). Both DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit). failure_count remains at 0 (recovered from 2026-05-10 18:00 transient dual-endpoint failure two sweeps ago)
  - rapid7                 # RSS via rss-bridge — status 200, last_modified 2026-05-11T11:17:04 GMT = 07:17 EDT (within window from feed-server activity), 0 items in 14h window after since-filter
  - crowdstrike            # RSS via rss-bridge — status 200, etag "15dd-65186ea8f3e6f-gzip", last_modified 2026-05-11T08:56:02 GMT = 04:56 EDT (within window from feed-server activity), 10 items returned ALL with null published_at (consistent persistent pattern across 15 consecutive sweeps now). Identical dateless marketing pile (Gartner MQ CTI Leader, Falcon OverWatch for Defender, Risk Assessments, AI Vuln Discovery podcast, CORDIAL/SNARKY SPIDER product marketing, ChatGPT Enterprise integration, Frost & Sullivan CNAPP, GCP RTCDR expansion, ROI marketing). No 2026-05-09/10/11 dated threat-intel content
  - sentinelone-labs       # RSS via rss-bridge (sentinelone.com/labs/feed/) — status 200, etag W/"b7504c24cc8243da39ea05fb832bee74", last_modified 2026-05-08T23:44:58 GMT pre-window (unchanged across SEVEN consecutive sweeps now), 0 items in 14h window
  - sophos                 # RSS via rss-bridge (news.sophos.com/feed/) — status 200, 9 items total in feed, 0 items in 14h window
  - eset-welivesecurity    # RSS via rss-bridge (welivesecurity.com/en/rss/feed/) — status 200, 100 items total in feed, 0 items in 14h window
  - mandiant               # feedburner.com/Mandiant returned 404 (fifteenth consecutive failure; failure_count 13→14). Cloud.google.com/blog/topics/threat-intelligence/rss alt path same malformed body. Index-page WebFetch from prior FLASH sweep confirmed top-8 titles unchanged (UNC6692, German Cyber Überfall, BRICKSTORM, UNC1069, M-Trends 2026, DarkSword, Ransomware Under Pressure, Proactive Preparation 2026) — all out-of-window per prior triangulations. Pattern fully entrenched; operator alt-endpoint decision still pending
  - cyberwarrior76         # RSS via rss-bridge (substack feed) — status 200, etag W/"1a2c01-RuEamGhnxuZNEtj3u9S/Yz92jAI", 20 items total in feed, 1 item in 14h window after since-filter — "THE INVISIBLE COMMAND Why Prompt Injection Is the #1 AI Security Crisis of 2026" (2026-05-11T03:20:24 UTC = 2026-05-10T23:20 EDT). Long-form OWASP LLM01 deep-dive analysis methodology piece by Cyber News Network (provisional-C OSINT). NO specific threat actor / NO IOCs / NO CVE / NO A&D-target named. Educational / methodology framing on prompt injection vulnerability class. Cited research: OWASP, NIST GenAI Risk Profile, UK NCSC, OpenAI red-team work, Microsoft AETHER, IBM watsonx.governance, MITRE ATLAS, NVIDIA NeMo Guardrails, ReAct-agent attack-success research. Methodology-piece scope — DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit). Flagged as awareness item — operator may want to capture cyberwarrior76 prompt-injection methodology content elsewhere in the corpus (capability brief, doctrine update, etc.); collector does not promote to grader queue
  - nvd                    # NVD lastModStartDate window-query 2026-05-11T08:00 → 11:30 UTC = 2026-05-11T04:00 → 07:30 EDT for the post-06:00-FLASH partial-window remainder. cvssV3Severity=CRITICAL → 0 results. cvssV3Severity=HIGH → 0 results. Empty vulnerabilities array for both severities. NVD endpoint remains healthy and responsive. (The earlier 6h window 2026-05-10T22:00→2026-05-11T04:00 UTC was covered by the 2026-05-11 00:00 FLASH sweep — CVE-2026-8260 D-Link IP camera consumer-class DISCARDED then.)
  - splunk-archimedes      # tstats over 24h NOT sourcetype=archimedes:* — zero events. Targeted IOC keyword sweep across 16 high-priority tokens (CVE-2026-42208, CVE-2026-6973, CVE-2026-0300, Checkmarx, TeamPCP, TrickMo, HookedWing, SailPoint, UNC1549, MuddyWater, APT28, APT29, APT37, Charming Kitten, plus duplicates) returned 7 hits — ALL archimedes:operation pipeline self-references (1x flash_sweep_clean 2026-05-11 06:00 EDT; 1x flash_sweep 2026-05-11 00:00 EDT; 1x threat_box_scoring_completed APT37 MEDIUM 2026-05-10 17:48 EDT; 1x brief_published afternoon 2026-05-10 16:20 EDT; 1x git_committed morning brief 2026-05-10 08:14 EDT; 1x finding_superseded MuddyWater A2→C3 2026-05-10 08:13 EDT; 1x brief_published morning 2026-05-10 08:13 EDT). Pipeline self-references, not external observations. Thirteenth consecutive sweep with dormant non-archimedes-internal stream pattern
  - splunk-defenseclaw     # tstats over 24h NOT sourcetype=archimedes:* — zero events. Index appears not receiving live security telemetry (thirteenth consecutive sweep with this pattern)
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted (4 consecutive 404s; now ~54h since stale flip). Alt-instance investigation pending. Operator-decision-required
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404 (3 consecutive failures; now ~40h since stale flip). Workaround: arstechnica.com/feed/ root feed valid as RSS but site-wide; needs security-tag filter. Operator-decision-required
  - x-cisagov              # STALE since 2026-05-10 12:00 — nitter.net WinError 10060 connection timeout (3 consecutive failures; now ~19.5h since stale flip). Eligible-to-retry rule fires after 2026-05-11T12:00 (next noon FLASH ~T+4.5h from this sweep). Held stale this sweep
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom (per-repo GHSA fallback path remains productive workaround when triggered; not triggered this sweep — no fresh CVE leads required global GHSA pivot)
  - iran-monitor           # 403 from prior sweep, deferred until WAF/UA workaround
  - dragos                 # /blog/feed/ 404 again this sweep — second observed failure on this path (same pattern as 2026-05-09 15:30 sweep). Not a stale flip — collector-side path-discovery issue. /blog/ landing page reachable via WebFetch (validate on next sweep with alt path discovery — possible paths to test: /resources/, /research/, /threat-research/). Recommend operator identify a working dragos.com RSS path
  - proofpoint             # /us/threat-insight/blog/feed remains 404 (operator-side alt-RSS-path discovery for threat-intel-specific surface still pending; corporate-news /us/rss.xml RECOVERED 2026-05-11 00:00 FLASH but not threat-research grade)
sources_health_recovered_this_sweep: []
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (fifteenth consecutive); failure_count 13→14. Index-page workaround viable for title surfacing only. Held healthy pending operator alt-endpoint decision
  - bleepingcomputer       # 1 in-window item (TrickMo Android TON), DISCARDED per Mode 1 filter (banking malware, no A&D / roster / CVE match). failure_count remains 0
  - securityweek           # 7 in-window items, productive sweep. (1) SailPoint GitHub repo hack RAW-SIGNALED as raw-2026-05-11-am-001 (non-FLASH grader-queue item). (6) other items either non-threat-intel (Cloudflare layoffs) or anti-noise vs prior corpus coverage (Checkmarx Jenkins AST from 06:00 FLASH; Canvas ShinyHunters; Dirty Frag CVE-2026-43284/43500; Crimenetwork takedown; HookedWing SOCRadar from 00:00 FLASH). failure_count remains 0
  - cyberwarrior76         # 1 in-window methodology piece (THE INVISIBLE COMMAND prompt injection deep-dive), DISCARDED per Mode 1 filter (no specific threat actor / IOC / CVE / A&D target). failure_count remains 0. Flagged as awareness item — operator may want to capture cyberwarrior76 prompt-injection methodology content elsewhere
  - sans-isc               # 2 in-window items (Stormcast podcast + YARA-X 1.16.0 release), both DISCARDED per Mode 1 filter. failure_count remains 0. RECOVERY held from 2026-05-11 00:00 FLASH (the 2026-05-10 18:00 dual-endpoint failure remained transient)
  - nvd                    # PRODUCTIVE this sweep — lastModStartDate window-query for post-06:00-FLASH remainder (2026-05-11T04:00→07:30 EDT) cvssV3Severity=CRITICAL/HIGH both returned 0 results (empty vulnerabilities arrays). NVD endpoint health and query mechanism re-confirmed
findings_in_window_to_filter: |
  Total items surfaced across all queried sources in 14h window:
    - BleepingComputer: 1 (TrickMo Android TON, DISCARDED)
    - SecurityWeek: 7 (1 RAW-SIGNALED → SailPoint; 6 anti-noise/non-threat-intel)
    - SANS-ISC: 2 (both DISCARDED)
    - Cyberwarrior76: 1 (methodology piece, DISCARDED)
  Plus already-raw-signaled-pre-window from FLASH sweeps:
    - HookedWing SOCRadar via SecurityWeek (raw-2026-05-11-flash-0000-001, 2026-05-11 00:00 FLASH)
    - Checkmarx Jenkins AST via SecurityWeek (raw-2026-05-11-flash-0600-001, 2026-05-11 06:00 FLASH)
  Net new raw-signal this pre-brief sweep: 1
    - raw-2026-05-11-am-001 (SailPoint GitHub repo hack)
flash_evaluation_summary:
  total_in_window_candidates_evaluated: 1
  flash_candidates_promoted: 0
  flash_triggers_evaluated: 6
  flash_triggers_fired: 0
  non_flash_grader_queue_items: 1     # SailPoint (raw-2026-05-11-am-001)
  carry_forward_from_prior_sweeps:
    - raw-2026-05-11-flash-0000-001  # HookedWing SOCRadar
    - raw-2026-05-11-flash-0600-001  # Checkmarx Jenkins AST plugin compromise
quiet_hours_active: false             # 07:32 EDT is post-09:00 quiet-hours-end boundary; standard pre-brief windowing applies
discord_post_status: not_applicable_pre_brief_collection_orchestrator_briefer_owns_publishing
notes: |
  Pre-brief collection sweep for 2026-05-11 morning brief (08:00 EDT). 14h window 2026-05-10T17:30 → 2026-05-11T07:30 EDT. NEAR-CLEAN sweep — 1 net new raw-signal file written (SailPoint GitHub repo hack via SecurityWeek). Plus 2 carry-forwards from prior FLASH sweeps (HookedWing, Checkmarx Jenkins AST).

  Key observations for the grader inheriting this sweep:

  1. SUPPLY-CHAIN PATTERN CONTINUATION: SailPoint joins Checkmarx Jenkins AST as same-day supply-chain compromise disclosures. Both reference (rumored or restated) TeamPCP attribution chain from prior reporting. Hard Rule 2 framing applies — Archimedes does NOT originate. The morning brief may want to note the SailPoint+Checkmarx temporal cluster under Supply-Chain Watch framing rather than treating each as fully independent disclosure. Both items have IDENTICAL A&D-relevance shape (capability-level / structural, no named primes, vendor-self-disclosure-source-class).

  2. KEV BACKLOG WATCH: CVE-2026-42208 BerriAI LiteLLM SQL Injection BOD-22-01 deadline 2026-05-11 today ~T-12h-to-T-16h from 08:00 brief. CVE-2026-6973 Ivanti EPMM deadline 2026-05-10 yesterday-passed without KEV compliance update (standard pattern). CVE-2026-0300 PAN-OS deadline 2026-05-09 still un-updated. No new KEV adds in window.

  3. SPLUNK FIRST-PARTY STREAM: Dormant for non-archimedes-internal events across both indexes (archimedes + defenseclaw_local) over 24h. 13th consecutive sweep with this pattern. Trigger 3 cannot fire on a dormant telemetry stream.

  4. CYBERWARRIOR76 PROMPT INJECTION DEEP-DIVE: First substantive methodology piece from this source in many sweeps (substack has been quiet since 2026-05-06). Long-form OWASP LLM01 analysis — not a raw-signal grader-queue item per Mode 1 filter (no specific threat actor / IOC / CVE / A&D target named) but flagged here as awareness piece. Operator may want to capture cyberwarrior76 prompt-injection methodology content elsewhere in corpus (e.g., capability brief if/when AI tradecraft becomes a structural Archimedes thread; doctrine reference). Provisional-C grade source — does not clear morning-brief promotion bar even as inventory mention without primary-source corroboration.

  5. SOURCE-HEALTH DEGRADATIONS HOLDING: Mandiant feedburner 15th consecutive 404 (failure_count 13→14, held healthy pending operator alt-endpoint decision); CrowdStrike 15th consecutive dateless marketing pile (held healthy, persistent pattern); Dragos /blog/feed/ 404 again (recommend operator path-discovery); Proofpoint /us/threat-insight/blog/feed remains 404 (corporate-news /us/rss.xml recovered but not threat-research grade). All operator-decision-required.

  6. NEW PROVISIONAL SOURCE-GRADE-LOG CANDIDATES SURFACED THIS WINDOW (not actioned by collector):
     - SOCRadar (HookedWing primary research, would be provisional-C on first surface per LayerX/Seqrite/Trendyol-Group-Albayrak precedent)
     - ThreatFabric (TrickMo research, would be provisional source-grade-log candidate)
     - HiddenLayer (mentioned in prior 2026-05-09 15:30 sweep — fake OpenAI HF repo / sefirah infostealer research)
     - SOCRadar especially noteworthy given the aviation-sector reference in HookedWing; if operator ratifies as B or upgrades to A on track-record observation, the aviation token in 7-sector listings becomes higher-trust for future A&D-edge filtering

  7. NEW /NEW-ACTOR CANDIDATES SURFACED (not actioned by collector):
     - Lapsus$ / DEV-0537 / Strawberry Tempest (mentioned in Checkmarx Jenkins AST piece from 06:00 FLASH; NOT in roster.yaml)
     - UNC6692 (Mandiant Snow Flurries — Teams social engineering; awareness item since 2026-05-09 15:30 sweep)
     - UNC1069 (Mandiant DPRK-nexus Axios npm supply chain; awareness item since 2026-05-09 15:30 sweep)
     - Star Blizzard / DarkSword (Proofpoint research alias; awareness item since 2026-05-09 00:00 FLASH)
     All require operator decision on /new-actor workflow; collector does NOT originate.

  No FLASH triggers fired during this pre-brief sweep window evaluation; no Discord-post required (briefer/orchestrator owns morning brief publishing at 08:00 EDT).
---

# Pre-brief collection sweep 2026-05-11 07:30 EDT — NEAR-CLEAN

This is the sentinel raw-signal file for the 2026-05-11 07:30 EDT pre-brief collection run feeding the 08:00 EDT morning brief.

**Mode:** pre_brief_collection per collector.md Mode 1 procedure.
**Window:** 2026-05-10T17:30 → 2026-05-11T07:30 EDT (14h).
**Outcome:** NEAR-CLEAN — 1 net new raw-signal file written.

## Source sweep summary

24 sources queried; 6 stale-skipped (3 MCP/key-missing, 3 nitter/Cloudflare/feed-retired chain); 5 soft-fail-skipped (threatfox/malwarebazaar awaiting MCP, github-advisories 406, iran-monitor 403, dragos path-discovery, proofpoint /us/threat-insight retired). 4 productive sources (BleepingComputer, SecurityWeek, SANS-ISC, Cyberwarrior76); 1 net new raw-signal promoted (SailPoint).

## Mode 1 procedure outcome

- **Total in-window candidate items across all sources:** 11 (1 BC + 7 SW + 2 SANS + 1 CW76 — plus the 2 prior-sweep carry-forwards)
- **Items DISCARDED at Mode 1 filter:** 10
  - 1 BC item (TrickMo banking malware — no A&D / roster / CVE match)
  - 6 SW items (Cloudflare layoffs non-threat-intel, plus 5 anti-noise items vs prior corpus coverage)
  - 2 SANS items (Stormcast podcast + YARA-X release announcement)
  - 1 CW76 item (prompt injection methodology piece)
- **Items RAW-SIGNALED as non-FLASH grader-queue:** 1
  - SailPoint GitHub repo hack via SecurityWeek (raw-2026-05-11-am-001)
- **Items FLASH-trigger-evaluated to fire:** 0 (zero FLASH triggers matched in window; SailPoint marginal-FAIL on Trigger 4 composite-source-grade and Trigger 2 new-attribution-test per Hard Rule 2 framing)

## Carry-forward state for 08:00 morning brief

Items from prior FLASH sweeps within the morning brief's relevance window (these are NOT this sweep's outputs, but they're listed for grader continuity):

- **raw-2026-05-11-flash-0000-001** — HookedWing SOCRadar 500+ org phishing campaign with aviation sector token. Marginal Trigger 5 + Trigger 4 composite-source-grade fails; grader-queue candidate.
- **raw-2026-05-11-flash-0600-001** — Checkmarx Jenkins AST plugin compromise. Trigger 2 restatement fails; grader-queue candidate; supply-chain pattern continuation.
- **raw-2026-05-11-am-001** (THIS SWEEP) — SailPoint GitHub repo hack. Trigger 2 rumored-unconfirmed fails; grader-queue candidate; supply-chain pattern continuation.

## Notes for the grader

See per-source observations in the YAML `sources_queried` and `notes` fields above, plus the detailed Grader Notes section in raw-2026-05-11-am-001.

The grader should especially weigh:
1. Whether SailPoint + Checkmarx Jenkins AST cluster under a single supply-chain finding (existing finding-2026-05-08-0008 TeamPCP supply-chain tracking thread or a new finding-2026-05-11-NNNN)
2. KEV deadline backlog status (CVE-2026-42208 today; CVE-2026-6973 yesterday-passed; CVE-2026-0300 still-passed)
3. Splunk 13th-consecutive-sweep dormant pattern (Trigger 3 cannot fire on a dormant telemetry stream — this is a Hard Rule 8 anti-overweight observation, not disconfirmation)
4. Source-health degradation pile (mandiant + crowdstrike + dragos + proofpoint operator-decision-required)
