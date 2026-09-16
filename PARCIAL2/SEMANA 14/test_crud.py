#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de prueba para validar operaciones CRUD sin interfaz gráfica
"""

import sys
import os
import json

# Ajustar ruta para importar módulos
ruta_app = os.path.join(os.path.dirname(__file__), 'restaurante_app')
sys.path.insert(0, ruta_app)

from servicios import ArchivoServicio, RestauranteServicio
from modelos import Producto

def main():
    print("=" * 60)
    print("PRUEBA DE OPERACIONES CRUD - RESTAURANTE APP SEMANA 14")
    print("=" * 60)
    
    # Inicializar servicios
    ruta_datos = os.path.join(ruta_app, 'datos')
    archivo_servicio = ArchivoServicio(ruta_datos)
    restaurante_servicio = RestauranteServicio(archivo_servicio)
    
    print("\n[1] ESTADO INICIAL")
    print("-" * 60)
    productos = restaurante_servicio.obtener_productos()
    print(f"Productos iniciales: {len(productos)}")
    for p in productos[:3]:
        print(f"  - {p.id}: {p.nombre} (${p.precio})")
    
    # Guardar estado inicial para restaurar después
    archivo_servicio_backup = ArchivoServicio(ruta_datos)
    productos_backup = archivo_servicio_backup.cargar_productos()
    
    try:
        print("\n[2] REGISTRAR NUEVO PRODUCTO")
        print("-" * 60)
        exito, resultado = restaurante_servicio.registrar_producto(
            nombre="Tacos al Pastor",
            precio=5.99,
            cantidad=75,
            descripcion="Tacos auténticos con carne al pastor"
        )
        if exito:
            print(f"✓ Producto registrado: {resultado.id} - {resultado.nombre}")
            print(f"  Precio: ${resultado.precio}, Cantidad: {resultado.cantidad}")
        else:
            print(f"✗ Error: {resultado}")
        
        print("\n[3] CARGAR PRODUCTO POR ID")
        print("-" * 60)
        exito, resultado = restaurante_servicio.cargar_producto_por_id("P001")
        if exito:
            p = resultado
            print(f"✓ Producto cargado: {p.id}")
            print(f"  Nombre: {p.nombre}")
            print(f"  Precio: ${p.precio}")
            print(f"  Cantidad: {p.cantidad}")
        else:
            print(f"✗ Error: {resultado}")
        
        print("\n[4] ACTUALIZAR PRODUCTO")
        print("-" * 60)
        exito, resultado = restaurante_servicio.actualizar_producto(
            producto_id="P001",
            nombre="Hamburguesa Premium",
            precio=11.99,
            cantidad=45,
            descripcion="Hamburguesa de primera calidad con queso importado"
        )
        if exito:
            p = resultado
            print(f"✓ Producto actualizado: {p.id} - {p.nombre}")
            print(f"  Nuevo precio: ${p.precio}")
            print(f"  Nueva cantidad: {p.cantidad}")
        else:
            print(f"✗ Error: {resultado}")
        
        print("\n[5] VERIFICAR PERSISTENCIA EN JSON")
        print("-" * 60)
        # Recargar desde archivo
        restaurante_servicio.recargar_productos()
        exito, resultado = restaurante_servicio.cargar_producto_por_id("P001")
        if exito:
            p = resultado
            if p.nombre == "Hamburguesa Premium" and p.precio == 11.99:
                print("✓ Datos persistidos correctamente en productos.json")
            else:
                print("✗ Los datos no se persistieron correctamente")
        
        print("\n[6] VALIDACIONES")
        print("-" * 60)
        test_cases = [
            ("", 10, 5, "Nombre vacío", False),
            ("Test", -5, 10, "Precio negativo", False),
            ("Test", 10, -5, "Cantidad negativa", False),
            ("Producto Válido", 15.99, 20, "Datos válidos", True),
        ]
        
        for nombre, precio, cantidad, descripcion, esperado_exito in test_cases:
            exito, _ = restaurante_servicio.registrar_producto(
                nombre, precio, cantidad, descripcion
            )
            estado = "✓" if exito == esperado_exito else "✗"
            print(f"{estado} {descripcion}: {exito}")
        
        print("\n[7] LISTAR PRODUCTOS FINALES")
        print("-" * 60)
        productos_finales = restaurante_servicio.obtener_productos()
        print(f"Total de productos: {len(productos_finales)}")
        for p in productos_finales:
            print(f"  - {p.id}: {p.nombre} (${p.precio}) x{p.cantidad}")
        
        print("\n[8] ELIMINAR PRODUCTO")
        print("-" * 60)
        # Eliminar el producto que agregamos (Producto Válido)
        if len(productos_finales) > len(productos_backup):
            ultimo_id = productos_finales[-1].id
            exito, mensaje = restaurante_servicio.eliminar_producto(ultimo_id)
            if exito:
                print(f"✓ {mensaje}")
            else:
                print(f"✗ Error: {mensaje}")
        
        print("\n[9] ESTADO FINAL")
        print("-" * 60)
        productos_final = restaurante_servicio.obtener_productos()
        print(f"Productos finales: {len(productos_final)}")
        
    except Exception as e:
        print(f"\n✗ ERROR NO ESPERADO: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        print("\n[10] RESTAURAR ESTADO INICIAL")
        print("-" * 60)
        # Restaurar productos originales
        archivo_servicio.guardar_productos(productos_backup)
        restaurante_servicio.recargar_productos()
        print("✓ Estado inicial restaurado")
    
    print("\n" + "=" * 60)
    print("PRUEBAS COMPLETADAS")
    print("=" * 60)

if __name__ == "__main__":
    main()
