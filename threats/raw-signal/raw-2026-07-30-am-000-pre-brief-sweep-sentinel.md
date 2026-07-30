---
raw_id: raw-2026-07-30-am-000
collected_at: 2026-07-30T07:40:00-04:00
run_id: pre-brief-20260730-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: multiple
  source_name: "Pre-brief sweep sentinel — all healthy sources"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sweep_sentinel, non_flash, coverage_record]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-28T07:40:00-04:00
---

# Pre-brief collection sweep sentinel — 2026-07-30 morning (07:30 EDT)

Window: **2026-07-29T17:30:00-04:00 → 2026-07-30T07:30:00-04:00** (14h, since the 15:30 EDT
afternoon pre-brief). Overlaps the 18:00 / 00:00 / 06:00 EDT FLASH sweeps (all cleared 0
FLASH candidates; the 06:00 sweep filed one below-bar UPDATE, see anti-noise).

**Net result: 2 net-new content raw-signals this pre-brief** (both below FLASH bar, grader queue):
- **raw-2026-07-30-am-001** — Unit 42 (A): Chinese-speaking actor "knaithe"/"KnYuan" autonomous
  AI-driven exploitation across 7 critical CVEs (emerging TTP; filter-marginal, surfaced on
  A-grade + emerging-tradecraft + critical-CVE-cluster grounds).
- **raw-2026-07-30-am-002** — Rapid7 ETR (A): firms VMware vCenter CVE-2026-59309 / -59310 at
  **CVSS 9.8 unauth** (UPDATE to yesterday's raw-2026-07-29-pm-003 SecurityWeek relay).

## Sources queried (healthy)

RSS/feed sweep via `fetch_feed` (all HTTP 200, parsed clean):
- **bleepingcomputer** — 3 in-window (15 in feed): all already-covered/anti-noise or discard (below).
- **securityweek** — 6 in-window (10 in feed): 1 net-new (Analog Devices, discarded); 5 already
  evaluated in the 06:00 FLASH sweep (anti-noise).
- **unit42** (feedburner) — 1 in-window: **raw-signaled am-001** (autonomous-AI exploitation).
- **rapid7** — 1 in-window: **raw-signaled am-002** (VMware vCenter ETR).
- **the-record** — 0 in-window (5 in feed).
- **sans-isc** (rssfeed.xml) — 2 in-window: Stormcast podcast (awareness-only) + SSH-miner-bot guest diary (discard).
- **krebs** — 0 in-window (10 in feed).

Authoritative CVE/KEV surface: **cisa-kev** JSON direct read (catalog v2026.07.29, released
2026-07-29T18:45Z). First-party **Splunk** (both indices) queried — see Trigger 3 below.

## Source-health changes this sweep

- **None.** All queried RSS/media/KEV/Splunk sources HTTP 200, remain `healthy`; no flips, no
  new failures, no recoveries. (mstic's single 403 from the 2026-07-29 AM sweep was not
  re-tested this pre-brief — no fresh CVE/actor lead in window required an MSTIC direct pull;
  `failure_count` carried at 1, held healthy. Flagged for next-sweep retry.)

## Sources skipped (stale, per source-health)

- **mandiant** — feedburner RSS 404 (long-running; cloud.google.com direct-HTML is the working path, not swept this pre-brief). stale_since 2026-06-13.
- **msrc** — feed parse error (stale_since 2026-05-30); content reaches corpus via relays.
- **ars-security** — security-specific feed retired (stale_since 2026-05-09); root-feed workaround.
- **github-advisories** — global advisories.atom 406 (per-repo GHSA fallback available; not triggered this sweep).
- **dragos** — /blog/feed/ soft-fail (not stale; multi-day cadence; not retried this pre-brief).
- **x-cisagov / x-gossithedog** — nitter-bridge stale; not swept.
- Enrichment APIs (shodan / VT / abuseipdb) — not swept in pre-brief scope (no surviving IOC set required enrichment).

## In-window MATCHES — already covered (ANTI-NOISE, not re-signaled)

1. **"Russian hackers exploit Exchange OWA zero-day for long-term mailbox access"**
   (BleepingComputer, Ionut Ilascu, 2026-07-29T19:44 EDT) — Laundry Bear / Void Blizzard
   exploiting **Exchange OWA CVE-2026-42897** (tracked **VT-008**) to deliver the **OWAReaper**
   backdoor for persistent mailbox access. **Already raw-signaled** at
   **raw-2026-07-29-flash-1200-001** (Proofpoint primary; aerospace among named sectors; HELD as
   UPDATE to finding-2026-07-23-0003 for the afternoon brief per commit 1f213de). This is a
   **second-outlet (BleepingComputer) corroboration** with a net-new framing angle
   ("long-term mailbox access" / OWAReaper persistence). Anti-noise — NOT re-signaled; flagged
   for the grader as **outlet-independence corroboration** to fold into the existing item.
   (Neither "Laundry Bear" nor "Void Blizzard" is on `_roster.yaml`; Void Blizzard has prior
   corpus context via the 2026-06-11 DOJ indictment finding.)
2. **"Cisco warns of FMC static credential flaw exploited in zero-day attacks"**
   (BleepingComputer, Lawrence Abrams, 2026-07-29T17:35 EDT) — **CVE-2026-20316**. Already
   raw-signaled (raw-2026-07-29-pm-001 KEV add + raw-2026-07-30-flash-0600-001 patch/exploitation
   UPDATE). Second-outlet relay; anti-noise. CVSS 5.3 (below FLASH-1 floor), patched.
3. **SecurityWeek 06:00-window items** (Ruflo/RufRoot CVE-2026-59726 CVSS 10.0 patched no-ITW;
   "1 in 5 Data Center Assets"; "US and Allies Update SBOM Guidance"; "Chrome 151 Patches 370
   Vulnerabilities"; "Cisco Secure FMC Zero-Day") — all evaluated + dispositioned in the
   06:00 FLASH sweep (raw-2026-07-30-flash-0600-000). Anti-noise.

## In-window items evaluated and DISCARDED (no watchlist / roster / vuln-index hit)

- **SecurityWeek — "Semiconductor Firm Analog Devices Discloses Data Breach"** (Eduard Kovacs,
  2026-07-30T07:16 EDT; **only net-new SecurityWeek item since the 06:00 sweep**): hackers
  detected on ADI systems, breach detection **2026-06-23**; **ExfilSquad** claimed 570,000
  records (data-theft group, no file-encryption; claim since removed from their leak site).
  **ExfilSquad is not a roster actor**; **no A&D/defense customer or product named**; no CVE;
  no IOCs; ADI states no operational disruption / not expected to be material. Analog Devices is
  **not** a watchlist entity. **DISCARD** per Mode 1. *Awareness note:* ADI is a major
  semiconductor supplier whose components appear in defense/aerospace systems (DIB
  supply-chain-adjacent) — below the raw-signal bar this window (no A&D-named exposure, no
  attribution to a tracked actor), but flagged for orchestrator/grader awareness if the
  semiconductor-supply-chain angle warrants watchlist consideration.
- **SANS ISC — "Reconnaissance First: An SSH Bot That Sizes Up Your Hardware Before Deploying a
  Miner"** (guest diary, 2026-07-30T00:42 EDT): commodity SSH cryptomining bot; no
  A&D/roster/tracked-CVE match; no atomic IOCs surfaced in the RSS layer. **DISCARD.**
- **BleepingComputer — "Anthropic confirms Claude is down worldwide"** (2026-07-29T21:39 EDT):
  AI-service outage, not threat intel. **DISCARD.**
- **SANS ISC Stormcast** (2026-07-30 daily podcast): awareness-only, no body content. Not signaled.

## KEV state (verified this sweep)

CISA KEV JSON direct read (catalog **v2026.07.29**, released 2026-07-29T18:45Z): **no
2026-07-30 dated adds.** Only 2026-07-29 add is **CVE-2026-20316** (Cisco Secure FMC, dueDate
2026-08-01) — already captured. Recent context: **CVE-2026-16812** (Arista VeloCloud
Orchestrator, CVSS 10.0) KEV/BOD-22-01 **dueDate is TODAY 2026-07-30** (already covered,
morning-brief 2026-07-29 lead); CVE-2025-68686 (Fortinet FortiOS, 2026-07-27, due 2026-08-10).
**No net-new KEV trigger material** for the morning brief.

## First-party Splunk (Trigger 3 negative)

Both indices queryable. Sentinel query `(index=archimedes OR index=defenseclaw_local) NOT
sourcetype=archimedes:*` over -14h → **0 events**, both indices. Targeted IOC/CVE sweep
(CVE-2026-59309/-59310/-47876/-20316/-16812/-42897/-33017/-3055 + OWAReaper + "Hermes Agent" +
knaithe + code.newcli + ExfilSquad) over -14h → only **2 `archimedes:operation`** internal
self-references (our own pipeline logs echoing CVE IDs), **0 `defenseclaw_local`** hits. Not
defender telemetry → **Trigger 3 does NOT fire.** Metadata-only per LEGAL-POLICY §Data Handling.

## Refusals / policy considerations

None. No prohibited query patterns, no active-scan requests, no authorized-targets implicated,
no credentials stored (the Cisco FMC "hard-coded password" and Analog Devices "records" are
class descriptors / breach-scope counts, not credential values — Hard Rule 7 preserved). Unit
42 CVEs recorded by ID only, no PoC/exploit mechanism copied (Hard Rule 3). No attribution
originated — knaithe/KnYuan and Laundry Bear/Void Blizzard attributions recorded verbatim from
their sources (Hard Rule 2).
