---
actor_id: "022"
actor_name: MuddyWater
last_updated: 2026-05-06
admiralty_grade: A2
tlp: CLEAR
source_of_record: true
sidecar: iocs.yaml
attribution_caveat: |
  All 19 indicators below are sourced from Rapid7's 2026-05-06 incident-response
  report (finding-2026-05-06-FLASH-0002) at "moderate confidence" attribution to
  MuddyWater. Single-source veto applied; SecurityWeek and BleepingComputer are
  relays. Two confidence constraints stack: vendor-self-rated moderate +
  single-source veto. 72-hour auto-downgrade clock registered (~2026-05-09 12:00
  EDT). Indicators are NOT promoted as MuddyWater-canonical until a second
  A/B-grade vendor independently corroborates.
---

# MuddyWater — Indicators of Compromise

> **First-pass scaffold (2026-05-06). 19 indicators ingested from Rapid7 2026-05-06.**
>
> **CAVEAT:** Each indicator below is carried as "Rapid7 attributes ... at moderate
> confidence." None are promoted as MuddyWater-canonical. If by ~2026-05-09 12:00
> EDT no second A/B-grade vendor (Mandiant, Unit 42, MSTIC, CrowdStrike, Recorded
> Future, Volexity) corroborates, no first-party Splunk hit lands, and no
> CISA / FBI advisory picks up, finding-2026-05-06-FLASH-0002 auto-downgrades to
> C3 "possibly true" per RETRACTION-POLICY — and the indicators here move with it.
>
> **Mechanism-level vs actor-specific framing:** The Microsoft Teams interactive
> screen-share + "IT Support" persona, MFA device-add manipulation, and Quick
> Assist phishing tradecraft are platform-generic. Defenders should hunt these
> mechanism-level surfaces regardless of which actor is currently using them.
> The actor-specific surfaces (custom RAT hash, code-signing thumbprint, specific
> domains/IPs) are the moderate-confidence MuddyWater claim; mechanism-level
> surfaces are independently defensible.

---

## CVEs Actively Exploited

*No CVEs documented as actively exploited by MuddyWater in the 2026-05-06 Rapid7
report. The 2026 intrusion relies on Microsoft Teams social engineering, Quick
Assist phishing, and operator-on-keyboard tradecraft, NOT CVE exploitation.
Historical MuddyWater reporting (2020-2022) documents exploitation of
ZeroLogon (CVE-2020-1472), ProxyLogon, and ProxyShell during their respective
exploitation windows.*

---

## Malicious Delivery Domains

| Domain | Role | First Seen | Source |
|---|---|---|---|
| `adm-pulse[.]com` | Quick Assist phishing infrastructure | 2026 (per Rapid7 campaign window) | Rapid7 2026-05-06 (moderate confidence) |

---

## C2 Domains

| Domain | Role | Related Malware | First Seen | Source |
|---|---|---|---|---|
| `moonzonet[.]com` | C2 | ms_upd.exe loader | 2026 | Rapid7 2026-05-06 (moderate confidence) |
| `uploadfiler[.]com` | C2 (port 443) | Game.exe / Darkcomp custom 12-command RAT | 2026 | Rapid7 2026-05-06 (moderate confidence) |

---

## IP Addresses

| IPv4 | Role | Notes | Source |
|---|---|---|---|
| `77.110.107.235` | Source IP | Microsoft Teams social engineering source | Rapid7 2026-05-06 (moderate confidence) |
| `93.123.39.127` | Source IP | Microsoft Teams social engineering source | Rapid7 2026-05-06 (moderate confidence) |
| `172.86.126.208` | Hosting | ms_upd.exe hosting | Rapid7 2026-05-06 (moderate confidence) |
| `116.203.208.186` | Contact | pythonw.exe outbound contact | Rapid7 2026-05-06 (moderate confidence) |

---

## Onion Addresses

| Onion | Role | Source |
|---|---|---|
| `hptqq2o2qjva7lcaaq67w36jihzivkaitkexorauw7b2yul2z6zozpqd[.]onion` | Chaos DLS facade — extortion theater (no actual victim leak per Rapid7) | Rapid7 2026-05-06 (moderate confidence) |

---

## File Hashes

### Custom tooling (Rapid7 2026, attribution-caveated)

| Hash | Filename | Role | Notes | Source |
|---|---|---|---|---|
| `1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6` | Game.exe | Custom RAT | 12-command backdoor (Darkcomp); masquerades as Microsoft WebView2 | Rapid7 2026-05-06 |
| `24857fe82f454719cd18bcbe19b0cfa5387bee1022008b7f5f3a8be9f05e4d14` | ms_upd.exe | Loader | C2 to moonzonet[.]com | Rapid7 2026-05-06 |
| `c86ab27100f2a2939ac0d4a8af511f0a1a8116ba856100aae03bc2ad6cb0f1e0` | visualwincomp.txt | Payload / config | Rapid7 reporting | Rapid7 2026-05-06 |
| `a47cd0dc12f0152d8f05b79e5c86bac9231f621db7b0e90a32f87b98b4e82f3a` | WebView2Loader.dll | DLL sideload | Rapid7 reporting | Rapid7 2026-05-06 |

### Legitimate binaries repurposed / abused

| Hash | Filename | Role | Source |
|---|---|---|---|
| `3df9dcc45d2a3b1f639e40d47eceeafb229f6d9e7f0adcd8f1731af1563ffb90` | WebView2.exe | Legitimate binary repurposed | Rapid7 2026-05-06 |
| `cd098eddb23f2d2f6c42271ca82803b0d5ac950cb82a9b8ae0928e83945a53df` | dwagent.exe | DWAgent — abused for persistence | Rapid7 2026-05-06 |
| `a3bac548b5bc91c526b4d6707623ddbd1a675aa952f0d1f9a0aa6f7230f09f23` | dwagsvc.exe | DWAgent service | Rapid7 2026-05-06 |
| `86e0197389f0573eb83ff53991f337d416124c7c8bd727721ef3d396cd5f65d` | dwaglnc.exe | DWAgent component | Rapid7 2026-05-06 |
| `bfc1675ee1e358db8356f515aaded7962923e426aa0a0a1c0eddfc4dab053f89` | AnyDesk.exe | AnyDesk — abused for remote access | Rapid7 2026-05-06 |

> The DWAgent / AnyDesk / WebView2 hashes are the SPECIFIC binaries observed in the Rapid7 incident. They are useful for retroactive hunt against historical EDR / file-event telemetry, but the legitimate binaries themselves are not malicious — defenders should hunt for the specific hashes paired with anomalous parent-process / network behavior, not block by hash.

---

## Code-Signing Certificate Indicators

| Subject | Issuer | Thumbprint | Status | Notes | Source |
|---|---|---|---|---|---|
| Donald Gay | Microsoft ID Verified CS AOC CA 02 | `B674578D4BDB24CD58BF2DC884EAA658B7AA250C` | Time-invalid (revoked shortly after deployment) | "Donald Gay" lineage; long-running MuddyWater code-signing pattern alongside "Amy Cherne" | Rapid7 2026-05-06 |

The Donald Gay / Amy Cherne code-signing lineage is a long-running pattern across multiple MuddyWater reporting cycles. The signing identities are typically time-invalid or revoked shortly post-deployment.

---

## Behavioral / TTP Indicators

### Microsoft Teams interactive screen-share with "IT Support" persona

**MITRE ATT&CK:** T1056 (Input Capture) + T1566.003 (Spearphishing via Service)

| Indicator | Description | Source |
|---|---|---|
| Microsoft Teams interactive screen-share for live credential harvest | Operator engages target via Teams meeting under "IT Support" persona; uses interactive screen-share for live credential capture during apparent troubleshooting session. | Rapid7 2026-05-06 + multiple historical MuddyWater sources |

**Detection scope:** PLATFORM-GENERIC — apparent across multiple actors in 2025-2026 reporting (Scattered Spider, Storm-1811, generic IAB tradecraft). Hunt for Teams external-account-initiated meetings paired with screen-share to internal users from non-allowlisted external tenants, regardless of attribution.

### MFA device-add manipulation

**MITRE ATT&CK:** T1556.006 (Modify Authentication Process: Multi-Factor Authentication)

| Indicator | Description | Source |
|---|---|---|
| Attacker-controlled device added to victim MFA registration | Operator harvests credentials, then adds attacker-controlled device to the victim's MFA configuration to maintain persistence; surfaces in Entra ID audit logs as `Add registered device` / `Update authentication method` events. | Rapid7 2026-05-06 |

**Detection scope:** PLATFORM-GENERIC. Hunt mechanism-level regardless of attribution.

### pythonw.exe code injection into suspended processes

**MITRE ATT&CK:** T1055 (Process Injection)

| Indicator | Description | Source |
|---|---|---|
| pythonw.exe creates suspended child processes and writes memory | Long-running MuddyWater pattern continued in 2026 reporting. Hunt: pythonw.exe (or other Python interpreters) creating suspended processes, particularly with memory write operations to the suspended target. | Rapid7 2026-05-06 + multiple historical MuddyWater sources |

### Chaos ransomware deployed without actual file encryption (false-flag indicator)

| Indicator | Description | Source |
|---|---|---|
| Chaos ransomware artifacts (ransom note, fake DLS facade) deployed without actual encryption | Operationally striking pattern: state-tradecraft objectives (custom RAT, credential harvest, MFA manipulation, persistence) wrapped in commodity-ransomware extortion theater. Espionage-shaped reading is partially independent of the MuddyWater actor attribution per red-team contrarian ACH. | Rapid7 2026-05-06 |

**Triage discipline:** if a Chaos-branded ransom note appears in environment without corresponding actual file encryption, treat as **espionage-with-cover** until proven otherwise. The "no encryption" outcome is not by itself diagnostic — it can be implementation failure or EDR-blocked encryption by a genuine criminal Chaos affiliate — but the combination with other state-tradecraft surfaces (custom RAT investment, persistence, credential harvest, MFA manipulation) supports the espionage reading.

---

## Registry Indicators

*No actor-specific registry artifacts catalogued in this first-pass scaffold. MuddyWater persistence via T1547.001 (Run keys) is documented at TTP level in `profile.md`; specific run-key names rotate per campaign and are not surfaced in the Rapid7 2026-05-06 IOC set.*

---

## Scheduled Task Indicators

*No specific scheduled-task names catalogued in this first-pass scaffold. T1053.005 referenced at TTP level.*

---

## Cloud C2 / Remote Access Tool Abuse

| Pattern | Description | Source |
|---|---|---|
| DWAgent abuse for persistence and remote access | DWAgent legitimate remote-access tool repurposed for operator persistence | Rapid7 2026-05-06 + multiple historical sources |
| AnyDesk abuse for remote access | AnyDesk legitimate remote-access tool used for operator access | Rapid7 2026-05-06 |
| Microsoft Quick Assist phishing initiation | Quick Assist sessions initiated from external accounts under "IT Support" pretext | Rapid7 2026-05-06 |

---

## Detection Queries (Hunt Guidance)

### 1. Outbound DNS to MuddyWater 2026 domains

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=dns
| eval domain=lower(query)
| where domain IN (
    "moonzonet.com",
    "uploadfiler.com",
    "adm-pulse.com"
  )
| stats count earliest(_time) latest(_time) by src, domain
| sort - count
```

False-positive consideration: very low for these specific domains. Hits are operationally significant.

### 2. Outbound to MuddyWater 2026 IPv4

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=stream:tcp OR sourcetype=zeek_conn
| where dest_ip IN ("77.110.107.235", "93.123.39.127", "172.86.126.208", "116.203.208.186")
   OR src_ip IN ("77.110.107.235", "93.123.39.127", "172.86.126.208", "116.203.208.186")
| stats count earliest(_time) latest(_time) by src_ip, dest_ip, dest_port
| sort - count
```

False-positive consideration: very low. Hits are operationally significant.

### 3. Microsoft Teams external-account screen-share hunt (mechanism-level)

**KQL (Microsoft 365):**

```kql
// Hunt for Teams meetings with screen-share initiated by external accounts
TeamsMeetings
| where TimeGenerated > ago(90d)
| where IsExternalParticipantPresent == true
| where ScreenShareDuration > 0
| where ExternalParticipantTenant !in (allowlisted_partner_tenants)
| project TimeGenerated, OrganizerUser, ExternalParticipantUser, ExternalParticipantTenant, ScreenShareDuration
| order by TimeGenerated desc
```

False-positive consideration: legitimate external-partner Teams collaborations. Tune by maintaining an allowlist of partner tenants.

This hunt is **mechanism-level** — relevant regardless of whether MuddyWater is the actor currently using the tradecraft.

### 4. MFA device-add events (mechanism-level)

**KQL:**

```kql
AuditLogs
| where TimeGenerated > ago(90d)
| where OperationName in ("Add registered device", "Update authentication method", "User registered security info")
| where InitiatedByActor != "Self-service password reset"
| project TimeGenerated, OperationName, InitiatedBy, TargetResources, Result
| order by TimeGenerated desc
```

False-positive consideration: legitimate device adds during normal user lifecycle. Pair with sign-in anomaly correlation and recent password-reset signal.

### 5. pythonw.exe suspended-process hunt

**EDR pseudo-logic:**

```
ON ENDPOINTS:
  ALERT IF process_name = "pythonw.exe" creates_child_process_with(creation_flag = CREATE_SUSPENDED)
  AND child_process_memory_write_count > 0
```

False-positive consideration: legitimate developer tooling can match. Tune for production endpoints (non-developer fleet) and pair with parent-process / user-context correlation.

### 6. Code-signing certificate hunt (Donald Gay lineage)

**EDR pseudo-logic:**

```
ON ENDPOINTS:
  ENUMERATE binaries signed by Microsoft ID Verified CS AOC CA 02
  ALERT IF cert.subject_name = "Donald Gay" OR cert.thumbprint = "B674578D4BDB24CD58BF2DC884EAA658B7AA250C"
  ALERT IF cert.valid_window < 30 days AND cert.revoked = true
```

False-positive consideration: legitimate developer-signed binaries with short cert validity; tune by issuing-CA + subject-pattern combination.

### 7. Game.exe / WebView2 masquerade hunt

**EDR pseudo-logic:**

```
ON ENDPOINTS:
  ALERT IF binary_name = "Game.exe"
       OR (binary_loads_module("WebView2Loader.dll")
           AND binary_path NOT IN known_microsoft_paths
           AND binary_outbound_connection_to_non_microsoft_destination = true)
```

False-positive consideration: legitimate WebView2 use in non-standard application paths; tune for outbound connection destination as the high-confidence pivot.

### 8. SHA256 hash sweep (all 9 hashes)

**EDR pseudo-logic:**

```
ON ENDPOINTS:
  SCAN file_hashes (-90d) for the 9 SHA256 hashes published by Rapid7 2026-05-06:
    [9 hashes from File Hashes section above]
  ALERT on match
```

False-positive consideration: legitimate-binary hashes (DWAgent, AnyDesk, WebView2) may match in legitimate use; pair hash match with parent-process / network anomaly correlation rather than treating hash-match alone as malicious.

### 9. Onion address hunt

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=tor_logs OR sourcetype=proxy
| where url_or_query contains "hptqq2o2qjva7lcaaq67w36jihzivkaitkexorauw7b2yul2z6zozpqd"
| stats count earliest(_time) latest(_time) by src_ip
```

False-positive consideration: very low. Hits are operationally significant. This is the Chaos DLS facade onion; presence in environment indicates either active engagement or research / IR review traffic.

---

## Sources

- [Rapid7: MuddyWater operation — Iranian APT intrusion masquerading as Chaos ransomware (2026-05-06)](https://www.rapid7.com/blog/) — A (provisional)
- [SecurityWeek: Iranian APT Intrusion Masquerades as Chaos Ransomware Attack (2026-05-06)](https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/) — B (relay)
- [BleepingComputer: MuddyWater hackers use Chaos ransomware as a decoy (2026-05-06)](https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/) — B (relay)
- [MITRE ATT&CK G0069 — MuddyWater](https://attack.mitre.org/groups/G0069/) — A1
- [Palo Alto Unit 42: MuddyWater research index](https://unit42.paloaltonetworks.com/) — A1
- finding-2026-05-06-FLASH-0002 — Archimedes graded finding (digraph A2, WEP "likely", red-team `qualify` with required briefer caveats and 72h auto-downgrade clock)

---

*First-pass scaffold authored 2026-05-06. All 19 indicators sourced from Rapid7
2026-05-06 disclosure via finding-2026-05-06-FLASH-0002 at moderate confidence.
Hard Rule 2 honored: every indicator and attribution claim traces to a cited
public source. None of these indicators are promoted as MuddyWater-canonical
pending second A/B-grade vendor confirmation. 72-hour auto-downgrade clock
registered (~2026-05-09 12:00 EDT) per RETRACTION-POLICY.*
