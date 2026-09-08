import tkinter as tk
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from servicios import ArchivoServicio, RestauranteServicio
from ui import LoginView, MainView


class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Semana 13")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Inicializar servicios
        ruta_datos = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "datos"
        )
        self.archivo_servicio = ArchivoServicio(ruta_datos)
        self.restaurante_servicio = RestauranteServicio(self.archivo_servicio)
        
        # Crear vista de login
        self.login_view = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_main_view
        )
        
        # MainView se crea de forma lazy cuando se autentica
        self.main_view = None
        
        # Mostrar login inicialmente
        self.mostrar_login_view()
    
    def mostrar_login_view(self):
        """Muestra la vista de login"""
        if self.main_view is not None:
            self.main_view.ocultar()
        self.restaurante_servicio.cerrar_sesion()
        self.login_view.limpiar()
        self.login_view.mostrar()
    
    def mostrar_main_view(self):
        """Muestra la vista principal"""
        # Crear MainView la primera vez que se necesita (después del login)
        if self.main_view is None:
            self.main_view = MainView(
                self.root,
                self.restaurante_servicio,
                self.mostrar_login_view
            )
        
        self.login_view.ocultar()
        self.main_view.mostrar()


def main():
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
