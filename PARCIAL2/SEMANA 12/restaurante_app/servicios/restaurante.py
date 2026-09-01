from typing import List, Optional, Dict, Set
try:
    # cuando se importa como paquete
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
    from ..modelos.venta import Venta
except Exception:
    # cuando se ejecuta dentro del directorio como script
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta


class Restaurante:
    """Servicio que administra colecciones de productos, usuarios y ventas.

    Mantiene la lógica de negocio (registro, búsqueda, actualización, eliminación y ventas)
    y provee métodos auxiliares para exportar/recuperar datos en formato dict.
    """

    def __init__(self) -> None:
        # Colecciones dinámicas: listas de objetos
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []
        
        # Índices auxiliares para búsquedas O(1)
        self._productos_index: Dict[str, Producto] = {}
        self._usuarios_index: Dict[str, Usuario] = {}
        self._ventas_por_usuario: Dict[str, List[Venta]] = {}

    # ---------- Productos ----------
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si no existe otro con el mismo código."""
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        self._productos_index[producto.codigo] = producto
        return True

    def listar_productos(self) -> List[str]:
        return [p.mostrar_informacion() for p in self._productos]

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        return self._productos_index.get(codigo)

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None, categoria: Optional[str] = None, precio: Optional[float] = None) -> bool:
        """Actualiza campos de un producto identificado por su código. Devuelve True si se actualizó."""
        p = self.buscar_producto_por_codigo(codigo)
        if p is None:
            return False
        if nombre is not None:
            p.nombre = nombre
        if categoria is not None:
            p.categoria = categoria
        if precio is not None:
            p.precio = float(precio)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        for i, p in enumerate(self._productos):
            if p.codigo == codigo:
                del self._productos[i]
                if codigo in self._productos_index:
                    del self._productos_index[codigo]
                return True
        return False

    def cargar_productos(self, productos: List[Producto]) -> None:
        """Carga una lista de objetos Producto en el servicio."""
        for p in productos:
            try:
                self.registrar_producto(p)
            except Exception:
                continue

    def obtener_productos_como_lista(self) -> List[Dict[str, object]]:
        """Devuelve la colección de productos en forma de lista de dicts (apta para JSON)."""
        return [p.to_dict() for p in self._productos]

    # ---------- Usuarios ----------
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario_por_id(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        self._usuarios_index[usuario.identificacion] = usuario
        self._ventas_por_usuario[usuario.identificacion] = []
        return True

    def listar_usuarios(self) -> List[str]:
        return [u.mostrar_informacion() for u in self._usuarios]

    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        return self._usuarios_index.get(identificacion)

    def cargar_usuarios(self, usuarios: List[Usuario]) -> None:
        """Carga una lista de objetos Usuario en el servicio."""
        for u in usuarios:
            try:
                self.registrar_usuario(u)
            except Exception:
                continue

    def obtener_usuarios_como_lista(self) -> List[Dict[str, str]]:
        """Devuelve la colección de usuarios en forma de lista de dicts (apta para JSON)."""
        return [u.to_dict() for u in self._usuarios]

    # ---------- Ventas ----------
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        """Realiza una venta de un producto a un usuario.

        Validaciones:
        - Usuario existe
        - Producto existe
        - Cantidad es válida (> 0)
        - Stock disponible

        Devuelve True si la venta fue exitosa, False en caso contrario.
        """
        usuario = self.buscar_usuario_por_id(identificacion_usuario)
        producto = self.buscar_producto_por_codigo(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        self._ventas_por_usuario[usuario.identificacion].append(venta)
        producto.vender(cantidad)
        return True

    def obtener_ventas_usuario(self, identificacion_usuario: str) -> List[str]:
        """Obtiene las ventas realizadas por un usuario específico."""
        ventas_usuario = self._ventas_por_usuario.get(identificacion_usuario, [])
        return [v.mostrar_informacion() for v in ventas_usuario]

    def listar_todas_ventas(self) -> List[str]:
        """Lista todas las ventas registradas."""
        return [v.mostrar_informacion() for v in self._ventas]

    def obtener_ventas_como_lista(self) -> List[Dict[str, object]]:
        """Devuelve la colección de ventas en forma de lista de dicts (apta para JSON)."""
        return [v.to_dict() for v in self._ventas]

    def cargar_ventas(self, ventas: List[Venta]) -> None:
        """Carga una lista de objetos Venta en el servicio."""
        for v in ventas:
            try:
                self._ventas.append(v)
                if v.usuario_id in self._ventas_por_usuario:
                    self._ventas_por_usuario[v.usuario_id].append(v)
            except Exception:
                continue

    # ---------- Estructuras auxiliares ----------
    def obtener_categorias_unicas(self) -> Set[str]:
        """Devuelve un conjunto con las categorías únicas de los productos."""
        return set(p.categoria for p in self._productos)

    def exportar_datos_dict(self) -> Dict[str, object]:
        """Exporta los datos del servicio en una estructura tipo dict."""
        productos_dict: Dict[str, Dict[str, object]] = {}
        for p in self._productos:
            productos_dict[p.codigo] = p.to_dict()

        usuarios_dict: Dict[str, Dict[str, str]] = {}
        for u in self._usuarios:
            usuarios_dict[u.identificacion] = u.to_dict()

        return {"productos": productos_dict, "usuarios": usuarios_dict}


