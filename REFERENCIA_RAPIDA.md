# 🚀 Referencia Rápida - Restaurante App Semana 11

## Ejecución Rápida

```bash
cd restaurante_app
python main.py
```

## Menú Principal

```
1-5:  Gestión de Productos (registrar, buscar, actualizar, eliminar, listar)
6-7:  Gestión de Usuarios (registrar, listar)
8-10: Operaciones de VENTA (nueva, consultar, listar todas)
11:   Salir
```

## Flujo de Venta (Principal Funcionalidad Nueva)

```
Seleccione opción: 8
  → Ingresa ID usuario: 12345
  → Ingresa código producto: BURGER1
  → Ingresa cantidad: 3
  
Si válido → Venta registrada, stock disminuye
Si inválido → Rechazada (usuario/producto no existe o stock insuficiente)
```

## Archivos JSON (Después de Primera Ejecución)

- **productos.json**: Productos con stock actualizado
- **usuarios.json**: Usuarios registrados  
- **ventas.json**: Historial de todas las ventas

## Clases Principales

### Producto
```python
Producto(codigo, nombre, categoria, precio, stock=0)
├── vender(cantidad)      # Disminuye stock
├── to_dict()            # Para JSON
└── from_dict(data)      # Recuperar de JSON
```

### Usuario
```python
Usuario(identificacion, nombre, correo)
├── to_dict()            # Para JSON
└── from_dict(data)      # Recuperar de JSON [NUEVO]
```

### Venta [NUEVA]
```python
Venta(usuario_id, producto_codigo, cantidad)
├── to_dict()            # Para JSON
└── from_dict(data)      # Recuperar de JSON
```

### Restaurante
```python
Restaurante()
├── vender_producto(codigo, id_usuario, cantidad) -> bool [NUEVA]
├── obtener_ventas_usuario(id_usuario) -> List[str] [NUEVA]
├── listar_todas_ventas() -> List[str] [NUEVA]
└── Otros métodos...
```

### ArchivoServicio
```python
ArchivoServicio(ruta_productos, ruta_usuarios, ruta_ventas) [MEJORADO]
├── cargar_productos() / guardar_productos()
├── cargar_usuarios() / guardar_usuarios() [NUEVO]
└── cargar_ventas() / guardar_ventas() [NUEVO]
```

## Validaciones

| Operación | Validación | Acción |
|-----------|-----------|--------|
| Crear Producto | stock < 0 | ValueError |
| Vender | cantidad ≤ 0 | Rechazada |
| Vender | stock < cantidad | Rechazada |
| Vender | usuario no existe | Rechazada |
| Vender | producto no existe | Rechazada |
| Cargar JSON | archivo no existe | Lista vacía |
| Cargar JSON | JSON inválido | Advertencia + lista vacía |

## Pruebas

```bash
python test_run.py
# Output: 8/8 pruebas pasaron ✓
```

## GitHub

```bash
git init
git add .
git commit -m "Restaurante App Semana 11: Ventas, Stock y Persistencia"
git remote add origin https://github.com/USUARIO/REPO.git
git push -u origin main
```

## Requisitos

- Python 3.9+
- Sin dependencias externas

## Documentación Completa

Ver **README.md** para:
- Descripción detallada
- Estructura completa
- Explicación de cada componente
- Flujo de venta detallado
- Manejo de excepciones
- Casos de prueba

## Archivos Principales

| Archivo | Líneas | Función |
|---------|--------|---------|
| main.py | ~350 | Interfaz usuario |
| restaurante.py | ~180 | Lógica negocio |
| archivo_servicio.py | ~80 | Persistencia JSON |
| producto.py | ~80 | Modelo con stock |
| usuario.py | ~30 | Modelo usuario |
| venta.py | ~50 | Modelo venta [NUEVO] |
| README.md | ~400 | Documentación |

## Ejemplo Rápido

```
Ejecuta main.py
├─ Registra producto: BURGER1, stock=20
├─ Registra usuario: 12345
├─ Realiza venta: usuario=12345, producto=BURGER1, cantidad=3
├─ Consulta ventas del usuario
└─ Cierra el programa

Al reiniciar:
└─ Todos los datos se recuperan desde JSON ✓
   (stock=17, venta registrada, usuario existe)
```

---

**¿Preguntas?** Consulta README.md o EJEMPLO_EJECUCION.md
