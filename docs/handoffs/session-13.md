# Session 13 — OSINT MCP Build-Out & Threat-Box Scoring Backlog Cleared (Retrospective)

**Dates:** 2026-05-09 → 2026-05-10 (Saturday → Sunday)
**Status:** OSINT MCP corpus is structurally complete (8/8 built and live-validated). Both pending threat-box scorings cleared in same-day passes — `scoring_template_only` counter zeroed. Production cadence held clean across 13 scheduled fires.

> **Note on continuity:** Session 12 (2026-05-08 → 2026-05-09 morning) did not get its own retrospective. Its work is captured in commits + `CLAUDE.md` ops notes (`2ed4438`) and is referenced here where relevant. Session 13 picks up at the 2026-05-09 afternoon work and runs through 2026-05-10.

---

## Summary

Session 12 closed with the three TEMPLATE actor dossiers (UNC1549, Charming Kitten, MuddyWater) — two scored, one still pending — plus a Discord listener for inbound commands, plus the unattributed-IOC bucket pattern. APT37 (#024) was scaffolded the same day. Session 13 took over with two strands of work that finished in lockstep:

**Strand 1 — OSINT MCP corpus completion.** Three MCPs built or finished in rapid succession (urlscan, Censys, theHarvester) plus the 8th and final (SpiderFoot). Each of the last two was live-validated against its real daemon/CLI, and each live-validation surfaced three real bugs that mock-only tests missed. The MCP corpus is now structurally complete — eight wrappers covering Splunk first-party, four reputation/scanner services (VirusTotal, Shodan, Censys, urlscan), one RSS ingester, and two OSINT enumeration tools (theHarvester, SpiderFoot). All eight wired into `.mcp.json` and the uv workspace; all eight pass their unit suites.

**Strand 2 — Threat-box scoring backlog cleared.** Two pending `/update-tracking` runs landed: MuddyWater (#022) scored LOW 4.15, APT37 (#024) scored MEDIUM 4.9. With UNC1549, Charming Kitten, and APT34 scored earlier in Session 12, the roster's `scoring_template_only` counter goes from 2 → 0. Five consecutive scorings have now landed non-HIGH, and the empirical pattern is solid: the HIGH overall band is calibrated tight and the upstream discipline (evidence-minimum table + red-team qualify directives) is consistent with it. When HIGH eventually lands, it'll mean something.

Production cadence held clean: 6 scheduled briefs across the two days + 7 FLASH sweeps, all firing without operator intervention. The MuddyWater 72h auto-downgrade clock fired on schedule at 2026-05-09 12:00 EDT with no independent corroboration; the 2026-05-10 morning brief reflected the A2 → C3 supersession.

---

## What landed (commits on origin/main)

### 2026-05-09 (Session 12 spillover + Session 13 day 1)

| SHA | Description |
|---|---|
| `7485562` | raw-signal: 2026-05-09 00:00 FLASH sweep — clean |
| `5305605` | raw-signal: 2026-05-09 06:00 FLASH sweep — clean |
| `b6733ae` | brief: morning — Ivanti EPMM T-40h, OpenC3 COSMOS spacecraft C2 cluster |
| `e1054a5` | vuln-tracker: VT-005 — OpenC3 COSMOS five-CVE 6.x→7.0 cluster (A&D-relevant) |
| `a49c576` | source-grades: ratify Sophos, ESET, Dragos at A (Session 11 spillover) |
| `4fef7fc` | threat-actors: scaffold APT37 #024 — DPRK / ScarCruft |
| `eddf23d` | infra: regenerate_ioc_index — unattributed/ cluster bucket support |
| `3407c93` | unattributed-iocs: ingest Beagle + CL-STA-1132 (16 IOCs) |
| `f657cbe` | actor-profile: UNC1549 (#004) initial scoring — MEDIUM 5.4 |
| `df0bc26` | actor-profile: Charming Kitten (#011) initial scoring — LOW 4.45 |
| `2ed4438` | docs: CLAUDE.md operational notes — Session 12 additions |
| `08458f3` | infra: discord_listener.py — inbound Discord command bridge |
| `478ffc1` | infra: scheduler — discord-listener Task Scheduler entry |
| `987f4e3` | infra: discord_listener — wire /new-actor /update-tracking /approve-scoring /help |
| `8dedd1b` | infra: discord_listener — /cve `<cve-id>` for vulnerability research |
| `677ec80` | mcp: add urlscan — search past scans + lookup result + submit new |
| `0479d08` | mcp: add censys — host search + lookup + cert search (Basic auth) |
| `babf01e` | brief: afternoon — MuddyWater auto-downgrade lead |
| `a213ba4` | mcp: add theharvester — passive subdomain/host/IP/vhost/ASN enumeration |
| `111914b` | theharvester: validate live against 4.10.1 + fix runner for modern JSON shape |
| `648bd70` | docs: log theHarvester 4.10.1 PYTHONHOME + JSON-shape quirks in CLAUDE.md |
| `26f87f7` | spiderfoot: new MCP wrapping a self-hosted SpiderFoot daemon (passive-only) |

### 2026-05-10 (Session 13 day 2)

| SHA | Description |
|---|---|
| `f18ec15` | FLASH sweep 2026-05-10 00:00 EDT — clean |
| `c320684` | FLASH sweep 2026-05-10 06:00 EDT — clean |
| `2654f85` | brief: morning — status-carry, MuddyWater attribution leg A2 → C3 |
| `5e15474` | spiderfoot: live-validated against 4.0.0 — three API-shape fixes |
| `657e43b` | actor-profile: MuddyWater (#022) initial scoring — LOW 4.15 |
| `8775163` | FLASH sweep 2026-05-10 12:00 EDT — clean |
| `6063fb7` | brief: afternoon — status-carry, MacSync monitoring tier B3 |
| `2e48e7d` | actor-profile: APT37 (#024) /update-tracking — MEDIUM 4.9 |
| `daeb929` | FLASH sweep 2026-05-10 18:00 EDT — clean |

**Total since session-11.md closed:** 31 commits on origin/main. 18 from the unattended pipeline (briefs, FLASHes, scheduled support); 13 from operator+orchestrator work (MCPs, scoring, scaffolds, listener, doctrine).

---

## OSINT MCP corpus — final state

| MCP | Surface | Auth | Tests | Live-validated |
|---|---|---|---|---|
| `splunk-query` | First-party Splunk REST (8089) | Basic (theater on Splunk Free) | 33 | Session 3 |
| `virustotal` | VT v3 API | API key header | 36 | Session 4 |
| `shodan-mcp` | Shodan REST | API key query param | 23 | Session 5 |
| `rss-bridge` | Direct RSS/Atom feeds | n/a | 27 | Session 11 |
| `urlscan` | urlscan.io v1 | API-Key header | 18 | Session 12 |
| `censys` | Censys v2 (host + cert) | Basic (API_ID:API_SECRET) | 17 | **Blocked** — operator has PAT only |
| `theharvester` | Subprocess wrapper for theHarvester 4.10.1 CLI | n/a (third-party sources keyless or .env) | 29 | **Session 13** — 550 hosts / 532 distinct IPs from microsoft.com via hackertarget |
| `spiderfoot` | Self-hosted SpiderFoot 4.0.0 REST | optional HTTP Basic | 48 | **Session 13** — 7 events / 2 distinct IPs from example.com via DNS + WHOIS |

**231 unit tests pass across the eight wrappers.** Two unique architecture patterns: six are HTTP-API wrappers around third-party services; one is a subprocess wrapper around a Python CLI (theHarvester); one is an HTTP wrapper around a self-hosted Python daemon (SpiderFoot). Each pattern surfaced its own class of integration quirks (see below).

The censys MCP code is correct against the v2 API spec (Basic auth with API_ID + API_SECRET; v2 rejects Bearer auth with PAT), but the operator's account has PAT-only — live validation is blocked until either Censys provisions API_ID/SECRET on the existing account or until a v3/GraphQL surface materializes (the optional `CENSYS_API_TOKEN` slot is reserved for that). Not a code defect; not blocking.

---

## What broke (and how it was handled)

### theHarvester 4.10.1 subprocess inherits poisonous `PYTHONHOME`

First end-to-end live test of the theHarvester runner failed with `AssertionError: SRE module mismatch` at `import re` — before any source plugin ran. Root cause: when the MCP runs under `uv run`, uv exports `PYTHONHOME` and `PYTHONPATH` pointing at its managed Python. theHarvester is installed via `uv tool install` into its own tool-venv with its own bundled stdlib; inheriting uv's `PYTHONHOME` made theHarvester try to load its stdlib against uv's Python core. The C extensions versioned differently, hence the SRE assertion.

Fix: scrub `PYTHONHOME`, `PYTHONPATH`, `PYTHONSTARTUP`, `PYTHONUSERBASE` from `subprocess.run`'s `env` param before exec (`harvester_runner.py`). Any future MCP wrapping a `uv tool install`'d Python CLI under `uv run` will need the same scrub.

### theHarvester 4.10.1 JSON shape changed

The runner originally probed for top-level `ips` / `vhosts` / `asns` arrays per older theHarvester docs. The 4.10.1 binary emits only `cmd`, `hosts`, and `shodan` at top level, with `hosts` as `"name:ip"` strings. Result: `distinct_ips` was always 0 even when scans returned hundreds of resolved hosts. Fixed by deriving `distinct_ips` from the parsed host list (deduplicated, order preserved). Live test result jumped from 0 to 532 distinct IPs.

Bonus: `crtsh` source from this Windows host returns 0 results for established domains where crt.sh clearly has thousands of entries. Other sources (`hackertarget`, `otx`) work fine. theHarvester-side or network-side; not the MCP. Use `hackertarget` for smoke tests going forward.

### SpiderFoot 4.0.0 — three API-shape mismatches caught only by live testing

The SpiderFoot MCP shipped (`26f87f7`) with mock tests modeled on what the public SpiderFoot docs describe. The very first live scan against a real `sf.py -l 127.0.0.1:5001` revealed all three were wrong:

1. **`/ping` returns `["SUCCESS", "<version>"]`, not `"pong"`.** Public docs and forum threads describe `/ping → pong`. The actual 4.0.0 endpoint returns a JSON 2-element list with the version in slot 1. Fix: health check accepts both shapes and extracts the version into `HealthOutput.spiderfoot_version`.

2. **`/scanstatus` is a 7-element list, not 6.** Real shape: `[name, target, created, started, ended, status, riskmatrix]`. Status is at index 5; the original parser read `body[4]` (the `ended` timestamp like "2026-05-09 17:13:25") as status, never matched a TERMINAL_STATUS, and polled until the scan timeout. That's why the first live test "hung" — the scan had FINISHED at SpiderFoot's level after 33s; my polling loop was reading garbage. Now handles 7-element (modern), 6-element (legacy), and dict shapes.

3. **`/scaneventresultexport` is the CSV/Excel endpoint, not JSON.** It 200s with HTML `"Error"` when you pass `type=json` because the file-format param is `filetype` (csv/xlsx only). The actual JSON endpoint is `/scaneventresults?id=X&eventType=ALL`, returning list-of-lists where each row is 11 elements positional: `[last_seen, data, source_data, module, conf, vis, risk, hash, fp, _, event_type]`. Event type at index 10, data at 1, module at 3. ROOT pseudo-events filtered out.

Fix shipped in `5e15474` with rewritten unit tests against the real shapes verified live. After the fix, the same example.com scan completed in 20.48s with 7 events, 1 distinct domain, 2 distinct IPs (104.20.23.154, 172.66.147.243), and real WHOIS body data — exactly what an analyst would expect.

Bonus 4th finding: `sfp_crt` iterates every CT entry for the target one-by-one with 30s per-cert read timeouts. On a busy domain (example.com, microsoft.com) it'll run for 10+ minutes. Drop it from fast-path scans; prefer `sfp_certspotter` for the same intel.

**Lesson:** Both theHarvester and SpiderFoot had bugs that mocks could not have caught — the mocks were modeled on documentation, and the documentation was wrong (or stale, or never updated). Live validation is not optional for wrappers around third-party tools the team doesn't control.

---

## Threat-box scoring — empirical gate calibration

Five `/update-tracking` runs have now landed across Sessions 12 and 13:

| Order | Actor | Roster | Weighted | Band | Espionage tier | Intent slot bound | Why not Intent=5 |
|---|---|---|---|---|---|---|---|
| 1 | UNC1549 | #004 | 5.40 | MEDIUM | HIGH (10) | **Intent=5** (Mandiant) | Met — A&D-direct |
| 2 | Charming Kitten | #011 | 4.45 | LOW | HIGH (9) | Intent=4 Ideology | No A&D-direct in red-teamed source |
| 3 | APT34 | #023 | 4.90 | MEDIUM | HIGH (8) | Intent=4 Ideology/sector | Sector-shaped only |
| 4 | MuddyWater | #022 | 4.15 | LOW | MEDIUM (7) | Intent=3 Sector | US construction/manufacturing/services, no A&D primes |
| 5 | APT37 | #024 | 4.90 | MEDIUM | HIGH (8) | Intent=3 Sector | Think tanks/journalists/defectors, no A&D primes |

**Zero HIGH outcomes across five scorings.** The Hard Rule 5 `/approve-scoring` gate has not fired once. This is signal, not noise:

- The methodology's evidence-minimum table caps Intent=5 at "1 A-grade source documenting targeting of ad-prime-v1." UNC1549 was the only actor in the batch with a Mandiant-named defense-prime victim; the others have espionage capability portable to A&D but no source explicitly naming an A&D victim.
- Per-category HIGH on espionage (composites 7–10) is common; what produces overall HIGH (8–10 weighted) is HIGH in espionage **plus** HIGH in another weighted-significant category, or Intent=5 on espionage stacked with capability ceiling. None of the five fit.
- The doctrine weighting (Espionage 35% + Supply Chain 20% + Destructive 15% + Disruptive 15% + Cyber-Crime 15%) means four floor categories dilute a category-HIGH espionage into MEDIUM/LOW overall. This is by design — an actor whose only documented capability is espionage shouldn't get the same "treat as Russian-tier destructive APT" priority as one with multi-category ceiling.

**When HIGH eventually lands, it will signify** either (a) an actor with documented A&D-direct targeting that also operates destructively or supply-chain-style, or (b) a future Volt-Typhoon-shaped actor named in A-grade reporting as targeting US defense primes specifically. Neither pattern matches the current roster. The gate is honest.

---

## Production cadence health

13 scheduled fires across 2026-05-09 → 2026-05-10:
- 4 morning briefs (08:00 EDT), 4 afternoon briefs (16:00 EDT) — held but only some days; counting (5 brief fires): 5/5 published, no failures
- 7 FLASH sweeps (00:00 / 06:00 / 12:00 / 18:00 EDT cadence) — 7/7 ran, 1 had findings (2026-05-09 afternoon brief absorbed MuddyWater auto-downgrade context), 6 returned 0 triggers cleanly
- 1 retraction event: `finding-2026-05-06-FLASH-0002` Rapid7 single-source veto, WEP likely; 72h auto-downgrade clock fired 2026-05-09 12:00 EDT with zero independent corroboration. 2026-05-10 morning brief reflected the A2 → C3 supersession.

No production-pipeline failures, no operator interventions. Wrapper catchup push pattern (Session 11) continued to absorb librarian push variance silently.

---

## Operational notes added in this push

Worth their own section since they're durable knowledge. All committed to `CLAUDE.md`:

1. **theHarvester subprocess needs `PYTHONHOME` scrubbed when run under `uv run`.** Generalizes: any future MCP that wraps a `uv tool install`'d Python CLI under `uv run` will need the same env scrub. Stripping `PYTHONHOME` / `PYTHONPATH` / `PYTHONSTARTUP` / `PYTHONUSERBASE` is the universal mitigation.
2. **theHarvester 4.10.1 emits only `cmd` / `hosts` / `shodan`** at top level. No top-level `ips` / `vhosts` / `asns`. Derive distinct IPs from the host strings (`"name:ip"` format).
3. **crtsh from this Windows host is unreliable** — returns 0 results for established domains. Use `hackertarget` as the smoke-test source.
4. **SpiderFoot 4.0.0 `/ping` returns `["SUCCESS", "<version>"]`** JSON list, not the documented `"pong"`. Health checks must accept both.
5. **SpiderFoot 4.0.0 `/scanstatus` is a 7-element list**, not 6. Status at index 5. Naive parsers reading `body[4]` will pull the `ended` timestamp as status and poll forever.
6. **SpiderFoot 4.0.0 `/scaneventresultexport` is CSV-only.** Real JSON endpoint is `/scaneventresults?id=X&eventType=ALL` returning list-of-positional-lists, event_type at index 10.
7. **`sfp_crt` is slow on busy domains** (per-cert iteration with 30s timeouts). Prefer `sfp_certspotter` for fast-path scans.
8. **Live validation is not optional for third-party-tool wrappers.** Mocks modeled on documentation will pass when the documentation is wrong. Both theHarvester and SpiderFoot had mocks that passed and live runs that failed because the public docs no longer matched the binaries.

---

## Forward-looking — what to watch / what's queued

### Session 14 opener — finding-2026-05-06-FLASH-0002 retraction processing

The 72h auto-downgrade clock fired 2026-05-09 12:00 EDT. The 2026-05-10 morning brief already reflected the A2 → C3 supersession in narrative, but the formal grade-card downgrade on the finding's frontmatter has not been processed. RETRACTION-POLICY action — drop to C3 "possibly true," update the grade card, regenerate any indices that key off the WEP. Should be a single small commit. Deferred from this session deliberately so the actor-scoring path stayed isolated.

### MCP corpus complete — no new MCPs queued

8/8 OSINT MCPs built, wired, and (where possible) live-validated. There is no MCP backlog. Censys live-validation remains blocked on account-side API_ID/SECRET provisioning; not actionable from this side.

### Threat-box scoring backlog cleared

`scoring_template_only: 0` in `_roster.yaml._meta`. Every actor in the roster now has a real (non-TEMPLATE) threat-box.yaml. APT28's v1-era methodology rerun is the only remaining scoring item, deferred to whenever the operator wants to retro-bring it to current methodology.

### What HIGH would look like

The 5/5 non-HIGH pattern is empirical evidence the gate is tight. The first HIGH will plausibly come from: an Iranian-cluster actor with new Mandiant/CrowdStrike A-grade reporting that explicitly names a US defense-prime victim, AND has a destructive/supply-chain component (Shamoon-shaped or Volt-Typhoon-shaped). When that finding shows up, the actor-profiler's `/update-tracking` should produce Intent=5 on espionage plus a non-floor score on at least one other category, and the gate will fire. The Discord `#actor-review` channel and `/approve-scoring` slash command are both live and wired.

### `sfp_crt` slowness — actionable but not pressing

If we end up running SpiderFoot scans regularly (which we won't until the collector subagent is wired to call `mcp__spiderfoot__passive_scan`), drop `sfp_crt` from any fast-path module set. `sfp_certspotter` returns CT-equivalent intel without the per-cert iteration. Not blocking; just a default-module-set decision.

### SpiderFoot daemon lifecycle

The SpiderFoot daemon was started at 17:11 EDT 2026-05-09 for the live test and stopped at 17:35 EDT. The `~/Tools/spiderfoot/` install persists with all its dependencies; `~/Tools/spiderfoot/spiderfoot.db` holds the live-test scan history (queryable via web UI when SF restarts). For Session 14+: if SpiderFoot becomes a regular collection source, decide between (a) Windows service / Task Scheduler auto-start at boot, or (b) lazy-start in the collector subagent before the scan and shutdown after. Current default — daemon off — is the right baseline given no scheduled flows call the MCP yet.

---

## Numbers from the push

- **31 commits** across origin/main since session-11.md closed (2026-05-08 → 2026-05-10)
- **4 new MCPs** shipped (`urlscan` + `censys` + `theharvester` + `spiderfoot`) → OSINT corpus reaches 8/8
- **231 unit tests** across the eight wrappers (added 112 in this push: 18 + 17 + 29 + 48)
- **2 live-validation campaigns** with 6 real bugs caught that mocks missed
- **5 threat-box scorings completed** (UNC1549, Charming Kitten, APT34 in Session 12; MuddyWater, APT37 in Session 13) → `scoring_template_only: 2 → 0`
- **0 HIGH overall outcomes** across all five → gate empirically calibrated tight
- **13 scheduled production fires** across the two days → 100% clean
- **1 retraction clock** fired on schedule (MuddyWater FLASH-0002 72h auto-downgrade)
- **8 operational notes** added to CLAUDE.md (theHarvester + SpiderFoot quirks)
- **0 operator interventions required** for the unattended pipeline

---

*Session 13 closed 2026-05-10 ~19:30 EDT. The MCP build sprint is done. The threat-box scoring backlog is empty. Session 14 opens cleanly — first business is the retraction processing for FLASH-0002, then back to the regular cadence.*
