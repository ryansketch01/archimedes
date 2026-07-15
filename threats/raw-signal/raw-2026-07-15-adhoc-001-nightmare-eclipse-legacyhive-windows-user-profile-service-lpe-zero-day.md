---
raw_id: raw-2026-07-15-adhoc-001
collected_at: 2026-07-15T16:20:00-04:00
run_id: adhoc-nightmare-eclipse-hunt-20260715
collection_mode: on_demand
on_demand:
  command: /investigate
  target: "Nightmare Eclipse (persona / vuln-drop series)"
  invoked_by: orchestrator (operator Ryan)
source:
  # Multi-source item — primary reporting outlets listed; researcher self-published claim is the origin
  primary_report:
    source_yaml_id: the-register
    source_name: The Register (Security)
    source_url: https://www.theregister.com/security/2026/07/15/microsofts-serial-tormentor-drops-legacyhive-0-day/5271723
    published_at: 2026-07-15T00:00:00-04:00
  corroborating_reports:
    - source_name: The Hacker News
      source_url: https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html
    - source_name: Cybernews
      source_url: https://cybernews.com/security/nightmare-eclipse-windows-legacyhive-privilege-escalation-bug/
    - source_name: SecurityOnline
      source_url: https://securityonline.info/legacyhive-windows-exploit/
    - source_name: CybersecurityNews
      source_url: https://cybersecuritynews.com/legacyhive-windows-0-day-vulnerability/
    - source_name: Cyderes (Howler Cell)
      source_url: https://www.cyderes.com/howler-cell/legacyhive-windows-user-profile-loading-vulnerability
    - source_name: Cryptika Cybersecurity
      source_url: https://www.cryptika.com/new-legacyhive-windows-0-day-vulnerability-allows-users-to-load-another-users-registry/
    - source_name: OffSeq Threat Radar
      source_url: https://radar.offseq.com/threat/nightmare-eclipse-could-be-dropping-his-big-promis-f402efe8c31193ec
  origin_channel:
    # Researcher self-hosted (existence noted only — NOT fetched; Hard Rule 3)
    - blog.projectnightcrawler.dev
    - git.projectnightcrawler.dev/NightmareEclipse/LegacyHive
match_reason:
  watchlist: []
  actors: ["Nightmare Eclipse", "Chaotic Eclipse"]   # persona tracked via vuln-drop series; NOT a formal _roster.yaml actor
  vulnerabilities: []        # no CVE assigned to LegacyHive as of collection
  keywords: [LegacyHive, "User Profile Service", "arbitrary hive load", "privilege escalation", "zero-day", "Nightmare Eclipse"]
triage_tags:
  - on_demand
  - actor_hunt
  - nightmare_eclipse_series
  - new_vuln_disclosure
  - windows_lpe
  - zero_day_no_patch          # maps to FLASH Trigger 6 candidate — grader/briefer to adjudicate; collector does not grade
  - poc_public
  - vendor_silent
iocs_extracted: true
iocs_count: 4                  # researcher-controlled publishing infra + persona handles; NO malicious C2/hashes/CVE
text_word_count: 0             # full article bodies not retrieved (Cybernews 403; The Register + THN via WebFetch structured summary); synthesis below
promoted: true
promoted_to_finding: finding-2026-07-15-0002
promoted_at: 2026-07-15T16:40:00-04:00
ttl_expires_at: 2026-10-13T16:20:00-04:00   # 90 days per LEGAL-POLICY retention
---

# Nightmare Eclipse drops "LegacyHive" — unpatched Windows User Profile Service LPE zero-day (8th/9th drop in series)

## What this is

On or about **2026-07-14**, within hours of Microsoft's July Patch Tuesday, the pseudonymous
researcher **Nightmare Eclipse** (aka **Chaotic Eclipse**) publicly released a new Windows
zero-day proof-of-concept dubbed **LegacyHive**. It is a **local privilege escalation (LPE)**
flaw in the **Windows User Profile Service** (`profsvc` / ProfSvc) and the Windows registry
user-hive loading path. This is the researcher's continuation of the Microsoft-grudge campaign
that ran the 7-drop CVE series closed 2026-07-09 (RoguePlanet CVE-2026-50656 was the last of
that set) plus the June GreatXML BitLocker bypass. Multiple outlets characterize LegacyHive as
the researcher's newest public repository in the series.

**This is a genuine, corroborated new drop — distinct from anything in the tracked baseline.**

## Vulnerability facts (per reporting — collector does not grade)

- **Name:** LegacyHive
- **Affected product/component:** Windows User Profile Service (the component that loads/unloads
  user profiles at sign-in) and Windows registry user hives (`usrclass.dat` in the public PoC).
- **Class:** Local Privilege Escalation — "arbitrary registry hive loading" / arbitrary hive-load
  elevation of privilege.
- **Mechanism (as described in public reporting, high level):** a carefully timed path-switching
  (race / TOCTOU-style) trick causes the User Profile Service to mount **another user's** registry
  hive — including an administrator's — into the attacker's own classes root.
- **CVE:** **None assigned** as of collection (2026-07-15).
- **CVSS:** **Not provided** by any source.
- **Affected versions:** Reported to work on **all currently supported Windows desktop and server
  installations**, including systems with the **July 2026 Patch Tuesday** updates applied.
- **Patch status:** **Unpatched zero-day** at disclosure. No Microsoft advisory, no CVE, no fix.
- **In-the-wild exploitation:** **None reported.** Analysts caution that capable actors could
  reverse-engineer the components the researcher withheld.
- **PoC:** **Public, but deliberately stripped down** per the researcher. The public version is
  said to require an additional standard-user credential plus a third username (which can be an
  administrator account) and to work only with the `usrclass.dat` hive; the researcher claims the
  original/unpublished variant needed no extra credentials and handled multiple hive types.
  **PoC existence noted only — code NOT fetched, mirrored, or reproduced (Hard Rule 3).**

## Vendor / dispute posture

- **Microsoft (MSRC): silent.** Both The Register and The Hacker News state they contacted
  Microsoft and had no response at publication. No MSRC advisory, no CVE, no confirmation/denial.
- **Researcher-dispute / "does it live up to the hype" angle:** LegacyHive fell short of the
  "bone-shattering" mass drop the researcher had promised for July 14 (a placeholder repo with only
  a license + README reportedly appeared on the date first). Independent researcher **Matei
  Badanoiu** is quoted assessing it as a useful post-compromise primitive while questioning whether
  it amounts to full system compromise as hyped. The Register's framing: not the promised
  "haymaker." (One quote per source; Register headline paraphrased.)

## Relationship to tracked baseline (do NOT re-report as new)

- Closed 7-drop CVE series (patched by 2026-07-09): BlueHammer, RedSun, UnDefend, YellowKey,
  GreenPlasma, MiniPlasma, RoguePlanet. **LegacyHive is NOT one of these** — it is a new,
  post-2026-07-09 disclosure.
- The standing 2026-07-09 watch signal (a promised "batch of Defender memory-corruption
  vulnerabilities" 8th drop) is **NOT** what materialized on July 14. LegacyHive targets the
  **User Profile Service**, not Defender memory corruption. The Defender memory-corruption batch
  and BitSkrieg (Secure Boot / BitLocker, co-claimed with JonasLyk) both remain **unreleased**
  per reporting — still open standing signals.
- GreatXML (June BitLocker/WinRE bypass) is a separate, prior drop — also distinct from LegacyHive.

## Relevance to A&D target profile

No A&D-specific targeting or victimology is claimed — this is a general Windows LPE PoC, not a
campaign. Relevance is **structural**: an unpatched, publicly-PoC'd SYSTEM-adjacent LPE affecting
fully-patched Windows desktop/server fleets is a post-compromise escalation primitive directly
applicable to any large ITAR-regulated Windows enterprise. Grader/vuln-tracker to adjudicate
priority; briefer to decide brief-worthiness.

---

## Extraction notes

- Language: en
- Article type: security news (multi-outlet) reporting a researcher self-published disclosure
- Publisher independence: HIGH at outlet level (The Register, THN, Cybernews, SecurityOnline,
  CybersecurityNews, Cyderes, Cryptika, OffSeq are separate publishers). **Evidence-basis
  independence: LOW** — all reporting traces to the same origin (Nightmare Eclipse's own PoC repo +
  blog post). Treat corroboration as "many outlets relaying one primary claimant," not multiple
  independent technical validations. Grader should apply single-originating-claim discipline.
- MSRC confirmation: absent (vendor silent). No CVE, no CVSS, no patch — all "not assigned / not
  provided" per every source checked.
- Raw IOC extraction invoked: yes (below). No malicious atomic IOCs exist (no C2, no hashes, no
  CVE); only researcher-controlled publishing infrastructure + persona handles.
- Hard Rule 3 compliance: PoC existence recorded; exploit/PoC code NOT retrieved or reproduced.
  `git.projectnightcrawler.dev` repo path noted for existence only — not fetched.
- Splunk first-party check: NOT run. No queryable atomic IOC (no CVE/hash/C2). Persona publishing
  domains could be swept if the operator wants outbound-connection hunting, but they are
  researcher-controlled, not attacker C2 — low value. Flagged as optional, not executed.
- Source-health notes: WebFetch on cybernews.com returned HTTP 403 (cybernews is WebFetch-blocked
  from this host; corroboration obtained via WebSearch snippet + independent Register/THN fetches).
  The Register (2026-07-15) and The Hacker News fetched successfully via WebFetch. No source-health
  state changes required for scheduled feeds (this was an ad-hoc WebSearch/WebFetch hunt, not an
  RSS sweep).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: nightmare-eclipse-legacyhive-2026-07
  source_url: https://www.theregister.com/security/2026/07/15/microsofts-serial-tormentor-drops-legacyhive-0-day/5271723
  extracted_at: 2026-07-15T16:20:00-04:00
  extracted_by: collector
  target_actor_id: null      # Nightmare Eclipse is a tracked persona/series, NOT a formal _roster.yaml actor
  text_word_count: 0         # full article bodies not retrieved; structured-summary synthesis

indicators:
  - id: raw-domain-projectnightcrawler-dev
    type: domain
    value: projectnightcrawler.dev
    defanged_original: null
    resolved_ip: null
    first_seen: 2026-06
    last_seen: 2026-07
    role: historical           # researcher-controlled self-hosted publishing platform (blog), NOT victim-facing malicious infra
    campaign: "Nightmare Eclipse Windows zero-day series"
    related_malware: []
    source_brief: nightmare-eclipse-legacyhive-2026-07
    context_excerpt: >
      "Researcher moved to self-hosted blog.projectnightcrawler.dev after repeated GitHub/GitLab
      repo takedowns; LegacyHive announced there."
    attribution_in_text: "Nightmare Eclipse / Chaotic Eclipse (persona self-attribution)"
    notes: "Publishing/identity infrastructure, not C2. Existence recorded; not fetched (Hard Rule 3)."

  - id: raw-domain-git-projectnightcrawler-dev
    type: domain
    value: git.projectnightcrawler.dev
    defanged_original: null
    resolved_ip: null
    first_seen: 2026-07
    last_seen: 2026-07
    role: historical           # self-hosted code repo host for the stripped PoC
    campaign: "Nightmare Eclipse Windows zero-day series"
    related_malware: []
    source_brief: nightmare-eclipse-legacyhive-2026-07
    context_excerpt: >
      "git.projectnightcrawler.dev/NightmareEclipse/LegacyHive named as the PoC host in reporting."
    attribution_in_text: "Nightmare Eclipse (persona self-attribution)"
    notes: "PoC repo path — EXISTENCE ONLY, not fetched/mirrored (Hard Rule 3). Not attacker C2."

  - id: raw-domain-deadeclipse666-blogspot-com
    type: domain
    value: deadeclipse666.blogspot.com
    defanged_original: null
    resolved_ip: null
    first_seen: 2026-04
    last_seen: 2026-07
    role: historical
    campaign: "Nightmare Eclipse Windows zero-day series"
    related_malware: []
    source_brief: nightmare-eclipse-legacyhive-2026-07
    context_excerpt: >
      "Persona historically published through deadeclipse666.blogspot.com."
    attribution_in_text: "Nightmare Eclipse / deadeclipse666 (persona self-attribution)"
    notes: "Legacy publishing channel / persona handle. Identity indicator, not malicious infra."

  - id: raw-other-github-msnightmare
    type: other
    type_detail: account_handle
    value: "github.com/MSNightmare"
    defanged_original: null
    resolved_ip: null
    first_seen: 2026-04
    last_seen: 2026-07
    role: historical
    campaign: "Nightmare Eclipse Windows zero-day series"
    related_malware: []
    source_brief: nightmare-eclipse-legacyhive-2026-07
    context_excerpt: >
      "GitHub account MSNightmare used historically before repeated takedowns."
    attribution_in_text: "Nightmare Eclipse (persona self-attribution)"
    notes: "Persona account handle; reportedly repeatedly removed. Identity indicator, not IOC-for-blocking."

attribution_claims:
  - claimed_actor: "Nightmare Eclipse (self-attributed persona)"
    ioc_ids:
      - raw-domain-projectnightcrawler-dev
      - raw-domain-git-projectnightcrawler-dev
      - raw-domain-deadeclipse666-blogspot-com
      - raw-other-github-msnightmare
    claimed_by_source: "researcher self-publication (relayed by the-register, thn, et al.)"
    attribution_confidence_in_source: "self-claimed / persona continuity per press"
    requires_grading: true

benign_filtered:
  - value: microsoft.com
    reason: reference_site (affected vendor, not an IOC)
  - value: theregister.com
    reason: reference_site (reporting publisher)
  - value: thehackernews.com
    reason: reference_site (reporting publisher)

extraction_warnings:
  - type: no_malicious_atomic_iocs
    ioc_id: null
    detail: >
      LegacyHive is a PoC disclosure, not an intrusion campaign. No CVE, no CVSS, no file hashes,
      no attacker C2, no victim infrastructure exist. All extracted indicators are
      researcher-controlled publishing/identity infrastructure. Grader/actor-profiler should treat
      these as persona-tracking identity indicators, NOT block-list IOCs.
  - type: evidence_basis_independence_low
    ioc_id: null
    detail: >
      Many outlets, one originating claimant. Corroboration is publisher-level, not independent
      technical validation. Vendor (MSRC) silent — no CVE/CVSS/patch to anchor grading.
```
