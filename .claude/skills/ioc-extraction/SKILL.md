---
name: ioc-extraction
description: Use when extracting Indicators of Compromise (IOCs) from unstructured text — threat reports, CVE advisories, vendor blogs, news articles, tweets, forum posts, Splunk search results, or any source containing technical indicators. Invoke when the collector subagent ingests new raw signal, when the actor-profiler needs to pull IOCs from fresh reporting into an actor's iocs.md, when vuln-tracker parses CVE writeups for affected systems, or when /ioc-hunt needs to normalize a user-supplied indicator. Handles defanged notation (example[.]com, hxxp://), filters benign/reference mentions, preserves context (campaign, role, source), and outputs entries matching the Archimedes iocs.yaml schema.
---

# IOC Extraction Skill

## Purpose

This skill parses unstructured text and produces structured IOC entries matching the Archimedes `iocs.yaml` schema. It handles defanged notation, filters obvious false positives, preserves context, and flags attribution claims that need separate admiralty grading.

**This skill does not grade. It only extracts.** Attribution of an IOC to an actor is a separate claim that requires `admiralty-grading`.

## Prerequisites

Before invoking, gather:

1. **The source text** — full article/advisory/post content, not just a URL
2. **The source_brief_id** — matches an entry in the findings index (e.g., `trellix-2026-02`)
3. **Context about why you're extracting** — new campaign reporting, routine monitoring, ad-hoc hunt query
4. **Target actor_id, if known** — only when extracting for a specific actor's `iocs.yaml`

If extracting for general raw signal (no specific actor yet), set `actor_id: null` — the grader will resolve attribution later.

## IOC types covered

| Type | Schema tag | Example |
|---|---|---|
| IPv4 | `ipv4` | `192.0.2.50` |
| IPv6 | `ipv6` | `2001:db8::1` |
| Domain | `domain` | `evil-corp.example` |
| URL | `url` | `https://evil-corp.example/payload.bin` |
| File hash — MD5 | `hash_md5` | `5d41402abc4b2a76b9719d911017c592` |
| File hash — SHA-1 | `hash_sha1` | `aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d` |
| File hash — SHA-256 | `hash_sha256` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4...` |
| Email address | `email` | `phish@evil-corp.example` |
| CVE | `cve` | `CVE-2024-1234` |
| File path | `file_path` | `C:\Users\Public\stage.exe` |
| Registry key | `registry_key` | `HKCU\Software\Microsoft\...` |
| Mutex | `mutex` | `Global\MaliciousMutex` |
| Crypto wallet | `crypto_wallet` | `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` |
| YARA rule name | `yara_rule` | `APT28_Covenant_Grunt` |
| JA3 fingerprint | `ja3` | `ce5f3254611a8c095a3d821d44539877` |
| JA3S fingerprint | `ja3s` | `b742b407517bac9536a77a7b0fee28e9` |
| JARM fingerprint | `jarm` | `27d40d40d29d40d1dc42d43d00041d...` |
| User-agent | `user_agent` | `Mozilla/5.0 (compatible; ...)` |
| TOR onion | `onion` | `examplehiddenservice7xyz.onion` |
| Scheduled task | `scheduled_task` | `\Microsoft\Windows\Update\ServiceCheck` |

For types not in this list, add `type: other` and record the observed type in `type_detail`.

## Procedure

### Step 1 — Normalize defanged notation

Threat intelligence routinely publishes IOCs in "defanged" form to prevent accidental navigation or email filter triggers. Recognize and normalize these before extraction:

| Defanged | Normalized |
|---|---|
| `evil[.]com`, `evil(.)com`, `evil{.}com` | `evil.com` |
| `evil .com` (space before dot) | `evil.com` |
| `hxxp://`, `hXXp://`, `h__p://` | `http://` |
| `hxxps://`, `hXXps://` | `https://` |
| `1[.]2[.]3[.]4`, `1(.)2(.)3(.)4` | `1.2.3.4` |
| `user[@]domain.com`, `user (at) domain.com` | `user@domain.com` |
| `192[.]0[.]2[.]50[:]8080` | `192.0.2.50:8080` |

**Record the original form** in `defanged_original` field so the human-readable `iocs.md` can preserve it if needed.

### Step 2 — Extract candidate IOCs

Scan the text for patterns matching each IOC type. Use these regex patterns as guidelines — apply judgment on edge cases:

- **IPv4**: `\b(?:\d{1,3}\.){3}\d{1,3}\b` — then validate each octet is 0-255
- **IPv6**: standard RFC 4291 notation
- **Domain**: `\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b` — excludes trailing punctuation
- **URL**: starts with `http://`, `https://`, `ftp://`, or `file://`
- **Hashes**: hex strings of exactly 32 (MD5), 40 (SHA-1), or 64 (SHA-256) characters
- **CVE**: `CVE-\d{4}-\d{4,7}` (case-insensitive)
- **Email**: `[\w.+-]+@[\w-]+\.[\w.-]+`
- **Registry key**: starts with `HKEY_` or `HKCU\`, `HKLM\`, `HKCR\`, `HKU\`, `HKCC\`
- **File path (Windows)**: matches `[A-Z]:\\` or `\\\\[\w-]+\\`
- **File path (Unix)**: starts with `/`, contains typical directories
- **Onion address**: `[a-z2-7]{16}\.onion` (v2) or `[a-z2-7]{56}\.onion` (v3)
- **Bitcoin address**: starts with `1`, `3`, or `bc1` and is 26-42 characters
- **JA3/JA3S**: 32-char hex string
- **JARM**: 62-char hex/numeric string

### Step 3 — Apply the benign filter

Many IOC-shaped strings in an article are NOT malicious indicators. Filter out:

**Benign domains and IPs:**
- Publisher's own domain (e.g., if extracting from a Mandiant article, `mandiant.com` is not an IOC)
- CISA, Microsoft, vendor reference sites (`cisa.gov`, `microsoft.com`, `github.com`, `mitre.org`, `virustotal.com`, etc.)
- Code repositories cited as references (`github.com/example-org/example-repo`)
- RFC-documentation IPs (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` — TEST-NET ranges)
- Private/internal IPs (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) — these are observational context, not IOCs
- Loopback (`127.0.0.0/8`) and link-local (`169.254.0.0/16`)

**Benign URLs:**
- Links to the article being analyzed ("read more at..." citations)
- Links to MITRE ATT&CK technique pages (`attack.mitre.org/techniques/...`)
- Links to NVD, CVE pages
- Social media profile links

**Benign hashes:**
- Hashes of known-good binaries (if available via NSRL/VT reputation check — flag for enrichment, don't reject outright)

**When in doubt, do not filter.** Over-extraction is correctable; missing IOCs is not. Prefer `role: ambiguous` over dropping the indicator.

### Step 4 — Determine context and role

For each surviving candidate, read the surrounding text (2-3 sentences before and after) to determine:

**Role** — what the IOC does in the campaign:
- `delivery` — initial payload delivery (phishing domain, maldoc URL)
- `staging` — hosts second-stage payloads
- `c2` — command and control infrastructure
- `exfil` — exfiltration destination
- `spray` — password spray / credential attack origin
- `persistence` — registry key, scheduled task, service
- `lateral` — lateral movement indicator
- `historical` — referenced as past activity, not currently active
- `ambiguous` — role unclear from context

**First seen / Last seen** — if dates are mentioned in the text, capture them. Use YYYY-MM format (year and month). If only year is mentioned, use YYYY.

**Campaign** — if the text names a campaign (e.g., "Operation RoundPress", "CVE-2026-21509 Wave"), capture it verbatim.

**Related malware** — malware family names associated with the IOC (e.g., `[SimpleLoader, CovenantGrunt]`).

**Resolved IP** (for domains) — if the text explicitly maps the domain to an IP, capture it. Do not do DNS resolution from this skill.

### Step 5 — Flag attribution claims separately

If the text claims an IOC is attributed to a specific threat actor, extract the claim as a separate output field — **do not bake attribution into the IOC's type/value**.

Attribution claims require `admiralty-grading`. This skill surfaces the claim; grading happens downstream.

Attribution claim format:

```yaml
attribution_claims:
  - ioc_id: apt28-domain-freefoodaid
    claimed_actor: APT28
    claimed_by_source: trellix-2026-02
    attribution_confidence_in_source: high  # as described in text
    requires_grading: true
```

### Step 6 — Assign stable IDs

IOC IDs follow the pattern: `<actor_id_or_prefix>-<type>-<slug>`

Examples:
- `apt28-domain-freefoodaid` (actor-specific)
- `apt28-ip-91-149-253-118` (IP with dots as dashes)
- `apt28-hash-e3b0c44298fc` (hash truncated to 12 chars)
- `raw-domain-newthreatpossible` (no actor yet — `raw` prefix)

**Rules:**
- Lowercase
- Dots in IPs become dashes
- Slashes in registry keys become dashes
- Hashes truncate to first 12 chars (full value preserved in `value` field)
- IDs must be unique within a file; check before assigning

### Step 7 — Produce the output

Return a YAML block per the schema below. One entry per IOC.

## Output format

```yaml
extraction_metadata:
  source_brief_id: trellix-2026-02
  source_url: https://www.trellix.com/blogs/research/2026-02-15-cve-2026-21509-wave/
  extracted_at: 2026-04-23T15:12:00Z
  extracted_by: collector
  target_actor_id: "006"  # or null for general raw signal
  text_word_count: 2843

indicators:
  - id: apt28-domain-freefoodaid
    type: domain
    value: freefoodaid.com
    defanged_original: "freefoodaid[.]com"
    resolved_ip: 159.253.120.2
    first_seen: 2026-01
    last_seen: 2026-02
    role: staging
    campaign: "CVE-2026-21509 Wave"
    related_malware: [SimpleLoader]
    source_brief: trellix-2026-02
    context_excerpt: >
      "Trellix researchers observed freefoodaid[.]com serving stage-2 payloads
      during January and February 2026."
    attribution_in_text: APT28
    notes: null

  - id: apt28-ip-91-149-253-118
    type: ipv4
    value: 91.149.253.118
    defanged_original: null
    first_seen: 2024-08
    last_seen: 2024-09
    role: spray
    campaign: null
    source_brief: nsa-cisa-2024-08
    context_excerpt: "Used for password spray against M365 tenants"
    attribution_in_text: APT28
    notes: null

attribution_claims:
  - claimed_actor: APT28
    ioc_ids:
      - apt28-domain-freefoodaid
      - apt28-ip-91-149-253-118
    claimed_by_source: trellix-2026-02
    attribution_confidence_in_source: high
    requires_grading: true

benign_filtered:
  - value: cisa.gov
    reason: reference_site
  - value: attack.mitre.org
    reason: reference_site
  - value: 192.0.2.0
    reason: rfc5737_documentation_range

extraction_warnings:
  - type: ambiguous_role
    ioc_id: apt28-ip-84-32-188-31
    detail: "Role not clearly stated in text — assigned 'ambiguous'; grader should confirm"
```

**All fields required.** Nulls must be explicit. Empty lists for empty collections, not omitted keys.

## Failure modes

Return a halt signal (not an extraction) when:

1. **Source text is too short to contain context** (<50 words) — request full text
2. **Source text appears to be table-of-contents or link-list** without actual content — request the body
3. **IOCs extracted would exceed 200 per document** — likely a data dump, not a threat report. Halt and request collector re-scope.
4. **Defanged notation is inconsistent within the document** (some defanged, some not) — flag for human review; don't silently normalize
5. **Critical metadata missing** — no source_brief_id, no source URL. Request from caller.

Halt format:

```yaml
status: halt
reason: source_text_too_short
detail: "Provided text is 23 words; appears to be abstract only. Request full article body."
action_requested: "Re-fetch full article content"
```

## Worked examples

### Example 1 — Standard extraction with defanged notation

**Input text:**
> "Trellix researchers observed APT28 infrastructure at freefoodaid[.]com (resolving to 159[.]253[.]120[.]2) serving stage-2 payloads during January and February 2026. The campaign also used hxxps://wellnesscaremed[.]com/doc.rtf as the initial delivery vector."

**Process:**
- Normalize: `freefoodaid[.]com` → `freefoodaid.com`; `159[.]253[.]120[.]2` → `159.253.120.2`; `hxxps://wellnesscaremed[.]com/doc.rtf` → `https://wellnesscaremed.com/doc.rtf`
- Extract: 2 domains, 1 IP, 1 URL
- Context: "serving stage-2 payloads" → `role: staging` for freefoodaid.com; "initial delivery vector" → `role: delivery` for wellnesscaremed.com URL
- Attribution: "APT28 infrastructure" — flag as claim requiring grading

### Example 2 — Benign filter at work

**Input text:**
> "For detection logic, see the MITRE ATT&CK page at https://attack.mitre.org/techniques/T1059/. CISA's advisory is at https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-123a. The malicious domain observed was badactor.example."

**Process:**
- Extract: `attack.mitre.org`, `www.cisa.gov`, `badactor.example`
- Benign filter: MITRE and CISA are reference sites → filter out
- Surviving IOCs: `badactor.example` only
- Record filtered items in `benign_filtered` for audit

### Example 3 — Attribution embedded, don't bake in

**WRONG approach:**
```yaml
- id: apt28-domain-evil
  type: domain
  value: evil.com
  actor: APT28  # ← don't do this
```

**RIGHT approach:**
```yaml
- id: apt28-domain-evil
  type: domain
  value: evil.com
  attribution_in_text: APT28  # record the claim

attribution_claims:
  - claimed_actor: APT28
    ioc_ids: [apt28-domain-evil]
    claimed_by_source: mandiant-2026-03
    requires_grading: true
```

Attribution is a separate claim that requires admiralty grading. The IOC entry records the claim-in-text, but actual assertion lives in `attribution_claims`.

### Example 4 — Ambiguous role, don't force a choice

**Input text:**
> "Among the indicators provided: 185.82.126.114"

No context about what the IP does. Don't guess.

```yaml
- id: raw-ip-185-82-126-114
  type: ipv4
  value: 185.82.126.114
  role: ambiguous
  context_excerpt: "Listed among indicators without role context"
```

Grader will enrich later if context becomes available.

## Interaction with other skills

- `admiralty-grading` consumes the `attribution_claims` array to grade each attribution separately
- The `_master-index.yaml` regeneration script (`scripts/regenerate_ioc_index.py`) consumes the schema-compliant `indicators` array
- `actor-profiler` takes the extracted IOCs and merges them into `threats/threat-actors/<actor>/iocs.yaml`

## References

- `references/ioc-patterns.md` — detailed regex patterns and edge cases for each IOC type (load on demand)
- `threats/threat-actors/APT28/iocs.yaml` — canonical schema example
- `scripts/regenerate_ioc_index.py` — downstream consumer that validates schema
