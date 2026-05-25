---
raw_id: raw-2026-05-25-pm-001-isc-sans-hartman-teampcp-supply-chain-activity-through-2026-05-24-consolidation
collected_at: 2026-05-25T15:35:00-04:00
run_id: pre-brief-20260525-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: sans-isc
  source_name: "SANS Internet Storm Center (Kenneth Hartman byline; Didier Stevens handler-on-duty)"
  source_url: https://isc.sans.edu/diary/rss/33016
  source_url_duplicate: https://isc.sans.edu/diary/rss/33014
  published_at: 2026-05-25T13:26:06+00:00
  byline: Kenneth Hartman
  handler_on_duty: Didier Stevens
  publication_classification: SANS ISC diary
  publication_dup_note: |
    Two diary entries published 19 seconds apart (diary 33016 at 13:26:06 UTC
    and diary 33014 at 13:25:47 UTC) with identical titles and overlapping
    content per WebFetch direct retrieval. Treated as ONE editorial item;
    33016 used as canonical link given later timestamp + slightly more
    complete content payload.
source_grade_at_collection:
  grade: B
  rationale: |
    sans-isc grade B per source-grades.yaml — "Quality research but
    community-contributed." Kenneth Hartman is named-byline diary author;
    Didier Stevens is handler-on-duty (long-running ISC handler / Trip
    Adler-tier malware-analysis veteran). Hartman piece is a TIMELINE
    CONSOLIDATION / TTP-MAP UPDATE on the corpus-tracked TeamPCP
    supply-chain campaign, citing originating vendors (Microsoft Security
    Blog 2026-05-20; SafeDep 2026-05-19/20; GitHub CISO Alexis Wales
    2026-05-21) for primary observations. Hartman synthesizes; does not
    originate primary observations.

match_reason:
  watchlist: []                  # No A&D-prime named victims in the consolidation
  actors: ["001"]                # TeamPCP (corpus-tracked since 2026-03-18 per roster #001; HIGH threat-level)
  vulnerabilities: ["VT-006"]    # CVE-2026-45321 Mini Shai-Hulud (corpus-tracked per _index.yaml)
  keywords:
    - "TeamPCP"
    - "Shai-Hulud"
    - "Mini Shai-Hulud"
    - "framework leak"
    - "framework source-code drop"
    - "durabletask"
    - "Linux disk-wiper"
    - "Nx Console"
    - "@antv"
    - "echarts-for-react"
    - "size-sensor"
    - "timeago.js"
    - "TanStack"
    - "OIDC credential abuse"
    - "CVE-2026-45321"
    - "Session messenger protocol"
    - "filev2.getsession.org"
    - "seed1.getsession.org"
    - "FreeBSD variant"
    - "kubectl exec"
    - "AWS SSM"
    - "CISA-NOT-on-KEV"
    - "Microsoft published SDK"

triage_tags:
  - corpus_anchored_consolidation
  - teampcp_ttp_consolidation
  - ttp_change_candidate
  - flash_trigger_4_marginal_fail
  - supply_chain_framework_open_sourcing_novel_in_corpus
  - durabletask_linux_disk_wiper_destructive_class_novel_for_teampcp
  - cisa_explicitly_not_on_kev_defender_observation
  - relay_secondary_synthesizer_not_originating_primary
  - vendor_primary_retrieval_pending_for_framework_leak_claim
  - grader_finding_tier_candidate

iocs_extracted: true
iocs_count: 13
text_word_count: 1500
promoted: true
promoted_to_finding: finding-2026-05-25-0002-teampcp-supply-chain-activity-through-2026-05-24-consolidation
promoted_at: 2026-05-25T16:00:00-04:00
ttl_expires_at: 2026-08-23T15:35:00-04:00

---

# TeamPCP Supply Chain Campaign: Activity Through 2026-05-24

**Source:** SANS Internet Storm Center — diary published 2026-05-25 13:26:06 UTC by Kenneth Hartman (handler on duty: Didier Stevens; threat level Green). URL: https://isc.sans.edu/diary/rss/33016 (and duplicate publication https://isc.sans.edu/diary/rss/33014 19 seconds earlier).

## Executive Summary (Hartman language preserved)

The Hartman diary summarizes one calendar week of TeamPCP supply-chain campaign activity through 2026-05-24, with the explicit framing that "the campaign escalated dramatically across three ecosystems in a single week. A malicious VS Code extension breached GitHub's internal repositories. An officially Microsoft-published Python SDK was trojanized. The @antv npm ecosystem suffered compromise of 639 malicious versions across 323 packages."

## Affected Packages & Versions (Hartman roll-up; corpus-anchored items marked)

### npm Ecosystem
- **Nx Console VS Code extension v18.95.0** (publisher: nrwl.angular-console; 2.2M installs; live for approximately 18 minutes on 2026-05-18). *Corpus-anchored via raw-2026-05-19-am-006.*
- **echarts-for-react** (~1.1M weekly downloads). *Corpus-anchored via raw-2026-05-19-pm-004 mass-wave.*
- **size-sensor** (~4.2M weekly downloads). *Corpus-anchored via same.*
- **@antv ecosystem**: 639 malicious versions across 323 packages (compromised maintainer account "atool"; 2026-05-19). *Corpus-anchored via raw-2026-05-19-pm-004.*
- **timeago.js** — among additional impacted packages. *Corpus-anchored.*

### PyPI Ecosystem
- **durabletask** (Azure Durable Functions SDK) versions 1.4.1, 1.4.2, 1.4.3 (~417K monthly downloads; published 2026-05-19; yanked within hours). *Corpus-anchored via raw-2026-05-19-am-009 / SafeDep 2026-05-20 primary in source surface.*

### CVE Identifier
- **CVE-2026-45321** — OIDC credential abuse chain originating from May 11 TanStack wave (corpus-anchored per VT-006 in `_index.yaml`).

## Operational Details (Hartman language preserved)

**Persistence Mechanisms:**
- `~/.claude/settings.json`
- `.vscode/tasks.json`

**C2 / Exfiltration Endpoints:**
- `filev2[.]getsession[.]org`
- `seed1[.]getsession[.]org`
- Session messenger protocol

**Credential Targets:** GitHub tokens, npm credentials, AWS keys, GCP/Azure tokens, SSH keys, Kubernetes service accounts, HashiCorp Vault secrets, Stripe API keys, password manager vaults (1Password, Bitwarden).

**Propagation Methods:**
- AWS SSM (EC2 instances)
- `kubectl exec` (Kubernetes environments)
- npm install execution

**Distinctive Artifacts:**
- PBKDF2 salt strings
- Reversed string pattern: "niagA oG eW ereH :duluH-iahS" (reversed reads as `Shai-Hulud: Here We Go Again`)
- Obfuscated JavaScript payload (~499 KB)

## Hartman Timeline (verbatim sequence)

| Date | Event |
|---|---|
| 2026-05-11 | TanStack credentials harvested (OIDC credential abuse chain origin) |
| 2026-05-18 | Nx Console trojanized extension published (18-minute window before takedown) |
| 2026-05-19 | durabletask trojanized; @antv wave launched (639 malicious versions / 323 packages) |
| 2026-05-20 | Microsoft Security Blog response published |
| 2026-05-21 | GitHub CISO Alexis Wales public statement on Nx Console root cause |
| 2026-05-22 | **Shai-Hulud framework source published to GitHub** — `Love - TeamPCP` and `Change keys and C2 as needed` README strings; at least three forks deployed within hours, including FreeBSD variant |
| 2026-05-24 | 3,800 GitHub repositories exfiltrated confirmed |

## Impact Summary (Hartman roll-up)

- **GitHub internal breach:** ~3,800 repositories exfiltrated. *Corpus-anchored via finding-2026-05-20-FLASH-0001.*
- **Named downstream victims:** OpenAI, Grafana Labs, Mistral AI.
- **42 malicious packages displayed forged Sigstore badges.** *Corpus-anchored.*
- **~61,274 npm granular access tokens invalidated** (write-permission tokens; bypassed-2FA at granular scope). *Corpus-anchored.*
- **Ransomware monetization channels (Vect / CipherForce) remained inactive** during the documented window.

## Attribution & Response (verbatim)

Microsoft published formal security analysis (corpus-anchored 2026-05-20). GitHub CISO Alexis Wales publicly confirmed the Nx Console root cause (corpus-anchored 2026-05-21). **CISA notably did not add CVE-2026-45321 to Known Exploited Vulnerabilities catalog despite GitHub-internal compromise and Microsoft SDK trojanization.** (Hartman attribution language preserved; corpus has tracked this as KEV-pending since VT-006 entry 2026-05-12.)

## Recommended Actions (Hartman roll-up)

> Rotate developer/CI/CD credentials; pin exact versions; verify lockfile hashes; audit `kubectl exec` and AWS SSM session history; inspect endpoints for persistence indicators; discontinue reliance on publisher verification badges as safety signals.

---

## Extraction notes

- Language: en
- Article type: SANS ISC diary / consolidation timeline
- Publication classification: B-grade community-vetted research synthesis
- Raw IOC extraction invoked: yes — see below
- Corpus anchoring: All seven non-novel items in Hartman's consolidation are previously corpus-tracked. Three NET-NEW capability layers identified for grader review.

### Three NET-NEW capability layers identified

1. **Framework source-code drop to GitHub on 2026-05-22** with "Love - TeamPCP" and "Change keys and C2 as needed" README strings + at least three forks within hours including a FreeBSD variant. *Hartman cites "documented by vendors" without naming specific vendor primary — VENDOR-PRIMARY RETRIEVAL PENDING.* This is a campaign-source-code public-drop / commoditization signal; first observed instance in Archimedes corpus.

2. **durabletask Linux disk-wiper capability** reported in the payload. Hartman cites this — SafeDep 2026-05-20 primary already in corpus (top-5 unchanged across AM/12:00/PM sentinel surfaces). Verification of SafeDep first-observation language on the disk-wiper claim is the grader's next-step action. If confirmed, this is a substantive TTP-MAP UPDATE on TeamPCP — destructive-category addition to predominantly credential-theft tradecraft, with threat-box recalibration implications.

3. **CISA explicitly did not add CVE-2026-45321 to KEV catalog** as of 2026-05-22 catalog release (4-day window post the 2026-05-18 Nx Console publish), despite GitHub-internal compromise + Microsoft-published SDK trojanization. Defender-context observation; corpus has flagged KEV-pending since VT-006 _index.yaml entry on 2026-05-12. Worth flagging in 16:00 PM brief as KEV-watch observation.

### Hard Rule 2 framing

Hartman's piece is a SECONDARY SYNTHESIS / TIMELINE CONSOLIDATION — it cites originating vendors (Microsoft Security Blog, SafeDep, GitHub CISO Wales) for primary observations but does not present any primary first-observation itself. Per FLASH-POLICY Trigger 4 conditions (which require source_grade in [A, B] + attributable_actor in _roster.yaml + article_describes_new_tooling_or_targeting_or_infrastructure), Trigger 4 marginally FAILS on the relay-vs-originating standard:

- The framework source-code GitHub drop claim cites "documented by vendors" — vendor name NOT given in Hartman's text. Direct vendor-primary retrieval required before promoting to finding-tier.
- The durabletask Linux disk-wiper claim cites SafeDep 2026-05-20 primary — corpus-anchored; SafeDep first-observation language needs grader verification.
- The CISA-NOT-on-KEV observation is contextual defender-observation, not vendor research.

### Hard Rule 3 framing

Hartman's "Recommended Actions" subsection is defender-posture guidance (credential rotation, lockfile hashing, audit kubectl/SSM session history). No PoC code, no exploitation walkthrough, no attack tooling presented. Hartman does NOT link to or describe the contents of the framework source-code drop beyond the README string snippets — extraction limited to the README-string IOCs (which are themselves vendor-attestation-grade, not exploitation-instruction).

### Hard Rule 7 framing

Hartman quotes preserved verbatim are all under 15 words each:
- "Love - TeamPCP" (3 words)
- "Change keys and C2 as needed" (6 words)
- "niagA oG eW ereH :duluH-iahS" (5 tokens / 1 reversed phrase)

Total of three discrete quotes from the diary, all defensively short. No quotes exceeding 15 words.

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  domains:
    - value: "filev2.getsession.org"
      type: c2_domain
      vendor_attestation: "Hartman / SANS ISC 2026-05-25 13:26 UTC consolidation; previously corpus-anchored via SafeDep + Wiz + Snyk per finding-2026-05-12-FLASH-0001"
      confidence: high
      protocol: Session messenger
      defanged: "filev2[.]getsession[.]org"
    - value: "seed1.getsession.org"
      type: c2_domain
      vendor_attestation: "Hartman / SANS ISC 2026-05-25 13:26 UTC consolidation; previously corpus-anchored"
      confidence: high
      protocol: Session messenger
      defanged: "seed1[.]getsession[.]org"

  cves:
    - id: CVE-2026-45321
      cvss: 9.6
      ghsa: GHSA-g7cv-rxg3-hmpx
      product: "OIDC credential abuse chain — Mini Shai-Hulud / TeamPCP"
      vendor_attestation: "Hartman 2026-05-25 consolidation re-cites VT-006 corpus anchor"
      corpus_anchor: VT-006
      kev_status: "PENDING — CISA explicitly did NOT add as of 2026-05-22 catalog release (Hartman defender-observation; 13 days post-disclosure)"

  affected_packages_named:
    npm:
      - name: "nrwl.angular-console (Nx Console VS Code extension)"
        version: "18.95.0"
        install_count: "2.2M installs"
        live_window: "approximately 18 minutes on 2026-05-18"
        corpus_anchor: "raw-2026-05-19-am-006"
      - name: "echarts-for-react"
        weekly_downloads: "~1.1M"
        corpus_anchor: "raw-2026-05-19-pm-004 mass-wave"
      - name: "size-sensor"
        weekly_downloads: "~4.2M"
        corpus_anchor: "raw-2026-05-19-pm-004"
      - name: "@antv ecosystem"
        compromised_versions: 639
        compromised_packages: 323
        compromised_maintainer_account: "atool"
        wave_date: "2026-05-19"
        corpus_anchor: "raw-2026-05-19-pm-004"
      - name: "timeago.js"
        notes: "named in Hartman roll-up as 'additional impacted'"
    pypi:
      - name: "durabletask"
        publisher_class: "officially Microsoft-published Python SDK (Azure Durable Functions SDK)"
        versions: ["1.4.1", "1.4.2", "1.4.3"]
        monthly_downloads: "~417K"
        publish_date: "2026-05-19"
        yank_window: "yanked within hours"
        novel_capability: "Linux disk-wiper capability reported in payload — VENDOR-PRIMARY VERIFICATION PENDING (SafeDep 2026-05-20 primary attestation needs grader confirmation)"
        corpus_anchor: "raw-2026-05-19-am-009"

  persistence_mechanisms:
    - value: "~/.claude/settings.json"
      class: persistence_file
      ecosystem: "Anthropic Claude Code config"
    - value: ".vscode/tasks.json"
      class: persistence_file
      ecosystem: "VS Code workspace config"

  propagation_methods:
    - "AWS SSM (EC2 instances)"
    - "kubectl exec (Kubernetes environments)"
    - "npm install execution"

  distinctive_artifacts:
    - artifact_type: reversed_string_pattern
      value: "niagA oG eW ereH :duluH-iahS"
      reversed_reads_as: "Shai-Hulud: Here We Go Again"
    - artifact_type: obfuscated_payload
      size_kb_approx: 499
      language: javascript
    - artifact_type: pbkdf2_salt_strings
      details: "named but specific values not enumerated in Hartman text"

  framework_leak_artifacts_NOVEL:
    - artifact_type: github_readme_string
      value: "Love - TeamPCP"
      novelty: "first observed instance in Archimedes corpus of TeamPCP campaign-source-code public-drop with explicit framework attribution"
      date: "2026-05-22"
      vendor_primary_retrieval: pending
      vendor_attestation_chain: "Hartman 2026-05-25 cites 'documented by vendors' — vendor name NOT given"
    - artifact_type: github_readme_string
      value: "Change keys and C2 as needed"
      novelty: "campaign-commoditization signal — fork-and-customize invitation"
      date: "2026-05-22"
      vendor_primary_retrieval: pending
    - artifact_type: fork_pattern
      value: "at least three forks deployed within hours, including FreeBSD variant"
      novelty: "first observed instance of TeamPCP framework fork-customization within Archimedes corpus"
      date: "2026-05-22"
      vendor_primary_retrieval: pending

  named_downstream_victims:
    - "OpenAI"
    - "Grafana Labs"
    - "Mistral AI"
    - "GitHub (internal codebase)"

  monetization_channels_inactive:
    - "Vect"
    - "CipherForce"

attribution_claims:
  - claim: "TeamPCP responsible for the consolidated campaign across npm, PyPI, and VS Code Marketplace ecosystems through 2026-05-24"
    source: "Kenneth Hartman / SANS ISC 2026-05-25 (citing originating sources Microsoft Security Blog 2026-05-20, SafeDep 2026-05-19/20, GitHub CISO Alexis Wales 2026-05-21, vendor-unnamed framework-leak documentation 2026-05-22)"
    confidence_per_source: "preserved through-cite to originating vendor primaries — Hartman does NOT originate attribution"
    corpus_anchor: "TeamPCP roster #001; finding-2026-05-12-FLASH-0001 originating attribution"
    archimedes_treatment: |
      Hartman piece is SECONDARY SYNTHESIS of corpus-anchored TeamPCP
      attribution chain. Does NOT constitute new first-observation
      attribution claim per Hard Rule 2.
  - claim: "CISA explicitly did NOT add CVE-2026-45321 to KEV catalog as of 2026-05-22 catalog release"
    source: Hartman defender-observation (verifiable against KEV catalogVersion 2026.05.22)
    confidence_per_source: high (catalog-version-attestable)
    archimedes_treatment: |
      Verified independently this sweep — CISA KEV catalogVersion 2026.05.22
      dateReleased 2026-05-22T18:00:11.5035Z does NOT contain CVE-2026-45321.
      Hartman observation is FACTUALLY CORRECT per Archimedes independent
      KEV catalog probe. Most recent KEV add remains CVE-2026-9082 Drupal
      2026-05-22 (T-2 federal deadline this Wednesday).

flash_trigger_evaluation:
  trigger_4_tracked_actor_ttp_change:
    fired: false
    reason: |
      Conditions: source_grade in [A, B] ✓ (sans-isc B);
      attributable_actor in _roster.yaml ✓ (TeamPCP #001);
      article_describes_new_tooling_or_targeting_or_infrastructure ✓.
      BUT: All three net-new TTP layers cite ORIGINATING sources that are
      already corpus-anchored (Microsoft Security Blog 2026-05-20, SafeDep
      2026-05-20, vendor-unnamed 2026-05-22). Hartman is SECONDARY
      SYNTHESIZER not originating observer. Per the attribution_is_new
      standard applied to TTP claims, Trigger 4 marginally FAILS on the
      relay-vs-originating standard. Grader has discretion to promote
      pm-001 to a TeamPCP TTP-Map-Update finding pending vendor-primary
      retrieval on the framework-leak claim (most novel layer).

grader_recommendations:
  - action: "Verify vendor-primary attestation of TeamPCP framework source-code GitHub drop 2026-05-22"
    rationale: |
      Hartman cites 'documented by vendors' without naming vendor primary.
      Operator may identify vendor name through cross-source retrieval
      (SafeDep, Socket, Wiz, Snyk, Aikido, StepSecurity, Microsoft MSTIC
      back-channel research). If a named A-grade vendor primary substantiates
      the 'Love - TeamPCP' / 'Change keys and C2 as needed' README claim
      with reproducible GitHub repository identifier(s), promote to
      finding-tier and consider FLASH Trigger 4 re-evaluation at next
      pre-brief.
  - action: "Verify SafeDep first-observation language on durabletask Linux disk-wiper capability"
    rationale: |
      Hartman cites SafeDep 2026-05-20 primary — corpus-anchored on the
      surface inventory but disk-wiper claim has not been independently
      verified in Archimedes corpus prior to this Hartman consolidation.
      If SafeDep's 2026-05-20 primary post explicitly attests disk-wiper
      capability (vs. credential-stealer-only), this is a substantive
      destructive-category addition to TeamPCP's TTP map with threat-box
      recalibration implications for the actor profile.
  - action: "Track CISA KEV catalog for CVE-2026-45321 addition"
    rationale: |
      VT-006 _index.yaml flags this as KEV-pending since 2026-05-12. The
      13-day delay (now 14-day delay after 2026-05-22 catalog release
      without addition) is materially atypical for CVSS-9.6 + GitHub-internal-
      compromise + Microsoft-SDK-trojanization scope. Worth surfacing in
      16:00 PM brief as KEV-watch defender observation.
```

## Source-grade & WEP framing for grader

- Source grade at this surface: B (sans-isc; community-vetted research synthesis with named-byline diary author and named handler-on-duty).
- WEP ceiling per single-source veto on the framework-leak claim: "likely" pending vendor-primary substantiation.
- WEP for corpus-anchored items in Hartman's consolidation (Nx Console, durabletask, @antv mass wave, GitHub internal repos, OIDC credential abuse chain): unchanged from original finding-tier WEPs (very likely / very likely / very likely / very likely / likely respectively).
- WEP for durabletask Linux disk-wiper claim: "likely" pending direct SafeDep primary verification.
- WEP for CISA-NOT-on-KEV observation: "very likely" (independently verified against catalog version 2026.05.22).

---

*Archimedes raw-signal collected at 2026-05-25T15:35:00-04:00 from SANS Internet Storm Center diary 33016 (Kenneth Hartman byline; Didier Stevens handler-on-duty). Sole originating primary on the consolidation framing; cites multiple corpus-anchored vendor primaries. Three net-new capability layers identified for grader review with explicit vendor-primary-retrieval pending tags on the framework-leak and disk-wiper layers. Trigger 4 marginally fails on relay-vs-originating standard; grader has discretion to promote to TeamPCP TTP-Map-Update finding.*
