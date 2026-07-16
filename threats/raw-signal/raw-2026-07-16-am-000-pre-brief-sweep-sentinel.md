---
raw_id: raw-2026-07-16-am-000
collected_at: 2026-07-16T07:32:00-04:00
run_id: pre-brief-20260716-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: collector-internal
  source_name: Collector pre-brief sweep sentinel
  source_url: null
  published_at: 2026-07-16T07:32:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sweep-coverage-record]
triage_tags: [sweep_sentinel, non_flash]
iocs_extracted: false
iocs_count: 0
text_word_count: 320
promoted: false
ttl_expires_at: 2026-10-14T07:32:00-04:00
---

# Pre-brief collection sweep sentinel — 2026-07-16 morning (08:00 brief)

Coverage record for the 2026-07-16 07:30 EDT pre-brief collection sweep.
Window: 2026-07-15T17:30:00-04:00 → 2026-07-16T07:30:00-04:00 (14h).

## Sources queried (healthy)

RSS/media/vendor: bleepingcomputer, securityweek, the-record, sans-isc, krebs,
unit42, mstic (microsoft.com/security parent feed), rapid7, crowdstrike,
cisa-advisories (all.xml). Authoritative feeds: cisa-kev (JSON catalog),
nvd (lastModified CRITICAL window query).

## Sources skipped (stale / no-MCP / fragile)

- mandiant — feedburner RSS dead (canonical-swap pending); direct-HTML path not swept this pass.
- msrc — feed parse error (stale since 2026-05-30); MSTIC content reaches corpus via parent feed + relays.
- ars-security — security-only feed 404 (stale 2026-05-09); root-feed workaround not needed this window.
- github-advisories — global advisories.atom 406 (per-repo GHSA fallback only, not triggered).
- dragos — blog RSS 404 (stale); no OT candidate required Dragos this window.
- threatfox / malwarebazaar — WebFetch CAPTCHA / MCP pending; no IOC enrichment required.
- censys / urlscan / hibp — no MCP / no key.
- x-cisagov / x-gossithedog — nitter bridge stale/fragile.

## Result

6 substantive raw-signal files written (am-001..am-005 + this sentinel). Highlights:
MSTIC @asyncapi npm supply-chain compromise (net-new, A-grade, live C2 IOC); F5
NGINX/BIG-IP quarterly (CVE-2026-42533 9.2 critical); Unit 42 npm threat-landscape
update (Shai-Hulud/TeamPCP lineage); plus fresh 07-16 corroborating relays for two
items already queued to this morning's brief (VT-043 Oracle EBS KEV Saturday deadline;
VT-042 LegacyHive). Evaluated-and-not-captured (already in corpus / no filter hit):
Adobe ColdFusion CVE-2026-48321 (part of already-captured 07-14 ColdFusion cluster),
KNX CVE-2023-4346 KEV add (absorbed by 06:00 FLASH, no A&D nexus), CrowdStrike
July Patch Tuesday retrospective (already captured 07-14), plus commodity items
(UAT-11795 Starland RAT, Spirals ransomware, Nichirei/KFC cold-chain, Dutch fraud
bust, Splunk/Zoom patches, UEFI shim Secure Boot bypass, Symfony Twig / WordPress
SAML / X-Rite NVD critical hits) — none matched watchlist / roster / vuln-index.

No source-health status flips observed this sweep. No policy-violation triggers.
