from typing import Dict, Any


class Producto:
    """
    Clase que representa un producto del restaurante.
    
    Atributos:
        codigo: str - identificador único
        nombre: str - nombre del producto
        categoria: str - categoría del producto
        precio: float - precio unitario
        stock: int - cantidad disponible
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        """
        Inicializa un producto con validaciones.
        
        Args:
            codigo: identificador único
            nombre: nombre del producto
            categoria: categoría del producto
            precio: precio unitario (debe ser no negativo)
            stock: cantidad disponible (por defecto 0)
            
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
        
        try:
            self.stock: int = int(stock)
        except (TypeError, ValueError) as e:
            raise ValueError("El stock debe ser un número entero válido") from e

        # Validaciones de integridad
        if not self.codigo:
            raise ValueError("El código no puede estar vacío")
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")

    def mostrar_informacion(self) -> str:
        """Retorna una representación legible del producto."""
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Stock: {self.stock}"
        )

    def vender(self, cantidad: int) -> None:
        """
        Disminuye el stock disponible.
        
        Args:
            cantidad: cantidad a vender
            
        Raises:
            ValueError: si la cantidad es inválida o hay stock insuficiente
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad

    def to_dict(self) -> Dict[str, Any]:
        """
        Convierte el producto a un diccionario compatible con JSON.
        
        Returns:
            Diccionario con los atributos del producto
        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Producto":
        """
        Reconstruye un Producto a partir de un diccionario.
        
        Args:
            data: diccionario con los datos del producto
            
        Returns:
            Nueva instancia de Producto
            
        Raises:
            KeyError: si faltan claves esperadas
            ValueError: si los datos son inválidos
        """
        try:
            codigo = data["codigo"]
            nombre = data["nombre"]
            categoria = data["categoria"]
            precio = data["precio"]
            stock = data.get("stock", 0)
        except KeyError as e:
            raise KeyError(f"Falta la clave esperada: {e}") from e
        
        return cls(codigo, nombre, categoria, precio, stock)
