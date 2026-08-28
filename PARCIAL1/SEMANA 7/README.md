# SEMANA 7: SISTEMA DE RESTAURANTE - POO DIDÁCTICO

## 📚 Objetivo
Comprender e implementar los **principios fundamentales de Programación Orientada a Objetos (POO)** a través de un sistema de gestión de restaurante.

## 🎯 Principios de POO Demostrados

### 1. **ENCAPSULACIÓN** 🔒
**¿Qué es?** Ocultar los detalles internos de una clase y permitir acceso controlado.

**Implementación en el código:**

```python
class Producto:
    def __init__(self, nombre: str, precio: float):
        # Los atributos son PRIVADOS (comienzan con _)
        self._nombre = None
        self._precio = None
        # Se asignan mediante setters que validan
        self.nombre = nombre
        self.precio = precio
    
    @property
    def precio(self) -> float:
        """GETTER: Permite lectura del dato privado"""
        return self._precio
    
    @precio.setter
    def precio(self, valor: float) -> None:
        """SETTER: Valida antes de asignar"""
        if valor <= 0:
            raise ValueError("El precio debe ser positivo")
        self._precio = valor
```

**Beneficios:**
- ✓ El objeto siempre está en un estado válido
- ✓ No se puede asignar datos inválidos
- ✓ Se puede cambiar la implementación interna sin afectar el código externo

---

### 2. **ABSTRACCIÓN** 🎭
**¿Qué es?** Mostrar solo la interfaz esencial, ocultando la complejidad.

**Implementación en el código:**

El usuario solo necesita conocer:
```python
# Interface pública (lo que el usuario ve)
producto = Producto("Pizza", "Plato", 15.99)
print(producto.mostrar_informacion())
producto.precio = 17.99  # Parece simple, pero valida internamente
```

El usuario **NO necesita saber:**
- Cómo se validan los datos
- Cómo se almacenan internamente
- Los detalles de implementación

---

### 3. **REUTILIZACIÓN** ♻️
**¿Qué es?** Crear código modular que se pueda usar en diferentes contextos.

**Jerarquía de clases (Composite Pattern):**

```
Restaurante (Gestor)
    ├── Lista de Productos
    └── Lista de Clientes
```

**Métodos reutilizables:**
```python
restaurante.registrar_producto(producto)
restaurante.buscar_producto("Pizza")
restaurante.obtener_productos_disponibles()
restaurante.obtener_productos_por_categoria("Plato")
```

---

### 4. **VALIDACIÓN** ✔️
**¿Qué es?** Garantizar que los datos sean válidos antes de almacenarlos.

**Niveles de validación:**

a) **En Setters (Producto):**
```python
@nombre.setter
def nombre(self, valor: str) -> None:
    valor = valor.strip()
    if not valor:
        raise ValueError("El nombre no puede estar vacío")
    self._nombre = valor
```

b) **En __post_init__ (Cliente - Dataclass):**
```python
@dataclass
class Cliente:
    nombre: str
    correo: str
    
    def __post_init__(self):
        if not self.nombre:
            raise ValueError("Nombre requerido")
```

---

## 📂 Estructura del Proyecto

```
SEMANA 7/
│
├── restaurante_app/
│   ├── main.py                 # Punto de entrada (menú interactivo + demos)
│   ├── __init__.py             # Marca como paquete
│   │
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py         # Demuestra ENCAPSULACIÓN con properties
│   │   └── cliente.py          # Demuestra @dataclass y validación
│   │
│   └── servicios/
│       ├── __init__.py
│       └── restaurante.py      # Gestor (patrón Container)
│
└── README.md                   # Este archivo

```

---

## 🚀 Cómo Ejecutar

### Opción 1: Ejecutar directamente
```bash
cd SEMANA\ 7/restaurante_app
python main.py
```

### Opción 2: Ejecutar como módulo
```bash
cd SEMANA\ 7
python -m restaurante_app.main
```

---

## 📋 Menú de Opciones

### Gestión de Productos
1. **Registrar producto** - Crear un nuevo producto con validación
2. **Listar productos** - Ver todos los productos
3. **Buscar producto** - Búsqueda por nombre
4. **Ver productos disponibles** - Filtrar solo disponibles
5. **Filtrar por categoría** - Búsqueda por categoría

### Gestión de Clientes
6. **Registrar cliente** - Crear un nuevo cliente
7. **Listar clientes** - Ver todos los clientes
8. **Buscar cliente** - Búsqueda por nombre

### Información y Demostraciones
9. **Ver estadísticas** - Resumen del restaurante
10. **Demo de ENCAPSULACIÓN** - Observar cómo se previene datos inválidos
11. **Demo de VALIDACIÓN** - Ver los validadores en acción
12. **Salir**

---

## 💡 Ejemplos de Uso Interactivo

### Ejemplo 1: Intentar asignar precio inválido

```
Cuando ejecutas Demo de Encapsulación:
1. Se crea: Producto("Pizza", "Plato", 15.99)
2. Se intenta: precio = -5
3. Resultado: ValueError previene el valor negativo ✓

Lección: El objeto rechaza datos inválidos automáticamente
```

### Ejemplo 2: Crear cliente con datos vacíos

```
Intento: Cliente("", "test@mail.com", "ID123")
Resultado: ValueError en __post_init__ ✓

Lección: La validación ocurre ANTES de que el objeto se use
```

---

## 📚 Conceptos Avanzados Implementados

### Type Hints
```python
def buscar_producto(self, nombre: str) -> Optional[Producto]:
    # Especificamos que espera str y devuelve Optional[Producto]
```

**Beneficio:** Mayor claridad e IDE mejor autocomplete

### Properties vs Getters/Setters tradicionales

```python
# Forma antigua (otros lenguajes):
producto.get_precio()
producto.set_precio(10)

# Forma Pythónica (este proyecto):
producto.precio      # getter automático
producto.precio = 10 # setter con validación automática
```

### Dataclasses
```python
@dataclass
class Cliente:
    nombre: str
    correo: str
    # Genera automáticamente: __init__, __repr__, __eq__, etc.
```

---

## 🔍 Tareas Educativas

### Tarea 1: Agregar un método a Producto
```python
def aplicar_descuento(self, porcentaje: float) -> float:
    """Calcula el precio con descuento"""
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("Porcentaje inválido")
    descuento = self.precio * (porcentaje / 100)
    return self.precio - descuento
```

### Tarea 2: Agregar validación de email a Cliente
```python
def __post_init__(self):
    # ... validaciones existentes ...
    if "@" not in self.correo:
        raise ValueError("Correo inválido")
```

### Tarea 3: Crear una clase Pedido que use Producto y Cliente
```python
@dataclass
class Pedido:
    cliente: Cliente
    productos: List[Producto]
    
    def calcular_total(self) -> float:
        return sum(p.precio for p in self.productos)
```

---

## 🧪 Pruebas Sugeridas

```python
# Prueba 1: Validación de encapsulación
p = Producto("Test", "Test", 10)
try:
    p.precio = -5  # Debe fallar
except ValueError:
    print("✓ Encapsulación funciona")

# Prueba 2: Búsqueda (insensible a mayúsculas)
r = Restaurante()
p = Producto("Pizza", "Plato", 10)
r.registrar_producto(p)
assert r.buscar_producto("PIZZA") is not None
print("✓ Búsqueda funciona correctamente")

# Prueba 3: Estadísticas
stats = r.obtener_estadisticas()
assert stats["total_productos"] == 1
print("✓ Estadísticas correctas")
```

---

## 🎓 Conclusión

Este proyecto demuestra que **la POO no es solo sintaxis**, sino:
- ✓ Una forma de **organizar** el código
- ✓ Una forma de **proteger** los datos
- ✓ Una forma de **reutilizar** componentes
- ✓ Una forma de **prevenir errores** mediante validación

**Principio fundamental:** *"Un buen objeto nunca está en un estado inválido"*

---

**Autor:** Semana 7 - POO  
**Tema:** Principios fundamentales de Programación Orientada a Objetos  
**Nivel:** Principiante - Intermedio

