"""
Módulo: platillo
Contiene la clase Platillo que hereda de Producto e incluye atributos específicos.
"""
from .producto import Producto


class Platillo(Producto):
    """Representa un platillo (comida) del restaurante.

    Atributos adicionales:
        calorias (int): energía aproximada en kcal
        tiempo_preparacion (int): minutos de preparación
    """

    def __init__(self, nombre: str, precio: float, calorias: int, tiempo_preparacion: int, disponible: bool = True):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self) -> str:
        """Sobrescribe mostrar_informacion para incluir datos de platillo."""
        base = super().mostrar_informacion()
        return f"{base} | Tipo: Platillo | Calorías: {self.calorias} kcal | Tiempo prep: {self.tiempo_preparacion} min"

