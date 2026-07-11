---
brief_id: 2026-07-11-afternoon
brief_type: afternoon
published_at: 2026-07-11T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: null          # not required — 0 net-new findings; no WEP very_likely+ new claim this cycle
human_override: null
word_count: 512
findings_referenced: []        # 0 net-new promoted findings this cycle
grading_run_id: afternoon-20260711-160000
grading_run_promotions: 0
grading_run_rejections: 0       # all in-window items discarded at collection; grader had nothing to promote or reject
tlp: CLEAR
discord_delivery:
  channel: intel-briefs
  message_ids: [1525596009047261334]
  parts: 1
  delivered_at: 2026-07-11T16:13:57-04:00
  via: librarian
---

# Afternoon Brief — 2026-07-11

**The 15:30 afternoon collection was a clean sweep — zero net-new findings, no FLASH triggers, and no watchlist company named.** The tracked board is unchanged since this morning: ColdFusion CVE-2026-48282 remains the only live-deadline item (federal remediation window lapsed July 10), while Gitea CVE-2026-20896 and Progress ShareFile hold steady with no in-window movement.

**Why it matters:** A quiet cycle means no new emergency actions for a DIB shop. The standing work is finishing the ColdFusion patch and holding the ShareFile power-off — not chasing fresh signal that hasn't materialized.

---

## 🚨 Active Threats

**No net-new active threats this cycle.** The 12:00 EDT FLASH sweep and the 15:30 pre-brief collection each returned zero candidates. CISA KEV added no A&D-relevant entries; Splunk returned zero IOC hits (only `archimedes` self-references).

The one standing watch item — Progress ShareFile Storage Zone Controllers (B2 · likely) — is unchanged since [this morning's brief](2026-07-11-morning.md): the vendor's promised ~24h follow-up to Friday's emergency power-off order still has not surfaced in the reporting window. Action unchanged — DIB teams that powered off on-prem SZC should keep them down and wait for the vendor bulletin before restoring. Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/progress-urges-sharefile-customers-to-shut-down-servers-over-credible-threat/)

---

## 🔓 Vulnerabilities

**No net-new vulnerabilities cleared the bar this window.** CISA KEV added no new entries since the July 10 Joomla-extension pair (CVE-2026-56291 Balbooa Forms, CVE-2026-48939 iCagenda), already logged out-of-A&D-scope at the 0800 brief.

The open vulnerability board is unchanged since [this morning's brief](2026-07-11-morning.md):

- **[ColdFusion CVE-2026-48282](../vulnerabilities/Adobe-ColdFusion-CVE-2026-48282/profile.md)** (A2 · exploitation very likely) — the max-severity, actively-exploited RCE whose BOD 22-01 deadline lapsed July 10. No new victims, CVE state, or telemetry today. The July 1 Adobe patch remains the only control; treat any unpatched, internet-exposed instance as compromised until proven otherwise.
- **Gitea CVE-2026-20896** (B2 · likely) — auth-bypass in the Gitea Docker image; fix remains 1.26.3 / 1.26.4. No change in the reporting window. A CISA KEV listing would lift the exploitation assessment from "likely" to "very likely"; none has landed. Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-auth-bypass-in-gitea-docker-image/)

---

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in the reporting window. Tracked actors with historical A&D targeting: APT28, UNC1549, Lazarus, APT41, Salt Typhoon.

---

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h.

---

## 📰 Other Signal

**First-party sentinel — clean.** The afternoon sweep queried `defenseclaw_local` and `archimedes` and returned zero target-telemetry hits. Per Hard Rule 8, silent Splunk does not disconfirm — Frank is visibility-bounded.

**In-window open-source items reviewed and discarded — no A&D nexus.** Two net-new open-source stories were checked and dropped: an ACSC global CMS-exploitation campaign (commodity, no attribution; already dispositioned at the 12:00 FLASH) and a Datadog report on ghost GitHub accounts running mass API recon (no actor, CVE, victim, or IOCs). Both awareness-only; neither cleared the promotion bar.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-07-11.

A quiet close: the afternoon collection was a clean sweep — zero net-new findings, no FLASH triggers, no watchlist company named. Nothing has moved since this morning; here's where the three open items stand.

🔓 **Vulnerabilities**

• **[ColdFusion CVE-2026-48282 — federal patch deadline already passed](https://www.bleepingcomputer.com/news/security/max-severity-adobe-coldfusion-flaw-now-exploited-in-attacks/)** — The CISA deadline for this max-severity, actively-exploited RCE lapsed July 10, and nothing changed today. **Running ColdFusion 2025.9 / 2023.20 or earlier? Confirm the July 1 Adobe patch is applied and treat any exposed unpatched box as compromised.**

• **[Gitea auth-bypass CVE-2026-20896 — still open](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-auth-bypass-in-gitea-docker-image/)** — No change since Friday's Singapore CSA warning; fix is 1.26.3 / 1.26.4. DIB teams on internet-exposed Gitea Docker 1.26.2 or older should still upgrade.

🚨 **Active Threats**

• **[Progress ShareFile — vendor's promised follow-up still overdue](https://www.bleepingcomputer.com/news/security/progress-urges-sharefile-customers-to-shut-down-servers-over-credible-threat/)** — Progress ordered on-prem Storage Zone Controllers powered off Friday and promised an update within ~24 hours; that bulletin still hasn't landed. **Keep affected SZC powered off and watch for the vendor advisory before restoring.**
