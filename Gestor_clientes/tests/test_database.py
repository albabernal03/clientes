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
        cliente_existe = db.Clientes.buscar('15j') 
        cliente_no_existe = db.Clientes.buscar('99X')
        self.assertIsNotNone(cliente_existe)
        self.assertIsNone(cliente_no_existe)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')

