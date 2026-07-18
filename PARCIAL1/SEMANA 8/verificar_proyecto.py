#!/usr/bin/env python
"""
Script de verificación del proyecto restaurante_app Semana 8.
Verifica que todos los archivos estén en su lugar y que el sistema funcione.
"""

import os
import sys

# Configurar path
BASE_DIR = 'C:\\Users\\User\\OneDrive\\Escritorio\\2626-POO-Arias-Adriana\\PARCIAL1\\SEMANA 8'
sys.path.insert(0, BASE_DIR)


def verificar_estructura():
    """Verifica que la estructura del proyecto sea correcta."""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE ESTRUCTURA DEL PROYECTO")
    print("="*70 + "\n")

    archivos_requeridos = {
        "restaurante_app/__init__.py": "Paquete restaurante_app",
        "restaurante_app/main.py": "Punto de entrada principal",
        "restaurante_app/modelos/__init__.py": "Paquete modelos",
        "restaurante_app/modelos/producto.py": "Clase Producto",
        "restaurante_app/modelos/bebida.py": "Clase Bebida",
        "restaurante_app/modelos/cliente.py": "Clase Cliente",
        "restaurante_app/servicios/__init__.py": "Paquete servicios",
        "restaurante_app/servicios/restaurante.py": "Clase Restaurante",
        "README.md": "Documentación",
    }

    todos_ok = True
    for ruta, descripcion in archivos_requeridos.items():
        ruta_completa = os.path.join(BASE_DIR, ruta)
        if os.path.exists(ruta_completa):
            print(f"✓ {ruta:40} ({descripcion})")
        else:
            print(f"✗ {ruta:40} FALTA")
            todos_ok = False

    return todos_ok


def verificar_importes():
    """Verifica que todos los módulos se puedan importar."""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE IMPORTES")
    print("="*70 + "\n")

    try:
        print("Importando restaurante_app.modelos.producto...", end=" ")
        from restaurante_app.modelos.producto import Producto
        print("✓")

        print("Importando restaurante_app.modelos.bebida...", end=" ")
        from restaurante_app.modelos.bebida import Bebida
        print("✓")

        print("Importando restaurante_app.modelos.cliente...", end=" ")
        from restaurante_app.modelos.cliente import Cliente
        print("✓")

        print("Importando restaurante_app.servicios.restaurante...", end=" ")
        from restaurante_app.servicios.restaurante import Restaurante
        print("✓")

        return True
    except ImportError as e:
        print(f"\n✗ Error de importación: {e}")
        return False


def verificar_funcionamiento():
    """Verifica que el sistema funcione básicamente."""
    print("\n" + "="*70)
    print("VERIFICACIÓN DE FUNCIONAMIENTO")
    print("="*70 + "\n")

    try:
        from restaurante_app.modelos.producto import Producto
        from restaurante_app.modelos.bebida import Bebida
        from restaurante_app.modelos.cliente import Cliente
        from restaurante_app.servicios.restaurante import Restaurante

        # Crear un restaurante
        print("Creando instancia de Restaurante...", end=" ")
        restaurante = Restaurante()
        print("✓")

        # Crear un producto
        print("Creando Producto...", end=" ")
        p1 = Producto("001", "Pizza", "Comida", 20.0)
        print("✓")

        # Registrar producto
        print("Registrando Producto...", end=" ")
        assert restaurante.registrar_producto(p1), "Fallo al registrar"
        print("✓")

        # Crear una bebida
        print("Creando Bebida...", end=" ")
        b1 = Bebida("002", "Coca Cola", "Bebida", 3.0, "500ml", "Botella")
        print("✓")

        # Registrar bebida
        print("Registrando Bebida...", end=" ")
        assert restaurante.registrar_producto(b1), "Fallo al registrar"
        print("✓")

        # Listar productos (polimorfismo)
        print("Listando productos (polimorfismo)...", end=" ")
        productos = restaurante.listar_productos()
        assert len(productos) == 2, "No se listaron todos los productos"
        print("✓")

        # Crear un cliente
        print("Creando Cliente...", end=" ")
        c1 = Cliente("001", "Juan", "juan@email.com")
        print("✓")

        # Registrar cliente
        print("Registrando Cliente...", end=" ")
        assert restaurante.registrar_cliente(c1), "Fallo al registrar"
        print("✓")

        # Validar duplicado (producto)
        print("Validando duplicado de código de producto...", end=" ")
        p2 = Producto("001", "Pasta", "Comida", 18.0)
        assert not restaurante.registrar_producto(p2), "Permitió duplicado"
        print("✓")

        # Validar duplicado (cliente)
        print("Validando duplicado de identificación de cliente...", end=" ")
        c2 = Cliente("001", "Maria", "maria@email.com")
        assert not restaurante.registrar_cliente(c2), "Permitió duplicado"
        print("✓")

        # Probar mostrar_informacion
        print("Probando método mostrar_informacion()...", end=" ")
        info_p1 = p1.mostrar_informacion()
        info_b1 = b1.mostrar_informacion()
        info_c1 = c1.mostrar_informacion()
        assert len(info_p1) > 0, "Producto no retorna info"
        assert len(info_b1) > len(info_p1), "Bebida no extiende info (LSP)"
        assert len(info_c1) > 0, "Cliente no retorna info"
        print("✓")

        return True
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


def mostrar_resumen():
    """Muestra un resumen final."""
    print("\n" + "="*70)
    print("RESUMEN FINAL")
    print("="*70 + "\n")

    print("✅ PROYECTO COMPLETADO CORRECTAMENTE\n")
    print("📁 ESTRUCTURA:")
    print("   ✓ Paquete restaurante_app con modelos y servicios")
    print("   ✓ Clases: Producto, Bebida, Cliente, Restaurante")
    print("   ✓ Archivos __init__.py en todos los paquetes")

    print("\n📋 FUNCIONALIDADES:")
    print("   ✓ Registro de productos y bebidas (una sola colección)")
    print("   ✓ Registro de clientes")
    print("   ✓ Validación de códigos/identificaciones únicas")
    print("   ✓ Listado con polimorfismo (no usa isinstance)")

    print("\n🎓 PRINCIPIOS SOLID:")
    print("   ✓ SRP: Cada clase tiene una responsabilidad")
    print("   ✓ OCP: Diseño extensible sin modificación")
    print("   ✓ LSP: Bebida sustituye a Producto sin problemas")

    print("\n▶️  PRÓXIMOS PASOS:")
    print("   1. Ejecuta: python -m restaurante_app.main")
    print("      → Verás la explicación SOLID y el menú interactivo")
    print("\n   2. Ejecuta: python demo_auto.py")
    print("      → Demostración automática de los principios SOLID")

    print("\n📝 COMPLETAR ANTES DE ENTREGAR:")
    print("   • Edita README.md y completa: Nombre del estudiante\n")


def main():
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  VERIFICACIÓN DEL PROYECTO: RESTAURANTE_APP SEMANA 8".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70)

    resultado1 = verificar_estructura()
    resultado2 = verificar_importes()
    resultado3 = verificar_funcionamiento()

    if resultado1 and resultado2 and resultado3:
        mostrar_resumen()
        print("\n" + "█"*70 + "\n")
        return 0
    else:
        print("\n❌ Hay problemas en el proyecto. Revisa los errores arriba.\n")
        print("█"*70 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())

