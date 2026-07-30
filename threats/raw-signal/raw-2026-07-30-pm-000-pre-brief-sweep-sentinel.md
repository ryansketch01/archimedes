---
raw_id: raw-2026-07-30-pm-000
collected_at: 2026-07-30T15:35:00-04:00
run_id: pre-brief-20260730-153000
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
triage_tags: [sweep_sentinel, pre_brief, afternoon, coverage_record]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-10-28T15:35:00-04:00
---

# Pre-brief collection sweep sentinel — 2026-07-30 afternoon (15:30 EDT)

Window: **2026-07-30T07:30:00-04:00 → 2026-07-30T15:30:00-04:00** (8h, since the 07:30 EDT morning
pre-brief). Overlaps the 12:00 EDT FLASH sweep (cleared 0 FLASH candidates; held the DPRK/Lazarus
SK cluster + Analog Devices breach below-FLASH for this afternoon-brief grader per commit 31dd68d).

**Net result: 5 net-new content raw-signals written this pre-brief** — all below the FLASH bar
(grader queue for the 16:00 afternoon brief):
- **pm-001** — Amazon attributes debug/chalk/axios/typo-crypto **npm supply-chain** compromises to
  DPRK **SapphireSleet / BlueNoroff = Stardust Chollima (roster #002)**.
- **pm-002** — SK agencies + AhnLab: **Lazarus Group (#003)** tool/infra overlap with **Gunra
  ransomware** ("Operation Double Barrel"); includes a **Korean defense-company GaN-semiconductor
  spearphishing lure** (A&D-adjacent).
- **pm-003** — **Broadcom/VMware** patch release: 5 CVEs, 3 critical (CVE-2026-59309 / -59310 @9.8
  auth-bypass + traversal; **CVE-2026-47876 @9.3 VM escape**). UPDATE to the tracked VMware cluster.
- **pm-004** — **Analog Devices** SEC-filed breach (semiconductor; ExfilSquad claim, DIB-supply-
  chain-adjacent; now multi-outlet; held for this board).
- **pm-005** — CISA ICS advisory **NASA cFS Health & Safety App CVE-2026-18064** (CVSS 7.5 DoS;
  **spacecraft flight software** — A&D/aerospace sector).

## Sources queried (healthy)

RSS/feed sweep via `fetch_feed` (all HTTP 200, parsed clean; since-filter 2026-07-30T07:30 EDT):
- **bleepingcomputer** — 7 in-window (15 in feed): pm-001 (DPRK npm), pm-003 (VMware), pm-004 (ADI);
  remainder anti-noise/discard (below).
- **securityweek** — 7 in-window (10 in feed): all funding/M&A/thought-leadership → discard.
- **the-record** — 4 in-window (5 in feed): pm-001 (DPRK npm), pm-002 (Lazarus/Gunra), pm-004 (ADI);
  UK DfE extortion → discard.
- **cisa-advisories** (all.xml) — 12 in-window: pm-005 (NASA cFS) + 10 generic ICS OT advisories
  (batch, not individually signaled) + 1 OSS-security guidance resource → see below.
- **rapid7** — 3 in-window: KindaRails2Shell CVE-2026-66066 (noted, below) + MDR-MarketScape +
  Metasploit 6.5 release → discard.
- **mstic** — 1 in-window ("What's new in Microsoft Security: July 2026") → product marketing, discard.
- **krebs** — 1 in-window (H96 TV-stick ad-fraud, Bitsight) → discard.
- **sans-isc** (rssfeed.xml) — 0 in-window. **unit42** (feedburner) — 0 in-window.

Authoritative CVE/KEV surface: **cisa-kev** JSON direct read (catalog **v2026.07.29**, released
2026-07-29T18:45Z) — **no 2026-07-30 adds**. First-party **Splunk** (both indices) queried — see
Trigger 3 below.

## Source-health changes this sweep

- **None.** All queried RSS/media/CISA/KEV/Splunk sources HTTP 200, remain `healthy`; no flips, no
  new failures, no recoveries. (mstic returned 200 this sweep — `failure_count` remains 0 from the
  2026-07-29 PM recovery.)

## Sources skipped (stale, per source-health)

- **mandiant** — feedburner RSS 404 (stale_since 2026-06-13); cloud.google.com HTML is the working
  path, not swept this pre-brief.
- **msrc** — feed parse error (stale_since 2026-05-30); content reaches corpus via relays.
- **ars-security** — security-specific feed retired (stale_since 2026-05-09); root-feed workaround.
- **github-advisories** — global advisories.atom 406 (per-repo GHSA fallback; not triggered).
- **dragos** — /blog/feed/ soft-fail (not stale; multi-day cadence; not retried).
- **x-cisagov / x-gossithedog** — nitter-bridge stale; not swept.
- **nvd** — not invoked; the CVE leads this window came from CISA ICS advisory (NASA cFS), Broadcom
  advisory (VMware), and Rapid7 ETR (Rails) directly. Enrichment APIs (shodan/VT/abuseipdb) not
  swept in pre-brief scope (surviving IOC set is CVE-IDs + package/malware names; no atomic
  network IOC required enrichment).

## In-window MATCHES — already covered (ANTI-NOISE, not re-signaled)

1. **VMware vCenter/ESX critical cluster** — the BleepingComputer VMware item is the vendor-patch
   UPDATE to the cluster tracked at raw-2026-07-29-pm-003 + raw-2026-07-30-am-002. Signaled as an
   UPDATE (pm-003), not a new topic — flagged for the grader to fold.
2. **Analog Devices breach** — first evaluated + discarded in the morning sentinel (raw-2026-07-30-
   am-000) as below-bar single-outlet. Now multi-outlet (SecurityWeek + BleepingComputer + The
   Record) + SEC filing, and explicitly held for this board at the 12:00 FLASH → **promoted to a
   raw-signal (pm-004)** so the grader has the material. Not anti-noise-suppressed given the
   outlet-count + SEC-filing state change.

## In-window items evaluated and DISCARDED (no watchlist / roster / vuln-index hit)

- **Rapid7 ETR — "KindaRails2Shell: CVE-2026-66066"** (16:11 UTC): critical **CVSS v4 9.5**
  unauthenticated arbitrary file read → possible RCE in **Ruby on Rails** Active Storage when using
  the **libvips** (Vips) variant processor (Rails 7.0+ default); advisory published by Rails
  2026-07-29. **No active exploitation, patched, no A&D/roster/tracked-vuln match** → DISCARD per
  Mode 1. **Awareness flag for vuln-tracker:** widely deployed framework + unauth + secret-exposure
  →RCE path; monitor for exploitation / KEV. (Not raw-signaled — filter discipline; no matching
  criterion. Recorded here so the surface is not lost.)
- **BleepingComputer — "Microsoft Teams vishing attacks lead to Chaos ransomware"** (15:56 UTC):
  IT-support impersonation → Chaos ransomware vs North American orgs. **Chaos not a roster actor; no
  A&D victim named; no tracked CVE/IOC in the RSS layer.** DISCARD (social-engineering commodity).
- **BleepingComputer — "ShinyHunters claims Brinks Home breach"** (16:46 UTC): ShinyHunters
  non-roster; residential-security company, not A&D; extortion self-claim. DISCARD (ShinyHunters
  recurring across sweeps; still non-roster).
- **BleepingComputer — "Google says AI helped Chrome fix 1,072 security bugs"** (17:00 UTC) +
  Huntress **Sponsored** post: product/vendor content. DISCARD.
- **SecurityWeek** — Okta/Permiso M&A, DataBahn/Cantina/Discern/Onyx **funding**, "Timeless
  Compliance" thought-leadership, and **"DangleGeddon: AI Could Weaponize Forgotten DNS Records"**
  (speculative research, no actor/CVE/A&D/IOC). DISCARD all.
- **The Record — "Cyber extortionists steal data from UK Department for Education"** (12:00 UTC):
  UK-gov extortion (>600k records claimed); no A&D, no roster actor, no CVE/IOC. DISCARD.
- **MSTIC — "What's new in Microsoft Security: July 2026"** (16:00 UTC): product-marketing roundup.
  DISCARD.
- **Krebs — H96 TV-streaming-stick ad-fraud / Fengwo Group** (Bitsight): IoT ad-fraud/residential-
  proxy; no A&D/roster/tracked-CVE. DISCARD.
- **Rapid7 — MDR IDC MarketScape + Metasploit Framework 6.5 release**: vendor/tooling. DISCARD (no
  exploit content copied; Metasploit release noted as tooling announcement only, Hard Rule 3 n/a).
- **CISA ICS batch (non-NASA), 2026-07-30 ICSA-26-211 series** — evaluated, none individually
  signaled (no A&D-named entity, no tracked actor, no active exploitation): Mitsubishi Electric
  CC-Link IE TSN (CVE-2026-13584, DoS); Schneider IGSS (CVE, 7.8 OOB write); **Toptech Systems
  RCU II+/Multiload II+ (CVE-2026-12562, 8.8 missing-auth root)**; MikroTik RouterOS (CVE-2026-14227,
  4.9); Watchfire Controller (CVE-2026-5846, 5.7 hard-coded key); Johnson Controls OpenBlue (2.4);
  MZ Automation libiec61850 (8 CVEs, 7.5) + lib60870 (6.5); Rockwell Automation Logix / 1756-EN4TR
  (CVE-2026-9636, 5.9); **o6 Automation open62541 (4 CVEs, 8.8 — OPC-UA stack, UAF/integer bugs)**.
  All generic critical-infra OT; handled by the standing ICS-batch surface, not the A&D raw-signal
  queue. Plus CISA **"Open Source Software: Security Principles and Practices"** guidance resource
  (reference doc, not a threat datum) → note only.

## KEV state (verified this sweep)

CISA KEV JSON direct read (catalog **v2026.07.29**, released 2026-07-29T18:45Z): **no 2026-07-30
dated adds.** Most recent add remains **CVE-2026-20316** (Cisco Secure FMC, dateAdded 2026-07-29,
dueDate **2026-08-01**) — already covered (raw-2026-07-29-pm-001 + raw-2026-07-30-flash-0600-001).
Deadline context: **CVE-2026-16812** (Arista VeloCloud Orchestrator, CVSS 10.0) BOD-22-01 **dueDate
was TODAY 2026-07-30** (led the 2026-07-29 morning brief; carried on the board). CVE-2025-68686
(Fortinet FortiOS, due 2026-08-10). **No net-new KEV trigger material** for the afternoon brief.

## First-party Splunk (Trigger 3 negative)

Both indices queryable. Sentinel query `(index=archimedes OR index=defenseclaw_local) NOT
sourcetype=archimedes:*` over -8h → **0 events**, both indices. Targeted IOC/CVE sweep over -24h
(CVE-2026-18064 / -66066 / -59309 / -59310 / -42897 + Lazarus + ExfilSquad + "Analog Devices" +
npm + Chalk + OWAReaper) → **0 events**, both indices. Not defender telemetry → **Trigger 3 does
NOT fire.** Metadata-only per LEGAL-POLICY §Data Handling — no log content copied.

## Refusals / policy considerations

None. No prohibited query patterns; no active-scan requests; no authorized-targets implicated. No
credentials stored (ADI "570,000 records" is a breach-scope claim; Lazarus/Gunra "SSH key
fingerprint" referenced qualitatively with no value present — Hard Rule 7 preserved). CVEs recorded
by ID only; no PoC/exploit mechanism copied (Hard Rule 3 — incl. the Rails CVE-2026-66066 and the
Metasploit 6.5 release). No attribution originated — SapphireSleet=Stardust Chollima, Lazarus<->Gunra
(AhnLab hedge preserved), and ExfilSquad claims all recorded verbatim from their sources
(Hard Rule 2).

## Carry-forward flagged for grader / briefer (afternoon brief)

- **DPRK double-header (roster hits):** Stardust Chollima (#002) npm supply-chain [pm-001] +
  Lazarus (#003)/Gunra ransomware overlap [pm-002] — the "DPRK/Lazarus SK cluster" the 12:00 FLASH
  held. Grader may cluster under a DPRK section; note the GaN-semiconductor Korean-defense lure as
  the A&D-adjacent thread in pm-002.
- **VMware cluster [pm-003]** — CVE-2026-59309/-59310 now vendor-confirmed @9.8 + CVE-2026-47876 @9.3
  VM escape, patched, no ITW. Fold into the tracked cluster; vuln-tracker handoff candidate.
- **NASA cFS CVE-2026-18064 [pm-005]** — A&D/aerospace ✈️ standing-section item; vuln-tracker candidate.
- **Analog Devices [pm-004]** — DIB-semiconductor-supply-chain awareness; ExfilSquad-vs-SEC-breach
  linkage UNCONFIRMED. Orchestrator: consider whether semiconductor-supply-chain warrants watchlist.
- **Rapid7 CVE-2026-66066 (Rails, 9.5 unauth)** — awareness-only (discarded, no match); vuln-tracker
  monitor for exploitation/KEV.
