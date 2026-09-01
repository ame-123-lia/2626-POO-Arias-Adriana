from typing import Dict, Any


class Venta:
    """Representa una venta que relaciona un usuario con un producto.

    Atributos:
        usuario_id: str - identificación del usuario que realizó la compra
        producto_codigo: str - código del producto vendido
        cantidad: int - cantidad vendida
    """

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        self.usuario_id: str = str(usuario_id).strip()
        self.producto_codigo: str = str(producto_codigo).strip()
        try:
            self.cantidad: int = int(cantidad)
        except (TypeError, ValueError) as e:
            raise ValueError("Cantidad inválida") from e

        if not self.usuario_id:
            raise ValueError("El ID del usuario no puede estar vacío")
        if not self.producto_codigo:
            raise ValueError("El código del producto no puede estar vacío")
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")

    def mostrar_informacion(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Representación en diccionario (útil para exportar a JSON)."""
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Venta":
        """Reconstruye una Venta a partir de un diccionario.

        Lanza KeyError si faltan claves esperadas o ValueError si hay datos inválidos.
        """
        usuario_id = data["usuario_id"]
        producto_codigo = data["producto_codigo"]
        cantidad = data["cantidad"]
        return cls(usuario_id, producto_codigo, cantidad)
