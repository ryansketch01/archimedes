---
raw_id: raw-2026-05-18-pm-001
collected_at: 2026-05-18T15:32:00-04:00
run_id: pre-brief-20260518-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/leaked-shai-hulud-malware-fuels-new-npm-infostealer-campaign/
  published_at: 2026-05-18T13:28:02-04:00
  author: Bill Toulas
match_reason:
  watchlist: []
  actors: [TeamPCP]
  vulnerabilities: []
  keywords: [Shai-Hulud, npm, supply-chain, Mini Shai-Hulud, VT-006, OxSecurity]
triage_tags: [vt_006_carry_forward, supply_chain, teampcp_lineage_refinement, net_new_iocs, anti_noise_partial_already_morning_brief_b812307]
iocs_extracted: true
iocs_count: 5
text_word_count: 380
promoted: true
promoted_to_finding: finding-2026-05-18-0003
promoted_at: 2026-05-18T16:08:00-04:00
ttl_expires_at: 2026-08-16T15:32:00-04:00
---

# Leaked Shai-Hulud malware fuels new npm infostealer campaign

BleepingComputer (Bill Toulas), 2026-05-18 13:28 EDT.

The Shai-Hulud malware that was leaked last week is now being used in new attacks against the npm (Node Package Manager) index, with infected packages emerging over the weekend. Originating Shai-Hulud campaign attributed to TeamPCP. The cloned variants were uploaded by a separate actor — npm account "deadcode09284814" — distinct from TeamPCP. Researcher attribution language preserved verbatim: "One incriminating evidence that this is a different actor from TeamPCP, is that the Shai-Hulud malware code is an almost exact copy of the leaked source code, with no obfuscation techniques."

Originating leak message reproduced as cited by BleepingComputer: "Here We Go Again - Let the Carnage Continue. A Gift from TeamPCP" (associated with the September 2025 originating campaign).

Four malicious npm packages identified by OxSecurity:
- chalk-tempalte (Shai-Hulud clone)
- @deadcode09284814/axios-util
- axois-utils (includes DDoS capability)
- color-style-utils

C2 indicator (raw, defanged): 87e0bbc636999[.]lhr[.]life

Victim sector: developers / development infrastructure. No named victim organizations specified in source.

Timeline: campaign inception September 2025 (TeamPCP originating campaign); current clone discovery weekend prior to 2026-05-18 publication.

Source firms cited: OxSecurity (research / discovery / analysis publication).

---

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas
- Article type: news (vendor-relay primary)
- Raw IOC extraction invoked: yes (manual extraction; ioc-extraction skill output below)
- Net-new IOC layer vs. morning brief b812307 mention-class: YES (morning brief carried Shai-Hulud clone mention-class without IOC list; this surface adds C2 domain + 4 npm package names + clone-publisher npm account name).
- Hard Rule 2 preservation: OxSecurity attribution discipline preserved — clone publisher "deadcode09284814" is described as UNATTRIBUTED and explicitly distinct from TeamPCP. Archimedes does NOT propagate TeamPCP attribution to clone publisher.
- Hard Rule 3: GitHub repo descriptor "A Mini Sha1-Hulud has Appeared" mentioned in earlier 06:00 FLASH a8121bc Item #2 cluster (THN/Ox Security 05:45 EDT) NOT linked here; no PoC URL reproduced.
- Anti-noise: same cluster as morning brief b812307 Other Signal mention; this surface materially refines with IOC list — flagged for grader as VT-006 carry-forward IOC-augmentation refinement.

## IOCs (extracted manually — ioc-extraction skill output)

```yaml
iocs:
  - type: domain
    value: 87e0bbc636999.lhr.life
    defanged: "87e0bbc636999[.]lhr[.]life"
    role: c2
    confidence_source: OxSecurity via BleepingComputer
    first_seen: 2026-05-17  # weekend prior to 2026-05-18 publication
    notes: "C2 infrastructure for cloned Shai-Hulud variants distributed via 4 npm packages."

  - type: package_name
    value: chalk-tempalte
    ecosystem: npm
    role: malicious_package
    confidence_source: OxSecurity via BleepingComputer
    notes: "Shai-Hulud clone — direct copy of leaked source code, no obfuscation."

  - type: package_name
    value: "@deadcode09284814/axios-util"
    ecosystem: npm
    role: malicious_package
    confidence_source: OxSecurity via BleepingComputer

  - type: package_name
    value: axois-utils
    ecosystem: npm
    role: malicious_package
    confidence_source: OxSecurity via BleepingComputer
    notes: "Adds DDoS capability beyond Shai-Hulud clone baseline (per BleepingComputer summary; cross-corroboration with prior 06:00 FLASH a8121bc Item #2 THN/Ox 05:45 EDT cluster — same Phantom Bot Golang DDoS class as axois-utils per OxSecurity research preserved attribution as UNATTRIBUTED clone-publisher distinct from TeamPCP)."

  - type: package_name
    value: color-style-utils
    ecosystem: npm
    role: malicious_package
    confidence_source: OxSecurity via BleepingComputer

  - type: npm_account
    value: deadcode09284814
    role: clone_publisher
    confidence_source: OxSecurity via BleepingComputer
    attribution: UNATTRIBUTED
    notes: "Per OxSecurity attribution discipline: 'a different actor from TeamPCP' — clone publisher distinct from TeamPCP originating actor. Hard Rule 2 preservation: Archimedes does NOT propagate TeamPCP attribution to clone publisher. Same UNATTRIBUTED treatment as 06:00 FLASH a8121bc Item #2."

attribution_claims:
  - claim: "Cloned Shai-Hulud variants uploaded by separate actor 'deadcode09284814' distinct from TeamPCP."
    claimed_by: OxSecurity via BleepingComputer
    confidence_language: "One incriminating evidence that this is a different actor"
    actor_named: UNATTRIBUTED (clone-publisher npm account "deadcode09284814")
    actor_in_roster: false
    archimedes_position: "Preserve verbatim. Do NOT propagate TeamPCP attribution to clone publisher. Hard Rule 2 binding."

  - claim: "Original Shai-Hulud campaign attributed to TeamPCP (#001 HIGH in _roster.yaml); inception September 2025."
    claimed_by: BleepingComputer (carry-forward)
    actor_named: TeamPCP
    actor_in_roster: true
    archimedes_position: "Carry-forward from prior corpus surfaces. No net-new attribution claim here."
```
