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
