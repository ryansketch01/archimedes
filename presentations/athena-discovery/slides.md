# Athena — Discovery Proposal · slide-by-slide spec

> Drop-into-your-own-template version of `athena-discovery.pptx`. Same 19-slide outline, same speaker notes. Copy what you need, edit what you don't.
>
> **Discovery framing throughout** — proposed approach with explicit "we know / need to validate" sub-lines, not a committed architecture. The ask is sponsorship for a 2-3 week Discovery Phase, not approval to build.

**Total: 19 slides · ~22 min · ~70s per slide**

---

## Slide 1 — Title

**Layout:** Big centered project name + subtitle + presenter byline. Amber `DISCOVERY PROPOSAL — for discussion, not commitment` banner across the top.

**Title:** `Athena`
**Subtitle:** AI-enabled CTI enrichment + decision support
**Byline:** [Presenter name] · [Date] · Audience: dev team + program sponsors

**Speaker notes:**
Open by naming the audience explicitly — dev team here to evaluate buildability, sponsors here to evaluate whether to fund a Discovery Phase. Frame: this is a Discovery proposal, not a build commitment. We have a working architecture pattern (Archimedes) we'd anchor on, but we're asking for 2-3 weeks of structured working sessions to validate the requirements before sizing a build. The deck shows the proposed approach plus the open questions that need stakeholder input.

---

## Slide 2 — The problem

**Subtitle:** From the intake — verbatim distilled.

**Quote block (italic, large):**

> "Threat intelligence analysts spend significant time manually reviewing and judging the trustworthiness and relevance of intelligence (especially from OpenCTI), then separately correlating it to our environment (assets in CMDB) and external risk context (e.g., Mandiant Advantage / GTI)."
>
> "This manual work slows triage, creates inconsistent confidence scoring and prioritization across analysts, and delays response actions for high-impact vulnerabilities and threats."

**Three takeaway tags (below the quote, side by side):**

- **Inconsistent** — scoring varies analyst-to-analyst
- **Slow** — manual correlation across OpenCTI + GTI + CMDB
- **Reactive** — high-impact threats wait on analyst capacity

**Speaker notes:**
Read the problem statement out loud — most of the room hasn't seen this slide before. The three tags at the bottom are what we'll come back to throughout — Athena's job is to make these three things go away. Don't get into the solution yet; this slide is anchoring why we're here.

---

## Slide 3 — The cost of status quo

**Subtitle:** What the manual workflow costs today — placeholders for your numbers.

**Bullets (drop in real numbers before presenting if you have them):**

- **Analyst-hours on triage, not analysis** — Most of an analyst's day is the rote 80% — re-reading what Mandiant + Unit 42 + MSTIC published, looking it up in OpenCTI, cross-checking CMDB by hand. The 20% only humans can do gets squeezed.
- **Inconsistent confidence across analysts** — Two analysts grading the same finding can land at "likely" vs. "almost certainly" depending on experience, day, mood. Leadership sees the inconsistency and discounts the output.
- **Delayed response on high-impact threats** — By the time a Mandiant FLASH gets correlated to your CMDB exposure + your GTI risk overlay, the patch window is often half gone. Time-to-action on a CVSS-10 should be hours, not days.
- **Prioritization drift across the org** — SOC, Vuln Mgmt, IR, and Leadership often have different lists of "top threats this week" — because there's no shared, transparent prioritization model. Decisions don't align.
- **Stakeholder reporting is its own job** — Weekly summaries to each team are hand-written. Tailoring the same intel to four audiences costs hours that don't produce new analysis.

**Speaker notes:**
If you have concrete numbers (analyst-hours per week, time-to-triage averages, MTTR for high-impact threats), drop them in here BEFORE this meeting — leadership wants the specific cost. If you don't have those numbers yet, the Discovery Phase produces them as part of validation. Frame that explicitly during the talk.

---

## Slide 4 — Why this is solvable now

**Subtitle:** The pattern is proven; the substrate exists; the missing piece is the analyst layer.

**Bullets:**

- **The pattern is proven elsewhere** — Archimedes — internal CTI agent — has been running this shape autonomously for several months. Twice-daily graded briefs, FLASH alerts, threat-actor tracking, full audit trail. Same problem class, different stack.
- **Substrate already exists in your environment** — OpenCTI for the entity store. Mandiant Advantage / GTI for the external risk overlay. CMDB for the asset inventory. SOAR for the playbook engine. The pieces are in place — they don't talk to each other yet.
- **Claude is the missing analyst layer** — Long-context reads (200 articles → 4 graded findings). Consistent framework application (Admiralty, WEP, MITRE). Strict-format output. Tool use across all your existing systems. Context-isolated subagents — one per role — reduce error rate by construction.
- **Discovery proves it for YOUR environment** — A 2-3 week structured discovery phase validates the integration paths, locks the requirements, and produces a sized build plan with confidence intervals. Then you decide whether to fund the build.

**Speaker notes:**
This is the "we know what we're doing" slide for leadership. Three points: pattern proven, substrate in place, Claude is the right engine. If asked to demo Archimedes, you can show #intel-briefs Discord post or screen-share a brief markdown file. The final bullet pivots to the Discovery ask without committing to a build yet.

---

## Slide 5 — Requirements → working hypotheses

**Subtitle:** Your spec, mapped to a proposed feature, with explicit "we know / we need to validate" sub-line per row.

**Marked as DISCOVERY (amber badge).**

**Three-column table:**

| Requirement | Proposed feature | We know / need to validate |
|---|---|---|
| **Confidence grading** | Admiralty 6×6 + WEP, applied per source per finding | 🟢 We know — same methodology in Archimedes today |
| **Threat prioritization** | Weighted threat-box scoring; per-category composites | 🟡 Validate — weights tuned to YOUR stakeholder priorities |
| **CMDB exposure scoring** | Finding IOCs/CVEs → CMDB asset match → criticality overlay | 🟡 Validate — your CMDB tool + asset-criticality field |
| **GTI risk cross-reference** | Mandiant Advantage risk score overlay on every graded finding | 🟡 Validate — your GTI license tier + API access |
| **Media attention signal** | Tracked-news source set + signal-volume metric per topic | 🟢 We know — pattern exists; needs source weighting |
| **Interactive Q&A** | Slash commands in Teams: `/cve` `/investigate` `/ioc-hunt` | 🟡 Validate — Teams as delivery platform; webhook plumbing |
| **"What matters now" dashboard** | Real-time view: top threats, exposure heatmap, FLASH queue, gates | 🟡 Validate — hosting model + auth/SSO + per-team filters |
| **Automated response playbooks** | Agent → SOAR webhook → playbook fires → result back to corpus | 🟡 Validate — which SOAR (Tines / Torq / ServiceNow / other) |
| **Weekly trend summaries** | Per-team renderings of the same canonical intel; "so what" framing | 🟡 Validate — stakeholder team list + contact owners |
| **On-demand threat reports** | `/report <topic>` against OpenCTI + GTI corpus | 🟢 We know — Archimedes `/investigate` already does this shape |

**Speaker notes:**
This is the load-bearing slide of the deck. Every requirement from the intake is mapped to a concrete proposed feature and labeled with what we already know vs. what needs Discovery validation. Green text = pattern proven in Archimedes, low risk. Amber text = needs your input to lock. This is also the place to invite questions from the room — anything they want to flag as "we need more on this" is fair game.

---

## Slide 6 — Confidence grading — proposed methodology

**Subtitle:** Admiralty 6×6 + Words of Estimative Probability. Transparent, doctrine-versioned, applied uniformly.

**Two-column layout (Reliability / Credibility), then WEP strip below.**

### Reliability (left column)

- **A — Completely reliable** — Mandiant, Unit 42, MSTIC, CrowdStrike, MITRE, CISA
- **B — Usually reliable** — BleepingComputer, The Record, Krebs
- **C — Fairly reliable** — Vendor blogs with mixed history; first-citation entrants
- **D / E / F** — Unreliable / unknown / questionable — monitoring only

### Credibility (right column)

- **1 — Confirmed** — Multiple independent A/B-grade sources
- **2 — Probably true** — One A-grade source + plausibility test passes
- **3 — Possibly true** — Single source, cannot be confirmed or denied
- **4 / 5 / 6** — Doubtful / improbable / cannot be judged

### WEP strip (full-width, light blue background)

Words of Estimative Probability bound every forward claim: **almost certainly** (≥95%) · **very likely** (85–95%) · **likely** (55–85%) · roughly even chance (~50%) · unlikely (15–45%) · very unlikely (5–15%) · remote (<5%)

*Hedging language banned by doctrine. "May / might / could" → fails preflight, regenerated until WEP-compliant.*

### Footer (italic, centered)

Single-source-veto rule: even an A-grade source caps the forward claim at "likely" on its own. Solves the analyst-to-analyst inconsistency problem by construction.

**Speaker notes:**
Frame: Admiralty is older than cyber — NATO has used it since the Cold War. WEP comes from a 1964 CIA paper. We're not inventing methodology; we're encoding existing methodology in doctrine the agent applies uniformly. The single-source-veto rule is the load-bearing answer to "inconsistent confidence across analysts" — the agent literally cannot promote a single-source claim above "likely" regardless of how strong it sounds.

---

## Slide 7 — Transparent prioritization — proposed

**Subtitle:** Threat-box scoring: per-category composites, weighted to overall HIGH / MEDIUM / LOW. Auditable. Doctrine-versioned.

**Marked as DISCOVERY (amber badge).**

**Two columns.**

### Left — how it works

- **Per-category scoring** — Espionage · Supply Chain · Destructive · Disruptive · Cyber-Crime · Influence. Each scored 0-10 against your environment.
- **Evidence-minimum tables** — Hard rules per score band. Agent refuses to manufacture HIGH from thin evidence. "Intent=5" requires named victim — not extrapolation.
- **Weighted to overall** — Default weights tunable per your stakeholder priorities. Espionage 35% / Supply 20% / Destructive 15% / Disruptive 15% / Cyber-Crime 15% as a starting point.
- **Human approval on HIGH** — Doctrine gate. Agent never auto-commits a HIGH score. Posts to review channel; waits for sign-off.
- **Empirically tight gate** — Archimedes ran 5 scorings; zero auto-HIGH. Gate refused to invent confidence. Same discipline carries over.

### Right — sample scoring (light gray block, monospace)

```
Example: APT37 threat-box scoring

Espionage          composite 8/10  →  HIGH
Supply Chain       composite 6/10  →  MEDIUM
Destructive        composite 2/10  →  LOW
Disruptive         composite 2/10  →  LOW
Cyber-Crime        composite 2/10  →  LOW

Weighted overall: 4.9  →  MEDIUM

Rationale — why not HIGH:
Intent capped at 3 (Sector Association) — public
reporting names think tanks / journalists, no
A&D primes. Methodology refused to extrapolate.
```

**Speaker notes:**
Critical for the inconsistency-across-analysts problem: the methodology is mechanical. Every analyst hitting this with the same evidence gets the same answer. The example on the right shows the discipline working — APT37 has espionage capability that would justify HIGH if you only looked at one category, but the four floor scores dilute to overall MEDIUM. Sponsors will ask "what if we disagree with the weights?" — answer: the weights are doctrine, versioned in git, tunable in Discovery Phase per your priorities.

---

## Slide 8 — CMDB + GTI integration — proposed shape

**Subtitle:** The bridge between external intel and your environment. The piece OpenCTI alone doesn't give you.

**Marked as DISCOVERY (amber badge).**

**Layout:** 5-box pipeline diagram, left to right, with arrows. Three amber "validation needed" callouts below.

**Pipeline:**

```
[ Graded finding ]  →  [ IOC / CVE extraction ]  →  [ CMDB asset match ]  →  [ GTI risk overlay ]  →  [ Prioritized output ]
   OpenCTI report          Pull indicators &           Match against your        Mandiant Advantage         Per-team brief
   + Admiralty digraph     CVE refs from the           asset inventory +         risk score for the         + dashboard tile
   + WEP                   finding body                criticality field         CVE / actor / TTP          + playbook trigger
```

**Validation callouts (amber boxes below):**

- *Validate: CMDB tool + API access (ServiceNow / Tanium / Axonius / other)*
- *Validate: asset-criticality field schema (score vs. tag vs. owner-tier)*
- *Validate: GTI license tier — read API for risk scores at finding-level granularity*

**Speaker notes:**
This is the slide where "AI in CTI" becomes specific to YOUR environment. OpenCTI alone gives you the external intel; CMDB alone gives you the asset inventory; GTI alone gives you a risk overlay. Athena connects all three so "CVE-2026-XXXX is hot" becomes "23 of YOUR assets are exposed; 4 are crown-jewel-tier; GTI rates this an 80; here's your prioritized list." The amber callouts at the bottom are the explicit Discovery questions — three integration paths we need to validate before sizing the build.

---

## Slide 9 — Stakeholder-tailored output — proposed matrix

**Subtitle:** One canonical record. Many renderings. Each team gets what they need, no more.

**Marked as DISCOVERY (amber badge).**

**Three-column table:**

| Stakeholder team | What they get | Cadence |
|---|---|---|
| **SOC** | IOCs, Splunk hunt queries, detection-tier signal | Daily Layer-2 + ad-hoc FLASH |
| **Vuln Mgmt** | CVE deadlines, KEV status, CMDB exposure list, patch posture | Weekly summary + FLASH on KEV adds |
| **Incident Response** | Actor TTPs, MITRE mapping, playbook handoffs, lessons | Weekly + on-demand `/investigate` |
| **Threat Intel team** | Full analyst-grade markdown, source grading detail, doctrine audit | Daily Layer-1 + weekly synthesis |
| **Leadership** | Executive Layer-2: top threats, exposure heatmap, posture summary | Weekly executive brief |

### Footer (amber, italic, centered)

*Validation needed: confirm the team list above matches your org. Confirm contact owner per team (who signs off on the per-team format). Confirm cadence expectations with each team lead before build.*

**Speaker notes:**
"Prioritization drift across the org" is solved here. Every team sees the same canonical findings, rendered for their workflow. Vuln Mgmt sees CVE deadlines; SOC sees Splunk hunt queries; Leadership sees the executive heatmap. Same source intel; same prioritization model; different surface. The discipline is in the doctrine — INTEL-BRIEF-STANDARDS specifies the per-team rendering rules.

---

## Slide 10 — "What matters now" dashboard — wireframe sketch

**Subtitle:** For discussion. The dashboard rendering surface; refined in Discovery.

**Marked as DISCOVERY (amber badge).**

**Layout:** 4-quadrant dashboard mock inside a single bordered frame. Header bar reads "Athena · What matters now · [date]".

### Quadrant 1 — TOP THREATS TODAY (top left)

```
1.  CVE-2026-0300 (PAN-OS) · A1 · 23 exposed assets
2.  Checkmarx Jenkins AST · B2 · DIB CI/CD impact
3.  Ivanti EPMM CVE-2026-6973 · KEV expired
4.  SailPoint GitHub repos · B2 · IGA stack
5.  Operation HookedWing · C3 · monitoring
```

### Quadrant 2 — YOUR EXPOSURE HEATMAP (top right)

```
Critical:    4 assets   ████
High:        18 assets  ████████
Medium:      37 assets  ██████
Low:         142 assets ███

[hover: drilldown to CMDB CI list]
```

### Quadrant 3 — FLASH QUEUE + PENDING GATES (bottom left)

```
FLASH queued:    2 (quiet-hours)
/approve-scoring waiting:  1 (UNC1549 → HIGH proposed)
Retraction proposed:  0
Source-grade ratify: 2 (Rapid7, SOCRadar)

→ click any item to action
```

### Quadrant 4 — RECENT ACTIVITY (bottom right)

```
08:00  Morning brief published  ·  5 findings
07:30  Pre-brief collection  ·  47 raw items
06:00  FLASH sweep  ·  clean
00:00  FLASH sweep  ·  clean
Yesterday 16:00  Afternoon brief  ·  3 findings
```

### Footer (amber, italic, centered)

*Validation needed: hosting model (cloud / on-prem) · auth/SSO integration · per-team filters · drilldown depth into CMDB*

**Speaker notes:**
Wireframe — for discussion, NOT a committed design. Four quadrants address four different consumption modes: "what's hot" (top threats), "where am I exposed" (heatmap), "what needs my attention" (FLASH+gates), "what just happened" (activity log). Sponsors will want to see this — leadership consumes the dashboard primarily. Dev team will ask about hosting / auth / data refresh; that's all Discovery work. Note this is also where "inconsistent prioritization across the org" gets visually resolved — everybody sees the same top-5 list.

---

## Slide 11 — Interactive Q&A — proposed slash commands

**Subtitle:** Analyst asks a question in Teams; agent investigates against OpenCTI + GTI + the corpus; returns analyst-grade response.

**Marked as DISCOVERY (amber badge).**

**Layout:** Full-width monospace block showing a sample analyst conversation.

```
[Analyst]  /investigate UNC1549

[Athena]
UNC1549 — Iranian-cluster espionage actor (a.k.a. Smoke Sandstorm).
Tracking since 2024. Last 90 days: 3 named A&D victims (Mandiant
2026-04-12, CrowdStrike 2026-04-28, MSTIC 2026-05-02).

Threat-box scoring: HIGH (5.4 weighted) — Espionage HIGH (10),
Supply Chain LOW, Destructive LOW, Disruptive LOW, Cyber-Crime LOW.
Last /update-tracking: 2026-05-09.

Current exposure in your environment:
  • 0 confirmed IOC hits in Splunk -30d
  • 4 CVEs tied to UNC1549 tradecraft; 2 unpatched on 11 assets
  • GTI risk score: 84 (threat-actor entity)

Action items proposed:
  • Patch CVE-2026-XXXX on the 11 exposed assets (Vuln Mgmt)
  • Confirm detection coverage for the named TTPs (SOC)
  • Review UNC1549 dossier for any sector-specific update (Intel team)

Sources cited: Mandiant 2026-04-12, CrowdStrike 2026-04-28, MSTIC
2026-05-02, internal /update-tracking 2026-05-09.

[Analyst]  /report UNC1549 last 30 days

[Athena]
Generating threat report from OpenCTI + GTI corpus...
[returns Layer-1 markdown brief with full source citations]
```

**Speaker notes:**
Show what "ask the agent a question" actually looks like. The shape is borrowed from Archimedes' Discord listener — slash commands, structured response, source citations. Three things to emphasize: (1) the agent investigates LIVE against OpenCTI + GTI, not just the cached corpus; (2) it returns the same analyst-grade format the briefs use, not a chatbot ramble; (3) every claim cites a source. If the audience asks "what if the agent gets it wrong" — the answer is single-source-veto + WEP discipline + every refusal logged for review.

---

## Slide 12 — Automated response playbooks — proposed integration shape

**Subtitle:** Agent posts; your SOAR orchestrates; result feeds back. Two webhooks each direction.

**Marked as DISCOVERY (amber badge).**

**Top row — 4 actor boxes (left to right, colored bars):**

`Athena` (dark blue) → `SOAR (your tool)` (mid blue) → `Splunk + CMDB` (green) → `Athena corpus` (dark blue)

**Numbered sequence below:**

1. FLASH triggers — Athena graded CVE-2026-XXXX as A1 + active exploitation + 4 exposed assets
2. Athena POSTs webhook to SOAR with finding-id, IOCs, CMDB asset list, suggested playbook
3. SOAR runs playbook — quarantine VLAN, force patch, page on-call, open ServiceNow ticket
4. SOAR POSTs result back to Athena — playbook id, action results, ticket ref
5. Athena writes outcome to corpus — finding now carries response-action provenance
6. Next brief surfaces the closed-loop event under "Recent activity / closed actions"

**Validation footer (amber box):**

*Validation needed: which SOAR (Tines / Torq / ServiceNow SecOps / Splunk SOAR / other), playbook catalog, auth/auth model for the webhooks, change-management approval path for automated actions.*

**Speaker notes:**
The bidirectional webhook pattern is what closes the loop on "delays response actions for high-impact threats." Without it, the agent just produces graded intel; with it, the intel triggers actual response. Critical caveat for sponsors: automated response on production assets is high-stakes. Discovery Phase needs to lock down which playbooks are agent-triggerable vs. analyst-confirmed-then-triggered. Pattern: low-risk actions auto-fire (quarantine, ticket open); destructive actions require human approval (block, isolate, take down).

---

## Slide 13 — Architecture sketch — proposed

**Subtitle:** Starting point. Component layout. Discovery validates the integration paths.

**Marked as DISCOVERY (amber badge).**

**Layout (sketch this diagram in your tool):**

- **Top row:** `Intel inputs` (left, blue: OpenCTI · Mandiant GTI · RSS · vendor blogs · Splunk) → `Claude (Athena)` (center, dark blue) → `Outputs` (right, green: Teams · Dashboard · SOAR webhooks · audit log)
- **Middle row:** 8 subagent boxes in a ring — collector, grader, analyst, red-team, actor-profiler, vuln-tracker, briefer, librarian. Each labeled with their role.
- **Amber band below:** *Validation needed: OpenCTI deployment status · CMDB API path · GTI license tier · SOAR webhook capability · Teams app/channel access*
- **Gray band below that:** Doctrine (versioned in git): LEGAL-POLICY · INTEL-GRADING · INTEL-BRIEF-STANDARDS · THREAT-BOX-METHODOLOGY · RETRACTION-POLICY · FLASH-POLICY
- **Caption (italic, centered):** Each subagent: own context, own write scope, own doctrine subset. Orchestrator never reads raw articles. Librarian is the only writer to side effects (corpus, Teams, SOAR, audit log).

**Speaker notes:**
This is the architecture for sponsors. Frame it as "this is the starting point we'd anchor on; Discovery validates the integration paths." The amber band lists the four integration unknowns explicitly — those are the questions we're asking sponsors to commit working-session time to resolve. If a dev in the room asks "why subagents instead of one prompt" — answer: context isolation. Proven pattern; lower error rate; auditable per-role.

---

## Slide 14 — Doctrine as code — the working memory layer

**Subtitle:** Versioned in git. Reviewable by analysts AND engineers. The agent's job description.

**Bullets:**

- **LEGAL-POLICY.md** — Prohibited queries, authorized targets, ITAR boundary, copyright. Read before every tool call.
- **INTEL-GRADING.md** — Admiralty 6×6 + WEP + single-source-veto + corroboration rules. Read by grader.
- **INTEL-BRIEF-STANDARDS.md** — Per-stakeholder rendering rules, word/char budgets, Smart Brevity, preflight checklist. Read by briefer.
- **THREAT-BOX-METHODOLOGY.md** — Per-category composite scoring + evidence-minimum tables. Read by actor-profiler on every scoring run.
- **RETRACTION-POLICY.md** — When to retract vs. correct, additive (never silent), 72h auto-downgrade clock.
- **FLASH-POLICY.md** — Trigger conditions, quiet hours, critical-override threshold.

### Why-it-matters footer (green callout box, centered)

Doctrine is what the agent's job description used to be locked inside a single prompt. Splitting it into versioned files means analysts, engineers, and compliance can review and iterate it like code. It also makes "why did the agent do that" answerable — every behavior traces back to a doctrine line.

**Speaker notes:**
Doctrine-as-code is the architectural answer to "how do we govern agent behavior in a regulated environment?" Every rule the agent follows is in a .md file. Every change is in git history. Every refusal is traceable. Engineers can review the structure; analysts can review the methodology. Compliance can audit both. This is the layer that makes the system defensible — not just performant. Discovery Phase includes a doctrine review with your intel team lead — they sign off on the methodology before we commit to building against it.

---

## Slide 15 — Discovery Phase — proposed scope

**Subtitle:** 2-3 weeks of structured work. Validated requirements doc, target architecture, sized build plan.

**Marked as DISCOVERY (amber badge).**

**Three-row table:**

| When | Focus | Activities + outcomes |
|---|---|---|
| **Week 1** | Requirement validation + stakeholder interviews | Working sessions with each stakeholder team (SOC, IR, Vuln Mgmt, Intel, Leadership). Confirm requirements, weight priorities, lock the per-team rendering format. Capture analyst-day shadow observations to ground the "cost of status quo" numbers. |
| **Week 2** | Integration POCs + doctrine review | Hands-on POCs for OpenCTI read, GTI API call, CMDB asset lookup, SOAR webhook. Each is a 1-day spike. Doctrine review with intel team lead — adopt-as-is, modify, or reject. Identify any deal-breakers early. |
| **Week 3** | Synthesis + sized build plan | Produce validated requirements doc, target architecture (no longer "proposed"), build plan with phases + confidence intervals, integration spec for each external system. Decision gate: green-light build, request additional scoping, or stop. |

### Deliverables footer (green callout, centered)

**Deliverables at end of Discovery:** validated requirements doc · target architecture · sized build plan · integration POC results · stakeholder sign-off

**Speaker notes:**
Discovery is a contained scope with a hard decision gate at the end. Three weeks; named deliverables; either we have a sized build plan or we have a documented reason not to proceed. Either outcome is valuable. Push for sponsor commitment to attend working sessions personally — without their input on weights and per-team rendering, we'll build the wrong thing efficiently.

---

## Slide 16 — Open questions to resolve in Discovery

**Subtitle:** Every one of these blocks a build commitment. Discovery is how we close them.

**Marked as DISCOVERY (amber badge).**

**Bullets:**

- **CMDB integration** — Which CMDB tool? API access available? Asset-criticality schema (score / tag / owner-tier)? Who owns the integration on your side?
- **GTI / Mandiant Advantage license** — Which license tier? API access for risk-score-at-finding-level granularity? Rate-limit headroom for daily volume?
- **SOAR / playbook engine** — Which tool (Tines / Torq / ServiceNow SecOps / Splunk SOAR / other)? Existing playbook catalog? Change-management path for automated actions on production?
- **Stakeholder team list** — Confirm the team list (SOC, IR, Vuln Mgmt, Intel, Leadership). Contact owner per team. Cadence + format expectations per team.
- **OpenCTI deployment status** — Already running in production? Connector inventory? Reasonable read-load on current instance? STIX 2.x or older?
- **Doctrine review** — Intel team lead available to review the 6 doctrine files? Modifications needed before the agent runs against them?
- **Hosting + auth** — Where does the dashboard live (cloud / on-prem)? SSO integration path? Per-team access controls?
- **Build team + timeline expectations** — FTE availability for the build phase? Target go-live date? Capacity for ongoing doctrine + corpus maintenance?

**Speaker notes:**
Read these out loud. The point is to make explicit what's NOT yet known — sponsors should see that we've thought about what could go wrong and have a structured plan to surface answers. If a sponsor in the room can already answer one of these, capture it immediately — that's pre-Discovery progress. The deck deliberately doesn't pretend to have answers we don't. Honest scope wins.

---

## Slide 17 — The ask

**Subtitle:** What we need from sponsors today to start Discovery next week.

**Bullets:**

- **Sponsor a 2-3 week Discovery Phase** — Named budget owner. Time commitment for working sessions. Clear scope as outlined.
- **Name working-session owners** — One per open dimension: CMDB, GTI, SOAR, Stakeholder list, OpenCTI, Doctrine. ~4-6 hours each across the phase.
- **Commit to the Discovery-end decision gate** — End of week 3: review validated requirements + target architecture + sized build plan. Decide: build / additional scoping / stop.
- **Confirm Athena as the working project name** — (or assign a different one). Used in working-session artifacts and the final build proposal.
- **Approve initial access requests for the POC integrations** — Read-only API access to OpenCTI, GTI, CMDB. Sandbox SOAR access. Teams app registration for the dashboard wireframe.

**Speaker notes:**
Five concrete asks. None of them commit to a build; all of them get us to a sized build plan. If sponsors push back on any specific ask — capture the resistance and route around it; don't argue. The point is to get to Discovery, not to win every line item. Closing line for this slide: "with these five things, we can start Discovery next Monday and have a sized build plan in three weeks."

---

## Slide 18 — What Discovery delivers

**Subtitle:** End-of-phase deliverables. Then you decide whether to fund the build.

**Bullets:**

- **Validated requirements document** — Every requirement bullet from the intake, validated through working sessions, with explicit acceptance criteria and stakeholder sign-off.
- **Target architecture** — Component diagram with integration paths locked. No more "proposed" — this is what we'd build. Reviewable, defensible, versionable.
- **Sized build plan with confidence intervals** — Phased delivery, FTE estimates, dependency map, risk register. "8 weeks ± 2" not "some amount of time."
- **Integration POC results** — OpenCTI read working. GTI risk-score lookup working. CMDB asset match working. SOAR webhook firing. Each demonstrated in the working sessions, not just claimed.
- **Doctrine sign-off** — Intel team lead has reviewed the 6 doctrine files and approved (or marked the modifications needed).
- **Stakeholder sign-off** — Each stakeholder team owner has confirmed the proposed per-team rendering format and cadence.
- **A clear go/no-go decision** — Either: "we have what we need to build, here's the plan" — or — "here's the specific reason this isn't ready to build yet." Both outcomes are valuable.

**Speaker notes:**
Close on the value of Discovery whether it leads to a build or not. A "no, not yet" answer that surfaces three specific blockers is worth as much as a "yes" — because we don't waste 8 weeks of build time on a project that wasn't ready. Both outcomes produce a defensible artifact. That's the discovery framing's strongest argument.

---

## Slide 19 — Q&A

**Layout:** Big centered "Questions?" + subtitle + presenter contact.

**Title (centered, large):** Questions?

**Subtitle (italic, centered):** And what you'd want to validate first in Discovery.

**Footer (centered):** [Presenter name] · [Email / Slack / Teams handle]

**Speaker notes:**
Likely questions to be ready for:

- **Cost** — Discovery is mostly your time + working-session hours; the build itself is the unknown until Discovery sizes it.
- **What if Discovery says "no"** — both outcomes produce a defensible artifact (see slide 18).
- **Why Claude vs. an in-house ML model** — long-context + tool-use + framework-application discipline at this maturity is hard to build from scratch; Claude solves the analyst-layer problem cheaper and faster than a custom model would.
- **Security review** — every external integration is auth-bounded; every action is logged; every doctrine refusal is auditable. Discovery includes a security review touchpoint.

---

*End of deck. 19 slides, ~22 minutes, ~70 seconds per slide.*

*This markdown corresponds 1:1 with `athena-discovery.pptx` — pick whichever surface is friendlier for your template-merge workflow.*
