Proyecto: restaurante_app - Semana 10

Descripción breve
------------------
Este proyecto es una evolución del restaurante_app trabajado en semanas anteriores. En la
Semana 10 se incorporó persistencia de productos en formato JSON, manejo de excepciones
relacionadas con archivos y la reconstrucción de objetos Producto al iniciar la aplicación.

Estructura del proyecto (relevante)
----------------------------------
restaurante_app/
├── datos/
│   └── productos.json     # archivo de persistencia
├── modelos/
│   ├── __init__.py
│   ├── producto.py        # clase Producto con to_dict y from_dict
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py  # lectura/escritura JSON con control de excepciones
│   └── restaurante.py       # lógica de negocio y helpers para exportar
├── main.py                # punto de entrada: carga y guardado al modificar

Funcionamiento principal
------------------------
- Al iniciar, `main.py` crea un `ArchivoServicio` apuntando a `datos/productos.json` y
  solicita la carga de registros con `cargar_productos()`.
- Cada registro recuperado se valida y se reconstruye mediante `Producto.from_dict()`;
  los registros inválidos (faltantes o con datos erróneos) se omiten y se informa al usuario.
- Las operaciones de registrar, actualizar y eliminar productos actualizan la colección en memoria
  y luego se solicita a `ArchivoServicio.guardar_productos(...)` que escriba el JSON actualizado.

Excepciones controladas
-----------------------
- FileNotFoundError: si `productos.json` no existe, la aplicación inicia con lista vacía.
- json.JSONDecodeError: si el archivo existe pero no contiene JSON válido, se informa y se ignoran los datos.
- PermissionError: si no hay permisos para crear/cargar/escribir el archivo, se informa al usuario.
- KeyError / ValueError: al reconstruir objetos desde registros defectuosos, se omiten sin detener la ejecución.

Prueba mínima (persistencia)
---------------------------
1. Ejecutar `main.py`.
2. Registrar uno o más productos desde el menú.
3. Verificar que `datos/productos.json` contenga los productos (como lista de dicts).
4. Cerrar la aplicación.
5. Ejecutar nuevamente `main.py` y listar productos; las entradas guardadas deben aparecer.

