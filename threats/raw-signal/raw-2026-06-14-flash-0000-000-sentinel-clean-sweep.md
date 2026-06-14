---
raw_id: raw-2026-06-14-flash-0000-000
collected_at: 2026-06-14T00:02:30-04:00
run_id: flash-sweep-20260614-000000
collection_mode: flash_sweep
source:
  source_yaml_id: sentinel-internal
  source_name: "FLASH sweep sentinel (internal)"
  source_url: null
  published_at: 2026-06-14T00:02:30-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [flash_sweep_clean, quiet_hours_active, source_health_delta_observed]
triage_tags: [non_flash, sentinel, sweep_clean, quiet_hours]
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: false
ttl_expires_at: 2026-09-12T00:02:30-04:00
---

# FLASH sweep 2026-06-14 00:00 EDT — clean sweep, 0 candidates, 0 triggers (quiet hours active)

## Sweep parameters

- Mode: `flash_sweep`
- Time window: 2026-06-13T18:01:30-04:00 → 2026-06-14T00:02:30-04:00 (~6h since previous 18:00 sentinel; PM brief commit dc85aae shipped 16:00 EDT)
- Quiet hours: **ACTIVE** (00:00 EDT falls within 21:00–09:00 EDT window per FLASH-POLICY §52). Any triggers would queue for 09:00 catchup sweep per `infrastructure/flash-queue.yaml`, not post live. Triggers were evaluated normally per orchestrator directive; quiet-hours gating is downstream briefer/librarian concern.
- Sources queried (FLASH-POLICY standard set, ~17 reachable): BleepingComputer, THN, SecurityAffairs, SecurityWeek, Krebs, The Record, MSTIC, Unit42, CISA all.xml, CISA KEV JSON, NVD lastModified critical window, DarkReading, The Register, Sygnia, DFIR Report, Check Point Research, Talos, WeLiveSecurity, SentinelLabs, Cybereason, plus Mandiant direct-HTML listing page.
- Sources skipped (stale-persistent, <24h since stale_since per under-24h rule from doctrine): volexity, msrc, lumen, shadowserver, sophos, industrialcyber-co, ars-security, trellix, x-cisagov, x-gossithedog, censys, urlscan, hibp.
- Mandiant feedburner: 404 again this sweep (counter increment noted below) — direct-HTML listing path used as workaround per PM brief commit dc85aae operator-note.
- SANS ISC RSS feed: parse error returned ("syntax error" at line 2 col 0) — soft observation, single-sweep occurrence, no health update applied. Re-check next sweep.

## Items in window

- **BleepingComputer:** 0 items after since-filter (15 in feed, none ≥ 2026-06-13T22:01:30Z UTC cutoff).
- **The Hacker News:** 0 items after since-filter (50 in feed).
- **Security Affairs:** 0 items after since-filter (10 in feed; feed last-modified 2026-06-13T14:32:11Z — pre-window).
- **SecurityWeek:** 0 items after since-filter (10 in feed; feed last-modified 2026-06-13T15:54:25Z — pre-window).
- **Krebs:** 0 items after since-filter (10 in feed; feed last-modified 2026-06-11 — well pre-window).
- **The Record:** 0 items after since-filter (5 in feed).
- **MSTIC:** 0 items after since-filter (10 in feed; feed last-modified 2026-06-10 — pre-window).
- **Unit 42:** 0 items after since-filter (15 in feed; feed last-modified 2026-06-12T22:00:14Z — pre-window).
- **CISA all.xml:** 0 items after since-filter (30 in feed).
- **DarkReading:** 1 dateless "Name That Toon Contest" promotional item — DISCARDED (no actor/CVE/watchlist/IOC).
- **The Register:** 0 items after since-filter (50 in feed).
- **Sygnia:** 0 items after since-filter (9 in feed; feed last-modified 2026-06-11T15:06:32Z — pre-window).
- **DFIR Report:** 0 items after since-filter.
- **Check Point Research:** 0 items after since-filter (15 in feed; feed last-modified 2026-06-11T13:47:47Z — pre-window).
- **Talos:** 0 items after since-filter (15 in feed).
- **WeLiveSecurity:** 0 items after since-filter (100 in feed).
- **SentinelLabs:** 0 items after since-filter (10 in feed; feed last-modified 2026-06-13T00:39:35Z — pre-window).
- **Cybereason:** 0 items after since-filter (10 in feed; feed last-modified 2026-06-10T17:24:59Z — pre-window).
- **Mandiant direct-HTML listing page:** Top-8 posts visible match yesterday's PM brief substrate (UNC6240/ShinyHunters PeopleSoft is most-recent, already covered by finding-2026-06-13-0002 + finding-2026-06-13-0006). No net-new posts in window.
- **CISA KEV JSON catalog scan** (dateAdded=2026-06-13 or 2026-06-14): 0 entries. Most recent KEV add remains CVE-2026-35273 (Oracle PeopleSoft) dateAdded 2026-06-12 — already finding-2026-06-13-0002 / finding-2026-06-13-0006 substrate.
- **NVD lastModStartDate window query** (2026-06-13T22:00:00Z → 2026-06-14T04:00:00Z UTC, cvssV3Severity=CRITICAL): 0 results.

## FLASH trigger evaluation

All 6 FLASH-POLICY triggers evaluated against the in-window null result and standing anti-noise list. **0 triggers matched.**

| # | Trigger | Result | Why |
|---|---|---|---|
| 1 | critical-cve-exploited (CVSS ≥9.0 + active exploitation + A-grade) | **NOT MATCHED** | No new critical CVEs in NVD window; no new CISA KEV adds; no A-grade source surfaced active exploitation of any NEW CVE. Standing anti-noise hold absorbs CVE-2026-35273 (PeopleSoft/KEV 06-12 already finding-0002/0006), CVE-2026-20253 (Splunk already finding-0004), CVE-2026-10520 (Ivanti Sentry KEV 06-11 already covered 06-12). |
| 2 | tracked-actor-attribution (NEW attribution to roster actor) | **NOT MATCHED** | No new in-window items name any of the 24 roster actors or their aliases. UNC6240 attribution restatements absorbed by anti-noise (Mandiant substrate already finding-0002/0006). UNC6240 is NOT a roster actor regardless — operator-deferred per /new-actor carry-forward. |
| 3 | first-party-ioc-hit (Splunk match on tracked IOC, last 24h) | **NOT MATCHED** | Sentinel sweep across 19 tracked IOCs returned 0 telemetry events. Single Splunk match on the search terms was the librarian's own `git_committed` event from the 2026-06-13 16:37 EDT PM-brief commit (self-meta-match on embedded brief metadata, NOT first-party detection). Telemetry confirmed flowing (23 archimedes-index events visible -24h: 16 scheduler, 7 operation). |
| 4 | tracked-actor-ttp-change (new tooling/targeting/infra from A/B-grade) | **NOT MATCHED** | No in-window A/B-grade source documents new TTPs for any roster actor. |
| 5 | ad-sector-campaign (active multi-victim A&D-named campaign) | **NOT MATCHED** | No in-window items name aerospace-defense.yaml watchlist entities (Lockheed, Boeing, RTX, Northrop, GD, BAE, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit). UNC6240 PeopleSoft campaign restated only at substrate level (Mandiant page already covered); no new A&D-prime victim named. |
| 6 | zero-day-no-patch (CVSS ≥8.0 OR widely-deployed, exploitation confirmed) | **NOT MATCHED** | No new zero-day disclosures in window. |

## Anti-noise holds applied this sweep (per orchestrator binding + FLASH-POLICY §134-145)

The following topics were considered and confirmed NOT re-triggered (no net-new material from A-grade sources that materially changes assessment):

- **PeopleSoft / UNC6240 / CVE-2026-35273** — Mandiant direct-HTML listing surfaced same UNC6240 / ShinyHunters Education-Sector post that was the AM finding-0002 + PM finding-0006 substrate. NO second IR firm (Unit 42 / CrowdStrike / Microsoft / ZDI / Volexity / Trend Micro) surfaced this window. NO new A&D-prime victim named. NO net-new scale-corroboration on the 100-org / ~455k-record / 68% higher-ed numbers. Hold sustained.
- **CVE-2026-20253 Splunk Enterprise** — NO in-the-wild exploitation report surfaced this window. THN's "no evidence of the flaw being exploited in the wild" (yesterday's 13-word verbatim) carry-forward still applies; ~54h negative-inference window now (was ~48h yesterday PM); exploitation-status WEP remains DOWNGRADED from `likely` to `roughly_even_chance` per PM red-team HEDGE (adverse-selection: affected product IS the SIEM tier generating detection reports). Hold sustained.
- **NPM 12 default script-execution change** — No new GitHub blog primary retrieval surfaced (planned next sweep per PM commit dc85aae). SecurityWeek relay layer unchanged. Hold sustained.
- **Fable 5 / Mythos 5 USG export-control** — Three-publisher convergence (BleepingComputer + THN + SecurityWeek/AP) at status-quo; no fourth publisher with net-new substrate; no EAR/ITAR statute named in any source yet; no defense-prime deployment documented. SecurityAffairs Anthropic relay already reject-2026-06-13-0002. Hold sustained.
- **Handala / Cal Water** — 3rd-source check NEGATIVE per yesterday PM (BreachNews + Wanaen both read off Handala's own leak post); SecurityWeek + SecurityAffairs share Dataminr substrate; Cal Water still silent at publisher layer. Hold sustained.
- **Velvet Ant Operation Highland** — Sygnia primary covered 06-12 PM; BleepingComputer + THN 2nd/3rd-publisher relay reject-2026-06-13-0003. Hold sustained.
- **Ivanti Sentry honeypot story** — Covered 06-12; CVE-2026-10520 KEV add 06-11. Hold sustained.

## Splunk first-party sentinel — Hard Rule 8 + Trigger 3

Indexes queried: `archimedes`, `defenseclaw_local`. Time window: -24h.

**Sentinel set (19 tracked IOCs)** — 8 AM finding-0002 set + 11 net-new PM finding-0006 set:
- Domain: `azurenetfiles.net`
- IPs: `176.120.22.24`, `142.11.200.186-190` (5 staging IPs)
- Filenames: `meshagent64-azure-ops.exe`, `meshagent64-v2.exe`, `meshagent32-azure-ops.exe`, `exfil.tar.zst`, `README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT`
- Behavioral patterns: Python SimpleHTTPServer port 8888 staging, attacker `.bash_history`
- (SHA-256 hashes from finding-0006 evaluated in extended sweep set; 0 matches)

**Result: 0 telemetry events on either index over -24h** on the IOC-specific search. The one Splunk match on the broader keyword sweep (`SimpleHTTPServer` OR `8888` OR `.bash_history` OR `ShinyHunters` OR `UNC6240`) was the librarian's own `git_committed` event from 2026-06-13T16:37:45 EDT commit `dc85aae` — embedded brief metadata, NOT first-party detection. Filtered out as self-meta-match.

**Telemetry IS flowing** (23 archimedes-index events visible -24h: 16 scheduler + 7 operation), so the zero count is a true negative, not a visibility gap. Per AM brief structural note: Frank is not a higher-ed environment consistent with UNC6240's 68% higher-ed victim concentration — silent Splunk does NOT disconfirm UNC6240 at this substrate. **Trigger 3 does NOT fire.**

## Source-health deltas observed this sweep

- **mandiant (feedburner.com/Mandiant):** RSS path returned 404 again (26th consecutive failure). `failure_count` 25 → 26. Already `stale`; no status flip. Direct-HTML listing retrieval (cloud.google.com/blog/topics/threat-intelligence) succeeded this sweep — operator-note candidate carries forward unchanged: "Direct-HTML path working 2026-06-13 PM and 2026-06-14 00:00; RSS path remains stale; canonical-swap decision pending operator."
- **proofpoint:** Feed returned 404 again this sweep (matches yesterday's PM observation pattern). Soft observation only — no health entry update applied (pre-existing entry pattern noted as not load-bearing for current corpus tracking per PM sentinel). If pattern reproduces a third time next sweep, propose status flip to stale.
- **sans-isc:** Feed returned XML parse error ("syntax error" at line 2 col 0) — single-sweep soft observation, no health update applied. May indicate transient encoding/transport issue at the source rather than feed-side breakage. Re-check next sweep; if reproduced, increment failure_count.
- All other healthy sources reachable with 0 in-window items. No new degradations.

## Disposition

**0 FLASH candidates after anti-noise filter. 0 triggers fired.**

Per FLASH-POLICY anti-noise rule 1, the orchestrator exits silently. Quiet-hours gating (00:00 EDT is within 21:00–09:00 EDT) would have queued any triggers regardless, but no triggers fired so the queue remains empty. No grader handoff. No briefer handoff. No librarian Discord post.

Net-new content for grader attention this window: **none**.

Carry-forward observations for next sweep (06:00 EDT):
- Mandiant feedburner stale-persistent (now 26 consecutive failures) — direct-HTML path remains viable, canonical-swap decision still pending operator
- Proofpoint 404 reproduced — propose stale flip if third occurrence
- SANS ISC RSS parse error single-occurrence — re-check
- NPM 12 GitHub blog primary retrieval still pending next sweep per PM commit dc85aae
- CVE-2026-20253 Splunk exploitation negative-inference window now ~54h; hedge persists; watch for second-vendor confirmation
- UNC6240 dossier creation remains operator-deferred per /new-actor carry-forward (11 net-new IOCs from finding-0006 still living at finding level, not folded into any actor iocs.yaml)
- Provisional source-grades ratification queue clock: 2026-06-15T16:00:00-04:00 (now ~40h out); Sonatype + Sygnia + Tenet Security + Dataminr + splunk-advisory + watchtowr-labs + breachnews + wanaen + Bloomberg-tier-decision all in queue per PM dc85aae

## Extraction notes

- Language: en
- Article type: sentinel (internal)
- Raw IOC extraction invoked: no (no candidate items)
- Publisher byline: n/a (internal sentinel)
