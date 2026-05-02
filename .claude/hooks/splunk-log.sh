#!/usr/bin/env bash
# .claude/hooks/splunk-log.sh — Thin wrapper over scripts/splunk_log.py.
#
# Stable hook contract referenced by the librarian agent and CLAUDE.md.
# All real work happens in scripts/splunk_log.py — this exists so the
# hook name stays stable if the underlying script ever moves.
#
# Usage (pass-through to splunk_log.py):
#   .claude/hooks/splunk-log.sh --event '{"phase":"morning-brief"}'
#   .claude/hooks/splunk-log.sh --event-file path/to/event.json
#   echo '{...}' | .claude/hooks/splunk-log.sh --event-stdin
#
# Exit codes mirror the underlying script (see scripts/splunk_log.py).

set -euo pipefail

# Resolve the repo root from this hook's location (.claude/hooks/ -> ../..)
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${HOOK_DIR}/../.." && pwd)"

cd "${REPO_ROOT}"
exec uv run python scripts/splunk_log.py "$@"
