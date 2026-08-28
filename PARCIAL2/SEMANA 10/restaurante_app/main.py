"""
Sistema de Gestión de Restaurante - Semana 10
Manejo de archivos, excepciones y persistencia JSON

Autor: Adriana Arias
Asignatura: Programación Orientada a Objetos (POO)
"""

try:
    # Cuando se ejecuta como paquete
    from .servicios.restaurante import Restaurante
    from .modelos.producto import Producto
    from .modelos.usuario import Usuario
    from .servicios.archivo_servicio import ArchivoServicio
except ImportError:
    # Cuando se ejecuta directamente como script
    from servicios.restaurante import Restaurante
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from servicios.archivo_servicio import ArchivoServicio

from typing import Callable, Dict, Optional
from pathlib import Path


# Tupla inmutable con opciones estables del menú
MENU_OPCIONES = ("1", "2", "3", "4", "5", "6", "7", "8", "9")


def mostrar_menu() -> None:
    """Muestra el menú principal en la consola."""
    print("\n" + "=" * 50)
    print("   SISTEMA DE RESTAURANTE - SEMANA 10")
    print("   Persistencia JSON de Productos")
    print("=" * 50)
    print("PRODUCTOS:")
    print("  1. Registrar producto")
    print("  2. Buscar producto")
    print("  3. Actualizar producto")
    print("  4. Eliminar producto")
    print("  5. Listar productos")
    print("-" * 50)
    print("USUARIOS:")
    print("  6. Registrar usuario")
    print("  7. Listar usuarios")
    print("-" * 50)
    print("  8. Consultar información de persistencia")
    print("  9. Salir")
    print("=" * 50)


def solicitar_producto_desde_input() -> Producto:
    """
    Solicita al usuario los datos de un nuevo producto.
    
    Returns:
        Nueva instancia de Producto
        
    Raises:
        ValueError: si los datos ingresados son inválidos
    """
    print()
    codigo = input("  Código del producto: ").strip()
    nombre = input("  Nombre: ").strip()
    categoria = input("  Categoría: ").strip()
    
    # Validar precio
    while True:
        try:
            precio = float(input("  Precio: ").strip())
            break
        except ValueError:
            print("  ❌ Precio inválido. Ingrese un número.")
    
    # Validar stock
    while True:
        try:
            stock = int(input("  Stock inicial: ").strip())
            break
        except ValueError:
            print("  ❌ Stock inválido. Ingrese un número entero.")
    
    return Producto(codigo, nombre, categoria, precio, stock)


def registrar_producto(
    restaurante: Restaurante, 
    archivo_servicio: ArchivoServicio
) -> None:
    """
    Registra un nuevo producto y lo guarda en JSON.
    
    Args:
        restaurante: servicio Restaurante
        archivo_servicio: servicio de persistencia
    """
    print("\n  📝 Registrar producto:")
    try:
        producto = solicitar_producto_desde_input()
    except ValueError as e:
        print(f"  ❌ Datos inválidos: {e}\n")
        return
    
    if restaurante.registrar_producto(producto):
        # Guardar en JSON después del registro
        if archivo_servicio.guardar_productos(restaurante.obtener_productos_como_lista()):
            print("  ✓ Producto registrado y guardado correctamente.\n")
        else:
            print("  ⚠️  Producto registrado pero hubo error al guardar en JSON.\n")
    else:
        print("  ❌ Error: ya existe un producto con ese código.\n")


def buscar_producto(restaurante: Restaurante) -> None:
    """
    Busca y muestra un producto por código.
    
    Args:
        restaurante: servicio Restaurante
    """
    print()
    codigo = input("  Ingrese código a buscar: ").strip()
    producto = restaurante.buscar_producto_por_codigo(codigo)
    
    if producto is None:
        print("  ℹ️  Producto no encontrado.\n")
    else:
        print("  📌 Producto encontrado:")
        print(f"     {producto.mostrar_informacion()}\n")


def actualizar_producto(
    restaurante: Restaurante, 
    archivo_servicio: ArchivoServicio
) -> None:
    """
    Actualiza la información de un producto existente.
    
    Args:
        restaurante: servicio Restaurante
        archivo_servicio: servicio de persistencia
    """
    print()
    codigo = input("  Ingrese código del producto a actualizar: ").strip()
    producto = restaurante.buscar_producto_por_codigo(codigo)
    
    if producto is None:
        print("  ℹ️  Producto no encontrado.\n")
        return
    
    print("  Deje vacío un campo para no modificarlo.")
    nombre = input(f"  Nuevo nombre [{producto.nombre}]: ").strip() or None
    categoria = input(f"  Nueva categoría [{producto.categoria}]: ").strip() or None
    
    precio_input = input(f"  Nuevo precio [{producto.precio}]: ").strip()
    precio: Optional[float] = None
    
    if precio_input:
        try:
            precio = float(precio_input)
        except ValueError:
            print("  ❌ Precio inválido. Operación cancelada.\n")
            return
    
    if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
        # Guardar cambios en JSON
        if archivo_servicio.guardar_productos(restaurante.obtener_productos_como_lista()):
            print("  ✓ Producto actualizado y guardado correctamente.\n")
        else:
            print("  ⚠️  Producto actualizado pero hubo error al guardar en JSON.\n")
    else:
        print("  ❌ No se pudo actualizar el producto.\n")


def eliminar_producto(
    restaurante: Restaurante, 
    archivo_servicio: ArchivoServicio
) -> None:
    """
    Elimina un producto del catálogo.
    
    Args:
        restaurante: servicio Restaurante
        archivo_servicio: servicio de persistencia
    """
    print()
    codigo = input("  Ingrese código del producto a eliminar: ").strip()
    
    if restaurante.eliminar_producto(codigo):
        # Guardar cambios en JSON
        if archivo_servicio.guardar_productos(restaurante.obtener_productos_como_lista()):
            print("  ✓ Producto eliminado y cambios guardados correctamente.\n")
        else:
            print("  ⚠️  Producto eliminado pero hubo error al guardar en JSON.\n")
    else:
        print("  ℹ️  Producto no encontrado.\n")


def listar_productos(restaurante: Restaurante) -> None:
    """
    Lista todos los productos disponibles.
    
    Args:
        restaurante: servicio Restaurante
    """
    productos = restaurante.listar_productos()
    
    if not productos:
        print("\n  ℹ️  No hay productos registrados.\n")
        return
    
    print("\n  📋 --- PRODUCTOS REGISTRADOS ---")
    for info in productos:
        print(f"     {info}")
    print()


def registrar_usuario(restaurante: Restaurante) -> None:
    """
    Registra un nuevo usuario.
    
    Args:
        restaurante: servicio Restaurante
    """
    print()
    identificacion = input("  Identificación: ").strip()
    nombre = input("  Nombre: ").strip()
    correo = input("  Correo: ").strip()
    
    usuario = Usuario(identificacion, nombre, correo)
    
    if restaurante.registrar_usuario(usuario):
        print("  ✓ Usuario registrado correctamente.\n")
    else:
        print("  ❌ Error: ya existe un usuario con esa identificación.\n")


def listar_usuarios(restaurante: Restaurante) -> None:
    """
    Lista todos los usuarios registrados.
    
    Args:
        restaurante: servicio Restaurante
    """
    usuarios = restaurante.listar_usuarios()
    
    if not usuarios:
        print("\n  ℹ️  No hay usuarios registrados.\n")
        return
    
    print("\n  📋 --- USUARIOS REGISTRADOS ---")
    for info in usuarios:
        print(f"     {info}")
    print()


def mostrar_info_persistencia(ruta_archivo: str) -> None:
    """
    Muestra información sobre la persistencia de datos.
    
    Args:
        ruta_archivo: ruta del archivo JSON
    """
    print()
    print("  ℹ️  INFORMACIÓN DE PERSISTENCIA:")
    print(f"     Archivo: {ruta_archivo}")
    print("     Formato: JSON")
    print("     Contenido: Lista de productos serializados")
    print("     Actualización: Automática después de cada cambio")
    print("     Carga: Automática al iniciar la aplicación")
    print()
    print("     Los productos se guardan en el archivo después de:")
    print("     - Registrar un nuevo producto")
    print("     - Actualizar datos de un producto")
    print("     - Eliminar un producto")
    print()
    print("     Cierre la aplicación y vuelva a ejecutarla para")
    print("     confirmar que los productos se recuperan automáticamente.")
    print()


def main() -> None:
    """Función principal que coordina la ejecución del programa."""
    
    # Construir rutas usando pathlib
    base = Path(__file__).resolve().parent
    ruta_productos = str(base / "datos" / "productos.json")
    
    # Crear servicios
    archivo_servicio = ArchivoServicio(ruta_productos)
    restaurante = Restaurante()
    
    # Cargar productos al iniciar
    print("  Cargando datos...\n")
    productos_cargados = archivo_servicio.cargar_productos()
    
    for producto in productos_cargados:
        restaurante.registrar_producto(producto)
    
    if productos_cargados:
        print(f"  ✓ {len(productos_cargados)} producto(s) cargado(s) desde JSON.\n")
    
    # Mapeo de opciones a funciones
    acciones: Dict[str, Callable] = {
        "1": lambda: registrar_producto(restaurante, archivo_servicio),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante, archivo_servicio),
        "4": lambda: eliminar_producto(restaurante, archivo_servicio),
        "5": lambda: listar_productos(restaurante),
        "6": lambda: registrar_usuario(restaurante),
        "7": lambda: listar_usuarios(restaurante),
        "8": lambda: mostrar_info_persistencia(ruta_productos),
    }
    
    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()
        
        if opcion == "9":
            print("\n  👋 ¡Hasta luego!\n")
            break
        
        if opcion not in MENU_OPCIONES:
            print("  ❌ Opción inválida. Intente nuevamente.")
            continue
        
        accion = acciones.get(opcion)
        if accion:
            try:
                accion()
            except Exception as e:
                print(f"  ❌ Error inesperado: {e}\n")
        else:
            print("  ❌ Opción no implementada.")


if __name__ == "__main__":
    main()
