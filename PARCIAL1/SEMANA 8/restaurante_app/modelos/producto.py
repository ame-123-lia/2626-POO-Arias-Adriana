
class Producto:
    """Clase base que representa un producto del restaurante.

    Atributos:
        codigo: identificador único del producto
        nombre: nombre descriptivo
        categoria: categoría (por ejemplo, 'Comida', 'Bebida')
        precio: precio en unidades monetarias
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = float(precio)

    def mostrar_informacion(self) -> str:
        """Devuelve una representación legible del producto.

        Este método puede ser sobrescrito por clases hijas pero su contrato
        (devolver una cadena con la información) se mantiene.
        """
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )

