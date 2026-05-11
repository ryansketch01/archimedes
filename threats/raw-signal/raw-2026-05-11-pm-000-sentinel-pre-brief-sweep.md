---
raw_id: raw-2026-05-11-pm-000
collected_at: 2026-05-11T15:32:00-04:00
run_id: pre-brief-20260511-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-11T15:30:00-04:00
time_window_start: 2026-05-11T07:30:00-04:00
time_window_end: 2026-05-11T15:30:00-04:00
test: false
sources_queried:
  - bleepingcomputer       # RSS via fetch_feed — status 200, etag c5659537aa88e3ccd11a3a8818f5092c, last_modified 2026-05-11T19:26:30 GMT (15:26 EDT in-window from feed-server activity), 4 items in 8h window after since-filter (Instructure Canvas XSS confirmation — already covered at 12:00 sentinel, anti-noise applies; Specops sponsored content — filtered; Google AI-generated zero-day exploit by Bill Toulas at 09:02 EDT in-window — RAW-SIGNALED as PM-001; webinar promo — filtered).
  - securityweek           # RSS via fetch_feed — status 200, etag W/"cd6c5cf6bb96a08c6b0c3b98092c908f", last_modified 2026-05-11T17:18:52 GMT (13:18 EDT in-window from feed-server activity), 3 items in 8h window after since-filter (Frame Security funding announcement — filtered; Build Application Firewalls editorial — already covered at 12:00 sentinel, anti-noise applies; Google AI-Generated Zero-Day Exploit by Eduard Kovacs at 09:04 EDT in-window — material identical to BleepingComputer item, captured under PM-001 with multi-source corroboration noted).
  - the-record             # RSS via fetch_feed — status 200, 5 items in feed total, 3 items in 8h window after since-filter (FCC drone/router update-ban deadline extension by Suzanne Smalley at 12:50 EDT in-window — RAW-SIGNALED as PM-004; UK water company / Cl0p / South Staffordshire Water ICO £963.9K fine by Alexander Martin at 08:51 EDT in-window — RAW-SIGNALED as PM-002; Dirty Frag Linux kernel second major bug by The Record at 08:26 EDT in-window — Dirty Frag thread already extensively covered in corpus across 2026-05-08/09/10, anti-noise applies, NOT raw-signaled).
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-08T15:10:32 GMT pre-window, 0 items in 8h window — normal Krebs cadence (multi-day).
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, etag "c3d7f06ea75f67de5907aa1028d2148f-gzip", last_modified 2026-05-11T17:38:35 GMT (13:38 EDT in-window from feed-server activity), 0 items in 8h window after since-filter. Most recent MSTIC content remains 2026-05-08T17:12 UTC Dirty Frag active-attack post (~94h aged at this sweep).
  - unit42                 # RSS (feedburner) via fetch_feed — status 200, last_modified 2026-05-08T21:09:40 GMT pre-window (unchanged across EIGHT consecutive sweeps), 0 items in 8h window.
  - sans-isc               # RSS via fetch_feed — status 200, etag W/"1d42-6518fc275f070", last_modified 2026-05-11T19:29:04 GMT (15:29 EDT in-window from feed-server activity), 1 item in 8h window — "Why we use CAPTCHAs" diary already noted at 12:00 sentinel, anti-noise applies, no fresh threat-intel content in 8h window.
  - rapid7                 # RSS via fetch_feed — status 200, last_modified 2026-05-11T19:16:38 GMT (15:16 EDT in-window from feed-server activity), 1 item in 8h window — "Final Countdown: Last Chance to Join the Rapid7 Global Cybersecurity Summit" already noted at 12:00 sentinel (marketing/events), anti-noise applies.
  - sentinelone-labs       # RSS via fetch_feed — status 200, last_modified 2026-05-11T15:44:32 GMT, 0 items in 8h window after since-filter.
  - sophos                 # RSS via fetch_feed (news.sophos.com/feed/) — status 200, 9 items in feed total, 0 items in 8h window.
  - eset-welivesecurity    # RSS via fetch_feed — status 200, 100 items in feed total, 0 items in 8h window.
  - cisa-advisories        # all.xml RSS via fetch_feed — status 200, 30 items in feed total, 0 items in 8h window after since-filter.
  - hacker-news            # feedburner/TheHackersNews RSS via fetch_feed — status 200, last_modified 2026-05-11T19:16:20 GMT (15:16 EDT in-window from feed-server activity), 4 items in 8h window after since-filter (TeamPCP Checkmarx Jenkins AST plugin restatement at 14:30 EDT in-window — same TeamPCP/Checkmarx thread covered in finding-2026-05-11-0001 and earlier sentinel reasoning trail, anti-noise applies; cPanel CVE-2026-41940 under active exploitation by Mr_Rot13 at 13:54 EDT in-window — RAW-SIGNALED as PM-003 with IOC extraction; AI-generated zero-day 2FA bypass first known mass exploitation at 11:45 EDT in-window — material consolidated into PM-001 as third corroborating source; Weekly Recap at 08:36 EDT in-window — aggregator content, filtered).
  - ars-feed-root          # ars-security stale workaround — arstechnica.com/feed/ root path via fetch_feed, status 200, etag "0ed6d924f8d88d77524f2c055e3a38f4", last_modified 2026-05-11T18:24:26 GMT (14:24 EDT in-window from feed-server activity), 7 items in 8h window. Two with potential security-adjacency: "Starlink shuts down its GPS-style cheat code" by Jeremy Hsu at 13:55 EDT in-window (Starlink PNT capability shutdown ahead of SpaceX IPO — space/satellite-class topic but vendor business-decision and academic-research framing, NOT a threat-research disclosure; A&D-relevance capability-level only; NO threat actor, NO CVE, NO IOC; NOT raw-signaled per Mode 1 procedure no-watchlist/roster/vuln-index hit) and "Indian launch startup Skyroot nears first orbital test flight" by Eric Berger at 09:53 EDT in-window (commercial-space business reporting; no security content; not raw-signaled). Other 5 items consumer/health/gaming/F1/Apple-OS, all filtered.
  - cisa-kev               # JSON feed via WebFetch — full-catalog scan for dateAdded >= 2026-05-11 returned zero entries. Most recent KEV add remains CVE-2026-42208 (BerriAI LiteLLM, dateAdded 2026-05-08, dueDate 2026-05-11 = today; deadline passed earlier this afternoon without KEV-update reflecting compliance status — standard pattern, KEV does not publish compliance-status changes). CVE-2026-41940 (cPanel) presence on KEV NOTED separately during PM-003 evaluation (added 2026-04-30 per source-health note, 11 days post-disclosure; this afternoon's QiAnXin XLab research is post-KEV-addition operational detail, not a fresh KEV-add event).
  - nvd                    # WebFetch on services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=2026-05-11T16:00:00Z&lastModEndDate=2026-05-11T19:30:00Z (12:00-15:30 EDT slice) cvssV3Severity=CRITICAL → 3 entries. CVE-2022-32224 (Rails Active Record YAML deserialization 9.8 — 2022 disclosure, patched 5.2.8.1+/6.0.5.1+/6.1.6.1+/7.0.3.1+, NVD lastModified is metadata refresh; not fresh). CVE-2024-43455 (Windows RDP Licensing Service spoofing 9.8 — Microsoft-issued security updates available; not fresh). CVE-2025-14087 (GLib GVariant parser heap-corruption 9.8 — already disposed at 12:00 sentinel as patch-available no-ITW). All three DISCARDED per Mode 1 procedure (no in-window fresh-disclosure, no A&D / tracked-actor / tracked-vuln hit, no in-the-wild observation flags). Routine NVD churn.
  - splunk-archimedes      # tstats over 8h NOT sourcetype=archimedes:* — zero events. Targeted IOC keyword sweep across 13 high-priority tokens (Cl0p, TeamPCP, UNC6780, UNC2814, APT45, "Dirty Frag", CVE-2026-41940, Mr_Rot13, Checkmarx, SailPoint, Instructure, "South Staffordshire Water", Filemanager) over 24h returned 4 events — ALL archimedes:operation / archimedes:scheduler pipeline self-references (08:00 morning brief_published referencing TeamPCP roster actor in related_actors and Checkmarx in related_campaigns; 08:17 git_committed for the morning brief; 06:08 flash_sweep_clean from 06:00 FLASH; 00:14 flash_sweep from midnight sweep). Pipeline self-references match keyword set in payload but reflect Archimedes' own operational logging. Thirteenth consecutive sweep with dormant non-archimedes-internal stream pattern.
  - splunk-defenseclaw     # NOT sourcetype=archimedes:* over 8h returns zero events; over 24h also zero. Thirteenth consecutive sweep with dormant non-archimedes-internal stream pattern across both indexes.
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH; ~27h elapsed at this sweep, eligible-to-retry per 24h-rule but pre-brief scope kept to RSS/vendor/KEV priority. Treating as effectively stale until operator alt-pool / direct-X-API decision.
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted (4 consecutive 404s prior). Pre-brief scope skips.
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround in use (arstechnica.com/feed/ root path — covered above).
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom; per-repo GHSA fallback path remains productive workaround when triggered; not triggered this sweep
  - iran-monitor           # iranmonitor.org 403 WAF/UA workaround pending
  - mandiant-feedburner    # feedburner.com/Mandiant 404 SIXTEENTH consecutive pattern; cloud.google.com/blog/topics/threat-intelligence index page WebFetch was invoked to corroborate the GTIG AI-zero-day publication (surfaced as #2 visible position: "GTIG AI Threat Tracker: Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access" — confirms today's BleepingComputer + SecurityWeek + HackerNews relays). Direct Mandiant blog primary remains operator-pending for an alt-endpoint decision.
sources_health_changed_this_sweep:
  - source_yaml_id: bleepingcomputer
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: securityweek
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: the-record
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: hacker-news
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: cisa-advisories
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: mstic
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: unit42
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: sans-isc
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: rapid7
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: sentinelone
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: sophos
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: krebs
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: nvd
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: cisa-kev
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: splunk-archimedes
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: splunk-defenseclaw
    field: last_successful_fetch
    new_value: 2026-05-11T15:30:00-04:00
    runtime_field: yes
  - source_yaml_id: mandiant
    field: failure_count
    old_value: 13
    new_value: 13
    note: "Held — this pre-brief sweep used the cloud.google.com index-page WebFetch workaround (which DID surface the new GTIG AI Threat Tracker post at #2 visible position), not a direct feedburner.com/Mandiant retry. failure_count therefore NOT incremented this sweep. The fundamental feedburner endpoint state remains unchanged. Operator alt-endpoint decision pending."
    runtime_field: yes
match_reason:
  watchlist: []
  actors: [TeamPCP, Cl0p]
  vulnerabilities: [CVE-2026-41940]
  keywords: [ai-generated-exploit, gtig, mandiant, mr-rot13, cpanel, filemanager, south-staffordshire-water, ico-fine, drone-router-fcc, starlink-pnt-shutdown, dirty-frag-anti-noise, instructure-anti-noise, build-app-firewalls-anti-noise]
triage_tags: [pre_brief_sweep_summary, active_hours, multi_source_corroboration_ai_zero_day, cl0p_roster_018_historical_incident_regulatory_closure, cpanel_kev_listed_mass_exploitation_operational_detail, fcc_drone_router_ad_adjacent_regulatory, ars_security_workaround_root_feed_in_use, splunk_dormant_13th_consecutive_pm_sweep, mandiant_feedburner_16th_consecutive_pattern]
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      The cPanel CVE-2026-41940 + Mr_Rot13 mass-exploitation story
      (PM-003) is a CRITICAL CVE with confirmed in-the-wild
      mass-exploitation (2,000+ attacker source IPs per QiAnXin
      XLab), but the CVE was added to CISA KEV on 2026-04-30 —
      eleven days prior to this sweep — and the BleepingComputer
      + SecurityWeek + The Hacker News coverage trail across the
      intervening period has already been touched. Today's
      QiAnXin XLab research adds OPERATIONAL DETAIL (IOC set:
      cp.dene[.]com, wrned[.]com, wpsock[.]com, helper.php hash
      2d7d121dfcca6c17130ef605124869bf84ce77bee343ada78e0db2236174583a;
      named-operator attribution: Mr_Rot13; backdoor family name:
      Filemanager) but the CVE-itself-is-KEV-with-active-exploitation
      gate was tripped 11 days ago. Per FLASH-POLICY anti-noise
      rule, the Trigger 1 event for this CVE belongs to the
      KEV-add date, not to subsequent operational detail. Today's
      research is grader-queue-worthy for vuln-tracker awareness
      but not Trigger 1 reset.

      The Google AI-zero-day story (PM-001) involves a confirmed
      in-the-wild exploit but the CVE is UNASSIGNED (Google
      coordinated disclosure with vendor; no CVE published yet).
      Trigger 1 requires CVSS >= 9.0 — without a CVE-assigned-CVSS,
      the gate cannot be evaluated cleanly. Per strict reading,
      Trigger 1 fails (CVSS-unascertainable).

      NVD lastModStartDate window query 12:00-15:30 EDT slice
      (16:00-19:30 UTC): CRITICAL = 3 entries (Rails Active Record
      CVE-2022-32224, Windows RDP Licensing CVE-2024-43455, GLib
      CVE-2025-14087). All three are post-patch publications
      with NVD metadata-refresh framing; none documented in-the-wild
      with mass exploitation today. Trigger 1 not matched on
      window-fresh NVD entries.

      Trigger 1 not matched.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      Two in-window items mention tracked-roster actors:

      - PM-001 (Google AI-zero-day, GTIG): The Hacker News piece
        notes the broader GTIG AI Threat Tracker report
        references TeamPCP (UNC6780) as one example of a threat
        actor leveraging AI in adjacent operations, alongside
        UNC2814 (China-linked, not in roster), APT45 (DPRK,
        not in roster), UNC5673, UNC6201, Russian "Operation
        Overload". TeamPCP is roster #001 HIGH. HOWEVER, the
        specific zero-day-developing actor is EXPLICITLY
        UNATTRIBUTED ("unknown threat actor"). The TeamPCP
        mention is a RESTATEMENT of prior AI-tradecraft
        observations, not a new attribution event. Per
        FLASH-POLICY Trigger 2 strict reading, restatement
        fails the new-attribution test.

      - PM-002 (South Staffordshire Water / Cl0p £963.9K
        ICO fine): The ICO regulatory action attributes the
        2022 breach to Cl0p (roster #018 HIGH). This is a
        RESTATEMENT of attribution that was established in
        2022 — Cl0p claimed the breach on its leak site at
        the time, and the ICO's regulatory framing accepts
        the Cl0p attribution without new technical evidence.
        The 2026-05-11 news event is regulatory closure on a
        2022 incident, not a fresh attribution. Trigger 2
        requires NEW attribution — fails.

      Trigger 2 not matched.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party check across both archimedes and
      defenseclaw_local indexes over 8h window via tstats and
      via NOT sourcetype=archimedes:* keyword sweep: zero
      events.

      Targeted IOC keyword sweep across 13 high-priority tokens
      (Cl0p, TeamPCP, UNC6780, UNC2814, APT45, "Dirty Frag",
      CVE-2026-41940, Mr_Rot13, Checkmarx, SailPoint, Instructure,
      "South Staffordshire Water", Filemanager) over 24h with
      NOT sourcetype=archimedes:* filter returned zero events.
      The 4 hits returned without the NOT-filter are all
      Archimedes' own pipeline self-references (08:00 morning
      brief_published, 08:17 git_committed, 06:08
      flash_sweep_clean, 00:14 flash_sweep) — correctly
      excluded by the NOT-archimedes filter.

      The PM-003 cPanel IOC set (cp.dene[.]com, wrned[.]com,
      wpsock[.]com, helper.php SHA-256 hash) was specifically
      checked against splunk-archimedes and splunk-defenseclaw
      over 30d via a targeted search: zero hits. None of the
      PM-003 IOCs has been observed on first-party telemetry.

      Thirteenth consecutive PM-sweep with dormant
      non-archimedes-internal stream pattern across both indexes.
      Trigger 3 cannot fire on a dormant external-telemetry
      stream.

      Trigger 3 not matched.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      The Google AI-zero-day GTIG research (PM-001) describes a
      NEW OPERATIONAL CLASS — "first known in-the-wild use of
      AI for vulnerability discovery and exploit generation in
      a mass-exploitation campaign" per Google's own framing.
      This is a substantial TTP-class observation. HOWEVER,
      FLASH Trigger 4 requires the change to be ATTRIBUTABLE
      to a TRACKED-ROSTER actor — and the developing actor is
      EXPLICITLY UNATTRIBUTED. The tracked-actor references
      (TeamPCP/UNC6780, APT45, UNC2814, etc.) are in the
      adjacent-cases section of the GTIG AI Threat Tracker
      report, not the central zero-day exploit case.

      Strict Trigger 4 reading: fails on attribution-coupling
      gate. The TTP-class observation is significant for grader
      / vuln-tracker / next-day awareness but does not clear
      the FLASH bar this sweep.

      No other tracked-actor TTP-change content in-window from
      MSTIC / Mandiant / CrowdStrike / Unit 42 / SentinelLabs /
      Sophos / ESET / Rapid7 / Recorded Future / Dragos /
      Proofpoint (all either dateless or pre-window or marketing
      content this sweep).

      Trigger 4 not matched.
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      No active multi-victim campaign explicitly targeting A&D
      or watchlist entities surfaced in the 8h window.

      PM-004 (FCC drone/router update-ban deadline extension to
      2029) is A&D-adjacent at CAPABILITY-LEVEL via
      counter-UAS / foreign-vendor-cyber-risk policy framing,
      but the news event is regulatory deadline-extension, NOT
      an active campaign with named A&D victims. No tracked
      actor, no CVE, no IOCs.

      The Cl0p / South Staffordshire Water item (PM-002) is
      multi-victim historical (4.1TB of customer data published
      2022) but explicit victim sector is UK WATER UTILITY,
      not A&D. Cl0p's broader 2022 MOVEit / GoAnywhere campaigns
      did touch A&D primes BUT today's news is the South Staffs
      Water regulatory closure specifically, not a fresh A&D-prime
      victim.

      No named A&D primes in any in-window item.

      Trigger 5 not matched.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      The Google AI-zero-day exploit (PM-001) targets a zero-day
      in an unnamed open-source web admin tool — but Google
      states the attack was "foiled before the mass exploitation
      phase" and Google "worked with vendor to prevent mass
      exploitation." Patch-coordination-underway language
      suggests the vendor is on track to patch (or has already
      patched as part of coordinated disclosure). The pre-patch
      condition cannot be cleanly evaluated without the CVE /
      vendor / product disclosed; Google's framing implies
      coordinated-disclosure-with-patch rather than open
      zero-day window.

      The cPanel CVE-2026-41940 has been patch-available since
      disclosure date 2026-04-30 (per CISA KEV); this is
      post-patch active exploitation, not pre-patch zero-day.

      The Dirty Frag Linux kernel bug (in-window via The Record)
      has been covered extensively in prior corpus with
      MSTIC active-attack post 2026-05-08; not a pre-patch
      zero-day at this sweep.

      Trigger 6 not matched.
post_evaluation_summary:
  pre_brief_raw_signals_written:
    - raw-2026-05-11-pm-000-sentinel-pre-brief-sweep.md       # this file
    - raw-2026-05-11-pm-001-bleepingcomputer-securityweek-hackernews-google-gtig-ai-generated-zero-day.md
    - raw-2026-05-11-pm-002-the-record-cl0p-south-staffordshire-water-ico-fine.md
    - raw-2026-05-11-pm-003-hackernews-cpanel-cve-2026-41940-mass-exploitation-mr-rot13.md
    - raw-2026-05-11-pm-004-the-record-fcc-drone-router-update-ban-deadline-extension-2029.md
  flash_triggers_fired: 0
  flash_awareness_items_noted: 2
  flash_awareness_detail: |
    Two items merit grader awareness for FLASH-trigger marginal
    reasoning:

    1. PM-001 Google AI-zero-day — Trigger 4 marginal fail on
       attribution-coupling gate (UNATTRIBUTED actor + new
       operational class). The TTP-class observation
       ("first known in-the-wild AI-generated zero-day exploit")
       is significant procedural intelligence and would be
       Trigger 4 if attribution surfaced. Recommend grader
       monitor for follow-on attribution by Mandiant / GTIG /
       Unit 42 / CrowdStrike in coming days.

    2. PM-003 cPanel CVE-2026-41940 + Mr_Rot13 — Trigger 1
       marginal fail on KEV-add-precedence (already KEV-listed
       2026-04-30; today is operational-detail / IOC-set
       addition). The 2,000+-source-IP mass exploitation
       observation is operationally significant for vuln-tracker
       and any A&D contractors running cPanel/WHM (consumer-
       hosting class; A&D-relevance LOW but capability-level
       awareness for hosted-website attack surface). IOC set
       extracted and ready for splunk-archimedes / first-party
       sweep pipeline integration.
  non_flash_raw_signals_written: 4
  grader_queue_handoff:
    - raw-2026-05-11-pm-001         # Trigger 4 marginal, TTP-class observation, tracked-actor TeamPCP restated
    - raw-2026-05-11-pm-002         # tracked-actor Cl0p (#018 HIGH) historical-incident regulatory closure
    - raw-2026-05-11-pm-003         # Trigger 1 marginal, KEV CVE operational detail + IOC extraction
    - raw-2026-05-11-pm-004         # A&D-adjacent capability-level regulatory signal
  next_action: |
    Per Mode 1 procedure: pre-brief raw-signal files written to
    threats/raw-signal/ for grader queue consumption at
    16:00 EDT afternoon brief composition.

    Carry-forward state for 16:00 brief:
    - Two tracked-actor touches (TeamPCP restated in GTIG AI
      Threat Tracker; Cl0p regulatory closure on 2022 incident)
    - One CISA KEV-listed CVE with fresh operational detail
      and 2,000+-source-IP mass exploitation (cPanel
      CVE-2026-41940, A&D-relevance LOW)
    - One A&D-adjacent regulatory signal (FCC drone/router
      update-ban deadline extension)
    - One TTP-class observation worth procedural noting
      (first known in-the-wild AI-generated zero-day exploit)

    Next FLASH sweep: 2026-05-11 18:00 EDT (~2.5 hours).
    Active hours end 21:00 EDT.
iocs_extracted: false        # sentinel only; PM-001/PM-003 carry IOC extractions in their own files
iocs_count: 0
text_word_count: 0
promoted: false
promotion_not_applicable: true
promotion_not_applicable_reason: "Sentinel sweep summary (Mode 1 collector pre-brief reasoning trail), not a finding candidate. Sibling raw-signal pm-001/pm-002/pm-003/pm-004 carry the actual claims; this file is the sweep-state record. Per grader procedure, sentinels are NOT graded as standalone clusters. Reviewed during afternoon-20260511-160000 grading run."
reviewed_by_grading_run_id: afternoon-20260511-160000
ttl_expires_at: 2026-08-09T15:32:00-04:00
---

# Pre-brief Collection Sentinel — 2026-05-11 15:30 EDT (8h Window)

**Four raw-signal files written this sweep, ALL non-FLASH grader-queue items.**
No FLASH triggers cleared. Three items mention tracked-roster actors
(TeamPCP roster #001 via GTIG AI Threat Tracker; Cl0p roster #018 via
South Staffordshire Water ICO regulatory closure) but all attribution
events are RESTATEMENTS of prior attribution rather than fresh
tracked-actor naming.

## Window summary

- **Time window:** 2026-05-11T07:30 → 2026-05-11T15:30 EDT (8h)
- **Active hours status:** ACTIVE (current local time ~15:32 EDT,
  inside 09:00-21:00 EDT window)
- **Sources queried (healthy):** 19 (RSS feeds + KEV JSON + NVD
  REST + Splunk x2 + cloud.google.com index page workaround for
  Mandiant primary). Ars Technica root-feed workaround in use.
- **Sources skipped stale:** 3 nitter/X delistings + ars-security
  404 (workaround in use) + 3 MCP-missing / API-key-missing
  (censys, urlscan, hibp).
- **Sources soft-failing this sweep:** 4 carry-forward (threatfox,
  malwarebazaar, github-advisories MCP-pending; iran-monitor WAF
  pending; mandiant feedburner 16th-consecutive 404 with index-page
  workaround productive this sweep).

## Raw-signal files written

| File | Topic | Tracked actor / CVE | Trigger eval |
|---|---|---|---|
| pm-000 | This sentinel | — | sweep summary |
| pm-001 | GTIG AI-Generated Zero-Day Exploit (Mandiant/GTIG primary; BleepingComputer + SecurityWeek + HackerNews relays) | TeamPCP (#001 HIGH) restated; UNC2814 / APT45 / UNC5673 / UNC6201 / Russian "Operation Overload" referenced as adjacent cases (none in roster) | Trigger 4 marginal-fail (UNATTRIBUTED actor for the zero-day) |
| pm-002 | South Staffordshire Water Cl0p £963.9K ICO fine (The Record / Alexander Martin) | Cl0p (#018 HIGH) restated | Trigger 2 fails (RESTATEMENT not new attribution) |
| pm-003 | cPanel CVE-2026-41940 mass exploitation by Mr_Rot13 (HackerNews relay of QiAnXin XLab) | CVE-2026-41940 (KEV-listed 2026-04-30); Mr_Rot13 NOT in roster | Trigger 1 marginal-fail (CVE already KEV-listed 11 days ago) |
| pm-004 | FCC drone/router update-ban deadline extension to 2029 (The Record / Suzanne Smalley) | No actor / no CVE | A&D-adjacent capability-level regulatory signal |

## Trigger evaluation — all six triggers FAILED

| # | Trigger | Result | Driver |
|---|---|---|---|
| 1 | Critical CVE exploited | FAIL | cPanel CVE-2026-41940 KEV-added 11 days ago (FLASH-trigger event belongs to KEV-add date, not to operational-detail follow-on). Google AI-zero-day CVE UNASSIGNED. NVD CRITICAL window has 3 entries, all post-patch metadata refresh. |
| 2 | Tracked-actor attribution | FAIL | TeamPCP restated in GTIG AI Threat Tracker (adjacent-cases section, NOT central zero-day case). Cl0p attribution restated in ICO regulatory closure on 2022 incident. Both restatements, not fresh. |
| 3 | First-party IOC hit | FAIL | Splunk dormant on non-archimedes-internal stream (THIRTEENTH consecutive PM-sweep). cPanel IOC set + Cl0p historical IOCs checked against -30d — zero hits. |
| 4 | Tracked-actor TTP change | FAIL | Google AI-zero-day operational class IS new ("first known in-the-wild AI-generated zero-day") but actor UNATTRIBUTED — Trigger 4 requires tracked-actor coupling. |
| 5 | A&D-sector campaign | FAIL | PM-004 FCC drone-policy news is regulatory deadline-extension, not active campaign. PM-002 South Staffs Water is utility (not A&D). No named A&D primes anywhere. |
| 6 | Zero-day no patch | FAIL | Google AI-zero-day appears coordinated-disclosure-with-patch (Google "worked with vendor"). cPanel CVE patch-available since 2026-04-30. Dirty Frag has prior patch (extensively covered). |

## Notable awareness items

**GTIG AI Threat Tracker as a new operational-class observation.**
Google's report is the first public assertion of in-the-wild AI-generated
zero-day exploit use in a mass-exploitation operation. The threat-class
implication for A&D contractors is substantial — particularly for any
A&D supplier running the unnamed open-source web admin tool. The
specific CVE and product remain undisclosed during coordinated
disclosure. Mandiant / GTIG primary referenced as:

    cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access
    (per BleepingComputer / HackerNews / SecurityWeek relays — direct fetch
    of cloud.google.com primary URLs from Archimedes' WebFetch tool has
    been historically unreliable; the cloud.google.com/blog/topics/threat-
    intelligence INDEX page WebFetch was productive this sweep, surfacing
    the new GTIG report at #2 top-of-list position with "GTIG AI Threat
    Tracker: Adversaries Leverage AI for Vulnerability Exploitation,
    Augmented Operations, and Initial Access" by GTIG byline. The Hacker
    News relay specifically names the actor as UNC6780 / TeamPCP for one
    of the AI-tradecraft examples in the broader report.)

The cPanel mass exploitation (PM-003) carries the most actionable
IOC set of the sweep — domain trio cp.dene[.]com / wrned[.]com /
wpsock[.]com plus SHA-256 hash
2d7d121dfcca6c17130ef605124869bf84ce77bee343ada78e0db2236174583a
for helper.php Filemanager backdoor. None observed on first-party
Splunk telemetry. Available for any vuln-tracker / actor-profiler
downstream pivots.

## Anti-noise applied this sweep

Per FLASH-POLICY rule 1 (one FLASH per trigger topic per 24h):
- Instructure/Canvas/ShinyHunters: extensive prior corpus coverage
  across 2026-05-08/09/10/11 (covered at 12:00 sentinel and morning
  brief). Today's BleepingComputer follow-on (Instructure confirms
  XSS as the vector) is procedural confirmation, not posture
  escalation. NOT raw-signaled.
- SecurityWeek "Build Application Firewalls" editorial: same
  Checkmarx Jenkins chain restatement covered at 12:00 sentinel.
  Anti-noise applies. NOT raw-signaled.
- Dirty Frag Linux kernel: covered extensively in corpus since
  2026-05-08 MSTIC active-attack post. The Record's 2026-05-11
  "second major bug" article is incremental restatement / context.
  Anti-noise applies. NOT raw-signaled.
- TheHackerNews "TeamPCP Compromises Checkmarx Jenkins AST Plugin"
  (14:30 EDT in-window): direct restatement of finding-2026-05-11-0001
  (Checkmarx Jenkins TeamPCP supply-chain compromise published 09:30
  EDT this morning via SecurityWeek). Anti-noise applies. NOT
  raw-signaled (the morning brief already covered the operational
  detail in finding-2026-05-11-0001).
- Rapid7 cybersecurity summit promo: marketing content, filtered.
- Specops sponsored Active Directory breach content: filtered.
- BleepingComputer "Webinar this week" promo: filtered.
- Frame Security $50M funding announcement: financial / industry
  news, no threat content, filtered.
- Starlink GPS-style PNT shutdown: space/satellite-class but vendor
  business decision (pre-IPO de-risking) + academic-research framing,
  NOT a threat-research disclosure. No actor, no CVE, no IOC. NOT
  raw-signaled per Mode 1 procedure (no watchlist / roster / vuln-index
  hit). Flagged here for orchestrator awareness — the Starlink PNT
  capability shutdown has potential A&D-relevance via GPS-jamming
  resilience for ITAR-regulated platforms, but at capability-level
  policy / business-decision tier, not operational-threat tier.

## Source-health observations (this sweep)

**No fresh stale flips this sweep.** Carry-forward set unchanged from
12:00 FLASH sentinel:

- `mandiant` — feedburner.com/Mandiant 404 SIXTEENTH consecutive
  pattern; cloud.google.com/blog/topics/threat-intelligence INDEX
  PAGE WebFetch workaround was PRODUCTIVE this sweep (surfaced the
  new GTIG AI Threat Tracker post at #2 top-of-list). The workaround
  is functional but operator alt-RSS-endpoint discovery decision
  remains pending.
- `crowdstrike` — SIXTEENTH consecutive sweep with dateless-marketing
  pattern (per 12:00 sentinel; same 10-item pile).
- `ars-security` — root-feed workaround (arstechnica.com/feed/)
  remains productive for the security-adjacent subset of content;
  the security-specific feeds.arstechnica.com endpoint remains
  stale (operator path-replacement decision pending).
- `x-cisagov`, `x-gossithedog` — same nitter-pool blockers as prior
  sweeps; x-cisagov stale_since 2026-05-10 12:00 ~27h ago at this
  sweep (eligible-to-retry per 24h rule on next sweep).
- `threatfox`, `malwarebazaar`, `github-advisories`, `iran-monitor`,
  `censys`, `urlscan`, `hibp` — same MCP-pending / endpoint-broken /
  WAF-blocked / key-missing blockers as prior sweeps.

## Splunk first-party state

THIRTEENTH consecutive PM-sweep with dormant non-archimedes-internal
stream pattern across both archimedes and defenseclaw_local indexes.
The 4 hits returned to the targeted IOC keyword sweep are all
Archimedes' own pipeline self-references (08:00 morning brief publish,
08:17 git commit, 06:08 FLASH-clean event, 00:14 FLASH-clean event).
NOT-archimedes-internal filter correctly excludes these.

PM-003 cPanel IOC set specifically checked over -30d against both
indexes: zero hits. None of cp.dene[.]com / wrned[.]com / wpsock[.]com
or the helper.php SHA-256 hash observed on first-party telemetry.

## Next sweep

Next checkpoint: **2026-05-11 16:00 EDT — Afternoon Brief composition
phase** (briefer + grader read the 4 PM raw-signal files plus the AM
batch from morning sweep + the 12:00 sentinel).

Following that: **2026-05-11 18:00 EDT FLASH sweep** (~2.5 hours from
this pre-brief). Active hours end 21:00 EDT.
