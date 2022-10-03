import os
import platform

from matplotlib.pyplot import text

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def leer_texto(longitud_min=0, longitud_max= 100, mensaje = None):
    print(mensaje) if mensaje else None
    while True:
        texto = input('>')
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto