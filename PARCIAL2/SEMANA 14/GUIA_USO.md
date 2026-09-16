# Guía de Uso - Diseño Doble Panel

## 🎯 Descripción Rápida

El nuevo diseño **Doble Panel** organiza la interfaz de productos en dos secciones:

- **Panel Izquierdo**: Lista siempre visible de todos los productos
- **Panel Derecho**: Formulario que se actualiza al seleccionar un producto

## 👀 Antes vs. Después

### ❌ Diseño Anterior (Secuencial)
```
┌─────────────────────────────────┐
│ Formulario (arriba)             │  ← Llenar datos
│ Botones (en medio)              │  ← Seleccionar acción
│ Tabla de productos (abajo)      │  ← Ver resultados
│ (necesitaba scroll)             │  ← Mala experiencia
└─────────────────────────────────┘
```
**Problemas:**
- ❌ Necesitaba scroll vertical para ver todo
- ❌ Formulario y tabla separados
- ❌ Flujo poco intuitivo
- ❌ Difícil saber qué hacer

### ✅ Diseño Nuevo (Doble Panel)
```
┌──────────────────┬─────────────────────────┐
│ LISTA DE PRODUCTOS│ FORMULARIO & ACCIONES │
│                  │                       │
│ • P001 - Hamb   │ ID: [P001]            │
│ • P002 - Pizza  │ Nombre: [Hamburguesa] │
│ • P003 - Pasta  │ Precio: [8.99]        │
│ • ...           │ Cantidad: [50]        │
│                  │ Descripción: [...]    │
│ + Nuevo          │                       │
│                  │ [Guardar | Act | Del] │
└──────────────────┴─────────────────────────┘
```
**Ventajas:**
- ✅ Todo visible sin scroll
- ✅ Lista siempre accesible
- ✅ Flujo claro: Seleccionar → Editar
- ✅ Interfaz intuitiva

## 📖 Casos de Uso

### Caso 1: Ver Todos los Productos

**¿Qué quiero?** Ver qué productos tengo registrados

**Paso a paso:**
1. Abrir la aplicación
2. Ir a Tab "Productos"
3. ✅ **Panel izquierdo muestra lista completa**

**Resultado:**
- Ves todos los productos de un vistazo
- Puedes contar, comparar precios
- Identifica cuál necesitas editar

---

### Caso 2: Crear Nuevo Producto

**¿Qué quiero?** Agregar un nuevo producto al restaurante

**Paso a paso:**
1. Tab "Productos" ya abierta
2. Clic en botón **"+ Nuevo Producto"** (panel izquierdo)
   ```
   ┌──────────────┐
   │+ Nuevo Prod. │ ← Aquí
   └──────────────┘
   ```
3. Panel derecho se limpia (sin ID, campos vacíos)
4. **Llenar datos:**
   - Nombre: "Tacos al Pastor"
   - Precio: "13.50"
   - Cantidad: "35"
   - Descripción: "Tacos auténticos..."
5. Clic en **"Guardar"** (panel derecho)
   ```
   [Guardar] ← Aquí
   ```
6. ✅ Mensaje: "Producto registrado: P007 - Tacos al Pastor"
7. ✅ Producto aparece en la lista (panel izquierdo)
8. ✅ Panel derecho se limpia para otro producto

**Resultado:**
- Nuevo producto guardado en JSON
- Inmediatamente visible en lista
- Puedes crear otro o editar este

---

### Caso 3: Modificar Producto Existente

**¿Qué quiero?** Cambiar precio de un producto

**Paso a paso:**
1. Tab "Productos" abierta
2. **Clic en el producto en la lista** (panel izquierdo)
   ```
   P001 - Hamburguesa Clásica ← Aquí
   ```
3. ✅ Panel derecho se rellena automáticamente:
   - ID: P001
   - Nombre: Hamburguesa Clásica
   - Precio: 8.99
   - Cantidad: 50
   - Descripción: [...]
4. **Modificar el campo deseado:**
   - Cambiar Precio de 8.99 → 9.99
   - O cambiar Cantidad de 50 → 45
5. Clic en **"Actualizar"** (panel derecho)
   ```
   [Guardar | Actualizar] ← Aquí
   ```
6. ✅ Mensaje: "Producto actualizado: Hamburguesa Clásica"
7. ✅ Cambio visible inmediatamente en lista

**Resultado:**
- Producto actualizado en JSON
- Lista refleja cambios
- Producto sigue seleccionado

---

### Caso 4: Eliminar Producto

**¿Qué quiero?** Borrar un producto que ya no ofrecemos

**Paso a paso:**
1. Tab "Productos" abierta
2. **Clic en el producto en la lista** (panel izquierdo)
3. Panel derecho muestra sus datos
4. Clic en **"Eliminar"** (panel derecho)
   ```
   [... | Actualizar | Eliminar] ← Aquí
   ```
5. ⚠️ Ventana de confirmación aparece:
   ```
   ¿Eliminar producto P001?
   [Sí] [No]
   ```
6. **Clic en "Sí"**
7. ✅ Mensaje: "Producto P001 eliminado"
8. ✅ Producto desaparece de la lista
9. ✅ Panel derecho se limpia

**Resultado:**
- Producto eliminado de JSON
- Lista actualizada automáticamente
- Puedes seguir trabajando

---

### Caso 5: Limpiar Formulario

**¿Qué quiero?** Empezar de nuevo sin perder datos

**Paso a paso:**
1. Panel derecho tiene datos (de un producto seleccionado)
2. Clic en **"Limpiar Formulario"** (abajo, panel derecho)
   ```
   [  Limpiar Formulario  ]
   ```
3. ✅ Todos los campos se vacían
4. ✅ Panel izquierdo: ningún producto seleccionado
5. ✅ Listo para crear nuevo o seleccionar otro

**Resultado:**
- Comienza nuevo flujo
- No se pierden datos (solo si no guardaste)

---

## 🔄 Flujo Completo de Día de Trabajo

```
1. INICIO
   └─ Tab "Productos"
      └─ Ver lista de productos

2. REVISAR INVENTARIO
   └─ Hacer clic en productos
   └─ Revisar precios, cantidades

3. HACER CAMBIOS
   ├─ Agregar nuevo → [+ Nuevo] → Llenar → [Guardar]
   ├─ Actualizar existente → [Clic] → Editar → [Actualizar]
   ├─ Eliminar → [Clic] → [Eliminar] → Confirmar
   └─ Limpiar → [Limpiar Formulario]

4. VERIFICAR CAMBIOS
   └─ Lista muestra actualizaciones en tiempo real

5. SALIR
   └─ Datos guardados en JSON automáticamente
```

---

## 🎨 Elementos Visuales

### Panel Izquierdo

```
┌──────────────────────────┐
│      PRODUCTOS           │
├──────────────────────────┤
│ + Nuevo Producto         │ ← Botón verde
├──────────────────────────┤
│ P001 - Hamb... ($8.99)   │
│ P002 - Pizza... ($12.50) │
│ P003 - Pasta... ($10.99) │
│ P004 - Ensala... ($7.50) │
│ P005 - Papas... ($3.99)  │
│ P006 - Refres... ($2.50) │
│                          │
│ ↕ Scrollbar (si hay más) │
└──────────────────────────┘
```

**Componentes:**
- Título: "PRODUCTOS" (ttk.LabelFrame)
- Botón: "+ Nuevo Producto" (verde)
- Lista: Listbox con todos los productos
- Scrollbar: Para navegar si hay muchos

---

### Panel Derecho

```
┌──────────────────────────────────┐
│    DETALLES DEL PRODUCTO         │
├──────────────────────────────────┤
│ ID:          [P001]              │ ← Deshabilitado
│ Nombre:      [Hamburguesa Clási..│
│ Precio ($):  [8.99]              │
│ Cantidad:    [50]                │
│ Descripción: [Hamburguesa con    │
│              carne de res...    ] │
├──────────────────────────────────┤
│ [Guardar] [Actualizar] [Eliminar]│ ← Botones acción
│                                  │
│  [  Limpiar Formulario  ]        │ ← Botón limpiar
└──────────────────────────────────┘
```

**Componentes:**
- Título: "DETALLES DEL PRODUCTO" (ttk.LabelFrame)
- Campos de entrada (Entry y Text)
- Botones de acción (colores semánticos)
- Separador visual

**Colores de botones:**
- 🟢 Verde: Guardar (crear nuevo)
- 🟠 Naranja: Actualizar (modificar)
- 🔴 Rojo: Eliminar (borrar)
- ⚫ Gris: Limpiar

---

## ⚠️ Cosas Importantes

### Validaciones

Si intentas operaciones inválidas:

**Guardar sin nombre:**
```
❌ Error: El nombre del producto no puede estar vacío
```

**Guardar con precio negativo:**
```
❌ Error: El precio no puede ser negativo
```

**Actualizar sin seleccionar producto:**
```
⚠️  Advertencia: Seleccione un producto de la lista
```

**Eliminar sin confirmar:**
```
⚠️  Se cancela la eliminación
```

### Persistencia

✅ Todos los cambios se guardan **automáticamente** en `productos.json`
✅ No necesitas clic en "Guardar Archivo"
✅ Si cierras y abres la app, los datos están allí

---

## 🆘 Solución de Problemas

**P: No veo ningún producto en la lista**
- R: Espera a que cargue, o verifica que productos.json tenga datos

**P: Clic en producto pero no se actualiza el formulario**
- R: Asegúrate de hacer clic dentro del área de la lista, no en la barra de scroll

**P: ¿Qué pasa si modifico un campo sin guardar?**
- R: Si cambias de producto sin actualizar, los cambios se pierden

**P: ¿Puedo deshacer una eliminación?**
- R: No hay deshacer. Se te pide confirmación para evitar accidentes

**P: ¿Por qué el ID está deshabilitado?**
- R: El ID se genera automáticamente y es único. No puede modificarse

---

## 📋 Resumen de Botones

| Botón | Color | Ubicación | Función |
|-------|-------|-----------|---------|
| + Nuevo Producto | Verde | Panel izq, arriba | Limpia formulario para crear nuevo |
| Guardar | Verde | Panel der, botones | Registra nuevo producto |
| Actualizar | Naranja | Panel der, botones | Modifica producto existente |
| Eliminar | Rojo | Panel der, botones | Borra producto (con confirmación) |
| Limpiar Formulario | Gris | Panel der, abajo | Vacía todos los campos |

---

## ✅ Checklist de Funcionalidad

- [ ] Abro la app y veo la lista de productos
- [ ] Hago clic en un producto y se carga en el formulario
- [ ] Puedo crear un nuevo producto
- [ ] Puedo modificar un producto existente
- [ ] Puedo eliminar un producto
- [ ] Los cambios persisten al cerrar la app
- [ ] Todo es visible sin scroll horizontal

**Si todo está ✓, ¡estás listo para trabajar!**

---

**Versión**: Semana 14 v2.0 (Doble Panel)  
**Diseño**: Intuitivo, claro, profesional  
**Estado**: ✅ Listo para usar
