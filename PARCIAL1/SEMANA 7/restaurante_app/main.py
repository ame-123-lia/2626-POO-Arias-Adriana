from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")


def solicitar_producto() -> Producto:
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría del producto: ").strip()
    precio_texto = input("Ingrese el precio del producto: ").strip()
    disponible_texto = input("¿Está disponible? (s/n): ").strip().lower()
    disponible = disponible_texto == "s"
    return Producto(nombre=nombre, categoria=categoria, precio=precio_texto, disponible=disponible)


def solicitar_cliente() -> Cliente:
    nombre = input("Ingrese el nombre del cliente: ").strip()
    correo = input("Ingrese el correo del cliente: ").strip()
    id_cliente = input("Ingrese el identificador del cliente: ").strip()
    return Cliente(nombre=nombre, correo=correo, id_cliente=id_cliente)


def registrar_producto(restaurante: Restaurante) -> None:
    try:
        producto = solicitar_producto()
        restaurante.registrar_producto(producto)
        print("Producto registrado correctamente.\n")
    except ValueError as error:
        print(f"Error al registrar el producto: {error}\n")


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.\n")
        return
    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. {producto.mostrar_informacion()}")
        print("----------------------------------------")
    print()


def buscar_producto(restaurante: Restaurante) -> None:
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(nombre)
    if producto:
        print("Producto encontrado:")
        print(producto.mostrar_informacion())
    else:
        print("No se encontró ningún producto con ese nombre.")
    print()


def registrar_cliente(restaurante: Restaurante) -> None:
    try:
        cliente = solicitar_cliente()
        restaurante.registrar_cliente(cliente)
        print("Cliente registrado correctamente.\n")
    except ValueError as error:
        print(f"Error al registrar el cliente: {error}\n")


def listar_clientes(restaurante: Restaurante) -> None:
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. Nombre: {cliente.nombre}")
        print(f"   Correo: {cliente.correo}")
        print(f"   ID: {cliente.id_cliente}")
        print("----------------------------------------")
    print()


def buscar_cliente(restaurante: Restaurante) -> None:
    nombre = input("Ingrese el nombre del cliente a buscar: ").strip()
    cliente = restaurante.buscar_cliente(nombre)
    if cliente:
        print("Cliente encontrado:")
        print(f"Nombre: {cliente.nombre}")
        print(f"Correo: {cliente.correo}")
        print(f"ID: {cliente.id_cliente}")
    else:
        print("No se encontró ningún cliente con ese nombre.")
    print()


def ejecutar_sistema() -> None:
    restaurante = Restaurante()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        print()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.\n")


if __name__ == "__main__":
    ejecutar_sistema()
