#!/bin/bash
#
# Script: permissions_check.sh
#
# Qué hace:
# Revisa los permisos de archivos críticos del sistema Linux.
#
# Por qué es útil en seguridad:
# Permite detectar configuraciones inseguras que podrían facilitar
# accesos no autorizados o escalamiento de privilegios.
#
# Cómo ejecutarlo:
# chmod +x permissions_check.sh
# ./permissions_check.sh
#
# Requisitos:
# - Sistema Linux
# - Permisos adecuados
#

# =====================
# Variables
# =====================

FILES=(
  "/etc/passwd"
  "/etc/shadow"
)

# =====================
# Lógica principal
# =====================

for FILE in "${FILES[@]}"; do
  if [ -f "$FILE" ]; then
    ls -l "$FILE"
  else
    echo "Archivo no encontrado: $FILE"
  fi
done
