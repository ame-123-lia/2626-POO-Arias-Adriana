class Producto:
    """
    Clase que representa un producto (plato o bebida) dentro del restaurante.
    """
    def __init__(self, nombre, precio, categoria):
        # Atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # Ejemplo: 'Plato Fuerte', 'Bebida'

    def __str__(self):
        # Define cómo se mostrará el producto en texto
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f}"