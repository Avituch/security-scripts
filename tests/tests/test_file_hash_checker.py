#!/usr/bin/env python3
"""
Test: test_file_hash_checker.py

Qué hace:
Valida el correcto funcionamiento del script file_hash_checker.py,
asegurando que el hash generado cumpla con el formato esperado.

Por qué es útil en seguridad:
En informática forense y verificación de integridad, es fundamental
garantizar que las funciones de hash entreguen resultados consistentes
y confiables. Este test ayuda a detectar errores en la lógica de hashing.

Qué valida este test:
- Que la función retorne un string
- Que el hash tenga la longitud correcta (SHA-256)

Qué NO valida:
- No compara hashes conocidos
- No valida resistencia criptográfica (fuera de alcance)

Cómo ejecutarlo:
python3 -m unittest tests/test_file_hash_checker.py
"""

import unittest
import os
from file_hash_checker import hash_file


class TestFileHashChecker(unittest.TestCase):

    def setUp(self):
        """
        Prepara un archivo temporal de prueba antes de cada test.
        """
        self.test_file = "test.txt"
        with open(self.test_file, "w") as f:
            f.write("seguridad")

    def tearDown(self):
        """
        Elimina el archivo temporal luego de cada test.
        """
        os.remove(self.test_file)

    def test_hash_is_string(self):
        """
        Verifica que el hash generado sea un string.
        """
        result = hash_file(self.test_file)
        self.assertIsInstance(result, str)

    def test_hash_has_correct_length(self):
        """
        Verifica que el hash SHA-256 tenga 64 caracteres.
        """
        result = hash_file(self.test_file)
        self.assertEqual(len(result), 64)


if __name__ == "__main__":
    unittest.main()
