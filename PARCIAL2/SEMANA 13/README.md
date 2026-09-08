# Restaurante App - Semana 13

## Descripción

Esta es la primera versión gráfica del proyecto **Restaurante App**, desarrollada como parte de la Semana 13 de la asignatura Programación Orientada a Objetos. La aplicación implementa una interfaz gráfica de usuario (GUI) utilizando **Tkinter**, manteniendo una arquitectura de capas clara que separa modelos, servicios, datos y vistas.

## Objetivo

Transitar desde una aplicación basada en consola hacia una aplicación con interfaz gráfica, comprendiendo cómo se integran la ventana principal, las vistas gráficas y los servicios en una estructura modular y escalable.

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json          # Datos de productos disponibles
│   └── usuarios.json           # Datos de usuarios del sistema
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Modelo de Producto
│   └── usuario.py              # Modelo de Usuario
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py      # Carga datos desde JSON
│   └── restaurante_servicio.py  # Lógica de negocio del restaurante
├── ui/
│   ├── __init__.py
│   ├── login_view.py            # Vista de autenticación
│   └── main_view.py             # Vista principal con tabs
├── main.py                       # Punto de entrada de la aplicación
└── README.md                     # Este archivo
```

## Descripción de Componentes

### Modelos (`modelos/`)

- **Producto**: Representa un producto del restaurante con atributos como nombre, precio, cantidad disponible y descripción.
- **Usuario**: Representa un usuario del sistema con información de autenticación y rol.

### Servicios (`servicios/`)

- **ArchivoServicio**: Responsable de cargar datos desde los archivos JSON (`productos.json` y `usuarios.json`).
- **RestauranteServicio**: Concentra la lógica de negocio:
  - Validación de acceso de usuarios
  - Gestión de sesión actual
  - Consulta de productos y usuarios
  - Obtención de disponibilidad de productos

### Datos (`datos/`)

- **productos.json**: Almacena la información de productos registrados en la aplicación.
- **usuarios.json**: Almacena la información de usuarios para la simulación de acceso.

### Vistas UI (`ui/`)

- **LoginView**: Presenta una pantalla de autenticación con campos para usuario y contraseña.
- **MainView**: Panel principal con tres tabs:
  - **Productos**: Listado de productos registrados con precio y stock
  - **Usuarios**: Listado de usuarios registrados con rol
  - **Ventas**: Sección pendiente (identificada como funcionalidad futura)

### Punto de Entrada (`main.py`)

- Crea la ventana principal de Tkinter
- Inicializa los servicios
- Coordina el cambio entre vistas
- Gestiona el ciclo de vida de la aplicación

## Flujo de la Aplicación

```
Inicio (main.py)
    ↓
Inicialización de servicios
    ↓
LoginView (pantalla de acceso)
    ↓
Validación de credenciales
    ↓
RestauranteServicio.validar_acceso()
    ↓
✓ Acceso exitoso → MainView
✗ Acceso fallido → Mensaje de error en LoginView
    ↓
MainView (interfaz principal)
    ├── Tab Productos (lista cargada desde productos.json)
    ├── Tab Usuarios (lista cargada desde usuarios.json)
    └── Tab Ventas (pendiente)
    ↓
Cerrar Sesión
    ↓
LoginView (regresa)
    ↓
Ciclo repetido
```

## Instrucciones de Ejecución

### Requisitos
- Python 3.7 o superior
- Tkinter (incluido con Python)

### Pasos para ejecutar

1. **Ubicarse en la carpeta del proyecto**:
   ```bash
   cd restaurante_app
   ```

2. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```

3. **Interfaz inicial**:
   - Se abrirá una ventana de acceso
   - Los campos vacíos o credenciales incorrectas mostrarán un mensaje de error
   - Ingrese credenciales válidas:
     - **Usuario**: `juan` | **Contraseña**: `123456`
     - **Usuario**: `maria` | **Contraseña**: `123456`
     - **Usuario**: `carlos` | **Contraseña**: `123456`
     - O cualquier otro usuario registrado en `datos/usuarios.json`

4. **Navegación en la aplicación**:
   - Después de acceder, verá la interfaz principal con las tres tabs
   - Seleccione "Productos" para ver los productos disponibles
   - Seleccione "Usuarios" para ver los usuarios registrados
   - Haga clic en "Cerrar Sesión" para volver al login

## Criterios de Funcionamiento Verificados

✓ La aplicación inicia sin errores  
✓ Se muestra primero la pantalla de acceso  
✓ Los campos permiten ingresar usuario y contraseña  
✓ Campos vacíos producen un mensaje de error  
✓ Credenciales incorrectas producen un mensaje visual  
✓ Credenciales válidas muestran la interfaz principal  
✓ La tab "Productos" carga datos desde `productos.json` mediante `RestauranteServicio`  
✓ La tab "Usuarios" carga datos desde `usuarios.json` mediante `RestauranteServicio`  
✓ Las vistas consultan `RestauranteServicio` y no leen directamente JSON  
✓ La opción "Cerrar Sesión" regresa al login dentro de la misma ventana  

## Nota Importante

Esta es una versión base simplificada para comprender los fundamentos de interfaces gráficas en una arquitectura modular. Las funcionalidades completas del restaurante (como ventas, reportes, etc.) se implementarán progresivamente en futuras semanas.

El acceso es una simulación pedagógica y **no representa un sistema real de autenticación segura**.

## Autora

Adriana Arias - Programación Orientada a Objetos (POO)  
Semana 13 - Conceptos fundamentales de interfaces gráficas de usuario
