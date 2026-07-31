---
raw_id: raw-2026-07-31-flash-1800-001
collected_at: 2026-07-31T18:05:00-04:00
run_id: flash-sweep-1800-20260731
collection_mode: flash_sweep
flash_candidate: true
source:
  source_yaml_id: mstic
  source_name: Microsoft MSTIC / Microsoft Threat Intelligence
  source_url: https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
  source_grade: A
  published_at: 2026-07-31T17:01:00-04:00   # 21:01 UTC
match_reason:
  watchlist: []                              # no named A&D prime victim (corporate-traveler targeting is sector-agnostic)
  actors: ["009"]                            # APT29 / Midnight Blizzard / Cozy Bear / NOBELIUM / SVR
  vulnerabilities: []                        # no CVE cited
  keywords: [Midnight Blizzard, Storm-2945, CaptiveCrunch, captive portal, AitM, device code phishing, Entra ID, ClickFix]
triage_tags: [flash_candidate, tracked-actor-attribution, tracked-actor-ttp-change, new_attribution, active_campaign, ai_augmented]
flash_triggers_matched:
  - trigger-2-tracked-actor-attribution     # NEW campaign + NEW sub-cluster designation attributed to a roster actor by A-grade source
  - trigger-4-tracked-actor-ttp-change       # new tooling + new targeting + new infrastructure class, attributable to APT29
digraph_estimate: A2                          # MSTIC A-grade first-party Defender telemetry; single originating primary on the Storm-2945->Midnight Blizzard sub-cluster attribution -> grader likely applies single-source veto, WEP capped at "likely" (partial independent corroboration from ReliaQuest 2026-07-23 on the doppelganger-domain/AitM layer only). Clears B2 FLASH minimum. GRADER OWNS FINAL DIGRAPH.
wep_estimate: likely
quiet_hours: false                            # 18:00 EDT is inside active window 09:00-21:00 -> if validated, posts to #flash-alerts (not queued)
anti_noise_check: net_new                     # grep of threats/ confirms no prior CaptiveCrunch / Storm-2945 / captive-portal-APT29 coverage in corpus; NOT a dedup
iocs_extracted: true
iocs_count: 12                                # 4 domains + 6 ipv4 + 2 sha256
first_party_splunk:
  mandatory_tracked_ioc_sweep:
    archimedes: 0
    defenseclaw_local: 0
    window: -24h
    note: "0 tracked-IOC hits either index. archimedes 2148 events/-90d (self-log operation+scheduler only, 0 IOC matches); defenseclaw_local 0 events in window (visibility-bounded null)."
  captivecrunch_ioc_enrichment:               # net-new indicators (not yet in _master-index), checked opportunistically
    archimedes: 0
    defenseclaw_local: 0
    window: -24h
promoted: true
promoted_to_finding: finding-2026-07-31-0002
promoted_at: 2026-07-31T18:12:00-04:00
ttl_expires_at: 2026-10-29T18:05:00-04:00
---

# CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft

**Source:** Microsoft Threat Intelligence (MSTIC), published 2026-07-31 ~17:01 EDT (in-window for the 18:00 FLASH sweep, ~12:00–18:00 EDT).

## Summary (collector paraphrase — not graded)

Microsoft Threat Intelligence reports **Storm-2945**, assessed as an **operational sub-cluster of Midnight Blizzard** (roster #009 — APT29 / Cozy Bear / NOBELIUM; attributed by US+UK governments to Russia's SVR), running a campaign MSTIC calls **CaptiveCrunch** since early May 2026. The actor compromises **captive-portal / Wi-Fi networks at hospitality-sector venues** (hotels, conference centers, shared venues) worldwide and manipulates DNS/HTTP traffic to redirect corporate travelers through actor-controlled infrastructure.

Two operational strands:
1. **AitM phishing** via doppelganger domains impersonating Microsoft online services, abusing the **device-code authentication flow in Microsoft Entra ID** (leads to Entra device registration + M365 data collection). ReliaQuest reported a portion of this on 2026-07-23.
2. **Malware delivery** — payloads disguised as browser/OS updates triggered by browsers' automated captive-portal connectivity checks, using **ClickFix** social-engineering prompts. Android APK delivery also observed.

MSTIC assesses Storm-2945 as Midnight Blizzard based on technical/operational overlaps with **Storm-2372** (Midnight Blizzard initial-access sub-cluster, device-code/OAuth phishing tracked through 2025). Notes TTP similarity to the **Forest Blizzard** (APT28 #006) DNS-hijacking op disclosed April 2026, but attributes CaptiveCrunch to Storm-2945/Midnight Blizzard, not Forest Blizzard. Microsoft states a significant portion of the operation is **AI-augmented** and credits collaboration with Anthropic and OpenAI.

## Why this is a FLASH candidate

- **Trigger 2 — new attribution for a tracked actor:** New campaign (CaptiveCrunch) and new sub-cluster designation (Storm-2945) attributed to Midnight Blizzard / APT29 (#009) by an A-grade source (MSTIC). First public disclosure today; not a restatement of prior attribution.
- **Trigger 4 — tracked actor TTP change:** New tooling (CornFlake Golang RAT, ChocoShell PowerShell infostealer, FruitStone C2 panel, Android APK), new targeting class (captive-portal/hospitality/traveler), new infrastructure class (captive-portal ecosystem access + AitM), AI-augmentation — all attributable to APT29 per A-grade source.

**A&D relevance:** INDIRECT / STRUCTURAL. No named A&D prime or watchlist entity victim. Targeting is corporate travelers generally; an ITAR/DIB executive traveling through a compromised hotel/conference Wi-Fi is within the plausible victim envelope (session-token/credential theft → M365 access). Trigger 2/4 do not require an A&D victim. Grader/briefer to judge sector-section placement.

**Attribution discipline (Hard Rule 2):** All attribution above is MSTIC's, recorded verbatim — "Storm-2945 is an operational sub-cluster of Midnight Blizzard based on distinctive technical and operational overlaps." Collector originates no attribution. Single originating primary on the sub-cluster claim (ReliaQuest 2026-07-23 corroborates only the doppelganger-domain/AitM portion); grader to apply single-source veto as warranted.

---

## Extraction notes

- Language: en
- Publisher byline: Microsoft Threat Intelligence
- Article type: vendor blog (threat-intelligence report)
- Raw IOC extraction invoked: yes
- Full article retrieved via WebFetch for the IOC appendix (RSS content truncated mid-body). No PoC/exploit content present or copied (Hard Rule 3 n/a — none published). No credentials in source (Hard Rule 7 n/a).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: mstic-captivecrunch-2026-07-31
  source_url: https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
  extracted_at: 2026-07-31T22:05:00Z
  extracted_by: collector
  target_actor_id: "009"    # APT29 / Midnight Blizzard — per MSTIC attribution; grader confirms
  text_word_count: 620      # captured body + IOC appendix (partial of full article)

indicators:
  - id: apt29-domain-ms365-device
    type: domain
    value: ms365-device.com
    defanged_original: "ms365-device[.]com"
    resolved_ip: null
    first_seen: 2026-05
    last_seen: 2026-07
    role: delivery            # doppelganger MS-service domain for AitM device-code phishing
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: >
      "doppelganger domains mimicking Microsoft online services to conduct
      follow-on adversary-in-the-middle (AitM) phishing operations that abuse
      the device code authentication flow in Microsoft Entra ID."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-domain-ms365-live
    type: domain
    value: ms365-live.com
    defanged_original: "ms365-live[.]com"
    resolved_ip: null
    first_seen: 2026-05
    last_seen: 2026-07
    role: delivery
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (doppelganger MS-service domains)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-domain-m365-owa
    type: domain
    value: m365-owa.com
    defanged_original: "m365-owa[.]com"
    resolved_ip: null
    first_seen: 2026-05
    last_seen: 2026-07
    role: delivery
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (doppelganger MS-service domains)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-domain-owa-ms365
    type: domain
    value: owa-ms365.com
    defanged_original: "owa-ms365[.]com"
    resolved_ip: null
    first_seen: 2026-05
    last_seen: 2026-07
    role: delivery
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (doppelganger MS-service domains)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-ip-31-57-243-154
    type: ipv4
    value: 31.57.243.154
    defanged_original: "31.57.243[.]154"
    first_seen: 2026-05
    last_seen: 2026-07
    role: c2
    campaign: "CaptiveCrunch"
    related_malware: [CornFlake, FruitStone]
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (actor-controlled infrastructure)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: "NOT the same as tracked 31.57.35.223 (different IOC in _master-index)."
  - id: apt29-ip-38-146-28-75
    type: ipv4
    value: 38.146.28.75
    defanged_original: "38.146.28[.]75"
    first_seen: 2026-05
    last_seen: 2026-07
    role: c2
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (actor-controlled infrastructure)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-ip-38-146-28-132
    type: ipv4
    value: 38.146.28.132
    defanged_original: "38.146.28[.]132"
    first_seen: 2026-05
    last_seen: 2026-07
    role: c2
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (actor-controlled infrastructure)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-ip-104-194-159-150
    type: ipv4
    value: 104.194.159.150
    defanged_original: "104.194.159[.]150"
    first_seen: 2026-05
    last_seen: 2026-07
    role: c2
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (actor-controlled infrastructure)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-ip-107-189-26-194
    type: ipv4
    value: 107.189.26.194
    defanged_original: "107.189.26[.]194"
    first_seen: 2026-05
    last_seen: 2026-07
    role: c2
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (actor-controlled infrastructure)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-ip-213-145-86-112
    type: ipv4
    value: 213.145.86.112
    defanged_original: "213.145.86[.]112"
    first_seen: 2026-05
    last_seen: 2026-07
    role: c2
    campaign: "CaptiveCrunch"
    related_malware: []
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "Listed in Microsoft IOC appendix (actor-controlled infrastructure)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: null
  - id: apt29-hash-918fa52ae45e
    type: hash_sha256
    value: 918fa52ae45ed60ba7cc8bdc99c3cbe9ab92e0375ec31fc05d0d4513be11c593
    defanged_original: null
    first_seen: 2026-05
    last_seen: 2026-07
    role: delivery
    campaign: "CaptiveCrunch"
    related_malware: [CornFlake, ChocoShell]
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "SHA-256 in Microsoft IOC appendix (malware posing as browser/OS update)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: "Family mapping (CornFlake/ChocoShell) is collector's best-effort association; grader/actor-profiler to confirm hash->family binding from full appendix."
  - id: apt29-hash-be99857449d2
    type: hash_sha256
    value: be99857449d2856dd5a84e21c8a3d5e0e01456adb44062ddec5a6b4970d8d42c
    defanged_original: null
    first_seen: 2026-05
    last_seen: 2026-07
    role: delivery
    campaign: "CaptiveCrunch"
    related_malware: [CornFlake, ChocoShell]
    source_brief: mstic-captivecrunch-2026-07-31
    context_excerpt: "SHA-256 in Microsoft IOC appendix (malware posing as browser/OS update)."
    attribution_in_text: "Storm-2945 (Midnight Blizzard sub-cluster)"
    notes: "Family mapping is best-effort; grader/actor-profiler to confirm."

tooling_named_in_text:            # malware family names (not atomic IOCs) — recorded for actor-profiler
  - name: CornFlake
    type: malware_family
    detail: "Fully-featured Windows RAT, compiled Golang — system enum, file/keystroke collection, credential + session-token theft, audio/video surveillance, removable-media monitoring, remote shell."
  - name: ChocoShell
    type: malware_family
    detail: "PowerShell infostealer."
  - name: FruitStone
    type: malware_family
    detail: "C2 panel."
  - name: "Android APK"
    type: malware_family
    detail: "Android component delivered via ClickFix landing; specific name not provided by MSTIC."

attribution_claims:
  - claimed_actor: "Midnight Blizzard (APT29 / Cozy Bear / NOBELIUM / SVR) — via Storm-2945 sub-cluster"
    ioc_ids:
      - apt29-domain-ms365-device
      - apt29-domain-ms365-live
      - apt29-domain-m365-owa
      - apt29-domain-owa-ms365
      - apt29-ip-31-57-243-154
      - apt29-ip-38-146-28-75
      - apt29-ip-38-146-28-132
      - apt29-ip-104-194-159-150
      - apt29-ip-107-189-26-194
      - apt29-ip-213-145-86-112
      - apt29-hash-918fa52ae45e
      - apt29-hash-be99857449d2
    claimed_by_source: mstic-captivecrunch-2026-07-31
    attribution_confidence_in_source: "assessed operational sub-cluster of Midnight Blizzard based on distinctive technical and operational overlaps"
    requires_grading: true
    notes: >
      Single originating primary (MSTIC) on the Storm-2945->Midnight Blizzard binding.
      ReliaQuest (2026-07-23) independently reported a portion of the doppelganger-domain/
      AitM device-code activity but did not (per MSTIC framing) make the Midnight Blizzard
      sub-cluster attribution. Grader: single-source veto candidate on the attribution layer.

benign_filtered:
  - value: microsoft.com
    reason: reference_site / publisher_domain
  - value: entra.microsoft.com
    reason: legitimate_service_referenced_as_target (Entra ID device-code flow)

extraction_warnings:
  - type: partial_appendix
    detail: "RSS content truncated mid-body; IOC appendix recovered via WebFetch. Hash->family bindings and any additional IOCs (URLs, filenames, Android APK hash) may exist in the full appendix beyond what WebFetch returned. Direct-retrieval verification recommended before actor-profiler folds into APT29 iocs.yaml."
  - type: new_indicator_not_in_master_index
    detail: "All 12 indicators are net-new (not in _master-index.yaml). First-party Splunk enrichment sweep over -24h returned 0 hits both indices."
```
