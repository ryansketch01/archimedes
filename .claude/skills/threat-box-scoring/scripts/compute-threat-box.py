#!/usr/bin/env python3
"""
compute-threat-box.py — deterministic Threat Box math.

Called by the threat-box-scoring skill to compute final scores, composites,
threat levels, and authority level from raw inputs. The agent provides
judgment (evidence adequacy, source grading); this script provides arithmetic.

Usage:
    python scripts/compute-threat-box.py --input path/to/raw-scores.yaml
    cat raw-scores.yaml | python scripts/compute-threat-box.py --stdin

Input schema (YAML):
    actor_id: "006"
    actor_name: "APT28"
    target_profile: "ad-prime-v1"
    scored_at: "2026-04-23"
    scored_by: "actor-profiler"
    scores:
      espionage:
        intent: {score: 5, willingness_modifier: 0}
        capability: {score: 5, novelty_modifier: 0}
        ioc_corroboration: {observed: false, bonus_category: null}
      supply_chain: {...}
      destructive: {...}
      disruptive: {...}
      cyber_crime: {...}

Output: full threat-box.yaml structure with computed fields.

Exit codes:
    0 — scored successfully
    1 — input validation error
    2 — HIGH threat level detected; requires human sign-off (still returns YAML)
"""

import sys
import argparse
from datetime import date, timedelta

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


CATEGORIES = ["espionage", "supply_chain", "destructive", "disruptive", "cyber_crime"]

WEIGHTS = {
    "espionage": 0.35,
    "supply_chain": 0.20,
    "destructive": 0.15,
    "disruptive": 0.15,
    "cyber_crime": 0.15,
}

THRESHOLDS = [
    (8, 10, "HIGH"),
    (5, 7, "MEDIUM"),
    (2, 4, "LOW"),
]

REVIEW_INTERVAL_DAYS = 90


def validate_input(data):
    """Validate input has required fields and value ranges. Returns list of errors."""
    errors = []

    for field in ["actor_id", "actor_name", "target_profile", "scored_at", "scored_by", "scores"]:
        if field not in data:
            errors.append(f"missing required field: {field}")

    if "scores" not in data:
        return errors

    for category in CATEGORIES:
        if category not in data["scores"]:
            errors.append(f"missing score category: {category}")
            continue

        cat = data["scores"][category]

        # Intent validation
        intent = cat.get("intent", {})
        intent_score = intent.get("score")
        if intent_score not in range(1, 6):
            errors.append(f"{category}.intent.score must be 1-5, got {intent_score}")

        willingness = intent.get("willingness_modifier")
        if willingness not in [0, 1, 2]:
            errors.append(f"{category}.intent.willingness_modifier must be 0, 1, or 2, got {willingness}")

        # Capability validation
        capability = cat.get("capability", {})
        cap_score = capability.get("score")
        if cap_score not in range(1, 6):
            errors.append(f"{category}.capability.score must be 1-5, got {cap_score}")

        novelty = capability.get("novelty_modifier")
        if novelty not in [0, 1, 2]:
            errors.append(f"{category}.capability.novelty_modifier must be 0, 1, or 2, got {novelty}")

        # IOC corroboration
        ioc = cat.get("ioc_corroboration", {})
        if ioc.get("observed") and ioc.get("bonus_category") and ioc["bonus_category"] not in CATEGORIES:
            errors.append(f"{category}.ioc_corroboration.bonus_category invalid: {ioc['bonus_category']}")

    return errors


def clamp(value, low, high):
    """Clamp value to [low, high] range."""
    return max(low, min(high, value))


def compute_category(cat_data, category_name, global_ioc_bonus_for_category):
    """Compute final scores for one attack category."""

    intent_score = cat_data["intent"]["score"]
    willingness_mod = cat_data["intent"]["willingness_modifier"]

    cap_score = cat_data["capability"]["score"]
    novelty_mod = cat_data["capability"]["novelty_modifier"]

    # Final Intent = Intent Score - Willingness Modifier
    # Note: modifier is given as a positive number (0, 1, 2) and SUBTRACTED
    final_intent = clamp(intent_score - willingness_mod, 1, 5)

    # Final Capability = Capability Score - Novelty Modifier + IOC Corroboration Bonus
    ioc_bonus = 1 if global_ioc_bonus_for_category else 0
    final_capability = clamp(cap_score - novelty_mod + ioc_bonus, 1, 5)

    composite = final_intent + final_capability

    # Apply threshold table
    threat_level = None
    for low, high, label in THRESHOLDS:
        if low <= composite <= high:
            threat_level = label
            break

    return {
        "final_intent": final_intent,
        "final_capability": final_capability,
        "composite": composite,
        "threat_level": threat_level,
        "ioc_bonus_applied": ioc_bonus,
    }


def determine_overall_threat_level(overall_score):
    """Apply threshold table to the overall weighted score."""
    # Use ceiling of the float for threshold comparison — err toward caution
    rounded = round(overall_score)
    for low, high, label in THRESHOLDS:
        if low <= rounded <= high:
            return label
    return "UNKNOWN"


def determine_authority(overall_threat_level):
    """Per doctrine: who can commit this score."""
    return {
        "LOW": "actor-profiler-autonomous",
        "MEDIUM": "actor-profiler-autonomous-with-notification",
        "HIGH": "actor-profiler-proposes-human-confirms",
    }.get(overall_threat_level, "unknown")


def compute_review_dates(scored_at_str):
    """Compute next_review_due from scored_at."""
    try:
        scored_date = date.fromisoformat(scored_at_str)
    except (ValueError, TypeError):
        return {"last_reviewed": scored_at_str, "next_review_due": None}

    next_review = scored_date + timedelta(days=REVIEW_INTERVAL_DAYS)
    return {
        "last_reviewed": scored_date.isoformat(),
        "next_review_due": next_review.isoformat(),
    }


def compute_threat_box(input_data):
    """Main computation. Returns full threat-box.yaml structure."""

    errors = validate_input(input_data)
    if errors:
        return {"status": "validation_error", "errors": errors}

    # Determine per-category IOC bonuses
    ioc_bonuses = {cat: False for cat in CATEGORIES}
    for category in CATEGORIES:
        ioc = input_data["scores"][category].get("ioc_corroboration", {})
        if ioc.get("observed") and ioc.get("bonus_category") == category:
            ioc_bonuses[category] = True

    # Compute each category
    category_results = {}
    for category in CATEGORIES:
        cat_data = input_data["scores"][category]
        computed = compute_category(cat_data, category, ioc_bonuses[category])
        category_results[category] = {**cat_data, **computed}

    # Compute weighted overall score
    overall_score = sum(
        category_results[cat]["composite"] * WEIGHTS[cat]
        for cat in CATEGORIES
    )

    overall_threat_level = determine_overall_threat_level(overall_score)
    authority = determine_authority(overall_threat_level)

    # Review policy
    review = compute_review_dates(input_data["scored_at"])

    # Build output
    output = {
        "actor_id": input_data["actor_id"],
        "actor_name": input_data["actor_name"],
        "target_profile": input_data["target_profile"],
        "scored_at": input_data["scored_at"],
        "scored_by": input_data["scored_by"],
        "reviewed_by": None if overall_threat_level == "HIGH" else "auto-committed",
        "scoring_version": input_data.get("scoring_version", 1),
        "scores": category_results,
        "overall": {
            "weighted_score": round(overall_score, 2),
            "weights_used": WEIGHTS,
            "threat_level": overall_threat_level,
            "authority_level": authority,
        },
        "review_policy": {
            "interval_days": REVIEW_INTERVAL_DAYS,
            "last_reviewed": review["last_reviewed"],
            "next_review_due": review["next_review_due"],
            "review_triggers": [
                "new_attribution_from_a_source",
                "new_tooling_documented",
                "cve_exploitation_linked_to_actor",
                "major_campaign_disclosure",
                "first_party_ioc_observation",
            ],
        },
        "status": "scored_pending_approval" if overall_threat_level == "HIGH" else "scored",
    }

    return output


def main():
    parser = argparse.ArgumentParser(description="Compute Threat Box scores")
    parser.add_argument("--input", help="Path to input YAML file")
    parser.add_argument("--stdin", action="store_true", help="Read input from stdin")
    args = parser.parse_args()

    if args.stdin:
        input_data = yaml.safe_load(sys.stdin)
    elif args.input:
        with open(args.input) as f:
            input_data = yaml.safe_load(f)
    else:
        parser.error("must provide --input or --stdin")

    result = compute_threat_box(input_data)

    # Emit YAML to stdout
    print(yaml.safe_dump(result, sort_keys=False, default_flow_style=False))

    # Exit codes
    if result.get("status") == "validation_error":
        sys.exit(1)
    if result.get("status") == "scored_pending_approval":
        print("NOTE: HIGH threat level detected. Requires /approve-scoring before commit.",
              file=sys.stderr)
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
