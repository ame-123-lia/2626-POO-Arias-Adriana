import json
import os
from modelos import Producto, Usuario


class ArchivoServicio:
    def __init__(self, ruta_datos):
        self.ruta_datos = ruta_datos
    
    def cargar_productos(self):
        """Carga los productos desde el archivo JSON"""
        ruta_archivo = os.path.join(self.ruta_datos, "productos.json")
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            return [Producto(**p) for p in datos]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error al cargar productos: {e}")
            return []
    
    def guardar_productos(self, productos):
        """Guarda los productos en el archivo JSON"""
        ruta_archivo = os.path.join(self.ruta_datos, "productos.json")
        try:
            datos = [
                {
                    "id": p.id,
                    "nombre": p.nombre,
                    "precio": p.precio,
                    "cantidad": p.cantidad,
                    "descripcion": p.descripcion
                }
                for p in productos
            ]
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Error al guardar productos: {e}")
            return False
    
    def cargar_usuarios(self):
        """Carga los usuarios desde el archivo JSON"""
        ruta_archivo = os.path.join(self.ruta_datos, "usuarios.json")
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            return [Usuario(**u) for u in datos]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")
            return []
    
    def guardar_usuarios(self, usuarios):
        """Guarda los usuarios en el archivo JSON"""
        ruta_archivo = os.path.join(self.ruta_datos, "usuarios.json")
        try:
            datos = [
                {
                    "id": u.id,
                    "nombre": u.nombre,
                    "usuario": u.usuario,
                    "contraseña": u.contraseña,
                    "rol": u.rol
                }
                for u in usuarios
            ]
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Error al guardar usuarios: {e}")
            return False
