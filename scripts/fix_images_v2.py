from pathlib import Path
import re
import os

ROOT = Path.cwd()
ASSETS = ROOT / "assets" / "imgs"

pattern = re.compile(r'!\[\]\((.*?)\)')

for md in ROOT.rglob("*.md"):

    text = md.read_text(encoding="utf-8")

    def replace(match):
        old_path = match.group(1)

        # Ignorar enlaces externos
        if old_path.startswith(("http://", "https://")):
            return match.group(0)

        filename = Path(old_path).name

        image = ASSETS / filename

        # Si la imagen no existe, no modificar
        if not image.exists():
            print(f"[!] No encontrada: {filename}")
            return match.group(0)

        # Ruta relativa desde el Markdown
        relative = os.path.relpath(image, md.parent)

        # Windows usa "\"; Markdown necesita "/"
        relative = relative.replace("\\", "/")

        return f"![]({relative})"

    new_text = pattern.sub(replace, text)

    if new_text != text:
        md.write_text(new_text, encoding="utf-8")
        print(f"[✓] {md}")

print("\n✔ Todas las rutas han sido corregidas.")
