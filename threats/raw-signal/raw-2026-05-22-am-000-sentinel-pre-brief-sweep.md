---
raw_id: raw-2026-05-22-am-000-sentinel
collected_at: 2026-05-22T07:34:00-04:00
run_id: pre-brief-20260522-073000
collection_mode: pre_brief_collection
sentinel: true
test: false
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel — 2026-05-22 morning pre-brief sweep"
  source_url: null
  published_at: 2026-05-22T07:34:00-04:00
sweep_window:
  start: 2026-05-21T17:30:00-04:00
  end: 2026-05-22T07:30:00-04:00
sources_queried:
  - bleepingcomputer       # RSS 200, last_modified 2026-05-22T11:21 GMT, 1 in 14h window — "US and Canada arrest and charge suspected Kimwolf botnet admin" (Sergiu Gatlan 09:01 GMT / 05:01 EDT); WebFetch followup confirmed DoD-IN IP-range targeting context BUT no named A&D-prime/DIB victim, no roster actor, no CVE, no IOC; DISCARDED per Mode 1 (no watchlist/roster/vuln-index hit) — DoD-network-targeting context flagged for briefer awareness
  - thehackernews          # feedburner 200, last_modified 2026-05-22T11:25 GMT, 3 in 14h window — (a) Kimwolf coverage (parallel to BleepingComputer above, DISCARDED same rationale); (b) "CISA Adds Exploited Langflow and Trend Micro Apex One Vulnerabilities to KEV" (05:47 GMT / 01:47 EDT) DEDUP via 2026-05-21 16:00 afternoon brief finding-2026-05-21-0008 lock through 2026-05-22T16:00 EDT; (c) "Cisco Patches CVSS 10.0 Secure Workload REST API Flaw" (05:36 GMT / 01:36 EDT) DEDUP via 2026-05-20 afternoon brief finding-2026-05-20-0006 (formal lock expired 2026-05-21T16:00 EDT but topic carried by 2026-05-21 afternoon brief context)
  - securityweek           # RSS 200, last_modified 2026-05-22T09:24 GMT, 3 in 14h window — (a) "Grafana Says Codebase and Other Data Stolen via TanStack Supply Chain Attack" (Ionut Arghire 07:49 GMT / 03:49 EDT) CRITICAL — first directly-confirmed enterprise-named-victim disclosure on VT-006 / Mini Shai-Hulud with May-11 detection + May-16 ransom-demand + May-22 public-disclosure timeline AND specific unrevoked-workflow-token causation; raw-signaled AM-001 as procedural-facts upgrade inside TeamPCP/TanStack/Nx Console campaign-chain lock from 2026-05-21 morning brief finding-0007 (lock expires concurrent with this brief at 2026-05-22T08:00 EDT); (b) "TrendAI Patches Apex One Zero-Day Exploited in the Wild" (Eduard Kovacs 08:19 GMT / 04:19 EDT) DEDUP via afternoon brief finding-0008 KEV lock; (c) "First VPN Cybercrime Service Disrupted" (Eduard Kovacs 09:24 GMT / 05:24 EDT) DEDUP (recurring item from 2026-05-21 12:00 + 18:00 sentinel discards)
  - therecord              # feed 200, 2 in 14h window — (a) "Hackers steal patient and billing data from German hospitals via third-party provider" (23:00 GMT / 19:00 EDT) healthcare third-party breach (Unimed billing services for privately insured patients across German hospitals), NOT A&D / NOT roster / NOT vuln-index; DISCARDED per Mode 1; (b) "CISA to allow researchers to report vulnerabilities to exploited bugs catalog" (2026-05-23T01:11 GMT = 2026-05-22T21:11 EDT — published in OUR future from this sweep, likely The Record server clock or feed-publish timestamp pulled-forward; KEV-nomination-form governance announcement) procedural CISA policy item, NOT threat-research, no actor / CVE / IOC; DISCARDED per Mode 1 — flagged for briefer awareness as KEV-program governance evolution context
  - darkreading            # rss.xml 200, last_modified 2026-05-22T11:31 GMT, 1 in-window article-class item — "China's Webworm Uses Discord, Microsoft Graphs to Hack EU Govts" (Alexander Culafi 07:01 GMT / 03:01 EDT); Webworm is a non-roster Chinese APT cluster (per Symantec historical naming, sometimes linked to Space Pirates / Webworm overlap); article describes Discord + Microsoft Graph API C2 + SOCKS5 + SoftEther VPN tunneling against EU government targets; NOT a roster actor (Webworm is not in _roster.yaml), NOT direct A&D-prime targeting (EU govts named not specific contractors); no CVE / no specific IOC visible in summary; Trigger 4 (TTP-change-on-tracked-actor) FAILS on no-roster-actor prong; DISCARDED per Mode 1 — flagged as potential /new-actor candidate for actor-profiler review given Microsoft-Graph-API + Discord-C2 + SOCKS5 cloud-living-off-trusted-services TTP pattern (DEFERRED, not raw-signaled)
  - unit42                 # feedburner 200, last_modified 2026-05-22T10:22 GMT, 1 in 14h window — "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud" (Bill Batchelor + Eyal Rafian 10:00 GMT / 06:00 EDT); NAMES four nation-state actors: Cloaked Ursa (= Midnight Blizzard = APT29 = roster #009), Curious Serpens (= Peach Sandstorm = APT33 NOT in roster), UTA0355 (Russian state-affiliated NOT in roster but cited via Volexity 2025), Void Blizzard (tag only, not in body); deep TTP-class research on ROADtools (open-source roadrecon/roadtx) Azure / Entra ID enumeration + token-exchange + device-registration + Conditional-Access-Policy-bypass + Primary-Refresh-Token (PRT) hijack patterns; no explicit "high confidence" / "moderate confidence" attribution language — describes "early observation" / "Volexity reported in 2025" with measured attribution discipline; no A&D-prime victim named (article frames "high-value targets" generically); MITRE ATT&CK techniques T1098.005 + T1550 + T1087 documented; UA-string + device-registration IOCs (DESKTOP-<8 digits> + OS 10.0.19041.928); raw-signaled AM-002 as roster-actor TTP-class research (APT29 tradecraft research) — Trigger 4 candidate for grader evaluation (tracked-actor TTP change documented by A-grade vendor)
  - mandiant               # feedburner persistent 404 (20+ consecutive sweeps; held healthy pending operator alt-endpoint decision per source-health.yaml notes); not separately WebFetched on cloud.google.com index page this sweep — pattern entrenched
  - mstic                  # Microsoft Security Blog feed 200, last_modified 2026-05-21T21:29 GMT pre-window, 0 in-window items
  - crowdstrike            # crowdstrike.com/blog/feed/ 200, last_modified 2026-05-22T08:57 GMT inside window from feed-server activity, 10 items total all null-timestamped marketing/MQ/monthly-retrospective pattern (15+ consecutive sweeps in this pattern); 0 in-window NEW threat-intel items
  - cisco-talos            # blog.talosintelligence.com/rss 200, etag W/"6e4f9-vUhizaj3z8NGfDXZMf+KG5BA7OU" unchanged from 12:00 sentinel, 0 in-window items
  - sentinel-one-labs      # sentinelone.com/labs/feed/ 200, last_modified 2026-05-21T16:47 GMT pre-window, 0 in-window items
  - welivesecurity         # ESET WeLiveSecurity feed 200, 0 in-window items
  - sophos-threat-research # news.sophos.com/en-us/category/threat-research/feed/ 200, 0 in-window items
  - github-blog-security   # github.blog/category/security/feed/ 200, last_modified 2026-05-22T00:23 GMT inside window from feed-server activity, 0 in-window items
  - cisa-advisories        # all.xml fetch_feed 200, 30 items in feed, 0 in 14h window since 2026-05-21T17:30 EDT
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — catalogVersion 2026.05.21, dateReleased 2026-05-21T18:43:06Z; 0 entries dated 2026-05-22; most recent KEV adds remain 2026-05-21 double-add (CVE-2026-34926 Trend Micro Apex One + CVE-2025-34291 Langflow) DEDUP via afternoon brief finding-0008 lock through 2026-05-22T16:00 EDT
  - nvd                    # REST API lastModStartDate=2026-05-21T22:00Z lastModEndDate=2026-05-22T11:30Z cvssV3Severity=CRITICAL → 1 result CVE-2026-42822 (Microsoft Azure Local Disconnected Operations improper authentication CVSS 10.0, CWE-287, published 2026-05-18 lastModified 2026-05-21T23:45Z) raw-signaled AM-003 as fresh-critical-disclosure-surface; cvssV3Severity=HIGH → 1 result CVE-2026-23281 (Linux kernel libertas WiFi driver UAF 7.8 LPE, CWE-416, published 2026-03-25 lastModified 2026-05-22T00:31Z) — kernel WiFi driver LPE 2-month-aged disclosure with metadata refresh, NOT A&D-direct (libertas is generic WiFi driver), DISCARDED per Mode 1
  - securityaffairs        # feedburner 200, last_modified 2026-05-22T09:56 GMT, 1 in 14h window — "One Telecom Provider Hosted Most of the Middle East's Active C2 Infrastructure" (Pierluigi Paganini 07:29 GMT / 03:29 EDT) Hunt.io research relay on 1,350+ C2 servers across 14 Middle East countries; STC (Saudi Telecom Company) = 72.4% of regional C2 hosting; Türk Telekom highest malware diversity; Regxa (Iraq) "bulletproof hosting" hosted Eagle Werewolf (NOT roster) Feb 2026 espionage with EchoGather RAT + Sliver + SoullessRAT + AquilaRAT against "state and industrial entities" using Starlink registration + drone training lures; DYNOWIPER Poland-energy-sector + RondoDox Iranian-infrastructure adjacent mentions; NO roster-actor attribution (Eagle Werewolf NOT in roster); NO A&D-prime victim; NO CVE; NO specific IOC retrievable from article body beyond regxa.iq provider; DISCARDED per Mode 1 — flagged for briefer awareness as infrastructure-mapping methodology + Iranian/MENA-region C2-concentration context
  - krebs                  # feed 200, last_modified 2026-05-21T21:50 GMT, 1 in 14h window — "Alleged Kimwolf Botmaster 'Dort' Arrested, Charged in U.S. and Canada" (Brian Krebs 21:50 GMT / 17:50 EDT) parallel coverage to BleepingComputer Kimwolf above; DoD-IN IP-range-targeting + DCIS-investigating context with $30 Tbps DDoS volume record; no roster actor, no CVE, no A&D-prime victim; DISCARDED per Mode 1 — DoD-network-targeting context flagged for briefer awareness (same as BleepingComputer item)
  - sans-isc               # RSS 200, last_modified 2026-05-22T11:29 GMT, 2 in 14h window — (a) "Cross-Platform NPM Stealer" diary (Friday May 22 06:14 GMT / 02:14 EDT) static-only analysis of Node.js stealer SHA256 049300aa5dd774d6c984779a0570f59610399c71864b5d5c2605906db46ddeb9 (~"extracted-decoded.js" VT upload); NO campaign attribution, NO actor named, NO target sector named; commodity supply-chain malware analysis class; DISCARDED per Mode 1 (no roster/A&D hit) — hash flagged for IOC-master-index awareness only (single sample, single source, B-grade community diary); (b) ISC Stormcast podcast detail Friday May 22 02:00 GMT (off-filter — podcast metadata only)
  - theregister-security   # atom 200, 3 in 14h window — (a) "Cisco AI Incident Reports" (Nate Pors/Cisco Talos blog relay, 05:38 GMT / 01:38 EDT) LLM-methodology-for-IR essay, NOT threat-research, no actor / CVE / IOC; DISCARDED; (b) "Dems slam Trump cyber budget cuts" (23:03 GMT prev day / 19:03 EDT) political/policy reporting on CISA budget + SLCGP + MS-ISAC fee model shift; off-filter for current sweep but flagged for briefer awareness as policy-context evolution; DISCARDED per Mode 1; (c) "Trump Mobile data leak 27k records" (10:59 GMT / 06:59 EDT) consumer-data-leak HTTP POST endpoint exposure; NOT A&D / NOT roster / NOT vuln-index; DISCARDED per Mode 1
  - cybersecuritydive      # feeds/news/ 200, last_modified 2026-05-21T15:00 GMT pre-window, 0 in-window items
  - github-advisories      # global advisories.atom 406 pattern entrenched (~10+ consecutive checks); not re-tested this sweep — per-repository GHSA fallback path remains the productive workaround when triggered (not triggered this sweep)
  - rapid7                 # rapid7.com/blog/rss/ 200, last_modified 2026-05-22T11:19 GMT inside window from feed-server activity, 0 in-window items (most recent in feed is the Q1 2026 Threat Landscape report from 2026-05-21 captured in afternoon brief finding-0013)
  - dragos                 # dragos.com/blog/feed/ persistent 404 (since 2026-05-13 first observed); failure_count operator-managed; not separately retried this sweep
  - bitdefender-labs       # bitdefender.com/blog/labs/feed/ 404 endpoint not reachable; failure noted (separate top-level health check item — see source_health_changes block)
  - industrialcyber-co     # industrialcyber.co/feed/ 403 endpoint rejected this sweep; failure noted (separate top-level health check item — see source_health_changes block)
  - symantec-threat-intel  # symantec-enterprise-blogs.security.com/blogs/threat-intelligence/feed 404 endpoint not reachable this sweep
  - socket-blog            # socket.dev/blog/rss.xml 404 endpoint not reachable this sweep; per source-grades.yaml socket is provisional B; failure noted as informational
  - proofpoint             # proofpoint.com/us/rss.xml 200, last_modified 2026-05-22T02:26 GMT inside window from feed-server activity, 0 in-window items
  - zdi-blog               # zerodayinitiative.com/blog/?format=rss 200, 0 in-window items
  - cisa-kev-msrc-cve-42822-direct  # WebFetch on msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42822 returned SPA-shell content (same client-side-rendering pattern documented in source-health.yaml prior sweeps); body unreachable via WebFetch; NVD record (lastModified 2026-05-21T23:45Z) used as primary substance source
  - splunk-first-party     # archimedes + defenseclaw_local indexes -14h since 2026-05-21T17:30 EDT, sourcetype filter excludes archimedes:* self-telemetry, 0 non-self events (54th consecutive dormant non-self sweep across the pre-brief + flash cadence)
match_reason:
  watchlist: []
  actors:
    - TeamPCP                  # Grafana confirmed-victim disclosure (AM-001); attribution layer unchanged — Grafana names no actor (per Hard Rule 2) but the breach vector is the TanStack-token-chain from VT-006 = TeamPCP-attributed-by-Wiz+StepSecurity per prior reporting
    - APT29                    # Unit 42 ROADtools research names Cloaked Ursa = Midnight Blizzard = APT29 (AM-002); roster #009
  vulnerabilities:
    - CVE-2026-45321           # VT-006 / Mini Shai-Hulud — Grafana named-victim disclosure (AM-001) is procedural-facts upgrade inside existing TanStack/TeamPCP campaign-chain lock
    - CVE-2026-42822           # NEW — Microsoft Azure Local Disconnected Operations improper-auth CVSS 10.0 (AM-003); first appearance in Archimedes corpus this window
  keywords:
    - mini_shai_hulud
    - tanstack_supply_chain
    - github_workflow_token_unrevoked
    - grafana_named_victim
    - ransom_demand_rejected
    - cloaked_ursa
    - midnight_blizzard
    - apt29
    - roadtools
    - roadrecon
    - roadtx
    - entra_id_enumeration
    - microsoft_graph_api_abuse
    - primary_refresh_token_hijack
    - conditional_access_policy_bypass
    - device_registration_persistence
    - mfa_circumvention
    - peach_sandstorm
    - apt33
    - curious_serpens
    - uta0355
    - void_blizzard
    - azure_local
    - azure_local_disconnected_operations
    - improper_authentication
    - cvss_10
    - cwe_287
    - kimwolf_botnet_dod_targeting
    - dod_in_ip_range_ddos
    - hunt_io_middle_east_c2_mapping
    - eagle_werewolf
    - dynowiper_poland_energy
    - rondodox_iranian_infrastructure
    - webworm_eu_govts
    - kev_nomination_form_governance
triage_tags:
  - pre_brief_sentinel
  - sweep_complete
  - 14h_window
  - splunk_first_party_zero_hits_54th_consecutive_dormant_sweep
  - mandiant_feedburner_persistent_404_pattern_unchanged_20_plus_sweeps
  - bitdefender_labs_feed_404_observed_this_sweep
  - industrialcyber_feed_403_observed_this_sweep
  - symantec_threat_intel_feed_404_observed_this_sweep
  - socket_blog_feed_404_observed_this_sweep
  - kev_double_add_anti_noise_lock_active_through_2026_05_22_t16
  - teampcp_tanstack_nx_console_anti_noise_lock_concurrent_with_brief_at_2026_05_22_t08
  - cisco_workload_anti_noise_lock_expired_carried_by_afternoon_brief_context
  - grafana_named_enterprise_victim_procedural_facts_upgrade_on_vt_006
  - apt29_cloaked_ursa_unit42_ttp_class_research_trigger_4_candidate_for_grader
  - cve_2026_42822_azure_local_cvss_10_fresh_critical_disclosure_surface
  - dod_in_ip_range_targeting_context_kimwolf_botnet_briefer_awareness
  - kev_nomination_form_governance_evolution_briefer_awareness
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-20T07:34:00-04:00
---

# Pre-brief collection sentinel — 2026-05-22 07:30 EDT cycle

Per INTEL-OPERATIONS.md Mode 1 procedure, the 07:30 EDT scheduled pre-brief
sweep ran across the canonical source set for the 14h window 2026-05-21T17:30
→ 2026-05-22T07:30 EDT. Three raw-signal files written (AM-001 through AM-003)
covering items in window that match the A&D watchlist / actor roster /
tracked-vulnerability filter.

See frontmatter `sources_queried` for the full source-by-source disposition
trail (200/404/parse-error/etag-unchanged, items in window, items raw-signaled,
items discarded with rationale).

## Anti-noise lock posture at sweep time

Six anti-noise locks were active heading into this sweep window per the
2026-05-21 18:00 FLASH sentinel:

1. **CISA KEV double-add 2026-05-21 (Apex One CVE-2026-34926 + Langflow
   CVE-2025-34291)** — afternoon brief finding-2026-05-21-0008.
   **Active through 2026-05-22T16:00 EDT.** Today's SecurityWeek/THN
   restatements DEDUP'd into this lock.

2. **KEV-7 batch 2026-05-20 (Microsoft Defender pair + 5 legacy
   Microsoft/Adobe)** — anti-noise lock nominally expired 2026-05-21T16:00
   EDT but 2026-05-21 morning brief UPDATE block on finding-2026-05-20-0005
   consumed the resurface budget. No new surfaces in window.

3. **Cisco Secure Workload CVE-2026-20223 CVSS 10.0** — 2026-05-20
   afternoon brief finding-2026-05-20-0006. Lock formally expired 2026-05-21
   T16:00 EDT but afternoon brief 2026-05-21 carried context forward.
   THN's 2026-05-22 morning restatement DEDUP'd into the expired-but-carried
   lock per FLASH anti-noise rule 1.

4. **TeamPCP / TanStack / Nx Console campaign chain** — 2026-05-21 morning
   brief finding-2026-05-21-0002 + finding-2026-05-21-0007. **Lock expires
   CONCURRENT with this brief at 2026-05-22T08:00 EDT.** Grafana's
   confirmed-victim disclosure (AM-001) is captured as procedural-facts
   upgrade inside the lock — the May-11 detection + unrevoked-workflow-token
   + May-16 ransom-demand + May-22 public-disclosure timeline closes a
   visible procedural-facts gap on the corpus-level campaign chain (one of
   the three secondary victims named by Nx Team yesterday — OpenAI / Mistral
   AI / Grafana — now has direct first-party self-disclosure attestation).

5. **Drupal CVE-2026-9082 SA-CORE-2026-004** — 2026-05-21 morning brief
   finding-2026-05-21-0004. Lock active through 2026-05-22T08:00 EDT
   (concurrent with this brief). No new surfaces in window.

6. **Chromium Service Worker persistence (no CVE)** — 2026-05-21 afternoon
   brief monitoring-tier surface. Lock active through 2026-05-22T16:00 EDT.
   No new surfaces in window.

## In-window items captured as raw-signal

### AM-001 — Grafana confirmed-victim disclosure on VT-006 / Mini Shai-Hulud / TeamPCP campaign chain

**Source:** SecurityWeek (Ionut Arghire), 2026-05-22T07:49:38Z / 03:49:38 EDT.
Primary substance is Grafana's own incident-disclosure post (relayed via
SecurityWeek per Hard Rule 2 — Grafana names no actor; SecurityWeek does not
originate attribution beyond carry-forward).

**What's new:** First directly-confirmed enterprise-named-victim
self-disclosure on the TanStack supply-chain chain, with three procedural
upgrades beyond what was visible at 2026-05-21 morning brief / afternoon
brief layer:

1. **May-11 detection date** — Grafana detected malicious activity on
   2026-05-11 and "immediately rotated GitHub workflow tokens." This dates
   secondary-victim detection earlier than yesterday's brief surfaced
   (Nx Team named OpenAI / Mistral AI / Grafana as TanStack-chain secondary
   victims but published no per-victim detection timestamps).

2. **Unrevoked token causal claim** — "A subsequent review confirmed that
   a specific GitHub workflow we originally deemed not impacted had, in
   fact, been compromised." This is the load-bearing operational detail:
   incomplete token rotation enabled continued attacker access despite
   initial response. Operationally directly applicable to every Tier-1
   A&D SDLC running GitHub Actions with workflow tokens.

3. **May-16 ransom demand + May-22 public disclosure timeline** — Grafana
   received a ransom demand on 2026-05-16 (rejected); chose to publicly
   disclose on 2026-05-22 after notifying law enforcement. This is the
   first confirmed-monetization-attempt data point on the VT-006 campaign
   chain (prior framing was "supply-chain-credential-theft + worm
   propagation"; the ransom-pivot is new at the secondary-victim layer).

**Scope-bounding claims preserved from Grafana primary:**
- Codebase stolen (public + private GitHub repos)
- Business contact names + email addresses + internal operational info
- NO customer production systems affected
- NO codebase modified
- Grafana Cloud platform operations remained uncompromised

**Hard Rule 2 status:** Grafana names no actor. TeamPCP attribution remains
inherited from VT-006 / Wiz + StepSecurity prior attestation. SecurityWeek
does not originate beyond that. Archimedes does NOT upgrade attribution.

**Grading direction (for grader, not collector):** Inside TeamPCP/TanStack
campaign-chain lock at 2026-05-21 morning brief finding-0007. Whether this
warrants a fresh finding ID vs UPDATE block on 0007/0002 is a grader/briefer
judgment. The May-16 ransom-demand data point and the unrevoked-token
causal claim are both *new procedural facts*, not novel attribution or
novel TTP.

### AM-002 — Unit 42 ROADtools research naming Midnight Blizzard / APT29 + Curious Serpens / APT33 + UTA0355

**Source:** Unit 42 / Palo Alto Networks (Bill Batchelor + Eyal Rafian),
2026-05-22T10:00:24Z / 06:00:24 EDT. Primary research, A-grade vendor source
per source-grades.yaml.

**What's new:** Formal Unit 42 publication on the misuse of ROADtools
(open-source Azure / Entra ID offensive-and-defensive Python framework)
by four named nation-state actors:

1. **Cloaked Ursa = Midnight Blizzard = APT29** (roster #009) — operates
   ROADtools since late 2021 for Azure AD enumeration after spear-phishing
   initial access.

2. **Curious Serpens = Peach Sandstorm = APT33** (NOT in roster) — used
   ROADtools after password-spray attacks in 2023. Iranian nation-state.

3. **UTA0355** (NOT in roster; Russian-aligned per Volexity 2025) — early
   2025 phishing campaign with roadtx-token-management capability
   alignment.

4. **Void Blizzard** (tag-only, not in article body) — no operational
   detail surfaced.

**Documented TTPs (MITRE ATT&CK alignment):**
- **T1098.005** — Device registration in Entra ID as durable persistence
- **T1550** — Stolen Primary Refresh Tokens (PRT) for programmatic
  tenant-wide access
- **T1087** — Account enumeration via Microsoft Graph API endpoints
- Conditional Access Policy (CAP) bypass via device-bound tokens
- MFA circumvention via stolen PRTs
- Rogue device registration with default OS Version 10.0.19041.928
- Device-naming pattern DESKTOP-<8 random digits>

**Hard Rule 2 status:** Unit 42 does NOT use explicit
"high confidence" / "moderate confidence" attribution language —
instead frames as "early observation" + "Volexity reported in 2025."
Conservative attribution discipline preserved verbatim per Hard Rule 2.

**Trigger evaluation context for grader:**
- **Trigger 4 (tracked-actor TTP change):** APT29 is in roster #009.
  Documented activity is from "late 2021" onward — not a fresh-this-week
  TTP class but the formal A-grade vendor publication of the
  ROADtools-misuse TTP cluster IS new this window. The grader should
  evaluate whether this is "new tooling/targeting/infrastructure class
  attributable to a tracked actor" or whether it's a documentation-of-
  existing-tradecraft retrospective. The Microsoft-Graph-API + Entra-ID
  + PRT-hijack pattern is operationally directly applicable to A&D-prime
  M365 / Entra tenancy.

### AM-003 — CVE-2026-42822 Microsoft Azure Local Disconnected Operations CVSS 10.0 (fresh-critical-disclosure-surface)

**Source:** NVD REST API (lastModified 2026-05-21T23:45:12Z inside window).
Microsoft is the CNA; MSRC update-guide entry exists but the MSRC SPA-shell
substance is unreachable via WebFetch (consistent with prior source-health
notes).

**What's new:** CVSS 10.0 critical disclosure on Microsoft Azure Local
(formerly Azure Stack HCI; on-prem Azure equivalent for disconnected /
sovereign / regulated environments). CWE-287 improper authentication.
Pre-auth network-vector unauthorized privilege elevation.

**Substance from NVD record:**
- CVE ID: CVE-2026-42822
- CVSS v3.1: 10.0 / CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- Published: 2026-05-18 (4 days before this sweep)
- LastModified: 2026-05-21T23:45:12Z (inside sweep window via metadata
  refresh, not original publication)
- Affected: Azure Local versions before 2604.2.25645, Azure Resource Manager
- CWE-287 Improper Authentication
- Description: "Improper authentication in Azure Local Disconnected
  Operations allows an unauthorized attacker to elevate privileges over
  a network."

**A&D relevance assessment (for grader):**
Azure Local Disconnected Operations is the canonical Azure-tenancy product
for environments that cannot maintain continuous cloud connectivity —
including ITAR-regulated A&D R&D enclaves, IL5/IL6 sovereign-cloud
deployments, and air-gapped program-data networks. Pre-auth network-vector
auth-bypass with scope-CHANGED in a product line designed for sensitive-
data sovereignty is a high-A&D-relevance signal class. Vendor-product
A-grade procedural-facts authority (Microsoft MSRC is CNA on own product
per established precedent).

**Exploitation status:** NOT determinable from NVD record alone. MSRC
update-guide page is the canonical exploitation-status authority but
the SPA-shell is unreachable via WebFetch. Conservative framing for grader:
no-in-the-wild-exploitation-attestation-visible-from-currently-retrievable-sources.

**Trigger evaluation context for grader:**
- **Trigger 1 (critical-CVE-exploited):** CVSS 10.0 satisfies the 9.0
  floor BUT requires active-exploitation-attested-by-A-grade-source.
  Currently no exploitation attestation visible — would need MSRC
  update-guide direct retrieval (SPA-shell currently blocking) or
  CISA-KEV addition (not yet) or A-grade vendor research publication.
  Most likely PARTIAL Trigger 1 pending exploitation-status retrieval.
- **Trigger 6 (zero-day-no-patch):** Microsoft has assigned the CVE
  with affected/fixed version data implying patches are available
  (Azure Local pre-2604.2.25645 = vulnerable, ≥2604.2.25645 = fixed).
  FAILS Trigger 6 zero-day prong.
- The 4-day-aged disclosure timing (published 2026-05-18, NVD-modified
  2026-05-21) suggests this surfaced into NVD lastModified during the
  current sweep window even though the underlying advisory was earlier
  in the week — analogous to the NVD-lastModified surfacing pattern
  documented in source-health.yaml prior sweeps. Briefer should evaluate
  whether the 4-day-aged item warrants morning-brief inclusion vs.
  waiting for exploitation-status clarification.

## Items DISCARDED per Mode 1 (categorically off-filter or DEDUP'd)

### DEDUP'd via active anti-noise locks
- **CISA KEV double-add restatement** (THN 01:47 EDT + SecurityWeek Trend
  Apex One patch piece 04:19 EDT) — both restate the 2026-05-21 KEV
  addition; absorbed by afternoon brief finding-0008 lock.
- **Cisco Secure Workload CVSS 10.0 restatement** (THN 01:36 EDT) —
  topic carried by 2026-05-21 afternoon brief context per expired-but-
  carried lock rule.

### Off-filter (no roster / no A&D / no vuln-index hit)
- **Kimwolf botnet admin arrest** (BleepingComputer Sergiu Gatlan 05:01
  EDT + THN 04:50 EDT + Krebs 17:50 EDT 2026-05-21). DoD-IN IP-range
  targeting context with DCIS-investigating + ~30 Tbps DDoS-record
  framing. No roster actor (Jacob Butler / Dort is named cybercriminal,
  not in _roster.yaml); no specific A&D-prime victim; no CVE; no IOC
  retrievable from article bodies. DoD-network-targeting context is
  worth briefer awareness but not raw-signal-promote per Mode 1.
- **German hospitals Unimed billing breach** (The Record 19:00 EDT
  2026-05-21). Healthcare third-party breach, NOT A&D / NOT roster /
  NOT vuln-index.
- **CISA KEV nomination form governance** (The Record 2026-05-23T01:11
  GMT — published in our future from this sweep, likely server clock
  or feed-publish-timestamp pulled forward). Procedural KEV-program
  evolution; no actor / no CVE / no IOC. Briefer awareness item.
- **First VPN cybercrime service disruption** (SecurityWeek Eduard
  Kovacs 05:24 EDT). Recurring item from 2026-05-21 12:00 + 18:00
  sentinel discards; LE op against cybercrime infrastructure, no roster
  actor / no A&D-prime victim.
- **China's Webworm via Discord + Microsoft Graphs** (Dark Reading
  Alexander Culafi 03:01 EDT). Non-roster Chinese APT cluster
  targeting EU governments; Microsoft-Graph-API + Discord-C2 + SOCKS5 +
  SoftEther VPN TTP pattern. NOT in roster; potential /new-actor
  candidate for actor-profiler deferral but not Mode 1 raw-signal —
  flagged for awareness.
- **Hunt.io Middle East C2 telco-concentration research** (Security
  Affairs Pierluigi Paganini 03:29 EDT). Infrastructure-mapping
  methodology with Eagle Werewolf (NOT roster) + DYNOWIPER (Poland
  energy) + RondoDox (Iranian infra) adjacent mentions; no roster
  actor primary; no A&D-prime victim; no specific IOC retrievable.
- **NVD CVE-2026-23281 Linux kernel libertas WiFi driver UAF LPE
  CVSS 7.8** — 2-month-aged disclosure with metadata refresh;
  generic WiFi driver, NOT A&D-direct.
- **Cisco AI incident report methodology** (The Register Nate Pors
  relay 01:38 EDT). LLM-for-IR essay, not threat-research.
- **Dems slam Trump cyber budget cuts** (The Register prev evening).
  Political / policy reporting; off-filter for current sweep but
  CISA-budget-context briefer awareness.
- **Trump Mobile data leak 27k records** (The Register 06:59 EDT).
  Consumer data leak; NOT A&D / NOT roster / NOT vuln-index.
- **SANS ISC Node.js NPM stealer static analysis** (06:14 GMT). Single
  SHA256 sample, no campaign / no actor / no target sector. Hash
  awareness only — not IOC-master-index-promote at single-sample
  B-grade level.
- **ISC Stormcast podcast detail Friday May 22** (02:00 GMT). Podcast
  metadata only.

## Source health observations and changes (separate from runtime-state-update block below)

### New observations this sweep
- **bitdefender-labs feed** — bitdefender.com/blog/labs/feed/ returned 404
  this sweep (feed host rejected request). First observation against this
  endpoint shape; previously cited via the bitdefender provisional-A entry
  at finding-2026-05-13-FLASH-0001. Endpoint path may have changed (the
  businessinsights.bitdefender.com path remains the alternative known to
  source-grades.yaml). Flagged for operator alt-endpoint discovery — not
  a runtime-state flip given first failure.

- **industrialcyber-co feed** — industrialcyber.co/feed/ returned 403 this
  sweep (feed host rejected request). Previously surfaced productively via
  finding-2026-05-13-FLASH-1800-0001 + 2026-05-21 sweeps (per prior
  sentinel notes referencing IndustrialCyber as relay). The 403 is a new
  pattern; could be transient (rate-limit / WAF) or persistent (auth-
  required path). First failure observation. Flagged for runtime-state
  awareness — not flipped to stale per the failure-count<2 rule.

- **symantec-threat-intel feed** — symantec-enterprise-blogs.security.com/
  blogs/threat-intelligence/feed returned 404. This was the alternative
  endpoint cited in source-grades.yaml symantec provisional-A entry.
  First failure observation. Flagged for runtime-state awareness.

- **socket-blog feed** — socket.dev/blog/rss.xml returned 404. The Socket
  provisional-B entry in source-grades.yaml does not list a verified RSS
  endpoint; this was a probe-attempt path. Not a regression; just an
  unsuccessful probe.

None of these warrant immediate `status: stale` flip (each is a single
failure observation this sweep; the failure-count>=2 rule has not fired).
Recommended runtime-state actions are documented in the source-health.yaml
updates section below.

### Patterns entrenched this sweep
- **mandiant feedburner persistent 404** — now ~20+ consecutive sweeps;
  pattern fully entrenched, held healthy pending operator alt-endpoint
  decision per source-health.yaml notes.
- **crowdstrike feed null-timestamped marketing pattern** — ~15+
  consecutive sweeps in this pattern; 10 items total, all null-published,
  product/marketing/MQ/monthly-retrospective content; no in-window NEW
  threat-intel items.
- **mstic feed cadence** — quiet through 14h window (last_modified
  2026-05-21T21:29 GMT pre-window).
- **dragos feed 404** — persistent since 2026-05-13 first observed;
  operator alt-path-identification pending.
- **github-advisories.atom 406** — persistent ~10+ sweeps; per-repository
  GHSA fallback path remains productive when triggered.

## Splunk first-party silence

54th consecutive dormant non-self sweep. archimedes + defenseclaw_local
indexes returned 0 events for the -14h window (excluding archimedes:*
self-telemetry). Hard Rule 8 framing: silence is neither confirming nor
disconfirming.

## Quiet hours posture

Current time 07:34 EDT is INSIDE quiet hours window (FLASH-POLICY active
hours 09:00–21:00 EDT applies to FLASH-tier posting; pre-brief collection
is mode-1 independent of quiet-hours posting). Pre-brief sentinel
proceeds normally; grader and briefer will run after this sentinel.

## FLASH-trigger evaluation notes for grader / orchestrator

The grader will run the formal Trigger 1-6 evaluation when promoting raw-
signal to findings. For collector-handoff context, the most FLASH-worthy
items in this sweep window are (in priority order):

1. **CVE-2026-42822 Azure Local CVSS 10.0** (AM-003) — Trigger 1 candidate
   PENDING exploitation-status retrieval (MSRC SPA-shell currently blocks
   substance access). If exploitation is attested in MSRC update-guide
   for this CVE OR if CISA KEV adds it during the 14h forward window OR
   if A-grade vendor research publishes exploitation observation, this
   becomes a full Trigger 1 fire. Until then PARTIAL — fresh-critical-
   disclosure-surface only.

2. **Unit 42 ROADtools / APT29 research** (AM-002) — Trigger 4 candidate.
   APT29 is in roster #009. The grader's call is whether ROADtools-misuse
   TTP cluster constitutes "new tooling/targeting/infrastructure class"
   for APT29 vs. "documentation of pre-existing 2021-onward tradecraft."
   Conservative framing: A-grade vendor formal-publication on roster-
   actor TTP cluster IS new in this corpus, even when the underlying
   activity is multi-year-aged. Grader's judgment.

3. **Grafana confirmed-victim disclosure on VT-006** (AM-001) — INSIDE
   existing campaign-chain lock concurrent with this brief. Procedural-
   facts upgrade (May-11 detection + unrevoked-workflow-token causal
   claim + May-16 ransom-demand + May-22 public-disclosure timeline)
   inside lock. NOT a fresh-FLASH; rather UPDATE-block material for
   the morning brief.

The grader applies the formal evaluation. Collector does not pre-grade.

## Anti-noise distinction from recent FLASHes / briefs / sentinels

- **flash-sweep-20260521-180000 (18:00 EDT sentinel, 0 triggers)** —
  prior FLASH cycle covering 12:00–18:00 EDT window. KEV double-add
  Apex One + Langflow ABSORBED by afternoon brief finding-0008.
- **flash-sweep-20260522-000000 (00:00 EDT sentinel, 0 triggers)** —
  midnight sentinel covered 18:00 EDT yesterday → 00:00 EDT today.
- **flash-sweep-20260522-060000 (06:00 EDT sentinel, 0 triggers)** —
  06:00 sentinel covered 00:00 EDT → 06:00 EDT today, immediately
  before this pre-brief window.
- **2026-05-21 morning brief (08:00 EDT)** — covers TeamPCP/TanStack/Nx
  Console campaign chain (findings 0002 + 0007), Drupal CVE-2026-9082
  (0004), Microsoft Defender pair UPDATE (0001), SonicWall CVE-2024-
  12802 ReliaQuest single-source ITW claim (0006), Unbound CVE-2026-
  42960 + CVE-2026-33278 dual criticals (0005), NVIDIA TRT-LLM
  deserialization cluster (0003). Locks active through 2026-05-22T08:00
  EDT (concurrent with this brief).
- **2026-05-21 afternoon brief (16:00 EDT)** — covers CISA KEV double-
  add Apex One + Langflow (0008), NASA F Prime CVE-2026-41144 (0009),
  ISC BIND 9 CVE-2026-3593 (0010), ABB ICS batch (0011-0012), Rapid7
  Q1 2026 Threat Landscape report (0013), Chromium Service Worker
  monitoring-tier surface (no CVE). Locks active through 2026-05-22T16:00
  EDT.

## Handoff items for tomorrow morning brief composer

The briefer should consider the following as candidates for UPDATE blocks,
fresh-finding inclusion, or monitoring-tier surface:

1. **Grafana confirmed-victim disclosure** (AM-001) — UPDATE block on
   finding-2026-05-21-0007 (TeamPCP/TanStack campaign chain) is the
   natural fit. May-11 detection + unrevoked-workflow-token + May-16
   ransom-demand + May-22 public-disclosure timeline are the three
   procedural-facts upgrades worth surfacing.

2. **Unit 42 ROADtools / APT29 research** (AM-002) — Fresh finding likely.
   APT29 roster #009. TTP-class research is A&D-prime-applicable
   (M365 / Entra tenancy attack surface).

3. **CVE-2026-42822 Azure Local CVSS 10.0** (AM-003) — Fresh finding
   possible if briefer assesses A&D relevance (sovereign/disconnected
   Azure deployments common in ITAR-regulated enclaves) outweighs the
   PARTIAL Trigger 1 status (no exploitation attestation visible yet).
   Monitoring-tier surface as conservative alternative.

4. **DoD-IN IP-range-targeting Kimwolf botnet LE op** (Krebs +
   BleepingComputer + THN parallel) — Awareness-level / monitoring
   surface only. Sophisticated cybercrime DDoS LE action with DoD-network-
   targeting framing; not roster-actor; not A&D-prime-victim. Briefer
   judgment whether to include as awareness item.

5. **Webworm Chinese APT EU-govt campaign** (Dark Reading) — Awareness-
   level only. Potential /new-actor candidate for actor-profiler
   deferral; Microsoft-Graph-API + Discord-C2 TTP pattern noted.

6. **Hunt.io Middle East C2 telco-concentration** (Security Affairs) —
   Awareness-level only. Infrastructure-mapping methodology context;
   no actor / no A&D-prime victim.

7. **CISA KEV nomination form governance** (The Record) — Awareness-
   level only. KEV-program evolution; researchers/vendors/industry
   partners can now nominate via web form.

## source-health.yaml runtime field updates required

The following source-health.yaml entries need runtime field updates to
reflect this sweep's outcomes (preserving operator-set `notes:` fields
verbatim per .claude/agents/collector.md field-ownership doctrine):

- **mandiant**: `last_error` extended to "feedburner.com/Mandiant returned
  404 on 2026-05-22T07:30 pre-brief — twentieth consecutive failure
  (failure_count incremented 18→19→20 across recent sweeps). Pattern
  fully entrenched; held healthy pending operator alt-endpoint decision."
  `failure_count`: 18→20 (incremented twice for 00:00 + 06:00 FLASH
  sweeps not previously updated, plus this pre-brief). `notes:` block
  preserved verbatim.
- **bitdefender** (separate from bitdefender-labs above): existing entry
  in source-grades.yaml is provisional-A; source-health.yaml entry, if
  exists, should reflect that bitdefender.com/blog/labs/feed/ returned
  404 this sweep — single failure, held healthy pending second
  observation per failure-count<2 rule. If no existing source-health
  entry, no runtime update required.
- **industrialcyber-co**: bootstrap new source-health entry as healthy
  with first failure observation (industrialcyber.co/feed/ returned
  403 this sweep — `failure_count`: 0→1, `status: healthy`, `last_error:
  "industrialcyber.co/feed/ returned 403 on 2026-05-22T07:30 pre-brief —
  first failure observation. Could be transient WAF/rate-limit. Held
  healthy per failure-count<2 rule pending second observation."`).
- **symantec**: bootstrap source-health entry if absent, with first
  failure observation on the threat-intelligence/feed endpoint —
  failure-count<2 rule applies.
- **socket**: socket.dev/blog/rss.xml first probe failure — informational;
  the source-grades.yaml entry does not specify a verified feed URL, so
  the failure is not a regression on a known-good endpoint.
- **All healthy sources with successful fetch this sweep**: bleepingcomputer,
  thehackernews, securityweek, therecord, darkreading, unit42, mstic,
  crowdstrike, cisco-talos, sentinel-one-labs, welivesecurity,
  sophos-threat-research, github-blog-security, cisa-advisories, cisa-kev,
  nvd, securityaffairs, krebs, sans-isc, theregister-security,
  cybersecuritydive, rapid7, proofpoint, zdi-blog — update
  `last_successful_fetch: 2026-05-22T07:30:00-04:00`, `failure_count: 0`,
  `status: healthy`, `stale_since: null`, `last_error: null`. Operator-set
  `notes:` blocks preserved verbatim.
- **dragos**: continued 404 since 2026-05-13; not retried this sweep
  (operator-managed). No runtime update required.
- **github-advisories**: continued 406 since 2026-05-08; not retried
  this sweep. No runtime update required.
- **splunk-archimedes** and **splunk-defenseclaw**: 0 non-self events
  this sweep (54th consecutive dormant sweep). Reachable.
  `last_successful_fetch: 2026-05-22T07:30:00-04:00` updated. Operator-
  set notes preserved.

## Extraction notes

- Language: en
- Article type: sentinel
- Raw IOC extraction invoked: no (sentinel — IOC extraction performed on
  AM-001 / AM-002 / AM-003 individually; per-skill output is in those
  files' bodies, not this sentinel)
- Run mode: pre_brief_collection (Mode 1)
- Output mode: sentinel + 3 raw-signal files (AM-001 / AM-002 / AM-003)
- Window: 14h since 2026-05-21T17:30 EDT
- Sources queried: 28 productive (with named-source-id) + 4 endpoint
  failures this sweep (bitdefender-labs, industrialcyber-co, symantec-
  threat-intel, socket-blog) + 2 long-standing failures (mandiant
  feedburner, dragos, github-advisories) + 2 not-tested-this-sweep
  (msrc-defender-update-guide SPA pattern, fortinet-fortiguard SSL
  certificate-mismatch persistent)
- Splunk first-party: 0 non-self events; 54th consecutive dormant sweep
- Active anti-noise locks at sweep time: 6 (KEV double-add Apex One +
  Langflow through 2026-05-22T16:00; KEV-7 batch carry-forward via
  morning UPDATE; Cisco Workload carry-forward via afternoon context;
  TeamPCP/TanStack/Nx Console chain through 2026-05-22T08:00 concurrent
  with this brief; Drupal CVE-2026-9082 through 2026-05-22T08:00; Chromium
  Service Worker through 2026-05-22T16:00)
- Webworm + Eagle Werewolf flagged as awareness-only / not-yet-roster
  /new-actor-deferral candidates per Mode 1 scope discipline
