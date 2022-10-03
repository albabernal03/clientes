import copy # Para copiar objetos
import unittest # Para hacer pruebas unitarias
import gestor.database as db # Importamos el modulo database
import helpers

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
    
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('28Z'))
        cliente_modificado = db.Clientes.modificar('28Z', 'Mariana', 'García')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('48H')
        cliente_rebuscado = db.Clientes.buscar('48H')
        self.assertEqual(cliente_borrado.dni, '48H')
    
    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('232323S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))

if __name__ == '__main__':
    unittest.main()
    