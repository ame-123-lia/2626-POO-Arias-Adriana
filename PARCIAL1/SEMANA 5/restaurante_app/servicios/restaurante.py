"""
Módulo de la clase Restaurante
Define la estructura del servicio que administra productos y clientes
"""

from typing import List
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.cliente import Cliente


class Restaurante:
    """
    Representa el servicio principal que gestiona un restaurante.
    Administra listas de productos disponibles y clientes registrados.

    Atributos:
        nombre (str): Nombre del restaurante
        lista_productos (List[Producto]): Lista que almacena todos los productos
        lista_clientes (List[Cliente]): Lista que almacena todos los clientes
        año_fundacion (int): Año en que fue fundado el restaurante
    """

    def __init__(self, nombre: str, año_fundacion: int) -> None:
        """
        Constructor que inicializa un objeto Restaurante.

        Args:
            nombre: Nombre del restaurante
            año_fundacion: Año de fundación del restaurante
        """
        self.nombre: str = nombre
        self.lista_productos: List[Producto] = []
        self.lista_clientes: List[Cliente] = []
        self.año_fundacion: int = año_fundacion

    def __str__(self) -> str:
        """
        Retorna información general del restaurante.

        Returns:
            str: Información formateada del restaurante
        """
        return (
            f"Restaurante: {self.nombre}\n"
            f"  Fundado: {self.año_fundacion}\n"
            f"  Productos en menú: {len(self.lista_productos)}\n"
            f"  Clientes registrados: {len(self.lista_clientes)}"
        )

    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un nuevo producto a la lista del restaurante.

        Args:
            producto: Objeto Producto a agregar
        """
        self.lista_productos.append(producto)
        print(f"[OK] Producto '{producto.nombre}' agregado al menu.")

    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Registra un nuevo cliente en el sistema del restaurante.

        Args:
            cliente: Objeto Cliente a registrar
        """
        self.lista_clientes.append(cliente)
        print(f"[OK] Cliente '{cliente.nombre}' registrado en el sistema.")

    def listar_productos(self) -> None:
        """
        Imprime en consola la lista de todos los productos disponibles.
        """
        print("\n" + "="*60)
        print(f"MENU DE {self.nombre.upper()}")
        print("="*60)

        if not self.lista_productos:
            print("No hay productos disponibles en el menu.")
        else:
            for indice, producto in enumerate(self.lista_productos, start=1):
                print(f"\n[Producto {indice}]")
                print(producto)

        print("="*60 + "\n")

    def listar_clientes(self) -> None:
        """
        Imprime en consola la lista de todos los clientes registrados.
        """
        print("\n" + "="*60)
        print(f"CLIENTES REGISTRADOS EN {self.nombre.upper()}")
        print("="*60)

        if not self.lista_clientes:
            print("No hay clientes registrados.")
        else:
            for indice, cliente in enumerate(self.lista_clientes, start=1):
                print(f"\n[Cliente {indice}]")
                print(cliente)

        print("="*60 + "\n")

    def obtener_total_productos(self) -> int:
        """
        Retorna la cantidad total de productos en el menú.

        Returns:
            int: Número de productos disponibles
        """
        return len(self.lista_productos)

    def obtener_total_clientes(self) -> int:
        """
        Retorna la cantidad total de clientes registrados.

        Returns:
            int: Número de clientes en el sistema
        """
        return len(self.lista_clientes)

    def buscar_producto_por_nombre(self, nombre: str) -> Producto | None:
        """
        Busca un producto por su nombre en el menú.

        Args:
            nombre: Nombre del producto a buscar

        Returns:
            Producto si lo encuentra, None en caso contrario
        """
        for producto in self.lista_productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def buscar_cliente_por_nombre(self, nombre: str) -> Cliente | None:
        """
        Busca un cliente por su nombre en el sistema.

        Args:
            nombre: Nombre del cliente a buscar

        Returns:
            Cliente si lo encuentra, None en caso contrario
        """
        for cliente in self.lista_clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None

    def mostrar_resumen(self) -> None:
        """
        Imprime un resumen general del restaurante.
        """
        print("\n" + "="*60)
        print("RESUMEN DEL RESTAURANTE")
        print("="*60)
        print(self)
        print("="*60 + "\n")


