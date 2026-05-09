#!/usr/bin/env python3
"""
regenerate_ioc_index.py — Rebuild threats/iocs/_master-index.yaml from
every actor's iocs.yaml sidecar plus any unattributed IOC clusters.

This is intended to run:
  - Nightly via cron/systemd timer
  - After any actor profile update (invoked by the librarian subagent)
  - After an unattributed cluster is added or updated
  - Manually when debugging ioc-hunt discrepancies

Usage:
    python scripts/regenerate_ioc_index.py [--dry-run]

Behavior:
  - Walks threats/threat-actors/*/iocs.yaml (actor-attributed IOCs)
  - Walks threats/iocs/unattributed/*.yaml (cluster-keyed IOCs with
    no actor attribution — see the unattributed/ README for schema
    and Hard Rule 2 isolation rationale)
  - Builds two reverse-lookup dicts (actor lookup + unattributed
    lookup), kept separate so attributed and unattributed indicators
    are never conflated
  - Identifies cross-actor indicators (2+ actors share the same value)
  - Computes stats by type and KEV status for both buckets
  - Writes threats/iocs/_master-index.yaml (overwrites)

Hard Rule 2 (no attribution origination): the script never merges
unattributed cluster IOCs with actor IOCs. If the same indicator
appears in both, it shows up in both lookups separately — operator
investigates and decides on attribution.
"""

import argparse
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REPO_ROOT = Path(__file__).resolve().parent.parent
ACTOR_DIR = REPO_ROOT / "threats" / "threat-actors"
UNATTRIBUTED_DIR = REPO_ROOT / "threats" / "iocs" / "unattributed"
INDEX_PATH = REPO_ROOT / "threats" / "iocs" / "_master-index.yaml"


def collect_indicators() -> tuple[dict, dict]:
    """Walk actor directories, return (lookup_dict, stats)."""
    lookup = defaultdict(lambda: {"actors": [], "details": []})
    stats_by_type = defaultdict(int)
    kev_count = 0
    actors_with_iocs = 0

    for ioc_yaml in sorted(ACTOR_DIR.glob("*/iocs.yaml")):
        try:
            with open(ioc_yaml) as f:
                data = yaml.safe_load(f)
        except Exception as e:
            print(f"  WARNING: failed to parse {ioc_yaml}: {e}", file=sys.stderr)
            continue

        if not data:
            continue

        actor_id = data.get("actor_id")
        if not actor_id:
            continue

        has_indicators = False
        for ind in data.get("indicators", []) or []:
            has_indicators = True
            value = ind.get("value")
            if not value:
                continue
            ind_type = ind.get("type", "unknown")
            stats_by_type[ind_type] += 1

            entry = lookup[str(value)]
            if actor_id not in entry["actors"]:
                entry["actors"].append(actor_id)
            entry["type"] = ind_type
            if ind_type == "cve":
                entry["cvss"] = ind.get("cvss")
                entry["kev"] = ind.get("status") == "kev"
                entry["products"] = [ind.get("product")] if ind.get("product") else []
                if entry.get("kev"):
                    kev_count += 1
            if "role" in ind:
                entry["role"] = ind["role"]
            if "first_seen" in ind:
                entry["first_seen"] = ind["first_seen"]
            if "last_seen" in ind:
                entry["last_seen"] = ind["last_seen"]
            if "malware" in ind:
                entry["malware"] = ind["malware"]
            if "filename" in ind:
                entry["filename"] = ind["filename"]
            if "detection_note" in ind:
                entry["detection_note"] = ind["detection_note"]

        if has_indicators:
            actors_with_iocs += 1

    # Resolve cross-actor indicators
    cross_actor = {v: entry for v, entry in lookup.items() if len(entry["actors"]) > 1}

    stats = {
        "total_indicators": sum(stats_by_type.values()),
        "total_actors_with_iocs": actors_with_iocs,
        "by_type": dict(stats_by_type),
        "cross_actor_indicators": len(cross_actor),
        "kev_count": kev_count,
    }

    # Clean up internal details field
    clean_lookup = {}
    for v, entry in lookup.items():
        clean_lookup[v] = {k: val for k, val in entry.items() if k != "details"}

    return clean_lookup, stats, cross_actor


def collect_unattributed() -> tuple[dict, dict, dict]:
    """Walk threats/iocs/unattributed/*.yaml. Return (lookup, clusters, stats).

    Each file in unattributed/ is one IOC cluster with no actor attribution.
    Schema mirrors actor iocs.yaml but keys on `cluster_id` instead of
    `actor_id`. Indicators have the same shape (id, type, value, role,
    first_seen, source, etc.).

    Hard Rule 2 isolation: this function returns its own lookup dict,
    NEVER merged with actor-IOC lookup. If the same indicator value
    appears in both an actor and an unattributed cluster, it shows up
    in both lookups separately — operator investigates manually.
    """
    lookup: dict = defaultdict(lambda: {"clusters": []})
    clusters: dict = {}
    stats_by_type: dict = defaultdict(int)
    kev_count = 0

    if not UNATTRIBUTED_DIR.exists():
        # Bucket may not exist yet on a fresh checkout — treat as empty
        return {}, {}, {
            "total_indicators": 0,
            "total_clusters": 0,
            "by_type": {},
            "kev_count": 0,
        }

    for cluster_yaml in sorted(UNATTRIBUTED_DIR.glob("*.yaml")):
        # Skip the README schema example if it lives as a yaml; only
        # accept files with cluster_id at the top level
        try:
            with open(cluster_yaml, encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            print(f"  WARNING: failed to parse {cluster_yaml}: {e}", file=sys.stderr)
            continue

        if not data:
            continue

        cluster_id = data.get("cluster_id")
        if not cluster_id:
            continue

        cluster_indicators = data.get("indicators") or []
        clusters[cluster_id] = {
            "cluster_name": data.get("cluster_name"),
            "first_seen": data.get("first_seen"),
            "indicator_count": len(cluster_indicators),
            "provenance_sources": [
                p.get("source") for p in (data.get("provenance") or []) if isinstance(p, dict) and p.get("source")
            ],
        }

        for ind in cluster_indicators:
            value = ind.get("value")
            if not value:
                continue
            ind_type = ind.get("type", "unknown")
            stats_by_type[ind_type] += 1

            entry = lookup[str(value)]
            if cluster_id not in entry["clusters"]:
                entry["clusters"].append(cluster_id)
            entry["type"] = ind_type
            if ind_type == "cve":
                entry["cvss"] = ind.get("cvss")
                entry["kev"] = ind.get("status") == "kev"
                if entry.get("kev"):
                    kev_count += 1
            for passthrough in ("role", "first_seen", "last_seen", "source", "notes"):
                if passthrough in ind:
                    entry[passthrough] = ind[passthrough]

    stats = {
        "total_indicators": sum(stats_by_type.values()),
        "total_clusters": len(clusters),
        "by_type": dict(stats_by_type),
        "kev_count": kev_count,
    }

    return dict(lookup), clusters, stats


def write_index(
    lookup: dict,
    stats: dict,
    cross_actor: dict,
    unattributed_lookup: dict,
    unattributed_clusters: dict,
    unattributed_stats: dict,
    dry_run: bool,
) -> None:
    output = {
        "version": 2,  # bumped — schema now includes unattributed sections
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "generated_by": "scripts/regenerate_ioc_index.py",
        "stats": stats,
        "lookup": lookup,
        "cross_actor": list(cross_actor.keys()),
        "unattributed_stats": unattributed_stats,
        "unattributed_clusters": unattributed_clusters,
        "unattributed_lookup": unattributed_lookup,
    }

    dumped = yaml.safe_dump(output, sort_keys=False, default_flow_style=False, width=120)

    if dry_run:
        print("--- DRY RUN -- would write to:", INDEX_PATH)
        print(dumped[:2000] + ("\n... [truncated]" if len(dumped) > 2000 else ""))
        return

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(
        "# threats/iocs/_master-index.yaml\n"
        "# GENERATED FILE -- regenerated by scripts/regenerate_ioc_index.py\n"
        "# DO NOT HAND-EDIT.\n"
        "#\n"
        "# Two parallel sections:\n"
        "#   lookup / cross_actor              -- actor-attributed IOCs\n"
        "#   unattributed_lookup / _clusters   -- IOC clusters with no actor attribution yet\n"
        "# The two sections are isolated per Hard Rule 2 (no attribution origination).\n"
        "# Same indicator may appear in both sections; operator investigates.\n\n"
        + dumped
    )
    print(f"OK: Wrote {INDEX_PATH}")
    print(f"   Actor:        {stats['total_indicators']} indicators across "
          f"{stats['total_actors_with_iocs']} actors "
          f"({stats['cross_actor_indicators']} cross-actor, {stats['kev_count']} KEV)")
    print(f"   Unattributed: {unattributed_stats['total_indicators']} indicators across "
          f"{unattributed_stats['total_clusters']} clusters "
          f"({unattributed_stats['kev_count']} KEV)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Print what would be written, don't save")
    args = parser.parse_args()

    print(f"Walking {ACTOR_DIR}...")
    lookup, stats, cross_actor = collect_indicators()
    print(f"Walking {UNATTRIBUTED_DIR}...")
    un_lookup, un_clusters, un_stats = collect_unattributed()
    write_index(lookup, stats, cross_actor, un_lookup, un_clusters, un_stats, args.dry_run)


if __name__ == "__main__":
    main()
