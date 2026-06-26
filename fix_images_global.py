from pathlib import Path
import re

# carpeta base de tu vault
ROOT = Path("bash/OverTheWire")
IMG_DIR = ROOT / "imgs"

# cargar imágenes reales
images = {img.name for img in IMG_DIR.glob("*.*")}

print(f"[+] Imágenes encontradas: {len(images)}")

# regex para ![](archivo.png)
pattern = re.compile(r'!\[\]\(([^)]+)\)')

# recorrer todos los md
for md_file in ROOT.glob("*.md"):
    text = md_file.read_text()

    def replace(match):
        name = match.group(1)

        # si ya tiene imgs/, lo dejamos igual
        if name.startswith("imgs/"):
            return match.group(0)

        # si existe en imgs/, lo arreglamos
        if name in images:
            return f"![](imgs/{name})"

        return match.group(0)

    new_text = pattern.sub(replace, text)

    if new_text != text:
        print(f"[+] Corregido: {md_file.name}")
        md_file.write_text(new_text)

print("[✔] Listo. Rutas corregidas.")
