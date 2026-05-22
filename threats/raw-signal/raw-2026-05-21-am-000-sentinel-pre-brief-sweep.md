---
raw_id: raw-2026-05-21-am-000-sentinel
collected_at: 2026-05-21T07:32:00-04:00
run_id: pre-brief-20260521-073000
collection_mode: pre_brief_collection
sentinel: true
test: false
source:
  source_yaml_id: archimedes-internal
  source_name: "Archimedes collector sentinel — 2026-05-21 morning pre-brief sweep"
  source_url: null
  published_at: 2026-05-21T07:32:00-04:00
sweep_window:
  start: 2026-05-20T17:30:00-04:00
  end: 2026-05-21T07:30:00-04:00
sources_queried:
  - bleepingcomputer       # RSS 200, 4 items in 14h window: Flipper One Linux project (off-filter), Microsoft Defender zero-day patch coverage (DEDUP via KEV-7 batch lock through 2026-05-21T16:00 — but raw-signaled separately as procedural-facts upgrade w/ CVE↔name assignment), GitHub TanStack-Nx breach linkage (DEDUP via TeamPCP/Nx Console lock through 2026-05-21T06:08 EXPIRED ~80m before sweep — captured as fresh raw-signal w/ GitHub formal confirmation + 18-min extension window detail), Ukraine infostealer 18yo arrest (off-filter, no A&D/roster/vuln hit)
  - thehackernews          # feedburner 200, 4 items in 14h window: "When Identity is Attack Path" (vendor analytical/no CVE-actor-IOC, DISCARDED), CVE-2026-46333 9yo Linux kernel (CVSS 5.5 below Trigger 1 floor 9.0 and Trigger 6 floor 8.0, no A&D, DISCARDED), GitHub Nx Console breach formal confirmation (DEDUP w/ TeamPCP lock expired pre-sweep — captured as raw-signal AM-002), Drupal CVE-2026-9082 highly critical PostgreSQL RCE (advisory release follow-up to 2026-05-18 PSA — captured as AM-004 procedural-facts upgrade)
  - securityweek           # RSS 200, 6 items in 14h window: Apple App Store rejections (corporate stats, DISCARDED), Drupal CVE-2026-9082 patches (DEDUP w/ Hacker News — covered in AM-004), Socket $60M funding (business news, DISCARDED), Microsoft Patches Exploited UnDefend/RedSun (CRITICAL ASSIGNMENT — CVE-2026-41091=UnDefend, CVE-2026-45498=RedSun; matches ZD-003 + ZD-002 tracked-vuln entries; raw-signaled as AM-001 procedural-facts upgrade w/ CVSS scores 7.8/4.0 + name-to-CVE binding), Chrome AI vuln discovery (research piece no CVEs, DISCARDED), Supply Chain Security Crisis editorial (Black Kite, prior DISCARD at 06:00 sentinel, DISCARDED)
  - therecord              # feed 200, 1 item in 14h window: Xi-Putin satellite/cyber/AI joint statement (strategic geopolitics, no specific actor/CVE/IOC but A&D-strategic-context-relevant — captured as AM-005 sector-strategic context)
  - bleepingcomputer-microsoft-defender-direct  # WebFetch on /microsoft-warns-of-new-defender-zero-days-exploited-in-attacks/ — substance for AM-001 source-layer enrichment (no CVSS scores in article, vendor patch versions 1.1.26040.8 + 4.18.26040.7, KEV federal-civilian deadline 2026-06-03 reconfirmed)
  - securityweek-undefend-redsun-direct  # WebFetch on /microsoft-patches-exploited-undefend-and-redsun-defender-zero-days/ — yielded CVE↔name binding + CVSS 7.8/4.0 + Fabian Bader (MSRC MVP) exploit-variant attribution
  - cisa-advisories        # all.xml fetch_feed 200 (30 items in feed), 0 in 14h window since 2026-05-20T17:30 EDT
  - cisa-kev               # WebFetch known_exploited_vulnerabilities.json — catalog dateReleased 2026-05-20T17:38:28Z, 0 entries dated 2026-05-21; most recent KEV adds remain 2026-05-20 batch of 7 (CVE-2026-41091/45498 Defender pair + 5 historical) — DEDUP'd via 2026-05-20-afternoon brief KEV-7 batch lock through 2026-05-21T16:00
  - nvd                    # REST API lastModStartDate=2026-05-20T22:00Z lastModEndDate=2026-05-21T11:30Z cvssV3Severity=CRITICAL → 6 results: CVE-2023-4833 (Besttem ERP 9.8, 2023-vintage metadata-refresh, DISCARDED); CVE-2025-33255 (NVIDIA TRT-LLM MPI server unsafe deserialization NIST 9.8, raw-signaled AM-003 w/ CNA-vendor downgrade context); CVE-2026-24142 (NVIDIA TRT-LLM unsafe-serialized-handle NIST 9.8 / NVIDIA-CNA 6.3, raw-signaled AM-003 same cluster); CVE-2026-33278 (NLnet Labs Unbound DNSSEC validator pointer-overwrite RCE-capable 9.8, raw-signaled AM-006); CVE-2026-42960 (NLnet Labs Unbound DNS cache poisoning CVSS 10.0, raw-signaled AM-006 cluster); CVE-2026-6279 (Avada Fusion Builder unauth RCE 9.8, consumer/SMB WordPress, no A&D relevance, no active exploitation, DISCARDED — also already DISCARDED at 06:00 sentinel)
  - mstic                  # Microsoft Security Blog feed 200, last_modified 2026-05-20T23:01 GMT pre-window (~80h aged), 0 in-window items
  - unit42                 # feedburner 200, last_modified 2026-05-20T21:08 GMT pre-window, 0 in-window items
  - mandiant               # feedburner persistent 404 (~17-18 consecutive sweeps); cloud.google.com/blog/topics/threat-intelligence/rss/ alt malformed body (same as prior sweeps); not separately WebFetched on index page this sweep — pattern entrenched, operator alt-endpoint decision still pending
  - crowdstrike            # feed reachable but persistent dateless-marketing pattern (~17+ consecutive sweeps); 0 in-window threat-intel items
  - cisco-talos            # feed reachable (15 items total, etag unchanged), 0 in-window items
  - sentinelone            # SentinelLabs feed 200, last_modified 2026-05-21T07:43 GMT inside-window from feed-server activity, 0 published items in window
  - proofpoint             # /rss.xml 200, last_modified 2026-05-21T11:30 GMT inside-window from feed-server activity, 0 items in window
  - welivesecurity         # ESET feed 200, 0 items in window
  - rapid7                 # rapid7.com/blog/rss/ 200, 0 items in window
  - krebs                  # feed 200, 0 items in window
  - sans-isc               # RSS 200, 1 item in window: ISC StormCast for Thursday May 21 (podcast detail, no body content, DISCARDED)
  - theregister-security   # atom 200, 3 items in window: Cisco Secure Workload CVE-2026-20223 perfect-10 (DEDUP w/ 2026-05-20 afternoon finding-2026-05-20-0006), Microsoft RAMPART/Clarity AI safety tools (defensive-tool feature, DISCARDED), zombie-account PWNED editorial (PoC essay, DISCARDED)
  - fortinet-fortiguard    # /rss/ir.xml 200, 0 in-window IR advisories (last update timestamp ~30s before fetch; pure timing — feed has not added entries since pre-window)
  - dragos                 # /blog/feed/ 404 (continuing failure since 2026-05-13 first observed; failure_count operator-managed; not separately retried this sweep)
  - cloud-google-mandiant-rss-alt  # /blog/topics/threat-intelligence/rss/ parse-error syntax (continuing same malformed pattern)
  - msrc-defender-update-guide  # NOT directly WebFetched this sweep — prior pattern is client-side-rendered SPA shell unsuitable for substance extraction; SecurityWeek + BleepingComputer + Hacker News relays carry the substance
  - splunk-first-party     # archimedes + defenseclaw_local indexes -14h since 2026-05-20T17:30, 0 non-self events (52nd consecutive dormant non-self sweep across the pre-brief + flash sweep cadence; only self-telemetry events from scheduler / flash-sweep / pre-brief-morning start/complete cycles)
match_reason:
  watchlist: []
  actors:
    - TeamPCP                  # GitHub formal Nx Console confirmation (AM-002); attribution layer unchanged from prior FLASH lock — still single-source-veto on Breached self-claim
  vulnerabilities:
    - CVE-2026-41091           # UnDefend; binds to ZD-003 in _index.yaml (was tracked unnamed as "DoS/Defender update block" — name now confirmed)
    - CVE-2026-45498           # RedSun; binds to ZD-002 in _index.yaml (was tracked unnamed as "LPE" — name now confirmed but description appears inverted vs ZD-002 LPE classification; SecurityWeek says CVE-2026-45498 RedSun = DoS, not LPE)
    - CVE-2026-9082            # Drupal SA-CORE-2026-004; advisory now released (was PSA-only at 2026-05-20-pm-004)
    - CVE-2025-33255           # NVIDIA TRT-LLM MPI server unsafe deserialization
    - CVE-2026-24142           # NVIDIA TRT-LLM unsafe-serialized-handle
    - CVE-2026-42960           # NLnet Labs Unbound DNS cache poisoning CVSS 10.0
    - CVE-2026-33278           # NLnet Labs Unbound DNSSEC validator pointer-overwrite CVSS 9.8 RCE-capable
  keywords:
    - microsoft_defender
    - undefend
    - redsun
    - cve_name_to_cve_id_binding
    - github_corp
    - nx_console
    - nrwl_angular_console
    - vs_code_extension_compromise
    - tanstack_npm_supply_chain
    - drupal_postgresql_sql_injection
    - nvidia_trt_llm
    - tensorrt_llm
    - nlnet_unbound
    - dns_cache_poisoning
    - dnssec_validator
    - xi_putin_satellite_cyber_cooperation
    - glonass_beidou_interoperability
    - russia_china_ai_governance
triage_tags:
  - pre_brief_sentinel
  - sweep_complete
  - 14h_window
  - splunk_first_party_zero_hits_52nd_consecutive_dormant_sweep
  - mandiant_feedburner_persistent_404_pattern_unchanged
  - cve_to_codename_binding_event_zd_002_zd_003
  - kev_7_batch_anti_noise_lock_active_through_2026_05_21_t16
  - teampcp_nx_console_anti_noise_lock_expired_2026_05_21_t06_08_procedural_facts_upgrade_capture_permitted
  - nvidia_cve_cna_vendor_cvss_disagreement_observed
  - nlnet_unbound_cvss_10_cache_poisoning_no_active_exploitation
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-08-19T07:32:00-04:00
---

# Pre-brief collection sentinel — 2026-05-21 07:30 EDT cycle

Per INTEL-OPERATIONS.md Mode 1 procedure, the 07:30 EDT scheduled
pre-brief sweep ran across the canonical source set for the 14h window
2026-05-20T17:30 → 2026-05-21T07:30 EDT. Six raw-signal files written
(AM-001 through AM-006) covering items in window that match the
A&D watchlist / actor roster / tracked-vulnerability filter.

See frontmatter `sources_queried` for the full source-by-source
disposition trail (200/404/parse-error, items in window, items raw-
signaled, items discarded with rationale).

## Anti-noise lock posture at sweep time

Two anti-noise locks were active heading into this sweep window:

1. **KEV-7 batch lock** (2026-05-20-afternoon brief) — expires
   2026-05-21T16:00:00-04:00. Covers CVE-2026-41091, CVE-2026-45498,
   CVE-2008-4250, CVE-2009-1537, CVE-2009-3459, CVE-2010-0249,
   CVE-2010-0806 (federal-civilian patch deadline 2026-06-03).
   AM-001 captures the Microsoft Defender pair as a **procedural-
   facts upgrade** inside this lock — the SecurityWeek article
   (Ionut Arghire 09:52 GMT) introduces the **CVE-to-codename
   binding**: CVE-2026-41091 = UnDefend, CVE-2026-45498 = RedSun.
   These codenames match ZD-002 (RedSun, LPE) and ZD-003 (UnDefend,
   DoS/Defender update block) in `threats/vulnerabilities/_index.yaml`
   — names previously tracked as unnamed zero-days for ~2 months.
   The grader should evaluate whether the CVE↔codename binding rises
   to FLASH-tier on its own (Trigger 2-ish for vuln-tracking, not
   actor attribution) OR whether it folds into the existing KEV-7
   anti-noise lock as a procedural-facts UPDATE block.

2. **TeamPCP / GitHub-corp / Nx Console chain lock**
   (flash-2026-05-20-0608) — expired 2026-05-21T06:08 EDT, **~80m
   before this sweep**. AM-002 captures GitHub's formal confirmation
   that the nrwl.angular-console VS Code extension was the initial-
   access vector for the 3,800-internal-repo breach, plus the 18-
   minute publish-window detail (12:30–12:48 UTC on 2026-05-18).
   The 06:00 FLASH sentinel marked this as DEDUP inside the lock by
   3 minutes; the lock has now expired and the procedural-facts
   upgrade is captured as fresh raw-signal for the grader to
   evaluate either as a new finding OR as a substantive UPDATE on
   the existing finding-2026-05-20-FLASH-0001 / sibling
   finding-2026-05-19-0002.

## Items raw-signaled this sweep

| ID | Topic | Source(s) | Lock status | Trigger flag |
|---|---|---|---|---|
| AM-001 | Microsoft Defender CVE↔name binding (UnDefend=41091, RedSun=45498) + CVSS scores 7.8/4.0 | SecurityWeek + BleepingComputer + Hacker News | Inside KEV-7 lock; procedural-facts upgrade | Trigger 1 evaluated (active exploitation re-confirmed, both CVEs on KEV w/ A-grade CISA attestation) → DEDUP per anti-noise rule 1; grader adjudication on whether codename-to-CVE binding warrants separate FLASH-tier handling |
| AM-002 | GitHub formal confirmation Nx Console (nrwl.angular-console) breach vector + 18-min extension publish window | BleepingComputer + Hacker News | TeamPCP lock expired 80m pre-sweep | Trigger 2 evaluated (attribution layer unchanged — TeamPCP single-source-veto persists; procedural-facts layer upgrade w/ GitHub-named extension identifier); grader adjudication |
| AM-003 | NVIDIA TRT-LLM CVE-2025-33255 + CVE-2026-24142 dual deserialization criticals (NIST 9.8 / NVIDIA-CNA 6.3 disagreement) | NVD via REST API; NVIDIA advisory a_id=5805 | No lock | Trigger 1 fails (no active exploitation attestation in either record), Trigger 6 fails (patches in TensorRT-LLM 1.2); grader queue |
| AM-004 | Drupal CVE-2026-9082 SA-CORE-2026-004 PostgreSQL SQLi RCE (CVSS 6.5) | Drupal SA + Hacker News + SecurityWeek | No lock; UPDATE on 2026-05-20-pm-004 PSA capture | Trigger 1 fails (CVSS 6.5 below floor 9.0, no active exploitation); grader queue |
| AM-005 | Xi-Putin May 20 Beijing joint statement on satellite (GLONASS+BeiDou interop), cyber-threat coordination, AI cooperation | The Record (Recorded Future News) | No lock | Strategic-context; no specific actor/CVE/IOC; grader queue for sector-strategic relevance |
| AM-006 | NLnet Labs Unbound CVE-2026-42960 (CVSS 10.0 DNS cache poisoning) + CVE-2026-33278 (CVSS 9.8 DNSSEC validator pointer-overwrite RCE) | NVD via REST API; NLnet vendor advisories | No lock | Trigger 1 fails (no active exploitation attestation per vendor; NIST published 2026-05-20 / NVD lastModified 2026-05-20 — patches in 1.25.1); Trigger 6 fails (patches available); grader queue — widely-deployed DNS resolver class |

## Splunk first-party silence

Splunk query against `archimedes` + `defenseclaw_local` -14h since
2026-05-20T17:30 returned 0 non-self events (only scheduler /
flash-sweep / pre-brief-morning start+complete telemetry from
sourcetype=archimedes:operation and archimedes:scheduler and
archimedes:flash). 52nd consecutive dormant non-self sweep across
the pre-brief + flash sweep cadence. Per Hard Rule 8 framing:
silence is neither confirming nor disconfirming.

## Items DISCARDED per Mode 1 procedure (not raw-signaled)

Off-filter items — no watchlist / roster / vuln-index hit:

- **BleepingComputer Flipper One Linux platform** (Bill Toulas
  2026-05-21T11:00 GMT) — hardware product feature, not threat-intel.
- **Hacker News "When Identity is Attack Path"** (2026-05-21T10:30
  GMT) — vendor analytical / no specific CVE-actor-IOC.
- **Hacker News CVE-2026-46333 9yo Linux kernel** (2026-05-21T07:35
  GMT) — CVSS 5.5 below Trigger 1 floor 9.0 and Trigger 6 floor 8.0;
  no A&D relevance; already DISCARDED at 06:00 sentinel.
- **SecurityWeek Apple App Store rejections** (Ionut Arghire 2026-05-
  21T11:17 GMT) — corporate transparency stats.
- **SecurityWeek Socket $60M funding** (Ionut Arghire 2026-05-21T10:32
  GMT) — business news.
- **SecurityWeek Chrome AI vuln discovery surge** (Eduard Kovacs
  2026-05-21T09:37 GMT) — research feature / no specific CVEs;
  already DISCARDED at 06:00 sentinel.
- **SecurityWeek Supply Chain Security Crisis** (Kevin Townsend /
  Black Kite 2026-05-21T08:14 GMT) — editorial / no specific
  exploitation / IOC / actor; already DISCARDED at 06:00 sentinel.
- **BleepingComputer Ukraine 18yo infostealer arrest** (Bill Toulas
  2026-05-20T21:36 GMT) — law-enforcement action, no actor in
  roster, no A&D nexus, no IOC tied to tracking.
- **The Register Cisco Secure Workload CVE-2026-20223** (2026-05-
  21T11:27 GMT) — DEDUP w/ 2026-05-20 afternoon finding-2026-05-
  20-0006 / brief 2026-05-20-afternoon; anti-noise lock effectively
  through next afternoon cycle.
- **The Register Microsoft RAMPART/Clarity AI safety tools** (2026-
  05-21T10:30 GMT) — defensive-tool launch coverage, not threat-
  intel.
- **The Register "Zombie account let hackers control water" PWNED**
  (2026-05-21T07:00 GMT) — editorial / case-study column;
  pre-window in narrow sense but published in window; no specific
  CVE/actor/IOC of immediate Archimedes-priority relevance.
- **NVD CVE-2023-4833 Besttem Network Marketing** — 2023-vintage
  metadata refresh; already DISCARDED at 06:00 sentinel.
- **NVD CVE-2026-6279 Avada Fusion Builder** — patched, consumer/
  SMB WordPress, no A&D; already DISCARDED at 06:00 sentinel.
- **SANS ISC StormCast podcast** — title/link only, no body content.

## Source health observations (this sweep)

No source-health.yaml runtime field changes required per the
operator-set policy (runtime updates are typically applied by the
out-of-band update script). All queried sources behaved consistent
with their entrenched patterns documented in `source-health.yaml`:

- **mandiant feedburner**: 404 pattern continues (~18 consecutive
  sweeps); operator alt-endpoint decision still pending.
- **crowdstrike**: dateless marketing-content pattern continues;
  ~18 consecutive sweeps without dated threat-intel posts.
- **cisco-talos / sentinelone / proofpoint / welivesecurity /
  rapid7 / krebs / mstic / unit42**: all reachable, 0 in-window
  items.
- **bleepingcomputer / thehackernews / securityweek / therecord /
  sans-isc**: all reachable, items in window — see disposition
  trail above.
- **nvd / cisa-kev / cisa-advisories**: all reachable. NVD critical-
  window query productive (6 results, 4 raw-signaled across AM-003
  and AM-006, 2 discarded).
- **dragos**: /blog/feed/ persistent 404 (no operator-discovery yet);
  not separately retried this sweep.
- **splunk-first-party**: reachable, 0 non-self events in -14h
  window.
- **fortinet-fortiguard**: /rss/ir.xml reachable, 0 in-window IR
  advisories.
- **theregister**: reachable, 3 items in window all DISCARDED or
  DEDUP'd.

## Handoff items for 08:00 morning brief composer

The grader will adjudicate promotion; the briefer should consider
these as the likely brief composition surface:

1. **Microsoft Defender CVE↔codename binding (AM-001)** — UPDATE on
   finding-2026-05-20-0005 (CISA KEV +7 batch); codenames UnDefend
   and RedSun now publicly bound to CVE-2026-41091 and CVE-2026-45498
   respectively per SecurityWeek (sourcing MSRC + CISA + Fabian
   Bader). Material because ZD-002 (RedSun) and ZD-003 (UnDefend)
   are TRACKED ZERO-DAYS in `_index.yaml` from 2026-03 — the
   tracked-vuln entries can now have CVEs attached, AND the SecurityWeek
   CVSS scores (7.8 for the LPE, 4.0 for the DoS) can be populated.
   Note: SecurityWeek's pairing assigns CVE-2026-41091=UnDefend=LPE
   and CVE-2026-45498=RedSun=DoS, which is INVERTED from
   `_index.yaml` descriptions (ZD-002 RedSun=LPE, ZD-003 UnDefend=
   DoS/Defender update block). Grader/vuln-tracker should reconcile.

2. **GitHub formal Nx Console attribution (AM-002)** — UPDATE on
   finding-2026-05-20-FLASH-0001 (TeamPCP / 3,800-repo breach).
   Procedural-facts upgrade: GitHub formally names
   nrwl.angular-console as the breach extension (vs. yesterday's
   "directionally consistent with our investigation" framing); plus
   18-minute publish window (12:30–12:48 UTC on 2026-05-18). TeamPCP
   attribution layer UNCHANGED (still Breached self-claim single-
   source-veto). Sibling cross-ref: finding-2026-05-19-0002
   (distinct-mechanism Nx Console cluster).

3. **NLnet Unbound CVSS 10.0 + 9.8 cluster (AM-006)** — NEW vuln-
   tracker handoff. CVE-2026-42960 DNS cache poisoning CVSS 10.0
   on widely-deployed open-source DNS resolver (used in production
   recursive resolvers at scale globally including likely A&D
   primes); CVE-2026-33278 DNSSEC validator pointer-overwrite RCE
   CVSS 9.8 same product. Patches available in Unbound 1.25.1.
   No active exploitation attestation. FLASH triggers all fail
   (no ITW; patches available) — vuln-tracker queue strong
   candidate.

4. **NVIDIA TRT-LLM CVE pair (AM-003)** — NEW vuln-tracker handoff
   if AI-infrastructure exposure tracking is in scope. CVSS
   disagreement notable: NIST 9.8 (network unauth) vs NVIDIA-CNA
   6.3 (local privilege-required) on CVE-2026-24142; CVE-2025-33255
   MPI server unsafe deserialization NIST 9.8 only. TensorRT-LLM is
   the LLM-inference library widely used in enterprise AI deployments
   including potential A&D R&D contexts. Patches in TRT-LLM 1.2.

5. **Drupal CVE-2026-9082 advisory release (AM-004)** — UPDATE on
   2026-05-20-pm-004 PSA capture. SA-CORE-2026-004 released CVSS 6.5
   PostgreSQL-specific SQLi → RCE/EoP/InfoDisclosure. Patches in
   Drupal 11.3.10 / 11.2.12 / 11.1.10 / 10.6.9 / 10.5.10 / 10.4.10.
   Drupal 7 unaffected. A&D web-presence relevance modest;
   PostgreSQL-only narrowing reduces blast radius.

6. **Xi-Putin satellite/cyber/AI joint statement (AM-005)** —
   strategic-context standing-section material. May 20 Beijing
   pledge to deepen GLONASS+BeiDou interoperability, coordinate on
   "information security and cyber threat response," establish
   "global organization dedicated to AI cooperation." No specific
   A&D-prime named; no specific operational mechanism announced;
   no specific CVE / IOC / threat-actor cited. Briefer judgment
   on Sector Focus inclusion.

## Anti-noise distinction from recent FLASHes / briefs / sentinels

- **flash-sweep-20260521-060000 (06:00 sentinel, 0 triggers)** —
  same KEV-7 + TeamPCP lock context; lock-collision dedup applied
  there now becomes lock-expired procedural-facts-capture here
  (TeamPCP lock expired 06:08, 80m pre-sweep). KEV-7 lock still
  active through 16:00.
- **flash-2026-05-20-1800 (ad-hoc sweep, 0 triggers + 4 handoff
  items)** — distinct window; subsequent 12h period now covered
  by midnight + dawn + pre-brief sentinels chain.
- **2026-05-20-afternoon (KEV-7 batch + Cisco Secure Workload CVE-
  2026-20223 CVSS 10.0)** — KEV-7 lock through 2026-05-21T16:00
  governs Microsoft Defender pair; UnDefend/RedSun codename binding
  is procedural-facts UPDATE inside the lock per anti-noise rule 1.

## Extraction notes

- Language: en
- Article type: sentinel
- Raw IOC extraction invoked: no (sentinel — no payload content;
  per-item raw-signals AM-001 through AM-006 carry their own
  extraction notes)
- Run mode: pre_brief_collection (Mode 1)
- Output mode: sentinel log + 6 raw-signal files
- Anti-noise lock collisions: 1 (KEV-7 batch through 2026-05-21T16:00
  — procedural-facts upgrades captured under existing lock)
- TeamPCP/Nx Console lock expired 80m pre-sweep — captured as
  fresh raw-signal AM-002 per Mode 1 procedure (lock-expired ⇒
  new substance permitted to land as fresh raw-signal)
