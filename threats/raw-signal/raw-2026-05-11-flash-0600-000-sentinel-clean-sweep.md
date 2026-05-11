---
raw_id: raw-2026-05-11-flash-0600-000
collected_at: 2026-05-11T06:02:00-04:00
run_id: flash-sweep-20260511-060000
collection_mode: flash_sweep
sweep_type: flash
sweep_time: 2026-05-11T06:00:00-04:00
time_window_start: 2026-05-11T00:00:00-04:00
time_window_end: 2026-05-11T06:00:00-04:00
test: false
sources_queried:
  - cisa-kev               # JSON feed via WebFetch — full-catalog scan for dateAdded >= 2026-05-10 returned zero entries. Most recent KEV add remains CVE-2026-42208 (BerriAI LiteLLM, dateAdded 2026-05-08, dueDate 2026-05-11 = TODAY ~T-2h to T-12h depending on EOD interpretation). CVE-2026-6973 Ivanti EPMM BOD-22-01 deadline 2026-05-10 EOB has passed without a KEV-catalog update. CVE-2026-0300 PAN-OS BOD deadline 2026-05-09 EOB also passed; KEV catalog does not publish compliance-status changes.
  - cisa-advisories        # all.xml RSS via fetch_feed — status 200, 30 items in feed total, 0 items in 6h window after since-filter.
  - bleepingcomputer       # RSS via fetch_feed — status 200, last_modified 2026-05-11T09:53:06 GMT (within window from feed-server activity), 1 item in 6h window after since-filter — "TrickMo Android banker adopts TON blockchain for covert comms" (2026-05-11T09:03 UTC = 05:03 EDT in-window, Bill Toulas byline). WebFetch on the article confirmed: ThreatFabric primary research, Trickmo.C variant, NO threat-actor attribution, NO A&D / defense / aerospace, NO CVEs, victim sectors = financial (banking + crypto wallets) in France/Italy/Austria. DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit; commodity Android banker for financial-fraud crowd).
  - securityweek           # RSS via fetch_feed — status 200, last_modified 2026-05-11T09:35:00 GMT (within window from feed-server activity), 4 items in 6h window after since-filter. (1) "Checkmarx Jenkins AST Plugin Compromised in Supply Chain Attack" (Ionut Arghire, 2026-05-11T09:34:55 UTC = 05:34 EDT in-window) — RAW-SIGNALED to raw-2026-05-11-flash-0600-001 below for grader queue (TeamPCP attribution restatement + new operational tooling delivery via Jenkins Marketplace; Trigger 2 fails on restated-attribution rule, Trigger 4 marginal). (2) "Canvas System Is Online After a Cyberattack Disrupted Thousands of Schools" (Associated Press, 2026-05-11T08:35:13 UTC = 04:35 EDT in-window) — Canvas/Instructure incident already in corpus (multiple BleepingComputer + SecurityWeek touches across 2026-05-08 / 09 / 10); ShinyHunters / education sector framing, NO A&D, NO tracked-actor on Archimedes roster. DISCARDED per anti-noise. (3) "New 'Dirty Frag' Linux Vulnerability Possibly Exploited in Attacks" (Eduard Kovacs, 2026-05-11T08:15:28 UTC = 04:15 EDT in-window) — RE-COVERAGE of CVE-2026-43284 / CVE-2026-43500 chain already in corpus (finding-2026-05-08-0005 B2/likely, finding-2026-05-08-0001 morning procedural). WebFetch confirms: Microsoft Defender observed "limited in-the-wild activity that could indicate exploitation"; patches now widely released (Red Hat / Amazon Linux / Ubuntu / Fedora / Alma Linux); same Hyunwoo Kim researcher + Microsoft threat-intel reporting as the 2026-05-08 disclosure. DISCARDED per anti-noise (existing finding covers; no material posture change — patches now available is REDUCTION in Trigger 6 eligibility, not escalation). (4) "Resurrected 'Crimenetwork' Marketplace Taken Down, Administrator Arrested" (Ionut Arghire, 2026-05-11T07:25:12 UTC = 03:25 EDT in-window) — German LE operation already in corpus via 2026-05-10 12:00 FLASH BleepingComputer item (anti-noise applies; cybercrime forum takedown, NO A&D, NO roster actor, NO CVE).
  - the-record             # RSS via fetch_feed — status 200, 5 items total in feed, 0 items in 6h window after since-filter (most recent dated 2026-05-08).
  - krebs                  # RSS via fetch_feed — status 200, last_modified 2026-05-08T15:10:32 GMT pre-window (unchanged), 0 items in 6h window — normal Krebs cadence.
  - mstic                  # RSS via fetch_feed (microsoft.com/en-us/security/blog/feed/) — status 200, last_modified 2026-05-08T23:03:04 GMT pre-window (unchanged across SEVEN consecutive sweeps), 0 items in 6h window. Most recent MSTIC content remains 2026-05-08T17:12 UTC Dirty Frag active-attack post (~85h aged at this sweep).
  - unit42                 # RSS (feedburner) via fetch_feed — status 200, last_modified 2026-05-08T21:09:40 GMT pre-window (unchanged across SIX consecutive sweeps), 0 items in 6h window.
  - sans-isc               # RSS via fetch_feed — status 200, last_modified 2026-05-11T09:59:04 GMT (within window from feed-server activity), 0 items in 6h window after since-filter.
  - rapid7                 # RSS via fetch_feed — status 200, last_modified 2026-05-11T09:46:51 GMT (within window from feed-server activity), 0 items in 6h window after since-filter.
  - crowdstrike            # RSS via fetch_feed — status 200, last_modified 2026-05-11T04:34:55 GMT (within window from feed-server activity), 10 items returned ALL with null published_at (FIFTEENTH consecutive sweep with this dateless marketing pattern). Same pile (Gartner MQ leader, Falcon OverWatch for Defender, Risk Assessments, AI Vuln Discovery podcast, CORDIAL/SNARKY SPIDER product-marketing). No 2026-05-10/11 threat-research content visible.
  - sentinelone-labs       # RSS via fetch_feed — status 200, last_modified 2026-05-08T23:44:58 GMT pre-window (unchanged), 0 items in 6h window.
  - sophos                 # RSS via fetch_feed (news.sophos.com/feed/) — status 200, 9 items total in feed, 0 items in 6h window.
  - eset-welivesecurity    # RSS via fetch_feed — status 200, 100 items total in feed, 0 items in 6h window.
  - hacker-news            # feedburner/TheHackersNews RSS via fetch_feed — status 200, last_modified 2026-05-11T08:55:47 GMT (within window from feed-server activity), 1 item in 6h window — "Fake OpenAI Privacy Filter Repo Hits #1 on Hugging Face, Draws 244K Downloads" (2026-05-11T07:05 UTC = 03:05 EDT in-window). This is a relay of the HiddenLayer research already covered in 2026-05-09 15:30 pre-brief (and discarded then per Mode 1 procedure on no-A&D / no-roster-actor / no-tracked-CVE filter). Anti-noise applies; same Open-OSS/privacy-filter Hugging Face typosquat. DISCARDED.
  - mandiant               # feedburner.com/Mandiant returned 404 (FIFTEENTH consecutive failure); failure_count 13→14. WebFetch on cloud.google.com/blog/topics/threat-intelligence INDEX page top-8 titles unchanged from 2026-05-11 00:00 sweep (UNC6692 Snow Flurries, German Cyber Überfall, BRICKSTORM Defender's Guide, UNC1069 Axios NPM, M-Trends 2026, DarkSword iOS, Ransomware Under Pressure, Proactive Preparation 2026). All previously triangulated as out-of-window. Operator alt-endpoint decision still pending.
  - nvd                    # WebFetch on services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=2026-05-11T04:00:00Z&lastModEndDate=2026-05-11T10:00:00Z for the 6h window. cvssV3Severity=CRITICAL → 0 results. cvssV3Severity=HIGH → 0 results. NVD endpoint healthy and responsive; window is genuinely empty.
  - splunk-archimedes      # tstats over 6h NOT sourcetype=archimedes:* — zero events. Targeted IOC keyword sweep across 8 high-priority tokens (Checkmarx, Jenkins, TeamPCP, Trivy, "Dirty Frag", CVE-2026-43284, CVE-2026-43500, HookedWing) over 24h returned 3 hits — ALL archimedes:operation pipeline self-references (00:00 FLASH sentinel log referencing HookedWing in its raw_signal_files list; 2026-05-10 afternoon brief_published event whose related_vulns includes CVE-2026-43284 + CVE-2026-43500; 2026-05-10 morning brief_published event with same vuln list). Pipeline self-references match the keyword tokens in their JSON payloads but reflect Archimedes' own operational logging, NOT external observations.
  - splunk-defenseclaw     # NOT sourcetype=archimedes:* over 24h returns zero events. THIRTEENTH consecutive sweep with dormant non-archimedes-internal stream pattern across both indexes.
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-cisagov              # STALE since 2026-05-10 12:00 FLASH — three consecutive WinError 10060 nitter.net timeouts. Still under 24h since stale-flip → skipped this sweep; eligible-to-retry after 2026-05-11T12:00 (next noon FLASH).
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted (4 consecutive 404s prior). >24h since stale flip but FLASH-fast scope kept to RSS/vendor/KEV priority feeds; treating as effectively stale until operator alt-pool / direct-X-API decision.
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround in use (arstechnica.com/feed/ root path).
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom (per-repo GHSA fallback path remains productive workaround when triggered; not triggered this sweep)
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (FIFTEENTH consecutive); failure_count 13→14. Held healthy pending operator alt-endpoint decision.
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_sweep_clean, sentinel, quiet_hours_active, checkmarx_jenkins_plugin_teampcp_restatement_non_flash, dirty_frag_re_coverage_anti_noise, kev_unchanged_three_deadlines_passed_or_today, splunk_dormant_13th_consecutive]
flash_triggers_evaluated:
  trigger_1_critical_cve_exploited:
    matched: false
    notes: |
      No new CVSS >= 9.0 with confirmed in-the-wild exploitation from
      A-grade source in the 00:00 EDT → 06:00 EDT (Mon) window.

      CISA KEV catalog full-catalog scan: zero entries with dateAdded
      >= 2026-05-10 or 2026-05-11. Most recent KEV addition remains
      CVE-2026-42208 (BerriAI LiteLLM SQL injection, dueDate 2026-05-11
      = TODAY) — already in corpus, status-carried in the 2026-05-10
      afternoon brief patch-backlog tier. Three KEV-listed CVE deadlines
      have now passed or hit today (CVE-2026-0300 PAN-OS BOD 2026-05-09
      passed; CVE-2026-6973 Ivanti EPMM BOD 2026-05-10 EOB passed;
      CVE-2026-42208 LiteLLM BOD 2026-05-11 = today). KEV catalog does
      not publish compliance-status changes against passed deadlines;
      these will surface in next-day federal-compliance reporting (out
      of Archimedes scope) but no new exploitation signal results from
      the deadline-passage itself.

      NVD lastModStartDate window query 04:00-10:00 UTC: CRITICAL = 0
      results. HIGH = 0 results. Window is genuinely empty (consistent
      with overnight quiet-hours publication cadence).

      SecurityWeek "New 'Dirty Frag' Linux Vulnerability Possibly
      Exploited" article (Eduard Kovacs, in-window 04:15 EDT) RE-COVERS
      CVE-2026-43284 / CVE-2026-43500 chain already in corpus —
      finding-2026-05-08-0005 (B2/likely, MSTIC confirms active
      exploitation) + finding-2026-05-08-0001 (morning procedural
      disclosure). The new SecurityWeek piece does NOT escalate posture:
      patches are NOW WIDELY AVAILABLE (Red Hat / Amazon Linux / Ubuntu
      / Fedora / Alma Linux); Microsoft Defender citation is "limited
      in-the-wild activity that could indicate exploitation" — same
      hedge framing as the 2026-05-08 MSTIC source. Material posture
      MOVES IN THE OTHER DIRECTION (patches available → reduces
      Trigger 6 eligibility, does not escalate Trigger 1). Anti-noise
      applies; same CVE chain.

      Trigger 1 not matched.
  trigger_2_tracked_actor_attribution:
    matched: false
    notes: |
      ONE candidate considered and DISCARDED on the new-attribution
      test.

      SecurityWeek "Checkmarx Jenkins AST Plugin Compromised in
      Supply Chain Attack" (Ionut Arghire, in-window 05:34 EDT):
      - Article attributes the broader Checkmarx compromise chain to
        TWO tracked-adjacent actors:
        (a) TeamPCP (Archimedes roster #001, HIGH threat-level) —
            "accessed Checkmarx repositories in late March via the
            Trivy supply chain attack"
        (b) Lapsus$ (NOT in Archimedes _roster.yaml — Lapsus$ /
            DEV-0537 / Strawberry Tempest is a known cybercriminal
            extortion group, /new-actor candidate if operator wishes
            to formalize) — "publicly released data allegedly stolen
            from company repositories in April"

      Trigger 2 evaluation requires "the attribution is new (not
      re-reporting prior attribution)":
      - TeamPCP-via-Trivy-to-Checkmarx attribution chain is ALREADY
        in Archimedes corpus references:
        * finding-2026-05-08-0008 (RansomHouse/Trellix breach claim):
          line 452 notes "potential connection (unverified) to recent
          supply-chain attacks affecting Checkmarx, Aqua Security,
          Bitwarden" — Checkmarx compromise was already a known prior
          event when finding-0008 was published 2026-05-08
        * finding-2026-05-08-0003 (PCPJack worm framework /
          TeamPCP-displacement claim by SentinelOne): TeamPCP roster
          entry referenced multiple times; TeamPCP's operational
          footprint on cloud-exposed targets discussed at length
        * threats/briefs/_coverage-log.yaml line 2510 references
          "PCPJack operator (hedged: 'could be a former TeamPCP
          operator')" in 2026-05-08 coverage
      - The TeamPCP attribution itself is NOT new — it's a restatement
        of the late-March/April supply-chain compromise chain that has
        been in the threat-intel public record since the original
        Checkmarx disclosure (the Lapsus$ April release was widely
        reported; the TeamPCP-Trivy connection has been covered)
      - What IS new in the SecurityWeek article is the OPERATIONAL
        DETAIL: a malicious version of the Checkmarx Jenkins AST
        plugin was published to the Jenkins Marketplace late last
        week (2026-05-09 Friday), and weekend variants surfaced on
        GitHub through 2026-05-10/11. This is delivery infrastructure
        downstream of the original TeamPCP intrusion — not a new
        attribution to TeamPCP, but a new TTP/tooling instance
        attributable to the existing TeamPCP chain.

      Per FLASH-POLICY Trigger 2 strict reading: "new attribution" =
      first-time naming of a tracked actor for a specific activity.
      The TeamPCP-Checkmarx connection has prior corpus coverage;
      restatement of attribution in a new article does NOT clear the
      new-attribution bar. Trigger 2 NOT MATCHED on strict reading.

      The "new TTP / new tooling" angle (compromised Jenkins plugin
      delivery via Marketplace) is properly evaluated under Trigger 4
      below.

      Trigger 2 not matched.
  trigger_3_first_party_ioc_hit:
    matched: false
    notes: |
      Splunk first-party check across both archimedes and
      defenseclaw_local indexes over 6h window via tstats: zero
      events. Targeted IOC keyword sweep across 8 high-priority
      tokens (Checkmarx, Jenkins, TeamPCP, Trivy, "Dirty Frag",
      CVE-2026-43284, CVE-2026-43500, HookedWing) over 24h returned
      3 hits — ALL archimedes:operation pipeline self-references
      (00:00 FLASH sentinel log referencing HookedWing in its
      raw_signal_files list; 2026-05-10 afternoon brief_published
      event whose related_vulns includes CVE-2026-43284 + CVE-2026-43500;
      2026-05-10 morning brief_published event with same vuln list).
      Pipeline self-references match the keyword tokens in their JSON
      payloads but reflect Archimedes' own operational logging, NOT
      external observations of those indicators in network/host
      telemetry.

      Thirteenth consecutive sweep with dormant non-archimedes-internal
      stream pattern across both indexes. Trigger 3 cannot fire on a
      dormant external-telemetry stream.

      Note: SecurityWeek Checkmarx Jenkins article does NOT include
      specific plugin-IOC indicators (no hash for malicious
      2.0.13-848.v76e89de8a_053 vs legitimate 2.0.13-829.vc72453fa_1c16
      version; no C2 domain; no payload behavior detail). To Splunk-
      hunt for the compromised Jenkins plugin in defenseclaw_local
      telemetry would require retrieving the Checkmarx security
      advisory primary for IOC extraction. Recorded here as a deferred
      grader / operator work item.

      Trigger 3 not matched.
  trigger_4_tracked_actor_ttp_change:
    matched: false
    notes: |
      ONE candidate considered and DISCARDED.

      SecurityWeek Checkmarx Jenkins AST Plugin compromise (in-window
      05:34 EDT) could potentially anchor on TeamPCP's roster entry
      (#001) as new operational delivery infrastructure:
      - "Malicious version of the Jenkins AST plugin published to the
        Jenkins Marketplace" represents NEW DELIVERY CHANNEL for
        TeamPCP's existing footprint (compromised Checkmarx CI/CD
        plugin distributing through legitimate Jenkins Marketplace)
      - Weekend timing (2026-05-09 Friday warning, 2026-05-10/11
        weekend variants on GitHub) is fresh operational tempo
      - Composite source-grade evaluation:
        * SecurityWeek = provisional B (awaiting ratification)
        * Originating disclosure = Checkmarx's own company blog
          + Jenkins Marketplace observation (NOT a Tier-1 threat-
          intel vendor research practice — Checkmarx is the COMPROMISED
          vendor itself, not a third-party threat researcher)
        * Composite grade: B (SecurityWeek relay) of vendor-self-
          disclosure (Checkmarx-as-victim, not Checkmarx-as-researcher)

      FLASH Trigger 4 conditions check:
      - "A/B-grade source": MARGINAL — SecurityWeek B-relay is in
        range; underlying disclosure is vendor-self-disclosure not
        third-party research; net composite hovers B
      - "Clearly attributable to a tracked actor": MARGINAL —
        SecurityWeek attributes the BROADER Checkmarx compromise
        chain to TeamPCP (per the article) but does NOT explicitly
        link the new Jenkins plugin malicious version to TeamPCP
        operators specifically (the article frames it as ongoing
        compromise activity at Checkmarx without naming who
        published the malicious plugin version); attribution
        inference is structural ("Checkmarx is compromised by
        TeamPCP per prior reporting; new malicious plugin emerges
        from Checkmarx's distribution channel; therefore likely
        TeamPCP downstream") not direct
      - "New tooling/targeting/infrastructure class": MARGINAL —
        Jenkins Marketplace as distribution channel for compromised
        CI/CD plugins is operationally interesting but is a
        DOWNSTREAM CONSEQUENCE of the original Checkmarx supply-
        chain compromise (which is already in corpus reference),
        not a NEW TTP-class. Better characterized as "TeamPCP
        chain extends a known supply-chain compromise into a new
        delivery vector" than as "TeamPCP adopts new tooling."
      - Hard Rule 2 attribution discipline: Archimedes does NOT
        originate attribution. SecurityWeek's TeamPCP attribution
        flows from prior third-party reporting; without an A/B-grade
        third-party threat-researcher publication explicitly linking
        the new Jenkins plugin variant to TeamPCP, Archimedes should
        report procedural facts at "per SecurityWeek per prior
        TeamPCP reporting" framing — not promote to FLASH on
        downstream-inference attribution

      Disposition: NOT FLASH-worthy. RAW-SIGNALED as the separate
      file raw-2026-05-11-flash-0600-001-securityweek-checkmarx-
      jenkins-ast-plugin-compromise-non-flash.md for the grader's
      morning-brief queue. The grader can evaluate whether the
      Jenkins Marketplace delivery vector warrants a new finding
      (likely B3 / "roughly even chance" framing on the downstream-
      inference attribution leg, B2 / "likely" on the procedural
      fact that a malicious plugin version is now published).

      Trigger 4 not matched.
  trigger_5_ad_sector_campaign:
    matched: false
    notes: |
      No active multi-victim campaign explicitly targeting A&D or
      watchlist entities surfaced in the 6h window.

      The carryover SecurityWeek HookedWing item from 2026-05-11
      00:00 sweep (raw-2026-05-11-flash-0000-001) is now out-of-window
      for THIS sweep but remains in the grader's morning-brief queue
      for promotion decision; not re-evaluated here.

      The Checkmarx Jenkins plugin item's victim profile is
      "Checkmarx itself + downstream Jenkins users" — supply-chain
      compromise with broad enterprise developer victim base, but
      NO named A&D primes in SecurityWeek's coverage. Trigger 5
      "explicitly targeting aerospace, defense, or watchlist
      companies" condition fails.

      Trigger 5 not matched.
  trigger_6_zero_day_no_patch:
    matched: false
    notes: |
      No new vulnerability disclosed pre-patch with CVSS >= 8.0 or
      widely-deployed-product profile in the 6h window.

      SecurityWeek Dirty Frag re-coverage article (in-window 04:15
      EDT) covers CVE-2026-43284 / CVE-2026-43500 chain ALREADY in
      corpus as finding-2026-05-08-0005 + finding-2026-05-08-0001.
      The new article's material change versus prior coverage is
      that patches are NOW WIDELY AVAILABLE (Red Hat, Amazon Linux,
      Ubuntu, Fedora, Alma Linux) — this MOVES the chain OFF
      Trigger 6 eligibility (Trigger 6 requires pre-patch
      disclosure; the chain is now post-patch on major distros).

      NVD 6h window genuinely empty (zero Critical, zero High).

      No other pre-patch zero-day disclosures surfaced from any
      vendor research source in the 6h window.

      Trigger 6 not matched.
post_evaluation_summary:
  flash_candidates_count: 0
  flash_disposition: nothing_fired
  non_flash_raw_signals_written:
    - raw-2026-05-11-flash-0600-001-securityweek-checkmarx-jenkins-ast-plugin-compromise
  next_action: |
    Per FLASH-POLICY.md anti-noise + quiet-hours rules:
    1. Zero FLASH candidates → orchestrator logs "flash_sweep_clean"
       and exits silently. NO discord post. NO queue file write.
    2. Checkmarx Jenkins AST Plugin raw-signal carries forward to
       the morning brief grader queue alongside the HookedWing
       carryover from 00:00 sweep. Grader has TWO non-FLASH items
       to evaluate for morning-brief promotion (2026-05-11 08:00 EDT):
       (a) HookedWing SOCRadar aviation phishing campaign
           (raw-2026-05-11-flash-0000-001)
       (b) Checkmarx Jenkins AST Plugin compromise / TeamPCP chain
           extension (raw-2026-05-11-flash-0600-001) — TeamPCP roster
           connection makes this the higher-priority of the two for
           grader attention
    3. Source-health.yaml updates for mandiant (failure_count 13->14,
       15th consecutive feedburner 404), all other priority sources
       healthy and responsive. No new stale flips this sweep.
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-09T06:02:00-04:00
---

# FLASH Sweep Sentinel — Clean Sweep (2026-05-11 06:00 EDT, Quiet Hours Active)

**Zero FLASH candidates surfaced this sweep.** One in-window item
required closer analysis — SecurityWeek "Checkmarx Jenkins AST Plugin
Compromised in Supply Chain Attack" (Ionut Arghire, 05:34 EDT in-
window) — evaluated against Trigger 2 (tracked-actor attribution)
and Trigger 4 (tracked-actor TTP change), DISCARDED from both:

- Trigger 2 fails on the new-attribution test: TeamPCP-via-Trivy-
  to-Checkmarx attribution chain is RESTATEMENT of late-March/April
  reporting already in Archimedes corpus references (finding-2026-
  05-08-0008 line 452, finding-2026-05-08-0003 multiple TeamPCP
  references, briefs/_coverage-log.yaml 2026-05-08 coverage)
- Trigger 4 fails on composite source-grade + attribution-inference
  marginality: SecurityWeek (provisional B relay) of Checkmarx vendor-
  self-disclosure (NOT third-party threat-intel research); attribution
  to TeamPCP for the new Jenkins plugin malicious version is structural-
  inference downstream of the prior Checkmarx compromise, not direct
  research-vendor attribution; Hard Rule 2 requires per-source framing
  not FLASH-elevation on downstream-inference attribution

Raw-signaled separately as raw-2026-05-11-flash-0600-001 for grader's
morning-brief queue alongside the HookedWing carryover from 00:00.

## Window summary

- **Time window:** 2026-05-11T00:00 → 2026-05-11T06:00 EDT (6h)
- **Quiet hours status:** ACTIVE (current local time 06:00 EDT,
  inside 21:00-09:00 EDT quiet window) — even if a FLASH had fired,
  it would have queued to flash-queue.yaml rather than posted to
  Discord directly. Per FLASH-POLICY.md, the "actually wake up"
  override (CVSS 10.0 + active exploitation + tracked actor +
  A&D watchlist entity) is the only path to immediate-post during
  quiet hours; none of these four conditions co-occurred this sweep.
- **Sources queried (healthy):** 22 (RSS feeds + KEV JSON + NVD
  REST + Mandiant index-page workaround + Splunk x2)
- **Sources skipped stale (24h-rule):** 3 (x-cisagov nitter pool,
  x-gossithedog nitter delist, ars-security feeds path) plus
  4 MCP-missing / API-key-missing / WAF-blocked (censys, urlscan,
  hibp, iran-monitor)
- **Sources soft-failing this sweep:** 0 fresh (3 carryover —
  threatfox, malwarebazaar, github-advisories continue
  carry-forward pending MCP build / endpoint workaround)
- **Sources recovered this sweep:** none new (sophos / proofpoint /
  sans-isc all stable from 2026-05-11 00:00 recovery)

## Trigger evaluation — all six triggers FAILED

| # | Trigger | Result | Driver |
|---|---|---|---|
| 1 | Critical CVE exploited | FAIL | No new KEV entries 2026-05-09+; NVD window empty; Dirty Frag re-coverage moves CVE chain OFF Trigger 6 eligibility (patches now widely available) |
| 2 | Tracked-actor attribution | FAIL | Checkmarx Jenkins article restates prior TeamPCP-Trivy-Checkmarx attribution already in corpus; new-attribution test fails |
| 3 | First-party IOC hit | FAIL | Splunk dormant on non-archimedes-internal stream (THIRTEENTH consecutive) |
| 4 | Tracked-actor TTP change | MARGINAL → FAIL | Jenkins Marketplace delivery vector is downstream of prior Checkmarx compromise, not new tooling-class; composite source-grade marginal (SecurityWeek B-relay of vendor-self-disclosure, not third-party research) |
| 5 | A&D-sector campaign | FAIL | No fresh A&D campaign with named primes; Checkmarx victim profile is broad enterprise developer base, no named A&D primes |
| 6 | Zero-day no patch | FAIL | Dirty Frag re-coverage notes patches NOW WIDELY AVAILABLE; NVD window empty |

## SecurityWeek "Checkmarx Jenkins AST Plugin Compromise" disposition

The one in-window item with TeamPCP roster proximity warranted
careful analysis. Recording the full reasoning trail so the grader
can pick up cleanly:

- **Article:** SecurityWeek (Ionut Arghire byline, 2026-05-11T09:34:55
  UTC = 05:34 EDT in-window, provisional B grade)
- **Originating disclosure:** Checkmarx company blog + Jenkins
  Marketplace observation (Checkmarx is the COMPROMISED vendor, not
  a third-party threat researcher)
- **Attribution chain (per article):**
  - Late March 2026: TeamPCP (Archimedes roster #001, HIGH threat
    level) "accessed Checkmarx repositories via the Trivy supply
    chain attack" — RESTATEMENT of prior late-March/April reporting
  - April 2026: Lapsus$ (NOT in Archimedes _roster.yaml; /new-actor
    candidate if operator wishes) "publicly released data allegedly
    stolen from company repositories"
  - May 9-11, 2026: Malicious Checkmarx Jenkins AST plugin version
    published to Jenkins Marketplace late last week (Friday warning);
    weekend variants on GitHub + Marketplace — NEW operational
    DELIVERY-VECTOR detail downstream of the prior compromise
- **IOCs in article:** NONE (no malicious-version hash, no C2
  domain, no payload behavior; legitimate version cited as
  2.0.13-829.vc72453fa_1c16 from December 2025; weekend remediation
  version is 2.0.13-848.v76e89de8a_053)
- **CVEs:** none mentioned
- **A&D relevance:** STRUCTURAL — Jenkins is widely deployed in
  enterprise CI/CD environments including A&D contractors (DevSecOps
  pipelines for software-defined systems, mission software, satellite
  ground software, etc.), but the SecurityWeek article names no A&D
  primes among compromised/exposed organizations; "downstream Jenkins
  users" is the implied victim base. A&D-relevance is therefore
  CAPABILITY-LEVEL (CI/CD plugin compromise = A&D-relevant attack
  surface) but not TARGETING-LEVEL (no named A&D victim)
- **Hard Rule 2 compliance:** SecurityWeek's TeamPCP attribution
  derives from prior third-party reporting (not first-time attribution
  in this piece); Archimedes does NOT originate attribution. The
  grader should report "per SecurityWeek per prior TeamPCP/Trivy/
  Checkmarx reporting" framing, not promote to FLASH on downstream-
  inference attribution
- **FLASH eligibility:** Trigger 2 FAILS (restatement); Trigger 4
  FAILS (marginal composite source-grade + attribution-inference
  rather than direct research-vendor attribution). Raw-signaled
  separately as a non-FLASH grader-queue item for the 08:00 morning
  brief inheritance

## SecurityWeek "Dirty Frag" re-coverage disposition

Anti-noise applies — Eduard Kovacs's 04:15 EDT piece re-covers
CVE-2026-43284 / CVE-2026-43500 chain already in corpus as
finding-2026-05-08-0005 (B2/likely; MSTIC confirms active
exploitation) + finding-2026-05-08-0001 (morning procedural).
Material change versus prior coverage: patches are NOW WIDELY
AVAILABLE on major distros (Red Hat, Amazon Linux, Ubuntu, Fedora,
Alma Linux). This MOVES the chain OFF Trigger 6 eligibility (which
requires pre-patch disclosure) rather than ESCALATING Trigger 1
posture. Microsoft Defender citation in the new article is the
SAME "limited in-the-wild activity that could indicate exploitation"
hedge framing as the 2026-05-08 MSTIC disclosure. No material
posture change requiring fresh raw-signal or FLASH.

The 72h second-vendor corroboration tripwire that was carried in
the 2026-05-10 afternoon brief patch-backlog tier (finding-2026-
05-08-0005 dirty_frag_72h_second_vendor with 10 remaining hours at
the time of the 2026-05-10 16:20 EDT publish) expired without
independent A/B-grade vendor research surfacing in the interim
(SecurityWeek is the only fresh touch and is a relay of the same
MSTIC + Hyunwoo Kim sourcing already in corpus). The tripwire's
status (whether the supersession to lower WEP fires) is a grader
disposition decision for the morning brief, not a FLASH event.

## SecurityWeek other in-window items dispositioned

| Item | In-window time | Disposition | Reason |
|---|---|---|---|
| Canvas System back online (AP) | 04:35 EDT | DISCARDED | Education-sector recovery; ShinyHunters framing already in corpus across 2026-05-08/09/10; NO A&D, NO roster actor |
| Crimenetwork takedown | 03:25 EDT | DISCARDED | German LE op already in corpus via 2026-05-10 12:00 FLASH BleepingComputer item; anti-noise applies |

## Source-health observations (this sweep)

**Continuing carry-forward (no change this sweep):**
- `mandiant` — feedburner.com/Mandiant 404 FIFTEENTH consecutive;
  alt cloud.google.com endpoints malformed/non-parseable.
  index-page WebFetch remains the workaround for title-surfacing.
  failure_count 13 → 14.
- `crowdstrike` — fifteenth consecutive sweep with dateless-
  marketing pattern (10 items, all null published_at).
- `x-cisagov`, `x-gossithedog`, `ars-security` — same blockers as
  prior sweeps.
- `threatfox`, `malwarebazaar`, `github-advisories`,
  `iran-monitor` — same MCP-pending / endpoint-broken / WAF-blocked
  blockers; per-repo GHSA fallback for github-advisories remains
  productive workaround (not triggered this sweep).

## Anti-noise check

Per FLASH-POLICY rule 1 (one FLASH per trigger topic per 24h):
- Zero FLASH candidates this sweep → no anti-noise dedup needed for
  trigger-level dedup
- Checkmarx Jenkins item: grep on threats/ tree confirms "Jenkins AST"
  has ZERO prior occurrences in raw-signal/findings/briefs; the
  PLUGIN-specific compromise is brand-new to the corpus. The
  TeamPCP-Trivy-Checkmarx ATTRIBUTION CHAIN has prior corpus
  references (finding-2026-05-08-0008 line 452, finding-2026-05-08-0003
  multiple TeamPCP references) — the attribution leg is restated, the
  operational/delivery leg is new. Distinguishing these is important
  for the grader.
- Dirty Frag re-coverage: existing findings 0001 + 0005 cover the
  chain; SecurityWeek piece adds no material posture change. Strong
  anti-noise applies; not re-raw-signaled.

## Quiet hours posture

Current local time 06:00 EDT falls inside the 21:00-09:00 EDT
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

Next FLASH sweep: 2026-05-11 12:00 EDT (~6 hours). Quiet hours
end 09:00 EDT; the 07:30 pre-brief and 08:00 morning brief
sit between this sweep and the noon FLASH. The morning brief
grader inherits TWO non-FLASH raw-signal items from this overnight
period:
1. raw-2026-05-11-flash-0000-001-securityweek-hookedwing-socradar-aviation
   (HookedWing aviation-sector phishing campaign, no named primes,
   SOCRadar provisional-C grade, marginal Trigger 5)
2. raw-2026-05-11-flash-0600-001-securityweek-checkmarx-jenkins-ast-plugin-compromise
   (Checkmarx Jenkins plugin compromise, TeamPCP roster #001
   attribution chain restated, marginal Trigger 4)

Both warrant grader-queue attention for the morning brief; neither
cleared FLASH thresholds.
