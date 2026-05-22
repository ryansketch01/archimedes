---
raw_id: raw-2026-05-22-flash-0600-000-sentinel-clean-sweep
collected_at: 2026-05-22T06:05:00-04:00
run_id: flash-sweep-20260522-060000
collection_mode: flash_sweep
sentinel: true
flash_candidate: false
test: false
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel (clean sweep, late-overnight window)"
  source_url: null
  published_at: 2026-05-22T06:05:00-04:00
sweep_window:
  start: 2026-05-22T00:00:00-04:00
  end: 2026-05-22T06:00:00-04:00
sources_queried:
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — catalog version 2026.05.21 with same 2 entries dated 2026-05-21 (CVE-2026-34926 Trend Micro Apex One + CVE-2025-34291 Langflow). NO new entries dated 2026-05-22. Both 2026-05-21 entries ABSORBED by 2026-05-21 16:00 afternoon brief finding-2026-05-21-0008 (anti-noise lock active through 2026-05-22T16:00 EDT). 0 new entries in 6h window.
  - cisa-advisories        # all.xml fetch_feed 200, 30 items in feed, 0 in 6h window since 2026-05-22T00:00 EDT
  - msrc-cvrf              # WebFetch api.msrc.microsoft.com/cvrf/v3.0/updates — top 5 entries all show CurrentReleaseDate 2026-05-22T01:42–01:48 UTC (= 2026-05-21T21:42–21:48 EDT, PRE-window by ~12–18 min). All are metadata refreshes of older bundles (2026-May, 2026-Mar, 2025-Sep, 2025-May, 2025-Feb) — NOT new out-of-band releases. Pattern is the monthly CVRF index refresh, not new disclosures. 0 in-window new releases.
  - nvd                    # WebFetch services.nvd.nist.gov rest cves 2.0 lastModStartDate 2026-05-22T04:00Z lastModEndDate 2026-05-22T10:00Z cvssV3Severity=CRITICAL — 1 candidate returned: CVE-2023-3616 (Mava Hotel Management System SQL Injection, CVSS 9.8, original publish 2023-09-05, lastModified 2026-05-22T08:16Z); 2023-era disclosure with NVD metadata refresh today. Turkish hotel-management software; not A&D, not widely-deployed; no in-window ITW exploitation claim; evaluated against Trigger 1 + Trigger 6 — FAILS both prongs (no A-grade source — single USOM/Siberguvenlik reference; 2.5-year-old disclosure; niche commercial sector not A&D-adjacent); DISCARDED per Mode 1
  - drupal-sa              # fetch_feed returned XML parse error ("mismatched tag" at line 26 col 289); fallback WebFetch on drupal.org/security listed most recent advisories — SA-CORE-2026-004 (2026-05-20, pre-window, already in 2026-05-21 morning brief finding-0004 lock through 2026-05-22T08:00 EDT) + PSA-2026-05-18 (2026-05-18, pre-window, already covered) + SA-CONTRIB-2026-035/036/037 (2026-05-13, pre-window). 0 new advisories in 6h window.
  - mstic                  # Microsoft Security Blog feed 200, last_modified 2026-05-21T21:29 GMT (= 17:29 EDT 2026-05-21, PRE-window by 6.5 hours), 0 in-window items
  - unit42                 # feedburner 200, last_modified 2026-05-21T16:27 GMT (= 12:27 EDT 2026-05-21, well pre-window), 0 in-window items
  - mandiant               # feedburner persistent 404 (now ~21+ consecutive sweeps; held healthy pending operator alt-endpoint decision per source-health.yaml notes). NOT re-attempted this sweep per stale-skip rule (stale-since not yet set but pattern indistinguishable from deep staleness).
  - cisco-talos            # blog.talosintelligence.com/feeds/posts/default returned 404 (different endpoint than blog.talosintelligence.com root); MCP fetch_feed error. Talos main blog last successful fetch via rssbridge was 2026-05-21 18:00 sentinel; A-grade source surface; flagged for next sweep recovery probe. 0 in-window items via this attempt.
  - sentinel-one-labs      # sentinelone.com/labs/feed/ 200, last_modified 2026-05-21T16:47 GMT (= 12:47 EDT 2026-05-21, well pre-window), 0 in-window items
  - welivesecurity         # ESET WeLiveSecurity feed 200, 0 in-window items per since filter (last_modified null, 100 items total in feed — Webworm/EchoCreep/GraphWorm ESET research from 2026-05-20 is in feed but PRE-window; already in raw-2026-05-20-flash-1200-001 + 2026-05-20 afternoon brief absorption)
  - crowdstrike            # crowdstrike.com/blog/feed/ 200, last_modified 2026-05-22T05:10 GMT (= 01:10 EDT, INSIDE window), 10 items total with null published timestamps in feed (identical entry set to 00:00 + 18:00 sentinels — Claude integration product post, Identity/Infostealers product post, Financial Services Threat Landscape Report, Falcon AIDR Kubernetes AI Apps, May 2026 Patch Tuesday retrospective, Automated Leads product, Gartner MQ CTI, Falcon OverWatch for Defender, Technical Risk Assessments, AI-Powered Vulnerability Discovery); no in-window NEW research on tracked actors / CVEs / A&D campaigns; same disposition as 00:00 sentinel
  - sophos-threat-research # sophos.com/news threat-research feed — same entrenched pattern, 0 in-window items
  - github-blog-security   # github.blog/security/feed/ 200, last_modified 2026-05-22T00:23 GMT (= 2026-05-21T20:23 EDT, PRE-window by 3.5h), 0 in-window items per since filter
  - bleepingcomputer       # RSS feed 200, last_modified 2026-05-22T09:51 GMT (= 05:51 EDT, INSIDE window), 1 in-window item — "US and Canada arrest and charge suspected Kimwolf botnet admin" (Sergiu Gatlan 09:01 GMT / 05:01 EDT); law enforcement DDoS-botnet arrest of Jacob Butler / Dort (Ottawa, Canada); botnet KimWolf assessed as AISURU variant infecting ~2M devices; NOT a roster actor (KimWolf not in _roster.yaml); no CVE; no A&D-named target; evaluated against Trigger 2 (tracked actor attribution) — FAILS on no-roster-actor prong; categorically off-filter for all 6 triggers; DISCARDED per Mode 1
  - thehackernews          # feedburner 200, last_modified 2026-05-22T09:06 GMT (= 05:06 EDT, INSIDE window), 3 in-window items: (a) "Kimwolf DDoS Botnet Operator Arrested in Canada" (08:50 GMT / 04:50 EDT) — same KimWolf arrest as BleepingComputer, parallel coverage, DISCARDED per Mode 1 categorical-fail Trigger 2; (b) "CISA Adds Exploited Langflow and Trend Micro Apex One Vulnerabilities to KEV" (05:47 GMT / 01:47 EDT) — KEV double-add media-relay on 2026-05-21 CISA additions; ABSORBED by 2026-05-21 16:00 afternoon brief finding-0008 (lock through 2026-05-22T16:00 EDT); DEDUP; (c) "Cisco Patches CVSS 10.0 Secure Workload REST API Flaw" (05:36 GMT / 01:36 EDT) — CVE-2026-20223 media-relay; ABSORBED by 2026-05-20 16:00 afternoon brief finding-2026-05-20-0001 + 2026-05-20 PM raw-signal raw-2026-05-20-pm-002-cisco-psirt-cve-2026-20223; nominal anti-noise lock from 2026-05-20 expired 2026-05-21T16:00 but topic remains carry-forward dedup via brief inclusion (no new exploitation-status change, no new patch revision, no actor attribution); DEDUP per FLASH anti-noise rule 1 ("one FLASH per trigger topic per 24h" extended via brief absorption)
  - securityweek           # RSS feed 200, last_modified 2026-05-22T09:24 GMT (= 05:24 EDT, INSIDE window), 3 in-window items: (a) "First VPN Cybercrime Service Disrupted, Administrator Arrested" (Eduard Kovacs 09:24 GMT / 05:24 EDT) — FBI law enforcement takedown of First VPN cybercrime service used by ransomware groups for network reconnaissance; ALREADY in 2026-05-21 12:00 sentinel discard and 2026-05-21 18:00 sentinel discard (Security Affairs surface 2026-05-21 13:57 EDT); now SecurityWeek + The Record continuing media-relay coverage; not roster actor, no CVE; categorically off-filter for all 6 triggers; DISCARDED per Mode 1; (b) "TrendAI Patches Apex One Zero-Day Exploited in the Wild" (08:19 GMT / 04:19 EDT) — CVE-2026-34926 Apex One on-prem path traversal; ABSORBED by 2026-05-21 16:00 afternoon brief finding-0008 (lock through 2026-05-22T16:00 EDT); DEDUP; (c) "Grafana Says Codebase and Other Data Stolen via TanStack Supply Chain Attack" (Ionut Arghire 07:49 GMT / 03:49 EDT) — Grafana official disclosure that attackers accessed GitHub repositories on 2026-05-11 via an unrotated GitHub workflow token compromised during TanStack/TeamPCP/Mini Shai-Hulud attack; ransom demand received 2026-05-16 and refused; public disclosure 2026-05-22; NEW victim named (first public Grafana naming) but ABSORBED by active anti-noise locks (a) 2026-05-21 morning brief findings 0002 + 0007 TeamPCP/TanStack/Nx Console campaign chain lock through 2026-05-22T08:00 EDT + (b) 2026-05-20 12:00 FLASH raw-2026-05-20-flash-1200-002 already covered "Grafana/TanStack token rotation continuation" surface; DEDUP per FLASH anti-noise rule 1; handoff to 2026-05-22 morning brief composer as new victim-named UPDATE block candidate on finding-0002 chain
  - therecord              # feed 200, 1 in-window item — "CISA to allow researchers to report vulnerabilities to exploited bugs catalog" (Suzanne Smalley feed-future-dated 2026-05-23T01:11 UTC, also surfaced in 00:00 sentinel discard); ALREADY in 2026-05-22 00:00 sentinel + 2026-05-21 12:00 sentinel discards; procedural CISA policy announcement; categorically off-filter; DISCARDED per Mode 1
  - sans-isc               # RSS feed 200, last_modified 2026-05-22T09:59 GMT (= 05:59 EDT, INSIDE window), 1 in-window item — "Cross-Platform NPM Stealer, Fri May 22nd" (Xavier Mertens diary; SHA256 049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9); static analysis of obfuscated Node.js stealer targeting Windows (WSL) + macOS + Linux with browser-credential / Chrome-extension wallet / npm-related capabilities; no actor attribution; no CVE; no campaign claim; no A&D-named target; npm-adjacent IOC potentially related to broader TeamPCP/Shai-Hulud npm ecosystem but no explicit attribution; B-grade SANS diary; evaluated against Trigger 4 (tracked-actor TTP change) — FAILS on attributable-tracked-actor prong; evaluated against Trigger 5 (A&D-sector campaign) — FAILS on multi-victim + A&D-named prong; DISCARDED per Mode 1; fresh IOC handoff to /ioc-hunt consideration if operator wants to check master-index for hash overlap with Mini Shai-Hulud master-index hashes
  - krebs                  # feed 200, last_modified 2026-05-21T21:50 GMT (pre-window), 0 in-window items
  - dark-reading           # rss.xml 200, last_modified 2026-05-22T10:02 GMT, 3 in-window items: (a) "China's Webworm Uses Discord, Microsoft Graphs to Hack EU Govts" (Alexander Culafi 07:01 GMT / 03:01 EDT) — Dark Reading continuing coverage of ESET Webworm/EchoCreep/GraphWorm research from 2026-05-20; Space Pirates / UAT-8302 / Webworm targeting Belgium, Italy, Poland, Serbia, Spain government organizations in 2025; NOT a roster actor (Webworm/Space Pirates not in _roster.yaml; deferred to actor-profiler /new-actor consideration as previously noted in 2026-05-20 12:00 FLASH); ABSORBED by raw-2026-05-20-flash-1200-001-thn-webworm-echocreep-graphworm-china-aligned.md raw-signal and absorbed in 2026-05-20 afternoon brief coverage; DEDUP per FLASH anti-noise rule 1; (b) "Infosecurity Europe" event listing (future event 2026-06-02) — off-filter administrative entry; DISCARDED per Mode 1; (c) "Anatomy of a Data Breach" virtual event registration (future event 2026-06-18) — off-filter; DISCARDED per Mode 1
  - securityaffairs        # feedburner 200, last_modified 2026-05-22T09:56 GMT (= 05:56 EDT, INSIDE window), 1 in-window item — "One Telecom Provider Hosted Most of the Middle East's Active C2 Infrastructure" (Pierluigi Paganini 07:29 GMT / 03:29 EDT) — Hunt.io infrastructure-mapping report; 1,350+ C2 servers across 98 providers in 14 ME countries; STC accounted for 72.4% of regional C2; references Eagle Werewolf cluster (NOT in _roster.yaml — Russia/Iran-nexus suspected per prior reporting, not currently tracked), DYNOWIPER targeting Poland energy sector (not A&D), commodity tooling families (Cobalt Strike, AsyncRAT, Sliver, Mirai, Mozi, Hajime, Tactical RMM, Gophish); no roster actor attribution; no A&D-named victim; no campaign explicitly targeting A&D primes; evaluated against Trigger 2 (no roster actor), Trigger 4 (no roster TTP), Trigger 5 (no A&D-named multi-victim campaign) — FAILS all; categorically off-filter for all 6 triggers; DISCARDED per Mode 1; potential actor-profiler /new-actor candidate for Eagle Werewolf if operator interested (separate workflow, not FLASH)
  - splunk-first-party     # archimedes + defenseclaw_local indexes -24h, 0 non-self events (event_count 0); 55th consecutive dormant non-self sweep. Splunk reachability not separately health-checked this sweep but query returned valid empty result set.
trigger_evaluation:
  trigger_1_critical_cve_exploited:
    fired: false
    reason: |
      One in-window CVSS ≥ 9.0 candidate evaluated and rejected via NVD
      lastModified path:

      CVE-2023-3616 (Mava Hotel Management System SQL Injection, CVSS 9.8)
      surfaced via NVD lastModified refresh at 2026-05-22T08:16Z in window
      but original publish was 2023-09-05 — 2.5-year-old disclosure with
      NVD metadata refresh today. FAILS Trigger 1 on multiple prongs:

      (1) NO A-grade source. Single USOM/Siberguvenlik reference (Turkish
      national cybersecurity authority); not in Archimedes A-grade tier
      (Mandiant / Unit 42 / MSTIC / CrowdStrike / CISA / Cisco Talos /
      ESET / SentinelLabs).

      (2) NO active in-the-wild exploitation claim in window. The 2023
      disclosure surface is old; no new ITW campaign / actor / observed
      exploitation cited in any in-window media.

      (3) NOT widely-deployed in A&D context. Mava Hotel Management
      System is a niche commercial-sector application (Turkish hospitality
      industry); A&D primes do not run hotel-management software on
      production estate.

      Categorical Trigger 1 failure. DISCARD per Mode 1.

      Two media-relay candidates also evaluated:

      (a) CISA KEV 2026-05-21 double-add (Apex One CVE-2026-34926 +
      Langflow CVE-2025-34291) covered by SecurityWeek "TrendAI Patches
      Apex One Zero-Day Exploited in the Wild" + Hacker News "CISA Adds
      Exploited Langflow and Trend Micro Apex One Vulnerabilities to
      KEV". KEV inclusion satisfies active-exploitation prong by CISA
      criterion, but ABSORBED by 2026-05-21 16:00 afternoon brief
      finding-0008 (anti-noise lock active through 2026-05-22T16:00
      EDT). DEDUP per FLASH anti-noise rule 1.

      (b) Cisco Secure Workload CVE-2026-20223 (CVSS 10.0) media-relay
      via Hacker News "Cisco Patches CVSS 10.0 Secure Workload REST API
      Flaw". CVE was ABSORBED by 2026-05-20 16:00 afternoon brief
      finding-2026-05-20-0001 + 2026-05-20 PM raw-signal raw-2026-05-20
      -pm-002. Nominal anti-noise lock from 2026-05-20 expired 2026-05-
      21T16:00 EDT but topic remains carry-forward DEDUP via brief
      absorption — no new exploitation-status change, no new patch
      revision, no actor attribution since brief publication. DEDUP per
      FLASH anti-noise rule 1.

      The CISA KEV catalog holds the same 2 entries from 2026-05-21
      unchanged (Apex One CVE-2026-34926 + Langflow CVE-2025-34291);
      no new KEV additions in 6h window.

      No A-grade source attests NEW active in-the-wild exploitation of a
      CVSS ≥ 9.0 CVE in window outside existing anti-noise locks.
  trigger_2_tracked_actor_attribution:
    fired: false
    reason: |
      No in-window item attributes NEW activity to any of the 24 actors
      in _roster.yaml (TeamPCP, Stardust Chollima, Lazarus, UNC1549,
      GlassWorm, APT28, Sandworm, Volt Typhoon, APT29, Salt Typhoon,
      Charming Kitten, Miyako, Scattered Spider, Handala Hack, LockBit,
      REvil, APT40, Cl0p, APT41, BlackCat/ALPHV, Payouts King,
      MuddyWater, APT34, APT37).

      One in-window item NAMES a tracked roster actor (TeamPCP) but is
      DEDUP'd via active anti-noise lock:

      SecurityWeek "Grafana Says Codebase and Other Data Stolen via
      TanStack Supply Chain Attack" (Ionut Arghire 03:49 EDT). Grafana
      Labs official disclosure naming themselves as a victim of the
      TanStack/TeamPCP/Mini Shai-Hulud supply chain attack; one
      unrotated GitHub workflow token compromised on 2026-05-11
      enabled attackers to access GitHub repositories; ransom demand
      received 2026-05-16 and refused; public disclosure 2026-05-22.
      NEW victim publicly named (first public Grafana naming as
      TanStack-chain victim). TeamPCP IS in _roster.yaml (#001).

      However, ABSORBED by ACTIVE anti-noise locks:

      (a) 2026-05-21 morning brief findings 0002 + 0007 — TeamPCP /
      TanStack / Nx Console campaign chain lock active through 2026-05-
      22T08:00 EDT covering all attribution + TTP surfaces on the
      campaign.

      (b) 2026-05-20 12:00 FLASH raw-2026-05-20-flash-1200-002 —
      BleepingComputer "Grafana TanStack token rotation continuation"
      already covered the Grafana token-rotation-failure surface at the
      time it was first detected.

      DEDUP per FLASH anti-noise rule 1 ("one FLASH per trigger topic
      per 24h"). Grafana-specific victim naming is a useful UPDATE-block
      handoff to 2026-05-22 morning brief composer (8:00 EDT) — but the
      campaign chain itself is already covered, and a fresh FLASH on
      "TeamPCP/TanStack adds Grafana victim" within the same active
      lock would constitute noise.

      Two in-window items reference NON-ROSTER actors:

      (i) BleepingComputer + Hacker News parallel coverage of KimWolf
      DDoS botnet operator arrest (Jacob Butler / Dort, Canadian).
      KimWolf assessed AISURU variant. KimWolf NOT in _roster.yaml.
      Law enforcement event; no new attribution; categorical Trigger 2
      failure. DISCARDED per Mode 1.

      (ii) Dark Reading "China's Webworm Uses Discord, Microsoft Graphs
      to Hack EU Govts" — continuing coverage of ESET research from
      2026-05-20 on Webworm / Space Pirates / UAT-8302 EchoCreep and
      GraphWorm backdoors targeting EU government organizations
      (Belgium, Italy, Poland, Serbia, Spain). Webworm / Space Pirates
      NOT in _roster.yaml; previously deferred to actor-profiler
      /new-actor consideration in 2026-05-20 12:00 FLASH. ABSORBED by
      raw-2026-05-20-flash-1200-001 + 2026-05-20 afternoon brief
      coverage. DEDUP.

      (iii) Security Affairs "One Telecom Provider Hosted Most of ME
      C2 Infrastructure" (Pierluigi Paganini) — Hunt.io report
      references Eagle Werewolf cluster (NOT in _roster.yaml).
      DISCARDED per Mode 1; potential actor-profiler /new-actor
      candidate for Eagle Werewolf as separate workflow.

      No NEW tracked-roster-actor attribution in window outside
      existing anti-noise locks.
  trigger_3_first_party_ioc_hit:
    fired: false
    reason: |
      Splunk query on archimedes + defenseclaw_local indexes (-24h,
      excluding archimedes:* self-telemetry) returned 0 events. 55th
      consecutive dormant non-self sweep at this run. Per Hard Rule 8:
      silence is neither confirming nor disconfirming.

      Tracked IOC inventory at last regeneration: 132 indicators across
      7 actors (per _master-index.yaml generated 2026-05-20T06:36 EDT
      — 12 CVEs, 22 domains, 13 IPv4, 25 SHA256, 16 malware families,
      etc.). All tracked IOCs implicit in the -24h non-self event
      search; zero hits.

      SANS ISC diary surfaced SHA256
      049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9
      (cross-platform npm stealer) as a fresh-IOC candidate but the
      hash is NOT in _master-index.yaml at sweep time; outside Trigger 3
      scope ("Splunk query returns match on tracked IOC"); flagged
      for /ioc-hunt consideration in handoff section.
  trigger_4_tracked_actor_ttp_change:
    fired: false
    reason: |
      No A/B-grade source documents NEW tooling, targeting, or
      infrastructure class attributable to a tracked actor in the 6h
      late-overnight window beyond what is already inside anti-noise
      locks.

      Mandiant feedburner: 404 pattern persists (now ~21+ consecutive
      sweeps; held healthy pending operator alt-endpoint decision).
      Unit 42: feed reachable, last_modified well pre-window, 0
      in-window items. MSTIC: feed reachable, last_modified well
      pre-window, 0 in-window items. CrowdStrike: 10 feed items but
      null-timestamped, all product/marketing/retrospective (same
      disposition as 00:00 sentinel). SentinelLabs: 0 in-window.
      Cisco Talos: feeds/posts/default endpoint 404 (different URL
      than main blog); flagged for next-sweep recovery probe.
      ESET WeLiveSecurity: 0 in-window per since filter (Webworm
      research from 2026-05-20 is pre-window, already absorbed).
      Sophos Threat Research: 0 in-window. GitHub Blog Security:
      0 in-window.

      Webworm/EchoCreep/GraphWorm Discord+OneDrive C2 TTPs (Dark
      Reading carry-over) are NEW TTPs but attributable to a
      NON-ROSTER actor (Webworm/Space Pirates/UAT-8302); FAILS
      Trigger 4 on tracked-actor prong; DEDUP per 2026-05-20 12:00
      FLASH absorption.

      Eagle Werewolf cluster (Security Affairs/Hunt.io carry-over)
      attributable to NON-ROSTER actor; FAILS Trigger 4 on tracked-
      actor prong.

      SANS ISC cross-platform npm stealer (SHA256
      049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9)
      is npm-ecosystem-adjacent (concept-overlap with TeamPCP/Mini
      Shai-Hulud) but NO actor attribution; FAILS Trigger 4 on
      attributable-tracked-actor prong.

      The TeamPCP/TanStack/Nx Console campaign-chain morning-brief
      coverage (finding-2026-05-21-0007 MSTIC + Unit 42 novel-TTPs
      cluster) anti-noise lock remains active through 2026-05-22T08:00
      EDT covering Bun runtime + /proc scanning + Runner.Worker memory
      scraping + 1Password CLI 2FA bypass + K8s SA tokens + AWS Secrets
      / HashiCorp Vault enumeration + npm OIDC abuse + SLSA forgery +
      PBKDF2 obfuscation. No new TTP class surfaced this window.

      Grafana victim-naming via TanStack chain (SecurityWeek) is a
      NEW victim discovery but NOT a NEW TTP class — same campaign-
      chain mechanism, additional victim. Outside Trigger 4 scope
      (which requires new TTP, not just new victim within known TTP).

      No tracked-actor TTP change observed in window.
  trigger_5_ad_sector_campaign:
    fired: false
    reason: |
      No in-window item describes an active multi-victim campaign
      explicitly targeting A&D primes (Lockheed Martin, Boeing, RTX,
      Northrop Grumman, General Dynamics, BAE Systems, L3Harris, Leidos,
      SAIC, Thales, GE Aerospace, Safran, Honeywell Aerospace, Airbus,
      Elbit Systems) or other watchlist entities.

      Webworm EU government campaign (Dark Reading carry-over) targets
      Belgium / Italy / Poland / Serbia / Spain government organizations
      — not A&D primes; FAILS Trigger 5 on A&D-watchlist prong.

      Eagle Werewolf cluster (Security Affairs/Hunt.io carry-over)
      DYNOWIPER attacks targeted Poland's energy sector — not A&D;
      FAILS Trigger 5 on A&D-watchlist prong.

      Grafana TanStack victim naming (SecurityWeek) — Grafana Labs is
      observability software vendor, not A&D-prime watchlist entity;
      FAILS Trigger 5 on A&D-prime prong.

      KimWolf law enforcement arrest (BleepingComputer / Hacker News)
      is single-actor arrest event, not active multi-victim campaign;
      FAILS Trigger 5 on active-campaign prong.

      First VPN takedown (SecurityWeek carry-over) is law enforcement
      retrospective on a service used by multiple ransomware groups;
      not an active A&D-targeted campaign; off-filter.

      Apex One + Langflow KEV double-add (anti-noise locked) is A&D-
      relevant via DIB Tier-2/3 supplier estate adjacency but is KEV
      procedural inclusion not multi-victim active campaign with A&D-
      prime named victim.

      No A&D-prime named victim across any in-window item.
  trigger_6_zero_day_no_patch:
    fired: false
    reason: |
      No zero-day-no-patch candidates passing Trigger 6 in window.

      CVE-2023-3616 (Mava Hotel Management System) is a 2023 disclosure
      with NVD metadata refresh today; patch status unclear but
      irrelevant — FAILS Trigger 6 on (1) no A-grade source (USOM/
      Siberguvenlik only), (2) no exploitation confirmed or imminent
      (no in-window ITW claim), (3) NOT widely-deployed in A&D context
      (niche hospitality software). DISCARD per Mode 1.

      The Chromium Service Worker persistence issue (no CVE, anti-noise
      lock from 2026-05-21 afternoon brief through 2026-05-22T16:00 EDT)
      remains in monitoring-tier status; no new surface in window.

      SANS ISC cross-platform npm stealer (SHA256
      049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9)
      is a stealer-binary disclosure, not a vulnerability disclosure;
      categorically outside Trigger 6 scope (no CVE, no patch concept,
      no vulnerability framing).

      No zero-day-no-patch candidates in window.
match_reason:
  watchlist: []
  actors:
    - TeamPCP                  # ABSORBED by active 2026-05-21 morning-brief lock through 2026-05-22T08:00 EDT (Grafana victim naming via SecurityWeek TanStack chain surface)
  vulnerabilities:
    - CVE-2023-3616            # evaluated and DISCARDED per Trigger 1 + Trigger 6 failure (no A-grade source, no in-window ITW, 2023 disclosure NVD metadata refresh, niche commercial sector not A&D)
    - CVE-2026-34926           # carry-forward dedup via 2026-05-21 16:00 afternoon brief finding-0008 (lock through 2026-05-22T16:00 EDT) — SecurityWeek + Hacker News in-window media-relay coverage
    - CVE-2025-34291           # carry-forward dedup via same lock — Hacker News in-window media-relay coverage
    - CVE-2026-20223           # carry-forward dedup via 2026-05-20 16:00 afternoon brief finding-2026-05-20-0001 — Hacker News in-window media-relay coverage
  keywords:
    - kimwolf_ddos_botnet_arrest_jacob_butler_canada_aisuru_variant_off_filter
    - cisa_kev_nomination_form_procedural_carry_forward
    - grafana_tanstack_teampcp_supply_chain_first_public_victim_naming_dedup_via_morning_brief_lock
    - webworm_space_pirates_uat_8302_echocreep_graphworm_eu_govts_carry_forward_dedup
    - eagle_werewolf_cluster_huntio_me_c2_mapping_off_filter_non_roster
    - cisco_secure_workload_cve_2026_20223_hacker_news_relay_dedup
    - apex_one_cve_2026_34926_langflow_cve_2025_34291_double_relay_dedup
    - mava_hotel_management_cve_2023_3616_nvd_metadata_refresh_niche_commercial_off_filter
    - sans_isc_cross_platform_npm_stealer_sha256_049300aa_no_attribution_handoff_ioc_hunt
    - first_vpn_takedown_carry_forward_dedup_law_enforcement
    - mandiant_feedburner_404_persists_21_consecutive
    - cisco_talos_feeds_posts_default_endpoint_404_alt_path_needed
    - msrc_cvrf_metadata_refresh_5_bundles_pre_window_18_min
    - drupal_sa_rss_parse_error_mismatched_tag_webfetch_fallback_used
    - crowdstrike_feed_null_timestamps_product_marketing_unchanged_from_00_sentinel
    - splunk_dormant_55th_consecutive_non_self
triage_tags:
  - flash_sentinel
  - clean_sweep
  - sentinel_log_only
  - late_overnight_window_quiet
  - trigger_1_evaluated_failed_mava_hotel_management_cve_2023_3616_no_a_grade_no_itw_niche_commercial
  - trigger_1_evaluated_failed_apex_one_langflow_kev_relay_dedup
  - trigger_1_evaluated_failed_cisco_secure_workload_hn_relay_dedup
  - trigger_2_evaluated_failed_kimwolf_arrest_non_roster_law_enforcement
  - trigger_2_evaluated_failed_webworm_eu_govts_non_roster_carry_forward
  - trigger_2_evaluated_failed_eagle_werewolf_non_roster_huntio_me
  - trigger_2_evaluated_dedup_grafana_teampcp_tanstack_chain_within_morning_brief_lock
  - trigger_6_evaluated_failed_mava_hotel_management_no_a_grade_niche_commercial
  - anti_noise_carry_forward_cisa_kev_double_add_apex_one_langflow_through_20260522t1600
  - anti_noise_carry_forward_kev_7_batch_through_morning_update_block
  - anti_noise_carry_forward_teampcp_tanstack_nx_console_through_20260522t0800_grafana_victim_naming_handoff
  - anti_noise_carry_forward_cisco_secure_workload_20260520_brief_lock
  - anti_noise_carry_forward_drupal_cve_2026_9082_through_20260522t0800
  - anti_noise_carry_forward_chromium_service_worker_through_20260522t1600
  - splunk_first_party_zero_hits_55th_consecutive_dormant_sweep
  - quiet_hours_active_post_2100_pre_0900_critical_override_does_not_apply
  - mandiant_feedburner_404_persists_21_consecutive_held_healthy_pending_operator_decision
  - cisco_talos_feeds_posts_default_endpoint_404_flagged_alt_path_needed_recovery_probe
  - drupal_sa_rss_parse_error_mismatched_tag_webfetch_fallback_succeeded
  - ioc_handoff_sans_isc_sha256_049300aa_cross_platform_npm_stealer_for_ioc_hunt_consideration
  - actor_profiler_handoff_eagle_werewolf_huntio_me_c2_non_roster_new_actor_candidate
  - actor_profiler_handoff_webworm_space_pirates_uat_8302_non_roster_new_actor_candidate_repeat
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-20T06:05:00-04:00
---

# FLASH alert sweep sentinel — 2026-05-22 06:00 EDT cycle (clean, 0 of 6 triggers fired)

Per FLASH-POLICY.md, the 06:00 EDT scheduled late-overnight sweep fired
clean against all six trigger conditions across a representative A-grade
source set (CISA KEV catalog + CISA advisories all.xml + MSRC CVRF + NVD
critical window + Drupal SA + MSTIC + Unit 42 + Mandiant + Cisco Talos +
SentinelLabs + WeLiveSecurity + Sophos Threat Research + CrowdStrike +
GitHub Blog Security + BleepingComputer + The Hacker News + SecurityWeek +
The Record + SANS ISC + Krebs + Dark Reading + Security Affairs + Splunk
first-party).

Sweep window: 2026-05-22T00:00 → 2026-05-22T06:00 EDT.

## Why no FLASH ships

See `trigger_evaluation` block in frontmatter. Multiple in-window items
evaluated and rejected via two paths:

1. **Categorical Mode 1 fails** on non-roster actors, off-filter content,
   law-enforcement events, niche commercial CVEs.
2. **Anti-noise DEDUP** within active locks established in 2026-05-20 /
   2026-05-21 morning + afternoon briefs and prior sentinels.

### Candidate A — CVE-2023-3616 (Mava Hotel Management System SQL Injection, CVSS 9.8)

NVD lastModified refresh in window on a 2023-09-05 original disclosure.
Turkish hospitality software (USOM/Siberguvenlik reference only).
Evaluated against Trigger 1 and Trigger 6 — FAILS both:

1. **No A-grade source.** USOM is a national CSIRT; not in Archimedes
   A-grade tier for FLASH (Mandiant / Unit 42 / MSTIC / CrowdStrike /
   CISA / Cisco Talos / ESET / SentinelLabs).
2. **No in-window in-the-wild exploitation claim.** 2.5-year-old
   disclosure with NVD metadata refresh, no new ITW campaign.
3. **Not widely-deployed in A&D context.** Niche hospitality software;
   A&D primes do not run hotel-management estate.

Categorical Trigger 1 and Trigger 6 failure. DISCARD per Mode 1.

### Candidate B — Grafana naming as TanStack/TeamPCP supply-chain victim (SecurityWeek)

Grafana Labs public disclosure 2026-05-22 03:49 EDT: one unrotated
GitHub workflow token compromised on 2026-05-11 during TanStack/TeamPCP/
Mini Shai-Hulud supply chain attack enabled attackers to access GitHub
repositories; ransom demand received 2026-05-16 and refused; public
disclosure 2026-05-22.

This IS a NEW victim publicly named (first public Grafana naming as
TanStack-chain victim). TeamPCP IS in `_roster.yaml` (#001).

However, **ABSORBED by ACTIVE anti-noise locks**:

(a) 2026-05-21 morning brief findings 0002 + 0007 — TeamPCP / TanStack /
Nx Console campaign chain lock active through 2026-05-22T08:00 EDT
covering all attribution + TTP surfaces on the campaign.

(b) 2026-05-20 12:00 FLASH raw-2026-05-20-flash-1200-002 — already
covered "Grafana/TanStack token rotation continuation" surface at the
time it was first detected.

DEDUP per FLASH anti-noise rule 1 ("one FLASH per trigger topic per
24h"). Grafana-specific victim naming is a useful UPDATE-block handoff
to 2026-05-22 morning brief composer (08:00 EDT) — but the campaign
chain itself is already covered by the active morning-brief lock, and a
fresh FLASH on "TeamPCP/TanStack adds Grafana victim" within the same
active lock window (lock ends T-2h from this sentinel) would constitute
noise.

### Candidate C — Dark Reading "China's Webworm Uses Discord, MS Graphs to Hack EU Govts"

Continuing coverage of ESET research on Webworm / Space Pirates / UAT-
8302 EchoCreep and GraphWorm backdoors. Webworm / Space Pirates NOT in
`_roster.yaml`; previously deferred to actor-profiler /new-actor
consideration in 2026-05-20 12:00 FLASH. ABSORBED by raw-2026-05-20-
flash-1200-001 + 2026-05-20 afternoon brief coverage. DEDUP.

### Candidate D — Hacker News + SecurityWeek CISA KEV double-add media-relay

Both Hacker News "CISA Adds Exploited Langflow and Trend Micro Apex
One Vulnerabilities to KEV" (01:47 EDT) and SecurityWeek "TrendAI
Patches Apex One Zero-Day Exploited in the Wild" (04:19 EDT) cover the
2026-05-21 CISA KEV additions of CVE-2026-34926 (Apex One) and CVE-
2025-34291 (Langflow). Both ABSORBED by 2026-05-21 16:00 afternoon
brief finding-0008 (anti-noise lock active through 2026-05-22T16:00
EDT). DEDUP.

### Candidate E — Hacker News "Cisco Patches CVSS 10.0 Secure Workload REST API Flaw"

Media-relay on CVE-2026-20223 (CVSS 10.0) ABSORBED by 2026-05-20 16:00
afternoon brief finding-2026-05-20-0001 + 2026-05-20 PM raw-signal
raw-2026-05-20-pm-002. Nominal anti-noise lock from 2026-05-20 expired
2026-05-21T16:00 EDT but topic remains carry-forward DEDUP via brief
absorption — no new exploitation-status change, no new patch revision,
no actor attribution since brief publication. DEDUP per FLASH anti-
noise rule 1.

### Items DISCARDED per Mode 1 (categorically off-filter)

- **BleepingComputer + Hacker News parallel KimWolf arrest coverage** —
  Canadian law enforcement arrest of Jacob Butler / Dort over KimWolf
  DDoS botnet (~2M devices, AISURU variant). KimWolf NOT in
  `_roster.yaml`. Law enforcement event; no new attribution; no CVE;
  no A&D-named target.

- **Security Affairs "One Telecom Provider Hosted Most of ME C2"**
  (Pierluigi Paganini 03:29 EDT) — Hunt.io infrastructure report; STC
  72.4% of regional C2; Eagle Werewolf cluster + DYNOWIPER targeting
  Poland energy sector + commodity tooling. Eagle Werewolf NOT in
  `_roster.yaml`; no A&D-prime named victim. Potential actor-profiler
  /new-actor candidate for Eagle Werewolf as separate workflow, not
  FLASH.

- **The Record "CISA to allow researchers to report vulnerabilities"**
  (Suzanne Smalley) — same procedural CISA KEV nomination form story
  from 00:00 sentinel + 2026-05-21 12:00 sentinel. Off-filter.

- **SecurityWeek "First VPN Cybercrime Service Disrupted"** (Eduard
  Kovacs 05:24 EDT) — FBI takedown of First VPN service used by
  ransomware groups. Same story carried by 2026-05-21 12:00 sentinel
  + 18:00 sentinel discard pile (Security Affairs surface 2026-05-21
  13:57 EDT). Not roster actor; no CVE; categorical Trigger 5 failure
  (law enforcement retrospective, not active campaign).

- **SANS ISC "Cross-Platform NPM Stealer"** (Xavier Mertens diary;
  SHA256 049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46
  ddeb9) — static analysis of obfuscated Node.js stealer with browser-
  credential / Chrome-extension wallet / npm capabilities. No actor
  attribution; no CVE; no campaign claim. B-grade SANS diary. Fresh
  IOC handoff candidate to /ioc-hunt if operator wants master-index
  overlap check with Mini Shai-Hulud hashes (none expected; this
  appears to be unrelated commodity stealer based on capabilities,
  not Shai-Hulud worm class).

- **Dark Reading event listings** (Infosecurity Europe 2026-06-02 +
  Anatomy of a Data Breach 2026-06-18) — administrative future-event
  registration entries; off-filter.

- **CrowdStrike feed 10 null-timestamped items** — identical set to
  00:00 + 18:00 sentinels (Claude integration, Identity/Infostealers,
  Financial Services Threat Landscape Report, Falcon AIDR Kubernetes
  AI Apps, May 2026 Patch Tuesday retrospective, Automated Leads,
  Gartner MQ CTI, Falcon OverWatch for Defender, Technical Risk
  Assessments, AI-Powered Vulnerability Discovery). All product /
  marketing / monthly retrospective; no in-window NEW threat-research.

- **MSRC CVRF index 5 most-recent entries** (CurrentReleaseDate
  2026-05-22T01:42-01:48 UTC = 21:42-21:48 EDT 2026-05-21, PRE-window
  by 12-18 min) — all metadata refreshes of older bundles (2026-May,
  2026-Mar, 2025-Sep, 2025-May, 2025-Feb); NOT new out-of-band
  releases. Monthly CVRF index refresh pattern.

## Anti-noise lock collisions and current lock state (carry-forward from 00:00 sentinel)

Six anti-noise locks active at sweep time, all carry-forward from prior
cadence:

1. **CISA KEV double-add 2026-05-21 (Apex One CVE-2026-34926 + Langflow
   CVE-2025-34291)** — 2026-05-21 16:00 afternoon brief finding-2026-05-
   21-0008. Lock active through 2026-05-22T16:00 EDT.

2. **KEV-7 batch 2026-05-20 (Microsoft Defender pair + 5 legacy
   Microsoft/Adobe)** — 2026-05-21 morning brief UPDATE block on
   finding-2026-05-20-0005. Lock active through 2026-05-22T08:00 EDT
   (UPDATE-block resurface-budget consumption).

3. **Cisco Secure Workload CVE-2026-20223** — 2026-05-20 afternoon brief
   finding-2026-05-20-0001. Nominal lock expired 2026-05-21T16:00 EDT;
   continued carry-forward DEDUP via brief absorption — Hacker News
   in-window relay this sweep covered by same brief.

4. **TeamPCP / TanStack / Nx Console campaign chain** — 2026-05-21
   morning brief finding-2026-05-21-0002 + finding-2026-05-21-0007.
   Lock active through 2026-05-22T08:00 EDT. Grafana victim naming
   (SecurityWeek) in-window surface DEDUP within this lock; handoff to
   morning brief composer.

5. **Drupal CVE-2026-9082 SA-CORE-2026-004** — 2026-05-21 morning brief
   finding-2026-05-21-0004. Lock active through 2026-05-22T08:00 EDT.
   No new surfaces in window.

6. **Chromium Service Worker persistence (no CVE)** — 2026-05-21 16:00
   afternoon brief monitoring-tier surface. Lock active through 2026-05-
   22T16:00 EDT with explicit tripwire on CVE assignment in 7-14d.

## Splunk first-party silence

55th consecutive dormant non-self sweep. archimedes + defenseclaw_local
indexes returned 0 events for the -24h window (excluding archimedes:*
self-telemetry). Hard Rule 8 framing: this is neither confirming nor
disconfirming.

## Quiet hours posture

Current time 06:05 EDT is OUTSIDE active hours (FLASH-POLICY active hours
09:00-21:00 EDT). If a trigger had fired at this sweep, FLASH would have
been QUEUED to `infrastructure/flash-queue.yaml` for catchup processing
at the 09:00 sweep — not posted live. Zero triggers fired → sentinel-log-
only path; no queue entry; no Discord post.

The critical-override path (CVSS 10.0 + active exploitation + tracked
actor + A&D watchlist entity) does NOT apply this sweep — the only
in-window CVSS ≥ 9.0 candidates are:

- CVE-2023-3616 (Mava Hotel Management CVSS 9.8): no active exploitation,
  no tracked actor, no A&D watchlist entity. FAIL conditions 2 + 3 + 4.
- CVE-2026-20223 (Cisco Secure Workload CVSS 10.0 via Hacker News relay):
  no active exploitation claim in window (vendor disclosure with no ITW
  attribution to date), no tracked actor named, no A&D watchlist entity
  named as victim. FAIL conditions 2 + 3 + 4. The CVSS 10.0 floor passes
  but the other three prongs fail.

## Source health observations

- **mandiant feedburner**: 404 pattern persists (now ~21+ consecutive
  sweeps); still held healthy pending operator alt-endpoint decision per
  source-health.yaml notes. Not re-attempted this sweep per pattern
  entrenchment.
- **cisco-talos**: `blog.talosintelligence.com/feeds/posts/default`
  endpoint returned 404 via fetch_feed (likely wrong RSS path). The
  blog.talosintelligence.com root previously surfaced via fetch_feed
  in 2026-05-21 18:00 sentinel. Different feed-discovery path needed
  for next sweep recovery probe; flagged but not silencing source-health
  yet — A-grade source surface that should not be lost. Operator may
  want to verify alt endpoint URL.
- **drupal-sa**: `drupal.org/security/all.rss` fetch_feed returned XML
  parse error ("mismatched tag" at line 26 col 289). WebFetch fallback
  on drupal.org/security succeeded with current advisory listing (most
  recent SA-CORE-2026-004 pre-window). RSS parser quirk; fallback worked
  this sweep. Consider source-health monitoring entry if pattern
  continues.
- **volexity blog feed**: NOT queried this sweep; from 00:00 sentinel
  observation it was parse-error for second consecutive sweep but the
  06:00 sweep skipped Volexity given source set was reduced for FLASH-
  speed; defer recovery probe to 2026-05-22 morning pre-brief sweep.
- **mstic, unit42, sentinel-one-labs, welivesecurity,
  sophos-threat-research, github-blog-security, crowdstrike**: all
  reachable; 0 in-window items (or in CrowdStrike's case, 10 items all
  null-timestamped product/marketing/retrospective — same disposition
  as 00:00 sentinel).
- **bleepingcomputer, thehackernews, securityweek, therecord, sans-isc,
  krebs, dark-reading, securityaffairs**: all reachable; in-window
  items DEDUP'd, off-filter, or categorical-Mode-1-fail per evaluation
  above.
- **cisa-kev**: WebFetch JSON 200, 0 new entries in 6h window (catalog
  still at version 2026.05.21 with the 2 yesterday Apex One + Langflow
  entries).
- **cisa-advisories**: all.xml fetch_feed 200, 0 in 6h window.
- **msrc-cvrf**: 0 out-of-band releases in window; 5 most-recent
  entries all metadata-refresh PRE-window by 12-18 min.
- **nvd critical window**: 1 in-window CVSS 9.8 candidate (Mava Hotel
  Management CVE-2023-3616 2023 disclosure with metadata refresh),
  evaluated and DISCARDED per Mode 1.
- **splunk first-party**: returned 0 non-self events in -24h window.

Operator-set `notes:` blocks on each source-health.yaml entry are
preserved verbatim per collector subagent definition. No runtime field
changes to source-health.yaml required this sweep.

## Handoff items for 2026-05-22 morning brief (08:00 EDT) composer

The briefer for 2026-05-22 morning brief should consider these as
candidates for UPDATE blocks or fresh-finding tracking — not FLASH-tier:

1. **Grafana TanStack/TeamPCP victim disclosure (SecurityWeek)** —
   FIRST public Grafana naming as TanStack-chain victim. UPDATE-BLOCK
   CANDIDATE on finding-2026-05-21-0002 + finding-2026-05-21-0007
   (TeamPCP/TanStack/Nx Console chain). Timeline detail: 2026-05-11
   token compromise; 2026-05-16 ransom demand received and refused;
   2026-05-22 public disclosure. Token-rotation-failure root cause
   matches BleepingComputer 2026-05-20 surface. Briefer should evaluate
   whether to UPDATE finding-0002 or scaffold a fresh finding given
   the victim-naming material is novel even though the campaign chain
   is locked.

2. **Webworm / Space Pirates EU government campaign Dark Reading
   carry-over** — Dark Reading continuing-coverage on 2026-05-20 ESET
   research (Webworm/UAT-8302 EchoCreep + GraphWorm backdoors targeting
   Belgium/Italy/Poland/Serbia/Spain govts). NOT in _roster.yaml;
   actor-profiler /new-actor candidate. Briefer may include as
   monitoring-tier or omit (already absorbed in 2026-05-20 afternoon
   brief).

3. **Eagle Werewolf Middle East C2 infrastructure mapping (Hunt.io
   via Security Affairs)** — Hunt.io report mapping 1,350+ C2 servers
   across 14 ME countries; STC 72.4% concentration; references Eagle
   Werewolf cluster + DYNOWIPER Poland energy targeting. NEW
   non-roster-actor cluster + infrastructure-level intelligence;
   actor-profiler /new-actor candidate for Eagle Werewolf. Briefer
   may include as infrastructure-tier observation or defer.

4. **SANS ISC cross-platform npm stealer SHA256 049300aa...** —
   fresh-IOC handoff candidate for /ioc-hunt master-index overlap
   check against Mini Shai-Hulud hashes; likely unrelated commodity
   stealer based on capabilities (browser-credential + Chrome-extension
   wallet + npm) but worth verifying.

5. **KimWolf DDoS botnet arrest (BleepingComputer + Hacker News)** —
   Canadian arrest of Jacob Butler / Dort; KimWolf assessed as AISURU
   variant. Law enforcement news; not roster actor. Briefer may
   include in standing-section blurb on cybercrime enforcement actions
   or omit.

6. **First VPN takedown (SecurityWeek + carry-over)** — FBI takedown
   of cybercrime VPN service used by ransomware operators. Law
   enforcement retrospective; not roster actor. Same disposition as
   KimWolf — briefer judgment.

7. **CVE-2023-3616 Mava Hotel Management NVD metadata refresh** —
   off-filter for A&D context; mention only if briefer is tracking
   NVD-refresh patterns for completeness.

8. **MSRC CVRF metadata refresh pattern (5 bundles, 2026-05-21 21:42-
   21:48 EDT)** — monthly CVRF index refresh, not new disclosures.
   Operator observation only; not brief material.

9. **Carry-forward from 00:00 sentinel handoff still standing**:
   CISA KEV nomination form (The Record + Cybersecurity Dive
   procedural); BookingPress Pro CVE-2026-6960 (already evaluated
   and discarded); Talos BadIIS MaaS (3-day stale); Google API Keys
   23-min post-deletion; Chromium Service Worker tripwire.

## Anti-noise distinction from recent FLASHes / briefs / sentinels

- **flash-sweep-20260522-000000 (00:00 sentinel, 0 triggers)** — covered
  18:00-00:00 EDT window; 1 candidate (BookingPress Pro CVE-2026-6960)
  evaluated and DISCARDED.
- **flash-sweep-20260521-180000 (18:00 sentinel, 0 triggers)** — covered
  12:00-18:00 EDT window; 4 candidates evaluated and all DEDUP'd or
  off-filter (CISA KEV double-add, Security Affairs KEV-7 catch-up,
  Chromium Service Worker, Google API Keys).
- **flash-sweep-20260521-120000 (12:00 sentinel, 0 triggers)** — covered
  06:00-12:00 EDT window; KEV-7 batch + Cisco Workload + Drupal + TeamPCP
  /TanStack/Nx Console anti-noise locks documented.
- **flash-sweep-20260521-060000 (06:00 sentinel, 0 triggers)** — covered
  the 00:00-06:00 EDT window.
- **flash-sweep-20260521-000000 (00:00 sentinel, 0 triggers)** — covered
  the prior overnight window (2026-05-20 18:00 → 2026-05-21 00:00 EDT).
- **2026-05-21 morning brief (08:00 EDT)** — TeamPCP/TanStack/Nx Console
  campaign chain (findings 0002 + 0007), Drupal CVE-2026-9082 (0004),
  Microsoft Defender pair UPDATE (0001), SonicWall CVE-2024-12802
  ReliaQuest single-source ITW claim (0006), Unbound CVE-2026-42960 +
  CVE-2026-33278 dual criticals (0005), NVIDIA TRT-LLM deserialization
  cluster (0003). All locks active through 2026-05-22T08:00 EDT.
- **2026-05-21 afternoon brief (16:00 EDT)** — CISA KEV double-add Apex
  One + Langflow (finding-2026-05-21-0008), NASA F Prime CVE-2026-41144
  (0009), ISC BIND 9 CVE-2026-3593 (0010), ABB ICS batch (0011-0012),
  Rapid7 Q1 2026 Threat Landscape (0013), Chromium Service Worker
  monitoring-tier surface. All locks active through 2026-05-22T16:00 EDT.

This 2026-05-22 06:00 sweep is the 6th consecutive scheduled FLASH
sentinel that fired clean (0 triggers) — late-overnight window in a
quiet 2-day cadence cycle following the Wed/Thu KEV/ICS/TeamPCP-cluster
high-volume coverage.

## Extraction notes

- Language: en
- Article type: sentinel
- Raw IOC extraction invoked: no (sentinel — no payload content to extract; all in-window candidate items either categorically off-filter per Mode 1, anti-noise DEDUP'd within active locks, or non-roster-actor handoffs to morning-brief composer / actor-profiler / /ioc-hunt; no new IOCs surfaced for FLASH-tier promotion)
- Run mode: flash_sweep (Mode 2)
- Output mode: sentinel log only (0 of 6 triggers fired)
- Anti-noise lock collisions: 6 active locks (CISA KEV double-add Apex One + Langflow through 2026-05-22T16:00 EDT; KEV-7 batch through 2026-05-22T08:00 EDT via morning UPDATE; Cisco Workload nominally expired but DEDUP via brief absorption persists; TeamPCP/TanStack/Nx Console chain through 2026-05-22T08:00 EDT with Grafana victim naming in-window handoff; Drupal CVE-2026-9082 through 2026-05-22T08:00 EDT; Chromium Service Worker monitoring-tier through 2026-05-22T16:00 EDT)
- Quiet hours: OUTSIDE active window (06:05 EDT post-2100 / pre-0900); any FLASH would have been QUEUED, not posted live; critical-override path not triggered for CVE-2026-20223 (CVSS 10.0 prong passes, but ITW + tracked-actor + A&D-watchlist prongs all fail)
- Notable non-FLASH actor-profiler handoffs carried forward: Calypso/Red Lamassu (China-nexus telecoms APT from 2026-05-21 12:00 sentinel); Webworm/Space Pirates/UAT-8302 (now multi-sentinel surface); Eagle Werewolf cluster (new this sweep via Hunt.io ME report)
- Fresh IOC handoff to /ioc-hunt: SHA256 049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9 (SANS ISC cross-platform npm stealer; static analysis only; no actor attribution; potential master-index overlap check candidate)
- Source-health observations not yet formalized: mandiant feedburner 21st consecutive 404 (held healthy); cisco-talos /feeds/posts/default 404 (alt path needed); drupal-sa RSS parse error (WebFetch fallback succeeded)
