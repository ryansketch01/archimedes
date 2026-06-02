---
raw_id: raw-2026-06-02-pm-005-cisa-7-agency-joint-automatic-tank-gauge-atg-hardening-energy-transportation-critical-infra
collected_at: 2026-06-02T15:45:00-04:00
run_id: pre-brief-20260602-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: cisa-advisories
  source_name: CISA joint advisory with FBI, NSA, DOE, EPA, TSA, DOT, USDA - Hardening Automatic Tank Gauge (ATG) Systems
  source_url: https://www.cisa.gov/resources-tools/resources/cisa-and-partners-urge-hardening-automatic-tank-gauge-systems
  published_at: 2026-06-02T08:00:00-04:00     # 12:00 UTC published; in-window at the absolute start of pre-brief window
source_grade: A (CISA joint advisory + 7 U.S. government agencies — government-body authority on critical-infrastructure protection guidance)
date: 2026-06-02
topic: cisa-joint-atg-systems-hardening-malicious-cyber-activity-energy-chemical-transport-foodag
match_reason:
  watchlist: []                  # No A&D-watchlist entity. Energy / Chemical / Food&Ag / Transportation sectors named.
  actors: []                     # No actor attributed by CISA. "Malicious cyber activity targeting U.S.-based automatic tank gauge systems" — actor-class observation without specific attribution.
  vulnerabilities: []
  keywords: [CISA, FBI, NSA, DOE, EPA, TSA, DOT, USDA, joint advisory, automatic tank gauge, ATG, OT, ICS, critical infrastructure, fuel storage, leak detection, energy sector, transportation sector, chemical sector, food and agriculture sector]
triage_tags: [government_joint_advisory, ot_ics_sector_intel, critical_infrastructure, no_ad_direct, sector_intelligence_carry_context]
candidate_triggers: []
# Trigger 5 (ad-sector-campaign): FAIL — Energy/Chemical/Food&Ag/Transport
# sectors named; A&D NOT named. CISA's advisory text observes "malicious
# cyber activity" generically — no multi-victim attribution or specific
# campaign named.
# Trigger 2 (tracked-actor-attribution): FAIL — no actor attributed.
# Result: no FLASH trigger fits. Raw-signal as PM-1 grader queue input
# for Sector Focus / critical-infrastructure carry-context.
iocs_extracted: false
iocs_count: 0
text_word_count: 720
promoted: true
promoted_to_finding: finding-2026-06-02-0009-cisa-8-agency-joint-automatic-tank-gauge-atg-hardening-advisory-energy-chemical-foodag-transport-no-ad-direct
promoted_at: 2026-06-02T16:32:00-04:00
promotion_run_id: afternoon-20260602-160000
ttl_expires_at: 2026-08-31T15:45:00-04:00
test: false
---

# CISA + FBI + NSA + DOE + EPA + TSA + DOT + USDA Joint Advisory — Hardening Automatic Tank Gauge (ATG) Systems

## Source

CISA joint resource page published 2026-06-02 at 12:00 UTC = 08:00
EDT (in-window at the absolute start of the pre-brief window). URL:
https://www.cisa.gov/resources-tools/resources/cisa-and-partners-urge-hardening-automatic-tank-gauge-systems

This is an **8-agency joint U.S. government advisory** — one of the
heaviest joint authoring counts CISA publishes for sector-specific
guidance. Authoring organizations:

1. **CISA** (Cybersecurity and Infrastructure Security Agency)
2. **FBI** (Federal Bureau of Investigation)
3. **NSA** (National Security Agency)
4. **DOE** (Department of Energy)
5. **EPA** (Environmental Protection Agency)
6. **TSA** (Transportation Security Administration)
7. **DOT** (Department of Transportation)
8. **USDA** (U.S. Department of Agriculture)

## Body

### Scope

CISA and partners "**are aware of malicious cyber activity targeting
U.S.-based automatic tank gauge (ATG) systems**" — actor-class
observation without specific attribution.

ATG systems are widely deployed across:
- **Energy Sector** (fuel storage tank monitoring)
- **Chemical Sector** (storage tank parameters / leak detection)
- **Food and Agriculture Sector** (agricultural / industrial liquid
  storage)
- **Transportation Systems Sector** (transport-fuel infrastructure)

ATG functions: automated and remote monitoring of storage tank
parameters including fuel levels, liquid levels, temperature, and
leak detection.

### Hardening guidance (per CISA framing)

The joint advisory urges ATG owners and operators to:
- **Secure ATG systems with strong passwords**
- **Remove default / weak / vendor-default credentials**
- (Implicit) **Network-segment ATG management interfaces away from
  internet-accessible exposure**

CISA's framing is procedural hardening guidance (default-credentials
+ password strength as the named first-action), not technical
exploitation analysis or attribution-class campaign reporting.

### What's NOT in the advisory

- **No specific CVE referenced** — this is operational-hardening
  guidance, not vulnerability disclosure
- **No threat actor named** — actor-class observation only
- **No multi-victim campaign attribution** — generic "malicious cyber
  activity" framing
- **No A&D / DIB sector mentioned** — the 4 sectors named (Energy,
  Chemical, Food&Ag, Transportation) do NOT include A&D, Defense
  Industrial Base, or any aerospace-defense.yaml watchlist entity
- **No specific ATG vendor named** — Veeder-Root / OPW / Franklin
  Fueling / Gilbarco common ATG vendors NOT singled out in the
  advisory text
- **No CISA KEV addition** for any ATG-vendor-product CVE concurrent
  with this advisory at sweep time

### A&D-prime relevance

**INDIRECT — sector-intelligence carry-context only.**

The closest A&D-prime nexus: **military / DoD fuel-storage estates**
deploy ATG systems for jet-fuel / motor-pool / strategic-reserve tank
monitoring. **TSA + DOT + DOE** joint authoring suggests U.S. national
fuel-infrastructure operational concern, with **possible DIB
fuel-vendor partner-flow inheritance** for the operational hardening
guidance.

However, the advisory's named sectors do NOT include Defense Industrial
Base, and **no A&D-prime watchlist entity is named** in CISA's text.

### Operator awareness signal

8-agency joint authoring is a strong signal of **U.S.-government
multi-agency concern** about ATG-targeting activity. Historical
precedent: similar joint advisories have preceded campaign-attribution
disclosures by 30-90 days (e.g., Iran-OT-targeting joint advisories
2023-2025 that preceded CyberAv3ngers attribution).

**No FLASH trigger fits**, but the advisory is **sector-intelligence
carry-context** for any future ATG-targeting actor attribution.
Vuln-tracker / actor-profiler should monitor for follow-on
campaign-attribution publications from CISA / FBI / DOE within the
next 30-90 day window.

### Hard Rule 2 — no attribution origination

CISA's advisory text observes "malicious cyber activity" generically
without naming any specific actor, nation-state, or campaign.
Archimedes preserves zero attribution. This is a **defensive
hardening advisory**, not a campaign-attribution publication.

## Extraction notes

- Language: en
- Article type: government joint advisory (CISA + 7 partners primary)
- Raw IOC extraction invoked: no — operational-hardening guidance,
  no infrastructure / hash / domain IOCs in scope
- Publisher: CISA (authoring organization)
- Window: in (12:00 UTC = 08:00 EDT — exact start of pre-brief window;
  treated as in-window per inclusive-start convention)
- Source-health update: cisa-advisories last_successful_fetch =
  2026-06-02T15:45 EDT
- Hard Rule 2: zero attribution; preserved
- Hard Rule 3: NO exploit / PoC; advisory is defensive guidance only
- FLASH trigger evaluation: all FAIL — generic actor-class observation
  fails Trigger 2; sector-set does not include A&D fails Trigger 5
- Anti-noise: NO prior Archimedes-corpus ATG-targeting coverage;
  net-new sector-intel topic; 8-agency joint authoring is the
  unusually-heavy signal here
- Operator handoffs: (a) actor-profiler awareness for potential
  follow-on attribution disclosures (CyberAv3ngers-class pattern from
  Iran OT-targeting precedent); (b) vuln-tracker awareness for any
  ATG-vendor CVE additions to KEV in the 30-90 day forward window;
  (c) sector-intel briefer note — joint 8-agency authoring is the
  newsworthy signal even absent specific A&D-prime relevance
