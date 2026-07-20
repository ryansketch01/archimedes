---
raw_id: raw-2026-07-20-pm-001
collected_at: 2026-07-20T15:31:00-04:00
run_id: pre-brief-20260720-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (relay of Group-IB technical analysis)
  source_url: https://www.bleepingcomputer.com/news/security/new-hollowgraph-malware-uses-microsoft-graph-for-stealthy-c2-comms/
  published_at: 2026-07-20T13:43:01-04:00
  originating_research: "Group-IB (primary technical report; HollowGraph analysis)"
match_reason:
  watchlist: []                 # no aerospace-defense.yaml entity named; targeting is Israel
  actors: []                    # Group-IB does NOT attribute to a _roster.yaml actor; see note below
  vulnerabilities: []           # no CVE referenced
  keywords: [Cavern C2 framework, Cav3rn, HollowGraph, Microsoft Graph C2, Iran-nexus, Lyceum, Israel, espionage]
  roster_relationship_note: >
    Brought into scope by the CAVERN C2 FRAMEWORK linkage, not an actor attribution.
    Group-IB assesses HollowGraph "with high confidence" as linked to the Cavern C2
    framework — the same "Cavern"/"Cav3rn" modular .NET C2 toolset tracked to
    Cavern Manticore (Actor #026, Iran-MOIS) per finding-2026-07-06-0001. Group-IB
    ALSO notes technical similarities to Lyceum (Iranian-nexus; Lyceum = OilRig/APT34
    #023 subgroup per CPR) but states evidence is "insufficient to attribute the
    activity to the threat actor with high confidence." Per Hard Rule 2, NO actor
    attribution is originated or hardened here — recorded as source-stated tooling
    linkage + low-confidence similarity only. Grader / actor-profiler to adjudicate
    whether this is a Cavern Manticore #026 cluster development.
triage_tags: [pre_brief, grader_queue, actor_profiler_candidate, iran_nexus, cavern_c2_framework, espionage, m365_graph_c2, non_flash]
iocs_extracted: true
iocs_count: 3
text_word_count: 430
promoted: true
promoted_to_finding: finding-2026-07-20-0001
promoted_at: 2026-07-20T16:05:00-04:00
ttl_expires_at: 2026-10-18T15:31:00-04:00
---

# HollowGraph — Microsoft Graph (M365 calendar) C2 malware linked to the Cavern C2 framework; Iran-nexus, Israel-targeted espionage (Group-IB)

Net-new to the Archimedes corpus this afternoon pre-brief sweep. Surfaced
2026-07-20 13:43 EDT via BleepingComputer (Bill Toulas) relaying an originating
Group-IB technical report. Raw-signaled as a **grader / actor-profiler queue item**
for the 2026-07-20 afternoon brief. Not graded here (grader's job); all attribution
recorded verbatim per Hard Rule 2.

## Procedural facts (per BleepingComputer relay of Group-IB)

- **HollowGraph** is a malicious component that abuses the **calendar feature of
  compromised Microsoft 365 mailboxes** as a command-and-control channel — reading
  attacker commands from and exfiltrating stolen data through calendar items via the
  **Microsoft Graph API** (living-off-trusted-cloud-service C2, blends with legitimate
  M365 traffic).
- **Tooling / framework linkage:** Group-IB assesses HollowGraph "with high confidence"
  as linked to the **Cavern C2 framework**, which the report describes as previously
  associated with Iranian threat actors targeting Israeli entities.
- **Similarity note (low confidence):** Group-IB observed technical similarities with
  the Iranian-nexus actor **Lyceum**, but states the available evidence is
  "insufficient to attribute the activity to the threat actor with high confidence."
- **Targeting:** primarily **Israel**; espionage-focused, targeted intrusion set.
- **Scope:** at least **12 systems infected**; 3 actively communicating with the
  operators between **2026-06-03 and 2026-07-09**.
- **IOCs disclosed:** C2/tunneling domain **cloudlanecdn[.]com** (DNS tunneling for
  credential/token refresh) and config-storage file **logAzure.txt**. No file hashes
  or IPs disclosed in the relay.
- **No CVE** referenced. **No aerospace or defense victim named.**

## Why in-scope (roster relationship)

The **Cavern C2 framework** ("Cavern" / "Cav3rn" modular .NET C2) is the distinctive
tooling tracked to **Cavern Manticore (Actor #026, Iran-MOIS)** in `_roster.yaml`
(first-pass dossier 2026-07-07, from finding-2026-07-06-0001 / Check Point Research;
tracked C2 domain hospitalinstallation[.]com). This Group-IB report is potentially a
NEW development on the same Cavern-framework cluster — a fresh capability (Microsoft
Graph / M365 calendar C2 via HollowGraph) and fresh IOC (cloudlanecdn[.]com) attached
to the framework, from an INDEPENDENT vendor (Group-IB) to the CPR originating source.
This is exactly the "tracked-actor-associated tooling, new capability/infrastructure"
shape the grader and actor-profiler should adjudicate. **No actor attribution asserted
here** — Group-IB links the tooling/framework and offers a low-confidence Lyceum
similarity; whether HollowGraph belongs to Cavern Manticore #026 (vs. a distinct
Cavern-framework operator) is an open analytic question for downstream, mirroring the
standing SAT-ACH question on finding-2026-07-06-0001 (distinct cluster vs.
MuddyWater/OilRig sub-cluster).

---

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas (BleepingComputer, B-grade relay)
- Originating research: Group-IB — FIRST-CORPUS-SURFACE (no existing `source-grades.yaml`
  id; grader to assign a provisional first-surface grade. Group-IB is a Tier-1/Tier-2
  DFIR/threat-intel vendor with named-analyst APT research; precedent points toward
  provisional-A or provisional-B first surface per SentinelLabs / Bitdefender / Socket
  precedents — grader's call).
- Article type: blog / vendor-relay news
- Raw IOC extraction invoked: yes
- Copyright: no verbatim quote >15 words; Group-IB confidence hedges short-quoted once each
- First-party Splunk sweep (this collection, -90d, archimedes + defenseclaw_local):
  0 hits on cloudlanecdn[.]com, hospitalinstallation[.]com (Cavern Manticore #026 C2),
  HollowGraph, logAzure — visibility-bounded null, no corroboration bonus (Frank not an
  Israeli target). Trigger 3 (first-party-IOC-hit) does NOT fire.
- A&D relevance: LOW / structural-indirect. Israel-targeted espionage; NO A&D prime or
  DIB victim named. Relevance is (a) Iran-nexus roster-adjacency (Cavern Manticore #026
  is a tracked Iran-MOIS espionage cluster) and (b) the M365-Graph-calendar C2 TTP is
  portable to any Microsoft-365 tenant including A&D primes — recorded as TTP-watch
  interest, NOT asserted targeting.

## FLASH trigger disposition (why NON-flash, pre-brief item)

- **T1 critical-cve-exploited:** no CVE. FAIL.
- **T2 tracked-actor-attribution:** Group-IB links the Cavern C2 *framework/tooling* but
  does NOT attribute the activity to a `_roster.yaml` actor with high confidence (explicit
  "insufficient to attribute" on Lyceum). No new hardened roster attribution → FAIL.
- **T3 first-party-IOC-hit:** Splunk null this sweep. FAIL.
- **T4 tracked-actor-TTP-change:** would require an attributable roster actor; framework
  linkage is tooling-level, actor unconfirmed. FAIL (grader may still treat as
  Cavern-cluster capability development for the scheduled brief).
- **T5 A&D-sector-campaign:** Israel-targeted; NO named A&D victim, no A&D multi-victim. FAIL.
- **T6 zero-day-no-patch:** no vulnerability disclosed. FAIL.

Correctly a pre-brief grader/actor-profiler-queue item, not a FLASH candidate.

## IOCs (ioc-extraction skill output)

```yaml
domains:
  - value: cloudlanecdn.com
    defanged_original: "cloudlanecdn[.]com"
    type: domain
    role: c2_dns_tunneling
    context: "DNS tunneling for credential/token refresh (per Group-IB via BleepingComputer)"
    source_brief_id: raw-2026-07-20-pm-001
    actor_id: null            # tooling-linked (Cavern C2 framework), actor unconfirmed — grader/actor-profiler to resolve
file_paths:
  - value: logAzure.txt
    type: file_path
    role: config_storage
    context: "HollowGraph configuration storage file"
    source_brief_id: raw-2026-07-20-pm-001
    actor_id: null
tooling:
  - name: HollowGraph
    type: malware
    detail: "M365-mailbox-calendar C2 via Microsoft Graph API; living-off-trusted-cloud-service"
  - name: "Cavern C2 framework"
    type: c2_framework
    detail: "Group-IB high-confidence linkage; = 'Cavern'/'Cav3rn' modular .NET C2 tracked to Cavern Manticore #026"
cves: []
network_iocs_ip: []
hashes: []
credentials_observed: false     # article references credential/token refresh mechanism; NO credential values published or stored (Hard Rule 7)
attribution_claims:
  - claim: "HollowGraph linked to the Cavern C2 framework"
    attributed_by: Group-IB
    confidence_language: "with high confidence"
    scope: tooling_framework_linkage        # NOT an actor attribution
    roster_match: false
  - claim: "technical similarities with Iranian-nexus actor Lyceum"
    attributed_by: Group-IB
    confidence_language: "insufficient to attribute ... with high confidence"
    scope: low_confidence_similarity
    roster_match: false                      # Lyceum = OilRig/APT34 #023 subgroup per CPR; NOT asserted here (Hard Rule 2)
  - claim: "Cavern framework previously associated with Iranian threat actors targeting Israeli entities"
    attributed_by: Group-IB
    confidence_language: "previously associated"
    scope: framework_provenance
    roster_relationship: "Cavern Manticore #026 (Iran-MOIS) operates the Cavern/Cav3rn framework per CPR/finding-2026-07-06-0001 — relationship recorded, NOT hardened to actor attribution"
```
