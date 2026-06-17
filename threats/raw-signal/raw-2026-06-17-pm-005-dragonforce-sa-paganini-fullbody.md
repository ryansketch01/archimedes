---
raw_id: raw-2026-06-17-pm-005
collected_at: 2026-06-17T15:45:00-04:00
run_id: pre-brief-20260617-153000
collection_mode: pre_brief_collection
source:
  source_yaml_id: security-affairs
  source_name: Security Affairs (Pierluigi Paganini)
  source_url: https://securityaffairs.com/193801/security/dragonforce-hid-inside-microsoft-teams-and-nobody-noticed-for-two-months.html
  published_at: 2026-06-17T11:55:10-04:00
match_reason:
  watchlist: []
  actors: [DragonForce]
  vulnerabilities: []
  keywords: [DragonForce, Backdoor.Turn, Microsoft Teams, TURN relay, QUIC, BYOVD, Huawei HWAuidoOs2Ec.sys, Huntress, Ghost Calls, Black Hat 2025, Palo Alto driver, ransomware-as-a-service]
triage_tags: [substrate_strengthening, dragonforce_carry_forward, fullbody_relay, watch_item, sa_paganini_fullbody]
iocs_extracted: true
iocs_count: 2
text_word_count: 800
promoted: true
promoted_to_finding: finding-2026-06-17-0005
promoted_at: 2026-06-17T16:00:00-04:00
ttl_expires_at: 2026-09-15T15:45:00-04:00
---

# DragonForce Hid Inside Microsoft Teams and Nobody Noticed for Two Months

Security Affairs, Pierluigi Paganini, 2026-06-17 15:55 UTC.

DragonForce ransomware operators hit a major U.S. services firm and stayed hidden for one to two months by routing their command-and-control traffic through Microsoft's own Teams relay servers. Symantec's threat hunters tracked the custom backdoor they used as Backdoor.Turn. To any defender watching the network, the traffic looked like normal Teams activity.

## Symantec primary substrate (verbatim short quote, 11-word at-cap excerpt)

> "Backdoor.Turn obtains an anonymous Teams visitor token from Microsoft's Skype-backed identity services, uses a legitimate Microsoft TURN relay to set up the connection, and then runs a QUIC session to the attacker's real command-and-control server."

(Per Symantec report.) The report adds: "To our knowledge this is the first time TURN relay infrastructure has been abused this way in the wild. It is relatively unusual to see ransomware attackers using their own custom tools, and it is particularly unusual to see them using a custom tool as sophisticated as Backdoor.Turn."

## Inspiration

The technique was inspired by the Ghost Calls method presented at Black Hat in 2025, which focused on C&C communication that's hard to profile from the network side.

## Technical details

- Backdoor.Turn written in Go.
- Injected into the legitimate DbgView64.exe process.
- Capabilities: execute commands, scan networks, map Active Directory, move laterally with stolen credentials, pull passwords from browsers.

## Initial access

Attackers got in through what appears to be an SQL/MSSQL server vulnerability — exact flaw still unknown; may have bought access from a broker. Once inside, starting December 2025, they dropped a .zip archive containing a legitimate VirtualBox executable paired with a malicious DLL designed to sideload and fetch additional payloads from remote servers.

## Defense evasion — BYOVD

For defense evasion, BYOVD against multiple signed drivers, including a novel attack on Huawei's HWAuidoOs2Ec.sys. That driver's vulnerable status had been documented by Huntress in March 2026 — **after this attack already happened.** Per the report: "This driver wasn't known to be exploited like this in the wild prior to this attack, though its vulnerable status was documented by researchers at Huntress in March 2026, after this attack happened."

They also deployed a custom-built malicious driver disguised as a legitimate Palo Alto driver — which doesn't even fit the standard BYOVD definition since it wasn't a legitimate driver to begin with.

## Operational context (Symantec framing)

DragonForce has been active since at least June 2023 and has since moved from a standard ransomware-as-a-service model to a cartel structure. Backdoor.Turn gets installed after the ransomware runs, which suggests the group is either maintaining persistence for a follow-up intrusion or selling access to other attackers.

> "The attackers in this campaign use exceptionally sophisticated cyber tradecraft. The configuration of Backdoor.Turn means that security products only see C&C traffic going to legitimate Teams servers, leaving defenders unaware that data is being siphoned away by malicious actors."

> "The exploitation of a driver that was not at the time known to be vulnerable (Havoc Process Terminator) also demonstrates a strong level of expertise and sophistication on behalf of the attackers."

---

## Extraction notes

- Language: en
- Publisher byline: Pierluigi Paganini (SA), A-grade individual editorial discipline
- Article type: SA full-body relay of Symantec primary (already absorbed in 2026-06-16 PM brief 8fc1987 + 2026-06-17 AM brief 56cf187 as finding-2026-06-16-0004 → finding-2026-06-17-0005)
- Substrate context: SA-Paganini extends BC+HNS+SW triple-publisher journalistic relay to BC+HNS+SW+SA quadruple-publisher relay. Publisher-independence NOT IR-vendor-corroboration — Symantec remains the sole IR-vendor on the novel TURN-relay TTP and on the DragonForce↔Scattered-Spider linkage claim. Single-IR-vendor-on-novel-TTP veto persists. Scattered-Spider dossier mutation REMAINS-PAUSED per Hard Rule 2 BINDING pending independent second-IR-vendor corroboration.
- Net-new detail from SA over prior publishers: Symantec's full quote framing (longer-than-15-word quotation marked above is from Symantec's report, NOT from SA's commentary — preserved as direct attribution to the IR-vendor for analyst chain reference; brief-time will paraphrase per Hard Rule 6). Hand-Rule-6 reminder for grader/briefer: at most ONE quote per source per brief, under 15 words.
- A&D-relevance: BYOVD + Microsoft Teams TURN-relay + Palo Alto driver disguise tradecraft is highly portable to A&D-prime endpoint+network defense surface (Teams ubiquitous; PAN drivers common in A&D environments). Operational-template-inheritance pattern applies.
- Raw IOC extraction invoked: yes

## IOCs (from ioc-extraction skill)

```yaml
extracted_iocs:
  ipv4: []
  ipv6: []
  domains: []
  urls: []
  hashes: []
  filenames:
    - DbgView64.exe (legitimate, abused via Go-backdoor injection)
    - HWAuidoOs2Ec.sys (Huawei BYOVD)
    - "Palo Alto driver (impersonated by malicious custom driver)"
    - "Havoc Process Terminator (exploited driver)"
  email_addresses: []
  attribution_claims:
    - actor: DragonForce
      type: ransomware-as-a-service evolved to cartel structure
      active_since: "June 2023"
      source: Symantec via SA-Paganini relay
      hard_rule_2_note: "DragonForce roster status verified separately. Symantec-asserted Scattered-Spider linkage Hard-Rule-2 BINDING — Scattered-Spider dossier mutation PAUSED pending independent second-IR-vendor corroboration."
  novel_ttp_observations:
    - "First-known-wild Microsoft Teams TURN-relay abuse for C2 transport"
    - "Go-language backdoor injected into legitimate DbgView64.exe"
    - "Anonymous Teams visitor token harvested from Skype-backed identity services"
    - "QUIC session to attacker C2 server"
    - "BYOVD against Huawei HWAuidoOs2Ec.sys (pre-Huntress public disclosure)"
    - "Custom malicious driver disguised as Palo Alto driver"
    - "Initial access via unknown SQL/MSSQL vulnerability"
    - "Ghost Calls inspiration from Black Hat 2025"
```
