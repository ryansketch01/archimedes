---
raw_id: raw-2026-05-06-flash-1200-001
collected_at: 2026-05-06T12:05:00-04:00
run_id: flash-sweep-20260506-120000
collection_mode: flash_sweep
sources:
  - source_yaml_id: bleepingcomputer
    source_name: BleepingComputer
    source_url: https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/
    grade: B
    role: relay
    published_at: 2026-05-06T09:02:52-04:00
  - source_yaml_id: securityweek
    source_name: SecurityWeek
    source_url: https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/
    grade: B
    role: relay
    published_at: 2026-05-06T09:00:00-04:00
  - source_yaml_id: rapid7-blog
    source_name: Rapid7
    source_url: https://www.rapid7.com/blog/
    grade: B
    role: originating
    published_at: 2026-05-06T09:00:27-04:00
    note: |
      Rapid7 not currently in source-grades.yaml. Provisionally treat as A-grade
      vendor research equivalent (peer of Mandiant/Unit42/CrowdStrike for
      incident-response forensics). Grader to assign formal grade.
match_reason:
  watchlist: []
  actors: ["022"]
  actor_names: [MuddyWater, Mango Sandstorm, Static Kitten, Mercury, Seedworm]
  vulnerabilities: []
  keywords: [iran, mois, false-flag, chaos-ransomware, microsoft-teams, code-signing, donald-gay-cert]
flash_triggers_evaluated:
  trigger-1-critical-cve-exploited:
    fires: false
    reason: "No CVE component"
  trigger-2-tracked-actor-attribution:
    fires: true
    detail: |
      Rapid7 attributes new campaign to MuddyWater (#022 in _roster.yaml,
      IR / MOIS) with "moderate confidence." Attribution language quoted
      verbatim: "moderate confidence in attributing the incident to
      MuddyWater." This is a NEW campaign attribution (Game.exe RAT, Donald
      Gay code-signing cluster, US construction/manufacturing/business-
      services targeting), not a restatement of prior MuddyWater attribution.
      MuddyWater profile is "pending" in roster — first profile-relevant
      Rapid7 intel since tracking began.
  trigger-3-first-party-ioc-hit:
    fires: false
    reason: |
      Splunk query (-24h) across archimedes + defenseclaw_local indices
      against tracked-IOC list returned 0 events. New IOCs in this report
      (moonzonet[.]com, uploadfiler[.]com, adm-pulse[.]com,
      77.110.107.235, 93.123.39.127, 172.86.126.208, 116.203.208.186,
      Donald Gay cert thumbprint B674578D4BDB24CD58BF2DC884EAA658B7AA250C,
      9 SHA256 hashes) are not yet in _master-index.yaml so cannot be
      checked retroactively against historical telemetry — librarian/
      vuln-tracker handoff: ingest IOCs and run -30d sweep.
  trigger-4-tracked-actor-ttp-change:
    fires: true
    detail: |
      A-equivalent grade source (Rapid7 incident response) documents new
      tooling, new tradecraft, and new C2 infrastructure clearly attributable
      to a tracked roster actor:
        - NEW TOOLING: Game.exe custom RAT (12-command backdoor, masquerades
          as Microsoft WebView2; SHA256 1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6)
        - NEW TRADECRAFT: Interactive Microsoft Teams screen-share for live
          credential harvest + MFA manipulation via attacker-controlled device
          addition; "false flag" Chaos ransomware masquerade with NO actual
          encryption (extortion-only, fake DLS hptqq2o2qjva7lcaaq67w36jihzivkaitkexorauw7b2yul2z6zozpqd[.]onion)
        - NEW INFRA: moonzonet[.]com (ms_upd.exe C2), uploadfiler[.]com
          (Game.exe C2), adm-pulse[.]com (Quick Assist phishing); IPs
          77.110.107.235, 93.123.39.127 (Teams source), 172.86.126.208
          (ms_upd hosting), 116.203.208.186 (pythonw.exe contact)
        - NEW CODE-SIGNING ABUSE: "Donald Gay" Microsoft ID Verified CS AOC
          CA 02 cert (thumbprint B674578D4BDB24CD58BF2DC884EAA658B7AA250C),
          time-invalid/revoked shortly post-deployment
  trigger-5-ad-sector-campaign:
    fires: false
    reason: |
      Victim sectors named: construction, manufacturing, business services,
      predominantly US. NO aerospace, defense, or A&D-watchlist entity
      named. Manufacturing is sector-adjacent but not A&D-direct.
  trigger-6-zero-day-no-patch:
    fires: false
    reason: "No CVE / no vulnerability component"
triage_tags:
  - flash_candidate
  - trigger-2-tracked-actor-attribution
  - trigger-4-tracked-actor-ttp-change
  - tracked_actor
  - iran
  - mois
  - false-flag-ransomware
  - microsoft-teams-abuse
  - code-signing-abuse
  - profile-pending-actor
iocs_extracted: true
iocs_count: 19
text_word_count: 0
promoted: true
promoted_to_finding: finding-2026-05-06-FLASH-0002
promoted_at: 2026-05-06T12:18:00-04:00
ttl_expires_at: 2026-08-04T12:05:00-04:00
anti_noise_check:
  topic_fingerprint: muddywater-chaos-rapid7-2026-05-06
  prior_24h_match_in_raw_signal: false
  prior_24h_match_in_coverage_log: false
  prior_24h_match_in_flash_queue: false
  conflict: none
---

# MuddyWater hackers use Chaos ransomware as a decoy in attacks

## Source items

### Primary source — Rapid7 (originating research)

**Title:** MuddyWater operation — Iranian APT intrusion masquerading as Chaos
ransomware (Rapid7 incident-response report, 2026-05-06).
**URL:** https://www.rapid7.com/blog/ (specific post URL via aggregator).
**Published:** 2026-05-06 ~09:00 EDT.

Rapid7 attributes a recent intrusion against an unnamed organization to
MuddyWater (also tracked as Mango Sandstorm / Static Kitten / Mercury /
Seedworm), an Iranian Advanced Persistent Threat affiliated with the
Iranian Ministry of Intelligence and Security (MOIS). Confidence:
**moderate**. Rapid7 attribution language (verbatim, single quote, 9 words):
"moderate confidence in attributing the incident to MuddyWater." Per Hard
Rule 6 (15-word quote limit, one quote per source).

The intrusion combined social engineering, persistence, credential
harvesting, and data theft — packaged behind a Chaos ransomware false-flag
without actual file encryption. Rapid7 assesses the ransomware artifacts
were deployed to obscure cyber-espionage intent. Sectors named:
**construction, manufacturing, business services**. Geography:
**predominantly United States**, with prior MENA targeting in Operation
Olalampo referenced as historical context. NO aerospace, defense,
government, or A&D-watchlist entity named as victim in this incident.

### Secondary relay — SecurityWeek (B-grade)

**Title:** "Iranian APT Intrusion Masquerades as Chaos Ransomware Attack."
**Published:** 2026-05-06 09:00 EDT.
**URL:** https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/

SecurityWeek paraphrases Rapid7's report; not independent corroboration.
Reproduces Rapid7 confidence assessment and US targeting framing.

### Secondary relay — BleepingComputer (B-grade)

**Title:** "MuddyWater hackers use Chaos ransomware as a decoy in attacks."
**Published:** 2026-05-06 09:02 EDT.
**URL:** https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/

BleepingComputer relays Rapid7's report. Reproduces attribution language.
No independent telemetry. Confirms tooling names: ms_upd.exe, Game.exe,
Stagecomp, Darkcomp.

---

## Extraction notes

- Language: en
- Article type: vendor incident-response report (Rapid7) + media relays (SecurityWeek, BleepingComputer)
- Originating researcher: Rapid7 (incident response engagement, named victim withheld)
- Independence: SINGLE EFFECTIVE SOURCE (Rapid7). Both media items relay the
  same incident-response narrative; do not constitute independent
  corroboration per INTEL-GRADING.md single-source veto rule.
- Tracked actor match: MuddyWater (#022) — primary_name match; alias
  matches on Mango Sandstorm, Static Kitten, Mercury, Seedworm.
- Profile status: MuddyWater profile listed `tracked_since: null` and
  `note: "Profile pending"` in `_roster.yaml`. This raw-signal item is
  the first substantive Rapid7-grade intel against the actor since
  intake — actor-profiler handoff candidate for first-pass profile.
- Hard Rule 2 honored: All attribution carried EXACTLY as Rapid7 stated
  ("moderate confidence in attributing the incident to MuddyWater"). No
  origination by Archimedes. MOIS service affiliation reproduced from
  Rapid7's text (which itself cites US Government attribution of
  MuddyWater to MOIS as background).
- Quote discipline (Hard Rule 6): one verbatim quote per source max.
  Rapid7 quote selected: "moderate confidence in attributing the incident
  to MuddyWater" (9 words). All other content paraphrased.
- Single-source veto candidate: WEP cap "likely" expected at grading per
  INTEL-GRADING.md if grader confirms only Rapid7 is originating.

## IOCs (extracted from Rapid7 reporting)

```yaml
iocs:
  sha256:
    - value: 24857fe82f454719cd18bcbe19b0cfa5387bee1022008b7f5f3a8be9f05e4d14
      filename: ms_upd.exe
      role: malware_loader
      attribution_claim: MuddyWater per Rapid7
    - value: 1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6
      filename: Game.exe
      role: custom_rat
      malware_family: Darkcomp (Rapid7 internal name)
      note: 12-command backdoor; masquerades as Microsoft WebView2
      attribution_claim: MuddyWater per Rapid7
    - value: 3df9dcc45d2a3b1f639e40d47eceeafb229f6d9e7f0adcd8f1731af1563ffb90
      filename: WebView2.exe
      role: legitimate_binary_repurposed
      attribution_claim: MuddyWater per Rapid7
    - value: c86ab27100f2a2939ac0d4a8af511f0a1a8116ba856100aae03bc2ad6cb0f1e0
      filename: visualwincomp.txt
      role: payload_or_config
      attribution_claim: MuddyWater per Rapid7
    - value: a47cd0dc12f0152d8f05b79e5c86bac9231f621db7b0e90a32f87b98b4e82f3a
      filename: WebView2Loader.dll
      role: dll_sideload
      attribution_claim: MuddyWater per Rapid7
    - value: cd098eddb23f2d2f6c42271ca82803b0d5ac950cb82a9b8ae0928e83945a53df
      filename: dwagent.exe
      role: legitimate_remote_access_tool
      note: DWAgent abused for persistence
      attribution_claim: MuddyWater per Rapid7
    - value: a3bac548b5bc91c526b4d6707623ddbd1a675aa952f0d1f9a0aa6f7230f09f23
      filename: dwagsvc.exe
      role: legitimate_remote_access_tool
      attribution_claim: MuddyWater per Rapid7
    - value: 86e0197389f0573eb83ff53991f337d416124c7c8bd727721ef3d396cd5f65d
      filename: dwaglnc.exe
      role: legitimate_remote_access_tool
      attribution_claim: MuddyWater per Rapid7
    - value: bfc1675ee1e358db8356f515aaded7962923e426aa0a0a1c0eddfc4dab053f89
      filename: AnyDesk.exe
      role: legitimate_remote_access_tool
      attribution_claim: MuddyWater per Rapid7

  domain:
    - value: moonzonet[.]com
      role: c2
      malware: ms_upd.exe
      attribution_claim: MuddyWater per Rapid7
    - value: uploadfiler[.]com
      role: c2
      port: 443
      malware: Game.exe / Darkcomp
      attribution_claim: MuddyWater per Rapid7
    - value: adm-pulse[.]com
      role: phishing
      note: Quick Assist phishing infrastructure
      attribution_claim: MuddyWater per Rapid7

  ipv4:
    - value: 77.110.107.235
      role: source_ip
      note: Microsoft Teams social engineering source
      attribution_claim: MuddyWater per Rapid7
    - value: 93.123.39.127
      role: source_ip
      note: Microsoft Teams social engineering source
      attribution_claim: MuddyWater per Rapid7
    - value: 172.86.126.208
      role: hosting
      note: ms_upd.exe hosting
      attribution_claim: MuddyWater per Rapid7
    - value: 116.203.208.186
      role: contact
      note: pythonw.exe outbound contact
      attribution_claim: MuddyWater per Rapid7

  onion:
    - value: hptqq2o2qjva7lcaaq67w36jihzivkaitkexorauw7b2yul2z6zozpqd[.]onion
      role: chaos_dls_facade
      attribution_claim: MuddyWater per Rapid7

  code_signing_certificate:
    - subject_name: Donald Gay
      issuer: Microsoft ID Verified CS AOC CA 02
      thumbprint: B674578D4BDB24CD58BF2DC884EAA658B7AA250C
      status: time-invalid (revoked shortly after deployment)
      role: malware_signing
      attribution_claim: MuddyWater per Rapid7

attribution_claims:
  - actor: MuddyWater
    aliases_invoked: [Mango Sandstorm, Static Kitten, Mercury, Seedworm]
    nation: IR
    service: MOIS
    confidence_per_source: moderate
    source: Rapid7 (originating)
    independent_corroboration: false
    relays:
      - SecurityWeek (paraphrase)
      - BleepingComputer (paraphrase)

ttp_changes_documented_vs_prior:
  new_tooling:
    - Game.exe / Darkcomp custom RAT (12-command backdoor, MS WebView2 masquerade)
  new_tradecraft:
    - Interactive Microsoft Teams screen-sharing for live credential harvest
    - MFA manipulation via attacker-controlled device addition
    - Chaos ransomware "false flag" deployment WITHOUT actual encryption
    - Fake leak-site (DLS) onion address used as extortion theater
  new_infrastructure:
    - moonzonet[.]com, uploadfiler[.]com, adm-pulse[.]com domains
    - IPs in 77.110.107.x, 93.123.39.x, 172.86.126.x, 116.203.208.x ranges
  new_code_signing_abuse:
    - Donald Gay code-signing cert cluster (Microsoft ID Verified CS AOC CA 02)
  historical_continuity_observed:
    - pythonw.exe code injection into suspended processes (known TTP)
    - "IT Support" persona via Teams (consistent with prior reporting)
    - Operation Olalampo branding overlap (historical campaign)
    - Code-signing cluster patterns (Donald Gay / Amy Cherne lineage)
```

## A&D relevance assessment (raw — for grader)

- **Direct A&D mention:** none. No watchlist entity named.
- **Sector adjacency:** "manufacturing" named by Rapid7 as a victim sector;
  US defense industrial base (DIB) overlaps with manufacturing but is NOT
  the same set. Rapid7 does not specify defense manufacturing.
- **Mechanism transfer risk:** Microsoft Teams interactive screen-share
  social engineering is platform-generic; M365 / Teams is universal across
  US primes and DIB tier-1/2 suppliers. The TTP is portable. Forward
  reasoning only — no observed prime-direct activity.
- **Iran-actor watch:** MuddyWater is Iran/MOIS. Iran Cyber Watch posture
  per recent briefs has been "no new activity in last 48h" — this changes
  that. Brief should reflect.

## Tripwires for re-grade up

- Independent A/B-grade vendor (Mandiant, Unit42, MSTIC, CrowdStrike)
  publishing corroborating attribution → lifts single-source veto, may
  allow "very likely" WEP.
- A US prime, DIB tier-1, or watchlist entity disclosed as victim.
- KEV addition of any associated CVE (none in current report).
- First-party Splunk hit on any of the 19 IOCs once ingested into
  _master-index.yaml.

## Anti-noise / FLASH-policy notes

- Topic fingerprint: muddywater-chaos-rapid7-2026-05-06.
- 24h prior coverage check: no MuddyWater entries in `_coverage-log.yaml`
  for the past 24h. Yesterday's afternoon brief covered
  finding-2026-05-05-0007 (MSTIC AitM, unattributed) and
  finding-2026-05-05-0008 (DAEMON Tools supply chain, no actor named) —
  neither overlaps MuddyWater. No 24h topic lock applies to this raw signal.
- Critical-override evaluation: NOT MET.
  - CVSS 10.0 required: N/A (no CVE).
  - Active exploitation required: yes (incident-response).
  - Tracked actor required: yes (MuddyWater #022).
  - A&D watchlist entity targeted: NO (no watchlist entity named).
  Conditions met: 2 of 4. Standard quiet-hours rules govern (irrelevant
  here — 12:00 EDT is inside active hours).
- FLASH disposition: candidate is INSIDE active hours (09:00–21:00 EDT
  per FLASH-POLICY); if grader/red-team approve, briefer composes FLASH
  for immediate post to #flash-alerts. WEP expected to cap at "likely"
  under single-source veto pending independent corroboration.
