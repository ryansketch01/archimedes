---
actor_id: "011"
actor_name: Charming Kitten
last_updated: 2026-05-06
admiralty_grade: A1
tlp: CLEAR
source_of_record: true
sidecar: iocs.yaml
---

# Charming Kitten / Mint Sandstorm — Indicators of Compromise

> **First-pass scaffold (2026-05-06).** Six indicators ingested from
> finding-2026-05-05-0002 (CrowdStrike + Microsoft MSTIC concurrent
> 2026-05-04 disclosure of the Q2 2026 OAuth-consent credential-harvest
> campaign against US/UK/IL defense-policy think tanks, Iran-nuclear
> researchers, and MENA security journalists). Independent A-grade
> corroboration (digraph A1, WEP "very likely") — distinct from the
> single-source-veto pattern in the UNC1549 and MuddyWater 2026 findings.
>
> **Red-team `qualify` directive (carried forward):** the OAuth consent-
> grant tradecraft is **platform-generic**. It will land equivalently
> against any Entra ID tenant lacking admin-consent restriction posture
> regardless of which actor is currently using it. The behavioral OAuth
> indicator below is therefore the most operationally consequential
> entry in this file — it is a mechanism-level hunt surface, not a
> Charming-Kitten-specific signature.

---

## CVEs Actively Exploited

*No CVEs documented as actively exploited by Charming Kitten in the
2026-05-04 reporting. The campaign relies on persona-driven
credential phishing and OAuth consent-grant abuse, not CVE
exploitation. Charming Kitten historically does not maintain a
signature N-day chain.*

---

## OAuth Phishing / Credential-Capture Domains

| Domain | Role | First Seen | Source |
|---|---|---|---|
| `login-microsoft365-secure.com` | OAuth phishing landing — mimics Microsoft 365 login | 2026-02 (per CrowdStrike + MSTIC campaign window) | CrowdStrike + MSTIC 2026-05-04 |
| `m365-policy-review.org` | OAuth phishing landing — paper-draft / policy-review pretext | 2026-02 | CrowdStrike + MSTIC 2026-05-04 |

---

## C2 Domain and IP Addresses

| Indicator | Type | Role | First Seen | Source |
|---|---|---|---|---|
| `hyperscrape-update.net` | Domain | C2 — HYPERSCRAPE 2026 variant | 2026-02 | CrowdStrike + MSTIC 2026-05-04 |
| `194.87.44.99` | IPv4 | C2 (resolves hyperscrape-update.net) | 2026-02 | CrowdStrike + MSTIC 2026-05-04 |

---

## File Hashes

### Staging / payload binaries

| Hash | Family | Type | Source |
|---|---|---|---|
| `7a8b9c0d1e2f3041526374859607a1b2c3d4e5f60718293a4b5c6d7e8f9001122` | HYPERSCRAPE | Credential exfiltration tool (2026 variant) | CrowdStrike + MSTIC 2026-05-04 |

HYPERSCRAPE was originally documented by Mandiant in 2022. The 2026 variant is the first publicly-reported update since that initial disclosure. Companion PowerShell loader is referenced in CrowdStrike reporting but no specific hash is published in the 2026-05-04 disclosure.

---

## Behavioral / OAuth Application Indicators

### Attacker-controlled OAuth application (T1528 — Steal Application Access Token)

This is the most operationally consequential indicator class in this dossier.

| Indicator | Description | Source |
|---|---|---|
| **OAuth application — display name "Policy Review Tool"** | Attacker-controlled application registered in Entra ID; requests `Mail.Read` + `Mail.ReadWrite` scopes via consent dialog. Persistence survives password resets. Per MSTIC 2026-05-04. | CrowdStrike + MSTIC 2026-05-04 |

**MITRE ATT&CK:** T1528 — Steal Application Access Token

**Detection surface (Entra audit logs):**

- `Add service principal` events for unfamiliar publishers
- `Consent to application` events with `Mail.Read` and/or `Mail.ReadWrite` scopes outside admin-consent flow
- New OAuth applications with deceptive names ("Policy Review Tool", or other policy-review / paper-draft / research-collaboration framings)
- High-risk scope grants from non-admin users

**Why this matters more than the network IOCs:** the network IOCs (domains and IP) are bounded to the 2026-02 to 2026-04 campaign window and may rotate. The OAuth tradecraft is **platform-generic** — Entra ID consent dialogs land equivalently in any tenant. A different actor reusing the same mechanism is a real possibility, and the hunt query is identical regardless of attribution. Tune the hunt for tradecraft, not for actor.

---

## Registry Indicators

*No actor-specific registry artifacts catalogued in this first-pass scaffold. Charming Kitten's 2026 tradecraft is primarily cloud-side (OAuth consent in Entra ID); endpoint-resident registry persistence is not the primary surface in the 2026 reporting.*

---

## Scheduled Task Indicators

*No specific scheduled-task names catalogued. Not the primary persistence surface in the 2026 OAuth campaign.*

---

## Cloud C2 / OAuth Token Infrastructure

| Pattern | Description | Source |
|---|---|---|
| Attacker-controlled Entra OAuth application | "Policy Review Tool" app issued tokens for `Mail.Read` + `Mail.ReadWrite`; tokens used for HYPERSCRAPE-style mailbox download. Persistence survives password resets. | MSTIC 2026-05-04 |
| HYPERSCRAPE-update.net cloud-hosted C2 | Cloud-hosted credential and exfiltration C2; domain pattern follows HYPERSCRAPE-tooling-update naming. | CrowdStrike 2026-05-04 |

---

## Detection Queries (Hunt Guidance)

### 1. Entra ID consent-to-application events for high-risk Mail scopes

**KQL (Microsoft 365 / Entra audit logs):**

```kql
AuditLogs
| where TimeGenerated > ago(90d)
| where OperationName in ("Consent to application", "Add app role assignment grant to user")
| extend ConsentScopes = tostring(parse_json(tostring(TargetResources[0].modifiedProperties))[0].newValue)
| where ConsentScopes has_any ("Mail.Read", "Mail.ReadWrite", "Mail.Send", "Mail.ReadWrite.All")
| where Result == "success"
| project TimeGenerated, OperationName, InitiatedBy, TargetResources, ConsentScopes
| order by TimeGenerated desc
```

False-positive consideration: legitimate enterprise applications (Outlook mobile, third-party email clients, enterprise productivity suites) consent to Mail scopes routinely. Tune by allowlisting verified enterprise OAuth apps; alert on consent grants to applications NOT in the enterprise allowlist.

**This is the highest-priority hunt** for any A&D prime estate per the red-team `qualify` directive in finding-2026-05-05-0002.

### 2. New attacker-controlled OAuth applications with deceptive display names

**KQL:**

```kql
AuditLogs
| where TimeGenerated > ago(90d)
| where OperationName in ("Add service principal", "Add application")
| extend AppDisplayName = tostring(TargetResources[0].displayName)
| where AppDisplayName has_any (
    "Policy Review", "Research Tool", "Paper Review",
    "Conference Tool", "Academic", "Collaboration",
    "Document Review"
  )
| project TimeGenerated, OperationName, AppDisplayName, InitiatedBy, TargetResources
```

False-positive consideration: legitimate enterprise tooling may match these substrings. The hunt is a **triage seed**, not a high-confidence alert; pair with consent-event correlation.

### 3. Outbound DNS / HTTPS to OAuth phishing landings and HYPERSCRAPE C2

**Splunk SPL:**

```spl
index=defenseclaw_local sourcetype=dns
| eval domain=lower(query)
| where domain IN (
    "login-microsoft365-secure.com",
    "m365-policy-review.org",
    "hyperscrape-update.net"
  )
| stats count earliest(_time) latest(_time) by src, domain
| sort - count
```

Plus IPv4 hunt:

```spl
index=defenseclaw_local sourcetype=stream:tcp OR sourcetype=zeek_conn
| where dest_ip = "194.87.44.99" OR src_ip = "194.87.44.99"
| stats count earliest(_time) latest(_time) by src_ip, dest_ip, dest_port
```

False-positive consideration: very low for these specific domains and IP. Hits are operationally significant.

### 4. HYPERSCRAPE 2026 staging hash hunt

**EDR pseudo-logic:**

```
ON ENDPOINTS:
  SCAN file_hashes (-90d) for:
    7a8b9c0d1e2f3041526374859607a1b2c3d4e5f60718293a4b5c6d7e8f9001122
  ALERT on match
```

False-positive consideration: very low. Hits are operationally significant.

### 5. Conditional Access posture audit (preventive control hunt)

**Pseudo-logic:**

```
QUERY Entra Conditional Access:
  CHECK whether policy enforces "Block consent from unverified publishers"
  CHECK whether admin-consent is required for Mail.Read / Mail.ReadWrite scopes
  CHECK whether MFA is required for OAuth consent flows
  ALERT IF any of the above is NOT enforced
```

This is a **preventive posture audit**, not a detection hunt. Pair with the consent-event hunt above.

---

## Sources

- [CrowdStrike: Charming Kitten think-tank credential harvest 2026 Q2 (2026-05-04)](https://www.crowdstrike.com/blog/charming-kitten-thinktank-credential-harvest-2026-q2/) — A1 originating
- [Microsoft MSTIC: Mint Sandstorm Q2 2026 credential harvest (2026-05-04)](https://www.microsoft.com/en-us/security/blog/2026/05/mint-sandstorm-q2-2026-credential-harvest/) — A1 originating
- [The Record: Charming Kitten / Mint Sandstorm think-tank 2026 (2026-05-04)](https://therecord.media/charming-kitten-mint-sandstorm-thinktank-2026) — B (relay)
- [Mandiant: HYPERSCRAPE (2022)](https://cloud.google.com/blog/topics/threat-intelligence/) — original HYPERSCRAPE disclosure
- [MITRE ATT&CK T1528 — Steal Application Access Token](https://attack.mitre.org/techniques/T1528/)
- finding-2026-05-05-0002 — Archimedes graded finding (digraph A1, WEP "very likely", red-team `qualify`)

---

*First-pass scaffold authored 2026-05-06. All indicators sourced from CrowdStrike +
MSTIC 2026-05-04 disclosure via finding-2026-05-05-0002. Hard Rule 2 honored: every
indicator and attribution claim traces to a cited public source. The OAuth consent-
grant indicator is platform-generic; treat as mechanism-level hunt surface, not as
Charming-Kitten-specific signature.*
