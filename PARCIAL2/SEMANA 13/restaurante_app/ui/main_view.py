import tkinter as tk
from tkinter import ttk


class MainView:
    def __init__(self, root, restaurante_servicio, callback_logout):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.callback_logout = callback_logout
        
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
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
        """Crea el contenido de la tab de productos"""
        titulo = tk.Label(
            self.tab_productos,
            text="Productos Registrados",
            font=("Arial", 14, "bold"),
            fg="#2c3e50"
        )
        titulo.pack(pady=15)
        
        # Frame para la tabla
        frame_tabla = tk.Frame(self.tab_productos)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        self.listbox_productos = tk.Listbox(
            frame_tabla,
            font=("Arial", 10),
            yscrollcommand=scrollbar.set
        )
        self.listbox_productos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox_productos.yview)
        
        # Cargar productos
        self._actualizar_productos()
    
    def _crear_tab_usuarios(self):
        """Crea el contenido de la tab de usuarios"""
        titulo = tk.Label(
            self.tab_usuarios,
            text="Usuarios Registrados",
            font=("Arial", 14, "bold"),
            fg="#2c3e50"
        )
        titulo.pack(pady=15)
        
        # Frame para la tabla
        frame_tabla = tk.Frame(self.tab_usuarios)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        self.listbox_usuarios = tk.Listbox(
            frame_tabla,
            font=("Arial", 10),
            yscrollcommand=scrollbar.set
        )
        self.listbox_usuarios.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox_usuarios.yview)
        
        # Cargar usuarios
        self._actualizar_usuarios()
    
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
    
    def _actualizar_productos(self):
        """Actualiza la lista de productos"""
        self.listbox_productos.delete(0, tk.END)
        productos = self.restaurante_servicio.obtener_productos()
        
        if not productos:
            self.listbox_productos.insert(tk.END, "No hay productos registrados")
        else:
            for p in productos:
                self.listbox_productos.insert(
                    tk.END,
                    f"{p.nombre} - ${p.precio:.2f} - Stock: {p.cantidad}"
                )
    
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
    
    def mostrar(self):
        """Muestra la vista principal"""
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def ocultar(self):
        """Oculta la vista principal"""
        self.frame.pack_forget()
