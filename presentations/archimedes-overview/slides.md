# Archimedes overview — slide-by-slide spec

> Drop-into-your-own-template version. Same content as `archimedes-overview.pptx` but as plain markdown so you can build each slide natively in your company template tool (PowerPoint, Google Slides, Keynote). Each slide has its content + speaker notes. Copy what you need, edit what you don't.

**Total: 24 slides · 30 min · ~75s per slide**

---

## Slide 1 — Title

**Layout:** Title slide (centered)

**Title:**
> Building a CTI Analyst with Claude

**Subtitle:**
> Lessons from Archimedes — an autonomous threat-intel agent shipping graded briefs twice a day

**Byline:**
> [Presenter name]  ·  [Date]  ·  For: [Software dev team / OpenCTI build]

**Speaker notes:**
Open by naming the audience — Claude-familiar devs building something similar on OpenCTI. Frame: 30 minutes, no live demo, lots of real artifacts from a working system. Goal of the talk is to make the case for WHY this kind of tool needs to exist, then show that Claude makes it feasible.

---

## Slide 2 — The CTI analyst's day

**Subtitle:** What an intel analyst is actually doing at 0700

**Bullets:**

- **~45 OSINT sources to monitor** — CISA KEV, vendor blogs (Mandiant, Unit 42, MSTIC, CrowdStrike), security trades (BleepingComputer, The Record, Krebs), X/RSS firehose, threat-feed APIs
- **Hundreds of items per day** — Most are noise. A handful are signal. Sorting one from the other is the job.
- **0800 deadline for the morning brief** — Leadership wants a 5-minute readable summary — graded, prioritized, sector-relevant — by 0800 EDT. Not raw signal. Not links to articles.
- **Then again at 1600. And FLASH if something breaks.** — Plus weekly synthesis, threat-actor deep dives, retraction handling when something ships wrong. The cadence never stops.
- **Burnout is the norm** — One human, one inbox, one "too much signal, too little time" problem. The grading and delivery layers eat the time the analyst should spend on judgment.

**Speaker notes:**
Spend most of this slide on the volume problem. Devs in the audience can map this to alert fatigue in SOC work — same shape, broader source set. The handoff next slide is: leadership doesn't see this volume; they see the analyst's output. The gap between firehose and decision-maker is where the system has to live.

---

## Slide 3 — Where leadership sits

**Subtitle:** Different audience, different document

**Bullets:**

- **Reads on a phone, on the way to a meeting** — Not at a desk. Not with attachments. Scan-on-mobile is the constraint.
- **Wants the call, not the evidence** — "Should we be worried about X?" — they want yes/no/watch with one sentence of why.
- **Trusts the brief or doesn't read it** — If two briefs in a row land wrong, you've lost them. Trust is binary.
- **Doesn't speak Admiralty, WEP, or MITRE IDs** — The framework is for the analyst's rigor — the leadership view strips it back to plain English.
- **Wants source links — for the reader who wants to dig** — Trust-but-verify. Headlines that link to the source article are non-negotiable.

**Speaker notes:**
The audience here might assume "leadership" means CISO — broaden it: program managers, IR leads, contract officers in regulated industries also consume these. Point being: one canonical analytic record, two audiences. The product has to serve both without compromising either. That's the design problem the rest of the talk addresses.

---

## Slide 4 — The three jobs

**Subtitle:** Collect → Grade → Deliver. Each has a human bottleneck.

**Layout:** Three columns, each with a colored header band + body text

### Column 1 — COLLECT (mid blue header)

Read everything that hit your sources in the last 14 hours.

Decide what's worth pulling forward to the brief.

Pull IOCs, actor mentions, CVE numbers, sector tags. Don't lose context.

Cross-reference against tracked actors and prior coverage.

### Column 2 — GRADE (dark blue header)

Apply the Admiralty 6×6 to each source.

Apply Words of Estimative Probability to every forward claim.

Single-source veto on "very likely" or higher.

Refuse to originate attribution.

Test alternative hypotheses on load-bearing claims.

### Column 3 — DELIVER (muted red header)

Compose the analyst-grade markdown — full doctrine framings.

Compose the Smart Brevity Discord summary — mobile-readable.

Post to the channel, commit to git, log the audit event.

Handle retractions additively. Never silently delete.

**Speaker notes:**
Each column corresponds to a layer of the agent architecture you'll see on slide 14. Critical framing: humans CAN do all three of these. They just can't do them at the volume and cadence leadership demands without burning out. Claude doesn't replace the analyst — it does the rote 80% so the human can spend time on the 20% only humans should do (attribution calls, retraction sign-off, doctrine updates).

---

## Slide 5 — Why Claude is the right tool

**Subtitle:** Three concrete asks Claude is good at

**Bullets:**

- **Read 200 articles, surface 4 worth grading** — Long-context, summarization-at-volume. Cheap relative to an analyst-hour.
- **Apply structured frameworks consistently** — Admiralty 6×6, WEP probability bands, MITRE ATT&CK tagging. Frameworks are rules; rules are what LLMs follow well when the doctrine is written precisely.
- **Compose to a strict format** — Smart Brevity — banned phrases, active voice, lead with impact, bold the "what." Format compliance is checklist-shaped; the agent regenerates if it fails preflight.
- **Tool use for collection + delivery** — MCP wrappers expose Shodan / VirusTotal / theHarvester / SpiderFoot / Splunk as callable tools. Claude calls them; Claude reads the responses; doctrine bounds what's allowed.
- **Subagent context isolation** — Each role gets its own context — collector never sees the brief; briefer never sees raw articles; librarian is the only writer to git/Splunk/Discord. Lower error rate by construction.

**Speaker notes:**
This slide is the "so what" for the dev audience. They already know Claude — frame it in terms they understand: long-context reads, tool use, structured outputs, multi-agent. The CTI tradecraft slides earlier set up WHAT to apply Claude to; this slide says WHY Claude is the right engine. Land hard on context isolation — it's the design insight most teams miss when they try to build something like this with one big prompt.

---

## Slide 6 — Daily rhythm

**Subtitle:** The cadence is the product. Fully autonomous; humans approve only HIGH-impact calls.

**Layout:** Schedule table (3 columns: time, event, output). Highlight rows where event contains "BRIEF" with a light blue background.

| Time (EDT) | Event | Output |
|---|---|---|
| 00:00 | FLASH sweep | Check for triggers; queue if outside active hours |
| 06:00 | FLASH sweep | Same |
| 07:30 | Pre-brief collection | Pull last 14h of OSINT into raw signal |
| **08:00** | **MORNING BRIEF** | Graded findings → analyst markdown + Discord summary |
| 12:00 | FLASH sweep | Same |
| 15:30 | Pre-brief collection | Same |
| **16:00** | **AFTERNOON BRIEF** | Same |
| 18:00 | FLASH sweep | Same |
| Wed 10:30 | Threat Detection Weekly | Detection-engineering focus |
| Fri 12:00 | Threat Actor Summary | Deep dive on 1-2 tracked actors |
| Sun 10:00 | Weekly Synthesis | Patterns across the week |

**Speaker notes:**
Point out: this is the same cadence as a real intel shop. The agent runs without human oversight between events — 30+ hours of unattended ops across the launch month with zero operator interventions. FLASH sweeps catch breaking news between scheduled briefs. Quiet hours (21:00-09:00 EDT) queue routine FLASHes unless the critical-override conditions all hit (CVSS 10 + active exploitation + tracked actor + sector watchlist) — then it bypasses and pings immediately.

---

## Slide 7 — A real brief — Discord summary (Layer 2)

**Subtitle:** Layer 2 — what leadership reads on their phone at 0800. ~240 words, source-linked, natural-language dates.

**Layout:** Dark monospace code block mimicking Discord channel rendering. Use Consolas font, dark gray background (#313338), light gray text (#DCDDDE), blue links (#00AFF4).

```
Good morning. Here's your 0800 brief — Monday, May 11.

🚨  Active Threats

•  Checkmarx Jenkins AST plugin compromised in supply-chain attack
    Checkmarx warned Friday May 9 of a malicious Jenkins AST plugin on the
    Marketplace; weekend variants surfaced on GitHub. Remediation 2.0.13-848
    is out. DIB CI/CD: pin to fix version now, capture plugin hashes for IOC
    backfill.

•  SailPoint discloses GitHub repository hack
    SailPoint disclosed an April 20 incident; a third-party app vulnerability
    exposed a subset of its GitHub repos. No production customer data
    accessed; some customer info was in the repos, extent undisclosed.
    SecurityWeek floats a possible TeamPCP link; Archimedes does not endorse.

🔓  Vulnerabilities

•  CVE-2026-6973 (Ivanti EPMM on-prem): federal patch deadline expired last
   night. Unpatched on-prem fleet now in non-compliance + standing
   exploitation risk.

•  CVE-2026-42208 (BerriAI LiteLLM): KEV deadline closes today (FCEB only).
   LiteLLM-proxying shops: inventory and patch by EOD.
```

**Tip:** If you can grab the literal screenshot from `#intel-briefs` message ID `1503423239337152572`, drop it in instead — looks better than a styled code block.

**Speaker notes:**
This is the actual Discord post that shipped from #intel-briefs on 2026-05-11. Three design choices to call out: (1) headline IS the hyperlink to the source article; (2) dates are natural-language so freshness is scan-readable; (3) no themed-character voice — clean professional. Discord renders the bullets with bold-blue link headlines and embed previews under each link; show that visually if you can pull it up live.

---

## Slide 8 — Same brief — analyst-grade markdown (Layer 1)

**Subtitle:** Layer 1 — what the intel team reviews. ~730 words. Lives in git. Audit-grade.

**Layout:** Light-gray code block, monospace, full width.

```markdown
[Two enterprise security vendors — Checkmarx and SailPoint — disclosed
supply-chain compromises on SecurityWeek 18 minutes apart this morning;
both relays are vendor-self-disclosure restatements, not new third-party
research...](https://www.securityweek.com/)
Per Hard Rule 2, the TeamPCP attribution to Checkmarx Jenkins AST is a
restatement of prior reporting; SecurityWeek's framing of the SailPoint-
TeamPCP link is explicitly speculative. Archimedes does not endorse either.

Why it matters: Both vendors are widely deployed in DIB CI/CD and identity-
governance stacks — Jenkins AST in Checkmarx-using DevSecOps pipelines,
SailPoint IGA in CMMC and ITAR-program access governance — so the structural
exposure is real even where no A&D prime has been named as a victim...

## Active Threats

**[Checkmarx warned of malicious Jenkins AST plugin published to Jenkins
Marketplace](https://www.securityweek.com/...)** ... Digraph: B2 · WEP:
likely (procedural facts only — relational/attribution layer carries lower
WEP) · finding-2026-05-11-0001.

🔗 Connects to: Actor #001 TeamPCP (HIGH, roster) — Jenkins AST plugin
distribution channel is the first appearance of CI/CD-pipeline-poisoning
in the TeamPCP TTP register; dossier update queued via actor-profiler.
```

**Speaker notes:**
Same morning, same findings — but this is the analyst-grade version. Note the doctrine framings throughout: Hard Rule 2 (no originating attribution), Digraph + WEP per item, finding-id citations, single-source-veto annotations. The intel team red-team-reviews this layer. Leadership never sees it — they get Layer 2. ONE canonical record, TWO renderings, one source of truth in git. Critical insight for OpenCTI builders: this maps to STIX-Report objects with extended properties for the doctrine framings.

---

## Slide 9 — Source grading — Admiralty 6×6

**Subtitle:** NATO-standard reliability + credibility framework, applied per source per finding.

**Layout:** Two columns side by side.

### Left column — Reliability (A–F)

- **A — Completely reliable** — Sustained track record across many findings (Mandiant, Unit 42, MSTIC, CrowdStrike, MITRE, CISA).
- **B — Usually reliable** — Established but with occasional gaps (BleepingComputer, The Record, Krebs).
- **C — Fairly reliable** — Vendor blogs with mixed history; new entrants on first citation.
- **D / E / F** — Unreliable / unknown / questionable. Findings from D-F can monitor but never load-bear.

### Right column — Credibility (1–6)

- **1 — Confirmed** — Multiple independent A/B-grade sources agree.
- **2 — Probably true** — One A-grade source + plausibility test passes.
- **3 — Possibly true** — Single source, cannot be confirmed or denied.
- **4 / 5 / 6** — Doubtful / improbable / cannot be judged.

### Footer note (italic, centered)

Every finding gets a digraph (e.g., A2, B3, C3). A1 = confirmed by completely reliable source. C3 = possibly true from a single fairly-reliable source. The single-source-veto rule caps any forward claim at "likely" when only one source backs it — even if both source and content are A-grade.

**Speaker notes:**
The CTI audience knows this; the dev audience may not. Frame it as: "this is older than cyber — NATO has used Admiralty since the Cold War." Why it matters: one bad source poisons a brief. The single-source-veto is the load-bearing safety primitive — it's what stops the agent from over-promoting unverified rumors into "very likely" assessments. OpenCTI maps this cleanly to opinion / confidence fields on STIX SDOs.

---

## Slide 10 — Words of Estimative Probability

**Subtitle:** CIA-standard probability vocabulary. The agent uses these — and refuses bare hedges like "may", "might", "could."

**Layout:** Two-column vocabulary table, centered.

| Term | Probability band |
|---|---|
| **Almost certainly** | ≥95% |
| **Very likely** | 85–95% |
| **Likely** | 55–85% |
| Roughly even chance | ~50% |
| Unlikely | 15–45% |
| Very unlikely | 5–15% |
| Remote | <5% |

### Footer (italic, centered)

Why: hedging language is the #1 way analysts get misread by leadership. "Could be a problem" gets ignored; "likely escalates within 72 hours" gets a meeting.

**Speaker notes:**
WEP comes from a 1964 CIA paper by Sherman Kent — frame it as "this is how every IC analyst has been trained for 60 years." Show that the preflight checklist rejects bare "may/might/could" — every forward claim has to use the WEP vocabulary or regenerate. Dev audience analog: this is type-safety for probability statements.

---

## Slide 11 — FLASH alerts

**Subtitle:** Async — for when something can't wait for the next scheduled brief.

**Bullets:**

- **Sweeps every 6 hours** — 00:00 / 06:00 / 12:00 / 18:00 EDT. Collector + grader on the fast path.
- **Triggers (any one fires a FLASH)** — (1) Critical CVE actively exploited · (2) New attribution to a tracked actor · (3) Major breach in scope · (4) Tracked actor TTP change · (5) Sector-specific zero-day · (6) Zero-day with no patch · (7) Supply-chain compromise impacting tracked vendors
- **Quiet hours: 21:00 – 09:00 EDT** — Routine FLASHes queue to 09:00 catchup sweep — operators are not woken up casually.
- **Critical override bypasses quiet hours** — ALL of: CVSS 10 + confirmed active exploitation + tracked actor + sector watchlist hit. Anything less queues. This is the "actually wake up" threshold.
- **72-hour auto-downgrade clock on single-source FLASHes** — If no independent A/B-grade source corroborates within 72h, attribution leg auto-drops to C3 "possibly true." Tested and fired clean on MuddyWater 2026-05-09.

**Speaker notes:**
FLASH is the answer to "what if something breaks between the morning and afternoon briefs?" Critical-override has only fired once in launch ops — the gate is intentionally tight. False FLASHes train operators to ignore them; a high-precision channel preserves the "wake-up" signal. The 72h auto-downgrade clock is the doctrine pattern for handling unverified single-source attribution — ship the FLASH, but commit to retracting/downgrading if independent corroboration doesn't arrive.

---

## Slide 12 — Threat actor profiles

**Subtitle:** Per-actor dossier: profile, IOCs, threat-box scoring. Reviewed every 90 days.

**Layout:** Two columns.

### Left column — bullets

- **23 actors tracked** — Iranian cluster (UNC1549, MuddyWater, APT34, Charming Kitten, Handala), DPRK (Lazarus, APT37, Stardust Chollima), Chinese (APT28, APT40), unattributed (TeamPCP, Cl0p, Lapsus$).
- **Per-actor dossier** — profile.md (background), iocs.yaml (machine-readable), threat-box.yaml (scoring), threat-box.md (narrative).
- **Threat-box methodology** — Per-category composite scores (Espionage 35%, Supply Chain 20%, Destructive 15%, Disruptive 15%, Cyber-Crime 15%) weighted to overall HIGH / MEDIUM / LOW.
- **Hard Rule 5: HIGH requires human sign-off** — Agent never auto-commits a HIGH score. Posts to #actor-review, waits for /approve-scoring.

### Right column — scoring sample (light gray monospace block)

```
APT37 (#024) — /update-tracking 2026-05-10

Espionage          composite 8/10  →  HIGH
Supply Chain       composite 6/10  →  MEDIUM
Destructive        composite 2/10  →  LOW
Disruptive         composite 2/10  →  LOW
Cyber-Crime        composite 2/10  →  LOW

Weighted overall: 4.9  →  MEDIUM

Why not HIGH:
Intent capped at 3 (Sector Association) — public reporting
names think tanks / journalists / defectors, no A&D primes.
The methodology refused to extrapolate.
```

**Speaker notes:**
Critical empirical observation: 5 of 5 actors scored to date landed non-HIGH (UNC1549 MEDIUM, Charming Kitten LOW, APT34 MEDIUM, MuddyWater LOW, APT37 MEDIUM). The gate is tight by design — HIGH requires an A-grade source explicitly naming an A&D-prime victim, which most public reporting on these actors does not provide. When HIGH eventually lands, it'll mean something. Audience takeaway: the framework refuses to invent confidence the source material doesn't support.

---

## Slide 13 — Hard Rules — the safety boundary

**Subtitle:** Non-negotiable. Agent refuses even when prompted to bypass.

**Bullets:**

- **1 · Legal policy is non-negotiable** — Active recon only against authorized targets. Refuses to query PII-heavy sources without justification.
- **2 · Never originate attribution** — Only reports what other sources have attributed, citing them. The agent does not invent attribution claims.
- **3 · No exploitation, ever** — Never generates PoC code, payloads, or exploit guides. Not for testing, not for research, not "educational."
- **4 · Never scan third parties** — Active reconnaissance only against targets in authorized-targets.yaml. Passive-only for everything else. SpiderFoot + theHarvester MCPs enforce module-level allowlists.
- **5 · Human sign-off for HIGH threat levels** — When actor-profiler proposes HIGH, posts to #actor-review and waits for /approve-scoring. Does not auto-commit.
- **6 · 15-word quote limit, one quote per source** — Copyright compliance. Hard-enforced in the preflight checklist; refuses to ship a brief that violates it.
- **7 · Credentials are radioactive** — If a query surfaces credentials, never stores them. Counts and reports exposure; discards.
- **8 · Splunk first-party > external sources** — When first-party telemetry contradicts an external source, first-party wins and the external source gets graded down.

**Speaker notes:**
Hard Rules are the audit-defense layer. CTI is regulated-adjacent — ITAR, export-control, copyright, evidence chain. Frame for the dev audience: these are operational constraints baked into the doctrine files that load into every agent invocation. The agent refuses to violate them even when the prompt asks it to. Show what the refusal looks like — collector subagent will refuse a non-authorized port-scan request and log to policy-violations.yaml. This is what "trust" looks like for a CTI tool.

---

## Slide 14 — Architecture

**Subtitle:** Orchestrator + 9 subagents + ~8 MCP wrappers + doctrine. Everything flows through git, Splunk, Discord.

**Layout (sketch the diagram in your template tool):**

```
                              ┌────────────────────────────┐
                              │   Claude (orchestrator)    │
                              └─────────────┬──────────────┘
                                            │
        ┌─────────────────────────┐         │         ┌─────────────────────┐
        │     8 MCP wrappers      │ ◄───────┼───────► │      Outputs        │
        │  Splunk · VT · Shodan   │         │         │ Discord · git ·     │
        │  Censys · urlscan ·     │         │         │ Splunk              │
        │  theHarvester ·         │         │         └─────────────────────┘
        │  SpiderFoot · RSS       │         │
        └─────────────────────────┘         │
                                            │
   ┌──────────────────────────────────────┴──────────────────────────────────┐
   │  Subagent ring (orchestrator delegates to these — each has own context)  │
   ├──────────────────────────────────────────────────────────────────────────┤
   │  collector  · grader · analyst · red-team-analyst · actor-profiler ·    │
   │  vuln-tracker · briefer · librarian  ·  (human approval for HIGH scores)│
   └──────────────────────────────────────────────────────────────────────────┘

   ┌──────────────────────────────────────────────────────────────────────────┐
   │  Doctrine (.md files, versioned in git):                                 │
   │  LEGAL-POLICY · INTEL-GRADING · INTEL-BRIEF-STANDARDS ·                  │
   │  THREAT-BOX-METHODOLOGY · RETRACTION-POLICY · FLASH-POLICY               │
   └──────────────────────────────────────────────────────────────────────────┘
```

### Caption (italic, centered, below diagram)

Each subagent has its own context window, its own write scope, its own doctrine subset. Orchestrator never reads raw articles. Librarian is the only writer to git / Splunk / Discord. Context isolation is the design that makes the multi-agent setup robust.

**Speaker notes:**
This is the slide where devs will start drawing parallels to their own stack. Land the three big ideas: (1) subagents = role separation, (2) doctrine files = persistent prompts that load on every run, (3) one writer to externalize side effects (the librarian). If they remember nothing else from the architecture section, this slide is the thing to remember.

---

## Slide 15 — Subagents = role separation

**Subtitle:** Each agent's job description, write scope, and doctrine are minimal.

**Layout:** Four-column table.

| Subagent | Role | Write scope | Doctrine read |
|---|---|---|---|
| **collector** | raw OSINT collection | `threats/raw-signal/` | source-grades, watchlists, FLASH triggers |
| **grader** | Admiralty + WEP promotion | `threats/findings/` | INTEL-GRADING |
| **analyst** | SAT/ACH/KAC structured analysis | findings (analysis sections) | ACH/KAC method |
| **red-team-analyst** | challenge HIGH-WEP findings | findings (red-team section) | contrarian SAT |
| **actor-profiler** | dossier maintenance + scoring | `threats/threat-actors/*` | THREAT-BOX-METHODOLOGY, ACTOR-PROFILE-STANDARD |
| **vuln-tracker** | CVE tracking + KEV monitoring | `threats/vulnerabilities/*` | NVD + KEV |
| **briefer** | compose all brief types | `threats/briefs/` | INTEL-BRIEF-STANDARDS, smart-brevity skill |
| **librarian** | ship + commit + log + index | git, Splunk, Discord, indices | RETRACTION-POLICY |

**Speaker notes:**
The audience should walk away noticing: write scopes never overlap. Only the librarian can git push. Only the actor-profiler can edit a dossier. The orchestrator never writes anything. That's the design that prevents context bleed and lets red-team-analyst be genuinely contrarian — it has no investment in the primary finding because it never wrote one. Counterintuitive but real: less context per agent = lower error rate. Bigger prompts are not always better.

---

## Slide 16 — Doctrine as code

**Subtitle:** The agent's working memory. Versioned in git. Reviewed like code.

**Bullets:**

- **doctrine/LEGAL-POLICY.md** — Prohibited query patterns, authorized targets, ITAR boundary, copyright. Read before every tool call.
- **doctrine/INTEL-GRADING.md** — Admiralty 6×6 + WEP + single-source-veto + corroboration rules. Read by grader on every promotion.
- **doctrine/INTEL-BRIEF-STANDARDS.md** — Layered format (analyst-grade + Discord), word/char budgets, Smart Brevity, preflight checklist. Read by briefer.
- **doctrine/THREAT-BOX-METHODOLOGY.md** — Per-category composite scoring with evidence-minimum tables. Read by actor-profiler on every /update-tracking.
- **doctrine/RETRACTION-POLICY.md** — When to retract vs. correct, additive (never silent), 72h auto-downgrade clock. Read by grader + librarian.
- **doctrine/FLASH-POLICY.md** — 7 trigger conditions, quiet hours, critical-override threshold. Read by collector on every sweep.

**Speaker notes:**
This is the slide where the OpenCTI angle matters: doctrine files map to versioned policy docs in your repo, loaded into the agent's context as system prompts or via skill files. Frame: doctrine is what the agent's job description USED to be locked inside a single prompt. Splitting it into versioned files means you can review, test, and iterate doctrine like code. Show one example briefly — INTEL-GRADING.md has the Admiralty 6×6 lookup table + the single-source-veto rule + how to handle source corroboration. Plain English. Reviewable by an analyst lead, not just an ML engineer.

---

## Slide 17 — Where OpenCTI fits in your stack

**Subtitle:** Same shape, different substrate. Map Archimedes patterns onto STIX entities + Teams delivery.

**Layout:** Two-column compare. Left header = ARCHIMEDES (what we built), Right header = YOUR BUILD (OpenCTI + Claude + Teams).

| | Archimedes | Your build |
|---|---|---|
| **Corpus** | Markdown + YAML in git | OpenCTI STIX 2.x entity store |
| **Entities** | Free-form actor / vuln / finding files | STIX-native (Threat-Actor, Indicator, Report, Campaign, Vulnerability) |
| **Collection** | MCP wrappers around OSINT APIs | OpenCTI connectors + optional MCP wrappers |
| **Analyst layer** | Claude subagents + doctrine | Same — Claude subagents + doctrine |
| **Delivery** | Discord (#intel-briefs, #flash-alerts) | Teams (webhook + Adaptive Cards) |
| **Audit** | git history + Splunk events + Discord log | OpenCTI provenance + git for doctrine + Splunk events |
| **Source of truth** | .md files; one record, two renderings | OpenCTI; analyst layer publishes Reports + Opinions |

**Speaker notes:**
This is the big takeaway slide for the audience. The shape transfers: same analyst layer, same doctrine, same subagent decomposition. What changes: the corpus (OpenCTI STIX entities replace markdown files), connectors replace some of our MCPs, Teams replaces Discord. Critical: STIX 2.x has Report, Opinion, and Analyst-Note objects that map cleanly to our finding + analyst section + red-team section. The mapping is straightforward.

---

## Slide 18 — MCP wrappers — the integration layer

**Subtitle:** One per external data source. Doctrine enforces what's callable.

**Layout:** Full-width Python code block.

```python
# theharvester MCP — passive-only enumeration
# (.claude/mcps/theharvester/src/theharvester_mcp/models.py)

PASSIVE_SOURCE_ALLOWLIST: tuple[str, ...] = (
    "crtsh", "otx", "hackertarget", "rapiddns", "certspotter",
    "duckduckgo", "bingsearch", "virustotal", "shodan", "censys",
    # ... 45 entries total — all passive, all OSINT, no PII-heavy
)

# spiderfoot MCP — same pattern, module-level allowlist
PASSIVE_MODULE_ALLOWLIST: tuple[str, ...] = (
    "sfp_dnsresolve", "sfp_whois", "sfp_crt", "sfp_certspotter",
    "sfp_archiveorg", "sfp_threatfox", "sfp_virustotal",
    # ... 45 entries
)

# Active modules are HARD-REJECTED at input validation:
PROHIBITED_MODULES: tuple[str, ...] = (
    "sfp_tool_nmap",        # port scanning
    "sfp_tool_nuclei",      # vulnerability probing
    "sfp_spider",           # web crawling target sites
    "sfp_dnsbrute",         # DNS brute force
    "sfp_screenshot",       # target screenshots
)

# Caller asking for an active module → SpiderFootPolicyError raised
# BEFORE any HTTP call to SpiderFoot. Cannot be bypassed by prompt.
```

**Speaker notes:**
Show what "doctrine enforced at the integration layer" looks like in code. The allowlist is the load-bearing safety primitive — Hard Rule 4 (no scanning third parties) is enforced before the HTTP call, regardless of prompt. Pattern is portable: wrap any data source as an MCP, encode the policy in the wrapper, the agent literally cannot violate it. Each of the 8 wrappers has a similar policy primitive — VirusTotal/Censys don't have allowlists but they have rate-limit + auth + structured-output discipline.

---

## Slide 19 — Audit trail

**Subtitle:** Every action logged. Every change versioned. Every retraction additive.

**Bullets:**

- **Git — full corpus history** — Every brief, every finding, every actor dossier update, every doctrine change. 60+ commits across the last week alone. Provenance is queryable: git log + git blame.
- **Splunk — operational telemetry** — Every brief composed, every Discord post, every refusal, every retraction. Indexed under 'archimedes' for dashboarding and alerting on the agent's behavior.
- **Discord — delivery log** — Every channel post archived with message IDs. Retractions appended to original briefs, never replacing.
- **Hard Rule logging** — Every legal-policy refusal logged to infrastructure/policy-violations.yaml. Surfaces patterns in attempted misuse.
- **Why this matters for CTI** — CTI is regulated-adjacent — ITAR, export-control, copyright. The audit trail isn't documentation; it's evidence. When an intel team gets asked "how did you arrive at this attribution," the answer is git log + Splunk + Discord.

**Speaker notes:**
Counterintuitive insight: agents are MORE auditable than human analysts, not less. Every Claude action is logged with timestamp, tool, doctrine version, and outcome. Frame this as a feature, not just compliance — it's how you debug a bad brief, how you defend a retraction in court, how you train the next iteration of the doctrine. OpenCTI's provenance model adds another layer here — STIX has built-in 'created_by_ref' and 'modified' fields that you get for free.

---

## Slide 20 — Lesson 1: Build trust before automation

**Subtitle:** The first bad brief breaks intel-team trust permanently.

**Bullets:**

- **Human approval gates on high-stakes calls** — HIGH actor threat-box scoring → /approve-scoring. New actor scaffolding → /new-actor. Source-grade ratification → human review. The agent proposes; the human approves.
- **Agent never originates attribution** — Hard Rule 2. The agent only reports what cited sources have attributed. If Mandiant says X, Archimedes says "Mandiant says X." If no one has said X yet, Archimedes refuses to be the first.
- **Single-source veto on "very likely" or higher** — Even if a source is A-grade, a single citation caps the forward claim at "likely." The 72h auto-downgrade clock then forces re-grading if no independent corroboration arrives.
- **Retraction is additive, never silent** — When something ships wrong (and it will), the original brief stays in the record with a retraction appended. The record of being wrong IS part of the record.
- **Five non-HIGH scorings empirically validate the gate** — UNC1549, Charming Kitten, MuddyWater, APT34, APT37 — zero auto-HIGH. The gate is honest; the methodology refuses to invent confidence the evidence doesn't support.

**Speaker notes:**
This is the most important slide of the talk. If the audience walks away with one thing it should be: build the gates BEFORE you build the automation. Pattern: agent proposes, human approves on anything with reputational stakes. The agent doesn't make the call where being wrong has consequences — it surfaces the call to the human. This is also why the agent never originates attribution: attribution is a load-bearing claim with policy + legal + reputational consequences.

---

## Slide 21 — Lesson 2: Live validation > mocks for tool wrappers

**Subtitle:** 6 real bugs caught by live tests that mocks couldn't have surfaced.

**Bullets:**

- **theHarvester 4.10.1 — 3 bugs the mocks missed** — (1) PYTHONHOME env poisoning under `uv run` → SRE module mismatch. (2) Modern JSON shape emits only cmd/hosts/shodan — older docs claimed ips/vhosts/asns. (3) securityTrails source name is case-sensitive (camelCase) — argparse rejects lowercase.
- **SpiderFoot 4.0.0 — 3 more** — (1) /ping returns `["SUCCESS", "4.0.0"]` (JSON list), not the documented "pong". (2) /scanstatus is a 7-element list, not 6 — status at index 5 not 4. (3) /scaneventresultexport is CSV-only — the real JSON endpoint is /scaneventresults.
- **All 6 were "docs match mocks; docs don't match reality"** — Every wrapper had unit tests modeled on the documentation. Documentation was wrong/stale. Mocks happily passed; live runs failed in ways that took an hour each to debug.
- **Fix: bind your test suite to a running service** — Spin up theHarvester (or SpiderFoot, or OpenCTI) in CI. Hit real endpoints. Catch shape drift before it ships.

**Speaker notes:**
Concrete, painful, valuable. Six bugs is enough to make the point. The pattern: third-party tool APIs drift, documentation lags, and mocks based on documentation are confidence-without-verification. Recommendation for OpenCTI builders: run an OpenCTI instance in your CI environment and exercise your Claude-integration tests against it. Painful upfront, pays back constantly.

---

## Slide 22 — Lesson 3: Context isolation reduces error rate

**Subtitle:** Counterintuitive: less context per agent = lower error rate.

**Bullets:**

- **Orchestrator never reads raw articles** — The orchestrator schedules and delegates. The collector reads articles; the grader reads raw signal; the briefer reads graded findings. Each step's context is minimal.
- **Briefer never sees the coverage log** — Anti-repetition logic runs in the orchestrator and gets passed as "these topics are stale." Briefer composes against a clean slate per its scope.
- **Red-team-analyst never wrote the primary finding** — It's contrarian by construction because it has no investment in the leading hypothesis. The architecture creates the conditions for genuine disagreement.
- **Librarian is the only writer to side effects** — git, Splunk, Discord — all funnel through one agent. Easy to audit; easy to add rate-limiting; easy to enforce LEGAL-POLICY content-scan before any external publication.
- **Practical implication for your OpenCTI build** — Each Claude-Code-style subagent corresponds to a service or worker in your architecture. Don't try to do all of CTI in one big prompt — split by role, give each minimal context, and have one writer to the OpenCTI database.

**Speaker notes:**
Surprising result that most teams miss. The instinct is "give the model everything it might need." The opposite works better — minimal scope per agent, with the orchestrator handling cross-agent state. Land hard on the practical implication for OpenCTI: their architecture should map subagents to services or worker queues, not to one big prompt.

---

## Slide 23 — What you can build

**Subtitle:** Archimedes shape on OpenCTI + Teams. ~6-week MVP if OpenCTI is already standing.

**Bullets:**

- **Week 1 — Doctrine + scaffolding** — Write the 5-6 doctrine files (LEGAL-POLICY, INTEL-GRADING, INTEL-BRIEF-STANDARDS, THREAT-BOX-METHODOLOGY, RETRACTION-POLICY, FLASH-POLICY). Set up the OpenCTI connector patterns for your top 5 OSINT sources.
- **Week 2-3 — Subagents** — Collector, grader, briefer, librarian to start. Each as a Claude subagent or as a service calling Claude. Test against a small set of canned findings first.
- **Week 4 — Delivery + audit** — Teams webhook + Adaptive Cards. Splunk (or equivalent) for telemetry. Git for doctrine versioning. Get the daily-cadence rhythm working end-to-end.
- **Week 5 — Threat actor + vuln tracking** — actor-profiler + vuln-tracker subagents. Threat-box scoring methodology. /approve-scoring gate posting to Teams for human review.
- **Week 6 — Hardening** — Red-team-analyst subagent. Retraction handling. Hard Rule refusals at every tool wrapper. Live-validate every external integration before production cutover.
- **Then iterate** — Real-world findings will surface gaps. Doctrine evolves. Add MCPs / connectors as needed. The first quarter is when the system earns its place in the intel team's workflow.

**Speaker notes:**
Realistic timeline assuming OpenCTI is already running and you have Claude API access. The doctrine work is the underestimated piece — it's not just markdown, it's the agent's job description. Don't skip the live validation in week 6. It's where the 6 bugs from lesson 2 surface in your own stack.

---

## Slide 24 — Q&A

**Layout:** Big centered "Questions?" + subtitle + presenter contact.

**Title (centered, large):**
> Questions?

**Subtitle (italic, centered):**
> Happy to dig into any layer — architecture, doctrine, specific subagent, OpenCTI mapping.

**Footer (centered):**
> [Presenter name]  ·  [Email / Slack / Teams handle]

**Speaker notes:**
Likely questions to be ready for:
- **Cost** — Claude API token usage at this volume, ballpark $X/month.
- **What doesn't work yet** — the dashboard (deferred indefinitely), the threat-box gate hasn't fired in five tries (feature not bug).
- **Team size** — Archimedes is one operator + Claude; their build will scale with team size and OpenCTI complexity.
- **What would you do differently** — probably build OpenCTI-on-day-1 instead of markdown corpus; we got the analytic patterns right but the data model is constrained by file-based storage.

---

*End of deck. 24 slides, ~30 minutes, ~75 seconds per slide.*

*This markdown corresponds 1:1 with `archimedes-overview.pptx` — pick whichever surface is friendlier for your template-merge workflow.*
