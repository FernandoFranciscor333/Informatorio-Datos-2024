import os
import platform

from clases import (
    Producto,
    ProductoElectronico,
    ProductoAlimenticio,
    GestionProductos
)

def limpiar_pantalla():
    # Limpiar la pantalla según el sistema operativo
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print(" =============== Menú de Gestión de Productos =============== ")
    print(" 1. Agregar Producto Electrónico")
    print(" 2. Agregar Producto Alimenticio")
    print(" 3. Buscar Producto")
    print(" 4. Actualizar Stock de Producto")
    print(" 5. Eliminar Producto")
    print(" 6. Mostrar todos los Productos")
    print(" 7. Salir")
    print(" ===============================================================")