# scratch: 2026-05-20 PM pre-brief runtime update script (do not commit; gitignored region)
# Records the exact runtime-field changes made by the 2026-05-20 15:30 EDT pre-brief sweep.
#
# Sources updated (last_successful_fetch bumped to 2026-05-20T15:30:00-04:00):
#   - cisa-advisories      (one in-window KEV-add alert surfaced, productive)
#   - cisa-kev             (7 in-window additions, productive — pm-001)
#   - nvd                  (6 in-window CRITICAL records returned; 1 raw-signaled as pm-002, 5 discarded)
#   - mstic                (2 in-window items, both awareness/discarded; reachable)
#   - unit42               (0 in-window items, reachable)
#   - sans-isc             (0 in-window items, reachable)
#   - krebs                (0 in-window items, reachable)
#   - the-record           (5 in-window items, 0 substantive, reachable)
#   - bleepingcomputer     (3 in-window items, 1 substantive net-new = pm-004)
#   - securityweek         (5 in-window items, 1 substantive net-new = pm-003)
#   - thehackernews        (5 in-window items, 0 substantive net-new — all anti-noise/awareness)
#   - rapid7               (1 in-window item, marketing-filtered, reachable)
#   - sentinelone          (1 in-window item, marketing-filtered, reachable)
#   - sophos               (0 in-window items, reachable)
#   - welivesecurity       (0 in-window items, reachable)
#   - crowdstrike          (10 items, dateless marketing pattern continues; reachable)
#   - wired-security       (not invoked this sweep)
#
# File-level last_updated bumped to 2026-05-20T15:30:00-04:00.
#
# No failure_count / status / stale_since / last_error / notes fields were modified this sweep.
# Notes preserved verbatim per operator-set field-ownership policy.
#
# Carry-forward failures with no source-health change required this sweep:
#   - mandiant feedburner persistent 404 (~22nd consecutive, held healthy per operator-set
#     instruction pending alt-endpoint decision)
#   - dragos /blog/feed/ 404 (failure_count=1, held healthy per operator-set instruction)
#   - cisco-talos /feeds/posts/default 404 (failure_count=2 from 2026-05-19 07:30; held
#     healthy per operator-set instruction)
#   - msrc.microsoft.com/blog/feed XML parse failure (carry-forward)
#   - industrialcyber.co/feed/ 403 WAF/Akamai (carry-forward)
#   - security.com/threat-intelligence/feed 404 (carry-forward)
#   - wiz.io/blog/feed.xml 404 (first observation this sweep — does not yet have a top-level
#     source-health entry; collector flags for next-pass first-entry creation)
#   - socket.dev/blog/rss.xml 404 (first observation this sweep — confirms the 2026-05-16
#     productive-miss pattern recorded against the existing socket entry)
#
# 49th consecutive sweep with dormant non-self-telemetry Splunk pattern across both
# archimedes + defenseclaw_local indexes. Per the existing Splunk source-health notes
# convention this constitutes a confirming observation, not a state change.
