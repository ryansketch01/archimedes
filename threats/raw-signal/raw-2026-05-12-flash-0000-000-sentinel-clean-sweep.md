---
raw_id: raw-2026-05-12-flash-0000-000
collected_at: 2026-05-12T00:05:00-04:00
run_id: flash-sweep-20260512-000000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-12T00:00:00-04:00
time_window_start: 2026-05-11T18:00:00-04:00
time_window_end: 2026-05-12T00:00:00-04:00
test: false
sources_queried:
  - cisa-kev               # JSON feed via WebFetch — 8 most recent entries returned. Zero entries with dateAdded >= 2026-05-11. Most recent KEV addition remains CVE-2026-42208 (BerriAI LiteLLM SQL injection, dateAdded 2026-05-08, dueDate 2026-05-11 = TODAY, now ~T+5h to T+11h depending on EOB interpretation). Three KEV-listed deadlines have now all passed (CVE-2026-0300 PAN-OS 2026-05-09 EOB, CVE-2026-6973 Ivanti EPMM 2026-05-10 EOB, CVE-2026-42208 LiteLLM 2026-05-11 EOB). CVE-2024-1708 ConnectWise ScreenConnect dueDate 2026-05-12 = TOMORROW. CVE-2026-32202 Microsoft Windows dueDate 2026-05-12 = TOMORROW. CVE-2026-31431 Linux Kernel dueDate 2026-05-15 = T+3d. KEV catalog does not publish compliance-status changes against passed deadlines.
  - cisa-advisories        # all.xml RSS via fetch_feed — status 200, 30 items in feed total, 0 items in 6h window after since-filter.
  - bleepingcomputer       # RSS via fetch_feed — status 200, etag 361dac58622b4e18ca15d59137d26957, last_modified 2026-05-12T03:50:57 GMT (within window from feed-server activity), 3 items in 6h window after since-filter. (1) "GM agrees to $12.75M California settlement over sale of drivers' data" (Bill Toulas, 2026-05-11T22:40 UTC = 18:40 EDT in-window) — California CCPA settlement, NO threat-intel, NO A&D, NO actor. DISCARDED per Mode 1 procedure. (2) "Official CheckMarx Jenkins package compromised with infostealer" (Bill Toulas, 2026-05-11T22:03 UTC = 18:03 EDT in-window) — RE-COVERAGE of TeamPCP/Checkmarx/Jenkins supply-chain story already raw-signaled at raw-2026-05-11-flash-0600-001 this morning and carried forward to 08:00 morning brief grader queue. Anti-noise applies — same package, same TeamPCP "With love" attribution note, same KICS lineage. DISCARDED per FLASH-POLICY anti-noise (one FLASH per topic per 24h). (3) "New GhostLock tool abuses Windows API to block file access" (Lawrence Abrams, 2026-05-11T22:02 UTC = 18:02 EDT in-window) — security researcher proof-of-concept by Kim Dvash of Israel Aerospace Industries. NOT in-the-wild, NO threat actor associated, NO CVE (legitimate API abused for novel purpose). The IAI researcher affiliation is A&D-watchlist-adjacent but PoC publication ≠ A&D-sector campaign per FLASH-POLICY Trigger 5 (must be active multi-victim against A&D, not researcher PoC). DISCARDED per Mode 1 procedure.
  - securityweek           # RSS via fetch_feed — status 200, etag W/cd6c5cf6bb96a08c6b0c3b98092c908f, last_modified 2026-05-11T17:18:52 GMT (pre-window — feed-server activity quieted overnight), 0 items in 6h window after since-filter.
  - the-record             # RSS via fetch_feed — status 200, 5 items total in feed, 0 items in 6h window after since-filter (most recent dated 2026-05-08; weekend cadence quiet through Monday).
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-12T02:20:41 GMT (within window from feed-server activity), 0 items in 6h window after since-filter — normal Krebs cadence.
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, last_modified 2026-05-11T17:38:35 GMT (pre-window), 0 items in 6h window. Most recent MSTIC content remains 2026-05-08T17:12 UTC Dirty Frag active-attack post (~103h aged at this sweep).
  - unit42                 # RSS (feedburner) via fetch_feed — status 200, last_modified 2026-05-11T22:51:12 GMT (within window from feed-server activity), 1 item in 6h window after since-filter — "Inside AD CS Escalation: Unpacking Advanced Misuse Techniques and Tools" (Stav Setty, Tom Fakterman, Shachar Roitman; 2026-05-11T22:00:43 UTC = 18:00 EDT in-window). WebFetch on the article confirmed: Fighting Ursa (APT28 alias, roster #006) referenced as HISTORICAL CONTEXT ONLY (2025 CISA advisory citation); NO new 2026 attribution; NO new TTP/tooling/infrastructure attributed to Fighting Ursa; NO A&D victims; defensive/educational research on AD CS attack mechanics (CVE-2022-26923 cited; ADExplorer + Certipy tooling discussed in defender terms; no IOCs published). Trigger 2 FAIL on "attribution is new — not re-reporting prior" (this is explicit historical-restatement). Trigger 4 FAIL on "new tooling/targeting/infrastructure documented" (no new TTP attributed to Fighting Ursa here; the techniques described are method-class, not actor-class developments). DISCARDED per Mode 1 procedure for FLASH purposes. Notable for morning-brief awareness as a defender's-reference piece on a roster-actor-aliased technique class — flagged to grader queue at non-FLASH severity if morning brief composer wants to use it as detection-engineering background.
  - sans-isc               # RSS via fetch_feed (rssfeed.xml) — status 200, etag W/1cb5-65196e2b06c8b, last_modified 2026-05-12T03:59:10 GMT (within window from feed-server activity), 2 items in 6h window after since-filter. (1) "ISC Stormcast For Tuesday, May 12th, 2026" (podcast detail, 2026-05-12T03:15 UTC = 23:15 EDT in-window) — awareness-only, no body content. DISCARDED. (2) "Apple Patches Everything, (Mon, May 11th)" (no author, 2026-05-11T22:19 UTC = 18:19 EDT in-window) — standard Patch Tuesday announcement, 84 CVEs across iOS/iPadOS/macOS/tvOS/watchOS/visionOS for the "26" series + iOS/iPadOS 18 + macOS 14/15. WebFetch not invoked (SANS ISC diary explicitly noted as feature-update routine). No specific ITW-exploited zero-day called out in this short diary entry; standard Patch Tuesday cadence. NOT a Trigger 1 single-CVE candidate, NOT a Trigger 6 zero-day-without-patch (Apple shipped the patches today). Flagged for morning brief patch-backlog tier awareness only, NOT raw-signaled as FLASH candidate. DISCARDED per Mode 1 procedure for FLASH-trigger purposes.
  - rapid7                 # RSS via fetch_feed (rapid7.com/blog/rss/) — status 200, last_modified 2026-05-12T03:20:05 GMT (within window from feed-server activity), 0 items in 6h window after since-filter.
  - crowdstrike            # RSS via fetch_feed — status 200, etag "15dd-651836b096ddb-gzip", last_modified 2026-05-11T04:45:38 GMT (pre-window), 10 items returned ALL with null published_at (SIXTEENTH consecutive sweep with this dateless marketing pattern across 8 days). Same pile (Gartner MQ leader, Falcon OverWatch for Defender, Risk Assessments, AI Vuln Discovery podcast, CORDIAL/SNARKY SPIDER product-marketing, CrowdStrike ChatGPT Enterprise audit logging, Frost & Sullivan CNAPP, Google Cloud detection expansion, Falcon Cloud Security ROI, Falcon Platform ROI). No 2026-05-11/12 threat-research content visible. Pattern fully entrenched.
  - sentinelone-labs       # RSS via fetch_feed (sentinelone.com/labs/feed/) — status 200, etag W/1c9232cf89238de946381ca496ee6085, last_modified 2026-05-12T01:33:43 GMT (within window from feed-server activity but no fresh body), 0 items in 6h window.
  - sophos                 # RSS via fetch_feed (news.sophos.com/feed/) — status 200, 9 items total in feed, 0 items in 6h window.
  - eset-welivesecurity    # RSS via fetch_feed — status 200, 100 items total in feed, 0 items in 6h window.
  - hacker-news            # WebFetch on thehackernews.com/ index — 8 most recent articles listed. Three items 2026-05-11-dated evaluated for FLASH-trigger fit: (1) "TeamPCP Compromises Checkmarx Jenkins AST Plugin Weeks After KICS Supply Chain Attack" — RE-COVERAGE of TeamPCP/Checkmarx/Jenkins story already raw-signaled at raw-2026-05-11-flash-0600-001 (FLASH-POLICY anti-noise applies). DISCARDED. (2) "cPanel CVE-2026-41940 Under Active Exploitation to Deploy Filemanager Backdoor" — RAW-SIGNALED to raw-2026-05-12-flash-0000-001 below for grader queue (NEW operational IOC layer + Mr_Rot13 actor — NOT in _roster.yaml; KEV-listed CVE 2026-04-30 with passed dueDate; Triggers 1/2/4/5/6 all fail on tracked-actor or A&D-targeting requirements; non-FLASH grader queue item). (3) "Hackers Used AI to Develop First Known Zero-Day 2FA Bypass for Mass Exploitation" — RAW-SIGNALED to raw-2026-05-12-flash-0000-002 below for grader queue (GTIG / Google Threat Intelligence Group A-grade primary; high-priority intel — first known AI-developed mass-exploitation zero-day; FLASH triggers fail on absent-CVE/CVSS-gating + absent-tracked-actor + patched-at-disclosure + no-A&D-sector-named; non-FLASH but morning-brief high-priority).
  - cloud-google-blog-mandiant  # WebFetch on cloud.google.com/blog/topics/threat-intelligence top page — confirmed GTIG post "Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access" is the originating source for the Hacker News AI-2FA item. Mandiant feedburner endpoint /Mandiant continues 404 (FIFTEENTH consecutive); failure_count 13→14. WebSearch corroboration confirms 2026-05-11 publication date (SiliconANGLE / Infosecurity Magazine / PYMNTS / blog.google all relay-corroborate same day). Operator alt-endpoint decision still pending; primary research was reachable on its destination page even though the RSS feedburner remains dead.
  - nvd                    # WebFetch on services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=2026-05-11T22:00:00.000-04:00&lastModEndDate=2026-05-12T04:00:00.000-04:00 for the 6h window. cvssV3Severity=CRITICAL → 2 results: CVE-2026-34260 (SAP S/4HANA SQL injection by authenticated attacker via user-controlled input, CVSS 9.6, published 2026-05-12T03:16Z) and CVE-2026-34263 (SAP Commerce Cloud unauthenticated malicious configuration upload + code injection → arbitrary server-side code execution, CVSS 9.6, published 2026-05-12T03:16Z). cvssV3Severity=HIGH → 1 result: CVE-2026-34259 (SAP Forecasting & Replenishment OS command execution by authenticated admin, CVSS 8.2, published 2026-05-12T03:16Z). All three are SAP cluster patches from SAP's Tuesday security advisory (May 2026 patch day). SAP is widely deployed in A&D primes as ERP backbone, but NONE of the three CVEs has any ITW-exploitation claim attached, and the primary source is NVD-metadata only (no A-grade vendor advisory with exploitation IOCs yet observed). Trigger 1 FAIL on "confirmed active exploitation in the wild + A-grade source" (NVD-only structural metadata; no exploitation claim). Trigger 6 FAIL on "exploitation confirmed or imminent per A-grade source" (no exploitation claim, patches already in advisory). All three DISCARDED per Mode 1 for FLASH purposes. Flagged for morning brief patch-backlog tier awareness — A&D supply-chain ERP relevance is real but the FLASH structural test fails cleanly.
  - splunk-archimedes      # search NOT sourcetype=archimedes:* over 6h returned zero events; same over 24h zero events. Targeted IOC keyword sweep across 25 high-priority tokens (APT28/Fancy Bear/APT29/Cozy Bear/UNC1549/Charming Kitten/MuddyWater/APT34/APT37/APT40/APT41/Volt Typhoon/Salt Typhoon/Lazarus/Stardust Chollima/Sandworm/Scattered Spider/TeamPCP + CVE-2026-0300/6973/42208/34260/34263/34259) over 24h returned 4 hits — ALL archimedes:operation pipeline self-references (1x flash_sweep operator-initiated 2026-05-11T17:00 event whose payload mentions CVEs in disposition strings; 1x brief_published afternoon at 16:47 EDT 2026-05-11 with related_vulns includes CVE-2026-41940/CVE-2020-1472/CVE-2026-6973/CVE-2026-42208 in payload; 1x brief_published morning at 08:16 EDT 2026-05-11 with related_actors includes "001" TeamPCP in payload; 1x flash_sweep_clean 06:00 EDT 2026-05-11 referencing the Checkmarx Jenkins item in raw_signal_files list). Pipeline self-references match the keyword tokens in their JSON payloads but reflect Archimedes' own operational logging, NOT external observations.
  - splunk-defenseclaw     # NOT sourcetype=archimedes:* over 6h returns zero events; over 24h also zero. FOURTEENTH consecutive sweep with dormant non-archimedes-internal stream pattern across both indexes.
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH — three consecutive WinError 10060 nitter.net timeouts. Now >36h since stale-flip → would be eligible-to-retry per 24h rule, but FLASH-fast scope kept to RSS/vendor/KEV priority feeds; treating as effectively stale until operator nitter-pool / direct-X-API decision.
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted. >72h since stale flip but FLASH-fast scope kept; treating as effectively stale.
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround in use (arstechnica.com/feed/ root path); root path not invoked this sweep — quiet-hours overnight cadence makes Ars site-wide unlikely to break fresh A&D-relevant signal in 6h window.
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom (per-repo GHSA fallback path remains productive workaround when triggered; not triggered this sweep)
  - proofpoint             # /us/threat-insight/blog/feed endpoint 404 since 2026-05-10 12:00 FLASH; alt /us/rss.xml corporate-news endpoint recovered at 2026-05-11 00:00 FLASH but multi-day cadence, not invoked this sweep
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (FIFTEENTH consecutive); failure_count 13→14. cloud.google.com index page WebFetch DID surface the GTIG AI Threat Tracker piece (originating source for the Hacker News AI-2FA item) — destination page reachable even though feedburner is dead. Operator alt-endpoint decision still pending.
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - flash_sweep_clean
  - sentinel
  - quiet_hours_active
  - gtig_ai_2fa_zero_day_non_flash_high_priority_grader_queue
  - cpanel_mr_rot13_active_exploitation_non_flash_grader_queue
  - teampcp_checkmarx_jenkins_repeat_anti_noise
  - apt28_unit42_ad_cs_historical_context_only_discarded
  - sap_cluster_three_cves_nvd_metadata_only_no_itw_discarded
  - apple_patch_tuesday_84_cves_routine_no_itw_zero_day_called_out
  - splunk_dormant_14th_consecutive
  - mandiant_feedburner_15th_consecutive_404
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      No new CVSS >= 9.0 with confirmed in-the-wild exploitation from an
      A-grade source in the 2026-05-11T18:00 EDT → 2026-05-12T00:00 EDT
      window.

      CISA KEV: zero entries dated >= 2026-05-11. Most recent KEV add
      remains CVE-2026-42208 (BerriAI LiteLLM SQL injection, dateAdded
      2026-05-08, dueDate 2026-05-11 = TODAY EOB now passed). Three
      KEV-listed deadlines have all passed this week (PAN-OS 2026-05-09,
      Ivanti EPMM 2026-05-10, LiteLLM 2026-05-11). KEV catalog does not
      publish compliance-status changes against passed deadlines.

      cPanel CVE-2026-41940 (KEV-listed 2026-04-30, knownRansomwareUse
      = Known) DOES have an active-exploitation operational layer
      published this window via Hacker News relaying QiAnXin XLab
      research (2,000+ attacker source IPs in mass-exploitation pattern;
      Mr_Rot13 actor named, NOT in _roster.yaml). The CVSS for CVE-2026-
      41940 is not handy from the immediate fetch (KEV catalog does
      not embed CVSS), but the structural Trigger 1 conditions still
      fail because: (a) the originating research source (QiAnXin XLab)
      is NOT in source-grades.yaml — it would be a new provisional grade
      per the LayerX/Seqrite/Trendyol-Albayrak precedent (likely C on
      first surface), NOT A-grade; (b) BleepingComputer / Hacker News
      relays are B-grade, below A-grade requirement; (c) no A-grade
      vendor (Mandiant/CrowdStrike/Unit 42/MSTIC/Volexity/SentinelLabs)
      independent corroboration of the active-exploitation operational
      layer was observed this sweep. Trigger 1 fails by source-grade
      structural test. RAW-SIGNALED to grader queue as a non-FLASH item
      for morning-brief composer awareness.

      NVD lastModStartDate window 2026-05-11T22:00 → 2026-05-12T04:00
      UTC: CRITICAL = 2 results (CVE-2026-34260 SAP S/4HANA SQL
      injection 9.6, CVE-2026-34263 SAP Commerce Cloud unauth code
      injection 9.6); HIGH = 1 result (CVE-2026-34259 SAP Forecasting
      & Replenishment OS command execution 8.2). All three are NVD-
      metadata-only entries from SAP's Tuesday patch day (May 2026
      cycle). NO ITW-exploitation claim is attached to any of the three.
      SAP is widely deployed in A&D primes as ERP backbone (real
      structural A&D-relevance), but Trigger 1 fails on the "confirmed
      active exploitation + A-grade source" structural test — NVD-only
      records without an exploitation claim or A-grade vendor advisory
      with IOCs do not satisfy the conjunction. Flagged for morning
      brief patch-backlog tier awareness only.

      Unit 42 "Inside AD CS Escalation" (Stav Setty / Tom Fakterman /
      Shachar Roitman, in-window 18:00 EDT) cites CVE-2022-26923 in
      defensive context. Old 2022 CVE; no active exploitation claim;
      educational/defender research. Trigger 1 FAIL.

      SAP cluster, Apple Patch Tuesday cluster, GTIG AI 2FA bypass
      (CVE-undisclosed), cPanel CVE-2026-41940 lineage — none cleanly
      meets the Trigger 1 conjunction of (CVSS >= 9.0 AND confirmed
      ITW AND A-grade source naming the ITW operational layer).

  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      TeamPCP / Checkmarx Jenkins plugin item (BleepingComputer 18:03
      EDT + Hacker News headline) RE-COVERS the 2026-05-11 06:00 FLASH
      raw-signal raw-2026-05-11-flash-0600-001 already in the morning
      brief grader queue. The TeamPCP attribution is RESTATEMENT, not
      first-time naming. Anti-noise rule (one FLASH per topic per 24h)
      applies — Checkmarx Jenkins / TeamPCP lineage was triaged at
      06:00 sweep as Trigger 2 fail on restated-attribution rule and
      Trigger 4 marginal on composite source-grade. Today's BC/THN
      relay does not introduce a new tracked-actor attribution; it
      adds operator-initiated reporting volume on the same incident.
      Trigger 2 FAIL.

      Unit 42 AD CS article (18:00 EDT in-window) references Fighting
      Ursa (APT28 alias, roster #006) as HISTORICAL CONTEXT ONLY (2025
      CISA advisory citation). Article authors do NOT attribute any
      new 2026 activity, new TTP, new tooling, or new infrastructure
      to Fighting Ursa. The Fighting Ursa mention is illustrative
      defender-education material, NOT a fresh attribution event.
      Trigger 2 FAIL on explicit historical-restatement.

      cPanel CVE-2026-41940 article names "Mr_Rot13" actor — NOT in
      _roster.yaml. Trigger 2 requires the attributed actor be in the
      tracked roster. FAIL.

      GTIG AI 2FA bypass article names the actor as "unknown threat
      actor" / "cybercrime threat actors" — NO named actor at all,
      let alone a tracked one. Trigger 2 FAIL.

      Apple Patch Tuesday and SAP cluster: no actor attribution. FAIL.

  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk archimedes + defenseclaw_local combined sweep over 6h
      window returns zero non-archimedes-internal events. Same query
      over 24h returns zero non-archimedes-internal events. Targeted
      IOC keyword sweep across 25 high-priority tokens (15 tracked
      actor aliases + 6 priority CVEs spanning corpus-tracked and
      this-window-disclosed) over 24h returned 4 hits — ALL four are
      archimedes:operation pipeline self-references (flash_sweep
      operator-initiated 17:00 EDT 2026-05-11 + brief_published
      afternoon 16:47 EDT + brief_published morning 08:16 EDT +
      flash_sweep_clean 06:00 EDT). Pipeline self-references match
      the keyword tokens in their JSON payloads but reflect
      Archimedes' own operational logging, NOT external observations.
      Both indexes appear not to be receiving live security telemetry.
      FOURTEENTH consecutive sweep with dormant non-archimedes-internal
      stream pattern. Trigger 3 cannot fire on a dormant non-Archimedes
      stream.

  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      No A-grade or B-grade source documented a new tooling, new
      targeting, or new infrastructure class clearly attributable to
      a tracked roster actor in the 6h window.

      Unit 42 AD CS article (Fighting Ursa = APT28 alias) is defender-
      educational research on a TECHNIQUE CLASS (AD CS template
      misuse, shadow credentials, certificate-based persistence),
      NOT a new TTP attribution to APT28 specifically. The techniques
      are well-documented in the broader corpus (MITRE T1098.001, T1649,
      T1606.001); citing Fighting Ursa as one example user does not
      constitute a NEW TTP attribution. FAIL.

      TeamPCP / Checkmarx Jenkins is a structural-continuation TTP
      (supply-chain plugin/package compromise via stolen GitHub
      credentials for infostealer distribution) — consistent with
      prior TeamPCP supply-chain attacks across npm, Trivy, KICS.
      Same TTP class, new victim. Per the 06:00 FLASH evaluation, this
      is Trigger 4 marginal on composite source-grade; the 18:03 EDT
      BC re-coverage does not change the TTP-novelty calculus. FAIL.

      GTIG AI 2FA bypass article describes an emerging-class TTP
      (AI-developed exploit for mass exploitation of an open-source
      vendor's product) but does NOT attribute it to any tracked
      roster actor — the article explicitly names the actor as
      "unknown threat actor." Trigger 4 requires "clearly attributable
      to a tracked actor"; FAIL.

      cPanel Mr_Rot13: actor not in roster. FAIL.

  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      No source documented an active multi-victim campaign explicitly
      targeting aerospace, defense, or watchlist companies in the 6h
      window.

      cPanel CVE-2026-41940 mass-exploitation (2,000+ attacker source
      IPs, multi-region across Germany/US/Brazil/Netherlands) is
      genuinely multi-victim and active, but the victim sector profile
      named is "hosting and webmaster customers of cPanel/WHM" — a
      hosting/SMB attack surface, NOT aerospace/defense. NO A&D primes
      named, NO A&D sector named. FAIL.

      GTIG AI 2FA bypass mass-exploitation operation is multi-victim
      and active per GTIG, but the impacted vendor is named only as
      "popular open-source, web-based system administration tool" —
      no sector breakdown, no A&D primes named. FAIL on
      A&D-sector-explicit-targeting.

      SAP S/4HANA cluster has real A&D structural relevance (ERP
      backbone in most A&D primes) but no exploitation claim and no
      victims named at all. FAIL on "active" + "multi-victim".

      Apple Patch Tuesday: no campaign claim, no victims. FAIL.

      TeamPCP / Checkmarx Jenkins: Jenkins is widely deployed in A&D
      DevSecOps environments (structural relevance noted in 06:00
      FLASH raw-signal frontmatter), but neither this 18:03 EDT BC
      re-coverage nor the morning Hacker News headline names any A&D
      prime among compromised/exposed organizations. Per the 06:00
      evaluation, this is Trigger 5 fail on no-named-primes. FAIL.

  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      No vulnerability disclosed before a patch was available with
      either CVSS >= 8.0 OR widely-deployed-product impact AND
      exploitation confirmed/imminent per A-grade source.

      GTIG AI 2FA bypass article (the closest structural fit) was a
      zero-day AT TIME OF ACTOR-EXPLOITATION, but GTIG explicitly
      states "Google worked with the impacted vendor to responsibly
      disclose the flaw and get it fixed" — patches exist at time of
      GTIG publication. Trigger 6 requires "Vulnerability disclosed
      before a patch is available"; the post-responsible-disclosure
      publication framing fails this structural test. FAIL.

      cPanel CVE-2026-41940 is patched (vendor advisory issued before
      KEV-listing 2026-04-30). FAIL on patch-available.

      SAP cluster: patches available in SAP's Tuesday advisory
      simultaneous with NVD disclosure. FAIL.

      Apple Patch Tuesday: patches shipped today, no orphan zero-days
      called out in the SANS ISC summary. FAIL.

      Unit 42 AD CS / CVE-2022-26923: old CVE, patched in 2022. FAIL.

  critical_override_evaluated:
    applied: false
    notes: |
      Critical override requires ALL FOUR: CVSS 10.0 + confirmed
      active exploitation + tracked actor + A&D watchlist entity
      named as target. ZERO of four conditions satisfied this
      sweep (no CVSS-10.0 candidate; no clean A-grade active
      exploitation claim against a Trigger 1 candidate; no tracked
      roster actor attribution; no A&D prime named as target).
      Override fails by all four hard thresholds. Quiet-hours rule
      remains in force regardless (00:00 EDT is inside 21:00-09:00
      quiet-hours window) — even a hypothetically successful FLASH
      would be queued, not posted, until 09:00 catchup sweep.

anti_noise_observations:
  - topic: TeamPCP-Checkmarx-Jenkins-plugin-compromise
    prior_flash_in_24h: true
    prior_raw_signal: raw-2026-05-11-flash-0600-001
    prior_disposition: non-FLASH grader queue carry-forward to 08:00 morning brief
    this_sweep_evidence:
      - "BleepingComputer 'Official CheckMarx Jenkins package compromised with infostealer' (Bill Toulas, 2026-05-11T22:03 UTC = 18:03 EDT)"
      - "Hacker News 'TeamPCP Compromises Checkmarx Jenkins AST Plugin Weeks After KICS Supply Chain Attack' (Ravie Lakshmanan, 2026-05-11-dated)"
    resurface_conditions_evaluated:
      new_iocs: false                       # BC article mentions only the version string 2026.5.09 already in prior raw-signal; no new hashes/C2/IP layers published this resurface
      independent_a_grade_corroboration: false   # both BC and THN relays are B-grade
      novel_post_exploitation_ttps: false   # same supply-chain-plugin-stolen-GitHub-creds-infostealer chain documented prior
    disposition: anti-noise rule applies; DISCARDED for new raw-signal write. Existing 06:00 raw-signal carries forward to 08:00 grader.
  - topic: APT28-Fighting-Ursa-historical-context-defensive-research
    prior_flash_in_24h: false
    prior_corpus_coverage: APT28 dossier (#006) and prior CISA 2025 advisory referenced are baseline-corpus context
    this_sweep_evidence:
      - "Unit 42 'Inside AD CS Escalation: Unpacking Advanced Misuse Techniques and Tools' (Stav Setty, Tom Fakterman, Shachar Roitman; 2026-05-11T22:00 UTC = 18:00 EDT)"
    disposition: Flagged for morning brief detection-engineering background section if composer wants; NOT a fresh attribution event, NOT raw-signaled at FLASH severity.
  - topic: Apple-May-2026-Patch-Tuesday-84-CVEs
    prior_corpus_coverage: none (routine vendor patch cycle, not previously tracked)
    this_sweep_evidence:
      - "SANS ISC diary 'Apple Patches Everything' (2026-05-11T22:19 UTC = 18:19 EDT)"
    disposition: Routine Patch Tuesday; no Trigger 1 single-CVE zero-day called out in the short diary entry. Morning brief patch-backlog tier awareness only.

flash_candidates: []

splunk_first_party_24h_sweep:
  query_archimedes: zero non-archimedes-internal events
  query_defenseclaw_local: zero non-archimedes-internal events
  targeted_keyword_token_hits: 4 hits, all pipeline self-references (archimedes:operation sourcetype)
  consecutive_dormant_sweeps: 14
  trigger_3_status: cannot_fire_on_dormant_stream

source_health_changes:
  - source_yaml_id: mandiant
    runtime_field: failure_count
    old_value: 13
    new_value: 14
    rationale: "feedburner.com/Mandiant returns 404 fifteenth consecutive; cloud.google.com destination page reachable and surfaced GTIG AI Threat Tracker piece this sweep. Held healthy pending operator alt-endpoint decision."
  - source_yaml_id: sans-isc
    runtime_field: last_successful_fetch
    old_value: 2026-05-11T00:00:00-04:00
    new_value: 2026-05-12T00:00:00-04:00
    rationale: "rssfeed.xml reachable status 200, 2 in-window items returned (Stormcast podcast + Apple Patch Tuesday diary). failure_count remains 0."
  - source_yaml_id: bleepingcomputer
    runtime_field: last_successful_fetch
    old_value: 2026-05-11T00:00:00-04:00
    new_value: 2026-05-12T00:00:00-04:00
    rationale: "RSS reachable status 200; 3 in-window items returned (GM CCPA settlement / Checkmarx Jenkins / GhostLock PoC); all discarded per Mode 1 (GM = consumer privacy not A&D; Checkmarx = anti-noise rule applies; GhostLock = researcher PoC not ITW)."
  - source_yaml_id: unit42
    runtime_field: last_successful_fetch
    old_value: 2026-05-11T00:00:00-04:00
    new_value: 2026-05-12T00:00:00-04:00
    rationale: "feedburner.com/Unit42 reachable status 200; 1 in-window item (AD CS escalation defensive research; Fighting Ursa historical context only)."
  - source_yaml_id: krebs
    runtime_field: last_successful_fetch
    old_value: 2026-05-11T00:00:00-04:00
    new_value: 2026-05-12T00:00:00-04:00
    rationale: "RSS reachable status 200; 0 in-window items — normal Krebs cadence."

run_summary:
  in_window_items_evaluated: 9    # 3 BC + 1 Unit42 + 2 SANS-ISC + 3 NVD CRITICAL/HIGH = 9 distinct items
  in_window_items_raw_signaled_non_flash_grader_queue: 2  # GTIG AI 2FA, cPanel Mr_Rot13
  in_window_items_anti_noise_discarded: 2     # TeamPCP/Checkmarx repeat (BC + THN headline), Crimenetwork bust would-be (no this-sweep — anti-noise from 2026-05-11 06:00 + 12:00 sweeps but not surfaced fresh this sweep)
  in_window_items_mode1_discarded: 5  # GM CCPA, GhostLock PoC, APT28 Unit42 historical-only, SANS Stormcast, Apple Patch Tuesday + 3 NVD CRITICAL/HIGH SAP cluster (counted separately): re-count 4 BC/Unit42/SANS-ISC discards + 3 NVD SAP discards = 7 Mode-1 discards
  flash_triggers_fired: 0
  flash_candidates_promoted: 0
  source_health_runtime_changes: 5
  quiet_hours_active: true
  posting_required: false

ttl_expires_at: 2026-08-10T00:05:00-04:00
---

# 00:00 EDT FLASH alert sweep (2026-05-12) — clean, two non-FLASH grader queue items

## Sentinel summary

00:00 EDT 2026-05-12 FLASH sweep ran clean against all six FLASH triggers. Six-hour window 2026-05-11T18:00 → 2026-05-12T00:00 EDT.

**Zero FLASH candidates surfaced.** Quiet-hours rule active (00:00 EDT inside 21:00–09:00 window) — no Discord posting required even if a FLASH had triggered (would have queued to 09:00 catchup sweep).

**Two non-FLASH grader-queue raw-signals written this sweep:**

1. `raw-2026-05-12-flash-0000-001` — cPanel CVE-2026-41940 active-exploitation operational layer (QiAnXin XLab originating research relayed via Hacker News / BleepingComputer-tier coverage; Mr_Rot13 actor NOT in `_roster.yaml`; 2,000+ attacker source IPs in mass-exploitation pattern; KEV-listed 2026-04-30 with passed dueDate; structural FLASH-trigger fails on tracked-actor and A&D-targeting requirements but worth grader awareness for the operational IOC layer).

2. `raw-2026-05-12-flash-0000-002` — Google Threat Intelligence Group (GTIG) "Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access" (Mandiant-tier A-grade primary, 2026-05-11 publication, first known AI-developed zero-day for mass-exploitation against a 2FA bypass on a "popular open-source, web-based system administration tool"; vendor undisclosed; patched at time of disclosure; structural FLASH-trigger fails on no-CVE/CVSS-gating + no-tracked-actor + patched-at-disclosure + no-A&D-sector-named; HIGH-PRIORITY morning-brief intel due to the AI-development novelty and A-grade primary source).

## Anti-noise observations

- **TeamPCP / Checkmarx Jenkins plugin compromise** (BleepingComputer 18:03 EDT + Hacker News headline) — RE-COVERAGE of the 2026-05-11 06:00 FLASH raw-signal `raw-2026-05-11-flash-0600-001` already in the morning brief grader queue. Anti-noise rule (one FLASH per topic per 24h) applies. No new IOCs published in the resurface, no independent A-grade corroboration, no novel post-exploitation TTPs. DISCARDED for new raw-signal write.

- **Unit 42 AD CS escalation article** references Fighting Ursa (APT28 alias, roster #006) as historical context only — 2025 CISA advisory citation. No new attribution, no new TTP/tooling/infrastructure. Defender-educational research. Flagged for morning brief detection-engineering background but NOT raw-signaled at FLASH severity.

- **Apple May 2026 Patch Tuesday** (84 CVEs across iOS / iPadOS / macOS / tvOS / watchOS / visionOS). Routine vendor patch cycle. No specific ITW-exploited zero-day called out in the SANS ISC short diary. Morning brief patch-backlog tier awareness only.

## Splunk first-party telemetry

Combined `archimedes` + `defenseclaw_local` index sweep over 6h returns zero non-archimedes-internal events. Same over 24h returns zero non-archimedes-internal events. Targeted IOC keyword sweep across 25 high-priority tokens (15 tracked actor aliases + 6 priority CVEs) over 24h returned 4 hits — all four are `archimedes:operation` sourcetype pipeline self-references (operator-initiated FLASH sweep 17:00 EDT + brief_published afternoon + brief_published morning + flash_sweep_clean 06:00 EDT, all with this-sweep-keyword tokens in their JSON payloads).

**Trigger 3 (first-party-IOC-hit) cannot fire on a dormant non-Archimedes stream.** Fourteenth consecutive sweep with this pattern across both indexes.

## Source health changes

- `mandiant` failure_count 13 → 14 (fifteenth consecutive feedburner 404; destination page reachable per WebFetch on cloud.google.com which surfaced the GTIG AI Threat Tracker primary). Held healthy pending operator alt-endpoint decision.
- `bleepingcomputer`, `unit42`, `sans-isc`, `krebs` — last_successful_fetch updated to 2026-05-12T00:00:00-04:00; failure_count remains 0 for all.

## Carry-forward state for 06:00 FLASH and morning brief

- **CISA KEV deadlines:** All three this-week deadlines (CVE-2026-0300 PAN-OS 2026-05-09, CVE-2026-6973 Ivanti EPMM 2026-05-10, CVE-2026-42208 LiteLLM 2026-05-11) have now passed. CVE-2024-1708 ConnectWise ScreenConnect dueDate 2026-05-12 = TOMORROW. CVE-2026-32202 Microsoft Windows dueDate 2026-05-12 = TOMORROW. CVE-2026-31431 Linux Kernel dueDate 2026-05-15 = T+3d.
- **Operation HookedWing** (2026-05-11 00:00 FLASH SecurityWeek/SOCRadar item) remains in grader queue without independent corroboration; brief composer can decide on UPDATE coverage.
- **GTIG AI Threat Tracker piece** is the standout intel for morning brief composition — A-grade primary on first known AI-developed zero-day for mass exploitation.

## Extraction notes

- Language: en
- Article types covered: vendor-research blog (Unit 42, GTIG/Mandiant page), media relay (BleepingComputer, Hacker News, SecurityWeek), government catalog (CISA KEV JSON, NVD REST), vendor advisory tier (SANS ISC, Apple shipped), Splunk first-party
- Raw IOC extraction skill invocation: not applicable to sentinel (no in-window FLASH candidate's body extracted at this level)

## IOCs

None at sentinel level. See companion raw-signals raw-2026-05-12-flash-0000-001 and raw-2026-05-12-flash-0000-002 for in-window non-FLASH grader-queue item bodies and any IOC sets carried in those.
