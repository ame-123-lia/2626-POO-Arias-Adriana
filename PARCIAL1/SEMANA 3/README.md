# Tarea Semana 3: Comparación de Paradigmas en Python

## Información del Estudiante
* **Nombre Completo:** Adriana Verónica Arias
* **Asignatura:** Programación Orientada a Objetos
* **Institución:** Universidad Estatal Amazónica (UEA)

---

## Descripción del Proyecto
Este proyecto consiste en un sistema básico de gestión de mascotas desarrollado bajo dos enfoques de programación distintos, con el objetivo de analizar y comparar la estructura, legibilidad y organización del código en cada paradigma:

1. **Programación Tradicional (`programacion-tradicional/`):** Una solución estructurada basada exclusivamente en variables y funciones independientes. Los datos se solicitan por teclado y se manipulan mediante estructuras básicas (diccionarios), manteniendo la lógica separada de los datos.
2. **Programación Orientada a Objetos (`programacion_poo/`):** Una solución modular que implementa el concepto de **abstracción** mediante la clase `Mascota` (ubicada en `mascota.py`). El archivo `main.py` actúa como el punto de entrada donde se instancian y gestionan los objetos, encapsulando sus atributos (nombre, especie, edad) y sus comportamientos a través de métodos.

---

## Estructura del Repositorio
```text
SEMANA 3
├── programacion-tradicional/
│   └── tradicional.py
├── programacion_poo/
│   ├── main.py
│   └── mascota.py
└── README.md