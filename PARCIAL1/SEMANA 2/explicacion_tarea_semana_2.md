# Explicación detallada del código de `tarea semana 2 .py`

Este archivo explica cada parte del código paso a paso. Está escrito pensando en alguien que está aprendiendo programación orientada a objetos (POO).

## 1. ¿Qué es una clase?

Una clase es una plantilla o molde para crear objetos. En POO, un objeto es una entidad que combina datos y funciones que trabajan con esos datos.

En este código, la clase se llama `CuentaBancaria`.

```python
class CuentaBancaria:
    """Clase que representa una cuenta bancaria sencilla."""
```

- `class CuentaBancaria:` define la clase.
- El texto entre `"""` se llama docstring y describe qué hace la clase.

## 2. El método `__init__`

El método `__init__` se ejecuta automáticamente cuando se crea un objeto nuevo de la clase.
Se conoce como el constructor.

```python
    def __init__(self, titular, numero_cuenta, saldo_inicial=0.0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = float(saldo_inicial)
```

- `self` es una referencia al propio objeto. Permite guardar datos dentro del objeto.
- `titular`, `numero_cuenta` y `saldo_inicial` son parámetros que se pasan al crear la cuenta.
- `self.titular = titular` guarda el nombre del titular en el objeto.
- `self.numero_cuenta = numero_cuenta` guarda el número de cuenta.
- `self.saldo = float(saldo_inicial)` guarda el saldo inicial como número decimal.

### Atributos de la clase

Los atributos son variables que pertenecen a cada objeto.

En esta clase, los atributos son:
- `self.titular`
- `self.numero_cuenta`
- `self.saldo`

Cada vez que creas una `CuentaBancaria`, esos atributos se guardan en el objeto.

## 3. Método `depositar`

Este método permite agregar dinero a la cuenta.

```python
    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser mayor que cero.")
            return
        self.saldo += monto
        print(f"Depósito: ${monto:.2f} realizado.")
```

- Se recibe un `monto` para depositar.
- Primero verifica si el monto es válido (`monto <= 0`). Si no lo es, muestra un mensaje y termina.
- Si el monto es correcto, suma el valor a `self.saldo`.
- `print(f"Depósito: ${monto:.2f} realizado.")` muestra el resultado con dos decimales.

## 4. Método `retirar`

Este método permite sacar dinero de la cuenta.

```python
    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser mayor que cero.")
            return
        if monto > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
            return
        self.saldo -= monto
        print(f"Retiro: ${monto:.2f} realizado.")
```

- También recibe un `monto`.
- Verifica primero que el monto sea mayor que cero.
- Después revisa si hay suficiente dinero en la cuenta (`monto > self.saldo`). Si no hay, muestra un mensaje.
- Si todo está bien, resta el monto de `self.saldo`.
- Imprime un mensaje con el monto retirado.

## 5. Método `mostrar_informacion`

Este método muestra los datos principales de la cuenta.

```python
    def mostrar_informacion(self):
        print("Información de la cuenta:")
        print(f"Titular: {self.titular}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Saldo actual: ${self.saldo:.2f}")
```

- No recibe datos adicionales.
- Imprime el nombre del titular, el número de cuenta y el saldo actual.

## 6. Bloque principal (`if __name__ == "__main__"`)

Esta parte del código se ejecuta sólo cuando corres el archivo directamente.

```python
if __name__ == "__main__":
    cuenta = CuentaBancaria("Adriana Arias", "1234567890", 1500.0)
    cuenta.mostrar_informacion()

    print("\nRealizando operaciones:")
    cuenta.depositar(250.0)
    cuenta.retirar(100.0)
    cuenta.retirar(2000.0)

    print("\nEstado final de la cuenta:")
    cuenta.mostrar_informacion()
```

- `CuentaBancaria("Adriana Arias", "1234567890", 1500.0)` crea un objeto nuevo llamado `cuenta`.
- Luego llama a `cuenta.mostrar_informacion()` para ver los datos iniciales.
- Hace un depósito de 250 pesos con `cuenta.depositar(250.0)`.
- Retira 100 pesos con `cuenta.retirar(100.0)`.
- Intenta retirar 2000 pesos con `cuenta.retirar(2000.0)`, pero el saldo no es suficiente, así que muestra un mensaje de error.
- Finalmente, muestra otra vez la información de la cuenta con el saldo actualizado.

## 7. ¿Por qué es útil la programación orientada a objetos aquí?

- La clase `CuentaBancaria` agrupa datos y acciones en un solo lugar.
- Cada cuenta bancaria que creas es un objeto independiente con su propio titular, número y saldo.
- Los métodos (`depositar`, `retirar`, `mostrar_informacion`) son acciones que la cuenta puede realizar.
- Esto ayuda a organizar mejor el código y a reutilizarlo cuando necesites crear más cuentas.

## 8. Resumen rápido

- `class CuentaBancaria`: define la plantilla de la cuenta.
- `__init__`: inicializa cada cuenta nueva.
- `depositar`: añade dinero.
- `retirar`: quita dinero si hay saldo suficiente.
- `mostrar_informacion`: enseña los datos de la cuenta.
- `if __name__ == "__main__"`: ejecuta ejemplos cuando corres el archivo.

¡Listo! Ya tienes una explicación paso a paso para entender cómo funciona este código en términos de POO.