---
raw_id: raw-2026-07-30-pm-004
collected_at: 2026-07-30T15:47:00-04:00
run_id: pre-brief-20260730-153000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: "BleepingComputer (Bill Toulas)"
  source_url: https://www.bleepingcomputer.com/news/security/analog-devices-discloses-data-breach-says-operations-unaffected/
  published_at: 2026-07-30T11:12:00-04:00
  secondary_outlets:
    - source_yaml_id: the-record
      source_name: "The Record (Recorded Future News)"
      source_url: https://therecord.media/analog-devices-semiconductor-company-data-breach
      published_at: 2026-07-30T15:10:00-04:00
    - source_yaml_id: securityweek
      source_name: "SecurityWeek (Eduard Kovacs) — earlier same-day (07:16 EDT)"
      source_url: https://www.securityweek.com/
      published_at: 2026-07-30T07:16:00-04:00
match_reason:
  watchlist: []          # ADI not a watchlist entity; semiconductor supplier is DIB-supply-chain-adjacent
  actors: []             # ExfilSquad not a roster actor
  vulnerabilities: []
  keywords: [semiconductor, "data breach", ExfilSquad, "supply chain", DIB]
triage_tags: [non_flash, breach_disclosure, dib_supply_chain_adjacent, grader_queue, awareness]
iocs_extracted: true
iocs_count: 0
text_word_count: 300
promoted: true
promoted_to_finding: finding-2026-07-30-0007
promoted_at: 2026-07-30T16:24:00-04:00
grading_run_id: afternoon-20260730-160000
ttl_expires_at: 2026-10-28T15:47:00-04:00
---

# Analog Devices (semiconductor) discloses SEC-filed data breach — operations unaffected

Surfaced across three publisher-independent outlets in-window (**SecurityWeek** 07:16 EDT,
**BleepingComputer** 11:12 EDT, **The Record** 15:10 EDT). Held below-FLASH at the 12:00 sweep and
flagged for the afternoon-brief grader; raw-signaled now that it is multi-outlet with an SEC filing.

**Facts (per relays):** American semiconductor firm **Analog Devices (ADI)** disclosed in an SEC
filing that an **unauthorized party accessed some systems and exfiltrated certain files.** Breach
**detected 2026-06-23**. ADI states **business operations were not affected** and does not
anticipate material financial impact; engaged external cybersecurity experts and notified law
enforcement. **Type of data compromised: not yet detailed** (scope still under investigation).
Separately, ADI noted an **unrelated cybersecurity matter** reported publicly ~2026-07-26.

**Actor:** **ExfilSquad** (a data-theft / extortion group, no file-encryption) initially claimed
ADI on its leak site — earlier reporting cited a **570,000-record** claim — then **delisted** the
company (a pattern typically consistent with ransom negotiation). Relays note it is **unclear
whether the ExfilSquad intrusion is connected** to the SEC-filed breach. **ExfilSquad is not a
roster actor.**

**A&D relevance (awareness):** ADI is a major semiconductor supplier whose components are used in
**aerospace/defense** systems — **DIB supply-chain-adjacent.** However: **no defense/aerospace
customer or product named, no tracked actor, no CVE, no atomic IOCs.** Below the normal raw-signal
bar on its own merits; surfaced for the grader because (a) it is now multi-outlet + SEC-filed and
(b) it was explicitly held for the afternoon board. Awareness flag for the orchestrator on whether
the **semiconductor-supply-chain** angle warrants watchlist consideration.

---

## Extraction notes

- Language: en
- Publisher byline: BleepingComputer (Bill Toulas) / The Record / SecurityWeek (Eduard Kovacs)
- Article type: news (breach disclosure / SEC filing)
- Raw IOC extraction invoked: yes — **no atomic IOCs present** in any relay
- Credentials: none stored; "570,000 records" is a breach-scope claim, not credential values (Hard Rule 7)

## IOCs (from ioc-extraction skill)

```yaml
iocs: []   # no domains, IPs, hashes, or malware names in any relay
attribution_claims:
  - actor: "ExfilSquad"
    type: "data-theft / extortion group (no file-encryption)"
    nation: unknown
    claimed_by: "ExfilSquad self-claim (leak-site listing, since delisted)"
    language: "relays note it is 'unclear if the ExfilSquad intrusion is connected to the data breach disclosed in the SEC filing'"
    roster_match: none
    note: "Self-claim recorded per Hard Rule 2; connection to the SEC-filed breach explicitly UNCONFIRMED."
```
