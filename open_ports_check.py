#!/usr/bin/env python3
"""
Script: open_ports_check.py

Qué hace:
Verifica si determinados puertos están abiertos en un host específico.

Por qué es útil en seguridad:
Permite identificar servicios expuestos innecesariamente, ayudando a reducir
la superficie de ataque.

Cómo ejecutarlo:
python3 open_ports_check.py

Requisitos:
- Python 3
"""

import socket

# =====================
# Configuración
# =====================

HOST = "127.0.0.1"
PORTS = [22, 80, 443]


# =====================
# Funciones
# =====================

def check_ports(host, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Puerto {port} abierto")
        sock.close()


# =====================
# Main
# =====================

if __name__ == "__main__":
    check_ports(HOST, PORTS)
