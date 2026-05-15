---
raw_id: raw-2026-05-15-0000-flash-sweep-clean
collected_at: 2026-05-15T00:10:00-04:00
run_id: flash-sweep-20260515-000000
collection_mode: flash_sweep
source:
  source_yaml_id: meta-sweep-tombstone
  source_name: "FLASH sweep tombstone (no candidates)"
  source_url: null
  published_at: 2026-05-15T00:00:00-04:00
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: []
  keywords: ["Mistral AI", "Mini Shai-Hulud continuation"]
triage_tags: [flash_sweep_clean, audit_trail, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-13T00:10:00-04:00
test: false

sweep_summary:
  sweep_window_start: 2026-05-14T18:00:00-04:00
  sweep_window_end: 2026-05-15T00:00:00-04:00
  sweep_window_hours: 6
  scope_rationale: "Async FLASH sweep per orchestrator instruction. Prior FLASH was 18:00 EDT clean (0 triggers / 15 sources). 16:00 afternoon brief shipped 6h before sweep (Cisco SD-WAN CVE-2026-20182 UAT-8616 KEV 3-day deadline; MSTIC Kazuar / Secret Blizzard architectural; Salt Typhoon Azerbaijan carry-forward + Twill Typhoon FDMTP; OpenAI TanStack confirmation; node-ipc UNATTRIBUTED). Quiet hours: 00:00 EDT IS outside the 09:00–21:00 EDT active window — any FLASH would queue to flash-queue.yaml, not post immediately."
  sources_queried: 15
  sources_skipped_stale: 0
  sources_blocked_this_sweep: 1          # cisa.gov advisories WebFetch direct (CISA KEV JSON pulled successfully — no in-window additions beyond Cisco SD-WAN already absorbed in 16:00 brief)
  items_fetched_in_window: 1
  items_already_covered_anti_noise: 0
  items_evaluated_against_flash_triggers: 1
  flash_candidates: 0
  brief_update_candidates_for_morning: 1
  source_health_changes: []
---

# FLASH sweep 2026-05-15 00:00 EDT — clean (0 triggers, 1 brief-update candidate)

**0 FLASH triggers fired. 1 brief-update candidate recorded for the 2026-05-15 08:00 morning brief (TeamPCP / Mistral AI ~5GB / ~450 internal repos data-sale claim — continuation of Mini Shai-Hulud / TanStack already absorbed in 16:00 afternoon brief via finding-2026-05-14-0008). Window: 2026-05-14 18:00 EDT → 2026-05-15 00:00 EDT (6 hours, post-afternoon-brief + post-18:00-FLASH-clean).**

Quiet hours: 00:00 EDT is OUTSIDE the 09:00–21:00 EDT active window. Had a FLASH fired, it would have queued to `infrastructure/flash-queue.yaml` for 09:00 catchup, not post immediately. No critical-override conditions met.

## Sweep window

2026-05-14T18:00:00-04:00 → 2026-05-15T00:00:00-04:00 (6h, post-afternoon-brief + post-18:00-FLASH)

## Sources queried (15)

Priority A-grade primary research + Tier-1 vendor PSIRTs + CISA + first-party Splunk:

- **CISA KEV catalog (JSON feed)** — pulled successfully. ONE entry on or after 2026-05-14: CVE-2026-20182 Cisco Catalyst SD-WAN auth bypass (dateAdded 2026-05-14, dueDate 2026-05-17, 3-day federal deadline) — already absorbed in 16:00 afternoon brief (finding-2026-05-14-0005). No fresh KEV additions in the 18:00→00:00 window.
- **CISA advisories all.xml (RSS)** — 0 items in window.
- **Cisco Talos blog (RSS)** — 0 items in window.
- **Palo Alto Unit 42 (RSS)** — 0 items in window. Most recent feed-published date is 2026-05-14T20:26 UTC (16:26 EDT, pre-window).
- **Microsoft MSTIC (Security Blog RSS)** — 0 items in window. Most recent feed-published is 2026-05-14T21:51 UTC (17:51 EDT, pre-window).
- **Mandiant Google Threat Intel (cloud.google.com index page WebFetch)** — index page shows same top-3 visible posts as the 18:00 sweep (GTIG AI Threat Tracker, UNC6692 Snow Flurries, "Defending Your Enterprise When AI Models Can Find Vulnerabilities Faster Than Ever"); all triangulated out-of-window per prior sweeps. Feedburner endpoint remains 404 (twenty-plus consecutive failure pattern — held healthy pending operator alt-endpoint decision per source-health.yaml).
- **CrowdStrike blog (RSS)** — feed returns 10 items but with NO `published` timestamps in any item. Manual triangulation by title against today's brief / prior sweep titles: top item "Falcon AIDR Detects Threats at the Prompt Layer in Kubernetes AI Applications" + "May 2026 Patch Tuesday: 30 Critical Vulnerabilities Among 130 CVEs" + "Inside CrowdStrike Automated Leads" + 7 product / marketing posts — none are net-new APT campaign / attribution content. None match A&D watchlist, none match tracked-actor names not already covered.
- **SentinelOne Labs (RSS)** — 0 items in window. Most recent last-modified 2026-05-14T20:22 UTC (16:22 EDT, pre-window).
- **Sophos Threat Research (RSS)** — 0 items in window.
- **ESET WeLiveSecurity (RSS)** — 0 items in window.
- **Wiz Research (RSS attempt)** — feed URL https://www.wiz.io/blog/rss.xml returns 404; no in-window items via this endpoint. Wiz primary research on Mini Shai-Hulud / TeamPCP campaign already absorbed via finding-2026-05-12-FLASH-0001; no new Wiz post on the TeamPCP / Mistral sale claim visible in window via search.
- **BleepingComputer (RSS)** — 1 in-window item: "TeamPCP hackers advertise Mistral AI code repos for sale" (Ionut Ilascu, 2026-05-14T18:50 EDT). Evaluated against triggers below — see Item 1.
- **The Hacker News (RSS)** — 0 items in window.
- **The Record (Recorded Future, RSS)** — 0 items in window.
- **SecurityWeek (RSS)** — 0 items in window. Most recent last-modified 2026-05-14T17:23 UTC (13:23 EDT, pre-window).
- **Krebs on Security (RSS)** — 0 items in window. Most recent last-modified 2026-05-13T10:43 UTC (pre-window).
- **SANS Internet Storm Center (RSS)** — 0 items in window.

First-party telemetry:

- **Splunk `archimedes` + `defenseclaw_local`** — last-24h sweep returned 36 events: `archimedes:operation` × 22 + `archimedes:scheduler` × 14. Zero events in `defenseclaw_local`. Zero tracked-IOC matches against the corpus IOC set (PAN-OS / MuddyWater / Ivanti EPMM / FamousSparrow / TeamPCP / node-ipc / Cisco SD-WAN / Fragnesia). 25th consecutive dormant sweep with the non-archimedes-internal stream. Per Hard Rule 8: silence is absence of evidence, not evidence of absence.

## Items evaluated against FLASH triggers

### Item 1 — TeamPCP advertises ~5GB / ~450 Mistral AI internal repos for sale ($25K BIN) [BleepingComputer 18:50 EDT + multiple media corroborations]

- TeamPCP forum post: ~450 internal repositories, ~5GB, $25,000 BIN, one-week leak deadline.
- Mistral AI confirms compromise of "codebase management system" on 2026-05-12 via "third-party software supply chain attack" — scope language: "non-core code repositories; no hosted services / managed user data / research and testing environments compromised."
- Mechanism: same as Mini Shai-Hulud / TanStack campaign per finding-2026-05-12-FLASH-0001 — stolen CI/CD credentials → codebase management system access → exfiltration.
- Multi-victim picture: Mistral is the SECOND named-enterprise victim publicly confirmed (after OpenAI per finding-2026-05-14-0008).
- Enterprise artifact named in disclosed sample: pfizer-rfp-2025.tar.gz (pharma-RFP context; NOT A&D).
- NO A&D-watchlist company named.

**Trigger evaluation:**

- **Trigger 1 (critical CVE + active exploitation + A-grade primary) — N/A.** No CVE in this surface.
- **Trigger 2 (new attribution for tracked actor) — FAILS.** TeamPCP IS in roster (#001, HIGH threat-level), but the TeamPCP-to-Mini-Shai-Hulud/TanStack attribution was established by Wiz / Snyk / StepSecurity in finding-2026-05-12-FLASH-0001. The current surface is a CONTINUATION of an already-attributed campaign (data-sale monetization stage), not a new attribution. The TeamPCP self-claim of the Mistral sale is a tautological self-attribution; not an A/B-grade vendor attribution. Fails the "new attribution" predicate per FLASH-POLICY trigger-2 conditions_all `attribution_is_new_not_restatement == true`.
- **Trigger 3 (first-party IOC hit, Splunk within 24h) — FAILS.** Splunk sweep returned zero tracked-IOC matches; 25th consecutive dormant sweep on non-archimedes-internal sourcetypes.
- **Trigger 4 (tracked actor TTP change, A/B-grade source) — FAILS.** No new tooling, no new infrastructure, no new C2, no new targeting class. Mechanism (CI/CD credential theft → codebase management system access → exfiltration) was already documented. Data-sale monetization is a downstream cybercriminal pattern, not a TTP change. Source grade for the sale-claim itself is B (BleepingComputer / HackRead / Cybernews / TechNadu media tier); no A-grade vendor primary research has surfaced on the sale claim within window.
- **Trigger 5 (active A&D-sector campaign, multi-victim, A&D sector) — FAILS.** Multi-victim picture YES (Mistral + TanStack + OpenAI), but no A&D-watchlist company named. Pfizer-rfp filename is pharma-enterprise-RFP context, not A&D. No defense prime referenced.
- **Trigger 6 (zero-day no patch) — FAILS.** No zero-day in this surface.

**24h anti-noise lockout:** Mini Shai-Hulud / TanStack / TeamPCP campaign was absorbed in finding-2026-05-12-FLASH-0001 (original FLASH) + finding-2026-05-14-0008 (OpenAI named-victim confirmation, 16:00 afternoon brief). 24h lockout window to ~2026-05-15 16:00 EDT in effect (relative to most recent absorbing brief).

**Critical override evaluation:** Conditions all four required:
- CVSS 10.0 — N/A (no CVE)
- Confirmed active exploitation — YES (Mini Shai-Hulud is actively exploited)
- Attributed to a tracked actor — YES (TeamPCP, roster #001 HIGH)
- A&D watchlist entity named as a target — **NO** (Mistral is AI/research; no defense primes named)

3 of 4 conditions met. Override does NOT apply (requires all 4 simultaneously).

**Disposition: BRIEF-UPDATE candidate for 2026-05-15 morning brief.** Material to corpus as Mistral = named-victim #2 + first publicly disclosed data-monetization stage of the Mini Shai-Hulud / TanStack campaign. Raw-signal file written: `raw-2026-05-14-flash-2200-001-teampcp-mistral-ai-450-repos-sale.md`. Not FLASH-eligible per the anti-noise rule (one FLASH per trigger topic per 24h; campaign already absorbed in 16:00 afternoon brief), per Trigger 2 failure (no NEW attribution), per Trigger 4 failure (no NEW TTP), and per Trigger 5 failure (no A&D-watchlist victim named).

## Hard Rule 8 — First-party Splunk

Clean across `archimedes` and `defenseclaw_local` over -24h. 36 events returned (`archimedes:operation` × 22 + `archimedes:scheduler` × 14). Zero events in `defenseclaw_local`. Zero tracked-IOC matches across the corpus IOC set. 25th consecutive dormant sweep with the non-archimedes-internal stream. Per doctrine: silence is absence of evidence, not evidence of absence.

## Quiet-hours and critical-override audit

- **Quiet hours:** 00:00 EDT is OUTSIDE the 09:00–21:00 EDT active window. Had a FLASH fired this sweep, it would have queued to `infrastructure/flash-queue.yaml` with `expires_at: 2026-05-15T12:00:00-04:00` (queue time + 12h) for 09:00 catchup processing.
- **Critical override (all 4 required):** TeamPCP / Mistral surface meets 3 of 4 (active exploitation, tracked actor TeamPCP #001, but no CVSS 10.0 and no A&D-watchlist entity named). Override does NOT apply.

## Anti-noise / 24h-lockouts in effect

- **TeamPCP / Mini Shai-Hulud / TanStack / Mistral / OpenAI** — absorbed in 2026-05-14 16:00 afternoon brief (finding-2026-05-14-0008) and earlier finding-2026-05-12-FLASH-0001. 24h lockout to ~2026-05-15 16:00 EDT.
- **Cisco SD-WAN CVE-2026-20182** — absorbed in 16:00 afternoon brief (finding-2026-05-14-0005). 24h lockout to 2026-05-15 16:00 EDT. CISA KEV 3-day deadline (dueDate 2026-05-17) carry-forward in morning brief.
- **MSTIC Kazuar / Secret Blizzard architectural** — absorbed in 16:00 afternoon brief. 24h lockout to 2026-05-15 16:00 EDT.
- **Salt Typhoon / FamousSparrow Azerbaijan O&G** — FLASHed 2026-05-13 14:30 + carry-forwarded in 16:00 brief. Lockout expired ~2026-05-14 16:00 (24h from original FLASH).
- **Twill Typhoon / Mustang Panda FDMTP** — absorbed in 16:00 afternoon brief. 24h lockout to 2026-05-15 16:00 EDT.
- **node-ipc UNATTRIBUTED** — absorbed in 16:00 afternoon brief. 24h lockout to 2026-05-15 16:00 EDT.
- **ESET FrostyNeighbor / UNC1151** — absorbed in 08:00 morning + 16:00 afternoon mention. 24h lockout to 2026-05-15 16:00 EDT.
- **PAN-OS CVE-2026-0300** — FLASHed twice 2026-05-06; deep coverage. Only fresh material would resurface.
- **MuddyWater / Symantec / ChromElevator** — absorbed in 2026-05-13 FLASH 18:00. Source-finding 72h ratification clock to 2026-05-16 18:25 EDT.

## Source-health changes this sweep

**None.** No status flips. No failure-count increments worth recording (Wiz feed URL 404 is documented endpoint issue, not source degradation — Wiz's primary research surfaces remain reachable via direct WebFetch / search). All A-grade vendor feeds queried remain healthy with normal cadence.

## Disposition

**Return: 0 candidates — clean sweep with 1 brief-update item recorded.** Pass nothing forward to grader / red-team / briefer for FLASH. The TeamPCP / Mistral AI raw-signal file is recorded for the 2026-05-15 morning brief collection cycle / grader review. No queue insertion required (00:00 EDT outside active hours; no FLASH fired regardless).

**Continuing-coverage items for 2026-05-15 07:30 collection cycle / 08:00 morning brief:**

- TeamPCP / Mistral AI ~450 repos / $25K BIN sale claim (NEW — raw-signal written this sweep)
- Cisco SD-WAN CVE-2026-20182 KEV deadline T-2 (2026-05-17)
- OpenAI TanStack 30-day cert-rotation window status
- Burst Statistics WordPress CVE-2026-8181 ~7400 attempts/24h (from prior 18:00 sweep)
- Sandworm OT/ICS Nozomi retrospective (from prior 18:00 sweep)
- MuddyWater 72h ratification clock T-3 (2026-05-16 18:25 EDT)
