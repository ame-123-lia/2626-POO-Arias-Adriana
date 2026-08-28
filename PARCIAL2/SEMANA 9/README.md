# Restaurante App - Semana 9

Alumno: [Nombre Completo]  <!-- Reemplace por su nombre -->

Descripción
-----------
Pequeña aplicación de consola que administra productos y usuarios de un restaurante.
El objetivo de la semana es integrar estructuras de datos de Python (list, tuple, dict, set)
en la solución, manteniendo una estructura modular (modelos/, servicios/, main.py).

Estructura del proyecto
-----------------------
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py

Dónde se usan las estructuras de datos
-------------------------------------
- list: Se utilizan listas en `Restaurante` para almacenar dinámicamente los objetos `Producto` y `Usuario` (`self._productos`, `self._usuarios`).
- tuple: `MENU_OPCIONES` en `main.py` es una tupla que define las opciones del menú y se mantiene estable durante la ejecución.
- dict: Se usa un diccionario en `main.py` para mapear opciones del menú a funciones (clave→valor). Además, `Restaurante.exportar_datos_dict()` devuelve un diccionario con los datos actuales (productos y usuarios) en forma clave→valor.
- set: `Restaurante.obtener_categorias_unicas()` devuelve un conjunto con las categorías únicas de los productos, eliminando duplicados.

Ejecución
---------
Desde la carpeta `PARCIAL2/SEMANA 9` ejecute:

```powershell
python -m restaurante_app.main
```

Notas
-----
- No se implementó persistencia en archivos ni base de datos (requisito de la actividad).
- Sustituya `[Nombre Completo]` por su nombre antes de entregar.

Reflexión breve
---------------
Elegir la estructura de datos adecuada facilita mantener invarianzas y optimizar operaciones.
Por ejemplo, listas permiten almacenar colecciones ordenadas y dinámicas, sets facilitan obtener
valores únicos sin duplicados y diccionarios son útiles cuando se necesita acceder por claves.

