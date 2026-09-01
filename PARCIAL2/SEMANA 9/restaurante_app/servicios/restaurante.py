from typing import List, Optional, Set

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
    
    Utiliza estructuras de datos:
    - LIST: Para almacenar productos y usuarios (colecciones dinámicas)
    - TUPLE: Para opciones estables del menú
    - DICT: Para mapear códigos a objetos (búsqueda rápida)
    - SET: Para obtener categorías únicas sin duplicados
    
    Responsabilidades:
        - Gestionar el registro, búsqueda, actualización y eliminación de productos
        - Mantener el registro de usuarios
        - Proporcionar operaciones de consulta sobre datos
    """

    def __init__(self) -> None:
        """Inicializa el restaurante con colecciones vacías."""
        # LIST: Colecciones dinámicas de objetos
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

    def obtener_categorias_unicas(self) -> Set[str]:
        """
        Retorna un conjunto de categorías únicas de los productos.
        
        ESTRUCTURA: SET
        Uso: Elimina automáticamente duplicados de categorías
        Beneficio: No hay necesidad de verificar manualmente si una categoría ya existe
        
        Returns:
            Conjunto (set) con las categorías únicas
        """
        return {producto.categoria for producto in self._productos}

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

    # ==================== MÉTODOS DE CONSULTA ====================

    def obtener_cantidad_productos(self) -> int:
        """Retorna la cantidad total de productos."""
        return len(self._productos)

    def obtener_cantidad_usuarios(self) -> int:
        """Retorna la cantidad total de usuarios."""
        return len(self._usuarios)

    def obtener_productos_como_lista(self) -> List[Producto]:
        """Retorna la lista interna de productos (para consulta)."""
        return self._productos
