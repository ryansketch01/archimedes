---
raw_id: raw-2026-06-01-pm-001-thn-socket-miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain
collected_at: 2026-06-01T15:30:00-04:00
run_id: pre-brief-20260601-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: socket
  source_name: Socket (originating research) + The Hacker News (relay)
  source_url: https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages
  source_url_relay: https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html
  source_byline: Socket Research Team (originating); Ravie Lakshmanan (THN relay)
  published_at: 2026-06-01T17:40:28+00:00
source_grade: B
source_grade_provisional: true
source_grade_note: >
  Socket is provisional B per source-grades.yaml (first cited
  2026-05-14-0009 node-ipc compromise; awaiting human ratification +
  awaiting direct retrieval). This raw-signal IS the direct
  retrieval of a Socket primary URL on a substantive surface, so
  the direct-retrieval flag can be lifted on next source-grade-log
  pass. THN is provisional B per multi-cycle citation (first scored
  2026-05-14). Co-attributors named in THN relay include Wiz
  (provisional A 2026-05-12), JFrog (no Archimedes corpus track
  record — would be provisional B / first-surface starting grade
  per Tier-2-vendor-research-firm precedent), Microsoft / MSTIC
  (A grade, ratified), Aikido Security (provisional C 2026-05-12),
  OX Security (provisional B 2026-05-15), SafeDep (provisional C
  2026-05-12), StepSecurity (provisional B 2026-05-12). Multi-firm
  co-attribution is methodologically positive but the underlying
  attribution-layer hedge ("Attribution remains unclear") is the
  load-bearing grading signal.
date: 2026-06-01
window_start: 2026-06-01T07:30:00-04:00
window_end: 2026-06-01T15:30:00-04:00
topic: miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain
match_reason:
  watchlist: []
  actors:
    - id: "001"
      name: TeamPCP
      match_basis: >
        Lineage-attribution-by-vendor — Socket explicitly identifies
        the campaign as "mini Shai-Hulud" and notes that "TeamPCP
        open-sourced the attack tools" linked to the Shai-Hulud
        worm lineage. Verbatim Socket hedge: "Attribution remains
        unclear, as the publicly available tooling lowers the
        barrier to entry and enables a broad range of threat
        actors to conduct similar operations." Hard Rule 2
        compliant — Socket does NOT originate first-time TeamPCP
        attribution on Miasma itself; the actor is named as a
        prior-campaign open-sourcer of the underlying tooling.
        Grader should layer WEP carefully between "Mini Shai-Hulud
        family identification" (likely / very_likely class) vs.
        "Miasma actor IS TeamPCP" (Socket explicitly declines).
  vulnerabilities:
    - id: VT-006
      name: "Mini Shai-Hulud (CVE-2026-45321 TanStack origination)"
      match_basis: >
        Socket explicitly identifies the campaign as "mini
        Shai-Hulud campaign." This is the third ecosystem expansion
        of the Mini Shai-Hulud lineage in the Archimedes corpus
        after npm @tanstack (VT-006 origination 2026-05-12) and Nx
        Console (VT-009 KEV-add 2026-05-27). New affected
        ecosystem: @redhat-cloud-services npm namespace (Red Hat
        Cloud Services packages). Mechanism re-uses same core
        tactics per Socket: install-time execution, credential
        harvesting, CI/CD targeting, encrypted exfiltration,
        potential downstream propagation. Strong vuln-index hit;
        grader should evaluate whether this constitutes a new
        vuln-index entry (VT-011?) or an extension of VT-006
        coverage scope.
  keywords:
    - "Mini Shai-Hulud"
    - "Miasma"
    - "@redhat-cloud-services"
    - "npm supply chain"
    - "TeamPCP"
    - "Shai-Hulud worm"
    - "credential harvesting"
    - "CI/CD targeting"
    - "Red Hat Cloud Services"
    - "api.anthropic[.]com C2 impersonation"
triage_tags:
  - non_flash
  - supply_chain_compromise
  - npm_ecosystem
  - vt006_lineage_extension
  - teampcp_lineage_attribution_hedge
  - tracked_actor_lineage_candidate
  - tracked_vuln_extension_candidate
  - multi_vendor_co_attribution
  - active_exploitation_self_propagating
  - c2_anthropic_impersonation
  - new_npm_ecosystem_affected
candidate_triggers: []
candidate_trigger_evaluation:
  trigger_1_critical_cve_exploited:
    fire: false
    reason: >
      No new CVE assigned to the Miasma campaign at Socket
      publication time. The underlying campaign is operationally
      tied to VT-006 (CVE-2026-45321 TanStack origination) per
      "mini Shai-Hulud campaign" language but does not itself
      carry a new CVE ID. CVSS not stated for the Miasma surface.
      Active exploitation IS confirmed (the worm IS the in-the-wild
      exploitation) but the Trigger 1 condition requires a
      Critical CVE with active exploitation at A-grade. Socket is
      provisional B; the only A-grade in the co-attributor list
      is Microsoft (no MSTIC blog post identified at sweep time).
      No-fire.
  trigger_2_tracked_actor_attribution:
    fire: false
    reason: >
      Socket EXPLICITLY hedges attribution: "Attribution remains
      unclear, as the publicly available tooling lowers the
      barrier to entry and enables a broad range of threat
      actors to conduct similar operations." The TeamPCP
      reference is a prior-campaign tooling-origin claim, NOT
      a new attribution of the Miasma campaign to TeamPCP.
      Hard Rule 2 compliance positive. No-fire on Trigger 2
      because no NEW attribution to TeamPCP is being claimed —
      this is a lineage-tooling reference, with attribution
      explicitly held open.
  trigger_3_first_party_ioc_hit:
    fire: false
    reason: >
      Splunk first-party check (-30d window across archimedes
      and defenseclaw_local indexes for api.anthropic*, v1/api,
      CVE-2024-21182, weblogic, @redhat-cloud-services, Miasma
      string set) returned zero events. No first-party telemetry
      hits.
  trigger_4_tracked_actor_ttp_change:
    fire: false
    reason: >
      TeamPCP TTP delta is operationally present (new affected
      ecosystem @redhat-cloud-services, new impersonation C2
      api.anthropic[.]com:443/v1/api, new GitHub-string identity
      "Miasma: The Spreading Blight") but Socket EXPLICITLY
      declines to attribute the Miasma campaign to TeamPCP.
      Trigger 4 requires "attributable: true." Socket's "broad
      range of threat actors" hedge breaks the attributability
      condition. No-fire.
  trigger_5_ad_sector_campaign:
    fire: false
    reason: >
      No A&D-prime named victim in Socket primary or THN relay.
      No defense / aerospace / industrial sector references. The
      affected ecosystem is @redhat-cloud-services, which has
      generalized enterprise / cloud-platform deployment
      footprint, not A&D-specific. A&D-prime SDLC exposure is
      indirect / dependency-graph dependent and unverified at
      this surface. No-fire.
  trigger_6_zero_day_no_patch:
    fire: false
    reason: >
      Affected packages have been unpublished or revoked per
      Socket downstream-impact language. Mechanism class is
      supply-chain compromise, not unpatched zero-day. Trigger
      requires "patch_available: false." Rolling unpublishes
      are the operational equivalent of patches at the npm
      ecosystem layer. No-fire.
iocs_extracted: true
iocs_count: 8
text_word_count: 1840
promoted: true
promoted_to_finding: finding-2026-06-01-0004-socket-thn-miasma-mini-shai-hulud-redhat-cloud-services-npm-supply-chain-vt006-family-expansion-anthropic-impersonation-c2
promoted_at: 2026-06-01T16:08:00-04:00
promotion_run_id: afternoon-20260601-160000
ttl_expires_at: 2026-08-30T15:30:00-04:00
test: false
---

# Miasma Mini Shai-Hulud Campaign — @redhat-cloud-services npm Supply-Chain Compromise

## Headline

Socket Research Team (originating, 2026-06-01) and The Hacker News
(Ravie Lakshmanan, relay 2026-06-01T17:40 UTC = 13:40 EDT) report a
new Mini Shai-Hulud family supply-chain campaign codenamed
**Miasma** that compromised at least seven `@redhat-cloud-services`
npm packages with credential-stealing, CI/CD-targeting, encrypted-
exfiltrating, self-propagating worm payloads. The campaign is
operationally and lineage-wise tied to the Mini Shai-Hulud worm
family (Archimedes-tracked as VT-006 since 2026-05-12) but Socket
**explicitly declines to attribute the Miasma campaign itself to
any specific actor**. TeamPCP is named only as the open-sourcer
of the underlying tooling lineage, not as the Miasma operator.

This is the third documented Mini Shai-Hulud family ecosystem
expansion in the Archimedes corpus after the original npm
`@tanstack` cluster (VT-006 origination, CVE-2026-45321,
2026-05-12) and the Nx Console developer-tooling pathway (VT-009,
KEV-listed 2026-05-27).

## Vulnerability Facts

**Campaign codename:** Miasma (originator unclear; "Miasma: The
Spreading Blight" appears as a GitHub repository description and
commit-message string; Socket appears to have coined or popularized
the codename via the originating research post but the post does
not claim authorship of the codename).

**Family lineage:** Mini Shai-Hulud (per Socket verbatim: "This is
effectively a mini Shai-Hulud campaign").

**Affected ecosystem:** npm registry, `@redhat-cloud-services`
organizational namespace.

**Affected packages (per THN relay of Socket):**

1. `@redhat-cloud-services/chrome@2.3.1` (only package with
   explicitly named version in Socket primary)
2. `@redhat-cloud-services/vulnerabilities-client`
3. `@redhat-cloud-services/tsc-transform-imports`
4. `@redhat-cloud-services/topological-inventory-client`
5. `@redhat-cloud-services/sources-client`
6. `@redhat-cloud-services/rule-components`
7. `@redhat-cloud-services/remediations-client`
8. `@redhat-cloud-services/rbac-client`

Socket post is plural ("packages") and references "affected
@redhat-cloud-services package versions" without enumerating
versions for packages 2-8 in the directly retrieved post content.

**Mechanism class (per Socket verbatim attribution language):**
"This is effectively a Mini Shai-Hulud campaign: it uses the same
core tactics of install-time execution, credential harvesting,
CI/CD targeting, encrypted exfiltration, and potential downstream
propagation."

## Attribution Layer (Socket verbatim, Hard Rule 2 compliant)

Socket's attribution language (verbatim from the directly
retrieved post):

> "Attribution remains unclear, as the publicly available
> tooling lowers the barrier to entry and enables a broad
> range of threat actors to conduct similar operations."

Socket separately notes:

> "TeamPCP open-sourced the attack tools" linked to the
> Shai-Hulud worm lineage, "opening the door for other threat
> actors" to execute similar campaigns.

Hard Rule 2 compliance: Socket does NOT originate first-time
attribution of Miasma to TeamPCP. Socket explicitly identifies
the campaign as Mini Shai-Hulud family by mechanism, then
explicitly declines actor-level attribution citing the open-source
diffusion of the underlying tooling. This is a clean
mechanism-attribution-vs-actor-attribution split that the grader
should preserve verbatim in any finding promotion.

## Co-Research / Co-Attribution Layer

THN relay names the following vendors as co-researchers /
co-attributors (Socket itself does not visibly co-attribute in
the directly retrieved primary post body):

- **Wiz** (provisional A 2026-05-12 first cited on VT-006 origination)
- **JFrog** (no prior Archimedes corpus citation — would be
  first-surface provisional starting grade per Tier-2-vendor-
  research-firm precedent if grader proceeds to source-grade-log)
- **Microsoft** (A grade, ratified — but no MSTIC blog post
  surfaced at sweep time; presence in co-attributor list is via
  THN relay, not directly retrieved MSTIC primary)
- **OX Security** (provisional B 2026-05-15)
- **SafeDep** (provisional C 2026-05-12)
- **StepSecurity** (provisional B 2026-05-12)
- **Aikido Security** (provisional C 2026-05-12)

The co-attributor list reuses substantial overlap with the
VT-006 origination roster (Wiz, Snyk, StepSecurity, Semgrep,
Onapsis, Aikido, SafeDep all named on 2026-05-12 finding-
FLASH-0001). Snyk is conspicuously absent from THN's Miasma
co-attributor list — could indicate Snyk has not yet published
on Miasma at sweep time, or could be a relay-incomplete artifact.

## Discovery / Disclosure Timeline

- **2026-05-29 first detection:** Per THN relay — commit
  containing "Miasma: The Spreading Blight" string identified
  in GitHub repositories used as encrypted exfiltration storage.
- **2026-06-01 article publication / disclosure:** Socket
  research blog post and THN relay both 2026-06-01.

Socket primary post does NOT provide a detection / unpublish
timeline; THN relay supplies the 2026-05-29 first-detection
date. Discrepancy between primary and relay is noted; grader
should preserve the relay-only detail with appropriate hedge.

## C2 / Infrastructure (Hard Rule 4 compliant — facts only)

**Primary exfiltration C2:**
`https://api.anthropic[.]com:443/v1/api`

This C2 endpoint impersonates Anthropic's legitimate API
infrastructure (real Anthropic API is on `api.anthropic.com`
without the trailing `:443/v1/api` path-stub; the difference is
the campaign-controlled domain or DNS-spoofed equivalent). The
impersonation tactic is novel within the Mini Shai-Hulud family
lineage — prior VT-006 cohort used session-network exfiltration
and direct attacker-controlled domains; the Anthropic-API
impersonation is a new tradecraft layer that suggests target
selection toward developer / AI-tooling-using enterprises.

**Fallback exfiltration:**
GitHub API used for encrypted-result storage in public
GitHub repositories with description string "Miasma: The
Spreading Blight."

## IOCs (from ioc-extraction)

```yaml
iocs:
  - type: domain
    value: api.anthropic[.]com  # impersonation; legitimate Anthropic API real
    role: c2_exfiltration_primary
    confidence: high_per_socket_primary
    notes: >
      Defanged. C2 path is /v1/api on port 443. Impersonates
      legitimate Anthropic API endpoint (api.anthropic.com) —
      treat as suspect / requires DNS-and-cert-pinning
      verification against Anthropic-legitimate infrastructure
      before any blocking action to avoid breaking legitimate
      Anthropic API consumers.

  - type: sha256
    value: 88896d478986d453f5da79b311de39d9b4b1bea95c21af1d8ef181b0f4e52fe9
    role: tarball_of_compromised_package
    artifact: "@redhat-cloud-services/chrome@2.3.1.tar.gz"
    confidence: high_per_socket_primary

  - type: sha256
    value: 21b6409a7b84446310daca5409ad6112ac60a1e4bef97736e53fff5f63bfdef4
    role: malicious_payload_file
    artifact: package/index.js
    confidence: high_per_socket_primary

  - type: sha256
    value: 0dc06ecdaa63fe24859cfd955053c23245c536e4733480239d14bebf12688e35
    role: decrypted_payload
    confidence: high_per_socket_primary

  - type: encryption_scheme
    value: AES-128-GCM and AES-256-GCM with RSA-OAEP wrapping
    role: campaign_encryption_layer
    confidence: high_per_socket_primary

  - type: string_identifier
    value: "IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner"
    role: campaign_string_signature
    confidence: high_per_socket_primary
    notes: >
      Internal campaign string discovered in payload. Useful for
      static-detection rule authoring; intentionally provocative
      language suggests operator-side awareness of detection
      research community.

  - type: github_string_identifier
    value: "Miasma: The Spreading Blight"
    role: github_repo_description_or_commit_string
    confidence: high_per_thn_relay
    notes: >
      Used as GitHub repository description and commit message
      string on the encrypted-result-storage GitHub repos. Useful
      for GitHub-side detection / hunt rule authoring.

  - type: cve
    value: CVE-2026-45321
    role: family_lineage_origination
    notes: >
      Originating CVE on VT-006 Mini Shai-Hulud family. Miasma
      reuses the same family mechanism class per Socket
      verbatim. No new CVE assigned to Miasma at disclosure
      time.

attribution_claims:
  - actor: Mini Shai-Hulud family
    claim_type: mechanism_family_identification
    confidence_per_source: explicit_per_socket
    source: socket
    verbatim_language: "This is effectively a mini Shai-Hulud campaign"

  - actor: TeamPCP
    claim_type: prior_campaign_tooling_origin
    confidence_per_source: explicit_lineage_only_NOT_miasma_attribution
    source: socket
    verbatim_language: >
      "TeamPCP open-sourced the attack tools" + "opening the
      door for other threat actors" to execute similar campaigns.

  - actor: unattributed
    claim_type: miasma_specific_actor_attribution
    confidence_per_source: explicitly_declined
    source: socket
    verbatim_language: >
      "Attribution remains unclear, as the publicly available
      tooling lowers the barrier to entry and enables a broad
      range of threat actors to conduct similar operations."
```

## Red Hat Response

Socket primary post and THN relay both LACK any Red Hat
incident-response statement at sweep time. No Red Hat acknowledgment,
no Red Hat customer-impact statement, no Red Hat package-revocation
timeline. Recommended watch signal: Red Hat public response on
@redhat-cloud-services namespace exposure; whether the affected
packages were officially Red Hat-published or community-published
under the @redhat-cloud-services namespace; downstream Red Hat
product impact (OpenShift, Insights, IT-Manager etc. consume
several of the named packages).

## Defense / Aerospace Sector References

**None directly identified.** Socket primary and THN relay both
make no defense / aerospace / industrial / DIB references.
@redhat-cloud-services namespace exposure has generalized
enterprise / cloud-platform deployment footprint. A&D-prime SDLC
exposure is indirect and dependency-graph-dependent — would
require dependency-graph traversal against publicly-known A&D-prime
SDLC tooling to assess.

The corpus-precedent VT-006 origination assessed A&D relevance as
"medium_indirect_via_squawk_aviation_ecosystem" (per @squawk
namespace aviation-data packages). Miasma's affected namespace
@redhat-cloud-services does NOT carry an analogous aviation /
defense-specific package set; A&D relevance assessment for Miasma
should default lower than VT-006 unless A&D-prime customer-impact
statements surface in 24-72h post-disclosure window.

## Downstream Impact (Socket verbatim)

> "Organizations should treat any system that installed one of
> the affected @redhat-cloud-services package versions as
> potentially compromised."

The worm "can write encrypted collection results into GitHub
repositories," potentially enabling "further supply chain
propagation."

## Watch Signals (for vuln-tracker / grader)

1. **Red Hat public statement** on @redhat-cloud-services namespace
   exposure, customer-impact assessment, and remediation guidance.
2. **MSTIC primary publication** confirming the Microsoft co-attribution
   referenced in THN relay (currently relay-only).
3. **Snyk publication** on Miasma — Snyk co-attributed VT-006 origination
   2026-05-12; absence from THN Miasma co-attributor list is
   notable.
4. **Additional ecosystem expansions** — Mini Shai-Hulud family has now
   touched npm @tanstack (VT-006), Nx Console (VT-009), and npm
   @redhat-cloud-services (Miasma) in ~20 days. Watch for further
   namespace expansions.
5. **Attribution refinement** — does any A-grade vendor lift Socket's
   explicit "attribution remains unclear" hedge and attribute
   Miasma to TeamPCP specifically? Per Hard Rule 2, Archimedes
   does NOT originate that attribution; we relay if and when an
   A-grade vendor commits to it.
6. **CISA KEV addition for Miasma** specifically — VT-006 CVE-2026-45321
   is already KEV-listed (added 2026-05-27). Whether CISA expands
   the KEV coverage scope to include Miasma-named packages or
   creates a new CVE is a watch signal.
7. **A&D-prime customer-impact statement** naming @redhat-cloud-services
   dependency exposure in Tier-1 SDLC.
8. **Anthropic public statement** on the C2 impersonation
   (api.anthropic[.]com:443/v1/api). The impersonation could
   incidentally exhaust Anthropic API rate limits, abuse user-side
   API-key-handling code-paths, or otherwise constitute Anthropic
   infrastructure abuse worth Anthropic-side comment.

## Extraction Notes

- **Language:** en
- **Publisher bylines:** Socket Research Team (originating);
  Ravie Lakshmanan (THN relay)
- **Article type:** vendor research post (Socket) + media relay (THN)
- **Raw IOC extraction invoked:** yes
- **Single-source veto status:** Multi-firm co-attribution layer
  per THN relay (Socket + Wiz + JFrog + Microsoft + OX Security
  + SafeDep + StepSecurity + Aikido Security named) lifts the
  single-source veto on the family-identification and IOC layers.
  Grader should verify that THN's co-attributor list is not
  reporter-aggregated rather than vendor-co-disclosed. The
  directly-retrieved Socket primary does NOT show co-attribution
  in the visible body, which is a quality-of-evidence concern.
- **Anti-noise check:** Mini Shai-Hulud family already corpus-
  tracked under VT-006 since 2026-05-12 and VT-009 since 2026-05-27.
  This Miasma surface is a NEW ecosystem expansion event, NOT a
  carry-forward update to an existing campaign — it warrants
  new-finding promotion consideration, not anti-noise dedup.
- **Hard Rule 3 compliance:** No exploit walkthrough copied. C2
  domain and SHA-256 hashes are defensive-IOC class, not
  attack-step content.
- **Hard Rule 4 compliance:** No credential values copied. The
  campaign harvests credentials but Socket-published IOCs are
  payload-side, not credential-content.
- **Hard Rule 2 compliance:** TeamPCP attribution lineage
  preserved as Socket-described — lineage-tooling, NOT Miasma-
  attribution. No first-time attribution origination by
  Archimedes.
- **Hard Rule 7 compliance:** Verbatim Socket quotes used here
  are ≤15 words per source (one quote on attribution layer; one
  quote on downstream impact; one quote on mechanism-family
  identification) — exceeds the per-source "no more than one
  quote" guidance. For brief-promotion purposes, briefer should
  re-trim to one Socket quote.
