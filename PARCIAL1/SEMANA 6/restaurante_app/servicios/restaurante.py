"""
Módulo de servicios: restaurante
Contiene la clase Restaurante que administra una lista de productos.
"""

class Restaurante:
    """Clase de servicio que administra productos del restaurante."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos = []  # lista para almacenar objetos Producto (Platillo/Bebida)

    def agregar_producto(self, producto):
        """Agrega un producto a la lista si tiene el método mostrar_informacion.

        Se valida de forma simple que el objeto sea compatible (polimorfismo por método).
        """
        if not hasattr(producto, "mostrar_informacion"):
            raise TypeError("El objeto no es un producto válido")
        self.productos.append(producto)

    def listar_productos(self):
        """Muestra en consola la información de todos los productos.

        Aquí se evidencia el polimorfismo: cada objeto devuelve su propia descripción
        al llamar al mismo método mostrar_informacion().
        """
        print(f"--- Productos registrados en {self.nombre} ---")
        if not self.productos:
            print("No hay productos registrados.")
            return
        for i, p in enumerate(self.productos, start=1):
            print(f"{i}. {p.mostrar_informacion()}")

