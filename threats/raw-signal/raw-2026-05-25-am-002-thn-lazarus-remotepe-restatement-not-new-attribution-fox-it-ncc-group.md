---
raw_id: raw-2026-05-25-am-002-thn-lazarus-remotepe-restatement-not-new-attribution-fox-it-ncc-group
collected_at: 2026-05-25T07:37:00-04:00
run_id: pre-brief-20260525-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News (Ravie Lakshmanan byline) — primary research NCC Group / Fox-IT (Yun Zheng Hu + Mick Koomen) — Lazarus Group RemotePE memory-only RAT expanded analysis"
  source_url: https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html
  source_grade_thn: B (provisional, awaiting ratification — second-cross-corroboration-cycle source per source-grades.yaml entry 2026-05-14)
  source_grade_fox_it_ncc_group: TENTATIVE_A_PENDING_SOURCE_GRADE_LOG_ENTRY    # fox-it / ncc-group NOT in source-grades.yaml as named entity; Tier-1 vendor research class (Fox-IT historical APT track record via NCC Group ownership); recommend operator add as A-grade provisional first-citation
  published_at: 2026-05-25T05:32:54-04:00
  primary_originating_publication: 2025-09-01       # "first highlighted in September 2025" per THN — exact date not in THN body; observation period mid-2023 to mid-2024
match_reason:
  watchlist: []                                 # No A&D-prime named victim
  actors: ["003"]                               # Lazarus Group — tracked actor #003 in _roster.yaml. BUT: restatement of September 2025 prior reporting, NOT new attribution. FLASH-POLICY Trigger 2 explicitly blocks restatement.
  vulnerabilities: []                           # No CVE cited
  keywords:
    - "Lazarus Group"
    - "North Korea"
    - "DPRK"
    - "RemotePE"
    - "DPAPILoader"
    - "RemotePELoader"
    - "Hell's Gate"
    - "ETW patching"
    - "PondRAT"
    - "POOLRAT"
    - "ThemeForestRAT"
    - "Fox-IT"
    - "NCC Group"
    - "memory-only RAT"
    - "DeFi"
    - "cryptocurrency"
triage_tags:
  - tracked_actor_surface
  - restatement_not_new_attribution
  - explicitly_not_flash_trigger_2_fire
  - actor_profiler_hook_003_review
  - splunk_first_party_first_pass_zero_hits
  - non_flash_tier
  - hard_rule_2_block_active
iocs_extracted: true
iocs_count: 4                                   # 1 C2 domain (aes-secure[.]net), 1 DPAPILoader DLL filename (Iassvc.dll), 1 social-engineering vector (Telegram impersonation), 1 fake-calendar-tool vector (Calendly/Picktime domains, named class not specific URLs)
text_word_count: 1700
promoted: false
rejected_at: 2026-05-25T08:00:00-04:00
rejection_id: reject-2026-05-25-0002
ttl_expires_at: 2026-08-23T07:37:00-04:00
---

# The Hacker News — Lazarus Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms
# Primary research: NCC Group / Fox-IT (Yun Zheng Hu + Mick Koomen, expanded technical analysis)

**Title:** Lazarus Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms
**THN byline:** Ravie Lakshmanan
**THN published:** 2026-05-25 09:32 UTC = 05:32 EDT (in-window)
**Primary researchers:** Yun Zheng Hu (Fox-IT / NCC Group); Mick Koomen (Fox-IT / NCC Group)
**Primary originating publication:** September 2025 ("first highlighted" per THN body)
**Observation period:** Mid-2023 to mid-2024
**Earliest DPAPILoader artifact:** November 2023
**Earliest RemotePE timestamp:** July 4, 2023
**URL:** https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html

---

## CRITICAL FRAMING — restatement not new attribution

This raw-signal is captured for **tracking-awareness and
actor-profiler hook** purposes. It is **explicitly NOT a
FLASH-POLICY Trigger 2 fire** despite citing tracked actor #003
(Lazarus Group) because:

1. **THN article body explicitly states "first highlighted in
   September 2025"** for the RemotePE malware family. This is
   the May 2026 follow-up offering expanded technical analysis,
   NOT a first-time attribution.
2. **FLASH-POLICY Trigger 2 explicitly requires
   `attribution_is_new_not_restatement`** per the trigger
   condition documented in `doctrine/FLASH-POLICY.md`.
3. **Observation period is mid-2023 to mid-2024**; earliest
   artifact is November 2023. This is **2+ year retrospective
   technical analysis**, not active-campaign disclosure.
4. **Hard Rule 2** independently blocks Archimedes-originated
   attribution; we preserve Fox-IT's attribution language
   verbatim ("North Korea-linked Lazarus Group" with no
   confidence qualifier in body text).

Companion sentinel am-000 documents this as a Trigger 2
**NEAR-MISS, not a fire.**

---

## Attribution language (Hard Rule 2 — verbatim preservation)

THN/Fox-IT attribution language used in the article body:

> "North Korea-linked Lazarus Group" (THN — no confidence qualifier such as high/moderate/low)

Fox-IT framing of the toolset:

> "purpose-built for long-term observation campaigns" (7 words — within Hard Rule 6 limit; single instance from Fox-IT)
> "may be reserved for high-value targets" (7 words — within Hard Rule 6 limit; single instance from Fox-IT — note "may be" hedge preserved)

**Lazarus aliases NOT used in this article** despite the
`_roster.yaml` entry #003 listing: Hidden Cobra, Zinc, Diamond
Sleet, Labyrinth Chollima, Guardians of Peace. The article uses
"Lazarus Group" exclusively.

---

## Victim sectors and geography

- **Sectors:** Financial organizations, cryptocurrency / crypto
  firms, decentralized finance (DeFi) sector
- **Geography:** One unnamed DeFi organization targeted; no
  specific country named
- **A&D / defense / aerospace impact:** NOT MENTIONED

**Calibration to Archimedes target profile (mid-to-large US A&D
contractor):** Lazarus targeting of financial / crypto / DeFi
sectors is the historical DPRK financial-operations pattern
(consistent with Stardust Chollima / BlueNoroff / APT38
tradecraft per `_roster.yaml` entry #002 lineage). Not
operationally aligned to A&D-prime defensive priority for this
specific campaign documentation.

---

## Malware components — technical analysis

| Component | Function |
|---|---|
| **DPAPILoader** | First-stage loader. Decrypts and loads `RemotePELoader` using Windows DPAPI (Data Protection API). Earliest artifact November 2023. |
| **RemotePELoader** | Second-stage loader. Beacons to C2; fetches `RemotePE` payload; employs **Hell's Gate** (direct syscall) and **ETW patching** (Event Tracing for Windows interference) for evasion. |
| **RemotePE** | Full-featured RAT (Remote Access Trojan) in C++. Memory-only execution (no disk persistence). Polls C2 for six command categories: config, file ops, process management, sleep/exit, server ping. |

**Cross-platform claim:** Article addresses **Windows only**.
NO Linux or macOS coverage mentioned.

**Attack vector (initial access):**
- Social engineering via **Telegram impersonation**
- Fake **Calendly / Picktime** domains (named as a class; specific
  URLs not in THN body)

---

## Indicators of Compromise (IOCs)

### C2 infrastructure

- **`aes-secure[.]net`** (C2 domain, single entry observed)

### File artifacts

- **`Iassvc.dll`** (DPAPILoader filename)

### Hashes

- **NONE provided** in THN body — no SHA-256 / SHA-1 / MD5 values
  for DPAPILoader, RemotePELoader, or RemotePE. The primary Fox-IT
  / NCC Group writeup may include them but THN summarization
  excludes them.

### IPs

- **NONE** provided in THN body.

### URLs / paths / registry keys / mutexes

- **NONE** provided in THN body.

### Splunk first-party hand-built query EXECUTED this sweep

```spl
search index=defenseclaw_local earliest=-24h@h latest=now
  (aes-secure OR Iassvc.dll OR DPAPILoader OR RemotePE OR
   RemotePELoader OR Lazarus)
| head 50
```

Result: **ZERO hits**. Hard Rule 8: silence is not disconfirming.
First-party telemetry surface dormant non-self pattern continues
(56th consecutive sweep on tstats baseline).

---

## Historical Lazarus campaign context cited in article

| Family | Relationship to RemotePE |
|---|---|
| **PondRAT** | Lightweight variant of POOLRAT (SIMPLESEA). Identified September 2024. |
| **ThemeForestRAT** | Deployed in same September 2025 DeFi intrusion as RemotePE. |
| **POOLRAT / SIMPLESEA** | Shares file-overwriting behavior (seven passes of constant bytes) with RemotePE. |

These prior families are cited for technical-lineage context only.
None are corpus-tracked vulnerabilities; all are documented
Lazarus / DPRK family malware per public-attribution Mandiant /
MSTIC / CrowdStrike / Kaspersky / Fox-IT baseline tracking.

---

## Why this is NOT a FLASH-POLICY Trigger 2 fire

Per `doctrine/FLASH-POLICY.md` Trigger 2:

```yaml
trigger-2-tracked-actor-attribution:
  conditions_all:
    - article_attributes_activity_to_actor == true
    - attributed_actor in _roster.yaml
    - attribution_is_new_not_restatement == true     # FAILS HERE
```

| Condition | Evaluation |
|---|---|
| `article_attributes_activity_to_actor == true` | YES — THN attributes to Lazarus Group |
| `attributed_actor in _roster.yaml` | YES — Lazarus = #003 (aliases: Hidden Cobra, Zinc, Diamond Sleet, Labyrinth Chollima, Guardians of Peace) |
| `attribution_is_new_not_restatement == true` | **NO — explicit restatement of September 2025 prior reporting; observation period mid-2023 to mid-2024** |

**Trigger 2 BLOCKED on the third condition.** This is a
restatement / expanded-technical-analysis surface, not a new-
attribution surface.

Additional structural reasons not to fire as FLASH:

- Victim sectors are financial / crypto / DeFi, not A&D — fails
  Trigger 5 (A&D-sector campaign) on victim profile.
- No CVE cited — fails Trigger 1 (critical CVE exploited) and
  Trigger 6 (zero-day no patch).
- First-party hit query returned zero on -24h@h — fails Trigger
  3 (first-party IOC hit).
- The TTP layer (DPAPILoader / RemotePELoader / Hell's Gate /
  ETW patching) IS net-new to Archimedes corpus dossier on #003
  Lazarus but is RESTATEMENT-class content (September 2025 prior
  reporting). Trigger 4 (tracked-actor TTP change) requires
  "new tooling / targeting / infrastructure documented" with the
  same `attribution_is_new_not_restatement` condition pattern
  applied as a general FLASH-POLICY restraint.

---

## Why this IS captured for actor-profiler #003 hook

Per `doctrine/ACTOR-PROFILE-STANDARD.md` and the operational
pattern for /update-tracking cycles, expanded-technical-analysis
surfaces on tracked actors **should be logged in the actor's
dossier TTP catalog** even when they don't fire FLASH.

This raw-signal serves as an **input for the next /update-tracking
on actor #003 Lazarus Group** (next review due: 2026-06-30 per
`_roster.yaml`). Operational asks for actor-profiler on that
review:

1. Determine whether RemotePE / DPAPILoader / RemotePELoader /
   Hell's Gate / ETW patching mechanisms warrant entry into the
   Lazarus dossier TTP catalog (cursory review suggests these
   are not all currently captured in the dossier).
2. Verify the September 2025 Fox-IT primary publication is in
   the dossier reference list (or add it if not).
3. Consider whether the Telegram-impersonation + fake-Calendly/
   Picktime initial-access vector is documented as a Lazarus
   TTP class (this is a common DPRK social-engineering pattern
   but may not be in the dossier explicitly).
4. The seven-passes-of-constant-bytes file-overwriting behavior
   (RemotePE / POOLRAT / SIMPLESEA shared signature) is a
   diagnostic forensic artifact — worth adding to the dossier
   as a detection-engineering signature class.
5. Memory-only RAT execution class + Hell's Gate direct-syscall
   + ETW patching is the **anti-EDR-instrumentation toolkit
   layer** that should be cataloged for defensive prioritization
   against Lazarus targets.

---

## Recommendations to morning grader / briefer / orchestrator

1. **Grader: DO NOT promote to finding-tier as a new attribution.**
   This is restatement; promotion as a finding would violate Hard
   Rule 2 and FLASH-POLICY Trigger 2 restraint. Acceptable
   alternative: TRACKING-AWARENESS entry in morning brief
   monitoring-section (similar to how UNC1151 Ghostwriter
   Prometheus has been handled across recent sentinels — surface
   for awareness without grading as a new-finding event).
2. **Briefer: morning brief tracking-section UPDATE candidate**
   on #003 Lazarus — explicitly framed as "Fox-IT / NCC Group
   expanded technical analysis of September 2025 RemotePE
   memory-only RAT family; mid-2023 to mid-2024 observation
   period; financial / crypto / DeFi targeting; not A&D
   operationally aligned but TTP layer (DPAPILoader / Hell's
   Gate / ETW patching) is anti-EDR-instrumentation toolkit class
   worth dossier capture."
3. **Actor-profiler #003 hook**: next /update-tracking on Lazarus
   (due 2026-06-30 or sooner) should integrate this raw-signal
   plus Fox-IT primary writeup into the dossier TTP catalog +
   detection-engineering reference list.
4. **Splunk Savedsearch action**: add `aes-secure[.]net` +
   `Iassvc.dll` + `DPAPILoader` to ongoing Splunk savedsearch
   keyword list against `defenseclaw_local`. Zero hits this
   sweep; maintain ongoing detection.
5. **Operator: source-grade-log entry**: consider adding
   "NCC Group / Fox-IT (named-byline research, Tier-1 vendor
   class)" as A-grade provisional source first-citation —
   precedent class is Bitdefender 2026-05-13 + Symantec
   2026-05-13 + Cisco Talos 2026-05-14 + Darktrace 2026-05-14
   + ZDI 2026-05-16 (all provisional-A first-citation for Tier-1
   vendor research surfaces). 72h ratification clock would run
   from operator decision. NCC Group / Fox-IT has multi-decade
   APT-research track record (named-engineer-byline; first-party
   IR telemetry; sustained Lazarus / DPRK family coverage going
   back to BlueNoroff origins).

---

## Hard Rules compliance check

- **Rule 2** (no Archimedes-originated attribution): EXPLICIT
  COMPLIANCE — this raw-signal flags the surface as RESTATEMENT
  not new attribution. Fox-IT's attribution language preserved
  verbatim ("North Korea-linked Lazarus Group" with no confidence
  qualifier; "purpose-built for long-term observation campaigns"
  and "may be reserved for high-value targets" hedged framing
  preserved). Archimedes does NOT upgrade to a new-attribution
  framing.
- **Rule 3** (no exploitation content): no PoC code reproduced.
  Hell's Gate + ETW patching mechanisms described conceptually
  (defensive-detection-engineering layer); no operational
  instruction.
- **Rule 4** (passive only): WebFetch on public THN article;
  Splunk hand-built query on Archimedes's own instance. No
  active recon.
- **Rule 6** (15-word quote limit): two short quotes from Fox-IT
  via THN (7 words each), single instance each per source.
  Within limit.
- **Rule 7** (credentials radioactive): no credential exposure
  in source body.
- **Rule 8** (Splunk first-party): hand-built sweep executed on
  RemotePE / DPAPILoader / aes-secure[.]net / Iassvc.dll / Lazarus
  keywords; zero hits in -24h@h. 56th consecutive dormant non-
  self sweep on `defenseclaw_local`. Silence is not disconfirming.

---

## Disposition

- **Raw-signal status:** companion to am-000 sentinel; NOT a
  morning-brief finding candidate. TRACKING-AWARENESS context
  for morning brief monitoring-section + actor-profiler #003
  hook for next /update-tracking cycle.
- **FLASH trigger status:** Trigger 2 NEAR-MISS, explicitly
  BLOCKED on `attribution_is_new_not_restatement == false`.
  Hard Rule 2 reinforces the block.
- **No anti-noise lock created** (restatement surfaces don't
  create locks per anti-noise policy; if subsequent in-window
  surfaces appeared with same restatement framing, would
  absorb as UPDATE flags without lock).
- **TLP:CLEAR.**
