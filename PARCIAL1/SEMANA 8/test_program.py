#!/usr/bin/env python
"""Script de prueba para demostrar el programa sin interacción interactiva."""

import sys
sys.path.insert(0, 'C:\\Users\\User\\OneDrive\\Escritorio\\2626-POO-Arias-Adriana\\PARCIAL1\\SEMANA 8')

from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente


def explicar_solid() -> None:
    """Muestra una explicación didáctica de los principios SOLID aplicada al sistema."""
    print("\n========================================")
    print("       EXPLICACIÓN DE PRINCIPIOS SOLID")
    print("========================================")
    print("S — Responsabilidad Única (Single Responsibility):")
    print("  Cada clase tiene una única responsabilidad:")
    print("   - Producto / Bebida / Cliente: representan datos del dominio.")
    print("   - Restaurante: gestiona colecciones y reglas de registro/listado.")
    print("   - main.py: sólo interactúa con el usuario y delega acciones al servicio.")
    print()
    print("O — Abierto/Cerrado (Open/Closed):")
    print("  El servicio Restaurante está diseñado para trabajar con la clase base Producto.")
    print("  Podemos añadir nuevas subclases (por ejemplo, Platillo) sin cambiar la lógica de Restaurante.")
    print("  Ejemplo: la clase Bebida extiende Producto y Restaurante no necesita modificar su código para gestionarla.")
    print()
    print("L — Sustitución de Liskov (Liskov Substitution):")
    print("  Una Bebida puede usarse donde se espera un Producto sin romper el sistema.")
    print("  Por eso Bebida mantiene la misma interfaz: implementa mostrar_informacion().")
    print("  Restaurante itera la lista de productos y llama p.mostrar_informacion() sin preguntar el tipo concreto.")
    print()
    print("Resumen didáctico:")
    print("  - Gracias a SRP, cada módulo es más fácil de entender y mantener.")
    print("  - Gracias a OCP, podemos extender con nuevas subclases sin tocar Restaurante.")
    print("  - Gracias a LSP, el polimorfismo funciona: Bebida se comporta como Producto.")
    print("\nA continuación se muestra un ejemplo práctico de cómo funciona el polimorfismo:\n")


def demostrar_polimorfismo() -> None:
    """Demuestra cómo Producto y Bebida comparten la misma interfaz."""
    print("=" * 70)
    print("              DEMOSTRACIÓN PRÁCTICA DE POLIMORFISMO")
    print("=" * 70)

    restaurante = Restaurante()

    # Crear productos y bebidas
    producto1 = Producto("001", "Hamburguesa", "Comida", 15.50)
    producto2 = Producto("002", "Ensalada", "Comida", 12.00)
    bebida1 = Bebida("003", "Coca Cola", "Bebida", 3.50, "500ml", "Botella")
    bebida2 = Bebida("004", "Jugo Natural", "Bebida", 5.00, "250ml", "Vaso")

    # Registrar en el servicio Restaurante
    restaurante.registrar_producto(producto1)
    restaurante.registrar_producto(producto2)
    restaurante.registrar_producto(bebida1)
    restaurante.registrar_producto(bebida2)

    print("\n✓ Productos y Bebidas registrados exitosamente.\n")
    print("Por qué esto demuestra POLIMORFISMO (parte de LSP):")
    print("-" * 70)
    print("- Producto y Bebida están en LA MISMA LISTA dentro de Restaurante.")
    print("- Restaurante NO pregunta: '¿es esto un Producto o una Bebida?'")
    print("- Simplemente llama a mostrar_informacion() para cada uno.")
    print("- Bebida sobrescribe el método pero mantiene la misma firma.")
    print("-" * 70)

    print("\n📋 LISTADO DE TODOS LOS PRODUCTOS (Productos + Bebidas mezclados):")
    print()
    for info in restaurante.listar_productos():
        print(f"  {info}")

    print("\n✅ Como ves, Bebida se comporta como Producto sin romper nada.")
    print("   Esto es el Principio de Sustitución de Liskov en acción.\n")


def prueba_validacion() -> None:
    """Demuestra la validación de códigos únicos."""
    print("=" * 70)
    print("         DEMOSTRACIÓN DE VALIDACIÓN DE CÓDIGOS ÚNICOS (SRP)")
    print("=" * 70)

    restaurante = Restaurante()

    producto1 = Producto("P100", "Pizza", "Comida", 20.00)
    print(f"\n1. Intentando registrar producto con código 'P100'...")
    resultado1 = restaurante.registrar_producto(producto1)
    print(f"   Resultado: {'✓ Registrado' if resultado1 else '✗ Rechazado'}")

    producto2 = Producto("P100", "Pasta", "Comida", 18.00)
    print(f"\n2. Intentando registrar otro producto con código 'P100' (duplicado)...")
    resultado2 = restaurante.registrar_producto(producto2)
    print(f"   Resultado: {'✓ Registrado' if resultado2 else '✗ Rechazado (código duplicado)'}")

    print(f"\n✅ Como ves, el Restaurante valida códigos únicos.")
    print(f"   Esto es Responsabilidad Única: Restaurante gestiona colecciones y reglas.\n")


if __name__ == "__main__":
    explicar_solid()
    demostrar_polimorfismo()
    prueba_validacion()
    print("=" * 70)
    print("Pruebas completadas. Puedes ejecutar 'python main.py' para el menú interactivo.")
    print("=" * 70)

