---
raw_id: raw-2026-07-21-flash-0000-002
collected_at: 2026-07-21T00:10:00-04:00
run_id: flash-sweep-20260721-000000
collection_mode: flash_sweep
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (Lawrence Abrams)
  source_url: https://www.bleepingcomputer.com/news/security/sonicwall-sma1000-flaws-exploited-as-zero-days-to-push-custom-malware/
  published_at: 2026-07-20T18:23:23-04:00
  originating_research: "Volexity (UTA0533 tracking designation) — BleepingComputer relay"
match_reason:
  watchlist: []
  actors: []            # UTA0533 is a Volexity temp designation, NOT in _roster.yaml
  vulnerabilities: [CVE-2026-15409, CVE-2026-15410]   # already promoted to finding-2026-07-14-0007 via raw-2026-07-20-flash-1200-001
  keywords: [SonicWall, SMA1000, zero-day, edge-appliance, KnuckleBall, ORANGETAIL, ROOTRUN]
triage_tags: [flash_sweep, non_flash, grader_queue, vuln_tracker_candidate, edge_appliance, anti_noise_deduplicated, update_material]
iocs_extracted: true
iocs_count: 4
text_word_count: 320
promoted: false        # UPDATE material for existing finding-2026-07-14-0007; grader folds
disposition: update_material_vuln_tracker_and_existing_finding
related_finding: finding-2026-07-14-0007    # SonicWall SMA1000 CVE-2026-15409/15410 (UTA0533)
vuln_tracker_target: sonicwall-sma1000-cve-2026-15409-15410   # proposed VT-NNN dossier (net-new to _index.yaml)
graded_at: 2026-07-21T08:24:00-04:00
grading_run_id: morning-20260721-080000
grader_note: >
  NOT a net-new finding and NOT a rejection. Incremental-facts UPDATE for the existing SonicWall
  SMA1000 finding (finding-2026-07-14-0007). Net-new details vs the 07-20 12:00 raw-signal: CVE
  type split (CVE-2026-15409 = critical SSRF; CVE-2026-15410 = high command injection); NET-NEW
  tooling ROOTRUN (privesc/root command execution); affected models SMA1000 6210/7210/8200v;
  patch versions 12.4.3-03453 / 12.5.0-02835. DOES NOT lift the existing A2/likely grade: this is
  a second BleepingComputer relay of the SAME Volexity upstream, so it shares a common origin
  (the A2->A1 lift was already BLOCKED by red-team-20260720-181500 on common-upstream grounds).
  Incremental facts fold at "likely." Splunk Rule 8 re-run on ROOTRUN / deploy_new.py /
  agent_wp8.jar / agent_wp9.jar / SMA1000 / CVE-2026-15409/15410 -> 0 genuine defenseclaw_local
  IOC hits (the 13 archimedes-index matches are the agent's own operational sweep/commit logs,
  NOT telemetry). Visibility-bounded null. vuln-tracker to open/populate the SonicWall SMA1000
  VT-NNN dossier (still absent from _index.yaml) with the ROOTRUN + model + patch-version facts.
ttl_expires_at: 2026-10-19T00:10:00-04:00
---

# SonicWall SMA1000 CVE-2026-15409/15410 (UTA0533) — BleepingComputer corroboration + net-new ROOTRUN tooling

**Anti-noise DEDUPLICATED.** This is the same story already raw-signaled
2026-07-20 12:00 (raw-2026-07-20-flash-1200-001), promoted to
finding-2026-07-14-0007, and briefed in the 2026-07-20 afternoon brief as an
UPDATE at "likely." Surfaced again this window via a second relay
(BleepingComputer / Lawrence Abrams, published 2026-07-20 18:23 EDT — after the
18:00 sweep). Raw-signaled as **non-FLASH UPDATE material** so the grader /
vuln-tracker can fold the incremental facts. Did NOT clear a FLASH trigger
(anti-noise one-per-topic-per-24h; UTA0533 not roster; no A&D victim; patch
available since 07-14). Not graded here; attribution verbatim per Hard Rule 2.

## Net-new / incremental facts vs. the 07-20 12:00 raw-signal

- **CVE type detail:** CVE-2026-15409 = critical **server-side request forgery
  (SSRF)**; CVE-2026-15410 = high-severity **command injection**. (CVSS still not
  provided in the relay; not independently established.)
- **NET-NEW tooling named:** **ROOTRUN** — a privilege-escalation tool for root
  command execution (not in the prior raw-signal, which listed KnuckleBall /
  ORANGETAIL / Suo5).
- **Affected models:** SMA1000 **6210, 7210, and 8200v** appliances.
- **Patch versions:** **12.4.3-03453** and **12.5.0-02835** (patches available
  since 2026-07-14; consistent with prior — NOT a no-patch zero-day now).
- **Attribution (verbatim):** UTA0533 "was observed using multiple zero-day
  exploits, malware designed specifically for SonicWall SMA VPN appliances, as
  well as other attacker tradecraft." UTA0533 remains a Volexity temp
  designation — **NOT a `_roster.yaml` actor**; no roster cross-walk asserted.
- Victim sectors still unspecified; **no aerospace or defense target named.**

## Why non-FLASH

- **T1:** the same CVE pair was FLASH-evaluated 2026-07-20 12:00 → non_flash,
  absorbed to afternoon brief; anti-noise bars a re-flash within 24h.
- **T4 (actor TTP change):** UTA0533 not roster → not attributable to a tracked
  actor.
- **T5 / T6:** no A&D victim; patch available (not no-patch).

---

## Extraction notes

- Language: en
- Publisher byline: Lawrence Abrams (BleepingComputer, B-grade relay)
- Article type: blog / news
- Raw IOC extraction invoked: yes — filename-class indicators below.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: filename
    value: "deploy_new.py"
    context: "KNUCKLEBALL custom dropper"
    confidence: reported
  - type: filename
    value: "agent_wp8.jar"
    context: "Suo5 (Sou5) Java reverse proxy"
    confidence: reported
  - type: filename
    value: "agent_wp9.jar"
    context: "ORANGETAIL custom Java webshell"
    confidence: reported
  - type: tool_name
    value: "ROOTRUN"
    context: "privilege-escalation tool for root command execution (NET-NEW this relay)"
    confidence: reported
cve_references:
  - id: CVE-2026-15409
    context: "critical SSRF; SonicWall SMA1000; actively exploited from ~2026-06-22"
  - id: CVE-2026-15410
    context: "high-severity command injection; SonicWall SMA1000"
attribution_claims:
  - actor: "UTA0533"
    roster_id: null       # NOT in _roster.yaml
    claim: "Zero-day exploitation of SonicWall SMA1000 with purpose-built malware"
    attributing_source: "Volexity (per BleepingComputer relay)"
    language: "observed / tracked designation"
    novelty: "corroboration of already-briefed 2026-07-14 disclosure; ROOTRUN net-new"
```
