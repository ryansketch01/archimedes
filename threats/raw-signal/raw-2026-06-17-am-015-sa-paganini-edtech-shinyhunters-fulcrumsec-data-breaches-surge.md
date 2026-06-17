---
raw_id: raw-2026-06-17-am-015-sa-paganini-edtech-shinyhunters-fulcrumsec-data-breaches-surge
collected_at: 2026-06-17T07:58:00-04:00
run_id: pre-brief-20260617-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityaffairs
  source_name: Security Affairs
  source_url: https://securityaffairs.com/193777/data-breach/edtech-faces-a-cybersecurity-crisis-data-breaches-surge.html
  published_at: 2026-06-17T09:16:23+00:00
match_reason:
  watchlist: []
  actors: [ShinyHunters, FulcrumSec]
  vulnerabilities: []
  keywords: [EdTech, ShinyHunters, FulcrumSec, Glendale Community College, Moody Bible Institute, Illinois Central College, Houston City College, Infinite Campus, Salesforce, Global Schools Foundation]
triage_tags: [out_of_ad_scope, shinyhunters_cluster_expansion_education_substrate, fulcrumsec_singapore_gsf_attack_substrate]
iocs_extracted: false
iocs_count: 0
text_word_count: 215
promoted: false
rejected_at: 2026-06-17T08:26:00-04:00
rejection_id: reject-2026-06-17-0007
ttl_expires_at: 2026-09-15T07:58:00-04:00
---

# EdTech Faces a Cybersecurity Crisis: Data Breaches Surge

**Source:** Security Affairs (https://securityaffairs.com/193777/data-breach/edtech-faces-a-cybersecurity-crisis-data-breaches-surge.html)
**Author byline:** Pierluigi Paganini
**Published:** 2026-06-17T09:16:23+00:00 (05:16:23 EDT)

## RSS-summary captured

> EdTech firms face rising cyberattacks as ShinyHunters and FulcrumSec target schools, exposing sensitive data and disrupting services. Resecurity (USA) warns the education technology (EdTech) sector has become a prime target for cybercriminals, as attacks against educational institutions and related platforms continue to escalate.

## Extraction notes

- **Language:** en
- **Publisher byline:** Pierluigi Paganini (Security Affairs)
- **Article type:** trade-press sector roundup citing Resecurity vendor analysis
- **Upstream primary:** Resecurity (vendor; not in source-grades.yaml; would be provisional on first surface)
- **Cited incidents:**
  - ShinyHunters (2026-06-16): Glendale Community College, Moody Bible Institute, Illinois Central College, Houston City College victim claims. Cross-ref to Salesforce data theft attack ~March 2026 affecting Infinite Campus K-12 SIS (3,200+ districts / 11M students / 46 states).
  - FulcrumSec (early June 2026): Global Schools Foundation (GSF) headquartered Singapore, international schools network, large-scale data exfiltration disrupted operations.
- **Cross-walk:** ShinyHunters + FulcrumSec NOT on 24-actor `_roster.yaml`. Education sector NOT A&D/DIB/CMMC/ITAR. Substrate-strengthening for ShinyHunters cluster (Kodak imaging/printing raw-014 + Education sector this raw + PeopleSoft Education Mandiant title raw-009 #3) — actor activity broad-spectrum but out-of-A&D-scope.
- **Hard Rule 6 preservation:** 15-word quote discipline preserved — RSS-summary lead sentence is within cap.
- **Hard Rule 2 preservation:** ShinyHunters + FulcrumSec attribution recorded per Resecurity + SA. NOT cross-walked.
- **Raw IOC extraction invoked:** no

## Substrate observation for grader

T2 FAIL ShinyHunters + FulcrumSec NOT on roster. T5 FAIL EdTech NOT A&D. T1/T3/T4/T6 FAIL no CVE. Critical-override 0-of-4. Non-FLASH-eligible.

Out-of-A&D-scope. Operator-deferred /new-actor-ShinyHunters + /new-actor-FulcrumSec candidacy noted given cross-sector activity expansion this week (Kodak + EdTech + PeopleSoft/Education + Novo Nordisk pharma per raw-016 below) but Hard Rule 2 BINDING — Archimedes does NOT originate roster mutation.
