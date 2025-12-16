# Notebook de Ejemplos DAX - Tienda Aurelion
## Guía Práctica de Implementación en Power BI

---

## Introducción

Este notebook contiene ejemplos prácticos y explicaciones detalladas de cada medida DAX utilizada en el proyecto. Cada ejemplo incluye:
- Código DAX completo
- Explicación de la lógica
- Casos de uso
- Ejemplo de resultado esperado

---

## 1. MEDIDAS DE AGREGACIÓN

### 1.1 SUM - Suma Simple

```dax
-- Total de Productos Vendidos = 
SUM(Detalle_Ventas[cantidad])
```

**Explicación:**
- `SUM()` suma todos los valores de la columna `cantidad` en la tabla `Detalle_Ventas`
- Esta es la forma más básica de agregación
- Respeta los filtros del contexto actual

**Uso en visualizaciones:**
- Tarjetas (Cards)
- Gráficos de barras/columnas
- Totalizadores en tablas

---

### 1.2 AVERAGE - Promedio

```dax
-- Promedio de Stock por Categoría = 
AVERAGE(Productos[stock])
```

**Explicación:**
- Calcula el promedio aritmético de todos los valores en `Productos[stock]`
- Útil para entender niveles típicos de stock

**Variación con contexto:**
```dax
-- Promedio Stock por Categoría (con contexto) = 
CALCULATE(
    AVERAGE(Productos[stock]),
    VALUES(Productos[categoria])
)
```

---

### 1.3 DISTINCTCOUNT - Conteo de Valores Únicos

```dax
-- Total Productos Únicos = 
DISTINCTCOUNT(Productos[id])
```

**Explicación:**
- Cuenta cuántos valores únicos hay en la columna `id`
- Útil para evitar duplicados en el conteo

**Comparación con COUNT:**
- `COUNT()`: Cuenta todas las filas (puede incluir duplicados)
- `DISTINCTCOUNT()`: Cuenta valores únicos

---

## 2. FUNCIONES DE FILTRO Y CONTEXTO

### 2.1 CALCULATE - Modificar Contexto

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

**Explicación paso a paso:**
1. `CALCULATE()` modifica el contexto de evaluación
2. `SUM(Ventas[total])` es la expresión a evaluar
3. `FILTER()` crea una tabla filtrada
4. Las condiciones dentro de `FILTER()` limitan a ventas del mes actual

**Funciones utilizadas:**
- `CALCULATE`: Función más importante de DAX para modificar contexto
- `FILTER`: Crea una tabla filtrada
- `YEAR()`, `MONTH()`, `TODAY()`: Funciones de fecha

---

### 2.2 FILTER con Múltiples Condiciones

```dax
-- Productos Stock Bajo = 
CALCULATE(
    COUNTROWS(Productos),
    FILTER(
        Productos, 
        Productos[stock] < 20 &&
        Productos[categoria] = "Pociones"
    )
)
```

**Explicación:**
- Filtra productos con stock menor a 20 Y de categoría "Pociones"
- `COUNTROWS()` cuenta las filas que cumplen la condición
- El operador `&&` es equivalente a AND

---

## 3. FUNCIONES DE TIEMPO

### 3.1 DATEADD - Desplazamiento de Fechas

```dax
-- Ventas Mes Anterior = 
CALCULATE(
    SUM(Ventas[total]),
    DATEADD(Ventas[fecha], -1, MONTH)
)
```

**Explicación:**
- `DATEADD(tabla[fecha], -1, MONTH)` desplaza las fechas un mes hacia atrás
- Compara el período actual con el período anterior

**Variaciones:**
```dax
-- Ventas del Próximo Mes = 
DATEADD(Ventas[fecha], 1, MONTH)

-- Ventas del Año Anterior = 
DATEADD(Ventas[fecha], -1, YEAR)

-- Ventas de Hace 7 Días = 
DATEADD(Ventas[fecha], -7, DAY)
```

---

### 3.2 DATESYTD - Año a la Fecha

```dax
-- Ventas YTD = 
CALCULATE(
    SUM(Ventas[total]),
    DATESYTD(Ventas[fecha])
)
```

**Explicación:**
- `DATESYTD()` incluye todas las fechas desde el 1 de enero del año actual hasta la fecha más reciente en el contexto
- Útil para análisis acumulativo del año

**Ejemplo de resultado:**
- Si estamos en marzo, suma ventas de enero + febrero + marzo
- Si estamos en diciembre, suma todo el año

---

### 3.3 SAMEPERIODLASTYEAR - Comparación Interanual

```dax
-- Ventas Año Anterior = 
CALCULATE(
    SUM(Ventas[total]),
    SAMEPERIODLASTYEAR(Ventas[fecha])
)
```

**Explicación:**
- Compara el mismo período del año anterior
- Si estamos viendo marzo 2025, compara con marzo 2024
- Mantiene la estructura del período actual (mes, trimestre, etc.)

**Ejemplo completo de variación YoY:**
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

---

## 4. FUNCIONES LÓGICAS Y CONDICIONALES

### 4.1 IF - Condicional Simple

```dax
-- Estado Stock = 
IF(
    SUM(Productos[stock]) < 20,
    "Bajo",
    "Normal"
)
```

**Explicación:**
- Sintaxis: `IF(condición, valor_si_verdadero, valor_si_falso)`
- Evalúa la condición y devuelve un valor u otro

---

### 4.2 SWITCH - Múltiples Condiciones

```dax
-- Estado Inventario = 
SWITCH(
    TRUE(),
    [-- Stock Total] < 100, "Stock Bajo",
    [-- Stock Total] < 300, "Stock Medio",
    "Stock Alto"
)
```

**Explicación:**
- `SWITCH(TRUE(), ...)` evalúa condiciones en orden
- La primera condición verdadera devuelve su valor asociado
- El último valor sin condición es el "default"

**Equivalente con IF anidados:**
```dax
IF([-- Stock Total] < 100, "Stock Bajo",
    IF([-- Stock Total] < 300, "Stock Medio",
        "Stock Alto"))
```

---

### 4.3 VAR/RETURN - Variables

```dax
-- Margen Utilidad = 
VAR Ingresos = SUM(Ventas[total])
VAR Costos = SUM(Detalle_Ventas[cantidad]) * 
    RELATED(Productos[precio_costo])
RETURN
    DIVIDE(Ingresos - Costos, Ingresos, 0)
```

**Explicación:**
- `VAR` define variables locales
- `RETURN` devuelve el resultado final
- Las variables se calculan una vez y se reutilizan
- Mejora legibilidad y rendimiento

---

## 5. FUNCIONES DE ITERACIÓN

### 5.1 SUMX - Suma con Iteración

```dax
-- Valor Total Inventario = 
SUMX(
    Productos,
    Productos[stock] * Productos[precio_unitario]
)
```

**Explicación:**
- `SUMX()` itera sobre cada fila de la tabla
- Para cada producto, calcula `stock * precio_unitario`
- Suma todos los resultados

**¿Cuándo usar SUMX vs SUM?**
- `SUM()`: Cuando solo necesitas sumar una columna
- `SUMX()`: Cuando necesitas calcular algo antes de sumar

**Ejemplo adicional:**
```dax
-- Total con Descuento = 
SUMX(
    Ventas,
    Ventas[total] * (1 - Ventas[descuento])
)
```

---

### 5.2 AVERAGEX - Promedio con Iteración

```dax
-- Promedio de Valor por Categoría = 
AVERAGEX(
    VALUES(Productos[categoria]),
    CALCULATE(SUM(Productos[valor_inventario]))
)
```

**Explicación:**
- Itera sobre cada categoría única
- Calcula el valor total de inventario por categoría
- Promedia esos totales

---

### 5.3 COUNTROWS - Contar Filas

```dax
-- Total de Transacciones = 
COUNTROWS(Ventas)
```

**Explicación:**
- Cuenta el número de filas en la tabla
- Útil para contar registros que cumplen ciertas condiciones

**Con filtro:**
```dax
-- Ventas del Mes = 
CALCULATE(
    COUNTROWS(Ventas),
    FILTER(Ventas, MONTH(Ventas[fecha]) = MONTH(TODAY()))
)
```

---

## 6. FUNCIONES DE TEXTO

### 6.1 CONCATENATEX - Concatenar con Iteración

```dax
-- Resumen Categorías = 
CONCATENATEX(
    VALUES(Productos[categoria]),
    Productos[categoria] & ": " & 
    CALCULATE(COUNT(Productos[id])),
    ", "
)
```

**Explicación:**
- Itera sobre cada categoría única
- Concatena el nombre de la categoría con su conteo
- Separa con ", "

**Resultado ejemplo:**
```
"Armas: 15, Armaduras: 12, Pociones: 10"
```

---

## 7. FUNCIONES DE RELACIÓN

### 7.1 RELATED - Traer Datos de Tabla Relacionada

```dax
-- Precio Costo en Detalle Ventas = 
RELATED(Productos[precio_costo])
```

**Explicación:**
- `RELATED()` trae valores de una tabla relacionada (uno a muchos)
- Solo funciona en el lado "muchos" de la relación

**Uso en medida:**
```dax
-- Costo Total Venta = 
SUMX(
    Detalle_Ventas,
    Detalle_Ventas[cantidad] * 
    RELATED(Productos[precio_costo])
)
```

---

### 7.2 RELATEDTABLE - Traer Tabla Relacionada

```dax
-- Ventas por Producto = 
COUNTROWS(RELATEDTABLE(Detalle_Ventas))
```

**Explicación:**
- `RELATEDTABLE()` devuelve una tabla filtrada con filas relacionadas
- Útil para contar o agregar datos del lado "uno" de una relación

---

## 8. CONSTRUCCIÓN DE KPIs

### Estructura Completa de KPI

#### Paso 1: Valor Actual
```dax
-- Rotación de Inventario = 
DIVIDE(
    [-- Total de Productos Vendidos],
    [-- Stock Total],
    0
)
```

#### Paso 2: Definir Objetivo
```dax
-- Objetivo Rotación = 2.5
```

#### Paso 3: Calcular Desviación
```dax
-- Desviación Objetivo = 
[-- Rotación de Inventario] - [-- Objetivo Rotación]
```

#### Paso 4: Calcular Porcentaje de Cumplimiento
```dax
-- % Cumplimiento Objetivo = 
DIVIDE(
    [-- Rotación de Inventario],
    [-- Objetivo Rotación],
    0
) * 100
```

#### Paso 5: Estado (Texto)
```dax
-- Estado Rotación = 
SWITCH(
    TRUE(),
    [-- Rotación de Inventario] >= [-- Objetivo Rotación], "✅ Objetivo Alcanzado",
    [-- Rotación de Inventario] >= [-- Objetivo Rotación] * 0.8, "⚠️ Cerca del Objetivo",
    "❌ Por Debajo del Objetivo"
)
```

#### Paso 6: Estado (Número para indicadores)
```dax
-- Indicador Estado = 
IF(
    [-- Rotación de Inventario] >= [-- Objetivo Rotación],
    1,  -- Verde
    IF(
        [-- Rotación de Inventario] >= [-- Objetivo Rotación] * 0.8,
        0,  -- Amarillo
        -1  -- Rojo
    )
)
```

---

## 9. ANÁLISIS TEMPORAL AVANZADO

### Comparación Mes a Mes (MoM)

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

### Promedio Móvil de 3 Meses

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

---

## 10. MEJORES PRÁCTICAS

### Nomenclatura
- Usar prefijo `--` para medidas (ej: `-- Total Ventas`)
- Nombres descriptivos y en español
- Evitar espacios en nombres de medidas (usar guiones o camelCase)

### Performance
- Usar `VAR` para evitar cálculos repetidos
- Preferir `SUM()` sobre `SUMX()` cuando sea posible
- Limitar el uso de `FILTER()` dentro de `CALCULATE()` cuando no sea necesario

### Legibilidad
- Usar saltos de línea y sangría
- Agrupar lógica relacionada
- Comentar medidas complejas

---

## 11. TROUBLESHOOTING COMÚN

### Error: "A table of multiple values was supplied where a single value was expected"
**Causa:** Usando una tabla donde se espera un valor escalar
**Solución:** Usar funciones de agregación (SUM, COUNT, etc.)

### Error: "Cannot find table"
**Causa:** Nombre de tabla incorrecto o relación faltante
**Solución:** Verificar nombres exactos y relaciones en el modelo

### Medida devuelve valores incorrectos
**Causa:** Problemas con el contexto de filtro
**Solución:** Revisar uso de `CALCULATE()` y filtros

---

**Fin del Notebook**

