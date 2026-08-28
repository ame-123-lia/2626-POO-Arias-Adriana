# 🍽️ Sistema de Gestión de Restaurante - Semana 11

## Descripción General

Este proyecto es un **Sistema de Gestión de Restaurante** desarrollado en Python que implementa principios de **Programación Orientada a Objetos (POO)** para manejar productos, usuarios y ventas de un restaurante. El sistema proporciona una interfaz de línea de comandos interactiva para gestionar todas las operaciones del negocio.

---

## 🎯 Características Principales

### 📦 Gestión de Productos
- ✅ Registrar nuevos productos con código, nombre, categoría, precio y stock
- 🔍 Buscar productos por código
- ✏️ Actualizar información de productos existentes
- 🗑️ Eliminar productos del catálogo
- 📋 Listar todos los productos disponibles

### 👥 Gestión de Usuarios
- ✅ Registrar nuevos usuarios con identificación, nombre y correo
- 📋 Listar todos los usuarios del sistema
- 🔗 Asociación de usuarios con sus compras

### 💳 Gestión de Ventas
- 💰 Realizar ventas (descontar stock automáticamente)
- 📊 Consultar historial de compras de un usuario específico
- 📈 Ver todas las ventas registradas en el sistema

### 💾 Almacenamiento Persistente
- 📁 Datos guardados en archivos JSON (productos.json, usuarios.json, ventas.json)
- 🔄 Carga automática de datos al iniciar la aplicación
- ⚡ Guardado automático tras cada operación

---

## 📁 Estructura del Proyecto

```
restaurante_app/
├── __init__.py                 # Definición del paquete
├── main.py                     # Punto de entrada y menú principal
├── datos/                      # Almacenamiento de datos en JSON
│   ├── productos.json         # Base de datos de productos
│   ├── usuarios.json          # Base de datos de usuarios
│   └── ventas.json            # Base de datos de transacciones
├── modelos/                    # Clases que representan entidades
│   ├── __init__.py
│   ├── producto.py            # Clase Producto
│   ├── usuario.py             # Clase Usuario
│   └── venta.py               # Clase Venta
└── servicios/                  # Lógica de negocio
    ├── __init__.py
    ├── restaurante.py         # Servicio principal (Restaurante)
    └── archivo_servicio.py    # Servicio de persistencia JSON
```

---

## 🏗️ Arquitectura y Patrones

### Capas del Proyecto

1. **Capa de Modelos** (`modelos/`)
   - Clases que representan las entidades del negocio
   - Incluyen validaciones y métodos de serialización JSON

2. **Capa de Servicios** (`servicios/`)
   - **Restaurante**: Orquesta la lógica de negocio (CRUD de productos, usuarios, ventas)
   - **ArchivoServicio**: Maneja la persistencia de datos en JSON

3. **Capa de Presentación** (`main.py`)
   - Interfaz de línea de comandos
   - Menú interactivo
   - Validación de entrada del usuario

### Patrones Utilizados

- **MVC (Modelo-Vista-Controlador)**: Separación de responsabilidades
- **DAO (Data Access Object)**: ArchivoServicio actúa como DAO para JSON
- **Tipo Hints**: Anotaciones de tipo para mayor legibilidad
- **Excepciones Personalizadas**: Manejo robusto de errores
- **Métodos de Clase**: `from_dict()` para deserialización

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
      SISTEMA DE RESTAURANTE (Semana 11)
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
VENTAS:
8. Realizar venta
9. Consultar ventas de usuario
10. Listar todas las ventas
--------------------------------------------------
11. Salir
```

---

## 📝 Ejemplos de Uso

### Registrar un Producto
```
Seleccione una opción: 1
📝 Registrar producto:
  Código del producto: P001
  Nombre: Pizza Margherita
  Categoría: Platos Principales
  Precio: 12.99
  Stock inicial: 50
  ✓ Producto registrado correctamente.
```

### Registrar un Usuario
```
Seleccione una opción: 6
📝 Registrar usuario:
  Identificación: 1234567890
  Nombre: Juan Pérez
  Correo: juan@email.com
  ✓ Usuario registrado correctamente.
```

### Realizar una Venta
```
Seleccione una opción: 8
💳 Realizar venta:
  Identificación del usuario: 1234567890
  Código del producto: P001
  Producto: Pizza Margherita | Stock disponible: 50
  Cantidad a vender: 2
  ✓ Venta registrada. Nuevo stock: 48
```

---

## 🏛️ Conceptos POO Implementados

### Encapsulación
- Atributos privados con prefijo `_` (ej: `self._productos`)
- Propiedades y métodos públicos para acceder a los datos

### Herencia
- La clase `Producto` y otras heredan validaciones comunes
- Métodos `from_dict()` estandarizados en las clases

### Polimorfismo
- Métodos `to_dict()` y `from_dict()` en todas las entidades
- Método `mostrar_informacion()` personalizado en cada modelo

### Abstracción
- Interfaces simples: `registrar_producto()`, `realizar_venta()`, etc.
- Complejidad interna oculta en las clases de servicio

---

## 💾 Formato de Datos JSON

### productos.json
```json
[
  {
    "codigo": "P001",
    "nombre": "Pizza Margherita",
    "categoria": "Platos Principales",
    "precio": 12.99,
    "stock": 48
  }
]
```

### usuarios.json
```json
[
  {
    "identificacion": "1234567890",
    "nombre": "Juan Pérez",
    "correo": "juan@email.com"
  }
]
```

### ventas.json
```json
[
  {
    "id": "V001",
    "identificacion_usuario": "1234567890",
    "codigo_producto": "P001",
    "cantidad": 2,
    "fecha": "2024-11-27",
    "monto_total": 25.98
  }
]
```

---

## ✅ Validaciones Implementadas

- ✔ Códigos únicos para productos y usuarios
- ✔ Precios no negativos
- ✔ Stock válido (no puede ser negativo)
- ✔ Cantidad válida en ventas
- ✔ Verificación de stock disponible antes de vender
- ✔ Validación de entrada de usuario
- ✔ Manejo de excepciones en carga de JSON

---

## 🔒 Manejo de Errores

El sistema implementa un robusto manejo de errores:

```python
try:
    # Operaciones
except ValueError as e:
    print(f"❌ Error de validación: {e}")
except KeyError as e:
    print(f"❌ Falta la clave {e}")
except PermissionError as e:
    print(f"❌ Permiso denegado: {e}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
```

---

## 🎓 Objetivos de Aprendizaje Alcanzados

- ✅ Diseño de clases con responsabilidades claras
- ✅ Uso de colecciones (listas, diccionarios)
- ✅ Serialización y deserialización JSON
- ✅ Manejo de excepciones
- ✅ Interfaces de usuario intuitivas
- ✅ Patrones de diseño (MVC, DAO)
- ✅ Type hints y documentación

---

## 👨‍💻 Notas para Desarrolladores

### Importaciones Flexibles
El código soporta dos formas de ejecución:
- Como paquete: importes relativos
- Como script: importes absolutos

```python
try:
    from .servicios.restaurante import Restaurante  # Paquete
except Exception:
    from servicios.restaurante import Restaurante   # Script
```

### Extensibilidad
Para agregar nuevas funcionalidades:
1. Crear una nueva clase en `modelos/`
2. Agregar métodos en `servicios/restaurante.py`
3. Crear funciones en `main.py` para la UI
4. Agregar opciones al menú

---

## 📞 Soporte

Para más información sobre el código, consulte los comentarios dentro de cada archivo o revise la documentación de las clases.

---

**Versión**: 1.0  
**Última actualización**: Semana 11 - 2024  
**Autor**: Adriana Arias  
**Asignatura**: Programación Orientada a Objetos (POO)
