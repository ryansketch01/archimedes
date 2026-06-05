## 📣 Discord Summary

Good morning. Here's your 0800 brief — 2026-05-29.

🚨 **Active Threats**

- **[Microsoft says three Chaotic Eclipse Windows zero-days now actively exploited](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085)** — Per MSRC's May 27 statement plus two trade-press relays (Security Affairs May 29; The Register May 28), **BlueHammer (CVE-2026-33825, patched May PT), RedSun, UnDefend** now under active exploitation. *No IR-firm telemetry corroborates yet; MSRC is both load-bearing source AND counterparty to the dispute.* *Patch May PT backlog now*; RedSun/UnDefend unpatched.

- **[MSTIC: `vpmdhaj` npm typosquat campaign steals AWS, Vault, npm publish tokens](https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/)** — Single maintainer published 14 typosquat packages May 28, harvesting AWS IMDSv2/ECS, Secrets Manager (16+ regions), Vault, GitHub Actions, npm publish tokens. Defender signed `Trojan:JS/ShaiWorm` — *family-name is internal classification, not attribution to TeamPCP per prior reporting*. *Block `aab.sportsontheweb.net`; alert on header `X-Supply: 1`.*

🔓 **Vulnerabilities**

- **[Oracle CPU May 2026 — nine criticals, CVSS 10.0 RCE in REST Data Services](https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV3Severity=CRITICAL)** — Patches May 28. DIB priorities: **CVE-2026-46840** (REST Data Services 10.0 scope-change RCE), **CVE-2026-46817** (EBS Payments 12.2.3–12.2.15, 9.8 pre-auth takeover), **CVE-2026-46833** (Database Net Service 9.0 pre-auth). No ITW, no PoC; Oracle CVEs typically see PoC within 3–14 days. *Inventory and patch.*

- **CVE-2026-45585 (YellowKey, BitLocker)** carry-forward — MSRC "exploitation more likely," public PoC, unpatched. Physical-access / SCIF re-entry threat model.
