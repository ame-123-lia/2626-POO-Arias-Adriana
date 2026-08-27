import json
import os
from typing import List, Dict, Any


class ArchivoServicio:
    """Servicio encargado de leer y escribir productos, usuarios y ventas en JSON.

    Maneja errores esperados: FileNotFoundError, json.JSONDecodeError, PermissionError.
    """

    def __init__(self, ruta_productos: str, ruta_usuarios: str, ruta_ventas: str) -> None:
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas

    def _cargar_desde_archivo(self, ruta: str) -> List[Dict[str, Any]]:
        """Carga datos desde un archivo JSON. Devuelve lista vacía si no existe o hay error."""
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
            if not isinstance(datos, list):
                raise ValueError(f"Formato de datos inválido en {ruta}: se esperaba una lista")
            return datos
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            print(f"  ❌ Error: el archivo JSON está corrupto ({ruta}): {e}")
            return []
        except PermissionError as e:
            print(f"  ❌ Permiso denegado al leer {ruta}: {e}")
            return []

    def _guardar_en_archivo(self, ruta: str, datos: List[Dict[str, Any]]) -> None:
        """Guarda datos en un archivo JSON. Crea la carpeta si es necesario."""
        carpeta = os.path.dirname(ruta)
        if carpeta and not os.path.exists(carpeta):
            try:
                os.makedirs(carpeta, exist_ok=True)
            except PermissionError as e:
                raise PermissionError(f"No se puede crear la carpeta de datos: {e}") from e

        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
        except PermissionError as e:
            raise PermissionError(f"No se puede escribir en el archivo {ruta}: {e}") from e

    def cargar_productos(self) -> List[Dict[str, Any]]:
        """Carga y devuelve la lista de productos desde el archivo JSON."""
        return self._cargar_desde_archivo(self.ruta_productos)

    def guardar_productos(self, productos: List[Dict[str, Any]]) -> None:
        """Guarda la lista de productos en el archivo JSON."""
        self._guardar_en_archivo(self.ruta_productos, productos)

    def cargar_usuarios(self) -> List[Dict[str, Any]]:
        """Carga y devuelve la lista de usuarios desde el archivo JSON."""
        return self._cargar_desde_archivo(self.ruta_usuarios)

    def guardar_usuarios(self, usuarios: List[Dict[str, Any]]) -> None:
        """Guarda la lista de usuarios en el archivo JSON."""
        self._guardar_en_archivo(self.ruta_usuarios, usuarios)

    def cargar_ventas(self) -> List[Dict[str, Any]]:
        """Carga y devuelve la lista de ventas desde el archivo JSON."""
        return self._cargar_desde_archivo(self.ruta_ventas)

    def guardar_ventas(self, ventas: List[Dict[str, Any]]) -> None:
        """Guarda la lista de ventas en el archivo JSON."""
        self._guardar_en_archivo(self.ruta_ventas, ventas)


