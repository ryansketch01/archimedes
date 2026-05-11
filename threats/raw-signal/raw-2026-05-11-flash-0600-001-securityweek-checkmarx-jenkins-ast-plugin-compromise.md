---
raw_id: raw-2026-05-11-flash-0600-001
collected_at: 2026-05-11T06:08:00-04:00
run_id: flash-sweep-20260511-060000
collection_mode: flash_sweep
sweep_type: flash
test: false
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (provisional B)
  source_url: https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/
  primary_disclosure_source: Checkmarx (vendor-self-disclosure; compromised vendor, not third-party research)
  primary_disclosure_source_grade: vendor_self_disclosure_no_archimedes_grade_assigned
  published_at: 2026-05-11T09:34:55+00:00
  author: Ionut Arghire
match_reason:
  watchlist: []
  watchlist_match_strength: structural_capability_only_not_targeting
  watchlist_match_detail: |
    Jenkins is widely deployed in enterprise CI/CD environments
    including A&D contractors (DevSecOps pipelines for software-
    defined systems, mission software, satellite ground software,
    etc.). The SecurityWeek article names NO A&D primes among
    compromised/exposed organizations; "downstream Jenkins users"
    is the implied victim base. A&D-relevance is therefore
    CAPABILITY-LEVEL (CI/CD plugin compromise is an A&D-relevant
    attack surface) but not TARGETING-LEVEL (no named A&D victim).
  actors:
    - TeamPCP    # roster #001, HIGH threat-level — attribution chain RESTATED, not new
  actors_attribution_note: |
    SecurityWeek attributes the BROADER Checkmarx compromise chain
    to TeamPCP per prior reporting on the late-March/April Trivy
    supply-chain attack. The TeamPCP attribution is RESTATEMENT,
    not first-time naming. Per FLASH-POLICY Trigger 2 strict reading,
    this fails the new-attribution test.

    The NEW operational detail in the SecurityWeek article is the
    malicious Jenkins AST plugin version published to Jenkins
    Marketplace (2026-05-09 Friday warning) with weekend variants
    on GitHub (2026-05-10/11). The article does NOT explicitly
    attribute the new plugin variant to TeamPCP operators; the
    TeamPCP-connection inference is structural (Checkmarx is
    compromised by TeamPCP per prior reporting; new malicious
    plugin emerges from Checkmarx's distribution channel; therefore
    likely TeamPCP downstream).
  vulnerabilities: []
  keywords: [supply-chain, jenkins-marketplace, checkmarx, ci-cd-compromise, ast-plugin, teampcp-restatement, lapsus-not-in-roster, malicious-plugin-version]
triage_tags:
  - non_flash
  - flash_marginal_trigger_2_restatement_discarded
  - flash_marginal_trigger_4_marginal_composite_source_grade_discarded
  - grader_queue_morning_brief_inventory_candidate
  - tracked_actor_roster_001_teampcp_attribution_restatement
  - lapsus_new_actor_candidate_not_in_current_roster
  - ad_relevance_capability_level_not_targeting_level
  - ioc_extraction_deferred_pending_checkmarx_advisory_primary_retrieval
iocs_extracted: false   # SecurityWeek piece provides version numbers (legitimate: 2.0.13-829.vc72453fa_1c16; remediation: 2.0.13-848.v76e89de8a_053) but NO malicious-version hash, NO C2 domain, NO payload behavior detail
iocs_count: 0
text_word_count: 950
promoted: true
promoted_to_finding: finding-2026-05-11-0001
promoted_at: 2026-05-11T08:08:00-04:00
ttl_expires_at: 2026-08-09T06:08:00-04:00
---

# Checkmarx Jenkins AST Plugin Compromised in Supply Chain Attack

**SecurityWeek**, by **Ionut Arghire** — 2026-05-11T05:34 EDT
(2026-05-11T09:34:55 UTC)

URL: https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/

> A malicious version of the plugin was published to the Jenkins
> Marketplace late last week.

(SecurityWeek summary line, 13 words — within the 15-word quote
ceiling per LEGAL-POLICY §Copyright Discipline)

---

## Article content summary (extracted via WebFetch, paraphrased)

**Originating disclosure:** Checkmarx itself (compromised vendor)
via its own statement and company blog. No third-party threat-
intelligence research practice is cited as the originator. The
SecurityWeek piece is a relay of Checkmarx's vendor-self-disclosure
plus brief contextualization of the prior Trivy / Lapsus$ chain.

**Article framing:**

- Checkmarx warned users on Friday (2026-05-09) about a malicious
  version of its Jenkins AST plugin published to the Jenkins
  Marketplace. The plugin integrates Checkmarx One platform
  functionality into Jenkins pipelines for source-code scanning.
- Checkmarx advised users to verify they are running the legitimate
  December 2025 version 2.0.13-829.vc72453fa_1c16
- Over the weekend (2026-05-10/11), two new plugin versions were
  released; remediation version 2.0.13-848.v76e89de8a_053 is now
  available on GitHub and the Jenkins Marketplace

**Attribution chain (per SecurityWeek, attributed to prior reporting):**

- **Late March 2026:** TeamPCP hacker gang accessed Checkmarx
  repositories via the Trivy supply-chain attack. Malicious
  artifacts were published.
- **April 2026:** A second wave of malicious artifacts was
  published. Lapsus$ extortion group publicly released data
  allegedly stolen from Checkmarx repositories.
- **May 9-11, 2026:** Malicious Jenkins AST plugin version
  surfaces on Jenkins Marketplace; weekend variants on GitHub
  and Marketplace; Checkmarx warns users.

**Threat actors named:**
- **TeamPCP** (Archimedes roster #001, HIGH threat-level) —
  attributed to the original late-March Trivy-Checkmarx
  intrusion. Attribution RESTATED from prior reporting, not
  first-time naming.
- **Lapsus$ / DEV-0537 / Strawberry Tempest** — NOT currently in
  Archimedes _roster.yaml. Cybercriminal extortion group with
  prior high-profile activity (Microsoft, Nvidia, Samsung,
  Okta, etc. in 2022). Could be a `/new-actor` candidate if
  the operator wishes to formalize tracking; not Archimedes'
  call to originate the addition.

**Malicious plugin payload/IOCs (per article):**
- NO malicious-version hash provided
- NO C2 domain or payload behavior detail
- NO exfiltration target or post-compromise activity described

To Splunk-hunt or first-party-IOC-sweep for the compromised
Jenkins plugin in defenseclaw_local telemetry would require
retrieving the Checkmarx security advisory primary publication
for IOC extraction. Recorded as deferred grader / operator work.

**Named victim companies/sectors:** NONE. The article discusses
Checkmarx as the compromised vendor but names NO downstream
victims or targeted sectors. The implied victim base is
"organizations running the Checkmarx Jenkins AST plugin in their
CI/CD pipelines" — broad enterprise developer base.

**CVEs/CVSS:** NONE mentioned.

**A&D / aerospace / defense sector relevance:** NO direct A&D
references in the article. Capability-level relevance is real
(Jenkins + CI/CD plugins are widely deployed in A&D contractor
DevSecOps environments for mission software, satellite ground
software, weapons software, classified-program tooling) but the
article identifies no A&D victims.

---

## FLASH trigger evaluation (recorded in primary sweep sentinel)

This item was the higher-priority of two in-window candidates for
FLASH evaluation in the 2026-05-11 00:00 → 06:00 EDT window. Full
evaluation in the sister file
`raw-2026-05-11-flash-0600-000-sentinel-clean-sweep.md`. Summary:

- **Trigger 1 (CVE):** N/A — no CVE
- **Trigger 2 (tracked-actor attribution):** FAIL on new-attribution
  test
  - TeamPCP roster #001 attribution: RESTATEMENT of prior late-
    March/April Trivy-Checkmarx reporting (already referenced in
    finding-2026-05-08-0008 line 452 and finding-2026-05-08-0003)
  - Lapsus$ named: NOT in Archimedes roster (would require
    `/new-actor` operator decision)
  - Per FLASH-POLICY: "the attribution is new (not re-reporting
    prior attribution)" — restatement fails the new-attribution
    bar
- **Trigger 3 (first-party IOC hit):** FAIL — no IOCs available
  to Splunk-query (article provides no malicious-version hash /
  C2 / payload detail), and Splunk is dormant on non-archimedes-
  internal stream (13th consecutive sweep)
- **Trigger 4 (TTP change):** MARGINAL → FAIL on composite source-
  grade + attribution-inference marginality
  - "A/B-grade source": MARGINAL — SecurityWeek B-relay of
    Checkmarx vendor-self-disclosure (NOT third-party research)
  - "Clearly attributable to a tracked actor": MARGINAL — TeamPCP
    inference is structural (downstream of prior compromise),
    not direct research-vendor attribution
  - "New tooling/targeting/infrastructure class": MARGINAL —
    Jenkins Marketplace as delivery vector is downstream of the
    existing compromise chain, not a new TTP-class
  - Hard Rule 2: Archimedes does NOT originate attribution;
    SecurityWeek's TeamPCP framing flows from prior third-party
    reporting; FLASH-elevation on downstream-inference
    attribution would violate Hard Rule 2 framing discipline
- **Trigger 5 (A&D-sector campaign):** FAIL — no named A&D primes
  among victims; "downstream Jenkins users" implied victim base
  is enterprise developers broadly, A&D-relevance is
  capability-level not targeting-level
- **Trigger 6 (zero-day no patch):** N/A — no vuln

**Disposition: NOT FLASH-worthy.** Raw-signaled here as a
non-FLASH grader-queue item for the next scheduled brief
(2026-05-11 morning brief at 08:00 EDT).

---

## Grader notes (for downstream subagent inheritance)

The grader inheriting this raw-signal should consider:

1. **Brand-new operational detail; restated attribution leg.** The
   "Checkmarx Jenkins AST Plugin malicious version on Marketplace"
   operational/delivery angle is BRAND-NEW to the Archimedes corpus
   (grep on threats/ tree: zero prior mentions of "Jenkins AST" or
   "Checkmarx Jenkins"). The TeamPCP-Trivy-Checkmarx ATTRIBUTION
   CHAIN is RESTATEMENT — already referenced in:
   - finding-2026-05-08-0008 line 452: "potential connection
     (unverified) to recent supply-chain attacks affecting
     Checkmarx, Aqua Security, Bitwarden"
   - finding-2026-05-08-0003 multiple lines: TeamPCP roster
     entry referenced repeatedly; "PCPJack operator (hedged:
     'could be a former TeamPCP operator')" hypothesis
   - briefs/_coverage-log.yaml 2026-05-08 entries
   Distinguishing these is important for the grader's promotion
   decision and digraph assignment.

2. **Promotion options:**
   - **Promote to finding** at B3 / "roughly even chance" framing
     on the downstream-inference attribution leg (Hard Rule 2
     compliant: "per SecurityWeek per prior TeamPCP/Trivy/
     Checkmarx reporting"); B2 / "likely" on the procedural fact
     that a malicious plugin version is now published to Jenkins
     Marketplace. Useful corpus entry for tracking ongoing
     TeamPCP supply-chain reach into CI/CD ecosystems.
   - **Reject promotion** with logged reason (restatement of
     prior attribution + no fresh IOCs + no named A&D victims +
     vendor-self-disclosure source-class makes this a "noted
     development" rather than a graded finding).
   - **Hold for morning brief inventory mention** under
     Supply-Chain Watch or A&D Capability-Watch framing without
     finding promotion.

3. **Lapsus$ source-grade-log expansion candidate.** Lapsus$ /
   DEV-0537 / Strawberry Tempest is a well-documented Microsoft-
   tracked actor with high-profile 2022 activity (Microsoft,
   Nvidia, Samsung, Okta, EA, T-Mobile breaches). Currently NOT
   in Archimedes _roster.yaml. The Checkmarx article's Lapsus$
   reference is brief but adds them to the "actors named in
   Archimedes-corpus articles but not tracked" pile (alongside
   UNC6692, UNC1069, DarkSword, etc. from prior Mandiant
   surface-only references). Operator decision required for
   `/new-actor Lapsus$` if cumulative reference pattern warrants.
   Collector does NOT originate.

4. **IOC extraction deferred — Checkmarx security advisory
   primary needed.** The SecurityWeek piece gives version-string
   anchors (legitimate 2.0.13-829.vc72453fa_1c16; remediation
   2.0.13-848.v76e89de8a_053) but no malicious-version hash, C2
   domain, or payload-behavior detail. To populate first-party
   hunt opportunities (Splunk sweep for "any host in defenseclaw_
   local that downloaded the malicious Jenkins plugin variant?"),
   the operator or grader would need to retrieve the Checkmarx
   security advisory primary publication and extract domain /
   IP / hash IOCs. Recorded as deferred work item; not blocking
   FLASH sweep.

5. **A&D-prime relevance assessment.** STRUCTURAL / CAPABILITY-
   LEVEL — Jenkins + CI/CD plugins are widely deployed in A&D
   contractor DevSecOps environments (mission software, satellite
   ground software, weapons software, classified-program tooling).
   A compromised Checkmarx plugin distributing through Jenkins
   Marketplace touches a real A&D-relevant attack surface even
   without a named A&D-prime victim. However: TARGETING-LEVEL
   relevance is undocumented (no A&D primes named in the
   SecurityWeek article; the "downstream Jenkins users" framing
   is broad enterprise). The grader should distinguish these
   when deciding promotion + framing.

6. **Tripwire potential.** The Dirty Frag 72h second-vendor
   corroboration tripwire (finding-2026-05-08-0005) is expected
   to fire during this morning brief window with no independent
   A/B-grade vendor research surfacing (SecurityWeek today is a
   relay of the same MSTIC + Hyunwoo Kim sourcing). Grader can
   evaluate whether the patches-now-available framing changes
   the supersession decision.

---

## Extraction notes

- **Language:** en
- **Publisher byline:** Ionut Arghire (SecurityWeek staff writer)
- **Article type:** vendor-self-disclosure relay (news writeup of
  Checkmarx's own company blog post)
- **Raw IOC extraction invoked:** NO — no specific IOCs in
  SecurityWeek piece beyond version strings (which are version
  IDs not IOC hashes); Checkmarx security advisory primary
  publication not yet retrieved (deferred for grader / operator
  decision)
- **Primary disclosure source:** Checkmarx (compromised vendor's
  own statement and blog — NOT third-party threat-intel research;
  source-grade implication: vendor-self-disclosure under stress
  has different reliability profile than third-party research,
  closer to "official vendor disclosure" tier; Archimedes does
  not currently have a specific grade-tier for compromised-
  vendor-self-disclosure but the precedent for similar disclosures
  has been B-grade with single-source veto until third-party
  research corroborates)
- **Hard-Rule 2 attribution discipline:** Article attributes the
  broader compromise chain to TeamPCP and Lapsus$ per prior
  third-party reporting (NOT first-time attribution in this
  piece). This raw-signal records the attribution claims with
  proper "per SecurityWeek per prior reporting" framing; it
  does NOT originate any attribution. The TeamPCP roster #001
  connection is a RESTATEMENT, not a NEW attribution event.
- **Hard-Rule 7 copyright discipline:** One direct quote from
  the SecurityWeek piece (13 words, within the 15-word ceiling);
  no second quote.

## IOCs (from ioc-extraction skill)

ioc-extraction skill not invoked this raw-signal — no specific
indicators present in the SecurityWeek piece beyond version
strings. Skill should be re-invoked if/when the Checkmarx
security advisory primary publication is retrieved and parsed
in a follow-on collection.

```yaml
iocs_extracted: false
iocs_count: 0
attribution_claims:
  - claimed_actor: "TeamPCP"
    relationship_to_tracked_actor: "EXACT — roster #001"
    source: SecurityWeek (Ionut Arghire, 2026-05-11)
    attribution_strength: restatement_of_prior_reporting_not_new
    attribution_language: "TeamPCP hacker gang accessed Checkmarx repositories in late March via the Trivy supply chain attack"
  - claimed_actor: "Lapsus$"
    relationship_to_tracked_actor: "NOT IN ROSTER — /new-actor candidate"
    source: SecurityWeek (Ionut Arghire, 2026-05-11)
    attribution_strength: restatement_of_prior_reporting_not_new
    attribution_language: "Lapsus$ extortion group publicly released data allegedly stolen from company repositories in April"
```
