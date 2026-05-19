---
raw_id: raw-2026-05-19-am-003
collected_at: 2026-05-19T07:43:00-04:00
run_id: pre-brief-20260519-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer (Bill Toulas)"
  source_url: https://www.bleepingcomputer.com/news/security/shub-macos-infostealer-variant-spoofs-apple-security-updates/
  published_at: 2026-05-18T17:42:20-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [macOS, infostealer, SHub, AppleScript, malvertising, fake Apple security update, cryptocurrency wallet]
triage_tags:
  - macos_infostealer_variant
  - shub_reaper_new_variant_name
  - sentinelone_originating_research
  - non_roster_actor_no_attribution
  - applescript_url_scheme_abuse
  - browser_credential_theft_crypto_wallet
  - russian_keyboard_exclusion_geofencing
  - no_a_and_d_targeting_consumer_class
  - commodity_macos_malware
  - non_flash_grader_queue_item
  - hard_rule_2_no_attribution_origination
iocs_extracted: true
iocs_count: 6
text_word_count: 538
promoted: false
rejected_at: 2026-05-19T08:40:00-04:00
rejection_id: reject-2026-05-19-0002
ttl_expires_at: 2026-08-17T07:43:00-04:00
---

# SHub macOS infostealer variant spoofs Apple security updates

## Headline & date

**Source:** BleepingComputer (Bill Toulas) — 2026-05-18T17:42:20-04:00 (21:42 GMT) — JUST inside 14h pre-brief window (~12 min margin to 17:30 start)
**Headline:** "SHub macOS infostealer variant spoofs Apple security updates"
**URL:** https://www.bleepingcomputer.com/news/security/shub-macos-infostealer-variant-spoofs-apple-security-updates/

## Originating researcher

SentinelOne (SentinelLabs — A-grade per provisional ratification 2026-05-08).

## Variant name

**SHub Reaper** — new variant of the SHub macOS infostealer family.

## Distribution & social engineering

Spoofed-installer domains impersonating WeChat, Miro, and Microsoft serve macOS executables (via Dropbox download buttons). Upon execution, the malware invokes the `applescript://` URL scheme to launch macOS Script Editor with a malicious AppleScript that displays a fake Apple security-update message referencing "XProtectRemediator."

## Capabilities

- Browser data theft: Chrome, Firefox, Brave, Edge, Opera
- Cryptocurrency wallet targeting: MetaMask, Phantom, Exodus, Atomic Wallet (hijacks wallet apps by replacing core files)
- Password-manager extension harvesting
- Persistence: LaunchAgent impersonating Google software updates

## Detection-evasion / geofencing

- Checks for Russian keyboard input and exits if detected (Russian-speaker exclusion — commodity-actor tradecraft signal, NOT attribution per Hard Rule 2)
- VM / VPN fingerprinting for sandbox evasion
- Bypasses Gatekeeper via quarantine attribute removal + ad hoc code signing

## IOCs (3 domains + 3 attack-chain artifact classes)

| IOC | Type | Notes |
|---|---|---|
| `qq-0732gwh22[.]com` | spoofed-installer domain | impersonates WeChat |
| `mlcrosoft[.]co[.]com` | spoofed-installer domain | typosquat on microsoft.com — Cyrillic/visual confusable |
| `mlroweb[.]com` | spoofed-installer domain | impersonates Miro |
| AppleScript via `applescript://` URL scheme | attack-chain artifact | dropper mechanism |
| LaunchAgent impersonating Google software updates | persistence artifact | macOS-specific |
| Replaced wallet-app core files (MetaMask/Phantom/Exodus/Atomic) | wallet-hijack artifact | crypto-wallet-specific |

## Attribution per source

No specific named threat actor cited. The Russian-keyboard-exclusion is a Russian-speaker-language commodity-actor signal often used by infostealer authors but is NOT a tracked-actor attribution per Hard Rule 2. SentinelOne does not name an APT for this variant in the BleepingComputer relay.

## A&D / defense-prime relevance

None. Consumer-class macOS targeting via spoofed-app malvertising. Crypto-wallet targeting is the financial-fraud profile. No defense, aerospace, federal, or A&D-prime customer named.

## Trigger evaluation

- Trigger 1 (CVE+active+A-grade): no CVE → **FAIL**
- Trigger 2 (new attribution): no roster actor → **FAIL**
- Trigger 3 (Splunk IOC): 0 hits on `qq-0732gwh22` / `mlcrosoft.co` / `mlroweb.com` per pre-brief sweep → **FAIL**
- Trigger 4 (TTP change): no roster actor → **FAIL**
- Trigger 5 (A&D campaign): no A&D sector → **FAIL**
- Trigger 6 (zero-day): no CVE, no zero-day → **FAIL**

Disposition: morning brief mention-class for SentinelLabs research-cadence carry-forward (SHub family is consumer-class macOS infostealer, not A&D-relevant). Grader may include in coverage-log only or skip.

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas
- Article type: news
- Hard Rule 2: no Archimedes-originated attribution. SentinelLabs framing preserved as-source-said.
- Hard Rule 3: no exploit code or PoC walkthroughs in source — defensive-detection oriented.
- Raw IOC extraction invoked: yes — 3 domain IOCs + 3 attack-chain artifact classes. Cataloged for grader IOC-augmentation consideration; consumer-class commodity-infostealer, low A&D priority for _master-index.yaml inclusion.
