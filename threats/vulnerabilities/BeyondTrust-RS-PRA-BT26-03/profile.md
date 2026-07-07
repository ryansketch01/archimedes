---
dossier_id: VT-016
cve_cluster: [CVE-2026-40138, CVE-2026-40139, CVE-2026-40140, CVE-2026-40141]
advisory_id: BT26-03
title: "BeyondTrust Remote Support / Privileged Remote Access — four flaws (two critical pre-auth authentication bypasses) in advisory BT26-03"
disclosed_at: 2026-07-06          # NVD record publication; vendor advisory relayed 2026-07-07
cvss_status: nvd_enriched         # NVD CVSS v4.0 present for all four (published 2026-07-06); NOT pending
cvss_scoring_version: "4.0"
cvss_max:
  base_score: 9.2
  cve: CVE-2026-40138             # tied with CVE-2026-40139 at 9.2
  vector: "CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N"
cwe_set: [CWE-287, CWE-400, CWE-943]
affected_products:
  - vendor: BeyondTrust
    product: Remote Support (RS)
    versions_affected: ["< 25.3.3 (25.3.x branch)", "< 26.2.1 (26.2.x branch)"]
  - vendor: BeyondTrust
    product: Privileged Remote Access (PRA)
    versions_affected: ["< 25.3.3 (25.3.x branch)", "< 26.2.1 (26.2.x branch)"]
fixed_versions: ["RS/PRA 25.3.3", "RS/PRA 26.2.1"]
cloud_patched: 2026-04-21          # all RS/PRA cloud customers patched per vendor
onprem_action: "Self-hosted customers must apply the April security rollup for their branch or upgrade to 25.3.3 / 26.2.1"
kev_status:
  in_kev: false
  kev_checked: 2026-07-07
  kev_catalog_version: 2026.07.01
exploitation_status: disclosed     # no PoC, no in-the-wild exploitation reported
exploitation_first_observed: null
patch_available: true
patch_released: 2026-04-21          # cloud; on-prem fixed versions available concurrently
mitigation_available: true
internet_exposure: "~2,000 internet-exposed RS/PRA instances (Shadowserver); unpatched proportion unknown"
related_actors: []                  # Hard Rule 2 — NONE. Silk Typhoon is HISTORICAL context re: PRIOR different BeyondTrust CVEs, not attributed to these.
related_findings: [finding-2026-07-07-0001]
ad_relevance: high
last_updated: 2026-07-07
tracking_version: 1
tlp: CLEAR
---

# BeyondTrust RS / PRA — advisory BT26-03 (CVE-2026-40138 · CVE-2026-40139 · CVE-2026-40140 · CVE-2026-40141)

BeyondTrust disclosed four vulnerabilities in its Remote Support (RS) and Privileged Remote Access (PRA) appliances — two critical pre-authentication authentication-bypass flaws that let a network-positioned attacker reach the appliance, including elevated-privilege accounts, plus a high-severity denial-of-service and a high-severity authorization-scope bypass.

## Summary

Advisory BT26-03 covers four CVEs in BeyondTrust's RS and PRA product line. The two critical flaws (CVE-2026-40138, CVE-2026-40139, both CVSS v4.0 9.2) are pre-authentication authentication-bypass conditions in the authentication subsystem: improper validation/processing of authentication data or requests can let an unauthenticated, network-positioned attacker bypass access controls and gain unauthorized access to the appliance, including accounts with elevated privileges. The two high-severity flaws are a pre-authentication DoS (CVE-2026-40140, CVSS 8.7, CWE-400) affecting appliance availability, and an authenticated low-privilege authorization-scope bypass (CVE-2026-40141, CVSS 8.5, CWE-943) allowing access to unintended resources or data.

All four are fixed. BeyondTrust patched all RS/PRA cloud customers as of 2026-04-21; self-hosted customers must apply the April security rollup for their branch or upgrade to 25.3.3 (25.3.x branch) or 26.2.1 (26.2.x branch). No active exploitation of these CVEs is reported, and no threat actor is attributed to them by any source. Notably, exploitation of the critical CVE-2026-40138 additionally requires a specific authentication configuration to be enabled — a precondition that narrows universal applicability.

A&D contractors should care because RS and PRA are privileged-remote-access / identity-adjacent infrastructure commonly deployed across the defense industrial base to broker vendor and administrator access into sensitive estates. Compromise of that broker sits at a high-value chokepoint. The A&D relevance here is structural (product-class deployment in the DIB), not anchored to any named A&D-watchlist victim in this reporting. The Shadowserver Foundation tracked roughly 2,000 internet-exposed RS/PRA instances as blast-radius context; the unpatched proportion is unknown.

## Technical detail

Authoritative technical facts below are from the NVD records (published 2026-07-06), which are downstream of BeyondTrust's CNA advisory BT26-03. No exploit detail, proof-of-concept, or attack-step chain is recorded here (Hard Rule 3); only vulnerability class, attack surface, and preconditions relevant to defense.

| CVE | Severity (CVSS v4.0) | CWE | Class | Vector highlights |
|---|---|---|---|---|
| CVE-2026-40138 | Critical 9.2 | CWE-287 (Improper Authentication) | Pre-auth authentication bypass in RS & PRA; unauthorized appliance access incl. elevated-privilege accounts | AV:N / AC:H / AT:P / PR:N / UI:N — network vector, high attack complexity, attack requirements present |
| CVE-2026-40139 | Critical 9.2 | CWE-287 (Improper Authentication) | Pre-auth authentication bypass via improper processing of authentication requests; unauthenticated remote access incl. elevated-privilege accounts | AV:N / AC:L / AT:P / PR:N / UI:N |
| CVE-2026-40140 | High 8.7 | CWE-400 (Uncontrolled Resource Consumption) | Pre-auth denial-of-service in the network communication subsystem; insufficient validation of client-supplied input affects appliance availability | AV:N / AC:L / AT:N / PR:N / UI:N — availability impact only |
| CVE-2026-40141 | High 8.5 | CWE-943 (Improper Neutralization in Data/Query Logic) | Authenticated low-privilege authorization-scope bypass; access to unintended resources/data beyond authorization scope | AV:N / AC:L / AT:N / PR:L / UI:N — requires low privilege (not pre-auth) |

Key defensive distinctions:
- **Two pre-auth criticals** (40138, 40139): network-reachable, no authentication required. These drive the priority. CVE-2026-40138 carries a documented precondition — a specific authentication configuration must be enabled — reflected in its AC:H / AT:P vector; CVE-2026-40139 is AC:L / AT:P.
- **CVE-2026-40140** is availability-only (DoS); no confidentiality/integrity impact.
- **CVE-2026-40141** is NOT pre-auth — it requires an authenticated low-privilege position (PR:L), then permits horizontal access beyond authorization scope.

## Affected products and versions

- **BeyondTrust Remote Support (RS):** versions before 25.3.3 (25.3.x branch) and before 26.2.1 (26.2.x branch).
- **BeyondTrust Privileged Remote Access (PRA):** versions before 25.3.3 (25.3.x branch) and before 26.2.1 (26.2.x branch).

NVD lists both RS and PRA as affected across all four CVEs. (The source finding described CVE-2026-40139 as RS-only; NVD — authoritative — scopes it to both RS and PRA. NVD scope recorded here.)

## Exploitation timeline

| Date | Event | Source |
|---|---|---|
| 2026-04-21 | All RS/PRA cloud customers patched (silent, pre-disclosure) | [BeyondTrust BT26-03](https://www.beyondtrust.com/trust-center/security-advisories/bt26-03) |
| 2026-07-06 | NVD records published for all four CVEs with CVSS v4.0 scoring | [NVD CVE-2026-40138](https://nvd.nist.gov/vuln/detail/CVE-2026-40138) |
| 2026-07-07 | Advisory publicized; ~2,000 internet-exposed instances noted | [BleepingComputer](https://www.bleepingcomputer.com/news/security/beyondtrust-warns-of-critical-flaws-in-remote-access-software/) |

No active-exploitation event recorded. BeyondTrust makes no mention of in-the-wild exploitation.

## Attribution to tracked actors

No Archimedes-tracked actor has been publicly attributed to exploitation of CVE-2026-40138, -40139, -40140, or -40141 as of 2026-07-07. No source attributes any actor to these CVEs, and none is originated here (Hard Rule 2).

**Product-line context only (NOT linked to these CVEs):** BeyondTrust RS/PRA has a prior history of exploited zero-days — reporting has associated Chinese state-linked "Silk Typhoon" with the 2024–2025 exploitation of *different, earlier* BeyondTrust flaws (e.g., CVE-2024-12356, CVE-2024-12686) in the US Treasury / OFAC incident. That is historical product-line context to explain why this attack surface warrants tracking. It is NOT an attribution of the BT26-03 CVEs. Silk Typhoon is not on the Archimedes roster and is a distinct MSS/HAFNIUM-lineage cluster (do not cross-walk to roster Salt/Volt Typhoon).

## Mitigations and patches

- **Cloud (RS/PRA):** patched by BeyondTrust as of 2026-04-21. No customer action required.
- **Self-hosted / on-prem:** apply the April security rollup patch for the affected branch if not on automatic updates, or upgrade to **RS/PRA 25.3.3** (25.3.x branch) or **RS/PRA 26.2.1** (26.2.x branch).
- **Precondition awareness:** CVE-2026-40138 exploitation requires a specific authentication configuration to be enabled; estates should not treat that as a substitute for patching but may use it to triage exposure.
- **Compensating controls (patching delayed):** restrict RS/PRA appliance management/network reachability to trusted segments; confirm the appliance is not needlessly internet-exposed (Shadowserver counted ~2,000 exposed instances); review authentication and session logs for anomalies prior to patching.

## Defense recommendations

1. **Inventory RS/PRA estate and version.** Identify any self-hosted RS/PRA appliance below 25.3.3 (25.3.x) or 26.2.1 (26.2.x). Cloud tenants are already covered.
2. **Patch/upgrade on-prem to a fixed branch** as the primary action — the two pre-auth criticals are network-reachable without authentication.
3. **Reduce internet exposure.** Confirm RS/PRA appliances are not unnecessarily reachable from untrusted networks; ~2,000 instances are internet-exposed per Shadowserver.
4. **Audit authentication configuration** relevant to CVE-2026-40138's precondition, and least-privilege scoping relevant to the authenticated CVE-2026-40141 authorization-bypass.
5. **Review logs** for anomalous appliance authentication, session, or authorization events in the window prior to patching.
6. **Track for KEV listing / exploitation.** No ITW today; a KEV addition or first confirmed exploitation is a state-change tripwire that would raise priority and (given the pre-auth criticals) FLASH consideration.

## Detection opportunities

Defensive observables only — no exploit signatures are reproduced here (Hard Rule 3).

- **Appliance auth logs:** unexpected successful authentications to RS/PRA without a corresponding legitimate session origin; access to elevated-privilege accounts from unrecognized network positions.
- **Availability monitoring:** abnormal RS/PRA appliance restarts, resource exhaustion, or service unavailability consistent with the DoS class (CVE-2026-40140).
- **Authorization anomalies:** authenticated low-privilege accounts accessing resources/data outside expected scope (CVE-2026-40141).
- **Network exposure baseline:** external-attack-surface monitoring for RS/PRA management interfaces reachable from the internet.
- First-party Splunk sweep (`index=defenseclaw_local OR index=archimedes`) returned 0 events for these CVEs / BeyondTrust product strings at finding time; silent Splunk is visibility-bounded, not disconfirming (Hard Rule 8).

## References

- [BeyondTrust security advisory BT26-03](https://www.beyondtrust.com/trust-center/security-advisories/bt26-03) — vendor primary (CNA)
- [NVD — CVE-2026-40138](https://nvd.nist.gov/vuln/detail/CVE-2026-40138) · [CVE-2026-40139](https://nvd.nist.gov/vuln/detail/CVE-2026-40139) · [CVE-2026-40140](https://nvd.nist.gov/vuln/detail/CVE-2026-40140) · [CVE-2026-40141](https://nvd.nist.gov/vuln/detail/CVE-2026-40141)
- [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — checked 2026-07-07 (catalog 2026.07.01); none of the four listed
- [BleepingComputer — BeyondTrust warns of critical flaws in remote access software](https://www.bleepingcomputer.com/news/security/beyondtrust-warns-of-critical-flaws-in-remote-access-software/) — B-grade relay
- Source finding: `threats/findings/finding-2026-07-07-0001-...md`
