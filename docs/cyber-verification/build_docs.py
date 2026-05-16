"""Generate the two Word documents for the Anthropic Cyber Verification
Program submission:

  1. archimedes-cyber-verification-draft.docx  — content to copy into form fields
  2. how-to-submit.docx                        — step-by-step submission guide

Both written with python-docx. Run:
  uv run python docs/cyber-verification/build_docs.py
"""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor


# ---------- style helpers ----------


def heading(doc: Document, text: str, level: int = 1) -> None:
    """Add a heading with consistent style — avoids placeholder weirdness across
    Word templates."""
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.name = "Calibri"
        if level == 1:
            run.font.size = Pt(24)
            run.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)
        elif level == 2:
            run.font.size = Pt(16)
            run.font.color.rgb = RGBColor(0x1F, 0x3A, 0x5F)
        else:
            run.font.size = Pt(13)
            run.font.color.rgb = RGBColor(0x4A, 0x90, 0xE2)


def para(doc: Document, text: str, *, italic: bool = False, bold: bool = False, size: int = 11) -> None:
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(size)
    run.italic = italic
    run.bold = bold


def bullet(doc: Document, text: str, *, level: int = 0, bold_lead: str | None = None) -> None:
    """Bullet. If bold_lead is set, that prefix is bolded and the rest is plain."""
    p = doc.add_paragraph(style="List Bullet" if level == 0 else "List Bullet 2")
    if bold_lead:
        r1 = p.add_run(bold_lead)
        r1.bold = True
        r1.font.name = "Calibri"
        r1.font.size = Pt(11)
        r2 = p.add_run(text)
        r2.font.name = "Calibri"
        r2.font.size = Pt(11)
    else:
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(11)


def num(doc: Document, text: str, *, bold_lead: str | None = None) -> None:
    p = doc.add_paragraph(style="List Number")
    if bold_lead:
        r1 = p.add_run(bold_lead)
        r1.bold = True
        r1.font.name = "Calibri"
        r1.font.size = Pt(11)
        r2 = p.add_run(text)
        r2.font.name = "Calibri"
        r2.font.size = Pt(11)
    else:
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(11)


def code_block(doc: Document, text: str) -> None:
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = "Consolas"
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)


def divider(doc: Document) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("• • •")
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x99, 0x99, 0x99)


# =====================================================================
# Document 1 — The draft (content to paste into the form fields)
# =====================================================================


def build_draft() -> Path:
    doc = Document()

    # Cover heading
    heading(doc, "Anthropic Cyber Verification Program — Submission Draft", level=1)
    para(
        doc,
        "Reference content for the form at claude.com/form/cyber-use-case. "
        "Copy each section into the corresponding form field; adjust the bracketed "
        "placeholders before submitting.",
        italic=True,
    )
    para(doc, "")  # spacer
    para(
        doc,
        "Project: Archimedes — an autonomous defensive CTI analyst agent built on Claude Code.",
        bold=True,
    )
    divider(doc)

    # --- Section 1
    heading(doc, "1.  Use case description", level=2)
    para(
        doc,
        "Archimedes is an autonomous defensive Cyber Threat Intelligence (CTI) "
        "analyst agent built on Claude Code. It serves a defensive CTI workflow "
        "at [your organization / team name], a US aerospace and defense "
        "contractor environment.",
    )
    para(
        doc,
        "The agent ingests open-source intelligence (~45 vetted sources including "
        "CISA KEV, Mandiant, Unit 42, MSTIC, CrowdStrike, BleepingComputer, "
        "The Record), grades each source-claim per the NATO Admiralty Scale "
        "(AJP-2.1), and produces twice-daily intelligence briefs (08:00 + 16:00 "
        "EDT) to a private Discord channel for the security team and leadership. "
        "It also maintains a structured corpus of threat actor dossiers and CVE "
        "tracking entries, and supports operator-driven queries via slash commands "
        "(/cve <id>, /investigate <target>, /ioc-hunt <indicator>).",
    )
    para(
        doc,
        "The agent is exclusively defensive. It does not generate exploit code, "
        "does not perform active reconnaissance against non-authorized targets, "
        "does not originate attribution claims, and does not produce offensive "
        "tooling of any kind.",
    )

    # --- Section 2
    heading(doc, "2.  Defensive intent — what the agent does NOT do", level=2)
    bullet(
        doc,
        "Hard Rule 3 in the agent's doctrine. Agent refuses to generate "
        "proof-of-concept code, payloads, exploit guides, or assistance "
        "attacking any system — including for \"testing,\" \"research,\" or "
        "\"educational\" purposes.",
        bold_lead="No exploitation, ever. ",
    )
    bullet(
        doc,
        "Hard Rule 4. Active reconnaissance is permitted only against assets "
        "in infrastructure/authorized-targets.yaml (the operator's own "
        "infrastructure). MCP wrappers for SpiderFoot and theHarvester enforce "
        "module-level passive-only allowlists in code — non-passive modules are "
        "rejected before any HTTP call is made.",
        bold_lead="No active scanning of third parties. ",
    )
    bullet(
        doc,
        "Hard Rule 2. The agent only reports what other named sources have "
        "already attributed, citing them; it does not generate first-time "
        "threat-actor attributions.",
        bold_lead="No originating attribution. ",
    )
    bullet(
        doc,
        "Hard Rule 7. If a query surfaces credentials, the agent counts and "
        "reports exposure, then discards. It does not store credentials, "
        "hashes-labeled-as-credentials, or personally identifiable information.",
        bold_lead="No credential handling. ",
    )

    # --- Section 3
    heading(doc, "3.  Safety controls in place", level=2)
    bullet(
        doc,
        "Every behavior the agent exhibits traces to a versioned .md file in "
        "the project's doctrine/ directory. Six files (LEGAL-POLICY, "
        "INTEL-GRADING, INTEL-BRIEF-STANDARDS, THREAT-BOX-METHODOLOGY, "
        "RETRACTION-POLICY, FLASH-POLICY) govern grading, brief composition, "
        "retraction handling, and trigger conditions. Versioned in git; "
        "reviewable; auditable.",
        bold_lead="Doctrine-as-code. ",
    )
    bullet(
        doc,
        "Hard-coded allowlists in the integration layer refuse non-passive "
        "operations before any HTTP request — see "
        "mcps/spiderfoot/src/spiderfoot_mcp/policy.py for the canonical example.",
        bold_lead="MCP wrappers enforce policy in code, not prose. ",
    )
    bullet(
        doc,
        "A dedicated librarian subagent is the only component allowed to write "
        "to git, Splunk, or Discord. Every external publication passes through "
        "a LEGAL-POLICY content-scan gate that refuses credential patterns, "
        "TLP:RED material, and ITAR-questionable detail.",
        bold_lead="Single-writer side effects. ",
    )
    bullet(
        doc,
        "Every agent action produces (1) a git commit, (2) a Splunk event with "
        "run_id, and (3) a Discord channel post. The three logs are joinable on "
        "run_id; any action can be reconstructed post-hoc.",
        bold_lead="Three-log audit trail. ",
    )
    bullet(
        doc,
        "Every Hard Rule refusal is logged to "
        "infrastructure/policy-violations.yaml with timestamp, attempted "
        "action, and reason. Auditable record of what the agent was asked to do "
        "but refused.",
        bold_lead="Refusal logging. ",
    )
    bullet(
        doc,
        "When the agent proposes a HIGH threat-actor scoring, it does not "
        "auto-commit — it posts to a review channel and waits for an "
        "operator's explicit approval (/approve-scoring <actor-id>). Five of "
        "five actor scorings to date have stayed below HIGH; the gate is preserved.",
        bold_lead="Human approval gates on high-stakes decisions. ",
    )

    # --- Section 4
    heading(doc, "4.  Example queries (the kind that would be made)", level=2)
    bullet(
        doc,
        "Pull NVD record, CISA KEV status, vendor patch advisory for a "
        "vulnerability; summarize patch posture and defensive priority for "
        "the security team. Use case is patch-management and defensive "
        "prioritization, not exploit research.",
        bold_lead="/cve CVE-2026-XXXX — ",
    )
    bullet(
        doc,
        "Pull existing tracked-actor dossier, summarize recent reporting from "
        "Tier-1 sources (Mandiant, Unit 42, MSTIC) on tactics, techniques, and "
        "procedures; produce a defender-focused situational summary.",
        bold_lead="/investigate <actor> — ",
    )
    bullet(
        doc,
        "Check an indicator against the local corpus, internal Splunk telemetry, "
        "and external reputation services (VirusTotal, AbuseIPDB). Used to "
        "determine whether a suspicious IP has any history relevant to defense.",
        bold_lead="/ioc-hunt <indicator> — ",
    )
    bullet(
        doc,
        "Automated runs that read overnight OSINT, grade against Admiralty, "
        "surface 4-8 items the operator's security team and leadership should "
        "know about. Output is a ~250-word Smart Brevity summary in a Discord "
        "channel.",
        bold_lead="Twice-daily morning + afternoon briefs — ",
    )

    # --- Section 5
    heading(doc, "5.  Why the AUP filter is firing today", level=2)
    para(
        doc,
        "The agent's defensive CTI work involves naming CVEs, threat groups, "
        "and TTPs — the same surface vocabulary used in offensive security "
        "research. The Anthropic Usage Policy classifier appropriately errs "
        "on the side of caution on cyber-adjacent queries, and we have hit "
        "refusals on routine defensive workflows (for example, requesting a "
        "patch-posture summary for a published, CISA-listed CVE). Cyber "
        "Verification will calibrate the classifier to this account's verified "
        "defensive use case so the agent's standard /cve workflow can proceed "
        "without manual rephrasing.",
    )

    divider(doc)
    heading(doc, "Notes before submitting", level=2)
    bullet(
        doc,
        "Replace [your organization / team name] in Section 1 with the name "
        "you want on the record.",
    )
    bullet(
        doc,
        "If the form has a character limit per field, prioritize Sections 1, "
        "2, and 3 over Sections 4 and 5 — the latter two are nice-to-have, "
        "the former three are load-bearing.",
    )
    bullet(
        doc,
        "If asked for supporting links or repository visibility, the Archimedes "
        "repo is at https://github.com/ryansketch01/archimedes — note that "
        "doctrine/ is the most useful directory for reviewers to look at.",
    )

    out = Path(__file__).parent / "archimedes-cyber-verification-draft.docx"
    doc.save(out)
    return out


# =====================================================================
# Document 2 — How to submit
# =====================================================================


def build_howto() -> Path:
    doc = Document()

    heading(doc, "How to submit the Cyber Verification request to Anthropic", level=1)
    para(
        doc,
        "Step-by-step. The submission is via a web form on Anthropic's site, "
        "not an upload. The draft Word document is a reference you paste from "
        "while filling out the form.",
        italic=True,
    )
    para(doc, "")
    divider(doc)

    heading(doc, "What you have", level=2)
    bullet(
        doc,
        "A draft Word document in this same folder: "
        "archimedes-cyber-verification-draft.docx",
    )
    bullet(
        doc,
        "A token-bound URL from Anthropic's API error response, sitting in your "
        "Discord channel #commands (channel ID 1499953336391045170).",
    )

    heading(doc, "Step 1 — Locate the form URL", level=2)
    num(
        doc,
        "Open Discord and go to the #commands channel.",
    )
    num(
        doc,
        "Scroll up to the bot's error reply from when /cve CVE-2026-44277 was "
        "attempted (timestamp ~11:01 EDT on 2026-05-13).",
    )
    num(
        doc,
        "The reply contains a link starting with https://claude.com/form/cyber-use-case?token= "
        "followed by a long token string. That entire URL is your form link.",
    )
    bullet(
        doc,
        "Important — copy the FULL URL including the ?token=... part. The bare "
        "https://claude.com/form/cyber-use-case will not work without the token.",
    )

    heading(doc, "Step 2 — Open the form", level=2)
    num(doc, "Paste the full URL into a browser tab and press Enter.")
    num(
        doc,
        "You should see Anthropic's Cyber Use Case form. It is hosted by "
        "Anthropic, asks for your account-identifying info plus a description "
        "of your defensive use case.",
    )
    bullet(
        doc,
        "If the form does not load or shows an error like \"token expired,\" "
        "the token may have aged out. To regenerate: trigger another /cve "
        "command in #commands; the new error reply will contain a fresh token-bound URL.",
    )

    heading(doc, "Step 3 — Fill out the form using the draft", level=2)
    num(
        doc,
        "Open archimedes-cyber-verification-draft.docx in Word (in this same folder).",
    )
    num(
        doc,
        "For each form field, copy the matching section from the draft into the "
        "form field. The draft is organized in the order the form typically asks them:",
    )
    bullet(
        doc,
        "Form field \"Use case description\" → copy Section 1 of the draft.",
    )
    bullet(
        doc,
        "Form field \"How do you ensure safe use\" / \"Safety controls\" → "
        "copy Sections 2 + 3 of the draft.",
    )
    bullet(
        doc,
        "Form field \"Example queries\" / \"What kinds of requests will you make\" → "
        "copy Section 4 of the draft.",
    )
    bullet(
        doc,
        "Form field \"Why are you applying\" / \"What is currently blocking you\" → "
        "copy Section 5 of the draft.",
    )
    num(
        doc,
        "Before submitting, replace any [your organization / team name] "
        "placeholders in the form fields with the actual name you want on the record.",
    )
    num(
        doc,
        "If the form asks for supporting links and the Archimedes repository is "
        "shareable, include https://github.com/ryansketch01/archimedes "
        "and note that the doctrine/ directory is the most useful starting point for reviewers.",
    )

    heading(doc, "Step 4 — Submit", level=2)
    num(doc, "Review the filled-out fields one more time.")
    num(
        doc,
        "Click the form's submit button. You should see a confirmation page or "
        "message acknowledging receipt.",
    )
    num(
        doc,
        "If you receive an email receipt from Anthropic, save it — it will "
        "likely include the contact channel they'll use to follow up.",
    )

    heading(doc, "Step 5 — Wait for approval (and how you'll know)", level=2)
    bullet(
        doc,
        "Most likely notification channel: email, to whatever address is on "
        "your Anthropic account (the same account tied to the token in the form URL).",
    )
    bullet(
        doc,
        "No published SLA — anecdotally these reviews tend to land within a "
        "few business days, but it can vary.",
    )
    bullet(
        doc,
        "Most reliable test: try /cve <any-cve-id> in Discord #commands "
        "periodically. As soon as the command succeeds (claude returns a "
        "patch-posture summary instead of an AUP refusal), verification has cleared.",
    )

    heading(doc, "Step 6 — While you wait", level=2)
    bullet(
        doc,
        "/ping, /help, /investigate, /ioc-hunt, /new-actor, /update-tracking, "
        "and /approve-scoring continue to work normally — only /cve is currently "
        "blocked by the AUP classifier.",
    )
    bullet(
        doc,
        "If you need a specific CVE briefed before verification clears, ask "
        "Claude directly in a Claude Code session (in this repo). That path "
        "does not trip the same classifier the same way and produces the "
        "patch-posture summary directly.",
    )
    bullet(
        doc,
        "Twice-daily scheduled briefs (08:00 + 16:00 EDT) continue to run "
        "without issue — they do not invoke the /cve command path directly.",
    )

    divider(doc)
    heading(doc, "If something goes wrong", level=2)
    bullet(
        doc,
        "Form returns \"token expired\" — trigger another /cve command in "
        "Discord to get a fresh token-bound URL in the bot's reply, then use that one.",
    )
    bullet(
        doc,
        "Form returns \"already submitted\" — check your email; you may have "
        "already submitted in a previous session and Anthropic is processing it.",
    )
    bullet(
        doc,
        "Form rejects content as too short — expand the Section 4 example "
        "queries with one or two more concrete examples from the agent's "
        "actual workflow.",
    )
    bullet(
        doc,
        "Approval denied — review the denial reason and respond to whatever "
        "Anthropic flagged. Common asks: clarify what is NOT done by the agent "
        "(exploitation, attribution origination, active scanning of "
        "non-authorized targets).",
    )

    out = Path(__file__).parent / "how-to-submit.docx"
    doc.save(out)
    return out


# =====================================================================


if __name__ == "__main__":
    p1 = build_draft()
    p2 = build_howto()
    print(f"Wrote: {p1}")
    print(f"       size: {p1.stat().st_size:,} bytes")
    print(f"Wrote: {p2}")
    print(f"       size: {p2.stat().st_size:,} bytes")
