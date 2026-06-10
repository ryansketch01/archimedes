---
raw_id: raw-2026-06-10-pm-009
collected_at: 2026-06-10T15:49:00-04:00
run_id: pre-brief-20260610-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer"
  source_url: https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data/
  published_at: 2026-06-09T21:34:00+00:00  # pre-window publication but new material since AM-006 coverage
  retrieval_method: WebFetch
secondary_sources: []
material_update_context:
  prior_raw_signal: raw-2026-06-10-am-006-bleepingcomputer-thn-securityweek-servicenow-api-exploitation-pending-cve-internal-since-april-7
  prior_finding: "Promoted to morning brief — ServiceNow API exploitation, pending CVE, internal since April 7"
  new_material_in_this_signal: "More-specific endpoint identification (/api/now/related_list_edit/create), Australia-platform scope-bounding, IOC IPv4 51.159.98.241, June 5 patch date, anomalous-activity detection method"
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []  # CVE still pending per ServiceNow
  keywords: [ServiceNow, security incident, customer data exposure, /api/now/related_list_edit/create, Australia platform, anomalous activity, June 5 patch, CVE pending, configuration-dependent, requires_authentication false]
triage_tags:
  - servicenow_followup_material_update_on_am006
  - vendor_self_disclosure_servicenow
  - specific_endpoint_identification_new
  - australia_platform_scope_bounding_new
  - ioc_published_single_ipv4_51_159_98_241
  - cve_assignment_pending_servicenow_evaluating
  - anomalous_activity_detection_method
  - no_actor_attribution
  - hard_rule_2_no_actor_origination
  - splunk_first_party_hunt_candidate_via_ipv4
iocs_extracted: true
iocs_count: 2  # 1 IPv4 + 1 endpoint path
text_word_count: 0
promoted: true
promoted_to_finding: finding-2026-06-10-0015-bleepingcomputer-servicenow-incident-material-extension-am006-endpoint-api-now-related-list-edit-create-australia-platform-scope-bounding-ipv4-51-159-98-241
promoted_at: 2026-06-10T16:30:00-04:00
ttl_expires_at: 2026-09-08T15:49:00-04:00
---

# ServiceNow Security Incident — Material Extension on AM-006 (Endpoint + IOC + Scope Bounding)

**Primary source:** BleepingComputer — "ServiceNow discloses security incident exposing customer data" — 2026-06-09T21:34:00 UTC
**Material-update context:** Extends raw-2026-06-10-am-006 / finding referenced in 2026-06-10-morning brief.

## Key claims (new material since AM-006)

### Vulnerability identification (NEW)
- Vulnerable endpoint: **`/api/now/related_list_edit/create`**.
- Misconfiguration: endpoint was "allegedly configured with `requires_authentication=false` before being patched" (verbatim per BC).
- Class: **unauthenticated API access flaw** allowing attackers to "query data from customer instances" (verbatim per BC).

### Scope bounding (NEW)
- Affected scope: "primarily 'customers on the Australia platform release or made certain configuration changes'" (verbatim per BC).
- Implication: This is a configuration-dependent issue, not universal — defender lens is auditable (check if your tenant is on Australia release or carries the certain-configuration-change indicator).

### Timeline (NEW)
- **Security patch applied: 2026-06-05** (June 5, NOT today's Patch Tuesday).
- Detection method: "anomalous activity".
- Article publication: 2026-06-09.

### CVE status (carry-forward from AM-006)
- "ServiceNow says it is still evaluating whether it will publish a CVE for the issue" (verbatim per BC).
- No CVE assigned as of this hour.

### Named victims
- **None specifically identified** in this article (consistent with AM-006).

### Actor attribution
- **No threat actor attribution** — article references "attackers" without specific group naming. Hard Rule 2 preserved.

### Public disclosure mechanism
- ServiceNow issued **customer support bulletin behind login portal** rather than public CVE-style disclosure.
- **No CISA notification** mentioned in article.
- Disclosure pattern more cautious than typical vendor-on-own-product PSIRT class.

## IOCs (PUBLISHED IN ARTICLE — new since AM-006)

### IPv4 address (NEW)
- **51.159.98.241** — published as IOC per BC.

### Endpoint path (NEW)
- `/api/now/related_list_edit` — vulnerable endpoint family (and specifically `/api/now/related_list_edit/create`).

### Hashes / domains / CVE
- None published.

## Cross-corpus context

### Material extension nature
This is a **material extension** of AM-006, not a re-coverage of the same article:
- AM-006 covered the broad framing: ServiceNow API exploitation discovered internally since April 7, pending CVE.
- pm-009 adds: specific endpoint path, scope-bounding to Australia platform / configuration-change indicator, June 5 patch date, IOC IPv4 51.159.98.241, detection method.

### Brief composition guidance
- This is a **coverage-log update** to the AM-006 finding rather than a fresh standalone finding.
- PM brief candidate as either:
  - Coverage-log update line (preferred — preserves anti-repetition discipline).
  - New finding only if grader judges the IOC + endpoint specificity as standalone-worthy.

### A&D-prime defender relevance
ServiceNow is widely deployed across A&D primes for IT service management, security operations workflow, vendor management, etc. The specific endpoint identification + IOC publication enable concrete defender action:
- Splunk hunt: incoming connections to ServiceNow instances from IPv4 51.159.98.241 over the April 7 → June 5 window.
- Configuration audit: check ServiceNow Australia-platform-release tenancy + the `requires_authentication=false` configuration on `/api/now/related_list_edit/create`.

## FLASH-trigger evaluation

- **Trigger 1 (critical-cve-exploited):** ❌ No CVE assigned; CVSS not framed.
- **Trigger 3 (first-party-ioc-hit):** ⚠️ Splunk first-party hunt recommended on IPv4 51.159.98.241 — if hits, this elevates rapidly.
- **Trigger 5 (ad-sector-campaign):** ❌ No A&D-prime named victim.

Not a FLASH trigger this sweep. Strong Splunk first-party hunt candidate.

## Extraction notes

- Language: en
- Publisher byline: BleepingComputer (specific byline not surfaced this sweep)
- Article type: vendor incident disclosure follow-up
- Raw IOC extraction invoked: yes (below)

## IOCs (from ioc-extraction skill)

```yaml
attribution_claims: []  # No actor attribution

cves: []  # CVE assignment pending per ServiceNow self-disclosure

vulnerable_endpoint:
  path: "/api/now/related_list_edit/create"
  endpoint_family: "/api/now/related_list_edit"
  misconfiguration: "requires_authentication=false (before patch)"
  scope_bounding: "Customers on the Australia platform release OR made certain configuration changes"
  patch_date: "2026-06-05"
  detection_method: "anomalous activity"

network_iocs_extracted:
  ipv4:
    - "51.159.98.241"
  domains: []
  hashes: []
  urls: []
  notes: "Single IPv4 published per BC — strong Splunk first-party hunt candidate"

splunk_first_party_hunt_recommended:
  query: "index=archimedes OR index=defenseclaw_local (src_ip=51.159.98.241 OR dest_url=*/api/now/related_list_edit/*) earliest=-90d latest=now"
  rationale: "Vulnerable since April 7 internally; patched June 5; published IOC 51.159.98.241; 90d window covers the full exposure period"

cross_corpus_extension:
  prior_raw_signal: raw-2026-06-10-am-006
  prior_finding_brief_coverage: "Morning brief 2026-06-10"
  new_material_specific:
    - "Vulnerable endpoint identification: /api/now/related_list_edit/create"
    - "Scope bounding: Australia platform release or certain config changes"
    - "Patch date: 2026-06-05"
    - "IOC publication: IPv4 51.159.98.241"
    - "Detection method: anomalous activity"
    - "Disclosure mechanism: customer support bulletin behind login portal (NOT public CVE-style)"

ad_prime_defender_priority:
  servicenow_a_d_deployment: "Widely deployed across A&D primes for ITSM / SecOps workflow / vendor management"
  configuration_audit_actionable: "Check Australia-platform-release tenancy + requires_authentication=false on /api/now/related_list_edit/create"
  ioc_search_actionable: "Splunk 51.159.98.241 over -90d"
```

## Notes for grader

- **Material extension of AM-006** — recommend treating as coverage-log update rather than new standalone finding. Anti-repetition discipline preserved.
- **Hard Rule 2** preserved — no actor attribution surfaced.
- **No FLASH trigger** at this sweep, but **Splunk first-party hunt strongly recommended** on IPv4 51.159.98.241 + endpoint path. Hit on Splunk would shift to Trigger 3 immediately.
- **PM brief candidate** as coverage-log line under the AM-006 ServiceNow finding; new specifics (endpoint + IOC + scope-bounding + patch date) make it brief-worthy as an update.
- **CISA notification not mentioned** — atypical for a customer-data-exposure incident at vendor scale. Worth noting if pattern continues.
