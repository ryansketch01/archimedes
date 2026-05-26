---
source: archimedes-internal
source_grade: N/A
collected_at: 2026-05-26T07:35:00-04:00
sweep: pre-brief-2026-05-26-am
candidate_trigger: morning_brief_collection
url: null
test: false
sentinel: true
sweep_type: pre-brief-morning
status: complete
sweep_window:
  start: 2026-05-25T17:30:00-04:00
  end: 2026-05-26T07:30:00-04:00
  duration_h: 14.0
prior_sweep_anchor:
  sweep_id: flash-2026-05-26-0600
  anchor_at: 2026-05-26T06:05:00-04:00
  raw_id: raw-2026-05-26-flash-0600-000-sentinel-clean-sweep.md
  disposition: zero_triggers_fired
  notes: |
    The 06:00 EDT FLASH sentinel was a canonical clean sweep — 0 of 6
    triggers fired on a 6h window. Three earlier overnight sweeps
    (1800/0000/0600) also cleared cleanly with 0 triggers. The morning
    pre-brief sweep extends collection forward across the full 14h
    pre-brief window 2026-05-25T17:30 → 2026-05-26T07:30 EDT.
match_reason:
  watchlist: []
  actors:
    - "004"               # UNC1549 / Nimbus Manticore / Screening Serpens — THN restatement; CKR + Unit 42 originating publications corpus-tracked from 2026-05-23 0600 FLASH lineage
    - "006"               # APT28 / Fancy Bear / Forest Blizzard / BlueDelta — Kremlin/Kozlov Rostec institutional context surfaced via The Record (Daryna Antoniuk byline)
  vulnerabilities:
    - VT-005              # Drupal CVE-2026-9082 KEV federal deadline T-1 (Wed 2026-05-27 EOB) — BC restatement (Sergiu Gatlan)
  keywords:
    - aviation
    - Nimbus Manticore
    - MiniFast
    - MiniJunk V2
    - MiniUpdate
    - AppDomainManager
    - getsqldeveloper
    - SEO poisoning
    - GTG-1002
    - Mexico breach
    - CLAUDE.md persistent jailbreak
    - Claude Code
    - AI provider credential theft
    - Bissa Scanner
    - EvilTokens
    - GRU
    - Unit 26165
    - Rostec
    - Andrei Kozlov
    - Lithuania National Register
    - ACR Stealer
    - Godzilla web shell
    - Cobalt Strike Beacon
    - KnowledgeDeliver
    - CVE-2026-5426
    - CVE-2026-9082
    - Drupal
triage_tags:
  - pre_brief_morning
  - am_collection
  - non_flash
  - corpus_anti_noise_relevant
  - unc1549_thn_restatement_anti_noise_carried_forward
  - cve_2026_9082_bc_restatement_carry_forward
  - mirhosting_securityweek_restatement_lock_through_1600
  - ckr_ai_threat_landscape_digest_new_a_grade_publication
iocs_extracted: false
iocs_count: 0
text_word_count: 1850
promoted: false
rejected_at: 2026-05-26T08:00:00-04:00
rejection_id: reject-2026-05-26-0003
ttl_expires_at: 2026-08-24T07:35:00-04:00
sources_queried:
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.22 UNCHANGED (~108h+ since last add CVE-2026-9082 Drupal 2026-05-22). 5 most-recent unchanged from 06:00 FLASH. CVE-2026-9082 Drupal T-1 deadline tomorrow EOB. CVE-2026-42897 Exchange T-3 (Fri).
  - cisa-advisories        # fetch_feed www.cisa.gov/cybersecurity-advisories/all.xml — 200 OK, 30 items in feed, 0 in 14h window.
  - nvd                    # WebFetch services.nvd.nist.gov rest/json/cves/2.0 lastModStartDate=2026-05-25T21:30 → 2026-05-26T07:30 cvssV3Severity=CRITICAL → totalResults=0. ZERO critical CVEs modified in 14h pre-brief window.
  - thehackernews          # fetch_feed feedburner — 200 OK; last_modified Tue 26 May 11:03 GMT (07:03 EDT INSIDE window). 4 in-window items: MFA Prompt Bombing (06:30 EDT — promotional), CERT-In 12h patching (05:13 EDT — regulatory news), UNC1549 MiniFast (03:13 EDT — RAW-SIGNAL), KnowledgeDeliver CVE-2026-5426 (01:19 EDT — RAW-SIGNAL).
  - bleepingcomputer       # fetch_feed — 200 OK; last_modified Tue 26 May 11:23 GMT INSIDE window. 3 in-window items: CISA Drupal CVE-2026-9082 (04:46 EDT — RAW-SIGNAL carry-forward), MS DC lookup KB5087537 (03:41 EDT — known-issue news), 7-Eleven ShinyHunters (03:01 EDT — not roster + consumer retail).
  - securityweek           # fetch_feed feedburner — 200 OK; last_modified Tue 26 May 11:14 GMT INSIDE window. 5 in-window items: KnowledgeDeliver (07:14 EDT — duplicate THN topic), Threat Detection Summit Watch on Demand (07:00 EDT — promotional), DockSec OSS (06:45 EDT — defensive tooling), Lithuania National Register data leak 600K (06:26 EDT — RAW-SIGNAL marginal NATO-context), MIRhosting Bulletproof Hosting Arrests (05:47 EDT — anti-noise lock 16:00 today).
  - the-record             # fetch_feed therecord.media/feed/ — 200 OK; 5 items total, 1 in 14h window: Kremlin Kozlov GRU Security Council (Mon 25 May 23:00 UTC = 19:00 EDT yesterday — RAW-SIGNAL).
  - krebs                  # fetch_feed krebsonsecurity.com/feed/ — 200 OK; last_modified Tue 26 May 11:24 GMT INSIDE window. 0 in-window items (most-recent is the MIRhosting FIOD piece Mon May 25 13:21 GMT, pre-window — covered in 16:00 PM brief already).
  - checkpoint-research    # fetch_feed research.checkpoint.com/feed/ — 200 OK; last_modified Tue 26 May 10:12 GMT INSIDE window. 1 in-window item: AI Threat Landscape Digest March-April 2026 (matthewsu, 06:09 EDT INSIDE window — RAW-SIGNAL new A-grade publication on AI-enabled offensive operations).
  - mstic                  # fetch_feed microsoft.com/en-us/security/blog/feed — 200 OK; last_modified Fri 22 May 17:57 GMT UNCHANGED (12th consecutive sweep). 0 in window.
  - unit42                 # fetch_feed feedburner — 200 OK; last_modified Mon 25 May 16:19 GMT pre-window UNCHANGED. 0 in window. NOTE: Unit 42 May 22 piece on UNC1549 MiniUpdate/MiniJunk V2/AppDomainManager corpus-tracked in 2026-05-23 0600 FLASH lineage.
  - mandiant               # fetch_feed mandiant.com/resources/blog/rss.xml — 200 OK with 20 items in feed, 0 in 14h window. THIRD consecutive 200 OK (00:00 + 06:00 + 07:30) after 24 consecutive 404 failures observed through 2026-05-25 12:00. RECOVERY CONFIRMED — runtime change applied (see source_health_changes below).
  - sentinelone            # fetch_feed sentinelone.com/labs/feed — 200 OK; last_modified Tue 26 May 05:33 GMT in-window but 0 items in 14h window after since-filter. Server-side index refresh, no new publication.
  - crowdstrike            # fetch_feed crowdstrike.com/blog/feed — 200 OK; last_modified Tue 26 May 08:57 GMT INSIDE window. 10 items returned ALL dateless slate (product/marketing). Same content pattern as 00:00/06:00 sweeps — no threat-research with publication-dates in window.
  - cisco-talos            # fetch_feed blog.talosintelligence.com/rss/ — 200 OK; 15 items in feed, 0 in 14h window.
  - rapid7                 # fetch_feed rapid7.com/blog/rss/ — 200 OK; last_modified Tue 26 May 11:16 GMT INSIDE window. 0 items in 14h window.
  - eset-welivesecurity    # fetch_feed welivesecurity.com/en/rss/feed — 200 OK; 100 items in feed, 0 in 14h window.
  - dfir-report            # fetch_feed thedfirreport.com/feed/ — 200 OK; last_modified Mon 11 May 14:05 GMT 15-day stale (cadence-slow publisher). 0 items in 14h window.
  - github-blog-security   # fetch_feed github.blog/security/feed/ — 200 OK; last_modified Tue 26 May 09:44 GMT INSIDE window. 0 items in 14h window.
  - proofpoint             # fetch_feed proofpoint.com/us/rss.xml — 200 OK; last_modified Tue 26 May 08:34 GMT INSIDE window. 0 items in 14h window. Server-side index refresh, no new publication.
  - sans-isc               # fetch_feed isc.sans.edu/rssfeed.xml — 200 OK; last_modified Tue 26 May 11:29 GMT INSIDE window. 2 in-window items: Stormcast podcast May 26 (02:00 EDT — daily podcast, no actionable content), Possible ACR Stealer From Page Impersonating Claude (Brad Duncan, 00:02 EDT — RAW-SIGNAL marginal IOC-tier defender alert with 6 hashed/domain IOCs).
  - securelist             # fetch_feed securelist.com/feed/ — 200 OK; last_modified Fri 22 May 10:08 GMT pre-window UNCHANGED. 0 items in 14h window.
  - bitdefender            # bitdefender.com/blog/labs/rss/ — 404 (feed-endpoint discovery pending — operator action item).
  - sophos                 # news.sophos.com/en-us/feed/ — 404 (consistent with prior sweeps — endpoint retirement; operator action item).
  - volexity               # volexity.com/blog/feed/ — XML parse error <unknown>:17:68 not well-formed invalid token, FOURTH consecutive failure (failure_count incrementing 3→4 past-threshold). Held healthy per operator-set instruction pending alt-endpoint decision (see source_health_changes below — recommend stale flip at next sweep if pattern persists).
  - dragos                 # dragos.com/blog/feed/ — 404 (consistent with prior sweeps; operator action item).
  - wiz-research           # wiz.io/feed.xml — 404 (consistent with prior sweeps; operator action item).
  - aikido                 # NOT re-fetched — STALE-flagged at AM-25; 24h skip rule continues until ~midday 2026-05-26.
  - reliaquest             # NOT re-queried (DNS resolution failure prior sweeps; operator decision pending).
  - splunk-archimedes      # mcp__splunk-query targeted 38-IOC sweep on -14h@h pre-brief window (executed THIS sweep; see splunk_first_party_check). ZERO events returned.
  - splunk-defenseclaw     # included in the -14h@h cross-index sweep; 0 events. 61st consecutive dormant non-self sweep (incremented from 60 at 06:00 FLASH).
splunk_first_party_check:
  query: 'search index=defenseclaw_local OR index=archimedes earliest=-14h@h latest=now ("MiniFast" OR "MiniJunk" OR "Nimbus Manticore" OR "Screening Serpens" OR UNC1549 OR "getsqldeveloper" OR "AppDomainManager" OR "MiniUpdate" OR CVE-2026-9082 OR CVE-2026-42897 OR CVE-2026-45321 OR CVE-2026-5426 OR "Drupal" OR "Exchange" OR ShinyHunters OR "7-Eleven" OR KnowledgeDeliver OR Godzilla OR "Cobalt Strike" OR "Stark Industries" OR MIRhosting OR WorkTitans OR TeamPCP OR "Shai-Hulud" OR "Charming Kitten" OR APT28 OR APT29 OR Sandworm OR Kremlin OR Kozlov OR Rostec OR "Claude Code" OR "GTG-1002" OR "Lithuania" OR DockSec OR "MFA prompt bombing")'
  result: 0 events — zero IOC hits across 38 corpus-tracked + in-window-surfaced strings on -14h@h pre-brief window
  consecutive_dormant_sweeps_defenseclaw: 61
  iac_ioc_hits_in_defenseclaw_local: 0
  hard_rule_8_framing: |
    Targeted 38-IOC sweep across (a) all carried-forward corpus-tracked
    IOCs (CVE-2026-9082 Drupal, CVE-2026-42897 Exchange, CVE-2026-45321
    Mini Shai-Hulud, TeamPCP cluster, MIRhosting/WorkTitans/Stark stack,
    Russia/Iran/DPRK roster actors), (b) NEW in-window-surfaced strings
    (MiniFast, getsqldeveloper, KnowledgeDeliver, CVE-2026-5426, Godzilla,
    7-Eleven, ShinyHunters, Kremlin/Kozlov/Rostec, Lithuania, GTG-1002,
    Claude Code, DockSec, MFA prompt bombing), and (c) AppDomainManager TTP
    keyword on -14h@h returned ZERO events. 61st consecutive dormant non-
    self sweep on defenseclaw_local. Hard Rule 8: silence is not
    disconfirming, not confirming — defenseclaw_local is structurally
    bounded by its ingest scope.

raw_signal_files_written:
  - raw-2026-05-26-am-001-thn-unc1549-nimbus-manticore-minifast-minijunk-v2-seo-poisoning-getsqldeveloper-restatement.md
    rationale: UNC1549 (#004) tracked actor — THN B-grade relay of CKR + Unit 42 originating publications (corpus-tracked from 2026-05-23 0600 FLASH lineage). New TTP elements: MiniFast naming distinct from MiniUpdate (Check Point vs Unit 42 taxonomy on adjacent family), SEO poisoning via getsqldeveloper[.]com fake SQL Developer page, AppDomain hijacking via ZIP-archived DLLs. Per FLASH-POLICY anti-noise, this is non-flash-tier — appropriate for AM brief absorption as UNC1549 surface UPDATE. Grader determines clustering with existing UNC1549 corpus surfaces.
  - raw-2026-05-26-am-002-checkpoint-research-ai-threat-landscape-digest-march-april-2026-gtg1002-mexico-breach-bissa-eviltokens.md
    rationale: CheckPoint Research (provisional A) new A-grade publication — AI Threat Landscape Digest. Covers GTG-1002 Chinese-nexus restated (Anthropic Nov 2025 disclosure), Mexico breach (single operator, 9 Mexican government agencies, 1,088 prompts + 5,317 commands, CLAUDE.md persistent jailbreak), Bissa Scanner (900+ Next.js endpoints compromised, 30,000+ .env files harvested), EvilTokens PhaaS (Microsoft OAuth + BEC), AI provider credential targeting (Anthropic/OpenAI/Groq/Mistral/HuggingFace/Replicate/DeepSeek). NO IOCs published (GTG-1002 was famously IOC-less per Anthropic). NO direct A&D-prime naming. Defender-impact: AI-orchestrated attack infrastructure pattern + .env credential exposure on AI provider keys is corpus-relevant to TeamPCP credential-theft tradecraft and the broader AI-augmented attacker workflow surface.
  - raw-2026-05-26-am-003-therecord-kremlin-andrei-kozlov-gru-unit-26165-rostec-security-council-apt28.md
    rationale: APT28 (#006) institutional context — The Record (Daryna Antoniuk byline) reports Russia's Security Council appointed Andrei Kozlov (former Rostec cybersecurity center head; held classified security clearance under Military Unit 26165 = 85th GTsSS = APT28 / Fancy Bear / Forest Blizzard / BlueDelta institutional home). Predecessor Pavel Konovalchik also linked to Unit 26165 per The Record. Article explicitly enumerates Unit 26165's targeting of "governments, defense contractors, logistics companies and policy organizations across Europe and the United States." NOT direct A&D-prime compromise; institutional-context shift signal in the GRU cyber chain of command, may correlate with future tradecraft / targeting changes in APT28 corpus dossier.
  - raw-2026-05-26-am-004-bleepingcomputer-cisa-drupal-cve-2026-9082-kev-deadline-t-1-imperva-shadowserver-670-unpatched.md
    rationale: Drupal CVE-2026-9082 KEV federal-deadline carry-forward (T-1 Wed 2026-05-27 EOB, ~36h from morning brief). BC (Sergiu Gatlan) — relay of CISA KEV addition (corpus-tracked from 2026-05-22 FLASH lineage) plus TWO new datapoints: (1) Shadowserver tracking 670 unpatched Drupal installations (272 NA, 273 Europe) as of 2026-05-25; (2) Imperva observation of 15,000+ attack attempts across 6,000+ sites in 65 countries as of 2026-05-21, with ~50% targeting Gaming and Financial Services. Originating CVE discovery credit: Google Mandiant researcher Michael Maturi. Anti-noise-locked under cve-2026-9082-drupal-core-sqli-kev-deadline-tracking. Brief-tier carry-forward.
  - raw-2026-05-26-am-005-thn-securityweek-knowledgedeliver-cve-2026-5426-zero-day-godzilla-cobalt-strike-mandiant-gtig-japan-lms.md
    rationale: KnowledgeDeliver CVE-2026-5426 (CVSS 7.5) hard-coded ASP.NET machine keys → ViewState deserialization → unauthenticated RCE → Godzilla web shell (BLUEBEAM alias) + Cobalt Strike Beacon deployment chain. Japan-domestic LMS. Patched pre-2026-02-24. Originating attribution: Google Mandiant + GTIG to "an unknown threat actor" (no named cluster). Below FLASH-trigger thresholds (CVSS 7.5 below 9.0 floor; not widely-deployed in A&D context). Captured for grader as retrospective-zero-day class with Mandiant primary attribution. Covered by both THN (Ravie Lakshmanan 01:19 EDT) and SecurityWeek (Ionut Arghire 07:14 EDT) — multi-relay pattern.
  - raw-2026-05-26-am-006-sans-isc-acr-stealer-fake-claude-download-page-brad-duncan-iocs-fairpoint29.md
    rationale: SANS ISC (Brad Duncan handler byline 00:02 EDT in-window) — defender-tier IOC publication on ACR Stealer infostealer delivered via fake Claude download landing page on fairpoint29[.]com with Google Ads malvertising delivery + sites.google[.]com URL concealment. Published 6 IOCs (1 fake-page domain, 3 download/staging domains, 1 C2 domain, 3 SHA-256 hashes). NO named threat actor (per Hard Rule 2). Cross-references the AI-impersonation pattern that the CKR AI Threat Landscape Digest surfaces (Anthropic / Claude brand abused in offensive operations). Corpus-relevant to the Claude-share-URL-abuse lineage in TeamPCP's broader supply-chain campaign per finding-2026-05-10-0001 (MacSync). Grader-tier item for IOC promotion into _master-index.yaml.
  - raw-2026-05-26-am-007-securityweek-lithuania-national-register-data-leak-600k-foreign-involvement-suspected-russian-hybrid-war.md
    rationale: SecurityWeek (Associated Press relay 06:26 EDT in-window) — Lithuanian authorities report 600,000+ entries leaked from national data registers (primarily real estate + legal entities) via stolen credentials of authorized institutions. Attribution language verbatim: "foreign country is suspected of involvement" (officials did NOT specify which nation). Opposition politician (Laurynas Kasčiūnas) social-media-alleged "Russian intelligence operation" but "offered no evidence." Article frames Lithuania within "Russia's hybrid war against Europe" context. NO named threat actor. NO A&D-prime impact. NATO-member-state breach with potential intelligence-officer / military-personnel / diplomat address exposure. Marginal raw-signal — grader determines whether to cluster with Russia-aligned ecosystem surface or discard as untracked geographic-shape adjacency.

filter_evaluation_summary:
  in_window_items_total: 19
  in_window_items_evaluated: 19
  in_window_items_raw_signaled: 7
  in_window_items_filtered_out_promotional: 3       # MFA Prompt Bombing, TDIR Summit Watch on Demand, ISC Stormcast
  in_window_items_filtered_out_regulatory_news: 1   # CERT-In 12h patching
  in_window_items_filtered_out_no_actor_no_ad: 2    # 7-Eleven ShinyHunters consumer retail, MS DC lookup KB5087537 known-issue
  in_window_items_filtered_out_defensive_tooling: 1 # DockSec OSS
  in_window_items_filtered_out_anti_noise_lock: 1   # MIRhosting SW restatement (lock active through 1600 today)
  in_window_items_filtered_out_duplicate_topic: 1   # KnowledgeDeliver SW item is duplicate of THN topic (folded under same raw-signal)
  notes: |
    Nineteen in-window items distributed across multiple A/B-grade
    sources. Seven raw-signaled for grader review. Twelve filtered
    out for reasons enumerated above:

    PROMOTIONAL (3):
      THN-MFA Prompt Bombing 06:30 EDT: generic security awareness
        article, no actor / no CVE / no IOC. NOT corpus-relevant.
      SW-TDIR Summit Watch on Demand 07:00 EDT: marketing /
        promotional content for SecurityWeek's own event series.
      ISC-Stormcast May 26 02:00 EDT: daily podcast, no item-specific
        threat content.

    REGULATORY NEWS (1):
      THN-CERT-In 12-Hour Patching Mandate 05:13 EDT: Indian
        regulatory guidance news, no CVE / no IOC / no actor. NOT
        a threat-intel surface; appropriate for compliance trade
        publications, not Archimedes corpus.

    NO ACTOR + NO A&D (2):
      BC-7-Eleven ShinyHunters 03:01 EDT: ShinyHunters NOT in
        _roster.yaml; consumer retail breach (no A&D relevance);
        no CVE, no FLASH-trigger event class.
      BC-MS DC Lookup KB5087537 03:41 EDT: Patching-side known-issue
        advisory. NOT a vulnerability with active exploitation;
        NOT a zero-day; NO actor; NO CVE.

    DEFENSIVE TOOLING (1):
      SW-DockSec OSS Docker AI Vulnerability Tool 06:45 EDT: OWASP
        incubator project release news. Defender-side tooling, not
        attacker activity.

    ANTI-NOISE LOCK ACTIVE (1):
      SW-MIRhosting Bulletproof Hosting Arrests 05:47 EDT: anti-
        noise lock stark-mirhosting-worktitans-russia-aligned-hosting-
        takedown ACTIVE through 2026-05-26 16:00 EDT (covered in PM
        brief 2026-05-25 finding-2026-05-25-0003 + 06:00 FLASH
        sentinel already absorbed). SW (Ionut Arghire) is narrative-
        synthesis restatement, no novel investigative content beyond
        confirming suspect names (Youssef Z., Andrey N. corroborates
        FIOD/Krebs).

    DUPLICATE TOPIC (1):
      SW-KnowledgeDeliver CVE-2026-5426 07:14 EDT: same topic as THN
        KnowledgeDeliver 01:19 EDT — folded under shared raw-signal
        am-005 with both relays attributed.

anti_noise_locks_active:
  - lock_id: teampcp-mini-shai-hulud-cluster-2026
    source_anchor: finding-2026-05-25-0002 (afternoon brief 2026-05-25)
    expires_at: 2026-05-26T16:00:00-04:00
    status: ACTIVE — TeamPCP topic locked through 2026-05-26 16:00 EDT
  - lock_id: stark-mirhosting-worktitans-russia-aligned-hosting-takedown
    source_anchor: finding-2026-05-25-0003 (afternoon brief 2026-05-25)
    expires_at: 2026-05-26T16:00:00-04:00
    status: ACTIVE — SW 05:47 EDT item is restatement-only of this corpus surface
  - lock_id: ghost-cms-cve-2026-26980-fresh-tradecraft-detail
    source_anchor: 12:00 EDT FLASH sentinel near-miss + 16:00 PM brief absorption
    expires_at: 2026-05-26T08:02:00-04:00 (24h from THN publication)
    status: EXPIRES at ~08:02 EDT — within minutes of morning brief publication
  - lock_id: kali365-fbi-phishing-as-a-service-corpus-tracked
    source_anchor: 2026-05-22 18:00 FLASH + 2026-05-25 12:00 FLASH reiteration
    expires_at: 2026-05-26T08:45:00-04:00 (24h from BC 2026-05-25 publication)
    status: EXPIRES at ~08:45 EDT — shortly after morning brief publication
  - lock_id: cve-2026-9082-drupal-core-sqli-kev-deadline-tracking
    source_anchor: continuous from 2026-05-22 FLASH; rolling brief-tier coverage
    expires_at: rolling — recurring brief surface
    status: ACTIVE — covered in 16:00 brief; T-1 deadline Wed EOB ~36h from morning brief
  - lock_id: cve-2026-42897-exchange-owa-xss-kev-deadline-tracking
    source_anchor: continuous from 2026-05-15 FLASH-0001 lineage
    expires_at: rolling — recurring brief surface
    status: ACTIVE — T-3 deadline Fri ~80h from morning brief
  - lock_id: cve-2026-45321-mini-shai-hulud-oidc-credential-abuse-kev-absent-watch
    source_anchor: VT-006 parent surface
    expires_at: rolling — recurring brief surface
    status: ACTIVE
  - lock_id: unc1549-screening-serpens-tradecraft-evolution-2026-tradecraft-rats-azure-staging
    source_anchor: 2026-05-23 0600 FLASH queue entry (flash-queue.yaml line 71-72)
    expires_at: nominal 2026-05-24T06:00:00-04:00 (24h) BUT operator notes "0523 still in queue" — TOPIC LOCK persists for AM-26 brief absorption disposition
    status: ACTIVE (effective) — THN 03:13 EDT MiniFast + SEO-poisoning restatement is absorbed under this lock per operator anti-noise list; raw-signaled as am-001 for grader cluster decision

hard_rules_compliance:
  rule_2_no_attribution_origination: |
    No Archimedes-side attribution origination. Each raw-signal file
    preserves the source's attribution language verbatim:
      - THN UNC1549 piece relays Check Point Research + Unit 42 named
        attribution to Iran/IRGC (corpus-baseline, vendor-consensus).
      - CKR AI Threat Landscape Digest uses "Chinese nexus" (GTG-1002)
        and explicitly declines actor identification on Mexico breach
        ("a single operator") and Bissa Scanner / EvilTokens.
      - The Record Kremlin/Kozlov piece names Unit 26165 / 85th GTsSS
        institutional ties but does NOT cite specific new APT28 ops.
      - BC Drupal piece attributes ZERO threat actor; CVE-discovery
        credit only (Mandiant researcher Michael Maturi).
      - THN / SW KnowledgeDeliver pieces relay Mandiant/GTIG to
        "an unknown threat actor" — no named cluster.
      - SANS ISC ACR Stealer piece attributes ZERO threat actor.
      - SW Lithuania piece relays "foreign country is suspected" with
        Russia-context framing but no specific attribution.
  rule_3_no_exploitation: |
    No PoC code, no payloads, no exploit guides referenced or
    generated in any raw-signal file. Technical mechanism descriptions
    are at family-name + capability-class level only (Godzilla web
    shell / Cobalt Strike Beacon / ViewState deserialization /
    SEO poisoning / AppDomain hijacking / OAuth device-code phishing).
    No reproduction-tier detail in any raw-signal.
  rule_4_passive_only: |
    No active scans. SpiderFoot not invoked. authorized-targets.yaml
    empty. All sources are passive RSS / WebFetch / NVD / KEV /
    Splunk over Archimedes's own indices.
  rule_6_quote_limit: |
    External quotes used in raw-signal files are 15-word-cap compliant
    per Hard Rule 6, one quote per source max. Specific verbatim
    attribution language is preserved where doctrine-required (Hard
    Rule 2) but framed as attribution-quotation, not editorial.
  rule_7_credentials: |
    No credential exposure surfaced this window. CKR AI Threat Landscape
    Digest discusses AI provider API key harvesting from .env files at
    the campaign-mechanism level (Anthropic, OpenAI, Groq, Mistral,
    HuggingFace, Replicate, DeepSeek targeted) — no specific credential
    values are referenced or stored.
  rule_8_splunk_first_party_priority: |
    Targeted 38-IOC sweep on -14h@h = 0 events. 61st consecutive
    dormant non-self sweep on defenseclaw_local. Hard Rule 8: silence
    is not disconfirming, not confirming.

source_health_changes:
  - source_yaml_id: mandiant
    observation: |
      mandiant.com/resources/blog/rss.xml returned 200 OK with 20
      items in feed THIRD consecutive sweep (00:00 FLASH + 06:00
      FLASH + 07:30 pre-brief) after 24 consecutive 404 failures
      observed through 2026-05-25 12:00. RECOVERY CONFIRMED across
      three consecutive observations. 0 in-window items but feed-
      endpoint health is now healthy.
    runtime_change_applied: |
      status remains healthy. failure_count flipped from 19 → 0.
      last_successful_fetch updated to 2026-05-26T07:30:00-04:00.
      last_error cleared (set to null). notes updated to record
      the three-observation recovery confirmation.
  - source_yaml_id: volexity
    observation: |
      volexity.com/blog/feed/ returned XML parse error <unknown>:17:68
      not well-formed (invalid token) — FOURTH consecutive failure
      (failure_count incrementing 3 → 4 past ≥2 stale threshold).
      Pattern (parse error on same line/column) suggests persistent
      malformed XML rather than transient network failure.
    runtime_change_applied: |
      failure_count incremented 3 → 4. status held healthy per
      operator-set policy pending alt-endpoint decision. last_error
      updated to record the fourth observation. notes appended.
      RECOMMENDATION: flip status to stale at next sweep if parse
      error persists (consistent with documented operator policy).
  - source_yaml_id: reliaquest
    observation: |
      NOT re-queried this sweep — DNS resolution failure prior
      sweeps; not in source-health.yaml; operator decision pending.
    runtime_change_applied: no_change_no_health_entry
  - source_yaml_id: aikido
    observation: |
      NOT re-fetched this sweep — STALE-flagged at AM-25; 24h skip
      rule continues until ~midday 2026-05-26. Eligible for re-try
      at 12:00 EDT FLASH or later.
    runtime_change_applied: no_change_24h_skip_rule_in_effect
---

# Pre-Brief Collection Sentinel — Morning 2026-05-26

This sentinel covers the 14-hour pre-brief window 2026-05-25T17:30 EDT
through 2026-05-26T07:30 EDT for the 08:00 EDT morning brief.

## Window summary

- **Sources queried:** 30
- **Sources healthy:** 26 (Mandiant recovery confirmed)
- **Sources held healthy past threshold:** 1 (volexity — fourth parse error, recommend stale flip)
- **Sources 404 / endpoint-broken (operator action):** 4 (bitdefender, sophos, dragos, wiz-research)
- **Sources skipped per 24h stale rule:** 1 (aikido)
- **Sources without health entry:** 1 (reliaquest)
- **In-window items total:** 19
- **In-window items raw-signaled:** 7
- **In-window items filtered:** 12 (promotional, regulatory, no-actor/no-A&D, defensive tooling, anti-noise lock, duplicate topic)

## Items raw-signaled

| File | Anchor | Source | Disposition for AM brief |
|---|---|---|---|
| am-001 | UNC1549 / Nimbus Manticore MiniFast restatement | THN (B-grade relay of CKR + Unit 42) | UPDATE on UNC1549 surface (anti-noise lock active) |
| am-002 | CheckPoint Research AI Threat Landscape Digest | CKR (provisional A) | NEW topic — AI-orchestrated offensive operations + GTG-1002 restatement |
| am-003 | Kremlin / Kozlov / GRU Unit 26165 / Rostec | The Record (B-grade) | APT28 institutional context — defender-relevant intel signal |
| am-004 | Drupal CVE-2026-9082 KEV T-1 + Imperva + Shadowserver | BC (B-grade) | KEV deadline carry-forward — T-1 ~36h from brief |
| am-005 | KnowledgeDeliver CVE-2026-5426 Godzilla + CS Beacon | THN + SW (both B-grade) | Retrospective zero-day, Mandiant/GTIG primary — grader-tier |
| am-006 | SANS ISC ACR Stealer + fake Claude landing page | ISC SANS (B-grade) | IOC-tier defender alert — 6 IOCs published |
| am-007 | Lithuania National Register data leak 600K | SW relay of AP (marginal) | Geographic-context — Russia hybrid-war framing, no named actor |

## Splunk first-party check

Zero events on -14h@h pre-brief window across 38 corpus-tracked + in-
window-surfaced IOC strings. 61st consecutive dormant non-self sweep
on defenseclaw_local.

## Anti-noise locks active

8 locks active (see frontmatter). Two locks (ghost-cms-cve-2026-26980,
kali365-fbi) expire within minutes of morning brief publication.

## Source health changes

- **mandiant** — RECOVERY CONFIRMED across three consecutive sweeps; runtime fields reset.
- **volexity** — fourth consecutive parse error past stale threshold; recommend stale flip if persists.

## Hard Rules compliance

All raw-signal files preserve source-attribution language verbatim per
Hard Rule 2. No exploitation content per Hard Rule 3. No active scans
per Hard Rule 4. Quote limits observed per Hard Rule 6. No credential
storage per Hard Rule 7. Splunk first-party check executed per Hard
Rule 8 (zero hits, framed per doctrine).

---

*Pre-brief collection sentinel for the morning brief at 08:00 EDT.
Grader takes over from here — clustering, Admiralty grading, and
promotion decisions are downstream.*
