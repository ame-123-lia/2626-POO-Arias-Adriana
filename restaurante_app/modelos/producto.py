from typing import Dict, Any


class Producto:
    """Clase que representa un producto del restaurante.

    Atributos:
        codigo: str - identificador único
        nombre: str
        categoria: str
        precio: float
        stock: int - cantidad disponible
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        self.codigo: str = str(codigo).strip()
        self.nombre: str = str(nombre).strip()
        self.categoria: str = str(categoria).strip()
        try:
            self.precio: float = float(precio)
        except (TypeError, ValueError) as e:
            raise ValueError("Precio inválido") from e
        try:
            self.stock: int = int(stock)
        except (TypeError, ValueError) as e:
            raise ValueError("Stock inválido") from e

        # Validaciones simples
        if not self.codigo:
            raise ValueError("El código no puede estar vacío")
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Stock: {self.stock}"
        )

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock de este producto."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad

    def to_dict(self) -> Dict[str, Any]:
        """Representación en diccionario (útil para exportar a JSON)."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Producto":
        """Reconstruye un Producto a partir de un dict.

        Lanza KeyError si faltan claves esperadas o ValueError si hay datos inválidos.
        """
        codigo = data["codigo"]
        nombre = data["nombre"]
        categoria = data.get("categoria", "")
        precio = data["precio"]
        stock = data.get("stock", 0)
        return cls(codigo, nombre, categoria, precio, stock)

