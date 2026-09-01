try:
    # Cuando se ejecuta como paquete: import relativo
    from .servicios.restaurante import Restaurante
    from .modelos.producto import Producto
    from .modelos.usuario import Usuario
    from .modelos.venta import Venta
    from .servicios.archivo_servicio import ArchivoServicio
except Exception:
    # Cuando se ejecuta como script directamente (python main.py), usar import absoluto
    from servicios.restaurante import Restaurante
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta
    from servicios.archivo_servicio import ArchivoServicio
from typing import Callable, Dict
from pathlib import Path


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
    "10",
    "11",
)


def mostrar_menu() -> None:
    print("\n" + "=" * 50)
    print("      SISTEMA DE RESTAURANTE (Semana 12)")
    print("=" * 50)
    print("PRODUCTOS:")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("-" * 50)
    print("USUARIOS:")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("-" * 50)
    print("VENTAS:")
    print("8. Realizar venta")
    print("9. Consultar ventas de usuario")
    print("10. Listar todas las ventas")
    print("-" * 50)
    print("11. Salir")


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
    while True:
        try:
            stock = int(input("  Stock inicial: ").strip())
            break
        except ValueError:
            print("  ❌ Stock inválido. Ingrese un número entero.")
    return Producto(codigo, nombre, categoria, precio, stock)


def registrar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n  📝 Registrar producto:")
    try:
        producto = solicitar_producto_desde_input()
    except ValueError as e:
        print(f"  ❌ Datos inválidos: {e}")
        return
    if restaurante.registrar_producto(producto):
        try:
            archivo_servicio.guardar_productos(restaurante.obtener_productos_como_lista())
        except PermissionError as e:
            print(f"  ❌ No se pudo guardar en archivo: {e}")
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


def actualizar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
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
        try:
            archivo_servicio.guardar_productos(restaurante.obtener_productos_como_lista())
        except PermissionError as e:
            print(f"  ❌ No se pudo guardar en archivo: {e}")
        print("  ✓ Producto actualizado correctamente.\n")
    else:
        print("  ❌ No se pudo actualizar el producto.\n")


def eliminar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    codigo = input("  Ingrese código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        try:
            archivo_servicio.guardar_productos(restaurante.obtener_productos_como_lista())
        except PermissionError as e:
            print(f"  ❌ No se pudo guardar en archivo: {e}")
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


def registrar_usuario(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n  📝 Registrar usuario:")
    identificacion = input("  Identificación: ").strip()
    nombre = input("  Nombre: ").strip()
    correo = input("  Correo: ").strip()
    usuario = Usuario(identificacion, nombre, correo)
    if restaurante.registrar_usuario(usuario):
        try:
            archivo_servicio.guardar_usuarios(restaurante.obtener_usuarios_como_lista())
        except PermissionError as e:
            print(f"  ❌ No se pudo guardar en archivo: {e}")
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


def realizar_venta(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n  💳 Realizar venta:")
    identificacion_usuario = input("  Identificación del usuario: ").strip()
    codigo_producto = input("  Código del producto: ").strip()
    
    usuario = restaurante.buscar_usuario_por_id(identificacion_usuario)
    if usuario is None:
        print("  ❌ Usuario no encontrado.\n")
        return
    
    producto = restaurante.buscar_producto_por_codigo(codigo_producto)
    if producto is None:
        print("  ❌ Producto no encontrado.\n")
        return
    
    print(f"  Producto: {producto.nombre} | Stock disponible: {producto.stock}")
    
    while True:
        try:
            cantidad = int(input("  Cantidad a vender: ").strip())
            break
        except ValueError:
            print("  ❌ Cantidad inválida. Ingrese un número entero.")
    
    if restaurante.vender_producto(codigo_producto, identificacion_usuario, cantidad):
        try:
            archivo_servicio.guardar_ventas(restaurante.obtener_ventas_como_lista())
            archivo_servicio.guardar_productos(restaurante.obtener_productos_como_lista())
        except PermissionError as e:
            print(f"  ❌ No se pudo guardar en archivo: {e}")
        print(f"  ✓ Venta registrada. Nuevo stock: {producto.stock}\n")
    else:
        print("  ❌ Error: cantidad inválida o stock insuficiente.\n")


def consultar_ventas_usuario(restaurante: Restaurante) -> None:
    identificacion_usuario = input("  Identificación del usuario: ").strip()
    
    usuario = restaurante.buscar_usuario_por_id(identificacion_usuario)
    if usuario is None:
        print("  ❌ Usuario no encontrado.\n")
        return
    
    ventas = restaurante.obtener_ventas_usuario(identificacion_usuario)
    if not ventas:
        print(f"\n  ℹ️  El usuario no ha realizado compras.\n")
        return
    
    print(f"\n  📋 --- COMPRAS DE {usuario.nombre.upper()} ---")
    for venta_info in ventas:
        print(f"     {venta_info}")
    print()


def listar_todas_ventas(restaurante: Restaurante) -> None:
    ventas = restaurante.listar_todas_ventas()
    if not ventas:
        print("\n  ℹ️  No hay ventas registradas.\n")
        return
    print("\n  📋 --- TODAS LAS VENTAS ---")
    for venta_info in ventas:
        print(f"     {venta_info}")
    print()




def main() -> None:
    # Construir ruta al archivo dentro del paquete
    base = Path(__file__).resolve().parent
    ruta_productos = str(base / "datos" / "productos.json")
    ruta_usuarios = str(base / "datos" / "usuarios.json")
    ruta_ventas = str(base / "datos" / "ventas.json")

    archivo_servicio = ArchivoServicio(ruta_productos, ruta_usuarios, ruta_ventas)
    restaurante = Restaurante()

    # Cargar productos desde JSON al iniciar
    print("  Cargando datos...\n")
    registros_productos = archivo_servicio.cargar_productos()
    if registros_productos:
        for i, rec in enumerate(registros_productos, start=1):
            try:
                p = Producto.from_dict(rec)
                restaurante.registrar_producto(p)
            except KeyError as e:
                print(f"  ⚠️  Producto {i} omitido: falta la clave {e}")
            except ValueError as e:
                print(f"  ⚠️  Producto {i} omitido: datos inválidos ({e})")

    # Cargar usuarios desde JSON al iniciar
    registros_usuarios = archivo_servicio.cargar_usuarios()
    if registros_usuarios:
        for i, rec in enumerate(registros_usuarios, start=1):
            try:
                u = Usuario.from_dict(rec)
                restaurante.registrar_usuario(u)
            except KeyError as e:
                print(f"  ⚠️  Usuario {i} omitido: falta la clave {e}")
            except ValueError as e:
                print(f"  ⚠️  Usuario {i} omitido: datos inválidos ({e})")

    # Cargar ventas desde JSON al iniciar
    registros_ventas = archivo_servicio.cargar_ventas()
    if registros_ventas:
        for i, rec in enumerate(registros_ventas, start=1):
            try:
                v = Venta.from_dict(rec)
                restaurante.cargar_ventas([v])
            except KeyError as e:
                print(f"  ⚠️  Venta {i} omitida: falta la clave {e}")
            except ValueError as e:
                print(f"  ⚠️  Venta {i} omitida: datos inválidos ({e})")

    # Diccionario: mapea opciones -> funciones
    acciones: Dict[str, Callable[[Restaurante], None]] = {
        "1": lambda r: registrar_producto(r, archivo_servicio),
        "2": lambda r: buscar_producto(r),
        "3": lambda r: actualizar_producto(r, archivo_servicio),
        "4": lambda r: eliminar_producto(r, archivo_servicio),
        "5": lambda r: listar_productos(r),
        "6": lambda r: registrar_usuario(r, archivo_servicio),
        "7": lambda r: listar_usuarios(r),
        "8": lambda r: realizar_venta(r, archivo_servicio),
        "9": lambda r: consultar_ventas_usuario(r),
        "10": lambda r: listar_todas_ventas(r),
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "11":
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

