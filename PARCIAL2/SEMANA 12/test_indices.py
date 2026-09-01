#!/usr/bin/env python
"""Script de prueba para validar los índices de SEMANA 12."""

import sys
from pathlib import Path

# Ajustar ruta para importar restaurante_app
sys.path.insert(0, str(Path(__file__).parent))

from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta


def prueba_indices():
    """Ejecuta pruebas de los índices implementados."""
    print("=" * 60)
    print("PRUEBA DE ÍNDICES - SEMANA 12")
    print("=" * 60)
    
    restaurante = Restaurante()
    
    # Test 1: Registrar y buscar productos
    print("\n✓ TEST 1: Índice de Productos (Dict[str, Producto])")
    print("-" * 60)
    
    p1 = Producto("P001", "Pizza Margherita", "Pizzas", 12.50, 10)
    p2 = Producto("P002", "Hamburguesa", "Hamburguesas", 8.99, 15)
    
    restaurante.registrar_producto(p1)
    restaurante.registrar_producto(p2)
    print(f"  Productos registrados: 2")
    print(f"  Tamaño del índice: {len(restaurante._productos_index)}")
    
    # Búsqueda rápida O(1)
    encontrado = restaurante.buscar_producto_por_codigo("P001")
    print(f"  Búsqueda 'P001': {encontrado.nombre if encontrado else 'No encontrado'}")
    assert encontrado is not None and encontrado.nombre == "Pizza Margherita"
    
    # Test 2: Registrar y buscar usuarios
    print("\n✓ TEST 2: Índice de Usuarios (Dict[str, Usuario])")
    print("-" * 60)
    
    u1 = Usuario("1001", "Juan Pérez", "juan@email.com")
    u2 = Usuario("1002", "María González", "maria@email.com")
    
    restaurante.registrar_usuario(u1)
    restaurante.registrar_usuario(u2)
    print(f"  Usuarios registrados: 2")
    print(f"  Tamaño del índice: {len(restaurante._usuarios_index)}")
    
    # Búsqueda rápida O(1)
    encontrado = restaurante.buscar_usuario_por_id("1001")
    print(f"  Búsqueda '1001': {encontrado.nombre if encontrado else 'No encontrado'}")
    assert encontrado is not None and encontrado.nombre == "Juan Pérez"
    
    # Test 3: Índice de ventas por usuario
    print("\n✓ TEST 3: Índice de Ventas por Usuario (Dict[str, List[Venta]])")
    print("-" * 60)
    
    # Realizar venta
    resultado = restaurante.vender_producto("P001", "1001", 2)
    print(f"  Venta realizada (2 pizzas a Juan): {resultado}")
    print(f"  Stock actualizado P001: {p1.stock}")
    print(f"  Tamaño dict ventas_por_usuario: {len(restaurante._ventas_por_usuario)}")
    
    # Consultar ventas del usuario (O(1) acceso al dict)
    ventas = restaurante.obtener_ventas_usuario("1001")
    print(f"  Ventas de usuario '1001': {len(ventas)} registros")
    print(f"  Venta: {ventas[0] if ventas else 'Ninguna'}")
    assert len(ventas) == 1
    
    # Segunda venta del mismo usuario
    resultado2 = restaurante.vender_producto("P002", "1001", 1)
    print(f"  Segunda venta realizada (1 hamburguesa a Juan): {resultado2}")
    ventas = restaurante.obtener_ventas_usuario("1001")
    print(f"  Ventas totales de usuario '1001': {len(ventas)} registros")
    assert len(ventas) == 2
    
    # Test 4: Sincronización de índices
    print("\n✓ TEST 4: Sincronización de Índices")
    print("-" * 60)
    
    # Verificar que el índice se actualiza con nuevos registros
    assert "P001" in restaurante._productos_index
    assert "1001" in restaurante._usuarios_index
    assert "1001" in restaurante._ventas_por_usuario
    print("  ✓ Índices sincronizados con colecciones principales")
    
    # Test 5: Coherencia entre listas e índices
    print("\n✓ TEST 5: Coherencia Listas vs Índices")
    print("-" * 60)
    
    print(f"  Productos en lista: {len(restaurante._productos)}")
    print(f"  Productos en índice: {len(restaurante._productos_index)}")
    assert len(restaurante._productos) == len(restaurante._productos_index)
    
    print(f"  Usuarios en lista: {len(restaurante._usuarios)}")
    print(f"  Usuarios en índice: {len(restaurante._usuarios_index)}")
    assert len(restaurante._usuarios) == len(restaurante._usuarios_index)
    
    print(f"  Ventas en lista: {len(restaurante._ventas)}")
    print(f"  Ventas agrupadas por usuario: {sum(len(v) for v in restaurante._ventas_por_usuario.values())}")
    assert len(restaurante._ventas) == sum(len(v) for v in restaurante._ventas_por_usuario.values())
    
    print("\n" + "=" * 60)
    print("✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    prueba_indices()
