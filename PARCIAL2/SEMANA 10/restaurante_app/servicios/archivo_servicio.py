import json
import os
from typing import List, Dict, Any


class ArchivoServicio:
    """Servicio encargado de leer y escribir productos en formato JSON.

    Maneja errores esperados: FileNotFoundError, json.JSONDecodeError, PermissionError.
    """

    def __init__(self, ruta: str) -> None:
        self.ruta = ruta

    def cargar_productos(self) -> List[Dict[str, Any]]:
        """Carga y devuelve la lista de productos desde el archivo JSON.

        Si el archivo no existe devuelve una lista vacía. Si el contenido no es
        un JSON válido devuelve una lista vacía y muestra un mensaje.
        """
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
            if not isinstance(datos, list):
                raise ValueError("Formato de datos inválido: se esperaba una lista de productos")
            return datos
        except FileNotFoundError:
            # Primer inicio: no hay archivo todavía
            return []
        except json.JSONDecodeError as e:
            print(f"  ❌ Error: el archivo JSON está corrupto o no es válido: {e}")
            return []
        except PermissionError as e:
            print(f"  ❌ Permiso denegado al leer el archivo: {e}")
            return []

    def guardar_productos(self, productos: List[Dict[str, Any]]) -> None:
        """Guarda la lista de productos en el archivo JSON. Crea la carpeta si hace falta."""
        carpeta = os.path.dirname(self.ruta)
        if carpeta and not os.path.exists(carpeta):
            try:
                os.makedirs(carpeta, exist_ok=True)
            except PermissionError as e:
                raise PermissionError(f"No se puede crear la carpeta de datos: {e}") from e

        try:
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump(productos, f, ensure_ascii=False, indent=2)
        except PermissionError as e:
            raise PermissionError(f"No se puede escribir en el archivo: {e}") from e

