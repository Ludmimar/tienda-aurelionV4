# 🚀 INICIO RÁPIDO - TIENDA AURELION

## ⚡ Ejecución Inmediata

> ⚠️ **IMPORTANTE**: Ejecuta estos comandos desde la carpeta raíz `Entregable/`

### 1️⃣ Ejecutar el Programa Python (Consola)

```bash
python programas/tienda_aurelion.py
```

**Requisito:** Python 3.6 o superior

### 2️⃣ Ejecutar Aplicación Web (Streamlit) ⭐ RECOMENDADO

```bash
# Instalar primero (solo una vez)
pip install streamlit pandas numpy matplotlib seaborn scipy

# Ejecutar la app web
streamlit run programas/app_streamlit.py
```

**Se abrirá automáticamente en tu navegador:** `http://localhost:8501`

### 3️⃣ Ejecutar Notebook (Jupyter)

```bash
# Instalar primero (solo una vez)
pip install jupyter

# Abrir el notebook principal
jupyter notebook programas/tienda_aurelion.ipynb
```

**También disponible:** Notebook de análisis estadístico completo
```bash
jupyter notebook programas/analisis_estadistico.ipynb
```

### 4️⃣ Ejecutar Análisis Estadístico (Sprint 2) ⭐ NUEVO

```bash
# Instalar dependencias (solo una vez)
pip install pandas numpy matplotlib seaborn scipy

# Ejecutar análisis completo
python programas/analisis_estadistico.py
```

Esto generará:
- Análisis completo en consola
- 3 gráficos profesionales en `graficos/`
- Documentación completa del análisis

### 5️⃣ Ejecutar Análisis Estadístico en Jupyter ⭐ NUEVO RECOMENDADO

```bash
# Instalar dependencias (solo una vez)
pip install pandas numpy matplotlib seaborn scipy jupyter

# Abrir el notebook de análisis estadístico
jupyter notebook programas/analisis_estadistico.ipynb
```

**Ventajas del Notebook:**
- ✅ Ejecución celda por celda
- ✅ Visualización interactiva de resultados
- ✅ Gráficos integrados en el documento
- ✅ Documentación completa del análisis
- ✅ Ideal para presentaciones y reportes

**Contenido del Notebook:**
1. Carga de datos desde los 4 archivos CSV
2. Estadísticas descriptivas básicas
3. Identificación de distribuciones
4. Análisis de correlaciones
5. Detección de outliers
6. 3 gráficos representativos
7. Resumen ejecutivo e interpretación

---

### 6️⃣ Dashboard Power BI ⭐⭐ NUEVO

#### Opción A: Usar Dashboard Ya Creado (Instantáneo)

```bash
# El archivo está listo en:
Sprint-2/Tienda_Aurelion_Dashboard_Sprint2.pbix
```

**Pasos para abrirlo:**
1. Descarga [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Gratis)
2. Doble click en el archivo `.pbix`
3. ¡Listo! El dashboard se abrirá con todos los datos

**También desde Streamlit:**
```bash
streamlit run programas/app_streamlit.py
# Ve a la página "📊 Dashboard Power BI" y descárgalo
```

#### Opción B: Crear Dashboard Desde Cero (30 minutos)

```bash
# 1. (Opcional) Valida los datos
python programas/validar_datos_powerbi.py

# 2. Abre la guía
# Archivo: documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md

# 3. Todos los recursos listos en: Power BI/
```

**El dashboard incluye:**
- 📄 **Página 1 - Overview**: 5 KPIs, gráficos de productos, alertas de stock
- 📄 **Página 2 - Ventas y Clientes**: Evolución temporal, top productos vendidos
- 🎨 **Diseño medieval**: Colores dorados, rojo oscuro, azul marino
- 🔗 **Interactividad completa**: Cross-filtering automático

**Guías disponibles:**
- 🎯 `documentacion/COMO_CREAR_DASHBOARD_POWERBI.md` - Guía maestra
- 🚀 `documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md` - Paso a paso (30 min)
- ✅ `documentacion/CHECKLIST_DASHBOARD.md` - Lista de verificación
- 🎨 `documentacion/LAYOUT_VISUAL_DASHBOARD.md` - Vista previa visual

---

## 📁 Archivos del Proyecto

**📁 Estructura Organizada:**

```
Entregable/
├── 📄 README.md, INSTRUCCIONES.md, INICIO_RAPIDO.md, RESUMEN_FINAL.md
├── 📁 datos/ → productos.csv, clientes.csv, ventas.csv, detalle_ventas.csv
├── 📁 programas/ → tienda_aurelion.py, app_streamlit.py, tienda_aurelion.ipynb, analisis_estadistico.py, analisis_estadistico.ipynb ⭐
├── 📁 graficos/ → Gráficos generados automáticamente
└── 📁 documentacion/ → Guías, pseudocódigo, análisis estadístico
```

| Carpeta/Archivo | Descripción |
|-----------------|-------------|
| **📁 datos/** | Base de datos CSV (4 archivos normalizados) |
| **📁 programas/** | 6 versiones del sistema (consola, web, notebooks, análisis, validador) |
| **📁 documentacion/** | Todas las guías y documentación técnica |
| **📁 Power BI/** | Queries M, medidas DAX, tema JSON, recursos dashboard ⭐ |
| **📁 graficos/** | Gráficos estadísticos generados automáticamente |
| **📄 README.md** | Documentación completa del proyecto ⭐ |
| **📄 INSTRUCCIONES.md** | Guía detallada de uso |
| **📄 INICIO_RAPIDO.md** | Este archivo - Guía rápida |
| **📄 RESUMEN_FINAL.md** | Resumen ejecutivo |
| **📄 requirements.txt** | Dependencias para instalar |
| **📄 Tienda_Aurelion_Dashboard_Sprint2.pbix** | Dashboard Power BI listo ⭐⭐ |
| **📄 documentacion/GUIA_RAPIDA_DASHBOARD_POWERBI.md** | Paso a paso para crear dashboard (30 min) ⭐ |

---

## 🎯 Menú del Programa

Cuando ejecutes el programa verás estas opciones:

```
╔══════════════════════════════════════════════════╗
║              MENÚ PRINCIPAL                      ║
╠══════════════════════════════════════════════════╣
║  🔍 CONSULTAS Y BÚSQUEDAS                        ║
║     1. Listar todos los productos                ║
║     2. Buscar por categoría                      ║
║     3. Buscar por ID                             ║
║     4. Buscar por nombre                         ║
║     5. Buscar por rango de precios               ║
║     6. Ver productos con bajo stock              ║
║     7. Ver estadísticas del inventario           ║
║     8. Buscar por proveedor                      ║
╠══════════════════════════════════════════════════╣
║  ✏️  GESTIÓN DE INVENTARIO                       ║
║     9. Agregar nuevo producto                    ║
║    10. Actualizar stock de producto              ║
╠══════════════════════════════════════════════════╣
║     0. Salir del sistema                         ║
╚══════════════════════════════════════════════════╝
```

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Ver Estadísticas
1. Ejecuta el programa
2. Presiona Enter en el mensaje inicial
3. Selecciona opción **7**
4. Verás: total productos, valor inventario, precios, stock, etc.

### Ejemplo 2: Buscar Productos de una Categoría
1. Selecciona opción **2**
2. Ingresa una categoría, por ejemplo: `Armas`
3. Verás todos los productos de esa categoría

### Ejemplo 3: Identificar Productos con Stock Bajo
1. Selecciona opción **6**
2. Verás productos con ≤20 unidades (requieren reabastecimiento)

### Ejemplo 4: Agregar Nuevo Producto
1. Selecciona opción **9**
2. Ingresa los datos solicitados
3. Confirma para guardar

### Ejemplo 5: Ejecutar Análisis Estadístico en Jupyter ⭐ NUEVO
1. Abre el notebook: `jupyter notebook programas/analisis_estadistico.ipynb`
2. Ejecuta las celdas en orden (Shift + Enter)
3. Visualiza los gráficos integrados en el documento
4. Revisa el resumen ejecutivo al final

---

## 📊 Datos de Ejemplo

### Categorías Disponibles
- Armas
- Armaduras
- Pociones
- Accesorios
- Consumibles
- Capas
- Calzado
- Escudos
- Libros
- Municiones

### Proveedores
- Forja Celestial
- Herrería Dragón
- Alquimia Místika
- Artesanía Élfica
- Zapatería Rápida
- Joyería Arcana
- Tejeduría Sombría
- Scriptorium Mágico
- Biblioteca Arcana
- Forja Sombría

### Productos Destacados
- **Más caro:** Gema de Resurrección (5,000 monedas)
- **Más económico:** Flechas Mágicas (25 monedas)
- **Más stock:** Flechas Mágicas (500 unidades)
- **Stock bajo:** Gema de Resurrección (3 unidades) ⚠️

---

## 🔧 Solución de Problemas

### Error: "No se encontró el archivo"
**Solución:** Asegúrate de que los archivos CSV están en la carpeta `datos/`:
- `productos.csv`
- `clientes.csv`
- `ventas.csv`
- `detalle_ventas.csv`

### Error: "python no se reconoce"
**Solución:** 
- Instala Python desde [python.org](https://www.python.org)
- O intenta: `python3 tienda_aurelion.py`
- En Windows: `py tienda_aurelion.py`

### El programa se cierra inmediatamente
**Solución:** Ábrelo desde terminal/cmd, no haciendo doble clic

---

## 📚 ¿Qué Leer Primero?

### Si quieres entender el proyecto completo:
1. **INDICE_PROYECTO.md** - Visión general
2. **README.md** - Documentación principal

### Si quieres ejecutar el programa:
1. **Este archivo** (INICIO_RAPIDO.md)
2. Ejecuta: `python tienda_aurelion.py`

### Si vas a crear el dashboard:
1. **GUIA_POWER_BI.md**

### Si vas a presentar:
1. **GUIA_PRESENTACION.md**

### Si quieres ver la lógica del código:
1. **PSEUDOCODIGO_Y_DIAGRAMAS.md**

### Si quieres realizar análisis estadístico completo:
1. **analisis_estadistico.ipynb** - Notebook interactivo ⭐ RECOMENDADO
2. **analisis_estadistico.py** - Script Python
3. **documentacion/ANALISIS_ESTADISTICO.md** - Documentación del análisis

---

## ✅ Checklist Pre-Entrega

- [ ] Todos los archivos están en la carpeta
- [ ] El programa Python ejecuta sin errores
- [ ] Has probado al menos 3 funcionalidades
- [ ] Has ejecutado el análisis estadístico (script o notebook) ⭐
- [ ] Has revisado los gráficos generados en `graficos/`
- [ ] Has leído el README.md completo
- [ ] Has preparado tu presentación
- [ ] Has creado el dashboard en Power BI (opcional)
- [ ] Has organizado los archivos en Drive
- [ ] Tienes el link para compartir

---

## 🎯 Comandos Útiles

### Windows
```cmd
# Navegar a la carpeta
cd "D:\IBM\SPRINT 1 - INTRO A LA INTELIGENCIA ARTIFICIAL\Entregable"

# Ejecutar programa
python tienda_aurelion.py

# Ver contenido de la carpeta
dir

# Ver contenido del CSV
type tienda_aurelion.csv

# Ejecutar análisis estadístico
python programas/analisis_estadistico.py

# Abrir notebook de análisis estadístico
jupyter notebook programas/analisis_estadistico.ipynb
```

### Linux/Mac
```bash
# Navegar a la carpeta
cd "/ruta/a/tu/carpeta/Entregable"

# Ejecutar programa
python3 tienda_aurelion.py

# Ver contenido de la carpeta
ls -la

# Ver contenido del CSV
cat tienda_aurelion.csv

# Ejecutar análisis estadístico
python3 programas/analisis_estadistico.py

# Abrir notebook de análisis estadístico
jupyter notebook programas/analisis_estadistico.ipynb
```

---

## 🆘 Necesitas Ayuda?

1. **Error técnico:** Revisa el archivo README.md sección "Instrucciones de Uso"
2. **Dudas de Power BI:** Lee GUIA_POWER_BI.md
3. **Preparar presentación:** Lee GUIA_PRESENTACION.md
4. **Entender el código:** Lee PSEUDOCODIGO_Y_DIAGRAMAS.md

---

## 🎓 Objetivos de Aprendizaje

Al completar este proyecto habrás:
- ✅ Estructurado datos para análisis
- ✅ Desarrollado un programa funcional en Python
- ✅ Implementado algoritmos de búsqueda
- ✅ Creado visualizaciones de datos
- ✅ Documentado un proyecto técnico
- ✅ Preparado una presentación profesional

---

## 🌟 Tips Finales

1. **Explora el programa:** Prueba todas las opciones del menú
2. **Lee los comentarios:** El código está bien documentado
3. **Personaliza:** Siéntete libre de agregar productos o modificar
4. **Practica la presentación:** Ensaya al menos 3 veces
5. **Haz preguntas:** Es mejor preguntar que adivinar

---

**¡Todo listo! Ahora tienes un proyecto completo y profesional para tu entrega. 🚀⚔️**

---

## 📞 Estructura de Entrega en Drive

```
📁 Carpeta compartida: "Tienda Aurelion - [Tu Nombre]"
│
├── 📄 INICIO_RAPIDO.md (este archivo - ¡Léeme primero!)
├── 📄 INDICE_PROYECTO.md
├── 📄 README.md
├── 📄 ANALISIS_ESTADISTICO.md ⭐
├── 📄 PSEUDOCODIGO_Y_DIAGRAMAS.md
├── 📄 SUGERENCIAS_COPILOT.md
├── 📄 GUIA_POWER_BI.md
├── 📄 GUIA_PRESENTACION.md
├── 📁 datos/
│   ├── productos.csv
│   ├── clientes.csv
│   ├── ventas.csv
│   └── detalle_ventas.csv
├── 📁 programas/
│   ├── tienda_aurelion.py
│   ├── app_streamlit.py
│   ├── tienda_aurelion.ipynb
│   ├── analisis_estadistico.py ⭐
│   └── analisis_estadistico.ipynb ⭐⭐ NUEVO
├── 📁 graficos/ ⭐
│   └── (gráficos generados automáticamente)
└── 📊 tienda_aurelion.pbix (si creaste el dashboard)
```

**Link para compartir:** [Genera el link de tu carpeta de Drive y compártelo]

---

**Autor:** Martos Ludmila  
**DNI:** 34811650  
**Sprint:** 2 - Introducción a la Inteligencia Artificial  
**Institución:** IBM  
**Fecha de creación:** Octubre 2025  
**Versión:** 2.0

---

¡Éxito en tu entrega! 🎉

