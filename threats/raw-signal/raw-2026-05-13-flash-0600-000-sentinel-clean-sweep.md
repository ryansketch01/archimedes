---
raw_id: raw-2026-05-13-flash-0600-000
collected_at: 2026-05-13T06:05:00-04:00
run_id: flash-sweep-20260513-060000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-13T06:00:00-04:00
time_window_start: 2026-05-13T00:00:00-04:00
time_window_end: 2026-05-13T06:00:00-04:00
test: false
quiet_hours_active: true                  # 06:00 EDT inside 21:00-09:00 EDT window
sources_queried:
  - bleepingcomputer       # RSS via fetch_feed — status 200, etag 3eeaef1bd1ed01af1b017485c00c69c9, last_modified 2026-05-13T09:50:08 GMT (05:50 EDT in-window from feed-server activity), 0 items in 6h window after since-filter. 15 items total in feed; most recent appear to be 2026-05-12-dated already-covered topics.
  - securityweek           # RSS via fetch_feed — status 200, etag W/195b50c9ad295345bf345f9cbb8885d5, last_modified 2026-05-13T09:36:59 GMT (05:36 EDT in-window from feed-server activity), 4 items in 6h window after since-filter. ALL four items reviewed; FLASH-trigger evaluation per item below.
  - the-record             # RSS via fetch_feed — status 200, 5 items total in feed, 0 items in 6h window after since-filter (most recent dated 2026-05-08; weekend cadence quiet through Wednesday morning).
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-12T22:02:01 GMT pre-window, 0 items in 6h window after since-filter. Normal Krebs cadence.
  - sans-isc               # RSS via fetch_feed (rssfeed.xml) — status 200, etag W/1fc0-651b007b87408, last_modified 2026-05-13T09:59:05 GMT (05:59 EDT in-window from feed-server activity), 1 item in 6h window after since-filter. (1) "Guest Diary - Tearing apart website fraud to see how it works" (Joshua Nikolson SANS.edu BACS intern, 2026-05-13T06:29:07Z = 02:29 EDT in-window) — student diary on phishing-site analysis methods, defensive/educational content, NO threat actor, NO fresh CVE, NO IOCs, NO A&D specific. DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit).
  - cisa-advisories        # all.xml RSS via fetch_feed — status 200, 30 items in feed total, 0 items in 6h window after since-filter. 2026-05-12 ICS batch (covered at PM-004 + finding-2026-05-12-0006 + afternoon brief) remains the most recent CISA activity. The Siemens / Schneider / CISA May 13 ICS Patch Tuesday cohort (announced via SecurityWeek in-window) has not yet propagated to the all.xml feed at this sweep time — CISA's ICS advisory publication typically posts at 12:00 UTC = 08:00 EDT later this morning, after this sweep window closes.
  - cisa-kev               # JSON catalog via WebFetch — top 10 most recent entries returned. ZERO entries dateAdded >= 2026-05-12 (corroborates the day's KEV-quiet pattern; full-catalog scan unchanged across all four 2026-05-12 sweeps + 2026-05-13 00:00 sweep). Most recent KEV addition remains CVE-2026-42208 (BerriAI LiteLLM, dateAdded 2026-05-08). CVE-2024-1708 ConnectWise ScreenConnect dueDate 2026-05-12 = YESTERDAY EOB now passed; CVE-2026-32202 Microsoft Windows dueDate 2026-05-12 = YESTERDAY EOB now passed (KEV catalog does not publish compliance-status changes against passed deadlines). CVE-2026-31431 Linux Kernel dueDate 2026-05-15 = T+2d.
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, etag "34e1865375dd494f6ac6bbc5a8f31b9a-gzip", last_modified 2026-05-12T23:45:12 GMT pre-window unchanged from 00:00 sweep, 0 items in 6h window. The MDASH disclosure + AI-synthetic-logs research from 18:00 EDT yesterday remain the most recent MSTIC content (both flagged for 2026-05-13 morning-brief orchestrator awareness at 00:00 FLASH sentinel; not raw-signaled at FLASH severity).
  - unit42                 # RSS (feedburner) via fetch_feed — status 200, last_modified 2026-05-11T22:51:12 GMT pre-window unchanged across multiple sweeps, 0 items in 6h window. The 2026-05-11 AD CS Escalation piece (Fighting Ursa = APT28 alias) remains the most recent post.
  - rapid7                 # RSS via fetch_feed (rapid7.com/blog/rss/) — status 200, last_modified 2026-05-13T09:46:34 GMT (05:46 EDT in-window from feed-server activity), 0 items in 6h window after since-filter. Yesterday's Patch Tuesday post remains in feed but pre-window from this sweep's perspective.
  - sentinelone-labs       # RSS via fetch_feed (sentinelone.com/labs/feed/) — status 200, etag W/31fd8980d598cf52bd58ea99c999b5b4, last_modified 2026-05-12T21:51:28 GMT pre-window, 0 items in 6h window.
  - sophos                 # RSS via fetch_feed (news.sophos.com/feed/) — status 200, 9 items total in feed, 0 items in 6h window. Normal cadence.
  - eset-welivesecurity    # RSS via fetch_feed — status 200, 100 items total in feed, 0 items in 6h window.
  - crowdstrike            # feedburner.com/crowdstrike returned 404 this sweep (first observed 404 on the crowdstrike feedburner endpoint — historically had returned valid-but-dateless marketing content). Different failure mode than the dateless-marketing pattern of prior sweeps. POSSIBLY transient or POSSIBLY feedburner shutdown propagating to a second CrowdStrike-side feed (Mandiant feedburner has been dead for 19+ sweeps). Operator alt-endpoint discovery may be needed if persistent.
  - hacker-news            # WebFetch on thehackernews.com/ index — top 10 visible titles. ONE new 2026-05-13-dated article: "GemStuffer Abuses 150+ RubyGems to Exfiltrate Scraped U.K. Council Portal Data" (Socket researchers; UK local-government democratic-services portal scraping via RubyGems exfil — Lambeth / Wandsworth / Southwark ModernGov portals targeted; NO threat-actor attribution claimed by Socket ("not clear if related" to the RubyGems suspension event yesterday); NO A&D / NO roster actor / NO CVE; data-exfil pattern using RubyGems as a covert storage layer, NOT malware distribution. DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit). One additional 2026-05-13-dated article: "Android Adds Intrusion Logging for Sophisticated Spyware Forensics" — Google + Amnesty International + Reporters Without Borders defensive-tooling collaboration; awareness-relevant but NO threat-intel, NO CVE, NO actor, NO A&D-relevance; DISCARDED per Mode 1. Other top-10 items all 2026-05-12-dated already-covered topics (Exim BDAT, RubyGems suspension, TrickMo, Mini Shai-Hulud, Instructure, OpenAI Daybreak, iOS 26.5, Checkmarx Jenkins) — anti-noise applies.
  - cloud-google-blog-mandiant  # WebFetch on cloud.google.com/blog/topics/threat-intelligence top page — top-5 visible titles unchanged from 2026-05-12 afternoon + 2026-05-13 00:00 sweeps (GTIG AI Threat Tracker, UNC6692 Snow Flurries, deSouza AI vuln post, German Cyber Überfall, BRICKSTORM Defender's Guide). NO fresh GTIG content this 6h window. Mandiant feedburner endpoint /Mandiant continues 404 (TWENTIETH consecutive); failure_count 18 → 19.
  - splunk-archimedes      # search NOT sourcetype=archimedes:* over 24h returned zero events. Targeted IOC keyword sweep across 25 high-priority tokens (CVE-2026-0300, CVE-2026-44277, CVE-2026-26083, CVE-2026-8043, CVE-2026-45185, Ruggedcom, "PAN-OS", "Captive Portal", FortiSandbox, FortiAuthenticator, Xtraction, GemStuffer, RubyGems, "Mini Shai-Hulud", TeamPCP, UNC1549, APT28, APT29, "Volt Typhoon", "Salt Typhoon", "Charming Kitten", MuddyWater, APT37, APT40, APT41, Lazarus) over 24h returned 11 hits — ALL eleven are archimedes:operation pipeline self-references from 2026-05-12 brief cycles + 2026-05-13 00:00 FLASH sentinel commit (splunk_log.py emissions). Pipeline self-references match keyword tokens in JSON payloads but reflect Archimedes' own operational logging, NOT external observations. TWENTIETH consecutive sweep with dormant non-archimedes-internal stream pattern across both indexes.
  - splunk-defenseclaw     # NOT sourcetype=archimedes:* over 24h returns zero events. Twentieth consecutive sweep.
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH — ~66h since stale-flip; FLASH-fast scope kept to RSS / vendor / KEV / Splunk priority feeds; operator nitter-pool / direct-X-API decision still pending.
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted; >4 days stale.
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround in use (arstechnica.com/feed/ root path); root path not invoked this FLASH-fast sweep.
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation); awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom; per-repo GHSA fallback path remains productive workaround when triggered (not triggered this sweep)
  - proofpoint             # /us/threat-insight/blog/feed endpoint 404 since 2026-05-10 12:00 FLASH; alt /us/rss.xml corporate-news endpoint multi-day cadence; not invoked this sweep
  - iran-monitor           # iranmonitor.org 403 WAF/UA workaround pending
  - dragos                 # dragos.com/blog/feed/ returned 404 this sweep (consistent with 2026-05-13 00:00 FLASH first-tracked failure + 2026-05-09 collector-discovery issue noted in source-health.yaml afternoon-2026-05-09 entry); operator-side working RSS path identification still pending. failure_count 1→2 (now AT stale threshold; held healthy this sweep pending next-sweep-retry given the no-fresh-blocking-impact on this sweep — CISA ICS batch already covered yesterday, Dragos cadence is multi-day).
  - wiz-research           # wiz.io/blog/rss.xml returned 404 — first attempt at the wiz blog RSS endpoint via fetch_feed. Not previously in source-health.yaml. Provisional A vendor (added 2026-05-12 per finding-2026-05-12-FLASH-0001 Mini Shai-Hulud co-primary). Operator action: identify working wiz.io RSS path (or accept WebFetch on the blog index page as the productive endpoint).
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (TWENTIETH consecutive); failure_count 18→19. cloud.google.com index page WebFetch surfaced same top-5 visible titles as 2026-05-13 00:00 + 2026-05-12 afternoon sweeps (all out-of-window per prior triangulations). Held healthy pending operator alt-endpoint decision.
  - securityweek           # last_successful_fetch 2026-05-12T06:00 → 2026-05-13T06:00; 4 in-window items returned, ALL DISCARDED per FLASH-trigger analysis (Fortinet+Ivanti Patch Tuesday no-ITW, Chipmaker Patch Tuesday no-ITW, RubyGems suspension UPDATE-flag to 2026-05-12 PM coverage with no actor attribution, ICS Patch Tuesday cohort including Ruggedcom APE1808 + PAN-OS CVE-2026-0300 expanded-surface UPDATE flag to 2026-05-07 FLASH coverage). Single new productive sweep for this source after 5 consecutive 0-item sweeps; surfaced the Siemens Ruggedcom APE1808 + CVE-2026-0300 expanded-surface disclosure (flagged for 2026-05-13 morning-brief orchestrator awareness as Patch Tuesday UPDATE, NOT a FLASH).
  - sans-isc               # last_successful_fetch 2026-05-13T00:00 → 2026-05-13T06:00; 1 in-window item DISCARDED per Mode 1 procedure (Guest Diary student fraud-site analysis).
  - bleepingcomputer       # last_successful_fetch 2026-05-13T00:00 → 2026-05-13T06:00; 0 in-window items (RSS clean).
  - mstic                  # last_successful_fetch 2026-05-13T00:00 → 2026-05-13T06:00; 0 in-window items (last_modified unchanged from 00:00 sweep).
  - dragos                 # failure_count 1→2 (first tracked failure at 00:00 sweep + this sweep). Now AT stale-flip threshold per >=2 consecutive-failure rule. HOLDING healthy this sweep pending operator-side working RSS path identification (Dragos publication cadence is multi-day; CISA ICS batch + SecurityWeek ICS Patch Tuesday relay this morning cover the OT surface adequately for this 6h window). Next sweep failure WILL trip stale per rule unless operator surfaces a working endpoint.
  - crowdstrike            # feedburner.com/crowdstrike returned 404 this sweep — FIRST observed 404 on this endpoint after 19+ consecutive sweeps with dateless-marketing valid-RSS responses. failure_count 0→1. Different failure mode than the dateless-marketing pattern; possibly transient feedburner-side issue, possibly the feedburner CrowdStrike feed is shutting down (Mandiant feedburner has been dead for 20+ sweeps). HOLDING healthy this sweep; if 12:00 FLASH also 404s, structural concern about second-vendor feedburner reliance.
  - wiz-research           # wiz.io/blog/rss.xml 404 — first attempt at wiz blog RSS endpoint. failure_count 0→1. New source-health entry. Provisional A vendor per source-grades.yaml. Operator action: identify working wiz.io RSS path or accept WebFetch on blog index as productive endpoint.
match_reason:
  watchlist: []                          # Zero in-window items matched aerospace-defense.yaml watchlist (Ruggedcom APE1808 is industrial-OT critical-infrastructure adjacent — Critical Manufacturing / Energy / Transportation sectors per prior CISA APE1808 advisory sector listing — NOT named A&D primes)
  watchlist_match_strength: structural_only
  actors: []                             # Zero in-window items attributed any tracked actor from _roster.yaml. SecurityWeek language on Ruggedcom-APE1808+PAN-OS exploitation = "possibly by Chinese state-sponsored hackers" SPECULATIVE — no specific actor named (no Volt Typhoon / Salt Typhoon / APT40 / APT41 attribution).
  vulnerabilities:
    - CVE-2026-0300                       # Already FLASH'd 2026-05-07 + tracked-dossier; today's Ruggedcom APE1808 affected-surface disclosure is UPDATE flag, NOT fresh FLASH. Anti-noise per FLASH-POLICY one-per-topic-per-24h. (24h lock from prior FLASH long since expired but topic-level coverage saturation applies.)
    - CVE-2026-44277                      # Fortinet FortiAuthenticator — already raw-signaled at PM-002 yesterday + covered in finding-2026-05-12-0004; SecurityWeek today's relay confirms "not aware of any of the patched vulnerabilities being exploited in the wild" — anti-noise applies.
    - CVE-2026-26083                      # Fortinet FortiSandbox — same as above; SecurityWeek today's relay restates no-ITW conclusion already in finding-2026-05-12-0004.
    - CVE-2026-8043                       # Ivanti Xtraction (NEW today, CVSS 9.6, no ITW per Ivanti) — patches-at-disclosure, NOT in _index.yaml, no actor; Trigger 1 fails on active_exploitation, Trigger 6 fails on patch-available. DISCARDED.
    - CVE-2026-20794                      # Intel Data Center Graphics Driver buffer overflow (CVSS 9.3, no ITW per SecurityWeek) — fails Trigger 1 on active_exploitation, Trigger 6 on patch-available.
    - CVE-2026-0481                       # AMD ROCm Device Metrics Exporter (CVSS 9.2, no ITW) — same.
  keywords:
    - siemens_ruggedcom_ape1808_pan_os_cve_2026_0300_expanded_surface_morning_brief_candidate
    - fortinet_psirt_2026_05_13_anti_noise_pm_002_finding_0004
    - ivanti_xtraction_cve_2026_8043_no_itw_patched_at_disclosure
    - chipmaker_patch_tuesday_intel_amd_no_itw
    - rubygems_suspension_socket_no_actor_attribution
    - gemstuffer_socket_rubygems_uk_council_scraping_no_actor_no_ad
    - patch_tuesday_may_2026_no_itw_cross_corroboration_securityweek
    - mini_shai_hulud_anti_noise_24h_lock_expired_06_30
    - mstic_mdash_capability_disclosure_no_itw_carry_forward_morning_brief
triage_tags:
  - sentinel
  - flash_sweep_0600_2026_05_13
  - quiet_hours_active
  - clean_sweep
  - zero_flash_triggers_matched
  - siemens_ruggedcom_ape1808_pan_os_cve_2026_0300_expanded_surface_morning_brief_candidate
  - patch_tuesday_may_2026_securityweek_no_itw_cross_corroboration
  - fortinet_ivanti_psirt_2026_05_13_anti_noise_to_finding_2026_05_12_0004
  - chipmaker_patch_tuesday_intel_amd_no_itw_anti_noise
  - mandiant_feedburner_20th_consecutive_404
  - splunk_dormant_20th_consecutive
  - dragos_feed_404_2nd_consecutive_at_stale_threshold
  - crowdstrike_feedburner_first_404_after_19_marketing_sweeps
  - wiz_research_rss_endpoint_404_first_attempt
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      Siemens-disclosed Ruggedcom APE1808 affected by Palo Alto PAN-OS
      CVE-2026-0300 (User-ID Captive Portal unauthenticated buffer
      overflow → root RCE; CVSS v4.0 9.3; "limited exploitation
      observed" per Palo Alto PSIRT 2026-05-05 advisory + KEV-added
      2026-05-06 + dueDate 2026-05-09 EOB passed) is the closest
      structural Trigger 1 candidate this sweep, but FAILS on the
      one-FLASH-per-topic-per-24h anti-noise rule. CVE-2026-0300 was
      already FLASH'd at 2026-05-07T11:32 EDT (threats/briefs/
      2026-05-07-flash-0000-pan-os-cl-sta-1132.md) and has its own
      dedicated vulnerability-tracking dossier
      (threats/vulnerabilities/PAN-OS-CVE-2026-0300/). The Ruggedcom
      APE1808 expanded-surface disclosure today via Siemens (relayed
      SecurityWeek 06:50 EDT) is meaningful UPDATE intel — Ruggedcom
      is deployed in Critical Manufacturing / Energy / Transportation
      sectors per prior CISA APE1808 advisory sector listing,
      structurally adjacent to DIB — but is NOT a fresh ITW event or
      fresh attribution; the underlying CVE + active-exploitation
      claim are the same as the 2026-05-07 FLASH. Trigger 1 FAILS on
      topic-already-FLASH'd anti-noise. RAW-SIGNALED to grader queue
      as a morning-brief UPDATE candidate (NOT FLASH).

      Fortinet FortiAuthenticator CVE-2026-44277 (CVSS 9.1, no ITW
      per Fortinet + SecurityWeek) + FortiSandbox CVE-2026-26083
      (CVSS 9.1, no ITW): both already raw-signaled at PM-002 +
      finding-2026-05-12-0004 yesterday afternoon. SecurityWeek's
      "Fortinet, Ivanti Patch Critical Vulnerabilities" today (09:36
      UTC = 05:36 EDT in-window) confirms the no-ITW conclusion of
      the prior afternoon coverage ("Neither vendor reported active
      wild exploitation; statement: 'not aware of any of the patched
      vulnerabilities being exploited in the wild'"). Trigger 1 FAILS
      on active_exploitation false. Anti-noise rule applies to the
      Fortinet pair (already grader-queue covered at finding-2026-05-
      12-0004); DISCARDED for fresh raw-signal write.

      Ivanti Xtraction CVE-2026-8043 (CVSS 9.6, "external file name
      control → sensitive file read + arbitrary HTML write to web
      directories"; remote-AUTHENTICATED attacker) is NEW today. NOT
      in _index.yaml. Patched at-disclosure (Xtraction 2026.2). NO
      ITW per Ivanti statement. Auth-required attack class. Trigger 1
      FAILS on active_exploitation false; Trigger 6 FAILS on patch-
      available. DISCARDED per Mode 1.

      Intel CVE-2026-20794 (Data Center Graphics Driver for VMware
      ESXi buffer overflow CVSS 9.3, NO ITW) + AMD CVE-2026-0481
      (ROCm Device Metrics Exporter unrestricted IP bind CVSS 9.2,
      NO ITW): both NEW today via Chipmaker Patch Tuesday SecurityWeek
      relay. NEITHER reported as exploited; Trigger 1 FAILS on
      active_exploitation false. Trigger 6 FAILS on patch-available
      (both shipped today). DISCARDED per Mode 1.

  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      SecurityWeek's ICS Patch Tuesday relay characterizes the
      Ruggedcom APE1808 + PAN-OS exploitation attribution as
      "possibly by Chinese state-sponsored hackers" — SPECULATIVE,
      no specific actor named (no Volt Typhoon / Salt Typhoon /
      APT40 / APT41 attribution). Trigger 2 requires the attributed
      actor be in the tracked roster AND the attribution be new (not
      re-reporting prior); the China-link language here is
      speculative-only and does not match a tracked roster actor
      with specificity. Trigger 2 FAILS on both new_attribution and
      tracked_actor_involved.

      GemStuffer (Socket research, RubyGems UK Council portal data
      exfil) is explicitly UNATTRIBUTED per Socket. Trigger 2 FAILS
      on tracked_actor_involved.

      RubyGems suspension event (~500 malicious packages targeting
      RubyGems itself, not end-users) per SecurityWeek 2026-05-13
      07:30 UTC publication = anti-noise to yesterday's PM coverage;
      Socket said "not clear if related" to the separate GemStuffer
      campaign; NO specific threat-actor attribution offered.
      Trigger 2 FAILS on tracked_actor_involved.

  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party telemetry across both indexes (archimedes +
      defenseclaw_local) returned 0 non-archimedes-internal events
      over 24h. Targeted IOC keyword sweep across 25 high-priority
      tokens (CVE-2026-0300, CVE-2026-44277, CVE-2026-26083,
      CVE-2026-8043, CVE-2026-45185, Ruggedcom, "PAN-OS", "Captive
      Portal", FortiSandbox, FortiAuthenticator, Xtraction,
      GemStuffer, RubyGems, "Mini Shai-Hulud", TeamPCP, UNC1549,
      APT28, APT29, "Volt Typhoon", "Salt Typhoon", "Charming
      Kitten", MuddyWater, APT37, APT40, APT41, Lazarus) over 24h
      returned 11 hits — ALL eleven are archimedes:operation
      pipeline self-references from 2026-05-12 brief cycles +
      2026-05-13 00:00 FLASH sentinel commit (splunk_log.py
      emissions). Pipeline self-references match keyword tokens in
      JSON payloads but reflect Archimedes' own operational logging,
      NOT external observations. Trigger 3 FAILS on splunk_match +
      ioc_tracked. TWENTIETH consecutive sweep with dormant non-
      archimedes-internal stream pattern across both indexes.

  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      Zero tracked-actor TTP change documented in any in-window item.
      Siemens Ruggedcom APE1808 disclosure is a customer-base
      affected-surface disclosure (Siemens informing customers their
      OT-deployed PAN-OS instances on Ruggedcom hardware are within
      the CVE-2026-0300 attack surface), NOT an adversary-tradecraft
      observation. The China-link language is speculative-attribution
      not TTP-class. Trigger 4 FAILS on attributable + ttp_delta.

  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      Zero active multi-victim A&D-sector campaign disclosed in any
      in-window item.

      The Siemens Ruggedcom APE1808 + PAN-OS expanded-surface
      disclosure is structurally A&D-adjacent (Ruggedcom APE1808 is
      a ruggedized application platform deployed in substations,
      transportation infrastructure, industrial control system
      networks — overlap with the defense industrial base via
      energy + transportation + critical-manufacturing supply chain),
      but the sector classification per prior CISA APE1808 advisory
      (ICSA-26-071-02) is explicitly "Critical Manufacturing, Energy,
      Transportation Systems" — NOT A&D-prime / DIB-prime / aerospace
      / defense. NO A&D prime named as a target. Multi-victim aspect
      is implied at sector level but no specific victim breakdown
      provided this sweep. Trigger 5 FAILS on A&D-sector-explicit-
      targeting; flagged for morning-brief orchestrator awareness as
      ICS-sector-adjacent intel.

      GemStuffer campaign = UK local-government democratic-services
      portal scraping; NOT A&D. FAIL.

      RubyGems suspension event = targeting RubyGems infrastructure
      itself (XSS + data-exfiltration attempts per SecurityWeek);
      NOT A&D. FAIL.

      Fortinet + Ivanti Patch Tuesday cohort: no campaign claim,
      no victims (no ITW). FAIL.

      Chipmaker Patch Tuesday (Intel + AMD): no campaign, no victims
      (no ITW). FAIL.

  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      ALL in-window CVEs ARE PATCHED at-disclosure or pre-disclosure.

      CVE-2026-0300 PAN-OS: Palo Alto patches forthcoming starting
      TODAY May 13 2026 per Palo Alto advisory; KEV deadline 2026-05-
      09 EOB has passed. Patches now beginning to roll out. FAIL on
      patch-available.

      Fortinet FortiAuthenticator CVE-2026-44277 + FortiSandbox CVE-
      2026-26083: patches available at-disclosure
      (FortiAuthenticator 6.5.7/6.6.9/8.0.3; FortiSandbox 5.0.2/
      4.4.9). FAIL on patch-available.

      Ivanti Xtraction CVE-2026-8043: patched at-disclosure
      (Xtraction 2026.2). FAIL on patch-available.

      Intel CVE-2026-20794 + AMD CVE-2026-0481: patched at-disclosure
      via May Chipmaker Patch Tuesday. FAIL on patch-available.

critical_override_evaluated:
  cvss_10: false                          # CVE-2026-0300 9.3 (CVSS v4.0); CVE-2026-44277/26083 9.1 each; CVE-2026-8043 9.6; CVE-2026-20794 9.3; CVE-2026-0481 9.2 — NONE at the CVSS-10.0 hard floor required by critical-override condition #1
  active_exploitation: partial            # CVE-2026-0300 IS actively exploited (Palo Alto "limited exploitation" + KEV-listed) but the CVSS-10 condition independently fails; for the new in-window CVEs (Fortinet pair, Ivanti Xtraction, Intel/AMD), no active exploitation reported
  tracked_actor: false                    # SecurityWeek "possibly by Chinese state-sponsored hackers" is speculative, no specific roster actor named
  ad_watchlist_hit: false                 # no A&D prime named in any in-window item (Ruggedcom APE1808 sectors are Critical Manufacturing / Energy / Transportation per prior CISA listing, A&D-adjacent but not A&D-named)
  conditions_met: 0_of_4                  # CVSS-10 floor fails as the gating condition; even with partial active_exploitation on CVE-2026-0300, the other three conditions also fail
  bypass_quiet_hours: false
  outcome: not_applicable                  # quiet-hours active (06:00 EDT inside 21:00-09:00 EDT window) AND critical-override fails on CVSS-10 floor

iocs_extracted: false                      # this is the sentinel sweep file; no per-item raw-signal written this sweep
iocs_count: 0
text_word_count: 0                         # sentinel sweep frontmatter-only
promoted: false
sentinel_disposition: audit_trail_only_no_flash_candidate
ttl_expires_at: 2026-08-11T06:05:00-04:00  # 90 days per LEGAL-POLICY retention
---

# Sentinel — 2026-05-13 06:00 EDT FLASH alert sweep

FLASH alert sweep for the 6h window 2026-05-13T00:00 → 06:00 EDT.
Quiet hours active (06:00 EDT inside 21:00-09:00 EDT window per
`infrastructure/flash-policy.yaml`). Outcome: CLEAN — zero FLASH
triggers matched across the six trigger definitions; no FLASH
candidates surfaced; zero raw-signal items beyond this sentinel
written.

## What the sweep found

Six in-window items surveyed, ALL DISCARDED at Mode 1 or anti-noise:

1. **SecurityWeek — "Fortinet, Ivanti Patch Critical Vulnerabilities"**
   (Ionut Arghire, 05:36 EDT in-window). Fortinet FortiAuthenticator
   CVE-2026-44277 (CVSS 9.1, unauthenticated RCE) + FortiSandbox
   CVE-2026-26083 (CVSS 9.1, unauthenticated RCE) — both ALREADY raw-
   signaled yesterday afternoon at PM-002 + grader-queue-covered at
   finding-2026-05-12-0004. Today's SecurityWeek relay confirms
   "Neither vendor reported active wild exploitation" — the same
   conclusion as yesterday's coverage. Ivanti Xtraction CVE-2026-8043
   (CVSS 9.6, authenticated file-read + HTML-write) is NEW today but
   patched at-disclosure (Xtraction 2026.2) with NO ITW per Ivanti.
   ANTI-NOISE for the Fortinet pair (anti-noise to finding-2026-05-12-
   0004); Ivanti Xtraction DISCARDED per Mode 1 (no ITW, no actor,
   patched-at-disclosure, not in _index.yaml).

2. **SecurityWeek — "Chipmaker Patch Tuesday: Intel and AMD Patch
   70 Vulnerabilities"** (Ionut Arghire, 04:37 EDT in-window). Intel
   CVE-2026-20794 (Data Center Graphics Driver for VMware ESXi buffer
   overflow CVSS 9.3) + AMD CVE-2026-0481 (ROCm Device Metrics
   Exporter unrestricted IP bind CVSS 9.2). NEITHER reported as
   exploited; both patched at-disclosure via May Chipmaker Patch
   Tuesday cohort. DISCARDED per Mode 1.

3. **SecurityWeek — "Hundreds of Malicious Packages Force RubyGems
   to Suspend Registrations"** (Eduard Kovacs, 03:30 EDT in-window).
   ~500 malicious packages pushed targeting RubyGems infrastructure
   itself rather than end-users (XSS + data-exfiltration attempts);
   RubyGems suspended new account registrations + planned enhanced
   rate-limiting + WAF protection. NO threat-actor attribution. NO
   relationship to Mini Shai-Hulud explicitly claimed. NO A&D /
   roster / vuln-index hit. DISCARDED per Mode 1.

4. **SecurityWeek — "ICS Patch Tuesday: New Security Advisories
   From Siemens, Schneider, CISA"** (Eduard Kovacs, 02:50 EDT
   in-window). 18 Siemens advisories + 4 Schneider Electric + CISA
   for ABB / Subnet Solutions / Fuji Electric / Maxhub / Johnson
   Controls + CERT@VDE 1 (VDE-2026-042 Codesys Modbus DoS). Notable
   in-window disclosure: **Siemens informed customers that its
   Ruggedcom APE1808 product is affected by the recently disclosed
   Palo Alto Networks PAN-OS vulnerability that has been exploited
   in the wild, possibly by Chinese state-sponsored hackers**. This
   refers to CVE-2026-0300 (PAN-OS Captive Portal unauthenticated
   buffer overflow → root RCE; CVSS v4.0 9.3; KEV-added 2026-05-06;
   already FLASH'd at 2026-05-07T11:32 EDT per threats/briefs/2026-
   05-07-flash-0000-pan-os-cl-sta-1132.md and tracked via threats/
   vulnerabilities/PAN-OS-CVE-2026-0300/). Ruggedcom APE1808 is a
   ruggedized application platform deployed in substations,
   transportation infrastructure, industrial control system
   networks per prior CISA APE1808 advisory sector listing
   (Critical Manufacturing / Energy / Transportation). The
   expanded-surface disclosure is meaningful UPDATE intel
   structurally adjacent to DIB but NOT a fresh FLASH:
   - **anti-noise rule applies** (one FLASH per topic per 24h —
     CVE-2026-0300 topic was FLASH'd 2026-05-07);
   - **no A&D-prime named** (Ruggedcom sectors are A&D-adjacent
     not A&D-prime);
   - **no specific tracked-actor attribution** (SecurityWeek
     language "possibly by Chinese state-sponsored hackers" is
     speculative, no Volt Typhoon / Salt Typhoon / APT40 / APT41
     specificity).
   **Flagged for 2026-05-13 morning-brief orchestrator awareness as
   PAN-OS CVE-2026-0300 expanded-surface UPDATE**, NOT raw-signaled
   at FLASH severity.

5. **SANS-ISC — Guest Diary student fraud-site analysis** (Joshua
   Nikolson SANS.edu BACS intern, 02:29 EDT in-window). Defensive
   / educational content. NO threat actor / NO fresh CVE / NO
   IOCs / NO A&D. DISCARDED per Mode 1.

6. **Hacker News — "GemStuffer Abuses 150+ RubyGems to Exfiltrate
   Scraped U.K. Council Portal Data"** (Socket researchers, 2026-
   05-13-dated). UK local-government democratic-services portal
   scraping (Lambeth / Wandsworth / Southwark ModernGov) using
   RubyGems as a covert storage layer for scraped agenda PDFs +
   officer-contact + RSS-feed content. Socket explicitly UNATTRIBUTED
   and said "not clear if related" to the separate RubyGems
   suspension event yesterday. NO A&D / NO roster actor / NO CVE /
   NO tracked-vuln hit. DISCARDED per Mode 1. (Also noted: Hacker
   News "Android Adds Intrusion Logging for Sophisticated Spyware
   Forensics" — Google + Amnesty + RWB defensive-tooling
   collaboration; awareness-relevant, NO threat-intel, DISCARDED.)

## Anti-noise applied this sweep

- **CVE-2026-0300 PAN-OS Captive Portal active exploitation** —
  topic-level coverage saturation. Already FLASH'd 2026-05-07T11:32
  EDT (`2026-05-07-flash-0000-pan-os-cl-sta-1132.md`); has dedicated
  vulnerability-tracking dossier; appears in 9 findings and 10
  briefs to date. Today's Ruggedcom APE1808 affected-surface
  disclosure is UPDATE-flag intel for morning-brief composition,
  NOT a fresh FLASH (24h anti-noise lock from 2026-05-07 long since
  expired but topic-saturation applies regardless of the formal
  24h window).
- **Fortinet FortiAuthenticator CVE-2026-44277 + FortiSandbox
  CVE-2026-26083** — already raw-signaled at PM-002 yesterday +
  covered in finding-2026-05-12-0004; today's SecurityWeek relay
  confirms (does not change) the no-ITW conclusion.
- **Microsoft + SAP + Siemens May Patch Tuesday cohort** — covered
  in 2026-05-12 morning + afternoon briefs (finding-2026-05-12-
  0001 SAP+Siemens, finding-2026-05-12-0003 Microsoft, finding-
  2026-05-12-0004 Fortinet, finding-2026-05-12-0006 CISA ICS
  batch). Chipmaker Patch Tuesday (Intel/AMD) extends the cohort
  to chip-vendor scope without changing the no-ITW conclusion.
- **Mini Shai-Hulud npm + PyPI worm topic** (CVE-2026-45321 /
  TeamPCP) — 24h anti-noise lock from 2026-05-12 06:00 FLASH
  EXPIRED at 2026-05-13T06:30 EDT (i.e., ~30 min after this sweep
  closes). No surface items in this sweep referenced the worm
  topic, so no deduplication required at this sweep.
- **MSTIC MDASH agentic vuln-discovery disclosure** + AI-synthetic-
  logs research — flagged at 2026-05-13 00:00 sentinel for
  morning-brief orchestrator awareness; carry-forward state
  unchanged this sweep (no fresh in-window MSTIC content).

## Source-health updates this sweep

See `sources_health_changed_this_sweep` block in frontmatter.
Notable:

- `mandiant` — feedburner 404 20th consecutive sweep; failure_count
  18 → 19 (held healthy pending operator alt-endpoint decision).
- `dragos` — failure_count 1 → 2 (second consecutive 404 on dragos
  .com/blog/feed/). NOW AT stale-flip threshold per >=2-failure
  rule. Held healthy this sweep pending operator-side working RSS
  path identification (Dragos cadence is multi-day, CISA ICS batch
  + SecurityWeek ICS Patch Tuesday relay cover the OT surface
  adequately for this 6h window); next-sweep failure WILL trip
  stale per rule unless operator surfaces a working endpoint.
- `crowdstrike` — feedburner.com/crowdstrike returned 404 this
  sweep. FIRST observed 404 on this endpoint after 19+ consecutive
  sweeps of dateless-marketing valid-RSS responses. failure_count
  0 → 1. Different failure mode than the prior dateless-marketing
  pattern; possibly transient feedburner-side issue, possibly
  the feedburner CrowdStrike feed is shutting down (Mandiant
  feedburner has been dead for 20+ sweeps — second-vendor
  feedburner reliance is now a structural concern).
- `wiz-research` — wiz.io/blog/rss.xml 404. FIRST attempt at the
  wiz blog RSS endpoint via fetch_feed. New source-health entry.
  Operator action: identify working wiz.io RSS path or accept
  WebFetch on blog index page as productive endpoint.
- `securityweek` — last_successful_fetch 2026-05-12T06:00 →
  2026-05-13T06:00; 4 in-window items returned. First productive
  sweep for this source after 5 consecutive 0-item sweeps; surfaced
  the Siemens Ruggedcom APE1808 + CVE-2026-0300 expanded-surface
  disclosure (flagged for 2026-05-13 morning-brief awareness as
  UPDATE flag, NOT FLASH).
- `sans-isc` — last_successful_fetch 2026-05-13T00:00 → 2026-05-
  13T06:00; 1 in-window item DISCARDED per Mode 1.
- `bleepingcomputer` + `mstic` + `unit42` + `rapid7` + others —
  last_successful_fetch updated; failure_count remains 0.

## Flagged for orchestrator awareness (2026-05-13 morning candidates)

- **Siemens Ruggedcom APE1808 + PAN-OS CVE-2026-0300 expanded-
  surface disclosure** (SecurityWeek ICS Patch Tuesday relay
  06:50 UTC = 02:50 EDT in-window). NEW in-window UPDATE flag on
  the already-FLASH'd 2026-05-07 CVE-2026-0300 topic — Ruggedcom
  APE1808 deployed in substations / transportation / ICS networks
  per prior CISA APE1808 advisory; structurally adjacent to DIB
  via Critical Manufacturing + Energy + Transportation sector
  overlap. SecurityWeek language "possibly by Chinese state-
  sponsored hackers" is speculative-only — no tracked-roster
  actor named with specificity. PAN-OS patches now beginning to
  roll out today per Palo Alto advisory cadence. Worth morning-
  brief UPDATE-section coverage as expanded-attack-surface intel
  for the existing CVE-2026-0300 vulnerability-tracking dossier.

- **Chipmaker Patch Tuesday: Intel + AMD 70 CVEs no-ITW**
  (SecurityWeek 08:37 UTC = 04:37 EDT in-window). Extends the
  May 2026 Patch Tuesday cohort coverage to chip-vendor scope.
  Notable: Intel CVE-2026-20794 (Data Center Graphics Driver
  buffer overflow CVSS 9.3) is a SERVER-vendor Critical CVE
  with VMware ESXi exposure. NO ITW. Worth morning-brief
  awareness as Patch Tuesday cohort extension; not a fresh
  finding.

- **Ivanti Xtraction CVE-2026-8043** (CVSS 9.6, authenticated
  external-filename-control → sensitive-file-read + arbitrary-
  HTML-write to web directories; NEW today; patched at-
  disclosure; NO ITW per Ivanti). Worth morning-brief patch-
  backlog tier awareness.

- **MSTIC MDASH agentic vuln-discovery + CVE-2026-33827/33824
  capability disclosure** — carry-forward from 2026-05-13
  00:00 sentinel.

- **RubyGems suspension + GemStuffer parallel campaigns** — no
  tracked-actor attribution and no A&D nexus, but the RubyGems
  ecosystem-stress is pattern-adjacent to the Mini Shai-Hulud
  npm + PyPI worm carrying TeamPCP attribution (different
  ecosystem, different operator-coined working name, no
  explicit lineage claim from Socket).

- **UNC6692 + UNC1069** remain Mandiant-blog top-of-list visible
  titles but NOT in `_roster.yaml` — operator `/new-actor`
  candidates pending decision (unchanged from prior sweeps).

## What did NOT change this sweep

- Splunk first-party non-archimedes-internal stream: 0 events
  6h + 24h (twentieth consecutive dormant sweep across both
  indexes).
- KEV catalog: 0 entries dateAdded ≥ 2026-05-12 (full-catalog
  scan corroborates the day's KEV-quiet pattern; CVE-2024-1708
  ConnectWise + CVE-2026-32202 Microsoft both dueDate 2026-05-12
  EOB passed without compliance-status update; standard KEV
  pattern).
- Mandiant feedburner: 20th consecutive 404.
- x-cisagov + x-gossithedog + ars-security: stale-held per prior
  source-health entries.

---

## Extraction notes

- Sentinel file — per FLASH-POLICY clean-sweep convention, this
  raw-signal carries the sweep audit trail in lieu of per-item
  files (since no per-item raw-signals were warranted this sweep).
- Pre-flight LEGAL-POLICY check: passive RSS/web fetches + own-
  index Splunk reads only; `authorized_for_active_recon` remains
  empty; no prohibited query patterns triggered; no credentials
  surfaced this sweep.
- Anti-noise enforced per FLASH-POLICY §one-flash-per-topic-per-
  24h (CVE-2026-0300 topic saturation, Fortinet PSIRT pair anti-
  noise to finding-2026-05-12-0004, Microsoft + SAP + Siemens
  Patch Tuesday cohort brief-covered).
- No raw-signal items marked `test: true` filtered from sweep
  (none observed in current `threats/raw-signal/` directory).
- Quiet hours active (06:00 EDT inside 21:00-09:00 EDT) — moot
  anyway since 0 FLASH triggers matched and critical-override
  failed on CVSS-10 hard floor.

## IOCs (sentinel level)

This sentinel file carries no body-level IOC extraction (zero
per-item raw-signals this sweep). The Splunk first-party sweep
queried but did not match any of the following indicator set:

```yaml
splunk_queried_iocs_no_match:
  in_window_cves:
    - CVE-2026-0300        # PAN-OS Captive Portal active exploitation (already FLASH'd 2026-05-07)
    - CVE-2026-44277       # Fortinet FortiAuthenticator (already PM-002 + finding-0004)
    - CVE-2026-26083       # Fortinet FortiSandbox (already PM-002 + finding-0004)
    - CVE-2026-8043        # Ivanti Xtraction (NEW today, NO ITW, patched)
    - CVE-2026-20794       # Intel Data Center Graphics Driver (NEW, NO ITW)
    - CVE-2026-0481        # AMD ROCm Device Metrics Exporter (NEW, NO ITW)
    - CVE-2026-45185       # Exim BDAT GnuTLS (yesterday, anti-noise)
  in_window_actors_speculative_only:
    - "Chinese state-sponsored hackers"   # SecurityWeek speculative attribution on Ruggedcom + PAN-OS, no roster specificity
  in_window_topics_no_attribution:
    - GemStuffer                          # Socket research, UK Council, no actor attribution
    - RubyGems_suspension_attackers       # No actor attribution per SecurityWeek
  in_window_expanded_surfaces:
    - Ruggedcom_APE1808                   # Siemens disclosure: affected by CVE-2026-0300
  tracked_roster_actors_queried:
    - TeamPCP
    - UNC1549
    - APT28
    - APT29
    - "Volt Typhoon"
    - "Salt Typhoon"
    - "Charming Kitten"
    - MuddyWater
    - APT37
    - APT40
    - APT41
    - Lazarus
```

Zero non-pipeline-self-reference matches across all of these
against `archimedes` and `defenseclaw_local` indexes over `-24h@h`
window.
