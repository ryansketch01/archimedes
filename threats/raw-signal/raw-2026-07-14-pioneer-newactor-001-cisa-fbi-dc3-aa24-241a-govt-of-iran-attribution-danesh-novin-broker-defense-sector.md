---
raw_id: raw-2026-07-14-pioneer-newactor-001
collected_at: 2026-07-14T16:42:00-04:00
run_id: pioneer-newactor-20260714-1630
collection_mode: on_demand
on_demand_command: /new-actor Pioneer Kitten (net-new roster actor — operator Ryan approved; targeted cold-start dossier-seed collection pass)
source:
  # LOAD-BEARING US-GOV PRIMARY for the whole dossier: FBI + CISA + DoD Cyber
  # Crime Center (DC3) joint Cybersecurity Advisory AA24-241A, published
  # 2024-08-28. This is the source that names DEFENSE among US targeted sectors
  # (Intent-scoring-relevant) and states the Government-of-Iran linkage +
  # front company + Br0k3r/xplfinder persona.
  # CISA-hosted advisory page 403s on direct WebFetch (WAF, documented in
  # source-health cisa-advisories notes). IC3 PDF mirror (ic3.gov/CSA/2024/240828.pdf)
  # retrieved but rendered as corrupted binary. Content below reconstructed from
  # CLEAN RELAYS of the same primary: The Hacker News, SOC Prime, SOCRadar, MITRE
  # G0117, Tenable, Picus/SafeBreach. Attribution language cross-checked across
  # relays; verbatim strings preserved where multiple relays agreed.
  source_yaml_id: cisa-advisories
  source_name: "FBI / CISA / DC3 Joint CSA AA24-241A — Iran-based Cyber Actors Enabling Ransomware Attacks on US Organizations"
  source_url: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-241a
  primary_pdf_url: https://www.ic3.gov/CSA/2024/240828.pdf
  cisa_hosted_pdf_url: https://www.cisa.gov/sites/default/files/2024-08/aa24-241a-iran-based-cyber-actors-enabling-ransomware-attacks-on-us-organizations_0.pdf
  relay_urls:
    - https://thehackernews.com/2024/08/us-agencies-warn-of-iranian-hacking.html
    - https://socprime.com/blog/pioneer-kitten-attack-detection/
    - https://socradar.io/blog/dark-web-profile-fox-kitten/
    - https://attack.mitre.org/groups/G0117/
  published_at: 2024-08-28T00:00:00-04:00
admiralty_pre_grade: A1
admiralty_pre_grade_rationale: >
  Source A (official US-gov joint advisory: FBI + CISA + DC3 — same class as
  the corpus-baseline-A cisa-advisories / fbi-flash IDs). Content 1 (confirmed
  by multiple independent bodies co-signing; FBI investigation-derived). NOTE
  the verbatim attribution + IOC appendix were reconstructed via RELAYS this
  pass — the grader should treat the primary as directly-retrievable-pending
  (WAF/PDF-render blockers, not a fidelity problem). Pre-grade is a collector
  convenience flag, NOT a grading decision.
relay_vs_primary: primary_via_relay      # A-grade primary, reconstructed through B-grade relays this pass
match_reason:
  watchlist: [aerospace-defense]         # AA24-241A names US "defense" sector among victims
  actors: [Pioneer Kitten, Fox Kitten, UNC757, Parisite, Lemon Sandstorm, RUBIDIUM, Br0k3r]
  vulnerabilities: [CVE-2024-24919, CVE-2024-3400, CVE-2023-3519, CVE-2019-19781, CVE-2022-1388]
  keywords: [IRGC, Government of Iran, Danesh Novin Sahand, ransomware access broker, NoEscape, RansomHouse, ALPHV, BlackCat, defense sector, DIB, xplfinder]
  match_basis: >
    Targeted /new-actor cold-start pass to seed a NET-NEW roster entry for
    Pioneer Kitten (not currently in _roster.yaml; roster max is #028
    CyberAv3ngers). This file captures the FOUNDATIONAL US-gov attribution
    layer: the Government-of-Iran linkage, the Danesh Novin Sahand front
    company, the Br0k3r / xplfinder access-broker persona, the ransomware-
    affiliate relationships, the edge/VPN CVE set, and the US DEFENSE-sector
    targeting that is the load-bearing fact for later Intent scoring.
triage_tags: [new_actor_seed, iran_irgc, access_broker, ransomware_enabler, ad_sector, defense_sector_named, edge_device_exploitation, attribution_foundation, on_demand_newactor]
iocs_extracted: true
iocs_count: 9        # 7 CVEs + 2 persona handles folded; network IOC appendix (IPs/domains/hashes) held pending_direct_retrieval
text_word_count: 1180
promoted: false
ttl_expires_at: 2026-10-12T16:42:00-04:00
---

# FBI / CISA / DC3 AA24-241A — Iran-based Cyber Actors Enabling Ransomware Attacks on US Organizations (2024-08-28)

Foundational attribution and TTP report for the actor Ryan approved as a NET-NEW
roster build: **Pioneer Kitten** (aliases Fox Kitten, UNC757, Parisite, Lemon
Sandstorm, RUBIDIUM; access-broker persona **Br0k3r** / **xplfinder**). This
file records the US-government attribution layer. The vendor alias-cluster +
attribution taxonomy is in companion `...-002`; the recent 2023–2025 CNI campaign
+ Splunk first-party baseline are in `...-003`.

## Attribution — recorded verbatim per Hard Rule 2 (NOT Archimedes-originated)

The advisory is authored by three US-gov bodies: the **FBI**, **CISA**, and the
**Department of Defense Cyber Crime Center (DC3)**.

- **Actor–Iran linkage — advisory language (per THN + SOC Prime relays of the CSA):**
  > "connected to the Government of Iran (GOI)"

  The joint advisory frames the actors as Iran-based and directly linked to the
  Government of Iran. The FBI's own framing (per relays): FBI "analysis and
  investigation indicate the group's activity is consistent with a cyber actor
  with Iranian state-sponsorship."

- **IRGC framing — caveat on precision:** Multiple industry references place
  Pioneer Kitten in the roster of **IRGC-attributed** Iranian groups (e.g.,
  CrowdStrike lists Pioneer Kitten among IRGC-aligned actors — see `...-002`).
  BUT the AA24-241A advisory text itself says "Government of Iran," not
  "IRGC-directed." Record the distinction: the US-gov primary asserts GOI
  linkage; the crisper IRGC attribution comes from the vendor layer. Do NOT
  harden "GOI-linked" into "IRGC-directed" on the strength of this source alone.

- **Front company — advisory names it explicitly:**
  > Iranian IT company **Danesh Novin Sahand** (company identification number
  > **14007585836**), assessed as "likely" a cover IT entity for the group's
  > malicious cyber activity.

- **HARD RULE 2 CORRECTION / NON-MERGE (flag for grader + profiler):** The task
  brief asked to verify **Aria Sepehr Ayandehsazan (ASA)** and **Danesh Novin
  Sahand** as Pioneer Kitten front companies. Verification result: **only Danesh
  Novin Sahand** is the Pioneer Kitten front (per AA24-241A). **Aria Sepehr
  Ayandehsazan (ASA)** is the mid-2024 rename of **Emennet Pasargad**, the front
  for **Cotton Sandstorm** (aka Emennet Pasargad / Haywire Kitten) — a SEPARATE
  IRGC-linked influence-operations actor, NOT Pioneer Kitten. Do NOT fold ASA
  into the Pioneer Kitten dossier. Recorded here so the profiler does not
  inherit a bad cross-walk.

## The Br0k3r / xplfinder access-broker persona

- The actors self-identify as **Br0k3r** and, as of 2024, operate under the
  handle **xplfinder** (per THN + SOC Prime + SOCRadar relays of the CSA).
- Br0k3r is the persona through which Pioneer Kitten **sells network access** on
  underground/cybercriminal marketplaces — the "access broker" side of the
  dual-track model below. Communication channels referenced: KeyBase and Twitter
  accounts (per SOCRadar relay). Specific handle infrastructure (e.g. any
  xplfinder[.]* domain) NOT cleanly retrieved this pass — held pending direct
  retrieval of the advisory IOC appendix.

## Dual-track operating model (the load-bearing behavioral fact)

Per the advisory (relays agree):

1. **State-aligned track:** high-volume network-intrusion operations against US
   and allied targets consistent with Iranian state intelligence objectives.
2. **Commercial ransomware-enabler track:** a significant share of the group's
   US-focused activity is aimed at obtaining/maintaining access that is then
   **sold or handed to ransomware affiliates** in exchange for a percentage of
   ransom proceeds. The FBI identified the actors collaborating directly with
   ransomware affiliates to enable encryption operations.

   Named ransomware affiliates (verbatim per relays): **NoEscape**,
   **RansomHouse**, and **ALPHV / BlackCat**.

## Sectors targeted (Intent-scoring-relevant — READ CAREFULLY)

- **United States:** education, finance, healthcare, and **defense** — plus
  local/municipal government entities. The advisory explicitly lists **defense**
  among US victim sectors.
- **Middle East / allied:** organizations in **Israel, Azerbaijan, and the
  United Arab Emirates**.
- **CAVEAT for later Intent scoring:** AA24-241A names the **"defense" sector**
  generically among US victims. It does NOT, in the text retrieved this pass,
  name a specific US A&D PRIME or DIB contractor by name. Whether this clears the
  THREAT-BOX evidence-minimum bar for Intent=5 (Target-Specific, which requires
  an A-grade source documenting targeting of the operator's SPECIFIC ad-prime
  profile) vs. Intent=4 (Ideology) or Intent=3 (Sector Association) is the
  profiler's call — flagged, not decided. This is the single most important open
  question for the scoring pass.

## Edge/VPN CVEs exploited (Hard Rule 3 — IDs only, no exploit detail)

Cross-corroborated across AA24-241A relays (THN, SOC Prime, SOCRadar, Tenable)
and MITRE G0117. Pioneer Kitten scans for and exploits public-facing networking
devices:

- **CVE-2019-19781** — Citrix ADC / Gateway (Netscaler)
- **CVE-2023-3519** — Citrix NetScaler ADC / Gateway RCE
- **CVE-2024-24919** — Check Point Security Gateway (info disclosure) *[the
  headline 2024 CVE in AA24-241A; note some relays mis-label this "F5 BIG-IP" —
  it is Check Point per the CISA text + NVD]*
- **CVE-2024-3400** — Palo Alto Networks PAN-OS GlobalProtect
- **CVE-2019-11510** — Pulse Secure / Ivanti Connect Secure (arbitrary file read)
- **CVE-2020-5902** — F5 BIG-IP TMUI RCE
- **CVE-2022-1388** — F5 BIG-IP iControl REST auth bypass

Tooling named (post-exploitation, for context — not exploits): AnyDesk,
Ligolo, ngrok, FRPC, Chisel, MeshCentral, ReverseSocks5, Glider Proxy, PuTTY/
Plink, TightVNC.

---

## Extraction notes

- Language: en
- Publisher bylines: FBI / CISA / DC3 (joint, no individual byline). Relays: The
  Hacker News (Ravie Lakshmanan, 2024-08-28); SOC Prime; SOCRadar; MITRE ATT&CK
  G0117 (curated).
- Article type: government joint cybersecurity advisory (primary) reconstructed
  via news/vendor relays.
- Originating primary: FBI + CISA + DC3 (AA24-241A). CISA-hosted page 403s on
  direct WebFetch (WAF — documented behavior); IC3 PDF mirror rendered as
  corrupted binary. **The verbatim attribution strings and the network-IOC
  appendix are therefore PENDING DIRECT RETRIEVAL** of a clean copy of the
  advisory (browser-side, or a non-WAF mirror). Attribution FACTS below are
  reliably corroborated across ≥3 independent relays; only the exact quotation
  marks and the raw IP/domain/hash appendix are held pending.
- Relay-vs-primary: this is an A-grade PRIMARY surfaced through B-grade RELAYS.
  The relays are NOT independent corroboration of each other (all trace to the
  one CSA); they are reconstruction aids. The grader should weight this as a
  single originating US-gov primary, not a multi-source consensus.
- Hard Rule 2: attribution recorded verbatim; GOI-linkage (advisory) kept
  distinct from IRGC-attribution (vendor layer); ASA/Cotton-Sandstorm explicitly
  NOT merged into Pioneer Kitten.
- Hard Rule 3: CVEs by ID only; no PoC/exploit content.
- Hard Rule 7: no credentials surfaced in this report.

## IOCs (ioc-extraction output)

```yaml
extraction_metadata:
  source_brief_id: cisa-fbi-dc3-aa24-241a-2024-08
  source_url: https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-241a
  extracted_at: 2026-07-14T16:42:00Z
  extracted_by: collector
  target_actor_id: null      # NET-NEW actor — no roster id assigned yet (grader/profiler will assign)
  text_word_count: 1180

indicators:
  # --- CVEs (Hard Rule 3: IDs only). Cross-corroborated across AA24-241A relays + MITRE G0117. ---
  - id: raw-cve-2024-24919
    type: cve
    value: CVE-2024-24919
    defanged_original: null
    role: exploitation
    campaign: "Pioneer Kitten edge-device access operations (AA24-241A)"
    related_malware: []
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "Check Point Security Gateway info-disclosure; headline 2024 CVE in AA24-241A"
    attribution_in_text: Pioneer Kitten
    notes: "Product = Check Point (NVD confirms); some relays mislabel as F5 BIG-IP. vuln-tracker handoff candidate."
  - id: raw-cve-2024-3400
    type: cve
    value: CVE-2024-3400
    defanged_original: null
    role: exploitation
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "Palo Alto PAN-OS GlobalProtect exploited for initial access"
    attribution_in_text: Pioneer Kitten
    notes: null
  - id: raw-cve-2023-3519
    type: cve
    value: CVE-2023-3519
    defanged_original: null
    role: exploitation
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "Citrix NetScaler ADC/Gateway RCE"
    attribution_in_text: Pioneer Kitten
    notes: null
  - id: raw-cve-2019-19781
    type: cve
    value: CVE-2019-19781
    defanged_original: null
    role: exploitation
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "Citrix ADC/Gateway (Netscaler) — long-running Pioneer Kitten access vector since 2019"
    attribution_in_text: Pioneer Kitten
    notes: null
  - id: raw-cve-2019-11510
    type: cve
    value: CVE-2019-11510
    defanged_original: null
    role: exploitation
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "Pulse Secure / Ivanti Connect Secure arbitrary file read"
    attribution_in_text: Pioneer Kitten
    notes: null
  - id: raw-cve-2020-5902
    type: cve
    value: CVE-2020-5902
    defanged_original: null
    role: exploitation
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "F5 BIG-IP TMUI RCE"
    attribution_in_text: Pioneer Kitten
    notes: null
  - id: raw-cve-2022-1388
    type: cve
    value: CVE-2022-1388
    defanged_original: null
    role: exploitation
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "F5 BIG-IP iControl REST auth bypass"
    attribution_in_text: Pioneer Kitten
    notes: null

  # --- Persona handles (attribution-context indicators, type=other). ---
  - id: raw-persona-br0k3r
    type: other
    type_detail: actor_persona_handle
    value: "Br0k3r"
    defanged_original: null
    role: c2         # access-broker sales persona
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "Self-identified access-broker persona through which Pioneer Kitten sells network access"
    attribution_in_text: Pioneer Kitten
    notes: "Persona, not a network IOC. Recorded for hunt/attribution context."
  - id: raw-persona-xplfinder
    type: other
    type_detail: actor_persona_handle
    value: "xplfinder"
    defanged_original: null
    role: c2
    source_brief: cisa-fbi-dc3-aa24-241a-2024-08
    context_excerpt: "2024 marketplace handle used by the Br0k3r persona"
    attribution_in_text: Pioneer Kitten
    notes: "Persona handle. Any xplfinder[.]* domain infra pending direct retrieval of advisory appendix."

  # --- Front company (attribution-context, NOT a network IOC). ---
  - type: note
    value: "Front company: Danesh Novin Sahand (Iranian IT company, company ID 14007585836) assessed 'likely' a cover entity for Pioneer Kitten per AA24-241A. Recorded as attribution context. DISTINCT from Aria Sepehr Ayandehsazan (ASA) = Emennet Pasargad rename = Cotton Sandstorm front — NOT Pioneer Kitten (Hard Rule 2 non-merge)."
    role: attribution_context

  # --- Network IOC appendix (IPs/domains/hashes/emails) held PENDING. ---
  - type: note
    value: "AA24-241A ships a network-IOC appendix (IPs, domains, hashes, email accounts). It was NOT cleanly retrievable this pass — CISA-hosted page 403s (WAF); IC3 PDF mirror rendered as corrupted binary; three relay articles (THN/SOC Prime/SOCRadar) reproduce the CVEs/personas/tools but NOT the atomic network indicators. Network IOC VALUES are therefore PENDING DIRECT RETRIEVAL of a clean advisory copy — do NOT fabricate or fold guessed IPs/domains. Companion file ...-003 records the FortiGuard Lemon Sandstorm campaign IOC status separately."
    role: pending_retrieval

attribution_claims:
  - claimant: "FBI / CISA / DC3 (AA24-241A joint CSA)"
    claim: "Pioneer Kitten is an Iran-based cyber actor connected to the Government of Iran (GOI), using Danesh Novin Sahand as a likely cover company, enabling ransomware attacks on US organizations"
    nation_named: Iran
    service_named: "Government of Iran (GOI) — IRGC NOT specified in advisory text"
    actor_named: Pioneer Kitten
    confidence_language: "connected to the Government of Iran; activity consistent with Iranian state-sponsorship (FBI); front company 'likely' a cover"
    requires_grading: true
  - claimant: "FBI (per AA24-241A)"
    claim: "Pioneer Kitten collaborates directly with ransomware affiliates NoEscape, RansomHouse, and ALPHV/BlackCat, selling/handing network access for a share of ransom proceeds via the Br0k3r/xplfinder persona"
    linkage_type: ransomware_affiliate_collaboration
    confidence_language: "FBI identified these actors collaborating directly"
    requires_grading: true
```
</content>
</invoke>
