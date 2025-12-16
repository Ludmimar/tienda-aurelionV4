# 🚀 Instrucciones de Ejecución - Sprint 4

## 📋 Archivo Principal: `procesamiento_datos.py`

Este es el archivo principal para ejecutar el procesamiento de datos del Sprint 4.

### 🎯 Ubicación
```
tienda-aurelionV4/Power BI/procesamiento_datos.py
```

### ✅ Requisitos Previos

1. **Python 3.7+** instalado
2. **Librerías necesarias**:
   ```bash
   pip install pandas numpy
   ```

### 🏃 Ejecución

#### Opción 1: Desde la carpeta Power BI
```bash
cd "tienda-aurelionV4/Power BI"
python procesamiento_datos.py
```

#### Opción 2: Desde cualquier ubicación
```bash
python "tienda-aurelionV4/Power BI/procesamiento_datos.py"
```

### 📊 Qué hace el script

1. **Carga de datos**:
   - Busca archivos CSV en `datos/` (productos, ventas, detalle_ventas, clientes)
   - Si no encuentra archivos, genera datos de ejemplo automáticamente

2. **Procesamiento**:
   - Calcula métricas básicas del negocio
   - Calcula rotación de inventario por producto
   - Calcula margen de utilidad por venta
   - Realiza análisis temporal (MoM, YoY)
   - Crea agrupaciones por rangos de stock y valor

3. **Resultados**:
   - Guarda archivos CSV procesados en `Power BI/resultados/`:
     - `productos_procesados.csv`
     - `ventas_temporales.csv`
     - `rotacion_inventario.csv`
     - `margen_utilidad.csv`

### 📁 Estructura de Datos Esperada

Si tienes tus propios datos, colócalos en:
```
tienda-aurelionV4/
└── datos/
    ├── productos.csv
    ├── ventas.csv
    ├── detalle_ventas.csv
    └── clientes.csv
```

### 🔧 Configuración

El script busca datos en las siguientes ubicaciones (en orden):
1. `Power BI/../datos/` (desde Power BI hacia datos/)
2. `Power BI/datos/` (si datos está en mismo nivel)
3. `datos/` (relativo al directorio actual)

Si no encuentra archivos, genera datos de ejemplo automáticamente.

### 📝 Salida del Script

El script muestra en consola:
- ✅ Confirmación de carga de datos
- ✅ Métricas calculadas
- ✅ Rotación promedio de inventario
- ✅ Margen promedio de utilidad
- ✅ Cantidad de períodos analizados
- ✅ Confirmación de guardado de archivos

### 🎯 Integración con Power BI

Los archivos CSV generados en `resultados/` pueden ser:
- Importados directamente en Power BI Desktop
- Usados como fuente de datos para el dashboard `Sprint4.pbix`
- Analizados con las medidas DAX implementadas

### 📚 Documentación Relacionada

- **Guía completa**: `Documentacion_Sprint4.md`
- **Ejemplos DAX**: `Notebook_DAX_Ejemplos.md`
- **Código DAX listo**: `Codigo_DAX_Listo_Copiar.md`
- **Guía paso a paso**: `Guia_Paso_a_Paso_Medidas_DAX.md`

---

**✅ Sprint 4 - Power BI: Medidas, KPIs y Análisis Temporal**

