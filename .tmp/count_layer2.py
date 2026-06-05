#!/usr/bin/env python3
"""Measure Layer 2 Discord Summary char/word count for the 2026-06-02 morning brief."""
import re
from pathlib import Path

brief = Path(r"C:\Users\rtske\Projects\archimedes\threats\briefs\2026-06-02-morning.md")
text = brief.read_text(encoding="utf-8")

marker = "## 📣 Discord Summary"
idx = text.find(marker)
if idx < 0:
    raise SystemExit("Layer 2 marker not found")

layer2 = text[idx:].rstrip() + "\n"

chars = len(layer2)
words = len(layer2.split())

body_no_header = "\n".join(layer2.splitlines()[1:]).strip() + "\n"
chars_no_header = len(body_no_header)
words_no_header = len(body_no_header.split())

print(f"Full Layer 2 section (with header):    chars={chars}  words={words}")
print(f"Body only (header stripped):           chars={chars_no_header}  words={words_no_header}")
print(f"Discord hard cap: 2000  |  Working ceiling: 1900")
print(f"Status (full):       {'PASS' if chars <= 1900 else 'FAIL'} (margin {1900-chars:+d})")
print(f"Status (body only):  {'PASS' if chars_no_header <= 1900 else 'FAIL'} (margin {1900-chars_no_header:+d})")

# Also Layer 1 word count
fm_end = text.find("\n---\n", 4)
if fm_end == -1:
    raise SystemExit("Frontmatter end not found")
layer1 = text[fm_end+5:idx]
# Strip code blocks and markdown
l1_stripped = re.sub(r"```[\s\S]*?```", "", layer1)
l1_stripped = re.sub(r"\(https?://[^)]+\)", "", l1_stripped)
l1_stripped = re.sub(r"[*_`#\[\]]", " ", l1_stripped)
l1_words = [w for w in re.split(r"\s+", l1_stripped) if w]
print()
print(f"Layer 1 word count: {len(l1_words)}")
print(f"Layer 1 word band 400-800: {'PASS' if 400 <= len(l1_words) <= 800 else 'FAIL'}")
