# Restaurante App - Semana 6

- Nombre: [Tu Nombre Aquí]

Descripción
-----------
Proyecto didáctico que demuestra conceptos de Programación Orientada a Objetos en Python
aplicados a un sistema simple de restaurante. Se implementan herencia, encapsulación y polimorfismo.

Estructura del proyecto
-----------------------
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase padre Producto con atributo encapsulado __precio
│   ├── platillo.py      # Clase Platillo (hereda Producto)
│   └── bebida.py        # Clase Bebida (hereda Producto)
├── servicios/
│   ├── __init__.py
│   └── restaurante.py   # Clase Restaurante que administra productos
└── main.py              # Punto de arranque

Herencia aplicada
------------------
La clase `Producto` actúa como clase padre con atributos comunes (nombre, precio, disponible).
`Platillo` y `Bebida` heredan de `Producto` y añaden atributos propios (calorías, tiempo de
preparación; volumen, tipo respectivamente).

Encapsulación
-------------
El atributo `__precio` en `Producto` está protegido (nombre con doble guión bajo). Se
accede y modifica mediante los métodos `obtener_precio()` y `cambiar_precio()` que validan
los datos (precio > 0).

Polimorfismo
------------
Cada subclase sobrescribe `mostrar_informacion()` para devolver una representación propia.
Al recorrer la lista de productos en `Restaurante.listar_productos()` se invoca el mismo
método en distintos objetos, demostrando polimorfismo.

Ejecución
---------
Ejecutar desde la carpeta `SEMANA 6`:

```powershell
python -m restaurante_app.main
```

Reflexión
---------
Organizar el código en módulos y aplicar principios de POO (herencia, encapsulación y
polimorfismo) facilita la ampliación y el mantenimiento del sistema. Separar modelos y
servicios mejora la legibilidad y permite reutilizar clases en otros contextos.

