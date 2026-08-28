from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """
    Clase Restaurante que demuestra:
    - RESPONSABILIDAD ÚNICA: Gestiona productos y clientes (lógica de negocio)
    - TYPE HINTS: Uso de tipos para mayor claridad
    - MÉTODOS REUTILIZABLES: Búsqueda, agregar, listar

    Patrón: Contenedor/Gestor que maneja colecciones de objetos.
    """

    def __init__(self, nombre: str = "Mi Restaurante"):
        """Inicializa el restaurante con listas vacías de productos y clientes."""
        self.nombre = nombre
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []
        print(f"🍽️  Restaurante '{self.nombre}' inicializado\n")

    # ========== MÉTODOS PARA PRODUCTOS ==========

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un nuevo producto en el restaurante."""
        self.productos.append(producto)
        print(f"✓ Producto '{producto.nombre}' registrado\n")

    def listar_productos(self) -> List[Producto]:
        """Devuelve la lista de todos los productos."""
        return self.productos

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        """
        Busca un producto por nombre (insensible a mayúsculas/minúsculas).

        Devuelve: el Producto encontrado o None si no existe.
        """
        nombre_buscado = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_buscado:
                return producto
        return None

    def obtener_productos_por_categoria(self, categoria: str) -> List[Producto]:
        """Devuelve todos los productos de una categoría específica."""
        categoria_buscada = categoria.strip().lower()
        return [p for p in self.productos
                if p.categoria.lower() == categoria_buscada]

    def obtener_productos_disponibles(self) -> List[Producto]:
        """Devuelve solo los productos disponibles."""
        return [p for p in self.productos if p.disponible]

    # ========== MÉTODOS PARA CLIENTES ==========

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un nuevo cliente en el restaurante."""
        self.clientes.append(cliente)
        print(f"✓ Cliente '{cliente.nombre}' registrado\n")

    def listar_clientes(self) -> List[Cliente]:
        """Devuelve la lista de todos los clientes."""
        return self.clientes

    def buscar_cliente(self, nombre: str) -> Optional[Cliente]:
        """
        Busca un cliente por nombre (insensible a mayúsculas/minúsculas).

        Devuelve: el Cliente encontrado o None si no existe.
        """
        nombre_buscado = nombre.strip().lower()
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre_buscado:
                return cliente
        return None

    # ========== MÉTODOS ESTADÍSTICOS ==========

    def obtener_estadisticas(self) -> dict:
        """Devuelve estadísticas del restaurante."""
        total_productos = len(self.productos)
        productos_disponibles = len(self.obtener_productos_disponibles())
        total_clientes = len(self.clientes)

        precio_promedio = 0
        if total_productos > 0:
            suma_precios = sum(p.precio for p in self.productos)
            precio_promedio = suma_precios / total_productos

        return {
            "total_productos": total_productos,
            "productos_disponibles": productos_disponibles,
            "total_clientes": total_clientes,
            "precio_promedio": precio_promedio
        }

    def mostrar_resumen(self) -> None:
        """Muestra un resumen del estado del restaurante."""
        stats = self.obtener_estadisticas()
        print("\n" + "="*50)
        print(f"📊 RESUMEN DEL RESTAURANTE: {self.nombre}")
        print("="*50)
        print(f"Total de productos: {stats['total_productos']}")
        print(f"Productos disponibles: {stats['productos_disponibles']}")
        print(f"Total de clientes: {stats['total_clientes']}")
        if stats['precio_promedio'] > 0:
            print(f"Precio promedio de productos: ${stats['precio_promedio']:.2f}")
        print("="*50 + "\n")


