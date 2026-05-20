---
raw_id: raw-2026-05-20-flash-1200-001
collected_at: 2026-05-20T12:08:00-04:00
run_id: flash-sweep-20260520-120000
collection_mode: flash_sweep
test: false
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News — relay of ESET (Eric Howard byline) and Symantec September 2022 baseline"
  source_url: https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html
  published_at: 2026-05-20T08:51:43-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords:
    - Webworm
    - EchoCreep backdoor
    - GraphWorm backdoor
    - Discord C2
    - Microsoft Graph API C2
    - OneDrive command-and-control
    - FishMonger
    - Aquatic Panda
    - SixLittleMonkeys
    - Space Pirates
    - APT17 (9002 RAT context)
    - China-aligned
    - aerospace sector named
    - IT services
    - electric power
    - SoftEther VPN
    - WormFrp ChainWorm SmuxProxy WormSocket proxy tools
    - GitHub repository impersonating WordPress fork
triage_tags:
  - in_window
  - thehackernews_b_grade_provisional_relay
  - eset_a_grade_eric_howard_originating_byline
  - symantec_a_grade_provisional_2022_lineage_baseline
  - webworm_not_in_roster_yaml
  - fishmonger_aquatic_panda_six_little_monkeys_space_pirates_apt17_not_in_roster_yaml
  - hard_rule_2_no_alias_origination_to_roster
  - aerospace_sector_named_but_no_ad_watchlist_prime
  - flash_trigger_5_borderline_fail_watchlist_specificity_clause
  - non_flash_morning_brief_ad_sector_focus_candidate
  - novel_ttp_discord_c2_plus_msgraph_api_c2_pair
  - infrastructure_softether_vpn_plus_github_impersonation
  - splunk_first_party_zero_hits_49th_consecutive_dormant_sweep
  - cross_actor_alias_cluster_apt17_overlap_via_9002_rat_eset_hedged
iocs_extracted: true
iocs_count: 0
text_word_count: 480
promoted: false
ttl_expires_at: 2026-08-18T12:08:00-04:00
---

# Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API

## Article body summary (extracted)

The Hacker News reports ESET researcher Eric Howard byline on China-aligned
threat actor Webworm (first documented by Broadcom-owned Symantec in September
2022) deploying two custom backdoors in 2025 campaign activity:

- **EchoCreep** — uses Discord for C2; supports file upload/download and
  cmd.exe execution
- **GraphWorm** — leverages Microsoft Graph API for C2; spawns cmd.exe
  sessions, executes processes, transfers files to/from OneDrive

Auxiliary infrastructure: GitHub repository impersonating a WordPress fork;
SoftEther VPN; custom proxy tools (WormFrp, ChainWorm, SmuxProxy, WormSocket).

**Attribution language verbatim (per THN extraction):** "China-aligned threat
actor" / "assessed to be active since at least 2022."

**Aliases / cluster mentions (THN extraction):** FishMonger (aka Aquatic
Panda), SixLittleMonkeys, Space Pirates, APT17 (referenced in 9002 RAT
context).

**Victims (sectors / countries):**
- Sectors: IT services, **aerospace**, electric power
- Countries: Russia, Georgia, Mongolia, Belgium, Italy, Serbia, Poland, Spain,
  South Africa

**IOC list:** none explicitly published in THN article body. ESET originating
research (welivesecurity.com) NOT directly retrieved this sweep — flagged
for next-pass direct retrieval if grader promotes.

## Roster-match evaluation (Hard Rule 2)

| Alias | In _roster.yaml? | Notes |
|---|---|---|
| Webworm | NO | Not a tracked primary name or listed alias |
| FishMonger | NO | Not in any of 24 actor entries |
| Aquatic Panda | NO | Not in any of 24 actor entries |
| SixLittleMonkeys | NO | Not in any of 24 actor entries |
| Space Pirates | NO | Not in any of 24 actor entries |
| APT17 | NO | Roster contains APT28, APT29, APT34, APT37, APT40, APT41 — NOT APT17 |

Hard Rule 2: Archimedes does NOT originate a cross-walk between Webworm /
its alias cluster and any tracked actor (e.g., does NOT speculate APT17 ↔
Salt Typhoon / FamousSparrow / Earth Estries; does NOT speculate Aquatic
Panda ↔ Volt Typhoon). The aliases are recorded verbatim from ESET via THN
relay; no propagation of attribution beyond what ESET asserts. If a future
ESET / Symantec / Mandiant / Unit 42 / CrowdStrike publication explicitly
brings Webworm into a tracked-actor cluster, that becomes a /new-actor or
roster-update candidate — not an Archimedes-originated claim.

## FLASH trigger evaluation

- **T1 (critical-cve-exploited):** FAIL — no CVE
- **T2 (tracked-actor-attribution new):** FAIL — actor + aliases NOT in
  roster; Hard Rule 2 prevents origination
- **T3 (first-party IOC hit):** FAIL — no IOCs published; Splunk -24h zero
  hits on broader tracked superset
- **T4 (tracked-actor TTP change):** FAIL — not a tracked actor
- **T5 (ad-sector-campaign):** **BORDERLINE-FAIL.** Conditions reviewed:
  - article_describes_active_campaign: YES (2025 campaign activity per ESET)
  - targets_include_aerospace_defense_or_watchlist_entity: PARTIAL —
    "aerospace" sector explicitly named in target list, BUT no specific
    A&D-watchlist company named (Lockheed Martin, Boeing, RTX, Northrop
    Grumman, General Dynamics, BAE, L3Harris, Leidos, SAIC, Thales, GE
    Aerospace, Safran, Honeywell Aerospace, Airbus, Elbit). Strict-read of
    trigger condition fails on watchlist-entity-specificity clause.
  - multi_victim_confirmed: YES (9 countries named, 3 sectors)
  - **Verdict:** 2 of 3 strict conditions PASS, 1 PARTIAL → TRIGGER FAILS
    per strict-read FLASH-POLICY clause. Surfaced as raw-signal for grader
    review on morning-brief A&D Sector Focus standing-section consideration.
    If grader's morning-brief composition opts to include a "sector-shape
    aerospace targeting by untracked China-aligned cluster" item in the
    A&D Sector Focus section, this raw-signal anchors it.
- **T6 (zero-day no patch):** FAIL — no CVE

## Why surface as raw-signal anyway

Three reasons the collector preserves this item rather than discarding to
log-only:
1. **Aerospace-sector named target** — directly relevant to the morning
   brief's standing A&D Sector Focus section (`watch-config.yaml` standing
   section id=ad-sector, always_include=true).
2. **TTP-pair novelty** — Discord C2 + MS Graph API / OneDrive C2 as a
   matched pair, both off-the-shelf-cloud-service-abuse mechanisms. Discord
   C2 is not new in isolation (many cybercrime + APT operators have used
   it); MS Graph API C2 is not new in isolation (UNC1549 cluster has
   neighboring tradecraft per Mandiant 2026-05-04 originating research,
   though UNC1549 uses different cloud services per finding-2026-05-05-0001).
   The pair, deployed concurrently by the same actor, is a noteworthy
   detection-engineering signal for A&D defenders running Defender for
   Cloud Apps / Microsoft Graph Activity log analytics.
3. **APT17 alias mention** — gap in roster. APT17 is a long-running
   China-attributed cluster (Hidden Lynx / DeputyDog historically); not
   currently in _roster.yaml. If subsequent ESET / Symantec / Mandiant /
   Unit 42 / CrowdStrike publications strengthen the Webworm ↔ APT17
   linkage, this becomes a /new-actor candidate. Surfacing now reduces
   discovery latency for the next /update-tracking cycle.

## Hard Rules compliance

- Rule 2 (no first-time attribution): preserved — all attribution layers
  recorded as ESET/Symantec-attested via THN relay; no Archimedes-side
  alias-to-roster cross-walk
- Rule 3 (no PoC content): no PoC / payload content extracted
- Rule 6 (15-word quote limit): "China-aligned threat actor" (4 words) /
  "assessed to be active since at least 2022" (8 words) — both under limit
- Rule 7 (copyright discipline): no >15-word verbatim quotes in this
  raw-signal beyond the two attribution-language strings above
- Rule 8 (Splunk first-party priority): zero hits on Webworm-adjacent
  query patterns (Discord C2 user-agent patterns, OneDrive anomaly
  patterns) in -24h sweep across both archimedes + defenseclaw_local
  indexes

## TLP marking

TLP:CLEAR — public news source (The Hacker News); no first-party telemetry
content reproduced; no PII; no credentials.
