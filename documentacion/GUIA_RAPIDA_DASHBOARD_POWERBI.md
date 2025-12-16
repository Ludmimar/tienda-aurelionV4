# 🚀 GUÍA RÁPIDA: Crear Dashboard Power BI - Tienda Aurelion (Sprint 3)

## ⚡ Tiempo estimado: 20-30 minutos

---

## ✅ CHECKLIST PREVIO

Antes de comenzar, verificá que tengas:

- [ ] Power BI Desktop instalado ([Descargar aquí](https://powerbi.microsoft.com/desktop/))
- [ ] Los 4 archivos CSV en la carpeta `Sprint-2/datos/`:
  - `productos.csv` ✓
  - `clientes.csv` ✓
  - `ventas.csv` ✓
  - `detalle_ventas.csv` ✓
- [ ] Los archivos en `Sprint-2/Power BI/`:
  - `query_productos.m` ✓
  - `query_clientes.m` ✓
  - `query_ventas.m` ✓
  - `query_detalle_ventas.m` ✓
  - `measures.dax` ✓
  - `theme.json` ✓

---

## 📋 PASO A PASO SIMPLIFICADO

### PASO 1: Abrir Power BI Desktop

1. Abre **Power BI Desktop**
2. Cierra cualquier ventana de bienvenida
3. Deberías ver una pantalla en blanco

---

### PASO 2: Cargar las 4 Tablas (5 minutos)

#### 2.1 Cargar Tabla PRODUCTOS

1. Click en **Home** → **Get Data** → **Blank Query**
2. En la ventana Power Query Editor, click en **Advanced Editor** (arriba a la izquierda)
3. **Borra todo** el contenido del editor
4. Abre el archivo `Sprint-2/Power BI/query_productos.m` con un editor de texto
5. **Copia todo** el contenido
6. **Pega** en el Advanced Editor de Power BI
7. Click en **Done**
8. En el panel derecho (Query Settings), cambia el nombre de "Query1" a **`Productos`**
9. Verifica que se carguen los datos correctamente (deberías ver 80 filas)

#### 2.2 Cargar Tabla CLIENTES

1. Click en **Home** → **New Source** → **Blank Query**
2. Click en **Advanced Editor**
3. Borra todo y pega el contenido de `query_clientes.m`
4. Click en **Done**
5. Renombra la query a **`Clientes`**
6. Verifica 50 filas

#### 2.3 Cargar Tabla VENTAS

1. Click en **Home** → **New Source** → **Blank Query**
2. Click en **Advanced Editor**
3. Borra todo y pega el contenido de `query_ventas.m`
4. Click en **Done**
5. Renombra la query a **`Ventas`**
6. Verifica 100 filas

#### 2.4 Cargar Tabla DETALLE_VENTAS

1. Click en **Home** → **New Source** → **Blank Query**
2. Click en **Advanced Editor**
3. Borra todo y pega el contenido de `query_detalle_ventas.m`
4. Click en **Done**
5. Renombra la query a **`Detalle_Ventas`**
6. Verifica 273 filas

#### 2.5 Cerrar Power Query

1. Click en **Close & Apply** (arriba a la izquierda)
2. Espera a que se carguen los datos (puede tardar unos segundos)

---

### PASO 3: Crear Relaciones entre Tablas (2 minutos)

1. Click en el icono **Model View** (tercer icono en el panel izquierdo, parece un diagrama)
2. Deberías ver las 4 tablas
3. **Power BI puede crear las relaciones automáticamente**. Si ya están creadas (líneas conectando las tablas), verifica:
   - `Clientes[id]` → `Ventas[id_cliente]` (1 a muchos)
   - `Ventas[id_venta]` → `Detalle_Ventas[id_venta]` (1 a muchos)
   - `Productos[id]` → `Detalle_Ventas[id_producto]` (1 a muchos)

4. **Si NO están creadas**, creálas manualmente:
   - Arrastra `Clientes[id]` hasta `Ventas[id_cliente]` → En el diálogo, asegúrate que Cardinality sea "One to many (*)" → OK
   - Arrastra `Ventas[id_venta]` hasta `Detalle_Ventas[id_venta]` → One to many (*) → OK
   - Arrastra `Productos[id]` hasta `Detalle_Ventas[id_producto]` → One to many (*) → OK

5. Verifica que las líneas entre tablas estén **continuas** (no punteadas) = relaciones activas

6. Click en **Report View** (primer icono en el panel izquierdo)

---

### PASO 4: Importar Tema Visual (1 minuto)

1. Click en **View** (en la barra superior)
2. Click en **Themes** → **Browse for themes**
3. Navega hasta `Sprint-2/Power BI/theme.json`
4. Selecciónalo y click en **Open**
5. El tema se aplicará automáticamente (colores dorados/medievales)

---

### PASO 5: Crear Medidas DAX (3 minutos)

1. Click en **Modeling** (en la barra superior)
2. Click en **New Measure**
3. Abre el archivo `Sprint-2/Power BI/measures.dax` con un editor de texto
4. **Copia la primera medida** (desde `-- Valor Total Inventario` hasta el final de esa medida)

```dax
Valor Total Inventario = 
SUMX(
    Productos,
    Productos[precio] * Productos[stock]
)
```

5. **Pega** en la barra de fórmulas de Power BI (donde dice "Measure =")
6. Presiona **Enter**
7. **Repite para TODAS las medidas** del archivo `measures.dax`

**TIP:** Puedes copiar y pegar múltiples medidas a la vez si Power BI lo permite, o una por una.

**Medidas esenciales que DEBES crear:**
- Valor Total Inventario
- Precio Promedio
- Stock Total
- Productos Stock Bajo
- % Stock Saludable
- Total Ventas
- Ingresos Totales
- Promedio Venta
- Ticket Promedio
- Total Clientes

---

### PASO 6: Crear PÁGINA 1 - Overview (8 minutos)

#### 6.1 Renombrar la página

1. Click derecho en "Page 1" (abajo) → **Rename**
2. Escribe **`Overview`**

#### 6.2 Agregar Tarjetas KPI (5 tarjetas)

**Tarjeta 1: Total de Productos**
1. Click en **Card** visual (icono de tarjeta en el panel Visualizations)
2. Arrastra `Productos[id]` al área **Fields**
3. Power BI automáticamente hará un COUNT
4. Colócala arriba a la izquierda
5. En **Format visual** (icono de rodillo), aumenta el tamaño de fuente del valor (36pt)
6. Agrega un título: **"Total Productos"**

**Tarjeta 2: Valor Total Inventario**
1. Agrega otra **Card**
2. Arrastra la medida `[Valor Total Inventario]` al área **Fields**
3. Formatea como moneda: selecciona la medida → Format → Currency → $ English (United States)
4. Título: **"Valor Total Inventario"**

**Tarjeta 3: Stock Total**
1. Agrega otra **Card**
2. Arrastra la medida `[Stock Total]`
3. Título: **"Stock Total"**

**Tarjeta 4: Total Ventas**
1. Agrega otra **Card**
2. Arrastra la medida `[Total Ventas]`
3. Título: **"Total Ventas"**

**Tarjeta 5: Ingresos Totales**
1. Agrega otra **Card**
2. Arrastra la medida `[Ingresos Totales]`
3. Formatea como moneda
4. Título: **"Ingresos Totales"**

**Organiza las 5 tarjetas en una fila horizontal en la parte superior del dashboard**

#### 6.3 Gráfico de Barras: Productos por Categoría

1. Click en **Stacked bar chart** (barras horizontales)
2. **Y-axis:** Arrastra `Productos[categoria]`
3. **X-axis:** Arrastra `Productos[id]` (automáticamente hará COUNT)
4. Título: **"Productos por Categoría"**
5. Colócalo en la zona media-izquierda

#### 6.4 Gráfico de Columnas: Top 10 Productos Más Valiosos

1. Click en **Clustered column chart** (columnas)
2. **X-axis:** Arrastra `Productos[nombre]`
3. **Y-axis:** Arrastra `Productos[valor_inventario]`
4. En **Filters** (panel derecho), selecciona `nombre`
5. Cambia de "All" a **"Top N"**
6. Configura: Show items **"Top 10"** by value `valor_inventario`
7. Título: **"Top 10 Productos Más Valiosos"**
8. Colócalo en la zona media-derecha

#### 6.5 Gráfico de Anillos: Distribución de Stock por Categoría

1. Click en **Donut chart**
2. **Legend:** Arrastra `Productos[categoria]`
3. **Values:** Arrastra `Productos[stock]` (automáticamente hará SUM)
4. Título: **"  "**
5. Colócalo abajo a la izquierda

#### 6.6 Tabla: Productos con Stock Bajo

1. Click en **Table**
2. Arrastra las columnas:
   - `Productos[nombre]`
   - `Productos[categoria]`
   - `Productos[stock]`
   - `Productos[proveedor]`
3. En **Filters on this visual**, agrega `Productos[stock]`
4. Configura: Show items when the value **"is less than or equal to"** **20**
5. Título: **"⚠️ Productos con Stock Bajo"**
6. **Formato condicional:** Selecciona la columna `stock` → Click derecho → Conditional formatting → Background color
   - Si valor es <= 10: Rojo
   - Si valor es <= 20: Amarillo
7. Colócalo abajo a la derecha

---

### PASO 7: Crear PÁGINA 2 - Ventas y Clientes (7 minutos)

#### 7.1 Crear nueva página

1. Click en el **+** al lado de "Overview" (abajo)
2. Renombra la página a **`Ventas y Clientes`**

#### 7.2 Tarjetas KPI de Ventas (fila superior)

Crea 4 tarjetas:
1. **Ticket Promedio** → medida `[Ticket Promedio]`
2. **Total Productos Vendidos** → medida `[Total Productos Vendidos]`
3. **Total Clientes** → medida `[Total Clientes]`
4. **Promedio Venta** → medida `[Promedio Venta]`

#### 7.3 Gráfico de Línea: Evolución de Ventas

1. Click en **Line chart**
2. **X-axis:** Arrastra `Ventas[fecha]`
3. **Y-axis:** Arrastra `[Ingresos Totales]` (medida)
4. Título: **"Evolución de Ingresos por Fecha"**
5. Habilita marcadores en las líneas (Format visual → Lines → Markers → On)
6. Colócalo en la zona media-superior

#### 7.4 Gráfico de Barras: Top 5 Productos Más Vendidos

1. Click en **Clustered bar chart**
2. **Y-axis:** Arrastra `Productos[nombre]`
3. **X-axis:** Arrastra `Detalle_Ventas[cantidad]` (automáticamente hará SUM)
4. En **Filters**, configura Top N = **Top 5** by `cantidad`
5. Título: **"Top 5 Productos Más Vendidos"**
6. Colócalo en la zona media-izquierda

#### 7.5 Gráfico de Barras: Clientes por Ciudad

1. Click en **Clustered column chart**
2. **X-axis:** Arrastra `Clientes[ciudad]`
3. **Y-axis:** Arrastra `Clientes[id]` (automáticamente hará COUNT)
4. Título: **"Clientes por Ciudad"**
5. Colócalo en la zona media-derecha

#### 7.6 Tabla de Ventas

1. Click en **Table**
2. Arrastra:
   - `Ventas[id_venta]`
   - `Ventas[fecha]`
   - `Ventas[total]`
   - `Clientes[nombre]`
   - `Clientes[ciudad]`
3. Ordena por `fecha` descendente
4. Título: **"Detalle de Ventas"**
5. Colócalo abajo a la izquierda

#### 7.7 Slicers (Filtros)

1. Click en **Slicer**
2. Arrastra `Ventas[fecha]`
3. Cambia el estilo a **Between** (rango de fechas)
4. Colócalo en la esquina superior derecha

---

### PASO 8: (OPCIONAL) Páginas Adicionales

Si tenés tiempo, podés crear:

**PÁGINA 3: Análisis de Productos**
- Top 10 productos con más stock
- Scatter plot: Precio vs Stock
- Slicers por categoría y rango de precio

**PÁGINA 4: Proveedores**
- Gráfico de barras apiladas: Proveedores y categorías
- Tabla de proveedores con valor de inventario

---

### PASO 9: Formateo Final (3 minutos)

1. **Alinea todos los visuales** usando las guías de alineación
2. **Verifica los títulos** de todos los gráficos
3. **Agrega un título principal** en cada página:
   - Inserta un **Text box** (Insert → Text box)
   - Escribe: **"⚔️ TIENDA AURELION - DASHBOARD"**
   - Aumenta el tamaño de fuente (28pt)
   - Centra el texto

4. **Ajusta los colores** si es necesario (el tema ya debería estar aplicado)

---

### PASO 10: Guardar y Exportar (2 minutos)

#### Guardar como .pbix

1. **File** → **Save**
2. Nombre del archivo: **`Tienda_Aurelion_Dashboard_Sprint2.pbix`**
3. Guárdalo en la carpeta **`Sprint-2/`**

#### Exportar como .pbit (Plantilla)

1. **File** → **Export** → **Power BI template**
2. Nombre: **`Tienda_Aurelion_Template_Sprint2.pbit`**
3. Agrega una descripción: "Dashboard de gestión de inventario, ventas y clientes - Tienda Aurelion Sprint 3"
4. Click en **OK**

#### Exportar capturas de pantalla

1. Toma capturas de pantalla de cada página del dashboard:
   - Overview
   - Ventas y Clientes
2. Guárdalas en `Sprint-2/capturas/` con nombres descriptivos:
   - `dashboard_overview.png`
   - `dashboard_ventas_clientes.png`

---

## ✅ CHECKLIST FINAL DE VERIFICACIÓN

Antes de dar por terminado, verifica que tu dashboard tenga:

### Datos y Relaciones
- [ ] 4 tablas cargadas (Productos, Clientes, Ventas, Detalle_Ventas)
- [ ] 3 relaciones activas entre tablas
- [ ] Todas las medidas DAX creadas (mínimo 10 medidas)

### Página 1 - Overview
- [ ] 5 tarjetas KPI en la parte superior
- [ ] Gráfico de barras: Productos por categoría
- [ ] Gráfico de columnas: Top 10 productos valiosos
- [ ] Gráfico de anillos: Distribución de stock
- [ ] Tabla: Productos con stock bajo (con formato condicional)

### Página 2 - Ventas y Clientes
- [ ] 4 tarjetas KPI de ventas/clientes
- [ ] Gráfico de línea: Evolución de ventas
- [ ] Gráfico: Top 5 productos más vendidos
- [ ] Gráfico: Clientes por ciudad
- [ ] Tabla de ventas detallada
- [ ] Slicer de fechas

### Diseño
- [ ] Tema visual aplicado (colores dorados/medievales)
- [ ] Títulos en todos los visuales
- [ ] Elementos alineados correctamente
- [ ] Título principal en cada página

### Archivos
- [ ] Archivo .pbix guardado
- [ ] Archivo .pbit exportado (opcional)
- [ ] Capturas de pantalla guardadas

---

## 🎯 RESULTADO ESPERADO

Al finalizar, deberías tener:

1. **Un dashboard interactivo** con 2 páginas principales:
   - **Overview:** Análisis general de inventario
   - **Ventas y Clientes:** Análisis de ventas y clientes

2. **Análisis visual completo** con:
   - KPIs principales (productos, inventario, ventas, clientes)
   - Distribución por categorías
   - Top productos (más valiosos y más vendidos)
   - Alertas de stock bajo
   - Evolución temporal de ventas
   - Distribución geográfica de clientes

3. **Interactividad:** Todos los gráficos están conectados y se filtran entre sí

---

## 🆘 SOLUCIÓN DE PROBLEMAS COMUNES

### "No se encuentran los archivos CSV"

**Solución:** Los queries M buscan los archivos en `datos/productos.csv` (ruta relativa). 

**Opción 1:** Abre Power BI Desktop desde la carpeta `Sprint-2/` para que la ruta relativa funcione.

**Opción 2:** Modifica los queries M para usar rutas absolutas:
```m
File.Contents("D:/IBM/IBM-Inteligencia-Artificial/Sprint-2/datos/productos.csv")
```

### "Las relaciones no funcionan"

**Solución:** 
1. Verifica en Model View que las relaciones estén activas (líneas continuas)
2. Verifica que los campos relacionados tengan el mismo tipo de dato (ambos Int64)
3. Verifica que no haya valores nulos en las claves foráneas

### "Las medidas DAX dan error"

**Solución:** 
1. Verifica que los nombres de las tablas sean exactos: `Productos`, `Ventas`, `Clientes`, `Detalle_Ventas`
2. Verifica que los nombres de columnas coincidan con los del query M
3. Si cambias nombres, actualiza las medidas DAX

### "El tema no se aplica correctamente"

**Solución:** 
1. Asegúrate de haber seleccionado el archivo `theme.json` correcto
2. Los colores deberían cambiar automáticamente
3. Si no se aplica, reinicia Power BI Desktop e intenta de nuevo

---

## 📞 CONTACTO Y SOPORTE

**Autor:** Martos Ludmila  
**DNI:** 34811650  
**Institución:** IBM - Sprint 3  
**Año:** 2025

---

## 📚 RECURSOS ADICIONALES

- **Documentación completa:** `Sprint-2/documentacion/GUIA_POWER_BI.md`
- **Instrucciones de layout:** `Sprint-2/Power BI/layout_instructions.md`
- **Medidas DAX:** `Sprint-2/Power BI/measures.dax`
- **Queries M:** Carpeta `Sprint-2/Power BI/`

---

**¡Éxitos con tu dashboard! ⚔️📊**



