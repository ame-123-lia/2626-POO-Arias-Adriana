from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str

    def __post_init__(self):
        self.nombre = self.nombre.strip()
        self.correo = self.correo.strip()
        self.id_cliente = str(self.id_cliente).strip()
        if not self.nombre:
            raise ValueError("El nombre del cliente no puede estar vacío.")
        if not self.correo:
            raise ValueError("El correo del cliente no puede estar vacío.")
        if not self.id_cliente:
            raise ValueError("El identificador del cliente no puede estar vacío.")
