# 🚀 INSTRUCCIONES DE USO - PROYECTO ORGANIZADO

## 📁 Estructura del Proyecto

```
Entregable/
│
├── 📄 README.md                    ← Documentación principal
├── 📄 RESUMEN_FINAL.md              ← Resumen ejecutivo
├── 📄 INICIO_RAPIDO.md              ← Guía rápida
├── 📄 INSTRUCCIONES.md              ← Este archivo
├── 📄 requirements.txt              ← Dependencias
│
├── 📁 datos/
│   ├── productos.csv          ← Base de datos de productos (80 productos)
│   ├── clientes.csv           ← Base de datos de clientes (50 clientes)
│   ├── ventas.csv             ← Base de datos de ventas (100 ventas)
│   └── detalle_ventas.csv     ← Detalles de ventas (273 registros)
│
├── 📁 programas/
│   ├── tienda_aurelion.py           ← Programa de consola
│   ├── app_streamlit.py             ← Aplicación web
│   ├── tienda_aurelion.ipynb        ← Jupyter Notebook
│   └── analisis_estadistico.py      ← Análisis estadístico completo ⭐
│
└── 📁 documentacion/
    ├── INDICE_PROYECTO.md           ← Índice general
    ├── PSEUDOCODIGO_Y_DIAGRAMAS.md  ← Algoritmos
    ├── SUGERENCIAS_COPILOT.md       ← Análisis de IA
    ├── GUIA_POWER_BI.md             ← Dashboard BI
    ├── GUIA_PRESENTACION.md         ← Presentación oral
    └── INSTRUCCIONES_STREAMLIT.md   ← Guía app web
```

---

## ⚡ EJECUCIÓN RÁPIDA

### Opción 1: Desde la RAÍZ (Entregable/)

```bash
# Programa de Consola
python programas/tienda_aurelion.py

# Aplicación Web Streamlit ⭐
streamlit run programas/app_streamlit.py

# Jupyter Notebook
jupyter notebook programas/tienda_aurelion.ipynb
```

### Opción 2: Desde carpeta PROGRAMAS/ 

```bash
# Ir a la carpeta
cd programas

# Programa de Consola
python tienda_aurelion.py

# Aplicación Web Streamlit ⭐
streamlit run app_streamlit.py

# Jupyter Notebook
jupyter notebook tienda_aurelion.ipynb
```

---

## 📦 INSTALACIÓN DE DEPENDENCIAS

### Para Streamlit (App Web):
```bash
pip install streamlit pandas numpy matplotlib seaborn scipy
```

### Para Jupyter Notebook:
```bash
pip install jupyter
```

### Instalar todo desde requirements.txt:
```bash
pip install -r requirements.txt
```

---

## 🔍 RUTAS ACTUALIZADAS

Todos los programas ya están configurados para buscar los datos en:
```
datos/productos.csv
datos/clientes.csv
datos/ventas.csv
datos/detalle_ventas.csv
```

Esto significa que funcionan tanto si:
- ✅ Ejecutas desde la raíz: `python programas/tienda_aurelion.py`
- ✅ Ejecutas desde programas/: `cd programas && python tienda_aurelion.py`

Los programas detectan automáticamente las rutas correctas de los 4 archivos CSV.

---

## 📚 DOCUMENTACIÓN

Todos los archivos de documentación están en `documentacion/`:

| Archivo | Descripción |
|---------|-------------|
| `INDICE_PROYECTO.md` | Navegación completa del proyecto |
| `ANALISIS_ESTADISTICO.md` | Análisis estadístico completo ⭐ |
| `PSEUDOCODIGO_Y_DIAGRAMAS.md` | 6 diagramas de flujo + algoritmos |
| `SUGERENCIAS_COPILOT.md` | 20 sugerencias evaluadas |
| `GUIA_POWER_BI.md` | Cómo crear dashboard |
| `GUIA_PRESENTACION.md` | Estructura de presentación |
| `INSTRUCCIONES_STREAMLIT.md` | Guía completa de la app web |

---

## 🎯 RECOMENDACIONES

### Para Presentar:
1. **Ejecuta Streamlit** (más visual e impactante)
   ```bash
   streamlit run programas/app_streamlit.py
   ```

2. **Ejecuta Análisis Estadístico** (muestra gráficos profesionales)
   ```bash
   python programas/analisis_estadistico.py
   ```

3. **Muestra el Jupyter Notebook** (documentación educativa)
   ```bash
   jupyter notebook programas/tienda_aurelion.ipynb
   ```

4. **Ten listo el programa de consola** (backup simple)
   ```bash
   python programas/tienda_aurelion.py
   ```

### Para Estudiar/Documentar:
- Lee `README.md` - Toda la información del proyecto
- Lee `documentacion/PSEUDOCODIGO_Y_DIAGRAMAS.md` - Algoritmos
- Lee `documentacion/SUGERENCIAS_COPILOT.md` - Decisiones técnicas

---

## ✅ VERIFICACIÓN

### Comprobar que todo funciona:

```bash
# 1. Verificar que existen los 4 archivos CSV
dir datos\*.csv    # Windows - debería mostrar productos.csv, clientes.csv, ventas.csv, detalle_ventas.csv
ls datos/*.csv     # Linux/Mac

# 2. Probar programa de consola
python programas/tienda_aurelion.py

# 3. Probar Streamlit (instalar primero si no lo tienes)
pip install streamlit pandas numpy matplotlib seaborn scipy
streamlit run programas/app_streamlit.py

# 4. Probar análisis estadístico (Sprint 2)
python programas/analisis_estadistico.py
```

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: "No se encontró el archivo"
- ✅ Verifica que estés en la carpeta correcta
- ✅ Asegúrate de que existen los 4 archivos CSV en `datos/`:
  - `productos.csv`
  - `clientes.csv`
  - `ventas.csv`
  - `detalle_ventas.csv`
- ✅ Si ejecutas desde programas/, las rutas ya están configuradas automáticamente

### Error: "streamlit: comando no encontrado"
```bash
pip install streamlit pandas
```

### Error: "jupyter: comando no encontrado"
```bash
pip install jupyter
```

---

## 📊 COMPARACIÓN DE VERSIONES

| Característica | Consola | Jupyter | Streamlit |
|----------------|---------|---------|-----------|
| **Instalación** | ✅ Inmediata | ⚠️ pip install | ⚠️ pip install |
| **Interfaz** | Texto | Mixta | Web profesional |
| **Gráficos** | ASCII | Estáticos | Interactivos |
| **Para presentar** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Documentación** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Ejecutar desde** | Terminal | Navegador | Navegador |

---

## 🎓 PARA TU ENTREGA EN DRIVE

Sube toda la carpeta `Entregable/` con su estructura de subcarpetas:

```
📁 Carpeta de Drive: "Tienda Aurelion - [Tu Nombre]"
│
└── (Sube toda la carpeta Entregable con sus subcarpetas)
    ├── datos/
    ├── programas/
    ├── documentacion/
    └── archivos .md en raíz
```

**No comprimas** - Sube la estructura de carpetas directamente.

---

## 💡 TIPS

1. **Backup**: Guarda una copia del CSV antes de hacer cambios
2. **Prueba todo**: Ejecuta las 3 versiones antes de presentar
3. **Lee la documentación**: Especialmente `GUIA_PRESENTACION.md`
4. **Practica**: Ensaya tu presentación con Streamlit

---

**📧 ¿Dudas?** Consulta `README.md` o `RESUMEN_FINAL.md`

---

**👨‍💻 Autor:** Martos Ludmila  
**📋 DNI:** 34811650  
**🏢 Institución:** IBM  
**📅 Sprint:** 3 - Machine Learning  
**📆 Año:** 2025

---




