#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests para validar CRUD de Usuarios en RestauranteServicio
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'restaurante_app'))

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from modelos import Usuario

def test_registrar_usuario():
    """Test: Registrar un nuevo usuario"""
    print("\n[TEST 1] Registrar usuario...")
    servicio = RestauranteServicio(ArchivoServicio('restaurante_app/datos'))
    usuarios_antes = len(servicio.usuarios)
    
    exito, resultado = servicio.registrar_usuario("Test User", "testuser", "pass123", "cliente")
    
    assert exito, f"Debería registrar usuario, pero falló: {resultado}"
    assert resultado.nombre == "Test User", "El nombre no coincide"
    assert resultado.usuario == "testuser", "El usuario no coincide"
    assert len(servicio.usuarios) == usuarios_antes + 1, "La lista de usuarios no aumentó"
    print(f"  ✓ Usuario registrado: {resultado.id} - {resultado.nombre}")


def test_cargar_usuario_por_id():
    """Test: Cargar un usuario por ID"""
    print("\n[TEST 2] Cargar usuario por ID...")
    servicio = RestauranteServicio(ArchivoServicio('restaurante_app/datos'))
    
    # Obtener el primer usuario
    usuarios = servicio.obtener_usuarios()
    assert len(usuarios) > 0, "No hay usuarios en la base de datos"
    usuario_original = usuarios[0]
    
    exito, usuario_cargado = servicio.cargar_usuario_por_id(usuario_original.id)
    
    assert exito, f"Debería cargar usuario, pero falló: {usuario_cargado}"
    assert usuario_cargado.id == usuario_original.id, "El ID no coincide"
    print(f"  ✓ Usuario cargado: {usuario_cargado.nombre}")


def test_actualizar_usuario():
    """Test: Actualizar un usuario existente"""
    print("\n[TEST 3] Actualizar usuario...")
    servicio = RestauranteServicio(ArchivoServicio('restaurante_app/datos'))
    
    usuarios = servicio.obtener_usuarios()
    usuario_id = usuarios[-1].id  # Usar el último usuario
    
    exito, resultado = servicio.actualizar_usuario(
        usuario_id, "Nombre Actualizado", "usuario_actualizado", "pass456", "gerente"
    )
    
    assert exito, f"Debería actualizar usuario, pero falló: {resultado}"
    assert resultado.nombre == "Nombre Actualizado", "El nombre no se actualizó"
    assert resultado.rol == "gerente", "El rol no se actualizó"
    print(f"  ✓ Usuario actualizado: {resultado.nombre} ({resultado.rol})")


def test_eliminar_usuario():
    """Test: Eliminar un usuario"""
    print("\n[TEST 4] Eliminar usuario...")
    servicio = RestauranteServicio(ArchivoServicio('restaurante_app/datos'))
    
    # Registrar un usuario para eliminarlo
    exito_reg, usuario_nuevo = servicio.registrar_usuario("Usuario a Eliminar", "eliminar_me", "pass", "cliente")
    assert exito_reg, "No se pudo registrar usuario de prueba"
    usuario_id = usuario_nuevo.id
    
    usuarios_antes = len(servicio.usuarios)
    exito, mensaje = servicio.eliminar_usuario(usuario_id)
    
    assert exito, f"Debería eliminar usuario, pero falló: {mensaje}"
    assert len(servicio.usuarios) == usuarios_antes - 1, "La lista de usuarios no disminuyó"
    print(f"  ✓ Usuario eliminado: {usuario_id}")


def test_validacion_usuario_duplicado():
    """Test: Validar que no se permita usuario duplicado"""
    print("\n[TEST 5] Validar usuario duplicado...")
    servicio = RestauranteServicio(ArchivoServicio('restaurante_app/datos'))
    
    usuarios = servicio.obtener_usuarios()
    usuario_existente = usuarios[0]
    
    exito, mensaje = servicio.registrar_usuario(
        "Otro Nombre", usuario_existente.usuario, "pass", "cliente"
    )
    
    assert not exito, "Debería fallar con usuario duplicado"
    assert "ya existe" in mensaje.lower(), "Mensaje de error incorrecto"
    print(f"  ✓ Validación correcta: {mensaje}")


def test_validacion_campos_vacios():
    """Test: Validar campos vacíos"""
    print("\n[TEST 6] Validar campos vacíos...")
    servicio = RestauranteServicio(ArchivoServicio('restaurante_app/datos'))
    
    # Nombre vacío
    exito, mensaje = servicio.registrar_usuario("", "usuario", "pass", "cliente")
    assert not exito, "Debería fallar con nombre vacío"
    print(f"  ✓ Validación nombre vacío: {mensaje}")
    
    # Usuario vacío
    exito, mensaje = servicio.registrar_usuario("Nombre", "", "pass", "cliente")
    assert not exito, "Debería fallar con usuario vacío"
    print(f"  ✓ Validación usuario vacío: {mensaje}")
    
    # Contraseña vacía
    exito, mensaje = servicio.registrar_usuario("Nombre", "usuario", "", "cliente")
    assert not exito, "Debería fallar con contraseña vacía"
    print(f"  ✓ Validación contraseña vacía: {mensaje}")


def test_persistencia_usuarios():
    """Test: Verificar que se guarden cambios en JSON"""
    print("\n[TEST 7] Persistencia en JSON...")
    
    # Crear servicio y registrar usuario
    servicio = RestauranteServicio(ArchivoServicio('restaurante_app/datos'))
    exito, usuario_nuevo = servicio.registrar_usuario("Usuario Persistencia", "persist_user", "pass", "cliente")
    assert exito, "No se pudo registrar usuario"
    usuario_id = usuario_nuevo.id
    
    # Crear nuevo servicio y verificar que el usuario sigue ahí
    servicio2 = RestauranteServicio(ArchivoServicio('restaurante_app/datos'))
    usuarios = servicio2.obtener_usuarios()
    usuario_encontrado = any(u.id == usuario_id for u in usuarios)
    
    assert usuario_encontrado, "El usuario no se guardó en JSON"
    print(f"  ✓ Usuario persistido: {usuario_id}")
    
    # Limpiar: eliminar el usuario de prueba
    servicio2.eliminar_usuario(usuario_id)
    print(f"  ✓ Usuario de prueba eliminado")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("PRUEBAS DE CRUD DE USUARIOS")
    print("="*60)
    
    try:
        test_registrar_usuario()
        test_cargar_usuario_por_id()
        test_actualizar_usuario()
        test_validacion_usuario_duplicado()
        test_validacion_campos_vacios()
        test_eliminar_usuario()
        test_persistencia_usuarios()
        
        print("\n" + "="*60)
        print("✅ TODOS LOS TESTS PASARON (7/7)")
        print("="*60 + "\n")
    except AssertionError as e:
        print(f"\n❌ ERROR: {e}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
