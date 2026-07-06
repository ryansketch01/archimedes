---
id: "025"
primary_name: "Icarus"
aliases: []
mitre_attack_id: null
mitre_attack_url: null
type: "Cybercriminal (Extortion)"
attribution:
  nation: unknown
  service: null
  persona: "Mr Brean"
active_since: 2026
status: active
status_note: "Emerged 2026-04-28 per The Hacker News; two named victims to date as of 2026-06-19 (~7-week track record at first tracking). Single-IR-vendor (Huntress) attribution."
motivation:
  - extortion
  - data-theft
threat_level: LOW
admiralty_grade: B2
tlp: CLEAR
dossier_version: 1
last_updated: 2026-07-06
last_reviewed: 2026-07-06
next_review_due: 2026-10-04
profile_path: threats/threat-actors/Icarus/
iocs_path: threats/threat-actors/Icarus/iocs.md
threat_box_path: threats/threat-actors/Icarus/threat-box.yaml
related_actors: []
tracked_since: 2026-07-06
source_finding: finding-2026-06-19-0003
---

# Icarus — Threat Actor Profile

**Actor #025**

---

## Overview

Icarus is a financially-motivated extortion group that surfaced in a single documented campaign: the June 2026 compromise of Klue Inc., a Vancouver-based competitive-intelligence platform whose OAuth-integrated app (Klue Battlecards) connected to downstream customer Salesforce instances. Per Huntress, attackers used a compromised legacy credential associated with a Klue integration service to harvest OAuth tokens for customer Salesforce tenants, then extorted affected organizations. Two victims are publicly named — both cybersecurity firms (Huntress and Recorded Future); neither is an aerospace and defense prime. Extortion communications carried the persona "Mr Brean." The so-what for an A&D defender is modest and indirect: Icarus has no documented A&D-prime targeting, but the tradecraft — third-party SaaS compromise to reach downstream Salesforce tenants via OAuth-token abuse — describes a structural exposure pattern that any Salesforce-ecosystem tenant, including A&D primes, shares.

**Attribution confidence — read this before relying on the Icarus label.** The Icarus actor-identity attribution rests on a single IR vendor (Huntress), reported at "high confidence" (Huntress's confidence language paraphrased here per the source finding). Publisher independence holds — SecurityWeek, The Hacker News, and BleepingComputer relayed the story with distinct bylines — but evidence-basis independence fails: all publisher accounts trace to Huntress's single primary attribution. Under Archimedes grading this caps the admiralty grade at **B2** and the WEP at **likely** on the actor-identity layer. The dossier is deliberately thin. That is correct: careful, rigorous, and boring by design.

**Open question / standing tripwire (from the finding's SAT-KAC).** A load-bearing assumption (KAC A1, classified *test*, confidence *low*, centrality *critical*) is unresolved: whether Huntress's *actual* attribution language asserts "Icarus is a distinct actor" versus "Huntress is tracking this unattributed activity under the label Icarus." Huntress's primary publication was not retrieved. The Hacker News framed the campaign as "mirroring prior attack waves mounted by ShinyHunters and UNC6395" — but that is publisher framing, not Huntress attribution language. Per the finding's SAT-ACH, two hypotheses are **not operationally distinguishable on current evidence**: H1 (Icarus is a genuinely-distinct net-new actor) and H3 (Icarus is a UNC6395 affiliate/splinter). Both predict the same future behavior; the distinction is attribution theory, not observable tradecraft. Until Huntress's primary language is reviewed or a second IR vendor weighs in, `/new-actor` tracking proceeds under an explicit caveat that "Icarus" may be a provisional single-vendor label rather than a settled distinct-actor attribution.

**Hard Rule 2 — no cross-walk.** The observed TTP pattern (data theft + extortion + OAuth-token abuse via third-party SaaS) resembles that of ShinyHunters and UNC6395 (and, more loosely, Scattered Spider / UNC3944). Archimedes preserves Icarus as a distinct identity and does **not** originate any attribution linking it to those actors. See Connection Web for pattern-adjacent, non-attributed comparisons only.

---

## Primary Targets

- **Cybersecurity firms** — the two named victims (Huntress, Recorded Future) are both cybersecurity/threat-intelligence vendors that used the Klue Battlecards Salesforce integration. Huntress notes other cybersecurity firms use Klue but have not publicly disclosed impact.
- **Salesforce-ecosystem tenants (structural)** — any organization whose Salesforce data is reachable via a compromised third-party OAuth-integrated app. This is an exposure *pattern*, not a documented targeting *preference*.

**Geographic Focus:** Not established. No documented geographic targeting preference at this time; the two named victims are North American cybersecurity firms, but the sample is too small to infer geography.

**A&D-prime targeting:** None documented. A&D / DIB exposure is indirect and structural only (shared Salesforce-OAuth-integration-governance layer).

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Klue / Salesforce supply-chain compromise | 2026 | Compromise of Klue Inc. (2026-06-11) via a legacy credential tied to an integration service; OAuth tokens for downstream customer Salesforce instances harvested; Huntress and Recorded Future named as victims; extortion demands reached Huntress employees 2026-06-16; Salesforce disabled the Klue Battlecards app integration 2026-06-17. Per Huntress via THN. |

---

## TTPs (MITRE ATT&CK)

> No MITRE ATT&CK group ID has been assigned to Icarus. Techniques below are mapped from the single documented campaign's reporting; T-numbers are analyst-mapped to described behavior, not vendor-assigned.

### Initial Access

| ID | Technique |
|---|---|
| T1078.004 | Valid Accounts: Cloud Accounts — compromised legacy credential associated with a Klue integration service (initial vector, per Klue/Huntress) |
| T1199 | Trusted Relationship — abuse of a trusted third-party SaaS integration (Klue) to reach downstream customer Salesforce tenants |

### Credential Access

| ID | Technique |
|---|---|
| T1528 | Steal Application Access Token — OAuth tokens for downstream customer Salesforce instances harvested via legacy-credential exploitation |

### Collection / Exfiltration

| ID | Technique |
|---|---|
| T1213.003 | Data from Information Repositories: CRM — CRM/business data harvested from victim Salesforce tenants (business contacts, price quotes, sales messaging, client names) |
| T1567 | Exfiltration Over Web Service — sustained extraction via Salesforce REST API (per SW-Arghire: ~1,000 queries in 15 minutes; extraction windows >6 hours — single-publisher quantitative claim) |

### Impact

| ID | Technique |
|---|---|
| T1657 | Financial Theft — extortion of affected organizations following data theft ("Mr Brean" persona in extortion communications) |

---

## Malware Arsenal

No custom malware documented at this time. Reporting describes commodity tradecraft — legacy-credential abuse, OAuth-token harvesting, and Salesforce REST API queries via Python-`urllib` — with no named implant, loader, or backdoor attributed to Icarus.

---

## Infrastructure Patterns

- **Third-party SaaS integration as pivot** — compromise a trusted OAuth-integrated SaaS vendor (Klue) rather than the end victim directly; use harvested OAuth tokens to reach downstream Salesforce tenants.
- **Legacy-credential exploitation** — initial access via a compromised legacy credential tied to an integration service.
- **Commodity HTTP tooling** — Python-`urllib` user-agent strings referenced against the Salesforce REST API (defender-pattern hint, not an extractable IOC value).
- No dedicated attacker infrastructure (domains, IPs, C2) was published in any source at time of tracking.

---

## Known IOCs

No IOCs (file hashes, domains, IP addresses, or attacker infrastructure) were published in any source article body at time of tracking. Huntress IR-vendor primary research may contain an IOC table but was not retrieved. The only defender-pattern hints are Python-`urllib` user-agent strings and Salesforce REST API endpoint patterns referenced in vendor disclosures — these are hunt *context*, not extractable indicator values.

See `iocs.md` for the (currently indicator-empty) human-readable reference and hunt guidance, and `iocs.yaml` for the agent-queryable sidecar.

---

## Geopolitical Context

No nation-state attribution or geopolitical context is documented. Icarus is assessed by its single attributing vendor (Huntress) as a financially-motivated extortion group with no reported state nexus. Nation is `unknown`; no willingness constraints apply (criminal-actor baseline).

---

## Connection Web

The following are **pattern-adjacent, non-attributed** comparisons only. Per Hard Rule 2, Archimedes asserts **no attribution link** between Icarus and any of these actors. They are listed because their published tradecraft resembles Icarus's, not because any cited source has connected them to Icarus.

- **ShinyHunters** *(not tracked on `_roster.yaml`; no dossier)* — The Hacker News framed the Klue campaign as "mirroring prior attack waves mounted by ShinyHunters and UNC6395." This is a **methodological-similarity** observation by a publisher, **NOT** an attribution-overlap claim. Similar OAuth/SaaS-abuse tradecraft; NO attribution link asserted.
- **UNC6395** *(not tracked on `_roster.yaml`; no dossier)* — named alongside ShinyHunters in the same THN "mirrors" framing. Similar Salesforce-data-theft tradecraft; NO attribution link asserted.
- **Actor #013 Scattered Spider (UNC3944)** *(roster ID #013; dossier pending — no profile.md on disk)* — pattern-adjacent as an OAuth/SaaS-abuse-capable extortion ecosystem operator. The finding's SAT-ACH rated the Scattered-Spider-adjacency hypothesis (H5) *very unlikely* — Icarus's cybersecurity-firm victim concentration is inconsistent with UNC3944's historically broad enterprise targeting. Similar tradecraft class only; NO attribution link asserted.

The `related_actors` frontmatter array is intentionally empty — no confirmed relationships exist.

---

## Defense Recommendations

1. **Audit third-party OAuth-integrated apps against your Salesforce tenant** — enumerate connected apps in Salesforce Setup → Connected Apps OAuth Usage; revoke apps that are unused or over-scoped. Icarus's vector was a trusted third-party integration (Klue), not a direct Salesforce compromise.
2. **Constrain OAuth scopes and enforce token lifetimes** — apply least-privilege scopes to integration apps; shorten refresh-token lifetimes so a harvested token has a limited window.
3. **Rotate and retire legacy integration-service credentials** — the initial vector was a compromised legacy credential tied to an integration service. Inventory service accounts and rotate any legacy or shared credentials.
4. **Alert on anomalous Salesforce REST API volume** — Icarus's extraction was high-velocity (per SW-Arghire, ~1,000 queries in 15 minutes; multi-hour extraction windows). Baseline normal per-integration API call volume and alert on spikes.
5. **Hunt for non-browser user agents against the Salesforce API** — Python-`urllib` (and similar scripting) user agents hitting the Salesforce REST API from an integration context warrant review. This is a pattern hint, not a signature — expect false positives from legitimate automation.
6. **Treat SaaS-vendor breach notifications as your incident** — when a connected SaaS vendor discloses a compromise, immediately revoke that app's tokens and review recent API activity rather than waiting for confirmation of downstream impact.

---

## References

- [finding-2026-06-19-0003 — Klue/Salesforce supply-chain compromise; Icarus extortion group](../../findings/finding-2026-06-19-0003-klue-salesforce-supply-chain-compromise-icarus-extortion-group-huntress-recorded-future-named-victims-oauth-token-abuse-net-new-actor-candidate.md) (Archimedes finding; source of record for this dossier)
- SecurityWeek (Ionut Arghire), "Cybersecurity Firms Impacted by Klue Supply Chain Attack," 2026-06-19 — https://www.securityweek.com/cybersecurity-firms-impacted-by-klue-supply-chain-attack/
- The Hacker News (Ravie Lakshmanan), "Salesforce Disables Klue App Integration After OAuth Token Abuse Exposes Customer Data," 2026-06-19 — https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
- Huntress — IR-vendor primary on Icarus attribution and named-victim self-disclosure (primary publication not retrieved at time of tracking; cited via publisher relay).

> **No MITRE ATT&CK group page** — Icarus has no assigned ATT&CK group ID. **No DOJ indictment or government advisory** references Icarus at time of tracking.

---

*Created 2026-07-06 via `/new-actor Icarus` (operator Ryan). First-pass dossier from finding-2026-06-19-0003. Single-IR-vendor (Huntress) attribution; admiralty B2, WEP likely on actor-identity layer.*
