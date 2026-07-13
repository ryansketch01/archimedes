---
raw_id: raw-2026-07-12-handala-newactor-002
collected_at: 2026-07-12T23:45:00-04:00
run_id: handala-newactor-20260712-2300
collection_mode: on_demand
on_demand_command: /new-actor Handala Hack (roster #014 — targeted dossier-seed collection pass)
source:
  # Handala-persona operational primary = Check Point Research "Handala Hack:
  # Unveiling Group's Modus Operandi" (2026). Stryker/Intune campaign corroborated
  # by multiple relays (Unit 42, Deepwatch, CSA Labs, Push Security) surfaced this
  # pass. CPR primary retrieved via WebFetch summarization (appendix anti-bot risk).
  source_yaml_id: checkpoint-research
  source_name: Check Point Research — "'Handala Hack' — Unveiling Group's Modus Operandi"
  source_url: https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/
  corroborating_source_url: https://unit42.paloaltonetworks.com/handala-hack-wiper-attacks/
  published_at: 2026-06-01T00:00:00-04:00      # approximate; CPR 2026, exact date pending direct retrieval
match_reason:
  watchlist: []            # Stryker = medical-device maker, NOT an A&D-prime watchlist entity; no A&D prime named
  actors: [Handala Hack, Void Manticore, Storm-0842]
  vulnerabilities: []
  keywords: [Handala, Handala Wiper, Stryker, Microsoft Intune, MDM wipe, VeraCrypt, PowerShell wiper, NetBird, hack-and-leak, faketivist, Iran, MOIS, Panjaki]
  match_basis: >
    Companion to raw-2026-07-12-handala-newactor-001. Captures the HANDALA-PERSONA
    operational layer: CPR's explicit statement that Handala Hack is a persona
    OPERATED BY Void Manticore, the 2024-2026 intrusion/leak history (Israel +
    US-enterprise expansion incl. Stryker), the Intune-MDM mass-wipe TTP, and the
    2026 IOC set. No A&D prime is named as a victim; relevance to the ad-prime
    profile is INDIRECT (large-enterprise MDM-abuse TTP portability + hack-and-leak
    posture), recorded without hardening any A&D-direct claim (Hard Rule 2).
triage_tags: [new_actor_seed, iran_mois, hacktivist_faketivist, destructive_wiper, intune_mdm_abuse, hack_and_leak, us_enterprise_expansion, ad_relevance_indirect, on_demand_newactor]
iocs_extracted: true
iocs_count: 3             # 1 VT-confirmed IP + 3 additional IPs (partial); hashes pending (see caveat)
text_word_count: 950
promoted: false
ttl_expires_at: 2026-10-10T23:45:00-04:00
---

# "Handala Hack" — Unveiling Group's Modus Operandi (Check Point Research, 2026)

Operational-history and persona-linkage report for roster #014. Pairs with the
attribution-foundation file `...-001`.

## Handala-persona <-> Void Manticore linkage — verbatim per Hard Rule 2

- **Check Point Research (A-grade) — verbatim:**
  > "Handala Hack is an online persona operated by Void Manticore (aka Red
  > Sandstorm, Banished Kitten), an actor affiliated with Iranian Ministry of
  > Intelligence and Security (MOIS)."

  CPR states the persona-operator linkage DIRECTLY: Handala Hack is a persona
  *operated by* Void Manticore. This is the specific equivalence Ryan flagged as
  the one to capture precisely — CPR does NOT hedge it. The roster #014 alias set
  [Void Manticore, Storm-0842, DEV-0842] is thereby CPR-supported, with "Red
  Sandstorm" and "Banished Kitten" as additional CPR-named aliases (both also
  appear in MITRE G1055's association list — see `...-001`).

- **Organizational specificity (CPR) — verbatim:**
  CPR ties the operator to the "MOIS Internal Security Deputy, particularly its
  Counter-Terrorism (CT) Division, operating under the supervision of Seyed Yahya
  Hosseini Panjaki" — whom the report states was reportedly killed during Israeli
  strikes on Iran in early March 2026. Recorded as CPR's assessment.

## 2024-2026 operations — claimed vs. verified

- **Israel:** multiple intrusions and hack-and-leak operations (the "Handala"
  leak persona, named for the Palestinian cartoon figure). CPR presents these as
  its own observations; most individual incidents are presented WITHOUT explicit
  independent third-party verification in the report body.
- **US-enterprise expansion — Stryker Corporation:** CPR notes recently expanded
  targeting to US-based enterprises "including medical technology giant Stryker."
  Per corroborating relays surfaced this pass (Deepwatch, Cloud Security Alliance
  Labs, Push Security, 7AI): on/around **2026-03-11** Handala executed a
  destructive attack against Stryker by abusing Stryker's OWN Microsoft Intune MDM
  platform to issue legitimate remote-wipe commands to 200,000+ enrolled devices
  across 79 countries. CPR cross-references Krebs on Security on the Stryker
  incident.
  - **Verification status:** the Intune-mass-wipe mechanism is reported
    consistently across multiple relays but they may share a common upstream;
    treat as reported-consistent, not independently confirmed. Grader to resolve.
- **Albania:** continuing "Homeland Justice" persona activity (regional
  destructive theatre carried over from the 2022-2024 Void Manticore campaigns).

## TTPs (CPR 2026)

- **Handala Wiper** — custom, MBR-based wiping.
- **PowerShell-based wiper** — CPR notes AI-assisted code for file deletion
  (recorded as CPR's characterization).
- **VeraCrypt** — legitimate full-disk-encryption tool repurposed for destructive
  (lock-out) impact.
- **Microsoft Intune / MDM abuse** — issuing legitimate remote-wipe commands from
  a compromised MDM tenant (the Stryker vector). NOTE: this TTP is directly
  PORTABLE to any large enterprise MDM tenant, including A&D primes — recorded as
  a portability observation for the analyst, NOT an A&D-direct targeting claim.
- **NetBird** — off-the-shelf network tunneling/overlay for access.
- **Manual hands-on:** RDP lateral movement, Group Policy distribution of wipers,
  manual deletion via RDP. Consistent with the 001-file characterization of
  Void Manticore as manual/hands-on with off-the-shelf + light-custom tooling.

## A&D-prime relevance (recorded, not hardened)

No aerospace/defense prime is named as a Handala/Void Manticore victim in any
retrieved source. Relevance to Ryan's ad-prime target profile is INDIRECT and
STRUCTURAL: (a) the Intune/MDM mass-wipe TTP is portable to any large ITAR-
regulated enterprise; (b) Handala's hack-and-leak posture would apply the same
way to a defense supplier as to Stryker; (c) Iran-nexus destructive intent
against Western industry is the standing geopolitical driver. This is context for
the analyst/actor-profiler — Archimedes originates NO A&D-direct targeting claim
(Hard Rule 2).

---

## Extraction notes

- Language: en
- Publisher bylines: Check Point Research (team); corroborating relays: Palo Alto
  Unit 42, Deepwatch Labs, CSA Labs, Push Security, 7AI, Krebs on Security (via
  CPR cross-reference).
- Article type: vendor threat-research report (CPR) + multiple news/vendor relays.
- Originating primary: Check Point Research 2026. Retrieved via WebFetch
  summarization; raw IOC appendix NOT cleanly retrieved. Publication date
  (2026-06-01) is APPROXIMATE — pending direct retrieval for exact date.
- Raw IOC extraction invoked: yes.
- Single-source discipline (NOT grading): CPR is the sole ORIGINATING A-grade
  primary on the Handala-persona-operated-by-Void-Manticore linkage and the
  actor's MO. Unit 42 is an independent A-grade voice on the "increased risk of
  wiper attacks" theme and MAY provide independent corroboration on the
  Stryker/Intune vector — the grader should verify whether Unit 42's report is
  evidence-independent of CPR or downstream of it. Recorded, not resolved.
- Hard Rule 3: no exploit/PoC content — wiper/Intune-abuse mechanics named and
  described by function only; no commands, no code.
- Hard Rule 7: NO credentials stored. The Stryker incident involves a compromised
  MDM tenant; no credential values surfaced in any retrieved source, and none
  would be stored if they had (query/count/discard). Credential exposure observed
  this pass: 0 instances.

## IOCs (ioc-extraction output)

```yaml
extraction_metadata:
  source_brief_id: checkpoint-handala-modus-operandi-2026
  source_url: https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/
  extracted_at: 2026-07-12T23:45:00Z
  extracted_by: collector
  target_actor_id: "014"
  text_word_count: 950

indicators:
  - id: handala-ip-82-25-35-25
    type: ipv4
    value: "82.25.35.25"
    defanged_original: "82.25.35[.]25"
    role: c2
    campaign: "Handala 2024-2026 operations"
    related_malware: [Handala Wiper, NetBird]
    source_brief: checkpoint-handala-modus-operandi-2026
    context_excerpt: "Handala operator/infrastructure IP in the CPR 2026 IOC set"
    attribution_in_text: Handala Hack (Void Manticore)
    enrichment:
      virustotal:
        found: true
        malicious: 9
        suspicious: 0
        country: GB
        asn: 21859
        as_owner: "Zenlayer Inc"
        network: "82.25.35.0/24"
        flagged_by: [ADMINUSLabs, BitDefender, CRDF, CyRadar, ESTsecurity, Fortinet, G-Data, SOCRadar, "alphaMountain.ai"]
        last_analysis_date: "2026-07-09T18:23:01+00:00"
      first_party_splunk:
        indices_checked: [defenseclaw_local, archimedes]
        window: "-90d"
        hits: 0
    notes: "VT-confirmed malicious (9 engines) as of 2026-07-09 — genuine IOC, recent activity."
  - id: handala-ip-31-57-35-223
    type: ipv4
    value: "31.57.35.223"
    defanged_original: "31.57.35[.]223"
    role: c2
    source_brief: checkpoint-handala-modus-operandi-2026
    context_excerpt: "Handala operator/infrastructure IP in the CPR 2026 IOC set"
    attribution_in_text: Handala Hack (Void Manticore)
    enrichment:
      first_party_splunk: {indices_checked: [defenseclaw_local, archimedes], window: "-90d", hits: 0}
    notes: "Reported by CPR relay; not independently VT-checked this pass."
  - id: handala-ip-107-189-19-52
    type: ipv4
    value: "107.189.19.52"
    defanged_original: "107.189.19[.]52"
    role: c2
    source_brief: checkpoint-handala-modus-operandi-2026
    context_excerpt: "Handala operator/infrastructure IP in the CPR 2026 IOC set"
    attribution_in_text: Handala Hack (Void Manticore)
    enrichment:
      first_party_splunk: {indices_checked: [defenseclaw_local, archimedes], window: "-90d", hits: 0}
    notes: "Reported by CPR relay; not independently VT-checked this pass. (107.189.0.0/16 = frequently-abused hosting.)"
  - id: handala-ip-146-185-219-235
    type: ipv4
    value: "146.185.219.235"
    defanged_original: "146.185.219[.]235"
    role: c2
    source_brief: checkpoint-handala-modus-operandi-2026
    context_excerpt: "Handala operator/infrastructure IP in the CPR 2026 IOC set"
    attribution_in_text: Handala Hack (Void Manticore)
    enrichment:
      first_party_splunk: {indices_checked: [defenseclaw_local, archimedes], window: "-90d", hits: 0}
    notes: "Reported by CPR relay; not independently VT-checked this pass."

  # --- Hashes REPORTED but NOT verifiable this pass ---
  - type: note
    value: "CPR 2026 report lists MD5 hashes for Handala Wiper (~5986ab04dd6b3d259935249741d3eff2), a PowerShell wiper (~3cb9dea916432ffb8784ac36d1f2d3cd), VeraCrypt (~3236facc7a30df4ba4e57fddfba41ec5), and NetBird (~e035c858c1969cffc1a4978b86e90a30) as surfaced via WebFetch summarization. The two spot-checked (Handala Wiper MD5, and the 001-file SHA-256) returned found:false on VirusTotal — a strong signal the summarizer garbled the strings. Hash VALUES held PENDING DIRECT RETRIEVAL of the CPR appendix; do NOT fold into iocs.yaml as-is. NetBird and VeraCrypt are legitimate dual-use tools regardless — their hashes are low-value even if confirmed."
    role: pending_retrieval
  # --- Host artifacts (low-confidence, WebFetch-surfaced) ---
  - type: note
    value: "Attacker machine names DESKTOP-FK1NPHF and WIN-P1B7V100IIS and Starlink/commercial-VPN source ranges (188.92.255.x, 209.198.131.x, 149.88.26.x, 169.150.227.x) were surfaced but are default-Windows-naming / shared-egress artifacts of LOW standalone value; recorded as context only, not as high-confidence atomic IOCs."
    role: ambiguous

attribution_claims:
  - claimant: "Check Point Research"
    claim: "Handala Hack is an online persona operated by Void Manticore (aka Red Sandstorm, Banished Kitten), affiliated with Iran's MOIS"
    nation_named: Iran
    service_named: MOIS
    actor_named: Void Manticore
    linkage_type: persona_operated_by_actor
    confidence_language: "is an online persona operated by (flat, no hedge)"
    requires_grading: true
  - claimant: "Check Point Research"
    claim: "Void Manticore operator tied to MOIS Internal Security Deputy, CT Division, under Seyed Yahya Hosseini Panjaki"
    nation_named: Iran
    service_named: "MOIS (Internal Security Deputy / CT Division)"
    confidence_language: "particularly / operating under the supervision of"
    requires_grading: true
  - claimant: "Check Point Research (cross-ref Krebs on Security)"
    claim: "Handala expanded to US enterprises incl. Stryker; ~2026-03-11 destructive attack via abuse of Stryker's Microsoft Intune MDM (remote-wipe of 200k+ devices, 79 countries)"
    nation_named: Iran
    actor_named: Handala Hack (Void Manticore)
    confidence_language: "recently expanded targeting / referenced"
    requires_grading: true
```
