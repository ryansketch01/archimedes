# ScadaBR RCE Cluster — CVE-2026-8602–8605 (CISA-Disclosed ICS/SCADA Unauth RCE)

## Identity

| Field | Details |
|---|---|
| **CVEs** | CVE-2026-8602 · CVE-2026-8603 · CVE-2026-8604 · CVE-2026-8605 |
| **Vendor Advisory** | [CISA ICSA-26-139-03](https://www.cisa.gov/news-events/ics-advisories/icsa-26-139-03) — disclosed ~May 19–20, 2026 |
| **Type** | Missing Authentication for Critical Functions + OS Command Injection + CSRF + Hard-Coded Credentials → Unauthenticated RCE |
| **Class** | CWE-306 (Missing Auth) · CWE-78 (OS Command Injection) · CWE-352 (CSRF) · CWE-798 (Hard-Coded Credentials) |
| **Affected Products** | ScadaBR 1.2.0 (ICS/SCADA HMI platform) |
| **Patch Status** | 🔴 **UNPATCHED — vendor unresponsive** (re-verified 2026-06-10) — Per CISA, ScadaBR has not responded to CISA's requests to develop mitigations; no fixed version listed. Remove external exposure immediately |
| **CVSS** | **9.1** (vendor-assigned, all four CVEs) |
| **Exploit Maturity** | ⚠️ DISCLOSED — Exploitation likelihood rated HIGH; no active exploitation confirmed for the 8602–8605 cluster |
| **CISA KEV** | ❌ Not listed (re-verified 2026-06-10). Note: a *separate, older* ScadaBR XSS CVE (CVE-2021-26829) is on CISA KEV (added 2025-11-28 after confirmed attacks) — distinct from this 2026 cluster; do not conflate |
| **Disclosed** | ~May 19–20, 2026 (CISA ICSA-26-139-03) |
| **Threat Level** | 🟠 HIGH — CVSS 9.1; ICS/OT targeting; three chainable vuln classes; unauthenticated RCE path viable; no active exploitation confirmed but high-value target class |
| **Admiralty Grade** | A2 — CISA-disclosed |
| **ATT&CK** | T1190 (Exploit Public-Facing Application) · T1059.004 (Unix Shell) · T1059 (Scripting) · T1498 (Network DoS — ICS impact) |

---

## Overview

CISA disclosed four high-severity vulnerabilities in ScadaBR 1.2.0 — an open-source ICS/SCADA HMI (Human-Machine Interface) platform used in industrial control environments. The four CVEs span three vulnerability classes that can be chained to achieve unauthenticated remote code execution against exposed ScadaBR instances.

### Why ScadaBR Matters

ScadaBR is widely deployed in utilities, water/wastewater, energy, and manufacturing SCADA environments globally. Compromise of a ScadaBR HMI provides:
- Direct visibility into and control over physical processes
- Pivot into the OT/ICS network segment
- Potential for process disruption, sensor spoofing, or physical damage

---

## Vulnerabilities

| CVE | Type | Impact |
|---|---|---|
| CVE-2026-8602 | Missing Authentication for Critical Functions | Unauthenticated crafted HTTP GET requests; inject arbitrary sensor readings / access restricted functions |
| CVE-2026-8603 | OS Command Injection | Arbitrary OS command execution with root privileges via injected input |
| CVE-2026-8604 | CSRF | A logged-in user lured to a malicious page triggers any session-permitted action |
| CVE-2026-8605 | Hard-Coded Credentials (CWE-798) | Fixed credentials allow administrative access (corrected 2026-06-10 — original profile said "additional auth bypass"; CISA classifies as hard-coded credentials) |

**Chain:** CVE-2026-8602 (missing auth) / CVE-2026-8605 (hard-coded creds) → CVE-2026-8603 (OS command injection, root) = unauthenticated RCE

---

## Mitigations

- **Remove external exposure** — ScadaBR should never be internet-facing; place behind a firewall immediately
- **Restrict to admin stations** — limit network access to trusted administrator workstations only
- **Enforce authentication** — deploy a WAF or reverse proxy with authentication in front of the application
- **Monitor** — watch for unusual process execution, configuration changes, and unexpected outbound connections
- Follow CISA advisory and vendor CSI guidance for patches when available

---

*Added: 2026-05-20 | CISA-disclosed (ICSA-26-139-03) | Vendor unresponsive — no patch*

---

## Intelligence Update — 2026-06-10

### Still UNPATCHED — vendor unresponsive to CISA; not on KEV; CVE-2026-8605 reclassified as hard-coded credentials

Patch-status re-verification against the CISA advisory (ICSA-26-139-03) and corroborating reporting. The cluster remains **unpatched**: CISA states ScadaBR has not responded to its requests to develop mitigations, and no fixed version is listed for the 8602–8605 cluster. The original "PATCH STATUS UNKNOWN" is now firmed up as "UNPATCHED — vendor unresponsive" (the absence of a fix is now confirmed, not merely unknown). Defensive posture is unchanged and the only viable control set: remove all external exposure, restrict to admin stations, front with an authenticating reverse proxy/WAF, and monitor for anomalous process execution and config changes.

Two corrections from the original profile:
- **CVE-2026-8605 root cause** is **hard-coded credentials (CWE-798)** per CISA — fixed credentials granting administrative access — not the "additional auth bypass" originally recorded.
- **CISA KEV:** the 8602–8605 cluster is **not** on CISA KEV. A separate, older ScadaBR cross-site-scripting CVE (CVE-2021-26829) was added to KEV on 2025-11-28 after confirmed attacks on a water-treatment honeypot; that is a distinct vulnerability and should not be conflated with this 2026 RCE cluster.

CVSS holds at 9.1 (vendor-assigned). No active exploitation confirmed for this cluster; no actor attribution. A&D relevance is indirect (ICS/OT HMI), tracked for OT-segment completeness.

| Date | Milestone |
|---|---|
| ~2026-05-19/20 | CISA ICSA-26-139-03 published; profile created |
| 2026-06-10 | Re-verified UNPATCHED (vendor unresponsive); not on KEV; CVE-2026-8605 corrected to hard-coded credentials |

*Updated: 2026-06-10 | Author: Archimedes (vuln-tracker) | Admiralty Grade: A2 — CISA-disclosed | TLP: CLEAR*
