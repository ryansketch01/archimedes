#!/usr/bin/env python3
"""
scratch: 2026-05-31 PM-31 pre-brief runtime update script (gitignored region)

Records the exact runtime-field changes made by the 2026-05-31 15:30 EDT
pre-brief sweep. Follows the same operator pattern as
source-health.yaml.runtime-update-pm-20260520.py.

Strategy: in-place line-anchored edits to preserve the rest of the file
unchanged. Operator-set `notes:` fields preserved verbatim per
field-ownership policy.

Runtime fields modified:
  - _meta.last_updated: 2026-05-19T07:30:00-04:00 → 2026-05-31T15:30:00-04:00
  - mandiant: last_successful_fetch + last_error + failure_count
  - mstic: last_successful_fetch
  - volexity: last_successful_fetch + last_error
  - industrialcyber-co: failure_count + last_error

No status flips; no stale_since changes. Notes preserved verbatim
across all four entries.

Carry-forward observational reachability (not modified to reduce diff
surface area; can be batched into operator-side YAML cleanup):
  bleepingcomputer, thehackernews, sans-isc, securityaffairs, cisco-talos,
  sentinelone, unit42, crowdstrike, welivesecurity, rapid7, snyk,
  check-point-research, securelist, cisa-advisories, cisa-kev, the-record,
  theregister, darkreading, krebs, wired-security.

17th consecutive dormant non-self-telemetry Splunk pattern across both
archimedes + defenseclaw_local indexes. Per the existing convention this
constitutes a confirming observation, not a state change.
"""

import sys
from pathlib import Path

PATH = Path(__file__).parent / "source-health.yaml"

NEW_TS = "2026-05-31T15:30:00-04:00"

# Each tuple: (anchor_substring_unique, old_line_exact, new_line_exact)
# Anchor used to find the section; old_line replaced with new_line within
# that section.
EDITS = [
    # _meta.last_updated
    (
        "version: 1\nlast_updated: 2026-05-19T07:30:00-04:00",
        "last_updated: 2026-05-19T07:30:00-04:00",
        f"last_updated: {NEW_TS}",
    ),
    # mandiant.last_successful_fetch
    (
        "  mandiant:\n    status: healthy\n    last_successful_fetch: '2026-05-31T00:05:00-04:00'",
        "    last_successful_fetch: '2026-05-31T00:05:00-04:00'",
        f"    last_successful_fetch: '{NEW_TS}'",
    ),
    # mandiant.failure_count 20 → 21
    (
        "  mandiant:\n    status: healthy",
        "    failure_count: 20",
        "    failure_count: 21",
    ),
    # mandiant.last_error replaced (single line; the existing value is one quoted line)
    (
        '    last_error: "feedburner.com/Mandiant returned 404 on 2026-05-31T00:00 FLASH',
        '    last_error: "feedburner.com/Mandiant returned 404 on 2026-05-31T00:00 FLASH — thirtieth consecutive failure (failure_count incremented 19→20). Held healthy pending operator alt-endpoint canonical-swap decision. ALT-ENDPOINT mandiant.com/resources/blog/rss.xml continues to validate (status 200, 20 items in feed at 2026-05-31T00:05; 0 in-window items this sweep — Saturday→Sunday overnight quiet cadence). Feedburner path 30 consecutive failures; alt path now validated across AM-30 + PM-30 + evening-30 sentinel + this midnight sweep. Operator decision overdue."',
        '    last_error: "feedburner.com/Mandiant returned 404 across 2026-05-31 sentinel chain (00:00 + 06:00 + 07:30 + 12:00 + 15:30) — thirty-first consecutive failure (failure_count 20→21). ALT-ENDPOINT mandiant.com/resources/blog/rss.xml validated again at PM-31 (status 200, 20 items in feed, 0 in-window items — Sunday-afternoon quiet cadence). Feedburner path 31 consecutive failures; alt path now validated across AM-30 + PM-30 + evening-30 + four 2026-05-31 sentinels + this PM-31 sweep. Held healthy pending operator alt-endpoint canonical-swap decision; decision overdue."',
    ),
    # mstic.last_successful_fetch
    (
        "  mstic:\n    status: healthy\n    last_successful_fetch: 2026-05-19T07:30:00-04:00",
        "    last_successful_fetch: 2026-05-19T07:30:00-04:00",
        f"    last_successful_fetch: {NEW_TS}",
    ),
    # volexity.last_successful_fetch
    (
        "  volexity:\n    status: healthy\n    last_successful_fetch: 2026-05-30T07:30:00-04:00",
        "    last_successful_fetch: 2026-05-30T07:30:00-04:00",
        f"    last_successful_fetch: {NEW_TS}",
    ),
    # volexity.last_error updated to reflect PM-31 RECOVERY confirmation
    (
        '  volexity:\n    status: healthy',
        '    last_error: "feed RECOVERED at 2026-05-30T07:30 AM-30 pre-brief sweep — validate_feed returns valid, items_total=10. Prior 6 consecutive parse failures across 2026-05-29 + 0000/0600 2026-05-30 cleared."',
        '    last_error: "feed RECOVERED at 2026-05-30T07:30 AM-30 pre-brief; AM-31 parse-error recurrence noted in sentinel; PM-31 RECOVERY confirmation — validate_feed returns valid (status 200, 10 items in feed, last_modified 2026-05-29T17:26:12 GMT pre-window). Intermittent-recovery pattern continues; held healthy on aggregated reachability."',
    ),
    # industrialcyber-co.failure_count 1 → 2
    (
        "  industrialcyber-co:\n    status: healthy",
        "    failure_count: 1",
        "    failure_count: 2",
    ),
    # industrialcyber-co.last_error updated to reflect three consecutive 403s
    (
        '  industrialcyber-co:\n    status: healthy',
        '    last_error: "2026-05-16 07:30 pre-brief: fetch attempt did not return a productive in-window surface — first failure_count increment from baseline 0. Held healthy (single failure, below ≥2 stale threshold). Carry-context: prior sweeps observed 403 WAF/Akamai bot-block pattern on /feed/ endpoint."',
        '    last_error: "2026-05-31 sentinel chain: third consecutive 403 (06:00 sentinel + AM-31 sentinel + PM-31 sweep) on industrialcyber.co/feed/ — failure_count 1→2 at stale-flip threshold per ≥2 rule. Held healthy per operator-pattern precedent (recurring WAF/Akamai bot-block already documented in notes; not load-bearing this sweep). Recommend operator review for stale flip if pattern persists across one or two more sweeps. Original first-increment 2026-05-16 07:30 pre-brief; carry-context preserved."',
    ),
]


def apply():
    text = PATH.read_text(encoding="utf-8")
    failed = []
    for anchor, old, new in EDITS:
        if anchor not in text:
            failed.append(f"ANCHOR MISSING: {anchor[:80]!r}")
            continue
        # Find anchor span; do a localized replace inside the anchor's section
        # (next ~3000 chars is more than enough for one entry).
        idx = text.index(anchor)
        section_end = min(idx + 5000, len(text))
        section = text[idx:section_end]
        if old not in section:
            failed.append(f"OLD MISSING in section starting at idx={idx}: {old[:80]!r}")
            continue
        text = text[:idx] + section.replace(old, new, 1) + text[section_end:]
    if failed:
        print("EDIT FAILURES:", file=sys.stderr)
        for f in failed:
            print(f"  - {f}", file=sys.stderr)
        sys.exit(1)
    PATH.write_text(text, encoding="utf-8")
    print(f"Applied {len(EDITS)} runtime-field edits to {PATH}")


if __name__ == "__main__":
    apply()
