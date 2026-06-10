---
raw_id: raw-2026-06-10-am-001
collected_at: 2026-06-10T07:35:00-04:00
run_id: pre-brief-20260610-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer  # primary B-grade with strongest ITW framing on GreenPlasma + MiniPlasma
  source_name: "BleepingComputer (Sergiu Gatlan)"
  source_url: https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/
  published_at: 2026-06-10T09:57:33+00:00
  retrieval_method: WebFetch + RSS
secondary_sources:
  - id: the-hacker-news
    name: "The Hacker News (Ravie Lakshmanan)"
    url: https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html
    published_at: 2026-06-10T09:38:13+00:00
    grade: B
  - id: krebs
    name: "Krebs on Security (Brian Krebs)"
    url: https://krebsonsecurity.com/2026/06/a-record-breaking-patch-tuesday-for-june-2026/
    published_at: 2026-06-09T22:07:28+00:00
    grade: B
  - id: rapid7
    name: "Rapid7 (Adam Barnett quoted via Krebs)"
    url: null
    grade: A_provisional
match_reason:
  watchlist: []  # No A&D-prime named victim
  actors: []  # Nightmare-Eclipse / Chaotic Eclipse is researcher pseudonym, NOT a tracked actor; no roster cross-walk per Hard Rule 2
  vulnerabilities:
    - CVE-2026-45585  # YellowKey BitLocker bypass
    - CVE-2026-45586  # GreenPlasma CTFMON LPE
    - CVE-2020-17103  # MiniPlasma Cloud Files Mini Filter Driver LPE
    - CVE-2026-50507  # BitLocker LPE (patch context per THN)
    - CVE-2026-49160  # HTTP.sys DoS (HTTP/2 Bomb)
    - CVE-2026-45657  # Windows Kernel UAF CVSS 9.8 RCE
    - CVE-2026-47291  # Windows HTTP.sys integer overflow CVSS 9.8
    - CVE-2026-44815  # Windows DHCP Client stack buffer overflow CVSS 9.8
  tracked_vuln_index_state_transitions:
    - ZD-001 (BlueHammer) — pending grader verification whether CVE-2026-45585 / 45586 / 50507 closes the BlueHammer family or is a sibling
    - ZD-002 (RedSun) — pending grader verification
    - ZD-003 (UnDefend) — pending grader verification
  keywords: [Microsoft Patch Tuesday, BitLocker, Nightmare Eclipse, Chaotic Eclipse, YellowKey, GreenPlasma, MiniPlasma, RoguePlanet, BlueHammer, RedSun, UnDefend, ZD-001, ZD-002, ZD-003, 206 flaws, record patch]
triage_tags:
  - vendor_patch_tuesday
  - zero_day_state_transition_patched
  - vuln_index_state_transition_required
  - microsoft_security_advisory_class
  - nightmare_eclipse_researcher_series_continuing_coverage
  - itw_exploitation_per_bleepingcomputer_greenplasma_miniplasma
  - bitskrieg_context_cve_2026_50507_per_thn
  - no_actor_attribution_per_hard_rule_2
iocs_extracted: true
iocs_count: 8  # CVE IDs only; no host/IP/domain/hash IOCs in published articles
text_word_count: 0  # grader to fill
promoted: true
promoted_to_finding: finding-2026-06-10-0001-bleepingcomputer-thn-krebs-june-2026-patch-tuesday-206-flaws-yellowkey-greenplasma-miniplasma-bitskrieg-http2-bomb-three-critical-rce
promoted_at: 2026-06-10T08:14:00-04:00
ttl_expires_at: 2026-09-08T07:35:00-04:00
---

# Microsoft June 2026 Patch Tuesday — 206 flaws fixed including three publicly-disclosed zero-days; GreenPlasma + MiniPlasma reported actively exploited

**Primary source:** BleepingComputer (Sergiu Gatlan) — "Microsoft patches YellowKey, GreenPlasma, MiniPlasma zero-days" — 2026-06-10T09:57:33 UTC
**Secondary:** The Hacker News (Ravie Lakshmanan) — "Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs" — 2026-06-10T09:38:13 UTC
**Secondary:** Krebs on Security (Brian Krebs) — "A Record-Breaking Patch Tuesday for June 2026" — 2026-06-09T22:07:28 UTC

## Key claims (primary + secondary aggregated)

### Patch volume
- **206 vulnerabilities patched** (THN; Krebs reports "nearly 200"). 39 rated Critical, 167 Important per THN. Including 63 EoP, 56 RCE, 30 info disclosure, 27 spoofing, 20 security feature bypass per THN.
- Krebs notes Rapid7's Adam Barnett observed an additional **360 browser vulnerabilities patched this month** (10x normal; Microsoft no longer enumerates Chromium CVEs in Security Update Guide).

### Three publicly-disclosed zero-days at Patch Tuesday

**1. YellowKey — CVE-2026-45585 — BitLocker bypass via Windows Recovery Environment (WinRE)**
- BleepingComputer: Attackers with physical access can circumvent BitLocker protection. Affects Windows 11, Windows Server 2022/2025.
- THN: CVSS 6.8. PoC released by Chaotic Eclipse (aka Nightmare Eclipse). Status per BC: "proof-of-concept publicly disclosed."
- Status per Krebs (alternate framing): Krebs places YellowKey as the earlier Nightmare-Eclipse release that surfaced the BitLocker physical-access issue (CVE-2026-50507 is described as "a patch for an elevation of privilege bug in BitLocker" — possibly a sibling or sub-component CVE).

**2. GreenPlasma — CVE-2026-45586 — Local privilege escalation in Collaborative Translation Framework (CTFMON)**
- BleepingComputer: SYSTEM-shell on fully patched Windows systems. **"PoC released; actively exploited in attacks."**
- THN: CVSS 7.8. Suspected to be the fix for "GreenPlasma." Attribution: Chaotic Eclipse / Nightmare Eclipse.

**3. MiniPlasma — CVE-2020-17103 — Local privilege escalation in Cloud Files Mini Filter Driver**
- BleepingComputer: SYSTEM-level access on fully patched systems. **"PoC public; actively exploited."**
- THN: Incomplete prior fix recently publicly disclosed by Chaotic Eclipse. (CVE-ID predates 2020 cycle — re-patched June 2026 Patch Tuesday for incomplete prior fix.)
- Attribution: Nightmare Eclipse.

### Additional zero-day patched on physical access / BitLocker family

**CVE-2026-50507 — BitLocker EoP (Krebs framing) / BitLocker bypass with "bitskrieg" exploit (THN framing)**
- Krebs: "elevation of privilege bug in BitLocker." Advisory does NOT credit a specific researcher.
- THN: CVSS 6.8. "Linked to the 'bitskrieg' exploit enabling full access to encrypted data." (Bitskrieg lineage carry-context from prior corpus surfaces — see finding-2026-06-02 PM-006 and finding-2026-06-03 PM-005.)
- Microsoft per Krebs: advisory "does not credit any researchers in the acknowledgement section" — only generic "coordinated vulnerability disclosure" language.

### Additional disclosed zero-day not in YellowKey / GreenPlasma / MiniPlasma trio

**CVE-2026-49160 — HTTP/2 Bomb DoS in HTTP.sys (IIS family)**
- Krebs: "denial of service vulnerability affecting a range of web servers, including Microsoft Internet Information Services (IIS)." **"Reported by OpenAI's Codex."**
- THN: CVSS 7.5. "HTTP/2 Bomb attack technique publicly available on GitHub."
- Carry-context: aligns with prior corpus surfaces `finding-2026-06-03-am-003` (NGINX + Apache + IIS + Envoy + Cloudflare Pingora HTTP/2 Bomb CVE-2026-49975 multi-server class). CVE-2026-49160 is the Microsoft-specific IIS fix in the HTTP/2 Bomb cluster.

### Critical non-zero-day RCE chain per THN

- **CVE-2026-45657** — Windows Kernel use-after-free RCE — CVSS 9.8
- **CVE-2026-47291** — Windows HTTP.sys integer overflow — CVSS 9.8
- **CVE-2026-44815** — Windows DHCP Client stack buffer overflow — CVSS 9.8

No ITW exploitation reported for these three at disclosure; patched at release.

## Nightmare-Eclipse / Chaotic Eclipse researcher cluster — extended carry-context

Per Krebs:
- Researcher claims to be **former Microsoft employee** (Microsoft has not responded to questions about this claim per Krebs).
- Last month's Krebs roundup referenced Microsoft initially threatening legal action against the researcher; Microsoft later clarified it would only report to authorities if researchers "break the law."
- Recent blog post by Nightmare Eclipse included an image of Albert Wesker (Resident Evil character — researcher who worked for a tech company then went rogue) — researcher-signaled persona framing.
- **Researcher pledges more zero-days on July 14, 2026** (next Patch Tuesday) — "bone shattering" drop planned.
- **Immediately after this Patch Tuesday: Nightmare Eclipse published a fresh Defender zero-day (RoguePlanet)** — already in 06:00 sweep summary (`raw-2026-06-10-flash-0600-000`). PoC-only, no ITW confirmed per BleepingComputer / THN.

**Cross-corpus continuing-coverage:** Bitskrieg / BlueHammer / RedSun / UnDefend / RoguePlanet / YellowKey / GreenPlasma / MiniPlasma is now an 8-disclosure-deep researcher series spanning multiple Microsoft product families. Hard Rule 2 applies — Chaotic Eclipse / Nightmare Eclipse is a researcher pseudonym, NOT a tracked threat actor. Archimedes does NOT roster-tier this researcher; coverage is vuln-tracker / researcher-series tracking.

## Cross-corpus tracked vulnerability state transitions

The June Patch Tuesday materially alters vuln-index `_index.yaml` state for several entries. Grader / vuln-tracker handoff required:

- **ZD-001 BlueHammer** (LPE Windows 10/11/Server) — currently `patch_status: patched` per existing index; tracked_since 2026-03. **No direct CVE collision identified in this Patch Tuesday's June advisories** — grader to verify whether BlueHammer family is fully closed or has remaining unpatched siblings.
- **ZD-002 RedSun** (LPE Windows 10/11/Server 2019+) — currently `patch_status: unpatched` per existing index; tracked_since 2026-03. **Grader to verify whether June Patch Tuesday's EoP cluster (63 EoP fixes) includes the RedSun family.** No explicit CVE mapping in primary sources retrieved this sweep — defer to grader for vuln-tracker direct retrieval of MSRC advisories CVE-2026-45586 (GreenPlasma) and adjacent EoP CVEs to determine RedSun resolution status.
- **ZD-003 UnDefend** (DoS / Defender update block) — currently `patch_status: unpatched`. **Grader to verify against June Defender advisories.** The RoguePlanet zero-day disclosed today by Nightmare-Eclipse is a SEPARATE Defender issue and does NOT close UnDefend.

**Vuln-tracker handoff queue items from this raw-signal:**

1. Scaffold new vuln-dossiers (or extend existing) for: CVE-2026-45585 YellowKey, CVE-2026-45586 GreenPlasma, CVE-2020-17103 MiniPlasma, CVE-2026-50507 BitLocker EoP, CVE-2026-49160 HTTP/2 Bomb IIS.
2. State-transition review for ZD-001 / ZD-002 / ZD-003 against June Patch Tuesday advisories.
3. Consider scaffolding ZD-005 series for the Nightmare-Eclipse researcher cluster (RoguePlanet + earlier).

## FLASH-trigger evaluation (advisory; quiet hours; for grader awareness)

### Trigger 1 — Critical CVE + active exploitation + A-grade source

- **YellowKey CVE-2026-45585:** CVSS 6.8. Strict hard-threshold FAIL (< 9.0). PoC-only per BC; no ITW exploitation framing per primary sources. **Trigger 1 FAILS.**
- **GreenPlasma CVE-2026-45586:** CVSS 7.8. Strict hard-threshold FAIL (< 9.0). BleepingComputer: "actively exploited in attacks." **Source-class:** BC is B-grade; THN is B-grade; Krebs is B-grade. **No A-grade source independently confirms ITW exploitation in this window** (no MSRC blog post, no Mandiant / Volexity / Unit 42 telemetry). Strict trigger-1 also requires A-grade source backing exploitation claim — current sourcing is BC reformulation; THN frames as "publicly disclosed" not "actively exploited." Single-source veto applies on active-exploitation prong. **Trigger 1 FAILS strict.**
- **MiniPlasma CVE-2020-17103:** Same disposition as GreenPlasma — BC frames as "actively exploited," THN frames as PoC public + incomplete prior fix. Same single-source-on-ITW posture. **Trigger 1 FAILS strict.**
- **CVE-2026-50507 BitLocker EoP / bitskrieg:** CVSS 6.8 strict fail. PoC-public; no explicit ITW framing in retrieved primaries. **Trigger 1 FAILS.**
- **CVE-2026-49160 HTTP/2 Bomb IIS:** CVSS 7.5 strict fail. PoC public on GitHub per THN. No ITW. **Trigger 1 FAILS.**
- **CVE-2026-45657 / 47291 / 44815 critical RCE chain:** CVSS 9.8 each PASS hard threshold. Patched at disclosure; **no ITW exploitation reported by Microsoft or any primary.** Strict trigger-1 fails on exploitation prong. **Trigger 1 FAILS.**

**Net: 0 Trigger-1 fires.** Multiple morning-brief priority items but no FLASH escalation.

### Trigger 2 — New attribution for tracked actor — FAILS
Nightmare-Eclipse / Chaotic Eclipse is researcher pseudonym not in `_roster.yaml`; no roster cross-walk per Hard Rule 2.

### Trigger 3 — First-party Splunk IOC hit — FAILS
Splunk 30d query against CVE IDs + Nightmare-Eclipse keyword returned zero substantive hits (61 events all sourcetype `archimedes:operation` self-instrumentation per Hard Rule 8).

### Trigger 4 — Tracked-actor TTP change — FAILS
No tracked-actor attribution to anchor on.

### Trigger 5 — Active A&D-sector campaign — FAILS
No A&D-prime named victim. Microsoft Windows is universally deployed including across A&D primes — structural exposure framing only.

### Trigger 6 — Zero-day without patch + exploitation — STATE TRANSITION OPPOSITE DIRECTION
The three Nightmare-Eclipse zero-days are TRANSITIONING TO PATCHED. Trigger 6 evaluates "no patch + exploitation"; this is "now patched." **Trigger 6 FAILS** — the inverse condition applies (state transition out of zero-day-no-patch class).

### Critical override evaluation
0 of 4 conditions met (no CVSS 10.0; tracked-actor false; A&D-watchlist false; ITW true but on sub-threshold CVSS only). Override does NOT apply.

## Extraction notes

- Language: en
- Article type: vendor Patch-Tuesday roundup (BC + THN); security-blog-roundup (Krebs)
- Raw IOC extraction invoked: yes — CVE IDs only; no host/IP/domain/hash IOCs in any retrieved primary
- Cross-corpus prior surfaces:
  - finding-2026-06-02-PM-006 — Bitskrieg / Nightmare-Eclipse / Secure Boot / BitLocker first surface
  - finding-2026-06-03-PM-005 — TheRegister Microsoft disclosure-policy clarification on Askar VS Code + Nightmare-Eclipse Bitskrieg explicit linkage
  - finding-2026-06-02-AM-001 — Google Android CVE-2025-48595 zero-day actively exploited (separate vendor, separate state transition)
  - finding-2026-06-02-PM-003 — Microsoft Android M365 app token bypass CVE-2026-41100/41101/41102 debug-flag (separate platform)
  - finding-2026-06-01-flash-1200-001 — Windows Netlogon CVE-2026-41089 ITW state transition (separate Windows component, separate Patch Tuesday cycle)

## IOCs (from ioc-extraction skill)

```yaml
iocs:
  cves:
    - id: CVE-2026-45585
      name: YellowKey
      class: BitLocker bypass via WinRE
      cvss: 6.8
      severity: Important
      exploitation_status: poc_publicly_disclosed
      itw_status_per_source:
        bleepingcomputer: "proof-of-concept publicly disclosed"
        thn: "publicly disclosed"
        krebs: "exploit released" (sub-component framing)
      patch_status: patched_2026_06_10_patch_tuesday
      cwe: pending
      attribution: Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym (NOT tracked actor)
      platform: Windows 11, Windows Server 2022, Windows Server 2025
    - id: CVE-2026-45586
      name: GreenPlasma
      class: Local privilege escalation in Collaborative Translation Framework (CTFMON)
      cvss: 7.8
      severity: Important
      exploitation_status: poc_public_actively_exploited_per_bleepingcomputer_single_source
      itw_status_per_source:
        bleepingcomputer: "actively exploited in attacks"
        thn: "publicly disclosed" (no ITW framing)
        krebs: not explicit
      patch_status: patched_2026_06_10_patch_tuesday
      attribution: Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym
      platform: Windows (full patched systems per BC)
    - id: CVE-2020-17103
      name: MiniPlasma
      class: Local privilege escalation in Cloud Files Mini Filter Driver
      cvss: null  # CVE ID from 2020 cohort; recent re-patch
      severity: pending
      exploitation_status: poc_public_actively_exploited_per_bleepingcomputer_single_source
      itw_status_per_source:
        bleepingcomputer: "actively exploited"
        thn: "incomplete prior fix recently publicly disclosed"
        krebs: not explicit
      patch_status: patched_2026_06_10_patch_tuesday (incomplete prior fix re-patched)
      attribution: Nightmare-Eclipse / Chaotic Eclipse researcher pseudonym
      platform: Windows
    - id: CVE-2026-50507
      name: bitskrieg-family BitLocker EoP
      class: BitLocker elevation of privilege
      cvss: 6.8
      severity: Important
      exploitation_status: poc_public
      attribution: per_thn "linked to the 'bitskrieg' exploit"; per_krebs no researcher credit in advisory
      patch_status: patched_2026_06_10_patch_tuesday
    - id: CVE-2026-49160
      name: HTTP/2 Bomb (Microsoft IIS variant)
      class: HTTP.sys denial of service
      cvss: 7.5
      severity: Important
      exploitation_status: poc_public_github
      attribution: OpenAI Codex reported per krebs (not actor attribution; automated discovery)
      patch_status: patched_2026_06_10_patch_tuesday
      cross_corpus_lineage: HTTP/2 Bomb cluster (CVE-2026-49975 NGINX/Apache/Envoy/Cloudflare Pingora per finding-2026-06-03-am-003)
    - id: CVE-2026-45657
      class: Windows Kernel use-after-free RCE
      cvss: 9.8
      severity: Critical
      exploitation_status: no_itw_at_disclosure
      patch_status: patched_2026_06_10_patch_tuesday
    - id: CVE-2026-47291
      class: Windows HTTP.sys integer overflow
      cvss: 9.8
      severity: Critical
      exploitation_status: no_itw_at_disclosure
      patch_status: patched_2026_06_10_patch_tuesday
    - id: CVE-2026-44815
      class: Windows DHCP Client stack buffer overflow
      cvss: 9.8
      severity: Critical
      exploitation_status: no_itw_at_disclosure
      patch_status: patched_2026_06_10_patch_tuesday
  attribution_claims:
    - claim_text: "Nightmare-Eclipse / Chaotic Eclipse — security researcher (pseudonym; claims former Microsoft employee per Krebs; Microsoft has not confirmed)"
      target: CVE-2026-45585, CVE-2026-45586, CVE-2020-17103
      source: krebs, bleepingcomputer, thehackernews
      attribution_type: researcher_pseudonym_NOT_tracked_actor
      hard_rule_2_compliant: true
  hashes: []
  domains: []
  ipv4: []
  urls: []
```
