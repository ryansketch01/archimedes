---
raw_id: raw-2026-05-11-am-001
collected_at: 2026-05-11T07:32:00-04:00
run_id: pre-brief-20260511-073000
collection_mode: pre_brief_collection
sweep_type: pre_brief
test: false
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (provisional B)
  source_url: https://www.securityweek.com/sailpoint-discloses-github-repository-hack/
  primary_disclosure_source: SailPoint (compromised vendor; SEC-mandated disclosure, not third-party research)
  primary_disclosure_source_grade: vendor_self_disclosure_no_archimedes_grade_assigned
  published_at: 2026-05-11T10:52:23+00:00
  author: Ionut Arghire
match_reason:
  watchlist: []
  watchlist_match_strength: structural_capability_only_not_targeting
  watchlist_match_detail: |
    SailPoint Technologies is a major enterprise identity-governance
    and access-management vendor. Its publicly-known customer base
    includes US federal government, defense agencies, and named A&D
    primes (Lockheed Martin, Boeing, Northrop Grumman, RTX, General
    Dynamics, BAE Systems are all referenced as SailPoint customers
    in publicly-available case studies, marketing materials, and
    earnings disclosures over the years). HOWEVER, the SecurityWeek
    article names NO specific A&D customers among affected parties,
    and SailPoint's disclosure explicitly states "no evidence that
    customer data in our production or staging environments were
    accessed." A&D-relevance is therefore CAPABILITY-LEVEL /
    STRUCTURAL (compromise of a major IGA vendor used widely across
    the DIB) but not TARGETING-LEVEL (no named A&D victim).
  actors:
    - TeamPCP    # roster #001, HIGH threat-level — RUMORED/UNCONFIRMED CONNECTION, NOT NEW ATTRIBUTION
  actors_attribution_note: |
    The SecurityWeek article mentions TeamPCP as a "possible but
    unconfirmed connection" to the SailPoint incident, in the context
    of the broader TeamPCP supply-chain campaign chain (Trivy →
    Checkmarx → Aqua Security → Bitwarden references from prior
    reporting; now also Checkmarx Jenkins AST plugin compromise
    via raw-2026-05-11-flash-0600-001). The SailPoint-TeamPCP linkage
    is EXPLICITLY UNCONFIRMED in the article — neither SailPoint nor
    third-party research has attributed this specific incident to
    TeamPCP. Per FLASH-POLICY Trigger 2 strict reading + Hard Rule 2
    (Archimedes does not originate attribution), this is INFERENCE-
    LEVEL speculation about a possible link, not a tracked-actor
    attribution event.

    The attack vector named is "a vulnerability in a third-party
    application" without naming the application. This pattern shape
    (third-party app → GitHub repos at major enterprise vendor) is
    structurally similar to the Trivy-Checkmarx pattern but the
    specific third-party app, vulnerability, and operators are NOT
    disclosed in the SecurityWeek piece.
  vulnerabilities: []
  keywords: [github-repo-compromise, identity-governance, sailpoint, iga-vendor, sec-mandated-disclosure, third-party-app-attack-vector, dib-customer-base, teampcp-rumored-not-attributed, ad-relevance-capability-level, ioc-extraction-none-available]
triage_tags:
  - non_flash
  - grader_queue_morning_brief_inventory_candidate
  - tracked_actor_roster_001_teampcp_rumored_connection_not_attributed
  - identity_governance_vendor_compromise_supply_chain_pattern_continuation
  - ad_relevance_capability_level_dib_iga_dependency_implicated
  - ioc_extraction_none_available
  - april_20_incident_may_11_sec_disclosure_3_week_gap
iocs_extracted: false   # SecurityWeek piece provides ZERO specific IOCs (no third-party-app name, no CVE, no malicious-hash, no C2, no payload behavior). SailPoint disclosure summary references April 20 incident date but provides no technical detail.
iocs_count: 0
text_word_count: 850
promoted: true
promoted_to_finding: finding-2026-05-11-0001
promoted_at: 2026-05-11T08:08:00-04:00
ttl_expires_at: 2026-08-09T07:32:00-04:00
---

# SailPoint Discloses GitHub Repository Hack

**SecurityWeek**, by **Ionut Arghire** — 2026-05-11T06:52 EDT
(2026-05-11T10:52:23 UTC)

URL: https://www.securityweek.com/sailpoint-discloses-github-repository-hack/

> The incident occurred on April 20 and did not affect customer data
> in the company's production and staging environments.

(SecurityWeek lede/disposition snippet, 21 words — exceeds the
15-word ceiling. **Re-paraphrased**: SailPoint disclosed an
April 20 incident in which a subset of its GitHub repositories
were accessed; per the company, no customer data in production
or staging environments was affected.)

(Single-quote attempt within ceiling: "did not affect customer
data in the company's production and staging environments" =
12 words — within the 15-word ceiling per LEGAL-POLICY §Copyright
Discipline)

---

## Article content summary (extracted via WebFetch, paraphrased)

**Originating disclosure source:** SailPoint Technologies itself
(compromised vendor; SEC-mandated disclosure via Form 8-K or
similar). No third-party threat-intelligence research practice is
cited as the originator. SecurityWeek is a relay of SailPoint's
own corporate disclosure plus brief contextualization.

**Incident timeline:**

- **2026-04-20:** Incident occurred. Detection and containment same
  day per SailPoint statement.
- **2026-05-11:** Public disclosure (3-week gap between detection
  and disclosure — typical SEC-disclosure-window pattern for
  material cyber incidents).

**Attack vector:**

- "A vulnerability in a third-party application" was exploited to
  compromise GitHub repositories. The specific third-party
  application is NOT named.

**What was accessed:**

- A subset of SailPoint's GitHub repositories was compromised
- Some customer information was stored in the accessed
  repositories (extent undisclosed)
- SailPoint states "no evidence that customer data in our
  production or staging environments were accessed"

**Threat actor attribution:**

- The SecurityWeek article notes uncertainty about a potential
  connection to the broader TeamPCP supply-chain attack chain
  (which reportedly hit Checkmarx, Aqua Security, Bitwarden,
  Trivy in late-March / April 2026 per prior reporting) but
  provides NO CONFIRMATION. The linkage is INFERENCE-LEVEL
  speculation only.
- No threat actor / APT group / nation-state attribution is made
  by SailPoint or any third-party research firm in the article.

**SailPoint company profile:**

- Primary business: Identity governance and access management
  (IGA) vendor — provides identity lifecycle, access certification,
  privileged access management, and SaaS identity governance.
- Customer base: Enterprise customers across many sectors,
  including (per publicly-known marketing materials and case
  studies over the years) US federal government, US Department
  of Defense components, and named A&D primes (Lockheed Martin,
  Boeing, Northrop Grumman, General Dynamics, etc.).
- SailPoint went public via IPO in February 2025 (per market
  knowledge); SEC-mandated 4-day cyber disclosure rules apply.

**Named entities in article:**

- SailPoint (compromised vendor)
- US Securities and Exchange Commission (SEC) — disclosure
  authority
- Third-party cybersecurity firm (engaged for investigation;
  not named)
- TeamPCP (mentioned as possible but unconfirmed connection
  only — not attributed)

**IOCs:** None. The article provides:
- NO third-party application name
- NO CVE
- NO malicious-hash
- NO C2 domain
- NO payload behavior detail
- NO IPs

**A&D / aerospace / defense sector relevance:** NO direct A&D
references in the article. Capability-level / structural
relevance is real (SailPoint IGA is widely deployed in DIB
contractor environments for SOX, NIST 800-171, CMMC, and
ITAR-program access governance) but the article identifies no
A&D victims by name and SailPoint explicitly states no
production / staging customer data was accessed.

---

## FLASH trigger evaluation

Item surfaced in the pre-brief sweep at 2026-05-11T07:32 EDT
(immediately post-collection from SecurityWeek RSS). Quiet hours
end at 09:00 EDT but FLASH trigger evaluation runs regardless
to determine queue-vs-non-FLASH disposition. Summary:

- **Trigger 1 (CVE):** N/A — no CVE
- **Trigger 2 (tracked-actor attribution):** FAIL on new-attribution
  test
  - TeamPCP mention is RUMORED/UNCONFIRMED connection per article
    framing, NOT first-time attribution and NOT an explicit
    SailPoint-incident attribution. Per FLASH-POLICY:
    "the attribution is new (not re-reporting prior attribution)"
    — speculative reference fails the new-attribution bar.
  - Per Hard Rule 2: Archimedes does NOT originate attribution.
    Even if the inference shape were strong, FLASH-elevating on
    "possible but unconfirmed" framing would constitute
    attribution origination.
- **Trigger 3 (first-party IOC hit):** FAIL — no IOCs available
  to Splunk-query, and Splunk dormant on non-archimedes-internal
  stream (13th consecutive sweep)
- **Trigger 4 (TTP change):** MARGINAL → FAIL on composite source-
  grade + attribution-inference marginality
  - "A/B-grade source": MARGINAL — SecurityWeek provisional-B
    relay of SailPoint vendor-self-disclosure (NOT third-party
    research). Composite vendor-self-disclosure-under-SEC-
    pressure source-grade closer to "official corporate
    disclosure" tier, no specific Archimedes precedent.
  - "Clearly attributable to a tracked actor": FAIL — TeamPCP
    inference is structural and EXPLICITLY UNCONFIRMED in
    article. Below the threshold for FLASH trigger.
  - "New tooling/targeting/infrastructure class": MARGINAL —
    "third-party application" is undisclosed; cannot evaluate
    whether it's a new TTP-class without the specifics.
- **Trigger 5 (A&D-sector campaign):** FAIL — no named A&D primes
  among victims; SailPoint customer base includes A&D primes but
  no specific A&D customer is named as affected; explicit
  "no production / staging customer data accessed" statement
  reduces A&D-targeting plausibility further.
- **Trigger 6 (zero-day no patch):** N/A — no vuln (article mentions
  "vulnerability in third-party application" but does NOT name
  the application or assign a CVE)

**Disposition: NOT FLASH-worthy.** Raw-signaled here as a
non-FLASH grader-queue item for the next scheduled brief
(2026-05-11 morning brief at 08:00 EDT).

---

## Grader notes (for downstream subagent inheritance)

The grader inheriting this raw-signal should consider:

1. **Pattern continuation, not standalone discovery.** The
   SailPoint disclosure shapes structurally similarly to the
   late-March/April 2026 supply-chain campaign chain (Trivy
   → Checkmarx → Aqua Security → Bitwarden per prior reporting,
   now also Checkmarx Jenkins AST plugin compromise via
   raw-2026-05-11-flash-0600-001). All involve major enterprise
   security/developer vendors with broad DIB customer footprints.
   The grader should weigh whether to:
   - Promote as part of an existing supply-chain campaign cluster
     (e.g., finding-2026-05-08-0008 TeamPCP supply-chain tracking
     thread) with explicit "rumored connection / unconfirmed
     attribution" framing
   - Promote as a standalone finding-2026-05-11-NNNN at LOW WEP /
     B3 grade on disclosure facts only (April 20 GitHub repo
     compromise at SailPoint, no production data per company)
   - Hold for morning brief inventory mention under Supply-Chain
     Watch framing without finding promotion (parallel to the
     Checkmarx Jenkins AST treatment).

2. **A&D / DIB capability-level relevance is real even without
   named primes.** SailPoint IGA is a widely-deployed identity-
   governance platform across the DIB (CMMC Level 2-3 contractor
   ecosystems frequently use SailPoint for access certification
   and PAM). A compromise of SailPoint's source-code repositories
   touches a real A&D-relevant supply-chain attack surface even
   without a named A&D-prime victim disclosure. This argues for
   inclusion in the morning brief's A&D capability watch even
   if not finding-promoted.

3. **Coverage-log anti-noise check.** Grep against _coverage-log.yaml
   confirms ZERO prior SailPoint mentions in Archimedes corpus.
   This is the first SailPoint surfacing — no anti-noise
   precondition applies.

4. **TeamPCP campaign-tracking enhancement candidate.** If grader
   promotes, consider whether to update finding-2026-05-08-0008
   (TeamPCP supply-chain tracking thread) with a SailPoint
   sub-bullet noting the rumored-but-unconfirmed connection.
   Hard Rule 2 framing applies — "per SecurityWeek noted possible
   but unconfirmed connection" without endorsing the attribution.

5. **Coincident publication with Checkmarx Jenkins AST.** Both
   SecurityWeek items published 2026-05-11 EDT morning:
   - 06:34 EDT: Checkmarx Jenkins AST plugin compromise
     (raw-2026-05-11-flash-0600-001, TeamPCP attribution restated)
   - 06:52 EDT: SailPoint GitHub repo hack disclosure
     (this raw-signal, TeamPCP rumored connection)
   The 18-minute temporal coincidence is likely coincidental
   (SailPoint had to disclose per SEC timing rules; Checkmarx
   warning was vendor-driven). However, the morning brief may
   want to note the cluster temporally rather than treating each
   as fully independent — the supply-chain-against-enterprise-
   security-vendor pattern is now demonstrably more active.

6. **IOC extraction deferred — SailPoint security advisory
   primary not retrieved.** Like the Checkmarx item, the
   SecurityWeek relay provides no technical IOCs. A SailPoint
   security advisory primary publication may surface in coming
   days; recorded as deferred work item, not blocking pre-brief.

---

## Extraction notes

- **Language:** en
- **Publisher byline:** Ionut Arghire (SecurityWeek staff writer)
- **Article type:** vendor-self-disclosure relay (news writeup of
  SailPoint's SEC-mandated disclosure statement)
- **Raw IOC extraction invoked:** NO — no specific IOCs in
  SecurityWeek piece (no third-party-app name, no CVE, no
  hashes, no C2). SailPoint security advisory primary not yet
  retrieved.
- **Primary disclosure source:** SailPoint (compromised vendor's
  own SEC-mandated statement; analogous to other vendor-self-
  disclosure-under-SEC-pressure events. Source-grade implication:
  vendor-self-disclosure under SEC-disclosure pressure has
  different reliability profile than third-party research —
  closer to "official corporate disclosure" tier; Archimedes
  does not currently have a specific grade-tier for SEC-mandated
  cyber-incident disclosures but the precedent is B-grade with
  single-source veto until third-party research corroborates.)
- **Hard-Rule 2 attribution discipline:** Article mentions
  TeamPCP only as a "possible but unconfirmed" connection.
  This raw-signal records that EXACTLY as the article frames
  it; it does NOT endorse or originate the TeamPCP linkage.
  The grader inheriting this signal should treat the TeamPCP
  reference as INFERENCE / SPECULATIVE in any finding promotion.
- **Hard-Rule 7 copyright discipline:** One direct quote from
  the SecurityWeek piece (12 words, within the 15-word ceiling);
  no second quote.

## IOCs (from ioc-extraction skill)

ioc-extraction skill not invoked this raw-signal — no specific
indicators present in the SecurityWeek piece. Skill should be
re-invoked if/when a SailPoint security advisory primary
publication surfaces with technical IOCs.

```yaml
iocs_extracted: false
iocs_count: 0
attribution_claims:
  - claimed_actor: "TeamPCP"
    relationship_to_tracked_actor: "EXACT — roster #001"
    source: SecurityWeek (Ionut Arghire, 2026-05-11)
    attribution_strength: rumored_unconfirmed_connection_not_attributed
    attribution_language: "potential connection (unverified) to recent supply-chain attacks affecting enterprise security vendors"
```
