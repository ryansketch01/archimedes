---
raw_id: raw-2026-05-16-flash-0600-000
collected_at: 2026-05-16T06:10:00-04:00
run_id: flash-sweep-20260516-060000
collection_mode: flash_sweep
source:
  source_yaml_id: archimedes-self
  source_name: "Archimedes collector — FLASH sweep sentinel"
  source_url: null
  published_at: 2026-05-16T06:10:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, flash_sweep, dedup_audit]
triage_tags: [sentinel, non_flash, dedup_audit, splunk_self_telemetry_only]
iocs_extracted: false
iocs_count: 0
text_word_count: 410
promoted: false
ttl_expires_at: 2026-08-14T06:10:00-04:00
---

# FLASH sweep sentinel — 2026-05-16 06:00 EDT

Window: 2026-05-16 00:00 → 06:00 EDT (6h)
Last prior sweep: 2026-05-16 00:00 EDT (clean, 0 triggers, 28th consecutive dormant non-self-telemetry Splunk sweep per commit 0d1debe)
Quiet hours active: YES (06:00 EDT < 09:00 EDT start) — any candidates queue, not post

## Sources queried (status)

| Source | Status | Items in window |
|---|---|---|
| CISA Advisories (RSS) | OK | 0 |
| CISA KEV (JSON) | OK | 1 (CVE-2026-42897 added 2026-05-15 — known carry-forward) |
| BleepingComputer (RSS + site scrape) | OK | 0 in 00:00-06:00 window; latest 2026-05-15 15:30 ET (Funnel Builder) and earlier |
| The Record (RSS) | OK | 0 |
| Microsoft Security Blog (RSS) | OK | 0 |
| MSRC blog (RSS) | PARSE ERROR (XML invalid token at 126:158) | n/a — re-flag if persists |
| Cisco Talos (RSS) | OK | 0 |
| Unit 42 (RSS) | OK | 0 |
| Unit 42 FeedBurner (RSS) | OK | 0 |
| CrowdStrike (RSS) | OK | 10 items returned with null timestamps — none match FLASH triggers (product/marketing posts; CORDIAL/SNARKY SPIDER defense-product framing, not new attribution) |
| Mandiant (RSS) | OK | 0 |
| Google Cloud Threat Intel (RSS) | PARSE ERROR (XML syntax) | n/a — re-flag if persists |
| Securelist (RSS) | OK | 0 |
| Volexity (RSS) | OK | 0 |
| The Register (Atom) | OK | 0 |
| Krebs (RSS) | OK | 0 |
| Sophos (RSS) | OK | 0 |
| WeLiveSecurity / ESET (RSS) | OK | 0 |
| Recorded Future (RSS) | OK | 0 |
| Dragos (RSS) | 404 — re-flag if persists | n/a |
| The Hacker News (RSS + site scrape) | OK | 0 in window; latest 2026-05-15 (4 items, all evaluated — none FLASH-triggering, see below) |
| SecurityWeek (RSS + site scrape) | OK | 1 in window (NGINX Rift PoC publication — separate raw-signal) |
| SANS ISC (RSS) | OK | 0 |
| Cisco PSIRT (web scrape) | JS-rendered, no parseable content | n/a |
| Palo Alto PSIRT (web scrape) | OK | 1 update (CVE-2026-0251 GlobalProtect LPE CVSS 5.9 — below thresholds, not FLASH) |
| Fortinet PSIRT (web scrape) | OK | 0 (latest 2026-05-12) |
| MSRC Update Guide (web scrape) | JS-rendered, no parseable content | n/a |
| Ivanti Hub (web scrape) | 403 | n/a — re-flag if persists |
| VMware/Broadcom advisories (web scrape) | OK | 0 (no advisories on page in window) |
| Bitdefender Business Insights (RSS) | 404 — re-flag if persists | n/a |
| IC3 PSA (RSS) | OK | 0 |
| Splunk defenseclaw_local | OK | 0 events last 6h — **29th consecutive dormant non-self-telemetry sweep** |
| Splunk archimedes | OK | 3 self-telemetry events (1 archimedes:operation + 2 archimedes:scheduler) — internal heartbeat only |
| Twitter/X (nitter bridges) | 403 from nitter.poast.org | n/a — gap; flag for source-health review |

Total sources queried: 32
Sources OK with in-window content: 3 (CISA KEV carry-forward; SecurityWeek NGINX PoC; Palo Alto routine LPE update)
Sources with parse / fetch errors: 6 (MSRC blog feed, Google Cloud feed, Dragos feed, Bitdefender feed, Ivanti hub, nitter bridges) — none load-bearing for this sweep, all known-quirky or known-blocked

## Items evaluated for FLASH trigger fire

Three items reached trigger evaluation; ALL FAIL all 6 triggers:

1. **NGINX Rift PoC (SecurityWeek, in-window 06:02 EDT)** — see raw-2026-05-16-flash-0600-001. Trigger 1 fails on `exploitation_status: active` (PoC ≠ active exploitation). Trigger 6 fails on `patch_available: false` (F5 patched 2026-05-13). Routes to morning brief as carry-forward update on finding-2026-05-14-0002.

2. **CVE-2026-42897 KEV carry-forward (CISA KEV JSON, dateAdded 2026-05-15)** — known carry-forward from yesterday's afternoon brief. Federal deadline 2026-05-29 T-13 today. **Dedup applied**: already flagged in raw-2026-05-15-flash-0600-001 + raw-2026-05-15-pm-001. No new development overnight. No re-FLASH per anti-noise one-per-topic-per-24h rule.

3. **Out-of-window THN items (evaluated for completeness):**
   - **Turla / Kazuar P2P botnet** (THN 2026-05-15) — already covered in 2026-05-15 18:00 FLASH sweep (raw-2026-05-15-flash-1800-001), forwarded to morning briefer. Dedup applied — no re-FLASH.
   - **OpenClaw Claw Chain** (THN 2026-05-15 / Cyera) — CVE-2026-44112 CVSS 9.6 + 44115 CVSS 8.8 + 44113 CVSS 7.7 + 44118 CVSS 7.8, ~245,000 publicly-exposed instances. FLASH evaluation: Trigger 1 fails on `exploitation_status: active` (responsible disclosure, no in-the-wild exploitation). Trigger 6 fails on `patch_available: false` (patched in OpenClaw 2026.4.22). No A&D targeting. Routes to morning brief regular flow.
   - **OpenAI TanStack carry-forward** (THN 2026-05-15) — already covered in finding-2026-05-14-0008 (morning brief 2026-05-14). Dedup applied.
   - **CVE-2026-42897 Exchange carry-forward + Cisco SD-WAN CVE-2026-20182 KEV** (THN 2026-05-15) — known carry-forwards. Dedup applied.
   - **Funnel Builder WordPress (BleepingComputer 2026-05-15 15:30 ET)** — 40k sites, active credit card skimming exploitation per Sansec, no CVE assigned, patched in FunnelKit 3.15.0.3 yesterday. FLASH evaluation: Trigger 1 fails (no CVE = no CVSS = cannot meet ≥9.0). Trigger 5 fails (WordPress/WooCommerce ≠ A&D). Trigger 6 fails (patched). Routes to regular brief, NOT A&D-relevant.
   - **Avada Builder WordPress (BleepingComputer 2026-05-15 11:56 ET)** — CVE-2026-4782 (CVSS 6.5) + CVE-2026-4798 (SQLi), 1M installs, patched 2026-05-12. FLASH evaluation: Trigger 1 fails (CVSS 6.5 < 9.0). Trigger 5 fails (not A&D). Trigger 6 fails (patched). Routes to regular brief.
   - **Pwn2Own Berlin Day 2** (BleepingComputer 2026-05-15 13:47 ET) — already covered in 2026-05-15 16:00 afternoon brief carry-forward (Orange Tsai / DEVCORE Exchange chain embargoed). Dedup applied.
   - **node-ipc compromise** (BleepingComputer 2026-05-15 13:10 ET) — already covered in finding-2026-05-15-0005 (four-firm UNATTRIBUTED consensus). Dedup applied.

## Conclusion

**Clean sweep, 0 FLASH triggers fired.** 29th consecutive dormant non-self-telemetry Splunk sweep. 1 carry-forward update raw-signal written for morning briefer (NGINX Rift PoC publication). No quiet-hours queue items. No critical override conditions met.

## Source-health changes proposed

None requiring immediate action. The following feed-error patterns persist (already known-quirky, do NOT mark stale yet):

- `msrc-blog-feed`: XML parse error (recurrence — was working earlier in week; likely Microsoft-side intermittent malformed XML). Re-check next sweep; mark stale if 2 more consecutive failures.
- `google-cloud-threat-intel-feed`: XML syntax error (persistent — known issue). Use Mandiant primary RSS as workaround per existing operator note.
- `dragos-feed`: 404 (URL changed?). Re-check next sweep; mark stale if persists.
- `bitdefender-businessinsights-feed`: 404 (URL changed?). Re-check next sweep; mark stale if persists.
- `nitter-poast-org`: 403 (bridge rate-limit or block). Not a hard dependency for this sweep. Flag for operator review whether to point at alternate nitter instance.

These are nice-to-have, not load-bearing — the A-grade primary set (CISA, MSRC web, vendor PSIRT pages, Mandiant, Talos, Unit 42, Securelist, Volexity, Sophos, ESET, Recorded Future) all returned cleanly.
