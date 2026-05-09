"""SpiderFoot MCP server for Archimedes.

Wraps a self-hosted SpiderFoot REST API. Enforces passive-module-only
operation per LEGAL-POLICY (Hard Rule 4 — no active recon against
non-authorized targets). Active modules (port scanning, web spidering,
DNS brute force, vulnerability probing, target screenshots) are
hard-rejected at the input boundary regardless of caller.
"""

from spiderfoot_mcp.server import main

__version__ = "0.1.0"
__all__ = ["main"]
