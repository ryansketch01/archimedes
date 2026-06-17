---
raw_id: raw-2026-06-17-pm-001
collected_at: 2026-06-17T15:40:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer (Lawrence Abrams)
  source_url: https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/
  published_at: 2026-06-17T11:12:57-04:00
match_reason:
  watchlist: [aerospace-defense]
  actors: []
  vulnerabilities: []
  keywords: [Fortinet, FortiGate, VPN, FortiBleed, Hudson Rock, Diachenko, NATO defense contractor, Siemens, Lenovo]
triage_tags: [fortibleed_substrate_strengthening, scale_revision, ad_sector, named_a&d_victim_hint, ir_vendor_corroboration, watch_item, ad_sector]
iocs_extracted: true
iocs_count: 0
text_word_count: 1100
promoted: true
promoted_to_finding: finding-2026-06-17-0002
promoted_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:40:00-04:00
---

# FortiBleed leak exposes Fortinet VPN credentials for 73,000 devices

BleepingComputer, Lawrence Abrams, 2026-06-17 15:12 UTC.

A newly discovered data leak dubbed "FortiBleed" has exposed what appears to be a collection of Fortinet and FortiGate VPN credentials for 73,932 firewall URLs at organizations worldwide.

## Discovery and verification

- Originating researcher: Bob Diachenko (independent threat researcher), who first spotted the exposed-server intrusion.
- Hudson Rock analyzed and published the dataset analysis.
- Kevin Beaumont (independent researcher) independently verified the data: "the data is legit. I have worked with several orgs listed, and can confirm the logins and passwords are real" — and noted "Many of the devices sampled are on fairly recent patches."

## Scale documented

- 73,932 unique Fortinet firewall URLs.
- 21,632 unique domains impacted.
- 194 countries.
- ~1.16 billion credential attempts against 320,777 FortiGate targets.
- Additional ~2.1 billion attempts against 163,650 Microsoft SQL Server systems.
- Per Shodan, the volume comprises about half of all internet-facing Fortinet firewalls.
- Most compromised devices remain online at time of publication.

## Named victim organizations

Per Hudson Rock and verified by Beaumont, the dataset includes credentials for major corporations including:

- **Technology / Manufacturing:** Foxconn, Samsung, Lenovo
- **Telecom / Utilities:** Comcast, AT&T, Sinopec, State Grid
- **Automotive:** Mercedes-Benz, Toyota
- **Professional Services:** PwC, Accenture, Oracle
- **Industrial:** Siemens
- **Government and critical infrastructure operators** (unnamed)
- **A Turkish NATO defense contractor** — Hudson Rock alleges full compromise of at least four organizations including this contractor, with theft of classified defense documents

No U.S. defense primes (Lockheed Martin, Northrop Grumman, Raytheon, Boeing) explicitly named at time of writing.

## Attribution

Diachenko attributed the operation to a Russian-speaking group:

> "They intercept SSL VPN authentication, crack hashes on a 45-GPU cluster managed via Hashtopolis, and pivot into internal Active Directory environments."

> "The operation processed 1.16 billion credential attempts against 320,777 FortiGate targets and 2.1 billion attempts against 163,650 MSSQL servers."

Operational shape per Diachenko: SSL VPN authentication interception → hash cracking on 45-GPU Hashtopolis cluster → pivot into internal Active Directory.

## Response

BleepingComputer / The Register reached out to Fortinet and the affected companies. Lenovo confirmed it was "looking into it"; no responses from the others.

---

## Extraction notes

- Language: en
- Publisher byline: Lawrence Abrams (BC). Cross-relay: Connor Jones at The Register (~17:27 UTC).
- Article type: news report relaying Hudson Rock IR-vendor primary + Diachenko independent researcher primary
- Substrate context: STRENGTHENS finding-2026-06-17-0002 (SocRadar 30K-firewall surface) on:
  - Scale revision: 30K → 73,932 (more than doubled from morning-brief substrate)
  - SECOND independent IR-vendor on the campaign (Hudson Rock corroborates SocRadar's broad observation — separate dataset analysis)
  - Named A&D-prime named victim layer: Turkish NATO defense contractor explicitly named (still NOT a US A&D prime, but NATO defense contractor is A&D-prime relevant)
  - Attribution language: "Russian-speaking multi-operator threat group" per Diachenko (Archimedes preserves verbatim per Hard Rule 2; does NOT cross-walk to APT28/Sandworm)
  - Multi-victim corroboration includes Siemens, Lenovo, Mercedes-Benz, Toyota — multinational corporations with supply-chain reach into A&D
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
extracted_iocs:
  ipv4: []
  ipv6: []
  domains: []
  urls: []
  hashes: []
  email_addresses: []
  attribution_claims:
    - actor: "Russian-speaking group" (Diachenko's framing; Hudson Rock/Beaumont do not attribute beyond data verification)
      confidence: "broad-attribution-language-only"
      source: Diachenko via BleepingComputer and The Register
      hard_rule_2_note: "Archimedes preserves attribution verbatim. Does NOT cross-walk to APT28 / Sandworm / Gamaredon / Forest Blizzard or any roster-tracked actor without independent A-grade IR-vendor attribution."
  technical_observations:
    - "73932 Fortinet firewall URLs in dataset"
    - "21632 unique domains"
    - "194 countries"
    - "1.16B credential attempts against 320,777 FortiGate targets"
    - "2.1B credential attempts against 163,650 MSSQL servers"
    - "45-GPU Hashtopolis cluster used for hash cracking"
    - "Turkish NATO defense contractor allegedly fully compromised with classified documents stolen"
  named_corporate_victims:
    - Foxconn
    - Samsung
    - Lenovo
    - Comcast
    - AT&T
    - Sinopec
    - State Grid
    - Mercedes-Benz
    - Toyota
    - PwC
    - Accenture
    - Oracle
    - Siemens
    - "Turkish NATO defense contractor (unnamed by publication)"
```
