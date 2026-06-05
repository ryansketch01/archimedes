import io, sys, pathlib

p = pathlib.Path(r"C:\Users\rtske\Projects\archimedes\threats\briefs\2026-05-26-morning.md")
text = p.read_text(encoding="utf-8")
# Find the Discord Summary section
idx = text.find("## 📣 Discord Summary")
if idx == -1:
    print("Discord Summary not found")
    sys.exit(1)
section = text[idx:]
# Count chars and words
chars = len(section)
words = len(section.split())
print(f"chars: {chars}")
print(f"words: {words}")
