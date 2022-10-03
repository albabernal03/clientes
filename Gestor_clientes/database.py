class Cliente:
    def __init__(self,dni,nombre,apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"{self.dni},{self.nombre},{self.apellido}" #esta funcion es para que cuando se imprima el objeto, se imprima en el formato que yo quiero
