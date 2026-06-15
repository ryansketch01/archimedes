---
raw_id: raw-2026-06-15-flash-1200-001
collected_at: 2026-06-15T12:08:00-04:00
run_id: flash-sweep-20260615-120000
collection_mode: flash_sweep
source:
  source_yaml_id: mandiant
  source_name: Google Threat Intelligence Group (Mandiant + Mandiant Consulting + FLARE team + Workspace Security)
  source_url: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research
  published_at: 2026-06-15T00:00:00-04:00
  byline: Google Threat Intelligence Group (GTIG)
  note: "Primary research — Mandiant/GTIG direct retrieval (NOT relay). Mandiant feedburner RSS stale 27 consecutive failures; direct HTML retrieval succeeded as it has across the prior 6 direct-HTML attempts. Surfaced via SecurityWeek + BleepingComputer same-day relays at 14:07 and 14:00 UTC (mid-window) crediting GTIG primary; substrate retrieved direct from cloud.google.com primary post."
secondary_publishers:
  - source_yaml_id: securityweek
    source_name: SecurityWeek
    source_url: https://www.securityweek.com/chinese-hackers-target-medical-military-and-ai-research-in-north-america/
    published_at: 2026-06-15T14:07:45+00:00
    byline: Eduard Kovacs
    note: "Same-day relay; SW credits GTIG primary; no independent telemetry, faithful summary of GTIG verbatim."
  - source_yaml_id: bleepingcomputer
    source_name: BleepingComputer
    source_url: https://www.bleepingcomputer.com/news/security/chinese-hackers-breach-redcap-servers-steal-medical-research/
    published_at: 2026-06-15T14:00:00+00:00
    byline: Bill Toulas
    note: "Same-day relay; BC credits GTIG primary; partial IOC reproduction (BebitaBarefoot774@gmail.com, Patroit compliance rule named). No independent telemetry."
match_reason:
  watchlist: [aerospace-defense]
  actors: [UNC6508]
  vulnerabilities: []
  keywords: [UNC6508, INFINITERED, REDCap, PRC-nexus, China-linked, military health institutions, defense intelligence, Indo-Pacific command, uncrewed vehicle systems, cyber offensive programs, national defense intelligence, North America, military readiness, AI research]
triage_tags: [flash_candidate, trigger-5-ad-sector-campaign, new_attribution, new_actor_candidate, active_campaign, multi_victim, ad_sector_adjacent, prc_nexus, gtig_primary_direct, mandiant_direct_html_path_validated, splunk_sentinel_clean]
iocs_extracted: true
iocs_count: 11
text_word_count: 1820
promoted: true
promoted_to_finding: finding-2026-06-15-flash1200-0006
promoted_at: 2026-06-15T12:24:00-04:00
ttl_expires_at: 2026-09-13T12:08:00-04:00
---

# GTIG primary — UNC6508 PRC-nexus targets North American medical, military health, defense intelligence, AI research, uncrewed vehicle systems via INFINITERED on exposed REDCap servers (Sept 2023 – Nov 2025, 26+ months dwell)

## Source provenance + relay map

- **Primary:** Google Threat Intelligence Group (GTIG), published 2026-06-15. Authors: GTIG + Mandiant Consulting + FLARE team + Workspace Security. 20-minute long-read with full IOC table + comprehensive YARA rule G_Backdoor_INFINITERED_1.
- **Relay 1:** SecurityWeek (Eduard Kovacs) at 10:07 EDT — credits GTIG, faithful summary, no independent telemetry.
- **Relay 2:** BleepingComputer (Bill Toulas) at 10:00 EDT — credits GTIG, surfaces 2 IOCs (email + "Patroit" compliance rule name), no independent telemetry.

Mandiant feedburner RSS continued failure (28th consecutive observation, under-24h skip rule applies — NOT re-attempted this sweep, source-health.yaml NOT mutated). Direct-HTML path on `cloud.google.com/blog/topics/threat-intelligence` succeeded for the 7th consecutive time. Canonical-swap operator decision still pending; the direct-HTML path is the productive endpoint and would have been required either way to retrieve full IOC substrate.

## Substance (paraphrased, no >15 word quotes per Hard Rule 7)

### Attribution language (verbatim where load-bearing, Hard Rule 2 binding)

GTIG attributes the activity to "UNC6508, a People's Republic of China (PRC)-nexus threat actor" — high-confidence assessment based on infrastructure overlaps between campaigns, consistent INFINITERED deployment on REDCap servers, and the specific targeting of medical research and defense sectors. GTIG describes UNC6508 as espionage-motivated with priorities aligning to historic PRC state-sponsored espionage trends and intelligence collection requirements.

GTIG did NOT cross-walk UNC6508 to any existing named PRC-nexus group — APT41, APT40, APT10, Volt Typhoon, Salt Typhoon, etc. are not invoked. UNC6508 is presented as a distinct cluster.

Per Hard Rule 2 — Archimedes preserves the GTIG attribution language verbatim and does NOT originate any cross-walk to existing roster actors. UNC6508 is **NOT on the 24-actor roster** as of this sweep (roster _meta total_actors: 24, last_updated 2026-05-10).

### Campaign timeframe

- **Earliest known compromise:** September 2023
- **Observed activity duration:** Sept 2023 through November 2025 (26+ months)
- **Dwell time before detection:** "More than a year undetected" in primary victim
- **Publication of GTIG analysis:** 2026-06-15 (today)

### Target categories (A&D-adjacent — explicit per GTIG primary)

**Sector categories (verbatim from GTIG, treated as the load-bearing claim):**

- North American academic medical research institutions
- World-renowned clinical providers
- Premier academic centers
- **North American military health institutions**
- Professional advocacy groups
- Health regulatory bodies

**Research/intelligence collection priorities (verbatim from GTIG):**

- Molecular discovery and clinical drug trials
- State-level public health policy
- **Military readiness**
- **Artificial intelligence**
- **Uncrewed vehicle systems**
- **Cyber offensive programs**
- **Indo-Pacific command operations**
- **National defense intelligence**

**Named victims:** None disclosed in GTIG primary. Described as "diverse set of national, state, and private medical entities" across US and Canada. No named A&D-prime (Lockheed Martin / Boeing / Raytheon / Northrop Grumman / etc.) implicated as victim. **A&D-adjacency is targeting-category-level, NOT named-A&D-prime victim level.** This is doctrinally important for the grader: campaign explicitly targets A&D-adjacent research priorities (uncrewed vehicles, AI, defense intelligence, Indo-Pacific command) but no A&D-prime contractor named as confirmed victim.

### Initial access vector

- **Primary:** Vulnerable / legacy REDCap (Research Electronic Data Capture) servers — exposed web-based medical research database platform widely used by academic medical centers
- **Targeting pattern:** Threat actor probed for legacy/vulnerable REDCap versions running side-by-side with current installations
- **Persistence:** "help.php" web shell deployed early; INFINITERED malware deployed ~3 months post-initial-compromise
- **Exfiltration:** Google Workspace content compliance rule abuse — rule named "Patroit" (typo of "Patriot") configured to capture and forward emails matching geo-strategic policy / military strategy / advanced technology / pathogen-research keywords (including "Chikungunya" — correlating with July 2025 Guangdong province outbreak)
- **Source of administrative access:** Compromised ASUS router at 23.169.65.49 (US-based OBF / Operational Relay Box network endpoint)

### Malware — INFINITERED (modular backdoor)

Three-module architecture deployed ~3 months post-initial-compromise:

1. **Dropper / Upgrade Interception** — initial installation + ongoing update capability
2. **Credential Harvester** — captures REDCap database session credentials; uses database session ID prefix `xc32038474a` as forensic marker
3. **Backdoor with C2** — persistent communication channel back to operator infrastructure; uses GUID delimiter `b49e334d-9c01-463e-9bc5-00a6920fb66e` as persistence marker

GTIG published comprehensive YARA rule `G_Backdoor_INFINITERED_1` covering magic flags, markers, code patterns (plaintext + base64-encoded variants).

### IOCs (full set extracted, Hard Rule 3 binding — IOCs only, no exploit content; YARA rule REFERENCED but not reproduced verbatim)

| IOC | Type | Context | Confidence |
|---|---|---|---|
| 23.169.65.49 | ipv4 | US-based OBF (Operational Relay Box) — compromised ASUS router used as administrative login source | A1 |
| BebitaBarefoot774@gmail.com | email | Exfiltration destination for "Patroit" Workspace compliance rule (account now disabled per GTIG) | A1 |
| help.php | filename | Web shell deployed early in compromise chain on REDCap servers | A1 |
| ba6b73b0ca0dc7f86b3b397893ac32d729fd53f9df20643288f141f29d020af7 | sha256 | Persistence (help.php) | A1 |
| db65c1b9f9e4cb4d729f45ad4b6fcf3e277caf9eb4c875425dec93fd883f9136 | sha256 | INFINITERED credential harvester | A1 |
| c1ac43d23f89d41eb4ff131678ab562ab2cfed9aa334b13767ef141d303b0e5b | sha256 | INFINITERED credential harvester | A1 |
| 8f0158855a656b629ca76ebca565f18bc25563ded34b65d6771632c20edb68ec | sha256 | INFINITERED backdoor | A1 |
| 51a57bfc9ed3eb6451c1c289607814d59e1698c666fb97ac5f694c398f23d045 | sha256 | INFINITERED backdoor | A1 |
| 4efbef69eb3b09bacff892d6a55778d07c418e7f15eba3cf1245e8cdfd8dda0b | sha256 | INFINITERED dropper | A1 |
| 58bb25777e0aa86bcd2125101e0bca4e8732b03d91bd8d2f205b446a2a8d5c86 | sha256 | INFINITERED dropper | A1 |
| b49e334d-9c01-463e-9bc5-00a6920fb66e | guid | INFINITERED backdoor persistence marker (host artifact) | A1 |
| xc32038474a | host_artifact | INFINITERED credential harvester database session ID prefix (forensic marker) | A1 |
| Patroit | host_artifact | Google Workspace content compliance rule name used for exfiltration (typo of "Patriot") | A1 |

**Total: 13 indicators** (1 IP, 1 email, 1 filename, 7 SHA256 hashes, 1 GUID, 2 host artifacts). All A1 confidence per Mandiant/GTIG primary direct attestation.

## Splunk first-party sentinel — 0 hits

- Query: 9 of the highest-fidelity UNC6508 IOCs (23.169.65.49 + email + 7 SHA256 hashes + GUID delimiter + INFINITERED string) across defenseclaw_local + archimedes, -30d lookback
- Result: 0 event_count
- Interpretation: silent Splunk does NOT disconfirm per Hard Rule 8. Frank is not a North American medical research institution and is not a REDCap deployment. UNC6508 target profile is medical/military health/academic research — Frank is a defense-research analyst workstation. Visibility-limited absence; this is the expected outcome. Sentinel logged as confirmation that the standing IOC set should be **EXPANDED** by the grader to track UNC6508 going forward.

Shodan InternetDB on 23.169.65.49 returned `found: false` — compromised ASUS router OBF endpoint has no public-facing services indexed by Shodan, consistent with a residential / SOHO consumer device used as a relay rather than a permanently-internet-facing C2.

## FLASH trigger evaluation

| Trigger | Result | Notes |
|---|---|---|
| 1. Critical CVE + active exploitation + A-grade | **NEGATIVE** | No specific CVE identified by GTIG; initial access is "legacy/vulnerable REDCap" exploitation but no CVE assigned per primary. PASS-by-default for CVSS gate (no CVE = no >=9.0 threshold to evaluate). |
| 2. New attribution to tracked actor | **NEGATIVE** | UNC6508 is NOT on the 24-actor roster. Attribution is to a *new* actor not currently tracked. This is the GAP that Trigger 5 closes — see below. |
| 3. First-party Splunk IOC hit within 24h | **NEGATIVE** | 0 hits on 9-IOC sentinel against defenseclaw_local + archimedes over -30d. Silent Splunk does NOT disconfirm (Hard Rule 8); Frank is not the UNC6508 target profile. **10th consecutive clean sentinel sweep across cumulative window.** |
| 4. Tracked actor TTP change A/B-grade | **NEGATIVE** | UNC6508 not tracked; TTP characterization is *first-time* on this actor, not a *delta* on an existing actor. |
| 5. Active multi-victim campaign vs A&D sector | **POSITIVE** | Campaign explicitly active (Sept 2023 through Nov 2025+, GTIG-confirmed). Multi-victim ("diverse set of national, state, and private medical entities" + military health institutions). A&D-adjacency at targeting-priority level (military readiness, uncrewed vehicle systems, AI, cyber offensive programs, Indo-Pacific command, national defense intelligence) per GTIG primary verbatim. Source-grade A1 (GTIG primary direct). **FLASH-ELIGIBLE.** |
| 6. Zero-day no patch | **NEGATIVE** | No specific CVE — REDCap "legacy/vulnerable versions" exploitation pattern is configuration / patch-hygiene exposure, not zero-day disclosure. |

## Critical override (actually-wake-up) evaluation

| Condition | Status |
|---|---|
| CVSS 10.0 | **N/A** — no CVE |
| Confirmed active exploitation | **N/A** — no CVE to be exploited; campaign IS active but condition is CVE-gated |
| Attributed to tracked actor | **N/A** — UNC6508 not on roster |
| A&D watchlist entity named as target | **NEGATIVE** — military health institutions / defense intelligence categories cited but no named A&D-prime victim |
| **Result** | **Override DOES NOT apply.** 0 of 4 conditions met. Standard active-hours posting rules apply. |

## Anti-noise check

- One FLASH per trigger-topic per 24h — UNC6508 is **first** FLASH on this topic (no prior FLASH or finding in corpus). Anti-noise PASSES.
- B2 minimum grade — GTIG primary direct retrieval = **A1 substrate quality.** Anti-noise PASSES.
- Red-team review (mandatory for WEP >= very-likely) — applies downstream at grader/red-team-analyst stage, not collector stage.

## Disposition

**FLASH-eligible per Trigger 5.** Hand off to grader for fast-path single-item grading + red-team review (since substrate quality is A1 + GTIG-stated high-confidence attribution, WEP is likely or very-likely territory).

Recommended grader notes:

1. **A1 source substrate** — GTIG primary direct retrieval with full IOC table + YARA rule. Highest possible source-grade.
2. **Hard Rule 2** — UNC6508 attribution belongs to GTIG; preserve verbatim ("PRC-nexus threat actor"), do NOT cross-walk to APT41/APT40/Salt Typhoon/Volt Typhoon. GTIG explicitly did NOT cross-walk; Archimedes must not originate one.
3. **Operator-deferred /new-actor candidacy** — UNC6508 is a high-quality candidate for the 24-actor roster: A1 primary disclosure, espionage-motivated, PRC-nexus, A&D-adjacent targeting categories, custom modular backdoor (INFINITERED) with publicly published YARA rule, 26-month documented dwell. Surface to operator via finding + brief; do NOT originate `/new-actor` scaffolding (collector does not originate; operator runs `/new-actor`).
4. **A&D-adjacency calibration** — targeting categories explicitly include military health, defense intelligence, uncrewed vehicle systems, Indo-Pacific command — these ARE A&D-adjacent in the broader sense (DoD MHS / military medical research / counter-UAS / SOCOM / INDOPACOM AOR). However, **no named A&D-prime contractor** is identified as a confirmed victim. The doctrinal calibration question for the grader is: does "category-level A&D-adjacent targeting per A1 primary" satisfy Trigger 5's "A&D sector targeting" element, or does the trigger require named-prime-victim binding? The collector reads the FLASH-POLICY Trigger 5 condition as "watchlist or A&D sector" — sector-level targeting per A1 primary should suffice. Grader to confirm.
5. **IOC expansion of standing sentinel set** — recommend adding the 9 high-fidelity IOCs to the standing Splunk sentinel set (was 19, would become 28). Operator may elect to keep 19-IOC PeopleSoft-focused set separate and run UNC6508 as a parallel 9-IOC tracking set, or fold both into a single 28-IOC set. Grader-deferred decision.
6. **Cross-walk to anti-noise hold** — Velvet Ant Operation Highland is in anti-noise hold. UNC6508 and Velvet Ant are BOTH PRC-nexus persistence-focused actors but GTIG does NOT cross-walk. Archimedes must NOT cross-walk either. Independent clusters per primary attribution.

## Hard Rule compliance

- **Hard Rule 1** (LEGAL-POLICY): All sources are publicly-available open-source intel (GTIG public blog, SecurityWeek, BleepingComputer). No prohibited query patterns, no exploitation assistance, no active recon. PASS.
- **Hard Rule 2** (No origination of attribution): UNC6508 attribution belongs to GTIG with high-confidence language. Archimedes preserves verbatim, originates no cross-walk. PASS.
- **Hard Rule 3** (No exploitation content): YARA rule REFERENCED by name (`G_Backdoor_INFINITERED_1`) and link to GTIG primary for full content. Detection content not exploitation content per doctrine; in any case the YARA rule itself is NOT copied into this raw-signal. IOCs captured at indicator level only. PASS.
- **Hard Rule 7** (15-word quote limit): No verbatim quote exceeds 15 words. Attribution language captured as paraphrased structured fields. PASS.
- **Hard Rule 8** (Splunk first-party priority): Splunk sentinel run and result captured. 0-hit outcome flagged as visibility-limited per target-profile mismatch, NOT as disconfirmation. PASS.

## Run metadata

- run_id: flash-sweep-20260615-120000
- collected_at: 2026-06-15T12:08:00-04:00
- collection_mode: flash_sweep
- ttl_expires_at: 2026-09-13T12:08:00-04:00 (90 days per LEGAL-POLICY retention)
- promoted: false (grader updates upon promotion)
