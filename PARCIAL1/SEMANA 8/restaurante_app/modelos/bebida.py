from .producto import Producto


class Bebida(Producto):
    """Clase que representa una bebida. Es una especialización de Producto.

    Añade atributos específicos como tamaño y tipo de envase.
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, envase: str) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano: str = tamano
        self.envase: str = envase

    def mostrar_informacion(self) -> str:
        """Sobrescribe mostrar_informacion para incluir datos de bebida.

        Mantiene la misma firma que en Producto para cumplir LSP.
        """
        base = super().mostrar_informacion()
        return f"{base} | Tamaño: {self.tamano} | Envase: {self.envase}"

