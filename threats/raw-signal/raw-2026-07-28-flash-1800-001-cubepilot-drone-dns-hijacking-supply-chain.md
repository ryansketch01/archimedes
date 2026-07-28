---
raw_id: raw-2026-07-28-flash-1800-001
collected_at: 2026-07-28T18:06:00-04:00
run_id: flash-sweep-20260728-180000
collection_mode: flash_sweep
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (Bill Toulas)
  source_url: https://www.bleepingcomputer.com/news/security/cubepilot-drone-software-dev-hit-by-dns-hijacking-to-intercept-traffic/
  published_at: 2026-07-28T17:17:39-04:00
match_reason:
  watchlist: [aerospace-defense-adjacent]
  actors: []
  vulnerabilities: []
  keywords: [CubePilot, drone, UAV, "flight controller", "DNS hijacking", "certificate spoofing", "supply chain", firmware, Ukraine, "defense and government applications"]
triage_tags: [non_flash, ad-sector-supply-chain, uav-drone, dns-hijacking, no-attribution, single-victim, grader-queue-next-brief]
iocs_extracted: true
iocs_count: 1
text_word_count: 240
promoted: false
ttl_expires_at: 2026-10-26T18:06:00-04:00
---

# CubePilot (UAV flight-controller developer) hit by DNS hijacking; firmware supply-chain tampering risk for July 24-25 downloads

Collected in the 18:00 EDT FLASH sweep. **Not a FLASH candidate** — clears no
FLASH trigger (no CVE, no tracked-actor attribution, no first-party IOC hit, no
multi-victim nation-state campaign). Preserved as a raw-signal for the grader to
consider for the next scheduled brief on A&D-supply-chain relevance.

## What the source reports (collection only — not graded)

- **CubePilot** — Australian firm designing autopilots / flight controllers
  (the "Cube" line) for UAVs. Per the source, products are used in surveying,
  search-and-rescue, agriculture, and **defense and government applications**,
  and the firm has **supplied products to Ukraine**.
- **Attack:** DNS hijacking of `cubepilot.org` on **2026-07-24**. Attacker
  gained control of the domain's DNS settings and obtained TLS certificates
  covering all subdomains, enabling traffic interception to attacker-controlled
  infrastructure (adversary-in-the-middle via certificate spoofing).
- **Exposure claim (verbatim, <15 words per Hard Rule 7):** "credentials entered
  on any of our services on 24 July may have been captured."
- **Supply-chain / firmware risk:** CubePilot advised against flashing firmware
  downloaded on **July 24-25** pending safety verification; firmware obtained
  before July 24 is considered safe. Potential firmware-tampering vector not
  confirmed either way in the source.
- **Attribution:** NONE. No threat actor named or attributed (Hard Rule 2 —
  nothing to inherit).
- **Victim scope:** Single organization (CubePilot itself); number of affected
  downstream users undetermined per the source.

## FLASH trigger evaluation (all fail)

- Trigger 1 (critical CVE + active exploitation): no CVE. FAIL.
- Trigger 2 (new tracked-actor attribution): no actor named. FAIL.
- Trigger 3 (first-party IOC hit): Splunk 24h sweep zero hits; `cubepilot.org`
  not in Frank telemetry. FAIL.
- Trigger 4 (tracked-actor TTP change): no actor. FAIL.
- Trigger 5 (active nation-state A&D campaign, multi-victim): A&D-adjacent
  (UAV/defense/gov + Ukraine supply) BUT no nation-state attribution and
  single-victim, not a multi-victim campaign. FAIL.
- Trigger 6 (zero-day no patch): DNS/domain-account compromise, not a product
  vulnerability. FAIL.

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas (BleepingComputer, B-grade relay)
- Article type: news / incident report
- Raw IOC extraction invoked: yes (thin — only the victim's own domain surfaced)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: domain
    value: cubepilot[.]org
    context: >
      Victim's own legitimate domain, DNS-hijacked 2026-07-24. NOT attacker
      infrastructure — do not blocklist as malicious. Traffic to this domain on
      2026-07-24/25 may have been intercepted via spoofed TLS certs. Recorded
      for context only.
    confidence: reported
    first_seen: 2026-07-24
attribution_claims: []   # none — no actor attributed by source (Hard Rule 2)
credentials_observed: false
notes: >
  No attacker IPs, hashes, or attacker-controlled domains published in the
  source. Firmware-hash IOCs for the July 24-25 tampering-risk window are NOT
  provided. If a follow-on advisory publishes attacker infrastructure or a
  tampered-firmware hash, that would be a candidate state change for the
  vuln/supply-chain watch.
```
