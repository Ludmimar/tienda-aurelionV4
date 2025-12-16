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

**📊 ¿Qué muestra esta medida?**

Esta medida calcula las **ventas acumuladas desde el 1 de enero del año actual hasta la fecha más reciente** en el contexto.

**Ejemplos:**
- Si estás en **Enero 2025**: Muestra ventas de enero 2025
- Si estás en **Junio 2025**: Muestra ventas acumuladas de enero a junio 2025
- Si estás en **Diciembre 2025**: Muestra todas las ventas del año 2025

**Cómo funciona:**
- `DATESYTD()` incluye todas las fechas desde el 1 de enero del año actual
- Suma todas las ventas desde el inicio del año hasta la fecha en el contexto
- Es útil para ver el progreso del año

**Ejemplo práctico:**
- Si tienes un gráfico por mes y usas esta medida, cada mes mostrará el acumulado desde enero
- Enero 2025: $158,119
- Febrero 2025: $282,586 (Enero + Febrero)
- Marzo 2025: $428,568 (Enero + Febrero + Marzo)
- Y así sucesivamente...

---

### Medida 13: Variación Interanual (YoY) / Crecimiento Anual
**📊 Esta medida tiene dos versiones dependiendo de lo que necesites:**

**Versión A: Compara año completo vs año anterior (FUNCIONA CON 3 AÑOS - RESPETA CONTEXTO DEL VISUAL)**
```dax
-- Crecimiento Anual de Ventas = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR AnioActual = 
    IF(
        HASONEVALUE(Ventas[fecha]),
        YEAR(VALUES(Ventas[fecha])),
        IF(
            HASONEVALUE(YEAR(Ventas[fecha])),
            VALUES(YEAR(Ventas[fecha])),
            YEAR(MAX(Ventas[fecha]))
        )
    )
VAR AnioAnterior = AnioActual - 1
VAR VentasAnioAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas),
            YEAR(Ventas[fecha]) = AnioAnterior
        )
    )
RETURN
    IF(
        ISBLANK(VentasAnioAnterior) || VentasAnioAnterior = 0 || AnioAnterior < 2023,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasAnioAnterior,
            VentasAnioAnterior,
            0
        ) * 100
    )
```

**✅ Versión SIMPLIFICADA que FUNCIONA mejor (USA EL AÑO DEL CONTEXTO DE CADA FILA):**
```dax
-- Crecimiento Anual de Ventas = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR AnioActual = 
    IF(
        HASONEVALUE(Ventas[fecha]),
        YEAR(SELECTEDVALUE(Ventas[fecha])),
        YEAR(MAX(Ventas[fecha]))
    )
VAR AnioAnterior = AnioActual - 1
VAR VentasAnioAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas),
            YEAR(Ventas[fecha]) = AnioAnterior
        )
    )
RETURN
    IF(
        ISBLANK(VentasAnioAnterior) || VentasAnioAnterior = 0,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasAnioAnterior,
            VentasAnioAnterior,
            0
        ) * 100
    )
```

**✅ MEJOR SOLUCIÓN: Crear columna calculada de Año y usar en medida:**
1. **Primero crea una columna calculada en la tabla Ventas:**
   ```dax
   -- Año (columna) = YEAR(Ventas[fecha])
   ```

2. **Luego usa esta medida (que funciona perfecto con agrupación por año):**
   ```dax
   -- Crecimiento Anual de Ventas = 
   VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
   VAR AnioActual = SELECTEDVALUE(Ventas[Año])
   VAR AnioAnterior = AnioActual - 1
   VAR VentasAnioAnterior = 
       CALCULATE(
           SUM(Ventas[total]),
           FILTER(
               ALL(Ventas),
               Ventas[Año] = AnioAnterior
           )
       )
   RETURN
       IF(
           ISBLANK(VentasAnioAnterior) || VentasAnioAnterior = 0,
           BLANK(),
           DIVIDE(
               VentasActuales - VentasAnioAnterior,
               VentasAnioAnterior,
               0
           ) * 100
       )
   ```

**🔍 Cómo usar para ver los 3 años:**
1. Crea un gráfico de columnas o tabla
2. Eje/Columnas: Arrastra `Ventas[Año]` (la columna calculada) o `Ventas[fecha]` → Formato → Nivel de fecha: "Año"
3. Valores: Arrastra `-- Crecimiento Anual de Ventas`
4. **Deberías ver**: 2023 (BLANK), 2024 (crecimiento vs 2023), 2025 (crecimiento vs 2024) ✅

**Versión B: Compara mismo período del año anterior (Para comparaciones mes a mes)**

**✅ Versión QUE FUNCIONA (Usa función de tiempo como YTD - compara período específico):**
```dax
-- Variación YoY = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR VentasAnioAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        SAMEPERIODLASTYEAR(Ventas[fecha])
    )
RETURN
    IF(
        ISBLANK(VentasAnioAnterior) || VentasAnioAnterior = 0,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasAnioAnterior,
            VentasAnioAnterior,
            0
        ) * 100
    )
```

**🔍 Usa SAMEPERIODLASTYEAR (función de tiempo estándar) igual que YTD usa DATESYTD**

**✅ Versión SIMPLIFICADA (Recomendada si la primera no funciona):**
```dax
-- Variación YoY = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR FechaMax = MAX(Ventas[fecha])
VAR AnioActual = YEAR(FechaMax)
VAR MesActual = MONTH(FechaMax)
VAR AnioAnterior = AnioActual - 1
VAR VentasAnioAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas[fecha]),
            YEAR(Ventas[fecha]) = AnioAnterior &&
            MONTH(Ventas[fecha]) = MesActual
        )
    )
RETURN
    IF(
        ISBLANK(VentasAnioAnterior) || VentasAnioAnterior = 0,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasAnioAnterior,
            VentasAnioAnterior,
            0
        ) * 100
    )
```

**🔍 Esta versión usa `ALL(Ventas[fecha])` para respetar el contexto (igual que MoM que funciona)**

**Formato**: Porcentaje (%)

**✅ SOLUCIÓN APLICADA:**
- Se agregaron datos de 2023, 2024 y 2025 a los CSV
- Ahora tienes datos de 3 años completos para comparación YoY
- **2023**: 372 ventas - $1,049,824.73 (Mayo-Diciembre)
- **2024**: 372 ventas - $1,062,852.92 (Mayo-Diciembre)  
- **2025**: 752 ventas - $2,379,416.26 (Enero-Diciembre) ✅
- **Crecimiento 2025 vs 2024**: ~123.8% (2025 tiene más del doble de ventas)
- Usa la "Versión A: Compara año completo" para ver el crecimiento total anual

**🔍 Solución de problemas:**
- Si muestra BLANK: Verifica que tengas datos de ambos años en el mismo período
- La medida compara el mismo período del año anterior usando SAMEPERIODLASTYEAR
- Ejemplo: Enero 2025 vs Enero 2024, Diciembre 2025 vs Diciembre 2024
- Si estás en 2025, la comparación será automáticamente con 2024

---

### Medida 14: Crecimiento Mes a Mes (MoM)
**⚠️ NOTA IMPORTANTE**: Esta medida requiere que tengas datos de al menos 2 meses consecutivos.

**✅ Versión QUE FUNCIONA (Usa función de tiempo como YTD):**
```dax
-- Crecimiento MoM = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR VentasMesAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        DATEADD(Ventas[fecha], -1, MONTH)
    )
RETURN
    IF(
        ISBLANK(VentasMesAnterior) || VentasMesAnterior = 0,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasMesAnterior,
            VentasMesAnterior,
            0
        ) * 100
    )
```

**🔍 Usa DATEADD (función de tiempo estándar) igual que YTD usa DATESYTD**

**Versión CORREGIDA (Resuelve el problema de "mes a mes"):**
```dax
-- Crecimiento MoM = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR FechaMax = MAX(Ventas[fecha])
VAR AnioActual = YEAR(FechaMax)
VAR MesActual = MONTH(FechaMax)
VAR MesAnterior = IF(MesActual = 1, 12, MesActual - 1)
VAR AnioAnterior = IF(MesActual = 1, AnioActual - 1, AnioActual)
VAR VentasMesAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas[fecha]),
            YEAR(Ventas[fecha]) = AnioAnterior &&
            MONTH(Ventas[fecha]) = MesAnterior
        )
    )
RETURN
    IF(
        ISBLANK(VentasMesAnterior) || VentasMesAnterior <= 0,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasMesAnterior,
            VentasMesAnterior,
            0
        ) * 100
    )
```

**✅ Versión ALTERNATIVA con PREVIOUSMONTH (Solo si tienes tabla de fechas):**
```dax
-- Crecimiento MoM (Con PREVIOUSMONTH) = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR VentasMesAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        PREVIOUSMONTH(Ventas[fecha])
    )
RETURN
    IF(
        ISBLANK(VentasMesAnterior) || VentasMesAnterior <= 0,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasMesAnterior,
            VentasMesAnterior,
            0
        ) * 100
    )
```
**Nota**: Esta versión solo funciona si tienes una tabla de fechas configurada correctamente. Si no tienes tabla de fechas, usa la versión RECOMENDADA.

**🔍 Cómo usar en visuales para ver mes a mes:**
1. Crea un gráfico de columnas o líneas
2. Arrastra `Ventas[fecha]` al Eje (en Formato → Tipo de categoría → selecciona "Fecha" y agrupa por Mes)
3. Arrastra `-- Crecimiento MoM` a Valores
4. Cada columna/punto mostrará el crecimiento de ese mes vs el mes anterior

**⚠️ IMPORTANTE**: Para que funcione "mes a mes", asegúrate de que el Eje esté agrupado por MES (no por fecha completa)

**❌ Versión ALTERNATIVA 1 (NO funciona mes a mes - no usar):**
~~Esta versión no funciona correctamente en visuales porque usa `ALL(Ventas)` en lugar de `ALL(Ventas[fecha])`~~

**❌ Versión ALTERNATIVA 2 (NO funciona mes a mes - no usar):**
~~Esta versión tampoco funciona porque usa `ALL(Ventas)` en lugar de `ALL(Ventas[fecha])`~~

**⚠️ Versión MEJORADA (Funciona pero más compleja - usar la RECOMENDADA mejor):**
```dax
-- Crecimiento MoM = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR FechaActual = MAX(Ventas[fecha])
VAR AñoActual = YEAR(FechaActual)
VAR MesActual = MONTH(FechaActual)
VAR MesAnterior = IF(MesActual = 1, 12, MesActual - 1)
VAR AñoMesAnterior = IF(MesActual = 1, AñoActual - 1, AñoActual)
VAR VentasMesAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas),
            YEAR(Ventas[fecha]) = AñoMesAnterior &&
            MONTH(Ventas[fecha]) = MesAnterior
        )
    )
RETURN
    IF(
        ISBLANK(VentasMesAnterior) || VentasMesAnterior <= 0,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasMesAnterior,
            VentasMesAnterior,
            0
        ) * 100
    )
```

**⚠️ Versión DEFINITIVA (Más compleja - usar la RECOMENDADA mejor):**
```dax
-- Crecimiento MoM = 
VAR VentasActuales = 
    CALCULATE(
        SUM(Ventas[total])
    )
VAR AñoActual = 
    IF(
        ISFILTERED(Ventas[fecha]),
        YEAR(MAX(Ventas[fecha])),
        YEAR(MAX(Ventas[fecha]))
    )
VAR MesActual = 
    IF(
        ISFILTERED(Ventas[fecha]),
        MONTH(MAX(Ventas[fecha])),
        MONTH(MAX(Ventas[fecha]))
    )
VAR MesAnterior = IF(MesActual = 1, 12, MesActual - 1)
VAR AñoMesAnterior = IF(MesActual = 1, AñoActual - 1, AñoActual)
VAR VentasMesAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas[fecha]),
            YEAR(Ventas[fecha]) = AñoMesAnterior &&
            MONTH(Ventas[fecha]) = MesAnterior
        )
    )
RETURN
    IF(
        ISBLANK(VentasMesAnterior) || VentasMesAnterior = 0,
        BLANK(),
        DIVIDE(
            VentasActuales - VentasMesAnterior,
            VentasMesAnterior,
            0
        ) * 100
    )
```

**🔍 SOLUCIÓN DE PROBLEMAS si NO muestra nada (BLANK):**

1. **Verifica que tienes datos de al menos 2 meses diferentes:**
   - Crea una visualización con `Ventas[fecha]` y cuenta los meses únicos
   - Si solo hay 1 mes, la medida mostrará BLANK (no hay mes anterior)

2. **Verifica el nombre de la columna de fecha:**
   - Si tu columna se llama diferente (ej: `Fecha`, `date`, `fecha_venta`), cambia `Ventas[fecha]` por el nombre correcto
   - Verifica que la columna esté formateada como **Fecha** en Power BI

3. **Prueba esta versión de diagnóstico primero:**
```dax
-- Test MoM (Diagnóstico) = 
VAR VentasActuales = SUM(Ventas[total])
VAR FechaMax = MAX(Ventas[fecha])
VAR MesActual = MONTH(FechaMax)
VAR AñoActual = YEAR(FechaMax)
VAR MesAnterior = IF(MesActual = 1, 12, MesActual - 1)
VAR AñoAnterior = IF(MesActual = 1, AñoActual - 1, AñoActual)
VAR VentasMesAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas),
            YEAR(Ventas[fecha]) = AñoAnterior &&
            MONTH(Ventas[fecha]) = MesAnterior
        )
    )
RETURN
    IF(
        ISBLANK(VentasMesAnterior) || VentasMesAnterior = 0,
        "Sin datos mes anterior", // Cambiar a BLANK() después de verificar
        DIVIDE(
            VentasActuales - VentasMesAnterior,
            VentasMesAnterior,
            0
        ) * 100
    )
```

4. **Si usas la medida en un visual con filtros de fecha:**
   - Asegúrate de que el filtro incluya al menos 2 meses
   - Prueba sin filtros primero para verificar que funciona

5. **Si sigue sin funcionar:**
   - Usa la **Versión ALTERNATIVA 1** (usa año*100 + mes)
   - Verifica que `SUM(Ventas[total])` funciona correctamente primero
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

