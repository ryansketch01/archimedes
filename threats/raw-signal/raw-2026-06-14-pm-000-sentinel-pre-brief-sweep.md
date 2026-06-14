---
raw_id: raw-2026-06-14-pm-000
collected_at: 2026-06-14T15:35:00-04:00
run_id: pre-brief-20260614-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: sentinel-internal
  source_name: "Pre-brief sweep sentinel (internal)"
  source_url: null
  published_at: 2026-06-14T15:35:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [pre_brief_sweep, source_health_delta_observed, splunk_sentinel_clean]
triage_tags: [non_flash, sentinel, sweep_clean, pre_brief]
iocs_extracted: false
iocs_count: 0
text_word_count: 1450
promoted: false
ttl_expires_at: 2026-09-12T15:35:00-04:00
---

# Pre-brief sweep 2026-06-14 15:30 EDT — afternoon brief substrate (1 UPDATE-candidate raw-signal, sentinel otherwise quiet)

## Sweep parameters

- Mode: `pre_brief_collection` for the 16:00 EDT afternoon brief
- Time window: 2026-06-14T07:30:00-04:00 → 2026-06-14T15:35:00-04:00 (8h05m since 07:30 pre-brief substrate which fed the 08:00 morning brief). Effective collection window opens at the end of the morning brief's pre-brief substrate close, NOT at 12:00 FLASH close — to capture everything since this morning's brief regardless of intermediate FLASH coverage.
- Active hours per FLASH-POLICY (09:00-21:00 EDT). This is a pre-brief collection, not a FLASH sweep; FLASH-trigger evaluation is downstream-of-grader.
- Sources queried: 18 healthy primary RSS feeds + KEV JSON + Mandiant direct-HTML index + Splunk first-party sentinel.
- Sources skipped (stale, <24h since stale_since per under-24h rule): volexity, msrc, lumen (lumen failure_count=1, not yet stale — held healthy this sweep), shadowserver (same — failure_count=1, held healthy), industrialcyber-co, ars-security, trellix, x-cisagov, x-gossithedog, censys, urlscan, hibp.
- Sources skipped (stale, retried per >=24h rule): mandiant feedburner (retried, still 404 — 28th consecutive observation; direct-HTML path remains the productive endpoint).
- Operator binding: COLLECTION ONLY. No grading, no FLASH evaluation, no brief composition, no Discord posting, no commit.

## In-window content survey

### BleepingComputer — 1 in-window item (UPDATE-candidate)

- **"FBI disrupts massive AI-powered phishing service using a million URLs"** by Bill Toulas (2026-06-14T14:36:23 UTC = 10:36 EDT inside window). Joint FBI + Google + Black Lotus Labs operational takedown of Outsider Enterprise — Chinese-based PhaaS coordinating via Telegram, 9000 fake websites + over a million fraudulent URLs at peak, Shopify e-commerce storefront, SMS smishing channels via AT&T / T-Mobile / Verizon. Article body confirms NO A&D / no DIB / no aerospace / no defense sector mention, NO IOCs disclosed (administration-server seizures referenced at quantity-only granularity), NO CVE references, NO UNC / roster-actor attribution beyond "Outsider Enterprise" (NOT on `_roster.yaml`). Google attribution language: "Based in China" + "coordinating through Telegram." No FBI exploitation-detection-tag attribution.

  This article is the **operational-takedown layer** on top of finding-2026-06-12-0006 (Google civil-suit + Gemini AI weaponization substrate, 12-Jun PM brief). The Gemini AI weaponization narrative is NOT restated in this 06-14 article; this 06-14 article is the FBI operational-disruption layer that ratifies the civil-suit's underlying scale claim (the "million URLs" figure was Google's civil-suit substrate; FBI takedown confirms it independently).

  **Raw-signaled as `raw-2026-06-14-pm-001-bleepingcomputer-fbi-google-blacklotuslabs-outsider-enterprise-takedown-update-on-finding-2026-06-12-0006`** for grader handoff. **UPDATE-on-finding-2026-06-12-0006 candidate** per the 12:00 FLASH sentinel substrate (carry-forward verbatim into this pre-brief). Grader decision: surface as UPDATE bullet in 16:00 afternoon brief or anti-noise-defer if the operational-layer adds insufficient net-new substrate at brief-composition time.

### SecurityAffairs — 2 in-window items, BOTH retrospective newsletters (no net-new substrate)

- **"SECURITY AFFAIRS MALWARE NEWSLETTER ROUND 101"** by Pierluigi Paganini (2026-06-14T13:23:29 UTC = 09:23 EDT just inside window). Weekly malware-research recap listing 15 items: IronWorm (Shai-Hulud rustier-cousin); Trojanized ai-sdk-ollama / Miasma npm worm via binding.gyp (Shai-Hulud-family lineage); Gafgyt C0XMO IoT-botnet variant (06-12 PM substrate); Using AI Agents to Analyze Malware on REMnux (academic); Miasma worm path-of-destruction (Shai-Hulud-family); Shai-Hulud Descends to Hades — Miasma Worm Campaign Spreads with New PyPI Wave (Shai-Hulud-family); VerdantBamboo / BRICKSTORM-in-the-firewall (Mandiant carry on direct-HTML index since 06-13 PM); NFCShare Android Trojan; 400+ AUR Packages Compromised (finding-2026-06-12-0005 Sonatype "Atomic Arch"); Expanded JDY IoT and SOHO botnet (finding-2026-06-10-0007 Lumen tying to Volt Typhoon associative); Inside Onyxc2 (finding-2026-06-11-0010 BlackFog); + 4 academic papers (ViPER, Sound-of-Malware, MalTree, NetGuard). **NO net-new actor attribution to roster-tracked actor. NO net-new CVE-with-active-exploitation substrate. NO new IOC class.** **DISCARDED — retrospective recap only.** Shai-Hulud / Miasma / IronWorm carry-forward as anti-noise-held npm-worm family per orchestrator binding (operator-deferred /new-actor decision; carried in morning brief).

- **"Security Affairs newsletter Round 581 by Pierluigi Paganini – INTERNATIONAL EDITION"** by Pierluigi Paganini (2026-06-14T13:03:56 UTC = 09:03 EDT just inside window). Weekly newsletter listing 25+ already-covered stories: Fable 5 / Mythos 5 Anthropic (finding-2026-06-13-0001); CISA KEV PeopleSoft (finding-2026-06-13-0002 + 0006); Handala Cal Water (finding-2026-06-13-0003); OnyxC2 (finding-2026-06-11-0010); Chaotic Eclipse YellowKey + RoguePlanet (VT-013, VT-011 already-tracked); Fortinet FortiSandbox new critical (potentially worth grader attention if not already covered); JDY KV-takedown + military-network targeting (finding-2026-06-10-0007 carry); 21,786 home cameras no-password (consumer-class, not A&D); CVE-2026-10520 Ivanti Sentry (finding-2026-06-11-0005 anti-noise-held tonight EOB clock); Russian APTs still exploiting CVE-2025-8088 WinRAR (potentially worth grader attention if not already covered — old CVE but Russian APT continued use); CISA KEV Cisco Catalyst SD-WAN + Arista EOS + Chromium V8 (cluster of 06-09 KEV adds already covered); Chaotic Eclipse RoguePlanet fully-patched-Windows (VT-011); AI Worms research demonstration (academic / not actor); France Tchap government-messaging breach (06-12 PM Other Signal); Microsoft Record-Breaking Patch Tuesday 208 CVEs (06-10 PM); Veeam Critical RCE low-priv backup-server takeover (already in 06-12 PM substrate); Miasma Worm 73 Microsoft GitHub repos (Shai-Hulud anti-noise carry); Chrome 5th 2026 zero-day (06-09 PM); CISA KEV LiteLLM + Check Point Security Gateway (06-08 finding cluster); CVE-2026-23111 Linux nf_tables (06-10 PM); Meta-NSO injunction; Everest Forms Pro plugin (consumer/SMB WordPress, not A&D); UNC3753 Vishing-to-Physical-Intrusion at US Legal & Financial (Mandiant "Seeking Counsel" campaign — Mandiant primary direct on direct-HTML index since 06-13 PM, operator-deferred); Meta AI Recovery Tool flaw exposing 20k Instagram accounts (06-10 PM); IoT Botnet C0XMO Competitor-Killing (06-12 substrate); DentaQuest ShinyHunters 2.6M (06-12 substrate as continuation of finding-2026-06-10-0012 ShinyHunters PeopleSoft campaign). **NO net-new substrate.** **DISCARDED — retrospective recap only.**

  The Round 581 "International Press" sub-section also references items NOT yet in Archimedes corpus this week: ESET APT Activity Report Q4 2025-Q1 2026 (dated 2026-05-28 per ESET WeLiveSecurity direct-fetch confirmation — out of window, not net-new); OceanLotus: From external espionage to domestic targeting (dated 2026-06-11 per ESET WeLiveSecurity direct-fetch — out of 8h window from 07:30 substrate close, but only 76h prior to this sweep; if not yet seen by grader, worth a single-line flag — OceanLotus is APT32 / SeaLotus, NOT on `_roster.yaml`, Vietnam-attributed cluster, "domestic targeting" framing is potentially TTP-class shift if substantive). Out-of-window per pre-brief scope but flagged here for grader awareness.

### The Register — 1 in-window item (already covered by 12:00 FLASH substrate)

- **"AI is code – and can't be prompted into being smarter"** (2026-06-14T12:30 UTC = 08:30 EDT inside window). Opinion / feature piece on jqwik Anti-AI Java property-testing tool clause + recap of Shai-Hulud JavaScript-worm coverage spanning 2025-09 / 2025-11 / 2026-05 (TeamPCP outsourcing) / 2026 mid-year (copycat / Miasma / IronWorm) cycles. Quotes "Sergeant-Major Williams" (reference to British sitcom). **No new attribution / no new CVE / no new IOC / no A&D mention.** Shai-Hulud carryover restating prior corpus baseline. TeamPCP roster #001 HIGH dossier-pending restated. **Already noted in 12:00 FLASH sentinel substrate.** **DISCARDED — opinion piece with no fresh primary substrate.**

### Ars Technica root feed — 1 in-window item (NOT security)

- **"Did a medieval flying monk spot Halley's comet, twice? It's complicated"** by Jennifer Ouellette (2026-06-14T16:02:53 UTC — actually just-after-window from sweep-start perspective). Science / culture / history content. **Not security-relevant. DISCARDED.**

### All other healthy sources — 0 in-window items after since-filter

- The Hacker News: 0 in window (last_modified Sun 14 Jun 14:42 GMT post-window from sweep-start)
- SecurityWeek: 0 in window (last_modified Sat 13 Jun 15:54 GMT pre-window)
- The Record: 0 in window (5 items total, all pre-window)
- Krebs: 0 in window (last_modified Thu 11 Jun 17:38 GMT pre-window)
- WeLiveSecurity (ESET): 0 in window via RSS; direct-fetch index confirms most recent in-window post would be OceanLotus 2026-06-11 OUT of 8h window
- Unit 42 feedburner: 0 in window (last_modified Fri 12 Jun 22:27 GMT pre-window)
- Microsoft Security Blog (MSTIC parent): 0 in window (last_modified Wed 10 Jun 16:00 GMT pre-window)
- Help Net Security: 0 in window (last_modified Sun 14 Jun 15:33 GMT inside window from feed-server activity but no items in window)
- SANS ISC rssfeed.xml: 0 in window (last_modified Sun 14 Jun 19:29 GMT but no diary items in window)
- CrowdStrike: 10 items in feed, ALL DATELESS marketing / Frost Radar / AI-product framing — same persistent pattern 30+ consecutive sweeps; pulled into "items_after_since_filter:10" by absence of published timestamps; **manual review confirms ALL 10 are dateless marketing not threat-intel research; DISCARDED.**
- CyberScoop: 0 in window (last_modified Sat 13 Jun 18:30 GMT pre-window)
- Cisco Talos blog.talosintelligence.com/rss/: 0 in window
- SentinelLabs: 0 in window (last_modified Sat 13 Jun 00:39 GMT pre-window)
- Rapid7: 20 items in feed, 0 in 8h window
- Bitdefender businessinsights.bitdefender.com/rss.xml: 0 in window (last_modified Wed 10 Jun 19:44 GMT pre-window)
- ZDI thezdi.com/blog (feed format): 0 in window (last_modified absent but 20 items all pre-window)
- DarkReading: 1 dateless future "Name That Toon Contest" event marker (DISCARDED)
- Wired Security Latest: 0 in window
- CISA all.xml Atom: 0 in window (Atom reachable, 30 items, all pre-window — no fresh advisory in window)
- Sophos news.sophos.com/en-us/category/threat-research/feed/: 0 in window (200 OK, 15 items, last_modified Sun 14 Jun 01:51 GMT pre-window — **RECOVERED category-path success; soft-pattern observation, NOT promoted to top-level recovery without operator approval per field-ownership rule**)
- Sophos news.sophos.com/en-us/feed/: not retested (top-level stale-persistent since 2026-05-17; under-24h-skip rule does NOT apply since >=24h since stale_since but category-path success above gives recovery substrate without thrashing the top-level endpoint)
- Proofpoint /us/threat-insight/blog/feed: 404 again (5th consecutive observation since 2026-05-10 first surface, 4 prior + this sweep). **No top-level proofpoint-threat-insight entry exists in source-health; per operator binding NOT promoted to status: stale without operator approval.** Logged here for soft-pattern continuity.

### CISA KEV catalog scan (dateAdded=2026-06-13 OR 2026-06-14): 0 entries

5 most recent KEV adds unchanged from 12:00 sweep + morning brief substrate:
- CVE-2026-35273 Oracle PeopleSoft (added 2026-06-12, dueDate 2026-06-15 ~T-26h to EOD Sunday — anti-noise-held; morning brief explicit "hunt-the-19-IOC-set today" call STILL ACTIVE)
- CVE-2026-10520 Ivanti Sentry (added 2026-06-11, dueDate 2026-06-14 = TODAY EOB ~T-4.5h from this sweep — anti-noise-held; morning brief explicit "T-12h" deadline-tonight call STILL ACTIVE, clock closes in this brief's lifetime)
- CVE-2026-11645 Chrome V8 (added 2026-06-09, dueDate 2026-06-23)
- CVE-2026-7473 Arista EOS (added 2026-06-09, dueDate 2026-06-23)
- CVE-2026-20245 Cisco Catalyst SD-WAN (added 2026-06-09, dueDate 2026-06-23)

**NO net-new KEV adds.** No FCEB-compliance data has landed on either expiring clock (PeopleSoft or Ivanti Sentry).

### Mandiant direct-HTML index (cloud.google.com/blog/topics/threat-intelligence)

Top-10 posts confirmed unchanged from morning brief + 12:00 FLASH substrate:
1. GTIG AI Threat Tracker (Adversaries Leverage AI for Vulnerability Exploitation)
2. ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit (finding-2026-06-13-0002 + 0006 substrate)
3. Seeking Counsel: Ongoing Targeted Campaign Against US Law Firms (UNC3753 vishing-to-physical-intrusion; carry-forward operator-deferred actor-profiler decision, A&D-supplier-ecosystem-adjacent via legal-counsel intermediary risk pathway)
4. Exploitation of KnowledgeDeliver via ViewState Deserialization
5. 2 PhaaS 2 Furious — Evolution of Chinese-Language Phishing Services (parallel-cluster framing vs today's BleepingComputer Outsider Enterprise FBI-takedown story; Mandiant's PhaaS analysis is distinct cluster, NOT same actor as Outsider Enterprise per Mandiant's framing)
6. Welcome to BlackFile: Inside a Vishing Extortion Operation
7. Snow Flurries — UNC6692 Social Engineering Custom Malware Suite (UNC6692 NOT on roster)
8. Defending Your Enterprise When AI Models Can Find Vulnerabilities (deSouza opinion-piece-class)
9. The German Cyber Criminal Überfall
10. vSphere and BRICKSTORM Malware: A Defender's Guide

**None dated in 8h window.** All previously substrate or out-of-window. **Direct-HTML path CONFIRMED working consistently 2026-06-13 PM + 2026-06-14 00:00 + 06:00 + 07:30 + 12:00 + 15:30 — SIXTH consecutive direct-HTML success against RSS-path failure; canonical-swap operator decision still pending after 6 consecutive direct-HTML successes.**

## Splunk first-party sentinel — Hard Rule 8

Indexes queried: `archimedes`, `defenseclaw_local`. Time window: -24h.

Sentinel set (19 IOCs carried forward from 2026-06-13 PM brief commit dc85aae): `azurenetfiles.net`, `176.120.22.24`, staging IPs `142.11.200.186-190` (5 IPs), Windows meshagent filenames `meshagent64-azure-ops.exe` / `meshagent64-v2.exe` / `meshagent32-azure-ops.exe` (3 filenames), Linux + Windows meshagent SHA-256 hashes (5 hashes — elided from this raw-signal body per Hard Rule 7), `.bash_history` reference, `exfil.tar.zst` pipe substrate, `envmetadata/data/environment/` persistence-path substrate, `README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT` defacement marker.

Query executed: `search index=archimedes OR index=defenseclaw_local ("azurenetfiles.net" OR "176.120.22.24" OR "142.11.200.186" OR "142.11.200.187" OR "142.11.200.188" OR "142.11.200.189" OR "142.11.200.190" OR "meshagent64-azure-ops" OR "meshagent64-v2" OR "meshagent32-azure-ops" OR "exfil.tar.zst" OR "envmetadata/data/environment" OR "README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED") earliest=-24h@h latest=now`

**Result: 0 events over -24h on either index.**

This is the **SIXTH consecutive sweep over the 19-IOC set with 0 hits** (18:00 + 00:00 + 06:00 + 07:30 + 12:00 + 15:30). Pattern fully established; sentinel set remains valid carry-forward. Frank is not a higher-ed environment consistent with UNC6240's 68% higher-ed victim concentration per Mandiant — silent Splunk does NOT disconfirm. Visibility-limited absence, NOT confirmed-negative.

## Source-health deltas observed this sweep (runtime fields only)

- **mandiant:** feedburner RSS 404 again — per under-24h-since-stale rule (stale_since=2026-06-13, ~37h ago at this sweep), the >=24h retry IS eligible. failure_count advanced 27 → 28. Direct-HTML retrieval path SUCCEEDED again (6th consecutive direct-HTML success). Operator-flagged canonical-swap decision still pending per morning brief substrate — NOT swapped this sweep per operator binding.
- **sans-isc:** rssfeed.xml reachable + parseable (last_modified 19:29 GMT inside window from feed-server activity). No diary items in window — Sunday cadence. No state change.
- **cisco-talos:** blog.talosintelligence.com/rss/ reachable (200 OK + ETag); 15 items in feed, 0 in window. No state change.
- **sophos:** **category-path RECOVERY observed** — `news.sophos.com/en-us/category/threat-research/feed/` returned 200 OK with 15 items, last_modified Sun 14 Jun 01:51 GMT. The top-level `news.sophos.com/en-us/feed/` remains stale-persistent (last_error 2026-05-17, failure_count 3); category-path recovery is a SOFT observation worth flagging to operator for endpoint-swap consideration. **NOT swapped this sweep per field-ownership / operator-decision rule.** Top-level stale status preserved; runtime fields on top-level entry unchanged.
- **proofpoint:** `/us/threat-insight/blog/feed` 404 again (5th consecutive observation). **No top-level proofpoint-threat-insight entry exists in source-health.yaml — soft-pattern continuity, NOT promoted to status:stale without operator approval per morning brief substrate carry-forward.** Logged in this raw-signal body for audit-trail purposes only.
- **lumen:** not retested this sweep (failure_count=1 from 2026-06-12 12:00 FLASH XML parse error; multi-day cadence; held healthy below stale threshold).
- **shadowserver:** not retested this sweep (failure_count=1 from 2026-06-12 12:00 FLASH 404; relay-tier already-productive coverage via BleepingComputer / SecurityWeek; held healthy).
- All other healthy sources reachable with 0 in-window items beyond what's noted above. No new degradations.

## Disposition / handoff

**1 substantive raw-signal written** for grader: BleepingComputer FBI / Google / Black Lotus Labs Outsider Enterprise operational-takedown article (UPDATE-on-finding-2026-06-12-0006 candidate; operational layer on top of prior civil-suit substrate). Filename: `raw-2026-06-14-pm-001-bleepingcomputer-fbi-google-blacklotuslabs-outsider-enterprise-takedown-update-on-finding-2026-06-12-0006.md`.

**Anti-noise carry-forward bindings preserved per orchestrator instruction** (none re-litigated as net-new this sweep; SA Round 581 + Round 101 newsletter recaps cleanly resolve to anti-noise carry):
- PeopleSoft / UNC6240 / CVE-2026-35273 — KEV clock ~T-26h to EOD Sunday 2026-06-15; no FCEB-compliance data landed in this 8h window; morning brief "hunt the 19-IOC set today" call sustained, Splunk sentinel zero hits 6/6 sweeps
- Ivanti Sentry CVE-2026-10520 — KEV clock ~T-4.5h to EOD TODAY 2026-06-14; afternoon brief will close in clock's lifetime; carries forward unchanged
- CVE-2026-20253 Splunk Enterprise — finding-2026-06-13-0004 carry unchanged
- NPM 12 default script-execution change — finding-2026-06-13-0005 carry; GitHub direct blog retrieval still pending
- Velvet Ant Operation Highland — Sygnia primary still pending
- Handala #014 / Cal Water — finding-2026-06-13-0003 carry; Hard Rule 2 binding preserved; OT/ICS impact NOT confirmed (RTKBase = GPS-correction not SCADA)
- Fable 5 / Mythos 5 Anthropic — finding-2026-06-13-0001 three-publisher carry
- Check Point VPN CVE-2026-50751 / Qilin — sustained hold, no net-new substrate
- Shai-Hulud / Miasma / IronWorm npm-worm family — carry as operator-deferred /new-actor decision; today's SA Malware Newsletter Round 101 reinforces 3+ relay surfaces over 24h pattern but no fresh primary substrate
- UNC3753 vishing-to-physical-intrusion / Mandiant "Seeking Counsel" — Mandiant direct-HTML carry-forward to actor-profiler /new-actor decision; SA Round 581 International Press section confirms it as 06-08 → present campaign visibility
- Lytvynenko / Conti DOJ plea — already covered as Other Signal in morning brief; not re-raised

**Items worth flagging to grader for afternoon brief composition** (trigger-NEGATIVE but noted):
1. **BleepingComputer FBI Outsider Enterprise takedown** (`raw-2026-06-14-pm-001`) — UPDATE-on-finding-2026-06-12-0006 candidate. FBI + Google + Black Lotus Labs joint coordinated takedown. Operational-disruption layer on Google's prior civil-suit substrate. Worth grader evaluation for 1-2 line UPDATE bullet in afternoon brief if not anti-noise-deferred.
2. **Ivanti Sentry CVE-2026-10520 KEV deadline closing tonight EOB** — grader should surface as "deadline closing in this brief's lifetime" reminder per morning brief substrate; no FCEB-compliance data landed.
3. **PeopleSoft / UNC6240 KEV deadline T-26h Sunday EOB** — grader should surface as "still in clock, Splunk sentinel 6/6 zero hits visibility-limited" reminder per morning brief substrate.
4. **Mandiant canonical-swap operator decision** — 6 consecutive direct-HTML successes against RSS-path failure; recommend operator-side endpoint canonical-swap before next pre-brief cycle.
5. **Sophos category-path recovery soft-observation** — `news.sophos.com/en-us/category/threat-research/feed/` working today; operator could consider endpoint swap on top-level sophos entry pending operator decision.

**Items worth flagging to grader as potentially-fresh-out-of-window** (operator awareness, NOT raw-signaled this sweep per pre-brief scope discipline):
- ESET WeLiveSecurity "OceanLotus: From external espionage to domestic targeting" dated 2026-06-11 (~76h before window start, OUT of pre-brief 8h scope; ESET A-grade primary; APT32 / SeaLotus / OceanLotus NOT on `_roster.yaml`; "domestic targeting" framing potentially TTP-class shift if substantive). Listed in SA Round 581 International Press section. Worth grader awareness if afternoon brief has substrate gap.
- ESET WeLiveSecurity "ESET APT Activity Report Q4 2025-Q1 2026" dated 2026-05-28 (~17 days before window, OUT of pre-brief 14d-lookback; major quarterly APT roundup; listed in SA Round 581). Worth operator awareness for /update-tracking cycle on roster-tracked actors but NOT a raw-signal candidate this sweep.
- "Russian APTs Still Exploiting Patched WinRAR Flaw CVE-2025-8088" (per SA Round 581 line item; would correspond to an SA-internal article not directly retrieved this sweep). CVE-2025-8088 WinRAR is old, but continued Russian-APT use is a sustained-campaign-class signal. Worth grader awareness if afternoon brief composition surfaces gap.

## Extraction notes

- Language: en
- Article type: sentinel (internal pre-brief substrate audit)
- Raw IOC extraction invoked: no (sentinel file; the one substantive raw-signal `raw-2026-06-14-pm-001` carries its own IOC-extraction block)
- Hard Rule binding: Rule 1 (LEGAL-POLICY) — all queries passive RSS / WebFetch / Splunk-self; no active recon of any target outside `authorized-targets.yaml` (which is empty). Rule 2 (no attribution origination) — no novel attributions made this sweep; FBI / Google attribution language on Outsider Enterprise preserved verbatim per source. Rule 3 (no exploitation assistance) — no PoC content or exploit walkthroughs ingested into raw-signal. Rule 7 (15-word quote discipline) — no verbatim quotes >15 words preserved in this sentinel. Rule 8 (Splunk first-party) — sentinel Splunk scan emitted with 19-IOC carry-forward set, 0 events on -24h.
- Operator-invocation context: scheduled 15:30 EDT pre-brief collection for 16:00 EDT afternoon brief. COLLECTION ONLY per operator binding — no grading, no FLASH evaluation, no brief composition, no Discord posting, no commit, no `_coverage-log.yaml` update.
