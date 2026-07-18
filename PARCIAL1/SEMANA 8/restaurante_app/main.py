from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n  📝 Ingrese los datos del producto:")
    codigo = input("  Código del producto: ").strip()
    nombre = input("  Nombre: ").strip()
    categoria = input("  Categoría: ").strip()
    try:
        precio = float(input("  Precio: ").strip())
    except ValueError:
        print("  ❌ Precio inválido. Operación cancelada.")
        return

    producto = Producto(codigo, nombre, categoria, precio)
    if restaurante.registrar_producto(producto):
        print("  ✓ Producto registrado correctamente.\n")
    else:
        print("  ❌ Error: ya existe un producto con ese código.\n")


def registrar_bebida(restaurante: Restaurante) -> None:
    print("\n  📝 Ingrese los datos de la bebida:")
    codigo = input("  Código de la bebida: ").strip()
    nombre = input("  Nombre: ").strip()
    categoria = input("  Categoría: ").strip()
    try:
        precio = float(input("  Precio: ").strip())
    except ValueError:
        print("  ❌ Precio inválido. Operación cancelada.")
        return
    tamano = input("  Tamaño (por ejemplo, 500ml): ").strip()
    envase = input("  Envase (lata, botella, vaso): ").strip()

    bebida = Bebida(codigo, nombre, categoria, precio, tamano, envase)
    if restaurante.registrar_producto(bebida):
        print("  ✓ Bebida registrada correctamente.\n")
    else:
        print("  ❌ Error: ya existe un producto con ese código.\n")


def registrar_cliente(restaurante: Restaurante) -> None:
    print("\n  📝 Ingrese los datos del cliente:")
    identificacion = input("  Identificación del cliente: ").strip()
    nombre = input("  Nombre: ").strip()
    correo = input("  Correo: ").strip()

    cliente = Cliente(identificacion, nombre, correo)
    if restaurante.registrar_cliente(cliente):
        print("  ✓ Cliente registrado correctamente.\n")
    else:
        print("  ❌ Error: ya existe un cliente con esa identificación.\n")


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("\n  ℹ️  No hay productos registrados.\n")
        return
    print("\n  📋 --- PRODUCTOS REGISTRADOS ---")
    for info in productos:
        print(f"     {info}")
    print()


def listar_clientes(restaurante: Restaurante) -> None:
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("\n  ℹ️  No hay clientes registrados.\n")
        return
    print("\n  📋 --- CLIENTES REGISTRADOS ---")
    for info in clientes:
        print(f"     {info}")
    print()


def mostrar_menu() -> None:
    print("\n" + "="*50)
    print("        SISTEMA DE RESTAURANTE")
    print("="*50)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 50)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 50)
    print("6. Ver explicación SOLID")
    print("7. Salir")
    print("="*50)


def explicar_solid() -> None:
    """Muestra una explicación didáctica de los principios SOLID aplicada al sistema."""
    print("\n" + "="*50)
    print("   EXPLICACIÓN DE PRINCIPIOS SOLID")
    print("="*50)
    print("\n🔹 S — RESPONSABILIDAD ÚNICA (Single Responsibility):")
    print("   Cada clase tiene UNA sola responsabilidad:")
    print("   • Producto/Bebida/Cliente: Guardan datos del dominio")
    print("   • Restaurante: Administra colecciones y validaciones")
    print("   • main.py: Interactúa con el usuario y delega al servicio")
    print("   ")
    print("   ✓ Ventaja: Fácil de modificar, entender y mantener")

    print("\n🔹 O — ABIERTO/CERRADO (Open/Closed):")
    print("   Abierto para extensión, cerrado para modificación.")
    print("   • Podemos crear nuevas subclases (ej: Platillo, Postre)")
    print("   • Restaurante NO necesita cambiar su código")
    print("   • Bebida extiende Producto automáticamente")
    print("   ")
    print("   ✓ Ventaja: Agregar funciones sin romper código existente")

    print("\n🔹 L — SUSTITUCIÓN DE LISKOV (Liskov Substitution):")
    print("   Bebida puede reemplazar a Producto sin romper el sistema.")
    print("   • Bebida hereda de Producto (relación válida)")
    print("   • Implementa el mismo método: mostrar_informacion()")
    print("   • Restaurante itera lista sin preguntar el tipo concreto")
    print("   • El polimorfismo funciona: cada objeto responde a su manera")
    print("   ")
    print("   ✓ Ventaja: Código genérico que funciona con cualquier Producto")

    print("\n" + "="*50)
    print("RESUMEN: Con SOLID, el código es flexible, mantenible y escalable 📈")
    print("="*50 + "\n")


def main() -> None:
    restaurante = Restaurante()
    # Mostrar explicación didáctica al inicio
    explicar_solid()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)
        elif opcion == "3":
            registrar_cliente(restaurante)
        elif opcion == "4":
            listar_productos(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            explicar_solid()
        elif opcion == "7":
            print("\n  👋 ¡Hasta luego!\n")
            break
        else:
            print("  ❌ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()

