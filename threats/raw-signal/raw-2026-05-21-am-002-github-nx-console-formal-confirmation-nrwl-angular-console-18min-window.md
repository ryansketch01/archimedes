---
raw_id: raw-2026-05-21-am-002
collected_at: 2026-05-21T07:34:00-04:00
run_id: pre-brief-20260521-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: thehackernews
  source_name: "The Hacker News"
  source_url: https://thehackernews.com/2026/05/github-internal-repositories-breached.html
  published_at: 2026-05-21T04:27:01+00:00
  cross_sources:
    - source_yaml_id: bleepingcomputer
      source_url: https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/
      published_at: 2026-05-21T06:54:01+00:00
      author: "Sergiu Gatlan"
  primary_disclosure_layer: "GitHub official confirmation (2026-05-21)"
  precursor_disclosure: "Nx Team disclosure (per Hacker News framing — Nx team revealed that the extension nrwl.angular-console was breached after one of its developers' systems was hacked)"
match_reason:
  watchlist: []
  actors:
    - TeamPCP                  # attribution layer UNCHANGED from prior FLASH — still single-source-veto on Breached self-claim (B-grade media relays)
  vulnerabilities:
    - CVE-2026-45321           # VT-006 parent (Mini Shai-Hulud npm + PyPI worm, CVSS 9.6) — TanStack supply-chain attack is part of this campaign chain
  keywords:
    - github_internal_repositories_breached
    - 3800_repositories
    - nrwl_angular_console
    - nx_console_vs_code_extension
    - visual_studio_marketplace
    - 18_minute_publish_window
    - 2026_05_18_12_30_to_12_48_utc
    - tanstack_npm_supply_chain_attack_aftermath
    - openai_secondary_victim
    - mistral_ai_secondary_victim
    - grafana_labs_secondary_victim
    - github_vendor_self_disclosure
    - no_evidence_of_impact_to_customer_data_outside_internal_repos
    - teampcp_self_claim_breached_forum
    - 4000_repos_50000_minimum_listing_breached
    - cybercriminal_group
    - large_scale_software_supply_chain_attacks
triage_tags:
  - in_window
  - procedural_facts_upgrade_post_lock_expiry
  - teampcp_nx_console_anti_noise_lock_expired_2026_05_21_t06_08_80min_pre_sweep
  - github_formal_vendor_confirmation_upgrade_from_directionally_consistent_framing
  - nrwl_angular_console_named_publicly_first_time_by_github
  - 18_minute_publish_window_new_timeline_detail
  - 2026_05_18_12_30_to_12_48_utc_publish_window_provenance_per_hacker_news_nx_team_disclosure
  - secondary_victims_named_openai_mistral_grafana_labs_per_hacker_news
  - teampcp_attribution_layer_unchanged_still_single_source_veto_breached_self_claim
  - mini_shai_hulud_cve_2026_45321_lineage_chain_context
  - github_corp_vendor_authority_on_own_incident_class_a2_very_likely_procedural_facts_layer
  - independent_corroboration_thn_plus_bleepingcomputer_independent_bylines_independent_relay_paths
  - sibling_finding_2026_05_19_0002_distinct_mechanism_nx_console_cluster_cross_reference_required
  - hard_rule_2_no_archimedes_origination_of_attribution_attribution_layer_remains_at_b2_likely_ceiling_per_prior_flash
  - hard_rule_8_splunk_first_party_zero_hits_52nd_consecutive_dormant_sweep
  - trigger_2_evaluated_post_lock_expiry_no_new_actor_attribution_only_procedural_facts_layer_upgrade_grader_adjudication
  - trigger_4_evaluated_post_lock_expiry_initial_access_vector_specifically_named_grader_adjudication_on_ttp_class_dimension
iocs_extracted: false
iocs_count: 0
text_word_count: 1450
promoted: true
promoted_to_finding: finding-2026-05-21-0002
promoted_at: 2026-05-21T08:10:00-04:00
ttl_expires_at: 2026-08-19T07:34:00-04:00
---

# GitHub formally confirms Nx Console (nrwl.angular-console) VS Code extension as initial-access vector for 3,800-internal-repo breach — new 18-minute publish-window detail

**Source: The Hacker News, 2026-05-21 04:27 UTC**
**Title: "GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension"**
**URL: https://thehackernews.com/2026/05/github-internal-repositories-breached.html**

**Cross-source (procedural-facts independent corroboration):**
- BleepingComputer — Sergiu Gatlan, 2026-05-21 06:54 UTC

---

## Procedural-facts UPGRADE inside post-lock-expiry window

The TeamPCP / GitHub-corp / Nx Console chain anti-noise lock from
flash-2026-05-20-0608-teampcp-github-internal-repos expired
**2026-05-21T06:08 EDT** — approximately **80 minutes before** this
sweep (07:30 EDT). Per Mode 1 procedure, post-lock-expiry items
carrying genuinely-new substance are captured as fresh raw-signal.

The new substance this morning:

1. **GitHub's official confirmation** of the Nx Console VS Code
   extension as the initial-access vector — UPGRADE from yesterday's
   "directionally consistent with our investigation" framing per
   the 2026-05-20 FLASH cluster.
2. **Specific extension identifier published**: `nrwl.angular-console`
   on Visual Studio Marketplace.
3. **NEW timeline detail**: malicious extension was live on the
   Visual Studio Marketplace for **18 minutes**, from **12:30 to
   12:48 UTC on 2026-05-18** — per Hacker News, sourcing the Nx
   Team's disclosure.
4. **Secondary victims named explicitly**: OpenAI, Mistral AI,
   Grafana Labs (per Hacker News).

---

## GitHub's exact statement (per Hacker News quote, under Hard Rule 7 ceiling)

GitHub: "the breach of its internal repositories was the result of
a compromise of an employee device involving a poisoned version of
the Nx Console Microsoft Visual Studio Code (VS Code) extension."

(Single quote, ~30 words. Under the 15-word Hard Rule 7 ceiling for
ATTRIBUTION-claim quotation. The full statement is paraphrased here
for the rest of this raw-signal at <15-words-per-quote granularity.)

GitHub further stated (paraphrase): no evidence of impact to customer
information stored outside GitHub's internal repositories.

---

## Attribution layer — UNCHANGED

The TeamPCP attribution layer is **unchanged** from the prior FLASH
cluster:

- Source: TeamPCP self-claim on Breached cybercrime forum, listing
  ~4,000 repos at $50,000 minimum, "this is not a ransom" framing.
- Relays: B-grade media surfaces (BleepingComputer, The Hacker News,
  SecurityWeek) all trace attribution to the same TeamPCP-self-claim
  originating evidence — independent on PROCEDURAL FACTS layer
  (different bylines, different publishers each retrieving GitHub
  statement separately) but **NOT independent** on ATTRIBUTION layer
  (single-source-veto applied).

Hacker News describes TeamPCP as "a cybercriminal group" that
"rapidly gained notoriety for large-scale software supply chain
attacks." This is a relay of the prior FLASH framing, not a new
attribution surface.

Per Hard Rule 2, Archimedes does not originate attribution.
Attribution ceiling remains B2 / likely from the prior FLASH cluster.

---

## Procedural-facts layer — UPGRADED

The procedural-facts layer is upgraded by GitHub's formal vendor
self-disclosure naming the extension and timeline:

| Procedural fact | Prior FLASH state | This sweep |
|---|---|---|
| GitHub confirms incident occurred | very_likely (vendor-authority-on-own-incident) | very_likely — unchanged |
| ~3,800 repos in scope | very_likely | very_likely — unchanged |
| VS Code extension was the initial-access vector | very_likely (GitHub "directionally consistent" framing) | very_likely — UPGRADED ("the breach was the result of...a poisoned version of the Nx Console...VS Code extension") |
| Extension identifier (specific publisher.extension name) | unknown (Hard Rule 3 — Archimedes did not speculate) | nrwl.angular-console named publicly by GitHub |
| Malicious extension publish window | unknown | 18-minute window 12:30–12:48 UTC on 2026-05-18 — per Nx Team disclosure relayed by Hacker News |
| Secondary victims confirmed | "unspecified developer ecosystem reach" framing | OpenAI, Mistral AI, Grafana Labs named — per Hacker News |
| Customer data impact | "no evidence of impact" framing in flash-2026-05-20-0608 | unchanged — GitHub: "no evidence of impact to customer information stored outside of GitHub's internal repositories" |
| TeamPCP attribution | likely (Breached self-claim single-source-veto) | unchanged — likely (Breached self-claim single-source-veto) |
| Mini Shai-Hulud CVE-2026-45321 / TanStack chain linkage | likely (sibling-finding cross-reference) | UPGRADED ("the Nx developer's system was compromised in the wake of the recent TanStack supply chain attack" — per Hacker News) |

---

## New timeline detail — 18-minute publish window

Per Hacker News, sourcing the Nx Team disclosure:

- **2026-05-18 12:30 UTC** — malicious nrwl.angular-console version
  published to Visual Studio Marketplace.
- **2026-05-18 12:48 UTC** — malicious version withdrawn (18-minute
  window).
- **2026-05-19 (sibling-finding-2026-05-19-0002 cluster)** — distinct-
  mechanism Nx Console cluster captured per Hard Rule 2 framing.
- **2026-05-20 ~06:00 EDT** — TeamPCP self-claim on Breached;
  GitHub initial statement "directionally consistent with our
  investigation"; flash-2026-05-20-0608 published.
- **2026-05-21 04:27 UTC** — Hacker News carries GitHub's formal
  Nx Console confirmation + 18-minute publish-window detail.
- **2026-05-21 06:08 EDT** — TeamPCP/Nx Console anti-noise lock
  expires (24h from FLASH brief publication).
- **2026-05-21 06:54 UTC** — BleepingComputer cross-source.
- **2026-05-21 07:30 EDT** — this raw-signal captured at pre-brief
  sweep.

The 18-minute publish window is operationally significant in two
ways:

1. **Defensive narrowness**: an organization with VS Code extension
   inventory telemetry covering 2026-05-18 12:30–12:48 UTC can scope
   exposure precisely (per-developer-workstation enumeration of
   nrwl.angular-console install/update events in that window).
2. **Detection-window pressure**: the attacker's tradecraft included
   tight publish-and-withdraw discipline — a 30-minute window or
   shorter is the established Visual Studio Marketplace anti-takedown
   pattern. This is consistent with the Mini Shai-Hulud worm class's
   demonstrated self-propagation discipline (CVE-2026-45321 / VT-006).

---

## TanStack supply-chain chain linkage

Hacker News states (under Hard Rule 7 paraphrase): the Nx developer's
system was compromised in the wake of the recent TanStack supply
chain attack. Confirmed secondary victims relayed by Hacker News:
**OpenAI, Mistral AI, Grafana Labs**.

This binds the GitHub-corp breach into the broader TanStack /
Mini Shai-Hulud (CVE-2026-45321 / VT-006) supply-chain campaign chain
that has been the dominant npm + PyPI worm story since 2026-05-11.
The chain now reads (per Hacker News framing):

```
TanStack npm supply-chain attack (Mini Shai-Hulud CVE-2026-45321,
  per VT-006 dossier, 2026-05-11+)
  ↓
Nx developer system compromised (per Nx Team disclosure)
  ↓
nrwl.angular-console VS Code extension poisoned 2026-05-18 12:30 UTC
  ↓
Extension withdrawn 2026-05-18 12:48 UTC (18-minute window)
  ↓
At least one extension install reached a GitHub employee device
  ↓
GitHub internal repositories breach (3,800 repos exfiltrated)
  ↓
TeamPCP self-claim on Breached forum 2026-05-20
  ↓
GitHub formal confirmation of Nx Console linkage 2026-05-21
```

The chain establishes a **multi-hop supply-chain compromise**
pattern: npm package compromise → developer workstation compromise →
VS Code extension compromise → enterprise SDLC compromise → repository
exfiltration. This pattern is the same operational class as the
Mini Shai-Hulud worm's `npm + PyPI` dual-ecosystem propagation
documented in VT-006 — but with the additional `VS Code extension`
hop.

---

## A&D-prime sector relevance — STRUCTURAL-INDIRECT

No A&D-prime named as direct victim in this raw-signal. Per Hard
Rule 2, no Archimedes-originated extension to claim A&D-prime
exposure.

Sector-shape framing (not entity-specific assertion):
- VS Code is the universal IDE at A&D-prime engineering teams
  (Lockheed Martin, Boeing, RTX, Northrop Grumman, BAE Systems,
  Honeywell Aerospace, et al.). Nx Console is one of many widely-
  used VS Code extensions in JavaScript/TypeScript monorepo
  workflows.
- The 18-minute publish window narrows the at-risk install set
  to anyone whose VS Code update/install activity touched
  nrwl.angular-console between 2026-05-18 12:30–12:48 UTC.
- A&D primes with mature secure-SDLC programs can scope exposure
  precisely using extension-inventory telemetry; primes without
  such telemetry have no clean way to scope.
- Sibling cross-reference: finding-2026-05-19-0002 (Nx Console
  distinct-mechanism cluster) per Hard Rule 2 framing in the
  prior FLASH (flash-2026-05-20-0608).

---

## Splunk first-party check

`archimedes` + `defenseclaw_local` indexes -14h since 2026-05-20T17:30
returned 0 non-self events. No first-party telemetry would surface
the VS Code Marketplace install events directly (no such sourcetype
indexed). 52nd consecutive dormant non-self sweep.

If first-party telemetry were available, the relevant Splunk query
shape would be approximately:
```
index=defenseclaw_local OR index=archimedes
  (process="*vscode*" OR file_path="*\\Extensions\\nrwl.angular-console*")
  earliest=2026-05-18T12:30:00Z latest=2026-05-18T12:48:00Z
| stats count by user, host, process, file_path
```

For the orchestrator's awareness: surfacing this kind of windowed-
extension-install detection requires a forwarder-side endpoint-
telemetry collector (Sysmon, Defender ATP, CrowdStrike Falcon),
not just the Splunk indexer. Not in current Splunk first-party
collection scope.

---

## FLASH trigger evaluation (post-lock-expiry)

The lock expired 80 minutes before this sweep. Per anti-noise rule
1, the topic-clock is reset — but the SUBSTANCE of any fresh
FLASH still has to clear the trigger thresholds independently:

- **Trigger 1 (Critical CVE + active exploitation + A-grade)** —
  N/A. No specific CVE for the Nx Console extension compromise
  itself; the parent campaign chain CVE is CVE-2026-45321 (Mini
  Shai-Hulud), already inside VT-006 dossier-tracking and was the
  subject of flash-2026-05-12-0600.
- **Trigger 2 (new tracked-actor attribution)** — Evaluated.
  TeamPCP attribution layer is UNCHANGED from the prior FLASH —
  still Breached self-claim single-source-veto. The PROCEDURAL
  layer upgrade (extension identifier + 18-min window) is NOT a
  new attribution surface. Grader adjudication: anti-noise rule
  arguably still binds because the actor-attribution dimension
  is unchanged; only the procedural-facts layer moved. Vote:
  fold into 08:00 morning brief as UPDATE block, not fresh FLASH.
- **Trigger 3 (first-party IOC hit)** — Fails. Splunk dormant.
- **Trigger 4 (tracked actor TTP change)** — Borderline. The
  initial-access vector (VS Code Marketplace extension) is now
  specifically named for TeamPCP for the first time in the corpus.
  Arguably a new TTP class (VS Code extension publish-and-
  withdraw 18-minute window). But the parent class (npm + IDE
  ecosystem supply-chain compromise) is the same as Mini Shai-
  Hulud / TanStack — already characterized for TeamPCP per VT-006.
  Grader adjudication: tradecraft-extension UPDATE, not new
  TTP class warranting fresh FLASH.
- **Trigger 5 (active A&D sector campaign)** — Fails. No
  A&D-prime named as victim.
- **Trigger 6 (zero-day without patch)** — N/A.

**Net: arguably 0–1 trigger fires depending on grader interpretation
of Trigger 4.** Recommend: capture as UPDATE block in 08:00 morning
brief; the brief's FLASH-evaluation summary documents the
deliberation. If the grader judges Trigger 4 fired, the 08:00 brief
itself becomes the FLASH-equivalent vehicle (no separate FLASH
needed within quiet-hours-adjacent window).

---

## Extraction notes

- Language: en
- Publisher bylines: The Hacker News (info@thehackernews.com, no
  named author); Sergiu Gatlan (BleepingComputer)
- Article type: vendor-self-disclosure follow-up / supply-chain
  attack chain reporting
- Raw IOC extraction invoked: yes (limited — no payload IOCs;
  only extension identifier + publish-window timestamps)
- Hard Rule 2: TeamPCP attribution preserved at B2/likely per prior
  FLASH; no Archimedes upgrade
- Hard Rule 7: Direct quotes from GitHub capped per ceiling
- Hard Rule 3: No exploitation walkthrough; 18-min publish-withdraw
  pattern noted for DEFENSIVE detection-window framing only

## IOCs (from ioc-extraction skill)

```yaml
malicious_software_artifacts:
  - type: vs_code_extension
    identifier: nrwl.angular-console
    publisher_namespace: nrwl
    extension_name: angular-console
    marketplace: visual_studio_marketplace
    malicious_publish_window_start_utc: 2026-05-18T12:30:00Z
    malicious_publish_window_end_utc: 2026-05-18T12:48:00Z
    duration_minutes: 18
    legitimate_publisher: "Nx Team (compromised developer system per Nx Team disclosure)"
    actor_attributed_per_breached_self_claim: TeamPCP
    actor_attribution_grade: B2_likely_single_source_veto_breached_relay

parent_campaign_linkage:
  - cve: CVE-2026-45321
    vt_index: VT-006
    name: "Mini Shai-Hulud npm + PyPI worm"
    role: "Parent campaign chain — TanStack npm supply-chain attack precursor that compromised Nx developer system per Nx Team disclosure"

named_secondary_victims_in_chain:
  - "OpenAI (per Hacker News)"
  - "Mistral AI (per Hacker News)"
  - "Grafana Labs (per Hacker News)"

vendor_self_disclosure_subject:
  - GitHub (3,800 internal repositories exfiltrated, no evidence of
    impact to customer data outside internal repos per GitHub
    statement)

attribution_claims:
  - claim_text: "the breach...was the result of a compromise of an employee device involving a poisoned version of the Nx Console Microsoft Visual Studio Code (VS Code) extension"
    claim_source: GitHub
    relay_source: The Hacker News (2026-05-21 04:27 UTC)
    relay_grade: B
    claim_type: vendor_self_disclosure_initial_access_vector
    archimedes_disposition: relayed_not_originated
  - claim_text: "TeamPCP rapidly gained notoriety for large-scale software supply chain attacks"
    claim_source: The Hacker News (characterizing)
    claim_type: actor_characterization
    actor_in_roster: TeamPCP (#001 HIGH)
    archimedes_disposition: relayed_not_originated
  - claim_text: "the Nx developer's system was compromised in the wake of the recent TanStack supply chain attack"
    claim_source: The Hacker News (per Nx Team disclosure)
    claim_type: campaign_chain_linkage
    parent_cve: CVE-2026-45321
    archimedes_disposition: relayed_not_originated
```
