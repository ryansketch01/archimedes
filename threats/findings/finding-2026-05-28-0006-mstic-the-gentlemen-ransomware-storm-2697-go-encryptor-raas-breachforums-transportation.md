---
finding_id: finding-2026-05-28-0006-mstic-the-gentlemen-ransomware-storm-2697-go-encryptor-raas-breachforums-transportation
created_at: 2026-05-28T16:11:00-04:00
graded_by: grader
grading_run_id: afternoon-20260528-160000
grading_mode: scheduled_brief
test: false

# Core grading
digraph: A2
source_reliability:
  grade: A
  source_name: "Microsoft Threat Intelligence (MSTIC)"
  source_yaml_id: mstic
  grade_rationale: >
    Pre-assigned A per source-grades.yaml. Tier-1 vendor research with
    first-party Defender telemetry — MSTIC is the originating canonical
    source on the Storm-* numbering taxonomy and on its own Defender
    detection signature (Ransom:Win64/Gentlemen). Single Tier-1 vendor
    primary in this sweep window; no parallel Mandiant / CrowdStrike /
    Unit 42 publication.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent_with_observed_raas_evolution_pattern_breachforums_affiliate_recruitment
    - probably_true_no_contradicting_a_b_grade_source
    - probably_true_technical_claims_internally_coherent_per_file_curve25519_xchacha20_garble_obfuscation_21_vector_lateral_movement_psexec_wmic_wmi_winrm_scheduled_tasks_services_all_individually_verifiable
  rationale: >
    MSTIC is the originating primary on Storm-2697 attribution and on
    The Gentlemen technical analysis. The Storm-* numbering convention
    is MSTIC-canonical (consistent precedent across Storm-0501 / Storm-
    1811 / Storm-2697 reporting class). Defender first-party telemetry
    is the underlying evidence base — MSTIC has direct observational
    authority on its own products' detection signatures. Technical
    design (Curve25519 ECDH per-file ephemeral keys + XChaCha20 stream
    cipher + Garble Go obfuscation + partial-encryption tiers + 21-
    vector lateral movement + dual persistence) is internally coherent
    and matches established cryptographic-modern-ransomware design
    patterns. RaaS-affiliate-recruitment via BreachForums is consistent
    with the corpus-tracked TeamPCP / Bling Libra / ShinyHunters
    operational pattern of affiliate-funnel-via-cybercrime-forum. No
    contradicting source. Credibility 2 (Probably True) is the ceiling
    absent second independent vendor publication — single Tier-1
    vendor on the new-actor introduction layer.
corroboration:
  independent_sources:
    - mstic
  independent: false
  test_passed: >
    No second independent vendor publication observed this sweep. MSTIC
    stands alone as originating primary. Single-source on the new-actor
    introduction. Defender telemetry provides high-quality evidence
    base but does not satisfy the independent-corroboration test
    (vendor-internal telemetry is one source).
first_party_precedence:
  applied: false
  splunk_evidence: null
  rationale: >
    Three SHA-256 hashes published (22b38d... encryptor; 078163... PsExec
    binary; fe1033... wallpaper BMP). Splunk first-party check against
    defenseclaw_local / archimedes indexes for these hashes is a
    candidate enrichment step but was not invoked in this grading pass.
    Recommend Splunk hunt at next sweep regardless of grade outcome.
single_source_veto_applied: true
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "MSTIC introduces Storm-2697 / 'The Gentlemen' RaaS — Go-based self-propagating encryptor with Curve25519+XChaCha20, 21-vector lateral movement, BreachForums affiliate-recruitment partnership; targets education, transportation, healthcare, financial"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-28-pm-002
  attribution_claims:
    - claimed_actor: "Storm-2697 (MSTIC designation; manages 'The Gentlemen' RaaS)"
      claimed_by_sources: [mstic]
      requires_analyst_review: true
      notes: >
        New-to-corpus actor designation. MSTIC procedural framing —
        "financially motivated threat actor that manages the RaaS
        platform known as 'The Gentlemen'." No nation / service
        attribution. Candidate for actor-profiler /new-actor scaffold
        decision (collector flagged; not initiated).

# Inclusion eligibility
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update

# Downstream handoff
analyst_review_required: true   # WEP ceiling "likely" + transportation sector A&D-adjacency + new-actor introduction
analyst_review_complete: true
analyst_review_run_id: analyst-20260528-1625
red_team_review_required: false # WEP capped at "likely" by single-source veto
red_team_review: null
analysis_sections:
  sat_ach: null  # not warranted — MSTIC canonical on Storm-2697 designation; no competing-actor question; single-source veto already caps WEP
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Storm-2697 / 'The Gentlemen' RaaS, after a September 2025 pivot from
        closed operations and a BreachForums affiliate partnership, will likely
        produce increased activity targeting transportation, education,
        healthcare, and financial sectors — with DIB tier-2/3 logistics
        adjacency via transportation-sector compromise" (paraphrased MSTIC +
        analyst forward-projection).
      analyzed_at: 2026-05-28T16:25:00-04:00
      analyzed_by: analyst
      invoking_context: "Analyst review on single-source A2 actor introduction; WEP capped at 'likely' by single-source veto; transportation-sector A&D adjacency assessed structurally"
      assumptions:
        - id: A1
          statement: "Storm-2697 is a coherent actor entity, not a cluster of related affiliates MSTIC has retroactively labeled"
          category: actor_continuity
          stated: false
          why_must_be_true: "Forward-projection of activity assumes actor-coherence"
          when_could_be_false: "MSTIC Storm-* numbering is sometimes provisional cluster assignment subject to later split / merge (see Storm-0501 lineage)"
          evidence_for: [mstic]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A2
          statement: "MSTIC's BreachForums-partnership characterization is operationally validated, not promotional / aspirational text from the actor"
          category: source_reliability
          stated: false
          why_must_be_true: "Increased-activity forecast is grounded in this partnership claim"
          when_could_be_false: "BreachForums posts can be self-promotional; Defender telemetry on the underlying recruitment funnel is the validation lever"
          evidence_for: [mstic]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A3
          statement: "RaaS-affiliate model is operationally sustainable for Storm-2697 (no LE / infrastructure-disruption visible)"
          category: actor_operational_status
          stated: false
          why_must_be_true: "Forward-projection assumes operational continuity"
          when_could_be_false: "BreachForums has historically been a takedown target (multiple seizures); affiliate-funnel disruption can follow rapidly"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: material
          classification: qualify
        - id: A4
          statement: "Transportation sector targeting in MSTIC's named victim categories includes DIB-logistics-relevant operators (airlines, shipping, freight, port, rail)"
          category: semantic
          stated: false
          why_must_be_true: "DIB tier-2/3 logistics adjacency depends on this categorical overlap"
          when_could_be_false: "MSTIC 'transportation' may be civilian / urban-transit dominant; DIB-logistics is a specific subset"
          evidence_for: [mstic]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A5
          statement: "DIB-logistics-flow compromise via transportation-sector ransomware would cascade to DIB-prime supply-chain continuity"
          category: capability
          stated: false
          why_must_be_true: "A&D-relevance narrative depends on cascading-impact mechanism"
          when_could_be_false: "DIB primes may have logistics redundancy / alternate-carrier contingency / inventory buffer absorbing transportation-sector ransomware impact within recovery windows"
          evidence_for: []
          evidence_against: []
          confidence: low
          centrality: critical
          classification: test
          proposed_test: >
            Query DIB-prime continuity-of-operations posture on transportation-
            partner ransomware via published 10-K risk disclosures and DCSA /
            DFARS continuity-of-operations guidance. Alternatively, Splunk
            first-party hunt for the three SHA-256 hashes across
            defenseclaw_local to validate any direct or indirect telemetry.
            Test resolves whether transportation-sector compromise is a
            modeled risk in DIB-prime continuity planning.
        - id: A6
          statement: "The three SHA-256 hashes MSTIC published are representative IOCs that will fire on actor's future builds (not single-build artifacts)"
          category: TTP_patterns
          stated: false
          why_must_be_true: "Splunk hunt recommendation depends on hash durability"
          when_could_be_false: "Modern ransomware encryptors rebuild per-affiliate / per-build; hash IOCs may fire only on the specific MSTIC-analyzed sample"
          evidence_for: [mstic]
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: qualify
        - id: A7
          statement: "MSTIC's first-party Defender telemetry is the canonical evidence base on Storm-2697 — no other Tier-1 vendor has produced independent visibility yet"
          category: source_reliability
          stated: true
          why_must_be_true: "Single-source veto applied; WEP capped at 'likely'"
          when_could_be_false: "Second Tier-1 vendor (Mandiant / CrowdStrike / Unit 42 / Sophos / ESET) may have already detected and not yet published"
          evidence_for: [mstic]
          evidence_against: []
          confidence: high
          centrality: critical
          classification: sound
        - id: A8
          statement: "Storm-2697 is not a rebrand / spin-off of an existing tracked RaaS operation (LockBit, Cl0p, BlackCat / ALPHV remnant)"
          category: actor_continuity
          stated: false
          why_must_be_true: "New-actor introduction status depends on non-overlap"
          when_could_be_false: "RaaS rebranding is the standard pattern; some Go-encryptor designs in 2025-2026 share code lineage"
          evidence_for: [mstic]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 2
        qualify: 5
        test: 1
        reject: 0
      remediation:
        status: proceed_with_test_flag
        blocking_assumption: null
        test_assumption: A5
        test_detail: >
          Assumption A5 (DIB-logistics cascading impact) is classified Test
          but does NOT block the assessment because the underlying actor
          claim (Storm-2697 exists, MSTIC-attributed, RaaS-affiliate-growing)
          is itself well-supported. The Test classification applies only to
          the DOWNSTREAM A&D-relevance inference. Briefer should treat the
          transportation-DIB-cascade as a flagged structural inference, not
          a confirmed cascade. Test would resolve via DIB-prime continuity
          disclosures + Splunk first-party hash hunt.
        qualifying_caveats:
          - "Storm-2697 actor-coherence (vs. provisional cluster label) is medium-confidence; designation may split / merge in later MSTIC reporting"
          - "BreachForums-partnership operational reality vs. promotional posting validated only by MSTIC Defender telemetry"
          - "RaaS-affiliate sustainability assumes no near-term LE / BreachForums-takedown disruption"
          - "MSTIC 'transportation' victim category may include civilian / urban-transit operators not directly in DIB-logistics-flow class"
          - "Three published SHA-256 hashes are likely build-specific; Splunk hunt productive but low base-rate expectation"
        next_action: "Brief at WEP 'likely' with transportation-DIB-cascade explicitly flagged as structural inference. Splunk hunt of three hashes regardless of brief inclusion. Watch for second Tier-1 vendor publication within 14 days to lift to A1 candidate."
      recommended_wep_after_test:
        if_dib_logistics_cascade_validated: likely  # no change
        if_dib_logistics_cascade_unsupported: likely  # core actor claim still stands; only A&D-relevance qualifier drops
        if_second_vendor_corroborates_storm_2697: very_likely  # lifts single-source veto

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-05-28-afternoon]
retracted: false
retraction_brief_id: null
---

# MSTIC Introduces Storm-2697 / "The Gentlemen" RaaS — Go Encryptor, 21-Vector Lateral Movement, BreachForums Affiliate Partnership

## Summary

Microsoft Threat Intelligence on 2026-05-28 published a technical analysis of "The Gentlemen" ransomware, attributing the platform to MSTIC-tracked actor **Storm-2697** (financially motivated, manages the RaaS). The encryptor is Go-based, Garble-obfuscated, and uses per-file ephemeral Curve25519 ECDH keys with XChaCha20 stream cipher — modern cryptographic design that defeats post-compromise key-recovery. The operational design centers on aggressive self-propagation: 21 remote operations per target spanning PsExec, WMIC, WMI, WinRM, scheduled tasks, and services, with deployment attempts from both infected-host SMB shares and target `C:\Temp` directories. Storm-2697 pivoted from closed-group operations (mid-2025) to RaaS in September 2025 and recently established a BreachForums partnership to recruit affiliates including penetration testers and initial access brokers. MSTIC named sectors include **transportation** (DIB tier-2/3 logistics adjacency), **education** (university-research / FFRDC / DoD-collaborative-research adjacency), healthcare, and financial; geographies span all populated continents. No A&D primes named.

## Sources

### MSTIC blog (mstic, digraph: A)

- URL: https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/
- Published: 2026-05-28T15:00:00Z (11:00 EDT)
- Author: Microsoft Threat Intelligence
- Key claim: Storm-2697 manages 'The Gentlemen' RaaS; affiliates carry out attacks. BreachForums partnership recently established to recruit penetration testers and initial access brokers. MSTIC warning: "this partnership may lead to increased activity as the program becomes accessible to a broader pool of threat actors" (verbatim, ≤15 words).

## Technical detail

### Encryption design
- Language: Go, obfuscated with Garble
- Per-file ephemeral Curve25519 ECDH key exchange
- XChaCha20 stream cipher
- Partial-encryption tiers: `--ultrafast` (~0.9% total), `--superfast` (~3%), `--fast` (~9%), and default full

### Operator command-line knobs
- `--password` (required, build-specific access password)
- `--path` (comma-separated target paths)
- `--T` (delay-before-encryption in minutes)
- `--silent` (suppress renaming / timestamp / wallpaper changes)
- `--system` (encrypt as SYSTEM, local drives only)
- `--shares` (encrypt mapped drives / UNC shares only)
- `--full` (two-phase, relaunches itself as `--system` + `--shares`)
- `--spread <domain/user:password>` (self-propagation; current-session token used if no credential)
- `--keep` (disable self-delete)
- `--wipe` (wipe free disk space)

### Host preparation
- Disables Microsoft Defender
- Removes shadow copies
- Removes event logs
- Terminates 60+ processes (databases, backup software, EDR agents, Office apps)
- Enables network discovery + UPnP
- Dual persistence (scheduled tasks + registry Run keys)

### Lateral movement
21 remote operations per target across PsExec, WMIC, WMI, WinRM, scheduled tasks (user + SYSTEM context), Windows services, PowerShell remoting. Deployment from both infected-host SMB share AND target `C:\Temp` directory.

### Double extortion
Data exfiltration paired with encryption; threats of public release for non-payment.

### Detection
- Microsoft Defender: `Ransom:Win64/Gentlemen`
- EDR alert classes: "Ransomware-linked threat actor detected" / "File backups were deleted" / "Ransomware behavior in file system"

## IOCs surfaced

```yaml
sha256_hashes:
  - 22b38dad7da097ea03aa28d0614164cd25fafeb1383dbc15047e34c8050f6f67   # The Gentlemen encryptor
  - 078163d5c16f64caa5a14784323fd51451b8c831c73396b967b4e35e6879937b   # PsExec binary (operationalized)
  - fe1033335a045c696c900d435119d210361966e2fb5cd1ba3382608cfa2c8e68   # Wallpaper BMP (post-encryption desktop change)
defender_signature: "Ransom:Win64/Gentlemen"
ip_addresses: []   # not published in MSTIC summary
domains: []        # not published in MSTIC summary
cves: []
```

**Splunk hunt recommended** against defenseclaw_local / archimedes for the three SHA-256 hashes regardless of brief inclusion.

## Relationship to existing findings

- Corpus-adjacent to morning brief finding-2026-05-28-0003 (Unit 42 "Out of the Crypt" extortion-economy analysis — TGR-CRI-1135 TeamPCP + Bling Libra ShinyHunters + Hazy Scorpius CL0P). Storm-2697 / The Gentlemen sits in the same RaaS-affiliate-recruitment-via-cybercrime-forum economic pattern.
- Adjacent to corpus-tracked TeamPCP roster #001 (HIGH threat-level, SDLC / supply-chain / BreachForums RaaS-affiliate lineage) — same affiliate-recruitment-via-BreachForums pattern but distinct actor; not a roster expansion.
- Transportation-sector targeting echoes the DIB tier-2/3 logistics adjacency concerns that have surfaced repeatedly in 2026 corpus.

## Open questions for analyst

- **Single-source veto applied.** WEP capped at "likely" pending second-vendor corroboration (Mandiant / CrowdStrike / Unit 42 / Sophos / ESET). If a second Tier-1 vendor publishes on The Gentlemen / Storm-2697 within 14 days, regrade to A1 candidate.
- **New-actor decision.** Storm-2697 NOT in `_roster.yaml`. Candidate for actor-profiler /new-actor scaffold decision — collector flagged. Analyst should advise on roster-entry merit given RaaS-affiliate-growth-trajectory.
- **Transportation A&D adjacency.** Major US transportation operators (airlines, shipping, freight, port operations, maritime, rail) support DoD logistics flows for DIB tier-1 primes. Cascading-impact analysis (SAT-KAC on the assumption "transportation-sector compromise is isolated from DIB-flow continuity") would surface DIB-prime supply-chain exposure.
- **Splunk hunt.** Three SHA-256 hashes published — recommend defenseclaw_local / archimedes hunt regardless of brief inclusion.

## Source notes

- All quotes ≤15 words per Hard Rule 6.
- MSTIC publication is direct A-grade with first-party Defender telemetry as evidence base.
- New-to-corpus actor introduction; novel attribution flag NOT applied because Storm-2697 is MSTIC-originated, not Archimedes-originated.

## Analytic notes (from analyst review)

KAC surfaces eight assumptions; the core actor claim (Storm-2697 exists, MSTIC-attributed, RaaS-affiliate-recruitment via BreachForums) holds at WEP "likely" with single-source veto appropriately applied. ACH is not warranted because no competing-actor question exists — MSTIC is canonical on its own Storm-* numbering. The interesting analytic load is downstream: the transportation-sector → DIB-logistics-cascade inference (A5) is the one Test-classified assumption — low-confidence, critical-centrality for the A&D-relevance narrative. It does not block the assessment but the briefer should treat the cascade as a structural inference, not a validated cascade.

Two secondary qualifying caveats matter for briefer framing: (1) MSTIC "transportation" category may include civilian / urban-transit operators distinct from DIB-logistics-flow operators (A4 medium-confidence), and (2) the three SHA-256 hashes are likely build-specific rather than durable across affiliate rebuilds (A6 low-confidence, peripheral). Splunk hunt for the three hashes against defenseclaw_local is recommended regardless of brief inclusion. WEP ceiling stays at "likely"; if a second Tier-1 vendor corroborates Storm-2697 within 14 days, lift to A1 candidate via regrade.
