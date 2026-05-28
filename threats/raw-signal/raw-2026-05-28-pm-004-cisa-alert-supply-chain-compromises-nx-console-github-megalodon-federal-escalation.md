---
raw_id: raw-2026-05-28-pm-004
collected_at: 2026-05-28T15:58:00-04:00
run_id: pre-brief-20260528-pm
collection_mode: pre_brief_collection
source:
  source_yaml_id: cisa-advisories
  source_name: CISA — Cybersecurity and Infrastructure Security Agency
  source_url: https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories
  source_grade: A
  authored_by: CISA
  published_at: 2026-05-28T12:00:00Z   # 08:00 EDT per CISA all.xml feed
match_reason:
  watchlist:
    - aerospace-defense (DIB SDLC adjacency — CI/CD pipelines and code-extensions in widespread enterprise use including DIB primes)
  actors:
    - "001"   # TeamPCP (corpus-anchored on Mini Shai-Hulud / npm supply-chain compromise lineage; Nx + Megalodon adjacency via SDLC threat surface)
  vulnerabilities:
    - CVE-2026-48027   # Nx Console malicious extension (KEV-listed 2026-05-27)
    - CVE-2026-45321   # TanStack Mini Shai-Hulud (KEV-listed 2026-05-27)
    - VT-006           # Mini Shai-Hulud (corpus tracked-vuln entry)
  keywords:
    - CISA alert
    - Supply Chain Compromises
    - Nx Console
    - VS Code marketplace extension
    - GitHub breach
    - Megalodon
    - CI/CD pipelines
    - federal escalation
    - DevOps ecosystem targeting
    - automatic update mechanism abuse
triage_tags:
  - non_flash
  - government_source_escalation
  - sdlc_supply_chain_surface
  - corpus_anchored_threat_surface
  - federal_kev_due_2026-06-10
  - dib_sdlc_relevance
iocs_extracted: true
iocs_count: 0
text_word_count: 750
promoted: true
promoted_to_finding: finding-2026-05-28-0007-cisa-alert-supply-chain-compromises-nx-console-github-megalodon-federal-escalation
promoted_at: 2026-05-28T16:13:00-04:00
promoted_run_id: afternoon-20260528-160000
ttl_expires_at: 2026-08-26T15:58:00-04:00
collector_provenance:
  retrieval_path: |
    Primary CISA alert URL returned 403 on Claude Code WebFetch
    (cisa.gov/news-events/alerts/... endpoint has WAF pattern
    consistent with the long-standing observation in source-health
    cisa-advisories notes — /cybersecurity-advisories/all.xml RSS
    path remains the productive endpoint while direct alert-page
    fetches frequently return 403). Article metadata + lede captured
    via all.xml RSS summary which provides the alert title, date,
    full lede paragraph naming Nx Console + GitHub + Megalodon, and
    procedural framing about CISA prioritizing response to multiple
    emerging software supply chain intrusion campaigns. Operator may
    wish to retrieve the full alert body via browser if PM-28 brief
    requires CISA-verbatim mitigation guidance.
---

# CISA Alert — Supply Chain Compromises Impact Nx Console and GitHub Repositories — 2026-05-28

## Alert metadata (per CISA all.xml feed)

**Title:** "Supply Chain Compromises Impact Nx Console and GitHub Repositories"

**Source:** CISA

**Published:** 2026-05-28T12:00:00Z (08:00 EDT)

**URL:** https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories

**Direct retrieval:** Body content NOT directly retrieved (HTTP 403 from Claude Code WebFetch — standard cisa.gov/news-events WAF pattern). Alert metadata + lede captured via /cybersecurity-advisories/all.xml RSS feed which is the productive endpoint.

---

## CISA alert lede (verbatim from all.xml RSS summary)

> CISA is prioritizing the response to multiple emerging software supply chain intrusion campaigns targeting developer ecosystems Continuous Integration/Continuous Development (CI/CD) pipelines. These recent incidents, including the GitHub compromise via a malicious Nx Console Visual Studio Code (VS Code) extension and the "Megalodon" supply chain intrusion campaign, demonstrate how cyber threat actors are abusing tools and processes that support enterprise, cloud, and DevOps environments — specifically CI/CD pipelines, code extensions and workflows.

## CISA mechanism description (verbatim from all.xml RSS summary, continued)

> Threat actors leveraged a prior compromise of Nx developer systems to compromise a GitHub employee's device through a poisoned third-party VS Code extension, resulting in unauthorized access and exfiltration of internal GitHub repositories. The malicious extension version (18.95.0) was distributed through VS Code's automatic update mechanism, meaning systems with Nx Console previously installed may have received the malicious build...

(RSS summary truncates here; full body not retrievable this sweep.)

---

## Cross-references to existing Archimedes corpus

This alert is the CISA government-source escalation linking two threat surfaces already deeply corpus-tracked:

1. **Nx Console VS Code extension compromise → GitHub repository exfil**
   - Corpus anchor: finding-2026-05-20-FLASH-0001 (GitHub breach ~3,800 internal repos via VS Code extension; TeamPCP self-claim, GitHub procedural confirmation)
   - Corpus anchor: finding-2026-05-27-0007 (CISA KEV three-add 2026-05-27 — CVE-2026-48027 Nx Console + CVE-2026-45321 TanStack)
   - Corpus anchor: TeamPCP roster #001 (HIGH threat-level, supply-chain lineage)
   - VT entry: VT-009 (Nx Console malicious extension scaffold per 2026-05-27 PM brief)
   - **Federal KEV deadline:** 2026-06-10 (Nx Console CVE-2026-48027)

2. **Megalodon supply chain intrusion campaign**
   - Corpus anchor: finding-2026-05-25-0001 (Megalodon GitHub workflow_dispatch mass-backdoor, 5,561 repos in six hours via Tiledesk org-token theft)
   - Corpus anchor: finding-2026-05-27-0001 (CrowdStrike GlassWorm takedown, related supply-chain ecosystem) — partial adjacency
   - Corpus anchor: raw-2026-05-25-am-001 (SecurityWeek Megalodon coverage)

**CISA alert's value-add over corpus:** the **government-source escalation signal**. CISA is now formally treating these as a coordinated supply-chain-attack class warranting federal-agency prioritization. The corpus has been tracking the underlying intrusions for ~8 days; this is the official escalation to federal-prioritized response posture.

---

## IOCs

```yaml
iocs:
  ip_addresses: []
  domains: []
  hashes: []
  cves:
    - CVE-2026-48027   # Nx Console (KEV-listed 2026-05-27, dueDate 2026-06-10)
    - CVE-2026-45321   # TanStack Mini Shai-Hulud (KEV-listed 2026-05-27, dueDate 2026-06-10)
  vs_code_extension_versions:
    - "Nx Console version 18.95.0 — malicious build"
  affected_software_distribution_mechanisms:
    - VS Code automatic update mechanism (per CISA: "systems with Nx Console previously installed may have received the malicious build")
attribution_claims:
  - claim: "Threat actors leveraged a prior compromise of Nx developer systems to compromise a GitHub employee's device through a poisoned third-party VS Code extension"
    claimed_by: CISA
    confidence_language: procedural government incident reporting (no actor named)
    actor_named: none in CISA alert (consistent with CISA's standard practice of avoiding actor-attribution in alert text; TeamPCP self-claim and corpus attribution are separately corpus-anchored, not CISA-attributed)
  - claim: Megalodon and Nx Console are part of "multiple emerging software supply chain intrusion campaigns targeting developer ecosystems"
    claimed_by: CISA
    confidence_language: pattern-of-activity framing; no single-actor attribution
named_entities:
  campaigns:
    - Megalodon supply chain intrusion campaign
    - Nx Console / GitHub repository compromise
  affected_organizations:
    - GitHub (named victim — employee device compromise + ~3,800 repo exfil per finding-2026-05-20-FLASH-0001)
    - Nx (named victim — developer systems compromise as precursor)
  affected_software:
    - Nx Console VS Code extension
    - VS Code (automatic update mechanism abused)
collection_notes: |
  CISA alert body not directly retrieved due to cisa.gov/news-events
  WebFetch 403 pattern. Operator may wish to retrieve full body via
  browser for verbatim mitigation guidance. RSS summary captures
  the alert's framing, the Nx Console + Megalodon scope, and the
  VS Code extension version 18.95.0 malicious-build identifier.
  CISA does NOT attribute these campaigns to a named actor; the
  TeamPCP corpus-anchored attribution (per finding-2026-05-20-
  FLASH-0001) is separately corpus-attributed, not CISA-attributed
  — Hard Rule 2 preserved.
```

---

## Extraction notes

- Language: en
- Article type: official US government cybersecurity alert (CISA — Cybersecurity and Infrastructure Security Agency)
- Body retrieval: 403 on direct URL (standard WAF pattern); metadata + lede via all.xml RSS feed
- Source grade: A (per source-grades.yaml — CISA government-source, official, technically vetted)
- Single-source veto consideration: CISA government-source escalation is corpus-corroborating layer on underlying threat surfaces already independently attributed via Wiz / Snyk / StepSecurity / Socket / Ox Security / Upwind / Sysdig / SafeDep / Semgrep / Aikido / Onapsis (for Mini Shai-Hulud) and SecurityWeek / Dark Reading / SafeDep / Ox Security (for Megalodon). Independent corroboration condition fully satisfied via existing corpus depth.
- No new IOCs beyond corpus-tracked CVE-2026-48027 + CVE-2026-45321 + the VS Code extension version 18.95.0 identifier already corpus-noted

## A&D / DIB relevance — collector framing for grader

- **DIB SDLC threat surface escalation** — CI/CD pipelines, VS Code extensions, and GitHub repos are deeply embedded in A&D-prime SDLCs (Boeing, Lockheed, Raytheon, Northrop, GD, BAE, L3Harris, Leidos all run extensive enterprise GitHub estates and use VS Code with extension ecosystems). The CISA alert raises the federal-prioritization profile for these surfaces, which means DCSA / DFARS 252.204-7012 / CMMC implementation guidance is now likely to incorporate the Nx Console / Megalodon vector class.
- **Federal compliance trajectory** — federal-agency mandate timing: CVE-2026-48027 (Nx Console) + CVE-2026-45321 (TanStack) KEV dueDate 2026-06-10 = 13 days from sweep. DIB primes operating to BOD-22-01-equivalent contractual obligations under DFARS 252.204-7012 are accelerating remediation cadence.
- **Standing carry-forward** — pairs with the standing LiteSpeed CVE-2026-48172 + Exchange OWA CVE-2026-42897 KEV deadlines (both due 2026-05-29 tomorrow) for a combined federal-deadline-density signal across the PM-28 → AM-29 → PM-29 brief windows.
- **TeamPCP corpus continuity** — Storm-2697 / GlassWorm / TeamPCP / Mini Shai-Hulud / Megalodon are the corpus-tracked SDLC-threat actor cluster. The CISA alert is the federal-escalation surface on a corpus-tracked threat already at HIGH threat-level for the TeamPCP roster anchor (#001).

## Flash trigger evaluation

- **Trigger 1**: NOT MATCHED. No new CVE-active-exploitation surface beyond what's already corpus-anchored. CVE-2026-48027 + CVE-2026-45321 KEV-listed 2026-05-27 (yesterday) — already corpus-covered. CISA alert is escalation, not new disclosure.
- **Trigger 2**: NOT MATCHED. No new tracked-actor attribution; CISA does not attribute by actor.
- **Trigger 3**: NOT MATCHED. No new IOC surface for Splunk check.
- **Trigger 4**: NOT MATCHED. No tracked-actor TTP change.
- **Trigger 5**: PARTIAL. CISA escalation on standing A&D-adjacent SDLC threat surface; multi-victim already corpus-confirmed (GitHub, Nx, ~3,800 + 5,561 repos). Defer to grader.
- **Trigger 6**: NOT MATCHED.

No FLASH escalation by collector. Candidate for PM-28 16:00 brief as federal-government-escalation update on the standing SDLC threat surface, paired with the LiteSpeed + Exchange OWA KEV-deadline-tomorrow carry-forwards.
