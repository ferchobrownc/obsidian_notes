from pathlib import Path
import re

ROOT = Path(".")
IMG_FOLDERS = []

# buscar todas las carpetas imgs
for p in ROOT.rglob("imgs"):
    if p.is_dir():
        IMG_FOLDERS.append(p)

print(f"[+] Carpetas imgs encontradas: {len(IMG_FOLDERS)}")

# mapa global: nombre -> ruta relativa
image_map = {}

for folder in IMG_FOLDERS:
    for img in folder.rglob("*"):
        if img.is_file():
            image_map[img.name] = img.as_posix()

print(f"[+] Imágenes indexadas: {len(image_map)}")

pattern = re.compile(r'!\[\]\(([^)]+)\)')

def fix(match):
    name = match.group(1)

    # ya está bien
    if name.startswith("http"):
        return match.group(0)

    # ya tiene ruta imgs/
    if name in image_map.values():
        return match.group(0)

    # nombre directo
    if name in image_map:
        return f"![]({image_map[name]})"

    return match.group(0)

for md in ROOT.rglob("*.md"):
    text = md.read_text()

    new_text = pattern.sub(fix, text)

    if new_text != text:
        print(f"[+] Fix: {md}")
        md.write_text(new_text)

print("[✔] DONE")
