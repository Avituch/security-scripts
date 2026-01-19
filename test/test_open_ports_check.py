#!/usr/bin/env python3
"""
Test: test_open_ports_check.py

Qué hace:
Valida el comportamiento básico del script open_ports_check.py,
asegurando que la función retorne una estructura de datos válida.

Por qué es útil en seguridad:
En scripts de análisis de superficie de ataque, es importante que
las funciones entreguen resultados consistentes que puedan ser
procesados por otras herramientas o scripts.

Qué valida este test:
- Que la función retorne una lista
- Que no genere errores en ejecución normal

Qué NO valida:
- No valida que un puerto específico esté abierto
- No realiza escaneos reales (evita falsos positivos)

Cómo ejecutarlo:
python3 -m unittest tests/test_open_ports_check.py
"""

import unittest
from open_ports_check import check_ports


class TestOpenPortsCheck(unittest.TestCase):

    def test_returns_list(self):
        """
        Verifica que la función retorne una lista,
        independiente de si hay puertos abiertos o no.
        """
        result = check_ports("127.0.0.1", [22])
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
