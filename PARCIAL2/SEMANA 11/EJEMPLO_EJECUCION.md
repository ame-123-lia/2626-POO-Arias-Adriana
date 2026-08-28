# Ejemplo de Ejecución - Restaurante App Semana 11

Este documento muestra cómo sería una ejecución completa del programa con ejemplo de flujo de venta.

## Ejecución 1: Primera Ejecución (Sin datos)

```
$ python main.py

  Cargando datos...

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
Seleccione una opción: 1

  📝 Registrar producto:
  Código del producto: BURGER1
  Nombre: Hamburguesa Clásica
  Categoría: Platos Principales
  Precio: 12.50
  Stock inicial: 20
  ✓ Producto registrado correctamente.

==================================================
      SISTEMA DE RESTAURANTE (Semana 11)
==================================================
...
Seleccione una opción: 1

  📝 Registrar producto:
  Código del producto: PIZZA1
  Nombre: Pizza Grande
  Categoría: Platos Principales
  Precio: 18.99
  Stock inicial: 15
  ✓ Producto registrado correctamente.

==================================================
...
Seleccione una opción: 5

  📋 --- PRODUCTOS REGISTRADOS ---
     Código: BURGER1 | Nombre: Hamburguesa Clásica | Categoría: Platos Principales | Precio: $12.50 | Stock: 20
     Código: PIZZA1 | Nombre: Pizza Grande | Categoría: Platos Principales | Precio: $18.99 | Stock: 15

==================================================
...
Seleccione una opción: 6

  📝 Registrar usuario:
  Identificación: 12345678
  Nombre: Juan Pérez
  Correo: juan.perez@example.com
  ✓ Usuario registrado correctamente.

==================================================
...
Seleccione una opción: 6

  📝 Registrar usuario:
  Identificación: 87654321
  Nombre: María García
  Correo: maria.garcia@example.com
  ✓ Usuario registrado correctamente.

==================================================
...
Seleccione una opción: 7

  📋 --- USUARIOS REGISTRADOS ---
     ID: 12345678 | Nombre: Juan Pérez | Correo: juan.perez@example.com
     ID: 87654321 | Nombre: María García | Correo: maria.garcia@example.com

==================================================
...
Seleccione una opción: 8

  💳 Realizar venta:
  Identificación del usuario: 12345678
  Código del producto: BURGER1
  Producto: Hamburguesa Clásica | Stock disponible: 20
  Cantidad a vender: 3
  ✓ Venta registrada. Nuevo stock: 17

==================================================
...
Seleccione una opción: 8

  💳 Realizar venta:
  Identificación del usuario: 87654321
  Código del producto: PIZZA1
  Producto: Pizza Grande | Stock disponible: 15
  Cantidad a vender: 2
  ✓ Venta registrada. Nuevo stock: 13

==================================================
...
Seleccione una opción: 9

  Identificación del usuario: 12345678

  📋 --- COMPRAS DE JUAN PÉREZ ---
     Usuario: 12345678 | Producto: BURGER1 | Cantidad: 3

==================================================
...
Seleccione una opción: 10

  📋 --- TODAS LAS VENTAS ---
     Usuario: 12345678 | Producto: BURGER1 | Cantidad: 3
     Usuario: 87654321 | Producto: PIZZA1 | Cantidad: 2

==================================================
...
Seleccione una opción: 11

  👋 ¡Hasta luego!

```

### Estado de archivos después de Ejecución 1:

**productos.json:**
```json
[
  {
    "codigo": "BURGER1",
    "nombre": "Hamburguesa Clásica",
    "categoria": "Platos Principales",
    "precio": 12.5,
    "stock": 17
  },
  {
    "codigo": "PIZZA1",
    "nombre": "Pizza Grande",
    "categoria": "Platos Principales",
    "precio": 18.99,
    "stock": 13
  }
]
```

**usuarios.json:**
```json
[
  {
    "identificacion": "12345678",
    "nombre": "Juan Pérez",
    "correo": "juan.perez@example.com"
  },
  {
    "identificacion": "87654321",
    "nombre": "María García",
    "correo": "maria.garcia@example.com"
  }
]
```

**ventas.json:**
```json
[
  {
    "usuario_id": "12345678",
    "producto_codigo": "BURGER1",
    "cantidad": 3
  },
  {
    "usuario_id": "87654321",
    "producto_codigo": "PIZZA1",
    "cantidad": 2
  }
]
```

---

## Ejecución 2: Segunda Ejecución (Con datos recuperados)

```
$ python main.py

  Cargando datos...

==================================================
      SISTEMA DE RESTAURANTE (Semana 11)
==================================================
...
Seleccione una opción: 5

  📋 --- PRODUCTOS REGISTRADOS ---
     Código: BURGER1 | Nombre: Hamburguesa Clásica | Categoría: Platos Principales | Precio: $12.50 | Stock: 17
     Código: PIZZA1 | Nombre: Pizza Grande | Categoría: Platos Principales | Precio: $18.99 | Stock: 13

==================================================
...
Seleccione una opción: 9

  Identificación del usuario: 12345678

  📋 --- COMPRAS DE JUAN PÉREZ ---
     Usuario: 12345678 | Producto: BURGER1 | Cantidad: 3

==================================================
...
Seleccione una opción: 8

  💳 Realizar venta:
  Identificación del usuario: 12345678
  Código del producto: BURGER1
  Producto: Hamburguesa Clásica | Stock disponible: 17
  Cantidad a vender: 20
  ❌ Error: cantidad inválida o stock insuficiente.

==================================================
...
Seleccione una opción: 8

  💳 Realizar venta:
  Identificación del usuario: 12345678
  Código del producto: BURGER1
  Producto: Hamburguesa Clásica | Stock disponible: 17
  Cantidad a vender: 5
  ✓ Venta registrada. Nuevo stock: 12

==================================================
...
Seleccione una opción: 9

  Identificación del usuario: 12345678

  📋 --- COMPRAS DE JUAN PÉREZ ---
     Usuario: 12345678 | Producto: BURGER1 | Cantidad: 3
     Usuario: 12345678 | Producto: BURGER1 | Cantidad: 5

==================================================
...
Seleccione una opción: 11

  👋 ¡Hasta luego!

```

### Observaciones

1. **Stock Recuperado:** Al iniciar la Ejecución 2, el stock de BURGER1 es 17 (no 20)
2. **Historial de Ventas:** Se recuperan las 2 ventas previas de Juan Pérez
3. **Rechazo de Venta:** El sistema rechaza comprar 20 unidades (solo hay 17)
4. **Venta Exitosa:** Se acepta compra de 5 unidades
5. **Persistencia:** Los cambios se guardan en JSON para la próxima ejecución

---

## Pruebas de Validación

### Validación 1: Stock Insuficiente
```
Seleccione una opción: 8

  💳 Realizar venta:
  Identificación del usuario: 12345678
  Código del producto: BURGER1
  Producto: Hamburguesa Clásica | Stock disponible: 17
  Cantidad a vender: 100
  ❌ Error: cantidad inválida o stock insuficiente.
```

### Validación 2: Usuario Inexistente
```
Seleccione una opción: 8

  💳 Realizar venta:
  Identificación del usuario: 99999999
  ❌ Usuario no encontrado.
```

### Validación 3: Producto Inexistente
```
Seleccione una opción: 8

  💳 Realizar venta:
  Identificación del usuario: 12345678
  Código del producto: INEXISTENTE
  ❌ Producto no encontrado.
```

### Validación 4: Usuario sin Compras
```
Seleccione una opción: 9

  Identificación del usuario: 87654321

  ℹ️  El usuario no ha realizado compras.
```

---

Este ejemplo demuestra que el sistema funciona correctamente con:
- ✓ Gestión de productos con stock
- ✓ Gestión de usuarios
- ✓ Operación de venta con validaciones
- ✓ Consulta de ventas por usuario
- ✓ Persistencia en JSON
- ✓ Recuperación de datos
- ✓ Control de errores y validaciones
