---
raw_id: raw-2026-05-20-am-001
collected_at: 2026-05-20T07:32:00-04:00
run_id: pre-brief-20260520-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek (Ionut Arghire)"
  source_url: https://www.securityweek.com/over-320-npm-packages-hit-by-fresh-mini-shai-hulud-supply-chain-attack/
  published_at: 2026-05-20T07:06:49-04:00
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: [VT-006]
  keywords:
    - Mini Shai-Hulud
    - "@antv namespace"
    - npm supply chain
    - PyPI
    - Composer
    - 639 malicious versions
    - 1055 versions across 502 unique packages
    - Python code execution downloaded
    - Claude Code backdoor drop
    - dual-channel credential exfil
    - TeamPCP attribution moderate confidence
    - timeago.js
    - echarts-for-react
    - actions-cool issues-helper
    - Durabletask Python SDK
triage_tags:
  - in_window
  - tracked_actor_teampcp_001_high
  - tracked_vulnerability_vt_006_cve_2026_45321
  - mini_shai_hulud_expansion_data_point
  - sw_attribution_suggesting_teampcp_moderate_confidence_hedge
  - securityweek_b_grade_provisional_relay
  - single_source_originating_unclear_sw_appears_originating
  - flash_candidate_trigger_4_tracked_actor_ttp_change_python_payload_addition
  - flash_candidate_trigger_2_marginal_NEW_data_point_within_existing_campaign_attribution
  - non_flash_anti_noise_topic_continuation_within_24h_topic_lock
  - distinct_topic_from_2026_05_20_flash_0600_github_corp_breach
  - distinct_topic_from_2026_05_19_pm_004_mini_shai_hulud_639_versions
  - ttp_evolution_python_downloader_added_per_sw_quote
  - claude_code_backdoor_drop_new_targeting_vector
  - no_ad_prime_named_no_critical_override
  - vuln_index_hit_vt_006
  - splunk_first_party_zero_hits_48th_consecutive_dormant_sweep
  - hard_rule_2_attribution_hedge_preserved_suggesting_not_confirming
  - hard_rule_7_quote_limit_compliance
iocs_extracted: true
iocs_count: 5
text_word_count: 950
promoted: true
promoted_to_finding: finding-2026-05-20-0001
promoted_at: 2026-05-20T07:50:00-04:00
grading_run_id: morning-20260520-080000
ttl_expires_at: 2026-08-18T07:32:00-04:00
test: false
---

# SecurityWeek — Mini Shai-Hulud expansion: 320+ npm packages in @antv namespace; TeamPCP attribution

## Source surface

**Author:** Ionut Arghire, international correspondent (SecurityWeek)
**URL:** https://www.securityweek.com/over-320-npm-packages-hit-by-fresh-mini-shai-hulud-supply-chain-attack/
**Published:** 2026-05-20T11:06:49 UTC (07:06 EDT)
**Source grade:** B (provisional per source-grades.yaml awaiting human ratification — first-cited 2026-05-06)

## Summary (verbatim claims only)

- Compromised maintainer account used to publish malicious package versions across the @antv namespace.
- Author attributes to TeamPCP with moderate hedge: "suggesting that the infamous hacking group TeamPCP mounted the attack" — language preserved verbatim per Hard Rule 2.
- Attribution rests on behavioral patterns: dual-channel credential exfiltration through GitHub and unspecified fallback server. SecurityWeek does NOT claim direct technical attribution.
- 639 malicious versions across @antv namespace specifically.
- Full Mini Shai-Hulud campaign total to date: 1,055 versions across 502 unique packages — broken down as 1,048 npm + 6 PyPI + 1 Composer.
- TTP evolution noted: "Unlike previous campaigns, malware now downloads Python code" for remote execution and drops backdoors into Claude Code. Quoted language preserved per Hard Rule 7 (15 words).

## Named affected packages

- @antv namespace (primary, 639 versions)
- timeago.js
- echarts-for-react
- actions-cool/issues-helper (GitHub Actions helper)
- Microsoft's Durabletask Python SDK

(NOTE: actions-cool/issues-helper + Durabletask Python SDK both cross-reference 2026-05-19-am-007 and 2026-05-19-am-008 raw-signal items, which captured those specific compromises with finer-grain detail. SW article treats them as part of the broader Mini Shai-Hulud campaign continuum.)

## A&D-sector filter outcome

**No A&D primes named.** No aerospace, defense, or A&D Tier-1 contractor (Lockheed, Boeing, RTX/Raytheon, Northrop, GD, BAE, L3Harris, Leidos, SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit) named as victim. Affected packages are JavaScript visualization libraries (@antv), time-formatting helpers, GitHub Actions tooling, and a Microsoft Python SDK — broad-developer-tooling layer, not A&D-direct.

A&D-relevance remains **structural-indirect** via SDLC supply-chain exposure (every A&D Tier-1/Tier-2 uses npm and PyPI through its CI/CD pipeline; @antv echarts visualization library is widely used in enterprise dashboards).

## Trigger evaluation

### Trigger 2 — new attribution for tracked actor (MARGINAL)
- Tracked actor: TeamPCP (#001 HIGH per `_roster.yaml`) — PASS on identity
- New attribution: FAIL on novelty test — this is a CONTINUATION of the Mini Shai-Hulud campaign attribution that has been documented in the corpus since the 2026-05-12 FLASH (finding-2026-05-12-FLASH-0001 by Wiz + Snyk + StepSecurity at A1 evidentiary tier) and has been re-stated in subsequent raw-signal surfaces (raw-2026-05-19-am-006, raw-2026-05-19-am-007, raw-2026-05-19-am-008, raw-2026-05-19-pm-004). SecurityWeek's attribution here ("suggesting TeamPCP mounted the attack") is a B-grade relay-tier restatement, not a new attribution chain.
- **Trigger 2 does NOT fire** — fails the "attribution_is_new_not_restatement" condition.

### Trigger 4 — tracked actor TTP change (CANDIDATE)
- Tracked actor attributable: PASS (TeamPCP, B-grade provisional source — though "suggesting" hedge is below the formal moderate-to-high confidence threshold).
- New tooling: **CANDIDATE** — SecurityWeek explicitly notes "malware now downloads Python code" + "drops backdoors into Claude Code" as deltas vs. prior Mini Shai-Hulud campaign mechanics. If accurate, this is a TTP evolution: (a) Python downloader layer added to prior JS-only payload chain; (b) Claude Code (Anthropic's coding assistant) targeted as a backdoor drop venue. The Claude Code backdoor angle, if substantiated, is a noteworthy AI-tooling TTP that has not previously surfaced in the corpus.
- Source grade A/B: PASS (B-grade provisional).
- **Single-source veto risk:** SecurityWeek appears to be the originating primary on this specific data point — the @antv 639-versions number and the Python-downloader / Claude Code claims are not cross-corroborated by Wiz / Snyk / Socket / StepSecurity in this window. Grader to assess single-source veto application at WEP layer.
- **Trigger 4 fires conditionally pending grader's single-source assessment.**

### Trigger 1 — critical CVE + active exploitation + A-grade
- VT-006 / CVE-2026-45321 is the parent campaign CVE. Already KEV-tracked and exploited from prior surfaces (finding-2026-05-12-FLASH-0001 + downstream). This raw-signal is a new data point within the same CVE — not a new Critical CVE.
- **Trigger 1 does NOT fire** (carry-forward, not net-new).

### Trigger 3 — first-party Splunk IOC hit
- Splunk query (-24h) on TeamPCP / Mini Shai-Hulud / antv / timeago / echarts / actions-cool / Durabletask / Python-downloader returned zero hits in archimedes + defenseclaw_local indexes. Only Archimedes-internal pipeline events (38 events total — operation 22, scheduler 15, brief 1) surfaced.
- 48th consecutive dormant non-self-telemetry sweep.
- **Trigger 3 does NOT fire.**

### Trigger 5 — A&D-sector multi-victim active campaign
- Multi-victim: PASS (multiple package compromises within campaign).
- A&D-sector named: FAIL (no A&D prime named as victim).
- **Trigger 5 does NOT fire** — same failure pattern as 2026-05-20 06:00 FLASH on GitHub-corp breach.

### Trigger 6 — zero-day no patch + CVSS≥8.0 + exploitation confirmed/imminent
- CVE-2026-45321 is patched but campaign continues via maintainer-account compromise (compromise vector remains active even though CVE is patched).
- This is not Trigger 6 shape — Trigger 6 is about un-patched zero-days. Campaign-level activity on a patched CVE is Trigger 2/4 territory.
- **Trigger 6 does NOT fire.**

### Critical override (quiet-hours bypass) evaluation
- CVSS 10.0: not applicable to this campaign-update surface (parent CVE patched).
- Active exploitation: YES (campaign ongoing).
- Tracked actor: YES (TeamPCP).
- A&D watchlist entity named: NO.
- **2 of 4 conditions met — override does NOT apply.** No quiet-hours bypass eligible regardless.

## Anti-noise compliance

- **Topic lock applied:** raw-2026-05-19-pm-004 captured "Shai-Hulud 639 versions 323 packages mass wave" yesterday afternoon (anti-noise lock active until 2026-05-20 PM). Today's @antv 639-versions number IS the same delta (the @antv-namespace 639-versions count is the same data point Bill Toulas reported at BleepingComputer yesterday).
- **However:** SecurityWeek's Python-downloader and Claude Code backdoor claims are NEW data points within the same 24h topic lock — these specifically warrant grader attention.
- **Recommendation to grader:** treat this as a CAMPAIGN-CHAIN UPDATE on the parent Mini Shai-Hulud finding, NOT a fresh FLASH. The Python-downloader + Claude Code claims are the only net-new data points; cross-corroboration from Wiz / Snyk / Socket / StepSecurity is pending.

## Disposition recommendation

Pre-brief absorption — fold into morning brief as one bullet within the TeamPCP campaign-chain block alongside the 06:00 FLASH GitHub-corp breach. No standalone FLASH. The 06:00 FLASH and this raw-signal cluster represent the TeamPCP-campaign primary action items for the 08:00 morning brief.

---

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire (SecurityWeek)
- Article type: blog (B-grade media)
- Raw IOC extraction invoked: yes — package-name IOCs only (no domains/IPs/hashes published in this primary)
- Splunk first-party: zero hits over -24h across TeamPCP / Mini Shai-Hulud / antv / package-name tokens; 48th consecutive dormant non-self-telemetry sweep
- Hard Rule 2 attribution-origination compliance: SecurityWeek's "suggesting" hedge preserved verbatim; not upgraded to confirmed
- Hard Rule 7 quote-limit compliance: each direct quote ≤ 15 words

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: package_compromise
    value: "@antv namespace (639 malicious versions)"
    source: SecurityWeek (Ionut Arghire)
    context: "Primary cluster of this campaign wave. JavaScript visualization library widely used in enterprise dashboards."
    confidence: provisional
    grade_facts: B (single-source originating)
    grade_attribution: B (TeamPCP attribution at 'suggesting' moderate-hedge confidence)
  - type: package_compromise
    value: "timeago.js (npm)"
    source: SecurityWeek
    context: "Time-formatting JS helper; broad-use developer dependency"
    confidence: provisional
    grade_facts: B
    grade_attribution: B
  - type: package_compromise
    value: "echarts-for-react (npm)"
    source: SecurityWeek
    context: "React wrapper for Apache ECharts visualization; broad enterprise use"
    confidence: provisional
    grade_facts: B
    grade_attribution: B
  - type: package_compromise
    value: "actions-cool/issues-helper (GitHub Actions)"
    source: SecurityWeek (cross-corroborates raw-2026-05-19-am-007)
    context: "GitHub Actions helper for issue management; CI/CD layer of compromise"
    confidence: confirmed
    grade_facts: A (multi-source incl. SecurityWeek + THN + Bleeping)
    grade_attribution: B
  - type: package_compromise
    value: "Microsoft Durabletask Python SDK"
    source: SecurityWeek (cross-corroborates raw-2026-05-19-am-008)
    context: "Microsoft Python SDK on PyPI; corporate-vendor supply-chain exposure"
    confidence: confirmed
    grade_facts: A (multi-source)
    grade_attribution: B
attribution_claims:
  - actor: TeamPCP
    nation: unknown
    service: null
    claim_source: SecurityWeek attribution (originating in this surface) — "suggesting that the infamous hacking group TeamPCP mounted the attack"
    confidence_hedge: "suggesting" (moderate-hedge; below "moderate confidence" formal threshold)
    behavioral_basis: "dual-channel credential exfiltration through GitHub and fallback server"
    new_or_restatement: RESTATEMENT of parent campaign attribution (Mini Shai-Hulud → TeamPCP). NOT first-time attribution; corpus has multi-A-grade attribution chain from finding-2026-05-12-FLASH-0001 (Wiz + Snyk + StepSecurity A1) onward.
    novel_ttp_claims:
      - "malware now downloads Python code" (Python downloader stage — NEW per SW; not previously documented in corpus Mini Shai-Hulud surfaces)
      - "drops backdoors into Claude Code" (AI-tooling-targeting TTP — NEW per SW; awaits Wiz/Snyk/Socket cross-corroboration)
campaign_lineage:
  parent_campaign: TeamPCP 2026 SDLC supply-chain chain → Mini Shai-Hulud npm + PyPI worm sub-campaign
  parent_finding: finding-2026-05-12-FLASH-0001 (A1 attribution by Wiz + Snyk + StepSecurity)
  parent_vt_index: VT-006 / CVE-2026-45321
  prior_corpus_anchors:
    - finding-2026-05-19-0001 (Mini Shai-Hulud expansion / Socket Burckhardt named-analyst)
    - raw-2026-05-19-pm-004 (Mini Shai-Hulud 639 versions 323 packages mass wave / BleepingComputer Bill Toulas)
    - raw-2026-05-19-am-007 (actions-cool/issues-helper / THN)
    - raw-2026-05-19-am-008 (@antv 323 packages atool maintainer / THN)
  this_surface_increment:
    - "Confirms @antv-namespace 639-version count via second independent source (SW after BleepingComputer)"
    - "Adds Python-downloader payload-stage claim (new TTP delta vs. prior JS-only Mini Shai-Hulud)"
    - "Adds Claude Code backdoor-drop claim (new AI-tooling targeting vector; awaits cross-corroboration)"
```
