---
raw_id: raw-2026-06-18-am-002-mstic-crypto-clipper-tor-worm-windows
collected_at: 2026-06-18T07:35:00-04:00
run_id: pre-brief-20260618-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: Microsoft Threat Intelligence (MSTIC) / Microsoft Defender Experts
  source_url: https://www.microsoft.com/en-us/security/blog/2026/06/17/crypto-clipper-uses-tor-worm-like-propagation-for-persistence-control/
  published_at: 2026-06-17T19:11:43-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [crypto_clipper, Tor, worm, USB, ".lnk", Windows, WScript, ActiveX, CryptoBandits, clipboard]
triage_tags: [commodity_cybercrime, financial, not_ad_priority, no_named_actor, mstic_primary, monitoring_watch_only]
iocs_extracted: false
iocs_count: 0
text_word_count: 480
promoted: false
rejected_at: 2026-06-18T08:18:00-04:00
rejection_id: reject-2026-06-18-0001
ttl_expires_at: 2026-09-16T07:35:00-04:00
---

# Crypto Clipper uses Tor and worm-like propagation for persistence and control

**Publisher:** Microsoft Threat Intelligence / Microsoft Defender Experts
**Published:** 2026-06-17T19:11 EDT
**URL:** https://www.microsoft.com/en-us/security/blog/2026/06/17/crypto-clipper-uses-tor-worm-like-propagation-for-persistence-control/

## Article body (Microsoft primary)

Microsoft Threat Intelligence and Microsoft Defender Experts identified a Windows-based cryptocurrency clipper that has affected users since February 2026. The clipper relies on Windows Script Host and ActiveX-driven logic to launch a bundled Tor proxy and poll a hidden-service C2 server, performing high-frequency clipboard theft, screenshot exfiltration, and wallet-address substitution. Microsoft Defender Antivirus detects it as `Trojan:Win32/CryptoBandits.A`.

The malware combines two components: a worm functionality that propagates via USB-borne `.lnk` shortcut files (scanning USB devices for .doc / .xlsx / .pdf files, hiding the original files, and creating `.lnk` shortcuts crafted to link to the worm payload), and a clipper/stealer component that harvests cryptocurrency wallet data through clipboard monitoring and wallet-address substitution. It deploys a renamed Tor binary `ugate.exe` in a hidden window, generates a victim GUID, registers the infected device with a hidden-service C2, polls roughly every 500 milliseconds, and supports an EVAL response that allows attacker-supplied code to execute at runtime.

Microsoft frames defender hunting priorities as behavioral: script interpreters spawning suspicious child processes, localhost:9050 proxy usage, screen-capture commands in PowerShell, signs of clipboard inspection or crypto-address replacement.

NO specific tracked-actor attribution by Microsoft. Notes the EVAL response capability "turns a financially motivated stealer into a lightweight backdoor."

---

## Extraction notes

- Language: en
- Publisher byline: Microsoft Defender Security Research Team and Microsoft Defender Experts
- Article type: vendor IR research blog (primary)
- A&D-relevance: low. Consumer cryptocurrency-theft pattern with USB-borne propagation. NOT a fresh CVE, NOT a tracked actor, NOT an A&D-prime targeting pattern. Possible morning-brief Other Signal one-liner watch-pattern (Tor-proxy-hidden-service C2 + USB-borne worm) but not finding scaffold material at this surface.
- IOC extraction invoked: no. Microsoft's article describes generic patterns (ugate.exe filename, localhost:9050 SOCKS5 proxy, JavaScript .lnk payloads) but does not enumerate concrete C2 onions / hashes / URLs in retrievable form within the visible body. Could be extracted on a deeper read of the full Defender Advanced Hunting section but not load-bearing for grader handoff.
- Anti-attribution discipline: Microsoft uses "actors" language only without cross-walk to any roster-tracked actor. Hard Rule 2 BINDING.
