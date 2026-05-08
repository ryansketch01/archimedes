---
raw_id: raw-2026-05-08-pm-007
collected_at: 2026-05-08T15:41:00-04:00
run_id: pre-brief-20260508-153000
collection_mode: pre_brief_collection
test: false
sources:
  - source_yaml_id: securityweek
    source_name: "SecurityWeek (In Other News column)"
    source_url: https://www.securityweek.com/in-other-news-train-hacker-arrested-pamdoora-linux-backdoor-new-cisa-director-frontrunner/
    source_grade_estimated: B
    role: pointer_relay
    published_at: 2026-05-08T14:30:00+00:00
    note: |
      SecurityWeek "In Other News" column references PamDOORa Linux
      backdoor being marketed by threat actor "darkworm" on a Russian
      cybercrime forum for $900. SecurityWeek itself is a one-line
      relay; primary research not yet identified in this sweep.
publish_window: { start: 2026-05-08T07:30:00-04:00, end: 2026-05-08T15:30:00-04:00 }
match_reason:
  watchlist: []
  actors:
    - "darkworm"  # NOT in roster — handle as untracked
  vulnerabilities: []
  keywords:
    - pamdoora
    - linux-pam-backdoor
    - persistent-ssh-access
    - credential-harvesting
    - russian-cybercrime-forum
    - darkworm-actor-handle
    - 900-usd-malware-source-code
triage_tags:
  - emerging_malware
  - linux_backdoor
  - source_code_for_sale
  - underground_marketplace_signal
  - low_signal_high_relevance_pattern
  - non_ad_specific
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    decision: not_triggered
    rationale: "No CVE; this is custom backdoor."
  trigger_2_tracked_actor_attribution:
    decision: not_triggered
    rationale: "'darkworm' is an underground forum handle, not a tracked actor."
  trigger_3_first_party_ioc_hit:
    decision: not_triggered
    rationale: "Splunk archimedes/defenseclaw_local clean."
  trigger_4_tracked_actor_ttp_change:
    decision: not_triggered
  trigger_5_ad_sector_campaign:
    decision: not_triggered
    rationale: "Forum-marketed source code, not a campaign-in-the-wild."
  trigger_6_zero_day_no_patch:
    decision: not_triggered
    rationale: "Not a vulnerability; PAM is the legitimate Linux subsystem being abused, not vulnerable per se."
iocs_extracted: true
iocs_count: 2
text_word_count: 380
publication_window_match: in_window
promoted: false
rejected_at: 2026-05-08T16:36:00-04:00
rejection_id: reject-2026-05-08-0003
ttl_expires_at: 2026-08-06T15:41:00-04:00
---

# PamDOORa — Linux PAM-stack backdoor source code marketed on Russian cybercrime forum

## Source summary

SecurityWeek's 2026-05-08 "In Other News" column flags a new Linux backdoor named **PamDOORa** marketed by a threat actor handle **"darkworm"** on a Russian cybercrime forum for **$900**. The malware targets the Linux Pluggable Authentication Module (PAM) stack — the legitimate authentication framework used by sshd, sudo, login, and other privileged daemons.

SecurityWeek's coverage is a single-line relay. Primary technical research not identified in this sweep — likely from a smaller researcher or vendor that SecurityWeek aggregated.

## Capabilities (per SecurityWeek's brief description)

- Persistent SSH access via PAM backdoor
- Credential harvesting from legitimate user authentications (i.e., as users SSH in normally, the malicious PAM module captures plaintext credentials)

## Why this matters

**PAM-backdoor pattern is high-value for adversaries:**
- Sits directly in the Linux authentication path
- Credentials are collected as users authenticate normally — no user-side anomaly visible
- Persistent across reboots if installed in `/lib/security` or `/lib64/security` and configured in `/etc/pam.d/*`
- Bypasses MFA when misconfigured (logs the password before MFA challenge)

**Source-code-for-sale pricing signal:**
- $900 is low-tier underground pricing — suggests broad availability, not a bespoke nation-state tool
- Source-code sales (versus binary-only) accelerate variant proliferation
- Russian-forum origin is conventional for commodity Linux-server tooling

**A&D relevance:**
- A&D primes operate large Linux server estates (build farms, container infrastructure, Tier-1 supplier connectivity gateways)
- PAM-backdoor implants weaponize existing trust in authentication — relevant to any environment where SSH credential discipline matters
- Specific A&D targeting NOT reported

**Detection guidance (general, defender-side only):**
- Audit `/etc/pam.d/*` for unexpected `auth required` or `auth optional` modules
- Monitor unusual modules in `/lib/security` (Linux) or `/lib64/security`
- File-integrity monitoring on the PAM library directory
- This is mitigation guidance only; no exploitation assistance.

## Anti-noise observation

First PamDOORa entry in Archimedes corpus. Single-source (SecurityWeek relay) — grader will likely treat as "monitor for corroborating reporting" rather than a finding-grade item without primary research.

## Extraction notes

- Language: en
- Article type: media digest (SecurityWeek In Other News)
- Publisher byline: SecurityWeek News
- Raw IOC extraction invoked: yes

## IOCs

```yaml
iocs:
  - type: malware_family_name
    value: "PamDOORa"
    role: emerging_malware
    platform: "Linux"
    target_subsystem: "PAM (Pluggable Authentication Module) stack"
    capabilities: "persistent SSH access; plaintext credential harvesting from legitimate auth flows"
    distribution: "source code marketed on Russian cybercrime forum for $900"
    sources: [securityweek-relay]

  - type: actor_handle_underground
    value: "darkworm"
    role: untracked_seller_handle
    notes: |
      Forum-handle granularity only. SecurityWeek does not name the
      forum. No prior Archimedes corpus reference. Not a tracked
      actor; not a /new-actor candidate without more evidence.
    sources: [securityweek-relay]

attribution_claims:
  - claim_text: "a threat actor known as 'darkworm' is marketing the source code"
    claim_source: securityweek-relay
    claim_confidence: forum_handle_observation
    claim_date: 2026-05-08
    notes: |
      Forum-handle observation, not attribution. Underground marketplace
      vendor names are interchangeable / disposable; no actor mapping.
```
