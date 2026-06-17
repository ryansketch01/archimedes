---
raw_id: raw-2026-06-17-pm-002
collected_at: 2026-06-17T15:40:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: the-register
  source_name: The Register (uncredited byline)
  source_url: https://www.theregister.com/cyber-crime/2026/06/17/massive-password-stealing-attack-hits-75k-fortinet-firewalls/5257877
  published_at: 2026-06-17T13:27:40-04:00
match_reason:
  watchlist: [aerospace-defense]
  actors: []
  vulnerabilities: []
  keywords: [Fortinet, FortiGate, VPN, FortiBleed, Hudson Rock, Diachenko, NATO defense contractor]
triage_tags: [fortibleed_substrate_strengthening, dual_publisher_relay, ir_vendor_corroboration, ad_sector, named_a&d_victim_hint, watch_item]
iocs_extracted: true
iocs_count: 0
text_word_count: 600
promoted: true
promoted_to_finding: finding-2026-06-17-0002
promoted_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:40:00-04:00
---

# Massive password-stealing attack hits 75k Fortinet firewalls

The Register, 2026-06-17 17:27 UTC.

If you have a Fortinet firewall, it's time to stop and change your passwords. Intruders somehow gained access to around 75,000 Fortinet firewall devices and stole credentials belonging to major corporations across 194 countries, in some cases leading to full network compromise.

## Verification

Security researchers verified the data, and the cracked FortiGate passwords belong to accounts spanning multinational corporations including FoxConn, Samsung, Comcast, Siemens, Lenovo, FedEx, PwC, Accenture, Oracle and many others.

## Hudson Rock framing (verbatim short quote)

Hudson Rock's analysis blog post:

> "The scale of this breach touches nearly every sector of the global economy, sparing no industry. The threat actors have built a verified database of working credentials for some of the largest enterprises on the planet."

Hudson Rock said the leak affects 21,632 unique domains.

## Diachenko technical-attribution detail

Volodymyr "Bob" Diachenko first spotted the intrusions and attributed them to a Russian-speaking group:

> "They intercept SSL VPN authentication, crack hashes on a 45-GPU cluster managed via Hashtopolis, and pivot into internal Active Directory environments."

> "The operation processed 1.16 billion credential attempts against 320,777 FortiGate targets and 2.1 billion attempts against 163,650 MSSQL servers."

Diachenko said the criminals fully pwned at least four organizations, including a Turkish NATO defense contractor, and, in that case, stole classified defense documents.

## Beaumont verification

Beaumont:

> "the data is legit. I have worked with several orgs listed, and can confirm the logins and passwords are real."

> "Many of the devices sampled are on fairly recent patches."

## Scale per Shodan

Per device search engine Shodan, the massive heist comprises about half of all internet-facing Fortinet firewalls. Beaumont noted most of the compromised Fortinet devices remain online.

## Fortinet response

The Register reached out to Fortinet and the companies affected by the so-called FortiBleed campaign for comment. Lenovo said it was looking into it; The Register did not receive responses from the others at time of publication.

---

## Extraction notes

- Language: en
- Publisher byline: uncredited (The Register editorial)
- Article type: news relay; second publisher behind BleepingComputer-Abrams on the same Hudson Rock + Diachenko + Beaumont substrate
- Substrate role: STRENGTHENS finding-2026-06-17-0002 — moves journalistic-relay layer to triple-publisher (SW-Kovacs morning + BC-Abrams + TR uncredited) AND adds Hudson Rock as a second IR-vendor source independent of SocRadar (substrate-pivot on IR-vendor-cardinality layer)
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
    - actor: "Russian-speaking group" (Diachenko's broad attribution preserved per Hard Rule 2)
      source: Diachenko via The Register relay
      hard_rule_2_note: "Same as raw-2026-06-17-pm-001; do not cross-walk to roster-tracked actor."
  scale_observations:
    - "75000 Fortinet firewall devices (Register framing — round number)"
    - "194 countries"
    - "21632 unique domains (Hudson Rock)"
    - "1.16B credentials attempted against 320,777 FortiGate targets"
    - "2.1B credentials attempted against 163,650 MSSQL servers"
    - "About half of all internet-facing Fortinet firewalls per Shodan"
  named_corporate_victims:
    - FoxConn
    - Samsung
    - Comcast
    - Siemens
    - Lenovo
    - FedEx
    - PwC
    - Accenture
    - Oracle
    - "Turkish NATO defense contractor (unnamed)"
  ir_vendor_observations:
    - vendor: Hudson Rock
      role: primary IR-vendor analysis of the dataset
      stake: independent of SocRadar (substrate-pivot — second IR-vendor on FortiBleed cluster)
    - vendor: Kevin Beaumont
      role: independent verification of data authenticity
```
