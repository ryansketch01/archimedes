---
brief_id: 2026-07-14-afternoon
brief_type: afternoon
published_at: 2026-07-14T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: archimedes-red-team
human_override: null
word_count: 772
findings_referenced:
  - finding-2026-07-14-0004
  - finding-2026-07-14-0005
  - finding-2026-07-14-0006
  - finding-2026-07-14-0007
  - finding-2026-07-14-0008
  - finding-2026-07-14-0009
  - finding-2026-07-14-0010
tlp: CLEAR
discord_delivery:
  channel: intel-briefs
  message_ids:
    - "1526691088864382989"
    - "1526691105545130046"
  parts: 2
  delivered_at: 2026-07-14T16:01:12-04:00
  via: librarian
---

# Afternoon Brief — 2026-07-14

**Patch now: four actively-exploited flaws hit CISA KEV today** — two Microsoft zero-days (ADFS and SharePoint EoP) and two SonicWall SMA1000 flaws, all under BOD 22-01 deadlines.

**Why it matters:** All four sit on ubiquitous DIB infrastructure — federal identity, collaboration, remote access. Fifteen more critical CVEs (ColdFusion, VMware Avi) plus a resolved ShareFile zero-day round out a patch-heavy afternoon.

---

## 🚨 Active Threats

**Microsoft's July Patch Tuesday ships two KEV-listed zero-days.**
- **CVE-2026-56155** (ADFS EoP) and **CVE-2026-56164** (SharePoint EoP) shipped today and hit CISA KEV the same day. Active exploitation is **likely** — the directly-retrieved KEV listing is the load-bearing attestation, corroborated by Microsoft; media only relay that disclosure, so this is not a triangulated finding. Patch now — BOD 22-01 deadlines apply.
- **CVE-2026-50661 (BitLocker bypass)** is publicly disclosed but **not exploited** and needs physical access — distinct from June's [YELLOWKEY](../vulnerabilities/YELLOWKEY/profile.md) WinRE bypass. ADFS/SharePoint/BitLocker are DIB-ubiquitous: structural relevance, no A&D targeting, no actor.
- Source: [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2026-patch-tuesday-fixes-massive-570-flaws-3-zero-days/) · [SecurityWeek](https://www.securityweek.com/microsoft-patches-record-622-vulnerabilities-including-two-exploited-zero-days/) · CISA KEV v2026.07.14 · Digraph: A2 (facts A1; exploitation *likely* per red-team)

**CISA adds two actively-exploited SonicWall SMA1000 flaws to KEV.**
- **CVE-2026-15409** (unauthenticated SSRF) and **CVE-2026-15410** (authenticated-admin code injection) on SonicWall's remote-access gateway. Active exploitation is **likely** — CISA's single-source KEV determination, no independent telemetry this sweep; KEV does not assert the two chain.
- SMA1000 is an internet-facing perimeter appliance — a classic breach surface for any DIB or supplier estate. Mitigate/patch now under BOD 22-01; fixed versions aren't in the KEV entry — pull from SonicWall PSIRT / NVD.
- Source: [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A2 (KEV fact A1; exploitation *likely*, single-source)

**🗓️ Patch This Week (by exploitation status):**
1. **Exploited / KEV-listed — first:** Microsoft CVE-2026-56155 + CVE-2026-56164; SonicWall CVE-2026-15409 + CVE-2026-15410.
2. **Critical, no exploitation yet:** Adobe ColdFusion (8 CVEs, Priority 1); VMware Avi Load Balancer (7 CVEs, critical auth bypass).
3. **Resolved:** Progress ShareFile SZC (5.12.5 / 6.0.2).

## 🔓 Vulnerabilities

**Adobe patches eight critical ColdFusion CVEs (Priority 1).**
- Eight arbitrary-code-execution and privesc flaws, fixed in ColdFusion 2025 Update 11 / 2023 Update 22. Adobe reports no in-the-wild exploitation — current awareness, **not** safe-to-defer; ColdFusion's recent exploited-after-disclosure pattern makes rapid exploitation **likely** enough to patch fast.
- 🔗 **Distinct from** [VT-017 / CVE-2026-48282](../vulnerabilities/Adobe-ColdFusion-CVE-2026-48282/profile.md) — the actively-exploited KEV-listed RCE from ~2 weeks ago. Different cohort; don't conflate. Source: [SecurityWeek](https://www.securityweek.com/adobe-patches-critical-coldfusion-vulnerabilities/) · Digraph: B2

**VMware patches seven Avi Load Balancer flaws, headlined by a critical auth bypass.**
- **CVE-2026-47865** (critical auth bypass) through CVE-2026-47871 — RCE, privesc to root, directory traversal. No exploitation per Broadcom, but an unauthenticated auth-bypass chaining to root RCE on an ADC warrants prompt patching. Fixed versions weren't in the advisory — pull from Broadcom / NVD.
- Source: [SecurityWeek](https://www.securityweek.com/7-severe-vulnerabilities-patched-in-vmware-avi-load-balancer/) · Digraph: B2

**UPDATE: Progress confirms the ShareFile SZC emergency was a path-traversal zero-day — now patched.**
- Progress traced last week's emergency Storage Zone Controller shutdown to a high-severity path-traversal zero-day and shipped **SZC 5.12.5 / 6.0.2**. It allows authenticated-admin arbitrary file read, write, or enumeration (CVE reserved, ~2 weeks out); Progress reports no unauthorized access, so exploitation stays unconfirmed. This **retires the earlier speculated CVE-2026-2699/2701 vector** — the confirmed cause is a new reserved-CVE flaw.
- 🔗 **Update on:** 2026-07-10 afternoon and 2026-07-11 morning briefs. Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/) · Digraph: B2

## ✈️ Sector Focus: Aerospace & Defense

**Dutch AIVD/MIVD: a Russian intelligence service is compromising internet-connected cameras to surveil NATO logistics.**
- A joint AIVD/MIVD advisory (2026-07-10) says at least one Russian intelligence service is hijacking exposed IP cameras (default passwords, outdated firmware) to surveil NATO military-logistics routes and Ukraine-bound weapons shipments. Attribution stays generic — no service or APT named; Archimedes maps it to none.
- The targets are **military** logistics, not commercial primes — treat as defense-logistics-sector awareness plus physical edge-device hygiene (exposed cameras, default creds, firmware). Single-source, high-brittleness. Source: [The Record](https://therecord.media/russian-intelligence-compromising-cameras-nato-ukraine-netherlands) · Digraph: B2

**New M365 phishing kits Jalisco and OmegaLord defeat MFA — hardening, not hunting.**
- ReliaQuest details two kits: **Jalisco** abuses the OAuth 2.0 device-code flow (fresh codes in real time to beat the 15-minute window, up to five rogue devices per account); **OmegaLord** uses fake login pages that capture the victim's phone number to bypass MFA. Operators exfiltrate SharePoint in minutes, then extort.
- No atomic IOCs — actionability is **posture-hardening, not detection**: block device-code auth via Conditional Access, cut Entra device-registration limits (50 → 1-2), and restrict OAuth grants. M365/Entra is the DIB's dominant identity fabric — directly portable to A&D tenants. Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/) · Digraph: B2

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors (UNC1549, Charming Kitten, Handala Hack, MuddyWater) in the last 48h.

---

*Sources hyperlinked inline. Admiralty digraph noted per item. TLP:CLEAR unless flagged.*

## 📣 Discord Summary

Good afternoon. Here's your 1600 brief — 2026-07-14.

🚨 **Active Threats**

• **[Microsoft ships two exploited zero-days in July Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-july-2026-patch-tuesday-fixes-massive-570-flaws-3-zero-days/)** — ADFS (CVE-2026-56155) and SharePoint (CVE-2026-56164) EoP flaws hit CISA KEV today; exploitation likely (CISA + Microsoft attest, media only relay). BitLocker CVE-2026-50661: disclosed, not exploited. *Apply July updates now* — BOD 22-01 clocks running.

• **[CISA flags two exploited SonicWall SMA1000 flaws](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)** — unauth SSRF (CVE-2026-15409) + admin code injection (CVE-2026-15410) on the remote-access gateway. *Patch now*; fixed versions from SonicWall PSIRT.

🔓 **Vulnerabilities**

• **[Adobe patches 8 critical ColdFusion CVEs (Priority 1)](https://www.securityweek.com/adobe-patches-critical-coldfusion-vulnerabilities/)** — no exploitation yet, but ColdFusion's exploited-after-disclosure record means *patch fast* (CF2025 u11 / CF2023 u22). Separate cohort from the actively-exploited CVE-2026-48282.

• **[VMware patches 7 Avi Load Balancer flaws](https://www.securityweek.com/7-severe-vulnerabilities-patched-in-vmware-avi-load-balancer/)** — critical auth bypass CVE-2026-47865 chains to root RCE; no exploitation reported. Fixed versions via Broadcom/NVD.

• **UPDATE — [ShareFile emergency was a path-traversal zero-day](https://www.bleepingcomputer.com/news/security/progress-confirms-sharefile-zero-day-flaw-behind-storage-zone-shutdown/)** — Progress patched it (SZC 5.12.5 / 6.0.2), closing last week's shutdown; retires the speculated CVE-2026-2699/2701 vector.

✈️ **Sector Focus: A&D**

• **[Dutch AIVD/MIVD: a Russian intelligence service is hijacking exposed IP cameras](https://therecord.media/russian-intelligence-compromising-cameras-nato-ukraine-netherlands)** — to surveil NATO logistics and Ukraine-bound arms shipments. Attribution stays generic — no APT named. Defense-logistics awareness + camera hygiene; single-source.

• **[New M365 kits Jalisco & OmegaLord defeat MFA](https://www.bleepingcomputer.com/news/security/new-phishing-kits-target-microsoft-365-accounts-evade-mfa/)** — OAuth device-code abuse + phone-capture, SharePoint exfil in minutes. No IOCs — *harden posture*: block device-code auth, cut Entra device-registration limits, restrict OAuth grants.
