"""
Módulo de la clase Producto
Define la estructura de un producto disponible en el restaurante
"""


class Producto:
    """
    Representa un producto (plato, bebida, etc.) disponible en el restaurante.

    Atributos:
        nombre (str): Nombre descriptivo del producto
        descripcion (str): Descripción detallada del producto
        precio (float): Precio en dólares del producto
        cantidad_disponible (int): Cantidad en stock del producto
        es_vegetariano (bool): Indica si el producto es vegetariano
    """

    def __init__(
        self,
        nombre: str,
        descripcion: str,
        precio: float,
        cantidad_disponible: int,
        es_vegetariano: bool
    ) -> None:
        """
        Constructor que inicializa un objeto Producto con sus atributos.

        Args:
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio del producto
            cantidad_disponible: Cantidad inicial en inventario
            es_vegetariano: Valor booleano indicando si es vegetariano
        """
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.cantidad_disponible: int = cantidad_disponible
        self.es_vegetariano: bool = es_vegetariano

    def __str__(self) -> str:
        """
        Retorna una representacion en texto del producto.
        
        Returns:
            str: Informacion formateada del producto
        """
        tipo_comida = "Vegetariano" if self.es_vegetariano else "Con proteina animal"
        return (
            f"Producto: {self.nombre}\n"
            f"  Descripcion: {self.descripcion}\n"
            f"  Precio: ${self.precio:.2f}\n"
            f"  En stock: {self.cantidad_disponible} unidades\n"
            f"  Tipo: {tipo_comida}"
        )

    def mostrar_detalles(self) -> None:
        """
        Imprime los detalles completos del producto en consola.
        """
        print(self)

    def actualizar_cantidad(self, cantidad: int) -> None:
        """
        Actualiza la cantidad disponible del producto.

        Args:
            cantidad: Nueva cantidad a sumar o restar del inventario
        """
        self.cantidad_disponible += cantidad
        print(f"Stock actualizado para {self.nombre}. Cantidad actual: {self.cantidad_disponible}")

    def obtener_disponibilidad(self) -> bool:
        """
        Verifica si el producto está disponible en stock.

        Returns:
            bool: True si hay stock, False caso contrario
        """
        return self.cantidad_disponible > 0

