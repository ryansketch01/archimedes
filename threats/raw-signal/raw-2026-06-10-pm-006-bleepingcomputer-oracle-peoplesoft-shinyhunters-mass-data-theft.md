---
raw_id: raw-2026-06-10-pm-006
collected_at: 2026-06-10T15:43:00-04:00
run_id: pre-brief-20260610-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer (Lawrence Abrams)"
  source_url: https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/
  published_at: 2026-06-10T18:31:57+00:00
  retrieval_method: WebFetch + RSS
secondary_sources: []
match_reason:
  watchlist: []  # No A&D-prime named victim — primarily education sector
  actors:
    - ShinyHunters  # NOT in roster — flagged for /new-actor evaluation
  vulnerabilities: []  # No CVE assigned per BC ("gadget chain of old and zero-day vulnerabilities")
  keywords: [Oracle PeopleSoft, ShinyHunters, data theft, gadget chain, zero-day, 300 instances, 100 organizations, Nottingham University, FBI portal, azurenetfiles.net]
triage_tags:
  - cybercriminal_mass_data_theft_campaign
  - shinyhunters_actor_not_in_roster_new_actor_candidate
  - oracle_peoplesoft_enterprise_erp_compromise
  - failed_fbi_breach_attempt_notable
  - iocs_published_ip_set_plus_tls_certificate_cn
  - education_sector_primary_a_d_indirect_only
  - no_named_a_d_prime_victim
  - actor_self_attestation_to_bleepingcomputer
iocs_extracted: true
iocs_count: 7  # 1 TLS cert CN + 6 IPv4 (5 contiguous block + 1 standalone + 1 third standalone)
text_word_count: 0
promoted: true
promoted_to_finding: finding-2026-06-10-0012-bleepingcomputer-oracle-peoplesoft-shinyhunters-self-attested-300-instances-100-orgs-gadget-chain-failed-fbi-attempt-7-iocs
promoted_at: 2026-06-10T16:30:00-04:00
ttl_expires_at: 2026-09-08T15:43:00-04:00
---

# Oracle PeopleSoft Servers Targeted — ShinyHunters Mass Data Theft Campaign (300 instances / 100+ orgs)

**Primary source:** BleepingComputer (Lawrence Abrams) — "Oracle PeopleSoft servers hacked in ShinyHunters data theft attacks" — 2026-06-10T18:31:57 UTC

## Key claims

### Attribution (per BC)
**ShinyHunters** self-attested responsibility to BleepingComputer, claiming "stolen data from 300 instances across more than 100 organizations" (verbatim per BC).
- ShinyHunters is a long-running extortion gang (not in current Archimedes roster — flag for /new-actor candidate review).
- Actor self-attestation directly to BleepingComputer is a notable disclosure pattern (similar to LockBit / BlackCat / Scattered Spider press-relations cadence).

### Named victim
- **Nottingham University** — only specific organization named; data published on ShinyHunters leak site.
- Primary sector: **education**.
- **No A&D / aerospace / defense / cleared contractor named** in this article.

### Failed FBI breach attempt
- BleepingComputer notes the ShinyHunters group "attempted FBI PeopleSoft portal breach unsuccessful."
- This is a notable failed-targeting data point — ShinyHunters tried to compromise the FBI's PeopleSoft instance and failed. The attempt itself is the news.

### Technical mechanism
- "Gadget chain of old and zero-day vulnerabilities" (verbatim) — no specific CVE designations published in article.
- Attack success "variable depending on instance configuration" — suggests the campaign is exploit-condition-sensitive, not universally successful.

### Timeline
- Attacks discovered: 2026-06-09 (reported to BleepingComputer).
- Public disclosure: 2026-06-10.

### Oracle response
- Oracle had **not responded** at publication time.
- No separate PeopleSoft-specific vendor statement noted.
- Suggests vendor silence on a likely-significant exploitation campaign on an Oracle product — historical pattern.

## IOCs (PUBLISHED IN ARTICLE — extract for grader + cross-corpus)

### IPv4 addresses
- 142.11.200[.]186
- 142.11.200[.]187
- 142.11.200[.]188
- 142.11.200[.]189
- 142.11.200[.]190
- 108.174.202[.]99
- 176.120.22[.]24

### Domain / TLS certificate
- **azurenetfiles[.]net** — TLS certificate CN linked to ShinyHunters infrastructure.

### Hashes
- None published in article.

### CVEs
- None published in article ("gadget chain of old and zero-day vulnerabilities" — vendor advisory missing).

## Cross-corpus context

### ShinyHunters historical context
- Long-running extortion group active since approximately 2020.
- Prior major incidents: AT&T (2024), Microsoft, AWS, etc.
- Multi-victim mass-data-theft pattern with leak-site monetization.
- **NOT currently in `_roster.yaml`** — recommend `/new-actor` candidate review given the mass-victim pattern and Oracle-product targeting class (Oracle PeopleSoft is widely deployed across A&D primes for HR / finance / supply chain).

### A&D-prime structural relevance (even without named A&D victim)
- **Oracle PeopleSoft is deeply deployed across A&D primes** for HR (employee onboarding, security clearance tracking, payroll), finance (program costing, budget), and supply chain (vendor management, contract administration). Lockheed Martin, Boeing, Northrop Grumman, RTX, BAE Systems, L3Harris all have material PeopleSoft footprints.
- ShinyHunters' mass-targeting campaign of PeopleSoft instances IS a structural defender concern for A&D primes — Nottingham University is the named victim but the 300-instance / 100-organization scope means substantially more victims exist; some may not yet be aware they are compromised.
- **No named A&D-prime victim in the corpus this hour** — preserves Hard Rule 2 (no propagation of A&D-victim claim from extrapolation).

### Failed FBI targeting as a data point
- The FBI PeopleSoft portal target attempt (and failure) is itself a notable intelligence data point — it tells defenders that ShinyHunters is actively scoping federal-class PeopleSoft instances, which implies they are scoping A&D-prime federal-contractor PeopleSoft instances as well.

## FLASH-trigger evaluation

- **Trigger 1 (critical-cve-exploited):** ⚠️ Partial — "old and zero-day" gadget chain referenced but no specific CVE; CVSS not surfaced. Doesn't cleanly meet Trigger 1 criteria.
- **Trigger 2 (tracked-actor-attribution):** ❌ ShinyHunters not in roster.
- **Trigger 5 (ad-sector-campaign):** ❌ No A&D-prime named victim.
- **Trigger 3 (first-party-ioc-hit):** ⚠️ Would require Splunk query against the published IPv4 set + azurenetfiles[.]net domain — RECOMMEND grader / on-demand Splunk enrichment on the 7 IPv4 + 1 domain.

Not a clean FLASH trigger. Brief-track candidate via Other Signal / cybercriminal-watch lane. Highly recommended for Splunk first-party hunt.

## Extraction notes

- Language: en
- Publisher byline: Lawrence Abrams (BleepingComputer recurring author)
- Article type: actor-attestation-driven cybercrime news
- Raw IOC extraction invoked: yes (below)

## IOCs (from ioc-extraction skill)

```yaml
attribution_claims:
  - source: "BleepingComputer (Lawrence Abrams) — actor self-attestation"
    actor_named: ShinyHunters
    attribution_language_verbatim: "stolen data from 300 instances across more than 100 organizations"
    confidence_language: "actor self-attestation to BC"
    hard_rule_2_compliance: "Self-attribution by actor reported as fact-of-claim; preserve verbatim; do NOT upgrade to corroborated"
    roster_status: "NOT in _roster.yaml — recommend /new-actor candidate evaluation"

cves: []  # No CVEs published — "gadget chain of old and zero-day" framing

network_iocs_extracted:
  ipv4:
    - "142.11.200.186"
    - "142.11.200.187"
    - "142.11.200.188"
    - "142.11.200.189"
    - "142.11.200.190"
    - "108.174.202.99"
    - "176.120.22.24"
  domains:
    - "azurenetfiles.net"
  domain_context: "TLS certificate CN linked to ShinyHunters infrastructure"
  hashes: []
  urls: []

named_victims:
  - victim: "Nottingham University"
    sector: education
    notes: "Data published on ShinyHunters leak site"

failed_targeting_data_points:
  - target: "FBI PeopleSoft portal"
    outcome: "Unsuccessful per BleepingComputer"
    notable: "Actor scoping federal-class PeopleSoft instances"

ad_prime_structural_relevance:
  oracle_peoplesoft_a_d_deployment: "Deeply deployed across all major A&D primes for HR / finance / supply chain"
  named_a_d_victim_in_corpus: false
  extrapolation_warning: "DO NOT extrapolate to named A&D-prime victims — Hard Rule 2 preserves Nottingham-as-sole-named-victim framing"

splunk_first_party_hunt_recommended:
  ipv4_search: "index=archimedes OR index=defenseclaw_local src_ip IN (142.11.200.186, 142.11.200.187, 142.11.200.188, 142.11.200.189, 142.11.200.190, 108.174.202.99, 176.120.22.24)"
  domain_search: "index=archimedes OR index=defenseclaw_local dest_host=*azurenetfiles* OR ssl_cn=*azurenetfiles*"
  time_range: "earliest=-30d latest=now"
```

## Notes for grader

- **ShinyHunters is NOT in _roster.yaml** — recommend `/new-actor` candidate review.
- **7 IPv4 + 1 domain published as IOCs** — strong candidate for Splunk first-party hunt query (Hard Rule 8 priority).
- **No named A&D-prime victim** preserves Hard Rule 2; do NOT propagate education-sector victim into A&D-direct campaign framing.
- **Oracle PeopleSoft structural relevance** to A&D primes is real but indirect at this hour.
- **No CVE published** — defender remediation guidance is constrained until Oracle publishes advisory or third-party IR firm identifies the gadget chain.
- **PM brief candidate** as Other Signal / cybercriminal-watch lane. Defer to grader on whether the failed-FBI-targeting angle warrants its own line.
- **Operator follow-up consideration:** /new-actor evaluation on ShinyHunters given the sustained mass-victim-targeting pattern + Oracle-product class exposure to A&D-prime estate.
