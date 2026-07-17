---
dossier_id: VT-047
cluster_name: Siemens-RUGGEDCOM-ROX-II-2025-Cluster
title: "Siemens RUGGEDCOM ROX II OT/industrial switches — chained three-CVE zero-day trilogy (one Critical) in pre-V2.17.1 firmware"
cluster_keying_principle: >
  Single cluster dossier keyed on the fix-version V2.17.1 boundary, NOT
  three separate per-CVE entries. The operational unit-of-tracking is
  "estate running RUGGEDCOM ROX II firmware before V2.17.1" — which is how
  an operator would scope remediation. All three CVEs share disclosure date
  (Siemens SSAs / NVD publication 2026-05-12), share fix release (V2.17.1),
  and Unit 42 documents them as a single exploitation chain. Matches the
  VT-005 (OpenC3 COSMOS) cluster-keying precedent the source finding cites.

anchor_cve: CVE-2025-40949           # Critical 9.1 persistence stage — chain anchor

cves:
  - cve_id: CVE-2025-40949
    severity: critical
    cvss_v3_base: 9.1
    cvss_v3_vector: "CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H"
    cvss_v4_base: 8.9
    cvss_v4_severity: high
    cvss_v4_vector: "CVSS:4.0/AV:N/AC:L/AT:P/PR:H/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H"
    cwe: [CWE-78]
    component: "Scheduler Web UI / task-scheduling backend (root cron table)"
    class: "OS command injection -> persistent root code execution"
    chain_stage: 3
    ssa_id: SSA-081142
  - cve_id: CVE-2025-40947
    severity: high
    cvss_v3_base: 7.5
    cvss_v3_vector: "CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H"
    cvss_v4_base: 7.7
    cvss_v4_severity: high
    cvss_v4_vector: "CVSS:4.0/AV:N/AC:H/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N"
    cwe: [CWE-78]
    component: "Feature-key installation process"
    class: "OS command injection -> privilege escalation to root"
    chain_stage: 2
    ssa_id: SSA-078743
  - cve_id: CVE-2025-40948
    severity: medium
    cvss_v3_base: 6.8
    cvss_v3_vector: "CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N"
    cvss_v4_base: 6.1
    cvss_v4_severity: medium
    cvss_v4_vector: "CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:N/VI:N/VA:N/SC:H/SI:N/SA:N"
    cwe: [CWE-88]
    component: "Web server JSON-RPC interface"
    class: "Improper input validation / argument injection -> arbitrary file read as root"
    chain_stage: 1
    ssa_id: SSA-973901

disclosed_at: 2026-05-12             # Siemens SSAs / NVD publication
nvd_published_at: 2026-05-12
nvd_last_modified_at: 2026-06-29
nvd_status: Analyzed
unit42_deepdive_published_at: 2026-07-17   # secondary research write-up (source finding basis)

affected_products:
  - vendor: Siemens
    product: RUGGEDCOM ROX II
    description: "Hardened OT / industrial ethernet switches and routers (RUGGEDCOM ROX II firmware line) used in industrial, utility, rail, and substation networks"
    models_affected:
      - RUGGEDCOM ROX MX5000
      - RUGGEDCOM ROX MX5000RE
      - RUGGEDCOM ROX RX1400
      - RUGGEDCOM ROX RX1500
      - RUGGEDCOM ROX RX1501
      - RUGGEDCOM ROX RX1510
      - RUGGEDCOM ROX RX1511
      - RUGGEDCOM ROX RX1512
      - RUGGEDCOM ROX RX1524
      - RUGGEDCOM ROX RX1536
      - RUGGEDCOM ROX RX5000
    versions_affected: "All versions before V2.17.1"
    fixed_in: "V2.17.1"

kev_status:
  any_cve_in_kev: false
  cves_in_kev: []
  last_checked: 2026-07-17
  last_checked_method: >
    Indirect via NVD (all three records Analyzed, last modified 2026-06-29);
    NVD reference set carries only the Siemens SSA vendor-advisory URLs — no
    CISA KEV / ADP catalog reference is present on any of the three records,
    consistent with not-KEV. CISA KEV feed not separately retrieved this pass.
  watch_signal_active: true
  watch_signal_note: >
    Track CISA KEV and CISA ICS advisories (ICSA-*) for these CVEs. KEV or
    ITW would lift the single-source-veto exploitation leg carried on the
    source finding and re-rate A&D relevance upward.

exploitation_status: not_observed
exploitation_status_qualifier: >
  No in-the-wild exploitation reported by any source. Unit 42 (the secondary
  research write-up, 2026-07-17) explicitly states no observed exploitation,
  released no public PoC, and named no threat actor. None of the three CVEs
  is on CISA KEV. Splunk first-party has no RUGGEDCOM ROX II OT-switch
  telemetry in scope, so silent Splunk is NOT disconfirming per Hard Rule 8.

public_exploit_available: false
public_exploit_note: >
  No public PoC released. Unit 42's write-up describes a reverse-shell chain
  at capability level; per Hard Rule 3 no exploit code, payload, or attack-
  step chain is reproduced in this dossier. The three CVE IDs plus the two
  host-side behavioral detection observables recorded below are the only
  operationally-tracked artifacts.

patch_status: patched
patch_release_date: 2026-05-12
mitigation_available: true

related_actors: []
related_actors_note: >
  No actor named by any source (Unit 42, Siemens SSAs, NVD). No exploitation
  reported. Per Hard Rule 2, Archimedes does not originate attribution and
  keeps this empty, not omitted.

related_findings:
  - finding-2026-07-17-0001

related_briefs: []

ad_relevance: medium
ad_relevance_tag: structural_unverified_exposure
ad_relevance_rationale: >
  STRUCTURAL, not victim-specific. RUGGEDCOM ROX II are hardened OT/industrial
  ethernet switches structurally pervasive in industrial network estates. The
  finding rates relevance medium on the OT/ICS-in-A&D tracking rationale the
  corpus applies to VT-005 (OpenC3 COSMOS) and VT-010 (Yamcs). Per the
  analyst KAC (finding-2026-07-17-0001, assumption A3, low confidence): there
  is NO evidence the ad-prime-v1 target profile runs RUGGEDCOM ROX II
  specifically — RUGGEDCOM's core market is utility / rail / substation, and
  an A&D prime's OT estate may run different vendors (Cisco IE, Hirschmann,
  etc.). Exposure is inference from OT-appliance ubiquity, not observation.
  Hold at medium, labeled structural / unverified-exposure. The VT-005/VT-010
  analogue is a tracking rationale (analyst A4), NOT evidence of A&D exposure —
  COSMOS/Yamcs are A&D mission-stack software; ROX II is general industrial
  networking gear. Re-rate upward only on ITW, a public weaponized PoC, a
  CISA ICS advisory, or actor attribution.

digraph: A2
wep_ceiling: likely
single_source_veto_applied: true
single_source_veto_basis: >
  Inherited from source finding-2026-07-17-0001. Unit 42 is the sole directly-
  retrieved source in the finding; the Siemens SSA advisories were referenced
  but not retrieved by the grader. This dossier ADDS independent direct
  retrieval of the three NVD records (all Analyzed, 2026-06-29), which
  corroborates the CVE facts, CVSS, CWE, affected-model matrix, and fix
  boundary — but NVD is downstream of the Siemens CNA process and shares that
  evidence basis, so the veto is not fully lifted. WEP held at "likely."

tracked_since: 2026-07-17
last_updated: 2026-07-17
tracking_version: 1
tlp: CLEAR
---

# Siemens RUGGEDCOM ROX II 2025 Cluster — Chained Three-CVE Zero-Day Trilogy (Pre-V2.17.1)

Siemens RUGGEDCOM ROX II — hardened OT / industrial ethernet switches and routers — carries three CVEs disclosed 2026-05-12 (Siemens SSA-973901 / -078743 / -081142) that Palo Alto Networks Unit 42 documents as a single exploitation chain: arbitrary file read as root, escalation to root via command injection, and persistent root code execution. All three are patched in firmware V2.17.1. No in-the-wild exploitation is reported, no public PoC has been released, and no threat actor is attributed. The operational unit-of-tracking is "estate running ROX II firmware before V2.17.1" — a single firmware update closes the chain.

## Summary

The three CVEs were assigned and disclosed by Siemens on 2026-05-12 with NVD records published the same day (all three now NVD-status **Analyzed**, last modified 2026-06-29). On 2026-07-17 Unit 42 published a technical write-up characterizing them as a chained trilogy that takes an attacker from limited access to persistent root on the switch. NVD confirms Unit 42's v3.1 CVSS figures exactly and adds CWE classifications, CVSS v4.0 vectors, and the precise affected-hardware matrix.

This cluster is tracked on the OT/ICS-in-A&D structural rationale the corpus applies to VT-005 (OpenC3 COSMOS) and VT-010 (Yamcs). Relevance is **medium and explicitly structural / unverified-exposure**: there is no evidence the target profile runs RUGGEDCOM ROX II specifically. RUGGEDCOM's core market is utility / rail / substation, not aerospace & defense, and an A&D prime's OT estate may run different switch vendors. The A&D nexus is inference from OT-appliance ubiquity, not observation (analyst KAC assumption A3, low confidence). The chain is patched with no ITW and no named A&D victim, so this is an awareness / monitoring item, not an action item.

Graded conservatively at **A2 / "likely"** with the single-source veto carried from the source finding. Unit 42 is the sole directly-retrieved narrative source; this dossier adds independent direct retrieval of the three NVD records, which corroborate the CVE facts but sit downstream of the Siemens CNA process (shared evidence basis), so the veto is not fully lifted.

## CVE roster

| CVE | Stage | Severity | CVSS v3.1 | CVSS v4.0 | CWE | Component | Siemens SSA |
|---|---|---|---|---|---|---|---|
| CVE-2025-40949 | 3 (persistence) | Critical | 9.1 | 8.9 (High) | CWE-78 | Scheduler Web UI / root cron table | SSA-081142 |
| CVE-2025-40947 | 2 (privesc) | High | 7.5 | 7.7 (High) | CWE-78 | Feature-key installation process | SSA-078743 |
| CVE-2025-40948 | 1 (file read) | Medium | 6.8 | 6.1 (Medium) | CWE-88 | Web server JSON-RPC interface | SSA-973901 |

All three affect the same 11 RUGGEDCOM ROX hardware models and are fixed in the same firmware release (V2.17.1).

## Technical detail

Vulnerability-class descriptions below are conceptual. Per Hard Rule 3, no exploit code, payload structure, attack-command chain, or Unit 42 reverse-shell detail is reproduced. NVD is the authoritative record for CVE facts; the Siemens SSAs are the vendor primary.

### CVE-2025-40949 — Persistent root code execution (Critical, CVSS v3.1 9.1)

- **Component / class:** Scheduler Web UI functionality; OS command injection (CWE-78). Per NVD, input-sanitization failure in the Scheduler Web UI lets an authenticated remote attacker inject commands into the task-scheduling backend, achieving arbitrary command execution with root privileges. Unit 42 frames this as persistence via injection into the system's root cron table — the chain anchor.
- **Vector (v3.1):** `AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H` — network-reachable, low complexity, **high privilege required**, no user interaction, scope-changed, full CIA impact.
- **v4.0:** 8.9 (High), `AV:N/AC:L/AT:P/PR:H/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H`.
- **Fixed in:** V2.17.1 (SSA-081142).

### CVE-2025-40947 — Privilege escalation via command injection (High, CVSS v3.1 7.5)

- **Component / class:** Feature-key installation process; OS command injection (CWE-78). Affected devices do not properly sanitize user-supplied input during feature-key installation, enabling an authenticated remote attacker to execute arbitrary commands with root privileges. Unit 42 places this as the escalation stage.
- **Vector (v3.1):** `AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H` — note **high attack complexity (AC:H)** and only **low privilege required (PR:L)** — the lowest privilege bar of the three per NVD's independent scoring.
- **v4.0:** 7.7 (High), `AV:N/AC:H/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`.
- **Fixed in:** V2.17.1 (SSA-078743).

### CVE-2025-40948 — Arbitrary file read as root (Medium, CVSS v3.1 6.8)

- **Component / class:** Web server JSON-RPC interface; improper input validation / argument injection (CWE-88). Per NVD, the JSON-RPC interface does not properly validate input, allowing an authenticated remote attacker to read arbitrary files from the underlying OS filesystem with root privileges (e.g., password hashes, private keys). Unit 42 frames this as the chain's first stage to obtain credentials/keys.
- **Vector (v3.1):** `AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N` — **high privilege required**, confidentiality-only, scope-changed.
- **v4.0:** 6.1 (Medium), `AV:N/AC:L/AT:N/PR:H/UI:N/VC:N/VI:N/VA:N/SC:H/SI:N/SA:N`.
- **Fixed in:** V2.17.1 (SSA-973901).

**NVD-vs-Unit-42 mechanism note (data note, not adjudicated):** The source finding described CVE-2025-40948 as arbitrary file disclosure via a "root-privileged `xz` misconfiguration." NVD's authoritative description instead attributes it to improper input validation in the **web server's JSON-RPC interface** (CWE-88, argument injection). These may describe the same underlying primitive at different layers (a JSON-RPC-reachable argument-injection into a root-privileged utility such as `xz`), but Archimedes does not adjudicate. NVD is recorded as authoritative for the CVE record; Unit 42's narrative is recorded as the secondary research characterization. Similarly, all three CVEs are **authenticated** per NVD (PR:H / PR:L), which the finding's chain narrative is consistent with (the chain acquires and escalates access rather than starting unauthenticated).

## Affected products and versions

- **Vendor:** Siemens
- **Product line:** RUGGEDCOM ROX II firmware
- **Models (per NVD CPE, all three CVEs):** ROX MX5000, MX5000RE, RX1400, RX1500, RX1501, RX1510, RX1511, RX1512, RX1524, RX1536, RX5000
- **Affected versions:** all versions before V2.17.1
- **Fixed in:** V2.17.1

Operational scope an operator would address: any ROX II instance on firmware below V2.17.1 carries the full chain. The single firmware update to V2.17.1 closes all three.

## Disclosure and exploitation timeline

| Date | Event | Source |
|---|---|---|
| 2026-05-12 | Siemens SSAs published (SSA-973901 / -078743 / -081142); NVD records published; fix V2.17.1 released | [Siemens ProductCERT](https://cert-portal.siemens.com/productcert/html/ssa-081142.html) |
| 2026-06-29 | NVD records last modified (Analyzed) | [NVD CVE-2025-40949](https://nvd.nist.gov/vuln/detail/CVE-2025-40949) |
| 2026-07-17 | Unit 42 technical deep-dive published | [Unit 42](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/) |
| 2026-07-17 | Surfaced via Archimedes morning collection; vuln-tracker dossier created | finding-2026-07-17-0001 |

No in-the-wild exploitation events have been reported.

## Attribution to tracked actors

No Archimedes-tracked actor has been publicly attributed to exploitation of any CVE in this cluster as of 2026-07-17. No source (Unit 42, Siemens SSAs, NVD) names any actor, and no exploitation is reported. Per Hard Rule 2, Archimedes does not originate attribution; if a future cited source attributes exploitation to a tracked actor, this dossier will be updated with the source-grade and citation.

## Mitigations and patches

**Patch:** Update RUGGEDCOM ROX II firmware to **V2.17.1**. The single release closes all three CVEs.

**OT patch-tempo caveat:** OT/ICS network gear is notoriously slow to patch in the field; vendor-fixed is not fleet-patched (analyst KAC assumption A5). Substation / rail / industrial switches commonly gate firmware updates behind maintenance windows and change-control. Vendor-published compensating guidance (per Siemens SSAs, paraphrased): restrict management-plane / Web UI and JSON-RPC reachability to trusted administrative networks; follow Siemens operational-security guidelines for RUGGEDCOM devices. Because all three CVEs are authenticated and network-reachable, limiting who can reach the device management surface materially reduces exposure pre-patch.

## Defense recommendations

For an operator with potential RUGGEDCOM ROX II exposure:

1. **Inventory.** Determine whether RUGGEDCOM ROX II switches/routers are deployed in any OT, facility SCADA, test-range, or manufacturing network, and identify firmware versions. Only an inventory query confirms operator-specific exposure — the A&D nexus in this dossier is structural, not observed.
2. **Patch to V2.17.1.** Schedule the firmware update through OT change-control. All three CVEs close with the single update.
3. **Restrict the management surface (pre-patch compensating control).** All three are authenticated + network-reachable; confine ROX II Web UI / JSON-RPC / scheduler management access to a dedicated administrative VLAN or jump-host path. Verify no management-plane reachability from general enterprise or untrusted OT segments.
4. **Account hygiene.** The chain begins from an authenticated position; review ROX II local accounts, rotate credentials, and remove shared/default logins.
5. **Detection.** Log ROX II configuration and task-scheduler changes; alert on unexpected scheduled tasks or config-daemon behavior (see below).

## Detection opportunities

Host-side behavioral observables (from the source finding; no atomic network IOCs exist):

- Unexpected scripts or commands appearing in switch configuration or task-scheduler (cron) files.
- Execution of `xz` with `-f` / `-c` / `-d` parameters by the privileged config daemon.

These are conceptual hunt sketches, not production detections, and assume ROX II management-plane logging is centralized. MITRE ATT&CK class alignment (paraphrased, not vendor-attested): T1190 Exploit Public-Facing Application (if the management surface is reachable beyond a trusted network); T1053 Scheduled Task/Job (cron-table persistence, CVE-2025-40949); T1078 Valid Accounts (all three require authentication).

## Data gaps

- **Siemens SSA advisories not directly retrieved this pass.** NVD (Analyzed) corroborates the CVE facts, CVSS, CWE, affected-model matrix, and V2.17.1 fix boundary, and carries the SSA URLs as references. Direct SSA retrieval (SSA-973901 / -078743 / -081142) is deferred enrichment to confirm any vendor-specific mitigation detail and exact affected-build enumeration beyond "< V2.17.1."
- **CVE-2025-40948 mechanism divergence** between the finding ("xz misconfig") and NVD ("JSON-RPC interface", CWE-88) is recorded, not adjudicated.
- **A&D exposure surface is unverified** — no evidence the target profile runs RUGGEDCOM ROX II (analyst A3). Relevance held medium / structural.
- **First-party telemetry not in scope** — Splunk carries no RUGGEDCOM ROX II OT-switch instrumentation; silent Splunk is not disconfirming (Hard Rule 8).

## Watch signals

1. **CISA KEV addition or CISA ICS advisory (ICSA-*)** for any of the three CVEs — lifts the single-source-veto exploitation leg via CISA's independent determination; re-rate A&D relevance and consider brief inclusion.
2. **In-the-wild exploitation observation** (vendor IR, government bulletin, security-firm telemetry) — converts from disclosure-tracking to exploitation-tracking.
3. **Public weaponized PoC** published outside Unit 42's write-up — broadens the attacker population.
4. **Actor attribution** by any A/B-grade source — populate related_actors (Hard Rule 2: inherited only).
5. **A&D-specific deployment evidence** (an A&D operator statement, DoD SBOM, or third-party survey naming ROX II in an A&D estate) — would resolve the unverified-exposure assumption and could re-rate relevance.

## References

Primary sources:

- [NVD CVE-2025-40949](https://nvd.nist.gov/vuln/detail/CVE-2025-40949) — persistent root code execution (Scheduler Web UI, CWE-78)
- [NVD CVE-2025-40947](https://nvd.nist.gov/vuln/detail/CVE-2025-40947) — privesc via command injection (feature-key install, CWE-78)
- [NVD CVE-2025-40948](https://nvd.nist.gov/vuln/detail/CVE-2025-40948) — arbitrary file read as root (JSON-RPC, CWE-88)
- [Siemens SSA-081142](https://cert-portal.siemens.com/productcert/html/ssa-081142.html) — vendor advisory CVE-2025-40949 (referenced; not directly retrieved this pass)
- [Siemens SSA-078743](https://cert-portal.siemens.com/productcert/html/ssa-078743.html) — vendor advisory CVE-2025-40947 (referenced; not directly retrieved this pass)
- [Siemens SSA-973901](https://cert-portal.siemens.com/productcert/html/ssa-973901.html) — vendor advisory CVE-2025-40948 (referenced; not directly retrieved this pass)

Secondary research (B-grade context, single directly-retrieved narrative source in the finding):

- [Unit 42 — Siemens ROX II zero-day vulnerabilities](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/) — chained-trilogy technical write-up (2026-07-17)

Internal:

- [finding-2026-07-17-0001](../../findings/finding-2026-07-17-0001-unit42-siemens-ruggedcom-rox-ii-ot-switch-zero-day-trilogy-cve-2025-40947-40948-40949-a2-likely-monitoring.md) — source finding (A2 / likely; single-source veto; KAC applied, ACH not applicable)

*Created: 2026-07-17 | Author: Archimedes (vuln-tracker) | Admiralty Grade: A2 — NVD primary (Analyzed) + Siemens SSA vendor primary; single-source veto still applies | TLP: CLEAR*
