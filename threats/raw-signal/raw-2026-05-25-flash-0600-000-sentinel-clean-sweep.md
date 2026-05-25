---
raw_id: raw-2026-05-25-flash-0600-000-sentinel-clean-sweep
collected_at: 2026-05-25T06:05:00-04:00
run_id: flash-sweep-20260525-060000
collection_mode: flash_sweep
sentinel: true
flash_candidate: false
test: false
sweep_type: flash-0600
status: complete
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel (06:00 EDT Monday-early FLASH sweep — 0 of 6 triggers fired, clean sweep; 3 in-window items surfaced but all evaluated NOT-FLASH-TIER)"
  source_url: null
  published_at: 2026-05-25T06:05:00-04:00
sweep_window:
  start: 2026-05-25T00:00:00-04:00
  end: 2026-05-25T06:00:00-04:00
  duration_h: 6
quiet_hours_status: quiet_hours_active    # 06:05 EDT is INSIDE 21:00-09:00 quiet window. Any FLASH-trigger fire would queue to flash-queue.yaml (catchup 09:00 EDT), UNLESS critical-override conditions all four simultaneously met. Zero fired makes this moot.
prior_sweep_anchor:
  brief_id: flash-2026-05-25-0000-canonical-scheduled-clean-sweep
  shipped_at: 2026-05-25T00:05:00-04:00
  trigger: none_fired
  notes: |
    Prior sweep was the 2026-05-25 00:00 EDT Monday-cadence-open clean
    sentinel (commit 2742c67). Monday cadence started clean — this 06:00
    sweep examines the 00:00 → 06:00 EDT window for net-new triggers.
flash_candidates_summary:
  count: 0
  candidates: []
in_window_items_evaluated:
  - item_id: thn-trapdoor-relay-of-socket
    source: thehackernews
    source_grade: B
    title: "TrapDoor Supply Chain Attack Spreads Credential-Stealing Malware via npm, PyPI, and CratesIO"
    url: "https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html"
    published: 2026-05-25T05:59:13+00:00
    in_window: true
    relevance_class: corpus_already_tracked_anti_noise_locked
    trigger_evaluation: NOT_FLASH_TIER
    trigger_evaluation_detail: |
      THN article is a B-grade relay of Socket's prior TrapDoor disclosure
      (corpus-tracked via finding-2026-05-24-0001 + brief 2026-05-24-afternoon
      commit 0774f79). Anti-noise lock trapdoor-multi-ecosystem-supply-chain-socket
      ACTIVE through 2026-05-25T16:00:00-04:00 — anti-noise rule 1 (one FLASH per
      topic per 24h) explicitly applies; absorbs as UPDATE flag at most into
      next scheduled brief. THN adds modest contextual analysis (`.cursorrules` /
      `CLAUDE.md` AI-agent-config manipulation framing, named GitHub-PR targets
      browser-use/browser-use, langchain-ai/langchain, langflow-ai/langflow,
      and ddjidd564.github[.]io GitHub Pages exfil endpoint detail) but provides
      NO additional file hashes, NO additional C2 domains beyond the GitHub Pages
      endpoint, NO IP IOCs, NO actor attribution. Socket remains UNATTRIBUTED;
      THN does not attribute. THN also explicitly disambiguates this TrapDoor
      from a separate Android ad-fraud campaign of the same name disclosed by
      HUMAN's Satori team the prior week. Trigger evaluations: T1 fail (no CVE),
      T2 fail (no actor attribution), T3 N/A (no Splunk hit hypothesis), T4 fail
      (no tracked actor), T5 fail (no A&D-prime named; structural-indirect via
      AI-agent-tooling ubiquity in SDLC; aligns with PM brief framing), T6 fail
      (not a vulnerability disclosure). Disposition: 07:30 morning collection
      should capture this as TrapDoor UPDATE under existing anti-noise lock.
  - item_id: securityweek-megalodon-relay-of-safedep
    source: securityweek
    source_grade: B
    title: "Over 5,500 GitHub Repositories Infected in 'Megalodon' Supply Chain Attack"
    url: "https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/"
    published: 2026-05-25T07:40:55+00:00      # = 03:40 EDT IN-WINDOW
    in_window: true
    relevance_class: net_new_to_corpus_but_not_flash_tier
    trigger_evaluation: NOT_FLASH_TIER
    trigger_evaluation_detail: |
      Megalodon is NEW to corpus. SafeDep primary research published 2026-05-21
      (4d ago — previously missed by Archimedes sweeps; documented as
      collection gap in this sentinel). SecurityWeek (Ionut Arghire) is the
      in-window relay at 2026-05-25 03:40 EDT. Direct retrieval of SafeDep
      blog post `/megalodon-mass-github-repo-backdooring-ci-workflows`
      confirms: 5,718 malicious commits across 5,561 GitHub repositories
      injected 2026-05-18 11:36-17:48 UTC via `workflow_dispatch` GitHub
      Actions anti-recursion bypass; @tiledesk/tiledesk-server npm packages
      2.18.6-2.18.12 published 2026-05-19 through 2026-05-21 by legitimate
      maintainer `eljohnny` from poisoned source-of-truth; C2 endpoint
      216.126.225.129:8443; throwaway GitHub accounts using author identity
      spoofs (build-bot, auto-ci, ci-bot, pipeline-bot patterns).
      Attribution: SafeDep explicitly UNATTRIBUTED — "No attribution made"
      to any tracked actor, no nation-state attribution attempted or
      disclaimed. SecurityWeek does NOT attribute. No A&D primes named. No
      CISA / US-CERT engagement mentioned. No CVE assigned. SafeDep cross-
      references "Mini Shai-Hulud Strikes Again: 314 npm Packages
      Compromised" (their own 2026-05-19 post) but provides NO technical
      lineage connection in body — relationship between Megalodon and the
      ShaiWorm family / TeamPCP lineage is structurally plausible but
      UNESTABLISHED by SafeDep.
      Trigger evaluations: T1 fail (no CVE / not vulnerability disclosure),
      T2 fail (no tracked-actor attribution — same logic that blocked
      prior unattributed supply-chain mass-compromise FLASHes: TrapDoor PM
      finding 2026-05-24-0001 stayed off FLASH-tier on Socket-unattributed
      grounds), T3 N/A (Splunk first-party first-pass next), T4 fail (no
      tracked actor; build-bot author-identity-spoofing is technique class
      already documented in TeamPCP TTP catalog, not actor-distinctive),
      T5 multi-victim YES (5,561 repos) but A&D-direct FAIL (no A&D-prime
      named; structural-indirect via developer-ecosystem ubiquity = same
      calculus as Mini Shai-Hulud, TrapDoor, art-template, durabletask),
      T6 fail (not a vulnerability; abuse-of-feature on GitHub Actions
      workflow_dispatch anti-recursion behavior, which GitHub considers
      intended-by-design per SafeDep framing).
      Disposition: 07:30 morning collection MUST capture this as fresh
      finding candidate. Strong morning-brief content: documents a
      novel-class GitHub Actions workflow_dispatch anti-recursion abuse
      pattern that materially expands the supply-chain attack toolkit
      visible across the 2026-Q2 wave (Mini Shai-Hulud, TrapDoor,
      Megalodon, durabletask all in a 7-day cluster). Strong candidate
      for inclusion in morning brief as standalone finding-tier item.
      Build-bot / auto-ci / ci-bot author-identity-spoofing pattern
      diagnostically links across multiple recent unattributed waves
      (cross-corpus author-naming-convention repeat with TeamPCP's
      claude@users.noreply.github.com pattern flagged for actor-profiler
      review on next /update-tracking cycle).
      ANTI-NOISE: distinct topic from TrapDoor (Socket) and distinct
      mechanism — Megalodon is GitHub Actions workflow_dispatch abuse,
      TrapDoor is multi-ecosystem package publication. NOT lock-collision.
      But still NOT FLASH-tier — no tracked actor, no A&D-direct, no CVE.
  - item_id: securityweek-docketwise-data-breach
    source: securityweek
    source_grade: B
    title: "DocketWise Data Breach Impacts 143,000"
    url: "https://www.securityweek.com/docketwise-data-breach-impacts-143000/"
    published: 2026-05-25T09:37:27+00:00      # = 05:37 EDT IN-WINDOW (just inside the 06:00 cutoff)
    in_window: true
    relevance_class: out_of_scope_legal_sector_no_actor_no_a_and_d
    trigger_evaluation: NOT_FLASH_TIER
    trigger_evaluation_detail: |
      DocketWise is an immigration / legal case management platform. The
      breach is a third-party supply-chain incident — threat actor cloned
      third-party partner repositories using valid credentials and accessed
      143,480 individuals' PII (SSN, DOB, financial accounts, driver's
      license, passport, health insurance, medical condition data). NO
      threat-actor attribution. NO tracked APT or cybercrime group named.
      NO CVE involved. NOT A&D / defense sector. Disclosure timeline:
      investigation launched October 2025; initial notification early April;
      updated filing 2026-05-25 brings total to 143,480 (was 116,000).
      Trigger evaluations: T1 fail (no CVE), T2 fail (no actor), T3 N/A,
      T4 fail (no tracked actor), T5 fail (legal sector, not A&D, no
      watchlist entity), T6 fail (no vulnerability disclosure).
      Disposition: NOT morning-brief-tier either. Standard third-party
      legal-sector PII breach update. Mention only if morning brief has
      a "compliance / breach disclosure landscape" angle (typically does
      not). Skip from finding queue.
in_window_items_evaluated_notes: |
  THREE in-window items surfaced — first non-zero in-window item count
  across the prior five consecutive scheduled FLASH sweeps (Sunday 00:00 /
  06:00 / 12:00 / 18:00 + Monday 00:00). Sunday-quiet baseline does NOT
  hold into the Monday early-hours window. However, ZERO of the three
  items fire any FLASH trigger:
    - THN/TrapDoor is corpus-already-tracked anti-noise-locked relay
      (absorbs into morning UPDATE flag)
    - SW/Megalodon is fresh-to-corpus and substantive but UNATTRIBUTED
      (no tracked actor) and not A&D-direct (no prime named)
    - SW/DocketWise is out-of-scope legal sector with no actor / no CVE
  All three are properly morning-brief / regular-cadence content.
  Megalodon is the highest-priority pickup for 07:30 collection.
anti_noise_locks_evaluated:
  - lock_id: trapdoor-multi-ecosystem-supply-chain-socket
    locked_until: 2026-05-25T16:00:00-04:00
    lock_state_at_sweep: active_10h_remaining
    sweep_observation: |
      Lock active through 2026-05-25 16:00 EDT (10h remaining). THN's
      2026-05-25 01:59 EDT article exercised the lock — explicitly
      classified as UPDATE-flag absorption, NOT re-FLASH. Lock prevents
      a Trigger-5 re-fire on the multi-ecosystem-supply-chain topic-
      category during this window. Socket's 2026-05-24 17:29 EDT post-
      window @SocketSecurity follow-up on modelcontextprotocol /
      gemini-cli upstream-injection claim (carry-forward from prior
      two sentinels) still held for 07:30 morning collection.
  - lock_id: unc1549-screening-serpens-tradecraft-evolution
    locked_until: 2026-05-24T06:00:00-04:00
    lock_state_at_sweep: expired_48h_ago
    sweep_observation: |
      Lock expired 48h before window start. No fresh Unit 42 / Mandiant /
      MSTIC / CrowdStrike UNC1549 content in window. Surface remains
      fully open for re-FLASH if any new tradecraft material surfaces.
      Zero pressure this sweep.
  - lock_id: litespeed-cpanel-plugin-cve-2026-48172-lsws-redisAble-root-rce
    locked_until: 2026-05-24T06:00:00-04:00
    lock_state_at_sweep: expired_48h_ago
    sweep_observation: |
      CISA KEV catalog version 2026.05.22 UNCHANGED (CVE-2026-48172 NOT
      added; 66h+ since the last KEV add). No second-vendor independent
      corroboration. No new LiteSpeed-blog post in window (litespeed-blog
      feed last_modified 2026-05-21 15:04 UTC). Re-fire would require
      fresh KEV addition OR independent IR-firm telemetry; neither
      materialized.
  - lock_id: cve-2024-12802-sonicwall-mfa-bypass-itw-reliaquest
    locked_until: 2026-05-21T18:00:00-04:00
    lock_state_at_sweep: expired_4d_ago
    sweep_observation: |
      Lock expired 4 days ago. No SonicWall CVE-2024-12802 fresh surface
      in window. SonicWall PSIRT silent across all recent sweeps.
  - lock_id: cve-2026-9082-drupal-itw-status-change
    locked_until: 2026-05-24T06:00:00-04:00
    lock_state_at_sweep: expired_48h_ago
    sweep_observation: |
      CISA KEV catalog version 2026.05.22 UNCHANGED — 66h+ since
      CVE-2026-9082 added. KEV due-date 2026-05-27 = T-2 from this sweep
      (Wednesday end-of-business, less than 54h away). No fresh Drupal
      SA-CORE content in window. Status quo; carries into 2026-05-25
      morning brief KEV-action-item block at elevated urgency tier.
  - lock_id: cve-2026-42897-exchange-ga-patch-itw-corroboration
    locked_until: 2026-05-24T06:00:00-04:00
    lock_state_at_sweep: expired_48h_ago
    sweep_observation: |
      No MSRC GA patch released in window. MSRC blog continues
      redirect-to-microsoft.com pattern; parent MSTIC feed
      last_modified 2026-05-22 17:57 UTC — no fresh post. ESU + EEMS /
      EOMT mitigation path unchanged. Active-exploitation single-source
      veto on MSRC "Exploitation Detected" tag still holds. KEV
      due-date 2026-05-29 = T-4 from this sweep.
sources_queried:
  - cisa-kev                # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.22 UNCHANGED, dateReleased 2026-05-22T18:00:11.5035Z. Only entry dateAdded >= 2026-05-22 is CVE-2026-9082 Drupal (already corpus-locked, T-2). VT-008 Exchange CVE-2026-42897 KEV due-date 2026-05-29 = T-4. ZERO net-new KEV entries in 66h+.
  - cisa-advisories         # fetch_feed cisa.gov/cybersecurity-advisories/all.xml — 200 OK, 30 items in feed, 0 in 6h since-filter window.
  - thehackernews           # fetch_feed feedburner — 50 items in feed, 1 item_after_since_filter (TrapDoor relay) — evaluated NOT_FLASH_TIER per anti-noise lock. Feed last_modified 2026-05-25 09:15:52 GMT = 05:15 EDT.
  - bleepingcomputer        # fetch_feed — 15 items in feed, 0 items in 6h since-filter window. Feed last_modified 2026-05-25 09:55:13 GMT = 05:55 EDT.
  - securityweek            # fetch_feed feedburner — 10 items, 2 in window: Megalodon (03:40 EDT) + DocketWise (05:37 EDT). Both evaluated NOT_FLASH_TIER per trigger logic; Megalodon strong morning candidate, DocketWise skip-from-finding-queue.
  - the-record              # fetch_feed therecord.media/feed/ — 5 items in feed, 0 in window.
  - unit42                  # fetch_feed feedburner — 15 items, 0 in window. Last update 2026-05-22 19:51:29 GMT (3d pre-window).
  - mstic                   # fetch_feed microsoft.com/en-us/security/blog/feed — 10 items, 0 in window. Last update 2026-05-22 17:57 UTC.
  - isc-sans                # fetch_feed isc.sans.edu/rssfeed.xml — 10 items, 0 in 6h window. Feed last_modified 2026-05-25 09:59:07 GMT (server-activity inside window; in-feed item-timestamps pre-window).
  - eset-welivesecurity     # fetch_feed welivesecurity.com — 100 items in feed, 0 in window.
  - rapid7                  # fetch_feed — 20 items in feed, 0 in window. Feed last_modified 2026-05-25 09:47:03 GMT (server-activity inside window; in-feed items pre-window).
  - sentinelone             # fetch_feed sentinelone.com/labs/feed — 10 items, 0 in window. Feed last_modified 2026-05-22 17:44 UTC (3d pre-window).
  - cisco-talos             # fetch_feed feedburner — 15 items in feed, 0 in window. Feed last_modified 2026-05-21 18:57 UTC. WebFetch blog.talosintelligence.com index corroborates: most recent post 2026-05-21 ("The art of being ungovernable"); no posts dated 2026-05-24 or 2026-05-25.
  - mandiant-index          # NOT re-fetched this sweep — cloud.google.com top-5 unchanged across prior 6 sweeps per established pattern; feedburner 404 streak entering its 22nd consecutive failure since 2026-05-05. Held healthy pending operator alt-endpoint decision.
  - socket-dev              # WebFetch socket.dev/blog — top 5 dated posts unchanged from 00:00 sentinel: 2026-05-23 Laravel-Lang, 2026-05-22 Postinstall Hook GitHub 700+ repos, 2026-05-22 "AI Has Taken Over Open Source", 2026-05-21 npm Granular Access Token invalidation, 2026-05-20 Coruna Respawned art-template iOS. All pre-window. TrapDoor remains undated featured top item (corpus-covered, anti-noise lock active 10h remaining).
  - safedep                 # WebFetch safedep.io/blog — DIRECT RETRIEVAL of Megalodon primary research (2026-05-21 publication, missed by prior Archimedes sweeps); used to substantiate SecurityWeek relay this sweep. Top 5: Megalodon (2026-05-21), Polymarket npm (2026-05-21), durabletask PyPI (2026-05-20), art-template (2026-05-20), Mini Shai-Hulud 317 packages (2026-05-19). All pre-window for original publication but Megalodon emergence into B-grade media wave (SecurityWeek 03:40 EDT) makes it the operational in-window pickup. Recommend operator add safedep.io to source-grades.yaml — vendor research with code/IOC depth comparable to Socket / Snyk / StepSecurity tier; tentative B-grade pending source-health validation.
  - crowdstrike-blog        # fetch_feed — 10 items returned (no published dates so all pass since-filter). Inspection: all corporate / marketing posts (Q2 Patch Tuesday analysis from 2 weeks ago, Falcon AIDR launches, financial-services threat report). NONE attribute to tracked actor; NONE document new TTPs. Zero FLASH-trigger relevance.
  - research-checkpoint     # fetch_feed research.checkpoint.com/feed — 15 items, 0 in window. Last update 2026-05-22 18:22 UTC.
  - sophos-threat-research  # fetch_feed news.sophos.com/en-us/category/threat-research/feed — 15 items, 0 in window.
  - krebs                   # fetch_feed krebsonsecurity.com/feed/ — 10 items, 0 in window. Last update 2026-05-22 21:18 UTC.
  - dark-reading            # fetch_feed darkreading.com/rss.xml — 50 items, 2 in window per persistent defensive-null-published behavior: both are forward-dated event listings (Infosecurity Europe 2026-06-02; Anatomy of a Data Breach virtual event 2026-06-18). NOT threat-intelligence content; NOT trigger-eligible.
  - litespeed-blog          # fetch_feed blog.litespeedtech.com/feed/ — 9 items in feed, 0 in window. Last update 2026-05-21 15:04 UTC.
  - nvd                     # WebFetch lastModStartDate=2026-05-25T00:00 lastModEndDate=2026-05-25T06:00 cvssV3Severity=CRITICAL — totalResults=5 but results page returned empty (NVD API result-pagination quirk; retried with resultsPerPage=20, same empty body). totalResults=5 in 6h window is non-trivial but the lack of resolvable CVE bodies means none can be triggered-evaluated this sweep. Carry-forward to 07:30 morning collection — pull NVD batch with explicit resultsPerPage and walk-paginate to inventory the 5 critical CVEs by ID. NONE of the unknown-ID CVEs are corpus-anchored at this sweep, and the API-quirk-induced opacity means none can fire Trigger 1 or Trigger 6 without ID resolution.
  - splunk-archimedes       # mcp__splunk-query | tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index → 30 events all in archimedes index (operation + scheduler self-telemetry). Splunk reachability HEALTHY.
  - splunk-defenseclaw      # Same query, plus targeted search index=defenseclaw_local earliest=-24h@h latest=now | head 10 → zero events. 55th CONSECUTIVE DORMANT non-self sweep.
sources_querying_skipped_or_deferred:
  - aikido                  # not re-tested this sweep — second consecutive sweep failure documented in prior 00:00 sentinel; FLASH-narrow scope held. If 07:30 AM pre-brief hits same failure mode, that's the third consecutive and librarian should formally mark stale.
  - volexity                # same — second consecutive sweep failure documented; third strike at 07:30 if pattern continues.
  - fortinet-psirt          # not re-tested this sweep (transient SSL hostname-mismatch in 18:00 sweep). Retry at 07:30.
  - proofpoint-threat-insight  # endpoint 404 in 18:00 sweep; not re-tested. Retry at 07:30.
  - checkpoint-blog         # endpoint 404 in 18:00 sweep; covered via research.checkpoint.com proxy this sweep.
  - cisco-psirt             # template-only render pattern persistent — skipped this sweep
  - msrc-blog               # not re-fetched (parent MSTIC feed already queried; persistent redirect pattern)
  - palo-alto-psirt         # sample-sweep cadence
  - ivanti-psirt            # same
  - citrix-psirt            # same
  - sonicwall-psirt         # same
  - vmware-broadcom-psirt   # same
  - shodan                  # not queried — no investigation hypothesis warrants paid-tier query
  - virustotal              # not queried this sweep — no fresh-IOC trigger event. Megalodon C2 IP 216.126.225.129 candidate for 07:30 collection enrichment.
splunk_first_party_check:
  query_a: "| tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index"
  query_b: "search index=defenseclaw_local earliest=-24h@h latest=now | head 10"
  archimedes_index_events_24h: 30          # self-telemetry only (operation + scheduler)
  defenseclaw_local_events_24h: 0
  splunk_first_party_dormant: true
  consecutive_dormant_sweeps: 55           # increments prior 54
  ioc_match_opportunity: false
  hard_rule_8_framing: |
    Silence is not disconfirming, not confirming. First-party
    defenseclaw_local index dormant non-self pattern continues
    (55th consecutive sweep). No tracked IOC published in window
    that warranted a targeted hand-built query beyond the residual
    24h sweep. Megalodon C2 IP 216.126.225.129 is fresh-corpus-
    candidate — would be reasonable target for a hand-built
    Splunk query at 07:30 morning collection if morning grader
    promotes Megalodon to finding-tier.
flash_trigger_evaluation:
  - trigger_id: trigger-1-critical-cve-exploited
    fired: false
    evaluation: |
      Required: CVSS >= 9.0 + confirmed active exploitation + A-grade
      source. ZERO new CVE disclosures with active-exploitation claim
      in window. CISA KEV catalog unchanged across 66h+ (catalogVersion
      2026.05.22). NVD lastModified critical query returned totalResults=5
      but API result-pagination quirk left bodies empty — none can be
      trigger-evaluated this sweep. The 5 unknown-ID critical CVEs in
      6h window is non-trivial but cannot fire Trigger 1 without ID
      resolution; carry-forward to 07:30 morning collection for
      paginate-and-inventory. KEV anti-noise locks on CVE-2026-9082
      (Drupal, T-2) and CVE-2026-42897 (Exchange, T-4) keep those
      topics in absorption rather than re-fire; no fresh fact pattern
      surfaced for either in window.
  - trigger_id: trigger-2-tracked-actor-attribution
    fired: false
    evaluation: |
      Required: new attribution to one of 24 tracked actors in
      _roster.yaml. ZERO new attribution surfaces in window. No
      Mandiant / Unit 42 / MSTIC / CrowdStrike / SentinelOne / ESET /
      Talos / Volexity / Check Point fresh post on a tracked actor.
      Hard Rule 2 prevents Archimedes-originated attribution. Megalodon
      (SafeDep + SecurityWeek) explicitly UNATTRIBUTED — neither source
      names a tracked actor; build-bot / auto-ci author-identity-spoofing
      pattern resembles TeamPCP TTP cataloging but is NOT
      actor-distinctive (the technique is portable post-access). TrapDoor
      (Socket + THN) explicitly UNATTRIBUTED at corpus baseline.
      TeamPCP, GlassWorm, Charming Kitten, Lazarus, Salt Typhoon, Volt
      Typhoon, APT28/29/37/40/41, MuddyWater, APT34, UNC1549 etc. all
      silent in window from primary research feeds.
  - trigger_id: trigger-3-first-party-ioc-hit
    fired: false
    evaluation: |
      Required: Splunk match on tracked IOC within last 24h.
      defenseclaw_local index dormant (0 events in -24h@h, 55th
      consecutive sweep) — IOC-match opportunity structurally zero.
      Hard Rule 8: silence is not disconfirming. No fresh tracked IOC
      published since the PM brief that would warrant a targeted hand-
      built query at the 06:00 cutoff. Megalodon C2 IP 216.126.225.129
      is candidate for 07:30 hand-built Splunk query if morning grader
      promotes Megalodon to finding-tier.
  - trigger_id: trigger-4-tracked-actor-ttp-change
    fired: false
    evaluation: |
      Required: new tooling / targeting / infrastructure documented +
      A/B-grade source + attributable to tracked actor. ZERO new TTP
      documentation surface attributable to any of the 24 tracked
      actors in window. Megalodon's workflow_dispatch anti-recursion
      bypass IS a substantive new TTP-class observation but is
      UNATTRIBUTED at primary source (SafeDep does not link to any
      tracked actor or known cluster). Without attribution, Trigger 4
      cannot fire — it's catalog content for the analyst's broader
      "AI-coding-agent abuse + supply-chain mass-compromise" TTP
      tracker, not a tracked-actor TTP-change FLASH.
  - trigger_id: trigger-5-ad-sector-campaign
    fired: false
    evaluation: |
      Required: active campaign + targets aerospace/defense/watchlist +
      multi-victim. Megalodon is multi-victim YES (5,561 GitHub
      repositories infected via the 2026-05-18 commit wave) but A&D-
      direct FAIL — no A&D-prime named in any source; structural-
      indirect via developer-ecosystem ubiquity only. Same calculus
      that held for Mini Shai-Hulud, TrapDoor (Socket), art-template,
      durabletask — supply-chain mass-compromise events that target
      the SDLC broadly rather than A&D specifically do not fire
      Trigger 5 unless an A&D-prime customer-impact statement
      materializes. None has for Megalodon. TrapDoor is in active
      anti-noise lock and would absorb as UPDATE flag rather than
      re-fire. DocketWise is legal-sector breach (out-of-scope).
      No multi-victim disclosure touching any of the watchlisted
      A&D primes (Lockheed Martin, Boeing, RTX, Northrop Grumman, GD,
      BAE Systems, L3Harris, Leidos, SAIC, Thales, GE Aerospace,
      Safran, Honeywell Aerospace, Airbus, Elbit).
  - trigger_id: trigger-6-zero-day-no-patch
    fired: false
    evaluation: |
      Required: vulnerability disclosed before patch + CVSS >= 8.0 OR
      widely-deployed product + exploitation confirmed or imminent.
      ZERO new vulnerability disclosures in window. Megalodon is
      abuse-of-feature on GitHub Actions workflow_dispatch anti-
      recursion behavior, which GitHub considers intended-by-design
      per SafeDep framing — NOT a vulnerability disclosure; no CVE
      assignable. VT-008 Exchange CVE-2026-42897 remains no-GA-patch
      but already-corpus-tracked (T-4 KEV due-date), NOT a new
      disclosure for this sweep — anti-noise expired but no new fact
      pattern.
source_health_changes: []                # No durable health changes this sweep. Aikido + Volexity not re-tested per FLASH-narrow scope (both at second-consecutive-failure threshold from 18:00 sentinel; third strike at 07:30 if pattern continues). Mandiant feedburner 22nd consecutive failure (long-standing held-healthy pattern). NVD API result-pagination quirk this sweep (totalResults=5 but empty result body on first two queries) — flagged for 07:30 collection retry with explicit pagination handling; not a stale-flip, just a query-parameter robustness issue.
critical_override_evaluation:
  conditions_required: cvss_10 AND active_exploitation AND tracked_actor AND ad_watchlist_targeted
  conditions_met: 0
  evaluation: |
    Critical-override conditions NOT met across any in-window item.
    Megalodon: 0 of 4 (no CVSS / no CVE, no exploitation confirmed in
    the sense of vulnerability exploitation, no tracked actor, no A&D
    watchlist entity). TrapDoor relay: anti-noise locked + same 0-of-4
    profile as Socket's PM-brief baseline. DocketWise: 0 of 4. Override
    path inapplicable. Quiet-hours queue path would have applied for any
    non-override FLASH fire — also inapplicable given zero fires.
quiet_hours_disposition: |
  06:05 EDT is INSIDE 21:00-09:00 quiet hours (T-3h until 09:00 window
  open). Any FLASH-trigger fire in this window would queue to
  infrastructure/flash-queue.yaml with catchup_sweep:
  2026-05-25T09:00:00-04:00 expires_at: 2026-05-25T18:05:00-04:00
  (12h-from-queue), UNLESS critical-override conditions all four
  simultaneously met. Zero candidates fired = nothing to queue.
carry_forward_items_for_2026_05_25_morning_brief:
  - id: megalodon-safedep-securityweek-multi-victim-github-actions-workflow-dispatch-abuse
    type: primary_morning_candidate_finding_tier
    summary: |
      Megalodon supply-chain attack — 5,718 malicious commits across
      5,561 GitHub repositories injected 2026-05-18 via workflow_dispatch
      GitHub Actions anti-recursion bypass; @tiledesk/tiledesk-server
      npm packages 2.18.6-2.18.12 published 2026-05-19 to 2026-05-21
      from poisoned source by legitimate maintainer `eljohnny`; C2
      216.126.225.129:8443; throwaway GitHub accounts with build-bot /
      auto-ci / ci-bot / pipeline-bot author-identity spoofing.
      Primary: SafeDep (2026-05-21 publication; A/B grade tentative
      pending source-health-yaml validation — vendor research with
      code/IOC depth comparable to Socket / Snyk / StepSecurity tier).
      Relay: SecurityWeek Ionut Arghire 2026-05-25 03:40 EDT (in-
      window pickup that triggered Archimedes attention). UNATTRIBUTED
      — no tracked actor named. NOT FLASH-tier per trigger evaluation
      but STRONG morning-brief finding candidate. Recommend grader
      promote to finding for morning brief inclusion. Recommend
      operator add safedep.io to source-grades.yaml. Recommend Splunk
      hand-built query on 216.126.225.129 in 07:30 collection.
      Cross-corpus diagnostic note for actor-profiler on next
      /update-tracking cycle: build-bot / auto-ci author-identity
      spoofing pattern overlaps thematically (but not deterministically)
      with TeamPCP's claude@users.noreply.github.com spoofing pattern
      from 2026-05-12 Mini Shai-Hulud worm; the technique is portable
      and likely shared across multiple unattributed cybercriminal
      operators in the current SDLC-targeting wave; do NOT collapse
      Megalodon / TrapDoor / TeamPCP into one actor without A/B-grade
      attribution.
  - id: thn-trapdoor-relay-of-socket-update-flag
    type: anti_noise_locked_update_absorption
    summary: |
      THN article published 2026-05-25 01:59 EDT is a B-grade relay of
      Socket's prior TrapDoor disclosure (corpus finding 2026-05-24-0001,
      anti-noise lock active through 2026-05-25 16:00 EDT). Net-new from
      THN over Socket: `.cursorrules` / `CLAUDE.md` AI-agent-config
      manipulation framing detail, named GitHub-PR targets browser-use,
      langchain-ai/langchain, langflow-ai/langflow, and exfil endpoint
      ddjidd564.github[.]io. NO new file hashes, NO new C2 domains
      beyond GitHub Pages endpoint, NO IP IOCs, NO actor attribution.
      Disposition: UPDATE-flag absorption into next scheduled brief
      under existing anti-noise lock — NOT re-FLASH. 07:30 collection
      should capture the AI-agent-targeting framing as UPDATE detail
      on the existing TrapDoor finding.
  - id: socket-modelcontextprotocol-gemini-cli-upstream-injection-claim-layer
    type: post_window_claim_layer_verification_target
    summary: |
      Socket @SocketSecurity 2026-05-24 17:29 EDT post-window
      (carry-forward from prior two sentinels) referenced attempted-
      injection of `.cursorrules` / `CLAUDE.md` into upstream
      `modelcontextprotocol` and `gemini-cli` repos. Not retrievable
      in 6h FLASH-narrow sweeps; held for 2026-05-25 07:30 morning
      collection. Under active TrapDoor anti-noise lock — UPDATE-flag
      candidate at most.
  - id: cve-2026-9082-drupal-kev-due-date-t-2
    type: kev_deadline_awareness
    summary: |
      CVE-2026-9082 Drupal Core SQL injection KEV federal due-date
      2026-05-27 — T-2 from this sweep (Wednesday end-of-business,
      less than 54h away). Already in morning + PM briefs every day
      since KEV add. Carry-forward to 2026-05-25 morning brief
      KEV-deadline action-item block at elevated urgency tier.
  - id: cve-2026-42897-exchange-kev-due-date-t-4
    type: kev_deadline_awareness
    summary: |
      VT-008 Exchange CVE-2026-42897 KEV federal due-date 2026-05-29 —
      T-4 from this sweep. No MSRC GA patch in window; ESU + EEMS /
      EOMT mitigation path continues. Active-exploitation single-source
      veto on MSRC originating tag still holds.
  - id: nvd-5-unknown-id-critical-cves-api-pagination-quirk
    type: collection_retry_target
    summary: |
      NVD lastModified critical query for 2026-05-25 00:00-06:00 EDT
      returned totalResults=5 but result body empty across two query
      attempts (API result-pagination quirk; retried with
      resultsPerPage=20, same empty body). 5 unknown-ID critical CVEs
      modified in the 6h window is non-trivial. 07:30 collection must
      retry with explicit pagination handling (startIndex / resultsPerPage
      walking) to inventory the 5 critical CVEs by ID and trigger-evaluate
      each. If any are corpus-anchored AND have active-exploitation +
      A-grade source, late-fire Trigger 1 as a 09:00 catchup FLASH.
  - id: source-health-borderline-stale-aikido-volexity
    type: source_health_pattern_awareness
    summary: |
      Aikido + Volexity not re-tested this sweep (FLASH-narrow scope
      held). Both at second-consecutive-failure threshold from
      2026-05-24 18:00 sentinel. If 07:30 AM pre-brief hits same
      failure modes, that's the third consecutive and librarian
      should formally mark stale per failure_count >= 2 + persist
      pattern threshold.
notes:
  - "Clean sweep on all 6 FLASH triggers. ZERO FLASH candidates fire. THREE in-window items surfaced — first non-zero in-window count across the prior five consecutive scheduled sweeps (Sun 00:00/06:00/12:00/18:00 + Mon 00:00). All three evaluated NOT-FLASH-TIER: THN/TrapDoor relay (anti-noise locked UPDATE absorption), SW/Megalodon (fresh-to-corpus but UNATTRIBUTED and not A&D-direct), SW/DocketWise (out-of-scope legal sector)."
  - "Megalodon is the priority pickup for 07:30 morning collection. Documents novel-class GitHub Actions workflow_dispatch anti-recursion abuse pattern; 5,561 repositories infected via 5,718 commits 2026-05-18; @tiledesk/tiledesk-server 2.18.6-2.18.12 published 2026-05-19 to 2026-05-21 from poisoned source; C2 216.126.225.129:8443; throwaway GitHub accounts spoofing build-bot / auto-ci / ci-bot / pipeline-bot author identities. Primary SafeDep 2026-05-21; in-window relay SecurityWeek 2026-05-25 03:40 EDT. UNATTRIBUTED — no tracked actor. Strong morning-brief finding candidate. Recommend operator add safedep.io to source-grades.yaml. Recommend morning collection Splunk hand-built query on 216.126.225.129."
  - "Six anti-noise locks evaluated. Five expired pre-window (UNC1549 48h ago, LiteSpeed CVE-2026-48172 48h ago, SonicWall CVE-2024-12802 4d ago, CVE-2026-9082 Drupal status 48h ago, CVE-2026-42897 Exchange GA/ITW 48h ago); one active (trapdoor-multi-ecosystem-supply-chain-socket through 2026-05-25 16:00 EDT, 10h remaining — exercised by THN relay as UPDATE absorption, NOT re-FLASH)."
  - "Splunk first-party: archimedes self-audit only (30 events in -24h). Zero defenseclaw_local events = 55th consecutive dormant non-self sweep. Hard Rule 8: silence is not disconfirming."
  - "Source-health: no durable changes this sweep. Aikido + Volexity not re-tested per FLASH-narrow scope; if 07:30 AM pre-brief hits same failure modes, third strike — librarian formally marks stale. Mandiant feedburner 22nd consecutive failure (long-standing held-healthy). NVD API result-pagination quirk this sweep — totalResults=5 critical CVEs in 6h window but empty result body across two queries; flagged for 07:30 retry with explicit pagination."
  - "Quiet-hours posture: 06:05 EDT is INSIDE 21:00-09:00 quiet window (T-3h to window open). Any FLASH-trigger fire would queue to flash-queue.yaml (not post live to #flash-alerts), UNLESS critical-override conditions all four simultaneously met. Zero fired = nothing to queue."
  - "Critical-override conditions NOT met across any in-window item — zero in-window CVE disclosures with active-exploitation + tracked actor + A&D coincidence."
  - "Carry-forwards for 2026-05-25 07:30 morning collection: (1) Megalodon as strong morning finding candidate with Splunk hand-built query on 216.126.225.129 + safedep.io source-add; (2) THN TrapDoor relay as UPDATE flag under anti-noise lock; (3) Socket modelcontextprotocol / gemini-cli post-window claim-layer verification (anti-noise-locked); (4) CVE-2026-9082 Drupal KEV deadline T-2 elevated urgency; (5) VT-008 Exchange CVE-2026-42897 KEV deadline T-4; (6) NVD 5 unknown-ID critical CVEs in 6h window — paginate retry; (7) Aikido + Volexity source-health third-strike check."
  - "7-day FLASH-fired-count anti-noise check: this sweep adds zero to the count. Six consecutive scheduled FLASH sweeps (Sun 00:00 / 06:00 / 12:00 / 18:00 + Mon 00:00 + this 06:00) have all been clean — Sunday-quiet baseline has broken (3 in-window items) but trigger-evaluated baseline holds."
  - "Hard Rules compliance: Rule 2 (no Archimedes-originated attribution) — Megalodon and TrapDoor explicitly preserved UNATTRIBUTED per primary sources. Rule 3 (no exploitation content) — no PoC referenced. Rule 4 (passive only) — no active scans, SpiderFoot not invoked, authorized-targets.yaml empty. Rule 6 (15-word quote limit) — no source-quotes used in this sentinel; framing is paraphrase throughout. Rule 7 (copyright) — no source text included beyond paraphrased titles + IOC extracts. Rule 8 (Splunk first-party) — 55th consecutive dormant non-self sweep."
  - "Briefer/orchestrator action: NO Discord post (quiet-hours active AND zero triggers fired per FLASH-POLICY silent-on-clean-sweep). Next scheduled cadence event is 07:30 EDT (Monday morning pre-brief collection)."
---

# 06:00 EDT 2026-05-25 FLASH sweep — NO TRIGGERS FIRED (3 in-window items all NOT-FLASH-TIER)

This sentinel record documents the 2026-05-25 06:00 EDT FLASH alert sweep.
Window: 2026-05-25T00:00 to 2026-05-25T06:00 EDT (6h).

## Sweep outcome

**ZERO FLASH candidates fired. 0 of 6 triggers fired.** Clean sweep on
all six triggers in `doctrine/FLASH-POLICY.md`. THREE in-window items
surfaced — first non-zero in-window count after five consecutive prior
clean sweeps — but all three evaluated NOT-FLASH-TIER:

1. **The Hacker News TrapDoor relay** (2026-05-25 01:59 EDT) — B-grade relay
   of Socket's prior 2026-05-24 disclosure. Anti-noise lock
   `trapdoor-multi-ecosystem-supply-chain-socket` ACTIVE through 2026-05-25
   16:00 EDT. Absorbs as UPDATE flag into next scheduled brief, NOT
   re-FLASH per anti-noise rule 1.

2. **SecurityWeek Megalodon** (2026-05-25 03:40 EDT) — B-grade relay of
   SafeDep's 2026-05-21 primary research (NEW to corpus; SafeDep was not
   in source-grades.yaml at the time of original publication and prior
   Archimedes sweeps did not pick it up — collection gap acknowledged).
   5,561 GitHub repositories infected via workflow_dispatch anti-recursion
   bypass. **UNATTRIBUTED** at both primary and relay layers. Not A&D-
   direct (no prime named). NOT FLASH-tier — but **strongest morning-
   brief finding candidate** of the three.

3. **SecurityWeek DocketWise data breach** (2026-05-25 05:37 EDT) — legal-
   sector PII breach. No tracked actor, no CVE, no A&D relevance. NOT
   FLASH-tier and NOT morning-brief-tier; standard third-party breach
   landscape noise.

## One-paragraph summary

The 00:00 → 06:00 EDT window produced three in-window items but **zero**
fire any of the six FLASH triggers. Megalodon (5,561 GitHub repositories
backdoored via `workflow_dispatch` anti-recursion bypass; @tiledesk/
tiledesk-server 2.18.6-2.18.12 published from poisoned source 2026-05-19
to 2026-05-21; C2 216.126.225.129:8443; throwaway GitHub accounts
spoofing build-bot / auto-ci / ci-bot / pipeline-bot author identities)
is the most substantive new signal — but SafeDep's primary research
(2026-05-21) **explicitly does not attribute** to any tracked actor or
known cluster, and no A&D prime is named in any source, so Triggers 2 / 4
fail on attribution and Trigger 5 fails on A&D-direct. The Hacker News's
2026-05-25 01:59 EDT TrapDoor article is a B-grade relay of Socket's
prior disclosure (corpus finding 2026-05-24-0001), absorbing as UPDATE
flag under the active anti-noise lock through 2026-05-25 16:00 EDT — adds
`.cursorrules` / `CLAUDE.md` AI-agent-config framing detail, named GitHub-
PR targets (browser-use, langchain-ai/langchain, langflow-ai/langflow),
and exfil endpoint ddjidd564.github[.]io, but **no** new file hashes, **no**
new C2 domains beyond the GitHub Pages endpoint, **no** new IP IOCs, **no**
attribution. DocketWise is out-of-scope legal-sector PII breach (143,480
individuals). CISA KEV catalog 2026.05.22 unchanged 66h+; KEV deadlines
T-2 Drupal CVE-2026-9082 (2026-05-27 Wed EOB) and T-4 Exchange CVE-2026-
42897 (2026-05-29) carry forward at elevated urgency. NVD lastModified
critical query for the 6h window returns `totalResults=5` but empty result
bodies across two queries (API result-pagination quirk); 5 unknown-ID
critical CVEs flagged for 07:30 morning paginate-retry. Splunk first-
party: 30 archimedes self-telemetry events in -24h; zero `defenseclaw_
local` events = 55th consecutive dormant non-self sweep.

## In-window items — detailed disposition

### 1. THN TrapDoor relay (B-grade)

- **URL:** `https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html`
- **Published:** 2026-05-25 05:59:13 UTC = 01:59 EDT
- **Primary:** Socket (corpus-anchored via finding-2026-05-24-0001)
- **Anti-noise lock:** ACTIVE through 2026-05-25 16:00 EDT
- **Disposition:** UPDATE-flag absorption into next scheduled brief
- **Net-new over Socket primary:** AI-agent-config framing
  (`.cursorrules` / `CLAUDE.md`), named GitHub-PR targets, exfil
  endpoint ddjidd564.github[.]io. No new hashes / IPs / domains beyond
  the GitHub Pages endpoint. No actor attribution.

### 2. SW Megalodon relay (B-grade)

- **URL:** `https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/`
- **Published:** 2026-05-25 07:40:55 UTC = 03:40 EDT
- **Primary:** SafeDep (2026-05-21 publication, `https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows`)
- **Disposition:** STRONG morning-brief finding candidate. NOT FLASH-tier.
- **Mechanism:** Attackers injected GitHub Actions workflows via fake
  automated commits exploiting `workflow_dispatch` trigger's intended
  anti-recursion bypass. Two payload classes: (a) add workflows
  triggered on push/PR; (b) replace existing workflows with dormant
  backdoors activated later via stolen GitHub tokens.
- **Scope:** 5,718 malicious commits across 5,561 repositories injected
  2026-05-18 11:36-17:48 UTC. Subsequent npm publication of poisoned
  @tiledesk/tiledesk-server 2.18.6-2.18.12 from compromised source-of-
  truth by legitimate maintainer `eljohnny` 2026-05-19 to 2026-05-21.
- **Data exfiltration targets per SafeDep primary:** CI environment
  variables, AWS / GCP / Azure credentials, SSH private keys, Docker /
  Kubernetes configs, API keys, database connection strings, GitHub
  Actions tokens, GitLab CI/CD tokens.
- **IOCs:** C2 `216.126.225.129:8443`; throwaway GitHub accounts with
  random 8-char usernames (examples rkb8el9r, bhlru9nr, lo6wt4t6);
  author-identity spoofing (build-bot, auto-ci, ci-bot, pipeline-bot);
  poisoned npm package versions @tiledesk/tiledesk-server 2.18.6-2.18.12.
- **Attribution:** **UNATTRIBUTED**. SafeDep makes no attribution to
  any tracked actor or known cluster. SecurityWeek does not attribute.
  Author-identity-spoofing pattern (build-bot etc.) thematically
  overlaps with TeamPCP's claude@users.noreply.github.com spoofing from
  2026-05-12 Mini Shai-Hulud worm but the technique is **portable and
  likely shared across multiple unattributed cybercriminal operators in
  the current SDLC-targeting wave** — Hard Rule 2 prevents Archimedes
  collapse of Megalodon / TrapDoor / TeamPCP into one actor without
  A/B-grade attribution.
- **A&D relevance:** Structural-indirect via developer-ecosystem
  ubiquity. No A&D prime named. Same calculus that has held for prior
  unattributed supply-chain mass-compromise events.
- **Recommendations to morning collection / orchestrator:**
  1. Grader promote to finding-tier for morning brief inclusion
  2. Operator add safedep.io to source-grades.yaml (vendor research
     with code/IOC depth comparable to Socket / Snyk / StepSecurity
     tier; tentative B-grade pending source-health validation; 6-day
     post-original-publication detection gap acknowledged)
  3. Collector run Splunk hand-built query on `216.126.225.129` in
     07:30 collection — if any defenseclaw_local hit, escalate
  4. Actor-profiler review build-bot / auto-ci author-identity-
     spoofing pattern on next /update-tracking cycle for cross-corpus
     diagnostic vs. TeamPCP's claude@users.noreply.github.com pattern
     (do NOT collapse without A/B-grade attribution)

### 3. SW DocketWise (B-grade)

- **URL:** `https://www.securityweek.com/docketwise-data-breach-impacts-143000/`
- **Published:** 2026-05-25 09:37:27 UTC = 05:37 EDT
- **Primary:** SecurityWeek (Ionut Arghire) reporting on DocketWise
  customer notification
- **Disposition:** SKIP from finding queue. Out-of-scope legal-sector
  PII breach (143,480 individuals); no actor named, no CVE, no A&D
  relevance.

## Splunk first-party check

Query A: `| tstats count where (index=archimedes OR index=defenseclaw_local) earliest=-24h@h latest=now by index`
Query B: `search index=defenseclaw_local earliest=-24h@h latest=now | head 10`

Result: 30 events in `archimedes` index (operation + scheduler
self-telemetry only). **ZERO `defenseclaw_local` events** in -24h —
**55th consecutive dormant non-self sweep** (prior 54 + this sweep).
No IOC-match opportunity exists structurally on this sweep cycle.

Megalodon C2 IP `216.126.225.129` is fresh-corpus-candidate and would
be a reasonable target for a hand-built Splunk query in 07:30 morning
collection if grader promotes Megalodon to finding-tier.

Splunk reachability healthy per both query paths.

## Quiet-hours and critical-override posture

- 06:05 EDT is **INSIDE the 21:00-09:00 quiet-hours window** (T-3h
  until 09:00 active-hours open). Any FLASH-trigger fire would queue
  to `infrastructure/flash-queue.yaml` with catchup at 2026-05-25 09:00
  EDT, UNLESS critical-override conditions all four simultaneously met.
  Zero candidates fired makes this moot.
- Critical-override conditions (CVSS 10.0 + confirmed active
  exploitation + tracked actor + A&D watchlist hit, all four
  simultaneously) not met on any in-window item — Megalodon 0 of 4,
  TrapDoor relay 0 of 4 (anti-noise locked anyway), DocketWise 0 of 4.

## Anti-noise lock state

| Lock topic | Expires | State this sweep |
|---|---|---|
| **TrapDoor multi-ecosystem (Socket)** | **2026-05-25 16:00** | **active, 10h remaining** — exercised by THN relay this window as UPDATE absorption, NOT re-FLASH |
| UNC1549 Screening Serpens tradecraft | 2026-05-24 06:00 | expired 48h ago — no re-fire pressure |
| LiteSpeed CVE-2026-48172 cpanel | 2026-05-24 06:00 | expired 48h ago — no re-fire pressure |
| CVE-2024-12802 SonicWall MFA bypass | 2026-05-21 18:00 | expired 4d ago — no re-fire pressure |
| CVE-2026-9082 Drupal KEV status | 2026-05-24 06:00 | expired 48h ago — T-2 KEV countdown carry-forward |
| CVE-2026-42897 Exchange GA / ITW | 2026-05-24 06:00 | expired 48h ago — T-4 KEV countdown carry-forward |

## Carry-forwards to 2026-05-25 07:30 morning collection

1. **MEGALODON as primary morning finding candidate.** SafeDep + SecurityWeek;
   UNATTRIBUTED; 5,561 GitHub repositories infected via workflow_dispatch
   anti-recursion bypass; @tiledesk/tiledesk-server 2.18.6-2.18.12 poisoned;
   C2 216.126.225.129:8443. Hand-built Splunk query on 216.126.225.129.
   Recommend operator add safedep.io to source-grades.yaml as new B-grade
   primary research source (Socket-tier IOC depth).
2. **THN TrapDoor UPDATE flag** under active anti-noise lock —
   `.cursorrules` / `CLAUDE.md` AI-agent-config framing detail.
3. **Socket modelcontextprotocol / gemini-cli upstream-injection claim
   layer** — 2026-05-24 17:29 EDT post-window @SocketSecurity follow-up,
   anti-noise-lock-covered, UPDATE-flag candidate at most.
4. **CVE-2026-9082 Drupal KEV deadline T-2** (2026-05-27 Wed EOB) —
   elevated urgency tier for morning brief KEV-action-item block.
5. **VT-008 Exchange CVE-2026-42897 KEV deadline T-4** (2026-05-29).
6. **NVD 5 unknown-ID critical CVEs API paginate-retry** — 6h window
   `totalResults=5` cvssV3Severity=CRITICAL but empty result body across
   two query attempts; collector retry with explicit `startIndex` /
   `resultsPerPage` walking to inventory and trigger-evaluate each.
7. **Aikido + Volexity source-health third-strike check** — if 07:30
   pre-brief hits same failure modes (DNS getaddrinfo on
   blog.aikido.dev / RSS parse error on Volexity), librarian formally
   marks stale per failure_count >= 2 threshold.

## Source-health transient observations (not durable changes)

- Aikido + Volexity not re-tested this sweep per FLASH-narrow scope
  (both at second-consecutive-failure threshold from 18:00 sentinel;
  third strike at 07:30 if pattern continues).
- Mandiant feedburner endpoint **22nd consecutive failure** since
  2026-05-05 (404 persistent; held healthy pending operator alt-
  endpoint decision per long-standing policy).
- NVD API result-pagination quirk this sweep — `totalResults=5` critical
  CVEs in 6h window but empty result body across two queries (first
  with `resultsPerPage` unset / second with explicit 20). Not a stale-
  flip; query-parameter robustness issue. Flagged for 07:30 morning
  paginate-retry with `startIndex=0&resultsPerPage=20` walk.

None of the above trip an immediate stale flip this sweep.

## Hard Rules compliance

- **Rule 2** (no Archimedes-originated attribution): Megalodon and
  TrapDoor preserved UNATTRIBUTED per primary sources. Author-identity-
  spoofing thematic overlap between Megalodon's build-bot / auto-ci
  pattern and TeamPCP's claude@users.noreply.github.com pattern is
  flagged for actor-profiler review WITHOUT collapse to common actor.
- **Rule 3** (no exploitation content): no PoC, no payloads, no
  exploit guides referenced.
- **Rule 4** (passive only): no active scans, SpiderFoot not invoked,
  `authorized-targets.yaml` empty.
- **Rule 6** (15-word quote limit): no quotes used in this sentinel.
  All framing paraphrased.
- **Rule 7** (copyright): no source text included beyond paraphrased
  titles + IOC extracts.
- **Rule 8** (Splunk first-party): `defenseclaw_local` 0 events in
  -24h (55th consecutive dormant non-self sweep). Silence is not
  disconfirming per established cadence.

## Disposition

- **No Discord post** — quiet-hours active AND zero FLASH-triggers
  fired per FLASH-POLICY (silent-on-clean-sweep).
- **No `flash-queue.yaml` update** — zero triggers fired, nothing to
  queue.
- **No `_master-index.yaml` regeneration** — sentinel writes no IOCs.
  Megalodon IOCs (216.126.225.129 C2, @tiledesk/tiledesk-server 2.18.6-
  2.18.12 packages) deferred to morning grader if Megalodon promoted
  to finding-tier.
- **Splunk HEC telemetry** `event_type=flash_sweep` to be shipped via
  `.claude/hooks/splunk-log.sh` by librarian on commit.
- **TLP:CLEAR.**
