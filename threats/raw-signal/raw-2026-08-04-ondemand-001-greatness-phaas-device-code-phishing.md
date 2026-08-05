---
raw_id: raw-2026-08-04-ondemand-001
collected_at: 2026-08-04T20:30:00-04:00
run_id: ondemand-investigate-20260804-greatness
collection_mode: investigation
source:
  # Multiple sources — primary reporting + first-party corroboration tooling
  primary:
    source_yaml_id: thehackernews
    source_name: The Hacker News
    source_url: https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html
    published_at: 2026-08-01T00:00:00-04:00
  secondary:
    - source_yaml_id: anyrun
      source_name: ANY.RUN (Threat Intelligence)
      source_url: https://medium.com/@anyrun/greatness-phaas-overview-60776ac601b7
      published_at: 2026-06-01T00:00:00-04:00
    - source_yaml_id: talos
      source_name: Cisco Talos (originating documentation, May 2023)
      source_url: https://blog.talosintelligence.com/state-of-the-art-phishing-mfa-bypass/
      published_at: 2023-05-01T00:00:00-04:00
match_reason:
  watchlist: [microsoft-365-identity, aitm-phishing, aerospace-defense-adjacent]
  actors: []          # PhaaS platform, not an attributed actor. No attribution to inherit (Hard Rule 2).
  vulnerabilities: []  # No CVE — technique abuse (OAuth 2.0 device authorization grant), not a product vuln
  keywords: [Greatness, PhaaS, "phishing-as-a-service", "device code phishing", "device authorization grant", AiTM, "adversary-in-the-middle", "Microsoft 365", "MFA bypass", "session cookie theft", "primary refresh token", OAuth]
triage_tags: [non_flash, on-demand-investigate, m365-identity, aitm-device-code, phaas-tooling, corroborated-ioc, grader-queue]
iocs_extracted: true
iocs_count: 3
text_word_count: 520
promoted: true
promoted_to_finding: finding-2026-08-04-0001
promoted_at: 2026-08-04T20:52:00-04:00
ttl_expires_at: 2026-11-02T20:30:00-04:00
---

# Greatness PhaaS adds device-code phishing to its AiTM Microsoft 365 credential/token-theft platform

On-demand `/investigate` collection (operator request, 2026-08-04). **Not a FLASH
candidate** — clears no FLASH trigger (no CVE, no tracked-actor attribution, no
first-party IOC hit, documented commodity tooling, no named A&D victim). Preserved
for grading as a tracked finding on M365-identity / AiTM relevance to the target
profile. Includes first-party corroboration of two published IOCs (VT + urlscan).

## What the sources report (collection only — not graded)

**Platform.** Greatness is a Phishing-as-a-Service (PhaaS) platform first documented
by **Cisco Talos in May 2023**, in the wild since ~2022. Subscription model sold via
public Telegram (`@GreatnessPage`, ~3,250 subscribers; registration/licensing via
`@gr8managerbot`). Price ~$120/mo at launch, raised to **~$289/mo** in Jan 2024. It
lowers the skill floor: affiliates get an attachment builder, prefilled-target lures,
brand-accurate Microsoft 365 clone pages, and Telegram capture notifications.

**Core mechanism.** Reverse-proxy **adversary-in-the-middle (AiTM)** — relays the
victim through the real Microsoft login and captures the **live session cookie after
a genuine MFA exchange**. Standard MFA does not stop it (MITRE ATT&CK T1557 AiTM,
T1539 steal web session cookie).

**What's new (per The Hacker News, Aug 2026).** Greatness added **device-code
phishing** abusing the **OAuth 2.0 Device Authorization Grant** (T1621 MFA request
generation / device-code phishing) to silently mint tokens and bypass MFA, plus
**OAuth consent abuse**, all from one operator panel / shared backend. Expanded beyond
M365 to **iCloud, Yahoo, Google Workspace**.

**Delivery + evasion.** HTML attachments with obfuscated JS; PDF/QR lures; fake
shared-document and RingCentral voicemail notifications. ~5-stage redirect chain with
User-Agent fingerprinting, IP filtering against researchers/sandboxes, and CAPTCHA /
Cloudflare "Just a moment…" gating before the phishing page renders. Static IOCs age
fast (API keys validate server-side; decoy pages served to suspected analysis hosts).

**Post-compromise.** Device registration within minutes to mint **Primary Refresh
Tokens (PRTs)** for persistence; delayed inbox/mailbox-forwarding rule manipulation to
suppress alerts; internal phishing from compromised accounts.

**Targeting.** Organizations using M365 in the US, Canada, UK, Australia, South Africa;
victim sectors incl. manufacturing, healthcare, technology, education, real estate,
construction, finance, business services. **No named A&D-prime victim** in the reporting.

## Relationship to existing corpus

- **finding-2026-07-31-0002** (CaptiveCrunch / Storm-2945 assessed Midnight Blizzard,
  APT29 #009) — same **Entra ID device-code / OAuth AiTM** technique family. Greatness
  is the *commodity / PhaaS* expression of the tradecraft APT29's Storm-2372 cluster
  pioneered. Distinct: Greatness is criminal PhaaS with no nation-state attribution —
  do NOT merge or cross-attribute.
- **finding-2026-07-14-0009** (ReliaQuest — Jalisco/OmegaLord M365 phishing kits,
  OAuth device-code abuse) — same broad TTP family; sibling commodity tooling.

## FLASH trigger evaluation (all fail)

- Trigger 1 (critical CVE + active exploitation): no CVE. FAIL.
- Trigger 2 (new tracked-actor attribution): PhaaS platform, no actor. FAIL.
- Trigger 3 (first-party IOC hit): Splunk -30d sweep 0 hits both indices. FAIL.
- Trigger 4 (tracked-actor TTP change): no tracked actor bound. FAIL.
- Trigger 5 (active nation-state A&D multi-victim campaign): commodity criminal PhaaS,
  no A&D victim named. FAIL.
- Trigger 6 (zero-day no patch): technique abuse, not a product 0-day. FAIL.

## First-party corroboration (Hard Rule 8 — first-party checked first)

- **Splunk `-30d`, both indices** (`defenseclaw_local` + `archimedes`): **0 hits** for
  Greatness / `38.248.95.214` / `aitomayu.com` / device-code / `gr8managerbot`. Clean.
  Silence is not disconfirmation (visibility-bounded on `defenseclaw_local`).

## IOC corroboration (VT + urlscan, 2026-08-04)

```yaml
iocs:
  - type: domain
    value: aitomayu[.]com
    context: >
      Greatness operator base domain (ANY.RUN example). Affiliate phishing pages are
      subdomains of form [targetname]-[token].aitomayu[.]com. VT 2026-08-04: 6/91
      engines malicious (BitDefender, ESET, Sophos, G-Data, Webroot, CRDF).
      Registered 2024-03-28.
    confidence: corroborated
    corroboration: "VT 6 engines malicious; urlscan 2 live subdomains Jun 2026"
    first_seen: 2024-03-28
  - type: domain
    value: solutionsonline-pyi5c7omq.aitomayu[.]com
    context: >
      Greatness affiliate phishing subdomain (urlscan uuid 019edf38..., 2026-06-19).
      Cloudflare-fronted (172.67.219.201), "Just a moment…" challenge gate — matches
      reported anti-analysis behavior. Shares affiliate token 'pyi5c7omq' with the
      napierparkglobal subdomain below.
    confidence: corroborated
    corroboration: "urlscan public scan 2026-06-19"
    first_seen: 2026-06-19
  - type: domain
    value: napierparkglobal-pyi5c7omq.aitomayu[.]com
    context: >
      Greatness affiliate phishing subdomain (urlscan uuid 019edcd5..., 2026-06-18),
      same token 'pyi5c7omq', same Cloudflare front + challenge gate.
    confidence: corroborated
    corroboration: "urlscan public scan 2026-06-18"
    first_seen: 2026-06-18
  - type: ipv4
    value: 38.248.95[.]214
    context: >
      Reported (The Hacker News) as Greatness AiTM proxy infrastructure. WEAKLY
      corroborated — VT 2026-08-04: only 1/91 malicious (GreyNoise), 55 harmless,
      Limestone Networks (ASN 46475). Likely scanner noise / thin confirmation; do
      NOT hard-blocklist on this evidence alone. Grade down.
    confidence: weakly_corroborated
    corroboration: "VT 1 engine only (GreyNoise); no urlscan hits"
    first_seen: 2026-08-04
attribution_claims: []   # none — commodity PhaaS, no actor attributed (Hard Rule 2)
credentials_observed: false
telegram_handles: ["@GreatnessPage", "@gr8managerbot"]   # operator channels, context only
notes: >
  Reporting stresses behavioral detection over static IOCs (server-side API-key
  validation, decoy pages, fast infra rotation). The base domain aitomayu[.]com and
  the [target]-[token] subdomain pattern are the durable pivots; the specific IP is
  low-confidence. Detection value is in the M365/Entra device-code + new-device
  registration telemetry, not the atomic indicators.
```
