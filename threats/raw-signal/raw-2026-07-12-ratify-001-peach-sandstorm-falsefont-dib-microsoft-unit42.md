---
raw_id: raw-2026-07-12-ratify-001
collected_at: 2026-07-12T14:35:00-04:00
run_id: ondemand-ratify-peach-sandstorm-20260712
collection_mode: on_demand
on_demand_command: dossier-ratification (collector direct-retrieval intake)
source:
  - source_yaml_id: microsoft-mstic
    source_name: Microsoft Threat Intelligence (MSTIC / Security Blog)
    source_url: https://thehackernews.com/2023/12/microsoft-warns-of-new-falsefont.html
    published_at: 2023-12-21
    note: "Microsoft's Dec 2023 FalseFont disclosure was a short MSTIC advisory/tweet; relayed here via THN + SecurityWeek + BleepingComputer. Primary originator = Microsoft."
  - source_yaml_id: unit42-paloalto
    source_name: Palo Alto Networks Unit 42
    source_url: https://unit42.paloaltonetworks.com/curious-serpens-falsefont-backdoor/
    published_at: 2024-03-25
    note: "Unit 42 full technical analysis of FalseFont (tracks actor as Curious Serpens = APT33/Peach Sandstorm). Retrieved cleanly."
  - source_yaml_id: nextron-systems
    source_name: Nextron Systems (Florian Roth et al.)
    source_url: https://www.nextron-systems.com/2024/01/29/analysis-of-falsefont-backdoor-used-by-peach-sandstorm-threat-actor/
    published_at: 2024-01-29
    note: "Independent technical analysis + YARA/Sigma. Referenced, not fully fetched."
match_reason:
  watchlist: [aerospace-defense]
  actors: [Peach Sandstorm, APT33, Curious Serpens, HOLMIUM, Refined Kitten, Elfin]
  vulnerabilities: []
  keywords: [FalseFont, Defense Industrial Base, DIB, Maxar, aerospace, IRGC]
triage_tags: [dossier_ratification, ad_sector, actor_peach_sandstorm_027, ioc_bearing]
iocs_extracted: true
iocs_count: 6
text_word_count: 1100
promoted: false
ttl_expires_at: 2026-10-10T14:35:00-04:00
admiralty_note: "Collector source-reliability read (advisory only; grader owns final digraph): Microsoft MSTIC A1; Unit 42 A1; Nextron A2/B1. Multi-A-grade, no single-source veto. Attribution reported per source, not originated (Hard Rule 2)."
---

# Peach Sandstorm (APT33) FalseFont backdoor vs the Defense Industrial Base — Microsoft (Dec 2023), corroborated by Unit 42 (Mar 2024) and Nextron (Jan 2024)

## Summary of retrievable reporting

Microsoft Threat Intelligence disclosed in December 2023 that the Iranian nation-state actor **Peach Sandstorm** (formerly HOLMIUM; also APT33, Elfin, Refined Kitten) attempted to deliver a newly developed custom backdoor, **FalseFont**, to individuals working for organizations in the **Defense Industrial Base (DIB)** sector. Microsoft first observed FalseFont in use in **early November 2023**. Microsoft assesses the activity supports intelligence collection on behalf of Iranian state interests, and states the development/use of FalseFont is "consistent with Peach Sandstorm activity observed by Microsoft over the past year." Microsoft Defender detects it as `Backdoor:MSIL/FalseFont.A!dha`.

Palo Alto **Unit 42** published a full technical analysis in March 2024, tracking the actor as **Curious Serpens** (their name for APT33/Peach Sandstorm). Unit 42 details FalseFont's capabilities: process/command execution, file manipulation, screenshot capture, browser-credential harvesting, and — notably — theft of credentials "for an aerospace-industry job application platform." The backdoor impersonates a legitimate application from US defense/intelligence/aerospace contractor **Maxar Technologies** (the malicious sample is named `Maxar.dll`). It communicates via periodic polling or real-time SignalR channels.

**Nextron Systems** (Florian Roth) published independent analysis plus YARA/Sigma detection content in January 2024.

## Priority-item confirmation

- **FalseFont backdoor vs the DIB (Microsoft, ~Dec 2023): CONFIRMED.** Microsoft MSTIC, Dec 2023, first-seen early Nov 2023, DIB-sector targeting. Corroborated independently by Unit 42 (A1) and Nextron (A2). Multi-A-grade — no single-source veto.

---

## Extraction notes

- Language: en
- Article type: vendor advisory (Microsoft) + vendor technical blog (Unit 42) + independent analysis (Nextron)
- Publisher bylines: Microsoft Threat Intelligence; Unit 42; Florian Roth / Nextron
- Raw IOC extraction invoked: yes
- Hard Rule 2 (no origination): attribution to APT33/Peach Sandstorm reported exactly as the vendors state it. Archimedes originates nothing.
- Hard Rule 3 (no exploit content): no PoC/exploit material present or copied.
- Hard Rule 7 (credentials radioactive): Unit 42's page published malware-embedded C2 authentication credentials (a hardcoded username + password the implant uses to authenticate to its own C2). Recorded as exposure metadata only — values NOT stored.

### VirusTotal sanity-check (collector enrichment)

- `364275326bbfc4a3b89233dabdaf3230a3d149ab774678342a40644ad9f8d614` — VT: **41/71 malicious**, `type: Win32 EXE`, `meaningful_name: Maxar.dll`, first submitted 2024-01-05, size ~191 MB (padded/overlay). Flagged by Microsoft, Paloalto, Kaspersky, ESET, Symantec, CrowdStrike-adjacent engines. MD5 `6fd5d31d607a212c6f7651c79e7655a3`, SHA1 `ddd18e208aff7b00a46e06f8d9485f81ff4221ea`. Confirms the Maxar-impersonation narrative.

### credential_exposure_detected

```yaml
credential_exposure_detected:
  source: unit42-paloalto
  type: malware_embedded_c2_auth
  count: 1
  stored_value: false
  notes: "LEGAL-POLICY Data Handling / Hard Rule 7: FalseFont's hardcoded C2 auth username+password published by Unit 42 counted and discarded; not victim credentials."
```

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: microsoft-mstic-falsefont-2023-12
  source_url: https://unit42.paloaltonetworks.com/curious-serpens-falsefont-backdoor/
  extracted_at: 2026-07-12T14:35:00Z
  extracted_by: collector
  target_actor_id: "027"
  text_word_count: 1100

indicators:
  - id: peach-hash-364275326bbf
    type: hash_sha256
    value: 364275326bbfc4a3b89233dabdaf3230a3d149ab774678342a40644ad9f8d614
    defanged_original: null
    first_seen: 2023-11
    last_seen: 2024-01
    role: delivery
    campaign: "FalseFont / DIB targeting"
    related_malware: [FalseFont]
    source_brief: unit42-curious-serpens-2024-03
    context_excerpt: "Packed FalseFont executable impersonating Maxar Technologies app (Maxar.dll); VT 41/71 malicious."
    attribution_in_text: "APT33 / Peach Sandstorm / Curious Serpens"
    notes: "MD5 6fd5d31d607a212c6f7651c79e7655a3; SHA1 ddd18e208aff7b00a46e06f8d9485f81ff4221ea"
  - id: peach-hash-4145e792c9e9
    type: hash_sha256
    value: 4145e792c9e9f3c4e80ca0e290bd7568ebcef678affd68d9b505f02c6acaab12
    defanged_original: null
    first_seen: 2023-11
    last_seen: 2024-03
    role: delivery
    campaign: "FalseFont / DIB targeting"
    related_malware: [FalseFont]
    source_brief: unit42-curious-serpens-2024-03
    context_excerpt: "Unpacked FalseFont executable (per Unit 42)."
    attribution_in_text: "Curious Serpens / APT33"
    notes: null
  - id: peach-domain-digitalcodecrafters
    type: domain
    value: digitalcodecrafters.com
    defanged_original: "Digitalcodecrafters[.]com"
    resolved_ip: 64.52.80.30
    first_seen: 2023-11
    last_seen: 2024-03
    role: c2
    campaign: "FalseFont / DIB targeting"
    related_malware: [FalseFont]
    source_brief: unit42-curious-serpens-2024-03
    context_excerpt: "FalseFont C2 domain (Unit 42), resolving to 64.52.80[.]30 on TCP 8080."
    attribution_in_text: "Curious Serpens / APT33"
    notes: null
  - id: peach-ip-64-52-80-30
    type: ipv4
    value: 64.52.80.30
    defanged_original: "64.52.80[.]30"
    first_seen: 2023-11
    last_seen: 2024-03
    role: c2
    campaign: "FalseFont / DIB targeting"
    related_malware: [FalseFont]
    source_brief: unit42-curious-serpens-2024-03
    context_excerpt: "FalseFont C2 IP (Unit 42), TCP 8080."
    attribution_in_text: "Curious Serpens / APT33"
    notes: null
  - id: peach-filename-maxar-dll
    type: other
    type_detail: filename
    value: Maxar.dll
    defanged_original: null
    first_seen: 2023-11
    last_seen: 2024-01
    role: delivery
    campaign: "FalseFont / DIB targeting"
    related_malware: [FalseFont]
    source_brief: unit42-curious-serpens-2024-03
    context_excerpt: "FalseFont impersonates a Maxar Technologies application; sample named Maxar.dll."
    attribution_in_text: "APT33 / Peach Sandstorm"
    notes: null
  - id: peach-detname-falsefont-a-dha
    type: yara_rule
    value: "Backdoor:MSIL/FalseFont.A!dha"
    defanged_original: null
    first_seen: 2023-12
    last_seen: 2023-12
    role: ambiguous
    campaign: "FalseFont / DIB targeting"
    related_malware: [FalseFont]
    source_brief: microsoft-mstic-falsefont-2023-12
    context_excerpt: "Microsoft Defender detection name for FalseFont."
    attribution_in_text: "Peach Sandstorm"
    notes: "Vendor detection signature name, not a filesystem IOC."

attribution_claims:
  - claimed_actor: "Peach Sandstorm (APT33 / Curious Serpens)"
    ioc_ids:
      - peach-hash-364275326bbf
      - peach-hash-4145e792c9e9
      - peach-domain-digitalcodecrafters
      - peach-ip-64-52-80-30
      - peach-filename-maxar-dll
    claimed_by_source: microsoft-mstic-falsefont-2023-12
    attribution_confidence_in_source: high
    requires_grading: true
  - claimed_actor: "Curious Serpens (= APT33 / Peach Sandstorm per Unit 42)"
    ioc_ids:
      - peach-domain-digitalcodecrafters
      - peach-ip-64-52-80-30
    claimed_by_source: unit42-curious-serpens-2024-03
    attribution_confidence_in_source: high
    requires_grading: true

benign_filtered:
  - value: microsoft.com
    reason: reference_site
  - value: attack.mitre.org
    reason: reference_site

extraction_warnings:
  - type: credential_in_source
    ioc_id: null
    detail: "Unit 42 page contains malware-embedded C2 auth username/password. Counted, values discarded per Hard Rule 7. Not extracted as IOCs."
```
