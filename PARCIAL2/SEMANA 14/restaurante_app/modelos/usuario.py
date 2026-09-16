class Usuario:
    def __init__(self, id, nombre, usuario, contraseña, rol="cliente"):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol = rol
    
    def __str__(self):
        return f"{self.nombre} ({self.usuario}) - {self.rol}"
    
    def __repr__(self):
        return f"Usuario({self.id}, {self.nombre}, {self.usuario}, {self.rol})"
