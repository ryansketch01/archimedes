---
raw_id: raw-2026-05-21-pm-006
collected_at: 2026-05-21T15:44:00-04:00
run_id: pre-brief-20260521-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: cisa-advisories
  source_name: "CISA ICS Advisories"
  source_url: https://www.cisa.gov/cybersecurity-advisories/all.xml
  published_at: 2026-05-21T08:00:00-04:00          # 12:00 UTC published-block right at morning-brief cutoff
  source_grade: A
sweep_window:
  start: 2026-05-21T08:00:00-04:00
  end: 2026-05-21T15:30:00-04:00
match_reason:
  watchlist:
    - aerospace-defense                          # Critical Manufacturing + Energy ICS deployment overlaps DIB Tier-2/3 supply chain
  actors: []
  vulnerabilities:
    - ICSA-26-141-01                              # Hitachi Energy GMS600 — CVE-2022-4304 OpenSSL timing-side-channel
    - ICSA-26-141-02                              # ABB B&R PCs — 9 CVE-2023-4523X SinoCMS lineage batch
    - ICSA-26-141-03                              # ABB B&R Automation Studio — CVSS 9.8 LEAD, 24+ CVE deep-dependency batch
    - ICSA-26-141-04                              # ABB B&R Automation Runtime — CVE-2025-3449 + CVE-2025-3448 + CVE-2025-11498
    - ICSA-26-141-05                              # ABB Terra AC Wallbox EV charger — CVE-2025-10504 + CVE-2025-12142 + CVE-2025-12143
  keywords:
    - cisa_ics_advisory_batch_2026_05_21
    - abb_br_automation_studio_cvss_9_8
    - abb_br_automation_runtime
    - abb_br_pcs_apc4100_apc910_c80_mpc3100
    - abb_terra_ac_wallbox_ev_charger
    - hitachi_energy_gms600
    - critical_manufacturing_sector
    - energy_sector
    - defense_supply_chain_ics_adjacency
    - openssl_cve_2022_4304_timing_side_channel
    - sinocms_2023_lineage
triage_tags:
  - cisa_ics_batch
  - critical_manufacturing_energy_sector
  - defense_supply_chain_ics_layer
  - abb_br_ics_widespread_dib_deployment
  - 5_advisory_batch_2026_05_21_08_00_edt
  - just_past_morning_brief_cutoff
iocs_extracted: false
iocs_count: 0
text_word_count: 560
promoted: true
promoted_to_finding: finding-2026-05-21-0012
promoted_at: 2026-05-21T16:28:00-04:00
ttl_expires_at: 2026-08-19T15:44:00-04:00
---

# CISA ICS 5-advisory batch dated 2026-05-21 — ABB B&R Automation Studio CVSS 9.8 lead; Critical Manufacturing + Energy sector deployment

## Source extraction

**Source**: CISA Advisories Atom feed at `cisa.gov/cybersecurity-advisories/all.xml`, fetched via `mcp__rss-bridge__fetch_feed`. RSS endpoint validated as the productive path per `source-health.yaml` notes (direct page fetches on `/cybersecurity-advisories` continue to 403).

**Sweep window timing**: Published 2026-05-21T12:00:00 UTC = 08:00:00 EDT. This is RIGHT at the morning brief composition cutoff — the morning briefer would have been finalizing copy at 08:00 EDT and this batch likely did not surface in time. Effectively the first afternoon-brief surface for this batch.

**5 advisories in single 12:00 UTC publication block**:

---

## ICSA-26-141-03 — ABB B&R Automation Studio (LEAD, CVSS 9.8)

- **Sector**: Energy (Critical Infrastructure)
- **Country of deployment**: Worldwide
- **Vendor HQ**: Switzerland
- **Affected versions**: B&R Automation Studio <6.5 (and 6.5 — some configurations)
- **CVE count**: 24+ CVEs spanning 2015-2024 (CVE-2025-6965, CVE-2025-3277, CVE-2023-7104, CVE-2022-35737, CVE-2020-15358, CVE-2020-13632, CVE-2020-13631, CVE-2020-13630, CVE-2020-13435, CVE-2020-13434, CVE-2020-11656, CVE-2020-11655, CVE-2019-19646, CVE-2019-19645, CVE-2019-8457, CVE-2018-20506, CVE-2018-20505, CVE-2018-20346, CVE-2018-8740, CVE-2017-10989, CVE-2016-6153, CVE-2015-6607, CVE-2015-5895, CVE-2015-3717, CVE-2015-3416)
- **Pattern**: Deep-dependency third-party-component update — CISA characterizes this as "An update is available that replaces an outdated third-party component" with vendor acknowledgment that "no successful exploitation was observed during testing" but "the identified vulnerabilities could present potential attack vectors that might enable unauthorized access, data exposure, or remote code execution"
- **CVSS**: 9.8 (highest in batch)

**Why this matters**: B&R Automation Studio is engineering software for the B&R control systems used in manufacturing — packaging, printing, plastics, food/beverage, semiconductor — but also defense-adjacent manufacturing (CNC, robotics integrators, contract manufacturers serving DIB Tier-2/3). The 24-CVE-deep batch is a single-product accumulator of unpatched dependency CVEs that engineering-workstation defenders must triage all at once.

---

## ICSA-26-141-04 — ABB B&R Automation Runtime

- **Sector**: Energy
- **Affected versions**: Automation Runtime <6.4 (and 6.4)
- **CVEs**: CVE-2025-3449 (predictable numbers/identifiers), CVE-2025-3448 (XSS), CVE-2025-11498 (CSV formula injection)
- **CVSS**: 6.1 (lead)
- **Vendor framing**: B&R-internal security analysis discovery; "An attacker who successfully exploited these vulnerabilities could take over a remote session or execute code in the context of the user's browser session."

---

## ICSA-26-141-02 — ABB B&R PCs (APC4100 / APC910 / C80 / MPC3100)

- **Sector**: Energy (presumed — per ABB B&R product family)
- **CVE batch**: 9-CVE 2023-4523X cluster (CVE-2023-45229, -45230, -45231, -45232, -45233, -45234, -45235, -45236, -45237)
- **Pattern**: 2023-vintage SinoCMS lineage — likely embedded-component refresh on industrial-PC products
- **CVSS**: Not surfaced in batch summary (RSS body did not include score)

---

## ICSA-26-141-05 — ABB Terra AC Wallbox (EV charger)

- **Sector**: Energy
- **Affected versions**: Terra AC wallbox (JP) ≤1.8.33, 1.8.36
- **CVEs**: CVE-2025-10504, CVE-2025-12142, CVE-2025-12143
- **CVSS**: 6.1 (lead)
- **Vulnerability class**: Heap-based buffer overflow, classic buffer overflow, stack-based buffer overflow
- **Impact** (verbatim, under 15 words): An attacker exploiting could pollute heap memory, potentially taking remote control and writing flash firmware
- **A&D relevance**: Indirect — EV chargers at A&D corporate-campus parking decks and DoD installation parking. Adjacent attack surface, not core attack surface.

---

## ICSA-26-141-01 — Hitachi Energy GMS600

- **Sector**: Critical Manufacturing
- **Country deployment**: Worldwide
- **HQ**: Switzerland (Hitachi Energy global HQ)
- **Affected versions**: GMS600 vers:GMS600 ≥1.3.0|≤1.3.1
- **CVE**: CVE-2022-4304 (OpenSSL timing-side-channel — Bleichenbacher-class oracle on RSA decryption)
- **CVSS**: 5.9
- **Vulnerability class**: Observable discrepancy (timing oracle)
- **Impact**: Attacker recovers pre-master secret via repeated trial-message timing measurements; decrypts captured TLS traffic

---

## Batch significance

ABB B&R is a major vendor of industrial automation across DIB Tier-2/3 contract manufacturers. The 24-CVE Automation Studio batch + 3-CVE Runtime batch + 9-CVE PCs batch together represent ~36 CVE entries in a single ABB B&R vendor batch published in one CISA block. **Defense supply-chain ICS-layer adjacency**: contract manufacturers using B&R control systems for precision machining and small-batch assembly serving DIB Tier-1/2 customers should patch this cycle.

Hitachi Energy GMS600 is grid-substation monitoring software — Energy critical-infrastructure adjacent, modestly relevant to A&D-prime-utility-supplier risk modeling.

No active exploitation reported by CISA on any of the 5 advisories. None on KEV.

## Extraction notes

- Language: en
- Article type: structured ICS advisory batch (CISA atom feed)
- Raw IOC extraction invoked: no — vendor patch references not IOCs
- 15-word quote limit observed
- Source grade A (CISA authoritative)
- Cross-finding correlation: Rapid7 Q1 2026 quarterly (PM-005) named "industrial systems" as Iranian state-aligned target tier — these ICS surfaces are plausible adversary interest points, though no roster-actor attribution from this batch
