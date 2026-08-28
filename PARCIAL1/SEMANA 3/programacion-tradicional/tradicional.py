# tradicional.py

def registrar_mascota():
    """Función para solicitar los datos de la mascota por teclado."""
    print("--- REGISTRO DE MASCOTA (Programación Tradicional) ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (Ej. Perro, Gato): ")

    # Validación simple para la edad
    while True:
        try:
            edad = int(input("Ingrese la edad de la mascota: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")

    # Retornamos los datos agrupados en un diccionario
    return {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }


def mostrar_mascota(mascota):
    """Función para mostrar la información estructurada de la mascota."""
    print("\n=================================")
    print("      INFORMACIÓN DE LA MASCOTA  ")
    print("=================================")
    print(f"Nombre:  {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad:    {mascota['edad']} años")
    print("=================================\n")


# Flujo principal del programa
if __name__ == "__main__":
    # Registramos una mascota
    nueva_mascota = registrar_mascota()
    # Mostramos su información
    mostrar_mascota(nueva_mascota)