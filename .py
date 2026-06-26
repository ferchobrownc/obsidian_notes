import re
from pathlib import Path

md_file = Path("bash/OverTheWire/Bandit.md")
img_dir = Path("bash/OverTheWire/imgs")

text = md_file.read_text()

# mapa: nombre -> ruta
images = {p.name: f"imgs/{p.name}" for p in img_dir.glob("*.*")}

def repl(match):
    name = match.group(1)
    if name in images:
        return f"![]({images[name]})"
    return match.group(0)

# reemplaza TODO lo que sea ![](algo.png)
text = re.sub(r'!\[\]\(([^)]+)\)', repl, text)

md_file.write_text(text)

print("OK - imágenes corregidas")
