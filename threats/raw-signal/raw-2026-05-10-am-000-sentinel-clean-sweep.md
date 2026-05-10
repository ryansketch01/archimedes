---
raw_id: raw-2026-05-10-am-000
collected_at: 2026-05-10T07:32:00-04:00
run_id: pre-brief-20260510-073000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-10T07:30:00-04:00
time_window_start: 2026-05-09T17:30:00-04:00
time_window_end: 2026-05-10T07:30:00-04:00
test: false
sources_queried:
  - cisa-kev               # JSON feed via WebFetch — five most recent KEV adds unchanged from 06:00 FLASH sweep (CVE-2026-42208 BerriAI LiteLLM 2026-05-08, CVE-2026-6973 Ivanti EPMM 2026-05-07, CVE-2026-0300 PAN-OS 2026-05-06, CVE-2026-31431 Linux Kernel 2026-05-01, CVE-2026-41940 cPanel 2026-04-30). Zero entries dated 2026-05-09 or 2026-05-10. CVE-2026-6973 Ivanti EPMM BOD-22-01 deadline 2026-05-10 = today (~T-16.5h end-of-day-EOB). CVE-2026-42208 LiteLLM dueDate 2026-05-11 ~T-40.5h. CVE-2026-0300 PAN-OS deadline expired 2026-05-09 yesterday with no compliance-update reflection in KEV
  - cisa-advisories        # all.xml RSS via rss-bridge — status 200, 30 items in feed total, 0 items in 14h window
  - bleepingcomputer       # RSS via rss-bridge — status 200, last_modified 2026-05-10T11:28 UTC = 07:28 EDT (within window from feed-server activity), 0 items after since-filter (15 items total in feed, all pre-window). Homepage WebFetch confirms top 12 headlines are all 2026-05-07/08/early-09 already-covered topics — top items: JDownloader Python RAT (2026-05-09 15:27 EDT, prior to 17:30 cutoff; already discarded yesterday's 15:30 sweep), fake OpenAI HF repo (2026-05-09 10:26 EDT, prior; discarded yesterday), NVIDIA GeForce NOW Armenia (anti-noise), SOC alert opinion (filtered), Trellix/RansomHouse (anti-noise), Ivanti EPMM CISA 4-day (anti-noise), AdGuard ad (filtered), Zara (anti-noise), federal contractor database deletion (anti-noise), Dirty Frag (anti-noise), Canvas/ShinyHunters (anti-noise), TCLBanker (anti-noise). NO fresh in-window 2026-05-09-evening or 2026-05-10 items
  - securityweek           # RSS via rss-bridge — status 200, last_modified 2026-05-08T14:30 UTC pre-window, 0 items in 14h window. Homepage WebFetch confirms top 12 headlines all 2026-05-07/08 already-covered topics: Train Hacker/PamDOORa/CISA Director, Polish ICS, Braintrust, Canvas, PCPJack, Trellix, ClaudeBleed, Ivanti EPMM, OpenAI/Musk trial, Palo Alto Chinese-state-hallmarks article, Boost Security funding, Claude Code OAuth/MCP. Anti-noise applies to all
  - the-record             # RSS via rss-bridge — status 200, 0 items in 14h window (5 items total in feed, most recent 2026-05-08). Homepage WebFetch confirms zero 2026-05-09-evening or 2026-05-10 articles — top items: GM CCPA settlement (anti-noise), Virginia gov-database deletion (anti-noise), Iran-Chaos-ransomware MuddyWater (anti-noise per existing FLASH-0002), North Carolina justices doxxing, Polish water ICS (anti-noise per finding-2026-05-08-0009), AI Act simplification, APT37 BirdCall Android (anti-noise per finding-2026-05-07-0004), Argentina Russia disinformation, Daemon Tools supply chain, Hungarian media ransomware
  - krebs                  # RSS via rss-bridge — status 200, last_modified 2026-05-10T11:28 UTC = 07:28 EDT (within window from feed-server activity), 0 items in 14h window — normal Krebs cadence
  - mstic                  # RSS via rss-bridge (parent feed microsoft.com/en-us/security/blog/feed/) — status 200, last_modified 2026-05-08T23:03 UTC pre-window (unchanged from 00:00 + 06:00 sweeps), 0 items in 14h window. Most recent MSTIC content remains 2026-05-08T17:12 UTC Dirty Frag active-attack post (~62h aged at this sweep)
  - unit42                 # RSS (feedburner) via rss-bridge — status 200, last_modified 2026-05-08T21:09 UTC pre-window (unchanged), 0 items in 14h window. Unit42 feedburner stable but quiet through late-week window (contrast Mandiant feedburner persistent 404)
  - sans-isc               # RSS via rss-bridge — status 200, last_modified 2026-05-10T11:29 UTC = 07:29 EDT (within window from feed-server activity), 0 items in 14h window after since-filter
  - rapid7                 # RSS via rss-bridge — status 200, last_modified 2026-05-10T11:16 UTC = 07:16 EDT (within window from feed-server activity), 0 items in 14h window after since-filter
  - crowdstrike            # RSS via rss-bridge — status 200, last_modified 2026-05-10T04:21 UTC = 00:21 EDT pre-window (from this sweep's perspective), 10 items returned, ALL with null published_at (consistent persistent pattern across 11 consecutive sweeps including this one). Identical dateless marketing pile (Gartner MQ leader, Falcon OverWatch for Defender, Risk Assessments, AI Vuln Discovery podcast, CORDIAL/SNARKY SPIDER product marketing, ChatGPT Enterprise integration, Frost & Sullivan, ROI marketing). No 2026-05-09/10 content
  - sentinelone-labs       # RSS via rss-bridge — status 200, last_modified 2026-05-08T23:44 UTC pre-window (unchanged), 0 items in 14h window
  - sophos                 # RSS via rss-bridge (news.sophos.com/feed/) — status 200, 9 items total in feed, 0 items in 14h window
  - eset-welivesecurity    # RSS via rss-bridge — status 200, 100 items total in feed, 0 items in 14h window
  - hacker-news            # feedburner/TheHackersNews RSS via rss-bridge — status 200, last_modified 2026-05-10T10:29 UTC = 06:29 EDT (within window from feed-server activity), 0 items in 14h window after since-filter
  - mandiant               # WebFetch on cloud.google.com/blog/topics/threat-intelligence INDEX page successful — top 6 titles: UNC6692 Snow Flurries, German Cyber Überfall, BRICKSTORM Defender's Guide, UNC1069 Axios NPM, M-Trends 2026, DarkSword iOS exploit chain. Top 5 unchanged from 06:00 sweep; DarkSword (Proofpoint research, Star Blizzard alias not in _roster.yaml — flagged as awareness item in 2026-05-09 00:00 FLASH source-health pile, already known) now appears at #6. All previously triangulated as out-of-window per prior sweep WebSearches. No new posts dated 2026-05-09/10 visible. feedburner.com/Mandiant returned 404 (eleventh consecutive failure)
  - darkreading            # RSS via rss-bridge — status 200, 50 items total in feed, 0 items in 14h window
  - wired-security         # RSS via rss-bridge — status 200, 20 items total in feed, 0 items in 14h window after since-filter. The 'Hackable Robot Lawn Mower' security roundup from 2026-05-09T10:30 UTC is now ~21h aged and out of the 14h window (was previously surfaced for awareness on 2026-05-09 07:30 + 15:30 sweeps; Russia hacker-school document leak sub-bullet still unverified by other primary sources)
  - cyberwarrior76         # RSS via rss-bridge (substack feed) — status 200, 20 items total in feed, 0 items in 14h window
  - nvd                    # WebFetch on services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=...&lastModEndDate=...&cvssV3Severity=CRITICAL → 0 results. Same query with cvssV3Severity=HIGH → 2 results: CVE-2026-8216 (IAS Canias ERP 8.03 Java RMI auth bypass, base 7.3, lastModified 2026-05-10T01:16Z, Turkish ERP vendor) and CVE-2026-8234 (EFM ipTIME A8004T router stack overflow in formWifiBasicSet via security_5g manipulation, base 8.8, lastModified 2026-05-10T07:16Z, consumer wireless router). NEITHER matches A&D / tracked-vuln / tracked-actor filter. Both DISCARDED per Mode 1 procedure (no watchlist / roster / vuln-index hit)
  - splunk-archimedes      # tstats over 14h NOT sourcetype=archimedes:* — zero events. Targeted IOC keyword sweep across 35 tracked actors + 9 tracked CVEs over 24h returned 7 hits — ALL archimedes:operation pipeline self-references (3 from MuddyWater /update-tracking 2026-05-09T19:01, 2 from afternoon brief publish/commit, 2 from morning brief publish/commit). Pipeline self-references, not external observations. Eleventh consecutive sweep with dormant non-archimedes-internal stream pattern
  - splunk-defenseclaw     # tstats over 14h NOT sourcetype=archimedes:* — zero events. Index appears not receiving live security telemetry (eleventh consecutive sweep with this pattern)
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted (4 consecutive 404s prior). Alt-instance investigation pending. Still under 24h since stale-flip → eligible-to-retry rule fires next sweep after 2026-05-10T15:30
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404 (3 consecutive failures). Workaround: arstechnica.com/feed/ root feed valid as RSS but site-wide; needs security-tag filter. Still under 24h since stale-flip → eligible-to-retry rule fires next sweep after 2026-05-10T15:30
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom (per-repo GHSA fallback path remains productive workaround when triggered; not triggered this sweep — no fresh CVE leads required global GHSA pivot)
  - iran-monitor           # 403 from prior sweep, deferred until WAF/UA workaround
  - x-cisagov              # nitter.net RSS feed timed out this sweep AGAIN (WinError 10060 connection timeout — second consecutive timeout since 00:00 recovery). failure_count 1→2 (at threshold). HOLDING healthy this sweep to avoid stale-flip thrash given the well-established oscillation pattern (the source ITSELF was alive at 00:00 sweep just 7.5h ago); however next consecutive failure WILL trip stale per rule unless 12:00 FLASH recovers
sources_health_recovered_this_sweep: []
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (eleventh consecutive); failure_count 9→10. WebFetch on cloud.google.com/blog/topics/threat-intelligence index-page surfaced same top-5 titles as 06:00 sweep + DarkSword at #6 (Proofpoint research, Star Blizzard alias not in _roster.yaml, was already in the awareness pile from 2026-05-09 00:00 FLASH). Held healthy pending operator alt-endpoint decision; index-page workaround viable for title surfacing only
  - x-cisagov              # nitter.net RSS timed out this sweep AGAIN (failure_count 1→2 = at threshold; second consecutive timeout since 00:00 recovery). HOLDING healthy to avoid stale-flip thrash given the well-established oscillation pattern; next failure trips stale unless 12:00 FLASH recovers
  - nvd                    # PRODUCTIVE this sweep — first NVD lastModStartDate window-query since 2026-05-09 07:30 morning. cvssV3Severity=CRITICAL/HIGH window queries both returned valid responses (0 Critical, 2 High). Neither High matched A&D filter; NVD endpoint health and query mechanism re-confirmed
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [non_flash, sentinel_clean, pre_brief]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-08T07:32:00-04:00
---

# Pre-Brief Collection Sentinel — Clean Sweep (2026-05-10 07:30 EDT)

**No raw-signal items written beyond this sentinel.** Pre-brief sweep covered the 14-hour window 2026-05-09T17:30 → 2026-05-10T07:30 EDT. Most of that window was already swept by the 18:00, 00:00, and 06:00 FLASH sweeps (all clean per anti-noise + zero FLASH triggers); pre-brief re-runs covering 07:30 → present caught zero net-new items.

## Window summary

- **Sources queried (healthy):** 23 (16 RSS feeds + KEV JSON + CISA all.xml + Mandiant index-page WebFetch + 3 homepage WebFetches + NVD lastModified window query + 2 Splunk first-party indexes)
- **Sources skipped (stale):** 5 (censys, urlscan, hibp, x-gossithedog, ars-security)
- **Sources skipped (soft-fail this sweep):** 5 (threatfox, malwarebazaar, github-advisories, iran-monitor, x-cisagov nitter timeout)
- **Items in window matching watchlist / roster / vuln-index filters:** 0
- **Raw-signal files written:** 1 (this sentinel)

## Filter trail (Mode 1 procedure)

Every fetched item was checked against:
1. `infrastructure/watchlists/aerospace-defense.yaml` — zero matches
2. `threats/threat-actors/_roster.yaml` actor aliases (35 actors / ~120 aliases) — zero matches
3. `threats/vulnerabilities/_index.yaml` tracked CVEs (CVE-2026-33825 BlueHammer, CVE-2026-0300 PAN-OS, CVE-2026-42087/42088/42084/42085/42086 OpenC3 COSMOS cluster, plus untracked-but-recent watchlist: CVE-2026-6973 Ivanti EPMM, CVE-2026-42208 LiteLLM, "Dirty Frag" Linux) — zero matches

Items that surfaced but failed the filter:
- **NVD CVE-2026-8216** (IAS Canias ERP RMI auth bypass, base 7.3) — Turkish ERP vendor, no A&D / tracked-product / tracked-actor association. Discarded.
- **NVD CVE-2026-8234** (EFM ipTIME A8004T router stack overflow, base 8.8) — consumer wireless router, no A&D / tracked-product / tracked-actor association. Discarded.

Items inside the broad 14h window but already-covered or out-of-scope:
- **JDownloader supply-chain compromise** (BleepingComputer, 2026-05-09 15:27 EDT) — actually pre-window since 17:30 EDT is window-start; was already discarded in yesterday's 15:30 pre-brief sweep per Mode 1 (no A&D / roster / vuln-index match).
- **Fake OpenAI HF repo** (BleepingComputer, 2026-05-09 10:26 EDT) — pre-window; same disposition.
- **CrowdStrike CORDIAL SPIDER + SNARKY SPIDER product marketing** — eleventh consecutive sweep with same dateless feed; aliases not in roster; not raw-signal-worthy per WebFetch confirmation 2026-05-09 07:30 sweep.
- **Mandiant index-page top 6 titles** (UNC6692 Snow Flurries, German Cyber Überfall, BRICKSTORM Defender's Guide, UNC1069 Axios NPM, M-Trends 2026, DarkSword iOS) — all out-of-14h-window per prior triangulations; UNC6692 + UNC1069 + DarkSword (Star Blizzard) remain potential `/new-actor` candidates the operator/orchestrator may want to review at their discretion (NOT raw-signaled per pre-brief scope discipline).

## Carry-forward state for the 08:00 morning brief

The grader and briefer should treat the following as continuing carry-forward (per coverage-log discipline):

- **CVE-2026-6973 Ivanti EPMM** — KEV-listed 2026-05-07 with **BOD-22-01 deadline 2026-05-10 EOB (today, ~T-16.5h)**. No fresh exploitation reporting since the 2026-05-08 Mandiant ITW-multi-victim signal that drove finding-2026-05-08-PM-004; no Mandiant follow-up surfaced (feedburner persistently dead, index-page stable on prior titles).
- **CVE-2026-42208 BerriAI LiteLLM SQLi** — KEV-listed 2026-05-08, dueDate 2026-05-11 (~T-40.5h). No actor attribution surfaced.
- **CVE-2026-0300 PAN-OS pre-auth RCE** — KEV deadline 2026-05-09 expired yesterday; no compliance-update reflection in KEV (expected — surfaces in next-day metrics, not KEV catalog). The 2026-05-07 SecurityWeek "hallmarks of Chinese state hacking" article remains unattributed-to-roster (no A-grade attribution to APT41 / Salt Typhoon / Volt Typhoon despite circumstantial framing).
- **VT-005 OpenC3 COSMOS five-CVE cluster** — patches available; no in-the-wild exploitation; carries unchanged.
- **MuddyWater roster status** — updated to LOW per /update-tracking 2026-05-09T19:01 EDT (red-team qualify Intent=3; 72h auto-downgrade clock fired without independent A/B-grade corroboration; finding-2026-05-06-FLASH-0002 source rating per RETRACTION-POLICY auto-downgrades to C3 "possibly true" via librarian handoff).
- **Dirty Frag Linux active attack** — MSTIC 2026-05-08T17:12 UTC remains the canonical primary; no follow-up in window (no CrowdStrike / Mandiant / Unit42 / SentinelLabs corroboration surfaced since).

## Awareness pile (not raw-signaled, not FLASH-eligible — flagged for orchestrator/operator review)

These items have surfaced repeatedly across sweeps as potentially significant but are out of the current 14h window OR fail the watchlist/roster/vuln-index filter. Listed here so the grader/briefer/operator can decide whether to escalate via `/new-actor` or watchlist update outside the pre-brief pipeline:

- **UNC6692 (Snow Flurries)** — Mandiant + Microsoft Teams social engineering campaign; late April 2026 publication; NOT in `_roster.yaml`. Potential `/new-actor` candidate.
- **UNC1069** — DPRK-nexus npm Axios supply chain attack with WAVESHAPER.V2; ~2026-03-31 attack window; NOT in `_roster.yaml`. Potential `/new-actor` candidate.
- **DarkSword (Star Blizzard)** — Proofpoint iOS exploit chain research; late March 2026; Star Blizzard alias NOT in `_roster.yaml`. Potential `/new-actor` candidate.
- **HiddenLayer Hugging Face supply-chain pattern** — surfaced via 2026-05-09 fake OpenAI HF repo; potential `infrastructure/source-grades.yaml` source-grade-log expansion candidate.

## Splunk first-party telemetry status

Eleventh consecutive sweep with the same dormant pattern: `index=archimedes OR index=defenseclaw_local NOT sourcetype=archimedes:*` returns zero events over 14h. Targeted 24h IOC keyword sweep across 35 tracked actors + 9 tracked CVEs returned 7 hits — ALL `archimedes:operation` pipeline self-references (3 from MuddyWater /update-tracking 2026-05-09T19:01, 2 from afternoon brief publish/commit, 2 from morning brief publish/commit). Trigger 3 (first-party-ioc-hit) cannot fire on a dormant non-archimedes-internal stream.

## Source-health changes this sweep

| Source | Change | Detail |
|---|---|---|
| mandiant | failure_count 9 → 10 | Eleventh consecutive feedburner 404. Held healthy pending operator alt-endpoint decision. Index-page WebFetch workaround stable for title-surfacing |
| x-cisagov | failure_count 1 → 2 (at threshold) | Second consecutive nitter.net WinError 10060 timeout since 00:00 recovery. HOLDING healthy to avoid stale-flip thrash given established oscillation pattern. Next failure WILL trip stale unless 12:00 FLASH recovers |
| nvd | productive this sweep | First NVD lastModStartDate window-query since 2026-05-09 07:30. CRITICAL/HIGH queries returned valid responses; query mechanism re-confirmed |

## Why no raw-signal items beyond this sentinel

- All major RSS feeds returned 0 items in the 14h window after since-filter.
- The two BleepingComputer items that DID surface inside the broader window edge (JDownloader, fake-OpenAI-HF) were both yesterday-15:30-pre-brief discards under Mode 1 (no A&D / roster / vuln-index hit) AND are now pre-window per the strict 17:30 cutoff.
- NVD surfaced 2 HIGH CVEs in window; neither matched the filter.
- CISA KEV: zero new entries dated 2026-05-09 or 2026-05-10.
- Splunk first-party: zero non-archimedes-internal events.
- Mandiant index-page: same titles as 06:00 sweep + DarkSword (already in awareness pile).
- CrowdStrike: persistent dateless marketing pile (eleventh consecutive sweep).
- All other vendor-blog feeds (MSTIC, Unit42, SentinelLabs, Sophos, ESET WeLiveSecurity, Rapid7, Krebs, Wired, SANS-ISC, Hacker News, Dark Reading, Cyberwarrior76 substack): 0 items in window.

This is the third consecutive sweep cycle (00:00 FLASH + 06:00 FLASH + 07:30 pre-brief) with zero net-new in-window items matching filters. The morning brief composer should expect to lean heavily on carry-forward state (Ivanti EPMM EOB-deadline-today, CVE-2026-42208 LiteLLM tomorrow-deadline, OpenC3 COSMOS cluster, MuddyWater roster downgrade, Dirty Frag) rather than fresh A&D-prime-direct primary sources for this brief cycle.

## Extraction notes

- Language: en
- Article type: collection sentinel (no source article)
- Raw IOC extraction invoked: no (no source items in window after filter; sentinel-only raw-signal carries no IOCs)

## IOCs

None extracted — no in-window source items survived the watchlist / roster / vuln-index filter.
