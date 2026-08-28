class Usuario:
    """
    Clase que representa un usuario (cliente) del restaurante.
    
    Atributos:
        identificacion: str - identificador único del usuario
        nombre: str - nombre completo
        correo: str - dirección de correo electrónico
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        """
        Inicializa un usuario.
        
        Args:
            identificacion: identificador único
            nombre: nombre completo del usuario
            correo: dirección de correo
        """
        self.identificacion: str = str(identificacion).strip()
        self.nombre: str = str(nombre).strip()
        self.correo: str = str(correo).strip()

    def mostrar_informacion(self) -> str:
        """Retorna una representación legible del usuario."""
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"
