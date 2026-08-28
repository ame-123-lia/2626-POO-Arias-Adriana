# 🎓 Programación Orientada a Objetos (POO) - Proyecto Académico

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📋 Descripción General

Este repositorio contiene el trabajo completo del curso **Programación Orientada a Objetos (POO)** que abarca dos parciales con múltiples semanas de desarrollo. El proyecto principal es un **Sistema de Gestión de Restaurante** que evoluciona progresivamente con cada semana, implementando conceptos fundamentales de POO.

**Estudiante**: Adriana Arias  
**Código de Curso**: 2626-POO-Arias-Adriana  
**Institución**: [Académica]  

---

## 📂 Estructura del Repositorio

```
2626-POO-Arias-Adriana/
├── README.md                          # Este archivo
├── .gitignore                         # Configuración de Git
├── PARCIAL1/                          # Primer parcial (Semanas 4-8)
│   ├── SEMANA 4/                      # Introducción a POO - Clases básicas
│   ├── SEMANA 5/                      # Herencia y composición
│   ├── SEMANA 6/                      # Polimorfismo
│   ├── SEMANA 7/                      # Encapsulación
│   └── SEMANA 8/                      # Integración de conceptos
│
└── PARCIAL2/                          # Segundo parcial (Semanas 9-11)
    ├── SEMANA 9/                      # Persistencia de datos
    ├── SEMANA 10/                     # Servicios y arquitectura
    └── SEMANA 11/                     # Sistema completo (README.md incluido)
```

---

## 🎯 Objetivos del Proyecto

### Parcial 1: Fundamentos de POO
- ✅ Entender y aplicar los 4 pilares de la POO
- ✅ Diseñar clases con responsabilidades claras
- ✅ Implementar herencia efectiva
- ✅ Usar polimorfismo para comportamientos flexibles
- ✅ Aplicar encapsulación de datos

### Parcial 2: Arquitectura y Persistencia
- ✅ Integrar persistencia de datos (JSON)
- ✅ Aplicar patrones de diseño (MVC, DAO)
- ✅ Desarrollar servicios de negocio
- ✅ Manejar excepciones robustamente
- ✅ Crear interfaces de usuario

---

## 🏛️ Evolución del Proyecto

### Semana 4️⃣: Introducción a Clases
**Conceptos**: Atributos, métodos, constructores  
**Resultado**: Clases base `Producto`, `Cliente`
```python
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
```

### Semana 5️⃣: Estructura de Paquetes
**Conceptos**: Módulos, paquetes, organización  
**Resultado**: Estructura `restaurante_app/` con carpetas `modelos/` y `servicios/`

### Semana 6️⃣: Extensión de Funcionalidades
**Conceptos**: Nuevos modelos, relaciones entre objetos  
**Resultado**: Clases `Bebida`, `Platillo` extendiendo `Producto`

### Semana 7️⃣: Herencia y Polimorfismo
**Conceptos**: Clase base `Producto`, clases derivadas  
**Resultado**: Uso efectivo de herencia en la jerarquía de productos

### Semana 8️⃣: Integración I
**Conceptos**: Composición, agregación, servicios básicos  
**Resultado**: Servicio `Restaurante` orquestando colecciones

### Semana 9️⃣: Persistencia JSON
**Conceptos**: Serialización, deserialización, I/O de archivos  
**Resultado**: `ArchivoServicio` con carga/guardado en JSON  
**Archivo**: `PARCIAL2/SEMANA 9/`

### Semana 🔟: Mejoría de Arquitectura
**Conceptos**: Patrones de diseño, servicios especializados  
**Resultado**: Refactorización completa del código  
**Archivo**: `PARCIAL2/SEMANA 10/`

### Semana 1️⃣1️⃣: Sistema Completo
**Conceptos**: Integración total, menú interactivo, validaciones  
**Resultado**: Sistema funcional listo para producción  
**Archivo**: `PARCIAL2/SEMANA 11/` 📌 **[VER ESTE]**

---

## 🍽️ Sistema de Gestión de Restaurante - Vista General

### Características Principales

#### 📦 Gestión de Productos
- Registro de productos con código, nombre, categoría, precio y stock
- Búsqueda rápida por código
- Actualización de información
- Eliminación de catálogo
- Listado completo

#### 👥 Gestión de Usuarios
- Registro de clientes con identificación, nombre y correo
- Listado de usuarios
- Historial de compras por usuario

#### 💳 Gestión de Ventas
- Registro de transacciones
- Control automático de stock
- Consulta de ventas por usuario
- Reportes de ventas totales

#### 💾 Almacenamiento Persistente
- Datos en JSON (productos, usuarios, ventas)
- Carga automática al iniciar
- Guardado automático tras cambios

### Arquitectura Técnica

```
Capa de Presentación
    ↓ (main.py - Menú interactivo)
Capa de Servicios
    ↓ (restaurante.py, archivo_servicio.py)
Capa de Modelos
    ↓ (producto.py, usuario.py, venta.py)
Almacenamiento
    ↓ (JSON files)
```

---

## 🏗️ Conceptos POO Implementados

### 1️⃣ Encapsulación
- Atributos privados con prefijo `_`
- Métodos de acceso públicos
- Validación en setters
```python
self._productos = []  # Privado
def registrar_producto(self, producto):  # Público
    # Lógica de validación
```

### 2️⃣ Herencia
- Clases base con funcionalidad común
- Métodos heredados en subclases
- `@classmethod` para constructores alternativos
```python
class Producto:
    def to_dict(self): pass
    
class Usuario(Entidad):
    def to_dict(self): pass  # Heredado
```

### 3️⃣ Polimorfismo
- Métodos `to_dict()` y `from_dict()` en todas las entidades
- Comportamiento diferente según el tipo
- Interfaz uniforme para serialización
```python
for entidad in [producto, usuario, venta]:
    entidad.to_dict()  # Polimórfico
```

### 4️⃣ Abstracción
- Interfaces simples y claras
- Complejidad oculta en implementación
- Métodos de nivel alto como `vender_producto()`
```python
def vender_producto(self, codigo, id_usuario, cantidad):
    # Abstracción de lógica compleja
    usuario = self.buscar_usuario_por_id(id_usuario)
    producto = self.buscar_producto_por_codigo(codigo)
    # ... validaciones y actualización
```

---

## 🚀 Cómo Usar Este Repositorio

### Ejecución del Sistema Completo (Recomendado)

```bash
# Navegar a la carpeta de la última semana
cd PARCIAL2/SEMANA\ 11/

# Ejecutar el sistema
python restaurante_app/main.py
```

### Explorar Progresión Histórica

```bash
# Ver versión de Semana 9 (con persistencia)
cd PARCIAL2/SEMANA\ 9/
python restaurante_app/main.py

# Ver versión de Semana 10 (arquitectura mejorada)
cd PARCIAL2/SEMANA\ 10/
python restaurante_app/main.py
```

### Estructura de Directorios de Ejecución

Cada carpeta de semana contiene:
```
SEMANA X/
├── restaurante_app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada
│   ├── modelos/                # Clases de entidades
│   ├── servicios/              # Lógica de negocio
│   └── datos/                  # Almacenamiento JSON
└── [archivos adicionales]
```

---

## 📋 Checklist de Funcionalidades

### Semana 11 (Sistema Completo)
- [x] Interfaz de usuario interactiva
- [x] Gestión completa de productos (CRUD)
- [x] Gestión de usuarios
- [x] Sistema de ventas con descuento de stock
- [x] Persistencia en JSON
- [x] Carga automática de datos
- [x] Validaciones exhaustivas
- [x] Manejo robusto de excepciones
- [x] Documentación completa (README.md)
- [x] Type hints en todo el código

---

## 🔧 Requisitos Técnicos

### Requisitos Mínimos
- **Python**: 3.8 o superior
- **Sistema Operativo**: Windows, macOS o Linux
- **Dependencias**: Ninguna (solo biblioteca estándar)

### Dependencias Utilizadas
```python
# Solo librerías estándar de Python
import json        # Manejo de JSON
import pathlib     # Operaciones con rutas
from typing import *  # Type hints
```

---

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| Semanas de Desarrollo | 8 |
| Versiones del Sistema | 4 |
| Clases Principales | 4 |
| Métodos Implementados | 50+ |
| Líneas de Código | 1500+ |
| Validaciones | 15+ |
| Archivos JSON | 3 |

---

## 📚 Archivos Destacados

### Semana 11 (Recomendado)
- `PARCIAL2/SEMANA 11/README.md` - Documentación detallada del sistema
- `PARCIAL2/SEMANA 11/restaurante_app/main.py` - Programa principal (332 líneas)
- `PARCIAL2/SEMANA 11/restaurante_app/servicios/restaurante.py` - Lógica de negocio

### Otras Semanas
Explora las carpetas anteriores para ver la evolución del proyecto:
- Semana 4-8: Desarrollo de conceptos fundamentales
- Semana 9: Introducción a persistencia JSON
- Semana 10: Mejora de arquitectura
- Semana 11: Sistema final completo

---

## 🎓 Conceptos de Clase Implementados

### Programación Estructurada
- Control de flujo (if, while, for)
- Funciones y parámetros
- Manejo de excepciones

### Programación Orientada a Objetos
- Clases y objetos
- Atributos y métodos
- Constructores (`__init__`)
- Encapsulación
- Herencia
- Polimorfismo
- Abstracción

### Patrones de Diseño
- **MVC**: Separación de modelos, vista (menú), controlador
- **DAO**: Patrón de acceso a datos (ArchivoServicio)
- **Singleton**: Instancia única de Restaurante

### Buenas Prácticas
- Type hints para claridad
- Docstrings descriptivos
- Nombres significativos de variables
- Validación de entrada
- Manejo de errores
- Modularización

---

## 💡 Puntos de Aprendizaje Clave

1. **Diseño de Clases**: Cómo estructurar responsabilidades
2. **Reutilización de Código**: Herencia efectiva
3. **Flexibilidad**: Polimorfismo y abstracción
4. **Persistencia**: Almacenamiento y recuperación de datos
5. **Interfaz de Usuario**: Menú interactivo en terminal
6. **Validaciones**: Reglas de negocio en el código
7. **Excepciones**: Manejo robusto de errores
8. **Documentación**: Código autodocumentado con docstrings

---

## 🔄 Cómo Navegar el Repositorio

### Para Ver Evolución del Proyecto
```
PARCIAL1/
├── SEMANA 4  → Concepto básico
├── SEMANA 5  → Con estructura
├── SEMANA 6  → Más clases
├── SEMANA 7  → Herencia completa
└── SEMANA 8  → Sistema simple

PARCIAL2/
├── SEMANA 9   → Agregar persistencia
├── SEMANA 10  → Mejorar arquitectura
└── SEMANA 11  → Sistema final ⭐
```

### Recomendación
Para obtener la mejor experiencia:
1. **Ejecuta Semana 11** para ver el sistema completo funcional
2. **Lee README.md de Semana 11** para detalles técnicos
3. **Revisa el código** de semanas anteriores para ver la evolución

---

## 📞 Información de Contacto

**Estudiante**: Adriana Arias  
**Asignatura**: Programación Orientada a Objetos (POO)  
**Código del Curso**: 2626-POO-Arias-Adriana  
**Repositorio**: GitHub - ame-123-lia/2626-POO-Arias-Adriana  

---

## 📄 Licencia

Este proyecto es parte del trabajo académico del curso de Programación Orientada a Objetos.

---

## 🎉 Conclusión

Este proyecto demuestra la evolución progresiva de un sistema desde conceptos básicos de programación hasta una aplicación completa siguiendo principios sólidos de POO. Cada semana construye sobre la anterior, creando un proyecto cohesivo y bien estructurado.

**¡Bienvenido a explorar el código!** 🚀

---

**Última actualización**: Semana 11 - 2024  
**Estado**: ✅ Completo  
**Versión**: 1.0
