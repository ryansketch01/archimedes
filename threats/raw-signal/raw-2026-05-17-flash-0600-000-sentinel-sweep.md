---
raw_id: raw-2026-05-17-flash-0600-000
collected_at: 2026-05-17T06:03:00-04:00
run_id: flash-sweep-20260517-060000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (scheduled, 06:00 EDT window)"
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
  - scheduled_0600_window
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-15T06:03:00-04:00
---

# FLASH sweep 2026-05-17 06:00 EDT (scheduled) — CLEAN

## Sweep summary

**Mode:** flash_sweep (scheduled 06:00 EDT window)
**Window:** 2026-05-17T00:00:00-04:00 → 2026-05-17T06:03:00-04:00 (~6h gap since prior 00:00 scheduled FLASH sweep commit d369efd, which itself was clean)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post (quiet hours active in any event — would have queued not posted).
**Quiet-hours state:** ACTIVE (06:03 EDT is pre-09:00 active-window threshold per FLASH-POLICY.md). Critical-override conditions NOT met (no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity coincidence).

## Sources queried (active A-grade priority set)

- CISA all.xml (`cisa-advisories`) — reachable (200), 0 in-window items.
- CISA KEV JSON (`cisa-kev`) — top entries unchanged: CVE-2026-42897 (Exchange OWA XSS, dateAdded 2026-05-15, due 2026-05-29 / T-12d), CVE-2026-20182 (Cisco Catalyst SD-WAN, dateAdded 2026-05-14, due 2026-05-17 / **T-0 today**), CVE-2026-42208 (LiteLLM, 2026-05-08), CVE-2026-6973 (Ivanti EPMM, 2026-05-07), CVE-2026-0300 (PAN-OS, 2026-05-06), CVE-2026-31431 (Linux Kernel, 2026-05-01), CVE-2026-41940 (WebPros cPanel & WHM, 2026-04-30 — Known ransomware use), CVE-2024-1708 (ConnectWise ScreenConnect, 2026-04-28 — Known ransomware use). **Zero KEV additions dated 2026-05-16 or 2026-05-17.** All within carry-forward state.
- The Hacker News (`thehackernews`) — reachable (200), **1 in-window item** evaluated and DISCARDED (see below).
- BleepingComputer (`bleepingcomputer`) — reachable (200), 0 in-window items (top item is 2026-05-16T20:55 UTC = 16:55 EDT Azure CVE-rejection already discarded in prior 17:30 sweep; second item is 2026-05-16T14:15 UTC = 10:15 EDT Kazuar/Secret Blizzard relay duplicate-locked against finding-2026-05-14-0006 / reject-2026-05-16-0001).
- Krebs on Security (`krebs`) — reachable (200), 0 in-window items.
- The Record (`the-record`) — reachable (200), 0 in-window items.
- SecurityWeek (`securityweek`) — reachable (200), 0 in-window items (last-modified 2026-05-16 12:45 UTC).
- Unit 42 feedburner (`unit42`) — reachable (200), 0 in-window items (last-modified 2026-05-15 19:46 UTC).
- Microsoft Security Blog parent feed (`mstic`) — reachable (200), 0 in-window items (last-modified 2026-05-14 21:51 UTC).
- WeLiveSecurity (`eset`) — reachable (200), 0 in-window items.
- SentinelLabs (`sentinelone`) — reachable (200), 0 in-window items (last-modified 2026-05-15 19:30 UTC).
- SANS ISC (`sans-isc`) — RSS endpoint `rssfeed.xml` parse error this sweep (second failure of same class; first 2026-05-12; not yet triggering stale threshold as prior recovery pattern is established). Diary archive WebFetch surfaced most-recent entry 2026-05-15 (Gokul Prema Thangavel "[Guest Diary] New Malware Libraries means New Signatures"). No 2026-05-16 or 2026-05-17 entries. Source held healthy.
- Cisco Talos (`cisco-talos`) — RSS endpoint blog.talosintelligence.com/feeds/posts/default 404 this sweep (second consecutive failure; first 2026-05-16 17:30 sweep — failure_count increments 0→1 on this sweep). Blog index page WebFetch reachable, latest post 2026-05-14 12:02 ("Ongoing exploitation of Cisco Catalyst SD-WAN vulnerabilities" — already in finding-2026-05-14-0005 carry-forward chain). No 2026-05-16 or 2026-05-17 posts. Held healthy on the WebFetch alt-path; recommend operator note for RSS-path review.
- Sophos (`sophos`) — RSS endpoint news.sophos.com/en-us/feed/ 404 this sweep (second consecutive failure; first 2026-05-16 17:30 sweep — failure_count increments 0→1 on this sweep). Blog index reachable via WebFetch (301 redirect to www.sophos.com/en-us/blog?taxonomy_blog_category=Threat+Research/); no dates surfaced on the index page (consistent prior observations). Held healthy on the WebFetch alt-path; recommend operator note for RSS-path review.
- Mandiant feedburner (`mandiant`) — known broken (~20 consecutive 404s; failure_count 18), skipped per source-health.
- Dragos (`dragos`) — known broken (`/blog/feed/` 404), skipped per source-health.
- Ars Technica security (`ars-security`) — known stale (status: stale since 2026-05-09), skipped per source-health.
- X / RSSHub bridges (`x-cisagov`, `x-gossithedog`) — rsshub.app 404 again this sweep (consistent prior failures; public RSS bridge fragility). Held in expected-broken state.

## Splunk self-telemetry sweep

`index=archimedes OR index=defenseclaw_local earliest=-24h` — **34 events total**, all in self-telemetry sourcetypes (`archimedes:operation` = 18 events, `archimedes:scheduler` = 16 events). **Zero non-self-telemetry events.** This is the **34th consecutive dormant non-self-telemetry Splunk sweep** since the corpus began tracking the cadence. Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`.

## Single in-window item evaluated and discarded

**The Hacker News (2026-05-17T07:13 UTC = 03:13 EDT): "Grafana GitHub Token Breach Led to Codebase Download and Extortion Attempt"**

- Topic: Grafana disclosed an unauthorized party obtained a GitHub token allowing codebase download; extortion attempt refused per FBI guidance; no customer data / no customer systems affected per Grafana statement.
- Named attribution: **CoinbaseCartel** (a data-extortion group emerging September 2025; THN cites Hackmanac and Ransomware.live as relay sources; "assessed as an offshoot of ShinyHunters, Scattered Spider, and LAPSUS$ ecosystems" — characterized via Halcyon + Fortinet FortiGuard Labs profiling). 170 reported victims across healthcare, technology, transportation, manufacturing, business services.
- **Roster intersect:** Scattered Spider (#013) appears as part of CoinbaseCartel's ecosystem-lineage framing — NOT as direct attribution of the Grafana breach to Scattered Spider. CoinbaseCartel itself is NOT on the roster.

**Trigger evaluation:**

- Trigger 1 (Critical CVE exploited): **FAIL** — no CVE; credential-abuse / past-access incident, not vulnerability exploitation.
- Trigger 2 (New tracked actor attribution): **FAIL** — primary attribution is to CoinbaseCartel (not on roster). Scattered Spider appears only as ecosystem-lineage context (CoinbaseCartel framed as "offshoot of ShinyHunters, Scattered Spider, and LAPSUS$ ecosystems") — this is lineage / parent-cluster framing, NOT direct attribution of the Grafana breach to Scattered Spider operators. Even if treated as ecosystem-association attribution, the cited sources (Hackmanac, Ransomware.live, Halcyon, Fortinet FortiGuard Labs) are not on source-grades.yaml as A-grade for actor-attribution claims, and THN itself is provisional-B (relay layer). Fails the A-grade-source requirement under flash-policy.yaml Trigger 2 conditions. Per Hard Rule 2 (no first-time attribution origination), Archimedes does not propagate the ecosystem-lineage framing as direct Scattered Spider attribution.
- Trigger 3 (First-party IOC hit): **FAIL** — Splunk dormant sweep #34; no IOCs in article.
- Trigger 4 (Tracked actor TTP change): **FAIL** — no tracked-actor TTP change documented (CoinbaseCartel attribution; not on roster).
- Trigger 5 (A&D sector campaign): **FAIL** — Grafana is observability software vendor; not A&D. No A&D-watchlist entity named. CoinbaseCartel's 170-victim profile spans healthcare/technology/transport/manufacturing/business services — no defense sector named. No multi-victim A&D pattern.
- Trigger 6 (Zero-day no patch): **FAIL** — no vulnerability disclosed; credential-abuse / extortion story.
- **Disposition: DISCARDED** per Mode 2 procedure (0 of 6 FLASH triggers fired). Item may be picked up by the grader on this morning's 08:00 brief as a supply-chain-credential-exposure item — Grafana is a widely-deployed observability platform in enterprise IT including A&D-adjacent operations, but no A&D-prime exposure is asserted by the source and Archimedes does not extrapolate. It is NOT FLASH-eligible. Coverage decision deferred to morning brief grader/briefer.

## Carry-forwards preserved (NOT re-triggered)

- **CVE-2026-20182** (Cisco Catalyst SD-WAN auth bypass, CVSS 10.0, KEV **T-0 federal deadline TODAY 2026-05-17**) — in afternoon brief 2026-05-16 16:00 carry-forward chain; KEV deadline arrives today. Calendar-event note for morning brief (08:00) — no new trigger today.
- **CVE-2026-42897** (Microsoft Exchange OWA XSS, KEV T-12d due 2026-05-29) — carry-forward.
- **Symantec / Carbon Black + SentinelLABS April 2026 Fast16 framework** (2005-era pre-Stuxnet simulation-sabotage targeting LS-DYNA + novel AUTODYN; A2 cluster anchor; no actor / no IOCs / no active exploitation) — finding-2026-05-16-0003 carry-forward. Symantec provisional-A 72h ratification clock fired 2026-05-16T18:25 EDT; awaiting operator pass.
- **CVE-2026-42945 NGINX Rift PoC** (depthfirst GitHub) + Pwn2Own Berlin 2026 closure ($943,250 / 42 zero-days) — morning brief 2026-05-16 carry-forwards.
- **Turla / Kazuar / Secret Blizzard D+2 relay layer** (BleepingComputer 2026-05-16T14:15 UTC item duplicate-locked against finding-2026-05-14-0006 / reject-2026-05-16-0001) — anti-noise rule 1 active; same surface re-appearing in BleepingComputer top-feed-position this sweep is the carry-forward duplicate, not a new trigger.

## Source health observations (this sweep)

- `cisco-talos`: blog.talosintelligence.com/feeds/posts/default returned 404 on this sweep — second consecutive failure (first 2026-05-16 17:30 sweep). failure_count increments from baseline 0 to 1. Blog index page WebFetch reachable; latest post 2026-05-14. Held healthy because WebFetch alt-path works and the RSS endpoint may be transient. If a third consecutive failure occurs at 12:00 sweep, mark stale per ≥2-consecutive-failure rule (note: doctrine says ≥2; this is the second — judgment call to hold one more sweep given WebFetch alt-path is verified working). Operator may wish to verify the canonical Talos blog RSS path on a future maintenance pass.
- `sophos`: news.sophos.com/en-us/feed/ returned 404 on this sweep — second consecutive failure (first 2026-05-16 17:30 sweep). failure_count increments from baseline 0 to 1. Blog index page reachable via WebFetch after 301 redirect to www.sophos.com/en-us/blog?taxonomy_blog_category=Threat+Research/. Same hold-healthy treatment as Cisco Talos pending operator review.
- `sans-isc`: rssfeed.xml parse error this sweep (recurrence of the same class as 2026-05-12 transient that recovered next sweep). Diary archive WebFetch alt-path surfaced no in-window items. Held healthy.
- `mandiant`: feedburner.com/Mandiant returned 404 again (~20th consecutive). Carried in expected-broken state per source-health.yaml; no action.
- `dragos`: /blog/feed/ returned 404 again. Carried in expected-broken state per source-health.yaml; no action.
- `ars-security`: stale since 2026-05-09 per source-health.yaml; no action.
- All other queried sources: reachable, zero in-window items.

## Disposition

**Clean sweep, 0 FLASH triggers fired, 34th consecutive dormant non-self-telemetry Splunk sweep, no escalation, no Discord post.** Carry-forwards unchanged. The 08:00 EDT morning brief pipeline will handle: (1) CVE-2026-20182 T-0 KEV deadline calendar-event today, (2) Grafana/CoinbaseCartel item if grader prioritizes for sub-FLASH coverage, (3) Symantec provisional-A ratification status (clock fired ~12h ago), (4) standard carry-forward chain.
