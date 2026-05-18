---
brief_id: 2026-05-18-afternoon
brief_type: afternoon
status: published
published_at: 2026-05-18T16:00:47-04:00
discord_message_id: "1506030879519281173"
discord_channel: intel-briefs
discord_post_status: 200
authored_by: archimedes-briefer
grader_approval: archimedes-grader
analyst_review: complete (finding-2026-05-18-0003 ACH H1 distinct-actor tied with H3 copy-cat-noise at zero inconsistencies, gather-more-evidence per Heuer; cluster anchor preserved at likely. finding-2026-05-18-0004 ACH decisively rejects H2 Scattered-Spider-relabeling on 5 inconsistencies; Hard Rule 2 non-propagation analytically confirmed; KAC 8 assumptions with 3 sound / 5 qualify / 0 test / 0 reject; cluster anchor preserved at likely on procedural-facts; threat-actor-cluster sub-layers each carry single-source veto.)
red_team_review: not_required (neither new finding crossed WEP "very likely" — both anchor at "likely" with single-source veto applied to multiple sub-layers; Scattered Spider non-propagation is binding-constraint discipline not confidence question)
human_override: null
word_count: 752
findings_referenced:
  - finding-2026-05-18-0003
  - finding-2026-05-18-0004
  - finding-2026-05-18-0001
  - finding-2026-05-18-0002
  - finding-2026-05-17-0001
  - finding-2026-05-14-0005
  - finding-2026-05-15-0003
  - finding-2026-05-16-0001
  - finding-2026-05-16-0002
  - finding-2026-05-16-0003
related_actors_referenced:
  - actor_name: "CoinbaseCartel"
    on_roster: false
    archimedes_treatment: reported_not_asserted_per_bleepingcomputer_per_the_record_per_actor_own_dls_self_claim
    new_actor_candidate: true
    proposed_conservative_threat_level: MEDIUM
  - actor_name: "ShinyHunters"
    on_roster: false
    archimedes_treatment: ecosystem_affiliate_framing_per_bleepingcomputer_WITH_actor_self_denial_preserved_verbatim
    new_actor_candidate: true
    proposed_conservative_threat_level: MEDIUM
  - actor_name: "Lapsus$"
    on_roster: false
    archimedes_treatment: ecosystem_affiliate_framing_per_bleepingcomputer
  - actor_name: "Scattered Lapsus$ Hunters (SLSH)"
    on_roster: false
    archimedes_treatment: parent_collective_framing_per_the_record_DISTINCT_from_scattered_spider_despite_name_overlap
    new_actor_candidate: deferred_to_analyst
  - actor_name: "Scattered Spider"
    on_roster: true
    roster_id: "013"
    threat_level: HIGH
    archimedes_treatment: NOT_ATTRIBUTED_TO_GRAFANA_OR_COINBASECARTEL_BY_ANY_DIRECTLY_RETRIEVED_SOURCE_THIS_SWEEP_per_hard_rule_2_LEGAL_POLICY_no_attribution_laundering_binding_constraint
  - actor_name: "TeamPCP"
    on_roster: true
    roster_id: "001"
    threat_level: HIGH
    archimedes_treatment: ORIGINATING_CAMPAIGN_LINEAGE_ONLY_NOT_PROPAGATED_TO_CLONE_PUBLISHER_per_hard_rule_2
  - actor_name: "deadcode09284814 (npm clone publisher)"
    on_roster: false
    archimedes_treatment: UNATTRIBUTED_per_ox_security_via_bleepingcomputer
related_vulns_referenced:
  - cve: CVE-2026-20182
    cvss: 10.0
    kev_due_date: 2026-05-17
    status: kev_federal_deadline_lapsed_t_plus_16h_no_fresh_a_grade_corroboration
  - cve: CVE-2026-42897
    cvss: 8.1
    kev_due_date: 2026-05-29
    status: kev_t_minus_11_single_source_veto_holds_72h_plus
  - cve: CVE-2026-42945
    cvss_v4: 9.2
    status: vulncheck_canaries_dual_relay_b_grade_defensive_telemetry_holding
  - cve: CVE-2020-17103
    cvss: 7.0
    status: poc_published_researcher_chaotic_eclipse_msrc_unresponsive_substantive_layer_at_roughly_even_chance_pending_test
  - cve: CVE-2026-44112
    cvss: 9.6
    status: cyera_originating_openclaw_claw_chain_patched_april_23_pre_disclosure_no_exploitation_status_update_candidate_for_vuln_tracker
hard_rule_2_framings_load_bearing:
  - "Scattered Spider (#013 HIGH) NOT attributed to Grafana or CoinbaseCartel by any directly retrieved source this sweep — LEGAL-POLICY no-attribution-laundering binding constraint analytically confirmed via ACH"
  - "BleepingComputer narrower framing (CoinbaseCartel consists of ShinyHunters + Lapsus$) preserved verbatim; ShinyHunters self-denial preserved verbatim"
  - "The Record SLSH parent-collective framing preserved verbatim, distinct from Scattered Spider despite name overlap"
  - "shinysp1d3r tool-attribution via Joe Shenouda relay-of-unnamed-researchers chain NOT propagated as Archimedes-attested IOC"
  - "Shai-Hulud clones attributed to UNATTRIBUTED clone-publisher per Ox Security via BleepingComputer — NOT propagated to TeamPCP"
  - "Grafana scope-bounding (no customer/personal data) preserved per vendor self-disclosure"
hard_rule_3_compliance:
  poc_url_in_brief_body: false
  protected_urls:
    - Nightmare-Eclipse/MiniPlasma_repo
    - depthfirst_CVE-2026-42945_repo
    - V12_security_CVE-2026-31635_repo
    - Ox_Security_npm_clone_GitHub_repos
hard_rule_6_quote_discipline:
  quotes_in_brief: 0
hard_rule_8_first_party_splunk:
  status: clean_at_compose
  hits: 0
  consecutive_dormant_sweep_count: 44
  framing: silence_is_not_disconfirming
tlp: CLEAR
---

# Afternoon Brief — 2026-05-18

**[Grafana confirms a stolen GitHub token enabled codebase theft](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-source-code/); CoinbaseCartel claimed credit via its leak site and Grafana refused to pay per FBI guidance.** Per [BleepingComputer](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-source-code/) (Bill Toulas, 09:46 EDT) and [The Record](https://therecord.media/grafana-coinbasecartel-extortion-refused) (13:50 EDT), no customer data or personal information was accessed and customer systems remained unaffected. Separately, Ox Security identifies the first npm clone wave of the leaked Shai-Hulud worm framework — four malicious packages by an UNATTRIBUTED publisher distinct from TeamPCP — materializing the VT-006 derivative-attacks prediction at T+3 days.

**Why it matters:** Scattered Spider (#013, HIGH) is **not** attributed to Grafana or CoinbaseCartel by either source directly retrieved this sweep. BleepingComputer narrows the cluster relative to yesterday's SecurityWeek broader framing; The Record introduces SLSH as a parent collective distinct from Scattered Spider despite name overlap. Per Hard Rule 2 + LEGAL-POLICY no-attribution-laundering, Archimedes does **not** propagate Scattered Spider attribution into this cluster.

---

## 🚨 Active Threats

**Grafana codebase theft confirmed; CoinbaseCartel claimed credit via its leak site; ransom refused.** Per [BleepingComputer](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-source-code/) + [The Record](https://therecord.media/grafana-coinbasecartel-extortion-refused), a stolen GitHub access token enabled the source-code download; Grafana scopes the impact to code only. BleepingComputer frames CoinbaseCartel as ShinyHunters + Lapsus$ affiliates and preserves a ShinyHunters self-denial; The Record frames CoinbaseCartel as a data-theft offshoot of SLSH, distinct from Scattered Spider despite the name overlap. Joe Shenouda via BleepingComputer references an in-memory ESXi encryptor `shinysp1d3r` — relay-of-named-individual, **not** an Archimedes-attested IOC, **not** added to defenseclaw_local watchlists. **B2** · WEP **likely** on procedural facts; cluster sub-layers capped at **likely** (or **roughly even chance** on `shinysp1d3r`) by single-source veto. 🔗 **Update on:** [2026-05-18 morning brief](2026-05-18-morning.md) — extends finding-2026-05-17-0001 base cluster.

---

## 🔓 Vulnerabilities

- **CVE-2026-20182 (Cisco Catalyst SD-WAN, CVSS 10.0) — federal KEV deadline lapsed Sunday end-of-day; T+16h post-mortem.** Carry-forward. No fresh A-grade reporting. UAT-8616 per [Cisco Talos](https://blog.talosintelligence.com/) carries forward with visibility-skew caveat. **A2**.
- **CVE-2026-42897 (Exchange OWA XSS) — [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) deadline Friday May 29 (T-11).** Carry-forward. >72h single-source veto holds; MSRC remains sole originating attester. **A1** on CVE record; exploitation claim capped at **likely**.
- **CVE-2026-42945 (NGINX Rift) — VulnCheck Canaries scanner probes via SecurityWeek + The Hacker News; defensive telemetry, not A-grade production exploitation.** Carry-forward. F5 K000160932 patches predate observation. **B2** · WEP **likely**.
- **CVE-2020-17103 (MiniPlasma / Windows Cloud Filter LPE) — researcher PoC effectiveness at roughly even chance pending MSRC or A-grade reproduction.** Carry-forward. Repo not linked per Hard Rule 3. **B2**.

---

## ✈️ Sector Focus: Aerospace & Defense

No A&D-prime named-victim disclosures this window. Grafana reaches A&D defensively via deployment in prime engineering and DoD-agency / MSSP estates (analyst inference, **not** source-attested); CVE-2026-20182 reaches A&D directly via Catalyst SD-WAN in DIB / CMMC partner-flow estates. [Symantec Fast16](https://www.security.com/threat-intelligence/fast16-nuclear-sabotage) provisional-A clock T+43h+ past elapsed; awaiting operator pass — Fast16 is pre-Stuxnet historical, **not** a current campaign. Tracked A&D actors ([APT28](../threat-actors/APT28/profile.md), [UNC1549](../threat-actors/UNC1549/profile.md), Lazarus, APT41, Salt Typhoon): no new direct activity.

---

## 🕵️ Actor Activity

**CoinbaseCartel, ShinyHunters, and SLSH each flagged as `/new-actor` candidates at conservative MEDIUM.** Per evidence-minimum-table, MEDIUM **not** HIGH absent A-grade vendor research (Mandiant / CrowdStrike / Unit 42 / MSTIC / Volexity / Bitdefender / ESET / Symantec / Talos). Scaffolding decisions deferred to analyst `/new-actor` workflow. The ShinyHunters self-denial of CoinbaseCartel linkage is preserved verbatim as actor self-signaling — Archimedes does **not** collapse it. [TeamPCP](../threat-actors/TeamPCP/profile.md) (#001 / HIGH) leak deadline Thursday May 21 (T-3) remains the next actor tripwire.

---

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors ([UNC1549](../threat-actors/UNC1549/profile.md), [Charming Kitten](../threat-actors/Charming-Kitten/profile.md), Handala Hack, [MuddyWater](../threat-actors/MuddyWater/profile.md)) in the last 48h. DarkReading Iran ATG fuel-tank surface this window is multi-step relay-of-unnamed-officials with no specific tracked Iranian APT named; fuel-storage is **not** A&D. No FLASH trigger.

---

## 📰 Other Signal

- **First Shai-Hulud npm clone wave — 4 packages by UNATTRIBUTED publisher per Ox Security via [BleepingComputer](https://www.bleepingcomputer.com/news/security/leaked-shai-hulud-malware-fuels-new-npm-infostealer-campaign/) (Bill Toulas, 13:28 EDT).** `chalk-tempalte` / `@deadcode09284814/axios-util` / `axois-utils` (adds DDoS) / `color-style-utils`; C2 `87e0bbc636999[.]lhr[.]life` on a public LocalHost.run anonymizer subdomain (uninformative for actor-distinction per analyst KAC). Materializes the VT-006 derivative-attacks-30d WEP at T+3 days; clones are **not** TeamPCP-attributed. ACH H1 (distinct actor) tied with H3 (copy-cat noise). Add four package names to dependency-quarantine. **B2** · WEP **likely**. 🔗 **Update on:** [2026-05-18 morning brief](2026-05-18-morning.md).
- **OpenClaw "Claw Chain" — CVE-2026-44112 (CVSS 9.6) + three sandbox-escape CVEs patched April 23.** Cyera-originating; no exploitation; no A&D-prime adoption visibility. Vuln-tracker `/index.yaml` candidate. **C3**.
- **Healthcare data-breach aggregate ~5.4M records across six US providers per [SecurityWeek](https://www.securityweek.com/) (Eduard Kovacs, 08:58 EDT).** No claimed-by attribution per source; healthcare is **not** A&D. Mention-class. **B3**.
- **INTERPOL Operation Ramz MENA cybercrime takedown** — LE-disruption commodity cybercrime; geographic adjacency to Iran is **not** attribution basis. Mention-class. **B2**.
- **Pwn2Own Berlin 2026 final wrap** — $1.298M / 47 zero-days; Orange Tsai's Exchange RCE-to-SYSTEM chain under ZDI 90-day embargo through ~2026-08-13. Carry-forward. **A2**.

---

*TLP:CLEAR. 44th consecutive dormant non-self-telemetry Splunk sweep — silence is not disconfirming per Hard Rule 8.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-05-18.

🚨 **Active Threats**

- **[Grafana confirms stolen GitHub token enabled codebase theft; CoinbaseCartel takes credit, ransom refused](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-source-code/)** — BleepingComputer and The Record (both Monday May 18) relay Grafana's disclosure: source code only, no customer data, no impact to customer systems. BleepingComputer frames CoinbaseCartel as ShinyHunters + Lapsus$ affiliates and reports a ShinyHunters self-denial; The Record frames CoinbaseCartel as a data-theft offshoot of the SLSH collective (distinct from Scattered Spider despite name overlap). *Archimedes does not propagate Scattered Spider (#013 HIGH) attribution into this cluster — neither source names it.* A `shinysp1d3r` ESXi tool is relayed via a named analyst but *not* added as an Archimedes IOC.

🔓 **Vulnerabilities**

- **CVE-2026-20182 (Cisco SD-WAN):** federal KEV deadline lapsed Sunday end-of-day; T+16h, still no fresh A-grade reporting.
- **CVE-2026-42897 (Exchange OWA XSS):** KEV *Friday May 29 — T-11*. >72h single-source veto holds.
- **CVE-2026-42945 (NGINX Rift):** VulnCheck Canaries scanner probes — defensive telemetry, *not* production exploitation.

🕵️ **Actor Activity**

- **CoinbaseCartel, ShinyHunters, SLSH** — `/new-actor` candidates at conservative MEDIUM; *not proposed today*. TeamPCP leak *Thursday May 21 — T-3*.

📰 **Other Signal**

- **[First Shai-Hulud npm clone wave — 4 packages by UNATTRIBUTED publisher](https://www.bleepingcomputer.com/news/security/leaked-shai-hulud-malware-fuels-new-npm-infostealer-campaign/)** — Per Ox Security via BleepingComputer (Monday May 18): `chalk-tempalte`, `@deadcode09284814/axios-util`, `axois-utils` (adds DDoS), `color-style-utils`; C2 on a LocalHost.run anonymizer subdomain. Clones are *not* TeamPCP. **Add the four package names to dependency-quarantine** *now*.
- **OpenClaw "Claw Chain":** four CVEs incl. CVSS 9.6 patched April 23 — no exploitation.
