# restaurante_app - Semana 12: Optimización de Colecciones

## Descripción General

Continuación del proyecto `restaurante_app` de la Semana 11 con mejoras en el rendimiento mediante la implementación de índices en memoria. Esta semana se enfoca en optimizar búsquedas, consultas y validaciones frecuentes sin modificar las funcionalidades principales.

## Mejoras Implementadas

### 1. Índice de Productos por Código
- **Estructura**: `Dict[str, Producto]` (`_productos_index`)
- **Mejora**: Búsqueda de productos por código de O(n) a O(1)
- **Operaciones mejoradas**:
  - `buscar_producto_por_codigo()` - ahora es acceso directo al diccionario
  - `registrar_producto()` - mantiene sincronizado el índice
  - `eliminar_producto()` - limpia la entrada del índice
- **Caso de uso**: Validar disponibilidad de un producto durante una venta

### 2. Índice de Usuarios por Identificación
- **Estructura**: `Dict[str, Usuario]` (`_usuarios_index`)
- **Mejora**: Búsqueda de usuarios por ID de O(n) a O(1)
- **Operaciones mejoradas**:
  - `buscar_usuario_por_id()` - ahora es acceso directo al diccionario
  - `registrar_usuario()` - mantiene sincronizado el índice e inicializa lista de ventas
- **Caso de uso**: Verificar identidad del usuario durante una transacción

### 3. Índice de Ventas por Usuario
- **Estructura**: `Dict[str, List[Venta]]` (`_ventas_por_usuario`)
- **Mejora**: Consulta de ventas de un usuario de O(n) a O(1) más pequeño conjunto
- **Operaciones mejoradas**:
  - `obtener_ventas_usuario()` - acceso O(1) a la lista de ventas del usuario
  - `vender_producto()` - añade la venta tanto a la lista principal como al índice
  - `cargar_ventas()` - reconstruye el índice tras cargar desde JSON
- **Caso de uso**: Generar historial de compras o análisis por usuario

## Arquitectura

### Colecciones Principales (Se conservan)
- `_productos: List[Producto]` - lista principal de productos
- `_usuarios: List[Usuario]` - lista principal de usuarios
- `_ventas: List[Venta]` - lista principal de ventas

### Índices Auxiliares (Nuevos)
- `_productos_index: Dict[str, Producto]` - búsqueda rápida por código
- `_usuarios_index: Dict[str, Usuario]` - búsqueda rápida por ID
- `_ventas_por_usuario: Dict[str, List[Venta]]` - búsqueda rápida de ventas por usuario

### Sincronización
- Los índices se actualizan automáticamente en operaciones de crear, modificar y eliminar
- Al cargar datos desde JSON, los índices se reconstruyen completamente
- Esto garantiza coherencia entre listas e índices

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Forma de Ejecución

### Requisitos
- Python 3.7+

### Instalación
```bash
# Clonar o descargar el repositorio
cd restaurante_app

# Ejecutar la aplicación
python main.py
```

### Funcionalidades Disponibles

1. **Registrar Producto**: Agregar productos con código, nombre, categoría, precio y stock
2. **Registrar Usuario**: Registrar usuarios con ID, nombre y correo
3. **Realizar Venta**: Vender productos a usuarios (valida stock automáticamente)
4. **Consultar Productos**: Listar todos los productos
5. **Consultar Usuarios**: Listar todos los usuarios
6. **Consultar Ventas**: Ver el historial de ventas general o por usuario
7. **Actualizar Producto**: Modificar detalles de un producto
8. **Eliminar Producto**: Remover un producto del sistema
9. **Persistencia**: Los datos se guardan automáticamente en archivos JSON

## Pruebas Principales Realizadas

### 1. Funcionalidades Base (Heredadas de Semana 11)
- ✅ Registro y listado de productos
- ✅ Registro y listado de usuarios
- ✅ Venta de productos con validación de stock
- ✅ Actualización y eliminación de productos
- ✅ Persistencia en JSON

### 2. Validación de Índices
- ✅ Búsqueda rápida de productos por código
- ✅ Búsqueda rápida de usuarios por ID
- ✅ Consulta rápida de ventas por usuario
- ✅ Sincronización de índices tras registrar nuevos objetos
- ✅ Limpieza de índices tras eliminar objetos

### 3. Recuperación y Reconstrucción
- ✅ Cierre y reapertura de la aplicación
- ✅ Datos cargados correctamente desde JSON
- ✅ Índices reconstruidos al iniciar
- ✅ Coherencia entre listas e índices verificada

## Justificación de Colecciones Elegidas

| Operación | Antes | Después | Colección |
|-----------|-------|---------|-----------|
| Buscar producto por código | O(n) | O(1) | `Dict[str, Producto]` |
| Buscar usuario por ID | O(n) | O(1) | `Dict[str, Usuario]` |
| Obtener ventas de un usuario | O(n) | O(1) + acceso a lista | `Dict[str, List[Venta]]` |
| Listar todos los productos | O(n) | O(n) | `List[Producto]` |
| Listar todas las ventas | O(n) | O(n) | `List[Venta]` |

Se NO utilizó `Set` porque:
- Los códigos de productos y IDs de usuarios ya son únicos por diseño
- No hay operaciones de validación de pertenencia frecuentes
- Los diccionarios ya proveen la funcionalidad necesaria

## Cambios Respecto a Semana 11

1. Adición de tres índices de tipo diccionario
2. Actualización de métodos de búsqueda para usar índices
3. Sincronización automática de índices en operaciones de crear/modificar/eliminar
4. Reconstrucción de índices al cargar datos desde JSON
5. Sin cambios en la API pública ni en las funcionalidades

## Notas Técnicas

- Los índices son internos al servicio Restaurante (privados, con prefijo `_`)
- La lógica de negocio permanece en el servicio, no en main
- Las listas principales se mantienen para iteración, persistencia y auditoría
- Los diccionarios se usan únicamente para acelerar búsquedas frecuentes

## Conclusiones

La implementación de índices en memoria proporciona mejoras significativas en rendimiento para operaciones críticas, especialmente en sistemas con muchos productos y usuarios. La solución mantiene la simplicidad de la arquitectura anterior mientras introduce optimizaciones pragmáticas basadas en las operaciones reales del sistema.
