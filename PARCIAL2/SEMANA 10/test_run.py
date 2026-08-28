import importlib.util
from pathlib import Path

base = Path(__file__).resolve().parent / 'restaurante_app'
archivo_servicio_path = base / 'servicios' / 'archivo_servicio.py'
producto_path = base / 'modelos' / 'producto.py'

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

mod_arch = load_module('archivo_servicio', archivo_servicio_path)
mod_prod = load_module('producto', producto_path)

ArchivoServicio = mod_arch.ArchivoServicio
Producto = mod_prod.Producto

ruta = str(base / 'datos' / 'productos.json')
serv = ArchivoServicio(ruta)
print('Cargando inicialmente:', serv.cargar_productos())
p = Producto('P1','Pan','Abarrotes',12.5)
serv.guardar_productos([p.to_dict()])
print('Guardado. Contenido ahora:', serv.cargar_productos())
serv.guardar_productos([])
print('Restaurado a vacio:', serv.cargar_productos())

