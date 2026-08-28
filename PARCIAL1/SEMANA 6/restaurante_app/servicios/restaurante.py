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
        """Muestra en consola la información de todos los productos con explicación didáctica.

        Por cada producto se muestra:
        - la representación (polimorfismo: cada subclase provee su propia descripción)
        - la clase concreta del objeto
        - demostración de encapsulación (acceso al precio mediante el getter)
        - una breve explicación pedagógica proporcionada por cada objeto
        """
        print(f"--- Productos registrados en {self.nombre} ---")
        if not self.productos:
            print("No hay productos registrados.")
            return

        for i, p in enumerate(self.productos, start=1):
            print(f"\nProducto #{i}")
            # Polimorfismo: cada objeto responde con su propia información
            print("Descripción:", p.mostrar_informacion())

            # Información sobre la clase y la jerarquía (herencia)
            clase_real = p.__class__.__name__
            mro_names = [c.__name__ for c in p.__class__.__mro__]
            pertenece_producto = 'Producto' in mro_names
            print(f"Clase concreta: {clase_real}")
            print(f"Jerarquía (MRO): {mro_names}")
            print(f"¿Pertenece a la jerarquía Producto? {'Sí' if pertenece_producto else 'No'}")

            # Encapsulación: intentar acceder directamente al atributo __precio
            try:
                precio_directo = getattr(p, '__precio')
                acceso_directo = True
            except Exception:
                precio_directo = None
                acceso_directo = False

            if acceso_directo:
                print("Acceso directo a __precio:", precio_directo, "(no recomendado)")
            else:
                print("Acceso directo a __precio: no permitido (encapsulación)")
                # mostrar precio mediante el método (correcto)
                try:
                            print(f"Precio (obtenido con getter): USD {p.obtener_precio():.2f}")
                except Exception:
                    print("Precio: no disponible")

            # Información pedagógica ofrecida por el propio objeto (si existe)
            if hasattr(p, 'informacion_pedagogica'):
                print("Nota pedagógica:", p.informacion_pedagogica())
            else:
                print("Nota pedagógica: Este producto hereda de Producto y puede sobrescribir métodos.")

            # Pequeña explicación sobre polimorfismo
            print("Polimorfismo: al llamar a 'mostrar_informacion()' se ejecuta la versión"
                  " definida en la clase concreta del objeto.")

