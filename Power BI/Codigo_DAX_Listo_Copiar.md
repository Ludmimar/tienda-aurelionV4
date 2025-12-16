# Código DAX Listo para Copiar y Pegar
## Tienda Aurelion - Sprint 4

---

## 📋 INSTRUCCIONES RÁPIDAS

1. Abre Power BI Desktop
2. Click derecho en la tabla indicada → "Nueva medida"
3. Copia y pega el código completo
4. Presiona Enter
5. Verifica que no haya errores (línea roja)

---

## 📊 TABLA: Productos

### Medida 1: Total de Productos Vendidos
```dax
-- Total de Productos Vendidos = SUM(Detalle_Ventas[cantidad])
```
**Formato**: Número entero

---

### Medida 2: Valor Total Inventario
```dax
-- Valor Total Inventario = SUM(Productos[valor_inventario])
```
**Alternativa si no existe valor_inventario**:
```dax
-- Valor Total Inventario = SUMX(Productos, Productos[stock] * Productos[precio_unitario])
```
**Formato**: Moneda ($)

---

### Medida 3: Stock Total
```dax
-- Stock Total = SUM(Productos[stock])
```
**Formato**: Número entero

---

### Medida 4: Promedio de Stock por Categoría
```dax
-- Promedio de Stock por Categoría = AVERAGE(Productos[stock])
```
**Formato**: Número decimal (2 decimales)

---

### Medida 5: Total Productos Únicos
```dax
-- Total Productos Únicos = DISTINCTCOUNT(Productos[id])
```
**Formato**: Número entero

---

### Medida 6: Productos con Stock Bajo
```dax
-- Productos Stock Bajo = 
CALCULATE(
    COUNTROWS(Productos),
    FILTER(Productos, Productos[stock] < 20)
)
```
**Formato**: Número entero

---

### Medida 7: Estado de Inventario
```dax
-- Estado Inventario = 
SWITCH(
    TRUE(),
    [-- Stock Total] < 100, "Stock Bajo",
    [-- Stock Total] < 300, "Stock Medio",
    "Stock Alto"
)
```
**Formato**: Texto

---

## 💰 TABLA: Ventas

### Medida 8: Total de Ventas
```dax
-- Total de Ventas = SUM(Ventas[total])
```
**Si la columna tiene otro nombre** (ej: monto, importe):
```dax
-- Total de Ventas = SUM(Ventas[monto])
```
**Formato**: Moneda ($)

---

### Medida 9: Ingresos Totales
```dax
-- Ingresos Totales = SUM(Ventas[total])
```
**O desde Detalle_Ventas**:
```dax
-- Ingresos Totales = SUMX(Detalle_Ventas, Detalle_Ventas[cantidad] * Detalle_Ventas[precio_unitario])
```
**Formato**: Moneda ($)

---

### Medida 10: Ventas del Mes Actual
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
**NOTA**: Ajusta `fecha` si tu columna tiene otro nombre (Fecha, date, fecha_venta, etc.)
**Formato**: Moneda ($)

---

### Medida 11: Ventas del Mes Anterior
```dax
-- Ventas Mes Anterior = 
CALCULATE(
    SUM(Ventas[total]),
    DATEADD(Ventas[fecha], -1, MONTH)
)
```
**Formato**: Moneda ($)

---

### Medida 12: Ventas YTD (Año a la Fecha)
```dax
-- Ventas YTD = 
CALCULATE(
    SUM(Ventas[total]),
    DATESYTD(Ventas[fecha])
)
```
**Formato**: Moneda ($)

---

### Medida 13: Variación Interanual (YoY)
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
**Formato**: Porcentaje (%)

---

### Medida 14: Crecimiento Mes a Mes (MoM)
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
        DIVIDE(
            VentasActuales - VentasMesAnterior,
            VentasMesAnterior,
            0
        ),
        BLANK()
    )
```
**Formato**: Porcentaje (%)

---

## 📈 KPIs - TABLA: Productos

### KPI 1: Rotación de Inventario

#### Valor Actual:
```dax
-- Rotación de Inventario = 
DIVIDE(
    [-- Total de Productos Vendidos],
    [-- Stock Total],
    0
)
```
**Formato**: Número decimal (2 decimales)

#### Objetivo:
```dax
-- Objetivo Rotación = 2.5
```
**Formato**: Número decimal

#### Estado:
```dax
-- Estado Rotación = 
IF(
    [-- Rotación de Inventario] >= [-- Objetivo Rotación],
    "✅ Objetivo Alcanzado",
    "⚠️ Por Debajo del Objetivo"
)
```
**Formato**: Texto

---

## 💵 KPIs - TABLA: Ventas

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
**Versión simplificada** (si no tienes precio_costo):
```dax
-- Margen Utilidad = 
VAR Ingresos = [-- Ingresos Totales]
VAR CostosEstimados = Ingresos * 0.7
RETURN
    DIVIDE(Ingresos - CostosEstimados, Ingresos, 0)
```
**Formato**: Porcentaje (%)

#### Objetivo:
```dax
-- Objetivo Margen = 0.30
```
**Formato**: Porcentaje (30%)

#### Estado:
```dax
-- Estado Margen = 
SWITCH(
    TRUE(),
    [-- Margen Utilidad] >= [-- Objetivo Margen], "✅ Excelente",
    [-- Margen Utilidad] >= [-- Objetivo Margen] * 0.8, "⚠️ Aceptable",
    "❌ Bajo"
)
```
**Formato**: Texto

---

### KPI 3: Nivel de Servicio

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
**Versión simplificada**:
```dax
-- Nivel Servicio = 
DIVIDE(
    COUNTROWS(Ventas) - [-- Productos Stock Bajo],
    COUNTROWS(Ventas),
    0
)
```
**Formato**: Porcentaje (%)

#### Objetivo:
```dax
-- Objetivo Nivel Servicio = 0.95
```
**Formato**: Porcentaje (95%)

#### Estado:
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
**Formato**: Texto

---

## 🔍 MEDIDAS ADICIONALES (Opcionales)

### Medida 15: Promedio Móvil de 3 Meses
```dax
-- Promedio Móvil 3 Meses = 
CALCULATE(
    AVERAGEX(
        DATESINPERIOD(
            Ventas[fecha],
            MAX(Ventas[fecha]),
            -3,
            MONTH
        ),
        [-- Total de Ventas]
    )
)
```
**Formato**: Moneda ($)

---

### Medida 16: Top 10 Productos por Ventas
```dax
-- Top 10 Productos = 
CALCULATE(
    SUM(Detalle_Ventas[cantidad]),
    TOPN(
        10,
        ALL(Productos[nombre]),
        [-- Total de Productos Vendidos]
    )
)
```
**Formato**: Número entero

---

### Medida 17: Resumen de Categorías (Texto)
```dax
-- Resumen Categorías = 
CONCATENATEX(
    VALUES(Productos[categoria]),
    Productos[categoria] & ": " & 
    CALCULATE(COUNT(Productos[id])),
    ", "
)
```
**Formato**: Texto

---

## ⚠️ NOTAS IMPORTANTES

1. **Nombres de Columnas**: Ajusta los nombres de columnas según tu modelo de datos
   - `fecha` podría ser `Fecha`, `date`, `fecha_venta`
   - `total` podría ser `monto`, `importe`, `precio`
   - `stock` podría ser `inventario`, `cantidad_stock`

2. **Nombres de Tablas**: Verifica que las tablas existan:
   - `Productos`
   - `Ventas`
   - `Detalle_Ventas`
   - `Clientes`

3. **Dependencias**: Algunas medidas dependen de otras:
   - `-- Crecimiento MoM` necesita `-- Total de Ventas`
   - `-- Estado Rotación` necesita `-- Rotación de Inventario` y `-- Objetivo Rotación`
   - Crea primero las medidas básicas

4. **Relaciones**: Asegúrate de que las relaciones entre tablas estén configuradas correctamente

---

## 📝 CHECKLIST DE CREACIÓN

### Medidas Básicas (Crear primero)
- [ ] -- Total de Productos Vendidos
- [ ] -- Valor Total Inventario
- [ ] -- Stock Total
- [ ] -- Promedio de Stock por Categoría
- [ ] -- Total Productos Únicos

### Medidas Intermedias
- [ ] -- Total de Ventas
- [ ] -- Ingresos Totales
- [ ] -- Productos Stock Bajo

### Medidas Avanzadas
- [ ] -- Ventas Mes Actual
- [ ] -- Ventas Mes Anterior
- [ ] -- Ventas YTD
- [ ] -- Variación YoY
- [ ] -- Crecimiento MoM
- [ ] -- Estado Inventario

### KPIs
- [ ] -- Rotación de Inventario
- [ ] -- Objetivo Rotación
- [ ] -- Estado Rotación
- [ ] -- Margen Utilidad
- [ ] -- Objetivo Margen
- [ ] -- Estado Margen
- [ ] -- Nivel Servicio
- [ ] -- Objetivo Nivel Servicio
- [ ] -- Estado Nivel Servicio

---

**Total de Medidas**: 17+

---

## 🚀 PRÓXIMOS PASOS

Después de crear todas las medidas:

1. Verifica que todas funcionen (arrastra a una tabla)
2. Crea las jerarquías (ver `Documentacion_Sprint4.md`)
3. Configura los visuales KPI en el informe
4. Prueba el dashboard completo

---

**Para más detalles, consulta**: `Guia_Paso_a_Paso_Medidas_DAX.md`

