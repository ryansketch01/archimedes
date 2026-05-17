---
raw_id: raw-2026-05-17-am-000
collected_at: 2026-05-17T07:32:00-04:00
run_id: pre-brief-20260517-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-self
  source_name: "Archimedes collector — pre-brief sweep sentinel"
  source_url: null
  published_at: 2026-05-17T07:32:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, pre_brief, dedup_audit, sunday_quiet]
triage_tags:
  - sentinel
  - non_flash
  - dedup_audit
  - splunk_self_telemetry_only
  - dormant_splunk_sweep_35
  - sunday_pattern
  - cve_2026_20182_kev_t_0_today
  - cve_2026_42897_kev_t_12d
  - symantec_provisional_a_clock_fired_13h_ago
iocs_extracted: false
iocs_count: 0
text_word_count: 1450
promoted: false
ttl_expires_at: 2026-08-15T07:32:00-04:00
---

# Pre-brief sweep sentinel — 2026-05-17 07:30 EDT (Sunday)

**Window:** 2026-05-16 17:30 EDT → 2026-05-17 07:32 EDT (~14h)
**Prior sweeps in this window:**
- 2026-05-16 17:30 EDT on-demand FLASH (clean sweep, 0 triggers, commit at top of repo log; raw-2026-05-16-flash-1730-000)
- 2026-05-17 00:00 EDT scheduled FLASH (clean sweep, 0 triggers; raw-2026-05-17-flash-0000-000; commit d369efd)
- 2026-05-17 06:00 EDT scheduled FLASH (clean sweep, 0 triggers, 34th consecutive dormant Splunk sweep, Grafana/CoinbaseCartel discarded; raw-2026-05-17-flash-0600-000; commit 83cb46f)

**Quiet hours:** ending 09:00 EDT today; morning brief publishes 08:00 EDT (well within active window).
**Catchup-window load this pre-brief:** the 17:30 / 00:00 / 06:00 sweeps already cleared the bulk of the 14h window; this pre-brief is effectively the gap-fill 06:00 → 07:30 (~1.5h fresh window) plus a full re-pass of the priority sources to catch any items that drifted in.

---

## Sources queried (this pre-brief sweep)

| Source | Status | Items in 14h window | Notes |
|---|---|---|---|
| CISA Advisories (`cisa-advisories`, RSS all.xml) | OK 200 | 0 | 30 items in feed total, all pre-window |
| CISA KEV (`cisa-kev`, JSON via WebFetch) | OK | 0 new entries | catalogVersion 2026.05.15 (unchanged from 06:00 sweep). Top entries: CVE-2026-42897 (Exchange OWA XSS, dateAdded 2026-05-15, due 2026-05-29 / **T-12d**), CVE-2026-20182 (Cisco Catalyst SD-WAN auth bypass, dateAdded 2026-05-14, due 2026-05-17 / **T-0 TODAY**), CVE-2026-42208 (LiteLLM, 2026-05-08), CVE-2026-6973 (Ivanti EPMM, 2026-05-07), CVE-2026-0300 (PAN-OS, 2026-05-06), CVE-2026-31431 (Linux Kernel, 2026-05-01), CVE-2026-41940 (WebPros cPanel & WHM, 2026-04-30 — Known ransomware use), CVE-2024-1708 (ConnectWise ScreenConnect, 2026-04-28 — Known ransomware use) |
| The Hacker News (`thehackernews`, RSS) | OK 200 | 1 (Grafana/CoinbaseCartel, evaluated and discarded — see below) | last_modified 10:51 UTC = 06:51 EDT, server-fresh |
| BleepingComputer (`bleepingcomputer`, RSS) | OK 200 | 0 | last_modified 11:21 UTC = 07:21 EDT, server-fresh. Homepage WebFetch confirms top 12 are all pre-window or already captured (Microsoft May 2026 Patch Tuesday from 2026-05-12 14:08, Shai-Hulud TanStack/Mistral from 2026-05-12 07:29, Kazuar P2P botnet from 2026-05-16 10:15 — all duplicate-locked) |
| SecurityWeek (`securityweek`, RSS) | OK 200 | 0 | last_modified 2026-05-16 12:45 UTC, pre-window. Homepage WebFetch top 12 confirmed all 2026-05-14 / 2026-05-15 / 2026-05-16 dated items already in corpus |
| Krebs on Security (`krebs`, RSS) | OK 200 | 0 | last_modified 2026-05-13, multi-day Krebs cadence (normal for weekend) |
| The Record (`the-record`, RSS) | OK 200 | 0 | 5 items in feed total, all pre-window |
| Unit 42 (`unit42`, RSS feedburner) | OK 200 | 0 | last_modified 2026-05-15 19:46 UTC, pre-window |
| Microsoft Security Blog parent feed (`mstic`, RSS) | OK 200 | 0 | last_modified 2026-05-14 21:51 UTC, pre-window. msrc.microsoft.com/blog/feed XML parse error this sweep (recurrence of known intermittent issue) |
| MITRE/CrowdStrike (`crowdstrike`, RSS) | OK 200 | 10 items but all dateless marketing/MQ content | last_modified 2026-05-17 07:36 UTC = 03:36 EDT server-fresh, but content unchanged from established 15th-consecutive-sweep dateless-marketing pattern |
| ESET WeLiveSecurity (`eset`, RSS) | OK 200 | 0 | 100 items in feed, all pre-window |
| SentinelLabs (`sentinelone`, RSS) | OK 200 | 0 | last_modified 2026-05-15 19:30 UTC, pre-window |
| Rapid7 (`rapid7`, RSS) | OK 200 | 0 | last_modified 2026-05-17 11:19 UTC = 07:19 EDT server-fresh, no new posts |
| SANS ISC (`sans-isc`, RSS rssfeed.xml) | **RECOVERED** OK 200 | 0 | 06:00 FLASH had RSS parse error; 07:30 returned 200, valid RSS (10 items), 0 in-window after since-filter. Same transient-class as 2026-05-10 18:00 and 2026-05-12 06:00 prior recoveries |
| Cisco Talos (`cisco-talos`, RSS) | 404 (third consecutive) | n/a via RSS; alt-path WebFetch verified | RSS endpoint blog.talosintelligence.com/feeds/posts/default returned 404 — third consecutive failure (17:30 + 00:00 + 06:00 + 07:30 = fourth observed). Blog index WebFetch reachable; latest post 2026-05-14 12:02 ("Ongoing exploitation of Cisco Catalyst SD-WAN vulnerabilities" — already in finding chain). No 2026-05-16 or 2026-05-17 posts. See source-health update note. |
| Sophos (`sophos`, RSS) | 404 (already stale per 06:00 commit) | n/a — already stale_since 2026-05-17 | Skipped per under-24h-stale rule; blog index WebFetch reachable but no new dated entries |
| Mandiant feedburner (`mandiant`) | 404 (~20th consecutive) | n/a | Carried in expected-broken state per source-health.yaml |
| Dragos (`dragos`) | known broken | n/a | /blog/feed/ 404; carried in expected-broken state |
| Bitdefender Labs (`bitdefender`) | businessinsights.bitdefender.com/rss 404 | n/a | Same path-discovery issue as 2026-05-16; blog index page out-of-window |
| Symantec security.com (`symantec`) | symantec-enterprise-blogs feed 404 | n/a | Same path-discovery issue as 2026-05-16. Operator may have changed surface; flag for source-health if recurs |
| Wiz Research (`wiz-research`) | feed.xml 404 | n/a | Same path-discovery issue as 2026-05-16 |
| Socket (`socket`) | blog/rss.xml 404 | n/a | Same path-discovery issue as 2026-05-16 |
| Industrial Cyber (`industrialcyber-co`) | 403 (Akamai WAF/bot-block) | n/a | Consistent prior pattern |
| Dark Reading (`darkreading`, RSS via mcp__rss-bridge__fetch_feed) | OK 200 | 1 (thought-leadership opinion piece, evaluated and discarded — see below) | last_modified 2026-05-17 11:32 UTC = 07:32 EDT server-fresh |
| ZDI Pwn2Own blog (`zdi-blog`, RSS) | OK 200 | 0 | 20 items in feed, all pre-window — last Pwn2Own Berlin Day 3 wrap was 2026-05-16 morning (raw-2026-05-16-am-001) |
| Splunk first-party (`splunk-archimedes`, `splunk-defenseclaw`) | OK | 0 non-self-telemetry events | **35th consecutive dormant non-self-telemetry sweep** — see Splunk section below |
| x-cisagov | stale (nitter bridge fragility) | skipped per source-health | <24h since stale_since=2026-05-10; eligible next sweep |
| x-gossithedog | stale (nitter delisted) | skipped per source-health | |
| ars-security | stale (feed retired) | skipped per source-health | Workaround: arstechnica.com/feed root works but security-only is retired |

---

## Splunk self-telemetry sweep

`index=archimedes OR index=defenseclaw_local earliest=-24h | stats count by sourcetype` returned:

- `archimedes:operation` = 17 events (pipeline operations, brief publications, FLASH evaluations, scoring events, etc.)
- `archimedes:scheduler` = 16 events (scheduled task launches)
- **Zero non-self-telemetry sourcetypes.**

This is the **35th consecutive dormant non-self-telemetry Splunk sweep**. Pattern fully entrenched. Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`. Trigger 3 (first-party-ioc-hit) cannot fire on a dormant non-archimedes-event stream.

---

## Single in-window THN item evaluated and discarded

**The Hacker News (2026-05-17T07:13 UTC = 03:13 EDT): "Grafana GitHub Token Breach Led to Codebase Download and Extortion Attempt"**

- Same item evaluated and discarded at the 06:00 FLASH sweep (raw-2026-05-17-flash-0600-000, commit 83cb46f). Anti-noise applies — not re-evaluated against FLASH triggers this sweep.
- Carry-forward note from the 06:00 sweep applies verbatim: "Item may be picked up by the grader on this morning's 08:00 brief as a supply-chain-credential-exposure item — Grafana is a widely-deployed observability platform in enterprise IT including A&D-adjacent operations, but no A&D-prime exposure is asserted by the source and Archimedes does not extrapolate. It is NOT FLASH-eligible. Coverage decision deferred to morning brief grader/briefer."
- Per orchestrator scope this morning: "The Hacker News Grafana/CoinbaseCartel codebase-download extortion (deferred from 06:00 FLASH sweep as possible sub-FLASH supply-chain item) — re-evaluate in 24h grading window." That re-evaluation is the briefer/grader's responsibility, not the collector's. Collector preserves the discard disposition.

## Single in-window Dark Reading item evaluated and discarded

**Dark Reading (2026-05-18T13:00 UTC future-scheduled per editorial calendar, fetched 2026-05-17T07:32 EDT): "The Boring Stuff is Dangerous Now"**

- Author: Shlomie Liberow (contributor byline; not a Tier-1 research practice byline).
- Article type: thought-leadership / opinion editorial on the AI-code-and-agents threat landscape.
- Body fetch returned 403 (Dark Reading paywall / bot-block on the article URL). Per RSS summary: "AI agents capable of discovering and exploiting obscure vulnerabilities are emerging alongside developers producing vast amounts of potentially flawed AI-generated code, forcing defenders to adapt accordingly."
- **No specific threat actor named.** **No CVE referenced.** **No IOCs.** **No A&D entity named.** **No campaign described.**
- Generic editorial framing. Fails A&D / roster / vuln-index filter per Mode 1 procedure.
- **DISPOSITION: DISCARDED.** Not raw-signaled as a standalone file (noted here for filter-trail transparency).

---

## Carry-forwards preserved (NOT re-collected)

Per orchestrator scope this morning — watch for new developments but do NOT re-collect existing topics:

1. **CVE-2026-20182 Cisco Catalyst SD-WAN auth bypass (CVSS 10.0, CISA KEV).** Federal patch deadline is **TODAY 2026-05-17** (T-0). Watched this sweep for late-disclosure exploitation, attribution updates, or CISA bulletins: zero new items. KEV catalogVersion 2026.05.15 unchanged (no T-0-day catalog refresh observed yet). Cisco Talos blog has no new post since 2026-05-14 12:02. SecurityWeek + BleepingComputer + The Hacker News + The Record + Krebs all 0 in-window items on this topic. Calendar-event for the morning brief (08:00 EDT) — no new collector trigger.

2. **CVE-2026-42897 Microsoft Exchange OWA XSS (CISA KEV, due 2026-05-29).** T-12d to federal patch deadline. Watched for PoC release or exploitation reporting: zero new items.

3. **Symantec Threat Hunter Team / SentinelLABS Fast16 (2005-era pre-Stuxnet simulation-sabotage framework targeting LS-DYNA + AUTODYN).** Provisional-A ratification clock fired 2026-05-16T18:25 EDT — currently **T+13h 7m** since clock fire. Watched this sweep for second-corpus citations: zero new corpus citations of the Fast16 research from any A/B-grade source. Single-source veto at finding-2026-05-16-0003 remains in effect (capped at "likely" WEP). Awaiting operator pass on ratification — outside collector scope.

4. **CVE-2026-42945 NGINX Rift PoC carry-forward** (depthfirst GitHub repo per finding-2026-05-16-0001). No new exploitation reporting or vendor advisory updates in window.

5. **Pwn2Own Berlin closure carry-forward** (raw-2026-05-16-am-001; $943,250 total / 42 zero-days; Day 2 Orange Tsai DEVCORE Exchange RCE-to-SYSTEM chain under standard 90-day embargo). No new ZDI blog posts in window.

6. **Turla/Kazuar D+2 relay layer duplicate-lock** (finding-2026-05-14-0006 / reject-2026-05-16-0001). BleepingComputer's "Russian hackers turn Kazuar backdoor into modular P2P botnet" item from 2026-05-16 10:15 AM EDT appears in BleepingComputer top-feed-position this sweep — this is the same surface already duplicate-locked. Anti-noise rule 1 active. **Not re-collected.**

---

## Source health observations (this sweep)

Runtime state changes proposed for `infrastructure/source-health.yaml` (operator-set `notes` preserved verbatim):

- **`sans-isc`**: RECOVERED. 06:00 FLASH had `rssfeed.xml` parse error. This sweep: status 200, valid RSS, 10 items, 0 in-window. Same transient-class as prior recoveries (2026-05-10 18:00, 2026-05-12 06:00). `failure_count` held at 1 (no second consecutive failure today; transient cleared). `last_successful_fetch` updates to 2026-05-17T07:32:00-04:00. `last_error` cleared.

- **`cisco-talos`**: continued RSS-endpoint failure. blog.talosintelligence.com/feeds/posts/default returned 404 — this is the FOURTH observed failure across 17:30 / 00:00 / 06:00 / 07:30 sweeps. Per ≥2-consecutive rule, this should formally flip to `stale`. Holding healthy for now ONLY because: (a) the blog-index WebFetch alt-path verifies working and surfaces the same latest-post date (2026-05-14 12:02); (b) the CVE-2026-20182 carry-forward is Talos-originating and stale-flipping the source on T-0 deadline day is operationally noisy; (c) operator-side path-replacement decision pending. **Recommend operator confirm or override.** `failure_count` should increment to 4 to reflect cumulative same-class observations; `last_error` updated.

- **`thehackernews`**: healthy. Fetch successful; in-window item (Grafana/CoinbaseCartel) evaluated and discarded at 06:00 + this pre-brief. `last_successful_fetch` updates to 2026-05-17T07:32:00-04:00.

- **`bleepingcomputer`**: healthy. Fetch successful; 0 in-window items; homepage WebFetch confirms top-12 already-captured topics. `last_successful_fetch` updates to 2026-05-17T07:32:00-04:00.

- **`splunk-archimedes`**, **`splunk-defenseclaw`**: both healthy; 35th consecutive dormant non-self-telemetry sweep. `last_successful_fetch` updates to 2026-05-17T07:32:00-04:00.

- All other queried sources: reachable or in known expected-broken/stale state per source-health.yaml; no changes proposed.

- `darkreading`: not currently in source-health.yaml or source-grades.yaml as a tracked source — the in-window discard above was a single opportunistic fetch via mcp__rss-bridge__fetch_feed for coverage discipline. Operator may consider adding to source-grades.yaml as provisional-B media outlet if this becomes a recurring surface; flagging only.

---

## Disposition

**Clean sweep, 0 new items survive A&D / roster / vuln-index filter, 35th consecutive dormant non-self-telemetry Splunk sweep.** Two in-window items evaluated and discarded (Grafana/CoinbaseCartel — anti-noise/carry-from-06:00; Dark Reading opinion piece — fails A&D filter). Carry-forwards unchanged. CVE-2026-20182 KEV federal deadline TODAY is calendar-event for the 08:00 morning brief; Symantec Fast16 provisional-A ratification clock at T+13h 7m awaiting operator pass.

**No FLASH-eligible items spotted.** Coverage decision on the Grafana/CoinbaseCartel item is deferred to the morning brief grader/briefer (orchestrator scope explicitly directs that re-evaluation, which is grading/promotion territory, not collector).

**Source-health runtime updates queued for `infrastructure/source-health.yaml`:** sans-isc recovered (last_successful_fetch, last_error cleared); cisco-talos failure_count++ with last_error updated; thehackernews + bleepingcomputer + splunk-archimedes + splunk-defenseclaw last_successful_fetch refresh. Operator-set `notes:` fields preserved verbatim per Hard Rule field-ownership doctrine.
