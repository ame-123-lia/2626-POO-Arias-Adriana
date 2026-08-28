# Sistema de Gestión de Restaurante — Semana 5

## Descripción

Aplicación didáctica que demuestra la aplicación de identificadores descriptivos, tipos de datos básicos, convenciones de nombres (PascalCase y snake_case), clases, objetos, constructores, métodos especiales (`__str__()`), importaciones y listas como tipo de dato compuesto en un proyecto modular de Python.

## Objetivo

Desarrollar un sistema básico de gestión de restaurante que evidencie el correcto uso de:
- Convenciones de nombres en Python
- Tipos de datos primitivos y compuestos
- Programación Orientada a Objetos (POO)
- Estructura modular con paquetes
- Anotaciones de tipo
- Importaciones entre módulos

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante (gestor principal)
└── main.py                  # Punto de entrada del programa
```

## Componentes Principales

### 1. Clase Producto (`modelos/producto.py`)

Representa un plato, bebida o artículo disponible en el restaurante.

**Atributos:**
- `nombre: str` - Nombre descriptivo del producto
- `descripcion: str` - Descripción detallada
- `precio: float` - Precio en dólares
- `cantidad_disponible: int` - Unidades en stock
- `es_vegetariano: bool` - Indicador de tipo de comida

**Métodos principales:**
- `__init__()` - Constructor
- `__str__()` - Representación en texto
- `mostrar_detalles()` - Imprime detalles del producto
- `actualizar_cantidad(cantidad: int)` - Modifica el stock
- `obtener_disponibilidad()` - Verifica si hay stock

### 2. Clase Cliente (`modelos/cliente.py`)

Representa un cliente registrado en el sistema del restaurante.

**Atributos:**
- `nombre: str` - Nombre completo
- `email: str` - Correo electrónico
- `telefono: str` - Número de contacto
- `edad: int` - Edad del cliente
- `es_miembro_premium: bool` - Tipo de membresía

**Métodos principales:**
- `__init__()` - Constructor
- `__str__()` - Representación en texto
- `mostrar_perfil()` - Imprime perfil del cliente
- `actualizar_email(nuevo_email: str)` - Actualiza email
- `actualizar_telefono(nuevo_telefono: str)` - Actualiza teléfono
- `obtener_estado_membresia()` - Retorna estado actual

### 3. Clase Restaurante (`servicios/restaurante.py`)

Gestiona listas de productos y clientes. Implementa métodos CRUD básicos.

**Atributos:**
- `nombre: str` - Nombre del restaurante
- `lista_productos: List[Producto]` - Lista de productos (tipo compuesto)
- `lista_clientes: List[Cliente]` - Lista de clientes (tipo compuesto)
- `año_fundacion: int` - Año de fundación

**Métodos principales:**
- `__init__()` - Constructor
- `agregar_producto(producto: Producto)` - Agrega producto al menú
- `agregar_cliente(cliente: Cliente)` - Registra un cliente
- `listar_productos()` - Imprime todos los productos
- `listar_clientes()` - Imprime todos los clientes
- `obtener_total_productos()` - Retorna cantidad de productos
- `obtener_total_clientes()` - Retorna cantidad de clientes
- `buscar_producto_por_nombre()` - Búsqueda de producto
- `buscar_cliente_por_nombre()` - Búsqueda de cliente
- `mostrar_resumen()` - Resumen del restaurante

## Convenciones Aplicadas

- **PascalCase**: Nombres de clases (`Producto`, `Cliente`, `Restaurante`)
- **snake_case**: Variables, atributos y métodos (`nombre_cliente`, `lista_productos`, `agregar_producto()`)
- **Anotaciones de tipo**: Especificadas en constructores y métodos
- **Comentarios**: Docstrings y comentarios explicativos

## Tipos de Datos Utilizados

- **str** - Nombre, descripción, email, teléfono
- **int** - Cantidad, edad, año
- **float** - Precio
- **bool** - es_vegetariano, es_miembro_premium
- **List** - lista_productos, lista_clientes

## Cómo Ejecutar

### Desde la carpeta SEMANA 5:

```bash
python main.py
```

### Desde la raíz del proyecto:

```bash
python "PARCIAL1/SEMANA 5/main.py"
```

## Salida Esperada

El programa:
1. Crea una instancia de Restaurante
2. Crea al menos 4 productos y los agrega al menú
3. Crea al menos 4 clientes y los registra
4. Muestra el menú completo con detalles de cada producto
5. Muestra la lista de clientes registrados
6. Demuestra diversos métodos adicionales (búsqueda, actualización, etc.)
7. Imprime un resumen final

## Requisitos Cumplidos

✓ Estructura modular con paquetes  
✓ Constructor `__init__()` en todas las clases  
✓ Método especial `__str__()` para representación de objetos  
✓ Identificadores descriptivos en clases, métodos y variables  
✓ Convenciones de nombres (PascalCase y snake_case)  
✓ Tipos de datos: str, int, float, bool  
✓ Listas como tipo compuesto  
✓ Anotaciones de tipo  
✓ Importaciones correctas entre módulos  
✓ Al menos 2 objetos de cada modelo  
✓ Métodos para gestionar (agregar, listar, buscar) información  
✓ Comentarios explicativos  
✓ Código didáctico y comprensible  

## Autor

Adriana Verónica Arias  
Semana 5 — Programación Orientada a Objetos  
Universidad Estatal Amazónica

