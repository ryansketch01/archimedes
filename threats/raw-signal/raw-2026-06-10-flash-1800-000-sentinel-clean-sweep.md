---
raw_id: raw-2026-06-10-flash-1800-000
collected_at: 2026-06-10T18:05:00-04:00
run_id: flash-sweep-20260610-180000
sweep: flash-2026-06-10-1800
collection_mode: flash_sweep
sentinel: true
flash_candidate: false
source:
  source_yaml_id: sentinel
  source_name: "FLASH sweep sentinel (NO TRIGGERS — clean sweep)"
  source_url: null
  published_at: 2026-06-10T18:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_candidate_sweep, clean_sweep, no_triggers, active_hours, anti_noise_pm_brief_lock_active, anti_noise_jdy_volt_typhoon_lock_active, anti_noise_triple_kev_lock_active]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-09-08T18:05:00-04:00
---

# FLASH sweep 2026-06-10 18:00 EDT — NO TRIGGERS (clean sweep; 8 items evaluated and ruled out)

Window: 12:00 EDT 2026-06-10 → 18:00 EDT 2026-06-10 (6 hours).

## Posture

- **Active hours.** 18:00 EDT is INSIDE 09:00–21:00 EDT FLASH-eligible window per FLASH-POLICY. Any candidate produced would compose immediately and ship to `#flash-alerts` (no quiet-hours queue).
- **No critical-override conditions present.** Hard threshold (CVSS 10.0 + ITW + tracked-actor + A&D-watchlist-victim, all four) not met on any in-window item.

## Anti-noise locks active at sweep start

- **`triple-kev-sweep-2026-06-10`** — covers CVE-2026-50751 (Check Point VPN/Qilin), CVE-2026-11645 (Chrome V8), CVE-2026-42271 (LiteLLM). Lock expires 2026-06-11T01:25 EDT. Originating: 00:00 FLASH (`flash-2026-06-10-0125`).
- **`pan-os-cve-2026-0257-unit42-ir-layer-resurface`** — covers CVE-2026-0257 PAN-OS GlobalProtect Unit 42 IR-layer. Lock expires 2026-06-11T06:00 EDT.
- **AM brief 2026-06-10 anti-noise** — covers Ivanti Sentry CVE-2026-10520/10523, Arista EOS CVE-2026-7473 KEV no-patch, ServiceNow API exploitation, RoguePlanet/Nightmare-Eclipse Defender LPE, Patch Tuesday three zero-days (CVE-2026-45586/50507/49160), Microsoft 72-repos Shai-Hulud/Miasma family (VT-006).
- **PM brief 2026-06-10 anti-noise** — covers Veeam CVE-2026-44963 (CVSS 9.4), Cyera protobufjs proto6 six-CVE cluster, ShinyHunters Oracle PeopleSoft mass campaign (per-actor scope), Adobe ColdFusion + Acrobat / Fortinet FortiSandbox + four SAP NetWeaver criticals, Lumen JDY botnet at 1,500+ devices (Volt Typhoon "previously linked" — hedged-associative restatement), ServiceNow AM-006 material extension (endpoint named + IPv4 IOC), VT-008 Exchange CVE-2026-42897 GA patch ships, "The Gentlemen" RaaS Krebs OSINT attribution.
- **`jdy-volt-typhoon-restatement-2026-06-10`** — covers Lumen Black Lotus Labs JDY botnet → Volt Typhoon hedged-associative attribution (BleepingComputer + THN relays). Established via 12:00 sweep rule-out + PM brief absorption. Lock expires 2026-06-11T16:00 EDT.

## Sources queried (this sweep)

**A-grade direct:**
- CISA Advisories all.xml — 0 items in 6h window
- CISA KEV JSON catalog — direct retrieval; **0 entries dated 2026-06-10.** Most recent dateAdded values: 2026-06-09 (3 entries, including CVE-2026-11645 Chrome V8 already under triple-KEV lock), 2026-06-08 (2), 2026-06-05 (1), 2026-06-03 (1), 2026-06-02 (2). No new KEV adds in window.
- Microsoft Security Blog feed — 1 item in window: "Turn specs into evals for any agent with ASSERT" (2026-06-10T16:00 UTC) — AI eval framework launch (Mehrnoosh Sameki et al.), product announcement, NOT threat content. No FLASH-trigger eligibility.
- Mandiant feed — cloud.google.com/blog/topics/threat-intelligence/rss returned parse error this sweep (consistent with persistent stale pattern; operator alt-endpoint canonical-swap decision overdue).
- MSRC blog feed — stale per source-health.yaml (parse error pattern since 2026-05-29); not retried.
- Unit 42 feed — 0 items in window (last-modified 2026-06-09T22:00 UTC pre-window).
- CrowdStrike blog feed — 10 items returned all dateless (marketing/MQ pattern persistent — known per source-health); no topical threat-research post in window. Repeated 06:00/12:00-sweep observation that CrowdStrike feed is publishing AI-product / customer-story / MQ-announcement content this week with no APT-research posts.

**B-grade aggregators:**
- BleepingComputer RSS — 4 items in 6h window (all evaluated below).
- The Hacker News (feedburner) — 1 item in 6h window (evaluated below; THN feed has slowed since AM cycle).
- SecurityWeek RSS — 0 items in 6h window. Last-modified 2026-06-10T18:17 UTC = exactly window-start; feed has not refreshed post-window-start. Source remains healthy (feed reachable, 200, ETag returned), just no new publications since the 16:00 afternoon brief composition cutoff.
- The Record — 1 item in 6h window (evaluated below).
- Krebs on Security — 0 items in window.

**First-party Splunk:**
- `archimedes` + `defenseclaw_local` indexes — `-6h` window. Two queries executed:
  1. Roster actor names (Volt/Salt Typhoon, Scattered Spider, LockBit, Cl0p, ShinyHunters, Qilin, MuddyWater, Charming Kitten/Mint Sandstorm, UNC1549/Smoke Sandstorm, APT28/29/34/37/40/41, TeamPCP, Lazarus, Stardust Chollima, Sandworm, Handala/Mango Sandstorm, Miyako, BlackCat/ALPHV, Payouts King, "The Gentlemen").
  2. Active CVEs (CVE-2026-50751/11645/42271/0257/10520/10523/7473/42897/44963/5027/35616) + keywords (langflow/veeam/servicenow/protobufjs/peoplesoft/jdy/coldfusion/netweaver/fortisandbox).
- Returns: only Archimedes self-instrumentation events from the 12:00 FLASH sweep (1 `flash_evaluation` event, commit b96973b) and the 17:02 afternoon-brief librarian publish (1 `brief_published` event for 2026-06-10-afternoon, message_id 1514374308527345745, 11 findings 0007-0017, 13 CVEs in `related_vulns`). **Zero substantive first-party matches** on tracked actors or tracked CVEs across either index in window. **Hard Rule 8: silence is not disconfirming.**

## Triggers evaluated

### Trigger 1 — Critical CVE (CVSS ≥ 9.0) + active exploitation + A-grade source

**0 FIRE.**

**Evaluated and ruled out:**

- **CVE-2026-5027 Langflow path-traversal RCE — BleepingComputer relay** (BleepingComputer 2026-06-10T21:23 UTC, Bill Toulas byline). Updates the 12:00-sweep VulnCheck/THN coverage with material new fact: **the vulnerability IS PATCHED** — langflow-base 0.8.3 (released 2026-03-30) and Langflow application 1.9.0 / 1.10.0 (1.10.0 released on publication date today). 12:00 sweep had ruled out partly on "still unpatched ~75 days later" framing; this BleepingComputer reporting corrects that — patch HAS shipped. Active exploitation per VulnCheck (Caitlin Condon) still attests test-file / recon-class activity on honeypots, NOT weaponized intrusion. CVSS **8.8 (< 9.0)** — fails trigger-1 hard threshold. **Single-source veto applies** on operational exploitation layer (VulnCheck sole originator; BleepingComputer + THN pure B-grade relays). MuddyWater attribution referenced in article is for **CVE-2025-3248 (different CVE, prior surface)** — NOT CVE-2026-5027; no actor attribution for the target CVE. Not in CISA KEV at this sweep (direct catalog retrieval). **Decision: RULE OUT for FLASH** — fails trigger-1 CVSS threshold; fails trigger-6 no-patch prong (patched). **Disposition:** retain as strong morning-brief candidate for 2026-06-11 as net-new AI/orchestration platform CVE with vendor-attested ITW (now-patched), structural-indirect A&D internal-AI-gateway relevance (parallels LiteLLM CVE-2026-42271 + previously-tracked LangChain/internal-AI-gateway theme).
- **Microsoft Exchange CVE-2026-42897 GA patch ships** — already absorbed into 2026-06-10 afternoon brief (per Splunk `brief_published` event, `related_vulns` includes CVE-2026-42897 + finding finding-2026-06-10-0014 VT-008 state transition documented). **Anti-noise PM brief lock excludes.**
- **CVE-2026-44963 Veeam Backup Server RCE (CVSS 9.4)** — already absorbed into afternoon brief. **Anti-noise PM brief lock excludes.**
- **Ivanti Sentry CVE-2026-10520/10523, Arista EOS CVE-2026-7473** — both in 06-10 morning brief. **Anti-noise lock excludes.**

### Trigger 2 — New attribution for tracked actor (not restatement)

**0 FIRE.**

**Evaluated and ruled out:**

- **JDY botnet THN restatement** — THN 2026-06-10T16:08 UTC re-reports Lumen Black Lotus Labs JDY botnet research already covered by BleepingComputer earlier today and absorbed into afternoon brief (`finding-2026-06-10-0013` per Splunk findings_referenced). THN attribution language is **even softer** than BleepingComputer's: "Chinese hacking groups **like** Volt Typhoon" + "China-nexus state-sponsored threat actors" + "first flagged as a cluster within another botnet" + "suspected to be offered by the operators to various hacking outfits." This is hedged-associative ("like" / "suspected") — NOT a direct attribution to Volt Typhoon. The Lumen primary research itself remains characterized as restatement of established patterns ("mirrors prior JDY operations") per the BleepingComputer earlier source. **Anti-noise `jdy-volt-typhoon-restatement-2026-06-10` lock excludes.** **Fails trigger-2 on `attribution_is_new_not_restatement` prong** for the third time in 24h (00:00 / 12:00 / 18:00 sweeps all evaluated and ruled out). **Disposition:** absorbed; no further action.
- **ShinyHunters Oracle PeopleSoft** (BleepingComputer 2026-06-10T18:31 UTC, Lawrence Abrams byline) — substantive new detail in this BleepingComputer follow-up: confirmed victim Nottingham University (education sector), TLS-cert pivot to `azurenetfiles[.]net`, "gadget chain" of old + zero-day exploits attested, SSH brute-force with `psoft` / `oracle` / `linuxadm` accounts, 300+ instances / 100+ organizations. ShinyHunters is **NOT on the 22-actor _roster.yaml** (verified: roster covers TeamPCP/Stardust Chollima/Lazarus/UNC1549/GlassWorm/APT28/Sandworm/Volt Typhoon/APT29/Salt Typhoon/Charming Kitten/Miyako/Scattered Spider/Handala/LockBit/REvil/APT40/Cl0p/APT41/BlackCat-ALPHV/Payouts King/MuddyWater/APT34/APT37). Already absorbed into 2026-06-10 afternoon brief as `finding-2026-06-10-0010` (per Splunk findings_referenced) with per-actor scope. **Anti-noise PM brief lock excludes.** **Fails trigger-2 on tracked-actor prong.** **Fails trigger-5** on A&D-sector prong (education sector, no named A&D-prime victim). **Disposition:** continuing-coverage UPDATE candidate for 2026-06-11 brief if attacker infrastructure pivot or A&D-sector victim subsequently surfaces.
- **Miasma worm source code leak** (BleepingComputer 2026-06-10T20:27 UTC, Bill Toulas byline) — material new event: threat actors deliberately leaked Miasma source code 2026-06-09/10 via "Miasma-Open-Source-Release" repos across multiple compromised GitHub developer accounts (SafeDep researchers attest deliberate, not accidental). Article does NOT attribute the Miasma framework itself to a tracked actor — references prior incidents (Red Hat npm packages, 73 Microsoft GitHub repos) but stops short of naming the operators. Miasma family is **TeamPCP-attributed** per Archimedes corpus (raw-2026-06-10-am-002 + VT-006 lineage; Wiz/Snyk/StepSecurity attribution chain). However: **source code leak ≠ new attribution + ≠ new attack** — no IOCs are published, no confirmed weaponized use in active attack post-leak in this article, no A&D-prime victim. The leak event itself is intelligence-noteworthy (lowers attack-tooling barrier; future supply-chain incidents may abuse the leaked source) but does not in itself meet a FLASH trigger — would require (a) direct TeamPCP attribution of the leak event by an A/B-grade source, OR (b) confirmed weaponized use of leaked source in attack against named A&D victim. Neither present. **Anti-noise AM brief Miasma/Shai-Hulud lock excludes from candidacy** (raw-am-002 covered the 72-repos campaign with TeamPCP attribution + Miasma family designation). **Fails trigger-2 on attribution-event prong** (leak ≠ attribution); **fails trigger-4 on attributable-to-tracked-actor prong** (source does not name TeamPCP at the leak event); **fails trigger-5 on A&D-victim prong**. **Disposition:** strong morning-brief candidate for 2026-06-11 — supply-chain attack-tooling proliferation event with structural-indirect A&D relevance (Tier-1/2 supplier dev-environment exposure). Update continuing-coverage on VT-006 / TeamPCP / Shai-Hulud-family theme.

### Trigger 3 — First-party Splunk IOC hit (tracked IOC, last 24h)

**0 FIRE.** Splunk queries across `archimedes` + `defenseclaw_local` returned only Archimedes self-instrumentation events from the 12:00 FLASH sweep and the 17:02 afternoon-brief librarian publish. Zero substantive first-party matches on roster actor names, active CVEs, or PM-brief IOCs. **Hard Rule 8: silence is not disconfirming, not confirming.**

### Trigger 4 — Tracked actor TTP change (A/B-grade, attributable, new tooling/targeting/infra)

**0 FIRE.**

- JDY/Volt Typhoon: THN restatement of Lumen research framed as "mirrors prior JDY operations" — explicitly restatement, not new TTP. Fails trigger-4.
- Miasma source-code leak: no actor attribution in this BleepingComputer article at the leak event; cannot be attributed to TeamPCP at this surface without source attribution. Fails trigger-4 on `attributable to tracked actor` prong.
- ShinyHunters Oracle PeopleSoft TTP detail (SSH brute-force account list + `azurenetfiles[.]net` pivot + "gadget chain"): ShinyHunters not on roster. Fails trigger-4 on `attributable to tracked actor` prong.
- No other A/B-grade publication in window names a roster actor with new tooling/targeting/infrastructure.

### Trigger 5 — Active A&D-sector campaign (multi-victim, named A&D entity)

**0 FIRE.** No A&D-prime victim named in any in-window publication.

- ShinyHunters Oracle PeopleSoft: Nottingham University named (education sector); "most organizations impacted are in the education sector" per attacker statement. No Lockheed/Boeing/RTX/Northrop/GD/BAE/L3Harris/Leidos/SAIC/Thales/GE Aerospace/Safran/Honeywell/Airbus/Elbit/sub-tier supplier named.
- JDY botnet: "U.S. and Brazil" geographic distribution (compromised SOHO devices, not victim organizations); "U.S. military and associated entities" target framing remains generic (12:00 sweep ruled-out posture holds).
- Miasma source-code leak: no victim named at leak event (only prior incidents Red Hat npm + 73 Microsoft repos referenced).
- No nation-state campaign disclosure naming A&D-watchlist entity in window.

### Trigger 6 — Zero-day without patch (CVSS ≥ 8.0 or wide deployment) + exploitation confirmed/imminent

**0 FIRE.**

- **CVE-2026-5027 Langflow** — BleepingComputer relay confirms **patch shipped** (langflow-base 0.8.3 + Langflow 1.10.0). Was a partial trigger-6 candidate at 12:00 sweep on "still unpatched" framing; that framing is now superseded by BleepingComputer's patch-status confirmation. **Fails trigger-6 on `no patch` prong** (vulnerability IS patched).
- Miasma source-code leak: not a vulnerability disclosure; supply-chain attack-tooling proliferation event. Not eligible for trigger-6.

## Items also evaluated, no trigger match

- **GitHub announces npm security changes to tackle supply-chain attacks** (BleepingComputer 2026-06-10T19:41 UTC) — vendor security-platform announcement (npm v12 release plan); not threat content; no FLASH-trigger eligibility. Defensive/policy-positive context for VT-006 / Shai-Hulud / Miasma theme.
- **Turn specs into evals for any agent with ASSERT** (MSTIC blog 2026-06-10T16:00 UTC) — Microsoft AI eval framework launch (Mehrnoosh Sameki et al.); product announcement; not threat content; no FLASH-trigger eligibility.
- **CISA to require federal agencies to patch some cyber vulnerabilities within 3 days** (The Record 2026-06-10T19:53 UTC) — CISA Binding Operational Directive 26-04 announcement; policy/regulatory news; names no specific CVEs, actors, or A&D entities. Not threat content; no FLASH-trigger eligibility. Weekly-synthesis or policy-context consideration only.

## Source-health observations

- All A-grade direct sources reachable; **no new failures or stale flips this sweep.**
- Mandiant feedburner remains 404 (alt cloud.google.com path returned parse error this sweep) — persistent pattern per source-health.yaml; operator alt-endpoint canonical-swap decision still overdue.
- MSRC blog feed remains stale per 2026-05-29/30 pattern; not retried.
- CrowdStrike feed continues dateless marketing-pattern publication this week; no topical APT research in window across 06:00 / 12:00 / 18:00 sweeps. **Failure-count increment NOT applied** — feed is reachable, 200 OK, ETag returned, content is just non-research; this is publication-cadence, not source-health failure.
- SecurityWeek RSS shows last-modified 2026-06-10T18:17 UTC exactly window-start with 0 in-window items; feed is healthy (reachable, 200, ETag) just slow this evening. **Failure-count increment NOT applied** — single window of slow publication does not indicate stale source.
- No 403/429/auth-error events this sweep across queried sources.

## Decision summary

**NO TRIGGERS FIRE. Clean sweep. Silent exit per FLASH-POLICY.**

Three candidates met partial-trigger thresholds but were ruled out per documented decision rules:

1. **CVE-2026-5027 Langflow** (BleepingComputer relay — partial trigger-1 / partial trigger-6 candidate) — ruled out on CVSS 8.8 < 9.0 hard threshold + patch-shipped supersedes "no patch" prong + single-source veto on operational exploitation layer + MuddyWater attribution is for different CVE (CVE-2025-3248). **Strong morning-brief candidate for 2026-06-11.**
2. **Miasma worm source-code leak** (partial trigger-2 / trigger-4 candidate) — ruled out on `attribution_is_new` prong (source code leak ≠ new actor attribution event; article does not attribute the leak to TeamPCP) + no confirmed weaponized use in attack post-leak + no A&D-prime victim. **Strong morning-brief candidate for 2026-06-11** as VT-006 / TeamPCP / Shai-Hulud-family continuing-coverage on supply-chain attack-tooling proliferation event.
3. **JDY/Volt Typhoon THN restatement** (third evaluation in 24h; trigger-2 / trigger-4 candidate) — ruled out on hedged-associative attribution language ("like Volt Typhoon" / "China-nexus") + explicit restatement framing + already absorbed into PM brief. **Anti-noise lock excludes; no further action.**

The 00:00 FLASH's `triple-kev-sweep-2026-06-10` lock, the 06:00 sweep's PAN-OS `cve-2026-0257-unit42-ir-layer-resurface` lock, the AM brief 2026-06-10 anti-noise lock, the PM brief 2026-06-10 anti-noise lock, and the new `jdy-volt-typhoon-restatement-2026-06-10` lock all held through this sweep. No supersession events. No critical-override evaluation upgraded any item.

## Audit trail handoff

Librarian: log `flash_sweep_completed` (or `flash_evaluation`) event to Splunk with `candidates_count: 0`, `triggers_fired: []`, `ruled_out_count: 8` (CVE-2026-5027 Langflow / Miasma source-code leak / JDY-THN restatement / ShinyHunters PeopleSoft PM-brief absorption / GitHub npm announcement / MSTIC ASSERT / CISA BOD 26-04 / no in-window SecurityWeek items but feed healthy), `sweep_window: flash-1800`, `quiet_hours_at_sweep: false`, `active_hours_eligible: true`. Commit this sentinel raw-signal with a short subject line; no findings/briefs to write.
