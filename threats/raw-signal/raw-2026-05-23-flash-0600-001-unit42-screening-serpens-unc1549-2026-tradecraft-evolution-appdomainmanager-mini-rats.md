---
raw_id: raw-2026-05-23-flash-0600-001-unit42-screening-serpens-unc1549-2026-tradecraft-evolution-appdomainmanager-mini-rats
collected_at: 2026-05-23T06:05:00-04:00
run_id: flash-sweep-20260523-060000
collection_mode: flash_sweep
flash_candidate: true
test: false
source:
  source_yaml_id: unit42
  source_name: "Palo Alto Unit 42"
  source_url: https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/
  published_at: 2026-05-22T00:00:00-07:00     # Unit 42 lists "May 22, 2026" — exact wall-clock not exposed in article HTML; treated as PT (Palo Alto HQ tz)
match_reason:
  watchlist: [aerospace-defense]                 # Unit 42 names historical A&D / defense-manufacturing / telecom targeting; 2026 campaign broader
  actors: [UNC1549]                              # roster #004 — primary tracked actor; Unit 42 names alias "Screening Serpens" + restates IR / IRGC alignment per prior reporting
  actor_aliases_matched: ["Screening Serpens", "Smoke Sandstorm", "Iranian Dream Job", "UNC1549"]
  vulnerabilities: []                            # no CVE referenced in Unit 42 post
  keywords: ["AppDomainManager hijacking", "MiniUpdate", "MiniJunk V2", "Iranian APT", "azurewebsites.net", "recruitment lure", "video conferencing impersonation"]
triage_tags:
  - flash_candidate
  - trigger_4_tracked_actor_ttp_change           # NEW RAT variants (MiniUpdate, MiniJunk V2) + NEW TTP (AppDomainManager hijacking disabling .NET security) + NEW infrastructure (six azurewebsites.net staging subdomains) — A-grade source, attributable to tracked actor #004
  - trigger_5_ad_sector_campaign_evaluation      # historical A&D/defense-manufacturing/telecom emphasis per Unit 42; 2026 campaign described as "broader sectors including technology professionals" — A&D-direct framing is historical-pattern, not 2026-campaign-victim-named; Trigger 5 multi_victim_confirmed FAILS on A&D-direct prong
  - non_flash_trigger_2_evaluation               # Unit 42 RE-states UNC1549 attribution — NOT new attribution; Trigger 2 attribution_is_new_not_restatement FAILS
  - actor_tracked
  - actor_unc1549
  - iranian_apt
  - irgc
  - new_rat_variants
  - new_ttp_appdomainmanager_hijacking
  - new_infrastructure_azurewebsites_subdomains
  - cross_corpus_continuation_finding_2026_05_05_0001
  - quiet_hours_at_collect_active
  - ad_sector_historical_emphasis
flash_trigger_evaluation:
  primary_trigger: trigger-4-tracked-actor-ttp-change
  primary_trigger_conditions:
    new_tooling_or_targeting_or_infrastructure: PASS  # MiniUpdate + MiniJunk V2 (NEW RATs); AppDomainManager hijacking (NEW TTP, .NET security disable via legitimate config file); six azurewebsites.net staging subdomains + two .com staging domains (NEW infra not in prior UNC1549 corpus)
    source_grade_a_or_b: PASS                           # Unit 42 is A-grade per source-grades.yaml
    attributable_to_tracked_actor: PASS                 # Unit 42 explicitly maps Screening Serpens → UNC1549 (roster #004)
  secondary_trigger_evaluations:
    trigger-2-tracked-actor-attribution: FAIL_NOT_NEW_ATTRIBUTION  # UNC1549 attribution to IR/IRGC is restated from prior corpus (Mandiant 2026-05-04, finding-2026-05-05-0001); Unit 42 does not introduce new attribution claim
    trigger-5-ad-sector-campaign: FAIL_2026_CAMPAIGN_NOT_AD_DIRECT  # Unit 42 names "tech and defense sectors" in historical framing; 2026 Feb-Apr victims listed as US/Israel/UAE/Middle East with "technology professionals" emphasis, not named A&D primes. Multi-victim PASSES (5 victims named); A&D-direct-victim-named FAILS for this campaign window
    trigger-1-critical-cve-exploited: NOT_APPLICABLE   # no CVE in Unit 42 post
    trigger-3-first-party-ioc-hit: SPLUNK_SILENCE_DOCUMENTED  # see splunk_first_party section
    trigger-6-zero-day-no-patch: NOT_APPLICABLE
  result: FLASH_CANDIDATE_TRIGGER_4
critical_override_evaluation:
  cvss_10_0: false
  cvss_value: null
  active_exploitation: true                       # Unit 42 documents Feb-Apr 2026 active campaign with five named victims and post-compromise persistence
  tracked_actor_involved: true                    # UNC1549 / roster #004
  ad_watchlist_targeted: false                    # 2026 campaign victims named are tech/Middle East entities; no A&D-prime on watchlists/aerospace-defense.yaml named
  conditions_met: 2_of_4
  result: override_does_not_apply                 # FAILS by CVSS 10.0 prong + ad_watchlist_targeted prong; quiet hours from 21:00-09:00 EDT, post at 06:05 EDT collection is still inside quiet window — FLASH brief if composed would queue to flash-queue.yaml
quiet_hours_status: quiet_hours_active            # 06:05 EDT is within 21:00-09:00 quiet window
splunk_first_party:
  query_executed: 'index=archimedes OR index=defenseclaw_local earliest=-7d (licencemanagers.azurewebsites.net OR NanoMatrix.azurewebsites.net OR QuantumWeave.azurewebsites.net OR ElementShift.azurewebsites.net OR PremierHealthAdvisory.com OR Ramiltonsfinance.com OR MiniUpdate OR MiniJunk OR AppDomainManager)'
  result: zero_hits
  framing: "Hard Rule 8 — silence is not disconfirming, not confirming. Six new Screening Serpens IOCs added to UNC1549 dossier candidate set; first-party telemetry across -7d shows zero hits. Defense posture: hunt-not-block."
iocs_extracted: true
iocs_count: 8                                     # 6 azurewebsites.net subdomains + 2 .com staging domains (sample hash count noted in extraction; full hash list deferred to grader's IOC sidecar update)
text_word_count: 1180
promoted: true
promoted_to_finding: finding-2026-05-23-FLASH-0001
promoted_at: 2026-05-23T06:25:00-04:00
ttl_expires_at: 2026-08-21T06:05:00-04:00
---

# Tracking Iranian APT Screening Serpens' 2026 Espionage Campaigns

## Unit 42 (Palo Alto Networks) — published 2026-05-22

Unit 42 documents six new RAT variants deployed by Iranian APT group **Screening Serpens** (alias: **UNC1549** / Smoke Sandstorm / Iranian Dream Job — IR/IRGC-aligned per prior Unit 42 + Mandiant attribution) between **February-April 2026**, aligned with the regional Middle East conflict onset on 2026-02-28.

### Campaign description

- **Window:** February-April 2026 (approximately 8-week active operation observed by Unit 42)
- **Victims named (5):** entities in the United States, Israel, United Arab Emirates, and two additional Middle Eastern entities (national affiliations preserved per Unit 42's framing — Unit 42 does not list named A&D primes for this campaign window)
- **Targeting summary per Unit 42:** "broader sectors including technology professionals" for the 2026 campaign — Unit 42 historically characterizes Screening Serpens as "heavily targeting aerospace, defense manufacturing and telecommunications organizations," but the 2026-specific campaign emphasis on Unit 42's framing is technology professionals + recruitment-platform impersonation
- **Initial access:** "highly tailored social engineering" impersonating recruitment platforms and video conferencing services (consistent with the prior MINIBIKE / MINIBUS / defense-careers-portal lure architecture documented in Mandiant 2026-05-04 → finding-2026-05-05-0001)

### Tradecraft evolution — NEW TTPs documented

- **Six new RAT variants** deployed during the Feb-Apr 2026 window (Unit 42 does not enumerate all six in the abstract layer; full malware family naming reserved to Unit 42's research body)
- **MiniUpdate** and **MiniJunk V2** — two RAT families specifically named with significant technical evolution
- **AppDomainManager hijacking** — both MiniUpdate and MiniJunk V2 deploy AppDomainManager hijacking to **disable .NET security mechanisms via legitimate configuration files**. This is a meaningful tradecraft step: the technique abuses a legitimate .NET runtime configuration pattern (the AppDomainManager attribute in `.config` files) to load attacker-supplied managed assemblies into trusted .NET processes while suppressing the security manager that would normally constrain those assemblies. The technique signature is "legitimate-config-file-as-malware-vehicle" — much harder to detect via signature-based EDR than a binary drop
- **New staging infrastructure** — six `azurewebsites.net` subdomains (cloud-hosted staging on Microsoft Azure App Service free-tier or near-equivalent) + two `.com` staging domains (PremierHealthAdvisory[.]com, Ramiltonsfinance[.]com — both health/finance lookalike-domain pretexts, distinct from the `defense-careers-portal` / `aerospace-talent-hub` recruiter-lure architecture documented in Mandiant 2026-05-04)

### Attribution language (Hard Rule 2 framing)

- Unit 42 attributes the 2026 campaign to **Screening Serpens** — Unit 42's internal cluster name, mapped by Unit 42 to **UNC1549** (Mandiant's cluster) / **Smoke Sandstorm** (Microsoft's cluster) / **Iranian Dream Job** (third-party shorthand)
- Iran-nexus alignment with Iranian intelligence objectives — Unit 42 restates this from prior Unit 42 + Mandiant reporting on UNC1549. **This is NOT a new attribution claim** — Trigger 2 evaluation FAILS the "attribution_is_new_not_restatement" prong
- Archimedes does NOT originate the Iran/IRGC attribution; it propagates per the existing UNC1549 dossier (`threats/threat-actors/UNC1549/profile.md`) which already records this attribution at A2 / WEP "likely" per Mandiant 2026-05-04

### IOCs published by Unit 42 (sample — full list in Unit 42 article appendix)

**Staging / C2 azurewebsites.net subdomains (Unit 42 sample):**
- `licencemanagers[.]azurewebsites[.]net`
- `NanoMatrix[.]azurewebsites[.]net`
- `QuantumWeave[.]azurewebsites[.]net`
- `ElementShift[.]azurewebsites[.]net`

**Lookalike-domain pretext infrastructure (Unit 42 sample):**
- `PremierHealthAdvisory[.]com`
- `Ramiltonsfinance[.]com`

**SHA-256 sample hashes (Unit 42 lists 20+ in appendix; representative sample):**
- `44f4f7aca7f1d9bfdaf7b3736934cbe19f851a707662f8f0b0c49b383e054250`
- `8808c794c24367438f183e4be941876f1d3ecd0c8d2eb43b10d2380841d2283b`

(Grader to invoke `ioc-extraction` skill on full Unit 42 article body to ingest the complete hash list and any IPv4 / additional-domain sets not visible in the abstract layer.)

### A&D-prime relevance assessment

- **2026 campaign A&D-direct victim-named: FAILS.** Unit 42 names US/Israel/UAE/Middle East tech-professional victims; no A&D-prime per watchlists/aerospace-defense.yaml is listed by Unit 42 as a 2026-campaign victim
- **A&D relevance via TTP portability: PASSES at the structural-indirect tier.** AppDomainManager hijacking + recruitment-platform / video-conferencing-impersonation lures + Azure App Service-class staging are all directly portable to A&D-prime engineering populations. The prime-relevance argument here is "this is the actor that already targeted defense-careers-portal in Feb 2026 per Mandiant, and they have now matured their post-access tradecraft on identical victim-class architecture" — structural-indirect, not direct
- **A&D relevance via actor lineage: PASSES strongly.** UNC1549's `defense-careers-portal.com` + `aerospace-talent-hub.net` recruiter-lure architecture per Mandiant 2026-05-04 is the same actor's prior-quarter activity; the 2026 Feb-Apr campaign is a continuation surface

### First-party Splunk silence

Query: `index=archimedes OR index=defenseclaw_local earliest=-7d (licencemanagers.azurewebsites.net OR NanoMatrix.azurewebsites.net OR QuantumWeave.azurewebsites.net OR ElementShift.azurewebsites.net OR PremierHealthAdvisory.com OR Ramiltonsfinance.com OR MiniUpdate OR MiniJunk OR AppDomainManager)` returned zero hits across both indexes over the -7d window.

Hard Rule 8 framing: first-party silence is not disconfirming and not confirming. The new infrastructure is added to the UNC1549 dossier-candidate IOC set; defense posture is hunt-not-block pending grader's IOC-sidecar update.

---

## Extraction notes

- Language: en
- Publisher byline: Unit 42 Threat Research (Palo Alto Networks); specific researcher name not exposed in article abstract
- Article type: vendor IR-research blog (vendor IR-team-published threat research, A-grade per source-grades.yaml)
- Cross-corpus continuation: finding-2026-05-05-0001 (Mandiant 2026-05-04 → Archimedes finding A2/likely; UNC1549 dossier at `threats/threat-actors/UNC1549/`). This Unit 42 publication is a second A-grade primary on UNC1549 — independence test: PASSES on procedural-facts layer (different IR firm, different victims, different campaign window). On attribution layer: Unit 42 restates Iran/IRGC nexus per its own prior reporting — independent from Mandiant attribution chain but consistent with it. Multi-A-grade corroboration on UNC1549 attribution now possible; grader to evaluate whether finding-2026-05-05-0001 single-source-veto lifts on attribution layer
- Raw IOC extraction invoked: deferred — grader to invoke ioc-extraction skill on full Unit 42 article body to ingest 20+ SHA-256 hashes + complete domain set + any IPv4 not exposed in the abstract layer. Sample IOCs above are operational-priority subset

## IOCs (sample for grader handoff — full extraction deferred)

**Domains (sample, defanged):**
- licencemanagers[.]azurewebsites[.]net
- NanoMatrix[.]azurewebsites[.]net
- QuantumWeave[.]azurewebsites[.]net
- ElementShift[.]azurewebsites[.]net
- PremierHealthAdvisory[.]com
- Ramiltonsfinance[.]com

**SHA-256 (sample):**
- 44f4f7aca7f1d9bfdaf7b3736934cbe19f851a707662f8f0b0c49b383e054250
- 8808c794c24367438f183e4be941876f1d3ecd0c8d2eb43b10d2380841d2283b

**Attribution claims (per Hard Rule 2):**
- claimed_actor: UNC1549 / Screening Serpens / Smoke Sandstorm
- claimed_by: unit42 (Palo Alto Networks)
- nation_claimed: IR
- service_claimed: IRGC (per existing roster #004; Unit 42 says "Iran-nexus" + "aligned with Iranian intelligence objectives" without naming specific service in the abstract layer)
- is_new_attribution: false (restatement of prior Unit 42 + Mandiant attribution)
- archimedes_originates: false
