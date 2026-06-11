---
raw_id: raw-2026-06-11-flash-0600-000
collected_at: 2026-06-11T06:05:00-04:00
run_id: flash-sweep-20260611-060000
sweep: flash-2026-06-11-0600
collection_mode: flash_sweep
sentinel: true
flash_candidate: false
source:
  source_yaml_id: sentinel
  source_name: "FLASH sweep sentinel (1 FLASH CANDIDATE — Ivanti Sentry CVE-2026-10520 ITW state transition)"
  source_url: null
  published_at: 2026-06-11T06:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-10520]
  keywords: [ivanti, sentry, shadowserver, itw, mass-exploitation]
triage_tags: [flash_candidate_sweep, candidates_present, quiet_hours, anti_noise_pm_brief_lock_active, anti_noise_am_brief_lock_partial_override, queue_supersession_likely]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: true
promoted_to_finding: finding-2026-06-11-0001-ivanti-sentry-cve-2026-10520-itw-state-transition
promoted_note: "Sentinel companion file to raw-2026-06-11-flash-0600-001; promotion is by reference (the 001 file carries the substantive FLASH candidate content; sentinel records the sweep-level evaluation context)"
promoted_at: 2026-06-11T06:12:00-04:00
ttl_expires_at: 2026-09-09T06:05:00-04:00
---

# FLASH sweep 2026-06-11 06:00 EDT — 1 FLASH CANDIDATE (Ivanti Sentry CVE-2026-10520 ITW state transition)

Window: 00:00 EDT 2026-06-11 → 06:00 EDT 2026-06-11 (6 hours).

## Posture

- **Quiet hours.** 06:00 EDT is OUTSIDE 09:00–21:00 EDT FLASH-eligible window per FLASH-POLICY. Per FLASH-POLICY § "Outside Quiet Hours": FLASH candidates generated this sweep queue to `infrastructure/flash-queue.yaml` for 09:00 catchup-sweep processing.
- **Supersession expected.** Morning brief composition starts 07:30 EDT (pre-brief collection) and ships 08:00 EDT — 1h before quiet-hours queue release. Per FLASH-POLICY queue processing rule: "If superseded by the 08:00 morning brief → mark `superseded: true`, archive." The candidate below is the canonical supersession case: a material state change on a CVE the morning brief already has continuing-coverage authorization for (AM brief 2026-06-10 covered CVE-2026-10520 at disclosure with `no_itw` posture).
- **No critical-override conditions present.** Hard threshold (CVSS 10.0 + ITW + tracked-actor + A&D-watchlist-victim, all four) NOT met. CVE-2026-10520 has CVSS 10.0 + ITW (Shadowserver attestation) but NO tracked-actor attribution + NO A&D-watchlist-victim named. Override fails on prongs 3 + 4. Standard quiet-hours queue path applies.

## Anti-noise locks active at sweep start

- **`triple-kev-sweep-2026-06-10`** — covers CVE-2026-50751 (Check Point VPN/Qilin), CVE-2026-11645 (Chrome V8), CVE-2026-42271 (LiteLLM). Lock expires 2026-06-11T01:25 EDT — **EXPIRED at sweep time** (sweep is at 06:00). Items still locked via AM-brief absorption for CVE-2026-50751 (Check Point FCEB deadline T-0 today) and via raw-signal coverage for the other two.
- **`pan-os-cve-2026-0257-unit42-ir-layer-resurface`** — covers CVE-2026-0257 PAN-OS GlobalProtect Unit 42 IR-layer. Lock expires 2026-06-11T06:00 EDT — **EXPIRED at sweep time** (exactly).
- **AM brief 2026-06-10 anti-noise** — covers Ivanti Sentry CVE-2026-10520/10523 **at disclosure with `no_itw` posture**, Arista EOS CVE-2026-7473 KEV no-patch, ServiceNow API exploitation, RoguePlanet/Nightmare-Eclipse Defender LPE, Patch Tuesday three zero-days (YellowKey/GreenPlasma/MiniPlasma), Microsoft 72-repos Shai-Hulud/Miasma family (VT-006). **Material state change on CVE-2026-10520 (ITW emergence) creates partial-override candidate — see Trigger 1 analysis below.**
- **PM brief 2026-06-10 anti-noise** — covers Veeam CVE-2026-44963, Cyera protobufjs proto6 six-CVE cluster, ShinyHunters Oracle PeopleSoft mass campaign (Nottingham University, education sector, per-actor scope), Adobe ColdFusion + Acrobat / Fortinet FortiSandbox / four SAP NetWeaver criticals, Lumen JDY botnet → Volt Typhoon hedged-associative, ServiceNow AM-006 extension, VT-008 Exchange CVE-2026-42897 GA patch, "The Gentlemen" RaaS Krebs OSINT attribution.
- **`jdy-volt-typhoon-restatement-2026-06-10`** — covers Lumen JDY → Volt Typhoon hedged-associative. Lock expires 2026-06-11T16:00 EDT.
- **`miasma-source-code-leak-2026-06-10`** — covers BleepingComputer Miasma worm source-code GitHub leak event. Operates as candidate-lock until 2026-06-11 morning brief composition.
- **`cve-2026-5027-langflow-patched-2026-06-10`** — covers Langflow path-traversal RCE (CVSS 8.8; patched). Operates as candidate-lock until 2026-06-11 morning brief composition.

## Sources queried (this sweep)

**A-grade direct:**
- **CISA Advisories all.xml** — 0 items in 6h window (feed reachable, 200 OK, ETag/last-modified unchanged, no new advisories since pre-window).
- **CISA KEV JSON catalog** — direct retrieval; **0 entries dated 2026-06-10 OR 2026-06-11.** Most recent dateAdded values: 2026-06-09 (3 entries: CVE-2026-11645, CVE-2026-7473, CVE-2026-20245); 2026-06-08 (CVE-2026-42271, CVE-2026-50751). CVE-2026-10520 / 10523 **NOT in CISA KEV as of this sweep** (despite ITW emergence — KEV lag-time is typical; expect addition within 24-72h per historical pattern).
- **Microsoft Security Blog feed** — 0 items in 6h window.
- **Mandiant / Google Threat Intel feed** — `cloud.google.com/blog/topics/threat-intelligence/rss` parse-error pattern persists (consistent with stale flag; alt-endpoint canonical-swap decision still overdue).
- **MSRC blog feed** — stale per source-health.yaml (parse error pattern since 2026-05-29); not retried.
- **Unit 42 feed** — 0 items in 6h window (last-modified 2026-06-09T22:00 UTC pre-window; healthy).
- **CrowdStrike blog feed** — 10 items returned all dateless (marketing/MQ pattern persistent — three threat-research items in feed but all are continuing-coverage of items already absorbed: Tech Threat Landscape Report annual marketing, June Patch Tuesday restatement, OpenID/IDPro product news). **No new in-window APT research.**
- **Volexity blog feed** — `volexity.com/blog/feed/` parse error at line 17 col 68 (not well-formed, invalid token). **Second consecutive observation** — failure_count increment 1→2 warranted per source-health.yaml runtime rules.
- **Rapid7 blog feed** — 0 items in 6h window.
- **SentinelLabs feed** — 0 items in 6h window.

**B-grade aggregators:**
- **BleepingComputer RSS** — **3 items in 6h window** (broke publication drought from overnight sweep):
  1. "Microsoft fixes BitLocker recovery bug on Windows Server 2025" (2026-06-11T08:44 UTC = 04:44 EDT in-window) — vendor-side fix for non-security operational issue; not threat content. **No FLASH-trigger eligibility.**
  2. "Nottingham University data breach affects over 450,000 students" (2026-06-11T07:27 UTC = 03:27 EDT in-window) — Nottingham confirmation + scale specifics (454,600 affected per HIBP analysis; ethnicities + disabilities + passport numbers exposed); follow-up to already-absorbed ShinyHunters Oracle PeopleSoft PM-brief item. No new attribution, no A&D victim, no IOC. **Anti-noise PM brief lock excludes; restatement framing applies.**
  3. **"Max severity Ivanti Sentry vulnerability now exploited in attacks"** (2026-06-11T06:20 UTC = 02:20 EDT in-window) — **MATERIAL STATE CHANGE: PoC-only → mass ITW exploitation** within ~24h of patch release. Shadowserver attests: "We are observing a large amount of Ivanti Sentry CVE-2026-10520 exploitation attempts based on the public PoC today." Shadowserver further detected 19 vulnerable Internet-exposed instances with "at least 2 backdoored" confirmed. Help Net Security parallel relay (independent B-grade) carries Shadowserver's same attestation: "Shadowserver Foundation has observed a large amount of Ivanti Sentry CVE-2026-10520 exploitation attempts based on the public PoC by watchTowr... at least two of 19 vulnerable instances backdoored." **This is the FLASH candidate. Detail in trigger-1 analysis below.**
- **The Hacker News (feedburner)** — 1 item in 6h window: "GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks" (2026-06-11T06:23 UTC = 02:23 EDT in-window). Vendor-side platform policy announcement (npm v12 install-scripts-off-by-default); not threat content; no actor attribution, no CVE, no A&D entity. **No FLASH-trigger eligibility.** Defensive/policy-positive context for VT-006 / Shai-Hulud / Miasma theme — continuing-coverage candidate for weekly synthesis only.
- **SecurityWeek RSS** — 3 items in 6h window:
  1. "'GreatXML' Zero-Day Exploit Bypasses BitLocker" (2026-06-11T09:56 UTC = 05:56 EDT in-window, 4 minutes before sweep close). Same Nightmare-Eclipse / Chaotic Eclipse researcher (per Categories tag `Chaotic Eclipse`) — public PoC, no ITW, **physical access + previous Defender offline scan precondition**. Continuing-coverage of the researcher's `nightmare_eclipse_researcher_series_continuing_coverage` campaign already in AM brief 2026-06-10's `related_campaigns`. **See trigger-6 analysis below.**
  2. "University of Nottingham Confirms Breach After Hackers Leak Data" (2026-06-11T08:30 UTC = 04:30 EDT in-window) — duplicate of BleepingComputer item #2 above; ShinyHunters credit + 450k+ email addresses leaked. **Anti-noise PM brief lock excludes.**
  3. "Microsoft Patches Exploited Exchange Server Vulnerability" (2026-06-11T06:52 UTC = 02:52 EDT in-window) — follow-up/recap of CVE-2026-42897 (VT-008 GA patch shipped 2026-06-09); contextual note that no Exchange CVEs were added to KEV in 2025 and only this one in 2026; **NO new attribution, NO new victim, NO new IOC**. **Anti-noise PM brief lock excludes.**
- **The Record (Recorded Future News)** — 0 items in 6h window (feed reachable, items_after_since_filter=0).
- **Krebs on Security** — 0 items in 6h window (last-modified 2026-06-10T15:55 UTC pre-window).

**First-party Splunk (24h window per FLASH-POLICY trigger-3 spec):**
- `archimedes` + `defenseclaw_local` indexes — `-24h@h` window. Roster-actor + active-CVE queries executed (Volt Typhoon / Salt Typhoon / Scattered Spider / LockBit / Cl0p / MuddyWater / Charming Kitten / UNC1549 / APT28/29/34/37/40/41 / TeamPCP / Lazarus / Stardust Chollima / Sandworm / Handala / Miyako / BlackCat / ShinyHunters / Qilin / GlassWorm; CVE-2026-50751 / 11645 / 42271 / 0257 / 10520 / 10523 / 7473 / 42897 / 44963 / 5027 / 20245; keywords langflow, veeam, servicenow, protobufjs, peoplesoft, jdy, ivanti, sentry, miasma).
- **16 events returned, all Archimedes self-instrumentation** (`archimedes:scheduler` sourcetype): six `started`/`completed` pairs for 2026-06-10 06:00 / 07:30 / 08:00 / 12:00 / 15:30 / 16:00 / 18:00 phases + 2026-06-11 00:00 / 06:00 phase starts. Zero substantive first-party matches on roster actors, tracked CVEs, or PM-brief IOCs across either index in window. **Hard Rule 8: silence is not disconfirming, not confirming.**

## Triggers evaluated

### Trigger 1 — Critical CVE (CVSS ≥ 9.0) + active exploitation + A-grade source

**1 FIRE.**

**CVE-2026-10520 Ivanti Sentry OS command injection RCE — PoC-only → mass ITW exploitation state transition.**

**Trigger 1 conditions:**
- ✅ **CVSS ≥ 9.0** — **CVSS 10.0** (pre-auth root-level RCE, OS command injection). watchTowr 2026-06-10 technical analysis confirms CVSS 10/10 verbatim: "CVE-2026-10520 (we know, it's catchy) gets full Secure-by-Design points with a CVSS score of 10/10 - just as you'd expect for a Pre-Authenticated Command Injection." Help Net Security parallel relay carries same.
- ✅ **Confirmed active exploitation (not PoC, not theoretical)** — Shadowserver attests **mass ITW exploitation attempts based on the public PoC + at least 2 of 19 vulnerable instances backdoored confirmed**, with remaining unpatched instances "most likely compromised." Quote-discipline (Hard Rule 6, < 15 words, single quote): Shadowserver — "Observing a large amount of Ivanti Sentry CVE-2026-10520 exploitation attempts based on the public PoC today." Help Net Security update added 2026-06-11: "Shadowserver Foundation has observed a large amount of Ivanti Sentry CVE-2026-10520 exploitation attempts based on the public PoC by watchTowr."
- ✅ **A-grade source** — Shadowserver Foundation is procedurally A-grade as scanning-telemetry attestation source (peer class to GreyNoise scanning attestations and Sysdig 2026-05-14 mass-scanner observation pattern). Citation path: Shadowserver (originating A-grade scanning telemetry) → BleepingComputer (B-grade independent relay) + Help Net Security (B-grade independent relay), TWO independent B-grade relays both surfacing the SAME Shadowserver attestation = sufficient corroboration. watchTowr (A-grade IR / vulnerability research; provisional A precedent class, validated separately on PCJack 2026-05-07 lineage and node-ipc 2026-05-14 cluster lineage) is the originating PoC publisher cited verbatim by Shadowserver. **Single-source veto NOT applicable**: Shadowserver's attestation is independent of watchTowr's PoC publication — PoC + scanning telemetry attesting weaponized use of PoC = layered evidence, not single-origin attestation.

**Anti-noise rule 1 evaluation:**

The AM brief 2026-06-10 covered CVE-2026-10520 in `finding-2026-06-10-0003` at **disclosure posture with `no_itw` framing** (file name pattern `...-patched-no-itw.md` confirms). The state-change at this sweep is a **material superseding fact**: PoC-only at AM brief composition → mass ITW exploitation observed 26h later. Per FLASH-POLICY anti-noise rule 1: "If the same CVE or campaign triggers multiple sweeps, only the first FLASH ships. Subsequent triggers get absorbed into the next scheduled brief with an UPDATE flag." The state change is the SECOND trigger (first was AM brief absorption at disclosure); this trigger should absorb into morning brief 2026-06-11 with UPDATE flag.

**Anti-noise rule 2: B2 minimum grade.** Layered evidence Shadowserver (A) + BleepingComputer (B) + Help Net Security (B) + watchTowr (A) easily clears B2 minimum.

**Anti-noise rule 3: Red-team mandatory if WEP ≥ very_likely.** Mass ITW exploitation attested by named-source-of-telemetry (Shadowserver) within 24h of public PoC publication on a CVSS 10.0 pre-auth root RCE on an Internet-exposed security gateway product places WEP at "very_likely" or higher on the FORWARD-LOOKING claim ("attackers will continue mass-exploiting unpatched Sentry"). Red-team review applies.

**Quiet-hours routing:**

06:00 EDT is OUTSIDE 09:00–21:00 EDT FLASH-eligible window. Per FLASH-POLICY § "Outside Quiet Hours":
1. Generate FLASH candidate raw-signal (this file's companion `raw-2026-06-11-flash-0600-001-...`).
2. Queue to `infrastructure/flash-queue.yaml` with:
   - `queued_at: 2026-06-11T06:05:00-04:00`
   - `brief_id: flash-2026-06-11-0605`
   - `trigger: trigger-1-cve`
   - `expires_at: 2026-06-11T18:05:00-04:00` (queue time + 12h staleness window)
   - `superseded: false`
3. At 09:00 catchup-sweep processing:
   - **Expected disposition: `superseded_by_morning_brief`** — the 08:00 morning brief ships 1h before 09:00 catchup and is the natural home for the UPDATE flag absorbing this state change. Morning brief composer should include CVE-2026-10520 UPDATE in Active Threats section: AM brief's `finding-2026-06-10-0003` state transitions from `patched-no-itw` to `patched-itw-observed` with Shadowserver attestation source layer, 19 vulnerable + 2 confirmed backdoored, scanner-leveraging-public-PoC.

**Disposition: FLASH CANDIDATE → QUEUE → EXPECTED SUPERSESSION BY 2026-06-11 MORNING BRIEF.**

**Companion raw-signal file:** `raw-2026-06-11-flash-0600-001-bleepingcomputer-helpnetsecurity-shadowserver-ivanti-sentry-cve-2026-10520-itw-state-transition.md` (separate write with full article text + IOC extraction).

### Trigger 2 — New attribution for tracked actor (not restatement)

**0 FIRE.**

**Evaluated and ruled out:**

- **ShinyHunters Nottingham follow-up** — BleepingComputer + SecurityWeek both surface the Nottingham confirmation (454,600 affected; ethnicities + disabilities + passport numbers exposed). ShinyHunters NOT on roster (verified against 22-actor _roster.yaml: TeamPCP/Stardust Chollima/Lazarus/UNC1549/GlassWorm/APT28/Sandworm/Volt Typhoon/APT29/Salt Typhoon/Charming Kitten/Miyako/Scattered Spider/Handala/LockBit/REvil/APT40/Cl0p/APT41/BlackCat-ALPHV/Payouts King/MuddyWater/APT34/APT37). Already absorbed into PM brief 2026-06-10 as `finding-2026-06-10-0010` per Splunk findings_referenced. **Fails trigger-2 on tracked-actor prong.** **Anti-noise PM brief lock excludes.** Continuing-coverage UPDATE candidate for 2026-06-11 morning brief if attacker infrastructure pivot or A&D-sector victim surfaces (neither present in window).
- **CVE-2026-10520 Ivanti Sentry ITW transition** — Shadowserver attests scanning + backdoor activity but does NOT name an attributed threat actor (Hard Rule 2 preserved). BleepingComputer + Help Net Security + watchTowr all silent on attribution. **Fails trigger-2 on `attributable_actor in _roster.yaml` prong** (no attribution at all). Trigger 1 fires; trigger 2 does not.
- **No other in-window publication attributes activity to a roster actor.**

### Trigger 3 — First-party Splunk IOC hit (tracked IOC, last 24h)

**0 FIRE.** Splunk queries across `archimedes` + `defenseclaw_local` returned **only Archimedes self-instrumentation events** (16 scheduler events for the 2026-06-10 phase cycle + 2026-06-11 00:00 / 06:00 phase starts). Zero substantive first-party matches on roster actor names, active CVEs, or PM-brief IOCs across either index in window. **Hard Rule 8: silence is not disconfirming, not confirming.**

### Trigger 4 — Tracked actor TTP change (A/B-grade, attributable, new tooling/targeting/infra)

**0 FIRE.**

- CVE-2026-10520 Ivanti Sentry ITW transition: not attributable to roster actor (Shadowserver silent on attribution).
- ShinyHunters Nottingham follow-up: not on roster.
- GreatXML / Nightmare-Eclipse BitLocker bypass: same researcher (NOT a threat actor) continuing zero-day series; no operator attribution; not attributable to roster actor.
- No other A/B-grade publication in window documents a roster actor's new tooling/targeting/infrastructure.

### Trigger 5 — Active A&D-sector campaign (multi-victim, named A&D entity)

**0 FIRE.** No A&D-prime victim named in any in-window publication.

- CVE-2026-10520 Ivanti Sentry: Shadowserver scanning telemetry generic (19 vulnerable instances, geographic distribution not published in B-grade relays); no A&D-prime named victim. **Note:** Ivanti Sentry is widely deployed in defense / government / Tier-1 A&D supplier environments as MDM-gateway product (historical 2025 Sentry CVE exploitations included reported federal-agency victims per BleepingComputer context). Structural A&D-prime exposure is non-trivial but no NAMED A&D victim surfaces in window. **Fails trigger-5 on `targets_include_aerospace_defense_or_watchlist_entity` prong on named-victim standard.**
- ShinyHunters Nottingham: education sector (university); not A&D.
- GreatXML BitLocker: no campaign / no victims (PoC drop).
- No nation-state campaign disclosure naming A&D-watchlist entity in window.

### Trigger 6 — Zero-day without patch (CVSS ≥ 8.0 or wide deployment) + exploitation confirmed/imminent

**0 FIRE.**

**Evaluated and ruled out:**

- **GreatXML BitLocker bypass (Chaotic Eclipse / Nightmare-Eclipse)** — SecurityWeek 2026-06-11T09:56 UTC. PoC published on GitHub; same researcher (NOT a threat actor — researcher handle/cluster) who dropped RoguePlanet 2026-06-10 (already absorbed into AM brief `nightmare_eclipse_researcher_series_continuing_coverage`). **Conditions evaluated:**
  - `vulnerability_disclosed_without_patch == true` — TRUE (no patch shipped at sweep time; Microsoft Defender offline-scan attack surface; not in June Patch Tuesday cluster).
  - `cvss_score >= 8.0 OR product_is_widely_deployed` — Product widely deployed (Windows + Defender), so qualifying on second prong. No CVE assigned at sweep time → no CVSS published.
  - `exploitation_confirmed OR exploitation_imminent per A-grade` — **FAILS.** SecurityWeek (B-grade) reports public PoC but no ITW. No A-grade source attests ITW. Attack preconditions are **physical access** (reboot into Recovery Mode via Shift+Restart) + **previous Defender offline scan must have run at least once on the target system**. Physical-access precondition substantially limits "imminent exploitation" plausibility for mass-exploitation framing — this is a targeted-physical-access surface (think evil-maid / nation-state targeted intrusion), not a remote-internet-facing mass-exploit surface. **A-grade source attestation of "exploitation imminent" not present.**
  - **Continuing-coverage absorption:** AM brief 2026-06-10's `related_campaigns: nightmare_eclipse_researcher_series_continuing_coverage` AND `watch_signals_set: nightmare_eclipse_july_14_predicted_next_zero_day_drop_window` already authorize morning brief 2026-06-11 to absorb GreatXML as new entry in researcher series. **Disposition: strong morning-brief candidate** as continuing-coverage (`nightmare_eclipse_researcher_series_continuing_coverage` campaign UPDATE adding GreatXML to the series tally — researcher's 6th-7th zero-day depending on count basis; six per Barracuda May 2026 framing).
  - **Fails trigger-6 on `exploitation_confirmed OR exploitation_imminent per A-grade` prong.**
- **CVE-2026-10520 Ivanti Sentry** — already patched (Ivanti R10.5.2 / R10.6.2 / R10.7.1 shipped 2026-06-10); fails trigger-6 on `no patch` prong. Trigger 1 is the correct evaluation path.
- **CVE-2026-5027 Langflow** — already locked out by `cve-2026-5027-langflow-patched-2026-06-10` candidate-lock; CVSS 8.8 fails trigger-1 threshold; patch shipped fails trigger-6 no-patch prong; strong morning-brief candidate retained.
- **Miasma worm source-code leak** — already locked out by `miasma-source-code-leak-2026-06-10` candidate-lock; not a vulnerability disclosure; supply-chain attack-tooling proliferation event. Not eligible for trigger-6.
- **No other in-window publication discloses a zero-day vulnerability without a patch.**

## Items also evaluated, no trigger match

- **Microsoft fixes BitLocker recovery bug on Windows Server 2025** (BleepingComputer 2026-06-11T08:44 UTC) — vendor-side fix for non-security operational issue (April 2026 security update caused some Windows Server 2025 devices to boot into BitLocker recovery; this is the operational regression-fix, not a CVE). Not threat content; no FLASH-trigger eligibility. Confused-headline risk: this is NOT a BitLocker bypass / not related to YellowKey / GreenPlasma / MiniPlasma / GreatXML / bitskrieg — it's a recovery-boot regression fix.
- **GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks** (THN 2026-06-11T06:23 UTC) — vendor platform policy announcement (npm v12, install-scripts-off-by-default); defensive/policy-positive context for VT-006 / Shai-Hulud / Miasma theme; no actor attribution, no CVE, no A&D entity, no campaign. Already noted in 18:00 sweep (raw-2026-06-10-flash-1800-000 reported BleepingComputer counterpart at 2026-06-10T19:41 UTC). **No FLASH-trigger eligibility.** Continuing-coverage candidate for weekly synthesis or morning brief's standing "supply-chain defensive context" section.
- **Microsoft Patches Exploited Exchange Server Vulnerability** (SecurityWeek 2026-06-11T06:52 UTC) — follow-up/recap of CVE-2026-42897 (VT-008) shipping GA patch 2026-06-09; absorbed into PM brief 2026-06-10. Contextual color (no Exchange CVEs in KEV in 2025, only this one in 2026 so far) but no new attribution / no new victim / no new IOC. **Anti-noise PM brief lock excludes.**
- **University of Nottingham Confirms Breach After Hackers Leak Data** (SecurityWeek 2026-06-11T08:30 UTC) — duplicate of BleepingComputer Nottingham item; ShinyHunters credit. **Anti-noise PM brief lock excludes.**
- **Nottingham University data breach affects over 450,000 students** (BleepingComputer 2026-06-11T07:27 UTC) — same as above; PM brief lock excludes; scale specifics (454,600 / passport+ethnicities+disabilities) are noteworthy as ShinyHunters-campaign continuing-coverage UPDATE candidate for morning brief but not FLASH-trigger eligible.

## Source-health observations

- **All A-grade direct sources reachable** except Mandiant (persistent parse error — alt-endpoint canonical-swap decision overdue across last 7+ sweeps) and MSRC (stale since 2026-05-30).
- **Volexity blog feed parse error** — SECOND consecutive observation (line 17 col 68 not well-formed). **failure_count increment 1→2 warranted** per source-health.yaml runtime rules. Approaching stale flag threshold (per "failure_count ≥ 2 → status: stale" rule). Recommend operator review whether Volexity blog feed schema has changed or RSS endpoint deprecated. **Updating source-health.yaml `volexity` entry: failure_count: 1 → 2, status: stale, stale_since: 2026-06-11, last_error: "parse error line 17 col 68 not well-formed invalid token (2nd consecutive)", preserve `notes:` operator-set field per Session 11 codified rule.**
- **CrowdStrike feed continues dateless marketing-pattern publication** — no topical APT research in window across 06:00 / 12:00 / 18:00 / 00:00 / 06:00 sweeps (5 consecutive). **Failure-count increment NOT applied** — feed is reachable, 200 OK, ETag returned, content is just non-research; this is publication-cadence, not source-health failure.
- **BleepingComputer + THN + SecurityWeek publication drought broken** — overnight drought (00:00 sweep) cleared by 06:00 EDT publication burst (3 / 1 / 3 in-window items respectively). Feeds healthy. Quiet-hours overnight slowdown was structural, not a feed-failure pattern.
- **No 403/429/auth-error events this sweep** across queried sources.

## Decision summary

**1 FLASH CANDIDATE FIRES. Quiet hours apply — queue to flash-queue.yaml. Expected supersession by 2026-06-11 morning brief.**

**Drivers for trigger-1 fire on CVE-2026-10520:**
1. **CVSS 10.0** pre-auth root RCE on widely-deployed Internet-exposed security gateway product (Ivanti Sentry; MDM gateway; historical 2025 federal-agency-victim pattern per BleepingComputer).
2. **PoC-only → mass ITW exploitation state transition** within ~24h of patch release. Shadowserver attests "large amount of exploitation attempts" + "at least 2 of 19 vulnerable instances backdoored" + remaining unpatched "most likely compromised."
3. **A-grade source attestation** layered: Shadowserver (originating telemetry, A-grade scanning-attestation source) → BleepingComputer (B independent relay) + Help Net Security (B independent relay) + watchTowr (A originating PoC publisher).
4. **Material superseding fact** vs AM brief 2026-06-10's `finding-2026-06-10-0003` `no_itw` posture. This is canonical PoC-weaponization-to-mass-exploitation pattern.

**Drivers for quiet-hours queue routing (not immediate post):**
1. 06:00 EDT outside 09:00–21:00 active hours per FLASH-POLICY.
2. No critical-override conditions met (CVSS 10.0 ✅ + ITW ✅ + tracked-actor ❌ + A&D-watchlist-victim ❌). Override fails on prongs 3 + 4. Standard quiet-hours queue path applies.
3. 08:00 morning brief composition (07:30 pre-brief + 08:00 publication) is the natural supersession point — morning brief composer can absorb as UPDATE flag on `finding-2026-06-10-0003` state transition without parallel FLASH ship.

**Six in-window items ruled out:**
1. Nottingham confirmation BleepingComputer + SecurityWeek (×2 items) — PM-brief-locked; ShinyHunters not on roster; education sector not A&D.
2. Microsoft Exchange CVE-2026-42897 SecurityWeek follow-up — PM-brief-locked; restatement of GA patch already absorbed.
3. Microsoft Server 2025 BitLocker recovery boot fix — operational regression-fix, not security; confused-headline risk.
4. GitHub npm v12 install-scripts-off-by-default (BleepingComputer + THN, ×2) — vendor platform policy announcement; defensive/positive context.
5. GreatXML BitLocker bypass SecurityWeek (Chaotic Eclipse / Nightmare-Eclipse) — same researcher continuing series; physical-access + Defender-offline-scan precondition; PoC public, no ITW, no A-grade ITW/imminence attestation; AM brief continuing-coverage authorization absorbs at morning brief.
6. CISA BOD 26-04 carryover (already 18:00 ruled out; no new in-window publication this sweep).

**Three carry-forward candidates from 18:00/00:00 sweeps retained for 2026-06-11 morning brief composition:**
1. **CVE-2026-5027 Langflow** — strong morning-brief candidate.
2. **Miasma worm source-code leak** — strong morning-brief candidate; VT-006 / TeamPCP continuing-coverage.
3. **CVE-2026-20245 Cisco Catalyst SD-WAN KEV-add** — continuing-coverage; profile dir exists.

**Plus four new carry-forward candidates from this sweep:**
4. **CVE-2026-10520 Ivanti Sentry ITW state transition** — FLASH candidate queued, expected morning-brief supersession.
5. **GreatXML BitLocker bypass (Chaotic Eclipse)** — continuing-coverage UPDATE on `nightmare_eclipse_researcher_series_continuing_coverage` campaign.
6. **Nottingham ShinyHunters confirmation + 454,600 scale** — continuing-coverage UPDATE on PM brief's ShinyHunters Oracle PeopleSoft item.
7. **GitHub npm v12 install-scripts-off-by-default** — defensive/policy context for VT-006 / Shai-Hulud / Miasma theme; morning brief standing-section candidate.

## Audit trail handoff

Librarian: log `flash_sweep_completed` (or `flash_evaluation`) event to Splunk with:
- `candidates_count: 1` (CVE-2026-10520 Ivanti Sentry ITW state transition)
- `triggers_fired: [trigger-1-cve]`
- `ruled_out_count: 6` (Nottingham BC / Nottingham SW / Exchange SW follow-up / Server 2025 BitLocker recovery-boot / GitHub npm v12 BC + THN / GreatXML SW)
- `sweep_window: flash-0600`
- `quiet_hours_at_sweep: true`
- `active_hours_eligible: false`
- `queue_routing: true`
- `expected_supersession: 2026-06-11-morning_brief`
- `sources_queried: 14` (CISA Advisories, CISA KEV JSON, Microsoft Security Blog, Mandiant [parse-error], MSRC [stale-skip], Unit 42, CrowdStrike, Volexity [parse-error 2nd], Rapid7, SentinelLabs, BleepingComputer, THN, SecurityWeek, The Record, Krebs — 15 attempted, 13 healthy, 2 parse-error)
- `sources_skipped_stale: 1` (MSRC; Volexity now also stale at 2nd consecutive parse-error → 2 stale-skips next sweep)
- `source_health_changes: [volexity failure_count 1→2, status: stale, stale_since: 2026-06-11]`
- `first_party_splunk_substantive_hits: 0`
- `anti_noise_locks_honored: [am-brief-2026-06-10_partial_override_on_cve-2026-10520_state_change, pm-brief-2026-06-10, jdy-volt-typhoon-restatement-2026-06-10, miasma-source-code-leak-2026-06-10, cve-2026-5027-langflow-patched-2026-06-10]`
- `anti_noise_locks_expired_at_sweep: [triple-kev-sweep-2026-06-10 (expired 01:25 EDT), pan-os-cve-2026-0257-unit42-ir-layer-resurface (expired 06:00 EDT exactly)]`

Companion raw-signal file for the FLASH candidate itself: `raw-2026-06-11-flash-0600-001-bleepingcomputer-helpnetsecurity-shadowserver-ivanti-sentry-cve-2026-10520-itw-state-transition.md`.

Queue the FLASH candidate to `infrastructure/flash-queue.yaml` per FLASH-POLICY § "Outside Quiet Hours" with `brief_id: flash-2026-06-11-0605`, `trigger: trigger-1-cve`, `expires_at: 2026-06-11T18:05:00-04:00`, `superseded: false`. The 09:00 catchup-sweep will evaluate supersession by the 08:00 morning brief (expected: superseded_by_morning_brief; morning brief composer should include CVE-2026-10520 UPDATE in Active Threats absorbing state transition with Shadowserver attestation source layer).

Update `source-health.yaml` for `volexity` entry (failure_count: 1 → 2, status: stale, stale_since: 2026-06-11, last_error: "parse error line 17 col 68 not well-formed invalid token (2nd consecutive)", preserve `notes:` operator-set field per Session 11 codified rule).
