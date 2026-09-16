class Producto:
    def __init__(self, id, nombre, precio, cantidad, descripcion=""):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.cantidad})"
    
    def __repr__(self):
        return f"Producto({self.id}, {self.nombre}, ${self.precio}, Stock: {self.cantidad})"
