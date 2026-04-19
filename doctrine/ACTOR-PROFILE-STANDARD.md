# ACTOR-PROFILE-STANDARD.md — Actor Profile Structure

> **Archimedes doctrine — actor profiles.**
> Every threat actor dossier must conform to this structure. The `actor-profiler` subagent is bound by it.

---

## Files Per Actor

Every tracked actor gets a directory at `threats/threat-actors/{ACTOR-NAME}/` containing:

| File | Purpose | Who writes |
|---|---|---|
| `profile.md` | Human-readable dossier | `actor-profiler` |
| `iocs.md` | Human-readable IOC reference | `actor-profiler` |
| `iocs.yaml` | Agent-queryable IOC data | `actor-profiler` (generates from intel) |
| `threat-box.yaml` | Structured scoring | `actor-profiler` (human approves HIGH) |
| `threat-box.md` | Scoring rationale narrative | generated from `threat-box.yaml` |

---

## Frontmatter Schema (profile.md)

Every profile opens with complete YAML frontmatter:

```yaml
---
id: "006"                              # 3-digit padded ID
primary_name: "APT28"
aliases: [Fancy Bear, Forest Blizzard, ...]
mitre_attack_id: G0007
mitre_attack_url: https://attack.mitre.org/groups/G0007/
type: "Nation-State APT"               # or Cybercriminal, Hacktivist, etc.
attribution:
  nation: RU                           # ISO 3166-1 alpha-2
  service: GRU
  unit: "Unit 26165"
active_since: 2004
status: active                         # active | dormant | disrupted
status_note: "Highly active"
motivation: [espionage, hack-and-leak, influence-operations]
threat_level: HIGH                     # HIGH | MEDIUM | LOW
admiralty_grade: A1
tlp: CLEAR
dossier_version: 1
last_updated: 2026-04-03
last_reviewed: 2026-04-03
next_review_due: 2026-07-02            # +90 days from last_reviewed
related_actors: ["004", "003"]         # IDs from _roster.yaml
---
```

---

## Section Structure

**Section order is fixed.** All sections must be present. If a section has no content, use "No documented [X] at this time."

1. **Overview** — 2–4 paragraphs of prose. Open with the most important insight.
2. **Primary Targets** — sectors + geography
3. **Signature Campaigns** — table
4. **TTPs** — subsections by ATT&CK tactic, each with a table
5. **Malware Arsenal** — table
6. **Infrastructure Patterns** — bullets
7. **Known IOCs** — brief summary with pointer to `iocs.md`
8. **Geopolitical Context** — prose
9. **Connection Web** — links to related actors
10. **Defense Recommendations** — numbered list, specific and actionable
11. **References** — links to primary sources

---

## Writing Standards

### Overview
- Open with the most important current-state insight, not historical background
- 2–4 paragraphs maximum
- Name the "so what" — why does a defender care about this actor?

### Primary Targets
- Specific sectors, not "various industries"
- Specific geographic focus, not "globally"
- Current focus separate from historical focus if both are relevant

### Signature Campaigns
- Table with columns: `Campaign | Year | Description`
- Campaigns are discrete named operations (2016 DNC hack, Operation RoundPress)
- Do not confuse tool rollouts with campaigns

### TTPs
- Organized by ATT&CK tactic (Initial Access, Execution, Persistence, etc.)
- Each technique cited by T-number with link to ATT&CK
- One-line description per technique

### Malware Arsenal
- Table with columns: `Malware | Type | Notes`
- Type: Backdoor, RAT, Loader, Dropper, Wiper, Stealer, etc.
- Include current-gen and historically significant tools

### Infrastructure Patterns
- How the actor builds and rotates infrastructure
- Not specific IOCs (those belong in iocs.md)
- Patterns: "heavy abuse of X," "uses compromised Y," "rotates domains within 48 hours"

### Defense Recommendations
- Specific and actionable, not "patch promptly"
- Each recommendation tied to a known TTP or IOC
- Include threat-hunt queries where possible (specific CLSIDs, scheduled task names, registry paths)

### References
- Prioritize primary sources (vendor reports, government advisories)
- Include MITRE ATT&CK group page
- Include any DOJ indictments or NSA/CISA advisories
- Markdown links with descriptive titles

---

## IOC File Structure

### iocs.md (human-readable)

Opens with frontmatter:

```yaml
---
actor_id: "006"
actor_name: APT28
last_updated: 2026-04-03
admiralty_grade: A1
tlp: CLEAR
---
```

Followed by sections:
1. CVEs Actively Exploited
2. Malicious Delivery Domains
3. IP Addresses
4. File Hashes (by role — documents, binaries)
5. Registry Indicators
6. Scheduled Task Indicators
7. Cloud C2 Infrastructure
8. Detection Queries (Hunt Guidance)
9. Sources

### iocs.yaml (agent-queryable sidecar)

Every indicator in `iocs.md` has a corresponding structured entry:

```yaml
actor_id: "006"
actor_name: APT28
last_updated: 2026-04-03
admiralty_grade: A1
tlp: CLEAR
source_of_record: iocs.md

ttl:
  network_infrastructure: 90    # days
  file_hashes: 730
  registry: never
  vulnerabilities: never

indicators:
  - id: apt28-cve-2026-21509
    type: cve                   # cve | domain | ipv4 | ipv6 | sha256 | md5 |
                                # sha1 | registry_key | scheduled_task | 
                                # cloud_service | url
    value: CVE-2026-21509
    # ... type-specific fields
    source_brief: trellix-2026-02    # references a finding/brief ID

hunt_queries:
  - id: <hunt-id>
    platform: <splunk | edr | m365 | etc>
    title: "Short title"
    query_type: <type>
    query: |
      <multi-line query>
```

The `actor-profiler` writes both files in sync. `iocs.md` is human-readable; `iocs.yaml` is the source of truth for the `_master-index.yaml` regeneration.

---

## Threat-Box Scoring File

Every actor has `threat-box.yaml`. Full schema:

```yaml
actor_id: "006"
actor_name: "APT28"
target_profile: "ad-prime-v1"
scored_at: 2026-04-03
scored_by: archimedes-actor-profiler
reviewed_by: ryan                 # null until human approves for HIGH

scores:
  espionage:
    intent:
      score: 5
      label: target-specific
      evidence: "..."
      sources: [<source-brief-ids>]
    willingness:
      modifier: 0
      label: no-constraints
      evidence: "..."
    capability:
      score: 5
      label: significant
      evidence: "..."
      sources: [...]
    novelty:
      modifier: 0
      label: custom-advanced
      evidence: "..."
    ioc_corroboration:
      observed: false
      capability_bonus_applied: 0
    final_intent: 5
    final_capability: 5
    composite: 10
    threat_level: HIGH
  
  supply_chain: { ... }
  destructive: { ... }
  disruptive: { ... }
  cyber_crime: { ... }

overall_score: 9.65
overall_threat_level: HIGH

confidence:
  admiralty: A1
  notes: "..."

review_policy:
  interval_days: 90
  last_reviewed: 2026-04-03
  next_review_due: 2026-07-02

history:
  - scored_at: 2026-04-03
    scorer: archimedes-actor-profiler
    change: "initial"
```

See `doctrine/THREAT-BOX-METHODOLOGY.md` for how scores are derived.

---

## Related Actors & Connection Web

The Connection Web section in `profile.md` links to related actors using their directory path:

```markdown
## Connection Web

- ⛓️ **GRU Unit 74455 (Sandworm)** — Sister GRU unit; destructive ops...
- ⛓️ **[Actor #004 UNC1549](../UNC1549/profile.md)** — Iranian IRGC equivalent playbook...
- ⛓️ **[Actor #003 Lazarus Group](../Lazarus-Group/profile.md)** — DPRK counterpart...
```

The `related_actors` frontmatter array (using IDs) is the machine-readable version. Both must stay in sync.

---

## Profile Versioning

`dossier_version` increments on any substantive content change. Typos and formatting do not bump the version.

The `history` field of `threat-box.yaml` tracks scoring revisions separately — scoring can change without the profile version bumping.

---

## Profile Migration (from old repo)

When migrating actors from the original `intel-repository`:

1. Copy `profile.md` to new location
2. Replace "Scoundrel #XXX" with "Actor #XXX"
3. Add full frontmatter per schema above
4. Generate `iocs.yaml` from existing `iocs.md` data
5. Create empty `threat-box.yaml` scaffold (scoring happens in subsequent pass)
6. Update related-actor links to new paths
7. Commit with message: `Migrate actor {NAME} from C3PO repo`

The APT28 directory in `threats/threat-actors/APT28/` is the reference migration — use it as the template for subsequent ports.

---

## Roster File

All tracked actors appear in `threats/threat-actors/_roster.yaml`. This is the master list. The `actor-profiler` reads it when resolving aliases ("is 'Cozy Bear' one we track? Yes, it's actor #009").

Adding a new actor to the roster requires:
1. Human decision to track
2. Initial profile stub created via `/new-actor` command
3. Roster entry added with ID, aliases, attribution summary
4. First-pass profile complete within 7 days
5. Threat-box scoring within 14 days (may require human sign-off)

---

*Last reviewed: Session 1 scaffold*
