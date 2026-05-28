---
source: archimedes-internal
source_grade: N/A
collected_at: 2026-05-28T07:34:00-04:00
sweep: pre-brief-2026-05-28-am
url: null
test: false
sentinel: true
sweep_type: pre-brief-collection
status: complete
mode: pre_brief_collection
invocation: scheduled pre-brief AM-28 cycle (07:30 EDT)
sweep_window:
  start: 2026-05-27T17:30:00-04:00
  end: 2026-05-28T07:34:00-04:00
  duration_h: 14.07
prior_sweep_anchor:
  sweep_id: flash-2026-05-28-0600
  anchor_at: 2026-05-28T06:05:00-04:00
  raw_id: raw-2026-05-28-flash-0600-000-sentinel-clean-sweep.md
  commit_sha: bb4b3c9
  disposition: zero_triggers_fired
  notes: |
    06:00 EDT Thursday dawn FLASH sentinel was the NINTH consecutive
    clean sweep across the Tuesday + Wednesday + early Thursday window.
    Carry-forward items the dawn sentinel flagged for AM-28 absorption:
    JINX-0164 (Wiz Research A-grade-provisional, novel actor explicitly
    DISCLAIMING tracked-roster overlap incl. roster #002 BlueNoroff
    alias) and Google AI Threat Defense Platform vendor consolidation
    (Mandiant + Wiz + Gemini). 06:00 EDT also documented mandiant.com/
    resources/blog/rss.xml as the working endpoint while cloud.google.com
    parse-error pattern persists.
prior_brief_anchor:
  brief_id: 2026-05-27-afternoon
  shipped_at: 2026-05-27T16:00:00-04:00
  commit_sha: 23be30c
  notes: |
    PM-27 afternoon brief published with three new findings + two PM
    enrichment amendments — CISA KEV three-add lead (CVE-2026-45321
    VT-006 state-transition to KEV-listed, CVE-2026-48027 Nx Console
    VT-009 scaffold, CVE-2026-8398 Daemon Tools Lite consumer not
    corpus-tracked), Yamcs CVE-2026-44632 A&D-direct spacecraft mission
    control RCE (VT-010 scaffold), Ox Security npm Claude AI user-data
    stealer (mouse5212 / super-formatter, UNATTRIBUTED). PM enrichments
    on GlassWorm (finding-2026-05-27-0001) and LACMTA / Iran (finding-
    2026-05-27-0004). Splunk first-party brief-publish event confirmed
    at 16:34 EDT via msg_id 1509293548162383942.

match_reason:
  watchlist: []
  actors:
    - roster_001_TeamPCP    # Unit 42 Out of the Crypt explicitly maps TGR-CRI-1135 → TeamPCP; supply-chain pattern + Vect RaaS + LAPSUS$ EaaS partnerships + 23k Mythos AI-discovered vulns context
    - roster_007_Sandworm    # Unit 42 World Cup uses Razing Ursa alias (GRU Unit 74455 = Sandworm); 2018 Olympic Destroyer historical precedent reference
    - roster_013_Scattered_Spider    # Unit 42 World Cup uses Muddled Libra alias (ALPHV/BlackCat operator alias for Scattered Spider per Unit 42); Out of the Crypt has Scattered LAPSUS$ Hunters cluster
    - roster_014_Handala_Hack    # Unit 42 World Cup names Handala Hack Team (aliases Banished Kitten, Storm-0842, Void Manticore, Cobalt Mystique) as MOIS front; ties to roster #014 (aliases Void Manticore, Storm-0842)
    - shinyhunters_via_bling_libra_alias    # Unit 42 Out of the Crypt formally aliases ShinyHunters as Bling Libra; Carnival Cruise breach is the 2026-05-28 ShinyHunters confirmation point
  vulnerabilities:
    - CVE-2026-4408    # NEW: Samba samba-dcerpcd OS command injection via check-password-script + %u substitution, CVSS 9.0 (NIST), published 2026-05-28; DIB-relevant given Samba's widespread deployment as Linux file-server / domain-controller in government & defense estates
    - CVE-2026-34000   # NEW: X.Org X server XKB geometry out-of-bounds read, CVSS 9.1 NIST (RH CNA 6.1); X11 server enterprise / gov / DIB
    - CVE-2026-34002   # NEW: X.Org X server XKB modifier-map out-of-bounds read, CVSS 9.1 NIST
    - CVE-2026-32590   # NEW: Red Hat Quay container-layer-upload deserialization → arbitrary code execution, CVSS 8.8 NIST; container registry used by DIB DevOps pipelines
    - VT-005    # OpenC3 COSMOS five-CVE cluster — corpus-tracked spacecraft C2 (precedent for VT-010 Yamcs)
    - VT-006    # Mini Shai-Hulud CVE-2026-45321 — KEV federal deadline T-13d 2026-06-10; Unit 42 Out of the Crypt extortion piece re-cites TeamPCP supply chain
    - VT-008    # Exchange CVE-2026-42897 — KEV federal deadline T-1d Friday 2026-05-29; anti-noise lock continues
    - VT-009    # Nx Console CVE-2026-48027 — KEV federal deadline T-13d 2026-06-10; anti-noise lock continues
    - VT-010    # Yamcs CVE-2026-44632 — A&D-direct spacecraft mission control RCE; PM-27 scaffold, 7-day review cadence
    - CVE-2026-48172    # LiteSpeed cPanel — KEV federal deadline T-1d Friday 2026-05-29
    - CVE-2026-9082    # Drupal Core — KEV federal deadline EXPIRED yesterday Wed EOB; T+5h state-monitoring posture
    - CVE-2026-27771    # Gitea unauth private container image disclosure — anti-noise lock from raw-2026-05-27-am-003; SecurityWeek today 07:24 EDT relay published "30,000 deployments exposed" framing
  keywords:
    - Carnival Cruise
    - ShinyHunters
    - Bling Libra
    - Scattered LAPSUS$ Hunters
    - Salesforce Aura
    - Salesloft Drift
    - Mariner Society
    - Holland America Line
    - 2026 World Cup
    - FIFA
    - Handala Hack Team
    - CyberAv3ngers
    - Shahid Kaveh Group
    - Bauxite
    - Hydro Kitten
    - Storm-0784
    - UNC5691
    - NoName057(16)
    - Razing Ursa
    - Muddled Libra
    - Fiddling Scorpius
    - CISA AA26-097A
    - Rockwell Allen-Bradley PLC
    - TGR-CRI-1135
    - TeamPCP
    - Hazy Scorpius
    - CLOP
    - CL-CRI-1116
    - BlackFile
    - Redact
    - Vect RaaS
    - LAPSUS$ Group
    - ATHR
    - Mythos
    - Anthropic
    - SymJack
    - Samba check-password-script
    - samba-dcerpcd
    - X.Org X server
    - XKB geometry
    - Red Hat Quay
    - Mirror Registry for Red Hat OpenShift
    - JINX-0164
    - AUDIOFIX
    - MiniRAT
    - velora-dex/sdk
    - DICOM
    - Pydicom
    - Orthanc
    - 39 seconds to exfil
    - 25 minutes AI-assisted exfil
    - frontier AI 3-5 month weaponization window

triage_tags:
  - pre_brief_sentinel
  - am_pre_brief_scheduled
  - tracked_actor_001_teampcp_unit42_extortion_economy_tgr_cri_1135_mapping
  - tracked_actor_007_sandworm_unit42_world_cup_razing_ursa_alias
  - tracked_actor_013_scattered_spider_unit42_muddled_libra_alias
  - tracked_actor_014_handala_hack_unit42_world_cup_banished_kitten_storm_0842_alias_cluster
  - shinyhunters_carnival_cruise_6m_confirmation_b_grade_relay
  - shinyhunters_bling_libra_unit42_formal_alias_mapping
  - iran_cyber_watch_carry_forward_cyberav3ngers_ot_targeting
  - iran_cyber_watch_carry_forward_handala_mois_front
  - critical_cve_samba_4408_9_0_dib_relevant
  - critical_cve_xorg_34000_34002_9_1
  - high_cve_redhat_quay_32590_container_registry_dib
  - frontier_ai_weaponization_3_5_month_horizon_per_unit42
  - kev_t_minus_1_exchange_litespeed_friday_2026_05_29
  - kev_t_past_drupal_t_plus_5h_state_monitoring
  - kev_t_minus_13_mini_shai_hulud_nx_console_2026_06_10
  - ad_direct_carry_forward_vt_010_yamcs_corpus_locked_pm_27
  - jinx_0164_situational_awareness_carry_forward_no_roster_overlap
  - mandiant_endpoint_canonicalization_recommendation_persisting
  - gitea_cve_2026_27771_anti_noise_corpus_lock_continues_securityweek_30k_deployments_relay

iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-26T07:34:00-04:00

# ============================================================================
# Sources queried — health snapshot
# ============================================================================
sources_queried:
  a_grade_healthy:
    - cisa-advisories                   # all.xml reachable; 0 items in window
    - cisa-kev                          # JSON reachable; catalog version 2026.05.27 (no 2026-05-28 adds; three 2026-05-27 adds already absorbed PM-27)
    - mandiant                          # mandiant.com/resources/blog/rss.xml alt endpoint reachable; 0 items in window (Mandiant cloud.google.com feedburner remains dead — pattern unchanged from prior sweeps)
    - unit42                            # feedburner reachable; 2 items in window (BOTH productive — World Cup attack surface + Out of the Crypt extortion economy)
    - mstic                             # parent feed reachable; 0 items in window (last_modified 2026-05-27T20:43 UTC pre-window)
    - crowdstrike                       # feed reachable; persistent-dateless-marketing pattern unchanged; GlassWorm takedown post still surfaces but is the corpus-locked one (raw-2026-05-27-am-001 → finding-2026-05-27-0001)
    - sans-isc                          # rssfeed.xml reachable; 1 item in window (StormCast podcast placeholder, no body content)
    - cisco-talos                       # blog.talosintelligence.com/rss reachable; 1 item in window (DICOM heap overflow research, medical-imaging — A&D-relevance NIL, NOT raw-signaled per Mode 1 discipline)
  a_grade_provisional_in_window:
    - wiz-research                      # JINX-0164 via THN 03:54 EDT relay; A-grade provisional; novel actor explicitly DISCLAIMS roster overlap (incl. BlueNoroff/Stardust Chollima); situational-awareness carry-forward from 06:00 FLASH sentinel
    - bitdefender                       # feed endpoint 404 today; B-grade fallback path not exercised this sweep
    - sentinelone                       # not exercised this sweep
    - sophos                            # category feed reachable; 0 items in window
  b_grade:
    - bleepingcomputer                  # RSS reachable; 3 items in window (Carnival Cruise / ShinyHunters PRODUCTIVE + Sextortion sentencing law-enforcement post-mortem out-of-scope + GPU-mining SEO poisoning AI chatbot anti-noise vs raw-2026-05-27-am-006 MSTIC primary)
    - securityweek                      # RSS reachable; 3 items in window (Gitea CVE-2026-27771 30k-deployments framing anti-noise vs raw-2026-05-27-am-003; Agentic Era opinion off-scope; Google AI Threat Defense Platform product news off-scope per 06:00 FLASH sentinel)
    - thehackernews                     # feed reachable; 1 item in window (JINX-0164 anti-noise vs 06:00 FLASH sentinel)
    - darkreading                       # RSS reachable; 1 item in window (Nordic CISOs opinion off-scope per 06:00 FLASH sentinel)
    - the-record                        # RSS reachable; 0 items in window
    - krebsonsecurity                   # RSS reachable; 0 items in window
    - industrial-cyber                  # 403 on feed endpoint; not exercised this sweep
  reference:
    - nvd                               # REST API lastModStartDate window query: cvssV3Severity=CRITICAL → 3 results (Samba 4408 / X.Org 34000 / X.Org 34002); cvssV3Severity=HIGH → 14 results (Red Hat Quay 32590 + 13 lower-priority WordPress/Defender/KubeVirt items). ALL 3 CRITICAL + Quay HIGH raw-signaled in AM-004.
    - github-advisories                 # global advisories.atom 406-persistent; per-repository GHSA fallback not triggered this sweep
    - mitre-attack                      # static reference; not exercised this sweep
  first_party_splunk:
    - "index=archimedes earliest=-24h@h (20 events all operational meta — scheduler / brief_published / git_committed / flash_sweep_clean / pre-brief-morning started 2026-05-28T07:30:02; NO IOC sourcetype)"
    - "index=defenseclaw_local earliest=-24h@h (0 events; no telemetry source feeding index in current steady state, consecutive_dormant_sweeps_defenseclaw=66 per 12:00 FLASH yesterday)"

items_returned_in_window: 14
items_filtered_in_window: 7        # Carnival + World Cup + Out of the Crypt + 3 NVD criticals batched + Red Hat Quay
items_raw_signaled_this_sweep: 5   # AM-000 (this sentinel) + AM-001 Carnival + AM-002 Unit42 World Cup + AM-003 Unit42 Out of the Crypt + AM-004 NVD critical CVE batch
items_discarded_off_scope: 6       # Sextortion sentencing + Nordic CISOs opinion + Google AI platform product news + ISC StormCast placeholder + Agentic Era opinion + Talos DICOM medical-imaging research
items_absorbed_anti_noise: 3       # Gitea CVE-2026-27771 SecurityWeek relay + GPU-mining AI-chatbot poisoning BleepingComputer + JINX-0164 THN

# ============================================================================
# Carry-forward absorptions
# ============================================================================
anti_noise_locks_active: 11        # Carry-forward from PM-27 (10 active) + new this sweep: Carnival Cruise / ShinyHunters confirmation now active anti-noise for the BleepingComputer Sergiu Gatlan single-source layer until/unless Carnival Corp 8-K disclosure or SEC/independent corroboration shifts to multi-source
kev_deadline_locks_active: 5       # CVE-2026-42897 Exchange T-1d, CVE-2026-48172 LiteSpeed T-1d, CVE-2026-45321 Mini Shai-Hulud T-13d, CVE-2026-48027 Nx Console T-13d, CVE-2026-9082 Drupal T+1d (expired)
investigation_carryforward_active: inv-2026-05-26-001    # LACMTA / Iran / Black Shadow / MOIS — finding-2026-05-27-0004 amended PM-27 with The Record relay

# ============================================================================
# Source-health observations this sweep
# ============================================================================
source_health_changes: []
source_health_notes: |
  All A-grade sources returned successful HTTP responses in window
  (CISA Advisories all.xml, CISA KEV JSON, MSTIC parent feed, CrowdStrike
  RSS, SANS ISC rssfeed.xml, Cisco Talos blog/rss/, Mandiant mandiant.com/
  resources/blog/rss.xml alt endpoint, Unit 42 feedburner). NVD REST API
  responded normally to lastModStartDate window query. B-grade sources
  likewise (BleepingComputer, SecurityWeek, The Hacker News, Dark Reading,
  The Record, Krebs on Security). Two non-blocking observations:
    1. Mandiant cloud.google.com/blog/topics/threat-intelligence/rss/
       remains dead (sixth consecutive sweep including this AM-28);
       mandiant.com/resources/blog/rss.xml continues as productive
       endpoint. Source-grades.yaml entry still cites the dead feedburner
       URL — operator endpoint-canonicalization recommendation carries
       forward. NOT updating source-health.yaml this sweep because the
       alt endpoint IS working and source-health currently marks
       mandiant status: healthy on last_successful_fetch 2026-05-07.
    2. industrialcyber.co/feed/ 403 today — not exercised; B-grade
       relay channel for ICS/OT context. Source-grades.yaml has
       industrialcyber-co as provisional-B awaiting ratification per
       relay-layer-conflation observation 2026-05-13. Pattern unchanged
       this sweep.
  No source-health.yaml runtime field updates required this sweep —
  all healthy sources confirmed healthy, no soft-failure increment,
  no recovery flip, no stale flip.

# ============================================================================
# Splunk first-party check
# ============================================================================
splunk_first_party:
  defenseclaw_local: "0 events over -24h@h (no telemetry source feeding index in current steady state; consecutive_dormant_sweeps_defenseclaw=66 carry-forward from 12:00 FLASH yesterday — same canonical no-hits outcome)"
  archimedes: "20 events over -24h@h, all operational meta (archimedes:scheduler started/completed + archimedes:operation flash_sweep_clean / brief_published / git_committed); no IOC sourcetype"
  ioc_hits: 0
  notes: |
    No first-party telemetry corroboration possible in current steady state.
    Brief-publish trace from PM-27 confirmed at 2026-05-27T16:34:00 EDT
    via Discord message_id 1509293548162383942 (preflight 13/13). 00:00 FLASH
    and 06:00 FLASH sentinels both committed cleanly (47929b7 / bb4b3c9) with
    Splunk events emitted.

# ============================================================================
# Disposition
# ============================================================================
disposition: |
  AM-28 pre-brief sweep yields FIVE raw-signal files including this
  sentinel. Three Unit 42 / BleepingComputer items mapped to
  TRACKED-ROSTER actors (#001 TeamPCP via TGR-CRI-1135 explicit alias,
  #007 Sandworm via Razing Ursa explicit alias, #013 Scattered Spider
  via Muddled Libra explicit alias, #014 Handala Hack via Banished
  Kitten / Storm-0842 / Void Manticore alias cluster). One additional
  raw-signal covers the three CRITICAL CVEs published in the NVD
  lastModStartDate window 2026-05-27T21:30 EDT → 2026-05-28T07:30 EDT
  (Samba CVE-2026-4408 CVSS 9.0 DIB-relevant, X.Org X server
  CVE-2026-34000 + CVE-2026-34002 CVSS 9.1 each, plus the in-window
  HIGH CVE-2026-32590 Red Hat Quay CVSS 8.8 grouped into the same
  raw-signal as a vendor-batch entry).

  Item-class summary for the grader:
    - Carnival Cruise ShinyHunters 6M-records B-grade confirmation
      (BleepingComputer single-source today; ShinyHunters self-claim
      from April 2026, Carnival Corp 8-K + customer-notification
      filings cited). The grader can elect anti-noise absorb under the
      broader ShinyHunters / Bling Libra / Scattered LAPSUS$ Hunters
      cluster covered by Unit 42 (AM-003) or treat as standalone
      breach-confirmation finding. ShinyHunters mapping to Bling Libra
      alias is FORMALLY codified in Unit 42 piece for the first time
      in Archimedes corpus.
    - Unit 42 World Cup attack surface A-grade primary names roster
      #014 Handala Hack (aliases incl. Banished Kitten + Storm-0842 +
      Void Manticore + Cobalt Mystique) as MOIS front + CyberAv3ngers
      (aliases incl. Shahid Kaveh Group + Bauxite + Hydro Kitten +
      Storm-0784 + UNC5691) IRGC Cyber-Electronic Command OT-targeting
      arm. Names Sandworm via Razing Ursa alias. Names Scattered Spider
      via Muddled Libra alias. Per Hard Rule 2, all attribution language
      preserved verbatim ("highly likely" Iran-nexus disruptive ops,
      "highest-volume highest-likelihood" cybercrime). Article focuses
      on sporting-event infrastructure / hospitality / municipal
      services / fan platforms — NO A&D / aerospace / defense sector
      mention. AD-relevance INDIRECT via tracked-actor capability
      observation, NOT via sector targeting. Notable: CISA AA26-097A
      cited as documenting "active, ongoing Iranian-affiliated
      campaign" against Rockwell Allen-Bradley PLCs in US critical
      infrastructure — defender carry-forward for OT estates.
    - Unit 42 Out of the Crypt extortion economy A-grade primary
      formally aliases TGR-CRI-1135 = TeamPCP (roster #001) with
      multi-attack supply-chain profile (20+ attacks / 500+ software
      pieces). Names Bling Libra = ShinyHunters alias formalization.
      Names Hazy Scorpius = CLOP. Documents CL-CRI-1116 BlackFile →
      Redact rebrand (Figures 6-7 May 2026, swatting double-extortion).
      Frontier-AI weaponization 3-5 month projection — Anthropic
      disclosure: Mythos AI model identified ~23,000 potential
      vulnerabilities across 1,000 open-source projects. SymJack +
      ATHR named as AI-attack TTPs. Carnival Cruise + Charter
      Communications NOT referenced in body. Quote: "39 seconds for
      threat actors to move from initial access to data exfiltration."
    - NVD-window CRITICAL CVE batch: Samba CVE-2026-4408 CVSS 9.0
      published today (OS command injection in samba-dcerpcd via
      check-password-script %u substitution; non-standard configuration
      but DIB-relevant because Samba is widely deployed as Linux file
      server and domain controller across government, DoD contractor,
      and ITAR-regulated R&D estates). X.Org CVE-2026-34000 and
      CVE-2026-34002 each CVSS 9.1 (XKB geometry / modifier-map OOB
      read affecting X.Org X server across RHEL 6.0 / 7.0 / 8.0 / 9.0 /
      10.0 — XKB processing functions). Red Hat Quay CVE-2026-32590
      CVSS 8.8 (resumable container image layer upload deserialization
      → arbitrary code execution on Quay server; affects Mirror Registry
      for Red Hat OpenShift). None KEV-listed. None ITW-flagged. All
      have Red Hat advisories.

  Discards and absorptions documented in items_returned_in_window
  tallies above. No FLASH-tier items this sweep — all three
  TRACKED-ROSTER mappings are A-grade Unit 42 single-source attributions
  on alias-cluster mapping (not new campaigns), and the NVD critical
  CVE batch lacks active-exploitation framing. AM-28 brief proceeds
  on standard cadence at 08:00 EDT.

  Carry-forward awareness items for grader:
    - JINX-0164 (Wiz Research A-grade provisional) per 06:00 FLASH
      sentinel — novel actor, no tracked-roster overlap, no A&D nexus,
      explicit disclaim of BlueNoroff/Stardust Chollima overlap.
      Situational awareness only.
    - Google AI Threat Defense Platform (SecurityWeek 09:55 EDT today
      relay, Mandiant + Wiz + Gemini consolidation) — vendor product
      news, no threat content. Briefer may absorb as situational-
      awareness platform-consolidation framing.
    - Cisco Talos DICOM / Pydicom / GDCM / Orthanc heap-overflow
      research today 06:00 EDT — medical-imaging vulnerability deep
      dive on Orthanc PACS, NOT A&D-relevant. Talos is A-grade in
      window but article scope is healthcare. DISCARDED per Mode 1
      discipline; flagged in items_discarded_off_scope tally.
    - Mandiant endpoint canonicalization: mandiant.com/resources/blog/
      rss.xml continues as the working endpoint while feedburner / cloud.
      google.com both remain broken — sixth consecutive sweep with this
      pattern. Operator decision on source-grades.yaml entry URL still
      pending. NOT a source-health.yaml change since both source-health
      and source-grades reflect the broken feedburner URL with the
      alt-endpoint workaround documented in notes.

quiet_hours_status:
  in_active_hours_now: false
  active_hours: "09:00-21:00 EDT"
  current_time_local: "2026-05-28T07:34:00-04:00"
  rationale: |
    07:34 EDT is OUTSIDE active hours (active 09:00-21:00). Not a
    FLASH sweep — this is the scheduled pre-brief collection feeding
    the 08:00 EDT morning brief. Active-hours posture is informational
    only for pre-brief sweeps.

anti_noise_rule_check:
  one_per_trigger_topic_per_24h: not_applicable_pre_brief
  b2_minimum_grade: applied_for_grader_use
  red_team_mandatory_above_very_likely: not_applicable_pre_brief
  weekly_count_against_self_review_threshold: tbd_post_brief
---

# Pre-brief sweep — AM-28 morning collection sentinel

Canonical AM-28 pre-brief sweep document. Frontmatter carries the full
source-coverage map, match-reason tags (4 tracked roster actors + 4
new CVEs + 7 corpus-tracked vulns), source-health observations, Splunk
first-party check (0 IOC hits expected in steady state), and the
disposition narrative for the grader.

Four substantive raw-signal files written this sweep:
  - **AM-001** Carnival Cruise / ShinyHunters 6M-records confirmation
    (B-grade BleepingComputer relay of Carnival 8-K + customer
    notification; April 2026 ShinyHunters self-claim corroborated
    today). Roster #013 Scattered Spider alias-cluster relevance via
    Unit 42 Bling Libra / Scattered LAPSUS$ Hunters mapping (AM-003).
  - **AM-002** Unit 42 (Justin Moore) "2026 World Cup: Discussing the
    World's Biggest Game's Attack Surface" — names roster #014 Handala
    Hack + tracked-actor Sandworm (Razing Ursa alias) + tracked-actor
    Scattered Spider (Muddled Libra alias) + non-roster CyberAv3ngers
    + NoName057(16). Article scope: sporting infrastructure / municipal
    OT / hospitality; NO A&D sector mention.
  - **AM-003** Unit 42 (Matt Brady + Justin Moore) "Out of the Crypt:
    The Evolving Cyber Extortion Economy" — formally aliases
    TGR-CRI-1135 = roster #001 TeamPCP, Bling Libra = ShinyHunters,
    Hazy Scorpius = CLOP. Frontier-AI 3-5 month weaponization
    projection. 39-second initial-access-to-exfil benchmark.
  - **AM-004** NVD-window CRITICAL CVE batch — Samba CVE-2026-4408
    CVSS 9.0 (DIB-relevant: file server + domain controller),
    X.Org CVE-2026-34000 + CVE-2026-34002 CVSS 9.1 each (X.Org X server
    XKB), Red Hat Quay CVE-2026-32590 CVSS 8.8 (container registry,
    DIB DevOps relevant). All four published / lastModified in the
    NVD window.

See per-file frontmatter for IOC-extraction, A&D-relevance, attribution
language preservation, KEV status, and grader-actionable triage tags.

---

## Sentinel disposition for AM-28 morning brief

Grader: four substantive raw-signals + this sentinel. Two TRACKED-ROSTER
actor pieces (Unit 42 World Cup + Out of the Crypt) are A-grade
attribution-language preservation cases; one supply-chain BREACH
confirmation (Carnival) is B-grade single-source claim with extortion-
group self-claim corroborated by victim 8-K; one CVE-batch (NVD-window)
is A-grade reference-only with no active-exploitation framing.

Briefer: standing sections likely to populate include:
  - **Aerospace & Defense** — light-touch (Yamcs VT-010 PM-27 carry-
    forward + Samba CVE-2026-4408 DIB-relevant new CVE; no fresh prime
    naming this sweep).
  - **Iran Cyber Watch** — Unit 42 World Cup names roster #014 Handala
    Hack (alias-cluster) + non-roster CyberAv3ngers as MOIS / IRGC
    fronts. INDIRECT relevance — no campaign claim, framing is
    "highly likely" prospective threat assessment for World Cup
    timeframe. Carry-forward from PM-27 (LACMTA / Black Shadow / MOIS
    inv-2026-05-26-001).
  - **KEV deadline tracking** — five locks active: Exchange T-1d Fri
    2026-05-29 (anti-noise lock), LiteSpeed T-1d Fri 2026-05-29,
    Mini Shai-Hulud T-13d 2026-06-10, Nx Console T-13d 2026-06-10,
    Drupal T+1d post-deadline state-monitoring.

Librarian: no source-health.yaml runtime updates required this sweep.
Mandiant endpoint canonicalization operator-decision still pending
(sixth consecutive sweep with alt-endpoint workaround productive).
