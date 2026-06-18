---
raw_id: raw-2026-06-18-am-008-sw-kovacs-rokarolla-android-banking-trojan-zimperium
collected_at: 2026-06-18T07:44:30-04:00
run_id: pre-brief-20260618-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (Eduard Kovacs)
  source_url: https://www.securityweek.com/rokarolla-banking-trojan-targets-200-applications/
  published_at: 2026-06-18T06:42:21-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Rokarolla, "Android banking trojan", Zimperium, zLabs, "device takeover", "credential phishing", "accessibility services", "screen overlays"]
triage_tags: [commodity_consumer_mobile, financial, not_ad_priority, no_named_actor, single_publisher_at_sweep_time, anti_noise_check_against_reject_2026_06_17_0011]
iocs_extracted: false
iocs_count: 0
text_word_count: 380
promoted: false
rejected_at: 2026-06-18T08:23:00-04:00
rejection_id: reject-2026-06-18-0006
ttl_expires_at: 2026-09-16T07:44:30-04:00
---

# Rokarolla Banking Trojan Targets 200 Applications (SW-Kovacs primary, third-publisher relay)

**Publisher:** SecurityWeek (Eduard Kovacs byline)
**Published:** 2026-06-18T06:42 EDT
**URL:** https://www.securityweek.com/rokarolla-banking-trojan-targets-200-applications/

## Article body summary

The Android malware Rokarolla, documented by Zimperium zLabs, allows operators to take control of infected devices and harvest sensitive information across approximately 217 banking and cryptocurrency applications. Distribution via malicious websites impersonating legitimate apps (Chrome, TikTok). Capabilities include lockscreen credential harvesting (PIN / pattern / password), screen overlays to phish banking app credentials, Accessibility Services abuse for WhatsApp contact harvesting, SMS exfiltration, call hijacking, keylogging, clipboard manipulation for cryptocurrency redirect, screenshot capture, and audio muting to suppress security alerts.

Zimperium quoted: "this audio suppression effectively masks critical cues, such as security alert notifications or incoming verification calls from banking institutions."

Evasion: hides app icon from drawer, disables Google Play Protect, mutes all device audio and vibrations. Distribution via fake Google Play Protect impersonation pages.

NO specific tracked-actor attribution by Zimperium. NO A&D-prime named victim. Consumer banking + cryptocurrency Android targeting.

---

## Extraction notes

- Language: en
- Publisher byline: Eduard Kovacs (SecurityWeek)
- Article type: trade-press IR-research relay
- Substrate context: this is the third-publisher relay (HNS-Markovic 2026-06-17 PM + SA-Paganini 2026-06-17 PM + SW-Kovacs this sweep) of the Zimperium zLabs research on Rokarolla. Already vetted as out-of-scope consumer Android banking via reject-2026-06-17-0011 (HNS-Markovic PM brief substrate). Anti-noise Rule 1 BINDING — discarded as raw-signal-eligible substrate only (not a finding scaffold candidate).
- T-gates evaluation: T1/T6 FAIL no CVE; T2/T4 FAIL no tracked-actor; T5 FAIL consumer Android banking NOT A&D / DIB / CMMC / ITAR. Critical-override 0-of-4 — non-FLASH-eligible.
- A&D-relevance: low. Consumer-mobile platform. Possible morning brief Other Signal one-liner for accessibility-abuse-pattern watch but already covered in PM brief reject.
- Attribution discipline: NO actor named. Hard Rule 2 BINDING.
- Recorded for grader audit-trail awareness — Rokarolla third-publisher journalistic-relay substrate-strengthening on publisher-independence layer only.
