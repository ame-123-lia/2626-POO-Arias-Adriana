# 🍽️ Sistema de Gestión de Restaurante - Semana 9

## 📋 Descripción General

Este proyecto continúa la evolución del Sistema de Gestión de Restaurante iniciado en semanas anteriores. La mejora principal de la **Semana 9** es el uso estratégico y funcional de las **principales estructuras de datos de Python** (list, tuple, dict, set), integrándolas de manera justificada para resolver necesidades reales del sistema.

**Estudiante**: Adriana Arias  
**Asignatura**: Programación Orientada a Objetos (POO)  
**Semana**: 9  
**Tema**: Estructuras de Datos Aplicadas

---

## 🎯 Objetivos de la Semana 9

- ✅ Utilizar listas para administrar colecciones dinámicas de productos y usuarios
- ✅ Usar tuplas para representar información estable (opciones de menú)
- ✅ Aplicar diccionarios para mapear opciones a funciones
- ✅ Implementar conjuntos para obtener valores únicos sin duplicados
- ✅ Mantener la arquitectura modular del proyecto
- ✅ Asegurar que cada estructura tenga un propósito justificable

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── __init__.py                      # Definición del paquete
├── main.py                          # Punto de entrada y menú principal
│
├── modelos/                         # Capa de modelos de negocio
│   ├── __init__.py
│   ├── producto.py                  # Clase Producto
│   └── usuario.py                   # Clase Usuario
│
└── servicios/                       # Capa de servicios
    ├── __init__.py
    └── restaurante.py               # Servicio Restaurante (CRUD)

README.md                            # Este archivo
```

---

## 🔄 Estructuras de Datos Utilizadas

### 1. **LIST** 📦 - Colecciones Dinámicas

**Ubicación**: `servicios/restaurante.py`

**Uso**:
```python
self._productos: List[Producto] = []  # Lista de productos
self._usuarios: List[Usuario] = []    # Lista de usuarios
```

**Justificación**:
- Las listas permiten almacenar colecciones dinámicas que crecen y se reducen
- Cada producto o usuario se agrega con `append()` y se elimina con `pop()`
- Las búsquedas se realizan iterando la lista con `for`

**Operaciones**:
- `append()`: Registrar nuevo producto/usuario
- `pop()`: Eliminar un elemento por índice
- `len()`: Contar cantidad de elementos
- Iteración: Buscar, actualizar, listar elementos

**Ventaja**: Flexibilidad para agregar, eliminar y modificar elementos en tiempo de ejecución

---

### 2. **TUPLE** 🔒 - Información Estable

**Ubicación**: `main.py`

**Uso**:
```python
MENU_OPCIONES: Tuple[str, ...] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
```

**Justificación**:
- Las tuplas son inmutables, garantizan que las opciones del menú NO cambiarán
- Previene errores accidentales de modificación
- Mejora el rendimiento (tuplas son más rápidas que listas para búsquedas)

**Operaciones**:
- `in`: Validar si una opción es válida
- `len()`: Contar opciones disponibles

**Ventaja**: Inmutabilidad asegura consistencia; mejor performance

---

### 3. **DICTIONARY** 🗺️ - Mapeo Clave → Valor

**Ubicación**: `main.py` (función `main()`)

**Uso**:
```python
acciones: Dict[str, Callable] = {
    "1": lambda: registrar_producto(restaurante),
    "2": lambda: buscar_producto(restaurante),
    "3": lambda: actualizar_producto(restaurante),
    # ... más opciones ...
}
```

**Justificación**:
- El diccionario mapea cada opción de menú con su función correspondiente
- Búsqueda O(1) en lugar de cadenas if-elif
- Código más limpio y fácil de mantener
- Fácil de agregar nuevas opciones

**Operaciones**:
- `get()`: Obtener la función correspondiente a una opción
- `keys()`: Obtener todas las opciones disponibles

**Ventaja**: Performance O(1), código más limpio, extensible

---

### 4. **SET** 🎯 - Valores Únicos Sin Duplicados

**Ubicación**: `servicios/restaurante.py`

**Uso**:
```python
def obtener_categorias_unicas(self) -> Set[str]:
    return {producto.categoria for producto in self._productos}
```

**Justificación**:
- Los conjuntos eliminan automáticamente categorías duplicadas
- No es necesario verificar manualmente si una categoría ya existe
- Presenta de forma clara las categorías disponibles

**Operaciones**:
- Comprensión de set: `{...}` para crear el conjunto
- `len()`: Contar categorías únicas
- Iteración: Mostrar cada categoría

**Ventaja**: Eliminación automática de duplicados, operaciones rápidas

---

## 📊 Ejemplo: Uso Integrado de Estructuras

```python
# LIST: Almacenar productos
_productos = [Producto("P001", "Pizza", "Comida", 12.99), ...]

# TUPLE: Opciones válidas
MENU_OPCIONES = ("1", "2", "3", ..., "9")

# DICT: Mapeo de opciones a funciones
acciones = {
    "1": lambda: registrar_producto(restaurante),
    "2": lambda: buscar_producto(restaurante),
    ...
}

# SET: Categorías únicas
categorias = {"Comida", "Bebida", "Postre"}  # Sin duplicados
```

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
      SISTEMA DE RESTAURANTE - SEMANA 9
   Estructuras de Datos: list, tuple, dict, set
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
  8. Mostrar categorías únicas (SET)
  9. Salir
==================================================
```

---

## 💡 Componentes Principales

### **modelos/producto.py**
- Clase Producto con atributos: código, nombre, categoría, precio
- Validaciones de datos
- Métodos `__str__()` y `__repr__()`

### **modelos/usuario.py**
- Clase Usuario con atributos: identificación, nombre, correo
- Métodos de representación en string

### **servicios/restaurante.py**
- Servicio que gestiona colecciones (LIST)
- CRUD completo de productos y usuarios
- Método para obtener categorías únicas (SET)

### **main.py**
- Menú interactivo con TUPLE y DICT
- Funciones para cada opción del menú
- Coordinación con el servicio Restaurante

---

## 🧪 Ejemplos de Uso

### Registrar un Producto
```
  Seleccione una opción: 1

  📝 Registrar producto:
  Código del producto: P001
  Nombre: Pizza Margherita
  Categoría: Comida
  Precio: 12.99
  ✓ Producto registrado correctamente.
```

### Mostrar Categorías Únicas
```
  Seleccione una opción: 8

  🏷️  --- CATEGORÍAS ÚNICAS (SIN DUPLICADOS) ---
     1. Bebida
     2. Comida
     3. Postre
```

---

## 🎓 Conceptos POO Aplicados

### Encapsulación
- Atributos privados con prefijo `_` en la clase Restaurante
- Métodos públicos para acceso controlado

### Abstracción
- Métodos de alto nivel como `registrar_producto()`, `obtener_categorias_unicas()`
- Complejidad interna oculta

### Polimorfismo
- Métodos `__str__()` en Producto y Usuario
- Representación personalizada según el tipo

### Separación de Responsabilidades
- **Modelos**: Definen las entidades
- **Servicios**: Administran colecciones y operaciones
- **main.py**: Coordina la interfaz de usuario

---

## 🔒 Características Técnicas

- ✅ Type hints en todos los métodos
- ✅ Docstrings descriptivos
- ✅ PEP 8 compliance
- ✅ Importación flexible (paquete o script)
- ✅ Manejo de excepciones básico
- ✅ Validaciones de entrada

---

## 📈 Flujo del Programa

```
Inicio del programa
    ↓
Mostrar bienvenida
    ↓
Mostrar menú (TUPLE de opciones)
    ↓
Usuario selecciona una opción
    ↓
Buscar en DICTIONARY de acciones
    ↓
Ejecutar función correspondiente
    ↓
Función utiliza servicio (con LIST)
    ↓
Mostrar resultado
    ↓
¿Es opción 9? → SI: Salir
                 NO: Volver al menú
```

---

## ✅ Validaciones Implementadas

- ✔ Códigos únicos para productos (búsqueda en LIST)
- ✔ Identificaciones únicas para usuarios
- ✔ Precios válidos (no negativos)
- ✔ Opciones de menú válidas (TUPLE)
- ✔ Función encontrada en DICT antes de ejecutar

---

## 🎯 Importancia de Seleccionar la Estructura Correcta

### ¿Por qué LIST en lugar de TUPLE?
- Los productos cambian durante la ejecución (agregar, eliminar)
- Las tuplas son inmutables, no sirven para colecciones dinámicas

### ¿Por qué TUPLE para opciones?
- Las opciones de menú permanecen iguales durante toda la ejecución
- La inmutabilidad previene errores accidentales

### ¿Por qué DICT para acciones?
- Necesitamos asociar cada opción con su función
- Búsqueda directa O(1) en lugar de if-elif-elif-elif...

### ¿Por qué SET para categorías?
- No queremos duplicados
- El SET automáticamente elimina elementos repetidos

---

## 📚 Comparación de Estructuras

| Estructura | Ordenada | Mutable | Duplicados | Búsqueda | Uso |
|-----------|----------|---------|------------|----------|-----|
| **List** | ✅ Sí | ✅ Sí | ✅ Sí | O(n) | Colecciones dinámicas |
| **Tuple** | ✅ Sí | ❌ No | ✅ Sí | O(n) | Datos inmutables |
| **Dict** | ✅ Sí* | ✅ Sí | ❌ No (claves) | O(1) | Mapeos clave-valor |
| **Set** | ❌ No | ✅ Sí | ❌ No | O(1) | Valores únicos |

*Desde Python 3.7, los diccionarios mantienen orden de inserción

---

## 🔍 Verificación del Proyecto

Pruebas recomendadas:
1. ✅ Registrar múltiples productos
2. ✅ Buscar productos por código
3. ✅ Actualizar información de productos
4. ✅ Eliminar productos
5. ✅ Listar todos los productos
6. ✅ Registrar usuarios
7. ✅ Mostrar categorías únicas (debe eliminar duplicados)
8. ✅ Validar que códigos duplicados no se permitan

---

## 📊 Estadísticas

- **Archivos creados**: 6
- **Líneas de código**: ~600
- **Métodos implementados**: 15+
- **Estructuras de datos**: 4 (list, tuple, dict, set)

---

## 🎓 Conceptos Aprendidos

✅ Estructura y mutabilidad de datos en Python  
✅ Selección apropiada de estructura según necesidad  
✅ Performance de búsqueda O(n) vs O(1)  
✅ Comprensiones de listas y conjuntos  
✅ Type hints y type safety  
✅ Arquitectura modular de aplicaciones  

---

## 🚀 Próximos Pasos (Semana 10)

La Semana 10 agregará:
- ✅ Persistencia de datos en JSON
- ✅ Servicio especializado para manejo de archivos
- ✅ Serialización/deserialización de objetos
- ✅ Manejo robusto de excepciones de archivo

---

## 📞 Información

**Estudiante**: Adriana Arias  
**Asignatura**: Programación Orientada a Objetos (POO)  
**Código del Curso**: 2626  
**Semana**: 9  

---

**Última actualización**: Semana 9 - 2024  
**Estado**: ✅ Completo y funcional  
**Versión**: 1.0
