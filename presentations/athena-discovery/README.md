# Athena — Discovery Proposal

22-minute pitch for a mixed audience (software dev team + program sponsors). Proposes funding a 2-3 week Discovery Phase to validate requirements before committing to a build. Maps a stakeholder intake spec to a proposed feature set, anchored on the Archimedes architecture pattern.

## What this deck is

- **Discovery framing throughout.** No build commitment. Every requirement bullet labeled "we know / need to validate." Amber `DISCOVERY` badges on slides that depend on stakeholder input.
- **The ask is Discovery sponsorship**, not build approval. 19 slides culminate in 5 concrete asks plus a "what Discovery delivers" close.
- **Named explicitly:** Mandiant Advantage / GTI by name. CMDB stays generic ("your CMDB") with a tooling footnote.
- **Project name placeholder:** *Athena*. Find-replace if your stakeholders use a different working name.
- **Length:** ~22 min, 19 slides, ~70s per slide.
- **Audience:** dev team + program sponsors in the same room.

## Files

- `build_deck.py` — the source. Run to regenerate.
- `athena-discovery.pptx` — the generated deck. **Open in PowerPoint and apply your company template via Design → Themes → Browse or Reuse Slides.**
- `slides.md` — drop-into-your-own-template version (same content, same speaker notes; copy slide-by-slide into your template natively).

## Regenerating

```bash
uv run python presentations/athena-discovery/build_deck.py
```

Dependencies: `python-pptx`, already installed in the workspace venv. The script writes the .pptx alongside itself.

## Section structure

| Section | Slides | Min |
|---|---|---|
| 1 — Problem & opportunity | 1–4 | ~5 |
| 2 — Proposed approach (requirements → features) | 5–9 | ~6 |
| 3 — What it could look like (dashboard, Q&A, playbooks) | 10–12 | ~4 |
| 4 — Discovery scope (architecture, doctrine, phase plan, open questions) | 13–16 | ~5 |
| 5 — Close (ask, deliverables, Q&A) | 17–19 | ~2 |

## Design notes

- Stylistically neutral (Calibri body, gray/dark-blue accents, no custom backgrounds) so applying a company template preserves the content cleanly.
- Speaker notes on every slide. 2–3 sentences each.
- Architecture diagram on slide 13 and CMDB-GTI pipeline on slide 8 built natively in pptx shapes (no external image dependencies).
- Sample Q&A on slide 11 and dashboard wireframe on slide 10 rendered as styled blocks — replace with real screenshots once Discovery produces real artifacts.
- Placeholder strings (`[Presenter name]`, `[Date]`, `[Email]`) on slides 1 and 19 — fill in before presenting.

## Things to review / strip before sharing externally

- **Project name** — change "Athena" → whatever your stakeholders call it (find-replace across `build_deck.py` and `slides.md`, then regenerate).
- **Cost-of-status-quo numbers** (slide 3) — currently abstract. Replace with real analyst-hour / MTTR numbers if you have them.
- **Five-actor scoring reference** (slide 7) — example shows APT37; swap to whatever actor your stakeholders are most familiar with if needed.
- **Slide 11 sample Q&A** — UNC1549 example; substitute an actor relevant to your environment if you want.
- **Stakeholder team list** (slide 9) — SOC / IR / Vuln Mgmt / Intel / Leadership as the default. Adjust to your org's actual team names.

## Relationship to the other deck

`presentations/archimedes-overview/` is the parallel deck — same audience-class but **retrospective explainer** of what Archimedes is. Use that one when introducing the existing system; use this one when proposing a new build modeled on it. Two distinct framings; pick the right one for the meeting.
