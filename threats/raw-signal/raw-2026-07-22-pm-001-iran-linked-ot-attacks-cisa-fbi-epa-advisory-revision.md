---
raw_id: raw-2026-07-22-pm-001
collected_at: 2026-07-22T15:36:00-04:00
run_id: pre-brief-20260722-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: the-record
  source_name: "The Record from Recorded Future News"
  source_url: https://therecord.media/federal-agencies-broaden-alert-on-iran-linked-ot-attacks
  published_at: 2026-07-22T15:18:00-04:00
match_reason:
  watchlist: [iran-cyber]
  actors: ["028"]              # CyberAv3ngers — TTP/advisory-line match (NOT source-originated attribution; Hard Rule 2)
  vulnerabilities: [CVE-2021-22681]   # VT-027 Rockwell Logix — structurally implicated (Rockwell/Allen-Bradley PLCs named); NOT named in the advisory per relay
  keywords: [Iran, OT, ICS, HMI, SCADA, PLC, "project file", Rockwell, Schneider, Siemens, "critical infrastructure", CISA, FBI, EPA]
triage_tags: [non_flash, iran_cyber, ot_ics_campaign, government_advisory, ad_sector_structural, actor_ttp_match, advisory_revision]
iocs_extracted: true
iocs_count: 0
text_word_count: 340
promoted: true
promoted_to_finding: finding-2026-07-22-0004
promoted_at: 2026-07-22T16:24:00-04:00
ttl_expires_at: 2026-10-20T15:36:00-04:00
---

# CISA / FBI / EPA broaden alert on Iran-linked OT attacks (revision of April 2026 advisory) — HMI/SCADA manipulation, PLC targeting

**State this window (07:30 → 15:30 EDT, afternoon pre-brief):** The Record (Recorded
Future News, 2026-07-22 ~15:18 EDT) relayed a revised joint advisory from **CISA, FBI,
and the Environmental Protection Agency (EPA)** broadening an earlier April 2026 alert
on **Iranian regime-affiliated** cyber activity against operational-technology (OT)
environments in US critical infrastructure.

Per the relay, the advisory describes observed incidents including *"malicious project
file interactions and manipulation of data on human machine interface (HMI) and
supervisory control and data acquisition (SCADA) displays,"* with affected organizations
experiencing operational disruption and financial loss. Targeting focuses on
**internet-facing programmable logic controllers (PLCs)** from **Rockwell Automation /
Allen-Bradley, Schneider Electric, Siemens**, and possible other PLC manufacturers.

Named sectors: power utilities, wastewater treatment, and manufacturing plants. **No
aerospace, defense, or DIB entity is named.**

## Why raw-signaled (Mode 1 — matches Iran Cyber Watch + roster-actor TTP line + tracked-CVE structural)

- **Iran Cyber Watch** standing section match (Iranian state-affiliated OT activity).
- **Advisory-line continuity:** this is presented as a **revision/broadening of the
  April 2026 advisory** — the corpus's April six-agency Iran-OT advisory is **AA26-097A**,
  already attributed in-corpus to **CyberAv3ngers (Actor #028, IRGC-CEC)** whose documented
  TTPs are exactly the ones described here (HMI/SCADA display manipulation, malicious
  project-file interaction, internet-facing PLC targeting, confirmed disruption + financial
  loss). The Rockwell/Allen-Bradley PLC targeting structurally implicates **VT-027
  (CVE-2021-22681)**, CyberAv3ngers' primary tracked CVE.
- **A&D relevance HIGH / structural-indirect:** Rockwell Logix + Siemens + Schneider PLCs
  are pervasive in A&D manufacturing / test-range / facility OT. No named A&D victim — the
  relevance is attack-surface-shared, not a disclosed prime intrusion.

## Attribution — recorded verbatim, NOT originated (Hard Rule 2)

The advisory (per the relay) **does not name a specific threat group** — attribution is
generic **"Iranian regime-affiliated"** / Iranian-government-affiliated. The Record adds a
caveat that attribution is difficult because the regime "sometimes uses ransomware gangs or
other groups as cover." Archimedes does NOT assert CyberAv3ngers here; the #028 linkage is
recorded as an **advisory-line + TTP correspondence** to the same April AA26-097A activity
the corpus already tracks, for the grader/actor-profiler to adjudicate. No new attribution
originated.

**FLASH evaluation (for grader awareness — pre-brief, not a FLASH sweep):** Trigger 5
(ad-sector-campaign) FAILS on no-named-A&D/DIB-victim + no multi-victim A&D confirmation;
Trigger 2/4 (actor attribution / TTP change) do not cleanly fire because the advisory names
no specific group (generic Iran) and describes no net-new TTP vs the April AA26-097A baseline
— this is a **broadening/restatement** of known activity, not a first attribution or a TTP
shift. Routed as afternoon-brief material for the Iran Cyber Watch + A&D sector sections.

## Extraction notes

- Language: en
- Publisher byline: The Record / Recorded Future News (staff; no byline in relay)
- Article type: trade-press relay of a CISA/FBI/EPA joint OT advisory
- Raw IOC extraction invoked: yes — no atomic IOCs in the relay
- Underlying government primary (CISA/FBI/EPA advisory) NOT directly retrieved this sweep —
  direct-retrieval todo (advisory ID + verbatim attribution string + any IOC appendix);
  A-grade government primary relayed via B-grade The Record.

## IOCs (from ioc-extraction skill)

```yaml
atomic_iocs: []            # no IPs / domains / hashes in the relay
cve_references:
  - id: CVE-2021-22681
    product: "Rockwell Automation Logix controllers / Studio 5000 (VT-027)"
    type: "authentication bypass (CWE-522) — structurally implicated, NOT named in advisory"
    exploitation_status: "actively exploited (KEV 2026-03-05); this advisory reinforces the OT/PLC targeting pattern but does not cite the CVE per the relay"
    note: "Recorded as structural linkage to CyberAv3ngers' primary tracked CVE; advisory names no CVE"
attribution_claims:
  - actor: "Iranian regime-affiliated / Iranian-government-affiliated (generic — no specific group named)"
    attributed_by: "CISA + FBI + EPA joint advisory (revision of April 2026 advisory), relayed by The Record"
    confidence_language: "advisory does not name specific threat groups; The Record caveat: regime 'sometimes uses ransomware gangs or other groups as cover'"
    corpus_note: "April 2026 predecessor = AA26-097A, in-corpus attributed to CyberAv3ngers (#028); linkage is advisory-line + TTP correspondence only, NOT Archimedes-originated attribution (Hard Rule 2)"
notes: "No PoC/exploit content (Hard Rule 3). No credentials (Hard Rule 7 N/A). Government primary via B-grade relay — pending direct retrieval of the CISA/FBI/EPA advisory."
```
