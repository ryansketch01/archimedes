---
raw_id: raw-2026-05-21-pm-004
collected_at: 2026-05-21T15:40:00-04:00
run_id: pre-brief-20260521-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: unit42
  source_name: "Palo Alto Unit 42"
  source_url: https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
  published_at: 2026-05-21T11:30:00-04:00     # May 21 update at 8:45 a.m. PT = 11:45 a.m. EDT (article shows 15:30 GMT in feed = 11:30 EDT)
  source_grade: A
  byline: "Unit 42"
sweep_window:
  start: 2026-05-21T08:00:00-04:00
  end: 2026-05-21T15:30:00-04:00
match_reason:
  watchlist:
    - aerospace-defense                # Mini Shai-Hulud npm/PyPI worm CI/CD scope persists A&D supplier-chain risk
  actors:
    - TeamPCP                          # Attribution carry-forward from prior coverage (Wiz / StepSecurity high-confidence; this update does NOT change attribution layer)
  vulnerabilities:
    - CVE-2026-45321                   # GHSA-g7cv-rxg3-hmpx, Mini Shai-Hulud npm self-replication CVE (per finding-2026-05-12-FLASH-0001 lineage)
  keywords:
    - mini_shai_hulud_npm_pypi_worm
    - antv_npm_packages_compromise
    - bun_runtime_execution
    - gh_auth_token_credential_access
    - cortex_xdr_xql_detection_query
    - koi_agentic_endpoint_security
    - unit_42_live_document_update_cycle
    - detection_engineering_operationalization
    - third_24h_update_cycle
triage_tags:
  - procedural_facts_upgrade
  - detection_engineering_layer
  - defender_tooling_addition
  - no_new_iocs_no_new_cves_no_attribution_change
  - update_to_morning_finding_0007
iocs_extracted: false                            # Sanitized "gh auth token" is detection-pattern not IOC; XQL query is detection-rule reference not raw IOC
iocs_count: 0
text_word_count: 470
promoted: false
rejected_at: 2026-05-21T16:38:00-04:00
rejection_id: reject-2026-05-21-0002
rejection_note: "Procedural-facts upgrade to morning finding-2026-05-21-0007 (MSTIC + Unit 42 same-day co-pub on Mini Shai-Hulud); no new IOCs/CVEs/attribution/TTPs per collector. Briefer may surface as one-liner update in afternoon brief if useful. Not a standalone finding warrant."
ttl_expires_at: 2026-08-19T15:40:00-04:00
---

# Unit 42 npm Threat Landscape Update — May 21 cycle adds Cortex XDR managed-threat-hunting XQL detection + Koi Agentic Endpoint Security integration

## Source extraction

**Source**: Unit 42 blog, "The npm Threat Landscape: Attack Surface and Mitigations" — a Unit 42 live document, byline "Unit 42" institutional team.

**Article URL**: https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/

**Update timestamp**: 2026-05-21 at 8:45 a.m. PT (11:45 a.m. EDT) per article page metadata. Feed publication timestamp 15:30 GMT (11:30 EDT) reflects the update's RSS surfacing.

**Update cycle context**: This is the THIRD 24h update cycle on the live document.

| Cycle | Date | Substantive change |
|---|---|---|
| 1 | 2026-05-19 | Initial coverage / pre-@antv compromise |
| 2 | 2026-05-20 (12:30 p.m. PT) | Added the two May 2026 campaign waves + "Mini Shai-Hulud Continues" section (this is what was covered in this morning's brief finding-2026-05-21-0007 as the co-published MSTIC + Unit 42 surface) |
| 3 | 2026-05-21 (8:45 a.m. PT) | Added managed-threat-hunting XQL query + Koi defensive-tool integration |

## What changed in the May 21 update (verbatim from WebFetch)

**Added — XQL query for detection**: A Cortex XDR query designed to "identify the Mini Shai-Hulud installation activity at various stages" by tracking JavaScript execution through Bun runtime in combination with credential access commands like `gh auth token`. This operationalizes the post-compromise TTP chain documented in this morning's MSTIC + Unit 42 co-publication into a deployable detection.

**Added — Product protection update**: Koi Agentic Endpoint Security was introduced as a defensive-tool integration allowing customers to delay automatic package updates. This is a npm-ecosystem-specific control: by gating package update auto-apply behind a policy delay window, defenders create time for the npm registry to detect and remove compromised packages before they propagate into developer machines and CI/CD runners.

## What did NOT change in the May 21 update

- **No new IOCs** (domains / IPs / hashes / package names)
- **No new CVEs** (CVE-2026-45321 / GHSA-g7cv-rxg3-hmpx remains the canonical reference)
- **No new actor attribution** (TeamPCP attribution layer unchanged — still tracks the prior Wiz / StepSecurity-originating high-confidence assessment)
- **No new TTPs** beyond the Bun + /proc PID scanning + Runner.Worker memory scraping + 1Password CLI 2FA bypass + K8s SA tokens + AWS Secrets Manager + HashiCorp Vault + npm OIDC + SLSA forgery + PBKDF2 obfuscation set already documented in the 2026-05-20 update layer

## Hard Rule 2 — attribution language preservation

This morning's finding-2026-05-21-0007 noted that **MSTIC and Unit 42 used unattributed-actor framing on the @antv coverage**, and that two A-grade vendors declining to name an actor on a TeamPCP-claimed campaign was a notable analytic signal. The May 21 update does NOT change that framing — Unit 42 continues to write about "Mini Shai-Hulud" the campaign / malware family without attributing to TeamPCP.

The morning brief's ACH read remains valid: most-likely explanation is editorial scope choice; telemetry-disagreement and genuine-attribution-uncertainty cannot be ruled out and run close to even. Today's update neither confirms nor denies — it operationalizes the defender layer without touching the attribution layer.

## A&D relevance — Tier-1 direct (carry-forward)

Carry-forward from this morning's finding-2026-05-21-0007. Every Tier-1 prime SDLC running modern npm-dependent dev/build pipelines is structurally inside Mini Shai-Hulud's targeting envelope. The May 21 Cortex XDR query + Koi integration give Palo Alto-equipped IR teams an immediate deployable detection / preventative control; teams on other EDR stacks should request equivalent queries from their vendor.

## Cross-finding correlation

This is an **update on this morning's finding-2026-05-21-0007** (MSTIC + Unit 42 same-day co-publication). Recommend grader treat this as procedural-facts upgrade to the existing finding rather than a new standalone finding. The cycle-3 update pattern itself (a same-vendor live document updating 3 times in 48h) is worth grader-side awareness — Unit 42 is treating Mini Shai-Hulud as a multi-cycle ongoing-campaign monitoring exercise, not a one-shot disclosure.

## Extraction notes

- Language: en
- Article type: blog (vendor-research live document)
- Raw IOC extraction invoked: no — XQL query is detection-rule reference, not IOC; "gh auth token" command pattern is technique not indicator
- 15-word quote limit observed
- Update cycle pattern is the consequential metadata, not the technical content (which carries forward)
