---
raw_id: raw-2026-06-15-flash-1200-000-sentinel
collected_at: 2026-06-15T12:10:00-04:00
run_id: flash-sweep-20260615-120000
collection_mode: flash_sweep
source:
  source_yaml_id: internal-sentinel
  source_name: Archimedes Internal Sentinel (FLASH sweep)
  source_url: null
  published_at: 2026-06-15T12:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [sentinel, flash_sweep_with_candidate, active_hours, unc6508_candidate_handoff]
iocs_extracted: false
iocs_count: 0
text_word_count: 1040
promoted: false
ttl_expires_at: 2026-09-13T12:10:00-04:00
---

# 12:00 EDT FLASH sweep — 1 candidate (UNC6508 / Trigger 5), 19-IOC PeopleSoft sentinel clean (10th consecutive)

## Sweep parameters

- **Window:** 2026-06-15 06:00 EDT → 2026-06-15 12:00 EDT (6.0h)
- **Quiet hours:** **INACTIVE** (12:00 EDT is inside 09:00–21:00 EDT active window). FLASH candidates post normally to `#flash-alerts` if grader/red-team chain promotes. Critical override evaluated but does not apply (see Trigger evaluation in raw-2026-06-15-flash-1200-001).
- **Trigger evaluation:** 6 FLASH triggers per `doctrine/FLASH-POLICY.md`
- **Splunk sentinel IOC sets:** 19-IOC standing PeopleSoft/UNC6240 set + 9-IOC ad-hoc UNC6508 set (this sweep, candidate-driven)
- **Splunk indexes queried:** defenseclaw_local, archimedes
- **Splunk lookback:** -24h@h (standing set), -30d@d (new UNC6508 IOCs)

## Results

- **candidates_found:** 1 (raw-2026-06-15-flash-1200-001 — GTIG primary UNC6508 PRC-nexus campaign against North American medical/military health/defense intelligence/AI research/uncrewed-vehicle-systems/cyber-offensive-programs/Indo-Pacific-command, INFINITERED modular backdoor on exposed REDCap servers, Sept 2023–Nov 2025+ 26-month dwell, 13 indicators captured)
- **triggers_fired:** [trigger-5-ad-sector-campaign]
- **Splunk sentinel (standing 19-IOC PeopleSoft/UNC6240 set):** 0 hits across defenseclaw_local + archimedes over -24h. **10th consecutive clean sentinel sweep** across the cumulative window (2026-06-13 18:00 + 2026-06-14 00:00 + 06:00 + 07:30 + 12:00 + 15:30 + 18:00 + 2026-06-15 00:00 + 06:00 + 12:00). Silent Splunk does NOT disconfirm — visibility-limited absence per Hard Rule 8.
- **Splunk sentinel (new UNC6508 9-IOC ad-hoc set):** 0 hits across defenseclaw_local + archimedes over -30d. Silent Splunk does NOT disconfirm — Frank is not a REDCap-running North American medical research institution / military health institution; visibility-limited absence per Hard Rule 8. Sentinel logged as confirmation that the standing IOC set should be **EXPANDED** by the grader to track UNC6508 going forward.
- **CISA KEV:** No net-new entries since 2026-06-12. CISA all.xml feed 200 OK, 30 items, 0 in-window. Five most-recent KEV unchanged from prior sweeps (CVE-2026-35273 PeopleSoft due **TONIGHT EOD Sunday 2026-06-15 ~T-12h**, CVE-2026-10520 Ivanti Sentry past 2026-06-14, CVE-2026-11645 Chrome V8 due 2026-06-23, CVE-2026-7473 Arista EOS due 2026-06-23, CVE-2026-20245 Cisco Catalyst SD-WAN due 2026-06-23).

## Sources queried + status

| source_yaml_id | status | in-window items |
|---|---|---|
| bleepingcomputer | 200 OK, last_modified Mon 15 Jun 16:01 GMT | 6 (FBI crypto-scam couriers, Vibe coders Tines marketing, **Chinese hackers REDCap UNC6508 InfiniteRed** ← Relay 2 for UNC6508 FLASH candidate, M365 Copilot SearchLeak Varonis, Infinite Campus ShinyHunters 137K K-12 staff, AI phishing webinar marketing) |
| thehackernews | 200 OK, last_modified Mon 15 Jun 15:49 GMT | 4 (M365 Copilot SearchLeak Varonis recap, weekly recap dateless, onboarding password marketing, 152 Chrome wallpaper extensions PUP) |
| securityweek | 200 OK, last_modified Mon 15 Jun 16:01 GMT | 7 (Mackay Sugar / The Gentlemen — anti-noise hold, **Chinese hackers UNC6508 Medical Military AI Research** ← Relay 1 for UNC6508 FLASH candidate, NewCore $66M funding marketing, Ukrainian Conti Lytvynenko plea — same as 2026-06-14 reject 0001, Novo Nordisk — same as 2026-06-15 reject 0001, French Tchap Misere — anti-noise hold finding-2026-06-15-0002, ShinyHunters Council of Europe — anti-noise hold finding-2026-06-15-0001) |
| securityaffairs | 200 OK, last_modified Mon 15 Jun 13:13 GMT | 2 (Novo Nordisk — already rejected 2026-06-15-0001, PAN-OS CVE-2026-0257 — anti-noise hold finding-2026-06-15-0004) |
| the-record | 200 OK | 3 (Russian Astral cyberattack disrupts business/gov — out of A&D scope adversary-side infrastructure, Finland cargo ship undersea cable charges — physical-incident not cyber FLASH, **Anthropic Fable 5 / Mythos 5 USG disable** ← anti-noise hold carry-forward) |
| helpnetsecurity | 200 OK, last_modified Mon 15 Jun 15:28 GMT | 10 (**Velvet Ant Sygnia backdoored auth stack 10-year dwell** ← anti-noise hold finding-2026-06-12-0004 4th-publisher relay no net-new substrate, Delinea+Cyera marketing, 1Password Credential Broker marketing, Trust3 AgentDOS marketing, Omada Agent Gov marketing, Ukrainian Conti Lytvynenko — already rejected, Red Sift GlobalSign marketing, AI vuln discovery 66K CVEs FIRST forecast research, PhishLumos research, Modat Passive DNS marketing) |
| crowdstrike | 200 OK, last_modified Mon 15 Jun 05:36 GMT | 0 (10 dateless marketing/MQ/Patch Tuesday recap items — pattern continues from 06:00 sweep) |
| unit42 | 200 OK, last_modified Fri 12 Jun 22:00 GMT pre-window | 0 |
| mstic | not re-attempted (under-24h skip rule; healthy at last successful 2026-06-12) | n/a |
| cisco-talos (feedburner) | 200 OK, last_modified Fri 12 Jun 11:48 GMT pre-window | 0 |
| krebs | 200 OK | 0 (no new posts) |
| sans-isc | 200 OK, last_modified Mon 15 Jun 15:59 GMT | 0 (10 items in feed, all pre-window — recovery pattern from 00:00 transient parse-error confirmed) |
| cisa-advisories | 200 OK, all.xml parsed cleanly with 30 items | 0 |
| cisa-kev (JSON) | reachable | 5 most-recent unchanged from 2026-06-12 |
| **mandiant (cloud.google.com direct-HTML)** | **PRODUCTIVE — UNC6508 primary retrieved** | **1 (THE FLASH CANDIDATE — GTIG primary direct retrieval succeeded for the 7th consecutive time)** |
| mandiant RSS feedburner | not re-attempted this sweep (under-24h skip rule, stale-persistent 28 consecutive failures from 15:30 PM 2026-06-14) | n/a |
| darkreading | not re-attempted this sweep (under-24h skip rule after first 404 observation at 06:00; awaiting operator URL review) | n/a |
| volexity | not re-attempted this sweep (under-24h skip rule, stale-persistent 7+ consecutive failures) | n/a |

## FLASH candidate

### Item: GTIG primary — UNC6508 PRC-nexus campaign against North American medical, military health, defense intelligence, AI research, uncrewed vehicle systems via INFINITERED on REDCap (Sept 2023 – Nov 2025)

- **raw-signal file:** `raw-2026-06-15-flash-1200-001-gtig-mandiant-primary-unc6508-prc-nexus-medical-military-ai-research-north-america-infinitered-redcap-flash-candidate-ad-adjacent.md`
- **Trigger fired:** Trigger 5 — active multi-victim campaign vs A&D sector (targeting-priority-level A&D-adjacency, not named-A&D-prime victim level — see calibration note in candidate file for grader)
- **Source:** Mandiant / Google Threat Intelligence Group primary direct retrieval at https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research — A1 grade
- **Relays:** SecurityWeek (Eduard Kovacs) 10:07 EDT + BleepingComputer (Bill Toulas) 10:00 EDT — both credit GTIG, no independent telemetry
- **Attribution:** "UNC6508, a People's Republic of China (PRC)-nexus threat actor" per GTIG high-confidence assessment. NOT cross-walked to any existing roster actor by GTIG; Archimedes preserves verbatim per Hard Rule 2
- **Roster status:** UNC6508 NOT on 24-actor roster — operator-deferred /new-actor candidate (grader surfaces, operator scaffolds)
- **IOCs:** 13 indicators (1 IP 23.169.65.49 / 1 email BebitaBarefoot774@gmail.com / 1 filename help.php / 7 SHA256 hashes / 1 GUID b49e334d-9c01-463e-9bc5-00a6920fb66e / 2 host artifacts Patroit + xc32038474a)
- **Critical override:** does NOT apply (no CVE, no roster actor, no named A&D-prime victim — 0 of 4 conditions met)
- **Quiet hours:** N/A (active hours)
- **Anti-noise:** PASS — first FLASH on this topic in 24h window, A1 substrate quality (> B2 minimum), no prior corpus entry on UNC6508

## Anti-noise holds applied this sweep (NOT re-FLASHed)

1. **Ivanti Sentry CVE-2026-10520** CVSS 10.0 — BOD 26-04 KEV deadline PAST EOB 2026-06-14 (~18h before this sweep); retrospective compliance-metrics phase
2. **Oracle PeopleSoft CVE-2026-35273** CVSS 9.8 UNC6240 / ShinyHunters per Mandiant primary — BOD 26-04 KEV deadline EOD TODAY Sunday 2026-06-15 (~T-12h from this sweep)
3. CVE-2026-20253 Splunk Enterprise (vendor confirmation pending)
4. NPM 12 default script-execution change
5. **Fable 5 / Mythos 5 Anthropic USG export-control** — The Record carried 2nd-day relay this sweep; no new substrate vs prior coverage; HOLD continues
6. Handala #014 / Cal Water (Iran Cyber Watch, third-source NEGATIVE binding)
7. **Velvet Ant Operation Highland** — HelpNet carried 4th-publisher relay of Sygnia primary this sweep; no new substrate beyond Sygnia primary (already covered as finding-2026-06-12-0004 substrate + raw-2026-06-13-pm-004); Sygnia primary direct retrieval still pending; HOLD continues
8. Check Point VPN CVE-2026-50751 / Qilin
9. PAN-OS CVE-2026-0257 (shipped this AM as finding-2026-06-15-0004 — 24h hold)
10. Awesome Motive WordPress supply-chain (shipped this AM as finding-2026-06-15-0003 — 24h hold)
11. **The Gentlemen ransomware** (shipped this AM as finding-2026-06-15-0005 — 24h hold; SW carried Mackay Sugar Australia victim this sweep, no FLASH-eligible substrate change — same actor, same campaign, anti-noise binding)
12. Tchap Misère (shipped this AM as finding-2026-06-15-0002 — 24h hold)
13. ShinyHunters Council of Europe (shipped this AM as finding-2026-06-15-0001 — 24h hold; BC carried separate Infinite Campus 137K K-12 staff item this sweep — separate ShinyHunters victim but K-12 sector not A&D, no roster-actor uplift, not FLASH-eligible)
14. FBI/Google Outsider Enterprise PhaaS takedown (finding-2026-06-14-0001)

## Source-health soft observations (NO file mutations this sweep, under-24h skip rule)

- **mandiant feedburner RSS:** Not re-attempted this sweep (under-24h skip rule; stale-persistent 28 consecutive failures from 15:30 PM 2026-06-14). Direct-HTML path on cloud.google.com SUCCEEDED for the 7th consecutive time — and was load-bearing for the UNC6508 candidate this sweep. Canonical-swap operator decision continues pending.
- **proofpoint /us/threat-insight/blog/feed:** Not re-attempted this sweep (under-24h skip rule). 5th consecutive 404 soft-pattern continuity.
- **sophos news.sophos.com/en-us/feed/:** Not re-attempted this sweep. Replacement candidate `news.sophos.com/en-us/category/threat-research/feed/` operator decision still pending.
- **CISA all.xml:** 200 OK + 30 items + clean parse. Recovery from Saturday 403 pattern stable through the weekend; routine pattern. 0 in-window items.
- **SANS ISC rssfeed.xml:** 200 OK + clean parse + 10 items in feed, 0 in-window. Recovery from 00:00 single parse-error observation fully stable across 06:00 → 12:00.
- **Dark Reading rss.xml:** Not re-attempted this sweep (under-24h skip rule after first 404 observation at 06:00 sweep). Awaiting operator URL review.

## Trigger evaluation — Trigger 5 POSITIVE, all others NEGATIVE

| Trigger | Result | Notes |
|---|---|---|
| 1. Critical CVE + active exploitation + A-grade | NEGATIVE | No net-new CVE-bound substrate in window. PAN-OS CVE-2026-0257 hold continues, M365 Copilot SearchLeak is vendor-fixed Varonis disclosure (no CVE / no exploitation framing). |
| 2. New attribution to tracked actor | NEGATIVE | No net-new attribution to any of the 24 roster actors in window. ShinyHunters Infinite Campus carry is anti-noise hold (continuation of cluster already shipped this AM). |
| 3. First-party Splunk IOC hit within 24h | NEGATIVE | 0 hits on 19-IOC standing set (10th consecutive clean sentinel); 0 hits on 9-IOC ad-hoc UNC6508 set. |
| 4. Tracked actor TTP change A/B-grade | NEGATIVE | No net-new TTP delta on any roster actor in window. |
| 5. Active nation-state campaign vs A&D | **POSITIVE** | UNC6508 — see candidate file. A1 GTIG primary + multi-victim + active 26-month campaign + A&D-adjacent target priorities verbatim (military health, defense intelligence, uncrewed vehicle systems, Indo-Pacific command, cyber offensive programs). |
| 6. Zero-day no patch (CVSS >= 8.0 or widely deployed) | NEGATIVE | No net-new zero-day in window. |

## Critical override (actually-wake-up) — does NOT apply

| Condition | Status |
|---|---|
| CVSS 10.0 | N/A — UNC6508 has no CVE (configuration / patch-hygiene REDCap exposure pattern); Ivanti CVE-2026-10520 at 10.0 is anti-noise hold with deadline already past |
| Confirmed active exploitation | UNC6508 campaign IS active but condition is CVE-gated |
| Attributed to tracked actor | UNC6508 NOT on roster |
| A&D watchlist entity named as target | NEGATIVE — military health institutions / defense intelligence categories cited but no named A&D-prime victim |
| **Result** | **Override DOES NOT apply** (0 of 4 conditions met) |

## Recommendation

**HAND OFF UNC6508 candidate to grader.** Active-hours posting rules apply; if grader promotes and red-team confirms, brief composes single-topic FLASH per INTEL-BRIEF-STANDARDS.md FLASH format and librarian posts to `#flash-alerts`. The candidate substrate is A1 GTIG primary with comprehensive IOC table + YARA rule — high-quality first FLASH on a previously-untracked PRC-nexus actor with A&D-adjacent targeting priorities.

Recommended grader-side actions:

1. **Read raw-2026-06-15-flash-1200-001** — full substance + 13-IOC table + GTIG attribution language verbatim + Trigger 5 calibration question
2. **Calibration on Trigger 5 A&D-sector element** — does "targeting-priority-level A&D-adjacency per A1 primary" (military health, defense intelligence, uncrewed vehicle systems, Indo-Pacific command, cyber offensive programs) satisfy the trigger, or does it require a named-A&D-prime victim? Collector reads the trigger as sector-level-sufficient given A1 primary attestation. Grader to confirm.
3. **Hard Rule 2 binding** — UNC6508 attribution belongs to GTIG with high-confidence framing. Preserve verbatim. Do NOT cross-walk to APT41 / APT40 / Salt Typhoon / Volt Typhoon — GTIG did not, Archimedes must not originate.
4. **Operator-deferred /new-actor candidacy** — surface UNC6508 to operator as high-quality `/new-actor` candidate: A1 primary, espionage-motivated, PRC-nexus, A&D-adjacent targeting, custom modular backdoor with public YARA rule, 26-month documented dwell. Collector does NOT originate scaffolding; operator runs `/new-actor`.
5. **IOC sentinel expansion** — recommend grader / librarian add the 9 high-fidelity UNC6508 IOCs (1 IP + 1 email + 7 SHA256) to the standing Splunk sentinel set going forward. Operator can decide whether to keep a separate UNC6508 9-IOC set or fold into a unified 28-IOC set with the existing 19-IOC PeopleSoft set.

## Hard Rule compliance

- Hard Rule 1 (LEGAL-POLICY): all sources public OSINT, no prohibited query patterns, no exploitation assistance. PASS.
- Hard Rule 2 (no novel attribution): UNC6508 attribution preserved verbatim from GTIG; no cross-walk originated. PASS.
- Hard Rule 3 (no exploitation content): YARA rule referenced by name + link to GTIG primary; not reproduced verbatim. IOCs at indicator level only. PASS.
- Hard Rule 7 (15-word quote limit): all source claims paraphrased; attribution language captured as structured fields. PASS.
- Hard Rule 8 (Splunk first-party priority): two sentinel queries run (standing 19-IOC + ad-hoc 9-IOC), 0 hits, visibility-limited absence flagged. PASS.

## Note for next scheduled brief (15:30 / 16:00 afternoon 2026-06-15)

- **Oracle PeopleSoft CVE-2026-35273** BOD 26-04 deadline at EOD Sunday 2026-06-15 (~T-12h from this sweep). The 16:00 afternoon brief is the **post-deadline-window-opens coverage** point (deadline closes at midnight EDT, brief publishes at 16:00 → T-8h before deadline closure). Briefer should pivot language to "T-8h before EOD closure" framing.
- **Velvet Ant Operation Highland** — HelpNet today is the 4th relay of the Sygnia primary; Sygnia primary direct retrieval still pending. Operator-deferred `/new-actor` status unchanged.
- **UNC6508 FLASH candidate (this sweep)** — if grader promotes, will be the first FLASH of the 2026-06-15 cycle; substantial A1-substrate net-new actor + IOC set delivered.
- Source-health: CISA all.xml stable, SANS ISC stable, Dark Reading still needs operator URL review (under-24h skip continues).
- Next FLASH sweep at 18:00 EDT 2026-06-15 (active hours, normal posting rules apply).
