---
brief_id: 2026-07-23-afternoon
brief_type: afternoon
published_at: 2026-07-23T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: null
human_override: null
word_count: 746
findings_referenced:
  - finding-2026-07-23-0003
  - finding-2026-07-23-0004
tlp: CLEAR
---

# Afternoon Brief — 2026-07-23

**CISA advisory AA26-204A and Palo Alto Unit 42 independently report a Russian state-supported campaign stealing email through a zero-click Zimbra flaw (CVE-2025-66376) — and CISA names the Defense Industrial Base among its targeted sectors.**

**Why it matters:** Zimbra runs across government and contractor webmail estates. A zero-click XSS that exfiltrates mail on message-view needs no user error, and CISA naming the DIB as a targeted sector makes an unpatched Zimbra server a direct sector exposure — even with no A&D victim named.

---

## 🚨 Active Threats

**Russian state-supported actors exploit a Zimbra zero-click XSS (CVE-2025-66376) for covert email theft — CISA names the DIB as a targeted sector**
- CISA (AA26-204A) and Unit 42 (CL-STA-1114) independently report a Russian state-supported cluster — LAUNDRY BEAR to the Netherlands AIVD/MIVD, Void Blizzard to Microsoft — compromising Western government and commercial Zimbra servers since at least July 2025.
- **Mechanism (class level):** JavaScript in a crafted HTML email runs on message-view with no user interaction and exfiltrates email data. Exploited as a zero-day before November 2025; patched November 2025; unpatched servers are **likely** to remain targeted.
- **A&D relevance is structural** — CISA lists the DIB among targeted sectors, but no A&D or DIB victim is named; sector exposure, not a targeted A&D campaign.
- **Attribution is the sources', not ours (Hard Rule 2).** CISA uses confirmed language — "Russian state-supported" — and assesses the intent is intelligence collection for Russia. The cluster is named LAUNDRY BEAR, Void Blizzard, and CL-STA-1114 across four bodies. Void Blizzard is not a roster actor but appears in the corpus via finding-2026-06-11-0007 (DOJ) — a candidate `/new-actor` decision for the operator, flagged not originated.
- **IOCs are provisional.** Six campaign domains were relay-captured (BleepingComputer) with ambiguous roles, pending verification against the authoritative CISA/Unit 42 appendix — not yet confirmed. First-party Splunk returned 0 hits over 90 days (visibility-bounded).
- **Action:** inventory Zimbra Collaboration Suite servers and confirm the November 2025 patch is applied; treat any unpatched Classic-UI instance as exposed.
- Source: [CISA AA26-204A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a) + [Unit 42 (CL-STA-1114)](https://unit42.paloaltonetworks.com/), relayed by [BleepingComputer](https://www.bleepingcomputer.com/) · Digraph: **A2** (two independent A-grade originators; single-source veto does not apply, WEP capped at **likely** — neither primary directly retrieved this cycle) · CVE-2025-66376 (not in the vuln index — vuln-tracker handoff).

## 🕵️ Actor Activity

**CERT-UA: UAC-0099 abuses a Notepad++ plugin DLL-hijack to deploy new malware — initial access linked to Sandworm ([#007](../threat-actors/Sandworm/profile.md))**
- CERT-UA, via a BleepingComputer relay (July 23), reports UAC-0099 distributing a password-protected archive that bundles legitimate Notepad++ v8.8.3 with a malicious sidecar DLL (LunchPoke, posing as the NppExport.dll plugin) for scheduled-task persistence, then loads BurnyBear and MatchBoil V2. Targeting is Ukrainian organizations; no A&D victim.
- **Access handoff, not a merge (Hard Rule 2).** CERT-UA attributes the campaign to UAC-0099 and says the activity is linked to handing initial access to APT44 ([Sandworm, roster #007](../threat-actors/Sandworm/profile.md)) — recorded exactly as CERT-UA's access-handoff relationship, not an identity equation. UAC-0099 is not a roster actor. Continues the CERT-UA → Sandworm thread from finding-2026-07-16-0003.
- **The CVE is disputed.** CERT-UA frames the delivery around CVE-2025-56383 (Notepad++ plugin DLL-hijacking), but the Notepad++ team disputes it as standard plugin functionality — treat it as disputed plugin-DLL-load abuse, not a confirmed exploitation primitive.
- **A&D relevance is low** — no A&D nexus, but the signed-app-plus-sidecar-DLL → scheduled-task pattern is portable tradecraft applicable to any Notepad++-using developer endpoint.
- **IOCs are filename-only** (NppExport.dll, InitTest.dll, updater.rar) with no hashes — not actionable alone (NppExport.dll is also a legitimate plugin name); the CERT-UA hash/C2 appendix was not retrieved. First-party Splunk: 0 hits over 90 days (visibility-bounded).
- **Action:** low priority — update Notepad++ (CERT-UA cites v8.9.7) on developer endpoints and watch for scheduled-task persistence dropped by sidecar DLLs.
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-abuse-notepad-plus-plus-plugins-to-stealthily-install-malware/) relaying CERT-UA · Digraph: **B2** (single-source veto — one relay of one CERT-UA advisory, primary not retrieved; WEP **likely**) · CVE-2025-56383 (disputed; not in the vuln index).

## ✈️ Sector Focus: Aerospace & Defense

No A&D or DIB victim was named this window. The Zimbra campaign's DIB-sector naming is structural exposure, not an A&D-directed operation; the UAC-0099 / Notepad++ activity has no A&D nexus and is portable-tradecraft interest only. Tracked actors with historical A&D targeting: APT28, UNC1549, Lazarus, APT41, Salt Typhoon.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h. This morning's CISA/FBI/EPA Iran-OT advisory coverage stands with no state change.

## 📰 Other Signal

**Standing KEV watch:** the July 25 federal deadline for Check Point SmartConsole [CVE-2026-16232](../vulnerabilities/CVE-2026-16232/profile.md) and on-prem SharePoint [CVE-2026-50522](../vulnerabilities/CVE-2026-50522/profile.md) is two days out — no net-new on either this cycle. Oracle EBS CVE-2026-46817 (VT-043) remains past-due since July 18.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR unless flagged.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-07-23.

🚨 **Active Threats**

• **[CISA and Unit 42 flag Russian state hackers stealing email via a zero-click Zimbra flaw](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a)** — CISA advisory AA26-204A and Palo Alto Unit 42 independently report a Russian state-supported cluster (LAUNDRY BEAR / Void Blizzard) exploiting Zimbra XSS bug CVE-2025-66376 for covert email theft since at least July 2025. It runs on message-view with no user interaction; exploited as a zero-day, patched November 2025, unpatched servers still hit. CISA names the Defense Industrial Base among targeted sectors — but no A&D victim. *Inventory Zimbra servers and confirm the November 2025 patch.* Attribution is CISA's and Unit 42's, not ours.

🕵️ **Actor Activity**

• **[CERT-UA: UAC-0099 hides malware in a fake Notepad++ plugin, feeding access to Sandworm](https://www.bleepingcomputer.com/news/security/hackers-abuse-notepad-plus-plus-plugins-to-stealthily-install-malware/)** — CERT-UA (via BleepingComputer, July 23) says UAC-0099 bundles legitimate Notepad++ with a malicious sidecar DLL (LunchPoke) to drop BurnyBear and MatchBoil V2 on Ukrainian targets, with the activity linked to handing initial access to APT44/Sandworm. The Notepad++ team disputes the underlying CVE-2025-56383 as normal plugin behavior. No A&D victim — but the signed-app-plus-sidecar-DLL trick is portable. Update Notepad++ (v8.9.7) on developer endpoints.
