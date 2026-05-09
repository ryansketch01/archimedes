---
raw_id: raw-2026-05-09-pm-000
collected_at: 2026-05-09T15:30:00-04:00
run_id: pre-brief-20260509-153000
collection_mode: pre_brief_collection
sweep_type: afternoon
sweep_time: 2026-05-09T15:30:00-04:00
time_window_start: 2026-05-09T07:30:00-04:00
time_window_end: 2026-05-09T15:30:00-04:00
test: false
sources_queried:
  - cisa-kev               # JSON feed via WebFetch — most recent KEV add is CVE-2026-42208 (2026-05-08); zero new entries dated 2026-05-09. CVE-2026-0300 PAN-OS BOD-22-01 deadline expired today (no compliance-status update reflected in catalog yet)
  - cisa-advisories        # all.xml RSS via rss-bridge — 0 items in 8h window. Direct landing page /news-events/cybersecurity-advisories returned 403 again (consistent — only the all.xml endpoint works)
  - cisa-ics-advisories    # ICS-specific advisories.xml RSS via rss-bridge — 0 items in 8h window (no ICS-CERT publications dated 2026-05-09)
  - bleepingcomputer       # RSS via rss-bridge — 2 items in 8h window. Both items reviewed and DISCARDED per Mode 1 (no watchlist/roster/vuln-index match):
                           #   1) JDownloader site hack delivering Python RAT (Windows + Linux installers) — C2 parkspringshotel[.]com, auraguest[.]lk, checkinnhotels[.]com — researcher Thomas Klemenc + Reddit user PrinceOfNightSky — generic Windows download manager, no A&D customer base, no actor attribution, no tracked CVE
                           #   2) Fake OpenAI Hugging Face repo "Open-OSS/privacy-filter" pushing "sefirah" Rust infostealer — C2 recargapopular[.]com — researcher HiddenLayer — reached #1 on HF trending with 244k downloads (likely inflated) — no A&D mention, no roster attribution, no tracked CVE
                           # Both items are commodity-malware / supply-chain compromises with broad-consumer-impact framing, not within current Archimedes A&D-prime tracking scope. Site homepage review on bleepingcomputer.com confirmed via WebFetch — these are the only two 2026-05-09-dated articles surfaced
  - securityweek           # RSS via rss-bridge — 0 items in 8h window. Site homepage review via WebFetch confirmed zero 2026-05-09-dated articles — most recent items all 2026-05-08-dated (Train Hacker/PamDOORa/CISA Director, Polish ICS, Braintrust, Canvas, PCPJack, Trellix, ClaudeBleed, Ivanti EPMM)
  - the-record             # RSS via rss-bridge — 0 items in 8h window. Site homepage review confirmed zero 2026-05-09-dated articles — most recent are 2026-05-08 (GM/CCPA settlement, Virginia gov-database deletion)
  - krebs                  # RSS via rss-bridge — 0 items in 8h window
  - mstic                  # RSS via rss-bridge — 0 items in 8h window. Most recent MSTIC content remains the 2026-05-08T17:12 UTC Dirty Frag active-attack post (already covered in finding-2026-05-08-0001 carry)
  - unit42                 # RSS (feedburner) via rss-bridge — 0 items in 8h window. Most recent Unit42 activity dated 2026-05-07T21:26 UTC
  - sans-isc               # RSS via rss-bridge — 0 items in 8h window
  - rapid7                 # RSS via rss-bridge — 0 items in 8h window
  - crowdstrike            # RSS via rss-bridge — 10 items returned, ALL with null published_at. Same dateless marketing/MQ pile observed across 8 consecutive sweeps (Gartner MQ leader, Falcon OverWatch for Defender, Risk Assessments, AI Vuln Discovery podcast, CORDIAL/SNARKY SPIDER product marketing, ChatGPT Enterprise integration, Frost & Sullivan, ROI marketing). Site homepage review earlier today confirmed most recent post 2026-05-06; no 2026-05-09 content
  - sentinelone-blog       # RSS via rss-bridge — 0 items in 8h window
  - sentinelone-labs       # RSS via rss-bridge — 0 items in 8h window
  - sophos                 # RSS via rss-bridge — alt path news.sophos.com/feed/ validates as healthy (9 items total) but 0 items in 8h window. Original /en-us/feed/ path returned 404 this sweep — alt path is the working endpoint
  - eset-welivesecurity    # RSS via rss-bridge — 0 items in 8h window
  - mandiant               # feedburner.com/Mandiant 404 (eighth consecutive failure). Alt cloud.google.com/blog/topics/threat-intelligence/rss returns malformed body (parse error). WebFetch on the cloud.google.com/blog/topics/threat-intelligence INDEX page successful — 7 most-recent post titles surfaced (UNC6692 Snow Flurries, German Cyber Überfall, BRICKSTORM Defender's Guide, UNC1069 Axios NPM, M-Trends 2026, DarkSword iOS, Ransomware Under Pressure). All triangulate as out-of-8h-window per WebSearch (DarkSword confirmed 2026-03-18 publication via thehackernews.com, helpnetsecurity.com, malwarebytes.com — March 2026 content). UNC6692 + UNC1069 still potential /new-actor candidates per morning observation
  - wired-security         # RSS via rss-bridge — 0 items in 8h window. Same "Hackable Robot Lawn Mower" security roundup from morning (2026-05-09T10:30 UTC = 06:30 EDT) is still the only 2026-05-09 item in the feed but published BEFORE the 07:30 window start; anti-noise from morning pre-brief applies. www.wired.com WebFetch blocked by Claude Code (consistent with morning sweep)
  - cyberwarrior76         # Substack RSS via rss-bridge — 0 items in 8h window
  - hacker-news            # feedburner/TheHackersNews RSS via rss-bridge (best-effort cross-coverage) — 0 items in 8h window
  - splunk-archimedes      # tstats over 8h: zero non-archimedes-internal events. Targeted IOC sweep across CVE-2026-0300, CVE-2026-6973, CVE-2026-42208, OpenC3 COSMOS cluster CVEs (42087/42088/42084), Dirty Frag CVEs (43284/43500), MuddyWater, UNC1549, Charming Kitten, PCPJack, RansomHouse, Trellix returned 3 hits — all archimedes:operation events (librarian git_committed and brief_published self-references from morning brief publication). No external IOC matches
  - splunk-defenseclaw     # tstats over 8h: zero non-archimedes-internal events (eighth consecutive sweep with this pattern; index appears dormant for live security telemetry)
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-gossithedog          # STALE flip 2026-05-09 00:00 — nitter.net account permanently delisted (4 consecutive 404s). Alt-instance investigation pending
sources_skipped_softfail_this_sweep:
  - mandiant               # eighth consecutive feedburner 404 (cloud.google.com alt path malformed body). Held healthy pending operator decision on alt-endpoint discovery / MCP build. Index-page WebFetch workaround viable for title surfacing only
  - x-cisagov              # nitter.net timeout this sweep — failure_count 2→3 (PAST threshold; held healthy pending alt-pool decision given the recovered/timed-out oscillation across sweeps)
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # ECONNREFUSED from prior sweep, awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom (5 consecutive checks); per-repo GHSAs reachable directly when needed
  - iran-monitor           # 403 from prior sweep, deferred until WAF/UA workaround
sources_stale_flipped_this_sweep:
  - ars-security           # feeds.arstechnica.com/arstechnica/security 404 — third consecutive failure (00:22, 07:30, 15:30 all 404). STALE FLIP per the >=2-failure rule. Endpoint likely permanently retired or restructured. Workaround: arstechnica.com/feed/ root feed validates as healthy RSS (200 OK, 20 items) but it's site-wide, not security-only — would need security-tag filter. Operator action: identify replacement feeds.arstechnica.com path OR switch source-grades.yaml ars-security configuration to root feed with security-tag filter
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [pre_brief_clean, sentinel, all_topics_already_covered, afternoon_window]
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      No new CVSS >= 9.0 with confirmed in-the-wild exploitation from
      A-grade source in the 8h window. CISA KEV: zero entries dated
      2026-05-09. Most recent KEV addition is CVE-2026-42208
      (BerriAI LiteLLM SQL injection, 2026-05-08, dueDate 2026-05-11)
      — already covered in morning brief 2026-05-09-morning. CVE-2026-0300
      PAN-OS BOD-22-01 deadline expired today (2026-05-09) — already
      covered, no fresh KEV update reflecting compliance status. Trigger
      1 not matched.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      No fresh attribution to any of the 24 tracked actors in
      _roster.yaml in the 8h window. UNC6692 (Snow Flurries) and
      UNC1069 (Axios NPM supply chain) are NOT in _roster.yaml — both
      are potential /new-actor candidates from this morning's awareness
      surface, but neither is a fresh attribution publication in this
      window (both triangulated as out-of-window per WebSearch).
      MuddyWater 72h auto-downgrade clock for FLASH-0002 expired
      ~2026-05-09T12:00 EDT (3.5h before this sweep); resolution is
      owned by morning workflow rather than this collection sweep.
      Trigger 2 not matched.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk targeted IOC sweep across both archimedes and
      defenseclaw_local indexes for the past 8h returned only
      archimedes-internal pipeline events (3 hits, all
      archimedes:operation matching CVE keywords in librarian
      git_committed and brief_published payloads — pipeline
      self-references, not external observations). No live external
      telemetry observed; eighth consecutive sweep with dormant
      non-archimedes-internal stream pattern. Trigger 3 cannot fire
      on a dormant stream.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      No new tooling/targeting/infrastructure-class documentation
      from A/B-grade sources for any tracked actor in the 8h window.
      CrowdStrike "Defending Against CORDIAL SPIDER and SNARKY SPIDER
      with Falcon Shield" remains dateless product marketing (already
      noted morning); CORDIAL SPIDER + SNARKY SPIDER aliases are NOT
      in _roster.yaml — would be /new-actor workflow path, not
      Trigger 4. DarkSword iOS surfaced on Mandiant index page but
      WebSearch confirms 2026-03-18 publication date — well outside
      window. Trigger 4 not matched.
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      No new active campaign explicitly targeting aerospace, defense,
      or watchlist companies in the 8h window. The two BleepingComputer
      items (JDownloader RAT, fake OpenAI HF repo) are commodity-malware
      / supply-chain compromises with broad-consumer-impact framing
      and no A&D mention. Trigger 5 not matched.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      No new vulnerability disclosed pre-patch with CVSS >= 8.0 or
      widely-deployed-product profile in the 8h window. The OpenC3
      COSMOS cluster (CVE-2026-42087/42088/42084/42085/42086, max CVSS
      9.6) was raw-signaled in the morning AM-001 / promoted to
      finding-2026-05-09-0001 / VT-005 — patches are AVAILABLE
      (7.0.0-rc3 / 7.0.0) so the no-patch criterion fails. The Dirty
      Frag CVE-2026-43284 / CVE-2026-43500 thread (active attacks
      per MSTIC 2026-05-08) is already a T-48h tripwire in the morning
      brief and patches are available. Trigger 6 not matched.
flash_overall_decision: no_trigger_matched_clean_sweep
flash_anti_noise_applied:
  applied: true
  reason: |
    Per FLASH-POLICY anti-noise rule "one FLASH per topic per 24h."
    Both BleepingComputer items in window failed the watchlist /
    roster / vuln-index filter at the Mode 1 stage, so they never
    reached FLASH-trigger evaluation. All other sources clean.
    The afternoon brief composer will draw on the morning's 9
    referenced findings (Ivanti EPMM T-40h carry, OpenC3 COSMOS
    finding-2026-05-09-0001, Dirty Frag T-48h tripwire, MuddyWater
    72h auto-downgrade clock outcome [resolves at morning workflow,
    not collector], LiteLLM/IIS/PAN-OS/LinuxCopyFail/FortiManager
    patch backlog, plus PCPJack worm + RansomHouse-Trellix +
    Polish ABW ICS carry items).
ad_relevance: none_in_window
new_actor_candidates_observed_out_of_window:
  - UNC6692 (Snow Flurries) — Mandiant + Microsoft Teams social-engineering campaign, late April 2026 publication, NOT in _roster.yaml
  - UNC1069 (Axios NPM supply chain) — DPRK-nexus, ~2026-03-31 attack window, NOT in _roster.yaml
  - CORDIAL SPIDER + SNARKY SPIDER — CrowdStrike voice-phishing AiTM SaaS attacks (2026-04-30 publication, dateless in feed), NOT in _roster.yaml
  - Both flagged for orchestrator/operator review at /new-actor-workflow discretion. None are FLASH-eligible (out of window or non-fresh attribution).
notes_for_grader: |
  Afternoon-window observation: zero raw-signal-promotable items after
  watchlist / roster / vuln-index filtering. Two BleepingComputer
  items had real IOCs and clear malicious activity (JDownloader Python
  RAT supply-chain compromise; fake OpenAI HF repo Rust infostealer
  with 244k inflated downloads) but ZERO matches against
  aerospace-defense.yaml watchlist, _roster.yaml actor aliases, or
  _index.yaml tracked CVEs — DISCARDED per Mode 1 procedure.

  All major source feeds (CISA all.xml, BleepingComputer, SecurityWeek,
  The Record, Krebs, MSTIC, Unit42, SANS-ISC, Rapid7, SentinelOne,
  SentinelLabs, Sophos, WeLiveSecurity, Cyberwarrior76, Hacker News,
  Wired, CrowdStrike) returned zero in-window items meeting filter
  criteria. CISA KEV: zero entries dated 2026-05-09. Splunk both indexes
  dormant for non-archimedes-internal events.

  This raw-signal serves as PROVENANCE for the afternoon brief composer
  to assert "no fresh A&D-relevant developments since the morning brief"
  with full audit trail, rather than re-deriving the absence-of-signal
  observation from disparate source-health entries.

  Briefer will draw on the morning's 9 referenced findings and the
  carry-forward state of the four T-tripwires (Ivanti EPMM T-40h,
  Dirty Frag T-48h, MuddyWater 72h auto-downgrade clock outcome,
  PAN-OS BOD deadline expired today). MuddyWater clock resolution
  is owned by the actor-profiler / grader, not the collector.

  Stale flip this sweep: ars-security (feeds.arstechnica.com 404, 3
  consecutive). Mandiant feedburner remains 404 entrenched (8 consecutive),
  index-page WebFetch workaround viable for title surfacing only.
  x-cisagov nitter.net oscillation continues (failure_count 2→3 past
  threshold but held healthy given recovered/timed-out alternation).
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-07T15:30:00-04:00
---

# Afternoon Pre-Brief Sweep — Clean (sentinel)

The 2026-05-09 15:30 EDT pre-brief sweep returned **zero
raw-signal-promotable items** after applying the watchlist / roster /
vuln-index filter against an 8-hour window (07:30 → 15:30 EDT).

This sentinel raw-signal exists to give the grader and afternoon brief
composer a single auditable record of "what was checked and why nothing
qualified" — rather than reconstructing absence-of-signal from
disparate source-health.yaml entries.

## Window summary

- **Window:** 2026-05-09T07:30:00-04:00 → 2026-05-09T15:30:00-04:00 (8h)
- **Sources queried:** 22 (RSS feeds, JSON catalogs, both Splunk indexes, Mandiant index-page WebFetch workaround, Wired security-category headline check, BleepingComputer + SecurityWeek + The Record homepage cross-checks)
- **Sources skipped stale:** 4 (censys, urlscan, hibp, x-gossithedog)
- **Sources skipped soft-fail:** 6 (mandiant, x-cisagov [past-threshold], threatfox, malwarebazaar, github-advisories, iran-monitor)
- **Source health changes this sweep:**
  - ars-security STALE FLIP (3 consecutive 404s on feeds.arstechnica.com/arstechnica/security; root arstechnica.com/feed/ valid as RSS but site-wide)
  - mandiant failure_count 6→7 (eighth consecutive feedburner 404; alt cloud.google.com path malformed)
  - x-cisagov failure_count 2→3 (past threshold but held healthy given oscillation pattern across sweeps)
- **Items fetched in window:** 12 (10 dateless CrowdStrike marketing entries + 2 BleepingComputer 2026-05-09 items + 5 dateless out-of-window Mandiant index titles surfaced via WebFetch)
- **Items matching filter (watchlist / roster / vuln-index):** 0
- **Items raw-signaled:** 0 (this sentinel only)
- **FLASH triggers matched:** 0 (none of 6 conditions evaluated as TRUE)

## Why nothing matched

**BleepingComputer surfaced 2 fresh in-window items, both DISCARDED per Mode 1 procedure:**

1. **JDownloader site hack delivering Python RAT** (2026-05-09T19:27 UTC = 15:27 EDT, by Lawrence Abrams). Generic Windows / Linux download manager compromise — Python-based RAT in the Windows installer, ELF systemd-exec persistence in the Linux installer. C2 infrastructure: parkspringshotel[.]com, auraguest[.]lk, checkinnhotels[.]com (lodging-themed typosquats). Researchers: Thomas Klemenc + Reddit user PrinceOfNightSky. **No A&D customer base, no actor attribution, no tracked CVE.** Filter result: discard.

2. **Fake OpenAI Hugging Face repo "Open-OSS/privacy-filter" pushing "sefirah" Rust infostealer** (2026-05-09T14:26 UTC = 10:26 EDT, by Bill Toulas). Typosquat repo masquerading as OpenAI's "Privacy Filter" project; reached #1 on HF trending list with 244k downloads (likely artificially inflated). C2: recargapopular[.]com. Researcher: HiddenLayer. **No A&D mention, no tracked-actor attribution, no tracked CVE.** Filter result: discard.

Both items are commodity-malware / supply-chain compromises with broad-consumer-impact framing — outside the current Archimedes A&D-prime tracking scope. Per Mode 1 procedure, items not matching watchlist / roster / vuln-index filters are discarded without a per-item raw-signal file.

**All other source feeds returned 0 in-window items**, confirmed by both RSS retrieval and homepage WebFetch on the major media properties (BleepingComputer, SecurityWeek, The Record). The two latter homepages contain only 2026-05-08-dated and earlier articles, all already covered in prior briefs.

**Splunk first-party telemetry remains dormant** for non-archimedes-internal events across both `archimedes` and `defenseclaw_local` indexes (eighth consecutive sweep with this pattern). Targeted IOC sweep across the morning's tracked CVEs and actor aliases returned only 3 archimedes:operation events — librarian `git_committed` and `brief_published` self-references from the morning brief publication, not external observations. Trigger 3 (first-party-ioc-hit) cannot fire on a dormant stream.

## Awareness items (out-of-window, non-FLASH, flagged for orchestrator)

These surfaced via the WebFetch fallback on the cloud.google.com/blog/topics/threat-intelligence index page (Mandiant index-page workaround for the persistently-404'd feedburner endpoint). All triangulate as out-of-8h-window per WebSearch and therefore are NOT raw-signaled per pre-brief scope discipline; they're noted here for orchestrator/operator review at `/new-actor` workflow discretion:

- **UNC6692 (Snow Flurries)** — Mandiant report on social-engineering campaign deploying a custom malware suite. Late April 2026 publication. NOT in `_roster.yaml`. Potential `/new-actor` candidate.
- **UNC1069** — Google Threat Intelligence Group report on DPRK-nexus actor compromising Axios NPM package in supply-chain attack. ~2026-03-31 attack window (M-Trends 2026 frame). NOT in `_roster.yaml`. Potential `/new-actor` candidate.
- **CORDIAL SPIDER + SNARKY SPIDER** — CrowdStrike "Defending Against CORDIAL SPIDER and SNARKY SPIDER with Falcon Shield" (2026-04-30 publication; appeared dateless in CrowdStrike RSS but confirmed via blog-index WebFetch). Voice-phishing AiTM SaaS attacks; CrowdStrike's framing is product-marketing-leaning rather than fresh research. NOT in `_roster.yaml`.
- **DarkSword iOS exploit chain** — Google Threat Intelligence Group report on iOS exploit chain leveraging six zero-days, used by multiple threat actors against targets in Turkey, Malaysia, Saudi Arabia, Ukraine. **2026-03-18 publication confirmed** via thehackernews.com / helpnetsecurity.com / malwarebytes.com via WebSearch — well outside window. Awareness item only.

## Carry-forward state for the afternoon brief composer

The morning brief 2026-05-09-morning referenced 9 findings; their carry-forward state at 15:30 EDT:

- **finding-2026-05-08-0002 (Ivanti EPMM CVE-2026-6973)** — T-40h federal CISA deadline 2026-05-11; lead-finding carry. No new exploitation reports, no second-vendor confirmation in window.
- **finding-2026-05-09-0001 (OpenC3 COSMOS five-CVE cluster, VT-005)** — A2 / WEP likely / single-source-veto-applied. No new ITW exploitation, no third-party technical analysis from Mandiant / Unit 42 / CrowdStrike / SentinelLabs / Bishop Fox / Praetorian, no NASA or BAE Systems public statement on COSMOS deployment posture in window. Watch signals all silent.
- **finding-2026-05-08-0001 (Dirty Frag CVE-2026-43284 / CVE-2026-43500)** — T-48h tripwire from MSTIC active-attack post 2026-05-08T17:12 UTC. No second-vendor confirmation surfaced in window (Unit 42 / CrowdStrike / SentinelLabs / Mandiant / Sophos / WeLiveSecurity feeds all 0 items).
- **finding-2026-05-06-FLASH-0002 (MuddyWater Chaos-ransomware-masquerade)** — 72h auto-downgrade clock expired ~2026-05-09T12:00 EDT (~3.5h before this sweep). Resolution is owned by actor-profiler / grader at morning workflow, not collector. No second A/B-grade source confirmation surfaced in this 8h window.
- **finding-2026-05-08-0003 (PCPJack worm)** — Status-only patch backlog carry. No update in window.
- **finding-2026-05-08-0005 (RansomHouse / Trellix)** — Status-only carry. No update in window.
- **finding-2026-05-08-0009 (Polish ABW water-utility APT28 / APT29 / UNC1151)** — Status-only carry from yesterday afternoon. No update in window. (Note: ABW source provisional B awaiting ratification.)
- **CVE-2026-42208 (BerriAI LiteLLM, KEV 2026-05-08)** — Status-only patch backlog carry. KEV due-date 2026-05-11.
- **CVE-2026-0300 (PAN-OS, KEV 2026-05-06)** — BOD-22-01 deadline 2026-05-09 = today; expired in this window. No KEV update reflecting compliance status (per CISA KEV catalog re-pull, no entries dated 2026-05-09 at all). Patches still scheduled for 2026-05-13 (10.2 / 11.1) and 2026-05-28 (11.2 / 12.1) per VT-004 dossier.
- **CVE-2026-31431 (Linux Kernel Copy Fail, KEV 2026-05-01)** — Status-only patch backlog carry. KEV due-date 2026-05-15.
- **CVE-2026-30445 (IIS HTTP.sys), CVE-2026-29841 (FortiManager)** — Status-only patch backlog carry from morning brief.

## Extraction notes

- Language: en
- Article type: sentinel / collection-provenance
- Raw IOC extraction invoked: no (no in-window items qualified for IOC extraction; the two BleepingComputer items had IOCs but were filtered out before extraction stage)
- Source-grade range queried: A (cisa-kev, cisa-advisories, mstic, unit42, mandiant-via-index-fetch, sophos, eset) + B (bleepingcomputer, securityweek, the-record, krebs, sans-isc, rapid7, abw [provisional], wired-security) + C/provisional (sentinelone-blog, sentinelone-labs, cyberwarrior76, layerx, securityweek-provisional, rapid7-provisional, sentinelone-provisional, abw-provisional)

## IOCs (from ioc-extraction skill)

```yaml
iocs: []
attribution_claims: []
extraction_notes:
  invoked: false
  reason: "No in-window items matched the watchlist / roster / vuln-index filter at Mode 1 stage. The two BleepingComputer items (JDownloader RAT C2: parkspringshotel[.]com, auraguest[.]lk, checkinnhotels[.]com; fake OpenAI HF repo C2: recargapopular[.]com) were observed but discarded per Mode 1 before reaching IOC extraction."
  observed_iocs_not_extracted:
    - parkspringshotel[.]com  (JDownloader RAT C2 — discarded)
    - auraguest[.]lk          (JDownloader RAT C2 — discarded)
    - checkinnhotels[.]com    (JDownloader RAT C2 — discarded)
    - recargapopular[.]com    (fake OpenAI HF repo / sefirah Rust infostealer C2 — discarded)
```
