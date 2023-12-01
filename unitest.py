import unittest
from unittest.mock import patch
from funcion.py import encontrar_propietario, pagary

class TestFunciones(unittest.TestCase):

    # Pruebas de éxito para encontrar_propietario
def test_encontrar_propietario_exito(self):
        # Simular un archivo CSV con un solo usuario para el número buscado
        with patch('tu_app.leer_csv', return_value=[{'celular': '123456789', 'name': 'Juan', 'saldo': '500'}]):
            resultado = encontrar_propietario('123456789')
            self.assertEqual(resultado, ['123456789', 'Juan', '500'])

    # Pruebas de error para encontrar_propietario
def test_encontrar_propietario_error(self):
        # Simular un archivo CSV sin el número buscado
        with patch('tu_app.leer_csv', return_value=[{'celular': '987654321', 'name': 'Ana', 'saldo': '300'}]):
            resultado = encontrar_propietario('123456789')
            self.assertEqual(resultado, "No se encontro usuario")

    # Pruebas de éxito para pagary
        with patch('builtins.open'), patch('csv.DictWriter') as mock_writer:
def test_pagary_exito(self):
        # Simular el archivo CSV de transacciones
            # Llamar a pagary con valores válidos
            resultado = pagary('123456789', '987654321', '100')
            self.assertIsInstance(resultado, list)
            # Asegurarse de que se llame a obtener_transacciones
            mock_writer.return_value.writerow.assert_called_once()

    # Pruebas de error para pagary
def test_pagary_error(self):
        # Simular un valor de transferencia excesivo
        resultado = pagary('123456789', '987654321', '250')
        self.assertEqual(resultado, [])
