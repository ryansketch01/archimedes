# PTC Windchill / FlexPLM Zero-Day — Unauthenticated RCE via Java Deserialization (CVSS 10.0)

## Identity

| Field | Details |
|---|---|
| **CVE** | **CVE-2026-4681** (assigned since original profile; was "None assigned") — re-verified 2026-06-10 |
| **Vendor Advisory** | [PTC Trust Center advisory](https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-critical-vulnerability) · [CISA ICSA-26-085-03](https://www.cisa.gov/news-events/ics-advisories/icsa-26-085-03) · BSI (Germany) — co-warned |
| **Type** | Unauthenticated Remote Code Execution / Java Deserialization |
| **Class** | CWE-502 — Deserialization of Untrusted Data |
| **Affected Products** | Windchill PDMLink 11.0 M030 → 13.1.3.0 · FlexPLM 11.0 M030 → 13.0.3.0 (per CVE-2026-4681 advisory; customer-managed deployments with internet-accessible servlets) |
| **Not Affected** | Cloud-hosted / PTC-managed instances with properly restricted servlet access |
| **Patch Status** | 🟠 **PATCHES ROLLING OUT** (re-verified 2026-06-10) — PTC is "actively developing and releasing security patches for all supported Windchill versions." Per-version fixed builds not fully enumerated in public sources; apply the vendor Apache/IIS servlet-block workaround immediately while sourcing the version-specific patch from PTC. No longer a strict zero-day (was "UNPATCHED, no patch available") |
| **CVSS** | **10.0 (Maximum)** — CVSS v3.1 (PTC CNA; confirmed via Kudelski / BleepingComputer) |
| **Exploit Maturity** | 🟠 **IMMINENT-THREAT / NO CONFIRMED ITW** (corrected 2026-06-10) — PTC cites "credible evidence of an imminent threat by a third-party group"; German BKA mobilized agents. PTC/CISA report NO confirmed customer exploitation as of current reporting. The original profile's "ATTACKED — IoCs confirmed (web shell uploads)" overstated this: vendor publishes web-shell IoCs (GW.class, payload.bin, dpr_*.jsp) as hunting guidance, not as confirmed in-the-wild compromise |
| **CISA KEV** | Not listed (re-verified 2026-06-10) — consistent with no CISA-confirmed active exploitation |
| **Disclosed** | ~2026-03-26 (CVE-2026-4681 advisory; CISA ICSA-26-085-03). Original Archimedes profile (2026-05-20) predated awareness of the CVE assignment but describes the same flaw (identical WindchillGW/WindchillAuthGW servlet paths, deserialization, Apache LocationMatch workaround, CVSS 10.0) |
| **Threat Level** | 🔴 CRITICAL — CVSS 10.0; actively exploited; no patch; ubiquitous in aerospace & defense PLM/PDM; unauthenticated internet-facing RCE |
| **Admiralty Grade** | A2 — Vendor (PTC) + CISA/BSI confirmation; CVE assigned; IoCs published as hunting guidance |
| **ATT&CK** | T1190 (Exploit Public-Facing Application) · T1505.003 (Web Shell) · T1059 (Command and Scripting Interpreter) · T1083 (File and Directory Discovery) |

---

## Overview

PTC Windchill and FlexPLM contain an unauthenticated remote code execution zero-day via Java deserialization in two Apache servlet endpoints. The vulnerability carries a vendor-assigned CVSS score of **10.0** — the maximum — and has already been exploited in the wild, with IoCs including post-exploitation web shell uploads documented by PTC's service partner EAC.

**Why this matters for aerospace & defense:** Windchill is the dominant Product Lifecycle Management (PLM) and Product Data Management (PDM) platform across the defense industrial base. It holds technical drawings, engineering models, BOM data, program schedules, and configuration management records for weapon systems, aircraft, ships, and other defense programs. Compromise of a Windchill instance = access to controlled technical data and program-sensitive information.

FlexPLM serves the same function for footwear and apparel supply chains but is co-deployed in multi-program contractor environments.

---

## Technical Analysis

### Vulnerable Endpoints

```
/servlet/WindchillGW/com.ptc.wvs.server.publish.Publish
/servlet/WindchillAuthGW/com.ptc.wvs.server.publish.Publish
```

Both endpoints accept and deserialize Java objects without authentication checks on the deserialization path. A crafted request can trigger arbitrary code execution with the privileges of the Windchill application server process.

### Post-Exploitation Indicators (vendor hunting guidance — not confirmed ITW)

- Web-shell artifacts published as IoCs to hunt for: `GW.class`, `payload.bin`, `dpr_*.jsp` on the Windchill filesystem; suspicious requests to the vulnerable servlet paths
- Likely follow-on if exploited: credential harvesting, lateral movement into connected engineering systems, exfiltration of technical documents
- **Correction (2026-06-10):** PTC and CISA report no confirmed customer exploitation; these are pre-emptive IoCs given the "imminent threat" warning, not evidence of in-the-wild compromise

---

## Workaround (Apply Immediately)

Block the vulnerable servlet paths in Apache:

1. Create `/etc/apache2/conf.d/90-app-Windchill-Auth.conf` (or highest-numbered file in conf.d):

```apache
<LocationMatch "^.*servlet/(WindchillGW|WindchillAuthGW)/com\.ptc\.wvs\.server\.publish\.Publish(?:;[^/]*)?/.*$">
    Require all denied
</LocationMatch>
```

2. Restart Apache

**If a file with prefix 90- or higher already exists, use a higher number to ensure this rule loads last.**

---

## A&D Relevance

Windchill is deployed at virtually every major U.S. and allied defense prime contractor (Lockheed Martin, Raytheon, Boeing, Northrop Grumman, General Dynamics, BAE Systems, and hundreds of tier-2/3 suppliers). A successful exploit chain against an internet-exposed Windchill instance provides access to:
- ITAR/EAR-controlled technical data
- Program schedules and SOW details
- Engineering designs and specifications
- Personnel and organizational structure via system metadata

This is a tier-1 espionage target for nation-state actors (China-nexus in particular given known PTC targeting history).

---

*Added: 2026-05-20 | Apply Apache/IIS workaround immediately | Monitor PTC for version-specific patch*

---

## Intelligence Update — 2026-06-10

### CVE assigned (CVE-2026-4681), patches rolling out, exploitation claim corrected — A&D priority remains maximum

Patch-status re-verification against the PTC Trust Center advisory, CISA ICSA-26-085-03, BleepingComputer, Kudelski Security, and SecurityWeek. Three material changes from the original 2026-05-20 zero-day profile:

1. **CVE assigned.** The flaw now carries **CVE-2026-4681** (CVSS v3.1 10.0). The original "None assigned" status is superseded. This is the same vulnerability — identical `WindchillGW`/`WindchillAuthGW` deserialization servlet paths, identical Apache `LocationMatch` workaround, identical vendor-assigned 10.0 — Archimedes simply tracked it before the CVE-assignment reporting surfaced. Affected scope is now precisely bounded: Windchill PDMLink 11.0 M030 → 13.1.3.0 and FlexPLM 11.0 M030 → 13.0.3.0.

2. **Patches are rolling out.** PTC states it is "actively developing and releasing security patches for all supported Windchill versions." Per-version fixed builds are not fully enumerated in the public sources reviewed, so the status moves from "UNPATCHED / no patch available" to **patches-rolling-out** — the version-specific fix must be sourced directly from PTC per deployment. The Apache/IIS servlet-block workaround remains the correct interim control and is still vendor-recommended for any instance not yet on a fixed build.

3. **Exploitation claim corrected (Hard Rule discipline).** The original profile asserted "ATTACKED — IoCs confirmed (web shell uploads post-exploitation)." Current PTC and CISA reporting states there is **no confirmed customer exploitation**, only "credible evidence of an imminent threat by a third-party group" (severe enough that German federal police mobilized to warn companies). The web-shell IoCs (`GW.class`, `payload.bin`, `dpr_*.jsp`) are vendor-published hunting guidance, not confirmed in-the-wild compromise. CVE-2026-4681 is **not on CISA KEV** as of 2026-06-10 — consistent with the "no confirmed exploitation" picture. First-party Splunk carries no Windchill exploitation telemetry in scope (silent ≠ disconfirming, Hard Rule 8).

**A&D bottom line unchanged:** Windchill is the dominant PLM/PDM platform across the defense industrial base, holding ITAR/EAR-controlled technical data. The combination of unauthenticated internet-facing RCE, CVSS 10.0, a named imminent-threat actor group, and BKA-level government concern keeps this at maximum remediation priority for any internet-exposed customer-managed instance — patch to the PTC-provided fixed build for your version, or apply the servlet block and remove internet exposure until you can.

| Date | Milestone |
|---|---|
| ~2026-03-26 | CVE-2026-4681 advisory; CISA ICSA-26-085-03; BSI co-warning; Apache/IIS workaround published |
| 2026-05-20 | Archimedes profile created (pre-CVE-assignment awareness) |
| 2026-06-10 | Re-verified: CVE assigned, patches rolling out for supported versions, no confirmed ITW exploitation, not on CISA KEV; exploitation overclaim corrected |

*Updated: 2026-06-10 | Author: Archimedes (vuln-tracker) | Admiralty Grade: A2 — PTC + CISA/BSI confirmation | TLP: CLEAR*
