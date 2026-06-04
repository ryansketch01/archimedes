---
brief_id: 2026-06-04-afternoon
brief_type: afternoon
published_at: 2026-06-04T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_invoked_no_substantive_claim_above_likely
human_override: null
status: published
run_id: afternoon-20260604-160000
word_count: 945
findings_referenced:
  - finding-2026-06-04-0001          # Cisco Unified CM SSRF CVE-2026-20230
  - finding-2026-06-04-0002          # Five Eyes "Safeguarding Our Secrets" PLA HUMINT advisory
  - finding-2026-06-03-0003          # HTTP/2 Bomb CVE-2026-49975 — vendor-response carry-forward UPDATE
  - finding-2026-06-02-0005          # Linux cgroups CVE-2022-0492 — KEV T-0 tomorrow
  - finding-2026-06-03-0005          # Mirasvit Magento CVE-2026-45247 — KEV T-2 Saturday
  - finding-2026-06-03-0001          # Miasma / CVE-2026-45321 — KEV T-5 (pointer only)
  - finding-2026-06-02-0010          # Bitskrieg watch — Other Signal monitoring tier
related_vulns:
  - CVE-2026-20230                   # Cisco Unified CM SSRF, CVSS 8.6
  - CVE-2026-49975                   # HTTP/2 Bomb DoS chain
  - CVE-2022-0492                    # Linux cgroups v1; FCEB due 2026-06-05 (tomorrow)
  - CVE-2026-45247                   # Mirasvit Magento; FCEB due 2026-06-06 (Saturday)
  - CVE-2026-45321                   # Miasma; FCEB due 2026-06-10 (T-5)
related_actors: []                   # Hard Rule 2 — Five Eyes generic "China's military intelligence services" preserved verbatim; no roster mapping
related_zero_days: []
related_campaigns:
  - miasma-mini-shai-hulud-2026-06-01
update_on:
  - finding-2026-06-03-0003          # HTTP/2 Bomb vendor-response layer (Microsoft + Cloudflare on-record)
  - finding-2026-06-02-0005          # KEV T-0 final reminder
  - finding-2026-06-03-0005          # KEV T-2 deadline tick
tlp: CLEAR
discord_delivery:
  channel: intel-briefs
  channel_id: "1499952717173358672"
  message_ids:
    - "1512193299753205933"
  parts: 1
  delivered_at: 2026-06-04T16:00:47-04:00
  via: librarian
watch_signals_set:
  - cve_2026_20230_first_tier1_ir_firm_telemetry_of_attempted_exploitation_lifts_to_action_tier
  - cve_2026_20230_kev_listing_collapses_predictive_to_procedural
  - microsoft_iis_patch_tuesday_2026_06_10_natural_cadence_point_for_http2_bomb_iis_patch
  - independent_third_party_validation_of_cloudflare_pingora_no_patch_position_either_direction
  - follow_on_dcsa_fbi_ncsc_advisory_explicitly_naming_cleared_defense_contractor_populations
  - tier_1_ir_firm_attribution_of_specific_pla_unit_or_tracked_actor_to_safeguarding_our_secrets_activity
---

# Afternoon Brief — 2026-06-04

**Cisco PSIRT disclosed CVE-2026-20230 — an unauthenticated SSRF-to-root primitive in Unified Communications Manager, CVSS 8.6, public PoC, no in-the-wild use — while the Five Eyes published a rare joint counterintelligence advisory on China's military intelligence services running LinkedIn-led HUMINT recruitment against cleared personnel.**

**Why it matters:** On-prem CUCM is common at DIB primes and CMMC-scope suppliers where SaaS voice is contractually restricted; the 14-train patch is available now, but 15-train estates wait for September unless TAC issues a COP1 interim. The Five Eyes advisory hits the cleared-personnel surface — a counterintelligence problem with FSO/DCSA AND HR/corporate-recruiter due-diligence leverage points. Tomorrow is the Linux cgroups KEV deadline.

---

## 🚨 Active Threats

**UPDATE: CVE-2022-0492 Linux kernel cgroups v1 container escape — FCEB deadline T-0 tomorrow (2026-06-05)** *(final reminder; update on [finding-2026-06-02-0005](finding-2026-06-02-0005.md))*

- **What's new.** Deadline closes inside 18 hours. No additional vendor or Tier-1 IR firm surface in the PM sweep. CISA-direct evidence basis still unpublished; no actor attribution carried.
- **DIB A&D action.** If kernels ≤ 5.16.x have not been patched or rebuilt by EOD, deploy AppArmor/SELinux confinement on container runtimes as interim and capture release_agent file-write artifacts in EDR for backfill. AM brief carries the full action set; no re-broadcast.
- Digraph **A2** unchanged · WEP **very likely** procedural / **likely** active-exploitation operational.

## 🔓 Vulnerabilities

**Cisco Unified CM SSRF CVE-2026-20230 — CVSS 8.6, public PoC via SSD Secure Disclosure, no ITW** *(see [finding-2026-06-04-0001](finding-2026-06-04-0001.md))*

- **What.** [Cisco PSIRT advisory cisco-sa-cucm-ssrf-cXPnHcW](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW) (2026-06-03) discloses an unauthenticated network-accessible SSRF in Unified Communications Manager and CM SME that escalates to root via arbitrary file write. Cisco PSIRT verbatim: *"The Cisco PSIRT is not aware of any malicious use of the vulnerability."* (14 words)
- **Patch posture.** 14-train fixed in 14SU6, available now. 15-train waits for 15SU5 in September 2026; Cisco TAC can provide a COP1 interim. No workarounds; WebDialer (default-disabled) is a partial mitigation only.
- **A&D context.** Third critical-class CUCM CVE in 11 months — after CVE-2025-20309 hard-coded SSH root (July 2025) and CVE-2026-20045 unauthenticated RCE (January 2026, [actively exploited per THN](https://thehackernews.com/2026/06/cisco-patches-cve-2026-20230-in-unified.html)). On-prem CUCM remains common in cleared-personnel-administered voice estates.
- **DIB A&D action.** Inventory by branch. 14-train: patch to 14SU6 today (PoC is public). 15-train: request COP1 from Cisco TAC; until then, segment CUCM management interfaces from untrusted networks and enforce egress filtering. Confirm WebDialer default-disabled. EDR: watch for unexpected file-write activity on CUCM servers as post-exploit signature.
- Digraph **A2** · WEP **very likely** procedural / **likely** exploitation imminent (predictive layer single-source-vetoed).

**🔗 Latest on HTTP/2 Bomb CVE-2026-49975 — Microsoft on-record; Cloudflare disputes need for Pingora patch** *(update on [finding-2026-06-03-0003](finding-2026-06-03-0003.md); see [2026-06-03 afternoon](2026-06-03-afternoon.md))*

- **What's new.** [The Register](https://www.theregister.com/security/2026/06/04/openais-codex-chains-decade-old-dos-techniques-into-http/2-bomb/5251377) adds vendor-response statements. Microsoft spokesperson on-record: *"We are aware and actively investigating appropriate mitigations to help keep customers protected."* (13 words). Cloudflare (paraphrased; full statement exceeded 15 words): existing architecture and DDoS mitigations already protect against the attack — Cloudflare disputes the patch-needed claim for Pingora.
- **What is not new.** Underlying CVE, the NGINX 1.29.8+ and Apache HTTPD 2.4.64+ patches, and the IIS/Envoy/Pingora unpatched posture are unchanged from yesterday. No ITW.
- **DIB A&D action.** (a) IIS estates: track Patch Tuesday 2026-06-10 as the natural Microsoft cadence point; until then, Calif's HTTP/2-disable or header-count-cap interim stands. (b) Cloudflare-managed customers should confirm protection with their account team. Self-hosted Pingora (rare): defender prudence favors the Calif interim until independent third-party validation of Cloudflare's position lands.
- Digraph **B3** cluster-anchor unchanged · affected-product claim layered **A2** post Microsoft acknowledgement · WEP **very likely** IIS-affected / **roughly even chance** Pingora-actually-vulnerable.

**🔗 Carry-forward — CVE-2026-45247 Mirasvit Magento KEV deadline T-2 Saturday (2026-06-06)** *(see [finding-2026-06-03-0005](finding-2026-06-03-0005.md) and [2026-06-04 morning](2026-06-04-morning.md))*

- Deadline tick only. Imperva WAF telemetry of active exploitation and Sansec ~6,000-store exposure carry forward unchanged. AM action set stands; no re-broadcast. Composer audit + patch 1.11.12+ or the `CacheWarmer:(Tz|Qz|YT)` WAF filter — Tier-2/Tier-3 supplier outreach via CMMC channels still the high-leverage pivot.
- Digraph **A2** · WEP **likely**.

**🔗 Carry-forward — CVE-2026-45321 (Miasma / VT-006) KEV deadline T-5 next Wednesday (2026-06-10); no new vendor surface in this sweep** *(see [finding-2026-06-03-0001](finding-2026-06-03-0001.md))*

- Pointer only. MSTIC + Unit 42 + Socket cluster unchanged; two Tier-1 declinations on the Miasma extension still standing. Defender posture from prior briefs holds.
- Digraph **B1** (layered A1 procedural, A2 novel-TTP) unchanged.

## ✈️ Sector Focus: Aerospace & Defense

**Five Eyes "Safeguarding Our Secrets" joint counterintelligence advisory — cleared-personnel HUMINT recruitment via LinkedIn, front companies, virtual interviews** *(see [finding-2026-06-04-0002](finding-2026-06-04-0002.md))*

- **What.** [MI5 (lead), FBI, ASIO, CSIS, and NZSIS](https://www.mi5.gov.uk/) published the joint advisory on 2026-06-04. Attribution preserved verbatim: **"China's military intelligence services"** — generic PLA-linked, not a specific tracked actor. Tradecraft: LinkedIn outreach; front companies posing as consultancies, think tanks, or HR firms; virtual interviews probing role and unit; encrypted-messaging hand-off; $100s–$1000s per intelligence report.
- **A&D scope.** Named target set covers "Indo-Pacific stationed military" and "anyone with access to classified or privileged information," with "indirect or peripheral access" language extending to academics, journalists, think-tank staff. **DIB primes are not explicitly named** — relevance to cleared-personnel at A&D primes and Tier-2/3 suppliers is implicit but materially applicable. Tradecraft is consistent with the broad PLA HUMINT pattern, not specifically calibrated to A&D.
- **DIB A&D action — two leverage points, not substitutes.**
  - **FSO/DCSA partnership.** Circulate the advisory through standing insider-threat awareness channels; reinforce LinkedIn-approach reporting expectations for cleared personnel; coordinate with DCSA on unsolicited foreign-employer outreach matching the front-company pattern.
  - **HR / corporate-recruiter due diligence.** Front-company-as-recruiter tradecraft targets the recruiter-to-candidate interface. HR and Corporate Security should refresh foreign-influence vetting on senior-cleared roles, validate inbound recruiter identities against public consultancy/think-tank rolls, and flag virtual-interview probing on role and unit affiliation.
- *Archimedes preserves the verbatim attribution and does not upgrade to Volt Typhoon, Salt Typhoon, APT40, APT41, or any specific tracked actor.*
- Digraph **A2** · WEP **very likely** procedural / **likely** DIB cleared-personnel within implicit target scope / **unable to assess** specific A&D-prime targeting.

## 🕵️ Actor Activity

No new attributed campaigns in the reporting window. Gamaredon carry-over from 2026-06-02 afternoon stands; `/new-actor` scaffolding operator decision still pending.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors ([UNC1549 #004](threats/threat-actors/UNC1549/profile.md), [Charming Kitten #011](threats/threat-actors/Charming-Kitten/profile.md), Handala Hack #014, [MuddyWater #022](threats/threat-actors/MuddyWater/profile.md)) in 48h.

## 📰 Other Signal

- **Bitskrieg watch — June window day-4; researcher-claimed Secure Boot + BitLocker bypass.** No specific disclosure event in the PM sweep. Day five begins tomorrow. Monitoring tier only; AM action set holds.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR. Splunk first-party: indexes dormant on non-archimedes-internal stream (twelfth consecutive sweep); per Hard Rule 8, silence is not disconfirming.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-04.

🔓 **Vulnerabilities**

- **[Cisco Unified CM SSRF (CVE-2026-20230): public PoC, no ITW](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)** — Unauth SSRF-to-root, CVSS 8.6. **14-train fix 14SU6 out**; 15-train waits for September (TAC COP1). Third critical CUCM CVE in 11 months. *Patch 14-train at cleared-personnel voice estates today; segment 15-train until COP1.*

- **[HTTP/2 Bomb (CVE-2026-49975): Microsoft on-record; Cloudflare disputes Pingora patch](https://www.theregister.com/security/2026/06/04/openais-codex-chains-decade-old-dos-techniques-into-http/2-bomb/5251377)** — Microsoft: *"We are aware and actively investigating appropriate mitigations to help keep customers protected."* Cloudflare: existing DDoS mitigations cover it; no Pingora patch. *Watch Patch Tuesday June 10 for IIS; self-hosted Pingora — apply Calif's HTTP/2-disable or header-cap interim.*

- **CVE-2022-0492 Linux cgroups KEV closes tomorrow.** *Patch ≤ 5.16.x by EOD or deploy AppArmor/SELinux confinement.*
- **CVE-2026-45247 Mirasvit KEV Saturday (T-2).** AM action stands.

✈️ **Sector Focus: A&D**

- **[Five Eyes: PLA military intelligence running LinkedIn HUMINT against cleared personnel](https://www.mi5.gov.uk/)** — MI5/FBI/ASIO/CSIS/NZSIS published "Safeguarding Our Secrets" today; verbatim attribution: "China's military intelligence services." Tradecraft: LinkedIn outreach via front-company consultancies/think-tanks/HR firms, virtual interviews probing role/unit, encrypted-messaging hand-off, $100s–$1000s per report. Scope: "anyone with access to classified or privileged information" + Indo-Pacific stationed military. **DIB primes not named explicitly; implicit but materially applicable.** *Two levers, not substitutes: FSO/DCSA circulation AND HR/recruiter due diligence.*
