#!/usr/bin/env python3
"""
Runtime-update script for source-health.yaml — 2026-06-01 AM-1 pre-brief
collector pass.

This script performs surgical, runtime-only updates on the source-health.yaml
file per the collector field-ownership rule: ONLY the runtime fields
(status, last_successful_fetch, failure_count, stale_since, last_error)
are touched. Operator-set fields (notes and any unrecognized keys) are
preserved VERBATIM by virtue of ruamel.yaml's round-trip preservation.

Per the AM-1 sentinel raw-signal raw-2026-06-01-am-000-...md, the following
runtime updates apply:

1. Sources productively swept at AM-1 — advance last_successful_fetch to
   2026-06-01T07:30:00-04:00 (preserve all other runtime/non-runtime fields):
     cisa-advisories, cisa-kev, nvd, crowdstrike, mstic, unit42,
     sans-isc, the-record, bleepingcomputer, securityweek, rapid7,
     sentinelone, cisco-talos

2. mandiant — last_successful_fetch advanced (alt endpoint validates),
   failure_count 21→22 (feedburner unchanged 404), last_error updated to
   note 32nd consecutive failure.

3. industrialcyber-co — failure_count 1→2 on first AM-1 sweep observation
   of 403 from rss-bridge MCP path; per >=2 stale threshold, flip
   status: stale, stale_since: 2026-06-01. last_error updated.

NEW first-time entries bootstrapped (collector-driven per the librarian's
2026-05-19 doctrine note that thehackernews + darkreading should get
collector-bootstrapped entries rather than librarian-speculative):

4. theregister — first-entry, productive AM-1 sweep (2 in-window items,
   both discarded per Mode 1).
5. darkreading — first-entry, productive AM-1 sweep (2 in-window events-
   page items, discarded per Mode 1).
6. thehackernews — first-entry, productive AM-1 sweep (0 fresh items
   beyond FLASH-0600).
7. securelist — first-entry, productive AM-1 sweep (1 in-window item
   already evaluated and discarded at FLASH-0600).
8. securityaffairs — first-entry, productive AM-1 sweep (0 fresh items
   beyond FLASH-0600).
9. checkpoint-research — first-entry, productive AM-1 sweep (0 in-window
   items).
10. welivesecurity — first-entry, productive AM-1 sweep (0 in-window items).
11. greynoise — first-entry, productive AM-1 sweep (0 in-window items).

(volexity already has a top-level entry; single transient parse failure
this sweep does not regress per its existing operator note.)

Top-level last_updated bumped to 2026-06-01T07:30:00-04:00.
"""

import sys
from pathlib import Path

try:
    from ruamel.yaml import YAML
except ImportError:
    print("ERROR: ruamel.yaml not installed. Run: uv run --with ruamel.yaml python ...")
    sys.exit(1)

HEALTH_PATH = Path(r"C:\Users\rtske\Projects\archimedes\infrastructure\source-health.yaml")
NEW_TS = "2026-06-01T07:30:00-04:00"

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.width = 100000  # avoid wrapping long single-line strings (notes)

data = yaml.load(HEALTH_PATH.read_text(encoding="utf-8"))

# Top-level bookkeeping
data["last_updated"] = NEW_TS

sources = data["sources"]

# Group 1 — sources productively swept at AM-1; advance last_successful_fetch
productive_swept = [
    "cisa-advisories",
    "cisa-kev",
    "nvd",
    "crowdstrike",
    "mstic",
    "unit42",
    "sans-isc",
    "the-record",
    "bleepingcomputer",
    "securityweek",
    "rapid7",
    "sentinelone",
    "cisco-talos",
]

for sid in productive_swept:
    if sid in sources:
        sources[sid]["last_successful_fetch"] = NEW_TS
        # Defensive: ensure failure_count stays at 0 if it was already 0
        # (do NOT zero out non-zero counts — those reflect documented patterns)
    else:
        print(f"WARN: {sid} not found in sources; skipping")

# Group 2 — mandiant: bump failure_count, update last_error
if "mandiant" in sources:
    sources["mandiant"]["last_successful_fetch"] = NEW_TS  # alt endpoint validates
    sources["mandiant"]["failure_count"] = 22
    sources["mandiant"]["last_error"] = (
        "feedburner.com/Mandiant returned 404 on 2026-06-01T07:30 AM-1 pre-brief sweep - "
        "thirty-second consecutive failure (failure_count incremented to 22). Held healthy "
        "pending operator alt-endpoint canonical-swap decision (now approximately one week "
        "past actionable threshold). ALT-ENDPOINT mandiant.com/resources/blog/rss.xml continues "
        "to validate (status 200, 20 items in feed at 2026-06-01T07:30; 0 in-window items this "
        "sweep - Sunday->Monday overnight quiet cadence carry-over). Feedburner path 32 "
        "consecutive failures across AM-30 + PM-30 + evening-30 sentinel + 2026-05-31 midnight "
        "sweep + 2026-06-01 00:00 canonical sweep + 06:00 canonical sweep + this AM-1 "
        "pre-brief sweep. Operator decision overdue."
    )

# Group 3 — industrialcyber-co: bump failure_count and flip stale
if "industrialcyber-co" in sources:
    sources["industrialcyber-co"]["failure_count"] = 2
    sources["industrialcyber-co"]["status"] = "stale"
    sources["industrialcyber-co"]["stale_since"] = "2026-06-01"
    sources["industrialcyber-co"]["last_error"] = (
        "2026-06-01T07:30 AM-1 pre-brief sweep: industrialcyber.co/feed/ returned 403 "
        "via rss-bridge MCP path (Feed host rejected request - 403). SECOND tracked "
        "failure (first was 2026-05-16 07:30 pre-brief). STALE FLIP per failure_count "
        ">=2 rule. Carry-context from prior operator notes: WAF/Akamai bot-block pattern "
        "previously observed on /feed/ endpoint; this is consistent with that pattern "
        "recurring. Operator action: verify whether industrialcyber.co/feed/ still serves "
        "RSS or has permanently restricted to authenticated access, or whether an alt "
        "User-Agent / Accept header workaround is required. WebFetch fallback against "
        "industrialcyber.co article URLs remains operational when specific stories need "
        "retrieval; the bulk-RSS-sweep path is the broken layer."
    )

# Group 4 — bootstrap new first-entries for sources swept AM-1 without prior records
def bootstrap_entry(notes_msg: str):
    return {
        "status": "healthy",
        "last_successful_fetch": NEW_TS,
        "failure_count": 0,
        "stale_since": None,
        "last_error": None,
        "notes": notes_msg,
    }

bootstrap_targets = {
    "thehackernews": (
        "First top-level entry created 2026-06-01 07:30 AM-1 pre-brief sweep "
        "(per collector-driven first-entry doctrine in 2026-05-19 librarian note). "
        "RSS feed feeds.feedburner.com/TheHackersNews reachable (status 200, "
        "last_modified 2026-06-01T11:04 GMT = 07:04 EDT inside window from feed-server "
        "activity). 0 fresh in-window items beyond FLASH-0600 already-evaluated set "
        "(WP Maps Pro WordPress plugin item 04:45 EDT publish discarded at FLASH-0600 "
        "per Mode 1). Healthy on first track."
    ),
    "theregister": (
        "First top-level entry created 2026-06-01 07:30 AM-1 pre-brief sweep. "
        "RSS feed theregister.com/security/headlines.atom reachable (status 200, "
        "50 items in feed). 2 in-window items fetched and evaluated, both DISCARDED "
        "per Mode 1: (1) Password manager Dashlane brute-force attacks (consumer-tier, "
        "no roster/vuln-index hit); (2) UK government subsea cable protection / Russian "
        "GUGI submarine surveillance (physical/maritime national-security commentary, "
        "not cyber-TI). Healthy on first track."
    ),
    "darkreading": (
        "First top-level entry created 2026-06-01 07:30 AM-1 pre-brief sweep. "
        "RSS feed darkreading.com/rss.xml reachable (status 200, 50 items in feed). "
        "2 in-window items both events-page metadata (Name That Toon contest, "
        "Infosecurity Europe event listing); awareness-only with no body content. "
        "Both DISCARDED per Mode 1 (no threat-intel surface). Healthy on first track."
    ),
    "securelist": (
        "First top-level entry created 2026-06-01 07:30 AM-1 pre-brief sweep "
        "(productively swept earlier today at 2026-06-01 06:00 FLASH sentinel where "
        "'Containers on fire: from container escapes to supply chain attacks' was "
        "fetched, evaluated, and DISCARDED per Mode 1 — defensive container-attack-"
        "surface survey, TeamPCP cited illustratively only pointing at 2026-05-11 "
        "corpus surface VT-006 lineage; NO new attribution, NO new IOCs, NO new TTPs). "
        "Same Mode 1 rationale carries forward at AM-1. RSS feed securelist.com/feed/ "
        "reachable (status 200, 10 items in feed). Kaspersky-published research surface. "
        "Healthy on first track."
    ),
    "securityaffairs": (
        "First top-level entry created 2026-06-01 07:30 AM-1 pre-brief sweep. "
        "RSS feed securityaffairs.com/feed reachable (status 200, 10 items in feed). "
        "0 fresh in-window items beyond FLASH-0600 already-evaluated set (PAN-OS KEV "
        "relay 04:36 EDT + Pentagon location-data op-ed 03:18 EDT both discarded at "
        "FLASH-0600 per Mode 1 — anti-noise + non-cyber-TI). Pierluigi Paganini byline. "
        "Productive at PM-30 / PM-31 brief cycles on net-new-topics newsletter "
        "surfacing (PM-31 brief flagged Nimbus Manticore / Screening Serpens / Lazarus "
        "RemotePE / TrapDoor / Showboat as awareness items pending originating-primary "
        "surface). Healthy on first track."
    ),
    "checkpoint-research": (
        "First top-level entry created 2026-06-01 07:30 AM-1 pre-brief sweep. "
        "RSS feed research.checkpoint.com/feed/ reachable (status 200, 15 items in feed, "
        "last_modified 2026-05-26T12:13 GMT pre-window). 0 in-window items. Multi-day "
        "publication cadence. Nimbus Manticore Operation Epic Fury piece (2026-05-22) "
        "is the most-recent visible content; operator-flagged via PM-31 brief Security "
        "Affairs newsletter relay as awareness item pending /new-actor scaffolding "
        "decision outside AM-1 scope. Healthy on first track."
    ),
    "welivesecurity": (
        "First top-level entry created 2026-06-01 07:30 AM-1 pre-brief sweep. "
        "RSS feed welivesecurity.com/en/rss/feed/ reachable (status 200, 100 items in feed). "
        "0 in-window items. ESET research surface. Multi-day publication cadence at the "
        "threat-research tier. Healthy on first track."
    ),
    "greynoise": (
        "First top-level entry created 2026-06-01 07:30 AM-1 pre-brief sweep "
        "(productively swept at FLASH-0600 with last_modified 2026-05-31T22:37 GMT pre-"
        "window, 0 in-window items). 0 in-window items at AM-1 either. GreyNoise blog "
        "surface; opportunistic scanning telemetry intelligence. Healthy on first track."
    ),
}

# Use a small helper to insert in a stable position — append at end of `sources`
# mapping in YAML order. Existing entries are not reordered.
for sid, notes_msg in bootstrap_targets.items():
    if sid not in sources:
        sources[sid] = bootstrap_entry(notes_msg)

# Write back
with HEALTH_PATH.open("w", encoding="utf-8", newline="\n") as f:
    yaml.dump(data, f)

print(f"OK: source-health.yaml runtime-updated for AM-1 pre-brief (2026-06-01T07:30:00-04:00)")
print(f"  - productive_swept (timestamp advance): {len(productive_swept)} sources")
print(f"  - mandiant: failure_count 21->22 (feedburner 32nd consecutive 404; alt validates)")
print(f"  - industrialcyber-co: failure_count 1->2, STALE FLIP (WAF 403 recurrence)")
print(f"  - bootstrap new first-entries: {len(bootstrap_targets)} sources")
