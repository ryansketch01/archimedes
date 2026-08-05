---
finding_id: finding-2026-08-04-0001
created_at: 2026-08-04T20:52:00-04:00
graded_by: grader
grading_run_id: ondemand-investigate-20260804-greatness
grading_mode: on_demand

# Core grading (from admiralty-grading skill output)
digraph: B2
source_reliability:
  grade: B
  source_name: The Hacker News (Aug 2026) reporting Greatness PhaaS device-code/AiTM capability expansion
  source_yaml_id: thehackernews
  grade_rationale: >
    Anchored at B (provisional per source-grades.yaml, 2026-05-14) — the source Archimedes
    holds for the DISTINGUISHING/novel element of the claim (Greatness NOW added OAuth
    device-code phishing + expanded to iCloud/Yahoo/Google Workspace). The foundational
    platform-is-AiTM-PhaaS element is independently corroborated by a higher grade (Cisco
    Talos, A, originating 2023 documentation) and by ANY.RUN (provisional B, 2026 overview),
    but neither of those documents the new device-code addition — so the conservative letter
    for the graded claim as framed is B (the carrier of the novel element). Letter is not
    lifted to A on Talos's foundational corroboration.
  provisional: false
credibility:
  grade: 2
  checklist_passed:
    - probably_true_ttp_consistent          # Greatness already runs reverse-proxy AiTM (Talos 2023, ANY.RUN 2026); adding OAuth 2.0 Device Authorization Grant abuse (T1621) + OAuth consent abuse is a natural, in-character PhaaS evolution; device-code phishing is an established, well-documented M365/Entra technique
    - probably_true_no_contradicting_ab      # no A/B-grade source contradicts
    - probably_true_claims_coherent          # OAuth 2.0 device authorization grant is real; T1557 (AiTM) / T1539 (session cookie theft) / T1621 (MFA request generation) are real ATT&CK techniques; PRT minting via rapid device registration is a real Entra persistence mechanism; multi-stage redirect + Cloudflare challenge-gate anti-analysis is corroborated by the urlscan IOC captures
  grade_1_withheld_reason: >
    Grade 1 withheld — the DISTINGUISHING claim (Greatness NOW supports device-code phishing +
    expanded to iCloud/Yahoo/Google Workspace, Aug 2026) rests on a single originating primary
    (The Hacker News). Cisco Talos (A, 2023) and ANY.RUN (B, Jun 2026) independently corroborate
    the FOUNDATION (Greatness is a commodity AiTM PhaaS platform vs M365) but predate and do NOT
    document the new device-code capability — so there is no independent A/B corroboration of the
    element that makes this claim novel. Err low -> 2.
  rationale: >
    Probably True. Greatness is a well-established commodity PhaaS platform (originating Cisco
    Talos documentation May 2023; ANY.RUN overview Jun 2026) that relays victims through the real
    Microsoft login via reverse-proxy AiTM to capture the live post-MFA session cookie. The Aug
    2026 reporting (The Hacker News) that it has added OAuth 2.0 Device Authorization Grant abuse
    (device-code phishing), OAuth consent abuse, and expanded beyond M365 to iCloud/Yahoo/Google
    Workspace is single-source but squarely consistent with the platform's existing tradecraft and
    with established M365/Entra device-code technique. Two published affiliate phishing domains are
    independently corroborated (VT 6 engines on the base domain aitomayu[.]com; urlscan confirms two
    live [target]-[token] affiliate subdomains, Jun 2026), which grounds the platform-is-operating
    facts even though the atomic IP indicator is only weakly corroborated (grade-down below).
corroboration:
  independent_sources:
    - thehackernews            # B — primary carrier of the novel device-code/expansion element (Aug 2026)
  partial_corroboration:
    - source: cisco-talos
      grade: A
      scope: "Originating documentation (May 2023) of Greatness as a reverse-proxy AiTM MFA-bypass PhaaS platform vs M365 — corroborates the FOUNDATION (platform exists, does AiTM session-cookie theft), NOT the Aug-2026 device-code addition."
    - source: anyrun
      grade: B
      provisional: true
      scope: "Platform overview (Jun 2026) — subscription model, affiliate tooling, AiTM mechanism, aitomayu[.]com operator base domain. Corroborates the FOUNDATION, not the new device-code capability."
    - source: virustotal
      grade_facts: B
      scope: "aitomayu[.]com flagged malicious 6/91 engines (facts) — corroborates the base domain is malicious Greatness infrastructure. Dual-grade: attribution F (VT cannot attribute)."
    - source: urlscan
      grade_facts: B
      scope: "Two live Greatness affiliate subdomains captured Jun 2026 (Cloudflare-fronted, 'Just a moment...' challenge gate matching reported anti-analysis behavior). Facts B; attribution F."
  independent: false
  independence_test_passed: >
    FAILS on the graded claim as framed — remove The Hacker News and the NOVEL element
    (device-code addition + iCloud/Yahoo/Google Workspace expansion, Aug 2026) does not stand;
    Talos (2023) and ANY.RUN (Jun 2026) predate it and never made that claim. One effective
    evidence basis on the novel element. NOTE: the FOUNDATION (Greatness = commodity AiTM PhaaS
    vs M365) IS independently corroborated (Talos A + ANY.RUN B, different orgs / different
    evidence bases / neither cites the other) and the two affiliate domains are technically
    corroborated (VT + urlscan) — the veto binds on the novel capability, not the platform's
    existence.
first_party_precedence:
  applied: false
  splunk_evidence: >
    Grader independently re-ran the Hard Rule 8 sweep -30d across both indices (confirming the
    recorded raw-signal sweep): defenseclaw_local 0 hits for Greatness / aitomayu[.]com /
    38.248.95[.]214 / gr8managerbot / device-code. archimedes index returned 1 event matching only
    the generic phrase "device code" — resolved to Archimedes's own archimedes:operation self-log
    (prior device-code findings: CaptiveCrunch 0002 / Jalisco-OmegaLord 0009), NOT an environmental
    detection; the Greatness-specific narrowed query returned 0. Clean. Silence is not
    disconfirmation (visibility-bounded on defenseclaw_local; absence of evidence != evidence of
    absence).
single_source_veto_applied: true
single_source_veto_note: >
  Veto applied on the novel capability/tooling claim — single effective evidence basis
  (The Hacker News) for the Aug-2026 device-code addition + provider expansion. Capability/tooling
  claim, not attribution — veto still caps WEP at "likely" regardless of the B-grade foundation's
  A-grade partial corroboration.
wep_ceiling: likely
wep_ceiling_rationale: >
  "Likely," capped by the single-source veto on the novel element. B2 would otherwise permit
  "very likely (with corroboration) / likely"; the device-code addition is single-source so it
  cannot exceed likely. This is a TTP-awareness / detection-hardening item on commodity tooling.
  A&D nexus is STRUCTURAL — M365/Entra ID is the dominant identity + collaboration fabric across
  the DIB; commodity AiTM + device-code MFA-bypass + PRT minting is a directly portable TTP against
  A&D-prime tenants. No named A&D victim, no threat-actor attribution (Hard Rule 2).

# Cluster metadata
cluster:
  topic: "Greatness PhaaS adds OAuth device-code phishing + OAuth consent abuse to its reverse-proxy AiTM M365 credential/session-token-theft platform; expands beyond M365 to iCloud/Yahoo/Google Workspace; sold as commodity subscription tooling (The Hacker News; platform per Cisco Talos 2023 + ANY.RUN 2026)"
  cluster_size: 1
  raw_signal_members:
    - raw-2026-08-04-ondemand-001
  attribution_claims: []       # NONE — commodity PhaaS platform, no threat-actor attribution to inherit. Hard Rule 2 preserved. Greatness/aitomayu are tooling/infrastructure, not an actor.

# Inclusion eligibility (from admiralty-grading + operator direction)
inclusion:
  eligible_for:
    - daily_brief_monitoring     # TTP-awareness / detection-hardening item; high structural A&D M365-identity relevance
    - weekly_synthesis           # C3+ threshold met (B2); M365-identity relevance
    - threat_detection_weekly    # operator-directed — M365/Entra device-code + new-device-registration detection value; behavioral-detection focus over static IOCs
  not_eligible_for:
    - flash                      # NON-FLASH — clears no FLASH trigger (no CVE, no tracked-actor attribution, no first-party hit, no named A&D victim, documented commodity tooling). Grade B2 meets the flash threshold but no trigger fired.
    - daily_brief_action         # not an action item — no CVE/patch, no first-party detection, no named victim; awareness/hardening only
    - actor_profile_update       # no actor attributed (Hard Rule 2) — nothing for actor-profiler to fold in

# Downstream handoff flags
analyst_review_required: true    # WEP ceiling "likely" (>= likely) — LIGHT review; no attribution, no ACH needed
analyst_review_note: >
  LIGHT. No attribution (commodity PhaaS — do NOT bind to any actor, incl. the related APT29/Storm-2945
  and Jalisco/OmegaLord findings). Ensure the brief/synthesis: (1) presents this as single-source
  (The Hacker News) TTP-awareness on the NEW device-code capability, with the platform foundation
  corroborated by Talos + ANY.RUN; (2) surfaces the detection/hardening levers — block OAuth device-code
  authentication via Conditional Access, restrict OAuth Device Authorization grants, cut Entra
  device-registration limits, alert on new-device registration + rapid PRT issuance + mailbox-forwarding
  rule creation, monitor OAuth consent grants; (3) frames A&D nexus as structural M365/Entra TTP-class,
  no named victim. KAC on the "commodity tooling, not targeted campaign" framing is optional/light.
red_team_review_required: false  # WEP ceiling "likely", not >= "very likely"
red_team_review: null
analysis_sections:
  sat_ach: null
  sat_kac: null

# Source-grade notes (librarian awareness)
source_grade_additions_proposed:
  - source_yaml_id: anyrun
    proposed_name: "ANY.RUN (Threat Intelligence / interactive sandbox)"
    proposed_grade: B
    provisional: true
    awaiting_direct_retrieval: true
    dual_grade: null
    grade_note: >
      First Archimedes-corpus citation via finding-2026-08-04-0001 (Greatness PhaaS overview, Jun 2026).
      ANY.RUN is an established interactive-malware-sandbox + threat-intelligence vendor with named
      published research and first-party sandbox-detonation telemetry. Provisional B is the conservative
      starting grade for a first-surface reputable vendor per the same precedent as Sysdig (2026-05-14),
      Socket (2026-05-14), ReliaQuest (2026-07-14). Cited here as a FOUNDATION corroborator (platform
      exists + does AiTM), not the novel-element carrier. Operator may upgrade to A on subsequent surfaces
      showing consistent telemetry-backed rigor, or hold at B. Primary retrieved via Medium post; direct
      ANY.RUN TI portal not retrieved this pass.
    first_cited: finding-2026-08-04-0001
source_grade_notes:
  - source_yaml_id: thehackernews
    status: "Already provisional B in source-grades.yaml (2026-05-14, awaiting ratification). No new action; anchored the novel-element grade here."
  - source_yaml_id: cisco-talos
    status: "Already provisional A in source-grades.yaml (2026-05-14, awaiting ratification). Cited as originating-documentation (2023) FOUNDATION corroborator only."

# IOC handoff (dual-graded technical corroboration; see IOCs surfaced)
ioc_grading:
  - value: "aitomayu[.]com"
    type: domain
    confidence: corroborated
    grade_note: "VT 6/91 malicious (facts B) + urlscan 2 live affiliate subdomains (facts B). Durable pivot — Greatness operator base domain; affiliate pages are [target]-[token].aitomayu[.]com."
  - value: "solutionsonline-pyi5c7omq.aitomayu[.]com"
    type: domain
    confidence: corroborated
    grade_note: "urlscan live capture 2026-06-19 (facts B). Cloudflare-fronted challenge gate matches reported anti-analysis behavior. Shares affiliate token 'pyi5c7omq'."
  - value: "napierparkglobal-pyi5c7omq.aitomayu[.]com"
    type: domain
    confidence: corroborated
    grade_note: "urlscan live capture 2026-06-18 (facts B). Same 'pyi5c7omq' affiliate token + Cloudflare front."
  - value: "38.248.95[.]214"
    type: ipv4
    confidence: weakly_corroborated
    grade_note: "GRADED DOWN — VT 1/91 (GreyNoise only), 55 harmless, Limestone Networks (AS46475). Likely scanner noise / thin confirmation. Do NOT hard-blocklist on this evidence alone. Reported (The Hacker News) as AiTM proxy infra; treat as low-confidence pending stronger corroboration."

# Vuln-tracker handoff
vuln_tracker_handoff:
  proposed: false
  note: "No CVE — technique abuse (OAuth 2.0 Device Authorization Grant) + commodity tooling, not a product vulnerability. No vuln-tracker action."

# Lifecycle
tlp: CLEAR
published_in_briefs: []
retracted: false
retraction_brief_id: null
---

# Greatness PhaaS adds OAuth device-code phishing and AiTM session-token theft to its commodity Microsoft 365 credential-theft platform, expanding beyond M365 to iCloud, Yahoo, and Google Workspace

## Summary

The Greatness Phishing-as-a-Service platform — first documented by Cisco Talos in May 2023 and sold as a subscription (~$289/mo) via public Telegram — has added OAuth 2.0 Device Authorization Grant abuse (device-code phishing) and OAuth consent abuse to its existing reverse-proxy adversary-in-the-middle (AiTM) toolkit, per The Hacker News (Aug 2026). Greatness relays victims through the real Microsoft login and captures the live session cookie after a genuine MFA exchange; the new device-code path silently mints tokens to bypass MFA from a shared operator backend, and coverage has expanded beyond Microsoft 365 to iCloud, Yahoo, and Google Workspace. The device-code addition is single-source (The Hacker News), so the single-source veto caps this at "likely"; the platform foundation and AiTM mechanism are independently corroborated by Cisco Talos (2023) and ANY.RUN (2026), and two live affiliate phishing domains are technically corroborated (VirusTotal + urlscan). This is commodity criminal tooling with no threat-actor attribution — the same device-code/OAuth-AiTM technique family that nation-state and other criminal operators also use, but it is NOT bound to any of them.

## Sources

### The Hacker News (thehackernews, digraph: B) — primary, novel element

- URL: https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html
- Published: 2026-08-01
- Key claim: Greatness added device-code phishing (OAuth 2.0 Device Authorization Grant abuse) + OAuth consent abuse and expanded beyond M365 to iCloud/Yahoo/Google Workspace, all from one operator panel.

### Cisco Talos (cisco-talos, digraph: A) — originating documentation, foundation corroborator

- URL: https://blog.talosintelligence.com/state-of-the-art-phishing-mfa-bypass/
- Published: 2023-05
- Key claim: Originating documentation of Greatness as a reverse-proxy AiTM MFA-bypass PhaaS platform against Microsoft 365 (foundation only — predates the device-code addition).

### ANY.RUN (anyrun, provisional B) — platform overview, foundation corroborator

- URL: https://medium.com/@anyrun/greatness-phaas-overview-60776ac601b7
- Published: 2026-06
- Key claim: Platform overview — subscription model, affiliate tooling, AiTM mechanism, aitomayu[.]com operator base domain (foundation only).

## Technical detail

- **Platform / business model:** Commodity PhaaS in the wild since ~2022; subscription (~$120/mo at launch, raised to ~$289/mo Jan 2024) sold via public Telegram (`@GreatnessPage`, licensing via `@gr8managerbot`). Lowers the skill floor: attachment builder, prefilled-target lures, brand-accurate M365 clone pages, Telegram capture notifications.
- **Core mechanism (Talos 2023, ANY.RUN 2026):** Reverse-proxy **AiTM** (MITRE ATT&CK **T1557**) relaying the victim through the real Microsoft login to capture the **live session cookie after a genuine MFA exchange** (**T1539** steal web session cookie). Standard MFA does not stop it.
- **New capability (The Hacker News, Aug 2026):** **OAuth 2.0 Device Authorization Grant** abuse — device-code phishing (**T1621** MFA request generation) to silently mint tokens and bypass MFA — plus **OAuth consent abuse**. Expanded from M365 to **iCloud, Yahoo, Google Workspace**.
- **Delivery + evasion:** HTML attachments with obfuscated JS; PDF/QR lures; fake shared-document / RingCentral voicemail notifications; ~5-stage redirect chain with User-Agent fingerprinting, IP filtering against researchers/sandboxes, and CAPTCHA / Cloudflare "Just a moment..." gating (the last corroborated by the urlscan captures below). Static IOCs age fast (server-side API-key validation, decoy pages).
- **Post-compromise:** device registration within minutes to mint **Primary Refresh Tokens (PRTs)** for persistence; delayed inbox/mailbox-forwarding-rule manipulation to suppress alerts; internal phishing from compromised accounts.
- **Targeting (reported):** organizations using M365 in the US/Canada/UK/Australia/South Africa; victim sectors incl. manufacturing, healthcare, technology, education, real estate, construction, finance, business services. **No named A&D-prime victim** in the reporting.

## IOCs surfaced

Behavioral detection is emphasized over atomic indicators (server-side key validation, decoy pages, fast infra rotation). The base domain + `[target]-[token]` subdomain pattern are the durable pivots; the specific IP is low-confidence.

- **domain — aitomayu[.]com** — Greatness operator base domain (ANY.RUN). Affiliate pages are `[target]-[token].aitomayu[.]com`. **VT 6/91 malicious** (BitDefender, ESET, Sophos, G-Data, Webroot, CRDF); registered 2024-03-28. Confidence: **corroborated** (VT facts B + urlscan). Durable pivot.
- **domain — solutionsonline-pyi5c7omq.aitomayu[.]com** — Greatness affiliate phishing subdomain (urlscan 2026-06-19), Cloudflare-fronted (172.67.219.201), "Just a moment..." challenge gate; affiliate token `pyi5c7omq`. Confidence: **corroborated** (urlscan facts B).
- **domain — napierparkglobal-pyi5c7omq.aitomayu[.]com** — Greatness affiliate phishing subdomain (urlscan 2026-06-18), same `pyi5c7omq` token + Cloudflare front. Confidence: **corroborated** (urlscan facts B).
- **ipv4 — 38.248.95[.]214** — reported (The Hacker News) as AiTM proxy infrastructure. **GRADED DOWN / weakly corroborated** — VT 1/91 (GreyNoise only), 55 harmless, Limestone Networks (AS46475). Likely scanner noise; **do NOT hard-blocklist on this evidence alone.**
- Context (not indicators): Telegram handles `@GreatnessPage`, `@gr8managerbot` (operator channels).

## Relationship to existing findings

Same **device-code / OAuth AiTM** technique family as two existing findings — cited as RELATED, explicitly **NOT merged and NOT cross-attributed** (Hard Rule 2):

- **finding-2026-07-31-0002** (CaptiveCrunch / Storm-2945, assessed Midnight Blizzard / APT29 per MSTIC) — the **nation-state** expression of the same Entra device-code / OAuth AiTM tradecraft. Greatness is the **commodity / PhaaS** expression. Distinct actor class; do not conflate.
- **finding-2026-07-14-0009** (ReliaQuest — Jalisco / OmegaLord M365 OAuth device-code phishing kits) — **sibling commodity tooling** in the same broad TTP family. Distinct tooling; do not merge.

Together these three findings trace the corpus's M365/Entra device-code threat surface across nation-state (APT29) and commodity-criminal (Greatness, Jalisco/OmegaLord) tiers — the technique is converging across the threat landscape, which is itself the analytic signal.

## A&D relevance

INDIRECT / STRUCTURAL. No named A&D prime or watchlist entity victim. M365/Entra ID is the dominant identity + collaboration fabric across the defense industrial base, so commodity AiTM + device-code MFA-bypass + PRT-minting persistence is a directly portable TTP against A&D-prime tenants and their Tier-1/2 supplier networks. The value is defensive-posture and detection-engineering, not a specific active campaign against the target profile.

## Open questions for analyst

- **Single-source novel element:** the Aug-2026 device-code addition + provider expansion is The Hacker News only; the platform foundation is Talos + ANY.RUN corroborated. Present the new capability as single-source TTP awareness. If a second independent A/B source confirms the device-code addition, the veto lifts and WEP can move toward "very likely" — re-grade on arrival.
- **Detection > IOCs:** atomic indicators age fast by design. The durable detection value is behavioral — M365/Entra OAuth device-code authentication events, new-device registration + rapid PRT issuance, mailbox-forwarding-rule creation, and OAuth consent grants — not the atomic domain/IP list. Threat-detection-weekly should lead with those.
- **No attribution:** commodity PhaaS — do NOT bind Greatness to APT29/Storm-2945, Jalisco/OmegaLord, or any actor. Record only what the sources state (a subscription tool with unknown affiliate operators).
- **Weak IP indicator:** 38.248.95[.]214 is 1-engine (GreyNoise) corroboration only — flag as low-confidence, not for blocklisting.
</content>
</invoke>
