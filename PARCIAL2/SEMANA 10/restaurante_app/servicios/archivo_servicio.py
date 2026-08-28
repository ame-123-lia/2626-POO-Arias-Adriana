import json
from typing import List, Dict, Any

try:
    # Cuando se importa como paquete
    from ..modelos.producto import Producto
except ImportError:
    # Cuando se ejecuta directamente
    from modelos.producto import Producto


class ArchivoServicio:
    """
    Servicio encargado de la persistencia de productos en JSON.
    
    Responsabilidades:
        - Cargar productos desde archivo JSON
        - Guardar productos a archivo JSON
        - Manejar errores de lectura/escritura
        - Validar estructura de datos
    """

    def __init__(self, ruta_archivo: str) -> None:
        """
        Inicializa el servicio con la ruta del archivo.
        
        Args:
            ruta_archivo: ruta completa del archivo productos.json
        """
        self.ruta_archivo: str = ruta_archivo

    def cargar_productos(self) -> List[Producto]:
        """
        Carga los productos desde el archivo JSON.
        
        Maneja las siguientes excepciones:
            - FileNotFoundError: si el archivo no existe (primera ejecución)
            - json.JSONDecodeError: si el contenido no es JSON válido
            - PermissionError: si no hay permisos de lectura
            - KeyError: si faltan claves en los registros
            - ValueError: si los datos de un producto son inválidos
        
        Returns:
            Lista de objetos Producto cargados desde el archivo
        """
        productos: List[Producto] = []
        
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                registros = json.load(archivo)
                
                if not isinstance(registros, list):
                    print("⚠️  Advertencia: El archivo no contiene una lista de productos.")
                    return productos
                
                for i, registro in enumerate(registros, start=1):
                    try:
                        producto = Producto.from_dict(registro)
                        productos.append(producto)
                    except KeyError as e:
                        print(f"⚠️  Producto {i} omitido: Falta la clave {e}")
                    except ValueError as e:
                        print(f"⚠️  Producto {i} omitido: Datos inválidos ({e})")
                    except TypeError as e:
                        print(f"⚠️  Producto {i} omitido: Error de tipo ({e})")
        
        except FileNotFoundError:
            print(f"ℹ️  El archivo '{self.ruta_archivo}' no existe. Se iniciará con colección vacía.")
        
        except json.JSONDecodeError as e:
            print(f"❌ Error: El archivo '{self.ruta_archivo}' no contiene JSON válido: {e}")
        
        except PermissionError:
            print(f"❌ Error: No hay permisos para leer el archivo '{self.ruta_archivo}'")
        
        except Exception as e:
            print(f"❌ Error inesperado al cargar productos: {e}")
        
        return productos

    def guardar_productos(self, productos: List[Producto]) -> bool:
        """
        Guarda los productos en el archivo JSON.
        
        Maneja las siguientes excepciones:
            - PermissionError: si no hay permisos de escritura
            - IOError: errores generales de entrada/salida
            - TypeError: si los objetos no son serializables
        
        Args:
            productos: lista de objetos Producto a guardar
            
        Returns:
            True si se guardaron correctamente, False en caso contrario
        """
        try:
            # Convertir cada Producto a diccionario
            registros: List[Dict[str, Any]] = [p.to_dict() for p in productos]
            
            # Guardar en JSON con indentación para legibilidad
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(registros, archivo, indent=2, ensure_ascii=False)
            
            return True
        
        except PermissionError:
            print(f"❌ Error: No hay permisos para escribir el archivo '{self.ruta_archivo}'")
            return False
        
        except IOError as e:
            print(f"❌ Error de entrada/salida al guardar productos: {e}")
            return False
        
        except TypeError as e:
            print(f"❌ Error: No se pueden serializar los productos a JSON: {e}")
            return False
        
        except Exception as e:
            print(f"❌ Error inesperado al guardar productos: {e}")
            return False
