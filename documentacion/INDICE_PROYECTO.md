# 📚 ÍNDICE GENERAL - PROYECTO TIENDA AURELION

**Autor:** Martos Ludmila  
**DNI:** 34811650  
**Sprint:** 3 - Machine Learning  
**Institución:** IBM

---

## 🎯 Descripción del Proyecto

Sistema integral de gestión de inventario para la Tienda Aurelion, que incluye:
- Base de datos normalizada en 4 archivos CSV
- Programa Python interactivo con gestión de ventas y clientes
- **Machine Learning: Predicción de ventas con Random Forest** ⭐ NUEVO
- Análisis estadístico completo
- Guía para dashboard en Power BI
- Documentación completa
- Guía para presentación oral

---

## 📁 Estructura de Archivos

```
Entregable/
├── 📄 README.md, INSTRUCCIONES.md, INICIO_RAPIDO.md, RESUMEN_FINAL.md
├── 📄 requirements.txt
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
│   └── analisis_estadistico.ipynb ⭐⭐
├── 📁 graficos/ ⭐
│   └── (gráficos generados automáticamente)
└── 📁 documentacion/
    └── (archivos de documentación)
```

### 📊 1. DATOS (Base de Datos Normalizada)
**Ubicación:** `datos/`
- `productos.csv` - Base de datos con 80 productos
- `clientes.csv` - Base de datos con 50 clientes
- `ventas.csv` - Base de datos con 100 ventas
- `detalle_ventas.csv` - Detalles de 273 transacciones
- Formato CSV compatible con Python, Excel y Power BI
- Estructura normalizada para análisis avanzados

### 🐍 2. PROGRAMAS (4 VERSIONES)

#### 2.1 Programa de Consola
**Ubicación:** `programas/tienda_aurelion.py`
- Programa interactivo completo mejorado
- 15 funcionalidades principales (incluye ventas y clientes)
- Interfaz de consola amigable
- Sin dependencias externas básicas

#### 2.2 Aplicación Web Streamlit ⭐
**Ubicación:** `programas/app_streamlit.py`
- Interfaz web profesional mejorada
- Gráficos interactivos
- Filtros dinámicos
- Dashboard completo con gestión de ventas y clientes

#### 2.3 Jupyter Notebook
**Ubicación:** `programas/tienda_aurelion.ipynb`
- Documentación interactiva
- Código ejecutable paso a paso
- Ideal para presentaciones

#### 2.4 Análisis Estadístico Completo ⭐ NUEVO
**Ubicación:** `programas/analisis_estadistico.py` y `programas/analisis_estadistico.ipynb`
- Estadísticas descriptivas básicas
- Identificación de distribución de variables
- Análisis de correlaciones
- Detección de outliers
- Generación de 3 gráficos profesionales
- Versión Python script y versión Jupyter Notebook

**Funcionalidades (todas las versiones):**
1. Listar todos los productos
2. Buscar por categoría
3. Buscar por ID
4. Buscar por nombre
5. Buscar por rango de precios
6. Ver productos con bajo stock
7. Ver estadísticas del inventario
8. Buscar por proveedor
9. Agregar nuevo producto
10. Actualizar stock de producto
11. Ver todas las ventas ⭐ NUEVO
12. Ver detalle de una venta ⭐ NUEVO
13. Ver estadísticas de ventas ⭐ NUEVO
14. Listar todos los clientes ⭐ NUEVO
15. Ver estadísticas de clientes ⭐ NUEVO

**Ejecución (desde raíz Entregable/):**
```bash
# Consola
python programas/tienda_aurelion.py

# Streamlit
streamlit run programas/app_streamlit.py

# Jupyter
jupyter notebook programas/tienda_aurelion.ipynb

# Análisis Estadístico (Sprint 2) ⭐
python programas/analisis_estadistico.py

# Análisis Estadístico en Jupyter (Sprint 2) ⭐⭐
jupyter notebook programas/analisis_estadistico.ipynb
```

### 📖 3. DOCUMENTACIÓN PRINCIPAL
**Ubicación:** `README.md` (raíz)

**Contenido completo:**
- ✅ Tema, problema y solución claramente definidos
- ✅ Fuente de datos (origen, método, almacenamiento)
- ✅ Definición y estructura de datos (diagrama ER)
- ✅ Tipos y escala de datos (clasificación de variables)
- ✅ Desarrollo del programa (pasos, metodología)
- ✅ Sugerencias de Copilot (aceptadas y descartadas)
- ✅ Instrucciones de uso

**Secciones principales:**
1. Tema, Problema y Solución
2. Fuente de Datos
3. Definición y Estructura de Datos
4. Tipos y Escala de Datos
5. Desarrollo del Programa
6. Sugerencias de Copilot
7. Instrucciones de Uso

### 📐 4. PSEUDOCÓDIGO Y DIAGRAMAS
**Ubicación:** `documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md`

**Contenido:**
- ✅ Pseudocódigo completo del programa
- ✅ Algoritmo principal paso a paso
- ✅ Funciones de carga y guardado
- ✅ Funciones de búsqueda
- ✅ Funciones de gestión
- ✅ Diagramas de flujo detallados
- ✅ Conceptos clave de algoritmos
- ✅ Análisis de complejidad temporal

**Diagramas incluidos:**
1. Diagrama de flujo principal
2. Diagrama de carga de datos
3. Diagrama de búsqueda por categoría
4. Diagrama de agregar producto
5. Diagrama de estadísticas
6. Diagrama de flujo de datos

### 🤖 5. SUGERENCIAS DE COPILOT
**Ubicación:** `documentacion/SUGERENCIAS_COPILOT.md`

**Contenido detallado:**

**✅ 10 Sugerencias Aceptadas:**
1. Uso de `csv.DictReader`
2. Conversión explícita de tipos de datos
3. Función de validación centralizada
4. Uso de f-strings para formateo
5. Context Manager para archivos (`with`)
6. Type hints (anotaciones de tipo)
7. Separadores visuales con Unicode
8. Emojis para mejorar UX
9. List comprehensions para filtrado
10. Función `sorted()` con `key` parameter

**❌ 10 Sugerencias Descartadas:**
1. SQLite en lugar de CSV
2. Interfaz gráfica con tkinter
3. Biblioteca Pandas
4. Sistema de autenticación
5. Logging con módulo `logging`
6. Validación con expresiones regulares
7. Clase Producto con POO
8. Virtualenv y requirements.txt
9. Tests unitarios
10. API REST con Flask

**Incluye:**
- Razones detalladas para cada decisión
- Ejemplos de código
- Alternativas adoptadas
- Estadísticas (50% tasa de aceptación)
- Lecciones aprendidas

### 📊 6. GUÍA PARA DASHBOARD POWER BI
**Archivo:** `GUIA_POWER_BI.md`

**Contenido completo:**
- ✅ Preparación de datos para importación
- ✅ Paso a paso para importar CSV a Power BI
- ✅ 10 visualizaciones recomendadas con configuración
- ✅ KPIs y métricas clave
- ✅ Medidas DAX completas
- ✅ Diseño del dashboard (layout sugerido)
- ✅ Paleta de colores temática medieval
- ✅ Interactividad y filtros
- ✅ Tips y mejores prácticas
- ✅ Checklist de entrega

**Visualizaciones recomendadas:**
1. Tarjetas de KPIs (5 principales)
2. Gráfico de barras: Productos por categoría
3. Gráfico de columnas: Top 10 más valiosos
4. Gráfico de anillos: Distribución de stock
5. Tabla: Productos con stock bajo
6. Gráfico de dispersión: Precio vs Stock
7. Gráfico de barras apiladas: Proveedores
8. Medidor: Indicador de stock saludable
9. Mapa de calor: Categoría vs Precio
10. Segmentaciones de datos (filtros)

### 🎤 7. GUÍA PARA PRESENTACIÓN ORAL
**Archivo:** `GUIA_PRESENTACION.md`

**Contenido:**
- ✅ Estructura completa de 11 slides
- ✅ Qué decir en cada slide (guión completo)
- ✅ Duración recomendada por sección
- ✅ Tips de diseño de slides
- ✅ Tips de presentación oral
- ✅ Manejo de preguntas y respuestas
- ✅ Checklist pre-presentación
- ✅ Criterios de evaluación
- ✅ Frases de transición útiles

**Estructura de la presentación (10-15 minutos):**
1. Portada (30 seg)
2. Contexto y Problema (2 min)
3. La Solución Propuesta (2 min)
4. Estructura de Datos (1.5 min)
5. Desarrollo Técnico - Python (2 min)
6. Demostración en Vivo (2-3 min)
7. Hallazgos y Análisis de Datos (2 min)
8. Dashboard Power BI (1.5 min)
9. Impacto y Resultados (1.5 min)
10. Aprendizajes y Próximos Pasos (1 min)
11. Preguntas y Agradecimientos

---

## 🚀 Cómo Usar Este Proyecto

### Para Ejecutar el Programa

1. Asegúrate de tener Python 3.6+ instalado
2. Abre una terminal en la carpeta del proyecto
3. Ejecuta:
   ```bash
   python tienda_aurelion.py
   ```
4. Sigue las instrucciones del menú interactivo

### Para Crear el Dashboard en Power BI

1. Abre `GUIA_POWER_BI.md`
2. Sigue el paso a paso de importación
3. Implementa las visualizaciones recomendadas
4. Usa las medidas DAX proporcionadas

### Para Preparar la Presentación

1. Lee `GUIA_PRESENTACION.md`
2. Crea tus slides siguiendo la estructura
3. Practica con el guión proporcionado
4. Prepara la demo en vivo del programa

---

## 📊 Estadísticas del Proyecto

### Base de Datos
- **Productos totales:** 20
- **Categorías:** 10
- **Proveedores:** 9
- **Rango de precios:** 25 - 5,000 monedas
- **Stock total:** 1,468 unidades
- **Valor total inventario:** 85,075 monedas

### Código Python
- **Líneas de código:** ~670
- **Funciones:** 15+
- **Validaciones:** Robustas con try-except
- **Dependencias externas:** 0 (solo librerías estándar)

### Documentación
- **Archivos totales:** 8
- **Páginas de documentación:** ~40
- **Diagramas de flujo:** 6
- **Ejemplos de código:** 30+

---

## ✅ Checklist de Entrega

### Documentación
- [x] README.md completo con todos los puntos requeridos
- [x] Pseudocódigo detallado
- [x] Diagramas de flujo
- [x] Sugerencias de Copilot (aceptadas y descartadas)

### Desarrollo Técnico
- [x] Base de datos CSV estructurada
- [x] Programa Python interactivo funcional
- [x] Sin errores de ejecución
- [x] Validaciones implementadas
- [x] Comentarios en el código

### Visualización
- [x] Guía completa para Power BI
- [x] Diseño de dashboard propuesto
- [x] Medidas DAX incluidas
- [x] Layout y paleta de colores

### Presentación
- [x] Estructura completa de slides
- [x] Guión de presentación
- [x] Tips de comunicación
- [x] Preparación para preguntas

---

## 🎯 Requisitos del Sprint - Verificación

| Requisito | Estado | Archivo |
|-----------|--------|---------|
| Tema, problema y solución claros | ✅ | README.md |
| Fuente de datos definida | ✅ | README.md |
| Definición y estructura de datos | ✅ | README.md |
| Tipos y escala de datos | ✅ | README.md |
| Pasos del desarrollo | ✅ | README.md |
| Pseudocódigo | ✅ | PSEUDOCODIGO_Y_DIAGRAMAS.md |
| Diagrama del programa | ✅ | PSEUDOCODIGO_Y_DIAGRAMAS.md |
| Sugerencias Copilot aceptadas | ✅ | SUGERENCIAS_COPILOT.md |
| Sugerencias Copilot descartadas | ✅ | SUGERENCIAS_COPILOT.md |
| Programa Python interactivo | ✅ | tienda_aurelion.py |
| Sin errores de ejecución | ✅ | Verificado |
| Documentación completa | ✅ | Todos los archivos |

---

## 📦 Archivos del Proyecto

```
Entregable/
│
├── 📄 INDICE_PROYECTO.md (este archivo)
├── 📄 README.md (documentación principal)
├── 📄 PSEUDOCODIGO_Y_DIAGRAMAS.md
├── 📄 SUGERENCIAS_COPILOT.md
├── 📄 GUIA_POWER_BI.md
├── 📄 GUIA_PRESENTACION.md
├── 📊 tienda_aurelion.csv (base de datos)
└── 🐍 tienda_aurelion.py (programa interactivo)
```

**Total:** 8 archivos

---

## 💡 Recomendaciones para la Entrega

### 1. Organización en Drive

Crea una carpeta con esta estructura:

```
📁 Tienda Aurelion - [Tu Nombre]
├── 📁 1. Documentación
│   ├── README.md
│   ├── PSEUDOCODIGO_Y_DIAGRAMAS.md
│   ├── SUGERENCIAS_COPILOT.md
│   └── INDICE_PROYECTO.md
│
├── 📁 2. Programa Python
│   ├── tienda_aurelion.py
│   └── tienda_aurelion.csv
│
├── 📁 3. Power BI
│   ├── GUIA_POWER_BI.md
│   └── tienda_aurelion.pbix (tu dashboard)
│
└── 📁 4. Presentación
    ├── GUIA_PRESENTACION.md
    └── Presentacion_Tienda_Aurelion.pptx
```

### 2. Archivo README en Drive

Incluye un archivo de texto con:
- Link al repositorio (si usas GitHub)
- Instrucciones de ejecución
- Tu información de contacto
- Fecha de entrega

### 3. Video Demo (Opcional pero Recomendado)

Graba un video corto (3-5 minutos) mostrando:
- Ejecución del programa Python
- Principales funcionalidades
- Dashboard de Power BI

---

## 🏆 Puntos Destacados del Proyecto

### Fortalezas
1. ✅ **Documentación exhaustiva** - Cada aspecto está detalladamente explicado
2. ✅ **Código limpio y comentado** - Fácil de entender y mantener
3. ✅ **Solución práctica** - Resuelve un problema real de negocio
4. ✅ **Escalable** - Diseñado para crecer con el negocio
5. ✅ **Sin dependencias externas** - Portable y fácil de ejecutar
6. ✅ **Interfaz amigable** - UX mejorada con emojis y validaciones
7. ✅ **Análisis de datos completo** - Estadísticas y visualizaciones
8. ✅ **Presentación profesional** - Guía completa para exponer

### Innovaciones
- 🎨 Interfaz temática medieval/fantasía
- 📊 Integración Python + Power BI
- 🤖 Análisis crítico de sugerencias de IA
- 📈 KPIs y métricas orientadas a negocio
- 🎤 Guía de presentación con storytelling

---

## 📞 Soporte y Contacto

Si tienes preguntas sobre el proyecto:
1. Revisa primero la documentación correspondiente
2. Consulta el README.md principal
3. Verifica las guías específicas (Power BI, Presentación)

---

## 📅 Información del Proyecto

**Proyecto:** Tienda Aurelion - Sistema de Gestión de Inventario  
**Sprint:** 1 - Introducción a la Inteligencia Artificial  
**Institución:** IBM  
**Año:** 2025  
**Versión:** 1.0  

---

## 🎓 Aprendizajes Clave

Este proyecto demuestra competencias en:
- ✅ Análisis de problemas de negocio
- ✅ Estructuración de datos
- ✅ Programación en Python
- ✅ Algoritmos de búsqueda y filtrado
- ✅ Validación y manejo de errores
- ✅ Visualización de datos
- ✅ Documentación técnica
- ✅ Comunicación profesional
- ✅ Toma de decisiones técnicas fundamentadas

---

## 🚀 Próximos Pasos Sugeridos

### Fase 2: Análisis Temporal
- Agregar historial de ventas
- Análisis de tendencias
- Predicción de demanda

### Fase 3: Machine Learning
- Modelo de predicción de stock
- Recomendaciones automáticas de reabastecimiento
- Clustering de productos

### Fase 4: Escalabilidad
- Migrar a base de datos SQL
- API REST para acceso remoto
- Sistema multi-usuario

---

**¡Proyecto completo y listo para entregar! ⚔️✨**

Este índice te ayudará a navegar por toda la documentación y entender la estructura completa del proyecto Tienda Aurelion.

