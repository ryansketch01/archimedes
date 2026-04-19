# LEGAL-POLICY-CHANGELOG.md

Version history for `doctrine/LEGAL-POLICY.md`. Every change to the legal policy must be recorded here before the policy file itself is modified.

---

## v1.0.0 — 2026-04-18 — Session 1 scaffold

**Type:** Initial

**Summary:** Migrated from C3PO legal policy with 8 operational additions for agent enforcement.

**Changes:**
- Carried forward: governing laws, authorization tiers, SpiderFoot passive-only, dark web guardrails, data handling, responsible disclosure
- Added: Prohibited query patterns (enforced at every subagent)
- Added: Authorized targets mechanism (`infrastructure/authorized-targets.yaml`)
- Added: Expanded data handling table for agent-specific cases
- Added: ITAR/EAR section
- Added: Attribution standards
- Added: Policy violation handling with logging
- Added: GDPR operational rules
- Added: Enforcement architecture

**Review date:** 2027-04-18

---

*Format for future entries:*

```
## vX.Y.Z — YYYY-MM-DD — Brief title

**Type:** Addition | Removal | Modification | Clarification
**Summary:** One paragraph
**Changes:** Bullet list
**Approved by:** Ryan
**Review date:** YYYY-MM-DD
```
