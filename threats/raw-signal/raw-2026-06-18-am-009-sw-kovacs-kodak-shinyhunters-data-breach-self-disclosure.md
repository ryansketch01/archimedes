---
raw_id: raw-2026-06-18-am-009-sw-kovacs-kodak-shinyhunters-data-breach-self-disclosure
collected_at: 2026-06-18T07:46:00-04:00
run_id: pre-brief-20260618-073000
collection_mode: pre_brief_collection
source:
  source_yaml_id: securityweek
  source_name: SecurityWeek (Eduard Kovacs)
  source_url: https://www.securityweek.com/kodak-admits-data-breach-after-shinyhunters-hack-claims/
  published_at: 2026-06-18T03:18:51-04:00
match_reason:
  watchlist: []
  actors: []
  vulnerabilities: []
  keywords: [Kodak, ShinyHunters, "data breach", "self-disclosure", "vendor statement", extortion]
triage_tags: [extortion_claim, vendor_self_disclosure, not_ad_prime, no_roster_actor, hard_rule_2_binding_no_cross_walk, operator_deferred_new_actor_candidate_carry_forward, twin_surface_with_shinyhunters_peoplesoft_education]
iocs_extracted: false
iocs_count: 0
text_word_count: 400
promoted: false
rejected_at: 2026-06-18T08:24:00-04:00
rejection_id: reject-2026-06-18-0007
ttl_expires_at: 2026-09-16T07:46:00-04:00
---

# Kodak Admits Data Breach After ShinyHunters Hack Claims (SW-Kovacs primary)

**Publisher:** SecurityWeek (Eduard Kovacs byline)
**Published:** 2026-06-18T03:18 EDT
**URL:** https://www.securityweek.com/kodak-admits-data-breach-after-shinyhunters-hack-claims/

## Article body

**Victim:** Kodak (commercial printing and imaging technologies company)

**Incident details:** ShinyHunters claimed on June 15 to have stolen more than 2.2 million records containing customer personal information and corporate data from Kodak's systems. The threat actors demanded ransom, threatening to leak the stolen data on June 18.

**Kodak's response:** Kodak confirmed the breach in a statement to SecurityWeek. A company spokesperson said: "Kodak recently discovered that an unauthorized third party illegally gained access to a limited amount of company data."

The company added that it is "confident the incident was limited in scope and has been contained and that there is no threat to our systems or operations as a result of the incident." Kodak stated it is conducting an investigation with external cybersecurity experts and has notified law enforcement.

**Attribution:** The breach is attributed to ShinyHunters, a cybercrime group described as "highly active" that has conducted massive data theft campaigns over the past year. The group recently exploited a zero-day vulnerability in Oracle PeopleSoft (CVE-2026-35273) to target at least 100 organizations.

**Context:** ShinyHunters has demonstrated significant operational capability, targeting widely used enterprise software and conducting coordinated campaigns against multiple victims. The Kodak breach aligns with the group's established pattern of data exfiltration followed by extortion threats.

---

## Extraction notes

- Language: en
- Publisher byline: Eduard Kovacs (SecurityWeek)
- Article type: trade-press victim-self-disclosure relay
- Substrate role: SECOND-publisher (after BC-Gatlan 2026-06-17 AM raw-2026-06-17-am-014). Substrate-strengthening on Kodak victim-self-disclosure layer with Kodak vendor statement verbatim. Twin-surface with Mandiant cloud.google.com "ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit" title-only carry-forward (Mandiant index page enumerated at 2026-06-17 PM sweep, body retrieval still operator-deferred).
- T-gates evaluation: T1/T6 FAIL no fresh CVE this incident (PeopleSoft CVE-2026-35273 is carry-forward — KEV-listed 2026-06-12, retrospective-compliance phase); T2/T4 FAIL ShinyHunters NOT on 24-actor _roster.yaml — Hard Rule 2 BINDING, Archimedes does NOT cross-walk ShinyHunters to roster; T5 FAIL Kodak is consumer-imaging / commercial-printing NOT A&D-prime / DIB / CMMC / ITAR (despite Kodak's defense-imaging historical heritage, current Kodak is not on aerospace-defense.yaml watchlist); single-incident credential extortion. Critical-override 0-of-4. NOT FLASH-eligible.
- A&D-relevance: LOW direct. ShinyHunters/Kodak twin-surface with carry-forward Mandiant "ShinyHunters Education PeopleSoft" / Council of Europe leak claim (carry-forward from 2026-06-15 AM brief) / FulcrumSec extortion campaign (carry-forward from raw-2026-06-17-am-015 + 016) substrate-strengthening on operator-deferred /new-actor-ShinyHunters candidacy at the actor-identity layer. Possible morning brief Other Signal one-liner.
- Quote-budget for morning brief: Kodak spokesperson "no threat to our systems or operations as a result of the incident" 13-word at-cap option (good), Kodak "unauthorized third party illegally gained access" 6-word at-cap option, "limited in scope and has been contained" 7-word at-cap option.
- Attribution discipline: SW-Kovacs preserves "ShinyHunters" attribution verbatim per Kodak's self-disclosure timing pattern + leak-site coincidence. Hard Rule 2 BINDING. Archimedes does NOT cross-walk to APT41 / any roster-tracked actor with ShinyHunters alias overlap claims.
