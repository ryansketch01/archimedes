---
raw_id: raw-2026-06-19-am-000-sentinel-pre-brief-sweep
collected_at: 2026-06-19T07:33:00-04:00
run_id: pre-brief-20260619-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: archimedes-internal
  source_name: Archimedes Collector Sentinel
  source_url: null
  published_at: 2026-06-19T07:33:00-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [sentinel, sweep_record]
triage_tags: [sentinel, pre_brief_collection, am_brief_substrate, non_promotion]
iocs_extracted: false
iocs_count: 0
text_word_count: 240
promoted: false
ttl_expires_at: 2026-09-17T07:33:00-04:00
---

# Sentinel — 2026-06-19 07:30 EDT Pre-Brief Collection

Internal sentinel substrate recording that the 2026-06-19 07:30 EDT pre-brief collection ran. Never promoted to finding; simply records that the sweep happened.

## Sweep summary

- **Window:** 2026-06-18T17:30:00-04:00 → 2026-06-19T07:30:00-04:00 (14h)
- **Sources queried (productive):** BleepingComputer, The Hacker News, SecurityWeek, The Record, Help Net Security, Dark Reading, Security Affairs, Krebs on Security, ISC SANS, Ars Technica, The Register, Mandiant (direct HTML), Cisco Talos, Unit 42, Check Point Research, WeLiveSecurity, Sophos Threat Research, Rapid7, Wired Security, CISA News, CISA Advisories, CISA KEV
- **Items fetched (in-window):** ~35 items across feeds
- **Items matched watchlists / roster / vuln-index:** 6 substrate-shifting items
- **Raw-signal files written (this sweep, beyond sentinel):** 6 (FortiBleed scale revision + Klue/Icarus cybersecurity victim cluster + Splunk CVE-2026-20253 triple-publisher relay + SocGholish takedown + Thiel Dialog Club leak + Mandiant ShinyHunters PeopleSoft Education sector)

## Splunk first-party sentinel

- **Query:** `(index=archimedes OR index=defenseclaw_local) NOT sourcetype IN (archimedes:operation, archimedes:scheduler) earliest=-14h`
- **Hit count:** 0
- **Consecutive clean sweeps:** 27th since 2026-06-13 18:00 EDT (~138h continuous clean window)
- **Visibility caveat:** Per Hard Rule 8, silent Splunk does NOT disconfirm. Frank is not a North American medical research / military health institution running REDCap, not a Higher-Ed PeopleSoft tenant, not a Splunk Enterprise self-hosted deployment, not a Fortinet VPN endpoint, not a Salesforce-Klue-integration tenant, not a Cisco SD-WAN/ISE shop, not a FortiSandbox shop, not a Rockwell PAC environment, not a Joomla/LiteSpeed CMS shop, not an NGINX edge-component deployment, not a Mastra-npm-AI-app-framework deployment, not a JetBrains-Marketplace AI tenant.

## Source-health changes this sweep

None. ISC RECOVERED to 200 OK with 1 in-window item (4th consecutive sweep recovery confirmed from 5c3c9ae 18:00 intermittent parse-error pattern). All previously-stale entries unchanged (mandiant feedburner RSS, proofpoint, sophos top-level, msrc, industrialcyber, volexity feed, shadowserver feed).

## Anti-noise carry-forwards (BINDING this sweep)

- UNC6508/INFINITERED 72h FLASH dedup BINDING through 2026-06-19 12:00 EDT (T+4.5h from sweep)
- MSTIC Crypto Clipper / CryptoBandits under-24h dedup BINDING (SW-Arghire re-publication is third-publisher relay, same MSTIC research)
- CVE-2026-20253 Splunk Enterprise — substrate-pivot UPDATE active for AM brief composition, not net-new
- FortiBleed finding-2026-06-17-0002 — substrate-pivot UPDATE active for AM brief composition (CISA government attestation 06:00 sweep + SocRadar 86,644 scale revision THIS sweep)
- Klue/Icarus operator-deferred /new-actor candidacy — substrate strengthening this sweep, Hard Rule 2 BINDING preserves Icarus as net-new
