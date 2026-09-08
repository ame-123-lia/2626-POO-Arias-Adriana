class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.productos = []
        self.usuario_actual = None
        self._cargar_datos()
    
    def _cargar_datos(self):
        """Carga todos los datos necesarios"""
        self.usuarios = self.archivo_servicio.cargar_usuarios()
        self.productos = self.archivo_servicio.cargar_productos()
    
    def validar_acceso(self, usuario, contraseña):
        """Valida el acceso del usuario"""
        for u in self.usuarios:
            if u.usuario == usuario and u.contraseña == contraseña:
                self.usuario_actual = u
                return True, f"Bienvenido, {u.nombre}"
        return False, "Usuario o contraseña incorrectos"
    
    def cerrar_sesion(self):
        """Cierra la sesión del usuario actual"""
        self.usuario_actual = None
    
    def obtener_productos(self):
        """Retorna la lista de productos"""
        return self.productos
    
    def obtener_usuarios(self):
        """Retorna la lista de usuarios"""
        return self.usuarios
    
    def obtener_cantidad_producto(self, producto_id):
        """Obtiene la cantidad disponible de un producto"""
        for p in self.productos:
            if p.id == producto_id:
                return p.cantidad
        return 0
    
    def obtener_usuario_actual(self):
        """Retorna el usuario actualmente autenticado"""
        return self.usuario_actual
