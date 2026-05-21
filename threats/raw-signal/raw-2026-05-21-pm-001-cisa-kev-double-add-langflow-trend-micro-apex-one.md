---
raw_id: raw-2026-05-21-pm-001
collected_at: 2026-05-21T15:34:00-04:00
run_id: pre-brief-20260521-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: cisa-kev
  source_name: "CISA Known Exploited Vulnerabilities Catalog"
  source_url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  published_at: 2026-05-21T00:00:00-04:00
  source_grade: A
sweep_window:
  start: 2026-05-21T08:00:00-04:00
  end: 2026-05-21T15:30:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities:
    - CVE-2025-34291                # Langflow CORS/SameSite refresh-token RCE
    - CVE-2026-34926                # Trend Micro Apex One on-premise directory traversal
  keywords:
    - kev_double_add_2026_05_21
    - langflow_ai_orchestration_platform
    - cors_samesite_refresh_token_rce
    - trend_micro_apex_one_on_premise
    - directory_traversal_pre_auth_local
    - cisa_kev_actively_exploited
    - federal_civilian_deadline_2026_06_04
    - a_and_d_tier_2_3_edr_deployment
triage_tags:
  - kev_addition
  - federal_civilian_deadline
  - trend_micro_apex_one_a_and_d_relevance
  - langflow_ai_orchestration_attack_surface
  - active_exploitation_implied_by_kev_inclusion
iocs_extracted: false
iocs_count: 0
text_word_count: 480
promoted: true
promoted_to_finding: finding-2026-05-21-0008
promoted_at: 2026-05-21T16:08:00-04:00
ttl_expires_at: 2026-08-19T15:34:00-04:00
---

# CISA KEV double-add 2026-05-21 — CVE-2025-34291 (Langflow) + CVE-2026-34926 (Trend Micro Apex One on-premise)

## Source extraction

**Endpoint**: `cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` (WebFetch, JSON catalog).

**Catalog state at sweep time**: 2 entries with `dateAdded: 2026-05-21`. Three most recent dateAdded buckets: 2026-05-21 (2 entries), 2026-05-20 (8 entries — the Defender + Watchguard + Sophos batch already covered in morning brief), 2026-05-15 (1 entry).

---

## Entry 1 — CVE-2025-34291 (Langflow)

- **vendorProject**: Langflow
- **product**: Langflow
- **vulnerabilityName**: Langflow Origin Validation Error Vulnerability
- **dateAdded**: 2026-05-21
- **shortDescription** (verbatim): "Langflow contains an origin validation error vulnerability in which an overly permissive CORS configuration combined with a refresh token cookie configured as SameSite=None allows a malicious webpage to perform cross-origin requests that include credentials and successfully call the refresh endpoint. This could allow the attacker to execute arbitrary code and achieve full system compromise via obtained tokens that permit access to authenticated endpoints."
- **requiredAction**: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use.
- **dueDate**: 2026-06-04
- **knownRansomwareCampaignUse**: Unknown
- **CWE**: CWE-346 (Origin Validation Error)
- **References**: Langflow GitHub repo + v1.9.3 release tag + issue #11465 + NVD CVE-2025-34291 record
- **Patched version**: 1.9.3 (per release-tag reference)

**Product context**: Langflow is an open-source low-code AI agent / LLM orchestration platform (visual flow builder for LangChain/LangGraph workflows). Deployed by enterprises building internal AI-agent pipelines.

**A&D relevance**: Tier-2 — primes and DIB Tier-1 suppliers building internal AI-agent / LLM-orchestration platforms may run Langflow. Federal-civilian KEV deadline 2026-06-04 (BOD 22-01).

**CVSS**: Not provided in KEV record. NVD record will carry the score.

---

## Entry 2 — CVE-2026-34926 (Trend Micro Apex One on-premise)

- **vendorProject**: Trend Micro
- **product**: Apex One
- **vulnerabilityName**: Trend Micro Apex One (On-Premise) Directory Traversal Vulnerability
- **dateAdded**: 2026-05-21
- **shortDescription** (verbatim): "Trend Micro Apex One (on-premise) contains a directory traversal vulnerability that could allow a pre-authenticated local attacker to modify a key table on the server to inject malicious code to deploy to agents on affected installations."
- **requiredAction**: Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance, or discontinue use.
- **dueDate**: 2026-06-04
- **knownRansomwareCampaignUse**: Unknown
- **CWE**: CWE-23 (Relative Path Traversal)
- **References**: Trend Micro KA-0023430 success article + NVD record

**Product context**: Trend Micro Apex One is the on-premise version of Trend's enterprise EDR/AV product. Widely deployed across DIB Tier-2/3 supplier estates (where Trend has historical mid-market and SMB-government penetration). Pre-auth-local-attacker requirement narrows blast radius (attacker needs initial-access foothold) but server-side key-table modification → agent payload deployment makes this a high-impact post-compromise pivot — turns the EDR control plane into a malware distribution mechanism for all endpoints managed by that Apex One server.

**A&D relevance**: Tier-1 direct. Trend Micro Apex One is a known enterprise-EDR fixture across DIB Tier-2/3 estates. KEV inclusion implies active exploitation observed by CISA (KEV catalog inclusion criterion). Federal-civilian deadline 2026-06-04.

**CVSS**: Not provided in KEV record.

---

## Cross-finding correlation

This is the SECOND KEV double-add event in two days — 2026-05-20 was an 8-entry batch (Microsoft Defender pair UnDefend/RedSun + Watchguard + Sophos + 4 others), and 2026-05-21 is a 2-entry batch. CISA cadence on KEV adds elevated above historical baseline (1-3 per week typical, 10 entries in 36h is notable).

The Trend Micro Apex One entry pairs operationally with the morning brief's Microsoft Defender pair: both are enterprise-EDR control-plane abuses (Defender pair = LPE + DoS-Defender; Trend Apex One = post-auth path-traversal + agent malware deployment). Adversaries are demonstrating systematic targeting of EDR control planes across vendors. **Cross-vendor pattern, not vendor-specific bug.**

## Extraction notes

- Language: en
- Article type: structured-data (JSON catalog)
- Raw IOC extraction invoked: no (no IOCs in KEV entries beyond CVE IDs themselves; vendor patch URLs not IOCs)
- Source: A-grade (CISA-KEV authoritative)
- KEV cadence-anomaly flag: 10 KEV adds in 36h crosses ~3x historical baseline — worth grader awareness for cross-finding pattern recognition
