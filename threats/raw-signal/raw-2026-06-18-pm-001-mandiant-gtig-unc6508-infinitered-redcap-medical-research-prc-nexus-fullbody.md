---
raw_id: raw-2026-06-18-pm-001-mandiant-gtig-unc6508-infinitered-redcap-medical-research-prc-nexus-fullbody
collected_at: 2026-06-18T15:36:00-04:00
run_id: pre-brief-20260618-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mandiant
  source_name: Mandiant / Google Threat Intel
  source_url: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research
  published_at: 2026-06-15T00:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [UNC6508, INFINITERED, China-Nexus, REDCap, medical research, military health, national defense intelligence, Indo-Pacific, AI, UAS, cyber offensive]
triage_tags: [substrate_pivot_update_candidate, body_substantiation_carry_forward, dedup_window_closed, prc_nexus, espionage, medical_research, military_health, structural_ad_relevance, gtig_a_grade_primary]
iocs_extracted: true
iocs_count: 12
test: false
promoted: true
promoted_to_finding: finding-2026-06-18-0002
promoted_at: 2026-06-18T16:08:00-04:00
ttl_expires_at: 2026-09-16T15:36:00-04:00
---

# Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research

## Source metadata

- **Publisher:** Google Threat Intelligence Group (GTIG) / Mandiant
- **Authors:** Patrick Whitsell, John McGuiness
- **Publication date:** 2026-06-15 (per article metadata)
- **URL:** https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research
- **Read time:** 21 minutes
- **Source grade:** A (Mandiant baseline per source-grades.yaml)
- **Retrieval timestamp:** 2026-06-18T15:36 EDT (~3.5 days post-publication; URL slug `prc-targets-us-medical-research` confirmed via cloud.google.com/blog/topics/threat-intelligence index-page enumeration at this sweep — slug differs from operator-anticipated path which was the body-retrieval blocker at 2026-06-17 18:00 sweep direct-URL 404)

## Collection context

This raw-signal substantiates the carry-forward title-only "Public and Private Medical Community Targeted by China-Nexus Threat Actor Pursuing Artificial Intelligence, Cyber, Medical, and National Defense Research" surface that was first visible on the cloud.google.com index page at the 2026-06-17 18:00 FLASH sweep 6e04142 and held under 72h FLASH dedup from FLASH-1200 c48f6fc (UNC6508 / INFINITERED PRC-nexus medical/military-health/AI/UAS research espionage cluster). **The 72h dedup window expired at 2026-06-18 12:00 EDT** — body-retrieval is now a collection priority per the orchestrator's PM cycle handoff. URL discovery succeeded this sweep via direct cloud.google.com/blog/topics/threat-intelligence index-page enumeration (slug `prc-targets-us-medical-research` differs from operator-anticipated medical-community-china-nexus path that returned 404 at the 18:00 sweep direct-URL attempt).

## Attribution-claim language (verbatim, per Hard Rule 2 BINDING — no Archimedes-originated cross-walk)

> "UNC6508, a People's Republic of China (PRC)-nexus threat actor"

> "GTIG attributes this activity to UNC6508 with high confidence. This assessment is based on infrastructure overlaps between campaigns, the consistent use of the INFINITERED backdoor on REDCap servers, and the specific targeting of medical research and defense sectors. We assess UNC6508 is an espionage motivated threat cluster, with priorities that align with historic PRC state-sponsored espionage trends and intelligence collection requirements."

> "GTIG assesses these collection priorities are aligned with the strategic interests of the People's Republic of China."

UNC6508 is NOT on `_roster.yaml` 24-actor list. Hard Rule 2 BINDING — Archimedes does NOT cross-walk UNC6508 to Volt Typhoon, Salt Typhoon, APT40, APT41, or any other PRC-attributed roster actor without an independent A-grade source making the specific actor-mapping. GTIG / Mandiant cluster identity is preserved verbatim.

## Victim sector descriptions (verbatim)

> "North American academic, medical, and military research community"

> "diverse set of national, state, and private medical entities"

> "world-renowned clinical providers, premier academic centers, North American military health institutions, professional advocacy groups, and health regulatory bodies"

Research areas of collection priority:

- Molecular discovery and clinical drug trials
- State-level public health policy and military readiness
- **Artificial Intelligence**
- **Uncrewed vehicle systems (UAS)**
- **Cyber offensive programs**
- **National defense intelligence**
- **Indo-Pacific command operations**
- **Medical research (including virology)** — with Chikungunya virus collection interest explicitly linked to July 2025 Guangdong outbreak

## Named victim organizations

**None named publicly in the GTIG report.** Victim descriptors are collective and sector-categorical:

- "Medical research university"
- "North American medical research institution"
- "affected organizations" (collective)

**Zero A&D primes on Archimedes watchlist named** (Lockheed Martin, Boeing, RTX/Raytheon, Northrop Grumman, GD, BAE, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit). The A&D relevance is structural / sector-adjacency — military health institutions + national defense intelligence + AI / UAS / cyber offensive research areas align with DIB workforce / DIB R&D ecosystem rather than DIB primes directly.

## Campaign timeline

- **September 2023:** Initial REDCap server compromise (earliest documented)
- **~December 2023 (3 months post-foothold):** INFINITERED backdoor deployment
- **2024 (full year):** Persistence + credential harvesting + lateral reconnaissance — "remained undetected for a year before accessing internal networks" per the published characterization
- **Post-2024:** Pivot to domain admin via credential replay
- **2025:** "Patroit" [sic] content-compliance rule deployed for email exfiltration
- **July 2025:** Chikungunya outbreak in Guangdong province (China) — surfaces as collection-priority alignment marker
- **November 2025:** Continuing activity through this date (campaign detection / disclosure window)

Per GTIG narrative: "deployed the InfiniteRed backdoor three months after the initial intrusion" and "remained undetected for a year before accessing internal networks." Multi-year dwell consistent with PRC-nexus espionage operational pattern.

## Tradecraft summary

INFINITERED is a **3-component PHP-based modular backdoor** embedded into REDCap server software:

1. **Dropper / upgrade interception:** Injects its own code into new REDCap versions by intercepting the legitimate upgrade process. Self-perpetuating across software updates. Embedded as a `b49e334d-9c01-463e-9bc5-00a6920fb66e` GUID-delimited block in the Upgrade.php file.
2. **Credential harvester:** Hooks the authentication system file. Captures plaintext username + password from POST requests during login; encrypts and stores in a database table prefixed with the `xc32038474a` session-ID marker; 60-day TTL.
3. **Backdoor / C2:** Hooks the custom-hooks system file (executes on every REDCap page load). C2 channel uses the REDCAP-TOKEN HTTP cookie value as the transport. Supports `00` shell_exec, `02` upload, `03` retrieve credentials, `04` delete credentials, `05` arbitrary SQL, `ej671a16i7fd8202nu6ltfg5p6x7u` download file, empty payload = beacon system info.

Post-compromise tradecraft:

- **Credential replay attack** from REDCap-harvested credentials to enterprise administrator account → domain admin pivot
- **Content compliance rule abuse** ("Patroit" rule using regex to match keyword + email-address patterns; silent BCC-forward to attacker-controlled Gmail account `BebitaBarefoot774@gmail.com`) — covert continuous email exfiltration via legitimate cloud productivity-suite feature
- **OBF (obfuscation) network** infrastructure routing — compromised routers + residential proxies + VPS — US-based exit-IPs exclusively for the Gmail access + credential replay portions of the operation
- **YARA rule** published in the report targeting the INFINITERED PHP variants

## IOCs (from ioc-extraction skill output)

```yaml
iocs:
  emails:
    - value: "BebitaBarefoot774@gmail.com"
      context: "Threat-actor-controlled Gmail account dedicated to email-data exfiltration via content compliance rule BCC-forwarding"
      defanged: "BebitaBarefoot774[@]gmail[.]com"
      first_seen: 2025 (per Mandiant narrative)
  
  ipv4:
    - value: "23.169.65.49"
      context: "Compromised ASUS router used as OBF-network exit-IP for administrator-account login and Gmail-account access (US-based exclusively)"
      defanged: "23.169.65[.]49"
  
  sha256:
    - value: "ba6b73b0ca0dc7f86b3b397893ac32d729fd53f9df20643288f141f29d020af7"
      context: "Persistence — help.php web shell file"
      family: INFINITERED
    - value: "db65c1b9f9e4cb4d729f45ad4b6fcf3e277caf9eb4c875425dec93fd883f9136"
      context: "Credential Harvester"
      family: INFINITERED
    - value: "c1ac43d23f89d41eb4ff131678ab562ab2cfed9aa334b13767ef141d303b0e5b"
      context: "Credential Harvester (variant)"
      family: INFINITERED
    - value: "8f0158855a656b629ca76ebca565f18bc25563ded34b65d6771632c20edb68ec"
      context: "Backdoor"
      family: INFINITERED
    - value: "51a57bfc9ed3eb6451c1c289607814d59e1698c666fb97ac5f694c398f23d045"
      context: "Backdoor (variant)"
      family: INFINITERED
    - value: "4efbef69eb3b09bacff892d6a55778d07c418e7f15eba3cf1245e8cdfd8dda0b"
      context: "Dropper"
      family: INFINITERED
    - value: "58bb25777e0aa86bcd2125101e0bca4e8732b03d91bd8d2f205b446a2a8d5c86"
      context: "Dropper (variant)"
      family: INFINITERED
  
  host_artifacts:
    - value: "help.php"
      context: "Web shell file name dropped on compromised REDCap server"
      family: INFINITERED
    - value: "b49e334d-9c01-463e-9bc5-00a6920fb66e"
      context: "INFINITERED current software version GUID delimiter (embedded in Upgrade.php for upgrade-survival injection)"
      family: INFINITERED
    - value: "xc32038474a"
      context: "INFINITERED REDCap database session-ID prefix (marks attacker-harvested credentials in database table)"
      family: INFINITERED
    - value: "ej671a16i7fd8202nu6ltfg5p6x7u"
      context: "INFINITERED magic command tag for arbitrary file download via C2"
      family: INFINITERED
    - value: "Patroit"
      context: "Content-compliance rule name (sic — typo of 'Patriot' per GTIG) used for silent BCC-forward email exfiltration"
      family: tradecraft

attribution_claims:
  - actor: UNC6508
    actor_status: not_on_roster
    confidence_phrase: "with high confidence"
    nation_nexus: PRC
    motivation: espionage
    asserted_by: GTIG / Mandiant
    cross_walk_to_roster: NONE — Hard Rule 2 BINDING; do NOT propagate to Volt Typhoon / Salt Typhoon / APT40 / APT41 / any other PRC roster-tracked actor
  
  - actor_relationship: INFINITERED == UNC6508-attributed bespoke backdoor
    confidence_phrase: "consistent use of the INFINITERED backdoor on REDCap servers"
    asserted_by: GTIG / Mandiant
    cross_walk_to_other_families: NONE asserted by GTIG

mitre_attack_techniques:
  - T1190 Exploit Public-Facing Application — REDCap exploitation
  - T1505.003 Server Software Component: Web Shell — help.php deployment
  - T1554 Compromise Client Software Binary — REDCap upgrade-process interception
  - T1027 Obfuscated Files or Information — Base64-encoded payloads in PHP
  - T1090.003 Proxy: Multi-hop Proxy — OBF networks
  - T1562.001 Impair Defenses: Disable or Modify Tools — silent BCC rules
  - T1689 Downgrade Attack — exploiting legacy REDCap versions
  - T1555 Credentials from Password Stores — local config files
  - T1056.003 Input Capture: Web Portal Capture — POST login credential harvest
  - T1114.003 Email Collection: Email Forwarding Rule — Patroit content-compliance rule
  - T1213 Data from Information Repositories — strategic-keyword search
  - T1071.001 Application Layer Protocol: Web Protocols — REDCAP-TOKEN cookie C2
  - T1567 Exfiltration Over Web Service — BCC-forward to Gmail
```

## Why this matters for the afternoon brief

**Substrate-pivot UPDATE candidate** for the 2026-06-18 afternoon brief:

1. **Body substantiation** of the previously title-only 72h-dedup-held Mandiant primary on UNC6508/INFINITERED PRC-nexus medical-research espionage cluster — dedup window closed at 12:00 EDT, body now available.
2. **Concurrent net-new SecurityWeek-Arghire 2026-06-18 17:07 UTC publication** as second-publisher relay establishing this as a multi-publisher cluster (see raw-2026-06-18-pm-002). Arghire surfaces specifically the **outdated REDCap exposure scan data** — ~8,500 internet-exposed REDCap instances globally, 40% in US, ~30% running version 16.0.17 versus latest 17.1.3 (1.18%). This is the **vulnerability-exposure dimension** Mandiant did NOT enumerate; the two publications are complementary rather than restating-the-same.
3. **Operational A&D relevance** is structural — military health institutions + national defense intelligence collection-priority + AI / UAS / cyber-offensive research areas align with DIB workforce + DIB R&D ecosystem rather than DIB primes directly. **Zero A&D primes named.** Frank's deployment is NOT a North American medical research institution running REDCap per operator setup — first-party visibility-bounded absence is consistent with 100% UNC6508 victim profile.
4. **Hard Rule 2 BINDING** — UNC6508 NOT on `_roster.yaml`. Operator-deferred `/new-actor` candidacy noted; cross-walk to Volt Typhoon / Salt Typhoon / APT40 / APT41 is BLOCKED without independent A-grade attribution mapping.
5. **WEP candidate framing** (for grader/red-team):
   - GTIG-attributed campaign identity → **very likely** (single-A-IR-vendor with high-confidence assertion + named tradecraft + named IOCs)
   - INFINITERED == UNC6508 bespoke malware → **likely** (single-vendor on cluster-malware identity layer)
   - PRC state-sponsorship → **likely** (consistent with PRC pattern + collection-priority alignment; verbatim GTIG framing)
   - A&D-DIB direct targeting → **roughly even chance** (sector-adjacent; military health + research areas only; no DIB-prime named victims)

## Quote budget reservations (Hard Rule 6, 15-word cap, 1-per-source ceiling — for briefer)

Candidate at-cap quotes from this article (briefer chooses ONE for the brief, NOT raw-signaled here for citation):

- "GTIG attributes this activity to UNC6508 with high confidence" (8 words) — attribution preface
- "UNC6508, a People's Republic of China (PRC)-nexus threat actor" (8 words) — cluster identity
- "world-renowned clinical providers, premier academic centers, North American military health institutions" (12 words) — victim-sector framing (BEST candidate for brief)
- "an espionage motivated threat cluster, with priorities that align with historic PRC" (12 words) — motivation framing
- "the InfiniteRed backdoor three months after the initial intrusion" (9 words) — tradecraft framing

## Extraction notes

- Language: en
- Publisher byline: Patrick Whitsell, John McGuiness
- Article type: vendor IR-blog research (Mandiant / GTIG)
- Raw IOC extraction invoked: yes (12 distinct IOCs across 4 types — 1 email, 1 IPv4, 7 SHA256, 3 host artifacts + 1 tradecraft string + 13 MITRE techniques)
- Publication date back-dated: article timestamp 2026-06-15 (3.5 days before this retrieval); first surfaced to Archimedes via Mandiant index-page enumeration at 2026-06-17 18:00 FLASH 6e04142 as title-only; 72h FLASH dedup window from FLASH-1200 c48f6fc held substrate until 2026-06-18 12:00 EDT; body-retrieval URL slug discovery succeeded this sweep.
