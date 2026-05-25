---
brief_id: 2026-05-25-afternoon
brief_type: afternoon
published_at: 2026-05-25T16:00:00-04:00
authored_by: archimedes-briefer
grader_approval: archimedes-grader
red_team_review: not_required_wep_ceiling_likely_below_very_likely_threshold
human_override: null
status: published
run_id: afternoon-20260525-160000
word_count: 712
findings_referenced:
  - finding-2026-05-25-0003-netherlands-fiod-mirhosting-worktitans-seizure-russia-aligned-hosting-takedown
  - finding-2026-05-25-0002-teampcp-supply-chain-activity-through-2026-05-24-consolidation
carry_forwards_referenced:
  - cve-2026-9082-drupal-kev-due-date-t-2
  - cve-2026-42897-exchange-kev-due-date-t-4
  - cve-2026-45321-mini-shai-hulud-kev-absent-14-day-delay
related_vulns:
  - CVE-2026-9082
  - CVE-2026-42897
  - CVE-2026-45321
related_actors:
  - "001"
related_zero_days: []
related_campaigns:
  - teampcp-mini-shai-hulud-2026
  - stark-mirhosting-worktitans-russia-aligned-hosting-ecosystem
tlp: CLEAR
---

# Afternoon Brief — 2026-05-25

**Dutch FIOD seized 800+ servers and arrested two operators of the Stark Industries Solutions successor stack (MIRhosting and WorkTitans BV) on 2026-05-18** — the first EU member-state enforcement action with arrests against the Russia-aligned hosting ecosystem that historically backstops APT28, Sandworm, and APT29 proxy and DDoS operations.

**Why it matters:** This is supporting-infrastructure disruption, not direct A&D-prime impact. Generic "Russia-backed hacking groups" attribution — no roster actor named per Krebs. Expect successor-entity emergence in another EU-adjacent jurisdiction over the coming weeks; watch new hosting providers with rapid network-asset transfers and BGP/RIPE pivots.

---

## 🚨 Active Threats

**Netherlands FIOD raids and arrests on Stark/MIRhosting/WorkTitans operators (LE-takedown signal; first corpus citation)**
- What: Dutch financial-crimes service (FIOD) raided three businesses in Enschede and Almere plus two data centers in Dronten and Schiphol-Rijk on 2026-05-18. Arrested Andrey Nesterenko (39, MIRhosting founder + Innovation IT Solutions Corp founder; Russian native) and Youssef Zinad (57, WorkTitans BV co-controller and prior MIRhosting employee). Seized 800+ servers plus laptops and telephones. Charges: violating EU sanctions law by making economic resources available to sanctioned entities — Stark Industries Solutions (EU-sanctioned 2025-05) and PQHosting / Neculiti brothers (EU-sanctioned 2025-05). WorkTitans BV operates as the.hosting successor to Stark and gets upstream connectivity solely through MIRhosting per Krebs's 2025-09 chain.
- Why it matters for A&D: Indirect ecosystem disruption. The infrastructure ecosystem that supports proxy and DDoS-staging for Russia-aligned operations against EU and NATO surfaces — including any A&D-prime-targeting sub-campaigns by [APT28](../threat-actors/APT28/profile.md), Sandworm (#007), and APT29 (#009) — loses a meaningful uplink. Per Krebs citing de Volkskrant's data review, WorkTitans and MIRhosting were the most-used networks in pro-Russian attacks on Danish government bodies during the 2025-11-13 to 2025-11-19 municipal elections window. MIRhosting's post-raid statement denies DDoS-consistent traffic in their network during that window; the attestation tension is on the activity layer, not the procedural-facts layer.
- Source: [Krebs on Security](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/) citing de Volkskrant and FIOD official statement · Digraph: B2 · WEP: very likely (procedural facts) / likely (ecosystem-attribution chain — single-source veto applies on Krebs's multi-year investigation arc)
- Hard Rule 2: **Krebs uses generic "Russia-backed hacking groups" framing alongside a parallel reference to Russia's intelligence agencies. No specific tracked actor is named. Archimedes does not promote to APT28 / Sandworm / APT29 attribution.** Related: finding-2026-05-25-0003.

## 🔓 Vulnerabilities

**KEV deadline calendar — T-2 and T-4 status tick; substance unchanged from morning**
- **CVE-2026-9082 (Drupal Core SQLi, PostgreSQL path)** — federal due Wednesday 2026-05-27 (T-2, ~36h from now). Action window narrowing. Confirm contractor-portal and vendor-microsite patch coverage before EOD tomorrow.
- **CVE-2026-42897 (Exchange OWA XSS)** — federal due Friday 2026-05-29 (T-4). MSRC blog surface still template-only / 403 this sweep. ESU-only patch path plus EEMS/EOMT mitigation unchanged. Active-exploitation single-source veto on MSRC originating tag still holds — Mandiant, Volexity, Unit 42, MSTIC TI blog, CrowdStrike silent on telemetry-backed corroboration.
- **CVE-2026-45321 (Mini Shai-Hulud / OIDC credential abuse chain) — NOT on KEV as of catalog version 2026.05.22.** Independently verified this sweep against the CISA catalog. 14-day delay from the 2026-05-18 Nx Console publish — materially atypical for CVSS-9.6 with GitHub-internal-compromise and Microsoft-SDK trojanization scope. Defender-context watch only; no federal compliance gate to enforce against it. Carry the watch into next week's brief windows.
- Source: [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · Digraph: A1 (KEV listings + KEV-absence verification)

## ✈️ Sector Focus: Aerospace & Defense

No new sector-specific cyber threats against watchlist companies in the reporting window. Tracked A&D-targeting actors ([APT28](../threat-actors/APT28/profile.md), [UNC1549](../threat-actors/UNC1549/profile.md), Lazarus, APT41, Salt Typhoon) silent this sweep.

## 🕵️ Actor Activity

**TeamPCP (#001) — one-week consolidation through 2026-05-24 surfaces three net-new capability layers (monitoring tier)**
- What: SANS ISC's Kenneth Hartman published a one-week TeamPCP consolidation on 2026-05-25 citing Microsoft, SafeDep, GitHub CISO Alexis Wales, and unnamed vendors. Three layers are net-new versus corpus: (1) a TeamPCP framework source-code public drop to GitHub on 2026-05-22 with README strings "Love - TeamPCP" and "Change keys and C2 as needed" plus at least three forks within hours including a FreeBSD variant — **vendor primary not named by Hartman, retrieval pending**; (2) a durabletask Linux disk-wiper capability cited via SafeDep's 2026-05-20 primary — **first-observation language pending grader verification** (if confirmed, this is a destructive-category addition to predominantly credential-theft tradecraft and a threat-box recalibration trigger for actor #001); (3) the CISA-not-on-KEV verification covered above.
- Why it matters for A&D: If the framework-leak claim holds, TeamPCP TTPs will commoditize through the fork ecosystem and proliferate to non-TeamPCP operators. The fork-and-customize invitation in the README is the load-bearing signal. DIB engineering estates with npm or PyPI exposure should treat post-2026-05-22 derivatives of the campaign-source pattern as in-scope for the same defender posture as the original.
- Source: [SANS Internet Storm Center diary 33016](https://isc.sans.edu/diary/rss/33016) (Kenneth Hartman; handler Didier Stevens) · Digraph: B3 (cluster anchor — framework-leak layer single-source via Hartman citing unnamed vendor primary; durabletask disk-wiper layer pending SafeDep first-observation verification) · WEP: likely (framework-leak claim; single-source veto applies) / very likely (CVE-2026-45321 KEV-absence sub-layer, independently verified)
- Hard Rule 2: **Hartman's piece is secondary synthesis. TeamPCP attribution chain is preserved through-cite to corpus-anchored primaries (Wiz, StepSecurity, Snyk on Mini Shai-Hulud; TeamPCP self-claim on Breached for the 2026-05-20 GitHub-corp surface). Archimedes does not promote Hartman to new first-observation attribution.** Related: finding-2026-05-25-0002.

## 🇮🇷 Iran Cyber Watch

No new activity from tracked Iranian actors ([UNC1549](../threat-actors/UNC1549/profile.md), [Charming Kitten](../threat-actors/Charming-Kitten/profile.md), Handala Hack, [MuddyWater](../threat-actors/MuddyWater/profile.md)) in the last 48h.

## 📰 Other Signal

**Megalodon — no material updates since [morning brief](2026-05-25-morning.md).** SafeDep primary unchanged; no second A/B-grade vendor corroboration in this window. Defender action (alert on `.github/workflows/*.yml` additions from no-history accounts; audit pinned `@tiledesk/tiledesk-server` versions) carries forward.

**First-party Splunk:** Zero `defenseclaw_local` events on the afternoon sentinel sweep (TeamPCP framework-leak strings, MIRhosting / WorkTitans organizational identifiers, FIOD-named persons, plus carry-forward Megalodon and tracked-actor tokens). **56th consecutive dormant non-self sweep.** Hard Rule 8 framing: first-party silence is neither confirming nor disconfirming; `defenseclaw_local` is structurally bounded by its narrow ingest scope.

---

*Sources hyperlinked inline. Digraph per item. TLP:CLEAR.*

## 📣 Discord Summary

Good afternoon — 1600 brief, 2026-05-25. **Dutch FIOD seized 800+ servers and arrested two operators of the Russia-aligned MIRhosting/WorkTitans hosting stack May 18.**

🚨 **Active Threats**

• **[Netherlands seizes 800 servers in Russia-aligned hosting takedown](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)** — FIOD raided MIRhosting + WorkTitans BV across four Dutch sites May 18; arrested Nesterenko + Zinad. Charges: violating EU sanctions by aiding Stark + PQHosting. *Per Krebs, generic "Russia-backed hacking groups" — Archimedes does not promote to APT28/Sandworm/APT29.* **Watch for a successor entity in an EU-adjacent jurisdiction.**

🔓 **KEV deadlines**

• **CVE-2026-9082 Drupal SQLi — due Wed May 27** (~36h). *Patch contractor portals + vendor microsites by EOD tomorrow.*
• **CVE-2026-42897 Exchange OWA XSS — due Fri May 29.** No MSRC GA; ESU + EEMS/EOMT only. MSRC single-source veto holds.
• **CVE-2026-45321 Mini Shai-Hulud — verified NOT on KEV** as of catalog 2026.05.22. 14-day delay, atypical for CVSS-9.6 scope.

🕵️ **Actor Activity**

• **[TeamPCP one-week consolidation — three net-new layers](https://isc.sans.edu/diary/rss/33016)** — Hartman/SANS ISC: (1) framework source dropped to GitHub May 22 with "Love - TeamPCP" + "Change keys and C2 as needed" READMEs, three+ forks within hours including FreeBSD — *vendor primary unnamed*; (2) durabletask Linux disk-wiper — *SafeDep first-observation pending*; (3) CISA-not-on-KEV above. **If the framework-leak holds, TeamPCP TTPs commoditize via the fork ecosystem.**

📰 **Other Signal**

• **Megalodon:** no material updates since morning; defender action carries forward.
• **Splunk:** zero `defenseclaw_local` hits on afternoon 17-IOC sweep — 56th consecutive dormant non-self sweep. *Silence ≠ disconfirming (Hard Rule 8).*
