#!/usr/bin/env python3
"""Script de pruebas automatizadas para restaurante_app Semana 11."""

import sys
import json
import tempfile
import os
from pathlib import Path

# Agregar la carpeta restaurante_app al path
sys.path.insert(0, str(Path(__file__).resolve().parent / "restaurante_app"))

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


def test_producto_con_stock():
    """Prueba crear un producto con stock."""
    print("\n🧪 Prueba 1: Crear Producto con stock")
    try:
        p = Producto("BURGER1", "Hamburguesa", "Platos", 10.50, 20)
        assert p.codigo == "BURGER1"
        assert p.stock == 20
        assert "Stock: 20" in p.mostrar_informacion()
        print("  ✓ Producto creado correctamente con stock")
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def test_producto_vender():
    """Prueba la operación vender de producto."""
    print("\n🧪 Prueba 2: Vender producto (disminuir stock)")
    try:
        p = Producto("BURGER1", "Hamburguesa", "Platos", 10.50, 20)
        p.vender(5)
        assert p.stock == 15
        print("  ✓ Stock disminuyó correctamente (20 -> 15)")
        
        # Intentar vender más del stock
        try:
            p.vender(20)
            print("  ❌ Debería haber lanzado error por stock insuficiente")
            return False
        except ValueError:
            print("  ✓ Correctamente rechazó venta con stock insuficiente")
            return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def test_usuario_persistencia():
    """Prueba to_dict y from_dict de Usuario."""
    print("\n🧪 Prueba 3: Usuario - Persistencia (to_dict/from_dict)")
    try:
        u = Usuario("12345", "Juan Pérez", "juan@test.com")
        d = u.to_dict()
        u2 = Usuario.from_dict(d)
        assert u2.identificacion == "12345"
        assert u2.nombre == "Juan Pérez"
        print("  ✓ Usuario persistencia funcionando")
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def test_venta_modelo():
    """Prueba crear una Venta."""
    print("\n🧪 Prueba 4: Crear objeto Venta")
    try:
        v = Venta("12345", "BURGER1", 3)
        assert v.usuario_id == "12345"
        assert v.producto_codigo == "BURGER1"
        assert v.cantidad == 3
        d = v.to_dict()
        v2 = Venta.from_dict(d)
        assert v2.cantidad == 3
        print("  ✓ Venta creada y persistencia funcionando")
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def test_restaurante_venta():
    """Prueba la operación vender_producto en Restaurante."""
    print("\n🧪 Prueba 5: Vender producto a través de Restaurante")
    try:
        r = Restaurante()
        p = Producto("BURGER1", "Hamburguesa", "Platos", 10.50, 20)
        u = Usuario("12345", "Juan", "juan@test.com")
        
        r.registrar_producto(p)
        r.registrar_usuario(u)
        
        # Venta válida
        resultado = r.vender_producto("BURGER1", "12345", 3)
        assert resultado is True
        assert p.stock == 17
        print("  ✓ Venta válida registrada, stock disminuyó (20 -> 17)")
        
        # Venta con stock insuficiente
        resultado = r.vender_producto("BURGER1", "12345", 20)
        assert resultado is False
        assert p.stock == 17
        print("  ✓ Venta rechazada por stock insuficiente, datos no modificados")
        
        # Venta con usuario inexistente
        resultado = r.vender_producto("BURGER1", "99999", 1)
        assert resultado is False
        print("  ✓ Venta rechazada por usuario inexistente")
        
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def test_consultar_ventas_usuario():
    """Prueba obtener ventas de un usuario."""
    print("\n🧪 Prueba 6: Consultar ventas de usuario")
    try:
        r = Restaurante()
        p1 = Producto("BURGER1", "Hamburguesa", "Platos", 10.50, 20)
        p2 = Producto("PIZZA1", "Pizza", "Platos", 15.00, 15)
        u = Usuario("12345", "Juan", "juan@test.com")
        
        r.registrar_producto(p1)
        r.registrar_producto(p2)
        r.registrar_usuario(u)
        
        r.vender_producto("BURGER1", "12345", 2)
        r.vender_producto("PIZZA1", "12345", 1)
        
        ventas = r.obtener_ventas_usuario("12345")
        assert len(ventas) == 2
        print("  ✓ Se recuperaron 2 ventas del usuario")
        
        ventas_usuario_inexistente = r.obtener_ventas_usuario("99999")
        assert len(ventas_usuario_inexistente) == 0
        print("  ✓ Usuario sin ventas retorna lista vacía")
        
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def test_persistencia_json():
    """Prueba guardar y cargar desde JSON."""
    print("\n🧪 Prueba 7: Persistencia JSON (cargar/guardar)")
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            ruta_p = os.path.join(tmpdir, "productos.json")
            ruta_u = os.path.join(tmpdir, "usuarios.json")
            ruta_v = os.path.join(tmpdir, "ventas.json")
            
            # Crear y guardar
            r = Restaurante()
            p = Producto("BURGER1", "Hamburguesa", "Platos", 10.50, 20)
            u = Usuario("12345", "Juan", "juan@test.com")
            r.registrar_producto(p)
            r.registrar_usuario(u)
            r.vender_producto("BURGER1", "12345", 3)
            
            archivo = ArchivoServicio(ruta_p, ruta_u, ruta_v)
            archivo.guardar_productos(r.obtener_productos_como_lista())
            archivo.guardar_usuarios(r.obtener_usuarios_como_lista())
            archivo.guardar_ventas(r.obtener_ventas_como_lista())
            print("  ✓ Datos guardados en JSON")
            
            # Cargar en nuevo restaurante
            r2 = Restaurante()
            
            prods = archivo.cargar_productos()
            for prod_dict in prods:
                prod = Producto.from_dict(prod_dict)
                r2.registrar_producto(prod)
            
            usus = archivo.cargar_usuarios()
            for usu_dict in usus:
                usu = Usuario.from_dict(usu_dict)
                r2.registrar_usuario(usu)
            
            ventas = archivo.cargar_ventas()
            for venta_dict in ventas:
                venta = Venta.from_dict(venta_dict)
                r2.cargar_ventas([venta])
            
            # Verificar
            assert len(r2.listar_productos()) == 1
            assert len(r2.listar_usuarios()) == 1
            assert len(r2.listar_todas_ventas()) == 1
            
            prod_recuperado = r2.buscar_producto_por_codigo("BURGER1")
            assert prod_recuperado.stock == 17
            
            print("  ✓ Datos recuperados correctamente")
            print("  ✓ Stock se recuperó correctamente (17)")
            return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def test_archivo_no_existe():
    """Prueba cargar desde archivo inexistente."""
    print("\n🧪 Prueba 8: Manejo de archivo inexistente")
    try:
        archivo = ArchivoServicio(
            "/ruta/inexistente/productos.json",
            "/ruta/inexistente/usuarios.json",
            "/ruta/inexistente/ventas.json"
        )
        
        prods = archivo.cargar_productos()
        usus = archivo.cargar_usuarios()
        ventas = archivo.cargar_ventas()
        
        assert prods == []
        assert usus == []
        assert ventas == []
        
        print("  ✓ Archivos inexistentes retornan listas vacías (no error)")
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def run_all_tests():
    """Ejecuta todas las pruebas."""
    print("=" * 60)
    print("  PRUEBAS AUTOMATIZADAS - RESTAURANTE APP SEMANA 11")
    print("=" * 60)
    
    tests = [
        test_producto_con_stock,
        test_producto_vender,
        test_usuario_persistencia,
        test_venta_modelo,
        test_restaurante_venta,
        test_consultar_ventas_usuario,
        test_persistencia_json,
        test_archivo_no_existe,
    ]
    
    resultados = []
    for test in tests:
        try:
            resultados.append(test())
        except Exception as e:
            print(f"  ❌ Excepción no controlada: {e}")
            resultados.append(False)
    
    print("\n" + "=" * 60)
    total = len(resultados)
    pasadas = sum(resultados)
    print(f"  RESULTADO: {pasadas}/{total} pruebas pasaron")
    
    if pasadas == total:
        print("  ✓ ¡TODAS LAS PRUEBAS PASARON!")
    else:
        print(f"  ❌ {total - pasadas} prueba(s) fallaron")
    
    print("=" * 60 + "\n")
    
    return pasadas == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
