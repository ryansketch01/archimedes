---
raw_id: raw-2026-05-16-flash-0600-001
collected_at: 2026-05-16T06:05:00-04:00
run_id: flash-sweep-20260516-060000
collection_mode: flash_sweep
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek"
  source_url: "https://www.securityweek.com/poc-code-published-for-critical-nginx-vulnerability/"
  published_at: 2026-05-16T06:02:00-04:00
  byline: "Ionut Arghire"
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: [CVE-2026-42945]
  keywords: [NGINX, F5, NGINX Rift, depthfirst, PoC, rewrite module]
triage_tags: [non_flash, carry_forward_update, vt_finding_0002_lineage, poc_published_not_active_exploitation]
flash_trigger_evaluation:
  trigger_1_critical_cve_exploited: false
  trigger_1_failure_reason: "PoC publication is not active in-the-wild exploitation per FLASH-POLICY Trigger 1 wording. Article explicitly states 'PoC code is now publicly available' — no in-the-wild exploitation cited. Trigger requires exploitation_status: active, not exploitation_imminent."
  trigger_6_zero_day_no_patch: false
  trigger_6_failure_reason: "Patch already available since 2026-05-13/14 F5 quarterly K000160932 release (covered in morning brief finding-2026-05-14-0002). patch_available: true."
  conclusion: "Material update to existing finding-2026-05-14-0002 (NGINX Rift / CVE-2026-42945) for 2026-05-16 morning brief carry-forward. Not a FLASH trigger."
iocs_extracted: false
iocs_count: 0
text_word_count: 280
promoted: false
ttl_expires_at: 2026-08-14T06:05:00-04:00
---

# PoC Code Published for Critical NGINX Vulnerability

**Publication:** 2026-05-16 06:02 EDT (within FLASH sweep window 00:00-06:00 EDT)
**Author:** Ionut Arghire
**Outlet:** SecurityWeek

## Source-attested facts

- **CVE:** CVE-2026-42945
- **CVSS:** 9.2 (Critical) — vendor F5 K000160932
- **Affected:** NGINX Plus 37.0.0 / R36 P4 / R32 P6; NGINX Open Source 1.31.0 / 1.30.1
- **Vulnerability class:** Heap buffer overflow in `ngx_http_rewrite_module`
- **Trigger condition:** Servers using `rewrite` and `set` directives; exploitation uses escaped URI data overflowing heap boundaries when question marks appear in rewrite replacements
- **Patch status:** Available as of week of 2026-05-13/14 (F5 quarterly release K000160932) — patched per finding-2026-05-14-0002
- **PoC publisher:** depthfirst (independent researcher; provisional F per source-grades.yaml first-citation 2026-05-14-0002)
- **PoC URL:** https://github.com/depthfirstdisclosures/nginx-rift (per SecurityWeek; not directly verified by Archimedes collector — Hard Rule 3 applies: do NOT fetch / mirror PoC content)
- **Active exploitation:** NOT explicitly mentioned in SecurityWeek primary. RCE possible only when ASLR disabled per F5 warnings; DoS otherwise.

## SecurityWeek opening framing (paraphrase — under 15-word quote limit)

Technical details and proof-of-concept code targeting a newly patched critical NGINX vulnerability are now available. The bug is a heap buffer overflow in the rewrite module enabling DoS, with RCE possible if ASLR is disabled per F5 warnings.

## Why this surfaces

- finding-2026-05-14-0002 (morning brief 2026-05-14, NGINX Rift T-?? watch) anticipated PoC publication as the most-likely next development pivot after F5 vendor-self-disclosure. depthfirst was already cited in that finding's editorial-chain context (THN '18-year dormancy' framing originated with THN + depthfirst).
- PoC publication 36-48h post-disclosure with explicit primitive disclosure (heap overflow / question-mark-in-rewrite-replacement / ASLR-dependency) materially raises in-the-wild-exploitation probability over the next 7-14 days. Mass scanning + opportunistic exploitation are the canonical post-PoC pattern for NGINX class vulnerabilities.
- Operational implication for A&D-prime defenders: NGINX is widely deployed in defense-contractor edge / reverse-proxy / Kubernetes-ingress paths. Patch status of internal NGINX Plus + NGINX Open Source deployments should be verified within next 24-72h. ASLR-enabled posture (default on modern Linux distros) downgrades RCE to DoS but does NOT eliminate exposure.

## FLASH evaluation per FLASH-POLICY.md

Walked all 6 triggers:

1. **critical-cve-exploited** — FAILS on `exploitation_status: active`. PoC publication is NOT active in-the-wild exploitation per policy wording. (CVSS 9.2 meets the 9.0 min; SecurityWeek is provisional B — fails A-grade requirement also.)
2. **tracked-actor-attribution** — FAILS. No actor attribution; depthfirst is independent researcher.
3. **first-party-ioc-hit** — FAILS. Splunk defenseclaw_local dormant; no IOC published.
4. **tracked-actor-ttp-change** — FAILS. No tracked actor.
5. **ad-sector-campaign** — FAILS. No campaign; no A&D targeting; no multi-victim.
6. **zero-day-no-patch** — FAILS on `patch_available: false`. Patch shipped 2026-05-13/14.

**Conclusion: NOT a FLASH trigger.** Routes to morning brief 2026-05-16 as carry-forward update on finding-2026-05-14-0002 (vt_finding_0002_lineage). Grader should evaluate as new corroborating signal on the existing NGINX Rift finding lineage; briefer should weave into the standing CVE watch section, not stand up a new FLASH.

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire (SecurityWeek)
- Article type: news / vendor-vulnerability update
- Raw IOC extraction invoked: no (no IOCs to extract — CVE reference only)
- Hard Rule 3 compliance: PoC URL recorded for analyst reference; PoC content NOT fetched / NOT mirrored / NOT extracted into raw-signal body
- Anti-noise check: This is the FIRST raw-signal in the 24h dedup window mentioning CVE-2026-42945 PoC publication. The CVE itself was the morning brief 2026-05-14 lead-cohort item; PoC publication is a NEW development on that cohort, not a re-report.

## IOCs (from ioc-extraction skill)

None. CVE-2026-42945 is the sole technical reference. No domains, IPs, hashes, or other indicators in the SecurityWeek primary.
