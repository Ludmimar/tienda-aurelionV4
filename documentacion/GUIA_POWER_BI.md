# 📊 GUÍA PARA DASHBOARD EN POWER BI - TIENDA AURELION

## 🎯 Objetivo del Dashboard

Crear un dashboard interactivo en Power BI que visualice los datos del inventario de la Tienda Aurelion, permitiendo análisis visual y toma de decisiones basada en datos.

---

## 📋 Índice
1. [Preparación de Datos](#preparación-de-datos)
2. [Importación a Power BI](#importación-a-power-bi)
3. [Visualizaciones Recomendadas](#visualizaciones-recomendadas)
4. [KPIs y Métricas](#kpis-y-métricas)
5. [Diseño del Dashboard](#diseño-del-dashboard)
6. [Interactividad y Filtros](#interactividad-y-filtros)
7. [Tips y Mejores Prácticas](#tips-y-mejores-prácticas)

---

## 📁 Preparación de Datos

### Paso 1: Verificar los Archivos CSV

Los archivos CSV ya están listos para importar a Power BI. Asegúrate de que existan los 4 archivos:

- `productos.csv` - Base de datos de productos
- `clientes.csv` - Base de datos de clientes  
- `ventas.csv` - Base de datos de ventas
- `detalle_ventas.csv` - Detalles de ventas

**Estructura de productos.csv:**
```csv
id,nombre,categoria,precio,stock,descripcion,proveedor
1,Espada Celestial,Armas,1500,25,Espada forjada con metal estelar,Forja Celestial
2,Armadura de Dragón,Armaduras,3000,15,Armadura resistente hecha de escamas de dragón,Herrería Dragón
...
```

✅ **Campos disponibles:**
- `id`: Identificador único (numérico)
- `nombre`: Nombre del producto (texto)
- `categoria`: Categoría del producto (texto)
- `precio`: Precio en monedas (numérico)
- `stock`: Cantidad disponible (numérico)
- `descripcion`: Descripción del producto (texto)
- `proveedor`: Nombre del proveedor (texto)

### Paso 2: Calcular Columnas Adicionales (Opcional)

Para análisis más profundo, puedes preparar columnas adicionales en Excel antes de importar:

| Columna Adicional | Fórmula/Cálculo | Utilidad |
|-------------------|-----------------|----------|
| `valor_inventario` | `precio * stock` | Valor total en inventario de cada producto |
| `estado_stock` | Si stock <= 20: "Bajo", Si stock <= 50: "Medio", Sino: "Alto" | Clasificación de nivel de stock |
| `rango_precio` | Si precio < 500: "Económico", Si precio < 2000: "Medio", Sino: "Premium" | Segmentación por precio |

---

## 📥 Importación a Power BI

### Paso 1: Abrir Power BI Desktop

1. Descarga e instala [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (gratis)
2. Abre la aplicación
3. Click en "Obtener datos" o "Get Data"

### Paso 2: Importar los 4 Archivos CSV y Crear Relaciones

**Opción A: Usar Power Query (M) - RECOMENDADO**

1. Home → Get Data → Blank Query
2. Para cada tabla, usa los archivos de query en `Power BI/`:
   - Para Productos: Advanced Editor → pegar `query_productos.m`
   - Para Clientes: Advanced Editor → pegar `query_clientes.m`
   - Para Ventas: Advanced Editor → pegar `query_ventas.m`
   - Para Detalle_Ventas: Advanced Editor → pegar `query_detalle_ventas.m`
3. Renombra cada query con el nombre de la tabla
4. Close & Apply

**Opción B: Importar Manualmente**

1. Selecciona **"Texto/CSV"**
2. Navega hasta `datos/productos.csv` y click en **"Cargar"**
3. Repite para `clientes.csv`, `ventas.csv`, `detalle_ventas.csv`
4. En View → Model View, crea las relaciones:
   - `Clientes[id]` → `Ventas[id_cliente]` (1 a muchos)
   - `Ventas[id_venta]` → `Detalle_Ventas[id_venta]` (1 a muchos)
   - `Productos[id]` → `Detalle_Ventas[id_producto]` (1 a muchos)

### Paso 3: Verificar Tipos de Datos y Relaciones

En la vista de **"Modelo"** o **"Datos"**, asegúrate de que:

**Tabla Productos:**
- `id` sea tipo **Número entero**
- `precio` sea tipo **Número entero**
- `stock` sea tipo **Número entero**
- `nombre`, `categoria`, `descripcion`, `proveedor` sean tipo **Texto**

**Tabla Clientes:**
- `id` sea tipo **Número entero**
- `fecha_registro` sea tipo **Fecha**
- `nombre`, `email`, `telefono`, `ciudad` sean tipo **Texto**

**Tabla Ventas:**
- `id_venta`, `id_cliente` sean tipo **Número entero**
- `fecha` sea tipo **Fecha**
- `total` sea tipo **Número entero**

**Tabla Detalle_Ventas:**
- `id_detalle`, `id_venta`, `id_producto`, `cantidad`, `precio_unitario`, `subtotal` sean tipo **Número entero**

**Verificar Relaciones:**
- Las 3 relaciones entre tablas deben estar activas (línea continua)
- Verifica que las relaciones sean 1 a muchos (uno a varios)

---

## 📊 Visualizaciones Recomendadas

### 1. Tarjetas de KPIs (Cards)

**Ubicación:** Parte superior del dashboard

**Métricas a mostrar:**
- **Total de Productos**: `COUNT(id)` o `COUNTROWS(Productos)`
- **Valor Total Inventario**: `[Valor Total Inventario]` (medida DAX)
- **Stock Total**: `[Stock Total]` (medida DAX)
- **Categorías Únicas**: `DISTINCTCOUNT(categoria)` o `DISTINCTCOUNT(Productos[categoria])`
- **Productos con Stock Bajo**: `[Productos Stock Bajo]` (medida DAX)
- **Total Ventas**: `[Total Ventas]` ⭐ NUEVO (medida DAX)
- **Ingresos Totales**: `[Ingresos Totales]` ⭐ NUEVO (medida DAX)

**Cómo crear:**
1. Selecciona visual **"Tarjeta"** en el panel de visualizaciones
2. Arrastra el campo o crea medida DAX
3. Formatea con formato de número apropiado

**Ejemplo de Medida DAX:**
```dax
Valor Total Inventario = SUMX(Productos, Productos[precio] * Productos[stock])
```

---

### 2. Gráfico de Barras: Productos por Categoría

**Tipo:** Gráfico de barras horizontales

**Configuración:**
- **Eje Y:** `categoria`
- **Eje X:** `COUNT(id)` o `SUM(stock)`
- **Ordenar por:** Cantidad (descendente)
- **Colores:** Usar paleta temática medieval (dorado, rojo, azul oscuro)

**Insights que muestra:**
- ¿Qué categorías tienen más productos?
- Distribución del inventario

---

### 3. Gráfico de Columnas: Top 10 Productos Más Valiosos

**Tipo:** Gráfico de columnas

**Configuración:**
- **Eje X:** `nombre`
- **Eje Y:** `valor_inventario` (precio * stock)
- **Filtro:** Top 10 por valor
- **Color:** Gradiente según valor

**Medida DAX:**
```dax
Valor por Producto = Productos[precio] * Productos[stock]
```

**Insights que muestra:**
- ¿Qué productos representan más valor?
- ¿Dónde está concentrado el capital del inventario?

---

### 4. Gráfico de Anillos (Donut): Distribución de Stock por Categoría

**Tipo:** Gráfico de anillos/donut

**Configuración:**
- **Leyenda:** `categoria`
- **Valores:** `SUM(stock)`
- **Colores:** Personalizar por categoría

**Insights que muestra:**
- ¿Qué porcentaje del stock representa cada categoría?
- Distribución de unidades en inventario

---

### 5. Tabla: Productos con Stock Bajo

**Tipo:** Tabla o Matriz

**Configuración:**
- **Columnas:** `nombre`, `categoria`, `stock`, `proveedor`
- **Filtro:** `stock <= 20`
- **Formato condicional:** 
  - Stock <= 10: Rojo
  - Stock <= 20: Amarillo
- **Ordenar por:** Stock ascendente

**Insights que muestra:**
- Alertas de reabastecimiento
- Productos críticos a reabastecer

---

### 6. Gráfico de Dispersión: Precio vs Stock

**Tipo:** Gráfico de dispersión (scatter plot)

**Configuración:**
- **Eje X:** `precio`
- **Eje Y:** `stock`
- **Detalles:** `nombre`
- **Tamaño de burbuja:** `valor_inventario`
- **Categoría (color):** `categoria`

**Insights que muestra:**
- Relación entre precio y cantidad en stock
- Identificar productos caros con poco stock (alto riesgo)

---

### 7. Gráfico de Barras Apiladas: Proveedores y Categorías

**Tipo:** Gráfico de barras apiladas

**Configuración:**
- **Eje Y:** `proveedor`
- **Eje X:** `COUNT(id)`
- **Leyenda:** `categoria`

**Insights que muestra:**
- ¿Qué proveedores suministran más productos?
- Diversificación de categorías por proveedor

---

### 8. Medidor (Gauge): Indicador de Stock Saludable

**Tipo:** Medidor/Gauge

**Configuración:**
- **Valor:** `Porcentaje de productos con stock adecuado`
- **Mínimo:** 0%
- **Máximo:** 100%
- **Objetivos:**
  - 0-50%: Rojo (crítico)
  - 50-80%: Amarillo (alerta)
  - 80-100%: Verde (saludable)

**Medida DAX:**
```dax
% Stock Saludable = 
DIVIDE(
    COUNTROWS(FILTER(Productos, [stock] > 20)),
    COUNTROWS(Productos),
    0
) * 100
```

---

### 9. Mapa de Calor (Matrix): Categoría vs Rango de Precio

**Tipo:** Matriz con formato condicional

**Configuración:**
- **Filas:** `categoria`
- **Columnas:** `rango_precio` (Económico, Medio, Premium)
- **Valores:** `COUNT(id)`
- **Formato condicional:** Escala de colores

**Insights que muestra:**
- Distribución de productos por categoría y rango de precio
- Identificar gaps en el catálogo

---

### 10. Lista de Segmentación: Filtros Interactivos

**Tipo:** Segmentación de datos (Slicer)

**Filtros recomendados:**
1. **Categoría** (lista o dropdown)
2. **Proveedor** (lista o dropdown)
3. **Rango de Precio** (slider)
4. **Estado de Stock** (botones: Bajo / Medio / Alto)

---

## 🎨 Diseño del Dashboard

### Layout Sugerido

```
╔═══════════════════════════════════════════════════════════════════╗
║                    ⚔️  TIENDA AURELION - DASHBOARD               ║
║                    Sistema de Gestión de Inventario               ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌────────┐ ║
║  │Total    │  │Valor    │  │Stock    │  │Categorías│ │Stock   │ ║
║  │Productos│  │Total    │  │Total    │  │Únicas   │  │Bajo    │ ║
║  │   20    │  │ 85,000  │  │ 1,468   │  │    10   │  │  3     │ ║
║  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └────────┘ ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ┌───────────────────────────┐  ┌───────────────────────────┐   ║
║  │                           │  │                           │   ║
║  │  Productos por Categoría  │  │  Top 10 Más Valiosos      │   ║
║  │  (Barras horizontales)    │  │  (Columnas)               │   ║
║  │                           │  │                           │   ║
║  └───────────────────────────┘  └───────────────────────────┘   ║
║                                                                   ║
║  ┌───────────────────────────┐  ┌───────────────────────────┐   ║
║  │                           │  │                           │   ║
║  │  Distribución de Stock    │  │  Precio vs Stock          │   ║
║  │  (Gráfico de anillos)     │  │  (Dispersión)             │   ║
║  │                           │  │                           │   ║
║  └───────────────────────────┘  └───────────────────────────┘   ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐ ║
║  │            ⚠️  PRODUCTOS CON STOCK BAJO                     │ ║
║  │  Nombre          Categoría    Stock   Proveedor             │ ║
║  │  Gema Resurrección Consumibles   3    Joyería Arcana       │ ║
║  │  Grimorio Antiguo  Libros        8    Biblioteca Arcana    │ ║
║  │  Capa Invisibilidad Capas       10    Tejeduría Sombría    │ ║
║  └─────────────────────────────────────────────────────────────┘ ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║  FILTROS:  [Categoría ▼] [Proveedor ▼] [Precio: 0-5000]        ║
╚═══════════════════════════════════════════════════════════════════╝
```

### Paleta de Colores Temática

**Tema Medieval/Fantasía:**
- **Primario:** Dorado (#D4AF37)
- **Secundario:** Rojo oscuro (#8B0000)
- **Terciario:** Azul marino (#000080)
- **Acento:** Plata (#C0C0C0)
- **Alertas:** Amarillo (#FFD700) y Rojo (#FF0000)
- **Fondo:** Gris oscuro (#2C2C2C) o Beige (#F5F5DC)

### Fuentes Recomendadas
- **Títulos:** Cinzel o Trajan Pro (medieval)
- **Cuerpo:** Segoe UI o Calibri (legibilidad)
- **Tamaños:**
  - Título principal: 24-28pt
  - KPIs: 36-48pt
  - Subtítulos: 14-16pt
  - Texto normal: 10-12pt

---

## 📈 KPIs y Métricas Clave

### Medidas DAX Esenciales

```dax
// 1. Valor Total del Inventario
Valor Total Inventario = 
SUMX(
    Productos,
    Productos[precio] * Productos[stock]
)

// 2. Precio Promedio
Precio Promedio = AVERAGE(Productos[precio])

// 3. Stock Promedio
Stock Promedio = AVERAGE(Productos[stock])

// 4. Productos con Stock Bajo
Productos Stock Bajo = 
COUNTROWS(
    FILTER(Productos, Productos[stock] <= 20)
)

// 5. Porcentaje de Stock Saludable
% Stock Saludable = 
DIVIDE(
    COUNTROWS(FILTER(Productos, [stock] > 20)),
    COUNTROWS(Productos),
    0
) * 100

// 6. Producto Más Caro
Producto Más Caro = 
MAXX(
    Productos,
    Productos[nombre]
)

// 7. Valor Promedio por Producto
Valor Promedio por Producto = 
DIVIDE(
    [Valor Total Inventario],
    COUNTROWS(Productos),
    0
)

// 8. Categoría con Más Stock
Categoría Top Stock = 
FIRSTNONBLANK(
    TOPN(
        1,
        VALUES(Productos[categoria]),
        [Stock Total],
        DESC
    ),
    1
)

// 9. Proveedor Líder
Proveedor Líder = 
CALCULATE(
    VALUES(Productos[proveedor]),
    TOPN(
        1,
        ALL(Productos[proveedor]),
        COUNTROWS(Productos),
        DESC
    )
)

// 10. Días Estimados de Inventario (asumiendo 5 ventas/día)
Días de Inventario = 
DIVIDE(
    [Stock Total],
    5,
    0
)
```

---

## 🔄 Interactividad y Filtros

### Segmentaciones Recomendadas

1. **Categoría**
   - Tipo: Lista vertical
   - Selección: Múltiple
   - Efecto: Filtra todos los visuales

2. **Proveedor**
   - Tipo: Dropdown
   - Selección: Única o múltiple
   - Efecto: Filtra todos los visuales

3. **Rango de Precio**
   - Tipo: Slider/Control deslizante
   - Rango: 0 a MAX(precio)
   - Efecto: Filtra productos por precio

4. **Estado de Stock**
   - Tipo: Botones
   - Opciones: Bajo (≤20) | Medio (21-50) | Alto (>50) | Todos
   - Efecto: Alerta visual de stock

### Drill-Through

Configura drill-through para análisis detallado:

1. **Desde:** Gráfico de barras de categorías
   **Hacia:** Página de detalle de categoría con:
   - Lista de todos los productos
   - Gráficos específicos de esa categoría
   - Estadísticas detalladas

2. **Desde:** Top 10 productos
   **Hacia:** Ficha de producto individual con:
   - Información completa
   - Histórico (si hay datos temporales)
   - Comparación con promedio de categoría

### Tooltips Personalizados

Crea tooltips que muestren al pasar el mouse:
- Nombre completo del producto
- Descripción
- Valor total en inventario
- Días estimados de stock
- Proveedor y categoría

---

## 💡 Tips y Mejores Prácticas

### 1. Diseño Visual

✅ **Hacer:**
- Usa espacio en blanco para separar secciones
- Mantén colores consistentes
- Alinea elementos cuidadosamente
- Usa íconos para mejorar comprensión
- Mantén jerarquía visual clara

❌ **Evitar:**
- Sobrecargar con demasiados gráficos
- Mezclar demasiados tipos de visualización
- Colores brillantes que cansen la vista
- Texto demasiado pequeño
- Gráficos 3D (distorsionan datos)

### 2. Performance

✅ **Optimizar:**
- Usa medidas DAX en lugar de columnas calculadas cuando sea posible
- Limita el uso de filtros complejos
- Evita relaciones bidireccionales innecesarias
- Comprime imágenes de fondo

### 3. Storytelling con Datos

📊 **Estructura narrativa:**
1. **Overview (Arriba):** KPIs principales - "¿Cómo estamos?"
2. **Análisis (Medio):** Gráficos comparativos - "¿Por qué estamos así?"
3. **Acción (Abajo):** Alertas y recomendaciones - "¿Qué hacemos?"

### 4. Actualizaciones

🔄 **Mantener datos frescos:**
- Configura actualización automática del CSV
- Añade marca de tiempo de última actualización
- Documenta frecuencia de actualización esperada

### 5. Accesibilidad

♿ **Hacer el dashboard accesible:**
- Usa contraste adecuado de colores
- Agrega texto alternativo a visuales
- No dependas solo del color para comunicar (usa íconos también)
- Tamaños de fuente legibles

---

## 📤 Exportación y Compartir

### Opciones para Compartir

1. **Archivo .pbix**
   - Para edición completa
   - Compartir con otros usuarios de Power BI Desktop

2. **Publicar en Power BI Service**
   - Dashboard en la nube
   - Acceso vía navegador web
   - Requiere cuenta de Power BI (gratis o Pro)

3. **Exportar a PDF**
   - Para presentaciones estáticas
   - Archivo > Exportar > PDF

4. **Exportar a PowerPoint**
   - Para incluir en presentación oral
   - Archivo > Exportar > PowerPoint

5. **Captura de Pantalla**
   - Para documentación rápida
   - Usar herramienta de recortes de Windows

---

## 🎯 Checklist de Entrega

Antes de presentar tu dashboard, verifica:

- [ ] Todos los KPIs principales están visibles
- [ ] Gráficos tienen títulos descriptivos
- [ ] Colores son consistentes y temáticos
- [ ] Filtros funcionan correctamente
- [ ] No hay errores de carga de datos
- [ ] Texto es legible (sin sobreposición)
- [ ] Marca de última actualización visible
- [ ] Tooltips están configurados
- [ ] Dashboard cuenta una historia clara
- [ ] Formato de números es apropiado (monedas, porcentajes)
- [ ] Diseño es responsive (se ve bien en diferentes tamaños)
- [ ] Hay sección de productos con stock bajo destacada
- [ ] Logo o título de "Tienda Aurelion" visible
- [ ] Créditos/autor incluidos

---

## 📚 Recursos Adicionales

### Tutoriales de Power BI
- [Documentación oficial de Microsoft](https://docs.microsoft.com/power-bi/)
- [Power BI para principiantes (YouTube)](https://www.youtube.com/results?search_query=power+bi+tutorial+español)
- [DAX Patterns](https://www.daxpatterns.com/)

### Inspiración de Diseño
- [Power BI Community Gallery](https://community.powerbi.com/t5/Data-Stories-Gallery/bd-p/DataStoriesGallery)
- [Themes para Power BI](https://powerbi.tips/tools/report-theme-generator/)

### Paletas de Colores
- [Coolors.co](https://coolors.co/) - Generador de paletas
- [Color Hunt](https://colorhunt.co/) - Paletas pre-diseñadas
- [Adobe Color](https://color.adobe.com/) - Herramienta profesional

---

## 🎓 Ejemplo de Dashboard Completo

Para este proyecto, un dashboard exitoso incluiría:

### Página 1: Overview General
- 5 tarjetas de KPIs principales
- Gráfico de barras de categorías
- Gráfico de anillos de distribución
- Tabla de productos con stock bajo
- Filtros globales

### Página 2: Análisis de Productos (Opcional)
- Top 10 productos más valiosos
- Top 10 productos con más stock
- Gráfico de dispersión precio vs stock
- Análisis de rango de precios

### Página 3: Proveedores (Opcional)
- Análisis por proveedor
- Productos por proveedor
- Valor de inventario por proveedor
- Diversificación de categorías

### Página 4: Ventas y Clientes ⭐ NUEVO (Sprint 2)
- Tarjetas KPI de ventas (Total Ventas, Ingresos Totales, Ticket Promedio)
- Gráfico de línea: Evolución de ventas por fecha
- Top 5 productos más vendidos
- Tabla de ventas con información de clientes
- Análisis de clientes por ciudad
- Tabla de clientes con información de contacto

---

## 📈 Nuevas Visualizaciones Sprint 2 - Ventas y Clientes

### Visualizaciones de Ventas

#### 1. Tarjetas KPI de Ventas
**Métricas:**
- **Total de Ventas**: `COUNTROWS(Ventas)`
- **Ingresos Totales**: `SUM(Ventas[total])`
- **Ticket Promedio**: `AVERAGE(Ventas[total])`
- **Total Productos Vendidos**: `SUM(Detalle_Ventas[cantidad])`

#### 2. Gráfico de Línea: Evolución de Ventas
**Tipo:** Gráfico de línea con marcadores

**Configuración:**
- **Eje X:** `Ventas[fecha]`
- **Eje Y:** `SUM(Ventas[total])`
- **Leyenda:** (opcional) por categoría de producto
- **Marcadores:** Habilitados para mejor visualización

**Insights:**
- Tendencia de ventas en el tiempo
- Identificar días con mayores ventas
- Patrones estacionales

#### 3. Gráfico de Barras: Top 5 Productos Más Vendidos
**Tipo:** Gráfico de barras horizontales

**Configuración:**
- **Eje X:** `SUM(Detalle_Ventas[cantidad])`
- **Eje Y:** `Productos[nombre]`
- **Filtro:** Top 5 por cantidad
- **Color:** Gradiente según cantidad vendida

**Medida DAX:**
```dax
Cantidad Vendida por Producto = SUM(Detalle_Ventas[cantidad])
```

#### 4. Tabla de Ventas Detallada
**Columnas:**
- `Ventas[id_venta]`
- `Ventas[fecha]`
- `Ventas[total]`
- `Clientes[nombre]` (usando relación)
- `Clientes[ciudad]`

**Formato condicional:**
- Ventas altas (>2000) en verde
- Ventas medias en amarillo
- Ventas bajas en rojo

### Visualizaciones de Clientes

#### 5. Tarjeta KPI: Total de Clientes
**Medida DAX:**
```dax
Total Clientes = COUNTROWS(Clientes)
```

#### 6. Gráfico de Barras: Clientes por Ciudad
**Tipo:** Gráfico de barras

**Configuración:**
- **Eje X:** `Clientes[ciudad]`
- **Eje Y:** `COUNT(Clientes[id])`
- **Ordenar por:** Cantidad descendente

#### 7. Tabla de Clientes
**Columnas:**
- `nombre`
- `email`
- `telefono`
- `ciudad`
- `fecha_registro`

**Formato condicional:**
- Clientes nuevos (último mes) destacados

### Filtros y Slicers para Ventas y Clientes

**Slicers recomendados:**
- **Rango de fechas** (Ventas) - Tipo: Date range
- **Ciudad** (Clientes) - Tipo: Lista
- **Categoría de producto** - Tipo: Lista
- **Cliente** - Tipo: Dropdown

---

## 🔗 Medidas DAX Adicionales (Sprint 2)

Usa las medidas del archivo `Power BI/measures.dax` actualizado que incluye:

### Medidas de Ventas:
- `Total Ventas`
- `Ingresos Totales`
- `Promedio Venta`
- `Ticket Promedio`
- `Total Productos Vendidos`

### Medidas de Clientes:
- `Total Clientes`
- `Clientes Nuevos`
- `Cliente con Más Compras`

### Medidas Combinadas:
- `Productos Más Vendidos`
- `Ingresos por Categoría`
- `Rotación Inventario`

---

**¡Buena suerte con tu dashboard de Power BI para Tienda Aurelion! ⚔️📊**

Este dashboard no solo mostrará los datos, sino que contará la historia del inventario y ayudará en la toma de decisiones estratégicas para la tienda.

---

**👨‍💻 Autor:** Martos Ludmila  
**📋 DNI:** 34811650  
**🏢 Institución:** IBM  
**📅 Sprint:** 2 - Introducción a la Inteligencia Artificial  
**📆 Año:** 2025

