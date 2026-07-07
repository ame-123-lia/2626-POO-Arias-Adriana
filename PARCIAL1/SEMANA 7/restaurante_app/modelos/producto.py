class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        valor = valor.strip()
        if not valor:
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        valor = valor.strip()
        if not valor:
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número válido.")
        if valor <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = valor

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool) -> None:
        self._disponible = bool(valor)

    def mostrar_informacion(self) -> str:
        estado = "Sí" if self.disponible else "No"
        return (
            f"Producto: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Disponible: {estado}"
        )
