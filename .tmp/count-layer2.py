p = r"C:\Users\rtske\Projects\archimedes\threats\briefs\2026-05-21-morning.md"
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('## 📣 Discord Summary')
layer2 = text[idx:].rstrip()
print(f"chars: {len(layer2)}")
print(f"words: {len(layer2.split())}")
