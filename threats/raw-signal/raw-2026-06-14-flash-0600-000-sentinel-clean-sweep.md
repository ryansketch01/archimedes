---
raw_id: raw-2026-06-14-flash-0600-000
collected_at: 2026-06-14T06:03:00-04:00
run_id: flash-sweep-20260614-060000
collection_mode: flash_sweep
source:
  source_yaml_id: sentinel-internal
  source_name: "FLASH sweep sentinel (internal)"
  source_url: null
  published_at: 2026-06-14T06:03:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [flash_sweep_clean, source_health_delta_observed]
triage_tags: [non_flash, sentinel, sweep_clean]
iocs_extracted: false
iocs_count: 0
text_word_count: 690
promoted: false
ttl_expires_at: 2026-09-12T06:03:00-04:00
---

# FLASH sweep 2026-06-14 06:00 EDT — clean sweep, 0 candidates, 0 triggers

## Sweep parameters

- Mode: `flash_sweep`
- Time window: 2026-06-13T18:00:00-04:00 → 2026-06-14T06:03:00-04:00 (~12h since prior 18:00 FLASH sweep, which was itself clean per commit 4a1dd47's preceding 18:00 sentinel; this sweep effectively covers the overnight EDT window outside quiet-hours wake threshold)
- **Quiet hours active** (00:00–09:00 EDT per FLASH-POLICY §Quiet Hours) — any FLASH would queue rather than post; critical override (CVSS 10.0 + active exploit + tracked actor + A&D entity named) NOT met today
- Sources queried: 15 healthy primary feeds + KEV JSON + NVD lastModified window + Mandiant direct-HTML index
- Sources skipped (stale, <24h since stale_since per under-24h rule): volexity, msrc, lumen, shadowserver, sophos, industrialcyber-co, ars-security, trellix, x-cisagov, x-gossithedog, censys, urlscan, hibp
- Sources skipped (stale, retried per >=24h rule): mandiant feedburner (retried, still 404 — 26th consecutive)

## Items in window

- **BleepingComputer:** 0 items in 12h window after since-filter (RSS reachable, 15 items in feed total, all pre-2026-06-13T18:00 EDT)
- **The Hacker News:** 0 items in 12h window after since-filter (RSS reachable, 50 items in feed total, all pre-window)
- **SecurityWeek:** 0 items in 12h window after since-filter (RSS reachable, 10 items in feed total, last_modified Sat 13 Jun 2026 15:54 GMT pre-window)
- **SecurityAffairs:** 1 item in window — "Ukrainian Extradited from Ireland Pleads Guilty Over Role in Conti Ransomware Scheme" (2026-06-14T05:58 UTC). DOJ retrospective indictment resolution on Oleksii Lytvynenko (44, Ukrainian extradited from Ireland, plea ~Cork base, ~$150M Conti payment estimate by January 2022, sentencing 2026-09-10, up to 20-year max). Conti is NOT on `_roster.yaml` actor list (Conti shuttered May 2022 with internal-chat leaks per source; lineage tracked into Black Basta / other clusters elsewhere on Archimedes corpus but the Conti brand itself is retrospective). No NEW attribution to a roster-tracked actor. No exploitation. No IOC. Not multi-victim active campaign. **All 6 triggers NEGATIVE.** Carries DOJ-primary cite — could surface in next scheduled brief as DOJ-cycle awareness, NOT FLASH. DISCARDED per Mode 1 procedure (no watchlist/roster/vuln-index hit).
- **The Record:** 0 items in 12h window after since-filter (RSS reachable, 5 items in feed total, all pre-window)
- **Krebs:** 0 items in 12h window after since-filter (RSS reachable, last_modified Thu 11 Jun 2026 17:38 GMT pre-window)
- **CISA all.xml:** 0 items in 12h window after since-filter (Atom reachable, 30 items in feed total, all pre-window)
- **SANS ISC rssfeed.xml:** 0 items in 12h window after since-filter (RSS reachable, 10 items in feed total, last_modified Sun 14 Jun 2026 09:59 GMT inside window from feed-server activity but no items in window — most recent diary 2026-06-10 per archive page). Soft-recovery from 2026-06-13 PM parse-error 1/3 (RSS reachable AND parseable this sweep).
- **The Register security:** 0 items in 12h window after since-filter
- **Talos Intelligence:** feed endpoint blog.talosintelligence.com/feeds/posts/default returned 404 (first observation this sweep — soft fail, no health update applied since no prior baseline). Worth flagging for next pre-brief retry. Not load-bearing for current sweep.
- **DarkReading:** 1 dateless "Name That Toon Contest" event marketing item — DISCARDED.
- **Unit 42 feedburner:** 0 items in 12h window after since-filter (RSS reachable, last_modified Fri 12 Jun 2026 22:27 GMT pre-window)
- **Microsoft Security Blog (MSTIC parent):** 0 items in 12h window after since-filter (RSS reachable, last_modified Wed 10 Jun 2026 16:00 GMT pre-window)
- **Help Net Security:** 1 item in window — "Week in review: Exploited Check Point VPN zero-day, Oracle PeopleSoft servers under attack" (2026-06-14T08:00 UTC published time, surfaced just inside this sweep's window). Pure retrospective recap of June 8-12 stories (DockSec, CISA SolarWinds Serv-U CVE-2026-28318, Check Point CVE-2026-50751/Qilin, FIFA-themed domains, Meta AI 20k Instagram hijack, NSO WhatsApp targeting, OpenAI ChatGPT Lockdown, LiteLLM CVE-2026-42271 KEV add, Mythos Preview N-day weaponization, Chrome CVE-2026-11645, Tchap French-gov messaging breach, Microsoft Patch Tuesday + "RoguePlanet" zero-day, Ivanti Sentry CVE-2026-10520, BitB campaign, BOD-26-04 patch-smarter directive, Oracle PeopleSoft CVE-2026-35273, FBI 13-domain seizure China-intel, Google Outsider Enterprise/Gemini lawsuit, Zscaler phishing-decline report, AudiA6 €336M takedown). All cited stories pre-2026-06-13T18:00 EDT and ALL ALREADY covered in prior briefs (Check Point CVE-2026-50751/Qilin in 2026-06-10 morning + 2026-06-11 afternoon; PeopleSoft CVE-2026-35273 in 2026-06-11 + 2026-06-13 AM/PM; Ivanti Sentry CVE-2026-10520 in 2026-06-11; AudiA6/Europol in 2026-06-11 PM; Patch Tuesday in 2026-06-10 PM). DISCARDED — retrospective recap with NO net-new substrate.
- **ESET WeLiveSecurity:** 0 items in 12h window after since-filter (RSS reachable, last_modified Sat 13 Jun 2026 05:32 GMT pre-window)
- **CyberScoop:** 0 items in 12h window after since-filter (RSS reachable, last_modified Sat 13 Jun 2026 18:30 GMT pre-window by 30 minutes)
- **Proofpoint Threat Insight:** feed returned 404 again (3rd consecutive observation per orchestrator note; prior 2/3 noted in 06-13 18:00 sentinel). Soft observation pattern; no top-level proofpoint source-health entry exists to flip yet.
- **Mandiant cloud.google.com/blog/topics/threat-intelligence direct-HTML index:** Top-8 posts retrieved successfully — GTIG AI Threat Tracker, ShinyHunters/PeopleSoft (covered finding-2026-06-13-0002+0006), Seeking Counsel US law firms campaign, KnowledgeDeliver ViewState exploit, 2 PhaaS 2 Furious, BlackFile vishing, UNC6692 Snow Flurries, deSouza AI vuln post. None dated in the 12h window; all out-of-window or already-substrate. Direct-HTML path CONFIRMED still working consistently 2026-06-13 PM → 2026-06-14 06:00 — operator-note candidate carries forward.
- **NVD lastModStartDate window query** (2026-06-13T22:00 → 2026-06-14T10:00 UTC, cvssV3Severity=CRITICAL): not run this sweep — FLASH-fast scope; prior pre-brief evidence shows NVD lastModified records consistently surface metadata refreshes on pre-existing CVEs rather than fresh active-exploitation triggers, so deferred to the 07:30 pre-brief.
- **CISA KEV catalog scan** (dateAdded=2026-06-13 OR 2026-06-14): 0 entries. Five most recent KEV adds: CVE-2026-35273 Oracle PeopleSoft (2026-06-12, dueDate 2026-06-15 ~T-2 days now), CVE-2026-10520 Ivanti Sentry (2026-06-11, dueDate 2026-06-14 = today EOB ~T-12h), CVE-2026-11645 Chrome V8 (2026-06-09), CVE-2026-7473 Arista EOS (2026-06-09), CVE-2026-20245 Cisco Catalyst SD-WAN (2026-06-09). The PeopleSoft and Ivanti Sentry topics are anti-noise-held; the Chrome/Arista/Cisco June 9 cluster covered in prior briefs. NO net-new KEV adds. **Trigger 1 NEGATIVE.**

## FLASH trigger evaluation

All 6 triggers evaluated against the in-window content (SecurityAffairs Conti DOJ plea, HelpNet Week-in-Review recap, BleepingComputer empty window) and against the standing anti-noise list. **0 triggers matched.**

- **Trigger 1 (critical CVE actively exploited):** NEGATIVE. KEV unchanged 2026-06-12. No new A-grade source claims on a CVSS >=9.0 vuln with active exploitation in the 12h window.
- **Trigger 2 (new attribution for tracked actor):** NEGATIVE. SecurityAffairs Conti/Lytvynenko item is DOJ-charge-resolution retrospective; Conti not in roster; no new attribution to a roster-tracked actor.
- **Trigger 3 (first-party IOC hit):** NEGATIVE. Splunk -12h scan on UNC6240 19-IOC sentinel set returned 0 events on both `archimedes` and `defenseclaw_local` indexes.
- **Trigger 4 (tracked actor TTP change):** NEGATIVE. No new TTP-class substrate from A/B-grade source on a roster actor.
- **Trigger 5 (active A&D-sector campaign):** NEGATIVE. No new active multi-victim campaign vs A&D / watchlist entity in window.
- **Trigger 6 (zero-day without patch):** NEGATIVE. No new zero-day disclosure in window.

## Anti-noise holds (per orchestrator binding + Doctrine §134-145)

The following topics are anti-noise-held; their absence from this sweep's trigger output is intentional, NOT a re-evaluation:

- PeopleSoft / UNC6240 / CVE-2026-35273 (finding-2026-06-13-0002 AM + finding-2026-06-13-0006 PM; BOD 26-04 deadline ~2026-06-15 still in clock)
- CVE-2026-20253 Splunk Enterprise (finding-2026-06-13-0004 PM)
- NPM 12 default script-execution change (finding-2026-06-13-0005 PM)
- Fable 5 / Mythos 5 USG export-control on Anthropic (finding-2026-06-13-0001 AM)
- Handala / Cal Water single-Dataminr-substrate (finding-2026-06-13-0003 PM)
- Velvet Ant Operation Highland (covered 06/12 PM)
- Ivanti Sentry CVE-2026-10520 (finding-2026-06-11-0001; KEV deadline 2026-06-14 EOB ~T-12h from this sweep)
- Check Point VPN CVE-2026-50751 + Qilin (finding-2026-06-10-flash-0000-002 + 2026-06-11 afternoon brief)

## Splunk first-party sentinel — Hard Rule 8 + Trigger 3

Indexes queried: `archimedes`, `defenseclaw_local`. Time window: -12h.

Sentinel set: UNC6240 19-IOC carry-forward from PM brief commit dc85aae — `azurenetfiles.net`, `176.120.22.24`, staging IPs `142.11.200.186-190`, Python SimpleHTTPServer:8888 pattern, Windows meshagent SHA-256 substitutes, Linux meshagent SHA-256, `.bash_history`, `exfil.tar.zst`, `README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT` defacement marker.

**Result: 0 events over -12h on either index.** Frank is not a higher-ed environment consistent with UNC6240's 68% higher-ed victim concentration — silent Splunk does NOT disconfirm at this substrate. Visibility-limited absence, NOT confirmed-negative.

## Source-health deltas observed this sweep

- **mandiant:** feedburner.com/Mandiant returned 404 again (26th consecutive failure — already on 26 per `last_attempt: 2026-06-14T00:02:30` value from the 00:00 sweep; this 06:00 sweep retried per >=24h-since-stale rule but produced same outcome). `failure_count` remains 26 (no double-increment for retries inside the same stale period). `last_attempt` advances to this sweep timestamp. Already `stale`; no status flip. Direct-HTML retrieval path SUCCEEDED again this sweep (top-8 posts visible, all out-of-window) — operator-note candidate "Direct-HTML path working consistently 2026-06-13 PM + 2026-06-14 00:00 + 2026-06-14 06:00" carries forward; canonical-swap decision still pending operator.
- **sans-isc:** rssfeed.xml RECOVERED parseability this sweep after the 2026-06-13 PM 1/3 parse error. `failure_count` stays at 0 (was already healthy). last_successful_fetch advances. No change.
- **proofpoint:** 404 again (3rd consecutive observation; soft-pattern). No top-level entry to flip yet.
- **talos:** blog.talosintelligence.com/feeds/posts/default returned 404 (first observation; soft, no health update).
- All other healthy sources reachable with 0 in-window items. No new degradations beyond Mandiant `last_attempt` advance.

## Disposition

0 FLASH candidates. 0 triggers matched. Per FLASH-POLICY anti-noise rule 1, the orchestrator exits silently. Net-new content for grader attention this window: **none**.

The two in-window items (SecurityAffairs Conti DOJ plea, HelpNet Week-in-Review recap) are logged in this sentinel file's "Items in window" section for audit-trail purposes and are NOT grader candidates (no watchlist/roster/vuln-index hit + retrospective-only).

Items worth flagging to the orchestrator as trigger-NEGATIVE-but-noted for 07:30 pre-brief awareness:

- SecurityAffairs Conti / Lytvynenko DOJ plea — DOJ-cycle awareness item, A-grade DOJ primary cite available in SA relay; not FLASH but could surface in afternoon brief as criminal-justice cycle bullet if grader picks it up
- BOD 26-04 PeopleSoft deadline 2026-06-15 (~T-36h) — clock still active, anti-noise-held, grader may surface as "still in clock" reminder if no FCEB-compliance data has surfaced
- Ivanti Sentry CVE-2026-10520 KEV deadline 2026-06-14 EOB (~T-12h from this sweep) — clock closes today; grader may surface as "deadline-today" reminder if no FCEB-compliance data has surfaced
- Talos feed 404 (first observation) — collector/operator follow-up flag

## Extraction notes

- Language: en
- Article type: sentinel (internal)
- Raw IOC extraction invoked: no (no candidate items)
- Hard Rule binding: Rule 1 (LEGAL-POLICY) — all queries passive RSS/WebFetch/Splunk-self; Rule 8 (Splunk first-party) — sentinel Splunk scan emitted; Rule 2 (no attribution origination) — no novel attributions made this sweep
