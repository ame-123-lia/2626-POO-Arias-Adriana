class Cliente:
    """
    Clase que representa a un cliente del restaurante.
    """
    def __init__(self, nombre, cedula, mesa):
        # Atributos del cliente
        self.nombre = nombre
        self.cedula = cedula
        self.mesa = mesa

    def __str__(self):
        # Define cómo se mostrará el cliente en texto
        return f"Cliente: {self.nombre} | C.I.: {self.cedula} | Mesa: {self.mesa}"