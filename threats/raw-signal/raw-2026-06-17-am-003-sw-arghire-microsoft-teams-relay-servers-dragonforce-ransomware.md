---
raw_id: raw-2026-06-17-am-003-sw-arghire-microsoft-teams-relay-servers-dragonforce-ransomware
collected_at: 2026-06-17T07:38:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/microsoft-teams-relay-servers-abused-in-dragonforce-ransomware-attack/
  published_at: 2026-06-17T10:38:00+00:00
match_reason:
  watchlist: []
  actors: [DragonForce, Scattered-Spider]
  vulnerabilities: []
  keywords: [DragonForce, Microsoft Teams, TURN, relay servers, Go backdoor, Backdoor.Turn, ransomware]
triage_tags: [carry_forward, finding_2026_06_16_0004_substrate_strengthening, third_publisher_relay, single_vendor_veto_persists, hard_rule_2_binding]
iocs_extracted: false
iocs_count: 0
text_word_count: 220
promoted: true
promoted_to_finding: finding-2026-06-17-0005
promoted_at: 2026-06-17T08:18:00-04:00
ttl_expires_at: 2026-09-15T07:38:00-04:00
---

# Microsoft Teams Relay Servers Abused in DragonForce Ransomware Attack

**Source:** SecurityWeek (https://www.securityweek.com/microsoft-teams-relay-servers-abused-in-dragonforce-ransomware-attack/)
**Author byline:** Ionut Arghire
**Published:** 2026-06-17T10:38:00+00:00 (06:38:00 EDT)

## RSS-summary captured

> The attackers deployed a new Go-based backdoor that uses Microsoft Teams servers for command-and-control.

## Extraction notes

- **Language:** en
- **Publisher byline:** Ionut Arghire (SecurityWeek)
- **Article type:** trade-press journalistic relay of Symantec primary research (Backdoor.Turn family)
- **Upstream primary:** Symantec Threat Hunter Team (originating IR-vendor on Backdoor.Turn novel-TTP layer, captured AM 2026-06-16 as finding-2026-06-16-0004)
- **Cross-walk:** Same trigger-topic carry-forward from 2026-06-16 AM brief `2bde07c` finding-2026-06-16-0004 + PM brief `8fc1987` substrate-strengthened BC+HNS dual-publisher. SW-Arghire adds **third independent B-grade publisher journalistic relay** (BC + HNS + SW). Single-vendor-IR-firm-on-novel-TTP-layer veto on Symantec still applies.
- **Hard Rule 6 preservation:** 15-word quote discipline preserved — RSS-summary is editorial paraphrase.
- **Hard Rule 2 preservation:** Symantec-asserted DragonForce/Scattered-Spider linkage Hard-Rule-2 BINDING preserved. Scattered-Spider dossier mutation PAUSED pending independent second-IR-vendor corroboration. Archimedes does NOT cross-walk DragonForce to Scattered-Spider on Symantec primary alone.
- **Raw IOC extraction invoked:** no (relay-layer article; IOCs already at Symantec upstream primary captured 2026-06-16 AM)

## Substrate observation for grader

Triple-publisher journalistic relay (BC + HNS + SW). **Substrate-strengthening for finding-2026-06-16-0004**, possible morning brief UPDATE pivot candidate. Substrate-strengthening is on the publisher-independence layer NOT on the IR-vendor-corroboration layer. The single-vendor-veto on Symantec Backdoor.Turn / novel TURN-relay TTP **persists** — Mandiant / CrowdStrike / Unit 42 / MSTIC independent IR-vendor corroboration would be the substrate that lifts the veto. No such substrate this sweep.

A&D-relevance via operational-template inheritance — Microsoft Teams TURN-relay abuse is identical-class novel TTP affecting any A&D-prime Teams tenant.
