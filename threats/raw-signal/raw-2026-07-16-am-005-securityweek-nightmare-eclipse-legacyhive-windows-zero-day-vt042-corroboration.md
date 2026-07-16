---
raw_id: raw-2026-07-16-am-005
collected_at: 2026-07-16T07:37:00-04:00
run_id: pre-brief-20260716-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (Ionut Arghire)
  source_url: https://www.securityweek.com/nightmare-eclipse-drops-legacyhive-windows-zero-day/
  published_at: 2026-07-16T06:48:40+00:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [VT-042]
  keywords: [LegacyHive, Nightmare Eclipse, Chaotic Eclipse, User Profile Service, profsvc, zero-day, PoC stripped]
triage_tags: [vuln, zero_day, unpatched, no_cve, corroboration, deduplicated, monitoring, non_flash]
iocs_extracted: true
iocs_count: 0
text_word_count: 110
promoted: false
disposition: absorbed_as_corroboration
absorbed_into_finding: finding-2026-07-15-0002
absorbed_at: 2026-07-16T08:30:00-04:00
grading_run_id: morning-20260716-080000
absorption_note: "Second-outlet (SecurityWeek) media surface of the already-graded LegacyHive drop (VT-042). Publisher-independent but NOT evidence-basis-independent (traces to the one originating researcher PoC+blog); does not lift the single-source veto; no material change to grade (B2) or WEP (likely). Recorded as an additional publisher-level relay in the finding's recalibration log; folds into the existing VT-042 MONITORING item. Not a new finding, not a rejection."
ttl_expires_at: 2026-10-14T07:37:00-04:00
---

# Nightmare Eclipse Drops 'LegacyHive' Windows Zero-Day

**Source:** SecurityWeek (Ionut Arghire), 2026-07-16 06:48 UTC.

SecurityWeek reports the Nightmare Eclipse / Chaotic Eclipse persona's **LegacyHive** Windows
zero-day — a Windows **User Profile Service (profsvc)** arbitrary registry-hive-load LPE.
The researcher **stripped the proof-of-concept** to prevent immediate exploitation. This is the
fresh 2026-07-16 media surface of the LegacyHive drop already tracked as **VT-042**.

## Dedup / corroboration status

- **Already in corpus:** captured 2026-07-15 as `raw-2026-07-15-adhoc-001`; tracked as VT-042
  in `_index.yaml` (v15); dossier scaffolded (`threats/vulnerabilities/LegacyHive/profile.md`);
  finding `finding-2026-07-15-0002`; queued to THIS morning's brief as a MONITORING item per
  `watch-config.yaml` (`nightmare-eclipse-legacyhive-2026-07-15`).
- **What is net-new:** a second-outlet (SecurityWeek) corroboration of the same drop, consistent
  with the existing B2 headline / single-source-veto grading (many outlets, one originating
  evidence basis = the researcher's own stripped PoC + blog). No CVE, no CVSS, unpatched
  (MSRC contacted-and-silent), no ITW, no named A&D victim. PoC deliberately stripped — not
  mirrored (Hard Rule 3). No actor attributed beyond the self-claimed persona (Hard Rule 2 —
  Nightmare Eclipse is a tracked persona/series, not a `_roster.yaml` actor).
- Collector disposition: corroboration only; grader/briefer fold into the existing VT-042
  monitoring item (anti-noise).

---

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire (SecurityWeek, grade B)
- Article type: security-media relay of researcher zero-day disclosure
- Raw IOC extraction invoked: yes — no atomic IOCs (no CVE assigned; no hashes/domains in relay).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-16-am-005
  source_url: https://www.securityweek.com/nightmare-eclipse-drops-legacyhive-windows-zero-day/
  extracted_at: 2026-07-16T11:37:00Z
  extracted_by: collector
  target_actor_id: null
  text_word_count: 110

indicators: []

attribution_claims: []

benign_filtered:
  - value: securityweek.com
    reason: reference_site_publisher

extraction_warnings:
  - type: no_atomic_indicators
    detail: "LegacyHive carries no CVE and the relay publishes no hashes/domains/IPs; tracked-persona keyword match only (VT-042). PoC deliberately stripped by researcher (Hard Rule 3)."
```
