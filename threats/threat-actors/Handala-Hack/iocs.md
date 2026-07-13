---
actor_id: "014"
actor_name: Handala Hack
last_updated: 2026-07-12
admiralty_grade: A2
tlp: CLEAR
---

# Handala Hack — IOC Reference

**Actor #014** · Source of record for the structured sidecar `iocs.yaml`.

All indicators inherit from a single originating source — Check Point Research (CPR 2024 + CPR 2026), relayed in part by The Hacker News; CPR IOC appendices not directly retrieved. Admiralty A2. **9 IP indicators** total: 2 VirusTotal-confirmed (higher confidence) and 7 reported-but-not-individually-VT-checked (lower confidence). **Wiper hash VALUES are held `pending_direct_retrieval`** — see §4.

**First-party Splunk sentinel (2026-07-12):** 0 hits over -90d across `defenseclaw_local` and `archimedes` on all 9 IPs. Per Hard Rule 8, silent Splunk does NOT disconfirm — Frank is not an Israeli/Albanian/US-medical-tech victim matching the target profile. Visibility-bounded null, not negative evidence.

---

## 1. CVEs Actively Exploited

No specific CVE is attributed to this actor in the retrieved reporting. CPR describes external-facing exploitation for access generically (T1190) but names no CVE ID. Referenced by ID only per Hard Rule 3 if any surfaces on direct retrieval.

*No documented CVE indicators at this time.*

---

## 2. Malicious Delivery Domains

No documented delivery domains at this time. The reporting provides operator IPs (§3), not staging domains.

---

## 3. IP Addresses

### Higher confidence — VirusTotal-confirmed

| IP | Confidence | VT | Hosting | Set | Role |
|---|---|---|---|---|---|
| 64.176.169.22 | High | 10 engines malicious (2026-06-26) | Vultr / Constant, AS20473, `64.176.160.0/19` | 2024 | Operator / C2 |
| 82.25.35.25 | High | 9 engines malicious (2026-07-09) | Zenlayer, AS21859, `82.25.35.0/24` | 2026 | Operator / C2 |

### Lower confidence — reported, not individually VT-checked

| IP | Confidence | Hosting / Note | Set |
|---|---|---|---|
| 64.176.172.235 | Low | Same Vultr /19 cluster as .169.22 | 2024 |
| 64.176.172.165 | Low | Same Vultr /19 cluster | 2024 |
| 64.176.173.77 | Low | Same Vultr /19 cluster | 2024 |
| 64.176.172.101 | Low | Same Vultr /19 cluster | 2024 |
| 31.57.35.223 | Low | Reported by CPR relay | 2026 |
| 107.189.19.52 | Low | `107.189.0.0/16` frequently-abused hosting | 2026 |
| 146.185.219.235 | Low | Reported by CPR relay | 2026 |

*(Network-infrastructure TTL 90 days — re-validate before long-term reliance. The lower-confidence IPs sit on shared commercial hosting; confirm the peer before blocking.)*

---

## 4. File Hashes

**No file hashes are published in this dossier.** CPR's reports list wiper hashes (SHA-256 in 2024; MD5 in 2026 for Handala Wiper, a PowerShell wiper, VeraCrypt, and NetBird), but the values surfaced via WebFetch summarization were **garbled** — the two spot-checked returned `found:false` on VirusTotal, a strong signal the summarizer corrupted the strings.

Hash **values are held `pending_direct_retrieval`** of the CPR IOC appendix (anti-bot). Malware **families** are recorded in `profile.md` → Malware Arsenal (BiBi, Cl Wiper, partition wipers, Handala Wiper, PowerShell wiper, Karma Shell). Hash strings are deliberately **not** folded into `iocs.yaml` — Archimedes does not transcribe unverified/garbled hashes. NetBird and VeraCrypt are legitimate dual-use tools; their hashes are low-value even if later confirmed.

---

## 5. Registry Indicators

No documented registry indicators at this time.

---

## 6. File / Host Artifacts (low value — context only)

Recorded for traceability, **not** as high-confidence atomic IOCs:

- Attacker machine names `DESKTOP-FK1NPHF`, `WIN-P1B7V100IIS` — default-Windows-style naming, low standalone fidelity.
- Starlink / commercial-VPN source ranges surfaced (`188.92.255.x`, `209.198.131.x`, `149.88.26.x`, `169.150.227.x`) — shared-egress artifacts, low standalone value.

Hunt on these only as corroborating context alongside the operator IPs (§3) or the behavioral hunts (§8).

---

## 7. Cloud C2 Infrastructure

No attacker-controlled cloud-service C2 is documented. The strategically significant "cloud" vector here is **abuse of the victim's own cloud management plane** — Microsoft Intune MDM used to issue legitimate remote-wipe commands (the Stryker vector). That is a behavioral/TTP concern, not an attacker-infrastructure IOC — see the Intune mass-wipe hunt in §8.

---

## 8. Detection Queries (Hunt Guidance)

### Hunt A — Operator IPs in network logs (Splunk)

```spl
index=defenseclaw_local (sourcetype=dns OR sourcetype=proxy OR sourcetype=firewall
  OR sourcetype=stream:* OR sourcetype=netflow)
  (dest_ip IN ("64.176.169.22","82.25.35.25","64.176.172.235","64.176.172.165",
    "64.176.173.77","64.176.172.101","31.57.35.223","107.189.19.52","146.185.219.235")
   OR src_ip IN ("64.176.169.22","82.25.35.25","64.176.172.235","64.176.172.165",
    "64.176.173.77","64.176.172.101","31.57.35.223","107.189.19.52","146.185.219.235"))
| stats count min(_time) as first_seen max(_time) as last_seen
        values(dest_ip) as dest_ips values(dest_port) as ports by src_ip, host
```

False-positive note: prioritize the two VT-confirmed IPs. The other seven are lower-confidence and sit on shared commercial hosting — confirm the peer before acting.

### Hunt B — Anomalous bulk MDM remote-wipe / retire (Intune) — behavioral

```spl
index=defenseclaw_local (sourcetype=intune OR sourcetype=azure:audit OR sourcetype=m365:audit)
  (Operation="*Wipe*" OR Operation="*Retire*" OR Operation="*FreshStart*"
   OR Operation="*RemoteWipe*" OR Operation="*deleteManagedDevice*")
| bucket _time span=1h
| stats count values(Operation) as ops dc(target_device) as devices_actioned
        by _time, initiator_user, initiator_ip
| where devices_actioned >= 10
| sort - devices_actioned
```

False-positive note: this targets the **Stryker-style Intune mass-wipe TTP** (T1485 via a compromised MDM tenant), not a specific hash/IP. Tune `devices_actioned` to your fleet's legitimate bulk-action baseline (offboarding waves, device refreshes). Correlate the initiator against known admin activity and change tickets — an unrecognized initiator issuing bulk wipe/retire is high-severity.

### Hunt C — Off-the-shelf tunnelers / overlay + web-shell context (EDR)

```spl
index=defenseclaw_local (sourcetype=Sysmon OR sourcetype=edr)
  (process_name IN ("netbird.exe","netbird-*") OR CommandLine="*reGeorge*"
   OR CommandLine="*tunnel.jsp*" OR CommandLine="*tunnel.aspx*")
| stats count values(process_name) as procs values(CommandLine) as cmds
        min(_time) as first_seen by host, User
```

False-positive note: NetBird is a legitimate overlay tool — alert only where it is not sanctioned. reGeorge/web-shell tunnel filenames are heuristics, **not** confirmed hashes (no verified hashes available). Correlate with Hunt A and with anomalous internet-facing-server child processes (web-shell context, T1505.003).

*No hash-based hunts are provided — there are no verified hashes to hunt on (held pending direct retrieval, §4).*

---

## 9. Sources

- Check Point Research — "Bad Karma, No Justice: Void Manticore Destructive Activities in Israel" (2024-05). Originating primary; IOC appendix not cleanly retrieved.
- Check Point Research — "'Handala Hack' — Unveiling Group's Modus Operandi" (2026). Originating primary; not directly retrieved; exact date pending.
- MITRE ATT&CK Group G1055 (Void Manticore) — cluster + tooling reference.
- The Hacker News (2024-05-20) — RELAY of CPR; not independent corroboration.
- Krebs on Security — Stryker incident (cross-referenced by CPR; not directly retrieved).
- Originating raw-signal: `raw-2026-07-12-handala-newactor-001`, `raw-2026-07-12-handala-newactor-002`.

*IOC set is single-origin and will grow / firm up on direct CPR appendix retrieval (verified wiper hashes) or independent second-IR-vendor corroboration.*
