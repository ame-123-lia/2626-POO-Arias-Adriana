"""
SISTEMA DE RESTAURANTE - SEMANA 7
==================================

Objetivo: Demostrar los principios fundamentales de Programación Orientada a Objetos

Principios de POO demostrados en este proyecto:
1. ENCAPSULACIÓN: Los datos están protegidos mediante properties (@property/@setter)
2. ABSTRACCIÓN: Ocultamos la complejidad interna de las clases
3. REUTILIZACIÓN: Código modular y reutilizable
4. VALIDACIÓN: Siempre se validan los datos antes de almacenarlos

Clases principales:
- Producto: Demuestra encapsulación con properties y validación
- Cliente: Usa @dataclass para simplificar el código
- Restaurante: Gestor de productos y clientes (patrón contenedor)
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_bienvenida():
    """Muestra un mensaje de bienvenida educativo."""
    print("\n" + "="*60)
    print("🍽️  BIENVENIDO AL SISTEMA DE RESTAURANTE - SEMANA 7")
    print("="*60)
    print("Este proyecto demuestra los principios de POO:")
    print("  ✓ Encapsulación  ✓ Abstracción  ✓ Validación")
    print("="*60 + "\n")


def mostrar_menu() -> None:
    """Muestra el menú principal del sistema."""
    print("\n" + "="*50)
    print("        MENÚ PRINCIPAL")
    print("="*50)
    print("--- PRODUCTOS ---")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Ver productos disponibles")
    print("5. Filtrar por categoría")
    print("----------------------------------------")
    print("--- CLIENTES ---")
    print("6. Registrar cliente")
    print("7. Listar clientes")
    print("8. Buscar cliente")
    print("----------------------------------------")
    print("--- INFORMACIÓN ---")
    print("9. Ver estadísticas del restaurante")
    print("10. Demostración de ENCAPSULACIÓN")
    print("11. Demostración de VALIDACIÓN")
    print("----------------------------------------")
    print("12. Salir")
    print("="*50)


def solicitar_producto() -> Producto:
    """Solicita al usuario los datos de un producto con validación educativa."""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría (ej: Plato, Bebida, Postre): ").strip()

    while True:
        try:
            precio_texto = input("Ingrese el precio del producto (debe ser > 0): ").strip()
            precio = float(precio_texto)
            if precio <= 0:
                print("❌ El precio debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("❌ El precio debe ser un número válido.")

    disponible_texto = input("¿Está disponible? (s/n): ").strip().lower()
    disponible = disponible_texto == "s"

    # El constructor de Producto realizará la validación automáticamente
    return Producto(nombre=nombre, categoria=categoria, precio=precio, disponible=disponible)


def solicitar_cliente() -> Cliente:
    """Solicita al usuario los datos de un cliente."""
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    nombre = input("Ingrese el nombre del cliente: ").strip()
    correo = input("Ingrese el correo del cliente: ").strip()
    id_cliente = input("Ingrese el identificador del cliente: ").strip()
    return Cliente(nombre=nombre, correo=correo, id_cliente=id_cliente)


def registrar_producto(restaurante: Restaurante) -> None:
    """Registra un nuevo producto con manejo de errores."""
    try:
        producto = solicitar_producto()
        restaurante.registrar_producto(producto)
    except ValueError as error:
        print(f"\n⚠️  Error al registrar el producto: {error}\n")


def listar_productos(restaurante: Restaurante) -> None:
    """Lista todos los productos registrados."""
    productos = restaurante.listar_productos()
    if not productos:
        print("\n📭 No hay productos registrados.\n")
        return

    print(f"\n{'='*50}")
    print(f"📋 LISTA DE PRODUCTOS ({len(productos)} registrados)")
    print(f"{'='*50}\n")

    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. {producto.mostrar_informacion()}")
        print("-" * 50)
    print()


def buscar_producto(restaurante: Restaurante) -> None:
    """Busca un producto por nombre."""
    nombre = input("\nIngrese el nombre del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(nombre)

    if producto:
        print(f"\n✓ Producto encontrado:")
        print(f"{'-'*50}")
        print(producto.mostrar_informacion())
        print(f"{'-'*50}\n")
    else:
        print(f"\n❌ No se encontró ningún producto con el nombre '{nombre}'.\n")


def listar_disponibles(restaurante: Restaurante) -> None:
    """Lista solo los productos disponibles."""
    disponibles = restaurante.obtener_productos_disponibles()

    if not disponibles:
        print("\n📭 No hay productos disponibles.\n")
        return

    print(f"\n{'='*50}")
    print(f"✓ PRODUCTOS DISPONIBLES ({len(disponibles)})")
    print(f"{'='*50}\n")

    for indice, producto in enumerate(disponibles, start=1):
        print(f"{indice}. {producto.mostrar_informacion()}")
        print("-" * 50)
    print()


def filtrar_por_categoria(restaurante: Restaurante) -> None:
    """Filtra productos por categoría."""
    categoria = input("\nIngrese la categoría a buscar: ").strip()
    productos = restaurante.obtener_productos_por_categoria(categoria)

    if not productos:
        print(f"\n❌ No hay productos en la categoría '{categoria}'.\n")
        return

    print(f"\n{'='*50}")
    print(f"📋 PRODUCTOS EN CATEGORÍA: {categoria.upper()} ({len(productos)})")
    print(f"{'='*50}\n")

    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. {producto.mostrar_informacion()}")
        print("-" * 50)
    print()


def registrar_cliente(restaurante: Restaurante) -> None:
    """Registra un nuevo cliente."""
    try:
        cliente = solicitar_cliente()
        restaurante.registrar_cliente(cliente)
    except ValueError as error:
        print(f"\n⚠️  Error al registrar el cliente: {error}\n")


def listar_clientes(restaurante: Restaurante) -> None:
    """Lista todos los clientes registrados."""
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("\n📭 No hay clientes registrados.\n")
        return

    print(f"\n{'='*50}")
    print(f"👥 LISTA DE CLIENTES ({len(clientes)} registrados)")
    print(f"{'='*50}\n")

    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. {cliente.mostrar_informacion()}")
        print("-" * 50)
    print()


def buscar_cliente(restaurante: Restaurante) -> None:
    """Busca un cliente por nombre."""
    nombre = input("\nIngrese el nombre del cliente a buscar: ").strip()
    cliente = restaurante.buscar_cliente(nombre)

    if cliente:
        print(f"\n✓ Cliente encontrado:")
        print(f"{'-'*50}")
        print(cliente.mostrar_informacion())
        print(f"{'-'*50}\n")
    else:
        print(f"\n❌ No se encontró ningún cliente con el nombre '{nombre}'.\n")


def mostrar_estadisticas(restaurante: Restaurante) -> None:
    """Muestra estadísticas del restaurante."""
    restaurante.mostrar_resumen()


def demo_encapsulacion() -> None:
    """Demuestra el concepto de ENCAPSULACIÓN."""
    print("\n" + "="*60)
    print("📚 DEMOSTRACIÓN: ENCAPSULACIÓN")
    print("="*60)
    print("\n¿Qué es la ENCAPSULACIÓN?")
    print("Es ocultar los detalles internos de una clase y permitir")
    print("acceso controlado a través de métodos públicos.\n")

    print("Creando un producto con validación automática...\n")

    try:
        # Esto funcionará correctamente
        producto = Producto(
            nombre="Pizza Margherita",
            categoria="Plato Principal",
            precio=15.99,
            disponible=True
        )
        print("✓ Producto creado exitosamente\n")
        print(f"Información:\n{producto.mostrar_informacion()}")
        print(f"\n{producto.info_pedagogica()}")

        # Ahora intentemos cambiar el precio a través del setter
        print("\n" + "-"*60)
        print("Intentando cambiar el precio a un valor inválido...")
        print("-"*60)
        try:
            producto.precio = -5  # Esto fallará
        except ValueError as e:
            print(f"\n✓ La encapsulación nos protegió: {e}\n")

    except ValueError as e:
        print(f"Error: {e}\n")

    print("="*60)
    print("Conclusión: El setter valida automáticamente cada asignación\n")


def demo_validacion() -> None:
    """Demuestra el sistema de VALIDACIÓN."""
    print("\n" + "="*60)
    print("📚 DEMOSTRACIÓN: VALIDACIÓN")
    print("="*60)
    print("\nLa validación ocurre en dos niveles:\n")

    print("1. SETTERS en Producto:")
    print("   - Nombre: No puede estar vacío")
    print("   - Categoría: No puede estar vacía")
    print("   - Precio: Debe ser número > 0")
    print("   - Disponible: Se convierte a booleano\n")

    print("2. __post_init__ en Cliente (Dataclass):")
    print("   - Nombre: No puede estar vacío")
    print("   - Correo: No puede estar vacío")
    print("   - ID: No puede estar vacío\n")

    print("-"*60)
    print("Probando validación en Producto\n")

    # Prueba 1: Precio inválido
    print("Intento 1: Crear producto con precio = -10")
    try:
        p = Producto("Test", "Test", -10)
    except ValueError as e:
        print(f"✓ Validación activada: {e}\n")

    # Prueba 2: Nombre vacío
    print("Intento 2: Crear producto con nombre vacío")
    try:
        p = Producto("  ", "Test", 10)
    except ValueError as e:
        print(f"✓ Validación activada: {e}\n")

    print("-"*60)
    print("Conclusión: La validación previene datos inválidos\n")
    print("="*60 + "\n")


def ejecutar_sistema() -> None:
    """Ejecuta el loop principal del sistema."""
    restaurante = Restaurante("Restaurant POO - Semana 7")
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-12): ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            listar_disponibles(restaurante)
        elif opcion == "5":
            filtrar_por_categoria(restaurante)
        elif opcion == "6":
            registrar_cliente(restaurante)
        elif opcion == "7":
            listar_clientes(restaurante)
        elif opcion == "8":
            buscar_cliente(restaurante)
        elif opcion == "9":
            mostrar_estadisticas(restaurante)
        elif opcion == "10":
            demo_encapsulacion()
        elif opcion == "11":
            demo_validacion()
        elif opcion == "12":
            print("\n👋 Saliendo del sistema. ¡Gracias por usar POO Restaurant!\n")
            break
        else:
            print("\n❌ Opción inválida. Por favor seleccione una opción válida.\n")


if __name__ == "__main__":
    ejecutar_sistema()


