"""
Módulo principal (main) del sistema de gestión de restaurante
Punto de entrada del programa que demuestra el uso de todas las clases del sistema
"""

# Importaciones de las clases del modelo
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.cliente import Cliente

# Importación del servicio principal
from restaurante_app.servicios.restaurante import Restaurante


def main() -> None:
    """
    Función principal que ejecuta el programa.
    Crea instancias de productos y clientes, los agrega al restaurante
    y muestra la información de forma organizada.
    """

    # ============================================================
    # SECCIÓN 1: Crear instancia del restaurante
    # ============================================================
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE - SEMANA 5")
    print("="*60 + "\n")

    # Crear el restaurante con nombre y año de fundación
    restaurante_amazonico = Restaurante(nombre="Sabor Amazónico", año_fundacion=2020)
    restaurante_amazonico.mostrar_resumen()

    # ============================================================
    # SECCIÓN 2: Crear productos y agregarlos al restaurante
    # ============================================================
    print("\n> Agregando productos al menu...\n")

    # Crear primer producto: Ceviche Amazónico
    producto_ceviche = Producto(
        nombre="Ceviche Amazónico",
        descripcion="Ceviche preparado con pescado fresco de la región",
        precio=18.50,
        cantidad_disponible=15,
        es_vegetariano=False
    )
    restaurante_amazonico.agregar_producto(producto_ceviche)

    # Crear segundo producto: Tacacho con queso
    producto_tacacho = Producto(
        nombre="Tacacho con Queso",
        descripcion="Plátano frito acompañado de queso derretido",
        precio=12.00,
        cantidad_disponible=20,
        es_vegetariano=True
    )
    restaurante_amazonico.agregar_producto(producto_tacacho)

    # Crear tercer producto: Jugo de Guaraná
    producto_guarana = Producto(
        nombre="Jugo de Guaraná",
        descripcion="Bebida energética natural de fruta amazónica",
        precio=5.50,
        cantidad_disponible=30,
        es_vegetariano=True
    )
    restaurante_amazonico.agregar_producto(producto_guarana)

    # Crear cuarto producto: Picadillo de carne
    producto_picadillo = Producto(
        nombre="Picadillo de Carne",
        descripcion="Carne molida sazonada con especias locales",
        precio=15.75,
        cantidad_disponible=10,
        es_vegetariano=False
    )
    restaurante_amazonico.agregar_producto(producto_picadillo)

    # ============================================================
    # SECCIÓN 3: Crear clientes y registrarlos en el restaurante
    # ============================================================
    print("\n> Registrando clientes en el sistema...\n")

    # Crear primer cliente: cliente premium
    cliente_juan = Cliente(
        nombre="Juan Carlos Mendoza",
        email="juan.mendoza@email.com",
        telefono="+593-2-5555555",
        edad=35,
        es_miembro_premium=True
    )
    restaurante_amazonico.agregar_cliente(cliente_juan)

    # Crear segundo cliente: cliente regular
    cliente_maria = Cliente(
        nombre="María Fernanda Gómez",
        email="maria.gomez@email.com",
        telefono="+593-2-6666666",
        edad=28,
        es_miembro_premium=False
    )
    restaurante_amazonico.agregar_cliente(cliente_maria)

    # Crear tercer cliente: cliente premium
    cliente_pedro = Cliente(
        nombre="Pedro Alejandro Ruiz",
        email="pedro.ruiz@email.com",
        telefono="+593-2-7777777",
        edad=45,
        es_miembro_premium=True
    )
    restaurante_amazonico.agregar_cliente(cliente_pedro)

    # Crear cuarto cliente: cliente regular
    cliente_ana = Cliente(
        nombre="Ana Patricia López",
        email="ana.lopez@email.com",
        telefono="+593-2-8888888",
        edad=31,
        es_miembro_premium=False
    )
    restaurante_amazonico.agregar_cliente(cliente_ana)

    # ============================================================
    # SECCIÓN 4: Mostrar información del menú
    # ============================================================
    restaurante_amazonico.listar_productos()

    # ============================================================
    # SECCIÓN 5: Mostrar lista de clientes registrados
    # ============================================================
    restaurante_amazonico.listar_clientes()

    # ============================================================
    # SECCIÓN 6: Demostración de métodos adicionales
    # ============================================================
    print("\n" + "="*60)
    print("PRUEBAS DE MÉTODOS ADICIONALES")
    print("="*60 + "\n")

    # Verificar disponibilidad de un producto
    print("→ Verificando disponibilidad de productos:")
    print(f"  {producto_ceviche.nombre}: {'Disponible' if producto_ceviche.obtener_disponibilidad() else 'No disponible'}")
    print(f"  {producto_tacacho.nombre}: {'Disponible' if producto_tacacho.obtener_disponibilidad() else 'No disponible'}\n")

    # Actualizar cantidad de un producto
    print("→ Actualizando stock de productos:")
    producto_guarana.actualizar_cantidad(-5)
    producto_ceviche.actualizar_cantidad(3)
    print()

    # Actualizar información de un cliente
    print("> Actualizando datos de clientes:")
    cliente_maria.actualizar_email("maria.fernanda.gomez@newemail.com")
    cliente_juan.actualizar_telefono("+593-2-9999999")
    print()

    # Mostrar estado de membresía
    print("> Estado de membresia de clientes:")
    print(f"  {cliente_juan.nombre}: {cliente_juan.obtener_estado_membresia()}")
    print(f"  {cliente_maria.nombre}: {cliente_maria.obtener_estado_membresia()}\n")

    # Buscar un producto por nombre
    print("> Buscando producto en el menu:")
    producto_encontrado = restaurante_amazonico.buscar_producto_por_nombre("Tacacho con Queso")
    if producto_encontrado:
        print(f"  [OK] Producto encontrado: {producto_encontrado.nombre} - ${producto_encontrado.precio:.2f}\n")

    # Buscar un cliente por nombre
    print("> Buscando cliente en el sistema:")
    cliente_encontrado = restaurante_amazonico.buscar_cliente_por_nombre("Pedro Alejandro Ruiz")
    if cliente_encontrado:
        print(f"  [OK] Cliente encontrado: {cliente_encontrado.nombre} ({cliente_encontrado.obtener_estado_membresia()})\n")

    # ============================================================
    # SECCIÓN 7: Resumen final
    # ============================================================
    restaurante_amazonico.mostrar_resumen()

    print("="*60)
    print("FIN DE LA DEMOSTRACIÓN DEL SISTEMA")
    print("="*60)


if __name__ == "__main__":
    # Ejecutar el programa principal
    main()

