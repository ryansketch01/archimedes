---
raw_id: raw-2026-05-14-0600-flash-sweep-clean
collected_at: 2026-05-14T06:08:00-04:00
run_id: flash-sweep-20260514-060000
collection_mode: flash_sweep
source:
  source_yaml_id: meta-sweep-tombstone
  source_name: "FLASH sweep tombstone (no candidates)"
  source_url: null
  published_at: 2026-05-14T06:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_sweep_clean, audit_trail, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-12T06:08:00-04:00
test: false

sweep_summary:
  sweep_window_start: 2026-05-13T18:00:00-04:00
  sweep_window_end: 2026-05-14T06:00:00-04:00
  sweep_window_hours: 12
  sources_queried: 14
  sources_skipped_stale: 0
  items_fetched_in_window: 14
  items_matching_watchlists: 0
  items_evaluated_against_flash_triggers: 7
  flash_candidates: 0
  source_health_changes: []
  brief_update_candidates_for_morning: 4
---

# FLASH sweep 2026-05-14 06:00 EDT — clean (0 triggers)

**0 triggers fired. 0 candidates queued. Window: 2026-05-13 18:00 EDT → 2026-05-14 06:00 EDT (12 hours; bridges yesterday's 18:00 FLASH on Symantec/MuddyWater/ChromElevator through this morning's 06:00 sweep, includes the overnight quiet-hours window 21:00–09:00).**

Quiet hours: 06:00 EDT is INSIDE the quiet window (21:00–09:00). Had any trigger fired, the FLASH would have queued to `infrastructure/flash-queue.yaml` for the 09:00 catchup sweep — no critical override conditions met (no CVSS 10.0 + active exploitation + tracked actor + A&D-watchlist named target simultaneously in any in-window item).

## Sweep window

2026-05-13T18:00:00-04:00 → 2026-05-14T06:00:00-04:00 (12h)

## Sources queried (14)

A-grade primary research / CISA / NVD / first-party Splunk (all in-window):

- **CISA Advisories all.xml RSS** — 0 items in window after since-filter. Last in-window item was the 2026-05-12 ICS-CERT batch (already absorbed).
- **CISA KEV catalog** (JSON, catalogVersion 2026.05.13, dateReleased 2026-05-13T17:58:37Z) — no new entries since 2026-05-08 (CVE-2026-42208 BerriAI LiteLLM remains the most recent addition). Ranking unchanged from yesterday's sweeps.
- **NVD** — 4 in-window CVSS 9.8 Critical CVE modifications identified (CVE-2026-8181 Burst Statistics WordPress, CVE-2026-6271 Career Section WordPress, CVE-2026-6510 + CVE-2026-6512 InfusedWoo Pro WordPress). All WordPress plugin auth-bypass / arbitrary-file-upload / privilege-escalation; **none carry active-exploitation claim**.
- **Mandiant / Google Threat Intel index page** (cloud.google.com/blog/topics/threat-intelligence) — top-8 visible titles included "North Korea-Nexus Threat Actor Compromises Widely Used Axios NPM Package in Supply Chain Attack" which on direct article fetch is **dated 2026-03-31** (6+ weeks old; UNC1069 attribution from March 31, 2026 — already-existing reporting NOT in-window). Mandiant feedburner remains 404 (twentieth consecutive failure pattern). No fresh post-2026-05-13-18:00 publication identifiable from the visible index.
- **CrowdStrike blog index** — one in-window item: "Falcon AIDR Detects Threats at the Prompt Layer in Kubernetes AI Applications" (2026-05-13 product piece, no threat-actor content, no fresh attribution, no fresh CVE).
- **Microsoft MSTIC feed** — feed endpoint 404'd this sweep (microsoft.com/en-us/security/blog/threat-intelligence/feed/); held healthy pending next-cycle retry per same pattern observed in prior sweeps. No alt-endpoint pivot this FLASH-fast scope.
- **Palo Alto Unit 42 feedburner** — reachable, 0 items in 12h window. Most recent visible item is the 2026-05-11 AD CS Escalation analysis (pre-window).
- **Symantec security.com Threat Intelligence index** — most recent visible items are 2026-05-12 Seedworm electronics-maker post (pre-window, parent of yesterday's MuddyWater FLASH) and 2026-03-05 Seedworm US bank/airport post (pre-window). No fresh post-yesterday-18:00 Symantec publication identifiable.
- **Bitdefender Labs / Business Insights** — most recent visible item is the 2026-05-13 FamousSparrow Azerbaijani O&G post (already absorbed in yesterday's 14:30 FLASH; anti-noise lockout to 2026-05-14 14:30 EDT). No fresh post-yesterday-18:00 publication.
- **ESET WeLiveSecurity** — 1 in-window item: "FrostyNeighbor: Fresh mischief and digital shenanigans" (Damien Schaeffer, 2026-05-14). ESET attributes to FrostyNeighbor cluster (alias set: Ghostwriter, UNC1151, UAC-0057, TA445, PUSHCHA, Storm-0257) — **Belarus-aligned APT NOT in `_roster.yaml`**. See detailed trigger evaluation below.
- **Sophos News blog** — visible content includes Patch Tuesday recap + AI-deployment defensive guidance + Identity Security 2026 survey + GPT-5.5-Cyber post. No tracked-actor attribution, no fresh CVE, no in-window APT analysis.
- **Dragos blog** — most recent visible items 2026-05-11 (OT AI) and 2026-05-07 (frontlines lessons). No post-yesterday-18:00 publication.
- **BleepingComputer RSS** — 3 in-window items: West Pharmaceutical encryption update (pharma single-victim, no actor named, anti-noise — covered in yesterday's afternoon brief), Fragnesia CVE-2026-46300 Linux kernel LPE (PoC only, no ITW exploitation, no actor, see trigger evaluation), Dream Market admin US indictment (law enforcement, not threat intel).
- **SecurityWeek RSS** — 3 in-window items: PraisonAI CVE-2026-44338 mass-scanner-probing within 4h of disclosure (see trigger evaluation), VMware Fusion high-severity patched at Pwn2Own Berlin (patched, no actor, no exploitation claim), YellowKey/GreenPlasma re-coverage (pure relay of yesterday's BleepingComputer; anti-noise — covered in yesterday's afternoon brief).
- **The Record RSS** — 0 items in 12h window.
- **Krebs on Security RSS** — 0 items in 12h window.
- **SANS ISC RSS** — 2 in-window items: Outlook Junk-folder link-preview tip (operational hygiene blog, not threat-intel) + Stormcast 2026-05-14 podcast index entry (audio).

First-party telemetry:

- **Splunk `archimedes` + `defenseclaw_local` last-24h tracked-actor sweep** — 9 hits returned, all of which are Archimedes' own audit-trail events (`archimedes:operation` git_committed / brief_published / flash_published / grade_revision / ioc_ingestion_deferred from yesterday's 14:30 FLASH + 16:00 afternoon brief + 18:00 FLASH). Zero security-event sourcetypes; zero tracked-IOC matches. 22nd consecutive dormant sweep with the non-archimedes-internal stream — consistent with the 21-consecutive-dormant-sweeps figure logged in yesterday's afternoon brief.

## Items evaluated against FLASH triggers

### Item 1 — ESET "FrostyNeighbor: Fresh mischief and digital shenanigans" (WeLiveSecurity, 2026-05-14, Damien Schaeffer)

- ESET attribution language verbatim: "FrostyNeighbor, also known as Ghostwriter, UNC1151, UAC-0057, TA445, PUSHCHA, or Storm-0257, is a group allegedly operating from Belarus."
- ESET confidence level: not explicitly stated in formal confidence taxonomy; uses "allegedly" + "apparent" attribution hedge language; no high/moderate/low qualifier.
- Targeted sectors: governmental organizations (primary), military/defense (Ukraine emphasis), industrial / manufacturing / healthcare / pharmaceuticals / logistics in Poland and Lithuania. **A&D-sector watchlist companies NOT named.**
- Geography: Ukraine (primary), Poland, Lithuania (secondary); non-Ukrainian IP addresses receive decoy documents only.
- Campaign timeline: active since at least 2016; recent surges July 2024 + February 2025 + August 2025 + December 2025; newly-detected activity since March 2026.
- IOCs published: 5 C&C domains (`.icu` and `.buzz` TLDs) + 8 SHA-1 hashes + CVE-2023-38831 (WinRAR) + CVE-2024-42009 (Roundcube XSS).
- Novel TTP elements: JavaScript-based PicassoLoader variant (new); server-side victim validation before payload delivery; geographic filtering; REG-file persistence via scheduled tasks; rundll32.exe copy-masquerading.

**Trigger evaluation:**

- **Trigger 2 (new attribution for tracked actor) — FAILS.** FrostyNeighbor → Ghostwriter / UNC1151 / Belarus-aligned cluster is **NOT in `_roster.yaml`** (24 tracked actors checked; UNC1151 appears only in finding-2026-05-08-0009 as a cited-but-not-tracked actor named by Polish ABW in the water-utility ICS-breach attribution alongside APT28 + APT29). No alias overlap with any of the 24 tracked roster actors. ESET makes no link to APT28 (FrostyNeighbor is consistently treated as a distinct Belarus-aligned cluster operating in parallel to GRU-attributed activity, not as an APT28 alias).
- **Trigger 4 (tracked actor TTP change, A/B grade) — FAILS.** TTP delta is for a NON-tracked actor (Ghostwriter / UNC1151). Would qualify for Trigger 4 only if FrostyNeighbor mapped to a roster entry, which it does not.
- **Trigger 5 (active multi-victim A&D campaign) — FAILS.** No A&D-watchlist company named. Ukraine government/military + Poland/Lithuania industrial-manufacturing-healthcare-pharma-logistics is sector-shaped Eastern European targeting; aerospace + defense primes not named. Would re-evaluate if subsequent ESET / Mandiant / Microsoft / CISA cross-corroboration named a Western A&D prime victim.

**Disposition: BRIEF-UPDATE candidate for 2026-05-14 morning brief (NOT a FLASH).**

The FrostyNeighbor / Ghostwriter / UNC1151 cluster is the same Belarus-aligned grouping referenced in finding-2026-05-08-0009 (Polish ABW water-utility ICS attribution). Surfacing this as morning-brief content serves three purposes: (1) demonstrates ESET first-party visibility into the cluster's 2026 evolution beyond the ABW retrospective; (2) potentially supports a /new-actor candidacy (Ghostwriter / UNC1151 has multi-A-grade-source historical coverage but no roster slot); (3) operator-facing context for any future ABW-style critical-infrastructure relay. **Anti-noise note:** the ABW finding-0009 has a "single-source-veto on attribution-direct" caveat — adding the ESET FrostyNeighbor surface does not change that finding's grading because ESET's reporting concerns a different campaign cluster (Ukraine/Poland/Lithuania government espionage) NOT the Polish water-utility ICS-modify activity.

### Item 2 — PraisonAI CVE-2026-44338 mass-scanner probing within 4h of disclosure (SecurityWeek, 2026-05-14T09:45 EDT, Ionut Arghire)

- CVE-2026-44338 affecting PraisonAI 2.5.6-4.6.33 (patched 4.6.34); authentication bypass in legacy Flask API server (disabled by default in newer deployments).
- NVD-confirmed CVSS v3 base score **7.3 HIGH** (`AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L`) — **NOT critical, NOT >= 9.0**.
- Sysdig (application protection firm) framed observed activity as "scanner identifying itself as CVE-Detector/1.0 was probing the exact vulnerable endpoint" within 3h44m of advisory publication. Sysdig's own characterization: "associated with a scanner, not interactive exploitation."
- No threat-actor attribution. No A&D-sector framing. Patch available at disclosure (4.6.34).

**Trigger evaluation:**

- **Trigger 1 (critical CVE + active exploitation + A-grade) — FAILS on TWO predicates:** (a) CVSS 7.3 below 9.0 floor; (b) "scanner not interactive exploitation" per Sysdig's own framing falls short of active-exploitation evidence. SecurityWeek is provisional B-grade media (relay layer), not A-grade primary.
- **Trigger 6 (zero-day no patch) — FAILS.** Patch available (4.6.34) at disclosure.

**Disposition: BRIEF-UPDATE candidate for 2026-05-14 morning brief.** AI-supply-chain mass-scanning-velocity context for AI-tooling adoption posture in A&D AI experimentation programs; useful FYI but not FLASH-eligible.

### Item 3 — Fragnesia CVE-2026-46300 Linux kernel LPE PoC (BleepingComputer, 2026-05-14T07:34 EDT, Sergiu Gatlan)

- CVE-2026-46300 (Fragnasia per Bleeping; "Fragnesia" in title appears typo; ESP-in-TCP subsystem XFRM logic bug per Zellic researcher William Bowling).
- Affected: "all Linux kernels released before May 13, 2026" — wide-deployment qualifier MET.
- Exploitation status: **proof-of-concept only**, no in-the-wild exploitation claim.
- Patch availability: kernel patch on netdev mailing list dated 2026-05-13; "Linux distros are rolling out patches" without enumerated dates per distro.
- No threat-actor attribution.
- Mitigation alternative documented: `rmmod esp4 esp6 rxrpc` (caveat: breaks AFS distributed network filesystems + IPsec VPNs).

**Trigger evaluation:**

- **Trigger 1 (critical CVE + active exploitation + A-grade) — FAILS** on no-active-exploitation predicate (PoC only) and A-grade-primary predicate (BleepingComputer is B-grade media, Zellic researcher byline; SecurityWeek not relaying yet within window).
- **Trigger 6 (zero-day no patch) — FAILS.** Patches rolling at disclosure (kernel patch on netdev mailing list 2026-05-13). CVSS not yet provided in article (article does NOT state a CVSS score; NVD entry not yet indexed at sweep time). Wide-deployment qualifier MET but exploitation predicate ("exploitation_confirmed_or_imminent") FAILS — PoC release without active exploitation claim is researcher PoC class, not imminent-exploitation class per FLASH-POLICY definition.

**Disposition: BRIEF-UPDATE candidate for 2026-05-14 morning brief.** Linux kernel LPE PoC affecting all pre-2026-05-13 kernels with VPN/IPsec mitigation caveats is meaningful patch-context for A&D defensive posture; useful for morning brief but not FLASH-eligible.

### Item 4 — VMware Fusion high-severity patched at Pwn2Own Berlin (SecurityWeek, 2026-05-14T08:42 EDT, Eduard Kovacs)

- Broadcom-issued patch for high-severity VMware Fusion vulnerability disclosed during Pwn2Own Berlin 2026 (week of 2026-05-12).
- Patches available at disclosure (Pwn2Own coordinated-disclosure pattern).
- No threat-actor attribution. No active-exploitation claim.

**Trigger evaluation:**

- **Triggers 1 / 6 — FAIL** (patched at disclosure; no active exploitation; high-severity not critical).

**Disposition: BRIEF-UPDATE candidate for morning brief (routine Pwn2Own coverage).**

### Item 5 — West Pharmaceutical confirms data theft + system encryption (BleepingComputer, 2026-05-13T22:23 EDT, Bill Toulas)

- Pharmaceutical company; **NOT A&D-watchlist**; single-victim.
- No threat-actor named.
- Anti-noise: West Pharmaceutical ransomware was raised in 2026-05-12 afternoon-sweep and 2026-05-13 morning-brief context; this is a follow-up confirmation of data exfiltration (the new fact this update adds is the encryption claim, not just data theft).

**Trigger evaluation:**

- **Trigger 5 (active multi-victim A&D campaign) — FAILS.** Pharma, not A&D; single-victim.
- **Trigger 2 — FAILS.** No threat actor attributed.

**Disposition: anti-noise (covered in prior brief context, no new tracked-actor surface, follow-up data-theft confirmation is not FLASH-eligible).**

### Item 6 — Dream Market admin US indictment / arrest in Germany (BleepingComputer, 2026-05-14T08:55 EDT, Sergiu Gatlan)

- Law-enforcement action against alleged Dream Market dark-web-marketplace administrator (money laundering charges).
- Historical-marketplace context (Dream Market shut down years prior).
- No threat-actor attribution to tracked roster.

**Trigger evaluation:**

- All triggers FAIL. Law-enforcement disposition news, not threat-intel.

**Disposition: not threat-intel material; outside FLASH scope.**

### Item 7 — SecurityWeek YellowKey/GreenPlasma re-coverage (2026-05-14T07:27 EDT)

- **Pure relay** of yesterday's BleepingComputer coverage. No MSRC advisory, no CVE assignment, no in-the-wild exploitation claim, no threat-actor attribution, no A&D-sector framing, no vendor patch announcement (SecurityWeek explicitly notes Microsoft email pending response).
- Anti-noise: YellowKey + GreenPlasma absorbed in 2026-05-13 afternoon brief (finding-2026-05-13-0003). Lockout active.

**Disposition: anti-noise; no trigger fires.**

## Anti-noise lockouts honored

Per orchestrator handoff and yesterday's brief audit trail, the following topics are anti-noise-locked and were NOT re-triggered this sweep:

- **FamousSparrow / Salt Typhoon / Azerbaijan O&G Exchange intrusion** — locked out until 2026-05-14 14:30 EDT (yesterday's 14:30 FLASH posted finding-2026-05-13-FLASH-0001). No new in-window material advances this topic.
- **MuddyWater / ChromElevator / SentinelOne fmapp + sentinelmemoryscanner DLL sideloading / Seedworm Q1 2026 multi-victim** — locked out until 2026-05-14 18:00 EDT (yesterday's 18:00 FLASH posted finding-2026-05-13-FLASH-1800-0001). No new in-window material advances this topic. Symantec primary blog unchanged; no second independent IR-grade corroboration emerged overnight; Industrial Cyber relay-conflation pattern (the falsely-attached "U.S. defense and aerospace software supplier with Israeli operations" victim claim) holds at NOT-propagated per Hard Rule 2.
- **KongTuke / ModeloRAT / Microsoft Teams + CVE-2023-36036 cldflt.sys / BitLocker YellowKey + GreenPlasma PoCs** — covered in 2026-05-13 16:00 afternoon brief (findings 0003 + 0004). No new in-window material advances these topics. SecurityWeek YellowKey/GreenPlasma piece is pure relay.

## CISA-KEV ranking

CISA KEV catalog version 2026.05.13 (released 2026-05-13T17:58:37Z) — no new entries since 2026-05-08 CVE-2026-42208 BerriAI LiteLLM addition. Ranking unchanged from prior 06:00 / 12:00 / 18:00 sweeps. ZD-004 PAN-OS CVE-2026-0300 remains the singular Archimedes-tracked KEV-listed active-exploitation CVE; CVE-2026-45321 Mini Shai-Hulud remains KEV-pending per _index.yaml.

## NVD critical-CVE in-window (4 modifications, all non-FLASH)

NVD lastModStartDate 2026-05-13T22:00Z → lastModEndDate 2026-05-14T10:00Z returned 4 CVSS 9.8 Critical entries — all WordPress plugin auth-bypass / arbitrary-file-upload / privilege-escalation class with **no active-exploitation claim**:

- CVE-2026-8181 — Burst Statistics (Privacy-Friendly WordPress Analytics) 3.4.0–3.4.1.1; auth bypass via `is_mainwp_authenticated()` flaw.
- CVE-2026-6271 — Career Section WordPress plugin <=1.7; arbitrary file upload via CV handler (missing file-type validation).
- CVE-2026-6510 — InfusedWoo Pro WordPress plugin; privilege escalation via missing-authorization AJAX handler.
- CVE-2026-6512 — InfusedWoo Pro WordPress plugin; authorization bypass enabling unauthenticated post/page/product/order deletion.

**Trigger 1 evaluation:** all four FAIL active-exploitation predicate. Trigger 1 not fired.

## First-party Splunk check (Trigger 3)

- Query: `index=archimedes OR index=defenseclaw_local earliest=-24h (<24 tracked actor names + aliases + current-cluster keywords>)`
- Result: 9 hits returned, all of which are Archimedes' own audit-trail events (`archimedes:operation` sourcetype) — yesterday's 14:30 FLASH brief_published / flash_published / grade_revision (Bitdefender provisional A), 16:00 afternoon brief_published / ioc_ingestion_deferred (KongTuke vuln-tracker handoff), 18:00 FLASH flash_published / brief_published / git_committed (Symantec / MuddyWater).
- Zero security-event sourcetypes; zero tracked-IOC matches.
- 22nd consecutive dormant sweep with the non-archimedes-internal stream.
- **Trigger 3 (first-party-ioc-hit) does not fire.**

Framing: silence is not disconfirming. No first-party observation to bump any external claim in either direction. Yesterday's KongTuke 13-C2-IP set, Symantec MuddyWater 4-IOC set (2 domains + 2 IPs), and Bitdefender FamousSparrow 12-IOC set returned zero matches over -30d earlier sweeps; the -24h re-check this sweep adds no new signal.

## Source-health observations

No status transitions warranted. Notable persistent patterns held healthy:

- **mandiant** — feedburner.com/Mandiant 404 (twentieth consecutive sweep failure pattern; alt cloud.google.com/blog/topics/threat-intelligence/rss returns malformed body). Held healthy pending operator alt-endpoint decision (not re-tested this sweep — FLASH-fast scope, alt-endpoint pivot tomorrow morning).
- **mstic feed** — feed endpoint returned 404 this sweep. Held healthy pending next-cycle retry per same pattern observed in prior 1-of-N sporadic-404 cycles; will re-validate on 2026-05-14 morning pre-brief collection.
- **dragos blog feed** — direct blog index reachable via WebFetch though /blog/feed/ remains the failure path noted 2026-05-09 (collector-discovery 404 on RSS path). Operator-side working dragos.com RSS path identification still pending.
- **sophos blog redirect** — news.sophos.com 301-redirected to www.sophos.com/en-us/blog this sweep; not a failure. Will update source URL on next operator pass.
- **crowdstrike** — feed reachable; one in-window product post (Falcon AIDR Kubernetes AI piece) is the highest-velocity content surfaced from this source this sweep, consistent with the 16-of-recent-N dateless-marketing-content pattern.

`source-health.yaml` not modified by this sweep.

## Brief-UPDATE candidates for 2026-05-14 morning pre-brief / 08:00 brief

Four items surfaced this sweep that do NOT meet FLASH criteria but warrant pre-brief collection pickup and morning-brief consideration:

1. **ESET FrostyNeighbor / Ghostwriter / UNC1151 — Belarus-aligned APT 2026-03 campaign** (Damien Schaeffer, 2026-05-14). Brief-UPDATE candidate + possible /new-actor candidacy (UNC1151 has multi-A-grade-source coverage spanning Mandiant, ABW, ESET but no Archimedes roster slot). Cross-references finding-2026-05-08-0009 (Polish ABW water-utility ICS attribution).
2. **PraisonAI CVE-2026-44338 mass-scanner probing within 4h of disclosure** (SecurityWeek + Sysdig, 2026-05-14). AI-supply-chain mass-scanning-velocity context.
3. **Fragnesia / Fragnasia CVE-2026-46300 Linux kernel ESP-in-TCP XFRM LPE PoC** (BleepingComputer + Zellic / William Bowling, 2026-05-14). Wide-deployment Linux LPE PoC; patches rolling; VPN/IPsec mitigation caveats.
4. **VMware Fusion high-severity Pwn2Own Berlin patch** (SecurityWeek, 2026-05-14). Routine Pwn2Own coverage.

## Decision

**0 FLASH candidates.** All evaluated items either fail trigger conditions (4 items), fall outside watchlist/roster/vuln-index scope (FrostyNeighbor cluster non-roster; West Pharmaceutical non-A&D), hit anti-noise lockouts (YellowKey/GreenPlasma SW relay; KongTuke / MuddyWater / FamousSparrow already-absorbed), or are non-threat-intel content (Dream Market law-enforcement disposition; SANS ISC operational hygiene).

Audit-trail tombstone for the 06:00 sweep — orchestrator will log `flash_sweep_clean` and exit silently per FLASH-POLICY anti-noise rules. Four brief-UPDATE candidates handed off to 2026-05-14 07:30 pre-brief collection / 08:00 morning briefer.

## Notes

- Quiet hours: 06:00 EDT is INSIDE quiet window (21:00–09:00). Had any trigger fired, the FLASH would have queued to `infrastructure/flash-queue.yaml`. No critical-override conditions met (no CVSS 10.0 + active exploitation + tracked actor + A&D-watchlist target simultaneous).
- The Mandiant UNC1069/Axios npm article visible on the cloud.google.com index page is dated **2026-03-31** (6+ weeks pre-window) — verified via direct article fetch. Index-page surfacing of older content is the publisher's editorial featuring choice, not a republication; no trigger fires.
- ESET FrostyNeighbor is the strongest BRIEF-UPDATE-candidate signal this sweep — A-grade vendor, named-byline analyst (Damien Schaeffer), first-party telemetry, novel TTP (JavaScript PicassoLoader variant + server-side validation), multi-victim multi-year campaign with March-2026-onward escalation. Held to UPDATE-not-FLASH solely because UNC1151 / Ghostwriter is non-roster.

---

## Extraction notes

- Collection mode: flash_sweep (Mode 2)
- Trigger evaluations: 6 triggers checked across 7 in-window items + Splunk 24h + NVD 12h + CISA KEV
- No raw-signal-worthy items surfaced (FLASH-fast scope; non-trigger items either anti-noise-absorbed, non-roster-cluster, sub-CVSS-floor, or filtered out per Mode 1 watchlist/roster/vuln-index rules)
- No IOC extraction invoked (no qualifying FLASH-trigger items)
- ioc-extraction skill: not invoked this sweep
- Article counts in narrative consistent with feed-level item counts; no items dropped or merged silently
