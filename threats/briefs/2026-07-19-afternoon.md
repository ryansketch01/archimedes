---
brief_id: 2026-07-19-afternoon
brief_type: afternoon
published_at: 2026-07-19T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: null
human_override: null
word_count: 615
findings_referenced: [finding-2026-07-16-0005, finding-2026-07-15-flash-1800-0001, finding-2026-07-18-0001]
tlp: CLEAR
discord_delivery:
  channel: intel-briefs
  message_ids: ["1528493563011399881"]
  parts: 1
  delivered_at: 2026-07-19T16:07:56-04:00
  late: false
  via: librarian
---

# Afternoon Brief — 2026-07-19

**The weekend's KEV deadline board is now fully closed and quiet** — SharePoint on-prem CVE-2026-58644 and the two FortiSandbox command-injection flaws (CVE-2026-25089 / CVE-2026-39808) reached their federal remediation deadline today (2026-07-19) and passed without escalation, joining Oracle EBS CVE-2026-46817 (past-due since yesterday). No new exploitation, IOC, attribution, or A&D-victim disclosure on any of them this window. The board is unchanged since the 0800 brief.

**Why it matters:** For a DIB estate the clock has flipped — an unpatched instance of any of these four internet-reachable CVEs now carries federal non-compliance on top of standing exploitation risk, not a countdown. The remediation action doesn't change; the compliance posture does. Second consecutive quiet Sunday phase: the weekend sweep and the afternoon collection promoted zero new findings.

---

## 🔓 Vulnerabilities

**Standing watch — weekend KEV deadlines have now closed, all quiet.**
- What: SharePoint on-prem CVE-2026-58644 (VT-041) plus FortiSandbox CVE-2026-25089 / CVE-2026-39808 (VT-045/046) hit their accelerated federal deadline today and passed with no escalation; Oracle EBS CVE-2026-46817 (VT-043) is now two days past its 2026-07-18 deadline. All four are KEV-listed and actively exploited.
- Status: no new exploitation, atomic IOC, actor attribution, or named A&D/DIB victim across the deadline passage. No Mandiant/GTIG exploitation confirmation on the Oracle EBS flaw. SharePoint exposure stays scoped to on-prem Server 2016/2019/SE — not SharePoint Online/M365.
- Why it matters for A&D: on-prem SharePoint, Fortinet appliances, and Oracle EBS 12.2 are common across DIB estates. Unpatched instances are now overdue — remediate and document the exception.
- Source: [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A2 · Vulns: [CVE-2026-58644](../vulnerabilities/CVE-2026-58644/profile.md) (VT-041), [CVE-2026-25089](../vulnerabilities/CVE-2026-25089/profile.md) (VT-045), [CVE-2026-39808](../vulnerabilities/CVE-2026-39808/profile.md) (VT-046), [CVE-2026-46817](../vulnerabilities/CVE-2026-46817/profile.md) (VT-043)

**wp2shell (CVE-2026-63030) — no new escalation since yesterday.**
- What: the critical unauthenticated WordPress Core RCE holds at its 2026-07-18 state — public GitHub PoCs live (existence noted only) and watchTowr's hedged early in-the-wild report, with no mass-exploitation telemetry beyond that onset and no named A&D victim.
- Why it matters for A&D: structural, not A&D-specific. Patched estates (6.9.5 / 7.0.2, forced auto-updates on) are safe; exposure sits at the public-web/marketing tier.
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/) · Digraph: A2 headline / B3 in-the-wild leg · Vuln: CVE-2026-63030 (net-new — VW-001, VT dossier promotion pending)

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in the reporting window. The now-closed weekend KEV deadlines remain the standing patch-priority for DIB estates running those systems; no named A&D victim in any tracked CVE this window. Tracked actors with historical A&D targeting: APT28, UNC1549, Lazarus, APT41, Salt Typhoon.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h. Background monitoring continues.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-07-19. Quiet Sunday close: the weekend and afternoon sweeps promoted no new findings, so this is a standing-watch update. All three weekend KEV deadlines have now closed with no escalation.

🔓 **Vulnerabilities**

• **[Weekend KEV deadlines close quietly — SharePoint, FortiSandbox, Oracle EBS all past-due](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — SharePoint on-prem CVE-2026-58644 and two FortiSandbox flaws (CVE-2026-25089 / CVE-2026-39808) hit their federal deadline today, July 19, and passed without escalation; Oracle EBS CVE-2026-46817 is now two days past its July 18 deadline. All actively exploited, all quiet — no new exploitation, IOCs, attribution, or A&D victim. Unpatched DIB instances are now overdue: *remediate and document the exception.*

• **[wp2shell holds steady — no new escalation since Saturday](https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/)** — The critical WordPress Core RCE (CVE-2026-63030) sits where it landed Saturday: public PoCs out, watchTowr's early in-the-wild signs, nothing beyond that onset. Patched estates (6.9.5 / 7.0.2, auto-updates on) are safe; exposure stays structural, not A&D-specific.
