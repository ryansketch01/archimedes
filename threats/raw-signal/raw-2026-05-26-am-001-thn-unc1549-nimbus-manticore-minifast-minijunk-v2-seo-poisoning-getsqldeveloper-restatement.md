---
raw_id: raw-2026-05-26-am-001
collected_at: 2026-05-26T07:32:00-04:00
run_id: pre-brief-20260526-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: thehackernews
  source_name: The Hacker News
  source_url: https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html
  published_at: 2026-05-26T03:13:05-04:00
  author: info@thehackernews.com (The Hacker News)
relays_originating_primaries:
  - vendor: Check Point Research
    publication: "Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict"
    publication_date: 2026-05-22
    corpus_tracked_since: 2026-05-23 0600 FLASH lineage
  - vendor: Palo Alto Networks Unit 42
    publication: "MiniUpdate / MiniJunk V2 / AppDomainManager tradecraft"
    publication_date: 2026-05-22
    corpus_tracked_since: 2026-05-23 0600 FLASH lineage
match_reason:
  watchlist: []                  # No A&D-prime named (aviation sector mentioned, not prime)
  actors:
    - "004"                      # UNC1549 / Nimbus Manticore / Screening Serpens / Smoke Sandstorm
  vulnerabilities: []
  keywords:
    - Iranian state-sponsored
    - IRGC
    - aviation sector
    - software sector
    - defense sector
    - telecommunications
    - oil and gas
    - MiniFast
    - MiniJunk V2
    - MiniUpdate
    - AppDomain hijacking
    - SEO poisoning
    - getsqldeveloper
    - trojanized Zoom installer
    - AI-assisted malware development
triage_tags:
  - tracked_actor_restatement
  - unc1549_tradecraft_evolution_update
  - b_grade_relay_a_grade_primaries
  - non_flash_morning_brief_absorption
  - corpus_anti_noise_locked
  - aviation_software_sectoral_shape_no_prime_naming
iocs_extracted: true
iocs_count: 2                    # getsqldeveloper[.]com + AppDomainManager TTP keyword (technique-name, not strict IOC)
text_word_count: 412
promoted: true
promoted_to_finding: finding-2026-05-26-0001-unc1549-nimbus-manticore-minifast-minijunk-v2-seo-poisoning-getsqldeveloper
promoted_at: 2026-05-26T08:00:00-04:00
ttl_expires_at: 2026-08-24T07:32:00-04:00
---

# Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning

**Source:** The Hacker News, 2026-05-26 03:13 EDT
**URL:** https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html
**Byline:** The Hacker News editorial (info@thehackernews.com)

## Article summary

The Iranian state-sponsored threat actor known as **Nimbus Manticore**
(aka **Screening Serpens** and **UNC1549**) has been attributed to a
fresh campaign using lures impersonating organizations in the
**aviation and software sectors** across the **U.S., Europe, and the
Middle East** following the joint U.S.-Israeli military campaign
against the country in late February 2026.

**Sectors targeted** (per THN relay of Check Point Research + Unit 42):
aviation, software, defense, telecommunications, oil and gas.

**Geographic targets:** U.S., Europe, Middle East, Saudi Arabia,
Australia, Israel, United Arab Emirates. Named individual employees
in Saudi Arabia and Australia (software and aviation sectors).

**Malware families:**
- **MiniFast** — newly developed backdoor, also referred to as
  **MiniUpdate** per Unit 42 taxonomy (naming overlap question:
  Check Point taxonomy calls it MiniFast; Unit 42 taxonomy calls it
  MiniUpdate; same/adjacent family).
- **MiniJunk** — previously deployed variant.
- **MiniJunk V2** — updated version.

**MiniFast capabilities** (per Check Point Research analysis cited
in THN relay): file operations, directory listings, process
enumeration, command execution via `cmd.exe`, DLL loading, ZIP
archive creation, persistence via scheduled tasks, privilege
escalation using `runas`, and configurable beacon intervals with
jitter randomization.

**Delivery vectors:**
1. **Phishing** — career-themed lures impersonating aviation/software
   organizations; fake meeting invitations; **trojanized Zoom
   installers**.
2. **SEO poisoning** — fake SQL Developer download pages ranking on
   Bing and DuckDuckGo; domain **`getsqldeveloper[.]com`**.
3. **AppDomain hijacking** — leveraged to launch malicious DLLs
   from benign executables in ZIP archives.

**Infrastructure indicators:**
- Domain: `getsqldeveloper[.]com` (fake SQL Developer download page).
- "Dozens of supporting domains registered for SEO reputation manipulation" (per THN relay; specific domains not enumerated in THN article).

**AI-assisted development indicators:** Check Point Research noted
"excessive error handling," "repetitive function naming," and
"modular code organization" suggesting AI-assisted malware
development.

**Attribution language (verbatim per THN):** "Iranian state-sponsored
threat actor" affiliated with "Iran's Islamic Revolutionary Guard
Corps (IRGC)." Campaign followed "joint U.S.-Israeli military
campaign against the country in late February 2026."

**Primary research vendors cited:**
- Check Point Research — analysis of MiniFast, AI-assisted
  development indicators.
- Palo Alto Networks Unit 42 — targeting documentation and
  MiniUpdate/MiniJunk V2 deployment tracking.

**A&D-prime named:** None explicitly mentioned as compromised in
primary attack narratives. Aviation sector mentioned but no
watchlist-prime named (Lockheed Martin, Boeing, RTX, Northrop, GD,
BAE, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran,
Honeywell Aerospace, Airbus, Elbit) per infrastructure/watchlists/
aerospace-defense.yaml.

---

## Extraction notes

- Language: en
- Publisher byline: The Hacker News editorial
- Article type: blog (B-grade relay)
- Raw IOC extraction invoked: yes
- Grader disposition target: UNC1549 (#004) tradecraft-evolution UPDATE
  surface for morning brief; per FLASH-POLICY anti-noise rule and
  operator anti-noise list "0523 still in queue", this is morning-
  brief absorption disposition, not a new finding promotion. Brief-
  tier update on existing corpus surface.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: domain
    value: getsqldeveloper[.]com
    context: |
      Fake SQL Developer download page. SEO poisoning delivery
      vector for MiniFast (aka MiniUpdate) backdoor distribution.
      Search engines: Bing and DuckDuckGo per THN relay.
    confidence: medium  # relay-layer attribution; CKR is originating primary
    source_attribution: "Check Point Research (relayed via The Hacker News)"
    first_observed: pre-2026-05-22 (CKR publication date)
    related_campaign: UNC1549 / Nimbus Manticore aviation-software-aerospace targeting 2026
    actor_id: "004"
    defanged: true

ttp_keywords:
  - name: AppDomain hijacking
    framework_mapping: MITRE T1574 / Hijack Execution Flow
    context: "Malicious DLLs launched from benign executables in ZIP archives per Nimbus Manticore campaign chain"
  - name: SEO poisoning
    framework_mapping: MITRE T1583.008 / Acquire Infrastructure — Malvertising
    context: "Fake SQL Developer download pages ranking on Bing and DuckDuckGo"

attribution_claims:
  - claim_text: "Iranian state-sponsored threat actor"
    actor_aliases: [Nimbus Manticore, Screening Serpens, UNC1549]
    affiliation_named: "Iran's Islamic Revolutionary Guard Corps (IRGC)"
    confidence_language: "attributed to" (THN relay)
    originating_primaries:
      - Check Point Research "Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict" (2026-05-22)
      - Palo Alto Networks Unit 42 (2026-05-22 concurrent publication on MiniUpdate/MiniJunk V2/AppDomainManager)
    corpus_baseline: |
      UNC1549 attribution to Iran/IRGC is vendor-community consensus
      baseline per Mandiant (originating cluster naming), Unit 42
      (concurrent cluster mapping as Smoke Sandstorm / Crimson
      Sandstorm), and now Check Point Research (Nimbus Manticore /
      Screening Serpens cluster mapping). THN's relay does not
      constitute new attribution per FLASH-POLICY Trigger 2 novelty
      prong.
    hard_rule_2_compliance: |
      Archimedes does not originate attribution. Source attribution
      language preserved verbatim. Cross-cluster alias merge
      (Nimbus Manticore = Screening Serpens = UNC1549 = Smoke
      Sandstorm = Crimson Sandstorm = Imperial Kitten = Tortoiseshell)
      is corpus-baseline per _roster.yaml actor #004.
```
