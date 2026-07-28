---
raw_id: raw-2026-07-28-am-000
collected_at: 2026-07-28T07:33:00-04:00
run_id: pre-brief-20260728-073000
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
triage_tags: [sweep_sentinel, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
grader_reviewed: true
grader_reviewed_at: 2026-07-28T08:12:00-04:00
grader_disposition: no_promotion_sweep_sentinel
grader_note: "Pre-brief sweep coverage record — no promotable claim of its own. In-window matches handled separately: Arista CVE-2026-16812 state change promoted via raw-2026-07-28-am-001 -> finding-2026-07-28-0001; Fastjson CVE-2026-16723 continuing-coverage already promoted at finding-2026-07-28-flash-0600-0001 (not re-promoted). Not logged to _rejection-log.yaml (sentinel, not an ineligible claim)."
ttl_expires_at: 2026-10-26T07:33:00-04:00
---

# Pre-brief collection sweep sentinel — 2026-07-28 morning (07:30 EDT)

Window: **2026-07-27T17:30:00-04:00 → 2026-07-28T07:30:00-04:00** (14h, since the
15:30 EDT afternoon pre-brief collection).

## Sources queried (healthy)

RSS/feed sweep: bleepingcomputer, securityweek, the-record, sans-isc, mstic
(microsoft.com parent feed), unit42 (feedburner), krebs, rapid7, cisa-advisories
(all.xml), cisa-kev (JSON, WebFetch). All returned HTTP 200 / parsed clean.

## Sources skipped (stale, per source-health)

- **mandiant** — feedburner RSS 404 (long-running; direct cloud.google.com HTML is the
  working path, not swept this pre-brief). stale_since 2026-06-13.
- **msrc** — feed parse error (stale_since 2026-05-30); MSRC content reaches corpus via relays.
- **ars-security** — security-specific feed retired (stale_since 2026-05-09); root-feed workaround.
- Enrichment APIs (shodan/VT/etc.) not swept in pre-brief scope (on-demand / enrichment only).

## In-window items evaluated and DISCARDED (no watchlist / roster / vuln-index hit)

- **BleepingComputer:** "Data breach at medical billing firm MCBS affects 1.26 million people"
  (healthcare data breach; no A&D / no actor / no tracked CVE / no IOCs) — DISCARD.
- **SecurityWeek (9 in-window):** Microsoft MAI-Cyber-1-Flash AI model launch; Hacker
  Conversations (Tal Kollander interview); Act Security stealth exit; Hush Security $30M funding;
  **"Google Adopts New Threat Actor Naming System"** (CTI-meta / awareness — Google two-word
  naming convention; no specific tracked actor/vuln/A&D hit, DISCARD but flagged for awareness
  below); Origin Energy data breach (900k Australians; energy-sector breach, no A&D/actor/CVE);
  "Skynet Day" rogue-AI-hacked-startup (AI incident, no match). All DISCARD except the two
  vuln-cluster items handled below.
- **SANS ISC (2 in-window):** "AutoIT Payload Injector" diary (generic malware technique, no
  tracked actor/CVE/A&D); Tuesday Stormcast podcast (no body content). DISCARD.
- **Rapid7 (1 in-window):** Exclusive Networks Benelux distribution-partnership announcement
  (marketing, non-threat-intel). DISCARD.
- **The Record / MSTIC / Unit42 / Krebs / CISA advisories:** 0 in-window items.

## In-window MATCHES (handled)

1. **Arista VeloCloud Orchestrator CVE-2026-16812** — net-new STATE CHANGE (patch release +
   CVSS 10.0 confirmation + 3 IOC IPs). Raw-signaled → **raw-2026-07-28-am-001**.
2. **Fastjson CVE-2026-16723** — continuing-coverage / independent-outlet corroboration of the
   06:00 FLASH item (already raw-2026-07-28-flash-0600-001, already promoted to
   finding-2026-07-28-flash-0600-0001). NOT re-raw-signaled (anti-noise); see grader note below.

## Awareness-only (not raw-signaled)

- **"Google Adopts New Threat Actor Naming System"** (SecurityWeek, 2026-07-28 04:42 EDT): Google
  is adopting a new two-word threat-actor naming convention (memorable term + cluster-category
  word). Relevant to CTI tradecraft / future actor-alias resolution across the roster, but no
  specific tracked actor, vuln, or A&D entity in scope this window. Flagged for orchestrator /
  actor-profiler awareness — may warrant a doctrine/alias-mapping note if Google's naming
  migration renames roster-tracked clusters (e.g. Mandiant UNC-series consolidation).

## Grader notes

- **Fastjson CVE-2026-16723 continuing coverage:** BleepingComputer (Bill Toulas, "Hackers
  target US firms in FastJson RCE zero-day attacks", 2026-07-27T19:49 EDT) + SecurityWeek (Ionut
  Arghire, 2026-07-28T03:27 EDT) provide **two publisher-independent B-grade relays** on the same
  active-exploitation topic already promoted to finding-2026-07-28-flash-0600-0001. BleepingComputer
  independently confirms: **US firms primary target** (limited Singapore + Canada), sectors =
  financial services / healthcare / computing / retail / business; **no patch** (1.x EOL,
  unmaintained); ThreatBook + Imperva as the exploitation-telemetry originators; **no actor
  attribution; no IOCs published**. Adds outlet-independence weight but NO substantively new facts
  beyond the FLASH raw-signal. Grader may fold as corroboration into the existing finding.
- **CISA KEV catalog v2026.07.27** (dateReleased 2026-07-27T19:00Z) directly retrieved: the only
  2026-07-27 adds are CVE-2026-16812 (Arista VeloCloud) and CVE-2025-68686 (Fortinet FortiOS) —
  BOTH already collected 2026-07-27 PM (raw-2026-07-27-pm-002 / -pm-003) and covered in the
  2026-07-27 afternoon brief. **No 2026-07-28-dated KEV adds.** Fastjson CVE-2026-16723 confirmed
  NOT in KEV (rapid-KEV watch remains active per VT-052).
