# Restaurante App - Semana 14: Componentes y Contenedores

## Descripción General

La presente actividad corresponde a la **Semana 14** de Programación Orientada a Objetos y aborda el tema **Componentes y Contenedores en Tkinter**. 

Este proyecto evoluciona la versión de Semana 13, mejorando significativamente la capa de interfaz gráfica mediante el uso adecuado de:
- **Componentes de Tkinter**: Entry, Text, Button, Label, Listbox
- **Componentes ttk**: Notebook (tabs), Frame, LabelFrame, Treeview, Scrollbar
- **Gestores de Geometría**: Grid y Pack para organizar componentes
- **Contenedores**: LabelFrame para agrupar lógicamente elementos relacionados

La interfaz utiliza un **diseño de Doble Panel** que proporciona una mejor experiencia de usuario y flujo más intuitivo.

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json          # Persistencia de productos
│   └── usuarios.json           # Datos de usuarios
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Clase Producto
│   └── usuario.py              # Clase Usuario
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Lectura/escritura JSON
│   └── restaurante_servicio.py # Lógica de negocio CRUD
├── ui/
│   ├── __init__.py
│   ├── login_view.py           # Interfaz de autenticación
│   └── main_view.py            # Interfaz principal (Doble Panel)
├── main.py                     # Punto de entrada
└── README.md                   # Documentación
```

## Mejoras Implementadas en Semana 14

### 1. Diseño Doble Panel (Principal)

#### Estructura Visual
La interfaz de productos ahora se organiza en **dos paneles** para máxima claridad:

```
┌──────────────────┐  ┌──────────────────────────────────┐
│  PANEL IZQUIERDO │  │   PANEL DERECHO (Formulario)    │
│   Lista de Prod. │  │   Detalles y CRUD               │
├──────────────────┤  ├──────────────────────────────────┤
│ + Nuevo Prod.    │  │ ID:          [Deshabilitado]    │
│                  │  │ Nombre:      [Entry]            │
│ P001 - Hamb...   │  │ Precio:      [Entry]            │
│ P002 - Pizza...  │  │ Cantidad:    [Entry]            │
│ P003 - Pasta...  │  │ Descripción: [Text multilinea]  │
│ P004 - Ensala... │  │                                 │
│ P005 - Papas...  │  │ ────────────────────────────    │
│ P006 - Refres... │  │ [Guardar | Actualizar | Elim]  │
│                  │  │ [  Limpiar Formulario  ]        │
│ (Scrollbar)      │  │                                 │
└──────────────────┘  └──────────────────────────────────┘
```

#### Panel Izquierdo: Lista de Productos
- **Componente**: `Listbox` con `Scrollbar`
- **Contenido**: Listado de productos con formato "ID - Nombre ($Precio)"
- **Interacción**: 
  - Clic en un producto → carga datos en el formulario
  - Botón "+ Nuevo Producto" → limpia formulario para crear nuevo

#### Panel Derecho: Formulario CRUD
- **Componentes**:
  - `Entry` para: ID (deshabilitado), Nombre, Precio, Cantidad
  - `Text` para: Descripción (multilinea)
  - `Button` para acciones: Guardar, Actualizar, Eliminar, Limpiar
- **Contenedor**: `LabelFrame` "Detalles del Producto"
- **Comportamiento**:
  - Se actualiza automáticamente al seleccionar un producto
  - Botones adaptan su función según el contexto
  - Validaciones mantienen la integridad de datos

### 2. Flujo de Usuario Mejorado

**Antes (Secuencial)**:
1. Llenar formulario → Ver tabla abajo → Necesita scroll

**Ahora (Contextual)**:
1. Ver lista de productos → Seleccionar → Editar en formulario → Todo visible

### 3. Métodos Optimizados

| Método | Propósito |
|--------|-----------|
| `_nuevo_producto()` | Prepara para crear nuevo producto |
| `_on_select_producto(event)` | Carga producto al seleccionar |
| `_cargar_producto_en_formulario(p)` | Rellena campos del formulario |
| `_guardar_producto()` | Registra nuevo producto |
| `_actualizar_producto()` | Modifica producto existente |
| `_eliminar_producto()` | Borra producto (con confirmación) |
| `_actualizar_listbox_productos()` | Recarga lista automáticamente |
| `_limpiar_formulario()` | Vacía todos los campos |

### 4. Componentes y Contenedores Utilizados

**Componentes tk**:
- `Frame` - Contenedor genérico
- `Label` - Texto estático y etiquetas
- `Entry` - Campos de texto
- `Text` - Área multilinea (descripción)
- `Button` - Botones de acción (Guardar, Actualizar, Eliminar, Limpiar)
- `Listbox` - Lista de productos

**Componentes ttk**:
- `Notebook` - Navegación de tabs
- `Frame` - Contenedor de tab
- `LabelFrame` - Agrupar formulario y lista
- `Scrollbar` - Navegación en Listbox
- `Separator` - Línea divisoria visual

### 5. Persistencia en JSON

- `ArchivoServicio.guardar_productos()` actualiza `productos.json`
- Los cambios se persisten automáticamente tras cada operación CRUD
- Los datos se recargan correctamente en nuevas ejecuciones

## Tab de Usuarios (CRUD Completo)

A partir de la Semana 14, el tab de usuarios implementa un **Diseño Doble Panel** idéntico al de Productos:

### Estructura Visual
```
┌──────────────────┐  ┌──────────────────────────────────┐
│  PANEL IZQUIERDO │  │   PANEL DERECHO (Formulario)    │
│  Lista Usuarios  │  │   Detalles y CRUD               │
├──────────────────┤  ├──────────────────────────────────┤
│ + Nuevo Usuario  │  │ ID:         [Deshabilitado]     │
│                  │  │ Nombre:     [Entry]             │
│ Juan (juan) - ... │  │ Usuario:    [Entry]             │
│ María (maria) -...│  │ Contraseña: [Entry con ****]   │
│ Carlos (car..) ..│  │ Rol:        [Combobox]          │
│ Ana (ana) - ...  │  │             admin/gerente/...   │
│ Pedro (pedro)... │  │ ────────────────────────────    │
│                  │  │ [Guardar | Actualizar | Elim]  │
│ (Scrollbar)      │  │ [  Limpiar Formulario  ]        │
└──────────────────┘  └──────────────────────────────────┘
```

### Operaciones CRUD Disponibles
1. **Crear Usuario** - Botón "+ Nuevo Usuario" → Completar formulario → Guardar
2. **Consultar Usuario** - Seleccionar en lista → Se carga en el formulario
3. **Actualizar Usuario** - Modificar datos → Botón "Actualizar"
4. **Eliminar Usuario** - Seleccionar → Botón "Eliminar" → Confirmar
5. **Limpiar Formulario** - Vaciar campos y deseleccionar de lista

## Tab de Ventas

- Placeholder para funcionalidad futura

## Operaciones Disponibles

### Productos

#### Registrar Producto
1. Clic en "+ Nuevo Producto"
2. Llenar formulario con datos
3. Clic en "Guardar"
4. Sistema genera ID automático (P001, P002, etc.)
5. Producto aparece en la lista

#### Modificar Producto
1. Clic en producto en la lista (panel izquierdo)
2. Datos se cargan en el formulario (panel derecho)
3. Modificar campos deseados
4. Clic en "Actualizar"
5. Cambios se reflejan en la lista

#### Eliminar Producto
1. Clic en producto en la lista
2. Clic en "Eliminar"
3. Confirmar en ventana de diálogo
4. Producto se elimina de la lista

#### Limpiar Formulario de Productos
1. Clic en "Limpiar Formulario"
2. Se vacían todos los campos
3. Se deselecciona el producto

### Usuarios (Nuevas Operaciones - Semana 14)

#### Registrar Usuario
1. Clic en "+ Nuevo Usuario"
2. Llenar formulario: Nombre, Usuario, Contraseña, Rol
3. Seleccionar rol del combobox (administrador, gerente, cajero, chef, mesero, cliente)
4. Clic en "Guardar"
5. Sistema genera ID automático (U006, U007, etc.)
6. Usuario aparece en la lista

#### Modificar Usuario
1. Clic en usuario en la lista (panel izquierdo)
2. Datos se cargan en el formulario (panel derecho)
3. Modificar campos deseados
4. Clic en "Actualizar"
5. Cambios se reflejan en la lista y en usuarios.json

#### Eliminar Usuario
1. Clic en usuario en la lista
2. Clic en "Eliminar"
3. Confirmar en ventana de diálogo
4. Usuario se elimina de la lista y usuarios.json

#### Limpiar Formulario de Usuarios
1. Clic en "Limpiar"
2. Se vacían todos los campos
3. Se deselecciona el usuario

## Validaciones

**Datos de Entrada - Productos:**
- Nombre no vacío
- Precio válido (número positivo)
- Cantidad válida (entero positivo)
- Descripción opcional

**Datos de Entrada - Usuarios:**
- Nombre no vacío
- Usuario no vacío y único (no puede duplicarse)
- Contraseña no vacía
- Rol válido (seleccionado de la lista)

**Confirmaciones:**
- Mensaje de éxito al registrar/actualizar
- Confirmación requerida para eliminar
- Mensajes de error específicos

**Validaciones Generales:**
- Campos vacíos detectados
- Tipos de datos correctos verificados
- Valores negros prevenidos
- Duplicados evitados (usuario)
- Formato de IDs únicos garantizado

## Requisitos para Ejecutar

- Python 3.6 o superior
- Tkinter (incluido con Python en Windows y macOS)
- Módulos estándar: `json`, `os`, `sys`

## Instrucciones de Ejecución

```bash
# En la carpeta del proyecto
cd restaurante_app

# Ejecutar la aplicación
python main.py
```

### Credenciales de Prueba
```
Usuario: juan
Contraseña: 123456
(Otros usuarios: maria, carlos, ana, pedro con la misma contraseña)
```

## Separación de Responsabilidades

**MainView (ui/main_view.py)**
- Coordina interacción del usuario
- Muestra y actualiza interfaz
- Llama métodos en `RestauranteServicio`
- Presenta mensajes de error

**RestauranteServicio (servicios/restaurante_servicio.py)**
- Valida datos de entrada
- Ejecuta lógica CRUD
- Coordina con `ArchivoServicio`
- Retorna resultados con mensajes

**ArchivoServicio (servicios/archivo_servicio.py)**
- Lectura de JSON
- Escritura de JSON
- Conversión Producto ↔ diccionario

**Modelos (modelos/)**
- Definición de estructura de datos
- Métodos de representación

## Persistencia de Datos

- **Archivo**: `datos/productos.json`
- **Formato**: Array de objetos JSON con campos: id, nombre, precio, cantidad, descripcion
- **Actualización**: Automática tras cada operación CRUD
- **Verificación**: Los datos persisten entre ejecuciones

Ejemplo de estructura en `productos.json`:
```json
[
  {
    "id": "P001",
    "nombre": "Hamburguesa Clásica",
    "precio": 8.99,
    "cantidad": 50,
    "descripcion": "Hamburguesa con carne de res, lechuga y tomate"
  }
]
```

## Comprobación de Funcionamiento

✅ Ejecutar `main.py` sin errores  
✅ Login con usuario válido funciona  
✅ MainView se muestra correctamente  
✅ **Tab Productos**: Panel izquierdo con lista + Panel derecho con formulario  
✅ **Tab Usuarios**: Panel izquierdo con lista + Panel derecho con formulario CRUD  
✅ Seleccionar producto en lista carga datos en formulario  
✅ Seleccionar usuario en lista carga datos en formulario  
✅ Crear nuevo producto funciona y persiste en `productos.json`  
✅ Crear nuevo usuario funciona y persiste en `usuarios.json`  
✅ Modificar producto funciona y persiste  
✅ Modificar usuario funciona y persiste  
✅ Eliminar producto funciona y persiste  
✅ Eliminar usuario funciona y persiste  
✅ Cambios persisten al cerrar y reapertura de la app  
✅ Interfaz clara con componentes bien organizados  
✅ Validaciones funcionan correctamente  
✅ Mensajes de error son informativos

## Características Destacadas

✅ **Diseño Doble Panel** - Mejor organización visual para Productos Y Usuarios  
✅ **Flujo Intuitivo** - Ver → Seleccionar → Editar  
✅ **CRUD Completo en Productos** - Registrar, Consultar, Actualizar, Eliminar  
✅ **CRUD Completo en Usuarios** - Registrar, Consultar, Actualizar, Eliminar (NUEVO)  
✅ **Componentes Profesionales** - Listbox, Entry, Text, Button, Combobox, Label  
✅ **Validaciones Robustas** - En RestauranteServicio, no en UI  
✅ **Actualización Automática** - Listas se recargan tras CRUD  
✅ **Persistencia Completa** - JSON siempre actualizado (productos.json y usuarios.json)  
✅ **Interfaz Responsiva** - Se adapta al tamaño de ventana  
✅ **Separación de Responsabilidades** - UI, Servicios, Modelos, Datos bien diferenciados

## Mejoras Futuras

- Búsqueda y filtrado de productos
- Ordenamiento de columnas
- Edición in-line en tabla
- Exportación a CSV
- Historial de cambios
- Estadísticas de inventario

## Autor
Estudiante de Programación Orientada a Objetos  
Semana 14: Componentes y Contenedores (Con CRUD de Usuarios)  
Año 2026

---

**Versión**: Semana 14 v2.1 (Doble Panel + CRUD Usuarios)  
**Última actualización**: 2026-09-15  
**Estado**: ✅ COMPLETADO (Productos + Usuarios CRUD Funcional)

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json          # Persistencia de productos
│   └── usuarios.json           # Datos de usuarios
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Clase Producto
│   └── usuario.py              # Clase Usuario
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Lectura/escritura JSON
│   └── restaurante_servicio.py # Lógica de negocio CRUD
├── ui/
│   ├── __init__.py
│   ├── login_view.py           # Interfaz de autenticación
│   └── main_view.py            # Interfaz principal con CRUD
├── main.py                     # Punto de entrada
└── README.md                   # Documentación
```

## Mejoras Implementadas en Semana 14

### 1. Componentes y Contenedores Mejorados

#### Tab de Productos
La interfaz de productos ahora está organizada en **tres secciones claras** usando `LabelFrame`:

**Sección 1: Formulario de Productos**
- Campos: ID (deshabilitado), Nombre, Precio, Cantidad, Descripción
- Uso de `tk.Entry` para campos numéricos y texto
- `tk.Text` para descripción multilinea
- Organización con gestor de geometría `grid()`

**Sección 2: Acciones CRUD**
- Botones con colores semanticos:
  - **Registrar** (verde): Crear nuevo producto
  - **Cargar por ID** (azul): Buscar y llenar formulario
  - **Actualizar** (naranja): Guardar cambios
  - **Eliminar** (rojo): Borrar producto
  - **Limpiar** (gris): Vaciar formulario
- Cada botón ejecuta métodos en `RestauranteServicio`

**Sección 3: Visualización con Treeview**
- Tabla profesional mostrando: ID, Nombre, Precio, Cantidad, Descripción
- Scrollbar vertical para navegación
- Actualización automática tras operaciones

#### Tab de Usuarios
- Visualización de usuarios registrados en el sistema
- Mantiene funcionalidad de Semana 13

### 2. Métodos CRUD en RestauranteServicio

El servicio ahora proporciona operaciones completas sobre productos:

```python
# Registrar nuevo producto
exito, producto = restaurante_servicio.registrar_producto(
    nombre, precio, cantidad, descripcion
)

# Cargar producto por ID
exito, producto = restaurante_servicio.cargar_producto_por_id(producto_id)

# Actualizar producto
exito, producto = restaurante_servicio.actualizar_producto(
    producto_id, nombre, precio, cantidad, descripcion
)

# Eliminar producto
exito, mensaje = restaurante_servicio.eliminar_producto(producto_id)

# Recargar desde archivo
restaurante_servicio.recargar_productos()
```

### 3. Persistencia en JSON

- `ArchivoServicio.guardar_productos()` permite escribir cambios en `productos.json`
- Los cambios se persisten automáticamente después de cada operación CRUD
- Los datos se recargan correctamente en nuevas ejecuciones

### 4. Validaciones

Todas las validaciones se ejecutan en `RestauranteServicio`:
- Campos vacíos
- Tipos de datos correctos (precio como float, cantidad como int)
- Valores no negativos
- Formato de IDs únicos

## Flujo Funcional

```
┌─────────────────────────────────┐
│    Inicio de la Aplicación      │
└────────────┬────────────────────┘
             ↓
┌─────────────────────────────────┐
│    LoginView (Autenticación)    │
│ Usuario: juan, Contraseña: ...  │
└────────────┬────────────────────┘
             ↓
┌─────────────────────────────────┐
│    MainView (Interfaz Principal)│
└────────────┬────────────────────┘
             ↓
    ┌────────┴────────┬─────────────┐
    ↓                 ↓             ↓
┌─────────┐    ┌──────────┐   ┌──────────┐
│Productos│    │ Usuarios │   │ Ventas   │
│         │    │          │   │(Pendiente)
│ Formulario   │ Listado  │   │
│ Botones      │ usuarios │   │
│ Treeview     │          │   │
└─────────┘    └──────────┘   └──────────┘

┌─────────────────────────────────┐
│  Operaciones sobre Productos:   │
│ Registrar → Cargar → Actualizar │
│         → Eliminar → Limpiar    │
│                                 │
│ Cada operación:                 │
│ 1. Solicita a RestauranteServicio
│ 2. Valida datos                 │
│ 3. Persiste en productos.json   │
│ 4. Actualiza interfaz           │
└─────────────────────────────────┘
```

## Componentes y Contenedores Utilizados

### Componentes de Tkinter
| Componente | Uso | Ubicación |
|-----------|-----|-----------|
| `tk.Label` | Encabezados y etiquetas | Header, Formulario |
| `tk.Entry` | Campos de texto | Formulario (ID, Nombre, Precio, Cantidad) |
| `tk.Text` | Área multilinea | Formulario Descripción |
| `tk.Button` | Acciones | Botones CRUD |
| `tk.Frame` | Divisiones | Contenedor general |
| `tk.Listbox` | Lista de usuarios | Tab Usuarios |

### Componentes ttk
| Componente | Uso | Ubicación |
|-----------|-----|-----------|
| `ttk.Notebook` | Navegación tabs | MainView principal |
| `ttk.Frame` | Contenedor de tab | Cada tab |
| `ttk.LabelFrame` | Agrupar secciones | Formulario, Acciones, Tabla |
| `ttk.Treeview` | Tabla de datos | Tabla de productos |
| `ttk.Scrollbar` | Navegación | Treeview, Usuarios |

### Gestores de Geometría
- **Pack**: Encabezado, Tab Usuarios, Tabs principales
- **Grid**: Formulario de productos (organización 2 columnas)
- **Grid + Pack combinado**: Tab Productos para estructuración compleja

## Operaciones Disponibles

### Registrar Producto
1. Completar formulario con datos del nuevo producto
2. Hacer clic en **Registrar**
3. Sistema genera ID automático (P001, P002, etc.)
4. Se guarda en productos.json
5. Se actualiza la tabla automáticamente

### Cargar Producto
1. Escribir ID en el campo ID del formulario
2. Hacer clic en **Cargar por ID**
3. Se completan todos los campos con datos del producto
4. Permite consultar y modificar información

### Actualizar Producto
1. Cargar un producto (ver operación anterior)
2. Modificar los datos en el formulario
3. Hacer clic en **Actualizar**
4. Los cambios se guardan en productos.json
5. Se actualiza la tabla automáticamente

### Eliminar Producto
1. Cargar un producto (ver Cargar Producto)
2. Hacer clic en **Eliminar**
3. Se solicita confirmación
4. Se elimina de productos.json
5. Se actualiza la tabla automáticamente

### Limpiar Formulario
1. Hacer clic en **Limpiar**
2. Se vacían todos los campos
3. El foco se posiciona en el campo Nombre

## Validaciones Implementadas

**Datos de Entrada:**
- Nombre no vacío
- Precio válido (número positivo)
- Cantidad válida (entero positivo)
- Descripción opcional

**Errores Manejados:**
- Campo vacío solicitado
- Tipo de dato incorrecto
- Valor negativo donde no es permitido
- Producto no encontrado
- Errores de acceso a archivos

**Confirmaciones:**
- Mensaje de éxito al registrar/actualizar
- Confirmación antes de eliminar
- Mensajes de error específicos

## Requisitos para Ejecutar

- Python 3.6 o superior
- Tkinter (incluido con Python en Windows y macOS)
- Módulos estándar: `json`, `os`, `sys`

## Instrucciones de Ejecución

```bash
# En la carpeta del proyecto
cd restaurante_app

# Ejecutar la aplicación
python main.py
```

### Credenciales de Prueba
```
Usuario: juan
Contraseña: 123456
(Otros usuarios: maria, carlos, ana, pedro con la misma contraseña)
```

## Separación de Responsabilidades

**MainView (ui/main_view.py)**
- Coordinar interacción del usuario
- Mostrar y actualizar interfaz
- Llamar métodos en `RestauranteServicio`
- Presentar mensajes de error

**RestauranteServicio (servicios/restaurante_servicio.py)**
- Validar datos de entrada
- Ejecutar lógica CRUD
- Coordinar con `ArchivoServicio`
- Retornar resultados con mensajes

**ArchivoServicio (servicios/archivo_servicio.py)**
- Lectura de JSON
- Escritura de JSON
- Conversión Producto ↔ diccionario

**Modelos (modelos/)**
- Definición de estructura de datos
- Métodos de representación

## Persistencia de Datos

- **Archivo**: `datos/productos.json`
- **Formato**: Array de objetos JSON con campos: id, nombre, precio, cantidad, descripcion
- **Actualización**: Automática tras cada operación CRUD
- **Verificación**: Los datos persisten entre ejecuciones

Ejemplo de estructura en `productos.json`:
```json
[
  {
    "id": "P001",
    "nombre": "Hamburguesa Clásica",
    "precio": 8.99,
    "cantidad": 50,
    "descripcion": "Hamburguesa con carne de res, lechuga y tomate"
  },
  {
    "id": "P002",
    "nombre": "Pizza Margarita",
    "precio": 12.50,
    "cantidad": 30,
    "descripcion": "Pizza con queso mozzarella y tomate"
  }
]
```

## Comprobación de Funcionamiento

✅ Ejecutar `main.py` sin errores  
✅ Login con usuario válido funciona  
✅ MainView se muestra correctamente  
✅ Tab Usuarios muestra lista de usuarios  
✅ Tab Productos muestra formulario + tabla  
✅ Registrar nuevo producto funciona y persiste  
✅ Cargar producto por ID funciona  
✅ Actualizar producto funciona y persiste  
✅ Eliminar producto funciona y persiste  
✅ Cambios persisten al cerrar y reapertar la app  
✅ Interfaz clara y componentes bien organizados  

## Notas y Consideraciones

1. **Gestión de geometría**: Se utiliza principalmente `grid()` en formularios y `pack()` en secciones principales para máxima flexibilidad
2. **Colores semanticos**: Los botones utilizan colores que indican su función (verde=crear, rojo=eliminar, etc.)
3. **Validación en servicios**: Toda validación está centralizada en `RestauranteServicio`, no en la UI
4. **Actualización automática**: La tabla y mensajes se actualizan después de cada operación
5. **Interfaz responsiva**: Componentes se adaptan al tamaño de la ventana

## Mejoras Futuras

- Búsqueda y filtrado de productos
- Ordenamiento de columnas en Treeview
- Edición directa en tabla
- Exportación a CSV/Excel
- Historial de cambios
- Estadísticas de inventario

## Autor
Estudiante de Programación Orientada a Objetos  
Semana 14: Componentes y Contenedores  
Año 2026
