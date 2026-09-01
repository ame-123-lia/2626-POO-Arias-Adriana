class Usuario:
    """
    Clase que representa un usuario (cliente) del restaurante.
    
    Atributos:
        identificacion: str - identificador único del usuario
        nombre: str - nombre completo del usuario
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

    def __str__(self) -> str:
        """Representación en string del usuario."""
        return self.mostrar_informacion()

    def __repr__(self) -> str:
        """Representación técnica del usuario."""
        return f"Usuario({self.identificacion!r}, {self.nombre!r}, {self.correo!r})"
