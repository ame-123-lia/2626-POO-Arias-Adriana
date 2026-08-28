# Instrucciones para Crear Repositorio GitHub

## Pasos para Crear un Nuevo Repositorio Público en GitHub

### 1. En GitHub (web)
1. Ve a https://github.com/new
2. Completa los detalles:
   - **Repository name:** `2626-POO-Arias-Adriana-Semana11`
   - **Description:** "Restaurante App - Semana 11: Relaciones Usuario-Producto, Ventas, Stock y Persistencia JSON"
   - **Visibility:** Público ✓
   - **Initialize with README:** NO (usaremos el nuestro)
3. Click "Create repository"
4. Copia la URL del repositorio (ej: `https://github.com/tu-usuario/2626-POO-Arias-Adriana-Semana11.git`)

### 2. En tu computadora (local)
```bash
# Navega a la carpeta SEMANA 11
cd c:\Users\User\OneDrive\Escritorio\2626-POO-Arias-Adriana\PARCIAL2\SEMANA 11

# Inicializa git (si no está ya inicializado)
git init

# Configura usuario y correo (reemplaza con los datos reales)
git config user.name "Adriana Arias"
git config user.email "tu-email@example.com"

# Agrega todos los archivos
git add .

# Crea el commit inicial
git commit -m "Restaurante App Semana 11: Ventas, Stock y Persistencia JSON

- Agregar atributo stock a Producto
- Crear clase Venta para representar relación Usuario-Producto
- Implementar operación vender_producto() con validaciones
- Completar persistencia JSON para productos, usuarios y ventas
- Implementar consulta de ventas por usuario
- Todos los modelos con métodos to_dict() y from_dict()
- 8/8 pruebas automatizadas pasadas

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"

# Agrega el repositorio remoto
git remote add origin https://github.com/tu-usuario/2626-POO-Arias-Adriana-Semana11.git

# Crea y cambia a rama main (si necesario)
git branch -M main

# Hace push al repositorio
git push -u origin main
```

### 3. Verifica en GitHub
1. Ve a tu repositorio en https://github.com/tu-usuario/2626-POO-Arias-Adriana-Semana11
2. Verifica que ves:
   - ✓ Carpeta `restaurante_app/` con modelos, servicios, main.py
   - ✓ Carpeta `datos/` con JSON files
   - ✓ `README.md` con documentación
   - ✓ `test_run.py` con pruebas
   - ✓ `.gitignore` configurado

## Checklist Final Antes de Entregar

- [ ] Repositorio público en GitHub
- [ ] README.md completo con:
  - [ ] Nombre de estudiante
  - [ ] Descripción del sistema
  - [ ] Estructura del proyecto
  - [ ] Responsabilidades de cada componente
  - [ ] Funcionamiento del stock
  - [ ] Relación Usuario-Producto mediante Venta
  - [ ] Excepciones controladas
  - [ ] Instrucciones de ejecución
- [ ] Proyecto con estructura correcta:
  - [ ] modelos/producto.py con stock
  - [ ] modelos/usuario.py con from_dict()
  - [ ] modelos/venta.py (NUEVA)
  - [ ] servicios/restaurante.py con vender_producto()
  - [ ] servicios/archivo_servicio.py con 3 archivos
  - [ ] main.py con menú actualizado
  - [ ] datos/ con productos.json, usuarios.json, ventas.json
- [ ] Pruebas ejecutadas y pasadas (8/8)
- [ ] Funcionamiento verificado

## Enlace a Entregar

Proporciona este enlace a tu profesor:
```
https://github.com/tu-usuario/2626-POO-Arias-Adriana-Semana11
```

---

**Nota:** Recuerda cambiar "tu-usuario" por tu nombre de usuario real en GitHub.
