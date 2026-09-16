#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de integración para verificar que MainView funciona con CRUD de usuarios
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'restaurante_app'))

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.main_view import MainView

def test_main_view_structure():
    """Test: Verificar que MainView tiene todos los métodos de usuarios"""
    print("\n[TEST] Estructura de MainView con métodos de usuarios...")
    
    # Crear mock root (no necesitamos GUI)
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()  # Ocultar ventana
    
    # Inicializar servicio
    archivo_servicio = ArchivoServicio('restaurante_app/datos')
    restaurante_servicio = RestauranteServicio(archivo_servicio)
    
    # Validar acceso
    exito, _ = restaurante_servicio.validar_acceso("juan", "123456")
    assert exito, "No se pudo validar acceso"
    
    # Crear MainView
    def mock_logout():
        pass
    
    main_view = MainView(root, restaurante_servicio, mock_logout)
    
    # Verificar atributos de usuarios
    assert hasattr(main_view, 'listbox_usuarios'), "Falta listbox_usuarios"
    assert hasattr(main_view, 'entry_nombre_usuario'), "Falta entry_nombre_usuario"
    assert hasattr(main_view, 'entry_usuario_usuario'), "Falta entry_usuario_usuario"
    assert hasattr(main_view, 'entry_contrasena'), "Falta entry_contrasena"
    assert hasattr(main_view, 'combo_rol'), "Falta combo_rol"
    
    print("  ✓ Widgets de usuarios presentes")
    
    # Verificar métodos de usuarios
    metodos_usuarios = [
        '_nuevo_usuario',
        '_on_select_usuario',
        '_cargar_usuario_en_formulario',
        '_guardar_usuario',
        '_actualizar_usuario',
        '_eliminar_usuario',
        '_limpiar_formulario_usuarios',
        '_actualizar_listbox_usuarios'
    ]
    
    for metodo in metodos_usuarios:
        assert hasattr(main_view, metodo), f"Falta método {metodo}"
        assert callable(getattr(main_view, metodo)), f"El método {metodo} no es callable"
    
    print(f"  ✓ Todos los {len(metodos_usuarios)} métodos de usuarios presentes y callable")
    
    # Verificar que la lista se cargó
    elementos_listbox = main_view.listbox_usuarios.size()
    assert elementos_listbox > 0, "Listbox de usuarios está vacío"
    print(f"  ✓ Listbox de usuarios cargado con {elementos_listbox} elementos")
    
    # Limpiar
    root.destroy()
    
    return True


def test_variables_usuarios():
    """Test: Verificar que las StringVar de usuarios están definidas"""
    print("\n[TEST] Variables StringVar para usuarios...")
    
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    
    archivo_servicio = ArchivoServicio('restaurante_app/datos')
    restaurante_servicio = RestauranteServicio(archivo_servicio)
    restaurante_servicio.validar_acceso("juan", "123456")
    
    def mock_logout():
        pass
    
    main_view = MainView(root, restaurante_servicio, mock_logout)
    
    # Verificar variables
    assert hasattr(main_view, 'var_id_usuario'), "Falta var_id_usuario"
    assert hasattr(main_view, 'var_nombre_usuario'), "Falta var_nombre_usuario"
    assert hasattr(main_view, 'var_usuario_usuario'), "Falta var_usuario_usuario"
    assert hasattr(main_view, 'var_contrasena'), "Falta var_contrasena"
    assert hasattr(main_view, 'var_rol'), "Falta var_rol"
    
    print("  ✓ Todas las StringVar de usuarios presentes")
    
    # Pruebar establecer y obtener valores
    main_view.var_nombre_usuario.set("Test")
    assert main_view.var_nombre_usuario.get() == "Test", "Error al get/set de variable"
    print("  ✓ Variables StringVar funcionan correctamente")
    
    root.destroy()
    return True


if __name__ == "__main__":
    print("\n" + "="*60)
    print("PRUEBAS DE INTEGRACIÓN - MAINVIEW CON USUARIOS")
    print("="*60)
    
    try:
        test_main_view_structure()
        test_variables_usuarios()
        
        print("\n" + "="*60)
        print("✅ TODAS LAS PRUEBAS DE INTEGRACIÓN PASARON")
        print("="*60 + "\n")
    except AssertionError as e:
        print(f"\n❌ ERROR: {e}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
