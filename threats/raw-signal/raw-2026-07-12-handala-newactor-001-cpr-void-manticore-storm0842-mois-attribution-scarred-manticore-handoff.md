---
raw_id: raw-2026-07-12-handala-newactor-001
collected_at: 2026-07-12T23:40:00-04:00
run_id: handala-newactor-20260712-2300
collection_mode: on_demand
on_demand_command: /new-actor Handala Hack (roster #014 — targeted dossier-seed collection pass)
source:
  # Load-bearing attribution primary = Check Point Research "Bad Karma, No Justice"
  # (2024). Vendor-designation crosswalk corroborated by The Hacker News (relay of
  # CPR) and MITRE ATT&CK G1055 (structured, A-grade). CPR primary retrieved via
  # WebFetch summarization (anti-bot risk on the raw appendix — see IOC caveat).
  source_yaml_id: checkpoint-research
  source_name: Check Point Research — "Bad Karma, No Justice: Void Manticore Destructive Activities in Israel"
  source_url: https://research.checkpoint.com/2024/bad-karma-no-justice-void-manticore-destructive-activities-in-israel/
  corroborating_source_url: https://thehackernews.com/2024/05/iranian-mois-linked-hackers-behind.html
  mitre_source_url: https://attack.mitre.org/groups/G1055/
  published_at: 2024-05-20T00:00:00-04:00
match_reason:
  watchlist: []            # no A&D-prime victim in this foundational report
  actors: [Handala Hack, Void Manticore, Storm-0842, DEV-0842, Scarred Manticore, Storm-0861]
  vulnerabilities: []
  keywords: [Void Manticore, Storm-0842, DEV-0842, MOIS, Iran, BiBi wiper, Cl Wiper, Partition wipers, Karma, Homeland Justice, Scarred Manticore, Storm-0861, wiper, hack-and-leak, destructive]
  match_basis: >
    Targeted /new-actor collection pass to seed roster #014 (Handala Hack,
    "profile pending" stub). This file captures the FOUNDATIONAL attribution
    layer: CPR's Void Manticore = MOIS attribution, the Microsoft Storm-0842
    (formerly DEV-0842) designation crosswalk, the Void Manticore <-> Scarred
    Manticore (Microsoft: Storm-0861) target-handoff relationship, and the named
    wiper toolset. Handala-persona <-> Void Manticore equivalence and 2024-2026
    persona operations are captured in companion file raw-2026-07-12-handala-newactor-002.
triage_tags: [new_actor_seed, iran_mois, destructive_wiper, vendor_crosswalk, attribution_foundation, scarred_manticore_handoff, on_demand_newactor]
iocs_extracted: true
iocs_count: 5             # 5 C2 IPs; hashes reported-but-unverified (see caveat)
text_word_count: 1100
promoted: false
ttl_expires_at: 2026-10-10T23:40:00-04:00
---

# Bad Karma, No Justice: Void Manticore Destructive Activities in Israel (Check Point Research, May 2024)

Foundational attribution and tooling report for the actor Ryan tracks as roster
#014 **Handala Hack** (aliases Void Manticore, Storm-0842, DEV-0842). This file
records the vendor attribution layer; the Handala-persona operational history and
2026 IOCs are in the companion file `...-002`.

## Vendor attribution — recorded verbatim per Hard Rule 2 (NOT Archimedes-originated)

- **Check Point Research (A-grade), MOIS attribution — verbatim:**
  > "Void Manticore is an Iranian threat actor affiliated with the Ministry of
  > Intelligence and Security (MOIS)."

  CPR states the MOIS affiliation directly, without hedge markers ("likely" /
  "assessed"). This is the load-bearing attribution the roster #014 entry inherits.

- **Vendor-designation crosswalk (per The Hacker News relaying CPR, corroborated by MITRE G1055):**
  > "Cybersecurity firm Check Point is tracking the activity under the moniker
  > Void Manticore ... also referred to as Storm-0842 (formerly DEV-0842) by
  > Microsoft."

  So: **CPR "Void Manticore" == Microsoft "Storm-0842" (formerly "DEV-0842")** is
  a stated equivalence made by the reporting, NOT originated by Archimedes. This
  ratifies the roster #014 alias set [Void Manticore, Storm-0842, DEV-0842].

- **MITRE ATT&CK G1055 (A-grade, structured) — assessed-affiliation wording:**
  > "VOID MANTICORE is a threat group assessed to operate on behalf of Iran's
  > Ministry of Intelligence and Security (MOIS)."

  MITRE uses the softer "assessed to operate on behalf of" vs. CPR's flat
  "affiliated with." Both land on MOIS; the confidence phrasing differs. Recorded
  for the grader — do not harden to a single phrasing.

## Void Manticore <-> Scarred Manticore relationship (the "structured collaboration")

Capture exactly how strongly the collaboration is stated — this is an
attribution-adjacent claim, not to be hardened.

- **CPR — verbatim:**
  > "There are clear overlaps between the targets of Void Manticore and Scarred
  > Manticore, with indications of systematic hand off of targets between those
  > two groups when deciding to conduct destructive activities against existing
  > victims of Scarred Manticore."

- **CPR handoff mechanism — verbatim:**
  > "a new web shell was dropped to disk. Following the shell's deployment, a
  > different set of IPs began accessing the network, suggesting the involvement
  > of another actor – Void Manticore."

- **Designation:** Scarred Manticore is tracked by Microsoft as **Storm-0861**
  (per THN relay of CPR). CPR frames the two as SEPARATE but COLLABORATING actors
  — Scarred Manticore performs initial access + stealthy exfiltration, then hands
  the access to Void Manticore for the destructive phase. CPR does NOT merge the
  two into one entity; the language is "overlaps," "systematic hand off,"
  "suggesting the involvement of another actor." Do NOT record this as an
  equivalence.

## Named wiper / destructive tooling (CPR 2024, corroborated THN)

CPR characterizes Void Manticore as reliant on manual, hands-on operations plus a
mix of CUSTOM wipers and off-the-shelf tooling:

- **BiBi Wiper** (Windows and Linux variants) — CPR: custom. THN attributes BiBi
  specifically to Void Manticore's "Karma" persona operating against Israel
  post-October 2023.
- **Cl Wiper** — custom; uses the **ElRawDisk** driver (commercial disk-access
  driver abused for raw disk writes).
- **Partition Wipers** — custom family; variants named LowEraser / "No-Justice",
  Pinky, JustMBR (partition-table / MBR destruction).
- **Karma Shell** — custom web shell (persona-branded).
- **reGeorge** — publicly available (off-the-shelf) HTTP tunneling tool. NOT a
  wiper; used for tunneling/pivot.

Note: MITRE G1055's software list (retrieved same pass) additionally cross-links
the broader cluster to **CHIMNEYSWEEP** (S1149), **ROADSWEEP** (S1150,
ransomware/encryptor), **ZeroCleare** (S1151, disk wiper), and **RawDisk**
(S0364) — these reflect the combined Karma/Homeland-Justice cluster MITRE folds
under G1055 (ROADSWEEP + ZeroCleare are historically the Homeland Justice /
Albania toolset). Recorded as MITRE's cluster mapping, not a CPR claim.

## Targeting (this report)

- **Israel:** CPR notes 40+ claimed Israeli victim organizations; specific names
  withheld in the public report.
- **Albania:** destructive campaigns via the "Homeland Justice" persona
  (2022–2024), the earlier well-documented Void Manticore theatre.
- No aerospace/defense prime named in THIS foundational report. A&D-supplier
  spillover relevance is assessed in companion file `...-002` (Stryker medical-
  device compromise) — indirect to the ad-prime target profile, not direct.

---

## Extraction notes

- Language: en
- Publisher bylines: Check Point Research (team); The Hacker News (Ravie
  Lakshmanan, 2024-05-20); MITRE ATT&CK G1055 (curated).
- Article type: vendor threat-research report (CPR) + news relay (THN) + curated
  KB (MITRE).
- Originating primary: Check Point Research. CPR raw report retrieved via WebFetch
  summarization; the raw IOC appendix was NOT cleanly retrieved (CPR site
  anti-bot). Treat hash values below as REPORTED-BUT-UNVERIFIED — see caveat.
- Raw IOC extraction invoked: yes.
- Single-source discipline (NOT grading, grader's call): CPR is the sole
  ORIGINATING A-grade primary on the Void Manticore/MOIS attribution and the
  Scarred Manticore handoff. THN is a pure relay of CPR (not independent
  corroboration). MITRE G1055 is independent on the FACT of the cluster + aliases
  + MOIS assessment (A-grade, its own curation) and DOES provide a second,
  independent-of-CPR statement of the MOIS attribution — the grader should weigh
  whether MITRE's curation counts as independent corroboration or is itself
  CPR-derived. Recorded both; not resolving here.
- Hard Rule 3: no exploit/PoC content. ElRawDisk/ReGeorge/wiper mechanics
  described by name and function only; no code.
- Hard Rule 7: no credentials surfaced in this report.

## IOCs (ioc-extraction output)

```yaml
extraction_metadata:
  source_brief_id: checkpoint-void-manticore-2024-05
  source_url: https://research.checkpoint.com/2024/bad-karma-no-justice-void-manticore-destructive-activities-in-israel/
  extracted_at: 2026-07-12T23:40:00Z
  extracted_by: collector
  target_actor_id: "014"
  text_word_count: 1100

indicators:
  # --- Network IOCs: 5 C2/operator IPs from the CPR 2024 report. ---
  # A SAMPLE was sanity-checked against VirusTotal this pass (see enrichment).
  - id: handala-ip-64-176-169-22
    type: ipv4
    value: "64.176.169.22"
    defanged_original: null
    role: c2
    campaign: "Void Manticore Israel destructive ops (Karma persona)"
    related_malware: [BiBi Wiper, Cl Wiper]
    source_brief: checkpoint-void-manticore-2024-05
    context_excerpt: "Operator IP in the CPR Void Manticore IOC set"
    attribution_in_text: Void Manticore
    enrichment:
      virustotal:
        found: true
        malicious: 10
        suspicious: 0
        country: IL
        asn: 20473
        as_owner: "The Constant Company, LLC"   # Vultr
        network: "64.176.160.0/19"
        flagged_by: [ADMINUSLabs, BitDefender, CRDF, "Chong Lua Dao", CyRadar, "Forcepoint ThreatSeeker", Fortinet, G-Data, SOCRadar, "alphaMountain.ai"]
        last_analysis_date: "2026-06-26T09:20:28+00:00"
      first_party_splunk:
        indices_checked: [defenseclaw_local, archimedes]
        window: "-90d"
        hits: 0
    notes: "VT-confirmed malicious (10 engines) as of 2026-06-26 — genuine IOC, not a WebFetch artifact."
  - id: handala-ip-64-176-172-235
    type: ipv4
    value: "64.176.172.235"
    defanged_original: null
    role: c2
    source_brief: checkpoint-void-manticore-2024-05
    context_excerpt: "Operator IP in the CPR Void Manticore IOC set (same Vultr /19 as .169.22)"
    attribution_in_text: Void Manticore
    enrichment:
      first_party_splunk: {indices_checked: [defenseclaw_local, archimedes], window: "-90d", hits: 0}
    notes: "Same-ASN cluster (Constant/Vultr AS20473) as the VT-confirmed .169.22 — not independently VT-checked this pass."
  - id: handala-ip-64-176-172-165
    type: ipv4
    value: "64.176.172.165"
    defanged_original: null
    role: c2
    source_brief: checkpoint-void-manticore-2024-05
    context_excerpt: "Operator IP in the CPR Void Manticore IOC set"
    attribution_in_text: Void Manticore
    enrichment:
      first_party_splunk: {indices_checked: [defenseclaw_local, archimedes], window: "-90d", hits: 0}
    notes: "Same Vultr /19 cluster; not independently VT-checked this pass."
  - id: handala-ip-64-176-173-77
    type: ipv4
    value: "64.176.173.77"
    defanged_original: null
    role: c2
    source_brief: checkpoint-void-manticore-2024-05
    context_excerpt: "Operator IP in the CPR Void Manticore IOC set"
    attribution_in_text: Void Manticore
    enrichment:
      first_party_splunk: {indices_checked: [defenseclaw_local, archimedes], window: "-90d", hits: 0}
    notes: "Same Vultr /19 cluster; not independently VT-checked this pass."
  - id: handala-ip-64-176-172-101
    type: ipv4
    value: "64.176.172.101"
    defanged_original: null
    role: c2
    source_brief: checkpoint-void-manticore-2024-05
    context_excerpt: "Operator IP in the CPR Void Manticore IOC set"
    attribution_in_text: Void Manticore
    enrichment:
      first_party_splunk: {indices_checked: [defenseclaw_local, archimedes], window: "-90d", hits: 0}
    notes: "Same Vultr /19 cluster; not independently VT-checked this pass."

  # --- Hashes REPORTED by CPR but NOT independently verifiable this pass. ---
  - type: note
    value: "CPR 2024 report lists ~6 SHA-256 wiper hashes (BiBi/Cl Wiper/Partition wipers). The values surfaced via WebFetch summarization did NOT resolve on VirusTotal (found:false on the two spot-checked), which is a strong signal the summarizer garbled the hash strings. Hash VALUES are therefore treated as PENDING DIRECT RETRIEVAL of the CPR IOC appendix — do NOT fold garbled hashes into iocs.yaml. Malware families (BiBi Windows/Linux, Cl Wiper, Partition wipers, Karma Shell) are recorded as named tooling; only the hash STRINGS are held pending."
    role: pending_retrieval

attribution_claims:
  - claimant: "Check Point Research"
    claim: "Void Manticore is an Iranian threat actor affiliated with the MOIS"
    nation_named: Iran
    service_named: MOIS
    actor_named: Void Manticore
    confidence_language: "affiliated with (flat, no hedge)"
  - claimant: "Microsoft (per THN relay of CPR)"
    claim: "The activity CPR calls Void Manticore is tracked by Microsoft as Storm-0842 (formerly DEV-0842)"
    linkage_type: vendor_designation_crosswalk
    confidence_language: "also referred to as"
  - claimant: "MITRE ATT&CK (G1055)"
    claim: "Void Manticore assessed to operate on behalf of Iran's MOIS"
    nation_named: Iran
    service_named: MOIS
    confidence_language: "assessed to operate on behalf of"
  - claimant: "Check Point Research"
    claim: "Void Manticore and Scarred Manticore (Microsoft: Storm-0861) show clear target overlaps with systematic hand-off of targets for destructive activity"
    linkage_type: collaboration_handoff_NOT_merge
    confidence_language: "clear overlaps / systematic hand off / suggesting the involvement of another actor"
    requires_grading: true
```
