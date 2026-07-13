---
raw_id: raw-2026-07-12-ratify-003
collected_at: 2026-07-12T15:00:00-04:00
run_id: ondemand-ratify-apt34-20260712
collection_mode: on_demand
on_demand_command: dossier-ratification (collector direct-retrieval intake)
source:
  - source_yaml_id: trendmicro-research
    source_name: Trend Micro Research
    source_url: https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html
    published_at: 2024-10-11
    note: "Primary Trend Micro report (Earth Simnavaz = APT34). Direct WebFetch 403'd (Trend Micro blocks automated fetch); content confirmed via WebSearch summary of the Trend Micro page + independent relays (cybersecuritynews, Dark Reading, SOC Prime, Industrial Cyber). Full IOC appendix NOT retrievable this pass."
  - source_yaml_id: cybersecuritynews
    source_name: Cyber Security News (relay of Trend Micro)
    source_url: https://cybersecuritynews.com/oilrig-hackers-microsoft-exchange-breach/
    published_at: 2024-10-14
    note: "Secondary relay; retrieved cleanly. Provided psgfilter.dll password-filter DLL detail + RunPE-In-Memory technique."
match_reason:
  watchlist: [aerospace-defense]
  actors: [APT34, OilRig, Earth Simnavaz, Helix Kitten, Crambus, Hazel Sandstorm]
  vulnerabilities: [CVE-2024-30088]
  keywords: [StealHook, Exchange, password filter DLL, ngrok, Gulf, UAE, MOIS]
triage_tags: [dossier_ratification, actor_apt34_023, ioc_bearing, cve_referenced]
iocs_extracted: true
iocs_count: 2
text_word_count: 900
promoted: false
ttl_expires_at: 2026-10-10T15:00:00-04:00
admiralty_note: "Collector source-reliability read (advisory only): Trend Micro Research A1 (primary originator). cybersecuritynews C3 (pure relay — NOT independent corroboration). Dark Reading / SOC Prime / Industrial Cyber additional relays. Ratifies training-knowledge dossier items against a live A-grade primary."
---

# APT34 (OilRig) 'Earth Simnavaz' campaign — StealHook backdoor, CVE-2024-30088 privesc, malicious password-filter DLL — Trend Micro (Oct 2024)

## Summary of retrievable reporting

Trend Micro Research disclosed (Oct 2024, "Earth Simnavaz (aka APT34) Levies Advanced Cyberattacks Against Middle East") that the Iranian MOIS-linked actor **APT34** (OilRig / Earth Simnavaz / Helix Kitten / Crambus) ran a cyber-espionage campaign against **UAE and wider Gulf** government and energy organizations. Trend Micro attributes the activity to APT34.

Key TTPs reported:
- Initial access via a **web shell** uploaded to a vulnerable web server; then downloaded **ngrok** to tunnel and reach the Domain Controller.
- **CVE-2024-30088** (Windows Kernel elevation-of-privilege) exploited for privilege escalation, delivered via a RunPE-In-Memory loading technique. (CVE cited by ID only — Hard Rule 3, no exploit detail collected.)
- A malicious **password-filter DLL** (`psgfilter.dll`) registered with the Local Security Authority to intercept plaintext credentials during LSA validation — MITRE **T1556.002** (Modify Authentication Process: Password Filter DLL).
- **StealHook** backdoor: retrieves stolen credentials and **exfiltrates data as email attachments through compromised (government) Microsoft Exchange servers** to an attacker-controlled address.

## Priority-item confirmation

- **Earth Simnavaz campaign (Trend Micro, ~Oct 2024) vs UAE/Gulf gov + energy: CONFIRMED.** Trend Micro Research, Oct 2024. A1 primary. (Direct page fetch blocked; confirmed via WebSearch extraction of the Trend Micro page itself + multiple independent relays.)
- **StealHook backdoor (Exchange credential relay/theft): CONFIRMED.** Trend Micro, Oct 2024 — StealHook exfiltrates via Exchange as email attachments. A1.
- **CVE-2024-30088 (Windows kernel privesc) used by APT34: CONFIRMED (linkage exists in reporting).** Trend Micro links CVE-2024-30088 to Earth Simnavaz/APT34 for privilege escalation. ID recorded only; no exploit content. A1.
- **Malicious password-filter DLL (T1556.002): CONFIRMED.** `psgfilter.dll` registered with LSA to harvest plaintext passwords. A1 (Trend Micro), technique-named in relay reporting.
- **2025–2026 OilRig/Crambus activity + fresh IOCs: PARTIALLY confirmed / mostly NOT retrievable as A-grade primary this pass.** Secondary/forecast sources (Brandefense, noorstream, Hedgehog) describe continued 2025 energy/defense targeting in Europe + Middle East via compromised M365/Azure, and Check Point / Dark Reading / The Record reported 2024–2025 APT34 espionage vs Iraqi government (8-month dwell) and Yemen. These are worth a dedicated follow-up retrieval; treat 2025-2026 claims as PENDING until a Check Point / Trend Micro / Mandiant primary URL is pulled. No fresh 2025-2026 hashes/domains retrieved.

## Retrievable IOCs

Trend Micro's full IOC appendix (hashes, C2 domains, exfil email addresses) was **not retrievable** this pass — the Trend Micro pages (US/AU) and Dark Reading / Industrial Cyber all returned HTTP 403 to automated fetch. The one durable, publicly-restated indicator is the password-filter DLL filename `psgfilter.dll`. Recommend a follow-up manual pull of the Trend Micro appendix (or SOC Prime / OTX pulse) to harvest StealHook hashes + C2 for the dossier iocs.yaml.

---

## Extraction notes

- Language: en
- Article type: vendor research report (Trend Micro, primary) + secondary relays
- Hard Rule 2: attribution to APT34/MOIS reported exactly as Trend Micro states. Not originated. No merge to Cavern Manticore (#026) or any peer — CPR's separately-noted OilRig/Lyceum tactical overlap stays CPR's assessment only.
- Hard Rule 3: CVE-2024-30088 recorded by ID only; NO exploit/PoC/technical exploitation detail collected or copied.
- Hard Rule 7: no victim credentials surfaced in retrieved content (the password-filter DLL is described as a capability; no harvested credential values were present to discard).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: trendmicro-earth-simnavaz-2024-10
  source_url: https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html
  extracted_at: 2026-07-12T15:00:00Z
  extracted_by: collector
  target_actor_id: "023"
  text_word_count: 900

indicators:
  - id: apt34-cve-2024-30088
    type: cve
    value: CVE-2024-30088
    defanged_original: null
    first_seen: 2024-10
    last_seen: 2024-10
    role: ambiguous
    campaign: "Earth Simnavaz"
    related_malware: [StealHook]
    source_brief: trendmicro-earth-simnavaz-2024-10
    context_excerpt: "Windows Kernel EoP used by APT34 for privilege escalation (ID only; no exploit detail per Hard Rule 3)."
    attribution_in_text: "APT34 / Earth Simnavaz"
    notes: "Linkage confirmation is the deliverable, not exploitation mechanics."
  - id: apt34-filename-psgfilter-dll
    type: other
    type_detail: filename
    value: psgfilter.dll
    defanged_original: null
    first_seen: 2024-10
    last_seen: 2024-10
    role: persistence
    campaign: "Earth Simnavaz"
    related_malware: [StealHook]
    source_brief: trendmicro-earth-simnavaz-2024-10
    context_excerpt: "Malicious password-filter DLL registered with LSA to intercept plaintext passwords (MITRE T1556.002)."
    attribution_in_text: "APT34 / Earth Simnavaz"
    notes: "Filename per relay reporting; confirm against Trend Micro appendix on follow-up."

attribution_claims:
  - claimed_actor: "APT34 (OilRig / Earth Simnavaz)"
    ioc_ids:
      - apt34-cve-2024-30088
      - apt34-filename-psgfilter-dll
    claimed_by_source: trendmicro-earth-simnavaz-2024-10
    attribution_confidence_in_source: high
    requires_grading: true

benign_filtered:
  - value: trendmicro.com
    reason: reference_site
  - value: microsoft.com
    reason: reference_site

extraction_warnings:
  - type: ioc_appendix_not_retrieved
    ioc_id: null
    detail: "Trend Micro full IOC appendix (StealHook hashes, C2 domains, exfil email) blocked by 403. Only psgfilter.dll + CVE-2024-30088 durably captured. Follow-up manual/OTX pull recommended before folding hashes into iocs.yaml."
  - type: relay_not_corroboration
    ioc_id: null
    detail: "cybersecuritynews / Dark Reading / SOC Prime / Industrial Cyber are relays of the single Trend Micro primary, NOT independent corroboration. Grader: single-A-grade-origin, apply single-source handling."
```
