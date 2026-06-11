# ssh-keysign-pwn — Linux LPE via ssh-keysign (SSH Server Private Key Read)

## Identity

| Field | Details |
|---|---|
| **Alias** | ssh-keysign-pwn (canonical) |
| **CVE** | **CVE-2026-46333** — assigned 2026-05-20 (Qualys TRU). This is the canonical dossier for the vulnerability; the former `CVE-2026-46333/` CVE-keyed dossier was consolidated into this one on 2026-06-10 (see consolidation note). |
| **Affected Function** | `__ptrace_may_access()` in the Linux kernel; FD theft via `pidfd_getfd()` during a transient ptrace permission window |
| **Type** | Local Privilege Escalation (LPE) → Root-Owned File Read (FD theft via `pidfd_getfd` during a transient ptrace window) |
| **Class** | Improper Access Control — ssh-keysign SUID binary's open root-owned file descriptors stolen during a privilege-drop ptrace window |
| **Latent Since** | ~9 years (Linux mainline v4.10-rc1, November 2016) |
| **Affected Systems** | All Linux kernels before upstream patch merged ~May 14, 2026 |
| **Confirmed Vulnerable Distros** | Debian 13, Ubuntu 24.04, Ubuntu 26.04, Fedora 43, Fedora 44 (default install, root execution confirmed by Qualys TRU) |
| **Patch Status** | ✅ **PATCHED** (as of 2026-06-10) — Upstream kernel patched 2026-05-14 by Linus Torvalds (commit `31e62c2ebbfd`); distribution backports have since SHIPPED across Debian, Ubuntu (24.04/26.04, Canonical guidance 2026-05-19), Fedora, RHEL, AlmaLinux (2026-05-15), SUSE, CloudLinux. Apply kernel update + reboot. |
| **CVSS** | Not yet scored; assessed **HIGH** — unprivileged user → root SSH key read; PoC public |
| **Exploit Maturity** | 🔴 **Public PoC** — Working PoC published by `_SiCK` within hours of patch commit analysis on May 14, 2026 |
| **Disclosed** | May 14–15, 2026 (patch landed May 14; PoC published same day) |
| **Discovered / PoC by** | **_SiCK** (same researcher responsible for Copy Fail 2 and related kernel LPE research) |
| **Prior Fix Proposed** | Yann Horn (Google Project Zero) proposed a fix for the underlying issue six years ago |
| **Threat Level** | 🟠 HIGH — Public PoC; enables SSH host key theft; low barrier on unpatched systems. Distro backports now shipped (2026-06-10); residual risk is unpatched/unrebooted estates. |
| **Admiralty Grade** | A2 — Public PoC; Qualys TRU vendor advisory + multiple distro confirmations (raised from B2 as vendor/distro confirmation landed) |
| **ATT&CK** | T1068 (Exploitation for Privilege Escalation) · T1552.004 (Unsecured Credentials: Private Keys) |

---

## Overview

**ssh-keysign-pwn** is a newly disclosed Linux local privilege escalation vulnerability involving the **`ssh-keysign` SUID binary**, a component of OpenSSH used to generate cryptographic signatures during host-based authentication. An unprivileged user can abuse `ssh-keysign`'s privileged execution to **read root-owned files**, with the most impactful application being the extraction of the **SSH server's private host key** — enabling impersonation of the server.

The upstream patch landed in Linus Torvalds' kernel tree on approximately May 14, 2026. Within hours, the researcher `_SiCK` — who had previously discovered Copy Fail 2 using the same technique of reverse-engineering patch commits — analyzed the fix and published a working PoC, collapsing the typical researcher-to-exploit timeline.

**A fix was proposed by Yann Horn (Google Project Zero) six years ago** but was not merged into the kernel mainline at the time. The vulnerability existed in all kernels up through May 14, 2026.

> **Consolidation note (2026-06-10):** The CVE for this issue was assigned **CVE-2026-46333** (Qualys TRU, 2026-05-20). A separate CVE-keyed `threats/vulnerabilities/CVE-2026-46333/` dossier previously tracked the same underlying flaw — the `__ptrace_may_access()` / `pidfd_getfd()` FD-theft window that lets an unprivileged user steal `ssh-keysign`'s open SSH-host-key file descriptors. These were **one vulnerability under two names** (the "ssh-keysign-pwn" PoC alias vs. the assigned CVE). The duplicate has now been **consolidated into this canonical dossier**; the CVE-2026-46333 directory carries a tombstone redirect pending librarian `git rm`. Unique technical detail from that dossier (Qualys TRU's four exploit variants, root-cause analysis, the "4th Linux kernel LPE in 3 weeks" context, and high-risk scenarios) is folded in below.

---

## Technical Analysis

### How ssh-keysign Works

`ssh-keysign` is installed as a **SUID binary** — it runs with root privileges when executed by any user, enabling it to access the SSH host private key files (typically `/etc/ssh/ssh_host_*_key`) on behalf of the SSH daemon. Its intended purpose is limited: sign challenges during SSH host-based authentication without requiring the daemon to hold the key directly.

### The Exploitation Path

The vulnerability enables an unprivileged user to invoke `ssh-keysign` in a manner that causes it to **read arbitrary root-owned files** beyond its intended scope. This can be triggered to read:
- **SSH private host keys** (`/etc/ssh/ssh_host_rsa_key`, `ssh_host_ed25519_key`, etc.)
- Potentially other sensitive root-owned files depending on the exploitation approach

### Root Cause (folded from CVE-2026-46333 dossier)

The vulnerability resides in `__ptrace_may_access()` — the kernel function that decides whether one process may ptrace-attach to another. The function correctly blocks ptrace across privilege boundaries **except** during a brief race window that opens when a process is dropping elevated privileges (e.g., a setuid binary transitioning from root to the invoking user's UID). During that transient window:

- `__ptrace_may_access()` temporarily permits ptrace access from a lower-privileged attacker process
- The attacker establishes a ptrace relationship before the window closes
- Via `pidfd_getfd()`, the attacker steals any file descriptor currently open in the target process

The bug was latent in the kernel for roughly 9 years (mainline v4.10-rc1, November 2016). Qualys reported it privately on 2026-05-11; the upstream fix landed publicly 2026-05-14.

### Exploit Variants (Qualys TRU PoC)

Qualys TRU published a full PoC with four variants targeting different SUID/privileged binaries that briefly open privileged resources. Per Hard Rule 3, only the affected component and outcome class are recorded — no attack-step detail:

| Exploit Target | What It Accesses | Outcome Class |
|---|---|---|
| `chage` (password-expiry change) | Privileged shadow-file operations | Root command execution |
| `ssh-keysign` (SSH host-key signing) | SSH host private-key FDs (`ssh_host_*_key`) | SSH private-key theft → server impersonation |
| `pkexec` (PolicyKit elevation) | PolicyKit privilege-elevation path | Root command execution |
| `accounts-daemon` (AccountsService) | System account management | Root command execution |

All four were confirmed achieving root command execution or credential theft on default installs of Debian 13, Ubuntu 24.04/26.04, Fedora 43/44.

### Impact of SSH Host Key Theft

Possession of a server's SSH private host key allows an attacker to:
1. **Impersonate the server** — perform man-in-the-middle attacks against SSH clients connecting to that host
2. **Defeat known_hosts verification** — clients that previously trusted the server will accept connections from the attacker
3. **Decrypt cached sessions** — in some configurations, historic SSH sessions may be decryptable

### Researcher Context

`_SiCK` has established a pattern of discovering Linux kernel LPEs by analyzing kernel patch commits and reverse-engineering the vulnerability from the fix:
- **Copy Fail 2** — discovered via the same commit-analysis methodology
- **ssh-keysign-pwn** — PoC published within ~1 hour of analyzing the upstream fix commit

This methodology means future kernel patches may similarly produce PoCs within hours of upstream merges.

---

## Affected Scope

- **All Linux kernels** up to (and including) the last kernel before the May 14, 2026 upstream patch
- **All major Linux distributions** — patched kernels have shipped as of 2026-06-10 (Debian, Ubuntu, RHEL, AlmaLinux, Rocky Linux, Fedora, SUSE, CloudLinux). Unpatched/unrebooted hosts remain exposed.
- Any system with `ssh-keysign` installed (default in most OpenSSH deployments on Linux) that has not yet applied the kernel update

---

## Context: 4th Linux Kernel LPE in 3 Weeks (folded from CVE-2026-46333 dossier)

| Name | CVE | Disclosed | Status (as of 2026-06-10) |
|---|---|---|---|
| Copy Fail | CVE-2026-31431 | ~May 1 | Patched across major distros; CISA KEV |
| Dirty Frag (ESP + RxRPC) | CVE-2026-43284 + CVE-2026-43500 | ~May 7 | Both halves patched + backported |
| Fragnesia | CVE-2026-46300 | ~May 13 | Upstream patched; distro backports shipped |
| **ssh-keysign-pwn** | **CVE-2026-46333** | ~May 14–20 | Upstream patched; distro backports shipped (not in KEV) |

A concentration of four Linux kernel LPEs in a three-week window (May 2026), the latter primarily via Qualys TRU. For A&D Linux fleets (server, container, OT/ICS) this represents meaningful attack-surface expansion.

## High-Risk Scenarios (folded from CVE-2026-46333 dossier)

| Scenario | Risk | Notes |
|---|---|---|
| Multi-user Linux servers (web, cloud, shared hosting) | CRITICAL | Any local user can reach root |
| Container environments with host PID-namespace sharing | HIGH | Container-escape path if host ptrace not isolated |
| Linux-based ICS/OT systems with local access | HIGH | LPE on OT Linux → potential process impact |
| SSH-enabled servers where key theft = infrastructure access | HIGH | ssh-keysign path steals host private keys |

## Distribution Patch Status (folded from CVE-2026-46333 dossier)

| Distribution | Status |
|---|---|
| Upstream kernel | Patched — commit `31e62c2ebbfd` (Linus Torvalds, 2026-05-14) |
| Debian | Backport shipped |
| Fedora 43/44 | Backport shipped |
| RHEL / CentOS Stream | Backport shipped |
| SUSE / openSUSE | Backport shipped |
| AlmaLinux | Backport shipped (advisory 2026-05-15) |
| CloudLinux | Backport shipped + Yama mitigation |
| Ubuntu 24.04 / 26.04 | Patched kernels in standard repos; Canonical guidance 2026-05-19 |

## Mitigations

Distribution kernel patches have shipped (as of 2026-06-10) — patch + reboot is the primary remediation. Tightening Yama `ptrace_scope` to `2` (admin-only attach) or `3` (no attach) blocks the public exploits and is the recommended no-reboot interim control. The measures below remain useful defense-in-depth on hosts pending a maintenance window:

1. **Remove the SUID bit from ssh-keysign** — this disables host-based SSH authentication but eliminates the attack surface
   ```bash
   chmod 0755 /usr/lib/openssh/ssh-keysign  # Debian/Ubuntu
   chmod 0755 /usr/libexec/openssh/ssh-keysign  # RHEL/CentOS/Fedora
   ```
   ⚠️ This disables `HostbasedAuthentication` — only apply if host-based auth is not in use
2. **Rotate SSH host keys after patching** — if exploitation cannot be ruled out, regenerate host keys to invalidate any previously extracted material
3. **Monitor for unexpected ssh-keysign invocations** — audit SUID binary execution; ssh-keysign should only be called by the ssh daemon, not user processes
4. **Apply upstream kernel patch** — distributions expected to ship fixes within days

---

## Detection

### Process-Level Indicators
- `ssh-keysign` invoked by non-root, non-sshd processes
- Unexpected access to `/etc/ssh/ssh_host_*_key` files from non-root UIDs
- Audit rules: `-a always,exit -F arch=b64 -S execve -F path=/usr/lib/openssh/ssh-keysign -k ssh_keysign_exec`

### File Access Monitoring
- Inotify or auditd watch on `/etc/ssh/ssh_host_*_key` — any read by a non-root UID is anomalous

---

## MITRE ATT&CK Mapping

| Tactic | Technique | Notes |
|---|---|---|
| Privilege Escalation | T1068 — Exploitation for Privilege Escalation | SUID binary abuse to escalate read access |
| Credential Access | T1552.004 — Unsecured Credentials: Private Keys | SSH host private key extraction is primary goal |
| Lateral Movement | T1021.004 — Remote Services: SSH | Stolen host key enables server impersonation |
| Defense Evasion | T1550.003 — Use Alternate Authentication Material | Impersonating server defeats SSH client host verification |

---

## Disclosure Timeline

| Date | Event |
|---|---|
| ~6 years prior | Yann Horn (Google Project Zero) proposes fix for underlying issue — not merged |
| 2026-05-14 | Upstream kernel patch merged by Linus Torvalds (commit `31e62c2ebbfd`) |
| 2026-05-14 | `_SiCK` analyzes patch commit; publishes working PoC ~1 hour later |
| 2026-05-15 | Profile created; distribution packages still pending; AlmaLinux patch published |
| 2026-05-19 | Canonical guidance — Ubuntu 24.04/26.04 patched kernels in standard repos |
| 2026-05-20 | CVE-2026-46333 assigned (Qualys TRU public advisory) |
| 2026-06-10 | Distribution backports shipped across all major distros; status PATCHED; not in CISA KEV |

---

## References

- [AllSec.sh — ssh-keysign-pwn: Linux LPE allows unprivileged users to read root-owned files (May 14–15, 2026)](https://allsec.sh/tag/Zero-Day)
- Linux Kernel upstream commit `31e62c2ebbfd` (2026-05-14) — ptrace/ssh-keysign privilege logic fix
- [Qualys — CVE-2026-46333 ptrace path LPE & credential disclosure](https://blog.qualys.com/vulnerabilities-threat-research/2026/05/20/cve-2026-46333-local-root-privilege-escalation-and-credential-disclosure-in-the-linux-kernel-ptrace-path)
- [AlmaLinux — ssh-keysign-pwn (CVE-2026-46333) Patches Released](https://almalinux.org/blog/2026-05-15-ssh-keysign-pwn-cve-2026-46333/)
- [Ubuntu — ssh-keysign-pwn (CVE-2026-46333) fixes available](https://ubuntu.com/blog/ssh-keysign-pwn-linux-vulnerability-fixes-available)

---

## Intelligence Update — 2026-06-10

### Status Flipped PARTIAL → PATCHED; CVE Assigned (CVE-2026-46333); Duplicate of CVE-2026-46333 Dossier Flagged

Two updates since profile creation. First, the patch gap has closed: the May-15 "distribution packages pending" status is superseded — distro kernel backports have shipped across Debian, Ubuntu (Canonical guidance 2026-05-19), Fedora, RHEL, AlmaLinux (2026-05-15), SUSE, and CloudLinux. Patch availability is no longer the gating factor; rollout (kernel update + reboot, or Yama `ptrace_scope` ≥ 2 as a no-reboot stopgap) is the remaining task.

Second, the CVE that was "TBD" at profile creation has been assigned as **CVE-2026-46333** by Qualys TRU. Archimedes already maintains a separate `CVE-2026-46333/` dossier for the same underlying `__ptrace_may_access()` / `pidfd_getfd()` FD-theft flaw. **This "ssh-keysign-pwn" profile and the CVE-2026-46333 dossier are one vulnerability tracked under two names.** This pass does not consolidate them (out of scope per task instruction) but flags the duplicate for orchestrator review.

No CISA KEV listing as of 2026-06-10; no named-actor attribution in the reporting reviewed (Hard Rule 2). Public PoC remains operational against unpatched kernels.

| Date | Milestone |
|---|---|
| 2026-05-14 | Upstream fix committed (`31e62c2ebbfd`); PoC published same day |
| 2026-05-19 | Ubuntu patched kernels confirmed (Canonical) |
| 2026-05-20 | CVE-2026-46333 assigned (Qualys TRU) |
| 2026-06-10 | Status PATCHED across all major distros; duplicate-of-CVE-2026-46333 flagged; not in KEV |

*Updated: 2026-06-10 | Author: Archimedes | Admiralty Grade: A2 — Qualys advisory + Canonical/AlmaLinux/CloudLinux distro confirmations; no actor attribution | TLP: WHITE*

---

*Profile created: 2026-05-15 | Author: C3PO | Admiralty Grade: B2 | TLP: WHITE*
