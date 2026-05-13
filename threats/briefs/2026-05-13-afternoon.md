---
brief_id: 2026-05-13-afternoon
brief_type: afternoon
published_at: 2026-05-13T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
analyst_review: archimedes-analyst (finding-2026-05-13-0004 SAT-ACH + SAT-KAC on KongTuke attribution and Octo Tempest tradecraft-similarity framing; finding-2026-05-13-0003 analyst review not required at WEP "likely")
red_team_review: not_required (no findings at WEP "very likely" or higher)
human_override: null
findings_referenced:
  - finding-2026-05-13-0001          # carry-forward UPDATE anti-noise; covered in 0800 morning brief
  - finding-2026-05-13-0002          # carry-forward UPDATE anti-noise; covered in 0800 morning brief
  - finding-2026-05-13-FLASH-0001    # carry-forward UPDATE anti-noise; covered in 14:30 FLASH
  - finding-2026-05-13-0003          # NEW — BitLocker YellowKey + GreenPlasma zero-day PoCs
  - finding-2026-05-13-0004          # NEW — KongTuke ModeloRAT campaign via Microsoft Teams + CVE-2023-36036
related_actors_referenced:
  - actor_id: "010"
    actor_name: Salt Typhoon
    alias_cited_in_source: FamousSparrow
    treatment: covered_in_14_30_flash_carry_forward_only_no_new_development
  - actor_id: "013"
    actor_name: Scattered Spider
    aliases: [UNC3944, Octo Tempest, 0ktapus]
    treatment: tradecraft_similarity_referenced_by_rapid7_NOT_attributed_to_april_2026_intrusion
related_vulns_referenced:
  - cve: CVE-2023-36036
    product: "Windows Cloud Files Mini Filter Driver (cldflt.sys)"
    class: heap_buffer_overflow_lpe
    cvss_v3: 7.8
    kev_listed: true
    kev_date_added: 2023-11
    role: n_day_weaponized_april_2026_per_rapid7_ir
  - name: YellowKey
    cve: null
    class: bitlocker_bypass_via_winre_ntfs_transactions
    patch_status: unpatched
    public_poc: github.com/Nightmare-Eclipse/YellowKey
  - name: GreenPlasma
    cve: null
    class: ctfmon_arbitrary_section_creation_lpe
    patch_status: unpatched
    public_poc: github.com/Nightmare-Eclipse/GreenPlasma
related_campaigns_referenced:
  - name: KongTuke_ModeloRAT_April_2026
    actor_per_source: KongTuke
    actor_confidence_per_source: moderate_to_high
    source: rapid7
new_actor_candidate_flagged:
  - name: KongTuke
    flagged_by: rapid7
    operator_review_required: true
    candidacy_open_question: |
      Whether KongTuke is a discrete actor or a tooling / access-broker
      cluster — Rapid7 references prior documentation by "multiple
      vendors" without naming them. Analyst surfaced this as a
      non-blocking precondition for /new-actor scaffolding.
flash_absorption:
  - flash_id: flash-2026-05-13-1430
    finding_id: finding-2026-05-13-FLASH-0001
    treatment: carry_forward_reference_only_no_new_development_since_14_30_post
hard_rule_2_framings_load_bearing:
  - "Rapid7 attributes the April 2026 intrusion to KongTuke at moderate-to-high confidence — Archimedes does not collapse to 'Rapid7 confirms' or 'Archimedes assesses'"
  - "Rapid7 observes Octo Tempest tradecraft similarity on the Microsoft Teams 'fake IT Support' pattern — similarity is NOT attribution; do not write 'linked to Scattered Spider' or 'Scattered Spider-adjacent'"
  - "KongTuke /new-actor candidacy carries open question (discrete actor vs tooling / access-broker cluster); single-source-with-tentative-prior-lineage framing preserved"
  - "Bitdefender attributes the Azerbaijani campaign to FamousSparrow at moderate-to-high confidence — Archimedes does not originate; FamousSparrow → Salt Typhoon alias is pre-existing in _roster.yaml"
  - "BleepingComputer is the single B-grade media source on YellowKey + GreenPlasma; no MSRC advisory, no CVE assigned, no Tier-1 vendor research; the BlueHammer / RedSun lineage-class pattern is B-grade editorial framing, not A-grade ITW attestation"
hard_rule_8_first_party_splunk:
  status: clean_at_compose
  query_window: -30d
  indexes_queried: [archimedes, defenseclaw_local]
  tokens_kongtuke: ["ModeloRAT", "KongTuke", "cldflt.sys", "PLURIBUS", "ssss.dll", "com6848.dll", "13 C2 IPs from Rapid7 publication"]
  tokens_bitlocker: ["BitLocker", "YellowKey", "GreenPlasma", "cldflt", "WinRE", "Nightmare-Eclipse", "Chaotic Eclipse"]
  hits_on_in_scope_iocs: 0
  consecutive_dormant_sweeps: 21
  framing: silence_is_not_disconfirming_no_first_party_observation_to_bump_external_claim_in_either_direction
word_count: 780
tlp: CLEAR
test: false
---

# Afternoon Brief — 2026-05-13

**[Rapid7 disclosed an April 2026 enterprise intrusion chaining a Microsoft Teams fake-IT-Support call → ModeloRAT DLL deployment → CVE-2023-36036 LPE → WinRM lateral movement → credential dumping → web-service exfiltration, attributing it to **KongTuke** at moderate-to-high confidence.](https://www.rapid7.com/blog/post/dissecting-a-modelorat-campaign-from-microsoft-teams-to-compromise/)** Rapid7 separately notes the Teams pattern resembles tradecraft documented for [Octo Tempest / Scattered Spider / UNC3944](../threat-actors/_roster.yaml) — similarity is not attribution of this intrusion to Scattered Spider.

**Why it matters:** Teams external messaging is widely enabled across DIB tenants; the same vector is reachable by anyone whose federation policy permits unauthenticated external chat or call invites. CVE-2023-36036 has been KEV-listed since November 2023 — n-day weaponization 2+ years post-patch confirms unpatched Windows endpoints remain in-scope.

---

## 🚨 Active Threats

**[Rapid7 IR: April 2026 intrusion chains Teams fake-IT-Support call → ModeloRAT → CVE-2023-36036 LPE; Rapid7 attributes to KongTuke at moderate-to-high confidence.](https://www.rapid7.com/blog/post/dissecting-a-modelorat-campaign-from-microsoft-teams-to-compromise/)** A Teams call posing as IT Support delivers a malicious DLL pair (`ssss.dll` + `com6848.dll`) loading **ModeloRAT** (Python-compiled); the actor weaponizes [CVE-2023-36036 (cldflt.sys, CVSS 7.8, KEV-listed November 2023)](https://nvd.nist.gov/vuln/detail/CVE-2023-36036) for SYSTEM, persists via the **PLURIBUS** sync-provider GUID, moves laterally over WinRM, dumps credentials, and exfiltrates over web services. Rapid7 publishes **13 C2 IPs, 2 SHA-256 hashes, and 1 persistence GUID** plus a 9-technique MITRE ATT&CK map. The Teams pattern resembles tradecraft documented for [Octo Tempest / Scattered Spider / UNC3944 (Actor #013)](../threat-actors/_roster.yaml); Rapid7 does not attribute this intrusion to Scattered Spider — the pattern is widely reused post-2023. **KongTuke is not in `_roster.yaml`**; single-source veto applies, WEP capped at "likely". **Action for DIB Teams owners:** audit external-messaging policy today (allow-list federated domains, alert on first-time external invites), verify CVE-2023-36036 patched fleet-wide, and ingest Rapid7's 16 IOCs into EDR / SIEM with a -30d retrospective sweep. Digraph: A3 · WEP: likely · finding-2026-05-13-0004.

## 🔓 Vulnerabilities

**[Pseudonymous researcher Chaotic Eclipse (GitHub: Nightmare-Eclipse) released PoCs for two undisclosed Windows zero-days — YellowKey (BitLocker bypass via NTFS-transaction manipulation in WinRE) and GreenPlasma (CTFMON arbitrary memory-section LPE). No CVE, no patch.](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)** BleepingComputer (Bill Toulas) is the single B-grade media source; no MSRC advisory, no CISA KEV addition, no Tier-1 vendor research. Microsoft acknowledged the report with no timeline. **YellowKey** defeats TPM-only BitLocker via crafted FsTx files on USB or the EFI partition plus CTRL-during-boot in WinRE; original-device only (stolen drives are not decrypted). The researcher claims TPM+PIN is also exploitable; no PoC published for that variant. **GreenPlasma** targets CTFMON section creation in SYSTEM-writable directories; published PoC is incomplete. BleepingComputer ties both to prior leaked classes [BlueHammer (CVE-2026-33825, ZD-001)](../vulnerabilities/_index.yaml) and [RedSun (ZD-002)](../vulnerabilities/_index.yaml) — editorial framing, not A-grade ITW attestation for YellowKey or GreenPlasma specifically. The threat model is **physical-access / supply-chain / evil-maid / SCIF re-entry, not remote**. **Action for DIB endpoint owners:** evaluate TPM+PIN on traveler / SCIF laptops where TPM-only is deployed; verify BIOS / UEFI passwords on the same fleet; review supply-chain integrity on pre-loaded devices; track MSRC + KEV over 7–14 days. Digraph: B3 · WEP: likely · finding-2026-05-13-0003.

**Carryover (no new development this afternoon):** [CVE-2026-40361 Outlook zero-click UAF](./2026-05-13-morning.md) — patch deployment active, no PoC / KEV / Tier-1 follow-on. Fortinet FortiSandbox CVE-2026-26083 + FortiAuthenticator CVE-2026-44277, and CISA ICS-26-132 (ABB AC500 V3 CVE-2025-15467 + five) — [2026-05-12 afternoon](./2026-05-12-afternoon.md), no n-day / PoC / KEV addition.

## ✈️ Sector Focus: Aerospace & Defense

No A&D prime is named today. The Teams fake-IT-Support vector is universal across [aerospace-defense watchlist](../../infrastructure/watchlists/aerospace-defense.yaml) M365 estates; the BitLocker YellowKey threat model maps to traveler / SCIF re-entry / supply-chain-pre-load programs at every prime issuing encrypted Windows endpoints to engineers operating outside controlled spaces. Operative question: **is Teams external messaging on by default for your tenants, and what is the response runbook when an unsolicited IT-Support external call surfaces?**

## 🕵️ Actor Activity

🔗 **Update on 14:30 FLASH:** [Bitdefender attributes the December 2025 → February 2026 multi-wave Exchange intrusion against an Azerbaijani oil and gas company to FamousSparrow (a [Salt Typhoon, Actor #010](../threat-actors/_roster.yaml) alias) at moderate-to-high confidence](./2026-05-13-flash-1430-famoussparrow-salt-typhoon-azerbaijan-energy.md). No new development since 14:30 EDT; cross-corroboration watch open through 2026-05-16. Energy sector, not on the A&D watchlist; structural relevance via South Caucasus energy's NATO-adjacent posture.

**KongTuke** (per Rapid7 above) is **not in [`_roster.yaml`](../threat-actors/_roster.yaml)** and is flagged as a `/new-actor` candidate pending operator review. The candidacy carries an open question Archimedes will not collapse: whether KongTuke is a discrete actor or a tooling / access-broker cluster. Rapid7 anchors the designation to unnamed prior vendor research; the analyst-queued lineage test is a precondition for scaffolding.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors ([UNC1549](../threat-actors/UNC1549/profile.md), [Charming Kitten](../threat-actors/Charming-Kitten/profile.md), Handala Hack, [MuddyWater](../threat-actors/MuddyWater/profile.md)) in the last 48h.

## 📰 Other Signal

**First-party Splunk:** Clean across `archimedes` and `defenseclaw_local` over -30d on the full IOC set from both new findings (Rapid7's 13 C2 IPs + ModeloRAT / KongTuke / PLURIBUS / cldflt.sys tokens; BitLocker / YellowKey / GreenPlasma / Nightmare-Eclipse tokens). 21st consecutive dormant non-archimedes-internal sweep. Per Hard Rule 8, silence is not disconfirming.

**Watch ahead (next 24–72h):** Tier-1 prior-research catalog for KongTuke / ModeloRAT (`/new-actor` precondition); cross-corroboration on the [FamousSparrow attribution](./2026-05-13-flash-1430-famoussparrow-salt-typhoon-azerbaijan-energy.md); MSRC advisory + CVE assignment for YellowKey / GreenPlasma; CISA KEV addition; Tier-1 post-Patch-Tuesday exploitation publication on CVE-2026-40361; Nitrogen leak-site sample-data naming an A&D prime; Foxconn IR disclosure of initial-access vector or IOCs.

---

*Sources hyperlinked inline. Admiralty digraph and WEP noted per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-05-13.

🚨 **Active Threats**

• **[Rapid7 IR: Teams fake-IT-Support → ModeloRAT → CVE-2023-36036 LPE; attributed to KongTuke](https://www.rapid7.com/blog/post/dissecting-a-modelorat-campaign-from-microsoft-teams-to-compromise/)** — Rapid7 attributes the April 2026 intrusion to **KongTuke** at moderate-to-high confidence and publishes 13 C2 IPs, 2 hashes, and 1 persistence GUID. The Teams pattern resembles **Octo Tempest / Scattered Spider** tradecraft per Rapid7 — but Rapid7 does **not** attribute this intrusion to Scattered Spider. KongTuke is not yet in Archimedes's roster; analyst queued a prior-research lineage test. **DIB Teams owners:** *audit external-messaging policy and patch CVE-2023-36036 fleet-wide right now*.

🔓 **Vulnerabilities**

• **[BitLocker YellowKey + Windows LPE GreenPlasma — PoCs, no patch, no CVE](https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/)** — A pseudonymous researcher published PoCs Wednesday May 13. **YellowKey** defeats TPM-only BitLocker via NTFS transactions in WinRE; original-device only. **GreenPlasma** is a CTFMON LPE; PoC incomplete. BleepingComputer is the only B-grade source; Microsoft acknowledged with no timeline. Threat model is physical-access, not remote. **Endpoint owners:** evaluate TPM+PIN on traveler / SCIF laptops; verify BIOS passwords.

🕵️ **Actor Activity**

• **[14:30 FLASH update](./2026-05-13-flash-1430-famoussparrow-salt-typhoon-azerbaijan-energy.md)** — No new development since Bitdefender's FamousSparrow / Salt Typhoon attribution on the Azerbaijani oil and gas intrusion. Cross-corroboration watch through May 16.

🔓 **Carryover** — [CVE-2026-40361 Outlook zero-click](./2026-05-13-morning.md): patch deployment active; no PoC, KEV, or Tier-1 follow-on.
