---
finding_id: finding-2026-07-31-0002
created_at: 2026-07-31T18:12:00-04:00
graded_by: grader
grading_run_id: flash-grade-20260731-1800

# Core grading (from admiralty-grading skill output)
digraph: A2
source_reliability:
  grade: A
  source_name: Microsoft Threat Intelligence (MSTIC)
  source_yaml_id: mstic
  grade_rationale: >
    Pre-assigned A per source-grades.yaml (ratified). Nation-state tracking authority,
    Defender first-party telemetry-backed. Originating primary on the CaptiveCrunch
    campaign disclosure and the Storm-2945 sub-cluster designation.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent
    - probably_true_no_contradicting_ab
    - probably_true_claims_coherent
  grade_1_withheld_reason: >
    Grade 1 withheld — the primary claim (Storm-2945 IS an operational sub-cluster of
    Midnight Blizzard / APT29 running CaptiveCrunch) rests on a single originating primary
    (MSTIC). ReliaQuest (2026-07-23, B) independently reported a portion of the
    doppelganger-domain / AitM device-code activity but did NOT make the Midnight Blizzard
    sub-cluster attribution — it corroborates a sub-component, not the attribution binding.
    No independent A/B source confirms the Storm-2945 -> Midnight Blizzard assessment.
  rationale: >
    Probably True. Device-code / OAuth AitM phishing against Entra ID with M365 data
    collection is squarely consistent with APT29 / Midnight Blizzard's documented
    initial-access tradecraft (MSTIC ties Storm-2945 to Storm-2372, the Midnight Blizzard
    device-code sub-cluster tracked through 2025). Captive-portal / hospitality-Wi-Fi
    access is a new delivery vector but the downstream TTPs are coherent and in-character.
    No contradicting A/B-grade reporting; MSTIC explicitly distinguishes CaptiveCrunch from
    the Forest Blizzard (APT28) DNS-hijacking op rather than conflating them. No CVE claimed.
corroboration:
  independent_sources:
    - mstic
  partial_corroboration:
    - source: reliaquest
      grade: B
      scope: "Doppelganger-domain / AitM device-code layer only (ReliaQuest 2026-07-23) — NOT the Storm-2945 -> Midnight Blizzard sub-cluster attribution."
  independent: false
  test_passed: "FAILS on the primary attribution claim — remove MSTIC and the Storm-2945 -> Midnight Blizzard binding does not stand; ReliaQuest never made that attribution. One effective evidence basis on the attribution layer."
first_party_precedence:
  applied: false
  splunk_evidence: >
    FLASH mandatory tracked-IOC sweep -24h: 0 hits in archimedes (2148 events/-90d,
    self-log only) and 0 hits in defenseclaw_local (0 events in window, visibility-bounded
    null). Net-new CaptiveCrunch IOC enrichment sweep also 0/0. Silence is not
    disconfirmation (absence of evidence != evidence of absence).
single_source_veto_applied: true
single_source_veto_note: "Veto applied on the attribution/campaign claim — single originating primary (MSTIC). WEP capped at likely regardless of A-grade."
wep_ceiling: likely

# Cluster metadata
cluster:
  topic: "CaptiveCrunch — Storm-2945 (assessed Midnight Blizzard / APT29 sub-cluster per MSTIC) compromises captive-portal / hospitality Wi-Fi worldwide for AitM device-code phishing + malware delivery against corporate travelers"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-31-flash-1800-001
  attribution_claims:
    - claimed_actor: "Midnight Blizzard (APT29 / Cozy Bear / NOBELIUM / SVR) — via Storm-2945 sub-cluster"
      roster_id: "009"
      claimed_by_sources: [mstic]
      source_confidence: "assessed operational sub-cluster of Midnight Blizzard based on distinctive technical and operational overlaps (with Storm-2372)"
      single_source: true
      requires_analyst_review: true

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - flash
    - daily_brief_action
    - weekly_synthesis
    - actor_profile_update

# Downstream handoff flags
analyst_review_required: true    # attribution claim present (new sub-cluster) AND WEP >= likely
red_team_review_required: false  # WEP ceiling is "likely", not >= "very likely" (FLASH anti-noise rule 3 / grader doctrine)
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Source-grade notes (librarian awareness)
source_grade_notes:
  - source_yaml_id: reliaquest
    status: "Already proposed for provisional B addition via finding-2026-07-14-0009 (source_grade_additions_proposed). No new action; cited here only as partial corroborator of the AitM/doppelganger layer."

# Lifecycle
tlp: CLEAR
published_in_briefs: [flash-2026-07-31-1800]
retracted: false
retraction_brief_id: null
---

# CaptiveCrunch: MSTIC attributes a captive-portal AitM campaign against corporate travelers to a new Midnight Blizzard sub-cluster (Storm-2945)

## Summary

Microsoft Threat Intelligence disclosed CaptiveCrunch, a campaign active since early May 2026 in which a newly designated actor MSTIC calls Storm-2945 compromises captive-portal and Wi-Fi networks at hospitality venues worldwide (hotels, conference centers, shared venues) and manipulates DNS/HTTP traffic to funnel corporate travelers through actor-controlled infrastructure. MSTIC assesses Storm-2945 as an operational sub-cluster of Midnight Blizzard (APT29 / Cozy Bear, roster #009, SVR-attributed) based on technical and operational overlap with Storm-2372, its device-code-phishing initial-access cluster. Two strands run in parallel: adversary-in-the-middle phishing via doppelganger Microsoft-service domains abusing the Entra ID device-code flow (Entra device registration + M365 collection), and malware delivery disguised as browser/OS updates triggered by automated captive-portal connectivity checks, using ClickFix social-engineering prompts. The Storm-2945-to-Midnight-Blizzard attribution rests on MSTIC alone; single-source veto binds, capping this at likely.

## Sources

### Microsoft Threat Intelligence (MSTIC) (mstic, digraph: A)

- URL: https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
- Published: 2026-07-31 ~17:01 EDT (21:01 UTC)
- Key claim: Storm-2945, assessed as a Midnight Blizzard sub-cluster, runs the CaptiveCrunch captive-portal AitM + malware-delivery campaign against travelers worldwide; a significant portion is AI-augmented (Microsoft credits collaboration with Anthropic and OpenAI).

### ReliaQuest (partial corroborator, grade: B)

- Published: 2026-07-23
- Key claim: Reported a portion of the doppelganger-domain / AitM device-code activity. Per MSTIC's framing, ReliaQuest did NOT make the Midnight Blizzard sub-cluster attribution — this corroborates the AitM delivery layer only, not the actor binding.

## Technical detail

- **Access vector (new):** compromise of captive-portal / hospitality-Wi-Fi ecosystems worldwide; DNS/HTTP manipulation to redirect corporate travelers. This is a new infrastructure/targeting class for the actor.
- **Strand 1 — AitM credential/session theft:** doppelganger domains impersonating Microsoft online services (ms365-device.com, ms365-live.com, m365-owa.com, owa-ms365.com) abusing the **Entra ID device-code authentication flow**, leading to Entra device registration and M365 data collection. This is consistent with Midnight Blizzard's Storm-2372 device-code tradecraft tracked through 2025 (MITRE ATT&CK T1621 Multi-Factor Authentication Request Generation / device-code phishing).
- **Strand 2 — malware delivery:** payloads posing as browser/OS updates, triggered by browsers' automated captive-portal connectivity checks, using **ClickFix** (T1204 user execution via fake prompts). Android APK delivery also observed.
- **Tooling named by MSTIC (for actor-profiler, not atomic IOCs):** CornFlake (Golang Windows RAT — system enum, file/keystroke collection, credential + session-token theft, A/V surveillance, removable-media monitoring, remote shell), ChocoShell (PowerShell infostealer), FruitStone (C2 panel), plus an unnamed Android component.
- **AI augmentation:** MSTIC states a significant portion of the operation is AI-augmented.
- **Not Forest Blizzard:** MSTIC notes TTP similarity to the APT28 (Forest Blizzard, #006) DNS-hijacking op disclosed April 2026 but attributes CaptiveCrunch to Storm-2945 / Midnight Blizzard, NOT Forest Blizzard. Do not cross-walk.

## IOCs surfaced

All 12 indicators are net-new (not previously in _master-index.yaml). Collector extraction; hash->family bindings flagged best-effort pending full-appendix direct retrieval.

- Domains (AitM doppelganger, role delivery): ms365-device[.]com, ms365-live[.]com, m365-owa[.]com, owa-ms365[.]com
- IPv4 (C2): 31.57.243[.]154 (CornFlake/FruitStone), 38.146.28[.]75, 38.146.28[.]132, 104.194.159[.]150, 107.189.26[.]194, 213.145.86[.]112
- SHA-256 (delivery, malware posing as browser/OS update): 918fa52ae45ed60ba7cc8bdc99c3cbe9ab92e0375ec31fc05d0d4513be11c593, be99857449d2856dd5a84e21c8a3d5e0e01456adb44062ddec5a6b4970d8d42c
- Note: 31.57.243[.]154 is NOT the tracked 31.57.35.223 already in _master-index (different IOC).

## Relationship to existing findings

- Related to **finding-2026-07-14-0009** (ReliaQuest via BleepingComputer — Jalisco/OmegaLord M365 phishing kits defeating MFA via OAuth device-code abuse). Same broad TTP family (Entra device-code / OAuth AitM against M365); ReliaQuest's 2026-07-23 doppelganger-domain reporting referenced by MSTIC is the partial corroborator here. Distinct campaign/actor — do not merge.
- No prior CaptiveCrunch / Storm-2945 / captive-portal-APT29 coverage in corpus (collector anti-noise grep confirmed net-new). No existing APT29 finding in the last-30d window overlaps.

## A&D relevance

INDIRECT / STRUCTURAL. No named A&D prime or watchlist entity victim — targeting is corporate travelers generally. An ITAR/DIB executive transiting a compromised hotel or conference-venue Wi-Fi is within the plausible victim envelope (session-token / credential theft -> M365 access). FLASH Triggers 2 (new attribution) and 4 (TTP change) do not require an A&D victim; briefer to judge sector-section placement.

## Open questions for analyst

- **Attribution (SAT-ACH candidate):** The Storm-2945 -> Midnight Blizzard binding is single-source (MSTIC), assessed on overlap with Storm-2372. Weigh the competing hypotheses: (H1) genuine Midnight Blizzard sub-cluster; (H2) distinct actor MSTIC is over-clustering on shared device-code tradecraft; (H3) tradecraft convergence with Forest Blizzard (MSTIC explicitly distinguishes but flags similarity). Do NOT harden beyond MSTIC's stated confidence per Hard Rule 2 — Archimedes reports "per MSTIC," not "APT29 did this."
- **Corroboration watch:** if a second independent A/B source confirms the Storm-2945 -> Midnight Blizzard attribution, the single-source veto lifts and WEP can move toward "very likely" — re-grade on arrival.
- **Hash->family bindings** (CornFlake/ChocoShell) are collector best-effort; full MSTIC IOC appendix (additional URLs/filenames, Android APK hash) may exist beyond the partial WebFetch — direct-retrieval verification recommended before actor-profiler folds into APT29 iocs.yaml.
- **AI-augmentation claim** (Anthropic/OpenAI collaboration) is novel reporting worth noting but not independently verifiable from this single source.
