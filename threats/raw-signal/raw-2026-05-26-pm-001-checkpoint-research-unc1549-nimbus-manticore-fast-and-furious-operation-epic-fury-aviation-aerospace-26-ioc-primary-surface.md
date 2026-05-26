---
raw_id: raw-2026-05-26-pm-001-checkpoint-research-unc1549-nimbus-manticore-fast-and-furious-operation-epic-fury-aviation-aerospace-26-ioc-primary-surface
collected_at: 2026-05-26T15:35:00-04:00
run_id: pre-brief-20260526-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: checkpoint-research
  source_name: "Check Point Research (primary publication) + SecurityWeek (Ionut Arghire relay) + Industrial Cyber (Anna Ribeiro relay)"
  source_url: https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/
  source_url_relay_securityweek: https://www.securityweek.com/iranian-apt-targets-aviation-software-companies-with-updated-tools/
  source_url_relay_industrialcyber: https://industrialcyber.co/ransomware/irgc-linked-nimbus-manticore-group-attacks-defense-aerospace-telecom-sectors-using-minifast-malware-toolkit/
  published_at: 2026-05-22T00:00:00+00:00       # Check Point Research primary date
  in_window_surfaces:
    - securityweek: 2026-05-26T13:26:17+00:00   # 09:26 EDT (in PM window)
    - industrialcyber: 2026-05-26T00:00:00+00:00 # Anna Ribeiro byline today
  byline_primary: Check Point Research team
  byline_securityweek: Ionut Arghire (International Correspondent)
  byline_industrialcyber: Anna Ribeiro (News Editor)
source_grade_at_collection:
  primary_grade: A
  primary_rationale: |
    Check Point Research is an A-grade vendor source per source-grades.yaml.
    "Fast and Furious - Nimbus Manticore Operations During the Iranian
    Conflict" is the originating publication (2026-05-22). SecurityWeek
    and Industrial Cyber pieces today (2026-05-26) are B-grade relays —
    SecurityWeek is in source-grades.yaml as B; Industrial Cyber is in
    source-grades.yaml as industrialcyber-co (B). Industrial Cyber adds
    explicit "defense, aerospace, telecom" sector framing in its relay
    that does NOT appear verbatim in the CKR primary — CKR primary uses
    "defense, aviation and telecommunication" — relay editorialization to
    "aerospace" should be flagged to the grader for fidelity assessment.
match_reason:
  watchlist: []                  # No A&D-prime named victims in CKR primary (named victims: zero; only sector + region descriptors)
  actors: ["004"]                # UNC1549 (corpus #004; aliases per _roster.yaml include Tortoiseshell, Smoke Sandstorm, Imperial Kitten, Crimson Sandstorm; aliases ADDED IN-WINDOW per CKR primary: Bohrium, TA455, Nimbus Manticore)
  related_actors_subgroup_relation: ["011"]    # Charming Kitten (APT35) — CKR describes Nimbus Manticore as "believed to be a subgroup of Charming Kitten (APT35)"
  vulnerabilities: []
  keywords:
    - "Nimbus Manticore"
    - "UNC1549"
    - "Bohrium"
    - "Smoke Sandstorm"
    - "TA455"
    - "Charming Kitten APT35 subgroup"
    - "IRGC"
    - "Operation Epic Fury"
    - "US military campaign against Iran"
    - "February 28 2026"
    - "MiniFast backdoor"
    - "MiniJunk V2"
    - "MiniUpdate"
    - "AppDomain hijacking"
    - "AppDomainManager"
    - "trojanized XML .config files"
    - "DLL sideloading"
    - "trojanized Zoom installer"
    - "SEO poisoning"
    - "getsqldeveloper.com"
    - "Oracle SQL Developer impersonation"
    - "career-themed phishing"
    - "fake hiring portals"
    - "US domestic airlines impersonated"
    - "AI-assisted malware development"
    - "LLM-based tools"
    - "Azure web sites hosting"
    - "OnlyOffice document hosting"
    - "SSL.com certificate abuse"
    - "Gray Matter Software"
    - "Kirubel Kerie Negeya"
    - "Operation Epic Fury campaign"
    - "Campaign 1 Rising Tension"
    - "Campaign 2 Operation Epic Fury"
    - "Campaign 3 SQL Developer"
    - "ZoomUpdateTaskUser"
    - "WindowsSecurityUpdate scheduled task"
    - "Saudi Arabia"
    - "Australia"
    - "United States aviation"
    - "Europe"
    - "Middle East"
    - "Israel"
    - "UAE"
    - "Accenture impersonation"

triage_tags:
  - corpus_extension_unc1549_thread
  - net_new_primary_source_surfacing_in_corpus
  - anti_noise_locked_thread_morning_finding_2026_05_26_0001
  - new_ioc_payload_26_hashes_26_domains_in_window
  - sector_framing_aviation_vs_aerospace_relay_drift_flagged
  - us_aviation_explicit_targeting_per_ckr_primary
  - defense_sector_named_no_specifics
  - novel_capability_appdomain_hijacking
  - novel_capability_ai_assisted_development
  - novel_capability_seo_poisoning_at_scale
  - novel_minifast_backdoor_full_capability_drop
  - sslsign_certificate_abuse_gray_matter_kirubel
  - flash_trigger_2_marginal_fail_attribution_not_new_to_corpus
  - flash_trigger_4_qualified_fail_ttps_corpus_anchored
  - flash_trigger_5_qualified_fail_no_named_a_d_prime_victim
  - grader_finding_extension_to_2026_05_26_0001
  - vendor_primary_url_now_in_corpus_first_time

iocs_extracted: true
iocs_count: 60                  # 26 SHA256 + 26 domains + 1 IP-style (no IP; 0) + 6 C2 API endpoints + 2 SSL.com cert subjects + 2 file paths + 2 scheduled tasks + 1 UA string + 0 CVE
text_word_count: 1850
promoted: true
promoted_to_finding: finding-2026-05-26-0007-checkpoint-research-unc1549-nimbus-manticore-fast-and-furious-operation-epic-fury-primary-26-ioc
promoted_at: 2026-05-26T16:00:00-04:00
promoted_by: grader
promoted_in_run: afternoon-20260526-160000
ttl_expires_at: 2026-08-24T15:35:00-04:00

---

# Fast and Furious — Nimbus Manticore Operations During the Iranian Conflict

**Source primary:** Check Point Research — "Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict" — 2026-05-22 (URL: https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/).

**In-window relays surfaced today (2026-05-26 PM window):**
- SecurityWeek — Ionut Arghire — 09:26 EDT 2026-05-26 — "Iranian APT Targets Aviation, Software Companies With Updated Tools" — https://www.securityweek.com/iranian-apt-targets-aviation-software-companies-with-updated-tools/
- Industrial Cyber — Anna Ribeiro — 2026-05-26 — "IRGC-linked Nimbus Manticore group attacks defense, aerospace, telecom sectors using Minifast malware toolkit" — https://industrialcyber.co/ransomware/irgc-linked-nimbus-manticore-group-attacks-defense-aerospace-telecom-sectors-using-minifast-malware-toolkit/

## Why this raw-signal exists despite morning anti-noise lock

The morning brief (2026-05-26 08:00) promoted **finding-2026-05-26-0001** from THN's relay surface of MiniFast / MiniJunk V2 / SEO poisoning / getsqldeveloper. That finding inherits anti-noise lock on the UNC1549 thread through 2026-05-27 08:00 per FLASH-POLICY.

**Net-new in PM window** (not in finding-0001):
1. **Check Point Research PRIMARY publication URL** — first time the CKR primary lands in the corpus surface. Prior corpus traction was via Unit 42 (Screening Serpens) and THN relays. CKR primary is the originating-source vendor for the Nimbus Manticore designation.
2. **26 SHA256 hashes + 26 malicious domains** — full IOC drop from CKR primary, not present in finding-0001's IOC set (finding-0001 had ~7 IOCs via THN relay).
3. **Aerospace sector framing** — Industrial Cyber's relay editorializes CKR's "aviation" to "aerospace, aviation, telecom"; grader should evaluate fidelity (CKR primary text uses "aviation" not "aerospace").
4. **Campaign 1 / Campaign 2 / Campaign 3 enumerated structure** — three-campaign breakdown (Rising Tension / Operation Epic Fury / SQL Developer) with date anchors.
5. **Operation Epic Fury** — campaign tied to "US military campaign against Iran launched on February 28, 2026". Significant geopolitical anchor.
6. **Full MiniFast 16-opcode capability matrix** — comprehensive backdoor capability drop (corpus had only abstract description prior).
7. **AppDomain hijacking specifics** — including trojanized `.config` files pointing to AppDomainManager classes, scheduled task hijacking of Zoom's `ZoomUpdateTaskUser-<SID>`, scheduled-task name `WindowsSecurityUpdate`.
8. **SSL.com certificate abuse** — two certificate subjects (Gray Matter Software S.R.L., Kirubel Kerie Negeya).
9. **AI-assisted malware development** — CKR explicit assessment ("We assess that this capability was likely supported, at least in part, by LLM-based tools and AI-assisted development techniques"). Novel TTP class for UNC1549.
10. **US aviation explicit targeting** — CKR primary quote: "the actor's recent operations demonstrate an expansion toward aviation-sector targets in the United States."

This raw-signal exists for **grader finding-extension consideration** on finding-2026-05-26-0001 (add CKR primary URL, expand IOCs, add sector-fidelity note). NOT a FLASH (anti-noise applies); the grader will decide whether to extend the existing finding or open a sibling.

## Executive summary (CKR primary language preserved where useful)

Check Point Research documents three waves of cyberattacks by Nimbus Manticore (tracked as UNC1549), an IRGC-affiliated Iranian threat actor, during geopolitical tensions in 2026:

- **Campaign 1 — Rising Tension (February 2026)**: New phishing activity; AppDomain Hijacking introduced; MiniJunk deployment.
- **Campaign 2 — Operation Epic Fury (February 28, 2026 +)**: "US military campaign against Iran launched on February 28, 2026"; Nimbus Manticore resurfaces with enhanced capabilities; trojanized Zoom installer; MiniFast backdoor introduced; AI-assisted development indicators.
- **Campaign 3 — SQL Developer (April 2026)**: SEO poisoning campaign targeting Oracle SQL Developer downloads; fake hiring portals impersonating US domestic airlines.

CKR attribution language (verbatim): *"Iranian, IRGC affiliated, threat actor Nimbus Manticore"*; *"believed to be a subgroup of Charming Kitten (APT35)"*; *"We assess that this capability was likely supported, at least in part, by LLM-based tools and AI-assisted development techniques."*

## Sector / geography framing (originating vs. relay editorialization)

| Source | Sectors named | Direct quote |
|---|---|---|
| Check Point Research (primary) | "defense, aviation and telecommunication" | "primarily targets the defense, aviation and telecommunication sectors" |
| SecurityWeek (Arghire relay) | aviation, software | "aviation and software companies" |
| Industrial Cyber (Ribeiro relay) | "defense, aerospace, telecom" + "aerospace, aviation, telecom" | "continues to focus heavily on defense, aerospace, and telecommunications sectors as geopolitical tensions intensify" |

**Grader-relevant**: Industrial Cyber's relay introduces "aerospace" (not in CKR primary text). For an Archimedes A&D-prime target audience, the distinction between commercial aviation (airlines) and aerospace (manufacturers including Boeing/Airbus/Lockheed) is material. The CKR primary text supports "aviation" (commercial airlines, with US-domestic-airline impersonation) and "defense" (generic, no specifics) — NOT "aerospace" in the manufacturer/prime sense. Industrial Cyber's editorialization may overstate the A&D-prime targeting signal.

## Named victims / impersonation targets

**Named confirmed victims:** ZERO (CKR primary names no specific company as a confirmed victim).

**Named impersonated organizations (used in phishing lures):**
- Accenture (in phishing lures)
- US-based airline (campaign 2 lure; specific airline unnamed)
- US-domestic airlines (campaign 3 fake hiring portals; specific airlines unnamed)
- Zoom (legitimate software trojanized via installer)
- Oracle SQL Developer (campaign 3 fake download)
- Chrome / Google (user-agent spoofing)

**Hosting / abuse infrastructure:**
- Azure Web Sites (hosting)
- OnlyOffice (document hosting / malware staging)
- SSL.com (certificate authority abused — two specific subjects)

## Tools and malware (capability layers; novel-to-corpus vs. corpus-anchored)

### MiniFast (novel-to-corpus full capability drop)
- 64-bit Windows PE DLL impersonating Chrome browser
- Entry point: `CheckForUpdates` exported function
- 16-opcode command matrix (corpus had only abstract description prior):
  - 0x02 directory enumeration
  - 0x03 file move/rename
  - 0x04 shell command execution via `cmd.exe /c`
  - 0x05 process enumeration
  - 0x06 file/directory deletion
  - 0x07 file download from C2
  - 0x08 file upload to C2
  - 0x09 drive enumeration
  - 0x0A process termination
  - 0x0B DLL loading with exported function invocation
  - 0x0C directory creation
  - 0x0D ZIP archive creation
  - 0xB0 UAC elevation via `runas`
  - 0xB1 persistence installation via scheduled tasks
  - 0xF0 dynamic poll interval adjustment
  - 0xF2 jitter configuration
- Communication: JSON-formatted API-style architecture; Base64-encoded task structures

### MiniJunk V2 (corpus-anchored predecessor; updated iteration)
- Backdoor framework (documented since 2025)
- Replaced by MiniFast in Operation Epic Fury phase

### Loaders (in-window first-time mention)
- `uevmonitor.dll` (Campaign 1 first-stage)
- `InitInstall.dll` (Campaign 2 first-stage)
- `Updater.dll` (Campaign 2 second-stage)

### Exploitation techniques
- **AppDomain Hijacking** — abuses .NET runtime via malicious `.config` files pointing to `AppDomainManager` classes (novel-to-corpus level of detail)
- **DLL sideloading** — legitimate binaries load malicious DLLs from same directory
- **Task hijacking** — intercepts legitimate Zoom scheduled tasks (`ZoomUpdateTaskUser-<SID>`) for persistence
- **SEO poisoning** — domain link farming + keyword stuffing for search-engine visibility (Bing + DuckDuckGo confirmed)

### AI-assisted development indicators (novel-to-corpus class for UNC1549)
- Excessive error handling on simple API calls
- Verbose, repetitive function naming patterns
- Embedded debug/status messages
- Modular code organization despite functional simplicity

## Timeline

| Date | Campaign | Event |
|---|---|---|
| At least 2022 | (Active since) | Initial UNC1549 / Nimbus Manticore activity |
| November 2024 | Dream Job campaign | Lazarus-style tactics adoption |
| February 2026 | Campaign 1: Rising Tension | AppDomain Hijacking introduction; MiniJunk deployment |
| **February 28, 2026** | **Operation Epic Fury** | **US military campaign against Iran launched**; Nimbus Manticore resurfaces |
| During Operation Epic Fury | Campaign 2 | Trojanized Zoom installer; MiniFast introduced; AI-assist indicators |
| April 2026 | Campaign 3 | SEO poisoning; getsqldeveloper.com; US-airline-themed hiring portals |
| 2026-05-22 | CKR primary published | Three-wave consolidation |
| 2026-05-26 (today) | SecurityWeek + Industrial Cyber relays | A&D-relevant audience surface |

## Splunk first-party check

```
search index=defenseclaw_local OR index=archimedes earliest=-8h@h latest=now
  ("MuddyWater" OR "Nimbus Manticore" OR "UNC1549" OR "MiniFast" OR "MiniJunk"
   OR "AppDomain" OR "Smoke Sandstorm" OR "Bohrium" OR "TA455"
   OR "157.20.182.49" OR "sendit.sh" OR "fmapp.exe" OR "fmapp.dll"
   OR "sentinelmemoryscanner" OR "sentinelagentcore"
   OR "ChromElevator" OR "FileFiend"
   OR CVE-2026-48172 OR CVE-2026-45659 OR CVE-2026-9082 OR CVE-2026-42897
   OR "LiteSpeed" OR "lsws.redisAble" OR "SharePoint"
   OR "Lithuania" OR "Centre of Registers" OR "OnlyOffice"
   OR APT35 OR "Charming Kitten" OR MuddyWater)
  NOT sourcetype=archimedes:*
```

**Result:** ZERO events. Hard Rule 8 framing: silence is not disconfirming.

---

## Extraction notes

- Language: en
- Article type: vendor blog (CKR primary) + news (SW + IC relays)
- Raw IOC extraction invoked: yes
- 15-word quote discipline observed throughout

## IOCs (from ioc-extraction skill)

```yaml
- type: cve
  value: null    # no CVE in this corpus extension; UNC1549 ops are post-exploit / supply-chain phishing class
- type: domain
  value: business-startup.org
  defanged_original: business-startup[.]org
  context: Nimbus Manticore C2 / phishing infrastructure
  source_brief_id: ckr-fast-and-furious-2026-05-22
  campaign: Operation Epic Fury (Campaign 2)
- type: domain
  value: business-startup.azurewebsites.net
  context: Azure-hosted Nimbus Manticore staging
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: businessstartup.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: buisness-centeral.azurewebsites.net
  defanged_original: buisness-centeral.azurewebsites[.]net
  context: Azure-hosted variant (typosquat of "business central")
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: buisness-centeral-transportation.azurewebsites.net
  context: Azure-hosted transportation-themed variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: buisness-centeral-transportation.com
  defanged_original: buisness-centeral-transportation[.]com
  context: Apex domain for transportation-themed lure
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: licencemanagers.azurewebsites.net
  context: Azure-hosted license-management lure
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: licencesupporting.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: peerdistsvcmanagers.azurewebsites.net
  context: Azure-hosted; impersonates Windows BranchCache service name (peerdistsvc)
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: nanomatrix.azurewebsites.net
  context: Azure-hosted
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: PremierHealthAdvisory.com
  defanged_original: PremierHealthAdvisory[.]com
  context: Healthcare-themed phishing lure apex
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: PremierHealthAdvisory.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: Premier-HealthAdvisory.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: ramiltonsfinance.com
  defanged_original: ramiltonsfinance[.]com
  context: Finance-themed phishing lure apex
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: ramiltonsfinance.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: ramiltons-finance.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: globalitconsultants.azurewebsites.net
  context: IT-consultancy-themed Azure-hosted lure
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: globalit-consultants.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: global-it-consultants.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: global-it-checkers.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: global-it-checkbusiness.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: global-check-itbusiness.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: global-check-business-it.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: globalbusiness-checkers-it.azurewebsites.net
  context: Azure-hosted variant
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: domain
  value: getsqldeveloper.com
  defanged_original: getsqldeveloper[.]com
  context: SEO-poisoning fake Oracle SQL Developer download site (Campaign 3, April 2026)
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 10fd541674adadfbba99b54280f7e59732746faf2b10ce68521866f737f1e46d
  context: Nimbus Manticore campaign artifact (CKR primary IOC list)
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: eee657ffdb2af8ed6412221e7d5fbf4f5742f2ac2c88f43f12db46af0697de71
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 781605ce9d4a9869e846f6c9657d71437cb6240ab27ffbc4cd550c0e06996690
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 2c214494fd0bad31473ca8adce78a4f50847876584571e66aadeae70827ec2dc
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: f08b17856616d66492a24dced27f788e235f35f42fa7cd10f315000d3a2f4c03
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: a57ffb819fe8d98ff925c5d7b239598fe302acf5a13193d7a535040a71298fdf
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 63d0d3c4a7f71bdbca720903d6a99b832089cc093c64d2938e7e001e56c17ab4
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 74882085db2088356ed7f72f01e0404a0a98cda88ef56fb15ce74c1f36b26d27
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: bc3b44154518c5794ce639108e7b9c5fecb0c189607a26de1aaed518d890c7ad
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: ecaf493c320d201d285ef5f61d75744216e47cf1115b4af528f9a78883cc446e
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 44f4f7aca7f1d9bfdaf7b3736934cbe19f851a707662f8f0b0c49b383e054250
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 0db36a04d304ad96f9e6f97b531934594cd95a5cea9ff2c9af249201089dc864
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 485f182f7b74ee4013b2539275a95d21e3a9bf0082c331937af9353a324b36f3
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 64530d7e6ee30e4a66d9eeed6b8595c33fd72f5f73409133ca40539e5695df4c
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 332ba2f0297dfb1599adecc3e9067893e7cf243aa23aedce4906a4c480574c17
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 9e4a658e6d831c9e9bdfe11884a75b7c64812ed0a80e8495ddf6b316505acac1
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 43dc62cef52ebdd69e79f10015b3e13890f26c058325c0ff139c70f8d8eadcfa
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 8808c794c24367438f183e4be941876f1d3ecd0c8d2eb43b10d2380841d2283b
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 5c3362d20229597d11380f56d1f2eb39647fb6afad7be8392a7abcd18dff12f8
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 0291ef318576953f7f3fe287e7775ed1d7c3206119dc7b9cd6d85c02779e6e40
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: d4a7e9f107fe40c1a5d0139c6c6e25bf6bf57f61feff090bee28f476bb3cc3c2
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 38bd137c672bd58d08c4f0502f993a6561e2c3411773d1ae57ee0151a0a9d11d
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: f54cd38632ac9da3af3533ae93e92625cbcb04df521dbf1b6acfaa81218f9e8c
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: b19e06da580cf91691eda066ac9ee4b09c6e5dc26c367af12660fe1f9306eec4
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: 9cf029daca89523d917dafed0568d11d00e45ec96b5b90b4a1f7fd4018c7da84
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: a13ba3c5aff46e9daf2d23df4b3e3d49dc7236c207c56f0a1433051f3450d441
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: hash_sha256
  value: dfa1e3137a032ee8561a1cd5e1a0f71a10bebb36aef7c336c878638a9c1239ee
  context: Nimbus Manticore campaign artifact
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: file_path
  value: C:\Users\<USER>\AppData\Local\Packages\
  context: MiniJunk deployment path (template; user-name expansion at runtime)
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: file_path
  value: C:\Users\<USER>\AppData\Local\Zoom\bin\update
  context: MiniFast staging directory; uses Zoom's bin/update path for blending
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: scheduled_task
  value: ZoomUpdateTaskUser-<SID>
  context: Hijacks Zoom legitimate update task for MiniFast persistence
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: scheduled_task
  value: WindowsSecurityUpdate
  context: Persistence task name; impersonates Windows security update routine
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: user_agent
  value: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
  context: MiniFast HTTPS user-agent impersonating Chrome 146
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: other
  type_detail: ssl_cert_subject
  value: "Gray Matter Software S.R.L."
  context: SSL.com-issued certificate abused for code signing (CKR primary)
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: other
  type_detail: ssl_cert_subject
  value: "Kirubel Kerie Negeya"
  context: SSL.com-issued certificate abused for code signing (CKR primary)
  source_brief_id: ckr-fast-and-furious-2026-05-22
- type: other
  type_detail: c2_api_endpoint
  value: "/rg (POST handshake), /agent/init (POST register), /agent/poll?token= (GET task), /agent/result (POST), /upload/ (PUT exfil), /files/ (GET download)"
  context: MiniFast C2 REST API surface
  source_brief_id: ckr-fast-and-furious-2026-05-22

attribution_claims:
  - actor_named: UNC1549
    actor_aliases_in_text:
      - Nimbus Manticore
      - Bohrium
      - Smoke Sandstorm
      - TA455
    actor_aliases_relation:
      - "subgroup of Charming Kitten (APT35)"      # CKR primary explicit
    confidence_language: "IRGC affiliated" (no formal "high confidence" qualifier)
    attribution_source: Check Point Research (primary, 2026-05-22)
    attribution_source_grade: A
    novelty_to_corpus: false        # corpus-anchored since 2026-04-02 (#004); MiniFast/MiniJunk thread anchored 2026-05-23 0600 FLASH
    novelty_to_window: |
      The CKR primary URL surfaces in corpus for the first time today.
      The "Bohrium" + "TA455" aliases land in corpus for the first time
      via this raw-signal (existing _roster.yaml #004 aliases do not
      include Bohrium or TA455 — actor-profiler should consider alias
      expansion). The "subgroup of Charming Kitten (APT35)" relation
      is novel framing — _roster.yaml has #004 (UNC1549) and #011
      (Charming Kitten) as separate entries with no subgroup relation
      documented; CKR's framing may warrant an actor-profiler review of
      the relationship between the two roster entries.
```
