---
detection_id: det-2026-08-04-001
title: Greatness PhaaS — device-code phishing, AiTM session theft, PRT persistence
created_at: 2026-08-04T20:45:00-04:00
author: archimedes
status: draft
related_findings:
  - finding-2026-08-04-greatness-phaas   # exact id pending grader promotion
  - finding-2026-07-31-0002              # CaptiveCrunch / Storm-2945 (APT29) — same technique
  - finding-2026-07-14-0009              # Jalisco/OmegaLord OAuth device-code kits
mitre_attack:
  - T1621   # MFA request generation (device-code phishing)
  - T1557   # Adversary-in-the-Middle
  - T1539   # Steal web session cookie
  - T1098.005  # Account manipulation — device registration
  - T1114.003  # Email collection — mailbox forwarding rule
data_dependency: >
  Requires Entra ID / M365 sign-in + audit logs ingested into Splunk (Azure AD
  SignInLogs / AuditLogs, e.g. via the Splunk Add-on for Microsoft Cloud Services
  or Microsoft 365 App). As of 2026-08-04 these are NOT confirmed present in
  defenseclaw_local — this detection is written against the standard Azure AD
  schema and must be pointed at the real sourcetype once M365 telemetry is onboarded.
tlp: CLEAR
---

# Detection: Greatness PhaaS — device-code phishing, AiTM, PRT persistence

**Why:** Greatness (and the wider commodity AiTM/device-code PhaaS class — APT29's
Storm-2372, Jalisco/OmegaLord) defeats standard MFA by stealing live session cookies
and abusing the OAuth 2.0 device-authorization grant. Atomic IOCs rot fast (server-side
key validation, decoy pages, fast infra rotation), so **behavioral identity telemetry is
the durable detection surface, not blocklists.** These four analytics target the
technique, not the infrastructure.

> **Tuning note:** field names below use the Azure AD SignInLogs / AuditLogs schema
> (`authenticationProtocol`, `properties.*`). Replace `index=* sourcetype=azure:aad:signin`
> with your actual onboarded sourcetype and adjust field paths to match your add-on's
> field extractions. Baseline each search in your tenant before alerting — device-code is
> legitimately used by some CLI/IoT/smart-TV flows, so expect known-good to tune out.

---

## 1. Device-code authentication grant (primary — highest signal)

Device-code sign-ins are rare in most corporate tenants and are the core of the new
Greatness capability. Alert on any success, enrich with user/IP/location.

```spl
index=* sourcetype=azure:aad:signin authenticationProtocol="deviceCode"
| eval status=coalesce('status.errorCode', status_errorCode)
| stats count min(_time) as first max(_time) as last
        values(appDisplayName) as apps
        values(ipAddress) as src_ips
        values(location.countryOrRegion) as countries
        by userPrincipalName status
| where status=0
| convert ctime(first) ctime(last)
| sort - count
```

**Triage:** any successful device-code grant to a user who has no legitimate device-code
workflow = investigate. Foreign / hosting-ASN source IP raises priority. Pair with a
Conditional Access policy that **blocks the device-code flow globally** except where
explicitly needed (the single most effective control against this technique).

---

## 2. New device registration shortly after interactive/device-code sign-in (PRT persistence)

Greatness registers a device within minutes post-compromise to mint a Primary Refresh
Token. Correlate an `Add registered device` / `Register device` audit event closely
following a sign-in from an anomalous source.

```spl
index=* sourcetype=azure:aad:audit
  (operationName="Add registered device" OR operationName="Register device"
   OR operationName="Add device")
| rename properties.userPrincipalName as upn, properties.ipAddress as reg_ip
| join type=inner upn
    [ search index=* sourcetype=azure:aad:signin
      (authenticationProtocol="deviceCode" OR isInteractive=true)
      | rename userPrincipalName as upn, ipAddress as signin_ip
      | fields _time upn signin_ip authenticationProtocol ]
| eval mins_after=round((_time - _time)/60,1)
| where signin_ip!=reg_ip
| table _time upn signin_ip reg_ip authenticationProtocol operationName
```

**Triage:** device registration where the registering IP differs from a normal corporate
egress, especially within ~15 min of a device-code sign-in, is a strong PRT-persistence
signal. (Refine the time-proximity join with a `transaction`/`stats` window once you have
live data — the join above is a starting skeleton.)

---

## 3. Post-compromise mailbox forwarding / inbox rule creation

Greatness creates forwarding rules to suppress security alerts (often delayed). Alert on
inbox-rule / forwarding changes, prioritizing external forwarding targets.

```spl
index=* sourcetype=o365:management:activity
  (Operation="New-InboxRule" OR Operation="Set-InboxRule"
   OR Operation="Set-Mailbox" OR Operation="New-TransportRule")
| search (ForwardTo=* OR RedirectTo=* OR ForwardingSmtpAddress=* OR "ForwardAsAttachmentTo"=*)
| stats count values(Operation) as ops values(Parameters{}.Value) as rule_params
        by UserId ClientIP
| sort - count
```

**Triage:** any auto-forwarding to an external/consumer domain immediately after a
suspicious sign-in = likely mailbox rule abuse (T1114.003). Cross-check `UserId` against
analytics 1 and 2.

---

## 4. Infrastructure pivot (low-confidence, corroboration only)

If web-proxy / DNS / TLS-SNI telemetry is available, hunt the Greatness domain pattern.
Base domain and `[target]-[token]` subdomains are the durable pivots; the reported proxy
IP is weakly corroborated — do NOT hard-block on it alone.

```spl
index=* (sourcetype=*proxy* OR sourcetype=*dns* OR sourcetype=stream:dns OR sourcetype=stream:http)
  (query="*aitomayu.com" OR dest_host="*aitomayu.com" OR ssl_subject_common_name="*aitomayu.com"
   OR url="*aitomayu.com*")
| stats count min(_time) as first max(_time) as last values(src_ip) as src by query dest_host url
| convert ctime(first) ctime(last)
```

**Do NOT blocklist `38.248.95.214`** on current evidence (VT 1/91, GreyNoise-only,
shared Limestone Networks hosting) — monitor only.

---

## Recommended controls (defense, not detection)

- **Conditional Access: block the OAuth device-code flow** tenant-wide; allow only for
  explicitly enumerated device-code use cases. Single highest-value mitigation.
- **Phishing-resistant MFA** (FIDO2 / passkeys / certificate-based) — AiTM cookie theft
  cannot replay a hardware-bound credential.
- Alert on new device registrations and token-issuance anomalies (sign-in frequency,
  impossible travel, new PRT).
- Audit and restrict external mailbox auto-forwarding at the transport-rule level.
- User awareness: distrust unsolicited "enter this code" prompts (device-code social eng).
