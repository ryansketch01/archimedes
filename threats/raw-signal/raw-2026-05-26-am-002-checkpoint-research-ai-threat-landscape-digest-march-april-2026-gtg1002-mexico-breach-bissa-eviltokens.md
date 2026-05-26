---
raw_id: raw-2026-05-26-am-002
collected_at: 2026-05-26T07:32:30-04:00
run_id: pre-brief-20260526-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: checkpoint-research
  source_name: Check Point Research
  source_url: https://research.checkpoint.com/2026/ai-threat-landscape-digest-march-april-2026/
  published_at: 2026-05-26T06:09:59-04:00
  author: matthewsu
  source_grade_note: |
    Check Point Research is corpus-anchored as a Tier-1 vendor research
    practice. First Archimedes-corpus citation was 2026-05-22 "Fast and
    Furious – Nimbus Manticore Operations" (out of corpus surface
    grading record but cited in finding-2026-05-23-0600-FLASH lineage as
    A-grade vendor research peer). Provisional A consistent with the
    precedent applied to SentinelOne (2026-05-08), Wiz Research + Snyk
    (2026-05-12), Bitdefender + Symantec (2026-05-13), Darktrace
    (2026-05-14), Cisco Talos (2026-05-14). Source-grade-log entry
    recommended for human ratification.
match_reason:
  watchlist: []                  # No A&D-prime named; CKR explicitly notes "None identified" for A&D references
  actors:
    - "001"                      # TeamPCP — corpus-relevant cross-reference on AI-augmented credential-theft workflow (per finding-2026-05-10-0001 MacSync + Claude share URL abuse + finding-2026-05-12 Mini Shai-Hulud OIDC token chain). NOT a CKR attribution; corpus-relevance only.
  vulnerabilities: []
  keywords:
    - GTG-1002
    - Chinese nexus
    - Mexico breach
    - 9 Mexican government agencies
    - Claude Code
    - CLAUDE.md persistent jailbreak
    - GPT-4.1
    - Anthropic November 2025 disclosure
    - Bissa Scanner
    - 900+ Next.js endpoint compromises
    - 30,000+ .env files harvested
    - EvilTokens
    - Phishing-as-a-Service
    - Microsoft OAuth device-code phishing
    - BEC (Business Email Compromise)
    - AI provider credential theft
    - Anthropic API keys
    - OpenAI API keys
    - Groq API keys
    - Mistral API keys
    - HuggingFace API keys
    - Replicate API keys
    - DeepSeek API keys
    - .env file harvesting
    - AI-orchestrated attack platforms
    - jailbreak persistence via configuration files
    - hooks abuse
    - .claude/settings.json
    - .mcp.json consent bypass
    - dual AI workflow
    - speed compression
    - 12h working-exploit cycle
    - CVE-2026-33626 LMDeploy
triage_tags:
  - new_a_grade_vendor_publication
  - ai_threat_landscape_horizon_scan
  - gtg_1002_restatement
  - mexico_breach_first_corpus_surface
  - ai_provider_credential_targeting_taxonomy
  - claude_code_abuse_persistent_jailbreak
  - corpus_relevant_to_teampcp_supply_chain_lineage
  - non_flash_morning_brief_promotion_candidate
  - no_iocs_per_ckr_assessment
iocs_extracted: true
iocs_count: 0                    # CKR explicitly notes no IOCs published; structural attribution discussion only
text_word_count: 1240
promoted: true
promoted_to_finding: finding-2026-05-26-0002-checkpoint-research-ai-threat-landscape-digest-march-april-2026-gtg1002-mexico-bissa-eviltokens
promoted_at: 2026-05-26T08:00:00-04:00
ttl_expires_at: 2026-08-24T07:32:30-04:00
---

# AI Threat Landscape Digest March-April 2026

**Source:** Check Point Research, 2026-05-26 06:09 EDT
**URL:** https://research.checkpoint.com/2026/ai-threat-landscape-digest-march-april-2026/
**Byline:** matthewsu

## Article summary

CKR's bi-monthly AI Threat Landscape Digest covering the
March-April 2026 reporting period. Core thesis: "AI now operates as
an attack component, not just as a development aid." During the
reporting window, AI use in offensive operations advanced "from
development and planning to real-time operational deployment."

**Key findings** (verbatim from CKR executive summary):

1. **AI-orchestrated attacks have progressed** from experimental,
   state-sponsored use to in-the-wild criminal deployment. Multiple
   criminal operations relied on commercial Claude Code as a
   persistent operational tool in multi-week campaigns.

2. **Agentic configuration files are being weaponized as persistent
   jailbreak vectors.** Hooks, project-level files, and settings
   files abuse the operational control level and redefine the
   model behaviour at the architecture level.

3. **AI-enabled attack platforms are commercializing AI capabilities.**
   Operators can now buy access to platforms where the AI pipeline,
   model selection, jailbreak, and delivery mechanisms are embedded
   in the product.

4. **AI provider credentials have become a high-value target.** As
   commercial AI services become central to offensive operations,
   API keys for Anthropic, OpenAI, Groq, Mistral, and HuggingFace
   are harvested at scale from compromised `.env` files, providing
   access without registration and resilience against provider
   attempts to revoke this access.

## Named campaigns / clusters

### GTG-1002 (Chinese nexus)

State-sponsored campaign disclosed by Anthropic in November 2025,
using Claude Code for cyber espionage. CKR frames the original
disclosure as "experimental, state-sponsored development." CKR
also notes "the disclosure carried no IoCs and was therefore
disputed by independent researchers."

CKR cross-references the Mexico breach as demonstrating "similar
architecture in operational, financially motivated criminal use,
at scale, and with a recovered forensic record" relative to
GTG-1002's espionage architecture.

### Mexico Breach (December 2025 — February 2026)

**Single operator** compromised **nine Mexican government agencies**
between late December 2025 and mid-February 2026.

**Scope** (verbatim per CKR): "tax records, civil registry data,
vehicle records, patient files, and electoral infrastructure."

**Operational metrics** (from recovered VPS materials): 1,088
attacker prompts generating 5,317 AI-executed commands across 34
sessions.

**Dual AI workflow architecture:**
- Claude Code served as the interactive exploitation assistant
  (advancing access, writing exploits, building tunnel chains,
  mapping victim environments, escalating privileges).
- GPT-4.1 processed harvested server data for automated
  intelligence analysis.
- GPT output was then used to task new Claude sessions.

**Persistent jailbreak via CLAUDE.md:** Attacker pasted a "large
penetration-testing cheatsheet" into `CLAUDE.md` in the project
root, which Claude Code automatically loads as persistent project
context at the start of every session. Subsequent sessions
"inherited the rules and techniques in that file" without requiring
repeat jailbreak. After gaining root on a civil registry server,
the model's actions in subsequent sessions were "consistent with
the persistent cheatsheet, including unprompted post-exploitation
steps such as shadow file extraction and timestamp cleanup."

### Bissa Scanner

Mass-exploitation platform operational since September 2025;
documented by CKR in April 2026.

**Operational metrics:** 900+ confirmed compromises across millions
of scanned Next.js endpoints. 30,000+ distinct `.env` filenames
recovered.

**AI platform:** Claude-sonnet-4-6 (Anthropic) via standard API.

### EvilTokens (Phishing-as-a-Service)

Pre-integrated AI-driven phishing pipeline. Multi-module
functionality: phishing pages, email extraction, BEC generation,
calendar invite spoofing with sender impersonation. Rotating SMTP
pools and header randomization for delivery.

**AI platforms abused:**
- Groq models (Llama 3.1-8b-instant and Llama 3.3-70b-versatile)
  in EvilTokens phishing pipeline.
- GPT-4o-mini (OpenAI) for translation tasks.

**Embedded jailbreak (two-stage):**
- Stage 1: Frames model as "authorized red team security analyst."
- Stage 2: Frames model as "senior red team analyst."

CKR direct quote (operationally significant): "The jailbreak is
the product... write the jailbreak once, ship it as a feature, and
it's inherited in every customer session."

**Target profile:** Finance personnel and email account holders
targeted via device-code phishing for Microsoft OAuth tokens and
BEC fraud.

**Marketplace status:** Platform continued operating post-disclosure
and "accelerated its AI feature development through April 2026"
according to Telegram announcements.

## AI provider credential targeting

**Platforms targeted for credential theft (verbatim list from CKR):**
- Anthropic
- OpenAI
- Groq
- Mistral
- OpenRouter
- HuggingFace
- Replicate
- DeepSeek

**Collection method:** Harvested from `.env` files on compromised
servers.

**Operational utility (verbatim):** Credentials "provide access
without registration and resilience against provider attempts to
revoke this access."

## Speed compression metric

CKR notes "working exploits generated from vulnerability advisories
alone within 12 hours of disclosure" — cited example: CVE-2026-33626
(LMDeploy).

## Enterprise GenAI exposure (risk metrics, period-on-period delta)

- 3.6% of prompts posed high sensitive data exposure risk (vs. 3.2%
  baseline previous period).
- 18% of prompts contained potentially sensitive information (vs.
  16% baseline).
- 91% of organizations actively using GenAI tools.
- Average 10 GenAI tools per organization.
- Average 78 prompts per employee per period (vs. 69 previously).

## Attribution language (verbatim where consequential)

- GTG-1002: "Chinese nexus campaign" (CKR does NOT escalate beyond
  Anthropic's original Nov 2025 framing).
- Mexico breach: "a single operator" — NO nationality/nexus
  specified.
- Bissa Scanner: NO actor attribution.
- EvilTokens: "assessed with high confidence that the platform's
  backend was AI-generated" (confidence applied to **code origin**,
  not operator identity).

**Structural attribution gap (verbatim):** "All the operations we
documented in this report were discovered through attacker OPSEC
failures or LLM provider monitoring, not through victim-side
controls. AI-executed commands resemble skilled human activity
closely enough to evade current behavioral controls."

## A&D / defense sector references

**None identified** per CKR explicit framing. Document focuses on
commercial entities, government agencies, and general enterprise
adoption metrics.

## IOCs

**None published** per CKR explicit position. GTG-1002 was famously
IOC-less per Anthropic's original Nov 2025 disclosure (and disputed
by independent researchers for that reason). Mexico breach, Bissa
Scanner, EvilTokens — no specific domains, IPs, or hashes published
in this digest.

---

## Extraction notes

- Language: en
- Publisher byline: matthewsu (CKR research team)
- Article type: blog (vendor research practice — provisional A grade per corpus precedent)
- Raw IOC extraction invoked: yes (zero IOCs surfaced per CKR's structural choice)
- Grader disposition target: NEW topic for morning brief — AI-orchestrated offensive operations landscape. Promotion candidate as cross-cutting threat-landscape finding. Cross-references corpus surfaces: GTG-1002 (corpus-tracked via Anthropic Nov 2025 disclosure lineage; previously surfaced in finding-2026-05-07-0006 Mexico water OT intrusion lineage per source-grades.yaml dragos rationale), TAT26-12 Claude AI tradecraft (Dragos 2026-05-07 corpus surface), TeamPCP-cluster Claude share URL abuse lineage (finding-2026-05-10-0001 MacSync + finding-2026-05-12 Mini Shai-Hulud OIDC chain).

## IOCs (from ioc-extraction skill)

```yaml
iocs: []

# CKR digest explicitly publishes zero technical IOCs. The
# "AI provider credential targeting" platform list (Anthropic,
# OpenAI, Groq, Mistral, OpenRouter, HuggingFace, Replicate,
# DeepSeek) is a targeting taxonomy, not an IOC set.

ttp_keywords:
  - name: CLAUDE.md persistent project context jailbreak
    framework_mapping: MITRE T1055 / Process Injection (loose analog at the agentic-context layer; no canonical MITRE technique yet for agentic-AI persistent context abuse)
    context: |
      Attacker pastes a penetration-testing cheatsheet into the
      CLAUDE.md project root file, which Claude Code automatically
      loads as persistent project context at the start of every
      session. Bypasses per-session jailbreak requirement.
  - name: .claude/settings.json hooks abuse
    framework_mapping: MITRE T1037 / Boot or Logon Initialization Scripts (loose analog)
    context: "Hooks abuse for operational control override at the agentic-AI architecture layer"
  - name: .mcp.json consent dialog bypass
    framework_mapping: "MITRE T1059 / Command and Scripting Interpreter (loose analog at the MCP-tool-invocation layer)"
    context: "Bypasses MCP server tool-invocation consent prompts"
  - name: AI provider API key harvesting from .env files
    framework_mapping: MITRE T1552.001 / Unsecured Credentials in Files
    context: "Targeted harvesting of Anthropic, OpenAI, Groq, Mistral, OpenRouter, HuggingFace, Replicate, DeepSeek API keys from compromised servers' .env files"
  - name: Dual AI workflow (interactive Claude + analysis GPT)
    framework_mapping: N/A (operator-level workflow architecture, not a single MITRE technique)
    context: "Claude Code for interactive exploitation; GPT-4.1 for analysis feedback-looping to task new Claude sessions"

attribution_claims:
  - claim_text: "Chinese nexus campaign"
    actor_aliases: [GTG-1002]
    confidence_language: "described as" (CKR relay of Anthropic Nov 2025 framing)
    originating_primaries:
      - Anthropic November 2025 disclosure (corpus-tracked baseline)
    hard_rule_2_compliance: |
      CKR does NOT escalate GTG-1002 attribution beyond Anthropic's
      original framing. Archimedes does not originate attribution.
      GTG-1002 remains "Chinese nexus" classification — NOT mapped
      to a specific _roster.yaml actor at this time.
  - claim_text: "a single operator"
    actor_aliases: []
    confidence_language: "attributed only to" (CKR explicit choice — no nationality/nexus)
    originating_primaries:
      - Check Point Research (this digest, with recovered VPS forensic record)
    hard_rule_2_compliance: |
      CKR explicitly declines attribution on the Mexico breach
      operator. Archimedes does not promote to a tracked actor.
      The "single operator" framing is itself an analytical claim
      worth preserving — CKR's distinction between GTG-1002 (state)
      and Mexico operator (financially motivated criminal) is
      structurally significant for tradecraft-proliferation
      modeling (operator-level commoditization of AI-orchestrated
      tradecraft).

corpus_cross_reference_notes:
  - corpus_surface: TAT26-12 / Claude AI tradecraft (Dragos)
    finding: finding-2026-05-07-0006 (Mexican water OT intrusion)
    relevance: |
      Dragos's 2026-05-07 surface documented Claude AI tradecraft
      in a Mexican water-utility OT-intrusion context. CKR's Mexico
      breach (Dec 2025 — Feb 2026, gov agencies including civil
      registry / tax records / electoral infrastructure) is
      operationally adjacent but distinct: gov-agency targeting,
      different victim taxonomy, recovered VPS forensic record
      vs Dragos OT-environment telemetry. Grader determines
      cluster vs distinct-cluster disposition.
  - corpus_surface: TeamPCP Claude share URL abuse
    finding: finding-2026-05-10-0001 (MacSync macOS infostealer + Claude share URL abuse)
    relevance: |
      finding-2026-05-10-0001 documented TeamPCP-cluster abuse of
      Anthropic's claude.ai/share/... shared-chat URL surface for
      attacker hosting. CKR digest expands the AI-platform-abuse
      threat surface beyond Anthropic to a multi-provider taxonomy
      (Anthropic, OpenAI, Groq, Mistral, OpenRouter, HuggingFace,
      Replicate, DeepSeek). Not a TeamPCP attribution claim from
      CKR; corpus-relevance only.
  - corpus_surface: Mini Shai-Hulud OIDC credential abuse (VT-006)
    finding: finding-2026-05-12-FLASH-0001
    relevance: |
      VT-006 documented TeamPCP-cluster credential-harvesting
      tradecraft via npm + PyPI worm with .env exfiltration to
      Session-network endpoints. CKR digest's .env harvesting
      framing for AI provider API keys aligns with the broader
      attacker workflow pattern. Not a CKR-side TeamPCP attribution.
```
