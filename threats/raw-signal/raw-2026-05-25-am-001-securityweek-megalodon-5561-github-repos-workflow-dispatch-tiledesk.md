---
raw_id: raw-2026-05-25-am-001-securityweek-megalodon-5561-github-repos-workflow-dispatch-tiledesk
collected_at: 2026-05-25T07:36:00-04:00
run_id: pre-brief-20260525-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: securityweek
  source_name: "SecurityWeek (Ionut Arghire byline) — primary research SafeDep (direct retrieval) — Megalodon mass GitHub workflow_dispatch backdooring campaign"
  source_url: https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/
  source_primary_url: https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows
  source_grade_securityweek: B (provisional, awaiting ratification)
  source_grade_safedep: TENTATIVE_B_PENDING_OPERATOR_RATIFICATION   # safedep.io NOT YET in source-grades.yaml; 4-day post-original-publication detection gap acknowledged; recommend operator-side source-grade-log entry
  published_at: 2026-05-25T03:40:00-04:00       # SecurityWeek relay in-window pickup
  primary_published_at: 2026-05-21T00:00:00-04:00   # SafeDep primary research; collection-gap acknowledged
match_reason:
  watchlist: []                                  # No A&D-prime named victim
  actors: []                                     # UNATTRIBUTED — Hard Rule 2 preserved per both SafeDep + SecurityWeek primary sources
  vulnerabilities: []                            # No CVE assigned; abuse-of-feature on GitHub Actions workflow_dispatch anti-recursion (GitHub considers intended-by-design per SafeDep framing)
  keywords:
    - "supply chain"
    - "GitHub Actions"
    - "workflow_dispatch"
    - "anti-recursion bypass"
    - "npm"
    - "@tiledesk/tiledesk-server"
    - "build-bot"
    - "auto-ci"
    - "ci-bot"
    - "pipeline-bot"
    - "Megalodon"
triage_tags:
  - strong_morning_finding_candidate
  - supply_chain_mass_compromise
  - github_actions_abuse
  - unattributed
  - net_new_to_corpus
  - safedep_first_corpus_citation
  - splunk_first_party_first_pass_zero_hits
  - non_flash_tier
iocs_extracted: true
iocs_count: 23                          # 1 C2 IP+port; 1 GitHub Pages domain (TrapDoor cross-reference, technically not Megalodon); 7 poisoned package versions; 1 forensic git commit hash; 4 author-identity spoofs; 3 throwaway GitHub usernames; 7 commit-message templates; 2 workflow filenames; 1 maintainer npm account
text_word_count: 2400
promoted: true
promoted_to_finding: finding-2026-05-25-0001-megalodon-github-workflow-dispatch-mass-backdoor
promoted_at: 2026-05-25T08:00:00-04:00
ttl_expires_at: 2026-08-23T07:36:00-04:00
---

# SecurityWeek — Over 5,500 GitHub Repositories Infected in 'Megalodon' Supply Chain Attack
# Primary: SafeDep (direct retrieval) — Megalodon Mass GitHub Repo Backdooring via CI Workflows

**Title (SecurityWeek):** Over 5,500 GitHub Repositories Infected in 'Megalodon' Supply Chain Attack
**Title (SafeDep primary):** Megalodon: Mass GitHub Repo Backdooring via CI Workflows
**Authors:** Ionut Arghire (SecurityWeek byline); SafeDep Team byline on primary (no individual researcher named)
**Published (SecurityWeek):** 2026-05-25 07:40 UTC = 03:40 EDT (in-window)
**Published (SafeDep primary):** 2026-05-21 (4 days prior to SecurityWeek relay; collection gap acknowledged)
**Primary source URL:** https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows
**Relay URL:** https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/

---

## One-paragraph summary

Attackers exploited a built-in GitHub Actions `workflow_dispatch`
anti-recursion behavior — by design GitHub does not retrigger the
workflow file that triggered it, which means a committer who can
add a workflow file via fake automated commits can deploy CI-time
payloads without setting off a recursive-trigger detection. Across
**5,718 malicious commits** spanning a tight 6h17m window on
2026-05-18 (11:36 → 17:48 UTC), the operator(s) backdoored **5,561
distinct GitHub repositories** via two payload-variant patterns
(SysDiag for push + pull_request_target maximum reach, Optimize-Build
for `workflow_dispatch` dormant backdoors). Both variants request
`id-token: write` and `actions: read` permissions and execute
`base64-encoded bash` one-liners. Downstream supply-chain impact:
the legitimate Tiledesk maintainer `eljohnny` unknowingly published
9 versions of `@tiledesk/tiledesk-server` from compromised source-
of-truth between 2026-05-19 and 2026-05-21 (clean version: 2.18.5;
poisoned versions: 2.18.6 through 2.18.12). C2 infrastructure:
`216.126.225.129:8443`. Throwaway GitHub accounts use random 8-
character usernames (examples `rkb8el9r`, `bhlru9nr`, `lo6wt4t6`)
with **author-identity spoofing** of build-bot / auto-ci / ci-bot /
pipeline-bot identities and 7 generic commit-message templates.
**Attribution: UNATTRIBUTED.** SafeDep does not link to any tracked
actor or known cluster; SecurityWeek does not attribute. No A&D
named victims. Discovery credited to SafeDep's internal "Malysis
engine."

---

## Attribution language (Hard Rule 2)

> "No attribution made" — SafeDep explicitly declines to attribute to any tracked actor or nation-state.

SecurityWeek uses generic "the attacker" and "attackers" language.
No tracked-actor cross-walk to TeamPCP / GlassWorm / Shai-Hulud
family / Mini Shai-Hulud / any nation-state cluster is offered by
either source.

**Hard Rule 2 preserved:** Archimedes does not originate a
TeamPCP / GlassWorm / cross-cluster attribution. Author-identity
spoofing of build-bot / auto-ci / ci-bot / pipeline-bot
thematically overlaps with TeamPCP's
`claude@users.noreply.github.com` spoofing pattern from the
2026-05-12 Mini Shai-Hulud worm (corpus VT-006), **but the
technique is portable and likely shared across multiple
unattributed cybercriminal operators in the current SDLC-
targeting wave**. Do NOT collapse Megalodon, TrapDoor, and
TeamPCP into one actor without A/B-grade attribution.

---

## Technical mechanism — `workflow_dispatch` anti-recursion bypass

GitHub Actions normally does not retrigger workflow runs that were
themselves triggered by a workflow committing a file. This anti-
recursion behavior — intended-by-design according to SafeDep's
framing — means a committer who pushes a `.github/workflows/*.yml`
file via a fake automated commit can deploy CI-time payloads
without firing a recursive-trigger detection.

The campaign deployed **two payload variants** using this
mechanism:

| Variant | Trigger surface | Effect |
|---|---|---|
| **SysDiag** | `push` (all branches) + `pull_request_target` | Maximum automated execution; runs on every push + every PR-merge candidate |
| **Optimize-Build** | `workflow_dispatch` (replaces existing) | Dormant backdoor executable via GitHub API when operator chooses (using stolen tokens) |

Both variants:

- Request permissions `id-token: write` and `actions: read`
- Execute via `set +e; echo "<BASE64>" | base64 -d | bash`
  one-liners ("base64-encoded bash" per SafeDep — 4-word quoted
  phrase under Hard Rule 6 limit)
- Target CI environment variables, AWS / GCP / Azure credentials,
  SSH private keys, Docker / Kubernetes configs, API keys,
  database connection strings, GitHub Actions tokens, GitLab CI/CD
  tokens

---

## Timeline

| Time (UTC) | Event |
|---|---|
| 2026-05-18 11:36–17:48 | Mass-injection window: 5,718 commits across 5,561 repositories |
| 2026-05-19 | `@tiledesk/tiledesk-server@2.18.6` published to npm by `eljohnny` (legitimate maintainer) from now-poisoned source-of-truth |
| 2026-05-19 → 2026-05-21 | Sequential npm publication of versions 2.18.7 through 2.18.12 |
| 2026-05-21 | SafeDep primary research published (`/megalodon-mass-github-repo-backdooring-ci-workflows`) |
| 2026-05-25 03:40 EDT | SecurityWeek (Ionut Arghire) in-window relay |
| 2026-05-25 06:00 EDT | Archimedes 06:00 FLASH sentinel flags as morning-pickup priority |
| 2026-05-25 07:30 EDT | Archimedes pre-brief sweep direct-retrieves SafeDep primary; this raw-signal written |

The legitimate Tiledesk maintainer `eljohnny` published versions
2.18.6 through 2.18.12 **without realizing the underlying source
repository had been compromised** in the May 18 mass-injection
window. Clean version: 2.18.5.

---

## Victim scope

### Primary directly-named victim

- **Tiledesk** (open-source live-chat / chatbot platform; 9 repos
  affected):
  - `tiledesk-server`
  - `tiledesk-dashboard`
  - `tiledesk-telegram-connector`
  - `tiledesk-llm`
  - `tiledesk-docker-proxy`
  - `tiledesk-community-app`
  - `tiledesk-campaign-dahboard` (sic, per SafeDep)
  - `tiledesk-helpcenter-template`
  - `tiledesk-ai`

### Secondary named organizations

- **Black-Iron-Project** (8 repositories)
- **WISE-Community** (count not specified)
- **~5,500 smaller repositories** (individual personal blogs,
  small OSS projects, miscellaneous)

### A&D / defense / aerospace impact

**None named.** SafeDep does not identify any A&D-prime victim;
SecurityWeek does not identify any A&D-prime victim. A&D
relevance is **structural-indirect** via developer-ecosystem
ubiquity only — Tiledesk is a live-chat platform with no
A&D-specific deployment context surfaced in either source.

---

## Indicators of Compromise

### C2 infrastructure

- **`216.126.225.129:8443`** (single C2 IP, single port observed)

### Cross-reference (TrapDoor exfil endpoint — distinct campaign, similar developer-ecosystem-abuse layer)

- `ddjidd564.github[.]io` — appears in TrapDoor coverage (THN
  2026-05-25 01:59 EDT) but NOT in Megalodon primary; documented
  here as cross-corpus disambiguator only. Operator should not
  conflate Megalodon and TrapDoor IOCs.

### Compromised npm package versions

- `@tiledesk/tiledesk-server@2.18.6`
- `@tiledesk/tiledesk-server@2.18.7`
- `@tiledesk/tiledesk-server@2.18.8`
- `@tiledesk/tiledesk-server@2.18.9`
- `@tiledesk/tiledesk-server@2.18.10`
- `@tiledesk/tiledesk-server@2.18.11`
- `@tiledesk/tiledesk-server@2.18.12`

Clean version: `@tiledesk/tiledesk-server@2.18.5` and earlier.

### Forensic commit hash (Tiledesk)

- `acac5a9854650c4ae2883c4740bf87d34120c038` — Tiledesk-side
  commit reference per SafeDep primary writeup

### Throwaway GitHub accounts (random 8-char usernames; pattern)

- `rkb8el9r`
- `bhlru9nr`
- `lo6wt4t6`

Pattern: 8-character lowercase-alphanumeric usernames; no prior
commit history; created shortly before the 2026-05-18 mass-
injection window.

### Author-identity spoofing (forged Git author names in commits)

- `build-bot`
- `auto-ci`
- `ci-bot`
- `pipeline-bot`

Associated forged email addresses are masked by Cloudflare email-
protection on the SafeDep primary surface and could not be
fully extracted via direct WebFetch (`[email protected]`-pattern
placeholders observed but actual addresses not in cleartext).

### Forged-commit message templates (7 variants observed)

- `ci: add build optimization step`
- `build: improve ci performance`
- `chore: optimize pipeline runtime`
- `chore: sync ci configuration`
- `chore: update ci/cd pipeline`
- `ci: update build config`
- `fix: correct build workflow`

### Workflow filenames

- `.github/workflows/ci.yml` (SysDiag variant — push +
  pull_request_target)
- Existing workflows REPLACED in the Optimize-Build variant
  (filename varies per victim)

### npm maintainer

- `eljohnny` (legitimate Tiledesk maintainer; UNKNOWING publisher
  of poisoned versions 2.18.6-2.18.12)

---

## Detection signatures (per SafeDep + extrapolation)

SafeDep does not publish formal YARA / Semgrep / Sigma rules.
Detection guidance focuses on:

1. **Workflow file names** `SysDiag` or `Optimize-Build` in
   `.github/workflows/`
2. **Base64-encoded bash payloads** in workflow files (especially
   in `run:` steps)
3. **Author emails** matching `noreply@` patterns with forged
   identities (`null` user fields in GitHub API responses are
   diagnostic)
4. **Permission requests** combining `id-token: write` AND
   `actions: read`
5. **Commit author names** matching `build-bot`, `auto-ci`,
   `ci-bot`, `pipeline-bot` from accounts with no prior history

### Splunk-actionable detections (Archimedes operator extension; not in SafeDep)

```spl
| search index=<github-audit> action=workflow_run.completed
  workflow.path="*.github/workflows/SysDiag*"
  OR workflow.path="*.github/workflows/Optimize-Build*"
| stats count by repo workflow.path actor

| search index=<github-audit> commit.author.email="*noreply*"
  commit.author.user=NULL
| stats count by repo commit.author.name commit.message
```

(Both queries are Archimedes-operator-side extensions, not
published by SafeDep. Useful only for GitHub audit-log ingest
estates.)

### Splunk first-party hand-built query EXECUTED this sweep

```spl
search index=defenseclaw_local earliest=-24h@h latest=now
  (216.126.225.129 OR megalodon OR tiledesk OR
   "@tiledesk/tiledesk-server" OR "build-bot" OR "auto-ci" OR
   "ci-bot" OR "pipeline-bot")
| head 50
```

Result: **ZERO hits**. Hard Rule 8: silence is not disconfirming.
First-party telemetry on `defenseclaw_local` index dormant non-self
(56th consecutive sweep on tstats baseline).

---

## Response recommendations (per SafeDep + Archimedes operator extension)

### SafeDep guidance

1. Audit `.github/workflows/*.yml` files for unauthorized changes
   since 2026-05-18
2. Review Git history for commits lacking linked GitHub accounts
   (`null` user fields)
3. **Invalidate exposed CI secrets, PATs, cloud credentials,
   SSH keys**
4. Inspect npm publish logs for packages built from compromised
   repositories

### Archimedes operator extension (A&D-prime SDLC context)

5. Check `package-lock.json` / `package.json` for transitive
   dependencies on `@tiledesk/tiledesk-server@2.18.6` through
   `@tiledesk/tiledesk-server@2.18.12` across all A&D-prime
   SDLCs (Lockheed Martin, Boeing, RTX, Northrop Grumman, GD,
   BAE Systems, L3Harris, Leidos, SAIC, Thales, GE Aerospace,
   Safran, Honeywell Aerospace, Airbus, Elbit)
6. If any pinning to a poisoned version surfaces, treat as a
   credential-exposure event for the affected SDLC's CI/CD
   chain — rotate everything in the SafeDep guidance list
7. Add `216.126.225.129` to perimeter blocklists and CI/CD
   egress-monitoring; query DNS resolver logs for any historical
   resolution of the IP
8. Consider whether GitHub Actions `workflow_dispatch` anti-
   recursion behavior should be addressed via repo-level branch-
   protection rules requiring signed commits and/or required
   reviews on `.github/workflows/*.yml` changes

---

## A&D relevance (per Archimedes target-profile calibration)

**Structural-indirect via developer-ecosystem ubiquity.** No A&D-
prime is named in either SafeDep or SecurityWeek. Same calculus
that has held for prior unattributed supply-chain mass-compromise
events in the corpus:

- Mini Shai-Hulud (VT-006, 2026-05-12) — `@squawk` aviation-namespace
  exposure tracked as indirect / medium
- TrapDoor (Socket, 2026-05-24) — AI-coding-agent SDLC ubiquity;
  no A&D-prime named
- art-template (Coruna 2026-05-20) — iOS-class supply chain
- durabletask (Wiz 2026-05-19) — TeamPCP PyPI compromise

If an A&D-prime publishes a customer-impact statement naming
`@tiledesk/tiledesk-server` transitive-dependency exposure in
the next 24-72h, ad_relevance shifts upward. Until then:
**indirect / structural / medium calibration**.

### Specific A&D-relevance hooks

- Tiledesk is live-chat / chatbot infrastructure — may appear in
  A&D-prime customer-support stacks, partner-portal layers, or
  internal IT help-desk deployments rather than in mission-system
  SDLCs. Lower-criticality blast radius than a mission-critical
  package.
- The `workflow_dispatch` anti-recursion bypass mechanism itself
  is the high-impact takeaway, not the Tiledesk package — any
  A&D-prime SDLC operating GitHub Actions is procedurally
  exposed to the same attack class if a repo's workflow files
  can be modified by a poisoned committer identity.

---

## Cross-corpus diagnostic note (for actor-profiler / next /update-tracking cycle)

Author-identity spoofing patterns observed across recent
unattributed supply-chain mass-compromise events:

| Campaign | Spoofed identity pattern | Source | Attribution |
|---|---|---|---|
| Megalodon (this) | `build-bot`, `auto-ci`, `ci-bot`, `pipeline-bot` | SafeDep | UNATTRIBUTED |
| Mini Shai-Hulud (VT-006) | `claude@users.noreply.github.com` | Wiz / Snyk / StepSecurity | TeamPCP (per StepSecurity → Wiz relay; single-A-grade-corroboration-tier per finding-2026-05-12-FLASH-0001) |
| TrapDoor (finding-2026-05-24-0001) | (not specified in Socket/THN coverage) | Socket | UNATTRIBUTED |
| node-ipc (finding-2026-05-14-0009 / 2026-05-15-0005) | `atiertant` (no-history account) | Socket / StepSecurity / Ox Security / Upwind | UNATTRIBUTED (four-firm consensus) |

**Cross-corpus pattern observation:** Author-identity spoofing
+ throwaway account creation is a technique class that has
appeared in 4+ unattributed supply-chain mass-compromise events
in the past 14 days. The technique is **portable post-access**
and does NOT distinguish actor identity. Actor-profiler should
treat this as a **technique-class catalog entry**, not as a
diagnostic actor-attribution signal. Recommend logging this
pattern in the analyst's "AI-coding-agent abuse + supply-chain
mass-compromise" TTP tracker (which already exists in the corpus
per prior sentinel-stream observations).

---

## Recommendations to morning grader / briefer / orchestrator

1. **Grader: promote this raw-signal to finding-tier** for the
   2026-05-25 morning brief. Substantive net-new technical
   content (the `workflow_dispatch` anti-recursion mechanism is a
   novel-class abuse pattern; the 5,561-repo scope is the largest
   single supply-chain mass-compromise event in the corpus to
   date by repo count). Tentative Admiralty grade per SafeDep
   primary: A2 (SafeDep tentative-A pending source-grade-log
   ratification × likely confidence on technical-mechanism
   facts; capped at "likely" not "very likely" because single-
   source-veto applies on the campaign-scope claim at primary
   level — SecurityWeek is pure relay).
2. **Operator: add safedep.io to source-grades.yaml** as
   tentative-B grade primary supply-chain research vendor (Socket /
   Snyk / StepSecurity tier). Acknowledge the 4-day post-original-
   publication detection gap in the source-grade-log entry. The
   `/megalodon-mass-github-repo-backdooring-ci-workflows`
   primary surface demonstrates Socket / Snyk-comparable IOC
   depth and named-engine attribution discipline ("Malysis
   engine" + explicit "no attribution made" methodological
   restraint).
3. **VirusTotal enrichment on `216.126.225.129`**: query
   `mcp__virustotal__lookup_ip` for AS / netblock / vendor
   detection scores. Pull into finding promotion if grader
   promotes.
4. **Splunk Hand-built sweep already executed this sweep
   (zero hits)**: maintain the keyword list as a Splunk savedsearch
   for ongoing monitoring against `defenseclaw_local` — fire a
   Splunk alert if `216.126.225.129` ever resolves in
   `defenseclaw_local` logs.
5. **Actor-profiler hook on next /update-tracking cycle**:
   add author-identity-spoofing pattern + throwaway-account-
   creation pattern to the "AI-coding-agent abuse + supply-chain
   mass-compromise" TTP catalog as technique-class observations
   that span 4+ unattributed events in the past 14 days.
   Explicitly DO NOT collapse Megalodon / TrapDoor / TeamPCP /
   node-ipc into a single actor without A/B-grade attribution.
6. **Vuln-tracker: not applicable** — no CVE assigned to the
   `workflow_dispatch` anti-recursion bypass mechanism;
   GitHub considers the anti-recursion behavior intended-by-design
   per SafeDep framing. No VT-entry candidate.

---

## Hard Rules compliance check

- **Rule 2** (no Archimedes-originated attribution): UNATTRIBUTED
  preserved. Cross-corpus author-identity-spoofing pattern flagged
  as technique-class observation, NOT actor-attribution.
- **Rule 3** (no exploitation content): no PoC code reproduced;
  attack mechanism described at conceptual level. Operator-side
  detection guidance and Splunk SPL examples are defensive.
- **Rule 4** (passive only): SafeDep direct-retrieval is passive;
  Splunk first-party query is on Archimedes's own instance.
  No active recon.
- **Rule 6** (15-word quote limit): 4-word quoted phrase
  ("base64-encoded bash") from SafeDep — within limit; single
  instance. 5-word quoted phrase from SafeDep methodology
  ("No attribution made") — within limit; single instance.
- **Rule 7** (credentials radioactive): no credentials surfaced
  in either source. Forged email addresses are
  Cloudflare-protected on SafeDep primary surface; not extracted
  in cleartext.
- **Rule 8** (Splunk first-party): hand-built sweep executed;
  zero hits on `216.126.225.129` + all related Megalodon
  keywords. 56th consecutive dormant non-self sweep on
  `defenseclaw_local`. Silence is not disconfirming.

---

## Disposition

- **Raw-signal status:** companion to am-000 sentinel; STRONG
  morning finding candidate for 2026-05-25 08:00 morning brief.
- **Grader promote target:** finding-tier-eligible. Tentative
  Admiralty A2 capped at "likely" pending source-grades.yaml
  entry for safedep.io.
- **Anti-noise lock recommended on grader promotion:**
  `megalodon-mass-github-workflow-dispatch-tiledesk` from finding-
  creation through 2026-05-26 16:00 EDT (24h post-grade) — same
  template as prior supply-chain anti-noise locks.
- **VirusTotal enrichment + Splunk-savedsearch action recommended
  to librarian.**
- **TLP:CLEAR.**
