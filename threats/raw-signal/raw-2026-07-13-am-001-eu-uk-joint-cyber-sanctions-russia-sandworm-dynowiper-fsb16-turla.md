---
raw_id: raw-2026-07-13-am-001-eu-uk-joint-cyber-sanctions-russia-sandworm-dynowiper-fsb16-turla
collected_at: 2026-07-13T07:32:00-04:00
run_id: pre-brief-20260713-073000
collection_mode: pre_brief_collection
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/eu-and-uk-hit-russia-with-first-joint-cyber-sanctions-package/
  published_at: 2026-07-13T07:19:05-04:00
  originating_primary: "EU Council sanctions designations + UK FCDO sanctions designations (A-grade government official action)"
  relay_grade: B
  corroborating_relay:
    source_yaml_id: securityweek
    source_name: SecurityWeek (Associated Press wire)
    source_url: https://www.securityweek.com/eu-targets-russian-intelligence-officers-accused-of-running-a-yearslong-cyber-spying-campaign/
    published_at: 2026-07-13T06:00:00-04:00
match_reason:
  watchlist: []
  actors: [Sandworm]
  actors_not_in_roster: [Turla, "FSB 16th Centre"]
  vulnerabilities: []
  keywords: [EU sanctions, UK sanctions, GRU, "FSB 16th Centre", DynoWiper, Turla, "Lumma Stealer", "Poland energy grid", "nuclear research", critical infrastructure, railway]
triage_tags: [tracked_actor, sanctions_action, restatement, ad_sector_marginal, non_flash, grader_queue_morning, roster_gap_turla_fsb16, potential_new_actor_candidate]
iocs_extracted: true
iocs_count: 0
text_word_count: 640
promoted: true
promoted_to_finding: finding-2026-07-13-0001
promoted_at: 2026-07-13T08:12:00-04:00
grading_run_id: morning-20260713-080000
ttl_expires_at: 2026-10-11T07:32:00-04:00
---

# EU and UK hit Russia with first joint cyber sanctions package

**Pre-brief collection note (window 2026-07-12T17:30 → 2026-07-13T07:30 EDT).**
Surfaced via BleepingComputer RSS at 07:19 EDT (Sergiu Gatlan), with a
corroborating Associated Press wire story carried by SecurityWeek at 06:00 EDT
(same underlying EU/UK sanctions action). This is the single substantive
raw-signal-worthy item of the AM pre-brief sweep; roster match is on
**Sandworm (#007)**.

## What the sources report

The European Union and the United Kingdom jointly announced their first
coordinated cyber-sanctions package against Russia, accusing Moscow of
coordinating a network of hacking groups responsible for attacks across Europe.

**Sanctions scope (per BleepingComputer relay):**
- **EU:** 9 individuals and 4 entities.
- **UK:** 24 individuals and entities.

**Named GRU officers (sanctioned; said to have "directed cyber and hybrid
operations"):** Vyacheslav Stafeyev, Ivan Senin, Ivan Kasyanenko.

**Named entities:**
- **IMPULS** — a company accused of recruiting hackers from Russian universities.
- **Rybar LLC** — media outlet, with 10 connected individuals.
- Participants in the **Lumma Stealer** malware operation.

**Threat groups / intelligence units named (verbatim class, per sources):**
- **FSB 16th Centre** — publicly identified as "controlling several cyber
  threat groups, including the notorious Turla hacking group." (SecurityWeek/AP
  frames the 16th Centre of Russia's FSB as the primary focus, stating it "has
  been controlling a variety of cyber threat groups" and "has conducted a wide
  range of malicious cyber activities with growing severity.")
- **Turla** — linked to targeting government networks and critical
  infrastructure across France, Germany, Poland, Cyprus, the Netherlands,
  Austria, Slovakia, Romania, and Finland since 2010.

**Cited attacks:**
- **Poland energy grid (late December):** Damaged operational-technology (OT)
  equipment; **attributed to Sandworm using DynoWiper malware** (per advisory,
  verbatim class).
- **Poland nuclear research:** Cyberattack on the National Centre for Nuclear
  Research (NCBJ) IT infrastructure.
- **Turla infrastructure strike:** a "failed strike targeting Poland's critical
  infrastructure ... could have cut power to roughly 500,000 people."
- Railway-infrastructure attacks (Poland specifically mentioned).

**Attribution language (EU):** characterized the activities as "Russia's efforts
to destabilize the EU, its member states and international partners."

---

## Why this is a roster match (characterization only — grader adjudicates)

- **Sandworm (#007, APT44 / Seashell Blizzard / GRU Unit 74455)** is named as the
  actor behind the Poland energy-grid OT-destructive attack using **DynoWiper**.
  Sandworm is a tracked roster actor. This is the promotion-relevant hook.
- **Attribution is a RESTATEMENT / official-action layer, not novel attribution.**
  Sandworm = GRU 74455 is long-established. The net-new elements are (a) the
  coordinated EU+UK sanctions designations and (b) the specific
  DynoWiper / Poland energy-grid event framing surfaced through the sanctions
  announcement. Per Hard Rule 2, Archimedes originates no attribution — all
  actor/campaign linkage above is recorded exactly as the cited sources state.
- **DynoWiper** is a wiper-family name new to the Archimedes corpus (grader/
  actor-profiler to confirm against Sandworm dossier). No hashes or atomic IOCs
  were published in either relay — the wiper is named at the family level only.

## Roster-gap / new-actor awareness

- **FSB 16th Centre** and **Turla** are NOT in `_roster.yaml`. The roster's
  Russian actors are APT28 (GRU 26165), Sandworm (GRU 74455), and APT29 (SVR) —
  plus RU-linked cybercrime (LockBit, Cl0p, REvil). No FSB-attributed actor is
  currently tracked. This is the SAME roster gap flagged in the companion
  06:00 FLASH item (raw-2026-07-13-flash-0600-001, FSB Center 16 / Berserk Bear
  critical-infra advisory). Two independent A-grade-government surfaces naming
  the FSB 16th Centre cluster within ~2 hours strengthens the `/new-actor`
  case for operator consideration (FSB 16th Centre / Turla / Berserk Bear /
  Static Tundra / Dragonfly). Flagging for operator discretion — collector does
  not originate roster additions.

## A&D relevance (marginal / structural)

- No aerospace-defense watchlist prime is named. Targeting is critical
  infrastructure (energy grid, nuclear research, railway) across EU member
  states — nation-state destructive/OT campaign class. A&D nexus is
  STRUCTURAL/INDIRECT (OT-destructive TTP + nuclear-research targeting are
  adjacent to the DIB threat model), NOT victim-anchored to any watchlist
  entity. Do not overstate. Legitimate morning-brief material as an A-grade
  government sanctions action naming a tracked roster actor (Sandworm).

## Companion / dedup context

- **Not a duplicate** of raw-2026-07-13-flash-0600-001 (FSB Center 16 defensive
  advisory — NSA/FBI/CISA joint router-targeting advisory, CVE-2018-0171 Cisco
  Smart Install). That is a defensive-guidance advisory; THIS is an EU/UK
  sanctions/policy action naming Sandworm + FSB 16th Centre + Turla. Related
  topic cluster (Russian state cyber), distinct event and distinct primary.
  Grader may choose to cluster them.

---

## Extraction notes

- Language: en
- Publisher byline: Sergiu Gatlan (BleepingComputer); Associated Press wire (via
  SecurityWeek).
- Article type: news (relay of EU Council + UK FCDO sanctions designations).
- Raw IOC extraction invoked: yes (ioc-extraction skill).
- Copyright discipline (Rule 7): no single quoted span exceeds 15 words; verbatim
  fragments limited to attribution-class group/unit names and one short EU
  characterization phrase, one use per source.
- GDPR note: named individuals (Stafeyev, Senin, Kasyanenko) are recorded as
  publicly-designated subjects of official EU/UK sanctions actions (public
  figures named in an official government designation) — permitted per
  LEGAL-POLICY GDPR data-minimization (name only; no other PII collected/stored).
- No credentials, no exploit content, no PoC present (Rules 3, 4 N/A).

## IOCs (from ioc-extraction skill)

```yaml
extraction_metadata:
  source_brief_id: raw-2026-07-13-am-001
  source_url: https://www.bleepingcomputer.com/news/security/eu-and-uk-hit-russia-with-first-joint-cyber-sanctions-package/
  extracted_at: 2026-07-13T11:32:00Z
  extracted_by: collector
  target_actor_id: null   # roster hint Sandworm #007; grader resolves attribution
  text_word_count: 640

indicators: []   # No atomic network IOCs published in either relay.
                 # No IPv4/IPv6/domain/URL/hash/CVE present. Malware families
                 # named at family level only (DynoWiper, Lumma Stealer) — recorded
                 # under related_malware in attribution_claims, not as atomic IOCs.

attribution_claims:
  - claimed_actor: Sandworm
    ioc_ids: []
    related_malware: [DynoWiper]
    claimed_campaign: "Poland energy grid OT-destructive attack (late December)"
    claimed_by_source: "EU Council / UK FCDO sanctions designations (per BleepingComputer + SecurityWeek/AP relays)"
    attribution_confidence_in_source: stated_as_fact_official_designation
    attribution_is_new_not_restatement: false   # Sandworm=GRU 74455 is long-established; sanctions action is the net-new element
    requires_grading: true
    notes: "Roster actor #007. Hard Rule 2 — recorded verbatim as sources state; Archimedes originates no attribution."
  - claimed_actor: "FSB 16th Centre"
    ioc_ids: []
    related_malware: []
    claimed_campaign: "control of multiple cyber threat groups incl. Turla; EU/UK sanctions target"
    claimed_by_source: "EU Council / UK FCDO sanctions designations (per relays)"
    attribution_confidence_in_source: stated_as_fact_official_designation
    attribution_is_new_not_restatement: false
    requires_grading: true
    notes: "NOT in _roster.yaml. Potential /new-actor candidate (operator discretion). Same cluster as raw-2026-07-13-flash-0600-001."
  - claimed_actor: Turla
    ioc_ids: []
    related_malware: []
    claimed_campaign: "gov + critical-infra targeting across 9 EU states since 2010; failed Poland power-grid strike (~500k people)"
    claimed_by_source: "EU Council / UK FCDO sanctions designations (per relays)"
    attribution_confidence_in_source: stated_as_fact_official_designation
    attribution_is_new_not_restatement: false
    requires_grading: true
    notes: "NOT in _roster.yaml. Named as controlled by FSB 16th Centre."
  - claimed_actor: "Lumma Stealer operation (participants)"
    ioc_ids: []
    related_malware: ["Lumma Stealer"]
    claimed_campaign: null
    claimed_by_source: "EU/UK sanctions designations (per relays)"
    attribution_confidence_in_source: stated_as_fact_official_designation
    attribution_is_new_not_restatement: false
    requires_grading: true
    notes: "Sanctioned operation participants; malware-family reference only, no atomic IOCs."

benign_filtered:
  - value: bleepingcomputer.com
    reason: publisher_own_domain
  - value: securityweek.com
    reason: publisher_own_domain

extraction_warnings:
  - type: no_atomic_iocs
    ioc_id: null
    detail: "Sanctions-announcement reporting; no IP/domain/hash/CVE published. Underlying EU Council + UK FCDO designation pages may carry entity detail; direct retrieval deferred to grader/actor-profiler if promoted. DynoWiper wiper-family hashes not published in these relays."
```
