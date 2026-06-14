---
brief_id: 2026-06-14-afternoon
brief_type: afternoon
published_at: 2026-06-14T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_required_update_layer_wep_ceiling_likely_on_bc_relay
human_override: null
word_count: 690
findings_referenced:
  - finding-2026-06-14-0001
rejections_referenced: []
tlp: GREEN
status: published
discord_delivery:
  channel: intel-briefs
  channel_id: "1499952717173358672"
  message_ids:
    - "1515812507040743496"
  parts: 1
  delivered_at: 2026-06-14T16:00:42-04:00
  late: false
  via: librarian
  layer_2_utf16_code_units: 1990
  operator_authorized_over_1900_buffer: true
cycle_class: single_update_atop_hold_status_carry_forward
sentinel_sweeps_in_window:
  - flash-2026-06-14-1200
  - pre-brief-2026-06-14-1530
sentinel_ioc_hits: 0
sentinel_ioc_set_size: 19
sentinel_sweeps_cumulative_since_2026_06_13_pm: 6
anti_noise_carry_forward_holds:
  - peoplesoft-unc6240-cve-2026-35273-fceb-kev-clock-t-minus-26h-sunday-eob
  - ivanti-sentry-cve-2026-10520-fceb-kev-clock-closes-tonight-t-minus-4-5h
  - splunk-enterprise-cve-2026-20253-postgres-sidecar-rce-self-substrate-pending-vendor-confirmation
  - npm-12-default-script-execution-change-defensive-roadmap-github-blog-primary-pending
  - velvet-ant-operation-highland-sygnia-primary-pending
  - handala-014-cal-water-iran-cyber-watch-third-source-negative-confirmed-hedge-binding
  - fable-5-mythos-5-anthropic-usg-export-control-3-publisher-status-quo
  - check-point-vpn-cve-2026-50751-qilin
  - shai-hulud-miasma-ironworm-npm-worm-family-operator-deferred-new-actor
  - unc3753-vishing-to-physical-mandiant-seeking-counsel-operator-deferred-new-actor
wep: likely
---

# Afternoon Brief — 2026-06-14

**FBI, Google, and Lumen Black Lotus Labs jointly disrupted the Outsider Enterprise smishing PhaaS today — administration-server seizures, ~1M-URL infrastructure ratified, no named-defendant indictment. The Ivanti Sentry CVE-2026-10520 KEV deadline closes in roughly four hours (EOB tonight); the Oracle PeopleSoft CVE-2026-35273 KEV deadline closes Sunday EOB. Zero net-new sector intel.**

**Why it matters:** A&D primes inherit both KEV deadlines via DFARS 252.204-7012 flow-down. The Outsider takedown is consumer-carrier credential theft — no direct DIB exposure — but it partially ratifies the 06-12 finding's open watch item on parallel criminal proceedings, and the cumulative-picture lifts the substantive-evidence-basis veto on the operational-structure claim.

---

## 🚨 Active Threats

**FCEB KEV deadlines — defender action by EOB tonight and Sunday EOB**

- **CVE-2026-10520 (Ivanti Sentry, CVSS 10.0):** FCEB BOD 26-04 3-day clock closes ~T-4.5h at publication. Patch to R10.5.2 / R10.6.2 / R10.7.1. DIB primes inherit via DFARS flow-down. Source: [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A1 (carry-forward) · finding-2026-06-11-0005.
- **CVE-2026-35273 (Oracle PeopleSoft, CVSS 9.8, UNC6240 / ShinyHunters per Mandiant primary direct):** FCEB BOD 26-04 3-day clock closes ~T-26h Sunday EOB. Oracle out-of-band mitigations only; no GA patch. Hunt the 19-IOC sentinel set; six consecutive Splunk sweeps since 06-13 PM returned zero hits — visibility-limited absence (Frank not higher-ed). Source: [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A1 (carry-forward) · finding-2026-06-13-0006.

## 🔓 Vulnerabilities — HOLD status

No net-new vulnerability disclosures in the reporting window. CVE-2026-20253 (Splunk Enterprise PostgreSQL-sidecar pre-auth RCE) carries forward — patched 2026-06-10, exploitation status *roughly even chance*, Frank Splunk Free 10.2.2 *likely* inherits the affected sidecar pending vendor confirmation. Patch action stands. Carry: [Splunk SVD-2026-0603](https://advisory.splunk.com/advisories/SVD-2026-0603) · Digraph: A2 · finding-2026-06-13-0004.

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in the reporting window. Tracked actors with historical A&D targeting: APT28, [UNC1549](../threat-actors/UNC1549/profile.md), Lazarus, APT41, Salt Typhoon. PeopleSoft KEV deadline above intersects A&D via deployed-cohort posture at DFARS-bound contractors.

## 🕵️ Actor Activity

🔗 **UPDATE on finding-2026-06-12-0006 — FBI + Google + Lumen Black Lotus Labs jointly disrupted Outsider Enterprise PhaaS**

- **What:** FBI operationally seized Outsider Enterprise administration servers in joint action with Google (continuing from its 06-12 SDNY civil suit) and Lumen Black Lotus Labs (new third joint participant adding network-telemetry corroboration). Net-new vs 06-12: operational-takedown layer atop the civil-litigation layer; ~1M-URL scale figure independently ratified by FBI action; two-week May 2026 SMS campaign window specified; Lumen as third evidence-basis class.
- **What this does NOT attest:** no federal criminal indictment of named defendants; no Chinese intelligence services attribution (per Google verbatim: "Based in China," "coordinating through Telegram" — civil cybercrime cluster, *not* state-attributed); no Volt Typhoon cross-walk despite Lumen's prior KV-botnet takedown lineage; no net-new IOCs (administration-server seizures at quantity-only granularity); no A&D direct intersection (consumer AT&T / T-Mobile / Verizon smishing).
- **Veto lift at cumulative-picture layer:** 06-12 substantive-evidence-basis single-Google-primary veto lifts because three distinct evidence bases now converge — Google civil + FBI operational + Lumen telemetry. The operational-structure-exists-in-fact claim moves from *likely* to *very likely*. BC-relay-only single-publisher veto still caps the 06-14 takedown announcement layer at *likely* until FBI .gov primary or second-publisher relay lands.
- **06-12 watch-item ratification:** partial. FBI operational disruption ratifies the parallel-criminal-proceedings open question but is *not* named-defendant indictment.
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/) · Digraph: B2 (BC-relay-only layer) / A2 (cumulative-picture layer) · finding-2026-06-14-0001.

**NPM 12 default script-execution change and Velvet Ant Operation Highland remain on HOLD** — GitHub blog primary and Sygnia primary still pending direct retrieval. *Archimedes does not endorse the Outsider Enterprise → Volt Typhoon linkage despite Lumen joint participation in both; clusters remain distinct per BC framing.*

## 🇮🇷 Iran Cyber Watch

**HOLD — Handala (#014) / Cal Water independence-check NEGATIVE confirmed (carry-forward).** Hard Rule 2 binding remains: Iranian retaliation *not* extrapolated to A&D-prime targeting from one water-utility cycle. OT/ICS impact *not* confirmed (RTKBase is GPS-correction infrastructure). No net-new substrate in this window. Source: [finding-2026-06-13-0003](../findings/finding-2026-06-13-0003-securityaffairs-handala-cal-water-iran-mois-dataminr-rtkbase-ntrip-second-publisher-corroboration-update-extension-on-pm-003.md) · Digraph: B3 (carry-forward).

## 📰 Other Signal

- **Splunk first-party sentinel (Hard Rule 8):** Six consecutive sweeps since 06-13 PM (1800 / 0000 / 0600 flash + 0730 / 1200 / 1530 pre-brief) returned zero events on the 19-IOC PeopleSoft / UNC6240 set across `defenseclaw_local` and `archimedes`. Silent Splunk does *not* disconfirm — Frank is *not* a higher-ed environment consistent with the 68% UNC6240 victim profile.
- **Cumulative-picture analytic note:** Today's UPDATE is the second Archimedes-corpus instance this week of multi-substrate convergence lifting a 06-12 single-vendor veto — the first being yesterday's Mandiant primary-direct retrieval on UNC6240 / PeopleSoft. Pattern observation only; no cluster claim.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:GREEN. Single substantive UPDATE atop HOLD-status carry-forward — no re-litigation of yesterday PM substrate.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-14.

🚨 **Active Threats**

• **[Ivanti Sentry CVE-2026-10520 KEV deadline closes tonight](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — CVSS 10.0; clock closes roughly four hours from publication EOB tonight. *Patch to R10.5.2 / R10.6.2 / R10.7.1 right now.* DIB primes inherit via DFARS flow-down.
• **[Oracle PeopleSoft CVE-2026-35273 KEV deadline closes Sunday EOB](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — CVSS 9.8; UNC6240 / ShinyHunters per Mandiant primary. Oracle out-of-band mitigations only, no GA patch. *Hunt the 19-IOC set this weekend.* Six consecutive Splunk sweeps since yesterday afternoon returned zero hits — visibility-limited, not disconfirmation.

🕵️ **Actor Activity**

• **[FBI, Google, and Lumen jointly disrupted the Outsider Enterprise smishing PhaaS](https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/)** — UPDATE on Thursday's Google civil suit. FBI seized administration servers; Lumen Black Lotus Labs joined as third participant with network telemetry. Scale figure (~1M URLs) ratified by the operational action. No named-defendant indictment, no Chinese intelligence services attribution (*per Google verbatim, "Based in China" — civil cybercrime cluster, not state-attributed*), no Volt Typhoon cross-walk despite Lumen's KV-botnet lineage, no A&D intersection (consumer AT&T / T-Mobile / Verizon smishing).

🔓 **Vulnerabilities**

• **Splunk CVE-2026-20253 (HOLD)** — patched June 10; exploitation status *roughly even chance* — the affected product IS the SIEM that would generate detection reports. Frank Splunk Free 10.2.2 likely inherits the affected sidecar; *patch regardless.*

📰 **Other Signal**

• **Sentinel posture:** Six sweeps since yesterday afternoon, zero IOC hits on the 19-IOC set. Single-substantive UPDATE day; no re-litigation of HOLD substrate.
