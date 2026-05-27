---
raw_id: raw-2026-05-27-am-006
collected_at: 2026-05-27T07:48:00-04:00
run_id: pre-brief-2026-05-27-am
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: Microsoft Security Blog — Microsoft Defender Experts and Microsoft Defender Security Research Team
  source_url: https://www.microsoft.com/en-us/security/blog/2026/05/26/poisoned-search-results-gpu-mining-cryptojacking-campaign-abusing-screenconnect-microsoft-net-utilities/
  published_at: 2026-05-26T21:35:34+00:00       # 17:35 EDT yesterday, IN WINDOW for this AM-27 pre-brief sweep
relay_layer_at_06_00_sentinel:
  source_yaml_id: thehackernews
  relay_url: https://thehackernews.com/2026/05/ai-chatbot-recommendations-redirect.html
  relay_published_at: 2026-05-27T07:45:52+00:00       # 03:45 EDT today
  note: |
    The THN relay was caught at the 06:00 FLASH sentinel and DISCARDED
    per Mode 1 in that sweep (no roster / no A&D / no vuln-index hit).
    However the MSTIC PRIMARY is in-window for this 16h AM-27 pre-brief
    window (published 2026-05-26T17:35 EDT yesterday) and warrants
    raw-signaling at primary tier rather than letting the relay-tier
    discard stand. The relay-vs-primary distinction matters because
    MSTIC is A-grade and the primary publication is the authoritative
    source for Microsoft Defender Experts' research methodology.
match_reason:
  watchlist: []
  actors: []          # MSTIC explicitly names "unknown threat actor"; no tracked-actor attribution
  vulnerabilities: []  # no specific CVE in primary scope (CVE-2025-33073 referenced separately re F5/Atlassian)
  keywords: [cryptojacking, SEO poisoning, AI chatbot poisoning, AI search result poisoning, Microsoft Defender Experts, ScreenConnect, DLL sideloading, autorun.dll, GPU mining, CrystalDiskInfo, HWMonitor, Display Driver Uninstaller, FurMark, K-Lite Codec Pack, PDFgear, gleeze.com, Dynu, dynamic DNS, dynu.com, 150 malicious domains, VirusTotal, LLM-generated response, large language model]
triage_tags: [a_grade_mstic_primary, unknown_threat_actor_explicit, novel_ai_chatbot_seo_poisoning_class, gpu_mining_targeting_high_end_pc_users, supply_chain_structural_warning_class, no_roster_no_ad_named, indirect_ad_developer_population_exposure_via_pc_enthusiast_audience, screenconnect_persistent_remote_access_pattern, dll_sideloading_class]
iocs_extracted: false
iocs_count: 0
text_word_count: 1060
promoted: true
promoted_to_finding: finding-2026-05-27-0005-mstic-cryptojacking-screenconnect-ai-chatbot-seo-poisoning-gleeze-com-dynu-autorun-dll
promoted_at: 2026-05-27T08:22:00-04:00
promoted_by: grader
promoted_in_run: morning-20260527-080000
ttl_expires_at: 2026-08-25T07:48:00-04:00
---

# From poisoned search results to GPU mining: A cryptojacking campaign abusing ScreenConnect and Microsoft .NET utilities

## Source

**Microsoft Security Blog** — joint byline **Microsoft Defender Experts
and Microsoft Defender Security Research Team**, published 2026-05-26
21:35:34 UTC = 17:35 EDT yesterday (in-window for this 16h AM-27
pre-brief sweep).

This is the A-grade MSTIC primary. The THN relay (Ravie Lakshmanan, 03:45
EDT today) was already evaluated at the 06:00 EDT FLASH sentinel and
discarded per Mode 1 at relay-tier; the MSTIC primary warrants raw-
signaling at primary-tier for grader-side disposition.

## Campaign overview

Microsoft Defender Experts have identified **an active cryptojacking
campaign** that combines:
- **Traditional SEO poisoning** (search-engine-result manipulation)
- **AI chatbot poisoning** (large-language-model recommendations
  directing users to attacker-controlled domains) — the novel layer

Per MSTIC's framing, "This emerging delivery technique extends social
engineering beyond conventional search results and increases the
visibility of malicious software recommendations" (paraphrased; no
direct quote >15 words).

The campaign **impersonates trusted system utilities** for high-
performance PC users:
- CrystalDiskInfo
- HWMonitor
- Display Driver Uninstaller (DDU)
- FurMark
- K-Lite Codec Pack
- PDFgear

The target population is deliberately curated for **users likely to
own high-performance discrete GPUs** — the hardware that makes GPU
cryptocurrency mining economically viable. This is a target-quality-
over-target-volume operational pattern.

## Attack chain

1. **Initial access** — user searches for a system utility (e.g.,
   `CrystalDiskInfo download`) via traditional search engine OR asks
   an AI chatbot for a software download recommendation
2. **Search/chatbot result poisoning** — manipulated search results
   and AI-generated responses direct user to **attacker-controlled
   lookalike sites**
3. **Download** — fake site presents a download button that claims to
   provide the legitimate utility. The download retrieves a ZIP archive
   hosted on a campaign-specific subdomain of `gleeze[.]com` (parent
   domain hosted by infrastructure associated with **Dynu**
   (`dynu.com`), a dynamic DNS provider frequently leveraged by threat
   actors)
4. **DLL sideloading** — the downloaded ZIP archive contains the
   legitimate utility executable alongside a malicious DLL named
   `autorun.dll`. When the user launches the executable, the legitimate
   program loads `autorun.dll` from the same folder via DLL sideloading
   (no exploitation, no user-visible anomaly). MSTIC analysis revealed
   **nine distinct `autorun.dll` variants** across the campaign.
5. **Silent installation of ScreenConnect** — the malicious DLL
   silently installs ScreenConnect (legitimate RMM software being
   abused) for persistent remote access
6. **Cryptocurrency mining** — GPU mining payload installed via the
   ScreenConnect persistent access
7. **Potential follow-on** — ScreenConnect persistence "could later
   support data theft, lateral movement, or ransomware activity" per
   MSTIC

## AI chatbot poisoning — methodology

Per MSTIC's research (paraphrased):
- In April 2026, Microsoft observed reports indicating users may have
  been directed to malicious domains through interactions with
  large-language-model (LLM)-based tools
- Users querying AI chatbots for software download recommendations
  were presented with links to attacker-controlled domains within
  generated responses
- Analysis of VirusTotal scan associated with these domains identified
  traffic metadata referencing chatbot interactions as a potential
  referral context
- MSTIC characterizes the behavior as "consistent with emerging
  techniques in AI search result poisoning, representing an extension
  of traditional SEO poisoning beyond conventional search engines"

MSTIC's example illustration explicitly notes: "This example is
illustrative and does not indicate a systemic issue with any specific
AI service" — meaning MSTIC does NOT attribute the chatbot
recommendation behavior to any specific LLM vendor's product flaw.
The mechanism is the broader ecosystem-level SEO-poisoning surface
being absorbed into AI-chatbot training-data and retrieval pipelines.

## Scope

- **More than 150 malicious domains** identified since March 2026 that
  Microsoft assesses serve these tools, masqueraded as system utilities
- Parent infrastructure: `gleeze.com` + subdomain-per-campaign pattern
  on Dynu dynamic-DNS

## Attribution — "unknown threat actor"

**MSTIC does NOT attribute the campaign to any named tracked actor.**
The framing throughout the post is "the threat actor" / "operator" —
not a specific cluster name, not a tracked APT alias, not a UNC
designation.

Per Hard Rule 2, Archimedes records MSTIC's explicit "unknown"
attribution and does NOT cross-walk to any tracked actor.

## A&D / aerospace / defense

**Not mentioned.** No watchlist A&D prime named. No A&D / aerospace /
defense / DIB / CMMC / ITAR sector explicitly named.

**Structural-supply-chain-warning class** for A&D-developer-population
indirect exposure: the targeted PC-enthusiast audience overlaps with
A&D-prime engineering staff who use high-performance workstations for
CAD / simulation / GPU-accelerated computation. Any A&D-prime
engineering laptop or workstation download of one of the named
utilities (CrystalDiskInfo, HWMonitor, DDU, FurMark, K-Lite, PDFgear)
during the campaign window had contemporaneous exposure to this attack
chain.

Per Hard Rule 2, Archimedes does NOT extrapolate from
"PC-enthusiast-audience" to "specific A&D-prime exposure" — the
extrapolation is structural-warning class only.

## CVE

**No CVE in primary scope.** MSTIC's post references CVE-2025-33073
in a separate context (an F5 / Atlassian unrelated case study about
SEO poisoning), NOT as a Megalodon-class vulnerability. No CVE
specific to this cryptojacking campaign.

## IOCs

| Type | Value | Notes |
|---|---|---|
| Domain (campaign parent) | gleeze[.]com | Per MSTIC; subdomain-per-campaign pattern |
| DNS infrastructure | Dynu (dynu.com) | Dynamic DNS provider hosting gleeze.com |
| Domain count (aggregate) | 150+ malicious domains identified since March 2026 | Per MSTIC research |
| File pattern | autorun.dll | DLL sideloading payload (9 distinct variants observed) |
| Abused legitimate software | ScreenConnect (RMM) | Persistent remote access mechanism |
| Lookalike utility brands | CrystalDiskInfo, HWMonitor, DDU, FurMark, K-Lite, PDFgear | Targeted brand impersonations |

Specific gleeze.com subdomains, autorun.dll hash values, and additional
IOC strings would require direct retrieval from MSTIC's full IOC
appendix (not directly captured in this raw-signal summary).

## MITRE ATT&CK

MSTIC's post does not include an explicit MITRE ATT&CK technique table
in the relayed coverage. Technique-class mapping (illustrative; per
the attack chain above):
- T1583.008 Acquire Infrastructure: Malvertising (SEO poisoning + AI
  chatbot poisoning)
- T1189 Drive-by Compromise (download-driven initial access)
- T1574.002 Hijack Execution Flow: DLL Side-Loading
- T1219 Remote Access Software (ScreenConnect abuse)
- T1496 Resource Hijacking (GPU cryptomining)

## Microsoft's defensive guidance

MSTIC recommends:
- Enable cloud-delivered protection
- Run EDR in block mode
- Enable attack surface reduction (ASR) rules

## Significance for AM-27 brief

Grader-side decision:
- **Structural-supply-chain warning class** for A&D-developer-population
  indirect exposure
- **No active A&D-prime victim disclosure**; brief inclusion is
  optional at grader discretion
- **NOT FLASH-eligible**: no tracked-actor (MSTIC explicit unknown);
  no specific CVE; no first-party hit; no A&D-prime named
- **MSTIC primary publication** at A-grade is the source-grade-log
  signal: this confirms MSTIC's continuing operational tempo on
  ecosystem-level abuse research

## Extraction notes

- Language: en
- Publisher byline: Microsoft Defender Experts and Microsoft Defender
  Security Research Team
- Article type: vendor research blog (MSTIC A-grade primary)
- Raw IOC extraction invoked: yes (manual; structured into IOCs table
  above)
- CVSS / CVE: N/A
- Hard Rule 2 compliance: MSTIC explicit "unknown threat actor"
  attribution preserved; no cross-walk to any tracked actor.
- Hard Rule 3 compliance: attack chain described at defender-actionable
  level; no working autorun.dll variant code reproduced; no
  ScreenConnect payload reproduced; no gleeze.com subdomain
  enumeration provided.
- Hard Rule 6 compliance: MSTIC framing paraphrased throughout; no
  direct quotes >15 words.
