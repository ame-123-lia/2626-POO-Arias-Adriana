# Arquitectura de Componentes y Contenedores - Semana 14

## Diagrama Jerárquico de Componentes

```
RestauranteApp (root)
│
├── LoginView
│   └── frame (tk.Frame)
│       ├── titulo (tk.Label)
│       ├── subtitulo (tk.Label)
│       ├── form_frame (tk.Frame)
│       │   ├── label_usuario (tk.Label)
│       │   ├── entry_usuario (tk.Entry)
│       │   ├── label_contraseña (tk.Label)
│       │   ├── entry_contraseña (tk.Entry - show="*")
│       │   └── btn_ingresar (tk.Button)
│       └── label_mensaje (tk.Label)
│
└── MainView
    └── frame (tk.Frame)
        ├── header_frame (tk.Frame - bg="#2c3e50")
        │   ├── titulo (tk.Label - usuario actual)
        │   └── btn_logout (tk.Button)
        │
        └── notebook (ttk.Notebook) ← CONTENEDOR DE TABS
            ├── tab_productos (ttk.Frame)
            │   │
            │   └── container (tk.Frame)
            │       │
            │       ├── form_frame (ttk.LabelFrame "Formulario de Productos")
            │       │   ├── label_id (tk.Label)
            │       │   ├── entry_id (tk.Entry - DISABLED)
            │       │   ├── label_nombre (tk.Label)
            │       │   ├── entry_nombre (tk.Entry)
            │       │   ├── label_precio (tk.Label)
            │       │   ├── entry_precio (tk.Entry)
            │       │   ├── label_cantidad (tk.Label)
            │       │   ├── entry_cantidad (tk.Entry)
            │       │   ├── label_descripcion (tk.Label)
            │       │   └── text_descripcion (tk.Text - 3 lineas)
            │       │
            │       ├── btn_frame (ttk.LabelFrame "Acciones")
            │       │   ├── btn_registrar (tk.Button - verde)
            │       │   ├── btn_cargar (tk.Button - azul)
            │       │   ├── btn_actualizar (tk.Button - naranja)
            │       │   ├── btn_eliminar (tk.Button - rojo)
            │       │   └── btn_limpiar (tk.Button - gris)
            │       │
            │       └── tabla_frame (ttk.LabelFrame "Productos Registrados")
            │           ├── tree (ttk.Treeview)
            │           │   ├── Columna: ID
            │           │   ├── Columna: Nombre
            │           │   ├── Columna: Precio
            │           │   ├── Columna: Cantidad
            │           │   └── Columna: Descripción
            │           └── scrollbar (ttk.Scrollbar)
            │
            ├── tab_usuarios (ttk.Frame)
            │   ├── titulo (tk.Label)
            │   ├── frame_tabla (tk.Frame)
            │   ├── scrollbar (ttk.Scrollbar)
            │   └── listbox_usuarios (tk.Listbox)
            │
            └── tab_ventas (ttk.Frame)
                ├── mensaje (tk.Label)
                └── pendiente (tk.Label)
```

## Matriz de Componentes

### Componentes de Tkinter (tk.*)

| Componente | Uso | Ubicación | Propiedades |
|-----------|-----|-----------|------------|
| `tk.Frame` | Contenedor genérico | Header, Container, Tab Usuarios | bg="#2c3e50", fill=BOTH, expand=True |
| `tk.Label` | Texto estático | Títulos, etiquetas | font, fg, bg, text |
| `tk.Entry` | Campo de texto | Formulario productos | width, font, state=DISABLED (ID) |
| `tk.Text` | Área multilinea | Descripción | font, width=25, height=3 |
| `tk.Button` | Acción interactiva | Botones CRUD | command=, bg (colores), fg=white |
| `tk.Listbox` | Lista de elementos | Usuarios | font, yscrollcommand |

### Componentes ttk (ttk.*)

| Componente | Uso | Ubicación | Propiedades |
|-----------|-----|-----------|------------|
| `ttk.Notebook` | Contenedor de tabs | MainView principal | fill=BOTH, expand=True |
| `ttk.Frame` | Contenedor con tema | Cada tab | - |
| `ttk.LabelFrame` | Contenedor etiquetado | Formulario, Acciones, Tabla | text="Título", padding=10 |
| `ttk.Treeview` | Tabla de datos | Productos | columns, height=12 |
| `ttk.Scrollbar` | Barra de desplazamiento | Treeview, Usuarios | orient, command= |

## Gestores de Geometría

### Pack (Packing Geometry Manager)

**Ubicaciones:**
- Header frame (fill=X)
- Tab principal (fill=BOTH, expand=True)
- Secciones contenedoras (fill=X o fill=BOTH, expand=True)
- Elementos dentro de secciones (side, fill)

**Ventajas utilizadas:**
- Simplicidad en disposición vertical
- Fácil control de expansión
- Buen para layouts simples

### Grid (Grid Geometry Manager)

**Ubicaciones:**
- Formulario de productos (2 columnas)
- Botones de acciones (5 columnas x 1 fila)

**Ventajas utilizadas:**
- Alineación perfecta de campos
- Control preciso de espacios
- Ideal para formularios

**Ejemplo del formulario:**
```
Fila 0: [Etiqueta ID]    [Entry ID]
Fila 1: [Etiqueta Nombre] [Entry Nombre]
Fila 2: [Etiqueta Precio] [Entry Precio]
Fila 3: [Etiqueta Cantidad] [Entry Cantidad]
Fila 4: [Etiqueta Descripción] [Text Descripción]
```

## Colores Semánticos

### Paleta de Colores

| Color | Código | Uso |
|-------|--------|-----|
| Azul Oscuro | #2c3e50 | Header background |
| Verde | #27ae60 | Botón "Registrar" (crear) |
| Azul | #3498db | Botón "Cargar" (leer) |
| Naranja | #f39c12 | Botón "Actualizar" (modificar) |
| Rojo | #e74c3c | Botón "Eliminar" (borrar) |
| Gris | #95a5a6 | Botón "Limpiar" (resetear) |
| Rojo Oscuro | #c0392b | Botón "Cerrar Sesión" |
| Blanco | white | Texto en botones |
| Gris Claro | #7f8c8d | Subtítulos |

### Organización Visual

```
┌──────────────────────────────────────────────────────┐
│ [#2c3e50]  Bienvenido, Usuario    [#c0392b] Cerrar   │  Header
└──────────────────────────────────────────────────────┘
│ PRODUCTOS │ USUARIOS │ VENTAS                          Tabs (ttk.Notebook)
├──────────────────────────────────────────────────────┤
│ ┌─── Formulario de Productos ───────────────────────┐ │
│ │ ID:          [Deshabilitado]                      │ │
│ │ Nombre:      [Entry                              ] │ │ LabelFrame
│ │ Precio:      [Entry                              ] │ │ Formulario
│ │ Cantidad:    [Entry                              ] │ │
│ │ Descripción: [Text                               ] │ │
│ └───────────────────────────────────────────────────┘ │
│ ┌─── Acciones ──────────────────────────────────────┐ │
│ │ [#27ae60 Registrar] [#3498db Cargar] [#f39c12 Act] │ │ LabelFrame
│ │ [#e74c3c Eliminar] [#95a5a6 Limpiar]             │ │ Botones
│ └───────────────────────────────────────────────────┘ │
│ ┌─── Productos Registrados ─────────────────────────┐ │
│ │ ID    Nombre         Precio  Cant  Descripción   │ │
│ │ P001  Hamburguesa    $8.99   50    Hamburguesa..│ │
│ │ P002  Pizza Marg     $12.50  30    Pizza con..  │ │
│ │ P003  Pasta Alfredo  $10.99  25    Pasta con..  │ │
│ │ ─ (scrollbar vertical) ───────────────────────── │ │ LabelFrame
│ │ (Treeview + Scrollbar)                          │ │
│ └───────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

## Propiedades de Expansión y Relleno

### Formulario (LabelFrame)
- `fill=tk.X` - Se expande horizontalmente
- `pady=(0, 10)` - Espacio debajo para separar de la siguiente sección

### Botones (LabelFrame)
- `fill=tk.X` - Se expande horizontalmente
- `pady=(0, 10)` - Espacio debajo

### Tabla (LabelFrame)
- `fill=tk.BOTH` - Se expande en ambas direcciones
- `expand=True` - Toma espacio adicional disponible
- Treeview ocupa todo el espacio disponible

### Treeview
- `side=tk.LEFT, fill=tk.BOTH, expand=True` - Occupa espacio principal
- Scrollbar `side=tk.RIGHT, fill=tk.Y` - Alineada a la derecha

## Variables y Validaciones

### Variables de Control (StringVar)

```python
self.var_id = tk.StringVar()           # ID del producto (deshabilitado)
self.var_nombre = tk.StringVar()       # Nombre del producto
self.var_precio = tk.StringVar()       # Precio (validado como float)
self.var_cantidad = tk.StringVar()     # Cantidad (validada como int)
self.var_descripcion = tk.StringVar()  # Descripción (opcional)
```

### Validaciones en RestauranteServicio

1. **Nombre**: No vacío
2. **Precio**: Número válido, no negativo
3. **Cantidad**: Entero válido, no negativo
4. **Descripción**: Opcional, se trimea
5. **ID**: Generado automáticamente, formato "PXXX"

## Métodos de Interacción (UI → Servicio)

### Registrar Producto
```python
def _registrar_producto(self):
    # Obtener datos del formulario
    # Llamar: restaurante_servicio.registrar_producto(...)
    # Mostrar mensaje
    # Actualizar tabla
    # Limpiar formulario
```

### Cargar Producto
```python
def _cargar_producto(self):
    # Obtener ID
    # Llamar: restaurante_servicio.cargar_producto_por_id(id)
    # Llenar formulario con datos
    # Mostrar mensaje
```

### Actualizar Producto
```python
def _actualizar_producto(self):
    # Validar que hay producto cargado
    # Obtener datos del formulario
    # Llamar: restaurante_servicio.actualizar_producto(...)
    # Mostrar mensaje
    # Actualizar tabla
    # Limpiar formulario
```

### Eliminar Producto
```python
def _eliminar_producto(self):
    # Validar que hay producto cargado
    # Pedir confirmación
    # Llamar: restaurante_servicio.eliminar_producto(id)
    # Mostrar mensaje
    # Actualizar tabla
    # Limpiar formulario
```

### Limpiar Formulario
```python
def _limpiar_formulario(self):
    # Vaciar todas las StringVar
    # Limpiar Text widget
    # Establecer foco en campo Nombre
```

## Flujo de Persistencia

```
Usuario interactúa con UI
    ↓
MainView recibe evento de botón
    ↓
MainView llama método en RestauranteServicio
    ↓
RestauranteServicio valida datos
    ↓
RestauranteServicio ejecuta operación en self.productos
    ↓
RestauranteServicio llama ArchivoServicio.guardar_productos()
    ↓
ArchivoServicio escribe en productos.json
    ↓
MainView recibe resultado (exito, datos)
    ↓
MainView actualiza Treeview automáticamente
    ↓
MainView muestra messagebox con resultado
```

## Conclusión: Componentes Implementados

✅ **Componentes tk**: 6 tipos utilizados  
✅ **Componentes ttk**: 5 tipos utilizados  
✅ **Contenedores**: LabelFrame (3) + Frame (múltiples) + Notebook  
✅ **Gestores**: Pack + Grid combinados estratégicamente  
✅ **Colores**: 8 colores semánticos aplicados  
✅ **Validaciones**: Centralizadas en RestauranteServicio  
✅ **Persistencia**: Automática tras cada operación  

**Objetivo Alcanzado**: Interfaz profesional, modular y fácil de usar, demostrando dominio de componentes y contenedores en Tkinter.
