---
brief_id: 2026-06-03-afternoon
brief_type: afternoon
published_at: 2026-06-03T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_invoked_no_substantive_claim_above_likely
human_override: null
status: published
run_id: afternoon-20260603-160000
word_count: 1118
findings_referenced:
  - finding-2026-06-03-0005
  - finding-2026-06-03-0006
  - finding-2026-06-03-0007
  - finding-2026-06-03-0003          # carry-forward UPDATE
related_vulns:
  - CVE-2026-45247                   # Mirasvit Magento KEV add, 3-day federal due 2026-06-06
  - CVE-2026-8206                    # Kirki Customizer Framework unauth privesc/account takeover
  - CVE-2026-49975                   # HTTP/2 Bomb carry-forward — Envoy timing + AI-methodology specificity
related_actors: []                   # Hard Rule 2 — three-vendor declination on CVE-2026-45247; Symantec declines attribution on stock-exchange espionage; no actor named in any PM item
related_zero_days: []
related_campaigns: []
update_on:
  - finding-2026-06-03-0003          # HTTP/2 Bomb — Envoy-priority timing (~10s) + Calif/OpenAI Codex methodology specificity fold into AM monitoring-tier surface
tlp: CLEAR
watch_signals_set:
  - third_compressed_kev_clock_within_seven_days_triggers_kac_rerun     # If a third 3-day KEV add lands by 2026-06-10, re-run KAC on cadence-shift hypothesis
  - tier_1_ir_firm_attribution_on_cve_2026_45247_collapses_ach_tie     # Mandiant / Unit 42 / MSTIC / CrowdStrike on CVE-2026-45247 collapses five-way attacker-class tie
  - stock_exchange_outlook_ttp_recurrence_against_second_high_value_executive_actor_profiler_scaffold # Recurrence of Aspose-wrapper + OneDrive-Personal-exfil + scheduled-task-rotation TTP set escalates to /new-actor scaffolding consideration
  - microsoft_iis_envoy_pingora_official_patch_or_advisory_on_http2_bomb # Any unpatched-vendor official patch on CVE-2026-49975 lifts to action-tier
discord_delivery:
  channel: intel-briefs
  channel_id: "1499952717173358672"
  message_ids:
    - "1511831403401187509"
  parts: 1
  delivered_at: 2026-06-03T16:00:32-04:00
  late: false
  via: librarian
---

# Afternoon Brief — 2026-06-03

**CVE-2026-45247 (Mirasvit Full Page Cache Warmer / Magento 2 PHP deserialization unauth RCE, CVSS 9.8) lands on CISA KEV with first-party Imperva WAF telemetry of active exploitation — patch 1.11.12 has been out since 2026-05-25, and any DIB-prime or Tier-2/3 supplier running the extension is the action surface today.**

**Why it matters:** Magento powers DIB-prime e-commerce and supplier portals; Mirasvit Cache Warmer adoption at primes is unknown at OSINT surface but documented across the small-to-mid Magento commerce base. CISA's federal due date is 3 days (2026-06-06) — supporting signal that compresses the timeline, not the primary justification. Pair this with a Symantec + Carbon Black 150-day Outlook-mailbox-theft tradecraft signal whose TTPs are reusable against A&D Outlook estates, and an HTTP/2 Bomb update sharpening Envoy as the unpatched edge to prioritize.

---

## 🚨 Active Threats

**CVE-2026-45247 — Mirasvit Full Page Cache Warmer / Magento 2 unauth RCE; CISA KEV, Imperva ITW telemetry, patched version available** *([finding-2026-06-03-0005](finding-2026-06-03-0005.md))*

- **What.** [CISA added CVE-2026-45247 to KEV](https://www.cisa.gov/news-events/alerts/2026/06/03/cisa-adds-one-known-exploited-vulnerability-catalog) with a 3-day federal due date of 2026-06-06. [Sansec's research](https://sansec.io/research/mirasvit-cache-warmer-object-injection) identifies a PHP Object Injection sink (CWE-502) reached unauthenticated via a crafted `CacheWarmer` cookie; [Imperva WAF telemetry](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-45247-in-mirasvit-full-page-cache-warmer-for-magento/) confirms active exploitation attempts carrying serialized PHP object payloads. [NVD](https://nvd.nist.gov/view/vuln/detail?vulnId=CVE-2026-45247) records CVSS 9.8. Affected versions: all Mirasvit Full Page Cache Warmer **before 1.11.12**; patched **1.11.12** released 2026-05-25. Sansec exposure scan estimates ~6,000 stores running Mirasvit extensions.
- **Attribution.** CISA, Sansec, and Imperva all decline attribution; Sansec's declination despite Magecart-ecosystem visibility is itself the analytic signal. **Archimedes does not originate attribution** — analyst SAT-ACH on attacker-class produced a five-way tie at zero inconsistencies (commodity / novel-financial / state-affiliated / multi-actor / false-flag); only "established-Magecart-cluster-Sansec-chose-not-to-name" is mildly disfavored.
- **DIB A&D action.** Audit Magento 2 deployments for the Mirasvit Cache Warmer extension (`composer show mirasvit/module-cache-warmer` or extension manager check). If present, update to **1.11.12+** immediately. If patch deployment is delayed, deploy Imperva's published WAF filter — cookie pattern `CacheWarmer:(Tz|Qz|YT)` (base64 PHP-serialized object markers) — as interim protection. Tier-2/Tier-3 supplier outreach via CMMC Level-1/2 channels: small-business contractors are more likely to run Magento storefronts than primes themselves.
- **The 3-day clock is supporting signal, not primary.** Analyst KAC found the "compressed clock = FCEB exposure" inference rests on assumptions Archimedes cannot inspect, and a second 3-day clock landed 24h earlier ([finding-2026-06-02-0005](finding-2026-06-02-0005.md), Linux cgroups CVE-2022-0492) — the "anomaly" reading is weakening. Action triggers on **CVSS 9.8 + Imperva ITW + canonical patch availability + extension presence**, independent of the clock-inference chain.
- Digraph **A2** (CISA + NVD ratified-A backbone; Sansec provisional-C originating + Imperva provisional-B WAF telemetry across three independent evidence bases) · WEP **very likely** procedural / **likely** substantive (active exploitation, A&D-prime exposure) / **roughly even chance** attacker-class.

## 🔓 Vulnerabilities

**UPDATE: HTTP/2 Bomb (CVE-2026-49975) — Envoy is the sharpest unpatched edge; Calif's OpenAI Codex methodology more specific** *(update on [finding-2026-06-03-0003](finding-2026-06-03-0003.md))*

- **What's new.** PM telemetry sharpens per-server impact: **Envoy ~10s to DoS at ~5,700:1 amplification**, Apache ~18s at ~4,000:1, NGINX ~45s, IIS ~45s. Calif's combined HPACK Bomb + Slowloris chain is the disclosure path; OpenAI Codex was used to discover the chain (methodology specificity, not actor signature). NGINX 1.29.8+ and Apache 2.4.64+ remain patched; **IIS, Envoy, and Cloudflare Pingora unpatched** at publication. No ITW.
- **DIB A&D action.** Prioritize **Envoy** for interim mitigation given the ~10s/5,700:1 profile — cap HPACK header counts and per-connection request rates at the proxy/sidecar layer; validate NGINX 1.29.8+ and Apache 2.4.64+ at the web edge.
- Digraph **B3** unchanged · WEP **likely** affected-product matrix / **very likely** CVE assignment procedural.

**CVE-2026-8206 — Kirki Customizer Framework WordPress plugin unauth privesc / account takeover; ITW per Defiant** *([finding-2026-06-03-0007](finding-2026-06-03-0007.md))*

- **What.** [SecurityWeek (Ionut Arghire)](https://www.securityweek.com/critical-flaw-in-kirki-customizer-framework-actively-exploited/) relays Defiant/Wordfence telemetry: CVE-2026-8206 (CVSS 9.8) and a sibling Burst Statistics plugin flaw are under active mass-exploitation, with thousands of blocked attacks in the past 24 hours per Defiant. Kirki affected 6.0.0–6.0.6; patched **6.0.7**. Burst Statistics affected 3.4.0–3.4.1.1; patched 3.4.2. No actor attribution; commodity mass-exploitation framing.
- **DIB A&D action.** Monitoring-tier — A&D-prime marketing-microsite WordPress estates are typically segregated from CUI/ITAR networks. **Tier-2/Tier-3 supplier outreach** is the operational pivot: small-business defense contractors hosting on WordPress should patch Kirki and Burst Statistics now.
- Digraph **B3** · WEP **likely** on substantive ITW magnitude (single-source through single relay; veto applied).

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific threats against watchlist companies in the reporting window. CVE-2026-45247 reach into A&D is indirect via Magento storefront / supplier-portal estates; CVE-2026-8206 reach is indirect via WordPress marketing-microsite estates and Tier-2/3 supplier infrastructure. Tracked actors with historical A&D targeting: APT28, [UNC1549](threats/threat-actors/UNC1549/profile.md), Lazarus, APT41, Salt Typhoon.

## 🕵️ Actor Activity

No new attributed campaigns in the reporting window. Gamaredon carry-over from 2026-06-02 afternoon still stands; Sekoia "FSB's matryoshka" #2/3 and #3/3 not yet published.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors ([UNC1549 #004](threats/threat-actors/UNC1549/profile.md), [Charming Kitten #011](threats/threat-actors/Charming-Kitten/profile.md), Handala Hack #014, [MuddyWater #022](threats/threat-actors/MuddyWater/profile.md)) in 48h.

## 📰 Other Signal

**Symantec + Carbon Black document 150-day Outlook mailbox theft against unnamed major global stock exchange executive — no A&D victim, no actor attribution, but reusable TTPs against A&D Outlook estates** *([finding-2026-06-03-0006](finding-2026-06-03-0006.md))*

- **What.** [SecurityWeek (Eduard Kovacs)](https://www.securityweek.com/hackers-target-global-stock-exchange-in-espionage-operation/) and [SecurityAffairs (Pierluigi Paganini)](https://securityaffairs.com/193086/intelligence/cyber-espionage-campaign-targeted-stock-exchange-executives-outlook-account.html) relay a Symantec Threat Hunter Team + Carbon Black joint write-up: 150-day dwell (2025-10-10 to 2026-03-19), single senior executive's mailbox, entry vector unknown. Core tradecraft wraps **Aspose** (a legitimate commercial .NET library) for OST→PST conversion in dated chunks; eight subsequent extraction runs at 2–4 week intervals adjoin `-t` time-windows for near-continuous mailbox theft. Exfiltration via **Dropbox + OneDrive Personal**, with **hardcoded Microsoft IPs** (not hostnames) bypassing DNS-tier logging. Persistence via scheduled tasks rotated across 5min / 5hr / 15hr / 24hr intervals under Adobe / Lenovo / OneDrive masquerade.
- **Attribution.** Symantec explicitly declines: "almost certainly state-linked given the target and the patience involved" (12 words, preserved verbatim). **Archimedes does not name a state class** — analyst SAT-ACH produced a five-way tie at zero inconsistencies (Russian / Chinese / Iranian / novel-state / false-flag-state); DPRK financial-pivot and criminal-with-state-discipline mildly disfavored but not ruled out.
- **Why it matters for A&D — TTPs structurally reusable; A&D-specific controls may break specific mechanism transfer.** Mailbox theft against A&D leadership is a canonical intelligence-collection objective (contract negotiation, supplier relationships, program scheduling metadata). Reusable layers: Aspose-wrapper OST→PST is platform-agnostic against any Outlook-using enterprise; Dropbox + OneDrive Personal exfil exploits the sanctioned-cloud blend DIB SOCs already struggle to distinguish from normal user behavior; **hardcoded-IP DNS-bypass is itself the CTI insight — DNS-tier blocklisting alone does not close this egress visibility gap**, IP-tier egress monitoring required. Mechanism-transfer hedges: A&D AppLocker/WDAC may block unsigned-Aspose load; ITAR/CUI personal-cloud policy may restrict but is loosely enforced on executive endpoints per documented audit patterns; Aspose may have legitimate footprint at primes running eDiscovery / litigation-hold tooling.
- **Defender pivot.** Extract Symantec's published file-hash IOC set from security.com, then hash-pivot against `archimedes` + `defenseclaw_local`. Splunk hunts: Aspose namespace invocation from non-licensed endpoints; scheduled-task masquerade names with unusual rotation intervals; outbound HTTPS to `onedrive.live.com` / personal-tenant `graph.microsoft.com` from cleared-personnel endpoints; outbound HTTPS to hardcoded Microsoft IPs (not hostnames).
- Digraph **B2** (Symantec provisional-A originating; SecurityWeek + SecurityAffairs B-grade publisher-independent relays; evidence-basis-independence fails through single-Symantec-primary; single-source veto applied) · WEP **likely** substantive / **very likely** procedural-fact / **roughly even chance** within-state-class.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-03.

🚨 **Active Threats**

- **[CVE-2026-45247 — Mirasvit Magento unauth RCE on CISA KEV; Imperva sees ITW](https://www.cisa.gov/news-events/alerts/2026/06/03/cisa-adds-one-known-exploited-vulnerability-catalog)** — Mirasvit Full Page Cache Warmer PHP deserialization, CVSS 9.8, federal due Saturday June 6. Patch **1.11.12** out since May 25. *DIB Magento operators: audit, patch, or WAF-filter the `CacheWarmer:(Tz|Qz|YT)` cookie.* Three-vendor attribution declination preserved.

🔓 **Vulnerabilities**

- **[UPDATE — HTTP/2 Bomb CVE-2026-49975: Envoy is the sharpest unpatched edge](https://www.securityweek.com/http-2-bomb-exploit-knocks-web-servers-offline-in-seconds/)** — Per-server timing: Envoy ~10s at 5,700:1 amplification, Apache ~18s, NGINX & IIS ~45s. NGINX 1.29.8+ and Apache 2.4.64+ patched; IIS, Envoy, Pingora unpatched. *Prioritize Envoy — cap HPACK headers and per-connection rates at the sidecar.*

- **[CVE-2026-8206 — Kirki WordPress unauth privesc; thousands of attacks/24h](https://www.securityweek.com/critical-flaw-in-kirki-customizer-framework-actively-exploited/)** — CVSS 9.8 account-takeover in Kirki 6.0.0–6.0.6 (patched 6.0.7) plus a Burst Statistics sibling. *Tier-2/3 supplier outreach — small-business contractors on WordPress should patch today.*

📰 **Other Signal**

- **[Symantec: 150-day Outlook mailbox theft against unnamed stock exchange exec](https://www.securityweek.com/hackers-target-global-stock-exchange-in-espionage-operation/)** — Aspose-wrapper OST→PST, Dropbox + OneDrive Personal exfil, **hardcoded Microsoft IPs bypassing DNS logging**, scheduled-task masquerade. Symantec: "almost certainly state-linked given the target and the patience involved." *Archimedes does not name a state class.* **DNS blocklisting alone won't close the IP-tier egress gap.**
