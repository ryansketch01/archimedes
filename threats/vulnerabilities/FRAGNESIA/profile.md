# Fragnesia — Linux Kernel LPE (Dirty Frag Class — Logic Bug Variant)

## Identity

| Field | Details |
|---|---|
| **Alias** | Fragnesia |
| **CVE** | **CVE-2026-46300** (CVSS 7.8) — assigned May 2026; XFRM logic bug class |
| **Related CVEs** | CVE-2026-43284 (ESP / Dirty Frag parent), CVE-2026-43500 (RxRPC / Dirty Frag parent) — see ZD-017 |
| **Vendor Advisory** | Linux kernel upstream patch merged May 13, 2026 |
| **Type** | Local Privilege Escalation (LPE) |
| **Class** | Logic Bug — XFRM/ESP and TCP subsystem; improper page cache write primitive |
| **Affected Systems** | All Linux kernel versions **before May 13, 2026 upstream patch** (all major distributions) |
| **Patch Status** | ✅ **PATCHED** (as of 2026-06-10) — Upstream Linux kernel patched May 13, 2026; distribution backports have since SHIPPED across AlmaLinux, Ubuntu (all supported LTS), Debian, RHEL (RHSB-2026-003), and CloudLinux/KernelCare. Apply distro kernel updates + reboot. |
| **CVSS** | **7.8 HIGH** (CVE-2026-46300, CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) |
| **Exploit Maturity** | 🔴 **Public PoC** — Full exploit with page cache corruption published May 13, 2026 by William Bowling (Zelic) |
| **Disclosed** | 2026-05-13 |
| **Discovered By** | William Bowling (Zelic Security Research) |
| **Threat Level** | 🟠 HIGH — Public PoC achieving root shell; more reliable than Dirty Frag (no race condition). Distro backports now shipped (2026-06-10); residual risk is unpatched/unrebooted estates. |
| **Admiralty Grade** | A2 — Researcher-confirmed full PoC; upstream kernel patched |
| **ATT&CK** | T1068 (Exploitation for Privilege Escalation) · T1611 (Escape to Host — container breakout) |

---

## Overview

**Fragnesia** is a newly disclosed Linux kernel local privilege escalation vulnerability in the **XFRM/ESP and TCP subsystem** (IPSec processing stack). It belongs to the **Dirty Frag vulnerability class** (see ZD-017) but represents a **more dangerous exploitation variant** than the original Dirty Frag.

Unlike Dirty Frag (CVE-2026-43284 + CVE-2026-43500), which required exploiting a **race condition** to achieve the page cache write primitive, Fragnesia abuses a **logic bug** — no race condition, no timing windows, no repeated attempts. Exploitation is **deterministic and reliable**.

Researcher William Bowling of **Zelic** disclosed the flaw alongside a full proof-of-concept exploit that achieves a **memory write primitive** in the kernel, used to corrupt the page cache memory of the `/usr/bin/su` binary to obtain a root shell. The same kernel subsystem vulnerability was described as affecting all Linux kernels released before May 13, 2026.

**Key difference from Dirty Frag:**

| Property | Dirty Frag (ZD-017) | Fragnesia (ZD-027) |
|---|---|---|
| Exploitation type | Race condition | Logic bug (deterministic) |
| Reliability | Moderate — requires timing | **High — no race condition** |
| Kernel subsystem | XFRM/ESP + RxRPC | XFRM/ESP + TCP |
| Patch status | ✅ Patched — ESP + RxRPC both shipped (RxRPC mainline `aa54b1d27fe0`) | ✅ Patched — upstream May 13; distro backports shipped |
| Public PoC | Yes | Yes — full root shell |

---

## Technical Analysis

### Root Cause

Fragnesia exploits a **logic bug** in the interaction between the Linux kernel's **XFRM (IPSec) ESP processing** and **TCP subsystem** path — specifically in how in-place decryption of ESP-encrypted TCP data allows controlled writes to kernel page cache memory.

The bug enables an attacker to obtain a **controlled page cache write primitive**: the ability to write to arbitrary memory pages backing filesystem objects, bypassing normal permissions. By targeting the `/usr/bin/su` binary's page cache, the attacker can overwrite the binary's code pages in memory with attacker-controlled instructions, then execute `su` to trigger the modified code and obtain a root shell.

### Exploitation Path

1. **Attacker achieves local access** (standard user shell, container escape vector, or any unprivileged process)
2. **Trigger logic bug** via crafted ESP-over-TCP packet processing in the kernel
3. **Obtain page cache write primitive** — controlled write to any kernel page cache region
4. **Corrupt `/usr/bin/su` page cache** — overwrite `su` binary's in-memory code pages
5. **Execute `su`** — triggers attacker-controlled code with SUID root privileges
6. **Root shell achieved**

### Why This Is Worse Than Dirty Frag

Dirty Frag (ZD-017) requires a race condition between two kernel code paths — timing-dependent, sometimes requires multiple attempts, and can be influenced by system load. Fragnesia's logic bug is **deterministic**:

- Works reliably on first attempt
- Not affected by system load or timing
- Can be executed from containerized environments (container escape path)
- Does not require any special prerequisites beyond local process execution

### Container Escape Vector

As with Dirty Frag, Fragnesia presents a **container escape path** on Linux hosts running Docker, Kubernetes, or similar container runtimes where the host kernel is shared. A compromised container process exploiting Fragnesia can escape container isolation and achieve root on the host system.

---

## Affected Systems

| System | Status (as of 2026-06-10) |
|---|---|
| All major Linux distros (Debian, Ubuntu, RHEL, AlmaLinux, Rocky, Fedora) | ✅ **PATCHED** — distribution backports shipped; apply kernel update + reboot |
| Linux kernel ≥ May 13, 2026 upstream build | ✅ Patched upstream |
| Cloud VMs running unpatched/unrebooted Linux kernels | ⚠️ **VULNERABLE until updated** — patch is available; treat unpatched estate as urgent |
| Docker/Kubernetes environments (host kernel unpatched) | ⚠️ **VULNERABLE until host kernel patched** + container escape risk |

---

## Relationship to Dirty Frag (ZD-017)

Fragnesia and Dirty Frag are **distinct vulnerabilities** within the same kernel subsystem family:

- **Dirty Frag (ZD-017)**: CVE-2026-43284 (XFRM/ESP) + CVE-2026-43500 (RxRPC); race condition; both components now **patched** — RxRPC fixed in mainline `aa54b1d27fe0` with distro backports shipped (as of 2026-06-10)
- **Fragnesia (ZD-027)**: CVE-2026-46300; XFRM/ESP + TCP; **logic bug** — more reliable; upstream patched May 13, distro backports shipped

The Copy Fail (ZD-014) → Dirty Frag (ZD-017) → Fragnesia (ZD-027) sequence represents an **active vulnerability research campaign** targeting Linux kernel page cache primitives, each disclosure building on the previous.

**As of 2026-06-10 all three (Copy Fail, Dirty Frag, Fragnesia) have shipped distribution backports.** The remaining defender task is rollout: ensure every Linux kernel in the estate is updated and rebooted — patch availability is no longer the gating factor.

---

## Patch / Mitigation

| Priority | Action |
|---|---|
| 🔴 IMMEDIATE | Apply **all available Linux kernel updates** + reboot — distribution backports for all three Dirty Frag class vulnerabilities have shipped (as of 2026-06-10); rollout is the remaining task |
| 🟠 HIGH | Copy Fail (ZD-014) CISA KEV deadline (May 15, 2026) has passed; the same kernel update that closed Copy Fail also addresses Fragnesia for most distributions |
| 🟠 MEDIUM | **Container isolation**: Review container security contexts; ensure containers do not run with CAP_NET_RAW or IPSec-related capabilities that could be leveraged for the XFRM path |
| 🟠 MEDIUM | **Monitor exploit activity**: Alert on `/usr/bin/su` execution from unexpected parent processes or container contexts |
| 🟡 MEDIUM | Apply **Copy Fail mitigations** (already noted in ZD-014/ZD-017): disable CONFIG_XFRM_INTERFACE or restrict IPSec where not required |

---

## A&D / Critical Infrastructure Relevance

Any Linux-based infrastructure — including:

- **Linux servers** in data centers, cloud deployments
- **Containerized workloads** (Docker, Kubernetes clusters)
- **Embedded Linux** in ICS/OT environments
- **Development build servers** where source code access provides exploitation paths

...is potentially vulnerable. The high reliability of Fragnesia (no race condition) makes it a more accessible exploitation target for mid-tier threat actors who lacked the timing expertise to weaponize Dirty Frag.

---

## References

- Cyber Threat Brief May 14, 2026 (YouTube transcript — Bleeping Computer / Zelic sourced)
- William Bowling (Zelic) — vulnerability researcher; PoC disclosed May 13, 2026
- Linux kernel upstream patch — merged May 13, 2026
- Related: ZD-017 (DIRTYFRAG) · ZD-014 (COPYFAIL)
- [AlmaLinux — Fragnesia (CVE-2026-46300) Patches Released](https://almalinux.org/blog/2026-05-13-fragnesia-cve-2026-46300/)
- [Ubuntu Security — CVE-2026-46300](https://ubuntu.com/security/CVE-2026-46300)
- [Red Hat — RHSB-2026-003 Networking subsystem Privilege Escalation (Dirty Frag / Fragnesia)](https://access.redhat.com/security/vulnerabilities/RHSB-2026-003)
- [CloudLinux — Fragnesia Mitigation and Kernel Update](https://blog.cloudlinux.com/fragnesia-mitigation-and-kernel-update)

---

## Intelligence Update — 2026-06-10

### Distro Backports SHIPPED — Status Flipped PARTIAL → PATCHED

The mid-May "upstream patched, distro backports pending" gap has closed. As of 2026-06-10, distribution kernel backports for Fragnesia (CVE-2026-46300) have shipped across every major distribution channel:

- **AlmaLinux** — patched kernels published (built ahead of Red Hat).
- **Ubuntu** — fixed in supported releases per Canonical's security tracker; rebootless livepatches in main/ePortal feeds for Jammy/Noble.
- **Debian** — backports available (Debian 11/12 rebootless feeds noted).
- **RHEL** — addressed under Red Hat bulletin **RHSB-2026-003** (groups CVE-2026-43284 ESP + CVE-2026-46300 Fragnesia for RHEL 8/9/10 + OpenShift); patched kernels in the errata system.
- **CloudLinux / KernelCare** — mitigation + kernel update plus no-reboot livepatches.

Patch *availability* is no longer the gating factor; the remaining defender task is rollout (update kernel + reboot, or apply a livepatch). No CISA KEV listing for CVE-2026-46300 as of this update, and no public reporting attributes exploitation to a named threat actor. The public PoC remains operational against unpatched kernels, so unpatched/unrebooted estates stay urgent.

| Date | Milestone |
|---|---|
| 2026-05-13 | Disclosure; upstream kernel patch merged; AlmaLinux patches released |
| 2026-06-10 | Status confirmed PATCHED — distro backports shipped across AlmaLinux/Ubuntu/Debian/RHEL/CloudLinux; not in CISA KEV; no actor attribution |

*Updated: 2026-06-10 | Author: Archimedes | Admiralty Grade: A2 — distro advisories (AlmaLinux, Canonical, Red Hat RHSB-2026-003, CloudLinux) corroborate shipped backports | TLP: WHITE*

---

*Profile created: 2026-05-14 | Author: C3PO | ZD-029 | Admiralty Grade: A2 | TLP: WHITE*
