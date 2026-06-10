---
raw_id: raw-2026-06-10-flash-0000-000
collected_at: 2026-06-10T00:30:00-04:00
run_id: flash-sweep-20260610-000000
collection_mode: flash_sweep
sentinel: true
flash_candidate: false
source:
  source_yaml_id: sentinel
  source_name: "FLASH sweep sentinel (candidates fired)"
  source_url: null
  published_at: 2026-06-10T00:00:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: []
triage_tags: [flash_candidate_sweep, quiet_hours, queue_path]
iocs_extracted: false
iocs_count: 0
text_word_count: 0
promoted: false
ttl_expires_at: 2026-09-08T00:30:00-04:00
---

# FLASH sweep 2026-06-10 00:00 EDT — 3 candidates fired across triggers 1 + 6

Window: 18:00 EDT 2026-06-09 → 00:00 EDT 2026-06-10. **Reporting gap context:** no raw-signal files exist in `threats/raw-signal/` between 2026-06-04 evening and this sweep — the 2026-06-05 through 2026-06-09 sweep cadence did not run / did not write outputs. This sweep effectively backfills 5+ days of FLASH-trigger evaluation against the 6-hour window's surfacing items. Anti-noise dedup rule ("one FLASH per trigger topic per 24h") does NOT suppress anything — no prior 24h FLASH on disk covering any of today's topics.

Quiet-hours window: 00:00 EDT is OUTSIDE active hours (09:00–21:00 EDT). Any candidate produced FLASH would QUEUE to `infrastructure/flash-queue.yaml` per FLASH-POLICY and ship via 09:00 catchup sweep — UNLESS critical-override fires (CVSS 10.0 + ITW + tracked-actor + A&D-watchlist-target, all four). None of today's candidates hit critical-override.

## Triggers evaluated

1. **Critical CVE (CVSS ≥9.0) + active exploitation (A-grade):** **2 FIRE.**
   - **CVE-2026-11645** Google Chromium V8 OOB R/W — CISA KEV add 2026-06-09, ITW exploitation confirmed. → `raw-2026-06-10-flash-0000-001`.
   - **CVE-2026-50751** Check Point Remote Access VPN IKEv1 auth bypass CVSS 9.3 — CISA KEV 2026-06-08, exploited by Qilin ransomware affiliate since 2026-05-07 (~1 month pre-patch). → `raw-2026-06-10-flash-0000-002`. (Also fires Trigger 6.)
   - **Candidate:** CVE-2026-42271 BerriAI LiteLLM command injection (standalone CVSS 8.7; chains with CVE-2026-48710 Starlette for CVSS 10.0 unauthenticated RCE per Horizon3.ai) — KEV-listed 2026-06-08, exploitation confirmed. Edge-case Trigger 1 disposition (standalone CVSS < 9.0 vs chain = 10.0). → `raw-2026-06-10-flash-0000-003`. **Grader to disposition.**

2. **New attribution for tracked actor:** none firing. Qilin named in Check Point VPN context but **Qilin is NOT in `_roster.yaml`** — operator should consider `/new-actor Qilin`. No other roster actor named in window. Microsoft Security Blog (June 8–9 posts) and Mandiant/GTIG (recent posts) did not name any roster actor in the 6h window.

3. **First-party Splunk IOC hit (last 24h):** none. Single comprehensive query against `defenseclaw_local` + `archimedes` indexes covering 40 high-value IOCs (IPv4 + domains tracked across UNC1549, APT28, Charming Kitten, TeamPCP, GHOSTBEARER + cross-actor set) returned 0 events in last 24h. Splunk telemetry remains Archimedes self-instrumentation only (no network/auth feed in either index — historical pattern).

4. **Tracked-actor TTP change (A/B-grade):** none in window. THN headline "WinRAR Flaw Exploited by Russia-Aligned Groups (Earth Dahu, SHADOW-EARTH-066) to Deploy Stealers in Ukraine" cites CVE-2025-8088 — already tracked via Gamaredon finding 2026-06-02. Earth Dahu / SHADOW-EARTH-066 are NOT in `_roster.yaml`; not roster-mapped tracked-actor TTP change. Defer to grader as standing-section update if relevant.

5. **Active A&D-sector nation-state campaign (multi-victim, active):** none firing. ServiceNow security-incident disclosure (API exploitation) is single-vendor scope, no A&D-prime victim named, no nation-state attribution. French Tchap messaging breach is single-victim French-government, no A&D nexus. GitHub-Microsoft-repos malware distribution (73 compromised repos pushing password-stealers) is wide-radius but no nation-state attribution and no A&D-prime victim named.

6. **Zero-day without patch (CVSS ≥8.0 or widely-deployed) + exploitation confirmed/imminent:** **1 FIRE** (overlaps with Trigger 1).
   - **CVE-2026-50751** Check Point Remote Access VPN — exploited for one month before patch existed (2026-05-07 → 2026-06-08). Pure zero-day window. Patch now available, but trigger evaluates the WAS-a-zero-day condition + active exploitation evidence. → handled by `raw-2026-06-10-flash-0000-002`.
   - **Candidate:** Microsoft Defender "RoguePlanet" zero-day (Nightmare Eclipse researcher TOCTOU race → SYSTEM LPE) disclosed 2026-06-09 via self-hosted Git repo. NO CVE assigned, NO patch, NO Microsoft advisory. CVSS unscored. **NOT firing Trigger 6** — no confirmed in-the-wild exploitation per BleepingComputer (PoC released, but PoC ≠ ITW per trigger letter, same pattern as Cisco Unified CM CVE-2026-20230 disposition on 2026-06-04). Carry to grader as Bitskrieg-series follow-on (Session 11 / 2026-06-02 PM-06 carryover); Nightmare Eclipse is the same researcher cluster as the Askar VS Code OAuth and earlier BitSkrieg disclosures.

## Notable-but-non-triggering items (carry to next pre-brief)

- **Microsoft Patch Tuesday June 2026:** 200 CVEs incl. 3 publicly-disclosed zero-days. Standard cadence; review by vuln-tracker for KEV-adjacent prioritization. Not FLASH today (no specific CVE with in-window ITW signal naming a roster actor or A&D victim).
- **Veeam Backup & Replication CVE-2026-44963 CVSS 9.4:** authenticated-domain-user RCE. Critical, but authenticated requirement + no ITW exploitation reported = not Trigger 1. Watch for KEV addition.
- **Linux kernel CVE-2026-23111 one-character nf_tables LPE (public exploits available):** local-only escalation; not Trigger 1 (no CVSS ≥9.0 RCE-class characterization), not Trigger 6 (patched). Defensive prioritization note.
- **SAP June 2026 patches (four critical NetWeaver / Commerce Cloud):** critical CVSS but no ITW exploitation surfaced in window. Watch.
- **UniFi OS chained-exploits root-without-auth:** three previously-patched bugs chained. Watch for re-emergence as ITW.
- **Gogs critical zero-day RCE (disclosed 2026-06-08):** already covered by `vuln_watch_keywords: gogs-argument-injection-2026-05-28` watch — this is the CVE-assignment-window landing per watch entry (expected 2026-06-04–2026-06-11). Vuln-tracker handoff pending; flagged for /new-actor or new vulnerability dossier creation. NOT firing FLASH today (already in coverage / watchlist).
- **Shai-Hulud PyPI attack 2026-06-08 (19 packages):** family expansion (PyPI surface vs prior npm focus); not in 6h sweep window (>24h prior). Defer to grader for PM brief — extends VT-006 / Miasma / IronWorm family-pattern across ecosystems.
- **GitHub Microsoft-org compromised-repos campaign (73 repos pushing infostealers):** wide-radius; no nation-state attribution; no A&D-prime victim. Defensive-prioritization note for next pre-brief.
- **ServiceNow API exploitation disclosure:** vendor-disclosed unauth API allowing customer-instance data query. Watch for victim disclosures + CVE assignment.

## Source health

All A-grade sources queried responded successfully. No status changes proposed. Stale-source posture unchanged from 2026-06-04 sweep: `msrc` (parse failure), `ars-security` (HTTP issues), `censys` / `urlscan` / `hibp` / abuse.ch family (no MCP / no key), `dragos` (404), `x-cisagov` / `x-gossithedog` (Twitter bridge degradation), `sophos`. Mandiant primary feedburner remains held-stale-but-healthy on alt-endpoint path; alt-endpoint returned 0 in-window items today.

Sources queried in this sweep (6 primary high-yield): CISA KEV JSON, BleepingComputer landing, The Hacker News landing, Microsoft Security Blog, Cloud / Mandiant blog, Splunk archimedes + defenseclaw_local indexes. Targeted-narrow per FLASH-doctrine; not a broad pre-brief collection.

## Disposition

**3 FLASH candidates fired** (`-001`, `-002`, `-003`). Per FLASH-POLICY quiet-hours behavior: candidates queue to `infrastructure/flash-queue.yaml`, ship via 09:00 EDT catchup sweep, with grader → red-team → briefer pipeline run before posting. Critical-override gate NOT met for any candidate (no CVSS 10.0 + tracked-actor + A&D-watchlist-named-target combo).

Operator action items surfaced:
1. **Consider `/new-actor Qilin`** — RaaS operator with confirmed zero-day-exploitation capability against widely-deployed VPN appliance, multi-victim, active. Roster-relevant.
2. **Vuln-tracker handoff:** CVE-2026-50751 (Check Point), CVE-2026-11645 (Chromium V8), CVE-2026-42271 + CVE-2026-48710 (LiteLLM+Starlette chain), Gogs CVE-assignment landing (already in vuln_watch).
3. **Pattern note:** 2nd LiteLLM CVE on KEV inside 31 days (prior CVE-2026-42208 SQLi 2026-05-08; now CVE-2026-42271 cmd-inj 2026-06-08). LiteLLM as recurring KEV-class vendor — worth a standing watch entry.

Orchestrator: log `flash_candidates_fired: 3` to Splunk; pass candidates to grader; trigger queue-write for catchup-post path.
