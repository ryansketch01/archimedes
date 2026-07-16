---
brief_id: 2026-07-16-afternoon
brief_type: afternoon
published_at: 2026-07-16T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: null
human_override: null
word_count: 748
findings_referenced: [finding-2026-07-16-0005, finding-2026-07-16-0003, finding-2026-07-16-0004]
tlp: CLEAR
---

# Afternoon Brief — 2026-07-16

**CISA KEV-listed three CVEs today — led by CVE-2026-58644, the unauthenticated on-prem SharePoint RCE Archimedes tracks as VT-041, which flipped from patched-not-exploited to actively exploited. All three are due Saturday, July 19.**

**Why it matters:** On-prem SharePoint (2016/2019/SE) is pervasive across DIB document-collaboration tiers — a patch-coverage priority for A&D, landing a day after the Oracle EBS deadline.

---

## 🚨 Active Threats

**UPDATE: SharePoint unauth RCE CVE-2026-58644 (VT-041) is now actively exploited**
- What: CISA KEV-listed CVE-2026-58644 today — a CVSS 9.8 unauthenticated deserialization RCE (CWE-502) in on-prem SharePoint Server 2016/2019/SE. Federal remediation due Saturday, July 19 (accelerated BOD 26-04 window).
- Why it matters for A&D: Patch-priority relevance driven by on-prem SharePoint's DIB ubiquity — not a broad external attack surface. Unauthenticated network RCE requires reachability, and many A&D SharePoint front-ends are internal, VPN-gated, or air-gapped. No first-party Splunk exposure data this sweep; SharePoint Online / M365 not affected.
- Action: Inventory on-prem SharePoint farms; confirm the CVE-2026-58644 patch is applied before Saturday.
- Source: [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A2 · WEP: likely (single-source veto — CISA's KEV determination is the sole exploitation basis)
- Related: [VT-041 / CVE-2026-58644](../vulnerabilities/CVE-2026-58644/profile.md)

🔗 **Update on:** 2026-07-15 afternoon SharePoint cluster — VT-041 was a priority escalation-watch (patched, not exploited); it is the unauthenticated sibling of the already-exploited [VT-038 (CVE-2026-45659)](../vulnerabilities/CVE-2026-45659/profile.md) and has now moved to exploited + KEV.

**UPDATE: Two FortiSandbox command-injection CVEs added to KEV**
- What: CISA also KEV-listed CVE-2026-25089 and CVE-2026-39808 — OS command-injection flaws in Fortinet FortiSandbox — both due Saturday, July 19.
- Why it matters for A&D: FortiSandbox is an edge/security-appliance-tier device; command injection on a detonation appliance is a perimeter-integrity concern for DIB shops running Fortinet.
- Action: Patch FortiSandbox to Fortinet's fixed builds before Saturday.
- Source: [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A2 · WEP: likely (single-source veto)
- Related: [VT-045 / CVE-2026-25089](../vulnerabilities/CVE-2026-25089/profile.md), [VT-046 / CVE-2026-39808](../vulnerabilities/CVE-2026-39808/profile.md) (net-new to the vuln corpus this cycle)

🔗 **Update on:** 2026-06-16 morning — the FortiSandbox active-exploitation cluster (then B2); the KEV listing assessed likely within 24-72h has now landed.

## 🔓 Vulnerabilities

Standing watch — carry-forward from this morning, no new development:
- **[Oracle EBS CVE-2026-46817 (VT-043)](../vulnerabilities/CVE-2026-46817/profile.md):** federal KEV deadline Saturday, July 18 — a day ahead of the SharePoint/FortiSandbox batch. Actively-exploited unauthenticated Payments takeover, CVSS 9.8, EBS 12.2. Digraph: A2.
- **[LegacyHive Windows profsvc LPE (VT-042)](../vulnerabilities/LegacyHive/profile.md):** unchanged since this morning — still no CVE, unpatched, no in-the-wild use. Digraph: B2.

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in the reporting window. The KEV items above carry structural DIB relevance only — no named A&D victim. Tracked actors with historical A&D targeting: APT28, UNC1549, Lazarus, APT41, Salt Typhoon.

## 🕵️ Actor Activity

**Sandworm shifts to ClickFix delivery against Ukrainian targets**
- What: CERT-UA reports Sandworm (#007, GRU Unit 74455) now uses a ClickFix chain — a fake CAPTCHA prompts the victim to paste a PowerShell command — to deploy new tooling (GhettoVibe, ScoutCurl, FluidLeech, LoadLoop).
- Why it matters for A&D: Limited. Targeting is primarily Ukrainian — no A&D, DIB, or government nexus. ClickFix is a commodity technique; Sandworm is adopting a common method in its home theater, not fielding a new capability class.
- Source: [CERT-UA via The Record](https://therecord.media/ukraine-sandworm-hacks-captcha-powershell) · Digraph: A2 · WEP: likely (single-source veto — CERT-UA is the sole upstream)
- Related: [Sandworm #007](../threat-actors/Sandworm/). No atomic IOCs in the relay.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h.

## 📰 Other Signal

**Two Scattered Spider members sentenced for the 2024 TfL attack** — A UK court sentenced Thalha Jubair and Owen Flowers to 5.5 years each for the August 2024 Transport for London breach after guilty pleas; the US DOJ brought parallel charges spanning ~120 breaches. Retrospective, no new TTP. Scattered Spider's help-desk/SIM-swap social engineering and Okta/M365 identity abuse remain relevant to the A&D identity attack surface. Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/scattered-spider-members-behind-transport-for-london-hack-get-five-years-in-prison/) · Digraph: B1 · Related: [Scattered Spider #013](../threat-actors/Scattered-Spider/).

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-07-16.

🚨 **Active Threats**

• **[SharePoint unauth RCE (CVE-2026-58644) is now actively exploited](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — CISA KEV-listed the CVSS 9.8 unauthenticated on-prem SharePoint RCE today. Federal deadline **Saturday, July 19**. On-prem 2016/2019/SE only, not M365. DIB SharePoint owners: confirm the patch is applied *before Saturday* — a patch-coverage priority, not proof of broad exposure.

• **[Two FortiSandbox command-injection CVEs added to KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — CVE-2026-25089 and CVE-2026-39808, both due **Saturday, July 19**. The listing we called likely on June 16 has landed. Fortinet shops: patch FortiSandbox before the weekend.

🔓 **Vulnerabilities**

• **Oracle EBS CVE-2026-46817 (VT-043):** federal KEV deadline **Saturday, July 18** — a day before the SharePoint/FortiSandbox batch. Actively-exploited Payments takeover; *patch now* if you run EBS 12.2.

🕵️ **Actor Activity**

• **[Sandworm shifts to ClickFix delivery in Ukraine](https://therecord.media/ukraine-sandworm-hacks-captcha-powershell)** — CERT-UA reports fake-CAPTCHA PowerShell paste attacks dropping new tooling. Primarily Ukrainian targeting, no A&D nexus; commodity technique, not a new capability.

📰 **Other Signal**

• **[Two Scattered Spider members sentenced for the 2024 TfL attack](https://www.bleepingcomputer.com/news/security/scattered-spider-members-behind-transport-for-london-hack-get-five-years-in-prison/)** — 5.5 years each in the UK after guilty pleas; parallel US DOJ charges. Their help-desk/SIM-swap and Okta/M365 identity tradecraft still maps to A&D.
