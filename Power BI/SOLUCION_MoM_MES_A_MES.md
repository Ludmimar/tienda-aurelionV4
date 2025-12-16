# ✅ Solución: Crecimiento MoM Mes a Mes

## 🔍 Problema
La medida MoM no muestra valores diferentes para cada mes en un visual, muestra el mismo valor o solo un valor.

## ✅ Solución Correcta

### Versión que funciona mes a mes:

```dax
-- Crecimiento MoM = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR FechaMax = MAX(Ventas[fecha])
VAR AñoActual = YEAR(FechaMax)
VAR MesActual = MONTH(FechaMax)
VAR MesAnterior = IF(MesActual = 1, 12, MesActual - 1)
VAR AñoAnterior = IF(MesActual = 1, AñoActual - 1, AñoActual)
VAR VentasMesAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas[fecha]),
            YEAR(Ventas[fecha]) = AñoAnterior &&
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

## 📊 Cómo configurar el Visual

### Paso 1: Crear el Visual
1. Crea un **Gráfico de Columnas** o **Gráfico de Líneas**

### Paso 2: Configurar el Eje
1. Arrastra `Ventas[fecha]` al campo **Eje**
2. Selecciona el campo `Ventas[fecha]` en el panel de campos
3. Ve a **Formato visual** (icono de rodillo)
4. Expande la sección **Eje X**
5. Busca **Tipo de categoría** → selecciona **"Fecha"**
6. Busca **Nivel de jerarquía** → selecciona **"Mes"** o **"Mes y año"**

### Paso 3: Agregar la Medida
1. Arrastra `-- Crecimiento MoM` al campo **Valores**
2. Cada mes debería mostrar su crecimiento vs el mes anterior

## 🔧 Si sigue sin funcionar

### Opción 1: Crear columna calculada de Mes-Año
```dax
-- MesAño (Columna Calculada en tabla Ventas)
MesAño = FORMAT(Ventas[fecha], "YYYY-MM")
```

Luego usa esta medida:
```dax
-- Crecimiento MoM (Con columna MesAño) = 
VAR VentasActuales = CALCULATE(SUM(Ventas[total]))
VAR MesAñoActual = MAX(Ventas[MesAño])
VAR AñoActual = LEFT(MesAñoActual, 4)
VAR MesActual = RIGHT(MesAñoActual, 2)
VAR MesAnterior = 
    IF(
        MesActual = "01",
        "12",
        FORMAT(VALUE(MesActual) - 1, "00")
    )
VAR AñoAnterior = 
    IF(
        MesActual = "01",
        FORMAT(VALUE(AñoActual) - 1, "0000"),
        AñoActual
    )
VAR MesAñoAnterior = AñoAnterior & "-" & MesAnterior
VAR VentasMesAnterior = 
    CALCULATE(
        SUM(Ventas[total]),
        FILTER(
            ALL(Ventas),
            Ventas[MesAño] = MesAñoAnterior
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

### Opción 2: Usar PREVIOUSMONTH (requiere tabla de fechas)
Si tienes una tabla de fechas relacionada:
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

## 📝 Verificación

Para verificar que funciona:
1. Crea una tabla con `Ventas[fecha]` (agrupado por mes) y `-- Crecimiento MoM`
2. Deberías ver un valor diferente para cada mes
3. El primer mes de cada año mostrará BLANK (no hay mes anterior)

## ✅ Cambios Importantes

1. **Usa `ALL(Ventas[fecha])` en lugar de `ALL(Ventas)`** - Esto respeta el contexto de filtros
2. **Configura el visual para agrupar por MES** - No uses fecha completa
3. **Verifica que cada mes sea una categoría separada** - Deberías ver múltiples barras/columnas

