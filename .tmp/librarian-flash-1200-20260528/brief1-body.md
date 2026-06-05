
# ⚡ FLASH: FortiClient EMS CVE-2026-35616 (CVSS 9.1) — Arctic Wolf observes fresh exploitation; patch shipped April in 7.4.7

*2026-05-28 12:35 EDT · B2 · WEP likely · TLP:CLEAR · posts immediately, within active hours*

**Action.** DIB / CMMC operators running FortiClient Endpoint Management Server: confirm **7.4.7** (Fortinet, early April 2026) is deployed. Hunt outbound to **83.138.53.110** and for binary **`FortiEndpoint_Patch.exe`** (Arctic Wolf names the payload **EKZ Infostealer**) at -30d across EDR, endpoint, and proxy logs. Treat any pre-7.4.7 EMS box as compromise-suspect; triage before patching.

**What.** [Arctic Wolf reports](https://www.securityweek.com/critical-forticlient-ems-vulnerability-exploited-in-fresh-attacks/) an active May 2026 campaign against unpatched FortiClient EMS via CVE-2026-35616 — pre-auth API access bypass to privilege escalation. Attackers weaponize the management server's own update pipeline to push malicious PowerShell to managed endpoints, dropping a previously-unreported Windows infostealer. [The Hacker News](https://thehackernews.com/2026/05/threat-actors-exploit-critical.html) corroborates and adds filename plus exfil IP 83.138.53.110.

**Exploitation framing (single-source veto).** SecurityWeek and THN are two publishers relaying one originating vendor — Arctic Wolf — so they collapse to one effective source on the exploitation-observation layer. WEP capped at *likely* pending independent telemetry from Mandiant, CrowdStrike, Unit 42, MSTIC, Fortinet PSIRT, or any non-Arctic-Wolf vendor naming the IOC pair. CVE record and April patch availability sit at *very likely* (A1 procedural fact).

**Impact.** A&D-prime direct exposure is **structural-indirect** — EMS is standard endpoint management in DIB / CMMC estates, but **no A&D-prime, sector, or geography has been named**. Arctic Wolf names **no actor or nation-state**; *Archimedes does not originate one.* Historical FortiClient EMS exploitation has been attributed in later IR rounds to Iranian and Chinese state-aligned actors; field stays null here until an independent vendor names one.

**First-party Splunk.** Zero hits at -30d on IP + product + payload sweep across `defenseclaw_local` + `archimedes`. Per Hard Rule 8: silence is not contradiction. 67th consecutive dormant non-self sweep.

**Trigger 1 fit caveat.** Spec requires A-grade attestation. Arctic Wolf is provisional B (first corpus citation, vendor-IR-research category, 72h ratification to 2026-05-31); substantive threshold met, procedural grade a half-step below A. Critical override 1/4 — fails CVSS-10.0, tracked-actor, A&D-watchlist prongs.

**Sources.** [SecurityWeek (2026-05-28)](https://www.securityweek.com/critical-forticlient-ems-vulnerability-exploited-in-fresh-attacks/) — B relay · [The Hacker News (2026-05-28)](https://thehackernews.com/2026/05/threat-actors-exploit-critical.html) — B relay · Arctic Wolf — provisional B, sole originating vendor.

**Related.** [finding-2026-05-28-FLASH-1200-0001](../findings/finding-2026-05-28-FLASH-1200-0001-securityweek-forticlient-ems-cve-2026-35616-fresh-exploitation-arctic-wolf.md). No prior CVE-2026-35616 or EKZ Infostealer coverage in corpus.
