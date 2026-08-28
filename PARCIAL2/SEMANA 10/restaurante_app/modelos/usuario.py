from typing import Dict


class Usuario:
    """Representa de forma genérica a una persona registrada en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = str(identificacion).strip()
        self.nombre: str = str(nombre).strip()
        self.correo: str = str(correo).strip()

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

    def to_dict(self) -> Dict[str, str]:
        return {"identificacion": self.identificacion, "nombre": self.nombre, "correo": self.correo}

