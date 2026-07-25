---
brief_id: 2026-07-25-afternoon
brief_type: afternoon
published_at: 2026-07-25T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: null
human_override: null
word_count: 491   # Layer 1 body only (400-800 afternoon band); Layer 2 ~152 words
findings_referenced: []   # QUIET SATURDAY CLOSE-OUT — 0 net-new promotions, 0 rejections (15:30 pre-brief null; 2 BleepingComputer items discarded as non-A&D/non-roster/non-CVE). The two 2026-07-25 KEV deadlines (CVE-2026-16232, CVE-2026-50522) were the deadline-day UPDATE resurface THIS MORNING (2026-07-25-morning) — this afternoon carries them as an end-of-day CLOSE-OUT continuing-coverage pointer (same deadline, same day, no net-new since 08:00), so per the 2026-07-24-pm / 2026-07-23-pm precedent NO covered_in append and NO published_in_briefs back-write. Zimbra CVE-2025-66376, Windchill CVE-2026-12569, Oracle EBS CVE-2026-46817, libssh2 CVE-2026-55200, LegacyHive VT-042 are all no-change pointers. See _coverage-log 2026-07-25-pm-brief-meta.
tlp: CLEAR
test: false
discord_delivery:
  channel: intel-briefs
  channel_id: "1499952717173358672"
  message_ids: ["1530669174907474060"]
  parts: 1
  delivered_at: 2026-07-25T16:00:47-04:00
  via: librarian
teams_delivery: null     # TEAMS_WEBHOOK_INTEL_BRIEFS unset — hook exit 6 (skip, non-fatal)
---

# Afternoon Brief — 2026-07-25

**Tonight closes the federal remediation window on two actively-exploited KEV flaws** — Check Point SmartConsole (CVE-2026-16232) and Microsoft on-prem SharePoint (CVE-2026-50522). Both carry a July 25 CISA due date; unpatched fleets lapse into federal non-compliance at end of day and keep standing exploitation risk beyond it.

**Why it matters:** Both flaws sit on an A&D contractor's identity and collaboration plane — SmartConsole is security-management infrastructure, SharePoint holds program collaboration data. Nothing net-new crossed the wire this afternoon, so this is a close-out reminder: land the two patches before the window shuts tonight.

---

## 🚨 Active Threats

**No net-new active threats this cycle.** The 15:30 pre-brief returned null — two BleepingComputer items were discarded as non-A&D, non-roster, non-CVE. The grader promoted and rejected nothing.

**Standing watch — Russian state Zimbra email-espionage (no change since 2026-07-23)**
- CISA (AA26-204A) and Palo Alto Unit 42 report a Russian state-supported cluster — LAUNDRY BEAR / Void Blizzard — exploiting the zero-click Zimbra Classic-UI XSS CVE-2025-66376 for covert email theft, with the Defense Industrial Base named among targeted sectors. No new victim, IOC, or attribution this cycle.
- Action: confirm the November 2025 Zimbra patch on any Classic-UI instance; unpatched servers remain **likely** to be targeted. Attribution is the sources', not ours (Hard Rule 2).
- Source: [CISA AA26-204A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a) · Digraph: A2 (CVE-2025-66376 pending vuln-tracker index)

## 🔓 Vulnerabilities

**Close-out: the two KEV federal remediation deadlines shut tonight, July 25**
- [CVE-2026-16232](../vulnerabilities/CVE-2026-16232/profile.md) (Check Point SmartConsole — unauthenticated login-token theft) and [CVE-2026-50522](../vulnerabilities/CVE-2026-50522/profile.md) (Microsoft on-prem SharePoint — deserialization RCE for machine-key theft) both hit their CISA KEV due date today. Both remain actively exploited; no net-new exploitation, victim, or IOC since this morning.
- Action: finish both today before the window closes (federal scope). SharePoint still needs machine-key rotation — patching alone leaves already-forged auth tokens valid.
- For A&D: exposure is structural on both — no named A&D/DIB victim. This is patch-posture urgency, not an active A&D incident.
- Source: [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A2 (CISA KEV authoritative on the listing and the July 25 deadline; per-CVE grading in the linked dossiers)
- 🔗 **Update on:** 2026-07-25 morning — status moves from "deadline today" to "deadline closing tonight."

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in the reporting window. The two July 25 KEV items and the Zimbra campaign carry structural DIB exposure only — no named A&D/DIB victim on any surfaced topic. Tracked actors with historical A&D targeting: APT28, UNC1549, Lazarus, APT41, Salt Typhoon.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h.

## 📰 Other Signal

**Standing vuln-watch — no change on any thread.**
- PTC Windchill/FlexPLM active exploitation ([CVE-2026-12569](../vulnerabilities/CVE-2026-12569/profile.md)) carries forward — the patch-and-hunt priority stands, and Windchill is the most A&D-central platform on this list (ITAR/EAR-controlled engineering IP). ReliaQuest's Cl0p attribution remains unconfirmed and Archimedes does not endorse it.
- Oracle E-Business Suite [CVE-2026-46817](../vulnerabilities/CVE-2026-46817/profile.md) (VT-043) remains past its July 18 KEV deadline.
- libssh2 client-side out-of-bounds write [CVE-2026-55200](../vulnerabilities/CVE-2026-55200/profile.md) (VT-051) stays PoC-only, with no in-the-wild exploitation.
- LegacyHive / Nightmare Eclipse Windows profsvc LPE ([VT-042](../vulnerabilities/LegacyHive/profile.md)) remains unpatched, with no CVE and no in-the-wild exploitation — MSRC silent.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR unless flagged.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-07-25.

A quiet Saturday close-out — nothing net-new crossed the wire this afternoon, and the grader promoted nothing. The one hard action still open shuts tonight; every standing exposure below carries over unchanged from earlier today.

🔓 **Vulnerabilities**

• **[Last hours to clear two actively-exploited KEV flaws](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — Check Point SmartConsole (CVE-2026-16232) and on-prem SharePoint (CVE-2026-50522) both hit their CISA federal remediation deadline today, July 25, and the window closes tonight. Both remain under active exploitation for token theft. *Finish both before end of day* — SharePoint also needs machine-key rotation, since patching alone leaves already-forged tokens valid.

📰 **Other Signal**

• **[Windchill active-exploitation patch-and-hunt still stands](https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/)** — PTC Windchill and FlexPLM (CVE-2026-12569) carry forward unchanged, and this is the most A&D-central platform in play: it holds ITAR/EAR-controlled drawings, engineering models, and program IP. *Patch and hunt now* if you haven't already closed it. ReliaQuest's Cl0p attribution stays unconfirmed; Archimedes does not endorse it.
