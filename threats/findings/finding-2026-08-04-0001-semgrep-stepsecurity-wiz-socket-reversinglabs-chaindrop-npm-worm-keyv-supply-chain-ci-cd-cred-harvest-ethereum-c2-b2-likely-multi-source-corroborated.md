---
finding_id: finding-2026-08-04-0001
created_at: 2026-08-04T14:10:00-04:00
graded_by: orchestrator                 # on-demand /investigate; grader subagent not separately invoked this cycle
grading_run_id: ondemand-investigate-20260804-140000
grading_mode: on_demand
finding_type: net_new                    # first Archimedes finding for the ChainDrop npm worm

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: "Semgrep (named the campaign) + StepSecurity + Wiz Research + Socket + ReversingLabs + SafeDep; The Hacker News relay"
  source_yaml_id: semgrep
  co_primary_source_yaml_ids: [stepsecurity, wiz-research, socket, safedep]
  co_primary_not_in_source_grades: [reversinglabs]     # B-class supply-chain research vendor; not yet in source-grades.yaml (flag for librarian)
  highest_grade_corroborator:
    source_name: "Wiz Research (observed the Bun/1.3.13 user-agent on malicious calls)"
    grade: A                             # wiz-research is provisional A in source-grades.yaml
    in_hand_this_cycle: false            # retrieved via WebSearch summary; direct fetch 403'd
  grade_rationale: >
    Multiple reputable supply-chain-security vendors independently report the SAME campaign, each contributing
    a distinct observation of directly-observable artifacts: Semgrep counted the registry spread and named it
    "ChainDrop"; Wiz (A) flagged the Bun/1.3.13 user-agent; Socket and ReversingLabs independently analysed the
    on-chain Ethereum C2 contract; SafeDep produced an independent (higher) version count. This is genuine
    publisher- AND telemetry-independent corroboration, not one report relayed by many outlets. Anchored at B
    (not A) for ONE reason only: every direct primary fetch returned HTTP 403 this cycle, so all content was
    captured through the WebSearch summarizer's paraphrase — evidentiary quality is relay-equivalent, not
    direct-primary. Wiz's A grade and the multi-vendor independence would support B/A on direct retrieval.
  provisional: false
  retrieval_caveat: >
    Direct WebFetch of Semgrep, StepSecurity, Wiz, and The Hacker News all returned HTTP 403. No primary was
    read in full this cycle. Grade reflects that haircut.
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent            # consistent with the established 2026 npm-worm class (Shai-Hulud / Miasma / node-gyp / Mini-Shai-Hulud lineage): preinstall-hook execution, npm-token-fuelled self-propagation, CI/CD credential harvest
    - probably_true_no_contradicting_ab        # no A/B-grade source contradicts; vendors agree on mechanism and patient-zero
    - probably_true_claims_coherent            # keyv@6.0.0 patient zero, preinstall-hook execution, Bun second stage, Ethereum-contract C2 → npm-cache[.]com are internally coherent and mutually consistent across vendors
  grade_1_withheld_reason: >
    Grade 1 (Confirmed) withheld on two counts: (a) NO primary was directly retrieved this cycle (all 403'd) —
    the corroboration, though genuinely multi-vendor, reached Archimedes only via search summaries; and (b) the
    quantitative claims still diverge (Semgrep 1,557 versions / 435 packages vs SafeDep 1,684 / 420) as expected
    of a same-day fast-moving event. The existence and mechanism of the campaign are near-confirmed, but
    Archimedes has not itself verified a single artifact (no first-party telemetry available this session), so
    the grade is held at 2 pending direct primary retrieval and/or a first-party observation.
  rationale: >
    The graded claim: a self-propagating npm worm (vendor name "ChainDrop") compromised ~435 packages / ~1,557
    versions on 2026-08-04 by hijacking maintainer/npm-token credentials, executes at install via a preinstall
    hook that loads a Bun-based second-stage credential harvester (targeting npm/CI/cloud/SSH secrets), and
    resolves C2 from an Ethereum-mainnet smart contract. Coherent, consistent with the documented 2026 npm-worm
    pattern, corroborated across independent vendors, no contradiction → Probably True.
corroboration:
  independent_sources:
    - semgrep
    - stepsecurity
    - wiz-research
    - socket
    - reversinglabs
    - safedep
  independent: true
  test_result: >
    PASSES independence. Unlike a single vendor report relayed by many outlets, here distinct vendors each
    contribute an independent observation of a directly-observable artifact set (npm registry state; the
    on-chain C2 contract; the Bun user-agent in request telemetry). Semgrep, Socket, ReversingLabs, Wiz, and
    SafeDep are separate research organisations with separate telemetry. The independence is genuine; the only
    limitation is Archimedes' own indirect (search-summary) retrieval this cycle.
first_party_precedence:
  applied: false
  queried_indices: []                    # NONE queried this cycle
  query_window: "n/a"
  splunk_evidence: >
    First-party check NOT run. The splunk-query, virustotal, and urlscan MCP servers did not connect this
    session, so neither the archimedes/defenseclaw_local indices nor external IOC enrichment could be queried.
    This is a TOOLING-UNAVAILABLE gap, distinct from a visibility-bounded null — no inference (neither
    corroboration nor disconfirmation) may be drawn from its absence. REQUIRED follow-up when tooling
    reconnects: /ioc-hunt npm-cache[.]com; Splunk search for user-agent "Bun/1.3.13" from build/CI hosts and
    for npm preinstall-triggered child processes; check package telemetry for the named scopes.
single_source_veto_applied: false
single_source_veto_note: >
  Does NOT apply — genuine multi-vendor independent corroboration on directly-observable artifacts. WEP is
  therefore not veto-capped. It is instead held at "likely" by the retrieval limitation (no direct primary,
  no first-party observation this cycle), not by a single-source condition.
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "Self-propagating npm worm ('ChainDrop', per Semgrep) breaks out 2026-08-04: hijacked maintainer/npm-token credentials republish ~435 legitimate packages / ~1,557 poisoned versions (SafeDep: 1,684 / 420 / 9 orgs) in a ~2h burst (09:40-11:44 UTC), starting from keyv@6.0.0 (09:35Z). Poisoned tarballs add obfuscated loaders (setup.mjs, math_init.js) to the npm preinstall hook → execute at install → pull the Bun runtime → run a second-stage credential harvester (npm tokens, GitHub Actions secrets, AWS/Vault/Kubernetes creds, SSH keys, CI secrets) and plant Claude Code + VS Code hooks; harvested npm tokens fuel the next propagation wave. C2 resolved from an Ethereum-mainnet smart contract (later returning npm-cache[.]com)."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-08-04-ondemand-001
  attribution_claims: []                 # NONE — no source names an actor; Hard Rule 2, none originated
  no_attribution_note: >
    No vendor attributes ChainDrop to a named threat actor as of this finding. Tradecraft overlaps the broader
    2026 npm-worm ecosystem (Shai-Hulud, Miasma, node-gyp/binding.gyp, Mini-Shai-Hulud/TeamPCP) but no source
    asserts a shared operator. Archimedes originates no attribution (Hard Rule 2).

# FLASH-adjacency adjudication
flash_adjacency:
  independently_warrants_flash: false
  rationale: >
    Active and fast-moving, but fails the CVSS-10-active-exploitation-plus-tracked-actor-plus-A&D-watchlist-hit
    wake condition: no CVE (access is via credential/token hijack, not a software vulnerability), no tracked
    actor, and no named A&D/DIB victim. High-priority supply-chain-awareness item for the daily board, not a
    quiet-hours-bypass FLASH. (Operator elected the formal-finding path only; FLASH not drafted.)

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_action
    - weekly_synthesis
    - threat_detection_weekly            # install-time detection content (preinstall hook, Bun UA, npm-cache[.]com)

# Downstream handoff flags
analyst_review_required: true            # structural A&D-relevance inference + retrieval caveat warrant KAC
analyst_review_complete: true
analyst_review_run_id: analyst-ondemand-20260804-141000
red_team_review_required: false
red_team_review: >
  Not required. The high-confidence element of this finding is a DIRECTLY-OBSERVABLE factual event (poisoned
  package versions on the npm registry; a C2 contract on the Ethereum mainnet) attested by multiple independent
  vendors — not a contested analytic assessment or attribution. There is no attribution to challenge (none was
  made) and no >=2-actor competition to adjudicate. The only genuinely analytic claim — A&D relevance — is
  explicitly rated structural / low-confidence and carries no high-confidence assessment for a red team to
  attack. WEP is held at "likely," below the "very likely" red-team trigger, principally by Archimedes' own
  indirect retrieval this cycle.
analysis_sections:
  sat_ach:
    status: not_applied
    reason: no_attribution_no_multi_actor_competition
    detail: >
      ACH not warranted. No source attributes ChainDrop to any actor, so there is no set of competing actor
      hypotheses to score. Constructing rival-attribution hypotheses would risk originating attribution beyond
      the cited sources (Hard Rule 2). The live analytic questions concern ASSUMPTIONS (retrieval quality, the
      A&D-relevance chain, the still-moving scale numbers), which KAC handles.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "A self-propagating npm worm ('ChainDrop') compromised ~435 packages / ~1,557 versions on 2026-08-04 via
        credential/token hijack, executing a Bun-based CI/CD credential harvester at install via a preinstall
        hook and using an Ethereum-contract C2 — relevant to A&D via the software supply chain."
      analyzed_at: 2026-08-04T14:10:00-04:00
      analyzed_by: orchestrator
      invoking_context: "On-demand /investigate pre-publication review of the supply-chain event and its A&D-relevance chain"
      assumptions:
        - id: A1
          statement: "The multi-vendor reporting reliably establishes the campaign's existence and mechanism"
          category: source_reliability
          stated: true
          why_must_be_true: "The whole finding rests on the campaign being real and working as described"
          when_could_be_false: "All primaries were retrieved only via search summaries (403s); a summarizer distortion or an early-report error could be propagating"
          evidence_for: [raw-2026-08-04-ondemand-001]     # 6+ independent vendors on directly-observable artifacts
          evidence_against: []
          confidence: high         # genuine multi-vendor independence on observable artifacts
          centrality: critical
          classification: qualify  # qualify only for the indirect-retrieval caveat, not for doubt about the event
        - id: A2
          statement: "The quantitative scale (~435 packages / ~1,557 versions) is approximately correct"
          category: source_reliability
          stated: true
          why_must_be_true: "Scale drives the urgency framing"
          when_could_be_false: "Counts still diverge (Semgrep 1,557 vs SafeDep 1,684) and will move as vendors reconcile"
          evidence_for: [raw-2026-08-04-ondemand-001]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify  # present as a floor, expect revision
        - id: A3
          statement: "The install-time credential harvest would plausibly reach a Tier-1 A&D software development lifecycle / CI-CD"
          category: capability
          stated: false
          why_must_be_true: "Underpins the A&D-relevance framing"
          when_could_be_false: "A&D SDLCs pin/vendor dependencies, use private registries or install-script blocking, or don't transitively consume the affected scopes; malicious versions caught before promotion"
          evidence_for: [raw-2026-08-04-ondemand-001]     # broadly-depended packages (keyv/cacheable) make transitive exposure plausible
          evidence_against: []
          confidence: low          # structural/plausible, NOT observed; no A&D victim named
          centrality: material
          classification: qualify
        - id: A4
          statement: "The access vector is credential/token hijack (not a software-vulnerability exploit)"
          category: TTP_patterns
          stated: true
          why_must_be_true: "Shapes defensive posture (identity/publish-rights + install-script hardening, not patching)"
          when_could_be_false: "A yet-unreported initial-compromise vector (e.g. a phished maintainer or a leaked CI secret) turns out to be a specific exploit"
          evidence_for: [raw-2026-08-04-ondemand-001]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
        - id: A5
          statement: "First-party Splunk / IOC enrichment is simply unavailable this cycle (not silently negative)"
          category: visibility
          stated: true
          why_must_be_true: "Prevents mis-reading a missing first-party check as reassurance"
          when_could_be_false: "n/a — the MCP servers demonstrably did not connect"
          evidence_for: [tooling-unavailable-this-session]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound     # correctly NOT applied as precedence; flagged for follow-up
      classifications_summary:
        sound: 2
        qualify: 3
        test: 0
        reject: 0
      remediation:
        status: proceed
        qualifying_caveats:
          - "No primary was directly retrieved this cycle (all 403'd) and no first-party observation was possible (splunk/VT/urlscan MCPs offline). Corroboration is genuinely multi-vendor but reached Archimedes only via search summaries — grade held at B2 / 'likely' accordingly."
          - "Scale numbers still diverge (1,557 vs 1,684) — present as a floor, expect upward revision."
          - "A&D relevance is STRUCTURAL / indirect: no DIB victim named. The risk is the supply-chain + CI/CD-credential-theft vector reaching a supplier SDLC transitively, not an observed A&D compromise."
          - "No attribution exists; none originated (Hard Rule 2)."
        blocking_assumption: null
        blocking_detail: "No Test-class assumptions. Publication proceeds at WEP 'likely' with the caveats above."
      recommended_wep_after_test:
        if_primary_directly_retrieved_and_consistent: very_likely     # direct primary + sustained multi-vendor agreement would lift toward very_likely / credibility 1
        if_first_party_telemetry_corroborates: very_likely            # a Splunk/VT/urlscan hit on any IOC would independently corroborate → candidate credibility 1
        if_reporting_materially_revised_down: likely                  # keep at likely if counts/mechanism are walked back

# vuln-tracker handoff
vuln_tracker_handoff:
  action: none
  note: "No CVE. Access is credential/token hijack, not software-vulnerability exploitation. No vuln-tracker entry warranted."

# actor-profiler handoff
actor_profiler_handoff:
  roster_actor: null
  recommended_action: none
  note: >
    No attribution in any source; no roster mapping. Track ChainDrop as a supply-chain campaign/IOC set, not an
    actor dossier, unless a future A-grade source names an operator (Hard Rule 2).

# Lifecycle
tlp: CLEAR
published_in_briefs: []
retracted: false
retraction_brief_id: null
---

# ChainDrop: self-propagating npm worm poisons ~435 packages via credential hijack, harvests CI/CD secrets, uses an Ethereum-contract C2 (2026-08-04)

## Summary

A self-propagating npm worm that security vendors are calling **ChainDrop** (Semgrep's name) broke out the morning of **2026-08-04**. Beginning with `keyv@6.0.0` (published 09:35:00Z), it hijacked maintainer/npm-token credentials to republish legitimate packages as poisoned versions — **~435 packages / ~1,557 versions in a ~2-hour burst** (09:40–11:44 UTC) per Semgrep; **1,684 versions / 420 names / 9 orgs** per SafeDep's higher count. Poisoned tarballs add obfuscated loaders (`setup.mjs`, `math_init.js`) wired into the npm **`preinstall`** lifecycle hook, so the code runs during `npm install` / dependency resolution — the package never has to be imported. The loader pulls the **Bun** runtime and executes a second-stage **credential harvester** targeting npm tokens, GitHub Actions secrets, cloud credentials (AWS IMDS/ECS, HashiCorp Vault, Kubernetes), SSH private keys, and CI secrets; harvested npm tokens fuel the next propagation wave. Command-and-control is resolved from an **Ethereum-mainnet smart contract** (a "dead-drop" that lets operators repoint infrastructure without a hardcoded domain; the on-chain config later returned `npm-cache[.]com`). Graded **B2** and held at **"likely"** — corroboration is genuinely multi-vendor and independent, but every primary fetch returned HTTP 403 this cycle and no first-party observation was possible, so Archimedes verified nothing directly.

## Grade rationale

- **Source B** — genuine, telemetry-independent corroboration across Semgrep (named it), StepSecurity, Wiz Research (A; observed the `Bun/1.3.13` user-agent), Socket and ReversingLabs (both independently analysed the on-chain C2 contract), and SafeDep (independent higher count). Anchored at B rather than A for one reason only: every direct primary fetch 403'd, so all content arrived via the WebSearch summarizer — relay-equivalent, not direct-primary.
- **Credibility 2** — coherent and consistent with the documented 2026 npm-worm class; no A/B contradiction. Held below 1 (Confirmed) because no primary was directly read this cycle, no first-party artifact was verified, and the scale counts still diverge (1,557 vs 1,684).
- **Single-source veto NOT applied** — this is real multi-vendor independence, not one report relayed by many outlets. WEP is capped at "likely" by Archimedes' indirect retrieval, not by a single-source condition.

## Sources

### Semgrep — named the campaign "ChainDrop" (semgrep, digraph: B, provisional)

- URL: https://semgrep.dev/blog/2026/its-not-npm-ver-yet-npm-worm-chaindrop-hits-400-packages-including-jaredwray-servicetitan-ornikar-qlik-and-nebulajs/
- Published: 2026-08-04 · Retrieval: **search summary only (direct fetch HTTP 403)**
- Key claim: worm-like republishing of legitimate packages under hijacked credentials — 435 packages / 1,557 versions in ~2h; patient zero `keyv@6.0.0` at 09:35Z.

### StepSecurity — "Bun-loaded CI/CD credential harvester with Ethereum dead-drop C2" (stepsecurity, digraph: B, provisional)

- URL: https://www.stepsecurity.io/blog/chaindrop-npm-worm
- Published: 2026-08-04 · Retrieval: **search summary only (HTTP 403)**
- Key claim: `preinstall` hook → Bun runtime → second-stage harvester; targets npm/GitHub Actions/AWS/Vault/Kubernetes/SSH/CI secrets; Ethereum dead-drop C2.

### Wiz Research — keyv/cacheable supply-chain attack (wiz-research, digraph: A, provisional)

- URL: https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack
- Published: 2026-08-04 · Retrieval: **search summary only (HTTP 403)**
- Key claim: identified user-agent `Bun/1.3.13` on malicious calls; keyv and cacheable among hijacked packages.

### Socket — "Massive npm Malware Campaign Leverages Ethereum Smart Contracts" (socket, digraph: B, provisional)

- URL: https://socket.dev/blog/massive-npm-malware-campaign-leverages-ethereum-smart-contracts
- Published: 2026-08-04 · Retrieval: **search summary only**
- Key claim: C2 resolution via an Ethereum smart contract; on-chain config initially listed 3 domains, later reduced to `npm-cache[.]com`.

### ReversingLabs — "Ethereum smart contracts used to push malicious code on npm" (reversinglabs; NOT in source-grades.yaml — treat as B-class, flag for librarian)

- URL: https://www.reversinglabs.com/blog/ethereum-contracts-malicious-code
- Published: 2026-08-04 · Retrieval: **search summary only**
- Key claim: independent analysis of the on-chain-contract C2 mechanism.

### SafeDep — expanded count (safedep, digraph: C, provisional)

- Published: 2026-08-04 · Retrieval: **search summary only**
- Key claim: 1,684 poisoned versions across 420 package names tied to 9 organisations (higher than Semgrep's count).

### The Hacker News — relay (thehackernews, digraph: B)

- URL: https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html
- Published: 2026-08-04 · Retrieval: **search summary only (HTTP 403)**
- Key claim: keyv-linked worm poisons hundreds of packages; plants Claude Code and VS Code hooks.

## Technical detail

Execution is install-time, not import-time. The poisoned tarball adds obfuscated loader files (observed as `setup.mjs` and `math_init.js`) and wires them into the package's **`preinstall`** lifecycle hook, so merely installing or restoring the dependency tree runs the code — the package never has to be `require`d by application code. The loader fetches the **Bun** JavaScript runtime and runs an obfuscated second stage; Wiz observed the resulting outbound calls under user-agent `Bun/1.3.13`. The second stage is a broad credential harvester aimed at developer workstations and CI/CD runners: npm auth tokens, GitHub Actions secrets and tokens, cloud-provider credentials (AWS IMDS/ECS, HashiCorp Vault, Kubernetes), SSH private keys, and any CI secrets exposed in the build environment. Reporting also describes planting **Claude Code and VS Code hooks** for persistence. Propagation is credential-fuelled: recovered npm tokens supply the publish rights for the next wave, which is why the campaign spread across many unrelated maintainer scopes in a single burst rather than radiating from one account.

Command-and-control is resolved from an **Ethereum-mainnet smart contract** rather than a hardcoded domain — a "dead-drop" the operators can update on-chain to repoint infrastructure. On-chain history shows the contract was initially configured with three domains before being updated to return only `npm-cache[.]com`. Recorded at awareness level (Hard Rule 3 — no exploit or payload mechanism reproduced).

## IOCs surfaced

```yaml
atomic_iocs:
  - type: eth_contract_address
    value: "0xa1b40044EBc2794f207D45143Bd82a1B86156c6b"
    context: "Ethereum-mainnet smart contract used as C2 dead-drop (resolver for C2 domains)"
    confidence: reported
    source: [socket, reversinglabs]
  - type: eth_wallet_address
    value: "0x52221c293a21D8CA7AFD01Ac6bFAC7175D590A84"
    context: "Associated wallet address"
    confidence: reported
    source: [socket, reversinglabs]
  - type: domain
    value: "npm-cache[.]com"
    context: "C2 domain returned by the on-chain contract after it was updated (was 3 domains initially)"
    confidence: reported
    source: [socket]
  - type: user_agent
    value: "Bun/1.3.13"
    context: "User-agent observed on second-stage malicious outbound calls (Bun runtime)"
    confidence: reported
    source: [wiz-research]
file_iocs:
  - type: filename
    value: "setup.mjs"
    context: "Obfuscated preinstall loader dropped into poisoned tarballs"
    confidence: reported
  - type: filename
    value: "math_init.js"
    context: "Obfuscated preinstall loader dropped into poisoned tarballs"
    confidence: reported
behavioral_iocs:
  - "Malicious npm `preinstall` lifecycle hook executing at install / dependency resolution"
  - "Bun runtime downloaded and executed on a developer workstation or CI runner"
  - "Outbound resolution of C2 via an Ethereum-mainnet smart-contract read"
  - "Reads of npm tokens, GitHub Actions secrets, AWS IMDS/ECS, Vault, Kubernetes creds, SSH private keys during install"
package_iocs:
  - type: npm_package
    value: "keyv"
    context: "Patient zero — keyv@6.0.0 published 2026-08-04 09:35:00Z"
    confidence: reported
  - type: npm_package
    value: "cacheable"
    context: "Hijacked (Wiz)"
    confidence: reported
  - type: npm_scope
    value: ["jaredwray", "servicetitan", "ornikar", "qlik", "nebula.js"]
    context: "Named affected scopes/packages (non-exhaustive; ~435 packages total)"
    confidence: reported
credential_exposure_detected: false      # objective is credential theft, but no credential VALUES handled (Hard Rule 7)
```

> **First-party enrichment pending.** splunk-query, virustotal, and urlscan MCP servers did not connect this session — no IOC was checked against first-party telemetry or external reputation. Required follow-up on reconnect: `/ioc-hunt npm-cache[.]com`; Splunk for `Bun/1.3.13` user-agent from build/CI hosts and for `preinstall`-triggered child processes; enrich the ETH contract/wallet and `npm-cache[.]com`.

## Relationship to existing findings

Continues the software-supply-chain / npm-worm threat class the corpus already tracks — the same operational family as the SapphireSleet/DPRK npm compromises (finding-2026-07-30-0005) and the broader 2026 npm-worm lineage (Shai-Hulud, Miasma / binding.gyp, node-gyp, Mini-Shai-Hulud / TeamPCP). ChainDrop is a **distinct** campaign: no shared attribution is asserted, the propagation is credential-token-fuelled self-replication, and the C2 is a blockchain dead-drop. Related as a class, not the same campaign. Not merged.

## A&D relevance

Structural / indirect, but higher-signal than a typical library compromise because the payload is a **CI/CD credential harvester**. The npm-maintainer-hijack → poisoned-preinstall → CI/cloud-secret-theft chain is the operational template that reaches a Tier-1/2 supplier's software development lifecycle: a poisoned transitive dependency pulled into a supplier build could exfiltrate GitHub Actions tokens, cloud credentials, and signing/publish secrets from the build environment, enabling downstream pipeline compromise. No DIB/A&D victim is named — the exposure is the vector (broadly-depended packages such as keyv/cacheable make transitive exposure plausible across enterprise and supplier tooling), not an observed A&D compromise. Blockchain C2 raises the takedown bar.

## Recommended defensive actions (for the brief)

- **Audit lockfiles** for the poisoned versions (start with `keyv`, `cacheable`, and the named scopes); pin/freeze and rebuild from a clean state.
- **Block install scripts** in CI (`npm install --ignore-scripts`); move to npm **trusted/staged publishing** and decouple pipeline credentials from registry-publish credentials. (npm v12 disables install scripts by default.)
- **Rotate** npm tokens, GitHub Actions secrets, cloud credentials, and SSH keys exposed to any affected build runner.
- **Detect/alert** on `npm-cache[.]com`, on outbound `Bun/1.3.13` from CI runners, and on unexpected Bun-runtime downloads during `npm install`.

## Analytic notes (KAC)

KAC applied; ACH declined (no attribution → no competing-actor hypotheses; constructing them would risk originating attribution, Hard Rule 2). Two qualifiers must reach the briefer. First, **retrieval quality**: corroboration is genuinely multi-vendor and independent, but every primary 403'd and no first-party observation was possible this cycle — Archimedes verified nothing directly, which is exactly why the grade is B2 / "likely" and not higher. Second, **A&D relevance is structural**: no DIB victim is named; the risk is the CI/CD-credential-theft supply-chain vector reaching a supplier SDLC transitively. Scale numbers (1,557 vs 1,684) should be presented as a floor. Direct primary retrieval or a single first-party IOC hit would lift this toward "very likely" / credibility 1.

## Open questions

- **Direct retrieval.** All primaries 403'd this cycle. Re-fetch Semgrep / StepSecurity / Wiz / Socket / ReversingLabs directly (or via an MCP fetch path) to confirm the mechanism and reconcile the scale counts.
- **First-party exposure.** Once splunk-query is back: any `Bun/1.3.13` UA from build/CI hosts? any resolution of `npm-cache[.]com`? any affected package versions in package telemetry?
- **Attribution.** None asserted. Watch for an A-grade source naming an operator before any actor-dossier action (Hard Rule 2).
- **Scope drift.** Counts were still climbing at report time; confirm the final package/version tally and whether additional scopes were hit after 11:44 UTC.
