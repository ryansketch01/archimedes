---
raw_id: raw-2026-05-28-pm-002
collected_at: 2026-05-28T15:50:00-04:00
run_id: pre-brief-20260528-pm
collection_mode: pre_brief_collection
source:
  source_yaml_id: mstic
  source_name: Microsoft Threat Intelligence (MSTIC)
  source_url: https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/
  source_grade: A
  authored_by: Microsoft Threat Intelligence
  published_at: 2026-05-28T15:00:00Z   # 11:00 EDT
match_reason:
  watchlist:
    - aerospace-defense (transportation sector named — DIB tier-2/3 logistics adjacency)
  actors: []   # Storm-2697 / The Gentlemen NOT in _roster.yaml
  vulnerabilities: []
  keywords:
    - The Gentlemen ransomware
    - Storm-2697
    - Go-based ransomware
    - Garble obfuscation
    - Curve25519 ECDH key exchange
    - XChaCha20 stream cipher
    - per-file ephemeral keys
    - 21-vector lateral movement
    - PsExec / WMIC / WMI / WinRM / scheduled tasks / services
    - BreachForums RaaS affiliate partnership
    - transportation sector
    - education sector
    - healthcare sector
    - financial sector
    - North America / South America / Europe / Africa / Asia
    - Microsoft Defender / Ransom:Win64/Gentlemen
triage_tags:
  - non_flash
  - new_to_corpus_actor_candidate
  - ransomware_raas_analysis
  - transportation_sector_named
  - tier1_vendor_research_a_grade
  - lateral_movement_aggressive
  - double_extortion
  - go_language_garble_obfuscated
iocs_extracted: true
iocs_count: 3
text_word_count: 2200
promoted: true
promoted_to_finding: finding-2026-05-28-0006-mstic-the-gentlemen-ransomware-storm-2697-go-encryptor-raas-breachforums-transportation
promoted_at: 2026-05-28T16:11:00-04:00
promoted_run_id: afternoon-20260528-160000
ttl_expires_at: 2026-08-26T15:50:00-04:00
---

# MSTIC — The Gentlemen Ransomware (Storm-2697): Self-Propagating Go Encryptor — 2026-05-28

## Source article header

**Title:** "The Gentlemen ransomware: Dissecting a self-propagating Go encryptor"

**Published:** 2026-05-28T15:00:00Z (11:00 EDT)

**Authored by:** Microsoft Threat Intelligence

**URL:** https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/

**Tags:** Elevation of privilege, Extortion, Human-operated ransomware, Lateral movement, Ransomware, Ransomware as a service, Storm, Windows

---

## Actor framing (MSTIC verbatim where possible)

- **MSTIC actor name:** Storm-2697 (financially motivated; manages "The Gentlemen" RaaS platform)
- **Aliases:** none publicly named by MSTIC in this analysis
- **Operational role:** Storm-2697 operates the platform; affiliates carry out attacks
- **Type:** Cybercriminal / RaaS
- **Attribution language (verbatim phrasing assembled from MSTIC blog):** "financially motivated threat actor that manages the RaaS platform known as 'The Gentlemen'"
- **MSTIC confidence level:** procedural / observational (MSTIC tracks Storm-2697 from first-party Defender telemetry; no confidence-level explicit framing in retrievable summary)

---

## Origin and operational evolution

- **Initial emergence:** mid-2025 as a closed ransomware group
- **RaaS pivot:** September 2025 — operators began offering as RaaS to affiliates
- **BreachForums partnership:** recently established as official partnership to recruit affiliates including penetration testers and initial access brokers
- **MSTIC warning:** "this partnership may lead to increased activity as the program becomes accessible to a broader pool of threat actors"

---

## Targeted sectors and geographies (MSTIC verbatim)

- **Sectors:** education, **transportation**, healthcare, financial industries
- **Geographies:** North America, South America, Europe, Africa, Asia

**A&D-direct relevance:** transportation sector named — DIB-tier-2/3 logistics adjacency. Education sector named — university-research / DOE-FFRDC / DoD-collaborative-research adjacency. No primes named.

---

## Technical characteristics (MSTIC verbatim where structured)

### Language and obfuscation
- Written in Go
- Obfuscated with Garble
- Targets Windows environment

### Encryption design
- **Key exchange:** per-file ephemeral Curve25519 ECDH keys
- **Cipher:** XChaCha20 stream cipher
- **Partial-encryption modes:**
  - `--ultrafast` — 0.3% per chunk (~0.9% total for large files)
  - `--superfast` — 1% per chunk (~3% total for large files)
  - `--fast` — 3% per chunk (~9% total for large files)
  - Default — full encryption

### Command-line arguments (operator-controlled)

| Argument | Description |
|---|---|
| `--password <password>` | Required access password (build-specific) |
| `--path <list of paths>` | Comma-separated list of target directories or file paths |
| `--T <minutes>` | Delay in minutes before file encryption begins |
| `--silent` | Silent mode — disables file renaming, timestamp changes, wallpaper change |
| `--system` | Encrypt files as SYSTEM, targeting only local drives |
| `--shares` | Encrypt only mapped network drives and available UNC shares |
| `--full` | Two-phase encryption — relaunches itself as two processes, one with `--system` for local drives and one with `--shares` for network shares |
| `--spread <domain/user:password>` | Enable self-propagation; accepts credentials for lateral movement; if no credential provided, current session token is used |
| `--ultrafast` / `--superfast` / `--fast` | Partial-encryption speed flags (see above) |
| `--keep` | Disable self-delete after file encryption completes |
| `--wipe` | Wipe free disk space after encryption |

### Defense evasion and host preparation
- Disables Microsoft Defender
- Removes shadow copies
- Removes event logs
- Terminates 60+ processes (databases, backup software, EDR agents, Office apps)
- Enables network discovery services and UPnP
- Enables dual persistence (scheduled tasks + registry Run keys)

### Lateral movement — 21 remote operations per target

The malware executes 21 remote operations per target spanning:
- PsExec exploitation
- WMIC process creation
- Scheduled tasks (user context and SYSTEM context)
- Windows services
- PowerShell remoting (WinRM)
- Direct WMI invocation

Deployment attempts from both infected host SMB share AND target's `C:\Temp` directory.

### Double extortion
Data exfiltration paired with encryption; threats of public release for non-payment.

---

## IOCs (per MSTIC publication)

```yaml
iocs:
  sha256_hashes:
    - hash: 22b38dad7da097ea03aa28d0614164cd25fafeb1383dbc15047e34c8050f6f67
      role: The Gentlemen encryptor binary
      first_seen: per MSTIC publication
    - hash: 078163d5c16f64caa5a14784323fd51451b8c831c73396b967b4e35e6879937b
      role: PsExec binary (operationalized for lateral movement)
      first_seen: per MSTIC publication
    - hash: fe1033335a045c696c900d435119d210361966e2fb5cd1ba3382608cfa2c8e68
      role: Wallpaper BMP (post-encryption desktop wallpaper change)
      first_seen: per MSTIC publication
  ip_addresses: []   # not in retrievable summary
  domains: []        # not in retrievable summary
  cves: []
  microsoft_defender_signature: "Ransom:Win64/Gentlemen"
  edr_alerts:
    - "Ransomware-linked threat actor detected"
    - "File backups were deleted"
    - "Ransomware behavior in file system"
attribution_claims:
  - claim: "Storm-2697 manages 'The Gentlemen' RaaS platform; affiliates carry out attacks"
    claimed_by: Microsoft Threat Intelligence (MSTIC)
    confidence_language: procedural / first-party Defender telemetry-backed
    nation: not attributed
    service: not attributed
    monetization: financially motivated
  - claim: "BreachForums RaaS partnership established to recruit affiliates including penetration testers and initial access brokers"
    claimed_by: MSTIC
    confidence_language: observational
named_entities:
  vendors_named_as_targeted_sectors:
    - education
    - transportation
    - healthcare
    - financial
  malware_families: ["The Gentlemen"]
  ransomware_capabilities:
    - per-file ephemeral Curve25519 + XChaCha20 encryption
    - 21-vector lateral movement
    - double extortion (encryption + exfil)
    - partial-encryption tiers
    - Defender disable / shadow-copy delete / event-log wipe
    - 60+ process termination
collection_notes: |
  MSTIC publication is the originating primary on Storm-2697 / The
  Gentlemen analysis. Sole A-grade vendor source this surface; no
  parallel Mandiant / CrowdStrike / Unit 42 publication observed
  this sweep window. Single-source-veto consideration: MSTIC has
  first-party Defender telemetry which is itself a high-quality
  evidence base (vendor-on-own-product-and-telemetry authority),
  similar to MSTIC's standing across prior tracked-actor surfaces
  (e.g. Storm-* numbering convention is MSTIC-canonical). Grader
  decides WEP cap policy on the new-actor introduction.
```

---

## Detection and mitigation guidance (MSTIC verbatim summary)

### Microsoft Defender detection signature
`Ransom:Win64/Gentlemen`

### EDR alert signatures
- "Ransomware-linked threat actor detected"
- "File backups were deleted"
- "Ransomware behavior in file system"

### Recommended mitigations
- Enable cloud-delivered protection and tamper protection
- Deploy controlled folder access
- Configure EDR in block mode
- Enable attack surface reduction rules — especially:
  - Block PsExec / WMI process creation
  - Ransomware-protection ASR rule
- Implement automatic attack disruption

---

## Extraction notes

- Language: en
- Article type: vendor research blog post (technical analysis with IOCs and detection guidance)
- Article body retrieved via WebFetch successfully (full structured summary captured)
- Source grade: A (per source-grades.yaml — Tier-1 vendor, Defender telemetry-backed, MSTIC named research arm)
- Publication is anchored MSTIC named research with first-party EDR telemetry — A-grade evidentiary standard
- Single-source-on-actor caveat: MSTIC is the sole originating primary on Storm-2697 attribution in this surface

## A&D / DIB relevance — collector framing for grader

- **Transportation sector explicitly named** — DIB tier-2/3 logistics adjacency. Major US transportation infrastructure (airlines, shipping, freight, port operations, maritime, rail) supports DoD logistics flows for DIB tier-1 primes. A successful Storm-2697 affiliate compromise of a major transportation operator could have cascading DIB-flow impact.
- **Education sector named** — university-research, DOE-FFRDC, federally funded research and development centers, DoD-collaborative-research consortia all sit in education sector. Lockheed / Boeing / RTX / Northrop / GD all maintain extensive university-research partnerships.
- **Healthcare sector named** — VA / DoD healthcare systems are adjacent but unlikely to be the primary Storm-2697 affiliate target set.
- **No A&D primes named** in MSTIC publication.
- **RaaS-affiliate growth trajectory** — BreachForums partnership is a recurring signal in the corpus (TeamPCP, Bling Libra, ShinyHunters, CL0P operate similar affiliate-recruitment funnels). The aggressive 21-vector lateral movement design favors fast network-wide impact once initial access lands — which is precisely the threat-model A&D primes need to harden against post-VPN / post-Entra-token-compromise.
- **NEW TO CORPUS:** Storm-2697 / The Gentlemen NOT in _roster.yaml. Candidate for /new-actor scaffold IF the operator determines RaaS-affiliate growth merits roster entry. Collector flags but does NOT initiate /new-actor; Storm-2697 will be raw-signal-named for downstream actor-profiler decision.

## Flash trigger evaluation

- **Trigger 1**: NOT MATCHED. No CVE.
- **Trigger 2**: NOT MATCHED. Storm-2697 / The Gentlemen NOT in _roster.yaml.
- **Trigger 3**: NOT MATCHED. No Splunk first-party query against the three IOC hashes at this collection step (deferred to grader / Splunk-enrichment mode).
- **Trigger 4**: NOT MATCHED. No tracked actor.
- **Trigger 5**: PARTIAL. Active multi-victim campaign across multiple continents; transportation + education + healthcare + financial sectors. A&D-direct prime victims NOT named. Defer to grader.
- **Trigger 6**: NOT MATCHED.

No FLASH escalation initiated by collector. A-grade vendor research candidate for PM-28 16:00 brief inclusion on ransomware-economy trajectory + transportation/education sector A&D adjacency.
