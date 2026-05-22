---
raw_id: raw-2026-05-22-am-001-securityweek-grafana-tanstack-confirmed-victim
collected_at: 2026-05-22T07:38:00-04:00
run_id: pre-brief-20260522-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek (Ionut Arghire byline)"
  source_url: https://www.securityweek.com/grafana-says-codebase-and-other-data-stolen-via-tanstack-supply-chain-attack/
  published_at: 2026-05-22T07:49:38+00:00
  primary_substance_source: "Grafana incident-disclosure (vendor self-disclosure on own incident); SecurityWeek is media relay layer per Hard Rule 2"
match_reason:
  watchlist: []
  actors:
    - TeamPCP                    # Inherited from VT-006 / Wiz + StepSecurity prior attribution; Grafana names no actor (Hard Rule 2)
  vulnerabilities:
    - CVE-2026-45321             # VT-006 / Mini Shai-Hulud (per _index.yaml)
  keywords:
    - mini_shai_hulud
    - tanstack_supply_chain
    - grafana_named_victim
    - github_workflow_token_unrevoked
    - codebase_exfil_public_and_private_repos
    - ransom_demand_rejected
    - may_11_detection
    - may_16_ransom_demand
    - may_22_public_disclosure
    - law_enforcement_notification
    - cloud_platform_unaffected
    - no_customer_production_systems_affected
    - business_contact_pii_exfil
triage_tags:
  - vendor_self_disclosure_relay_via_securityweek
  - named_enterprise_victim_third_in_tanstack_chain
  - procedural_facts_upgrade_on_vt_006_corpus_lock
  - teampcp_attribution_unchanged_via_hard_rule_2
  - inside_active_anti_noise_lock_finding_2026_05_21_0007
  - lock_expires_concurrent_with_2026_05_22_morning_brief_at_t08
  - first_ransom_pivot_data_point_at_secondary_victim_layer_on_vt_006_chain
  - openai_disclosed_2026_05_14_grafana_disclosed_2026_05_22_mistralai_pending_at_sweep
  - operationally_applicable_to_a_and_d_sdlc_running_github_actions_workflow_tokens
iocs_extracted: true
iocs_count: 0   # No new IOCs in the Grafana disclosure beyond the carry-forward VT-006 set already in _master-index.yaml
text_word_count: 320
promoted: true
promoted_to_finding: finding-2026-05-22-0001
promoted_at: 2026-05-22T08:14:00-04:00
ttl_expires_at: 2026-08-20T07:38:00-04:00
---

# Grafana confirms codebase and operational data stolen via TanStack supply-chain chain — May-11 detection, unrevoked GitHub workflow token enabled continued access, May-16 ransom demand rejected, May-22 public disclosure

## Source

SecurityWeek (Ionut Arghire byline), published 2026-05-22T07:49:38+00:00
(03:49 EDT). Primary substance is Grafana's own incident-disclosure post;
SecurityWeek is the media-relay layer per Hard Rule 2. Article URL:
https://www.securityweek.com/grafana-says-codebase-and-other-data-stolen-via-tanstack-supply-chain-attack/

## What Grafana confirmed

Grafana confirmed that unauthorized access to its GitHub repositories
resulted from the TanStack supply-chain attack. The company detected
malicious activity on **2026-05-11** and immediately rotated GitHub
workflow tokens, though **one token was not revoked**, enabling continued
threat-actor access. Grafana's own statement (preserved verbatim per
Hard Rule 7 quote discipline, ≤15 words): "A subsequent review confirmed
that a specific GitHub workflow we originally deemed not impacted had,
in fact, been compromised."

## What was stolen

- **Grafana's codebase** — both public and private source code in
  internal GitHub repositories
- **Business contact names and email addresses** from professional
  relationships
- **Internal operational information and business details**

Grafana emphasized that:
- **NO customer production systems were affected**
- **NO codebase was modified**
- **Grafana Cloud platform operations remained uncompromised**

## Timeline

| Date | Event |
|------|-------|
| 2026-05-11 | Malicious activity detected; initial GitHub workflow token rotation performed |
| 2026-05-11+ | Subsequent review identifies one workflow originally deemed not impacted as in fact compromised; unrevoked token enables continued attacker access |
| 2026-05-16 | Ransom demand received; Grafana rejects |
| 2026-05-22 | Public disclosure published; law enforcement notified |

## Attribution language

Grafana names no threat actor. SecurityWeek does not originate attribution
beyond carry-forward of the established VT-006 / Mini Shai-Hulud campaign
chain. Per Hard Rule 2, Archimedes does not upgrade attribution. The
TeamPCP attribution that exists in the corpus is inherited from
finding-2026-05-12-FLASH-0001 (Wiz + StepSecurity originating; Snyk relays
StepSecurity per source-grades.yaml). MSTIC (2026-05-20) and Unit 42
(2026-05-20) both used unattributed-actor framing per their own Hard-Rule-
2-equivalent discipline in finding-2026-05-21-0007.

## Why this is a procedural-facts upgrade (not a fresh-FLASH)

This disclosure sits INSIDE the TeamPCP / TanStack / Nx Console campaign-
chain anti-noise lock established by 2026-05-21 morning brief finding-
2026-05-21-0007. The lock expires concurrent with the 2026-05-22 morning
brief at 08:00 EDT. The disclosure is captured as procedural-facts upgrade
inside the lock, surfacing three operationally-significant new data points:

1. **May-11 detection date for a named-secondary-victim.** Yesterday's Nx
   Team named OpenAI, Mistral AI, and Grafana as TanStack-chain secondary
   victims but published no per-victim detection timestamps. Grafana now
   provides one: detection on the same day as a public-OpenAI 2026-05-14
   disclosure week (note: OpenAI's own disclosure was 2026-05-14 per
   finding-2026-05-14-0008; Grafana lags 11 days on public-disclosure
   relative to OpenAI even though detection was earlier).

2. **Unrevoked-workflow-token causal claim.** This is the operationally
   load-bearing detail: incomplete token rotation enabled continued
   attacker access despite initial response. Operationally directly
   applicable to every Tier-1 A&D SDLC running GitHub Actions with
   workflow tokens — the "rotate everything, even what you think
   wasn't impacted" lesson is now vendor-confirmed by a named secondary
   victim. Defensive prescription update for A&D-prime SOC / DevSecOps
   teams: when responding to TanStack-chain exposure, enumerate every
   workflow that has ever touched the affected dependency chain and
   rotate all of them, not just those assessed as exposed at first
   triage.

3. **May-16 ransom-demand + May-22 public-disclosure timeline.** This is
   the first confirmed-monetization-attempt data point on the VT-006
   campaign chain at the secondary-victim layer. Prior framing of the
   Mini Shai-Hulud campaign was "supply-chain credential theft + worm
   propagation + CI/CD-credential targeting" (per MSTIC + Unit 42
   2026-05-20 publications). The ransom-pivot is new at this layer.
   Grafana rejected; what the actor does next on un-rejecting victims
   is open intelligence question.

## Operational template for A&D primes

The Grafana operational shape is now the first-clear vendor-confirmed
template for what a TanStack-chain victim disclosure looks like at a
named-enterprise tier:

- 2 employee devices or workflow-token compromise (OpenAI's prior
  disclosure framed device-compromise; Grafana frames workflow-token
  compromise) → token / cert exfil → code-repository access expansion
  → ransom pivot.
- A&D-prime SDLC exposure to @tanstack / @squawk / @uipath / @mistralai /
  @opensearch-project / DraftLab / PyPI guardrails-ai@0.10.1 / PyPI
  mistralai@2.4.6 dependency-graph reach is the trigger condition.
- The operational ask: inventory developer-workstation extensions, audit
  CI/CD pipelines for tokens issued during the 2026-05-04 → 2026-05-12
  worm-active window, rotate even those assessed as not-impacted, monitor
  GitHub commit/push activity from anomalous IP / device-registration
  for 30+ days post-rotation.

## Hard Rule 2 status

- Grafana names no actor.
- SecurityWeek does not originate attribution.
- Archimedes does NOT upgrade attribution.
- The TeamPCP attribution carried in the VT-006 corpus entry is per
  Wiz + StepSecurity 2026-05-12 originating attribution + the MSTIC +
  Unit 42 2026-05-20 unattributed-framing-preserved findings.

## Hard Rule 4 status

No credentials surfaced in the Grafana disclosure or SecurityWeek relay.
Grafana describes "business contact names and email addresses" as
exfiltrated PII — these are GDPR-scoped data categories not
credentials. Archimedes records the exfiltration event class, not the
data values.

## Trigger evaluation context (for grader, not collector)

- **Trigger 1 (critical-CVE-exploited):** N/A — Grafana disclosure
  is post-disclosure named-victim self-attestation, not new CVE.
  CVE-2026-45321 VT-006 already inside corpus lock.
- **Trigger 2 (tracked-actor-attribution):** N/A — Grafana names no
  actor; no new attribution surfaces.
- **Trigger 3 (first-party-IOC-hit):** N/A — Splunk first-party 0
  events this sweep (54th consecutive dormant sweep).
- **Trigger 4 (tracked-actor-TTP-change):** N/A — no new TTP class
  surfaced (consistent with prior MSTIC + Unit 42 2026-05-20 publication
  TTPs).
- **Trigger 5 (A&D-sector campaign):** Grafana is NOT an A&D-prime;
  Grafana is a SDLC observability / monitoring platform vendor. No
  named A&D-prime victim surfaces in this disclosure.
- **Trigger 6 (zero-day-no-patch):** N/A.

All six triggers fail. The disclosure is best characterized as
PROCEDURAL-FACTS UPGRADE inside the existing campaign-chain anti-
noise lock — UPDATE block material for the morning brief, not fresh
FLASH-tier.

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire (SecurityWeek)
- Article type: blog / news-relay
- Raw IOC extraction invoked: yes (per Mode 1 — but yielded zero new IOCs
  beyond carry-forward VT-006 set; details below)
- Source grade per source-grades.yaml: securityweek provisional-B; effective
  primary substance is Grafana vendor self-disclosure on own incident
  (procedurally A-grade per same precedent as OpenAI / Cisco PSIRT /
  GitHub blog self-disclosure)

## IOCs (from ioc-extraction skill)

No new IOCs surface in this Grafana disclosure beyond carry-forward.
The article does not publish:
- New malicious package versions beyond VT-006 corpus set
- New C2 domains or IPs beyond VT-006 set already in _master-index.yaml
- New file hashes
- New attacker accounts or identities

Carry-forward VT-006 IOC set remains as documented in finding-2026-05-12-
FLASH-0001 (17 IOCs: 1 CVE + 1 GHSA + 6 C2 domains + 1 C2 IP + 2 staging
URLs + 3 SHA-256 hashes + 1 Session ID + 1 PBKDF2 salt + 1 GitHub author
identity).

The only addition this disclosure makes to corpus state is the **Grafana**
named-victim self-attestation tag on the VT-006 secondary-victims list,
joining the already-attested OpenAI (finding-2026-05-14-0008) and the
Nx-Team-named-but-not-yet-self-attested Mistral AI.

```yaml
attribution_claims:
  - source: Grafana (vendor self-disclosure)
    claim: "Unauthorized access to GitHub repositories resulted from the TanStack supply-chain attack"
    attribution_language: "confirmed" / direct first-party attestation on own incident
    confidence: vendor authority on own incident (procedurally A-grade)
    actor_named: null              # Grafana names no actor (Hard Rule 2 preserved)
  - source: SecurityWeek (media relay)
    claim: "carry-forward of established VT-006 / Mini Shai-Hulud / TeamPCP framing from prior reporting"
    attribution_language: pass-through (no origination)
    confidence: relay-layer B-grade
    actor_named: null              # SecurityWeek does not originate
no_new_iocs_observed: true
carry_forward_set_referenced:
  - VT-006 / Mini Shai-Hulud per finding-2026-05-12-FLASH-0001
  - 17-IOC set per threats/vulnerabilities/_index.yaml entry VT-006
secondary_victims_layer_state_update:
  named_by_nx_team_2026_05_21:
    - OpenAI                # self-disclosed 2026-05-14 per finding-2026-05-14-0008
    - Mistral AI            # not yet self-disclosed at this sweep time
    - Grafana               # SELF-DISCLOSED 2026-05-22 per this raw-signal
  pending_first_party_self_disclosure:
    - Mistral AI
```
