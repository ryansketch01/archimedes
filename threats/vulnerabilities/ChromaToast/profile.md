# CVE-2026-45829 — ChromaToast: Pre-Auth RCE in ChromaDB Python Server (CVSS 10.0)

## Identity

| Field | Details |
|---|---|
| **CVE** | CVE-2026-45829 |
| **Alias** | ChromaToast |
| **Vendor Advisory** | None — no official security advisory from ChromaDB maintainers as of 2026-06-10 (re-verified) |
| **Type** | Pre-Authentication Remote Code Execution / Logic Error in Auth Ordering |
| **Class** | CWE-269 — Improper Privilege Management; CWE-287 — Improper Authentication |
| **Affected Products** | ChromaDB Python FastAPI API server, versions 1.0.0 through 1.5.8 |
| **Not Affected** | ChromaDB Rust-based frontend; local-only (non-API-server) deployments |
| **Patch Status** | 🔴 **UNPATCHED** (re-verified 2026-06-10) — No official patch or security advisory. v1.5.9 question RESOLVED: v1.5.9 shipped ~2 weeks before disclosure but does NOT remediate the flaw (the vulnerable code path persists); researchers and CSO Online confirm "unpatched in v1.5.9 (latest)." GitHub issue #6717 remains open with no PR/fix; maintainers still unresponsive since the February 2026 report |
| **CVSS** | **10.0 (Critical)** |
| **Exploit Maturity** | ⚠️ **DISCLOSED** — Vulnerability details public; no weaponized public PoC confirmed but the attack path is trivially reconstructable |
| **CISA KEV** | Not listed (re-verified 2026-06-10) — no active exploitation confirmed |
| **Exposed Instances** | ~73% of internet-facing ChromaDB instances running vulnerable versions (HiddenLayer telemetry, May 2026) |
| **Disclosed** | May 19, 2026 (reported to maintainers February 2026 by HiddenLayer) |
| **Threat Level** | 🔴 CRITICAL — CVSS 10.0; unauthenticated; full server takeover; AI/ML pipeline targeting; vector database = API keys + embeddings + raw data |
| **Admiralty Grade** | B2 — Reported by credible security firm (HiddenLayer); no confirmation from vendor |
| **ATT&CK** | T1190 (Exploit Public-Facing Application) · T1059 (Command and Scripting Interpreter) · T1552 (Unsecured Credentials) · T1005 (Data from Local System) |

---

## Overview

CVE-2026-45829 ("ChromaToast") is a pre-authentication remote code execution vulnerability in the Python FastAPI server of ChromaDB — a widely-used vector database for AI/RAG (Retrieval Augmented Generation) applications.

The vulnerability stems from a fundamental logic error: **authentication is checked after client-supplied configuration is processed**, not before. This means an unauthenticated attacker can dictate model-loading parameters — including the `trust_remote_code` flag — before the server ever validates credentials.

### Why It Matters for AI Environments

ChromaDB is the default vector store in thousands of AI and RAG pipelines. Successful exploitation against an exposed instance yields:
- Full server takeover with the privileges of the ChromaDB process
- Exfiltration of API keys, environment variables, mounted secrets
- Access to the underlying vector store (embeddings, documents, metadata)
- Pivot point for broader network intrusion into AI/ML infrastructure

The attack completes silently — the server returns a 500 error after the payload executes (the delayed auth check fails), hiding the successful compromise behind normal application noise.

---

## Technical Analysis

### Root Cause

The `/api/v2/tenants/{tenant}/databases/{db}/collections` endpoint processes incoming JSON before verifying the caller's identity. Within the configuration payload, clients can set `trust_remote_code=True` and supply a Hugging Face repository path as the embedding model source.

The server fetches and **executes the model's initialization code** before the auth check runs. Any code in the model's `__init__` executes with the server's process privileges.

### Attack Flow

1. Attacker stages a malicious model on a public or attacker-controlled repository
2. Attacker sends unauthenticated POST to collection creation endpoint
3. Payload includes `trust_remote_code: true` + attacker's model path in `kwargs`
4. Server fetches and initializes model — malicious `__init__` code executes
5. Server encounters delayed auth failure → returns HTTP 500 (attack already complete)

### Affected Scope

- All Python FastAPI ChromaDB server deployments 1.0.0–1.5.8
- Any instance with the API port exposed to untrusted networks
- Cloud deployments, SaaS wrappers, CI/CD test environments with ChromaDB

---

## Mitigations

**Immediate:**
- Firewall the ChromaDB API port — it should never be publicly accessible
- Restrict access to trusted internal clients only via network security groups
- Audit environment variables and secrets mounted in ChromaDB containers

**Architectural:**
- Migrate to Rust-based ChromaDB frontend (not affected)
- Move to local-only deployments that do not expose the API server

**If building from source:**
- Move authentication verification to occur *before* any configuration loading
- Strip `kwargs` from incoming collection creation payloads to block parameter injection

---

*Added: 2026-05-20 | Reporter: HiddenLayer (February 2026) | No vendor patch confirmation*

---

## Intelligence Update — 2026-06-10

### Patch-status re-verification: still UNPATCHED; the v1.5.9 ambiguity is now resolved as "does not fix"

Re-checked against NVD, the ChromaDB GitHub issue (#6717), the HiddenLayer research report, and independent reporting (CSO Online, Hadrian, CVEReports). The status is unchanged at the headline level — no official patch, no vendor security advisory, maintainers still unresponsive since the February 2026 disclosure — but the open question from the original profile is now closed.

**v1.5.9 does NOT remediate CVE-2026-45829.** Version 1.5.9 became available roughly two weeks before public disclosure; researchers and CSO Online explicitly state the flaw "remains unpatched in v1.5.9 (latest at time of writing)" because the vulnerable model-reference parsing path still executes ahead of the authentication check. The only protections remain the operational ones already in this profile: run the Rust server path (not affected), and firewall the API port to trusted clients. A source-described local hotfix exists (reorder the auth check ahead of collection-config loading and strip the remote-code-trust parameter from embedding-function kwargs) — recorded as a configuration-hardening pointer, not reproduced as code (Hard Rule 3).

NVD lists the record as "Awaiting Enrichment"; CNA (HiddenLayer) CVSS v4.0 10.0 stands. Affected scope on NVD reads "1.0.0 and later" — broader than the original "1.0.0–1.5.8" framing precisely because 1.5.9 does not fix it. Not on CISA KEV; no confirmed in-the-wild exploitation. No threat actor attributed.

| Date | Milestone |
|---|---|
| 2026-05-19/20 | Disclosed; profile created; v1.5.9 "may address, unconfirmed" |
| 2026-06-10 | Re-verified UNPATCHED; v1.5.9 confirmed NOT a fix; still no advisory, no KEV, no confirmed exploitation |

*Updated: 2026-06-10 | Author: Archimedes (vuln-tracker) | Admiralty Grade: B2 — credible security-firm reporting (HiddenLayer) corroborated by independent press; no vendor confirmation | TLP: CLEAR*
