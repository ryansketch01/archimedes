---
brief_id: 2026-06-01-afternoon
brief_type: afternoon
published_at: 2026-06-01T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_required
human_override: null
status: published
run_id: afternoon-20260601-160000
word_count: 783
findings_referenced:
  - finding-2026-06-01-0002
  - finding-2026-06-01-0003
  - finding-2026-06-01-0004
  - finding-2026-06-01-0005
related_vulns:
  - CVE-2026-41089   # Windows Netlogon — ITW state transition (UPDATE on 2026-05-12-pm-004 Patch Tuesday cluster)
  - CVE-2026-0826    # HP Poly VVX/Trio coordinated zero-day, unauth RCE
  - CVE-2024-21182   # Oracle WebLogic — CISA KEV add, 3-day FCEB deadline
  - CVE-2026-0257    # PAN-OS GlobalProtect — KEV deadline EOD today (status carry from morning)
related_actors: []
related_zero_days: []
related_campaigns:
  - miasma-mini-shai-hulud-2026-06-01
update_on:
  - finding-2026-05-12-0003   # CVE-2026-41089 Netlogon — Patch Tuesday cluster, now ITW per CCB
  - finding-2026-05-29-0004   # PAN-OS — deadline-day status tick only
tlp: CLEAR
discord_delivery:
  channel: intel-briefs
  message_ids:
    - "1511108544345411694"
  parts: 1
  delivered_at: 2026-06-01T16:05:00-04:00
  via: librarian
  late: false
---

# Afternoon Brief — 2026-06-01

**Four federally-relevant items land in one window — CVE-2026-41089 (Windows Netlogon) crosses to in-the-wild per Belgian CCB, CISA adds CVE-2024-21182 (Oracle WebLogic) to KEV with a 3-day FCEB due date, HP Poly VVX/Trio phones ship a coordinated unauth-RCE zero-day (CVE-2026-0826) patched today per Rapid7, and a new Shai-Hulud-family npm wave hits `@redhat-cloud-services/*` packages per Socket.**

**Why it matters:** Four discrete defender actions this afternoon. Netlogon escalation in the DA-tier demands patch confirmation. WebLogic and HP Poly add patch-cycle work. The npm wave is a dependency-manifest grep.

---

## 🚨 Active Threats

**UPDATE — CVE-2026-41089 Windows Netlogon: ITW state transition** *(material update on [2026-05-12 Patch Tuesday cluster](2026-05-12-afternoon.md) / finding-2026-06-01-0002)*

- **What.** Belgium's [CCB](https://ccb.belgium.be/en) issued an advisory observing Netlogon-vector exploitation against unpatched Windows domain controllers; [BleepingComputer](https://www.bleepingcomputer.com/) and [SecurityWeek](https://www.securityweek.com/) re-report. CCB names no actor; Archimedes does not originate attribution.
- **Analyst note.** Leading ACH hypothesis is authenticated-to-DA escalation (H2), not cold-start cross-domain pre-auth compromise (H1). Both drive the same defender action — DCs are the operator-of-last-resort tier in every Windows estate.
- **A&D action.** Confirm the May 2026 Patch Tuesday rollup is deployed on every DC and Netlogon-participating member server today.
- Digraph **B2** (single-source-veto: CCB primary, two re-reporters) · WEP **likely** on the ITW characterization · finding-2026-06-01-0002.

**Miasma — Mini Shai-Hulud npm wave hits `@redhat-cloud-services/*`** *([finding-2026-06-01-0004](finding-2026-06-01-0004.md))*

- **What.** [Socket](https://socket.dev/blog) reports a Shai-Hulud-family npm compromise affecting `@redhat-cloud-services/*` packages, naming the wave **Miasma**; [THN](https://thehackernews.com/) relays. Novel tradecraft: C2 impersonating the Anthropic API endpoint. DIB CI/CD pulling `@redhat-cloud-services/*` directly or transitively needs a manifest sweep.
- **Analyst note (Hard Rule 2).** Socket references TeamPCP tooling-lineage; analyst ACH places three hypotheses tied at rank 1 (tooling-leaked-and-reused / heterogeneous-opportunistic / composite-affiliate) with TeamPCP-direct LAST. **Archimedes does not extend Miasma operator attribution to TeamPCP.** Defender action is mechanism-class.
- **A&D action.** `grep -r '@redhat-cloud-services/' package*.json` across CI/CD repos; if hit, pin to last-known-good and rotate pipeline secrets touching affected versions. Anthropic-API-impersonation C2 may be campaign-specific — do not anchor long-term detection on this IOC alone.
- Digraph **B2** · WEP **likely** · finding-2026-06-01-0004.

## 🔓 Vulnerabilities

**CVE-2026-0826 — HP Poly VVX / Trio coordinated unauthenticated RCE zero-day; patched today** *([finding-2026-06-01-0003](finding-2026-06-01-0003.md))*

- **What.** [Rapid7](https://www.rapid7.com/blog/) discloses a 5-month coordinated zero-day in HP Poly VVX/Trio desk phones — unauth RCE reachable when ICE (Interactive Connectivity Establishment) is enabled. Vendor patch + Metasploit ship concurrent. No ITW. Voice-tier endpoints inside DIB sites are typically out of EDR scope but on the same VLAN as engineering workstations.
- **Analyst note.** ICE factory default is OFF — treat as a **pre-condition to verify**, not inherited risk reduction. Provisioning templates, Teams Direct Routing, CUCM integrations, and MSP golden-images may enable ICE regardless.
- **A&D action.** Inventory firmware; patch to vendor-fixed builds. Verify ICE state in **provisioning templates** — operational state, not factory state, is what matters.
- Digraph **A2** · WEP **likely** · finding-2026-06-01-0003.

**UPDATE — CVE-2024-21182 Oracle WebLogic: CISA KEV addition, FCEB due 2026-06-04** *([finding-2026-06-01-0005](finding-2026-06-01-0005.md))*

- **What.** [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) adds CVE-2024-21182 (Oracle WebLogic, T3/IIOP unauthenticated take-over) with a 3-day FCEB due of **2026-06-04**. DFARS 252.204-7012 and CMMC 2.0 do **not** mandate inheriting KEV deadlines — treat as an **elevated-urgency signal per organization-specific governance**. T3/IIOP exposure concentrates in legacy / shadow-IT / acquisition-inherited residual WebLogic.
- **A&D action.** Inventory WebLogic including acquisition-inherited assets; confirm T3/IIOP is not public-internet-exposed; patch where exposure exists.
- **Pattern note.** Two consecutive 3-day FCEB deadlines within ~96h (PAN-OS today; WebLogic Thursday). May be coincidence, cadence recalibration, or campaign signal. **Archimedes notes the pattern; does not assert cause.**
- Digraph **A2** operational / **A1** procedural · WEP **likely** · finding-2026-06-01-0005.

**Carry-forward — CVE-2026-0257 PAN-OS GlobalProtect:** KEV federal deadline closes EOD tonight. No new substance this window. See [today's morning brief](2026-06-01-morning.md) for the operational package.

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in window. Tracked A&D actors: APT28, [UNC1549](threats/threat-actors/004-unc1549/profile.md), Lazarus, APT41, Salt Typhoon. Today's four items all carry structural DIB exposure rather than named-prime targeting: Netlogon (universal Windows estate), HP Poly (VLAN-adjacent voice tier), `@redhat-cloud-services/*` (DIB CI/CD), WebLogic (acquisition-inherited middleware).

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors ([UNC1549 #004](threats/threat-actors/004-unc1549/profile.md), [Charming Kitten #011](threats/threat-actors/011-charming-kitten/profile.md), Handala Hack #014, MuddyWater #022) in the last 48h.

## 📰 Other Signal

**Two-deadline-in-96h FCEB pattern (PAN-OS today, WebLogic Thursday)** flagged for weekly-synthesis attention. CCB's Netlogon advisory is a separate procedural datapoint — a national CERT escalating ITW characterization ahead of US-side Tier-1 IR firm corroboration.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-01.

🚨 **Active Threats**

- **[CVE-2026-41089 Netlogon — ITW per Belgian CCB](https://ccb.belgium.be/en)** — CCB observed Netlogon-vector exploitation against unpatched DCs Monday; BleepingComputer and SecurityWeek re-report. Leading hypothesis is authenticated-to-DA escalation, not cold-start cross-domain — both drive the same action. No attribution. *Confirm the May Patch Tuesday rollup is on every DC today.*
- **[Miasma — Shai-Hulud npm wave hits @redhat-cloud-services](https://socket.dev/blog)** — Socket names the wave Monday; novel Anthropic-API-impersonation C2. Tooling-lineage may trace to TeamPCP per Socket; *Archimedes does not extend operator attribution.* *DIB CI/CD: grep manifests for @redhat-cloud-services, pin last-known-good, rotate touched pipeline secrets.*

🔓 **Vulnerabilities**

- **[CVE-2026-0826 HP Poly VVX/Trio unauth RCE zero-day — patched today](https://www.rapid7.com/blog/)** — Rapid7 ships a 5-month coordinated disclosure; RCE reachable when ICE is enabled; Metasploit concurrent. ICE factory default is OFF but provisioning templates / Teams Direct Routing / CUCM / MSP golden-images may enable it. *Verify ICE in provisioning templates, not just device-level.*
- **[CVE-2024-21182 Oracle WebLogic — CISA KEV, FCEB due Thursday June 4](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — DFARS / CMMC do not mandate KEV inheritance; treat as elevated-urgency signal. T3/IIOP exposure concentrates in legacy / shadow-IT / acquisition-inherited WebLogic. *Inventory including acquisitions; confirm T3/IIOP not public-exposed.*
- **CVE-2026-0257 PAN-OS** carry-forward — KEV federal deadline closes EOD tonight; no new substance.
