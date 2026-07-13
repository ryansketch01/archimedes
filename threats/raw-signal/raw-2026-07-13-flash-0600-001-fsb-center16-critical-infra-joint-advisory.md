---
raw_id: raw-2026-07-13-flash-0600-001-fsb-center16-critical-infra-joint-advisory
collected_at: 2026-07-13T06:08:00-04:00
run_id: flash-sweep-20260713-060000
collection_mode: flash_sweep
test: false
source:
  source_yaml_id: bleepingcomputer
  source_name: BleepingComputer
  source_url: https://www.bleepingcomputer.com/news/security/us-and-allies-share-defense-tips-against-russian-hackers-targeting-critical-infrastructure/
  published_at: 2026-07-13T05:32:23-04:00
  originating_primary: NSA / FBI / CISA + 15 partner agencies (joint advisory; A-grade government)
  relay_grade: B
match_reason:
  watchlist: [aerospace-defense]
  actors: []
  vulnerabilities: [CVE-2018-0171]
  keywords: [defense industrial base, critical infrastructure, Cisco Smart Install, Russian state]
triage_tags: [non_flash, ad_sector_marginal, restatement, actor_not_in_roster, grader_queue_morning]
iocs_extracted: true
iocs_count: 1
promoted: false
ttl_expires_at: 2026-10-11T06:08:00-04:00
---

# US and allies warn of Russian critical infrastructure attacks (FSB Center 16)

Joint cybersecurity advisory (BleepingComputer relay, Sergiu Gatlan,
in-window 05:32 EDT) from NSA, FBI, CISA plus 15 additional agencies across
Australia, UK, Canada, New Zealand, Estonia, Finland, France, and Italy,
warning that Russian state hackers are targeting vulnerable and
poorly-configured routers to infiltrate critical infrastructure.

**Attribution (per advisory, verbatim class):** FSB Center 16, also tracked
as Berserk Bear / Energetic Bear / Crouching Yeti / Dragonfly / Ghost
Blizzard / Static Tundra.

**TTP:** Scanning for routers with default/weak SNMP credentials; spoofed IP
commands to extract device config files; TFTP exfiltration to attacker
servers; exploitation of Cisco Smart Install (CVE-2018-0171, CVSS 9.8,
exploited since November 2021).

**Targeted sectors (per advisory):** energy, communications, **defense
industrial base**, healthcare, financial services, **defense**, and
state/local government.

**Attribution status:** Ongoing confirmation / restatement of a known
long-running campaign, NOT new attribution — FBI previously warned of the
same group's Cisco activity in August 2025.

---

## Why this is NON-FLASH (characterization only — grader adjudicates)

- **Trigger 2 (tracked-actor attribution) FAILS:** FSB Center 16 / Berserk
  Bear / Dragonfly / Static Tundra is NOT in `_roster.yaml`. The roster's
  Russian actors are APT28 (GRU 26165), Sandworm (GRU 74455), and APT29
  (SVR). This is a distinct FSB cluster. Also an explicit restatement, not
  new attribution → fails the "new-not-restatement" condition independently.
- **Trigger 1 (critical-CVE-exploited) marginal-FAIL:** CVE-2018-0171 is
  CVSS 9.8 with confirmed active exploitation and an A-grade source, but it
  is a 2018 vuln inside an ongoing campaign, not a fresh exploitation event.
- **Trigger 5 (A&D-sector campaign) marginal-FAIL:** DIB and defense ARE
  named, but among seven broad critical-infra sectors — generic
  critical-infrastructure framing, restatement quality, not a
  defense-specific multi-victim campaign.

**Recommend:** Route to the 08:00 morning brief A&D / standing-section
queue. A-grade joint advisory naming the DIB is legitimate morning-brief
material even though it does not warrant an async FLASH. Potential
`/new-actor` consideration for FSB Center 16 / Berserk Bear (operator
discretion — roster gap: no FSB-attributed actor currently tracked).

## IOCs (FLASH-fast, inline)

- **CVE-2018-0171** — Cisco IOS / IOS XE Smart Install feature; CVSS 9.8;
  exploited by FSB Center 16 since Nov 2021 per advisory. Not a tracked
  vuln in `_index.yaml` (verify at grader).
- No atomic network IOCs (IP / domain / hash) in the BleepingComputer relay;
  the joint-advisory PDF may carry indicators — direct retrieval deferred to
  grader / vuln-tracker if promoted.
- Attribution claim recorded verbatim per Hard Rule 2 (FSB Center 16;
  Archimedes originates no attribution).
