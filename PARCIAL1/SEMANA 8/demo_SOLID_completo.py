#!/usr/bin/env python
"""
Demostración completa del software restaurante_app con explicación SOLID
Este script simula las interacciones del usuario para mostrar cómo funciona.
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


def demostrar_srp():
    """Demuestra el Principio de Responsabilidad Única."""
    print("\n" + "╔" + "="*68 + "╗")
    print("║ " + "DEMOSTRACIÓN 1: RESPONSABILIDAD ÚNICA (SRP)".ljust(66) + " ║")
    print("╚" + "="*68 + "╝")

    print("\nEn este proyecto, SRP se cumple así:\n")
    print("1️⃣  MODELOS (Producto, Bebida, Cliente):")
    print("    ├─ Responsabilidad: Guardar datos y su representación")
    print("    ├─ ¿Qué hacen?: Almacenan atributos y el método mostrar_informacion()")
    print("    └─ Código no toca: Administración de colecciones, interacción con usuario")

    print("\n2️⃣  SERVICIOS (Restaurante):")
    print("    ├─ Responsabilidad: Administrar colecciones y reglas")
    print("    ├─ ¿Qué hace?: Registra, busca, lista productos y clientes")
    print("    ├─ Valida: Códigos únicos, identificaciones únicas")
    print("    └─ No toca: Creación de objetos, interacción con usuario")

    print("\n3️⃣  MAIN (Interacción):")
    print("    ├─ Responsabilidad: Mostrar menú e interactuar con el usuario")
    print("    ├─ ¿Qué hace?: Solicita datos, crea objetos, llama al servicio")
    print("    └─ No toca: Lógica de negocio, administración de datos")

    print("\n✅ RESULTADO: Si necesitas cambiar la lógica de registro, solo editas Restaurante.")
    print("           Si necesitas cambiar el formato del menú, solo editas main.py.\n")


def demostrar_ocp():
    """Demuestra el Principio Abierto/Cerrado."""
    print("\n" + "╔" + "="*68 + "╗")
    print("║ " + "DEMOSTRACIÓN 2: ABIERTO/CERRADO (OCP)".ljust(66) + " ║")
    print("╚" + "="*68 + "╝")

    print("\nEl código está CERRADO para modificación, ABIERTO para extensión:\n")

    print("Ahora mismo tenemos:")
    print("    • Producto (clase base)")
    print("    • Bebida (hereda de Producto)")

    print("\n¿Qué pasa si queremos agregar PLATILLO?\n")
    print("Código ANTES (Sin OCP):")
    print("    ❌ Modificaríamos Restaurante para diferenciar Bebidas y Platillos")
    print("    ❌ Agregaríamos condiciones: if isinstance(p, Bebida): ... elif isinstance(p, Platillo): ...")
    print("    ❌ El código original se modifica (RIESGO)")

    print("\nCódigo AHORA (Con OCP):")
    print("    ✓ Creamos: class Platillo(Producto)")
    print("    ✓ Heredamos: mostrar_informacion()")
    print("    ✓ Restaurante NO CAMBIA: sigue iterando y llamando mostrar_informacion()")
    print("    ✓ POLIMORFISMO: cada objeto responde a su manera")

    print("\n✅ RESULTADO: El código es EXTENSIBLE sin riesgo de romper lo existente.\n")


def demostrar_lsp():
    """Demuestra el Principio de Sustitución de Liskov."""
    print("\n" + "╔" + "="*68 + "╗")
    print("║ " + "DEMOSTRACIÓN 3: SUSTITUCIÓN DE LISKOV (LSP) - POLIMORFISMO".ljust(66) + " ║")
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

    print("\n" + "─"*70)
    print("\n📋 LISTANDO PRODUCTOS CON POLIMORFISMO:\n")
    print("🔑 Clave: Restaurante NO pregunta qué tipo es cada objeto.")
    print("         Simplemente llama a: producto.mostrar_informacion()\n")

    for i, info in enumerate(restaurante.listar_productos(), 1):
        print(f"{i:2}. {info}")

    print("\n" + "─"*70)
    print("\n✅ RESULTADO: LSP en acción!")
    print("   • Producto y Bebida están en LA MISMA LISTA")
    print("   • Restaurante usa POLIMORFISMO: una sola línea para todos")
    print("   • Cada objeto muestra su información a su manera")
    print("   • NO hay condicionales tipo: 'if isinstance(x, Bebida)'\n")


def demostrar_ejemplo_codigo():
    """Muestra el código actual que demuestra SOLID."""
    print("\n" + "╔" + "="*68 + "╗")
    print("║ " + "EL CÓDIGO QUE DEMUESTRA SOLID".ljust(66) + " ║")
    print("╚" + "="*68 + "╝")

    print("\n📄 En servicios/restaurante.py, línea con POLIMORFISMO:\n")
    print("    def listar_productos(self) -> List[str]:")
    print("        return [p.mostrar_informacion() for p in self._productos]")
    print("                 ↑")
    print("        Sin preguntar el tipo, simplemente usa mostrar_informacion()")

    print("\n📄 En modelos/bebida.py, línea que sobrescribe:\n")
    print("    class Bebida(Producto):")
    print("        def mostrar_informacion(self) -> str:")
    print("            base = super().mostrar_informacion()")
    print("            return f\"{base} | Tamaño: {self.tamano} | Envase: {self.envase}\"")
    print("                     ↑")
    print("        Bebida amplía pero mantiene la firma (LSP ✓)")

    print("\n✅ ESTO ES POLIMORFISMO: cada clase responde distinto al mismo llamado.\n")


def main():
    mostrar_titulo()

    # Primera: explicación teórica
    explicar_solid()
    input("Presiona ENTER para ver DEMOSTRACIÓN 1 de SRP...")

    demostrar_srp()
    input("Presiona ENTER para ver DEMOSTRACIÓN 2 de OCP...")

    demostrar_ocp()
    input("Presiona ENTER para ver DEMOSTRACIÓN 3 de LSP (Polimorfismo)...")

    demostrar_lsp()
    input("Presiona ENTER para ver el código que demuestra SOLID...")

    demostrar_ejemplo_codigo()

    print("╔" + "="*68 + "╗")
    print("║ " + "CONCLUSIONES".ljust(66) + " ║")
    print("╚" + "="*68 + "╝")
    print("\n✨ RESUMEN DE LOS PRINCIPIOS SOLID EN RESTAURANTE_APP:\n")
    print("1. SRP: Cada clase tiene una responsabilidad. Código más limpio.")
    print("2. OCP: Extensible sin modificar código existente. Menos errores.")
    print("3. LSP: Polimorfismo sin condicionales. Código más elegante.\n")
    print("Ahora ejecuta: python -m restaurante_app.main")
    print("              Para usar el sistema interactivo y probar tú mismo.\n")
    print("█"*70 + "\n")


if __name__ == "__main__":
    main()

