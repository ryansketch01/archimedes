---
raw_id: raw-2026-07-14-pioneer-newactor-003
collected_at: 2026-07-14T16:54:00-04:00
run_id: pioneer-newactor-20260714-1630
collection_mode: on_demand
on_demand_command: /new-actor Pioneer Kitten (net-new roster actor — recent-campaign + first-party Splunk baseline pass)
source:
  # Most RECENT significant Pioneer Kitten (Lemon Sandstorm) campaign: the
  # FortiGuard Incident Response Team report on a ~2-year intrusion into a
  # Middle East critical national infrastructure (CNI) entity (May 2023 -> early
  # 2025, traces to 2021). Adds destructive-prepositioning signal + new backdoor
  # arsenal. Fortinet FortiGuard IR = originating A-grade vendor primary.
  source_yaml_id: fortinet-fortiguard
  source_name: "FortiGuard Incident Response Team — Investigating Iranian Intrusion into Strategic Middle East Critical National Infrastructure (Lemon Sandstorm)"
  source_url: https://www.fortinet.com/blog/threat-research/fortiguard-incident-response-team-detects-intrusion-into-middle-east-critical-national-infrastructure
  primary_report_pdf: https://www.fortinet.com/content/dam/fortinet/assets/reports/report-incident-response-middle-east.pdf
  relay_urls:
    - https://thehackernews.com/2025/05/iranian-hackers-maintain-2-year-access.html
    - https://www.darkreading.com/cyberattacks-data-breaches/lemon-sandstorm-risks-middle-east-infrastructure
  published_at: 2025-05-01T00:00:00-04:00
admiralty_pre_grade: A2
admiralty_pre_grade_rationale: >
  Fortinet FortiGuard IR is a Tier-1 vendor research/IR practice with first-party
  incident telemetry (analogous to the A-grade vendor-research precedent for
  Mandiant/CrowdStrike/Unit42/Dragos). NOTE fortinet-fortiguard is NOT yet a
  ratified entry in source-grades.yaml — this is its FIRST Archimedes-corpus
  surface; the grader/librarian should open a provisional-A entry (Tier-1
  vendor-research first-surface precedent, e.g. SentinelOne 2026-05-08). Content
  retrieved via WebSearch summary of the FortiGuard report + THN/DarkReading
  relays; FortiGuard primary PDF not directly rendered this pass. Collector
  convenience flag only, not a grading decision.
relay_vs_primary: primary_via_relay      # FortiGuard IR originating primary, via search/relay this pass
new_source_flag:
  source_yaml_id: fortinet-fortiguard
  status: first_corpus_surface
  action_for_librarian: "Open provisional source-grades.yaml entry for Fortinet FortiGuard Labs / FortiGuard IR (proposed provisional A, Tier-1 vendor-research first-surface precedent). Pending human ratification + direct-retrieval of the FortiGuard report PDF."
match_reason:
  watchlist: [aerospace-defense]     # CNI / prepositioning relevance to A&D-prime critical infra
  actors: [Lemon Sandstorm, Pioneer Kitten, Parisite, UNC757, RUBIDIUM]
  vulnerabilities: [CVE-2018-13379, CVE-2019-11510, CVE-2019-1579]
  keywords: [Lemon Sandstorm, critical national infrastructure, CNI, prepositioning, destructive, HanifNet, HXLibrary, NeoExpressRAT, Havoc, VPN exploitation, espionage]
  match_basis: >
    Captures the most recent major Pioneer Kitten (Lemon Sandstorm) campaign for
    the net-new dossier: a ~2-year CNI intrusion with SUSPECTED DESTRUCTIVE
    PREPOSITIONING — the single most important recent behavioral escalation for
    threat scoring, since it moves the actor beyond pure access-brokering toward
    potential effects operations against critical infrastructure. Also carries
    the first-party Splunk baseline sweep result for this build.
triage_tags: [new_actor_seed, iran_irgc, recent_campaign, cni_targeting, destructive_prepositioning, espionage, splunk_first_party_baseline, new_source_surface, on_demand_newactor]
iocs_extracted: true
iocs_count: 3        # 3 CVEs folded; backdoor family hashes/C2 held pending FortiGuard IOC-appendix direct retrieval
text_word_count: 780
promoted: false
ttl_expires_at: 2026-10-12T16:54:00-04:00
---

# FortiGuard IR — Lemon Sandstorm 2-year Middle East CNI intrusion (May 2023 → early 2025)

Recent-activity companion to `...-001` (US-gov foundation) and `...-002` (vendor
taxonomy). This file captures the most recent significant Pioneer Kitten /
Lemon Sandstorm campaign and the first-party Splunk baseline for the build.

## The campaign (per FortiGuard IR, via search + THN/DarkReading relays)

- **Victim:** a Middle Eastern **critical national infrastructure (CNI)** entity
  (unnamed).
- **Dwell time:** active intrusion from **May 2023** with initial-access traces
  back to **2021**, persistence maintained into **early 2025** — a ~2-year
  (up to ~4-year by first-trace) undetected campaign.
- **Attribution (FortiGuard, verbatim framing per relays):** tradecraft overlaps
  with the known Iranian nation-state actor **Lemon Sandstorm (formerly
  Rubidium)**, also tracked as **Parisite, Pioneer Kitten, and UNC757.**
  FortiGuard frames it as tradecraft-overlap attribution (not a flat
  identity claim) — preserve the "overlaps with" hedge per Hard Rule 2.

## Tooling / arsenal (recorded as named tooling)

Backdoors deployed via Scheduled Tasks disguised as legitimate system jobs:
- **HanifNet** — novel backdoor (command execution, file ops, system discovery)
- **HXLibrary** — novel backdoor
- **NeoExpressRAT** — novel RAT
- **Havoc** — open-source C2 framework (off-the-shelf)

This is a materially more capable, custom arsenal than the access-broker-era
web-shell/tunneler toolkit in `...-002` — a capability signal for scoring.

## Destructive-prepositioning signal (SCORING-CRITICAL — flag for profiler)

Per FortiGuard (relayed): researchers assess the attackers **"may have been
positioning themselves to carry out a future destructive attack"** against the
CNI target — extensive espionage PLUS suspected **network prepositioning** for
future strategic/destructive effect.

- This is the most important recent escalation: it pushes Lemon Sandstorm/
  Pioneer Kitten beyond pure espionage + access-brokering toward
  **potential effects/destructive operations** against critical infrastructure —
  the Volt-Typhoon-shaped "prepositioning" pattern.
- SCORING CAVEAT (Hard Rule 2): this is a **suspected/assessed** intent, hedged
  by FortiGuard ("may have been positioning"). Do NOT harden to a confirmed
  destructive capability. Dragos (`...-002`) separately states PARISITE has no
  observed ICS-specific destructive capability. Record the tension: espionage +
  suspected-prepositioning (FortiGuard) vs. no-observed-destructive-capability
  (Dragos). The profiler weighs both.

## Edge/VPN CVEs (this campaign; Hard Rule 3 — IDs only)

- **CVE-2018-13379** — Fortinet FortiOS SSL VPN path traversal
- **CVE-2019-11510** — Pulse Secure arbitrary file read (also in ...-001)
- **CVE-2019-1579** — Palo Alto Networks GlobalProtect SSL VPN RCE

## First-party Splunk baseline (Mode-4 corroboration, Hard Rule 8)

Run this pass against Frank's Splunk (health: reachable, v10.2.2, both indices
live). Sweep over **-90d** across `archimedes` + `defenseclaw_local` for the
full Pioneer Kitten indicator set (7 CVEs from ...-001 + this file's 3 CVEs +
aliases Pioneer/Fox Kitten, UNC757, Lemon Sandstorm + persona handles
Br0k3r/xplfinder + candidate domain gupdate.net):

- **Result: 0 hits.**
- **Index liveness (control):** archimedes = 1,725 events / -90d;
  defenseclaw_local = 6 events / -90d. Both indices confirmed live (not a dead-
  feed false-null).
- **Interpretation:** **visibility-bounded null — NO first-party corroboration,
  and NO corroboration bonus.** Frank is not a Pioneer Kitten victim environment
  and has no A&D-prime-scale edge-VPN telemetry; a categorical zero here is
  expected and carries no evidential weight either direction. Consistent with
  prior new-actor builds (Handala #014, CyberAv3ngers #028, Peach Sandstorm #027
  all logged the same visibility-bounded null).

---

## Extraction notes

- Language: en
- Publisher bylines: FortiGuard Incident Response Team (Fortinet, team byline).
  Relays: The Hacker News (2025-05); Dark Reading; Israel Defense.
- Article type: vendor incident-response report (primary) via search/news relay.
- Originating primary: FortiGuard IR. Primary blog + report PDF NOT directly
  rendered this pass (WebSearch summary + THN/DarkReading relays) — the atomic
  IOC appendix (HanifNet/HXLibrary/NeoExpressRAT hashes, C2 IPs/domains) is
  **PENDING DIRECT RETRIEVAL** of the FortiGuard report. Only the 3 campaign
  CVEs (corroborated across relays) are folded as indicators.
- Relay-vs-primary: A-grade originating vendor primary, reconstructed via
  search + B-grade relays this pass.
- NEW SOURCE: fortinet-fortiguard is a FIRST Archimedes-corpus surface — flagged
  in frontmatter new_source_flag for the librarian to open a provisional entry.
- Hard Rule 2: FortiGuard "tradecraft overlaps with Lemon Sandstorm" hedge and
  the "may have been positioning" destructive-intent hedge both preserved; not
  hardened.
- Hard Rule 3: CVEs by ID only; no exploit/PoC content.
- Hard Rule 7: no credentials surfaced.

## IOCs (ioc-extraction output)

```yaml
extraction_metadata:
  source_brief_id: fortiguard-lemon-sandstorm-cni-2025-05
  source_url: https://www.fortinet.com/blog/threat-research/fortiguard-incident-response-team-detects-intrusion-into-middle-east-critical-national-infrastructure
  extracted_at: 2026-07-14T16:54:00Z
  extracted_by: collector
  target_actor_id: null
  text_word_count: 780

indicators:
  - id: raw-cve-2018-13379
    type: cve
    value: CVE-2018-13379
    defanged_original: null
    role: exploitation
    campaign: "Lemon Sandstorm Middle East CNI intrusion (FortiGuard IR, 2023-2025)"
    related_malware: [HanifNet, HXLibrary, NeoExpressRAT, Havoc]
    source_brief: fortiguard-lemon-sandstorm-cni-2025-05
    context_excerpt: "Fortinet FortiOS SSL VPN path traversal used for initial access"
    attribution_in_text: Lemon Sandstorm
    notes: "vuln-tracker handoff candidate."
  - id: raw-cve-2019-11510
    type: cve
    value: CVE-2019-11510
    defanged_original: null
    role: exploitation
    campaign: "Lemon Sandstorm Middle East CNI intrusion (FortiGuard IR, 2023-2025)"
    source_brief: fortiguard-lemon-sandstorm-cni-2025-05
    context_excerpt: "Pulse Secure arbitrary file read — recurs across Pioneer Kitten campaigns (also AA24-241A)"
    attribution_in_text: Lemon Sandstorm
    notes: "Also folded in ...-001; same CVE across both surfaces — dedupe at grader/index."
  - id: raw-cve-2019-1579
    type: cve
    value: CVE-2019-1579
    defanged_original: null
    role: exploitation
    campaign: "Lemon Sandstorm Middle East CNI intrusion (FortiGuard IR, 2023-2025)"
    source_brief: fortiguard-lemon-sandstorm-cni-2025-05
    context_excerpt: "Palo Alto GlobalProtect SSL VPN RCE"
    attribution_in_text: Lemon Sandstorm
    notes: null

  - type: note
    value: "FortiGuard report ships an IOC appendix (HanifNet / HXLibrary / NeoExpressRAT / Havoc hashes + C2 IPs/domains). NOT retrieved this pass (search-summary only). Backdoor family names recorded as tooling; hashes + C2 VALUES held PENDING DIRECT RETRIEVAL of the FortiGuard report PDF. Do not fabricate."
    role: pending_retrieval

  - type: note
    value: "FIRST-PARTY SPLUNK BASELINE (Mode 4, Hard Rule 8): -90d sweep across archimedes + defenseclaw_local for full Pioneer Kitten indicator/alias/CVE/persona set = 0 hits. Index liveness control: archimedes 1725 events, defenseclaw_local 6 events over -90d (both live). Visibility-bounded null — NO corroboration, NO bonus. Frank not a Pioneer Kitten victim env."
    role: first_party_splunk_baseline

attribution_claims:
  - claimant: "FortiGuard Incident Response Team (Fortinet)"
    claim: "A ~2-year intrusion into a Middle East CNI entity shows tradecraft overlaps with the Iranian nation-state actor Lemon Sandstorm (formerly Rubidium; aka Parisite, Pioneer Kitten, UNC757); attackers may have been prepositioning for a future destructive attack"
    nation_named: Iran
    service_named: "Iranian nation-state (IRGC not specified by FortiGuard in retrieved content)"
    actor_named: Lemon Sandstorm
    confidence_language: "tradecraft overlaps with (attribution hedge); 'may have been positioning' for future destructive attack (intent hedge)"
    requires_grading: true
```
</content>
