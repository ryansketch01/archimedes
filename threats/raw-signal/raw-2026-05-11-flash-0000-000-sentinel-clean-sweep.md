---
raw_id: raw-2026-05-11-flash-0000-000
collected_at: 2026-05-11T00:03:00-04:00
run_id: flash-sweep-20260511-000000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-11T00:00:00-04:00
time_window_start: 2026-05-10T18:00:00-04:00
time_window_end: 2026-05-11T00:00:00-04:00
test: false
sources_queried:
  - cisa-kev               # JSON feed via WebFetch — full-catalog scan for dateAdded >= 2026-05-10 returned zero entries. Confirmed: most recent KEV add remains CVE-2026-42208 (BerriAI LiteLLM, dateAdded 2026-05-08, dueDate 2026-05-11 ~T-8h to T-12h). KEV ranking unchanged from 2026-05-10 18:00 sweep. CVE-2026-6973 Ivanti EPMM BOD-22-01 deadline 2026-05-10 EOB has now passed without a KEV update.
  - cisa-advisories        # all.xml RSS via fetch_feed — status 200, 30 items in feed total, 0 items in 6h window after since-filter.
  - bleepingcomputer       # RSS via fetch_feed — status 200, last_modified 2026-05-11T03:59:38 GMT = 23:59 EDT (within window from feed-server activity), 0 items in 6h window after since-filter.
  - securityweek           # RSS via fetch_feed — status 200, last_modified 2026-05-11T03:53:04 GMT = 23:53 EDT (within window from feed-server activity), 1 item in 6h window after since-filter — "Over 500 Organizations Hit in Years-Long Phishing Campaign" by Ionut Arghire (2026-05-11T03:49:18Z = 2026-05-10T23:49 EDT, in-window by 10 minutes). WebFetch on the article: originating research = SOCRadar (vendor; NO prior source-grade in source-grades.yaml). Campaign name = "Operation HookedWing" (researcher-coined; no actor attribution claimed). Duration = 4+ years (started 2022, continuing 2025). Status = active/ongoing. Victims = 500+ orgs across aviation, critical infrastructure, energy, financial, government/public-admin, logistics, technology — but NO named A&D primes, NO specific aviation primes identified. TTPs = phishing impersonating HR/colleagues/notifications, Microsoft Outlook themed lures, full-screen pre-loaders with org-name personalization, GitHub-hosted infrastructure + compromised intermediary hosts, geo + email validation in background script. Infra = ~24 C&C servers + 100+ GitHub domains + dozen+ distribution domains (specifics NOT in SecurityWeek piece — would require WebFetch on SOCRadar primary). NO CVEs. NO threat-actor attribution. FLASH trigger evaluation: Trigger 1 fails (no CVE); Trigger 2 fails (no actor); Trigger 3 fails (no IOCs available in our corpus to Splunk-query); Trigger 4 fails (no tracked actor); Trigger 5 MARGINAL — aviation listed but no named A&D primes, SOCRadar is provisional-unknown-grade (would be conservative C on first-surface per LayerX/Seqrite/Trendyol precedent — below FLASH B2-minimum bar), campaign 4-year retrospective with extension (not a "first-time disclosure of new active campaign" event); Trigger 6 fails (no vuln). RAW-SIGNALED as FLASH-0000-001 below for grader's morning-brief inventory (in-window, watchlist-adjacent on aviation token, brand-new SecurityWeek disclosure of a previously-undocumented campaign that may warrant SOCRadar source-grade-log expansion).
  - the-record             # RSS via fetch_feed — status 200, 0 items in 6h window (5 items total in feed, most recent 2026-05-08).
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-11T03:53:04 GMT pre-window, 0 items in 6h window — normal Krebs cadence.
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, last_modified 2026-05-08T23:03:04 GMT pre-window (unchanged across SIX consecutive sweeps), 0 items in 6h window. Most recent MSTIC content remains 2026-05-08T17:12 UTC Dirty Frag active-attack post (~79h aged at this sweep).
  - unit42                 # RSS (feedburner) via fetch_feed — status 200, last_modified 2026-05-08T21:09:40 GMT pre-window (unchanged across FIVE consecutive sweeps), 0 items in 6h window.
  - sans-isc               # RSS via fetch_feed — status 200, last_modified 2026-05-11T03:59:22 GMT = 23:59 EDT (within window from feed-server activity), 2 items in 6h window after since-filter — (1) "ISC Stormcast For Monday, May 11th, 2026" (podcast detail, 2026-05-11T02:15:11Z), no body content, awareness-only; (2) "YARA-X 1.16.0 Release" (2026-05-10T22:37:08Z = 18:37 EDT just inside window), tool release announcement, no threat-intel claim. NO FLASH-relevant content; both DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit).
  - rapid7                 # RSS via fetch_feed — status 200, last_modified 2026-05-11T03:19:20 GMT = 23:19 EDT (within window from feed-server activity), 0 items in 6h window after since-filter.
  - crowdstrike            # RSS via fetch_feed — status 200, last_modified 2026-05-10T04:18:42 GMT pre-window, 10 items returned ALL with null published_at (fourteenth consecutive sweep with this dateless marketing pattern). Same pile (Gartner MQ leader, Falcon OverWatch for Defender, Risk Assessments, AI Vuln Discovery podcast, CORDIAL/SNARKY SPIDER product-marketing, ChatGPT Enterprise integration, Frost & Sullivan, ROI marketing). No 2026-05-10/11 threat-research content visible.
  - sentinelone-labs       # RSS via fetch_feed — status 200, last_modified 2026-05-08T23:44:58 GMT pre-window (unchanged), 0 items in 6h window.
  - sophos                 # RSS via fetch_feed (news.sophos.com/feed/) — status 200, 9 items total in feed, 0 items in 6h window. RECOVERED — prior 2026-05-10 PM sweep recorded 404 on news.sophos.com/en-us/feed/ subpath; root path was the productive endpoint (matches pre-2026-05-10 PM source-health pattern). failure_count 1→0 healthy this sweep.
  - eset-welivesecurity    # RSS via fetch_feed — status 200, 100 items total in feed, 0 items in 6h window.
  - hacker-news            # feedburner/TheHackersNews RSS via fetch_feed — status 200, last_modified 2026-05-11T03:10:41 GMT pre-window, 0 items in 6h window.
  - darkreading            # RSS via fetch_feed — status 200, 50 items total in feed, 0 items in 6h window.
  - ars-technica           # Workaround used: arstechnica.com/feed/ root feed (site-wide; ars-security path retired since 2026-05-09). Reachable, status 200, 0 items in 6h window.
  - proofpoint             # RECOVERED — alt endpoint proofpoint.com/us/rss.xml reachable (status 200, last_modified 2026-05-10T22:38:09 GMT just-inside window from feed-server activity, 10 items total in feed). 0 items in 6h window after since-filter. Note: this is the corporate-news feed, not the /us/threat-insight/blog/feed (which 404'd starting 2026-05-10 12:00 sweep — that endpoint remains broken / retired). Operator: this feed cadence is multi-day; not a real-time threat-research surface, but at least reachable as a coarse Proofpoint surface signal.
  - mandiant               # WebFetch on cloud.google.com/blog/topics/threat-intelligence INDEX page — top 8 titles unchanged from 2026-05-10 18:00 sweep (UNC6692 Snow Flurries, German Cyber Überfall, BRICKSTORM Defender's Guide, UNC1069 Axios NPM, M-Trends 2026, DarkSword iOS, Ransomware Under Pressure, Proactive Preparation 2026). All previously triangulated as out-of-window. feedburner.com/Mandiant returned 404 (FOURTEENTH consecutive failure). Operator alt-endpoint decision still pending.
  - dragos                 # WebFetch on /blog/ index — top 5 most recent posts unchanged from 2026-05-10 sweeps: "OT Cybersecurity Lessons Learned from the Frontlines" (2026-05-07), "AI in the Breach: How an Adversary Leveraged AI to Target a Water Utility's OT" (2026-05-06), "Why Is Manufacturing the Most Targeted Sector for OT Cyber Attacks?" (2026-04-28), "ZionSiphon: Why This Malware Isn't A Credible ICS Threat" (2026-04-23), "Detection to Due Diligence: Strengthening NERC CIP Compliance" (2026-04-22). NO posts dated 2026-05-08 / 09 / 10 / 11. Most recent (2026-05-07) is ~4 days aged, out of 6h window. Note: dragos.com/blog/feed/ and /feed/ both 404 per 2026-05-09 PM observation; index-page WebFetch remains the working workaround.
  - talos-intel            # WebFetch on /rss/ — top 4 articles unchanged from 2026-05-10 sweeps ("Unplug your way to better code" 2026-05-07; "Insights into the clustering and reuse of phone numbers in scam emails" 2026-05-06; "UAT-8302 and its box full of malware" 2026-05-05; "CloudZ RAT potentially steals OTP messages using Pheno plugin" 2026-05-05). NO posts dated 2026-05-09 / 10 / 11. Out-of-window regardless.
  - nvd                    # WebFetch on services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=2026-05-10T22:00:00Z&lastModEndDate=2026-05-11T04:00:00Z for the 6h window. cvssV3Severity=CRITICAL → 0 results. cvssV3Severity=HIGH → 1 result — CVE-2026-8260 (D-Link DCS-935L network camera HNAP service buffer overflow in SetDeviceSettings AdminPassword parameter, CVSS 8.8, published 2026-05-11T02:16Z; PoC publicly available; authenticated-attacker requirement). CONSUMER IP-CAMERA product, not A&D / aerospace / defense / tracked-vuln / tracked-actor. No active in-the-wild exploitation cited (PoC-only is not Trigger 1 active-exploitation). DISCARDED per Mode 1 procedure.
  - splunk-archimedes      # tstats over 6h NOT sourcetype=archimedes:* — zero events. Targeted IOC keyword sweep (18 high-priority actor + CVE tokens spanning the tracked roster + tracked vulnerabilities) over 24h returned 5 hits — ALL archimedes:operation pipeline self-references (APT37 threat_box_scoring_completed event 2026-05-10T17:48 EDT; afternoon brief publish 16:20; morning brief publish 08:13; MuddyWater finding_superseded A2→C3 event 08:13; git_committed events for 2026-05-10 morning brief). Pipeline self-references match CVE/actor names in payloads but reflect Archimedes' own operational logging. TWELFTH consecutive sweep with dormant non-archimedes-internal stream pattern.
  - splunk-defenseclaw     # tstats over 24h NOT sourcetype=archimedes:* — zero events. TWELFTH consecutive sweep with dormant non-archimedes-internal stream pattern.
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH — three consecutive WinError 10060 nitter.net timeouts. Within 24h since stale-flip → still skipped this sweep; eligible-to-retry rule fires after 2026-05-11T12:00 (next noon FLASH).
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted (4 consecutive 404s prior). >24h since stale flip but FLASH-fast scope kept to RSS/vendor/KEV priority feeds; not retried this sweep (operator alt-pool / direct-X-API decision pending; treating as effectively stale until path resolution).
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround in use (arstechnica.com/feed/ root path); the security-specific stale entry remains stale pending operator path-replacement decision.
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom (per-repo GHSA fallback path remains productive workaround when triggered; not triggered this sweep)
  - iran-monitor           # 403 from prior sweep, deferred until WAF/UA workaround
  - cisa-news-events       # Direct page fetch on cisa.gov/news-events/cybersecurity-advisories returned 403 (consistent with prior sweeps — WAF block on direct page; all.xml RSS remains productive endpoint and returned 0 in-window this sweep)
  - ncsc-uk                # ncsc.gov.uk/section/keep-up-to-date/news returned 404 (path may have changed; recommend operator path discovery on next pre-brief if a UK-government-source check is desired)
sources_health_recovered_this_sweep:
  - sophos                 # news.sophos.com/feed/ root path returned status 200 and valid RSS this sweep, confirming the 2026-05-10 PM en-us/feed/ subpath 404 was a path-mismatch issue; failure_count 1→0
  - proofpoint             # proofpoint.com/us/rss.xml corporate-news endpoint reachable, status 200 valid RSS; the /us/threat-insight/blog/feed threat-intel endpoint remains broken (404 persistent since 2026-05-10 12:00). Recovered for coarse Proofpoint surface awareness only; not a real-time threat-research surface
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (FOURTEENTH consecutive); failure_count 12→13. WebFetch on cloud.google.com/blog/topics/threat-intelligence index-page surfaced top-8 titles unchanged from 2026-05-10 18:00 sweep — all out-of-window per prior triangulations. Held healthy pending operator alt-endpoint decision.
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_sweep_clean, sentinel, quiet_hours_active, hookedwing_socradar_in_window_non_flash, sophos_recovered, proofpoint_corporate_feed_recovered, x_cisagov_still_stale, x_gossithedog_still_stale, cve_2026_8260_dlink_consumer_ip_camera_discarded]
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      No new CVSS >= 9.0 with confirmed in-the-wild exploitation from
      A-grade source in the 18:00 EDT (Sun) → 00:00 EDT (Mon) window.
      CISA KEV catalog full-catalog scan: zero entries with dateAdded
      >= 2026-05-10 or 2026-05-11. Most recent KEV addition remains
      CVE-2026-42208 (BerriAI LiteLLM SQL injection, dueDate 2026-05-11
      ~T-8h to T-12h from this sweep) — already in corpus, being
      status-carried in the 2026-05-10 afternoon brief patch-backlog
      tier.

      NVD lastModStartDate window query 22:00-04:00 UTC: CRITICAL =
      zero results. HIGH = 1 result (CVE-2026-8260 D-Link DCS-935L
      consumer IP camera HNAP buffer overflow, CVSS 8.8). D-Link
      DCS-935L is a consumer-class IP camera, NOT A&D /
      tracked-product / tracked-actor-attributed. PoC publicly
      available per NVD entry but "PoC available" alone is NOT
      Trigger 1 "active in-the-wild exploitation" — the trigger
      requires confirmed exploitation from an A-grade source, and
      no A-source carries this. Also CVSS 8.8 falls BELOW the
      Trigger 1 9.0 floor (would be a Trigger 6 candidate if a
      patch were unavailable AND exploitation were confirmed, but
      neither condition is documented).

      Trigger 1 not matched.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      No fresh attribution to any of the 24 tracked actors in
      _roster.yaml in the 6h window. SecurityWeek "Operation
      HookedWing" article (SOCRadar primary, 2026-05-10T23:49 EDT)
      explicitly does NOT attribute the campaign to a named
      threat-actor group ("targeting pattern that is not random"
      and "high geopolitical relevance" hedges but no nation /
      service / alias claim). Mandiant index-page workaround
      surfaced same top-8 titles as prior sweeps — all
      out-of-window. MSTIC, Unit 42, CrowdStrike (dateless
      marketing), SentinelLabs, Sophos, ESET, Rapid7, Talos,
      Dragos feeds all 0 items in window OR fully out-of-window
      content. The /new-actor candidates flagged in prior sweeps
      (UNC6692 Snow Flurries, UNC1069 Axios NPM, DarkSword, UAT-8302,
      CORDIAL SPIDER, SNARKY SPIDER) remain NOT in _roster.yaml
      with no fresh in-window publication on any. Trigger 2 not
      matched.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party check across both archimedes and
      defenseclaw_local indexes over 6h window via tstats: zero
      events. Targeted IOC keyword sweep across 18 high-priority
      tokens (tracked actors + tracked CVEs) over 24h returned
      5 hits — ALL archimedes:operation pipeline self-references
      from 2026-05-10 (APT37 threat_box_scoring_completed at 17:48
      EDT, afternoon brief publish at 16:20 EDT, morning brief
      publish at 08:13 EDT, MuddyWater finding_superseded
      A2->C3 event at 08:13 EDT, git_committed event at 08:14
      EDT). Pipeline self-references match the CVE/actor name
      strings in their JSON payloads (e.g., MuddyWater event
      references "MuddyWater" by name; afternoon brief publish
      event references CVE-2026-6973, CVE-2026-42208, etc., in
      its related_vulns array) but these are Archimedes' own
      operational logging, NOT external observations of those
      indicators in network/host telemetry.

      Twelfth consecutive sweep with dormant non-archimedes-internal
      stream pattern across both indexes. Trigger 3 cannot fire on
      a dormant external-telemetry stream.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      No new tooling/targeting/infrastructure-class documentation
      from A/B-grade sources for any tracked actor in the 6h window.
      All vendor-research feeds (Mandiant via index-page, MSTIC,
      Unit42, CrowdStrike, SentinelLabs, Sophos, WeLiveSecurity,
      Dragos via index-page, Rapid7, Talos) returned 0 items in
      window OR dateless marketing material OR fully out-of-window
      content. No tracked-actor TTP delta surfaced. Trigger 4 not
      matched.
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      One MARGINAL candidate considered and DISCARDED.

      SecurityWeek (2026-05-10T23:49 EDT, in-window by ~10 minutes):
      "Over 500 Organizations Hit in Years-Long Phishing Campaign"
      by Ionut Arghire, relaying SOCRadar's "Operation HookedWing"
      research. The article reports:
      - Aviation listed as one of 7 victim sectors (alongside
        critical infrastructure, energy, financial, government /
        public administration, logistics, technology)
      - NO named A&D primes (Lockheed Martin, Boeing, RTX,
        Northrop Grumman, General Dynamics, BAE Systems, L3Harris,
        Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell
        Aerospace, Airbus, Elbit) — only sector tokens
      - Campaign duration: 4+ years (started 2022, continuing
        through 2025) — described as "ongoing" with sustained
        activity through 2025 and expanding infrastructure / lures
      - 500+ victim organizations total across all sectors
      - Multi-victim YES; active YES; NO threat-actor attribution
        ("not random" + "high geopolitical relevance" hedges only)
      - Originating researcher: SOCRadar (vendor; NO prior
        Archimedes source-grade — would be provisional-unknown
        on first surface; per LayerX / Seqrite / Trendyol
        precedent the conservative starting grade would be C)
      - Infrastructure cited at sector level (24 C&C servers,
        100+ GitHub domains, dozen+ distribution domains) but
        specific IOCs (domains / IPs / hashes) NOT in the
        SecurityWeek piece — would require WebFetch on the
        primary SOCRadar publication to extract

      FLASH Trigger 5 evaluation:
      - "multi-victim" condition: PASSED (500+ orgs)
      - "active" condition: PASSED (ongoing through 2025 per
        SOCRadar)
      - "explicitly targeting aerospace, defense, or watchlist
        companies" condition: MARGINAL — aviation listed but
        no named A&D primes; "aviation" includes commercial
        travel and is broader than the watchlist-prime profile
      - Anti-noise rule "B2 minimum grade applies to FLASH":
        FAILS — SecurityWeek is provisional B-grade (would
        relay at B/C depending on ratification trajectory), but
        SOCRadar primary has no Archimedes source-grade and
        would be provisional C on first-surface per the
        conservative starting-grade precedent. Composite source
        signal is C-grade-bounded, NOT B2-minimum.

      Disposition: NOT FLASH-worthy. RAW-SIGNALED as the
      separate file raw-2026-05-11-flash-0000-001-securityweek-
      hookedwing-socradar-aviation-non-flash.md for the grader's
      morning-brief queue. The grader can decide whether
      HookedWing warrants a morning-brief inventory mention,
      whether SOCRadar should be added to source-grade-log.md
      as a new provisional source (LayerX / Seqrite / Trendyol
      precedent at C), and whether the operator should retrieve
      the underlying SOCRadar primary for IOC extraction (the
      ~24 C&C servers + 100+ GitHub domains may include
      indicators worth ingesting to _master-index.yaml for
      future first-party IOC-hunt sweeps even if no A&D-prime
      attribution materializes — the "aviation" sector token is
      adjacent enough to the A&D watchlist to warrant grader-
      level attention without firing FLASH).

      Trigger 5 not matched.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      No new vulnerability disclosed pre-patch with CVSS >= 8.0
      or widely-deployed-product profile in the 6h window.

      One CVSS-eligible candidate considered and DISCARDED:

      - CVE-2026-8260 (D-Link DCS-935L IP camera HNAP service
        buffer overflow, CVSS 8.8, published 2026-05-11T02:16Z =
        2026-05-10T22:16 EDT inside window). Per NVD entry:
        authenticated-attacker requirement (cannot exploit pre-
        authentication), CWE-119/120 buffer-overflow class. PoC
        publicly available. NO patch_status field; NVD does not
        cite patch availability. Affected product is a consumer-
        class network camera (D-Link DCS-935L mydlink Cloud HD
        camera, retail product line) — NOT widely-deployed in
        Archimedes A&D-prime profile (no SCADA / industrial-
        camera / defense-systems heritage). Trigger 6 conditions:
        "CVSS >= 8.0" PASSED; "widely-deployed product OR active
        exploitation" — consumer IP cameras are widely deployed
        in the consumer / SMB market but NOT in the A&D-prime
        target profile; authenticated-attacker requirement plus
        product profile makes this a low-priority advisory for
        Archimedes. Even if reclassified as "widely deployed,"
        "exploitation confirmed or imminent per A-grade source"
        fails — only NVD/PoC citation, no A-grade vendor
        reporting active exploitation. DISCARDED.

      Trigger 6 not matched.
post_evaluation_summary:
  flash_candidates_count: 0
  flash_disposition: nothing_fired
  non_flash_raw_signals_written:
    - raw-2026-05-11-flash-0000-001-securityweek-hookedwing-socradar-aviation
  next_action: |
    Per FLASH-POLICY.md anti-noise + quiet-hours rules:
    1. Zero FLASH candidates → orchestrator logs "flash_sweep_clean"
       and exits silently. NO discord post. NO queue file write.
    2. HookedWing raw-signal carries forward to the morning brief
       grader queue (in-window, watchlist-adjacent on aviation
       sector token, brand-new SecurityWeek piece on a previously-
       undocumented campaign with potential SOCRadar source-grade-
       log expansion implication and potential IOC-extraction
       opportunity for first-party hunt purposes).
    3. Source-health.yaml updates for sophos (recovered),
       proofpoint (alt-endpoint recovered for coarse signal),
       mandiant (failure_count 12→13 thirteenth consecutive),
       sans-isc (recovered from 2026-05-10 18:00 PM dual-endpoint
       failure — rssfeed.xml status 200 this sweep). Operator
       open items unchanged: x-cisagov nitter pool blocker;
       x-gossithedog nitter account delist; Mandiant
       feedburner alt-endpoint decision; ars-security RSS path
       replacement; CISA news-events direct-page WAF; NCSC UK
       advisories path discovery.
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-09T00:03:00-04:00
---

# FLASH Sweep Sentinel — Clean Sweep (2026-05-11 00:00 EDT, Quiet Hours Active)

**Zero FLASH candidates surfaced this sweep.** One in-window
SecurityWeek item (SOCRadar "Operation HookedWing" aviation-among-7-
sectors phishing campaign disclosure) evaluated against Trigger 5
and DISCARDED as MARGINAL — multi-victim active campaign yes, but no
named A&D primes, originating researcher (SOCRadar) has no
Archimedes source-grade (provisional-C on first surface per
established precedent), and source-composite grade is below the
FLASH anti-noise B2-minimum bar. Raw-signaled separately for
grader's morning-brief queue.

## Window summary

- **Time window:** 2026-05-10T18:00 → 2026-05-11T00:00 EDT (6h)
- **Quiet hours status:** ACTIVE (current local time 00:00 EDT, 
  inside 21:00-09:00 EDT quiet window) — even if a FLASH had fired, 
  it would have queued to flash-queue.yaml rather than posted to
  Discord directly. Per FLASH-POLICY.md, the "actually wake up"
  override (CVSS 10.0 + active exploitation + tracked actor +
  A&D watchlist entity) is the only path to immediate-post during
  quiet hours; none of these four conditions co-occurred this sweep.
- **Sources queried (healthy):** 23 (RSS feeds + KEV JSON + NVD
  REST + Mandiant/Dragos index-page workarounds + Splunk x2)
- **Sources skipped stale (24h-rule):** 3 (x-cisagov nitter pool,
  ars-security feeds path, x-gossithedog nitter delist) plus
  4 MCP-missing / API-key-missing / WAF-blocked
  (censys, urlscan, hibp, iran-monitor)
- **Sources soft-failing this sweep:** 0 fresh (3 carryover —
  threatfox, malwarebazaar, github-advisories continue
  carry-forward pending MCP build / endpoint workaround)
- **Sources recovered this sweep:** sophos (root-path feed),
  proofpoint (alt-endpoint recovered for coarse signal),
  sans-isc (recovered from 2026-05-10 18:00 PM dual-endpoint
  failure)

## Trigger evaluation — all six triggers FAILED

| # | Trigger | Result | Driver |
|---|---|---|---|
| 1 | Critical CVE exploited | FAIL | No new KEV entries 2026-05-09+; CVE-2026-8260 D-Link consumer IP camera CVSS 8.8 below 9.0 floor + PoC-only not active exploitation |
| 2 | Tracked-actor attribution | FAIL | Zero fresh attributions to any of 24 roster actors; HookedWing explicitly NOT attributed |
| 3 | First-party IOC hit | FAIL | Splunk dormant on non-archimedes-internal stream (twelfth consecutive) |
| 4 | Tracked-actor TTP change | FAIL | No A/B-grade vendor research published in window |
| 5 | A&D-sector campaign | MARGINAL → FAIL | HookedWing aviation-listed but no named primes; SOCRadar provisional-C grade below FLASH B2-minimum |
| 6 | Zero-day no patch | FAIL | D-Link DCS-935L consumer camera, authenticated, no active-exploitation A-source claim |

## SecurityWeek "Operation HookedWing" disposition

The one in-window in-scope item required closer analysis. Recording
the full reasoning trail so the grader can pick up cleanly:

- **Originating research:** SOCRadar (Turkish-origin XTI vendor;
  legitimate cyber-threat intelligence company; NO prior
  Archimedes-corpus citation; would be a NEW provisional source-
  grade decision for the librarian's source-grade-log)
- **Relay:** SecurityWeek (provisional B per source-grades.yaml;
  awaiting ratification)
- **Campaign:** "Operation HookedWing" — researcher-coined working
  name, NO threat-actor attribution claimed
- **Duration:** 2022 → present (4+ years)
- **Victims:** 500+ organizations across 7 sectors (aviation,
  critical infrastructure, energy, financial, government/public
  administration, logistics, technology) — NO named primes /
  watchlist entities
- **TTPs:** Phishing impersonating HR / colleagues / notifications;
  Microsoft Outlook themed lures (2022-2024); French content +
  additional themes (2024-2025); full-screen pre-loader with
  organization-name personalization; geolocation + email validation
  in background script
- **Infrastructure:** ~24 C&C servers, 100+ GitHub domains,
  dozen+ distribution domains on other platforms (specific
  indicators NOT in SecurityWeek piece; would require WebFetch on
  the SOCRadar primary to extract)
- **CVEs:** none mentioned
- **Source-grade implications:** SOCRadar appears to be a
  legitimate XTI vendor and warrants source-grade-log review for
  provisional addition (LayerX / Seqrite / Trendyol precedent: C
  on first surface, opportunity to upgrade as track record
  observed)
- **A&D relevance:** STRUCTURAL but not direct — aviation is
  listed in the sector mix but no aerospace-defense prime
  (Lockheed, Boeing, RTX, Northrop Grumman, GD, BAE, L3Harris,
  Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus,
  Elbit) is named as a victim; the aviation sector token covers
  commercial travel + airlines + airport authorities + flight
  operators broadly, not exclusively defense aviation
- **FLASH eligibility:** FAILS Trigger 5 on conjunction of
  "named A&D primes" gap + SOCRadar grade below B2-minimum
  (per FLASH-POLICY anti-noise rule 2). Raw-signaled separately
  as a non-FLASH grader-queue item for morning-brief inheritance

## Source-health observations (this sweep)

**Recovered:**
- `sophos` — news.sophos.com/feed/ root path returned 200 + valid
  RSS (9 items, 0 in window). The 2026-05-10 PM en-us/feed/ subpath
  404 was a path-mismatch, not a source-side outage. failure_count
  1 → 0.
- `proofpoint` — proofpoint.com/us/rss.xml corporate-news endpoint
  reachable (200, valid RSS, 10 items, 0 in window). The
  /us/threat-insight/blog/feed threat-intel endpoint remains
  broken (404 persistent since 2026-05-10 12:00). Recovered for
  coarse Proofpoint surface awareness only; not a real-time
  threat-research surface. Operator-side alt-RSS-path discovery
  for the threat-intel surface remains an open item.
- `sans-isc` — rssfeed.xml returned 200 valid RSS with 10 items
  total (2 in window). The 2026-05-10 18:00 sweep recorded a
  transient dual-endpoint failure (rssfeed.xml parse error AND
  diary.xml 404); recovered this sweep, treated as transient
  not persistent.

**Continuing carry-forward (no change this sweep):**
- `mandiant` — feedburner.com/Mandiant 404 fourteenth consecutive;
  alt cloud.google.com endpoints malformed/non-parseable.
  index-page WebFetch remains the workaround for title-surfacing.
  failure_count 12 → 13.
- `crowdstrike` — fourteenth consecutive sweep with dateless-
  marketing pattern (10 items, all null published_at, all
  product-marketing / Gartner-MQ / Frost-Sullivan content); no
  threat-research material visible.
- `x-cisagov` — STALE since 2026-05-10 12:00 FLASH (three
  consecutive nitter.net WinError 10060 timeouts). Within 24h
  since stale-flip → still skipped this sweep; eligible-to-retry
  after 2026-05-11T12:00.
- `x-gossithedog` — STALE since 2026-05-09 (nitter.net account
  permanently delisted, 4 consecutive 404s). >24h since stale
  flip but FLASH-fast scope kept to RSS/vendor/KEV priority feeds;
  treating as effectively stale until operator nitter-pool /
  direct-X-API decision.
- `ars-security` — STALE since 2026-05-09 (feeds.arstechnica.com/
  arstechnica/security 404). Workaround in use (arstechnica.com/
  feed/ root path); the security-specific stale entry remains
  stale pending operator path-replacement decision.
- `threatfox`, `malwarebazaar`, `github-advisories`,
  `iran-monitor` — same blockers as prior sweeps (CAPTCHA / MCP
  pending / 406 / 403); per-repo GHSA fallback path for
  github-advisories remains the productive workaround when
  triggered (not triggered this sweep).

**New observations:**
- `cisa-news-events` direct-page 403 (consistent with prior
  pattern — WAF block; all.xml RSS remains productive)
- `ncsc-uk` /section/keep-up-to-date/news 404 (path may have
  changed; recommend operator path discovery on next pre-brief
  if a UK-government-source surface is desired in the standard
  rotation)

## Anti-noise check

Per FLASH-POLICY rule 1 (one FLASH per trigger topic per 24h):
- Zero FLASH candidates this sweep → no anti-noise dedup needed.
- HookedWing is brand-new to the corpus (no prior raw-signal /
  finding / brief touches "HookedWing" or "SOCRadar" per
  grep on the threats/ tree) — no dedup against prior coverage.

## Quiet hours posture

Current local time 00:00 EDT falls inside the 21:00-09:00 EDT
quiet window. Per FLASH-POLICY.md, posting to Discord during
quiet hours is restricted to the "actually wake up" override
(CVSS 10.0 + active exploitation + tracked actor + A&D
watchlist entity named as target). None of these four
conditions co-occurred this sweep; the override would not have
been invoked even if a FLASH had cleared the trigger bar.

Per the policy: "FLASH evaluations still run at 00:00 and 06:00
sweeps. If a FLASH is generated, queue to flash-queue.yaml."
Zero FLASH generated this sweep → no queue write. Orchestrator
should log "flash_sweep_clean" to Splunk and exit silently.

## Next sweep

Next FLASH sweep: 2026-05-11 06:00 EDT (in ~6 hours). Quiet
hours remain active until 09:00 EDT. The 06:00 sweep will
re-check KEV (CVE-2026-42208 LiteLLM dueDate hits 2026-05-11,
so any KEV-update reflecting that deadline may surface),
Mandiant index-page top-of-list rotation, MSTIC parent feed
(80h+ aged since most recent post), and Splunk first-party
stream (still dormant on external observations 12 sweeps
running).
