"""Live SpiderFoot MCP test script — Session 13.

Runs a passive_scan against example.com using only DNS + WHOIS modules
(skips sfp_crt to avoid the slow per-cert iteration on busy domains).
Demonstrates the full MCP path end-to-end: policy validation,
start_scan, polling, /scaneventresults parsing, and aggregated output.
"""

from __future__ import annotations

import sys

from spiderfoot_mcp.config import load_config
from spiderfoot_mcp.policy import validate_modules
from spiderfoot_mcp.spiderfoot_client import SpiderFootClient


def main() -> int:
    cfg = load_config()
    modules = validate_modules(["sfp_dnsresolve", "sfp_whois"])
    print(f"modules after policy filter: {modules}", flush=True)

    with SpiderFootClient(cfg) as c:
        h = c.health()
        print(
            f"health: reachable={h.reachable} version={h.spiderfoot_version} "
            f"msg={h.message}",
            flush=True,
        )
        if not h.reachable:
            return 1

        out = c.run_passive_scan(
            target="example.com",
            modules=modules,
            scan_name="archimedes-live-test-v3",
        )
        print(f"scan_id: {out.scan_id}", flush=True)
        print(f"status: {out.status}", flush=True)
        print(f"duration: {out.duration_seconds}s", flush=True)
        print(f"events: {len(out.events)}", flush=True)
        print(
            f"distinct_domains: {len(out.distinct_domains)} -> "
            f"{out.distinct_domains[:8]}",
            flush=True,
        )
        print(
            f"distinct_ips: {len(out.distinct_ips)} -> {out.distinct_ips}",
            flush=True,
        )
        print(
            f"distinct_emails: {len(out.distinct_emails)} -> {out.distinct_emails}",
            flush=True,
        )
        print(
            "event types:", sorted({e.event_type for e in out.events}), flush=True
        )
        # Show first 3 events as a sanity check on parsing
        print("---first 3 events---", flush=True)
        for e in out.events[:3]:
            data_preview = e.data[:60] + ("..." if len(e.data) > 60 else "")
            print(
                f"  [{e.event_type}] {data_preview!r} via {e.source_module}",
                flush=True,
            )
        print(f"web_url: {out.web_url}", flush=True)
        return 0


if __name__ == "__main__":
    sys.exit(main())
