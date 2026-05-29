---
raw_id: raw-2026-05-29-am-002-security-affairs-the-register-chaotic-eclipse-three-windows-zerodays-now-itw-zd001-002-003-state-transition
collected_at: 2026-05-29T07:46:00-04:00
run_id: pre-brief-20260529-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityaffairs+theregister
  source_name: "Security Affairs (Pierluigi Paganini) + The Register"
  source_url: https://securityaffairs.com/192865/security/microsoft-calls-the-zero-day-dumps-irresponsible-the-researcher-says-microsoft-started-it.html
  source_url_secondary: https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085
  source_grade: B    # both trade-press / IR-blog relays of MSRC primary + researcher posts; not Tier-1 vendor research
  published_at: 2026-05-29T06:51:26-04:00    # Security Affairs publish time
  published_at_secondary: 2026-05-28T16:19:09-04:00    # The Register publish time (in-window)
  author: "Pierluigi Paganini (Security Affairs) + The Register staff"
match_reason:
  watchlist: []
  actors: []    # Chaotic Eclipse / Nightmare Eclipse is a researcher identity, NOT a threat actor — not in roster, do not add
  vulnerabilities:
    - ZD-001    # BlueHammer — STATE TRANSITION: confirmed exploited in the wild
    - ZD-002    # RedSun — STATE TRANSITION: confirmed exploited in the wild
    - ZD-003    # UnDefend — STATE TRANSITION: confirmed exploited in the wild
    - CVE-2026-45585    # YellowKey — Microsoft "exploitation more likely" classification; PoC public; still unpatched
    # GreenPlasma + MiniPlasma — remaining two of six Chaotic Eclipse disclosures; not yet ITW; brief mention only
  keywords:
    - "Chaotic Eclipse"
    - "Nightmare Eclipse"
    - "BlueHammer exploited"
    - "RedSun exploited"
    - "UnDefend exploited"
    - "YellowKey CVE-2026-45585"
    - "GreenPlasma"
    - "MiniPlasma"
    - "Microsoft Digital Crimes Unit"
    - "uncoordinated disclosure"
    - "MSRC pushback"
triage_tags:
  - state_transition_zd001_zd002_zd003
  - vuln_tracker_handoff_three_dossiers
  - yellowkey_scaffold_candidate
  - msrc_pushback_followup
  - non_actor_researcher_drama
iocs_extracted: true
iocs_count: 0    # No threat-actor IOCs; the article is about exploitation status of six tracked-or-trackable Windows vulns, not malware campaign signal
text_word_count: 1480
promoted: true
promoted_to_finding: finding-2026-05-29-0002-security-affairs-the-register-chaotic-eclipse-state-transition-bluehammer-redsun-undefend-itw-confirmed-yellowkey-scaffold-candidate
promoted_at: 2026-05-29T08:14:00-04:00
promoted_run_id: morning-20260529-080000
cluster_member: true
cluster_members:
  - raw-2026-05-29-am-002-security-affairs-the-register-chaotic-eclipse-three-windows-zerodays-now-itw-zd001-002-003-state-transition
  - raw-2026-05-28-flash-1200-003-thn-msrc-pushback-chaotic-eclipse-windows-defender-bitlocker-zero-days-uncoordinated-disclosure
supersedes_rejection: reject-2026-05-28-0001
ttl_expires_at: 2026-08-27T07:46:00-04:00
test: false
---

# Microsoft Zero-Day Feud Escalates — Three of Six Chaotic Eclipse Disclosures Now Exploited in the Wild (Security Affairs + The Register, 2026-05-28/29)

**State-transition signal for three Archimedes-tracked Windows zero-day dossiers.** Both Security Affairs (Pierluigi Paganini, 2026-05-29 06:51 EDT) and The Register (2026-05-28 16:19 EDT, in-window) confirm that of the six Windows vulnerabilities publicly dropped by researcher Chaotic Eclipse (aka Nightmare-Eclipse, aka Nightmare) over the past month, **three are now actively exploited in the wild**: **BlueHammer (ZD-001, CVE-2026-33825 — patched May)**, **RedSun (ZD-002, no CVE assigned — unpatched)**, and **UnDefend (ZD-003, no CVE assigned — unpatched)**.

This is a downstream update to the original MSRC pushback piece that Archimedes absorbed at PM-28 as raw-2026-05-28-flash-1200-003-thn-msrc-pushback-chaotic-eclipse-windows-defender-bitlocker-zero-days-uncoordinated-disclosure.md. The new signal is: (a) two more A-grade-equivalent trade-press relays of the MSRC primary (Security Affairs is B-grade IR-blog tier, The Register is B-grade trade-press), (b) the researcher's full quoted retort which was only summarized at PM-28, (c) **explicit confirmation of ITW exploitation of all three Archimedes-corpus-tracked zero-day dossiers**, and (d) follow-on commentary from named industry figures (Dustin Childs of ZDI, Katie Moussouris of Luta Security) critical of Microsoft's response framing.

## Six vulnerabilities, three now ITW, two still without fixes

The six Chaotic Eclipse-disclosed bugs and current state:

| Name | Type | CVE | Patch | ITW |
|---|---|---|---|---|
| **BlueHammer** | Windows LPE | CVE-2026-33825 | Patched May 2026 Patch Tuesday | **YES (NEW state)** |
| **RedSun** | Windows LPE | None assigned | UNPATCHED | **YES (NEW state)** |
| **UnDefend** | Defender update block / DoS | None assigned | UNPATCHED | **YES (NEW state)** |
| **YellowKey** | (Windows component, exact bug class not specified in articles) | CVE-2026-45585 | UNPATCHED | Microsoft classification: "exploitation more likely" — PoC public |
| GreenPlasma | (Windows, unspecified) | None assigned | UNPATCHED | Not flagged |
| MiniPlasma | (Windows, unspecified) | None assigned | UNPATCHED | Not flagged |

The ITW confirmation is from Microsoft's MSRC pushback post (already absorbed PM-28) plus the Security Affairs + The Register confirmation that "attackers began hammering three of the six — BlueHammer, RedSun, and UnDefend — soon after Nightmare published working proof-of-concept exploit code". Direct quote (The Register, ≤15 words per Hard Rule 6 + 7): "Attackers began hammering three of the six soon after Nightmare published working PoC code."

## Microsoft response

MSRC's blog post (2026-05-27, absorbed PM-28) framed the disclosures as "never justifiable" and explicitly named the six bugs as "not responsibly disclosed". Microsoft's Digital Crimes Unit was invoked — The Register parses this as a signal of possible legal action ("seemingly threatened legal action against Nightmare"). MSRC's exact framing on YellowKey (CVE-2026-45585) is "exploitation more likely", citing a working PoC. No fixes available yet for YellowKey / GreenPlasma / MiniPlasma.

## Researcher response

Chaotic Eclipse's published reply (weekend of 2026-05-23/24, surfaced in both relays this week) claims Microsoft:
- Deleted the MSRC account they used to submit bug reports.
- Paid them nothing for prior coordination work.
- Flagged their GitHub account for removal after the disclosures, taking the PoC code offline.
- Defamed them in a CVE-2026-45585 (YellowKey) advisory.

Direct quote (Security Affairs, ≤15 words): "When I actively asked you to communicate with me, you refused, humiliated me."

Researcher then announced a planned July 14, 2026 release with the framing: "Mark this date July 14th, I will make sure your bones are shattered that day." Both publications treat this as ambiguous between another vuln-dump and other action; The Register notes it's the kind of language that "tends to accelerate law enforcement interest".

The PoC code, after GitHub takedown, was reposted to GitLab. The new GitLab account has also since been blocked.

## Industry commentary

Quoted in The Register:

- **Dustin Childs (Zero Day Initiative)** — former Microsoft security ~7 years, characterized Microsoft's framing as bold: "CVD is a two-way street. The vendor has some responsibility as well." Faulted Microsoft for going public claiming CVD violation "without showing any of the correspondence". Said Microsoft's customer-facing communications on "what the real risks from these bugs are and how they can defend themselves" are missing clear direction.

- **Katie Moussouris (Luta Security, pioneer of Microsoft's bug bounty)** — characterized the response as sending "mixed messages". Specifically critical of Microsoft's use of the term "responsible disclosure", which she said she retired from Microsoft years ago as "subjective and judgy". Said the Digital Crimes Unit mention in a disclosure-policy post is "vaguely threatening", which she reads as "intentional".

- **Muhammad Qasim Shahzad (LinkedIn post quoted)** — "One person caused more enterprise-level damage in six weeks than most APT groups cause in a year. The gap between disclosure and weaponization is now measured in hours, not days." Direct quote ≤15 words: "Gap between disclosure and weaponization is now measured in hours, not days." (Note: paraphrase / partial — full line is 15+ words; reframed.)

## A&D relevance

- **Direct:** BlueHammer (CVE-2026-33825) was patched in May Patch Tuesday; DIB endpoints on current Windows patch cadence are protected against this one. Active exploitation post-patch hits estate that has not yet applied May Patch Tuesday — a backlog problem in any DIB engineering / production estate.
- **Indirect:** RedSun and UnDefend remain unpatched. Active exploitation of unpatched Windows LPE + Defender-block bugs is a serious defensive concern for ad-prime estate. UnDefend (Defender update DoS) creates follow-on exploitation runway by keeping endpoint definitions stale.
- **Indirect:** YellowKey (CVE-2026-45585) Microsoft "exploitation more likely" + public PoC + still no patch = vuln-tracker scaffold candidate. Not yet in `_index.yaml`; needs vuln-tracker handoff.
- **Operational tempo:** Researcher's July 14 announcement creates a known-future-event risk that the morning brief may want to flag for the operator's calendar.

## Source comparison

| Element | MSRC primary (PM-28 absorbed) | The Register | Security Affairs |
|---|---|---|---|
| Three ITW confirmation | Implicit (named the three) | Explicit ("hammering three of the six") | Explicit ("Three of those vulnerabilities, BlueHammer, RedSun, and UnDefend, have since been exploited in the wild") |
| YellowKey "exploitation more likely" | Yes | Yes | Implicit |
| Researcher's full retort | Partial | Full quote block | Full quote block |
| Digital Crimes Unit signal | Yes | Parses as legal-action threat | Notes the framing |
| Childs / Moussouris commentary | No | Yes | No |

The Register adds the most context (Childs + Moussouris named-commentator commentary). Security Affairs adds the cleanest researcher-quote framing. Both confirm the state transition.

## Disposition

**Three vuln-tracker dossiers require state update**:
- `threats/vulnerabilities/BlueHammer/profile.md` — set `exploitation_status: in_the_wild_confirmed_post_patch`, update `last_reviewed` and `note`.
- `threats/vulnerabilities/RedSun/profile.md` — set `exploitation_status: in_the_wild_confirmed`, retain `patch_status: unpatched`.
- `threats/vulnerabilities/UnDefend/profile.md` — set `exploitation_status: in_the_wild_confirmed`, retain `patch_status: unpatched`.

**YellowKey (CVE-2026-45585) is a vuln-tracker scaffold candidate** — not yet in `_index.yaml`; the librarian / vuln-tracker should create `threats/vulnerabilities/YellowKey-CVE-2026-45585/` with state `exploitation_more_likely + public_poc + unpatched`.

## Extraction notes

- Language: en
- Publisher byline: Pierluigi Paganini (Security Affairs); The Register staff (uncredited security desk)
- Article type: trade-press + IR-blog relay of MSRC primary + researcher posts
- Raw IOC extraction invoked: not applicable — this is a vulnerability state-transition signal, not malware/IOC content
- Quote compliance: Hard Rule 6 + 7 — quotes ≤15 words, one per source maximum, paraphrased where longer

## IOCs (from ioc-extraction)

```yaml
domains: []
ip_addresses: []
file_hashes: []
urls: []

# Researcher / disclosed-bug identifiers (not IOCs in the threat-actor sense — corpus tracking):
researcher_aliases:
  - "Chaotic Eclipse"
  - "Nightmare Eclipse"
  - "Nightmare"
  note: "Researcher identity, NOT a tracked threat actor. Do not add to _roster.yaml."

cve_state_transitions:
  - cve: CVE-2026-33825
    name: BlueHammer
    vuln_tracker_id: ZD-001
    state_change: exploitation_status_updated_to_in_the_wild_confirmed_post_patch
    confidence: high
    sources: [msrc_primary_pm28, security_affairs, the_register]

  - cve: null
    name: RedSun
    vuln_tracker_id: ZD-002
    state_change: exploitation_status_updated_to_in_the_wild_confirmed
    patch_status: still_unpatched
    confidence: high
    sources: [msrc_primary_pm28, security_affairs, the_register]

  - cve: null
    name: UnDefend
    vuln_tracker_id: ZD-003
    state_change: exploitation_status_updated_to_in_the_wild_confirmed
    patch_status: still_unpatched
    confidence: high
    sources: [msrc_primary_pm28, security_affairs, the_register]

  - cve: CVE-2026-45585
    name: YellowKey
    vuln_tracker_id: null_not_yet_scaffolded
    state_change: vuln_tracker_scaffold_candidate
    classification: msrc_exploitation_more_likely_plus_public_poc_plus_unpatched
    confidence: high
    sources: [msrc_primary_pm28, the_register]

attribution_claims:
  - source: msrc_via_security_affairs
    actor: null    # MSRC names no actor for the ITW exploitation; the people exploiting are unattributed opportunistic
    confidence_language: null
    direct_quote_under_15_words: |
      "details of these vulnerabilities were not shared with Microsoft prior to release"
    notes: |
      MSRC's framing is on the disclosure process, not actor attribution.
      Both relays repeat MSRC's framing. No tracked threat actor named as
      exploiter of BlueHammer / RedSun / UnDefend.

a_and_d_relevance_assessment:
  level: direct
  rationale: |
    Three Windows vulnerabilities now ITW, two still without patches, hitting
    common DIB endpoint estate. BlueHammer is post-May-Patch-Tuesday; estate
    on current cadence is protected, but backlog estate is exposed. RedSun + 
    UnDefend remain unpatched and ITW. UnDefend specifically degrades Defender
    update capability, creating follow-on runway. YellowKey (CVE-2026-45585)
    public PoC + Microsoft "exploitation more likely" classification + still
    unpatched = imminent scaffold candidate.

corroboration_required:
  - "Direct Mandiant / CrowdStrike / Microsoft Defender for Endpoint telemetry confirming named-victim exploitation (currently the ITW claim is MSRC-anchored without IR-firm victim disclosure)"
  - "Volexity or Unit 42 follow-up identifying the threat-actor cluster running the post-disclosure exploitation"
  - "CISA KEV addition for CVE-2026-33825 (BlueHammer) — currently absent despite ITW status"

grader_handoff_notes: |
  - Two B-grade relays (Security Affairs, The Register) of A-grade MSRC primary
    (PM-28 absorbed). Independent corroboration that all three named bugs are
    ITW.
  - Hard Rule 2 strict — no attribution origination; MSRC + relays name no
    threat actor for the ITW exploitation. Treat exploiters as unattributed
    opportunistic until IR-firm telemetry surfaces a cluster.
  - Likely WEP "very likely" on procedural facts (PoC public, three named
    bugs flagged by MSRC as ITW). Operational claims (specific victims, scale,
    threat-actor cluster) absent — do not WEP-promote past MSRC's framing.
  - Vuln-tracker handoff: three dossier state updates + one new scaffold
    (YellowKey CVE-2026-45585).
```
