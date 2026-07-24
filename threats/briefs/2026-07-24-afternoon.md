---
brief_id: 2026-07-24-afternoon
brief_type: afternoon
published_at: 2026-07-24T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: null
human_override: null
word_count: 497   # Layer 1 body only (400-800 afternoon band), consistent with prior-brief convention; Layer 2 ~165 words
findings_referenced: []   # QUIET AFTERNOON — 0 net-new promotions; all in-window items dedup/discarded. No finding receives net-new coverage this cycle. Every referenced topic (Zimbra CVE-2025-66376, Check Point CVE-2026-16232, SharePoint CVE-2026-50522, Oracle EBS CVE-2026-46817, Windchill CVE-2026-12569, UAC-0099) is a NO-CHANGE continuing-coverage pointer to prior briefs — per the 2026-07-23-afternoon precedent, no-change pointers do NOT append covered_in and do NOT back-write published_in_briefs. See _coverage-log 2026-07-24-pm-brief-meta.
tlp: CLEAR
test: false
discord_delivery:
  channel: intel-briefs
  message_ids: ["1530306432803799120"]
  parts: 1
  delivered_at: 2026-07-24T16:00:47-04:00
  late: false
  via: librarian
teams_delivery:
  status: skipped
  reason: TEAMS_WEBHOOK_INTEL_BRIEFS unset (exit 6)
---

# Afternoon Brief — 2026-07-24

**No net-new threats crossed the wire this afternoon; the highest standing A&D exposure remains yesterday's Russian state-supported Zimbra email-theft campaign (CVE-2025-66376), and two KEV-listed flaws hit their federal patch deadline tomorrow.**

**Why it matters:** On a low-signal day the work is defensive housekeeping — confirm the November 2025 Zimbra patch, and clear tomorrow's two July 25 KEV deadlines before they lapse into federal non-compliance and standing exploitation risk. No new A&D-directed campaign has emerged.

---

## 🚨 Active Threats

**No net-new active threats this afternoon.** The 15:30 pre-brief produced zero net-new substantive signal — all in-window items were duplicates or discarded.

**Standing watch — Russian state Zimbra email-espionage (no change since the 2026-07-23 afternoon brief)**
- Covered in full yesterday: CISA (AA26-204A) and Palo Alto Unit 42 (CL-STA-1114) report a Russian state-supported cluster — LAUNDRY BEAR / Void Blizzard — exploiting the zero-click Zimbra Classic-UI XSS CVE-2025-66376 for covert email theft, with the Defense Industrial Base named among targeted sectors.
- No new victim, IOC, or attribution development this cycle. A&D relevance stays structural — no named A&D/DIB victim. Attribution is the sources', not ours (Hard Rule 2).
- Action: unchanged — confirm the November 2025 Zimbra patch on any Classic-UI instance; unpatched servers remain **likely** to be targeted.
- Source: [CISA AA26-204A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a) + [Unit 42](https://unit42.paloaltonetworks.com/) · Digraph: A2 (WEP capped at likely — neither A-primary directly retrieved) · CVE-2025-66376 (not in the vuln index — vuln-tracker handoff pending).

## 🔓 Vulnerabilities

**Two KEV-listed flaws reach their federal remediation deadline tomorrow, July 25 — no net-new on either this cycle**
- [CVE-2026-16232](../vulnerabilities/CVE-2026-16232/profile.md) (Check Point SmartConsole — unauthenticated improper-auth login-token theft) and [CVE-2026-50522](../vulnerabilities/CVE-2026-50522/profile.md) (Microsoft on-prem SharePoint — deserialization RCE for machine-key theft) both carry a 2026-07-25 CISA KEV due date. Both remain actively exploited; no net-new exploitation, victim, or IOC surfaced today.
- For A&D: exposure is structural on both — no named A&D/DIB victim. This is patch-posture urgency, not an active A&D incident.
- Action: remediate both by tomorrow (federal scope). SharePoint additionally needs machine-key rotation — patching alone leaves already-forged auth tokens valid.
- Source: [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A2 (CISA KEV — authoritative on the listing and the July 25 deadline; per-CVE grading in the linked dossiers).

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in the reporting window. The Zimbra campaign's DIB-sector naming remains structural exposure, not an A&D-directed operation, and no A&D/DIB victim has been named on it or on the two July 25 KEV items. Tracked actors with historical A&D targeting: APT28, UNC1549, Lazarus, APT41, Salt Typhoon.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h. The CISA/FBI/EPA Iran-OT advisory thread (AA26-097A revision), covered 2026-07-22 and 2026-07-23, stands with no state change.

## 📰 Other Signal

**Standing vuln-watch — no change.** Oracle E-Business Suite [CVE-2026-46817](../vulnerabilities/CVE-2026-46817/profile.md) (VT-043) remains past its July 18 KEV deadline. This morning's PTC Windchill/FlexPLM active-exploitation lead ([CVE-2026-12569](../vulnerabilities/CVE-2026-12569/profile.md)) carries forward with no afternoon development — the patch-and-hunt priority stands. Yesterday's UAC-0099 / Notepad++ activity (Ukraine theater) shows no A&D nexus and no change.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR unless flagged.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-07-24.

A quiet afternoon — nothing net-new crossed the wire. Two housekeeping actions and one standing exposure carry over.

🔓 **Vulnerabilities**

• **[Two KEV-listed flaws hit their federal patch deadline tomorrow](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — Check Point SmartConsole (CVE-2026-16232) and on-prem SharePoint (CVE-2026-50522) both carry a July 25 CISA remediation due date, and both remain actively exploited for token/credential theft. *Close both out by tomorrow* — SharePoint also needs machine-key rotation, since patching alone leaves forged tokens valid. Oracle E-Business Suite (CVE-2026-46817) is still past its July 18 deadline.

🚨 **Active Threats**

• **[Top standing A&D exposure, unchanged: Russian state Zimbra email theft](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a)** — No change since yesterday. CISA (AA26-204A) and Unit 42 report a Russian state-supported cluster exploiting Zimbra's zero-click XSS (CVE-2025-66376) for covert email theft, with the Defense Industrial Base named as a targeted sector. *Confirm the November 2025 Zimbra patch is applied.* Attribution is CISA's and Unit 42's, not ours.
