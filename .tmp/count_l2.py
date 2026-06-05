import re
from pathlib import Path

p = Path(r"C:\Users\rtske\Projects\archimedes\threats\briefs\2026-05-31-afternoon.md")
text = p.read_text(encoding="utf-8")

# Layer 2 starts at "## 📣 Discord Summary"
marker = "## 📣 Discord Summary"
idx = text.find(marker)
l2 = text[idx:].strip()

# Discord doesn't render frontmatter; we care about everything from the heading down,
# but the librarian extracts CONTENT under the heading (typically without the heading itself).
# Per spec, the heading IS included in the extracted text? Re-check: spec says
# "extracts the content under `## 📣 Discord Summary`" — content under, not including heading.
# So char count for Discord's 2000-char limit = content after heading.
content_after_heading = text[idx + len(marker):].strip()

print(f"Layer 2 chars (with heading): {len(l2)}")
print(f"Layer 2 chars (content only, no heading): {len(content_after_heading)}")
# word count
words = re.findall(r"\S+", content_after_heading)
print(f"Layer 2 word count (content only): {len(words)}")

# Full brief body word count (excluding frontmatter)
fm_end = text.find("---", 4) + 3
body = text[fm_end:].strip()
# strip the Layer 2 for Layer 1 word count
layer1 = text[fm_end:idx].strip()
l1_words = re.findall(r"\S+", layer1)
print(f"Layer 1 word count (excluding Layer 2): {len(l1_words)}")
print(f"Full body word count (Layer 1 + Layer 2): {len(re.findall(r'\S+', body))}")
