---
brief_id: 2026-05-27-afternoon
brief_type: afternoon
published_at: 2026-05-27T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: null  # no PM finding cleared "very likely" forward-looking threshold requiring red-team challenge per pipeline
human_override: null
status: published
run_id: afternoon-20260527-160000
word_count: 763
findings_referenced:
  - finding-2026-05-27-0007-cisa-kev-three-add-cve-2026-45321-tanstack-mini-shai-hulud-cve-2026-48027-nx-console-cve-2026-8398-daemon-tools
  - finding-2026-05-27-0009-github-advisory-yamcs-cve-2026-44632-server-side-code-injection-rce-spacecraft-mission-control-ad-direct
  - finding-2026-05-27-0001-crowdstrike-glassworm-takedown-roster-005-counter-adversary-operations-google-shadowserver  # PM enrichment layer only
  - finding-2026-05-27-0004-securityweek-lacmta-iran-black-shadow-mois-gambit-israel-cyber-directorate-relay-investigation-update  # PM enrichment layer only
  - finding-2026-05-27-0008-ox-security-thn-mouse5212-super-formatter-npm-claude-ai-user-data-credential-stealer-unattributed
carry_forwards_referenced:
  - cve-2026-48172-litespeed-kev-due-date-tomorrow-fri-2026-05-29
  - cve-2026-42897-exchange-kev-due-date-tomorrow-fri-2026-05-29
related_vulns:
  - CVE-2026-45321   # KEV-listed today; VT-006 state change
  - CVE-2026-48027   # KEV-listed today; VT-010 candidate
  - CVE-2026-8398    # KEV-listed today; not corpus-tracked
  - CVE-2026-44632   # Yamcs A&D-direct
  - CVE-2026-48172   # KEV deadline T-1
  - CVE-2026-42897   # KEV deadline T-1
related_actors:
  - "005"   # GlassWorm — PM enrichment
  - "001"   # TeamPCP — KEV three-add corpus carry-forward attribution
related_zero_days: []
related_campaigns:
  - cisa-kev-three-add-2026-05-27
  - glassworm-takedown-2026-05-26  # PM enrichment continuation
  - lacmta-iran-attribution-investigation-inv-2026-05-26-001  # PM enrichment continuation
  - ai-developer-tooling-supply-chain-pressure-arc
sentinel_sweeps_today:
  - 00:00 EDT — zero triggers
  - 06:00 EDT — zero triggers
  - 12:00 EDT — zero triggers
tlp: CLEAR
---

# Afternoon Brief — 2026-05-27

**[CISA KEV catalog v2026.05.27 added three CVEs at noon UTC today](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) — two are corpus-tracked supply-chain surfaces that just transitioned to CISA-attested active exploitation: CVE-2026-45321 TanStack (Mini Shai-Hulud, [VT-006](../vulnerabilities/VT-006-mini-shai-hulud/profile.md)) and CVE-2026-48027 Nx Console. Both carry June 10 federal remediation deadlines under BOD 22-01.**

**Why it matters:** DIB and CMMC partner-flow estates inherit FCEB compliance pressure on the same calendar — June 10 is the contractual hard line for A&D primes whose engineering SDLCs touch either ecosystem. VT-006's `@squawk` aviation-data namespace remains the structural exposure path; no A&D-prime named victim on either CVE.

---

## 🚨 Active Threats

**CISA adds three CVEs to KEV catalog v2026.05.27 (12:00 UTC) — two corpus-tracked, due June 10.**
- What: CVE-2026-45321 TanStack ([VT-006](../vulnerabilities/VT-006-mini-shai-hulud/profile.md) KEV-pending watch signal FIRED; due 2026-06-10 T+14) and CVE-2026-48027 Nx Console (corpus [finding-2026-05-20-FLASH-0001](../findings/finding-2026-05-20-FLASH-0001-teampcp-github-internal-repos-3800-breach-via-nx-console-malicious-extension.md) KEV-listed; due 2026-06-10 T+14). Third addition CVE-2026-8398 Daemon Tools Lite carries an accelerated T+3 dueDate (2026-05-30) but is not corpus-tracked — consumer ISO virtualization utility, out of A&D scope.
- Why it matters for A&D: KEV listing equals CISA-attested active exploitation per BOD 22-01. DIB / CMMC partner-flow estates inheriting FCEB compliance posture carry the same June 10 deadline. VT-006's underlying mechanism (npm registry maintainer-account compromise → credential-stealer published under trusted identity) is already corpus-anchored at A1 via Wiz + StepSecurity + Snyk on the [TeamPCP (#001)](../threat-actors/TeamPCP/profile.md) attribution chain. CISA KEV does not publish actor attribution — TeamPCP corpus carry-forward preserved per Hard Rule 2.
- Action: VT-006 _index.yaml flip kev_pending → kev (operator-tracked via vuln-tracker handoff). Scaffold VT-010 for CVE-2026-48027 Nx Console mirroring VT-006 pattern. DIB/CMMC SDLCs: inventory TanStack + Nx Console dependency graphs; treat embedded npm tokens, OIDC tokens, and 1Password vault material as potentially-compromised within the affected version windows per VT-006 and [finding-2026-05-20-FLASH-0001](../findings/finding-2026-05-20-FLASH-0001-teampcp-github-internal-repos-3800-breach-via-nx-console-malicious-extension.md) disposition.
- Source: [CISA KEV catalog v2026.05.27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) · Digraph: A1 · WEP: almost_certainly (procedural cataloging facts + dueDates); very_likely (active exploitation implication for the two corpus-tracked CVEs, already at this WEP per prior corpus dispositions); very_likely (DIB/CMMC partner-flow inheritance of FCEB compliance pressure).

## 🔓 Vulnerabilities

**[CVE-2026-44632 — Yamcs spacecraft mission-control RCE, CVSS 9.1, patched 5.12.7.](https://github.com/advisories/GHSA-524g-x36v-9wm6)** Yamcs project maintainers self-disclosed via GitHub Security Advisory ([GHSA-524g-x36v-9wm6](https://github.com/advisories/GHSA-524g-x36v-9wm6)) today: server-side code injection in `org.yamcs:yamcs-core` via Janino Expression Engine in the algorithm execution factory. Post-authenticated, high-privilege (`SystemPrivilege.ChangeMissionDatabase` required). No in-the-wild exploitation reported per vendor at disclosure; PoC is in the advisory body. Affected: all pre-5.12.7. Direct A&D fit — see Sector Focus below. Digraph: A2 · WEP: very_likely (CVE assignment, patch availability, no-ITW at disclosure as procedural facts); likely (exploitation trajectory, single-source veto on vendor-coordinated-disclosure class).

**KEV deadline tracker — Friday 2026-05-29 (T-1):**
- **CVE-2026-48172 (LiteSpeed cPanel)** — substance carried forward from [2026-05-26 afternoon](2026-05-26-afternoon.md); no new substance overnight. Patch `v2.4.7` + WHM `v5.3.1.0`. Digraph: A2.
- **[CVE-2026-42897](../vulnerabilities/Exchange-CVE-2026-42897/profile.md) (Exchange OWA XSS)** — substance carried forward; mitigation ESU + EEMS/EOMT. Digraph: A1.

## ✈️ Sector Focus: Aerospace & Defense

**Second consecutive brief with A&D-direct CVE focus.** Yamcs CVE-2026-44632 is structurally A&D-direct: open-source mission control software for spacecraft, satellites, and ground-station automation. Customer base spans commercial smallsat operators, government space agencies, and academic research consortia. Parallel to corpus [VT-005 OpenC3 COSMOS](../vulnerabilities/VT-005-openc3-cosmos/profile.md) five-CVE cluster from 2026-04-20 (NASA + BAE Systems user base attested at that surface). No A&D-prime named-customer disclosure on Yamcs yet; vuln-tracker handoff for VT-* scaffolding (slot arbitrated with VT-010 candidate for CVE-2026-48027). The post-auth + high-privilege gate narrows the immediate exposure boundary — but mission-database edit privileges are typically broadly delegated in real spacecraft-operations environments (telemetry engineer, software engineer, mission planning lead), so the practical exposure is wider than the CVSS vector suggests. Insider-threat and compromised-operator-credential scenarios remain valid attack paths; cross-spacecraft-mission lateral movement post-MDB-RCE is catastrophic-impact (mission database controls telemetry parsing, command authorization, algorithm execution chains). Carry-forward: [Gitea CVE-2026-27771](2026-05-27-morning.md) substance from AM unchanged — no patch-adoption telemetry or named A&D prime since.

## 🕵️ Actor Activity

**UPDATE: GlassWorm ([#005](../threat-actors/_roster.yaml), HIGH) — Russian-attribution corroboration enriched but veto holds.** Since this morning's brief, The Register relayed CrowdStrike's [GlassWorm takedown disclosure](https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/) (third PM relay; SecurityWeek + BleepingComputer + The Hacker News also on file — four relays total). New substance from the Register layer: **CIS-locale termination check** (Conti/TrickBot/Sandworm-toolkit precedent class) and **Russian-language code comments throughout source** are now A-attested via CrowdStrike. **John Hultquist confirmed Google Threat Intelligence Group's takedown role via social media** — first byline-credit surface for the GTIG partnership, but operational confirmation, not parallel-telemetry corroboration. Four relays of one A-grade primary do NOT constitute independent corroboration per the INTEL-GRADING independence test. Hard Rule 2 still holds: Archimedes preserves "the criminals are likely based in Russia" verbatim, with CrowdStrike's own caveat that no single indicator is proof on its own and that the code comments may reflect AI tooling rather than human authorship. Roster #005 `nation` field stays at `unknown` pending second A/B-grade IR-firm parallel telemetry. Digraph: A2 · WEP: likely (Russia-origin, single-source veto unchanged).

## 🇮🇷 Iran Cyber Watch

**UPDATE: LACMTA attribution — second alias "Ababil of Minab" surfaces via The Record; investigation lock holds.** [The Record (Suzanne Smalley, 09:20 EDT)](https://therecord.media/lacmta-cyberattack-iranian-attribution-gambit-security) became the second media relay of the Gambit Security primary research (SecurityWeek/Kovacs was first this morning). New surface from The Record layer: a second front-group alias **"Ababil of Minab"** — different naming from SecurityWeek's "Black Shadow" for what appears to be the same Gambit-Security-assigned MOIS-front cluster (two-name surface may be naming-overlap by the relays or two distinct Gambit labels; primary direct retrieval would resolve). Additional regional victims now named: Israeli media organization, Israeli university, Turkish insurance brokerage, additional Saudi sectors. **No A&D prime named in the expanded victim list.** The Record editorially mentions Handala Hack ([#014](../threat-actors/HandalaHack/profile.md)) and Stryker as a separate MOIS-front example — Archimedes does NOT cross-walk LACMTA Ababil-of-Minab/Black Shadow to Handala despite the shared MOIS service designation. Two relays of one Gambit-Security primary still fail the independence test. Investigation `inv-2026-05-26-001` carries forward through 2026-06-09 (T+13). Digraph: C3 · WEP unchanged: very_likely (LACMTA breach occurred); roughly_even_chance (Black Shadow / Ababil-of-Minab cluster + MOIS service attribution). No new activity from [UNC1549 (#004)](../threat-actors/UNC1549/profile.md), [Charming Kitten (#011)](../threat-actors/CharmingKitten/profile.md), [MuddyWater (#022)](../threat-actors/MuddyWater/profile.md), or Handala Hack in the PM-27 window.

## 📰 Other Signal

**AI-developer-tooling supply-chain pressure — 5th in-class event since 2026-05-12.** [OX Security via The Hacker News (11:44 EDT)](https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html) disclosed malicious npm package `mouse5212-super-formatter` (676 downloads at disclosure; attacker GitHub account `unplowed3584` created 2026-05-26, now suspended). Mechanism: npm postinstall stage triggers credential-stealer using victim's GitHub environment token OR a hardcoded fallback, then recursively uploads files from Anthropic Claude AI's `/mnt/user-data` directory to the attacker-controlled GitHub account. OPSEC failure: malware leaked its own hardcoded private GitHub token — lower-tier operator skill versus TeamPCP-tier tradecraft. **OX Security explicitly declines attribution** to TeamPCP / Shai-Hulud / Mini Shai-Hulud / GlassWorm / Megalodon lineage despite shared GitHub-token-exfil primitive; researchers characterize it as part of a broader lower-bar-entrants trend. Archimedes preserves the explicit decline per Hard Rule 2 — no cross-walk on technical-primitive adjacency alone. Joins the AI-developer-tooling-ecosystem-supply-chain-pressure arc (Mini Shai-Hulud → Nx Console → OpenAI TanStack → SymJack → MSTIC cryptojack → mouse5212-super-formatter). Digraph: B3 · WEP: likely (artifact existed); roughly_even_chance (campaign expansion forward-looking). A&D relevance: low-indirect — Anthropic Claude AI is the target, not A&D-prime SDLC software per se; structural-supply-chain-warning class for A&D engineering populations using Claude Code or the Anthropic API within ITAR-regulated SDLCs.

**Sentinel cadence.** Today's 00:00, 06:00, and 12:00 FLASH sweeps all fired zero triggers.

**First-party Splunk.** Zero `defenseclaw_local` events across CVE-2026-45321 / CVE-2026-48027 / CVE-2026-8398 / TanStack / Nx Console / Daemon Tools Lite / Yamcs / Janino / `mouse5212-super-formatter` / `unplowed3584` / `/mnt/user-data` / Ababil of Minab keyword sets in the PM-27 sweep. **67th consecutive dormant non-self sweep.** Per Hard Rule 8, silence is neither confirming nor disconfirming. Yamcs deployment posture at A&D-prime smallsat / mission-operator scope is bounded by `defenseclaw_local` visibility — silence does not confirm absence.

---

*Sources hyperlinked inline. Digraph per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-05-27. **CISA added three CVEs to KEV at noon UTC — two are corpus-tracked surfaces with June 10 federal deadlines.**

🚨 **Active Threats**

• **[CISA KEV adds CVE-2026-45321 TanStack, CVE-2026-48027 Nx Console, CVE-2026-8398 Daemon Tools](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)** — TanStack + Nx due **June 10**; Daemon Tools **June 1 (T+3)**. Both corpus CVEs anchor to TeamPCP. *DIB/CMMC inherit — inventory dependency graphs now.*

🔓 **Vulnerabilities**

• **[CVE-2026-44632 Yamcs spacecraft mission-control RCE, CVSS 9.1, patched 5.12.7](https://github.com/advisories/GHSA-524g-x36v-9wm6)** — Janino injection, post-auth + high-priv, no ITW. Mission-DB edit privs usually broadly delegated in spacecraft ops — practical exposure exceeds CVSS. *Patch 5.12.7.*
• **CVE-2026-48172 + CVE-2026-42897:** KEV deadline Friday May 29 — T-1.

🕵️ **Actor Activity**

• **[UPDATE: GlassWorm — CIS-locale + Russian-lang comments now A-attested via The Register](https://www.theregister.com/2026/05/27/glassworm_takedown/)** — 4th relay since AM; Hultquist confirmed GTIG. *4 relays of 1 A-primary aren't corroboration.* Roster #005 stays `nation: unknown`.

🇮🇷 **Iran Cyber Watch**

• **[UPDATE: LACMTA — 2nd alias "Ababil of Minab" via The Record](https://therecord.media/lacmta-cyberattack-iranian-attribution-gambit-security)** — Apparent 2nd Gambit label for the same MOIS-front cluster; more Israel/Saudi/Turkey victims, **A&D still absent**. *No cross-walk to MuddyWater or Handala.* Locked to June 9.

📰 **Other Signal**

• **[OX via THN: malicious npm exfils Claude AI `/mnt/user-data`](https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html)** — 5th in AI-dev-tooling supply-chain arc since May 12. **OX declines attribution**.
