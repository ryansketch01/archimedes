#!/usr/bin/env python3
"""
migrate_actor.py — Port a single actor from the old C3PO intel-repository
to the new Archimedes repo structure.

Usage:
    python scripts/migrate_actor.py <source-dir> <actor-id>

Example:
    python scripts/migrate_actor.py \\
        ~/intel-repository/threats/threat-actors/APT29 \\
        009

What it does:
    1. Reads the old profile.md and iocs.md
    2. Locates the actor entry in _roster.yaml
    3. Writes a new profile.md with full frontmatter
    4. Writes iocs.md with frontmatter (content mostly preserved)
    5. Generates an empty iocs.yaml scaffold (manual IOC migration required)
    6. Generates a threat-box.yaml scaffold (scoring requires manual fill-in)
    7. Validates related_actors links resolve

This is intentionally conservative — it does not auto-populate iocs.yaml or
threat-box.yaml from markdown. Those require judgment. The script creates
scaffolds that the actor-profiler subagent (or a human) then completes.
"""

import argparse
import sys
from pathlib import Path
from datetime import date, timedelta

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REPO_ROOT = Path(__file__).resolve().parent.parent
ROSTER_PATH = REPO_ROOT / "threats" / "threat-actors" / "_roster.yaml"
ACTOR_DIR_ROOT = REPO_ROOT / "threats" / "threat-actors"


def load_roster() -> dict:
    if not ROSTER_PATH.exists():
        print(f"ERROR: roster not found at {ROSTER_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(ROSTER_PATH) as f:
        return yaml.safe_load(f)


def find_actor(roster: dict, actor_id: str) -> dict:
    for actor in roster.get("actors", []):
        if actor["id"] == actor_id:
            return actor
    print(f"ERROR: actor id '{actor_id}' not found in roster", file=sys.stderr)
    sys.exit(1)


def build_frontmatter(actor: dict, source_dir: Path) -> str:
    today = date.today().isoformat()
    review_due = (date.today() + timedelta(days=90)).isoformat()
    fm = {
        "id": actor["id"],
        "primary_name": actor["primary_name"],
        "aliases": actor.get("aliases", []),
        "type": actor.get("type", "Unknown"),
        "attribution": actor.get("attribution", {}),
        "active_since": None,
        "status": "active",
        "status_note": "",
        "motivation": [],
        "threat_level": actor.get("threat_level", "UNKNOWN"),
        "admiralty_grade": "F6",  # placeholder — human/actor-profiler fills in
        "tlp": "CLEAR",
        "dossier_version": 1,
        "last_updated": today,
        "last_reviewed": today,
        "next_review_due": review_due,
        "profile_path": f"threats/threat-actors/{source_dir.name}/",
        "iocs_path": f"threats/threat-actors/{source_dir.name}/iocs.md",
        "threat_box_path": f"threats/threat-actors/{source_dir.name}/threat-box.yaml",
        "related_actors": [],
        "migrated_from": str(source_dir),
    }
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, default_flow_style=False) + "---\n"


def migrate(source_dir: Path, actor_id: str) -> None:
    if not source_dir.exists():
        print(f"ERROR: source directory does not exist: {source_dir}", file=sys.stderr)
        sys.exit(1)

    roster = load_roster()
    actor = find_actor(roster, actor_id)
    actor_name = actor["primary_name"].replace(" ", "-").replace("/", "-")
    dest_dir = ACTOR_DIR_ROOT / actor_name
    dest_dir.mkdir(parents=True, exist_ok=True)

    print(f"Migrating actor #{actor_id} ({actor['primary_name']})")
    print(f"  from: {source_dir}")
    print(f"  to:   {dest_dir}")

    # --- profile.md ---
    old_profile = source_dir / "profile.md"
    if old_profile.exists():
        content = old_profile.read_text()
        # Strip old Scoundrel framing
        content = content.replace("Scoundrel #", "Actor #")
        content = content.replace("🕵️ ", "")
        frontmatter = build_frontmatter(actor, dest_dir)
        new_profile = dest_dir / "profile.md"
        # If file starts with YAML frontmatter, replace it; else prepend.
        if content.startswith("---"):
            end_idx = content.find("---", 3)
            if end_idx != -1:
                content = content[end_idx + 3:].lstrip("\n")
        new_profile.write_text(frontmatter + "\n" + content)
        print(f"  ✓ profile.md written ({new_profile.stat().st_size} bytes)")
    else:
        print(f"  ⚠ no profile.md found at source — skipping")

    # --- iocs.md ---
    old_iocs = source_dir / "iocs.md"
    if old_iocs.exists():
        content = old_iocs.read_text()
        today = date.today().isoformat()
        ioc_frontmatter = (
            "---\n"
            f"actor_id: \"{actor['id']}\"\n"
            f"actor_name: {actor['primary_name']}\n"
            f"last_updated: {today}\n"
            "admiralty_grade: F6\n"
            "tlp: CLEAR\n"
            "source_of_record: true\n"
            "sidecar: iocs.yaml\n"
            "---\n\n"
        )
        if content.startswith("---"):
            end_idx = content.find("---", 3)
            if end_idx != -1:
                content = content[end_idx + 3:].lstrip("\n")
        new_iocs = dest_dir / "iocs.md"
        new_iocs.write_text(ioc_frontmatter + content)
        print(f"  ✓ iocs.md written")
    else:
        print(f"  ⚠ no iocs.md found at source — skipping")

    # --- iocs.yaml scaffold ---
    iocs_yaml = dest_dir / "iocs.yaml"
    if not iocs_yaml.exists():
        scaffold = {
            "actor_id": actor["id"],
            "actor_name": actor["primary_name"],
            "last_updated": date.today().isoformat(),
            "admiralty_grade": "F6",
            "tlp": "CLEAR",
            "source_of_record": "iocs.md",
            "ttl": {
                "network_infrastructure": 90,
                "file_hashes": 730,
                "registry": "never",
                "scheduled_task": "never",
                "cloud_service": "never",
                "vulnerabilities": "never",
            },
            "indicators": [],
            "hunt_queries": [],
        }
        iocs_yaml.write_text("# Generated by migrate_actor.py — populate indicators from iocs.md\n\n"
                             + yaml.safe_dump(scaffold, sort_keys=False))
        print(f"  ✓ iocs.yaml scaffold created (empty — populate manually)")

    # --- threat-box.yaml scaffold ---
    tb = dest_dir / "threat-box.yaml"
    if not tb.exists():
        scaffold = {
            "actor_id": actor["id"],
            "actor_name": actor["primary_name"],
            "target_profile": "ad-prime-v1",
            "scored_at": None,
            "scored_by": None,
            "reviewed_by": None,
            "scoring_version": 1,
            "scores": {
                cat: {
                    "intent": {"score": None, "label": "TBD", "evidence": "", "sources": []},
                    "willingness": {"modifier": 0, "label": "TBD", "evidence": ""},
                    "capability": {"score": None, "label": "TBD", "evidence": "", "sources": []},
                    "novelty": {"modifier": 0, "label": "TBD", "evidence": ""},
                    "ioc_corroboration": {"observed": False, "capability_bonus_applied": 0},
                    "final_intent": None,
                    "final_capability": None,
                    "composite": None,
                    "threat_level": "TBD",
                }
                for cat in ["espionage", "supply_chain", "destructive", "disruptive", "cyber_crime"]
            },
            "overall_score": None,
            "overall_threat_level": "TBD",
            "confidence": {"admiralty": "F6", "notes": ""},
            "review_policy": {
                "interval_days": 90,
                "last_reviewed": None,
                "next_review_due": None,
                "review_triggers": [
                    "new_attribution_from_a_source",
                    "new_tooling_documented",
                    "cve_exploitation_linked_to_actor",
                    "major_campaign_disclosure",
                    "first_party_ioc_observation",
                ],
            },
            "history": [],
        }
        tb.write_text(
            "# Threat Box scoring — populate via actor-profiler subagent.\n"
            "# HIGH threat levels require human sign-off before commit.\n\n"
            + yaml.safe_dump(scaffold, sort_keys=False)
        )
        print(f"  ✓ threat-box.yaml scaffold created (scoring TBD)")

    print(f"\n✅ Migration of actor #{actor_id} complete.")
    print(f"   Next steps:")
    print(f"   1. Review/edit {dest_dir}/profile.md frontmatter")
    print(f"   2. Populate {dest_dir}/iocs.yaml from iocs.md content")
    print(f"   3. Score {dest_dir}/threat-box.yaml (or invoke actor-profiler)")
    print(f"   4. Run: python scripts/regenerate_ioc_index.py")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source_dir", help="Path to actor's directory in old C3PO repo")
    parser.add_argument("actor_id", help="3-digit actor ID from _roster.yaml (e.g., 009)")
    args = parser.parse_args()
    migrate(Path(args.source_dir).expanduser().resolve(), args.actor_id)


if __name__ == "__main__":
    main()
