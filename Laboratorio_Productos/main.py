import os
import platform

from clases import (    
    ProductoElectronico,
    ProductoAlimenticio,
    GestionProductos
)

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print(" =============== Menú de Gestión de Productos =============== ")
    print(" 1. Agregar Producto Electrónico")
    print(" 2. Agregar Producto Alimenticio")
    print(" 3. Buscar Producto")
    print(" 4. Actualizar Precio de Producto")
    print(" 5. Actualizar Stock de Producto")
    print(" 6. Eliminar Producto")
    print(" 7. Mostrar todos los Productos")
    print(" 8. Salir")
    print(" ===============================================================")

def agregar_producto(gestion:GestionProductos, tipo_producto):
    try:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        origen = input("Ingrese el país de origen del producto: ")
        
        if tipo_producto == '1':
            fecha_fabricacion = input("Ingrese la fecha de fabricación del producto (dd-mm-aaaa): ")
            producto = ProductoElectronico(nombre, precio, stock, origen, fecha_fabricacion)
        elif tipo_producto == '2':
            fecha_vencimiento = input("Ingrese la fecha de caducidad del producto (dd-mm-aaaa): ")
            producto = ProductoAlimenticio(nombre, precio, stock, origen, fecha_vencimiento)
        else:
            print("Opción inválida")
            return
        
        gestion.crear_producto(producto)
        input("Presione Enter para continuar...")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
def buscar_producto_por_nombre(gestion):
    nombre = input("ingrese el nombre del producto: ")
    gestion.leer_producto(nombre)
    input("Presione Enter para continuar") 

def actualizar_precio_producto(gestion):
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    datos = gestion.leer_datos()
    
    if nombre in datos:
        producto = datos[nombre]
        precio_actual = float(producto['precio'].replace('$', '').replace(',', ''))
        
        print(f"Precio actual de {nombre}: ${precio_actual:.2f}")
        
        opcion = input("¿Desea establecer un nuevo precio (1) o modificar por porcentaje (2)? ")
        
        if opcion == '1':
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
        elif opcion == '2':
            porcentaje = float(input("Ingrese el porcentaje de cambio (positivo para aumentar, negativo para disminuir): "))
            nuevo_precio = precio_actual * (1 + porcentaje/100)
        else:
            print("Opción no válida.")
            return
        
        diferencia = nuevo_precio - precio_actual
        
        gestion.actualizar_precio_producto(nombre, nuevo_precio)
        
        if diferencia > 0:
            print(f"El precio de {nombre} aumentó en ${diferencia:.2f}.")
        elif diferencia < 0:
            print(f"El precio de {nombre} disminuyó en ${abs(diferencia):.2f}.")
        else:
            print(f"El precio de {nombre} no cambió.")
    else:
        print(f"No se encontró el producto {nombre}")
    
    input("Presione Enter para continuar")



def actualizar_stock_producto(gestion):
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    datos = gestion.leer_datos()
    
    if nombre in datos:
        producto = datos[nombre]
        stock_actual = int(producto['stock'])
        
        print(f"Stock actual de {nombre}: {stock_actual}")
        
        opcion = input("¿Desea establecer un nuevo valor (1) o modificar por porcentaje (2)? ")
        
        if opcion == '1':
            nuevo_stock = int(input("Ingrese el nuevo valor de Stock: "))
        elif opcion == '2':
            porcentaje = float(input("Ingrese el porcentaje de cambio (positivo para aumentar, negativo para disminuir): "))
            nuevo_stock = int(stock_actual * (1 + porcentaje/100))
        else:
            print("Opción no válida.")
            return
        
        diferencia = nuevo_stock - stock_actual
        
        gestion.actualizar_stock_producto(nombre, nuevo_stock)
        
        if diferencia > 0:
            print(f"El stock de {nombre} aumentó en {diferencia} unidades.")
        elif diferencia < 0:
            print(f"El stock de {nombre} disminuyó en {abs(diferencia)} unidades.")
        else:
            print(f"El stock de {nombre} no cambió.")
    else:
        print(f"No se encontró el producto {nombre}")
    
    input("Presione Enter para continuar")
    
def eliminar_producto(gestion):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    gestion.eliminar_producto(nombre)
    input("Presione Enter para continuar")
    
def mostrar_todos_los_productos(gestion):
    print(" =========== Listado Completo de Productos ================")
    for producto in gestion.leer_datos().values():
        if 'fecha_fabricacion' in producto:
            print(f"{producto['nombre']} - Stock {producto['stock']}")
        else:
            print(f"{producto['nombre']} - Stock {producto['stock']}")
    print(" ===============================================================")
    input("Presione Enter para continuar")
    

if __name__ == "__main__":
    archivo_productos = 'productos_lista_db.json'
    gestion = GestionProductos(archivo_productos)
    
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