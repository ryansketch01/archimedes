---
raw_id: raw-2026-05-27-am-002
collected_at: 2026-05-27T07:40:00-04:00
run_id: pre-brief-2026-05-27-am
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (Ionut Arghire)
  source_url: https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/
  published_at: 2026-05-25T03:40:00-04:00       # 2026-05-25 07:40 UTC = 03:40 EDT
secondary_source:
  source_yaml_id: dark-reading
  source_name: Dark Reading (Rob Wright)
  source_url: https://www.darkreading.com/application-security/megalodon-malware-infects-thousands-github-repos
  published_at: 2026-05-26T19:47:14+00:00       # 2026-05-26 15:47 EDT — yesterday PM in window
originating_research:
  primary:
    name: SafeDep
    source_yaml_id: safedep
    grade_existing: C (provisional, per source-grades.yaml 2026-05-12)
    role: Originating uncoverer of the May 18 commit campaign; published full list of compromised repositories
  secondary:
    name: Ox Security
    source_yaml_id: ox-security
    grade_existing: B (provisional, per source-grades.yaml 2026-05-15; awaiting_direct_retrieval: true)
    role: Secondary analysis with Mini Shai-Hulud lineage reference
    note: |
      Per source-grades.yaml, ox-security was awaiting_direct_retrieval:
      true. This SecurityWeek + Dark Reading + cross-referenced Ox
      Security blog citation does NOT yet constitute the direct primary
      retrieval — the actual ox.security/blog/megalodon-cicd-malware-github/
      page was not WebFetched this sweep. Direct-retrieval flag should
      remain set; this raw-signal counts as second co-citation, not
      direct fetch.
match_reason:
  watchlist: []
  actors: []          # UNATTRIBUTED per SafeDep + Ox Security explicit decline; peer-mention of TeamPCP and Mini Shai-Hulud as lineage references but NO cross-walk
  vulnerabilities:
    - VT-006 (CVE-2026-45321 Mini Shai-Hulud — lineage-adjacent per Ox Security peer mention)
  keywords: [Megalodon, GitHub Actions, supply chain, SafeDep, Ox Security, build-bot, build-system@noreply.dev, ci-bot@automated.dev, 5561 repositories, 5718 commits, Tiledesk, eljohnny, workflow_dispatch, dormant backdoor, npm, CI/CD, credential theft, Mini Shai-Hulud, TeamPCP]
triage_tags: [supply_chain_attack_multi_victim, github_ecosystem_compromise, ci_cd_pipeline_attack, credential_theft_scope_aws_gcp_azure_ssh_docker_kubernetes_github_gitlab, unattributed_per_originator, mini_shai_hulud_teampcp_lineage_adjacent_per_peer_mention, structural_ad_sdlc_warning, ox_security_direct_retrieval_still_pending]
iocs_extracted: false
iocs_count: 0
text_word_count: 1240
promoted: false
rejected_at: 2026-05-27T08:12:00-04:00
rejection_id: reject-2026-05-27-0001
rejected_by: grader
rejected_in_run: morning-20260527-080000
rejection_summary: "Anti-noise rule 1 saturated - SAME EVENT as finding-2026-05-25-0001 Megalodon GitHub workflow_dispatch mass backdoor promoted 2026-05-25 morning brief; Dark Reading (Rob Wright) in-window relay adds no net-new research layer beyond SafeDep + Ox Security primaries already corpus-tracked."
ttl_expires_at: 2026-08-25T07:40:00-04:00
---

# Over 5,500 GitHub Repositories Infected in Megalodon Supply Chain Attack

## Sources

**Primary research originators:**
- **SafeDep** — uncovered the May 18 commit campaign, published the
  full list of 5,561 compromised repositories, traced the malicious
  commits to forged author `build-bot` with email
  `build-system@noreply[.]dev` and commit message `ci: add build
  optimization step`.
- **Ox Security** — secondary analysis layer; published a separate
  blog post titled "Megalodon: New CI/CD Malware Spreads Across
  GitHub, Infecting ~5,000+ Repositories" at
  https://www.ox.security/blog/megalodon-cicd-malware-github/ (NOT
  directly retrieved this sweep — Ox Security `awaiting_direct_retrieval`
  flag remains set per source-grades.yaml 2026-05-15 entry).

**Media relays in this AM-27 pre-brief window:**
- SecurityWeek (Ionut Arghire), 2026-05-25 07:40 UTC = 03:40 EDT
- Dark Reading (Rob Wright), 2026-05-26 19:47 UTC = 15:47 EDT (this
  is the in-window item that surfaced via the Dark Reading RSS feed
  this sweep)

## Attack timeline

**All 5,718 malicious commits landed on the same day: 2026-05-18.**
The activity was concentrated in a **6-hour window from approximately
11:36 to 17:48 UTC** (= 07:36 to 13:48 EDT). The attacker targeted
**5,561 distinct repositories** with the commits.

Follow-on compromise: Tiledesk packages were published with the
infection 2026-05-19 through 2026-05-21 (the eljohnny npm account was
compromised and used to push poisoned package versions).

## Attack mechanism

Two distinct payload classes were deployed:

1. **Payload class 1 — new workflow injection**: A new GitHub Actions
   workflow added to the target repository, configured to trigger on
   every `push` and `pull_request` event.
2. **Payload class 2 — workflow replacement**: Existing workflows
   replaced with `workflow_dispatch`-type workflows that act as
   **dormant backdoors**. The `workflow_dispatch` trigger type is
   notable because it is exempted from GitHub's anti-recursion rules
   (workflows triggered by `workflow_dispatch` can themselves trigger
   further workflows, which is normally blocked for `push` triggers
   to prevent loops). The dormant backdoor is remotely activatable
   via stolen GitHub tokens.

## Credential theft scope

Per SafeDep's research, the payload exfiltrated:
- CI environment variables (general)
- AWS, GCP, Azure cloud credentials
- SSH private keys
- Docker and Kubernetes config files
- API keys (general)
- Database connection strings
- GitHub Actions tokens
- GitLab CI/CD tokens
- "Dozens of other types of secrets" (per the SecurityWeek relay,
  paraphrased — not a verbatim quote per Hard Rule 6)

## Forged identities

- Author: `build-bot`
- Two distinct email addresses linked to **2,878 and 2,841 commits
  respectively** (sum = 5,719 ≈ 5,718 ± 1 reconciliation noise)
- Email pattern (per the searched/relayed reporting):
  `build-system@noreply[.]dev` and `ci-bot@automated[.]dev`
- npm account compromised: `eljohnny` (associated email per the
  reporting)
- Author identity strings designed to mimic routine automated CI
  maintenance (`build-bot`, `auto-ci`, `ci-bot`, `pipeline-bot`)

## Named victims

**Tiledesk** (open-source live-chat / chatbot platform) — the only
explicitly named victim. Poisoned Tiledesk packages were published
2026-05-19 through 2026-05-21 via the compromised eljohnny npm
account.

No A&D / aerospace / defense / DIB / CMMC / ITAR victims named.
**No watchlist A&D prime named** (Lockheed Martin, Boeing, RTX,
Northrop Grumman, General Dynamics, BAE Systems, L3Harris, Leidos,
SAIC, Thales, GE Aerospace, Safran, Honeywell, Airbus, Elbit Systems
all silent).

## Attribution — UNATTRIBUTED

**SafeDep does not attribute Megalodon to a specific group.** SafeDep
references **TeamPCP compromising GitHub** as a preceding event in
the broader supply-chain-attack timeline, framing Megalodon as part
of an ongoing supply-chain-attack era rather than a TeamPCP-attributed
operation specifically.

**Ox Security mentions "Mini Shai-Hulud"** in its analysis as a
lineage reference — Mini Shai-Hulud is Archimedes-tracked as VT-006
(CVE-2026-45321) and connects to the TeamPCP roster actor (#001).
Ox Security's framing per the relay is that supply-chain attacks have
become "an endless wave" with Megalodon as the latest manifestation.

**Per Hard Rule 2, Archimedes records the SafeDep + Ox Security
explicit non-attribution and the peer-mention of TeamPCP / Mini
Shai-Hulud as lineage references only — NOT as attribution cross-walks.**
Megalodon is UNATTRIBUTED in the Archimedes corpus pending
A-grade-IR-firm corroborating attribution.

## IOCs

| Type | Value | Notes |
|---|---|---|
| Author identity (forged) | `build-bot` | Single author name across all 5,718 commits |
| Author identity (alternates per relay) | `auto-ci`, `ci-bot`, `pipeline-bot` | Per SecurityWeek-cited Ox Security analysis |
| Email (forged) | `build-system@noreply[.]dev` | Associated with 2,878 commits per SafeDep |
| Email (forged) | `ci-bot@automated[.]dev` | Associated with 2,841 commits per SafeDep |
| npm account (compromised) | eljohnny | Email per reporting; used to push poisoned Tiledesk packages |
| Commit message (pattern) | "ci: add build optimization step" | The canonical commit message used across the 5,718 commits |
| Compromised repository count | 5,561 distinct repositories | Full list published by SafeDep |
| Compromised commits count | 5,718 total commits | Sum across the 6h window 2026-05-18 |

Per Hard Rule 3, no working exploit chain or PoC payload is reproduced
in this raw-signal. The attack mechanism description above is
defender-actionable (detection rules) but does NOT include the actual
payload code that exfiltrated secrets.

## CVE assigned

**None.** The article does not reference any assigned CVE ID for the
Megalodon campaign. The compromise was at the GitHub-organization /
npm-account credential layer, not a software-vulnerability layer per
se.

## GitHub's response

Per the SecurityWeek relay, GitHub's specific response on Megalodon is
not detailed. The relay notes:
- GitHub's anti-recursion rules exist but the `workflow_dispatch`
  trigger type bypasses them by design
- npm (separate platform, GitHub-owned) "invalidated all granular
  access tokens with write access bypassing 2FA last week" — this is
  a related but distinct response to a broader credential-hygiene
  surface, not a Megalodon-specific intervention

No GitHub self-disclosure post (github-blog-self-disclosure id per
source-grades.yaml, provisional A) located this sweep.

## A&D-SDLC indirect exposure framing

While no A&D prime is named in the Megalodon coverage, the supply-chain
attack mechanism (GitHub Actions workflow injection + `workflow_dispatch`
dormant backdoor + CI-credential exfiltration) is structurally relevant
to A&D-prime SDLCs: any A&D-prime engineering organization with public
or partner-accessible GitHub repositories had contemporaneous exposure
to the same attack mechanism. The 5,561-repository scope is the largest
single-day GitHub supply-chain attack the Archimedes corpus has tracked.

This is **structural supply-chain warning class** for the grader's
consideration. Per Hard Rule 2, Archimedes does NOT extrapolate from
"5,561 unnamed victims" to "specific A&D-prime exposure" — that
extrapolation would require a named-victim disclosure.

## Relationship to Mini Shai-Hulud (VT-006)

Mini Shai-Hulud is Archimedes-tracked as VT-006 (CVE-2026-45321),
which connects to TeamPCP roster actor #001. Ox Security's
peer-mention of Mini Shai-Hulud in the Megalodon analysis is a
**lineage reference, not an attribution claim**. The mechanism
differs (Mini Shai-Hulud was OIDC-credential-abuse on npm; Megalodon
is GitHub Actions workflow injection on GitHub Actions CI/CD), so
the cross-walk should be treated as ecosystem-adjacency framing, not
direct attribution.

## Extraction notes

- Language: en
- Publisher byline: Ionut Arghire (SecurityWeek); Rob Wright (Dark
  Reading)
- Article type: media relay of vendor research (SafeDep + Ox Security
  primaries)
- Raw IOC extraction invoked: yes (manual; structured into the IOCs
  table above)
- CVSS / CVE: N/A (no CVE assigned; campaign is supply-chain
  credential-theft class)
- Hard Rule 2 compliance: SafeDep + Ox Security non-attribution
  preserved; TeamPCP / Mini Shai-Hulud peer-mentions recorded as
  lineage references only, NOT attribution cross-walks. Megalodon
  remains UNATTRIBUTED in Archimedes corpus.
- Hard Rule 3 compliance: no working payload code reproduced; attack
  mechanism described at defender-actionable level only.
- Hard Rule 6 compliance: no direct quotes >15 words; SafeDep and Ox
  Security characterizations paraphrased.
- Ox Security direct-retrieval flag in source-grades.yaml remains
  set (this raw-signal is a media-relay surface, not direct fetch
  of ox.security/blog/megalodon-cicd-malware-github/).
