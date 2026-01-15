#!/bin/bash
# Script para revisar permisos de archivos críticos

FILES=(
  "/etc/passwd"
  "/etc/shadow"
)

for FILE in "${FILES[@]}"; do
  if [ -f "$FILE" ]; then
    ls -l "$FILE"
  else
    echo "Archivo no encontrado: $FILE"
  fi
done
