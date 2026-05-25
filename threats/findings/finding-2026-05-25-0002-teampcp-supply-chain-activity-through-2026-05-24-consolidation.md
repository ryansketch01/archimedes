---
finding_id: finding-2026-05-25-0002-teampcp-supply-chain-activity-through-2026-05-24-consolidation
created_at: 2026-05-25T16:00:00-04:00
graded_by: grader
grading_run_id: afternoon-20260525-160000
grading_mode: scheduled_brief
test: false

# Core grading (admiralty-grading skill output)
digraph: B3
digraph_layered:
  hartman_secondary_synthesis_one_week_consolidation_through_2026_05_24: B2
  teampcp_attribution_chain_preserved_through_cite_to_corpus_anchored_primaries: B2
  nx_console_vs_code_extension_18min_window_2026_05_18_corpus_anchored: A2
  echarts_for_react_size_sensor_atantv_mass_wave_corpus_anchored: A2
  durabletask_pypi_microsoft_published_sdk_trojanization_corpus_anchored: A2
  github_internal_repos_3800_exfiltrated_2026_05_24_corpus_anchored: A2
  cve_2026_45321_oidc_credential_abuse_chain_vt006_corpus_anchored: A2
  61274_npm_granular_access_tokens_invalidated_corpus_anchored: A2
  42_packages_forged_sigstore_badges_corpus_anchored: A2
  named_downstream_victims_openai_grafana_mistral_corpus_anchored: A2
  framework_source_code_drop_github_2026_05_22_love_teampcp_readme_vendor_primary_pending: B3
  at_least_three_forks_within_hours_including_freebsd_variant_vendor_primary_pending: B3
  change_keys_and_c2_as_needed_readme_string_commoditization_signal_vendor_primary_pending: B3
  durabletask_linux_disk_wiper_capability_safedep_first_observation_pending_grader_verification: B3
  cisa_explicitly_did_not_add_cve_2026_45321_to_kev_as_of_2026_05_22_catalog_release: A1
  ransomware_monetization_channels_vect_cipherforce_remained_inactive_during_window: B2
  c2_filev2_seed1_getsession_org_session_messenger_corpus_anchored: A1
  persistence_files_claude_settings_json_vscode_tasks_json_corpus_anchored: A2
  splunk_first_party_zero_hits_on_consolidation_keywords: A1
  no_actor_originating_attribution_by_hartman_per_hard_rule_2_block: A1
  no_ad_prime_named_in_consolidation: A1
  cluster_anchor: B3

digraph_anchor: >
  Cluster digraph B3 anchored on the load-bearing net-new claim layer:
  Hartman / SANS ISC 2026-05-25 13:26 UTC consolidates one calendar
  week of TeamPCP (corpus-tracked roster #001 HIGH) supply-chain
  campaign activity through 2026-05-24 and identifies three net-new
  capability layers not previously corpus-anchored. The most novel
  layer — a TeamPCP framework source-code public drop to GitHub on
  2026-05-22 with README strings "Love - TeamPCP" and "Change keys
  and C2 as needed", with at least three forks deployed within hours
  including a FreeBSD variant — is single-sourced via Hartman who
  cites "documented by vendors" without naming the vendor primary.
  Vendor-primary retrieval is pending. The second net-new layer
  (durabletask Linux disk-wiper capability) cites SafeDep 2026-05-20
  corpus-anchored but disk-wiper-specific first-observation language
  has not been independently verified in the Archimedes corpus prior
  to this Hartman consolidation. The third net-new layer (CISA
  explicitly did NOT add CVE-2026-45321 to KEV as of 2026-05-22
  catalog release) was INDEPENDENTLY VERIFIED this sweep against
  KEV catalogVersion 2026.05.22 dateReleased 2026-05-22T18:00:11Z —
  the claim is factually correct.

  B3 (not B2, not A2) holds on the CLUSTER anchor because:
    - sans-isc is graded B per source-grades.yaml (community-vetted
      research; Kenneth Hartman named-byline diary author with
      Didier Stevens handler-on-duty).
    - The cluster anchor's load-bearing net-new layer is the
      framework-leak claim (most novel; first observed instance in
      corpus of TeamPCP campaign-source-code public-drop with
      explicit framework attribution). That layer is SINGLE-SOURCE
      (Hartman) and cites unnamed vendor primaries — credibility 3
      (Possibly True) pending vendor-primary retrieval.
    - Credibility 3 (not 2) because while the framework-leak claim
      is consistent with established TeamPCP TTPs (corpus-anchored
      campaign-source-code style) and technically plausible (GitHub
      hosts TeamPCP-attributed forks per Hartman observation), it
      requires the multiple-unverified-assumption that Hartman's
      unnamed-vendor citation is reliable. The Hartman secondary-
      synthesis pattern itself is corpus-precedent-trusted (sans-isc
      diaries have a multi-decade track record), but the absent
      vendor primary cap credibility at "Possibly True" not
      "Probably True".
    - Cluster includes A1 sub-layer (CISA-NOT-on-KEV independently
      verified against catalog version 2026.05.22) and multiple A2
      corpus-anchored sub-layers (Nx Console, durabletask, @antv,
      GitHub internal repos, OIDC credential abuse chain CVE-2026-
      45321). These do NOT lift the cluster anchor — the cluster
      anchor is graded on the load-bearing NET-NEW claim, not the
      corpus-anchored carry-forward layers.
    - Single-source veto applies on the framework-leak layer per
      Step 5: WEP ceiling capped at "likely" on the framework-leak
      claim regardless of B-grade source reliability.

  Hard Rule 2 binding: Hartman piece is SECONDARY SYNTHESIS / TIMELINE
  CONSOLIDATION — it cites originating vendors (Microsoft Security
  Blog 2026-05-20; SafeDep 2026-05-19/20; GitHub CISO Alexis Wales
  2026-05-21; vendor-unnamed framework-leak documentation 2026-05-22)
  for primary observations but does NOT present any primary first-
  observation itself. The TeamPCP attribution chain is preserved
  through-cite to corpus-anchored primaries (TeamPCP roster #001;
  finding-2026-05-12-FLASH-0001 originating attribution; finding-
  2026-05-20-FLASH-0001 GitHub-corp compromise). Archimedes does
  NOT promote Hartman's secondary synthesis to new first-observation
  attribution.

source_reliability:
  grade: B
  source_name: "SANS Internet Storm Center (Kenneth Hartman byline; Didier Stevens handler-on-duty)"
  source_yaml_id: sans-isc
  grade_rationale: >
    Pre-assigned B per source-grades.yaml — "Quality research but
    community-contributed." Kenneth Hartman is named-byline diary
    author; Didier Stevens is handler-on-duty (long-running ISC
    handler, multi-decade malware-analysis veteran). Hartman piece
    is a timeline-consolidation / TTP-map UPDATE on the corpus-
    tracked TeamPCP supply-chain campaign, citing originating
    vendors (Microsoft, SafeDep, GitHub CISO) for primary
    observations. Hartman synthesizes; does not originate primary
    observations.
  provisional: false

credibility:
  grade: 3
  checklist_passed:
    - possibly_true_single_source_uncorroborated_b_grade_on_framework_leak_layer
    - possibly_true_partially_consistent_with_known_ttps_but_some_elements_novel
    - possibly_true_technical_claims_plausible_but_not_independently_verifiable_on_framework_leak_specifically
  rationale: >
    The cluster anchor's load-bearing net-new layer (framework
    source-code GitHub drop 2026-05-22 with "Love - TeamPCP" and
    "Change keys and C2 as needed" README strings + three forks
    including FreeBSD variant) is single-source via Hartman who
    cites "documented by vendors" without naming vendor primary.
    Credibility 3 (Possibly True): consistent with TeamPCP
    established TTPs (campaign-source-code style commoditization is
    novel-for-TeamPCP but consistent with general open-sourcing
    trend across cybercrime-as-a-service operators); technical
    claim plausible (GitHub hosts TeamPCP-attributed forks per
    Hartman observation); not independently verifiable in
    Archimedes corpus at this sweep pending vendor-primary
    retrieval. Cannot rise to credibility 2 (Probably True) because
    Probably True requires no contradicting evidence AND consistent
    with established TTPs AND technical claims internally coherent
    — the "no contradicting evidence" condition is satisfied but
    the framework-source-public-drop element is novel-for-TeamPCP
    in the Archimedes corpus and requires vendor-primary
    verification before promotion to Probably True. The CISA-NOT-
    on-KEV sub-layer is independently verified (credibility 1) but
    does not lift the cluster anchor.

corroboration:
  independent_sources:
    - sans-isc
  independent: false
  test_passed: >
    Hartman is the sole originating primary on the consolidation
    framing. Originating vendor primaries cited by Hartman
    (Microsoft Security Blog 2026-05-20, SafeDep 2026-05-19/20,
    GitHub CISO Alexis Wales 2026-05-21, vendor-unnamed framework-
    leak documentation 2026-05-22) are corpus-anchored on
    everything EXCEPT the framework-leak layer. The framework-leak
    layer specifically has NO independently retrieved vendor
    primary — Hartman cites unnamed vendors. Cluster fails
    corroboration on the load-bearing net-new layer.

first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_query_executed: >
    Component of consolidated 17-IOC sweep against
    `defenseclaw_local` documented in raw-2026-05-25-pm-000 sentinel.
    Result: ZERO hits on TeamPCP / Mini Shai-Hulud / framework-leak
    / durabletask / @antv keywords in -24h@h. Per Hard Rule 8,
    silence is not disconfirming.

single_source_veto_applied: true
single_source_veto_rationale: >
  Step 5 single-source veto applies to the framework-leak claim
  (sole-source Hartman citing unnamed vendor primary). WEP ceiling
  capped at "likely" on the framework-leak claim regardless of
  source-letter-grade B and corpus-anchored carry-forward A2
  sub-layers. Corpus-anchored sub-layers (Nx Console, durabletask,
  @antv, GitHub internal repos, CVE-2026-45321) retain their
  original finding-tier WEPs (very likely / very likely / very
  likely / very likely / likely respectively from finding-2026-05-
  12-FLASH-0001 and finding-2026-05-20-FLASH-0001).

wep_ceiling: likely
wep_layered:
  framework_leak_claim_vendor_primary_pending: likely
  durabletask_linux_disk_wiper_capability_safedep_first_obs_pending: likely
  cisa_not_on_kev_as_of_2026_05_22_catalog_release: very_likely
  corpus_anchored_carry_forward_layers: very_likely

inclusion:
  eligible_for:
    - daily_brief_monitoring
    - weekly_synthesis
    - actor_profile_update
  not_eligible_for:
    - flash                         # B3 below B2 FLASH threshold
    - daily_brief_action            # B3 below B2 action threshold
  inclusion_rationale: >
    Cluster anchor B3 → eligible for daily brief monitoring
    (≥C3 threshold met). Eligible for actor profile update on
    TeamPCP #001 dossier — the durabletask Linux disk-wiper layer
    (if confirmed) is a destructive-category addition to
    predominantly credential-theft tradecraft with threat-box
    recalibration implications. Eligible for weekly synthesis as
    consolidation surface. NOT eligible for FLASH (single-source
    veto + below B2 threshold) or daily brief action items
    (below B2 threshold).

# Cluster metadata
cluster:
  topic: "TeamPCP supply-chain campaign consolidation through 2026-05-24 (Hartman/SANS ISC; three net-new capability layers identified)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-05-25-pm-001-isc-sans-hartman-teampcp-supply-chain-activity-through-2026-05-24-consolidation
  attribution_claims:
    - claimed_actor: TeamPCP
      claimed_actor_roster_id: "001"
      claimed_by_sources: [sans-isc]
      attribution_specificity: >
        Hartman preserves the corpus-anchored TeamPCP attribution
        through-cite to originating vendors (Microsoft Security
        Blog 2026-05-20, SafeDep 2026-05-19/20, GitHub CISO Alexis
        Wales 2026-05-21). Does NOT originate new attribution.
      hard_rule_2_treatment: >
        Hartman's piece is SECONDARY SYNTHESIS not new first-
        observation attribution. The TeamPCP attribution chain is
        corpus-anchored via finding-2026-05-12-FLASH-0001 (Mini
        Shai-Hulud Wiz/StepSecurity/Snyk originating attribution
        layer) and finding-2026-05-20-FLASH-0001 (TeamPCP self-
        claim on Breached relayed by BleepingComputer/SW/THN).
        Archimedes preserves Hartman's secondary-synthesis
        framing verbatim.
      requires_analyst_review: false

# Downstream handoff flags
analyst_review_required: false           # B3 cluster anchor; no novel attribution; corpus-anchored TTP-Map-Update class
red_team_review_required: false          # WEP ceiling "likely" not "very likely"; no red-team challenge required per CLAUDE.md threshold
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Lifecycle
tlp: CLEAR
published_in_briefs:
  - 2026-05-25-afternoon
retracted: false
retraction_brief_id: null
---

# TeamPCP Supply-Chain Campaign Consolidation Through 2026-05-24: Three Net-New Capability Layers Identified (Hartman/SANS ISC)

## Summary

Hartman / SANS ISC 2026-05-25 consolidates one calendar week of TeamPCP (corpus-tracked roster #001 HIGH) supply-chain campaign activity through 2026-05-24 and identifies three net-new capability layers not previously corpus-anchored: (1) a framework source-code public drop to GitHub on 2026-05-22 with "Love - TeamPCP" and "Change keys and C2 as needed" README strings and at least three forks deployed within hours including a FreeBSD variant; (2) durabletask Linux disk-wiper capability cited via corpus-anchored SafeDep 2026-05-20 primary but with disk-wiper-specific first-observation pending grader verification; (3) CISA explicitly did NOT add CVE-2026-45321 (Mini Shai-Hulud / OIDC credential abuse chain, VT-006) to the Known Exploited Vulnerabilities catalog as of the 2026-05-22 catalog release — independently verified this sweep against catalogVersion 2026.05.22. The Hartman piece is a secondary synthesis citing originating vendors (Microsoft, SafeDep, GitHub CISO Wales) for primary observations; the framework-leak claim cites unnamed vendor primaries and is the load-bearing net-new layer driving the cluster anchor digraph B3.

## Sources

### SANS Internet Storm Center diary 33016 (sans-isc, digraph: B)

- URL: https://isc.sans.edu/diary/rss/33016 (canonical) / https://isc.sans.edu/diary/rss/33014 (duplicate published 19 seconds earlier with identical title)
- Published: 2026-05-25T13:26:06Z (handler on duty: Didier Stevens)
- Byline: Kenneth Hartman
- Key claim: One-week TeamPCP consolidation timeline through 2026-05-24 with three net-new capability layers identified (framework leak; durabletask disk-wiper; CISA-not-on-KEV); preserves through-cite to originating vendor primaries on corpus-anchored carry-forward elements.

## Technical detail

### Hartman timeline (verbatim sequence)

| Date | Event |
|---|---|
| 2026-05-11 | TanStack credentials harvested (OIDC credential abuse chain origin) |
| 2026-05-18 | Nx Console trojanized extension published (18-min window before takedown) |
| 2026-05-19 | durabletask trojanized; @antv wave launched (639 malicious versions / 323 packages) |
| 2026-05-20 | Microsoft Security Blog response published |
| 2026-05-21 | GitHub CISO Alexis Wales public statement on Nx Console root cause |
| 2026-05-22 | Shai-Hulud framework source published to GitHub — "Love - TeamPCP" / "Change keys and C2 as needed" README strings; at least three forks within hours, including FreeBSD variant |
| 2026-05-24 | 3,800 GitHub repositories exfiltrated confirmed |

### Three net-new capability layers (cluster-anchor framing)

1. **Framework source-code public drop to GitHub (2026-05-22) — VENDOR-PRIMARY RETRIEVAL PENDING.** Hartman cites "documented by vendors" without naming the vendor primary. README strings preserved verbatim ("Love - TeamPCP" 3 words; "Change keys and C2 as needed" 6 words — both under Hard Rule 6 limit). First observed instance in Archimedes corpus of TeamPCP campaign-source-code public drop with explicit framework attribution. At least three forks deployed within hours including a FreeBSD variant — first observed instance of TeamPCP framework fork-customization in corpus. Campaign-commoditization signal: the README-string "Change keys and C2 as needed" is a fork-and-customize invitation.

2. **durabletask Linux disk-wiper capability — SAFEDEP FIRST-OBSERVATION VERIFICATION PENDING.** Hartman cites this — SafeDep 2026-05-20 primary already corpus-anchored. Verification of SafeDep first-observation language on the disk-wiper claim (vs. credential-stealer-only framing) is the grader/actor-profiler next-step action. If confirmed, this is a substantive TTP-map update on TeamPCP — destructive-category addition to predominantly credential-theft tradecraft, with threat-box recalibration implications for the actor profile.

3. **CISA explicitly did NOT add CVE-2026-45321 to KEV catalog as of 2026-05-22 catalog release — INDEPENDENTLY VERIFIED THIS SWEEP.** Catalog version 2026.05.22 dateReleased 2026-05-22T18:00:11.5035Z does NOT contain CVE-2026-45321. Hartman observation is factually correct per Archimedes independent KEV catalog probe. Most recent KEV add remains CVE-2026-9082 Drupal 2026-05-22 (T-2 federal deadline this Wednesday). Defender-context observation; corpus has flagged KEV-pending since VT-006 `_index.yaml` entry on 2026-05-12 (13-day delay now 14-day delay after 2026-05-22 catalog release without addition, materially atypical for CVSS-9.6 + GitHub-internal-compromise + Microsoft-SDK-trojanization scope).

### Operational details (Hartman roll-up; corpus-anchored unless flagged)

- **Persistence files:** `~/.claude/settings.json`, `.vscode/tasks.json`
- **C2/exfil endpoints:** `filev2[.]getsession[.]org`, `seed1[.]getsession[.]org` (Session messenger protocol) — corpus-anchored
- **Credential targets:** GitHub tokens, npm credentials, AWS keys, GCP/Azure tokens, SSH keys, Kubernetes service accounts, HashiCorp Vault secrets, Stripe API keys, password-manager vaults (1Password, Bitwarden)
- **Propagation:** AWS SSM (EC2), `kubectl exec` (Kubernetes), npm install execution
- **Distinctive artifacts:** PBKDF2 salt strings; reversed-string pattern `niagA oG eW ereH :duluH-iahS` (reverses to "Shai-Hulud: Here We Go Again"); ~499 KB obfuscated JavaScript payload

## IOCs surfaced

```yaml
iocs:
  domains:
    - value: "filev2.getsession.org"
      type: c2_domain
      defanged: "filev2[.]getsession[.]org"
      protocol: Session messenger
      corpus_anchor: finding-2026-05-12-FLASH-0001 + finding-2026-05-20-FLASH-0001
    - value: "seed1.getsession.org"
      type: c2_domain
      defanged: "seed1[.]getsession[.]org"
      protocol: Session messenger
      corpus_anchor: finding-2026-05-12-FLASH-0001

  cves:
    - id: CVE-2026-45321
      cvss: 9.6
      ghsa: GHSA-g7cv-rxg3-hmpx
      product: "OIDC credential abuse chain — Mini Shai-Hulud / TeamPCP"
      corpus_anchor: VT-006
      kev_status: "VERIFIED NOT ON KEV as of catalogVersion 2026.05.22 (2026-05-22T18:00:11Z); 14-day delay post-Nx-Console-publish 2026-05-18"

  framework_leak_artifacts_NOVEL:
    - artifact_type: github_readme_string
      value: "Love - TeamPCP"
      date: 2026-05-22
      vendor_primary_retrieval: pending
    - artifact_type: github_readme_string
      value: "Change keys and C2 as needed"
      date: 2026-05-22
      vendor_primary_retrieval: pending
    - artifact_type: fork_pattern
      value: "at least three forks deployed within hours including FreeBSD variant"
      date: 2026-05-22
      vendor_primary_retrieval: pending

  persistence_mechanisms:
    - value: "~/.claude/settings.json"
      class: persistence_file
      ecosystem: "Anthropic Claude Code config"
    - value: ".vscode/tasks.json"
      class: persistence_file
      ecosystem: "VS Code workspace config"

  named_downstream_victims_corpus_anchored:
    - "OpenAI"
    - "Grafana Labs"
    - "Mistral AI"
    - "GitHub (internal codebase, ~3,800 repos)"

  affected_packages_corpus_anchored:
    npm:
      - "nrwl.angular-console (Nx Console VS Code extension) v18.95.0 — 2.2M installs, 18-min window 2026-05-18"
      - "echarts-for-react (~1.1M weekly downloads)"
      - "size-sensor (~4.2M weekly downloads)"
      - "@antv ecosystem (639 malicious versions / 323 packages; compromised maintainer 'atool'; 2026-05-19)"
      - "timeago.js"
    pypi:
      - "durabletask v1.4.1/1.4.2/1.4.3 (officially Microsoft-published Azure Durable Functions SDK; ~417K monthly downloads; published 2026-05-19; yanked within hours; novel disk-wiper capability VENDOR-PRIMARY-PENDING)"

  monetization_channels_inactive_during_window:
    - "Vect"
    - "CipherForce"
```

## Relationship to existing findings

- **finding-2026-05-12-FLASH-0001** (Mini Shai-Hulud / VT-006 originating attribution; Wiz + StepSecurity + Snyk primary) — Hartman's consolidation carries forward the OIDC credential abuse chain attribution; corpus-anchored.
- **finding-2026-05-20-FLASH-0001** (TeamPCP self-claim on Breached + GitHub-corp internal repos compromise) — Hartman's consolidation carries forward the 3,800-repos figure; corpus-anchored.
- **finding-2026-05-25-0001** (Megalodon mass GitHub workflow_dispatch backdoor) — explicitly NOT clustered: SafeDep declined to attribute Megalodon to any tracked actor, and Hartman does not claim Megalodon = TeamPCP. Cross-corpus author-identity-spoofing pattern observation noted in finding-2026-05-25-0001 ("technique is portable post-access and does NOT distinguish actor identity").
- **VT-006 `_index.yaml`** (Mini Shai-Hulud CVE-2026-45321) — Hartman observation that CISA explicitly did not add this CVE to KEV as of 2026-05-22 catalog release is independently verified; defender-context KEV-watch observation.

## Open questions for analyst / actor-profiler

1. **Vendor-primary retrieval on framework-leak claim (most novel layer).** Hartman cites "documented by vendors" without naming vendor primary. If a named A-grade vendor primary (SafeDep, Socket, Wiz, Snyk, Aikido, StepSecurity, Microsoft MSTIC, Mandiant, Unit 42) substantiates the "Love - TeamPCP" / "Change keys and C2 as needed" README claim with reproducible GitHub repository identifier(s), regrade and consider FLASH Trigger 4 re-evaluation at next pre-brief.

2. **SafeDep first-observation language on durabletask Linux disk-wiper capability.** Hartman cites SafeDep 2026-05-20 primary — corpus-anchored on the surface inventory but disk-wiper claim has not been independently verified in Archimedes corpus prior to this Hartman consolidation. If SafeDep's 2026-05-20 primary post explicitly attests disk-wiper capability (vs. credential-stealer-only), this is a substantive destructive-category addition to TeamPCP's TTP map with threat-box recalibration implications for actor profile #001.

3. **CISA KEV catalog watch for CVE-2026-45321 addition.** VT-006 `_index.yaml` flags this as KEV-pending since 2026-05-12. The 14-day delay (now post-2026-05-22 catalog release without addition) is materially atypical for CVSS-9.6 + GitHub-internal-compromise + Microsoft-SDK-trojanization scope. Worth surfacing in the 16:00 PM brief as KEV-watch defender observation alongside the previously-tracked CVE-2026-9082 Drupal T-2 federal deadline (this Wednesday).

4. **Threat-box recalibration trigger condition for actor #001 TeamPCP.** If the durabletask Linux disk-wiper layer confirms vendor-primary, the TeamPCP threat-box scoring should be re-run with a destructive/disruptive category lift (current per-category at floor for destructive). Next /update-tracking on actor #001 should incorporate this raw-signal and any vendor-primary follow-on.

5. **Campaign-source-code commoditization signal.** If the framework-leak claim confirms, this is the first corpus instance of TeamPCP campaign-source-code public-drop with explicit framework attribution and fork-customization invitation. Defender-prioritization implication: TeamPCP TTPs may proliferate to non-TeamPCP operators via the fork ecosystem, expanding the attack surface beyond the originating actor.
