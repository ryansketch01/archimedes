# Archimedes — Architecture Walkthrough

45-minute engineering handoff. Designed so that after the talk, the audience could rebuild Archimedes from scratch — knows what to build, in what order, with what invariants must hold.

## Audience

Senior software engineer / architect, **Claude-familiar** (knows MCP, subagents, hooks). New to CTI tradecraft is fine — the deck doesn't dwell on Admiralty / WEP / MITRE because those are domain inputs, not architecture; if your audience needs CTI scaffolding too, pair this with `presentations/archimedes-overview/` first.

## Section structure

| Section | Slides | Min |
|---|---|---|
| §0 — Mental model (title, one-picture diagram, 5 invariants, on-disk layout) | 1–4 | ~6 |
| §1 — Doctrine layer (6 files, anatomy, Hard Rules, skills) | 5–8 | ~5 |
| §2 — Subagents (inventory, anatomy, context isolation, grading chain, librarian, orchestrator) | 9–14 | ~9 |
| §3 — MCPs + tool integration (architecture, wrapper anatomy, policy primitive code, inventory) | 15–18 | ~5 |
| §4 — Pipelines (scheduled brief, FLASH, on-demand, Layer 1/2, retraction) | 19–23 | ~8 |
| §5 — Infrastructure + ops (scheduler, hooks, audit trail, config, testing) | 24–28 | ~7 |
| §6 — Rebuild guide (MVP, build order, what to skip) | 29–31 | ~4 |
| Close — Q&A | 32 | ~1 |

## Files

- `build_deck.py` — python-pptx source. Run to regenerate.
- `archimedes-architecture.pptx` — generated deck. 32 slides, speaker notes throughout.
- `slides.md` — drop-into-your-own-template markdown version.

## Regenerating

```bash
uv run python presentations/archimedes-architecture/build_deck.py
```

## What's intentionally in this deck (vs. the other two)

- **Real artifacts.** Real directory trees (slides 4, 16, 29). Real code excerpts (slides 6, 10, 17, 22, 25). Real subagent inventory with real write scopes and tool subsets (slides 9, 10, 11).
- **Engineering-grade detail.** Sequence diagram for the scheduled brief pipeline with phase timings (slide 19). FLASH triggers + quiet hours + 72h auto-downgrade in tabular form (slide 20). Test coverage breakdown (slide 28).
- **Rebuild guide as the close.** §6 is the actionable part — minimum viable Archimedes (slide 29), week-by-week build order (slide 30), what to skip (slide 31). The audience should walk out knowing where they'd start tomorrow.

## What this deck DOESN'T do (vs. archimedes-overview)

- Less CTI tradecraft framing. We don't dwell on Admiralty 6×6 or WEP probability bands as concepts; we mention them as inputs the agent uses.
- No "look what's possible" inspiration. The framing assumes the audience already accepts that an agent-shaped CTI system is worth building.
- No Discord brief sample — that's in the overview deck.

## Things to review / strip before sharing externally

Per session-13 convention, flagged but included:

- **Target profile name** — the deck mentions "A&D contractor / ITAR / DIB" in passing (slides 11, 22). Strip if your audience shouldn't see it.
- **Real actor names** — UNC1549, MuddyWater, APT37, TeamPCP appear in slides 12 (grading chain example), 22 (brief content), 23 (retraction example). All public APT names, but listed concretely.
- **Splunk index names** — `archimedes`, `defenseclaw_local` appear in speaker notes only. Already redacted from the slide bodies.
- **Specific commit hashes / message IDs** — only in speaker notes, none in slide bodies.

Operator name, `.env` contents, source-grade specifics are excluded from the draft entirely.

## Relationship to the other decks

| | Archimedes overview | Athena Discovery | **Architecture walkthrough** |
|---|---|---|---|
| Audience | Mixed dev + sponsor | Mixed dev + sponsor | **Senior engineer / architect** |
| Frame | "Look what's possible" | "We'd build this IF…" | **"Here's exactly how it's wired"** |
| Density | Moderate | Moderate | **High — engineering handoff** |
| Length | 30 min / 24 slides | 22 min / 19 slides | **45 min / 32 slides** |
| Best for | Introducing the system | Pitching a similar build | **Handoff to engineers who'll rebuild it** |

Use this deck when the goal is technical transfer. Pair with the overview deck if the engineering audience also needs the problem context first.
