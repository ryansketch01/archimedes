---
raw_id: raw-2026-05-18-pm-003
collected_at: 2026-05-18T15:38:00-04:00
run_id: pre-brief-20260518-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: the-record
  source_name: The Record from Recorded Future News
  source_url: https://therecord.media/grafana-refuses-to-pay-ransom-codebase-theft
  published_at: 2026-05-18T13:50:00-04:00
  author: null
match_reason:
  watchlist: []
  actors: []  # CoinbaseCartel / ShinyHunters / Scattered Lapsus$ Hunters NOT in _roster.yaml
  vulnerabilities: []
  keywords: [CoinbaseCartel, Scattered Lapsus$ Hunters, SLSH, Grafana, ransom-refusal, FBI-guidance]
triage_tags: [grafana_cluster_refinement, slsh_collective_framing_introduced, ransom_refusal_class, anti_noise_partial_already_06_00_flash_a8121bc_and_12_00_flash_ac3683d, third_relay_of_grafana_cluster]
iocs_extracted: false
iocs_count: 0
text_word_count: 280
promoted: true
promoted_to_finding: finding-2026-05-18-0004
promoted_at: 2026-05-18T16:14:00-04:00
ttl_expires_at: 2026-08-16T15:38:00-04:00
---

# Grafana refuses to pay ransom after codebase theft

The Record from Recorded Future News, 2026-05-18 13:50 EDT (no byline).

Grafana Labs has refused to pay ransom following the CoinbaseCartel codebase theft disclosed over the weekend. Verbatim source language preserved on cluster framing: CoinbaseCartel "emerged last year as a data theft offshoot of the larger Scattered Lapsus$ Hunters (SLSH) cybercriminal collective."

Verbatim Grafana refusal statement preserved: "We've determined the appropriate path forward is to not pay the ransom. As part of Grafana Labs' standard security practices, we will share additional information..."

Reasoning per The Record: Grafana based refusal on "longstanding FBI guidance that paying cybercriminals does not guarantee anything."

Scope (Grafana victim self-disclosure):
- Source code downloaded via compromised GitHub token
- "No customer data or personal information was accessed"
- "No evidence of impact to customer systems or operations"

Ransom demand amount: undisclosed in source.

Timeline:
- Friday (2026-05-15): CoinbaseCartel claimed theft
- Saturday night (2026-05-16): Grafana's public statement
- Article published: 2026-05-18 13:50 EDT (3rd relay layer of Grafana cluster)

CoinbaseCartel scope claim per source: "has attempted to extort more than 100 companies" (temporal qualifier "attempted" indicates ongoing activity rather than confirmed successes — preserved verbatim).

Source firms / authorities cited: Halcyon (cybersecurity experts), Recorded Future (publisher), FBI (guidance referenced).

No IOCs (domains, IPs, hashes, GitHub indicators) provided in source.

---

## Extraction notes

- Language: en
- Publisher byline: not specified
- Article type: news (third relay layer of Grafana cluster after 06:00 FLASH a8121bc SecurityWeek 04:34 EDT + pm-002 BleepingComputer 09:46 EDT)
- Raw IOC extraction invoked: not applicable (no IOCs in source body)
- Net-new vs. prior relays: introduces NEW framing "Scattered Lapsus$ Hunters (SLSH) cybercriminal collective" as parent-ecosystem-lineage of CoinbaseCartel; adds Grafana ransom-refusal procedural fact and FBI-guidance reasoning; adds Halcyon named source.
- Hard Rule 2 preservation: SLSH "cybercriminal collective" framing preserved verbatim; CoinbaseCartel "data theft offshoot of the larger SLSH" preserved verbatim. Per Hard Rule 2 + LEGAL-POLICY no-attribution-laundering, Archimedes does NOT propagate SLSH parent-collective framing to Grafana as Archimedes-originated attribution — the relay chain is The Record → Recorded Future ecosystem (Recorded Future-as-publisher) — but the underlying SLSH-as-parent-collective claim is preserved-as-source-said.
- Scattered Spider non-propagation: SLSH naming contains "Scattered" but is a distinct collective framing — Scattered Spider (#013 HIGH _roster.yaml) is NOT the same as "Scattered Lapsus$ Hunters." Hard Rule 2 prevents conflation. The Record does NOT name Scattered Spider in this article.
- Anti-noise: Same cluster as 06:00 FLASH a8121bc Item #3 + pm-002. This is a THIRD relay layer with material refinement (ransom-refusal procedural fact + SLSH parent-collective framing). Flagged for grader as cluster-anchor refinement candidate.

## IOCs

```yaml
iocs: []  # No file-level / network-level IOCs published in source body.

attribution_claims:
  - claim: "CoinbaseCartel is a data theft offshoot of Scattered Lapsus$ Hunters (SLSH) cybercriminal collective."
    claimed_by: The Record from Recorded Future News
    confidence_language: "emerged last year as a data theft offshoot of the larger"
    actor_named: CoinbaseCartel, Scattered Lapsus$ Hunters (SLSH)
    actors_in_roster: false (both)
    archimedes_position: "Preserve verbatim. Per Hard Rule 2 + LEGAL-POLICY no-attribution-laundering, the SLSH parent-collective framing is NOT propagated to Grafana as Archimedes-originated attribution. Distinct from Scattered Spider (#013) — name overlap on 'Scattered' is not basis for cluster conflation."

  - claim: "CoinbaseCartel has attempted to extort more than 100 companies."
    claimed_by: The Record (citing CoinbaseCartel DLS / extortion portal)
    actor_named: CoinbaseCartel
    actor_in_roster: false
    archimedes_position: "Actor self-claim on own infrastructure is factual record of signaling NOT independently verified. Preserved verbatim with 'attempted' temporal qualifier."

ransom_refusal_procedural:
  victim: Grafana Labs
  refused: true
  reasoning_per_source: "longstanding FBI guidance that paying cybercriminals does not guarantee anything"
  procedural_grade: A (victim self-disclosure on own incident response)
```
