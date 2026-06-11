# UniFi OS Security Advisory 064 — Triple CVSS 10.0 Cluster (Command Injection + Path Traversal + Access Control)

## Identity

| Field | Details |
|---|---|
| **Cluster ID** | ZD-060 |
| **Vendor Advisory** | Ubiquiti Security Advisory Bulletin 064 |
| **CVEs** | CVE-2026-34910 (CVSS 10.0) · CVE-2026-34909 (CVSS 10.0) · CVE-2026-34908 (CVSS 10.0) · CVE-2026-33000 (CVSS 9.1) · CVE-2026-34911 (CVSS 7.7) |
| **Types** | Command Injection (Unauthenticated) · Path Traversal → Account Access (Unauthenticated) · Improper Access Control (Unauthenticated) · Command Injection (High-Priv) · Path Traversal → Info Disclosure |
| **Affected Product** | Ubiquiti UniFi OS — all device families (UDM, UCG-Industrial, UDR, UNVR, UCKP, UCK, UNAS, etc.) |
| **Patch Status** | ✅ PATCHED — UniFi OS 5.1.12 (most devices) / 5.1.11 (UDM-Beast) / 5.0.8 (UniFi OS Server) / 5.1.10 (UNAS) |
| **CISA KEV** | Not listed — verified absent from CISA KEV catalog 2026-06-10; no active exploitation confirmed as of 2026-06-10 |
| **Disclosed** | May 21–22, 2026 (Ubiquiti Security Advisory Bulletin 064) |
| **Threat Level** | 🔴 HIGH — Three unauthenticated CVSS 10.0 CVEs in ubiquitous enterprise networking gear; network perimeter gear; patch immediately |
| **Admiralty Grade** | A2 — Vendor-confirmed with patch; exploit reported available |
| **ATT&CK** | T1190 (Exploit Public-Facing Application) · T1059 (Command and Scripting Interpreter) · T1078 (Valid Accounts via credential access) |

---

## Overview

Ubiquiti released Security Advisory Bulletin 064 on May 21–22, 2026, disclosing **five vulnerabilities in UniFi OS** — the operating system powering all Ubiquiti Dream Machine, Cloud Gateway, UniFi Network Recorder, Cloud Key, and NAS device families. Three of the five vulnerabilities carry **CVSS 10.0 (maximum severity)** and are exploitable by unauthenticated network attackers.

UniFi OS devices are among the most widely deployed network infrastructure products globally, used in enterprise, government, education, healthcare, and defense environments. UniFi Dream Machines (UDMs) commonly serve as network perimeter gateways, firewalls, and VPN endpoints. A compromised UniFi OS device grants the attacker control over the network boundary.

---

## Vulnerability Breakdown

### CVE-2026-34910 — Unauthenticated Command Injection (CVSS 10.0)
**CWE-78 — Improper Neutralization of Special Elements in OS Command**

A malicious actor with network access — **no privileges required** — can exploit an improper input validation vulnerability in UniFi OS devices to execute arbitrary OS commands. CVSS vector: `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`. Full network compromise from unauthenticated position.

*Affected:* UCG-Industrial ≤ 5.0.13 · UDM/UDM-Pro/UDM-SE/UDM-Pro-Max/EFG/UDW/UDR/UDR7/Express 7/UNVR variants ≤ 5.0.16 · UDR-5G/ENVR-Core/UCKP/UCK/UCK-Enterprise ≤ 5.0.17 · UniFi OS Server ≤ 5.0.6 · UNVR-G2/UNVR-G2-Pro ≤ 5.1.11 · UDM-Beast/UNAS variants ≤ 5.1.8

*Fix:* Update to UniFi OS 5.1.12 (or version-specific fix per device family)

### CVE-2026-34909 — Unauthenticated Path Traversal → Account Access (CVSS 10.0)
**CWE-22 — Path Traversal**

A malicious actor with network access — **no privileges required** — can exploit a path traversal vulnerability to access underlying system files that can be manipulated to **access an underlying account** (credential theft / privilege acquisition). CVSS vector: `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`.

*Affected:* Same device matrix as CVE-2026-34910

*Fix:* Update to UniFi OS 5.1.12 (or version-specific fix per device family)

### CVE-2026-34908 — Unauthenticated Improper Access Control → Unauthorized System Changes (CVSS 10.0)
**CWE-284 — Improper Access Control**

A malicious actor with network access — **no privileges required** — can exploit an access control vulnerability to **make unauthorized changes to the system** — modifying network configuration, firewall rules, VPN endpoints, routing, or other OS-level settings. CVSS vector: `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`.

*Affected:* UCG-Industrial ≤ 5.0.13 · UDM/UDM-Pro and variants ≤ 5.0.16 (and other affected families)

*Fix:* Update to UniFi OS 5.1.12 (or version-specific fix per device family)

### CVE-2026-33000 — High-Privilege Command Injection (CVSS 9.1)
**CWE-78 — Improper Neutralization of Special Elements in OS Command**

A malicious actor with network access **and high privileges** can execute a command injection via improper input validation. Requires elevated access but still critical given the management plane context.

*Affected:* UniFi OS Server ≤ 5.0.6

*Fix:* Update UniFi OS Server to 5.0.8 or later

### CVE-2026-34911 — Low-Privilege Path Traversal → Information Disclosure (CVSS 7.7)
**CWE-22 — Path Traversal**

Low-privileged user with network access can read arbitrary files from the underlying system, enabling sensitive information disclosure.

*Fix:* Update to UniFi OS 5.1.12 (or version-specific fix per device family)

---

## Target Device Matrix and Required Patch Versions

| Device Family | Affected Version | Fix Version |
|---|---|---|
| UCG-Industrial | ≤ 5.0.13 | 5.1.12 |
| UDM, UDM-Pro, UDM-SE, UDM-Pro-Max, EFG, UDW, UDR, UDR7, Express 7, UNVR, UNVR-Pro, UNVR-Instant, ENVR, UCG-Ultra, UCG-Max, UCG-Fiber | ≤ 5.0.16 | 5.1.12 |
| UDR-5G, ENVR-Core, UCKP, UCK, UCK-Enterprise | ≤ 5.0.17 | 5.1.12 |
| UniFi OS Server | ≤ 5.0.6 | 5.0.8 |
| UNVR-G2, UNVR-G2-Pro | ≤ 5.1.11 | 5.1.12 |
| UDM-Beast | ≤ 5.1.8 | 5.1.11 |
| UNAS-2, UNAS-4, UNAS-Pro, UNAS-Pro-4, UNAS-Pro-8 | ≤ 5.1.8 | 5.1.10 |

---

## Risk Assessment

UniFi OS devices are **network perimeter infrastructure**. Their role in most enterprise deployments:
- **UDM/UDM-Pro**: Default gateway, firewall, IDS/IPS, VPN endpoint
- **UCG-Industrial**: OT/industrial network gateway
- **UNVR**: Physical security / network video recorder infrastructure
- **UCK/UCKP**: Cloud Key — manages all UniFi controller state

Compromise of any of these via the unauthenticated CVSS 10.0 vulnerabilities grants:
1. Full OS command execution on the gateway/perimeter device
2. Firewall rule modification (disable blocking, add pass-through rules)
3. VPN credential access / key theft
4. Lateral movement into all network segments behind the device
5. Traffic interception and man-in-the-middle positioning
6. Persistent access via implants in the UniFi OS layer

The combination of **unauthenticated access + command injection + path traversal targeting credentials** means a single CVE-2026-34909/34910 exploit provides both execution and credential access — a self-reinforcing attack chain.

---

## Remediation

1. **Patch immediately** — Open UniFi OS Controller → Firmware Updates → verify all devices are at patched version
2. **Prioritize internet-facing devices** — UCG-Industrial, UDM-Pro, UDR, EFG devices with WAN-exposed management are highest risk
3. **Restrict management access** — UniFi OS management interface should not be internet-exposed; enforce firewall rules blocking management ports from untrusted sources
4. **Review UniFi Network Application access logs** — look for unexpected admin login attempts, configuration changes, or unexpected firmware update attempts
5. **Check for IoCs** — unexpected outbound connections from gateway devices; anomalous routing/firewall rule changes

---

## Detection

### Network Indicators
- Unexpected HTTP/HTTPS requests to UniFi OS management interface from external IPs
- OS command execution evidence in UniFi OS system logs (unexpected spawned processes)
- Path traversal sequences (`../`) in management interface request logs
- Unexpected configuration changes to firewall rules, routing tables, or VPN settings

### MITRE ATT&CK Mapping

| Tactic | Technique | Notes |
|---|---|---|
| Initial Access | T1190 — Exploit Public-Facing Application | Unauthenticated; network-reachable UniFi OS management |
| Execution | T1059 — Command and Scripting Interpreter | OS command injection via CVE-2026-34910 or CVE-2026-33000 |
| Credential Access | T1078 — Valid Accounts | CVE-2026-34909 path traversal → underlying account access |
| Defense Evasion | T1562.004 — Disable or Modify System Firewall | Firewall rule modification via CVE-2026-34908 access control bypass |
| Persistence | T1505.003 — Web Shell | Post-RCE persistence on network infrastructure device |
| Lateral Movement | T1021 — Remote Services | Compromised gateway provides pivot point into all downstream segments |

---

## References

- [Ubiquiti Security Advisory Bulletin 064](https://community.ui.com/releases/Security-Advisory-Bulletin-064-064/84811c09-4cf4-42ab-bd61-cc994445963b)
- [GitHub Advisory Database — CVE-2026-34908 (GHSA-p8c5-xwrc-584f)](https://github.com/advisories/GHSA-p8c5-xwrc-584f)
- [Releasebot.io — Ubiquiti UniFi OS May 2026 Security Update](https://releasebot.io/updates/ubiquiti)
- [CERT CVE HR — CVE-2026-34910/34909/34908 (May 22, 2026)](https://cve.cert.hr)

---

*Profile created: 2026-05-22 | Author: C3PO | Admiralty Grade: A2 | TLP: WHITE*
