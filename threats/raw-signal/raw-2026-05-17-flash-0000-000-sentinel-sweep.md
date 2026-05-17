---
raw_id: raw-2026-05-17-flash-0000-000
collected_at: 2026-05-17T00:05:00-04:00
run_id: flash-sweep-20260517-000000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (scheduled 00:00 EDT)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - flash_sweep_clean
  - dormant_splunk_sweep_34
  - scheduled_0000
  - quiet_hours_active
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-15T00:05:00-04:00
---

# FLASH sweep 2026-05-17 00:00 EDT (scheduled, quiet hours active) — CLEAN

## Sweep summary

**Mode:** flash_sweep (scheduled 00:00 EDT)
**Window:** 2026-05-16T18:02:00-04:00 → 2026-05-17T00:05:00-04:00 (~6h since close of 17:30 on-demand sweep)
**Quiet hours:** ACTIVE (00:00 EDT falls outside 09:00–21:00 EDT FLASH-POLICY active window). Any FLASH that fired would have been QUEUED to `infrastructure/flash-queue.yaml` for the 09:00 catchup sweep — NOT posted to Discord — unless the critical-override conditions (CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity named) all fired simultaneously.
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Critical override:** Not applicable (no candidate). The known-active CVSS 10.0 carry-forward (CVE-2026-20182 Cisco SD-WAN) does not satisfy the override on its own — no tracked actor (UAT-8616 is Talos-named but NOT in `_roster.yaml`'s 22 tracked actors), and no A&D watchlist entity has been publicly named as a CVE-2026-20182 victim.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post; no queue entry.

## Sources queried (active A/B-grade priority set)

All fetches via `mcp__rss-bridge__fetch_feed` unless noted otherwise; `since=2026-05-16T18:02:00-04:00`:

- CISA all.xml (`cisa-advisories`) — reachable (HTTP 200, 30 items in feed), **0 in-window items**.
- CISA KEV JSON (`cisa-kev`) — direct WebFetch, reachable, 5 most recent additions confirmed unchanged from 17:30 sweep: CVE-2026-42897 (Exchange OWA XSS, 2026-05-15, due 2026-05-29 / T-12d), CVE-2026-20182 (Cisco Catalyst SD-WAN, 2026-05-14, due **2026-05-17 / T-0 today**), CVE-2026-42208 (LiteLLM, 2026-05-08, expired), CVE-2026-6973 (Ivanti EPMM, 2026-05-07, expired), CVE-2026-0300 (PAN-OS, 2026-05-06, expired). **Zero KEV additions dated 2026-05-16 or 2026-05-17.** All within carry-forward state per afternoon brief.
- The Hacker News (`thehackernews`) — reachable (HTTP 200, 50 items in feed), **0 in-window items**. Most recent item (Funnel Builder WordPress plugin, 2026-05-16T15:20 UTC = 11:20 EDT 2026-05-16) is BEFORE window start.
- BleepingComputer (`bleepingcomputer`) — reachable (HTTP 200, 15 items in feed), **0 in-window items**. Most recent items already evaluated in prior sweeps: Microsoft Azure-vuln rejection (2026-05-16T20:55 UTC = 16:55 EDT — discarded in 17:30 sweep) and Turla/Kazuar P2P (2026-05-16T14:15 UTC = 10:15 EDT — duplicate-locked against finding-2026-05-14-0006 / reject-2026-05-16-0001).
- Krebs on Security (`krebs`) — reachable (HTTP 200, 10 items in feed), **0 in-window items**.
- The Record (`the-record`) — reachable (HTTP 200, 5 items in feed), **0 in-window items**.
- SecurityWeek (`securityweek`) — reachable (HTTP 200, 10 items in feed), **0 in-window items**.
- Unit 42 feedburner (`unit42`) — reachable (HTTP 200, 15 items in feed), **0 in-window items**.
- Microsoft Security Blog parent feed (`mstic`) — reachable (HTTP 200, 10 items in feed), **0 in-window items**.
- WeLiveSecurity (`eset`) — reachable (HTTP 200, 100 items in feed), **0 in-window items**.
- SentinelLabs (`sentinelone`) — reachable (HTTP 200, 10 items in feed), **0 in-window items**.
- SANS ISC (`sans-isc`) — reachable (HTTP 200, 10 items in feed), **0 in-window items**.
- Cisco Talos (`cisco-talos`) — feed endpoint `blog.talosintelligence.com/feeds/posts/default` returned **404 (2nd consecutive 404 after 17:30 sweep)**. Not in source-health.yaml as a tracked entry — held healthy for now per implicit-default, but operator may wish to verify the canonical Talos blog RSS path on next maintenance pass. Noted in source health observations below.
- Sophos (`sophos`) — feed endpoint `news.sophos.com/en-us/feed/` returned **404 (3rd consecutive 404 across 07:30 morning + 17:30 on-demand + this 00:00 sweep)**. Meets `failure_count >= 2` stale threshold. Marked stale (see source-health changes below). Operator may verify the canonical Sophos blog RSS path.
- Nitter @CISAgov (`x-cisagov`) — reachable (HTTP 200, 20 items in feed), **0 in-window items**.
- Nitter @GossiTheDog (`x-gossithedog`) — 404 (Nitter instance intermittent — known transient pattern; not marked stale on a single failure).
- Mandiant feedburner (`mandiant`) — known broken (consecutive 404 streak continues), skipped per source-health (stale).
- Dragos (`dragos`) — known broken (`/blog/feed/` 404), skipped per source-health (stale).
- Ars Technica security (`ars-security`) — known stale, skipped per source-health.

## Splunk self-telemetry sweep

`index=archimedes OR index=defenseclaw_local earliest=-24h` — **33 events total**, all in self-telemetry sourcetypes (`archimedes:operation` = 17 events, `archimedes:scheduler` = 16 events). **Zero non-self-telemetry events.** Zero events in `defenseclaw_local`. This is the **34th consecutive dormant non-self-telemetry Splunk sweep** since the corpus began tracking the cadence. Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml` (132 tracked indicators across 7 actors with attributions, plus unattributed clusters).

## Per-trigger evaluation of in-window items

**No in-window items reached evaluation.** All sources either had zero items past the `since` filter or had items that were duplicate-locked from prior sweeps (and thus not re-evaluated per anti-noise Rule 1: "One FLASH per trigger topic per 24 hours"). For completeness, the explicit pass/fail status against the 6 FLASH triggers for the empty in-window set:

- **Trigger 1 (critical-cve-exploited, CVSS ≥9.0 + active exploitation + A-grade source):** FAIL — no in-window item, no new CVE matching threshold. CVE-2026-20182 is already in carry-forward / afternoon-brief coverage; not a new trigger.
- **Trigger 2 (tracked-actor-attribution):** FAIL — no in-window item; no new tracked-actor attribution surfaced. Turla / Kazuar P2P (Secret Blizzard / Turla = NOT in `_roster.yaml`, would not trigger on actor-roster anyway; relay-layer item duplicate-locked against finding-2026-05-14-0006).
- **Trigger 3 (first-party-ioc-hit):** FAIL — Splunk dormant sweep #34; zero non-self-telemetry events; zero IOC matches.
- **Trigger 4 (tracked-actor-ttp-change):** FAIL — no in-window item; no tracked actor.
- **Trigger 5 (ad-sector-campaign):** FAIL — no in-window item; no A&D / aerospace / defense watchlist entity named in any source's recent items.
- **Trigger 6 (zero-day-no-patch):** FAIL — no in-window item; no new zero-day disclosed. CVE-2026-42945 NGINX Rift has both vendor patch (F5 K000160932) and PoC (depthfirst) already in carry-forward coverage; not a new trigger.

## Out-of-window heads-up (NOT in-window; NOT FLASH-eligible this sweep)

The following items appeared in retrieved feed metadata but published BEFORE the 18:02 EDT window start. Documented for situational awareness — the grader will evaluate these on the 2026-05-17 morning brief pre-brief collection (which spans last 14h from 07:30 EDT):

- **Funnel Builder WordPress plugin active-exploitation skimmer** (BleepingComputer 2026-05-15T19:30 UTC = 15:30 EDT 2026-05-15; The Hacker News 2026-05-16T15:20 UTC = 11:20 EDT 2026-05-16). Critical-class plugin vulnerability under active exploitation per Sansec; **no CVE identifier yet assigned**. Even if in-window, would FAIL Trigger 1 (no CVE → cvss_score unknown → cannot meet ≥9.0 threshold), FAIL Trigger 5 (WordPress plugin → not A&D-sector targeting), FAIL Trigger 6 (no zero-day-disclosure framing — vendor patch behavior unclear from headlines). Pre-FLASH disposition: NOT-FLASH-eligible. Grader may pick up on 2026-05-17 morning brief as a coverage item if operator prioritizes WordPress-supply-chain.
- **OpenClaw "Claw Chain" four-flaw chain** (The Hacker News 2026-05-15T13:35 UTC = 09:35 EDT 2026-05-15). Cyera-researched data-theft / privesc / persistence chain. Outside window; outside scope of any tracked actor; non-A&D-sector targeting on initial framing. Pre-FLASH disposition: NOT-FLASH-eligible.

## Carry-forwards preserved (NOT re-triggered, NOT re-evaluated per anti-noise Rule 1)

- **CVE-2026-20182** (Cisco Catalyst SD-WAN auth bypass, CVSS 10.0, **KEV deadline 2026-05-17 = TODAY**) — in afternoon brief; T-0 deadline today. UAT-8616 Talos-attributed active exploitation since 2023 (`high confidence` per finding-2026-05-14-0005). Does NOT satisfy critical-override (UAT-8616 not in `_roster.yaml`; no A&D watchlist victim publicly named).
- **CVE-2026-42897** (Microsoft Exchange OWA XSS, KEV T-12d due 2026-05-29) — in afternoon brief.
- **Symantec / Carbon Black + SentinelLABS April 2026 Fast16 framework** (2005-era pre-Stuxnet simulation-sabotage targeting LS-DYNA + novel AUTODYN addition; A2 cluster anchor; no actor / no IOCs / no active exploitation; provisional-A Symantec) — finding-2026-05-16-0003 in afternoon brief. **Symantec 72h provisional-A ratification clock fired at 2026-05-16T18:25:00-04:00** (just after start of this sweep's window opening 18:02:00); no operator-pass observed within window; clock outcome pending operator review.
- **CVE-2026-42945 NGINX Rift PoC** (depthfirst GitHub) + Pwn2Own Berlin 2026 closure ($943,250 / 42 zero-days) — morning brief carry-forwards.
- **Turla / Kazuar D+2 relay layer** (BleepingComputer 2026-05-16T14:15 UTC + The Hacker News 2026-05-15T17:10 UTC) — anti-noise duplicate-lock active against finding-2026-05-14-0006 / reject-2026-05-16-0001. Both items in retrieved metadata; NOT re-evaluated.

## Source health observations (this sweep)

- **`sophos`** — `news.sophos.com/en-us/feed/` 404 on this 00:00 sweep. Combined with 2026-05-16 07:30 pre-brief failure (recorded in source-health.yaml as `failure_count: 1`) and the 17:30 on-demand-sweep observation (which also got a 404 but did not increment in source-health.yaml), this is the third independent failure cycle. Meets `failure_count >= 2` stale threshold. **Marking stale.** Runtime fields updated; operator `notes`/standing-context fields preserved verbatim per CLAUDE.md "source-health.yaml field ownership."
- **`cisco-talos`** — `blog.talosintelligence.com/feeds/posts/default` 404 on this 00:00 sweep. The 17:30 on-demand sweep also observed a 404. Cisco Talos does NOT have a source-health.yaml entry (the source-grades.yaml `cisco-talos` provisional-A first-cited 2026-05-14 has not yet been bootstrapped into source-health.yaml). Per the operator-only-can-add-source-health-entries doctrine, **not adding a new entry** — documented here for operator visibility, recommending operator add a `cisco-talos` health entry on next maintenance pass with the canonical RSS path verified.
- All other queried sources: reachable (HTTP 200), zero in-window items.

## Disposition

**Clean sweep, 0 FLASH triggers fired, 34th consecutive dormant non-self-telemetry Splunk sweep, no escalation, no Discord post, no queue entry.** Quiet hours active (would have queued not posted in any event). Carry-forwards unchanged from afternoon brief. The 06:00 EDT scheduled FLASH sweep window will conduct an independent re-check ~6h from this sweep's close, with quiet hours still active until the 07:30 EDT pre-brief collection / 08:00 morning brief catchup.
