from typing import List, Optional

try:
    # Cuando se importa como paquete
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
except ImportError:
    # Cuando se ejecuta directamente
    from modelos.producto import Producto
    from modelos.usuario import Usuario


class Restaurante:
    """
    Servicio que administra las colecciones de productos y usuarios.
    
    Responsabilidades:
        - Gestionar el registro, búsqueda, actualización y eliminación de productos
        - Mantener el registro de usuarios
        - Proporcionar operaciones de venta (descontar stock)
        - Exponer métodos para acceder a las colecciones
    """

    def __init__(self) -> None:
        """Inicializa el restaurante con colecciones vacías."""
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # ==================== MÉTODOS DE PRODUCTOS ====================

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un nuevo producto si no existe uno con el mismo código.
        
        Args:
            producto: instancia de Producto a registrar
            
        Returns:
            True si se registró correctamente, False si ya existe
        """
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """
        Busca un producto por su código.
        
        Args:
            codigo: código del producto a buscar
            
        Returns:
            Instancia de Producto si existe, None en caso contrario
        """
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(
        self, 
        codigo: str, 
        nombre: Optional[str] = None, 
        categoria: Optional[str] = None, 
        precio: Optional[float] = None
    ) -> bool:
        """
        Actualiza los datos de un producto existente.
        
        Args:
            codigo: código del producto a actualizar
            nombre: nuevo nombre (opcional)
            categoria: nueva categoría (opcional)
            precio: nuevo precio (opcional)
            
        Returns:
            True si se actualizó correctamente, False si no existe el producto
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False
        
        if nombre is not None:
            producto.nombre = str(nombre).strip()
        if categoria is not None:
            producto.categoria = str(categoria).strip()
        if precio is not None:
            producto.precio = float(precio)
        
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """
        Elimina un producto del catálogo.
        
        Args:
            codigo: código del producto a eliminar
            
        Returns:
            True si se eliminó correctamente, False si no existe
        """
        for i, producto in enumerate(self._productos):
            if producto.codigo == codigo:
                self._productos.pop(i)
                return True
        return False

    def listar_productos(self) -> List[str]:
        """
        Retorna una lista de representaciones textuales de todos los productos.
        
        Returns:
            Lista de strings con información de cada producto
        """
        return [p.mostrar_informacion() for p in self._productos]

    def obtener_productos_como_lista(self) -> List[Producto]:
        """
        Retorna la lista interna de productos.
        
        Returns:
            Lista de objetos Producto
        """
        return self._productos

    # ==================== MÉTODOS DE USUARIOS ====================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra un nuevo usuario si no existe uno con la misma identificación.
        
        Args:
            usuario: instancia de Usuario a registrar
            
        Returns:
            True si se registró correctamente, False si ya existe
        """
        if self.buscar_usuario_por_id(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        """
        Busca un usuario por su identificación.
        
        Args:
            identificacion: identificación del usuario
            
        Returns:
            Instancia de Usuario si existe, None en caso contrario
        """
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def listar_usuarios(self) -> List[str]:
        """
        Retorna una lista de representaciones textuales de todos los usuarios.
        
        Returns:
            Lista de strings con información de cada usuario
        """
        return [u.mostrar_informacion() for u in self._usuarios]

    # ==================== MÉTODOS DE VENTAS ====================

    def vender_producto(self, codigo_producto: str, cantidad: int) -> bool:
        """
        Realiza una venta descontando stock del producto.
        
        Args:
            codigo_producto: código del producto a vender
            cantidad: cantidad a vender
            
        Returns:
            True si la venta se realizó correctamente, False en caso contrario
        """
        producto = self.buscar_producto_por_codigo(codigo_producto)
        if producto is None:
            return False
        
        try:
            producto.vender(cantidad)
            return True
        except ValueError:
            return False
