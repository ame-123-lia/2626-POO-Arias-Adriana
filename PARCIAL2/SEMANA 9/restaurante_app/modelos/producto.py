from typing import Dict


class Producto:
    """Clase que representa un producto del restaurante.

    Atributos:
        codigo: str - identificador único
        nombre: str
        categoria: str
        precio: float
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = str(codigo).strip()
        self.nombre: str = str(nombre).strip()
        self.categoria: str = str(categoria).strip()
        self.precio: float = float(precio)

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )

    def to_dict(self) -> Dict[str, object]:
        """Representación en diccionario (útil para exportar o para estructuras tipo dict)."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

