# Documentación del Proyecto - Sprint 4
## Tienda Aurelion: Medidas, KPIs y Análisis Temporal

---

## 1. Resumen del Proyecto

### Problema Identificado
La gestión de inventario y ventas de la Tienda Aurelion requiere un análisis profundo de métricas clave para optimizar la operación, identificar tendencias y tomar decisiones informadas sobre productos, stock y estrategias comerciales.

### Solución Propuesta
Desarrollo de un dashboard en Power BI con medidas DAX avanzadas, jerarquías, agrupaciones y KPIs que permitan un análisis completo del negocio con capacidades de análisis temporal.

---

## 2. Modelo de Datos

### Tablas Principales
- **Productos**: Información de productos (id, nombre, categoria, stock, valor_inventario, proveedor)
- **Clientes**: Información de clientes
- **Ventas**: Registro de transacciones de venta
- **Detalle_Ventas**: Detalles específicos de cada venta

### Relaciones
- Ventas → Clientes (Relación uno a muchos)
- Ventas → Detalle_Ventas (Relación uno a muchos)
- Detalle_Ventas → Productos (Relación muchos a uno)

---

## 3. Jerarquías y Agrupaciones

### 3.1 Jerarquía de Tiempo (Análisis Temporal)
```
Año
  └── Trimestre
      └── Mes
          └── Día
```

### 3.2 Jerarquía de Productos
```
Categoría
  └── Proveedor
      └── Producto
```

### 3.3 Jerarquía Geográfica (si aplica)
```
Región
  └── Ciudad
      └── Cliente
```

### 3.4 Agrupaciones por Rangos
- **Stock por Rango**: 
  - Stock Bajo (< 20)
  - Stock Medio (20-50)
  - Stock Alto (> 50)
  
- **Valor de Inventario por Segmento**:
  - Bajo Valor (< $1000)
  - Valor Medio ($1000-$5000)
  - Alto Valor (> $5000)

---

## 4. Medidas DAX (Mínimo 6 con diferentes tipos de función)

### 4.1 Funciones de Agregación (SUM, COUNT, AVERAGE)

#### Medida 1: Total de Productos Vendidos
```dax
-- Total de Productos Vendidos = 
SUM(Detalle_Ventas[cantidad])
```
**Tipo de función**: Agregación (SUM)  
**Descripción**: Suma total de productos vendidos en todas las transacciones.

#### Medida 2: Promedio de Stock por Categoría
```dax
-- Promedio de Stock por Categoría = 
AVERAGE(Productos[stock])
```
**Tipo de función**: Agregación (AVERAGE)  
**Descripción**: Promedio del stock disponible en todas las categorías.

#### Medida 3: Conteo de Productos Únicos
```dax
-- Total Productos Únicos = 
DISTINCTCOUNT(Productos[id])
```
**Tipo de función**: Agregación (DISTINCTCOUNT)  
**Descripción**: Número total de productos únicos en el catálogo.

### 4.2 Funciones de Filtro (CALCULATE, FILTER)

#### Medida 4: Total de Ventas del Mes Actual
```dax
-- Ventas Mes Actual = 
CALCULATE(
    SUM(Ventas[total]),
    FILTER(
        Ventas,
        YEAR(Ventas[fecha]) = YEAR(TODAY()) &&
        MONTH(Ventas[fecha]) = MONTH(TODAY())
    )
)
```
**Tipo de función**: Filtro (CALCULATE, FILTER)  
**Descripción**: Calcula las ventas totales solo del mes actual usando funciones de filtro y tiempo.

#### Medida 5: Productos con Stock Bajo (Menor a 20)
```dax
-- Productos Stock Bajo = 
CALCULATE(
    COUNTROWS(Productos),
    FILTER(Productos, Productos[stock] < 20)
)
```
**Tipo de función**: Filtro (CALCULATE, FILTER)  
**Descripción**: Cuenta cuántos productos tienen stock menor a 20 unidades.

### 4.3 Funciones de Tiempo (DATEADD, DATESYTD, SAMEPERIODLASTYEAR)

#### Medida 6: Ventas del Mes Anterior
```dax
-- Ventas Mes Anterior = 
CALCULATE(
    SUM(Ventas[total]),
    DATEADD(Ventas[fecha], -1, MONTH)
)
```
**Tipo de función**: Tiempo (DATEADD)  
**Descripción**: Calcula las ventas del mes anterior usando funciones de manipulación de fechas.

#### Medida 7: Ventas Acumuladas Año a la Fecha (YTD)
```dax
-- Ventas YTD = 
CALCULATE(
    SUM(Ventas[total]),
    DATESYTD(Ventas[fecha])
)
```
**Tipo de función**: Tiempo (DATESYTD)  
**Descripción**: Suma acumulada de ventas desde el inicio del año hasta la fecha actual.

#### Medida 8: Variación Interanual (YoY)
```dax
-- Variación YoY = 
VAR VentasActuales = SUM(Ventas[total])
VAR VentasAñoAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        SAMEPERIODLASTYEAR(Ventas[fecha])
    )
RETURN
    IF(
        VentasAñoAnterior > 0,
        (VentasActuales - VentasAñoAnterior) / VentasAñoAnterior,
        BLANK()
    )
```
**Tipo de función**: Tiempo (SAMEPERIODLASTYEAR), Lógica (IF, VAR/RETURN)  
**Descripción**: Calcula el porcentaje de variación comparando con el mismo período del año anterior.

### 4.4 Funciones Lógicas y Condicionales (IF, SWITCH, AND, OR)

#### Medida 9: Estado de Inventario (Alto/Medio/Bajo)
```dax
-- Estado Inventario = 
SWITCH(
    TRUE(),
    [-- Stock Total] < 100, "Stock Bajo",
    [-- Stock Total] < 300, "Stock Medio",
    "Stock Alto"
)
```
**Tipo de función**: Lógica (SWITCH)  
**Descripción**: Clasifica el inventario en categorías según el nivel de stock total.

### 4.5 Funciones de Búsqueda y Referencia (RELATED, RELATEDTABLE, LOOKUPVALUE)

#### Medida 10: Valor Total de Inventario (con relación)
```dax
-- Valor Total Inventario = 
SUMX(
    Productos,
    Productos[stock] * Productos[precio_unitario]
)
```
**Tipo de función**: Iteración (SUMX)  
**Descripción**: Calcula el valor total del inventario multiplicando stock por precio unitario de cada producto.

### 4.6 Funciones de Texto (CONCATENATE, LEFT, RIGHT, FIND)

#### Medida 11: Productos por Categoría (Texto)
```dax
-- Resumen Categorías = 
CONCATENATEX(
    VALUES(Productos[categoria]),
    Productos[categoria] & ": " & [-- Total Productos Únicos],
    ", "
)
```
**Tipo de función**: Texto (CONCATENATEX)  
**Descripción**: Genera un texto concatenado con el resumen de productos por categoría.

---

## 5. KPIs (Key Performance Indicators)

### Estructura de KPI en Power BI:
Cada KPI debe tener:
1. **Valor Actual**: Medida que representa el valor actual
2. **Objetivo (Target)**: Valor objetivo a alcanzar
3. **Umbral**: Niveles de estado (por encima/por debajo del objetivo)

### KPI 1: Tasa de Rotación de Inventario

#### Valor Actual:
```dax
-- Rotación de Inventario = 
DIVIDE(
    [-- Total de Productos Vendidos],
    [-- Stock Total],
    0
)
```

#### Objetivo:
```dax
-- Objetivo Rotación = 2.5
```
**Interpretación**: Se espera una rotación de 2.5 veces el inventario.

#### Medida de Estado:
```dax
-- Estado Rotación = 
IF(
    [-- Rotación de Inventario] >= [-- Objetivo Rotación],
    "✅ Objetivo Alcanzado",
    "⚠️ Por Debajo del Objetivo"
)
```

---

### KPI 2: Margen de Utilidad

#### Valor Actual:
```dax
-- Margen Utilidad = 
VAR Ingresos = [-- Ingresos Totales]
VAR Costos = SUMX(
    Detalle_Ventas,
    RELATED(Productos[precio_costo]) * Detalle_Ventas[cantidad]
)
RETURN
    DIVIDE(Ingresos - Costos, Ingresos, 0)
```

#### Objetivo:
```dax
-- Objetivo Margen = 0.30
```
**Interpretación**: Se espera un margen de utilidad del 30%.

#### Medida de Estado:
```dax
-- Estado Margen = 
SWITCH(
    TRUE(),
    [-- Margen Utilidad] >= [-- Objetivo Margen], "✅ Excelente",
    [-- Margen Utilidad] >= [-- Objetivo Margen] * 0.8, "⚠️ Aceptable",
    "❌ Bajo"
)
```

---

### KPI 3: Nivel de Servicio (Fill Rate)

#### Valor Actual:
```dax
-- Nivel Servicio = 
VAR PedidosCompletos = 
    COUNTROWS(
        FILTER(
            Ventas,
            RELATED(Detalle_Ventas[cantidad]) <= RELATED(Productos[stock])
        )
    )
VAR TotalPedidos = COUNTROWS(Ventas)
RETURN
    DIVIDE(PedidosCompletos, TotalPedidos, 0)
```

#### Objetivo:
```dax
-- Objetivo Nivel Servicio = 0.95
```
**Interpretación**: Se espera cumplir el 95% de los pedidos sin falta de stock.

#### Medida de Estado:
```dax
-- Estado Nivel Servicio = 
IF(
    [-- Nivel Servicio] >= [-- Objetivo Nivel Servicio],
    "✅ Objetivo Alcanzado",
    IF(
        [-- Nivel Servicio] >= [-- Objetivo Nivel Servicio] * 0.9,
        "⚠️ Aceptable",
        "❌ Requiere Atención"
    )
)
```

---

## 6. Análisis Temporal

### 6.1 Medidas de Comparación Temporal

#### Crecimiento Mes a Mes (MoM)
```dax
-- Crecimiento MoM = 
VAR VentasActuales = [-- Total de Ventas]
VAR VentasMesAnterior = 
    CALCULATE(
        [-- Total de Ventas],
        DATEADD(Ventas[fecha], -1, MONTH)
    )
RETURN
    IF(
        VentasMesAnterior > 0,
        DIVIDE(VentasActuales - VentasMesAnterior, VentasMesAnterior, 0),
        BLANK()
    )
```

#### Tendencia de 3 Meses
```dax
-- Promedio 3 Meses = 
CALCULATE(
    AVERAGEX(
        VALUES(Ventas[fecha]),
        [-- Total de Ventas]
    ),
    DATESINPERIOD(
        Ventas[fecha],
        MAX(Ventas[fecha]),
        -3,
        MONTH
    )
)
```

---

## 7. Resumen de Funciones DAX Utilizadas

### Grupo 1: Funciones de Agregación (2+ funciones)
- ✅ SUM
- ✅ AVERAGE
- ✅ COUNT
- ✅ DISTINCTCOUNT
- ✅ SUMX

### Grupo 2: Funciones de Filtro (2+ funciones)
- ✅ CALCULATE
- ✅ FILTER
- ✅ VALUES

### Grupo 3: Funciones de Tiempo (2+ funciones)
- ✅ DATEADD
- ✅ DATESYTD
- ✅ SAMEPERIODLASTYEAR
- ✅ DATESINPERIOD
- ✅ YEAR, MONTH, TODAY

### Grupo 4: Funciones Lógicas (2+ funciones)
- ✅ IF
- ✅ SWITCH
- ✅ AND
- ✅ OR

### Grupo 5: Funciones de Texto (2+ funciones)
- ✅ CONCATENATEX
- ✅ DIVIDE (operador)

### Grupo 6: Funciones de Iteración (2+ funciones)
- ✅ SUMX
- ✅ AVERAGEX
- ✅ COUNTROWS

---

## 8. Visualizaciones Recomendadas

### Dashboard Principal
1. **Tarjetas KPI**: Mostrar los 3 KPIs principales con indicadores de estado
2. **Gráfico de Líneas**: Evolución temporal de ventas (con comparación año anterior)
3. **Gráfico de Columnas**: Rotación de inventario por categoría
4. **Gráfico de Barras**: Top 10 productos más vendidos
5. **Matriz**: Análisis por jerarquía (Categoría → Proveedor → Producto)
6. **Mapa de Árbol**: Distribución de valor de inventario por categoría

### Página de Análisis Temporal
1. **Gráfico de Líneas**: Tendencias mensuales con variación YoY
2. **Tarjetas**: Crecimiento MoM, YTD, Variación YoY
3. **Tabla**: Comparativa por períodos

---

## 9. Criterios de Aceptación

✅ **Jerarquías**: Se han creado al menos 3 jerarquías (Tiempo, Productos, Geográfica)  
✅ **Métricas**: Se han implementado al menos 6 métricas con diferentes tipos de función DAX  
✅ **KPIs**: Se han construido 3 KPIs con estructura completa (Valor, Objetivo, Estado)  
✅ **Funciones DAX**: Se utilizan al menos 2 funciones de cada grupo aprendido  
✅ **Análisis Temporal**: Se incluyen medidas de comparación temporal (MoM, YoY, YTD)  
✅ **Visualizaciones**: Dashboard completo con visualizaciones apropiadas para cada métrica  

---

## 10. Instrucciones de Implementación

1. **Abrir Power BI Desktop** y cargar el archivo `Sprint4.pbix`
2. **Crear Jerarquías**:
   - Panel derecho → Campos → Click derecho en tabla → "Nueva jerarquía"
3. **Crear Medidas**:
   - Panel derecho → Tabla seleccionada → Click derecho → "Nueva medida"
   - Copiar y pegar cada medida DAX del documento
4. **Crear KPIs**:
   - Insertar visual KPI desde el panel de visualizaciones
   - Asignar Valor Actual, Objetivo y Estado
5. **Configurar Visualizaciones**:
   - Arrastrar medidas y campos a los visuales apropiados
   - Configurar formatos y colores según tema medieval

---

**Fecha de Creación**: Diciembre 2025  
**Proyecto**: Tienda Aurelion - Sprint 4  
**Versión**: 1.0

