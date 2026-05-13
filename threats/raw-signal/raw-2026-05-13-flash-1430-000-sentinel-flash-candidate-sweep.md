---
raw_id: raw-2026-05-13-flash-1430-000
collected_at: 2026-05-13T14:35:00-04:00
run_id: flash-sweep-20260513-143000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-13T14:30:00-04:00
time_window_start: 2026-05-13T06:00:00-04:00
time_window_end: 2026-05-13T14:30:00-04:00
test: false
quiet_hours_active: false                  # 14:30 EDT inside 09:00-21:00 EDT active window
sources_queried:
  - bleepingcomputer       # RSS via fetch_feed — status 200, 6 items in 8.5h window. ALL DISCARDED at Mode 1 or anti-noise: Microsoft BitLocker recovery fix (Windows-product engineering, no threat-intel), Microsoft Autopatch driver bug fix (same), Microsoft Office Windows 365 install issue (same), Picus Security sponsored content (filtered), webinar promo (filtered). Foxconn / Nitrogen ransomware confirmation (12:49 UTC = 08:49 EDT in-window) — ALREADY COVERED in 2026-05-13 morning brief (finding-2026-05-13-0002); anti-noise applies. The BleepingComputer relay corroborates the Foxconn statement already in the morning brief's coverage of the Wired primary; no new information.
  - securityweek           # RSS via fetch_feed — status 200, 5 items in 8.5h window. ALL DISCARDED at anti-noise or Mode 1: CVE-2026-40361 Outlook zero-click critical (10:33 UTC = 06:33 EDT in-window) — this IS the SecurityWeek originating article that the 2026-05-13 morning brief's finding-2026-05-13-0001 reframed CVE-2026-40361 from; anti-noise applies (already FLASH-eligible content was absorbed into the morning brief at WEP "likely" per anti-noise §B2-minimum-grade). OpenLoop Health breach (716k impacted) — healthcare data breach, NO A&D, NO actor, NO CVE, DISCARDED per Mode 1. Instructure / Canvas government scrutiny (12:13 UTC) — government follow-up on prior breach (covered 2026-05-08 → 2026-05-09 corpus); no fresh threat-intel; DISCARDED. Sweet Security agentic AI red teaming product launch + ROI webinar — marketing/product content; DISCARDED per Mode 1.
  - the-record             # RSS via fetch_feed — status 200, 2 items in 8.5h window. Microsoft 2026 vulnerability record + MDASH AI patch wave (12:54 UTC = 08:54 EDT in-window) — references CVE-2026-41089 Netlogon 9.8 + CVE-2026-41096 DNS 9.8 + CVE-2026-42898 Dynamics 365 9.9 (May 2026 Patch Tuesday cohort already covered in 2026-05-12 afternoon finding-2026-05-12-0003 + MSTIC MDASH already flagged at 2026-05-13 00:00 sentinel for morning-brief orchestrator awareness); anti-noise applies. UK Computer Misuse Act security-researcher shield reform (12:58 UTC) — UK policy / legislation; NO threat-intel; DISCARDED per Mode 1.
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-13T10:43:26 GMT (in-window from feed-server activity), 0 items in 8.5h window. Normal Krebs cadence; no fresh content.
  - sans-isc               # RSS via fetch_feed (rssfeed.xml) — status 200, etag W/1fc0-651b50f28cfac, last_modified 2026-05-13T15:59:05 GMT (11:59 EDT in-window from feed-server activity), 0 items in 8.5h window (since-filter: most recent in-window content from earlier 00:00 + 06:00 sweeps already evaluated).
  - cisa-advisories        # all.xml RSS via fetch_feed — status 200, 30 items in feed total, 0 items in 8.5h window. CISA ICS Patch Tuesday batch propagation expected via cisa.gov/news-events/cybersecurity-advisories landing later today but not yet in all.xml feed.
  - cisa-kev               # JSON catalog via WebFetch — top 5 most recent entries returned. ZERO entries dateAdded >= 2026-05-13. Most recent KEV addition remains CVE-2026-42208 (BerriAI LiteLLM, dateAdded 2026-05-08). KEV-quiet pattern continues into mid-day 2026-05-13.
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, etag "34e1865375dd494f6ac6bbc5a8f31b9a-gzip", last_modified 2026-05-12T23:45:12 GMT pre-window unchanged from 00:00 + 06:00 sweeps, 0 items in 8.5h window.
  - unit42                 # RSS (feedburner) via fetch_feed — status 200, last_modified 2026-05-13T14:59:37 GMT (10:59 EDT in-window from feed-server activity), 0 items in 8.5h window. Unit42 feedburner reachable + stable; no fresh content.
  - rapid7                 # RSS via fetch_feed (rapid7.com/blog/rss/) — status 200, last_modified 2026-05-13T15:46:43 GMT (11:46 EDT in-window from feed-server activity), 1 item in 8.5h window — "Rapid7 Partner Academy: Driving Impact with Gold Stevie Award-Winning Partner Services Certifications" (Rapid7 byline, 13:54 UTC = 09:54 EDT in-window). Marketing / partner-services content; NO threat-intel; NO actor; NO CVE; NO IOCs. DISCARDED per Mode 1.
  - sentinelone-labs       # RSS via fetch_feed (sentinelone.com/labs/feed/) — status 200, etag W/d7c6c58e49999eefd3a59e6178947d96, last_modified 2026-05-13T13:00:41 GMT (09:00 EDT in-window from feed-server activity), 0 items in 8.5h window.
  - sophos                 # RSS via fetch_feed (news.sophos.com/feed/) — status 200, 9 items total in feed, 0 items in 8.5h window. Normal cadence.
  - eset-welivesecurity    # RSS via fetch_feed — status 200, 100 items total in feed, 0 items in 8.5h window.
  - arstechnica-root       # RSS via fetch_feed (arstechnica.com/feed/) — status 200, last_modified 2026-05-13T16:00:58 GMT, 5 items in 8.5h window — all non-security (astronomy gravitational lens, Blue Origin funding, Daredevil S2 TV review, Rivian AI assistant, space-pharma drug manufacturing). NO security desk content. NO threat-intel / NO A&D / NO actor / NO CVE. ALL DISCARDED per Mode 1. (ars-security feeds.arstechnica.com/arstechnica/security stale since 2026-05-09 per source-health.yaml; root-feed workaround in use this sweep.)
  - hacker-news            # WebFetch on thehackernews.com/ index — top 10 visible titles. ONE FLASH-CANDIDATE-PRODUCTIVE article: "Azerbaijani Energy Firm Hit by Repeated Microsoft Exchange Exploitation" (Ravie Lakshmanan, 2026-05-13-dated) — Bitdefender attributes multi-wave intrusion to FamousSparrow (Salt Typhoon alias per _roster.yaml line 160). Full retrieval via Bitdefender originating URL (businessinsights.bitdefender.com/famoussparrow-apt-targets-azerbaijani-oil-gas-industry); cross-corroboration via Dark Reading title surface (article body returned 403). RAW-SIGNALED at raw-2026-05-13-flash-1430-001 as FLASH candidate matching Trigger 2 (tracked-actor-attribution) cleanly + Trigger 4 (tracked-actor-ttp-change) on multiple tradecraft observations. Other top-10 items: MDASH AI vuln-discovery + Microsoft Patch Tuesday 138 CVEs + GemStuffer RubyGems + Android intrusion logging — all anti-noise or DISCARDED per Mode 1 (covered yesterday or no A&D / actor / CVE hit).
  - cloud-google-blog-mandiant  # WebFetch on cloud.google.com/blog/topics/threat-intelligence top page — top-5 visible titles unchanged from 2026-05-13 06:00 + 2026-05-12 afternoon sweeps (GTIG AI Threat Tracker, UNC6692 Snow Flurries, deSouza AI vuln post, German Cyber Überfall, BRICKSTORM Defender's Guide). NO fresh GTIG content this 8.5h window. Mandiant feedburner endpoint /Mandiant continues 404 (TWENTY-FIRST consecutive); failure_count 19 → 20.
  - wiz-research           # WebFetch on wiz.io/blog — top-5 most recent post titles surfaced. Two items in extended-window relevance: (1) "Fragnesia: Linux Kernel Local Privilege Escalation via ESP-in-TCP" (Merav Bar + Rami McCarthy, 2026-05-13 publication date in-window). (2) "Mini Shai-Hulud Strikes Again: TanStack + more npm Packages Compromised" (2026-05-12, pre-window expansion of prior FLASH; anti-noise applies). FRAGNESIA evaluated separately below — Trigger 6 candidate (Linux kernel zero-day, unpatched at disclosure, public PoC via V12 security GitHub) but FAILS on "exploitation_imminent per A-grade source" — Wiz disclosure does NOT make an imminent-exploitation claim; no ITW observed; positive PoC-available alone is not the doctrine threshold. RAW-SIGNALED awareness item: Linux kernel LPE in Dirty Frag family family lineage, CVE not yet assigned, unpatched in mainline at disclosure, PoC published. NOT raw-signaled at FLASH severity — flagged for orchestrator awareness for afternoon brief Vulnerabilities section coverage.
  - snyk                   # WebFetch on snyk.io/blog — top-5 most recent posts. (1) TanStack Mini Shai-Hulud expansion (2026-05-11) — anti-noise to 2026-05-12 FLASH-0001. (2) Lightning PyPI Compromise (2026-04-30) — out-of-window. NO 2026-05-13-dated content. NO FLASH candidate.
  - splunk-archimedes      # search index=archimedes OR index=defenseclaw_local ("Salt Typhoon" OR FamousSparrow OR "Earth Estries" OR GhostEmperor OR UNC2286 OR "UAT-9244" OR "Deed RAT" OR Snappybee OR TernDoor OR "Mofu Loader" OR virusblocker.it.com OR sentinelonepro.com) NOT sourcetype=archimedes:* over -30d returned ZERO events. ALSO searched ProxyShell + ProxyNotShell + Exchange CVE chain over -30d → ZERO events. Salt Typhoon first-party telemetry CLEAN over 30d. TWENTY-FIRST consecutive sweep with dormant non-archimedes-internal stream pattern across both indexes.
  - splunk-defenseclaw     # NOT sourcetype=archimedes:* over 24h returns zero events. Twenty-first consecutive sweep dormant.
  - virustotal-c2-domains  # mcp__virustotal__lookup_domain on the two FamousSparrow C2 domains: virusblocker[.]it[.]com (2/92 malicious, ADMINUSLabs + Kaspersky detections, registrar Intis Telecom Limited, creation 1992-10-23 / last-update 2025-12-02 = Wave-1-onset alignment); sentinelonepro[.]com (2/92 malicious, same detection engines, creation 2026-02-26 = Wave-3-onset alignment, brand-impersonation infrastructure). Both VT-confirm Bitdefender's malicious-classification. Recorded in raw-2026-05-13-flash-1430-001 IOC block.
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH — ~73h since stale-flip; FLASH-fast scope kept to RSS / vendor / KEV / Splunk priority feeds.
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted.
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround in use this sweep (arstechnica.com/feed/ root path; 5 in-window items all non-security DISCARDED).
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation); awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom; per-repo GHSA fallback path remains productive workaround when triggered (not triggered this sweep)
  - proofpoint             # /us/threat-insight/blog/feed endpoint 404 since 2026-05-10 12:00 FLASH; alt /us/rss.xml corporate-news endpoint multi-day cadence; not invoked this sweep
  - iran-monitor           # iranmonitor.org 403 WAF/UA workaround pending
  - dragos                 # dragos.com/feed/ + /blog/feed/ both 404 this sweep — consistent with 2026-05-13 00:00 + 06:00 FLASH failures. failure_count now 3 cumulative (00:00 → 06:00 → 14:30). PER >=2-failure rule, this source should FLIP TO STALE. Marking stale this sweep (operator-side working RSS path identification still pending; held healthy through 00:00 + 06:00 sweeps as soft-fail with multi-day Dragos cadence justification — third consecutive failure triggers the stale flip).
  - crowdstrike            # feedburner.com/crowdstrike returned 404 on 2026-05-13 06:00 FLASH (first 404); NOT re-tested this sweep (FLASH-fast scope). failure_count remains 1; held healthy pending next-sweep retry per source-health doctrine.
  - wiz-research-rss       # wiz.io/blog/rss.xml 404; this sweep used WebFetch on the blog index page instead (productive — surfaced both Fragnesia + TanStack-expansion posts). RSS path still 404; operator action pending or WebFetch acceptance.
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (TWENTY-FIRST consecutive); failure_count 19→20. cloud.google.com index page WebFetch surfaced same top-5 visible titles as 2026-05-13 06:00 + 2026-05-12 afternoon sweeps (all out-of-window per prior triangulations). Held healthy pending operator alt-endpoint decision.
  - securityweek           # last_successful_fetch 2026-05-13T06:00 → 2026-05-13T14:30; 5 in-window items returned, ALL DISCARDED per analysis above. Productive second consecutive sweep for this source.
  - bleepingcomputer       # last_successful_fetch 2026-05-13T06:00 → 2026-05-13T14:30; 6 in-window items, all DISCARDED or anti-noise.
  - the-record             # last_successful_fetch 2026-05-12T06:00 → 2026-05-13T14:30; 2 in-window items DISCARDED. First productive sweep for this source after 5 consecutive 0-item sweeps.
  - rapid7                 # last_successful_fetch 2026-05-12T06:00 → 2026-05-13T14:30; 1 in-window item DISCARDED (marketing).
  - sentinelone-labs       # last_successful_fetch updated; 0 in-window items.
  - dragos                 # failure_count 2→3 (third consecutive 404 across 00:00 + 06:00 + 14:30 sweeps). STALE FLIP this sweep per >=2-failure rule (held one extra sweep at 06:00 to allow operator decision; now operationally stale).
  - mstic + sophos + unit42 + krebs + sans-isc + cisa-advisories + cisa-kev + eset-welivesecurity   # last_successful_fetch updated; 0 in-window items each.
  - bitdefender            # NEW source-health entry. First Archimedes-corpus citation via raw-2026-05-13-flash-1430-001 (FamousSparrow Azerbaijani oil and gas multi-wave intrusion). Provisional A grade proposed per Tier-1 vendor research precedent. Operator action: add to source-grades.yaml + source-health.yaml entries.
match_reason:
  watchlist: []                            # Zero in-window items matched aerospace-defense.yaml watchlist directly (Azerbaijani oil and gas is energy, not A&D)
  watchlist_match_strength: structural_only
  actors:
    - "Salt Typhoon (FamousSparrow alias match)"   # ONE FLASH-CANDIDATE attribution via Bitdefender (raw-1430-001). HIGH-threat-level roster actor (id 010, China MSS).
  vulnerabilities:
    - CVE-2026-40361                                # Outlook zero-click UAF — already absorbed into 2026-05-13 morning brief finding-2026-05-13-0001; anti-noise applies (single-source veto continued from morning).
    - CVE-2026-41089 / CVE-2026-41096 / CVE-2026-42898   # Microsoft Patch Tuesday Netlogon + DNS + Dynamics 365 critical CVEs — already covered in 2026-05-12 afternoon finding-2026-05-12-0003; anti-noise.
    - CVE-2021-34473 / CVE-2021-34523 / CVE-2021-31207 / CVE-2022-41040 / CVE-2022-41082   # ProxyShell + ProxyNotShell — recycled n-day by FamousSparrow; long-patched. Triggered Trigger 4 (TTP delta) NOT Trigger 1.
  keywords:
    - flash_candidate_bitdefender_famoussparrow_salt_typhoon_azerbaijan_oil_gas_morning_brief_candidate
    - fragnesia_linux_kernel_lpe_wiz_v12_unpatched_pubic_poc_no_itw_orchestrator_awareness_afternoon
    - foxconn_nitrogen_anti_noise_to_finding_2026_05_13_0002
    - mdash_ai_vuln_discovery_anti_noise_to_morning_orchestrator_awareness
    - microsoft_patch_tuesday_138_cves_anti_noise_to_finding_2026_05_12_0003
    - openloop_health_breach_no_ad_no_actor
    - instructure_canvas_gov_scrutiny_carryforward_from_2026_05_09
    - mandiant_feedburner_21st_consecutive_404
    - dragos_feed_third_consecutive_404_stale_flip_this_sweep
    - splunk_dormant_21st_consecutive
    - bitdefender_first_corpus_citation_provisional_a_proposed
triage_tags:
  - sentinel
  - flash_sweep_1430_2026_05_13
  - quiet_hours_inactive
  - one_flash_candidate_matched
  - trigger_2_tracked_actor_attribution_matched
  - trigger_4_tracked_actor_ttp_change_matched
  - critical_override_not_applicable
  - bitdefender_first_corpus_citation
  - fragnesia_wiz_v12_unpatched_linux_kernel_lpe_orchestrator_awareness_not_flash
  - mandiant_feedburner_21st_consecutive_404
  - dragos_feed_stale_flip_third_consecutive_404
  - splunk_dormant_21st_consecutive
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      Zero new critical-CVE-with-active-exploitation observations in
      window. CVE-2026-40361 Outlook UAF (SecurityWeek 06:33 EDT) is
      a fresh Critical CVE but MICROSOFT REPORTS NO IN-THE-WILD
      EXPLOITATION at disclosure; PoC-only (Haifei Li built PoC,
      not working exploit); already absorbed into 2026-05-13 morning
      brief at WEP "likely" with single-source veto applied. Trigger
      1 FAILS on active_exploitation false. The other in-window CVEs
      (Microsoft Patch Tuesday Netlogon / DNS / Dynamics 365, all no-
      ITW) similarly fail. ProxyShell + ProxyNotShell n-day chain
      used by FamousSparrow is actively exploited against the
      Azerbaijani victim BUT the CVEs themselves are 2021/2022 long-
      patched, not fresh; Trigger 1 requires CVE freshness.

  trigger_2_tracked_actor_attribution:
    matched: true
    notes: |
      TRIGGER 2 MATCHES via the Bitdefender FamousSparrow attribution
      to the Azerbaijani oil and gas company multi-wave intrusion.
      FamousSparrow is a listed alias for Salt Typhoon (roster id
      010) per threats/threat-actors/_roster.yaml line 160:
      aliases: [GhostEmperor, FamousSparrow, UNC2286, Earth Estries].
      Zero prior Archimedes-corpus coverage of FamousSparrow or this
      campaign (grep returned zero matches). Bitdefender's moderate-
      to-high confidence attribution language meets the standard.
      Full detail in raw-2026-05-13-flash-1430-001.

  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party telemetry across both indexes returned 0
      non-archimedes-internal events over -30d on the full
      FamousSparrow / Salt Typhoon / Deed RAT / TernDoor / C2 domain
      / n-day CVE chain indicator set. Twenty-first consecutive
      dormant sweep across both indexes.

  trigger_4_tracked_actor_ttp_change:
    matched: true
    notes: |
      TRIGGER 4 ALSO MATCHES via the same Bitdefender disclosure —
      multiple tradecraft delta observations against Salt Typhoon:
      Deed RAT magic value 0xFF66ABCD, Deflate compression, Mofu
      Loader → TernDoor combination, evolved DLL sideloading via
      LogMeIn Hamachi binary chain, new C2 infrastructure (brand-
      impersonation sentinelonepro[.]com registered 2026-02-26
      aligning with Wave 3), three-wave persistence pattern with
      backdoor rotation, TernDoor target-set expansion from South
      American telecom into South Caucasus energy. Full detail in
      raw-2026-05-13-flash-1430-001.

  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      Bitdefender's disclosed victim is an Azerbaijani oil and gas
      company (anonymized, single-victim disclosure). Energy sector,
      NOT aerospace-defense.yaml. NOT a US DIB prime. Trigger 5
      FAILS on ad_sector_targeted AND on multi_victim (single
      victim disclosed today; multi-victim across time is plausible
      per prior FamousSparrow / Salt Typhoon victimology but not in
      today's disclosure).

      Wiz Fragnesia Linux kernel LPE is widely-deployed kernel-
      subsystem class — but not a CAMPAIGN against the A&D sector;
      it's a vulnerability disclosure. Trigger 5 N/A.

  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      Wiz Fragnesia Linux kernel LPE via ESP-in-TCP (Merav Bar +
      Rami McCarthy, 2026-05-13 publication):
        - patch_available: FALSE (unpatched at disclosure; patch
          submitted upstream but not yet shipped per Wiz)
        - cvss_score: not assigned at disclosure
        - wide_deployment: TRUE (Linux kernel XFRM ESP-in-TCP
          subsystem; affects all Linux distros without disabling
          esp4/esp6/rxrpc)
        - exploitation_confirmed: FALSE (no ITW observed per Wiz)
        - exploitation_imminent_per_a_grade: FALSE — Wiz disclosure
          recommends "apply vendor kernel patches as they become
          available" and notes AppArmor partial mitigation; does
          NOT make an "imminent exploitation" claim positively.
          Public PoC on V12 security GitHub lowers exploitation
          barrier but PoC-availability-alone is not the doctrine
          threshold per FLASH-POLICY.md Trigger 6 language.

      Trigger 6 FAILS on exploitation_confirmed_or_imminent. The
      Wiz disclosure is a high-quality vulnerability advisory worth
      morning/afternoon brief Vulnerabilities-section coverage but
      does NOT cross the FLASH severity bar in the strict reading
      of the doctrine. Flagged for orchestrator awareness for
      afternoon-brief composition.

      The Bitdefender disclosure (FamousSparrow Trigger 2 + 4 match)
      uses RECYCLED N-DAY 2021/2022 CVEs (ProxyShell + ProxyNotShell)
      — long-patched, not zero-day. Trigger 6 N/A on that surface.

critical_override_evaluated:
  cvss_10: false                            # Bitdefender disclosure uses n-day chain (max ProxyShell 9.8 NOT 10.0); Fragnesia CVSS not assigned; CVE-2026-40361 Critical but no CVSS published yet at disclosure
  active_exploitation: partial              # Bitdefender disclosure has active exploitation against the Azerbaijani victim but on n-day CVEs; Fragnesia + CVE-2026-40361 PoC-only, no ITW
  tracked_actor: true                       # Salt Typhoon (FamousSparrow alias) IS tracked in roster
  ad_watchlist_hit: false                   # Energy sector ≠ A&D watchlist; Fragnesia vuln disclosure not campaign-specific to any sector
  conditions_met: 1_of_4                    # only tracked_actor positive; CVSS-10 floor + ad_watchlist_hit fail; active_exploitation only partial
  bypass_quiet_hours: false                 # moot — quiet hours inactive anyway (14:30 EDT inside 09:00-21:00 EDT active window)
  outcome: not_applicable                   # FLASH posting permitted in active hours regardless of critical-override status

iocs_extracted: false                       # sentinel sweep frontmatter-only; per-item IOCs are in raw-2026-05-13-flash-1430-001
iocs_count: 0
text_word_count: 0                          # sentinel sweep frontmatter-only
promoted: false
sentinel_disposition: audit_trail_for_flash_candidate_sweep_with_one_candidate_promoted
ttl_expires_at: 2026-08-11T14:35:00-04:00   # 90 days per LEGAL-POLICY retention
---

# Sentinel — 2026-05-13 14:30 EDT FLASH alert sweep (one FLASH candidate)

FLASH alert sweep for the 8.5h window 2026-05-13T06:00 → 14:30 EDT
(extended from the standard 6h FLASH cadence because the human-
operator-issued ad-hoc sweep falls between the scheduled 12:00 and
18:00 FLASH windows; treated as on-demand FLASH-mode invocation).
Quiet hours INACTIVE (14:30 EDT inside 09:00-21:00 EDT active
window per `infrastructure/flash-policy.yaml`).

## Sweep outcome — ONE FLASH candidate

**FLASH candidate:** `raw-2026-05-13-flash-1430-001` —
**Bitdefender attributes Azerbaijani Oil & Gas multi-wave intrusion
to FamousSparrow (Salt Typhoon alias)**.

- Trigger 2 (tracked-actor-attribution) MATCHES cleanly
- Trigger 4 (tracked-actor-ttp-change) MATCHES on multiple
  tradecraft observations
- Critical-override fails on CVSS-10 floor; quiet hours inactive
  anyway

Bitdefender Labs is FIRST corpus citation; provisional A grade
proposed per Tier-1 vendor research precedent (SentinelOne 2026-
05-08, Wiz Research + Snyk 2026-05-12, Sophos / ESET / Dragos
Session 11 ratifications).

## In-window items surveyed (DISCARDED at Mode 1 or anti-noise)

1. **BleepingComputer — Foxconn / Nitrogen ransomware confirmation
   (12:49 UTC = 08:49 EDT in-window).** Already covered in 2026-
   05-13 morning brief finding-2026-05-13-0002. Anti-noise applies.

2. **SecurityWeek — CVE-2026-40361 Outlook zero-click critical
   patch (10:33 UTC = 06:33 EDT in-window).** This IS the
   SecurityWeek originating article that the 2026-05-13 morning
   brief absorbed into finding-2026-05-13-0001 at WEP "likely".
   Anti-noise applies; no fresh information.

3. **SecurityWeek — OpenLoop Health breach (11:18 UTC).** Healthcare
   data breach, NO A&D, NO actor, NO CVE. DISCARDED per Mode 1.

4. **SecurityWeek — Instructure / Canvas government scrutiny
   (12:13 UTC).** Government follow-up on prior breach; no fresh
   threat-intel; DISCARDED per Mode 1.

5. **SecurityWeek — Sweet Security agentic AI red teaming product
   launch + ROI webinar.** Marketing/product content. DISCARDED.

6. **The Record — Microsoft 2026 vulnerability record + MDASH AI
   patch wave (12:54 UTC).** References Patch Tuesday cohort
   already covered in 2026-05-12 afternoon finding-2026-05-12-0003
   + MSTIC MDASH already flagged at 2026-05-13 00:00 sentinel
   for morning-brief orchestrator awareness. Anti-noise applies.

7. **The Record — UK Computer Misuse Act security-researcher
   shield reform (12:58 UTC).** UK policy / legislation; NO
   threat-intel; DISCARDED per Mode 1.

8. **Rapid7 — Partner Academy Gold Stevie Award (13:54 UTC).**
   Marketing / partner-services content. DISCARDED per Mode 1.

9. **Hacker News — MDASH AI vuln-discovery + Microsoft Patch
   Tuesday + GemStuffer RubyGems + Android intrusion logging
   (2026-05-13).** All anti-noise or DISCARDED per Mode 1
   (covered yesterday or no A&D / actor / CVE hit).

10. **Hacker News — "Azerbaijani Energy Firm Hit by Repeated
    Microsoft Exchange Exploitation" (Ravie Lakshmanan, 2026-
    05-13).** → **FLASH CANDIDATE.** Bitdefender originating
    research surfaced via this Hacker News relay; full retrieval
    via businessinsights.bitdefender.com/famoussparrow-apt-targets-
    azerbaijani-oil-gas-industry. RAW-SIGNALED at flash-1430-001.

11. **Wiz Research — "Fragnesia: Linux Kernel LPE via ESP-in-TCP"
    (Merav Bar + Rami McCarthy, 2026-05-13).** New Linux kernel LPE
    in Dirty Frag family lineage. UNPATCHED at disclosure (patch
    submitted upstream); public PoC on V12 security GitHub; NO
    in-the-wild exploitation observed. Trigger 6 FAILS on
    exploitation_confirmed_or_imminent per A-grade source (Wiz
    disclosure recommends future-tense patch deployment, does not
    claim imminent exploitation). High-quality vulnerability
    advisory worth afternoon-brief Vulnerabilities section
    coverage. **NOT raw-signaled at FLASH severity** — flagged for
    orchestrator awareness.

12. **Wiz Research / Snyk — Mini Shai-Hulud TanStack expansion
    (2026-05-11 / 2026-05-12, pre-window).** Anti-noise to
    2026-05-12 FLASH-0001.

13. **Ars Technica root feed — Blue Origin funding + 4 other non-
    security items.** Stale ars-security workaround in use; all
    in-window items non-security. ALL DISCARDED per Mode 1.

14. **SANS-ISC + Krebs + CISA-Advisories + CISA-KEV + MSTIC +
    Unit42 + SentinelOne + Sophos + ESET-WeLiveSecurity.** All
    reachable, zero in-window items.

## Anti-noise applied this sweep

- **CVE-2026-40361 Outlook zero-click UAF** — absorbed into
  2026-05-13 morning brief finding-2026-05-13-0001 at WEP
  "likely" with single-source veto applied; today's SecurityWeek
  originating article IS the morning brief's primary source.
- **Foxconn / Nitrogen ransomware confirmation** — finding-2026-
  05-13-0002 in this morning's brief; BleepingComputer relay
  this afternoon corroborates without adding fresh information.
- **Microsoft May 2026 Patch Tuesday cohort (CVE-2026-41089
  Netlogon + CVE-2026-41096 DNS + CVE-2026-42898 Dynamics 365)**
  — covered in 2026-05-12 afternoon finding-2026-05-12-0003.
- **MSTIC MDASH agentic vuln-discovery + AI-developed zero-day
  mass-exploitation** — flagged at 2026-05-13 00:00 sentinel +
  morning brief orchestrator awareness.
- **Mini Shai-Hulud TanStack expansion** — anti-noise to
  2026-05-12 06:00 FLASH-0001.
- **Fortinet + Ivanti + Chipmaker Patch Tuesday cohort** — covered
  in 2026-05-12 PM raw signals + finding-2026-05-12-0004.

## Source-health updates this sweep

See `sources_health_changed_this_sweep` block in frontmatter.
Notable:

- `mandiant` — feedburner 404 21st consecutive sweep; failure_count
  19 → 20 (held healthy pending operator alt-endpoint decision).
- `dragos` — STALE FLIP this sweep (third consecutive 404 across
  00:00 + 06:00 + 14:30 sweeps; per >=2-failure rule, source is
  now operationally stale; operator-side working RSS path
  identification still pending).
- `crowdstrike` — feedburner 404 from 06:00 sweep NOT re-tested
  this sweep (FLASH-fast scope); failure_count remains 1.
- `wiz-research-rss` — wiz.io/blog/rss.xml still 404; WebFetch on
  the blog index page is the productive endpoint this sweep
  (surfaced both Fragnesia + TanStack-expansion).
- `bitdefender` — NEW source-health entry. First Archimedes-corpus
  citation via raw-1430-001. Provisional A grade proposed.

## Flagged for orchestrator awareness (2026-05-13 afternoon brief candidates)

- **Wiz Research — Fragnesia Linux kernel LPE via ESP-in-TCP
  (2026-05-13).** UNPATCHED at disclosure; public PoC on V12
  security GitHub; NO ITW; Dirty Frag family lineage variant
  (regression from the original Dirty Frag patches). Worth
  afternoon-brief Vulnerabilities section coverage as widely-
  deployed kernel-subsystem class disclosure with active mitigation
  guidance (disable esp4/esp6/rxrpc unused, restrict user
  namespaces). NOT FLASH per Trigger 6 strict reading.

- **Microsoft 2026 patching pace + MDASH AI vuln-discovery** —
  carry-forward from 2026-05-13 00:00 sentinel + morning-brief
  orchestrator awareness. The Record relay 12:54 UTC today
  extends the corpus coverage; MDASH disclosure was at MSTIC
  18:00 EDT yesterday.

- **OpenLoop Health 716k-impacted data breach** — healthcare
  sector, no A&D, no actor; afternoon-brief Other Signal
  candidate only if A&D-relevance angle surfaces.

- **Foxconn / Nitrogen carry-forward** — BleepingComputer
  corroboration of finding-2026-05-13-0002; no fresh information;
  afternoon brief should reference the morning-brief item
  without re-litigating.

## What did NOT change this sweep

- Splunk first-party non-archimedes-internal stream: 0 events
  6h + 24h + 30d on the full FamousSparrow / Salt Typhoon /
  Deed RAT / TernDoor / C2 domain / n-day CVE chain indicator
  set (twenty-first consecutive dormant sweep across both
  indexes).
- KEV catalog: 0 entries dateAdded ≥ 2026-05-13 (CVE-2026-42208
  BerriAI LiteLLM remains most recent at 2026-05-08).
- Mandiant feedburner: 21st consecutive 404.
- x-cisagov + x-gossithedog + ars-security: stale-held per prior
  source-health entries; ars-security workaround in use this
  sweep (root feed, no security desk content).

---

## Extraction notes

- Sentinel file — per FLASH-POLICY convention for sweeps that
  produce FLASH candidates, this sentinel carries the broader
  sweep audit trail while the per-candidate raw-signal carries
  the full source content + IOC extraction.
- Pre-flight LEGAL-POLICY check: passive RSS/web fetches + own-
  index Splunk reads + VirusTotal C2 domain lookups only;
  `authorized_for_active_recon` remains empty; no prohibited
  query patterns triggered; no credentials surfaced this sweep.
- Anti-noise enforced per FLASH-POLICY §one-flash-per-topic-per-
  24h (Outlook zero-click absorbed into morning brief; Foxconn /
  Nitrogen morning-brief covered; Patch Tuesday cohort prior-
  brief covered).
- No raw-signal items marked `test: true` filtered from sweep
  (none observed in current `threats/raw-signal/` directory
  via my survey of recent files).
- Quiet hours INACTIVE — FLASH candidate eligible for immediate
  posting if grader / red-team / briefer concur on FLASH-format
  publication.

## IOCs (sentinel level)

This sentinel file carries no body-level IOC extraction. The full
IOC block (9 indicators including 2 VT-confirmed C2 domains, 2
MD5 hashes, 5 ProxyShell + ProxyNotShell CVEs recycled as n-day,
3 named malware families) is in raw-2026-05-13-flash-1430-001.

Splunk first-party queries this sweep:

```yaml
splunk_queried_iocs_no_match:
  flash_candidate_actor_aliases:
    - "Salt Typhoon"
    - FamousSparrow
    - "Earth Estries"
    - GhostEmperor
    - UNC2286
    - "UAT-9244"
  flash_candidate_malware_families:
    - "Deed RAT"
    - Snappybee
    - TernDoor
    - "Mofu Loader"
  flash_candidate_c2_domains:
    - virusblocker.it.com
    - sentinelonepro.com
  flash_candidate_initial_access_cves:
    - CVE-2021-34473
    - CVE-2021-34523
    - CVE-2021-31207
    - CVE-2022-41040
    - CVE-2022-41082
    - ProxyShell
    - ProxyNotShell
    - "Exchange Server"
  tracked_roster_actors_baseline_queried:
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
against `archimedes` and `defenseclaw_local` indexes over `-30d`
window.
