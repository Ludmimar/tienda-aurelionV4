# Guía Paso a Paso: Crear Medidas DAX en Power BI
## Tienda Aurelion - Sprint 4

---

## 📌 Índice

1. [Introducción](#introducción)
2. [Configuración Inicial](#configuración-inicial)
3. [Cómo Crear una Medida](#cómo-crear-una-medida)
4. [Medidas Básicas - Paso a Paso](#medidas-básicas---paso-a-paso)
5. [Medidas Intermedias - Paso a Paso](#medidas-intermedias---paso-a-paso)
6. [Medidas Avanzadas - Paso a Paso](#medidas-avanzadas---paso-a-paso)
7. [Crear KPIs - Paso a Paso](#crear-kpis---paso-a-paso)
8. [Verificar y Probar Medidas](#verificar-y-probar-medidas)
9. [Troubleshooting](#troubleshooting)

---

## Introducción

Esta guía te llevará paso a paso para crear todas las medidas DAX necesarias para el proyecto. Cada medida se explica con capturas conceptuales y código completo.

**Tiempo estimado**: 30-45 minutos para todas las medidas

---

## Configuración Inicial

### Paso 1: Abrir Power BI Desktop

1. **Abrir Power BI Desktop**
   - Busca "Power BI Desktop" en el menú de inicio
   - O ejecuta desde el escritorio

2. **Abrir tu archivo**
   - Click en **Archivo** → **Abrir** → **Examinar**
   - Navega hasta `Sprint4.pbix`
   - Click en **Abrir**

3. **Verificar que el modelo de datos esté cargado**
   - En el panel izquierdo, click en el ícono de **Modelo** (3 cuadrados conectados)
   - Deberías ver las tablas: Productos, Clientes, Ventas, Detalle_Ventas
   - Verifica que las relaciones entre tablas estén creadas

---

## Cómo Crear una Medida

### Método 1: Desde el Panel de Campos (Recomendado)

1. **Seleccionar la tabla donde crear la medida**
   - En el panel derecho, busca la tabla **Productos**
   - Click derecho sobre el nombre de la tabla **Productos**

2. **Crear nueva medida**
   - En el menú contextual, selecciona **"Nueva medida"**
   - O usa el atajo: **Alt + N + M**

3. **Editor de fórmulas**
   - Se abrirá el editor de fórmulas en la barra superior
   - Verás algo como: `Medida = `

4. **Escribir la fórmula DAX**
   - Borra `Medida` y escribe el nombre de tu medida
   - Escribe el signo `=` y luego la fórmula DAX
   - Ejemplo: `-- Total de Productos Vendidos = SUM(Detalle_Ventas[cantidad])`

5. **Aceptar la medida**
   - Presiona **Enter** o click en la marca de verificación ✓
   - La medida aparecerá en la tabla con un ícono de calculadora 🧮

### Método 2: Desde la Vista de Datos

1. **Ir a la Vista de Datos**
   - Click en el ícono de **"Vista de datos"** (tabla) en el panel izquierdo

2. **Seleccionar tabla**
   - En el panel derecho, selecciona la tabla donde crear la medida

3. **Crear medida**
   - En la cinta superior, click en **"Nueva medida"** (ícono de calculadora)
   - O usa **Ctrl + Shift + M**

---

## Medidas Básicas - Paso a Paso

### Medida 1: Total de Productos Vendidos

**Tabla**: Productos (o Detalle_Ventas)  
**Dificultad**: ⭐ Fácil

#### Paso a Paso:

1. **Crear nueva medida**
   - Click derecho en tabla **Productos** → **"Nueva medida"**

2. **Escribir el nombre y fórmula**
   ```
   -- Total de Productos Vendidos = SUM(Detalle_Ventas[cantidad])
   ```

3. **Explicación**:
   - `--` es el prefijo recomendado para medidas
   - `SUM()` suma todos los valores
   - `Detalle_Ventas[cantidad]` es la columna que queremos sumar

4. **Presionar Enter**
   - Verifica que no haya errores (no debe aparecer línea roja)
   - La medida aparece en la lista de campos de la tabla

5. **Formato (opcional)**
   - Click derecho en la medida → **"Formato de número"**
   - Selecciona **"Número entero"** o **"Número decimal"**

---

### Medida 2: Valor Total Inventario

**Tabla**: Productos  
**Dificultad**: ⭐ Fácil

#### Paso a Paso:

1. **Crear nueva medida en tabla Productos**

2. **Escribir la fórmula**
   ```
   -- Valor Total Inventario = SUM(Productos[valor_inventario])
   ```
   **NOTA**: Si no existe la columna `valor_inventario`, usar:
   ```
   -- Valor Total Inventario = SUMX(Productos, Productos[stock] * Productos[precio_unitario])
   ```

3. **Formato de moneda**
   - Click derecho en la medida → **"Formato de número"**
   - Selecciona **"Moneda"** o **"Moneda decimal"**
   - Selecciona símbolo: **$** (Dólar)

4. **Presionar Enter**

---

### Medida 3: Stock Total

**Tabla**: Productos  
**Dificultad**: ⭐ Fácil

#### Paso a Paso:

1. **Crear nueva medida en tabla Productos**

2. **Escribir la fórmula**
   ```
   -- Stock Total = SUM(Productos[stock])
   ```

3. **Formato**
   - Formato de número: **"Número entero"**

4. **Presionar Enter**

---

### Medida 4: Promedio de Stock por Categoría

**Tabla**: Productos  
**Dificultad**: ⭐⭐ Fácil-Medio

#### Paso a Paso:

1. **Crear nueva medida en tabla Productos**

2. **Escribir la fórmula**
   ```
   -- Promedio de Stock por Categoría = AVERAGE(Productos[stock])
   ```

3. **Explicación**:
   - `AVERAGE()` calcula el promedio
   - Power BI aplicará automáticamente el contexto de filtro si usas esta medida en un gráfico por categoría

4. **Formato**: Número decimal (2 decimales)

5. **Presionar Enter**

---

### Medida 5: Total Productos Únicos

**Tabla**: Productos  
**Dificultad**: ⭐ Fácil

#### Paso a Paso:

1. **Crear nueva medida en tabla Productos**

2. **Escribir la fórmula**
   ```
   -- Total Productos Únicos = DISTINCTCOUNT(Productos[id])
   ```

3. **Explicación**:
   - `DISTINCTCOUNT()` cuenta valores únicos (sin duplicados)
   - Útil para contar productos sin repetir

4. **Formato**: Número entero

5. **Presionar Enter**

---

## Medidas Intermedias - Paso a Paso

### Medida 6: Total de Ventas

**Tabla**: Ventas (crear nueva tabla o usar existente)  
**Dificultad**: ⭐⭐ Medio

#### Paso a Paso:

1. **Crear nueva medida**
   - Si no tienes tabla Ventas visible, puedes crearla o usar Productos
   - Click derecho en tabla **Ventas** → **"Nueva medida"**

2. **Escribir la fórmula**
   ```
   -- Total de Ventas = SUM(Ventas[total])
   ```
   
   **Si la columna se llama diferente, ajusta**:
   ```
   -- Total de Ventas = SUM(Ventas[monto])
   ```
   o
   ```
   -- Total de Ventas = SUMX(Detalle_Ventas, Detalle_Ventas[cantidad] * Detalle_Ventas[precio_unitario])
   ```

3. **Formato**: Moneda ($)

4. **Presionar Enter**

---

### Medida 7: Ingresos Totales

**Tabla**: Ventas o Productos  
**Dificultad**: ⭐⭐ Medio

#### Paso a Paso:

1. **Crear nueva medida en tabla Ventas**

2. **Escribir la fórmula**
   ```
   -- Ingresos Totales = SUM(Ventas[total])
   ```
   
   O si calculas desde detalle:
   ```
   -- Ingresos Totales = SUMX(Detalle_Ventas, Detalle_Ventas[cantidad] * Detalle_Ventas[precio_unitario])
   ```

3. **Formato**: Moneda ($)

4. **Presionar Enter**

---

### Medida 8: Productos con Stock Bajo

**Tabla**: Productos  
**Dificultad**: ⭐⭐⭐ Medio-Avanzado

#### Paso a Paso:

1. **Crear nueva medida en tabla Productos**

2. **Escribir la fórmula completa**
   ```
   -- Productos Stock Bajo = 
   CALCULATE(
       COUNTROWS(Productos),
       FILTER(Productos, Productos[stock] < 20)
   )
   ```

3. **Explicación paso a paso**:
   - `CALCULATE()` modifica el contexto
   - `COUNTROWS()` cuenta filas
   - `FILTER()` filtra productos con stock < 20
   - `<` significa "menor que"

4. **Formato de escritura en el editor**:
   - Puedes escribir todo en una línea
   - O usar Enter para separar líneas (mejora legibilidad)
   - Power BI acepta ambos formatos

5. **Presionar Enter**

6. **Verificar**: Debe mostrar un número entero

---

## Medidas Avanzadas - Paso a Paso

### Medida 9: Ventas del Mes Actual

**Tabla**: Ventas  
**Dificultad**: ⭐⭐⭐ Avanzado

#### Paso a Paso:

1. **Crear nueva medida en tabla Ventas**

2. **Escribir la fórmula**
   ```
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

3. **Importante - Sintaxis**:
   - `YEAR()` extrae el año de una fecha
   - `MONTH()` extrae el mes de una fecha
   - `TODAY()` devuelve la fecha actual
   - `&&` significa "Y" (AND lógico)
   - `=` compara igualdad

4. **Si tienes error con la columna `fecha`**:
   - Verifica el nombre exacto de la columna de fecha
   - Podría ser `Fecha`, `date`, `fecha_venta`, etc.
   - Ajusta el nombre en la fórmula

5. **Formato**: Moneda ($)

6. **Presionar Enter**

---

### Medida 10: Ventas del Mes Anterior

**Tabla**: Ventas  
**Dificultad**: ⭐⭐⭐ Avanzado

#### Paso a Paso:

1. **Crear nueva medida en tabla Ventas**

2. **Escribir la fórmula**
   ```
   -- Ventas Mes Anterior = 
   CALCULATE(
       SUM(Ventas[total]),
       DATEADD(Ventas[fecha], -1, MONTH)
   )
   ```

3. **Explicación**:
   - `DATEADD()` desplaza fechas
   - `-1` significa "restar 1"
   - `MONTH` es la unidad (mes)

4. **Formato**: Moneda ($)

5. **Presionar Enter**

---

### Medida 11: Ventas YTD (Año a la Fecha)

**Tabla**: Ventas  
**Dificultad**: ⭐⭐⭐ Avanzado

#### Paso a Paso:

1. **Crear nueva medida en tabla Ventas**

2. **Escribir la fórmula**
   ```
   -- Ventas YTD = 
   CALCULATE(
       SUM(Ventas[total]),
       DATESYTD(Ventas[fecha])
   )
   ```

3. **Explicación**:
   - `DATESYTD()` incluye todas las fechas desde el 1 de enero hasta hoy
   - Útil para análisis acumulativo

4. **Formato**: Moneda ($)

5. **Presionar Enter**

---

### Medida 12: Variación Interanual (YoY)

**Tabla**: Ventas  
**Dificultad**: ⭐⭐⭐⭐ Muy Avanzado

#### Paso a Paso:

1. **Crear nueva medida en tabla Ventas**

2. **Escribir la fórmula completa (línea por línea)**
   
   Primera línea:
   ```
   -- Variación YoY = 
   ```
   
   Segunda línea (crear variable):
   ```
   VAR VentasActuales = SUM(Ventas[total])
   ```
   
   Tercera línea (otra variable):
   ```
   VAR VentasAñoAnterior = 
   ```
   
   Continuar en la misma línea o siguiente:
   ```
       CALCULATE(
           SUM(Ventas[total]),
           SAMEPERIODLASTYEAR(Ventas[fecha])
       )
   ```
   
   Última línea (RETURN):
   ```
   RETURN
       IF(
           VentasAñoAnterior > 0,
           (VentasActuales - VentasAñoAnterior) / VentasAñoAnterior,
           BLANK()
       )
   ```

3. **Fórmula completa** (para copiar y pegar):
   ```
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

4. **Explicación**:
   - `VAR` define una variable
   - `RETURN` devuelve el resultado
   - `IF()` verifica si el año anterior > 0
   - Si es verdadero, calcula el porcentaje
   - Si es falso, devuelve BLANK() (vacío)

5. **Formato**: Porcentaje (%)

6. **Presionar Enter**

---

### Medida 13: Crecimiento Mes a Mes (MoM)

**Tabla**: Ventas  
**Dificultad**: ⭐⭐⭐⭐ Muy Avanzado

#### Paso a Paso:

1. **Crear nueva medida en tabla Ventas**

2. **Escribir la fórmula**:
   ```
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

3. **Importante**:
   - Usa `[-- Total de Ventas]` que creamos antes
   - `DIVIDE()` es mejor que `/` porque maneja división por cero

4. **Formato**: Porcentaje (%)

5. **Presionar Enter**

---

### Medida 14: Estado de Inventario

**Tabla**: Productos  
**Dificultad**: ⭐⭐⭐ Avanzado

#### Paso a Paso:

1. **Crear nueva medida en tabla Productos**

2. **Escribir la fórmula**:
   ```
   -- Estado Inventario = 
   SWITCH(
       TRUE(),
       [-- Stock Total] < 100, "Stock Bajo",
       [-- Stock Total] < 300, "Stock Medio",
       "Stock Alto"
   )
   ```

3. **Explicación**:
   - `SWITCH(TRUE(), ...)` evalúa condiciones en orden
   - Primera condición verdadera devuelve su valor
   - Último valor es el "default"

4. **Formato**: Texto (sin formato especial)

5. **Presionar Enter**

---

## Crear KPIs - Paso a Paso

### KPI 1: Rotación de Inventario

#### Paso 1: Crear la Medida de Valor Actual

1. **Crear nueva medida en tabla Productos**

2. **Escribir**:
   ```
   -- Rotación de Inventario = 
   DIVIDE(
       [-- Total de Productos Vendidos],
       [-- Stock Total],
       0
   )
   ```

3. **Formato**: Número decimal (2 decimales)

4. **Presionar Enter**

---

#### Paso 2: Crear la Medida de Objetivo

1. **Crear nueva medida en tabla Productos**

2. **Escribir**:
   ```
   -- Objetivo Rotación = 2.5
   ```

3. **Formato**: Número decimal

4. **Presionar Enter**

---

#### Paso 3: Crear la Medida de Estado

1. **Crear nueva medida en tabla Productos**

2. **Escribir**:
   ```
   -- Estado Rotación = 
   IF(
       [-- Rotación de Inventario] >= [-- Objetivo Rotación],
       "✅ Objetivo Alcanzado",
       "⚠️ Por Debajo del Objetivo"
   )
   ```

3. **Formato**: Texto

4. **Presionar Enter**

---

#### Paso 4: Agregar Visual KPI

1. **En una página del informe**, click en el ícono **KPI** (o busca "KPI" en visualizaciones)

2. **Arrastrar campos**:
   - **Valor**: Arrastra `-- Rotación de Inventario`
   - **Objetivo**: Arrastra `-- Objetivo Rotación`
   - **Tendencias**: (Opcional) Arrastra `-- Rotación de Inventario` y una columna de fecha

3. **El KPI aparecerá visualmente**

---

### KPI 2: Margen de Utilidad

#### Paso 1: Crear Medida de Valor Actual

1. **Crear nueva medida en tabla Ventas**:

```
-- Margen Utilidad = 
VAR Ingresos = [-- Ingresos Totales]
VAR Costos = SUMX(
    Detalle_Ventas,
    RELATED(Productos[precio_costo]) * Detalle_Ventas[cantidad]
)
RETURN
    DIVIDE(Ingresos - Costos, Ingresos, 0)
```

**NOTA**: Si no tienes `precio_costo`, ajusta la fórmula o usa un valor estimado.

**Alternativa simplificada**:
```
-- Margen Utilidad = 
VAR Ingresos = [-- Ingresos Totales]
VAR CostosEstimados = Ingresos * 0.7  -- Asumiendo 30% de margen
RETURN
    DIVIDE(Ingresos - CostosEstimados, Ingresos, 0)
```

2. **Formato**: Porcentaje (%)

3. **Presionar Enter**

---

#### Paso 2: Crear Objetivo

1. **Crear medida**:
```
-- Objetivo Margen = 0.30
```

2. **Formato**: Porcentaje (30%)

---

#### Paso 3: Crear Estado

1. **Crear medida**:
```
-- Estado Margen = 
SWITCH(
    TRUE(),
    [-- Margen Utilidad] >= [-- Objetivo Margen], "✅ Excelente",
    [-- Margen Utilidad] >= [-- Objetivo Margen] * 0.8, "⚠️ Aceptable",
    "❌ Bajo"
)
```

---

### KPI 3: Nivel de Servicio

#### Paso 1: Crear Medida de Valor Actual

1. **Crear nueva medida** (puede ir en tabla Ventas):

```
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

**Versión simplificada** (si hay problemas con relaciones):
```
-- Nivel Servicio = 
DIVIDE(
    [-- Total de Ventas],
    [-- Total de Ventas] + 10,  -- Ajustar según lógica del negocio
    0
)
```

2. **Formato**: Porcentaje (%)

3. **Presionar Enter**

---

#### Paso 2 y 3: Objetivo y Estado

Similar a los KPIs anteriores.

---

## Verificar y Probar Medidas

### Cómo Verificar que una Medida Funciona

1. **Crear una tabla simple**:
   - En una página del informe
   - Arrastra la medida a la tabla
   - Debe mostrar un valor (no error)

2. **Verificar en diferentes contextos**:
   - Arrastra la medida a un gráfico de barras
   - Agrega una categoría (ej: Productos[categoria])
   - Verifica que los valores cambien según el contexto

3. **Usar el panel de filtros**:
   - Agrega un filtro de fecha
   - Verifica que la medida responde al filtro

---

## Troubleshooting

### Error: "No se puede encontrar el nombre 'Tabla[Columna]'"

**Causa**: Nombre de tabla o columna incorrecto

**Solución**:
1. Ve a la vista de Modelo
2. Verifica el nombre exacto de la tabla
3. Verifica el nombre exacto de la columna
4. Los nombres son case-sensitive (mayúsculas/minúsculas importan)

---

### Error: "Una expresión que no es un escalar se utilizó en un contexto..."

**Causa**: Estás usando una tabla donde se espera un valor

**Solución**:
- Usa funciones de agregación: SUM(), COUNT(), AVERAGE(), etc.
- Ejemplo incorrecto: `Medida = Productos[stock]`
- Ejemplo correcto: `Medida = SUM(Productos[stock])`

---

### Error: "Se detectaron errores en la fórmula"

**Causa**: Error de sintaxis

**Solución**:
1. Verifica paréntesis cerrados: `()` `[]`
2. Verifica comas entre argumentos
3. Verifica comillas en texto: `"Texto"`
4. Usa el botón de verificación ✓ para ver el error específico

---

### La medida muestra "Error" en lugar de un número

**Causa**: Error en tiempo de ejecución

**Solución**:
1. Click derecho en la medida → "Editar medida"
2. Revisa la fórmula línea por línea
3. Verifica que las columnas existan
4. Verifica que las relaciones entre tablas estén correctas

---

### La medida devuelve valores incorrectos

**Causa**: Problema con el contexto de filtro

**Solución**:
1. Revisa si necesitas usar `CALCULATE()`
2. Verifica que las relaciones estén configuradas correctamente
3. Prueba la medida en diferentes visualizaciones

---

## Checklist Final

Antes de considerar completas las medidas, verifica:

- [ ] Todas las medidas se crean sin errores
- [ ] Cada medida muestra valores (no errores) en una tabla
- [ ] Las medidas responden a filtros
- [ ] Los formatos de número son correctos (moneda, porcentaje, etc.)
- [ ] Los 3 KPIs tienen valor, objetivo y estado
- [ ] Al menos 6 medidas con diferentes tipos de función DAX
- [ ] Se utilizan funciones de al menos 6 grupos diferentes

---

## Resumen de Medidas a Crear

### Medidas Básicas (Fáciles)
1. ✅ -- Total de Productos Vendidos
2. ✅ -- Valor Total Inventario
3. ✅ -- Stock Total
4. ✅ -- Promedio de Stock por Categoría
5. ✅ -- Total Productos Únicos

### Medidas Intermedias
6. ✅ -- Total de Ventas
7. ✅ -- Ingresos Totales
8. ✅ -- Productos Stock Bajo

### Medidas Avanzadas
9. ✅ -- Ventas Mes Actual
10. ✅ -- Ventas Mes Anterior
11. ✅ -- Ventas YTD
12. ✅ -- Variación YoY
13. ✅ -- Crecimiento MoM
14. ✅ -- Estado Inventario

### KPIs
15. ✅ -- Rotación de Inventario + Objetivo + Estado
16. ✅ -- Margen Utilidad + Objetivo + Estado
17. ✅ -- Nivel Servicio + Objetivo + Estado

**Total**: 17+ medidas

---

## Próximos Pasos

Después de crear todas las medidas:

1. **Crear visualizaciones** en el informe
2. **Crear jerarquías** (ver documentación principal)
3. **Configurar KPIs** visuales
4. **Probar el dashboard** completo

---

**¡Éxito con tu proyecto!** 🚀

Si tienes dudas específicas, consulta `Documentacion_Sprint4.md` o `Notebook_DAX_Ejemplos.md`

