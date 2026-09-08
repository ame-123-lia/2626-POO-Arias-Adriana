import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(self, root, restaurante_servicio, callback_login):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.callback_login = callback_login
        
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self._crear_widgets()
    
    def _crear_widgets(self):
        """Crea los widgets de la interfaz de login"""
        # Título
        titulo = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 24, "bold"),
            fg="#2c3e50"
        )
        titulo.pack(pady=20)
        
        # Subtítulo
        subtitulo = tk.Label(
            self.frame,
            text="Ingrese sus credenciales",
            font=("Arial", 12),
            fg="#7f8c8d"
        )
        subtitulo.pack(pady=10)
        
        # Frame para el formulario
        form_frame = tk.Frame(self.frame, bg="white")
        form_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)
        
        # Etiqueta usuario
        tk.Label(
            form_frame,
            text="Usuario:",
            font=("Arial", 11),
            bg="white",
            justify=tk.LEFT
        ).pack(anchor=tk.W, pady=(10, 5), padx=20)
        
        # Campo usuario
        self.entry_usuario = tk.Entry(form_frame, font=("Arial", 11), width=30)
        self.entry_usuario.pack(padx=20, pady=5, fill=tk.X)
        self.entry_usuario.bind("<Return>", lambda e: self.ingresar())
        
        # Etiqueta contraseña
        tk.Label(
            form_frame,
            text="Contraseña:",
            font=("Arial", 11),
            bg="white",
            justify=tk.LEFT
        ).pack(anchor=tk.W, pady=(10, 5), padx=20)
        
        # Campo contraseña
        self.entry_contraseña = tk.Entry(
            form_frame,
            font=("Arial", 11),
            width=30,
            show="*"
        )
        self.entry_contraseña.pack(padx=20, pady=5, fill=tk.X)
        self.entry_contraseña.bind("<Return>", lambda e: self.ingresar())
        
        # Botón ingresar
        btn_ingresar = tk.Button(
            form_frame,
            text="Ingresar",
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=10,
            command=self.ingresar
        )
        btn_ingresar.pack(pady=20)
        
        # Label para mensajes
        self.label_mensaje = tk.Label(
            self.frame,
            text="",
            font=("Arial", 10),
            fg="#c0392b"
        )
        self.label_mensaje.pack(pady=10)
    
    def ingresar(self):
        """Procesa el intento de login"""
        usuario = self.entry_usuario.get().strip()
        contraseña = self.entry_contraseña.get()
        
        if not usuario or not contraseña:
            self.label_mensaje.config(text="Por favor, complete todos los campos")
            return
        
        exito, mensaje = self.restaurante_servicio.validar_acceso(usuario, contraseña)
        
        if exito:
            self.entry_usuario.delete(0, tk.END)
            self.entry_contraseña.delete(0, tk.END)
            self.label_mensaje.config(text="")
            self.callback_login()
        else:
            self.label_mensaje.config(text=mensaje)
    
    def limpiar(self):
        """Limpia los campos de entrada"""
        self.entry_usuario.delete(0, tk.END)
        self.entry_contraseña.delete(0, tk.END)
        self.label_mensaje.config(text="")
    
    def mostrar(self):
        """Muestra la vista de login"""
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.entry_usuario.focus()
    
    def ocultar(self):
        """Oculta la vista de login"""
        self.frame.pack_forget()
