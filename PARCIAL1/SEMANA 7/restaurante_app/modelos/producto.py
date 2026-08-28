class Producto:
    """
    Clase que representa un Producto del restaurante.

    Demuestra:
    - ENCAPSULACIÓN: Los atributos son privados (_nombre, _categoria, etc.)
    - PROPERTIES: Usado getters y setters para validar datos
    - VALIDACIÓN: Se valida cada atributo al ser asignado

    Principio: "No confiar en el usuario" - siempre validar entrada.
    """

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        """Inicializa un producto con validación de todos sus atributos."""
        # Los setters automáticamente validan los datos
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self) -> str:
        """
        GETTER: Obtiene el nombre del producto.
        Demostración de ENCAPSULACIÓN: el usuario accede via propiedad.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """
        SETTER: Valida y asigna el nombre.
        VALIDACIÓN: Garantiza que el nombre no sea vacío.
        """
        valor = valor.strip()
        if not valor:
            raise ValueError("❌ El nombre del producto no puede estar vacío.")
        self._nombre = valor
        print(f"✓ Nombre asignado correctamente: {self._nombre}")

    @property
    def categoria(self) -> str:
        """GETTER: Obtiene la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        """SETTER: Valida y asigna la categoría."""
        valor = valor.strip()
        if not valor:
            raise ValueError("❌ La categoría del producto no puede estar vacía.")
        self._categoria = valor
        print(f"✓ Categoría asignada correctamente: {self._categoria}")

    @property
    def precio(self) -> float:
        """GETTER: Obtiene el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        """
        SETTER: Valida y asigna el precio.
        VALIDACIÓN: Convierte a float y verifica que sea > 0.
        """
        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise ValueError("❌ El precio debe ser un número válido.")
        if valor <= 0:
            raise ValueError("❌ El precio del producto debe ser mayor que cero.")
        self._precio = valor
        print(f"✓ Precio asignado correctamente: ${self._precio:.2f}")

    @property
    def disponible(self) -> bool:
        """GETTER: Obtiene si el producto está disponible."""
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool) -> None:
        """SETTER: Convierte y asigna el estado de disponibilidad."""
        self._disponible = bool(valor)

    def mostrar_informacion(self) -> str:
        """Devuelve una representación legible del producto."""
        estado = "✓ Sí" if self.disponible else "✗ No"
        return (
            f"Producto: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Disponible: {estado}"
        )

    def info_pedagogica(self) -> str:
        """
        Información educativa sobre los principios de POO aplicados.
        Muestra cómo se implementa la ENCAPSULACIÓN en esta clase.
        """
        return (
            f"\n📚 LECCIÓN DE POO APLICADA EN '{self.nombre}':\n"
            f"  • Clase: {self.__class__.__name__}\n"
            f"  • Encapsulación: Los atributos reales son _nombre, _categoria, _precio, _disponible\n"
            f"  • Acceso controlado: Se usa @property para leer y @setter para validar\n"
            f"  • Validación: Cada atributo es validado antes de ser asignado\n"
            f"  • Beneficio: El objeto siempre está en un estado válido"
        )
