#!/usr/bin/env bash
# .claude/hooks/discord-post.sh — Thin wrapper over scripts/discord_post.py.
#
# Stable hook contract referenced by the librarian agent and CLAUDE.md.
# All real work happens in scripts/discord_post.py — this exists so the
# hook name stays stable if the underlying script ever moves.
#
# Usage (pass-through to discord_post.py):
#   .claude/hooks/discord-post.sh --channel commands --message "test"
#   .claude/hooks/discord-post.sh --channel intel-briefs --message-file brief.md
#   echo "..." | .claude/hooks/discord-post.sh --channel intel-briefs --message-stdin
#
# Symbolic --channel values: intel-briefs | flash-alerts | actor-review | commands
# Or pass --channel-id <id> for a raw Discord channel ID.
#
# Exit codes mirror the underlying script (see scripts/discord_post.py).

set -euo pipefail

# Resolve the repo root from this hook's location (.claude/hooks/ -> ../..)
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${HOOK_DIR}/../.." && pwd)"

cd "${REPO_ROOT}"
exec uv run python scripts/discord_post.py "$@"
