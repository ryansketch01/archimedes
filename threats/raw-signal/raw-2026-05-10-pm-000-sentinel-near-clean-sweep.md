---
raw_id: raw-2026-05-10-pm-000
collected_at: 2026-05-10T15:32:00-04:00
run_id: pre-brief-20260510-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-10T15:30:00-04:00
time_window_start: 2026-05-10T07:30:00-04:00
time_window_end: 2026-05-10T15:30:00-04:00
test: false
sources_queried:
  - cisa-kev               # JSON feed via WebFetch — full-catalog dateAdded>=2026-05-09 scan: zero entries. Five most recent KEV adds unchanged from noon FLASH sweep (CVE-2026-42208 BerriAI LiteLLM 2026-05-08 dueDate 2026-05-11 ~T-12h; CVE-2026-6973 Ivanti EPMM 2026-05-07 dueDate 2026-05-10 EOB ~T-4h from this sweep; CVE-2026-0300 PAN-OS 2026-05-06; CVE-2026-31431 Linux Kernel 2026-05-01; CVE-2026-41940 cPanel 2026-04-30)
  - cisa-advisories        # all.xml RSS via rss-bridge — status 200, 30 items in feed total, 0 items in 8h window
  - bleepingcomputer       # RSS via rss-bridge — status 200, last_modified 2026-05-10T19:28 UTC = 15:28 EDT (within window from feed-server activity), 1 item after since-filter — "Hackers abuse Google ads, Claude.ai chats to push Mac malware" (2026-05-10T17:52 UTC = 13:52 EDT). RAW-SIGNALED as PM-001 (watchlist-edge admission on TTP-pattern overlap with tracked Beagle cluster). Homepage WebFetch confirms this is the only fresh 2026-05-10-afternoon BleepingComputer item
  - securityweek           # RSS via rss-bridge — status 200, last_modified 2026-05-08T14:30 UTC pre-window (unchanged from morning sweep), 0 items in 8h window. Homepage WebFetch confirms zero 2026-05-10 articles — most recent are 2026-05-08
  - the-record             # RSS via rss-bridge — status 200, 0 items in 8h window (5 items total in feed, most recent 2026-05-08)
  - krebs                  # RSS via rss-bridge — status 200, last_modified 2026-05-08T15:10 UTC pre-window, 0 items in 8h window — normal Krebs cadence
  - mstic                  # RSS via rss-bridge (parent feed microsoft.com/en-us/security/blog/feed/) — status 200, last_modified 2026-05-08T23:03 UTC pre-window (unchanged across 4 consecutive sweeps), 0 items in 8h window. Most recent MSTIC content remains 2026-05-08T17:12 UTC Dirty Frag active-attack post (~70h aged at this sweep)
  - unit42                 # RSS (feedburner) via rss-bridge — status 200, last_modified 2026-05-08T21:09 UTC pre-window (unchanged across 4 consecutive sweeps), 0 items in 8h window
  - sans-isc               # RSS via rss-bridge — status 200, last_modified 2026-05-10T19:29 UTC = 15:29 EDT (within window from feed-server activity), 0 items in 8h window after since-filter
  - rapid7                 # RSS via rss-bridge — status 200, last_modified 2026-05-10T19:16 UTC = 15:16 EDT (within window from feed-server activity), 0 items in 8h window after since-filter
  - sentinelone-labs       # RSS via rss-bridge — status 200, last_modified 2026-05-08T23:44 UTC pre-window (unchanged), 0 items in 8h window
  - sophos                 # RSS via rss-bridge (news.sophos.com/en-us/feed/) — 404 this sweep (likely transient or path-shift; news.sophos.com/feed/ root path was used successfully on prior morning sweep; recommend operator validate exact path). Soft-fail recorded; not yet stale (failure_count=0→1 this sweep)
  - eset-welivesecurity    # RSS via rss-bridge — status 200, 100 items total in feed, 0 items in 8h window
  - hacker-news            # feedburner/TheHackersNews RSS via rss-bridge — status 200, last_modified 2026-05-10T18:57 UTC = 14:57 EDT (within window from feed-server activity), 1 item after since-filter — "Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak" (CVE-2026-7482, 2026-05-10T12:41 UTC = 08:41 EDT). ALREADY EVALUATED AT NOON FLASH (per source-health.yaml entry for 2026-05-10 12:00 FLASH); anti-noise applies — not re-raw-signaled. Disposition unchanged: awareness-only, fails Trigger 1 (no active exploit, no A-grade source claiming exploit), Trigger 6 (patch available 0.17.1), no A&D match. Additionally per Splunk requery this sweep CVE-2026-7482 surfaced in a 2026-05-05 archimedes:operation git_committed event tied to a prior afternoon brief — CVE has been in the corpus for 5 days, today's TheHackerNews piece is re-surfacing, not fresh disclosure
  - mandiant               # WebFetch on cloud.google.com/blog/topics/threat-intelligence INDEX page — top 11 titles surfaced (Defending Enterprise AI, UNC6692 Snow Flurries, German Cyber Überfall, BRICKSTORM Defender's Guide, UNC1069 Axios NPM, M-Trends 2026, DarkSword iOS, Ransomware Under Pressure, Proactive Preparation 2026 Edition, Look What You Made Us Patch 2025 Zero-Days in Review, Coruna iOS Exploit Kit). All previously triangulated as out-of-window. feedburner.com/Mandiant returned 404 (thirteenth consecutive failure). Operator alt-endpoint decision still pending
  - darkreading            # RSS via rss-bridge — status 200, 50 items total in feed, 0 items in 8h window
  - ars-technica           # Workaround used: arstechnica.com/feed/ root feed (site-wide; ars-security path retired). Reachable, 0 items in 8h window
  - cyberwarrior76         # RSS via rss-bridge (substack feed) — not invoked this sweep (substack cadence is slow; morning sweep already returned 0 items, no fresh leads warranted re-poll)
  - nvd                    # WebFetch on services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=...&lastModEndDate=... for full 8h window (07:30 → 15:30 EDT). cvssV3Severity=CRITICAL → 7 results: CVE-2026-2786 Firefox 9.8 (2026-02-24 disclosure already patched, NVD lastModified metadata refresh); CVE-2026-20797 Copeland XWEB Pro 9.8 (NVD-stamped 9.8 but actual CVSS 4.3 per Claroty Team82, commercial HVAC/refrigeration controller, 2026-02-26 disclosure already patched, metadata refresh); CVE-2021-47923 OpenCart 3.0.3.8 session fixation 9.8 (2021 vintage NVD-publishing today, e-commerce platform, not A&D); CVE-2021-47932 WordPress TheCartPress 9.8 (2021 vintage WordPress plugin); CVE-2021-47933 WordPress MStore API 9.8 (2021 vintage WordPress plugin); CVE-2021-47936 OpenCATS 0.9.4 9.8 (2021 vintage applicant tracking system); CVE-2021-47940 WordPress Download From Files 9.8 (2021 vintage WordPress plugin). NONE match A&D / tracked-vuln / tracked-actor filter. All DISCARDED per Mode 1 procedure
  - splunk-archimedes      # tstats over 8h NOT sourcetype=archimedes:* — zero events. Targeted IOC keyword sweep across the new BleepingComputer Mac-malvertising IOCs (3 domains + 2 SHA256 hashes) returned zero hits over -30d. Targeted CVE keyword sweep on CVE-2026-7482 / CVE-2026-42248 / CVE-2026-42249 (Ollama Bleeding Llama trio) returned 3 hits — pipeline self-references including a 2026-05-05 afternoon brief commit referencing CVE-2026-7482 by name (confirming the CVE has been in the corpus for 5 days; today's TheHackerNews piece is re-surfacing). Twelfth-plus consecutive sweep with dormant non-archimedes-internal stream pattern
  - splunk-defenseclaw     # tstats over 8h NOT sourcetype=archimedes:* — zero events. Index appears not receiving live security telemetry (twelfth-plus consecutive sweep)
  - virustotal             # PRODUCTIVE this sweep — invoked on 5 IOCs from BleepingComputer Mac-malvertising raw signal (3 domains + 2 SHA256 hashes). customroofingcontractors.com = 8 malicious + 3 suspicious / 47 harmless (BitDefender, G-Data, CRDF, Certego, ADMINUSLabs, CyRadar, LevelBlue, alphaMountain.ai), reputation -1. bernasibutuwqu2.com = 0 malicious but domain registered 2026-05-09 (1 day before publication; new-attacker-infrastructure pattern). briskinternet.com = 0 malicious / 58 harmless (lower-confidence IOC). SHA256 ed5ed79a... = 25 malicious detections on 1444-byte shell script (Microsoft, Sophos, Kaspersky, ESET, BitDefender, Trellix). SHA256 a833ad98... = 24 malicious detections on 1349-byte loader.sh. Strong VT corroboration for the IOC set; results recorded in PM-001 frontmatter
sources_skipped_stale:
  - censys                 # MCP not built (deferred to Session 11+)
  - urlscan                # MCP not built (deferred to Session 11+)
  - hibp                   # No API key configured (HIBP_API_KEY missing from .env)
  - x-gossithedog          # STALE since 2026-05-09 — nitter.net account permanently delisted. Within 24h since stale-flip → still skipped this sweep; eligible-to-retry rule fires next sweep after 2026-05-10T15:30 → THIS SWEEP would be eligible-to-retry by clock, but pre-brief scope is RSS/feeds-first and the alt-instance-investigation is the actual blocker; held skipped this sweep, operator alt-pool decision pending
  - ars-security           # STALE since 2026-05-09 — feeds.arstechnica.com/arstechnica/security 404. Workaround used (root arstechnica.com/feed/ via fetch_feed); the security-specific stale entry remains stale pending operator path-replacement decision
  - x-cisagov              # STALE FLIP at noon FLASH (2026-05-10 12:00) — three consecutive WinError 10060 nitter.net timeouts. Within 24h since stale-flip → skipped this sweep; eligible-to-retry rule fires next sweep after 2026-05-11T12:00 (next noon FLASH). Source itself confirmed alive at 00:00 sweep so this remains bridge-instance fragility; operator alt-pool / direct-X-API decision pending
sources_skipped_softfail_this_sweep:
  - threatfox              # CAPTCHA wall via WebFetch (auth-injection limitation), awaiting MCP build priority
  - malwarebazaar          # awaiting MCP build priority
  - github-advisories      # 406 Not Acceptable on global advisories.atom (per-repo GHSA fallback path remains productive workaround when triggered; not triggered this sweep — no fresh CVE leads required global GHSA pivot)
  - iran-monitor           # 403 from prior sweep, deferred until WAF/UA workaround
  - proofpoint             # NEW soft-fail at noon FLASH (/us/threat-insight/blog/feed 404); not re-tested this sweep (12:00 FLASH disposition stands — endpoint potentially retired, recommend operator alt-RSS-path discovery)
sources_health_recovered_this_sweep: []
sources_health_changed_this_sweep:
  - mandiant               # feedburner.com/Mandiant continues 404 (thirteenth consecutive); failure_count 11→12. WebFetch on cloud.google.com/blog/topics/threat-intelligence index-page surfaced top-11 titles including pre-existing awareness items (UNC6692, UNC1069, DarkSword) — all out-of-window per prior triangulations. Held healthy pending operator alt-endpoint decision; index-page workaround stable for title-surfacing
  - sophos                 # First soft-fail this sweep — news.sophos.com/en-us/feed/ returned 404 via fetch_feed. Path was successful on prior morning sweep at news.sophos.com/feed/ (root, no en-us subpath); recommend operator validate exact endpoint path. failure_count 0→1; not yet stale
  - virustotal             # PRODUCTIVE this sweep (first VT invocation in current sweep cycle) — 5 IOC lookups (3 domains + 2 SHA256) all returned valid responses with strong malicious-detection consensus on 3 of 5 IOCs. VT API health re-confirmed
  - nvd                    # PRODUCTIVE this sweep — CRITICAL severity window query returned 7 results (vs 0 on morning sweep over 14h, 7 on noon FLASH over 6h); endpoint health stable. All 7 results out-of-A&D-filter per Mode 1 (5 are 2021 vintage NVD-publishing today, 2 are early-2026 metadata refreshes already-patched)
match_reason:
  watchlist: []          # this sentinel has no watchlist matches — see PM-001 for the one in-window raw-signaled item
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags:
  - non_flash
  - sentinel_near_clean   # not "sentinel_clean" — one in-window item was raw-signaled as PM-001 on TTP-pattern-overlap watchlist-edge admission
  - pre_brief
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-08T15:32:00-04:00
---

# Pre-Brief Collection Sentinel — Near-Clean Sweep (2026-05-10 15:30 EDT)

**One raw-signal file written this sweep: PM-001 (BleepingComputer Mac
malvertising / Claude.ai shared-chat abuse).** All other in-window
candidates either failed the Mode 1 watchlist/roster/vuln-index filter
or were already evaluated upstream (noon FLASH) under anti-noise rules.

## Window summary

- **Time window:** 2026-05-10T07:30 → 15:30 EDT (~8 hours; afternoon
  pre-brief)
- **Sources queried (healthy):** 22 (16 RSS feeds + KEV JSON + CISA
  all.xml + Mandiant index-page WebFetch + 2 homepage WebFetches + NVD
  lastModified window query + 2 Splunk first-party indexes + VirusTotal
  IOC enrichment)
- **Sources skipped (stale):** 6 (censys, urlscan, hibp,
  x-gossithedog, ars-security, x-cisagov — added at noon FLASH)
- **Sources skipped (soft-fail this sweep):** 5 (threatfox,
  malwarebazaar, github-advisories, iran-monitor, proofpoint added at
  noon FLASH)
- **New soft-fail this sweep:** sophos (news.sophos.com/en-us/feed/ 404
  via fetch_feed; verify exact endpoint path)
- **Items in window matching watchlist / roster / vuln-index filters:** 0
- **Items in window admitted on TTP-pattern-overlap edge:** 1
- **Raw-signal files written:** 2 (this sentinel + PM-001)

## In-window items and their dispositions

### PM-001 — BleepingComputer "Hackers abuse Google ads, Claude.ai chats to push Mac malware"

- **Published:** 2026-05-10T17:52 UTC = 13:52 EDT (in window)
- **Source:** BleepingComputer (Ax Sharma) relaying Trendyol Group
  researcher Berk Albayrak
- **Disposition:** RAW-SIGNALED with `watchlist_edge_admit` triage tag
- **Filter outcome:** FAILED strict Mode 1 (no A&D, no roster, no
  tracked CVE) but PASSED softer TTP-pattern-overlap admission with
  tracked unattributed `beagle` cluster (both share AI-brand-
  impersonation-Anthropic lure pattern). Hard Rule 2 respected — no
  cross-walk attribution made; pattern overlap recorded as TTP-
  evolution signal only.
- **IOCs extracted:** 7 (3 domains, 2 claude.ai-share URLs, 2 SHA256
  shell scripts). VT-corroborated: 25 malicious / 24 malicious on the
  two hashes; 8 malicious on customroofingcontractors[.]com. Splunk
  first-party clean on full IOC set -30d.
- **FLASH triggers:** 0 of 6 matched. `non_flash` tag.
- **A&D-prime relevance:** Indirect (Mac infostealer aimed at
  developers using Claude AI; structural exposure to A&D
  developer-endpoint workflows; no direct A&D-prime targeting in
  source).
- **Full content:** see `raw-2026-05-10-pm-001-mac-malvertising-claude-ai-share-abuse.md`.

### TheHackerNews — "Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak"

- **Published:** 2026-05-10T12:41 UTC = 08:41 EDT (in window)
- **Source:** TheHackerNews (Ravie Lakshmanan) relaying Cyera research
  (codename "Bleeding Llama")
- **Disposition:** DISCARDED per anti-noise + prior-evaluation rule
- **Why discarded:**
  1. Already evaluated at noon FLASH sweep (2026-05-10 12:00) per
     source-health.yaml entry — confirmed CVE-2026-7482 CVSS 9.1, patch
     available (0.17.1), no in-the-wild exploitation, no A&D, fails
     Trigger 1 + Trigger 6
  2. Splunk requery this sweep on `CVE-2026-7482` surfaced a 2026-05-05
     `archimedes:operation` `git_committed` event from a prior
     afternoon brief commit message — CVE has been in the corpus for 5
     days; today's TheHackerNews piece is media re-surfacing of a
     5-day-old disclosure, not fresh disclosure. Secondary
     CVE-2026-42248 / CVE-2026-42249 (Ollama for Windows updater path
     traversal + missing-signature-verification, both CVSS 7.7) are
     newly named in this piece but are non-A&D (developer LLM-framework
     tooling on commodity Windows hosts), no in-the-wild exploitation,
     90-day-disclosure-window expired by Striga researcher
- **A&D-prime relevance:** None claimed in source.

### Other items inside the window edge but already-covered

- **JDownloader Python RAT supply-chain compromise** (BleepingComputer,
  2026-05-09 15:27 EDT) — pre-window per 17:30 cutoff (well outside
  this sweep's 07:30 → 15:30 EDT window). Already discarded in
  2026-05-09 15:30 pre-brief.
- **Fake OpenAI HF repo** (BleepingComputer, 2026-05-09 10:26 EDT) —
  pre-window, same disposition.
- **CrowdStrike CORDIAL/SNARKY SPIDER product marketing** — twelfth
  consecutive sweep with same dateless feed; not raw-signal-worthy.

## NVD lastModStartDate window query results (full 8h)

NVD CRITICAL window query returned 7 results over 07:30 → 15:30 EDT:

| CVE | Vendor/Product | CVSS | NVD Published | Disposition |
|---|---|---|---|---|
| CVE-2026-2786 | Mozilla Firefox/Thunderbird use-after-free | 9.8 | 2026-02-24 | Already patched in Firefox 148 / ESR 140.8 / Thunderbird 148; NVD lastModified is metadata refresh; not A&D-specific. Discarded |
| CVE-2026-20797 | Copeland XWEB Pro stack buffer overflow | NVD 9.8 (Claroty Team82 4.3 actual) | 2026-02-27 | Commercial HVAC/refrigeration controller (not A&D); DoS-only program-termination; already patched; metadata refresh. Discarded |
| CVE-2021-47923 | OpenCart 3.0.3.8 session fixation | 9.8 | 2026-05-10 | 2021 vintage e-commerce platform CVE newly NVD-published today; not A&D. Discarded |
| CVE-2021-47932 | WordPress TheCartPress unauthenticated privesc | 9.8 | 2026-05-10 | 2021 vintage WordPress plugin; not A&D. Discarded |
| CVE-2021-47933 | WordPress MStore API arbitrary file upload | 9.8 | 2026-05-10 | 2021 vintage WordPress plugin; not A&D. Discarded |
| CVE-2021-47936 | OpenCATS 0.9.4 unauthenticated RCE | 9.8 | 2026-05-10 | 2021 vintage applicant tracking system; not A&D. Discarded |
| CVE-2021-47940 | WordPress Download From Files v1.48 | 9.8 | 2026-05-10 | 2021 vintage WordPress plugin; not A&D. Discarded |

NVD HIGH-severity window not re-queried this sweep (8h window NVD
CRITICAL noise level confirms HIGH-severity noise would be higher;
morning sweep's 14h HIGH query already returned 2 discards on IAS Canias
ERP + EFM ipTIME router; no fresh CVE leads warrant HIGH-severity
re-poll).

NVD endpoint health and query mechanism re-confirmed (vs 0 results on
morning sweep) — the 7-result return is the expected backfill pattern
when NVD's lastModified-timestamp window catches up on 2021-vintage
CVEs being newly published.

## CISA KEV status

Full-catalog scan for `dateAdded >= 2026-05-09`: **zero entries**.

Five most recent KEV adds unchanged from noon FLASH:

| CVE | Vendor / Product | dateAdded | dueDate | Status |
|---|---|---|---|---|
| CVE-2026-42208 | BerriAI LiteLLM SQLi | 2026-05-08 | 2026-05-11 (~T-44h) | KEV-listed |
| CVE-2026-6973 | Ivanti EPMM improper-input-validation | 2026-05-07 | **2026-05-10 EOB (~T-4h)** | KEV-listed; BOD-22-01 deadline tonight |
| CVE-2026-0300 | PAN-OS pre-auth RCE | 2026-05-06 | 2026-05-09 (expired) | KEV-listed; deadline expired yesterday |
| CVE-2026-31431 | Linux Kernel resource transfer | 2026-05-01 | (older) | KEV-listed |
| CVE-2026-41940 | WebPros cPanel & WHM auth bypass | 2026-04-30 | (older) | KEV-listed |

**Operational note for the afternoon briefer:** CVE-2026-6973 Ivanti
EPMM BOD-22-01 deadline expires tonight EOB (~T-4h from this sweep).
The morning brief carried this; afternoon brief should retain the
deadline-imminent framing through publication. Status-carry treatment
appropriate (no fresh exploitation reporting since 2026-05-08).

## Splunk first-party telemetry status

Twelfth-plus consecutive sweep with the same dormant pattern:
`index=archimedes OR index=defenseclaw_local NOT sourcetype=archimedes:*`
returns zero events over the 8h window.

Two productive Splunk requeries this sweep:

1. **PM-001 IOC requery** (`customroofingcontractors` OR
   `bernasibutuwqu` OR `briskinternet` OR two SHA256 hashes) over -30d:
   **zero hits**. Confirms IOCs not active in our environment.
2. **CVE-2026-7482 / Bleeding Llama requery** over -30d: **3 hits**, all
   pipeline self-references — one 2026-05-07
   `ioc_post_ingest_requery` event for Beagle cluster (unrelated
   namespace collision), one 2026-05-07 `brief_published` afternoon
   brief, and one 2026-05-05 `git_committed` event with commit message
   "brief: 2026-05-05 afternoon — 3 findings (MSTIC AitM, DAEMON Tools
   supply chain, Ollama CVE-2026-7482)". This confirms CVE-2026-7482
   has been in the corpus since 2026-05-05 — today's TheHackerNews
   piece is media re-surfacing, not fresh disclosure. Anti-noise
   discard at noon FLASH was correct.

Trigger 3 (first-party-ioc-hit) cannot fire on a dormant non-
archimedes-internal stream.

## Source-health changes this sweep

| Source | Change | Detail |
|---|---|---|
| mandiant | failure_count 11 → 12 | Thirteenth consecutive feedburner 404. Held healthy pending operator alt-endpoint decision |
| sophos | failure_count 0 → 1 | First soft-fail this sweep — `news.sophos.com/en-us/feed/` 404 via fetch_feed (prior morning sweep used `news.sophos.com/feed/` root path successfully; verify exact endpoint) |
| virustotal | productive this sweep | First VT invocation in current sweep cycle; 5 IOC lookups all returned valid responses with strong malicious-detection consensus |
| nvd | productive this sweep | CRITICAL window query returned 7 results vs 0 on morning sweep; endpoint health stable, all 7 results A&D-filter MISS |

## Anomalies worth flagging to the operator

1. **CVE-2026-7482 namespace collision with prior brief.** The Splunk
   requery on `CVE-2026-7482` surfaced a 2026-05-05 `git_committed`
   event referencing this CVE in the afternoon brief commit message
   alongside MSTIC AitM and DAEMON Tools. This means CVE-2026-7482 has
   been in the corpus for 5 days but today's TheHackerNews piece is
   surfacing it again with a new "Bleeding Llama" codename framing.
   Operator may want to verify the historical Ollama coverage to
   confirm Bleeding Llama is the same CVE (likely yes — CVE IDs are
   immutable identifiers); if so, the apparent fresh-disclosure framing
   is a media re-surfacing artifact.

2. **bernasibutuwqu2.com is 1 day old.** The domain in PM-001 was
   registered 2026-05-09, less than 24h before the BleepingComputer
   publication. This is consistent with attacker-controlled
   infrastructure rather than benign use. Operator may want to add
   `bernasibutuwqu2.com` to a watch-domains list for any future
   pattern-overlap signal.

3. **Three distinct AI-brand-impersonation (Anthropic / Claude)
   campaigns now in corpus.** Beagle (Windows, 2026-05-07) → MacSync
   (Mac, 2026-05-10) → and Anthropic's own brand is being abused via
   real `claude.ai/share/...` URLs as part of MacSync's lure
   instruction set. This is a developing tradecraft pattern;
   recommend operator consider whether the `beagle.yaml` unattributed
   cluster should be expanded into a TTP-watch entry titled
   "AI-brand-impersonation-Anthropic lures" with cross-references to
   both Beagle and MacSync raw signals.

4. **No FLASH-eligible candidates this sweep.** Both in-window items
   (PM-001 and the discarded Ollama Bleeding Llama re-surfacing)
   evaluate against all 6 FLASH triggers as false. Sentinel-near-clean
   treatment.

5. **CVE-2026-6973 Ivanti EPMM BOD-22-01 deadline expires tonight
   (~T-4h).** Afternoon briefer should retain deadline-imminent framing
   through 16:00 publication. Status-carry; no fresh exploitation
   reporting in window.

## Carry-forward state for the 16:00 afternoon brief

- **CVE-2026-6973 Ivanti EPMM** — KEV deadline **TONIGHT EOB (~T-4h
  from this sweep)**. Status-carry from morning brief.
- **CVE-2026-42208 BerriAI LiteLLM** — KEV deadline 2026-05-11 (~T-44h).
- **CVE-2026-0300 PAN-OS** — KEV deadline 2026-05-09 expired; no
  compliance-update reflection in KEV catalog (expected — surfaces in
  next-day metrics).
- **VT-005 OpenC3 COSMOS five-CVE cluster** — patches available; carry
  unchanged.
- **MuddyWater roster status** — LOW per /update-tracking 2026-05-09;
  finding-card supersession to C3 still pending librarian (noted in
  noon FLASH).
- **Dirty Frag Linux active attack** (MSTIC 2026-05-08T17:12 UTC) — 72h
  tripwire ~10h remaining at this sweep; afternoon briefer should note
  tripwire-state but no follow-up vendor coverage surfaced in window.
- **PM-001 MacSync / Claude.ai-share-abuse / Beagle TTP-pattern signal**
  — NEW raw-signal-this-sweep, watchlist-edge admission. Grader to
  decide finding-grade treatment.

## Awareness pile (carry-forward from prior sweeps, not raw-signaled)

- **UNC6692 (Snow Flurries)** — Mandiant + Microsoft Teams social
  engineering campaign; not in `_roster.yaml`. Potential `/new-actor`.
- **UNC1069** — DPRK-nexus npm Axios supply chain attack; not in
  `_roster.yaml`. Potential `/new-actor`.
- **DarkSword (Star Blizzard)** — Proofpoint iOS exploit chain; Star
  Blizzard alias not in `_roster.yaml`. Potential `/new-actor`.
- **UAT-8302** — Talos China-nexus APT vs South America / SE Europe
  government targets; not A&D-prime targeting; potential `/new-actor`.
- **HiddenLayer Hugging Face supply-chain pattern** — potential
  `source-grades.yaml` expansion candidate.

## Extraction notes

- Language: en
- Article type: collection sentinel (no source article)
- Raw IOC extraction invoked: no (PM-001 is the in-window raw-signal
  carrying the IOC enrichment for the sweep's one filter-passing item;
  this sentinel carries the sweep-level metadata only)

## IOCs

None extracted at the sentinel level — see `raw-2026-05-10-pm-001-mac-malvertising-claude-ai-share-abuse.md` for the 7 IOCs (3 domains, 2 claude.ai-share URLs, 2 SHA256 hashes) admitted on TTP-pattern-overlap watchlist-edge framing.
