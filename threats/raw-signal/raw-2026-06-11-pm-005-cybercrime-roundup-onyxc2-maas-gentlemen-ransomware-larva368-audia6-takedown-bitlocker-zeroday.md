---
raw_id: raw-2026-06-11-pm-005
collected_at: 2026-06-11T16:00:00-04:00
run_id: pre-brief-20260611-153000
collection_mode: pre_brief_collection
sources:
  - source_yaml_id: securityweek
    source_name: SecurityWeek (OnyxC2)
    source_url: https://www.securityweek.com/onyxc2-stealer-offers-cybercriminals-enterprise-grade-theft-for-250-a-month/
    grade: B
    published_at: 2026-06-11T13:00:00-04:00
  - source_yaml_id: securityaffairs
    source_name: Security Affairs (OnyxC2)
    source_url: https://securityaffairs.com/193523/malware/onyxc2-malware-as-a-service-offers-enterprise-grade-data-theft.html
    grade: B
    published_at: 2026-06-11T14:22:21-04:00
  - source_yaml_id: thehackernews
    source_name: The Hacker News (Gentlemen Ransomware)
    source_url: https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html
    grade: B
    published_at: 2026-06-11T16:50:47-04:00
  - source_yaml_id: bleepingcomputer
    source_name: BleepingComputer (AudiA6 takedown)
    source_url: https://www.bleepingcomputer.com/news/legal/authorities-dismantle-audia6-ransomware-crypto-laundering-service/
    grade: B
    published_at: 2026-06-11T15:55:41-04:00
  - source_yaml_id: theregister
    source_name: The Register (Nightmare Eclipse GreatXML BitLocker bypass)
    source_url: https://www.theregister.com/security/2026/06/11/nightmare-eclipse-drops-claimed-bitlocker-bypass-for-microsoft-windows/5254371
    grade: B
    published_at: 2026-06-11T17:51:52-04:00
  - source_yaml_id: thehackernews
    source_name: The Hacker News (GreatXML BitLocker bypass)
    source_url: https://thehackernews.com/2026/06/new-greatxml-exploit-bypasses-windows.html
    grade: B
    published_at: 2026-06-11T17:43:52-04:00
match_reason:
  watchlist: [aerospace-defense]
  actors: ["LockBit (#015 in roster)", "Qilin (NOT in roster)", "Medusa (NOT in roster)", "Nightmare Eclipse (NOT in roster — researcher / leak actor)"]
  vulnerabilities: [GreatXML BitLocker bypass — unassigned CVE]
  keywords: [OnyxC2, Gentlemen Ransomware, LARVA-368, Phantom Mantis, Storm-2697, AudiA6, Nightmare Eclipse, BitLocker, MSNightmare]
triage_tags:
  - cybercrime_threat_landscape_cluster
  - lockbit_roster_actor_indirect_mention
  - maas_commoditization_signal
  - ransomware_operator_indictment
  - microsoft_unpatched_disclosure_threatened_drop
  - non_flash_cluster
iocs_extracted: true
iocs_count: 1
text_word_count: 1200
promoted: true
promoted_to_findings:
  - finding-2026-06-11-0009   # Gentlemen Ransomware / PRODAFT / Microsoft Storm-2697 material extension
  - finding-2026-06-11-0010   # OnyxC2 MaaS
  - finding-2026-06-11-0011   # AudiA6 takedown
  - finding-2026-06-11-0012   # Nightmare Eclipse GreatXML
promoted_at: 2026-06-11T17:35:00-04:00
promotion_decomposition_note: "Multi-claim raw-signal decomposed into 4 separate findings per admiralty-grading skill Step 2 multi-claim halt + decomposition rule"
ttl_expires_at: 2026-09-09T16:00:00-04:00
---

# Cybercrime + threat-landscape cluster — OnyxC2 MaaS, Gentlemen Ransomware (Phantom Mantis / Storm-2697), AudiA6 takedown, GreatXML BitLocker bypass

## Why bundled

Four lower-individual-priority but cluster-relevant cybercrime / threat-landscape items in the afternoon window. Bundling avoids raw-signal-file proliferation while preserving searchable provenance. Each is non-FLASH; collectively they describe today's cybercrime tempo for the briefer's threat-landscape watch line.

---

## (1) OnyxC2 MaaS stealer — BlackFog research

- **Originator:** BlackFog researchers (vendor-tier research, B-grade by current posture)
- **Pricing:** $250/month standard, $500/month premium (HVNC), $6,000 source-code purchase
- **Targets:** 210+ applications including 37 Chromium + 8 Gecko browsers, 95 Chromium + 14 Gecko extensions (6 dedicated 2FA, 5 password managers), 17 crypto wallets, 11 FTP, 5 email, plus VPN / RDP / messaging / gaming clients
- **Evasion:** AES-256 encrypted payloads, DLL sideloading (malicious DLL disguised as NVIDIA library), in-memory execution, legitimate-signature wrapper application
- **VirusTotal posture:** Zero detections across 71 engines on initial upload (verified 2026-05-30 per BlackFog)
- **Lure installers bundled:** FinePrint, SystemSettings, fake Windows updates, Fling-Standalone gaming installers
- **Persistence:** Designed for prolonged foothold; converts one workstation into ongoing visibility into browsers + password managers + 2FA tokens + email + FTP + VPN credentials + crypto wallets
- **A&D relevance:** None named. MaaS commoditization → lower barrier for credential-theft against any enterprise including DIB workforce; indirect / watch-list signal only.

## (2) The Gentlemen Ransomware — PRODAFT (tracked as Phantom Mantis) / Microsoft (tracked as Storm-2697)

- **Victim count claimed:** 478
- **Worm-like spread:** `--spread` argument flag converts single-host encryptor into self-propagating worm
- **Operator named:** LARVA-368 = **Alexander Andreevich Yapaev**, 36, Izhevsk, Russia (per PRODAFT)
- **Operator history:** Previously operated under alias ArmCorp; transitioned from RaaS affiliate to independent operator July 2025
- **Prior affiliate relationships per PRODAFT:** **LockBit (aka Tenacious Mantis)**, **Qilin (aka Pestilent Mantis)**, **Medusa (aka Venomous Mantis)**
- **Technical:** Go binary with Garble obfuscation; X25519 key exchange + XChaCha20 encryption; Windows / Linux / ESXi / LVM targeting; 2–6 week dwell time
- **Geographic distribution:** Only ~13% U.S.-based; majority Thailand / UK / Brazil / Germany / India
- **Roster crosswalk:** LockBit IS in Archimedes roster (#015, HIGH). Qilin and Medusa are NOT in roster. The "Yapaev / ArmCorp / LARVA-368 / Phantom Mantis / Storm-2697 / The Gentlemen" attribution chain involves a former LockBit affiliate now independent — relevant to ongoing LockBit dossier upkeep (last-reviewed 2026-04-11, next-review-due 2026-07-10).
- **A&D relevance:** No defense-sector targeting per source. Watch-list signal only.

## (3) AudiA6 crypto-laundering takedown — Europol-coordinated 11-country op

- **Scale:** >$380M laundered 2022–2025
- **Linked investigations:** 15+ international ransomware investigations
- **Mechanism:** Posed as cryptocurrency mixing service; 3–10% commission; 1-hour turnaround
- **Arrests:** 2 — Ruslan Igorevich Tkachuk (37, Ukrainian), Alexander Vladimirovich Ledenev (25, Russian); detained in Georgia; up to 20 years each; also charged with administering "Dark2Web" forum
- **Prior arrest 2025-09:** Polish authorities arrested a separate Ukrainian national linked to AudiA6
- **Seizures:** 25 domains, €86,000 in crypto seized, €692,000 in crypto frozen, 80 vehicles/properties seized, Telegram accounts blocked
- **Ransomware groups named explicitly:** None — only "more than 15 distinct international investigations of ransomware attacks"
- **A&D relevance:** Indirect — ransomware-economy disruption reduces general operational tempo against any victim including DIB.

## (4) Nightmare Eclipse — GreatXML BitLocker bypass (unpatched zero-day disclosure)

- **Researcher:** Nightmare Eclipse / MSNightmare (Chaotic Eclipse alias) — prolific Microsoft-grudge zero-day discloser; some researchers speculate ex-Microsoft employee
- **Vulnerability:** Claimed BitLocker bypass via Recovery partition XML files
- **Mechanism per researcher:** Copy `unattend.xml` + `Recovery` directory to recovery partition; reboot into WinRE via Shift-click Restart → "shell with unrestricted access to the bitlocker volume"
- **Precondition:** Windows Defender Offline Scan must have run at some point in the past
- **Total zero-day count for this researcher in this disclosure series:** 8 (RedSun, UnDefend, BlueHammer, YellowKey, GreenPlasma, MiniPlasma — patched in June 2026 Patch Tuesday; RoguePlanet and GreatXML — currently unpatched)
- **Microsoft posture:** Confirmed investigating RoguePlanet; "none of the vulnerabilities were reported via its official channels prior to being made public"; banned researcher's GitHub account
- **Independent reproduction:** Will Dormann tested GreatXML and called the writeup "flawed" — could not reproduce; says preconditions (logged-in admin to initiate Defender Offline scan) negate the bypass value
- **CVE assignment:** None yet
- **A&D relevance:** Workstation full-disk-encryption integrity is a DIB CMMC L2/L3 control. Unpatched BitLocker bypasses warrant operator awareness even when researcher-reproduction is contested.

### FLASH evaluation for GreatXML
- Trigger 6 (zero-day-no-patch):
  - Vulnerability disclosed without patch: yes (claimed).
  - CVSS ≥ 8.0: not assigned (no CVE; no CVSS).
  - Widely deployed product: yes — BitLocker.
  - Exploitation confirmed or imminent per A-grade: NO — disclosed via Blogger / GitHub by single researcher; reproduction contested by Will Dormann; Microsoft "actively investigating validity"; no A-grade ITW attestation.
- **Does not satisfy Trigger 6** (no A-grade exploitation confirmation; contested reproduction).
- Cumulative researcher pattern (8 disclosed bugs, 6 patched, 2 outstanding, ongoing public-grudge campaign) warrants operator awareness as a sustained Microsoft-product-security drama, not a FLASH.

## Multi-source convergence for OnyxC2 procedural facts

| Source | Grade | Procedural fact |
|---|---|---|
| SecurityWeek | B | BlackFog research origination, $250 pricing tier, 210+ app target list |
| Security Affairs | B | Same BlackFog origination, identical pricing, evasion details, persistence framing |

Two B-grade media sources independently relay BlackFog research; treat OnyxC2 facts as B-grade-corroborated through publisher-independent relay, anchoring on BlackFog vendor-tier underneath.

## Extraction notes

- Language: en
- Article type: 4 distinct media stories bundled
- Raw IOC extraction invoked: yes — 1 IOC (LARVA-368 individual-attribution alias)

## IOCs (from ioc-extraction skill)

```yaml
iocs: []

attribution_claims:
  - actor: The Gentlemen Ransomware / LARVA-368 / Phantom Mantis / Storm-2697 / ArmCorp
    real_name_alleged: Alexander Andreevich Yapaev (36, Izhevsk, Russia)
    source: thehackernews relaying PRODAFT (2026-06-11)
    affiliate_history: Previously affiliated with LockBit, Qilin, Medusa
    independent_corroboration: true (Microsoft Storm-2697 tracking corroborates PRODAFT Phantom Mantis)
    grade_at_attribution_layer: A2 (PRODAFT + Microsoft independent attribution at originator layer, B-grade media relay above)
    archimedes_attribution_origination_check: pass_per_hard_rule_2
    roster_actor_crosswalk: LockBit (#015) affiliate history surface — not a roster-promotion trigger by itself
  - vendor: BlackFog
    claim: "OnyxC2 sold $250/month, persistent credential-theft MaaS"
    source: securityweek + securityaffairs (2026-06-11)
    independent_corroboration: true (two publisher-independent B-grade relays of same BlackFog research)
  - subject: Denis Obrezko — separate case, see raw-2026-06-11-pm-003
  - subject: Ruslan Igorevich Tkachuk + Alexander Vladimirovich Ledenev (AudiA6)
    nationality: Ukrainian + Russian
    arrest_location: Georgia (2026 charging)
    charges: Cybercrime money laundering + Dark2Web forum admin
    source: bleepingcomputer (2026-06-11)
    independent_corroboration: false_at_collector_layer_b_grade_single_relay
    archimedes_attribution_origination_check: pass_per_hard_rule_2
  - researcher: Nightmare Eclipse / MSNightmare / Chaotic Eclipse
    disclosure: GreatXML BitLocker bypass (unassigned CVE)
    source: theregister + thehackernews (2026-06-11)
    reproduction_contested_by: Will Dormann
    independent_corroboration: true_for_disclosure_event_false_for_validity_of_exploit
    microsoft_posture: investigating_RoguePlanet_no_comment_yet_on_GreatXML

extraction_skill_status: ok
```
