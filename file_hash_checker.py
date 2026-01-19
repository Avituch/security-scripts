#!/usr/bin/env python3
"""
Script: file_hash_checker.py

Qué hace:
Calcula el hash SHA-256 de un archivo para verificar su integridad.

Por qué es útil en seguridad:
Es una técnica fundamental en informática forense para detectar modificaciones
no autorizadas en archivos.

Cómo ejecutarlo:
python3 file_hash_checker.py

Requisitos:
- Python 3
"""

import hashlib

# =====================
# Funciones
# =====================

def hash_file(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


# =====================
# Main
# =====================

if __name__ == "__main__":
    file_to_check = "test.txt"
    print(hash_file(file_to_check))
