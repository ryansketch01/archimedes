---
campaign_id: montana-empire
type: phishing-kit
aliases: [Montana Empire, PTTAVM phishing kit, AI-built postal e-commerce phishing kit]
status: active
first_observed: 2026-03-31 (attacker domain registration + kit deployment; hallucination detected 2026-03-08)
last_observed: 2026-06-30 (Unit 42 disclosure)
attributed_actors: []              # Hard Rule 2 — Unit 42 attributes to no named actor
attribution_caveats: |
  No actor attribution. Unit 42 does not name a threat actor or group.
  Operator-context signals (Turkish-language admin panel string, PTT AVM
  impersonation) suggest a Türkiye-nexus / Turkish-speaking operator but this
  is NOT a source-stated attribution — recorded as context only, not a claim.
delivery_technique: phantom-squatting   # this kit was staged on an AI-hallucinated domain
sectors_targeted: [postal / e-commerce marketplace customers — consumer credential + payment theft]
geographies: [Türkiye (PTT AVM impersonation per VirusTotal filename metadata)]
impersonated_brand: "PTT AVM (pttavm.com) — Türkiye national postal service e-commerce marketplace (per VT filename PTTAVM.zip; Unit 42 redacts as 'a national postal service')"
named_victims: []                  # brand is impersonated, not breached
ad_relevance: none-direct-illustrative
ad_relevance_rationale: |
  No A&D nexus. Consumer postal/e-commerce credential-and-card theft. Tracked
  by Archimedes solely as the documented in-the-wild instance of the
  phantom-squatting tactic and as an example of an AI-coding-assistant-built
  phishing kit — both of which ARE A&D-relevant as technique classes.
capabilities:
  - real-time storefront scraper (site parity with legitimate marketplace)
  - dual-channel payment interception (credit card + bank transfer)
  - IBAN rotation via Telegram bot command
  - national ID document harvesting alongside payment data
  - manual OTP relay via operator control panel (real-time victim adjudication)
  - PHP backend
  - Telegram-based C2 / exfiltration
build_method: "AI coding assistant — project directory structure + session logs inside the kit ZIP show the assistant was used to build the scraper, PHP backend, and Telegram C2"
source_grade: A2                   # Unit 42 primary + first-party VT artifact confirmation
wep_ceiling: likely                # single-primary-source narrative; artifacts VT-corroborated
related_briefs: []
related_campaigns: [phantom-squatting]
related_actors_referenced: []
related_vulnerabilities: []
related_iocs: threats/iocs/unattributed/montana-empire-phantom-squatting-pttavm-phishing-kit-2026-06-30.yaml
tracked_since: 2026-07-17
last_reviewed: 2026-07-17
next_review_due: 2026-10-17
dossier_version: 1
tlp: CLEAR
---

# Campaign — Montana Empire (AI-built phishing kit on a phantom-squatted domain)

## Status

**Active.** Disclosed by **Unit 42 (Palo Alto Networks)** on **2026-06-30** as the flagship in-the-wild case of [phantom squatting](../phantom-squatting/profile.md). First Archimedes-corpus surface 2026-07-17 on operator tasking.

## What it is

**Montana Empire** is a full-featured phishing kit that an operator **built using an AI coding assistant** and deployed on a domain that LLMs had **hallucinated** for a national postal e-commerce marketplace. It is simultaneously two notable things: an instance of phantom squatting (delivery infrastructure) and an instance of AI-assisted offensive tooling (the kit itself).

## Timeline (Unit 42)

| Date | Event |
|---|---|
| 2026-03-08 | Unit 42 pipeline detects 13 hallucinated URLs for the postal-marketplace domain across both LLM families and all temperature settings — including precise (T=0.1). |
| 2026-03-31 | Attacker registers the exact hallucinated domain and stands up the kit. |
| — | **Adversarial Exploitation Window (AEW): 23 days** of defender lead time went unused. |
| 2026-06-30 | Unit 42 public disclosure. |

## Target / impersonated brand

Unit 42 redacts the brand as "a national postal service's e-commerce marketplace." **First-party VirusTotal filename metadata identifies it: the kit ZIP is `PTTAVM.zip`** — PTT AVM (pttavm.com), Türkiye's national postal service (PTT) e-commerce marketplace. The admin panel's Turkish-language string **"Kimseye Güvenme"** ("Trust No One") corroborates a Turkish-language operator. Victims are PTT AVM *customers*; PTT AVM itself was impersonated, not breached.

A **related, separately-tracked APK campaign** in the same Unit 42 dataset impersonates **Australia Post** (VT filename `auspost.apk`, AEW 51 days) — a distinct artifact, not part of the Montana Empire kit, but captured in the IOC file as it shares the phantom-squatting tactic.

## Capabilities (Unit 42)

- **Real-time scraper** mirrors the legitimate storefront so the phishing page stays in parity with the real site.
- **Dual-channel payment interception** — credit cards *and* bank transfers; **IBAN rotation** driven by Telegram bot commands.
- **National ID document harvesting** alongside payment credentials.
- **Manual OTP relay** — an operator control panel lets the human approve victims' one-time passcodes by hand in real time (defeats OTP on the fly).
- **PHP backend**, **Telegram-based C2** for real-time exfiltration and control.

## AI-assisted build (the second notable finding)

The kit ZIP contained a **project directory structure and session logs from an AI coding assistant**, showing the assistant was used to build the storefront scraper, the PHP backend, and the Telegram C2 interface. This closes a feedback loop: accessible AI tooling both **predicts the phantom domain** and **builds the kit** that lands on it. This is the A&D-relevant part — the technique class, not the postal target.

## A&D relevance

**None direct.** Consumer postal/e-commerce fraud, Türkiye-focused, no A&D or DIB nexus. Tracked only as (1) the documented in-the-wild proof of phantom squatting and (2) a concrete case of AI-coding-assistant-built offensive tooling — both technique classes that matter for A&D-prime defense.

## Grading

**A2, WEP capped at "likely."** Unit 42 primary research; secondary outlets are relays, not independent corroboration. **First-party VirusTotal confirms both artifacts:** the `PTTAVM.zip` kit (1/61 detections — novel/low-signature, consistent with a fresh custom kit) and the `auspost.apk` (18/62 detections — well-flagged). Artifact existence is first-party corroborated; the campaign narrative rests on the single Unit 42 primary. No actor attribution originated.

## Source citations

- Unit 42, "Phantom Squatting…," 2026-06-30 — https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/ (primary)
- Unit 42 Intel (@Unit42_Intel) X post announcing the Montana Empire kit
- Cyberpress relay — https://cyberpress.org/ai-hallucinated-domain-theft/
- VirusTotal (first-party enrichment) — ZIP `eb07edaa…b0bcd`, APK `2202a30d…e34b`

## Related Archimedes records

- **Parent tactic:** [Phantom Squatting](../phantom-squatting/profile.md)
- **IOCs:** [montana-empire-phantom-squatting cluster](../../iocs/unattributed/montana-empire-phantom-squatting-pttavm-phishing-kit-2026-06-30.yaml)

## Operator notes

Migrate to actor-attributed only if a cited A/B-grade source names an operator/group. The Turkish-language admin string and PTT AVM targeting are **operator context, not attribution** — do not promote to a claim. Re-grade or FLASH trigger if the same kit or a variant is later observed impersonating a DIB/A&D brand, or if first-party Splunk surfaces either hash.
