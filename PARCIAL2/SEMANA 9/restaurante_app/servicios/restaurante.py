from typing import List, Optional, Dict, Set
from ..modelos.producto import Producto
from ..modelos.usuario import Usuario


class Restaurante:
    """Servicio que administra colecciones de productos y usuarios.

    - Usa listas para almacenar las colecciones dinámicas (_productos, _usuarios).
    - Proporciona métodos para registrar, buscar, actualizar, eliminar y listar.
    - Permite exportar una representación tipo dict de los datos (requisito)
    - Proporciona método para obtener categorías únicas mediante set.
    """

    def __init__(self) -> None:
        # Colecciones dinámicas: listas de objetos
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # ---------- Productos ----------
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si no existe otro con el mismo código."""
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self) -> List[str]:
        return [p.mostrar_informacion() for p in self._productos]

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

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
                return True
        return False

    # ---------- Usuarios ----------
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario_por_id(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[str]:
        return [u.mostrar_informacion() for u in self._usuarios]

    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    # ---------- Estructuras auxiliares ----------
    def obtener_categorias_unicas(self) -> Set[str]:
        """Devuelve un conjunto con las categorías únicas de los productos."""
        return set(p.categoria for p in self._productos)

    def exportar_datos_dict(self) -> Dict[str, object]:
        """Exporta los datos del servicio en una estructura tipo dict.

        La estructura tiene la siguiente forma:
        {
            "productos": { codigo: {..producto..}, ... },
            "usuarios": { identificacion: {..usuario..}, ... }
        }

        Este diccionario sirve para inspección o para uso interno cuando se
        requiere una relación clave->valor de los datos (requisito de la tarea).
        """
        productos_dict: Dict[str, Dict[str, object]] = {}
        for p in self._productos:
            productos_dict[p.codigo] = p.to_dict()

        usuarios_dict: Dict[str, Dict[str, str]] = {}
        for u in self._usuarios:
            usuarios_dict[u.identificacion] = u.to_dict()

        return {"productos": productos_dict, "usuarios": usuarios_dict}

