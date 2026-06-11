# NVIDIA Triton Inference Server — CVE-2026-24207 Authentication Bypass + AI Infrastructure CVE Cluster

## Identity

| Field | Details |
|---|---|
| **Lead CVE** | CVE-2026-24207 (CVSS Critical — authentication bypass → RCE/EoP/DoS) |
| **Additional CVEs** | CVE-2026-24206 (auth bypass, high) · CVE-2026-24213/24214 (DALI backend OOB/overflow) · CVE-2026-24209/24208 (path traversal) · CVE-2026-24215 (resource exhaustion) · CVE-2026-24163/24142/24160 (TRT-LLM deserialization/RCE) · CVE-2025-33255 (TRT-LLM MPI server deserialization) |
| **Vendor Advisory** | NVIDIA Security Bulletin — May 18–20, 2026 |
| **Type** | Authentication Bypass + Code Execution / Privilege Escalation / Denial of Service |
| **Affected Products** | NVIDIA Triton Inference Server (all affected versions) · NVIDIA TensorRT-LLM (TRT-LLM) |
| **Patch Status** | ✅ PATCHED (re-verified 2026-06-10) — Fixed in **Triton Inference Server / DALI Backend r26.03** (Linux). Update to r26.03 or later; apply latest TensorRT-LLM release per NVIDIA bulletin |
| **CVSS** | CVE-2026-24207: **9.8 Critical** (CVSS v3.1 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, NVIDIA CNA) · CVE-2026-24213: 8.0 · CVE-2026-24214: 7.5 · CVE-2026-24209: 7.5 · CVE-2026-24208: 5.3; CVE-2026-24206: High |
| **Exploit Maturity** | No active exploitation confirmed (re-verified 2026-06-10) |
| **CISA KEV** | Not listed (re-verified 2026-06-10) |
| **Disclosed** | May 18–20, 2026 |
| **Threat Level** | 🟠 HIGH — Critical auth bypass on AI inference infrastructure; no active exploitation but high-value target for AI lab and enterprise ML environments |
| **Admiralty Grade** | A1 — NVIDIA-confirmed and patched |
| **ATT&CK** | T1190 (Exploit Public-Facing Application) · T1068 (EoP) · T1499 (DoS) · T1552 (Credential Access) |

---

## Overview

NVIDIA released a cluster of security patches for **Triton Inference Server** and **TensorRT-LLM** covering authentication bypasses, code execution paths, deserialization vulnerabilities, and resource exhaustion issues. The lead vulnerability (CVE-2026-24207) is a critical authentication bypass that can lead to code execution, privilege escalation, data tampering, and denial of service.

### Why AI Inference Infrastructure Matters

Triton Inference Server is NVIDIA's production-grade inference platform, deployed at scale in:
- Enterprise AI/ML production environments
- Defense and intelligence AI applications
- Research lab inference clusters
- Cloud AI APIs built on NVIDIA infrastructure

Compromise of a Triton server provides:
- Access to models and their weights (IP theft)
- Access to inference request data (potentially sensitive inputs)
- Pivot into the GPU cluster and broader ML infrastructure
- Model poisoning or substitution potential

---

## Key CVEs

| CVE | Type | Severity | Notes |
|---|---|---|---|
| CVE-2026-24207 | Authentication Bypass → RCE/EoP/DoS/InfoDisc | **9.8 Critical** | Core inference server; code execution, privesc possible. Fixed in r26.03 |
| CVE-2026-24206 | Authentication Bypass → EoP/DoS/InfoDisc | High | Secondary auth bypass path |
| CVE-2026-24213 | OOB Read / DALI Backend → RCE/DoS/InfoDisc | High | Data pipeline component |
| CVE-2026-24214 | Integer Overflow / DALI Backend → Code Exec/DoS | High | Data pipeline component |
| CVE-2026-24163 | Unsafe Deserialization / TRT-LLM RPC → RCE/DoS | High | TensorRT-LLM component (requires high priv) |
| CVE-2025-33255 | Unsafe Deserialization / TRT-LLM MPI Server → RCE | High | MPI server component |
| CVE-2026-24142 | Deserialization + Unsafe Handle / TRT-LLM | Medium | Data tampering, InfoDisc |

---

## Mitigations

- **Update immediately** — apply latest NVIDIA Triton Inference Server and TRT-LLM releases per NVIDIA security bulletin
- **Restrict network access** — Triton inference ports should not be publicly exposed; restrict to trusted internal clients
- **Audit deployment configs** — review who has access to inference endpoints and model loading interfaces
- Monitor for unusual model loading, unexpected lateral movement from GPU nodes

---

*Added: 2026-05-20 | NVIDIA security bulletin May 2026 | Patch available — update immediately*

---

## Intelligence Update — 2026-06-10

### Fixed version pinned (r26.03); lead CVSS confirmed 9.8; still no confirmed exploitation

Patch-status re-verification against NVD (CVE-2026-24207) and the NVIDIA May 2026 Triton security bulletin (custhelp a_id 5828). The original "UPDATE AVAILABLE" status is now firmed up with a concrete fixed version: **all affected Triton Inference Server and DALI Backend versions prior to r26.03 (Linux) are vulnerable; r26.03 is the fixed release.** Apply the latest TensorRT-LLM release per the bulletin for the TRT-LLM-component CVEs.

Lead vulnerability CVE-2026-24207 is confirmed **CVSS v3.1 9.8 Critical** (NVIDIA CNA; NVD awaiting its own enrichment) — an unauthenticated, network, low-complexity authentication bypass that can lead to code execution, privilege escalation, data tampering, DoS, or information disclosure. Companion CVEs scored: CVE-2026-24213 (8.0, OOB read), CVE-2026-24214 (7.5, integer overflow), CVE-2026-24209 (7.5) and CVE-2026-24208 (5.3) path traversal.

No active exploitation confirmed; not on CISA KEV. Status remains PATCHED (vendor fix shipped). No threat actor attributed.

| Date | Milestone |
|---|---|
| 2026-05-18/20 | NVIDIA bulletin published; profile created |
| 2026-06-10 | Fixed version confirmed r26.03; CVE-2026-24207 CVSS 9.8 confirmed; no exploitation; not on KEV |

*Updated: 2026-06-10 | Author: Archimedes (vuln-tracker) | Admiralty Grade: A1 — NVIDIA-confirmed and patched | TLP: CLEAR*
