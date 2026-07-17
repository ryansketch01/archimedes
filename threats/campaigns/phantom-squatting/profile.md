---
campaign_id: phantom-squatting
type: technique-ttp                # not an actor-attributed campaign; an emerging tactic class
aliases: [Phantom Squatting, AI-hallucinated-domain squatting, slopsquatting-adjacent (domain variant)]
status: active-emerging
first_observed: 2026-06-30 (Unit 42 public disclosure; underlying data collected Mar–Jun 2026)
last_observed: 2026-06-30
attributed_actors: []              # Hard Rule 2 — Unit 42 makes NO actor attribution; none originated here
attribution_caveats: |
  Unit 42 attributes phantom squatting to no named actor. It is a technique
  class, not a single-actor campaign. Any future actor attribution must come
  from a cited source — Archimedes does not originate it.
mitre_attack:
  - T1583.001                      # Acquire Infrastructure: Domains (registration of hallucinated domains)
  - T1608.001                      # Stage Capabilities: Upload Malware (payloads on phantom domains)
  - T1566                          # Phishing (primary delivery outcome)
sectors_targeted: [cross-sector — any brand an LLM can be prompted about; software supply chain]
geographies: [global — 913 brands sampled across global markets]
named_victims: []                  # brands are impersonated, not breached; Unit 42 redacts them
ad_relevance: structural-supply-chain-and-developer-trust
ad_relevance_rationale: |
  Two A&D-relevant exposure paths, both inferential (Unit 42 does not name
  A&D primes): (1) developers and AI coding assistants at A&D primes may
  integrate LLM-suggested dependency/documentation/API endpoints that resolve
  to attacker-registered phantom domains — a software-supply-chain vector into
  ITAR-regulated dev environments; (2) A&D staff self-provisioning AI tooling
  (shadow IT) may be routed to phantom infrastructure by an assistant they
  treat as authoritative. Monitoring tier — no A&D-prime victim named.
source_grade: A2                   # Unit 42 primary research; single primary source (relays not independent)
wep_ceiling: likely                # single-primary-source veto; VT corroborates artifacts, not narrative
related_briefs: []
related_campaigns: [montana-empire]   # Montana Empire is the documented in-the-wild instance
related_actors_referenced: []
related_vulnerabilities: []
related_iocs: threats/iocs/unattributed/montana-empire-phantom-squatting-pttavm-phishing-kit-2026-06-30.yaml
tracked_since: 2026-07-17
last_reviewed: 2026-07-17
next_review_due: 2026-10-17
dossier_version: 1
tlp: CLEAR
---

# Technique — Phantom Squatting (AI-hallucinated domain registration)

## Status

**Active / emerging.** First Archimedes-corpus surface 2026-07-17 on operator tasking. Disclosed publicly by **Unit 42 (Palo Alto Networks)** on **2026-06-30** (Keerthiraj Nagaraj, Diva-Oriane Marty, Beliz Kaleli, Oleksii Starov). Underlying measurement data collected March–June 2026.

## What it is

Adversaries **register domains that large language models hallucinate** — plausible-looking but nonexistent web portals, API endpoints, or corporate service URLs that an LLM invents when answering a prompt about a brand. Once registered, the attacker controls infrastructure that the LLM will keep recommending to real users as authoritative.

**The distinction from typosquatting is the point:** typosquatting waits for a *human* to mistype a real domain. Phantom squatting waits for a *model* to invent a plausible one and then hand users to it. There is no misspelling and no user error — the AI is the delivery mechanism, and it presents the fictitious domain as fact.

## Attack lifecycle (per Unit 42)

Unit 42 frames a four-phase cycle. Described here at the defensive level of the public report — Archimedes does not operationalize discovery or registration:

1. **Discover** — probe LLM hallucination patterns via systematic prompting to learn which fictitious domains a model repeatedly generates for a target brand.
2. **Act** — pre-register the hallucinated domains (trivial cost/barrier for generic TLDs).
3. **Lure** — the LLM delivers the domain to users inside an authoritative-sounding answer.
4. **Bypass** — zero-reputation, freshly registered domains evade reputation-based URL filtering because there is no history to score against.

## Scale (Unit 42 measurement)

- **2.1M** unique URLs generated across **685,339** prompts spanning **913** global brands.
- **13,229** confirmed-malicious URLs (0.61%) already flagged by threat intel.
- **41,313** high-risk URLs (1.90%) assessed as nascent/opportunistic.
- **~250,000** hallucinated domains still **unregistered** — standing pre-registration opportunity for adversaries.
- **809,455** URLs (37.28%) resolve to non-existent domains (NXD).
- Confirmed-malicious breakdown: malware 67.2%, phishing 16.2%, grayware 13.7%, C2 3.0%.

**Precision-mode caveat (highest-value subset):** domains that a model generates *even at low temperature* (T=0.1, "precise") are the highest-value targets — the model is most likely to surface them to real users as fact. Hallucination is not just a high-creativity artifact.

## Why it matters for the target profile

Unit 42 frames LLMs as **trusted dependencies in the software supply chain**: AI coding assistants generate documentation/API/service links that developers paste into production code and CI/CD; autonomous agents fetch model-generated URLs without independent verification. For an ITAR-regulated A&D prime, the exposure is a phantom domain reaching a **developer or build pipeline** through an assistant treated as authoritative — before reputation-based defenses have anything to score.

Structural advantage for the attacker (Unit 42, paraphrased): by the time threat-intel systems catch up, users have already been funneled to the site by an AI system they trust.

## Defensive framing

Unit 42's mitigation concept is the **Adversarial Exploitation Window (AEW)** — the interval between first hallucination detection and attacker registration. A *positive* AEW is defender lead time: if you can enumerate the domains your brand's name causes models to hallucinate, you can pre-register or block them before an adversary does. Documented AEWs in the Montana Empire dataset ran 23–51 days (one historical case at −11 months, i.e. attacker beat detection).

Practical detection posture for a prime (Archimedes framing, not source-stated):
- Treat freshly registered, zero-reputation domains referenced in AI-assistant output or dev tooling as **untrusted until verified**.
- Monitor for internal resolution of newly registered domains that lexically resemble the prime's own brand/service namespace.
- Verify LLM-suggested dependency URLs, package registries, and API endpoints against a known-good allowlist before they enter code or CI/CD.

## Grading

**A2, WEP capped at "likely."** Unit 42 is an A-grade primary research source. The many secondary outlets (The Hacker News, SC Media, Dark Reading, Cybernews, GBHackers, Check Point Research, CSA) are **relays of the same primary report — not independent corroboration** (per standing single-source discipline). First-party VirusTotal enrichment independently confirms the *artifacts* in the Montana Empire instance (see IOC file), which corroborates the in-the-wild claim but not the broader measurement narrative. WEP held at "likely" under single-primary-source veto.

## Source citations

- Unit 42, "Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector," 2026-06-30 — https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/ (primary)
- The Hacker News, 2026-07 (relay) — https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html
- SC Media, Dark Reading, Cybernews, GBHackers, Check Point Research 6-July threat-intel report (relays)

## Related Archimedes records

- **In-the-wild instance:** [Montana Empire phishing kit](../montana-empire/profile.md) — the documented deployment of this tactic (PTT AVM impersonation).
- **IOCs:** [montana-empire-phantom-squatting cluster](../../iocs/unattributed/montana-empire-phantom-squatting-pttavm-phishing-kit-2026-06-30.yaml)

## Operator notes

Re-grade-up / brief triggers: (1) a second A/B-grade vendor publishes *independent* phantom-squatting research (not a Unit 42 relay); (2) first-party Splunk observation of an A&D-prime host resolving an AI-suggested phantom domain; (3) any named A&D-prime or DIB victim, which would lift `ad_relevance` from monitoring to active and warrant a FLASH evaluation. This is the third LLM-platform-abuse surface class in the corpus (cf. LLMShare, ChatGPhish) — candidate for an "AI Platform Security" standing brief section if the cluster grows.
