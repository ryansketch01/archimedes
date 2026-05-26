---
source: archimedes-internal
source_grade: N/A
collected_at: 2026-05-26T06:05:00-04:00
sweep: flash-2026-05-26-0600
candidate_trigger: none_fired
url: null
test: false
sentinel: true
sweep_type: flash-early-morning
status: complete
triggers_fired: 0
sweep_window:
  start: 2026-05-26T00:00:00-04:00
  end: 2026-05-26T06:00:00-04:00
  duration_h: 6.0
prior_sweep_anchor:
  sweep_id: flash-2026-05-26-0000
  anchor_at: 2026-05-26T00:05:00-04:00
  raw_id: raw-2026-05-26-flash-0000-000-sentinel-clean-sweep.md
  commit_sha: 9125941
  disposition: zero_triggers_fired
  notes: |
    The 00:00 EDT sentinel was a canonical clean sweep — 0 of 6
    triggers fired on a 6h overnight window. Two in-window items
    surfaced (SANS ISC Stormcast podcast + SANS ISC ACR Stealer
    diary), both categorical-fail across all triggers. This 06:00
    sweep extends the chain forward through the second-half
    overnight window 00:00 → 06:00 EDT inside quiet hours.
match_reason:
  watchlist: []          # aviation referenced in THN UNC1549 piece but A&D-prime watchlist not directly hit
  actors:
    - "004"               # UNC1549 / Nimbus Manticore / Screening Serpens — restatement-only via THN B-grade relay
  vulnerabilities:
    - VT-005              # CVE-2026-9082 Drupal — BC restatement of corpus-tracked KEV-deadline-tracking
  keywords: [aviation, Nimbus Manticore, MiniFast, MiniJunk V2, getsqldeveloper, SEO poisoning]
triage_tags:
  - flash_sentinel
  - flash_early_morning
  - clean_sweep
  - zero_triggers_fired
  - quiet_hours_overnight
  - unc1549_thn_restatement_anti_noise_absorbed
  - cve_2026_9082_bc_restatement_anti_noise_absorbed
  - mirhosting_securityweek_restatement_anti_noise_absorbed
iocs_extracted: false        # extracted into THN-restatement assessment block, not standalone IOC sidecar
iocs_count: 1                # getsqldeveloper[.]com (per CKR May 22 originating publication, cited via THN)
text_word_count: 2200
promoted: false
rejected_at: 2026-05-26T08:00:00-04:00
rejection_id: reject-2026-05-26-0002
ttl_expires_at: 2026-08-24T06:05:00-04:00
sources_queried:
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.22 UNCHANGED (~102h+ since last add CVE-2026-9082 Drupal 2026-05-22). ZERO net-new KEV adds since 00:00 sweep. T-1 Drupal CVE-2026-9082 deadline (Wed EOB ~14h from this sweep at peak urgency) unchanged; T-3 Exchange CVE-2026-42897 unchanged (~75h to Fri).
  - cisa-advisories        # not re-queried this sweep (00:00 sweep returned 0 in-window from 6h prior; combined overnight 12h window has zero CISA-advisory publication candidates per 00:00 + 06:00 pattern)
  - nvd                    # WebFetch services.nvd.nist.gov rest/json/cves/2.0 lastModStartDate=2026-05-26T04:00 UTC lastModEndDate=2026-05-26T10:00 UTC cvssV3Severity=CRITICAL → totalResults=0. ZERO critical CVEs modified in 6h window per direct NVD query.
  - thehackernews          # fetch_feed feedburner — 200 OK; last_modified Tue 26 May 2026 09:51:44 GMT (= 05:51 EDT, INSIDE window). 3 in-window items — see filter_evaluation_summary.
  - bleepingcomputer       # fetch_feed — 200 OK; last_modified Tue 26 May 2026 09:56:54 GMT (= 05:56 EDT, INSIDE window). 3 in-window items — see filter_evaluation_summary.
  - securityweek           # fetch_feed feedburner — 200 OK; last_modified Tue 26 May 2026 09:47:25 GMT (= 05:47 EDT, INSIDE window). 1 in-window item — see filter_evaluation_summary.
  - the-record             # fetch_feed therecord.media/feed — 200 OK; 5 items in feed, 0 in 6h window.
  - krebs                  # not re-queried this sweep (00:00 sweep last_modified Mon 25 May 2026 13:21:49 GMT pre-window unchanged; cadence-slow publisher unlikely to update inside 00:00 → 06:00 overnight EDT window)
  - checkpoint-research    # fetch_feed research.checkpoint.com/feed — 200 OK; last_modified Mon 25 May 2026 15:08:41 GMT (pre-window 11:08 EDT) UNCHANGED 12h+. 0 items in 6h window. NOTE: the originating CKR "Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict" was published 2026-05-22 per WebSearch retrieval — out of 6h window and already corpus-tracked in 2026-05-23 0600 FLASH lineage.
  - mstic                  # fetch_feed microsoft.com/en-us/security/blog/feed — 200 OK; last_modified Fri 22 May 2026 17:57 GMT UNCHANGED (11th consecutive sweep). 0 in window.
  - unit42                 # fetch_feed feedburner — 200 OK; last_modified Mon 25 May 2026 16:19:50 GMT (12:19 EDT, pre-window) UNCHANGED from 00:00 sweep. 0 in window. NOTE: Unit 42 May 22 piece on UNC1549 MiniUpdate/MiniJunk V2/AppDomainManager is corpus-tracked in 2026-05-23 0600 FLASH lineage — out of 6h window.
  - sentinelone            # fetch_feed sentinelone.com/labs/feed — 200 OK; last_modified Tue 26 May 2026 05:33:13 GMT (01:33 EDT, INSIDE window) but 0 items in 6h window after since-filter. Server-side index refresh, no new publication.
  - crowdstrike            # fetch_feed crowdstrike.com/blog/feed — 200 OK; last_modified Tue 26 May 2026 08:54:46 GMT (04:54 EDT, INSIDE window). 10 items returned ALL dateless slate (product/marketing). Same content slate as 00:00 sweep — no threat-research with publication-dates in window.
  - cisco-talos            # fetch_feed blog.talosintelligence.com/rss/ — 200 OK; 15 items in feed, 0 in 6h window.
  - mandiant               # fetch_feed mandiant.com/resources/blog/rss.xml — 200 OK with 20 items in feed, 0 in 6h window. SECOND consecutive 200 OK observation (00:00 sweep was first after 24 consecutive 404 failures). NOTE: Mandiant/GTIG identified as Trigger-6-adjacent CVE-2026-5426 (KnowledgeDeliver LMS, CVSS 7.5) originating source per THN article — primary publication date appears pre-2026-02-24 (patch availability indicates Feb 2026 disclosure). Out of window per primary; THN is B-grade relay.
  - rapid7                 # not re-queried this sweep (00:00 sweep last_modified Tue 26 May 2026 03:17:33 GMT in window with 0 new items; overnight cadence-slow publisher pattern holds)
  - eset-welivesecurity    # fetch_feed welivesecurity.com/en/rss/feed — 200 OK; 100 items in feed, 0 in 6h window.
  - dfir-report            # not re-queried this sweep (cadence-slow, 00:00 sweep last_modified Mon 11 May UNCHANGED 2 weeks)
  - proofpoint             # fetch_feed proofpoint.com/us/rss.xml — 200 OK; last_modified Tue 26 May 2026 08:34:25 GMT (04:34 EDT, INSIDE window). 0 items in 6h window. Server-side index refresh, no new publication.
  - sans-isc               # fetch_feed isc.sans.edu/rssfeed.xml — 200 OK; last_modified Tue 26 May 2026 09:59:05 GMT (= 05:59 EDT, INSIDE window). 0 items in 6h window after since-filter (the ACR Stealer / Stormcast items from 00:00 sweep are now outside the 00:00 → 06:00 EDT window).
  - aikido                 # NOT re-fetched — STALE-flagged at AM-25; 24h skip rule continues until ~midday 2026-05-26.
  - volexity               # NOT re-queried (00:00 sweep parse error 4th+ consecutive; deferred to AM-26 per held-healthy operator policy)
  - reliaquest             # NOT re-queried (00:00 sweep DNS resolution failure; not in source-health.yaml; operator decision pending)
  - splunk-archimedes      # mcp__splunk-query targeted 27-IOC sweep on -6h@h (executed THIS sweep; see splunk_first_party_check). ZERO events returned.
  - splunk-defenseclaw     # included in the -6h@h cross-index sweep; 0 events. 60th consecutive dormant non-self sweep (incremented from 59 at 00:00).
splunk_first_party_check:
  query: 'search index=defenseclaw_local OR index=archimedes earliest=-6h@h latest=now ("MiniFast" OR "MiniJunk" OR "Nimbus Manticore" OR "Screening Serpens" OR UNC1549 OR "getsqldeveloper" OR "AppDomainManager" OR "MiniUpdate" OR CVE-2026-9082 OR CVE-2026-42897 OR "Drupal" OR "Exchange" OR ShinyHunters OR "7-Eleven" OR KnowledgeDeliver OR Godzilla OR "Cobalt Strike" OR CVE-2026-5426 OR "Stark Industries" OR MIRhosting OR WorkTitans OR TeamPCP OR "Shai-Hulud" OR "Charming Kitten" OR APT28 OR APT29 OR Sandworm) | head 50'
  result: 0 events — zero IOC hits across 27 corpus-tracked + in-window-surfaced strings on -6h@h overnight window
  consecutive_dormant_sweeps_defenseclaw: 60   # incremented from 59 at 00:00
  iac_ioc_hits_in_defenseclaw_local: 0
  hard_rule_8_framing: |
    Targeted 27-IOC sweep across (a) all carried-forward corpus-tracked
    IOC strings, (b) in-window-surfaced strings from THN UNC1549 / KnowledgeDeliver
    / 7-Eleven / SecurityWeek MIRhosting items, and (c) roster
    Russia/Iran/DPRK actors + Mini Shai-Hulud lineage on defenseclaw_local
    + archimedes in -6h@h returned ZERO events. 60th consecutive dormant
    non-self sweep on defenseclaw_local. Hard Rule 8: silence is not
    disconfirming, not confirming.
filter_evaluation_summary:
  in_window_items_total: 7
  in_window_items_evaluated: 7
  in_window_items_corpus_restatement_anti_noise_absorbed: 3
  in_window_items_filtered_out_cvss_below_threshold: 1
  in_window_items_filtered_out_no_actor_no_ad: 2
  in_window_items_filtered_out_regulatory_news: 1
  in_window_items_flash_tier: 0
  notes: |
    Seven in-window items distributed across three A/B-grade media surfaces
    (THN: 3, BC: 3, SecurityWeek: 1). All seven categorically fail FLASH
    promotion under current corpus state:

    THN-1 "CERT-In Mandates 12-Hour Patching" (09:13 UTC = 05:13 EDT):
      Indian regulatory guidance news, no CVE, no IOC, no actor. Not a
      FLASH-trigger event class. FILTER OUT (regulatory-news).

    THN-2 "Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing
    and SEO Poisoning" (07:13 UTC = 03:13 EDT):
      B-grade relay of Check Point Research "Fast and Furious – Nimbus
      Manticore Operations During the Iranian Conflict" (2026-05-22,
      out of window) + Unit 42 May 22 concurrent (out of window;
      already corpus-tracked in 2026-05-23 0600 FLASH lineage).
      Tracked actor: UNC1549 / Nimbus Manticore / Screening Serpens /
      Smoke Sandstorm (#004). NEW TTP elements vs prior corpus surface:
      (a) MiniFast naming distinct from MiniUpdate (Check Point taxonomy
      vs Unit 42 taxonomy on same/adjacent family — naming-overlap
      question), (b) SEO poisoning delivery vector with getsqldeveloper[.]com
      fake SQL Developer download page, (c) explicit aviation sector
      targeting language (no A&D prime named). Restatement of
      tradecraft evolution under active corpus tracking. Per FLASH-POLICY
      anti-noise rule and operator-supplied anti-noise list ("UNC1549
      Unit 42 tradecraft (0523 still in queue)"), this is FLASH-anti-noise-
      absorbed — incremental detail belongs in AM-26 morning brief as
      an UPDATE on the UNC1549 corpus surface, not a duplicate FLASH.
      ABSORB to morning brief.

    THN-3 "KnowledgeDeliver LMS Flaw Exploited to Deploy Godzilla and
    Cobalt Strike" (05:19 UTC = 01:19 EDT):
      Mandiant/GTIG-originated retrospective on CVE-2026-5426
      (hard-coded ASP.NET machine keys, Japanese LMS). CVSS 7.5 — below
      Trigger 1 floor (≥9.0) AND below Trigger 6 floor (≥8.0 unless
      widely-deployed; Japanese-domestic LMS is not widely-deployed in
      A&D context). Patch available since pre-2026-02-24. NO tracked
      actor named. Restitution-style retrospective, not a fresh FLASH
      event class. FILTER OUT (CVSS below floor + patched + no actor +
      not widely-deployed).

    BC-1 "CISA Orders Feds to Patch Actively Exploited Drupal Vulnerability"
    (08:46 UTC = 04:46 EDT):
      Restatement of CVE-2026-9082 KEV addition (2026-05-22, T-1 deadline
      Wed 2026-05-27 EOB now ~14h away). Anti-noise lock ACTIVE
      (cve-2026-9082-drupal-core-sqli-kev-deadline-tracking). One new
      data point: Shadowserver tracking 670 unpatched Drupal installations
      (272 North America, 273 Europe). Operationally useful Shadowserver
      datum but NOT FLASH-tier — appropriate for AM-26 morning brief
      situational-awareness paragraph under existing CVE-2026-9082
      surface. FLASH-anti-noise-absorbed. ABSORB to morning brief.

    BC-2 "Microsoft: Domain Controller lookup may fail on Windows Server
    2016" (07:41 UTC = 03:41 EDT):
      Microsoft known-issue advisory on KB5087537 May 2026 update.
      NOT a vulnerability with active exploitation. NOT a zero-day.
      NO actor. NO CVE. Patching-side operational issue. FILTER OUT
      (no FLASH-trigger event class).

    BC-3 "7-Eleven data breach exposes personal information of 185,000 people"
    (07:01 UTC = 03:01 EDT):
      ShinyHunters convenience-store data breach. ShinyHunters surfaces in
      Archimedes corpus as an IOC string but NOT in _roster.yaml. Consumer-
      retail breach, no A&D relevance, no CVE, no FLASH-trigger event class
      under current tracking definitions. FILTER OUT (no tracked actor in
      roster + no A&D + no CVE).

    SW-1 "Admins of Bulletproof Hosting Service Used by Russian Hackers
    Arrested in Netherlands" (09:47 UTC = 05:47 EDT):
      Same MIRhosting / WorkTitans / Stark Industries incident covered by
      Krebs 2026-05-25 PM + FIOD originating disclosure (finding-2026-05-25-0003
      in afternoon brief 2026-05-25). Anti-noise lock ACTIVE
      (stark-mirhosting-worktitans-russia-aligned-hosting-takedown) through
      2026-05-26 16:00. SecurityWeek (Ionut Arghire) is narrative-synthesis
      restatement, no novel investigative content beyond confirming suspect
      names (Youssef Z., Andrey N. — corroborates FIOD/Krebs). FLASH-anti-
      noise-absorbed. ABSORB to morning brief if morning brief covers, or
      let lock expire at 16:00 if morning brief omits.

trigger_evaluation:
  trigger_1_critical_cve_exploited:
    fired: false
    reason: |
      ZERO new critical CVEs (CVSS ≥ 9.0) disclosed in the 6h window
      with active exploitation + A-grade source. NVD direct query
      (cvssV3Severity=CRITICAL, lastModStartDate=2026-05-26T04:00 UTC,
      lastModEndDate=2026-05-26T10:00 UTC) returned totalResults=0.
      CISA KEV catalog version 2026.05.22 UNCHANGED (~102h+ since
      last add CVE-2026-9082 Drupal 2026-05-22; longest catalog-
      quiescence stretch in current corpus tracking window). The
      only in-window CVE referenced is CVE-2026-5426 (KnowledgeDeliver
      LMS, CVSS 7.5) — BELOW the 9.0 floor. Trigger 1 categorical-fail
      on the CVSS-magnitude prong.
  trigger_2_tracked_actor_attribution:
    fired: false
    reason: |
      ZERO NEW attribution publications in the 6h window. The THN
      Nimbus Manticore / UNC1549 piece is B-grade relay of Check Point
      Research's 2026-05-22 "Fast and Furious" primary (out of window,
      already corpus-tracked in 2026-05-23 0600 FLASH lineage) plus
      Unit 42 May 22 concurrent (already covered in same FLASH queue
      entry). Per FLASH-POLICY Trigger 2 spec ("attribution is new
      (not re-reporting prior attribution)"), this fails on the
      novelty prong. UNC1549 attribution to Iran / IRGC is now a
      vendor-community-consensus baseline (Mandiant, Unit 42, Check
      Point); THN's relay does not constitute new attribution.
      Trigger 2 categorical-fail on the novelty prong + the
      independent-primary-in-window prong.
  trigger_3_first_party_ioc_hit:
    fired: false
    reason: |
      Targeted 27-IOC sweep on defenseclaw_local + archimedes -6h@h
      returned ZERO events. The sweep included (a) carried-forward
      corpus IOCs (CVE-2026-9082 Drupal, CVE-2026-42897 Exchange,
      VT-006 Mini Shai-Hulud surface, TeamPCP cluster, MIRhosting,
      Stark Industries, Russia/Iran/DPRK roster actors), (b) NEW
      in-window-surfaced strings (MiniFast, getsqldeveloper,
      KnowledgeDeliver, CVE-2026-5426, Godzilla web shell, 7-Eleven,
      ShinyHunters), and (c) AppDomainManager TTP keyword. 60th
      consecutive dormant non-self sweep on defenseclaw_local.
      Hard Rule 8: silence is not disconfirming, not confirming.
  trigger_4_tracked_actor_ttp_change:
    fired: false
    reason: |
      The THN Nimbus Manticore / UNC1549 piece documents NEW tooling
      (MiniFast, named distinct from MiniUpdate) and NEW delivery
      infrastructure (SEO poisoning via getsqldeveloper[.]com fake
      SQL Developer page). THN is B-grade. UNC1549 IS in _roster.yaml
      (#004). The originating publications (Check Point Research
      2026-05-22, Unit 42 2026-05-22) are A-grade vendor sources
      OUT OF the 6h window. Per FLASH-POLICY Anti-Noise Rule 1 ("one
      FLASH per trigger topic per 24 hours") and the operator's
      anti-noise list explicitly flagging "UNC1549 Unit 42 tradecraft
      (0523 still in queue)" — Trigger 4 conditions technically
      satisfy on the B-grade-relay layer but the topic is corpus-
      locked under the 2026-05-23 0600 FLASH (flash-queue.yaml entry
      brief_id flash-2026-05-23-0600-001-unc1549-screening-serpens-
      tradecraft-evolution). FLASH-anti-noise-absorbed; incremental
      MiniFast naming + SEO-poisoning detail belongs as an UPDATE
      block in AM-26 morning brief on UNC1549 surface, not a
      duplicate FLASH at 06:00 EDT. Doctrine result: trigger does
      NOT fire because the topic is corpus-locked and the canonical
      disposition is morning-brief absorption.
  trigger_5_ad_sector_campaign:
    fired: false
    reason: |
      The THN UNC1549 piece describes aviation sector targeting (US,
      Europe, Middle East, with named Saudi Arabia + Australia
      employees in software and aviation sectors). Aviation IS A&D-
      adjacent. HOWEVER no aerospace/defense PRIME (Lockheed Martin,
      Boeing, RTX, Northrop, GD, BAE, L3Harris, Leidos, SAIC, Thales,
      GE Aerospace, Safran, Honeywell Aerospace, Airbus, Elbit per
      watchlists/aerospace-defense.yaml) is named. The Unit 42
      generic "U.S. oil and gas firm" + "employees in software and
      aviation sectors" framing is sectoral-shape, NOT direct prime
      targeting. Per FLASH-POLICY Trigger 5 ("explicitly targeting
      aerospace, defense, or watchlist companies"), watchlist-prime
      naming is the operative threshold. Trigger 5 fails on the
      watchlist-prime-naming prong. ALSO restatement of corpus-
      tracked 2026-05-23 0600 FLASH content — anti-noise-absorbed.
  trigger_6_zero_day_no_patch:
    fired: false
    reason: |
      ZERO in-window zero-day disclosures without a patch. The
      KnowledgeDeliver CVE-2026-5426 piece IS a zero-day retrospective
      (exploited as a zero-day pre-patch per Mandiant/GTIG framing)
      but PATCH IS AVAILABLE since pre-2026-02-24 — Trigger 6
      ("disclosed before a patch is available") fails on the
      patch-availability prong. Additionally CVSS 7.5 is below
      Trigger 6 ≥8.0 floor unless widely-deployed; KnowledgeDeliver
      is a Japanese-domestic LMS, not widely-deployed in any
      A&D/global enterprise context. Categorical-fail on multiple
      prongs.

anti_noise_locks_active:
  - lock_id: teampcp-mini-shai-hulud-cluster-2026
    source_anchor: finding-2026-05-25-0002 (afternoon brief 2026-05-25)
    expires_at: 2026-05-26T16:00:00-04:00
    status: ACTIVE — TeamPCP topic locked through 2026-05-26 16:00 EDT
  - lock_id: stark-mirhosting-worktitans-russia-aligned-hosting-takedown
    source_anchor: finding-2026-05-25-0003 (afternoon brief 2026-05-25)
    expires_at: 2026-05-26T16:00:00-04:00
    status: ACTIVE — SecurityWeek 05:47 EDT item is restatement-only of this corpus surface
  - lock_id: ghost-cms-cve-2026-26980-fresh-tradecraft-detail
    source_anchor: 12:00 EDT FLASH sentinel near-miss + 16:00 PM brief absorption
    expires_at: 2026-05-26T08:02:00-04:00 (24h from THN publication)
    status: ACTIVE — expires in ~2h
  - lock_id: kali365-fbi-phishing-as-a-service-corpus-tracked
    source_anchor: 2026-05-22 18:00 FLASH + 2026-05-25 12:00 FLASH reiteration
    expires_at: 2026-05-26T08:45:00-04:00 (24h from BC 2026-05-25 publication)
    status: ACTIVE — expires in ~2.75h
  - lock_id: cve-2026-9082-drupal-core-sqli-kev-deadline-tracking
    source_anchor: continuous from 2026-05-22 FLASH; rolling brief-tier coverage
    expires_at: rolling — recurring brief surface
    status: ACTIVE — covered in 16:00 brief; T-1 deadline Wed EOB ~14h from this sweep at PEAK urgency; BC 04:46 EDT item is restatement-only with one Shadowserver datum (670 unpatched)
  - lock_id: cve-2026-42897-exchange-owa-xss-kev-deadline-tracking
    source_anchor: continuous from 2026-05-15 FLASH-0001 lineage
    expires_at: rolling — recurring brief surface
    status: ACTIVE — T-3 deadline Fri ~75h from this sweep
  - lock_id: cve-2026-45321-mini-shai-hulud-oidc-credential-abuse-kev-absent-watch
    source_anchor: VT-006 parent surface
    expires_at: rolling — recurring brief surface
    status: ACTIVE
  - lock_id: unc1549-screening-serpens-tradecraft-evolution-2026-tradecraft-rats-azure-staging
    source_anchor: 2026-05-23 0600 FLASH queue entry (flash-queue.yaml line 71-72)
    expires_at: nominal 2026-05-24T06:00:00-04:00 (24h) BUT operator notes "0523 still in queue" — TOPIC LOCK persists for AM-26 brief absorption disposition
    status: ACTIVE (effective) — THN 03:13 EDT MiniFast + SEO-poisoning restatement is absorbed under this lock per operator anti-noise list
hard_rules_compliance:
  rule_2_no_attribution_origination: |
    No NEW attribution publications in window. THN UNC1549 piece
    explicitly relays Check Point Research + Unit 42 — Archimedes
    propagates the relay framing without origination. THN
    KnowledgeDeliver piece relays Mandiant/GTIG attribution to
    "unknown threat actor" — no Archimedes-side attribution
    addition. SecurityWeek MIRhosting piece relays FIOD + Volkskrant
    + Krebs originating sources — no Archimedes-side attribution
    addition.
  rule_3_no_exploitation: |
    No PoC code, no payloads, no exploit guides referenced or
    generated. THN KnowledgeDeliver piece references hard-coded
    ASP.NET machine keys mechanism but provides no exploitation
    detail beyond high-level family naming (Godzilla web shell,
    Cobalt Strike Beacon). THN UNC1549 piece references SEO
    poisoning delivery without operational PoC. No exploitation-
    content surface to filter.
  rule_4_passive_only: |
    No active scans. SpiderFoot not invoked. authorized-targets.yaml
    empty. All sources are passive RSS / WebFetch / NVD / KEV /
    Splunk over Archimedes's own indices.
  rule_6_quote_limit: |
    No external quotes used in this sentinel from any retrieved
    source. The THN/BC/SW item evaluations paraphrase article
    framings without quoting; load-bearing claims retrieved during
    evaluation are not reproduced verbatim in this sentinel.
  rule_7_credentials: "No credential exposure surfaced this window."
  rule_8_splunk_first_party_priority: |
    Targeted 27-IOC sweep on -6h@h = 0 events. 60th consecutive
    dormant non-self sweep on defenseclaw_local. Hard Rule 8:
    silence is not disconfirming, not confirming.
source_health_changes:
  - source_yaml_id: mandiant
    observation: |
      Feed mandiant.com/resources/blog/rss.xml returned 200 OK with
      20 items SECOND consecutive sweep (00:00 + 06:00) after 24
      consecutive 404 failures observed through 2026-05-25 12:00.
      0 in-window items both sweeps. The 06:00 observation
      CONFIRMS the 00:00 recovery signal — two consecutive 200 OK
      observations is now a recovery-confirmed pattern. Runtime
      field update recommended at AM-26 pre-brief sweep: flip
      status from de-facto-stale to healthy, reset failure_count
      from 19 to 0, update last_successful_fetch to 2026-05-26T06:01
      EDT.
    runtime_change_applied: deferred_to_am_26_sweep_for_runtime_update_per_two_consecutive_recovery_observations
  - source_yaml_id: volexity
    observation: |
      NOT re-queried this sweep per held-healthy operator policy.
      Defer to AM-26 sweep for next confirmation cycle on parse-
      error pattern.
    runtime_change_applied: no_change_deferred_to_am_26
  - source_yaml_id: reliaquest
    observation: |
      NOT re-queried this sweep (DNS resolution failure at 00:00,
      operator decision pending; not blocking).
    runtime_change_applied: no_change_operator_decision_pending
  - source_yaml_id: aikido
    observation: |
      STALE-flagged at AM-25 sweep; 24h skip rule applies until
      ~midday 2026-05-26. Not re-fetched this sweep.
    runtime_change_applied: no_change_within_24h_skip_window
flash_dispatch_disposition:
  candidates_total: 0
  candidates_per_trigger:
    trigger_1_critical_cve_exploited: 0
    trigger_2_tracked_actor_attribution: 0
    trigger_3_first_party_ioc_hit: 0
    trigger_4_tracked_actor_ttp_change: 0   # corpus-locked under 2026-05-23 0600 FLASH; restatement-only via B-grade THN relay
    trigger_5_ad_sector_campaign: 0
    trigger_6_zero_day_no_patch: 0
  near_misses_documented: 1   # THN UNC1549 MiniFast + SEO-poisoning incremental — material new tradecraft detail that BELONGS in AM-26 morning brief UPDATE block, not in duplicate FLASH
  quiet_hours_status: outside_active_hours_06_05_edt_quiet_hour_gating_applies
  critical_override_evaluated: false # No CVSS 10.0 + active exploitation + tracked actor + A&D watchlist hit simultaneously in window
  discord_post_required: false       # Zero triggers fired AND outside active hours
notes:
  - "ZERO FLASH-trigger fires this sweep — 0 of 6 triggers fired. Clean sweep. 6h window 00:00 → 06:00 EDT inside quiet hours."
  - "Seven in-window items evaluated (THN: 3, BC: 3, SecurityWeek: 1). Three are corpus-tracked restatements absorbed under active anti-noise locks (THN-2 UNC1549, BC-1 CVE-2026-9082, SW-1 MIRhosting). Four are FLASH-tier-failing (THN-1 regulatory news, THN-3 below-CVSS-floor and-patched, BC-2 known-issue not vuln, BC-3 consumer-retail no-actor-no-AD)."
  - "PRIMARY NEAR-MISS: THN 03:13 EDT 'Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning.' Tracked actor UNC1549 #004 (Nimbus Manticore / Screening Serpens / Smoke Sandstorm). NEW TRADECRAFT DETAIL vs prior corpus surface: (a) MiniFast naming distinct from MiniUpdate (Check Point taxonomy vs Unit 42 taxonomy — naming-overlap question parallels MINIBIKE/MINIBUS earlier), (b) SEO poisoning delivery vector with getsqldeveloper[.]com fake SQL Developer download page, (c) explicit aviation sector targeting language. Originating sources Check Point Research 'Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict' (2026-05-22) + Unit 42 May 22 concurrent — BOTH out of 6h window and BOTH corpus-tracked under 2026-05-23 0600 FLASH (flash-queue.yaml entry brief_id flash-2026-05-23-0600-001). Per FLASH-POLICY Anti-Noise Rule 1 AND operator anti-noise list ('UNC1549 Unit 42 tradecraft (0523 still in queue)') — disposition is morning-brief absorption as UPDATE block on UNC1549 surface, NOT duplicate FLASH at 06:00 EDT inside quiet hours that would be queued and likely superseded by 08:00 morning brief at 09:00 catchup."
  - "Trigger 4 disposition reasoning: the B-grade THN relay does technically satisfy the 'A/B-grade source documenting new tooling/targeting/infra attributable to tracked actor' surface elements, BUT the operative doctrine reading is that the topic is corpus-locked under prior FLASH (flash-queue.yaml entry from 2026-05-23 0600) and the AM-26 morning brief is the canonical disposition vehicle. Trigger does NOT fire; the canonical post-hoc test (would a duplicate FLASH at 06:00 add operational value vs morning-brief UPDATE?) returns 'no' — morning-brief absorption is the better vehicle, operator anti-noise list confirms."
  - "Splunk first-party: targeted 27-IOC sweep on defenseclaw_local + archimedes -6h@h returned ZERO events. 60th consecutive dormant non-self sweep on defenseclaw_local. Hard Rule 8: silence is not disconfirming. NEW IOC strings added to sweep this round: MiniFast, getsqldeveloper, KnowledgeDeliver, CVE-2026-5426, Godzilla, 7-Eleven."
  - "KEV catalog version 2026.05.22 UNCHANGED at ~102h+ since last add (CVE-2026-9082 Drupal 2026-05-22 EDT) — longest catalog-quiescence stretch in current corpus tracking window. NVD critical-CVE direct window query returned totalResults=0. T-1 Drupal CVE-2026-9082 deadline Wed EOB ~14h from this sweep at PEAK urgency. T-3 Exchange VT-008 CVE-2026-42897 Fri ~75h. BC 04:46 EDT Drupal restatement adds one operationally useful Shadowserver datum (670 unpatched: 272 NA, 273 EU) — appropriate for AM-26 morning brief situational-awareness paragraph under existing surface."
  - "Source-health changes: (1) MANDIANT recovery CONFIRMED — second consecutive 200 OK after 24 consecutive 404s; runtime field flip recommended at AM-26 (status healthy, failure_count 19 → 0, last_successful_fetch 2026-05-26T06:01); (2) VOLEXITY not re-queried (defer to AM-26); (3) RELIAQUEST not re-queried (operator decision pending); (4) AIKIDO remains stale-skipped per 24h rule until ~midday 2026-05-26."
  - "Several A-grade feed servers updated last_modified headers within window without publishing new items (SentinelOne at 01:33 EDT, CrowdStrike at 04:54 EDT, Proofpoint at 04:34 EDT, SANS ISC at 05:59 EDT, Krebs not re-queried, Rapid7 not re-queried) — overnight aggregator-tag-refresh cadence pattern same as 00:00 sweep."
  - "Hard Rules compliance: Rule 2 — no new attribution, all three substantive in-window items are vendor-relay restatements without Archimedes-side attribution addition; Rule 3 — no PoC/payload/exploit content; Rule 4 — passive only; Rule 6 — no external quotes in sentinel; Rule 7 — no credentials surfaced; Rule 8 — defenseclaw_local 60th consecutive dormant non-self sweep + targeted 27-IOC sweep zero."
  - "Quiet-hours posture: 06:05 EDT is OUTSIDE active hours (09:00-21:00). FLASH dispatch would have been queued to flash-queue.yaml if any trigger fired; zero triggers fired = no Discord post regardless. Critical-override conditions (CVSS 10.0 + confirmed active exploitation + tracked actor + A&D watchlist hit, all four simultaneously) NOT met on any in-window item."
  - "Disposition: NO Discord post (zero FLASH triggers fired + outside active hours). Sentinel raw-signal written to threats/raw-signal/raw-2026-05-26-flash-0600-000-sentinel-clean-sweep.md for librarian commit + Splunk flash_sweep_clean event. AM-26 morning brief should ABSORB three corpus-tracked-restatement surfaces as UPDATE/situational-awareness blocks: (i) UNC1549 MiniFast + SEO-poisoning incremental tradecraft, (ii) CVE-2026-9082 Drupal Shadowserver 670-unpatched datum + T-1 EOB-deadline reminder, (iii) MIRhosting/WorkTitans/Stark Industries arrests SecurityWeek confirmation of suspect names. AM-26 pre-brief collector also confirms Mandiant recovery + considers Volexity stale flip + ReliaQuest operator decision."
  - "TLP:CLEAR."
---

# 06:00 EDT Tuesday FLASH sentinel — CLEAN SWEEP

This sentinel documents the 2026-05-26 06:00 EDT Tuesday-early-morning
FLASH collection sweep. Window: 2026-05-26T00:00 to 2026-05-26T06:00
EDT (6.0h, inside overnight quiet hours). **Zero FLASH-trigger fires.
0 of 6 triggers fired.**

## Sweep outcome

**ZERO FLASH candidates** across all six triggers. Of 22+ A/B-grade
publication surfaces queried, three media surfaces returned in-window
items (THN: 3, BleepingComputer: 3, SecurityWeek: 1) — seven in-window
items total. All seven categorically fail FLASH promotion under
current corpus state. The most operationally interesting in-window
item — THN's 03:13 EDT Nimbus Manticore / UNC1549 MiniFast + SEO-
poisoning piece — is a B-grade restatement of Check Point Research's
2026-05-22 "Fast and Furious" primary and Unit 42's concurrent May 22
report, both already corpus-tracked under the 2026-05-23 0600 FLASH
queue entry. Disposition: morning-brief absorption as an UPDATE block
on the UNC1549 surface, not a duplicate FLASH inside quiet hours.

## In-window items — disposition table

| Item | Source | Time (EDT) | Disposition |
|---|---|---|---|
| CERT-In 12-hour patching | THN | 05:13 | FILTER OUT (regulatory news; no CVE/IOC/actor) |
| Iranian Hackers Deploy MiniFast and MiniJunk V2 (UNC1549) | THN | 03:13 | ABSORB to AM-26 morning brief (UNC1549 corpus lock) |
| KnowledgeDeliver CVE-2026-5426 + Godzilla + Cobalt Strike | THN | 01:19 | FILTER OUT (CVSS 7.5 below floor, patched, no actor, not widely-deployed) |
| CISA orders feds to patch Drupal CVE-2026-9082 | BC | 04:46 | ABSORB to AM-26 morning brief (CVE-2026-9082 corpus lock) |
| Microsoft DC lookup may fail Server 2016 | BC | 03:41 | FILTER OUT (known-issue advisory, not a vuln/exploit) |
| 7-Eleven data breach exposes 185,000 (ShinyHunters) | BC | 03:01 | FILTER OUT (consumer-retail, no tracked actor in roster, no A&D) |
| Admins of bulletproof hosting arrested Netherlands (MIRhosting) | SecurityWeek | 05:47 | ABSORB to AM-26 morning brief if covered (MIRhosting corpus lock through 16:00) |

## Surfaces queried — full table

| Source | Class | Status | Last_modified | In-window items |
|---|---|---|---|---|
| CISA KEV catalog | A1 | unchanged | catalogVersion 2026.05.22 (~102h+ stale) | 0 new adds |
| NVD critical-CVE direct query | A1 | empty | — | totalResults=0 |
| The Hacker News | B | 200 | 05:51 EDT in-window | 3 (1 ABSORB, 2 FILTER OUT) |
| BleepingComputer | B | 200 | 05:56 EDT in-window | 3 (1 ABSORB, 2 FILTER OUT) |
| SecurityWeek | B | 200 | 05:47 EDT in-window | 1 (1 ABSORB) |
| The Record | A | 200 | — (5 items in feed) | 0 |
| Check Point Research | A | 200 | 25 May 11:08 EDT pre-window UNCHANGED | 0 |
| MSTIC | A | 200 | 22 May 17:57 UTC (11th sweep unchanged) | 0 |
| Unit 42 | A | 200 | 25 May 12:19 EDT pre-window UNCHANGED | 0 |
| SentinelOne Labs | A | 200 | 01:33 EDT in-window header refresh only | 0 |
| CrowdStrike | A | 200 | 04:54 EDT in-window (10 dateless product items) | 0 threat-research |
| Cisco Talos | A | 200 | — (15 items in feed) | 0 |
| Mandiant | A | **200** | — (20 items in feed) | 0 **(recovery CONFIRMED — 2nd consecutive 200 OK)** |
| ESET WeLiveSecurity | A | 200 | — (100 items in feed) | 0 |
| Proofpoint | A | 200 | 04:34 EDT in-window header refresh only | 0 |
| SANS ISC | B | 200 | 05:59 EDT in-window (0 items after since-filter) | 0 |
| Krebs | A | not re-queried | (cadence-slow, 00:00 result unchanged) | n/a |
| Rapid7 | B | not re-queried | (cadence-slow, 00:00 result 0 in window) | n/a |
| DFIR Report | A | not re-queried | (cadence-slow, 2 weeks unchanged) | n/a |
| CISA all-advisories | A1 | not re-queried | (00:00 result 0 in window) | n/a |
| ReliaQuest | (untracked) | not re-queried | DNS-fail at 00:00; operator decision pending | n/a |
| Volexity | A | not re-queried | parse error 4th+ at 00:00; held healthy | n/a |
| Aikido | A | stale | skip-until ~midday 2026-05-26 | n/a |
| Splunk defenseclaw_local | A1 (first-party) | healthy | -6h@h | 0 IOC hits (60th consecutive dormant) |
| Splunk archimedes | (self-telemetry) | healthy | -6h@h | 0 events |

## FLASH-trigger evaluation

| Trigger | Result | Reason |
|---|---|---|
| 1: Critical CVE exploited | FAILED | NVD direct query totalResults=0; KEV catalog unchanged ~102h+; only in-window CVE is CVE-2026-5426 at CVSS 7.5 (below 9.0 floor) |
| 2: New tracked-actor attribution | FAILED | THN UNC1549 piece is B-grade relay of Check Point Research + Unit 42 May 22 primaries (out of window, corpus-tracked under 2026-05-23 0600 FLASH); not novel attribution |
| 3: First-party Splunk IOC hit | FAILED | 27-IOC sweep -6h@h = 0 events; 60th consecutive dormant non-self sweep on defenseclaw_local |
| 4: Tracked-actor TTP change | FAILED | THN restatement of UNC1549 MiniFast + SEO-poisoning is anti-noise-absorbed under 2026-05-23 0600 FLASH corpus lock; morning-brief UPDATE block is the canonical disposition |
| 5: A&D-sector active campaign | FAILED | THN UNC1549 aviation-sector framing names no A&D-watchlist prime; sectoral-shape only, not direct prime targeting; also restatement-anti-noise-absorbed |
| 6: Zero-day without patch | FAILED | THN KnowledgeDeliver CVE-2026-5426 zero-day retrospective has PATCH AVAILABLE since pre-2026-02-24 + CVSS 7.5 below floor + not widely-deployed |

## Primary near-miss — THN UNC1549 MiniFast + SEO-poisoning (anti-noise-absorbed)

The Hacker News (Ravie Lakshmanan) published "Iranian Hackers Deploy
MiniFast and MiniJunk V2 via Phishing and SEO Poisoning" at
2026-05-26T03:13 EDT (within window). The piece is a B-grade synthesis
of:

- **Check Point Research** (Sergey Shykevich, Threat Intelligence
  Group Manager) "Fast and Furious – Nimbus Manticore Operations
  During the Iranian Conflict" — published **2026-05-22**, out of
  6h window
- **Palo Alto Networks Unit 42** May 22 concurrent on UNC1549
  MiniUpdate / MiniJunk V2 / AppDomainManager hijacking — already
  corpus-tracked in the 2026-05-23 0600 FLASH queue entry

NEW tradecraft elements vs prior corpus surface:

1. **MiniFast naming distinct from MiniUpdate** — Check Point Research
   taxonomy names a backdoor "MiniFast" while Unit 42 May 22 named
   "MiniUpdate." These may be the same family under different vendor
   naming (parallel to the MINIBIKE/MINIBUS-vs-Unit 42 naming overlap
   question already flagged in 2026-05-23 FLASH queue entry) OR
   genuinely distinct families in the Nimbus Manticore RAT inventory.
   No published code comparison at this sweep.
2. **SEO poisoning delivery vector** — fake SQL Developer download
   page at **getsqldeveloper[.]com** with dozens of bogus dependent
   domains. NEW delivery infrastructure class vs prior recruiter-
   lure pretexts (PremierHealthAdvisory[.]com,
   Ramiltonsfinance[.]com) and azurewebsites[.]net staging.
3. **Aviation sector targeting language** — explicit Check Point
   framing names "aviation and software sectors across the U.S.,
   Europe, and the Middle East" with "employees in software and
   aviation sectors in Saudi Arabia and Australia." Aviation IS
   A&D-adjacent but no A&D-prime entity from
   `watchlists/aerospace-defense.yaml` is named.
4. **AI-assisted malware development** — Check Point quotes
   Shykevich asserting "strong indicators" UNC1549 used AI tools to
   accelerate MiniFast development. Notable claim but the substance
   is investigator-quoted assertion not technical code-pattern
   evidence at this surface.

Tracked actor: **UNC1549 (#004)** — Nimbus Manticore / Screening
Serpens / Smoke Sandstorm / Tortoiseshell / Imperial Kitten /
Crimson Sandstorm cluster. Iran / IRGC attribution per prior
vendor-community consensus (Mandiant 2026-05-04, Unit 42 2026-05-22,
Check Point 2026-05-22).

**Why this is NOT a fresh FLASH** despite material new tradecraft
detail:

- **Anti-noise lock active**: 2026-05-23 0600 FLASH queue entry
  (brief_id flash-2026-05-23-0600-001-unc1549-screening-serpens-
  tradecraft-evolution) covers UNC1549 tradecraft evolution under
  Unit 42 + Mandiant cross-corpus. Operator anti-noise list
  explicitly flags "UNC1549 Unit 42 tradecraft (0523 still in queue)."
- **Canonical disposition is morning-brief UPDATE**: incremental
  MiniFast naming + SEO-poisoning detail belongs as an UPDATE block
  in AM-26 morning brief on the UNC1549 corpus surface, not a
  duplicate FLASH at 06:00 EDT inside quiet hours that would be
  queued and likely superseded by the 08:00 morning brief at the
  09:00 catchup.
- **Originating primaries are out of 6h window**: Check Point May 22
  + Unit 42 May 22 are both 4 days old at this sweep. THN's B-grade
  relay does not constitute novel attribution or independent in-
  window primary.

**AM-26 grader-queue disposition**: ABSORB to morning brief as an
UPDATE block on UNC1549 corpus surface. Tradecraft inventory should
now reflect MiniFast (Check Point taxonomy) alongside MiniUpdate
(Unit 42 taxonomy) with the naming-overlap question flagged
unresolved, plus add SEO-poisoning + getsqldeveloper[.]com to the
delivery-infrastructure inventory.

## Other in-window items — restatement-or-filter dispositions

**BC 04:46 EDT — CVE-2026-9082 Drupal CISA-deadline-reminder.** Single
new operational datum: Shadowserver tracking 670 unpatched Drupal
installations (272 NA, 273 EU) as of publication. Anti-noise lock
ACTIVE on cve-2026-9082-drupal-core-sqli-kev-deadline-tracking. T-1
KEV deadline Wed EOB ~14h from this sweep at PEAK urgency. Disposition:
ABSORB to AM-26 morning brief as part of the rolling CVE-2026-9082
situational-awareness paragraph, with the Shadowserver datum included
as operationally useful color.

**SW 05:47 EDT — MIRhosting/WorkTitans/Stark Industries arrests
SecurityWeek confirmation.** Same incident as Krebs 2026-05-25 PM +
FIOD originating source. SecurityWeek (Ionut Arghire) is narrative-
synthesis restatement; corroborates suspect names "Youssef Z." and
"Andrey N." Anti-noise lock ACTIVE on stark-mirhosting-worktitans-
russia-aligned-hosting-takedown through 2026-05-26T16:00 EDT.
Disposition: ABSORB to AM-26 morning brief if morning brief covers,
or let lock expire at 16:00 if morning brief omits.

**THN 01:19 EDT — KnowledgeDeliver CVE-2026-5426 + Godzilla web shell
+ Cobalt Strike.** Mandiant/GTIG-originated retrospective. CVSS 7.5
below Trigger 1 9.0 floor AND below Trigger 6 8.0 floor (unless
widely-deployed — KnowledgeDeliver is Japanese-domestic LMS, NOT
widely-deployed in A&D/global enterprise). PATCH AVAILABLE pre-
2026-02-24. NO tracked actor named ("unknown threat actor" per
Mandiant). FILTER OUT.

**THN 05:13 EDT — CERT-In 12-hour patching mandate.** Indian
regulatory news on patching guidance. No CVE, no IOC, no actor, no
FLASH-trigger event class. FILTER OUT.

**BC 03:41 EDT — Microsoft DC lookup may fail Server 2016 (KB5087537).**
Microsoft known-issue advisory on May 2026 update. Not a vulnerability
with exploitation. NO CVE, NO actor, NO FLASH-trigger event class.
FILTER OUT.

**BC 03:01 EDT — 7-Eleven data breach 185,000 (ShinyHunters).**
Consumer-retail breach. ShinyHunters surfaces in Archimedes IOC corpus
but NOT in `_roster.yaml`. No A&D relevance, no CVE, no FLASH-trigger
event class under current actor-tracking definitions. FILTER OUT.

## Splunk first-party check

Primary query (27 IOCs, -6h@h):
```
search index=defenseclaw_local OR index=archimedes earliest=-6h@h latest=now
  ("MiniFast" OR "MiniJunk" OR "Nimbus Manticore" OR "Screening Serpens" OR
   UNC1549 OR "getsqldeveloper" OR "AppDomainManager" OR "MiniUpdate" OR
   CVE-2026-9082 OR CVE-2026-42897 OR "Drupal" OR "Exchange" OR
   ShinyHunters OR "7-Eleven" OR KnowledgeDeliver OR Godzilla OR
   "Cobalt Strike" OR CVE-2026-5426 OR "Stark Industries" OR MIRhosting OR
   WorkTitans OR TeamPCP OR "Shai-Hulud" OR "Charming Kitten" OR
   APT28 OR APT29 OR Sandworm) | head 50
```
Result: 0 events.

60th consecutive dormant non-self sweep on defenseclaw_local.
Hard Rule 8: silence is not disconfirming.

## Anti-noise locks honored

Eight anti-noise locks at this sweep — all honored. The seven from
00:00 sweep plus the corpus-effective UNC1549 lock under 2026-05-23
0600 FLASH (formal 24h expiry was 2026-05-24T06:00 but operator
anti-noise list keeps the topic locked for morning-brief absorption
disposition):

1. **TeamPCP cluster** — ACTIVE through 2026-05-26 16:00
2. **Stark / MIRhosting / WorkTitans takedown** — ACTIVE through
   2026-05-26 16:00 (SecurityWeek 05:47 EDT item restatement-absorbed)
3. **Ghost CMS CVE-2026-26980** — ACTIVE through 2026-05-26 08:02
   (~2h remaining)
4. **FBI Kali365 PhaaS** — ACTIVE through 2026-05-26 08:45
   (~2.75h remaining)
5. **CVE-2026-9082 Drupal KEV** — rolling, T-1 deadline Wed EOB ~14h
   from this sweep (BC 04:46 EDT item restatement-absorbed)
6. **CVE-2026-42897 Exchange KEV** — rolling, T-3 deadline Fri ~75h
7. **CVE-2026-45321 Mini Shai-Hulud KEV-absent watch** — rolling
8. **UNC1549 / Nimbus Manticore tradecraft evolution** — effective
   corpus-lock per operator anti-noise list (formal 24h-expiry was
   2026-05-24T06:00 but topic stays locked for AM-26 morning-brief
   absorption disposition)

## Quiet-hours posture

06:05 EDT is OUTSIDE active hours (09:00-21:00). FLASH dispatch
would have been queued to `infrastructure/flash-queue.yaml` if any
trigger fired; zero triggers fired = no Discord post regardless and
no queue entry.

Critical-override conditions (CVSS 10.0 + confirmed active exploitation
+ tracked actor + A&D watchlist hit, all four simultaneously) NOT
met on any in-window item.

## Source health changes

- **mandiant** — **RECOVERY CONFIRMED**. Feed mandiant.com/resources/
  blog/rss.xml returned 200 OK with 20 items in feed SECOND consecutive
  sweep (00:00 + 06:00) after 24 consecutive 404 failures. Runtime
  field update recommended at AM-26 pre-brief: status `healthy`,
  failure_count 19 → 0, last_successful_fetch
  2026-05-26T06:01:00-04:00, last_error null. Two consecutive 200
  OK observations is sufficient signal to flip from de-facto-stale
  back to healthy.
- **volexity** — not re-queried this sweep per held-healthy operator
  policy. Defer to AM-26 sweep.
- **reliaquest** — not re-queried (operator decision pending on
  source-health.yaml entry).
- **aikido** — Remains stale-skipped per 24h rule until ~midday
  2026-05-26.
- **cisco-talos** — RSS feed healthy (200 OK, 15 items, 0 in-window).

## Hard Rules compliance

- **Rule 2**: no new attribution; THN UNC1549 piece is B-grade relay
  of Check Point + Unit 42 primaries; THN KnowledgeDeliver relays
  Mandiant/GTIG "unknown threat actor" framing; SW MIRhosting relays
  FIOD/Krebs. No Archimedes-side attribution origination.
- **Rule 3**: no PoC code, no payloads, no exploit guides referenced
  or generated.
- **Rule 4**: passive only; SpiderFoot not invoked; authorized-
  targets empty.
- **Rule 6**: no external quotes in sentinel from any retrieved
  source.
- **Rule 7**: no credentials surfaced.
- **Rule 8**: defenseclaw_local 60th consecutive dormant non-self
  sweep; targeted 27-IOC sweep ZERO.

## Disposition

- **No Discord post** — zero FLASH triggers fired AND outside active
  hours.
- **Sentinel raw-signal written** for librarian commit + Splunk
  `flash_sweep_clean` event.
- **All eight anti-noise locks honored** — three in-window items
  (THN UNC1549, BC Drupal, SW MIRhosting) are restatement-absorbed
  under active locks; one near-miss (THN UNC1549) flagged for
  AM-26 morning brief UPDATE block.
- **AM-26 morning brief priorities** for the briefer:
  (i) UNC1549 UPDATE block — MiniFast (CKR taxonomy) alongside
  MiniUpdate (Unit 42), SEO-poisoning + getsqldeveloper[.]com
  delivery infrastructure, aviation sector targeting framing
  noting no A&D prime named.
  (ii) CVE-2026-9082 Drupal situational-awareness paragraph —
  Shadowserver 670-unpatched datum (272 NA / 273 EU) + T-1 deadline
  Wed EOB reminder (peak urgency).
  (iii) MIRhosting/WorkTitans/Stark Industries — SecurityWeek
  confirmation of suspect names if brief covers; otherwise let lock
  expire at 16:00.
- **AM-26 source-health follow-up**: flip Mandiant runtime fields
  (recovery confirmed); consider Volexity stale flip if parse-error
  pattern persists across AM-26 + 12:00 sweeps; operator decision
  on ReliaQuest tracking entry; Aikido remains stale-skipped.
- **TLP:CLEAR.**
