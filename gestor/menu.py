import os 
import helpers
import database as db
def iniciar():
    while True:
        helpers.limpiar_pantalla()
        os.system('clear')
        print("========================")
        print("  Bienvenido AL Manager ") 
        print("========================")
        print("[1] Listar los clientes ")
        print("[2] Buscar un cliente   ")
        print("[3] Añadir un cliente   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion= input('>')

        if opcion == '1':
            print('Listando los clientes...\n')
            for cliente in db.Clientes.lista:
                print(cliente)
        if opcion == '2':
            print('Buscando un cliente...\n')
            dni= helpers.leer_texto(3,3,'DNI (2 ints y 1 char').upper()
            cliente= db.Clientes.buscar(dni)
        if opcion == '3':
            print('Añadiendo un cliente...\n')
        if opcion == '4':
            print('Modificando un cliente...\n')
        if opcion == '5':
            print('Borrando un cliente...\n')
        if opcion == '6':
            print('Saliendo...\n')
            break
        input('\n Presione ENTER para continuar...')