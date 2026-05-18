---
raw_id: raw-2026-05-18-pm-002
collected_at: 2026-05-18T15:35:00-04:00
run_id: pre-brief-20260518-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/
  published_at: 2026-05-18T09:46:26-04:00
  author: Bill Toulas
match_reason:
  watchlist: []
  actors: [Scattered Spider]  # cluster-adjacent (ShinyHunters / Lapsus$ affiliates per source; Scattered Spider NOT named by this source)
  vulnerabilities: []
  keywords: [CoinbaseCartel, ShinyHunters, Lapsus$, Grafana, GitHub-token, shinysp1d3r, ESXi, VMware]
triage_tags: [grafana_cluster_refinement, shinyhunters_new_actor_candidate, coinbasecartel_new_actor_candidate, scattered_spider_cluster_adjacent, anti_noise_partial_already_06_00_flash_a8121bc_and_12_00_flash_ac3683d]
iocs_extracted: true
iocs_count: 1
text_word_count: 460
promoted: true
promoted_to_finding: finding-2026-05-18-0004
promoted_at: 2026-05-18T16:14:00-04:00
ttl_expires_at: 2026-08-16T15:35:00-04:00
---

# Grafana says stolen GitHub token let hackers steal codebase

BleepingComputer (Bill Toulas), 2026-05-18 09:46 EDT.

Grafana Labs disclosed that hackers have downloaded its source code after breaching its GitHub environment using a stolen access token. CoinbaseCartel has claimed the attack by adding Grafana to their data leak site (DLS) ("100+ victims" announced on extortion portal).

Verbatim source language preserved for attribution cluster framing: "CoinbaseCartel consists of ShinyHunters and Lapsus$ affiliates that gain access to target networks via social engineering, various forms of phishing, and compromised credentials." Verbatim caveat preserved: "ShinyHunters extortion gang told BleepingComputer that the CoinbaseCartel is not linked to their group."

Researcher attribution claim preserved: Joe Shenouda (Threat Intelligence Specialist) claims CoinbaseCartel deploys "shinysp1d3r" tool — an in-memory encryption tool targeting VMware ESXi that disables snapshots. Planned Linux and ESXi encryptor versions referenced as in-development. BleepingComputer analyzed the prior Windows version of ShinySp1d3r encryptor in a prior year.

Note on attribution-laundering hedge per Hard Rule 2: BleepingComputer's CoinbaseCartel framing in this article DROPS Scattered Spider — unlike the prior SecurityWeek 06:00 FLASH a8121bc Item #3 framing which said "Coinbase Cartel linked to ShinyHunters, Scattered Spider, and Lapsus, whose members have been collaborating since at least mid-2025." This narrower BleepingComputer framing is to be treated as narrower-source-preferred per Hard Rule 2 — Scattered Spider (#013 HIGH in _roster.yaml) is NOT attributed to Grafana by this source. The relay-of-unnamed-researchers attribution chain on "shinysp1d3r" (Joe Shenouda is named, but he relays the tool-attribution claim) — Archimedes does NOT propagate as Archimedes-attested IOC; Hard Rule 2 binding constraint.

Grafana victim self-disclosure (procedurally A-class on own incident per OpenAI/TanStack 2026-05-14 precedent): scope bounded by Grafana own statement: "no evidence that customer data or personal information was exposed"; "customer systems remained unaffected." Source code downloaded from GitHub environment.

Timeline: Grafana announcement made weekend prior to 2026-05-18 publication. CoinbaseCartel emerged ~September 2025 per source.

Source firms / researchers cited: Joe Shenouda (Threat Intelligence Specialist, named); BleepingComputer (article author + prior ShinySp1d3r encryptor analysis); multiple unnamed researchers cited generally for CoinbaseCartel-ShinyHunters/Lapsus$ affiliate framing.

No file hashes, IPs, or non-tool-name IOCs published in source.

---

## Extraction notes

- Language: en
- Publisher byline: Bill Toulas
- Article type: news (Grafana self-disclosure + threat-actor-cluster framing)
- Raw IOC extraction invoked: yes
- Net-new vs. 06:00 FLASH a8121bc Item #3 (SecurityWeek Eduard Kovacs 04:34 EDT): YES — adds Joe Shenouda named-analyst byline; adds "shinysp1d3r" in-memory ESXi tool relay; NARROWS attribution-cluster framing (drops Scattered Spider relative to SecurityWeek 06:00 framing).
- Hard Rule 2 preservation: Multiple layers preserved verbatim — (a) BleepingComputer "CoinbaseCartel consists of ShinyHunters and Lapsus$ affiliates" framing; (b) ShinyHunters self-denial "not linked to their group"; (c) "shinysp1d3r" tool attribution via Joe Shenouda relay-of-unnamed-researchers chain NOT propagated as Archimedes-attested IOC; (d) Scattered Spider non-propagation per BleepingComputer narrower framing (Hard Rule 2 narrower-source-preferred).
- /new-actor candidacy flags surfaced by 12:00 FLASH ac3683d preserved: ShinyHunters at conservative MEDIUM; CoinbaseCartel at conservative MEDIUM — both pending A-grade vendor (Mandiant / CrowdStrike / Unit 42 / MSTIC / Volexity / Bitdefender / ESET / Symantec / Talos) corroboration.
- Cluster-anchor refinement candidate for grader 16:00 afternoon brief evaluation.

## IOCs (extracted manually — ioc-extraction skill output)

```yaml
iocs:
  - type: tool_name
    value: shinysp1d3r
    role: in_memory_encryptor
    target: VMware ESXi (current variant per source)
    capability: "disables snapshots; planned Linux and ESXi encryptor versions per source"
    confidence_source: Joe Shenouda via BleepingComputer
    attribution_chain: relay_of_unnamed_researchers
    archimedes_position: "Per Hard Rule 2 NOT propagated as Archimedes-attested IOC."

attribution_claims:
  - claim: "CoinbaseCartel responsible for Grafana codebase theft."
    claimed_by: CoinbaseCartel (self-claim on own DLS) + Grafana incident disclosure
    confidence_language: "claimed the attack by adding Grafana to their data leak site"
    actor_named: CoinbaseCartel
    actor_in_roster: false
    archimedes_position: "Actor self-claim on own infrastructure is factual record of signaling, NOT independently verified. /new-actor candidate at conservative MEDIUM."

  - claim: "CoinbaseCartel consists of ShinyHunters and Lapsus$ affiliates."
    claimed_by: BleepingComputer (multiple unnamed researchers)
    confidence_language: "consists of ... affiliates"
    actor_named: ShinyHunters, Lapsus$
    actors_in_roster: false (Lapsus$), false (ShinyHunters — /new-actor candidate from finding-2026-05-18-0002)
    archimedes_position: "Preserve verbatim. ShinyHunters self-denial 'not linked' also preserved verbatim. Hard Rule 2 binding."

  - claim: "shinysp1d3r in-memory tool targets VMware ESXi; CoinbaseCartel deploys it."
    claimed_by: Joe Shenouda via BleepingComputer
    actor_named: CoinbaseCartel
    actor_in_roster: false
    archimedes_position: "Relay-of-unnamed-researchers attribution chain. Hard Rule 2 prevents propagation as Archimedes-attested IOC. Preserved as fact-of-source-coverage."

  - claim: "Scattered Spider attributed to Grafana / CoinbaseCartel cluster."
    claimed_by: NOT_CLAIMED_BY_THIS_SOURCE
    note: "BleepingComputer narrower framing DROPS Scattered Spider relative to prior SecurityWeek 06:00 FLASH a8121bc framing. Hard Rule 2 narrower-source-preferred — Archimedes does NOT propagate Scattered Spider attribution to Grafana incident."

scope_bounded:
  source: Grafana Labs victim self-disclosure
  affected: source code downloaded from GitHub
  unaffected: customer data, personal information, customer systems, production
  procedural_grade: A (vendor self-disclosure on own incident; same precedent class as OpenAI TanStack finding-2026-05-14-0008)
```
