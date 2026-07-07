from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def listar_productos(self) -> List[Producto]:
        return self.productos

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        nombre_buscado = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_buscado:
                return producto
        return None

    def registrar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def listar_clientes(self) -> List[Cliente]:
        return self.clientes

    def buscar_cliente(self, nombre: str) -> Optional[Cliente]:
        nombre_buscado = nombre.strip().lower()
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre_buscado:
                return cliente
        return None
