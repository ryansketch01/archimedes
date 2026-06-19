---
raw_id: raw-2026-06-19-flash-0000-001-bc-toulas-gentlemen-edr-killers-second-publisher-relay
collected_at: 2026-06-19T00:08:00-04:00
run_id: flash-sweep-20260619-000000
collection_mode: flash_sweep
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (Bill Toulas)
  source_url: https://www.bleepingcomputer.com/news/security/gentlemen-ransomware-uses-multiple-edr-killers-to-disable-defenses/
  published_at: 2026-06-18T22:31:52+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Gentlemen, ransomware, RaaS, GentleKiller, HexKiller, ThrottleBlood, HavocKiller, OxideHarvest, EDR, BYOVD, Warlock, MedusaLocker, DragonForce, Qilin, ESET, Oltenia, SystemBC]
triage_tags: [substrate_strengthening, ransomware_research, edr_killer_tooling_layer, second_publisher_relay, single_ir_vendor_eset_primary, ad_indirect, energy_sector_named_victim, operator_deferred_new_actor_candidate, anti_noise_check_against_reject_2026_06_17_0007, anti_noise_check_against_reject_2026_06_18_0008, hard_rule_2_binding, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 540
promoted: false
ttl_expires_at: 2026-09-17T00:08:00-04:00
---

# Gentlemen ransomware uses multiple EDR killers to disable defenses (BC-Toulas second-publisher relay)

**Publisher:** BleepingComputer (Bill Toulas byline)
**Published:** 2026-06-18T22:31:52+00:00 (~6.5h before this sweep)
**URL:** https://www.bleepingcomputer.com/news/security/gentlemen-ransomware-uses-multiple-edr-killers-to-disable-defenses/

## Why this raw-signal was written

This is a **substrate-strengthening** entry for the operator-deferred Gentlemen /new-actor candidacy carry-forward. BC-Toulas relays ESET-primary GentleKiller research (Jakub Souček byline on the underlying ESET work) that was first surfaced by Help Net Security (Anamarija Pogorelec) on 2026-06-18 morning (raw-2026-06-18-am-010, reject-2026-06-18-0008) and the underlying ESET-WeLiveSecurity primary research was operator-deferred /new-actor candidacy carry-forward from reject-2026-06-17-0007.

**BC = second-publisher relay** widening publisher-independence on the EDR-killer-tooling-supply layer. ESET remains the single IR-vendor primary on actor identity and tooling. **Single-IR-vendor-on-actor-identity-veto still persists** — Mandiant / CrowdStrike / Unit-42 / MSTIC corroboration on the Gentlemen actor identity + EDR-killer-tooling-supply layer remains substrate-that-would-lift-veto.

Net-new this sweep vs. prior corpus:
- Second publisher (BC) joins HNS on the same ESET primary
- Named victim: **Romanian energy provider Oltenia** (energy sector, NOT A&D-prime per watch-config sector_tags — does NOT shift T5 ad_sector_campaign gate)
- Named adjacent infrastructure: **SystemBC proxy botnet with 1,570+ compromised corporate hosts** (referenced as adjacent affiliate-distribution channel)

## Article body summary

BleepingComputer (Bill Toulas) relays ESET research on The Gentlemen ransomware-as-a-service (RaaS) operation's active development and maintenance of a suite of endpoint detection and response (EDR) killers used by affiliates to evade defenses in attacks. Unlike most RaaS operations where defense-disabling tooling is sourced by affiliates from third-party tool markets, Gentlemen develops and maintains EDR killers in-house and ships them as a benefit of the affiliate relationship.

### EDR-killer toolkit (per BC relay of ESET)

- **GentleKiller** — flagship tool. 8 variants observed. Each impersonates a legitimate security product (Kaspersky, Valorant, Javelin, WatchDog observed as cover names). Leverages BYOVD (Bring Your Own Vulnerable Driver) or malicious kernel drivers.
- **HexKiller** — previously associated with Warlock ransomware gang.
- **ThrottleBlood** — linked to MedusaLocker and DragonForce ransomware operations.
- **HavocKiller** — observed in ransomware operations broadly.
- **OxideHarvest** — Rust-based credential stealer believed externally developed (NOT in-house Gentlemen tool, used adjacent to the EDR-killer kit).

### Targeting coverage

GentleKiller targets **400+ security processes across approximately 48 vendor products**, including Microsoft Defender, CrowdStrike Falcon, SentinelOne, Palo Alto Cortex, Sophos, Trend Micro, ESET, Bitdefender, McAfee/Trellix, and Kaspersky. (BC explicit count restatement of ESET primary figure.)

### Named victims and adjacent infrastructure

- **Oltenia** — Romanian energy provider (named victim).
- **SystemBC** — proxy botnet with 1,570+ compromised corporate hosts referenced as adjacent affiliate-distribution / lateral-movement infrastructure (BC paraphrases ESET — not a victim of Gentlemen per se but used by ransomware affiliates broadly).

### Attribution (BC verbatim — no cross-walk by Archimedes per Hard Rule 2)

BC cites "According to ESET researchers" and identifies the threat group only as "Gentlemen RaaS." No tracked-roster actor attribution (no UNC1549/APT28/Lazarus/Volt Typhoon/Salt Typhoon/APT41/MuddyWater/APT37 cross-walk). Gentlemen is NOT on _roster.yaml (24-actor roster). Operator-deferred /new-actor candidacy from reject-2026-06-17-0007 continues to carry-forward. Hard Rule 2 BINDING — Archimedes does NOT originate Gentlemen → tracked-roster attribution.

## FLASH-trigger evaluation (this sweep)

- **T1 critical CVE exploited:** FAIL — no CVE in article
- **T2 tracked actor attribution:** FAIL — Gentlemen NOT on _roster.yaml
- **T3 first-party IOC hit:** FAIL — no IOCs published; Splunk sentinel 0 hits this sweep
- **T4 tracked actor TTP change:** FAIL — Gentlemen not on roster, attribution layer prerequisite missing
- **T5 A&D sector campaign:** FAIL — Oltenia is Romanian ENERGY sector not A&D-prime per watch-config sector_tags; single-incident not multi-victim-campaign sufficient for T5
- **T6 zero-day no patch:** FAIL — no fresh CVE this article
- **Critical-override:** 0-of-4 conditions met

**Verdict:** non-FLASH-eligible. Substrate-strengthening signal for operator-deferred /new-actor Gentlemen candidacy and possible morning-brief Other Signal one-liner candidate IF substrate-strengthening absorbed into AM lift on EDR-killer-tooling-supply-pattern layer. NOT a FLASH candidate this sweep.

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas (BC)
- Article type: blog / news article (B-grade per source-grades.yaml bleepingcomputer entry)
- Raw IOC extraction invoked: no (article carries no IOCs per BC body — ESET primary may; not retrieved this sweep)
- Anti-noise checks performed: cross-checked against reject-2026-06-17-0007 (ESET-primary GentleKiller original surface) and reject-2026-06-18-0008 (raw-2026-06-18-am-010 HNS-Pogorelec relay AM brief dac22e4 substrate). This BC-Toulas item is genuinely net-new publisher relay, NOT under-24h dedup hit on same publisher.

## IOCs

None published in BC article body. ESET primary research (referenced URL: https://www.welivesecurity.com/en/eset-research/the-gentlemen-call/ per HNS-Pogorelec relay) may contain IOC tables but were not retrieved this sweep — defer to grader / next pre-brief collection cycle for ESET primary body retrieval if substrate strengthens further.
