# 📈 Medida de Crecimiento de Ventas por Año

## 🔍 Problema
La medida muestra que se vendió más en 2024 cuando en realidad 2025 tiene más ventas.

## ✅ Solución: Medida de Crecimiento Anual

### Medida 1: Crecimiento de Ventas por Año (Comparación año anterior)

```dax
-- Crecimiento Anual de Ventas = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR AnioActual = YEAR(MAX(Ventas[fecha]))
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

### Medida 2: Total de Ventas por Año (Para verificar)

```dax
-- Total Ventas por Año = 
CALCULATE(
    SUM(Ventas[total]),
    FILTER(
        ALL(Ventas),
        YEAR(Ventas[fecha]) = YEAR(MAX(Ventas[fecha]))
    )
)
```

### Medida 3: Ventas Año Anterior (Para comparar)

```dax
-- Ventas Año Anterior = 
VAR AnioActual = YEAR(MAX(Ventas[fecha]))
VAR AnioAnterior = AnioActual - 1
RETURN
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas),
            YEAR(Ventas[fecha]) = AnioAnterior
        )
    )
```

## 📊 Cómo usar

1. **Para ver el crecimiento anual:**
   - Crea un gráfico con `Ventas[fecha]` agrupado por Año en el Eje
   - Agrega `-- Crecimiento Anual de Ventas` a Valores
   - Mostrará el % de crecimiento de cada año vs el anterior

2. **Para verificar los totales:**
   - Crea una tabla con:
     - `Ventas[fecha]` agrupado por Año
     - `-- Total Ventas por Año`
     - `-- Ventas Año Anterior`
     - `-- Crecimiento Anual de Ventas`
   - Deberías ver:
     - 2023: $1,049,824.73
     - 2024: $1,062,852.92 (crecimiento ~1.2% vs 2023)
     - 2025: $2,379,416.26 (crecimiento ~123.8% vs 2024) ✅

## 🔧 Si sigue mostrando datos incorrectos

1. **Actualiza los datos en Power BI:**
   - Presiona F5 o Inicio → Actualizar
   - Verifica que cargue 1,496 ventas

2. **Verifica que la medida use los datos correctos:**
   - Crea una tabla simple con `SUM(Ventas[total])` agrupado por año
   - Deberías ver los totales correctos

3. **Si el problema persiste:**
   - Puede ser caché de Power BI
   - Cierra y vuelve a abrir Power BI Desktop
   - O usa la medida de "Total Ventas por Año" que usa FILTER explícito

