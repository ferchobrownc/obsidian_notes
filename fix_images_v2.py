from pathlib import Path
import re

ROOT = Path(".")

pattern = re.compile(r'!\[\]\(([^)]+)\)')

def fix(match):
    path = match.group(1)

    # ignorar URLs externas
    if path.startswith("http"):
        return match.group(0)

    # quedarse SOLO con el nombre del archivo
    filename = Path(path).name

    return f"![](imgs/{filename})"

for md in ROOT.rglob("*.md"):
    text = md.read_text()
    new_text = pattern.sub(fix, text)

    if new_text != text:
        print(f"[+] Fix: {md}")
        md.write_text(new_text)

print("[✔] DONE")
