---
raw_id: raw-2026-05-14-am-000
collected_at: 2026-05-14T07:38:00-04:00
run_id: pre-brief-20260514-073000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-14T07:30:00-04:00
time_window_start: 2026-05-13T17:30:00-04:00
time_window_end: 2026-05-14T07:30:00-04:00
time_window_hours: 14
test: false
source:
  source_yaml_id: meta-sweep-tombstone
  source_name: "Pre-brief sentinel tombstone (sweep summary)"
  source_url: null
  published_at: 2026-05-14T07:30:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [pre_brief_sentinel, audit_trail, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
grader_disposition: sentinel_audit_trail_no_graded_claim
grader_disposition_run_id: morning-20260514-080000
grader_disposition_at: 2026-05-14T08:15:00-04:00
grader_disposition_rationale: "Pre-brief sentinel/tombstone sweep summary; no graded claim. The four enumerated raw-signal items (AM-001 through AM-004) were each individually graded — AM-001 → finding-2026-05-14-0001 (A2), AM-002 → finding-2026-05-14-0002 (A2), AM-003 → finding-2026-05-14-0003 (B2), AM-004 → finding-2026-05-14-0004 (B2). Sentinel is retained as audit-trail evidence of the 07:30 pre-brief collection sweep; not promoted to finding and not logged to rejection log (sentinels are not rejected claims — they are sweep-summary tombstones)."
ttl_expires_at: 2026-08-12T07:38:00-04:00
---

# Pre-brief collection 2026-05-14 07:30 EDT — sweep summary

**4 raw-signal files written (AM-001 ESET FrostyNeighbor, AM-002 NGINX "Rift" CVE-2026-42945, AM-003 Fragnesia CVE-2026-46300, AM-004 PraisonAI CVE-2026-44338). 14h window 2026-05-13 17:30 EDT → 2026-05-14 07:30 EDT bridges yesterday's 18:00 FLASH (Symantec / MuddyWater) through this morning's 06:00 FLASH (clean) through the 07:30 pre-brief collection.**

The 06:00 FLASH sentinel (`2026-05-14-0600-flash-sweep-clean.md`) flagged FOUR BRIEF-UPDATE candidates for handoff to this pre-brief collection: ESET FrostyNeighbor, PraisonAI CVE-2026-44338, Fragnesia CVE-2026-46300, VMware Fusion Pwn2Own. This sweep promotes the first three to raw-signal files and ADDS one (NGINX "Rift" CVE-2026-42945) that surfaced after the 06:00 FLASH in The Hacker News + SecurityWeek F5 advisory coverage between 07:00 and 11:15 EDT. VMware Fusion is held to FLASH-sentinel-only awareness (routine Pwn2Own coverage, no actor / no exploitation / patched at disclosure).

## Sweep window

2026-05-13T17:30:00-04:00 → 2026-05-14T07:30:00-04:00 (14h)

## Sources queried (16 productive + 8 dormant)

A-grade / B-grade RSS feeds + CISA + NVD + Splunk first-party (all in-window):

- **CISA all.xml** — fetch_feed status 200, 30 items total, 0 items in 14h window after since-filter. Most recent advisory pre-window.
- **CISA KEV catalog** (JSON, catalogVersion 2026.05.13, dateReleased 2026-05-13T17:58:37Z) — unchanged from yesterday's 18:00 FLASH baseline. 5 most recent: CVE-2026-42208 BerriAI LiteLLM (2026-05-08), CVE-2026-6973 Ivanti EPMM (2026-05-07), CVE-2026-0300 PAN-OS (2026-05-06), CVE-2026-31431 Linux Kernel (2026-05-01, dueDate 2026-05-15 = tomorrow), CVE-2026-41940 cPanel (2026-04-30, ransomware-use=Known). No 2026-05-13 evening or 2026-05-14 additions. **Important carry-over context for morning brief:** CVE-2026-31431 Linux Kernel ("Copy Fail") BOD-22-01 federal-agency remediation deadline = 2026-05-15 (tomorrow). BleepingComputer's Fragnesia piece references this as actively exploited.
- **NVD** — lastModStartDate 2026-05-14T06:00:00 → 11:30:00 EDT, cvssV3Severity=CRITICAL returned 2 entries: CVE-2025-11024 + CVE-2026-2347, both 9.8, both Akilli Commerce Software Technologies Ltd. Co. e-commerce platform <4.5.001 (Turkish e-commerce vendor). NOT A&D / NOT tracked-vuln / NOT roster-actor / NOT Linux/networking/Microsoft. DISCARDED per Mode 1 procedure. Earlier-in-window NVD 06:00 FLASH absorbed 4 CVSS 9.8 Critical WordPress plugin auth-bypass / arbitrary-file-upload / privesc CVEs (Burst Statistics + Career Section + InfusedWoo Pro x2) — all sub-Trigger-1 no-active-exploitation. NVD endpoint healthy and responsive.
- **Mandiant / Google Threat Intel index page** (cloud.google.com/blog/topics/threat-intelligence) — top-of-list visible items unchanged from 06:00 FLASH (UNC1069 Axios npm 2026-03-31 article is featured-back-to-top editorial, NOT a fresh publication). Mandiant feedburner remains 404 (twentieth+ consecutive failure pattern; held healthy pending operator alt-endpoint decision).
- **CrowdStrike blog feed** — fetch_feed status 200, 10 items returned, most dateless (typical of marketing rotation). One technically-fresh item in window: "May 2026 Patch Tuesday: 30 Critical Vulnerabilities Among 130 CVEs" (Falcon Exposure Management Team, 2026-05-12) is ANTI-NOISE — already absorbed in 2026-05-12 afternoon brief (PM-001) and 2026-05-12 morning brief Patch Tuesday cohort. Confirmed via WebFetch direct fetch on /en-us/blog/patch-tuesday-analysis-may-2026/. CrowdStrike continues 20th+ consecutive dateless-marketing pattern; no fresh threat-research content in 14h window.
- **Microsoft MSTIC feed** — `microsoft.com/en-us/security/blog/threat-intelligence/feed/` validate_feed returned 404 (consistent with 06:00 FLASH). Parent feed `microsoft.com/en-us/security/blog/feed/` reachable (status 200, last_modified 2026-05-13T23:29:54 GMT pre-window), 0 items in 14h window. MSTIC threat-intel-specific feed remains held healthy pending next-cycle retry per same 1-of-N sporadic-404 pattern observed in prior sweeps.
- **Palo Alto Unit 42 feedburner** — fetch_feed status 200, 15 items, 0 items in 14h window. Most recent visible item pre-window.
- **Symantec security.com Threat Intelligence index** — top-of-page is still 2026-05-12 Seedworm electronics-maker post (the parent of yesterday's 18:00 FLASH; ANTI-NOISE lockout to 2026-05-14 18:10 EDT). No fresh post-2026-05-13-18:00 publication. Verified via WebFetch.
- **Bitdefender Labs / Business Insights** — top-of-page is still 2026-05-13 FamousSparrow Azerbaijani O&G post (parent of yesterday's 14:30 FLASH; ANTI-NOISE lockout to 2026-05-14 14:30 EDT). No fresh post-2026-05-13-18:00 publication. Verified via WebFetch on businessinsights.bitdefender.com (which now 301-redirects to bitdefender.com/blog/businessinsights — flag for source-grades.yaml URL update on next operator pass).
- **ESET WeLiveSecurity feed** — fetch_feed since-filter returned 0 items in window via en/rss/feed/ endpoint. HOWEVER the FrostyNeighbor article surfaced via 06:00 FLASH WebSearch and direct WebFetch on welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/ — published 2026-05-14, in-window. RSS feed cadence may differ from publish cadence; tagged as productive-via-direct-WebFetch.
- **BleepingComputer RSS** — fetch_feed status 200, 5 items in 14h window after since-filter: (1) Dell SupportAssist BSOD 2026-05-14T06:03 EDT — software defect, NO actor, NO CVE, NO A&D — DISCARDED Mode 1; (2) Dream Market US indictment 2026-05-14T04:55 EDT — LE action, NO threat intel — DISCARDED Mode 1; (3) **Fragnesia CVE-2026-46300 2026-05-14T03:34 EDT — RAW-SIGNALED AS AM-003**; (4) West Pharmaceutical encryption update 2026-05-13T18:23 EDT — pharma single-victim, NO actor — DISCARDED Mode 1 + ANTI-NOISE (PM-005 / 06:00 FLASH discussed); (5) **Iranian / MuddyWater Seedworm South Korean electronics maker 2026-05-13T17:59 EDT — ANTI-NOISE LOCKOUT** (covered in 2026-05-13 18:00 FLASH finding-2026-05-13-FLASH-1800-0001; BleepingComputer relay is Bill Toulas pure-Symantec-relay verified via WebFetch, adds NO new facts not in Symantec primary).
- **SecurityWeek RSS** — fetch_feed status 200, 5 items in 14h window: (1) **G7 AI SBOM Guidance 2026-05-14T07:15 EDT** — international government guidance, NO actor, NO CVE, NO active exploitation — DISCARDED Mode 1 (no watchlist / roster / vuln-index hit; G7 AI-SBOM is governance/policy content for AI supply-chain transparency, not threat-intel; CISA/NSA not named in piece per WebFetch); (2) **F5 patches 50+ vulnerabilities incl. CVE-2026-42945 NGINX Rift 2026-05-14T06:47 EDT — RAW-SIGNALED AS AM-002** (NGINX 18-year-old pre-auth RCE class, broad A&D infrastructure exposure); (3) **PraisonAI CVE-2026-44338 mass-scanner 2026-05-14T05:45 EDT — RAW-SIGNALED AS AM-004**; (4) VMware Fusion Pwn2Own Berlin patch 2026-05-14T04:42 EDT — high-severity patched-at-disclosure, NO actor, NO exploitation — DISCARDED Mode 1 (routine Pwn2Own coverage, FLASH-sentinel awareness only, not raw-signal-worthy); (5) YellowKey/GreenPlasma re-coverage 2026-05-14T03:27 EDT — pure relay of 2026-05-13 BleepingComputer — ANTI-NOISE LOCKOUT (covered in 2026-05-13 16:00 afternoon brief finding-2026-05-13-0003).
- **The Record RSS** — fetch_feed status 200, 0 items in 14h window after since-filter. Most recent items pre-window.
- **Krebs on Security RSS** — fetch_feed status 200, 0 items in 14h window after since-filter. Most recent items pre-window.
- **SANS ISC RSS** — fetch_feed status 200, 10 items, 2 items in 14h window after since-filter: (1) Outlook Junk-folder link-preview bypass diary 2026-05-14T02:08 EDT — defensive operational-hygiene blog, NO threat intel — DISCARDED Mode 1; (2) Stormcast podcast 2026-05-14T00:20 EDT — audio podcast index, NO body — DISCARDED Mode 1.
- **Sophos News blog** — visible content unchanged from 06:00 FLASH (Patch Tuesday recap + AI-deployment defensive guidance + Identity Security survey + GPT-5.5-Cyber post). No tracked-actor attribution, no fresh CVE, no in-window APT analysis. Verified via 06:00 FLASH WebFetch surface; no re-verification this sweep (FLASH-fast scope inheritance).
- **Dragos blog** — most recent visible items remain 2026-05-11 (OT AI) and 2026-05-07 (frontlines lessons). dragos.com/blog/feed/ continues to return 404 (failure_count holds at 1 — soft-fail, not yet stale; consistent with 2026-05-09 collector-discovery + 2026-05-13 00:00 FLASH source-health entry). No post-2026-05-13-17:30 publication identifiable.
- **TheHackerNews** (provisional B media-relay-tier, NOT in source-grades.yaml as a separate id but appears as relay surface across multiple findings) — surfaced two NEW items this sweep that align with primary-source coverage: (1) NGINX "Rift" CVE-2026-42945 framing (depthfirst researcher byline, 18-year exposure, ASLR-dependent code-execution framing) — used to corroborate F5/SecurityWeek coverage in AM-002; (2) Fragnesia CVE-2026-46300 framing — used to corroborate BleepingComputer + Zellic researcher coverage in AM-003. THN is acting as cross-corroboration layer, not originating primary.

First-party telemetry (Splunk):

- **`archimedes` + `defenseclaw_local` last-24h non-archimedes-internal sweep** — `index=archimedes OR index=defenseclaw_local earliest=-24h NOT sourcetype=archimedes:*` returned 0 events. **23rd consecutive dormant sweep** with the non-archimedes-internal stream (extending the 22-consecutive figure logged in yesterday's 06:00 FLASH).
- **Targeted IOC keyword sweep across 18 tokens** (CVE-2026-46300, CVE-2026-44338, CVE-2026-42945, CVE-2026-41089, CVE-2026-41096, Fragnesia, PraisonAI, FrostyNeighbor, Ghostwriter, UNC1151, MuddyWater, Seedworm, FamousSparrow, Salt Typhoon, PicassoLoader, Ukrtelecom, F5, BIG-IP) — 7 hits returned, ALL SEVEN are `archimedes:operation` pipeline self-references from yesterday's 14:30 + 18:00 FLASH cycles (brief_published / flash_published / grade_revision Bitdefender provisional A / git_committed). Pipeline self-references match the searched terms in their payloads (FamousSparrow + Salt Typhoon in the 14:30 Bitdefender FLASH; MuddyWater + Seedworm in the 18:00 Symantec FLASH) but reflect Archimedes' own operational logging, NOT external observations. **Trigger 3 (first-party-ioc-hit) cannot fire on a dormant non-archimedes-internal stream.**

## Items raw-signaled this sweep (4)

| File | Source | Topic | Triage tags |
|---|---|---|---|
| AM-001 | ESET WeLiveSecurity (A) | FrostyNeighbor / UNC1151 / Ghostwriter Belarus APT 2026-03+ campaign vs Ukraine gov + Poland/Lithuania industrial — JavaScript PicassoLoader variant + server-side validation + Cobalt Strike payload; Ukrtelecom-impersonating spearphishing PDFs | brief_update, non_flash, non_roster_actor, possible_new_actor_candidate, ad_sector_no |
| AM-002 | SecurityWeek (B provisional) + TheHackerNews relay | NGINX "Rift" CVE-2026-42945 9.2 — 18-year-old rewrite-module heap buffer overflow, pre-auth RCE class (ASLR-dependent), patches available in NGINX Plus + Open Source + Ingress Controller + App Protect WAF; part of F5 quarterly batch (50+ CVEs) | brief_update, non_flash, cve, ad_sector_indirect, infrastructure_widely_deployed |
| AM-003 | BleepingComputer (B) + TheHackerNews relay + Zellic researcher byline | Fragnesia CVE-2026-46300 — Linux kernel XFRM ESP-in-TCP page-cache-corruption LPE, all pre-2026-05-13 kernels, PoC-only no ITW, kernel-patch-on-netdev + distros rolling, mitigation `rmmod esp4 esp6 rxrpc` (breaks IPsec VPNs + AFS) | brief_update, non_flash, cve, linux_kernel, ad_sector_indirect, poc_published |
| AM-004 | SecurityWeek (B provisional) + Sysdig researcher | PraisonAI CVE-2026-44338 7.3 HIGH — Flask API auth-bypass affects 2.5.6–4.6.33 (patched 4.6.34), mass-scanner probing within 3h44m of disclosure per Sysdig (CVE-Detector/1.0 scanner identifier, ~70 reqs/50s x2 passes), Sysdig's own framing "scanner not interactive exploitation" | brief_update, non_flash, cve, ai_supply_chain, ad_sector_indirect, scanner_observed_not_active_exploitation |

## Items filtered out (10)

Discarded per Mode 1 procedure (no watchlist / roster / vuln-index hit) or anti-noise:

1. **BleepingComputer MuddyWater South Korean electronics maker** (Bill Toulas, 2026-05-13T17:59 EDT) — pure Symantec primary relay, NO new facts, ANTI-NOISE LOCKOUT until 2026-05-14T18:10 EDT (yesterday's 18:00 FLASH covers).
2. **BleepingComputer Dell SupportAssist BSOD** (Sergiu Gatlan, 2026-05-14T06:03 EDT) — software defect, no actor, no CVE, no A&D.
3. **BleepingComputer Dream Market US indictment** (Sergiu Gatlan, 2026-05-14T04:55 EDT) — LE action, not threat intel.
4. **BleepingComputer West Pharmaceutical encryption update** (Bill Toulas, 2026-05-13T18:23 EDT) — pharma single-victim, no actor named, ANTI-NOISE already in 06:00 FLASH brief.
5. **SecurityWeek G7 AI SBOM Guidance** (Eduard Kovacs, 2026-05-14T07:15 EDT) — governance/policy content, no threat actor, no CVE, not threat intel scope.
6. **SecurityWeek VMware Fusion Pwn2Own Berlin patch** (Eduard Kovacs, 2026-05-14T04:42 EDT) — routine Pwn2Own coverage, patched at disclosure, no actor, no exploitation. FLASH-sentinel awareness only; orchestrator may surface as morning-brief routine-patches mention if word-count permits.
7. **SecurityWeek YellowKey/GreenPlasma re-coverage** (Ionut Arghire, 2026-05-14T03:27 EDT) — pure relay of yesterday's BleepingComputer, ANTI-NOISE LOCKOUT (2026-05-13 afternoon brief finding-2026-05-13-0003).
8. **SANS ISC Outlook Junk-folder diary** (2026-05-14T02:08 EDT) — defensive operational hygiene, not threat intel.
9. **SANS ISC Stormcast podcast** (2026-05-14T00:20 EDT) — audio podcast index, no body.
10. **CrowdStrike May 2026 Patch Tuesday analysis** (2026-05-12 publish date surfaced via dateless feed; ANTI-NOISE — covered in 2026-05-12 afternoon brief PM-001).
11. **NVD CVE-2025-11024 + CVE-2026-2347 e-commerce** — Akilli Commerce Turkish vendor, not A&D / not tracked.

## Anti-noise lockouts honored

Per yesterday's brief audit trail and Splunk anti-noise lock topics:

- **FamousSparrow / Salt Typhoon / Azerbaijan O&G Exchange intrusion** — locked out until 2026-05-14 14:30 EDT (yesterday's 14:30 FLASH posted finding-2026-05-13-FLASH-0001). No new in-window material advances this topic.
- **MuddyWater / Seedworm / ChromElevator / SentinelOne fmapp + sentinelmemoryscanner DLL sideloading / Q1 2026 multi-victim** — locked out until 2026-05-14 18:10 EDT (yesterday's 18:00 FLASH posted finding-2026-05-13-FLASH-1800-0001). BleepingComputer Toulas relay (5 hrs post-FLASH) adds NO new facts; Industrial Cyber relay-conflation pattern (the falsely-attached "U.S. defense and aerospace software supplier with Israeli operations" victim claim) holds at NOT-propagated per Hard Rule 2.
- **KongTuke / ModeloRAT / Microsoft Teams + CVE-2023-36036 cldflt.sys / BitLocker YellowKey + GreenPlasma PoCs** — covered in 2026-05-13 16:00 afternoon brief (findings 0003 + 0004). SecurityWeek YellowKey/GreenPlasma piece is pure relay.
- **Mini Shai-Hulud / TeamPCP / npm + PyPI worm** — covered in 2026-05-12 FLASH-0001 finding (24h+ ago, but topic continues at vuln-tracker tracking layer); no fresh in-window material.

## Source-health observations (this sweep)

No status transitions warranted. Notable persistent patterns held healthy:

- **mandiant** — feedburner.com/Mandiant 404 (twenty-first consecutive failure pattern; alt cloud.google.com/blog/topics/threat-intelligence/rss returns malformed body). Held healthy pending operator alt-endpoint decision. Index page top-of-list unchanged (UNC1069 Axios npm 2026-03-31 still featured).
- **mstic** — `microsoft.com/en-us/security/blog/threat-intelligence/feed/` 404 again (consistent with 06:00 FLASH and recurring sporadic-404 pattern; parent `microsoft.com/en-us/security/blog/feed/` reachable but 0 items in window).
- **bitdefender** — top-level URL `businessinsights.bitdefender.com/` now 301-redirects to `bitdefender.com/blog/businessinsights`. Operator should update source-grades.yaml URL on next pass.
- **sophos** — root path `news.sophos.com/` 301-redirected to `www.sophos.com/en-us/blog` on 06:00 FLASH; same pattern this sweep (held; no failure_count increment since not re-tested this FLASH-fast scope).
- **dragos** — `dragos.com/blog/feed/` 404 unchanged (failure_count=1, soft-fail, held healthy). Operator-side working RSS path identification still pending.
- **crowdstrike** — twenty-first consecutive dateless-marketing pattern unchanged; one in-window dateless item is the 2026-05-12 Patch Tuesday analysis (ANTI-NOISE).

Runtime fields advanced this sweep for the productive sources (timestamps updated to 2026-05-14T07:30:00-04:00):
- bleepingcomputer: last_successful_fetch
- securityweek: last_successful_fetch
- the-record: last_successful_fetch (0 in window)
- krebs: last_successful_fetch (0 in window)
- sans-isc: last_successful_fetch
- mstic: last_successful_fetch (parent feed; threat-intel-feed 404 noted in last_error)
- mandiant: failure_count 18→19 (twenty-first consecutive feedburner 404); held healthy pending operator decision
- unit42: last_successful_fetch (0 in window)
- crowdstrike: last_successful_fetch (dateless content, no fresh threat intel)
- bitdefender: last_successful_fetch (verified via WebFetch; no new post)
- symantec: last_successful_fetch (verified via WebFetch; no new post)
- sentinelone: not re-checked this sweep (FLASH-fast inheritance)
- rapid7: last_successful_fetch (0 in window)
- abuseipdb: not invoked this sweep — Fragnesia / PraisonAI / NGINX Rift / FrostyNeighbor IOCs are either: domains (ESET FrostyNeighbor C&C domains went into AM-001 directly; not IP-only enrichable), or CVE-only (no IP IOC layer in AM-002 / AM-003 / AM-004), or already covered (Symantec MuddyWater 4-IOC set, Bitdefender FamousSparrow 12-IOC set already absorbed in prior FLASH cycles).
- shodan: not invoked this sweep — no qualifying IP-or-product-string IOC needs Shodan enrichment for the four BRIEF-UPDATE items.

(`source-health.yaml` not modified by THIS raw-signal file directly — the collector will roll those changes back into source-health.yaml at the librarian stage per Mode 1 procedure.)

## Carry-forward context for 08:00 morning brief

- **CVE-2026-31431 "Copy Fail" Linux Kernel BOD-22-01 deadline = 2026-05-15 (TOMORROW).** Already KEV-listed since 2026-05-01; due date one day out. BleepingComputer's Fragnesia piece cross-references this as "actively exploited and flagged by CISA for federal agency remediation by May 15." This is a useful Linux-kernel-deadline anchor for the morning brief's defensive-posture section, especially in combination with AM-003 Fragnesia PoC release (both Linux kernel privesc class within 13 days).
- **CVE-2026-42945 NGINX "Rift" (AM-002)** is a CVSS 9.2 18-year-old pre-auth RCE class with ASLR-dependent code-execution caveat. Broad A&D infrastructure exposure (NGINX is the dominant web-tier / reverse-proxy / ingress-controller deployment across the prime tier). Patch availability is the protective-action recommendation.
- **CVE-2026-46300 Fragnesia (AM-003)** is a wide-deployment Linux LPE PoC; patches rolling; VPN/IPsec mitigation caveats. Combined with Copy Fail (CVE-2026-31431) deadline, this is the strongest "do-this-today" defensive-action signal of the morning.
- **CVE-2026-44338 PraisonAI (AM-004)** is the AI-supply-chain mass-scanning-velocity context — within 4h of disclosure, scanner probing the exact endpoint. The "velocity" finding is the headline (3h44m discovery-to-probe), more so than the CVSS 7.3 itself. AI tooling adoption velocity in A&D AI experimentation programs is the indirect relevance.
- **FrostyNeighbor / UNC1151 / Ghostwriter (AM-001)** is the strongest BRIEF-UPDATE-candidate signal — A-grade vendor + named-byline analyst Damien Schaeffer + first-party telemetry + novel TTP (JavaScript PicassoLoader variant + server-side validation + Ukrtelecom-impersonation) + multi-year campaign with March-2026-onward escalation. Cross-references finding-2026-05-08-0009 (Polish ABW water-utility ICS attribution naming APT28 + APT29 + UNC1151). Holds at BRIEF-UPDATE not FLASH because UNC1151 / Ghostwriter is non-roster (FLASH Trigger 2 fails on tracked-actor predicate). **Possible /new-actor candidacy** — UNC1151 has multi-A-grade-source coverage spanning Mandiant + ABW + ESET, but no Archimedes roster slot. Operator decision required.
- **NVD `lastModStartDate` deferred to next FLASH** — sweep is current; the 12:00 FLASH should re-window from 11:30 EDT forward.
- **NGINX "Rift" vs F5 quarterly batch** — these are the same root vulnerability (CVE-2026-42945). The Hacker News and SecurityWeek frame it differently (THN as standalone NGINX, SecurityWeek bundling it as F5's top critical in a 50+ CVE quarterly). Single CVE / two reporting angles; the morning brief should consolidate.

## Decision

**4 raw-signal files written. 0 FLASH triggers fired. 0 anti-noise violations.** All four are BRIEF-UPDATE candidates for the 2026-05-14 08:00 morning brief, grader-queued. Per Mode 1 procedure, the grader subagent will cluster + apply credibility checklist + promote eligible clusters to findings during the morning brief phase.

Audit-trail tombstone for the 07:30 pre-brief sweep — orchestrator passes the four AM-001/002/003/004 files plus this sentinel to the grader.

## Notes

- Mandiant feedburner failure_count incremented 18→19 this sweep (twenty-first consecutive failure pattern; held healthy pending operator alt-endpoint decision).
- The Hacker News surfaced both NGINX Rift and Fragnesia as their May 14 headline content; THN is acting as cross-corroboration layer for two of the four AM raw-signals (AM-002 + AM-003).
- The 06:00 FLASH already covered ESET FrostyNeighbor + PraisonAI + Fragnesia + VMware Fusion as BRIEF-UPDATE candidates; this 07:30 pre-brief sweep extends with the NGINX "Rift" coverage that emerged 07:00-11:15 EDT and drops VMware Fusion (routine Pwn2Own, no actor / no exploitation).
- Zero items match the aerospace-defense.yaml watchlist directly this sweep. AM-002 NGINX Rift has indirect A&D relevance (widely deployed in prime web tier); AM-003 Fragnesia has indirect A&D relevance (Linux kernel is broadly deployed). AM-001 FrostyNeighbor has zero A&D-prime relevance (Eastern European gov / industrial sectors named, no Western A&D primes). AM-004 PraisonAI has indirect A&D relevance (AI-supply-chain velocity context).

---

## Extraction notes

- Collection mode: pre_brief_collection (Mode 1)
- 14h window since prior afternoon brief checkpoint; bridges yesterday's 18:00 FLASH and this morning's 06:00 FLASH
- ioc-extraction skill invoked on AM-001 (FrostyNeighbor IOC set), AM-002 (no IOC layer beyond CVE), AM-003 (no IOC layer beyond CVE), AM-004 (no IOC layer beyond CVE). All IOC-bearing extraction lives in per-item raw-signal files; this sentinel does NOT carry redundant IOC content.
- Sources queried successfully: 16 RSS / WebFetch / Splunk
- Sources skipped stale: 0 directly skipped this sweep (the cohort previously stale — ars-security feed-endpoint-retired, censys / urlscan / hibp no-MCP, threatfox / malwarebazaar no-MCP-for-auth, x-cisagov nitter-bridge-stale, x-gossithedog nitter-delisted, iran-monitor WAF — was not re-tested per FLASH-fast inheritance from the 06:00 FLASH; no operator decision on those workarounds has surfaced since).
- Items fetched in window: ~21 across the productive feeds
- Items matching watchlist / roster / vuln-index filter: 0 direct A&D-watchlist hits this sweep (4 BRIEF-UPDATE candidates raised on indirect-relevance grounds + 1 non-roster-cluster signal)
- Items raw-signaled (this sentinel excepted): 4 (AM-001 / AM-002 / AM-003 / AM-004)
- Items discarded per Mode 1 procedure: 11
- Items anti-noise-locked: 3 topics (FamousSparrow / Salt Typhoon, MuddyWater / Seedworm / ChromElevator, KongTuke / ModeloRAT + YellowKey / GreenPlasma)
