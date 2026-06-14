---
raw_id: raw-2026-06-14-flash-1200-000
collected_at: 2026-06-14T12:05:00-04:00
run_id: flash-sweep-20260614-120000
collection_mode: flash_sweep
source:
  source_yaml_id: sentinel-internal
  source_name: "FLASH sweep sentinel (internal)"
  source_url: null
  published_at: 2026-06-14T12:05:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [flash_sweep_clean, source_health_delta_observed, ad_hoc_operator_invocation]
triage_tags: [non_flash, sentinel, sweep_clean, ad_hoc]
iocs_extracted: false
iocs_count: 0
text_word_count: 1180
promoted: false
ttl_expires_at: 2026-09-12T12:05:00-04:00
---

# FLASH sweep 2026-06-14 12:00 EDT — clean sweep, 0 candidates, 0 triggers (ad-hoc operator invocation)

## Sweep parameters

- Mode: `flash_sweep` (ad-hoc operator invocation; not on standard 00:00/06:00/12:00/18:00 cadence position but coincident with the 12:00 EDT FLASH-window slot)
- Time window: 2026-06-14T07:30:00-04:00 → 2026-06-14T12:05:00-04:00 (~4.5h since 07:30 pre-brief substrate which fed the 08:00 morning brief). Effective collection window therefore opens at the end of the morning brief's pre-brief collection, NOT at 06:00 sweep close — to prevent re-litigating substrate already consumed by the 08:00 brief.
- **Active hours** per FLASH-POLICY §Quiet Hours (09:00–21:00 EDT) — any FLASH would post immediately to `#flash-alerts`, NOT queue. Critical override (CVSS 10.0 + active exploit + tracked actor + A&D entity named) NOT met today.
- Sources queried: 15 healthy primary RSS feeds + KEV JSON + Mandiant direct-HTML index + Splunk first-party sentinel.
- Sources skipped (stale, <24h since stale_since per under-24h rule): volexity, msrc, lumen, shadowserver, sophos, industrialcyber-co, ars-security, trellix, x-cisagov, x-gossithedog, censys, urlscan, hibp.
- Sources skipped (stale, retried per >=24h rule): mandiant feedburner (retried, still 404 — 27th consecutive observation per morning brief substrate; direct-HTML path remains the productive endpoint).

## Items in window (since 07:30 pre-brief consumed substrate)

- **BleepingComputer:** 1 item in window — "FBI disrupts massive AI-powered phishing service using a million URLs" (2026-06-14T14:36:23 UTC = 10:36 EDT inside window). FBI + Google + Black Lotus Labs coordinated takedown of "Outsider Enterprise" Chinese-based PhaaS coordinating via Telegram, operational since at least 2023, "hundreds of thousands of users worldwide" impacted, SMS smishing channels via AT&T / T-Mobile / Verizon. **No A&D / no DIB / no aerospace / no defense sector mention.** **No new CVE.** **No IOCs in article.** **Outsider Enterprise NOT on `_roster.yaml`** (already evaluated 06-12 PM as not-on-roster cybercriminal cluster). **Already covered substrate** — finding-2026-06-12-0006 captured the Google civil-suit + Gemini AI weaponization layer of this same actor cluster two days ago. Today's BleepingComputer item is a follow-up cycle on FBI's operational takedown component of the same campaign, NOT a fresh attribution to a roster-tracked actor and NOT a new TTP class. **UPDATE-on-finding-2026-06-12-0006 candidate for afternoon brief grader**, NOT FLASH. Anti-noise Rule 1 (one FLASH per trigger topic per 24h) applies — Outsider Enterprise was the 06-12 PM brief topic, less than 48h ago. **DISCARDED for FLASH purposes per Mode 1 procedure + anti-noise carry.**
- **The Hacker News:** 0 items in 4.5h window after since-filter (50 items in feed total, all pre-window per last_modified Sun 14 Jun 2026 14:42 GMT).
- **SecurityWeek:** 0 items in 4.5h window after since-filter (10 items in feed total, last_modified Sat 13 Jun 2026 15:54 GMT pre-window).
- **SecurityAffairs:** 2 items in window — both retrospective newsletter roundups (no net-new substrate, no fresh in-window primary reporting):
  - **"Security Affairs Newsletter Round 581 by Pierluigi Paganini – International Edition"** (2026-06-14T13:03:56 UTC = 09:03 EDT just inside window). Weekly roundup listing 25+ stories ALL ALREADY covered in prior briefs (Fable 5 / Mythos 5 Anthropic — finding-2026-06-13-0001; CISA KEV PeopleSoft — finding-2026-06-13-0002 + 0006; Handala Cal Water — finding-2026-06-13-0003; ShinyHunters / PeopleSoft / Mandiant — finding-2026-06-13-0006; CISA KEV Cisco SD-WAN / Arista EOS / Chromium V8 — finding cluster 06-09 + 06-10; Ivanti Sentry CVE-2026-10520 — finding-2026-06-11-0005; WinRAR CVE-2025-8088 carryover; Microsoft Patch Tuesday — 06-10 PM; Tchap French-gov breach — 06-12 PM Other Signal; OnyxC2 — finding-2026-06-11-0010; Veeam Critical RCE — already in 06-12 PM; Miasma Worm + 73 Microsoft GitHub repos — Shai-Hulud carry-forward already noted in 06-13 PM brief; Google Chrome zero-day CVE-2026-11645 — 06-09 PM; LiteLLM CVE-2026-42271 KEV — finding cluster; CVE-2026-23111 Linux nf_tables — already in 06-10 PM; Meta NSO injunction; Everest Forms; UNC3753 vishing-to-physical-intrusion — already named on Mandiant direct-HTML index since 06-13 PM as "Seeking Counsel" campaign covered by Mandiant primary direct, deferred to vuln-tracker / actor-profiler handoff; Meta AI 20k Instagram — 06-10 PM; C0XMO IoT botnet — 06-12 PM substrate; DentaQuest ShinyHunters 2.6M — already noted in 06-12 substrate as continuation of finding-2026-06-10-0012 ShinyHunters self-attested PeopleSoft campaign). **NO net-new substrate.** **DISCARDED — retrospective recap only.**
  - **"Security Affairs Malware Newsletter Round 101"** (2026-06-14T13:23:29 UTC = 09:23 EDT just inside window). Weekly malware research roundup listing 15 items: IronWorm (Shai-Hulud rustier cousin; Shai-Hulud was carried 06-13 PM brief as roster-gap candidate operator-deferred /new-actor decision); Trojanized ai-sdk-ollama / Miasma npm worm via binding.gyp (Shai-Hulud-family lineage); Gafgyt C0XMO IoT-botnet variant (already finding-2026-06-12 + 06-12 PM substrate); REMnux + AI Agents methodology (academic); Miasma worm path-of-destruction (Shai-Hulud-family); Miasma + PyPI wave (Shai-Hulud-family); VerdantBamboo / BRICKSTORM-in-the-firewall (Mandiant BRICKSTORM was top-of-direct-HTML on 2026-05-09 sweep, Defender's Guide on Mandiant index since 06-13); NFCShare Android trojan; 400+ AUR packages compromised (already finding-2026-06-12-0005 Sonatype "Atomic Arch"); JDY IoT/SOHO botnet expansion (already finding-2026-06-10-0007 Lumen tying to Volt Typhoon associative); OnyxC2 stealer / 210 apps (already finding-2026-06-11-0010 BlackFog); plus 4 academic papers (ViPER, Sound-of-Malware, MalTree, NetGuard). **NO net-new actor attribution to roster-tracked actor. NO net-new CVE-with-active-exploitation substrate.** **DISCARDED — retrospective + academic recap only.**
- **The Record:** 0 items in 4.5h window after since-filter (5 items in feed, all pre-window).
- **Krebs:** 0 items in 4.5h window after since-filter (last_modified Thu 11 Jun 2026 17:38 GMT pre-window).
- **CISA all.xml:** 0 items in 4.5h window after since-filter (Atom reachable, 30 items in feed, all pre-window — no fresh ICS / advisory in window).
- **SANS ISC rssfeed.xml:** 0 items in 4.5h window after since-filter (10 items in feed, last_modified Sun 14 Jun 2026 15:59 GMT inside window from feed-server activity but no diary items in window; most recent diary 2026-06-10 — quiet weekend cadence consistent with normal SANS pattern).
- **The Register security:** 1 item in window — "AI is code – and can't be prompted into being smarter" (2026-06-14T12:30 UTC = 08:30 EDT inside window). Opinion/feature piece on jqwik anti-AI Java property-testing tool clause + recap of Shai-Hulud JavaScript worm coverage. Quotes Sergeant-Major Williams. **No new attribution / no new CVE / no new IOC / no A&D mention.** Shai-Hulud carryover only (NOT on roster, operator-deferred /new-actor decision, already named in 06-13 PM brief and 06-14 morning brief). TeamPCP reference is restatement of prior corpus baseline (roster #001 HIGH, dossier pending). **DISCARDED — opinion piece with no fresh primary substrate.**
- **DarkReading:** 1 dateless "Name That Toon Contest" event marketing item (updated 2026-06-26 future-event marker). **DISCARDED.**
- **Unit 42 feedburner:** 0 items in 4.5h window after since-filter (15 items in feed, last_modified Fri 12 Jun 2026 22:27 GMT pre-window).
- **Microsoft Security Blog (MSTIC parent):** 0 items in 4.5h window after since-filter (10 items in feed, last_modified Wed 10 Jun 2026 16:00 GMT pre-window).
- **Help Net Security:** 0 items in 4.5h window after since-filter (10 items in feed, last_modified Sun 14 Jun 2026 15:33 GMT inside window from feed-server activity but no items in window — Week-in-Review already consumed by 06:00 + 07:30 sweeps).
- **ESET WeLiveSecurity:** 0 items in 4.5h window after since-filter (100 items in feed, none in window).
- **CyberScoop:** 0 items in 4.5h window after since-filter (10 items in feed, last_modified Sat 13 Jun 2026 18:30 GMT pre-window).
- **Cisco Talos blog.talosintelligence.com/rss/:** 0 items in 4.5h window after since-filter (15 items in feed, last_modified header missing but feed reachable). Soft-pattern note: this is the `/rss/` endpoint that RECOVERED on 2026-06-14 07:30 pre-brief after one-time 404 on the deprecated `/feeds/posts/default` path; rssfeed endpoint stable this sweep.
- **Mandiant cloud.google.com/blog/topics/threat-intelligence direct-HTML index:** Top-8 posts unchanged from 06:00 sweep + morning-brief substrate — GTIG AI Threat Tracker, ShinyHunters/PeopleSoft (covered finding-2026-06-13-0002+0006), Seeking Counsel US law firms campaign (Mandiant primary direct, deferred — corresponds to UNC3753 in SA newsletter recap), KnowledgeDeliver ViewState exploit, 2 PhaaS 2 Furious Chinese-language phishing-services (parallel surface to today's BleepingComputer Outsider Enterprise FBI takedown story but Mandiant's analysis is distinct cluster), BlackFile vishing extortion operation, UNC6692 Snow Flurries social-engineering campaign (UNC6692 not on roster), Defending Your Enterprise AI Vulnerabilities (deSouza). None dated in the 4.5h window; all out-of-window or already-substrate. Direct-HTML path CONFIRMED working consistently 2026-06-13 PM + 2026-06-14 00:00 + 06:00 + 07:30 + 12:00 — fifth consecutive direct-HTML success against RSS-path failure; canonical-swap operator decision still pending.
- **CISA KEV catalog scan** (dateAdded=2026-06-13 OR 2026-06-14): 0 entries. Five most recent KEV adds unchanged from 06:00 sweep: CVE-2026-35273 Oracle PeopleSoft (2026-06-12, dueDate 2026-06-15 ~T-32h to EOD Sunday — anti-noise-held), CVE-2026-10520 Ivanti Sentry (2026-06-11, dueDate 2026-06-14 = today EOB ~T-8h from this sweep — anti-noise-held), CVE-2026-11645 Chrome V8 (2026-06-09, dueDate 2026-06-23), CVE-2026-7473 Arista EOS (2026-06-09), CVE-2026-20245 Cisco Catalyst SD-WAN (2026-06-09). **NO net-new KEV adds.** **Trigger 1 NEGATIVE.**

## FLASH trigger evaluation

All 6 triggers evaluated against the in-window content (BleepingComputer FBI Outsider Enterprise takedown, SA Newsletter Round 581 + Round 101 retrospectives, The Register AI opinion piece) and against the standing anti-noise list. **0 triggers matched.**

- **Trigger 1 (critical CVE actively exploited):** NEGATIVE. KEV unchanged. No new A-grade source claims on a CVSS >=9.0 vuln with active exploitation in the 4.5h window.
- **Trigger 2 (new attribution for tracked actor):** NEGATIVE. BleepingComputer Outsider Enterprise item is FBI takedown follow-up on already-covered actor cluster (Outsider Enterprise NOT on roster); no new attribution to a roster-tracked actor. SA newsletter recap items all restate prior attributions.
- **Trigger 3 (first-party IOC hit):** NEGATIVE. Splunk -24h scan on UNC6240 19-IOC sentinel set returned 0 events on both `archimedes` and `defenseclaw_local` indexes.
- **Trigger 4 (tracked actor TTP change):** NEGATIVE. No new TTP-class substrate from A/B-grade source on a roster actor. Shai-Hulud / Miasma / IronWorm npm-worm references in SA Malware Newsletter Round 101 are summaries of prior research; Shai-Hulud actor NOT on roster (operator-deferred /new-actor decision); TeamPCP (roster #001 HIGH, dossier pending) restated but no new tooling / targeting / infra class documented.
- **Trigger 5 (active A&D-sector campaign):** NEGATIVE. No new active multi-victim campaign vs A&D / watchlist entity in window. FBI Outsider Enterprise takedown explicitly carries "no specific named victims or sectors" per source extraction; smishing campaign impacted consumer carriers, not A&D primes.
- **Trigger 6 (zero-day without patch):** NEGATIVE. No new zero-day disclosure in window.

## Anti-noise holds (per orchestrator binding + Doctrine §134-145)

The following topics are anti-noise-held; their absence from this sweep's trigger output is intentional, NOT a re-evaluation:

- PeopleSoft / UNC6240 / CVE-2026-35273 (finding-2026-06-13-0006 + 0002; BOD 26-04 deadline 2026-06-15 EOB ~T-32h from this sweep — clock STILL ACTIVE, the morning brief's "hunt the 19-IOC set today" call stands; advance to UPDATE only if FCEB-compliance data lands)
- CVE-2026-20253 Splunk Enterprise (finding-2026-06-13-0004)
- NPM 12 default script-execution change (finding-2026-06-13-0005)
- Fable 5 / Mythos 5 USG export-control on Anthropic (finding-2026-06-13-0001 + SA newsletter recap)
- Handala / Cal Water single-Dataminr-substrate (finding-2026-06-13-0003 + SA newsletter recap)
- Velvet Ant Operation Highland (covered 06-12 PM)
- Ivanti Sentry CVE-2026-10520 (finding-2026-06-11-0005; KEV deadline 2026-06-14 EOB ~T-8h from this sweep — clock CLOSES TONIGHT, morning brief explicit call stands)
- Check Point VPN CVE-2026-50751 + Qilin (finding-2026-06-10-flash-0000-002)
- Outsider Enterprise PhaaS (finding-2026-06-12-0006 Google civil suit; today's BleepingComputer FBI-takedown follow-up is UPDATE-candidate for afternoon brief grader, NOT FLASH)
- Shai-Hulud npm-worm family / Miasma / IronWorm (06-13 PM brief; NOT on roster, operator-deferred /new-actor decision, restated in 06-14 morning brief)
- UNC3753 vishing-to-physical-intrusion / Mandiant Seeking Counsel campaign (Mandiant direct-HTML since 06-13 PM, deferred to actor-profiler /new-actor decision)

## Splunk first-party sentinel — Hard Rule 8 + Trigger 3

Indexes queried: `archimedes`, `defenseclaw_local`. Time window: -24h.

Sentinel set (19 IOCs carried forward from 2026-06-13 PM brief commit dc85aae): `azurenetfiles.net`, `176.120.22.24`, staging IPs `142.11.200.186-190` (5 IPs), Windows meshagent filenames `meshagent64-azure-ops.exe` / `meshagent64-v2.exe` / `meshagent32-azure-ops.exe` (3 filenames), Linux meshagent SHA-256 + 4 Windows meshagent SHA-256 hashes (5 hashes — note: hashes elided from this raw-signal body per Hard Rule 7 quote-discipline; full hash set is in 2026-06-13 PM brief substrate), `.bash_history` reference, `exfil.tar.zst` pipe substrate, `envmetadata/data/environment/` persistence-path substrate, `README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT` defacement marker.

Query executed: `index=archimedes OR index=defenseclaw_local (azurenetfiles.net OR "176.120.22.24" OR "142.11.200.186" OR "142.11.200.187" OR "142.11.200.188" OR "142.11.200.189" OR "142.11.200.190" OR "meshagent64-azure-ops" OR "meshagent64-v2" OR "meshagent32-azure-ops" OR "exfil.tar.zst" OR "envmetadata/data/environment" OR "README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED") earliest=-24h@h latest=now`

**Result: 0 events over -24h on either index.** Frank is not a higher-ed environment consistent with UNC6240's 68% higher-ed victim concentration — silent Splunk does NOT disconfirm at this substrate. Visibility-limited absence, NOT confirmed-negative.

This is the FIFTH consecutive sweep over the 19-IOC set with 0 hits (18:00 + 00:00 + 06:00 + 07:30 + 12:00). Pattern fully established; sentinel set remains valid carry-forward.

## Source-health deltas observed this sweep

- **mandiant:** feedburner.com/Mandiant returned 404 again (28th consecutive failure observation if we count this sweep; 27 was the morning brief's substrate count from the 07:30 pre-brief — this sweep would advance to 28 OR remain at 27 depending on whether the failure-count rule treats <6h re-attempts as a single observation per the under-24h-skip pattern in the schema). Per the §"After fetching" rule "if `status: stale` AND `stale_since < 24h` → skip (don't thrash failing APIs)", this 12:00 sweep should NOT have attempted the Mandiant RSS since `stale_since: 2026-06-13` is less than 24h ago — so I should NOT advance the counter. Net result: `last_attempt` is the only field that should advance (to this sweep's timestamp); `failure_count` and `status` unchanged. Direct-HTML retrieval path SUCCEEDED again this sweep (top-8 posts visible, all out-of-window or already-substrate) — operator-note candidate "Direct-HTML path working consistently 2026-06-13 PM + 2026-06-14 00:00 + 06:00 + 07:30 + 12:00" carries forward; canonical-swap decision still pending operator after 5 consecutive direct-HTML successes against RSS-path failure.
- **sans-isc:** rssfeed.xml reachable + parseable (last_modified inside window from feed-server activity). No diary items in window — quiet weekend cadence consistent with normal SANS pattern. No change.
- **cisco-talos:** blog.talosintelligence.com/rss/ reachable (recovered endpoint from 06:00 sweep after one-time 404 on `/feeds/posts/default`); 15 items in feed, 0 in window. No change.
- **proofpoint:** not queried this sweep (still no top-level source-health entry exists for proofpoint — 4 prior consecutive 404 observations on `/us/threat-insight/blog/feed` remain operator-flag candidates; no top-level entry to flip yet, no change).
- All other healthy sources reachable with 0 in-window items. No new degradations beyond Mandiant `last_attempt` advance.

## Disposition

0 FLASH candidates. 0 triggers matched. Per FLASH-POLICY anti-noise rule 1, the orchestrator exits silently for FLASH posting purposes. Net-new content for grader attention this window: **none new**.

The four in-window items (BleepingComputer FBI Outsider Enterprise takedown, SA Newsletter Round 581, SA Malware Newsletter Round 101, The Register AI opinion piece) are logged in this sentinel file's "Items in window" section for audit-trail purposes and are NOT FLASH-candidates (anti-noise applies; UPDATE-class material at best).

Items worth flagging to the orchestrator as trigger-NEGATIVE-but-noted for the 15:30 afternoon pre-brief / 16:00 afternoon brief:

- **BleepingComputer FBI Outsider Enterprise takedown** — UPDATE-on-finding-2026-06-12-0006 candidate. FBI + Google + Black Lotus Labs primary-A-grade-DOJ-cite available. Adds operational-takedown detail to the prior civil-suit substrate. Worth a 1-2 line UPDATE bullet in afternoon brief if grader picks it up; NOT a fresh finding.
- **Mandiant "Seeking Counsel" US law firms campaign** — visible on Mandiant direct-HTML index since 06-13 PM, parallel-cluster to BleepingComputer's Outsider Enterprise Chinese-language smishing PhaaS surface (per SA newsletter recap correlating to UNC3753 vishing-to-physical-intrusion). Mandiant primary direct retrieval recommended for the afternoon grader if relevant to A&D supplier-ecosystem (legal-firm intermediary risk pathway).
- **BOD 26-04 PeopleSoft deadline 2026-06-15 EOB ~T-32h** — clock still active, anti-noise-held; grader may surface as "still in clock" reminder if no FCEB-compliance data lands in 15:30 pre-brief window.
- **Ivanti Sentry CVE-2026-10520 KEV deadline 2026-06-14 EOB ~T-8h from this sweep** — clock closes TONIGHT EOB; grader should surface as "deadline-tonight" reminder regardless of additional substrate (the morning brief already explicit-called this; afternoon brief can sustain or close).
- **Mandiant canonical-swap operator decision** — 5 consecutive direct-HTML successes against RSS-path failure; recommend operator flip canonical Mandiant fetch path before next pre-brief cycle.

## Extraction notes

- Language: en
- Article type: sentinel (internal)
- Raw IOC extraction invoked: no (no candidate items)
- Hard Rule binding: Rule 1 (LEGAL-POLICY) — all queries passive RSS/WebFetch/Splunk-self; Rule 2 (no attribution origination) — no novel attributions made this sweep; Rule 7 (15-word quote discipline) — no verbatim quotes >15 words preserved in this sentinel; Rule 8 (Splunk first-party) — sentinel Splunk scan emitted with 19-IOC carry-forward set.
- Operator-invocation context: ad-hoc FLASH sweep at 12:05 EDT, slotted into the standard 12:00 EDT FLASH cadence position; sweep window opens at 07:30 pre-brief substrate close to prevent re-litigation of morning-brief consumed content.
