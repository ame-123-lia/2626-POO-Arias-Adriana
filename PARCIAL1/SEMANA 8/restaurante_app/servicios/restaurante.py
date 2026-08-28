from typing import List, Optional
from ..modelos.producto import Producto
from ..modelos.cliente import Cliente


class Restaurante:
    """Servicio que administra productos y clientes del restaurante."""

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si su código no existe. Devuelve True si se agregó."""
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self) -> List[str]:
        """Devuelve una lista de cadenas con la información de cada producto.

        Usa polimorfismo: no pregunta el tipo concreto, sólo llama a mostrar_informacion().
        """
        return [p.mostrar_informacion() for p in self._productos]

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente si su identificación no existe. Devuelve True si se agregó."""
        if self.buscar_cliente_por_id(cliente.identificacion) is not None:
            return False
        self._clientes.append(cliente)
        return True

    def listar_clientes(self) -> List[str]:
        return [c.mostrar_informacion() for c in self._clientes]

    def buscar_cliente_por_id(self, identificacion: str) -> Optional[Cliente]:
        for c in self._clientes:
            if c.identificacion == identificacion:
                return c
        return None

