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

## Readability palette (applied 2026-05-19)

Splunk Dashboard Studio's default dark-theme text colors are too dim against `#080D12` / `#0F172A` panel backgrounds. The following overrides are applied across the dashboard:

| Use | Color | Notes |
|---|---|---|
| Panel titles ("Pipeline Health" etc.) | `#F1F5F9` (slate-100) | `titleColor` property |
| Body text (table rows, pie labels, legend) | `#E2E8F0` (slate-200) | `rowColor`, `legendLabelColor`, `labelColor` |
| Secondary text (subtitles, axis labels) | `#CBD5E1` (slate-300) | `subtitleColor`, `axisLabelColorX/Y` |
| Brightest accent (axis titles, table headers) | `#F1F5F9` | `axisTitleColorX/Y`, `headerColor` |
| Big single-value numbers | varies (existing `majorColor` retained) | Pipeline Health green, FLASH orange, etc. |

Background palette unchanged: `#080D12` (outer), `#0F172A` (panels), `#1E293B` (header bands + table-header backgrounds + odd-row backgrounds), `#0F172A` (even-row backgrounds for alternating contrast).

## Properties that may not render on older Splunk Dashboard Studio versions

If any of these properties show as warnings in the Source editor, comment them out or remove them — they're safe to drop without breaking the dashboard:

- `headerColor`, `rowColor` on tables — verified on Dashboard Studio 9.1+
- `legendLabelColor`, `labelColor` on pies — verified on Dashboard Studio 9.1+
- `axisLabelColorX/Y`, `axisTitleColorX/Y`, `legendLabelColor` on columns/bars — verified on Dashboard Studio 9.1+
- `subtitleColor`, `unitColor` on singlevalue — verified on Dashboard Studio 9.1+

If your Splunk version is older and these don't take, the dashboard will still render — just without the readability fix on those specific elements. Drop the unsupported keys and the rest still works.
