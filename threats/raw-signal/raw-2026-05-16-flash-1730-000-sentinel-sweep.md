---
raw_id: raw-2026-05-16-flash-1730-000
collected_at: 2026-05-16T18:02:00-04:00
run_id: flash-sweep-20260516-173000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (on-demand, post-afternoon-brief)"
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
  - dormant_splunk_sweep_33
  - on_demand_post_pm_brief
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-14T18:02:00-04:00
---

# FLASH sweep 2026-05-16 17:30 EDT (on-demand, post-afternoon-brief) — CLEAN

## Sweep summary

**Mode:** flash_sweep (on-demand, invoked between afternoon brief 16:00 EDT and 18:00 EDT scheduled sweep window)
**Window:** 2026-05-16T15:30:00-04:00 → 2026-05-16T18:02:00-04:00 (~2.5h; effectively the post-afternoon-brief gap)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation.

## Sources queried (active A-grade priority set)

- CISA all.xml (`cisa-advisories`) — reachable, 0 in-window items.
- CISA KEV JSON (`cisa-kev`) — 5 most recent additions confirmed: CVE-2026-42897 (Exchange OWA XSS, 2026-05-15, due 2026-05-29 / T-13), CVE-2026-20182 (Cisco Catalyst SD-WAN, 2026-05-14, due 2026-05-17 / T-1 Sunday), CVE-2026-42208 (LiteLLM, 2026-05-08), CVE-2026-6973 (Ivanti EPMM, 2026-05-07), CVE-2026-0300 (PAN-OS, 2026-05-06). **Zero KEV additions dated 2026-05-16.** All within carry-forward state per afternoon brief.
- The Hacker News (`thehackernews`) — reachable, 0 in-window items.
- BleepingComputer (`bleepingcomputer`) — reachable, **1 in-window item** evaluated and DISCARDED (see below).
- Krebs on Security (`krebs`) — reachable, 0 in-window items.
- The Record (`the-record`) — reachable, 0 in-window items.
- SecurityWeek (`securityweek`) — reachable, 0 in-window items.
- Unit 42 feedburner (`unit42`) — reachable, 0 in-window items.
- Microsoft Security Blog parent feed (`mstic`) — reachable, 0 in-window items.
- WeLiveSecurity (`eset`) — reachable, 0 in-window items.
- SentinelLabs (`sentinelone`) — reachable, 0 in-window items.
- SANS ISC (`sans-isc`) — reachable, 0 in-window items.
- Cisco Talos (`cisco-talos`) — feed endpoint blog.talosintelligence.com/feeds/posts/default 404 this sweep (transient; not marking stale this single failure).
- Sophos (`sophos`) — feed endpoint news.sophos.com/en-us/feed/ 404 this sweep (transient; not marking stale this single failure).
- Mandiant feedburner (`mandiant`) — known broken (20th+ consecutive 404), skipped per source-health.
- Dragos (`dragos`) — known broken (`/blog/feed/` 404), skipped per source-health.
- Ars Technica security (`ars-security`) — known stale, skipped.

## Splunk self-telemetry sweep

`index=archimedes OR index=defenseclaw_local earliest=-24h` — **34 events total**, all in self-telemetry sourcetypes (`archimedes:operation` = 18 events, `archimedes:scheduler` = 16 events). **Zero non-self-telemetry events.** This is the **33rd consecutive dormant non-self-telemetry Splunk sweep** since the corpus began tracking the cadence. Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml` (132 tracked indicators).

## Single in-window item evaluated and discarded

**BleepingComputer (Ax Sharma, 2026-05-16T20:55 UTC = 16:55 EDT): "Microsoft rejects critical Azure vulnerability report, no CVE issued"**

- Topic: Confused-deputy privilege-escalation vulnerability in Azure Backup for AKS (Azure Kubernetes Service); researcher dispute with Microsoft over CNA-hierarchy-blocked CVE assignment; CERT/CC issued VU#284781 before closing case under CNA rules.
- Trigger 1 (Critical CVE exploited): **FAIL** — no CVE assigned (Microsoft blocked CVE issuance via CNA hierarchy); no active exploitation in the wild claimed.
- Trigger 2 (New tracked actor attribution): **FAIL** — no threat actor named.
- Trigger 3 (First-party IOC hit): **FAIL** — Splunk dormant sweep #33; no IOCs in article.
- Trigger 4 (Tracked actor TTP change): **FAIL** — no actor.
- Trigger 5 (A&D sector campaign): **FAIL** — no A&D / aerospace / defense targeting; vulnerability class is generic Azure RBAC↔Kubernetes-RBAC trust-boundary, not sector-targeted.
- Trigger 6 (Zero-day no patch): **FAIL** — Microsoft claims silently fixed (researcher disputes — "no product changes were made" is Microsoft's framing while researcher documents a silent fix); no exploitation confirmed or imminent per A-grade source; the disclosure dispute is a CNA-policy story, not an active-threat story.
- Disposition: **DISCARDED** per Mode 2 procedure (no FLASH trigger). Item may be picked up by the grader on tomorrow's morning brief as a coverage-gap / disclosure-process item if the operator prioritizes it; it is NOT FLASH-eligible.

## Carry-forwards preserved (NOT re-triggered)

- **CVE-2026-20182** (Cisco Catalyst SD-WAN auth bypass, CVSS 10.0, KEV T-1 Sunday 2026-05-17) — in afternoon brief; T-1 calendar position unchanged.
- **CVE-2026-42897** (Microsoft Exchange OWA XSS, KEV T-13 due 2026-05-29) — in afternoon brief.
- **Symantec / Carbon Black + SentinelLABS April 2026 Fast16 framework** (2005-era pre-Stuxnet simulation-sabotage targeting LS-DYNA + novel AUTODYN addition; A2 cluster anchor; no actor / no IOCs / no active exploitation) — finding-2026-05-16-0003 in afternoon brief; provisional-A Symantec ratification clock T-2h25m queued for operator pass (clock at 2026-05-16T18:25:00-04:00 from corpus framing).
- **CVE-2026-42945 NGINX Rift PoC** (depthfirst GitHub) + Pwn2Own Berlin 2026 closure ($943,250 / 42 zero-days) — morning brief carry-forwards.
- **Turla/Kazuar D+2 relay layer** (BleepingComputer + The Hacker News duplicate-locked against finding-2026-05-14-0006 / reject-2026-05-16-0001) — anti-noise rule active.

## Source health observations (this sweep)

- `cisco-talos`: blog.talosintelligence.com/feeds/posts/default returned 404 on this single sweep. Insufficient to mark stale (rule requires >=2 consecutive failures). Held healthy pending next sweep retry. Operator may wish to verify the canonical Talos blog RSS path on a future maintenance pass.
- `sophos`: news.sophos.com/en-us/feed/ returned 404 on this single sweep. Same treatment — held healthy pending next sweep retry.
- All other queried sources: reachable, zero in-window items.

## Disposition

**Clean sweep, 0 FLASH triggers fired, 33rd consecutive dormant non-self-telemetry Splunk sweep, no escalation, no Discord post.** Carry-forwards unchanged from afternoon brief. The 18:00 EDT scheduled FLASH sweep window will conduct an independent re-check ~30 minutes from this sweep's close.
