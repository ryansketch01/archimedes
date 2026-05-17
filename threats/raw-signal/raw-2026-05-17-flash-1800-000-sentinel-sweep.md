---
raw_id: raw-2026-05-17-flash-1800-000
collected_at: 2026-05-17T18:05:00-04:00
run_id: flash-sweep-20260517-180000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (scheduled, 18:00 EDT window)"
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
  - dormant_splunk_sweep_39
  - scheduled_1800_window
  - non_promotable
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promoted_note: "Sentinel tombstone — non-promotable per established precedent (see raw-2026-05-17-flash-0000-000, raw-2026-05-17-flash-0600-000, raw-2026-05-17-flash-1200-000 pattern). One in-window item (DarkReading 'The Boring Stuff is Dangerous Now' opinion essay, dated 2026-05-18 13:00 UTC = inside window from forward-dating but content fails all 6 triggers) evaluated and discarded; no separate raw-signal file written. This sentinel records the sweep decision-trail."
ttl_expires_at: 2026-08-15T18:05:00-04:00
---

# FLASH sweep 2026-05-17 18:00 EDT (scheduled) — CLEAN

## Sweep summary

**Mode:** flash_sweep (scheduled 18:00 EDT window)
**Window:** 2026-05-17T12:00:00-04:00 → 2026-05-17T18:00:00-04:00 (~6h since 12:00 sweep c17bf91, ~2h since 16:00 afternoon brief 005596f)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post (FLASH-POLICY: silent on clean sweep).
**Quiet-hours state:** ACTIVE-WINDOW (18:00 EDT inside 09:00–21:00 EDT active window per FLASH-POLICY.md — had any trigger fired, post to `#flash-alerts` would have been live, not queued). Critical-override conditions NOT met (no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity coincidence).

## Sources queried (active A-grade priority set)

- CISA all.xml (`cisa-advisories`) — reachable (200, 30 items in feed), 0 in-window items after since-filter.
- CISA KEV JSON (`cisa-kev`) — WebFetch confirmed top five most-recent entries are CVE-2026-42897 (2026-05-15, due 2026-05-29), CVE-2026-20182 (2026-05-14, due 2026-05-17 — **federal deadline TODAY EOB, ~6h remaining at sweep time**), CVE-2026-42208 (2026-05-08), CVE-2026-6973 (2026-05-07), CVE-2026-0300 (2026-05-06). **Zero KEV additions dated 2026-05-17.** All within carry-forward state.
- BleepingComputer (`bleepingcomputer`) — reachable (200, last-modified 2026-05-17T21:50 UTC = 17:50 EDT inside window from feed-server activity), 0 in-window items after since-filter.
- The Hacker News (`thehackernews`) — reachable (200, last-modified 2026-05-17T20:54 UTC = 16:54 EDT inside window from feed-server activity, 50 items in feed total), 0 in-window items after since-filter.
- Krebs on Security (`krebs`) — reachable (200), 0 in-window items.
- The Record (`the-record`) — reachable (200), 0 in-window items (5 items total in feed, most recent pre-window).
- SecurityWeek (`securityweek`) — reachable (200, last-modified 2026-05-16T12:45 UTC pre-window), 0 in-window items.
- Unit 42 feedburner (`unit42`) — reachable (200, last-modified 2026-05-15T19:46 UTC pre-window), 0 in-window items.
- Microsoft Security Blog parent feed (`mstic`) — reachable (200, last-modified 2026-05-14T21:51 UTC pre-window), 0 in-window items.
- WeLiveSecurity (`eset`) — reachable (200, 100 items in feed total), 0 in-window items after since-filter.
- SentinelLabs (`sentinelone`) — reachable (200, last-modified 2026-05-15T19:30 UTC pre-window), 0 in-window items.
- SANS ISC (`sans-isc`) — reachable (200, last-modified 2026-05-17T21:59 UTC = 17:59 EDT inside window from feed-server activity), 0 in-window items after since-filter. RSS path recovered from 06:00 transient parse-error pattern; ISC remains healthy.
- Cisco Talos (`cisco-talos`) — `blog.talosintelligence.com/rss/` reachable (200, 15 items in feed), 0 in-window items. RSS path recovery (from `/feeds/posts/default` 404 pattern) holds.
- CrowdStrike (`crowdstrike`) — reachable (200, last-modified 2026-05-17T06:52 UTC pre-window), 10 dateless items returned (since-filter passes all per null published_at; persistent marketing/MQ pattern documented across 14+ consecutive sweeps; no threat-intel content). All filtered as marketing/non-priority per established source-health pattern.
- DarkReading (`darkreading`) — reachable (200, last-modified 2026-05-17T22:02 UTC inside window from feed-server activity), 1 item after since-filter evaluated and DISCARDED (see below): "The Boring Stuff is Dangerous Now" (Shlomie Liberow, dated 2026-05-18 13:00 UTC = 09:00 EDT 2026-05-18 forward-dated; opinion essay on AI agents / AI-generated code).
- Ars Technica root feed (`ars-security` workaround path `arstechnica.com/feed/`) — reachable (200), 0 in-window items.
- Volexity feedburner (`volexity`) — reachable (200, last-modified 2026-05-13T21:15 UTC pre-window), 0 in-window items.
- Wired Security (`wired-security`) — reachable (200), 0 in-window items.
- Mandiant feedburner (`mandiant`) — known broken (~20+ consecutive 404s), skipped per source-health.
- Dragos (`dragos`) — known broken (`/blog/feed/` 404), skipped per source-health.
- Sophos (`sophos`) — `news.sophos.com/en-us/feed/` returned 404 this sweep (fourth-consecutive observation post-stale-flip per 06:00 sweep state); skipped per source-health stale state with operator-path-replacement still pending.
- CISA ICS advisories direct endpoint (`cisa.gov/cybersecurity-advisories/ics-advisories.xml`) — returned 403 (likely WAF persistence on this surface, consistent with prior /news-events/cybersecurity-advisories WAF behavior — `all.xml` master feed remains productive endpoint and surfaced 0 ICS-class items in window above).
- GitHub Advisories Atom (`github-advisories`) — known persistent 406; not re-tested this sweep (FLASH-fast scope; per-repository GHSA fallback path remains the productive workaround when triggered, not triggered this sweep).

## Splunk first-party non-self-telemetry sweep

`index=defenseclaw_local earliest=-6h@h` — **0 events.**
`index=archimedes sourcetype!=archimedes:operation sourcetype!=archimedes:scheduler earliest=-6h@h` — **0 events.**

This is the **39th consecutive dormant non-self-telemetry Splunk sweep** (38 at 16:00 afternoon brief 005596f; 37 at 15:30 pre-brief; 36 at 12:00 FLASH c17bf91; 35 at 08:00 morning brief c8a140d; 34 at 06:00 FLASH 83cb46f). Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`. No Trigger 3 fire.

## In-window items evaluated and discarded

### Item 1 — DarkReading (2026-05-18T13:00 UTC = 2026-05-18T09:00 EDT, forward-dated inside this sweep window from feed-server activity): "The Boring Stuff is Dangerous Now"

- Topic: Opinion / analysis essay by Shlomie Liberow on the convergence of AI-agent-discovered vulnerabilities and AI-generated code volume forcing defender adaptation.
- Named attribution: none (no actor attribution; no specific incident; no campaign).
- Roster intersect: none.
- CVE / vulnerability: none cited.
- A&D entity: none named.
- Sector / campaign claim: none — general industry analysis.

**Trigger evaluation:**

- Trigger 1 (Critical CVE actively exploited, A-grade attestation): **FAIL** — no CVE cited.
- Trigger 2 (New tracked actor attribution): **FAIL** — no actor attribution.
- Trigger 3 (First-party IOC hit): **FAIL** — Splunk dormant sweep #39; no first-party Splunk hit.
- Trigger 4 (Tracked actor TTP change): **FAIL** — no tracked-actor TTP change documented.
- Trigger 5 (A&D sector campaign): **FAIL** — no A&D-watchlist entity named; opinion essay framing only.
- Trigger 6 (Zero-day no patch): **FAIL** — no vulnerability disclosed.
- **Disposition: DISCARDED** for FLASH purposes. General opinion / analysis content, no operational intelligence. Not a status-update candidate; afternoon-brief-grader briefing context not needed. Pure no-op.

## Carry-forwards preserved (NOT re-triggered, all unchanged from 12:00 FLASH and 16:00 afternoon brief)

- **CVE-2026-20182** (Cisco Catalyst SD-WAN auth bypass, CVSS 10.0, KEV **T-0 federal deadline TODAY 2026-05-17 EOB, ~6h remaining at sweep time**) — finding-2026-05-14-0005 carry-forward chain; afternoon brief 005596f covered as headline calendar-event with no posture shift. WebSearch confirmed no fresh A-grade attestation in 12:00–18:00 window beyond carry-forward Talos/Tenable/Rapid7/SOCRadar surfaces already in coverage. Operator decision: 00:00 FLASH or 08:00 morning brief tomorrow handles deadline post-mortem (federal-agency compliance state assessment will surface in next-day metrics, not in the catalog itself per established pattern).
- **CVE-2026-42897** (Microsoft Exchange OWA XSS, KEV T-12d due 2026-05-29) — carry-forward; afternoon brief's >48h single-source veto on exploitation-claim layer (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike all silent) preserved. WebSearch confirmed no fresh A-grade attestation in window — same Microsoft + SOCPrime + SC Media + Security Affairs + BleepingComputer + The Hacker News surfaces already in coverage. The exploitation-claim layer remains within single-source veto state (Microsoft is the originating attester via MSRC; no independent A-grade corroboration in window).
- **CVE-2026-42945 NGINX Rift PoC** — carry-forward; VulnCheck honeypot scanner-class refinement from 12:00 FLASH already absorbed into afternoon brief finding-2026-05-16-0001. No fresh A-grade attestation of production exploitation in window. Hard Rule 3 PoC repo URL not linked.
- **Symantec / Carbon Black + SentinelLABS April 2026 Fast16 framework** (A2 cluster anchor) — finding-2026-05-16-0003 carry-forward. Symantec provisional-A 72h ratification clock fired 2026-05-16T18:25 (now T+23h35m at sweep time); operator pass still pending per afternoon brief disposition. No fresh Symantec content in window (SentinelLabs feed last-modified 2026-05-15 pre-window).
- **Pwn2Own Berlin 2026 Day 2 Exchange RCE-to-SYSTEM chain** — embargoed through ZDI clock (~2026-08-13); afternoon brief carry-forward unchanged.
- **Turla / Kazuar / Secret Blizzard D+2 relay layer** — finding-2026-05-14-0006 / reject-2026-05-16-0001 anti-noise duplicate-lock active; no new relay surface this window.
- **Tycoon2FA device-code phishing PhaaS** (finding-2026-05-17-0002 cluster, commodity criminal, no tracked actor) — promoted in afternoon brief as defensive-TTP add. No fresh relay or development in 12:00–18:00 window. Anti-noise applies (one FLASH per trigger-topic per 24h — but anti-noise moot here since not a FLASH-trigger topic to begin with).
- **eSentire provisional-B source-grades.yaml addition candidate** — flagged for librarian pickup per afternoon brief; no librarian action expected pre-00:00 sweep.

## Source health observations (this sweep) — operator pass deferred, NOT applied to source-health.yaml

Per task scope (operator has pending edits to source-health.yaml per untracked-files state), these observations are recorded here ONLY; source-health.yaml is NOT modified by this collector invocation.

- `sophos`: news.sophos.com/en-us/feed/ fourth-consecutive 404 confirmed (compounding the stale-flip from 06:00 sweep 83cb46f with stale_since: 2026-05-17). Operator-path-replacement still pending.
- `cisco-talos`: `blog.talosintelligence.com/rss/` path recovery from 12:00 sweep holds (200 + 15 items in feed). Operator pass on canonical RSS path in source-health.yaml still pending.
- `sans-isc`: RSS path remains healthy (recovered from 06:00 transient parse-error per 12:00 sweep observation).
- `cisa-advisories`: ICS-specific endpoint (`cisa.gov/cybersecurity-advisories/ics-advisories.xml`) returns 403, consistent with prior /news-events/cybersecurity-advisories WAF behavior. The `all.xml` master feed remains the productive endpoint and was reached successfully this sweep. No state change; observation only.
- `crowdstrike`: 14th-or-15th consecutive sweep returning 10 dateless marketing/MQ items; pattern fully entrenched per source-health note. No state change.
- `mandiant`, `dragos`, `ars-security`, `github-advisories`, `x-cisagov`, `x-gossithedog`: carried in expected-broken / stale state per source-health.yaml; no action.
- All other queried sources: reachable, zero non-discarded in-window items.

## Carry-forward to 00:00 FLASH sweep / 08:00 morning brief grader

The 00:00 FLASH (~6h from this sweep) and 08:00 morning brief tomorrow will inherit the following operational state:

1. **CVE-2026-20182 federal KEV deadline post-mortem.** Deadline lapses end-of-day TODAY 2026-05-17. The 00:00 FLASH window straddles the deadline transition; the 08:00 morning brief grader should evaluate whether overnight reporting surfaces (a) federal-agency-compliance reporting, (b) post-deadline exploitation surge reporting, (c) Talos UAT-8616 expansion reporting, or (d) silence (the parsimonious expectation per the 48h+ second-corpus silence pattern). The federal compliance metric typically surfaces in next-day CISA / OMB reporting rather than the KEV catalog itself, per established pattern.
2. **CVE-2026-42897 Exchange OWA XSS** carry-forward unchanged; >48h single-source-veto state on exploitation-claim layer holds through the full afternoon-and-evening window. T-12d federal deadline Friday 2026-05-29.
3. **CVE-2026-42945 NGINX Rift PoC** carry-forward unchanged with VulnCheck honeypot-class probe refinement now integrated into finding-2026-05-16-0001 (per afternoon brief).
4. **Symantec/SentinelLABS Fast16 provisional-A ratification clock** now T+23h35m past elapsed deadline awaiting operator pass.
5. **Pwn2Own Berlin Day 2 Exchange RCE chain** ZDI embargo unchanged.
6. **Turla/Kazuar D+2 relay layer** duplicate-lock unchanged.
7. **Tycoon2FA device-code phishing** absorbed into finding-2026-05-17-0002 from afternoon brief; no FLASH carry-forward state.
8. **39th consecutive dormant non-self-telemetry Splunk sweep** state — silence is not disconfirming, but the cadence should continue tracking.

## Disposition

**Clean sweep, 0 FLASH triggers fired, 39th consecutive dormant non-self-telemetry Splunk sweep, no escalation, no Discord post.** All carry-forwards preserved unchanged. Sentinel tombstone non-promotable per established precedent. The 00:00 FLASH sweep (~6h from this sweep, will be inside quiet-hours so any trigger would queue not post) and the 08:00 morning brief pipeline will handle: (1) CVE-2026-20182 deadline post-mortem reporting if any surfaces overnight; (2) standard carry-forward chain refresh; (3) any net-new actor-attribution or campaign reporting that surfaces in the 18:00–00:00 EDT window.
