"""
Módulo: producto
Contiene la clase padre Producto con atributos comunes y protección de precio mediante encapsulación.
"""
class Producto:
    """Clase padre que representa un producto general del restaurante.

    Atributos:
        nombre (str): nombre del producto
        __precio (float): precio protegido (encapsulado)
        disponible (bool): indica si el producto está disponible
    """

    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        # atributo protegido: nunca asignar directamente sin validación
        self.__precio = 0.0
        # usar el método para validar y asignar el precio
        self.cambiar_precio(precio)
        self.disponible = disponible

    def obtener_precio(self) -> float:
        """Retorna el precio actual del producto."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """Valida y cambia el precio. El precio debe ser numérico y mayor que cero.

        Lanza ValueError en caso de valor inválido.
        """
        if not isinstance(nuevo_precio, (int, float)):
            raise ValueError("El precio debe ser un número.")
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = float(nuevo_precio)

    def mostrar_informacion(self) -> str:
        """Devuelve una representación textual genérica del producto.

        Usamos el getter para acceder al precio (ejemplo de encapsulación).
        """
        dispo = "Sí" if self.disponible else "No"
        return (
            f"Producto: {self.nombre} | Precio: USD {self.obtener_precio():.2f} | "
            f"Disponible: {dispo}"
        )

    def informacion_pedagogica(self) -> str:
        """Devuelve una cadena con información didáctica sobre POO aplicada.

        Indica la clase del objeto, que el precio está encapsulado y el método
        usado para acceder al precio.
        """
        return (
            f"Clase real: {self.__class__.__name__} | "
            f"Atributo encapsulado: __precio (acceso mediante obtener_precio())"
        )

