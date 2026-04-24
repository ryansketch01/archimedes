# IOC Patterns Reference

> **On-demand reference.** Loaded when the collector encounters an unfamiliar IOC type, needs to handle an unusual defanging pattern, or needs to validate an edge case.
> For routine extraction, the patterns in `SKILL.md` Step 2 are sufficient.

---

## Defanging notation — extended reference

Threat intel published by different vendors uses different defanging conventions. Normalize all of these:

### Domain/URL defanging
| Variant | Normalized |
|---|---|
| `evil[.]com` | `evil.com` |
| `evil(.)com` | `evil.com` |
| `evil{.}com` | `evil.com` |
| `evil[dot]com` | `evil.com` |
| `evil DOT com` | `evil.com` |
| `evil .com` (whitespace) | `evil.com` |
| `e v i l . c o m` (letter-spaced) | `evil.com` — only if unambiguous |
| `evil[.]c[o]m` (partial defang) | `evil.com` |

### Scheme defanging
| Variant | Normalized |
|---|---|
| `hxxp://` | `http://` |
| `hXXp://` | `http://` |
| `h__p://` | `http://` |
| `h**p://` | `http://` |
| `httpx://` | `http://` (non-standard but seen) |
| `hxxps://` | `https://` |
| `hXXps://` | `https://` |
| `fxp://` | `ftp://` |

### IP defanging
| Variant | Normalized |
|---|---|
| `1[.]2[.]3[.]4` | `1.2.3.4` |
| `1(.)2(.)3(.)4` | `1.2.3.4` |
| `1[dot]2[dot]3[dot]4` | `1.2.3.4` |
| `192[.]0[.]2[.]50[:]8080` | `192.0.2.50:8080` |

### Email defanging
| Variant | Normalized |
|---|---|
| `user[@]domain.com` | `user@domain.com` |
| `user (at) domain.com` | `user@domain.com` |
| `user AT domain DOT com` | `user@domain.com` |
| `user[at]domain[dot]com` | `user@domain.com` |

### DO NOT normalize
- Deliberate spelling variants that could be typosquatting IOCs themselves (e.g., `rnicrosoft.com` with `rn` instead of `m` is a real indicator, not a defang)
- Unicode homoglyph domains (e.g., `аpple.com` with Cyrillic `а`) — flag for human review

---

## IPv4 validation rules

A valid IPv4 matches `^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$`

**Special ranges to always filter:**

| Range | Purpose | Action |
|---|---|---|
| `0.0.0.0/8` | Reserved | Filter |
| `10.0.0.0/8` | RFC 1918 private | Filter (unless Splunk internal context) |
| `100.64.0.0/10` | CGNAT | Filter |
| `127.0.0.0/8` | Loopback | Filter |
| `169.254.0.0/16` | Link-local | Filter |
| `172.16.0.0/12` | RFC 1918 private | Filter (unless Splunk internal context) |
| `192.0.0.0/24` | IANA | Filter |
| `192.0.2.0/24` | RFC 5737 TEST-NET-1 | Filter (documentation only) |
| `192.168.0.0/16` | RFC 1918 private | Filter (unless Splunk internal context) |
| `198.18.0.0/15` | Benchmark testing | Filter |
| `198.51.100.0/24` | RFC 5737 TEST-NET-2 | Filter |
| `203.0.113.0/24` | RFC 5737 TEST-NET-3 | Filter |
| `224.0.0.0/4` | Multicast | Filter |
| `240.0.0.0/4` | Reserved | Filter |
| `255.255.255.255` | Broadcast | Filter |

**Splunk internal context exception:** If the extraction is from a Splunk search result or first-party telemetry, private-range IPs CAN be IOCs (e.g., internal lateral movement). Only filter private ranges when extracting from external reporting.

---

## Domain validation rules

A valid domain has:
- At least two labels separated by dots
- Each label 1-63 characters
- Labels contain letters, digits, and hyphens; cannot start or end with hyphen
- TLD is at least 2 characters, all letters (though there are exceptions like `.xn--...` IDN)
- Total length ≤253 characters

**Common false positives to filter:**

- Versioned file names (`jquery-3.5.1.min.js` contains dots but isn't a domain)
- IP addresses (already handled by IP extraction; don't double-extract)
- File extensions in text (`config.ini` could match a domain pattern but obviously isn't)
- Sentence-ending periods (`Check example.com.` — extract `example.com`, not `example.com.`)

**Disambiguation heuristic:**
If a candidate ends with a common file extension (`.exe`, `.dll`, `.js`, `.html`, `.pdf`, `.doc`, `.xlsx`, `.zip`, etc.), it's probably a file, not a domain. Unless it appears in a URL context (with scheme or path).

**Common legitimate domains to always filter:**

- `*.cisa.gov`, `*.mitre.org`, `*.nist.gov`, `*.dhs.gov`
- `*.microsoft.com`, `*.google.com`, `*.apple.com` (unless specifically called out as IOC)
- `*.github.com`, `*.gitlab.com`, `*.bitbucket.org`
- `*.virustotal.com`, `*.any.run`, `*.hybrid-analysis.com`
- `*.mandiant.com`, `*.crowdstrike.com`, `*.paloaltonetworks.com` (publisher sites)
- `*.twitter.com`, `*.x.com`, `*.linkedin.com`
- `attack.mitre.org`, `nvd.nist.gov`, `cve.mitre.org`

**Override:** If the text explicitly states a well-known domain is acting malicious (e.g., "attacker hosted payload on drive.google.com/..."), extract it. Context matters.

---

## Hash validation rules

| Hash | Length | Character set |
|---|---|---|
| MD5 | 32 hex chars | `[a-fA-F0-9]` |
| SHA-1 | 40 hex chars | `[a-fA-F0-9]` |
| SHA-256 | 64 hex chars | `[a-fA-F0-9]` |
| SHA-512 | 128 hex chars | `[a-fA-F0-9]` |
| ssdeep | `N:XXXX:YYYY` format | mixed |
| imphash | 32 hex (looks like MD5) | `[a-fA-F0-9]` |
| TLSH | 70 hex chars (typically) | `[a-fA-F0-9]` + `T1` prefix |

**Disambiguation:**
- 32-char hex could be MD5 OR imphash. Context determines — "imphash: XXXX" is imphash, unqualified is MD5.
- Git commit SHAs look like SHA-1 (40 hex) but aren't file hashes. If the text mentions git/commit/repo, skip.
- UUIDs look similar but have dashes — don't confuse.

**Store hashes lowercase** regardless of how they appear in source text. Normalization helps deduplication.

---

## URL handling

### Normalization rules
1. Lowercase the scheme and host
2. Keep path case-sensitive (it often is semantically)
3. Remove default ports (`:80` for http, `:443` for https)
4. Preserve query strings — they may be IOC-relevant
5. Strip fragments (`#anchor`) unless specifically meaningful

### Common false positive URLs
- "Read more at..." citations
- Vendor reference pages
- CVE/NVD pages
- Archive.org snapshots (but DO extract the original URL inside the archive link)

### URL vs domain+path decision
- If the text says "the attacker registered evil.com," that's a domain IOC
- If the text says "the maldoc downloaded https://evil.com/stage2.bin," that's a URL IOC
- Prefer URL over domain when path information is material

---

## Edge cases — when NOT to extract

### Version-like strings
`v1.2.3.4`, `2.0.1.4` — if preceded by "version", "v", or in a context of software versioning, skip.

### Timestamps disguised as IPs
`2026.04.23.14` — if the numbers are dates or times, skip.

### IOC lookalikes in prose
"Attacker targeted over 4.5.6.7 million users" — `4.5.6.7` here is not an IP, it's a number with periods. Context matters.

### CVE pattern in documentation
`CVE-XXXX-YYYY` — if XXXX-YYYY are placeholders (not real digits), skip. Real CVEs always have digits.

### Hash-looking strings
A 64-char hex string could be a SHA-256 OR a JARM signature OR a private key fingerprint. Context:
- "hash" or "SHA-256" or "IOC" → SHA-256
- "JARM" → JARM
- "fingerprint" (without SHA-256 qualifier) → could be JARM or SSL cert fingerprint
- "ed25519" or "RSA" → SSH/TLS key, not file hash

---

## Output validation checklist

Before returning extraction results, verify:

- [ ] All IOC IDs are unique within the output
- [ ] All required fields are present (null where empty, not omitted)
- [ ] Defanged values have `defanged_original` preserved
- [ ] Filtered items are recorded in `benign_filtered`
- [ ] Attribution claims are in `attribution_claims`, not baked into IOC entries
- [ ] Warnings are in `extraction_warnings` array (empty if none)
- [ ] Dates use YYYY-MM or YYYY format, not full dates
- [ ] Source brief ID matches a real entry in the findings index
- [ ] Hashes are lowercase
- [ ] Domains have trailing periods stripped

---

## Interaction with other skills

When extracted IOCs are about to be committed to an actor's `iocs.yaml`:

1. The actor-profiler invokes this skill for extraction
2. The `attribution_claims` array passes to `admiralty-grading`
3. Graded claims return with digraphs
4. Only claims meeting the B2 threshold get merged into actor profile
5. All IOCs, regardless of attribution confidence, go to `threats/raw-signal/` first
6. Librarian runs `scripts/regenerate-ioc-index.py` to update `_master-index.yaml`

This means the IOC extraction skill should NEVER claim attribution itself — only surface the claim for grading.

---

*Last updated: Session 2 scaffold*
*Canonical schema: `threats/threat-actors/APT28/iocs.yaml`*
