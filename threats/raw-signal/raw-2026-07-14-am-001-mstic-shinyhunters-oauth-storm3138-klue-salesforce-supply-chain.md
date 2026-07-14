---
raw_id: raw-2026-07-14-am-001
collected_at: 2026-07-14T07:33:00-04:00
run_id: pre-brief-20260714-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: mstic
  source_name: Microsoft MSTIC / Microsoft Security Blog
  source_url: https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/
  published_at: 2026-07-13T18:02:41-04:00
  originating_primary: Microsoft Threat Intelligence (MSTIC) — A-grade vendor, first-party Defender/Entra telemetry
  relay_grade: null
match_reason:
  watchlist: []
  actors: [Icarus]
  vulnerabilities: []
  keywords: [ShinyHunters, Storm-3138, Klue, Salesforce, OAuth, Salesloft Drift, Gainsight, SaaS supply chain, vishing]
triage_tags: [tracked_actor_ttp, attribution_development, saas_supply_chain, roster_icarus_klue_linkage, grader_queue_morning, non_flash]
iocs_extracted: true
iocs_count: 0
text_word_count: 620
promoted: true
promoted_to_finding: finding-2026-07-14-0001
promoted_at: 2026-07-14T08:12:00-04:00
ttl_expires_at: 2026-10-12T07:33:00-04:00
---

# Defending SaaS-based applications against ShinyHunters OAuth abuse (MSTIC)

Microsoft Threat Intelligence published defensive guidance (Microsoft
Security Blog, 2026-07-13 18:02 EDT, IN WINDOW) on a series of campaigns
observed **mid-2025 through mid-2026** that MSTIC attributes to "threat
actor activity with overlapping tradecraft commonly associated with
**ShinyHunters**." The activity abuses trusted OAuth relationships against
SaaS applications (primarily Salesforce) for unauthorized access, data
exfiltration, and persistence.

## Why this matches the roster (collector rationale — grader adjudicates)

MSTIC names **Storm-3138** as the actor that, **in June 2026, gained
access to the market-intelligence platform Klue** and used credentials to
access Salesforce customer instances "to discover, query, and exfiltrate
data." The **Klue June-2026 compromise is already roster-tracked in
Archimedes as Icarus (#025)** via finding-2026-06-19-0003 (Huntress-
attributed Klue/Salesforce supply-chain compromise, OAuth-token abuse via
legacy integration credential). This surface is therefore a same-incident
attribution/label development on a tracked actor's originating event.

**Hard Rule 2 discipline (BINDING):** Archimedes originates no attribution
and no merge. Recorded strictly as what MSTIC says: Microsoft labels the
Klue-June-2026 activity **Storm-3138** and clusters the broader campaign
set under **ShinyHunters-associated tradecraft**. Huntress labeled the same
Klue incident **Icarus**. These are two vendor labels applied to the same
underlying incident — the actor-profiler must adjudicate the relationship;
the collector asserts no equivalence. The Icarus dossier's standing SAT-KAC
open question (A1: "Icarus is a distinct actor" vs. "Huntress tracking
unattributed activity under a label") and the SAT-ACH H3 hypothesis
(UNC6395 affiliate/splinter) are directly implicated by MSTIC's naming.
Icarus roster note explicitly declined a ShinyHunters/UNC6395 cross-walk;
MSTIC's Storm-3138 label does not by itself resolve that — it is a new data
point for the actor-profiler, not a confirmation.

## Campaign detail (per MSTIC)

Three primary intrusion paths, all OAuth-trust abuse (not a Salesforce
product vulnerability — MSTIC states this explicitly):

1. **Vishing-driven OAuth consent abuse (from mid-2025):** actors
   impersonate IT support, socially engineer employees into authorizing an
   attacker-controlled connected app disguised as a legitimate "Salesforce
   Data Loader" tool; consented app then performs API calls on the victim's
   behalf — enumeration, persistent CRM access, possible lateral movement
   into other SaaS via discovered credentials.
2. **SaaS supply-chain compromise of trusted integrations:** Aug 2025
   compromised **Salesloft Drift** credentials yielded downstream OAuth
   connection secrets usable across multiple customer Salesforce instances;
   Nov 2025 campaign targeted **Gainsight**-published Salesforce-integrated
   apps for persistent API access. Activity often indistinguishable from
   legitimate integration behavior (bulk queries + mass exfil of accounts,
   contacts, case data without sign-in anomalies).
3. **Guest-access misconfiguration used for exfiltration.**

**Observed victim industries (per MSTIC):** retail, education,
manufacturing — no aerospace/defense prime named. A&D relevance is
**structural/indirect** (any large ITAR enterprise running Salesforce +
OAuth-connected third-party integrations shares the exposure surface;
Salesloft/Gainsight-class integration compromise is SDLC/CRM-supply-chain
portable). Collector originates no A&D-exposure claim.

**Mitigation framing (per MSTIC):** monitor OAuth-connected apps, validate
third-party integrations, review guest access, enable Salesforce event
monitoring; Microsoft worked with Salesforce to add near-real-time
Defender for Cloud Apps detection with connected-application attribution.

---

## Extraction notes

- Language: en
- Publisher byline: Microsoft Security Research and Microsoft Defender Security Research Team (MSTIC)
- Article type: blog (vendor defensive guidance + threat-actor characterization)
- Raw IOC extraction invoked: yes
- No atomic network IOCs (IP / domain / hash / URL) in the published body —
  the piece is defensive-guidance shaped, not an indicator drop. Storm-3138 /
  ShinyHunters / Salesloft Drift / Gainsight / Klue are actor and
  vendor/product names, not IOCs. Attribution claims recorded below.

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: mstic-2026-07-13-shinyhunters-oauth
  source_url: https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/
  extracted_at: 2026-07-14T11:33:00Z
  extracted_by: collector
  target_actor_id: null   # collector asserts no merge; grader/actor-profiler resolves Storm-3138 <-> Icarus(#025) <-> ShinyHunters
  text_word_count: 620

indicators: []   # no atomic network IOCs in the published body

attribution_claims:
  - claimed_actor: "Storm-3138 (Microsoft label)"
    ioc_ids: []
    claimed_by_source: mstic-2026-07-13-shinyhunters-oauth
    attribution_confidence_in_source: >
      Named directly as the actor that accessed Klue in June 2026 and used
      credentials against Salesforce customer instances. No confidence
      qualifier attached by MSTIC to the Storm-3138 label itself.
    requires_grading: true
    notes: >
      Same underlying incident (Klue, June 2026, OAuth-token/credential abuse
      of Salesforce instances) that Huntress attributed to Icarus and that
      Archimedes tracks as roster actor #025. Collector originates NO merge
      (Hard Rule 2). Flag for actor-profiler: bears directly on Icarus SAT-KAC
      assumption A1 and SAT-ACH hypotheses H1/H3.
  - claimed_actor: "ShinyHunters (tradecraft-overlap cluster)"
    ioc_ids: []
    claimed_by_source: mstic-2026-07-13-shinyhunters-oauth
    attribution_confidence_in_source: >
      "overlapping tradecraft commonly associated with ShinyHunters" —
      explicitly hedged as tradecraft overlap, not definitive actor identity.
    requires_grading: true
    notes: >
      MSTIC clusters the broader mid-2025→mid-2026 Salesforce OAuth-abuse
      campaign set under ShinyHunters-associated tradecraft. Hedge preserved
      verbatim. ShinyHunters is NOT a roster actor; do not originate a roster
      entry from this relay.

benign_filtered:
  - value: microsoft.com
    reason: publisher_and_reference_site
  - value: salesforce.com
    reason: named_victim_platform_not_an_ioc

extraction_warnings:
  - type: no_atomic_iocs
    ioc_id: null
    detail: "Defensive-guidance blog; no IP/domain/hash/URL indicators published. Actor labels and integration-vendor names only."
```
