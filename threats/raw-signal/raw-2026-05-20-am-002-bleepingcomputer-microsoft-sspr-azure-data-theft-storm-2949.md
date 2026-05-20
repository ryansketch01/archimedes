---
raw_id: raw-2026-05-20-am-002
collected_at: 2026-05-20T07:33:00-04:00
run_id: pre-brief-20260520-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer (Bill Toulas) — relay of Microsoft Security Blog (2026-05-18)"
  source_url: https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/
  published_at: 2026-05-19T19:35:32-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords:
    - Storm-2949
    - Microsoft 365
    - Azure production environments
    - Self-Service Password Reset SSPR
    - MFA manipulation
    - Microsoft Graph API enumeration
    - OneDrive SharePoint exfil
    - Azure RBAC exploitation
    - Key Vault credential theft
    - ScreenConnect remote access tool
    - Defender protection disablement
    - OAuth privilege escalation
    - production cloud environment intrusion
triage_tags:
  - in_window
  - microsoft_security_blog_a_grade_originating_2026_05_18
  - bleepingcomputer_b_grade_relay
  - storm_2949_microsoft_temporary_designation_not_in_roster
  - storm_actor_class_unattributed_until_classified
  - non_flash_no_tracked_actor_no_named_ad_victim
  - non_flash_no_cve_no_active_exploitation_per_se_TTP_campaign_class
  - ad_relevance_structural_indirect_m365_azure_universal_in_ad_tier_1
  - grader_queue_candidate_tradecraft_relevance
  - mstic_indirectly_corroborated_via_bleepingcomputer_relay
  - splunk_first_party_zero_hits_48th_consecutive_dormant_sweep
  - hard_rule_2_attribution_origination_compliance_storm_designation_preserved
  - hard_rule_7_quote_limit_compliance
  - ttp_evolution_oauth_m365_azure_attack_class
iocs_extracted: true
iocs_count: 0
text_word_count: 720
promoted: true
promoted_to_finding: finding-2026-05-20-0002
promoted_at: 2026-05-20T07:55:00-04:00
grading_run_id: morning-20260520-080000
ttl_expires_at: 2026-08-18T07:33:00-04:00
test: false
---

# BleepingComputer — Microsoft Self-Service Password Reset abused in Azure data-theft attacks (Storm-2949)

## Source surface

**Author:** Bill Toulas (BleepingComputer)
**URL:** https://www.bleepingcomputer.com/news/security/microsoft-self-service-password-reset-abused-in-azure-data-theft-attacks/
**Published:** 2026-05-19T19:35:32 EDT (in-window: 2026-05-19 15:30 → 2026-05-20 07:30)
**Originating primary:** Microsoft Security Blog 2026-05-18 (B-grade relay of A-grade vendor disclosure)
**Source grade:** B (BleepingComputer); originating MSTIC A-grade per source-grades.yaml

## Summary (verbatim claims only, ≤15 word quotes)

- Microsoft tracks the threat actor as **Storm-2949** — Microsoft's standard "temporary designation for threat activity that has yet to be classified" framing preserved verbatim per Hard Rule 2.
- Storm-2949 is **NOT in `_roster.yaml`** (verified via grep across `threats/threat-actors/`). This is a Microsoft-only naming; no Mandiant / CrowdStrike / Unit 42 / MSTIC formal aliases yet.
- Target environment class: Microsoft 365 + Azure production environments.
- Attack tradecraft (TTP enumeration from BleepingComputer summary):
  1. Social engineering targeting privileged users (initial vector).
  2. Self-Service Password Reset (SSPR) abuse with MFA manipulation.
  3. Microsoft Graph API enumeration for environment discovery.
  4. OneDrive + SharePoint data exfiltration.
  5. Azure RBAC exploitation for privilege escalation.
  6. Key Vault credential theft.
  7. ScreenConnect remote access tool deployment.
  8. Defender protection disablement.
- **Zero named victim organizations.** Article references "one instance" but provides no organizational identifiers.
- **Zero published IOCs** in this primary surface — no email/UPN patterns, OAuth app names, IPs, or domains disclosed by Microsoft or relayed by BleepingComputer.

## A&D-sector filter outcome

**No A&D primes named.** No watchlist entity (Lockheed, Boeing, RTX, Northrop, GD, BAE, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit) named as victim.

**A&D-relevance: structural-indirect.** Every A&D Tier-1/Tier-2 contractor uses Microsoft 365 + Azure for productivity and CI/CD; SSPR + MFA + Graph API + Key Vault + Defender are universally-deployed control surfaces. The Storm-2949 tradecraft is fully portable into any A&D Tier-1 M365/Azure tenant. Detection-relevance is high; targeting-specificity is null.

Per Hard Rule 2, Archimedes does not extrapolate A&D-prime exposure from generic-targeting Microsoft research.

## Roster check

- Storm-2949: NOT in `_roster.yaml` (24 actors current). Microsoft "Storm" designation is by definition pre-classification — could later be re-attributed to a tracked actor (e.g., Scattered Spider #013, Octo Tempest alias has SSPR/MFA-fatigue tradecraft track record per pre-2026 reporting; Charming Kitten #011 has OAuth/M365 tradecraft per CrowdStrike + MSTIC A1 attribution chain in finding-2026-05-05-0002 lineage).
- **No `_roster.yaml` write triggered this surface** (Hard Rule 2: only the actor-profiler creates roster entries; collector only matches).
- **Awareness flag for orchestrator:** Storm-2949 is a candidate for `/new-actor` evaluation if subsequent A-grade reporting cross-corroborates the cluster or if Microsoft re-classifies to a named threat actor with A&D-relevant TTP overlap.

## Trigger evaluation

### Trigger 1 — critical CVE + active exploitation + A-grade
- No CVE cited. SSPR / Graph / Key Vault / RBAC / Defender abuse is misuse-of-legitimate-features class, not a vulnerability with a CVSS score.
- **Does NOT fire.**

### Trigger 2 — new attribution for tracked actor
- Storm-2949 not in roster.
- **Does NOT fire.**

### Trigger 3 — first-party Splunk IOC hit
- Splunk query (-24h) on Storm-2949 / SSPR / Self-Service Password Reset / Azure data theft tokens returned zero non-Archimedes-internal events. 48th consecutive dormant non-self-telemetry sweep.
- **Does NOT fire.**

### Trigger 4 — tracked actor TTP change
- Tracked actor attributable: FAIL (Storm-2949 not in roster).
- **Does NOT fire** (the TTP set is otherwise an exemplar of OAuth/M365 tradecraft that Charming Kitten and Scattered Spider have used in pre-2026 reporting — but this surface does NOT attribute to those actors).

### Trigger 5 — A&D-sector multi-victim active campaign
- Multi-victim claim ambiguous (Microsoft cites "one instance"; campaign-class framing is implicit not explicit).
- A&D-sector named: NO.
- **Does NOT fire.**

### Trigger 6 — zero-day no patch + CVSS≥8.0 + exploitation confirmed/imminent
- No CVE, no patch dimension. Misuse-of-feature class.
- **Does NOT fire.**

### Critical override
- Zero of four conditions met. Override does NOT apply.

## Disposition recommendation

Grader queue (non-FLASH). Tradecraft-relevance to A&D environments is high enough to warrant brief inclusion if the briefer has slot capacity, but no FLASH trigger fires. The actionable angle for A&D defenders: SSPR + MFA-manipulation + Graph-API-enumeration + OneDrive/SharePoint-exfil + Key-Vault-credential-theft + Defender-disablement is a 7-step tradecraft chain that maps cleanly to A&D M365 environments. Detection coverage on each step is a productive analyst task downstream of this raw-signal.

---

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas (BleepingComputer)
- Article type: blog (B-grade media relay)
- Originating primary: Microsoft Security Blog (A-grade) 2026-05-18
- Raw IOC extraction invoked: yes — zero IOCs published in primary or relay
- Splunk first-party: zero hits over -24h on Storm-2949 / SSPR / Azure-data-theft tokens
- Hard Rule 2 attribution-origination compliance: Microsoft "Storm-2949" temporary designation preserved verbatim; not upgraded
- Hard Rule 7 quote-limit compliance: each direct quote ≤ 15 words

## IOCs (from ioc-extraction skill)

```yaml
iocs: []
attribution_claims:
  - actor: Storm-2949
    nation: unknown
    service: null
    claim_source: Microsoft Security Blog (2026-05-18) — relayed by BleepingComputer (Bill Toulas) 2026-05-19T19:35:32 EDT
    microsoft_designation_class: "temporary designation for threat activity that has yet to be classified"
    in_roster: false
    awareness_flag_for_orchestrator: "Candidate /new-actor evaluation if subsequent A-grade reporting cross-corroborates the cluster or Microsoft re-classifies to named actor"
    new_or_restatement: NEW Storm-named cluster (not in corpus)
ttps_observed:
  - "Social engineering targeting privileged users"
  - "Self-Service Password Reset (SSPR) abuse with MFA manipulation"
  - "Microsoft Graph API enumeration"
  - "OneDrive + SharePoint data exfiltration"
  - "Azure RBAC exploitation"
  - "Key Vault credential theft"
  - "ScreenConnect remote access tool deployment"
  - "Defender protection disablement"
ttp_chain_a_d_relevance:
  ad_prime_named: false
  ad_relevance_class: structural_indirect_m365_azure_universal
  detection_value_high_targeting_specificity_null: true
```
