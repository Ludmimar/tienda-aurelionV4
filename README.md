# 🌟 Tienda Aurelion - Sistema de Gestión de Inventario

**Sprint 4 - Power BI: Medidas, KPIs y Análisis Temporal - IBM**

> 💡 **Proyecto completo con Power BI:** Dashboard profesional con medidas DAX, KPIs, análisis temporal, Machine Learning, Aplicación Web Online, Consola Python, Aplicación Web Local, Jupyter Notebook y Análisis Estadístico

---

## 🌐 Acceso Directo a la Aplicación Web

**¡Prueba la aplicación directamente en tu navegador sin instalaciones!**

🔗 **[👉 Acceder a la Aplicación Web](https://tienda-aurelionv4.streamlit.app/)**

> ✨ **Incluye:** Gestión de productos, clientes y ventas | Análisis estadístico completo | Gráficos interactivos | Dashboard profesional

---

## 📋 Índice
0. [⚡ Inicio Rápido](#inicio-rápido) ← **Empieza aquí**
1. [📊 Power BI Dashboard](#power-bi-dashboard) ← **NUEVO - Sprint 4**
2. [🤖 Machine Learning](#machine-learning) ← **Sprint 3**
3. [Tema, Problema y Solución](#tema-problema-y-solución)
4. [Fuente de Datos](#fuente-de-datos)
5. [Definición y Estructura de Datos](#definición-y-estructura-de-datos)
6. [Tipos y Escala de Datos](#tipos-y-escala-de-datos)
7. [Desarrollo del Programa](#desarrollo-del-programa)
8. [Sugerencias de Copilot](#sugerencias-de-copilot)
9. [Instrucciones de Uso](#instrucciones-de-uso) ← **Guía completa**
10. [Información del Proyecto](#información-del-proyecto)
11. [Notas Adicionales](#notas-adicionales)


---

## ⚡ Inicio Rápido

### 🌐 Opción 1: Aplicación Web Online ⭐⭐ RECOMENDADO (Sin instalaciones)

**¡Prueba la aplicación directamente en tu navegador!**

🔗 **[Acceder a la Aplicación Web](https://tienda-aurelionv4.streamlit.app/)**

> ✨ **Ventajas:** No requiere instalación, funciona inmediatamente, siempre actualizada

---

### 🖥️ Opción 2: Programa de Consola (Sin instalaciones)
```bash
python programas/tienda_aurelion.py
```

### 🌐 Opción 3: Aplicación Web Local ⭐ RECOMENDADO
```bash
# Instalar dependencias (solo primera vez)
pip install streamlit pandas numpy matplotlib seaborn scipy

# Ejecutar la aplicación web
streamlit run programas/app_streamlit.py
```
**Se abrirá automáticamente en tu navegador:** `http://localhost:8501`

> ⚠️ **IMPORTANTE**: Ejecuta estos comandos desde la carpeta raíz del proyecto

### 📓 Opción 4: Jupyter Notebook
```bash
# Instalar Jupyter (solo primera vez)
pip install jupyter

# Abrir el notebook
jupyter notebook programas/tienda_aurelion.ipynb
```

> 📘 **Para más detalles**, consulta [Instrucciones de Uso](#instrucciones-de-uso) o `INSTRUCCIONES.md`

---

## 📊 Power BI Dashboard

### 🎯 Dashboard Profesional con Medidas DAX y KPIs

**NUEVO en Sprint 4**: Dashboard completo en Power BI Desktop con medidas DAX avanzadas, KPIs con objetivos, análisis temporal, jerarquías y agrupaciones.

#### Características del Dashboard Sprint 4

- **11+ Medidas DAX** con diferentes tipos de función:
  - Funciones de Agregación: SUM, AVERAGE, COUNT, DISTINCTCOUNT, SUMX
  - Funciones de Filtro: CALCULATE, FILTER, VALUES
  - Funciones de Tiempo: DATEADD, DATESYTD, SAMEPERIODLASTYEAR
  - Funciones Lógicas: IF, SWITCH, VAR/RETURN
  - Funciones de Iteración: SUMX, AVERAGEX, COUNTROWS

- **3 KPIs Completos**:
  1. **Rotación de Inventario**: Valor actual, objetivo (2.5), estado
  2. **Margen de Utilidad**: Valor actual, objetivo (30%), estado
  3. **Nivel de Servicio**: Valor actual, objetivo (95%), estado

- **Análisis Temporal**:
  - Crecimiento Mes a Mes (MoM)
  - Variación Interanual (YoY)
  - Ventas YTD (Año a la fecha)

- **Jerarquías y Agrupaciones**:
  - Jerarquía de Tiempo: Año → Trimestre → Mes → Día
  - Jerarquía de Productos: Categoría → Proveedor → Producto
  - Agrupaciones por Rangos: Stock (Bajo/Medio/Alto), Valor (Bajo/Medio/Alto)

#### 🚀 Acceso al Dashboard

**Archivo**: `Power BI/Sprint4.pbix`

**Requisitos**:
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Gratis)

**Documentación Completa**:
- 📄 [Documentacion_Sprint4.md](./Power%20BI/Documentacion_Sprint4.md) - Documentación completa
- 📊 [Presentacion_Lectura_PowerBI.md](./Power%20BI/Presentacion_Lectura_PowerBI.md) - Cómo leer el dashboard
- ⭐ [Guia_Paso_a_Paso_Medidas_DAX.md](./Power%20BI/Guia_Paso_a_Paso_Medidas_DAX.md) - Crear medidas DAX
- 📋 [Codigo_DAX_Listo_Copiar.md](./Power%20BI/Codigo_DAX_Listo_Copiar.md) - Código listo para usar
- 💡 [Notebook_DAX_Ejemplos.md](./Power%20BI/Notebook_DAX_Ejemplos.md) - Ejemplos detallados
- 🐍 [procesamiento_datos.py](./Power%20BI/procesamiento_datos.py) - Script principal Python

#### 📊 Procesamiento de Datos

El proyecto incluye un script Python principal para procesar datos:

```bash
cd "Power BI"
python procesamiento_datos.py
```

**Funcionalidades**:
- ✅ Carga de datos desde CSV
- ✅ Cálculo de métricas básicas
- ✅ Análisis de rotación de inventario
- ✅ Cálculo de margen de utilidad
- ✅ Análisis temporal (MoM, YoY)
- ✅ Creación de agrupaciones
- ✅ Generación de archivos CSV procesados

**Resultados**: Se guardan en `Power BI/resultados/`

---

## 🤖 Machine Learning

### 🎯 Modelo de Predicción de Ventas

**NUEVO en Sprint 3**: Modelo de Machine Learning para predecir el total de ventas basado en características de productos y patrones de compra.

#### Características del Modelo

- **Tipo**: Regresión supervisada
- **Algoritmo**: Random Forest Regressor (100 árboles)
- **Objetivo**: Predecir el monto total de una venta
- **Variables de entrada**: 
  - Cantidad de productos
  - Precio promedio
  - Categorías de productos
  - Temporalidad (mes, día de la semana)
- **Métricas**: MAE, RMSE, R², MAPE

#### 🚀 Ejecutar el Modelo

**Machine Learning está disponible en TODAS las aplicaciones:**

| Aplicación | Comando | ML Incluido |
|------------|---------|:-----------:|
| **Consola Python** | `python programas/tienda_aurelion.py` (opciones 16-17) | ✅ |
| **App Web Streamlit** | `streamlit run programas/app_streamlit.py` | ✅ |
| **Jupyter Notebook** | `jupyter notebook programas/tienda_aurelion.ipynb` | ✅ |
| **Análisis Estadístico** | `jupyter notebook programas/analisis_estadistico.ipynb` | ✅ |
| **Script ML Standalone** | `python programas/modelo_ml_ventas.py` | ✅ |

```bash
# Instalar dependencias (solo primera vez)
pip install pandas numpy matplotlib seaborn scikit-learn

# Opción 1: Ejecutar modelo ML standalone
python programas/modelo_ml_ventas.py

# Opción 2: Usar ML en la consola interactiva
python programas/tienda_aurelion.py
# Luego seleccionar opción 16 (Entrenar modelo) o 17 (Predecir venta)

# Opción 3: Usar ML en la app web
streamlit run programas/app_streamlit.py
# Ir a la sección "🤖 Machine Learning"
```

**Salidas generadas**:
- ✅ Métricas de evaluación (R², MAE, RMSE, MAPE)
- ✅ Importancia de características
- ✅ Predictor interactivo (consola y web)
- ✅ 4 gráficos profesionales en `graficos/`

#### 📊 Resultados Esperados

- **R² Score**: ~0.70-0.85 (modelo explica 70-85% de variabilidad)
- **MAE**: ~300-450 monedas (error promedio)
- **MAPE**: ~20-30% (error porcentual)

#### 📚 Documentación Completa

Para información técnica detallada, consulta:
- 📄 [MODELO_ML.md](./documentacion/MODELO_ML.md) - Documentación completa del modelo
  - Objetivo y justificación del algoritmo
  - Descripción de entradas (X) y salida (y)
  - Proceso de división train/test
  - Métricas de evaluación
  - Interpretación de resultados
  - Conclusiones y recomendaciones

---


## 🎯 Tema, Problema y Solución

### Tema
**Sistema de Gestión de Inventario para Tienda de Fantasía Medieval**

La Tienda Aurelion es un comercio especializado en artículos mágicos y de aventura en un mundo de fantasía. Necesita un sistema eficiente para gestionar su inventario de productos.

### Problema
La tienda enfrenta los siguientes desafíos:
- **Gestión manual ineficiente**: El registro de productos, ventas y stock se realiza en papel, causando errores y pérdida de tiempo
- **Falta de visibilidad**: No hay forma rápida de consultar disponibilidad de productos o buscar por categorías
- **Control de stock deficiente**: No se puede identificar rápidamente qué productos tienen bajo inventario
- **Análisis limitado**: No hay capacidad para analizar tendencias de precios, categorías más populares o proveedores

### Solución
Desarrollo de un **Sistema Interactivo de Gestión de Inventario** implementado en **3 versiones diferentes**:

#### 🖥️ **Versión 1: Consola Python** (`tienda_aurelion.py`)
- Programa interactivo de línea de comandos
- Sin dependencias externas (solo Python estándar)
- 10 funcionalidades principales
- Interfaz de texto amigable con emojis

#### 🌐 **Versión 2: Aplicación Web Streamlit** (`app_streamlit.py`) ⭐
- Interfaz web profesional en el navegador
- **Disponible online:** [https://tienda-aurelionv4.streamlit.app/](https://tienda-aurelionv4.streamlit.app/) ⭐⭐
- Gráficos interactivos en tiempo real
- Filtros dinámicos (sliders, dropdowns)
- Dashboard visual completo
- Gestión de inventario desde la interfaz
- Análisis estadístico completo integrado con descripciones detalladas

#### 📓 **Versión 3: Jupyter Notebook** (`tienda_aurelion.ipynb`)
- Documentación interactiva con código ejecutable
- Explicaciones paso a paso
- Visualización de resultados en cada celda
- Ideal para presentaciones educativas

**Funcionalidades comunes a todas las versiones:**
- ✅ Consultar productos por diferentes criterios (ID, nombre, categoría, rango de precios)
- ✅ Visualizar estadísticas del inventario (productos más caros, stock total, categorías)
- ✅ Identificar productos con bajo stock para reabastecimiento
- ✅ Buscar productos por proveedor
- ✅ Agregar nuevos productos al inventario
- ✅ Actualizar stock existente
- ✅ Gestión completa de clientes (listar, estadísticas)
- ✅ Sistema de ventas (historial, detalles, estadísticas)
- ✅ Análisis estadístico completo (Sprint 2)

---

## 📊 Fuente de Datos

### Origen
Los datos provienen de la **base de datos histórica de la Tienda Aurelion**, recopilada durante los últimos 2 años de operación comercial.

### Método de Recolección
- Registro de productos ingresados al inventario
- Información proporcionada por proveedores
- Clasificación manual por categorías de producto
- Actualización continua de precios y stock

### Almacenamiento
Los datos se almacenan en formato **CSV (Comma-Separated Values)** en **4 archivos normalizados**, lo que permite:
- Fácil lectura y escritura
- Compatibilidad con múltiples herramientas (Excel, Python, bases de datos)
- Portabilidad y respaldo sencillo
- Bajo consumo de recursos
- Estructura normalizada para análisis avanzados

**Archivos de base de datos:**
- `productos.csv` - 80 productos con información completa
- `clientes.csv` - 50 clientes registrados
- `ventas.csv` - 100 ventas realizadas
- `detalle_ventas.csv` - 273 detalles de productos vendidos

---

## 🗂️ Definición y Estructura de Datos

### Estructura del Dataset

La base de datos contiene **4 tablas relacionadas** con información completa:

#### Tabla PRODUCTOS (21 registros)
Campos: id, nombre, categoria, precio, stock, descripcion, proveedor

#### Tabla CLIENTES (15 registros)
Campos: id, nombre, email, telefono, ciudad, fecha_registro

#### Tabla VENTAS (20 registros)
Campos: id_venta, id_cliente, fecha, total

#### Tabla DETALLE_VENTAS (31 registros)
Campos: id_detalle, id_venta, id_producto, cantidad, precio_unitario, subtotal

### Relaciones entre Tablas

- `ventas.id_cliente` → `clientes.id`
- `detalle_ventas.id_venta` → `ventas.id_venta`
- `detalle_ventas.id_producto` → `productos.id`

---

## 📐 Tipos y Escala de Datos

### Tipos de Datos por Campo

| Campo | Tipo de Dato | Tipo Python | Rango/Características |
|-------|--------------|-------------|----------------------|
| **id** | Numérico entero | `int` | 1 - 20 (autoincremental) |
| **nombre** | Texto/String | `str` | 10-30 caracteres |
| **categoria** | Texto categórico | `str` | 10 categorías únicas |
| **precio** | Numérico entero | `int` | 25 - 5000 monedas |
| **stock** | Numérico entero | `int` | 3 - 500 unidades |
| **descripcion** | Texto largo | `str` | 20-50 caracteres |
| **proveedor** | Texto categórico | `str` | 9 proveedores únicos |

### Escala de Datos

#### Escala Actual
- **Registros totales**: 
  - 80 productos
  - 50 clientes
  - 100 ventas
  - 273 detalles de ventas
- **Tamaño total de archivos**: ~3 KB
- **Categorías**: 10 diferentes
- **Proveedores**: 10 diferentes
- **Rango de precios**: 25 - 5000 monedas
- **Stock total**: 4,585 unidades
- **Ingresos totales**: 231,485 monedas
- **Valor inventario**: 1,909,400 monedas

#### Escalabilidad
El sistema está diseñado para escalar hasta:
- ✅ 10,000+ productos
- ✅ 100+ categorías
- ✅ 50+ proveedores
- ✅ Archivos de hasta 10 MB
- ✅ Tiempo de búsqueda < 1 segundo

### Clasificación de Variables

**Variables Cuantitativas (Numéricas)**:
- `precio` - Cuantitativa continua (discreta en práctica)
- `stock` - Cuantitativa discreta
- `id` - Cuantitativa discreta

**Variables Cualitativas (Categóricas)**:
- `nombre` - Nominal
- `categoria` - Nominal
- `descripcion` - Nominal (texto libre)
- `proveedor` - Nominal

---

## 💻 Desarrollo del Programa

### Pasos del Desarrollo

#### Paso 1: Análisis de Requisitos
- Identificar necesidades del usuario
- Definir funcionalidades principales
- Establecer estructura de datos

#### Paso 2: Diseño del Sistema
- Diseñar estructura de menú interactivo
- Planificar funciones de consulta y análisis
- Definir validaciones de entrada

#### Paso 3: Implementación
- Crear funciones de carga de datos (CSV)
- Implementar funciones de búsqueda y filtrado
- Desarrollar estadísticas y análisis
- Construir interfaz de usuario interactiva

#### Paso 4: Pruebas
- Probar cada funcionalidad
- Validar manejo de errores
- Verificar integridad de datos

#### Paso 5: Documentación
- Documentar código con comentarios
- Crear manual de usuario
- Preparar ejemplos de uso

### Pseudocódigo

```
INICIO PROGRAMA

// Cargar datos
FUNCIÓN cargar_datos(archivo_csv)
    productos = []
    ABRIR archivo_csv
    PARA cada línea en archivo
        producto = convertir_línea_a_diccionario()
        AGREGAR producto a productos
    FIN PARA
    RETORNAR productos
FIN FUNCIÓN

// Función principal de menú
FUNCIÓN mostrar_menu()
    MIENTRAS usuario_no_salga HACER
        MOSTRAR opciones de menú
        opción = LEER entrada_usuario
        
        SEGÚN opción:
            CASO 1: listar_todos_productos()
            CASO 2: buscar_por_categoria()
            CASO 3: buscar_por_id()
            CASO 4: buscar_por_nombre()
            CASO 5: buscar_por_rango_precios()
            CASO 6: productos_bajo_stock()
            CASO 7: estadisticas_inventario()
            CASO 8: buscar_por_proveedor()
            CASO 9: agregar_producto()
            CASO 10: actualizar_stock()
            CASO 0: SALIR
            OTRO: mensaje_error()
        FIN SEGÚN
    FIN MIENTRAS
FIN FUNCIÓN

// Buscar por categoría
FUNCIÓN buscar_por_categoria(productos, categoria_buscar)
    resultados = []
    PARA cada producto en productos
        SI producto.categoria == categoria_buscar ENTONCES
            AGREGAR producto a resultados
        FIN SI
    FIN PARA
    MOSTRAR resultados
FIN FUNCIÓN

// Calcular estadísticas
FUNCIÓN estadisticas_inventario(productos)
    total_productos = CONTAR(productos)
    valor_total = SUMAR(producto.precio * producto.stock)
    categorías = CONTAR_ÚNICAS(producto.categoria)
    stock_total = SUMAR(producto.stock)
    
    producto_más_caro = MÁXIMO(productos, clave=precio)
    producto_más_barato = MÍNIMO(productos, clave=precio)
    
    MOSTRAR todas_las_estadísticas
FIN FUNCIÓN

// Productos con bajo stock
FUNCIÓN productos_bajo_stock(productos, umbral=20)
    PARA cada producto en productos
        SI producto.stock <= umbral ENTONCES
            MOSTRAR producto con ALERTA
        FIN SI
    FIN PARA
FIN FUNCIÓN

// Agregar nuevo producto
FUNCIÓN agregar_producto(productos)
    LEER datos_nuevo_producto
    VALIDAR datos
    nuevo_id = MÁXIMO(producto.id) + 1
    CREAR nuevo_producto con nuevo_id
    AGREGAR nuevo_producto a productos
    GUARDAR en archivo_csv
    MENSAJE éxito
FIN FUNCIÓN

LLAMAR mostrar_menu()

FIN PROGRAMA
```

### Diagrama de Flujo

```
                    ┌─────────────┐
                    │   INICIO    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Cargar CSV  │
                    └──────┬──────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  Mostrar Menú         │
              │  1. Listar todos      │
              │  2. Por categoría     │
              │  3. Por ID            │
              │  4. Por nombre        │
              │  5. Por precio        │
              │  6. Bajo stock        │
              │  7. Estadísticas      │
              │  8. Por proveedor     │
              │  9. Agregar producto  │
              │ 10. Actualizar stock  │
              │  0. Salir             │
              └───────────┬────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Leer opción usuario  │
              └───────────┬───────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   ┌────────┐      ┌──────────┐      ┌──────────┐
   │Opción 1│      │Opción 2-8│      │Opción 9-10│
   │Listar  │      │Búsquedas │      │  Agregar/ │
   │        │      │Análisis  │      │Actualizar │
   └────┬───┘      └─────┬────┘      └─────┬────┘
        │                │                  │
        ▼                ▼                  ▼
   ┌────────┐      ┌──────────┐      ┌──────────┐
   │Mostrar │      │ Filtrar  │      │ Validar  │
   │Todos   │      │  Datos   │      │  Datos   │
   └────┬───┘      └─────┬────┘      └─────┬────┘
        │                │                  │
        │                ▼                  ▼
        │         ┌──────────┐      ┌──────────┐
        │         │ Mostrar  │      │ Guardar  │
        │         │Resultado │      │   CSV    │
        │         └─────┬────┘      └─────┬────┘
        │               │                  │
        └───────────────┴──────────────────┘
                        │
                        ▼
                ┌───────────────┐
                │ ¿Continuar?   │
                └───────┬───────┘
                        │
                 ┌──────┴──────┐
                 │             │
            SÍ   │             │  NO
                 ▼             ▼
         ┌────────────┐  ┌─────────┐
         │Volver Menú │  │   FIN   │
         └────────────┘  └─────────┘
```

---

## 🤖 Sugerencias de Copilot

### ✅ Sugerencias Aceptadas

1. **Uso de `csv.DictReader`**
   - **Sugerencia**: Utilizar `csv.DictReader` en lugar de `csv.reader` para acceder a columnas por nombre
   - **Razón**: Hace el código más legible y mantenible al usar nombres de columnas en lugar de índices numéricos
   - **Implementación**: Aceptada en función `cargar_datos()`

2. **Conversión de tipos de datos**
   - **Sugerencia**: Convertir 'precio' y 'stock' a `int` al cargar datos
   - **Razón**: Permite operaciones matemáticas y comparaciones correctas
   - **Implementación**: Aceptada con manejo de errores para datos inválidos

3. **Función de validación centralizada**
   - **Sugerencia**: Crear una función `validar_entrada_numerica()` reutilizable
   - **Razón**: Evita duplicación de código y centraliza validaciones
   - **Implementación**: Aceptada y usada en múltiples funciones

4. **Uso de f-strings para formateo**
   - **Sugerencia**: Usar f-strings para formateo de texto en lugar de `.format()` o `%`
   - **Razón**: Sintaxis más moderna, legible y eficiente en Python 3.6+
   - **Implementación**: Aceptada en todo el código

5. **Manejo de archivos con context manager**
   - **Sugerencia**: Usar `with open()` para manejo automático de cierre de archivos
   - **Razón**: Previene fugas de recursos y es más seguro
   - **Implementación**: Aceptada en todas las operaciones de archivo

6. **Separadores visuales en interfaz**
   - **Sugerencia**: Agregar líneas decorativas para mejorar legibilidad del menú
   - **Razón**: Mejora experiencia de usuario y organización visual
   - **Implementación**: Aceptada con caracteres Unicode

### ❌ Sugerencias Descartadas

1. **Uso de base de datos SQLite**
   - **Sugerencia**: Migrar de CSV a SQLite para mejor rendimiento
   - **Razón de descarte**: Para el tamaño actual del dataset (20 productos), CSV es suficiente y más simple. SQLite agregaría complejidad innecesaria
   - **Alternativa**: Se mantiene CSV con opción de migrar a futuro si escala

2. **Framework GUI (tkinter)**
   - **Sugerencia**: Crear interfaz gráfica con tkinter
   - **Razón de descarte**: El proyecto requiere específicamente una interfaz de consola interactiva. GUI requeriría más tiempo de desarrollo
   - **Alternativa**: Se mantiene interfaz de consola con menús claros

3. **Librería pandas para análisis**
   - **Sugerencia**: Usar pandas.DataFrame para manipulación de datos
   - **Razón de descarte**: Agrega dependencia externa innecesaria. Las operaciones requeridas se pueden hacer eficientemente con Python estándar
   - **Alternativa**: Uso de estructuras de datos nativas (listas y diccionarios)

4. **Autenticación de usuarios**
   - **Sugerencia**: Implementar sistema de login con diferentes roles (admin, vendedor)
   - **Razón de descarte**: Excede el alcance del proyecto actual. No es requisito del sprint
   - **Alternativa**: Sistema de gestión sin autenticación, enfocado en funcionalidad core

5. **Logging con módulo logging**
   - **Sugerencia**: Implementar registro de operaciones con el módulo `logging`
   - **Razón de descarte**: Para un programa educativo y de demostración, print statements son suficientes y más directos
   - **Alternativa**: Mensajes descriptivos con `print()`

6. **Expresiones regulares para validación**
   - **Sugerencia**: Usar regex para validar formatos de entrada
   - **Razón de descarte**: Las validaciones requeridas son simples (números, strings básicos). Regex agregaría complejidad innecesaria
   - **Alternativa**: Validaciones con métodos string estándar (`.isdigit()`, `.strip()`)

---

## 🚀 Instrucciones de Uso

> ⚠️ **IMPORTANTE**: Todos los comandos se ejecutan desde la carpeta raíz `Entregable/`

### 📁 Estructura del Proyecto

```
Entregable/
├── 📄 README.md                (este archivo)
├── 📄 INSTRUCCIONES.md         (guía detallada)
├── 📄 requirements.txt         (dependencias)
├── 📁 datos/
│   ├── productos.csv
│   ├── clientes.csv
│   ├── ventas.csv
│   ├── detalle_ventas.csv
│   └── tienda_aurelion.pbix (opcional - dashboard Power BI)
├── 📁 programas/
│   ├── tienda_aurelion.py      (consola)
│   ├── app_streamlit.py        (web)
│   ├── tienda_aurelion.ipynb    (notebook)
│   ├── analisis_estadistico.py  (análisis estadístico) ⭐
│   └── analisis_estadistico.ipynb  (notebook análisis estadístico) ⭐⭐
├── 📁 graficos/ ⭐
│   └── (gráficos generados automáticamente)
└── 📁 documentacion/
    └── (archivos de documentación)
```

---

### Opción 1: Programa de Consola (Básico)

**Requisitos:**
- Python 3.6 o superior

**Ejecución desde raíz:**
```bash
python programas/tienda_aurelion.py
```

**Ventajas:**
- ✅ Sin dependencias externas
- ✅ Rápido y simple
- ✅ Funciona en cualquier sistema con Python

---

### Opción 2: Aplicación Web Online ⭐⭐ RECOMENDADO (Sin instalaciones)

**Acceso directo:**
🔗 **[Acceder a la Aplicación Web Online](https://tienda-aurelionv4.streamlit.app/)**

**Ventajas:**
- ✅ Sin instalación requerida
- ✅ Funciona inmediatamente en cualquier navegador
- ✅ Siempre actualizada con la última versión
- ✅ Interfaz web profesional y moderna
- ✅ Gráficos interactivos en tiempo real
- ✅ Análisis estadístico completo integrado

---

### Opción 3: Aplicación Web Streamlit Local ⭐ RECOMENDADO

**Requisitos:**
- Python 3.6 o superior
- Streamlit y dependencias

**Instalación (solo primera vez):**
```bash
pip install streamlit pandas numpy matplotlib seaborn scipy
```

**Ejecución desde raíz:**
```bash
streamlit run programas/app_streamlit.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

**Ventajas:**
- ✅ Interfaz web profesional y moderna
- ✅ Gráficos interactivos en tiempo real
- ✅ Control total del código y datos
- ✅ Filtros dinámicos (sliders, dropdowns)
- ✅ Dashboard visual completo
- ✅ No requiere conocimientos técnicos para usar
- ✅ Ideal para presentaciones y demos

**Características de la App Web:**
- 🏠 **Página Inicio**: Dashboard con métricas y gráficos
- 🔍 **Explorar Productos**: Filtros avanzados y búsqueda
- 📊 **Estadísticas**: Análisis detallado por categoría/proveedor
- ✏️ **Gestionar**: Agregar productos y actualizar stock desde la interfaz

---

### Opción 4: Jupyter Notebook

**Requisitos:**
- Python 3.6 o superior
- Jupyter

**Instalación (solo primera vez):**
```bash
pip install jupyter
```

**Ejecución desde raíz:**
```bash
jupyter notebook programas/tienda_aurelion.ipynb
```

**Ventajas:**
- ✅ Documentación interactiva
- ✅ Código ejecutable paso a paso
- ✅ Explicaciones integradas
- ✅ Ideal para aprendizaje y presentaciones educativas

### Opción 4: Análisis Estadístico en Jupyter Notebook ⭐ NUEVO RECOMENDADO

**Requisitos:**
- Python 3.6 o superior
- Librerías científicas: pandas, numpy, matplotlib, seaborn, scipy

**Instalación (solo primera vez):**
```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

**Ejecución desde raíz:**
```bash
jupyter notebook programas/analisis_estadistico.ipynb
```

**Ventajas:**
- ✅ Ejecución celda por celda (interactivo)
- ✅ Visualización de resultados integrada
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

Si quieres instalar todo de una vez:
```bash
pip install -r requirements.txt
```

---

### Características Principales (Todas las Versiones)
- 🔍 Búsqueda por múltiples criterios
- 📊 Análisis estadístico del inventario
- ➕ Agregar nuevos productos
- 🔄 Actualizar stock existente
- ⚠️ Alertas de bajo stock
- 💾 Persistencia de datos en CSV

---

### 📚 Archivos de Documentación

Para más información, consulta:
- 📄 `INSTRUCCIONES.md` - Guía completa de uso
- 📄 `INICIO_RAPIDO.md` - Guía rápida
- 📄 `RESUMEN_FINAL.md` - Resumen del proyecto
- 📁 `documentacion/INSTRUCCIONES_STREAMLIT.md` - Guía de la app web
- 📁 `documentacion/GUIA_PRESENTACION.md` - Guía para presentar
- 📁 `documentacion/` - Toda la documentación técnica

---

## 👨‍💻 Información del Proyecto

**Proyecto**: Sprint 4 - Power BI: Medidas, KPIs y Análisis Temporal  
**Institución**: IBM  
**Tema**: Sistema de Gestión de Inventario con Power BI, DAX, Machine Learning y Python  
**Autor**: Martos Ludmila  
**DNI**: 34811650  
**Fecha**: 2025  
**Versión**: 4.0

### 🌐 Enlaces del Proyecto

- 🔗 **[Aplicación Web Online](https://tienda-aurelionv4.streamlit.app/)** ⭐⭐ - Acceso directo sin instalaciones

---

## 📝 Notas Adicionales

Este proyecto demuestra conceptos fundamentales de:
- Estructuras de datos
- Algoritmos de búsqueda y filtrado
- Manejo de archivos CSV
- Interfaces de usuario (consola, web, notebook)
- Validación de datos
- Análisis estadístico completo
- Base de datos normalizada (4 tablas relacionadas)
- Gestión de ventas y clientes
- Generación automática de gráficos profesionales
- **Power BI y DAX** (Sprint 4): Medidas, KPIs, análisis temporal
- **Machine Learning** (Sprint 3): Predicción de ventas con Random Forest

### Archivos del Proyecto

**📁 Raíz (Entregable/):**
| Archivo | Descripción |
|---------|-------------|
| `README.md` | Este archivo - Documentación completa ⭐ |
| `INSTRUCCIONES.md` | Guía completa de uso |
| `INICIO_RAPIDO.md` | Guía de inicio rápido |
| `RESUMEN_FINAL.md` | Resumen ejecutivo del proyecto |
| `requirements.txt` | Dependencias Python |

**📁 datos/:**
| Archivo | Descripción |
|---------|-------------|
| `productos.csv` | Base de datos de productos (80 productos) |
| `clientes.csv` | Base de datos de clientes (50 clientes) |
| `ventas.csv` | Base de datos de ventas (100 ventas) |
| `detalle_ventas.csv` | Detalles de ventas (273 registros) |

**📁 programas/:**
| Archivo | Descripción |
|---------|-------------|
| `tienda_aurelion.py` | Consola Python con ML (opciones 16-17) ⭐ |
| `app_streamlit.py` | App web Streamlit con ML integrado ⭐⭐ |
| `tienda_aurelion.ipynb` | Jupyter Notebook con ML ⭐ |
| `analisis_estadistico.py` | Script de análisis estadístico completo ⭐ |
| `analisis_estadistico.ipynb` | Análisis estadístico + ML ⭐⭐ |
| `modelo_ml_ventas.py` | Script ML standalone (genera gráficos) ⭐ |

**📁 documentacion/:**
| Archivo | Descripción |
|---------|-------------|
| `INDICE_PROYECTO.md` | Índice general de navegación |
| `ANALISIS_ESTADISTICO.md` | Análisis estadístico completo ⭐ |
| `PSEUDOCODIGO_Y_DIAGRAMAS.md` | Algoritmos y 6 diagramas de flujo |
| `SUGERENCIAS_COPILOT.md` | 20 sugerencias de IA evaluadas |
| `GUIA_POWER_BI.md` | Guía para crear dashboard |
| `GUIA_PRESENTACION.md` | Estructura para presentación oral |
| `INSTRUCCIONES_STREAMLIT.md` | Guía de uso de la app web |

**📁 Power BI/ (Sprint 4):**
| Archivo | Descripción |
|---------|-------------|
| `Sprint4.pbix` | ⭐ Dashboard Power BI completo |
| `procesamiento_datos.py` | ⭐ Script principal Python |
| `Documentacion_Sprint4.md` | Documentación completa del Sprint 4 |
| `Presentacion_Lectura_PowerBI.md` | Cómo leer el dashboard |
| `Guia_Paso_a_Paso_Medidas_DAX.md` | Guía para crear medidas DAX |
| `Codigo_DAX_Listo_Copiar.md` | Código DAX listo |
| `Notebook_DAX_Ejemplos.md` | Ejemplos detallados |
| `README_Sprint4.md` | Resumen ejecutivo |
| `resultados/` | CSV generados por procesamiento_datos.py |

**📄 Guías Dashboard Power BI (Sprint 2 - Legacy):**
| Archivo | Descripción |
|---------|-------------|
| `COMO_CREAR_DASHBOARD_POWERBI.md` | Guía maestra (Sprint 2) |
| `GUIA_RAPIDA_DASHBOARD_POWERBI.md` | Instrucciones paso a paso (Sprint 2) |
| `CHECKLIST_DASHBOARD.md` | Lista de verificación (Sprint 2) |
| `LAYOUT_VISUAL_DASHBOARD.md` | Vista previa visual (Sprint 2) |

**💡 Para Sprint 4, consulta la documentación en `Power BI/`**

El código está completamente documentado y diseñado para ser educativo y fácil de entender.

### Comparación de Versiones

| Aspecto | Consola | Jupyter | Streamlit |
|---------|---------|---------|-----------|
| Instalación | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Interfaz | Texto | Mixta | Web profesional |
| Gráficos | ASCII | Estáticos | Interactivos |
| Para presentar | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Documentación | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Interactividad | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Recomendación:** Usa **Streamlit** para presentaciones impactantes, **Jupyter** para documentación educativa, y **Consola** para uso rápido sin instalaciones.

---

## 📊 Dashboard Power BI - Sprint 4

### 🎯 Dashboard Completo con Medidas DAX y KPIs

**El dashboard está COMPLETO y LISTO para usar**: `Power BI/Sprint4.pbix`

#### 🚀 Acceso Directo

**Abrir el dashboard**:
1. Abre Power BI Desktop
2. Abre el archivo: `Power BI/Sprint4.pbix`
3. ¡Listo! El dashboard ya está completo con todas las medidas y visualizaciones

#### 📚 Documentación del Sprint 4

| Recurso | Descripción | Ubicación |
|---------|-------------|-----------|
| 📄 **[Documentacion_Sprint4.md](./Power%20BI/Documentacion_Sprint4.md)** | Documentación completa del proyecto | `Power BI/` |
| 📊 **[Presentacion_Lectura_PowerBI.md](./Power%20BI/Presentacion_Lectura_PowerBI.md)** | Cómo leer y entender el dashboard | `Power BI/` |
| ⭐ **[Guia_Paso_a_Paso_Medidas_DAX.md](./Power%20BI/Guia_Paso_a_Paso_Medidas_DAX.md)** | Guía para crear medidas DAX | `Power BI/` |
| 📋 **[Codigo_DAX_Listo_Copiar.md](./Power%20BI/Codigo_DAX_Listo_Copiar.md)** | Código DAX listo para usar | `Power BI/` |
| 💡 **[Notebook_DAX_Ejemplos.md](./Power%20BI/Notebook_DAX_Ejemplos.md)** | Ejemplos detallados | `Power BI/` |
| 🐍 **[procesamiento_datos.py](./Power%20BI/procesamiento_datos.py)** | Script principal Python | `Power BI/` |

#### ✅ Características Implementadas

**11+ Medidas DAX** con diferentes tipos de función:
- Funciones de Agregación: SUM, AVERAGE, COUNT, DISTINCTCOUNT, SUMX
- Funciones de Filtro: CALCULATE, FILTER, VALUES
- Funciones de Tiempo: DATEADD, DATESYTD, SAMEPERIODLASTYEAR
- Funciones Lógicas: IF, SWITCH, VAR/RETURN
- Funciones de Iteración: SUMX, AVERAGEX, COUNTROWS

**3 KPIs Completos**:
1. Rotación de Inventario (valor, objetivo, estado)
2. Margen de Utilidad (valor, objetivo, estado)
3. Nivel de Servicio (valor, objetivo, estado)

**Análisis Temporal**:
- Crecimiento Mes a Mes (MoM)
- Variación Interanual (YoY)
- Ventas YTD

**Jerarquías y Agrupaciones**:
- Jerarquía de Tiempo
- Jerarquía de Productos
- Agrupaciones por Rangos

#### 📥 Descargar Power BI Desktop

Si aún no tienes Power BI Desktop:

🔗 **[Descargar Power BI Desktop](https://powerbi.microsoft.com/desktop/)** (Gratis)

---

## 👨‍💻 Autor

**Desarrollador**: Ludmila Martos

## 📞 Contacto

- **Email**: [ludmilamartos@gmail.com](mailto:ludmilamartos@gmail.com)
- **LinkedIn**: [ludmimar89](https://www.linkedin.com/in/ludmimar89/)
- **GitHub**: [Ludmimar](https://github.com/Ludmimar)
