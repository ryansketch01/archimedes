---
raw_id: raw-2026-07-12-ratify-002
collected_at: 2026-07-12T14:45:00-04:00
run_id: ondemand-ratify-peach-sandstorm-20260712
collection_mode: on_demand
on_demand_command: dossier-ratification (collector direct-retrieval intake)
source:
  - source_yaml_id: microsoft-mstic
    source_name: Microsoft Threat Intelligence (Security Blog)
    source_url: https://www.microsoft.com/en-us/security/blog/2024/08/28/peach-sandstorm-deploys-new-custom-tickler-malware-in-long-running-intelligence-gathering-operations/
    published_at: 2024-08-28
    note: "Primary Microsoft blog; retrieved cleanly with full IOC appendix."
match_reason:
  watchlist: [aerospace-defense]
  actors: [Peach Sandstorm, APT33, Refined Kitten, HOLMIUM]
  vulnerabilities: []
  keywords: [Tickler, password spray, satellite, oil and gas, Yahsat, Azure C2, IRGC, LinkedIn]
triage_tags: [dossier_ratification, ad_sector, actor_peach_sandstorm_027, ioc_bearing]
iocs_extracted: true
iocs_count: 20
text_word_count: 1300
promoted: false
ttl_expires_at: 2026-10-10T14:45:00-04:00
admiralty_note: "Collector source-reliability read (advisory only): Microsoft MSTIC A1. Mandiant linkage sought but NOT located as a standalone A-grade Tickler report in this pass — see confirmation status below."
---

# Peach Sandstorm (APT33) Tickler backdoor + password-spray vs satellite / oil-and-gas / government / defense — Microsoft (Aug 28, 2024)

## Summary of retrievable reporting

Microsoft Threat Intelligence reported (Aug 28, 2024) that between **April and July 2024**, Peach Sandstorm deployed a new custom multi-stage backdoor named **Tickler** against organizations in the **satellite, communications equipment, oil and gas, and federal/state government** sectors in the **United States and the United Arab Emirates**. Microsoft attributes Peach Sandstorm to the Iranian **IRGC**.

Delivery followed **password-spray** attacks (ongoing since February 2023 across defense, space, education, and government sectors) and LinkedIn-based social engineering (operators masquerading as students, developers, and talent-acquisition managers). Tickler was staged in archives alongside decoy PDFs; one sample was named `YAHSAT NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20240421.pdf.exe` — a lure referencing UAE satellite operator **Yahsat**, directly corroborating the satellite-sector targeting. C2 ran on **fraudulent, attacker-controlled Azure subscriptions** (`*.azurewebsites.net`). Password-spray traffic used a `go-http-client` user agent. The two malicious DLLs act as fully functional backdoors supporting `systeminfo`, `dir`, `run`, `delete`, `interval`, `upload`, `download`.

## Priority-item confirmation

- **Tickler backdoor / password-spray vs defense/satellite/oil-and-gas (Microsoft, ~Aug 2024): CONFIRMED.** Microsoft Security Blog, 2024-08-28, full IOC appendix. April–July 2024 activity window. US + UAE, satellite/oil-and-gas/government/defense. A1.
- **Mandiant co-reporting on Tickler: NOT FOUND (as standalone A-grade Tickler report) in this retrieval pass.** The Aug-2024 Tickler disclosure that surfaced is Microsoft's; no independent Mandiant Tickler advisory was retrieved. Keep the "Mandiant" attribution flagged pending — Mandiant has historically co-reported APT33 password-spray/Azure activity, but this specific Tickler report is Microsoft-originated. Recommend the profiler cite Microsoft as the Tickler source and not co-credit Mandiant absent a retrievable Mandiant URL.

---

## Extraction notes

- Language: en
- Article type: vendor advisory (Microsoft Security Blog) with IOC appendix
- Raw IOC extraction invoked: yes
- Hard Rule 2: attribution to Peach Sandstorm/APT33/IRGC reported exactly as Microsoft states. Not originated.
- Hard Rule 3: no exploit/PoC content present or copied.

### VirusTotal sanity-check (collector enrichment)

- `7eb2e9e8cd450fc353323fd2e8b84fbbdfe061a8441fd71750250752c577d198` — VT: **49/69 malicious**, `type: Win32 EXE`, `meaningful_name: YAHSAT NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20240421.pdf.exe`, first submitted 2024-04-22 (inside Microsoft's window). MD5 `ea79d9e044c7daff1de15f95f49a0265`, SHA1 `fb4b1b9244a924015eb82296dbecf5fa2a861ba9`. Flagged by Microsoft, CrowdStrike, TrendMicro, Paloalto, Kaspersky, ESET, Symantec. The Yahsat-themed filename independently corroborates satellite-sector targeting.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: microsoft-mstic-tickler-2024-08
  source_url: https://www.microsoft.com/en-us/security/blog/2024/08/28/peach-sandstorm-deploys-new-custom-tickler-malware-in-long-running-intelligence-gathering-operations/
  extracted_at: 2026-07-12T14:45:00Z
  extracted_by: collector
  target_actor_id: "027"
  text_word_count: 1300

indicators:
  - id: peach-hash-7eb2e9e8cd45
    type: hash_sha256
    value: 7eb2e9e8cd450fc353323fd2e8b84fbbdfe061a8441fd71750250752c577d198
    role: delivery
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Tickler sample; VT name YAHSAT NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20240421.pdf.exe (Yahsat satellite lure)."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: "MD5 ea79d9e044c7daff1de15f95f49a0265"
  - id: peach-hash-ccb617cc7418
    type: hash_sha256
    value: ccb617cc7418a3b22179e00d21db26754666979b4c4f34c7fda8c0082d08cec4
    role: delivery
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Tickler malware sample (Microsoft IOC appendix)."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: null
  - id: peach-hash-fb70ff49411c
    type: hash_sha256
    value: fb70ff49411ce04951895977acfc06fa468e4aa504676dedeb40ba5cea76f37f
    role: staging
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Associated Tickler payload."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: null
  - id: peach-hash-711d3deccc22
    type: hash_sha256
    value: 711d3deccc22f5acfd3a41b8c8defb111db0f2b474febdc7f20a468f67db0350
    role: staging
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Associated Tickler payload."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: null
  - id: peach-hash-5df4269998ed
    type: hash_sha256
    value: 5df4269998ed79fbc997766303759768ce89ff1412550b35ff32e85db3c1f57b
    role: staging
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Associated Tickler payload."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: null
  - id: peach-hash-dad53a786627
    type: hash_sha256
    value: dad53a78662707d182cdb230e999ef6effc0b259def31c196c51cc3e8c42a9b8
    role: staging
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Legitimate msvcp140.dll abused for DLL sideloading."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: "Abused legit binary (msvcp140.dll) — sideloading host, not malicious file itself."
  - id: peach-hash-56ac00856b19
    type: hash_sha256
    value: 56ac00856b19b41bc388ecf749eb4651369e7ced0529e9bf422284070de457b6
    role: staging
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "LoggingPlatform.dll used in sideloading chain (backdoor DLL)."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: null
  - id: peach-hash-22017c9b022e
    type: hash_sha256
    value: 22017c9b022e6f2560fee7d544a83ea9e3d85abee367f2f20b3b0448691fe2d4
    role: staging
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Legitimate vcruntime140.dll abused for DLL sideloading."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: "Abused legit binary."
  - id: peach-hash-e984d9085ae1
    type: hash_sha256
    value: e984d9085ae1b1b0849199d883d05efbccc92242b1546aeca8afd4b1868c54f5
    role: staging
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Microsoft.SharePoint.NativeMessaging.exe used in sideloading chain."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: null
  - id: peach-domain-subreviews-azure
    type: domain
    value: subreviews.azurewebsites.net
    role: c2
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Fraudulent attacker-controlled Azure C2."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: "One of 16 azurewebsites.net C2 subdomains in Microsoft appendix (full list in body)."
  - id: peach-domain-satellite2-azure
    type: domain
    value: satellite2.azurewebsites.net
    role: c2
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Fraudulent Azure C2 (satellite-themed subdomain)."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: null
  - id: peach-domain-satellitegardens-azure
    type: domain
    value: satellitegardens.azurewebsites.net
    role: c2
    first_seen: 2024-04
    last_seen: 2024-07
    campaign: "Tickler"
    related_malware: [Tickler]
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "Fraudulent Azure C2 (satellite-themed)."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: null
  - id: peach-ua-go-http-client
    type: user_agent
    value: "go-http-client"
    role: spray
    first_seen: 2023-02
    last_seen: 2024-07
    campaign: "Peach Sandstorm password spray"
    related_malware: []
    source_brief: microsoft-mstic-tickler-2024-08
    context_excerpt: "User agent observed in password-spray traffic."
    attribution_in_text: "Peach Sandstorm / APT33"
    notes: "Low-fidelity IOC (generic Go HTTP client UA); contextual only."

# Full azurewebsites.net C2 list (Microsoft appendix), recorded in body for grader/profiler:
#   subreviews, satellite2, nodetestservers, satellitegardens, softwareservicesupport,
#   getservicessuports, getservicessupports, getsupportsservices, satellitespecialists,
#   satservicesdev, servicessupports, websupportprotection, supportsoftwarecenter,
#   centersoftwaresupports, softwareservicesupports, getsdervicessupoortss  (all .azurewebsites.net)

attribution_claims:
  - claimed_actor: "Peach Sandstorm (APT33)"
    ioc_ids:
      - peach-hash-7eb2e9e8cd45
      - peach-hash-ccb617cc7418
      - peach-domain-subreviews-azure
      - peach-domain-satellite2-azure
    claimed_by_source: microsoft-mstic-tickler-2024-08
    attribution_confidence_in_source: high
    requires_grading: true

benign_filtered:
  - value: azurewebsites.net
    reason: "parent service domain is benign; specific attacker subdomains ARE the IOCs (not filtered)"
  - value: microsoft.com
    reason: reference_site

extraction_warnings:
  - type: abused_legitimate_binary
    ioc_id: peach-hash-dad53a786627
    detail: "msvcp140.dll and vcruntime140.dll are legitimate Microsoft binaries abused as sideloading hosts; hashes are the specific abused copies, not the malicious payload itself. Grader should tag role accordingly."
  - type: low_fidelity_ioc
    ioc_id: peach-ua-go-http-client
    detail: "Generic Go HTTP client user agent — contextual, high false-positive risk if used standalone."
```
