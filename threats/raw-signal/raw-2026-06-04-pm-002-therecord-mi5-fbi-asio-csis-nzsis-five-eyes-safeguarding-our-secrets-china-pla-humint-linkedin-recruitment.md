---
raw_id: raw-2026-06-04-pm-002-therecord-mi5-fbi-asio-csis-nzsis-five-eyes-safeguarding-our-secrets-china-pla-humint-linkedin-recruitment
collected_at: 2026-06-04T15:45:00-04:00
run_id: pre-brief-20260604-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mi5-fbi-asio-csis-nzsis-joint                # Joint Five Eyes counterintelligence advisory — NEW source-id candidate (would need source-grade-log entry; conservative A grade per government-CERT precedent + five-service joint authorship)
  source_name: "Five Eyes joint advisory — 'Safeguarding Our Secrets' (MI5, FBI, ASIO, CSIS, NZSIS)"
  source_url: https://www.mi5.gov.uk/sites/default/files/2026-06/SAFEGUARDING%20OUR%20SECRETS%20PUBLICATION.pdf
  published_at: 2026-06-04T00:00:00-04:00
source_grade: A_provisional_new_source_id   # Five Eyes joint counterintelligence advisory — A grade procedurally per the same precedent as CISA / NSA / FBI Flash; new source-id pending source-grade-log entry
additional_sources:
  - source_yaml_id: the-record
    source_name: "The Record — 'Five Eyes warns Chinese spies are using job sites to recruit insiders'"
    source_url: https://therecord.media/five-eyes-warns-chinese-spies-are-using-job-sites-to-recruit-insiders
    published_at: 2026-06-04T00:00:00-04:00
    source_grade: B_provisional
    role: relay
date: 2026-06-04
topic: five-eyes-joint-advisory-china-pla-military-intelligence-humint-recruitment-linkedin-front-companies-virtual-interviews-cleared-personnel-indo-pacific-stationed-military
match_reason:
  watchlist: []                                          # No A&D-watchlist entity directly named. DIB cleared-personnel are within "anyone with access to classified or privileged information" scope but no A&D prime / aerospace / defense company is named in the advisory.
  actors: []                                             # Generic PLA / Chinese military intelligence attribution — no specific roster actor (Volt Typhoon, Salt Typhoon, APT40, APT41 all PLA-attributed but none named in this advisory).
  vulnerabilities: []
  keywords:
    - "Five Eyes"
    - "Safeguarding Our Secrets"
    - "MI5"
    - "FBI"
    - "ASIO"
    - "CSIS"
    - "NZSIS"
    - "China"
    - "Chinese military intelligence services"
    - "PLA"
    - "HUMINT recruitment"
    - "LinkedIn"
    - "front companies"
    - "virtual interviews"
    - "cleared personnel"
    - "Indo-Pacific"
    - "insider threat"
    - "counterintelligence"
triage_tags: [pm_pre_brief, counterintelligence_advisory, china_pla_attribution_generic, humint_not_cyber, cleared_personnel_target_set_implicit_dib_scope, joint_intelligence_service_a_grade, ad_sector_implicit_not_explicit, no_specific_tracked_actor]
iocs_extracted: false                                    # HUMINT advisory; no cyber-IOCs by definition. Operational artifacts (LinkedIn behavior patterns, front-company indicators) are tradecraft-recognition not IOC-class.
iocs_count: 0
text_word_count: ~520
promoted: true
promoted_to_finding: finding-2026-06-04-0002-mi5-fbi-asio-csis-nzsis-the-record-five-eyes-joint-advisory-safeguarding-our-secrets-china-pla-humint-recruitment-linkedin-cleared-personnel
promoted_at: 2026-06-04T16:24:00-04:00
promoted_by_grading_run_id: afternoon-20260604-160000
ttl_expires_at: 2026-09-02T15:45:00-04:00
---

# Five Eyes joint advisory — "Safeguarding Our Secrets" — Chinese PLA military intelligence HUMINT recruitment via LinkedIn, front companies, and virtual interviews; cleared-personnel target set

A joint advisory titled **"Safeguarding Our Secrets"** was published 2026-06-04 by the five Five Eyes counterintelligence services — **MI5** (UK), **FBI** (US), **ASIO** (Australia), **CSIS** (Canada), and **NZSIS** (New Zealand). The advisory was released as a PDF hosted on mi5.gov.uk and reported by The Record from Recorded Future News (Jun 4, 2026 18:04 UTC = 14:04 EDT, in-window). MI5 named as the lead agency.

The advisory warns that **"China's military intelligence services"** are conducting HUMINT recruitment operations against personnel in Five Eyes nations who hold security clearances or have access to "classified or privileged information." The target scope is broader than government / military employees and explicitly includes:

- Government and military personnel.
- **Indo-Pacific stationed military personnel** (named verbatim in the advisory per The Record relay).
- Academics, journalists, think-tank staff (cited as targets with "indirect or peripheral access" to privileged information).
- Anyone with "direct or indirect access to privileged information."

The advisory hedges that targets "may not necessarily be 'classified'" but possess valuable "insights and network of contacts."

## Named tradecraft

- **LinkedIn** (primary platform — named explicitly).
- Generic job-advertisement platforms.
- **Front companies** posing as private consultancies, think tanks, or human resources firms.
- Virtual interviews with role-and-unit probing questions.
- Encrypted-messaging-app transitions (off LinkedIn after initial contact).
- Payment via unconventional methods ($100s–$1000s per intelligence report).

## Attribution layer

**Five Eyes attribution language verbatim:** *"China's military intelligence services"* — phrasing connotes PLA-linked (military intelligence apparatus) rather than civilian intelligence (MSS / Ministry of State Security). No specific PLA unit, no specific tracked-actor designation. The Record explicitly notes the absence of named threat-actor (no APT40, APT41, Volt Typhoon, or Salt Typhoon references appear in the advisory).

**Hard Rule 2 compliance:** Five Eyes attributes generically to "China's military intelligence services." Archimedes preserves verbatim. Does NOT upgrade to specific tracked-actor mapping.

## A&D / DIB nexus

**Not explicit.** The advisory names "government and military personnel" and "anyone with access to classified or privileged information." DIB cleared-personnel — and by extension A&D prime / Tier-2/3 supplier security-cleared engineers, program managers, and program-office staff — are **squarely within the implicit target scope** but are **not in the named-target list**.

**Operational read for the target profile:** A mid-to-large US aerospace and defense contractor's cleared-personnel population — ITAR-program engineers, classified-program PMs, USG contract-vehicle leads — falls within "anyone with access to classified or privileged information." Indo-Pacific-deployed military personnel call-out is direct-relevance to A&D primes with INDOPACOM customer programs (B-21 / B-1B sustainment, F-22 / F-35 modification, GMD / THAAD, Aegis BMD, submarine and shipbuilding). The advisory's framing is HUMINT-led counterintelligence rather than cyber-tradecraft, which puts it adjacent to but outside the standard cyber-CTI surface.

## Why this is NOT a FLASH trigger

Per the 12:00 FLASH sentinel evaluation (carried forward and re-evaluated here):

1. **Trigger 2 (new tracked-actor attribution):** Five Eyes attributes generically to "China's military intelligence services" — PLA-attributed but no specific tracked-actor in `_roster.yaml` is named. Volt Typhoon (#008), Salt Typhoon (#010), APT40 (#017), APT41 (#019) are all PLA / China-affiliated and present in the roster but none is named in this advisory. No new tracked-actor attribution.
2. **Trigger 4 (tracked-actor TTP change):** Same gap — no roster-mapped tracked-actor, no new tooling / targeting / infrastructure attributable to a tracked-actor.
3. **Trigger 5 (active A&D-sector campaign):** Trigger letter requires "targets include aerospace-defense or watchlist entity" with multi-victim confirmed and active campaign. Five Eyes alert IS active, IS multi-victim by design (recruitment campaign across five-country footprint), IS implicitly cleared-personnel including A&D-DIB-eligible — BUT the campaign is HUMINT-led counterintelligence, **not cyber-TTP**, and A&D-sector targeting is implicit not explicit. The FLASH trigger evaluation considers this a marginal-fail on the explicit-A&D-naming and cyber-TTP requirements.

This is a **counterintelligence-adjacent finding** material for the A&D-target-profile audience even though it is technically out-of-cyber-domain. PM-04 brief is the right disposition.

## Suggested grading hint for grader

Source layer: Five Eyes joint counterintelligence advisory (A1 procedural — five-government-intelligence-service joint authorship is the highest-credibility public counterintelligence source class). The Record relay is B-grade media.

WEP layering (grader to assess):
- **Procedural facts** (advisory exists, PLA-attributed campaign described, named tradecraft) — **very likely** (vendor-on-own-incident equivalent: government counterintelligence service on own observed activity).
- **Operational claim that DIB cleared-personnel are within target scope** — **likely** (implicit target scope per "anyone with access to classified or privileged information" + "Indo-Pacific stationed military personnel" — direct inference for A&D-cleared-personnel audiences).
- **Operational claim that a specific A&D prime is targeted in any active recruitment cell** — **unable to assess** (no named-victim disclosure in this advisory).

Suggested digraph: **A1** (procedural) / **A2 → B2** (operational implications for DIB cleared-personnel audiences — government source attesting to active campaign with implicit target scope, capped at B2 because of single-source veto on the campaign's specific operational reach into A&D programs versus general cleared-personnel population).

## Watch signals for grader / actor-profiler

- Any cyber-TTP overlap surfaced by a Tier-1 IR firm (e.g., subsequent malware delivery against recruited insider) — would lift this from counterintelligence advisory to cyber-actionable.
- Any APT40 / APT41 / Volt Typhoon / Salt Typhoon attribution layered on by a Tier-1 IR firm — would lift to Trigger 2 territory and likely FLASH-trigger a re-evaluation.
- Named A&D prime in any follow-on Five Eyes, NCSC, CISA, or industry-association advisory.
- Any DIB / cleared-defense-contractor-specific guidance from CISA / DSS / DCSA / NCSC paralleling the Five Eyes alert (DCSA insider-threat guidance update would be the strongest follow-on signal for the target profile).
- Operator decision: should "Chinese PLA HUMINT cluster" become a tracked entity in `_roster.yaml`? Currently no, given Hard Rule 2 (no first-time attribution origination) and the absence of a specific tracked-actor designation in the advisory itself.

## Defensive prioritization for target profile

A mid-to-large US aerospace and defense contractor with cleared-personnel population:

1. **Cleared-personnel security-awareness reminder** — circulate via FSO / DCSA channels: unsolicited LinkedIn contacts from "private consultancies," "think tanks," or "human resources firms" offering paid consulting work / "intelligence reports" / virtual-interview engagement are within the named tradecraft. Pattern-recognition guidance: probing questions about role, unit, customer programs in an early-stage interview is a flag; payment offers are a flag; transition to encrypted-messaging is a flag.
2. **Indo-Pacific program teams** — direct circulation of the MI5 PDF to security-cleared personnel on INDOPACOM-customer programs (named-target call-out in the advisory). Brief FSOs on the specific Indo-Pacific framing.
3. **Corporate security CI partnership** — confirm working relationship with FBI Counterintelligence / DCSA insider-threat program; report any matching tradecraft observations.
4. **HR / external-recruiter due diligence** — for senior-cleared roles, augment standard background checks with insider-threat / foreign-influence vetting where DCSA permits. Front-company-as-recruiter is a named tradecraft; the recruiting org itself may be the threat surface.
5. **No cyber-TTP defensive action change today** — this is HUMINT-led counterintelligence; standard cyber controls (endpoint EDR, network egress, identity hardening) are not the leverage point for this campaign. The leverage point is human-factor security awareness and CI partnership.

---

## Extraction notes

- Language: en
- Publisher byline: not bylined (joint government advisory PDF); The Record relay byline absent in feed metadata.
- Article type: joint government counterintelligence advisory (primary, PDF) + trade-press relay (The Record).
- Raw IOC extraction invoked: no — HUMINT advisory, no cyber-IOCs by definition.

## IOCs (from ioc-extraction skill) — not applicable

No cyber-IOCs in the advisory. Operational artifacts are tradecraft-recognition (LinkedIn approach patterns, front-company-as-recruiter, virtual-interview probing, encrypted-messaging transition, unconventional-payment) not network / endpoint / file-system IOCs.

Attribution claims preserved verbatim: *"China's military intelligence services"* (Five Eyes joint, generic PLA-attributed). Archimedes does NOT upgrade to specific tracked-actor mapping. No first-time attribution origination per Hard Rule 2.
