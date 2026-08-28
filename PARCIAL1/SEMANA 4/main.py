# Importamos las clases desde sus respectivos módulos y carpetas
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def ejecutar_sistema():
    # 1. Crear la instancia del restaurante
    mi_restaurante = Restaurante("Sabor Amazónico")

    print("--- Cargando Menú del Restaurante ---")
    # 2. Crear objetos de la clase Producto
    plato1 = Producto("Maito de Pescado", 8.50, "Plato Fuerte")
    plato2 = Producto("Chicha de Chonta", 2.00, "Bebida")
    plato3 = Producto("Volquetero Amazónico", 6.00, "Plato Fuerte")

    # Agregar los productos al restaurante
    mi_restaurante.agregar_producto(plato1)
    mi_restaurante.agregar_producto(plato2)
    mi_restaurante.agregar_producto(plato3)

    print("\n--- Registrando Clientes ---")
    # 3. Crear objetos de la clase Cliente
    cliente1 = Cliente("María Torres", "0201548796", 4)
    cliente2 = Cliente("Carlos Mendoza", "1723456789", 2)

    # Registrar los clientes
    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)

    # 4. Mostrar el reporte final en consola
    mi_restaurante.mostrar_informacion_general()


if __name__ == "__main__":
    ejecutar_sistema()