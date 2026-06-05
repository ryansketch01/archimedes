"""
Runtime field updates for source-health.yaml following the 2026-05-31
00:00 EDT canonical scheduled FLASH sweep (Sat→Sun rollover, quiet hours
active). Same documentation/script pattern as prior runtime-update-*.py
scratch files (e.g. source-health.yaml.runtime-update-pm-20260520.py).

Applies surgical runtime-field-only updates using ruamel.yaml round-trip
to preserve all operator-set notes verbatim per the Hard Rule on
source-health field ownership.

Changes applied:
  sources.mandiant:
    last_successful_fetch: 2026-05-07T15:30:00-04:00 → 2026-05-31T00:05:00-04:00
                            (alt endpoint mandiant.com/resources/blog/rss.xml
                             status 200, 20 items at 2026-05-31T00:05)
    failure_count: 19 → 20  (feedburner.com/Mandiant 404, 30th consecutive)
    last_error: refreshed text reflecting 30th-consecutive count and
                alt-endpoint canonical-swap decision overdue.

All other sources: no runtime field changes this sweep (clean sweep with
zero state changes beyond mandiant's continued feedburner pattern; per
established intermittent-bump convention many entries' last_successful_fetch
already lags the sweep date and is updated only on meaningful state change).

File-level last_updated: held at 2026-05-19T07:30:00-04:00 per established
intermittent-bump convention; collector documents but does not advance
unilaterally without operator instruction.

Volexity transient parse error this sweep (single failure) — NOT incrementing
failure_count per the AM-30 recovery streak-reset; carried as awareness in
diff-summary only.

Usage:
    cd C:\\Users\\rtske\\Projects\\archimedes
    uv run --with ruamel.yaml python infrastructure/source-health.yaml.runtime-update-flash-0000-20260531.py
"""
from pathlib import Path
from ruamel.yaml import YAML


def main() -> None:
    p = Path("infrastructure/source-health.yaml")
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 100000  # do not wrap long single-line notes strings
    yaml.indent(mapping=2, sequence=4, offset=2)

    with p.open(encoding="utf-8") as f:
        data = yaml.load(f)

    m = data["sources"]["mandiant"]
    m["last_successful_fetch"] = "2026-05-31T00:05:00-04:00"
    m["failure_count"] = 20
    m["last_error"] = (
        "feedburner.com/Mandiant returned 404 on 2026-05-31T00:00 FLASH — "
        "thirtieth consecutive failure (failure_count incremented 19→20). "
        "Held healthy pending operator alt-endpoint canonical-swap decision. "
        "ALT-ENDPOINT mandiant.com/resources/blog/rss.xml continues to validate "
        "(status 200, 20 items in feed at 2026-05-31T00:05; 0 in-window items "
        "this sweep — Saturday→Sunday overnight quiet cadence). Feedburner path "
        "30 consecutive failures; alt path now validated across AM-30 + PM-30 "
        "+ evening-30 sentinel + this midnight sweep. Operator decision overdue."
    )

    with p.open("w", encoding="utf-8", newline="\n") as f:
        yaml.dump(data, f)

    print(
        "mandiant entry updated: failure_count=20, "
        "last_successful_fetch=2026-05-31T00:05:00-04:00"
    )


if __name__ == "__main__":
    main()
