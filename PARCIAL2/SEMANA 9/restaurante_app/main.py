from .servicios.restaurante import Restaurante
from .modelos.producto import Producto
from .modelos.usuario import Usuario
from typing import Callable, Dict


# Tupla: opciones estables del menú (información que no cambia en ejecución)
MENU_OPCIONES = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
)


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("-" * 40)
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("-" * 40)
    print("8. Mostrar categorías")
    print("9. Salir")


def solicitar_producto_desde_input() -> Producto:
    codigo = input("  Código del producto: ").strip()
    nombre = input("  Nombre: ").strip()
    categoria = input("  Categoría: ").strip()
    while True:
        try:
            precio = float(input("  Precio: ").strip())
            break
        except ValueError:
            print("  ❌ Precio inválido. Ingrese un número.")
    return Producto(codigo, nombre, categoria, precio)


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n  📝 Registrar producto:")
    producto = solicitar_producto_desde_input()
    if restaurante.registrar_producto(producto):
        print("  ✓ Producto registrado correctamente.\n")
    else:
        print("  ❌ Error: ya existe un producto con ese código.\n")


def buscar_producto(restaurante: Restaurante) -> None:
    codigo = input("  Ingrese código a buscar: ").strip()
    p = restaurante.buscar_producto_por_codigo(codigo)
    if p is None:
        print("  ℹ️  Producto no encontrado.\n")
    else:
        print("  📌 Producto encontrado:")
        print(f"   {p.mostrar_informacion()}\n")


def actualizar_producto(restaurante: Restaurante) -> None:
    codigo = input("  Ingrese código del producto a actualizar: ").strip()
    p = restaurante.buscar_producto_por_codigo(codigo)
    if p is None:
        print("  ℹ️  Producto no encontrado.\n")
        return
    print("  Deje vacío un campo para no modificarlo.")
    nombre = input(f"  Nuevo nombre [{p.nombre}]: ").strip() or None
    categoria = input(f"  Nueva categoría [{p.categoria}]: ").strip() or None
    precio_input = input(f"  Nuevo precio [{p.precio}]: ").strip() or None
    precio = None
    if precio_input is not None:
        if precio_input == "":
            precio = None
        else:
            try:
                precio = float(precio_input)
            except ValueError:
                print("  ❌ Precio inválido. Operación cancelada.")
                return
    if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
        print("  ✓ Producto actualizado correctamente.\n")
    else:
        print("  ❌ No se pudo actualizar el producto.\n")


def eliminar_producto(restaurante: Restaurante) -> None:
    codigo = input("  Ingrese código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("  ✓ Producto eliminado.\n")
    else:
        print("  ℹ️  Producto no encontrado.\n")


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("\n  ℹ️  No hay productos registrados.\n")
        return
    print("\n  📋 --- PRODUCTOS REGISTRADOS ---")
    for info in productos:
        print(f"     {info}")
    print()


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n  📝 Registrar usuario:")
    identificacion = input("  Identificación: ").strip()
    nombre = input("  Nombre: ").strip()
    correo = input("  Correo: ").strip()
    usuario = Usuario(identificacion, nombre, correo)
    if restaurante.registrar_usuario(usuario):
        print("  ✓ Usuario registrado correctamente.\n")
    else:
        print("  ❌ Error: ya existe un usuario con esa identificación.\n")


def listar_usuarios(restaurante: Restaurante) -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("\n  ℹ️  No hay usuarios registrados.\n")
        return
    print("\n  📋 --- USUARIOS REGISTRADOS ---")
    for info in usuarios:
        print(f"     {info}")
    print()


def mostrar_categorias(restaurante: Restaurante) -> None:
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("\n  ℹ️  No hay categorías para mostrar.\n")
        return
    print("\n  🧾 Categorías únicas de productos:")
    for c in categorias:
        print(f"    - {c}")
    print()


def main() -> None:
    restaurante = Restaurante()

    # Diccionario: mapea opciones -> funciones (relación clave->valor)
    acciones: Dict[str, Callable[[Restaurante], None]] = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "9":
            print("\n  👋 ¡Hasta luego!\n")
            break
        if opcion not in MENU_OPCIONES:
            print("  ❌ Opción inválida. Intente nuevamente.")
            continue
        accion = acciones.get(opcion)
        if accion:
            try:
                accion(restaurante)
            except Exception as e:
                print(f"  ❌ Ocurrió un error: {e}")
        else:
            print("  ❌ Opción no implementada.")


if __name__ == "__main__":
    main()

