---
id: "011"
primary_name: "Charming Kitten"
aliases:
  - APT35
  - Magic Hound
  - Mint Sandstorm
  - Phosphorus
  - Newscaster
  - Ajax Security Team
  - Yellow Garuda
  - "TA453"            # Proofpoint taxonomy overlap
mitre_attack_id: G0059
mitre_attack_url: https://attack.mitre.org/groups/G0059/
type: "Nation-State APT"
attribution:
  nation: IR
  service: "IRGC-IO"   # IRGC Intelligence Organization
  unit: null
  attribution_source: "Long-running consensus across CrowdStrike, Microsoft MSTIC, Mandiant; reproduced in finding-2026-05-05-0002 from CrowdStrike + MSTIC concurrent A-grade publication 2026-05-04."
active_since: 2014
status: active
status_note: "Active Q2 2026 OAuth-consent credential harvest campaign vs. defense-policy think tanks per CrowdStrike + MSTIC 2026-05-04 (concurrent A-grade independent corroboration; digraph A1, WEP very likely)."
motivation:
  - espionage
  - persona-driven-credential-harvest
  - intelligence-collection-on-iran-policy-adversaries
  - defense-policy-and-academic-targeting
threat_level: LOW                  # Per /update-tracking 2026-05-09 — weighted overall 4.45 → LOW (auto-commit). Espionage category alone scores composite 9 (HIGH category-level); per-category HIGH does not trigger Hard Rule 5 gate.
admiralty_grade: A1                # Per finding-2026-05-05-0002 — concurrent A-grade independent corroboration
tlp: CLEAR
dossier_version: 2
last_updated: 2026-05-09
last_reviewed: 2026-05-09
next_review_due: 2026-08-07
profile_path: threats/threat-actors/Charming-Kitten/
iocs_path: threats/threat-actors/Charming-Kitten/iocs.md
threat_box_path: threats/threat-actors/Charming-Kitten/threat-box.yaml
related_actors:
  - "004"   # UNC1549 — IRGC-aligned sister cluster; persona-driven targeting overlap, distinct A&D-direct vs. think-tank ecosystems
  - "022"   # MuddyWater — fellow Iranian APT, MOIS not IRGC; distinct service tasking
  - "023"   # APT34 — MOIS-aligned, Iranian ecosystem context
  - "014"   # Handala Hack — MOIS-adjacent hacktivist-with-IRGC-backing pattern; structurally distinct mission profile
notes_first_pass: |
  First-pass dossier authored 2026-05-06 from finding-2026-05-05-0002 (CrowdStrike +
  Microsoft MSTIC concurrent 2026-05-04 publication, digraph A1, WEP "very likely",
  red-team review qualify with required briefer caveats). All attribution and TTP
  claims inherit from cited sources per Hard Rule 2.
notes_scoring: |
  /update-tracking Mode 2 run 2026-05-09 — weighted overall 4.45 → LOW → auto-commit.
  Espionage composite 9 (category HIGH) but doctrine keys gate on weighted overall
  only. Espionage Intent=4 (Ideology) — NOT 5 (Target-Specific) — per the red-team
  qualify directive on the source finding binding Intent against named think-tank
  victim ecosystem rather than extrapolating to ad-prime-v1. Operator-anticipated
  HIGH outcome did NOT materialize; the disciplined Intent=4 outcome is the qualify
  directive doing what it was meant to do. Splunk first-party check zero hits over
  -30d on all 6 IOCs and OAuth consent-grant audit-log patterns — no IOC bonus.
  See threat-box.md for full per-category narrative.
---

# Charming Kitten — Threat Actor Profile

**Actor #011**

---

## Overview

Charming Kitten is one of the longest-running and most-tracked Iranian cyber-espionage clusters, attributed by CrowdStrike, Microsoft MSTIC, Mandiant, Proofpoint, and Google TAG to the IRGC Intelligence Organization (IRGC-IO). Microsoft tracks the group as Mint Sandstorm (formerly Phosphorus); CrowdStrike's primary alias is Charming Kitten; MITRE ATT&CK lists the cluster as G0059 / APT35. The cluster has been documented operating since at least 2014 and is best known for persona-driven credential-phishing operations against defense-policy think tanks, Iran-nuclear-program researchers, MENA-focused journalists, and academic-and-research personas in the Iran-policy ecosystem.

For the Archimedes target profile (`ad-prime-v1` — mid-to-large US A&D contractor), Charming Kitten's relevance is **second-order but operationally important** for two reasons. First, the Q2 2026 campaign documented by CrowdStrike + MSTIC on 2026-05-04 (finding-2026-05-05-0002) introduced a new persistence path: OAuth application consent grants requesting `Mail.Read` + `Mail.ReadWrite` scopes via attacker-controlled apps (display name observed: "Policy Review Tool"). The OAuth consent-grant tradecraft is platform-generic — it works against any Entra ID tenant where users encounter consent dialogs — so even though the named victim ecosystem is think-tank/academic/journalist (with no defense primes named), the mechanism transfers to any M365 estate without operational lift. Second, defense-policy think-tank staff (Brookings, RUSI, Atlantic Council, named in CrowdStrike + MSTIC reporting) interact with prime corporate-affairs, government-affairs, and strategic-research personnel as a regular ecosystem feature — lateral pretext from a compromised think-tank persona into a prime mailbox is operationally plausible.

The 2026 OAuth tradecraft is the most consequential dossier delta. Prior Charming Kitten reporting through 2024–2025 documented persona-driven credential-phishing leaning on fake conference invitations, fake research collaborations, and HYPERSCRAPE credential-exfiltration tooling (originally documented by Mandiant in 2022 and Google TAG ahead of that). The OAuth consent-grant pivot is a quieter persistence path that survives password resets. Microsoft's detection guidance — published in the same 2026-05-04 disclosure — recommends Entra audit-log hunts for `Add app role assignment` and `Consent to application` events with `Mail.Read` / `Mail.ReadWrite` scopes outside standard admin-consent flows.

The 2026-05-04 reporting clears the corroboration test — CrowdStrike (Falcon-derived telemetry) and Microsoft MSTIC (Defender + Entra-derived telemetry) publish concurrently with separate evidence bases, neither citing the other. Microsoft surfaces the OAuth consent-grant tradecraft detail that CrowdStrike's blog does not, confirming independent observation. Digraph A1, WEP "very likely" on the attribution itself. **The red-team review on finding-2026-05-05-0002 issued a `qualify` recommendation with required briefer caveats** that distinguish (a) the attribution of the named campaign to Charming Kitten — solid — from (b) the generalization of OAuth consent-grant tradecraft to prime mailbox risk — forward-looking, mechanism-based, NOT observed prime-direct. That distinction must be carried forward into any future briefs.

---

## Primary Targets

- **Defense-policy think tanks** — Brookings, RUSI, Atlantic Council named in CrowdStrike + MSTIC 2026-05-04. Long-running pattern across 2024–2026.
- **Iran-nuclear-program researchers** — academic and policy researchers covering Iranian nuclear, missile, and military programs.
- **Journalists covering MENA security** — particularly Iran-focused journalists, dissident communities, exile media.
- **Iranian dissidents and human-rights advocates** — extensively documented across 2014–2025 reporting.
- **Government and DoD policy advisors** — through fake conference / research-collaboration personas.
- **Defense-adjacent academics and graduate students** — universities supporting defense-policy research.
- **Pharma and biotech (historical)** — Microsoft documented credential-targeting against pharma during 2020 COVID-vaccine research period.

**Geographic Focus:** US, UK, Israel; Iranian diaspora communities globally. The 2026 think-tank wave names US, UK, and Israeli think-tank ecosystems explicitly.

**A&D-prime relevance:** **Second-order, mechanism-driven.** No defense primes named as direct victims in the 2026-05-04 reporting. A&D risk is mediated through (1) ecosystem persona-overlap with prime corporate-affairs / government-affairs / strategic-research staff, and (2) the platform-generic nature of the OAuth consent-grant tradecraft, which would land equivalently against a prime tenant lacking admin-consent restriction posture. See Defense Recommendations for the concrete moves.

---

## Signature Campaigns

| Campaign | Year | Description |
|---|---|---|
| Newscaster persona network | 2014 | iSIGHT Partners (later FireEye/Mandiant) documents fake-journalist persona network used for credential phishing against US/UK targets — earliest publicly-documented Charming Kitten campaign. |
| HBO / dissident targeting | 2017 | DOJ unsealed indictment naming Behzad Mesri for HBO intrusion; broader IRGC cyber operations context. |
| 2018–2020 dissident credential-phishing | 2018–2020 | Sustained Microsoft, CERTFA, and Google TAG reporting of credential-phishing against Iranian dissidents, journalists, and academics. |
| HYPERSCRAPE disclosure | 2022 | Mandiant documents HYPERSCRAPE credential-exfiltration tooling — operator-controlled tool that downloads contents of a compromised mailbox after credential capture. |
| LA Times-style fake conferences and academic personas | 2022–2024 | Microsoft and Proofpoint document persistent academic / journalist persona pretexts. |
| Q2 2026 OAuth consent-grant credential harvest | 2026-02 to 2026-04 | CrowdStrike + MSTIC 2026-05-04 — campaign against US/UK/IL defense-policy think tanks, Iran-nuclear researchers, MENA security journalists. New HYPERSCRAPE variant + new OAuth consent-grant persistence tradecraft (Mail.Read + Mail.ReadWrite scopes via attacker-controlled "Policy Review Tool" app). |

---

## TTPs (MITRE ATT&CK)

> **First-pass scaffold.** Techniques below reflect long-running Charming Kitten reporting plus the 2026-05-04 OAuth-tradecraft delta. Full ATT&CK mapping deferred to a subsequent collector pass against MITRE G0059 and current vendor disclosures.

### Initial Access

| ID | Technique |
|---|---|
| T1566.002 | Spearphishing Link (OAuth phishing pages mimicking Microsoft login; "comment on a paper draft" pretext per CrowdStrike + MSTIC 2026-05) |
| T1566.001 | Spearphishing Attachment (historical pattern; less prominent in 2026 OAuth campaign) |
| T1566.003 | Spearphishing via Service (LinkedIn, expert-outreach personas) |
| T1199 | Trusted Relationship (think-tank persona compromise leveraged for adjacent outreach) |

### Execution

| ID | Technique |
|---|---|
| T1059.001 | PowerShell (updated PowerShell loader documented in 2026 reporting) |
| T1204.001 | User Execution: Malicious Link |

### Persistence

| ID | Technique |
|---|---|
| T1098 | Account Manipulation |
| **T1528** | **Steal Application Access Token — OAuth application consent grants requesting Mail.Read + Mail.ReadWrite scopes; attacker-controlled apps registered with deceptive display names (e.g., "Policy Review Tool"). Mint Sandstorm 2026 Q2 tradecraft per MSTIC 2026-05-04. Persistence survives password resets — this is the operationally consequential 2026 delta.** |
| T1136 | Create Account (rare; persona-driven over account-creation) |

### Defense Evasion

| ID | Technique |
|---|---|
| T1036 | Masquerading (lookalike Microsoft-login domains; deceptive OAuth app display names) |
| T1027 | Obfuscated Files |
| T1550.001 | Use Alternate Authentication Material: Application Access Token (post-OAuth-consent persistence) |

### Credential Access

| ID | Technique |
|---|---|
| T1056.003 | Web Portal Capture (OAuth phishing landing pages) |
| T1110 | Brute Force (post-2014 password-spray patterns documented by Microsoft) |

### Collection / Exfiltration

| ID | Technique |
|---|---|
| T1114.002 | Email Collection: Remote Email Collection (HYPERSCRAPE; OAuth-token-driven mailbox download) |
| T1567 | Exfiltration Over Web Service (cloud-hosted credential exfiltration C2) |
| T1041 | Exfiltration Over C2 Channel |

---

## Malware Arsenal

| Malware | Type | Notes |
|---|---|---|
| HYPERSCRAPE | Credential-exfiltration tool | Originally documented by Mandiant 2022; new variant in 2026 campaign per CrowdStrike + MSTIC. Downloads target mailbox contents after credential capture. |
| Updated PowerShell loader | Loader | 2026 campaign per CrowdStrike — companion to HYPERSCRAPE in the post-OAuth landing flow. |
| TBD post-2024 backdoor families | Multiple | Historical reporting documents miscellaneous custom and modified-commodity tooling. Full arsenal mapping deferred to subsequent collector pass. |

> **Source-of-record arsenal note:** HYPERSCRAPE has been the operationally-load-bearing tool across multiple Charming Kitten campaigns. The 2026 variant is the first publicly-documented update since 2022 (per CrowdStrike + MSTIC 2026-05-04). Charming Kitten operates more on the persona-and-tradecraft axis than on novel malware development; its custom tooling investment is comparatively lighter than UNC1549's MINIBIKE/MINIBUS toolchain.

---

## Infrastructure Patterns

- **OAuth phishing landings on Microsoft-lookalike domains** — `login-microsoft365-secure.com`, `m365-policy-review.org` (per CrowdStrike + MSTIC 2026-05-04). Domain naming follows deceptive Microsoft-365 / policy-review patterns.
- **Cloud-hosted credential C2** — `hyperscrape-update.net` (per CrowdStrike) used as HYPERSCRAPE C2 in the 2026 campaign.
- **Persona-driven domain registration ahead of campaign waves** — long-running pattern: domain registrations match the lure persona (research-domain, journalist outlet, conference-host).
- **Tehran-aligned operational tempo** — CrowdStrike cites operational-hours pattern as one attribution pillar in 2026-05-04 reporting; consistent with prior reporting across 2014–2025.
- **Attacker-controlled OAuth applications as Entra ID artifacts** — display name "Policy Review Tool" per MSTIC 2026-05; the application registration itself is an Entra audit-log artifact (`Add service principal` / `Consent to application` events).

---

## Known IOCs

This profile is a first-pass scaffold built from the six IOCs published by CrowdStrike + MSTIC on 2026-05-04 (finding-2026-05-05-0002). See [`iocs.md`](./iocs.md) and [`iocs.yaml`](./iocs.yaml) for the structured indicator set, organized by:

- OAuth phishing domains and HYPERSCRAPE C2 domain
- C2 IPv4 (hosting hyperscrape-update.net)
- HYPERSCRAPE staging hash (2026 variant)
- Behavioral indicator: attacker-controlled OAuth application "Policy Review Tool" with `Mail.Read` + `Mail.ReadWrite` scopes (T1528)

**No first-party Splunk observations of Charming Kitten infrastructure as of 2026-05-06** — collector queried `defenseclaw_local` and `archimedes` indices for the six IOCs over -30d window with zero hits. Silent telemetry, not disconfirming.

The OAuth consent-grant tradecraft is the most operationally consequential indicator class for a prime-tier defender, because it is detectable in Entra audit logs **regardless of whether Charming Kitten is the actor currently using it** — the platform-generic mechanism applies to any actor who registers an attacker-controlled app and lures users through consent dialogs.

---

## Geopolitical Context

Charming Kitten / Mint Sandstorm operates as part of Iran's broader IRGC-aligned cyber-operations ecosystem. The IRGC Intelligence Organization (IRGC-IO) — distinct from Iran's Ministry of Intelligence and Security (MOIS) — is the long-running attributed sponsor per CrowdStrike, Microsoft MSTIC, Mandiant, and US Government reporting. The cluster's operational signature is intelligence-collection-driven persona phishing rather than the destructive or hack-and-leak patterns associated with sister IRGC-aligned and MOIS-aligned clusters.

The 2026 think-tank wave fits the IRGC-IO mission profile: Iran's strategic interest in collection against external Iran-policy formation (think tanks → policy advisors → US government) is a sustained tasking. The introduction of OAuth consent-grant tradecraft reflects an evolution toward quieter, post-password-reset-resilient persistence — a tradecraft maturation rather than a mission-profile shift.

For a US A&D prime, Charming Kitten risk maps to:

- **Strategic-research, government-affairs, corporate-affairs staff** — these personnel interact with the named victim ecosystem (defense-policy think tanks) as a regular feature; lateral pretext from a compromised think-tank persona is operationally plausible (ACH H2 in finding-2026-05-05-0002 ranked 3rd at one inconsistency).
- **Mechanism-portability of OAuth consent-grant tradecraft to prime tenants** — the tradecraft is platform-generic; any Entra ID tenant without admin-consent restriction for `Mail.Read` / `Mail.ReadWrite` scopes is exposed to equivalent technique whether or not Charming Kitten specifically targets the tenant. This is the load-bearing forward-risk surface; the red-team review on finding-2026-05-05-0002 explicitly required briefs to keep mechanism-risk and observed-activity distinct.
- **Academic and research partnerships** — primes operating defense-research partnerships with named target universities or research institutes face indirect exposure if a research partner mailbox is compromised.

Charming Kitten is **NOT** the most A&D-direct Iranian APT — UNC1549 is. Charming Kitten is the most **mechanism-portability-relevant** Iranian APT via the OAuth consent-grant tradecraft. Briefs and dossier consumers must keep the two distinctions clear.

---

## Connection Web

- ⛓️ **[Actor #004 UNC1549](../UNC1549/profile.md)** — Sister IRGC cluster (IRGC vs. IRGC-IO). UNC1549 is A&D-direct (recruiter-lure into A&D primes); Charming Kitten is academic / think-tank / journalist focus with mechanism-portability A&D risk. Persona-driven targeting overlap as a tradecraft pattern; distinct ecosystems.
- ⛓️ **[Actor #022 MuddyWater](../MuddyWater/profile.md)** — Fellow Iranian APT, but MOIS rather than IRGC-IO. Different service tasking; occasional shared infrastructure historical patterns per Microsoft tracking.
- ⛓️ **[Actor #023 APT34](../APT34/profile.md)** — MOIS-aligned; overlapping Iranian-ecosystem context but no documented operational overlap with Charming Kitten specifically.
- ⛓️ **[Actor #014 Handala Hack](../Handala-Hack/profile.md)** — MOIS-adjacent hacktivist-with-IRGC-backing pattern. Structurally distinct mission profile (hack-and-leak influence operations); not an operational sibling, but Iranian-ecosystem context warrants the link.

---

## Defense Recommendations

1. **Audit Entra ID consent posture** — Require admin consent for `Mail.Read`, `Mail.ReadWrite`, `Mail.Send`, `Files.Read.All`, and any high-risk delegated scopes. Set tenant default to "Do not allow user consent" for unverified publishers. This is the highest-value preventive control against the 2026 OAuth tradecraft and is **mechanism-level**, not Charming-Kitten-specific.
2. **Hunt Entra audit logs for unauthorized consent events** — Run retrospective hunt against `consent-to-application` and `Add app role assignment` events for high-risk scopes (`Mail.Read`, `Mail.ReadWrite`) outside standard admin-consent flows. Cover the Feb–Apr 2026 campaign window if audit-log retention permits (KAC A5 in finding-2026-05-05-0002 flags retention gaps as a real risk).
3. **Investigate suspicious OAuth app registrations** — Specifically attacker-controlled apps with deceptive display names ("Policy Review Tool" per MSTIC 2026-05). Maintain an inventory of legitimate enterprise OAuth applications; alert on new app registrations with high-risk scope requests.
4. **Conditional Access for high-risk scope grants** — Where Entra license tier permits, require MFA reauthentication before consent dialogs with `Mail.*` scopes; block consent from unverified publishers via Conditional Access app filter.
5. **Strategic-research and government-affairs persona-awareness training** — Personnel who interact with defense-policy think tanks regularly are operationally exposed to the lateral-pretext H2 hypothesis. Train on "comment on paper draft" / fake-conference / fake-collaboration pretexts, including the OAuth consent-dialog red flag.
6. **Hunt for the six published CrowdStrike + MSTIC IOCs across -90d window** — Run retrospective hunt against `defenseclaw_local` and `archimedes` for `login-microsoft365-secure.com`, `m365-policy-review.org`, `hyperscrape-update.net`, `194.87.44.99`, the HYPERSCRAPE 2026 hash, and the OAuth app registration pattern. See `iocs.yaml` hunt queries.
7. **Phishing-resistant MFA on all privileged accounts** — Standard hygiene; relevant because Charming Kitten's traditional credential-phishing pretext layer continues alongside the new OAuth tradecraft.
8. **Coverage attestation for Entra audit-log ingestion** — KAC A1 in finding-2026-05-05-0002 flags this as the load-bearing assumption: confirm whether `consent-to-application` events are ingested into `defenseclaw_local`, what retention is in place, and whether existing rules alert on `Mail.Read` / `Mail.ReadWrite` scope grants outside admin-consent flow.

---

## Attribution Notes

Per Hard Rule 2, all attribution claims trace to cited public sources. The 2026-05-04 disclosure rests on **concurrent independent A-grade attribution** from CrowdStrike (Falcon-derived telemetry, "Charming Kitten") and Microsoft MSTIC (Defender + Entra-derived telemetry, "Mint Sandstorm"). Both vendors publish same-day with separate evidence bases; neither cites the other. This is the strongest corroboration tier in the 2026 corpus to date — distinct from finding-2026-05-05-0001 (UNC1549, single-source) and finding-2026-05-06-FLASH-0002 (MuddyWater, single-source with red-team `qualify`).

The roster confirms `Charming Kitten` ↔ `Mint Sandstorm` as authoritative aliases for cluster ID 011. No new actor entry was needed.

**Red-team `qualify` directive (carried forward from finding-2026-05-05-0002):**

The red-team review on the 2026-05-05 finding issued a `qualify` outcome with required briefer caveats. The directive: any future brief MUST explicitly distinguish (a) the attribution of the named campaign to Charming Kitten / Mint Sandstorm — solid at A1 / very likely — from (b) the generalization of OAuth consent-grant tradecraft to prime mailbox risk — forward-looking, mechanism-based, NOT observed prime-direct. Briefs must NOT characterize prime-direct OAuth-consent activity as observed or attributed by either vendor; that mechanism-level risk applies regardless of which actor is currently using it. This dossier carries the same discipline.

---

## References

- [CrowdStrike: Charming Kitten think-tank credential harvest 2026 Q2 (2026-05-04)](https://www.crowdstrike.com/blog/charming-kitten-thinktank-credential-harvest-2026-q2/) — A1 originating
- [Microsoft MSTIC: Mint Sandstorm Q2 2026 credential harvest (2026-05-04)](https://www.microsoft.com/en-us/security/blog/2026/05/mint-sandstorm-q2-2026-credential-harvest/) — A1 originating
- [The Record: Charming Kitten / Mint Sandstorm think-tank 2026 (2026-05-04)](https://therecord.media/charming-kitten-mint-sandstorm-thinktank-2026) — B (relay)
- [MITRE ATT&CK G0059 — Magic Hound / APT35](https://attack.mitre.org/groups/G0059/)
- [Mandiant: HYPERSCRAPE (2022)](https://cloud.google.com/blog/topics/threat-intelligence/) — original HYPERSCRAPE disclosure (specific URL via Mandiant blog index)
- [Microsoft: Mint Sandstorm overview](https://www.microsoft.com/en-us/security/blog/) — Microsoft taxonomy and tracking
- [CERTFA / Iran Threats project](https://blog.certfa.com/) — long-running Iran cyber threat reporting on Charming Kitten dissident targeting
- [Google TAG quarterly bulletins](https://blog.google/threat-analysis-group/) — credential-phishing reporting against journalists, dissidents, and policy researchers
- finding-2026-05-05-0002 — Archimedes graded finding (digraph A1, WEP "very likely", red-team `qualify`); source-of-truth for the Q2 2026 campaign with full ACH / KAC analysis and required briefer caveats.

---

*First-pass profile authored 2026-05-06 by `actor-profiler` from finding-2026-05-05-0002.
All attribution and TTP claims herein inherit from cited sources per Hard Rule 2 — Archimedes
does not originate attribution. Threat-box scoring is TEMPLATE pending /update-tracking pass
with /approve-scoring gate. Red-team `qualify` directive on prime-tradecraft-portability
distinct from observed-prime-targeting carried forward.*
