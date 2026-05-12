# Archimedes — Intern Intro

5-7 minute orientation talk for a college intern (or anyone joining the team with no CTI / no Claude / no security-tools background). Goal: by the end they understand what the system does, why it exists, and that they can ask it questions in chat.

## What this deck is

- **10 slides · ~5-7 min · plain English.** No Admiralty, no WEP, no MITRE references, no Hard Rule numbers.
- **Analogies they'd know** — Google News on steroids, Discord bot, ChatGPT for our threat intel.
- **One artifact** — a real Discord brief sample on slide 4 so they can see what the output actually looks like.
- **Same neutral styling** as the other three decks for company-template merge.

## Slide outline

1. Title — *"Meet Archimedes"*
2. The problem — why security teams need this
3. What we built — one centered sentence
4. What it looks like — real Discord brief sample
5. How it works — step 1: collecting
6. How it works — step 2: grading
7. How it works — step 3: writing the brief (Layer 1 + Layer 2 explained without using those names)
8. Safety rails — what the agent refuses to do
9. You can talk to it — slash commands example
10. Wrap-up + Q&A — three takeaways, then questions

## Files

- `build_deck.py` — python-pptx source. Regenerate after edits.
- `archimedes-intern-intro.pptx` — 59KB, 10 slides, speaker notes throughout.

## Regenerating

```bash
uv run python presentations/archimedes-intern-intro/build_deck.py
```

## How this differs from the other three decks

| | overview | discovery | architecture | **intern intro** |
|---|---|---|---|---|
| Length | 30 min | 22 min | 45 min | **~5-7 min** |
| Slides | 24 | 19 | 32 | **10** |
| Audience | Mixed dev + sponsor | Mixed dev + sponsor | Engineer/architect | **College intern** |
| Jargon | Moderate | Moderate | High | **None** |
| Best for | Concept intro to working pros | Pitching a similar build | Engineering handoff | **Orienting newcomers** |

## Things to review before delivering

- **Slide 4 Discord sample** — currently uses the May 11 brief content (Checkmarx, SailPoint, Ivanti, BerriAI). Swap with a more recent example if the intern is starting later.
- **Slide 9 slash commands** — `/cve`, `/investigate`, `/ioc-hunt`, `/help` are accurate; add or remove based on which slash commands the intern actually has access to.
- **Sensitive content** — this deck deliberately omits target-profile specifics, actor names beyond a generic `APT37` example, and Splunk index names. Pre-redacted for the intern audience.

## Speaker notes

Every slide has 2-3 sentences of speaker notes. Open the deck in PowerPoint → View → Notes Page (or just use the notes pane in normal view) to see them. They give you a casual script — read them once before delivering and the talk lands in 5-7 minutes.
