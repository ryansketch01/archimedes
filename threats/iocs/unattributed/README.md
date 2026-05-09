# Unattributed IOC clusters

This directory holds IOC clusters that have **no confirmed actor
attribution** but are worth tracking and queryable through the master
index.

## When to use

A cluster file goes here when **all** of:

1. A finding (or set of findings) produces meaningful IOCs — domains,
   IPs, hashes, URLs, certs, behavioral indicators
2. The originating research does **not** attribute the cluster to a
   tracked actor in `threats/threat-actors/_roster.yaml`
3. The grader / actor-profiler considered force-fitting attribution
   to the closest tracked actor and concluded that doing so would
   breach **Hard Rule 2 (no attribution origination)**
4. The IOCs are still useful to a CTI consumer — they should be
   queryable via `mcp__splunk-query__search` lookups, surfaced by
   `/ioc-hunt`, and visible in the master index

Without this bucket, IOCs in that situation get stranded — written
into a finding's body but never reaching `_master-index.yaml`. That
silent loss bit Archimedes during 2026-05-07's afternoon brief
(Beagle backdoor + PAN-OS CL-STA-1132 IOCs both went missing from
the index because no actor home existed and force-fitting would
have breached Rule 2).

## When NOT to use

- The cluster has solid attribution to a roster actor → put indicators
  in that actor's `iocs.yaml`, not here
- The cluster has attribution to a brand-new actor → run `/new-actor`
  for the actor, then put indicators in the new dossier's `iocs.yaml`
- The IOCs are noise (false positives, scanner ASNs, well-known
  benign infrastructure) → discard, don't track

If a cluster initially lands here and later earns attribution
(corroborating reporting, /new-actor scaffolding, etc.), **migrate**
the indicators to the relevant actor's `iocs.yaml` and **delete**
the cluster file from this directory. The master index regen will
remove it from the unattributed section automatically. Keep a note
in the actor's profile.md citing the migration so audit trail
survives.

## Cluster file schema

One cluster per `.yaml` file. Filename should match `cluster_id`
(lowercase, hyphens, no spaces). Schema:

```yaml
cluster_id: beagle                    # slug; matches filename
cluster_name: "Beagle backdoor"       # human-readable
first_seen: 2026-05-07                # ISO date

# Why this cluster has no actor attribution. Be honest about hedged
# overlaps — they're useful for an operator's mental model but Hard
# Rule 2 forbids promoting them to attribution.
provenance:
  - source: finding-2026-05-07-0003
    note: >
      BleepingComputer relaying Sophos research. Sophos hedges PlugX
      tradecraft overlap but explicitly does NOT attribute Beagle to
      a known PlugX-using cluster.
  - source: <future-finding-id>
    note: <added when more findings reference this cluster>

# Free-text section explaining the cluster's defining tradecraft, what
# corroboration would lift it to actor-attributed, and any other
# context an operator would need at /ioc-hunt time.
notes: |
  Beagle is a credential-stealer / loader observed in fake-Claude-AI
  watering-hole campaigns. PlugX overlap is loose (string-stack
  encryption pattern only) — not promoted.

  To migrate to actor-attributed:
  - Mandiant / CrowdStrike / Unit 42 / MSTIC publishes corroborating
    attribution
  - First-party Splunk hit on these IOCs ties them to a roster actor's
    infrastructure

# Indicators — same shape as actor iocs.yaml indicator entries.
indicators:
  - id: beagle-domain-fake-claude-001
    type: domain
    value: anthropic-claude.support       # example, fictitious
    role: delivery
    first_seen: 2026-05-07
    source: finding-2026-05-07-0003

  - id: beagle-hash-loader-001
    type: sha256
    value: a1b2c3...                       # full hash
    role: payload
    first_seen: 2026-05-07
    source: finding-2026-05-07-0003
```

Indicator types should match what's used in actor `iocs.yaml`
(domain, ipv4, ipv6, sha256, sha1, md5, url, cve, email,
malware_family, certificate_thumbprint, code_signing_subject, other).

## Hard Rule 2 isolation

`scripts/regenerate_ioc_index.py` keeps actor and unattributed
indicators in **two separate sections** of the master index:

- `lookup` / `cross_actor` — actor-attributed IOCs only
- `unattributed_lookup` / `unattributed_clusters` — clusters from this directory

If the same indicator value appears in both an actor's `iocs.yaml`
AND an unattributed cluster, it shows up in both lookups separately.
The script does not auto-merge; the operator investigates.

## How `/ioc-hunt` consumes this

`/ioc-hunt <indicator>` should query both sections and report:

- **Actor-attributed hit**: indicator value found in `lookup`,
  show `actors[]` from the entry
- **Unattributed cluster hit**: indicator value found in
  `unattributed_lookup`, show `clusters[]` from the entry plus
  the cluster's `provenance_sources`
- **Both**: surface both, flag as "potential cross-walk — Hard Rule 2
  forbids automatic attribution; investigate"
- **Neither**: indicator not in corpus

## Doctrine references

- `CLAUDE.md` Hard Rule 2: no attribution origination
- `doctrine/INTEL-GRADING.md`: source / cluster grading
- `doctrine/ACTOR-PROFILE-STANDARD.md`: when to scaffold a new actor
  vs. file as unattributed
