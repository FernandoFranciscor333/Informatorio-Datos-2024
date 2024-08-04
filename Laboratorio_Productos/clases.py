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
from datetime import datetime
from datetime import date
import traceback

class Producto:
    def __init__(self, nombre, precio, stock, origen):
        self.__nombre = nombre
        self.__precio = self.validar_precio(precio)
        self.__stock = self.validar_stock(stock)
        self.__origen = origen
    
    @property    
    def nombre(self):
        return self.__nombre.capitalize()
    
    @property
    def precio(self):
        return float(self.__precio)
    
    @property
    def stock(self):
        return int(self.__stock)
    
    @property
    def origen(self):
        return self.__origen.capitalize() 
    
    #SETTERS
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio) 

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = self.validar_stock(nuevo_stock) 
    
    #AÑADIR VALIDACIONES
    
    # def validar_precio(self, precio):
    #     try:
    #         precio_num = float(precio)
    #         if precio_num <= 0:
    #             print("El precio debe ser mayor a igual a 0")
    #         else:
    #             return precio_num
    #     except ValueError:
    #         raise ValueError("El precio debe ser un número válido")
        
        
    # def validar_stock(self, stock):
    #     try:
    #         stock_num = int(stock)
    #         if stock_num <= 0:
    #             print("El precio debe ser mayor a igual a 0")
    #         else:
    #             return stock_num
    #     except ValueError:
    #         raise ValueError("El stock debe ser un número válido")        
    
    def validar_precio(self, precio):
        try:
            precio_num = float(precio)
            if precio_num <= 0:
                raise ValueError("El precio debe ser mayor a 0")
            return precio_num
        except ValueError as e:
            raise ValueError(f"Error en el precio: {str(e)}")

    def validar_stock(self, stock):
        try:
            stock_num = int(stock)
            if stock_num < 0:
                raise ValueError("El stock no puede ser negativo")
            return stock_num
        except ValueError as e:
            raise ValueError(f"Error en el stock: {str(e)}")

    
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
        self.__fecha_fabricacion = self.validar_fecha(fecha_fabricacion)
        
    
    @property
    def fecha_fabricacion(self):
        return self.__fecha_fabricacion 
    
    @fecha_fabricacion.setter
    def fecha_fabricacion(self, nueva_fecha):
        self.__fecha_fabricacion = self.validar_fecha(nueva_fecha)  # Corregido
    
    def validar_fecha(self, fecha): #FORMATO FECHA
        try:
            fecha_fabricacion = datetime.strptime(fecha,'%d-%m-%Y')
            fecha_fabricacion = fecha_fabricacion.date()
            return fecha_fabricacion
        except Exception as e:
            print("Ingrese un formato de fecha correcto: dd/mm/aaaa: {e}")
        
        
    def to_dict(self):
        data = super().to_dict()
        data['fecha_fabricacion'] = self.fecha_fabricacion.isoformat()
        return data
        
    def __str__(self):
        return f'{super().__str__()} - Fecha de Fabricación: {self.fecha_fabricacion}'

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, stock, origen, fecha_vencimiento):
        super().__init__(nombre, precio, stock, origen)        
        self.__fecha_vencimiento = self.validar_fecha(fecha_vencimiento)
        
    
    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento 
       
    @fecha_vencimiento.setter
    def fecha_vencimiento(self, nueva_fecha):
        self.__fecha_vencimiento = self.validar_fecha(nueva_fecha)  # Corregido
    
    def validar_fecha(self, fecha): #FORMATO FECHA
        try: 
            fecha_vencimiento = datetime.strptime(fecha, '%d-%m-%Y')
            fecha_vencimiento = fecha_vencimiento.date()
            return fecha_vencimiento
        except Exception as e:
            print("Ingrese un formato de fecha correcto: dd/mm/aaaa: {e}")
    
    
    def to_dict(self):
        data = super().to_dict()
        data['fecha_vencimiento'] = self.fecha_vencimiento.isoformat()
        return data
        
    def __str__(self):
        return f'{super().__str__()} - Fecha de Vencimiento: {self.fecha_vencimiento}'
    
class GestionProductos:
    def __init__(self, archivo):
        self.archivo = archivo

    
    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
            print(f"Datos leídos correctamente: {len(datos)} productos encontrados.")
            return datos
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no fue encontrado.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error al decodificar el JSON: {str(e)}")
            return {}
        except Exception as e:
            print(f"Error inesperado al leer datos del archivo: {str(e)}")
            return {}
    
    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4, default=self.serializar_fecha)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')    
            
    @staticmethod
    def serializar_fecha(obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

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
                    
            if isinstance(producto, ProductoElectronico):
                print(f"Fecha de fabricación: {producto.fecha_fabricacion}")
            elif isinstance(producto, ProductoAlimenticio):
                print(f"Fecha de vencimiento: {producto.fecha_vencimiento}")
            else:
                print(f"No se encontró el producto '{nombre_producto}'")
        
        except Exception as e:
            print(f"Error al leer el producto: {str(e)}")
            print("Detalles del error:")
            print(traceback.format_exc())
    
    def actualizar_precio_producto(self, nombre_producto, nuevo_precio):
        try:
            datos = self.leer_datos()
            if str(nombre_producto) in datos.keys():
                datos[nombre_producto]['precio'] = nuevo_precio
                self.guardar_datos(datos)
                print(f"Precio actualizado: {nombre_producto}")
            else:
                print(f"No se encontró el producto {nombre_producto}")
        except Exception as e:
            print(f"Error al actualizar el producto: {e}")
    
    def actualizar_stock_producto(self, nombre_producto, nuevo_stock):
        try:
            datos = self.leer_datos()
            if str(nombre_producto) in datos.keys():
                datos[nombre_producto]['stock'] = nuevo_stock
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
