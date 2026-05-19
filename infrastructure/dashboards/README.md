# infrastructure/dashboards/

Versioned reference copies of Splunk Dashboard Studio dashboards. The dashboards themselves live inside Splunk; these files are diff-able snapshots so changes are reviewable in git.

## Files

- `defenseclaw-archimedes-operations-center.json` — the two-tab dashboard (DefenseClaw tab + Archimedes tab) on Frank's Splunk. Source-editor-pasteable JSON.

## How to update Splunk from this file

1. Open the dashboard in Splunk Web
2. Click **⋮ menu** (top right) → **Edit Dashboard**
3. Click **Source** to open the JSON view
4. Select all (Ctrl+A), paste the file contents
5. Click **Save**

## How to update this file from Splunk

Same process in reverse — copy from Splunk's Source editor, paste into this file, commit.

## Dark-theme readability — 2026-05-19 fix

The dashboard reads correctly on a dark background because the top-level JSON now declares:

```json
"theme": "enterprise.dark"
```

Splunk Dashboard Studio defaults to `enterprise.light` when no theme is set. A dashboard with dark backgrounds (`#080D12` / `#0F172A` / `#1E293B`) under the light theme produces dark text — the original symptom. Setting `theme: "enterprise.dark"` flips all the chrome (panel titles, table cells, pie/legend labels, axis labels) to light text on dark backgrounds.

### Properties Splunk Dashboard Studio actually controls

Per-viz `options` only affect things rendered INSIDE the visualization:

- `backgroundColor` ✅
- `majorColor`, `majorFontSize` ✅ (singlevalue)
- `seriesColors` ✅ (pie / column / bar / line)
- `headerBackgroundColor`, `rowBackgroundColorOdd`, `rowBackgroundColorEven` ✅ (table)
- `legendDisplay`, `labelDisplay`, `stackMode`, `orientation` ✅
- `fillColor`, `strokeColor` ✅ (rectangle)
- `fontColor` ✅ (markdown only — inline CSS in the rendered HTML)

Properties controlling **panel chrome** (panel titles, axis label text, table cell text, legend label text) are NOT exposed per-viz. They're driven by the dashboard theme. To override them individually, you'd need custom CSS via a Splunk app — out of scope for a single dashboard file.

### Things that were tried but don't actually work (lesson learned 2026-05-19)

A previous version of this file added the following per-viz options to brighten text. **Splunk silently ignores them** — they're not in the Dashboard Studio schema. Removed in this version:

- `titleColor`, `subtitleColor`, `unitColor` on singlevalue
- `headerColor`, `rowColor` on table
- `legendLabelColor`, `labelColor` on pie
- `axisLabelColorX/Y`, `axisTitleColorX/Y`, `legendLabelColor` on column / bar

If those names ever become real Splunk options, they can be re-added — but the `theme` property is the actual lever today.

## Theme value compatibility

- `enterprise.dark` — current Splunk Dashboard Studio (9.x+)
- `enterprise.light` — default when `theme` is absent
- If your Splunk parses neither: try the plain values `"dark"` / `"light"` (older builds) or check Splunk's theme dropdown in the UI

## Background palette (unchanged)

| Element | Color | Notes |
|---|---|---|
| Layout (outer) | `#080D12` | Near-black |
| Panel backgrounds | `#0F172A` | Dark slate |
| Header bands + table-header cells | `#1E293B` | Mid slate |
| Table row alternating (even) | `#0F172A` | Matches panel |
| Table row alternating (odd) | `#1E293B` | Matches header band |

## Accent color palette (unchanged)

| Use | Color |
|---|---|
| Title (Archimedes tab) | `#FBBF24` (gold) |
| Title (DefenseClaw tab) | `#00C7EB` (cyan) |
| Subtitle | `#CBD5E1` (slate-300) |
| Singlevalue major numbers | varies — `#E2E8F0` neutral / `#22D3EE` cyan / `#22C55E` green / `#F97316` orange |
| Pie / column series | 8-color rotation: cyan / gold / green / orange / purple / pink / blue / red |
| Severity pie (DefenseClaw) | red / orange / yellow / green / blue (P1→info) |
