---
raw_id: raw-2026-05-14-flash-2200-001-teampcp-mistral-ai-450-repos-sale
collected_at: 2026-05-15T00:05:00-04:00
run_id: flash-sweep-20260515-000000
collection_mode: flash_sweep
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer (Ionut Ilascu byline) — relay of TeamPCP forum post + Mistral statement"
  source_url: https://www.bleepingcomputer.com/news/security/teampcp-hackers-advertise-mistral-ai-code-repos-for-sale/
  published_at: 2026-05-14T18:50:36-04:00
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: []
  keywords: ["Mini Shai-Hulud", "TanStack", "CI/CD credential theft", "codebase management system compromise", "supply-chain monetization"]
triage_tags: [non_flash, brief_update_candidate_morning_2026_05_15, teampcp_continuation, mini_shai_hulud_monetization_stage, named_enterprise_victim_2_mistral, anti_noise_24h_lockout_to_2026_05_15_1600]
iocs_extracted: true
iocs_count: 0
text_word_count: 1180
promoted: true
promoted_to_finding: finding-2026-05-15-0001
promoted_at: 2026-05-15T07:55:00-04:00
promoted_grading_run_id: morning-20260515-080000
ttl_expires_at: 2026-08-13T00:05:00-04:00
test: false
---

# TeamPCP advertises ~5GB / ~450 Mistral AI internal repositories for sale ($25K BIN) — continuation of Mini Shai-Hulud / TanStack supply-chain campaign

**Net-new fact for the corpus:** Mistral AI is the SECOND named-enterprise victim (after OpenAI) publicly confirmed as impacted by the Mini Shai-Hulud / TanStack supply-chain campaign that Wiz / Snyk / StepSecurity attributed to TeamPCP "with high confidence" in finding-2026-05-12-FLASH-0001. TeamPCP has now moved to the MONETIZATION stage — advertising ~5GB / ~450 internal repositories for sale at $25,000 BIN with a one-week leak deadline.

**FLASH disposition:** NON-FLASH. Trigger 2 (new attribution to tracked actor) FAILS — attribution is to TeamPCP's own forum-post claim plus continuation of an already-FLASHed campaign, not new vendor attribution. Trigger 4 (TTP change) FAILS — the data-sale stage is monetization downstream of an already-FLASHed mechanism, not a new tooling/infrastructure class. Trigger 5 (A&D-sector campaign) FAILS — no A&D-watchlist company named (Mistral is AI/research, pfizer-rfp filename suggests pharma-RFP enterprise context, no defense primes). 24h anti-noise lockout to ~2026-05-15 16:00 EDT in effect (TanStack / TeamPCP / OpenAI absorbed in 2026-05-14 16:00 afternoon brief via finding-2026-05-14-0008).

**Brief-update disposition:** STRONG candidate for 2026-05-15 morning brief. The Mistral named-victim element + the $25K monetization stage + the "pfizer-rfp-2025.tar.gz" repository name (suggesting Mistral had pharma-enterprise RFP material in scope) materially extend the campaign picture documented in findings 0001 (Mini Shai-Hulud) and 0008 (OpenAI TanStack confirmation).

---

## Source content (BleepingComputer, Ionut Ilascu)

### Headline + lede

"TeamPCP hackers advertise Mistral AI code repos for sale" — published 2026-05-14T22:50:36 UTC (18:50 EDT).

The TeamPCP hacker group is threatening to leak source code from the Mistral AI project unless a buyer is found for the data.

### TeamPCP claim

TeamPCP's forum post claims approximately 450 repositories totaling "nearly 5 gigabytes of internal repositories and source code" used for "training, fine-tuning, benchmarking, model delivery, and inference." The repositories are described as SDK and development materials, NOT customer data or communications.

Asking price: **$25,000 BIN (Buy It Now)**. TeamPCP language: "We are looking for $25k BIN or they can pay this and we will shred these permanently." Negotiable per the post. If no buyer materializes within one week, TeamPCP says the data will be leaked publicly.

### Acquisition mechanism (per BleepingComputer summary)

The breach stemmed from the Mini Shai-Hulud supply-chain attack. Specifically: "hackers compromised a codebase management system" after the "compromise of official packages from TanStack and Mistral AI through stolen CI/CD credentials and legitimate workflows."

This is the same mechanism Wiz / Snyk / StepSecurity documented in finding-2026-05-12-FLASH-0001 (Mini Shai-Hulud / CVE-2026-45321 / GHSA-g7cv-rxg3-hmpx). TanStack pivot → stolen CI/CD credentials → codebase management system access → exfiltration of internal repositories. No new infrastructure class disclosed.

### Mistral AI confirmation (statement to BleepingComputer + carried in HackRead update)

Mistral AI confirmed the incident but minimized scope:

- "They contaminated some of our SDK packages for a brief period." (Note: this is TeamPCP, the attacker — Mistral's wording "they contaminated our SDK packages" is referring to the supply-chain malware leg of the campaign.)
- "The impacted data was not part of the core code repositories."
- "Neither our hosted services, managed user data, nor any of our research and testing environments were compromised."

Mistral also confirmed in a separate statement (per Cybernews / TechNadu relays) that "attackers temporarily compromised one of the company's codebase management systems on May 12, 2026, through a third-party software supply chain attack."

### Repository names disclosed in forum post (per HackRead sample listing, 24 of ~450)

HackRead published a sample listing of 24 of the ~450 claimed repository names, including:
- mistral-inference-internal
- chatbot-security-evaluation
- **pfizer-rfp-2025.tar.gz** ← enterprise customer artifact in scope; pharma-RFP context
- (Plus other internal-tooling names per the article — training systems, fine-tuning projects, benchmarking tools, dashboards, inference infrastructure, experiments, "future AI projects.")

The pfizer-rfp-2025 filename is the only named-enterprise-customer artifact in the disclosed sample. NO A&D-watchlist company appears in the disclosed names.

### Verification status

- BleepingComputer: "The claims have not been independently verified."
- HackRead: "No public evidence confirming that the files, if authentic, originated from the company's internal systems."
- No security vendor (Wiz, Snyk, StepSecurity, Socket, SafeDep, Aikido, Semgrep, Onapsis) has issued a primary research statement on the sale claim within the FLASH window.

### Independent corroborations

Multiple media outlets surface this story within the 16:00–22:00 EDT 2026-05-14 window:

1. **BleepingComputer** (Ionut Ilascu, 18:50 EDT) — primary relay (sourced from TeamPCP forum + Mistral statement)
2. **Cybernews** ("Mistral AI allegedly breached by Dune-loving criminals following TanStack supply chain hit, 450 repositories exposed") — same content, "Dune-loving" framing references TeamPCP's affinity for Dune-referenced strings in their tradecraft (Mini Shai-Hulud naming convention; Spice Harvester / Sandworm-symbolism in package payload comments per finding-2026-05-12-FLASH-0001)
3. **TechNadu** ("TeamPCP Claims Theft of Mistral AI Source Code")
4. **HackRead** ("TeamPCP Claims Sale of Mistral AI Repositories Amid Mini Shai-Hulud Attack (Updated)")
5. **Dark Web Informer** (X post, social C-grade, F-grade for attribution per source-grades.yaml)
6. **KSEC Community Forum** (relay of BleepingComputer; community-source, not primary)

**All 6 corroborations are B-or-lower grade media / social. No A-grade vendor primary research (Wiz / Snyk / StepSecurity / Socket / Mandiant / CrowdStrike / Unit 42 / MSTIC) has yet covered the sale claim in the FLASH window.** This is consistent with vendor cadence — Wiz's 2026-05-12 primary research was the campaign-attribution layer; sale-stage events typically don't trigger fresh vendor research within hours.

---

## Linkage to existing corpus

### Linkage to finding-2026-05-12-FLASH-0001 (Mini Shai-Hulud, original TeamPCP attribution)

- Attribution lineage: TeamPCP per Wiz "high confidence" + Snyk co-primary (CVE-2026-45321 / GHSA-g7cv-rxg3-hmpx) + StepSecurity originating-attribution per Wiz citation.
- Mechanism: TanStack pivot → stolen CI/CD credentials → npm / PyPI package poisoning → downstream consumer compromise → propagation to internal codebase management systems of upstream maintainers.
- Mistral was already publicly known via the Mini Shai-Hulud campaign as a victim of package contamination ("They contaminated some of our SDK packages for a brief period" — Mistral confirms this in the current statement). The NEW fact here is the SCOPE: ~450 internal repos / ~5GB exfiltrated, claimed as for-sale at $25K BIN.

### Linkage to finding-2026-05-14-0008 (OpenAI TanStack breach self-disclosure)

- finding-0008 established OpenAI as the first named-enterprise victim publicly confirmed (2 employee devices compromised; multi-platform code-signing cert rotation; bounded scope: no customer / production / IP / deployed-software impact; macOS app deadline 2026-06-12).
- Mistral is now the second named-enterprise victim with public confirmation of the same underlying mechanism (codebase management system compromise via stolen CI/CD credentials). Mistral's scope statement parallels OpenAI's ("not core code repositories; no hosted services / managed user data / research and testing environments compromised") — both victim-side scope claims are minimization-shaped, both restrict to non-core code.
- The two named-victim disclosures together establish a pattern (TeamPCP via Mini Shai-Hulud / TanStack pivot can reach codebase management systems of upstream maintainers / customers; vendors with mature CI/CD hygiene contain blast radius to non-core repos and non-production-key contexts).

### Linkage to operational template per analyst SAT-ACH on finding-2026-05-14-0008

Finding-0008's analyst SAT-ACH framed the OpenAI 2-devices → cert-key-exfil → multi-platform-rotation pattern as the operational template an A&D-prime victim disclosure would follow if @squawk aviation-namespace dependencies reach Tier-1 SDLCs. The Mistral disclosure CONFIRMS the template at the second-named-enterprise-victim layer (~450 internal repos exfil; codebase management system compromise; minimization-shaped scope statement; data-monetization downstream stage). A&D-prime extrapolation remains GUARDED per Hard Rule 2 — no A&D-prime is publicly named as impacted in either OpenAI or Mistral disclosure to date.

### Linkage to roster actor #001 TeamPCP (HIGH threat level, tracked since 2026-03-18)

- This is the third in-window surface of TeamPCP attribution per the 2026-05-12 / 2026-05-14 / 2026-05-15 cycle.
- The monetization stage (selling exfiltrated data) is consistent with TeamPCP's cybercriminal classification in the roster (type: "Cybercriminal", attribution: nation unknown).
- No new TTP — the data-sale monetization stage is a downstream cybercriminal pattern, not a TTP change.

---

## Hard Rule 2 — Attribution discipline

- TeamPCP attribution itself is NOT first-time-origination here. Wiz / Snyk / StepSecurity established TeamPCP attribution for the Mini Shai-Hulud / TanStack campaign on 2026-05-12. BleepingComputer / HackRead / Cybernews / TechNadu cite TeamPCP's own forum post for the SALE claim; the broader campaign attribution is the established Wiz / Snyk / StepSecurity chain.
- The Mistral sale-claim itself is TeamPCP's own self-attribution to TeamPCP, which is a tautology — preserved verbatim in the corpus as "per TeamPCP forum post" and "Mistral AI confirms compromise of codebase management system but did NOT confirm scope of TeamPCP's specific claim of ~450 repos / ~5GB."
- Archimedes does NOT extrapolate or upgrade the Mistral-confirmation language ("They contaminated some of our SDK packages for a brief period" + "not core code repositories" + "no hosted services / managed user data / research and testing environments compromised") to imply that the ~450 repo claim is independently verified.

---

## Hard Rule 8 — First-party Splunk

Last-24h sweep (2026-05-14 04:00 UTC → 2026-05-15 04:00 UTC) returned 36 events:
- `index=archimedes sourcetype=archimedes:operation` × 22
- `index=archimedes sourcetype=archimedes:scheduler` × 14
- `index=defenseclaw_local` × 0

Zero tracked-IOC matches against any TeamPCP / Mini Shai-Hulud IOC set. 25th consecutive dormant sweep with the non-archimedes-internal stream. Per Hard Rule 8: silence is absence of evidence, not evidence of absence.

---

## Extraction notes

- Language: en
- Publisher byline: Ionut Ilascu (BleepingComputer, primary relay)
- Article type: news (media B-grade per source-grades.yaml)
- Primary research source NOT yet surfaced in window — Wiz / Snyk / StepSecurity have not published on the sale claim within the FLASH window
- Raw IOC extraction: zero IOCs (no domains, no IPs, no hashes, no package names beyond Mistral + TanStack already corpus-known)

## IOCs (no new IOCs extracted)

```yaml
iocs: []
attribution_claims:
  - actor: "TeamPCP"
    actor_roster_id: "001"
    source: "TeamPCP forum post (self-claim) + BleepingComputer + HackRead + Cybernews + TechNadu relays"
    source_grade: B (BleepingComputer / HackRead / Cybernews / TechNadu media tier)
    confidence_language: "[TeamPCP self-claim, no vendor-confirmed independent verification in window]"
    note: "Continuation of Mini Shai-Hulud / TanStack campaign already attributed to TeamPCP per finding-2026-05-12-FLASH-0001 (Wiz high confidence + Snyk co-primary + StepSecurity originating). Mistral AI confirms codebase-management-system compromise via third-party software supply chain attack on 2026-05-12, but DOES NOT confirm the ~450 repos / ~5GB scope claimed by TeamPCP."
  - victim_named: "Mistral AI"
    victim_class: AI/research enterprise (NOT A&D watchlist)
    victim_self_disclosure: yes (Mistral statement to BleepingComputer + Cybernews + TechNadu)
    scope_per_victim: "non-core code repositories; no hosted services / managed user data / research and testing environments compromised"
    scope_per_attacker_claim: "~450 internal repositories / ~5GB / SDK + training / fine-tuning / benchmarking / inference / dashboards / experiments / future AI projects"
    enterprise_artifact_named: "pfizer-rfp-2025.tar.gz (pharma-RFP context; NOT A&D)"
  - linkage: "Same mechanism as finding-2026-05-12-FLASH-0001 (Mini Shai-Hulud / CVE-2026-45321 / GHSA-g7cv-rxg3-hmpx) — TanStack pivot → stolen CI/CD credentials → codebase management system compromise. Second named-enterprise victim (after OpenAI per finding-2026-05-14-0008)."
```
