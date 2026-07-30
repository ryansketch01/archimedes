---
finding_id: finding-2026-07-30-0005
created_at: 2026-07-30T16:12:00-04:00
graded_by: grader
grading_run_id: afternoon-20260730-160000
grading_mode: scheduled_brief
finding_type: net_new                 # first Archimedes finding for the SapphireSleet npm four-package cluster

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: "The Record (Recorded Future News) + BleepingComputer (Bill Toulas) — both relaying Amazon threat intelligence"
  source_yaml_id: the-record
  secondary_source_yaml_id: bleepingcomputer
  underlying_primary:
    source_name: "Amazon threat intelligence report (originating primary; SapphireSleet npm attribution + maintainer-social-engineering methodology across four packages)"
    grade: A                          # Tier-1 vendor threat-intel would grade A-class; NOT in source-grades.yaml, NOT directly retrieved this cycle
    in_hand_this_cycle: false
    yaml_status: not_in_source_grades  # flag for librarian: consider provisional amazon-threat-intel entry
  grade_rationale: >
    Anchored B on the two retrieved relays (The Record + BleepingComputer, both B per source-grades.yaml),
    which carry the Amazon report. The Amazon primary (A-class vendor threat intel) was NOT directly
    retrieved and is not yet in source-grades.yaml. Both in-window outlets relay the SAME Amazon report —
    publisher-independent but single upstream evidence basis.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent            # consistent with Stardust Chollima / BlueNoroff (DPRK financial-theft APT) established TTPs — crypto/credential theft, and with the broader documented DPRK npm/open-source supply-chain pattern (Lazarus npm, node-ipc / Shai-Hulud lineage)
    - probably_true_no_contradicting_ab        # no A/B-grade source contradicts; Google + Microsoft PREVIOUSLY linked the axios compromise to DPRK actors (partial independent support for the axios strand)
    - probably_true_claims_coherent            # packages (typo-crypto/debug/chalk/axios) are real, axios >100M weekly downloads is accurate, OSV designation MAL-2026-3400 internally coherent, maintainer-social-engineering (not vuln-exploitation) access vector is plausible
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld. The two in-window relays (The Record, BleepingComputer) both restate the
    SAME Amazon report — a shared upstream primary, so they are NOT independent corroboration of each other
    (INTEL-GRADING: two sources are not independent when both relay the same vendor document). Google's and
    Microsoft's PRIOR linkage of the axios compromise to DPRK is an independent second basis, but it covers
    only the axios strand, is referenced within the relay rather than separately retrieved this cycle, and
    does not confirm the CONSOLIDATED four-package maintainer-social-engineering methodology that is the
    graded claim. Single effective evidence basis for the consolidated claim -> at most grade 2.
  rationale: >
    The graded claim is Amazon's consolidation: a DPRK cluster (Amazon: SapphireSleet; aka BlueNoroff /
    Stardust Chollima / UNC1069) compromised four widely-used npm packages via maintainer social-engineering
    and pushed malicious updates (payload family MAL-2026-3400) to steal passwords, cryptocurrency, and
    personal data. Coherent, consistent with the actor's known financial-theft mission and the DPRK
    open-source-supply-chain pattern, no contradiction -> Probably True.
corroboration:
  independent_sources:
    - the-record
    - bleepingcomputer
  independent: false
  test_result: >
    FAILS independence for the consolidated claim. The Record and BleepingComputer are publisher-independent
    but relay the same Amazon report (single shared evidence basis). Google + Microsoft's prior axios->DPRK
    attribution is a genuinely independent second basis but is axios-strand-only and not separately retrieved
    this cycle; it strengthens confidence in the axios attribution without confirming the four-package
    consolidation. Outlet-level agreement supports "likely," not a confirmed-independent second basis.
first_party_precedence:
  applied: false
  queried_indices: [archimedes, defenseclaw_local]
  query_window: "-24h (grader confirmatory) + collector 15:30 pre-brief IOC/entity sweep"
  splunk_evidence: >
    Rule 8 run by grader this cycle: (index=archimedes OR index=defenseclaw_local) NOT sourcetype=archimedes:*
    over "SapphireSleet" / "BlueNoroff" / "MAL-2026-3400" / npm / Chalk -> 0 events, both indices. Collector's
    15:30 pre-brief sweep also 0 defender-telemetry hits. Visibility-bounded null — neither corroboration nor
    disconfirmation (Hard Rule 8). first_party_precedence not applied. Re-run if the malicious package
    versions or MAL-2026-3400 artifacts surface in first-party SDLC / package telemetry.
single_source_veto_applied: true
single_source_veto_note: >
  Applies — single effective evidence basis (the Amazon report, relayed by two publishers) for the
  consolidated four-package claim. WEP capped at "likely." Veto lifts on direct retrieval of the Amazon
  primary establishing an independent documentary basis, on a second vendor independently corroborating the
  full four-package methodology, or on first-party telemetry corroboration.
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "Amazon attributes maintainer-social-engineering compromise of four widely-used npm packages (typo-crypto ~Mar 2025; debug + chalk ~Sep 2025; axios ~Mar 2026, >100M weekly downloads) to a DPRK cluster it tracks as SapphireSleet; payload family MAL-2026-3400 (OSV); objective = theft of passwords, cryptocurrency, personal data. Access via socially engineering trusted package maintainers, NOT software-vulnerability exploitation."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-30-pm-001
  attribution_claims:
    - claimed_actor: "SapphireSleet (Amazon designation)"
      aka: [BlueNoroff, "Stardust Chollima", UNC1069, CageyChameleon, "Alluring Pisces"]
      nation: "North Korea (DPRK)"
      claimed_by_sources: ["Amazon threat intelligence (via The Record + BleepingComputer relays)"]
      prior_independent_support: "Google + Microsoft previously attributed/linked the axios compromise to North Korean actors (axios strand only)"
      roster_match: "#002 Stardust Chollima (via BlueNoroff / Sapphire Sleet aliases in _roster.yaml)"
      requires_analyst_review: true
      hard_rule_2_note: >
        Attribution RECORDED as Amazon's, not originated or upgraded by Archimedes. The alias UNC1069 is
        recorded verbatim from the relay and is NOT merged into the roster (prior /new-actor candidate;
        Hard Rule 2). SapphireSleet / BlueNoroff / Sapphire Sleet map to roster #002 Stardust Chollima via
        existing confirmed aliases.

# FLASH-adjacency adjudication (grader)
flash_adjacency:
  independently_warrants_flash: false
  rationale: >
    Tracked actor (#002) but NO active-exploitation-of-a-CVE event, NO named A&D victim, NO first-party hit,
    and the access vector is social engineering rather than a weaponizable vulnerability. Correctly held
    below-FLASH by the collector (and by the 12:00 sweep) for the afternoon board as a supply-chain-awareness
    item.

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update

# Downstream handoff flags
analyst_review_required: true            # attribution claim present + tracked actor (#002); WEP likely
analyst_review_complete: true
analyst_review_run_id: analyst-20260730-164000
red_team_review_required: false          # WEP ceiling 'likely' (< very_likely); analyst reinforces cap
red_team_review: null
analysis_sections:
  sat_ach:
    status: not_applied
    reason: no_multi_actor_competition
    detail: >
      ACH not warranted. Amazon attributes directly to a single DPRK cluster (SapphireSleet -> roster #002 via
      confirmed BlueNoroff/Sapphire Sleet aliases), with independent Google + Microsoft support on the axios
      strand. There is no genuine >=2-actor competition to adjudicate. Constructing rival-actor hypotheses here
      would risk originating attribution beyond the cited sources (Hard Rule 2). The live analytic questions are
      about ASSUMPTIONS (roster mapping, four-package consolidation, A&D-relevance chain), which KAC handles.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "A DPRK cluster Amazon tracks as SapphireSleet (roster #002 Stardust Chollima) compromised four
        widely-used npm packages (typo-crypto, debug, chalk, axios) via maintainer social-engineering, pushing
        malicious updates (MAL-2026-3400) to steal passwords, cryptocurrency, and personal data — relevant to
        A&D via the software supply chain."
      analyzed_at: 2026-07-30T16:58:00-04:00
      analyzed_by: analyst
      invoking_context: "Pre-publication review of attribution + A&D-relevance chain for the afternoon brief"
      assumptions:
        - id: A1
          statement: "Amazon's SapphireSleet -> DPRK attribution is reliable"
          category: source_reliability
          stated: true
          why_must_be_true: "The whole finding is an attributed-actor claim"
          when_could_be_false: "Amazon's cluster methodology is wrong, or SapphireSleet is a fuzzy label spanning multiple activity sets"
          evidence_for: [raw-2026-07-30-pm-001]   # Tier-1 vendor; Google+Microsoft independently linked the axios strand to DPRK
          evidence_against: []
          confidence: medium       # high for the axios strand (independent corroboration); medium for the cluster overall (single vendor)
          centrality: critical
          classification: qualify
        - id: A2
          statement: "SapphireSleet maps to roster #002 Stardust Chollima via BlueNoroff / Sapphire Sleet aliases"
          category: semantic
          stated: true
          why_must_be_true: "Determines whether this feeds the #002 dossier"
          when_could_be_false: "Amazon's SapphireSleet is a distinct cluster from what the roster calls Stardust Chollima; the UNC1069 alias (recorded verbatim, NOT merged) hints the cluster boundary is unsettled"
          evidence_for: [roster-002-aliases]
          evidence_against: []
          confidence: high         # BlueNoroff / Sapphire Sleet are confirmed roster #002 aliases
          centrality: material
          classification: sound
        - id: A3
          statement: "All FOUR packages are attributable to the same actor (the consolidation)"
          category: source_reliability
          stated: true
          why_must_be_true: "The finding presents a single four-package campaign"
          when_could_be_false: "The independent (Google/Microsoft) support covers ONLY axios; the other three (typo-crypto, debug, chalk) rest solely on Amazon's consolidation"
          evidence_for: [raw-2026-07-30-pm-001]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A4
          statement: "The access vector was maintainer social-engineering, not software-vulnerability exploitation"
          category: TTP_patterns
          stated: true
          why_must_be_true: "Shapes the defensive posture (identity/publish-rights hardening, not patching)"
          when_could_be_false: "Access was actually via a compromised token/CI pipeline rather than social engineering"
          evidence_for: [raw-2026-07-30-pm-001]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A5
          statement: "The npm compromise chain would plausibly reach a Tier-1 A&D software development lifecycle"
          category: capability
          stated: false
          why_must_be_true: "Underpins the A&D-relevance framing"
          when_could_be_false: "A&D SDLCs pin/vendor dependencies, use private registries, or don't transitively consume these packages; malicious versions caught before promotion"
          evidence_for: [raw-2026-07-30-pm-001]   # axios >100M weekly downloads makes transitive exposure plausible
          evidence_against: []
          confidence: low          # structural/plausible, NOT observed; no A&D victim named
          centrality: material
          classification: qualify
        - id: A6
          statement: "The payload objective (password/crypto/personal-data theft) is consistent with #002's financial-theft mission"
          category: actor_intent
          stated: true
          why_must_be_true: "Coherence of the attribution"
          when_could_be_false: "Objective differs on direct retrieval of MAL-2026-3400"
          evidence_for: [raw-2026-07-30-pm-001]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A7
          statement: "First-party Splunk would surface these packages/artifacts if present in Frank's environment"
          category: visibility
          stated: false
          why_must_be_true: "Justifies reading the Splunk null as (weak) reassurance"
          when_could_be_false: "Frank has no SDLC/package telemetry; the null is visibility-bounded (Hard Rule 8)"
          evidence_for: [splunk-negative-search]
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: sound     # null is non-dispositive; correctly not applied as precedence
      classifications_summary:
        sound: 4
        qualify: 3
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "The four-package consolidation is single-source (Amazon). Independent corroboration (Google + Microsoft) covers ONLY the axios strand — do not present all four as independently confirmed."
          - "A&D relevance is STRUCTURAL / indirect: no DIB victim named. The risk is the supply-chain vector (transitive-dependency exposure via a >100M-weekly-download package), not an observed A&D compromise."
          - "Attribution is Amazon's, recorded not originated. The UNC1069 alias is recorded verbatim and NOT merged into roster #002 pending /new-actor adjudication (Hard Rule 2)."
        blocking_assumption: null
        blocking_detail: "No Test-class assumptions. Publication proceeds at WEP 'likely' with the caveats above."
      recommended_wep_after_test:
        if_amazon_primary_retrieved_confirming_all_four: likely   # firms consolidation; veto still caps at likely absent a 2nd vendor
        if_only_axios_stays_corroborated: likely                   # three-package strand remains single-source; keep the consolidation caveat

# actor-profiler handoff
actor_profiler_handoff:
  roster_actor: "002"                    # Stardust Chollima
  recommended_action: consider_dossier_update
  note: >
    Amazon's four-package npm supply-chain consolidation (incl. axios >100M weekly downloads) is a candidate
    TTP/campaign addition to the Stardust Chollima (#002) dossier IF the analyst confirms the attribution
    stands. UNC1069 alias NOT to be merged without /new-actor adjudication (Hard Rule 2).

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-30-afternoon]
retracted: false
retraction_brief_id: null
---

# Amazon ties npm supply-chain compromises of debug, chalk, axios and typo-crypto to DPRK cluster SapphireSleet (BlueNoroff / Stardust Chollima)

## Summary

Amazon threat intelligence attributes the compromise of four widely-used npm packages to a North Korean cluster it tracks as SapphireSleet — mapped in our roster to Stardust Chollima (#002) via its BlueNoroff / Sapphire Sleet aliases. Per The Record and BleepingComputer (both relaying the Amazon report), the actor gained access by socially engineering trusted package maintainers rather than exploiting software flaws, then published malicious updates to typo-crypto (~March 2025), debug and chalk (~September 2025), and axios (~March 2026, >100M weekly downloads). The payload family is tracked as MAL-2026-3400 in OSV; the reported objective is theft of passwords, cryptocurrency, and personal data. Graded B2 (two B-grade relays of one un-retrieved Amazon primary — single effective evidence basis); single-source veto caps the assessment at "likely." Google and Microsoft had previously linked the axios compromise to DPRK actors, which independently supports the axios strand but not the full four-package consolidation.

## Grade rationale

- **Source B** — The Record (B) and BleepingComputer (B) are the retrieved sources; the Amazon primary (A-class vendor threat intel) was not directly retrieved and is not yet in source-grades.yaml (flagged for librarian).
- **Credibility 2** — coherent, consistent with Stardust Chollima's financial-theft mission and the DPRK open-source-supply-chain pattern; but both relays share one Amazon evidence basis, so no confirmed-independent second source for the consolidated claim -> cannot reach 1.
- **Single-source veto applied** — one effective evidence basis -> WEP held at "likely."

## Sources

### The Record — Recorded Future News (the-record, digraph: B)

- URL: https://therecord.media/north-korea-hackers-amazon-malware
- Published: 2026-07-30T09:00 EDT
- Key claim: Amazon identified a North Korean cluster (SapphireSleet) behind the compromise of several high-profile npm libraries via maintainer social-engineering.

### BleepingComputer — Bill Toulas (bleepingcomputer, digraph: B)

- URL: https://www.bleepingcomputer.com/news/security/amazon-links-debug-chalk-npm-supply-chain-attacks-to-north-korean-hackers/
- Published: 2026-07-30T14:13 EDT
- Key claim: Amazon links the debug/chalk/axios/typo-crypto npm compromises to DPRK; payload tracked as MAL-2026-3400 (OSV).

## Technical detail

Access vector is human, not technical: the actor reportedly social-engineered trusted npm package maintainers to obtain publish rights, then shipped malicious versions of legitimate, heavily-depended-upon packages. The axios compromise is the highest-blast-radius instance at >100M weekly downloads ("embedded in countless web applications and enterprise services" — paraphrased). Payload family MAL-2026-3400 (OSV) reportedly targets passwords, cryptocurrency, and personal data — consistent with a financially-motivated DPRK mission. No atomic domains, IPs, hashes, or wallet addresses were present in the relay layer; pending direct retrieval of the Amazon primary and the OSV MAL-2026-3400 record. Recorded at awareness level (Hard Rule 3 — no exploit/payload mechanism).

## IOCs surfaced

```yaml
atomic_iocs: []                          # no domains/IPs/hashes/wallets in the relay layer
package_iocs:
  - type: npm_package
    value: "typo-crypto"
    context: "malicious version ~March 2025"
    confidence: reported
  - type: npm_package
    value: "debug"
    context: "legitimate package, malicious update ~September 2025 (maintainer social-engineering)"
    confidence: reported
  - type: npm_package
    value: "chalk"
    context: "legitimate package, malicious update ~September 2025"
    confidence: reported
  - type: npm_package
    value: "axios"
    context: "malicious update ~March 2026 (>100M weekly downloads); previously linked to DPRK by Google + Microsoft"
    confidence: reported
malware_id:
  - value: "MAL-2026-3400"
    context: "OSV-database designation for the payload family"
    confidence: reported
credential_exposure_detected: false      # objective is credential theft, but no credential VALUES present (Hard Rule 7)
```

## Relationship to existing findings

DPRK double-header with finding-2026-07-30-0006 (Lazarus #003 / Gunra ransomware overlap) on this same afternoon board — DISTINCT findings: different actor (#002 vs #003), different campaign (npm supply-chain vs ransomware-nexus tool-sharing), different originating primary (Amazon vs AhnLab + SK agencies). NOT merged (merging would create a multi-claim cluster and imply corroboration that does not exist). The briefer may present both under a shared DPRK section. Continues the open-source-supply-chain threat class the corpus tracks (VT-006 Mini Shai-Hulud lineage; node-ipc precedents) — related as a class, not the same campaign.

## A&D relevance

Structural / indirect. npm maintainer-compromise -> malicious dependency updates is the same operational template that would reach a Tier-1 A&D software development lifecycle (the axios blast radius makes transitive-dependency exposure plausible across enterprise/DIB tooling). No A&D victim named; relevance is the supply-chain vector, not a named-prime compromise.

## Analytic notes (from analyst review)

KAC applied; ACH declined (run analyst-20260730-164000). No genuine multi-actor competition exists — Amazon attributes directly to one DPRK cluster with independent Google + Microsoft support on the axios strand, so constructing rival-actor hypotheses would risk originating attribution (Hard Rule 2). The analytic action is in the assumptions.

Two qualifiers should reach the briefer. First, the four-package consolidation is single-source (Amazon); the independent corroboration covers only axios, so typo-crypto, debug, and chalk rest solely on Amazon's consolidation. Present the axios strand as the well-supported anchor and the other three as consolidated-by-Amazon. Second, A&D relevance is structural and indirect — no DIB victim is named. The exposure is the supply-chain vector (a malicious update to a >100M-weekly-download dependency reaching an enterprise/DIB SDLC transitively), not an observed compromise. The roster mapping to #002 via BlueNoroff/Sapphire Sleet is sound; the UNC1069 alias stays recorded-not-merged. No test blocks publication; the grade stays "likely."

## Open questions for analyst

- **Attribution (Hard Rule 2).** Amazon attributes to SapphireSleet; roster maps to Stardust Chollima (#002) via BlueNoroff / Sapphire Sleet. Confirm the mapping holds and whether the UNC1069 alias warrants /new-actor adjudication (recorded verbatim, NOT merged).
- **Consolidation vs prior attribution.** Google + Microsoft previously linked only axios to DPRK; Amazon consolidates four packages. Does the independent axios support extend analytically to the other three, or is the consolidation single-source (Amazon)?
- **Direct retrieval.** Amazon primary + OSV MAL-2026-3400 record not retrieved — retrieval would firm the payload artifacts and could establish an independent documentary basis (candidate to lift credibility).
