---
raw_id: raw-2026-05-15-am-000
collected_at: 2026-05-15T07:32:00-04:00
run_id: pre-brief-20260515-073000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-15T07:30:00-04:00
time_window_start: 2026-05-14T17:30:00-04:00
time_window_end: 2026-05-15T07:30:00-04:00
window_hours: 14
test: false
sentinel: true
source:
  source_yaml_id: archimedes-internal
  source_name: Archimedes collector
  source_url: null
  published_at: 2026-05-15T07:30:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sentinel, sweep_summary, brief_update_candidates, anti_noise_carry_forward]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promotion_disposition: non_promotable_sentinel_tombstone_no_grading_required
graded_at: 2026-05-15T08:05:00-04:00
graded_by: grader
grading_run_id: morning-20260515-080000
graded_disposition_rationale: "Sentinel tombstone summarizes the AM sweep — operational audit-trail artifact, not a substantive raw-signal candidate for grading. The 1 substantive in-window item it references (am-001 Cisco SD-WAN sixth-zero-day editorial pattern) was graded individually under this same grading run and promoted to finding-2026-05-15-0002. The two earlier FLASH raw-signals it references (flash-0600-001 MSRC Exchange CVE-2026-42897 and flash-0600-002 TeamPCP Shai-Hulud source-code release + BreachForums challenge) were already promoted under the flash-grade-20260515-060000 run to finding-2026-05-15-FLASH-0001 and finding-2026-05-15-FLASH-0002. The yesterday-22:00 FLASH raw-signal (flash-2200-001 TeamPCP Mistral AI 450 repos sale) was graded individually under this same morning run and promoted to finding-2026-05-15-0001. Sentinel is retained per 90-day raw-signal retention policy for audit-trail completeness but not promoted to a finding."
ttl_expires_at: 2026-08-13T07:32:00-04:00
---

# Pre-brief collection sweep — 2026-05-15 07:30 EDT (sentinel)

Sweep window: **2026-05-14 17:30 → 2026-05-15 07:30 EDT (14h)**.

## Headline disposition

**Two FLASH-triggered candidates were already raw-signaled at the 06:00 FLASH sweep and remain in queue for 09:00 post-quiet-hours processing:**

1. **raw-2026-05-15-flash-0600-001** — MS Exchange CVE-2026-42897 zero-day, MSRC self-disclosure, exploitation detected, no general-availability patch (ESU-only). Trigger 6 + Trigger 1.
2. **raw-2026-05-15-flash-0600-002** — TeamPCP releases Shai-Hulud worm source code on GitHub + BreachForums "supply chain challenge" bounty. Trigger 4 + Trigger 2.

Plus the **2026-05-14 22:00 FLASH** raw-signal (raw-2026-05-14-flash-2200-001) which captured TeamPCP advertising ~5GB / ~450 Mistral AI repos for sale ($25K BIN, one-week leak deadline) — non-FLASH but strong brief-update candidate.

**Anti-noise window:** all three items remain LIVE for the 08:00 morning brief; the grader / briefer should treat them as the brief's headline cluster.

## In-window items collected this 07:30 sweep

One **NEW brief-update candidate** raw-signaled:

- **raw-2026-05-15-am-001** — SecurityWeek (Eduard Kovacs) Cisco SD-WAN editorial extending PM-001 / CVE-2026-20182 picture with the "Sixth exploited in 2026" pattern: 5-of-15 KEV-catalog SD-WAN CVEs are from 2026 + CVE-2022-20775 also exploited in 2026 + Talos has observed 10 activity clusters exploiting SD-WAN vulnerabilities for crypto-miners / credential-stealers / backdoors / webshells. Editorial pattern-context, not a new attribution. ANTI-NOISE applies to the underlying CVE-2026-20182 / UAT-8616 facts; the EDITORIAL pattern-context is new and worth surfacing for briefer awareness.

All other in-window items DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit) or ANTI-NOISE (already covered in yesterday's afternoon brief / today's 06:00 FLASH / yesterday's 22:00 FLASH):

| Item | Source | Disposition |
|---|---|---|
| MS Exchange CVE-2026-42897 zero-day | BleepingComputer, THN | ANTI-NOISE (already at raw-2026-05-15-flash-0600-001) |
| TeamPCP releases Shai-Hulud source code | SecurityWeek, BleepingComputer | ANTI-NOISE (already at raw-2026-05-15-flash-0600-002) |
| OpenAI hit by TanStack supply chain attack | SecurityWeek (Ionut Arghire, 10:37 EDT) | ANTI-NOISE (already at PM-004 / finding-2026-05-14-0008, 24h lockout to 2026-05-15 16:00 EDT) |
| Cisco SD-WAN sixth zero-day editorial | SecurityWeek (Eduard Kovacs, 06:28 EDT) | RAW-SIGNALED as am-001 (pattern-context editorial extending PM-001) |
| Chrome 148 critical patches | SecurityWeek (Ionut Arghire, 07:25 EDT) | DISCARD Mode 1 (no actor / no A&D / no ITW exploitation cited) |
| CISA Adds Cisco SD-WAN CVE-2026-20182 to KEV | The Hacker News (05:28 EDT) | ANTI-NOISE (covered in PM-001 + KEV catalog already evaluated) |
| American Lending Center data breach | SecurityWeek (Eduard Kovacs, 11:06 EDT) | DISCARD Mode 1 (financial services late-report, no A&D, no actor, ransomware from ~1y ago) |
| Gremlin Stealer evolved tactics | Unit 42 (Chhaparwal + Lim, 10:00 EDT) | DISCARD Mode 1 (commodity infostealer, no actor attribution, no A&D, no tracked CVE) |
| TeamPCP Mistral AI repos for sale | BleepingComputer (Ionut Ilascu, 18:50 EDT yesterday) | ANTI-NOISE (already at raw-2026-05-14-flash-2200-001, brief-update candidate for AM brief) |
| Guest Diary: New Malware Libraries means New Signatures | SANS-ISC (06:38 EDT) | DISCARD Mode 1 (defensive diary, no actor / no IOC / no A&D) |
| ISC Stormcast podcast | SANS-ISC (04:10 EDT) | DISCARD Mode 1 (podcast index, no body) |
| CrowdStrike feed | CrowdStrike | DISCARD Mode 1 (~23rd consecutive sweep of dateless marketing/MQ rotation; no fresh threat-research) |

## Source health observations

**Healthy and productive this sweep:**
- bleepingcomputer (2 items in window, both anti-noise or already-FLASH-queued)
- securityweek (5 items in window; 1 raw-signaled as am-001, 4 anti-noise or discarded)
- thehackernews (2 items in window, both anti-noise)
- unit42 (1 item in window, discarded Mode 1)
- sans-isc (2 items in window, both discarded Mode 1)
- cisa-kev (KEV catalog re-checked; CVE-2026-20182 confirmed added 2026-05-14, dueDate 2026-05-17 = 3-day window; CVE-2026-31431 Copy Fail dueDate 2026-05-15 = **TODAY**)
- cisa-advisories all.xml (0 items in 14h window after since-filter; last entry pre-window)
- krebs (0 items in window, normal cadence)
- the-record (0 items in window, normal cadence)
- mstic / microsoft security blog parent feed (0 items in 14h window — last_modified 2026-05-14T21:51 GMT pre-window; PM-002 Kazuar post from 11:00 EDT yesterday already absorbed)
- crowdstrike (10 items all dateless marketing, ~24th consecutive sweep of this pattern)
- unit42 (1 in-window post Gremlin Stealer, discarded)
- sentinelone labs (0 items, last_modified 2026-05-14T20:22 GMT pre-window)
- sophos news (0 items in window)
- rapid7 (0 items in window — last_modified 2026-05-15T11:17 GMT but no items after since-filter)
- welivesecurity / ESET (0 items in window)
- talos blog (0 items in window — last_modified header missing)
- darktrace (0 items in window after since-filter)
- snyk (0 items)
- wired security (0 items)

**Soft-fail observations (held healthy, no failure_count incrementation this sweep):**
- mandiant: feedburner.com/Mandiant 404 again — **twenty-third consecutive** (failure_count 20→21). Pattern fully entrenched; operator alt-endpoint decision still pending.
- bitdefender labs feed 404 (consistent with yesterday — RSS path retired; index-page WebFetch remains the productive surface).
- symantec enterprise blogs feed 404 (consistent with yesterday — security.com/threat-intelligence index-page WebFetch remains the productive surface).
- industrialcyber.co/feed/ 403 Forbidden (WAF/Akamai bot-block pattern — not a connectivity failure, no failure_count increment; held healthy from yesterday's first-fetch).
- socket.dev/blog/rss.xml 404 (no RSS path identified; vendor surfaces via The Hacker News / SecurityWeek relays).

**Stale-skipped this sweep (under-24h or persistent-stale rules):**
- ars-security (feed retired, workaround in use)
- x-cisagov (nitter bridge fragility, stale since 2026-05-10)
- x-gossithedog (nitter account delisted, stale since 2026-05-09)
- hibp, censys, urlscan (no MCP / no key)

**Splunk first-party observations:**
- splunk-archimedes + splunk-defenseclaw_local: combined NOT sourcetype=archimedes:* over 24h returns **zero** non-archimedes-internal events. Targeted IOC keyword sweep across 18 tokens (CVE-2026-42897, CVE-2026-20182, CVE-2026-31431, Exchange, Catalyst, SD-WAN, TeamPCP, Shai-Hulud, Mistral, TanStack, UAT-8616, Secret Blizzard, Kazuar, Twill Typhoon, FrostyNeighbor, UNC1151, Salt Typhoon, FamousSparrow) returned **3 hits** — all archimedes:operation pipeline self-references (yesterday's FLASH cycles + today's 06:00 FLASH self-emissions). **24th consecutive sweep** with dormant non-archimedes-internal stream. Trigger 3 (first-party-ioc-hit) cannot fire on a dormant non-archimedes-internal stream.

## Carry-forward state for the 08:00 morning brief

1. **CVE-2026-42897 MS Exchange zero-day** — primary FLASH candidate. Quiet-hours queued at 06:00; ripe for 09:00 EDT post-quiet-hours processing OR fold into morning brief as the headline finding.
2. **TeamPCP Shai-Hulud worm source-code release + BreachForums "supply chain challenge"** — secondary FLASH candidate. Same quiet-hours queue logic. TTP change (Trigger 4) for tracked-actor #001.
3. **TeamPCP Mistral AI 450-repo sale + OpenAI TanStack continuation** — non-FLASH brief-update candidate. Cluster with #2 above as the multi-day TeamPCP / Mini Shai-Hulud / TanStack campaign continuation.
4. **CVE-2026-20182 Cisco SD-WAN (UAT-8616)** — KEV deadline T-2 days (2026-05-17). Brief-update via am-001 editorial pattern-context.
5. **CVE-2026-31431 "Copy Fail" Linux Kernel** — KEV deadline **TODAY (2026-05-15)**. Brief-update reminder for the federal-deadline calendar — no fresh research-content this window.

## Notes on /new-actor candidates surfaced earlier this week (status carry-forward)

- **Secret Blizzard / Turla / VENOMOUS BEAR** (raw-2026-05-14-pm-002) — high-priority /new-actor candidacy flag from yesterday afternoon. Operator decision pending.
- **Twill Typhoon / Mustang Panda / TA416** (raw-2026-05-14-pm-003) — medium-priority /new-actor candidacy flag from yesterday afternoon. Operator decision pending.
- **FrostyNeighbor / Ghostwriter / UNC1151** (raw-2026-05-14-am-001 + earlier finding-2026-05-08-0009) — medium-priority /new-actor candidacy flag, second corpus surface in 6 days. Operator decision pending.
- **UAT-8616** (raw-2026-05-14-pm-001 + this sweep's am-001 editorial) — observed-cluster, NOT yet promoted to roster; Talos does not nation-attribute. Operator decision: track as cluster only, defer roster promotion until additional A-grade cluster-identity corroboration surfaces.

---

## Extraction notes

- Language: en
- Sentinel raw-signal for the 07:30 pre-brief sweep
- Article type: sweep summary
- Raw IOC extraction invoked: no (sentinel — no source content)
