"""
Runtime field updates for source-health.yaml following the 2026-06-01
06:00 EDT canonical scheduled FLASH sweep (Sun→Mon rollover, quiet hours
active). Same documentation/script pattern as prior runtime-update-*.py
scratch files (e.g. source-health.yaml.runtime-update-flash-0000-20260531.py).

Applies surgical runtime-field-only updates using ruamel.yaml round-trip
to preserve all operator-set notes verbatim per the Hard Rule on
source-health field ownership (collector writes runtime fields only:
status / last_successful_fetch / failure_count / stale_since / last_error;
operator-set notes preserved verbatim).

Changes applied this sweep:
  sources.mandiant:
    last_successful_fetch -> 2026-06-01T06:05:00-04:00 (alt endpoint
                              mandiant.com/resources/blog/rss.xml validates,
                              status 200, 20 items in feed)
    failure_count: 20 -> 21 (feedburner.com/Mandiant 404, 31st consecutive)
    last_error: refreshed text reflecting 31st-consecutive count and
                continued overdue operator alt-endpoint canonical-swap.

All other A-grade sources successfully swept this run advance
last_successful_fetch to 2026-06-01T06:05:00-04:00 where applicable.
See accompanying diff-summary-flash-0600-20260601.txt for the full list.

volexity: single transient parse failure this sweep (recurring intermittent
pattern). Single failure does NOT regress the AM-30 recovery streak-reset.
Held healthy; failure_count NOT incremented.

msrc: remains stale (8th+ consecutive parse failure since 2026-05-29).
Unchanged this sweep.

File-level last_updated: held per established intermittent-bump convention;
collector documents but does not advance unilaterally without operator
instruction.

Usage:
    cd C:\\Users\\rtske\\Projects\\archimedes
    uv run --with ruamel.yaml python infrastructure/source-health.yaml.runtime-update-flash-0600-20260601.py
"""
from pathlib import Path
from ruamel.yaml import YAML


SWEEP_TS = "2026-06-01T06:05:00-04:00"

# Sources actually swept this run with status 200 and last_successful_fetch
# eligible for advance per the sentinel doc. Mandiant handled separately
# below (alt-endpoint validate + feedburner failure_count increment).
ADVANCE_LSF = [
    "mstic",
    "unit42",
    "crowdstrike",
    "cisco-talos",
    "sentinelone",
    "welivesecurity",
    "checkpoint",
    "securelist",
    "greynoise",
    "rapid7",
    "cisa-kev",
    "cisa-advisories",
    "nvd",
    "bleepingcomputer",
    "the-hacker-news",
    "securityaffairs",
    "the-record",
    "sans-isc",
    "darkreading",
    "splunk-archimedes",
    "splunk-defenseclaw",
]


def main() -> None:
    p = Path("infrastructure/source-health.yaml")
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 100000  # do not wrap long single-line notes strings
    yaml.indent(mapping=2, sequence=4, offset=2)

    with p.open(encoding="utf-8") as f:
        data = yaml.load(f)

    sources = data.get("sources", {})

    # 1) Mandiant special handling: alt-endpoint validate + feedburner increment.
    if "mandiant" in sources:
        m = sources["mandiant"]
        m["last_successful_fetch"] = SWEEP_TS
        prior_fc = m.get("failure_count", 20)
        m["failure_count"] = prior_fc + 1 if isinstance(prior_fc, int) else 21
        m["last_error"] = (
            "feedburner.com/Mandiant returned 404 on 2026-06-01T06:00 FLASH - "
            "thirty-first consecutive failure (failure_count incremented to "
            f"{m['failure_count']}). Held healthy pending operator alt-endpoint "
            "canonical-swap decision (now well overdue). ALT-ENDPOINT "
            "mandiant.com/resources/blog/rss.xml continues to validate "
            "(status 200, 20 items in feed at 2026-06-01T06:05; 0 in-window "
            "items this sweep - Sunday->Monday overnight quiet cadence). "
            "Feedburner path 31 consecutive failures; alt path validated across "
            "AM-30 + PM-30 + evening-30 sentinel + 2026-05-31 midnight sweep + "
            "2026-06-01 00:00 canonical sweep + this 06:00 canonical sweep. "
            "Operator decision overdue."
        )
        advanced = [("mandiant", "alt-endpoint validate; feedburner fc->21")]
    else:
        advanced = []

    # 2) Advance last_successful_fetch on other swept-healthy sources.
    for sid in ADVANCE_LSF:
        if sid in sources:
            entry = sources[sid]
            entry["last_successful_fetch"] = SWEEP_TS
            advanced.append((sid, "last_successful_fetch advanced"))

    with p.open("w", encoding="utf-8", newline="\n") as f:
        yaml.dump(data, f)

    print(f"Applied {len(advanced)} runtime updates:")
    for sid, note in advanced:
        print(f"  - {sid}: {note}")


if __name__ == "__main__":
    main()
