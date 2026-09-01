"""
Sistema de Gestión de Restaurante - Semana 9
Estructuras de Datos: list, tuple, dict, set

Autor: Adriana Arias
Asignatura: Programación Orientada a Objetos (POO)
"""

try:
    # Cuando se ejecuta como paquete
    from .servicios.restaurante import Restaurante
    from .modelos.producto import Producto
    from .modelos.usuario import Usuario
except ImportError:
    # Cuando se ejecuta directamente como script
    from servicios.restaurante import Restaurante
    from modelos.producto import Producto
    from modelos.usuario import Usuario

from typing import Callable, Dict, Optional, Tuple


# ESTRUCTURA: TUPLE
# Uso: Almacenar opciones estables del menú que NO cambiarán durante la ejecución
# Beneficio: Inmutabilidad garantiza que las opciones permanezcan consistentes
MENU_OPCIONES: Tuple[str, ...] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")


def mostrar_menu() -> None:
    """Muestra el menú principal en la consola."""
    print("\n" + "=" * 50)
    print("      SISTEMA DE RESTAURANTE - SEMANA 9")
    print("   Estructuras de Datos: list, tuple, dict, set")
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
    print("  8. Mostrar categorías únicas (SET)")
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
    
    while True:
        try:
            precio = float(input("  Precio: ").strip())
            break
        except ValueError:
            print("  ❌ Precio inválido. Ingrese un número.")
    
    return Producto(codigo, nombre, categoria, precio)


def registrar_producto(restaurante: Restaurante) -> None:
    """
    Registra un nuevo producto.
    
    Args:
        restaurante: servicio Restaurante
    """
    print("\n  📝 Registrar producto:")
    try:
        producto = solicitar_producto_desde_input()
    except ValueError as e:
        print(f"  ❌ Datos inválidos: {e}\n")
        return
    
    if restaurante.registrar_producto(producto):
        print("  ✓ Producto registrado correctamente.\n")
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


def actualizar_producto(restaurante: Restaurante) -> None:
    """
    Actualiza la información de un producto existente.
    
    Args:
        restaurante: servicio Restaurante
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
        print("  ✓ Producto actualizado correctamente.\n")
    else:
        print("  ❌ No se pudo actualizar el producto.\n")


def eliminar_producto(restaurante: Restaurante) -> None:
    """
    Elimina un producto del catálogo.
    
    Args:
        restaurante: servicio Restaurante
    """
    print()
    codigo = input("  Ingrese código del producto a eliminar: ").strip()
    
    if restaurante.eliminar_producto(codigo):
        print("  ✓ Producto eliminado correctamente.\n")
    else:
        print("  ℹ️  Producto no encontrado.\n")


def listar_productos(restaurante: Restaurante) -> None:
    """
    Lista todos los productos disponibles.
    
    ESTRUCTURA: LIST
    Uso: Almacenar la colección dinámica de productos
    Beneficio: Permite agregar, eliminar y modificar elementos fácilmente
    
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
    
    ESTRUCTURA: LIST
    Uso: Almacenar la colección dinámica de usuarios
    Beneficio: Permite gestionar usuarios de forma ordenada
    
    Args:
        restaurante: servicio Restaurante
    """
    usuarios = restaurante.listar_usuarios()
    
    if not usuarios:
        print("\n  ℹ️  No hay usuarios registrados.\n")
        return
    
    print("\n  👥 --- USUARIOS REGISTRADOS ---")
    for info in usuarios:
        print(f"     {info}")
    print()


def mostrar_categorias(restaurante: Restaurante) -> None:
    """
    Muestra todas las categorías únicas de los productos.
    
    ESTRUCTURA: SET
    Uso: Obtener categorías sin duplicados
    Beneficio: El SET automáticamente elimina duplicados
              No es necesario verificar manualmente si una categoría existe
    
    Args:
        restaurante: servicio Restaurante
    """
    categorias = restaurante.obtener_categorias_unicas()
    
    if not categorias:
        print("\n  ℹ️  No hay categorías registradas.\n")
        return
    
    print("\n  🏷️  --- CATEGORÍAS ÚNICAS (SIN DUPLICADOS) ---")
    for i, categoria in enumerate(sorted(categorias), 1):
        print(f"     {i}. {categoria}")
    print()


def main() -> None:
    """Función principal que coordina la ejecución del programa."""
    
    # Crear servicio
    restaurante = Restaurante()
    
    # ESTRUCTURA: DICTIONARY
    # Uso: Mapear opciones del menú a funciones (clave → valor)
    # Beneficio: Búsqueda O(1) de la función correspondiente
    #           Código más limpio sin cadenas de if-elif
    #           Fácil de expandir con nuevas opciones
    acciones: Dict[str, Callable] = {
        "1": lambda: registrar_producto(restaurante),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante),
        "4": lambda: eliminar_producto(restaurante),
        "5": lambda: listar_productos(restaurante),
        "6": lambda: registrar_usuario(restaurante),
        "7": lambda: listar_usuarios(restaurante),
        "8": lambda: mostrar_categorias(restaurante),
    }
    
    print("\n  ¡Bienvenido al Sistema de Restaurante!")
    print("  Semana 9: Estructuras de Datos (list, tuple, dict, set)\n")
    
    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()
        
        # Salida del programa
        if opcion == "9":
            print("\n  👋 ¡Hasta luego!\n")
            break
        
        # Validar que la opción esté dentro de las permitidas
        if opcion not in MENU_OPCIONES:
            print("  ❌ Opción inválida. Intente nuevamente.")
            continue
        
        # Ejecutar la acción correspondiente
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
