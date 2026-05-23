---
raw_id: raw-2026-05-23-pm-003-snyk-laravel-lang-supply-chain-advisory-primary-vt-detection-escalation
collected_at: 2026-05-23T15:40:00-04:00
run_id: pre-brief-20260523-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: snyk
  source_name: "Snyk (Tier-1 application-security research; provisional A per source-grades.yaml 2026-05-12; pending ratification)"
  source_url: https://snyk.io/blog/laravel-lang-supply-chain-advisory/
  published_at: 2026-05-23T16:00:00+00:00
match_reason:
  watchlist: []                       # Laravel-Lang is widely-deployed PHP localization library across web stacks (including sub-tier suppliers); not directly A&D-watchlisted but ecosystem-broad
  actors: []                          # NO actor attribution — Snyk does NOT attribute (Hard Rule 2 preserved); no actor named in Snyk advisory
  vulnerabilities: []                 # NO CVE assigned to the supply-chain compromise itself; Snyk uses its own SNYK-PHP-* identifiers (4 advisory IDs published)
  keywords:
    - laravel_lang_supply_chain_advisory_snyk_first_party_primary
    - corroborates_am_001_thn_socket_aikido_relay_chain
    - approximately_700_historical_versions_compromised_across_four_packages
    - github_packagist_tag_resolution_abuse_attacker_controlled_fork
    - composer_autoload_files_helpers_php_execute_on_every_php_request
    - c2_flipboxstudio_info
    - virustotal_detection_escalation_3_to_10_malicious_engines_4h_delta
    - debugchromium_exe_windows_artifact
    - var_run_secrets_proc_pid_environ_runtime_credential_harvest
    - background_php_cscript_processes
    - laravel_lang_lang_attributes_actions_http_statuses_four_packages
triage_tags:
  - non_flash
  - primary_corroboration_for_am_001
  - virustotal_detection_escalation_observable
  - supply_chain_watch_finding_candidate
  - actor_unattributed
  - originating_research_snyk_provisional_a
  - relay_layer_thn_b_grade_am_001
  - laravel_php_ecosystem_widespread_deployment
  - anti_noise_continuation_of_morning_brief_supply_chain_thread
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited: FAIL  # No CVE assigned to the supply-chain compromise itself; Snyk uses its own advisory IDs
  trigger_2_tracked_actor_attribution: FAIL  # Explicitly UNATTRIBUTED per Snyk + Socket + Aikido (am-001 cluster); no tracked-actor named
  trigger_3_first_party_ioc_hit: FAIL  # Splunk -30d sweep zero hits across flipboxstudio.info + DebugChromium.exe + adjacent IOC set
  trigger_4_tracked_actor_ttp_change: FAIL  # No tracked actor
  trigger_5_ad_sector_campaign: FAIL  # No A&D-direct victim named in Snyk advisory or AM-001 relay layer
  trigger_6_zero_day_no_patch: FAIL  # Packages removed from Packagist; remediation guidance published
  overall_flash_qualifies: false
  flash_evaluation_rationale: |
    Snyk first-party primary publishes 2026-05-23 16:00 UTC, ~6h after THN/Socket/
    Aikido relay-chain disclosure captured in am-001 this morning. This is
    corroborating primary on the same campaign — not a new finding event.
    Closes the am-001 'primary not directly retrieved' flag for the Snyk layer
    (Socket and Aikido remain not-directly-retrieved). Also surfaces real-time
    VirusTotal detection escalation on flipboxstudio[.]info (3→10 malicious
    engines in ~4h between AM and PM VT lookups), which is enrichment-quality
    signal for the grader / vuln-tracker / finding-2026-05-23-0007 if promoted.
    No new FLASH trigger fires.
promoted: false
rejected_at: 2026-05-23T16:22:00-04:00
rejection_id: reject-2026-05-23-0004
ttl_expires_at: 2026-08-21T15:40:00-04:00
---

# Laravel Lang Supply Chain Advisory

**Source:** Snyk Blog
**Published:** 2026-05-23T16:00:00+00:00 (12:00 EDT, in window)
**Snyk vendor research:** First-party originating advisory; corroborates THN/Socket/Aikido relay-chain disclosure captured in raw-2026-05-23-am-001

## Summary
Hundreds of historical Laravel Lang Packagist releases were republished with malicious code, putting Composer installs at risk of credential theft and secret exfiltration.

## Affected Packages (Four; all versions affected ≥ 0.0.0)
- `laravel-lang/lang`
- `laravel-lang/http-statuses`
- `laravel-lang/attributes`
- `laravel-lang/actions`

Approximately **700 historical versions** across these packages were compromised.

## Snyk Advisory Identifiers (No CVE Assigned)
- `SNYK-PHP-LARAVELLANGLANG-16801059`
- `SNYK-PHP-LARAVELLANGHTTPSTATUSES-16801060`
- `SNYK-PHP-LARAVELLANGATTRIBUTES-16801061`
- `SNYK-PHP-LARAVELLANGACTIONS-16801062`

(No traditional CVE numbers — Snyk uses its own SNYK-PHP-* numbering for supply-chain-compromise advisories that lack a vendor-assigned CVE.)

## Attack Mechanism
The attacker exploited **GitHub-to-Packagist tag resolution** by creating malicious tags pointing to commits in an attacker-controlled fork. A malicious `src/helpers.php` file was registered in Composer's `autoload.files`, **executing automatically on every PHP request** to any application using the compromised package.

## Command & Control Infrastructure
- **C2 Domain:** `flipboxstudio[.]info`
- **Second-stage payload URL:** `https://flipboxstudio[.]info/payload`
- **Exfiltration endpoint:** `https://flipboxstudio[.]info/exfil`

## Key IOCs (per Snyk Advisory)
- Malicious file path: `src/helpers.php`
- Infection marker (Unix-like): `<tmp>/.laravel_locale/<md5_hash>`
- Windows artifact filename: `DebugChromium.exe`
- Suspicious runtime: Background PHP/CScript processes; reads from `/var/run/secrets/` and `/proc/[pid]/environ`

## Attribution
**Explicitly UNATTRIBUTED.** Snyk advisory names no threat-actor group. This is consistent with the am-001 Socket + Aikido + THN relay layer's no-attribution framing. The four-firm UNATTRIBUTED consensus (Snyk + Socket + Aikido + THN-relay) closes the AM-sweep flag on the Snyk layer.

## Remediation Summary (from Snyk advisory)
- Quarantine affected hosts and rebuild from clean images
- Rotate all credentials readable by the PHP process
- Block the C2 domain across DNS and proxy infrastructure
- Implement integrity verification in CI/CD pipelines (signed dependencies)
- Adopt egress controls and short-lived, scoped secrets

## VirusTotal Detection Escalation (Mode 4 Enrichment, Empirical Time-Series)

`flipboxstudio[.]info` VT lookup deltas, PM vs AM same-day:

| Timestamp (UTC) | Sweep | Malicious | Suspicious | Harmless | Undetected | Engine Coverage |
|---|---|---|---|---|---|---|
| 2026-05-23 11:12 | AM (raw-2026-05-23-am-001 enrichment + sentinel) | 3 | 1 | 47 | 33 | Kaspersky, Forcepoint ThreatSeeker, ADMINUSLabs (3 hits) |
| 2026-05-23 16:57 | PM (this raw-signal) | **10** | 1 | 47 | 33 | Kaspersky, Sophos, Fortinet, ADMINUSLabs, Forcepoint ThreatSeeker, CRDF, Certego, Lionic, SOCRadar, VIPRE (10 hits) |

**Delta:** Malicious-engine count ramped **3.3x in ~4 hours**. This is real-time vendor-consensus escalation following the Snyk first-party publication. alphaMountain.ai categorizes as "Suspicious"; no registrar or creation-date metadata is exposed in VT record (privacy-protected WHOIS).

This kind of VT-detection-escalation time-series is operationally useful for the grader (corroborates the campaign is active and being adopted by vendor blocklists) and for the briefer (concrete signal that "by 12:00 EDT 3/79 engines flagged the C2; by 17:00 EDT 10/79 engines flagged the C2" — without exceeding 15-word quote limit on the source itself).

## Extraction Notes

- **Language:** en
- **Publisher byline:** Snyk (no individual analyst byline visible in RSS summary; full advisory page may carry one — flagged for direct verification if grader needs name)
- **Article type:** vendor advisory (provisional A — Snyk first-party originating-research class per source-grades.yaml 2026-05-12)
- **Raw IOC extraction invoked:** yes (full IOC set carried forward from Snyk advisory)
- **Relay-chain status:** Snyk primary directly retrieved THIS sweep, closing the am-001 'primary not directly retrieved' flag for the Snyk layer. Socket and Aikido primaries remain not-directly-retrieved (Socket blog/rss returns 404; Aikido blog primary URL not retrieved). Provisional grades unchanged.

## IOCs (ioc-extraction skill output)

```yaml
indicators:
  packages:
    - ecosystem: packagist
      name: laravel-lang/lang
      affected_versions: [">= 0.0.0 (all)"]
      compromise_method: "GitHub-to-Packagist tag resolution abuse; ~700 historical versions republished with helpers.php injection"
    - ecosystem: packagist
      name: laravel-lang/http-statuses
      affected_versions: [">= 0.0.0 (all)"]
    - ecosystem: packagist
      name: laravel-lang/attributes
      affected_versions: [">= 0.0.0 (all)"]
    - ecosystem: packagist
      name: laravel-lang/actions
      affected_versions: [">= 0.0.0 (all)"]
  domains:
    - domain: "flipboxstudio[.]info"
      role: c2_and_payload_staging
      ioc_observed_in: [snyk_advisory_2026_05_23, thn_am_001, socket_am_001, aikido_am_001]
      vt_state_2026_05_23_17_00_utc: "10/79 malicious, 1 suspicious; alphaMountain.ai 'Suspicious'; no public registrar"
  urls:
    - "https://flipboxstudio[.]info/payload"
    - "https://flipboxstudio[.]info/exfil"
  filenames:
    - "src/helpers.php"                                      # injected file, Composer autoload.files registration target
    - "DebugChromium.exe"                                    # Windows artifact dropped by stealer
    - "<tmp>/.laravel_locale/<md5_hash>"                     # Unix-like infection marker pattern
  runtime_patterns:
    - "background PHP processes reading /var/run/secrets/"
    - "background PHP processes reading /proc/[pid]/environ"
    - "background CScript processes (Windows)"
  snyk_advisory_ids:
    - SNYK-PHP-LARAVELLANGLANG-16801059
    - SNYK-PHP-LARAVELLANGHTTPSTATUSES-16801060
    - SNYK-PHP-LARAVELLANGATTRIBUTES-16801061
    - SNYK-PHP-LARAVELLANGACTIONS-16801062
attribution_claims:
  - source: snyk
    claim: "no attribution — campaign described mechanically; no threat-actor group named"
    confidence: high (on the no-attribution itself; Hard Rule 2 compliant)
  - cross_corroboration: socket + aikido + thn-relay (am-001 cluster) all UNATTRIBUTED
```

## Brief-Composition Relevance Notes

- **Primary corroboration for am-001:** This Snyk advisory is the Snyk-layer first-party primary on the Laravel-Lang campaign captured this morning via THN/Socket/Aikido relay chain in am-001. The am-001 raw-signal flagged "Snyk primary URL not directly retrieved this sweep — flagged for follow-up"; THIS raw-signal closes that flag. Snyk's advisory adds detail not present in the THN summary:
  - **Exact attack mechanism:** GitHub-to-Packagist tag resolution abuse via attacker-controlled fork (THN was less specific)
  - **Snyk advisory ID set** (four distinct advisories — useful for vulnerability-tracker indexing even though no CVE)
  - **Composer autoload.files / helpers.php execute-on-every-PHP-request mechanism** is named precisely
  - **`DebugChromium.exe` Windows artifact** is a concrete IOC the briefer can call out
  - **`/var/run/secrets/` + `/proc/[pid]/environ` runtime patterns** are concrete detection signals (Splunk hunt queries for any future first-party telemetry)
- **VT detection escalation 3→10 in 4h:** Real-time vendor-consensus signal that the campaign is being adopted across vendor blocklists post-disclosure. Briefer can use this as quantitative signal without quoting Snyk text. Useful smart-brevity "lead with impact" hook for the supply-chain narrative.
- **Anti-noise lock recommendation:** 24h anti-noise lock on "Laravel-Lang campaign" topic (this is the second raw-signal of the day on the same campaign; the morning brief at 08:00 will cover am-001; this pm-003 adds primary-corroboration + VT delta but is the same campaign). Grader and briefer should treat as continuation/enrichment of the morning's coverage, not a re-coverage.
- **Cluster relationship with Packagist 8-pkg (pm-002):** Same week, same ecosystem (PHP/Composer/Packagist), both UNATTRIBUTED, both involve GitHub infrastructure. Mechanically distinct (autoload.files + helpers.php vs. package.json postinstall + Linux binary). Grader's choice on whether to surface as separate findings or a clustered supply-chain finding.
