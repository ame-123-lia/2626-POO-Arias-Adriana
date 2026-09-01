class Producto:
    """
    Clase que representa un producto del restaurante.
    
    Atributos:
        codigo: str - identificador único del producto
        nombre: str - nombre del producto
        categoria: str - categoría del producto
        precio: float - precio unitario del producto
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        """
        Inicializa un producto con validaciones.
        
        Args:
            codigo: identificador único
            nombre: nombre del producto
            categoria: categoría del producto
            precio: precio unitario
            
        Raises:
            ValueError: si algún parámetro es inválido
        """
        self.codigo: str = str(codigo).strip()
        self.nombre: str = str(nombre).strip()
        self.categoria: str = str(categoria).strip()
        
        try:
            self.precio: float = float(precio)
        except (TypeError, ValueError) as e:
            raise ValueError("El precio debe ser un número válido") from e

        # Validaciones de integridad
        if not self.codigo:
            raise ValueError("El código no puede estar vacío")
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")

    def mostrar_informacion(self) -> str:
        """Retorna una representación legible del producto."""
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )

    def __str__(self) -> str:
        """Representación en string del producto."""
        return self.mostrar_informacion()

    def __repr__(self) -> str:
        """Representación técnica del producto."""
        return f"Producto({self.codigo!r}, {self.nombre!r}, {self.categoria!r}, {self.precio!r})"
