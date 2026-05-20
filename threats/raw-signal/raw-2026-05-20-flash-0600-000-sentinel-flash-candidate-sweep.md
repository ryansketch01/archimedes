---
raw_id: raw-2026-05-20-flash-0600-000
collected_at: 2026-05-20T06:00:00-04:00
run_id: flash-sweep-20260520-060000
collection_mode: flash_sweep
source:
  source_yaml_id: multi
  source_name: "Multi-source FLASH sweep (06:00 EDT Wednesday — canonical scheduled slot)"
  source_url: null
  published_at: null
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: []
  keywords: []
triage_tags:
  - sentinel
  - flash_candidate_fired
  - scheduled_0600_window
  - quiet_hours_active
  - critical_override_fails
  - companion_to_raw_2026_05_20_flash_0600_001_teampcp_github_breach
  - dormant_splunk_sweep
  - 47th_consecutive_dormant
  - cisa_kev_no_new_entries_since_2026_05_15_cve_2026_42897
  - cisa_advisories_zero_in_window
  - therecord_zero_in_window
  - msrc_blog_feed_parse_failure_known
  - mstic_zero_in_window
  - unit42_zero_in_window
  - krebs_zero_in_window
  - sans_isc_zero_in_window
  - mandiant_feedburner_404_known_failure_count_20_plus
  - google_ti_rss_parse_failure_known
  - dragos_feed_404_known_failure
  - securityweek_marketing_post_only_plus_teampcp_github_relay
  - bleepingcomputer_3_items_2_in_topic_cluster_1_yellowkey_update_class
  - thehackernews_3_items_2_in_topic_cluster_1_yellowkey_update_class
iocs_extracted: false
iocs_count: 0
text_word_count: 580
promoted: false
non_promotable_tombstone: true
grader_inspected: true
grader_inspected_at: 2026-05-20T06:18:00-04:00
grading_run_id: flash-grade-20260520-060000
grader_disposition: "Non-promotable sentinel companion — procedural FLASH sweep audit trail; no claim to grade independently. Companion flash candidate raw-2026-05-20-flash-0600-001 promoted to finding-2026-05-20-FLASH-0001. Per established precedent (raw-2026-05-19-flash-0600-000, raw-2026-05-18-flash-1200-000, raw-2026-05-17-flash-0000-000, etc.), sentinel tombstones do NOT generate rejection-log entries."
ttl_expires_at: 2026-08-18T06:00:00-04:00
test: false
---

# FLASH sweep 2026-05-20 06:00 EDT — companion sentinel to flash candidate raw-2026-05-20-flash-0600-001

Wednesday 06:00 EDT scheduled FLASH sweep. Time window 2026-05-20T00:00 EDT to 2026-05-20T06:00 EDT (last 6 hours). Quiet hours active (21:00-09:00 EDT) — any FLASH generated queues, not posts, except under the four-condition critical override.

## Sweep result

**One FLASH candidate fired:** raw-2026-05-20-flash-0600-001 (TeamPCP-claimed GitHub breach of 3,800 internal repositories via poisoned VS Code extension). Triggers fired: Trigger 2 (new attribution for tracked actor TeamPCP #001 HIGH) + Trigger 4 (tracked actor TTP change — first compromise of GitHub-corp itself, vs. prior supply-chain-of-supply-chain pattern). Critical override evaluation: 2 of 4 conditions met (PASS active exploitation; PASS tracked actor; FAIL CVSS 10.0 — no CVE applicable to intrusion-disclosure; FAIL A&D watchlist entity named). Override fails — FLASH queues to `flash-queue.yaml` for 09:00 catchup.

## Trigger evaluation summary

- **Trigger 1 (critical CVE + active exploitation + A-grade):** Not fired. YellowKey CVE-2026-45585 (Microsoft mitigation publication, BleepingComputer + The Hacker News in-window) is BitLocker security-feature-bypass, CVSS 6.8 — below 9.0 floor. Microsoft does NOT claim YellowKey in-the-wild exploitation specifically (Nightmare Eclipse companion zero-days BlueHammer + RedSun ARE noted exploited per The Hacker News, but those are separate CVEs not surfaced in this window). YellowKey FAILS both CVSS-floor and active-exploitation gates. CISA KEV no new entries since CVE-2026-42897 (2026-05-15) — 5-day carry-forward.
- **Trigger 2 (new attribution for tracked actor):** FIRED on TeamPCP #001 HIGH. See raw-2026-05-20-flash-0600-001 for full trigger analysis.
- **Trigger 3 (first-party IOC hit):** Not fired. Splunk -24h zero hits across `archimedes` + `defenseclaw_local` on TeamPCP / Mini Shai-Hulud / Shai-Hulud / nx-console / VS Code / vscode / YellowKey / BitLocker / check.git-service / m-kosche. 47th consecutive dormant non-self-telemetry sweep. Only operational events surfaced (prior FLASH sweep self-telemetry).
- **Trigger 4 (tracked actor TTP change):** FIRED on TeamPCP — first GitHub-corp compromise via VS Code marketplace extension. See raw-2026-05-20-flash-0600-001.
- **Trigger 5 (active multi-victim A&D-sector nation-state campaign):** Not fired. No A&D-prime victim named in any in-window source. TeamPCP campaign chain IS multi-victim across 2026 (Trivy / Checkmarx / Bitwarden CLI / TanStack / OpenAI / Mistral / Grafana / now GitHub) but named victims are dev-tooling / AI / observability — not A&D primes. Hard Rule 2 prevents Archimedes-side cross-walk to A&D-prime naming.
- **Trigger 6 (zero-day no patch + CVSS ≥ 8.0 + exploitation confirmed/imminent):** Not fired. YellowKey CVE-2026-45585 has no permanent patch yet (mitigation only) and IS pre-disclosure-class, but CVSS 6.8 is below the 8.0 floor AND no in-the-wild exploitation claimed on YellowKey itself. ChromaDB CVE-2026-45829 (anti-noise-locked from raw-2026-05-19-pm-006, dedup carry-forward from 00:00 sentinel) remains unpatched and pre-auth RCE on widely-deployed AI infrastructure — but still no in-the-wild exploitation claim, fails exploitation-confirmed-or-imminent gate. Drupal pre-disclosure PSA (raw-2026-05-19-pm-005, finding-2026-05-19-0009) is scheduled for patch release 2026-05-20 17:00-21:00 UTC = 13:00-17:00 EDT — post-sweep, not in-window yet.

## Critical override evaluation (for raw-2026-05-20-flash-0600-001 candidate)

- CVSS 10.0: FAIL (no CVE applicable — intrusion-disclosure, not vulnerability disclosure)
- Active exploitation: PASS (GitHub confirmed breach occurred)
- Tracked actor: PASS (TeamPCP #001 per `_roster.yaml`)
- A&D watchlist entity named: FAIL (no A&D prime named as victim or affected customer)

2 of 4 met. Override does NOT bypass quiet hours. FLASH queues to `flash-queue.yaml` for 09:00 catchup, or absorption by 08:00 morning brief.

## Sources queried (in-window)

**A-grade RSS confirmed empty or zero-after-since-filter:** The Record, Recorded Future, Microsoft Security Blog (MSTIC), Unit 42, Krebs on Security, SANS ISC, CISA Advisories all.xml, Mandiant cloud.google.com (RSS path remains broken — carry-forward).

**A-grade RSS partial coverage:** SecurityWeek (2 in-window items — one marketing virtual-event post + one TeamPCP-GitHub relay folded into raw-2026-05-20-flash-0600-001), BleepingComputer (3 in-window items — 2 TeamPCP-GitHub cluster folded into candidate, 1 YellowKey mitigation publication evaluated as UPDATE-class not fresh FLASH), The Hacker News (3 in-window items — 1 TeamPCP-GitHub folded into candidate, 1 Grafana investigation-update relay folded as campaign-chain context into candidate, 1 YellowKey mitigation publication evaluated as UPDATE-class).

**B-grade RSS with known feed-layer failures (handled per source-health, no source-health changes this sweep):** Mandiant feedburner (404, twentieth-plus consecutive — operator alt-endpoint decision still pending), Dragos /blog/feed/ (404 carry-forward), Google Cloud TI RSS (XML parse error re-confirmed this sweep). MSRC blog feed (XML parse error carry-forward). These are tracked carry-forward conditions — no new failures introduced by this sweep.

**KEV check:** CISA KEV JSON re-checked via WebFetch. Most recent 5 entries by dateAdded: CVE-2026-42897 (2026-05-15, MS Exchange OWA XSS), CVE-2026-20182 (2026-05-14, Cisco Catalyst SD-WAN auth bypass), CVE-2026-42208 (2026-05-08, BerriAI LiteLLM SQLi), CVE-2026-6973 (2026-05-07, Ivanti EPMM), CVE-2026-0300 (2026-05-06, PAN-OS). Zero entries 2026-05-19 or 2026-05-20. CVE-2026-42897 5-day carry-forward; FLASH-queued 2026-05-15 06:55, superseded by 2026-05-15-morning, no fresh FLASH trigger in this window.

**Splunk first-party:** `archimedes` + `defenseclaw_local` -24h zero hits on TeamPCP / Mini Shai-Hulud / Shai-Hulud / nx-console / VS Code / vscode / YellowKey / BitLocker / check.git-service / m-kosche. 47th consecutive dormant non-self-telemetry sweep — operational events only (this is the expected baseline; no IT-tier telemetry forwarded yet).

## Source-health changes

None this sweep. All known carry-forward failures (Mandiant feedburner, Dragos /blog/feed/, MSRC blog feed, Google TI RSS, Volexity blog parse) remain in their prior state; the sweep did not introduce new failures.

## Anti-noise compliance

- TeamPCP-GitHub-internal-breach: anti-noise lock candidate `teampcp-github-internal-repos-breach-via-vscode-extension-2026-05-20` until 2026-05-21T06:08:00-04:00. Distinct from 2026-05-15 TeamPCP source-code-release FLASH (different mechanism — release vs. breach; different actor-victim posture — TeamPCP-as-uploader vs. TeamPCP-as-intruder) and distinct from 2026-05-19-am-006 nx-console VS Code extension surface (different victim — nx-console maintainer vs. GitHub-corp; different extension; different mechanism — package compromise vs. employee-device compromise).
- ChromaDB CVE-2026-45829 BleepingComputer chain: dedup-locked from raw-2026-05-19-pm-006 (24h not yet elapsed; no fresh exploitation claim in window).
- YellowKey CVE-2026-45585 mitigation publication: UPDATE-class on raw-2026-05-13-pm-001 PoC surface; covered as secondary item context in flash-0600-001, not separately raw-signaled.
- Grafana GitHub breach (The Hacker News investigation-update relay 2026-05-20T05:12:06 UTC): folded as campaign-chain context into flash-0600-001 (same TeamPCP campaign chain); not separately raw-signaled.

## Disposition

- One FLASH candidate file written: `threats/raw-signal/raw-2026-05-20-flash-0600-001-github-teampcp-internal-repos-breach-vscode-extension.md`.
- Per FLASH-POLICY pipeline: grader → red-team-analyst (WEP "very likely" candidate) → briefer.
- Briefer composes FLASH brief; queues to `infrastructure/flash-queue.yaml` per quiet-hours rule.
- 08:00 morning brief is the natural absorption point — predict supersession by 2026-05-20-morning.
- This companion sentinel preserves the full audit trail of the sweep including non-fired triggers, source-coverage summary, and anti-noise compliance.
