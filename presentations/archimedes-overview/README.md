# Archimedes overview — presentation deck

30-minute pitch for a Claude-familiar / CTI-new software dev team building something similar on OpenCTI. Walks through:

1. **Problem** — what a CTI analyst actually does, the volume problem, leadership's audience profile (slides 1–5)
2. **What it does** — the daily rhythm, real Layer 1 + Layer 2 brief samples, Admiralty grading, WEP vocabulary, FLASH alerts, actor profiles, Hard Rules (slides 6–13)
3. **Architecture (light)** — orchestrator + subagents + MCPs + doctrine; subagent role separation; doctrine as code; where OpenCTI fits in their stack; MCP wrappers; audit trail (slides 14–19)
4. **Lessons** — build trust before automation; live validation > mocks; context isolation reduces error rate (slides 20–22)
5. **Close** — 6-week build plan + Q&A (slides 23–24)

## Files

- `build_deck.py` — the source. Run to regenerate.
- `archimedes-overview.pptx` — the generated deck. **Open in PowerPoint and apply your company template via Design → Reuse Slides or master swap.**

## Regenerating

```bash
uv run python presentations/archimedes-overview/build_deck.py
```

Dependencies: `python-pptx`, already installed in the workspace venv. The script writes the .pptx alongside itself.

## Design notes

- Stylistically neutral (Calibri body, gray/dark-blue accents, no custom backgrounds) so applying a company template preserves the content cleanly.
- Speaker notes on every slide. 2–3 sentences each.
- Architecture diagram on slide 14 built natively in pptx shapes (no external image dependencies).
- Discord brief on slide 7 rendered as a styled monospace block that approximates the channel look — operator can drop a literal screenshot in their template-merged copy if preferred.
- Placeholder strings (`[Presenter name]`, `[Date]`, `[Email]`) on slides 1 and 24 — fill in before presenting.

## Things to review / strip before sharing externally

Per session-13 build conversation, these are included on the current draft and may want to be redacted depending on audience:

- Target-profile naming (`mid-to-large US A&D contractor / ITAR / DIB`) — slides 3, 8, 12, 13
- Specific tracked actor names (UNC1549, MuddyWater, APT34, APT37, Charming Kitten, TeamPCP) — slides 8, 12, 20 (all public APT names but listed concretely)
- The FLASH-0002 / MuddyWater example — slide 11
- Splunk index names (`archimedes`, `defenseclaw_local`) — slide 14, 19
- Specific commit hashes / message IDs — none in slides (in speaker notes only)

`.env` contents, source-grade specifics, and operator name are excluded from the draft.
