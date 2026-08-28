"""
Punto de entrada del sistema restaurante_app.
Desde aquí se crean objetos Platillo y Bebida, se registran en Restaurante y se imprime la lista.
"""
"""Punto de entrada del paquete restaurante_app.

Soporta ejecución como módulo (python -m restaurante_app.main) y como script
directo (python main.py) ajustando las importaciones cuando sea necesario.
"""
try:
    # Importaciones cuando se ejecuta como paquete
    from .modelos.platillo import Platillo
    from .modelos.bebida import Bebida
    from .servicios.restaurante import Restaurante
except Exception:
    # Fallback cuando se ejecuta directamente como script (sin parent package)
    import sys
    import os

    # Añadir la carpeta del paquete al path para poder importar los módulos internos
    package_dir = os.path.dirname(os.path.abspath(__file__))
    if package_dir not in sys.path:
        sys.path.insert(0, package_dir)

    from modelos.platillo import Platillo
    from modelos.bebida import Bebida
    from servicios.restaurante import Restaurante


def main():
    restaurante = Restaurante("Mi Restaurante POO")

    # Crear al menos dos platillos
    platillo1 = Platillo("Lomo Saltado", 25.50, calorias=800, tiempo_preparacion=20)
    platillo2 = Platillo("Ceviche", 22.00, calorias=400, tiempo_preparacion=15)

    # Crear al menos dos bebidas
    bebida1 = Bebida("Inca Kola", 4.50, volumen_ml=500, tipo="Gaseosa")
    bebida2 = Bebida("Limonada", 3.00, volumen_ml=350, tipo="Natural")

    # Agregar productos al servicio Restaurante
    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    # Mostrar la información (polimorfismo en acción)
    restaurante.listar_productos()


if __name__ == "__main__":
    main()

