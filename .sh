#!/usr/bin/env bash

FILE="bash/OverTheWire/Bandit.md"
IMGDIR="bash/OverTheWire/imgs"

cp "$FILE" "$FILE.bak"

echo "[+] Reparando imágenes en $FILE..."

# 1. Reemplaza imágenes tipo Obsidian o mal formadas
sed -i 's/!\[\]/![]/g' "$FILE"

# 2. Corrige imágenes bandit*
sed -i 's|![](bandit|![](imgs/bandit|g' "$FILE"

# 3. Corrige imágenes level*
sed -i 's|![](level|![](imgs/level|g' "$FILE"

# 4. Limpia placeholders rotos de Obsidian
sed -i 's/{fileName}-{date}//g' "$FILE"

# 5. Limpieza general de basura
sed -i 's|![](imgs/)|![]()|g' "$FILE"

echo "[+] Listo. Backup en Bandit.md.bak"
