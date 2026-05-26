---
brief_id: 2026-05-26-afternoon
brief_type: afternoon
published_at: 2026-05-26T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: applied_to_finding_0007_aviation_targeting_layer_and_finding_0008_ad_indirect_relevance_layer
human_override: null
status: published
run_id: afternoon-20260526-160000
word_count: 712
findings_referenced:
  - finding-2026-05-26-0007-checkpoint-research-unc1549-nimbus-manticore-fast-and-furious-operation-epic-fury-primary-26-ioc
  - finding-2026-05-26-0008-cisa-kev-cve-2026-48172-litespeed-cpanel-plugin-cvss-10-active-exploitation-bod-22-01-t-3
carry_forwards_referenced:
  - cve-2026-9082-drupal-kev-due-date-t-1-wed-2026-05-27
  - cve-2026-42897-exchange-kev-due-date-t-3-fri-2026-05-29
  - cve-2026-48172-litespeed-kev-due-date-t-3-fri-2026-05-29
related_vulns:
  - CVE-2026-48172
  - CVE-2026-9082
  - CVE-2026-42897
related_actors:
  - "004"   # UNC1549 (Nimbus Manticore / Screening Serpens / Smoke Sandstorm)
  - "011"   # Charming Kitten (related via CKR-claimed subgroup framing; preserved as CKR-only single-vendor analytical claim)
related_zero_days: []
related_campaigns:
  - unc1549-nimbus-manticore-2026-active-campaign
  - operation-epic-fury-2026
  - campaign-3-sql-developer-april-2026
  - cve-2026-48172-litespeed-cpanel-plugin-kev-deadline-tracking
tlp: CLEAR
---

# Afternoon Brief — 2026-05-26

**Three federal KEV deadlines now compress within 72 hours: Drupal CVE-2026-9082 tomorrow EOB (T-1), Exchange CVE-2026-42897 Friday (T-3), and LiteSpeed cPanel CVE-2026-48172 Friday (T-3) — the LiteSpeed addition is net-new this afternoon at CISA KEV catalog 2026.05.26.**

**Why it matters:** FCEB and CMMC-partner-flow estates carry a Wed-Fri patch compression. The new LiteSpeed entry (CVSS 10.0, authenticated-cPanel-user-to-root, active exploitation per LiteSpeed observation) does NOT route to A&D primes directly — primes do not run cPanel — but Tier-2/Tier-3 supplier hosting and contractor-portal microsites are the load-bearing exposure layer.

---

## 🚨 Active Threats

**CVE-2026-48172 (LiteSpeed User-End cPanel Plugin) — CISA KEV addition today; CVSS 10.0; federal deadline Friday 2026-05-29 (T-3). UPDATE on 2026-05-23 0600 FLASH lineage: KEV listing now adds federal procedural validation to vendor's exploitation observation.**
- What: CISA KEV catalog version 2026.05.26 (published 2026-05-26 13:02 EDT) adds CVE-2026-48172 with `dueDate` 2026-05-29 under BOD 22-01. Affected: LiteSpeed User-End cPanel Plugin v2.3–v2.4.4 (incorrect privilege assignment, CWE-269 family, in `lsws.redisAble`). Outcome: an authenticated cPanel user of any privilege level executes scripts as root via a single malformed API call with `cpanel_jsonapi_func=redisAble`. Patched in v2.4.7 + WHM v5.3.1.0. Discoverer: David Strydom (independent).
- Why it matters for A&D — layered per red-team review:
  - **Prime-direct cPanel exposure: very_unlikely** — primes use enterprise procurement and CMS platforms (SAP Ariba, Coupa, Sitecore, Adobe Experience Manager), not cPanel shared hosting.
  - **Tier-2/Tier-3 supplier cPanel exposure: likely** — cPanel/WHM dominates SMB shared-hosting markets; many small A&D suppliers (specialty parts, materials, niche services with 1–5 IT staff) operate cPanel-managed estates.
  - **Supply-chain pivot from a Tier-3 cPanel compromise to prime-relevant data: roughly_even_chance** — conditional on supplier IT topology (co-located web+mail+CRM raises pivot likelihood; enterprise-email-decoupled-from-marketing-site lowers it).
- Action: Verify CMMC partner-flow supplier-attestation channel covers KEV-listed CVSS 10.0 vulnerabilities by 2026-05-29. Vendor mitigation if patch is deferred: `/usr/local/lsws/admin/misc/lscmctl cpanelplugin --uninstall`. Vendor detection grep: `grep -rE "cpanel_jsonapi_func=redisAble" /var/cpanel/logs /usr/local/cpanel/logs/`.
- Source: [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [LiteSpeed advisory](https://blog.litespeedtech.com/2026/05/21/security-update-litespeed-cpanel-plugin/) · Digraph: A2 · WEP: very_likely (procedural CVE facts, KEV deadline); likely (active exploitation continuing through deadline; single effective evidence basis on exploitation). Hard Rule 2: no actor attributed by any source. UPDATE on coverage log entry [2026-05-23-flash-0600-002](flash-2026-05-23-0600-002-litespeed-cpanel-cve-2026-48172.md) — resurface trigger `cisa_kev_addition` met.

**[UNC1549](../threat-actors/UNC1549/profile.md) / Nimbus Manticore — Check Point Research primary now in corpus directly; 26 SHA256 + 26 domain IOC drop, MiniFast 16-opcode capability matrix, AppDomain hijacking specifics, Zoom scheduled-task hijack, SSL.com certificate abuse. SIBLING to this morning's THN-relay finding-0001.**
- What: Check Point Research primary "Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict" (2026-05-22) surfaces in corpus directly via [SecurityWeek](https://www.securityweek.com/iranian-apt-targets-aviation-software-companies-with-updated-tools/) (Ionut Arghire, today) and [Industrial Cyber](https://industrialcyber.co/threats-attacks/irgc-linked-nimbus-manticore-group-attacks-defense-aerospace-telecom-sectors-using-minifast-malware-toolkit/) (Anna Ribeiro, today). CKR + Palo Alto Unit 42 published concurrently 2026-05-22 on overlapping cluster mappings (CKR's "Nimbus Manticore" vs Unit 42's "Screening Serpens / Smoke Sandstorm"). Net-new corpus material: **26 SHA256 hashes + 26 domains** (including the 21 `azurewebsites[.]net` staging family); **MiniFast 16-opcode command matrix** (T1083 directory enum, T1059.003 cmd exec, T1490 inhibit recovery, T1548.002 runas UAC bypass, plus 12 more opcodes); **AppDomain hijacking via trojanized XML `.config` files** pointing to AppDomainManager classes (MITRE T1574.014); **Zoom scheduled-task hijack** via `ZoomUpdateTaskUser-<SID>` and the persistence task name `WindowsSecurityUpdate` (T1053.005); **SSL.com code-signing certificate abuse** with two distinct subjects (Gray Matter Software S.R.L., Kirubel Kerie Negeya).
- Why it matters for A&D — layered per red-team review:
  - **CKR-said-it (verbatim): aviation explicit targeting with US-domestic-airline impersonation lures — very_likely.** CKR primary names "defense, aviation and telecommunication" sectors; airline lures are concrete.
  - **A&D-prime employee exposure inference via airline-themed lures: roughly_even_chance** — analyst KAC A4 test-deferred (specific airline-adjacent employee segmentation not achievable from publicly available corpus).
  - **CKR-only analytical claims (single-source veto applied): likely, NOT very_likely** — "Operation Epic Fury" campaign-naming tied to a US military operation Feb 28 2026; Nimbus Manticore as a **subgroup of [Charming Kitten](../threat-actors/Charming-Kitten/profile.md) (APT35)** (novel-to-corpus relation; Unit 42's concurrent publication does NOT adopt the subgroup framing); Bohrium + TA455 alias additions to the UNC1549 set.
- Relay drift flag: Industrial Cyber editorializes CKR's "aviation" framing to "aerospace, aviation, telecom." CKR primary text does NOT use "aerospace." For A&D-prime audiences the commercial-aviation vs aerospace-manufacturer distinction is material; Archimedes propagates CKR's "aviation" framing.
- Source: [Check Point Research primary](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/) · Digraph: A2 · WEP: very_likely (corroborated tradecraft via CKR + Unit 42); likely (three CKR-only analytical claims). Attribution corpus-baseline per [actor #004 dossier](../threat-actors/UNC1549/profile.md), not originated. SIBLING to [morning brief item 1](2026-05-26-morning.md) (finding-0001 anchored on THN relay); 0007 upgrades the corpus treatment from B2 (relay) to A2 (originating primary) on the same surface.

## 🔓 Vulnerabilities

**KEV deadline tracker (Wed–Fri compression):**
- **CVE-2026-9082 (Drupal Core SQLi, PostgreSQL) — T-1, Wednesday 2026-05-27 EOB.** Substance not re-litigated; see [morning brief](2026-05-26-morning.md). Imperva attacker-side telemetry (~50% Gaming + Financial Services, NOT A&D-shaped) and Shadowserver internet-scale census (670 unpatched as of 2026-05-25) carry forward. Digraph: A1.
- **CVE-2026-42897 (Exchange OWA XSS) — T-3, Friday 2026-05-29.** Substance not re-litigated; mitigation path remains ESU-only + EEMS/EOMT per [VT-008](../vulnerabilities/Exchange-CVE-2026-42897/profile.md). Digraph: A1.
- **CVE-2026-48172 (LiteSpeed cPanel) — T-3, Friday 2026-05-29.** Net-new this afternoon; see Active Threats above. Digraph: A2.

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific cyber threats against watchlist companies in the PM reporting window. The UNC1549 / Nimbus Manticore CKR-primary surface above names **aviation** (commercial), not aerospace (manufacturers); no A&D prime named compromised. Tracked actors with historical A&D targeting: [APT28](../threat-actors/APT28/profile.md), [UNC1549](../threat-actors/UNC1549/profile.md), Lazarus, APT41, Salt Typhoon.

## 🕵️ Actor Activity

UNC1549 / Nimbus Manticore CKR-primary upgrade covered above in **Active Threats**. No other tracked-actor PM-window activity.

## 🇮🇷 Iran Cyber Watch

UNC1549 / Nimbus Manticore CKR-primary upgrade covered above in **Active Threats** — see actor [#004 dossier](../threat-actors/UNC1549/profile.md). CKR claims Nimbus Manticore is a subgroup of [Charming Kitten](../threat-actors/Charming-Kitten/profile.md) (APT35); single-vendor analytical framing pending corroboration — flagged for actor-profiler review on whether to integrate the relation into `_roster.yaml`. No new activity from Handala Hack or [MuddyWater](../threat-actors/MuddyWater/profile.md) in the last 48h.

## 📰 Other Signal

**First-party Splunk:** Zero `defenseclaw_local` events across CVE-2026-48172 / LiteSpeed / `lsws.redisAble` / cPanel / `redisAble`, plus the UNC1549 / MiniFast / MiniJunk / Nimbus Manticore / `getsqldeveloper` / AppDomain / Smoke Sandstorm / Bohrium / TA455 / Charming Kitten / APT35 keyword sets, in an 8h PM sweep. **62nd consecutive dormant non-self sweep.** Per Hard Rule 8, silence is neither confirming nor disconfirming. Note: A&D-prime estates do not typically run cPanel inside program-data enclaves, so `defenseclaw_local` silence on those strings is expected.

---

*Sources hyperlinked inline. Digraph per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-05-26. **Three federal KEV deadlines now compress Wed–Fri: Drupal tomorrow EOB, Exchange Friday, LiteSpeed cPanel newly added today, also Friday.**

🚨 **Active Threats**

• **[CISA KEV adds LiteSpeed cPanel CVE-2026-48172 — federal due Fri May 29](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — CVSS 10.0; authenticated cPanel user runs scripts as root via `lsws.redisAble`. Patched v2.4.7 + WHM v5.3.1.0. **Primes don't run cPanel directly**; Tier-2/Tier-3 supplier hosting and contractor microsites are the exposure layer. *Verify CMMC partner-flow attestation covers KEV CVSS-10 by Friday.* No actor attributed.

• **[UNC1549 / Nimbus Manticore — Check Point primary now in corpus; 26 hashes + 26 domains drop](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/)** — Direct upgrade of this morning's THN-relay item. MiniFast 16-opcode matrix, AppDomain hijacking via trojanized `.config` files, Zoom `ZoomUpdateTaskUser-<SID>` task hijack, SSL.com cert abuse (Gray Matter Software, Kirubel Kerie Negeya). **CKR names "aviation" (commercial); Industrial Cyber relay drifts to "aerospace" — not in primary.** CKR's Nimbus-Manticore-as-subgroup-of-Charming-Kitten framing is single-vendor; *Archimedes does not endorse the relation.*

🔓 **Vulnerabilities**

• **KEV deadline tracker:** Drupal **CVE-2026-9082** Wed May 27 EOB · Exchange **CVE-2026-42897** Fri May 29 · LiteSpeed **CVE-2026-48172** Fri May 29. Substance on Drupal and Exchange carries from morning brief; LiteSpeed is net-new.

📰 **Other Signal**

• **First-party Splunk:** zero `defenseclaw_local` hits on LiteSpeed/cPanel + UNC1549 keyword sets. **62nd consecutive dormant non-self sweep.** *Expected state given A&D-prime estates do not run cPanel.*
