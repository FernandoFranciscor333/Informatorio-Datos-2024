""" Desafío 1: Sistema de Gestión de Productos
Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar productos del inventario.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.
 """


import json

class Producto:
    def __init__(self, nombre, precio, stock, origen):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__origen = origen
    
    @property    
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def precio(self):
        return self.__precio   #que devuelva con puntos y $
    
    @property
    def stock(self):
        return self.__stock   #que devuelva con puntos
    
    @property
    def origen(self):
        return self.__origen.capitalize() 
    
    #AÑADIR VALIDACIONES
    
    #FUNCIONES
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "origen": self.origen             
        }
        
    def __str__(self):
        return f"{self.nombre}"
    
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, origen, fecha_fabricacion):
        super().__init__(nombre, precio, stock, origen)        
        self.__fecha_fabricacion = fecha_fabricacion 
        
    
    @property
    def fecha_fabricacion(self):
        return self.__fecha_fabricacion #FORMATO FECHA
    
    def to_dict(self):
        data = super().to_dict()
        data['fecha_fabricacion'] = self.fecha_fabricacion
        
    def __str__(self):
        return f'{super().__str__()} - Fecha de Fabricación: {self.fecha_fabricacion}'

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, stock, origen, fecha_vencimiento):
        super().__init__(nombre, precio, stock, origen)        
        self.__fecha_vencimiento = fecha_vencimiento
        
    
    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento #FORMATO FECHA
    
    def to_dict(self):
        data = super().to_dict()
        data['fecha_vencimiento'] = self.fecha_vencimiento
        
    def __str__(self):
        return f'{super().__str__()} - Fecha de Vencimiento: {self.fecha_vencimiento}'
    
class GestionProductos:
    def __init__(self, archivo):
        self.archivo = archivo
    
    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)            
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos
    
    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')    

    def crear_producto(self, producto):
        try:
            datos = self.leer_datos()
            nombre = producto.nombre
            if not str(nombre) in datos.keys():
                datos[nombre] = producto.to_dict()
                self.guardar_datos(datos)
                print(f'Producto ({producto.nombre}) - creado correctamente')
            else:
                print(f'Producto ({nombre}) ya existe en el inventario')            
        except Exception as error:
            print(f'Error inesperado al crear producto: {error}')
    
    def leer_producto(self, nombre_producto):
        try:
            datos = self.leer_datos()
            if nombre_producto in datos:
                producto_data = datos[nombre_producto]
                if 'fecha_fabricacion' in producto_data:
                    producto = ProductoElectronico(**producto_data) 
                else:
                    producto = ProductoAlimenticio(**producto_data) 
                print(f"Producto {producto} encontrado")
            else:
                print(f"No se encontró el producto {producto}")
                    
        except Exception as e:
            print("Error al leer el producto: {e}")
    
    def actualizar_producto(self, nombre_producto, nuevo_stock):
        try:
            datos = self.leer_datos()
            if str(nombre_producto) in datos.keys():
                datos[nombre_producto]['stock'] = nuevo_stock #hacer validaciones
                self.guardar_datos(datos)
                print(f"Stock actualizado: {nombre_producto}")
            else:
                print(f"No se encontró el producto {nombre_producto}")            
        except Exception as e:
            print(f"Error al actualizar el producto: {e}")
    
    def eliminar_producto(self, nombre_producto):
        try:
            datos = self.leer_datos()
            if str(nombre_producto) in datos.keys():
                del datos[nombre_producto]
                self.guardar_datos(datos)
                print(f"El producto {nombre_producto} ha sido eliminado correctamente")
            else:
                print(f"No se encontró el producto {nombre_producto}")            
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")  
         

    