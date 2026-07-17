---
finding_id: finding-2026-07-17-0002
created_at: 2026-07-17T08:18:00-04:00
graded_by: grader
grading_run_id: morning-20260717-080000
grading_mode: scheduled_brief

# Core grading (from admiralty-grading skill output)
digraph: A2
source_reliability:
  grade: A
  source_name: Microsoft Security Research / Microsoft Defender Experts / MSTIC (Balaji Venkatesh S)
  source_yaml_id: mstic
  grade_rationale: >
    Pre-assigned A per source-grades.yaml (ratified). Nation-state + commodity-threat
    tracking backed by first-party Microsoft Defender EDR telemetry. Full RSS body
    retrieved this sweep; the atomic-IOC appendix (IPs/domains/hashes + KQL hunts)
    is NOT in the syndicated body and is flagged pending_direct_retrieval.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent           # ClickFix delivery, WebDAV+rundll32, MSHTA+PowerShell, steganography, browser-cred-store theft are all established, coherent techniques; ClickFix is a corpus-tracked cross-cutting TTP (finding-2026-07-16-0003 Sandworm)
    - probably_true_no_contradicting_ab       # no A/B-grade source contradicts; consistent with the documented ACR Stealer / Amatera rebrand infostealer family
    - probably_true_claims_coherent           # two intrusion chains internally coherent; first-party EDR-telemetry-backed observation window (late Apr - mid Jun 2026)
  grade_1_withheld_reason: >
    Grade 1 withheld: single evidence basis (MSTIC/Defender telemetry). No
    independent second research firm corroborating THIS campaign wave; the atomic
    IOC appendix that would enable cross-source technical matching is not in the
    syndicated body (pending_direct_retrieval). Family-level attribution only.
  rationale: >
    MSTIC reports increased ACR Stealer activity (late Apr - mid Jun 2026) across
    customer environments using ClickFix lures to steal browser credentials,
    auth/session tokens, and sensitive documents from enterprise environments. ACR
    Stealer is reportedly a malware-as-a-service infostealer associated with the
    rebranding of Amatera Stealer. Two intrusion chains: (1) WebDAV-based ClickFix
    with rundll32 DLL load + Python loaders + blockchain dead-drop C2; (2)
    MSHTA-initiated obfuscated PowerShell with steganography-assisted in-memory
    execution. Attribution is family-level (ACR Stealer), behavior + OSINT-infra
    corroborated — NO threat-actor / roster attribution (Hard Rule 2 preserved).
    First-party-telemetry-backed, coherent, consistent -> Probably True.
corroboration:
  independent_sources:
    - mstic
  independent: false
  independence_test_result: >
    Single directly-retrieved evidence basis (MSTIC Defender telemetry) for this
    campaign wave. ACR Stealer / Amatera is a documented family with prior OSINT
    coverage, but no independent second source corroborates THIS April-June wave or
    the two specific intrusion chains this pass. Remove MSTIC and no other retrieved
    source stands on its own for the campaign detail. Single effective source.
first_party_precedence:
  applied: false
  splunk_evidence: null
  splunk_note: >
    Rule 8 check RUN, not skipped. Queried index=defenseclaw_local OR index=archimedes
    over -30d for ACR Stealer / Amatera / google.ct / ClickFix / "conhost.exe --headless":
    4 hits, ALL Archimedes' own operational telemetry (FLASH-sweep event notes naming
    the ACR Stealer grader-queue handoff and ClickFix anti-noise holds). ZERO
    defenseclaw_local first-party target hits; defenseclaw_local_24h_ioc_hits = 0 in
    the 06:00 sweep. The MSTIC atomic IOC appendix (WebDAV host, C2 domains/IPs,
    blockchain resolver, payload SHA-256) is not yet in hand (pending_direct_retrieval),
    so there is no atomic indicator to match. Silent, not disconfirming; first-party
    precedence does not apply either way.
single_source_veto_applied: true
single_source_veto_note: >
  Applies — single effective evidence basis (MSTIC). WEP capped at "likely." Veto
  lifts on independent second research-firm corroboration of this ACR Stealer wave,
  or first-party defenseclaw_local telemetry matching the (pending) atomic IOC set.
wep_ceiling: likely

# Inclusion eligibility (from admiralty-grading)
inclusion:
  eligible_for:
    - daily_brief_monitoring        # A2 clears floors; TTP-proliferation / technique-watch monitoring item
    - weekly_synthesis
  not_eligible_for:
    - flash                         # NOT a FLASH trigger — confirmed at 00:00 flash eval (grader_queue_nonflash): commodity MaaS infostealer, family-level attribution only, no roster actor, no A&D nexus, no CVE, no CVSS 10.0. Fails all 6 triggers.
    - daily_brief_action            # A2 grade-eligible, but a cross-cutting TTP-awareness item, not a discrete action item
    - actor_profile_update          # NO roster actor — ACR Stealer is a commodity MaaS family, not a _roster.yaml actor (Hard Rule 2)

# Cluster metadata
cluster:
  topic: "MSTIC reports increased ACR Stealer (MaaS infostealer, Amatera rebrand) activity Apr-Jun 2026 using ClickFix lures to steal enterprise browser credentials/tokens/documents, via two intrusion chains (WebDAV+rundll32+blockchain C2; MSHTA+PowerShell+steganography). Family-level attribution only, no roster actor. Primary value: ClickFix TTP-proliferation tracking (now spans commodity MaaS + nation-state)."
  cluster_size: 1
  raw_signal_members:
    - raw-2026-07-17-am-003
  attribution_claims: []            # NONE at actor level. Family-level "ACR Stealer / Amatera rebrand" is malware-family, not a threat-actor attribution. Hard Rule 2: empty, not omitted.

# A&D relevance (structural — no A&D-specific victimology)
ad_relevance: medium
ad_relevance_rationale: >
  No A&D victim named and no roster actor. Relevance is STRUCTURAL: enterprise
  browser-credential / session-token / document theft applies to any large
  organization including A&D primes + Tier-1/2 suppliers. The primary analytic value
  is TTP-PROLIFERATION tracking — ClickFix as a delivery primitive now spans commodity
  MaaS (this finding) and nation-state (Sandworm/APT44, finding-2026-07-16-0003),
  reinforcing ClickFix as a cross-cutting technique defenders must cover regardless of
  attributed actor. Rated medium (not high): commodity MaaS, no targeting, atomic IOCs
  pending retrieval. Re-rate if an A&D victim or roster actor is named, or if the
  campaign is shown targeting DIB enterprises.

# TTP-tracking handoff
ttp_tracking_handoff:
  technique: ClickFix (user-executed paste-and-run lure -> LOLBin execution)
  proliferation_note: >
    ClickFix delivery now documented across BOTH commodity MaaS (ACR Stealer, this
    finding) and nation-state (Sandworm/APT44 fake-CAPTCHA PowerShell, finding-2026-07-16-0003).
    Track as a cross-cutting delivery primitive, not per-actor.
  behavioral_observables:
    - "WebDAV DLL load via rundll32 over HTTPS; GUID-style directories + legit-looking filenames (e.g. google.ct)"
    - "pushd-mounted WebDAV share; headless/obfuscated pushd via conhost.exe --headless with env-var obfuscation + delayed expansion"
    - "MSHTA-initiated obfuscated PowerShell; steganography-assisted in-memory execution"
    - "Browser-credential-store access; scheduled-task persistence; Python-based loaders"
  atomic_iocs_status: pending_direct_retrieval   # MSTIC blog IOC appendix (WebDAV host, C2 domains/IPs, blockchain dead-drop resolver, payload SHA-256) + KQL hunts not in the syndicated feed body
  enrichment_needed:
    - "Direct-retrieve the MSTIC blog to fold the atomic IOC appendix (WebDAV host, C2 domains/IPs, blockchain resolver, payload SHA-256) into the master IOC index + first-party sentinel set."
    - "Then re-run the Rule 8 first-party check against defenseclaw_local with the atomic indicators."

# Downstream handoff flags
analyst_review_required: true
analyst_review_note: >
  Flagged per the WEP-"likely" rule; LIGHT pass expected. No actor attribution (no ACH
  at actor level — family-level ACR Stealer only). Little SAT surface: the finding is a
  first-party-EDR-backed A-grade family-level campaign report. Load-bearing open items:
  (1) atomic IOCs are pending direct retrieval, so the technical layer is not yet
  complete; (2) A&D relevance is structural (no victim) — keep at monitoring/TTP-watch,
  do not overstate. The genuinely useful analytic thread is ClickFix TTP-proliferation
  (commodity MaaS + nation-state), which is a WATCH/synthesis theme, not a new claim.
red_team_review_required: false        # WEP ceiling "likely" < "very likely"; single-source veto binds. Red-team not mandatory. Unchanged post-KAC (WEP not raised).
red_team_review: null

# Analyst review outcome (KAC applied 2026-07-17)
analyst_review_complete: true
analyst_review_run_id: analyst-20260717-090000
sats_applied: [sat-kac]              # sat-ach not_applicable (family-level, no actor)
wep_ceiling_adjusted: likely         # unchanged — already capped by single-source veto
wep_ceiling_adjustment_reason: >
  No adjustment. KAC found no critical-centrality low-confidence assumption. Three
  QUALIFY caveats shape downstream CHARACTERIZATION, not the grade: (A2) the ClickFix
  TTP-proliferation framing is a legitimate watch theme but thin (two data points) and
  should not be overstated; (A3) the ACR->Amatera rebrand is incidental color, NOT
  load-bearing (finding stands if lineage is wrong); (A6) A&D relevance is GENERIC
  enterprise applicability, not A&D-specific. The Rule 8 0-hit result is a visibility-
  limited null (no atomic IOC to match), not evidence of absence.
assessment_blocked_pending_test: false   # atomic-IOC retrieval is enrichment, not a gate

analysis_sections:
  sat_ach:
    status: not_applicable
    reason: no_actor_attribution_claim
    detail: >
      Attribution is family-level only (ACR Stealer, reportedly an Amatera rebrand) —
      a malware-family label, not a threat-actor attribution. cluster.attribution_claims
      is empty at actor level. No competing roster-actor hypotheses exist to rank.
      Running ACH with a roster-actor H1 would originate attribution (Hard Rule 2).
      Not applied.
  sat_kac:
    kac_analysis:
      assessment_under_review: >
        "Increased ACR Stealer activity (late Apr - mid Jun 2026) using ClickFix lures
        and two LOLBin intrusion chains to steal enterprise credentials/tokens/documents;
        the PRIMARY analytic value is ClickFix TTP-proliferation tracking (now spanning
        commodity MaaS + nation-state); medium structural A&D relevance, monitoring/
        TTP-watch tier, graded A2 / likely."
      analyzed_at: 2026-07-17T09:20:00-04:00
      analyzed_by: analyst
      invoking_context: >
        Grader flagged analyst_review_required (WEP-"likely" rule). Light KAC pass —
        no actor attribution. Focus per orchestrator: interrogate the TTP-proliferation
        framing, whether the ACR->Amatera rebrand attribution is load-bearing, and the
        Rule 8 first-party null result.
      assumptions:
        - id: A1
          statement: "MSTIC's campaign characterization (two ClickFix->LOLBin chains, Apr-Jun 2026 window) is accurate"
          category: source_reliability
          stated: true
          why_must_be_true: "The finding's factual layer rests on the single first-party-EDR-backed source"
          when_could_be_false: "MSTIC mischaracterizes the chains, or the activity window/scope differs on direct blog retrieval"
          evidence_for: [raw-2026-07-17-am-003]
          evidence_against: []
          confidence: high
          centrality: material
          classification: sound
        - id: A2
          statement: "The 'primary value is ClickFix TTP-proliferation' framing is analytically load-bearing — ClickFix spanning commodity MaaS + nation-state is a meaningful proliferation signal"
          category: ttp_patterns
          stated: true
          why_must_be_true: "The finding elevates proliferation-tracking as its main contribution over the credential-theft facts"
          when_could_be_false: >
            ClickFix is one of the most widely adopted delivery techniques of 2024-2026;
            finding it in two reports (this + Sandworm finding-2026-07-16-0003) is closer
            to base-rate expectation than to a distinctive proliferation trend. Two data
            points is thin for a 'proliferation' claim — the technique's ubiquity may make
            'it appears across actor tiers' unremarkable rather than insightful.
          evidence_for: [raw-2026-07-17-am-003]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A3
          statement: "The ACR Stealer -> Amatera rebrand lineage is load-bearing to the finding"
          category: semantic
          stated: true
          why_must_be_true: "The finding foregrounds the family-level rebrand attribution"
          when_could_be_false: >
            Test by removal: if the ACR=Amatera rebrand claim were wrong, the finding's
            value (ClickFix delivery, LOLBin chains, enterprise credential theft, TTP
            proliferation) is UNCHANGED. The rebrand lineage is incidental color, not a
            pillar. MSTIC itself hedges ('reportedly,' 'associated with').
          evidence_for: [raw-2026-07-17-am-003]
          evidence_against: []
          confidence: low
          centrality: peripheral
          classification: sound
        - id: A4
          statement: "The atomic IOCs pending direct retrieval will complete the technical layer without contradicting the syndicated-body account"
          category: source_reliability
          stated: true
          why_must_be_true: "The finding's technical layer is explicitly incomplete pending the IOC appendix"
          when_could_be_false: "The blog IOC appendix diverges from the body, or the KQL hunts reframe the chains once retrieved"
          evidence_for: [raw-2026-07-17-am-003]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A5
          statement: "The defenseclaw_local 0-hit result is silent, not disconfirming (visibility-limited null)"
          category: visibility
          stated: true
          why_must_be_true: "The Rule 8 note relies on the null carrying no 'we are clean' weight"
          when_could_be_false: >
            n/a as framed — the null is correctly interpreted. Two reinforcing reasons the
            null is near-zero-weight: (1) atomic IOCs are pending, so the query had no
            malicious indicator to match; (2) the 4 hits returned were Archimedes' OWN
            operational telemetry, not target detections. Risk is a downstream reader
            misreading 0 hits as evidence of absence.
          evidence_for: []
          evidence_against: []
          confidence: high
          centrality: peripheral
          classification: sound
        - id: A6
          statement: "Medium A&D relevance is warranted via generic enterprise-credential-theft applicability"
          category: semantic
          stated: true
          why_must_be_true: "No A&D victim or roster actor is named; relevance rides on 'applies to any large org incl. A&D'"
          when_could_be_false: >
            This is GENERIC enterprise relevance, not A&D-SPECIFIC — it applies equally to
            any Fortune-500 target. That is legitimately weaker than victimology-backed
            relevance; medium is defensible precisely because it is generic, and should not
            be read as A&D targeting.
          evidence_for: [raw-2026-07-17-am-003]
          evidence_against: []
          confidence: medium
          centrality: material
          classification: qualify
        - id: A7
          statement: "The two observed intrusion chains are representative ACR Stealer TTPs, not one-off variants"
          category: ttp_patterns
          stated: false
          why_must_be_true: "TTP-watch value assumes the chains generalize beyond the specific intrusions MSTIC saw"
          when_could_be_false: "The chains are bespoke to a few intrusions and don't recur; commodity MaaS TTPs churn"
          evidence_for: [raw-2026-07-17-am-003]
          evidence_against: []
          confidence: medium
          centrality: peripheral
          classification: sound
      classifications_summary:
        sound: 4
        qualify: 3
        test: 0
        reject: 0
      remediation:
        status: proceed
        blocking_assumption: null
        qualifying_caveats:
          - "TTP-proliferation framing (A2) is a legitimate WATCH/synthesis theme but should not be overstated as a novel signal — ClickFix is already ubiquitous, and two data points (ACR + Sandworm) is thin. Frame as 'ClickFix confirmed across actor tiers,' not 'proliferating.'"
          - "The ACR->Amatera rebrand (A3) is INCIDENTAL color, not load-bearing; the finding stands unchanged if the lineage is wrong. Do not let family-lineage detail crowd out the credential-theft substance."
          - "The defenseclaw_local 0-hit result (A5) is a visibility-limited null (no atomic IOC to match; the 4 hits were Archimedes' own telemetry) — do NOT imply the target is unaffected."
          - "A&D relevance (A6) is GENERIC enterprise applicability, not A&D-specific; medium is right, but the brief must not imply A&D targeting."
        next_action: >
          Proceed at monitoring/TTP-watch tier. No test blocks publication — the atomic-IOC
          retrieval is enrichment (already flagged) and, for a monitoring-tier commodity-MaaS
          finding, not a gate. Re-run the Rule 8 check once atomic IOCs are in hand.
      recommended_wep_after_test:
        no_change: likely
        note: >
          WEP already correctly capped at "likely" by the single-source veto. KAC surfaces
          no critical assumption; the strongest QUALIFY items (proliferation framing,
          rebrand-incidental, generic relevance) shape how the finding is CHARACTERIZED
          downstream, not the grade. No WEP change.

# Lifecycle
tlp: CLEAR
published_in_briefs: [2026-07-17-morning]
retracted: false
retraction_brief_id: null
---

# MSTIC: increased ACR Stealer activity uses ClickFix lures and two LOLBin intrusion chains to steal enterprise credentials

## Summary

Microsoft Defender Experts / MSTIC observed increased ACR Stealer activity from
late April to mid-June 2026 across customer environments, using ClickFix lures to
steal browser credentials, authentication/session tokens, and sensitive documents
from enterprise environments. ACR Stealer is reportedly a malware-as-a-service
infostealer associated with the rebranding of Amatera Stealer. MSTIC documents two
intrusion chains, both beginning with ClickFix: (1) a WebDAV-based chain where a
ClickFix prompt leads to `cmd.exe` then `rundll32.exe` loading a DLL from a remote
WebDAV share over HTTPS, with Python loaders and some intrusions using blockchain-
backed dead-drop C2 resolution; and (2) an MSHTA-initiated, more fileless chain
using obfuscated PowerShell and steganography-assisted in-memory execution.
Attribution is family-level (ACR Stealer) based on behavior plus OSINT
infrastructure analysis — no threat-actor / roster attribution (Hard Rule 2).

The primary analytic value is TTP-proliferation tracking: ClickFix as a delivery
primitive now spans commodity MaaS (this campaign) and nation-state activity
(Sandworm/APT44, finding-2026-07-16-0003). Graded A2 / "likely" with the single-
source veto applied — MSTIC is the sole effective evidence basis, and the atomic
IOC appendix is not in the syndicated feed body (pending direct retrieval). This is
a monitoring / technique-watch item, not a FLASH item — a disposition the 00:00
FLASH evaluation already reached before routing it to the grader queue.

## Sources

### Microsoft MSTIC / Defender Experts (mstic, digraph letter: A) — primary, first-party EDR telemetry

- URL: https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/
- Published: 2026-07-16T23:12:02Z (Microsoft Security Research + Balaji Venkatesh S)
- Key claim: Increased ACR Stealer activity (late Apr - mid Jun 2026) using ClickFix
  lures and two LOLBin intrusion chains to steal enterprise credentials/tokens/documents;
  family-level attribution, no actor.

## Technical detail

- **Malware family:** ACR Stealer (reportedly MaaS; associated with the rebranding of
  Amatera Stealer). Family-level attribution only.
- **Delivery:** ClickFix lures (likely malvertising / SEO-poisoned results).
- **Campaign 1 (WebDAV):** ClickFix prompt -> `cmd.exe` -> `rundll32.exe` loads a DLL
  from a remote WebDAV share over HTTPS. WebDAV path uses GUID-style directories +
  legit-looking filenames (e.g., `google.ct`). Three initial-execution variants: direct
  `rundll32`; `pushd`-mounted WebDAV share; headless/obfuscated `pushd` via
  `conhost.exe --headless` with env-var obfuscation + delayed expansion. Python loaders
  + persistence; some intrusions use blockchain-backed dead-drop C2 resolution.
- **Campaign 2 (MSHTA):** more fileless — MSHTA + obfuscated PowerShell +
  steganography-assisted in-memory execution.
- **Objective (both):** steal browser-stored credentials and other sensitive data for
  exfiltration.
- **Hard Rule 3:** execution chains described at capability level only; no runnable
  commands/payloads reproduced. The `google.ct` masquerade filename and the
  `rundll32`/`pushd`/`conhost --headless`/MSHTA sequence are detection observables.
- **Defender coverage:** MSTIC provides behavioral coverage + hunting for LOLBin
  execution, suspicious WebDAV/MSHTA activity, obfuscated PowerShell, scheduled-task
  persistence, in-memory execution, and browser-credential-store access.

## IOCs surfaced

Atomic network IOCs are NOT in the syndicated feed body (pending_direct_retrieval).
Only a masquerade-filename observable + behavioral TTP observables were captured:

```yaml
indicators:
  - type: file_path
    value: google.ct
    role: delivery
    campaign: "ACR Stealer Campaign 1 (WebDAV/ClickFix)"
    related_malware: [ACR Stealer, Amatera Stealer]
    notes: "Masquerade filename observable, not a full path/hash. Atomic WebDAV host + C2 domains/IPs + payload hashes are in the MSTIC blog IOC appendix — pending_direct_retrieval."
behavioral_detection_observables:
  - "WebDAV DLL load via rundll32 over HTTPS; GUID-style dirs + legit-looking filenames"
  - "pushd-mounted WebDAV share; conhost.exe --headless obfuscated pushd"
  - "MSHTA -> obfuscated PowerShell -> steganography-assisted in-memory execution"
  - "Browser-credential-store access; scheduled-task persistence; Python loaders"
atomic_iocs_status: pending_direct_retrieval
first_party_hits: none   # defenseclaw_local -30d: 0; no atomic IOC yet to match
```

## Relationship to existing findings

- **ClickFix TTP-proliferation continuity with finding-2026-07-16-0003** (CERT-UA /
  Sandworm-APT44 ClickFix fake-CAPTCHA PowerShell, Ukraine). This finding documents
  the SAME delivery primitive (ClickFix) in a DIFFERENT context — commodity MaaS
  infostealer rather than nation-state. Not the same campaign or actor; the shared
  thread is the technique. Track ClickFix as a cross-cutting primitive.
- No IOC or actor overlap with any current finding; no roster actor to link.

## Open questions for analyst

- **Atomic IOCs pending.** The MSTIC blog carries an IOC appendix (WebDAV host, C2
  domains/IPs, blockchain dead-drop resolver, payload SHA-256) + KQL hunts not in the
  feed body. Direct retrieval is needed to complete the technical layer and to re-run
  the Rule 8 first-party check against `defenseclaw_local` with real indicators.
- **A&D relevance stays structural.** No victim, no roster actor — keep at medium and
  monitoring/TTP-watch tier. Do not imply A&D targeting.
- **ClickFix proliferation is the synthesis theme.** The cross-cutting spread of
  ClickFix (commodity MaaS + nation-state) is a watch/weekly-synthesis thread, not a
  new asserted claim here.

## Analytic notes (from analyst review)

KAC (no ACH — no actor attribution) confirms the A2/likely grade and surfaces three
characterization caveats, none grade-changing. First, interrogate the headline
framing: "primary value is ClickFix TTP-proliferation." ClickFix is already one of
the most common delivery techniques of the period, so seeing it in both a commodity
MaaS report and a Sandworm report is closer to base-rate than to a distinctive
trend. It is a legitimate weekly-synthesis WATCH thread — but "confirmed across
actor tiers" is the honest framing, not "proliferating." Two data points is thin.

Second, the ACR Stealer -> Amatera rebrand attribution is incidental, not
load-bearing: remove it and the finding (ClickFix delivery, LOLBin chains,
enterprise credential theft) is unchanged. Don't let family-lineage color crowd out
the substance. Third, the defenseclaw_local 0-hit result is a visibility-limited
null — atomic IOCs are pending so there was nothing to match, and the 4 returned
hits were Archimedes' own operational telemetry, not target detections. It must not
read as "we're clean." A&D relevance is generic-enterprise, not A&D-specific; medium
is right. WEP stays "likely" (veto-capped); atomic-IOC retrieval is enrichment, not
a gate.
