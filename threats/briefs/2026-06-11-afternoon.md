---
brief_id: 2026-06-11-afternoon
brief_type: afternoon
published_at: 2026-06-11T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: applied_to_ivanti_kev_bod_26_04_layer_scoping_oracle_peoplesoft_mitigations_only_and_dib_pull_softening
human_override: null
status: published
run_id: afternoon-20260611-160000
word_count: 728
findings_referenced:
  - finding-2026-06-11-0005
  - finding-2026-06-11-0006
  - finding-2026-06-11-0007
  - finding-2026-06-11-0008
  - finding-2026-06-11-0009
  - finding-2026-06-11-0010
  - finding-2026-06-11-0011
  - finding-2026-06-11-0012
related_vulns:
  - CVE-2026-10520
  - CVE-2026-35273
  - CVE-2026-5027
related_actors:
  - "Void Blizzard (per The Record relay of DOJ filing; NOT in Archimedes roster; /new-actor DEFER pending DOJ primary retrieval)"
  - "The Gentlemen / Storm-2697 / LARVA-368 / Phantom Mantis (per PRODAFT + Microsoft; NOT in roster; /new-actor candidacy strengthened, A&D weak — operator decision pending)"
  - "ShinyHunters (self-claim only; carry-forward; Hard Rule 2 binding)"
update_on:
  - 2026-06-11-am-001 (Ivanti Sentry CVE-2026-10520 — CISA KEV inclusion + 3-day FCEB deadline + BOD 26-04; federal procedural attestation, not new telemetry; morning "mass" hedge carries forward)
  - 2026-06-11-flash-1200-001 (Oracle PeopleSoft CVE-2026-35273 — mitigations-only posture firmed at A1 via three-publisher convergence; ZDI Childs "limited exploitation" introduces independent scale tension)
  - 2026-06-10-pm-008 (The Gentlemen — PRODAFT Phantom Mantis + Microsoft Storm-2697 corroborate Krebs OSINT on Yapaev; LARVA-368 designation + 478 victim claim + prior LockBit/Qilin/Medusa affiliate history)
new_actor_decisions_pending:
  - actor_name: Void Blizzard
    candidacy: DEFER
    rationale: analyst_recommendation_pending_primary_doj_filing_retrieval_single_b_grade_source_at_compose
  - actor_name: The Gentlemen
    candidacy: APPROVE_CANDIDACY_OPERATOR_DECISION_PENDING
    rationale: three_independent_vendor_attributions_corroborate_yapaev_identity_but_a_d_relevance_weak_13_percent_us_zero_defense_victims_named
    do_not_initiate_in_brief: true
tlp: GREEN
tlp_rationale: "Public open-source reporting; structural-indirect A&D relevance; charged subjects named per LEGAL-POLICY data-handling table"
discord_delivery:
  channel: intel-briefs
  channel_id: "1499952717173358672"
  message_ids:
    - "1514737249948795053"
  parts: 1
  layer_2_chars: 1884
  delivered_at: 2026-06-11T16:00:00-04:00
  late: false
  via: librarian
---

# Afternoon Brief — 2026-06-11

**CISA added Ivanti Sentry CVE-2026-10520 to KEV with a 3-day FCEB deadline and issued BOD 26-04, a new risk-based vulnerability management directive; Oracle PeopleSoft CVE-2026-35273 is now firmly anchored at mitigations-only with no GA patch; DOJ unsealed an indictment of a Russian national for infrastructure-provider support to the Void Blizzard cyberespionage cluster.**

**Why it matters:** A&D defenders patch on the morning's evidence base, not on a new federal scale claim — the KEV listing is *procedural* attestation, not new telemetry, and the morning's "mass" hedge holds. BOD 26-04's 3-day clock is FCEB-only; treat as aspirational for DIB primes. Oracle PeopleSoft remains mitigations-only — apply now, treat ShinyHunters' 100-org claim as upper-bound.

---

## 🚨 Active Threats

**UPDATE: CISA adds Ivanti Sentry CVE-2026-10520 to KEV; FCEB deadline 2026-06-14; BOD 26-04 issued**
- What: [CISA added CVE-2026-10520 to KEV today](https://www.bleepingcomputer.com/news/security/cisa-orders-federal-agencies-to-patch-ivanti-sentry-vulnerability-in-three-days/) with the KEV short description *"unmanaged appliances with externally accessible endpoints"* (6 words). [BOD 26-04 issued same day](https://www.helpnetsecurity.com/2026/06/11/cisa-bod-26-04-risk-based-vulnerability-management/) establishes a risk-based VM framework: 3-day remediation for KEV + internet-exposed + automatable + full system control; 14-day default for lower-risk; 60-day policy update; 180-day full compliance.
- Why it matters for A&D: BOD 26-04 is statutorily FCEB-only — does NOT bind DIB primes, contractors, DoD War, or IC. Indirect structural pull on DIB via KEV-as-industry-standard absorption is **roughly even chance** per red-team — the 2021 KEV launch precedent is a single analogy and BOD 26-04 introduces new risk-factor scoring not mechanistically equivalent. Treat the 3-day clock as aspirational for DIB SLAs, NOT contractual.
- Action: **Patch Internet-exposed Sentry to R10.5.2 / R10.6.2 / R10.7.1 today** if not already done per the morning brief. KEV federally codifies ITW status; it does NOT publish new telemetry. Shadowserver's 19/2 baseline from this morning remains the only published exploitation-scale evidence; the "mass" framing stays capped per red-team carry-forward.
- Source: CISA KEV (A) + CISA BOD 26-04 (A) + BleepingComputer (B) + Help Net Security (B prov) + [SecurityWeek](https://www.securityweek.com/cisa-issues-binding-operational-directive-on-vulnerability-management/) (B). Digraph: **A1** · WEP: **very likely** on procedural-attestation layer; **likely** on operational scale (carry-forward).
- 🔗 **Update on:** [2026-06-11 morning brief](./2026-06-11-morning.md). CVE-2026-10523 (companion auth bypass CVSS 9.9) NOT in this KEV addition; remains exploitable.

**UPDATE: Oracle PeopleSoft CVE-2026-35273 — mitigations-only firmed at A1; ZDI characterizes exploitation as limited**
- What: SecurityWeek confirms verbatim *"only mitigations have been released by Oracle rather than a full patch"* (12 words). Trend Micro ZDI's Dustin Childs, reporter-credit holder per Oracle's advisory, [characterizes exploitation as limited](https://www.theregister.com/2026/06/11/oracle_peoplesoft_zero_day_shinyhunters/) — independent evidence basis in tension with ShinyHunters' 100-org self-claim. HIBP analysis of the leaked Nottingham dump enumerates ~455,000 unique email addresses plus passport numbers and payment details — independent of ShinyHunters' attestation.
- Why it matters for A&D: Three-publisher convergence may share a single Mandiant-sourced chain — treat mitigations-only as **likely** durable until Oracle-side independent verification. DIB exposure is **roughly even chance** pending deployment-density signal; no A&D-prime victim is named, and ShinyHunters' victim profile is mostly educational per Help Net Security.
- Action: Apply Oracle's out-of-band mitigations on PeopleTools 8.61 / 8.62 (and earlier unsupported versions); hunt against the 7 IOCs already in corpus from [finding-2026-06-10-0012](../findings/finding-2026-06-10-0012-bleepingcomputer-oracle-peoplesoft-shinyhunters-self-attested-300-instances-100-orgs-gadget-chain-failed-fbi-attempt-7-iocs.md); treat ShinyHunters' 100-org claim as upper-bound self-attestation. The Register relays publisher-side skepticism on ShinyHunters' history of misrepresenting access.
- Source: [SecurityWeek](https://www.securityweek.com/oracle-addresses-peoplesoft-vulnerability-amid-reports-of-zero-day-attacks/) (B) + [Help Net Security](https://www.helpnetsecurity.com/2026/06/11/oracle-peoplesoft-under-attack-cve-2026-35273/) (B prov) + The Register (B) + [The Record](https://therecord.media/university-of-nottingham-cyber-incident-shiny-hunters) (B). Mandiant Carmakal LinkedIn is upstream A-grade primary. Digraph: **A2** · WEP: **likely** on operational ITW (single-source veto carry-forward); **very likely** on mitigations-only posture.
- 🔗 **Update on:** [2026-06-11 12:00 FLASH](./2026-06-11-flash-1200.md) — mitigations-only firmed from "likely" to A1; ZDI "limited" framing constrains scale. The second-zero-day cluster framing (alongside CVE-2026-20245 Cisco SD-WAN) is **observational only**, not a coherent operational pattern per red-team. Per Hard Rule 2, ShinyHunters remains self-claim only.

## 🔓 Vulnerabilities

**NEW: Langflow CVE-2026-5027 (CVSS 8.8) path-traversal RCE in active exploitation per VulnCheck**
- What: [SecurityWeek relays VulnCheck research](https://www.securityweek.com/langflow-path-traversal-vulnerability-exploited-in-the-wild/) attesting in-the-wild exploitation of a path-traversal-to-arbitrary-file-write in `POST /api/v2/files`, effectively unauthenticated via Langflow's auto-login default. Originally disclosed by Tenable 2026-03-27; patch has been out three months. VulnCheck scans count ~7,000 internet-accessible Langflow instances skewed to North America.
- Why it matters for A&D: First confirmed-ITW AI-workflow-platform compromise in the Archimedes corpus. No A&D-prime named victim — structural inference only; A&D R&D environments are **likely** to host LangChain/Langflow for internal AI-assisted engineering, but no source-confirmed deployment data this sweep.
- Action: Patch Langflow post-March 2026; audit internal-facing instances; disable auto-login default if exposed externally. Treat ~7,000-instance count as VulnCheck-sole telemetry.
- Source: SecurityWeek (B) sole in-window publisher relaying VulnCheck (B prov). Digraph: **B2** · WEP: **likely** (single-source veto on ITW + scanning numbers).

## ✈️ Sector Focus: Aerospace & Defense

The Ivanti Sentry KEV listing and the Oracle PeopleSoft UPDATE carry the sector-specific load this cycle. No additional A&D-watchlist-entity-named activity in the last 24 hours. Void Blizzard's longitudinal Microsoft-tracked victim profile names "defense contractors" in source-language sector taxonomy — see Actor Activity below.

## 🕵️ Actor Activity

**DOJ unseals indictment of Denis Obrezko (36, Russian national) for infrastructure-provider role in Void Blizzard cluster**
- What: [The Record reports](https://therecord.media/russian-national-denis-obrezko-void-blizzard-indictment-thailand-extradition) DOJ unsealed the indictment 2026-06-10; Obrezko was arrested November 2025 in Phuket, Thailand (FBI / Thai Royal Police joint op), extradited, with initial Boston federal court appearance 2026-06-10. Prosecutors allege Obrezko used cryptocurrency to purchase VPS and domains used as Void Blizzard attack infrastructure. At least 11 U.S. companies compromised per prosecutors.
- Why it matters for A&D: The Record characterizes Void Blizzard's longitudinal victim profile as **"government agencies, defense contractors, transportation, media, healthcare, NGOs"** (10 words) operating across Europe and North America. Source-direct sector taxonomy; the 11 U.S. companies are NOT enumerated and **no A&D-prime is named** as a specific victim.
- /new-actor decision: **DEFER pending direct DOJ filing retrieval.** Single B-grade in-window source through B-grade relay. Per Hard Rule 2, Archimedes does NOT map Void Blizzard to APT28 / Sandworm / Cozy Bear / any roster actor.
- Source: The Record (B) sole publisher. Digraph: **B2** · WEP: **likely** (single-source veto on substantive operational claims).
- 🔗 **Pairs with:** [2026-06-11 morning brief](./2026-06-11-morning.md) — China-attribution FBI/DOJ 13-website seizure ran this morning. Three counter-cyberespionage data points across China and Russia surfaces in a 7-day window (AM + PM + 2026-06-04 Five Eyes). **Temporal continuity, NOT confirmed campaign continuity.**

**Material extension: The Gentlemen / Storm-2697 / LARVA-368 — PRODAFT + Microsoft corroborate Krebs OSINT on Yapaev**
- What: [The Hacker News relays PRODAFT research](https://thehackernews.com/2026/06/the-gentlemen-ransomware-prodaft-microsoft.html) tracking The Gentlemen as Phantom Mantis with operator designation LARVA-368; Microsoft independently tracks the same operator as Storm-2697. PRODAFT names Yapaev as prior LockBit affiliate (Tenacious Mantis), Qilin (Pestilent Mantis), and Medusa (Venomous Mantis) before transitioning to independent operator July 2025. Claimed victim count: 478. Technical: Go binary + Garble obfuscation, X25519 + XChaCha20, Windows/Linux/ESXi/LVM, `--spread` worm-flag, 2–6 week dwell.
- Why it matters for A&D: Geographic distribution is only ~13% U.S.-based (majority Thailand / UK / Brazil / Germany / India per PRODAFT). No A&D-prime victim, no defense-sector targeting per source. Watchlist signal only. The `--spread` worm-flag is defensible at endpoint command-line audit layer.
- /new-actor decision: **Candidacy strengthened by three vendor-tier attributions converging on Yapaev identity, but A&D-prime relevance weak (~13% U.S., zero defense-sector victims named).** Operator decision pending — Archimedes does NOT initiate /new-actor in this brief. Yapaev's prior LockBit affiliation is a touchpoint for [LockBit roster #015](../threat-actors/015-lockbit/profile.md) (next review 2026-07-10); Hard Rule 2 binding — do NOT extend the LockBit dossier to cover The Gentlemen's independent operations.
- Source: The Hacker News (B prov) relaying PRODAFT (B prov) + Microsoft Storm-2697 (MSTIC ratified A originator). Digraph: **B2** · WEP: **likely** (single-source veto on PRODAFT-specific details).
- 🔗 **Material extension on:** [2026-06-10 afternoon brief](./2026-06-10-afternoon.md) — three independent vendor-tier attributions on the same Yapaev identity lift identity-layer confidence above 2026-06-10's Krebs-only baseline.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h.

## 📰 Other Signal

**OnyxC2 MaaS — BlackFog vendor research; credential-stealer commoditization watchlist.** [SecurityWeek](https://www.securityweek.com/onyxc2-maas-credential-stealer-blackfog-research/) + Security Affairs relay BlackFog research on a new MaaS at $250/mo (standard) / $500/mo (HVNC premium) / $6,000 source-code purchase. 210+ application targets, 95+ Chromium and 14+ Gecko extensions, dedicated 2FA and password-manager modules. Zero VirusTotal detections across 71 engines on the 2026-05-30 initial upload per BlackFog. DLL sideloading via NVIDIA-library masquerade + in-memory execution + legitimate-signature wrapper. Two publisher-independent relays, single BlackFog evidence basis. No actor attribution. **Digraph: B2 · WEP: likely**.

**Europol dismantles AudiA6 crypto-laundering service — >$380M laundered.** [BleepingComputer relays](https://www.bleepingcomputer.com/news/security/europol-dismantles-audia6-crypto-laundering-service-380m/) the 11-country Europol operation: 2 administrators charged (Ruslan Igorevich Tkachuk, 37, Ukrainian; Alexander Vladimirovich Ledenev, 25, Russian) detained in Georgia; 25 domains + €86k crypto seized + €692k frozen + Telegram blocked. Linked to 15+ international ransomware investigations (no groups named). Indirect ransomware-economy disruption; no A&D-prime named. **Digraph: B2 · WEP: likely**.

**Nightmare Eclipse claims GreatXML BitLocker bypass — reproduction contested by Will Dormann.** [The Register](https://www.theregister.com/2026/06/11/nightmare_eclipse_greatxml_bitlocker/) and The Hacker News relay the researcher's eighth zero-day disclosure: claimed BitLocker bypass via Recovery-partition `unattend.xml` + WinRE shell access. No CVE, no patch, no A-grade ITW. Independent researcher Will Dormann reports he cannot reproduce — preconditions (logged-in admin must have initiated Defender Offline Scan previously) negate the bypass per Dormann critique. Microsoft confirmed investigating sibling RoguePlanet; no comment yet on GreatXML; researcher's GitHub account banned. CMMC L2/L3 BitLocker-as-FDE-integrity awareness signal only. **Digraph: B3 · WEP: roughly even chance** on mechanism validity.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:GREEN — public open-source reporting; structural-indirect A&D relevance; charged subjects named per LEGAL-POLICY data-handling table.*

**FLASH supersession status:** [2026-06-11 12:00 FLASH](./2026-06-11-flash-1200.md) on Oracle PeopleSoft is materially extended (NOT superseded) by this brief — mitigations-only firmed at A1, ZDI "limited" introduces independent scale tension. The [06:08 Ivanti FLASH](./2026-06-11-flash-0608-ivanti-sentry-cve-2026-10520.md) was fully superseded by the morning brief; this afternoon's KEV/BOD UPDATE stacks on the morning, not on the FLASH.

**Watch items:** (1) Second-scanner corroboration of Shadowserver 19/2 (GreyNoise, Censys); (2) Second IR-firm corroboration of Mandiant on PeopleSoft (Unit 42, CrowdStrike, MSTIC, Volexity); (3) Oracle GA patch state transition out of mitigations-only; (4) Independent attestation on Langflow ITW beyond VulnCheck; (5) Direct DOJ filing retrieval on Obrezko for /new-actor Void Blizzard decision; (6) Microsoft formal GreatXML position or Dormann follow-up.

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-11.

🚨 **Active Threats**

• **[CISA adds Ivanti Sentry CVE-2026-10520 to KEV; FCEB deadline Sunday June 14; BOD 26-04 issued](https://www.bleepingcomputer.com/news/security/cisa-orders-federal-agencies-to-patch-ivanti-sentry-vulnerability-in-three-days/)** — Federal *procedural* attestation; KEV publishes no telemetry, so the morning's "mass" hedge holds. BOD 26-04's 3-day clock is **FCEB-only** — *aspirational for DIB*. **Patch Sentry to R10.5.2 / R10.6.2 / R10.7.1 today.**

• **[Oracle PeopleSoft CVE-2026-35273 — mitigations-only firmed; ZDI calls exploitation "limited"](https://www.theregister.com/2026/06/11/oracle_peoplesoft_zero_day_shinyhunters/)** — Three-publisher convergence anchors no-GA-patch; ZDI's Childs is independent of Mandiant and tensions ShinyHunters' 100-org self-claim. HIBP found ~455k Nottingham emails. *Apply Oracle's mitigations now*; hunt the 7 corpus IOCs.

🔓 **Vulnerabilities**

• **[Langflow CVE-2026-5027 (CVSS 8.8) path-traversal RCE — in-the-wild per VulnCheck](https://www.securityweek.com/langflow-path-traversal-vulnerability-exploited-in-the-wild/)** — First confirmed-ITW AI-workflow-platform compromise in the corpus; ~7,000 internet-exposed instances, mostly North America. Patch out since March. **Audit internal Langflow; disable auto-login default.**

🕵️ **Actor Activity**

• **[DOJ indicts Russian national Denis Obrezko for Void Blizzard infrastructure role](https://therecord.media/russian-national-denis-obrezko-void-blizzard-indictment-thailand-extradition)** — Arrested November 2025 in Phuket; Boston court June 10. The Record names "defense contractors" in the sector taxonomy; 11 U.S. companies unenumerated. Void Blizzard *not in roster* — /new-actor deferred pending DOJ filing. (Layer 1 covers The Gentlemen / Storm-2697 PRODAFT corroboration.)
