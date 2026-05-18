---
raw_id: raw-2026-05-18-pm-004
collected_at: 2026-05-18T15:42:00-04:00
run_id: pre-brief-20260518-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek
  source_url: https://www.securityweek.com/claw-chain-openclaw-flaws-allow-sandbox-escape-backdoor-delivery/
  published_at: 2026-05-18T08:14:43-04:00
  author: Ionut Arghire
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []  # CVE-2026-44112 / 44113 / 44115 / 44118 not on _index.yaml (candidate evaluation)
  keywords: [OpenClaw, CVE-2026-44112, CVE-2026-44113, CVE-2026-44115, CVE-2026-44118, sandbox-escape, race-condition, Cyera, AI-assistant]
triage_tags: [openclaw_claw_chain_first_corpus_surface, cyera_first_source_surface_candidate, patched_before_disclosure, anti_noise_partial_already_12_00_flash_ac3683d, status_update_candidate]
iocs_extracted: true
iocs_count: 4
text_word_count: 290
promoted: false
rejected_at: 2026-05-18T16:18:00-04:00
rejection_id: reject-2026-05-18-0001
ttl_expires_at: 2026-08-16T15:42:00-04:00
---

# 'Claw Chain' OpenClaw Flaws Allow Sandbox Escape, Backdoor Delivery

SecurityWeek (Ionut Arghire), 2026-05-18 08:14 EDT.

Four vulnerabilities in OpenClaw can be chained together to steal credentials, escape the sandbox, and plant persistent backdoors. CVE-2026-44112 (critical-severity, CVSS 9.6) is a race condition in the OpenShell sandbox. CVE-2026-44113 is a race condition for file read outside mount root. CVE-2026-44115 is an exec allowlist analysis bug enabling unapproved command execution. CVE-2026-44118 is an MCP loopback flaw for privilege escalation. CVSS scores for CVE-2026-44113, 44115, 44118 not specified in source.

Affected product: OpenClaw AI assistant + OpenShell sandbox component. Source references "over 60,000 publicly accessible OpenClaw instances" with "broad access to internal systems."

Disclosure timeline preserved verbatim: "All four vulnerabilities were reported to OpenClaw's maintainers on April 22, and patches were rolled out the next day."

Active exploitation: NO claims of active exploitation or in-the-wild observations.

Threat actor attribution: NEUTRAL language only — "an attacker" and "an adversary" without attribution to specific threat actors or nation-states.

Victim sectors: NOT specified. No A&D / defense / Tier-1 prime references in source.

Cybersecurity firm credited: Cyera (sole source — first Archimedes-corpus surface).

---

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire
- Article type: vulnerability research (research-vendor first-surface)
- Raw IOC extraction invoked: yes (CVE-class IOCs only)
- Net-new vs. 12:00 FLASH ac3683d: Same item; FLASH evaluated against all 6 triggers — Trigger 1 FAIL (no A-grade source per current source-grades.yaml; Cyera first surface unrated; no exploitation claim), Trigger 6 FAIL (patched April 23 before disclosure 2026-05-18 = 26d pre-patched).
- Hard Rule 2 preservation: Cyera framing preserved without elevation (vendor framing on own research; first corpus surface — provisional-grade-pending candidate per Sysdig 2026-05-14 / Zellic 2026-05-14 / depthfirst 2026-05-14 / V12 security 2026-05-17 first-surface precedent pattern).
- Status-update candidates for grader 16:00 afternoon brief: (a) Cyera potential addition to source-grades.yaml as provisional-grade vendor research firm (conservative C per LayerX / Seqrite / Trendyol-Albayrak precedent class; or B if peer-reviewed publication observed); (b) CVE-2026-44112 cluster evaluation for vuln-tracker _index.yaml addition pending Cyera surface recurrence OR A&D-prime adoption of OpenClaw emerges; (c) NOT a tracked-actor or A&D-prime watchlist hit, so cluster anchor unlikely to materialize as standalone finding without further surface refinement.

## IOCs

```yaml
iocs:
  - type: cve
    value: CVE-2026-44112
    cvss_v3: 9.6
    cvss_class: Critical
    description: "Race condition in OpenShell sandbox"
    product: OpenClaw AI assistant / OpenShell sandbox
    patched: true
    patched_date: 2026-04-23
    confidence_source: Cyera via SecurityWeek

  - type: cve
    value: CVE-2026-44113
    cvss_v3: null
    description: "Race condition for file read outside mount root"
    product: OpenClaw AI assistant / OpenShell sandbox
    patched: true
    patched_date: 2026-04-23
    confidence_source: Cyera via SecurityWeek

  - type: cve
    value: CVE-2026-44115
    cvss_v3: null
    description: "Exec allowlist analysis bug for unapproved command execution"
    product: OpenClaw AI assistant / OpenShell sandbox
    patched: true
    patched_date: 2026-04-23
    confidence_source: Cyera via SecurityWeek

  - type: cve
    value: CVE-2026-44118
    cvss_v3: null
    description: "MCP loopback flaw for privilege escalation"
    product: OpenClaw AI assistant / OpenShell sandbox
    patched: true
    patched_date: 2026-04-23
    confidence_source: Cyera via SecurityWeek

attribution_claims: []  # Neutral attribution language only; "an attacker" / "an adversary" — no actor named.

deployment_scope_per_source:
  publicly_accessible_instances: "over 60,000"
  access_breadth: "broad access to internal systems"
  exposure_class: "first-corpus-surface vendor-research framing — NOT independently retrieved or verified by Archimedes"
```
