---
raw_id: raw-2026-05-18-flash-0600-000
collected_at: 2026-05-18T06:05:00-04:00
run_id: flash-sweep-20260518-060000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (scheduled, 06:00 EDT Monday)"
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
  - dormant_splunk_sweep_41
  - scheduled_0600_window
  - quiet_hours_active
  - non_promotable
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
promoted_note: "Sentinel tombstone — non-promotable per established precedent (see raw-2026-05-17-flash-*-000 chain and raw-2026-05-18-flash-0000-000 immediate predecessor). Seven in-window items evaluated and all DISCARDED for FLASH purposes: (1) SecurityWeek 'Exploitation of Critical NGINX Vulnerability Begins' — VulnCheck Canaries honeypot scanner-class observation, same evidentiary class as 2026-05-17 12:00 FLASH evaluation that capped at defensive-telemetry not A-grade-attested production exploitation; anti-noise rule 1 active on CVE-2026-42945 finding-2026-05-16-0001 carry-forward; (2) SecurityWeek 'First Shai-Hulud Worm Clones Emerge' — Ox Security single-source on 4 cloned npm packages by an UNATTRIBUTED actor explicitly distinct from TeamPCP, materializes the predicted derivative-attacks-30-days WEP from flash-2026-05-15-0600-teampcp-shai-hulud-release / VT-006 carry-forward; anti-noise rule 1 applies; (3) SecurityWeek Grafana breach 'Coinbase Cartel linked to ShinyHunters / Scattered Spider / Lapsus$' — SecurityWeek single-source-relay attribution per unnamed 'cybersecurity companies' to a non-roster cluster (Coinbase Cartel not in _roster.yaml); Hard Rule 2 prevents direct Scattered-Spider tracked-actor attribution origination from this relay; no A-grade vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC) cited; (4) SecurityWeek + BleepingComputer Pwn2Own Berlin 2026 final wrap $1.298M / 47 zero-days / DEVCORE Master of Pwn — finding-2026-05-16-0002 carry-forward unchanged, ZDI 90-day vendor-coordinated-disclosure embargo intact through ~2026-08-13; (5) BleepingComputer DirtyDecrypt Linux kernel rxgk LPE CVE-2026-31635 — V12 security team PoC published, patched in mainline 2026-04-25, no A-grade exploitation attestation, no tracked actor, no CVSS published in source, narrower distro footprint (Fedora / Arch / openSUSE Tumbleweed only); (6) The Hacker News Symantec Fast16 nuclear-weapons-simulations confirmation — relay/extension of finding-2026-05-16-0003 carry-forward, pre-Stuxnet 2005-2010 historical activity, Equation Group implicit attribution (not in _roster.yaml), no current A&D campaign; new second-corpus surface strengthens Symantec provisional-A operator ratification case (clock T+35h+ past elapsed); (7) The Hacker News MiniPlasma — second relay of BleepingComputer Lawrence Abrams 18:30 EDT 2026-05-17 originating coverage, anti-noise applies, same PoC-only-not-exploitation evaluation as 00:00 FLASH and 18:00 FLASH 33d3f9a evaluations; status-update CANDIDATE for 08:00 morning brief grader pending A-grade corroboration (MSRC / MSTIC / CISA KEV). Single DarkReading AI-essay item also discarded per anti-noise (same as 00:00 + 18:00 FLASH disposition). No FLASH-trigger fires; all 6 triggers FAIL on all 7 in-window items."
ttl_expires_at: 2026-08-16T06:05:00-04:00
---

# FLASH sweep 2026-05-18 06:00 EDT (scheduled, Monday morning pre-brief) — CLEAN

## Sweep summary

**Mode:** flash_sweep (scheduled 06:00 EDT Monday window)
**Window:** 2026-05-18T00:00:00-04:00 → 2026-05-18T06:00:00-04:00 (~6h since 00:00 FLASH 9c61bdb)
**Trigger evaluation outcome:** 0 of 6 FLASH triggers fired.
**Disposition:** clean sweep — no candidates promoted to grader; no escalation; no Discord post (FLASH-POLICY: silent on clean sweep + quiet-hours active regardless).
**Quiet-hours state:** ACTIVE-QUIET (06:00 EDT inside 21:00–09:00 EDT quiet-hours per FLASH-POLICY.md — had any trigger fired, post to `#flash-alerts` would have QUEUED to `infrastructure/flash-queue.yaml` for 09:00 catchup sweep, NOT posted live). Critical-override conditions NOT met across any in-window item (no CVSS 10.0 + active exploitation + tracked actor + A&D watchlist entity coincidence — see per-item evaluations below).

## Sources queried (active A-grade / B-grade priority set)

- **BleepingComputer** (`bleepingcomputer`) — reachable (200, last-modified 2026-05-18T09:53 UTC = 05:53 EDT inside window from feed-server activity, etag ef38ed6d6ae23ccd6c5aa988b60bdcdc), **3 in-window items** after since-filter: (a) Microsoft Windows 11 KB5089549 install issues 08:33 UTC = 04:33 EDT (technical-operations class, not a threat-intel surface, no actor, no CVE, all 6 triggers FAIL — DISCARDED at filter), (b) DirtyDecrypt Linux kernel rxgk LPE CVE-2026-31635 PoC 07:18 UTC = 03:18 EDT (see Item 5 evaluation below), (c) Pwn2Own Berlin 2026 final wrap $1.298M / 47 zero-days 05:33 UTC = 01:33 EDT (see Item 4 evaluation below).
- **The Hacker News** (`thehackernews`) — reachable (200, last-modified 2026-05-18T08:44 UTC = 04:44 EDT inside window from feed-server activity, 50 items in feed total), **2 in-window items** after since-filter: (a) Fast16 nuclear-weapons-simulations Symantec confirmation 06:46 UTC = 02:46 EDT (see Item 6 evaluation below), (b) MiniPlasma Windows 0-day 04:59 UTC = 00:59 EDT (see Item 7 evaluation below).
- **SecurityWeek** (`securityweek`) — reachable (200, last-modified 2026-05-18T09:45 UTC = 05:45 EDT inside window from feed-server activity, etag W/"3fa4bd7c0ad0ec41a3ee02c99c3bd46d"), **4 in-window items** after since-filter: (a) First Shai-Hulud Worm Clones Emerge 09:45 UTC = 05:45 EDT (see Item 2 evaluation below), (b) Grafana Confirms Breach / Coinbase Cartel 08:34 UTC = 04:34 EDT (see Item 3 evaluation below), (c) Exploitation of Critical NGINX Vulnerability Begins 07:27 UTC = 03:27 EDT (see Item 1 evaluation below), (d) Hackers Earn $1.3M at Pwn2Own Berlin 2026 04:05 UTC = 00:05 EDT (see Item 4 evaluation below — parallel coverage to BleepingComputer).
- **CISA all.xml** (`cisa-advisories`) — reachable (200, 30 items in feed), 0 in-window items after since-filter.
- **The Record** (`the-record`) — reachable (200), 0 in-window items (5 items total in feed, all pre-window).
- **Unit 42 feedburner** (`unit42`) — reachable (200, last-modified 2026-05-18T08:35 UTC = 04:35 EDT from feed-server activity, but 15 items total all pre-window), 0 in-window items after since-filter.
- **Microsoft Security Blog parent feed** (`mstic`) — reachable (200, last-modified 2026-05-14T21:51 UTC pre-window), 0 in-window items.
- **DarkReading** (`darkreading`) — reachable (200, last-modified 2026-05-18T10:01 UTC fresh, only 1 in-window item) — same "The Boring Stuff is Dangerous Now" Shlomie Liberow AI-essay forward-dated 2026-05-18T13:00 UTC (already discarded in 2026-05-17 18:00 FLASH 33d3f9a + 2026-05-18 00:00 FLASH 9c61bdb — anti-noise applies; same DISCARDED disposition).
- **Mandiant feedburner** (`mandiant`) — known broken (~20+ consecutive 404s, feedburner endpoint persistently retired); skipped per source-health.
- **CrowdStrike RSS** — not re-tested this sweep per established marketing-only pattern (15+ consecutive sweeps returning 10 dateless MQ items per source-health note; persistent no-threat-intel-content pattern).
- **Cisco Talos** — `feeds/posts/default` broken-path pattern continues; canonical `blog.talosintelligence.com/rss/` workaround not re-tested this FLASH-fast sweep per scope discipline.
- **SANS ISC** (`sans-isc`) — not re-tested this FLASH-fast sweep (would validate 2026-05-18 00:00 transient parse-error class).
- **Sophos** (`news.sophos.com/en-us/feed/`) — known 404, carried in stale state per source-health.
- **GitHub Advisories Atom** (`github-advisories`) — known persistent 406; not re-tested.
- **CISA KEV JSON** (`cisa-kev`) — not WebFetched directly this FLASH-fast sweep; relies on `cisa-advisories` all.xml master feed (0 in-window items). KEV state unchanged from 2026-05-18 00:00 sweep state (CVE-2026-42897 due 2026-05-29 / CVE-2026-20182 federal deadline LAPSED end-of-day 2026-05-17 / CVE-2026-42208 due 2026-05-11 / CVE-2026-6973 / CVE-2026-0300 — all carry-forwards).

## Splunk first-party non-self-telemetry sweep

- `index=defenseclaw_local OR index=archimedes earliest=-6h@h | stats count by index, sourcetype`:
  - `archimedes` / `archimedes:operation` — 1 event (self-telemetry, run lifecycle).
  - `archimedes` / `archimedes:scheduler` — 3 events (self-telemetry, scheduled-task firing).
  - **0 events** outside self-telemetry sourcetypes.
- `index=defenseclaw_local OR index=archimedes NOT sourcetype=archimedes:scheduler NOT sourcetype=archimedes:operation earliest=-24h@h | head 20` — **0 events.**

This is the **41st consecutive dormant non-self-telemetry Splunk sweep** (40 at 2026-05-18 00:00 FLASH 9c61bdb; 39 at 2026-05-17 18:00 FLASH 33d3f9a; 38 at 16:00 afternoon brief 005596f; 37 at 15:30 pre-brief; 36 at 12:00 FLASH c17bf91; 35 at 08:00 morning brief c8a140d). Per doctrine: silence is not disconfirming. No IOC hits against `threats/iocs/_master-index.yaml`. **No Trigger 3 fire.**

## In-window items evaluated

### Item 1 — SecurityWeek (2026-05-18T07:27 UTC = 03:27 EDT, inside window): "Exploitation of Critical NGINX Vulnerability Begins"

**Source:** SecurityWeek (Ionut Arghire byline). Source grade: B (provisional). Underlying observer: **VulnCheck** (Patrick Garrity). VulnCheck not currently in `source-grades.yaml`; first surface as named primary in Archimedes corpus (prior 2026-05-17 12:00 FLASH evaluation cited VulnCheck via The Hacker News relay only — this is a second relay surface, NOT a new direct-retrieval surface).

**Headline content (per WebFetch direct retrieval):**

- **CVE:** CVE-2026-42945 (NGINX Rift heap overflow in rewrite module). Carry-forward from finding-2026-05-16-0001 and finding-2026-05-14-0002 (F5 K000160932 quarterly advisory).
- **CVSS:** 9.2 (v4 per F5 K000160932; unchanged).
- **Exploitation classification:** VulnCheck exact language per WebFetch: "We're seeing active exploitation of CVE-2026-42945 in F5 NGINX...on VulnCheck Canaries just days after the CVE was published." The phrase "VulnCheck Canaries" specifies their **honeypot canary infrastructure** — same evidentiary class as the 2026-05-17 12:00 FLASH evaluation (commit c17bf91) which characterized VulnCheck honeypot observations as scanner-class probes / defensive telemetry, NOT A-grade attestation of confirmed production exploitation against live targets.
- **Named victims:** NONE. No A&D entity named. No specific victim organization identified.
- **IOCs:** NONE published (no IPs, no domains, no hashes).
- **Attribution:** NONE. No tracked actor named (no TeamPCP, no APT, no UNC, no named threat-actor cluster).
- **Patch status:** F5 patches released prior to exploitation observation per F5 K000160932 carry-forward; no update.
- **Editorial framing concern (Hard Rule 2):** SecurityWeek headline "Exploitation of Critical NGINX Vulnerability Begins" exceeds VulnCheck's actual claim scope — VulnCheck observes activity on their own canary infrastructure (i.e., scanner-class probes), which is methodologically different from "exploitation in the wild against real targets." Same Hard Rule 2 evaluation as 2026-05-17 12:00 FLASH on The Hacker News' "exploited in the wild" framing on the same VulnCheck source.

**FLASH-trigger evaluation:**

- **Trigger 1 (Critical CVE actively exploited, CVSS ≥ 9.0, A-grade attestation):**
  - CVSS 9.2 (PASS on the ≥9.0 threshold).
  - **Active exploitation A-grade attestation: FAIL.** VulnCheck is not in `source-grades.yaml`; conservative provisional grade would be B per Sysdig (2026-05-14 first surface as honeypot/scanner-detection vendor) and SecurityWeek precedent. SecurityWeek is provisional-B media-relay layer. Both sources are B-grade-or-lower; neither meets the A-grade-attestation requirement.
  - **Production-exploitation-vs-canary-scanner-class distinction: FAIL on production exploitation leg.** VulnCheck's exact language scopes the observation to "VulnCheck Canaries" — i.e., their canary/honeypot infrastructure detecting scanner-class probes from internet-facing attackers running their published-PoC payload. This is the same defensive-telemetry evidentiary class that the 2026-05-17 12:00 FLASH evaluation (commit c17bf91), 16:00 afternoon brief (005596f), and 18:00 FLASH (33d3f9a) characterized as NOT A-grade attestation of confirmed production exploitation. Anti-noise rule 1 active on CVE-2026-42945 trigger-topic (finding-2026-05-16-0001 carry-forward chain).
  - **DISPOSITION: Trigger 1 FAIL.** Single-source B-grade-or-lower media relay + canary/honeypot-scanner-class-only observation + editorial-framing-exceeds-source-scope (Hard Rule 2) + anti-noise rule 1 active (same trigger-topic as ongoing CVE-2026-42945 carry-forward) — disposition is status-update CANDIDATE for 08:00 morning brief grader for evaluation as CVE-2026-42945 carry-forward refinement (defensive-telemetry expansion: SecurityWeek + The Hacker News + Ionut Arghire byline cluster on VulnCheck Canaries observations), NOT a FLASH-trigger fire.
- **Trigger 2 (New tracked actor attribution):** FAIL. No `_roster.yaml` actor named.
- **Trigger 3 (First-party Splunk IOC hit, within 24h):** FAIL. 41st consecutive dormant non-self-telemetry Splunk sweep; no IOCs from source to query against in any case.
- **Trigger 4 (Tracked actor TTP change, A/B-grade source, attributable):** FAIL. No tracked actor; TTP not attributable.
- **Trigger 5 (Active A&D-sector campaign, multi-victim):** FAIL. No A&D entity named; no specific victim count.
- **Trigger 6 (Zero-day no-patch, CVSS ≥ 8.0 or widely-deployed, exploitation confirmed/imminent):** FAIL on patch-absence leg (patched per F5 K000160932 carry-forward) AND on exploitation-confirmed-or-imminent-per-A-grade leg (canary scanner-class probes are defensive-telemetry, not A-grade-attested production exploitation). Wide-deployment criterion: MET (NGINX broadly deployed, ~5.7M instances per source). CVSS ≥ 8.0: MET (9.2). But the conjunction fails because patches exist AND exploitation-class evidence is sub-A-grade defensive-telemetry.

**Disposition for SecurityWeek NGINX Rift "exploitation begins":** **DISCARDED for FLASH purposes.** Status-update CANDIDATE for 08:00 morning brief grader as CVE-2026-42945 carry-forward refinement (defensive-telemetry surface expansion from VulnCheck canaries via SecurityWeek + The Hacker News dual relay; underlying VulnCheck primary unchanged from 2026-05-17 12:00 evaluation; Ionut Arghire byline now anchors the dual-relay coverage). Hard Rule 2 prevents propagation of SecurityWeek's "exploitation begins" editorial framing as Archimedes-originated active-exploitation claim. Hard Rule 3 PoC repository URL not linked.

### Item 2 — SecurityWeek (2026-05-18T09:45 UTC = 05:45 EDT, inside window): "First Shai-Hulud Worm Clones Emerge"

**Source:** SecurityWeek (Ionut Arghire byline). Source grade: B (provisional). Underlying observer: **Ox Security** (provisional B, first-surface direct-retrieval pending per 2026-05-15 entry in `source-grades.yaml`).

**Headline content (per WebFetch direct retrieval):**

- **Mechanism:** Threat actor distinct from TeamPCP has adopted the publicly-released Shai-Hulud worm source code (released by TeamPCP per flash-2026-05-15-0600-teampcp-shai-hulud-release / finding-2026-05-15-FLASH-0002 / VT-006 carry-forward) and is using it to publish malicious npm packages.
- **Attribution language (per WebFetch verbatim):** "According to Ox Security, a threat actor published four NPM packages containing infostealer malware." — explicitly an UNATTRIBUTED actor distinct from TeamPCP.
- **Named victim packages (4 npm packages):**
  - `@deadcode09284814/axios-util`
  - `axois-utils`
  - `chalk-tempalte`
  - `color-style-utils`
- **Ecosystem:** npm only. NO PyPI references (unlike the parent 2026-05-12 Mini Shai-Hulud campaign which was npm + PyPI dual-ecosystem per VT-006).
- **Named A&D entity victims:** NONE. No defense / aerospace entity named.
- **No mention of @squawk aviation namespace or @tanstack** in the cloned package set.
- **Operational characterization (per WebFetch):** "first phase of an upcoming wave" — Ox Security framing, not contrast-analysis with the 2026-05-12 Mini Shai-Hulud campaign.

**FLASH-trigger evaluation:**

- **Trigger 1 (Critical CVE actively exploited):** FAIL. No CVE assigned to this clone activity; CVE-2026-45321 is the VT-006 parent surface CVE but clone packages do not extend its CVE scope. No CVSS.
- **Trigger 2 (New tracked actor attribution):** **FAIL.** The cloning actor is EXPLICITLY UNATTRIBUTED per Ox Security's exact language ("a threat actor"). TeamPCP (#001 HIGH) is credited only with the source-code RELEASE act (per the 2026-05-15 06:55 EDT FLASH carry-forward via finding-2026-05-15-FLASH-0002), NOT with the cloning act. Ox Security disciplines its attribution per Hard Rule 2 compliance — same restraint pattern as Socket / StepSecurity / Ox Security / Upwind on the node-ipc compromise (finding-2026-05-14-0009 + finding-2026-05-15-0005 four-firm UNATTRIBUTED consensus). Per INTEL-GRADING + Hard Rule 2, Archimedes does NOT cross-attribute this clone activity to TeamPCP from the relay; the clone-publisher actor is non-roster + UNATTRIBUTED.
- **Trigger 3 (First-party Splunk IOC hit, within 24h):** FAIL. 41st consecutive dormant non-self-telemetry Splunk sweep; clone packages would not appear in defense-network telemetry without active developer-machine infection.
- **Trigger 4 (Tracked actor TTP change, A/B-grade source, attributable):**
  - Source-grade: Ox Security provisional B (cited via SecurityWeek provisional B relay); both qualify as A/B-grade.
  - Attributable: FAIL — the clone-publisher actor is UNATTRIBUTED, not a tracked actor per `_roster.yaml`; the cloning is NOT a TeamPCP TTP because Ox explicitly distinguishes the cloning act from TeamPCP's source-code release act.
  - **TeamPCP-direct TTP change reading:** The flash-2026-05-15-0600-teampcp-shai-hulud-release brief explicitly forecast "derivative attacks expected forward 30 days" with WEP "likely." The clones materialize that forecast at T+3d. However: (a) the derivative-actor is NOT TeamPCP (Ox decline attribution), so this is not a TeamPCP-direct TTP change; (b) anti-noise rule 1 is active on the trigger-topic teampcp-shai-hulud-source-code-release-bounty (24h window expired 2026-05-16T06:35 — outside the 24h lock, BUT the trigger-topic is the parent campaign cluster, not a new topic; downstream-actor adoption of released code is an EXPECTED + PREDICTED follow-on, not a Trigger 4 fire on TeamPCP itself).
  - **DISPOSITION: Trigger 4 FAIL.** The clone-publisher actor is non-roster UNATTRIBUTED; no tracked actor's TTP has changed. This is a VT-006 carry-forward refinement and a materialization of the previously-stated WEP "likely" forecast on derivative-attacks.
- **Trigger 5 (Active A&D-sector campaign, multi-victim):** FAIL. No A&D entity named; victim package count is 4 npm packages, no organizational victims named.
- **Trigger 6 (Zero-day no-patch):** FAIL. No CVE; existing CVE-2026-45321 (VT-006 parent) is patched-by-rolling-unpublishes (no new patch boundary). No new zero-day disclosed.

**Disposition for SecurityWeek Shai-Hulud worm clones:** **DISCARDED for FLASH purposes.** Status-update CANDIDATE for 08:00 morning brief grader as VT-006 / Mini Shai-Hulud lineage carry-forward refinement — the clones MATERIALIZE the predicted "derivative attacks expected forward 30 days" WEP "likely" from flash-2026-05-15-0600-teampcp-shai-hulud-release at T+3d post-source-code-release, validating the briefer's forecast. Defensive-relevance: A&D-prime SOCs should add the 4 cloned package names to npm dependency-tree-quarantine watchlists. Hard Rule 2 prevents TeamPCP-cross-attribution origination on the cloning act; Ox Security's explicit UNATTRIBUTED framing is preserved verbatim. The four-firm UNATTRIBUTED consensus pattern (Socket / StepSecurity / Ox Security / Upwind on node-ipc) extends here — Ox Security maintains attribution discipline.

### Item 3 — SecurityWeek (2026-05-18T08:34 UTC = 04:34 EDT, inside window): "Grafana Confirms Breach After Hackers Claim They Stole Data"

**Source:** SecurityWeek (Eduard Kovacs byline). Source grade: B (provisional). Grafana = victim self-disclosure (A-procedural on own incident per OpenAI / TanStack 2026-05-14 precedent class).

**Headline content (per WebFetch direct retrieval):**

- **Threat actor named:** "Coinbase Cartel" — a cybercrime cluster. NOT in `_roster.yaml`.
- **Attribution chain (per WebFetch verbatim):** "Cybersecurity companies say Coinbase Cartel is linked to ShinyHunters, Scattered Spider, and Lapsus$, whose members have been collaborating since at least mid-2025, with some evidence pointing to a possible partnership dating back to 2024."
- **A-grade vendor attribution check:** NONE cited (Mandiant / CrowdStrike / Unit 42 / MSTIC / Volexity all absent). SecurityWeek attribution is to unnamed "cybersecurity companies" — single-source-relay-of-unnamed-cluster.
- **Data breached:** Source code only. Grafana statement (per WebFetch): "the hackers managed to download its codebase, but said no personal or customer information was stolen."
- **A&D entity named as victim or downstream-exposed:** NONE.
- **IOCs published:** NONE.
- **Impact scope per Grafana:** "no personal or customer information was stolen and the incident has not impacted customer systems or operations."

**FLASH-trigger evaluation:**

- **Trigger 1 (Critical CVE):** FAIL — no CVE / no CVSS.
- **Trigger 2 (New tracked actor attribution):**
  - Scattered Spider (#013 HIGH) is in roster. The attribution chain is **Grafana → Coinbase Cartel** (direct attribution) **→ "linked to" ShinyHunters / Scattered Spider / Lapsus$** (per unnamed "cybersecurity companies" per SecurityWeek).
  - Per **Hard Rule 2** (never originate attribution) + **INTEL-GRADING single-source veto** (only SecurityWeek as relay; underlying "cybersecurity companies" not named): Archimedes does NOT cross-attribute this breach to Scattered Spider as a Trigger 2 fire. SecurityWeek's "linked to" language is multi-step indirect attribution (Coinbase Cartel → linked to → Scattered Spider) — this is attribution-of-attribution-of-relay, which is exactly the laundering pattern Hard Rule 2 + LEGAL-POLICY §Attribution Standards prohibit.
  - No A-grade vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC) names Scattered Spider as the Grafana-breach actor in window.
  - **DISPOSITION: Trigger 2 FAIL.** Coinbase Cartel is non-roster; Scattered-Spider-cross-attribution from SecurityWeek single-source relay is methodologically prohibited per Hard Rule 2 + LEGAL-POLICY no-attribution-laundering.
- **Trigger 3 (First-party Splunk IOC hit, within 24h):** FAIL. Splunk dormant; no Grafana-breach-related IOCs published anyway.
- **Trigger 4 (Tracked actor TTP change):** FAIL. The TTP would only be attributable to Scattered Spider if Trigger 2 attribution path were valid (it is not — see above).
- **Trigger 5 (Active A&D-sector campaign, multi-victim):** FAIL. Single victim (Grafana); no A&D entity; no campaign-class narrative.
- **Trigger 6 (Zero-day no-patch):** FAIL — no CVE.

**Disposition for SecurityWeek Grafana / Coinbase Cartel breach:** **DISCARDED for FLASH purposes.** Status-update CANDIDATE for 08:00 morning brief grader for evaluation as possible Scattered Spider (#013 HIGH) cluster-adjacent surface PENDING A-grade vendor corroboration (Mandiant / CrowdStrike / Unit 42 / MSTIC explicit Scattered-Spider attribution to Grafana breach). Defensive-relevance to A&D-prime SOCs running Grafana for observability is structural-indirect (no production / customer / R&D data impact per Grafana's bounded-scope statement). Hard Rule 2 prevents Scattered-Spider attribution origination from SecurityWeek's "linked to" relay of unnamed "cybersecurity companies."

### Item 4 — SecurityWeek + BleepingComputer (2026-05-18T04:05 + 05:33 UTC, parallel coverage): "Pwn2Own Berlin 2026 final wrap — $1.298M, 47 zero-days, DEVCORE Master of Pwn"

**Sources:** SecurityWeek (Eduard Kovacs byline) + BleepingComputer (Sergiu Gatlan byline). Both source grade: B (provisional). Originating authority: **ZDI / Trend Micro** (provisional A — `zdi-blog`, first cited finding-2026-05-16-0002).

**Headline content (per WebFetch direct retrieval, BleepingComputer):**

- **Final totals:** Day 1 ($523,000 / 24 zero-days) + Day 2 ($385,750 / 15 zero-days) + Day 3 ($389,500 / 8 zero-days) = **$1,298,250 / 47 zero-days total**.
- **Note on prior Archimedes coverage:** finding-2026-05-16-0002 carry-forward through 00:00 FLASH evaluated event total as $943,250 through Day 3 — discrepancy with $1.298M today (the $1.298M figure includes prior corrections / late bonus payouts ZDI publishes in the post-event wrap; Day-3 total revised from $34,500 to $389,500 likely includes the final-day bonus tier per standard Pwn2Own scorekeeping).
- **Master of Pwn:** **DEVCORE** with 50.5 points and $505,000 in rewards — Orange Tsai's team wins (consistent with finding-2026-05-16-0002 forecast).
- **Orange Tsai / DEVCORE Exchange RCE-to-SYSTEM chain:** $200,000 awarded for chaining 3 bugs to RCE-with-SYSTEM on Microsoft Exchange. **Standard ZDI 90-day vendor-coordinated-disclosure embargo remains intact** through ~2026-08-13 (finding-2026-05-16-0002 carry-forward unchanged).
- **A&D-relevant products:** NONE. Affected products: Microsoft Exchange / SharePoint / Edge / Windows 11, Red Hat Linux, NVIDIA, VMware ESXi.
- **Tracked actors named:** NONE. Only security research teams: DEVCORE, STARLabs SG, Out Of Bounds, IBM X-Force.
- **Active exploitation in the wild claim distinct from contest:** NONE.

**FLASH-trigger evaluation:**

- **All 6 triggers FAIL.** Contest results, no active exploitation in the wild, no tracked actor attribution, no A&D entity, no CVE assigned to in-window claims (all CVEs under embargo per ZDI 90-day disclosure clock), no first-party Splunk IOC hits.

**Disposition for Pwn2Own Berlin 2026 final wrap:** **DISCARDED for FLASH purposes.** Status-update CANDIDATE for 08:00 morning brief grader as finding-2026-05-16-0002 carry-forward refinement (final event totals: $1.298M total / 47 zero-days / DEVCORE Master of Pwn / Orange Tsai Exchange chain $200K under ZDI embargo through ~2026-08-13). Anti-noise rule 1 applies (same trigger-topic as ongoing finding-2026-05-16-0002 carry-forward across multiple sweeps).

### Item 5 — BleepingComputer (2026-05-18T07:18 UTC = 03:18 EDT, inside window): "Exploit available for new DirtyDecrypt Linux root escalation flaw"

**Source:** BleepingComputer (Sergiu Gatlan byline). Source grade: B (provisional). Underlying researcher: **V12 security team** (not in `source-grades.yaml`; first surface in Archimedes corpus). Analyst providing CVE linkage: **Will Dormann (Tharros)** (not in `source-grades.yaml`; first surface as named-analyst byline).

**Headline content (per WebFetch direct retrieval):**

- **CVE identifier:** **CVE-2026-31635** (linked by Will Dormann / Tharros).
- **Vulnerability class:** Local Privilege Escalation (LPE) to root in Linux kernel rxgk module. Codename: **DirtyDecrypt**.
- **CVSS score:** **NOT DISCLOSED** in source.
- **Patch status:** Patched in Linux mainline 2026-04-25. Affected distros (closely following upstream): **Fedora, Arch Linux, openSUSE Tumbleweed**. NO mention of RHEL / Debian stable / Ubuntu LTS — narrower wide-deployment footprint than enterprise distros.
- **Active exploitation status:** **PoC ONLY.** Per WebFetch verbatim: "V12's proof-of-concept exploit has only been tested against Fedora and the mainline Linux kernel." NO A-grade vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC / Volexity / Talos / Symantec / ESET / CISA) attests in-the-wild exploitation. Article references "recent exploitation of a different flaw (Copy Fail)" — explicitly distinguishing DirtyDecrypt from any in-the-wild-exploited surface.
- **Originating researcher:** **V12 security team** (discovered + reported May 9, 2026; PoC published).
- **Named tracked actor:** NONE.
- **A&D entity named:** NONE.
- **IOCs:** NONE published (PoC code referenced via GitHub link in V12 security repository — Hard Rule 3 PoC URL not linked).

**FLASH-trigger evaluation:**

- **Trigger 1 (Critical CVE actively exploited, CVSS ≥ 9.0, A-grade attestation):**
  - CVSS not disclosed in source — **CVSS ≥ 9.0 leg UNKNOWN/FAIL** (LPE-to-root class typically scores ~7.0-7.8 on CVSS v3 base; rxgk module LPE likely in that range, below 9.0 floor).
  - Active exploitation A-grade attestation: **FAIL** (PoC-only per V12 itself; no vendor confirmation; same Hard Rule 2 evidentiary bar as MiniPlasma).
  - **DISPOSITION: Trigger 1 FAIL.**
- **Trigger 2 (New tracked actor attribution):** FAIL — no tracked actor; V12 security team is non-roster researcher.
- **Trigger 3 (First-party Splunk IOC hit, within 24h):** FAIL — Splunk dormant; no IOCs published.
- **Trigger 4 (Tracked actor TTP change):** FAIL — no tracked actor.
- **Trigger 5 (Active A&D-sector campaign, multi-victim):** FAIL — no A&D entity / no campaign.
- **Trigger 6 (Zero-day no-patch, CVSS ≥ 8.0 or widely-deployed, exploitation confirmed/imminent):**
  - Wide-deployment criterion: **PARTIAL** (Fedora / Arch / openSUSE Tumbleweed only — narrower than RHEL / Debian / Ubuntu LTS; not "widely deployed" in the A&D-prime enterprise context).
  - Patch-absence: **FAIL** (patched in mainline 2026-04-25; affected distros also patched per upstream-following).
  - CVSS ≥ 8.0: **UNKNOWN** (not stated).
  - Exploitation confirmed-or-imminent per A-grade: **FAIL** (PoC-only, no A-grade attestation, V12 not on `source-grades.yaml`).
  - **DISPOSITION: Trigger 6 FAIL.** Patch-absence leg is decisive — the kernel is patched upstream.

**Disposition for BleepingComputer DirtyDecrypt:** **DISCARDED for FLASH purposes.** Status-update CANDIDATE for 08:00 morning brief grader for evaluation as new tracked-vuln consideration only if A-grade corroboration surfaces (vendor in-the-wild observation, CISA KEV addition, or A-grade attribution to a tracked actor). Same disposition class as MiniPlasma (PoC-only, single-source B-grade media relay, no A-grade attestation, no tracked actor). Defensive-relevance to A&D-prime Linux fleets is structural-indirect (most A&D primes run RHEL / Ubuntu LTS / Debian stable, NOT Fedora / Arch / openSUSE Tumbleweed — narrower exposure footprint than the BleepingComputer headline suggests). Hard Rule 3 PoC repository URL not linked.

### Item 6 — The Hacker News (2026-05-18T06:46 UTC = 02:46 EDT, inside window): "Pre-Stuxnet Fast16 Malware Tampered with Nuclear Weapons Simulations"

**Source:** The Hacker News (`info@thehackernews.com` byline). Source grade: B (provisional). Underlying originating primary: **Broadcom-owned Symantec + Carbon Black teams** (provisional A first cited 2026-05-13 per finding-2026-05-13-FLASH-1800-0001; 72h ratification clock fired 2026-05-16T18:25; now T+35h+ past elapsed). Sequential prior research: **SentinelOne / SentinelLabs** (provisional A first cited 2026-05-08).

**Headline content (per WebFetch direct retrieval):**

- **Research attribution:** "Broadcom-owned Symantec and Carbon Black teams" published this analysis confirming Fast16's sabotage intent against uranium-compression simulations central to nuclear weapon design.
- **Sequential relationship:** Per WebFetch verbatim: "The development comes weeks after SentinelOne presented an analysis of fast16, describing it as the first sabotage framework whose components may have developed as early as 2005, predating the earliest known version of Stuxnet...by two years."
- **Temporal frame:** **Historical 2005-2010 era** — pre-Stuxnet sabotage tooling. NOT active 2026 exploitation.
- **Named victims:** NONE specifically named (no Sandia, no Los Alamos, no LLNL, no A&D primes).
- **Actor attribution:** **Implicit Equation Group** (state-sponsored, NSA-tied per The Shadow Brokers 2017 leak). Equation Group is **NOT in `_roster.yaml`** — Archimedes does not track suspected-Five-Eyes attribution clusters in the same operational way as adversary nation-state actors (per CLAUDE.md mission focus on Iranian / Russian / Chinese / North Korean APTs + criminal clusters).
- **IOCs:** NONE provided.
- **Corroborating A-grade sources beyond Symantec + SentinelOne:** NONE (Mandiant / CrowdStrike / Unit 42 / MSTIC all absent per WebFetch).

**FLASH-trigger evaluation:**

- **Trigger 1 (Critical CVE actively exploited):** FAIL — no 2026 CVE / no current active exploitation (historical 2005-2010 surface).
- **Trigger 2 (New tracked actor attribution):** **FAIL.** Equation Group is not in `_roster.yaml`. Per CLAUDE.md scope ("Iranian cyber operations, and global APT tracking") + LEGAL-POLICY no-attribution-origination, Archimedes does NOT originate suspected-Five-Eyes attribution as new tracked-actor surface. The implicit-NSA-attribution layer is via The Shadow Brokers 2017 leak provenance + SentinelOne's prior analysis framing, not via current vendor-attested claim in this article.
- **Trigger 3 (First-party Splunk IOC hit, within 24h):** FAIL — Splunk dormant; no IOCs to query.
- **Trigger 4 (Tracked actor TTP change):** FAIL — Equation Group is non-roster + historical 2005-2010 activity is not a current TTP change.
- **Trigger 5 (Active A&D-sector campaign, multi-victim):** **FAIL.** Historical sabotage-framework retrospective, NOT current active campaign. No 2026-active multi-victim claim. (Nuclear-weapons-simulations sabotage is broadly A&D-sector-adjacent — uranium-compression simulations and nuclear weapon design are within the strategic-defense scope. However: (a) the activity is historical, not current; (b) no specific A&D-prime victim named; (c) no multi-victim 2026 campaign described.)
- **Trigger 6 (Zero-day no-patch):** FAIL — historical 2005-2010 sabotage framework, no 2026 CVE / no current patch question.

**Disposition for The Hacker News Symantec Fast16 nuclear-weapons-sims confirmation:** **DISCARDED for FLASH purposes.** Status-update CANDIDATE for 08:00 morning brief grader as finding-2026-05-16-0003 (Symantec/SentinelLABS Fast16 framework) carry-forward refinement — Symantec's confirmation of Fast16's sabotage intent against uranium-compression simulations adds a second-corpus surface on top of the original April 2026 Fast16 framework analysis, strengthening the case for operator pass on the Symantec provisional-A ratification (clock T+35h+ past elapsed at this sweep). Defensive-implications: Fast16's selective-corruption-targeting of physics-simulation pipelines is the operational template that any future adversary-side sabotage-framework against A&D-prime CAD / MBSE / FEA / CFD design pipelines would follow — but Archimedes does not extrapolate A&D-prime exposure from this historical retrospective per Hard Rule 2 + LEGAL-POLICY no-novel-attribution. The Equation Group attribution layer is preserved verbatim from source (implicit, NSA-tied per Shadow Brokers 2017 leak) and is NOT propagated as Archimedes-originated attribution to a new tracked actor.

### Item 7 — The Hacker News (2026-05-18T04:59 UTC = 00:59 EDT, inside window): "MiniPlasma Windows 0-Day Enables SYSTEM Privilege Escalation on Fully Patched Systems"

**Source:** The Hacker News (`info@thehackernews.com` byline). Source grade: B (provisional). Underlying researcher: **Chaotic Eclipse / Nightmare-Eclipse** (not in `source-grades.yaml`; non-roster).

**Headline content (per WebFetch direct retrieval):**

- **CVE assignment:** **No new CVE assigned to MiniPlasma itself.** Per WebFetch verbatim: "originally reported to Microsoft by Google Project Zero researcher James Forshaw in September 2020" and "assumed that the shortcoming was fixed by Microsoft in December 2020 as part of CVE-2020-17103." Researcher characterizes MiniPlasma as a **regression** of the patched 2020 flaw.
- **Active exploitation:** **PoC-only.** Per WebFetch verbatim: "I weaponized the original PoC to spawn a SYSTEM shell. It seems to work reliably in my machines but success rate may vary since it's a race condition." NO MSRC / CISA KEV / Mandiant / CrowdStrike attribution of in-the-wild attacks.
- **Microsoft acknowledgment:** NONE. Per WebFetch verbatim: "I'm unsure if Microsoft just never patched the issue or the patch was silently rolled back."
- **CVSS:** NOT PUBLISHED for MiniPlasma. Related 2025 flaw in same component (CVE-2025-62221) had CVSS 7.8 — class-typical for LPE-to-SYSTEM, below 8.0 floor.
- **Tracked actor:** NONE.
- **A&D entity:** NONE.
- **IOCs:** NONE.
- **Source relationship:** This is The Hacker News' **second relay** of the same originating researcher coverage that BleepingComputer (Lawrence Abrams) published 2026-05-17T22:30 UTC = 18:30 EDT — NOT independent A-grade attestation, NOT a new direct-retrieval surface.

**FLASH-trigger evaluation:**

- **All 6 triggers FAIL** — same as 2026-05-18 00:00 FLASH 9c61bdb evaluation (commit reference): PoC-only, single-source-with-second-relay (BleepingComputer → The Hacker News, both B-grade provisional media), no A-grade exploitation attestation (the "spotted being exploited" framing is B-grade editorial commentary applying to a 3-vuln cluster, not vendor-attested), no tracked actor, no A&D entity, no IOCs, no CVSS published, no new 2026 CVE assignment (this is a 2020 CVE regression claim).
- **Anti-noise rule 1 active** (same trigger-topic MiniPlasma already evaluated 6h ago at 00:00 FLASH; "one FLASH per trigger-topic per 24h" — moot since not a trigger to begin with).

**Disposition for The Hacker News MiniPlasma:** **DISCARDED for FLASH purposes.** Status-update CANDIDATE for 08:00 morning brief grader as **continued non-fire** — MiniPlasma remains a PoC-only single-originating-researcher surface with second relay (BleepingComputer → The Hacker News) but no A-grade corroboration in window. Per 2026-05-18 00:00 FLASH disposition: tracked-vuln list addition pending (a) Microsoft MSRC confirmation of regression, (b) MSTIC active-exploitation telemetry, or (c) CISA KEV addition. Defensive-relevance to A&D-prime Windows 11 fleets is structural-indirect not source-attested. Hard Rule 2 prevents propagation of BleepingComputer's "spotted being exploited" editorial framing.

### Item 8 — DarkReading (2026-05-18T13:00 UTC = 09:00 EDT 2026-05-18 forward-dated): "The Boring Stuff is Dangerous Now"

- Same item already discarded in 2026-05-17 18:00 FLASH 33d3f9a and 2026-05-18 00:00 FLASH 9c61bdb. **DISCARDED per anti-noise.** Same disposition.

## Carry-forwards preserved (NOT re-triggered, all unchanged from 00:00 FLASH 9c61bdb except where noted)

- **CVE-2026-20182** (Cisco Catalyst SD-WAN auth bypass, CVSS 10.0, KEV federal deadline LAPSED end-of-day Sunday 2026-05-17) — finding-2026-05-14-0005 carry-forward chain. **Deadline post-mortem now T+6h+ past elapsed active state for 08:00 morning brief grader.** No fresh A-grade attestation in 00:00–06:00 window (no Mandiant / MSTIC / Unit 42 / Talos / Volexity / CrowdStrike / BleepingComputer / The Hacker News / SecurityWeek in-window items naming CVE-2026-20182 or UAT-8616). Federal-agency-compliance reporting still expected to surface in next-day CISA / OMB reporting per established pattern, not in the KEV catalog itself.
- **CVE-2026-42897** (Microsoft Exchange OWA XSS, KEV T-11d due Friday 2026-05-29) — finding-2026-05-15-0003 carry-forward. >48h single-source veto on exploitation-claim layer holds (Mandiant / Volexity / Unit 42 / MSTIC / CrowdStrike all silent through 2026-05-18 06:00; this sweep extends silence to ~36h+ since afternoon brief 005596f). MSRC remains sole originating attester.
- **CVE-2026-42945 NGINX Rift** (depthfirst PoC + VulnCheck Canaries scanner-class probes) — finding-2026-05-16-0001 carry-forward. **Carry-forward refined this sweep** (Item 1 above): SecurityWeek + The Hacker News dual-relay coverage of VulnCheck Canaries observations now established; Ionut Arghire byline anchors the dual-relay layer; "exploitation begins" editorial framing is B-grade source / B-grade relay, NOT A-grade attestation of confirmed production exploitation. Same evidentiary class as 2026-05-17 12:00 FLASH evaluation; anti-noise rule 1 active. Hard Rule 3 PoC repo URL not linked.
- **Symantec / Carbon Black + SentinelLABS April 2026 Fast16 framework** — finding-2026-05-16-0003 carry-forward. **Carry-forward refined this sweep** (Item 6 above): Symantec's nuclear-weapons-simulations sabotage-intent confirmation adds second-corpus surface on top of the original Fast16 framework analysis; provisional-A 72h ratification clock now T+35h+ past elapsed. Strengthens case for operator pass on Symantec provisional-A ratification. Not actionable in this sweep per task scope.
- **Pwn2Own Berlin 2026 final wrap** (Orange Tsai / DEVCORE Exchange RCE-to-SYSTEM chain, $200K, ZDI 90-day embargo) — finding-2026-05-16-0002 carry-forward. **Carry-forward refined this sweep** (Item 4 above): final event totals confirmed $1.298M / 47 zero-days / DEVCORE Master of Pwn 50.5 points / $505K rewards; Orange Tsai Exchange chain remains under standard 90-day ZDI vendor-coordinated-disclosure embargo through ~2026-08-13.
- **VT-006 / Mini Shai-Hulud / CVE-2026-45321** — finding-2026-05-12-FLASH-0001 + finding-2026-05-15-FLASH-0002 carry-forward chain. **Carry-forward refined this sweep** (Item 2 above): first Shai-Hulud worm clones materialize at T+3d post-source-code-release; 4 npm packages by UNATTRIBUTED actor (Ox Security explicitly disciplines attribution per Hard Rule 2; the cloning is NOT TeamPCP per Ox). Materializes the predicted "derivative attacks expected forward 30 days" WEP "likely" from flash-2026-05-15-0600-teampcp-shai-hulud-release. Anti-noise rule 1 applies (parent campaign cluster trigger-topic, not net-new trigger-topic).
- **Turla / Kazuar / Secret Blizzard D+2 relay layer** — finding-2026-05-14-0006 / reject-2026-05-16-0001 anti-noise duplicate-lock active; no new relay surface this window.
- **Tycoon2FA device-code phishing PhaaS** — absorbed into finding-2026-05-17-0002 per afternoon brief 005596f. Commodity criminal PhaaS, no tracked actor, anti-noise rule 1 active.
- **eSentire provisional-B source-grades.yaml addition candidate** — flagged for librarian pickup; no librarian action expected pre-06:00 sweep. Carried forward to 08:00 morning brief librarian pickup window.
- **MiniPlasma (CVE-2020-17103 rediscovery)** — finding-pending candidate carry-forward from 00:00 FLASH 9c61bdb. **Carry-forward refined this sweep** (Item 7 above): The Hacker News second relay of BleepingComputer originating coverage; no A-grade corroboration; PoC-only; same disposition (status-update CANDIDATE for 08:00 morning brief grader pending MSRC / MSTIC / CISA KEV).

## Net-new status-update candidates surfaced this sweep (for 08:00 morning brief grader evaluation)

1. **CVE-2026-31635 DirtyDecrypt Linux kernel rxgk LPE** — V12 security team PoC; patched in mainline 2026-04-25; narrow distro footprint (Fedora / Arch / openSUSE Tumbleweed only); no A-grade exploitation attestation; same disposition class as MiniPlasma — tracked-vuln list addition pending A-grade corroboration. Will Dormann (Tharros) named-analyst byline first surface in corpus (potential provisional-grade candidate for `source-grades.yaml` if Tharros surfaces again as named analyst).
2. **Shai-Hulud worm clones (4 npm packages by UNATTRIBUTED actor via Ox Security)** — materializes predicted derivative-attacks-30-days WEP from flash-2026-05-15-0600-teampcp-shai-hulud-release at T+3d; package names for npm dependency-tree-quarantine watchlists. VT-006 carry-forward refinement.
3. **Grafana / Coinbase Cartel breach** — Scattered Spider (#013 HIGH) cluster-adjacent surface via SecurityWeek single-source-relay-of-unnamed-cybersecurity-companies attribution chain; Hard Rule 2 + LEGAL-POLICY no-attribution-laundering prevents Trigger 2 fire; pending A-grade vendor corroboration.

## Source health observations (this sweep) — operator pass deferred, NOT applied to source-health.yaml

Per established precedent (operator has pending edits to source-health.yaml per untracked-files state including `.pm-update.py`, `.afternoon-edits.txt`, `.diff-summary*` files), these observations are recorded here ONLY; source-health.yaml is NOT modified by this collector invocation.

- `bleepingcomputer`: 200 with 3 productive in-window items (DirtyDecrypt + Pwn2Own wrap + Windows 11 KB5089549 install issues); healthy continues.
- `thehackernews`: 200 with 2 productive in-window items (Fast16 nuclear-weapons-sims confirmation + MiniPlasma); healthy continues.
- `securityweek`: 200 with 4 productive in-window items (NGINX exploitation + Shai-Hulud clones + Grafana breach + Pwn2Own wrap); healthy continues. **Highest-productivity sweep for SecurityWeek in the last 14 days** (matches Ionut Arghire + Eduard Kovacs bylines on critical topics).
- `cisa-advisories`: all.xml 200, 0 in-window items (CVE-2026-20182 KEV deadline post-mortem reporting not yet surfaced in catalog feed); healthy continues.
- `darkreading`: 200 with 1 in-window item (re-discarded per anti-noise); healthy continues.
- `the-record`: 200 with 0 in-window items; healthy continues.
- `unit42` feedburner: 200 with 0 in-window items; healthy continues.
- `mstic` parent feed: 200 with 0 in-window items (last-modified 2026-05-14 pre-window); healthy continues.
- `mandiant`, `dragos`, `sophos`, `ars-security`, `github-advisories`: carried in expected-broken / stale state per source-health.yaml; no action.
- `crowdstrike`, `cisco-talos`, `sans-isc`: not re-tested this FLASH-fast sweep per scope discipline.

## Disposition

**Clean sweep, 0 FLASH triggers fired, 41st consecutive dormant non-self-telemetry Splunk sweep, no escalation, no Discord post.**

Seven in-window items evaluated and all DISCARDED for FLASH purposes — all eight if the DarkReading anti-noise re-discard is counted. Carry-forwards refined where new evidence surfaced (Items 1, 2, 4, 6, 7) but no carry-forward elevated to net-new FLASH trigger. Three net-new status-update candidates surfaced for 08:00 morning brief grader (DirtyDecrypt CVE-2026-31635, Shai-Hulud worm clones, Grafana / Coinbase Cartel breach).

The 08:00 morning brief grader (Monday 2026-05-18, ~2h from this sweep) will inherit a notably-productive carry-forward state: (1) CVE-2026-20182 federal KEV deadline post-mortem reporting (deadline LAPSED end-of-day Sunday); (2) CVE-2026-42897 Exchange OWA XSS T-11d carry-forward; (3) CVE-2026-42945 NGINX Rift VulnCheck Canaries dual-relay refinement (defensive telemetry, NOT A-grade production exploitation); (4) Pwn2Own Berlin 2026 final wrap; (5) Symantec Fast16 nuclear-weapons-sims confirmation strengthening provisional-A ratification case; (6) VT-006 Shai-Hulud worm clones materialization at T+3d post-source-code-release; (7) Grafana / Coinbase Cartel breach; (8) DirtyDecrypt Linux kernel CVE-2026-31635 PoC; (9) MiniPlasma continued non-fire pending A-grade corroboration.

**Hard Rule 2 compliance verified** across all 7 evaluations:
- SecurityWeek "exploitation begins" framing on CVE-2026-42945 preserved verbatim as B-grade-relay editorial, NOT propagated as Archimedes-originated active-exploitation claim;
- Ox Security UNATTRIBUTED framing on Shai-Hulud worm clones preserved verbatim, NOT cross-attributed to TeamPCP from clone-publisher act;
- SecurityWeek "Coinbase Cartel linked to ShinyHunters / Scattered Spider / Lapsus$" multi-step relay-of-unnamed-cybersecurity-companies NOT propagated as Trigger 2 Scattered-Spider attribution;
- Symantec Fast16 Equation Group implicit attribution preserved verbatim, NOT propagated as Archimedes-originated attribution to new tracked actor;
- BleepingComputer + The Hacker News MiniPlasma "spotted being exploited" editorial framing NOT propagated as A-grade-attested production exploitation.

**Hard Rule 3 compliance verified** — no PoC repository URLs linked (CVE-2026-42945 depthfirst GitHub, CVE-2026-31635 V12 security GitHub, MiniPlasma Chaotic-Eclipse / Nightmare-Eclipse PoC code all referenced by source but URLs / payloads NOT reproduced).

**LEGAL-POLICY prohibited-query-patterns** not triggered (no active recon, no exploitation assistance, no credential storage, no impersonation, no circumvention). **SpiderFoot** not invoked (`authorized-targets.yaml` empty per established state).

Sentinel tombstone non-promotable per established precedent. No post-sweep Discord notification.
