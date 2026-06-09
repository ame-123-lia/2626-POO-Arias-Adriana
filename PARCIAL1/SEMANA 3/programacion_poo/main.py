# main.py
from mascota import Mascota


def ejecutar_sistema():
    print("--- SISTEMA DE GESTIÓN DE MASCOTAS (POO) ---\n")

    # Mascota 1: Pidiendo datos al usuario
    print("Ingrese los datos de la primera mascota:")
    nom1 = input("Nombre: ")
    esp1 = input("Especie: ")
    edad1 = int(input("Edad: "))
    mascota1 = Mascota(nom1, esp1, edad1)

    # Mascota 2: Registro automático (para cumplir con el mínimo de 2 objetos)
    print("\nRegistrando segunda mascota de forma automática...")
    mascota2 = Mascota("Luna", "Gato", 3)

    # Mostrar la información de ambos objetos
    print("\n=================================")
    print("      MOSTRANDO OBJETOS (POO)    ")
    print("=================================")

    print("[Mascota 1]")
    mascota1.mostrar_informacion()
    print(f"Sonido:  {mascota1.hacer_sonido()}")
    print("-" * 33)

    print("[Mascota 2]")
    mascota2.mostrar_informacion()
    print(f"Sonido:  {mascota2.hacer_sonido()}")
    print("=================================")


if __name__ == "__main__":
    ejecutar_sistema()