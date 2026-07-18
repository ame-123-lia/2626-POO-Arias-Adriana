#!/usr/bin/env python
"""
Simulación de una sesión interactiva del sistema restaurante_app.
Muestra cómo se vería la explicación SOLID al iniciar el programa.
"""

import sys
sys.path.insert(0, 'C:\\Users\\User\\OneDrive\\Escritorio\\2626-POO-Arias-Adriana\\PARCIAL1\\SEMANA 8')

from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente


def main():
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  SIMULACIÓN: INICIO DEL PROGRAMA restaurante_app".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")

    # Mostrar la explicación que ve el usuario al iniciar
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

    # Mostrar el menú
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

    # Simular algunas acciones
    print("\n[SIMULANDO INTERACCIÓN DEL USUARIO]\n")

    restaurante = Restaurante()

    # Opción 1: Registrar producto
    print(">>> Usuario selecciona: 1")
    print("\n  📝 Ingrese los datos del producto:")
    print("  Código del producto: 001")
    print("  Nombre: Pizza Pepperoni")
    print("  Categoría: Comida")
    print("  Precio: 18.50")

    p1 = Producto("001", "Pizza Pepperoni", "Comida", 18.50)
    if restaurante.registrar_producto(p1):
        print("  ✓ Producto registrado correctamente.\n")

    # Opción 2: Registrar bebida
    print(">>> Usuario selecciona: 2")
    print("\n  📝 Ingrese los datos de la bebida:")
    print("  Código de la bebida: B001")
    print("  Nombre: Coca Cola")
    print("  Categoría: Bebida")
    print("  Precio: 3.50")
    print("  Tamaño (por ejemplo, 500ml): 500ml")
    print("  Envase (lata, botella, vaso): Botella")

    b1 = Bebida("B001", "Coca Cola", "Bebida", 3.50, "500ml", "Botella")
    if restaurante.registrar_producto(b1):
        print("  ✓ Bebida registrada correctamente.\n")

    # Opción 3: Registrar cliente
    print(">>> Usuario selecciona: 3")
    print("\n  📝 Ingrese los datos del cliente:")
    print("  Identificación del cliente: C001")
    print("  Nombre: Juan García")
    print("  Correo: juan@example.com")

    c1 = Cliente("C001", "Juan García", "juan@example.com")
    if restaurante.registrar_cliente(c1):
        print("  ✓ Cliente registrado correctamente.\n")

    # Opción 4: Listar productos
    print(">>> Usuario selecciona: 4")
    print("\n  📋 --- PRODUCTOS REGISTRADOS ---")
    for info in restaurante.listar_productos():
        print(f"     {info}")
    print()

    print("🔍 OBSERVACIÓN IMPORTANTE:")
    print("   La Pizza es un Producto, la Coca Cola es una Bebida.")
    print("   ¡PERO están en la MISMA lista!")
    print("   Restaurante NO pregunta el tipo, solo llama mostrar_informacion()")
    print("   ← ESTO ES POLIMORFISMO (LSP) en acción\n")

    # Opción 5: Listar clientes
    print(">>> Usuario selecciona: 5")
    print("\n  📋 --- CLIENTES REGISTRADOS ---")
    for info in restaurante.listar_clientes():
        print(f"     {info}")
    print()

    # Opción 6: Ver explicación SOLID
    print(">>> Usuario selecciona: 6")
    print("\n[Se muestra nuevamente la explicación SOLID]")
    print("\n(Usuario puede releer SOLID en cualquier momento)")
    print()

    # Opción 7: Salir
    print(">>> Usuario selecciona: 7")
    print("\n  👋 ¡Hasta luego!\n")

    print("█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  FIN DE LA SIMULACIÓN".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")

    print("✅ Como ves, el programa:")
    print("   1️⃣  Explica SOLID al iniciar")
    print("   2️⃣  Ofrece un menú interactivo amigable")
    print("   3️⃣  Permite registrar y listar con validación")
    print("   4️⃣  Demuestra el polimorfismo en acción")
    print("   5️⃣  Permite releer SOLID en cualquier momento\n")


if __name__ == "__main__":
    main()

