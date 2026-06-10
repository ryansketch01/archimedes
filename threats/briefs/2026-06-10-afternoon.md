---
brief_id: 2026-06-10-afternoon
brief_type: afternoon
published_at: 2026-06-10T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_invoked_no_substantive_predictive_or_attributive_claim_above_likely_this_cycle
human_override: null
status: published
run_id: afternoon-20260610-160000
word_count: 1180
findings_referenced:
  - finding-2026-06-10-0010   # Veeam CVE-2026-44963 CVSS 9.4 domain-joined low-priv RCE
  - finding-2026-06-10-0011   # protobufjs proto6 six-CVE cluster (Cyera Research)
  - finding-2026-06-10-0012   # ShinyHunters Oracle PeopleSoft self-attested 300 instances
  - finding-2026-06-10-0008   # Exchange CVE-2026-42897 GA patch ships; VT-008 patched
  - finding-2026-06-10-0009   # Fortinet FortiSandbox + SAP NetWeaver June 2026 patch cluster
  - finding-2026-06-10-0016   # Adobe June 2026 PT — 123 CVEs, ColdFusion highest priority
  - finding-2026-06-10-0007   # Lumen JDY botnet; hedged Volt Typhoon associative
  - finding-2026-06-10-0015   # UPDATE — ServiceNow AM-006 material extension
  - finding-2026-06-10-0017   # Krebs OSINT — The Gentlemen RaaS / Yapaev (per-Krebs)
  - finding-2026-06-10-0013   # DINUM Tchap French government messaging breach
  - finding-2026-06-10-0014   # ICS Patch Tuesday — Siemens/Schneider/Phoenix Contact
related_vulns:
  - CVE-2026-44963   # Veeam VBR domain-joined low-priv RCE
  - CVE-2026-44295   # protobufjs proto6 code injection (pbjs)
  - CVE-2026-44290   # protobufjs proto6 process-wide DoS
  - CVE-2026-44291   # protobufjs proto6 prototype-pollution-to-code-execution gadget
  - CVE-2026-44292   # protobufjs proto6 prototype injection (generated constructors)
  - CVE-2026-42897   # MS Exchange OWA — GA patch (VT-008 state transition)
  - CVE-2026-25089   # Fortinet FortiSandbox unauth WEB UI command injection
  - CVE-2026-44748   # SAP NetWeaver XML signature wrapping (SAML)
  - CVE-2026-27671   # SAP NetWeaver RFC memory corruption
  - CVE-2026-22732   # SAP Commerce Cloud Spring Security
  - CVE-2026-40128   # SAP NetWeaver directory traversal
  - CVE-2026-35616   # FortiClient EMS (Lumen JDY rapid-targeting; Arctic Wolf cross-corpus)
  - CVE-2025-15467   # OpenSSL re-exposed in Siemens Scalance/Simatic/Sinamics/Sinec
related_actors:
  - "ShinyHunters (self-attested scope only — not Archimedes-confirmed)"
  - "JDY operator (Lumen hedged-associative to Volt Typhoon #008; ACH ranks H1 fifth)"
  - "The Gentlemen (NOT in roster; /new-actor candidate; per-Krebs Breadcrumbs, not LE-confirmed)"
related_zero_days: []
related_campaigns:
  - veeam_kev_attractor_pattern_watch
  - patch_tuesday_june_2026_cluster_cross_vendor
  - cve_2026_35616_forticlient_ems_dual_campaign_arctic_wolf_lumen_jdy
update_on:
  - 2026-06-10-am-006   # ServiceNow API exploitation — material extension
tlp: CLEAR
discord_delivery:
  channel: intel-briefs
  channel_id: "1499952717173358672"
  message_ids:
    - "1514374308527345745"
  parts: 1
  delivered_at: 2026-06-10T17:02:55-04:00
  late: false
  via: librarian
watch_signals_set:
  - watchtowr_post_disclosure_poc_publication_veeam_cve_2026_44963
  - tier_1_ir_firm_telemetry_veeam_or_protobufjs_exploitation
  - cisa_kev_addition_any_today_cluster_cve
  - second_tier_1_vendor_independent_attribution_jdy_to_volt_typhoon
  - lumen_primary_blog_direct_retrieval_for_full_ioc_set
  - servicenow_cve_assignment_window_2026_06_10_to_2026_06_17
  - oracle_response_or_advisory_on_peoplesoft_shinyhunters_claim
---

# Afternoon Brief — 2026-06-10

**June Patch Tuesday lands a heavy cluster: Veeam ships a CVSS 9.4 backup-server RCE reachable by any domain user, Adobe flags ColdFusion as its highest-priority fix, Fortinet and SAP add five more critical CVEs, and Cyera surfaces six new protobufjs CVEs with public exploit code reported for one.**

**Why it matters:** Backup servers, ERP, and Node.js dependency graphs are core A&D enterprise surface. Three items carry ransomware-staging or supply-chain economics. Patch windows are short.

---

## 🚨 Active Threats

**Veeam VBR — CVSS 9.4 RCE reachable by any domain user**
- What: Veeam KB4830 patches CVE-2026-44963 — low-privileged-domain-user RCE on domain-joined VBR (≤12.3.2.4465). v13.x not affected. Researcher credit: Sina Kheirkhah (WatchTowr Labs). Three publisher-independent primaries; no ITW per vendor at disclosure.
- Why it matters for A&D: VBR is the dominant enterprise backup platform across A&D primes. A domain-user-reachable backup-server RCE is a ransomware-staging primitive. Veeam's CVE history (CVE-2024-40711, CVE-2023-27532) is a documented KEV attractor.
- Action: Patch domain-joined VBR to 12.3.2.4854 ASAP. Treat WatchTowr post-disclosure PoC publication as assumed-imminent.
- Source: [The Hacker News](https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-veeam-vulnerability-exposes-backup-servers-to-rce-attacks/) · [Security Affairs](https://securityaffairs.com/193385/uncategorized/critical-veeam-rce-flaw-lets-low-privilege-users-take-over-backup-servers.html) · Digraph: B2 (B1 on procedural facts — three independent primaries)
- Related: finding-2026-06-10-0010

**protobufjs / proto6 — six CVEs, public exploit code reported for one**
- What: Cyera Research's proto6 disclosure: CVE-2026-44295 (code injection in pbjs static output, CVSS 8.7); CVE-2026-44291 (prototype-pollution-to-code-execution gadget, CVSS 8.1); CVE-2026-44290 (process-wide DoS, CVSS 7.5); CVE-2026-44292 (prototype injection in generated constructors, CVSS 5.3); two additional CVEs in cluster. Fixed in protobufjs 7.5.6 / 8.0.2 and protobufjs-cli 1.2.1 / 2.0.2.
- Why it matters for A&D: protobufjs is a transitive dependency in Google Cloud client libs, CI/CD plumbing, and Node.js messaging frameworks. SBOM exposure is dispersed; inventory is the work.
- Action: Run dependency-graph search now; pin patched versions. Public exploit code is reported by SC Media (B3 single-source on the exploit-code framing); no ITW attestation.
- Source: [The Hacker News](https://thehackernews.com/2026/06/six-proto6-vulnerabilities-in.html) · [Cyera Research](https://www.cyera.com/research/proto6-the-schema-was-not-supposed-to-run) · Digraph: B2
- Related: finding-2026-06-10-0011

**ShinyHunters self-attests Oracle PeopleSoft mass campaign — scope is per-actor, not Archimedes-confirmed**
- What: ShinyHunters claims 300 PeopleSoft instances across 100+ organizations via a gadget chain of older and zero-day vulnerabilities. Nottingham University data on the group's leak site. BleepingComputer is sole primary; Oracle had not responded at publication. IOCs published: IPv4s 142.11.200.186–190, 108.174.202.99, 176.120.22.24, and domain `azurenetfiles.net`.
- Hard Rule 2: Archimedes does NOT propagate the 300/100+ scope claim or the "failed FBI portal attempt" line as confirmed — both are actor self-attestation single-sourced via BC. Failed-FBI is a press-relations precedent, NOT confirmed federal targeting. Structural PeopleSoft exposure across A&D ERP does NOT imply A&D-prime victims.
- Action: Sweep published IPv4s and `azurenetfiles.net` against perimeter telemetry. First-party Splunk silent over -90d (not disconfirming).
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/) · Digraph: B2 (scope and failed-FBI claim: B3 — single-source veto applied)
- Related: finding-2026-06-10-0012

---

## 🔓 Vulnerabilities

**Microsoft Exchange CVE-2026-42897 — GA patch ships; VT-008 transitions to patched**
- What: MSRC shipped the GA patch in the June 2026 cycle. ESU/EEMS mitigation posture matures to fully patched. KEV federal deadline (2026-05-29) already passed; active-exploitation claim remains MSRC sole-primary at +26 days, no Tier-1 IR corroboration.
- Action: Apply GA patch across Exchange 2016/2019/SE estate, all update levels. Online not affected.
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-exchange-server-zero-day-exploited-in-attacks/) · Digraph: B2 (active-exploitation layer WEP capped at "likely" — single-source veto persists)
- Related: finding-2026-06-10-0008 · VT-008

**Fortinet + SAP — five critical-class CVEs, no ITW per vendors**
- What: Fortinet PSIRT patches CVE-2026-25089 (FortiSandbox unauth WEB UI command injection, CVSS 9.1). SAP Security Patch Day ships four critical: CVE-2026-44748 (NetWeaver SAML XML signature wrapping, CVSS 9.9), CVE-2026-27671 (NetWeaver RFC memory corruption, CVSS 9.8), CVE-2026-22732 (Commerce Cloud Spring Security, CVSS 9.1), CVE-2026-40128 (NetWeaver directory traversal, CVSS 9.0). Patches concurrent with disclosure.
- Action: Inventory SAP NetWeaver and Commerce Cloud surfaces; FortiSandbox patches alongside Veeam this week. Watch WatchTowr / Horizon3.ai / Assetnote for post-disclosure PoC.
- Source: [The Hacker News](https://thehackernews.com/2026/06/ivanti-fortinet-and-sap-release-patches.html) · [BleepingComputer SAP](https://www.bleepingcomputer.com/news/security/sap-fixes-critical-flaws-in-netweaver-and-commerce-cloud/) · Digraph: B2
- Related: finding-2026-06-10-0009

**Adobe June Patch Tuesday — 123 CVEs across 10 products; ColdFusion is Adobe's highest priority**
- What: APSB26-66 Campaign Classic (two CVSS 10 CVEs), APSB26-64 ColdFusion (seven CVEs — Adobe-self-tagged highest priority), APSB26-63 Acrobat Reader (20 CVEs), APSB26-58 InDesign (12 CVEs), APSB26-57 Experience Manager Forms (3 CVEs). No ITW attested.
- Why it matters for A&D: ColdFusion has a documented CISA KEV attractor history. Acrobat Reader endpoint depth is wide.
- Action: Prioritize ColdFusion and Campaign Classic; queue Acrobat for endpoint patch cycle.
- Source: [SecurityWeek](https://www.securityweek.com/adobe-patches-123-vulnerabilities/) · [Qualys](https://blog.qualys.com/vulnerabilities-threat-research/2026/06/09/microsoft-and-adobe-patch-tuesday-june-2026-security-update-review) · Digraph: B2
- Related: finding-2026-06-10-0016

---

## ✈️ Sector Focus: Aerospace & Defense

Today's lead items map to A&D enterprise surface; each carries a structural-exposure caveat that does NOT name an A&D-prime victim.

- **Veeam VBR** is the dominant enterprise backup platform across A&D primes. Domain-user-reachable backup-server RCE is a ransomware-staging primitive.
- **SAP NetWeaver / Commerce Cloud and Oracle PeopleSoft** are common A&D HR/finance/supply-chain ERP. ShinyHunters has NOT named A&D victims; structural deployment is NOT a likely-victim inference.
- **ColdFusion** remains a documented KEV attractor; A&D contractor public-facing apps still carry it in the periphery.

No new sector-specific named-victim threats against watchlist companies in the reporting window.

## 🕵️ Actor Activity

**Lumen reports JDY botnet expansion to 1,500+ SOHO/IoT devices — "previously linked to" Volt Typhoon operations**
- What: Lumen Black Lotus Labs reports JDY growth from ~650 (Jan 2024) to 1,500+ MIPS-based SOHO/IoT devices (Cisco, Araknis, Mimosa, Ubiquiti, DrayTek, Hikvision, Linksys). Function: distributed scanning, SSL/TLS cert harvest, banner-fingerprinting — NOT DDoS or delivery. C2 is Tor-hidden. Per Lumen, U.S. military networks are the most prominent targeted sector. Rapid targeting of CVE-2026-35616 (FortiClient EMS) noted.
- Attribution framing (strict): Lumen's exact phrasing is "previously linked to Volt Typhoon operations" — hedged-associative, NOT direct ownership. Single-source veto applies — BC and THN relay Lumen and do not independently corroborate. Tor-hidden C2 is OFF-canonical for Volt Typhoon's documented LotL profile. Analyst ACH ranks two alternatives ahead of direct ownership: distinct China-nexus cluster (H2) and criminal botnet with PRC-aligned downstream customer (H3) — both zero inconsistencies vs H1's two.
- Cross-corpus: CVE-2026-35616 also surfaced in finding-2026-05-28-FLASH-1200-0001 (Arctic Wolf criminal-IR). Per analyst KAC, the dual-appearance reads as two campaigns sharing a high-attractiveness N-day, NOT shared toolkit.
- Action: Inventory SOHO/IoT periphery — branch offices, supplier connections, OT-adjacent admin networks. No infrastructure IOCs in the relay layer; Lumen primary not directly retrieved this sweep.
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/china-linked-jdy-botnet-expands-targeting-of-us-military-networks/) · [The Hacker News](https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html) · Digraph: B2 (attribution layer B3 — single-source veto; WEP capped at "likely")
- Related: finding-2026-06-10-0007 · Actor #008 Volt Typhoon (associative only; NOT Archimedes-confirmed) · CVE-2026-35616

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h.

## 📰 Other Signal

**🔗 UPDATE on AM-006 — ServiceNow names endpoint, bounds scope, publishes IPv4 IOC, confirms 2026-06-05 patch date**
- AM-006 covered ServiceNow's REST API exploitation disclosure (CVE pending). Material extension: endpoint `/api/now/related_list_edit/create` with `requires_authentication=false`; affected scope bounded to Australia platform release plus pre-Australia tenants with specific config changes; patched 2026-06-05 (not today's PT cycle); IPv4 IOC 51.159.98.241. Disclosed via customer-support bulletin behind login — no public CVE, no CISA notification.
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/servicenow-discloses-security-incident-exposing-customer-data/) · Digraph: B2 (BC sole-primary on extension layer; AM-006 three-source consensus on broader cluster carries)
- Related: finding-2026-06-10-0015 · finding-2026-06-10-0006

**Krebs identifies "The Gentlemen" RaaS administrator as Alexander Yapaev (Izhevsk, Russia) per Breadcrumbs methodology — NOT LE-confirmed**
- Per Krebs, a Breadcrumbs chain integrating Check Point, Intel 471, Flashpoint, Constella, KELA, and Epieos identifies The Gentlemen RaaS administrator. Per Check Point and Intel 471 via Krebs, the operator runs the locker, the RaaS panel, and takes 10% of ransoms. The group is reportedly 2026's second-most-active ransomware op (332 victims since mid-2025), runs a 90/10 affiliate split, hits internet-facing VPN/firewall, and per Krebs "moves quickly to encrypt entire networks within hours." Forum nicknames Hastalamuerte/Zeta88 pivot via email/Telegram/GitHub/phone selectors to Alexander Andreevich Yapaev, 36, Izhevsk. Yapaev did not respond to comment requests; identity chain is per-Krebs, not LE-confirmed.
- Why it matters for A&D: Internet-facing VPN/firewall + hours-to-encryption is canonical RaaS. The Gentlemen is NOT in the Archimedes roster — /new-actor candidate.
- Source: [Krebs on Security](https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/) · Digraph: B2 (OSINT identity-chain layer B3 — single-source veto applied)
- Related: finding-2026-06-10-0017 · /new-actor candidate

**French DINUM Tchap breach — 73,000 accounts, 650,000 messages exfiltrated (monitoring)**
- DINUM disclosed a 2026-06-09 breach of the Tchap (Matrix-protocol) education shard. Initial access via social-engineering account hijack; credential pivot allegedly via hardcoded LDAP credentials in a PowerShell script. Attribution unknown; account blocked; CNIL alerted. No formal IOCs; no A&D-prime victim. Cautionary tale on hardcoded credentials in scripts.
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/french-govt-messaging-service-breached-in-account-hijacking-attack/) · Digraph: C3
- Related: finding-2026-06-10-0013

**ICS Patch Tuesday — Siemens / Schneider / Phoenix Contact ship June cycle (monitoring)**
- SecurityWeek aggregates: Siemens SINEC INS, SIPROTEC 5, WinCC Certificate Manager; Schneider PowerLogic P7, EasyLogic T150 + Saitel DP RTU, EcoStruxure IT Data Center Expert; Phoenix Contact CHARX SEC-3xxx. CVE-2025-15467 (OpenSSL) re-exposed in Siemens Scalance/Simatic/Sinamics/Sinec lineup. SW article thin on CVSS/CVE-IDs/ITW status; vendor PSIRT primaries not retrieved.
- Source: [SecurityWeek](https://www.securityweek.com/ics-patch-tuesday-vulnerabilities-fixed-by-siemens-schneider-phoenix-contact/) · Digraph: C3
- Related: finding-2026-06-10-0014

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-06-10.

🚨 **Active Threats**

• **[Veeam CVSS 9.4 backup-server RCE — any domain user](https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html)** — CVE-2026-44963 in KB4830 (VBR ≤12.3.2.4465; v13.x clean). WatchTowr-credited; Veeam is a KEV-attractor. *Patch to 12.3.2.4854 right now.*

• **Six new protobufjs CVEs (Cyera proto6 via THN)** — prototype-pollution-to-RCE gadget chain; exploit code reported for one. Fixed in 7.5.6 / 8.0.2. *Run SBOM search now.*

• **ShinyHunters self-attests Oracle PeopleSoft campaign (BC sole)** — 300 instances / 100+ orgs claimed; Nottingham on leak site; Oracle silent. IOCs: 142.11.200.186–190, 108.174.202.99, 176.120.22.24, `azurenetfiles.net`. *Hard Rule 2: self-attestation.*

🔓 **Vulnerabilities** (no ITW)

• Exchange CVE-2026-42897 GA patch ships; VT-008 patched.
• Fortinet FortiSandbox 9.1 + four SAP NetWeaver/Commerce Cloud CVEs 9.0–9.9.
• Adobe 123 CVEs / 10 products — ColdFusion top priority; Campaign Classic has two CVSS 10s.

🕵️ **Actor Activity**

• **Lumen: JDY botnet at 1,500+ SOHO/IoT devices targets U.S. military** (BC/THN) — Lumen says *"previously linked to"* Volt Typhoon — hedged, not direct ownership. Tor C2 off-canonical; no second-vendor corroboration. *Archimedes does not endorse the headline.* Inventory SOHO/IoT periphery.

📰 **Other Signal**

• **UPDATE: ServiceNow (AM-006)** — endpoint `/api/now/related_list_edit/create`; Australia platform scope; patched 2026-06-05; IPv4 51.159.98.241; CVE pending.

• **Krebs IDs "The Gentlemen" RaaS admin as Alexander Yapaev (Izhevsk)** — Breadcrumbs via Check Point + Intel 471 + Flashpoint. 2026's #2 RaaS (332 victims); hits VPN/firewall. *Per Krebs, not LE-confirmed.* New-actor candidate.

• Monitoring: French DINUM Tchap (73k accounts); ICS PT — Siemens / Schneider / Phoenix Contact.
