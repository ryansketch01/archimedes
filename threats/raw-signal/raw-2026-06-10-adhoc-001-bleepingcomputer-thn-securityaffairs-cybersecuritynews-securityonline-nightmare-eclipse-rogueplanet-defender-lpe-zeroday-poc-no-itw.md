---
raw_id: raw-2026-06-10-adhoc-001
collected_at: 2026-06-10T11:40:00-04:00
run_id: ad-hoc-rogueplanet-20260610-1140
collection_mode: on_demand
on_demand_command: breaking-vuln-sweep
post_am_brief_breaking: true   # 2026-06-10 morning brief shipped 08:00 EDT BEFORE this deep-collection; RoguePlanet was a 06:00 FLASH rule-out carried to AM brief as continuing-coverage (raw-2026-06-10-flash-0600-000). This raw-signal is the post-AM-brief deep collection on RoguePlanet specifically.
source:
  source_yaml_id: bleepingcomputer   # B-grade active; co-primary with strongest independent-verification framing (ThreatLocker)
  source_name: "BleepingComputer (Lawrence Abrams)"
  source_url: https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/
  published_at: 2026-06-09T19:11:00-04:00   # BC byline "June 9, 2026, 7:11 PM" — published evening before/around June PT; THN + SecurityAffairs followed 2026-06-10
  retrieval_method: WebFetch
secondary_sources:
  - id: thehackernews
    name: "The Hacker News (Ravie Lakshmanan)"
    url: https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html
    published_at: 2026-06-10
    grade: B   # provisional B per source-grades.yaml (thehackernews, provisional_since 2026-05-14, awaiting ratification)
    role: co-primary independent verification (cites Will Dormann reliability test) + sibling CVE-binding source
  - id: securityaffairs
    name: "Security Affairs (Pierluigi Paganini)"
    url: https://securityaffairs.com/193436/security/chaotic-eclipse-unveils-rogueplanet-exploit-targeting-fully-patched-windows.html
    published_at: 2026-06-10
    grade: B   # provisional B per source-grades.yaml (securityaffairs, provisional_since 2026-05-29, awaiting ratification)
    role: relay + adds researcher fatigue quotes + MSRC framing
  - id: cybersecuritynews
    name: "Cyber Security News (Guru Baran)"
    url: https://cybersecuritynews.com/windows-defender-0-day-exploit-rogueplanet/
    published_at: 2026-06-10
    grade: C_provisional   # FIRST Archimedes-corpus citation; NOT in source-grades.yaml; provisional C — see provisional_source_grades below
    role: adds TOCTOU framing + Huntress SIBLING-ITW claim (NOT RoguePlanet ITW)
  - id: securityonline
    name: "Security Online / SecurityOnline.info (Do Son)"
    url: https://securityonline.info/defender-zero-day-exploit-rogueplanet/
    published_at: 2026-06-10
    grade: C_provisional   # FIRST Archimedes-corpus citation; NOT in source-grades.yaml; provisional C — see provisional_source_grades below
    role: thin relay; corroborates PoC-only + success-rate quote + ISO-mount detail
provisional_source_grades:   # librarian handoff — two NEW sources surfaced this collection, not in source-grades.yaml
  - id: cybersecuritynews
    name: "Cyber Security News"
    proposed_grade: C
    category: media
    rationale: >
      First Archimedes-corpus citation. Indian-origin cybersecurity news
      aggregator (cybersecuritynews.com); Guru Baran byline. No prior
      Archimedes-corpus track record; trade-aggregator profile. Provisional
      C is the conservative starting grade per the same precedent as
      LayerX / Seqrite / Trendyol-Albayrak (unknown media/vendor without
      corpus track record). On THIS surface it is the SOLE source to relay
      a Huntress sibling-ITW claim (BlueHammer/RedSun/UnDefend in live
      attack chains) not present in the four other sources — single-source
      status on that specific sub-claim; do NOT propagate as corroborated.
      Operator may upgrade to B if subsequent surfaces show consistent
      accuracy, or hold at C if context-thin aggregation profile persists.
    awaiting_ratification: true
  - id: securityonline
    name: "Security Online (SecurityOnline.info)"
    proposed_grade: C
    category: media
    rationale: >
      First Archimedes-corpus citation. SecurityOnline.info; Do Son byline.
      No prior Archimedes-corpus track record; thin-relay trade-aggregator
      profile (this article is the shortest and least technically detailed
      of the five; no GitHub repo, no Microsoft response, no sibling-CVE
      bindings). Provisional C conservative starting grade per LayerX /
      Seqrite precedent. Operator may upgrade to B on demonstrated rigor,
      or hold at C.
    awaiting_ratification: true
match_reason:
  watchlist: []   # No A&D-prime named victim; Microsoft Defender is universally deployed including across DIB endpoints — structural exposure only
  actors: []      # Nightmare Eclipse / Chaotic Eclipse / Dead Eclipse is a SECURITY-RESEARCHER PSEUDONYM, NOT a tracked threat actor. Hard Rule 2 — NO roster cross-walk, NO _roster.yaml entry. Per finding-2026-05-29-0002 disposition (researcher pseudonym explicitly NOT actor-tiered).
  vulnerabilities:
    - "RoguePlanet (no CVE assigned)"   # 7th drop in Nightmare-Eclipse Defender/Windows series; tracked as researcher-series item, no CVE at collection
    # Sibling CVEs referenced (already in corpus _index.yaml):
    - CVE-2026-33825   # ZD-001 BlueHammer (patched)
    - CVE-2026-45498   # bound to UnDefend per THN/SecurityAffairs THIS surface — CONTRADICTS prior corpus (see source_contradiction)
    - CVE-2026-41091   # bound to RedSun per THN/SecurityAffairs THIS surface — CONTRADICTS prior corpus (see source_contradiction)
    - CVE-2026-45585   # YellowKey (patched June PT)
    - CVE-2020-17103   # MiniPlasma (re-patched June PT)
  tracked_vuln_index_state_transitions:
    - "ZD-003 UnDefend — RoguePlanet is a SEPARATE Defender issue and does NOT close UnDefend (per AM raw-2026-06-10-am-001 and 06:00 sweep). RoguePlanet is a candidate NEW researcher-series tracking entry (ZD-005 series candidate per AM handoff)."
  keywords: [RoguePlanet, Microsoft Defender, LPE, race condition, TOCTOU, NTFS junction, SMB, vhd, vhdx, mpengine, SysIO, Nightmare Eclipse, Chaotic Eclipse, Dead Eclipse, deadeclipse666, MSNightmare, projectnightcrawler, zero-day, no CVE, no patch, NT AUTHORITY SYSTEM, June 2026 Patch Tuesday, ThreatLocker, Will Dormann, Huntress]
triage_tags:
  - zero_day_no_patch_no_cve
  - microsoft_defender_lpe
  - poc_public_no_itw_confirmed_for_rogueplanet_specifically
  - nightmare_eclipse_researcher_series_7th_drop
  - post_am_brief_breaking_signal
  - researcher_pseudonym_not_tracked_actor_hard_rule_2
  - sibling_cve_binding_contradiction_with_prior_corpus
  - dropped_hours_after_june_patch_tuesday
  - independent_verification_threatlocker_will_dormann
  - huntress_sibling_itw_claim_single_source_cybersecuritynews
  - hard_rule_3_no_poc_reproduction
iocs_extracted: true
iocs_count: 9   # 5 sibling CVEs + 1 GitHub handle/repo + 1 blog domain + 1 self-hosted PoC domain + 1 PoC-removal-history note (GitHub/GitLab); no hashes/IPs/C2 in any source
text_word_count: 0   # grader to fill
promoted: false   # grader updates on promotion
ttl_expires_at: 2026-09-08T11:40:00-04:00   # 90-day retention per LEGAL-POLICY
---

# RoguePlanet — Microsoft Defender race-condition LPE zero-day (Nightmare Eclipse, 7th series drop, dropped hours after June 2026 Patch Tuesday)

**Co-primary:** BleepingComputer (Lawrence Abrams) — "Microsoft Defender RoguePlanet zero-day grants SYSTEM privileges" — 2026-06-09 19:11 EDT
**Co-primary:** The Hacker News (Ravie Lakshmanan) — "Microsoft Defender RoguePlanet zero-day" — 2026-06-10
**Secondary:** Security Affairs (Pierluigi Paganini) — 2026-06-10
**Secondary (provisional C):** Cyber Security News (Guru Baran) — 2026-06-10
**Secondary (provisional C):** Security Online / SecurityOnline.info (Do Son) — 2026-06-10

> **Context — this is post-AM-brief breaking signal.** The 2026-06-10 morning brief
> shipped at 08:00 EDT. RoguePlanet was surfaced at the 06:00 FLASH sweep
> (`raw-2026-06-10-flash-0600-000`), evaluated against Trigger 6, and **ruled out of
> FLASH** because no in-the-wild exploitation was confirmed (PoC-only). It was carried
> to the morning brief as a continuing-coverage UPDATE on the Nightmare-Eclipse
> researcher series. This raw-signal is the deeper ad-hoc collection requested after
> the AM brief shipped. **No new FLASH trigger fires** (see FLASH re-evaluation below).

---

## The headline fact, stated precisely

**RoguePlanet is a publicly-released proof-of-concept Microsoft Defender local privilege
escalation. It is NOT confirmed to be exploited in the wild.** All five sources agree on
PoC-only status for RoguePlanet specifically. Do NOT read "PoC public" as "ITW" — the
collector preserves this distinction per Hard Rule 2 disposition discipline established
in finding-2026-05-29-0002.

The single in-the-wild claim in the source set (Cyber Security News relaying Huntress)
attaches to the SIBLING tools — BlueHammer, RedSun, UnDefend — **not** to RoguePlanet.
See the ITW section below for the exact scoping.

---

## Key claims (five-source aggregate)

### What RoguePlanet is
- **Race-condition (TOCTOU) local privilege escalation in Microsoft Defender** that spawns
  a `cmd.exe` shell as `NT AUTHORITY\SYSTEM` on **fully patched Windows 10 and Windows 11**
  (including systems with the June 2026 Patch Tuesday updates installed; THN/BC reference
  build KB5094126 / Canary).
- Mechanism (conceptual, detection-level only per Hard Rule 3): a time-of-check/time-of-use
  race in Defender's **file remediation / quarantine engine**. The exploit redirects a
  privileged Defender file-write operation via **NTFS junction points** (path redirection /
  inadequate path validation during privileged write) to land code execution as SYSTEM.
  Cyber Security News labels it TOCTOU explicitly.
- **Origin → downgrade narrative (per BleepingComputer):** originally developed as a
  *remote* code execution abusing Defender's handling of files on **remote SMB shares** and
  **.vhd(x)** images (coerce a victim to open a `.vhd(x)` hosted on a remote SMB server →
  Defender mishandles its own file operations → RCE). The researcher states it was
  **downgraded to LPE** after Microsoft **silently hardened the `mpengine!SysIO*` API in
  mid-May 2026**, which blocked the junction-based remote path.

### Affected / not-affected
- **Affected:** Windows 10 and Windows 11, fully patched through June 2026 Patch Tuesday.
- **Windows Server:** described as vulnerable in principle but the **public PoC is
  non-functional** on Server editions because **standard users cannot mount ISO images**
  there (the PoC's initialization relies on mounting an ISO). THN, Security Affairs,
  Security Online all note this.

### Exploitation status — RoguePlanet specifically: PoC-only, NO confirmed ITW
- BleepingComputer: PoC demonstrated by the researcher and **independently verified by
  ThreatLocker**; **not** confirmed actively exploited.
- The Hacker News: PoC publicly released; researcher Will Dormann reliability-tested it
  ("worked on the first attempt for me" — reportedly not 100% reliable). Framed as
  "active PoC released, not yet widely exploited in the wild."
- Security Affairs: "Proof-of-Concept only — not actively exploited in the wild at
  publication date."
- Security Online: "Proof-of-Concept only … not actively exploited in operational attacks."

### The one ITW claim is about the SIBLINGS, not RoguePlanet (single-source, provisional C)
- **Cyber Security News (Guru Baran) only** relays a **Huntress** claim that **earlier**
  tooling from this researcher — **BlueHammer, RedSun, and the Defender-disruption tool
  UnDefend** — has been **observed in live attack chains**. This is consistent with the
  corpus state-transition already graded in finding-2026-05-29-0002 (three siblings to
  ITW per MSRC + relays). **It is NOT a RoguePlanet ITW claim.** Single-source
  (Cyber Security News, provisional C) on the Huntress relay specifically — the other four
  sources do not carry it. Surface; do not corroborate.

### CVE / patch status
- **No CVE assigned. No patch. No public Microsoft advisory** as of collection. Zero-day
  status confirmed across all five sources.

### Researcher identity (pseudonym — NOT a tracked actor)
- Public aliases: **Chaotic Eclipse** (THN's "primary public name") / **Nightmare Eclipse**
  / **Dead Eclipse** / **deadeclipse666**.
- GitHub account: **`MSNightmare`**; repository **`MSNightmare/RoguePlanet`** (defanged in
  IOC block; not linked).
- Blog: **deadeclipse666.blogspot[.]com** (defanged).
- After GitHub and GitLab removed previous repositories at Microsoft's request, the
  researcher is self-hosting PoC code at **projectnightcrawler[.]dev** (defanged; per BC).
- Researcher claims to be a **former Microsoft employee** (per Krebs carry-context in
  AM raw-2026-06-10-am-001; Microsoft has not confirmed).
- Persona signaling: prior blog post used an Albert Wesker (Resident Evil) image
  (per AM carry-context).

### Researcher quotes (Hard Rule 6 — capped at ≤15 words each, one per source)
- Seed/BC/THN/Security Online race-condition quote (verbatim, the canonical line):
  *"The exploit is a race condition, so it's a hit or miss."* (13 words)
- Security Affairs adds (separate quote, ≤15 words):
  *"writing this PoC genuinely drained my soul."* (7 words)
- Microsoft / MSRC framing relayed by THN (paraphrase, not quoted beyond limit): public
  disclosures "never justifiable"; revoked the researcher's MSRC account; **no intention
  to pursue legal action against security researchers**; advocates Coordinated
  Vulnerability Disclosure.

### Disclosure-dispute context (carry-forward; not new)
- Continuation of the ongoing Nightmare-Eclipse vs. Microsoft MSRC / bug-bounty dispute
  already tracked in finding-2026-06-02-0010 and finding-2026-05-29-0002. Grievances cited:
  dismissed reports, lack of compensation, MSRC account revocation. Microsoft previously
  threatened the Digital Crimes Unit then backed down (clarifying it would only report to
  authorities if researchers "break the law"). Researcher has pledged a further
  "bone-shattering" drop on **July 14, 2026** (next Patch Tuesday).

---

## Sibling-series cross-reference (Nightmare-Eclipse Defender/Windows series)

RoguePlanet is the **7th drop** in the researcher series Archimedes already tracks. Corpus
mapping (per `threats/vulnerabilities/_index.yaml` + dossiers):

| Codename | CVE (per THIS surface) | Corpus index | Type | Patch status (corpus) | ITW (corpus) |
|---|---|---|---|---|---|
| BlueHammer | CVE-2026-33825 | ZD-001 | LPE | patched (May PT) | ITW per finding-2026-05-29-0002 (meta-statement A2; underlying-fact roughly-even per red-team) |
| RedSun | CVE-2026-41091 *(per THN/SecAffairs today)* | ZD-002 | LPE | unpatched | ITW (same caveats) |
| UnDefend | CVE-2026-45498 *(per THN/SecAffairs today)* | ZD-003 | DoS / Defender-update block | unpatched | ITW (same caveats) |
| YellowKey | CVE-2026-45585 | YELLOWKEY dossier | BitLocker bypass (WinRE) | patched (June PT) | PoC public |
| GreenPlasma | CVE-2026-45586 | GREENPLASMA dossier | LPE (CTFMON) | patched (June PT) | "actively exploited" per BC single-source |
| MiniPlasma | CVE-2020-17103 | MiniPlasma dossier | LPE (Cloud Files Mini Filter Driver) | re-patched (June PT, incomplete prior fix) | PoC public / ITW per BC single-source |
| **RoguePlanet** | **none assigned** | **NEW (ZD-005 series candidate)** | **LPE (race condition, Defender file remediation)** | **unpatched zero-day** | **PoC-only; NO confirmed ITW** |

**Vuln-tracker handoff:** RoguePlanet is a candidate new tracking entry (ZD-005 series per
AM raw-2026-06-10-am-001 handoff item 3). It is a SEPARATE Defender issue and does NOT close
ZD-003 UnDefend.

---

## Source contradiction surfaced (Hard Rule 8 class — sibling CVE binding)

THN and Security Affairs on THIS surface bind:
- **UnDefend ⇔ CVE-2026-45498**
- **RedSun ⇔ CVE-2026-41091**

This **CONTRADICTS** the prior corpus state and is itself an inversion already documented:
- `_index.yaml` ZD-002 (RedSun) and ZD-003 (UnDefend) both carry `cve: null`.
- finding-2026-05-21-0001 (SecurityWeek) bound **RedSun ⇔ CVE-2026-45498** and
  **UnDefend ⇔ CVE-2026-41091** — i.e., the **opposite** pairing to today's THN/SecAffairs
  binding (the two CVEs are swapped between the two codenames across reporting cycles).
- finding-2026-05-29-0002 already capped this binding layer at **B3** pending vuln-tracker
  reconciliation and flagged reporter codename↔CVE mapping drift (analyst ACH H3/H4).

**Grader/vuln-tracker disposition:** Do NOT silently choose a binding. This collection adds a
THIRD distinct mapping observation to the existing contradiction record. The codename↔CVE
mapping for RedSun/UnDefend remains unreconciled; this raw-signal reinforces the
"reporters struggle to keep the mapping straight" red-team meta-signal (finding-2026-05-29-0002 W4).

---

## First-party Splunk check (Mode-4 priority, Hard Rule 8)

Query executed against `archimedes` + `defenseclaw_local`:

```
index=defenseclaw_local OR index=archimedes ("RoguePlanet" OR "Rogue Planet" OR
"Nightmare Eclipse" OR "deadeclipse666" OR "Chaotic Eclipse" OR "cmd.exe" OR
"NT AUTHORITY\SYSTEM") NOT sourcetype=archimedes:operation  (earliest -30d)
```

**Result: 0 events.** First-party telemetry silent on all RoguePlanet / Nightmare-Eclipse
terms and on the LPE behavioral strings over 30 days. **Hard Rule 8: silence is not
disconfirming** — absence of a SIEM signal does not refute the PoC-only status nor confirm
absence of exploitation; defender-side hunt would be required to assert either. First-party
precedence not applied (no attestation to bump or contradict).

---

## FLASH re-evaluation (advisory; confirms 06:00 sweep ruling holds)

- **Trigger 6 (zero-day, no patch, CVSS ≥8.0 or widely-deployed, + exploitation
  confirmed/imminent):** RoguePlanet is zero-day + no patch + arguably widely-deployed
  (Defender ships on all Windows). BUT the **exploitation_confirmed_or_imminent prong FAILS** —
  PoC-only, no confirmed ITW for RoguePlanet. **Trigger 6 does NOT fire.** Same disposition as
  the 06:00 sweep and as the Cisco Unified CM CVE-2026-20230 PoC-alone precedent (2026-06-04).
- **Trigger 1 (critical CVE + active exploitation + A-grade):** No CVE, no CVSS, no A-grade
  ITW confirmation. FAILS.
- **Trigger 2 / 4 (tracked-actor):** Researcher pseudonym not in `_roster.yaml`. FAILS.
- **Trigger 3 (first-party IOC hit):** Splunk 0 hits. FAILS.
- **Trigger 5 (A&D-sector campaign):** No A&D-prime victim. FAILS.
- **Critical override:** 0 of 4 conditions (no CVSS 10.0, no tracked actor, no A&D-watchlist
  hit, no confirmed ITW). Does NOT apply.

**Net: 0 FLASH triggers fire. Disposition = continuing-coverage / vuln-tracker handoff for the
next scheduled brief (afternoon 16:00) — already partially carried in the 08:00 morning brief.**

---

## Extraction notes

- Language: en
- Article types: vendor/security-news report (BC, THN, Security Affairs) + trade-aggregator
  (Cyber Security News, Security Online)
- Raw IOC extraction invoked: yes — researcher PoC handles/domains + sibling CVEs only;
  **no host IOCs (no IPs, no domains-as-C2, no file hashes, no Defender signature names)**
  published in any of the five sources. The PoC-hosting handles/domains are recorded as
  reference/attribution context, defanged, NOT as malicious C2.
- **Hard Rule 3 (no exploitation, ever):** mechanism captured at conceptual/detection level
  only (race condition / TOCTOU / NTFS junction path-redirection / SMB+.vhd origin /
  mpengine!SysIO hardening). **NO PoC code, NO exploit steps, NO payload, NO reproduction
  walkthrough** copied. PoC repo referenced by name only (defanged), not linked or mirrored.
- **Hard Rule 2 (no novel attribution):** Nightmare-Eclipse / Chaotic Eclipse is a
  security-researcher pseudonym, recorded as authored-by context only. NOT added to
  `_roster.yaml`; NOT treated as a tracked threat actor. The Huntress sibling-ITW claim is
  attributed to its single source (Cyber Security News relaying Huntress), not asserted by
  Archimedes.
- **Hard Rule 6 (quote limit):** researcher quotes capped ≤15 words, ≤1 per source.
- No credentials, PII, or breach data surfaced.
- Cross-corpus prior surfaces:
  - finding-2026-06-02-0010 — Nightmare Eclipse 0day researcher dispute / Bitskrieg / Secure Boot / BitLocker forthcoming-claim
  - finding-2026-06-03-PM-005 — TheRegister Microsoft disclosure-policy / Askar VS Code / Nightmare-Eclipse Bitskrieg linkage
  - finding-2026-05-29-0002 — Chaotic Eclipse three-sibling ITW state transition (BlueHammer/RedSun/UnDefend) + CVE-binding contradiction
  - finding-2026-05-21-0001 — UnDefend/RedSun SecurityWeek CVE name-binding (inverse mapping to today's)
  - finding-2026-06-10-0001 — June Patch Tuesday (YellowKey/GreenPlasma/MiniPlasma patched)
  - raw-2026-06-10-flash-0600-000 — 06:00 FLASH sweep where RoguePlanet was first surfaced + ruled out
  - raw-2026-06-10-am-001 — AM pre-brief sweep carrying RoguePlanet as continuing-coverage

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-06-10-adhoc-001
  source_url: https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-rogueplanet-zero-day-grants-system-privileges/
  extracted_at: 2026-06-10T11:40:00-04:00
  extracted_by: collector
  target_actor_id: null   # researcher pseudonym, NOT a tracked actor — Hard Rule 2
  text_word_count: 0      # grader to fill from source bodies

indicators:
  - id: raw-cve-2026-33825
    type: cve
    value: CVE-2026-33825
    defanged_original: null
    first_seen: 2026-03
    last_seen: 2026-06
    role: historical   # sibling — BlueHammer, patched May PT; referenced as series context
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "Sibling BlueHammer LPE; patched May Patch Tuesday; ZD-001."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "Corpus ZD-001. CVSS 7.8 per Cyber Security News."
  - id: raw-cve-2026-45498
    type: cve
    value: CVE-2026-45498
    defanged_original: null
    first_seen: 2026-05
    last_seen: 2026-06
    role: ambiguous   # codename binding contested — UnDefend per THN/SecAffairs today; RedSun per SecurityWeek 2026-05-21
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "Bound to UnDefend by THN + Security Affairs on this surface; bound to RedSun by SecurityWeek 2026-05-21 (inverted). Corpus _index.yaml carries cve:null for both ZD-002/ZD-003."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "SOURCE CONTRADICTION — see source-contradiction section. Do not silently bind. Vuln-tracker reconciliation pending (carried from finding-2026-05-29-0002)."
  - id: raw-cve-2026-41091
    type: cve
    value: CVE-2026-41091
    defanged_original: null
    first_seen: 2026-05
    last_seen: 2026-06
    role: ambiguous   # codename binding contested — RedSun per THN/SecAffairs today; UnDefend per SecurityWeek 2026-05-21
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "Bound to RedSun by THN + Security Affairs on this surface; bound to UnDefend by SecurityWeek 2026-05-21 (inverted). Corpus _index.yaml carries cve:null for both."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "SOURCE CONTRADICTION — see above. Vuln-tracker reconciliation pending."
  - id: raw-cve-2026-45585
    type: cve
    value: CVE-2026-45585
    defanged_original: null
    first_seen: 2026-05
    last_seen: 2026-06
    role: historical   # sibling YellowKey, patched June PT
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "Sibling YellowKey BitLocker bypass (WinRE); patched June Patch Tuesday."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "Corpus YELLOWKEY dossier. CVSS 6.8."
  - id: raw-cve-2020-17103
    type: cve
    value: CVE-2020-17103
    defanged_original: null
    first_seen: 2020
    last_seen: 2026-06
    role: historical   # sibling MiniPlasma; 2020-cohort CVE re-patched June PT for incomplete prior fix
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "Sibling MiniPlasma LPE (Cloud Files Mini Filter Driver); incomplete prior fix re-patched June PT."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "Corpus MiniPlasma dossier."
  - id: raw-other-github-msnightmare-rogueplanet
    type: other
    type_detail: code_repository_handle_poc_hosting
    value: "github[.]com/MSNightmare/RoguePlanet"
    defanged_original: "github.com/MSNightmare/RoguePlanet"
    first_seen: 2026-06
    last_seen: 2026-06
    role: ambiguous   # PoC hosting / researcher attribution context, NOT malicious infrastructure
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "GitHub account MSNightmare hosting RoguePlanet PoC (per THN/Security Affairs). Defanged. Hard Rule 3 — referenced by name, NOT linked or mirrored."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "PoC-hosting handle, NOT C2. Prior GitHub/GitLab repos removed at Microsoft request; researcher migrating to self-hosting."
  - id: raw-domain-deadeclipse666-blogspot
    type: domain
    value: deadeclipse666.blogspot.com
    defanged_original: "deadeclipse666.blogspot[.]com"
    first_seen: 2026-05
    last_seen: 2026-06
    role: ambiguous   # researcher's blog / disclosure channel, NOT malicious C2
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "Researcher disclosure blog (per THN, Security Affairs, Security Online). Defanged."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "Disclosure channel, NOT C2. blogspot.com is a benign hosting platform; the subdomain is the researcher's persona handle."
  - id: raw-domain-projectnightcrawler-dev
    type: domain
    value: projectnightcrawler.dev
    defanged_original: "projectnightcrawler[.]dev"
    first_seen: 2026-06
    last_seen: 2026-06
    role: ambiguous   # self-hosted PoC distribution after GitHub/GitLab takedowns, NOT malicious C2
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "Self-hosted PoC distribution site per BleepingComputer, used after GitHub + GitLab removed prior repos at Microsoft's request. Defanged. Hard Rule 3 — NOT linked or mirrored."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "PoC-hosting domain, NOT C2. Recorded for defender awareness / takedown-tracking only."
  - id: raw-other-rogueplanet-no-cve
    type: other
    type_detail: unassigned_vulnerability_codename
    value: "RoguePlanet (Microsoft Defender race-condition LPE; no CVE)"
    defanged_original: null
    first_seen: 2026-06
    last_seen: 2026-06
    role: ambiguous
    campaign: "Nightmare-Eclipse / Chaotic Eclipse Windows zero-day series (7th drop)"
    related_malware: []
    source_brief: raw-2026-06-10-adhoc-001
    context_excerpt: "RoguePlanet Defender LPE, no CVE assigned, no patch, PoC public, no confirmed ITW. Spawns cmd.exe as NT AUTHORITY\\SYSTEM on fully-patched Win10/11."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (researcher pseudonym)"
    notes: "ZD-005-series tracking candidate. SMB+.vhd(x) RCE origin downgraded to LPE after mpengine!SysIO* hardening (mid-May 2026)."

attribution_claims:
  - claimed_actor: null   # researcher pseudonym, NOT a tracked threat actor — Hard Rule 2
    ioc_ids:
      - raw-other-rogueplanet-no-cve
      - raw-other-github-msnightmare-rogueplanet
      - raw-domain-deadeclipse666-blogspot
      - raw-domain-projectnightcrawler-dev
      - raw-cve-2026-33825
      - raw-cve-2026-45498
      - raw-cve-2026-41091
      - raw-cve-2026-45585
      - raw-cve-2020-17103
    claimed_by_source: [bleepingcomputer, thehackernews, securityaffairs, cybersecuritynews, securityonline]
    attribution_confidence_in_source: "authored-by (self-claimed researcher pseudonym); NOT a threat-actor attribution"
    requires_grading: false   # not a tracked-actor attribution; Hard Rule 2 — do NOT roster-tier
    notes: >
      "Nightmare Eclipse / Chaotic Eclipse / Dead Eclipse / deadeclipse666"
      is a SECURITY-RESEARCHER pseudonym (GitHub MSNightmare). Recorded as
      authored-by context only. Do NOT add to _roster.yaml. Do NOT treat as
      adversary attribution. Per finding-2026-05-29-0002 disposition.
  - claimed_actor: null
    ioc_ids: [raw-cve-2026-33825, raw-cve-2026-41091, raw-cve-2026-45498]
    claimed_by_source: [cybersecuritynews]   # SINGLE-SOURCE (provisional C) relaying Huntress
    attribution_confidence_in_source: "Huntress 'observed in live attack chains' (sibling tools BlueHammer/RedSun/UnDefend) — relayed by Cyber Security News only"
    requires_grading: true
    notes: >
      SIBLING ITW claim — NOT a RoguePlanet ITW claim. Single-source
      (Cyber Security News, provisional C) relaying Huntress. The other four
      sources do not carry it. Consistent with prior corpus sibling-ITW state
      transition (finding-2026-05-29-0002) but adds a NEW named telemetry
      source (Huntress) — grader to assess whether this independently
      corroborates the prior MSRC-load-bearing sibling-ITW claim or is a
      single-source relay requiring veto. RoguePlanet itself remains PoC-only.

benign_filtered:
  - value: bleepingcomputer.com
    reason: reporting_publisher
  - value: thehackernews.com
    reason: reporting_publisher
  - value: securityaffairs.com
    reason: reporting_publisher
  - value: cybersecuritynews.com
    reason: reporting_publisher
  - value: securityonline.info
    reason: reporting_publisher
  - value: microsoft.com
    reason: reference_vendor_site
  - value: github.com
    reason: reference_platform   # platform itself benign; MSNightmare/RoguePlanet path recorded as ambiguous-role IOC
  - value: gitlab.com
    reason: reference_platform

extraction_warnings:
  - type: ambiguous_role
    ioc_id: raw-other-github-msnightmare-rogueplanet
    detail: "PoC-hosting handle, not malicious C2. Role 'ambiguous' — recorded for takedown/attribution awareness; defender should NOT block-list github.com wholesale."
  - type: source_contradiction
    ioc_id: raw-cve-2026-45498
    detail: "Codename↔CVE binding (UnDefend vs RedSun) contradicts SecurityWeek 2026-05-21 (inverted) and corpus _index.yaml (cve:null). Do not resolve at extraction; vuln-tracker reconciliation pending per finding-2026-05-29-0002."
  - type: single_source_itw_subclaim
    ioc_id: raw-cve-2026-33825
    detail: "Sibling-ITW (Huntress via Cyber Security News only). NOT RoguePlanet ITW. Grader: assess single-source veto on the Huntress relay; provisional-C origin."

hashes: []
domains:   # researcher disclosure/PoC-hosting domains only — recorded above as ambiguous-role indicators, NOT malicious C2
  - deadeclipse666.blogspot.com
  - projectnightcrawler.dev
ipv4: []
urls: []
```
