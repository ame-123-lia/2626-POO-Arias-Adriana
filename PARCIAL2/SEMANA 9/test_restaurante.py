from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


def run_tests() -> None:
    r = Restaurante()

    p1 = Producto("P001", "Hamburguesa", "Comida", 5.5)
    p2 = Producto("P002", "Gaseosa", "Bebida", 1.5)
    assert r.registrar_producto(p1) is True
    assert r.registrar_producto(p2) is True
    # Duplicate code
    assert r.registrar_producto(Producto("P001", "Otro", "Comida", 2.0)) is False

    assert r.buscar_producto_por_codigo("P001") is not None
    assert r.actualizar_producto("P001", nombre="Hamburguesa Doble", precio=7.0) is True
    assert r.buscar_producto_por_codigo("P001").precio == 7.0
    assert r.eliminar_producto("P002") is True

    u1 = Usuario("U001", "Ana", "ana@example.com")
    assert r.registrar_usuario(u1) is True
    assert r.registrar_usuario(Usuario("U001", "Ana2", "a2@example.com")) is False

    categorias = r.obtener_categorias_unicas()
    assert isinstance(categorias, set)

    datos = r.exportar_datos_dict()
    assert "productos" in datos and "usuarios" in datos

    print("Pruebas unitarias básicas: OK")


if __name__ == '__main__':
    run_tests()

