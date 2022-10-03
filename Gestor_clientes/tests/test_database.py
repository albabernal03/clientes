import copy # Para copiar objetos
import unittest # Para hacer pruebas unitarias
import database as db # Para importar el modulo database

class TestDatabase(unittest.TestCase):
    def setUp(self): # Se ejecuta antes de cada prueba
        db.Clientes.lista = [
            db.Cliente('15J', 'Marta', 'Pérez'),
            db.Cliente('48H', 'Manolo', 'López'),
            db.Cliente('28Z', 'Ana', 'García')
        ]
    def test_bucar_cliente(self):
        