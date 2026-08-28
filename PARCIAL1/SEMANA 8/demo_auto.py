#!/usr/bin/env python
"""
Demostración automática (sin input) del software restaurante_app con explicación SOLID
"""

import sys
sys.path.insert(0, 'C:\\Users\\User\\OneDrive\\Escritorio\\2626-POO-Arias-Adriana\\PARCIAL1\\SEMANA 8')

from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente


def mostrar_titulo():
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  DEMOSTRACIÓN: SISTEMA RESTAURANTE CON PRINCIPIOS SOLID".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")


def explicar_solid() -> None:
    """Muestra una explicación didáctica de los principios SOLID aplicada al sistema."""
    print("\n" + "="*70)
    print("   EXPLICACIÓN DE PRINCIPIOS SOLID")
    print("="*70)
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

    print("\n" + "="*70)
    print("RESUMEN: Con SOLID, el código es flexible, mantenible y escalable 📈")
    print("="*70 + "\n")


def demostrar_polimorfismo():
    """Demuestra el polimorfismo en acción."""
    print("\n" + "╔" + "="*68 + "╗")
    print("║ " + "DEMOSTRACIÓN: POLIMORFISMO CON LSP".ljust(66) + " ║")
    print("╚" + "="*68 + "╝")

    restaurante = Restaurante()

    # Crear varios productos
    print("\n📝 Creando productos (Productos normales y Bebidas):\n")

    productos_datos = [
        ("001", "Hamburguesa", "Comida", 15.50, None, None),
        ("002", "Ensalada", "Comida", 12.00, None, None),
        ("003", "Coca Cola", "Bebida", 3.50, "500ml", "Botella"),
        ("004", "Jugo Natural", "Bebida", 5.00, "250ml", "Vaso"),
        ("005", "Agua Mineral", "Bebida", 2.50, "1L", "Botella"),
    ]

    for codigo, nombre, categoria, precio, tamano, envase in productos_datos:
        if tamano and envase:
            bebida = Bebida(codigo, nombre, categoria, precio, tamano, envase)
            restaurante.registrar_producto(bebida)
            print(f"   ✓ Bebida: {nombre}")
        else:
            producto = Producto(codigo, nombre, categoria, precio)
            restaurante.registrar_producto(producto)
            print(f"   ✓ Producto: {nombre}")

    print("\n" + "-"*70)
    print("\n📋 LISTANDO PRODUCTOS CON POLIMORFISMO:\n")
    print("🔑 Clave: Restaurante NO pregunta qué tipo es cada objeto.")
    print("         Simplemente llama a: producto.mostrar_informacion()\n")

    for i, info in enumerate(restaurante.listar_productos(), 1):
        print(f"{i:2}. {info}")

    print("\n" + "-"*70)
    print("\n✅ RESULTADO: LSP en acción!")
    print("   • Producto y Bebida están en LA MISMA LISTA")
    print("   • Restaurante NO usa condicionales 'isinstance'")
    print("   • Cada objeto muestra su información a su manera")
    print("   • Este es el POLIMORFISMO que enseña los principios SOLID\n")


def demostrar_validacion():
    """Demuestra validación de códigos únicos (SRP)."""
    print("\n" + "╔" + "="*68 + "╗")
    print("║ " + "DEMOSTRACIÓN: RESPONSABILIDAD ÚNICA (SRP)".ljust(66) + " ║")
    print("╚" + "="*68 + "╝")

    print("\n🔍 VALIDACIÓN DE CÓDIGOS ÚNICOS:\n")
    print("   La lógica de validación está en RESTAURANTE, no en main.py\n")

    restaurante = Restaurante()

    p1 = Producto("P001", "Pizza", "Comida", 20.50)
    print(f"1. Registrando pizza con código 'P001': ", end="")
    if restaurante.registrar_producto(p1):
        print("✓ ÉXITO")
    else:
        print("❌ FALLO")

    p2 = Producto("P001", "Pasta", "Comida", 18.00)
    print(f"2. Intentando registrar pasta con código 'P001' (duplicado): ", end="")
    if restaurante.registrar_producto(p2):
        print("✓ ÉXITO")
    else:
        print("❌ RECHAZADO (código duplicado)")

    print("\n✅ RESULTADO: SRP en acción!")
    print("   • main.py NO valida, solo solicita datos")
    print("   • Restaurante valida que no haya duplicados")
    print("   • Si cambias la regla, editas UN SOLO LUGAR\n")


def demostrar_extension():
    """Demuestra cómo se puede extender sin modificar código (OCP)."""
    print("\n" + "╔" + "="*68 + "╗")
    print("║ " + "DEMOSTRACIÓN: ABIERTO/CERRADO (OCP)".ljust(66) + " ║")
    print("╚" + "="*68 + "╝")

    print("\n🔄 EXTENSIBILIDAD DEL SISTEMA:\n")
    print("   Ahora tenemos: Producto, Bebida")
    print("   ")
    print("   ¿Qué pasa si queremos agregar POSTRE?")
    print("   ")
    print("   SIN OCP (malo):")
    print("   ❌ Modificaríamos Restaurante para diferenciar tipos")
    print("   ❌ Agregaríamos: if isinstance(p, Bebida): ...; elif isinstance(p, Postre): ...")
    print("   ❌ RIESGO: romper código existente")
    print("   ")
    print("   CON OCP (bien):")
    print("   ✓ Creamos: class Postre(Producto): ...")
    print("   ✓ Heredamos: mostrar_informacion()")
    print("   ✓ Restaurante NO CAMBIA (cerrado para modificación)")
    print("   ✓ Pero ACEPTA Postre automáticamente (abierto para extensión)")
    print("   ")
    print("✅ RESULTADO: OCP en acción!")
    print("   • El código existente no se modifica")
    print("   • Nuevas clases se agregan sin cambiar Restaurante")
    print("   • Menos errores, más seguridad, código robusto\n")


def main():
    mostrar_titulo()
    explicar_solid()
    print("─" * 70)
    demostrar_polimorfismo()
    print("─" * 70)
    demostrar_validacion()
    print("─" * 70)
    demostrar_extension()
    print("─" * 70)

    print("\n" + "╔" + "="*68 + "╗")
    print("║ " + "CONCLUSIONES".ljust(66) + " ║")
    print("╚" + "="*68 + "╝")
    print("\n✨ RESUMEN DE LOS PRINCIPIOS SOLID EN RESTAURANTE_APP:\n")
    print("1️⃣  SRP (Single Responsibility): Cada clase tiene una responsabilidad")
    print("    → Código más fácil de entender y mantener")
    print("\n2️⃣  OCP (Open/Closed): Extensible sin modificar código existente")
    print("    → Agregar funcionalidad sin riesgo")
    print("\n3️⃣  LSP (Liskov Substitution): Polimorfismo sin condicionales")
    print("    → Código más elegante y genérico")
    print("\n" + "─" * 70)
    print("\n📌 ARCHIVOS CLAVE DEL PROYECTO:\n")
    print("   • restaurante_app/modelos/producto.py  → Clase Producto (base)")
    print("   • restaurante_app/modelos/bebida.py    → Clase Bebida (hereda Producto)")
    print("   • restaurante_app/modelos/cliente.py   → Clase Cliente (independiente)")
    print("   • restaurante_app/servicios/restaurante.py → Servicio (administra colecciones)")
    print("   • restaurante_app/main.py              → Menú interactivo\n")
    print("─" * 70)
    print("\n▶️  Para usar el sistema interactivo, ejecuta:")
    print("    python -m restaurante_app.main\n")
    print("█"*70 + "\n")


if __name__ == "__main__":
    main()

