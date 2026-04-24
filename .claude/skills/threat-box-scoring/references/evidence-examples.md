# Evidence Narrative Examples

> **On-demand reference.** Loaded when the actor-profiler is drafting evidence fields for a new actor's threat-box.yaml and wants to see what well-written evidence looks like.
> Based on the APT28 Session 1 exemplar.

---

## Structure of a good evidence field

Evidence narratives should:

1. **Cite specific sources** by `source_brief_id` that match entries in the findings index
2. **Reference specific campaigns or TTPs** rather than generic capability claims
3. **Establish temporal relevance** — when was this observed?
4. **Answer the scoring question explicitly** — why this score, not the score above or below?
5. **Stay under ~150 words per category field** — longer than that, split into structured sub-fields

---

## Intent evidence — good examples

### Intent=5 (Target-Specific) — APT28 Espionage

```yaml
intent:
  score: 5
  label: target-specific
  evidence: |
    Two decades of documented operations targeting NATO defense ministries,
    weapons suppliers, and Ukraine aid logistics. Specific targeting of
    named A&D primes and defense ministries in DoJ 2018 indictment and
    NSA/CISA May 2025 advisory on GRU Unit 26165 logistics targeting.
    The operational objective — collection of defense and military
    intelligence — is achievable only within our target's network.
  sources: [doj-2018-indictment, mitre-g0007, nsa-cisa-2025-05]
```

**Why this works:** Names the specific legal document (DoJ 2018 indictment), the specific advisory (NSA/CISA May 2025), and the specific Unit (GRU 26165). Explains why the objective is Target-Specific (achievable only within target network) rather than sector-association.

### Intent=4 (Ideology Association) — APT28 Supply Chain

```yaml
intent:
  score: 4
  label: ideology-association
  evidence: |
    Known targeting of NATO logistics and aid supply chain supporting Ukraine
    (NSA/CISA May 2025 advisory). While not solely supply-chain-focused, A&D
    primes are reached via trusted relationship compromise (T1199) of
    suppliers and government accounts.
  sources: [nsa-cisa-2025-05, mitre-g0007]
```

**Why this works:** The ideology link (anti-Ukraine aid) is explicitly named. The MITRE technique T1199 (Trusted Relationship) anchors the claim in a specific TTP. The "while not solely" qualifier honestly scopes the claim rather than overreaching.

### Intent=3 (Sector Association) — hypothetical criminal group

```yaml
intent:
  score: 3
  label: sector-association
  evidence: |
    Named in 2024 FBI Flash Alert as targeting defense sector for ransomware
    extortion. Not specifically A&D primes — victim list includes logistics
    firms, manufacturers, and one DoD subcontractor. Sector framing is
    generic "defense industrial base," not specific to ITAR-regulated primes.
  sources: [fbi-flash-2024-11]
```

**Why this works:** Explicitly distinguishes sector-association from target-specific by showing the victim pattern includes non-A&D-primes. Anchors in a named FBI document.

### Intent=1 (Target of Opportunity) — opportunistic scanner

```yaml
intent:
  score: 1
  label: target-of-opportunity
  evidence: |
    No documented targeting of A&D, defense, or government sectors. Mass
    exploitation of Exchange vulnerabilities across victim pool of 2000+
    entities globally, no sector-targeting pattern. Victim distribution
    matches internet-exposed Exchange instance distribution, consistent
    with opportunistic targeting.
  sources: [microsoft-2024-hafnium-variant, bleepingcomputer-2024-09]
```

**Why this works:** The claim "no sector-targeting pattern" is grounded in the victim-distribution observation. Explicitly ruling out higher scores.

---

## Capability evidence — good examples

### Capability=5 (Significant) — APT28 Espionage

```yaml
capability:
  score: 5
  label: significant
  evidence: |
    X-Agent, AUTHENTIC ANTICS, GooseEgg, Operation RoundPress, CVE-2026-21509
    active campaigns — all confirmed by multiple trusted sources (Microsoft MSTIC,
    Palo Alto Unit 42, UK NCSC, ESET, Trellix). Documented active use within
    last 24 months. Multiple A-grade sources.
  sources: [mstic-2024, unit-42-2024, ncsc-uk-2025, eset-2025, trellix-2026-02]
```

**Why this works:** Names five specific malware families/campaigns. Cites five A-grade sources. Explicitly addresses the "active within 24 months" requirement.

### Capability=3 (Limited) — emerging actor

```yaml
capability:
  score: 3
  label: limited
  evidence: |
    Two documented campaigns (2024 phishing against Middle Eastern energy firms,
    2025 credential harvesting against US academics). No evidence of custom
    tooling or living-off-the-land. Sample count in public threat feeds: 23
    hashes. Sources: Mandiant 2024 report, CyberWarrior76 2025 Substack.
  sources: [mandiant-2024-energy, cyberwarrior76-2025-07]
```

**Why this works:** Names specific campaigns. Quantifies evidence (23 hashes). Mixes A-grade and C-grade sources transparently.

### Capability=1 (Not Capable) — nominal capability

```yaml
capability:
  score: 1
  label: not-capable
  evidence: |
    No documented destructive operations by this actor. Ransomware-adjacent
    activity (encryption for extortion) is scored under Cyber-Crime, not
    Destructive. No wiper tooling, no disruption of industrial systems, no
    integrity-attacking TTPs observed across 4 years of tracking.
  sources: []
```

**Why this works:** Explicitly distinguishes from adjacent categories. Names the time window. An empty sources array is correct here — we're asserting the absence of evidence.

---

## Willingness evidence — good examples

Willingness evidence is usually one sentence. It's a geopolitical posture statement, not a detailed narrative.

```yaml
willingness:
  modifier: 0
  label: no-constraints
  evidence: "Active hostilities via Ukraine war; sustained sanctions regime; no diplomatic constraints."
```

```yaml
willingness:
  modifier: 1
  label: moderate-constraints
  evidence: "Limited diplomatic ties via Tehran-facilitated negotiations on narrow issues; no economic cooperation."
```

```yaml
willingness:
  modifier: 2
  label: strong-constraints
  evidence: "NATO ally, Five Eyes intelligence sharing, strong economic integration. Rarely applies to threat actors."
```

---

## Novelty evidence — good examples

Also usually one sentence. Describes the tooling profile.

```yaml
novelty:
  modifier: 0
  label: custom-advanced
  evidence: |
    Custom tooling per campaign. COM hijacking via novel CLSID. Living-off-the-land
    in M365 via OAuth token theft (AUTHENTIC ANTICS). Cloud-storage-as-C2 to defeat
    perimeter detection.
```

```yaml
novelty:
  modifier: 1
  label: semi-custom
  evidence: |
    Proprietary loader family shared across multiple campaigns. No off-the-shelf
    components observed in 2024-2025 activity. Tooling documented by Unit 42.
```

```yaml
novelty:
  modifier: 2
  label: commodity
  evidence: |
    Cobalt Strike beacons, Mimikatz, publicly-available LOLBAS techniques. No
    custom malware observed. Tradecraft matches generic ransomware affiliate
    pattern.
```

---

## IOC corroboration — good examples

### When observed

```yaml
ioc_corroboration:
  observed: true
  splunk_search: "index=defenseclaw_local src_ip=70.34.253.247 OR dest_ip=70.34.253.247"
  first_seen: "2026-04-15T08:22:00Z"
  bonus_category: espionage
  note: |
    Password-spray IP 70.34.253.247 (per NSA/CISA 2024-08 advisory) observed
    in authentication logs against M365 tenant on 2026-04-15. Two failed login
    attempts; no successful compromise. Bonus applied to espionage category
    matching the credential-access TTP context of the original advisory.
```

### When not observed

```yaml
ioc_corroboration:
  observed: false
  bonus_category: null
  note: "No first-party IOC hits at time of initial scoring."
```

---

## What bad evidence looks like

### Too generic

```yaml
# BAD — what does this mean?
evidence: "Actor is a well-known threat to the defense sector."
```

### No sources

```yaml
# BAD — unsupported assertion
evidence: "This group is known to have advanced capabilities."
sources: []
```

### Hedged without being specific

```yaml
# BAD — "may" without WEP vocabulary
evidence: "The actor may be capable of destructive attacks based on reported activity."
```

### Copies source language too closely

```yaml
# BAD — close paraphrase of source text
evidence: "The Mandiant report notes that 'UNC1549 has shifted TTPs to include supply chain compromise.'"
```

Per Hard Rule 6, quotes must be under 15 words and limited to one per source. Better: paraphrase fully and cite.

### Claims capability without evidence

```yaml
# BAD — nation-state inference
evidence: "As a nation-state actor, this group has significant resources and can conduct sophisticated attacks."
```

The doctrine explicitly bans inference from "this is a nation-state" to high capability scores. Evidence of specific capability, or lower score.

---

## Checklist for an evidence field

Before moving on from a score, ask:

- [ ] Did I name at least one specific campaign, TTP, or incident?
- [ ] Did I cite a `source_brief_id` that exists in the findings index?
- [ ] If I claimed Intent=5 or Capability=5, do I have A-grade sources?
- [ ] Did I stay under ~150 words per evidence field?
- [ ] Did I avoid banned phrases from `smart-brevity/references/banned-phrases.md`?
- [ ] Am I asserting what the evidence supports — not inflating and not overhedging?

If any answer is no, revise before scoring.

---

*Last updated: Session 2 scaffold*
*Based on: `threats/threat-actors/APT28/threat-box.yaml`*
