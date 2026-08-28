# Restaurante App — Semana 8

**Nombre del estudiante:** [Completa aquí tu nombre]

## Descripción

Proyecto de la Semana 8 que implementa un sistema sencillo para registrar y listar productos (incluyendo bebidas) y clientes de un restaurante. El objetivo es aplicar los principios SOLID (Responsabilidad única, Abierto/Cerrado y Sustitución de Liskov) mediante una arquitectura modular.

**Característica especial:** Al iniciar el programa, se muestra una explicación didáctica de cómo se aplican los principios SOLID en el sistema restaurante.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py        # Clase Producto (base)
│   ├── bebida.py          # Clase Bebida (hereda Producto)
│   └── cliente.py         # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py     # Servicio (administra colecciones)
└── main.py                # Menú interactivo con explicación SOLID
```

## Responsabilidad de cada clase

- **Producto:** representa datos comunes de un producto y define el método `mostrar_informacion()`.
- **Bebida:** hereda de Producto e incluye atributos específicos (tamaño, envase). Sobrescribe `mostrar_informacion()`.
- **Cliente:** representa la información de un cliente y su método `mostrar_informacion()`.
- **Restaurante:** servicio que administra las colecciones de productos y clientes, valida duplicados y expone métodos de registro y listado.

## Relación Producto / Bebida

Bebida es una especialización de Producto. Gracias a la herencia y al polimorfismo, Bebida puede almacenarse en la misma colección que Productos y el servicio puede llamar al método `mostrar_informacion()` sin distinguir el tipo concreto.

## Principios SOLID aplicados

### S — Responsabilidad Única (SRP)
- Cada clase tiene una única responsabilidad concreta.
- Modelos guardan datos, Restaurante administra colecciones, main.py interactúa con el usuario.
- Si necesitas cambiar la lógica de validación, editas un solo lugar.

### O — Abierto/Cerrado (OCP)
- El código está cerrado para modificación: no cambias Restaurante.
- Pero está abierto para extensión: puedes agregar nuevas subclases (ej: Platillo, Postre).
- Bebida extiende Producto sin cambiar el código existente.

### L — Sustitución de Liskov (LSP)
- Bebida puede usarse donde se espera un Producto sin romper el sistema.
- Restaurante itera objetos y llama `mostrar_informacion()` sin pregunta qué tipo es cada uno.
- El polimorfismo funciona: cada objeto responde a su manera.

## Ejecución

### Sistema interactivo (con explicación SOLID al iniciar)

Desde la raíz del proyecto (carpeta SEMANA 8), ejecuta:

```bash
python -m restaurante_app.main
```

Al iniciar, verás:
1. Una explicación didáctica de los principios SOLID aplicados al restaurante.
2. El menú interactivo para registrar productos, bebidas y clientes.
3. Opción 6 en el menú para ver nuevamente la explicación SOLID en cualquier momento.

### Demostración automática de SOLID

Para ver una demostración completa sin interacción del usuario:

```bash
python demo_auto.py
```

Esto muestra:
- Explicación teórica de S, O y L
- Demostración práctica de polimorfismo.
- Validación de códigos únicos.
- Cómo extender el sistema con nuevas clases.

## Menú interactivo

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
----------------------------------------
4. Listar productos
5. Listar clientes
----------------------------------------
6. Ver explicación SOLID
7. Salir
========================================
```

## Características principales

✅ **Responsabilidad Única:** Cada módulo tiene una tarea específica.
✅ **Abierto/Cerrado:** Extensible mediante herencia sin modificar lo existente.
✅ **Sustitución de Liskov:** Polimorfismo sin condicionales `isinstance`.
✅ **Validación:** No permite códigos de producto ni identificaciones de cliente duplicados.
✅ **Interacción:** Menú amigable con emojis y mensajes claros.
✅ **Educativo:** Explicación didáctica integrada en el programa.

## Ejemplo de uso

```
Seleccione una opción: 2

  📝 Ingrese los datos de la bebida:
  Código de la bebida: B001
  Nombre: Coca Cola
  Categoría: Bebida
  Precio: 3.50
  Tamaño (por ejemplo, 500ml): 500ml
  Envase (lata, botella, vaso): Botella
  ✓ Bebida registrada correctamente.

Seleccione una opción: 4

  📋 --- PRODUCTOS REGISTRADOS ---
     Código: B001 | Nombre: Coca Cola | Categoría: Bebida | Precio: $3.50 | Tamaño: 500ml | Envase: Botella
```

## Notas finales

- Completa el campo "Nombre del estudiante" antes de entregar.
- Prueba varias entradas para verificar que no se permiten duplicados.
- Usa la opción 6 del menú para reforzar tu comprensión de SOLID.
- Examina el código fuente para ver cómo aparecen los principios SOLID en acción.

