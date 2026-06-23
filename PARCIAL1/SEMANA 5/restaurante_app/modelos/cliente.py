"""
Módulo de la clase Cliente
Define la estructura de un cliente registrado en el restaurante
"""


class Cliente:
    """
    Representa un cliente registrado en el sistema del restaurante.

    Atributos:
        nombre (str): Nombre completo del cliente
        email (str): Dirección de correo electrónico del cliente
        telefono (str): Número de teléfono de contacto
        edad (int): Edad del cliente
        es_miembro_premium (bool): Indica si el cliente es miembro premium
    """

    def __init__(
        self,
        nombre: str,
        email: str,
        telefono: str,
        edad: int,
        es_miembro_premium: bool
    ) -> None:
        """
        Constructor que inicializa un objeto Cliente con sus atributos.

        Args:
            nombre: Nombre completo del cliente
            email: Email del cliente
            telefono: Teléfono de contacto
            edad: Edad del cliente
            es_miembro_premium: Booleano indicando membresía premium
        """
        self.nombre: str = nombre
        self.email: str = email
        self.telefono: str = telefono
        self.edad: int = edad
        self.es_miembro_premium: bool = es_miembro_premium

    def __str__(self) -> str:
        """
        Retorna una representacion en texto del cliente.

        Returns:
            str: Informacion formateada del cliente
        """
        estado_membresia = "Si" if self.es_miembro_premium else "No"
        return (
            f"Cliente: {self.nombre}\n"
            f"  Email: {self.email}\n"
            f"  Telefono: {self.telefono}\n"
            f"  Edad: {self.edad} anos\n"
            f"  Miembro Premium: {estado_membresia}"
        )

    def mostrar_perfil(self) -> None:
        """
        Imprime el perfil completo del cliente en consola.
        """
        print(self)

    def actualizar_email(self, nuevo_email: str) -> None:
        """
        Actualiza la direccion de correo del cliente.

        Args:
            nuevo_email: Nueva direccion de correo electronico
        """
        email_anterior = self.email
        self.email = nuevo_email
        print(f"Email de {self.nombre} actualizado de {email_anterior} a {nuevo_email}")

    def actualizar_telefono(self, nuevo_telefono: str) -> None:
        """
        Actualiza el numero de telefono del cliente.

        Args:
            nuevo_telefono: Nuevo numero de telefono
        """
        telefono_anterior = self.telefono
        self.telefono = nuevo_telefono
        print(f"Telefono de {self.nombre} actualizado de {telefono_anterior} a {nuevo_telefono}")

    def obtener_estado_membresia(self) -> str:
        """
        Retorna el estado de membresía del cliente.

        Returns:
            str: Descripción del estado de membresía
        """
        if self.es_miembro_premium:
            return "Cliente Premium con beneficios especiales"
        else:
            return "Cliente Regular"

