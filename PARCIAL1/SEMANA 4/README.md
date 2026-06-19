# Sistema de Gestión de Restaurante (POO Modular)

Estudiante: Adriana Verónica Arias

Asignatura: Programación Orientada a Objetos — Semana 4

Institución: Universidad Estatal Amazónica

---

1. Descripción
--------------
Proyecto educativo que modela un restaurante mediante una arquitectura modular en Python. Separa claramente las entidades (modelos), la lógica del negocio (servicios) y el punto de entrada para facilitar la lectura y la ampliación del código.

2. Objetivos
-----------
- Aplicar principios de POO (encapsulamiento, clases y responsabilidades)
- Diseñar un sistema modular y reutilizable
- Practicar la organización de un proyecto en paquetes y módulos

3. Estructura del proyecto (SEMANA 4)
-----------------------------------
```
SEMANA 4/
├── README.md
├── main.py             # Punto de entrada y ejemplo de uso
├── modelos/
│   ├── producto.py     # Clase Producto
│   └── cliente.py      # Clase Cliente
└── servicios/
	└── restaurante.py  # Lógica del restaurante (menú, clientes, pedidos)
```

4. Uso rápido
-------------
Desde la raíz del proyecto, en PowerShell (Windows):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python .\PARCIAL1\SEMANA 4\main.py
```

5. Notas
--------
- Revisar las clases en `modelos/` para entender atributos y métodos disponibles.
- El servicio `restaurante.py` centraliza las operaciones sobre clientes y productos.

Contacto
-------
Adriana Verónica Arias — Universidad Estatal Amazónica

