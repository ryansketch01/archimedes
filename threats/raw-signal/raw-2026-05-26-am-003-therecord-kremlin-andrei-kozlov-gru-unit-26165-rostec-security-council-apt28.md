---
raw_id: raw-2026-05-26-am-003
collected_at: 2026-05-26T07:33:00-04:00
run_id: pre-brief-20260526-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: the-record
  source_name: The Record (Recorded Future)
  source_url: https://therecord.media/andrei-kozlov-appointed-russia-security-council
  published_at: 2026-05-25T19:00:00-04:00
  author: Daryna Antoniuk
match_reason:
  watchlist: []                  # No A&D-prime directly compromised; defense contractors enumerated as Unit 26165 historical target class
  actors:
    - "006"                      # APT28 / Fancy Bear / Forest Blizzard / BlueDelta / Sofacy / Sednit / Pawn Storm / STRONTIUM / Iron Twilight / Tsar Team / Unit 26165 / 85th GTsSS — institutional context shift signal
  vulnerabilities: []
  keywords:
    - Kremlin
    - Andrei Kozlov
    - Sergei Shoigu
    - Pavel Konovalchik
    - Vladimir Putin
    - Russia Security Council
    - Rostec
    - RT-Information Security
    - RT-IB
    - GRU
    - Military Unit 26165
    - 85th Main Special Service Center
    - 85th GTsSS
    - Fancy Bear
    - APT28
    - BlueDelta
    - Forest Blizzard
    - cyber espionage
    - credential theft
    - influence operations
    - defense contractors
    - logistics companies
    - policy organizations
triage_tags:
  - tracked_actor_institutional_context
  - apt28_chain_of_command_signal
  - gru_unit_26165_personnel_movement
  - russia_security_council_appointment
  - no_new_ops_attribution
  - no_iocs_published
  - defender_relevant_intel_signal
  - morning_brief_actor_activity_candidate
iocs_extracted: true
iocs_count: 0                    # No technical IOCs; institutional / personnel intelligence only
text_word_count: 280
promoted: true
promoted_to_finding: finding-2026-05-26-0003-therecord-kozlov-rostec-gru-unit-26165-security-council-apt28-institutional-context
promoted_at: 2026-05-26T08:00:00-04:00
ttl_expires_at: 2026-08-24T07:33:00-04:00
---

# Kremlin Appoints Cyber Executive with Alleged GRU Ties to Security Council Role

**Source:** The Record (from Recorded Future News), 2026-05-25 19:00 EDT
**URL:** https://therecord.media/andrei-kozlov-appointed-russia-security-council
**Byline:** Daryna Antoniuk

## Article summary

Andrei Kozlov, the former head of a cybersecurity center within
Russia's state-owned defense conglomerate **Rostec**, was named an
aide to Security Council Secretary Sergei Shoigu on Friday
(2026-05-22 per article reference; published Mon 2026-05-25 19:00
EDT).

## Named persons

- **Andrei Kozlov** — appointee. Former head of a cybersecurity
  center within Rostec. Reportedly **held a classified security
  clearance under Military Unit 26165**.
- **Sergei Shoigu** — Security Council Secretary (Kozlov's new
  reporting line).
- **Pavel Konovalchik** — predecessor in the same Security Council
  aide role; "also reportedly linked to the same GRU unit" per The
  Record.
- **Vladimir Putin** — Russian President; appointment context.

## Named organizations

- **Russia's Security Council** — Kozlov's new affiliation.
- **Rostec** — Russian state-owned defense conglomerate; Kozlov's
  prior employer (head of cybersecurity center within).
- **GRU Military Unit 26165 / 85th Main Special Service Center
  (85th GTsSS)** — Kozlov's reported prior classified security
  clearance affiliation; also linked to predecessor Konovalchik.
- **RT-Information Security (RT-IB)** — referenced in article
  context (Rostec subsidiary).
- **TASS** — Russian state news agency (article source).

## GRU Unit 26165 tradecraft enumeration

The Record (verbatim quote of Unit 26165 historical targeting):
"accused of conducting cyber espionage, credential theft and
influence operations targeting **governments, defense contractors,
logistics companies and policy organizations across Europe and the
United States**."

## Tracked threat actor aliases enumerated by The Record

Per The Record, Unit 26165 is the institutional home of:
- **Fancy Bear**
- **APT28**
- **BlueDelta**
- **Forest Blizzard**

Per `_roster.yaml` actor #006, additional aliases include: Sofacy,
Sednit, Pawn Storm, STRONTIUM, FROZENLAKE, Fighting Ursa, Iron
Twilight, GruesomeLarch, UAC-0001, TG-4127, Tsar Team, Group 74.
MITRE ATT&CK ID: **G0007**.

## A&D-prime impact analysis

NO direct A&D-prime compromise reported. The Record explicitly
enumerates "defense contractors" as a Unit 26165 historical target
class but does NOT name specific watchlist primes (Lockheed Martin,
Boeing, RTX, Northrop, GD, BAE, L3Harris, Leidos, SAIC, Thales,
GE Aerospace, Safran, Honeywell Aerospace, Airbus, Elbit) in
connection with this appointment. The story is institutional /
personnel context, NOT an operational compromise event.

## Defender relevance

Personnel movements at the senior Russian state-cyber chain of
command are intelligence signals — not directly operational, but
correlate with potential changes in tradecraft focus, victim
prioritization, or political tasking patterns over the medium
term. Archimedes does NOT extrapolate to specific predictions per
Hard Rule 2; the corpus surface is institutional-context
documentation for actor #006 (APT28) dossier review at next
update cycle (next_review_due: 2026-07-02 per _roster.yaml).

---

## Extraction notes

- Language: en
- Publisher byline: Daryna Antoniuk (Recorded Future / The Record)
- Article type: news (B-grade media; The Record is corpus-anchored
  at B per source-grades.yaml)
- Raw IOC extraction invoked: yes (zero technical IOCs; institutional
  intel only)
- Grader disposition target: morning brief Actor Activity section as
  APT28 institutional-context note. Not a finding promotion candidate
  (no new operational compromise, no new tradecraft, no new
  victimology); brief-tier defender-relevant intel signal only.

## IOCs (from ioc-extraction skill)

```yaml
iocs: []

# No technical IOCs in this article. Institutional / personnel
# intelligence only. Persons (Kozlov, Shoigu, Konovalchik) and
# organizations (Rostec, RT-IB, Security Council, Unit 26165 /
# 85th GTsSS) are named-entity intelligence, not network IOCs.

ttp_keywords: []
# No TTPs documented in this article. Article references Unit
# 26165's historical TTP categories (cyber espionage, credential
# theft, influence operations) but does NOT document specific
# new tradecraft.

attribution_claims:
  - claim_text: |
      "Military Unit 26165 (85th Main Special Service Center)"
      institutional home of "Fancy Bear, APT28, BlueDelta, Forest
      Blizzard"
    actor_aliases: [Fancy Bear, APT28, BlueDelta, Forest Blizzard]
    affiliation_named: "GRU / Military Unit 26165 / 85th GTsSS"
    confidence_language: "accused of" + "reportedly linked to"
    originating_primaries:
      - Western intelligence community attribution baseline (US/UK/EU/NATO governments, FBI/CISA/NCSC joint advisories from 2018 onward)
      - The Record direct framing in this article
    corpus_baseline: |
      APT28 attribution to GRU Unit 26165 is corpus-baseline per
      _roster.yaml actor #006 attribution: nation=RU,
      service=GRU, unit="Unit 26165 (85th GTsSS)". The Record's
      framing aligns with corpus baseline. No new attribution
      origination; restatement of established attribution.
    hard_rule_2_compliance: |
      Archimedes does not originate attribution. The Record's
      framing is preserved verbatim. Institutional appointment
      story is corpus-relevant as actor #006 chain-of-command
      personnel context; Archimedes does NOT extrapolate the
      personnel movement to specific operational predictions.
  - claim_text: |
      Unit 26165 historical targeting: "governments, defense
      contractors, logistics companies and policy organizations
      across Europe and the United States"
    target_categories_named: [governments, defense contractors, logistics companies, policy organizations]
    geographic_scope: [Europe, United States]
    confidence_language: "accused of"
    originating_primaries:
      - Western intelligence community baseline (corpus-tracked)
    corpus_baseline: |
      APT28's targeting of "defense contractors" is corpus-
      baseline per established Mandiant / CrowdStrike / Unit 42 /
      MSTIC documentation since at least 2014 (DCLeaks, World
      Anti-Doping Agency, German Bundestag, etc.). The Record's
      restatement aligns with corpus baseline.
```
