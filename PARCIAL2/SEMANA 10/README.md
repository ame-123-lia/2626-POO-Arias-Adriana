# 🍽️ Sistema de Gestión de Restaurante - Semana 10

## 📋 Descripción General

Este proyecto continúa la evolución del Sistema de Gestión de Restaurante iniciado en semanas anteriores. La mejora principal de la **Semana 10** es la implementación de **persistencia de datos en JSON**, permitiendo que los productos registrados se guarden en un archivo externo y se recuperen automáticamente al reiniciar la aplicación.

**Estudiante**: Adriana Arias  
**Asignatura**: Programación Orientada a Objetos (POO)  
**Semana**: 10  
**Tema**: Manejo de archivos, excepciones y persistencia JSON

---

## 🎯 Objetivos de la Semana 10

- ✅ Implementar persistencia de productos mediante JSON
- ✅ Manejar excepciones específicas en operaciones de archivo
- ✅ Crear un servicio dedicado a la carga y guardado de datos
- ✅ Reconstruir objetos Producto a partir de datos almacenados
- ✅ Mantener la arquitectura modular del proyecto
- ✅ Asegurar que los datos persistan entre ejecuciones

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── __init__.py                      # Definición del paquete
├── main.py                          # Punto de entrada y menú principal
│
├── modelos/                         # Capa de modelos de negocio
│   ├── __init__.py
│   ├── producto.py                  # Clase Producto con serialización
│   └── usuario.py                   # Clase Usuario
│
├── servicios/                       # Capa de servicios
│   ├── __init__.py
│   ├── restaurante.py               # Servicio Restaurante (CRUD)
│   └── archivo_servicio.py          # Servicio de persistencia JSON
│
└── datos/                           # Almacenamiento de archivos
    └── productos.json               # Base de datos de productos (JSON)

README.md                            # Este archivo
```

---

## 🔄 Flujo de Carga de Datos

```
Inicio de la aplicación
       ↓
main.py crea ArchivoServicio
       ↓
ArchivoServicio.cargar_productos()
       ↓
Lectura de datos/productos.json
       ↓
json.load() recupera la información
       ↓
Validación de estructura
       ↓
Producto.from_dict() reconstruye cada producto
       ↓
Restaurante.registrar_producto() incorpora los objetos
       ↓
Menú interactivo con datos disponibles
```

---

## 💾 Flujo de Guardado de Datos

```
Usuario realiza una acción (registra, actualiza o elimina)
       ↓
main.py solicita la operación al Restaurante
       ↓
Restaurante valida y modifica la colección en memoria
       ↓
main.py solicita a ArchivoServicio guardar cambios
       ↓
producto.to_dict() convierte cada objeto a diccionario
       ↓
json.dump() escribe en datos/productos.json
       ↓
Archivo actualizado con éxito
```

---

## 📝 Componentes Principales

### 1. **modelos/producto.py** - Clase Producto

**Responsabilidades:**
- Representar un producto con atributos: código, nombre, categoría, precio y stock
- Validar integridad de datos (precios no negativos, stock válido)
- Proporcionar métodos de serialización `to_dict()` y `from_dict()`

**Métodos destacados:**
```python
def __init__(self, codigo, nombre, categoria, precio, stock=0)
    # Validaciones de datos

def to_dict() -> Dict[str, Any]
    # Convierte el producto a diccionario para JSON

@classmethod
def from_dict(cls, data: Dict[str, Any]) -> "Producto"
    # Reconstruye un Producto desde un diccionario
    # Lanza KeyError si faltan claves
    # Lanza ValueError si datos son inválidos

def vender(cantidad: int)
    # Disminuye el stock (usado en operaciones de venta)
```

### 2. **modelos/usuario.py** - Clase Usuario

**Responsabilidades:**
- Representar un usuario del sistema
- Almacenar identificación, nombre y correo

**Nota**: En esta semana, los usuarios permanecen en memoria. La persistencia es solo para productos.

### 3. **servicios/restaurante.py** - Servicio Restaurante

**Responsabilidades:**
- Administrar colecciones de productos y usuarios
- Implementar operaciones CRUD (Create, Read, Update, Delete)
- Coordinar operaciones de venta

**Métodos principales:**
```python
# Productos
def registrar_producto(producto: Producto) -> bool
def buscar_producto_por_codigo(codigo: str) -> Optional[Producto]
def actualizar_producto(codigo, nombre=None, categoria=None, precio=None) -> bool
def eliminar_producto(codigo: str) -> bool
def listar_productos() -> List[str]
def obtener_productos_como_lista() -> List[Producto]

# Usuarios
def registrar_usuario(usuario: Usuario) -> bool
def buscar_usuario_por_id(identificacion: str) -> Optional[Usuario]
def listar_usuarios() -> List[str]

# Ventas
def vender_producto(codigo_producto: str, cantidad: int) -> bool
```

### 4. **servicios/archivo_servicio.py** - Servicio de Persistencia

**Responsabilidades:**
- Cargar productos desde `productos.json`
- Guardar productos en `productos.json`
- Manejar excepciones específicas de archivo y JSON
- Validar estructura de datos

**Métodos principales:**
```python
def __init__(self, ruta_archivo: str)
    # Inicializa con la ruta del archivo

def cargar_productos() -> List[Producto]
    # Carga productos desde JSON
    # Maneja: FileNotFoundError, JSONDecodeError, PermissionError, KeyError, ValueError

def guardar_productos(productos: List[Producto]) -> bool
    # Guarda productos a JSON
    # Maneja: PermissionError, IOError, TypeError
```

---

## ⚠️ Excepciones Controladas

### Operaciones de Carga

| Excepción | Causa | Acción |
|-----------|-------|--------|
| `FileNotFoundError` | Archivo no existe (primera ejecución) | Se inicia con colección vacía |
| `json.JSONDecodeError` | Contenido no es JSON válido | Se muestra advertencia y se carga vacío |
| `PermissionError` | Sin permisos de lectura | Se muestra error y se carga vacío |
| `KeyError` | Falta una clave en un registro | Se omite ese producto y continúa |
| `ValueError` | Datos inválidos en un producto | Se omite ese producto y continúa |

### Operaciones de Guardado

| Excepción | Causa | Acción |
|-----------|-------|--------|
| `PermissionError` | Sin permisos de escritura | Se muestra error, retorna False |
| `IOError` | Error general de entrada/salida | Se muestra error, retorna False |
| `TypeError` | Objeto no es serializable | Se muestra error, retorna False |

---

## 📋 Archivo productos.json

### Estructura

```json
[
  {
    "codigo": "P001",
    "nombre": "Pizza Margherita",
    "categoria": "Platos Principales",
    "precio": 12.99,
    "stock": 50
  },
  ...
]
```

### Datos de Ejemplo Incluidos

**Platos Principales:**
- P001: Pizza Margherita - $12.99 (50 unidades)
- P002: Pasta Carbonara - $14.50 (35 unidades)
- P004: Salmón a la Mantequilla - $22.99 (20 unidades)

**Ensaladas:**
- P003: Ensalada César - $8.99 (40 unidades)

**Sopas:**
- P005: Sopa de Tomate - $6.50 (30 unidades)

**Bebidas:**
- B001: Agua Natural - $2.00 (100 unidades)
- B002: Jugo de Naranja - $4.50 (60 unidades)
- B003: Café Americano - $3.50 (80 unidades)

**Postres:**
- D001: Brownie de Chocolate - $5.99 (25 unidades)
- D002: Helado de Vainilla - $4.99 (45 unidades)

---

## 🚀 Cómo Usar

### Requisitos Previos
- Python 3.8 o superior
- No se requieren dependencias externas

### Ejecución

#### Opción 1: Ejecutar como script directo
```bash
cd restaurante_app
python main.py
```

#### Opción 2: Ejecutar como paquete
```bash
python -m restaurante_app.main
```

---

## 📊 Menú Principal

```
==================================================
   SISTEMA DE RESTAURANTE - SEMANA 10
   Persistencia JSON de Productos
==================================================
PRODUCTOS:
  1. Registrar producto
  2. Buscar producto
  3. Actualizar producto
  4. Eliminar producto
  5. Listar productos
--------------------------------------------------
USUARIOS:
  6. Registrar usuario
  7. Listar usuarios
--------------------------------------------------
  8. Consultar información de persistencia
  9. Salir
==================================================
```

---

## 🧪 Comprobación de Persistencia

Siga estos pasos para verificar que la persistencia funciona correctamente:

### Prueba 1: Carga Inicial
1. Ejecute `python main.py`
2. Seleccione opción 5 (Listar productos)
3. Verifique que carga los 10 productos de ejemplo
4. Seleccione opción 8 para ver información de persistencia

### Prueba 2: Registro de Nuevo Producto
1. Seleccione opción 1 (Registrar producto)
2. Ingrese datos: código "P999", nombre "Producto Test", categoría "Test", precio "9.99", stock "10"
3. Verifique el mensaje de confirmación
4. Abra `datos/productos.json` con un editor de texto
5. Confirme que el nuevo producto está al final del archivo

### Prueba 3: Persistencia Real
1. Seleccione opción 5 para listar (debería ver el nuevo producto)
2. **Cierre completamente el programa** (Ctrl+C o seleccione 9)
3. **Ejecute nuevamente** `python main.py`
4. Seleccione opción 5
5. Confirme que **el producto registrado sigue disponible**

### Prueba 4: Actualización
1. Seleccione opción 3 (Actualizar producto)
2. Ingrese código "P001" (Pizza Margherita)
3. Actualice el precio a "15.99"
4. Cierre y reinicie la aplicación
5. Busque o liste el producto
6. Confirme que el precio cambió permanentemente

### Prueba 5: Eliminación
1. Seleccione opción 4 (Eliminar producto)
2. Ingrese código "P999" (el producto de prueba)
3. Cierre y reinicie la aplicación
4. Intente buscar "P999"
5. Confirme que ya no existe

---

## 🎓 Conceptos POO Implementados

### Encapsulación
- Atributos privados en Restaurante (`_productos`, `_usuarios`)
- Métodos públicos para acceso controlado
- Validación en setters

### Serialización de Objetos
- Método `to_dict()` convierte objetos a diccionarios
- Método `from_dict()` reconstruye objetos desde diccionarios
- Patrón polimórfico en conversiones

### Manejo de Excepciones
- Excepciones específicas para cada tipo de error
- Mensajes descriptivos para el usuario
- El programa continúa funcionando ante errores controlados

### Separación de Responsabilidades
- **Restaurante**: Lógica de negocio (CRUD)
- **ArchivoServicio**: Persistencia (JSON)
- **main.py**: Interfaz de usuario
- **Producto/Usuario**: Modelos de datos

---

## 💡 Puntos Técnicos Importantes

### Type Hints
Todo el código utiliza anotaciones de tipo para mayor claridad:
```python
def cargar_productos(self) -> List[Producto]:
    ...

def actualizar_producto(
    self, 
    codigo: str, 
    nombre: Optional[str] = None
) -> bool:
    ...
```

### Manejo de Rutas
Se utiliza `pathlib.Path` para compatibilidad entre sistemas:
```python
base = Path(__file__).resolve().parent
ruta_productos = str(base / "datos" / "productos.json")
```

### Codificación UTF-8
Se especifica siempre la codificación en operaciones de archivo:
```python
with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
    ...
```

### JSON con Indentación
El archivo se guarda con indentación para legibilidad:
```python
json.dump(registros, archivo, indent=2, ensure_ascii=False)
```

---

## ✅ Validaciones Implementadas

- ✔ Códigos únicos para productos
- ✔ Precios no negativos
- ✔ Stock válido (no negativo)
- ✔ Estructura JSON válida
- ✔ Registros incompletos se omiten sin detener el programa
- ✔ Datos inválidos se reportan con claridad
- ✔ Archivo ausente se maneja gracefully

---

## 🔒 Seguridad y Buenas Prácticas

- ✅ No se realizan operaciones de archivo sin manejo de excepciones
- ✅ Los objetos Producto validan sus datos
- ✅ No se modifica directamente `_productos` desde fuera de Restaurante
- ✅ Nombres descriptivos y convenciones PEP 8
- ✅ Docstrings en todas las clases y métodos
- ✅ Mensajes de error claros y útiles

---

## 📦 Importación Flexible

El código soporta dos formas de ejecución:

```python
try:
    # Como paquete
    from .servicios.restaurante import Restaurante
except ImportError:
    # Como script directo
    from servicios.restaurante import Restaurante
```

Esto permite:
```bash
# Opción 1: Desde el directorio restaurante_app
cd restaurante_app
python main.py

# Opción 2: Desde la raíz del proyecto
python -m restaurante_app.main
```

---

## 📚 Archivos Generados

- `restaurante_app/main.py` - Programa principal (298 líneas)
- `restaurante_app/modelos/producto.py` - Clase Producto (114 líneas)
- `restaurante_app/modelos/usuario.py` - Clase Usuario (31 líneas)
- `restaurante_app/servicios/restaurante.py` - Servicio Restaurante (185 líneas)
- `restaurante_app/servicios/archivo_servicio.py` - Servicio de Persistencia (151 líneas)
- `restaurante_app/datos/productos.json` - Base de datos (280 líneas)
- `README.md` - Este archivo

**Total**: ~1,000+ líneas de código

---

## 🎯 Mejoras Respecto a Semanas Anteriores

| Semana | Mejora |
|--------|--------|
| Semanas 4-9 | Estructura básica sin persistencia |
| **Semana 10** | ✨ **Persistencia en JSON** |
| **Semana 10** | ✨ **Manejo robusto de excepciones** |
| **Semana 10** | ✨ **Servicio dedicado a archivos** |
| **Semana 10** | ✨ **Reconstrucción de objetos** |

---

## 🚦 Estado del Proyecto

- [x] Estructura modular implementada
- [x] Clases de modelos con validaciones
- [x] Servicio Restaurante con CRUD completo
- [x] Servicio de persistencia JSON funcional
- [x] Menú interactivo
- [x] Manejo de excepciones específicas
- [x] Datos de ejemplo incluidos
- [x] Persistencia verificada
- [x] Documentación completa

---

## 🔍 Ejemplo de Ejecución

```
  Cargando datos...

  ✓ 10 producto(s) cargado(s) desde JSON.

==================================================
   SISTEMA DE RESTAURANTE - SEMANA 10
   Persistencia JSON de Productos
==================================================
PRODUCTOS:
  1. Registrar producto
  2. Buscar producto
  3. Actualizar producto
  4. Eliminar producto
  5. Listar productos
...
  Seleccione una opción: 5

  📋 --- PRODUCTOS REGISTRADOS ---
     Código: P001 | Nombre: Pizza Margherita | Categoría: Platos Principales | Precio: $12.99 | Stock: 50
     Código: P002 | Nombre: Pasta Carbonara | Categoría: Platos Principales | Precio: $14.50 | Stock: 35
     ... (más productos)
```

---

## 📞 Contacto e Información

**Estudiante**: Adriana Arias  
**Asignatura**: Programación Orientada a Objetos (POO)  
**Curso**: 2626  
**Semana**: 10  

---

**Última actualización**: Semana 10 - 2024  
**Estado**: ✅ Completo y funcional  
**Versión**: 1.0
