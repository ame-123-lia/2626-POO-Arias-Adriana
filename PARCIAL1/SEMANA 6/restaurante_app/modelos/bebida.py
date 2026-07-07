"""
Módulo: bebida
Contiene la clase Bebida que hereda de Producto e incluye atributos específicos.
"""
from .producto import Producto


class Bebida(Producto):
    """Representa una bebida del restaurante.

    Atributos adicionales:
        volumen_ml (int): volumen en mililitros
        tipo (str): categoría de la bebida (ej. Gaseosa, Natural, Caliente)
    """

    def __init__(self, nombre: str, precio: float, volumen_ml: int, tipo: str, disponible: bool = True):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml
        self.tipo = tipo

    def mostrar_informacion(self) -> str:
        """Sobrescribe mostrar_informacion para incluir datos de la bebida.

        Incluye volumen y categoría/tipo.
        """
        base = super().mostrar_informacion()
        return (
            f"{base} | Tipo: Bebida | Volumen: {self.volumen_ml} ml | "
            f"Categoría: {self.tipo}"
        )

    def informacion_pedagogica(self) -> str:
        """Información didáctica específica para Bebida."""
        return (
            "Bebida hereda de Producto -> reutiliza nombre, precio y disponibilidad; "
            f"añade volumen_ml y tipo. Clase: {self.__class__.__name__}."
        )

