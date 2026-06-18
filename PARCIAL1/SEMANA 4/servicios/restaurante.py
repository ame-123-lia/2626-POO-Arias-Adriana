class Restaurante:
    """
    Clase de servicio que gestiona el menú de productos y los clientes activos.
    """

    def __init__(self, nombre_restaurante):
        self.nombre_restaurante = nombre_restaurante
        self.menu_productos = []  # Lista para almacenar objetos Producto
        self.clientes_activos = []  # Lista para almacenar objetos Cliente

    def agregar_producto(self, producto):
        """Agrega un plato o bebida al menú."""
        self.menu_productos.append(producto)
        print(f"✔ Producto '{producto.nombre}' agregado al menú.")

    def registrar_cliente(self, cliente):
        """Registra un cliente en una mesa."""
        self.clientes_activos.append(cliente)
        print(f"✔ Cliente '{cliente.nombre}' registrado en la mesa {cliente.mesa}.")

    def mostrar_informacion_general(self):
        """Muestra todo el estado actual del restaurante de forma organizada."""
        print(f"\n=========================================")
        print(f"      SISTEMA DE GESTIÓN: {self.nombre_restaurante.upper()}      ")
        print(f"=========================================")

        # Recorrer y mostrar el menú
        print("\n--- MENÚ DEL DÍA ---")
        if not self.menu_productos:
            print("No hay productos en el menú.")
        else:
            for prod in self.menu_productos:
                print(f" * {prod}")

        # Recorrer y mostrar los clientes
        print("\n--- CLIENTES EN SALA ---")
        if not self.clientes_activos:
            print("No hay clientes en este momento.")
        else:
            for cli in self.clientes_activos:
                print(f" * {cli}")
        print("=========================================\n")