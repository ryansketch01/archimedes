---
raw_id: raw-2026-05-13-pm-002
collected_at: 2026-05-13T15:38:00-04:00
run_id: pre-brief-20260513-153000
collection_mode: pre_brief_collection
sweep_type: pre_brief
sweep_time: 2026-05-13T15:30:00-04:00
time_window_start: 2026-05-13T07:30:00-04:00
time_window_end: 2026-05-13T15:30:00-04:00
test: false
source:
  source_yaml_id: rapid7
  source_name: Rapid7 (provisional A per source-grades.yaml; awaiting human ratification)
  source_url: https://www.rapid7.com/blog/post/tr-it-support-dissecting-modelorat-campaign-microsoft-teams-compromise
  source_byline: Anna Sirokova
  published_at: 2026-05-13T14:44:02+00:00     # 10:44 EDT, inside afternoon pre-brief window
  fetched_via: fetch_feed + WebFetch
  fetched_at: 2026-05-13T15:37:00-04:00
secondary_sources_via_websearch_or_extraction_notes:
  - source_id: prior_kongtuke_modelorat_vendor_research_lineage
    role: rapid7_cites_prior_documentation_by_multiple_vendors
    grade_class: not_named_in_article
    note: |
      Rapid7 article frames KongTuke / ModeloRAT attribution as "based
      on previous documentation by multiple vendors" but does not name
      those vendors in the body. Grader should treat the KongTuke
      attribution as Rapid7-relayed-from-prior-research rather than
      Rapid7-originated. Unit 42 / Proofpoint / SentinelLabs have
      published prior KongTuke / ClickFix research; this Rapid7 piece
      may be citing those lineage vendors without explicit attribution
      in the body.
  - source_id: octo_tempest_scattered_spider_unc3944_tradecraft_referenced
    role: tradecraft_similarity_observation_not_attribution
    note: |
      Rapid7 explicitly notes the "fake IT Support via Microsoft Teams"
      social-engineering pattern as Octo Tempest / Scattered Spider /
      UNC3944 tradecraft. Scattered Spider IS in _roster.yaml (#013;
      aliases include UNC3944, Octo Tempest, 0ktapus, Scatter Swine,
      Muddled Libra, Starfraud). Rapid7 does NOT attribute this
      intrusion to Scattered Spider — the framing is tradecraft-similar-
      to-Octo-Tempest, with Rapid7's attribution landing on KongTuke /
      ModeloRAT. This is an important grader distinction: Trigger 4
      (tracked-actor-ttp-change) requires "attributable_actor in
      _roster.yaml" — KongTuke is NOT in the roster, only Scattered
      Spider via UNC3944/Octo-Tempest alias chain. Tradecraft-similarity
      is NOT actor-attribution.
match_reason:
  watchlist: []
  watchlist_match_strength: structural_via_microsoft_teams_universal_enterprise_deployment_dib_relevance
  actors:
    - kongtuke                                   # Rapid7's attribution; NOT in _roster.yaml
    - octo_tempest_tradecraft_referenced         # alias of Scattered Spider #013 — referenced, NOT attributed
    - scattered_spider_unc3944_alias_chain       # roster #013; tradecraft-similarity only
  vulnerabilities:
    - cve_2023_36036                              # Windows Cloud Files Mini Filter Driver (cldflt.sys) heap buffer overflow LPE; previously KEV; weaponized in this intrusion
  keywords:
    - microsoft_teams_fake_it_support_social_engineering
    - modelorat_framework_python_dll_beacon
    - kongtuke_threat_cluster_rapid7_attribution
    - octo_tempest_scattered_spider_tradecraft_similarity
    - cve_2023_36036_cldflt_sys_lpe_weaponized_in_intrusion
    - winrm_lateral_movement_t1021_006
    - python_pyinstaller_compiled_payloads
    - socks5_proxy_pluribus_persistence
    - pluribus_sync_provider_registry_persistence
    - cloudflare_workers_dot_dev_staging
    - powershell_python_living_off_the_land_chain
    - april_2026_incident_investigation
triage_tags:
  - tracked_actor_tradecraft_similarity_not_attribution
  - kongtuke_new_actor_candidate_for_operator_review
  - flash_trigger_4_marginal_fail_attribution_to_non_roster_actor
  - cve_2023_36036_kev_already_listed_class_n_day_weaponization
  - microsoft_teams_attack_surface_structural_dib_relevance
  - moderate_to_high_confidence_attribution_per_rapid7
  - single_intrusion_not_multi_victim_campaign
  - non_flash_grader_queue_item_pm_afternoon_brief_eligible
  - rich_ioc_set_grader_priority
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    matched: false
    rationale: |
      CVE-2023-36036 is a 2-year-old already-KEV-listed LPE; this
      intrusion weaponizes the n-day rather than disclosing a 0day.
      Trigger 1 typically frames around fresh CVE disclosures with
      active exploitation; an n-day weaponization within an already-
      attributed campaign cluster is more naturally a Trigger 4
      candidate. Active exploitation: TRUE (Rapid7 IR observation).
      CVSS: CVE-2023-36036 7.8 (under the 9.0 threshold) — Trigger 1
      FAILS on cvss_score>=9.0.
  trigger_2_tracked_actor_attribution:
    matched: false
    rationale: |
      Attribution is to KongTuke (NOT in _roster.yaml). Octo Tempest /
      Scattered Spider tradecraft is referenced as similarity, NOT as
      attribution. Trigger 2 requires "attributed_actor in
      _roster.yaml". FAILS on attribution-to-non-roster-actor.
      KongTuke is flagged as a potential /new-actor candidate for
      operator review.
  trigger_3_first_party_ioc_hit:
    matched: false
    rationale: |
      Splunk archimedes + defenseclaw_local indices searched over -30d
      against the IOC set in this raw-signal — ZERO events. Tested
      tokens: ModeloRAT, KongTuke, cldflt.sys, PLURIBUS, "fake IT
      Support", ssss.dll, com6848.dll, 46.225.231.170, 144.172.99.68,
      64.94.85.158, 140.82.6.45, 45.76.241.51, 87.120.186.229,
      149.248.78.202, 144.172.88.18, 64.190.113.187, 45.59.122.231,
      96.9.125.29, 144.172.111.49, 104.194.152.246. Twentieth
      consecutive dormant non-archimedes-internal stream sweep.
  trigger_4_tracked_actor_ttp_change:
    matched: marginal_fail
    rationale: |
      source_grade: A (Rapid7 provisional A — provides high-fidelity
      IR research with first-party telemetry). attributable: ambiguous
      — Rapid7 attributes to KongTuke (NOT in roster) and references
      Octo Tempest / Scattered Spider tradecraft similarity. ttp_delta:
      TRUE if the operator-grader treats KongTuke + Octo-Tempest-
      tradecraft cluster as effectively-Scattered-Spider-adjacent; FALSE
      if strict-attribution rule applies (KongTuke != Scattered Spider).
      Conservative read: Trigger 4 FAILS on strict attribution; flag for
      grader as TTP-similarity material useful for /update-tracking
      Scattered Spider next review.
  trigger_5_ad_sector_campaign:
    matched: false
    rationale: |
      Single intrusion. NOT multi-victim campaign per Rapid7's framing
      ("an enterprise intrusion that ... illustrates a critical risk").
      No A&D prime named as victim. Trigger 5 FAILS on multi_victim
      AND ad_sector_targeted both not-confirmed.
  trigger_6_zero_day_no_patch:
    matched: false
    rationale: |
      CVE-2023-36036 patched November 2023; on KEV catalog. N-day, not
      0day. Trigger 6 FAILS on patch_available=true.
  net: NON-FLASH. Grader-queue item for 2026-05-13 16:00 afternoon brief.
grader_disposition_recommendation: |
  Two possible grader dispositions:

  (A) Promote to fresh standalone finding in 2026-05-13 afternoon brief
      "Actor Activity" or "Other Signal" section, with explicit framing:
      - KongTuke = NEW actor cluster, flagged for operator /new-actor
        review (not currently in _roster.yaml).
      - Scattered Spider (#013) / Octo Tempest tradecraft REFERENCED,
        NOT ATTRIBUTED — per Hard Rule 2 Archimedes does not originate
        attribution; we report Rapid7's framing.
      - CVE-2023-36036 already-KEV n-day weaponization datapoint
        useful for vulnerability-tracker corpus.
      - IOC set (15+ C2 IPs + 2 file hashes + PLURIBUS persistence)
        is grader-priority for first-party Splunk pivoting and
        defensive-rule generation.
      - Single intrusion, NOT multi-victim — frame at WEP "possible"
        for campaign breadth, NOT "likely" or higher.

  (B) Queue as input to /update-tracking on Scattered Spider (#013) for
      next routine actor-review cycle, in case the orchestrator wants
      to refresh Scattered Spider's TTP-fidelity given Rapid7's
      tradecraft-similarity observation here. NOT urgent; multi-week
      timeframe acceptable.

  Recommend BOTH: ship as afternoon-brief item AND queue for
  Scattered Spider refresh tracking.

  Forward watch:
    - Independent Tier-1 vendor corroboration on KongTuke cluster
      (Unit 42, Proofpoint, SentinelLabs, Mandiant, CrowdStrike
      naming + clustering analysis).
    - Additional KongTuke intrusions confirming multi-victim campaign
      class — would upgrade to Trigger 5 candidacy if multiple primes
      or DIB orgs reported.
    - Microsoft Teams hardening guidance from MSRC / Microsoft
      Defender team in response to the tradecraft pattern.
copyright_compliance:
  - quote_count: 1_quote_from_rapid7
  - quote_word_count: 13_words_under_15_word_cap
  - paraphrase_majority: true
iocs_extracted: true
iocs_count: 17                                 # 15 C2 IPs + 2 file hashes
iocs_count_breakdown:
  c2_ips_modelorat_beacon: 5
  c2_ips_internal_py_microsoft5237: 2
  c2_ips_tcp_shell: 3
  c2_ips_socks5_proxy: 3
  file_hashes_sha256: 2
  registry_persistence_artifacts: 1            # PLURIBUS sync provider GUID
  mitre_attack_techniques: 9                   # T1566.003, T1059.001, T1059.006, T1068, T1053.005, T1056.002, T1003, T1021.006, T1567.002
text_word_count_full_capture: 487              # synthesized from Rapid7 body via WebFetch
promoted: true
promoted_to_finding: finding-2026-05-13-0004
promoted_at: 2026-05-13T16:14:00-04:00
promoted_by_run_id: afternoon-20260513-160000
promoted_disposition: action_item_tier_a3_single_source_rapid7_a_grade_provisional_with_kongtuke_novel_to_corpus_attribution_single_source_veto_wep_likely_analyst_review_required_new_actor_candidate_flagged_scattered_spider_update_tracking_input
ttl_expires_at: 2026-08-11T15:38:00-04:00     # 90 days per LEGAL-POLICY retention
---

# When IT Support Calls — ModeloRAT Campaign from Microsoft Teams to Domain Compromise (Rapid7 2026-05-13 10:44 EDT)

## Source

- **Outlet:** Rapid7 (provisional A per source-grades.yaml; awaiting human ratification per source-grade-log 2026-05-06 entry)
- **URL:** https://www.rapid7.com/blog/post/tr-it-support-dissecting-modelorat-campaign-microsoft-teams-compromise
- **Byline:** Anna Sirokova
- **Published:** 2026-05-13T14:44:02Z (10:44 EDT, inside 8h afternoon pre-brief window)
- **Type:** Rapid7 Labs IR case writeup (first-party incident response telemetry)

## Synthesized body (extraction notes — not verbatim Rapid7 copy)

Rapid7's IR practice investigated an April 2026 enterprise intrusion that exemplifies a complete chain from initial-access social engineering to full domain compromise:

**Initial access — Microsoft Teams "fake IT Support" social engineering.** An external Teams message from an account impersonating "IT Support" reached the target user. Rapid7 explicitly frames this pattern as **Octo Tempest / Scattered Spider / UNC3944 tradecraft** but attributes THIS specific intrusion to **KongTuke**, a cluster Rapid7 cites as "previously documented by multiple vendors" (vendors not named in the body). The piece notes confidence-of-attribution as **moderate-to-high**.

**Initial payload — ModeloRAT framework.** Two key Python-compiled DLL payloads deployed via PowerShell + Python LotL chain:
- `ssss.dll` — SHA256 `b00c1cbcfb98d2618a5c2ccb311da94f3c57709a397be6c8de29839f4e943976`
- `com6848.dll` — SHA256 `30e5a6c982396cdf3157195b540f75096869baa8570f66fab88c07c161be27f0`

**Persistence — PLURIBUS sync provider.** Registry-level persistence via a custom sync provider with GUID `{904EE598-0511-4664-82A8-22C4A7501044}`.

**Privilege escalation — CVE-2023-36036 weaponization.** Windows Cloud Files Mini Filter Driver (`cldflt.sys`) heap buffer overflow LPE. **This CVE was added to CISA KEV at original disclosure (November 2023)** — this intrusion is an n-day weaponization of an already-published, already-KEV'd, already-patched vulnerability against an unpatched target. CVSS v3.1 7.8 (under Trigger 1's 9.0 threshold; that's why Trigger 1 doesn't fire even with active exploitation confirmed).

**Lateral movement — WinRM** (T1021.006).

**Credential access — credential dumping** (T1003).

**Exfiltration — web service exfiltration** (T1567.002).

**Full MITRE ATT&CK technique map (9 techniques):**
- T1566.003 — Spearphishing via Service (Microsoft Teams external messaging)
- T1059.001 — PowerShell
- T1059.006 — Python
- T1068 — Exploitation for Privilege Escalation (CVE-2023-36036)
- T1053.005 — Scheduled Task / Job: Scheduled Task
- T1056.002 — Input Capture: GUI Input Capture
- T1003 — OS Credential Dumping
- T1021.006 — Remote Services: Windows Remote Management
- T1567.002 — Exfiltration Over Web Service: Exfiltration to Cloud Storage

## Extraction notes — A&D / DIB structural relevance

This intrusion is NOT attributed to an A&D-prime victim, but the attack-surface pattern is universally relevant to the Archimedes target profile:

1. **Microsoft Teams "fake IT Support" external messaging is a cross-DIB attack vector.** Every prime on aerospace-defense.yaml deploys M365 with Teams; external Teams access is on by default in many tenant configurations; the social-engineering pattern (impersonate-as-internal-IT) succeeds without exploit code.
2. **CVE-2023-36036 KEV-listed but n-day-weaponizable.** This is the same class of risk that the corpus has tracked across CVE-2023-23397 Outlook NTLM, CVE-2024-21413 MonikerLink, and other n-day Microsoft component vulnerabilities — "patched 2 years ago" does NOT mean "deployed across the DIB 2 years ago." Vuln-tracker should verify CVE-2023-36036 patch deployment status across primes if any first-party data layer exists.
3. **Scattered Spider (#013) tradecraft adjacency.** Per _roster.yaml, Scattered Spider is currently tracked with aliases including UNC3944, Octo Tempest, 0ktapus, Scatter Swine, Muddled Libra, Starfraud. Rapid7's tradecraft-similarity framing is grader-actionable input for the actor-profiler's next /update-tracking cycle on #013.

## Extraction notes — KongTuke as /new-actor candidate

KongTuke is NOT in _roster.yaml. Per /new-actor workflow (per `.claude/commands/new-actor.md`), criteria for new-actor scaffolding include:
- Independent vendor attribution from 2+ Tier-1 sources, OR
- Single-source A-grade attribution with technical IOC support sufficient to enable detection-rule generation.

Rapid7's piece is a single A-grade source on KongTuke with substantial IOC support; the bar for /new-actor scaffolding is approachable. Flag for operator review.

## Extraction notes — FLASH trigger evaluation

This raw-signal sits at **Trigger 4 marginal-fail** on the strict attribution rule (KongTuke not in roster). All other triggers FAIL cleanly per the frontmatter rationale. **Net: NON-FLASH**, grader-queue for 2026-05-13 afternoon brief.

Operator-actionable framings for the briefer:
- Microsoft Teams "fake IT Support" external-messaging tradecraft is a DIB-relevant attack surface, even when the named actor is not in the roster.
- CVE-2023-36036 n-day weaponization is a useful datapoint for the Vulnerabilities section's KEV-vintage-tracking.
- Scattered Spider (#013) /update-tracking refresh has additional input material.

## Extraction notes — Splunk first-party check

`(index=archimedes OR index=defenseclaw_local) earliest=-30d (ModeloRAT OR KongTuke OR cldflt.sys OR PLURIBUS OR ssss.dll OR com6848.dll OR "46.225.231.170" OR "144.172.99.68" OR "64.94.85.158" OR "140.82.6.45" OR "45.76.241.51" OR "87.120.186.229" OR "149.248.78.202" OR "144.172.88.18" OR "64.190.113.187" OR "45.59.122.231" OR "96.9.125.29" OR "144.172.111.49" OR "104.194.152.246") NOT sourcetype=archimedes:*` returned **0 events** — no first-party telemetry hits on any of the 17 IOCs. Twentieth consecutive dormant non-archimedes-internal stream sweep. Trigger 3 cannot fire on a dormant stream.

## Extraction notes — Hard Rules compliance

- **Hard Rule 2 (no attribution origination):** Compliant. KongTuke attribution is per Rapid7; Octo Tempest / Scattered Spider tradecraft-similarity is per Rapid7. Archimedes does not originate either.
- **Hard Rule 3 (no exploitation, ever):** Compliant. CVE-2023-36036 weaponization is recorded as a fact-of-the-intrusion; no PoC reproduction. Rapid7's MITRE ATT&CK technique enumeration is grader-actionable defensive context, not offensive reproduction.
- **Hard Rule 4 (never scan third parties):** Compliant — no scanning conducted. Splunk queries are first-party only.
- **Hard Rule 6 (15-word quote limit, one per source):** Compliant — one Rapid7 quote captured (13 words): "Collaboration tools are part of your attack surface. Attackers used Teams to reach users directly."
- **Hard Rule 7 (credentials are radioactive):** N/A — Rapid7 piece describes credential dumping technique but does not surface specific credentials.
- **Hard Rule 8 (Splunk first-party priority):** Splunk dormant on every IOC tested; no first-party signal to contradict or confirm Rapid7's claims.

## IOCs (from ioc-extraction extraction notes)

```yaml
ioc_set:
  c2_infrastructure:
    - ip: "46.225.231.170"
      role: modelorat_beacon
      first_observed: 2026-04
      source: rapid7_ir_telemetry
    - ip: "144.172.99.68"
      role: modelorat_beacon
      source: rapid7_ir_telemetry
    - ip: "64.94.85.158"
      role: modelorat_beacon
      source: rapid7_ir_telemetry
    - ip: "140.82.6.45"
      role: modelorat_beacon
      source: rapid7_ir_telemetry
    - ip: "45.76.241.51"
      role: modelorat_beacon
      source: rapid7_ir_telemetry
    - ip: "87.120.186.229"
      role: internal_py_microsoft5237_py_c2
      source: rapid7_ir_telemetry
    - ip: "149.248.78.202"
      role: internal_py_microsoft5237_py_c2
      source: rapid7_ir_telemetry
    - ip: "144.172.88.18"
      role: tcp_shell
      source: rapid7_ir_telemetry
    - ip: "64.190.113.187"
      role: tcp_shell
      source: rapid7_ir_telemetry
    - ip: "45.59.122.231"
      role: tcp_shell
      source: rapid7_ir_telemetry
    - ip: "96.9.125.29"
      role: socks5_proxy
      source: rapid7_ir_telemetry
    - ip: "144.172.111.49"
      role: socks5_proxy
      source: rapid7_ir_telemetry
    - ip: "104.194.152.246"
      role: socks5_proxy
      source: rapid7_ir_telemetry

  file_hashes:
    - sha256: b00c1cbcfb98d2618a5c2ccb311da94f3c57709a397be6c8de29839f4e943976
      filename: ssss.dll
      role: modelorat_payload_compiled_python_dll
      source: rapid7_ir_telemetry
    - sha256: 30e5a6c982396cdf3157195b540f75096869baa8570f66fab88c07c161be27f0
      filename: com6848.dll
      role: modelorat_payload_compiled_python_dll
      source: rapid7_ir_telemetry

  persistence_artifacts:
    - type: registry_sync_provider_guid
      value: "{904EE598-0511-4664-82A8-22C4A7501044}"
      name: PLURIBUS
      role: persistence_via_sync_provider_registration

  exploited_vulnerabilities:
    - cve: CVE-2023-36036
      product: Windows Cloud Files Mini Filter Driver (cldflt.sys)
      class: heap_buffer_overflow_lpe
      cvss_v3_base: 7.8
      kev_listed: true
      kev_date_added: 2023-11
      weaponization_status: n_day_observed_in_april_2026_rapid7_ir

attribution_claims:
  - actor: KongTuke
    confidence_per_source: moderate_to_high
    source: rapid7
    in_roster_yaml: false
    /new-actor_candidate: true
  - actor: Octo Tempest / Scattered Spider / UNC3944
    relation_type: tradecraft_similarity_referenced_not_attributed
    source: rapid7
    in_roster_yaml: true_via_scattered_spider_id_013
```
