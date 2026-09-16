import tkinter as tk
from tkinter import ttk, messagebox


class MainView:
    def __init__(self, root, restaurante_servicio, callback_logout):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.callback_logout = callback_logout
        
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Variables para el formulario de productos
        self.var_id = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_cantidad = tk.StringVar()
        self.var_descripcion = tk.StringVar()
        
        # Variables para el formulario de usuarios
        self.var_id_usuario = tk.StringVar()
        self.var_nombre_usuario = tk.StringVar()
        self.var_usuario_usuario = tk.StringVar()
        self.var_contrasena = tk.StringVar()
        self.var_rol = tk.StringVar()
        
        # Variables de estado
        self.producto_seleccionado = None
        self.usuario_seleccionado = None
        
        self._crear_widgets()
    
    def _crear_widgets(self):
        """Crea los widgets de la interfaz principal"""
        # Encabezado con usuario y botón logout
        header_frame = tk.Frame(self.frame, bg="#2c3e50")
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        usuario_actual = self.restaurante_servicio.obtener_usuario_actual()
        titulo = tk.Label(
            header_frame,
            text=f"Bienvenido, {usuario_actual.nombre}",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#2c3e50"
        )
        titulo.pack(side=tk.LEFT, padx=20, pady=15)
        
        btn_logout = tk.Button(
            header_frame,
            text="Cerrar Sesión",
            font=("Arial", 10, "bold"),
            bg="#c0392b",
            fg="white",
            padx=15,
            pady=8,
            command=self.callback_logout
        )
        btn_logout.pack(side=tk.RIGHT, padx=20, pady=15)
        
        # Frame para opciones/tabs
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab de Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Productos")
        self._crear_tab_productos()
        
        # Tab de Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text="Usuarios")
        self._crear_tab_usuarios()
        
        # Tab de Ventas (pendiente)
        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text="Ventas")
        self._crear_tab_ventas()
    
    def _crear_tab_productos(self):
        """Crea el contenido de la tab de productos con diseño DOBLE PANEL"""
        # Container principal
        container = tk.Frame(self.tab_productos)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        container.columnconfigure(0, weight=1)  # Panel izquierdo
        container.columnconfigure(1, weight=2)  # Panel derecho (más grande)
        
        # ═══════════════════════════════════════════════════════════════════════
        # PANEL IZQUIERDO: LISTA DE PRODUCTOS
        # ═══════════════════════════════════════════════════════════════════════
        panel_izq = ttk.LabelFrame(container, text="Productos", padding=5)
        panel_izq.grid(row=0, column=0, sticky=tk.NSEW, padx=(0, 5))
        panel_izq.columnconfigure(0, weight=1)
        panel_izq.rowconfigure(1, weight=1)
        
        # Botón para nuevo producto
        btn_nuevo = tk.Button(
            panel_izq,
            text="+ Nuevo Producto",
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            padx=10,
            pady=8,
            command=self._nuevo_producto
        )
        btn_nuevo.grid(row=0, column=0, sticky=tk.EW, padx=5, pady=5)
        
        # Frame para la lista con scrollbar
        frame_lista = tk.Frame(panel_izq)
        frame_lista.grid(row=1, column=0, sticky=tk.NSEW)
        frame_lista.columnconfigure(0, weight=1)
        frame_lista.rowconfigure(0, weight=1)
        
        # Scrollbar para la lista
        scrollbar_izq = ttk.Scrollbar(frame_lista)
        scrollbar_izq.grid(row=0, column=1, sticky=tk.NS)
        
        # Listbox con productos
        self.listbox_productos = tk.Listbox(
            frame_lista,
            font=("Arial", 10),
            bg="white",
            fg="#2c3e50",
            yscrollcommand=scrollbar_izq.set,
            activestyle='none'
        )
        self.listbox_productos.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar_izq.config(command=self.listbox_productos.yview)
        
        # Bind para seleccionar producto
        self.listbox_productos.bind('<<ListboxSelect>>', self._on_select_producto)
        
        # ═══════════════════════════════════════════════════════════════════════
        # PANEL DERECHO: FORMULARIO CRUD
        # ═══════════════════════════════════════════════════════════════════════
        panel_der = ttk.LabelFrame(container, text="Detalles del Producto", padding=10)
        panel_der.grid(row=0, column=1, sticky=tk.NSEW)
        panel_der.columnconfigure(1, weight=1)
        
        # ID (solo lectura)
        tk.Label(panel_der, text="ID:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        entry_id = tk.Entry(panel_der, textvariable=self.var_id, font=("Arial", 10), state=tk.DISABLED, width=30)
        entry_id.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Nombre
        tk.Label(panel_der, text="Nombre:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_nombre = tk.Entry(panel_der, textvariable=self.var_nombre, font=("Arial", 10), width=30)
        self.entry_nombre.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Precio
        tk.Label(panel_der, text="Precio ($):", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_precio = tk.Entry(panel_der, textvariable=self.var_precio, font=("Arial", 10), width=30)
        self.entry_precio.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Cantidad
        tk.Label(panel_der, text="Cantidad:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_cantidad = tk.Entry(panel_der, textvariable=self.var_cantidad, font=("Arial", 10), width=30)
        self.entry_cantidad.grid(row=3, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Descripción
        tk.Label(panel_der, text="Descripción:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky=tk.NW, padx=5, pady=5)
        self.text_descripcion = tk.Text(panel_der, font=("Arial", 10), width=30, height=4)
        self.text_descripcion.grid(row=4, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Separador
        ttk.Separator(panel_der, orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky=tk.EW, pady=10)
        
        # Botones de acción
        frame_botones = tk.Frame(panel_der)
        frame_botones.grid(row=6, column=0, columnspan=2, sticky=tk.EW, padx=5, pady=5)
        frame_botones.columnconfigure([0, 1, 2], weight=1)
        
        btn_guardar = tk.Button(
            frame_botones,
            text="Guardar",
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            padx=10,
            pady=8,
            command=self._guardar_producto
        )
        btn_guardar.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)
        
        btn_actualizar = tk.Button(
            frame_botones,
            text="Actualizar",
            font=("Arial", 10, "bold"),
            bg="#f39c12",
            fg="white",
            padx=10,
            pady=8,
            command=self._actualizar_producto
        )
        btn_actualizar.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            font=("Arial", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=10,
            pady=8,
            command=self._eliminar_producto
        )
        btn_eliminar.grid(row=0, column=2, padx=5, pady=5, sticky=tk.EW)
        
        # Botón limpiar
        btn_limpiar = tk.Button(
            panel_der,
            text="Limpiar Formulario",
            font=("Arial", 9),
            bg="#95a5a6",
            fg="white",
            padx=10,
            pady=6,
            command=self._limpiar_formulario
        )
        btn_limpiar.grid(row=7, column=0, columnspan=2, sticky=tk.EW, padx=5, pady=5)
        
        # Cargar productos iniciales
        self._actualizar_listbox_productos()

    
    def _crear_tab_usuarios(self):
        """Crea el contenido de la tab de usuarios con diseño DOBLE PANEL"""
        # Container principal con dos paneles
        container = tk.Frame(self.tab_usuarios)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ===== PANEL IZQUIERDO: LISTA DE USUARIOS =====
        frame_lista = tk.LabelFrame(container, text="Usuarios", font=("Arial", 11, "bold"), padx=10, pady=10)
        frame_lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Botón para nuevo usuario
        btn_nuevo_usuario = tk.Button(
            frame_lista,
            text="+ Nuevo Usuario",
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            padx=10,
            pady=8,
            command=self._nuevo_usuario
        )
        btn_nuevo_usuario.pack(fill=tk.X, padx=0, pady=(0, 10))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        self.listbox_usuarios = tk.Listbox(
            frame_lista,
            font=("Arial", 10),
            yscrollcommand=scrollbar.set,
            height=15,
            width=30
        )
        self.listbox_usuarios.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox_usuarios.bind("<<ListboxSelect>>", self._on_select_usuario)
        scrollbar.config(command=self.listbox_usuarios.yview)
        
        # ===== PANEL DERECHO: FORMULARIO DE USUARIOS =====
        frame_form = tk.LabelFrame(container, text="Detalles del Usuario", font=("Arial", 11, "bold"), padx=10, pady=10)
        frame_form.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # ID (solo lectura)
        tk.Label(frame_form, text="ID:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W, padx=5, pady=8)
        self.entry_id_usuario = tk.Entry(frame_form, textvariable=self.var_id_usuario, state=tk.DISABLED, font=("Arial", 10))
        self.entry_id_usuario.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=8)
        
        # Nombre
        tk.Label(frame_form, text="Nombre:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky=tk.W, padx=5, pady=8)
        self.entry_nombre_usuario = tk.Entry(frame_form, textvariable=self.var_nombre_usuario, font=("Arial", 10))
        self.entry_nombre_usuario.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=8)
        
        # Usuario
        tk.Label(frame_form, text="Usuario:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=tk.W, padx=5, pady=8)
        self.entry_usuario_usuario = tk.Entry(frame_form, textvariable=self.var_usuario_usuario, font=("Arial", 10))
        self.entry_usuario_usuario.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=8)
        
        # Contraseña
        tk.Label(frame_form, text="Contraseña:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky=tk.W, padx=5, pady=8)
        self.entry_contrasena = tk.Entry(frame_form, textvariable=self.var_contrasena, font=("Arial", 10), show="*")
        self.entry_contrasena.grid(row=3, column=1, sticky=tk.EW, padx=5, pady=8)
        
        # Rol
        tk.Label(frame_form, text="Rol:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky=tk.W, padx=5, pady=8)
        self.combo_rol = ttk.Combobox(
            frame_form,
            textvariable=self.var_rol,
            values=["administrador", "gerente", "cajero", "chef", "mesero", "cliente"],
            font=("Arial", 10),
            state="readonly"
        )
        self.combo_rol.grid(row=4, column=1, sticky=tk.EW, padx=5, pady=8)
        
        # Botones de acción
        frame_botones = tk.Frame(frame_form)
        frame_botones.grid(row=5, column=0, columnspan=2, sticky=tk.EW, padx=5, pady=15)
        
        btn_guardar = tk.Button(
            frame_botones,
            text="Guardar",
            font=("Arial", 10, "bold"),
            bg="#3498db",
            fg="white",
            padx=10,
            pady=6,
            command=self._guardar_usuario
        )
        btn_guardar.pack(side=tk.LEFT, padx=5)
        
        btn_actualizar = tk.Button(
            frame_botones,
            text="Actualizar",
            font=("Arial", 10, "bold"),
            bg="#f39c12",
            fg="white",
            padx=10,
            pady=6,
            command=self._actualizar_usuario
        )
        btn_actualizar.pack(side=tk.LEFT, padx=5)
        
        btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            font=("Arial", 10, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=10,
            pady=6,
            command=self._eliminar_usuario
        )
        btn_eliminar.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            font=("Arial", 10, "bold"),
            bg="#95a5a6",
            fg="white",
            padx=10,
            pady=6,
            command=self._limpiar_formulario_usuarios
        )
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        # Configurar peso de las columnas
        frame_form.columnconfigure(1, weight=1)
        
        # Cargar usuarios iniciales
        self._actualizar_listbox_usuarios()
    
    def _crear_tab_ventas(self):
        """Crea el contenido de la tab de ventas (pendiente)"""
        mensaje = tk.Label(
            self.tab_ventas,
            text="Funcionalidad de Ventas",
            font=("Arial", 14, "bold"),
            fg="#2c3e50"
        )
        mensaje.pack(pady=20)
        
        pendiente = tk.Label(
            self.tab_ventas,
            text="Esta funcionalidad está en desarrollo\ny será implementada en futuras versiones.",
            font=("Arial", 11),
            fg="#7f8c8d",
            justify=tk.CENTER
        )
        pendiente.pack(pady=10)
    
    def _nuevo_producto(self):
        """Prepara el formulario para crear un nuevo producto"""
        self._limpiar_formulario()
        self.entry_nombre.focus()
    
    def _on_select_producto(self, event):
        """Se ejecuta cuando se selecciona un producto en la lista"""
        seleccion = self.listbox_productos.curselection()
        if not seleccion:
            return
        
        indice = seleccion[0]
        productos = self.restaurante_servicio.obtener_productos()
        
        if indice < len(productos):
            producto = productos[indice]
            self.producto_seleccionado = producto
            self._cargar_producto_en_formulario(producto)
    
    def _cargar_producto_en_formulario(self, producto):
        """Carga los datos de un producto en el formulario"""
        self.var_id.set(producto.id)
        self.var_nombre.set(producto.nombre)
        self.var_precio.set(str(producto.precio))
        self.var_cantidad.set(str(producto.cantidad))
        self.text_descripcion.delete("1.0", tk.END)
        self.text_descripcion.insert("1.0", producto.descripcion)
    
    def _guardar_producto(self):
        """Guarda un nuevo producto"""
        nombre = self.var_nombre.get()
        precio = self.var_precio.get()
        cantidad = self.var_cantidad.get()
        descripcion = self.text_descripcion.get("1.0", tk.END).strip()
        
        if not self.var_id.get():  # Es un producto nuevo
            exito, resultado = self.restaurante_servicio.registrar_producto(
                nombre, precio, cantidad, descripcion
            )
            
            if exito:
                messagebox.showinfo("Éxito", f"Producto registrado: {resultado.id} - {resultado.nombre}")
                self._limpiar_formulario()
                self._actualizar_listbox_productos()
            else:
                messagebox.showerror("Error", resultado)
        else:
            messagebox.showwarning("Advertencia", "Use 'Actualizar' para modificar un producto existente")
    
    def _actualizar_producto(self):
        """Actualiza el producto actualmente seleccionado"""
        producto_id = self.var_id.get().strip()
        
        if not producto_id:
            messagebox.showwarning("Advertencia", "Seleccione un producto de la lista")
            return
        
        nombre = self.var_nombre.get()
        precio = self.var_precio.get()
        cantidad = self.var_cantidad.get()
        descripcion = self.text_descripcion.get("1.0", tk.END).strip()
        
        exito, resultado = self.restaurante_servicio.actualizar_producto(
            producto_id, nombre, precio, cantidad, descripcion
        )
        
        if exito:
            messagebox.showinfo("Éxito", f"Producto actualizado: {resultado.nombre}")
            self._actualizar_listbox_productos()
            # Mantener el producto seleccionado pero actualizado
            self._cargar_producto_en_formulario(resultado)
        else:
            messagebox.showerror("Error", resultado)
    
    def _eliminar_producto(self):
        """Elimina el producto actualmente seleccionado"""
        producto_id = self.var_id.get().strip()
        
        if not producto_id:
            messagebox.showwarning("Advertencia", "Seleccione un producto de la lista")
            return
        
        # Confirmar eliminación
        if not messagebox.askyesno("Confirmar", f"¿Eliminar producto {producto_id}?"):
            return
        
        exito, mensaje = self.restaurante_servicio.eliminar_producto(producto_id)
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self._limpiar_formulario()
            self._actualizar_listbox_productos()
        else:
            messagebox.showerror("Error", mensaje)
    
    def _limpiar_formulario(self):
        """Limpia todos los campos del formulario"""
        self.var_id.set("")
        self.var_nombre.set("")
        self.var_precio.set("")
        self.var_cantidad.set("")
        self.text_descripcion.delete("1.0", tk.END)
        self.producto_seleccionado = None
        self.listbox_productos.selection_clear(0, tk.END)
        self.entry_nombre.focus()
    
    def _actualizar_listbox_productos(self):
        """Actualiza la lista de productos en el panel izquierdo"""
        self.listbox_productos.delete(0, tk.END)
        productos = self.restaurante_servicio.obtener_productos()
        
        if not productos:
            self.listbox_productos.insert(tk.END, "(No hay productos)")
        else:
            for p in productos:
                # Mostrar: ID - Nombre (Precio)
                texto = f"{p.id} - {p.nombre} (${p.precio:.2f})"
                self.listbox_productos.insert(tk.END, texto)
    
    def _actualizar_usuarios(self):
        """Actualiza la lista de usuarios"""
        self.listbox_usuarios.delete(0, tk.END)
        usuarios = self.restaurante_servicio.obtener_usuarios()
        
        if not usuarios:
            self.listbox_usuarios.insert(tk.END, "No hay usuarios registrados")
        else:
            for u in usuarios:
                self.listbox_usuarios.insert(
                    tk.END,
                    f"{u.nombre} ({u.usuario}) - {u.rol}"
                )
    
    # ===== MÉTODOS CRUD PARA USUARIOS =====
    
    def _nuevo_usuario(self):
        """Prepara el formulario para crear un nuevo usuario"""
        self._limpiar_formulario_usuarios()
        self.entry_nombre_usuario.focus()
    
    def _on_select_usuario(self, event):
        """Se ejecuta cuando se selecciona un usuario en la lista"""
        seleccion = self.listbox_usuarios.curselection()
        if not seleccion:
            return
        
        indice = seleccion[0]
        usuarios = self.restaurante_servicio.obtener_usuarios()
        
        if indice < len(usuarios):
            usuario = usuarios[indice]
            self.usuario_seleccionado = usuario
            self._cargar_usuario_en_formulario(usuario)
    
    def _cargar_usuario_en_formulario(self, usuario):
        """Carga los datos de un usuario en el formulario"""
        self.var_id_usuario.set(usuario.id)
        self.var_nombre_usuario.set(usuario.nombre)
        self.var_usuario_usuario.set(usuario.usuario)
        self.var_contrasena.set(usuario.contraseña)
        self.var_rol.set(usuario.rol)
    
    def _guardar_usuario(self):
        """Guarda un nuevo usuario"""
        nombre = self.var_nombre_usuario.get()
        usuario = self.var_usuario_usuario.get()
        contrasena = self.var_contrasena.get()
        rol = self.var_rol.get()
        
        if not self.var_id_usuario.get():  # Es un usuario nuevo
            exito, resultado = self.restaurante_servicio.registrar_usuario(
                nombre, usuario, contrasena, rol
            )
            
            if exito:
                messagebox.showinfo("Éxito", f"Usuario registrado: {resultado.id} - {resultado.nombre}")
                self._limpiar_formulario_usuarios()
                self._actualizar_listbox_usuarios()
            else:
                messagebox.showerror("Error", resultado)
        else:
            messagebox.showwarning("Advertencia", "Use 'Actualizar' para modificar un usuario existente")
    
    def _actualizar_usuario(self):
        """Actualiza el usuario actualmente seleccionado"""
        usuario_id = self.var_id_usuario.get().strip()
        
        if not usuario_id:
            messagebox.showwarning("Advertencia", "Seleccione un usuario de la lista")
            return
        
        nombre = self.var_nombre_usuario.get()
        usuario = self.var_usuario_usuario.get()
        contrasena = self.var_contrasena.get()
        rol = self.var_rol.get()
        
        exito, resultado = self.restaurante_servicio.actualizar_usuario(
            usuario_id, nombre, usuario, contrasena, rol
        )
        
        if exito:
            messagebox.showinfo("Éxito", f"Usuario actualizado: {resultado.nombre}")
            self._actualizar_listbox_usuarios()
            # Mantener el usuario seleccionado pero actualizado
            self._cargar_usuario_en_formulario(resultado)
        else:
            messagebox.showerror("Error", resultado)
    
    def _eliminar_usuario(self):
        """Elimina el usuario actualmente seleccionado"""
        usuario_id = self.var_id_usuario.get().strip()
        
        if not usuario_id:
            messagebox.showwarning("Advertencia", "Seleccione un usuario de la lista")
            return
        
        # Confirmar eliminación
        if not messagebox.askyesno("Confirmar", f"¿Eliminar usuario {usuario_id}?"):
            return
        
        exito, mensaje = self.restaurante_servicio.eliminar_usuario(usuario_id)
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self._limpiar_formulario_usuarios()
            self._actualizar_listbox_usuarios()
        else:
            messagebox.showerror("Error", mensaje)
    
    def _limpiar_formulario_usuarios(self):
        """Limpia todos los campos del formulario de usuarios"""
        self.var_id_usuario.set("")
        self.var_nombre_usuario.set("")
        self.var_usuario_usuario.set("")
        self.var_contrasena.set("")
        self.var_rol.set("")
        self.usuario_seleccionado = None
        self.listbox_usuarios.selection_clear(0, tk.END)
        self.entry_nombre_usuario.focus()
    
    def _actualizar_listbox_usuarios(self):
        """Actualiza la lista de usuarios en el panel izquierdo"""
        self.listbox_usuarios.delete(0, tk.END)
        usuarios = self.restaurante_servicio.obtener_usuarios()
        
        if not usuarios:
            self.listbox_usuarios.insert(tk.END, "(No hay usuarios)")
        else:
            for u in usuarios:
                # Mostrar: Nombre (Usuario) - Rol
                texto = f"{u.nombre} ({u.usuario}) - {u.rol}"
                self.listbox_usuarios.insert(tk.END, texto)
    
    def mostrar(self):
        """Muestra la vista principal"""
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def ocultar(self):
        """Oculta la vista principal"""
        self.frame.pack_forget()
