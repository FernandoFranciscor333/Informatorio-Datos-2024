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
    print(" 5. Actualizar Precio de Producto")
    print(" 6. Eliminar Producto")
    print(" 7. Mostrar todos los Productos")
    print(" 8. Salir")
    print(" ===============================================================")

def agregar_producto(gestion:GestionProductos, tipo_producto):
    try:
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        stock = input("Ingrese el stock del producto: ")
        origen = input("Ingrese el país de origen del producto: ")
        
        if tipo_producto == '1':
            fecha_fabricacion = input("Ingrese la fecha de fabricación del producto: ")
            producto = ProductoElectronico(nombre, precio, stock, origen, fecha_fabricacion)
        elif tipo_producto == '2':
            fecha_vencimiento = input("Ingrese la fecha de caducidad del producto: ")
            producto = ProductoAlimenticio(nombre, precio, stock, origen, fecha_vencimiento)
        else:
            print("Opción inválid")
            return
        
        gestion.crear_producto(producto)
        input("Presione Enter para continuar")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
def buscar_producto_por_nombre(gestion):
    nombre = input("ingrese el nombre del producto: ")
    gestion.leer_producto(nombre)
    input("Presione Enter para continuar")
    
def actualizar_stock_producto(gestion):
    nombre = input("Ingrese el nombre del producto que desea actualizar: ") #mejorar eso a aumentar o disminuir stock, y si se puede, opcion para modificar por porcentaje   
    nuevo_stock = float(input("Ingrese el nuevo valor de Stock"))
    gestion.actualizar_stock_producto(nombre, nuevo_stock)
    input("Presione Enter para continuar")
    
def actualizar_precio_producto(gestion):
    nombre = input("Ingrese el nombre del producto que desea actualizar")
    nuevo_precio = input("Ingrese el nuevo precio para el producto: ")
    gestion.actualizar_precio_producto(nombre, nuevo_precio)
    input("Presione Enter para continuar")
    
def eliminar_producto(gestion):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    gestion.eliminar_producto(nombre)
    input("Presione Enter para continuar")
    
def mostrar_todos_los_productos(gestion):
    print(" =========== Listado Completo de Colaboradores ================")
    for producto in gestion.leer_datos().values():
        if 'fecha_fabricacion' in producto:
            print(f"{producto['nombre']} - Stock {producto['stock']}")
        else:
            print(f"{producto['nombre']} - Stock {producto['stock']}")
    print(" ===============================================================")
    input("Presione Enter para continuar")
    

if __name__ == "__main__":
    archivo_colaboradores = 'colaboradores_db.json'
    gestion = GestionProductos(archivo_colaboradores)
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')
        
        if opcion == '1' or opcion == '2':
            agregar_producto(gestion, opcion)
        elif opcion == '3':
            buscar_producto_por_nombre(gestion)    
        elif opcion == '4':
            actualizar_precio_producto(gestion)     
        elif opcion == '5':
            actualizar_stock_producto(gestion)      
        elif opcion == '6':
            eliminar_producto(gestion)  
        elif opcion == '7':
            mostrar_todos_los_productos(gestion)
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")