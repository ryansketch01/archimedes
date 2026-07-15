---
raw_id: raw-2026-07-14-pioneer-newactor-002
collected_at: 2026-07-14T16:48:00-04:00
run_id: pioneer-newactor-20260714-1630
collection_mode: on_demand
on_demand_command: /new-actor Pioneer Kitten (net-new roster actor — vendor alias-cluster + attribution-taxonomy collection pass)
source:
  # Aggregated vendor-designation + attribution taxonomy across the Tier-1
  # bodies that independently track this actor. Load-bearing structured
  # reference = MITRE ATT&CK G0117 (A-grade, curated), which maps each vendor's
  # alias to the same cluster. Dragos PARISITE page retrieved DIRECTLY.
  source_yaml_id: mitre-attack
  source_name: "Vendor alias cluster — CrowdStrike (PIONEER KITTEN), Mandiant/CISA (UNC757), Dragos (PARISITE), Microsoft (RUBIDIUM / Lemon Sandstorm), ClearSky (Fox Kitten), via MITRE ATT&CK G0117"
  source_url: https://attack.mitre.org/groups/G0117/
  dragos_primary_url: https://www.dragos.com/threat/parisite/
  crowdstrike_url: https://www.crowdstrike.com/en-us/adversaries/pioneer-kitten/
  relay_urls:
    - https://malpedia.caad.fkie.fraunhofer.de/actor/fox_kitten
    - https://fortiguard.fortinet.com/threat-actor/5570/fox-kitten
  published_at: 2024-08-28T00:00:00-04:00
admiralty_pre_grade: A2
admiralty_pre_grade_rationale: >
  MITRE G0117 is A-grade curated reference; Dragos PARISITE page retrieved
  directly (A-grade vendor primary). CrowdStrike PIONEER KITTEN attribution
  surfaced via WebSearch summary this pass (CrowdStrike adversary page not
  directly fetched — awaiting_direct_retrieval). Aggregated taxonomy = well-
  corroborated FACT of the alias cluster; individual vendor attribution
  confidence phrasings preserved separately. Collector convenience flag only.
relay_vs_primary: mixed      # MITRE curated + Dragos direct primary; CrowdStrike/Mandiant/Microsoft via relay/search this pass
match_reason:
  watchlist: [aerospace-defense]     # Dragos names AEROSPACE + oil&gas + ICS/OT among PARISITE targets
  actors: [Pioneer Kitten, Fox Kitten, UNC757, Parisite, RUBIDIUM, Lemon Sandstorm]
  vulnerabilities: [CVE-2019-19781, CVE-2019-11510]
  keywords: [IRGC, PIONEER KITTEN, UNC757, PARISITE, RUBIDIUM, Lemon Sandstorm, Pay2Key, ICS, OT, aerospace, access broker]
  match_basis: >
    Resolves the multi-vendor alias cluster for the net-new Pioneer Kitten
    build and records each vendor's attribution language separately (Hard Rule
    2). Captures the Dragos AEROSPACE/oil&gas/ICS sector list (A&D-relevant) and
    the CrowdStrike IRGC-alignment framing that is crisper than the AA24-241A
    "Government of Iran" wording in companion file ...-001.
triage_tags: [new_actor_seed, iran_irgc, alias_cluster, vendor_crosswalk, ics_ot_targeting, aerospace_named_dragos, attribution_taxonomy, on_demand_newactor]
iocs_extracted: true
iocs_count: 0        # taxonomy/attribution file; no net-new atomic IOCs (malware family names recorded as tooling, not IOCs)
text_word_count: 1010
promoted: false
ttl_expires_at: 2026-10-12T16:48:00-04:00
---

# Pioneer Kitten — vendor alias cluster & attribution taxonomy (MITRE G0117 + Dragos + CrowdStrike + Microsoft)

Companion to `...-001` (the AA24-241A US-gov foundation). This file resolves the
multi-vendor naming and records EACH vendor's attribution phrasing separately so
the profiler inherits the alias cluster as the vendors' designations — NOT an
Archimedes-originated merge (Hard Rule 2).

## Alias cluster — who calls it what (per MITRE ATT&CK G0117, A-grade curated)

| Designation | Assigning vendor(s) |
|---|---|
| **Pioneer Kitten** | CrowdStrike, CISA |
| **Fox Kitten** | ClearSky, Dragos, CrowdStrike |
| **UNC757** | Mandiant, CISA |
| **Parisite** | Dragos, ClearSky |
| **RUBIDIUM** | Microsoft |
| **Lemon Sandstorm** | Microsoft (current; formerly RUBIDIUM) |

MITRE folds all of the above into one group (G0117). The equivalence is
**MITRE's / the vendors' mapping**, not an Archimedes assertion.

Proposed roster alias set (for the profiler to ratify): primary_name
**Pioneer Kitten**; aliases [Fox Kitten, UNC757, Parisite, RUBIDIUM, Lemon
Sandstorm]; access-broker persona [Br0k3r, xplfinder] (from `...-001`).

## Attribution language — recorded PER VENDOR (Hard Rule 2, do not harden)

- **MITRE ATT&CK (G0117) — verbatim:**
  > "threat actor with a **suspected nexus to the Iranian government**"

  MITRE uses "suspected," active "since at least 2017."

- **CrowdStrike (PIONEER KITTEN) — per WebSearch summary of CrowdStrike framing
  this pass:** CrowdStrike tracks the actor as an **Iran-based** adversary with a
  **suspected nexus to the Iranian government**, widely assessed to operate in
  alignment with **IRGC** (Islamic Revolutionary Guard Corps) intelligence
  objectives while running a parallel commercial access-selling operation.
  CrowdStrike lists Pioneer Kitten among **IRGC**-attributed Iranian groups
  (alongside APT33, APT35, APT42, CyberAv3ngers, Cotton Sandstorm).
  *CAVEAT: CrowdStrike's own adversary page was NOT directly fetched this pass
  (WebSearch summary only) — the IRGC-alignment phrasing is
  awaiting_direct_retrieval before it should be quoted as verbatim CrowdStrike
  language.*

- **Dragos (PARISITE) — retrieved DIRECTLY, verbatim:**
  > "Dragos does not corroborate nor conduct political attribution to threat
  > activity."

  Dragos deliberately does NOT assign nation-state/IRGC attribution. It tracks
  PARISITE as an activity group by TTP. Important nuance: the "Iranian" label on
  the PARISITE cluster comes from the IT-vendor layer (ClearSky/CrowdStrike/
  Microsoft), NOT from Dragos.

- **Microsoft (RUBIDIUM → Lemon Sandstorm):** Iranian nation-state actor;
  Microsoft's "Sandstorm" suffix denotes Iran-nexus in its weather taxonomy.
  (Attribution detail via MITRE + Fortinet relay; Microsoft primary blog not
  directly fetched this pass.)

**Net attribution picture for the grader:** the US-gov primary (`...-001`) says
"Government of Iran"; CrowdStrike/industry sharpen to **IRGC-aligned**; MITRE
hedges to "suspected nexus"; Dragos abstains entirely. The dossier should carry
attribution as **IR / IRGC-linked** with the confidence-language spread noted —
NOT a flat "IRGC-directed."

## Sectors targeted (per vendor — A&D relevance)

- **Dragos (PARISITE), verbatim sector list:** **Oil & Gas, Aerospace,
  Utilities (water/electric/gas), Government, NGOs.** Dragos explicitly names
  **AEROSPACE** — the most A&D-relevant sector attribution in the cluster,
  though Dragos frames PARISITE activity as IT-network initial-access/recon
  against ICS-related entities, and states: "At this time, PARISITE does not
  appear to have an ICS-specific disruptive or destructive capability."
- **MITRE G0117 sector list:** oil & gas, technology, government, **defense**,
  healthcare, manufacturing, engineering.
- **Geography (MITRE + Dragos):** Middle East, North Africa, Europe, Australia,
  North America.

**A&D-scoring note:** Dragos "Aerospace" + MITRE "defense" are SECTOR-level
attributions. Neither (in the content retrieved this pass) names a specific US
A&D PRIME / DIB contractor victim. This mirrors the `...-001` caveat — the
Intent=5 (Target-Specific) evidence-minimum bar likely is NOT met on sector-list
attributions alone; profiler decides. This is the single recurring open question
across all three collection files.

## Tooling / malware associated (recorded as named tooling, NOT as IOCs)

Per MITRE G0117: **China Chopper** (web shell), **ngrok**, **Pay2Key**
(ransomware — the actor's own earlier ransomware, 2020 Israel campaign),
**PsExec**, **SystemBC**. Recent-campaign backdoors (HanifNet, HXLibrary,
NeoExpressRAT, Havoc) are in companion file `...-003`. No atomic hashes for
these were retrieved this pass — families recorded as tooling only.

---

## Extraction notes

- Language: en
- Publisher bylines: MITRE ATT&CK (curated, G0117); Dragos (team, PARISITE
  threat page); CrowdStrike (adversary page — via WebSearch summary, not direct
  fetch); Microsoft (via MITRE/Fortinet relay).
- Article type: curated ATT&CK reference (primary-structured) + vendor threat
  pages.
- Originating primaries: MITRE (curated) + Dragos (direct). CrowdStrike +
  Microsoft attribution surfaced via search/relay this pass — flagged
  awaiting_direct_retrieval for the exact quotations.
- Relay-vs-primary: MIXED. MITRE G0117 and Dragos are directly-retrieved
  A-grade; CrowdStrike PIONEER KITTEN and Microsoft RUBIDIUM/Lemon Sandstorm
  attribution are relay/search-derived this pass (facts corroborated, exact
  vendor quotations pending).
- Hard Rule 2: every alias recorded as the ASSIGNING VENDOR'S designation; the
  cross-vendor equivalence is MITRE's/the vendors' mapping, not Archimedes-
  originated. Attribution confidence phrasing preserved per vendor; Dragos's
  explicit non-attribution recorded verbatim so it is not overwritten by the
  IT-vendor "Iranian" label.
- Hard Rule 3: CVEs by ID only (see ...-001 for full set); no exploit content.
- Hard Rule 7: no credentials surfaced.

## IOCs (ioc-extraction output)

```yaml
extraction_metadata:
  source_brief_id: mitre-g0117-vendor-cluster-2024
  source_url: https://attack.mitre.org/groups/G0117/
  extracted_at: 2026-07-14T16:48:00Z
  extracted_by: collector
  target_actor_id: null
  text_word_count: 1010

indicators: []      # taxonomy/attribution file — no net-new atomic IOCs. Malware family names recorded as tooling in body, not folded as indicators.

attribution_claims:
  - claimant: "MITRE ATT&CK (G0117)"
    claim: "Fox Kitten / Pioneer Kitten / UNC757 / Parisite / RUBIDIUM / Lemon Sandstorm are one group with a suspected nexus to the Iranian government, active since at least 2017"
    nation_named: Iran
    service_named: "Iranian government (unspecified service)"
    confidence_language: "suspected nexus"
    linkage_type: alias_cluster_equivalence
    requires_grading: true
  - claimant: "CrowdStrike (PIONEER KITTEN) — via WebSearch summary, direct page pending"
    claim: "Pioneer Kitten is IRGC-aligned, operating in alignment with IRGC intelligence objectives while running a parallel commercial access-selling operation"
    nation_named: Iran
    service_named: IRGC
    confidence_language: "widely assessed to operate in alignment with IRGC (industry consensus framing)"
    awaiting_direct_retrieval: true
    requires_grading: true
  - claimant: "Dragos (PARISITE)"
    claim: "Dragos tracks PARISITE by TTP and explicitly does NOT conduct political/nation-state attribution"
    nation_named: null
    service_named: null
    confidence_language: "does not corroborate nor conduct political attribution (verbatim, deliberate abstention)"
    requires_grading: true
  - claimant: "Microsoft"
    claim: "RUBIDIUM (renamed Lemon Sandstorm) is an Iran-nexus nation-state actor"
    nation_named: Iran
    service_named: "Iran-nexus (Sandstorm = Iran in MSFT taxonomy)"
    confidence_language: "nation-state (Sandstorm taxonomy)"
    awaiting_direct_retrieval: true
    requires_grading: true
```
</content>
