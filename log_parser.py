#!/usr/bin/env python3
"""
Script: log_parser.py

Qué hace:
Analiza logs de autenticación y cuenta intentos de acceso fallidos.

Por qué es útil en seguridad:
Apoya la detección temprana de ataques de fuerza bruta y accesos no autorizados,
siendo útil en la fase de detección y análisis de incidentes.

Cómo ejecutarlo:
python3 log_parser.py

Requisitos:
- Python 3
- Permisos de lectura sobre /var/log/auth.log
"""

# =====================
# Funciones
# =====================

def parse_log(file_path):
    failed_attempts = 0

    try:
        # Lectura del archivo de logs línea por línea
        with open(file_path, "r") as log:
            for line in log:
                # Identificación de fallos de autenticación
                if "Failed password" in line:
                    failed_attempts += 1

        print(f"Intentos de acceso fallidos detectados: {failed_attempts}")

    except FileNotFoundError:
        print("Archivo de log no encontrado.")


# =====================
# Main
# =====================

if __name__ == "__main__":
    log_file = "/var/log/auth.log"
    parse_log(log_file)
