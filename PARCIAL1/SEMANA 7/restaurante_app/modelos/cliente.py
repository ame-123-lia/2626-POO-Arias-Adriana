from dataclasses import dataclass

@dataclass
class Cliente:
    """
    Clase Cliente usando @dataclass.

    Demuestra:
    - ABSTRACCIÓN: Dataclass genera automáticamente __init__, __repr__, __eq__
    - VALIDACIÓN: Usa __post_init__ para validar después de la inicialización
    - DICCIONARIO DE DATOS: Encapsula datos relacionados a un cliente

    Nota: @dataclass es syntactic sugar que simplifica la creación de clases
    que principalmente almacenan datos.
    """
    nombre: str
    correo: str
    id_cliente: str

    def __post_init__(self):
        """
        Validación después de la inicialización.
        En un dataclass, este método se llama automáticamente después de __init__.
        """
        self.nombre = self.nombre.strip()
        self.correo = self.correo.strip()
        self.id_cliente = str(self.id_cliente).strip()

        if not self.nombre:
            raise ValueError("❌ El nombre del cliente no puede estar vacío.")
        if not self.correo:
            raise ValueError("❌ El correo del cliente no puede estar vacío.")
        if not self.id_cliente:
            raise ValueError("❌ El identificador del cliente no puede estar vacío.")

        print(f"✓ Cliente '{self.nombre}' creado exitosamente")

    def mostrar_informacion(self) -> str:
        """Devuelve una representación legible del cliente."""
        return (
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"ID: {self.id_cliente}"
        )

    def info_pedagogica(self) -> str:
        """
        Información educativa sobre los principios de POO aplicados.
        Muestra cómo @dataclass simplifica la POO.
        """
        return (
            f"\n📚 LECCIÓN DE POO APLICADA EN '{self.nombre}':\n"
            f"  • Clase: {self.__class__.__name__}\n"
            f"  • Tipo: Dataclass (simplifica definición de clases de datos)\n"
            f"  • Métodos automáticos: __init__, __repr__, __eq__, __hash__\n"
            f"  • Validación: Implementada en __post_init__\n"
            f"  • Beneficio: Código limpio y mantenible para clases de datos"
        )

