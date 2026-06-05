## 📣 Discord Summary

Good morning. Here's your 0800 brief — 2026-05-19.

🚨 **Active Threats**

• **[Mini Shai-Hulud's largest single-day expansion: 639 npm versions across 323 packages](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html)** — Compromised `atool` maintainer; 22-minute burst across @antv + `echarts-for-react`. A parallel `actions-cool/issues-helper` tag-redirect ties in via shared C2 `t.m-kosche[.]com`. **SHA-pin Actions, audit npm trees, hunt that C2** *today*. TeamPCP per prior reporting.

• **[Nx Console `rwl.angular-console` 18.95.0 hit in an 11-minute window](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html)** — 498 KB stealer for 1Password, Claude Code, npm/GitHub/AWS creds; macOS `cat.py` LaunchAgent persistence. Separate cluster — *Archimedes does not propagate TeamPCP attribution.* Revoke creds for yesterday's installers; hunt the named paths.

🔓 **Vulnerabilities**

• **[CVE-2026-8153 — Universal Robots PolyScope 5 cobot unauth RCE, CVSS 9.8](https://www.securityweek.com/critical-vulnerability-exposes-industrial-robot-fleets-to-hacking/)** — Patched in 5.25.1; CISA advisory ICSA-26-134-17. No in-the-wild. **Audit PolyScope 5 inventory across supplier estate; check Dashboard Server segmentation.**

• **[Microsoft confirms restricted-network patching failures](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-patching-issues-in-restricted-windows-networks/)** — KB5083806 / KB5083631 January preview broke March-and-later updates on air-gapped + firewalled fleets. **Deploy the KIR MSI** on classified / IL5+ estates.

• **CVE-2026-20182 (Cisco SD-WAN):** KEV deadline lapsed Sunday — T+38h+, no fresh A-grade exploitation reporting.

📰 **Other Signal**

• **SEPPMail SEG seven-CVE cluster (CVSS up to 10.0):** all patched; US A&D-direct exposure low. Audit if deployed.
