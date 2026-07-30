---
raw_id: raw-2026-07-30-pm-002
collected_at: 2026-07-30T15:45:00-04:00
run_id: pre-brief-20260730-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: the-record
  source_name: "The Record (Recorded Future News) — relaying AhnLab + four South Korean agencies"
  source_url: https://therecord.media/north-korea-hackers-ransomware
  published_at: 2026-07-30T10:00:00-04:00
match_reason:
  watchlist: [aerospace-defense]   # Korean defense-company spearphishing lure (GaN semiconductor survey) — sector-adjacent
  actors: ["003"]                  # Lazarus Group
  vulnerabilities: []
  keywords: [Lazarus, Gunra, ransomware, "Operation Double Barrel", DPRK, GaN semiconductor, defense]
triage_tags: [non_flash, tracked_actor, dprk, ransomware_nexus, ad_sector_adjacent, grader_queue, tracked_actor_ttp]
iocs_extracted: true
iocs_count: 3
text_word_count: 360
promoted: true
promoted_to_finding: finding-2026-07-30-0006
promoted_at: 2026-07-30T16:18:00-04:00
grading_run_id: afternoon-20260730-160000
ttl_expires_at: 2026-10-28T15:45:00-04:00
---

# South Korean agencies warn: Lazarus Group tools / infrastructure shared with Gunra ransomware operators (Operation Double Barrel)

**Originating primaries:** AhnLab + **four South Korean security and intelligence agencies**
(joint advisory; specific agency names not enumerated in the relay). **Relay (in-window):** The
Record, 2026-07-30 ~10:00 EDT. Originating advisory / AhnLab primary NOT directly retrieved this
sweep.

The advisory reports **overlapping technical indicators between North Korea's Lazarus Group and the
Gunra ransomware operation**, evidence of deepening entanglement between Pyongyang-backed hackers
and the ransomware ecosystem. Reported overlaps:

- Identical malware filenames and execution arguments
- Same privilege-escalation tools
- Same command-and-control servers
- Same SSH key fingerprint
- Identical file-deletion method (renaming files to random four-character strings)

All exploited vulnerabilities in **Korean financial-security software products**. Campaign named
**"Operation Double Barrel."**

**Gunra ransomware:** emerged April 2025, built on leaked **Conti v2** source code, claimed ≥32
victims by March 2026. Prior DPRK links previously identified with **Play, Qilin, and Medusa**
ransomware operations (2024–2025). Per the advisory, Lazarus installed backdoors in **≥72
organizations in 2026** alone. Victim sectors: South Korean government agencies, cryptocurrency
exchanges, IT service providers, healthcare, manufacturing.

**A&D-relevant detail:** one targeted email campaign in the advisory involved **spearphishing a
Korean defense company using GaN (gallium-nitride) semiconductor survey lures.** GaN is a defense
RF/radar-relevant material class; this is the sharpest A&D-adjacent datum in the report (single
named defense-sector target, non-US). Recorded for grader/briefer awareness — **no US A&D prime
named.**

**Attribution language (preserve verbatim, Hard Rule 2):** AhnLab **"stopped short of definitively
attributing both campaigns to the same actor,"** classifying the findings as **"a high likelihood
of technical linkage"** requiring continued investigation. Lazarus Group = **roster #003**.

---

## Extraction notes

- Language: en
- Publisher byline: The Record (no byline)
- Article type: news (national-CERT / vendor joint-advisory relay)
- Raw IOC extraction invoked: yes
- Copyright: <15 words quoted per source (Hard Rule 6). No credential values present (Hard Rule 7)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: campaign_name
    value: "Operation Double Barrel"
    context: "AhnLab / SK-agency joint-advisory designation for the Lazarus <-> Gunra overlap campaign"
    confidence: reported
  - type: malware_family
    value: "Gunra ransomware"
    context: "Conti v2 source-code lineage; emerged Apr 2025; >=32 victims by Mar 2026; technical overlap with Lazarus tooling"
    confidence: reported
  - type: ttp
    value: "file-deletion via rename to random 4-character strings"
    context: "shared anti-forensics method cited as a Lazarus<->Gunra technical-linkage indicator"
    confidence: reported
# Atomic IOCs (C2 IPs/domains, SSH key fingerprint value, malware hashes/filenames) referenced
# qualitatively but NOT provided as values in the relay layer — pending direct retrieval of the
# AhnLab / SK-agency primary. No credentials present.
attribution_claims:
  - actor: "Lazarus Group"
    nation: "North Korea (DPRK) / Reconnaissance General Bureau"
    claimed_by: "AhnLab + four South Korean security & intelligence agencies (joint advisory)"
    language: "'stopped short of definitively attributing both campaigns to the same actor'; 'a high likelihood of technical linkage'"
    confidence_source: "national-CERT-class joint advisory + AV-vendor research (relay-level)"
    roster_match: "#003 Lazarus Group"
    note: "Recorded verbatim per Hard Rule 2. The Lazarus<->Gunra linkage is EXPLICITLY hedged by AhnLab — do not upgrade."
  - actor: "Gunra ransomware operators"
    nation: "unattributed (ransomware ecosystem; DPRK-linkage under investigation)"
    prior_dprk_ransomware_links: [Play, Qilin, Medusa]
    claimed_by: "AhnLab / SK agencies"
    note: "Gunra not a roster actor; recorded as ransomware-nexus context only."
```
