---
raw_id: raw-2026-05-16-pm-000
collected_at: 2026-05-16T15:40:00-04:00
run_id: pre-brief-20260516-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-self
  source_name: "Archimedes collector — afternoon pre-brief sweep sentinel"
  source_url: null
  published_at: 2026-05-16T15:40:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, pre_brief, dedup_audit, saturday_quiet]
triage_tags: [sentinel, non_flash, dedup_audit, splunk_self_telemetry_only, saturday_pattern]
iocs_extracted: false
iocs_count: 0
text_word_count: 880
promoted: false
ttl_expires_at: 2026-08-14T15:40:00-04:00
---

# Afternoon pre-brief sweep sentinel — 2026-05-16 15:30 EDT (Saturday)

Window: 2026-05-16 07:30 EDT → 2026-05-16 15:30 EDT (8h)
Last prior sweep: 2026-05-16 11:30 EDT on-demand FLASH (clean, 0 triggers, 31st consecutive dormant non-self-telemetry Splunk sweep per commit 9bc608f)
Intervening publication: 2026-05-16 08:00 morning brief (commit 3cc6118 — 30th consecutive dormant non-self-telemetry sweep noted there)
Quiet hours: NOT active (15:30 EDT is well inside 09:00–21:00 window) — afternoon brief will publish at 16:00 EDT, no queueing

## Conclusion (top-line)

**1 raw signal written (Symantec Fast16 historical-research, sector-adjacent, NOT a FLASH candidate)**, 0 FLASH-shape candidates, **32nd consecutive dormant non-self-telemetry Splunk sweep**. All 6 carry-forward items checked; only Symantec Fast16 surfaced as new in-window content from the A-grade priority set. Source-health: 1 NEW failure_count increment proposed (Sophos retry confirmed second consecutive failure — flagging at threshold but not yet stale).

## Sources queried (in 8h pre-brief window)

| Source | Status | Items in window |
|---|---|---|
| CISA Advisories (RSS all.xml) | OK | 0 |
| CISA KEV (JSON, full-catalog dateAdded scan) | OK | 0 new — most recent: CVE-2026-42897 dateAdded 2026-05-15 dueDate 2026-05-29 (T-13 today); CVE-2026-20182 dateAdded 2026-05-14 dueDate 2026-05-17 (**T-1 tomorrow**) |
| BleepingComputer (RSS) | OK | 1 — Turla/Kazuar P2P relay (Bill Toulas 10:15 EDT) — **duplicate-locked against finding-2026-05-14-0006 + reject-2026-05-16-0001**; same anti-noise lock active since 2026-05-15 18:00; pure outlet-to-outlet relay layer, no new IOCs / no new victims / no new tradecraft (verified via WebFetch) |
| The Record (RSS) | OK | 0 |
| The Hacker News (RSS) | OK | 1 — "Funnel Builder Flaw Under Active Exploitation Enables WooCommerce Checkout Skimming" (Sansec, 15:20 UTC); WordPress plugin payment skimmer; NO official CVE; NO A&D / NO roster actor / NO tracked vuln; commodity WP-checkout skimmer (40k+ WooCommerce stores); **DISCARDED per Mode 1 procedure** (no watchlist / roster / vuln-index hit) |
| Krebs (RSS) | OK | 0 (last_modified 19:24 UTC = 15:24 EDT inside window from feed-server activity; no new posts since 2026-05-13 — multi-day Krebs cadence) |
| Microsoft Security Blog (RSS) | OK | 0 (last_modified 2026-05-14 21:51 UTC pre-window — unchanged from morning sweep; MSTIC quiet through weekend) |
| MSRC blog (redirect) | OK via redirect | n/a — covered via parent MS Security Blog feed |
| Mandiant (cloud.google.com index page) | feedburner 404 persistent | n/a — index-page top-8 unchanged from morning (UNC6692 / Axios NPM / BRICKSTORM / M-Trends / German Überfall / deSouza AI / BlackFile / GTIG AI) — all out-of-window |
| Unit 42 (feedburner) | OK | 0 (last_modified 2026-05-15 19:46 UTC pre-window) |
| Cisco Talos (RSS) | OK | 0 |
| Securelist (RSS) | OK | 0 (last_modified 2026-05-15 10:15 UTC pre-window) |
| Sophos (RSS) | **404 again** | n/a — **second consecutive failure** this sweep; first was morning 07:30 sweep; failure_count 0→1 then 1→2 across the two sweeps — held healthy per the held-healthy 2-failure rule, but at threshold; recommend operator path re-discovery; A-grade primary surface, NOT load-bearing this sweep |
| WeLiveSecurity / ESET (RSS) | OK | 0 |
| SentinelOne / SentinelLabs (RSS) | OK | 0 (last_modified 2026-05-15 19:30 UTC pre-window) |
| Volexity (RSS) | XML parse error | n/a — second consecutive parse error; flag for source-health |
| SANS ISC (RSS) | OK | 0 |
| Rapid7 (RSS) | OK | 0 (last_modified 2026-05-16 19:16 UTC = 15:16 EDT inside window from feed-server activity but no new posts published) |
| SecurityWeek (RSS) | OK | 0 (last_modified 2026-05-16 12:45 UTC = 08:45 EDT inside window from feed-server activity but no new posts since AM sweep NGINX Rift PoC item — that was already raw-2026-05-16-flash-0600-001) |
| Bitdefender Labs (RSS) | 404 again | n/a — third consecutive failure this sweep; path-changed; flag for source-health |
| Industrial Cyber (RSS) | 403 again | n/a — bot-block persistent; flag for source-health |
| Symantec security.com (RSS feed path) | 404 | n/a — feed path broken; **but index-page WebFetch productive** — surfaced "Fast16: Pre-Stuxnet Sabotage Tool" 2026-05-16 (see raw-2026-05-16-pm-001) |
| Wiz Research (RSS) | 404 again | n/a — second consecutive; path may have moved |
| Snyk (RSS) | OK | 0 |
| Socket (RSS) | 404 | n/a — second consecutive |
| Darktrace (RSS) | OK | 0 (last_modified 2026-05-16 00:51 UTC pre-window) |
| Check Point Research (RSS) | OK | 0 (last_modified 2026-05-14 13:56 UTC pre-window) |
| Cybersecurity Dive (RSS) | OK | 0 (last_modified 2026-05-15 15:20 UTC pre-window) |
| ZDI Pwn2Own (blog RSS) | OK | **0 net-new** in 8h window — index-page WebFetch confirms top-5 unchanged from morning sweep (Day Three / Day Two / Day One / Schedule / May 2026 Patch Tuesday Review); Day 3 wrap was AM-001 |
| CrowdStrike (RSS) | OK | 0 in-window dated items — same 10 dateless marketing / MQ / SPIDER-product-marketing items as the morning sweep saw; pattern fully entrenched (now ~14 consecutive sweeps with no dated threat-intel content) |
| nitter.net @CISAgov (RSS) | OK | 1 — "A week powered by regional teamwork" 14:56 UTC promotional video; **NO security signal**; DISCARDED per Mode 1 procedure |
| F5 K000160932 (WebFetch) | CSS load error (dynamic page) | n/a — known F5-manage dynamic-portal quirk; primary content already captured in finding-2026-05-14-0002 |
| Shodan / Internet DB | Not invoked | No in-window CVE / IOC required Shodan enrichment |
| Splunk defenseclaw_local | OK | 0 events last 24h — **32nd consecutive dormant non-self-telemetry sweep** |
| Splunk archimedes | OK | 7 self-telemetry events last 24h (4 archimedes:operation + 3 archimedes:scheduler) — internal heartbeat only; targeted IOC keyword sweep across 16 tracked actor + 7 tracked CVE tokens returned 7 hits, ALL archimedes:operation pipeline self-references (this morning's brief publish/commit, 11:30 FLASH sweep operation, finding promotions / rejections from morning grader run, 2026-05-15 afternoon brief publish) |

Total sources queried: 33
Sources OK with in-window content matching filters: 1 (Symantec Fast16 historical-research via security.com index-page WebFetch)
Sources OK with in-window content discarded per Mode 1 filter: 3 (BleepingComputer Turla relay duplicate-locked, THN Funnel Builder WP commodity skimmer, nitter CISA promo video)
Sources with parse / fetch errors: 7 (Sophos × 2 = at-threshold, Volexity × 2, Bitdefender × 3, Industrial Cyber × 2, Symantec feed-path, Wiz × 2, Socket × 2 — none load-bearing)

## Raw signals written this run

1. **raw-2026-05-16-pm-001-symantec-fast16-pre-stuxnet-nuclear-simulation-sabotage.md**
   - Symantec Threat Hunter Team + Carbon Black publishes "Fast16: Pre-Stuxnet Sabotage Tool Was Built to Subvert Nuclear Weapons Simulations" (security.com/threat-intelligence/fast16-nuclear-sabotage, date 2026-05-16, 8-min read)
   - Historical-research forensic-archaeology piece on a 2005-era simulation-sabotage framework
   - Target software: **LS-DYNA + AUTODYN** (both widely deployed in A&D engineering — finite-element / hydrocode tools for blast / impact / weapon-effects modeling at every US defense prime)
   - Builds on SentinelLABS April 2026 originating research (`fast16.sys`, `svcmgmt.exe`, Lua VM, LS-DYNA 970 / PKPM / MOHID)
   - Symantec adds AUTODYN to the target set; does NOT adopt SentinelLabs' PKPM / MOHID naming
   - Attribution: NONE — no nation-state, no actor, hedged "All evidence suggests that attackers were specifically targeting simulations of nuclear detonations"
   - Active exploitation: NONE claimed — Symantec: "We do not know if a modern-day version of fast16 exists"
   - IOCs: NONE published (no hashes, no C2, no IPs)
   - CVEs: NONE
   - NOT a FLASH candidate (0 of 6 triggers fire); routes to afternoon brief regular flow as A&D-sector-adjacent historical research

## Carry-forward items from prior cycles — status check

Per orchestrator instructions, these were checked for NEW reporting in the 8h afternoon window:

1. **NGINX Rift PoC publication (CVE-2026-42945)** — NO new exploitation reporting in window. SecurityWeek feed had no fresh NGINX Rift content beyond the morning AM-coverage. F5 K000160932 page unreachable via WebFetch (dynamic-portal CSS-load quirk, expected). Anti-noise lock active. **No new raw signal.**

2. **CVE-2026-42897 KEV addition (Microsoft Exchange)** — Verified KEV JSON: still most-recent entry; **T-13 today**. No new MSRC reporting in window. No exploitation-status-change signal. Anti-noise active. **No new raw signal.**

3. **Pwn2Own Berlin Day 2 Exchange chain (Orange Tsai / DEVCORE, embargoed)** — ZDI blog index unchanged from morning sweep (Day 3 wrap was AM-001). Day 2 Exchange chain still embargoed; no embargo-lift signal in window. Anti-noise active. **No new raw signal.**

4. **node-ipc compromise (UNATTRIBUTED, 4-firm consensus)** — Socket / Wiz / Bitdefender Labs all 404 again. No new vendor research reaching us. Anti-noise active. **No new raw signal.**

5. **Cisco SD-WAN CVE-2026-20182 T-1** — Federal deadline dueDate 2026-05-17 = **T-1 tomorrow (Sunday)**. KEV catalog unchanged. No new exploitation reporting in window. Briefer should retain in T-1 watch position; Monday morning brief may surface compliance-status indicators if CISA publishes Q2 metrics. **No new raw signal.**

6. **Turla / Kazuar P2P botnet (MSTIC A1)** — BleepingComputer Bill Toulas 10:15 EDT post is pure relay (verified via WebFetch — cites MSTIC primary, no new IOCs, no new victims, no narrower attribution). THN morning relay was already rejected as reject-2026-05-16-0001. `turla-kazuar-relay` anti-noise lock active. **No new raw signal** (duplicate-locked).

## FLASH-shape candidates the grader should fast-path

**None.** Symantec Fast16 is the only in-window net-new raw signal; it routes to afternoon brief regular flow as a historical-research / sector-adjacent awareness item. NOT a FLASH candidate (0 of 6 triggers fire).

## Source-health changes proposed

All non-load-bearing this sweep; A-grade primary set returned cleanly via WebFetch fallbacks where direct RSS failed:

- **sophos**: Second consecutive 404 on news.sophos.com/en-us/feed/. failure_count 1→2 (at stale threshold). HOLDING healthy this sweep per oscillation discipline; next consecutive failure trips stale per >=2-failure rule. Recommend operator path re-discovery (root feed path or alternate /en-us/feed/ endpoint).
- **volexity**: Second consecutive XML parse error. failure_count 1→2 (at stale threshold). HOLDING healthy; next consecutive failure trips stale.
- **bitdefender**: Third consecutive 404. failure_count 2→3 (PAST stale threshold). Recommend stale flip on next pass; index-page WebFetch fallback works for content but flag for operator path re-discovery.
- **industrialcyber-co**: Bot-block 403 persistent. failure_count carries from morning sweep increment.
- **wiz-research / socket**: Second consecutive 404 each. failure_count 1→2 each (at threshold).
- **symantec** (RSS feed path 404): Index-page WebFetch fallback works, surfaced today's Fast16 piece productively. Feed path flagged for operator re-discovery.

None of these are load-bearing for the afternoon brief: CISA / Splunk / BleepingComputer / The Record / THN / SecurityWeek / Mandiant index / Talos / Securelist / WLS / SentinelLabs / SANS ISC / Rapid7 / Snyk / Darktrace / CP Research / Cybersecurity Dive / ZDI all returned cleanly. Symantec content captured via index-page WebFetch fallback.

## Splunk first-party detail

`(index=archimedes OR index=defenseclaw_local) NOT sourcetype=archimedes:* earliest=-24h` → **0 events**.

Targeted IOC keyword sweep across 16 tracked actors (UNC1549 / Charming Kitten / MuddyWater / Turla / Kazuar / Salt Typhoon / APT28 / APT29 / APT37 / Volt Typhoon / APT41 / Lazarus / Mustang Panda / FamousSparrow / TeamPCP / Mandiant / Symantec / Bitdefender) over 24h returned 7 hits — ALL `archimedes:operation` pipeline self-references (this morning's brief publish/commit, 11:30 FLASH operation, finding promotions / rejections, 2026-05-15 afternoon brief publish).

Targeted CVE sweep across 7 tracked CVEs (CVE-2026-42945 / CVE-2026-42897 / CVE-2026-20182 / CVE-2026-45321 / CVE-2026-0300 / CVE-2026-46300 / CVE-2026-42208) over 24h returned 7 hits — same set, all archimedes-operation pipeline self-references.

**32nd consecutive dormant non-self-telemetry sweep** carrying forward the streak:
- 28th: 0d1debe (2026-05-16 00:00 sweep)
- 29th: d2560d4 (2026-05-16 06:00 sweep)
- 30th: 3cc6118 (2026-05-16 08:00 morning brief)
- 31st: 9bc608f (2026-05-16 11:30 on-demand FLASH)
- 32nd: **this sweep (2026-05-16 15:30 pre-brief)**

## Conclusion

**Quiet Saturday afternoon sweep**, 1 raw signal written (Symantec Fast16 historical-research, A&D-sector-adjacent via LS-DYNA + AUTODYN simulation-toolchain target set, NOT a FLASH candidate), **0 FLASH candidates for grader fast-path**, **32nd consecutive dormant non-self-telemetry Splunk sweep**. All 6 carry-forward items checked; no exploitation news; no embargo lifts; no surprise vendor disclosures beyond Symantec's Fast16 follow-on to SentinelLabs' April 2026 originating research.

The Fast16 piece is the natural anchor for the afternoon brief's "Sector Focus: Aerospace & Defense" standing section — a structural-supply-chain awareness note on simulation-toolchain integrity (LS-DYNA / AUTODYN deployed across every US defense prime). Briefer's call on weight / placement; recommend NOT leading with it (no urgent action) but treating as the substantive sector-section content for an otherwise quiet Saturday.
