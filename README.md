<<<<<<< HEAD
# Restaurante App - Semana 11

**Estudiante:** Adriana Arias

**Asignatura:** Programación Orientada a Objetos  
**Semana:** 11

## 📋 Descripción General

Este proyecto es una evolución de la aplicación `restaurante_app` de la Semana 10. La aplicación implementa un sistema de gestión de restaurante que permite:

- **Gestión de productos** con atributo de stock
- **Gestión de usuarios** registrados
- **Operación de venta** que relaciona usuarios con productos
- **Persistencia JSON** de productos, usuarios y ventas

### Objetivo Principal

Comprender y aplicar los fundamentos de colecciones para representar relaciones entre objetos (Usuario ↔ Producto mediante Venta), controlar inventario y persistir datos mediante archivos JSON.

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json    # Productos con stock actualizado
│   ├── usuarios.json     # Usuarios registrados
│   └── ventas.json       # Relaciones Usuario-Producto-Cantidad
├── modelos/
│   ├── __init__.py
│   ├── producto.py       # Clase Producto con stock
│   ├── usuario.py        # Clase Usuario con persistencia
│   └── venta.py          # NUEVA: Clase Venta (relación)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py   # Maneja todas las persistencias
│   └── restaurante.py        # Lógica de negocio y ventas
├── main.py               # Interfaz de usuario
└── README.md
```

## 🔧 Componentes

### Modelos (modelos/)

#### `producto.py` - Clase Producto
Representa un producto del restaurante con atributos:
- `codigo`: str (identificador único)
- `nombre`: str
- `categoria`: str
- `precio`: float
- `stock`: int (cantidad disponible, **NUEVO en Semana 11**)

**Métodos principales:**
- `mostrar_informacion()`: Retorna string con toda la información incluido stock
- `vender(cantidad: int)`: Disminuye el stock y valida que no sea negativo
- `to_dict()`: Convierte a diccionario para JSON (incluye stock)
- `from_dict(data)`: Reconstruye objeto desde diccionario

#### `usuario.py` - Clase Usuario
Representa una persona registrada en el sistema con atributos:
- `identificacion`: str (único)
- `nombre`: str
- `correo`: str

**Métodos principales:**
- `mostrar_informacion()`: Retorna string formateado
- `to_dict()`: Convierte a diccionario
- `from_dict(data)`: Reconstruye objeto (**NUEVO en Semana 11**)

#### `venta.py` - Clase Venta ⭐ NUEVA
**Clase completamente nueva que representa una venta (relación Usuario-Producto).**

Atributos:
- `usuario_id`: str (identificación del usuario que compra)
- `producto_codigo`: str (código del producto vendido)
- `cantidad`: int (cantidad vendida)

**Métodos principales:**
- `mostrar_informacion()`: Retorna string con los detalles de la venta
- `to_dict()`: Convierte a diccionario para persistencia
- `from_dict(data)`: Reconstruye objeto desde diccionario

### Servicios (servicios/)

#### `archivo_servicio.py` - ArchivoServicio
Centraliza toda la persistencia JSON. **Ampliado en Semana 11** para manejar tres archivos:

**Inicialización:**
```python
archivo_servicio = ArchivoServicio(
    ruta_productos="datos/productos.json",
    ruta_usuarios="datos/usuarios.json",
    ruta_ventas="datos/ventas.json"
)
```

**Métodos principales:**
- `cargar_productos()` / `guardar_productos(lista_dicts)`
- `cargar_usuarios()` / `guardar_usuarios(lista_dicts)`
- `cargar_ventas()` / `guardar_ventas(lista_dicts)`

**Manejo de excepciones:**
- `FileNotFoundError`: Si archivo no existe, retorna lista vacía
- `json.JSONDecodeError`: Si JSON es inválido, imprime error y retorna lista vacía
- `PermissionError`: Si no hay permisos, lanza excepción

#### `restaurante.py` - Restaurante
Servicio que administra toda la lógica de negocio. **Ampliado en Semana 11** con operaciones de venta.

**Colecciones internas:**
- `_productos: List[Producto]`
- `_usuarios: List[Usuario]`
- `_ventas: List[Venta]` (**NUEVA**)

**Métodos principales:**
- Productos: `registrar_producto()`, `buscar_producto_por_codigo()`, `listar_productos()`, etc.
- Usuarios: `registrar_usuario()`, `buscar_usuario_por_id()`, `listar_usuarios()`
- **Ventas (NUEVOS):**
  - `vender_producto(codigo, id_usuario, cantidad)`: Realiza venta con validaciones
  - `obtener_ventas_usuario(id_usuario)`: Retorna ventas de un usuario específico
  - `listar_todas_ventas()`: Retorna todas las ventas
  - `obtener_ventas_como_lista()`: Para persistencia

### Main (main.py)
Interfaz de usuario por consola. Menú con opciones para:

**PRODUCTOS:**
1. Registrar producto (solicita stock inicial)
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos

**USUARIOS:**
6. Registrar usuario
7. Listar usuarios

**VENTAS:** ⭐ NUEVAS OPCIONES
8. Realizar venta
9. Consultar ventas de usuario
10. Listar todas las ventas

11. Salir

## 📊 Flujo de una Venta

```
Usuario selecciona "Realizar venta"
    ↓
Se solicita: ID usuario, código producto, cantidad
    ↓
main() valida que usuario y producto existan
    ↓
Se muestra stock disponible
    ↓
restaurante.vender_producto() valida:
  - Usuario existe ✓
  - Producto existe ✓
  - Cantidad > 0 ✓
  - Stock ≥ cantidad solicitada ✓
    ↓
Si todas las validaciones pasan:
  - Se crea objeto Venta
  - Se agrega a la colección _ventas
  - Se disminuye stock del producto (producto.vender())
  - Se guarda ventas.json (con la nueva venta)
  - Se guarda productos.json (con stock actualizado)
  - Se muestra confirmación
    ↓
Si falla alguna validación:
  - Se rechaza la operación
  - Se imprime mensaje de error
  - NO se modifica ningún dato
```

## 💾 Persistencia

### Archivos JSON

#### `productos.json`
Almacena productos con stock actualizado después de cada venta:
```json
[
  {
    "codigo": "BURGERS001",
    "nombre": "Hamburguesa Clásica",
    "categoria": "Plato Principal",
    "precio": 12.50,
    "stock": 15
  }
]
```

#### `usuarios.json`
Almacena usuarios registrados:
```json
[
  {
    "identificacion": "12345678",
    "nombre": "Juan Pérez",
    "correo": "juan@example.com"
  }
]
```

#### `ventas.json`
Almacena todas las ventas realizadas:
```json
[
  {
    "usuario_id": "12345678",
    "producto_codigo": "BURGERS001",
    "cantidad": 2
  }
]
```

### Cuándo se Guardan los Datos

| Operación | Archivos Guardados |
|-----------|------------------|
| Registrar producto | productos.json |
| Actualizar producto | productos.json |
| Eliminar producto | productos.json |
| Registrar usuario | usuarios.json |
| **Realizar venta** | **ventas.json + productos.json** |

### Recuperación al Iniciar

Cuando se ejecuta `main.py`:
1. Se crea instancia de `Restaurante` (vacía)
2. Se cargan productos desde `productos.json` y se reconstruyen objetos `Producto`
3. Se cargan usuarios desde `usuarios.json` y se reconstruyen objetos `Usuario`
4. Se cargan ventas desde `ventas.json` y se reconstruyen objetos `Venta`
5. Se inicia el menú con todos los datos previos disponibles

## ⚠️ Excepciones Controladas

### En Persistencia (ArchivoServicio)
- **FileNotFoundError**: Primer inicio, no hay archivos aún → devuelve lista vacía
- **json.JSONDecodeError**: Archivo corrupto → imprime advertencia, devuelve lista vacía
- **PermissionError**: Sin permisos de lectura/escritura → lanza excepción

### En Modelos
- **ValueError**: Datos inválidos en construcción
  - Código vacío → Error
  - Precio negativo → Error
  - Stock negativo → Error
  - Cantidad inválida en Venta → Error
- **KeyError**: Clave faltante en reconstrucción desde dict

### En Restaurante.vender_producto()
- Usuario no existe → Retorna False
- Producto no existe → Retorna False
- Cantidad ≤ 0 → Retorna False
- Stock insuficiente → Retorna False

## 🧪 Comprobación Mínima de Funcionamiento

### Caso 1: Venta Exitosa
1. ✓ Registrar usuario: `12345` | Juan | juan@test.com
2. ✓ Registrar producto: `BURGER1` | Hamburguesa | Plato Principal | $10.50 | Stock: 10
3. ✓ Realizar venta: Usuario `12345`, Producto `BURGER1`, Cantidad 3
4. ✓ Verificar stock disminuyó: Stock debe ser 7
5. ✓ Consultar ventas del usuario: Debe mostrar 1 venta
6. ✓ Revisar ventas.json: Debe contener la venta
7. ✓ Revisar productos.json: Debe mostrar stock=7

### Caso 2: Venta Rechazada (Stock Insuficiente)
1. ✓ Intentar venta: Usuario `12345`, Producto `BURGER1`, Cantidad 10 (stock actual: 7)
2. ✓ Sistema rechaza: "Error: cantidad inválida o stock insuficiente"
3. ✓ Verificar stock NO cambió: Stock sigue siendo 7
4. ✓ Verificar ventas.json NO se modificó

### Caso 3: Persistencia
1. ✓ Cerrar completamente el programa
2. ✓ Ejecutar nuevamente `main.py`
3. ✓ Verificar que todos los datos fueron recuperados:
   - Productos con stock actualizado
   - Usuarios registrados
   - Ventas históricas

## 🚀 Cómo Ejecutar

### Requisitos
- Python 3.9+
- No requiere dependencias externas (usa solo bibliotecas estándar)

### Ejecución
```bash
# Desde la carpeta restaurante_app/
cd restaurante_app
python main.py
```

O si está en el directorio padre:
```bash
python -m restaurante_app.main
```

## 📝 Notas de Implementación

### Stock en Producto
- El atributo `stock` tiene valor por defecto 0 si no se proporciona
- Método `vender(cantidad)` lanza `ValueError` si intenta vender más del stock disponible
- En `to_dict()` y `from_dict()` se incluye el stock para persistencia

### Validación en Venta
- La cantidad debe ser positiva (> 0)
- Se valida en el constructor de `Venta`
- Se valida nuevamente en `restaurante.vender_producto()`

### Flujo de Persistencia
- Los datos se guardan **después** de cada operación exitosa
- Si ocurre excepción durante guardado, se imprime pero la operación no se revierte
- Las colecciones en memoria siempre prevalecen; JSON es respaldo

### Uso de Colecciones
- Todas las colecciones son `List`, no diccionarios
- Los objetos se mantienen como instancias de clases (Producto, Usuario, Venta)
- La conversión a dict es solo para persistencia

## 🔄 Cambios Respecto a Semana 10

| Aspecto | Semana 10 | Semana 11 |
|--------|----------|----------|
| Stock en Producto | No | ✓ Sí |
| Persistencia Usuarios | No | ✓ Sí (usuarios.json) |
| Persistencia Ventas | No | ✓ Sí (ventas.json) |
| Clase Venta | No | ✓ NUEVA |
| Operación Vender | No | ✓ vender_producto() |
| Consulta de Ventas | No | ✓ obtener_ventas_usuario() |
| ArchivoServicio | 1 archivo | ✓ 3 archivos |
| Usuario.from_dict() | No | ✓ Sí |

## 👨‍💻 Responsabilidades

| Archivo | Responsabilidad |
|---------|-----------------|
| `producto.py` | Modelo con atributo stock y validaciones |
| `usuario.py` | Modelo con persistencia completa |
| `venta.py` | Modelo que representa relación Usuario-Producto |
| `archivo_servicio.py` | Persistencia de todas las colecciones |
| `restaurante.py` | Lógica de negocio y operaciones de venta |
| `main.py` | Interfaz de usuario e interacción |

---

**Fecha de entrega:** Semana 11  
**Formato:** Repositorio GitHub público  
**Contenido:** Proyecto completo + JSON + README.md
=======

# Asignatura — Programación Orientada a Objetos (POO) — Universidad Estatal Amazónica

Resumen
-------
Repositorio educativo que contiene prácticas y ejercicios de Programación Orientada a Objetos (POO) organizados por tareas. El objetivo es ofrecer ejemplos modulares y fáciles de entender para aprender a estructurar proyectos en Python usando paquetes y clases.

Autor
-----
- Adriana Verónica Arias

Descripción general
-------------------
Este proyecto muestra varias pequeñas aplicaciones y ejercicios que ilustran conceptos de POO en Python: definición de modelos (clases), separación en módulos, y servicios que operan sobre esos modelos. Es ideal como material didáctico y punto de partida para ampliaciones.

Principales funcionalidades (ejemplos)
- Modelos básicos para representar entidades (por ejemplo: cliente, producto, mascota).
- Servicios que encapsulan lógica de negocio (por ejemplo: operaciones relacionadas con un restaurante o gestión de pedidos).
- Scripts de ejemplo para ejecutar y probar los componentes.

Tecnologías
-----------
- Python 3.10+ (o versión compatible)

Estructura del repositorio
--------------------------
El repositorio está organizado por carpetas que contienen prácticas y tareas. A modo orientativo:

2626-POO-Arias-Adriana/
├── README.md
├── pyproject.toml
├── uv.lock
├── PARCIAL 2/
├── PARCIAL1/
│   ├── SEMANA 2/
│   ├── SEMANA 3/
│   └── SEMANA 4/
│       ├── main.py
│       ├── modelos/
│       │   ├── cliente.py
+       │   └── producto.py
       └── servicios/
           └── restaurante.py

Cómo ejecutar (instrucciones rápidas)
-----------------------------------
1. Crear un entorno virtual (recomendado):

   python -m venv .venv

2. Activar el entorno (Windows PowerShell):

   .\.venv\Scripts\Activate.ps1

3. Ejecutar un script de ejemplo (por ejemplo, el principal dentro de `PARCIAL1/SEMANA 4/` si desea probar el ejemplo del restaurante):

   python "PARCIAL1/SEMANA 4/main.py"

Notas
-----
- Algunos subdirectorios contienen ejercicios por semana; revise la estructura para encontrar el ejemplo que desea ejecutar.
- Este README ofrece información global del proyecto; los detalles específicos de cada práctica (por ejemplo, instrucciones o explicaciones) están dentro de sus respectivas carpetas.

Contacto
-------
Adriana Verónica Arias — Universidad Estatal Amazónica

>>>>>>> dd645dc17eb11c1017dab808d63bb5f00cd488b6
