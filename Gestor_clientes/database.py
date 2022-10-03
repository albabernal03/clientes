class Cliente:
    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"{self.dni},{self.nombre},{self.apellido}" #esta funcion es para que cuando se imprima el objeto, se imprima en el formato que yo quiero

class Clientes:
    lista=[]

    @staticmethod #para que no se cree una instancia de la clase
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
    
    @staticmethod
    def crear(dni,nombre,apellido):
        cliente = Cliente(dni,nombre,apellido)
        Clientes.lista.append(cliente)
        return cliente
    
    @staticmethod
    def modificar(dni,nombre,apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                return Clientes.lista[i]
        
