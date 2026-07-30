---
raw_id: raw-2026-07-30-pm-001
collected_at: 2026-07-30T15:44:00-04:00
run_id: pre-brief-20260730-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: the-record
  source_name: "The Record (Recorded Future News) — relaying Amazon threat intel"
  source_url: https://therecord.media/north-korea-hackers-amazon-malware
  published_at: 2026-07-30T09:00:00-04:00
  secondary_outlets:
    - source_yaml_id: bleepingcomputer
      source_name: "BleepingComputer (Bill Toulas)"
      source_url: https://www.bleepingcomputer.com/news/security/amazon-links-debug-chalk-npm-supply-chain-attacks-to-north-korean-hackers/
      published_at: 2026-07-30T14:13:00-04:00
match_reason:
  watchlist: []
  actors: ["002"]   # Stardust Chollima (aliases BlueNoroff, Sapphire Sleet, CopperCore Chollima)
  vulnerabilities: []
  keywords: [npm, supply-chain, DPRK, SapphireSleet, BlueNoroff, UNC1069]
triage_tags: [non_flash, tracked_actor, dprk, supply_chain, grader_queue, tracked_actor_ttp]
iocs_extracted: true
iocs_count: 5
text_word_count: 340
promoted: true
promoted_to_finding: finding-2026-07-30-0005
promoted_at: 2026-07-30T16:12:00-04:00
grading_run_id: afternoon-20260730-160000
ttl_expires_at: 2026-10-28T15:44:00-04:00
---

# Amazon attributes debug / chalk / axios npm supply-chain compromises to North Korean SapphireSleet (BlueNoroff)

**Originating primary:** Amazon threat intelligence. **Relays (in-window):** The Record (2026-07-30
~09:00 EDT) and BleepingComputer (Bill Toulas, 2026-07-30 14:13 EDT). Both are pure relays of the
Amazon report; Amazon primary NOT directly retrieved this sweep.

Amazon says a North Korean threat cluster it tracks as **SapphireSleet** was behind several
high-profile compromises of widely used open-source npm libraries. Per the relays, other vendors
track the same cluster as **UNC1069, BlueNoroff, Stardust Chollima, CageyChameleon, and Alluring
Pisces**. The cluster reportedly gained access by **socially engineering trusted package
maintainers** (not by exploiting software vulnerabilities), then published malicious updates.

**Compromised packages (per relay):**
- `typo-crypto` (March 2025)
- `debug` (September 2025)
- `chalk` (September 2025)
- `axios` (March 2026) — noted at >100M weekly downloads, "embedded in countless web applications
  and enterprise services"

Payload family tracked as **MAL-2026-3400** in the Open Source Vulnerabilities (OSV) database.
Reported objective: theft of passwords, cryptocurrency, and personal data. Google and Microsoft
had previously attributed / linked the `axios` compromise to North Korean actors; Amazon's report
consolidates the maintainer-social-engineering methodology across the four packages.

**Roster relevance:** SapphireSleet / BlueNoroff maps to **Stardust Chollima (#002)** via the
`_roster.yaml` aliases (`BlueNoroff`, `Sapphire Sleet`). Note the alias `UNC1069` also appears in
Mandiant source-health awareness notes as a prior /new-actor candidate — recorded here verbatim,
NOT merged (Hard Rule 2). Supply-chain relevance to A&D is **structural/indirect**: npm maintainer-
compromise → malicious dependency updates is the same operational template that would reach a
Tier-1 A&D SDLC (cf. the Shai-Hulud / node-ipc corpus precedents); **no A&D victim named**.

---

## Extraction notes

- Language: en
- Publisher byline: The Record (no byline) / BleepingComputer (Bill Toulas)
- Article type: blog/news (vendor-report relay)
- Raw IOC extraction invoked: yes
- Copyright: <15 words quoted per source (Hard Rule 6); Amazon primary pending direct retrieval

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  - type: npm_package
    value: "typo-crypto"
    context: "malicious version published ~March 2025"
    confidence: reported
  - type: npm_package
    value: "debug"
    context: "malicious update ~September 2025 (legitimate package compromised via maintainer social-engineering)"
    confidence: reported
  - type: npm_package
    value: "chalk"
    context: "malicious update ~September 2025 (legitimate package compromised)"
    confidence: reported
  - type: npm_package
    value: "axios"
    context: "malicious update ~March 2026 (>100M weekly downloads); previously linked to DPRK by Google + Microsoft"
    confidence: reported
  - type: malware_id
    value: "MAL-2026-3400"
    context: "OSV-database designation for the payload family"
    confidence: reported
# No atomic domains / IPs / hashes / wallet addresses present in the relay layer.
attribution_claims:
  - actor: "SapphireSleet"
    aka: [UNC1069, BlueNoroff, "Stardust Chollima", CageyChameleon, "Alluring Pisces"]
    nation: "North Korea (DPRK)"
    claimed_by: "Amazon (threat intelligence)"
    language: "Amazon 'identified' the group; Google/Microsoft previously 'attributed'/'linked' the axios compromise to North Korean actors"
    confidence_source: "vendor report (relay-level; Amazon primary not directly retrieved)"
    roster_match: "#002 Stardust Chollima (via BlueNoroff / Sapphire Sleet aliases)"
    note: "Recorded verbatim per Hard Rule 2. Archimedes does not originate or upgrade attribution."
```
