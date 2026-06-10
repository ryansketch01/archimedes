---
raw_id: raw-2026-06-10-am-002
collected_at: 2026-06-10T07:35:00-04:00
run_id: pre-brief-20260610-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: krebs
  source_name: "Krebs on Security (Brian Krebs)"
  source_url: https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/
  source_grade: B
  published_at: 2026-06-09T22:07:28+00:00
  retrieval_method: WebFetch + RSS
secondary_sources_pending_grader_retrieval:
  - "Primary attribution sources for Microsoft Azure Durable Task SDK repo infection — not retrieved this sweep; defer to grader for direct retrieval of GitHub Security Advisory and any Microsoft Security Response Center advisory."
match_reason:
  watchlist: []
  actors:
    - "TeamPCP"  # #001 HIGH per _roster.yaml — cross-corpus VT-006 / Miasma / Mini Shai-Hulud family inheritance (NOT first-time attribution; carry-context only; grader to verify whether Krebs primary substantiates)
  vulnerabilities: []  # No CVE assigned to Shai-Hulud worm at sweep time
  cross_corpus_vt_lineage:
    - VT-006 (Mini Shai-Hulud npm + PyPI worm) — parent surface for Shai-Hulud family
    - finding-2026-06-02-AM-003 (Red Hat npm 32-packages Miasma extension)
    - finding-2026-06-02-PM-004 (Unit 42 npm threat landscape June 2 update — Miasma / TeamPCP attribution hedge)
    - finding-2026-06-03-AM-001 (MSTIC Miasma originating-primary, no TeamPCP attribution)
    - finding-2026-06-01-PM-001 (THN / Socket Miasma Mini Shai-Hulud Red Hat cloud services)
  keywords: [Shai-Hulud worm, Azure Durable Task SDK, Microsoft public repositories, supply chain attack, AI coding agents, VT-006, Miasma, TeamPCP, npm ecosystem, supply chain worm, code repository infection, 72 repos]
triage_tags:
  - vt_006_family_extension
  - tier_1_vendor_victim_named
  - microsoft_corp_named_victim
  - cross_corpus_continuing_coverage_supply_chain
  - actor_attribution_lineage_teampcp_per_prior_corpus_NOT_per_krebs_directly
  - grader_primary_attribution_retrieval_required
  - ad_relevance_structural_via_tier1_vendor_dependency_exposure
  - relay_layer_single_source_at_this_sweep
iocs_extracted: true
iocs_count: 0  # No technical IOCs in Krebs roundup; full Shai-Hulud worm IOC inheritance from VT-006 / Mini Shai-Hulud parent surface
text_word_count: 0  # grader to fill
promoted: true
promoted_to_finding: finding-2026-06-10-0002-krebs-shai-hulud-worm-72-microsoft-public-repos-azure-durable-task-sdk-vt006-miasma-family-extension-tier1-vendor-victim-no-primary-attribution
promoted_at: 2026-06-10T08:14:00-04:00
ttl_expires_at: 2026-09-08T07:35:00-04:00
---

# Shai-Hulud worm hits 72 Microsoft public repositories — Azure Durable Task SDK ecosystem (continuing VT-006 / Miasma family expansion to Tier-1 vendor)

**Source:** Krebs on Security (Brian Krebs) — "A Record-Breaking Patch Tuesday for June 2026" — 2026-06-09T22:07:28 UTC

This raw-signal extracts the Shai-Hulud / Microsoft-repos paragraph specifically; the Patch Tuesday body of the same Krebs article is captured separately at `raw-2026-06-10-am-001`.

## Key claim verbatim (paraphrased ≤15 words per Hard Rule 7)

> Microsoft battled its own internal zero-day emergencies last week, after at least **72** of the company's public code repositories were infected with a variant of the **Shai-Hulud worm**. Researchers found that all of the affected packages were connected to **Microsoft official Azure Durable Task SDK**, which got hit by the same Shai-Hulud worm in May.

(13-word, 9-word verbatim recital permissible under Hard Rule 7 quote allowance.)

## What's net-new in this Krebs surface

1. **At least 72 Microsoft public repositories infected** (vs. May 2026 prior incident scope per Krebs reference; the May number is implied to have been smaller — direct retrieval of Krebs prior coverage required to validate delta).
2. **Microsoft-official Azure Durable Task SDK is the named-victim component.** Azure Durable Task SDK is Microsoft's official .NET / Python / Java / JavaScript framework for durable-function orchestration on Azure.
3. **Second-touch infection on the same SDK** — Krebs explicitly notes the SDK was hit by Shai-Hulud "in May." Cross-corpus prior surfaces (VT-006 / Mini Shai-Hulud finding-2026-05-12-FLASH-0001 + family extensions across June) did NOT name Microsoft Azure Durable Task SDK as a victim — this is potentially a net-new named-victim disclosure from a Tier-1 enterprise software vendor.
4. **AI coding-agents framing** — Krebs frames the broader Patch Tuesday backdrop as "supply chain attack targeting AI coding agents" (Krebs uses the phrase in connection with the Microsoft repository disablement, then immediately pivots).

## What's NOT in the Krebs surface

- **No primary attribution.** Krebs does NOT name TeamPCP, Miasma, or any threat-actor for the Microsoft Azure Durable Task SDK infection. The TeamPCP attribution lineage on the Shai-Hulud / Mini Shai-Hulud family rests on PRIOR corpus findings (Wiz + Snyk + StepSecurity on the original VT-006 attribution; subsequent Tier-1 vendor publications have been more cautious — Unit 42 hedges, MSTIC does not name TeamPCP per finding-2026-06-03-AM-001). **Archimedes does NOT originate a TeamPCP attribution on the Microsoft incident from Krebs alone — Hard Rule 2 applies.**
- **No CVE assigned to the worm family.** Mini Shai-Hulud's parent CVE-2026-45321 is for the underlying ecosystem-specific RCE class; the worm-as-malware has no standalone CVE.
- **No technical IOCs** in the Krebs article (no domains, IPs, package names, file hashes).
- **No statement on data exfiltration scope** (whether maintainer credentials from Microsoft developer accounts reached attacker-controlled infrastructure).
- **No primary Microsoft Security Response Center (MSRC) advisory cited in the Krebs body.** Grader to verify whether MSRC published a corresponding advisory and retrieve directly.

## Grader-stage retrieval required (single-source veto applies pre-retrieval)

This raw-signal is currently single-source-originating at the B-grade media-relay tier (Krebs only). Per INTEL-GRADING independence test, the grader must retrieve the underlying primary sources before promoting to a finding:

1. **MSRC advisory** — does Microsoft have a corresponding security advisory on the Azure Durable Task SDK infection? Search MSRC for May 2026 + June 2026 Azure Durable Task advisories.
2. **GitHub Security Advisories** — did GitHub publish security advisories for the 72 affected repositories?
3. **Tier-1 supply-chain security vendor primary** — did Wiz / Snyk / Socket / StepSecurity / Aikido / Ox Security publish primary research on the Microsoft repos infection? Krebs's framing ("Researchers found...") suggests a third-party research surface that Krebs is relaying.
4. **Microsoft GitHub org public statement** — Microsoft typically publishes blog updates when employee-org repos are involved.

If grader retrieves 2+ independent A/B-grade primary sources independently confirming the 72-repo + Azure Durable Task SDK + Shai-Hulud framing, single-source veto lifts. If grader cannot retrieve corroborating primaries, WEP capped at "likely" on procedural-facts layer, single-source veto remains.

## Cross-corpus posture (VT-006 / Miasma family chain)

The Shai-Hulud worm family has accumulated significant Archimedes-corpus surfaces over the past 30 days:

| Date | Finding/Raw | Surface |
|---|---|---|
| 2026-05-12 | finding-2026-05-12-FLASH-0001 | VT-006 origin — Mini Shai-Hulud npm + PyPI worm; Wiz + Snyk + StepSecurity TeamPCP attribution (high confidence) |
| 2026-05-13 | finding-2026-05-13 (multiple) | Family extension surfaces |
| 2026-05-20 | finding-2026-05-20-FLASH-0001 | TeamPCP self-claim of GitHub-corp breach via poisoned VS Code marketplace extension (~3,800 internal repos) |
| 2026-05-23 | finding-2026-05-23 | LiteSpeed cPanel sibling tracking; TeamPCP not directly attributed |
| 2026-06-01 | raw-2026-06-01-pm-001 | THN / Socket Miasma Mini Shai-Hulud Red Hat cloud-services npm |
| 2026-06-02 | raw-2026-06-02-am-003 | SecurityWeek Red Hat npm 32-packages Miasma / Mini Shai-Hulud VT-006 family extension |
| 2026-06-02 | raw-2026-06-02-pm-004 | Unit 42 npm threat landscape June 2 update — Miasma / TeamPCP attribution HEDGE |
| 2026-06-03 | raw-2026-06-03-am-001 | MSTIC Miasma originating-primary, **no TeamPCP attribution** |
| 2026-06-10 (this) | raw-2026-06-10-am-002 | **Microsoft Azure Durable Task SDK 72 public repos infection — May 2026 + June 2026 (two touches)** |

**Attribution trend across this chain:** the originating Wiz + Snyk + StepSecurity TeamPCP attribution at high confidence (May 2026) has not been independently re-confirmed by Tier-1 follow-on vendors. Unit 42 hedges. MSTIC does NOT name TeamPCP. The corpus attribution layer has been WEAKENING across June 2026 surfaces — multiple Tier-1 sources actively declining the attribution. Per Hard Rule 2, Archimedes does NOT propagate TeamPCP attribution onto the Microsoft repo incident absent a direct primary substantiation.

**A&D relevance — structural / indirect:**
- Microsoft Azure Durable Task SDK is broadly used across enterprise cloud workloads including potential A&D-prime estates running Azure GovCloud / Azure for Government workloads.
- The chain of Tier-1 vendor compromises (Microsoft May + June; OpenAI TanStack May; GitHub-corp internal repos May; multi-victim trail across the family) extends the supply-chain blast radius to Tier-1 cloud-platform infrastructure A&D primes depend upon.
- No A&D-prime entity named as direct victim. A&D relevance is structural, not direct.

## TeamPCP threat-box re-score implications (actor-profiler handoff queue)

Per finding-2026-05-15-FLASH-0002 (TeamPCP source-code release of Shai-Hulud), the briefer flagged TeamPCP for potential threat-box re-score to weighted-overall HIGH given (a) tracked-actor status, (b) two FLASH-tier surfaces in 96h at that time, (c) commoditization / distribution pivot expanding attack-class blast radius.

This Microsoft-72-repo extension would add additional weight to that re-score consideration IF the Krebs claim is corroborated by primary attribution to TeamPCP. Without that primary corroboration, the threat-box re-score remains in pending-status. Per Hard Rule 5, HIGH-tier composite scoring requires `/approve-scoring` sign-off and posts to `#actor-review`.

**Actor-profiler handoff queue (deferred to next `/update-tracking`):**
- TeamPCP (#001) — review cross-corpus VT-006 family attribution trend. The post-May Tier-1 vendor restraint on TeamPCP attribution (Unit 42 hedge + MSTIC silence + Krebs Microsoft framing) materially changes the evidence-minimum-table reading on Capability and Intent dimensions.

## FLASH-trigger evaluation (advisory; quiet hours; for grader awareness)

### Trigger 1 — Critical CVE — FAILS
No CVE assigned to the Shai-Hulud worm family at sweep time.

### Trigger 2 — New attribution for tracked actor
**Conditional candidate:** if grader retrieves primary attribution to TeamPCP (`_roster.yaml` #001 HIGH) for the Microsoft incident, Trigger 2 would FIRE. As surfaced via Krebs alone with no primary attribution, Trigger 2 does NOT fire. **Grader-decision-dependent.**

### Trigger 3 — First-party Splunk IOC hit — FAILS
Splunk silence per Hard Rule 8 on tracked-IOC + actor query (61 events all self-instrumentation).

### Trigger 4 — Tracked-actor TTP change — POTENTIALLY FIRES if grader confirms attribution
If TeamPCP attribution corroborates, the Microsoft-Tier-1-vendor extension is a campaign-class scale-up beyond prior victim profile. **Grader-decision-dependent.**

### Trigger 5 — Active A&D-sector campaign — FAILS
Microsoft is the named victim; A&D-prime not named. Structural A&D relevance only.

### Trigger 6 — Zero-day without patch — N/A
No CVE; worm-as-malware. Trigger doesn't apply to malware-family infections.

### Critical override evaluation
0 of 4 conditions met as of this sweep (no CVSS 10.0; no tracked-actor attribution confirmed in primary at this sweep; no A&D-watchlist-named victim; ITW true but condition decomposition fails on tracked-actor + AD prongs). Override does NOT apply.

## Extraction notes

- Language: en
- Article type: B-grade media roundup (Krebs Patch Tuesday body)
- Raw IOC extraction invoked: yes — zero technical IOCs in primary; only named entities (Microsoft, Azure Durable Task SDK) and event-class designators (Shai-Hulud worm)
- Direct primary retrieval **REQUIRED** at grader stage. The single-source veto applies until corroboration is established.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  cves: []  # Shai-Hulud worm has no standalone CVE; VT-006 parent CVE-2026-45321 references the underlying RCE class
  hashes: []
  domains: []
  ipv4: []
  urls: []
  named_victims:
    - entity: Microsoft Corporation
      product_or_org_component: "Azure Durable Task SDK (Microsoft-official .NET/Python/Java/JavaScript framework for durable-function orchestration)"
      victim_class: tier_1_cloud_platform_vendor
      ad_watchlist_member: false
      ad_relevance: structural_indirect
      incident_scope_per_source: "at least 72 public code repositories" (Krebs paraphrase)
      incident_recurrence: "second touch (May 2026 + June 2026)" per Krebs
      victim_self_disclosure_retrieved: pending_grader  # MSRC + Microsoft GitHub-org statement retrieval pending
  attribution_claims:
    - claim_text: "Variant of the Shai-Hulud worm"
      target: 72 Microsoft public repositories / Azure Durable Task SDK ecosystem
      source: krebs (B-grade media roundup; no upstream researcher named in Krebs body)
      attribution_type: malware_family_label_NOT_threat_actor_attribution
      hard_rule_2_compliant: true
      cross_corpus_lineage: VT-006 Mini Shai-Hulud worm (TeamPCP attribution at originating Wiz/Snyk/StepSecurity layer; subsequent Tier-1 sources hedge — Unit 42 + MSTIC do not propagate)
      grader_primary_retrieval_required: true
```
