# mascota.py

class Mascota:
    def __init__(self, nombre, especie, edad):
        """Método constructor para inicializar los atributos de la mascota."""
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Método para mostrar los datos de forma organizada."""
        print(f"Nombre:  {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad:    {self.edad} años")

    def hacer_sonido(self):
        """Método para simular el sonido según la especie."""
        especie_baja = self.especie.lower()
        if "perro" in especie_baja:
            return "¡Guau guau!"
        elif "gato" in especie_baja:
            return "¡Miau miau!"
        else:
            return "¡Hace un sonido característico!"