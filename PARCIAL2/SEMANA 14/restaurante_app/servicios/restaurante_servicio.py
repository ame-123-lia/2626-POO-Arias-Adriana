from modelos import Producto, Usuario


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
    
    def registrar_producto(self, nombre, precio, cantidad, descripcion=""):
        """
        Registra un nuevo producto.
        Retorna tupla (exito: bool, producto: Producto o mensaje: str)
        """
        try:
            # Validar datos
            if not nombre or not nombre.strip():
                return False, "El nombre del producto no puede estar vacío"
            
            try:
                precio = float(precio)
                if precio < 0:
                    return False, "El precio no puede ser negativo"
            except (ValueError, TypeError):
                return False, "El precio debe ser un número válido"
            
            try:
                cantidad = int(cantidad)
                if cantidad < 0:
                    return False, "La cantidad no puede ser negativa"
            except (ValueError, TypeError):
                return False, "La cantidad debe ser un número entero válido"
            
            # Generar ID único (P001, P002, etc.)
            max_id = 0
            for p in self.productos:
                try:
                    num = int(p.id[1:])
                    max_id = max(max_id, num)
                except:
                    pass
            nuevo_id = f"P{str(max_id + 1).zfill(3)}"
            
            # Crear y agregar producto
            nuevo_producto = Producto(
                id=nuevo_id,
                nombre=nombre.strip(),
                precio=precio,
                cantidad=cantidad,
                descripcion=descripcion.strip()
            )
            self.productos.append(nuevo_producto)
            
            # Guardar en JSON
            self.archivo_servicio.guardar_productos(self.productos)
            
            return True, nuevo_producto
        except Exception as e:
            return False, f"Error al registrar producto: {str(e)}"
    
    def cargar_producto_por_id(self, producto_id):
        """
        Carga un producto por su ID.
        Retorna tupla (exito: bool, producto: Producto o mensaje: str)
        """
        for p in self.productos:
            if p.id == producto_id.strip():
                return True, p
        return False, "Producto no encontrado"
    
    def actualizar_producto(self, producto_id, nombre, precio, cantidad, descripcion=""):
        """
        Actualiza un producto existente.
        Retorna tupla (exito: bool, producto: Producto o mensaje: str)
        """
        try:
            # Validar datos
            if not nombre or not nombre.strip():
                return False, "El nombre del producto no puede estar vacío"
            
            try:
                precio = float(precio)
                if precio < 0:
                    return False, "El precio no puede ser negativo"
            except (ValueError, TypeError):
                return False, "El precio debe ser un número válido"
            
            try:
                cantidad = int(cantidad)
                if cantidad < 0:
                    return False, "La cantidad no puede ser negativa"
            except (ValueError, TypeError):
                return False, "La cantidad debe ser un número entero válido"
            
            # Buscar y actualizar producto
            for i, p in enumerate(self.productos):
                if p.id == producto_id.strip():
                    self.productos[i].nombre = nombre.strip()
                    self.productos[i].precio = precio
                    self.productos[i].cantidad = cantidad
                    self.productos[i].descripcion = descripcion.strip()
                    
                    # Guardar en JSON
                    self.archivo_servicio.guardar_productos(self.productos)
                    
                    return True, self.productos[i]
            
            return False, "Producto no encontrado"
        except Exception as e:
            return False, f"Error al actualizar producto: {str(e)}"
    
    def eliminar_producto(self, producto_id):
        """
        Elimina un producto por su ID.
        Retorna tupla (exito: bool, mensaje: str)
        """
        try:
            for i, p in enumerate(self.productos):
                if p.id == producto_id.strip():
                    self.productos.pop(i)
                    
                    # Guardar en JSON
                    self.archivo_servicio.guardar_productos(self.productos)
                    
                    return True, f"Producto {producto_id} eliminado"
            
            return False, "Producto no encontrado"
        except Exception as e:
            return False, f"Error al eliminar producto: {str(e)}"
    
    def recargar_productos(self):
        """Recarga la lista de productos desde el archivo"""
        self.productos = self.archivo_servicio.cargar_productos()
        return len(self.productos) > 0
    
    # ===== MÉTODOS CRUD PARA USUARIOS =====
    
    def registrar_usuario(self, nombre, usuario, contraseña, rol="cliente"):
        """
        Registra un nuevo usuario.
        Retorna tupla (exito: bool, usuario: Usuario o mensaje: str)
        """
        try:
            # Validar datos
            if not nombre or not nombre.strip():
                return False, "El nombre del usuario no puede estar vacío"
            
            if not usuario or not usuario.strip():
                return False, "El nombre de usuario no puede estar vacío"
            
            if not contraseña or not contraseña.strip():
                return False, "La contraseña no puede estar vacía"
            
            if not rol or not rol.strip():
                return False, "El rol no puede estar vacío"
            
            # Validar que el usuario no exista
            for u in self.usuarios:
                if u.usuario == usuario.strip():
                    return False, "El usuario ya existe"
            
            # Generar ID único (U001, U002, etc.)
            max_id = 0
            for u in self.usuarios:
                try:
                    num = int(u.id[1:])
                    max_id = max(max_id, num)
                except:
                    pass
            nuevo_id = f"U{str(max_id + 1).zfill(3)}"
            
            # Crear y agregar usuario
            nuevo_usuario = Usuario(
                id=nuevo_id,
                nombre=nombre.strip(),
                usuario=usuario.strip(),
                contraseña=contraseña.strip(),
                rol=rol.strip()
            )
            self.usuarios.append(nuevo_usuario)
            
            # Guardar en JSON
            self.archivo_servicio.guardar_usuarios(self.usuarios)
            
            return True, nuevo_usuario
        except Exception as e:
            return False, f"Error al registrar usuario: {str(e)}"
    
    def cargar_usuario_por_id(self, usuario_id):
        """
        Carga un usuario por su ID.
        Retorna tupla (exito: bool, usuario: Usuario o mensaje: str)
        """
        for u in self.usuarios:
            if u.id == usuario_id.strip():
                return True, u
        return False, "Usuario no encontrado"
    
    def actualizar_usuario(self, usuario_id, nombre, usuario, contraseña, rol="cliente"):
        """
        Actualiza un usuario existente.
        Retorna tupla (exito: bool, usuario: Usuario o mensaje: str)
        """
        try:
            # Validar datos
            if not nombre or not nombre.strip():
                return False, "El nombre del usuario no puede estar vacío"
            
            if not usuario or not usuario.strip():
                return False, "El nombre de usuario no puede estar vacío"
            
            if not contraseña or not contraseña.strip():
                return False, "La contraseña no puede estar vacía"
            
            if not rol or not rol.strip():
                return False, "El rol no puede estar vacío"
            
            # Validar que el nuevo usuario no exista (si cambió)
            for u in self.usuarios:
                if u.id != usuario_id.strip() and u.usuario == usuario.strip():
                    return False, "El usuario ya existe"
            
            # Buscar y actualizar usuario
            for i, u in enumerate(self.usuarios):
                if u.id == usuario_id.strip():
                    self.usuarios[i].nombre = nombre.strip()
                    self.usuarios[i].usuario = usuario.strip()
                    self.usuarios[i].contraseña = contraseña.strip()
                    self.usuarios[i].rol = rol.strip()
                    
                    # Guardar en JSON
                    self.archivo_servicio.guardar_usuarios(self.usuarios)
                    
                    return True, self.usuarios[i]
            
            return False, "Usuario no encontrado"
        except Exception as e:
            return False, f"Error al actualizar usuario: {str(e)}"
    
    def eliminar_usuario(self, usuario_id):
        """
        Elimina un usuario por su ID.
        Retorna tupla (exito: bool, mensaje: str)
        """
        try:
            for i, u in enumerate(self.usuarios):
                if u.id == usuario_id.strip():
                    self.usuarios.pop(i)
                    
                    # Guardar en JSON
                    self.archivo_servicio.guardar_usuarios(self.usuarios)
                    
                    return True, f"Usuario {usuario_id} eliminado"
            
            return False, "Usuario no encontrado"
        except Exception as e:
            return False, f"Error al eliminar usuario: {str(e)}"
    
    def recargar_usuarios(self):
        """Recarga la lista de usuarios desde el archivo"""
        self.usuarios = self.archivo_servicio.cargar_usuarios()
        return len(self.usuarios) > 0
