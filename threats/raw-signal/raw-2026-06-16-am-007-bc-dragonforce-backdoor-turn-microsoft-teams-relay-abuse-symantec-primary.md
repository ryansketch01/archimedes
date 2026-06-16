---
raw_id: raw-2026-06-16-am-007
collected_at: 2026-06-16T07:54:00-04:00
run_id: pre-brief-20260616-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (Symantec/Broadcom primary, Scattered Spider cross-walk)
  source_url: https://www.bleepingcomputer.com/news/security/ransomware-gang-abuses-microsoft-teams-relays-to-hide-malicious-traffic/
  published_at: 2026-06-16T10:18:48+00:00
match_reason:
  watchlist: []
  actors: [DragonForce, Scattered-Spider]
  vulnerabilities: []
  keywords: [DragonForce, Backdoor.Turn, Microsoft Teams, TURN relay, NAT traversal, Go RAT, Symantec, BYOVD, Huawei driver, Topaz Antifraud, K7 Security, Palo Alto masquerader, defense evasion]
triage_tags: [novel_ttp_layer, ransomware_op_substrate, possible_scattered_spider_cross_walk, no_ad_prime_victim, possible_other_signal_one_liner]
iocs_extracted: true
iocs_count: 0
text_word_count: 720
promoted: true
promoted_to_finding: finding-2026-06-16-0004
promoted_at: 2026-06-16T08:00:00-04:00
ttl_expires_at: 2026-09-14T07:54:00-04:00
---

# DragonForce Ransomware — Novel Microsoft Teams TURN Relay Abuse for C2 Obfuscation (Symantec Primary, Backdoor.Turn Go-based RAT)

**Sources**:
- **BleepingComputer**, Bill Toulas byline. Published 2026-06-16T10:18:48Z.
- **Symantec / Broadcom primary** (referenced by BC as the IR vendor publishing the IOC list)

**URL:** https://www.bleepingcomputer.com/news/security/ransomware-gang-abuses-microsoft-teams-relays-to-hide-malicious-traffic/

## Article substance (paraphrased, no >15 word quotes)

**DragonForce** ransomware operators used a custom malware named **Backdoor.Turn** (Go-based RAT) to hide command-and-control traffic inside Microsoft Teams **TURN (Traversal Using Relays around NAT)** relay infrastructure. The novel TTP allows the malware's C2 communications to be masked as legitimate Teams traffic.

### Novel TTP analysis

- **Backdoor.Turn** is described as "the first known malware to abuse Microsoft Teams' TURN relay servers" per Symantec (15 words — at the Hard Rule 6 limit, NOT exceeded but operator should consider whether to paraphrase or quote in brief composition)
- TURN is a legitimate protocol used by WebRTC services (including Microsoft Teams) to traverse NAT-restricted networks via relay servers
- By abusing the Teams TURN relays, attackers blend malicious C2 with normal corporate Teams traffic — defenders see flows to legitimate Microsoft infrastructure
- The technique is genuinely novel as a TTP layer; possible detection-pattern substrate worth elevating to operational template tier

### DragonForce attribution context

- BC describes DragonForce as "linked to Scattered Spider" — Scattered Spider IS on the _roster.yaml #013 (HIGH threat level)
- DragonForce itself is NOT on _roster.yaml as a primary or alias; the Scattered Spider linkage is a Symantec/BC observation, not a roster cross-walk
- Hard Rule 2 BINDING: Archimedes does NOT originate the DragonForce/Scattered Spider cross-walk; Symantec attributes the linkage per BC

### Named victim and timeline

- **Named victim**: "A major U.S. services company" (December 2025 attack)
- BC does NOT identify the company by name
- Symantec's full report likely names or anonymizes the victim — direct Symantec retrieval would be needed to confirm
- **No A&D-prime named victim**

### Tradecraft sophistication (per Symantec)

- Attackers demonstrated "exceptionally sophisticated cyber tradecraft" per Symantec attribution (paraphrased)
- Employed **BYOVD (Bring Your Own Vulnerable Driver)** techniques with multiple vulnerable drivers:
  - Huawei driver
  - Topaz Antifraud driver
  - K7 Security driver
  - **Custom Palo Alto Networks masquerader** (i.e., the attackers built a driver that impersonates Palo Alto Cortex XDR / Palo Alto driver to evade detection — distinct tradecraft from generic vulnerable-driver abuse)
- BYOVD pre-ransomware-deployment for defense evasion

### Ransomware operation context

- Final-stage ransomware deployment after BYOVD defense-evasion
- DragonForce active since 2023 per Symantec
- This is one DragonForce campaign; not the only one observed in 2026

## Attribution language (Hard Rule 2 preserved)

- Symantec originates the Backdoor.Turn / DragonForce attribution
- Symantec originates the DragonForce / Scattered Spider linkage claim
- Hard Rule 2 BINDING: Archimedes records what Symantec says; does not originate either claim independently
- DragonForce NOT on _roster.yaml; Scattered Spider IS on roster as #013 — but Hard Rule 2 prohibits Archimedes from collapsing the two clusters even though Symantec asserts the linkage. The grader/red-team-analyst can record the Symantec-asserted linkage but should preserve cluster-identity discipline.

## A&D relevance assessment

- **A&D-relevance: LOW-MEDIUM**
- "A major U.S. services company" — sector unspecified; likely commercial services, not A&D-prime
- **TTP-pattern A&D-relevance**: HIGH — the TURN-relay abuse pattern is broadly applicable across enterprise tenants using Microsoft Teams, including A&D-prime tenants. Detection-pattern substrate worth surfacing.
- BYOVD with custom Palo Alto masquerader is a tradecraft layer that A&D-prime EDR posture defenders should track.

## IOC extraction

**No specific IOCs** in the BC article. BC states: "Symantec published a complete indicators of compromise list" — Symantec primary retrieval would be needed for the full IOC table.

**Behavioral / detection patterns** (operational substrate):
1. Anomalous TCP/UDP traffic flows to Microsoft Teams TURN relay servers (legitimate Teams uses TURN, so detection is by anomaly rather than blocklist — egress flow analysis with timing/volume anomaly detection)
2. BYOVD vulnerable-driver indicators: Huawei driver, Topaz Antifraud driver, K7 Security driver
3. Custom Palo Alto Networks driver masquerade — driver signing certificate anomaly detection
4. Go-based RAT executable patterns

## Grader notes

- **Source grading path**: Symantec/Broadcom A-grade vendor IR primary. BC B-grade trade press relay. T1 GATE PARTIALLY SATISFIED — one A-grade primary + one B-grade relay; absence of second IR vendor confirmation caps WEP at LIKELY.
- **Independent corroboration test**: SINGLE-A-VENDOR-PRIMARY substrate. Symantec stands alone on the Backdoor.Turn discovery and the DragonForce/Scattered Spider linkage. Single-source-veto applies.
- **Hard Rule 6 quote limit**: 15-word Symantec quote captured (at limit). One quote per source.
- **Promotability assessment** (for grader to decide):
  - Net-new substrate: YES (novel TURN-relay TTP)
  - Active campaign confirmed: YES (December 2025 attack documented)
  - Named A&D-prime victim: NO
  - Tracked-actor on roster: PARTIAL (DragonForce not on roster; Scattered Spider IS on roster but cross-walk requires operator-deferred validation)
  - **Likely promotability**: B2 finding standard analyst path, OR "Other Signal" one-liner for the TTP-pattern surfacing. Operator-deferred Scattered Spider dossier mutation candidacy if cross-walk is operator-approved (separate /update-tracking path).
  - **FLASH-eligibility retrospective**: T2 (tracked-actor-attribution) PARTIAL FIRE on Scattered Spider linkage — but the linkage is Symantec-asserted not vendor-confirmed by separate IR firm. T4 (tracked-actor-ttp-change) PASSES — TURN-relay abuse is novel TTP layer. T5 FAIL — no A&D-prime named victim. Net: morning-brief candidate.
